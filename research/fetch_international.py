import urllib.request,json,gzip,concurrent.futures,time
from pathlib import Path
p=Path('/workspace/sites/olympiad-atlas/research/international-raw');p.mkdir(exist_ok=True)
m=json.loads(gzip.decompress(Path('/workspace/sites/olympiad-atlas/research/raw/data_v2_manifest.json.gz').read_bytes()))
sources=['asia-pacific-mathematics-olympiad-apmo','european-girls-mathematical-olympiad-egmo','nordic-mathematical-olympiad','benelux-mathematical-olympiad','middle-european-mathematical-olympiad-memo','jbmo','balkan-mathematical-olympiad','imo','baltic-way','ibero-american-mathematical-olympiad','zhautykov-olympiad','romanian-master-of-mathematics-rmm','czech-polish-slovak-mathematical-match','silk-road-mathematics-competition','portuguese-language-countries-olympiad-omcplp']
rows=sorted([r for r in m['rows'] if r[1] in sources],key=lambda r:(sources.index(r[1]),-r[2] if r[2] else 0,r[0]))
Path('/workspace/sites/olympiad-atlas/research/international-manifest.json').write_text(json.dumps(rows))
def get(r):
 out=p/(r[0]+'.json')
 if out.exists():return True
 u='https://mathnet.mit.edu/data_v2/full/'+r[1]+'/'+r[0]+'.json.gz'
 for attempt in range(2):
  try:
   b=urllib.request.urlopen(u,timeout=30).read(); d=json.loads(gzip.decompress(b));out.write_text(json.dumps(d,ensure_ascii=False));return True
  except Exception as e:
   if attempt: return (r[0],str(e))
   time.sleep(2)
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:
 for i,result in enumerate(ex.map(get,rows)):
  if result is not True: print('ERROR',result,flush=True)
  if i%100==0:print('Downloaded',i+1,'/',len(rows),flush=True)
print('DONE',len(rows),flush=True)
