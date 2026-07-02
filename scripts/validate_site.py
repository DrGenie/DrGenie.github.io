from pathlib import Path
import json, re, sys
root=Path(__file__).resolve().parents[1]
errors=[]
for q in root.rglob('*.qmd'):
    txt=q.read_text(encoding='utf-8')
    if 'title: false' in txt: errors.append(f'{q}: contains title: false')
    if txt.count('<h1') + len(re.findall(r'^# ', txt, re.M)) > 1: errors.append(f'{q}: possible duplicate H1')
json.loads((root/'assets/data/publications.json').read_text(encoding='utf-8'))
for p in json.loads((root/'assets/data/publications.json').read_text(encoding='utf-8')):
    if p.get('doi') and not re.match(r'^10\.\S+/.+', p['doi']): errors.append(f"bad DOI: {p.get('title')}")
required=['_quarto.yml','CNAME','robots.txt','sitemap.xml','assets/css/site.css','assets/js/site.js','cv/mesfin-genie-cv.pdf']
for r in required:
    if not (root/r).exists(): errors.append(f'missing {r}')
if errors:
    print('\n'.join(errors)); sys.exit(1)
print('Validation checks passed.')
