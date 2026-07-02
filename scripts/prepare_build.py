from pathlib import Path
from datetime import datetime, timezone
import json
root=Path(__file__).resolve().parents[1]
today=datetime.now(timezone.utc).date().isoformat()
(root/'assets'/'data').mkdir(parents=True, exist_ok=True)
(root/'assets'/'data'/'build-info.json').write_text(json.dumps({'last_updated':today}, indent=2)+'\n', encoding='utf-8')
paths=['/','/about/','/research/','/publications/','/tools/','/teaching/','/teaching/behavioural-economics/','/supervision/','/talks-media/','/blog/','/cv/','/contact/']
xml=['<?xml version="1.0" encoding="UTF-8"?>','<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for p in paths:
    xml.append(f'  <url><loc>https://mesfingenie.com{p}</loc><lastmod>{today}</lastmod></url>')
xml.append('</urlset>')
(root/'sitemap.xml').write_text('\n'.join(xml)+'\n', encoding='utf-8')
