import numpy as np, json
from scipy.optimize import milp, Bounds, LinearConstraint
from scipy.sparse import lil_matrix, vstack
P=[(i,j) for i in range(8) for j in range(8)]
E=[(a,b) for a in range(64) for b in range(64) if a!=b and max(abs(P[a][0]-P[b][0]),abs(P[a][1]-P[b][1]))==1]
d=lambda a: (2*P[a][0]-7)**2+(2*P[a][1]-7)**2
c=np.array([-int(d(b)<d(a)) for a,b in E]);A=lil_matrix((128,len(E)))
for k,(a,b) in enumerate(E):A[a,k]=1;A[64+b,k]=1
lo=np.ones(128);hi=np.ones(128)
for it in range(100):
 res=milp(c,integrality=np.ones(len(E)),bounds=Bounds(0,1),constraints=LinearConstraint(A.tocsr(),lo,hi),options={'time_limit':20})
 if res.x is None:raise Exception(res)
 nxt={a:b for i,(a,b) in enumerate(E) if res.x[i]>.5};cycles=[];seen=set()
 for a in range(64):
  if a in seen:continue
  cy=[];b=a
  while b not in seen:seen.add(b);cy.append(b);b=nxt[b]
  cycles.append(cy)
 print(it,-res.fun,list(map(len,cycles)),flush=True)
 if len(cycles)==1:
  path=[P[a] for a in cycles[0]];print(path);open('/workspace/sites/olympiad-atlas/research/europe/king_construct.json','w').write(json.dumps({'path':path,'pleasant':int(-res.fun)}));break
 rows=lil_matrix((len(cycles),len(E)))
 for j,cy in enumerate(cycles):
  ss=set(cy)
  for k,(a,b) in enumerate(E):
   if a in ss and b in ss:rows[j,k]=1
 A=vstack([A,rows]);lo=np.r_[lo,np.full(len(cycles),-np.inf)];hi=np.r_[hi,[len(x)-1 for x in cycles]]
