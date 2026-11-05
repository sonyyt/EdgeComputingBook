#!/usr/bin/env python3
"""Check complete-book coverage, preserved text, local links, image hashes, math and code."""
from __future__ import annotations
import argparse,hashlib,json,re,sys
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit,unquote

class Page(HTMLParser):
    def __init__(self,text):
        super().__init__(convert_charrefs=True);self.stack=[];self.text=[];self.ids=set();self.links=[];self.images=[];self.math=[];self.code=0;self.tables=0
        self.feed(text)
    def handle_starttag(self,tag,attrs):
        d=dict(attrs);classes=d.get('class','').split();parent=self.stack[-1] if self.stack else (None,False,False,False)
        main=parent[1] or d.get('itemprop')=='articleBody'
        skip=parent[2] or tag in ('script','style') or 'headerlink' in classes or 'math' in classes
        math=parent[3] or 'math' in classes
        if d.get('id'):self.ids.add(d['id'])
        for key in ('href','src'):
            if key in d:self.links.append(d[key])
        if main:
            if tag=='img':self.images.append(d)
            if 'math' in classes:self.math.append(d)
            if tag=='pre':self.code+=1
            if tag=='table':self.tables+=1
        if main and tag in ('p','br','div','li','h1','h2','h3','h4','h5','td','th','tr','pre'):self.text.append(' ')
        if tag not in ('area','base','br','col','embed','hr','img','input','link','meta','param','source','track','wbr'):self.stack.append((tag,main,skip,math))
    def handle_endtag(self,tag):
        if self.stack and self.stack[-1][1] and tag in ('p','div','li','h1','h2','h3','h4','h5','td','th','tr','pre'):self.text.append(' ')
        for i in range(len(self.stack)-1,-1,-1):
            if self.stack[i][0]==tag: del self.stack[i:];break
    def handle_data(self,data):
        if self.stack and self.stack[-1][1] and not self.stack[-1][2]:self.text.append(data)

def normalize(s):return re.sub(r'\s+',' ',s).strip()
def compact(s):return re.sub(r'\s+','',s)

def main():
    p=argparse.ArgumentParser();p.add_argument('site',type=Path);p.add_argument('--report',type=Path,default=Path('VALIDATION_REPORT.json'));a=p.parse_args()
    root=Path(__file__).resolve().parent.parent;site=a.site.resolve();manifest=json.loads((root/'SOURCE_MANIFEST.json').read_text());expected=json.loads((root/'tools/expected_content.json').read_text())
    pages={f.resolve():Page(f.read_text()) for f in site.rglob('*.html')};errors=[];checks=Counter();coverage=[]
    for page,expect in expected.items():
        html=(site/Path(page).with_suffix('.html')).resolve()
        if html not in pages:errors.append('Missing '+str(html));continue
        doc=pages[html];text=normalize(''.join(doc.text));textcompact=compact(text)
        for kind in ('paragraphs','table_cells'):
            for entry in expect[kind]:
                if not entry:continue
                checks[kind]+=1
                if compact(entry) not in textcompact:errors.append(f'{page}: missing {kind}: {entry[:220]}')
        stats=next(x for x in manifest['pages'] if x['path']==page)
        for key,actual in [('images',len(doc.images)),('math',len(doc.math)),('tables',doc.tables),('code_blocks',doc.code)]:
            checks[key]+=actual
            if actual!=stats[key]:errors.append(f'{page}: {key} {actual} != {stats[key]}')
        coverage.append({'page':page,'paragraphs':len(expect['paragraphs']),'table_cells':len(expect['table_cells']),'images':len(doc.images),'math':len(doc.math),'tables':doc.tables,'code_blocks':doc.code})
    for path,page in pages.items():
        for href in page.links:
            u=urlsplit(href)
            if u.scheme or u.netloc or href.startswith('mailto:'):continue
            target=(path.parent/unquote(u.path)).resolve() if u.path else path
            if target.is_dir():target=target/'index.html'
            checks['local_links_assets']+=1
            if not target.exists():errors.append(f'{path.relative_to(site)} broken {href}')
            elif u.fragment and target in pages and unquote(u.fragment) not in pages[target].ids:errors.append(f'{path.relative_to(site)} broken anchor {href}')
    for image in manifest['images']:
        f=root/'docs/images'/image['file'];checks['source_image_hashes']+=1
        if hashlib.sha256(f.read_bytes()).hexdigest()!=image['sha256']:errors.append('Image hash mismatch '+image['file'])
    ref=pages[site/'references.html']
    for i in range(1,212):
        checks['reference_labels']+=1
        if f'ref-{i}' not in ref.ids:errors.append('Missing reference '+str(i))
    for fig in manifest['figures']:
        page=pages[site/f'chapters/ch{int(fig.split(".")[0]):02d}.html'];checks['figure_labels']+=1
        if 'fig-'+fig.replace('.','-') not in page.ids:errors.append('Missing figure '+fig)
    if len(list((root/'docs/chapters').glob('ch*.md')))!=14:errors.append('Chapter count')
    if len(list((root/'docs/appendices').glob('*.md')))!=5:errors.append('Appendix count')
    report={'status':'passed' if not errors else 'failed','html_pages':len(pages),'checks':dict(checks),'coverage':coverage,'errors':errors,'scope':'Rendered normalized prose/table-cell inclusion, exact source image hashes, structural counts and local anchors. Browser behavior and scientific correctness are separate checks.'}
    a.report.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({k:v for k,v in report.items() if k!='coverage'},indent=2));sys.exit(bool(errors))

if __name__=='__main__':main()
