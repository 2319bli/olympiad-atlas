import urllib.request,gzip,json,concurrent.futures,pathlib
p=pathlib.Path('/workspace/sites/olympiad-atlas/research/international-raw')
m=json.load(gzip.open('/workspace/sites/olympiad-atlas/research/raw/data_v2_manifest.json.gz'))
years={'imo':2024,'baltic-way':2023,'romanian-master-of-mathematics-rmm':2021,'zhautykov-olympiad':2021,'ibero-american-mathematical-olympiad':2003,'balkan-mathematical-olympiad':2023}
r=[r for r in m['rows'] if r[1] in years and r[2]==years[r[1]]]
def f(r):
 fn=p/(r[0]+'.json')
 if not fn.exists():
  try:fn.write_bytes(gzip.decompress(urllib.request.urlopen('https://mathnet.mit.edu/data_v2/full/'+r[1]+'/'+r[0]+'.json.gz',timeout=20).read()))
  except Exception as e:return r[0],str(e)
 return r[0],'ok'
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:
 for result in ex.map(f,r):print(result,flush=True)
