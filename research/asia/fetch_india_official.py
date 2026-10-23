import json,urllib.request,pathlib,concurrent.futures,subprocess
P=pathlib.Path('research/asia/india'); urls=json.load(open(P/'archive-links.json'))
names=['sol-inmo_17.pdf','inmo2017.pdf','sol-inmo-20.pdf','Inmo-2019-Solutions.pdf','INMO_2021_solutions.pdf','INMO_2024_final_solutions.pdf','inmo-2003.pdf']
def get(name):
 u=next(x for x in urls if x.endswith('/'+name));p=P/name
 try:
  if not p.exists():p.write_bytes(urllib.request.urlopen(u,timeout=35).read())
  r=subprocess.run(['pdftotext','-layout',str(p),str(p.with_suffix('.txt'))],capture_output=True)
  return name, p.stat().st_size, r.returncode
 except Exception as e:return name,str(e)
with concurrent.futures.ThreadPoolExecutor(max_workers=7) as pool:print(list(pool.map(get,names)))
