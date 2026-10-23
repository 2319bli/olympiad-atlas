import json,gzip,urllib.request,concurrent.futures,pathlib
P=pathlib.Path('research/asia');out=P/'extra';out.mkdir(exist_ok=True)
rows=[r for r in json.load(open(P/'manifest.json')) if isinstance(r,list) and r[1] in ['japan','south-korea'] and r[2]>=2022]
def get(r):
 p=out/(r[0]+'.json')
 if p.exists() or pathlib.Path('research/raw/asia',r[0]+'.json').exists():return(r[0],'cached')
 try:
  d=json.loads(gzip.decompress(urllib.request.urlopen(f'https://mathnet.mit.edu/data_v2/full/{r[1]}/{r[0]}.json.gz',timeout=30).read()));p.write_text(json.dumps(d,ensure_ascii=False));return(r[0],'ok')
 except Exception as e:return(r[0],str(e))
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as ex:res=list(ex.map(get,rows))
(P/'eastasia-download-results.json').write_text(json.dumps(res));print('download results',len(res),sum(x[1]=='ok' for x in res),[x for x in res if x[1] not in ['cached','ok']])
