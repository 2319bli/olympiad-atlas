import json
from pathlib import Path
p=Path('/workspace/sites/olympiad-atlas');new=[];src='https://www.ommenlinea.org/wp-content/uploads/concursos/nacionales/nac29.pdf';solurl='https://www.ommenlinea.org/wp-content/uploads/2016/03/Tzaloa-1-2016.pdf'
def add(n,r,t,tags,s,sol,reason):new.append(dict(id=f'mx-omm-national-2015-{n}',country='Mexico',competition='OMM National',year=2015,number=str(n),statement=s,solution=sol or f'[View the official OMM magazine’s worked solutions, pages 38–42]({solurl}).',sourceUrl=src,solutionUrl=solurl,solutionKind='original-exposition' if sol else 'source-link',topic=t,tags=tags.split('|'),difficulty=r,ratingReason=reason,reviewStatus='individually-assessed',notes='Statement restated. Full national paper and organizer-published solution magazine individually reviewed.'))
add(3,5.5,'Algebra','Functional equations|Substitution|Backward reasoning',r'Let $f:\mathbb N\to\mathbb N$ satisfy $f(1)=1$ and $f(a+b+ab)=a+b+f(ab)$ for all positive integers $a,b$. Determine $f(2015)$.',r'''Define $g(n)=f(n)-n$. Then $g(1)=0$ and $g(a+b+ab)=g(ab)$. In particular, taking $a=1$ gives $g(2b+1)=g(b)$.

Repeated halving of odd arguments gives
$$g(2015)=g(1007)=g(503)=g(251)=g(125)=g(62).$$
To pass the even obstruction, use $(a,b)=(2,31)$, obtaining $g(62)=g(95)$. Then
$$g(95)=g(47)=g(23).$$
The choice $(a,b)=(3,5)$ gives $g(23)=g(15)$, and finally
$$g(15)=g(7)=g(3)=g(1)=0.$$
Therefore $f(2015)=2015$. The function $f(n)=n$ satisfies all conditions, so these conditions are consistent.''','Subtracting the identity function exposes an invariant between related integer arguments. Odd-argument reduction alone gets stuck at an even number; two carefully chosen factorisations connect it to the known value at 1. Discovering that bridge is the substantive step.')
add(4,5.5,'Number theory','Double counting|Divisor coprimality|Perfect squares',r'Write every ordered triple $(a,b,c)\in\{1,\ldots,n\}^3$. In each triple erase every entry smaller than its maximum, retaining all copies of the maximum. Prove that the total number of remaining entries is never a perfect square.',r'''Count retained entries by their position and value. If the first entry equals $j$, it survives precisely when the other two entries are at most $j$, giving $j^2$ triples. The same count holds for each position, including ties. Hence the total is
$$T=3\sum_{j=1}^n j^2=\frac{n(n+1)(2n+1)}2.$$
If $n$ is odd, the factors $n$, $(n+1)/2$, and $2n+1$ are pairwise coprime. If $T$ were square each would be square, but $2n+1\equiv3\pmod4$.

If $n=2k$ is even, the factors $k,2k+1,4k+1$ are pairwise coprime. Square $T$ would make both $k$ and $4k+1$ squares. Writing $k=u^2$, this puts the square $4u^2+1$ strictly between $(2u)^2$ and $(2u+1)^2$, since $u\ge1$. Both cases are impossible.''','Counting surviving positions avoids awkward tie cases and produces a product of three almost consecutive factors. The proof then splits by parity, isolates pairwise coprime factors, and uses different square obstructions in the two cases.')
add(5,6.5,'Geometry','Incentre|Arc midpoints|Reflection|Similarity',r'Let $I$ be the incentre of an acute triangle $ABC$. Line $AI$ meets the circumcircle of $BIC$ again at $E$. Let $D$ be the perpendicular projection of $A$ onto $BC$, and let $J$ be the reflection of $I$ in $BC$. Prove that $D,J,E$ are collinear.',None,'The midpoint of arc BC is also the circumcentre of BIC, so IE is a diameter. Midpoints convert the desired collinearity into parallelism; a pair of similar triangles and the angle-bisector theorem supply the necessary ratios. The auxiliary arc midpoint links the two circles.')
data=json.loads((p/'data/americas.json').read_text());ids={x['id'] for x in new};data=[x for x in data if x['id'] not in ids]+new
(p/'data/americas.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
c=json.loads((p/'research/americas-coverage.json').read_text());c['partiallyScreened']=[x for x in c['partiallyScreened'] if not(x['competition']=='OMM National' and x['year']==2015)];c['fullyScreened']=[x for x in c['fullyScreened'] if not(x['competition']=='OMM National' and x['year']==2015)];c['fullyScreened'].append(dict(competition='OMM National',year=2015,ratings=[3,4.5,5.5,5.5,6.5,6.5],source=solurl))
c['papersScreened']=len(c['fullyScreened']);c['problemAppearancesScreened']=sum(len(x['ratings']) for x in c['fullyScreened']+c['partiallyScreened']);c['uniqueIncluded']=len(data)
c['gaps'][5]='Mexico: OMM State Final 2014 and OMM National 2015 fully screened; 2013/2015 state finals and 2014/2016/2017 national papers partially screened. Other years pending.'
(p/'research/americas-coverage.json').write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n');print('Total',len(data))
