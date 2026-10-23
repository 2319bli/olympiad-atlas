import json
from pathlib import Path
p=Path('/workspace/sites/olympiad-atlas');new=[];src='https://www.scribd.com/document/818167155/2024f4n3'
def add(n,r,t,tags,s,sol,reason):new.append(dict(id=f'pe-onem-final-iii-2024-{n}',country='Peru',competition='ONEM National Final Level 3',year=2024,number=str(n),statement=s,solution=sol,sourceUrl=src,solutionUrl=src,solutionKind='original-exposition',topic=t,tags=tags.split('|'),difficulty=r,ratingReason=reason,reviewStatus='individually-assessed',notes='Official 24 October 2024 examination read via a publicly indexed document mirror; MINEDU archive returned HTTP 418. Statement restated and solution independently derived.'))
add(3,6,'Number theory','Quadratic forms|Induction|Coprimality|Modular arithmetic',r'Prove that for every positive integer $n$ there exist nonzero coprime integers $a,b$ such that $a^2+ab+b^2=7^n$.',r'''We construct pairs recursively. Begin with $(a,b)=(2,1)$ for $n=1$, and replace a pair by
$$(a',b')=(2a-b,\ a+3b).$$
Expansion gives
$$(a')^2+a'b'+(b')^2=7(a^2+ab+b^2),$$
so the required value grows by a factor of 7 at each step.

We prove at the same time that the coordinates remain coprime and that $a\equiv2b\pmod7$ with $7\nmid b$. These facts hold for $(2,1)$. Under the replacement, $a'-2b'=-7b$, and $b'=a+3b\equiv5b\not\equiv0\pmod7$. If a prime $p$ divides both $a',b'$, then it divides $3a'+b'=7a$ and $2b'-a'=7b$. Coprimality of $a,b$ forces $p=7$, which the congruence just excluded.

Finally neither coordinate can be zero: coprimality would force the other to be $\pm1$, giving norm 1 rather than $7^n$. This proves all requirements for every $n$.''','A multiplicative identity for the quadratic form gives a natural induction, but preserving primitivity is the obstacle. The carefully chosen linear transformation and its stable nonzero residue class modulo 7 solve both issues simultaneously.')
add(4,5.5,'Combinatorics','Forbidden subsequences|Induction|Extremal words',r'Words are formed from an alphabet of $n$ distinct letters. Adjacent letters must differ, and no subsequence may have the form $XYXY$ for distinct letters $X,Y$. Here a subsequence keeps the order of selected letters but need not use consecutive positions. Determine the greatest possible length.',r'''The maximum is $\boxed{2n-1}$. It is attained by
$$A_1A_2A_1A_3A_1\cdots A_{n-1}A_1A_nA_1,$$
where each letter other than $A_1$ occurs only once.

For the upper bound, use induction on the number of letters actually used. Let $A$ be the first letter of a valid word and suppose it occurs $k$ times. Write the word as
$$A\,W_1\,A\,W_2\,\cdots\,A\,W_k,$$
where none of the blocks $W_i$ contains $A$. The first $k-1$ blocks are nonempty because adjacent letters differ. No other letter can occur in two different blocks: those two occurrences, together with the A immediately before the earlier block and the next A, would form $AXAX$.

Let $t$ be the number of nonempty blocks and let their alphabet sizes be $n_1,\ldots,n_t$. Their alphabets are disjoint, so $\sum n_i\le n-1$, and $t\ge k-1$. Each block satisfies the same restrictions, so induction bounds its length by $2n_i-1$. Hence the total length is at most
$$k+\sum_{i=1}^t(2n_i-1)\le k+2(n-1)-t\le2n-1.$$
The one-letter case is immediate, completing the proof.''','The sharp construction is easy to guess, but the upper bound depends on splitting at repeated occurrences of the first letter. The forbidden pattern forces disjoint alphabets in the intervening blocks, allowing a precise induction and accounting for the separators.')
data=json.loads((p/'data/americas.json').read_text());ids={x['id'] for x in new};data=[x for x in data if x['id'] not in ids]+new;(p/'data/americas.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
c=json.loads((p/'research/americas-coverage.json').read_text());c['partiallyScreened']=[x for x in c['partiallyScreened'] if not(x['competition']=='ONEM National Final Level 3' and x['year']==2024)];c['partiallyScreened'].append(dict(competition='ONEM National Final Level 3',year=2024,ratings={'1':3.5,'3':6,'4':5.5},pending=['2'],source=src));c['papersScreened']=len(c['fullyScreened']);c['problemAppearancesScreened']=sum(len(x['ratings']) for x in c['fullyScreened']+c['partiallyScreened']);c['uniqueIncluded']=len(data)
c['gaps'][6]='Latin-American gaps: Chile 2021 junior/senior finals partially screened from indexed official papers; other Chile papers are blocked by intermittent organizer timeouts/503. Colombia, Bolivia, Cuba and other national competitions remain pending except as separately listed. Cono Sur 2024 fully screened; Ibero-American 2024/2025 partially screened. Other regional years pending.'
c['gaps'].append('Peru: ONEM National Final Level 3 2024 Q1/Q3/Q4 individually assessed; Q2 geometry remains pending. The official exam is available through an indexed public mirror while the organizer archive returns HTTP 418. Other years/levels pending.')
(p/'research/americas-coverage.json').write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n');print('Total',len(data))
