import urllib.request,urllib.parse,concurrent.futures,subprocess,json
from pathlib import Path
p=Path(__file__).parent
base='https://naec.ge/uploads/postData/20-25/ეროვნული სასწავლო ოლიმპიადა - მესამე ტური-შედეგები/მათემატიკა/'
urls={g:urllib.parse.quote(base+f,safe=':/') for g,f in [('10','მათემატიკა -10-ამოხსნები.pdf'),('11-12','მათემატიკა_XI-XII_ამოხსნები.pdf')]}
(p/'geo2025-urls.json').write_text(json.dumps(urls,ensure_ascii=False,indent=2))
def g(z):
 k,u=z;f=p/f'geo2025-{k}.pdf'
 try:
  f.write_bytes(urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'}),timeout=30).read());subprocess.run(['pdftotext','-layout',str(f),str(f.with_suffix('.txt'))]);return k,len(f.read_bytes())
 except Exception as e:return k,str(e)
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as ex:
 for z in ex.map(g,urls.items()):print(z)
