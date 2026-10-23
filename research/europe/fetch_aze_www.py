import urllib.request,subprocess,concurrent.futures
from pathlib import Path
p=Path(__file__).parent
urls={
'2026-j':'https://www.arti.edu.az/wp-content/uploads/2026/03/Riyaziyyat_yarimfinal_AYQ_rus_2026.pdf',
'2026-s':'https://www.arti.edu.az/wp-content/uploads/2026/03/Riyaziyyat_yarimfinal_YYQ_rus_2026.pdf',
'2025-j':'https://www.arti.edu.az/wp-content/uploads/2025/03/Riyaziyyat_Rus_AYQ_2025.pdf',
'2025-s':'https://www.arti.edu.az/wp-content/uploads/2025/03/Riyaziyyat_Rus_YYQ_2025.pdf'}
def f(item):
 k,u=item;fn=p/f'aze{k}.pdf'
 try:
  if not fn.exists():fn.write_bytes(urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'}),timeout=40).read())
  subprocess.run(['pdftotext','-layout',str(fn),str(fn.with_suffix('.txt'))],check=True);print(k,fn.stat().st_size)
 except Exception as e:print(k,str(e))
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:list(ex.map(f,urls.items()))
