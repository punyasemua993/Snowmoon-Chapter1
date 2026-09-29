from pathlib import Path
import hashlib
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'08-manifests'/'SHA256SUMS.txt'
rows=[]
for p in sorted(ROOT.rglob('*')):
    if p.is_file() and p.name!='SHA256SUMS.txt':
        rows.append(f"{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.relative_to(ROOT).as_posix()}")
OUT.write_text('\n'.join(rows)+'\n',encoding='utf-8')
print(OUT)
