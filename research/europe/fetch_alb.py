import urllib.request,re,concurrent.futures,pathlib,subprocess,json
p=pathlib.Path(__file__).parent
ids=[35,31,38,37]
def fetch(i):
 u=f'https://www.ama.org.al/documents/{i}/view/';html=urllib.request.urlopen(u,timeout=20).read().decode();asset=re.search(r'href="(/asset/[^\"]+)"',html).group(1);url='https://www.ama.org.al'+asset;data=urllib.request.urlopen(url,timeout=20).read();f=p/f'albania-{i}.pdf';f.write_bytes(data);subprocess.run(['pdftotext','-layout',str(f),str(f.with_suffix('.txt'))]);return(i,url)
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:r=list(ex.map(fetch,ids))
(p/'albania-urls.json').write_text(json.dumps(r));print(r)
