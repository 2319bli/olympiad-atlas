import json
from pathlib import Path
p=Path(__file__).parent;r=json.loads((p/'reviews.json').read_text())
u='https://dev.skoljka.org/media/documents/cc89d67e-aab5-4076-a2f3-b7947e3481de/hmo_2019_rj.pdf'
map={'854625':(2,2),'c1f83b':(3,4),'523c4a':(4,4),'ec3990':(1,6),'38e372':(2,7),'a36998':(3,7),'6415a1':(4,10),'e98a03':(2,14),'6f9827':(3,14),'db6f07':(4,14),'ccdd53':(1,16),'63e1eb':(3,18),'7234cc':(4,18)}
for s,(number,page) in map.items():
 d=r['hrv_2019_'+s];d['number']=str(number);d['notes']='Original question number verified against the Croatian Mathematical Society’s 2019 Croatian-language solutions, mirrored by Školjka.'
 d['sourceUrl']=u+'#page='+str(page)
 if s=='6f9827':d['statement']=d['statement'].replace('interior point $T$ of $ABC$','interior point $T$ of acute triangle $ABC$')
(p/'reviews.json').write_text(json.dumps(r,ensure_ascii=False,indent=2))
