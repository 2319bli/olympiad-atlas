import os,urllib.request,concurrent.futures,fitz,subprocess,re,json
from pathlib import Path
P=Path('/workspace/sites/olympiad-atlas/research/historic');P.mkdir(exist_ok=True)
html=Path('/workspace/sites/olympiad-atlas/research/bmos.html').read_text()
urls=re.findall(r'href="(/home/(?:bmo|fist)-\d{4}\.pdf)"',html)
def job(s):
 u='https://bmos.ukmt.org.uk'+s;name=s.split('/')[-1];dest=P/name
 try:
  if not dest.exists():dest.write_bytes(urllib.request.urlopen(u,timeout=45).read())
  d=fitz.open(dest);out=[]
  for i,p in enumerate(d):
   t=p.get_text()
   if len(t.strip())<50:
    img=P/(dest.stem+f'-p{i}.png');p.get_pixmap(matrix=fitz.Matrix(2,2)).save(img)
    t=subprocess.check_output(['tesseract',str(img),'stdout','--psm','3'],stderr=subprocess.DEVNULL,text=True,env={**os.environ,'OMP_THREAD_LIMIT':'1'})
   out.append(t)
  (P/(dest.stem+'.txt')).write_text('\n\n'.join(out))
  return {'name':name,'pages':len(d),'characters':sum(map(len,out))}
 except Exception as e:return {'name':name,'error':str(e)}
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex:
 for x in ex.map(job,urls):print(json.dumps(x),flush=True)
