from pathlib import Path
import json, datetime
root=Path(__file__).resolve().parents[1]
today=datetime.datetime.now(datetime.timezone.utc).date().isoformat()
(root/'assets/build-info.json').write_text(json.dumps({'last_updated':today},indent=2)+'\n')
urls=['','research/','publications/','conferences/','tools/','teaching/','cv/']
xml=['<?xml version="1.0" encoding="UTF-8"?>','<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for u in urls: xml.append(f'  <url><loc>https://mesfingenie.com/{u}</loc><lastmod>{today}</lastmod></url>')
xml.append('</urlset>')
(root/'sitemap.xml').write_text('\n'.join(xml)+'\n')
