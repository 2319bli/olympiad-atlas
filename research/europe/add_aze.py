import json
from pathlib import Path
p=Path(__file__).parent;r=json.loads((p/'reviews.json').read_text())
rows=[
(2,'Combinatorics','All six sums can be prime: rows 1,2,4 / 5,8,6 / 7,3,9 give row sums 7,19,19 and column sums 13,13,19.'),
(3,'Geometry','With the orthocentre as origin, the pairwise dot products agree; subtracting the two given side-length squares gives CH squared minus AH squared.'),
(1.5,'Number theory','Comparing prime exponents gives k=2, n=-1 and m=3.'),
(2,'Combinatorics','For x+z=13t there are 13t-1 ordered positive pairs; sum for t from one to seven.'),
(2.5,'Geometry','The tangent at the common point meets the common external tangent at its midpoint; the resulting diameter circle makes the target triangle right-angled.'),
(2,'Number theory','If both x and y were at least two the reciprocal sum would be too small; one equals one and the other equals z.'),
(2.5,'Algebra','Multiply the interior geometric-series sum by the common ratio and subtract to cancel every intermediate term.'),
(2,'Geometry','In the right triangle AGB its hypotenuse midpoint is ten from G; the centroid ratio gives the required median.'),
(1,'Number theory','The numbers 25n+1 end in 01,26,51,76; the first hundreds digit eight occurs at n=32.'),
(1.5,'Algebra','Separate positive and negative x before multiplying the inequality; the negative interval gives -44.'),
(3,'Algebra','The substitution x=3+t makes the equation even in t; boundedness and existence of roots give the extreme-root sum six.'),
(3,'Geometry','Put the four collinear points at 0,3,8,32; subtract the two diameter-circle equations to locate the perpendicular projection of B.'),
(1,'Combinatorics','Choose nonempty subsets independently from the three teacher groups: 31 times 7 times 3.'),
(2,'Algebra','Three nonzero terms and their reciprocals can both be arithmetic progressions only when all three are equal.'),
(2.5,'Number theory','Factor the translated equation as (x+100)(y+100)=20000 and count positive and negative divisor pairs.'),
(None,'Geometry','The exact angle statement is verified in both language versions, but no complete proof of the incenter-crossline angle has yet been validated.'),
(1.5,'Combinatorics','Sum 63-2k over the thirty-one possible positive even values y=2k.'),
(1.5,'Algebra','Equate the two journey times and solve the resulting quadratic; the positive speed is fifty.'),
(2,'Algebra','Repeated difference-of-squares identities give x squared plus its reciprocal as three and the required absolute expression as 105.'),
(1.5,'Number theory','Sixty-three positive consecutive terms already sum to at least 2016, while 2 through 63 attain 2015.'),
(3.5,'Geometry','Order the four points around the square and equate opposite-side separations in perpendicular directions; the orientation must be axis-aligned.'),
(3,'Combinatorics','Count the digit sums 1,4,9,16,25 using bounded stars-and-bars; the five contributions are 1,10,45,66,6.'),
(2,'Number theory','Parity forces one prime to be two, then reduction modulo three forces the other to be three.'),
(4.5,'Number theory','Shift one cubic product to expose a common quadratic factor; factorial valuations and one extra factor of five determine the trailing zero count.'),
(3.5,'Combinatorics','The smaller prime subset sum is 5,7,13 or 17; the corresponding subset counts 3,5,11,13 total thirty-two.'),
(1.5,'Algebra','Expand the quadratic summands and use the standard first-power and square-sum formulas.'),
(2.5,'Number theory','Split the divisibility-by-eleven condition into a+c=b and a+c=b+11, excluding equal digits in each case.'),
(2.5,'Geometry','The diagonal-midpoint segment gives a base difference forty; cotangent addition gives a horizontal projection of four times the height.'),
(3,'Algebra','Eight times the first equation minus the second factors every cubic difference and telescopes cyclically to a+b+c.'),
(2,'Combinatorics','Inclusion-exclusion over the three forbidden occurrences of 23 leaves 625-75+1 possibilities.')]
src='https://arti.edu.az/wp-content/uploads/2025/03/Riyaziyyat_Az_AYQ_2025.pdf'
for n,(v,t,why) in enumerate(rows,1):
 slug=f'aze_2025_j_{n}';st='See the official paper for the full statement.';sol='';kind='original-exposition';notes='Multiple-choice semifinal paper; mathematical reasoning assessed independently. The Azerbaijani original was used to repair corrupt letters in the Russian transcription.'
 if n==24:
  st=r'How many trailing decimal zeroes does the integer $$\prod_{k=4}^{2017}(k^3+1)+\prod_{k=3}^{2016}(k^3-1)$$ have?'
  sol=r'Let $P=\prod_{j=3}^{2016}(j^2+j+1)$. Factoring the cubics and shifting the index in the first product gives $$P\,\frac{2015!}{24}\bigl(2016\cdot2017\cdot2018+24\bigr).$$ No factor of $P$ is divisible by 5: checking the five residues of $j$ proves this. The exponent of 5 in $2015!$ is $403+80+16+3=502$. The bracket is 20 modulo 25, so contributes one further factor of 5. Thus the entire expression has exactly 503 factors of 5. The exponent of 2 in $2015!/24$ already exceeds 503, so there are exactly **503 trailing zeroes**.'
 (p/(slug+'.json')).write_text(json.dumps({'country':'Azerbaijan','competition':'Azerbaijan National Mathematical Olympiad','year':2025,'section':'Semifinal — Junior (Grades 8–9)','problem_number':str(n),'problem_markdown':st,'solutions_markdown':[]},ensure_ascii=False,indent=2))
 r[slug]={'difficulty':v,'topic':t,'tags':[],'reason':why,'number':str(n),'sourceUrl':src,'solutionUrl':src+f'#page={(n-1)//2+3}','solution':sol,'solutionKind':kind,'sourceName':'ARTI — official semifinal paper','license':'Original competition rights retained; concise English mathematical paraphrase.','notes':notes}
 if n==16:r[slug]['status']='quarantined'
(p/'reviews.json').write_text(json.dumps(r,ensure_ascii=False,indent=2))
q=p/'coverage_inventory.py';s=q.read_text().replace("if c in ['Albania','Georgia']:return nums(1,5)","if c in ['Albania','Georgia']:return nums(1,5)\n if c=='Azerbaijan':return nums(1,30) if y==2025 else nums(1,20)")
s=s.replace("'archiveGaps':[","'archiveGaps':[\n {'country':'Azerbaijan','sourceUrl':'https://arti.edu.az/2025/03/06/respublika-f%C9%99nn-olimpiadalarinin-respublika-m%C9%99rh%C9%99l%C9%99sinin-yarimfinal-turunun-sual-kitabcalari/','status':'2025 junior semifinal: all 30 statements inspected, 29 independently assessed, question 16 pending proof verification. Senior semifinals and 2026 papers located but not fully reviewed. A verified public national-final source remains to be found.'},\n {'country':'Luxembourg','sourceUrl':'https://www.script.lu/en/news/2025-09/olympiades-de-mathematiques-2024-2025-plus-de-3300-eleves-mobilises','status':'Official SCRIPT report identifies participation in the Belgian OMB plus international OFM, Benelux, EGMO and IMO. No separate Luxembourg national paper was located; Belgian and international papers retain their own provenance.'},")
q.write_text(s)
