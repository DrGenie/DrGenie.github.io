from pathlib import Path
import json,re,sys
root=Path(__file__).resolve().parents[1]
errors=[]
qmd=list(root.rglob('*.qmd'))
for q in qmd:
    txt=q.read_text(encoding='utf-8')
    if 'title: false' in txt: errors.append(f'{q}: contains title: false')
    if 'Pending source upload' in txt: errors.append(f'{q}: contains placeholder status')
    h1=len(re.findall(r'<h1(?:\s|>)',txt,re.I))+len(re.findall(r'^#\s+',txt,re.M))
    if h1>1: errors.append(f'{q}: contains {h1} H1 headings')
for name in ['profile','publications','grants','courses','supervision','talks','tools']:
    json.loads((root/'assets/data'/f'{name}.json').read_text(encoding='utf-8'))
pubs=json.loads((root/'assets/data/publications.json').read_text(encoding='utf-8'))
seen_doi={};seen_title={}
for p in pubs:
    doi=p.get('doi','').strip()
    if doi and not re.match(r'^10\.\S+/.+',doi):errors.append(f"Bad DOI: {p.get('title')}")
    if doi and doi.lower() in seen_doi:errors.append(f"Duplicate DOI: {doi}")
    if doi:seen_doi[doi.lower()]=1
    title=re.sub(r'\W+','',p.get('title','').lower())
    if title in seen_title:errors.append(f"Duplicate title: {p.get('title')}")
    seen_title[title]=1
required=['_quarto.yml','CNAME','robots.txt','sitemap.xml','assets/css/site.css','assets/js/site.js','assets/body-start.html','assets/generated/publications-list.html','cv/mesfin-genie-cv.pdf']
for r in required:
    if not (root/r).exists():errors.append(f'Missing {r}')
if (root/'tools/steps-decision-aid').exists():errors.append('Obsolete public STEPS placeholder remains')
if errors:
    print('\n'.join(errors));sys.exit(1)
print(f'Validation checks passed for {len(qmd)} Quarto pages and {len(pubs)} publication records.')
