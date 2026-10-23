import urllib.request, re,concurrent.futures,html,json,os
P='/workspace/sites/olympiad-atlas/research/oceania/'
def entries(s):return [(a,html.unescape(b)) for a,b in re.findall(r'data-id="([^"]+)" jsname="vtaz5c"[^>]+data-tooltip="([^"]+)"',s)]
root=entries(open(P+'nigeria-drive.html').read())
def get(z):
 id,name=z
 if 'Shared folder' not in name:return (name,[])
 try:
  s=urllib.request.urlopen('https://drive.google.com/drive/folders/'+id,timeout=50).read().decode();open(P+'drive-'+id+'.html','w').write(s);return(name,entries(s))
 except Exception as e:return(name,str(e))
with concurrent.futures.ThreadPoolExecutor(max_workers=7) as pool:
 res=list(pool.map(get,root));json.dump(res,open(P+'nigeria-drive-index.json','w'),indent=2)
 for z in res:print(z)
