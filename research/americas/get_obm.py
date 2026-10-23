import pathlib,re,urllib.request,concurrent.futures,subprocess,json
p=pathlib.Path('/workspace/sites/olympiad-atlas/research/americas'); s=(p/'obm.html').read_text()
urls=[]
for m in re.finditer(r'<div class="prova post" data-ano="(\d+)" data-nivel="([^"]+)">(.*?)(?=<div class="prova post"|$)',s,re.S):
 y,l,b=m.groups()
 if 2021<=int(y)<=2025 and l in ['Nível 2','Nível 3']:
  for u in re.findall('href="([^"]+\\.pdf)"',b): urls.append(dict(year=int(y),level=l[-1],url=u))
json.dump(urls,open(p/'obm-links.json','w'),indent=2)
def f(r):
 q=p/f'OBM-{r["year"]}-N{r["level"]}.pdf'
 try:
  q.write_bytes(urllib.request.urlopen(r['url'],timeout=25).read()); subprocess.run(['pdftotext','-layout',str(q),str(q.with_suffix('.txt'))]);print(q.name,flush=True)
 except Exception as e:print(q.name,e,flush=True)
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex:list(ex.map(f,urls))
