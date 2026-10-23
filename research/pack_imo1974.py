from functools import lru_cache
import json
sets=[[1,2,3,4,5,7,10],[1,2,3,4,5,8,9],[1,2,3,4,6,7,9],[1,2,3,5,6,7,8]]
answers=[]
for sizes in sets:
 dims={a:[(w,2*a//w) for w in range(1,9) if 2*a%w==0 and 2*a//w<=8] for a in sizes}
 @lru_cache(None)
 def rec(mask,remaining):
  if not remaining:return ()
  k=next(i for i in range(64) if not (mask>>i)&1);y,x=divmod(k,8)
  for a in sorted(remaining,reverse=True):
   for w,h in dims[a]:
    if x+w>8 or y+h>8:continue
    bits=sum(1<<((y+j)*8+x+i) for i in range(w) for j in range(h))
    if bits&mask:continue
    rest=rec(mask|bits,tuple(t for t in remaining if t!=a))
    if rest is not None:return ((a,x+1,y+1,w,h),)+rest
  return None
 result=rec(0,tuple(sizes));answers.append({'whiteCounts':sizes,'rectangles':result});print(sizes,result,'states',rec.cache_info().currsize)
open('research/international-official/imo1974p4-tilings.json','w').write(json.dumps(answers,indent=2))
