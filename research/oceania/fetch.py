import gzip,json,urllib.request,concurrent.futures,time
from pathlib import Path
p=Path('/workspace/sites/olympiad-atlas/research/oceania');(p/'full').mkdir(exist_ok=True)
rows=json.loads((p/'manifest.json').read_text())
def get(r):
 f=p/'full'/(r[0]+'.json')
 if f.exists():return True
 u=f'https://mathnet.mit.edu/data_v2/full/{r[1]}/{r[0]}.json.gz'
 for k in range(2):
  try:
   b=urllib.request.urlopen(u,timeout=25).read();d=json.loads(gzip.decompress(b));d['_manifest']=r;f.write_text(json.dumps(d,ensure_ascii=False));return True
  except Exception as e:
   if k: return [r[0],str(e)]
with concurrent.futures.ThreadPoolExecutor(max_workers=8)as e: results=list(e.map(get,rows))
print('fetched',sum(x is True for x in results),'failures',[x for x in results if x is not True])
allrows=[json.loads(f.read_text())for f in sorted((p/'full').glob('*.json'))]
(p/'all.json').write_text(json.dumps(allrows,ensure_ascii=False))
