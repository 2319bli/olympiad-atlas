import numpy as np,json
from scipy.optimize import milp,Bounds,LinearConstraint
base=[(0,0),(1,0),(1,1),(2,1)]; forms=set()
for flip in [1,-1]:
 for rot in range(4):
  s=[(x*flip,y) for x,y in base]
  for _ in range(rot):s=[(-y,x) for x,y in s]
  mx=min(x for x,y in s);my=min(y for x,y in s)
  forms.add(tuple(sorted((x-mx,y-my) for x,y in s)))
shapes=[]
for form in forms:
 for x in range(5-max(a for a,b in form)):
  for y in range(5-max(b for a,b in form)):
   s=[(a+x,b+y) for a,b in form]
   if (2,2) not in s:shapes.append(s)
a=np.array([[int((x,y) in s) for s in shapes] for y in range(5) for x in range(5)])
low=np.ones(25);high=np.full(25,2);low[12]=high[12]=0
r=milp(np.zeros(len(shapes)),integrality=np.ones(len(shapes)),bounds=Bounds(0,1),constraints=LinearConstraint(a,low,high))
print(r.message)
selected=[[(x+1,y+1) for x,y in shapes[i]] for i,v in enumerate(r.x) if v>0.5];print(selected)
open('research/asia/japan/2023-final-q1-construction.json','w').write(json.dumps(selected))
