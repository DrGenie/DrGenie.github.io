from pathlib import Path
from datetime import datetime, timezone
from html import escape
import json

root=Path(__file__).resolve().parents[1]
data=root/'assets'/'data'
gen=root/'assets'/'generated'
gen.mkdir(parents=True,exist_ok=True)
today=datetime.now(timezone.utc).date().isoformat()
(data/'build-info.json').write_text(json.dumps({'last_updated':today},indent=2)+'\n',encoding='utf-8')

pubs=json.loads((data/'publications.json').read_text(encoding='utf-8'))
tools=json.loads((data/'tools.json').read_text(encoding='utf-8'))
supervision=json.loads((data/'supervision.json').read_text(encoding='utf-8'))

def e(v):return escape(str(v or ''),quote=True)

def status_for(p):
    t=p.get('type','')
    if t=='Working paper':return 'Working paper'
    if t=='Data output':return 'Published data'
    if t=='Book chapter':return 'Published'
    return p.get('status') or 'Published'

journal_count=sum(1 for p in pubs if p.get('type')=='Journal article')
live_tools=sum(1 for t in tools if t.get('status')=='Live')
current_supervision=sum(1 for s in supervision if s.get('status')=='Current')
metrics=f"""<div class=\"credibility-band\" aria-label=\"Selected verified profile indicators\"><div class=\"credibility-inner\"><div class=\"credibility-item\"><strong>{journal_count}</strong> peer-reviewed journal articles</div><div class=\"credibility-item\"><strong>A$4.75m</strong> multi-institution MandEval programme</div><div class=\"credibility-item\"><strong>{live_tools}</strong> live decision tools</div><div class=\"credibility-item\"><strong>{current_supervision}</strong> current research supervisions</div></div></div>"""
(gen/'evidence-strip.html').write_text(metrics+'\n',encoding='utf-8')

featured=[p for p in pubs if p.get('featured_home')]
featured=sorted(featured,key=lambda x:(x.get('year',0),x.get('title','')),reverse=True)[:3]
items=[]
for p in featured:
    journal=', '.join(x for x in [p.get('journal',''),p.get('citation_detail','')] if x)
    items.append(f"""<li><div class=\"meta\">{e(journal)} · {e(p.get('year'))}</div><h3><a href=\"{e(p.get('url'))}\" target=\"_blank\" rel=\"noopener noreferrer\">{e(p.get('title'))}</a></h3><p class=\"authors\">{p.get('authors_html','')}</p><p><span class=\"status\">{e(status_for(p))}</span> <a href=\"{e(p.get('doi_url') or p.get('url'))}\" target=\"_blank\" rel=\"noopener noreferrer\">DOI or publisher ↗</a></p></li>""")
(gen/'recent-publications.html').write_text('<ul class="compact-list">'+''.join(items)+'</ul>\n',encoding='utf-8')

# Full publications grouped in compact details sections
years=sorted({int(p['year']) for p in pubs},reverse=True)
out=[]
for i,y in enumerate(years):
    rows=[p for p in pubs if int(p['year'])==y]
    out.append(f'<details class="pub-year" data-default-open="{str(i==0).lower()}"'+(' open' if i==0 else '')+f'><summary><span>{y}</span><span class="count-badge">{len(rows)} outputs</span></summary><div>')
    for p in rows:
        journal=', '.join(x for x in [p.get('journal',''),p.get('citation_detail','')] if x)
        link=p.get('url') or p.get('doi_url') or '#'
        doi=p.get('doi_url') or p.get('url')
        source_label='DOI' if p.get('doi') else 'Source'
        earlier=''
        if p.get('earlier'):
            earlier=' '.join(f'<a href="{e(u)}" target="_blank" rel="noopener noreferrer">Earlier version ↗</a>' for u in p['earlier'])
        out.append(f"""<article class=\"publication-record\" data-year=\"{e(p.get('year'))}\" data-theme=\"{e(p.get('theme'))}\" data-type=\"{e(p.get('type'))}\"><div class=\"meta\">{e(p.get('type'))} · {e(p.get('theme'))}</div><h3><a href=\"{e(link)}\" target=\"_blank\" rel=\"noopener noreferrer\">{e(p.get('title'))}</a></h3><p class=\"authors\">{p.get('authors_html','')}</p><p class=\"citation\">{e(journal)}</p><p><span class=\"status\">{e(status_for(p))}</span> <a href=\"{e(doi)}\" target=\"_blank\" rel=\"noopener noreferrer\">{source_label} ↗</a>{(' · '+earlier) if earlier else ''}</p></article>""")
    out.append('</div></details>')
(gen/'publications-list.html').write_text('\n'.join(out)+'\n',encoding='utf-8')

paths=['/','/about/','/research/','/research/projects/mandeval/','/research/projects/world-bank-fetp/','/research/projects/eye-tracking-choice/','/research/projects/decision-tools/','/publications/','/tools/','/tools/emandelval-future/','/tools/soil-crc-bca-tool/','/teaching/','/teaching/behavioural-economics/','/supervision/','/talks-media/','/conferences/','/blog/','/cv/','/contact/']
for post in sorted((root/'blog'/'posts').glob('*/index.qmd')):
    paths.append('/blog/posts/'+post.parent.name+'/')
xml=['<?xml version="1.0" encoding="UTF-8"?>','<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for path in paths:xml.append(f'  <url><loc>https://mesfingenie.com{path}</loc><lastmod>{today}</lastmod></url>')
xml.append('</urlset>')
(root/'sitemap.xml').write_text('\n'.join(xml)+'\n',encoding='utf-8')
