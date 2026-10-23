import json,math
from pathlib import Path
p=Path('/workspace/sites/olympiad-atlas');new=[];src='https://revistas.tec.ac.cr/index.php/matematica/article/download/4233/3810/11561'
def add(n,r,t,tags,s,sol,reason,notes=''):
 new.append(dict(id=f'cr-olcoma-final-iii-2017-{n}',country='Costa Rica',competition='OLCOMA Final Level III',year=2017,number=str(n),statement=s,solution=sol or f'[View the official OLCOMA solution volume: exercise 3.3.1 and its solution, printed pages 73 and 106–107]({src}).',sourceUrl=src,solutionUrl=src,solutionKind='original-exposition' if sol else 'source-link',topic=t,tags=tags.split('|'),difficulty=r,ratingReason=reason,reviewStatus='individually-assessed',notes='Statement restated. The organizer-authored volume explicitly identifies the six actual final-exam questions separately from unused proposals. '+notes))
add(2,4.5,'Number theory','Greatest common divisor|Congruences|Valuations',r'Find the greatest common divisor of $5^5-5,\ 7^7-7,\ 9^9-9,\ldots,\ 2017^{2017}-2017$.',r'''For any odd $n$, $n^n-n=n(n^{n-1}-1)$ is divisible by $n(n^2-1)$, since $n-1$ is even. The product $n(n-1)(n+1)$ is divisible by 3, while the consecutive even numbers $n-1,n+1$ contribute at least three factors of 2. Hence every listed number is divisible by 24.

To prove this is the greatest common divisor, first calculate
$$\gcd(5^5-5,7^7-7)=\gcd(3120,823536)=48.$$
But $11^2\equiv9\pmod{16}$, so $11^{10}\equiv9\pmod{16}$ and
$$11^{11}-11\equiv11(9-1)\equiv8\pmod{16}.$$
Thus $11^{11}-11$ is not divisible by 16. The common divisor of all listed numbers divides 48, is a multiple of 24, and cannot be 48. It is therefore $\boxed{24}$.''','The lower bound comes from factoring odd powers and combining divisibility by 3 and 8. A separate sharpness check is necessary: the first two terms still have gcd 48, and a third term removes the extra factor of 2.','The official solution proves common divisibility by 24 but omits an upper-bound check; the original exposition includes it.')
add(3,6.5,'Combinatorics','Games|Forced moves|Case analysis',r'On a $4\times4$ grid, yellow pieces initially occupy $(1,1)$ and $(4,4)$, while white pieces occupy $(2,3)$ and $(3,2)$; all other cells are empty. A turn consists of choosing a colour for the opponent, who places a piece of that colour in an empty cell. That opponent then chooses a colour for the first player to place, and so on. A player wins by placing a piece which completes three consecutive pieces of one colour in a horizontal, vertical, or diagonal line. Yolanda chooses the first colour and Xinia places the first piece. Determine whether either player has a winning strategy, and describe one.',None,'The unusual rule lets a player control the opponent’s colour rather than their square. The solution forces yellow pieces into the two vacant corners, then splits the opponent’s next placement into centre and two edge types, using immediate-threat arguments to force a win for Yolanda. A complete strategy requires careful control of all replies.','Initial diagram transcribed into row/column coordinates. Consecutive triples are made explicit, as used by the official strategy.')
add(6,5,'Algebra','Functional equations|Injectivity|Monotonicity',r'A strictly increasing function $f:(0,\infty)\to\mathbb R$ satisfies $f(x)\,f\!\left(f(x)+\frac1x\right)=1$ for every $x>0$, with the inner argument in its domain. Determine $f(1)$.',r'''Write $t=f(1)$. The equation at $x=1$ yields $t\ne0$, $t+1>0$, and $f(t+1)=1/t$. Applying the equation again at $x=t+1$ gives
$$f\left(\frac1t+\frac1{t+1}\right)=t=f(1).$$
Strict increase implies injectivity, so
$$\frac1t+\frac1{t+1}=1,$$
which simplifies to $t^2-t-1=0$. Thus $t=(1\pm\sqrt5)/2$.

If the positive root were chosen, $t>1$ and $t+1>1$, whereas strict increase would require $f(t+1)>f(1)=t$. But $f(t+1)=1/t<1<t$, a contradiction. Hence
$$\boxed{f(1)=\frac{1-\sqrt5}{2}}.$$
For consistency, let $c=(\sqrt5-1)/2$. The increasing function $f(x)=-c/x$ satisfies the identity because $1-c=c^2$, so its inner argument is $c^2/x>0$.''','Iterating the functional equation once produces a repeated function value, and injectivity converts it into a quadratic equation. Strict monotonicity then rules out one algebraic root. Both uses of the function’s order condition are essential.')
data=json.loads((p/'data/americas.json').read_text());ids={x['id'] for x in new};data=[x for x in data if x['id'] not in ids]+new
for x in data:
 if x['id']=='mx-omm-national-2016-1':
  a=dict(country='Costa Rica',competition='OLCOMA Final Level III',year=2017,number='5',sourceUrl=src)
  x['appearances']=[v for v in x.get('appearances',[]) if not(v['competition']==a['competition'] and v['year']==2017)]+[a]
(p/'data/americas.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
c=json.loads((p/'research/americas-coverage.json').read_text());c['fullyScreened']=[x for x in c['fullyScreened'] if not(x['competition']=='OLCOMA Final Level III' and x['year']==2017)];c['fullyScreened'].append(dict(competition='OLCOMA Final Level III',year=2017,ratings=[3.5,4.5,6.5,2.5,4.5,5],source=src));c['papersScreened']=len(c['fullyScreened']);c['problemAppearancesScreened']=sum(len(x['ratings']) for x in c['fullyScreened']+c['partiallyScreened']);c['uniqueIncluded']=len(data);c['gaps'].append('Costa Rica: OLCOMA Final Level III 2017 fully screened from organizer-authored TEC volume. Q5 duplicates OMM National 2016 Q1 and is represented as an additional appearance. Other years and levels pending; contemporary OLCOMA web archive intermittently returns 503.')
(p/'research/americas-coverage.json').write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n');print('Total',len(data))
