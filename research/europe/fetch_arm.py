import urllib.request,re,concurrent.futures,subprocess,json
from pathlib import Path
p=Path(__file__).parent
u='https://www.olymp.am/hy/node/1254';s=urllib.request.urlopen(urllib.request.Request(u,headers={"User-Agent":"Mozilla/5.0"}),timeout=25).read().decode();urls=re.findall(r'href="([^"]+\.pdf)"',s);urls=list(dict.fromkeys(x for x in urls if 'Lucumner' in x))
(p/'arm2025-urls.json').write_text(json.dumps(urls,indent=2));print(urls,flush=True)
def g(u):
 if u.startswith('/'):u='https://www.olymp.am'+u
 f=p/u.split('/')[-1]
 try:
  f.write_bytes(urllib.request.urlopen(urllib.request.Request(u,headers={"User-Agent":"Mozilla/5.0"}),timeout=35).read());subprocess.run(['pdftotext','-layout',str(f),str(f.with_suffix('.txt'))]);return f.name,len(f.read_bytes())
 except Exception as e:return str(e)
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as e:
 for z in e.map(g,urls):print(z,flush=True)
