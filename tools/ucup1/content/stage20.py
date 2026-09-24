# -*- coding: utf-8 -*-
STAGE = {
    'no': 20,
    'name': 'Stage 20: India',
    'source_name': 'June 17-18, 2023',
    'source_html': r'''
<p>Zadatke su pripremili autori iz indijske natjecateljske zajednice (Jatin Yadav, Jatin Garg, Nishank Suresh, Vaibhav Gosain, Chaithanya Shyam D, Aryan, Jeroen Op de Beek, Harris Leung, Arul Kolla). Prijevod službenog rješenja: <a href="https://contest.ucup.ac/download.php?type=attachments&amp;id=1259&amp;r=1">Tutorial (en)</a>. Tekst zadatka preveden je prema službenim <a href="https://contest.ucup.ac/download.php?type=attachments&amp;id=1259&amp;r=0">engleskim tekstovima zadataka</a>. Zadatak je dostupan na <a href="https://contest.ucup.ac/contest/1259">Universal Cup Judging System</a>.</p>
''',
}

PROBLEMS = [
# ---------------------------------------------------------------- A
{
    'letter': 'A', 'title': 'Maximum Bitwise OR', 'title_hr': 'Najveći bitovni ILI', 'slug': 'A_maximum_bitwise_or',
    'tl': '2 s', 'ml': '256 MiB',
    'statement': r'''
<p>Dan je niz $A$ od $N$ cijelih brojeva i $Q$ upita $(L, R)$. Za upit promatramo niz $B = A[L..R]$. Jedan <em>potez</em>: odaberi indeks $j$ i cijeli broj $i$ takav da je $2^i \le B[j]$, pa zamijeni $B[j]$ s $B[j] \oplus (B[j] - 2^i)$ ($\oplus$ je bitovni XOR). Za svaki upit ispiši najveći mogući bitovni ILI svih vrijednosti u $B$ i najmanji broj poteza kojim se on postiže.</p>
<h3>Ulaz</h3>
<p>$T \le 10^5$ testova; $N, Q \le 10^5$ (ukupno po $10^5$), $0 \le A[i] \le 10^9$, $1 \le L \le R \le N$.</p>
<h3>Izlaz</h3>
<p>Za svaki upit dva broja: najveći ILI i najmanji broj poteza.</p>
<h3>Primjer</h3>
<p>$A = (10, 10, 5)$. Upit $(1,2)$: $B = (10, 10)$; potezima $j=1, i=0$ ($10 \to 3$) i $j=2, i=2$ ($10 \to 12$) dobivamo ILI $= 15$ u $2$ poteza. Upit $(1,3)$: ILI je već $15$, $0$ poteza.</p>
''',
    'hints': [
        r'''<p>Što potez radi s brojem $x$? Ako je bit $i$ postavljen u $x$, rezultat je točno $2^i$. Inače rezultat ima postavljene točno bitove $[i, j]$, gdje je $j$ najmanji postavljeni bit od $x$ veći od $i$. Nikad se ne može stvoriti bit iznad najvišeg bita $k$ koji se pojavljuje u $B$.</p>''',
        r'''<p>Maksimalni ILI je uvijek $2^{k+1} - 1$ i postiže se u najviše $2$ poteza ($x \to 2^k \to 2^{k+1} - 1$). Ostaje odlučiti je li dovoljno $0$ ili $1$ potez. Neka su $l$ i $r$ najniži i najviši bit $\le k$ koji nije postavljen ni u jednoj vrijednosti; jedan potez mora popuniti cijeli raspon $[l, r]$, a da se ne izgubi nijedan bit koji ima samo ta vrijednost.</p>''',
    ],
    'coach': [
        ('Opažanje 1: učinak poteza', r'''<p>$x \oplus (x - 2^i)$: ako je bit $i$ u $x$ jedinica, $x - 2^i$ samo gasi taj bit pa je XOR jednak $2^i$. Ako je nula, oduzimanje „posuđuje” od najbližeg višeg postavljenog bita $j$: bitovi $i..j-1$ postaju jedinice, bit $j$ nula; XOR s $x$ daje točno bitove $[i, j]$. Zaključak: potez nikad ne stvara bit iznad najvišeg bita od $x$.</p>'''),
        ('Opažanje 2: gornja granica i dva poteza', r'''<p>Ako je $k$ najviši bit koji se pojavljuje u $B$, ILI ne može premašiti $2^{k+1} - 1$. Tu vrijednost uvijek postižemo: uzmi $x$ s bitom $k$; $x \oplus (x - 2^k) = 2^k$, a zatim $2^k \oplus (2^k - 2^0) = 2^{k+1} - 1$. Dakle odgovor je uvijek $2^{k+1}-1$, a broj poteza je $0$, $1$ ili $2$.</p>'''),
        ('Redukcija: kada je dovoljan jedan potez?', r'''<p>Ako je početni ILI već $2^{k+1}-1$: $0$. Inače neka su $l \le r$ najniži i najviši nedostajući bit. Jedan potez na $x$ daje bitove $[i, j]$ pa mora biti $i \le l$ i $j \gt r$ — tj. u $x$ su bitovi $[l, r]$ nule, a iznad $r$ postoji postavljeni bit. Pritom potez „gasi” sve ostale bitove od $x$, što smije samo ako ih pokrivaju druge vrijednosti. Vrijednost je <em>posebna</em> ako ima bit koji nema nitko drugi u $B$; posebnih vrijednosti je $O(\log M)$ i nalazimo ih pomoću „sljedeća pozicija s bitom $b$” za svaki indeks.</p>'''),
        ('Algoritam', r'''<p>Neposebne vrijednosti: postoji li $x$ u $[L, R]$ bez bitova u $[l, r]$ i s bitom iznad $r$? Za svaki $r$ držimo segmentno stablo minimuma nad nizom „najveći bit $b \le r$ sadržan u $A_i$” (vrijednosti koje nemaju bit iznad $r$ isključimo); minimum na $[L, R]$ manji od $l$ znači „da”. Posebna vrijednost $x$ s posebnim bitom $j$: nakon poteza preživi samo bit $j$, pa $j$ mora biti jedini posebni bit od $x$, bitovi $[l, r]$ nule i $j \gt r$ — provjera u $O(\log M)$ po posebnoj vrijednosti. Ako ništa ne prolazi, odgovor je $2$.</p>'''),
        ('Složenost', r'''<p>$O(\log M)$ segmentnih stabala, upiti u $O(\log M \cdot \log N)$; ukupno otprilike $O((N + Q)\log M \log N)$ uz $\sum N, \sum Q \le 10^5$.</p>'''),
    ],
    'solution': r'''
<p>Kad primijenimo potez $x \to x \oplus (x - 2^i)$, dobivamo $2^i$ ako je bit $i$ postavljen u $x$, a inače vrijednost koja ima postavljene točno bitove $[i, j]$, gdje je $j$ najmanji bit $\gt i$ postavljen u $x$.</p>
<p>Ako je najviši postavljeni bit među svim vrijednostima $k$, što god radili ne možemo postaviti nijedan bit $\gt k$. Ali uvijek možemo postaviti sve bitove $\le k$: odaberi bilo koji element $x$ s postavljenim $k$-tim bitom, zamijeni ga s $x \oplus (x - 2^k) = 2^k$, a zatim $2^k$ zamijeni s $2^k \oplus (2^k - 2^0) = 2^{k+1} - 1$. Dakle najveći mogući odgovor je $2^{k+1} - 1$ i postiže se u $\le 2$ poteza.</p>
<p>Ako je početni ILI već $2^{k+1} - 1$, potrebno je $0$ poteza. Inače treba odlučiti možemo li proći s jednim potezom. Neka je $l$ najniži, a $r$ najviši bit $\le k$ koji nije postavljen ni u jednoj vrijednosti.</p>
<p>Vrijednost nazovimo <em>posebnom</em> ako postoji bit postavljen samo u njoj. Posebne vrijednosti obrađujemo odvojeno; sve ih je lako naći u $O(\log M)$ ako za svaki indeks predračunamo sljedeću poziciju koja sadrži dani bit.</p>
<p>Potez na neposebnoj vrijednosti $x$ uspijeva ako i samo ako su svi bitovi u rasponu $[l, r]$ u $x$ nule i $x \gt 2^r$. Postoji li takva vrijednost provjeravamo tako da za svaki $r$ pohranimo segmentno stablo minimuma nad nizom čiji je $i$-ti element najveći bit $b \le r$ sadržan u $A_i$.</p>
<p>Promotrimo sada posebnu vrijednost $x$. Ako je bit $j$ sadržan samo u $x$, moramo osigurati da $j$-ti bit ostane postavljen i nakon operacije. Primijetimo da $j$ mora biti jedini posebni bit od $x$, jer postoji najviše jedan bit koji je jedinica i prije i poslije primjene operacije. Dakle moramo odabrati neki $i \le l$ takav da je $j$ najmanji bit $\gt l$ postavljen u $x$. To radi ako su svi bitovi u $[l, r]$ u $x$ nule i $j \gt r$.</p>
''',
},
# ---------------------------------------------------------------- B
{
    'letter': 'B', 'title': 'Minimize Median', 'title_hr': 'Minimiziraj medijan', 'slug': 'B_minimize_median',
    'tl': '2 s', 'ml': '256 MiB',
    'statement': r'''
<p>Dan je niz $A$ od $N$ (neparan) cijelih brojeva iz $[1, M]$ i niz $cost$ duljine $M$. Jedan potez: odaberi indeks $i$ i $x \in [1, M]$ te zamijeni $A[i]$ s $\lfloor A[i]/x \rfloor$ uz cijenu $cost[x]$. Ukupna cijena poteza ne smije premašiti $K$. Nađi najmanji mogući $\mathrm{median}(A)$ (srednji element sortiranog niza).</p>
<h3>Ulaz</h3>
<p>$T \le 10^5$ testova; $N \le 10^6$ neparan, $2 \le M \le 10^6$, $0 \le K \le 10^9$, $1 \le A[i] \le M$, $1 \le cost[i] \le 10^9$; $\sum N, \sum M \le 10^6$.</p>
<h3>Izlaz</h3>
<p>Najmanji mogući medijan.</p>
<h3>Primjer</h3>
<p>$A = (2, 5, 2)$, $cost = (3, 2, 4, 6, 13)$: $K = 0 \Rightarrow 2$; $K = 3 \Rightarrow 2$; $K = 6$: podijeli $5$ s $3$ (cijena $4$) i $2$ s $2$ (cijena $2$) $\Rightarrow$ medijan $1$.</p>
''',
    'hints': [
        r'''<p>Dijeljenje većim brojem nikad nije gore, pa neka $cost_i \leftarrow \min(cost_i, \dots, cost_M)$. Ako medijan možemo spustiti na $\le x$, možemo i na $\le x+1$ — binarno traži $x$. Za fiksni $x$ treba $\lceil N/2 \rceil$ najmanjih elemenata spustiti na $\le x$.</p>''',
        r'''<p>$\lfloor \lfloor a/y \rfloor / z \rfloor = \lfloor a/(yz) \rfloor$: niz dijeljenja je jedno dijeljenje s umnoškom, uz zbroj cijena. Definiraj $f(y)$ = najmanja cijena dijeljenja točno s $y$ i računaj je sitom u $O(M \log M)$; element $A_i$ treba dijeliti s barem $\lceil (A_i + 1)/(x+1) \rceil$.</p>''',
    ],
    'coach': [
        ('Opažanje 1: monotonost', r'''<p>Dijeljenje većim $x$ daje manji rezultat, pa smijemo staviti $cost_i = \min_{j \ge i} cost_j$ (sufiksni minimum). Također, „medijan $\le x$” je monotono svojstvo u $x$ — binarno pretraživanje po odgovoru.</p>'''),
        ('Opažanje 2: što treba za fiksni $x$', r'''<p>Sortiraj $A_1 \le \dots \le A_N$, $N = 2k+1$. Medijan je $\le x$ točno kad barem $k+1$ elemenata bude $\le x$, a najjeftinije je uzeti $k+1$ najmanjih. Element $A_i$ treba u ukupnosti podijeliti s barem $\lceil (A_i+1)/(x+1) \rceil$ (najmanji $y$ s $\lfloor A_i / y \rfloor \le x$).</p>'''),
        ('Redukcija: niz dijeljenja = jedno dijeljenje', r'''<p>Za pozitivne cijele brojeve vrijedi $\lfloor \lfloor a/y \rfloor / z \rfloor = \lfloor a/(yz) \rfloor$. Zato je niz poteza na istom elementu isto što i jedno dijeljenje s umnoškom, uz zbroj cijena. Neka je $f(y)$ najmanja cijena „dijeljenja točno s $y$”: $f(y) = \min(cost_y, \min_{d \mid y} cost_d + f(y/d))$.</p>'''),
        ('Algoritam', r'''<p>$f$ računamo sitom (za svaki $d$ prolazimo višekratnike) u $O(M \log M)$. Oprez blizu $M$: može biti isplativo dijeliti s brojem većim od $M$, ali nas zanima samo prvi višekratnik iznad $M$, pa $f$ računamo do $2M$ (nedostajuće cijene su $\infty$), a zatim $f(y) \leftarrow \min_{y' \ge y} f(y')$. Za fiksni $x$ cijena je $\sum_{i \le k+1} f(\lceil (A_i+1)/(x+1) \rceil)$ u $O(N)$; usporedi s $K$.</p>'''),
        ('Složenost', r'''<p>$O(M \log M + N \log M)$ po testu (sito + binarno pretraživanje s $O(N)$ provjerom); s $\sum N, \sum M \le 10^6$ prolazi.</p>'''),
    ],
    'solution': r'''
<p>Dijeljenje većim brojem nikad nije gore, pa kao pripremni korak stavimo $cost_i = \min(cost_i, cost_{i+1}, \dots, cost_M)$.</p>
<p>Ako se medijan može učiniti $\le x$, onda se naravno može učiniti i $\le x+1$. Zato binarnim pretraživanjem tražimo najmanji valjani $x$. Za fiksni $x$ želimo izračunati najmanju cijenu da medijan bude $\le x$.</p>
<p>Neka je $A_1 \le A_2 \le \dots \le A_N$ i $N = 2k+1$. Optimalno je pokušati $A_1, A_2, \dots, A_{k+1}$ sve učiniti $\le x$. Da bi $A_i$ pao na $\le x$, treba ga ukupno podijeliti s barem $\left\lceil \frac{A_i + 1}{x + 1} \right\rceil$.</p>
<p>Za sve pozitivne cijele brojeve $x, y, z$ cjelobrojno dijeljenje ima svojstvo $\left\lfloor \frac{\lfloor x/y \rfloor}{z} \right\rfloor = \left\lfloor \frac{x}{yz} \right\rfloor$, što znači da niz cjelobrojnih dijeljenja možemo promatrati kao jedno dijeljenje, sa zbrojenim cijenama.</p>
<p>Izračunajmo $f(y)$, najmanju cijenu dijeljenja točno s $y$. Inicijaliziramo $f(y) = cost_y$, a zatim za svaki djelitelj $d$ od $y$ relaksiramo s $cost_d + f(y/d)$. Dinamičkim programiranjem u stilu sita to traje ukupno $O(M \log M)$.</p>
<p>Potreban je oprez s vrijednostima blizu $M$, jer može biti optimalno dijeliti s vrijednošću većom od $M$. No zanima nas samo prvi višekratnik svakog cijelog broja koji premašuje $M$, pa možemo npr. računati $f(y)$ do $2M$ (nedostajuće cijene tretiramo kao $\infty$). Konačno, kako dijeljenje većim brojevima nije gore, $f(y)$ postavimo na sufiksni minimum $\min(f(y), f(y+1), \dots, f(M))$.</p>
<p>Kad su sve vrijednosti $f(y)$ poznate, cijena da medijan bude $\le x$ računa se lako u $O(N)$: jednostavno zbrojimo $f\!\left(\left\lceil \frac{A_i+1}{x+1} \right\rceil\right)$ po svim relevantnim $A_i$.</p>
''',
},
# ---------------------------------------------------------------- C
{
    'letter': 'C', 'title': 'Exam Requirements', 'title_hr': 'Uvjeti za ispite', 'slug': 'C_exam_requirements',
    'tl': '3 s', 'ml': '512 MiB',
    'statement': r'''
<p>$N$ ispita, ispit $i$ traje u zatvorenom intervalu $[S_i, E_i]$. Da bi položio ispit moraš prisustvovati cijelom, a prisustvovati možeš samo ispitima koji se međusobno ne preklapaju ($[1,3]$ i $[3,10]$ se preklapaju; $[1,3]$ i $[4,5]$ ne). Za diplomu treba ispuniti $M$ uvjeta oblika „položi barem jedan od ispita $A$ ili $B$” ($A \ne B$). Može li se diplomirati?</p>
<h3>Ulaz</h3>
<p>$T \le 100$ testova; $N \le 10^5$, $0 \le M \le 10^5$, $0 \le S_i \le E_i \le 10^9$; $\sum N, \sum M \le 10^5$.</p>
<h3>Izlaz</h3>
<p><code>YES</code> ili <code>NO</code>.</p>
<h3>Primjer</h3>
<p>Ispiti $[1,5],[2,7],[10,11]$, uvjet $(2,1)$: <code>YES</code>. Ispiti $[1,5],[2,7],[5,7]$ i uvjeti $(1,2),(2,3),(3,1)$: svi se preklapaju, a treba barem $2$ — <code>NO</code>.</p>
''',
    'hints': [
        r'''<p>Uvedi logičku varijablu $x_i$ = „prisustvujem ispitu $i$”. Uvjet daje klauzulu $(x_A \lor x_B)$, a svaki par ispita koji se preklapaju klauzulu $(\lnot x_X \lor \lnot x_Y)$. To je 2-SAT.</p>''',
        r'''<p>Parova koji se preklapaju može biti $O(N^2)$. Sortiraj ispite po početku: ispit $X$ se preklapa točno s ispitima čiji početak pada u $[S_X, E_X]$ (i simetrično). Umjesto brida do svakog takvog ispita, dodaj pomoćne vrhove nalik segmentnom stablu koji predstavljaju raspone ispita — $O(\log N)$ bridova po ispitu.</p>''',
    ],
    'coach': [
        ('Opažanje: model s logičkim varijablama', r'''<p>Odluka „idem / ne idem na ispit $i$” je logička varijabla. Uvjet $(A, B)$: $x_A \lor x_B$. Nekompatibilnost ispita koji se preklapaju: $\lnot x_X \lor \lnot x_Y$. Sve klauzule imaju dva literala — konjunktivna normalna forma s dvije varijable po klauzuli (2-CNF).</p>'''),
        ('Algoritam 1: 2-SAT', r'''<p>Zadovoljivost 2-CNF-a je klasični 2-SAT: graf implikacija na $2N$ literalima, za klauzulu $(a \lor b)$ bridovi $\lnot a \to b$ i $\lnot b \to a$; formula je zadovoljiva ako i samo ako nijedna varijabla nije u istoj jako povezanoj komponenti sa svojom negacijom (Tarjan/Kosaraju).</p>'''),
        ('Redukcija: previše klauzula preklapanja', r'''<p>Preklapajućih parova može biti $\Theta(N^2)$. Sortiraj ispite po $S$. Preklapanje ispita $X$ s ispitima koji počinju u $[S_X, E_X]$ čini kontinuirani raspon u sortiranom poretku (svaki preklapajući par uhvati onaj koji počinje ranije). Izgradi segmentno stablo nad tim poretkom čiji unutarnji vrhovi imaju bridove prema listovima $\lnot x_Y$ svog raspona; tada $x_X \to$ $O(\log N)$ čvorova stabla umjesto $O(N)$ bridova. Za kontrapozitivne implikacije ($x_Y \to \lnot x_X$) treba i „zrcalno” stablo s bridovima od listova prema korijenu. Isključi $X$ iz vlastitog raspona (podijeli raspon na dva dijela), inače bi dobio $x_X \to \lnot x_X$.</p>'''),
        ('Složenost', r'''<p>$O(N \log N)$ vrhova i bridova, SCC u linearnom vremenu po veličini grafa: $O((N + M) \log N)$ ukupno.</p>'''),
    ],
    'solution': r'''
<p>Odluku o prisustvovanju svakom ispitu modeliramo zasebnom logičkom varijablom.</p>
<p>Za svaki uvjet $A, B$ mora vrijediti logički izraz $A \lor B$. Za svaki par ispita $X, Y$ koji se preklapaju mora vrijediti $X' \lor Y'$ (negacije). Svi ti izrazi moraju biti istiniti da bismo diplomirali s valjanim rasporedom prisustvovanja. Ukupni izraz koji treba zadovoljiti je oblika $(A_1 \lor B_1) \land (A_2 \lor B_2) \land \dots \land (X_1' \lor Y_1') \land (X_2' \lor Y_2') \land \dots$, što je logički izraz u konjunktivnoj normalnoj formi s dva literala po klauzuli (2-CNF).</p>
<p>Provjera zadovoljivosti 2-CNF izraza dobro je poznat problem, poznat kao 2-zadovoljivost (<a href="https://en.wikipedia.org/wiki/2-satisfiability">2-SAT</a>). Rješava se modeliranjem izraza kao grafa, s implikacijskim bridovima za svaki „ili” uvjet.</p>
<p>Budući da preklapajućih raspona može biti $O(N^2)$, u našem izrazu može biti $O(N^2)$ „ili” uvjeta. Da smanjimo broj implikacijskih bridova u 2-SAT grafu, možemo stvoriti pomoćne vrhove nalik segmentnom stablu, odgovorne za „segment” — kontinuirani raspon ispita sortiranih po vremenu početka ili završetka.</p>
<p>Sada za svaki ispit, umjesto izravnih implikacijskih bridova prema svim ispitima koji se s njim preklapaju, dodajemo bridove prema $O(\log N)$ pomoćnih vrhova segmentnog stabla koji su odgovorni za raspone ispita koji počinju ili završavaju unutar raspona ovog ispita. To smanjuje broj bridova grafa na $O(N \log N)$, a ukupna vremenska složenost je također $O(N \log N)$.</p>
''',
},
# ---------------------------------------------------------------- D
{
    'letter': 'D', 'title': 'Central Subset', 'title_hr': 'Središnji podskup', 'slug': 'D_central_subset',
    'tl': '2 s', 'ml': '256 MiB',
    'statement': r'''
<p>Dan je neusmjeren povezan graf s $N$ vrhova i $M$ bridova. Nađi podskup vrhova $S$ takav da je $|S| \le \lceil \sqrt{N} \rceil$ i da za svaki vrh $u$ postoji $v \in S$ s $\mathrm{dist}(u, v) \le \lceil \sqrt{N} \rceil$. Ako takav podskup ne postoji, ispiši $-1$.</p>
<h3>Ulaz</h3>
<p>$T \le 2 \cdot 10^4$ testova; $N \le 2 \cdot 10^5$, $M \le 10^6$, bez petlji i višestrukih bridova, graf povezan; $\sum N \le 2 \cdot 10^5$, $\sum M \le 10^6$.</p>
<h3>Izlaz</h3>
<p>$|S|$ i vrhovi skupa (bilo koje valjano rješenje), ili $-1$.</p>
<h3>Primjer</h3>
<p>Put $1-2-3-4$: $\lceil \sqrt 4 \rceil = 2$; valjani su npr. $\{2\}$, $\{3\}$, $\{1, 4\}$. Za drugi graf sa $6$ vrhova jedan odgovor je $\{2, 5, 6\}$.</p>
''',
    'hints': [
        r'''<p>Rješenje uvijek postoji. Zadaci na stablima obično su lakši od zadataka na grafovima: uzmi bilo koje razapinjuće stablo — udaljenosti u stablu su $\ge$ udaljenosti u grafu, pa podskup valjan za stablo valjan je i za graf.</p>''',
        r'''<p>Ukorijeni stablo, uzmi najdublji list $v$ i njegovog pretka $\mathrm{anc}(v)$ točno $\lceil \sqrt N \rceil$ razina iznad (ili korijen ako je $v$ pliće). Dodaj $\mathrm{anc}(v)$ u $S$ i ukloni cijelo njegovo podstablo; ponavljaj. Zašto se to događa najviše $\lceil \sqrt N \rceil$ puta?</p>''',
    ],
    'coach': [
        ('Opažanje 1: dovoljno je stablo', r'''<p>Za bilo koje razapinjuće stablo $T$ vrijedi $\mathrm{dist}_G(u, v) \le \mathrm{dist}_T(u, v)$. Ako nađemo $S$ koji pokriva stablo unutar $\lceil \sqrt N \rceil$, isti $S$ pokriva i graf. Razapinjuće stablo dobivamo DSU-om ili jednim DFS-om/BFS-om.</p>'''),
        ('Opažanje 2: pohlepno od najdubljeg lista', r'''<p>Ukorijeni stablo. Neka je $v$ najdublji list, a $\mathrm{anc}(v)$ predak $\lceil \sqrt N \rceil$ razina iznad (korijen ako je $v$ pliće). Svaki vrh $u$ u podstablu od $\mathrm{anc}(v)$ udaljen je od njega najviše $\lceil \sqrt N \rceil$, jer je $v$ najdublji. Dodaj $\mathrm{anc}(v)$ u $S$ i odreži cijelo podstablo — ostaje isti zadatak na manjem stablu.</p>'''),
        ('Argument brojanja', r'''<p>Svakom iteracijom dodajemo točno jedan vrh u $S$ i uklanjamo barem $\lceil \sqrt N \rceil$ vrhova (put od $v$ do $\mathrm{anc}(v)$), osim posljednje kad dodajemo korijen. Kako je vrhova $N$, iteracija je najviše $\lceil \sqrt N \rceil$, pa $|S| \le \lceil \sqrt N \rceil$. Odgovor $-1$ nikad se ne ispisuje.</p>'''),
        ('Algoritam i složenost', r'''<p>Naivno ponavljanje „nađi najdublji list” daje $O(N \sqrt N)$. Brže: predračunaj dubine i drži vrhove u skupu sortiranom po dubini, pa je ukupno $O(N \log N + (N + M)\,\alpha(N))$ uključujući DSU za razapinjuće stablo. Postoji i rješenje $O((N+M)\,\alpha(N))$ jednim DFS-om: pri povratku iz vrha prati visinu preostalog (neodrezanog) podstabla; kad dosegne $\lceil \sqrt N \rceil$, taj vrh dodaj u $S$ i podstablo tretiraj kao odrezano.</p>'''),
    ],
    'solution': r'''
<p>Može se dokazati da takav podskup uvijek postoji. Budući da su zadaci na stablima obično lakši od zadataka na grafovima, pretvorimo ovo u zadatak na stablu.</p>
<p>Uzmimo bilo koje razapinjuće stablo grafa. Ako nađemo valjani podskup za to stablo, isti će podskup biti valjan i za izvorni graf, jer je $\mathrm{dist}_G(u, v) \le \mathrm{dist}_T(u, v)$ za sve $u, v$.</p>
<p>Ukorijenimo razapinjuće stablo u proizvoljnom vrhu. Neka je $v$ najdublji list stabla. Neka je $\mathrm{anc}(v)$ predak od $v$ koji je $\lceil \sqrt N \rceil$ razina iznad $v$; ako je dubina od $v$ manja od $\lceil \sqrt N \rceil$, neka je $\mathrm{anc}(v)$ korijen.</p>
<p>Uočimo da za svaki vrh $u$ u podstablu od $\mathrm{anc}(v)$ vrijedi $\mathrm{dist}(u, \mathrm{anc}(v)) \le \lceil \sqrt N \rceil$. Zato dodamo $\mathrm{anc}(v)$ u $S$ i uklonimo podstablo ukorijenjeno u $\mathrm{anc}(v)$. Sada treba riješiti isti zadatak za manje stablo; rekurziramo dok ne dodamo korijen u $S$.</p>
<p>U svakoj iteraciji dodajemo točno jedan vrh u $S$, pa je $|S|$ jednak broju iteracija. U svakoj iteraciji uklanjamo iz stabla barem $\lceil \sqrt N \rceil$ vrhova. Kako vrhova ima samo $N$, iteracija može biti najviše $\lceil \sqrt N \rceil$. Stoga je $|S| \le \lceil \sqrt N \rceil$, pa je $S$ valjan podskup.</p>
<p>Naivno izvođenje gornjeg algoritma daje složenost $O(N \sqrt N)$, ali može se optimizirati ako predračunamo dubine svih vrhova i stavimo ih u skup. Budući da trebamo i DSU za razapinjuće stablo, konačna vremenska složenost je $O(N \log N + (N + M) \cdot \alpha(N))$, a prostorna $O(N)$. Postoji i alternativno rješenje složenosti $O((N + M) \cdot \alpha(N))$ s jednim DFS-om nakon dobivanja razapinjućeg stabla.</p>
''',
},
# ---------------------------------------------------------------- E
{
    'letter': 'E', 'title': 'Strange Keyboard', 'title_hr': 'Čudna tipkovnica', 'slug': 'E_strange_keyboard',
    'tl': '1.5 s', 'ml': '512 MiB',
    'statement': r'''
<p>Tipkovnica ima $N$ običnih tipki i tipku backspace. Počinješ s praznim stringom. Pritisak $i$-te obične tipke dodaje string $S_i$ na kraj; backspace ne radi ništa ako je trenutna duljina $\lt K$, a inače briše posljednjih $K$ znakova. Može li se dobiti string $T$ i koliko najmanje pritisaka treba?</p>
<h3>Ulaz</h3>
<p>$Q \le 100$ testova; $N \le 10^6$, $1 \le K \le 5000$; $\sum |S_i| \le 10^6$ i $\sum |T| \le 5000$ preko svih testova; mala slova engleske abecede.</p>
<h3>Izlaz</h3>
<p>Najmanji broj pritisaka ili $-1$.</p>
<h3>Primjer</h3>
<p>$K = 3$, $S = \{\texttt{defgh}, \texttt{abc}\}$, $T = \texttt{abcde}$: $\texttt{abc} \to \texttt{abcdefgh} \to$ backspace $\to \texttt{abcde}$, ukupno $3$. $K = 1$, $S = \{\texttt{a}\}$, $T = \texttt{b}$: $-1$.</p>
''',
    'hints': [
        r'''<p>$dp_i$ = najmanji broj poteza za točno prefiks duljine $i$ od $T$; $dp_i = \min_{j \lt i} dp_j + c(j+1, i)$, gdje je $c(x, y)$ cijena da se od nule napravi $T[x..y]$. Jedini stringovi koje možemo „ostaviti” su prefiksi nekog $S_i$ nakon što višak izbrišemo.</p>''',
        r'''<p>Definiraj $cost(x)$ = broj poteza da se s kraja izbriše točno $x$ znakova: $cost(0) = 0$; $x \ge K$: $1 + cost(x - K)$; $x \lt K$: $1 + \min_L cost(x + L)$ po duljinama $L$ ulaznih stringova (dodaš string pa brišeš). Različitih duljina je $O(\sqrt{\sum |S_i|})$. Zatim trie svih $S_i$.</p>''',
    ],
    'coach': [
        ('Opažanje 1: DP po prefiksima cilja', r'''<p>Konačni string se gradi „segment po segment”: $dp_i$ = najmanji broj poteza da string bude točno $T[1..i]$. $dp_i = \min_{j \lt i} \bigl(dp_j + c(j+1, i)\bigr)$, gdje je $c(x, y)$ najmanji broj poteza da od praznog stringa dobijemo točno $T[x..y]$. Kako je $\sum |T| \le 5000$, $O(|T|^2)$ prijelaza je u redu.</p>'''),
        ('Opažanje 2: brisanja ovise samo o duljinama', r'''<p>Segment $T[x..y]$ nastaje tako da dodamo neki $S_i$ čiji je prefiks $T[x..y]$ i onda izbrišemo višak od $|S_i| - (y-x+1)$ znakova — pri čemu smijemo dodavati još stringova (bilo kojih, važna je samo duljina) pa ih brisati. $cost(x)$ = najmanji broj poteza da se izbriše točno $x$ znakova s kraja: $cost(0) = 0$; za $x \ge K$: $cost(x) = 1 + cost(x-K)$; za $x \lt K$: $cost(x) = 1 + \min_L cost(x+L)$ po različitim duljinama $L$. Različitih duljina je $O(\sqrt{\sum|S_i|})$.</p>'''),
        ('Algoritam', r'''<p>1) Izračunaj $cost$ za $x \lt K + \max|S_i|$ u $O(\max|S_i| + K\sqrt{\sum|S_i|})$. 2) Ubaci sve $S_i$ u trie; čvoru na dubini $d$ pridruži $val = 1 + \min cost(D - d)$ po duljinama $D$ stringova koji prolaze tim čvorom (svaki string doprinosi svakom svojem pretku, ukupno $O(\sum|S_i|)$ parova). 3) Za svaki početak $x$ hodaj trie-om po $T[x..]$; $c(x, y)$ je $val$ dosegnutog čvora. 4) $dp$.</p>'''),
        ('Složenost i zamka', r'''<p>$O\!\left(K\sqrt{\sum|S_i|} + 26\sum|S_i| + |T|^2\right)$. Zbroj $K$ preko testova nije ograničen, pa bi $O(K^2)$ po testu ($100$ testova s $K = 5000$) bio prespor — otud trik s $O(\sqrt{\cdot})$ različitih duljina.</p>'''),
    ],
    'solution': r'''
<p>Koristimo dinamičko programiranje. Neka je $dp_i$ najmanji broj poteza potreban da se formira točno prefiks duljine $i$ od $T$. Prijelaz: $dp_i = \min(dp_j + c(j+1, i))$ po svim $j \lt i$, gdje je $c(x, y)$ najmanji broj poteza potreban da se od nule formira string $T[x : y]$.</p>
<p>Za računanje vrijednosti $c(x, y)$ prvo predračunamo $cost(x)$: broj poteza potreban da se s kraja trenutnog stringa izbriše točno $x$ znakova. Uočimo da brisanja uvijek možemo pokušati obraditi prije dodavanja, pa:</p>
<ul>
<li>$cost(0) = 0$;</li>
<li>ako je $x \ge K$, $cost(x) = 1 + cost(x - K)$ — prvo izbrišemo $K$ znakova;</li>
<li>ako je $x \lt K$, možemo pokušati dodati jedan od $N$ stringova. No nije važno koji string dodamo — samo njegova duljina. Dakle $cost(x) = 1 + \min(cost(x + L))$ po svim $L$ koji se pojavljuju kao duljina nekog $S_i$.</li>
</ul>
<p>Različitih duljina ulaznih stringova ima samo $O\!\left(\sqrt{\sum |S_i|}\right)$, pa se sve vrijednosti $cost$ računaju u $O\!\left(\max |S_i| + K\sqrt{\sum |S_i|}\right)$.</p>
<p>Konačno, sve $S_i$ stavimo u trie i pomoću niza $cost$ nađemo najmanji broj poteza za formiranje svakog prefiksa. To nam ujedno daje vrijednosti $c(x, y)$ koje trebamo za početni DP, jer su jedini relevantni stringovi koje možemo formirati kombinacije prefiksa stringova $S_i$.</p>
<p>Složenost je $O\!\left(K\sqrt{\sum|S_i|} + 26 \cdot \sum |S_i| + |T|^2\right)$. Napomena: zbroj $K$ preko testova nije ograničen, pa bi $O(K^2)$ po testu prekoračilo vremensko ograničenje.</p>
''',
},
# ---------------------------------------------------------------- F
{
    'letter': 'F', 'title': 'Longest Strictly Increasing Sequence', 'title_hr': 'Najdulji strogo rastući podniz', 'slug': 'F_longest_strictly_increasing_sequence',
    'tl': '1 s', 'ml': '256 MiB',
    'statement': r'''
<p>Dan je niz $b$ duljine $n$. Nađi niz $a$ duljine $n$ takav da je za svaki $i$ duljina najduljeg strogo rastućeg podniza od $a[1..i]$ jednaka $b[i]$, ili utvrdi da ne postoji.</p>
<h3>Ulaz</h3>
<p>$T \le 4000$ testova; $n \le 10$, $1 \le b[i] \le 10$, $\sum n \le 20000$. Traži se $1 \le a[i] \le 100$.</p>
<h3>Izlaz</h3>
<p><code>NO</code>, ili <code>YES</code> i niz $a$.</p>
<h3>Primjer</h3>
<p>$b = (1,2,3,2,5,7)$: <code>NO</code>. $b = (1, 2)$: <code>YES</code>, npr. $a = (1, 2)$ (ili $(4, 9)$, $(25, 26)$; $(5,5)$ i $(10,5)$ nisu točni).</p>
''',
    'hints': [
        r'''<p>Kako se duljina LIS-a prefiksa može mijenjati kad dodamo jedan element? Ne može pasti, a može porasti za najviše $1$. Dakle nužno je $b_1 = 1$ i $b_{i+1} - b_i \in \{0, 1\}$.</p>''',
        r'''<p>Isprobaj $a = b$: ako je $b$ neopadajući s koracima $0$/$1$ i $b_1 = 1$, najdulji strogo rastući podniz od $b[1..i]$ ima duljinu jednaku broju različitih vrijednosti, a to je upravo $b_i$.</p>''',
    ],
    'coach': [
        ('Opažanje: nužan uvjet', r'''<p>Dodavanje jednog elementa na kraj niza duljinu LIS-a ne smanjuje i povećava je za najviše $1$; LIS jednog elementa je $1$. Dakle $b_1 = 1$ i $b_{i+1} \in \{b_i, b_i + 1\}$, inače <code>NO</code>.</p>'''),
        ('Konstrukcija: $a = b$', r'''<p>Ako uvjet vrijedi, $b$ je neopadajući niz koji poprima sve vrijednosti $1, 2, \dots, b_i$ na prefiksu $[1..i]$. Strogo rastući podniz neopadajućeg niza uzima svaku vrijednost najviše jednom, a sve različite vrijednosti se mogu uzeti — LIS prefiksa je točno $b_i$. Vrijednosti su u $[1, 10] \subseteq [1, 100]$.</p>'''),
        ('Algoritam i složenost', r'''<p>Postavi $a = b$ i (radi sigurnosti) izravno provjeri LIS svakog prefiksa u $O(n^2)$ — $n \le 10$. Ako provjera prođe, <code>YES</code> i ispiši $a$; inače <code>NO</code>. Ukupno $O(\sum n^2)$.</p>'''),
    ],
    'solution': r'''
<p>Postoji mnogo valjanih rješenja. Jedno je odabrati $a = b$ i zatim provjeriti zadovoljava li dane LIS uvjete. Može se dokazati da, ako je odgovor <code>YES</code>, tada i $a = b$ zadovoljava uvjete.</p>
''',
},
# ---------------------------------------------------------------- G
{
    'letter': 'G', 'title': 'Perfect Strings', 'title_hr': 'Savršeni stringovi', 'slug': 'G_perfect_strings',
    'tl': '3 s', 'ml': '256 MiB',
    'statement': r'''
<p>Abeceda $\sigma$ ima $c$ znakova. String duljine $2n$ je <em>savršen</em> ako se njegovi indeksi $\{1, \dots, 2n\}$ mogu podijeliti u $n$ parova tako da za svaki par $(i, j)$ vrijedi $S[i] = S[j]$ i da se nikoja dva para ne „isprepliću”: za parove $(i, j), (k, l)$ ne smije biti $i \lt k \lt j \lt l$. Za dane $n$ i $c$ prebroji savršene stringove duljine $2n$ modulo $10^9 + 7$.</p>
<h3>Ulaz</h3>
<p>$T \le 10^5$ testova; $1 \le n, c \le 10^7$, $\sum n \le 10^7$.</p>
<h3>Izlaz</h3>
<p>Broj savršenih stringova.</p>
<h3>Primjer</h3>
<p>$n = 3, c = 1$: $1$. $n = 2, c = 2$: $6$ (<code>aaaa</code>, <code>aabb</code>, <code>abba</code>, <code>baab</code>, <code>bbaa</code>, <code>bbbb</code>).</p>
''',
    'hints': [
        r'''<p>Savršen string uvijek sadrži dva susjedna jednaka znaka (promotri „najuži” par u podjeli). Štoviše, susjedne jednake znakove uvijek smijemo spariti: ako je podjela imala $(i', i)$ i $(j', j)$ za susjedne $i, j$, valjano je i $(i, j), (i', j')$. Dakle string je savršen ako i samo ako ga stog (pop kad je vrh jednak trenutnom znaku, inače push) svede na prazan.</p>''',
        r'''<p>Neka je $f(n)$ broj savršenih stringova duljine $2n$, a $g(n)$ broj savršenih stringova duljine $2n+2$ koji počinju i završavaju istim fiksiranim znakom i čiji je stog prazan samo na početku i na kraju. Napiši rekurzije u Catalanovom stilu i prevedi ih u funkcije izvodnice: $G - 1 = (c-1)xG^2$, $F = 1/(1 - cxG)$.</p>''',
    ],
    'coach': [
        ('Opažanje 1: stog', r'''<p>U savršenom stringu postoje susjedni jednaki znakovi: uzmi par $(i, j)$ s najmanjim $j - i$; svaki $k$ s $i \lt k \lt j$ morao bi biti sparen s nečim između (inače isprepletanje), pa je $j = i+1$. Susjedne jednake znakove smijemo uvijek spariti (zamjena $(i',i),(j',j) \to (i,j),(i',j')$ čuva valjanost). Dakle: stog koji poništava jednake susjede mora završiti prazan.</p>'''),
        ('Opažanje 2: rekurzije', r'''<p>$g(n)$: stringovi duljine $2n+2$ oblika $a\,w\,a$ gdje $w$ nikad ne isprazni stog s vrhom $a$; prvi znak od $w$ je jedan od $c-1$ znakova $\ne a$ i on otvara blok: $g(0) = 1$, $g(n) = (c-1)\sum_{k=0}^{n-1} g(k)\,g(n-1-k)$. $f(n)$: prvi znak (bilo koji od $c$) otvara blok tipa $g$: $f(0) = 1$, $f(n) = c\sum_{k=0}^{n-1} g(k)\,f(n-1-k)$.</p>'''),
        ('Redukcija: funkcije izvodnice', r'''<p>$G(x) - 1 = (c-1)xG(x)^2 \Rightarrow G = \dfrac{1 - \sqrt{1 - 4(c-1)x}}{2(c-1)x}$. $F - 1 = cxGF \Rightarrow F = \dfrac{1}{1 - cxG}$. Uvrštavanjem i racionalizacijom nazivnika dobiva se oblik $\dfrac{\alpha + \beta\sqrt{1 - \gamma x}}{1 - \delta x}$; konkretno (provjera prevoditelja, slaže se s primjerima) $F(x) = \dfrac{c\sqrt{1 - 4(c-1)x} - (c-2)}{2(1 - c^2 x)}$. Za $c = 1$ odgovor je $1$ (dijeljenje s $c-1$ zahtijeva poseban slučaj).</p>'''),
        ('Algoritam i složenost', r'''<p>Koeficijenti $\sqrt{1 - \gamma x}$ dobivaju se iz $\binom{1/2}{k}(-\gamma)^k$ (Catalanovi brojevi do faktora), a $1/(1 - \delta x)$ je geometrijski niz; $[x^n]F = \frac{1}{2}\bigl(c\sum_{k=0}^{n} s_k\,\delta^{\,n-k} - (c-2)\delta^{\,n}\bigr)$. Uz predračunate faktorijele do $2 \cdot 10^7$ to je $O(n)$ po testu, ukupno $O(\sum n)$.</p>'''),
    ],
    'solution': r'''
<p>Uočimo da u svakom savršenom stringu negdje moraju postojati dva susjedna jednaka znaka. Inače promotrimo najbliži par u podjeli, recimo $(i, j)$. Očito je $j \gt i + 1$, a svaki $i \lt k \lt j$ morao bi ostati nesparen.</p>
<p>Također, za svaki takav par susjednih znakova optimalno ih je spariti međusobno. Naime, ako je podjela sadržavala $(i', i)$ i $(j', j)$, lako se provjeri da je valjano umjesto toga spariti $(i, j)$ i $(i', j')$.</p>
<p>To znači da, ako u savršenom stringu krenemo slijeva nadesno i stalno sparujemo (i uklanjamo) jednake znakove, na kraju moramo dobiti prazan string. To se simulira stogom: skidamo vrh ako je trenutni znak jednak vrhu stoga, inače trenutni znak stavljamo na stog.</p>
<p>Neka je $f(n)$ broj savršenih stringova duljine $2n$. Neka je $g(n)$ broj savršenih stringova duljine $2n + 2$ u kojima su prvi i posljednji znak oba $a$, a stog je prazan samo prije stavljanja prvog znaka i nakon obrade svih znakova.</p>
<p>Vrijedi $g(0) = 1$ i $g(n) = (c - 1)\sum_{k=0}^{n-1} g(k)\,g(n-1-k)$ za $n \ge 1$. Funkcija izvodnica $G(x)$ zadovoljava $G(x) - 1 = (c-1)\,x\,G^2(x)$, pa je $G(x) = \dfrac{1 - \sqrt{1 - 4(c-1)x}}{2(c-1)x}$.</p>
<p>Također $f(0) = 1$ i $f(n) = c\sum_{k=0}^{n-1} g(k)\,f(n-1-k)$ za $n \ge 1$. Stoga $F(x) - 1 = c\,x\,G(x)\,F(x)$, tj. $F(x) = \dfrac{1}{1 - c\,x\,G(x)}$.</p>
<p>Dakle $F(x) = \dfrac{1}{1 - \frac{c}{2(c-1)}\left(1 - \sqrt{1 - 4(c-1)x}\right)}$, što se može preurediti u oblik $\dfrac{\alpha + \beta\sqrt{1 - \gamma x}}{1 - \delta x}$ za neke konstante $\alpha, \beta, \gamma, \delta$. Razvoj toga daje formulu složenosti $O(n)$.</p>
''',
},
# ---------------------------------------------------------------- H
{
    'letter': 'H', 'title': 'Treelection', 'title_hr': 'Izbori u stablu', 'slug': 'H_treelection',
    'tl': '3 s', 'ml': '256 MiB',
    'statement': r'''
<p>Tvrtka ima $N$ zaposlenika; za $u \ge 2$ zaposlenik $P_u \lt u$ je nadređeni od $u$, a $1$ je direktor. „Vođa” od $u$ je bilo koji njegov (strogi) predak u tom stablu. Svaki zaposlenik osim direktora glasa za jednog od svojih vođa. Koji zaposlenici mogu biti <em>jedini pobjednik</em> izbora (strogo više glasova od svakog drugog)?</p>
<h3>Ulaz</h3>
<p>$T$ testova; $2 \le N \le 10^6$, $\sum N \le 10^6$; $P_2, \dots, P_N$ s $1 \le P_i \lt i$.</p>
<h3>Izlaz</h3>
<p>String duljine $N$; $i$-ti znak je <code>1</code> ako $i$ može biti jedini pobjednik.</p>
<h3>Primjer</h3>
<p>Lanac $1-2-3-4$: <code>1100</code> (npr. $2$ glasa za $1$, a $3$ i $4$ za $2$). $P = (1, 1, 2, 2)$: <code>10000</code>.</p>
''',
    'hints': [
        r'''<p>Neka je $f_{t,x}$ najmanji broj glasova koji iz podstabla od $x$ mora „otići” precima od $x$ ako svaki vrh smije dobiti najviše $t$ glasova: $f_{t,x} = [x \ne 1] + \max\!\bigl(0, \sum_{y \in \mathrm{children}(x)} f_{t,y} - t\bigr)$. Najmanji $z$ za koji je $f_{z,1} = 0$ nalazi se binarnim pretraživanjem.</p>''',
        r'''<p>Neka je $S_x$ broj strogih potomaka. $S_x \gt z$: $x$ sigurno može pobijediti (u raspodjeli gdje svi dobiju $\le z$ preusmjeri sve glasove iz podstabla na $x$). $S_x \lt z$: ne može (netko mora dobiti $\ge z$). Zanimljiv je slučaj $S_x = z$: $x$ mora dobiti točno $z$, a svi ostali $\lt z$ — promotri $f_{z-1,\cdot}$ i što se promijeni ako se ograničenje za $x$ opusti na $z$.</p>''',
    ],
    'coach': [
        ('Opažanje 1: „koliko mora proći gore”', r'''<p>Fiksiraj gornju granicu $t$ glasova po vrhu. Iz podstabla od $x$ prema strogim precima mora otići: vlastiti glas od $x$ (ako $x \ne 1$) plus glasovi djece koje $x$ ne može upiti: $f_{t,x} = [x \ne 1] + \max(0, \sum_y f_{t,y} - t)$. Raspodjela u kojoj svi dobiju $\le t$ postoji ako i samo ako $f_{t,1} = 0$. Funkcija je monotona u $t$ — binarno traži najmanji takav $z$.</p>'''),
        ('Opažanje 2: tri slučaja po $S_x$', r'''<p>Vrh $x$ može dobiti najviše $S_x$ glasova (strogi potomci). Ako je $S_x \gt z$: kreni od raspodjele sa svima $\le z$ i sve glasove iz podstabla od $x$ prebaci na $x$ — ostali samo gube glasove, $x$ ima $S_x \gt z$: pobjeda. Ako je $S_x \lt z$: $x$ ima $\le z - 1$, a po definiciji $z$ netko ima $\ge z$: nemoguće. Ostaje $S_x = z$.</p>'''),
        ('Redukcija: slučaj $S_x = z$', r'''<p>Trebamo raspodjelu u kojoj svi osim $x$ dobiju $\le z-1$, a $x$ točno $z$ (svi potomci glasaju za $x$, pa iz $x$ prema gore ide samo njegov vlastiti glas). Izračunaj $f_{z-1,\cdot}$ za sve vrhove. „Preljev” $\max(0, \sum_y f_{z-1,y} - (z-1))$ u $x$ iznosi najviše $1$ (jer je $S_x = z$); opuštanje granice za $x$ na $z$ znači postaviti taj preljev na $0$. Ako je preljev u $x$ već $0$, ništa se ne mijenja i $f_{z-1,1} \ge 1$ ostaje — nemoguće. Inače se smanjenje za $1$ širi prema korijenu, ali se zaustavlja kod prvog pretka čiji je preljev $0$; $x$ pobjeđuje ako i samo ako smanjenje stigne do korijena i ondje je $f_{z-1,1}$ bilo točno $1$.</p>'''),
        ('Algoritam i složenost', r'''<p>Binarno pretraživanje $z$: $O(N \log N)$. Zatim jedan prolaz za $f_{z-1}$ i jedan prolaz od korijena prema dolje koji označava vrhove do kojih se „lanac preljeva $\ge 1$” proteže od korijena (uz $f_{z-1,1} = 1$). Odgovor: $S_x \gt z$, ili $S_x = z$ uz preljev u $x$ jednak $1$ i označen lanac. Ukupno $O(N \log N)$.</p>'''),
    ],
    'solution': r'''
<p>Definirajmo $f_{t,x}$ kao najmanji broj glasova koji iz podstabla od $x$ mora otići njegovim precima ako svaki vrh smije dobiti najviše $t$ glasova:</p>
<p>$$f_{t,x} = [x \ne 1] + \max\!\Bigl(0, \sum_{y \in \mathrm{children}(x)} f_{t,y} - t\Bigr).$$</p>
<p><em>Napomena prevoditelja:</em> u službenom tekstu redoslijed oduzimanja u zagradi je zapisan obrnuto; gornji oblik odgovara opisu („glasovi koji moraju otići precima”).</p>
<p>Prvo nađemo najmanju vrijednost $z$ takvu da je moguće da svi dobiju $\le z$ glasova. Očito je $z$ najmanji $y$ za koji je $f_{y,1} = 0$, a nalazi se binarnim pretraživanjem.</p>
<p>Za vrh $x$, ako je veličina podstabla $S_x$ (računajući samo stroge potomke) veća od $z$, tada $x$ sigurno može biti jedini pobjednik: uzmemo glasanje u kojem svi dobiju $\le z$ glasova i u njemu glas svakog vrha iz podstabla od $x$ promijenimo u glas za $x$.</p>
<p>Ako je $S_x \lt z$, $x$ ne može biti jedini pobjednik, jer može dobiti najviše $z - 1$ glasova, a barem jedan vrh mora dobiti $\ge z$ glasova.</p>
<p>Ako je $S_x = z$, želimo osigurati da je $x$ jedini vrh koji dobije $z$ glasova, a svi ostali dobiju $\lt z$. Prvo nađemo vrijednosti $f_{z-1,y}$ za sve $y$; pri tome smo koristili uvjet da svaki vrh može dobiti najviše $z-1$ glasova. Treba jedna mala promjena: kakve su nove $f$-vrijednosti ako se ta granica za vrh $x$ podigne sa $z-1$ na $z$? Dakle želimo vidjeti promjenu $f$-vrijednosti ako $f_{z-1,x}$ (točnije njegov dio „preljeva” $\max(0, \cdot)$, koji je zbog $S_x = z$ najviše $1$) postavimo na $0$.</p>
<p>Ako neki predak $y$ od $x$ (uključujući sam $x$) ima preljev $0$, tada $x$ ne može biti jedini pobjednik, jer se $f$-vrijednosti predaka od $y$ — a time ni korijena — ne mogu promijeniti. Inače je preljev u $x$ jednak $1$ i $f$-vrijednosti predaka od $x$ možemo smanjiti za najviše $1$; dakle mora biti i $f_{z-1,1} = 1$.</p>
''',
},
# ---------------------------------------------------------------- I
{
    'letter': 'I', 'title': 'Disk Tree', 'title_hr': 'Stablo diskova', 'slug': 'I_disk_tree',
    'tl': '3 s', 'ml': '256 MiB',
    'statement': r'''
<p>Dano je $n$ diskova u ravnini koji se međusobno ne sijeku i ne dodiruju (rub pripada disku). Nacrtaj $n - 1$ dužina koje povezuju diskove tako da postoji put između svaka dva diska koji prolazi samo unutar diskova i po dužinama. Uvjeti: krajevi dužina su cjelobrojne točke u $[0, 10^9]^2$; dužina smije dodirivati ili sjeći najviše dva diska; dvije dužine se ne smiju sjeći ni dodirivati, osim što smiju dijeliti krajnju točku.</p>
<h3>Ulaz</h3>
<p>$2 \le n \le 2 \cdot 10^5$; $0 \le x_i, y_i \le 10^9$, $1 \le r_i \le 10^9$.</p>
<h3>Izlaz</h3>
<p><code>YES</code> i $n-1$ dužina $(x_1, y_1, x_2, y_2)$, ili <code>NO</code>.</p>
<h3>Primjer</h3>
<p>Diskovi $(1,0,3), (10,10,6), (0,5,1)$: <code>YES</code>, npr. dužine $(0,4)-(7,12)$ i $(0,0)-(16,8)$.</p>
''',
    'hints': [
        r'''<p>Rješenje uvijek postoji. Razmisli o sweep-lineu po $x$: događaji su krajnje lijeva ($x_i - r_i$) i krajnje desna ($x_i + r_i$) točka svakog diska. Aktivne diskove drži u skupu sortiranom po $y$ središta.</p>''',
        r'''<p>Kad disk postane aktivan, spoji njegovu krajnje lijevu točku <em>vertikalnom</em> dužinom s najbližim aktivnim diskom iznad ili ispod (po $y$) — vertikalni pravac kroz tu točku siječe taj disk, a disjunktnost diskova jamči da ništa nije između. Na kraju povezuj komponente (disjunktne intervale po $x$) dužinama u prazninama.</p>''',
    ],
    'coach': [
        ('Opažanje 1: sweep-line po $x$', r'''<p>Ključni događaji su $x_i - r_i$ (umetanje) i $x_i + r_i$ (brisanje). Skup $S$ aktivnih diskova sortiraj po $y$-koordinati središta. Za isti $x$ obradi po rastućem $y$, a umetanja prije brisanja.</p>'''),
        ('Opažanje 2: vertikalne spojnice su sigurne', r'''<p>Umetnuti disk $i$ u točki $x = x_i - r_i$ spoji vertikalnom dužinom od $(x, y_i)$ do $(x, y_j)$, gdje je $j$ susjed u $S$ (iznad ili ispod). Točka $(x, y_j)$ leži u disku $j$ jer je $j$ aktivan. Tetive različitih diskova na istom vertikalnom pravcu su disjunktne i poredane kao središta, pa dužina dodiruje samo $i$ i $j$. Ako pri istom $x$ ulazi više diskova, obrada po rastućem $y$ osigurava da se vertikalne dužine ne preklapaju.</p>'''),
        ('Algoritam', r'''<p>Nakon sweepa imamo komponente čije $x$-projekcije čine disjunktne intervale (komponenta se „zatvori” kad $S$ postane prazan). Susjedne komponente spoji dužinom od krajnje desne točke prethodne do krajnje lijeve točke sljedeće — u toj praznini nema diskova, pa dužina siječe samo ta dva diska i nikakve vertikalne dužine. Krajnje lijeve točke mogu imati negativan $x$: sve takve vertikalne dužine pomakni na $x = 0$ (svi ti diskovi sadrže neku točku pravca $x = 0$ jer su im središta u $x \ge 0$), pazeći opet na preklapanja.</p>'''),
        ('Složenost', r'''<p>$O(n \log n)$ za sortiranje događaja i operacije nad uređenim skupom; uvijek <code>YES</code>.</p>'''),
    ],
    'solution': r'''
<p>Radimo sweep po $x$-koordinatama slijeva nadesno; bitni događaji su krajnje lijeve i krajnje desne točke diskova ($x_i - r_i$ odnosno $x_i + r_i$). Krajnje lijeve točke su umetanja, krajnje desne su brisanja.</p>
<p>Tijekom sweepa održavamo skup $S$ „aktivnih” kružnica, sortiran po $y$-koordinati središta. Za fiksnu $x$-koordinatu obrađujemo po rastućoj $y$-koordinati, a umetanja prije brisanja. Zatim:</p>
<ul>
<li>Pri umetanju kružnice, vertikalnom je dužinom spojimo s najbližom kružnicom iz $S$ iznad/ispod nje. Najbližu kružnicu nalazimo binarnim pretraživanjem. Potom kružnicu umetnemo u $S$.</li>
<li>Pri brisanju kružnice samo je izbacimo iz $S$.</li>
</ul>
<p>Treba paziti da se tako stvorene vertikalne dužine ne preklapaju.</p>
<p>Na kraju sweepa imamo nekoliko povezanih komponenata kružnica, određenih disjunktnim intervalima duž $x$-osi. Da sve povežemo, crtamo dužine od lijevog kraja jednog intervala do desnog kraja prethodnog; one očito ne sijeku vertikalne dužine stvorene tijekom sweepa.</p>
<p>Neke vertikalne dužine mogle bi imati negativne $x$-koordinate; no sve ih se može pomaknuti na $x = 0$ bez gubitka povezanosti (ponovno pazeći da se ne preklapaju), jer sve kružnice imaju desne krajeve s pozitivnim $x$-koordinatama.</p>
''',
},
# ---------------------------------------------------------------- J
{
    'letter': 'J', 'title': 'Talk That Talk', 'title_hr': 'Talk That Talk', 'slug': 'J_talk_that_talk',
    'tl': '2 s', 'ml': '512 MiB',
    'statement': r'''
<p>Za binarni string $s$ i cijeli broj $t$, <em>$t$-vrijednost</em> je broj trojki $(i, j, k)$ s $1 \le i \lt j \lt k \le |s|$, $j - i = k - j$, $1 \le j - i \le t$ i $s_i = s_j = s_k$. Dan je prost broj $p$ i string $w$ duljine $p - 1$ u kojem je $w_x = 1$ ako postoji $z$ sa $z^2 \equiv x \pmod p$ (kvadratni ostatak), inače $0$. Izračunaj $t$-vrijednost od $w$.</p>
<h3>Ulaz</h3>
<p>$T \le 5 \cdot 10^5$ testova; $5 \le p \le 10^{12}$ prost, $1 \le t \le 10^6$, $\sum t \le 10^6$.</p>
<h3>Izlaz</h3>
<p>$t$-vrijednost za svaki test.</p>
<h3>Primjer</h3>
<p>$p = 13$: $w = 101100001101$, trojke su $(5,6,7), (6,7,8), (2,5,8), (5,8,11)$. Za $t = 1$ odgovor je $2$, za $t = 2$ također $2$. $p = 7, t = 32$: $0$.</p>
''',
    'hints': [
        r'''<p>Legendreov simbol $g_i = i^{(p-1)/2} \in \{-1, 1\}$ (i $g_0 = 0$). Za trojku $(i, i+d, i+2d)$ izraz $h_i = (g_i g_{i+d} + g_{i+d} g_{i+2d} + g_{i+2d} g_i + 1)/4$ jednak je $1$ ako su sva tri jednaka, a $0$ inače. Što se dobije ako se $\sum_i h_i$ uzme ciklički po svim $i = 1, \dots, p-1$ (indeksi modulo $p$)?</p>''',
        r'''<p>$\sum_{i=1}^{p-1} i^r \equiv 0 \pmod p$ za $1 \le r \lt p-1$ i $\equiv -1$ za $r = p-1$. Jer je $(i(i+d))^{(p-1)/2}$ polinom stupnja $p-1$ bez slobodnog člana, $\sum_i g_i g_{i+d} \equiv -1$, a kako je to zbroj $p-2$ vrijednosti $\pm 1$, jednako je točno $-1$. Ciklički zbroj po $d$ je dakle $(p-4)/4$; ostaje oduzeti „omotane” trojke ($i + 2d \ge p$), a njih je $O(t^2)$ ali se broje u $O(t)$.</p>''',
    ],
    'coach': [
        ('Opažanje 1: algebarski indikator', r'''<p>$w_i = 1$ točno kad je $g_i = i^{(p-1)/2} \equiv 1$; inače $g_i \equiv -1$. Za tri vrijednosti $\pm 1$ vrijedi $(g_a g_b + g_b g_c + g_c g_a + 1)/4 = 1$ ako su sve jednake, $0$ inače. Broj trojki s razlikom $d$ je $\sum_{i=1}^{p-1-2d} h_i$.</p>'''),
        ('Opažanje 2: ciklički zbroj je eksplicitan', r'''<p>Proširi zbroj na sve $i = 1..p-1$ s indeksima modulo $p$ (uz $g_0 = 0$). $g_i g_{i+d} = (i(i+d))^{(p-1)/2}$ je polinom u $i$ stupnja $p-1$ s vodećim koeficijentom $1$ i bez slobodnog člana; jer $\sum_{i=1}^{p-1} i^r \equiv 0$ za $1 \le r \lt p-1$ i $\equiv -1$ za $r = p-1$, dobivamo $\sum_i g_i g_{i+d} \equiv -1 \pmod p$. Zbroj ima $p-2$ pribrojnika $\pm 1$ (dva su nula), pa je točno $-1$. Ciklički zbroj za fiksni $d$ iznosi $(-3 + (p-1))/4 = (p-4)/4$ (u cijelim brojevima, prije oduzimanja omotanih članova).</p>'''),
        ('Redukcija: omotani članovi', r'''<p>Za svaki $d \le t$ treba oduzeti doprinos $i$ s $p - 2d \le i \lt p$. Svi ti indeksi (i njihova $+d$, $+2d$ pomaknuta verzija modulo $p$) leže u prozoru duljine $4t$ oko $p$: definiraj $A_{2t-i} = g_{p-i}$ za $1 \le i \le 2t$ i $A_{2t+i} = g_i$ za $0 \le i \lt 2t$. Traži se $\sum (A_a A_{a+d} + A_{a+d}A_{a+2d} + A_{a+2d}A_a + 1)$ po $0 \le a \lt 2t$, $1 \le d \le t$, $2t \le a + 2d \lt 4t$.</p>'''),
        ('Algoritam', r'''<p>Zbrajamo po parovima, ne po $d$: za fiksni prvi indeks skup dopuštenih drugih indeksa je kontinuirani raspon (za članove s pomakom $d$) ili raspon istog pariteta (za članove s pomakom $2d$), pa prefiksni/sufiksni zbrojevi niza $A$, posebno po parnim i neparnim indeksima, daju sve u $O(t)$. Za $p \le 2t+1$ ograniči $d$ na $\lfloor (p-2)/2 \rfloor$ (veći $d$ ne daju trojke); tako prozor $4t$ ne premašuje period.</p>'''),
        ('Složenost', r'''<p>$O(t \log p)$ po testu za računanje $4t$ Legendreovih simbola brzim potenciranjem (ili Eulerovim kriterijem), zatim $O(t)$; $\sum t \le 10^6$.</p>'''),
    ],
    'solution': r'''
<p>Promotrimo neku vrijednost razlike $d = j - i$. Treba $1 \le i \le p - 1 - 2d$. Dopustimo prvo cijeli raspon $1 \le i \lt p$, a zatim ćemo ukloniti doprinos svih $i$ za koje treba „omotavanje” ($p - 2d \le i \lt p$).</p>
<p>Neka je $g_i = i^{\frac{p-1}{2}}$ i $h_i = (g_i g_{i+d} + g_{i+d} g_{i+2d} + g_{i+2d} g_i + 1)/4$. Uočimo da je $h_i = 1$ ako je $w_i = w_{i+d} = w_{i+2d}$, a inače $h_i = 0$. Dakle broj trojki za dani $d$ je $\sum_{i=1}^{p-1} h_i$.</p>
<p>Vrijedi $\sum_{i=1}^{p-1} i^r \equiv 0 \pmod p$ za sve $1 \le r \lt p - 1$, te $\equiv p - 1 \pmod p$ za $r = p - 1$. Nadalje, $g_i g_{i+d} = (i(i+d))^{\frac{p-1}{2}} = i^{p-1} +$ (neka težinska suma nižih nenul potencija od $i$), pa je $\sum_{i=1}^{p-1} g_i g_{i+d} \equiv p - 1 \pmod p$.</p>
<p>Sada još treba ukloniti doprinos svih $1 \le i \lt p$, $1 \le d \le t$ s $i + 2d \ge p$. Formiramo novi niz $A$ duljine $4t$, gdje je $A_{2t-i} = g_{p-i}$ za $1 \le i \le 2t$ i $A_{2t+i} = g_i$ za $0 \le i \lt 2t$. U tom nizu treba naći zbroj $A_i A_{i+d} + A_{i+d} A_{i+2d} + A_{i+2d} A_i + 1$ po svim $i$ i $d$ koji zadovoljavaju $0 \le i \lt 2t$, $2t \le i + 2d \lt 4t$. To se može u $O(t)$ pomoću prefiksnih i sufiksnih zbrojeva pohranjenih zasebno za neparne i parne indekse.</p>
<p>Ukupna vremenska složenost je $O(t \log p)$, za računanje niza $A$.</p>
''',
},
# ---------------------------------------------------------------- K
{
    'letter': 'K', 'title': 'XOR Dice', 'title_hr': 'XOR kockice', 'slug': 'K_xor_dice',
    'tl': '1 s', 'ml': '256 MiB',
    'statement': r'''
<p>Dani su $n$ i $d$. Nađi $n$ kockica čije su strane označene nenegativnim cijelim brojevima $\le 10^6$ tako da su na svakoj kockici svih šest brojeva različiti i da je, kako god kockice pale, bitovni XOR $n$ gornjih brojeva uvijek djeljiv s $d$. Takve kockice uvijek postoje.</p>
<h3>Ulaz</h3>
<p>$1 \le n \le 100$, $2 \le d \le 60$.</p>
<h3>Izlaz</h3>
<p>$n$ redaka sa po šest različitih brojeva.</p>
<h3>Primjer</h3>
<p>$n = 3, d = 2$: npr. $[1,3,5,7,9,11]$, $[3,5,7,9,11,2023]$, $[0,2,4,6,100000,10]$; $7 \oplus 3 \oplus 2 = 6$ je djeljivo s $2$.</p>
''',
    'hints': [
        r'''<p>XOR ne „prenosi” između bitova, ali djeljivost s $d$ da. Kako natjerati XOR da se ponaša poput zbroja? Podijeli bitove u blokove od $6$ ($d \le 60 \lt 64$) i u svaki blok upiši ili $0$ ili $d$.</p>''',
        r'''<p>Brojevi $d \cdot (a_0 + a_1 2^6 + a_2 2^{12})$ s $a_i \in \{0, 1\}$: XOR bilo koliko takvih brojeva opet je takav broj (u svakom bloku XOR kopija od $d$ i nula daje $0$ ili $d$), dakle višekratnik od $d$. Ima ih $8$, a treba $6$ različitih po kockici.</p>''',
    ],
    'coach': [
        ('Opažanje: blokovi bitova', r'''<p>Kako je $d \le 60 \lt 2^6$, zapis od $d$ stane u $6$ bitova. Promotrimo brojeve čiji je svaki od blokova bitova $[0,5]$, $[6,11]$, $[12,17]$ jednak $0$ ili $d$: to su $d \cdot (a_0 + a_1 \cdot 2^6 + a_2 \cdot 2^{12})$, $a_i \in \{0,1\}$.</p>'''),
        ('Redukcija: zatvorenost na XOR', r'''<p>XOR se radi po blokovima neovisno (blokovi se ne preklapaju). U svakom bloku XOR-amo neke kopije $d$ i nule: rezultat je $d$ (neparno mnogo kopija) ili $0$. Dakle XOR bilo kojeg izbora gornjih strana opet je oblika $d \cdot (b_0 + b_1 2^6 + b_2 2^{12})$ — djeljiv s $d$.</p>'''),
        ('Algoritam i provjera ograničenja', r'''<p>Takvih brojeva je $2^3 = 8$; svaka kockica dobije bilo kojih $6$ od njih (sve kockice mogu biti jednake). Najveći je $d(1 + 64 + 4096) \le 60 \cdot 4161 = 249\,660 \le 10^6$. Složenost $O(n)$.</p>'''),
    ],
    'solution': r'''
<p>Promotrimo brojeve oblika $d \times (a_0 + a_1 \times 2^6 + a_2 \times 2^{12})$, gdje je svaki $a_i$ jednak $0$ ili $1$. To su brojevi kojima su bitovi $0 \dots 5$ jednaki ili $0$ ili $d$; isto tako bitovi $6 \dots 11$ jednaki su ili $0$ ili $d$, a isto vrijedi i za bitove $12 \dots 17$.</p>
<p>Za izbore $a_0, a_1, a_2$ postoji $8$ takvih brojeva, a za svaku kockicu možemo odabrati bilo kojih $6$ od njih.</p>
''',
},
# ---------------------------------------------------------------- L
{
    'letter': 'L', 'title': '(1, 2) Nim', 'title_hr': '(1, 2) Nim', 'slug': 'L_1_2_nim',
    'tl': '2 s', 'ml': '256 MiB',
    'statement': r'''
<p>Sprague i Grundy igraju s $N$ hrpa kamenčića, $A[i]$ u $i$-toj. Potez: odaberi nepraznu hrpu i ukloni iz nje proizvoljan pozitivan broj kamenčića. Sprague igra prvi i u svom potezu radi točno jedan potez. Grundy u svom redu najprije radi jedan potez, a zatim, ako je ostao barem jedan kamenčić, mora napraviti točno još jedan potez. Tko uzme posljednji kamenčić, pobjeđuje. Tko pobjeđuje uz optimalnu igru?</p>
<h3>Ulaz</h3>
<p>$T \le 10^4$ testova; $N \le 10^5$, $1 \le A[i] \le 10^9$, $\sum N \le 10^5$.</p>
<h3>Izlaz</h3>
<p><code>Sprague</code> ili <code>Grundy</code>.</p>
<h3>Primjer</h3>
<p>$(1, 2)$: <code>Grundy</code>. $(5)$: <code>Sprague</code>. $(1, 7, 2, 9)$: <code>Grundy</code>.</p>
''',
    'hints': [
        r'''<p>Riješi najprije slučaj u kojem su sve hrpe jedinice: Sprague uzima $1$, Grundy $2$ (ili posljednji $1$) — svaki krug nestaju $3$ kamenčića. Tko pobjeđuje ovisi o $N \bmod 3$.</p>''',
        r'''<p>Neka je $k$ broj hrpa s više od jednog kamenčića. Sprague može u jednom potezu $k = 1$ svesti na $k = 0$ s $N$ ili $N-1$ hrpa (spusti veliku hrpu na $1$ ili na $0$). Za $k \ge 2$ Sprague ne može doći do $k=0$, a Grundy s dva poteza uvijek može odgovoriti. Formuliraj tvrdnje za $k \ge 2$, $k = 1$, $k = 0$ i dokaži ih indukcijom.</p>''',
    ],
    'coach': [
        ('Opažanje 1: sve hrpe po $1$', r'''<p>Ako su sve hrpe jedinice, potezi su prisiljeni: Sprague uzima $1$, Grundy $2$ (ili $1$ ako je ostao samo jedan). Sprague pobjeđuje ako i samo ako $N \equiv 1 \pmod 3$ ($N = 1$: uzme ga; $N = 2, 3$: Grundy uzima ostatak; $N = 4$: nakon $1 + 2$ ostaje $1$ za Spraguea). Ako je Grundy na potezu s $N$ jedinica, gubi ako i samo ako $N \equiv 0 \pmod 3$.</p>'''),
        ('Opažanje 2: hrpe veće od $1$', r'''<p>Neka je $k$ broj hrpa s $\gt 1$ kamenčićem. Za $k = 1$ Sprague može veliku hrpu spustiti na $1$ ili $0$ i predati Grundyju $N$ ili $N-1$ jedinica; to je pobjeda ako je $N \equiv 0$ ili $N - 1 \equiv 0 \pmod 3$, tj. $N \not\equiv 2$. Pokazuje se da za $N \equiv 2$ ni drugi potezi ne pomažu. Za $k \ge 2$ Sprague ne može stvoriti poziciju sa svim jedinicama, a Grundy sa svoja dva poteza uvijek vrati Spraguea u gubitničku poziciju.</p>'''),
        ('Tvrdnje (dokaz indukcijom)', r'''<p>Na potezu Spraguea: $k \ge 2 \Rightarrow$ Sprague gubi; $k = 1 \Rightarrow$ Sprague pobjeđuje ako i samo ako $N \not\equiv 2 \pmod 3$; $k = 0 \Rightarrow$ Sprague pobjeđuje ako i samo ako $N \equiv 1 \pmod 3$. Na potezu Grundyja: gubi ako i samo ako su sve hrpe jedinice i $N \equiv 0 \pmod 3$. Indukcija po ukupnom broju kamenčića provjerava da iz svake „pobjedničke” pozicije postoji potez u „gubitničku” i obrnuto.</p>'''),
        ('Algoritam i složenost', r'''<p>Prebroji $k$ i primijeni tvrdnje: $O(N)$ po testu.</p>'''),
    ],
    'solution': r'''
<p>Sve sljedeće tvrdnje dokazuju se indukcijom. Neka je $k$ broj hrpa koje sadrže više od jednog kamenčića.</p>
<ul>
<li>Ako je $k \ge 2$, prvi igrač gubi.</li>
<li>Ako je $k = 1$, prvi igrač pobjeđuje ako i samo ako $N \not\equiv 2 \pmod 3$.</li>
<li>Ako je $k = 0$, prvi igrač pobjeđuje ako i samo ako $N \equiv 1 \pmod 3$.</li>
<li>Ako je na potezu drugi igrač, on gubi ako i samo ako sve hrpe imaju po jedan kamenčić i $N \equiv 0 \pmod 3$.</li>
</ul>
''',
},
# ---------------------------------------------------------------- M
{
    'letter': 'M', 'title': 'Graphs and Colors', 'title_hr': 'Grafovi i boje', 'slug': 'M_graphs_and_colors',
    'tl': '1 s', 'ml': '256 MiB',
    'statement': r'''
<p>Dan je potpuni graf s $N$ vrhova. Svaki brid oboji jednom od $K$ boja tako da za svaku boju $j$ graf sastavljen od svih $N$ vrhova i bridova boje $j$ ima dijametar $d_j \le 4$ (udaljenost nepovezanih vrhova je $\infty$).</p>
<h3>Ulaz</h3>
<p>$T$ testova; $2 \le N \le 100$, $1 \le K \le N(N-1)/2$, $\sum N \le 10^4$.</p>
<h3>Izlaz</h3>
<p><code>NO</code>, ili <code>YES</code> i $N-1$ redaka: u $i$-tom redu $i$ brojeva, $j$-ti je boja brida $(j, i+1)$.</p>
<h3>Primjer</h3>
<p>$N = 5, K = 10$: <code>NO</code>. $N = 5, K = 2$: <code>YES</code>, npr. redovi <code>1</code> / <code>2 1</code> / <code>2 2 1</code> / <code>1 2 2 1</code>.</p>
''',
    'hints': [
        r'''<p>Konačan dijametar znači da je graf svake boje povezan na svih $N$ vrhova, pa ima barem $N-1$ bridova. Iz $K(N-1) \le N(N-1)/2$ slijedi $K \le \lfloor N/2 \rfloor$. Pokaži da je to i dovoljno.</p>''',
        r'''<p>Za parni $N$ i $K = N/2$: vrhove grupiraj u parove $(2k, 2k+1)$ „boje $k$”. Brid unutar para ima boju $k$; između parova $i \lt j$ „paralelne” bridove $(2i,2j),(2i+1,2j+1)$ oboji s $i$, a „ukrižene” $(2i,2j+1),(2i+1,2j)$ s $j$. Svaki vrh je tada u boji $i$ susjedan s $2i$ ili $2i+1$.</p>''',
    ],
    'coach': [
        ('Opažanje: nužan uvjet', r'''<p>Dijametar $\le 4$ podrazumijeva povezanost svih $N$ vrhova u svakoj boji, dakle $\ge N-1$ bridova po boji. Ukupno $K(N-1) \le \binom N2 \Rightarrow K \le N/2$. Ako je $K \gt \lfloor N/2 \rfloor$: <code>NO</code>.</p>'''),
        ('Redukcija: dovoljno je $K = \lfloor N/2 \rfloor$', r'''<p>Ako imamo konstrukciju za $K_0 = \lfloor N/2 \rfloor$ boja, za manji $K$ sve bridove boja $\ge K$ (0-indeksirano) prebojimo u boju $0$: dodavanje bridova ne povećava dijametar.</p>'''),
        ('Konstrukcija za parni $N$', r'''<p>Za $0 \le k \lt N/2$ vrhovi $2k, 2k+1$ su „predstavnici” boje $k$; brid $(2k, 2k+1)$ ima boju $k$. Za $i \lt j$: $(2i, 2j)$ i $(2i+1, 2j+1)$ boje $i$, a $(2i, 2j+1)$ i $(2i+1, 2j)$ boje $j$. U boji $i$ svaki vrh $2j$ odnosno $2j+1$ ($j \ne i$) susjedan je s $2i$ ili $2i+1$, a $2i$ i $2i+1$ su susjedni; svaka dva vrha spaja put duljine $\le 3$ preko predstavnika. Svaki brid dobio je točno jednu boju.</p>'''),
        ('Neparni $N$ i složenost', r'''<p>Riješi za $N - 1$ pa zadnji vrh $N-1$ spoji s vrhom $i$ bridom boje $\lfloor i/2 \rfloor$: on je tako susjedan s oba predstavnika svake boje. Ispis u $O(N^2)$ po testu.</p>'''),
    ],
    'solution': r'''
<p>Svaki podgraf treba barem $N - 1$ bridova, pa je $K \le \frac{N}{2}$. Taj je uvjet i dovoljan. Konstruirat ćemo rješenje za $K = \lfloor N/2 \rfloor$; ako je $K \lt \lfloor N/2 \rfloor$, sve bridove boje $\ge K$ prebojimo u boju $0$ (boje indeksiramo od $0$).</p>
<p>Pretpostavimo prvo da je $N$ paran. Za svaki $0 \le k \lt \frac N2$ neka vrhovi $2k, 2k+1$ budu vrhovi boje $k$; brid $(2k, 2k+1)$ obojimo bojom $k$. Za svaki $0 \le i \lt j \lt K$ bridove $(2i, 2j)$ i $(2i+1, 2j+1)$ obojimo bojom $i$, a bridove $(2i, 2j+1)$ i $(2i+1, 2j)$ bojom $j$.</p>
<p>Za svaki $j \ne i$ vrh $2j$ susjedan je (u boji $i$) s $2i$ ili $2i+1$; isto vrijedi za vrh $2j+1$, pa je dijametar svake boje $i$ najviše $3$.</p>
<p>Za neparni $N$ prvo napravimo rješenje za $N - 1$, a zatim za svaki $i \lt N-1$ brid $(i, N-1)$ obojimo bojom $\lfloor i/2 \rfloor$.</p>
''',
},
# ---------------------------------------------------------------- N
{
    'letter': 'N', 'title': 'Red Black Grid', 'title_hr': 'Crveno-crna mreža', 'slug': 'N_red_black_grid',
    'tl': '1 s', 'ml': '256 MiB',
    'statement': r'''
<p>Za dane $N$ i $K$ konstruiraj $N \times N$ mrežu čija je svaka ćelija crvena ili crna, tako da postoji točno $K$ neuređenih parova susjednih (dijele stranicu) ćelija različitih boja, ili utvrdi da ne postoji.</p>
<h3>Ulaz</h3>
<p>$T \le 10^4$ testova; $1 \le N \le 10^3$, $0 \le K \le 2N(N-1)$, $\sum N^2 \le 10^6$.</p>
<h3>Izlaz</h3>
<p><code>Impossible</code>, ili <code>Possible</code> i $N$ redaka s <code>R</code>/<code>B</code>.</p>
<h3>Primjer</h3>
<p>$N = 3, K = 6$: <code>BRB</code> / <code>RBB</code> / <code>BBB</code>. $N = 3, K = 1$: <code>Impossible</code>.</p>
''',
    'hints': [
        r'''<p>Najviše je $2N(N-1)$ parova (šahovnica). Zašto su $K = 1$ i $K = 2N(N-1) - 1$ nemogući, a sve ostalo (za $N \ge 4$) moguće?</p>''',
        r'''<p>Oboji sve „neparne” ćelije ($i + j$ neparno) crno. Parne ćelije nisu međusobno susjedne, pa svaka crvena parna ćelija doprinosi točno svoj stupanj ($2$, $3$ ili $4$ susjeda). Treba odabrati podskup parnih ćelija sa zbrojem stupnjeva $K$.</p>''',
    ],
    'coach': [
        ('Opažanje 1: parne i neparne ćelije', r'''<p>0-indeksirano, ćelija $(i, j)$ je neparna ako je $i + j$ neparno. Susjedne ćelije uvijek imaju različit paritet. Ako su sve neparne ćelije crne, a od parnih neke crvene, broj raznobojnih parova jednak je zbroju stupnjeva (broja susjeda) crvenih parnih ćelija — parne ćelije nikad nisu susjedne međusobno.</p>'''),
        ('Opažanje 2: koje zbrojeve možemo dobiti', r'''<p>Stupnjevi su $2$ (kutovi), $3$ (rub), $4$ (unutrašnjost); za $N \ge 4$ postoje parne ćelije svakog od tih stupnjeva. Zbroj svih stupnjeva parnih ćelija je točno $2N(N-1)$ (svaki susjedni par sadrži jednu parnu ćeliju). Podskup sa zbrojem $1$ ne postoji, a zbroj $2N(N-1) - 1$ zahtijevao bi izostaviti ćeliju stupnja $1$ — nema je. Ostali $K$ su dostižni.</p>'''),
        ('Algoritam', r'''<p>$N \le 3$: gruba sila po svim bojanjima ($2^9$). $N \ge 4$: ako je $K \gt N(N-1)$, riješi za $2N(N-1) - K$ i uzmi komplement skupa parnih ćelija (zbroj stupnjeva je komplementaran). Zatim pohlepno: uzimaj ćelije stupnja $4$ dok je ostatak $\ge 4$; ostatak $r \in \{0, 2, 3\}$ pokrij jednom ćelijom stupnja $2$ ili $3$; za $r = 1$ zamijeni jednu četvorku ćelijama stupnja $2$ i $3$ ($2 + 3 = 5$). Provjeri da ćelija svakog stupnja ima dovoljno, što za $N \ge 4$ vrijedi.</p>'''),
        ('Složenost', r'''<p>$O(N^2)$ po testu za ispis mreže; $\sum N^2 \le 10^6$.</p>'''),
    ],
    'solution': r'''
<p>Rješenje ne postoji ako je $K = 1$ ili $K = 2 \times N \times (N-1) - 1$. Za $N \le 3$ može se primijeniti gruba sila; dalje pretpostavljamo $N \ge 4$.</p>
<p>Indeksirajmo od $0$ i nazovimo ćeliju $(i, j)$ neparnom ako je $i + j \equiv 1 \pmod 2$, a parnom inače. Prvo sve neparne ćelije obojimo jednom bojom (crno).</p>
<p>Neka je stupanj ćelije broj ćelija susjednih njoj. Želimo da zbroj stupnjeva crvenih ćelija bude jednak $K$. Za svaki $d = 2, 3, 4$ postoji pozitivan broj parnih ćelija stupnja $d$.</p>
<p>Dovoljno je proći parne ćelije po padajućem stupnju i pohlepno odlučivati hoćemo li ih uključiti, uz nekoliko malih prilagodbi.</p>
''',
},
]
