import json,gzip,urllib.request,concurrent.futures,time
from pathlib import Path
p=Path(__file__).parent
m=json.loads(gzip.decompress((p.parent/'raw/data_v2_manifest.json.gz').read_bytes()))
sources=['austria','netherlands','estonia','poland','russia','romania','germany','france','ukraine','slovenia','italy','croatia','spain','belarus','soviet-union','bulgaria','switzerland','north-macedonia','greece','czech-republic','moldova','serbia','portugal']
rows=[]
for src in sources:
 rs=[r for r in m['rows'] if r[1]==src and r[2]]
 y=max(r[2] for r in rs);rows += [r for r in rs if r[2]==y]
(p/'queue.json').write_text(json.dumps(rows))
def get(r):
 out=p/(r[0]+'.json')
 if out.exists():return r[0],'cached'
 u='https://mathnet.mit.edu/data_v2/full/'+r[1]+'/'+r[0]+'.json.gz'
 for tries in range(2):
  try:
   d=json.loads(gzip.decompress(urllib.request.urlopen(u,timeout=30).read()))
   out.write_text(json.dumps(d,ensure_ascii=False));return r[0],'ok'
  except Exception as e:
   if tries==1:return r[0],str(e)
   time.sleep(2)
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as e:
 for i,x in enumerate(e.map(get,rows)):
  if i%20==0 or x[1] not in ['ok','cached']:print(i,len(rows),*x,flush=True)
print('complete',len(rows))
