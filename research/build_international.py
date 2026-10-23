from pathlib import Path
import json,re,collections
root=Path('/workspace/sites/olympiad-atlas');raw=root/'research/international-raw';reviews=json.loads((root/'research/international-reviews.json').read_text())
overrides={
'apm_2025_0453f0':r'''The answer is all positive pairs with $\alpha+\beta=2$.

Write the point visited after $n$ moves as $(x_n,y_n)$. Then $x_n+y_n=n$ and $|x_n-y_n|<2025$. The labels are nondecreasing because both parameters are positive. Since every nonnegative integer appears exactly once, the $n$th label is $n$.

Now
$$x_n\alpha+y_n\beta=\frac{\alpha+\beta}{2}n+\frac{\alpha-\beta}{2}(x_n-y_n).$$
The second term is bounded independently of $n$, and taking a floor changes a number by less than one. Thus $|n-(\alpha+\beta)n/2|$ is bounded for all $n$, forcing $\alpha+\beta=2$.

Conversely suppose the sum is two, and by swapping the axes assume $\alpha\geq\beta$. Alternate right and up moves. After $2m$ moves the unfloored label is $2m$; after $2m+1$ moves it is $2m+\alpha$. Since $1\leq\alpha<2$, its floor is $2m+1$. The path stays within distance one of the diagonal and has exactly the required labels.''',
'apm_2024_531576':r'''Put $F_k(x)=(2/(1+x))^{2^k}$. We first establish, for $x,y>0$ and $k\geq1$,
$$F_k(x)+F_k(y)\geq2F_{k-1}(xy).$$
For $k=1$, clearing positive denominators reduces this to
$$xy(x-y)^2+(xy-1)^2\geq0.$$
If it holds for $k-1$, then $u^2+v^2\geq(u+v)^2/2$, applied to $u=F_{k-1}(x)$ and $v=F_{k-1}(y)$, proves it for $k$.

Start with the left-hand side of the desired inequality plus $2^{-n}$. Pair its last term with $2^{-n}F_n(1)$ and apply the lemma; these two terms are at least $2^{-(n-1)}F_{n-1}(a_n)$. Pair this with the term involving $a_{n-1}$, and continue. After all $n$ applications the result is at least
$$F_0(a_1\cdots a_n)=\frac{2}{1+a_1\cdots a_n}.$$
Subtracting $2^{-n}$ gives the assertion.'''
}
# These extractions have a consequential gap or a figure-dependent construction; retain their source link without presenting an unreliable embedded proof.
withhold={'apm_2024_91e126','apm_2023_fb45d1','bxm_2022_fe31d1','bmo_2024_4b7efa','btw_2023_38796d','btw_2023_df10b2'}
overrides.update({
'imo_2024_41dbe2':r'''The only pair is $(a,b)=(1,1)$, which gives the constant gcd two.

Suppose the gcd is a constant $g$ for all $n\geq N$, and set $M=ab+1$. Both $a$ and $b$ are coprime to $M$. Choose $n\geq N$ with $n\equiv-1\pmod{\varphi(M)}$. Euler's theorem gives
$$a^n+b\equiv a^{-1}+b\equiv0\pmod M,$$
and likewise $b^n+a\equiv0\pmod M$. Thus $M\mid g$.

Since the gcd is still $g$ at the next exponent, $M$ divides both $a^{n+1}+b$ and $a^n+b$. Subtracting gives
$$M\mid a(a^n+b)-(a^{n+1}+b)=b(a-1).$$
As $\gcd(M,b)=1$, we get $M\mid a-1$. But $0\leq a-1<M$, so $a=1$. Interchanging $a,b$ gives $b=1$, as claimed.''',
'imo_2024_5877d2':r'''For each index $i$, writing $x_i$ as a sum of $x_i$ ones costs
$$2^ix_i^2=\sum_{j=1}^{x_i}2^i(2j-1).$$
Every positive integer has a unique expression $2^i(2j-1)$, so across all indices these marginal costs are distinct positive integers. Since exactly $n$ costs are selected, their sum is at least $1+2+\cdots+n=n(n+1)/2$.

To attain this bound, select all the costs from one through $n$. At each fixed index $i$ they form an initial segment of the list $2^i,3\cdot2^i,5\cdot2^i,\ldots$, hence define a valid nonnegative integer $x_i$. No index above $n$ is needed. These choices have total $n$ and attain the bound.''',
'imo_2024_7db46b':r'''Let $A'$ be the reflection of $A$ through $I$. Central reflection in $I$ sends each tangent of the incircle to the opposite parallel tangent. Thus $A'X$ is parallel to $AC$ and $A'Y$ is parallel to $AB$.

The point $P$ lies on $AA'$. Inscribed angles give $\angle APB=\angle ACB=\angle A'XC$, so $B,P,A',X$ are concyclic. Similarly $C,Y,A',P$ are concyclic.

The homothety with centre $A$ and scale two sends $K,I,L$ to $B,A',C$, giving $\angle KIL=\angle BA'C$. From the two cyclic quadrilaterals,
$$\angle APX=\angle A'BC,\qquad\angle YPA=\angle BCA'.$$
Adding these identities makes $\angle KIL+\angle YPX$ the sum of the three angles of triangle $BA'C$, which is $180^\circ$.''',
'nmo_2022_b252c5':r'''Britta wins exactly when $n$ is prime.

If $n$ is composite, Anton first takes a prime divisor $p<n$ and eventually chooses $x_1=p$. The displayed expression is divisible by $p$, so it cannot be congruent to one modulo $n$.

Now suppose $n$ is prime. Pair every integer $a$ in the set with $n-a$. Since $n$ is odd these pairs have distinct members. Whenever Anton takes one member of a pair, Britta takes the other. Thus after Anton selects $x_1,x_2$, Britta can select $y_1=n-x_1,y_2=n-x_2$. Modulo $n$ the product inside the power becomes
$$x_1x_2(2x_1)(2x_2)=(2x_1x_2)^2.$$
Its required power is $(2x_1x_2)^{n-1}$, which is one by Fermat's little theorem, since none of the factors is divisible by $n$.''',
'bxm_2025_be509d':r'''Write the angles of $ABC$ as $A,B,C$. Since $E,F$ are the arc midpoints, the lines $BE$ and $CF$ pass through $I$. Standard inscribed-angle calculations give
$$\angle EFI=B/2,\qquad \angle FEI=C/2.$$
Also $DD'$ is a diameter, and the arc-midpoint definitions give
$$\angle D'EF=B/2,\qquad \angle D'FE=C/2.$$
Consequently $D'E$ is parallel to $FI$ and $D'F$ is parallel to $EI$. Thus $ED'FI$ is a parallelogram. Its diagonals $EF$ and $D'I$ bisect each other, so the midpoint $M$ of $EF$ lies on $D'I$. The symmetric case follows directly by symmetry.''',
'mem_2024_1c96e4':r'''Each $a_i$ divides $k$, so only finitely many primes can divide any term. Fix such a prime $p$, write $c=v_p(k)$, and put $e_i=v_p(a_i)$.

If $e_{i+1}>e_i$, the divisibility condition implies that $2e_i=c$: otherwise $v_p(k-a_i^2)=\min(c,2e_i)\leq2e_i<e_i+e_{i+1}$, a contradiction. Since $2e_{i+1}>c$, the next condition gives $e_{i+1}+e_{i+2}\leq c$, hence $e_{i+2}<c/2$.

Whenever $e_j<c/2$, we have $v_p(k-a_j^2)=2e_j$ and consequently $e_{j+1}\leq e_j$. Thus, after its first strict increase, this exponent sequence becomes nonincreasing from two terms later. If no strict increase occurs, it is already nonincreasing. In either case it eventually stabilises because its terms are nonnegative integers. Applying this to the finitely many primes dividing $k$ shows that all prime exponents, and therefore the integers $a_i$ themselves, are eventually constant.'''
})
d_egmo=json.loads((raw/'egm_2020_9202c0.json').read_text())
overrides['egm_2020_9202c0']=d_egmo['solutions_markdown'][0].split('\nB. ')[1].split('\nC. ')[0].strip()
d_memo=json.loads((raw/'mem_2023_7aad50.json').read_text())
overrides['mem_2023_7aad50']=d_memo['solutions_markdown'][0].replace('f(-1) \\leq f(1)-2 \\gamma=0','f(-1)^2 \\leq f(1)-2 \\gamma=0')
d_apmo=json.loads((raw/'apm_2022_789d8c.json').read_text())
overrides['apm_2022_789d8c']='If $a=1$, then $b^2$ divides one, so $b=1$, giving a solution. In the remaining argument assume $a>1$; in particular the modulus $a-1$ is positive.\n\n'+d_apmo['solutions_markdown'][0]
for slug in ['imo_2024_071598','imo_2024_46c203','imo_2024_657c6a']:
 source=json.loads((raw/(slug+'.json')).read_text())['solutions_markdown'][0]
 if slug=='imo_2024_071598':overrides[slug]=source.split('\nComment.')[0]
 if slug=='imo_2024_46c203':overrides[slug]='Set $\\varepsilon=1/2024$.\n\n'+source.split('\nSolution 2.')[0]
 if slug=='imo_2024_657c6a':overrides[slug]='The maximum is $n(n-1)/2$, attained when every race has the same ranking.\n\nNote that taking'+source.split('Note that taking')[1]
overrides.update({
'bmo_2024_3a17e7':r'''Necessarily $a>b$. Write $a=bq+r$ with $q\geq1$ and $0\leq r<b$. Reduction modulo $3^b+2$ gives
$$3^b+2\mid(-2)^q3^r+2.$$
This expression can be zero only when $q=1,r=0$, which would mean $a=b$.

If $q$ is even, write $2^q3^r+2=(3^b+2)t$ with $t>0$. Modulo $3^r$ we have $t\equiv1$. The case $t=1$ would give $2^q3^r=3^b$, impossible. Thus $t\geq3^r+1$ and comparison gives $2^q>3^b$, hence $q>b$ and $a>b^2$.

If $q$ is odd, write $2^q3^r-2=(3^b+2)t$ with $t>0$. If $r=0$, positivity already gives $2^q>3^b$, and we finish as above. Otherwise reduction modulo $3^r$ gives $t\equiv-1$, so $t\geq3^r-1>3^r/2$. Consequently $2^{q+1}>3^b$. The case $q=1$ is impossible because $2\cdot3^r-2<3^b+2$. For $q\geq3$ we have $2^{q+1}<3^q$, whence $q>b$ and again $a>b^2$.''',
'bmo_2024_c7a652':r'''Set $M=10^{2023}$ and
$$u_n=1+\sum_{k\geq1,\,3k\leq n}\binom n{3k}8^k.$$
If $\omega$ is a primitive cube root of unity, the roots-of-unity filter gives
$$u_n=\frac{3^n+(1+2\omega)^n+(1+2\omega^2)^n}{3}.$$
The three bases are the roots of $(t-1)^3-8=t^3-3t^2+3t-9$. Consequently
$$u_{n+3}=3u_{n+2}-3u_{n+1}+9u_n,\qquad u_0=u_1=u_2=1.$$
Modulo $M$, a triple of consecutive terms determines both the next and the previous term, since nine is invertible. The evolution on the finite set of triples is therefore periodic from the start. Let $d>0$ be a period; it cannot be one, since $u_3=9$.

Applying the recurrence across the period boundary gives
$$9u_{d-1}=u_{d+2}-3u_{d+1}+3u_d\equiv1-3+3=1\pmod M.$$
The integer $(8M+1)/9$ is the inverse of nine modulo $M$, so
$$u_{d-1}-1\equiv\frac{8(M-1)}9\pmod M.$$
The residue on the right consists of exactly 2023 eights. Thus $n=d-1$ has the required property.''',
'bmo_2024_54aaec':r'''For $n=1$ the answer is no. We prove that for every $n\geq2$ it is yes.

Write $A_n=\sum_{x\in S_n}x$, $B_n=\sum_{x\in S_n}x^2$, and $C_n=\sum_{x\in S_n}x^3$. Counting each digit position gives
$$A_n\equiv2\cdot4^{n-1}\pmod{4^n}.$$
Appending a leading digit $c\in\{1,2,3,4\}$ and expanding squares shows
$$B_{n+1}=4B_n+20\cdot10^nA_n+30\cdot4^n10^{2n}\equiv4B_n\pmod{4^{n+1}}.$$
Since $B_1=30$, this yields $B_n\equiv2\cdot4^{n-1}\pmod{4^n}$.

The corresponding cube expansion is
$$C_{n+1}=4C_n+30\cdot10^nB_n+90\cdot10^{2n}A_n+100\cdot4^n10^{3n}.$$
For $n\geq2$ the last three terms are divisible by $4^{n+1}$, using the preceding congruences. Directly $C_2\equiv8\pmod{16}$, so induction gives
$$C_n\equiv2\cdot4^{n-1}\pmod{4^n}\quad(n\geq2).$$
If the $4^n$ numbers in $S_n$ had distinct residues modulo $4^n$, they would form a complete residue system. Their cubes would then have sum congruent to
$$\sum_{i=1}^{4^n}i^3=\left(\frac{4^n(4^n+1)}2\right)^2\equiv0\pmod{4^n},$$
contradicting the formula for $C_n$. Hence two distinct numbers have the required difference.''',
'jbm_2023_78057b':r'''Bob has a winning strategy. Put $K=100^2+1$. In each of the first 99 rows, pair columns $(1,2),(3,4),\ldots,(99,100)$. In the last row use the same pairs except replace the first two by $(1,3)$ and $(2,4)$.

Whenever Alice places $j$ in a cell, Bob places $K-j$ in its paired cell. This is always possible: after each Bob move both members of every cell pair are filled or both empty, and used numbers occur in complementary pairs. No integer equals its own complement because $K$ is odd.

At the end every row sum is $50K$. The average column sum is also $50K$, so Bob cannot lose. Suppose all column sums equal $50K$. Let $a,b,c,d$ be the last-row entries in columns one through four. The first 99 rows contribute $99K$ to the sum of columns one and two. Thus $a+b=K$. But the crossed pairing also gives $a+c=K$, hence $b=c$, contradicting distinctness of all entries. Some column sum therefore exceeds $50K$, and Bob wins.'''
})
overrides.update(json.loads((root/'research/international-extra-solutions.json').read_text()))
def clean(s):
 s=re.sub(r'!\[([^\]]*)\]\((images/[^)]+)\)',lambda m:'!['+m.group(1)+'](https://mathnet.mit.edu/'+m.group(2)+')',s)
 s=re.sub(r'\\begin\{equation\*?\}|\\end\{equation\*?\}','',s)
 return s.strip()
old_bank={p['id']:p for p in json.loads((root/'data/international.json').read_text())}
old_coverage=json.loads((root/'research/international-coverage.json').read_text())
old_decisions={p['id']:p for p in old_coverage.get('decisions',[])}
out=[];excluded=[]
for slug,(rating,reason) in reviews.items():
 f=raw/(slug+'.json')
 if not f.exists():raise ValueError(slug)
 d=json.loads(f.read_text())
 competition=d.get('competition_code') or d.get('competition')
 if slug.startswith('jbm_2023_'):competition='JBMO'
 if slug.startswith('bmo_2024_'):competition='Balkan MO Shortlist'
 aliases=[]
 if slug=='bmo_2024_37ccab':aliases=[{'competition':'Balkan MO','year':2024,'number':'2'}]
 if slug=='bmo_2024_3a17e7':aliases=[{'competition':'Balkan MO','year':2024,'number':'3'}]
 if not 1<=rating<=10:
  excluded.append({'id':slug,'competition':d.get('competition'),'year':d.get('year'),'number':d.get('problem_number'),'difficulty':rating,'reason':reason});continue
 statement=clean(d['problem_markdown']);solution=clean(overrides.get(slug,(d.get('solutions_markdown')or[''])[0]))
 if slug in withhold:solution=None
 # Remove an answer accidentally embedded after the complete question.
 if slug=='apm_2024_91e126':statement=statement.split('\nAnswer:')[0]
 if slug=='mem_2024_2aa484':statement=statement.split('\nAnswer.')[0]
 if slug=='egm_2024_10a8ce':solution=solution.replace('a_{0}', 'a_{1}')
 if slug=='ibe_2003_733d39':statement=statement.replace('respectively. Show', 'respectively, with $X\\ne Y$. Show')
 if slug=='rou_2025_daceb6':statement=statement.replace('a sequence of integers', 'an infinite sequence of positive integers')
 if slug=='btw_2023_63fd11':statement=statement.replace('+ \\dots + 2F_2', '+ \\dots - 2F_2')
 if slug=='btw_2023_3a179b':statement=statement.replace('for all integers $n \\ge 1$. Prove', 'for all integers $n \\ge 2$. Prove')
 if slug=='apm_2016_703ac5':
  # The extraction incorrectly names the diameter of APDQ; the original statement is unaffected.
  solution=None
 tags=[]
 for topic in d.get('topics',[]):
  if topic[-1] not in tags:tags.append(topic[-1])
 topic=d.get('primary_domain') or 'Combinatorics'
 notes='Individually assessed from the statement and sourced solution. Text supplied by MathNet; CC BY 4.0 applies subject to original contest rights.'
 if slug in overrides:notes+=' Solution rewritten to correct transcription issues and streamline the mathematical argument.'
 if not solution:notes+=' Embedded solution withheld because the available extraction needs further verification; consult the linked source.'
 out.append({'id':slug,'country':'International','competition':competition,'year':d.get('year'),'number':re.sub(r'^(?:Problem\s*|P)(\d+)\.?$',r'\1',d.get('problem_number') or '').rstrip('.'),'statement':statement,'solution':solution,'sourceUrl':'https://mathnet.mit.edu/explorer.html?p='+slug,'solutionUrl':'https://mathnet.mit.edu/explorer.html?p='+slug,'topic':topic,'tags':tags,'difficulty':rating,'ratingReason':reason,'reviewStatus':'individually-assessed','notes':notes,'provenance':{'collection':'MathNet','bookletTitle':d.get('booklet_title'),'competitionRaw':d.get('competition_raw'),'section':d.get('section'),'copyrightHolder':d.get('booklet_copyright_holder')}})
 if aliases:
  out[-1]['alternateOrigins']=aliases
  out[-1]['notes']+=' Also selected as '+', '.join(x['competition']+' '+str(x['year'])+' problem '+x['number'] for x in aliases)+'.'
 if d.get('officialSourceUrl'):
  out[-1]['sourceUrl']=d['officialSourceUrl'];out[-1]['solutionUrl']=d['officialSolutionUrl'];out[-1]['provenance']['collection']='Official contest archive';out[-1]['notes']=d.get('reviewNote','Statement and proof rewritten from the official released paper; individually assessed.')
 if slug in {'bmo_2024_37ccab','bmo_2024_3a17e7','bmo_2023_0ab85a','bmo_2023_83afda'}:
  selected={'bmo_2024_37ccab':('2','C3'),'bmo_2024_3a17e7':('3','N5'),'bmo_2023_0ab85a':('1','A1'),'bmo_2023_83afda':('2','G3')}[slug]
  out[-1]['competition']='Balkan Mathematical Olympiad';out[-1]['number']=selected[0]
  out[-1]['alternateOrigins']=[{'competition':'Balkan MO Shortlist','year':d['year'],'number':selected[1]}]
  out[-1]['notes']+=' Official contest selection verified against the organisers’ released paper.'
  if d['year']==2024:
   out[-1]['sourceUrl']='https://bmo2024.org/wp-content/uploads/2024/05/BOM_english.pdf';out[-1]['solutionUrl']='https://bmo2024.org/wp-content/uploads/2024/05/BOM_englishSolutions.pdf'
  else:
   out[-1]['sourceUrl']='https://bmo2023.tubitak.gov.tr/problems';out[-1]['solutionUrl']='https://bmo2023.tubitak.gov.tr/assets/files/BMO_2023_Solutions.pdf'
 if slug=='balkan_2024_official_p1':out[-1]['competition']='Balkan Mathematical Olympiad'
 if slug.startswith('zhk_2021_'):
  out[-1]['competition']='International Zhautykov Olympiad'
  out[-1]['number']=re.sub(r'[^0-9]','',d.get('problem_number',''))
  out[-1]['sourceUrl']='https://izho.kz/wp-content/uploads/2021/01/Solutions-IZHO-2021.pdf'
  out[-1]['solutionUrl']=out[-1]['sourceUrl']
 if slug.startswith('rmm_2021_'):
  out[-1]['competition']='Romanian Master of Mathematics'
  out[-1]['sourceUrl']='https://rmms.lbi.ro/rmm2021/index.php?id=problems_math'
 if slug.startswith('rou_2025_'):
  out[-1]['competition']='Romanian Master of Mathematics'
  day=1 if int(out[-1]['number'])<=3 else 2
  out[-1]['sourceUrl']=f'https://rmms.lbi.ro/rmm2025/pr{day}/RMM2025-Day{day}-English.pdf'
  out[-1]['notes']+=' Exact statement and problem order verified against the official released paper.'
 if slug.startswith(('ibe_2000_','ibe_2001_','ibe_2002_')):
  out[-1]['competition']='Ibero-American Mathematical Olympiad'
  out[-1]['number']={'A1':'1','A2':'2','A3':'3','B1':'4','B2':'5','B3':'6'}[d['problem_number']]
  out[-1]['sourceUrl']=f'https://www.obm.org.br/content/uploads/2018/01/ibero{d["year"]}.pdf'
  if slug=='ibe_2000_a16b2e':out[-1]['statement']=out[-1]['statement'].replace('n > 3',r'n \geq 3')
  if slug=='ibe_2000_6e6cb0':out[-1]['statement']=r'A pile initially contains 2000 stones. Two players alternate removing one to five stones, but a player cannot remove the same number as their opponent did on the preceding turn. A player who has no legal move loses. Which player has a winning strategy, and what is it?'
  if slug=='ibe_2002_779f08':out[-1]['statement']=out[-1]['statement'].replace('0<n<2002',r'1\leq n\leq2002')
  if slug=='ibe_2001_33a740':out[-1]['statement']=r'In triangle $ABC$, the incircle has centre $I$ and touches $BC,CA,AB$ at $D,E,F$. Lines $BI,CI$ meet line $EF$ at $P,Q$, respectively. Prove that $DP=DQ$ implies that $ABC$ is isosceles.'
 if slug.startswith('ibe_2003_'):
  out[-1]['competition']='Ibero-American Mathematical Olympiad'
  out[-1]['number']={'A1':'1','A2':'2','A3':'3','B1':'4','B2':'5','B3':'6'}[d['problem_number']]
  out[-1]['sourceUrl']='https://oma.org.ar/enunciados/ibe18.htm'
  out[-1]['notes']+=' Official released problem order verified; the host archive heading has a year typo.'
 if slug.startswith('btw_2023_'):
  selected={'A 2':'1','A 3':'2','A 6':'3','A 9':'5','C 1':'6','C 2':'7','C 5':'8','C 7':'9','C 8':'10','G 1':'11','G 4':'12','G 6':'13','G 8':'14','G 13':'15','N 4':'16','N 8':'17','N 9':'18','N 10':'19','C 3':'20'}
  out[-1]['competition']='Baltic Way Shortlist'
  if d['problem_number'] in selected:
   out[-1]['competition']='Baltic Way';out[-1]['number']=selected[d['problem_number']]
   out[-1]['alternateOrigins']=[{'competition':'Baltic Way Shortlist','year':2023,'number':d['problem_number']}]
   out[-1]['sourceUrl']='https://bw2025.lu.lv/fileadmin/user_upload/lu_portal/projekti/baltic_way_2013/BW_problems_solutions/bw2023_solutions.pdf';out[-1]['solutionUrl']=out[-1]['sourceUrl']
   out[-1]['notes']+=' Selection and problem number verified against the official contest paper.'
  if slug=='btw_2023_22414b':
   out[-1]['statement']=statement.replace('positive integer $n \\ge 1$', 'positive integer $n \\ge 2$')
   out[-1]['solution']=solution.replace('precisely when $n$ is even or $n = 1$', 'precisely when $n$ is even')
   out[-1]['solution']=re.sub(r'If \$n = 1\$.*?\n\n','',out[-1]['solution'],flags=re.S)
  if slug=='btw_2023_2c5c1f':out[-1]['statement']=statement.replace('circles with no common points.', 'circles with no common points, neither contained inside the other.')
 if slug in {'imo_2024_071598','imo_2024_41dbe2','imo_2024_7db46b'}:
  selected={'imo_2024_071598':('1','A1'),'imo_2024_41dbe2':('2','N4'),'imo_2024_7db46b':('4','G2')}[slug]
  out[-1]['competition']='IMO';out[-1]['number']=selected[0]
  out[-1]['alternateOrigins']=[{'competition':'IMO Shortlist','year':2024,'number':selected[1]}]
  out[-1]['sourceUrl']='https://www.imo-official.org/assets/documents/problems/2024/2024_eng.pdf'
  out[-1]['solutionUrl']='https://www.imo-official.org/assets/documents/problems/2024/IMO2024SL.pdf'
  out[-1]['notes']+=' Also IMO Shortlist 2024 '+selected[1]+'. Official contest selection verified.'
 selected_imo={'imo_2023_2e005b':('1','N1'),'imo_2023_1ae32a':('2','G4'),'imo_2023_7a9af0':('4','A3'),'imo_2023_a99802':('5','C3'),'imo_2022_b034b8':('1','C2'),'imo_2022_e1fe8a':('2','A3'),'imo_2022_cd4ff4':('4','G1'),'imo_2022_230fa0':('5','N4')}
 if slug in selected_imo:
  num,sl=selected_imo[slug];year=d['year']
  out[-1]['competition']='IMO';out[-1]['number']=num
  out[-1]['alternateOrigins']=[{'competition':'IMO Shortlist','year':year,'number':sl}]
  out[-1]['sourceUrl']=f'https://www.imo-official.org/assets/documents/problems/{year}/{year}_eng.pdf'
  out[-1]['solutionUrl']=f'https://www.imo-official.org/assets/documents/problems/{year}/IMO{year}SL.pdf'
  out[-1]['notes']+=' Official contest selection and numbering verified.'
for item in out:
 if item['id'].startswith('imo_2025_official_p'):
  item['alternateOrigins']=[{'competition':'IMO Shortlist','year':2025,'number':{'1':'C1','2':'G4','3':'N7','4':'N3','5':'A3','6':'C8'}[item['number']]}]
# Retain already verified source labels, topic fixes and mathematical corrections.
for j,item in enumerate(out):
 prior=old_decisions.get(item['id'],{})
 for key in ['country','competition','year','section','number','sourceUrl']:
  if key in prior:item[key]=prior[key]
 if item['id'] in old_bank:out[j]=old_bank[item['id']]
exec((root/'research/international-all-difficulties.py').read_text())
out.sort(key=lambda x:(x['competition'],-(x['year'] or 0),x['number']))
(root/'data/international.json').write_text(json.dumps(out,ensure_ascii=False,indent=2))
coverage={'scope':'International and regional olympiads excluding PAMO','assessmentMethod':'Individual mathematical review of statement and supplied solution, calibrated to agreed BMO scale; ratings not inferred from contest or question number.','reviewedCount':len(reviews),'includedCount':len(out),'excluded':excluded,'byCompetition':dict(collections.Counter(x['competition'] for x in out)),'gaps':['The MathNet corpus is not a complete archive of every competition/year. Downloaded records are not counted as reviewed.','Original archive verification and the remaining individual assessments are still in progress.'],'reviewedIds':list(reviews),'complete':False}
(root/'research/international-coverage.json').write_text(json.dumps(coverage,ensure_ascii=False,indent=2))
print('Included',len(out),'reviewed',len(reviews))

import runpy
runpy.run_path(str(root/"research/enhance_international_coverage.py"))
coverage=json.loads((root/'research/international-coverage.json').read_text())
if old_coverage.get('historicalInventory'):coverage['historicalInventory']=old_coverage['historicalInventory']
coverage['ratingPolicy']='All individually assessed difficulties from 1 to 10 are included; 4–7 is the preferred browsing range.'
(root/'research/international-coverage.json').write_text(json.dumps(coverage,ensure_ascii=False,indent=2))
