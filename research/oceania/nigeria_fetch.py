import urllib.request,json,re,html,concurrent.futures
P='/workspace/sites/olympiad-atlas/research/oceania/'
def entries(s):return [(a,html.unescape(b)) for a,b in re.findall(r'data-id="([^"]+)" jsname="vtaz5c"[^>]+data-tooltip="([^"]+)"',s)]
a=json.load(open(P+'nigeria-drive-index.json'))
folders=[z for label,ls in a for z in ls if isinstance(ls,list) and ('2nd ROUND' in z[1] or any(str(y) in z[1] for y in [2018,2019,2020])) and 'folder' in z[1]]
def get(z):
 id,name=z
 try:
  s=urllib.request.urlopen('https://drive.google.com/drive/folders/'+id,timeout=50).read().decode();open(P+'drive-'+id+'.html','w').write(s);return(name,entries(s))
 except Exception as e:return(name,str(e))
with concurrent.futures.ThreadPoolExecutor(max_workers=7) as pool:
 res=list(pool.map(get,folders));json.dump(res,open(P+'nigeria-drive-index2.json','w'),indent=2)
 for label,ls in res: print(label,ls)
try:
 s=urllib.request.urlopen('https://drive.google.com/uc?export=download&id=13ntL170SGpdpcFh6hi9sfIYeIfcOooxk',timeout=50).read();open(P+'nigeria-second.pdf','wb').write(s);print('SENIOR PDF',len(s),s[:30])
except Exception as e:print(e)
