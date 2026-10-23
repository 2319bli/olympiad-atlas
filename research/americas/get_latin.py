import urllib.request,concurrent.futures,pathlib,gzip,json,subprocess
p=pathlib.Path('/workspace/sites/olympiad-atlas/research/americas'); m=json.load(gzip.open(p.parent/'raw/data_v2_manifest.json.gz'))['rows']
rows=[r for r in m if (r[1]=='brazil' and r[2]==2022) or (r[1]=='argentina' and r[2]==2023 and r[3]=='ArgMO')]
print('rows',len(rows),flush=True)
urls=[(p/'mathnet'/f'{r[0]}.json',f'https://mathnet.mit.edu/data_v2/full/{r[1]}/{r[0]}.json.gz') for r in rows]
urls += [(p/f'solfinal{y}.pdf',f'https://www.ommenlinea.org/wp-content/uploads/practica/finales/solfinal{y}.pdf') for y in range(13,17)]
urls += [(p/f'nac{i}.pdf',f'https://www.ommenlinea.org/wp-content/uploads/concursos/nacionales/nac{i}.pdf') for i in range(28,32)]
def get(v):
 f,u=v
 if f.exists():return
 try:
  r=urllib.request.urlopen(u,timeout=25).read(); f.write_bytes(gzip.decompress(r) if u.endswith('.gz') else r)
  if f.suffix=='.pdf':subprocess.run(['pdftotext','-layout',str(f),str(f.with_suffix('.txt'))],check=True)
  print(f.name,len(r),flush=True)
 except Exception as e: print(f.name,e,flush=True)
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as ex:list(ex.map(get,urls))
