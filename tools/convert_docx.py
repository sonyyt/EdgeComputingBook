#!/usr/bin/env python3
"""Loss-conscious DOCX -> MyST/Sphinx conversion for Edge Computing Systems v0.4.2.
No paraphrasing. Pandoc reads Office Math and hyperlinks; this writer adds web structure.
"""
from __future__ import annotations
import argparse, collections, copy, hashlib, json, re, shutil, subprocess, sys
from pathlib import Path
from zipfile import ZipFile
from lxml import etree as ET

NS={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main','m':'http://schemas.openxmlformats.org/officeDocument/2006/math','a':'http://schemas.openxmlformats.org/drawingml/2006/main'}

def walk(n):
    if isinstance(n,dict):
        if 't' in n: yield n
        for v in n.values(): yield from walk(v)
    elif isinstance(n,list):
        for v in n: yield from walk(v)

def plain(n, math=True, image_alt=False):
    if isinstance(n,list): return ''.join(plain(v,math,image_alt) for v in n)
    if not isinstance(n,dict): return ''
    t=n['t']; c=n.get('c',[])
    if t=='Str': return c
    if t in ('Space','SoftBreak'): return ' '
    if t=='LineBreak': return '\n'
    if t=='Math': return c[1] if math else ''
    if t=='Image': return plain(c[1],math,image_alt) if image_alt else ''
    if t in ('Link','Span'): return plain(c[1],math,image_alt)
    if t=='Header': return plain(c[2],math,image_alt)
    if t=='Code': return c[1]
    return plain(c,math,image_alt)

def norm(s): return re.sub(r'\s+',' ',s).strip()
def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def sid(num):return 'section-'+num.replace('.','-')
def fid(num):return 'fig-'+num.replace('.','-')

class Converter:
    def __init__(self,source,out,work):
        self.source=source;self.out=out;self.work=work
        self.out.mkdir(parents=True,exist_ok=True)
        self.docs=out/'docs';self.docs.mkdir(exist_ok=True)
        (self.docs/'chapters').mkdir(exist_ok=True);(self.docs/'appendices').mkdir(exist_ok=True);(self.docs/'images').mkdir(exist_ok=True)
        self.work.mkdir(parents=True,exist_ok=True)
        subprocess.run(['pandoc',str(source),'-t','json','--extract-media='+str(work/'assets'),'-o',str(work/'book.json')],check=True)
        self.data=json.loads((work/'book.json').read_text())
        self.blocks=self.data['blocks'];self.codes={};self.raw_code=[]
        with ZipFile(source) as z:
            self.xml=ET.fromstring(z.read('word/document.xml'))
            for p in self.xml.findall('.//w:p',NS):
                s=p.find('w:pPr/w:pStyle',NS)
                if s is not None and s.get('{'+NS['w']+'}val')=='SourceCode':
                    text=''
                    for el in p.iter():
                        if el.tag=='{'+NS['w']+'}t':text+=el.text or ''
                        elif el.tag=='{'+NS['w']+'}br':text+='\n'
                        elif el.tag=='{'+NS['w']+'}tab':text+='\t'
                    self.codes[norm(text)]=text;self.raw_code.append(text)
        self.parts=[];self.pages=[];self.labels={};self.figure_ids=[];self.expected={};self.image_map={};self.records=[];self.maths=[];self.used_codes=[]
        self.protected={};self.depth=0;self.tables=0;self.counter=collections.Counter();self.current=''

    def add_page(self,title,blocks,path,label):
        self.pages.append({'title':title,'blocks':blocks,'path':path,'label':label})

    def organize(self):
        start=next(i for i,b in enumerate(self.blocks) if b['t']=='Header' and plain(b)=='Preface')
        current=[];title=None;path=None;label=None
        for b in self.blocks[start:]:
            text=norm(plain(b))
            if re.match(r'^Part [IVX]+\. ',text):
                self.parts.append(text);continue
            if b['t']=='Header' and b['c'][0]==1:
                if title is not None:self.add_page(title,current,path,label)
                title=text;current=[b]
                if title=='Preface':path='preface.md';label='preface'
                elif (m:=re.match(r'Chapter (\d+)\.',title)):
                    n=int(m[1]);path=f'chapters/ch{n:02d}.md';label=f'chapter-{n}'
                elif (m:=re.match(r'Appendix ([A-E])\.',title)):
                    path=f'appendices/appendix-{m[1].lower()}.md';label=f'appendix-{m[1].lower()}'
                else:path='references.md';label='references'
            elif title is not None:current.append(b)
        if title is not None:self.add_page(title,current,path,label)
        for page in self.pages:
            for b in page['blocks']:
                if b['t']=='Header':
                    old=b['c'][1][0];tx=norm(plain(b))
                    m=re.match(r'^(\d+\.\d+(?:\.\d+)*)\s',tx)
                    if b['c'][0]==1:lab=page['label']
                    elif m:lab=sid(m[1])
                    else:lab=page['label']+'-'+re.sub('[^a-z0-9]+','-',tx.lower()).strip('-')
                    self.labels[old]=lab;b['_label']=lab
        self.all_labels=set(self.labels.values())
        for page in self.pages:
            for b in page['blocks']:
                text=norm(plain(b))
                if m:=re.match(r'^Figure (\d+\.\d+)\.',text):
                    self.figure_ids.append(m[1]);self.all_labels.add(fid(m[1]));b['_figure']=m[1]
                if page['label']=='references' and (m:=re.match(r'^\[(\d+)\]',text)):
                    b['_ref']=int(m[1]);self.all_labels.add('ref-'+m[1])
        assert len(self.figure_ids)==156 and len(set(self.figure_ids))==156
        assert sum(bool(b.get('_ref')) for p in self.pages for b in p['blocks'])==211

    def refs(self,s):
        def cite(m):
            if any(not (1<=int(x)<=211) for x in re.findall(r'\d+',m[1])):return m[0]
            if m[2] and not re.match(r',?\s*(Table|Section|Figure) ',m[2]):return m[0]
            a=re.sub(r'\d+',lambda x:'{ref}`'+x[0]+' <ref-'+x[0]+'>`',m[1])
            return '['+a+m[2]+']'
        s=re.sub(r'\[(\d+(?:\s*[,–-]\s*\d+)*)([^\]\n]*)\](?!\()',cite,s)
        def ref(m):
            kind,num=m[1],m[2]
            lab={'Figure':fid(num),'Section':sid(num),'Chapter':'chapter-'+num,'Table':'table-'+num.replace('.','-')}[kind]
            return '{ref}`'+m[0]+' <'+lab+'>`' if lab in self.all_labels else m[0]
        return re.sub(r'\b(Figure|Section|Chapter|Table) (\d+(?:\.\d+)*)(?![\d.])',ref,s)

    def esc(self,s):
        return re.sub(r'([\\`*_$<>|])',r'\\\1',s)

    def image(self,n):
        src=n['c'][2][0];old=Path(src)
        if src not in self.image_map:
            target='asset-'+hashlib.sha256(old.read_bytes()).hexdigest()[:16]+old.suffix.lower()
            shutil.copyfile(old,self.docs/'images'/target)
            self.image_map[src]=target
        rel=('../' if '/' in self.current else '')+'images/'+self.image_map[src]
        alt=norm(plain(n['c'][1])) or n['c'][2][1] or 'Textbook illustration'
        self.records.append({'page':self.current,'file':self.image_map[src],'source_media':old.name,'sha256':sha(old),'alt':alt})
        return '!['+alt.replace('[','\\[').replace(']','\\]')+']('+rel+')'

    def protect(self,s):
        key='@@SAFE'+str(len(self.protected))+'@@';self.protected[key]=s;return key

    def inline(self,nodes,link_refs=True):
        self.depth+=1
        result=[]
        for n in nodes:
            t=n['t'];c=n.get('c',[])
            if t=='Str':result.append(self.esc(c))
            elif t=='Space':result.append(' ')
            elif t in ('LineBreak','SoftBreak'):result.append('<br>\n' if t=='LineBreak' else ' ')
            elif t in ('Strong','Emph'):
                mark='**' if t=='Strong' else '*';result.append(mark+self.inline(c,False)+mark)
            elif t=='Underline': result.append(self.inline(c,False))
            elif t=='Span': result.append(self.inline(c[1],False))
            elif t=='Image':result.append(self.protect(self.image(n)))
            elif t=='Math':
                self.maths.append({'page':self.current,'type':c[0]['t'],'tex':c[1]})
                result.append(self.protect(('\n\n$$\n'+c[1]+'\n$$\n\n') if c[0]['t']=='DisplayMath' else '$'+c[1]+'$'))
            elif t=='Link':
                target=c[2][0];label=self.inline(c[1],False)
                if target.startswith('#') and target[1:] in self.labels:result.append('{ref}`'+plain(c[1])+' <'+self.labels[target[1:]]+'>`')
                else:result.append(self.protect('['+label+']('+target.replace(' ','%20')+')'))
            elif t=='Code':result.append(self.protect('`'+c[1]+'`'))
            else:raise ValueError('Unhandled inline '+t)
        s=''.join(result)
        s=self.refs(s) if link_refs else s
        self.depth-=1
        if self.depth==0:
            while re.search(r'@@SAFE\d+@@',s):s=re.sub(r'@@SAFE\d+@@',lambda m:self.protected[m[0]],s)
        return s

    def table(self,b):
        self.tables+=1;c=b['c'];rows=c[3][1][:]
        for body in c[4]: rows+=body[2]+body[3]
        rows+=c[5][1]
        cols=len(c[2]);out=['```{list-table}', ':header-rows: '+str(len(c[3][1])), ':class: book-table', '']
        for row in rows:
            cells=row[1];entries=[]
            for cell in cells:
                assert cell[2]==1, 'Unsupported row span'
                parts=[]
                for x in cell[4]:
                    assert x['t'] in ('Para','Plain'), x['t']
                    parts.append(self.inline(x['c']).replace('\n',' '))
                entries.append('<br><br>'.join(parts))
                for _ in range(cell[3]-1):entries.append('')
            assert len(entries)==cols,(len(entries),cols)
            for i,entry in enumerate(entries):out.append((' * - ' if i==0 else '   - ')+entry)
        out+=['```',''];return '\n'.join(out)

    def render(self,b):
        t=b['t'];self.counter[t]+=1
        if t=='Header':
            return '('+b['_label']+')=\n\n'+'#'*b['c'][0]+' '+self.inline(b['c'][2],False)+'\n\n'
        if t=='Table':return self.table(b)+'\n'
        if t not in ('Para','Plain'):raise ValueError('Unhandled block '+t)
        txt=norm(plain(b));code=self.codes.get(txt)
        if code is not None:
            self.used_codes.append(code)
            lang='json' if code.lstrip().startswith('{') else 'text'
            if code.startswith('apiVersion:'):lang='yaml'
            elif code.startswith('FROM '):lang='dockerfile'
            elif code.startswith('python ') or code.startswith('docker ') or 'docker ' in code[:130] or code.startswith('# Optional:'):lang='bash'
            elif code.startswith('result = ') or 'while task.can_continue' in code:lang='python'
            return '```'+lang+'\n'+code+'\n```\n\n'
        prefix=''
        if b.get('_figure'):prefix='('+fid(b['_figure'])+')=\n\n'
        if b.get('_ref'):prefix='(ref-'+str(b['_ref'])+')=\n\n'
        if m:=re.match(r'^Table (\d+\.\d+)\. ',txt):prefix='(table-'+m[1].replace('.','-')+')=\n\n'
        s=self.inline(b['c'],not bool(b.get('_ref')))
        # Preserve the caption identifier without making the caption a self-link.
        if b.get('_figure'):
            n=b['_figure'];s=s.replace('{ref}`Figure '+n+' <'+fid(n)+'>`','Figure '+n)
        return prefix+s+'\n\n'

    def run(self):
        self.organize()
        for p in self.pages:
            for b in p['blocks']:
                if m:=re.match(r'^Table (\d+\.\d+)\. ',norm(plain(b))):self.all_labels.add('table-'+m[1].replace('.','-'))
        coverage=[]
        for page in self.pages:
            self.current=page['path'];before_images=len(self.records);before_math=len(self.maths);before_tables=self.tables;before_codes=len(self.used_codes)
            text=''.join(self.render(b) for b in page['blocks'])
            (self.docs/page['path']).write_text(text,encoding='utf-8')
            # A block-level record permits exact normalized visible-text comparison after rendering.
            expectations=[norm(plain(b,False)) for b in page['blocks'] if b['t']!='Table']
            table_cells=[]
            for b in page['blocks']:
                if b['t']=='Table':
                    for n in walk(b):
                        if n['t'] in ('Para','Plain'):table_cells.append(norm(plain(n,False)))
            self.expected[page['path']]={'paragraphs':expectations,'table_cells':table_cells}
            coverage.append({'path':page['path'],'title':page['title'],'source_blocks':len(page['blocks']),'images':len(self.records)-before_images,'math':len(self.maths)-before_math,'tables':self.tables-before_tables,'code_blocks':len(self.used_codes)-before_codes,'characters':sum(len(x) for x in expectations+table_cells)})
        assert len(self.pages)==21
        assert len(self.records)==159,len(self.records)
        assert len(self.maths)==80,len(self.maths)
        assert self.tables==48,self.tables
        assert len(self.used_codes)==18,(len(self.used_codes),len(self.codes))
        assert collections.Counter(self.raw_code)==collections.Counter(self.used_codes)
        manifest={'version':'0.4.2','source_file':self.source.name,'source_sha256':sha(self.source),'conversion':'Pandoc DOCX reader and custom MyST writer; original text, numbering, equations, tables, figures, captions, references and credits retained. No substantive rewriting.','pages':coverage,'totals':{'chapters':14,'appendices':5,'content_pages':21,'numbered_figures':156,'embedded_image_occurrences':159,'unique_image_files':len(set(self.image_map.values())),'tables_including_photo_layouts':48,'office_math_objects':80,'source_code_blocks':18,'references':211},'figures':self.figure_ids,'images':self.records,'math':self.maths,'limitations':['Original photograph permission caveats remain; conversion is not publication-rights clearance.','Laboratory code archives were not supplied as part of the current DOCX migration; no tests or deployments of teaching systems are claimed.','Printed cover and page-number table of contents replaced by web navigation. Original manual chapter and figure numbers retained.','Word underlining is represented as normal text; bold and italic emphasis are retained.']}
        (self.out/'SOURCE_MANIFEST.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
        (self.out/'tools').mkdir(exist_ok=True)
        (self.out/'tools'/'expected_content.json').write_text(json.dumps(self.expected,ensure_ascii=False,separators=(',',':'))+'\n')
        print(json.dumps(manifest['totals'],indent=2))
        self.make_index()
    def make_index(self):
        parts=[(self.parts[0],1,4),(self.parts[1],5,9),(self.parts[2],10,12),(self.parts[3],13,14)]
        text='# Edge Computing Systems\n\n## Building Intelligent Applications Across Devices, Edge, and Cloud\n\n**Zheng Song · English manuscript v0.4.2**\n\nThis web edition contains the complete English manuscript: all fourteen chapters, five appendices, references, and image credits. Chapter and figure numbers follow the manuscript.\n\n```{toctree}\n:maxdepth: 1\n:caption: About this book\n\npreface\npublication\n```\n\n'
        for title,start,end in parts:
            text+='```{toctree}\n:maxdepth: 2\n:caption: '+title+'\n\n'+'\n'.join('chapters/ch'+str(i).zfill(2) for i in range(start,end+1))+'\n```\n\n'
        text+='```{toctree}\n:maxdepth: 2\n:caption: Appendices and references\n\n'+'\n'.join('appendices/appendix-'+x for x in 'abcde')+'\nreferences\n```\n'
        (self.docs/'index.md').write_text(text)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('source',type=Path);p.add_argument('out',type=Path);p.add_argument('--work',type=Path,default=Path('_conversion'));a=p.parse_args()
    Converter(a.source.resolve(),a.out.resolve(),a.work.resolve()).run()
