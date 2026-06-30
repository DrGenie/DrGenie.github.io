from pathlib import Path
import json,re,sys,time
from datetime import datetime,timezone
import requests
from bs4 import BeautifulSoup
URL='https://scholar.google.com/citations?user=v2SXM_kAAAAJ&hl=en'
out=Path(__file__).resolve().parents[1]/'assets/scholar-metrics.json'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/124 Safari/537.36','Accept-Language':'en-US,en;q=0.9'}
try:
    time.sleep(2)
    r=requests.get(URL,headers=headers,timeout=30)
    r.raise_for_status()
    low=r.text.lower()
    if 'unusual traffic' in low or 'not a robot' in low: raise RuntimeError('Google Scholar rate-limited the request')
    soup=BeautifulSoup(r.text,'html.parser')
    name=soup.select_one('#gsc_prf_in') or soup.select_one('.gsc_prf_in')
    if not name or 'Mesfin' not in name.get_text(' ',strip=True): raise RuntimeError('Author profile could not be verified')
    vals={}
    for row in soup.select('table.gsc_rsb_std tr'):
        cells=[c.get_text(' ',strip=True) for c in row.select('td')]
        if len(cells)>=3:
            key=cells[0].lower(); value=re.sub(r'[^0-9]','',cells[1])
            if value: vals[key]=int(value)
    citations,h,i10=vals.get('citations'),vals.get('h-index'),vals.get('i10-index')
    if not all(isinstance(x,int) and x>=0 for x in (citations,h,i10)): raise RuntimeError('Metrics table was incomplete')
    data={'status':'verified','citations':citations,'h_index':h,'i10_index':i10,'updated_at':datetime.now(timezone.utc).isoformat(),'source':URL}
    out.write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
    print('Updated verified Google Scholar metrics')
except Exception as exc:
    print('Scholar metrics not updated:',exc)
    sys.exit(0)
