"""Cache exactly the public figure URLs referenced by reviewed entries."""
import concurrent.futures,hashlib,json,urllib.request,urllib.parse
from pathlib import Path
root=Path(__file__).resolve().parents[1]
dest=root/'public/assets/diagrams';dest.mkdir(parents=True,exist_ok=True)
mf=root/'data/asset-map.json'
mapping=json.loads(mf.read_text()) if mf.exists() else {}
report=json.loads((root/'research/validation-report.json').read_text())
urls=[u for u in report['images'] if u.startswith(('https://mathnet.mit.edu/images/','https://cdn.mathpix.com/cropped/')) and u not in mapping]
def fetch(url):
    try:
        suffix=Path(urllib.parse.urlparse(url).path).suffix.lower()
        if suffix not in ['.png','.jpg','.jpeg','.webp','.svg']:return url,None,'Unsupported file type'
        name=hashlib.sha256(url.encode()).hexdigest()[:20]+suffix
        with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'OlympiadAtlas-research/1.0'}),timeout=40) as res:
            data=res.read(8*1024*1024)
            if not res.headers.get('Content-Type','').startswith('image/'):return url,None,'Not an image'
        (dest/name).write_bytes(data)
        return url,'assets/diagrams/'+name,None
    except Exception as e:return url,None,str(e)
errors=[]
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
    for u,path,err in pool.map(fetch,urls):
        if path:mapping[u]=path
        else:errors.append({'url':u,'error':err,'entries':report['images'][u]})
mf.write_text(json.dumps(mapping,ensure_ascii=False,indent=2))
(root/'research/diagram-report.json').write_text(json.dumps({'cached':len(mapping),'errors':errors},indent=2))
print(json.dumps({'cached':len(mapping),'newlyRequested':len(urls),'errors':errors},indent=2))
