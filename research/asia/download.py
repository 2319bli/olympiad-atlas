import json,gzip,urllib.request,concurrent.futures,time
from pathlib import Path
p=Path('/workspace/sites/olympiad-atlas/research/asia'); out=p.parent/'raw'/'asia';out.mkdir(parents=True,exist_ok=True)
rows=json.loads((p/'manifest.json').read_text())
latest={s:max(r[2] for r in rows if r[1]==s) for s in set(r[1] for r in rows)}
selected=[r for r in rows if r[1] in ['china','india'] or r[2]==latest[r[1]]]
selected.sort(key=lambda r:(r[1]!='india',r[1]!='china',r[2],r[0]))
(p/'download-selection.json').write_text(json.dumps(selected))
def get(r):
 path=out/(r[0]+'.json')
 if path.exists():return (r[0],'cached')
 url=f'https://mathnet.mit.edu/data_v2/full/{r[1]}/{r[0]}.json.gz'
 try:
  raw=urllib.request.urlopen(url,timeout=35).read();d=json.loads(gzip.decompress(raw));path.write_text(json.dumps(d,ensure_ascii=False));return(r[0],'ok')
 except Exception as e:return(r[0],str(e))
res=[]
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex:
 for i,result in enumerate(ex.map(get,selected)):
  res.append(result)
  if (i+1)%100==0:print(i+1,'/',len(selected),flush=True)
(p/'download-results.json').write_text(json.dumps(res))
print('done',len(res),sum(x[1] not in ['ok','cached'] for x in res),flush=True)
