#!/usr/bin/env python3
"""One-time branch-only package import. No private key or signed URL is published."""
from pathlib import Path, PurePosixPath
import base64, hashlib, io, json, os, subprocess, sys, time, urllib.request, urllib.error, urllib.parse, zipfile
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
TMP = Path(os.environ['RUNNER_TEMP'])
PRIVATE = TMP / 'book-transfer-private.pem'
PUBLIC = TMP / 'book-transfer-public.pem'
BRANCH = 'full-book-v042'
def key():
    k = rsa.generate_private_key(public_exponent=65537, key_size=3072)
    PRIVATE.write_bytes(k.private_bytes(serialization.Encoding.PEM, serialization.PrivateFormat.PKCS8, serialization.NoEncryption()))
    PRIVATE.chmod(0o600)
    PUBLIC.write_bytes(k.public_key().public_bytes(serialization.Encoding.PEM, serialization.PublicFormat.SubjectPublicKeyInfo))
    print('Ephemeral public transfer key prepared; private key remains on this runner.')
def load_payload(fingerprint):
    repo = os.environ['GITHUB_REPOSITORY']
    api = f'https://api.github.com/repos/{repo}/contents/.migration/full-book-transfer.json?ref={BRANCH}'
    headers = {'Authorization': 'Bearer '+os.environ['GH_TOKEN'], 'Accept': 'application/vnd.github+json', 'X-GitHub-Api-Version': '2022-11-28'}
    deadline = time.monotonic() + 1000
    while time.monotonic() < deadline:
        try:
            with urllib.request.urlopen(urllib.request.Request(api, headers=headers), timeout=25) as response:
                body = json.load(response)
            payload = json.loads(base64.b64decode(body['content']))
            if payload.get('key_fingerprint') == fingerprint:
                return payload
        except (urllib.error.HTTPError, urllib.error.URLError, KeyError, ValueError):
            pass
        time.sleep(8)
    raise RuntimeError('No encrypted package handoff for this ephemeral key arrived.')
def run_import():
    if os.environ.get('GITHUB_REF') != 'refs/heads/'+BRANCH:
        raise RuntimeError('This importer is restricted to the migration branch.')
    fp = hashlib.sha256(PUBLIC.read_bytes()).hexdigest()
    payload = load_payload(fp)
    k = serialization.load_pem_private_key(PRIVATE.read_bytes(), password=None)
    aes_key = k.decrypt(base64.b64decode(payload['encrypted_key']), padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None))
    data = json.loads(AESGCM(aes_key).decrypt(base64.b64decode(payload['nonce']), base64.b64decode(payload['ciphertext']), fp.encode()))
    expected = os.environ['EXPECTED_PACKAGE_SHA256']
    if data.get('sha256') != expected:
        raise RuntimeError('Package fingerprint is not the approved fingerprint.')
    url = data['url']; parsed = urllib.parse.urlsplit(url)
    if parsed.scheme != 'https' or not (parsed.hostname or '').endswith('.oaiusercontent.com'):
        raise RuntimeError('Unexpected package transfer host.')
    try:
        with urllib.request.urlopen(url, timeout=120) as response:
            package = response.read(60000001)
    except Exception:
        raise RuntimeError('Package transfer failed; signed address omitted from logs.') from None
    if len(package)>60000000 or hashlib.sha256(package).hexdigest()!=expected:
        raise RuntimeError('Package size or SHA-256 validation failed.')
    subprocess.run(['git','fetch','origin',BRANCH],check=True)
    subprocess.run(['git','merge','--ff-only','origin/'+BRANCH],check=True)
    allowed_top={'README.md','.gitignore','requirements.txt','requirements-conversion.txt','SOURCE_MANIFEST.json','VALIDATION_REPORT.json','MIGRATION_REPORT.md'}
    allowed_tools={'tools/convert_docx.py','tools/check_site.py','tools/expected_content.json','tools/BROWSER_CHECK.json'}
    with zipfile.ZipFile(io.BytesIO(package)) as z:
        if sum(i.file_size for i in z.infolist())>90000000:
            raise RuntimeError('Uncompressed package exceeds limit.')
        for info in z.infolist():
            p=PurePosixPath(info.filename)
            if info.is_dir():continue
            if p.is_absolute() or '..' in p.parts or '\\' in info.filename or (info.external_attr>>16)&0o170000==0o120000:
                raise RuntimeError('Unsafe archive member.')
            if not (p.parts[0]=='docs' or str(p) in allowed_top or str(p) in allowed_tools):
                raise RuntimeError('Archive member outside approved textbook paths: '+str(p))
            dest=Path(*p.parts);dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(z.read(info))
    for old in ('docs/sample.md','docs/contents.md'):
        Path(old).unlink(missing_ok=True)
    PRIVATE.unlink(missing_ok=True)
    print('Complete source package imported with matching SHA-256; no deployment performed.')
if __name__=='__main__':
    if sys.argv[1]=='key':key()
    elif sys.argv[1]=='import':run_import()
    else:raise SystemExit('Expected key or import')
