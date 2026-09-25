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
    'solution': r'''
<p>Kad primijenimo potez $x \to x \oplus (x - 2^i)$, dobivamo $2^i$ ako je bit $i$ postavljen u $x$, a inače vrijednost koja ima postavljene točno bitove $[i, j]$, gdje je $j$ najmanji bit $\gt i$ postavljen u $x$.</p>
<p>Ako je najviši postavljeni bit među svim vrijednostima $k$, što god radili ne možemo postaviti nijedan bit $\gt k$. Ali uvijek možemo postaviti sve bitove $\le k$: odaberi bilo koji element $x$ s postavljenim $k$-tim bitom, zamijeni ga s $x \oplus (x - 2^k) = 2^k$, a zatim $2^k$ zamijeni s $2^k \oplus (2^k - 2^0) = 2^{k+1} - 1$. Dakle najveći mogući odgovor je $2^{k+1} - 1$ i postiže se u $\le 2$ poteza.</p>
<p>Ako je početni ILI već $2^{k+1} - 1$, potrebno je $0$ poteza. Inače treba odlučiti možemo li proći s jednim potezom. Neka je $l$ najniži, a $r$ najviši bit $\le k$ koji nije postavljen ni u jednoj vrijednosti.</p>
<p>Vrijednost nazovimo <em>posebnom</em> ako postoji bit postavljen samo u njoj. Posebne vrijednosti obrađujemo odvojeno; sve ih je lako naći u $O(\log M)$ ako za svaki indeks predračunamo sljedeću poziciju koja sadrži dani bit.</p>
<p>Potez na neposebnoj vrijednosti $x$ uspijeva ako i samo ako su svi bitovi u rasponu $[l, r]$ u $x$ nule i $x \gt 2^r$. Postoji li takva vrijednost provjeravamo tako da za svaki $r$ pohranimo segmentno stablo minimuma nad nizom čiji je $i$-ti element najveći bit $b \le r$ sadržan u $A_i$.</p>
<p>Promotrimo sada posebnu vrijednost $x$. Ako je bit $j$ sadržan samo u $x$, moramo osigurati da $j$-ti bit ostane postavljen i nakon operacije. Primijetimo da $j$ mora biti jedini posebni bit od $x$, jer postoji najviše jedan bit koji je jedinica i prije i poslije primjene operacije. Dakle moramo odabrati neki $i \le l$ takav da je $j$ najmanji bit $\gt l$ postavljen u $x$. To radi ako su svi bitovi u $[l, r]$ u $x$ nule i $j \gt r$.</p>
''',
    'coach': [
        (r'Što točno potez radi s binarnim zapisom broja $x$?',
         r'''<p>Oduzimanje $2^i$ mijenja samo bitove od $i$ prema gore: ako je bit $i$ postavljen, on se ugasi i ništa drugo; inače „posudba” pretvori nule na pozicijama $i, \dots, j-1$ u jedinice i ugasi bit $j$, gdje je $j$ najniži postavljeni bit iznad $i$. XOR s $x$ zadrži točno promijenjene bitove: rezultat je <strong>blok jedinica $[i, j]$</strong> (u prvom slučaju $j = i$, tj. $2^i$). Rezultat je dakle uvijek blok $[i, j]$ gdje je $j$ postavljen u $x$, a $x$ nema postavljenih bitova strogo između $i$ i $j$; svi ostali bitovi od $x$ su izgubljeni.</p>'''),
        (r'Koja je najveća moguća vrijednost ILI-ja i zašto ne veća?',
         r'''<p>Blok $[i, j]$ nikad ne prelazi najviši bit $j$ od $x$, pa nijedan potez ne stvara bit iznad $k$ = najvišeg bita koji se pojavljuje u $B$: maksimum je $\le 2^{k+1} - 1$. S druge strane, dva poteza na elementu $x$ s bitom $k$ daju točno taj broj: $i = k$ daje $2^k$, a zatim $i = 0$ na $2^k$ daje blok $[0, k] = 2^{k+1} - 1$. Ostaje samo pitanje treba li $0$, $1$ ili $2$ poteza.</p>'''),
        (r'Kad je dovoljan jedan potez?',
         r'''<p>Neka su $l \le r$ najniži i najviši bit koji nedostaju u ILI-ju $O$. Jedan potez mijenja jedan element $x$ u blok $[i, j]$ koji mora sadržavati $l$ i $r$ ($i \le l$, $j \ge r + 1$), pa $x$ ne smije imati postavljene bitove u $[i, j-1] \supseteq [l, r]$ i mora imati neki bit iznad $r$. Uz to, bitove koje je jedino $x$ držao (posebne bitove) ne smijemo izgubiti — oni moraju ostati u bloku, a blok od bitova od $x$ zadržava samo $j$. Dakle: $x \ge 2^{r+1}$, $x$ nema bitova u $[l, r]$, i svaki posebni bit od $x$ jednak je $j$ (najnižem bitu od $x$ iznad $r$). Takav $x$ s potezom $i = l$ daje puni ILI.</p>'''),
        (r'Kako to provjeriti brzo za $10^5$ upita?',
         r'''<p>Podijelimo elemente na <em>posebne</em> (drže barem jedan bit sami) i ostale. Posebnih je u rasponu najviše $31$ — po jedan za svaki bit s brojem pojavljivanja $1$ — a nalazimo ih preko prefiksnih brojača bitova i tablice „prva pozicija $\ge i$ s bitom $b$”; svakog provjerimo izravno. Za neposebne treba samo znati postoji li u $[L, R]$ element s $x \ge 2^{r+1}$ i bez bitova u $[l, r]$; uvjet „bez bitova u $[l,r]$” znači da je najviši bit od $x$ koji je $\le r$ manji od $l$. Zato za svaki $r$ pozicije elemenata $\ge 2^{r+1}$ grupiramo po tom najvišem bitu; upit prebroji pozicije u $[L, R]$ u grupama s vrijednošću $\lt l$ binarnim pretraživanjem i oduzme posebne koji su ondje ubrojeni.</p>'''),
    ],
    'tips': [
        r'''Operacije oblika $x \oplus (x - 2^i)$, $x \,\&\, (x-1)$, $x \oplus (x+1)$ i slične uvijek prvo „prevedi” u riječi: koje bitove mijenjaju i kako — gotovo uvijek ispadne blok uzastopnih bitova.''',
        r'''Kad je odgovor ograničen malom konstantom (ovdje $0$, $1$ ili $2$ poteza), zadatak se pretvara u niz odluka „je li moguće u $t$ poteza?”; najlakše granice dokaži prvo (maksimum i gornja ograda broja poteza), pa razradi jedini netrivijalni slučaj.''',
        r'''Elementi koji sami drže neki bit („posebni”) su rijetki — najviše onoliko koliko ima bitova; obradi ih izravno, a masu ostalih prebroji strukturom podataka.''',
        r'''Za upite oblika „postoji li u $[L,R]$ element s bitovnim svojstvom” s $\approx 30$ mogućih parametara, sortirani vektori pozicija po parametru i binarno pretraživanje često su jednostavniji od segmentnog stabla.''',
    ],
    'detailed': r'''
<h3>1. Što potez radi</h3>
<p>Fiksirajmo $x \ge 2^i$ i pogledajmo $y = x - 2^i$. Bitovi ispod $i$ se ne mijenjaju. Ako je bit $i$ postavljen u $x$, oduzimanje ga samo ugasi: $x \oplus y = 2^i$. Ako nije, oduzimanje traži „posudbu”: neka je $j \gt i$ najniži postavljeni bit od $x$ iznad $i$ (postoji jer je $x \ge 2^i$ i bit $i$ nije postavljen, pa $x \gt 2^i$). Tada $y$ ima bit $j$ ugašen, bitove $i, \dots, j-1$ upaljene (u $x$ su bili $0$) i sve ostalo isto. Zato je $x \oplus y$ točno blok jedinica na pozicijama $[i, j]$. Zaključak, uključujući prvi slučaj kao $j = i$:</p>
<p style="text-align:center">$x \;\to\; \text{blok } [i, j],\quad j = \text{najniži bit od } x \text{ koji je } \ge i.$</p>
<p>Svi ostali bitovi od $x$ nestaju. Rezultat ne može imati bit iznad najvišeg bita od $x$.</p>
<h3>2. Maksimalni ILI</h3>
<p>Neka je $O$ ILI raspona i $k$ njegov najviši bit (ako je $O = 0$, odgovor je $0\ 0$). Po prethodnom, nijedan potez ne stvara bit $\gt k$ (ni kasnije: najviši bit u nizu nikad ne raste), pa je ILI uvijek $\le 2^{k+1} - 1$. Ta se vrijednost postiže u najviše dva poteza na bilo kojem elementu $x$ s bitom $k$: $i = k$ daje $2^k$; zatim na $2^k$ potez $i = 0$ daje blok $[0, k] = 2^{k+1} - 1$, koji kao član niza sam čini ILI punim. Dakle <strong>najveći ILI je uvijek $2^{k+1} - 1$</strong>, a broj poteza je $0$, $1$ ili $2$.</p>
<h3>3. Nula poteza</h3>
<p>Ako je $O = 2^{k+1} - 1$, odgovor je $0$. Inače postoje bitovi ispod $k$ koji nedostaju; neka su $l$ i $r$ najniži i najviši od njih ($0 \le l \le r \lt k$).</p>
<h3>4. Točan uvjet za jedan potez</h3>
<p>Jedan potez mijenja jedan element $x$ u blok $[i, j]$. Novi ILI je $O' \,|\, [i,j]$, gdje je $O'$ ILI <em>ostalih</em> elemenata. Potez uspijeva ako i samo ako:</p>
<ol>
<li>blok pokriva sve bitove koji nedostaju: $i \le l$ i $j \ge r+1$, i</li>
<li>nijedan bit od $O$ nije izgubljen: svaki bit koji drži samo $x$ (<em>posebni bit</em> od $x$) mora biti u bloku $[i, j]$.</li>
</ol>
<p>Uvjet 1 znači da $x$ nema postavljenih bitova u $[i, j-1] \supseteq [l, r]$ i da ima neki bit iznad $r$, tj. $x \ge 2^{r+1}$ i $x \,\&\, [l..r] = 0$. Ako $x$ zadovoljava to, potez $i = l$ (bit $l$ nije postavljen, $2^l \le x$) daje blok $[l, j]$ s $j$ = najniži bit od $x$ iznad $r$, koji pokriva $[l, r]$ i sve nedostajuće bitove između (oni su svi u $[l, r]$). Manji $i \lt l$ ne pomaže: da bi blok i tada pokrio $[l, r]$, $x$ ne smije imati bitove u $[i, r]$, pa je rezultat $[i, j]$ s istim $j$, a jedini dodatni pokriveni bitovi $[i, l-1]$ već su u $O$.</p>
<p>Za uvjet 2 primijetimo da od bitova od $x$ blok $[i, j]$ zadržava <em>samo</em> $j$ (bitovi ispod $i$ i iznad $j$ su izgubljeni, a između nije bilo postavljenih). Zato posebni bitovi od $x$ moraju svi biti jednaki $j$ — $x$ ima najviše jedan posebni bit i to baš $j$. Element bez posebnih bitova automatski zadovoljava uvjet 2.</p>
<p><strong>Zaključak.</strong> Jedan potez dovoljan je ako i samo ako u $[L, R]$ postoji $x$ takav da (a) $x \ge 2^{r+1}$ i $x$ nema bitova u $[l, r]$, te (b) svaki posebni bit od $x$ jednak je najnižem bitu od $x$ iznad $r$. U protivnom je odgovor $2$.</p>
<h3>5. Brza provjera</h3>
<p>Za svaki bit $b \lt 31$ pripremimo prefiksne brojače $cnt_b[i]$ (koliko od $A_1..A_i$ ima bit $b$) i $nxt_b[i]$ (prva pozicija $\ge i$ s bitom $b$). Za upit:</p>
<ul>
<li>$O$ i $k$ dobivamo iz $cnt$ u $O(31)$; isto $l$ i $r$.</li>
<li><em>Posebni elementi.</em> Bit $b$ je poseban ako je $cnt_b[R] - cnt_b[L-1] = 1$; tada ga drži element na poziciji $nxt_b[L]$. Skup takvih pozicija ima najviše $31$ element. Za svaki provjerimo uvjete (a) i (b) izravno u $O(31)$.</li>
<li><em>Neposebni elementi.</em> Uvjet (b) je automatski, treba samo (a). Za neposebni $x$ uvjet „nema bitova u $[l, r]$” ekvivalentan je s „najviši bit od $x$ koji je $\le r$ manji je od $l$” (ili ne postoji). Zato za svaki $r \in [0, 30]$ pozicije elemenata $\ge 2^{r+1}$ razvrstamo u $32$ sortirana vektora prema tom najvišem bitu $v \in \{-1, 0, \dots, r\}$. Upit zbroji, za $v \lt l$, broj pozicija u $[L, R]$ (dva binarna pretraživanja po vektoru) i oduzme broj posebnih elemenata koji zadovoljavaju (a) — oni su također u tim vektorima. Ako ostane barem jedan, postoji neposebni kandidat i odgovor je $1$.</li>
</ul>
<p>Predračun je $O(31 N)$ vremena i memorije (svaka pozicija je u najviše $31$ vektoru), upit $O(31 \log N + 31^2)$. Uz $\sum N, \sum Q \le 10^5$ to je daleko unutar limita.</p>
<h3>6. Primjer</h3>
<p>$A = (10, 10, 5)$, upit $(1, 2)$: $O = 10 = 1010_2$, $k = 3$, puni ILI $15$; nedostaju bitovi $0$ i $2$, $l = 0$, $r = 2$. Oba elementa su $10$, nijedan bit nije poseban. Uvjet (a): $10 \ge 8$, ali $10$ ima bit $1 \in [0, 2]$ — ne. Odgovor $15\ 2$ (npr. $10 \to 3$ potezom $i=0$ i $10 \to 12$ potezom $i=2$, kako navodi primjer). Upit $(1,3)$: $O = 15$, $0$ poteza. Još dva mala primjera: $A = (15)$, upit $(1,1)$: $O = 15$ je već pun, $15\ 0$. Za $A = (8)$: $O = 8$, $l = 0$, $r = 2$, element $8$ je poseban za bit $3 = j$, pa jedan potez ($i = 0$: $8 \to 15$) — odgovor $15\ 1$.</p>
<h3>7. Zamke</h3>
<ul>
<li>$A_i \le 10^9 \lt 2^{30}$, ali puni ILI $2^{k+1}-1$ može biti $2^{30} - 1$; računati u 64 bita ili barem paziti na pomake ($1 \ll 31$ je nedefinirano za <code>int</code>).</li>
<li>Uvjet (a) mora tražiti da su <em>svi</em> bitovi $[l, r]$ nule, ne samo krajevi — provjera samo „$x \ge 2^{r+1}$” daje krive odgovore (npr. $x = 10$ gore).</li>
<li>Posebni element koji zadovoljava (a) ali ne (b) ne smije se računati kao neposebni kandidat — zato ih oduzimamo od zbroja.</li>
<li>$O = 0$ (svi elementi $0$): ispisati $0\ 0$; poteza nema jer $2^i \le 0$ nije moguće.</li>
</ul>
''',
    'verified': r'''uzorak 1/1; 300 slučajnih testova ($N \le 4$, vrijednosti do $31$) protiv brute forcea koji BFS-om po stanjima niza iscrpno traži najveći ILI i najmanji broj poteza; 3 velika testa ($N = Q = 10^5$ slučajnih vrijednosti, potencije dvojke, te $T = 10^5$ sićušnih testova).''',
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
    'solution': r'''
<p>Dijeljenje većim brojem nikad nije gore, pa kao pripremni korak stavimo $cost_i = \min(cost_i, cost_{i+1}, \dots, cost_M)$.</p>
<p>Ako se medijan može učiniti $\le x$, onda se naravno može učiniti i $\le x+1$. Zato binarnim pretraživanjem tražimo najmanji valjani $x$. Za fiksni $x$ želimo izračunati najmanju cijenu da medijan bude $\le x$.</p>
<p>Neka je $A_1 \le A_2 \le \dots \le A_N$ i $N = 2k+1$. Optimalno je pokušati $A_1, A_2, \dots, A_{k+1}$ sve učiniti $\le x$. Da bi $A_i$ pao na $\le x$, treba ga ukupno podijeliti s barem $\left\lceil \frac{A_i + 1}{x + 1} \right\rceil$.</p>
<p>Za sve pozitivne cijele brojeve $x, y, z$ cjelobrojno dijeljenje ima svojstvo $\left\lfloor \frac{\lfloor x/y \rfloor}{z} \right\rfloor = \left\lfloor \frac{x}{yz} \right\rfloor$, što znači da niz cjelobrojnih dijeljenja možemo promatrati kao jedno dijeljenje, sa zbrojenim cijenama.</p>
<p>Izračunajmo $f(y)$, najmanju cijenu dijeljenja točno s $y$. Inicijaliziramo $f(y) = cost_y$, a zatim za svaki djelitelj $d$ od $y$ relaksiramo s $cost_d + f(y/d)$. Dinamičkim programiranjem u stilu sita to traje ukupno $O(M \log M)$.</p>
<p>Potreban je oprez s vrijednostima blizu $M$, jer može biti optimalno dijeliti s vrijednošću većom od $M$. No zanima nas samo prvi višekratnik svakog cijelog broja koji premašuje $M$, pa možemo npr. računati $f(y)$ do $2M$ (nedostajuće cijene tretiramo kao $\infty$). Konačno, kako dijeljenje većim brojevima nije gore, $f(y)$ postavimo na sufiksni minimum $\min(f(y), f(y+1), \dots, f(M))$.</p>
<p>Kad su sve vrijednosti $f(y)$ poznate, cijena da medijan bude $\le x$ računa se lako u $O(N)$: jednostavno zbrojimo $f\!\left(\left\lceil \frac{A_i+1}{x+1} \right\rceil\right)$ po svim relevantnim $A_i$.</p>
''',
    'coach': [
        (r'Kako pretvoriti „minimiziraj medijan” u pitanje na koje se lako odgovara?',
         r'''<p>Medijan niza duljine $N = 2k+1$ je $\le x$ ako i samo ako je barem $k+1$ elemenata $\le x$. Svojstvo „medijan se može spustiti na $\le x$ uz cijenu $\le K$” je monotono u $x$ (što smijemo za $x$, smijemo i za $x+1$), pa binarno pretražujemo najmanji takav $x$. Preostaje: za fiksni $x$ izračunati <em>najmanju cijenu</em> da barem $k+1$ elemenata bude $\le x$.</p>'''),
        (r'Koliko košta spustiti jedan element $A_i$ na $\le x$, i koje elemente spuštati?',
         r'''<p>Niz dijeljenja $\lfloor\lfloor A/a\rfloor/b\rfloor = \lfloor A/(ab)\rfloor$ ponaša se kao jedno dijeljenje umnoškom; $\lfloor A_i / y \rfloor \le x \iff y \ge \lfloor A_i/(x+1) \rfloor + 1 =: y_i$. Dakle cijena za $A_i$ je $F(y_i)$, gdje je $F(y)$ najmanja cijena da umnožak djelitelja bude <em>barem</em> $y$. $F$ je neopadajuća, a $y_i$ raste s $A_i$, pa su najjeftiniji upravo $k+1$ najmanjih elemenata — njih spuštamo, sve ostale ne diramo.</p>'''),
        (r'Kako izračunati $F(y)$ za sve $y$ odjednom?',
         r'''<p>Prvo $cost_d \leftarrow \min(cost_d, \dots, cost_M)$: dijeljenje većim brojem nikad nije gore, pa „dijeljenje s $d$” smijemo tumačiti kao „dijeljenje s nekim $d' \ge d$ po najjeftinijoj cijeni”. Zatim $f(y)$ = najmanja cijena za umnožak <em>točno</em> $y$: $f(1) = 0$, i za svaki $y$ s konačnim $f(y)$ relaksiramo $f(yd) \leftarrow f(y) + cost_d$ za $d = 2, \dots, M$. To je sito: ukupno $\sum_y L/y = O(L \log L)$ koraka. Na kraju $F(y) = \min_{y' \ge y} f(y')$ sufiksnim minimumom.</p>'''),
        (r'Do kojeg umnoška treba računati $f$ i zašto ne samo do $M$?',
         r'''<p>Potrebni $y_i \le A_i + 1 \le M + 1$, ali optimalni umnožak može biti veći od $M$ (npr. $M = 5$, $y = 5$, jeftin samo djelitelj $3$: $3 \cdot 3 = 9$). Uzmimo optimalni multiskup djelitelja $d_1 \le \dots \le d_t$ umnoška $P \ge y$. Umnožak bez najvećeg, $P' = P/d_t$, je $\lt y$ (inače bismo izbacili $d_t$ i uštedjeli). Zamijenimo $d_t$ s $e = \lceil y/P' \rceil \le d_t$: nakon sufiksnog minimuma $cost_e \le cost_{d_t}$, pa cijena ne raste, a $P' e \lt y + P' \le 2M + 1$. Dakle uvijek postoji optimalni umnožak $\le 2M+1$ i dovoljno je računati $f$ do $L = 2M+2$.</p>'''),
    ],
    'tips': [
        r'''„Minimiziraj $k$-tu statistiku (medijan, maksimum…) uz budžet” gotovo uvijek znači binarno pretraživanje po odgovoru i podzadatak „najmanja cijena da barem $k$ elemenata zadovolji prag”.''',
        r'''Cjelobrojna dijeljenja se slažu: $\lfloor\lfloor A/a\rfloor/b\rfloor = \lfloor A/(ab)\rfloor$. Niz operacija „podijeli” postaje jedna operacija s umnoškom, pa se cijene mogu računati DP-om po umnošku (sitom).''',
        r'''Kad je operacija monotona (dijeljenje većim brojem nije gore), zamijeni cjenik sufiksnim/prefiksnim minimumom — to legalizira „zaokruživanje” djelitelja u dokazima i pojednostavljuje DP.''',
        r'''Za granicu „do kojeg umnoška računati” koristi zamjenski argument: iz optimalnog rješenja izbaci/smanji zadnji korak i ocijeni koliko umnožak može prijeći cilj.''',
    ],
    'detailed': r'''
<h3>1. Binarno pretraživanje po odgovoru</h3>
<p>Neka je $N = 2k + 1$ i neka je $A$ sortiran: $A_1 \le \dots \le A_N$. Medijan je $A_{k+1}$, pa je medijan $\le x$ ako i samo ako barem $k+1$ elemenata ima vrijednost $\le x$. Definirajmo $C(x)$ = najmanja ukupna cijena poteza nakon kojih je barem $k+1$ elemenata $\le x$. Ako je $C(x) \le K$, onda je i $C(x+1) \le K$ (isti potezi rade), pa je skup dopuštenih $x$ oblika $[x^*, \infty)$ i tražimo $x^*$ binarnim pretraživanjem na $[0, A_{k+1}]$ — gornja granica je uvijek dopuštena bez poteza. Vrijednost $0$ je legitimna (dijeljenje brojem većim od elementa daje $0$).</p>
<h3>2. Cijena spuštanja jednog elementa</h3>
<p>Za pozitivne cijele $A, a, b$ vrijedi $\lfloor \lfloor A/a \rfloor / b \rfloor = \lfloor A/(ab) \rfloor$. (Dokaz: napišimo $A = qab + r$, $0 \le r \lt ab$; tada je $\lfloor A/a \rfloor = qb + \lfloor r/a \rfloor$ s $\lfloor r/a\rfloor \lt b$, pa je $\lfloor \lfloor A/a\rfloor / b \rfloor = q$.) Indukcijom, niz dijeljenja s $d_1, \dots, d_t$ daje $\lfloor A / (d_1 \cdots d_t) \rfloor$, a ukupna cijena je $\sum cost_{d_j}$. Redoslijed nije važan.</p>
<p>Uvjet $\lfloor A_i / y \rfloor \le x$ ekvivalentan je s $A_i / y \lt x + 1$, tj. $y \gt A_i/(x+1)$, tj. $y \ge y_i := \lfloor A_i/(x+1) \rfloor + 1$. Dakle za $A_i$ trebamo umnožak djelitelja barem $y_i$, a najmanja cijena za to je</p>
<p style="text-align:center">$F(y) = \min\{\, \textstyle\sum_j cost_{d_j} : d_j \in [1, M],\ \prod_j d_j \ge y \,\}.$</p>
<p>$F$ je neopadajuća funkcija od $y$ (veći cilj — manje dopuštenih multiskupova), a $y_i$ je neopadajuća u $A_i$. Stoga je cijena spuštanja neopadajuća u $A_i$ i optimalno je spustiti točno $k+1$ <em>najmanjih</em> elemenata: $C(x) = \sum_{i=1}^{k+1} F(y_i)$. Elementi koji su već $\le x$ imaju $y_i = 1$ i $F(1) = 0$.</p>
<h3>3. Sufiksni minimum cjenika</h3>
<p>Dijeljenje većim brojem nikad nije gore za naš cilj (rezultat je manji ili jednak). Zato definiramo $cost'_d = \min_{e \ge d} cost_e$. Multiskup djelitelja s cijenama $cost'$ odgovara multiskupu s originalnim cijenama u kojem je svaki $d$ zamijenjen nekim $e \ge d$ (onim koji postiže minimum) — umnožak je veći ili jednak, cijena ista. Obratno, svaki originalni multiskup ima s $cost'$ cijenu $\le$ originalnoj. Dakle $F$ se ne mijenja ako računamo s $cost'$, a $cost'$ ima korisno svojstvo: <strong>neopadajuća je u $d$</strong> (manji djelitelji su jeftiniji ili jednaki).</p>
<h3>4. Gornja granica umnoška</h3>
<p>Potrebni $y_i \le A_i + 1 \le M + 1$. Tvrdimo: za svaki $y \le M+1$ postoji optimalni multiskup (za $cost'$) s umnoškom $P \le 2M + 1$. Neka je $d_1 \le \dots \le d_t$ optimalan s $P \ge y$, $t \ge 2$ (za $t \le 1$ je $P \le M$). Neka je $P' = P / d_t$. Vrijedi $P' \lt y$: inače bismo izbacili $d_t$, umnožak bi i dalje bio $\ge y$, a cijena strogo manja ($cost \ge 1$), suprotno optimalnosti. Zamijenimo $d_t$ s $e = \lceil y / P' \rceil$. Kako $P' d_t \ge y$, vrijedi $e \le d_t$, pa je $cost'_e \le cost'_{d_t}$ — cijena ne raste, novi multiskup je i dalje optimalan. Umnožak je $P' e \lt P'(y/P' + 1) = y + P' \lt 2y \le 2M + 2$. Dakle dovoljno je poznavati $f$ na $[1, L]$ s $L = 2M + 2$ i uzeti $F(y) = \min_{y \le y' \le L} f(y')$.</p>
<h3>5. Sito za $f$</h3>
<p>$f(y)$ = najmanja cijena za umnožak <em>točno</em> $y$: $f(1) = 0$, $f(y) = \infty$ inače na početku. Prolazimo $y = 2, \dots, L$ rastuće; kad dođemo do $y$, $f(y)$ je konačan (sve njegove faktorizacije završavaju relaksacijom iz manjeg umnoška), i za $d = 2, \dots, M$ s $yd \le L$ relaksiramo $f(yd) \leftarrow \min(f(yd), f(y) + cost'_d)$. Broj koraka je $\sum_{y \le L} \lfloor L/y \rfloor = O(L \log L) = O(M \log M)$. Ispravnost: svaki multiskup $d_1 \cdots d_t = y$ odgovara lancu $1 \to d_1 \to d_1 d_2 \to \dots \to y$ kroz relaksacije, i obrnuto. Zatim $F(y) = \min(f(y), F(y+1))$ za $y = L, \dots, 1$.</p>
<h3>6. Cijeli algoritam i složenost</h3>
<ol>
<li>$cost' \leftarrow$ sufiksni minimum, $O(M)$.</li>
<li>Sito za $f$ do $L = 2M+2$, sufiksni minimum $F$: $O(M \log M)$.</li>
<li>Sortiraj $A$: $O(N \log N)$.</li>
<li>Binarno pretraživanje $x \in [0, A_{k+1}]$; provjera $\sum_{i \le k+1} F(\lfloor A_i/(x+1)\rfloor + 1) \le K$ u $O(N)$ (prekid čim zbroj prijeđe $K$). Ukupno $O(N \log M)$.</li>
</ol>
<p>Uz $\sum N, \sum M \le 10^6$ sve prolazi u vremenu. Memorija $O(N + M)$.</p>
<h3>7. Primjer</h3>
<p>$A = (2, 5, 2)$, $cost = (3, 2, 4, 6, 13)$, $M = 5$. $cost' = (2, 2, 4, 6, 13)$; $f(2) = 2$, $f(3) = 4$, $f(4) = \min(6, f(2) + cost'_2) = 4$, $f(5) = 13$, $f(6) = f(3) + 2 = 6$, … Sortirano $A = (2, 2, 5)$, $k = 1$, spuštamo dva najmanja. $K = 6$: $x = 1$ traži $y = \lfloor 2/2 \rfloor + 1 = 2$ za oba, cijena $2 + 2 = 4 \le 6$; $x = 0$ traži $y = 3$, $F(3) = 4$, cijena $8 \gt 6$. Odgovor $1$ (drugačijim potezima nego u primjeru, ali s istim medijanom). $K = 3$: $x = 1$ košta $4 \gt 3$, pa medijan ostaje $2$.</p>
<h3>8. Zamke</h3>
<ul>
<li>Zbroj cijena može biti do $10^6 \cdot 10^9$, koristi 64-bitne tipove; $\infty$ birati tako da $\infty + cost$ ne prelije (ili preskakati beskonačne $f(y)$, kao u kodu).</li>
<li>Ne zaboraviti $f(1) = 0$ — elementi koji su već $\le x$ ne koštaju ništa.</li>
<li>Računati $f$ samo do $M$ je pogrešno (vidi odjeljak 4); do $2M+2$ je dovoljno.</li>
<li>Binarno pretraživanje mora dopustiti $x = 0$; formula $\lfloor A_i/(x+1) \rfloor$ tada dijeli s $1$ i ne dijeli nulom.</li>
</ul>
''',
    'verified': r'''uzorak 1/1; 300 slučajnih testova ($N \le 7$, $M \le 8$) protiv brute forcea koji za svaki element Dijkstrom po vrijednostima $0..A_i$ računa najjeftinije spuštanje na svaki prag i zatim ispituje sve pragove; 3 velika testa ($N = 999\,999$, $M = 10^6$, $K \in \{0, 10^6, 10^9\}$).''',
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
    'solution': r'''
<p>Odluku o prisustvovanju svakom ispitu modeliramo zasebnom logičkom varijablom.</p>
<p>Za svaki uvjet $A, B$ mora vrijediti logički izraz $A \lor B$. Za svaki par ispita $X, Y$ koji se preklapaju mora vrijediti $X' \lor Y'$ (negacije). Svi ti izrazi moraju biti istiniti da bismo diplomirali s valjanim rasporedom prisustvovanja. Ukupni izraz koji treba zadovoljiti je oblika $(A_1 \lor B_1) \land (A_2 \lor B_2) \land \dots \land (X_1' \lor Y_1') \land (X_2' \lor Y_2') \land \dots$, što je logički izraz u konjunktivnoj normalnoj formi s dva literala po klauzuli (2-CNF).</p>
<p>Provjera zadovoljivosti 2-CNF izraza dobro je poznat problem, poznat kao 2-zadovoljivost (<a href="https://en.wikipedia.org/wiki/2-satisfiability">2-SAT</a>). Rješava se modeliranjem izraza kao grafa, s implikacijskim bridovima za svaki „ili” uvjet.</p>
<p>Budući da preklapajućih raspona može biti $O(N^2)$, u našem izrazu može biti $O(N^2)$ „ili” uvjeta. Da smanjimo broj implikacijskih bridova u 2-SAT grafu, možemo stvoriti pomoćne vrhove nalik segmentnom stablu, odgovorne za „segment” — kontinuirani raspon ispita sortiranih po vremenu početka ili završetka.</p>
<p>Sada za svaki ispit, umjesto izravnih implikacijskih bridova prema svim ispitima koji se s njim preklapaju, dodajemo bridove prema $O(\log N)$ pomoćnih vrhova segmentnog stabla koji su odgovorni za raspone ispita koji počinju ili završavaju unutar raspona ovog ispita. To smanjuje broj bridova grafa na $O(N \log N)$, a ukupna vremenska složenost je također $O(N \log N)$.</p>
''',
    'coach': [
        (r'Kako zapisati sve što se traži kao logičke uvjete na odluke „idem / ne idem na ispit $i$”?',
         r'''<p>Uvedimo $x_i$ = „prisustvujem ispitu $i$”. Uvjet za diplomu $(A, B)$ kaže $x_A \lor x_B$. Ograničenje rasporeda kaže da za svaki par ispita $X, Y$ koji se preklapaju vrijedi $\lnot x_X \lor \lnot x_Y$. Svaki uvjet je disjunkcija <em>dva</em> literala, a svi moraju vrijediti odjednom: to je 2-CNF, dakle 2-SAT, rješiv u linearnom vremenu preko implikacijskog grafa i jako povezanih komponenti.</p>'''),
        (r'Zašto izravni 2-SAT ne prolazi i što točno treba smanjiti?',
         r'''<p>Preklapajućih parova može biti $\Theta(N^2)$ (svi ispiti u istom trenutku), a svaki daje dvije implikacije: $10^{10}$ bridova. Klauzule s uvjetima su samo $M$; problem su isključivo klauzule preklapanja, i one imaju strukturu: sortiramo li ispite po početku, ispit $i$ preklapa se točno s ispitima čiji početak leži u $[S_i, E_i]$ — to je <em>kontinuirani raspon</em> pozicija u sortiranom redoslijedu (bez $i$ samog). Svaki preklapajući par uočava barem jedan od svoja dva ispita (onaj s ranijim početkom).</p>'''),
        (r'Kako izraziti „$x_i \Rightarrow$ nitko iz raspona pozicija $[l, r]$ ne ide” s $O(\log N)$ klauzula?',
         r'''<p>Pomoćnim varijablama nalik segmentnom stablu. Za svaki čvor $v$ stabla nad sortiranim ispitima uvedemo $U_v$ = „nitko iz raspona čvora $v$ ne prisustvuje”, s klauzulama $U_v \Rightarrow U_{\text{lijevo}}$, $U_v \Rightarrow U_{\text{desno}}$ i za list $U_{\text{list}(j)} \Rightarrow \lnot x_j$. Tada „$x_i \Rightarrow$ nitko iz $[l, r]$” zapišemo kao $x_i \Rightarrow U_v$ za $O(\log N)$ kanonskih čvorova koji pokrivaju $[l, r]$; implikacije se lančano spuštaju do listova. Ukupno $O(N \log N)$ klauzula.</p>'''),
        (r'Zašto je proširena formula zadovoljiva točno kad je izvorna?',
         r'''<p>Ako izvorna ima rješenje, postavimo $U_v$ istinitim točno kad nitko iz raspona $v$ ne ide: sve pomoćne klauzule vrijede (podskup od „nitko” je „nitko”; ako $x_i$ vrijedi, svi iz njegova raspona se s njim preklapaju pa ne idu). Obratno, iz rješenja proširene formule slijede sve izvorne klauzule preklapanja: za preklapajući par $(i, j)$ u kojem $i$ vidi $j$, $x_i \Rightarrow U_v \Rightarrow \dots \Rightarrow U_{\text{list}(j)} \Rightarrow \lnot x_j$. Pomoćne varijable ne dodaju nova ograničenja na $x$.</p>'''),
    ],
    'tips': [
        r'''Kad su svi uvjeti oblika „barem jedno od dvoje” ili „ne oboje” — to je 2-SAT. Prepoznaj ga i onda razmišljaj samo o broju klauzula.''',
        r'''Klauzula od jedne varijable prema <em>rasponu</em> varijabli (u nekom sortiranom poretku) standardno se komprimira pomoćnim varijablama segmentnog stabla: $O(\log N)$ implikacija umjesto $O(N)$. Isti trik radi za bridove grafa općenito („segment tree graph”).''',
        r'''Pri uvođenju pomoćnih varijabli uvijek napiši oba smjera dokaza ekvizadovoljivosti — lako je slučajno dodati implikaciju koja izvorno rješenje čini nevaljanim.''',
        r'''Za $N$ do $10^5$ i rekurzivni Tarjan/Kosaraju pazi na dubinu rekurzije (graf ima do $\approx 4N$ vrhova u lancu); iterativna implementacija ili povećani stog.''',
    ],
    'detailed': r'''
<h3>1. Model kao 2-SAT</h3>
<p>Za svaki ispit $i$ uvedimo logičku varijablu $x_i$ („prisustvujem ispitu $i$”). Zahtjevi:</p>
<ul>
<li>za svaki uvjet $(A, B)$: $x_A \lor x_B$;</li>
<li>za svaki par ispita $X \ne Y$ koji se preklapaju ($\max(S_X, S_Y) \le \min(E_X, E_Y)$, intervali su zatvoreni): $\lnot x_X \lor \lnot x_Y$.</li>
</ul>
<p>Diplomirati se može ako i samo ako postoji vrijednost svih $x_i$ koja zadovoljava sve klauzule. Sve su klauzule disjunkcije dvaju literala, pa je to instanca 2-SAT-a.</p>
<p><em>Podsjetnik na 2-SAT.</em> Klauzula $a \lor b$ ekvivalentna je implikacijama $\lnot a \Rightarrow b$ i $\lnot b \Rightarrow a$. Izgradimo usmjereni graf na $2n$ literala s tim bridovima. Formula je zadovoljiva ako i samo ako nijedna varijabla $x$ nije u istoj jako povezanoj komponenti (SCC) kao $\lnot x$ (jer bi tada $x \Rightarrow \lnot x \Rightarrow x$). Uz Tarjanov algoritam sve je $O(V + E)$.</p>
<h3>2. Problem: previše klauzula preklapanja</h3>
<p>Uvjeta je $M \le 10^5$, ali preklapajućih parova može biti $\binom N2 \approx 5 \cdot 10^9$. Treba iskoristiti strukturu preklapanja. Sortirajmo ispite po početku $S$ i označimo poziciju ispita $i$ u tom redoslijedu s $p_i$. Za ispit $i$ neka je $[lo_i, hi_i]$ raspon pozicija ispita čiji početak leži u $[S_i, E_i]$ (nalazimo ga binarnim pretraživanjem: $lo_i$ = prva pozicija s $S \ge S_i$, $hi_i$ = posljednja s $S \le E_i$). Tada:</p>
<p><strong>Lema.</strong> Ispiti $i \ne j$ se preklapaju ako i samo ako je $p_j \in [lo_i, hi_i]$ ili $p_i \in [lo_j, hi_j]$.<br>
<em>Dokaz.</em> Ako se preklapaju i $S_i \le S_j$, onda $S_j \le \min(E_i, E_j) \le E_i$, pa je $S_j \in [S_i, E_i]$ i $p_j \in [lo_i, hi_i]$; simetrično za $S_j \le S_i$. Obratno, ako je $S_i \le S_j \le E_i$, presjek sadrži točku $S_j$ ($S_j \le E_j$ uvijek). $\square$</p>
<p>Dakle sve klauzule preklapanja dobivamo ako za svaki $i$ zahtijevamo: $x_i \Rightarrow \lnot x_j$ za sve $j$ na pozicijama $[lo_i, hi_i] \setminus \{p_i\}$. To je još uvijek potencijalno $O(N^2)$ implikacija, ali sad svaka ide od jedne varijable prema <em>kontinuiranom rasponu</em> pozicija.</p>
<h3>3. Kompresija segmentnim stablom</h3>
<p>Nad pozicijama $0, \dots, n-1$ izgradimo (implicitno) segmentno stablo veličine $sz = 2^{\lceil \log_2 n \rceil}$; čvor $v$ pokriva raspon pozicija $R(v)$, listovi su pojedini ispiti. Za svaki čvor uvedemo novu logičku varijablu $U_v$ sa značenjem „nitko iz $R(v)$ ne prisustvuje” i dodamo klauzule:</p>
<ul>
<li>$U_v \Rightarrow U_{2v}$ i $U_v \Rightarrow U_{2v+1}$ za unutarnje čvorove (klauzule $\lnot U_v \lor U_{2v}$ itd.),</li>
<li>$U_{\text{list}(k)} \Rightarrow \lnot x_{j}$ gdje je $j$ ispit na poziciji $k$,</li>
<li>za svaki ispit $i$ i svaki od $O(\log N)$ kanonskih čvorova $v$ koji rastavljaju $[lo_i, p_i - 1]$ i $[p_i + 1, hi_i]$: $x_i \Rightarrow U_v$.</li>
</ul>
<p>Broj klauzula: $2(sz - 1) + n + O(n \log n) + m$, dakle $O((N + M)\log N)$ bridova i $O(N)$ vrhova ($n + 2sz \lt 5n$ varijabli, dvostruko literala).</p>
<h3>4. Dokaz ekvizadovoljivosti</h3>
<p><em>Izvorna $\Rightarrow$ proširena.</em> Uzmimo rješenje izvorne formule i definirajmo $U_v$ = istina ako i samo ako $x_j$ = laž za sve $j$ s pozicijom u $R(v)$. Klauzule $U_v \Rightarrow U_{\text{dijete}}$ vrijede jer je $R(\text{dijete}) \subseteq R(v)$; $U_{\text{list}(k)} \Rightarrow \lnot x_j$ vrijedi po definiciji. Za $x_i \Rightarrow U_v$: ako je $x_i$ istina, svaki $j$ iz $R(v) \subseteq [lo_i, hi_i] \setminus \{p_i\}$ preklapa se s $i$ (Lema), pa po izvornoj klauzuli $x_j$ = laž; dakle $U_v$ = istina.</p>
<p><em>Proširena $\Rightarrow$ izvorna.</em> Uzmimo rješenje proširene formule i ograničimo ga na $x$. Klauzule uvjeta su iste. Za preklapajući par $(i, j)$ po Lemi bez smanjenja općenitosti $p_j \in [lo_i, hi_i]$, $j \ne i$; pozicija $p_j$ leži u nekom kanonskom čvoru $v$ raspona $[lo_i, p_i-1]$ ili $[p_i+1, hi_i]$, pa imamo lanac $x_i \Rightarrow U_v \Rightarrow U_{\text{dijete}} \Rightarrow \dots \Rightarrow U_{\text{list}(p_j)} \Rightarrow \lnot x_j$. Dakle $\lnot x_i \lor \lnot x_j$ vrijedi. $\square$</p>
<p>Zato je odgovor <code>YES</code> ako i samo ako je proširena 2-SAT formula zadovoljiva.</p>
<h3>5. Algoritam</h3>
<ol>
<li>Sortiraj ispite po $S$; izračunaj $p_i$, $lo_i$, $hi_i$ binarnim pretraživanjem po sortiranim početcima.</li>
<li>Stvori $n + 2sz$ varijabli, dodaj klauzule stabla (roditelj $\Rightarrow$ djeca, list $\Rightarrow \lnot x$).</li>
<li>Za svaki $i$ rastavi $[lo_i, p_i-1]$ i $[p_i+1, hi_i]$ na kanonske čvorove (standardna iterativna petlja po segmentnom stablu odozdo) i dodaj $x_i \Rightarrow U_v$.</li>
<li>Za svaki uvjet dodaj $x_A \lor x_B$.</li>
<li>Tarjanov SCC na grafu literala; <code>NO</code> ako je neka varijabla u istoj komponenti sa svojom negacijom, inače <code>YES</code>.</li>
</ol>
<p>Složenost $O((N + M) \log N)$ po testu, ukupno unutar $3$ s uz $\sum N, \sum M \le 10^5$.</p>
<h3>6. Primjer</h3>
<p>Drugi primjer: $[1,5], [2,7], [5,7]$ i uvjeti $(1,2), (2,3), (3,1)$. Sva tri para se preklapaju ($[1,5]$ i $[5,7]$ dijele točku $5$ — zatvoreni intervali!). Uvjeti traže barem dva položena ispita od tri, a preklapanje dopušta najviše jedan: implikacijski graf sadrži ciklus kroz $x_1$ i $\lnot x_1$, odgovor <code>NO</code>. Prvi primjer: $[10, 11]$ se ni s kim ne preklapa; uvjet $(2, 1)$ zadovoljava $x_1$ = istina, $x_2$ = laž — <code>YES</code>.</p>
<h3>7. Zamke</h3>
<ul>
<li>Intervali su zatvoreni: $E_X = S_Y$ je preklapanje; koristi <code>upper_bound(E_i)</code> pri određivanju $hi_i$. Ispiti s jednakim početkom vide jedan drugoga u oba smjera (raspon $[lo_i, p_i - 1]$ ih uključuje).</li>
<li>Isključi sam ispit iz raspona ($p_i$), inače dobivaš $x_i \Rightarrow \lnot x_i$ i sve postaje <code>NO</code>.</li>
<li>Više ispita može imati isti početak: $lo_i$ je prva pozicija s $S \ge S_i$ (može biti $\lt p_i$), ne sama pozicija $p_i$.</li>
<li>Graf ima do $\approx 10 N$ literala i duge lance $U$-implikacija — rekurzivni DFS može probiti stog; koristi iterativni Tarjan.</li>
<li>$M = 0$ je dopušteno: odgovor je tada uvijek <code>YES</code> (ne idemo ni na jedan ispit).</li>
</ul>
''',
    'verified': r'''uzorak 1/1; 300 slučajnih testova ($N \le 9$, male koordinate radi mnogo preklapanja) protiv brute forcea koji ispituje sve podskupove ispita, plus dodatnih 1000 slučajnih testova; 3 velika testa ($N = M = 10^5$, koordinate do $10^9$, $10^5$ i $10^3$).''',
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
    'solution': r'''
<p>Može se dokazati da takav podskup uvijek postoji. Budući da su zadaci na stablima obično lakši od zadataka na grafovima, pretvorimo ovo u zadatak na stablu.</p>
<p>Uzmimo bilo koje razapinjuće stablo grafa. Ako nađemo valjani podskup za to stablo, isti će podskup biti valjan i za izvorni graf, jer je $\mathrm{dist}_G(u, v) \le \mathrm{dist}_T(u, v)$ za sve $u, v$.</p>
<p>Ukorijenimo razapinjuće stablo u proizvoljnom vrhu. Neka je $v$ najdublji list stabla. Neka je $\mathrm{anc}(v)$ predak od $v$ koji je $\lceil \sqrt N \rceil$ razina iznad $v$; ako je dubina od $v$ manja od $\lceil \sqrt N \rceil$, neka je $\mathrm{anc}(v)$ korijen.</p>
<p>Uočimo da za svaki vrh $u$ u podstablu od $\mathrm{anc}(v)$ vrijedi $\mathrm{dist}(u, \mathrm{anc}(v)) \le \lceil \sqrt N \rceil$. Zato dodamo $\mathrm{anc}(v)$ u $S$ i uklonimo podstablo ukorijenjeno u $\mathrm{anc}(v)$. Sada treba riješiti isti zadatak za manje stablo; rekurziramo dok ne dodamo korijen u $S$.</p>
<p>U svakoj iteraciji dodajemo točno jedan vrh u $S$, pa je $|S|$ jednak broju iteracija. U svakoj iteraciji uklanjamo iz stabla barem $\lceil \sqrt N \rceil$ vrhova. Kako vrhova ima samo $N$, iteracija može biti najviše $\lceil \sqrt N \rceil$. Stoga je $|S| \le \lceil \sqrt N \rceil$, pa je $S$ valjan podskup.</p>
<p>Naivno izvođenje gornjeg algoritma daje složenost $O(N \sqrt N)$, ali može se optimizirati ako predračunamo dubine svih vrhova i stavimo ih u skup. Budući da trebamo i DSU za razapinjuće stablo, konačna vremenska složenost je $O(N \log N + (N + M) \cdot \alpha(N))$, a prostorna $O(N)$. Postoji i alternativno rješenje složenosti $O((N + M) \cdot \alpha(N))$ s jednim DFS-om nakon dobivanja razapinjućeg stabla.</p>
''',
    'coach': [
        (r'Zašto smijemo zaboraviti većinu bridova i raditi na razapinjućem stablu?',
         r'''<p>Za razapinjuće stablo $T$ grafa $G$ svaki put u $T$ je i put u $G$, pa je $\mathrm{dist}_G(u,v) \le \mathrm{dist}_T(u,v)$. Ako nađemo $S$ koji u stablu pokriva svaki vrh unutar udaljenosti $s = \lceil\sqrt N\rceil$, isti $S$ pokriva i graf. Stabla su ugodnija: imaju korijen, dubinu, podstabla — sve što treba za pohlepni argument. Stablo dobivamo jednim BFS-om.</p>'''),
        (r'Koji je vrh „najhitnije” pokriti i tko ga najbolje pokriva?',
         r'''<p>Najdublji nepokriveni list $v$. Njegov pokrivač mora biti na udaljenosti $\le s$; najkorisniji izbor je predak $a$ točno $s$ razina iznad $v$ (ili korijen ako je $v$ pliće), jer je „najviši” dopušteni vrh pa pokriva najveće podstablo. Ključno: <em>svaki</em> vrh $u$ u podstablu od $a$ udaljen je od $a$ za najviše $s$ — dubina od $u$ ne prelazi dubinu od $v$ (v je najdublji), a $\mathrm{depth}(v) - \mathrm{depth}(a) = s$. Dakle dodavanjem $a$ u $S$ cijelo podstablo od $a$ je pokriveno i smijemo ga odrezati.</p>'''),
        (r'Zašto se to ne dogodi više od $\lceil\sqrt N\rceil$ puta?',
         r'''<p>Svaki put kad dodamo vrh $a \ne$ korijen, odrežemo njegovo podstablo koje sadrži cijeli put $v \to a$, dakle barem $s + 1$ vrhova koji do tada nisu bili odrezani. Odrezani skupovi su disjunktni, pa je takvih koraka najviše $\lfloor N/(s+1) \rfloor$. Na kraju eventualno dodamo korijen. Kako je $N \le s^2$, vrijedi $\lfloor N/(s+1)\rfloor + 1 \le \lfloor s^2/(s+1)\rfloor + 1 \le (s - 1) + 1 = s$. Odgovor $-1$ dakle nikad ne treba.</p>'''),
        (r'Kako to izvesti u linearnom vremenu bez stalnog traženja najdubljeg lista?',
         r'''<p>Obradimo vrhove od najdubljih prema korijenu (obrnuti BFS redoslijed) i za svaki vrh $x$ računamo $h(x)$ = udaljenost do najdaljeg <em>još nepokrivenog</em> vrha u njegovu podstablu ($h = 0$ ako je jedini takav sam $x$, $-1$ ako ga nema). Kad $h(x)$ dosegne $s$, stavimo $x$ u $S$ i označimo podstablo odrezanim ($h(x) \leftarrow -1$). Roditelj dobiva $h(p) = \max(h(p), h(x) + 1)$. To je isti pohlepni postupak: vrh $x$ postaje centar točno kad je predak na udaljenosti $s$ najdubljeg nepokrivenog lista. Na kraju, ako je $h(\text{korijen}) \ge 0$, dodamo korijen.</p>'''),
    ],
    'tips': [
        r'''Kad uvjet zadatka govori o udaljenostima u grafu i traži se <em>pokrivanje</em>, često smiješ prijeći na razapinjuće stablo — udaljenosti u stablu su gornje ograde za udaljenosti u grafu, a stablo ima strukturu (dubina, podstabla) koja omogućuje pohlepu i indukciju.''',
        r'''Granica oblika $\sqrt N$ gotovo uvijek dolazi iz argumenta „svaki korak troši barem $\sqrt N$ objekata, a objekata je $N$” — kad je vidiš, traži što se u svakom koraku nepovratno troši.''',
        r'''Pohlepni postupak „uzmi najdublji list i njegova pretka na fiksnoj udaljenosti” standardno se implementira jednim prolazom odozdo prema gore koji za svaki vrh pamti udaljenost do najdaljeg nepokrivenog vrha u podstablu.''',
        r'''Za konstruktivne zadatke bez jedinstvenog odgovora piši checker koji izravno provjerava svojstvo (ovdje BFS iz svih centara), umjesto uspoređivanja s jednim „ispravnim” ispisom.''',
    ],
    'detailed': r'''
<h3>1. Preformulacija</h3>
<p>Neka je $s = \lceil\sqrt N\rceil$. Tražimo skup $S$ s $|S| \le s$ takav da je svaki vrh na udaljenosti $\le s$ od nekog vrha iz $S$. Zadatak dopušta odgovor $-1$, ali pokazat ćemo da takav skup <em>uvijek</em> postoji, pa se $-1$ nikad ne ispisuje.</p>
<h3>2. Prelazak na razapinjuće stablo</h3>
<p>Neka je $T$ bilo koje razapinjuće stablo povezanog grafa $G$ (npr. BFS stablo iz vrha $1$). Svaki put u $T$ koristi samo bridove iz $G$, pa je $\mathrm{dist}_G(u,v) \le \mathrm{dist}_T(u,v)$ za sve $u, v$. Ako je $S$ valjan za $T$, tj. za svaki $u$ postoji $c \in S$ s $\mathrm{dist}_T(u, c) \le s$, onda je i $\mathrm{dist}_G(u,c) \le s$, pa je $S$ valjan i za $G$. Dakle dovoljno je riješiti zadatak na stablu.</p>
<h3>3. Pohlepni postupak i njegova ispravnost</h3>
<p>Ukorijenimo $T$ u vrhu $1$. Ponavljamo dok postoji nepokriven vrh:</p>
<ol>
<li>neka je $v$ nepokriveni vrh najveće dubine;</li>
<li>neka je $a$ predak od $v$ točno $s$ razina iznad $v$, odnosno korijen ako je $\mathrm{depth}(v) \lt s$;</li>
<li>dodaj $a$ u $S$ i proglasi cijelo podstablo od $a$ pokrivenim (odreži ga).</li>
</ol>
<p><strong>Lema 1 (korak je valjan).</strong> Svaki vrh $u$ u podstablu od $a$ ima $\mathrm{dist}_T(u, a) \le s$.<br>
<em>Dokaz.</em> Put od $u$ do pretka $a$ ide samo prema gore, duljine $\mathrm{depth}(u) - \mathrm{depth}(a)$. Ako je $u$ u podstablu od $a$ i nepokriven, $\mathrm{depth}(u) \le \mathrm{depth}(v)$ jer je $v$ najdublji nepokriveni vrh, pa je duljina $\le \mathrm{depth}(v) - \mathrm{depth}(a) \le s$. Ako je $u$ već pokriven, on je već unutar $s$ od nekog ranijeg centra i ništa ne treba. (U stvarnosti se u podstablu od $a$ ne nalaze ranije odrezani vrhovi, vidi Lemu 2, ali dokazu to nije potrebno.) $\square$</p>
<p><strong>Lema 2 (koraci troše disjunktne skupove).</strong> Ako je $a \ne$ korijen, podstablo od $a$ sadrži barem $s + 1$ vrhova koji nisu bili odrezani u ranijim koracima.<br>
<em>Dokaz.</em> Put $v = u_0, u_1, \dots, u_s = a$ ima $s + 1$ vrhova. Kad bi neki $u_i$ bio odrezan u ranijem koraku s centrom $c$, bio bi u podstablu od $c$, a onda bi i njegov potomak $v$ bio u podstablu od $c$, dakle odrezan — no $v$ je nepokriven. $\square$</p>
<p><strong>Teorem.</strong> $|S| \le s$.<br>
<em>Dokaz.</em> Svaki korak s centrom različitim od korijena odreže barem $s+1$ novih vrhova, a svaki vrh se odreže najviše jednom, pa je takvih koraka najviše $\lfloor N/(s+1) \rfloor$. Korijen se dodaje najviše jednom (nakon toga je sve pokriveno). Iz $N \le s^2$ slijedi $N/(s+1) \le s^2/(s+1) = s - 1 + \frac{1}{s+1} \lt s$, dakle $\lfloor N/(s+1) \rfloor \le s - 1$ i $|S| \le s$. $\square$</p>
<p>Napomena: korijen postaje centar samo kad svi preostali nepokriveni vrhovi imaju dubinu $\lt s$ (inače bi najdublji od njih imao pretka točno $s$ razina iznad sebe i on bi bio odabran), pa su svi oni unutar $s$ od korijena i taj završni korak pokriva sve.</p>
<h3>4. Implementacija u linearnom vremenu</h3>
<p>Umjesto da svaki put tražimo najdublji nepokriveni list, pohlepu izvodimo jednim prolazom od listova prema korijenu. BFS iz vrha $1$ daje roditelje i redoslijed u kojem su roditelji uvijek ispred djece; prolazimo taj redoslijed <em>unatrag</em>. Za vrh $x$ držimo $h(x)$ = udaljenost od $x$ do najdaljeg nepokrivenog vrha u njegovu podstablu, uz $h(x) = -1$ ako je podstablo potpuno pokriveno; početno $h(x) = 0$ (sam $x$ je nepokriven).</p>
<ul>
<li>Kad obradimo $x$ (sva djeca već obrađena i „gurnula” svoje vrijednosti u $h(x)$): ako je $h(x) = s$, tada je $x$ točno $s$ razina iznad najdubljeg nepokrivenog vrha svog podstabla, pa $x$ dodamo u $S$ i stavimo $h(x) = -1$.</li>
<li>Ako je $h(x) \ge 0$, ažuriramo roditelja: $h(p) = \max(h(p), h(x) + 1)$.</li>
</ul>
<p>Vrijednost $h$ nikad ne prelazi $s$: dijete ima $h \le s - 1$ (inače bi postalo centar i imalo $-1$), pa je $h(x) \le s$. Na kraju, ako je $h(1) \ge 0$, korijen dodamo u $S$ — svi preostali nepokriveni vrhovi su na udaljenosti $h(1) \le s$ od njega. Ovo je točno pohlepni postupak iz odjeljka 3 izveden „odozdo”: vrh postaje centar u trenutku kad je predak na udaljenosti $s$ nekog najdubljeg nepokrivenog vrha, a analiza $|S| \le s$ ostaje ista (svaki centar $\ne$ korijen ima u podstablu lanac od $s+1$ nepokrivenih vrhova, a ti su lanci disjunktni).</p>
<h3>5. Primjer</h3>
<p>Put $1-2-3-4$, $N = 4$, $s = 2$. BFS iz $1$: dubine $0,1,2,3$. Obrada unatrag: $h(4) = 0 \to h(3) = 1 \to h(2) = 2 = s$, pa $2 \in S$, $h(2) = -1$; korijen ostaje $h(1) = 0 \ge 0$, pa i $1 \in S$. Izlaz $\{2, 1\}$: vrh $4$ je na udaljenosti $2$ od $2$, sve ostalo bliže. (Optimalno bi bio i sam $\{2\}$ ili $\{3\}$; zadatak ne traži minimum.)</p>
<h3>6. Složenost i zamke</h3>
<p>BFS $O(N + M)$, prolaz $O(N)$, ukupno $O(N + M)$ po testu — brže od službenog $O(N \log N + (N+M)\alpha(N))$ jer stablo gradimo BFS-om, a ne DSU-om. Zamke: $s$ računati cjelobrojno ($s$ = najmanji cijeli broj s $s^2 \ge N$), ne preko <code>sqrt</code> u pomičnom zarezu; $N = 1$ daje $s = 1$ i $S = \{1\}$; graf je povezan pa BFS dohvaća sve vrhove; uz $\sum M \le 10^6$ i $T \le 2 \cdot 10^4$ ne alocirati velike strukture po testu izvan $O(N + M)$.</p>
''',
    'verified': r'''uzorak 1/1 (checker); 300 slučajnih testova ($N \le 12$, slučajno stablo plus dodatni bridovi) provjereno checkerom koji zahtijeva $|S| \le \lceil\sqrt N\rceil$, valjane različite vrhove i BFS-om iz svih centara potvrđuje da je svaki vrh na udaljenosti $\le \lceil\sqrt N\rceil$; 3 velika testa ($N = 2 \cdot 10^5$: slučajni graf s $M \approx 8 \cdot 10^5$, put i zvijezda).''',
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
    'coach': [
        (r'Kako izgleda konačni string $T$ u odnosu na pritisnute tipke?',
         r'''<p>Backspace briše samo s kraja, pa ako je neki znak dodanog stringa $S$ preživio, preživjeli su i svi znakovi ispred njega iz istog $S$. Dakle od svakog pritiska preživi <em>prefiks</em> (možda prazan) i $T = P_1 P_2 \cdots P_b$, gdje su $P_j$ neprazni prefiksi pritisnutih stringova, u redoslijedu pritisaka. Pritisci s praznim preživjelim prefiksom su „smeće” koje služi samo za poravnanje brisanja.</p>'''),
        (r'Što se mora dogoditi između pritiska koji daje $P_j$ i pritiska koji daje $P_{j+1}$?',
         r'''<p>U trenutku pritiska za $P_{j+1}$ string mora biti točno $P_1 \cdots P_j$: sve što bi stajalo iza $P_j$ ostalo bi između $P_j$ i $P_{j+1}$, a brisanje toga poslije bi prvo uništilo $P_{j+1}$. Zato se rad dijeli na neovisne blokove: pritisni $S$ (cijena $1$), pa obriši točno višak $x = |S| - |P_j|$ znakova uz eventualno dodavanje smeća. Cijena bloka je $1 + cost(x)$, gdje $cost(x)$ ovisi samo o $x$, ne o tome što je ispred.</p>'''),
        (r'Kako izračunati $cost(x)$, najmanji broj poteza da se obriše točno $x$ zadnjih znakova?',
         r'''<p>Ako je $x \ge K$, backspace odmah: $cost(x) = 1 + cost(x-K)$ (backspace se može pomaknuti ispred svih dodavanja bez promjene broja poteza). Ako je $0 \lt x \lt K$, backspace bi zagrizao u sačuvani dio ili ne bi radio ništa, pa moramo dodati neki string; važna je samo njegova duljina $L$: $cost(x) = 1 + \min_L cost(x+L)$. Slijedi $cost(x) = \lfloor x/K \rfloor + cost(x \bmod K)$, a za ostatke $r \lt K$ dobivamo najkraći put u grafu na $K$ vrhova s bridovima $r \to (r+L) \bmod K$ težine $1 + \lfloor (r+L)/K \rfloor$ do cilja $0$. Različitih duljina $L$ je $O(\sqrt{\sum|S_i|})$, pa Dijkstra ima $O(K\sqrt{\sum|S_i|})$ bridova.</p>'''),
        (r'Kako za svaki podstring $T[i..i+l)$ brzo naći najjeftiniji $S$ kojemu je on prefiks?',
         r'''<p>Trie svih $S_i$: čvor $u$ na dubini $l$ predstavlja prefiks, a $val[u] = \min_{S \text{ kroz } u} cost(|S| - l)$ računamo hodajući svakim $S$ kroz njegove čvorove — ukupno $\sum |S_i|$ koraka. Zatim $dp[i+l] = \min(dp[i] + 1 + val[u])$ gdje $u$ dobivamo hodanjem trie-om po $T$ od pozicije $i$; hodanje staje kad slovo ne postoji. Kako je $\sum |T| \le 5000$, $O(|T|^2)$ prijelaza je zanemarivo.</p>'''),
    ],
    'tips': [
        r'''Operacije „dodaj na kraj / briši s kraja” daju stogovnu strukturu: od svakog dodavanja preživi prefiks, a konačni string je konkatenacija takvih prefiksa. To odmah sugerira DP po prefiksima cilja.''',
        r'''Kad cijena nekog koraka ovisi o brojevima do $K$ preko „zbroj modulo $K$”, radi se o najkraćem putu na ostacima — Dijkstra ili BFS po $K$ vrhova, a ne DP kvadratne složenosti.''',
        r'''Broj različitih duljina među stringovima ukupne duljine $\Sigma$ je najviše $O(\sqrt{\Sigma})$ — klasična ušteda kad prijelaz ovisi samo o duljini.''',
        r'''Kad treba „najjeftiniji string s danim prefiksom”, trie s agregatom po podstablu je standardna struktura; agregat popuni obilaskom svakog stringa umjesto rekurzije.''',
    ],
    'detailed': r'''
<h3>1. Struktura konačnog stringa</h3>
<p>Dodavanje piše na kraj, brisanje briše s kraja. Promatrajmo bilo koji niz poteza koji završava sa stringom $T$. Znak dodan pritiskom tipke $S$ preživio je ako nikad nije obrisan; ako je preživio, preživjeli su i svi znakovi iz istog $S$ ispred njega (brisanje bi ih dosegnulo tek nakon njega). Zato je doprinos svakog pritiska <em>prefiks</em> stringa $S$ (možda prazan), i</p>
<p style="text-align:center">$T = P_1 P_2 \cdots P_b,\qquad P_j$ neprazan prefiks nekog $S_{i_j}$,</p>
<p>gdje su blokovi u redoslijedu pritisaka. Pritiske s praznim doprinosom zovemo <em>smeće</em>.</p>
<h3>2. Rastav na neovisne blokove</h3>
<p><strong>Lema.</strong> U trenutku pritiska tipke bloka $j+1$ string je točno $P_1 \cdots P_j$.<br>
<em>Dokaz.</em> Prefiks $P_1 \cdots P_j$ nikad ne biva obrisan (svi ti znakovi preživljavaju do kraja). Sve što je u tom trenutku iza $P_j$ ostat će u konačnom stringu između $P_j$ i $P_{j+1}$, osim ako se obriše — ali brisanje s kraja bi prije toga obrisalo cijeli $P_{j+1}$, koji preživljava. Dakle iza $P_j$ nema ničega. $\square$</p>
<p>Zato se potezi dijele na $b$ faza: u fazi $j$ pritisnemo $S_{i_j}$ (jedan potez), a zatim obrišemo točno višak $x_j = |S_{i_j}| - |P_j|$ znakova, pri čemu smijemo dodavati smeće; faza završava kad string postane $P_1 \cdots P_j$. Broj poteza u fazi $j$ je $1 + (\text{najmanji broj poteza da se obriše točno } x_j \text{ znakova})$. Taj broj, $cost(x_j)$, ne ovisi o sadržaju ispred (backspace gleda samo duljinu, a duljina je $\ge x_j$ kad god $x_j \ge K$).</p>
<h3>3. Funkcija $cost(x)$</h3>
<p>$cost(0) = 0$. Za $x \gt 0$ imamo dva slučaja:</p>
<ul>
<li>$x \ge K$: tvrdimo $cost(x) = 1 + cost(x - K)$. Svaki niz poteza koji obriše točno $x$ znakova sadrži barem jedan backspace; premjestimo prvi backspace na sam početak. Dodavanja prije njega samo su povećavala višak, pa je backspace na početku dopušten ($x \ge K$) i briše $K$ znakova viška; ostatak niza sada briše višak $x - K$ plus isto smeće — isti broj poteza, ista završna situacija. Dakle optimalno je brisati odmah.</li>
<li>$0 \lt x \lt K$: backspace bi ili obrisao dio sačuvanog stringa (ako je ukupna duljina $\ge K$) ili ne bi učinio ništa — u oba slučaja beskoristan. Prvi potez je dodavanje nekog $S_i$; nakon njega višak je $x + |S_i|$ i važna je samo duljina: $cost(x) = 1 + \min_{L \in \mathcal{L}} cost(x + L)$, gdje je $\mathcal{L}$ skup različitih duljina među $S_i$.</li>
</ul>
<p>Iz prvog slučaja indukcijom: $cost(x) = \lfloor x/K \rfloor + cost(x \bmod K)$. Za ostatke $r \in [1, K-1]$ drugi slučaj glasi $cost(r) = 1 + \min_L \left(\lfloor (r+L)/K \rfloor + cost((r+L) \bmod K)\right)$: to je <strong>najkraći put</strong> u usmjerenom grafu s vrhovima $0, \dots, K-1$, bridovima $r \to (r+L) \bmod K$ težine $1 + \lfloor (r+L)/K \rfloor \ge 1$ i ciljem $0$ (udaljenost $0$). Računamo ga Dijkstrom iz cilja po obrnutim bridovima: iz $r'$ u $r = (r' - L) \bmod K$ s istom težinom. Vrhovi nedostižni do $0$ imaju $cost = \infty$ (višak te veličine se ne može obrisati). Broj bridova je $K \cdot |\mathcal{L}|$, a $|\mathcal{L}| \le \sqrt{2\sum|S_i|} \approx 1414$ jer različite duljine $1, 2, \dots, d$ zbrajaju se na $d(d+1)/2 \le \sum |S_i|$.</p>
<h3>4. Najjeftiniji blok za dani podstring</h3>
<p>Za blok koji daje $P = T[i..i+l)$ trebamo $\min\{ cost(|S| - l) : S \in \{S_i\},\ P \text{ prefiks od } S \}$. Ubacimo sve $S_i$ u trie; čvor $u$ dubine $l$ odgovara prefiksu duljine $l$. Definiramo $val[u] = \min_{S \text{ prolazi kroz } u} cost(|S| - \mathrm{dubina}(u))$. Umjesto rekurzije po podstablu, za svaki $S$ prođemo njegovim čvorovima $u_1, \dots, u_{|S|}$ i za svaki postavimo $val[u_k] \leftarrow \min(val[u_k], cost(|S| - k))$: ukupno $\sum |S_i|$ koraka, svaki $O(1)$ preko $cost(x) = cres[x \bmod K] + \lfloor x/K \rfloor$.</p>
<h3>5. DP po prefiksima cilja</h3>
<p>$dp[i]$ = najmanji broj poteza da string bude točno $T[0..i)$. $dp[0] = 0$ i</p>
<p style="text-align:center">$dp[i + l] = \min\big(dp[i + l],\ dp[i] + 1 + val[u_l]\big)$, gdje je $u_l$ čvor trie-a za $T[i..i+l)$.</p>
<p>Za fiksni $i$ hodamo trie-om po slovima $T[i], T[i+1], \dots$ dok put postoji. Ispravnost: po odjeljcima 1–2 svaki valjan niz poteza rastavlja se na blokove čija je ukupna cijena $\sum (1 + cost(x_j))$, a za blok s prefiksom $P_j$ najbolji izbor tipke daje točno $val[u]$; obratno, svaki DP put odgovara stvarnom nizu poteza (pritisak, zatim optimalan niz brisanja/smeća iz definicije $cost$). Odgovor je $dp[|T|]$, ili $-1$ ako je $\infty$.</p>
<h3>6. Složenost</h3>
<p>Dijkstra: $O(K |\mathcal{L}| \log K)$ — u najgorem slučaju $\approx 7 \cdot 10^6$ relaksacija; trie: $O(26 \sum |S_i|)$ memorije i $O(\sum |S_i|)$ vremena za gradnju i $val$; DP: $O(|T|^2)$ s $\sum |T| \le 5000$. Sve unutar $1.5$ s. Napomena: $\sum K$ preko testova nije ograničen, pa bi bilo kakav $O(K^2)$ po testu bio prespor; zato je bitno da graf ostataka ima $K|\mathcal{L}|$, a ne $K^2$ bridova.</p>
<h3>7. Primjer</h3>
<p>$K = 3$, $S = \{\texttt{defgh}, \texttt{abc}\}$, $T = \texttt{abcde}$. $\mathcal{L} = \{3, 5\}$; $cost(0) = 0$, $cost(3) = 1$, $cost(1) = 1 + \min(cost(4), cost(6)) = 1 + \min(2, 2) = 3$, $cost(2) = 1 + \min(cost(5), cost(7)) = 1 + \min(cost(2)+1, cost(1)+2)$, tj. $cost(2) = 1 + \min(cost(2) + 1, 5) = 6$. Blok $\texttt{abc}$: $x = 0$, $dp[3] = 1$. Blok $\texttt{de}$ iz $\texttt{defgh}$: $x = 3$, $cost = 1$, $dp[5] = 1 + 1 + 1 = 3$. Drugi primjer: $T = \texttt{b}$, a nijedan $S$ ne počinje s $\texttt{b}$ — trie nema puta, $dp[1] = \infty$, odgovor $-1$.</p>
<h3>8. Zamke</h3>
<ul>
<li>Backspace pri duljini $\lt K$ ne radi ništa — u analizi se to pojavljuje samo kao „beskorisan potez”, ali tvoj brute force mora ga simulirati doslovno.</li>
<li>$cost$ može biti $\infty$ za neke ostatke (npr. $K = 2$, sve duljine parne, $x$ neparan): tada blok nije moguć; ne zbrajati $\infty + 1$ u tipu koji prelijeva — provjeravati prije zbrajanja.</li>
<li>Trie s $10^6$ čvorova $\times 26$ pokazivača je $\approx 100$ MB — unutar $512$ MiB, ali ne alocirati po testu više nego treba ($\sum |S_i| \le 10^6$ ukupno).</li>
<li>Brojevi poteza mogu biti veliki ($cost$ do $\approx 10^6$ po bloku), koristi 64-bitne tipove za $dp$.</li>
</ul>
''',
    'verified': r'''uzorak 1/1; 300 slučajnih testova ($N \le 3$, $K \le 3$, $|S_i| \le 3$, $|T| \le 5$, abeceda $\{a, b\}$) protiv brute forcea koji BFS-om po stvarnim stringovima doslovno simulira poteze (uz dokazanu gornju granicu duljine), plus dodatnih 1000 slučajnih testova; 3 velika testa ($\sum |S_i| = 10^6$, $K = 5000$, $|T| = 5000$).''',
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
    'solution': r'''
<p>Postoji mnogo valjanih rješenja. Jedno je odabrati $a = b$ i zatim provjeriti zadovoljava li dane LIS uvjete. Može se dokazati da, ako je odgovor <code>YES</code>, tada i $a = b$ zadovoljava uvjete.</p>
''',
    'coach': [
        (r'Kako se duljina najduljeg strogo rastućeg podniza može promijeniti kad nizu dodamo jedan element?',
         r'''<p>Ne može pasti (svaki rastući podniz prefiksa ostaje rastući podniz duljeg prefiksa) i ne može porasti za više od $1$ (iz rastućeg podniza duljine $b_{i+1}$ koji koristi novi element izbacimo taj element i dobijemo rastući podniz prefiksa $[1..i]$ duljine $b_{i+1}-1 \le b_i$). Uz $b_1 = 1$ to daje nužan uvjet: $b_1 = 1$ i $b_{i+1} - b_i \in \{0, 1\}$ za svaki $i$.</p>'''),
        (r'Je li taj nužan uvjet i dovoljan, tj. možemo li za svaki takav $b$ naći niz $a$?',
         r'''<p>Da, i to gotovo besplatno: probajmo $a = b$. Niz $b$ je tada neopadajući i na prefiksu $[1..i]$ poprima točno vrijednosti $1, 2, \dots, b_i$ (kreće od $1$ i raste u koracima po $1$). Strogo rastući podniz neopadajućeg niza ne može dvaput uzeti istu vrijednost, pa ima najviše $b_i$ članova; a podniz koji uzme prvo pojavljivanje svake vrijednosti $1, \dots, b_i$ ima točno $b_i$ članova. Dakle LIS prefiksa je $b_i$.</p>'''),
        (r'Zašto u kodu ipak isplati izravno provjeriti LIS svakog prefiksa od $a = b$?',
         r'''<p>Jer time uvjet „$b$ je valjan” i konstrukciju provjeravamo istim kodom: ako $a = b$ zadovoljava uvjete, odgovor je <code>YES</code>; ako ne, po prethodnom koraku nikakav $a$ ne postoji, pa je odgovor <code>NO</code>. Uz $n \le 10$ provjera u $O(n^2)$ je zanemariva, a štiti od pogreške u ručnom zapisu uvjeta.</p>'''),
    ],
    'tips': [
        r'''Kad se traži niz s zadanim „prefiksnim statistikama” (LIS, maksimum, broj inverzija…), prvo odredi kako se statistika može promijeniti dodavanjem jednog elementa — to odmah daje nužne uvjete i često sugerira konstrukciju.''',
        r'''Najjednostavniji kandidat (ovdje $a = b$) često je i ispravan; prije traženja pametne konstrukcije provjeri trivijalne.''',
        r'''Kad je provjera valjanosti jeftina, umjesto ručno zapisanog uvjeta isplati se provjeriti kandidata izravno — jedan kod za oba slučaja (<code>YES</code>/<code>NO</code>) smanjuje mogućnost greške.''',
    ],
    'detailed': r'''
<h3>1. Kako se LIS prefiksa mijenja</h3>
<p>Označimo s $\mathrm{LIS}(i)$ duljinu najduljeg strogo rastućeg podniza od $a[1..i]$. Dvije jednostavne činjenice vrijede za <em>svaki</em> niz $a$:</p>
<ul>
<li>$\mathrm{LIS}(i+1) \ge \mathrm{LIS}(i)$, jer je svaki rastući podniz od $a[1..i]$ ujedno rastući podniz od $a[1..i+1]$;</li>
<li>$\mathrm{LIS}(i+1) \le \mathrm{LIS}(i) + 1$: uzmimo najdulji rastući podniz od $a[1..i+1]$. Ako ne koristi $a_{i+1}$, on je podniz od $a[1..i]$ pa je $\mathrm{LIS}(i+1) \le \mathrm{LIS}(i)$. Ako koristi $a_{i+1}$, izbacimo taj posljednji element; ostatak je rastući podniz od $a[1..i]$ duljine $\mathrm{LIS}(i+1) - 1$, dakle $\mathrm{LIS}(i+1) - 1 \le \mathrm{LIS}(i)$.</li>
</ul>
<p>Uz očito $\mathrm{LIS}(1) = 1$ dobivamo <strong>nužan uvjet</strong> na $b$: $b_1 = 1$ i $b_{i+1} - b_i \in \{0, 1\}$ za sve $i$. Primjer $b = (1,2,3,2,5,7)$ pada već na $b_4 = 2 \lt b_3 = 3$, pa je odgovor <code>NO</code>.</p>
<h3>2. Konstrukcija $a = b$ i dokaz</h3>
<p>Pretpostavimo da $b$ zadovoljava nužan uvjet. Tvrdimo da $a = b$ radi. Niz $b$ je neopadajući, počinje s $1$ i raste u koracima od $0$ ili $1$, pa skup vrijednosti na prefiksu $b[1..i]$ iznosi točno $\{1, 2, \dots, b_i\}$ (svaka vrijednost između $1$ i $b_i$ mora se pojaviti jer se ne može „preskočiti”).</p>
<ul>
<li><em>Gornja granica.</em> Strogo rastući podniz neopadajućeg niza ima međusobno različite vrijednosti (strogo raste), a sve su iz skupa $\{1, \dots, b_i\}$; dakle ima najviše $b_i$ članova.</li>
<li><em>Donja granica.</em> Uzmimo za svaku vrijednost $v = 1, \dots, b_i$ prvo pojavljivanje u $b$. Ta pojavljivanja dolaze u rastućem redoslijedu indeksa (niz je neopadajući, pa se manja vrijednost prvi put pojavi prije veće) i vrijednosti strogo rastu: dobili smo strogo rastući podniz duljine $b_i$ unutar prefiksa $[1..i]$.</li>
</ul>
<p>Dakle $\mathrm{LIS}(i) = b_i$ za svaki $i$, tj. $a = b$ je valjan odgovor. Vrijednosti su u $[1, 10] \subseteq [1, 100]$, kako zadatak traži. Zajedno s prvim odjeljkom dobivamo karakterizaciju: rješenje postoji ako i samo ako $b_1 = 1$ i svi koraci su $0$ ili $1$; a ako postoji, $a = b$ je jedno rješenje.</p>
<h3>3. Algoritam</h3>
<ol>
<li>Stavi $a = b$.</li>
<li>Izračunaj $\mathrm{LIS}(i)$ za sve prefikse klasičnim $O(n^2)$ DP-om ($dp_i = 1 + \max_{j \lt i,\ a_j \lt a_i} dp_j$, $\mathrm{LIS}(i) = \max_{j \le i} dp_j$).</li>
<li>Ako je $\mathrm{LIS}(i) = b_i$ za sve $i$, ispiši <code>YES</code> i $a$; inače <code>NO</code>.</li>
</ol>
<p>Korak 3 je korektan u oba smjera: ako provjera prođe, $a$ je očito valjan; ako ne prođe, po odjeljku 2 uvjet iz odjeljka 1 ne vrijedi (inače bi $a = b$ prošao), pa niz ne postoji. Zato ne treba posebno kodirati uvjet „koraci $0$/$1$” — provjera ga implicitno obavlja.</p>
<h3>4. Složenost i zamke</h3>
<p>$O(n^2)$ po testu, ukupno $O(\sum n \cdot 10)$ — trenutno. Jedina zamka je čitanje uvjeta: traži se <em>strogo</em> rastući podniz, pa $(5, 5)$ ima LIS $1$, a ne $2$; zbog toga niz $a$ smije imati jednake susjedne vrijednosti točno ondje gdje $b$ stagnira.</p>
''',
    'verified': r'''uzorak 1/1 (checker prihvaća bilo koji valjan niz); 300 slučajnih testova ($n \le 6$) uspoređeno s brute forceom koji iscrpno pretražuje sve nizove $a \in \{1,\dots,n\}^n$ (odgovor <code>YES</code>/<code>NO</code> mora se slagati), a ispisani niz provjeren checkerom koji izravno računa LIS svih prefiksa; 3 velika testa ($T = 4000$, $n = 10$).''',
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
    'solution': r'''
<p>Uočimo da u svakom savršenom stringu negdje moraju postojati dva susjedna jednaka znaka. Inače promotrimo najbliži par u podjeli, recimo $(i, j)$. Očito je $j \gt i + 1$, a svaki $i \lt k \lt j$ morao bi ostati nesparen.</p>
<p>Također, za svaki takav par susjednih znakova optimalno ih je spariti međusobno. Naime, ako je podjela sadržavala $(i', i)$ i $(j', j)$, lako se provjeri da je valjano umjesto toga spariti $(i, j)$ i $(i', j')$.</p>
<p>To znači da, ako u savršenom stringu krenemo slijeva nadesno i stalno sparujemo (i uklanjamo) jednake znakove, na kraju moramo dobiti prazan string. To se simulira stogom: skidamo vrh ako je trenutni znak jednak vrhu stoga, inače trenutni znak stavljamo na stog.</p>
<p>Neka je $f(n)$ broj savršenih stringova duljine $2n$. Neka je $g(n)$ broj savršenih stringova duljine $2n + 2$ u kojima su prvi i posljednji znak oba $a$, a stog je prazan samo prije stavljanja prvog znaka i nakon obrade svih znakova.</p>
<p>Vrijedi $g(0) = 1$ i $g(n) = (c - 1)\sum_{k=0}^{n-1} g(k)\,g(n-1-k)$ za $n \ge 1$. Funkcija izvodnica $G(x)$ zadovoljava $G(x) - 1 = (c-1)\,x\,G^2(x)$, pa je $G(x) = \dfrac{1 - \sqrt{1 - 4(c-1)x}}{2(c-1)x}$.</p>
<p>Također $f(0) = 1$ i $f(n) = c\sum_{k=0}^{n-1} g(k)\,f(n-1-k)$ za $n \ge 1$. Stoga $F(x) - 1 = c\,x\,G(x)\,F(x)$, tj. $F(x) = \dfrac{1}{1 - c\,x\,G(x)}$.</p>
<p>Dakle $F(x) = \dfrac{1}{1 - \frac{c}{2(c-1)}\left(1 - \sqrt{1 - 4(c-1)x}\right)}$, što se može preurediti u oblik $\dfrac{\alpha + \beta\sqrt{1 - \gamma x}}{1 - \delta x}$ za neke konstante $\alpha, \beta, \gamma, \delta$. Razvoj toga daje formulu složenosti $O(n)$.</p>
''',
    'coach': [
        (r'Kako prepoznati savršen string bez traženja podjele na parove?',
         r'''<p>U svakoj podjeli bez ispreplitanja postoji par susjednih indeksa $(i, i+1)$: uzmi par $(i, j)$ s najmanjim $j - i$; svaki $k$ strogo između bio bi sparen s nekim izvan $(i, j)$, što je ispreplitanje, ili unutar, što proturječi minimalnosti. Dalje, ako su $S[i] = S[i+1]$ susjedni jednaki znakovi, oni se <em>smiju</em> spariti međusobno: ako su bili spareni s $i'$ i $j'$, zamjena za $(i, i+1), (i', j')$ opet je bez ispreplitanja (provjera slučajeva). Zato je string savršen ako i samo ako ga redukcija stogom — skini vrh kad je jednak trenutnom znaku, inače stavi — svede na prazan stog.</p>'''),
        (r'Koja je prirodna rekurzija za takve „zagradne” strukture?',
         r'''<p>Rastav po <em>prvom povratku</em> stoga na početnu razinu, kao za Catalanove brojeve. Neka $g(k)$ broji stringove duljine $2k$ koji, obrađeni nad stogom čiji je vrh $a$, nikad ne skidaju $a$ i završavaju s istim stogom; $g(0) = 1$, a za $k \ge 1$ prvi znak je $b \ne a$ ($c - 1$ izbora), skida se na poziciji $2j + 2$ uz unutrašnjost $g(j)$ i ostatak $g(k - 1 - j)$: $g(k) = (c-1)\sum_j g(j)\,g(k-1-j)$. Slično $f(n) = c\sum_j g(j)\,f(n-1-j)$ za sve savršene stringove (prvi znak slobodan).</p>'''),
        (r'Kako od rekurzija konvolucijskog tipa doći do formule u $O(n)$?',
         r'''<p>Konvolucije su umnošci funkcija izvodnica: $G = 1 + (c-1)xG^2$ i $F = 1 + cxGF$. Prva je kvadratna, $G = \frac{1 - \sqrt{1 - 4(c-1)x}}{2(c-1)x}$; uvrštavanjem u $F = 1/(1 - cxG)$ i racionalizacijom dobivamo $F(x) = \dfrac{(2-c) + c\sqrt{1-4(c-1)x}}{2(1 - c^2x)}$. Korijen razvijamo poznatim redom $\sqrt{1-4y} = 1 - 2\sum_{k\ge1} \mathrm{Cat}(k-1) y^k$, a $1/(1-c^2x)$ je geometrijski red; koeficijent uz $x^n$ je konačna suma.</p>'''),
        (r'Kako izračunati $10^7$ Catalanovih brojeva modulo prost broj dovoljno brzo?',
         r'''<p>Iterativno: $\mathrm{Cat}(k) = \mathrm{Cat}(k-1)\cdot\frac{2(2k-1)}{k+1}$, a inverze $1, \dots, 10^7 + 1$ predračunamo linearno formulom $inv[i] = -\lfloor p/i \rfloor \cdot inv[p \bmod i]$. Uz $\sum n \le 10^7$ svaki test košta $O(n)$ množenja, bez ikakvog logaritma u petlji.</p>'''),
    ],
    'tips': [
        r'''Uvjet „parovi se ne isprepliću” = zagradna struktura; uvijek postoji „najuži” par, koji je susjedan. To daje redukciju stogom i rekurzije Catalanova tipa (rastav po prvom povratku na početnu razinu).''',
        r'''Rekurzija oblika $a_n = \sum_k b_k a_{n-1-k}$ je umnožak funkcija izvodnica; kvadratna jednadžba za $G$ rješava se korijenom, a $\sqrt{1-4y}$ ima poznat razvoj preko Catalanovih brojeva.''',
        r'''Provjeri zatvorenu formulu na rubnim vrijednostima ($c = 1$, mali $n$) protiv brute forcea prije nego što se pouzdaš u algebru — izvodi s korijenima lako pokupe krivi predznak.''',
        r'''Za mnogo upita s velikim $n$ i $\sum n$ ograničenim, računaj faktore (Catalan, potencije) iterativno uz linearnu tablicu inverza, a ne binarnim potenciranjem po članu.''',
    ],
    'detailed': r'''
<h3>1. Karakterizacija stogom</h3>
<p>Redukcija stogom: prolazimo string slijeva; ako je stog neprazan i vrh jednak trenutnom znaku, skidamo vrh (tvoreći par), inače stavljamo znak na stog. Tvrdimo: <strong>string je savršen ako i samo ako redukcija završi praznim stogom.</strong></p>
<p><em>($\Leftarrow$)</em> Parovi koje redukcija tvori su jednaki znakovi i ne isprepliću se: kad se skida par $(i, j)$, svi znakovi stavljeni između $i$ i $j$ već su skinuti, dakle spareni unutar $(i, j)$.</p>
<p><em>($\Rightarrow$)</em> Indukcijom po duljini. Neka je $S$ savršen s podjelom $\mathcal P$. <em>Korak 1:</em> postoji par susjednih indeksa. Uzmimo $(i, j) \in \mathcal P$ s najmanjim $j - i$; kad bi bilo $k$ s $i \lt k \lt j$, njegov partner $k'$ ne može biti unutar $(i, j)$ (par bi bio uži) ni izvan (ispreplitanje). Dakle $j = i + 1$ i $S[i] = S[i+1]$, pa redukcija stogom sigurno nešto skida; neka je prvo skidanje na poziciji $j$ (par $(j-1, j)$). <em>Korak 2:</em> podjela $\mathcal P$ smije se preurediti tako da sadrži $(j-1, j)$. Ako već sadrži, gotovo. Inače su $j-1$ i $j$ spareni s nekim $a$ i $b$; zamijenimo parove $(a, j-1), (b, j)$ parovima $(j-1, j)$ i $(a, b)$ (znakovi su jednaki jer $S[a] = S[j-1] = S[j] = S[b]$). Par $(j-1, j)$ ne isprepliće se ni s čim (nema indeksa između). Par $(a, b)$: promotrimo glavni slučaj $a \lt j-1 \lt j \lt b$. Kad bi se $(a, b)$ ispreplitao s nekim $(u, v) \in \mathcal P$, točno jedan od $u, v$ (recimo $u$) bio bi strogo između $a$ i $b$, dakle u $(a, j-1)$ ili u $(j, b)$, a $v$ izvan $[a, b]$. Ako je $u \in (a, j-1)$, onda je $v$ izvan $(a, j-1)$ i $(u, v)$ se isprepliće s izvornim parom $(a, j-1)$; ako je $u \in (j, b)$, isprepliće se s $(j, b)$ — u oba slučaja kontradikcija s valjanošću $\mathcal P$. Slučajevi kad su $a$ i $b$ s iste strane (npr. $a \lt b \lt j-1$) provjeravaju se istom vrstom argumenta: uljez u $(a, b)$ s partnerom izvan isprepliće se s $(a, j-1)$ ako je partner izvan $(a, j-1)$, a inače s $(b, j)$. <em>Korak 3:</em> izbacimo $j-1$ i $j$; ostatak je savršen (podjela $\mathcal P \setminus \{(j-1,j)\}$ i dalje je bez ispreplitanja) i kraći, pa se po indukciji reducira do praznog stoga; a redukcija stogom cijelog $S$ nakon skidanja $(j-1, j)$ nastavlja točno kao redukcija ostatka. $\square$</p>
<h3>2. Rekurzije</h3>
<p>Neka je $f(n)$ broj savršenih stringova duljine $2n$; $f(0) = 1$. Neka je $g(k)$ broj stringova duljine $2k$ koji, obrađeni redukcijom nad stogom čiji je vrh neko slovo $a$, nikad ne skidaju to $a$ i završavaju s nepromijenjenim stogom; $g(0) = 1$ i $g$ ne ovisi o $a$ (zamjena slova je bijekcija). Za savršen string duljine $2n \ge 2$ prvi znak $x$ (bilo koji od $c$) stavlja se na stog i skida se prvi put na nekoj poziciji $2j+2$ — <em>rastav po prvom povratku na praznu razinu</em>. Unutrašnjost duljine $2j$ nikad ne skida $x$ (inače bi se $x$ skinuo ranije) i vraća stog na $[x]$: $g(j)$ mogućnosti. Ostatak, duljine $2(n-1-j)$, počinje s praznim stogom i savršen je: $f(n-1-j)$. Dakle</p>
<p style="text-align:center">$f(n) = c\sum_{j=0}^{n-1} g(j)\,f(n-1-j).$</p>
<p>Za $g(k)$, $k \ge 1$: prvi znak $b$ ne smije biti $a$ (skinuo bi $a$): $c - 1$ izbora; $b$ se prvi put skida na poziciji $2j+2$ uz unutrašnjost koja nikad ne skida $b$ — $g(j)$; ostatak nad stogom s vrhom $a$ ne skida $a$ — $g(k-1-j)$. Dakle</p>
<p style="text-align:center">$g(k) = (c-1)\sum_{j=0}^{k-1} g(j)\,g(k-1-j).$</p>
<p>(Službeni editorijal definira $g$ s uključenim vanjskim parom; brojevi su isti.)</p>
<h3>3. Funkcije izvodnice</h3>
<p>S $G(x) = \sum g(k)x^k$ i $F(x) = \sum f(n) x^n$ konvolucije postaju umnošci: $G = 1 + (c-1)xG^2$ i $F = 1 + cxGF$. Iz kvadratne jednadžbe, $G = \dfrac{1 - s}{2(c-1)x}$ gdje je $s = \sqrt{1 - 4(c-1)x}$ (predznak biramo tako da $G(0) = 1$). Tada $cxG = \dfrac{c(1-s)}{2(c-1)}$ i</p>
<p style="text-align:center">$1 - cxG = \dfrac{(c-2) + cs}{2(c-1)},\qquad F = \dfrac{2(c-1)}{(c-2) + cs}.$</p>
<p>Racionaliziramo množenjem s $(c-2) - cs$: nazivnik postaje $(c-2)^2 - c^2 s^2 = c^2 - 4c + 4 - c^2 + 4c^2(c-1)x = -4(c-1)(1 - c^2x)$, pa</p>
<p style="text-align:center">$F(x) = \dfrac{(2-c) + c\sqrt{1-4(c-1)x}}{2\,(1 - c^2 x)}.$</p>
<h3>4. Koeficijenti</h3>
<p>Poznati razvoj $\sqrt{1-4y} = 1 - 2\sum_{k \ge 1} \mathrm{Cat}(k-1)\,y^k$ (npr. $1 - 2y - 2y^2 - 4y^3 - 10y^4 - \dots$) uz $y = (c-1)x$ daje brojnik $\frac{(2-c) + cs}{2} = 1 - c\sum_{k\ge1}\mathrm{Cat}(k-1)(c-1)^k x^k$. Množenje geometrijskim redom $\frac{1}{1-c^2x} = \sum_m c^{2m}x^m$ i čitanje koeficijenta uz $x^n$:</p>
<p style="text-align:center">$f(n) = c^{2n} - \sum_{k=1}^{n} \mathrm{Cat}(k-1)\,(c-1)^k\,c^{\,2n-2k+1}.$</p>
<p>Provjera: $n = 2$, $c = 2$: $16 - (1\cdot1\cdot 8 + 1\cdot1\cdot 2) = 6$. Za $c = 1$ svi članovi sume su $0$ i $f(n) = 1$ — točno, jedini string $a^{2n}$ je savršen; izvod preko $G$ dijeli s $c - 1$, ali konačna formula vrijedi i za $c = 1$ (rekurzije su polinomijalne u $c$, pa identitet koeficijenata koji vrijedi za sve $c \ge 2$ vrijedi kao polinomijalni identitet).</p>
<h3>5. Implementacija</h3>
<ul>
<li>Predračunamo $inv[i]$ za $i \le 10^7 + 1$ linearno: $inv[i] = -\lfloor p/i \rfloor \cdot inv[p \bmod i] \pmod p$ (jer $p = \lfloor p/i \rfloor i + (p \bmod i)$).</li>
<li>Po testu: $\mathrm{Cat}(0) = 1$, $\mathrm{Cat}(k) = \mathrm{Cat}(k-1)\cdot 2(2k-1)\cdot inv[k+1]$; član $(c-1)^k c^{2n-2k+1}$ počinjemo s $(c-1)c^{2n-1}$ i svaki korak množimo s $(c-1)\cdot (c^2)^{-1}$. Zbroj oduzmemo od $c^{2n}$.</li>
</ul>
<p>Složenost $O(n)$ po testu plus $O(10^7)$ predračun; ukupno $O(\sum n + 10^7)$ uz $\sum n \le 10^7$. Memorija: tablica inverza od $10^7$ 32-bitnih brojeva ($40$ MB).</p>
<h3>6. Zamke</h3>
<ul>
<li>$c$ do $10^7 \lt p$, pa je $c^2 \not\equiv 0$ i inverz postoji; $c - 1$ može biti $0$ — formula to tolerira, ali ne dijeliti s $c - 1$.</li>
<li>$2n$ do $2 \cdot 10^7$ u eksponentu — koristiti 64-bitne tipove u potenciranju; svi umnošci dvaju ostataka moraju ići kroz <code>long long</code>.</li>
<li>Tablicu inverza držati kao <code>vector&lt;int&gt;</code>, ne <code>long long</code> — pola memorije.</li>
<li>Predznak: $f(n) = c^{2n} - \Sigma$; rezultat normalizirati u $[0, p)$.</li>
</ul>
''',
    'verified': r'''uzorak 1/1; 300 slučajnih testova ($n \le 4$, $c \le 4$) protiv brute forcea koji nabraja sve $c^{2n}$ stringove i intervalnom dinamikom neovisno provjerava postoji li podjela na parove bez ispreplitanja; 3 velika testa ($n = 10^7$, $c \in \{1, 2, 123456, 10^7\}$).''',
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
    'coach': [
        (r'Koje je jednostavnije pitanje od „može li $x$ biti jedini pobjednik”?',
         r'''<p>„Postoji li glasanje u kojem nitko ne dobije više od $t$ glasova?” To je pitanje o kapacitetima i monotono je u $t$. Na stablu ga rješava pohlepni DP odozdo: $f_t(x)$ = najmanji broj glasova koji iz podstabla od $x$ <em>moraju</em> otići strogim precima od $x$. Djeca su neovisna, $x$ upije najviše $t$ dolaznih glasova, ostatak i vlastiti glas od $x$ idu gore: $f_t(x) = [x \ne 1] + \max(0, \sum_{y} f_t(y) - t)$. Glasanje postoji ako i samo ako $f_t(1) = 0$. Najmanji takav $t$ zovemo $z$ i nalazimo ga binarnim pretraživanjem.</p>'''),
        (r'Što $z$ govori o pobjedniku, i koje vrhove odmah možemo razvrstati?',
         r'''<p>U svakom glasanju netko dobije $\ge z$ glasova, a postoji glasanje s maksimumom točno $z$. Vrh $x$ može dobiti najviše $S_x$ glasova (broj strogih potomaka). Ako je $S_x \lt z$, $x$ ne može biti jedini pobjednik. Ako je $S_x \gt z$, uzmemo glasanje s maksimumom $z$ i sve potomke od $x$ preusmjerimo na $x$: $x$ ima $S_x \gt z$, a ostali nisu dobili ništa novo — $x$ pobjeđuje. Ostaje granični slučaj $S_x = z$.</p>'''),
        (r'Što točno mora vrijediti kad je $S_x = z$?',
         r'''<p>Svi potomci od $x$ glasaju za $x$ (inače $x$ ima $\lt z$), a svi ostali vrhovi smiju dobiti najviše $z - 1$. To je isti problem s kapacitetima kao prije, samo s kapacitetom $z - 1$ svugdje osim u $x$, gdje je $z$. Vrijednosti $f_{z-1}$ mijenjaju se samo na putu od $x$ do korijena, pa gledamo kako se promjena širi.</p>'''),
        (r'Kako se povećanje kapaciteta u $x$ za $1$ odražava na $f$ predaka?',
         r'''<p>Označimo $e(y) = \max(0, \sum_{\text{djeca}} f_{z-1} - (z-1))$ „višak” u $y$. Kako je $\sum_{\text{djeca}} f \le S_x = z$, u $x$ je $e(x) \le 1$ i s kapacitetom $z$ višak postaje $0$: $f(x)$ padne za $e(x)$. Ako je $e(x) = 0$, ništa se ne mijenja i $f_{z-1}(1) \ge 1$ ostaje — nemoguće. Ako je $e(x) = 1$, smanjenje za $1$ putuje prema korijenu: roditelj $p$ prenosi smanjenje točno ako je $e(p) \ge 1$ (inače ga $\max(0, \cdot)$ proguta). Dakle uvjet je: $e(y) \ge 1$ za sve $y$ na putu od $x$ do korijena i $f_{z-1}(1) = 1$ (smanjenje za $1$ mora korijen spustiti na $0$).</p>'''),
    ],
    'tips': [
        r'''„Može li $x$ biti strogi maksimum?” razdvoji na „koliki je najmanji mogući maksimum $z$” (binarno pretraživanje + provjera izvedivosti) i „može li $x$ premašiti / točno dostići $z$”.''',
        r'''Provjera izvedivosti s kapacitetima na stablu gotovo je uvijek pohlepni DP odozdo: svako podstablo izvozi najmanje što mora, jer upijanje bliže izvoru nikad ne šteti.''',
        r'''Kad se jedan parametar promijeni u jednom vrhu, promjena $f$-vrijednosti širi se samo po putu do korijena i kroz $\max(0,\cdot)$ prolazi samo tamo gdje je argument pozitivan — to omogućuje odgovor za sve $x$ iz jednog izračuna.''',
        r'''Roditelji su indeksirani manje od djece ($P_u \lt u$): obradi vrhove od $N$ do $1$ i nema rekurzije ni sortiranja po dubini.''',
    ],
    'detailed': r'''
<h3>1. Izvedivost s kapacitetom $t$</h3>
<p>Fiksirajmo $t$ i pitajmo: postoji li glasanje u kojem svaki vrh dobije najviše $t$ glasova? Glas vrha $u$ ide nekom strogom pretku, dakle ili nekom vrhu unutar podstabla od $x$ (ako je $u$ u podstablu od $x$, $u \ne x$) ili strogom pretku od $x$. Definirajmo $f_t(x)$ = najmanji mogući broj glasova iz podstabla od $x$ (uključujući glas samog $x$ ako $x \ne 1$) koji odlaze strogim precima od $x$, uz kapacitet $t$ u svakom vrhu podstabla.</p>
<p><strong>Lema.</strong> $f_t(x) = [x \ne 1] + \max\!\left(0, \sum_{y \in \text{djeca}(x)} f_t(y) - t\right)$.<br>
<em>Donja ograda.</em> U svakom valjanom glasanju iz podstabla svakog djeteta $y$ izlazi barem $f_t(y)$ glasova (indukcija). Ti glasovi idu ili u $x$ (najviše $t$) ili dalje gore, pa dalje gore ide barem $\max(0, \sum f_t(y) - t)$, a k tome glas samog $x$.<br>
<em>Dostižnost.</em> Uzmimo u svakom djetetu glasanje koje ostvaruje $f_t(y)$ izlaznih (podstabla su disjunktna, izbori neovisni). Od $\sum f_t(y)$ dolaznih glasova $x$ upije $\min(t, \sum f_t(y))$, ostatak proglasimo izlaznima — oni će biti dodijeljeni nekom pretku kasnije u istom postupku. $\square$</p>
<p>Glasanje s kapacitetom $t$ postoji ako i samo ako $f_t(1) = 0$ (korijen nema kome proslijediti). Za $t = N - 1$ postoji (svi glasaju za direktora), a $f_t$ je neopadajuća u $t$ po vrhu (indukcija), pa binarnim pretraživanjem na $[1, N-1]$ nađemo $z$ = najmanji izvediv $t$. Vrhove obrađujemo u redoslijedu $N, N-1, \dots, 1$ — zbog $P_u \lt u$ djeca su obrađena prije roditelja — pa je jedna provjera $O(N)$ bez rekurzije, a binarno pretraživanje $O(N \log N)$.</p>
<h3>2. Značenje $z$ i lagani slučajevi</h3>
<p>$z$ je najmanji mogući maksimalni broj glasova: u svakom glasanju netko dobije $\ge z$, i postoji glasanje $V^*$ u kojem svi dobiju $\le z$. Neka je $S_x$ broj strogih potomaka od $x$ (samo oni mogu glasati za $x$).</p>
<ul>
<li>$S_x \lt z$: $x$ dobije najviše $S_x \le z - 1$, a netko drugi $\ge z$ — <strong>ne može</strong>.</li>
<li>$S_x \gt z$: krenimo od $V^*$ i glas svakog potomka od $x$ prebacimo na $x$. Vrh $x$ ima $S_x \gt z$ glasova; nijedan drugi vrh nije dobio novi glas, pa ima $\le z \lt S_x$ — <strong>može</strong>.</li>
<li>$S_x = z$: jedini kandidat za glasanje u kojem $x$ pobjeđuje je: svi potomci glasaju za $x$ ($x$ ima točno $z$), svi ostali dobiju $\le z - 1$. Postoji li?</li>
</ul>
<h3>3. Granični slučaj $S_x = z$</h3>
<p>Tražimo glasanje s kapacitetima $c(y) = z - 1$ za $y \ne x$ i $c(x) = z$. (Ako takvo postoji, prebacivanje svih potomaka od $x$ na $x$ ga pretvara u traženo; obrat je očit.) Lema vrijedi i za kapacitete koji ovise o vrhu. Izračunajmo jednom $f := f_{z-1}$ i $\Sigma(y) := \sum_{\text{djeca}} f(y')$, te <em>višak</em> $e(y) = \max(0, \Sigma(y) - (z-1))$, tako da je $f(y) = [y \ne 1] + e(y)$. Označimo s $f'$ vrijednosti uz promijenjeni kapacitet u $x$; razlikuju se od $f$ samo na putu $x \to 1$.</p>
<p><em>U vrhu $x$.</em> Svaki glas iz podstabla djeteta broji se najviše jednom, pa je $\Sigma(x) \le S_x = z$, dakle $e(x) \le 1$, a s kapacitetom $z$ višak je $\max(0, \Sigma(x) - z) = 0$. Dakle $f'(x) = f(x) - e(x)$.</p>
<p><em>Širenje prema korijenu.</em> Ako je $e(x) = 0$, ništa se ne mijenja: $f'(1) = f(1) \ge 1$ (jer $z - 1$ nije izvediv), <strong>ne može</strong>. Ako je $e(x) = 1$, roditelj $p$ vidi $\Sigma'(p) = \Sigma(p) - 1$. Ako je $e(p) \ge 1$, tj. $\Sigma(p) \ge z$, onda je $\max(0, \Sigma(p) - 1 - (z-1)) = e(p) - 1$ i $f'(p) = f(p) - 1$ — smanjenje se prenosi dalje. Ako je $e(p) = 0$, $\max(0, \cdot)$ ostaje $0$, $f'(p) = f(p)$ i lanac se prekida, korijen ostaje $\ge 1$. Indukcijom po putu: $f'(1) = f(1) - 1$ ako svi vrhovi $y$ na putu od $x$ do $1$ (uključivo) imaju $e(y) \ge 1$, a inače $f'(1) = f(1)$. Kako trebamo $f'(1) = 0$ i $f(1) = e(1) \ge 1$, uvjet je:</p>
<p style="text-align:center">$e(y) \ge 1$ za sve $y$ na putu $x \to 1$ $\quad$ i $\quad f_{z-1}(1) = 1$.</p>
<p>Za $x = 1$ uvjet se svodi na $e(1) = 1$, što je uz $S_1 = z$ automatski (iz $\Sigma(1) \le z$ i $\Sigma(1) \gt z - 1$).</p>
<h3>4. Algoritam</h3>
<ol>
<li>Učitaj $P$, izračunaj veličine podstabala ($sz$) prolazom od $N$ do $2$.</li>
<li>Binarno pretraživanje $z$ na $[1, N-1]$; provjera je jedan prolaz koji računa $f_t$.</li>
<li>Izračunaj $f_{z-1}$ i $\Sigma$; označi $visak[y] = [\Sigma(y) \ge z]$ i $dobar[y] = visak[y] \land dobar[P_y]$ (prolaz od $1$ do $N$, roditelj prije djeteta).</li>
<li>Za svaki $x$: <code>1</code> ako $S_x \gt z$, ili $S_x = z$ i $f_{z-1}(1) = 1$ i $dobar[x]$; inače <code>0</code>.</li>
</ol>
<p>Složenost $O(N \log N)$ vremena i $O(N)$ memorije, ukupno za $\sum N \le 10^6$ daleko unutar limita.</p>
<h3>5. Primjer</h3>
<p>Lanac $1 - 2 - 3 - 4$. $t = 1$: $f(4) = 1$, $f(3) = 1 + \max(0, 1-1) = 1$, $f(2) = 1$, $f(1) = \max(0, 1 - 1) = 0$, dakle $z = 1$. $S_1 = 3$, $S_2 = 2$ — oba $\gt z$: <code>1</code>. $S_3 = 1 = z$: uz kapacitet $0$: $f(4) = 1$, $\Sigma(3) = 1$, $f(3) = 2$, $\Sigma(2) = 2$, $f(2) = 3$, $\Sigma(1) = 3$, $f(1) = 3 \ne 1$ — <code>0</code> (doista: $4$ glasa za $3$, a $2$ nužno glasa za $1$, pa i $1$ ima barem jedan glas — izjednačenje). $S_4 = 0$: <code>0</code>. Rezultat <code>1100</code>.</p>
<h3>6. Zamke</h3>
<ul>
<li>Rekurzivni DFS na lancu duljine $10^6$ probija stog; koristi svojstvo $P_u \lt u$ i petlje.</li>
<li>Za $S_x = z$ nije dovoljno provjeriti samo $e(x) = 1$ — cijeli put do korijena mora prenositi smanjenje, a korijen mora biti točno na $1$.</li>
<li>Zbrojevi $\Sigma$ mogu biti do $N$; <code>int</code> je dovoljan, ali oduzimanje $t$ mora biti predznačeno prije $\max(0, \cdot)$.</li>
<li>Binarno pretraživanje počinje od $t = 1$, ne $0$ (uz $N \ge 2$ netko mora dobiti glas), i $z - 1 \ge 0$ je valjan kapacitet za drugi prolaz.</li>
</ul>
''',
    'verified': r'''uzorak 1/1; 300 slučajnih testova ($N \le 8$, lanci i slučajna stabla) protiv brute forcea koji nabraja sva glasanja (svaki vrh bira bilo kojeg strogog pretka) i bilježi jedine pobjednike; 3 velika testa ($N = 10^6$: lanac, slučajno stablo, „duboko” stablo s $P_i \ge i - 3$).''',
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
    'coach': [
        (r'Postoji li uopće ulaz s odgovorom <code>NO</code>?',
         r'''<p>Ne — pokazat ćemo konstrukciju koja uvijek uspijeva, pa je odgovor uvijek <code>YES</code>. Ključ je da su diskovi disjunktni: između svaka dva „susjedna” diska postoji prazan prostor kroz koji se dužina može provući ne dodirujući ništa treće. Treba samo odabrati poredak u kojem se „susjedstvo” lako određuje.</p>'''),
        (r'Koji poredak diskova čini „tko je kome susjed” jednodimenzionalnim pitanjem?',
         r'''<p>Sweep vertikalnim pravcem $x = X$. Disk je <em>aktivan</em> dok pravac prolazi kroz njega ($x_i - r_i \le X \le x_i + r_i$); tada ga pravac siječe u tetivi sa središtem u $(X, y_i)$. Tetive aktivnih diskova su disjunktne (diskovi su), pa su na pravcu potpuno uređene, i to isto kao njihova središta po $y$: ako je tetiva $A$ ispod tetive $B$, onda je i $y_A \lt y_B$. Dakle skup aktivnih diskova, sortiran po $y_i$ u <code>std::set</code>, u svakom trenutku daje geometrijski poredak duž pravca.</p>'''),
        (r'Gdje nacrtati dužinu kad se novi disk pojavi, tako da sigurno ne dira ništa drugo?',
         r'''<p>Na samom pravcu $x = X$ ulaska: vertikalna dužina od $(X, y_u)$ do $(X, y_v)$ gdje su $u$ i $v$ susjedi u poretku aktivnih. Obje krajnje točke su unutar (ili na rubu) svojih diskova, a između tetiva $u$ i $v$ nema tetive trećeg aktivnog diska (susjedi su), dok neaktivni diskovi pravac uopće ne sijeku. Dužina dira točno dva diska. Dvije vertikalne dužine na istom $X$ spajaju različite susjedne parove pa dijele najviše krajnju točku; na različitim $X$ se ne mogu ni dodirnuti.</p>'''),
        (r'Što ostaje nespojeno i kako to spojiti bez presijecanja?',
         r'''<p>Svaki novi disk spoji se na barem jedan već aktivan disk, ako takav postoji; kad se pravac nađe u praznini (nijedan aktivan disk), počinje nova komponenta. Komponente su intervali unije $x$-projekcija diskova. Susjedne komponente spajamo dužinom od najdesnije točke lijeve komponente $(x_j + r_j, y_j)$ do najljevije točke desne $(x_k - r_k, y_k)$: ona prolazi kroz $x$-prazninu bez diskova i bez vertikalnih dužina, a krajnje točke dira samo s diskovima $j, k$ i eventualno kao zajednički kraj s vertikalnim dužinama na $x = x_k - r_k$. Brojanje: $n - (\text{broj komponenata}) + (\text{broj komponenata} - 1) = n - 1$.</p>'''),
        (r'Kako osigurati koordinate u $[0, 10^9]$ kad diskovi mogu stršati izvan tog kvadrata?',
         r'''<p>Koristimo samo apscise ulaska $\max(0, x_i - r_i)$ i ordinate središta $y_i$, sve u $[0, 10^9]$. Za disk koji strši lijevo od $0$ „ulazak” pomaknemo na $X = 0$: pravac $x = 0$ i dalje ga siječe. Spojnica komponenata počinje u $x_j + r_j$, što bi moglo biti $\gt 10^9$ — ali iza nje počinje druga komponenta u $x_k - r_k \le x_k \le 10^9$, pa je $x_j + r_j \lt x_k - r_k \le 10^9$ automatski.</p>'''),
    ],
    'tips': [
        r'''Kod konstruktivnih geometrijskih zadataka s disjunktnim objektima traži poredak u kojem se „susjed” definira jednodimenzionalno — sweep po jednoj koordinati uz uređeni skup aktivnih objekata.''',
        r'''Ključna lema sweepa: presjeci disjunktnih konveksnih likova s istim pravcem su disjunktni intervali čiji poredak odgovara poretku središta, i ne mijenja se dok su oba lika aktivna. Zato je <code>std::set</code> po fiksnom ključu (koordinata središta) ispravan.''',
        r'''Crtaj dužine <em>na</em> sweep-pravcu u trenutku događaja: točno tada znaš tko je aktivan i u kojem redoslijedu, a dužine na različitim pravcima se trivijalno ne sijeku.''',
        r'''Za konstruktivne zadatke napiši strogi checker (cjelobrojna geometrija bez decimalnih grešaka) — provjera „dira najviše dva diska” i „ne sijeku se” lako se propusti okom.''',
    ],
    'detailed': r'''
<h3>1. Rješenje uvijek postoji</h3>
<p>Konstrukcija u nastavku za svaki ulaz daje $n - 1$ valjanih dužina, pa nikad ne ispisujemo <code>NO</code>.</p>
<h3>2. Sweep i poredak aktivnih diskova</h3>
<p>Pomičemo vertikalni pravac $x = X$ slijeva nadesno. Disk $i$ je <em>aktivan</em> za $X \in [x_i - r_i,\, x_i + r_i]$; pravac ga siječe u tetivi $\{X\} \times [y_i - h, y_i + h]$, $h = \sqrt{r_i^2 - (X - x_i)^2} \ge 0$ (na rubovima tetiva je jedna točka — dodirna). Za $X \notin [x_i - r_i, x_i + r_i]$ pravac disk ne dira.</p>
<p><strong>Lema 1.</strong> Ako su diskovi $u \ne v$ oba aktivni za neki $X$, tetive su im disjunktne i $y_u \lt y_v$ ako i samo ako je tetiva $u$ ispod tetive $v$.<br>
<em>Dokaz.</em> Tetive su podskupovi disjunktnih diskova. Dva disjunktna intervala $[y_u - h_u, y_u + h_u]$ i $[y_v - h_v, y_v + h_v]$ imaju isti poredak kao njihova središta. $\square$</p>
<p>Zato aktivne diskove držimo u <code>std::set</code> sortiranom po $(y_i, i)$: u svakom trenutku redoslijed u skupu jednak je redoslijedu tetiva na pravcu, a susjedi u skupu su susjedne tetive bez ičega između.</p>
<p>Događaji: ulazak diska $i$ na $X_i^{\text{in}} = \max(0, x_i - r_i)$ i izlazak na $x_i + r_i$. Pomak ulaska na $0$ je dopušten jer je $x_i \ge 0$ i $r_i \ge 1$, pa pravac $x = 0$ siječe disk kad je $x_i - r_i \lt 0$. Na istoj apscisi obrađujemo <em>sve ulaske prije svih izlazaka</em>: disk koji izlazi na $X$ još dira pravac (u točki $(X, y_i)$) i mora se smatrati aktivnim da ga ne bismo prošli dužinom.</p>
<h3>3. Vertikalne dužine pri ulasku</h3>
<p>Na apscisi $X$ ubacimo sve nove diskove u skup. Zatim za svaki maksimalan niz uzastopnih (u poretku skupa) <em>novih</em> diskova $u_1 \lt u_2 \lt \dots \lt u_m$ (po $y$) nacrtamo dužine $(X, y_{u_j})$–$(X, y_{u_{j+1}})$ za $j \lt m$, te — ako je prije ovog $X$ skup bio neprazan — jednu dužinu do starog susjeda niza: do prethodnika $u_1$ u skupu ako postoji, inače do sljedbenika $u_m$ (barem jedan postoji jer ima starih diskova).</p>
<p><strong>Lema 2.</strong> Svaka takva dužina dira točno dva diska, a dvije dužine dijele najviše krajnju točku.<br>
<em>Dokaz.</em> Dužina spaja $(X, y_a)$ i $(X, y_b)$ za susjede $a, b$ u skupu; obje točke leže u tetivama (središta tetiva), dakle u diskovima $a, b$. Točke dužine strogo između tetiva $a$ i $b$ nisu ni u jednom aktivnom disku (Lema 1: treći aktivni disk bi imao tetivu između, pa bi bio između $a$ i $b$ u skupu), a neaktivni diskovi pravac ne diraju. Dužine na istom $X$ odgovaraju različitim susjednim parovima u linearnom poretku, pa se preklapaju samo u zajedničkom kraju; dužine na različitim apscisama leže na paralelnim pravcima. $\square$</p>
<p>Nakon obrade svi novi diskovi na $X$ su spojeni s nekim starim (ako je star postojao) ili međusobno (ako je skup bio prazan — tada su svi novi jedan niz). Broj dužina: $m$ po nizu sa starim susjedom, $m - 1$ ako je skup bio prazan.</p>
<h3>4. Spajanje komponenata</h3>
<p>Skup postaje prazan točno na krajevima maksimalnih intervala unije $x$-projekcija $[X_i^{\text{in}}, x_i + r_i]$. Diskovi jednog intervala čine jednu povezanu komponentu (indukcijom po ulascima). Neka komponenta $c-1$ završava u $X_{\text{end}} = \max (x_j + r_j)$ (disk $j$), a komponenta $c$ počinje u $X_{\text{start}} = x_k - r_k$ (neki disk $k$ koji ulazi tada; $X_{\text{start}} \gt X_{\text{end}} \gt 0$, pa nema pomaka na $0$). Nacrtamo dužinu $(x_j + r_j, y_j)$–$(x_k - r_k, y_k)$.</p>
<p><strong>Lema 3.</strong> Ta dužina dira samo diskove $j$ i $k$ i ne siječe druge dužine osim u zajedničkom kraju.<br>
<em>Dokaz.</em> Njezine točke imaju apscise u $[X_{\text{end}}, X_{\text{start}}]$. Za $X$ strogo unutra nijedan disk nije aktivan. Na $X_{\text{end}}$ dužina ima jedinu točku $(X_{\text{end}}, y_j)$; drugi disk $w$ koji dira pravac $x = X_{\text{end}}$ dira ga samo u $(X_{\text{end}}, y_w)$ (izlazi tada — inače bi bio aktivan i dalje, protivno maksimalnosti), a $y_w \ne y_j$ jer bi se inače diskovi dirali. Simetrično na $X_{\text{start}}$. Vertikalnih dužina na $x = X_{\text{end}}$ nema (nitko ne ulazi tada, jer bi tada bio aktivan poslije $X_{\text{end}}$), a one na $x = X_{\text{start}}$ prolaze kroz $(X_{\text{start}}, y_k)$ samo kao kroz svoju krajnju točku, što je dopušteno. $\square$</p>
<p>Uz $C$ komponenata sweep daje $n - C$ dužina, spojnice još $C - 1$: ukupno $n - 1$, graf disk–dužina je povezan.</p>
<h3>5. Koordinate</h3>
<p>Krajevi vertikalnih dužina su $(X_i^{\text{in}}, y_u)$ s $X_i^{\text{in}} \in [0, x_i] \subseteq [0, 10^9]$ i $y_u \in [0, 10^9]$. Spojnica ima apscise $x_j + r_j \lt x_k - r_k \le x_k \le 10^9$ i $x_k - r_k = X_{\text{start}} \gt 0$. Sve su koordinate cjelobrojne i u $[0, 10^9]$ — zato je izlaz uvijek valjan bez dodatnog „guranja” na $x = 0$ koje spominje službeni editorijal (mi ulaske odmah režemo na $0$).</p>
<h3>6. Algoritam i složenost</h3>
<ol>
<li>Napravi $2n$ događaja $(X, \text{tip}, i)$, tip $0$ = ulazak, $1$ = izlazak; sortiraj.</li>
<li>Prolazi po grupama iste apscise: ubaci nove, obradi nizove novih (Odjeljak 3), zatim izbaci izlaske i ažuriraj najdesniji disk tekuće komponente.</li>
<li>Spoji susjedne komponente (Odjeljak 4), ispiši.</li>
</ol>
<p>Sortiranje i operacije nad <code>std::set</code>-om: $O(n \log n)$; memorija $O(n)$. Izlaz od $2 \cdot 10^5$ redaka ispisujemo skupljanjem u jedan spremnik.</p>
<h3>7. Primjer</h3>
<p>Diskovi $(1,0,3), (10,10,6), (0,5,1)$. Ulasci: disk $1$ na $\max(0, -2) = 0$, disk $3$ na $0$, disk $2$ na $4$; izlasci: disk $3$ na $1$, disk $1$ na $4$, disk $2$ na $16$. Na $X = 0$ skup je prazan, novi $\{1, 3\}$ čine niz po $y$: dužina $(0,0)$–$(0,5)$. Na $X = 1$ izlazi disk $3$. Na $X = 4$ ulazi disk $2$ (tetiva je točka $(4, 10)$), stari susjed ispod je disk $1$ (tetiva točka $(4, 0)$, izlazi na $4$ ali je još aktivan): dužina $(4,0)$–$(4,10)$. Jedna komponenta, dvije dužine — drugačije od uzorka, ali valjano (checker prihvaća svaki valjan izlaz).</p>
<h3>8. Zamke</h3>
<ul>
<li>Ulasci prije izlazaka na istoj apscisi; inače dužina može proći kroz dodirnu točku diska koji „upravo izlazi”.</li>
<li>Vrijednosti do $2 \cdot 10^9$ ($x + r$) — 64-bitni tipovi za događaje.</li>
<li>Kad je skup prije $X$ bio prazan, ne crtati dužinu do „starog susjeda” — nema ga; tada niz od $m$ novih daje $m - 1$ dužina i počinje nova komponenta.</li>
<li>Najdesniji disk komponente nije nužno posljednji koji je ušao; ažurirati ga na svakom izlasku.</li>
</ul>
''',
    'verified': r'''uzorci 3/3 (checker); 300 slučajnih testova ($n \le 10$, guste konfiguracije diskova) provjereno checkerom koji egzaktnom cjelobrojnom geometrijom potvrđuje raspon koordinata, da svaka dužina dira najviše dva diska, da se dužine ne sijeku osim u zajedničkom kraju i da je graf povezan, plus dodatnih 1500 slučajnih testova; 3 velika testa ($n = 2 \cdot 10^5$: mreža, stupci s jednakim apscisama ulaska, jedan golemi disk i mnogo malih).''',
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
    'solution': r'''
<p>Promotrimo neku vrijednost razlike $d = j - i$. Treba $1 \le i \le p - 1 - 2d$. Dopustimo prvo cijeli raspon $1 \le i \lt p$, a zatim ćemo ukloniti doprinos svih $i$ za koje treba „omotavanje” ($p - 2d \le i \lt p$).</p>
<p>Neka je $g_i = i^{\frac{p-1}{2}}$ i $h_i = (g_i g_{i+d} + g_{i+d} g_{i+2d} + g_{i+2d} g_i + 1)/4$. Uočimo da je $h_i = 1$ ako je $w_i = w_{i+d} = w_{i+2d}$, a inače $h_i = 0$. Dakle broj trojki za dani $d$ je $\sum_{i=1}^{p-1} h_i$.</p>
<p>Vrijedi $\sum_{i=1}^{p-1} i^r \equiv 0 \pmod p$ za sve $1 \le r \lt p - 1$, te $\equiv p - 1 \pmod p$ za $r = p - 1$. Nadalje, $g_i g_{i+d} = (i(i+d))^{\frac{p-1}{2}} = i^{p-1} +$ (neka težinska suma nižih nenul potencija od $i$), pa je $\sum_{i=1}^{p-1} g_i g_{i+d} \equiv p - 1 \pmod p$.</p>
<p>Sada još treba ukloniti doprinos svih $1 \le i \lt p$, $1 \le d \le t$ s $i + 2d \ge p$. Formiramo novi niz $A$ duljine $4t$, gdje je $A_{2t-i} = g_{p-i}$ za $1 \le i \le 2t$ i $A_{2t+i} = g_i$ za $0 \le i \lt 2t$. U tom nizu treba naći zbroj $A_i A_{i+d} + A_{i+d} A_{i+2d} + A_{i+2d} A_i + 1$ po svim $i$ i $d$ koji zadovoljavaju $0 \le i \lt 2t$, $2t \le i + 2d \lt 4t$. To se može u $O(t)$ pomoću prefiksnih i sufiksnih zbrojeva pohranjenih zasebno za neparne i parne indekse.</p>
<p>Ukupna vremenska složenost je $O(t \log p)$, za računanje niza $A$.</p>
''',
    'coach': [
        (r'Kako uvjet „$w_i = w_j = w_k$” pretvoriti u algebru s kojom se može računati?',
         r'''<p>Znak $w_x$ je Legendreov simbol $g_x = \left(\frac{x}{p}\right) = x^{(p-1)/2} \bmod p \in \{-1, 1\}$ (uz $g_0 = 0$). Za tri vrijednosti $a, b, c \in \{\pm 1\}$ izraz $ab + bc + ca + 1$ jednak je $4$ ako su sve tri jednake, a $0$ inače. Dakle broj „monokromatskih” trojki s razlikom $d$ je $\frac14\sum_i (g_i g_{i+d} + g_{i+d} g_{i+2d} + g_{i+2d} g_i + 1)$ — zbroj umnožaka Legendreovih simbola, a o njima se puno zna.</p>'''),
        (r'Što znamo o $\sum_{i} \left(\frac{i}{p}\right)\left(\frac{i+d}{p}\right)$ po svim ostacima $i$?',
         r'''<p>Za $d \not\equiv 0$ taj je zbroj točno $-1$: za $i \ne 0$ vrijedi $\left(\frac{i(i+d)}{p}\right) = \left(\frac{i^2}{p}\right)\left(\frac{1 + d i^{-1}}{p}\right) = \left(\frac{1 + d i^{-1}}{p}\right)$, a $1 + d i^{-1}$ prolazi svim ostacima osim $1$; zbroj svih simbola je $0$, pa ostaje $-\left(\frac{1}{p}\right) = -1$. To omogućuje da se ciklički zbroj po svim $i = 1, \dots, p-1$ (indeksi modulo $p$) izračuna bez gledanja stringa: $4\cdot\text{total}_d = (p-1) - 1 - 1 - (1 + g_d g_{2d}) = p - 4 - g_d g_{2d}$.</p>'''),
        (r'Ciklički zbroj broji i „omotane” trojke; koliko ih je i gdje se nalaze?',
         r'''<p>Omotane su one s $i + 2d \ge p$, tj. $i \in [p - 2d, p - 1]$: za svaki $d$ točno $2d$ vrijednosti, ukupno $O(t^2)$ članova — previše za izravno brojanje, ali svi indeksi koji se pojavljuju leže u prozoru $g_{p-2t}, \dots, g_{p-1}, g_0, \dots, g_{2t}$ od $4t + 1$ vrijednosti. Uz $g_{p-i} = g_{-1}\, g_i$ i $g_{-1} = (-1)^{(p-1)/2}$ cijeli prozor računamo iz $g_1, \dots, g_{2t}$.</p>'''),
        (r'Kako dvostruku sumu po $(d, i)$ svesti na linearno vrijeme?',
         r'''<p>Svaki od tri umnoška $A_a A_{a+d}$, $A_{a+d}A_{a+2d}$, $A_a A_{a+2d}$ fiksiramo po većem indeksu: skup dopuštenih manjih indeksa je tada interval (za $A_a A_{a+2d}$ još i s uvjetom parnosti, jer $a \equiv a + 2d \pmod 2$). Intervalne zbrojeve daju prefiksne sume, odvojeno za parne i neparne indekse, pa je sve $O(t)$ po testu; jedini logaritam je računanje Legendreovih simbola Jacobijevim algoritmom, $O(t \log p)$.</p>'''),
    ],
    'tips': [
        r'''Indikator „sve tri vrijednosti $\pm1$ jednake” je $(ab + bc + ca + 1)/4$; općenito, zamjena indikatora polinomom u $\pm1$ varijablama pretvara brojanje u zbroj korelacija.''',
        r'''Zbroj $\sum_i \left(\frac{i(i+d)}{p}\right) = -1$ (za $p \nmid d$) standardna je činjenica o Legendreovom simbolu; pamti trik množenja s $\left(\frac{i^{-2}}{p}\right) = 1$.''',
        r'''Kad je „točan” odgovor razlika cikličke veličine (koja ima zatvorenu formulu) i lokalne korekcije (koja živi u malom prozoru), računaj samo prozor — ovdje $O(t)$ umjesto $O(p)$.''',
        r'''Dvostruke sume $\sum_{d}\sum_{a} A_a A_{a+d}$ pod linearnim ograničenjima na $(a, d)$ zamijeni sumom po jednom indeksu puta intervalna suma drugog; kad se u ograničenju pojavi $2d$, uvedi prefiksne sume po parnosti.''',
    ],
    'detailed': r'''
<h3>1. Legendreov simbol i indikator trojke</h3>
<p>Za prost $p \gt 2$ i $x \not\equiv 0$ Legendreov simbol $g_x = \left(\frac{x}{p}\right)$ je $1$ ako je $x$ kvadratni ostatak, inače $-1$; $g_0 = 0$. Po Eulerovu kriteriju $g_x \equiv x^{(p-1)/2} \pmod p$, i $g$ je potpuno multiplikativan: $g_{xy} = g_x g_y$. Dakle $w_x = 1 \iff g_x = 1$ za $1 \le x \le p-1$.</p>
<p>Za $a, b, c \in \{-1, 1\}$: ako su svi jednaki, $ab + bc + ca + 1 = 4$; ako su dva jednaka i treći različit, dva umnoška su $-1$ i jedan $1$, zbroj $0$. Zato je broj trojki s razlikom $d$</p>
<p style="text-align:center">$N_d = \dfrac14 \displaystyle\sum_{i=1}^{p-1-2d} \big(g_i g_{i+d} + g_{i+d} g_{i+2d} + g_{i+2d} g_i + 1\big),$</p>
<p>a odgovor je $\sum_{d=1}^{t} N_d$. Za $d \gt (p-2)/2$ nema trojki, pa smijemo staviti $t \leftarrow \min(t, \lfloor (p-2)/2 \rfloor)$.</p>
<h3>2. Ciklički zbroj ima zatvorenu formulu</h3>
<p><strong>Lema.</strong> Za $p \nmid d$: $\displaystyle\sum_{i=0}^{p-1} g_i g_{i+d} = -1$ (indeksi modulo $p$).<br>
<em>Dokaz.</em> Član $i = 0$ je $0$. Za $i \ne 0$, $g_i g_{i+d} = g_{i(i+d)} = g_{i^2}\, g_{1 + d i^{-1}} = g_{1 + d i^{-1}}$. Kad $i$ prolazi $1, \dots, p-1$, $d i^{-1}$ prolazi sve nenul ostatke, pa $1 + d i^{-1}$ prolazi sve ostatke osim $1$. Zbroj Legendreovih simbola po svim ostacima je $0$ (jednako kvadratnih ostataka i neostataka), pa je zbroj $0 - g_1 = -1$. $\square$</p>
<p>Definirajmo cikličku verziju $T_d = \sum_{i=1}^{p-1} (g_i g_{i+d} + g_{i+d} g_{i+2d} + g_{i+2d} g_i + 1)$ s indeksima modulo $p$. Po lemi $\sum_{i=1}^{p-1} g_i g_{i+d} = -1$ i $\sum_{i=1}^{p-1} g_i g_{i+2d} = -1$ ($2d \not\equiv 0$ jer $1 \le d \lt p/2$). Za srednji član supstituiramo $j = i + d$: $j$ prolazi sve ostatke osim $d$, pa $\sum_{i=1}^{p-1} g_{i+d} g_{i+2d} = \sum_{j} g_j g_{j+d} - g_d g_{2d} = -1 - g_d g_{2d}$. Konstanta daje $p - 1$. Ukupno</p>
<p style="text-align:center">$T_d = p - 4 - g_d\, g_{2d}.$</p>
<p>(Službeni editorijal zaokružuje na $(p-4)/4$; član $g_d g_{2d}$ je nužan da bi rezultat bio točan cijeli broj, što potvrđuje i brute force.)</p>
<h3>3. Korekcija za omotane trojke</h3>
<p>$4N_d = T_d - W_d$, gdje je $W_d$ zbroj istih članova za $i \in [p-2d, p-1]$ (točno oni $i$ za koje je $i + 2d \ge p$; pri tome neki indeks može biti $\equiv 0$, kad je $g = 0$, što je u redu jer $W_d$ jednostavno oduzima ono što je $T_d$ pribrojio). U $W_d$ se pojavljuju $g_x$ za $x \in [p - 2d, p + 2d - 1]$, dakle za sve $d \le t$ samo $g_{p-2t}, \dots, g_{p-1}, g_0, g_1, \dots, g_{2t}$. Definiramo prozor $A_{2t + k} = g_k$ za $-2t \le k \le 2t$ (indeksi $0 \ldots 4t$), pri čemu $g_{-k} = g_{p-k} = g_{-1} g_k$ i $g_{-1} = (-1)^{(p-1)/2}$ (Eulerov kriterij). Supstitucijom $a = i - (p - 2t)$:</p>
<p style="text-align:center">$W = \displaystyle\sum_{d=1}^{t}\ \sum_{a = 2t - 2d}^{2t - 1} \big(A_a A_{a+d} + A_{a+d} A_{a+2d} + A_{a+2d} A_a + 1\big).$</p>
<p>Konstantni dio je $\sum_d 2d = t(t+1)$. Preostala tri dvostruka zbroja imaju $O(t^2)$ članova, ali svaki se svodi na $O(t)$:</p>
<ul>
<li>$\sum A_a A_{a+2d}$: fiksiramo $b = a + 2d \in [2t, 4t-1]$; uvjeti $1 \le d \le t$, $a \le 2t - 1$ daju $a \in [\max(0, b - 2t),\ \min(2t-1, b-2)]$ s $a \equiv b \pmod 2$; doprinos $A_b \cdot (\text{zbroj } A_a \text{ po tom intervalu iste parnosti})$.</li>
<li>$\sum A_{a+d} A_{a+2d}$: fiksiramo $b = a + 2d$ i $c = a + d$, tj. $a = 2c - b$, $d = b - c$; uvjeti $a \in [0, 2t-1]$ i $d \in [1, t]$ daju interval za $c$: $\max(b - t, \lceil b/2 \rceil) \le c \le \min(b - 1, \lfloor (b + 2t - 1)/2 \rfloor)$.</li>
<li>$\sum A_a A_{a+d}$: fiksiramo $c = a + d \in [1, 4t-1]$; uvjeti $d \in [1, t]$, $a \le 2t - 1$ i $a \ge 2t - 2d = 2t - 2(c - a) \iff a \le 2c - 2t$ daju $a \in [\max(0, c - t),\ \min(2t-1, c-1, 2c-2t)]$.</li>
</ul>
<p>Intervalne zbrojeve dobivamo iz prefiksnih suma prozora, odvojeno po parnosti indeksa (za prvi slučaj) ili ukupno. Konačno $\text{odgovor} = \frac14\left(\sum_{d=1}^{t} T_d - W\right)$; dijeljenje je egzaktno.</p>
<h3>4. Računanje Legendreovih simbola</h3>
<p>Trebamo $g_1, \dots, g_{2t}$ za $p$ do $10^{12}$. Eulerov kriterij traži modularno potenciranje 128-bitnim međurezultatima; jednostavnije je Jacobijev simbol $\left(\frac{a}{n}\right)$ algoritmom nalik Euklidovu (zakon kvadratnog reciprociteta i $\left(\frac{2}{n}\right) = (-1)^{(n^2-1)/8}$), koji radi u 64-bitnoj aritmetici u $O(\log p)$ koraka; za prost $n$ Jacobijev simbol jednak je Legendreovu.</p>
<h3>5. Složenost i veličine</h3>
<p>Po testu $O(t \log p)$ za simbole i $O(t)$ za sve zbrojeve; uz $\sum t \le 10^6$ i $T \le 5 \cdot 10^5$ ukupno je to nekoliko desetaka milijuna operacija. Odgovor je najviše $\sum_d (p - 1 - 2d) \lt t p \le 10^{18}$, a međuvrijednost $\sum T_d \lt t p$ također, pa <code>long long</code> dostaje (ali <code>int</code> ne, ni za $p$).</p>
<h3>6. Primjer</h3>
<p>$p = 13$: kvadratni ostaci su $\{1, 3, 4, 9, 10, 12\}$, $w = 101100001101$. Za $d = 1$: $T_1 = 13 - 4 - g_1 g_2 = 9 - (1)(-1) = 10$. Omotani $i \in \{11, 12\}$: $i = 11$ daje $(g_{11}, g_{12}, g_0) = (-1, 1, 0)$, član $-1 + 0 + 0 + 1 = 0$; $i = 12$ daje $(g_{12}, g_0, g_1) = (1, 0, 1)$, član $0 + 0 + 1 + 1 = 2$. $W_1 = 2$, $N_1 = (10 - 2)/4 = 2$ — trojke $(5,6,7)$ i $(6,7,8)$. Za $t = 2$ treba još $N_2 = 0$ (nema trojki s razlikom $2$), pa je odgovor opet $2$.</p>
<h3>7. Zamke</h3>
<ul>
<li>Ne zaboraviti član $g_d g_{2d}$ u $T_d$ i ograničiti $t$ na $\lfloor (p-2)/2 \rfloor$ (npr. $p = 7$, $t = 32$).</li>
<li>Prozor mora sadržavati i $A_{4t} = g_{2t}$: u $W$ indeksi idu do $4t - 1$, ali $g_{2d}$ za $d = t$ treba u $T_d$.</li>
<li>Parnost u zbroju $A_a A_{a+2d}$ — bez razdvajanja prefiksnih suma po parnosti rezultat je pogrešan.</li>
<li>$g_{-1}$ ovisi o $p \bmod 4$; prozor lijevo od središta množi se tim predznakom.</li>
<li>Puno testova ($5 \cdot 10^5$): alocirati $O(t)$ po testu, ništa ovisno o $p$.</li>
</ul>
''',
    'verified': r'''uzorak 1/1; 300 slučajnih testova (prosti $p \lt 400$, $t$ do $2p$) protiv brute forcea koji izravno gradi $w$ iz kvadratnih ostataka i broji trojke u $O(p^2)$; 3 velika testa ($\sum t = 10^6$: jedan test s $p \approx 10^{12}$ i $t = 10^6$, odnosno $T = 5 \cdot 10^5$ testova s $t = 2$).''',
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
    'solution': r'''
<p>Promotrimo brojeve oblika $d \times (a_0 + a_1 \times 2^6 + a_2 \times 2^{12})$, gdje je svaki $a_i$ jednak $0$ ili $1$. To su brojevi kojima su bitovi $0 \dots 5$ jednaki ili $0$ ili $d$; isto tako bitovi $6 \dots 11$ jednaki su ili $0$ ili $d$, a isto vrijedi i za bitove $12 \dots 17$.</p>
<p>Za izbore $a_0, a_1, a_2$ postoji $8$ takvih brojeva, a za svaku kockicu možemo odabrati bilo kojih $6$ od njih.</p>
''',
    'coach': [
        (r'Zašto je XOR „nezgodan” za djeljivost i kako ga možemo ukrotiti?',
         r'''<p>Djeljivost s $d$ svojstvo je zbroja s prijenosom, a XOR nema prijenosa među bitovima — općenito XOR dvaju višekratnika od $d$ nije višekratnik od $d$ (npr. $3 \oplus 6 = 5$). Nema smisla tražiti proizvoljne višekratnike; tražimo <em>podskup</em> višekratnika od $d$ koji je <strong>zatvoren na XOR</strong>. Ako svaka strana svake kockice pripada takvom skupu, XOR bilo kojeg izbora strana opet je u skupu, dakle djeljiv s $d$.</p>'''),
        (r'Koji skup višekratnika od $d$ je zatvoren na XOR?',
         r'''<p>Bitovi ne međudjeluju u XOR-u, pa razmišljamo po disjunktnim blokovima bitova. Kako je $d \le 60 \lt 64 = 2^6$, zapis od $d$ stane u $6$ bitova. Uzmimo brojeve kojima je svaki od blokova bitova $[0,5]$, $[6,11]$, $[12,17]$ ili sav $0$ ili točno kopija od $d$: to su $d\,(a_0 + a_1 2^6 + a_2 2^{12})$ uz $a_i \in \{0,1\}$. XOR više takvih brojeva računa se blok po blok, a u bloku XOR-amo kopije od $d$ i nule: rezultat je $d$ (neparno kopija) ili $0$. Rezultat je opet istog oblika, a svaki takav broj je $d$ puta cijeli broj.</p>'''),
        (r'Ima li dovoljno takvih brojeva i staju li u ograničenja?',
         r'''<p>Trojki $(a_0, a_1, a_2)$ ima $2^3 = 8$, a treba $6$ različitih po kockici — dovoljno (zato tri bloka, a ne dva: s dva bloka imali bismo samo $4$ broja). Najveći je $d(1 + 64 + 4096) = 4161 d \le 249\,660 \le 10^6$. Sve kockice mogu biti jednake; ispis je $O(n)$.</p>'''),
    ],
    'tips': [
        r'''Kad kombiniraš XOR i djeljivost (ili zbroj i XOR), traži skup <em>zatvoren</em> na operaciju: podijeli bitove u disjunktne blokove tako da se svaki blok ponaša neovisno, i u svaki blok upiši samo $0$ ili jednu fiksnu vrijednost.''',
        r'''Provjeri veličinu skupa koji konstruiraš prije nego ga fiksiraš: ovdje treba $\ge 6$ elemenata, pa su nužna barem $3$ bloka ($2^3 = 8$), ali i gornja granica $10^6$ ograničava broj blokova.''',
        r'''Za konstruktivne zadatke napiši checker koji iscrpno računa skup svih mogućih ishoda (ovdje skup svih dostižnih XOR-ova po kockicama) — to je jedina prava provjera tvrdnje „za svaki ishod”.''',
    ],
    'detailed': r'''
<h3>1. Preformulacija: skup zatvoren na XOR</h3>
<p>Traži se $n$ kockica, svaka sa $6$ različitih oznaka $\le 10^6$, tako da je XOR gornjih strana <em>uvijek</em> djeljiv s $d$. Uvjet „uvijek” sugerira sljedeći pristup: nađimo skup $V$ nenegativnih cijelih brojeva sa svojstvima</p>
<ol>
<li>svaki $v \in V$ djeljiv je s $d$,</li>
<li>$V$ je zatvoren na XOR: $u, v \in V \Rightarrow u \oplus v \in V$,</li>
<li>$|V| \ge 6$ i $\max V \le 10^6$.</li>
</ol>
<p>Ako svaka strana svake kockice nosi element iz $V$, onda je XOR bilo kojeg izbora $n$ strana (indukcijom po $n$, po svojstvu 2) element od $V$, dakle djeljiv s $d$. Time je zadatak sveden na konstrukciju jednog takvog skupa $V$; sve kockice mogu biti identične.</p>
<h3>2. Zašto blokovi bitova</h3>
<p>XOR djeluje na svaki bit neovisno. Ako pozicije bitova podijelimo u disjunktne blokove $B_0 = [0,5]$, $B_1 = [6,11]$, $B_2 = [12,17]$, onda je XOR dvaju brojeva „XOR po blokovima”: blok $B_j$ rezultata ovisi samo o blokovima $B_j$ operanada. Skup brojeva čiji je svaki blok iz nekog malog skupa $W$ zatvoren je na XOR ako je $W$ zatvoren na XOR. Najjednostavniji netrivijalni $W$ je $\{0, d\}$: $0 \oplus 0 = 0$, $0 \oplus d = d$, $d \oplus d = 0$. Da bi $d$ „stao” u blok od $6$ bitova treba $d \lt 2^6 = 64$, što vrijedi jer je $d \le 60$.</p>
<p>Dakle $V = \{\, d\,(a_0 + a_1 2^6 + a_2 2^{12}) : a_0, a_1, a_2 \in \{0, 1\} \,\}$. Broj $d\,(a_0 + a_1 2^6 + a_2 2^{12}) = a_0 d + a_1 (d \cdot 2^6) + a_2 (d \cdot 2^{12})$ upravo ima u bloku $B_j$ zapis od $d$ ako je $a_j = 1$, a nule inače — pribrojnici se ne preklapaju jer $d \lt 2^6$.</p>
<h3>3. Dokaz svojstava</h3>
<ul>
<li><em>Djeljivost.</em> Svaki element je $d$ puta cijeli broj $a_0 + 64a_1 + 4096a_2$.</li>
<li><em>Zatvorenost.</em> Za $u = d\sum a_j 2^{6j}$ i $v = d\sum b_j 2^{6j}$ blok $B_j$ od $u \oplus v$ jednak je XOR-u blokova $B_j$ od $u$ i $v$, tj. $d$ ako je točno jedan od $a_j, b_j$ jednak $1$, a $0$ inače. Dakle $u \oplus v = d\sum (a_j \oplus b_j) 2^{6j} \in V$.</li>
<li><em>Veličina i raspon.</em> $|V| = 2^3 = 8 \ge 6$ (elementi su različiti jer su trojke $(a_0,a_1,a_2)$ različite, a $d \ne 0$). Najveći element je $d(1 + 64 + 4096) = 4161\,d \le 4161 \cdot 60 = 249\,660 \le 10^6$.</li>
</ul>
<p>Zašto ne dva bloka? Tada bi $|V| = 4 \lt 6$. Zašto ne četiri? Ne treba, a $d \cdot 2^{18} \gt 10^6$ za $d \ge 4$ bi probio ograničenje.</p>
<h3>4. Algoritam i primjer</h3>
<p>Generiramo $8$ brojeva $v_m = \bigoplus_{j : m_j = 1} (d \ll 6j)$ za $m = 0, \dots, 7$ i svakoj od $n$ kockica ispišemo prvih $6$. Za $d = 2$: $V = \{0, 2, 128, 130, 8192, 8194, 8320, 8322\}$; npr. $2 \oplus 128 \oplus 8194 = 8320$, djeljivo s $2$. Složenost $O(n)$.</p>
<h3>5. Zamke</h3>
<p>Brojevi na kockici moraju biti <em>različiti</em> — ne smijemo ispisati šest nula. Provjera zadatka „za svaki ishod” ne može se testirati simulacijom bacanja; ispravna provjera računa skup svih dostižnih XOR-ova dinamikom po kockicama (skup nakon $i$ kockica $= \{x \oplus s\}$ po svim $x$ iz prethodnog skupa i stranama $s$), što je i naš checker.</p>
''',
    'verified': r'''uzorak 1/1 (checker); 300 slučajnih testova ($n \le 6$, $2 \le d \le 60$) provjereno checkerom koji zahtijeva $6$ različitih brojeva u $[0, 10^6]$ po kockici i iscrpno računa skup svih dostižnih XOR-ova (svi moraju biti djeljivi s $d$); 3 velika testa ($n = 100$).''',
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
    'solution': r'''
<p>Sve sljedeće tvrdnje dokazuju se indukcijom. Neka je $k$ broj hrpa koje sadrže više od jednog kamenčića.</p>
<ul>
<li>Ako je $k \ge 2$, prvi igrač gubi.</li>
<li>Ako je $k = 1$, prvi igrač pobjeđuje ako i samo ako $N \not\equiv 2 \pmod 3$.</li>
<li>Ako je $k = 0$, prvi igrač pobjeđuje ako i samo ako $N \equiv 1 \pmod 3$.</li>
<li>Ako je na potezu drugi igrač, on gubi ako i samo ako sve hrpe imaju po jedan kamenčić i $N \equiv 0 \pmod 3$.</li>
</ul>
''',
    'coach': [
        (r'Koji je najjednostavniji netrivijalni slučaj kojim možemo početi?',
         r'''<p>Sve hrpe imaju po jedan kamenčić. Tada nema izbora: Sprague uzima jedan kamenčić, Grundy dva (ili jedan, ako je to sve što ostaje). U jednom krugu nestaju $3$ kamenčića, pa ishod ovisi samo o $N \bmod 3$: $N = 1$ — Sprague uzima posljednji; $N = 2, 3$ — Grundy uzima ostatak; $N = 4$ — nakon $1 + 2$ ostaje $1$ za Spraguea. Dakle Sprague (na potezu) pobjeđuje ako i samo ako $N \equiv 1 \pmod 3$, a Grundy (na potezu) gubi ako i samo ako $N \equiv 0 \pmod 3$.</p>'''),
        (r'Koja veličina razlikuje „prisiljene” pozicije od onih s izborom?',
         r'''<p>Broj $k$ hrpa s više od jednog kamenčića. Dok je $k \ge 1$, igrač na potezu ima izbor koliko kamenčića ostaviti u velikoj hrpi, dakle može <em>birati</em> u koji razred (po $N \bmod 3$) pozicije s jedinicama ubaciti protivnika. Jedan potez smanjuje $k$ za najviše $1$; Grundy u svom redu ima dva poteza, Sprague samo jedan. To je asimetrija koja odlučuje igru.</p>'''),
        (r'Što Sprague može napraviti kad je $k = 1$, a što kad je $k \ge 2$?',
         r'''<p>Za $k = 1$ Sprague veliku hrpu spusti na $1$ (Grundy dobiva $N$ jedinica) ili na $0$ (Grundy dobiva $N-1$ jedinica). Grundy gubi točno kad je broj jedinica djeljiv s $3$, pa Sprague pobjeđuje ako je $N \equiv 0$ ili $N \equiv 1 \pmod 3$, tj. $N \not\equiv 2$. Za $N \equiv 2$ ne pomaže ni ostavljanje velike hrpe (Grundy tada ima $k \ge 1$ i pobjeđuje, vidi sljedeći korak). Za $k \ge 2$ nakon Spragueova poteza ostaje $k \ge 1$, pa Grundy uvijek pobjeđuje.</p>'''),
        (r'Zašto Grundy pobjeđuje uvijek kad na potezu ima barem jednu veliku hrpu?',
         r'''<p>Jer s dva poteza može pogoditi bilo koji od razreda koje Sprague gubi. Ako je $k \ge 3$, dva poteza ne mogu $k$ spustiti ispod $1$, a Grundy lako ostavi $k \ge 2$ (npr. smanjuje velike hrpe za po jedan kamenčić; ako time nastane jedinica, drugim potezom uzme jednu jedinicu). Ako je $k = 2$ s $m$ jedinica, Grundy obje velike hrpe spusti na $0$ ili $1$ i tako Spragueu preda $m$, $m+1$ ili $m+2$ jedinica — barem jedan od tih brojeva nije $\equiv 1 \pmod 3$. Ako je $k = 1$ s $m \ge 1$ jedinica, Grundy velikom hrpom i jednom jedinicom napravi $m$ ($m \equiv 0, 2$) ili $m - 1$ ($m \equiv 1$) jedinica; za $m = 0$ hrpu spusti na $1$ pa je uzme i pobijedi odmah.</p>'''),
        (r'Kako sve tvrdnje složiti u dokaz?',
         r'''<p>Indukcijom po ukupnom broju kamenčića dokazujemo istodobno: (S1) Sprague na potezu, $k \ge 2$: gubi; (S2) $k = 1$: pobjeđuje ako i samo ako $N \not\equiv 2$; (S3) $k = 0$: pobjeđuje ako i samo ako $N \equiv 1$; (G) Grundy na potezu gubi ako i samo ako $k = 0$ i $N \equiv 0 \pmod 3$. Svaka tvrdnja provjerava se tako da se pokaže postojanje poteza u protivnikovu gubitničku poziciju, odnosno da svi potezi vode u protivnikovu pobjedničku poziciju (koje su „manje” pa za njih tvrdnje već vrijede).</p>'''),
    ],
    'tips': [
        r'''U igrama s nestandardnim pravilima poteza ne posezi odmah za Sprague–Grundyjevom teorijom (ovdje se ne primjenjuje jer igrači nemaju iste poteze); umjesto toga nađi malu „normalnu formu” pozicija (ovdje: broj velikih hrpa i $N \bmod 3$) i dokaži tvrdnje indukcijom.''',
        r'''Uvijek prvo riješi prisiljene pozicije (sve hrpe po $1$) — one su baza indukcije, a ostatak analize svodi se na pitanje „tko može birati u koji razred prisiljene pozicije ubaciti protivnika”.''',
        r'''Napiši brute force koji pretražuje cijelo stablo igre za male ulaze i usporedi s hipotezom; ovdje je upravo takav test otkrio pogrešno napisan uvjet za $k = 1$.''',
    ],
    'detailed': r'''
<h3>1. Oznake</h3>
<p>Neka je $N$ broj (nepraznih) hrpa, a $k$ broj hrpa s barem $2$ kamenčića („velike” hrpe); ostalih $N - k$ hrpa su „jedinice”. Sprague u svom redu radi jedan potez, Grundy dva (drugi samo ako je nakon prvog ostao barem jedan kamenčić). Tko uzme posljednji kamenčić pobjeđuje; ekvivalentno, igrač koji je na potezu bez kamenčića je izgubio.</p>
<h3>2. Prisiljene pozicije: sve hrpe su jedinice</h3>
<p>Ako je $k = 0$, svaki potez uzima točno jednu hrpu. Sprague uzme jednu, Grundy dvije (ili jednu ako je ostala samo jedna). Označimo $N \bmod 3$:</p>
<ul>
<li>Sprague na potezu: $N = 1$ pobjeđuje; $N = 2$ ili $3$ gubi (Grundy uzme sve ostalo); $N = 4$ pobjeđuje ($4 \to 3 \to 1$). Općenito jedan puni krug uklanja $3$ hrpe, pa Sprague pobjeđuje <strong>ako i samo ako $N \equiv 1 \pmod 3$</strong>.</li>
<li>Grundy na potezu: $N = 0$ već je izgubio; $N = 1, 2$ pobjeđuje odmah; $N = 3$ ostavlja $1$ Spragueu i gubi. Općenito Grundy gubi <strong>ako i samo ako $N \equiv 0 \pmod 3$</strong>.</li>
</ul>
<h3>3. Tvrdnje</h3>
<p>Dokazujemo indukcijom po ukupnom broju kamenčića (pozicije nakon poteza imaju strogo manje kamenčića):</p>
<ul>
<li><strong>(S1)</strong> Sprague na potezu, $k \ge 2$: Sprague gubi.</li>
<li><strong>(S2)</strong> Sprague na potezu, $k = 1$: Sprague pobjeđuje ako i samo ako $N \not\equiv 2 \pmod 3$.</li>
<li><strong>(S3)</strong> Sprague na potezu, $k = 0$: Sprague pobjeđuje ako i samo ako $N \equiv 1 \pmod 3$.</li>
<li><strong>(G)</strong> Grundy na potezu (početak njegova reda): Grundy gubi ako i samo ako $k = 0$ i $N \equiv 0 \pmod 3$.</li>
</ul>
<p>Skup Spragueovih gubitničkih pozicija je dakle $\mathcal{L}_S = \{k \ge 2\} \cup \{k = 1, N \equiv 2\} \cup \{k = 0, N \not\equiv 1\}$.</p>
<h3>4. Dokaz tvrdnje (G)</h3>
<p><em>Slučaj $k = 0$.</em> Riješen u odjeljku 2 (potezi su prisiljeni, a rezultat je konzistentan sa (S3): nakon Grundyjeva reda Sprague dobiva $N - 2$ jedinica, a $N \equiv 0 \Rightarrow N - 2 \equiv 1$, Sprague pobjeđuje; $N \equiv 1, 2 \Rightarrow N - 2 \equiv 2, 0$, Sprague gubi).</p>
<p><em>Slučaj $k = 1$</em>, velika hrpa $a \ge 2$ i $m = N - 1$ jedinica. Ako je $m = 0$, Grundy spusti $a$ na $1$ pa drugim potezom uzme posljednji kamenčić — pobjeda. Ako je $m \ge 1$: za $m \equiv 0$ ili $2 \pmod 3$ Grundy spusti $a$ na $1$ i uzme jednu jedinicu; Sprague dobiva $k = 0$ s $m$ jedinica, $m \not\equiv 1$, pa po (S3) gubi. Za $m \equiv 1$ Grundy uzme cijelu hrpu $a$ i jednu jedinicu; Sprague dobiva $m - 1 \equiv 0$ jedinica i gubi.</p>
<p><em>Slučaj $k = 2$</em>, velike hrpe $a, b$ i $m$ jedinica. Grundy prvim potezom spusti $a$ na $0$ ili $1$ (kamenčića još ima jer je $b \ge 2$), a drugim $b$ na $0$ ili $1$. Sprague dobiva $k = 0$ i $m$, $m+1$ ili $m+2$ jedinica; od tri uzastopna broja barem dva nisu $\equiv 1 \pmod 3$, pa Grundy bira jedan od njih i Sprague po (S3) gubi.</p>
<p><em>Slučaj $k \ge 3$.</em> Grundy prvim potezom smanji neku veliku hrpu za jedan kamenčić: $k$ ostaje isti ili (ako je hrpa imala $2$) padne na $k - 1 \ge 2$ uz novu jedinicu. Drugim potezom: ako je $k$ i dalje $\ge 3$, opet smanji neku veliku hrpu za $1$; ako je $k = 2$, uzme tu novonastalu jedinicu. U oba slučaja Sprague dobiva $k \ge 2$ i po (S1) gubi.</p>
<h3>5. Dokaz tvrdnji (S1)–(S3)</h3>
<p><em>(S1)</em> Spragueov jedan potez smanjuje $k$ za najviše $1$, pa Grundy dobiva $k \ge 1$ i po (G) pobjeđuje.</p>
<p><em>(S2)</em> Sprague može: (a) spustiti veliku hrpu na $1$ — Grundy dobiva $k = 0$ s $N$ jedinica; (b) uzeti je cijelu — $k = 0$ s $N - 1$ jedinica; (c) ostaviti je velikom ili uzeti jedinicu — Grundy dobiva $k = 1$ i po (G) pobjeđuje. Po (G) Sprague pobjeđuje ako i samo ako je $N \equiv 0$ ili $N - 1 \equiv 0 \pmod 3$, tj. $N \not\equiv 2$.</p>
<p><em>(S3)</em> Jedini potez uzima jedinicu; Grundy dobiva $N - 1$ jedinica i gubi ako i samo ako $N - 1 \equiv 0$, tj. $N \equiv 1 \pmod 3$.</p>
<h3>6. Algoritam, složenost, zamke</h3>
<p>Za svaki test prebrojimo hrpe s $A_i \gt 1$ i primijenimo (S1)–(S3): $O(N)$ po testu, ukupno $O(\sum N)$. Primjeri: $(1, 2)$ — $k = 1$, $N = 2 \equiv 2$: <code>Grundy</code>; $(5)$ — $k = 1$, $N = 1$: <code>Sprague</code>; $(1, 7, 2, 9)$ — $k = 3$: <code>Grundy</code>. Vrijednosti $A_i \le 10^9$ ne utječu (važno je samo je li $A_i \gt 1$), ali ih treba čitati u 32-bitni ili širi tip. Klasična zamka je pogrešan uvjet za $k = 1$ (npr. $N \equiv 1$ umjesto $N \not\equiv 2$) — brute force po stablu igre to odmah otkriva.</p>
''',
    'verified': r'''uzorak 1/1; 300 slučajnih testova ($N \le 6$, $A_i \le 4$) protiv brute forcea koji memoizacijom pretražuje cijelo stablo igre (stanje = sortirane hrpe, tko je na potezu, je li Grundyjev drugi potez); 3 velika testa ($N = 10^5$).''',
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
    'solution': r'''
<p>Svaki podgraf treba barem $N - 1$ bridova, pa je $K \le \frac{N}{2}$. Taj je uvjet i dovoljan. Konstruirat ćemo rješenje za $K = \lfloor N/2 \rfloor$; ako je $K \lt \lfloor N/2 \rfloor$, sve bridove boje $\ge K$ prebojimo u boju $0$ (boje indeksiramo od $0$).</p>
<p>Pretpostavimo prvo da je $N$ paran. Za svaki $0 \le k \lt \frac N2$ neka vrhovi $2k, 2k+1$ budu vrhovi boje $k$; brid $(2k, 2k+1)$ obojimo bojom $k$. Za svaki $0 \le i \lt j \lt K$ bridove $(2i, 2j)$ i $(2i+1, 2j+1)$ obojimo bojom $i$, a bridove $(2i, 2j+1)$ i $(2i+1, 2j)$ bojom $j$.</p>
<p>Za svaki $j \ne i$ vrh $2j$ susjedan je (u boji $i$) s $2i$ ili $2i+1$; isto vrijedi za vrh $2j+1$, pa je dijametar svake boje $i$ najviše $3$.</p>
<p>Za neparni $N$ prvo napravimo rješenje za $N - 1$, a zatim za svaki $i \lt N-1$ brid $(i, N-1)$ obojimo bojom $\lfloor i/2 \rfloor$.</p>
''',
    'coach': [
        (r'Što uvjet „dijametar $\le 4$” zapravo govori o grafu jedne boje?',
         r'''<p>Da je konačan, dakle da je graf boje $j$ <em>povezan na svih $N$ vrhova</em> (udaljenost nepovezanih vrhova je $\infty$). Povezan graf na $N$ vrhova ima barem $N - 1$ bridova. Kako svaki od $\binom N2$ bridova ima točno jednu boju, mora biti $K(N-1) \le \frac{N(N-1)}{2}$, tj. $K \le N/2$. Za $K \gt \lfloor N/2 \rfloor$ odgovor je <code>NO</code>.</p>'''),
        (r'Zašto je dovoljno riješiti samo najteži slučaj $K = \lfloor N/2 \rfloor$?',
         r'''<p>Ako imamo bojanje s $K_0 = \lfloor N/2 \rfloor$ boja, za manji $K$ sve bridove boja $K, \dots, K_0 - 1$ (0-indeksirano) prebojimo u boju $0$. Graf boje $0$ time samo dobiva bridove, a dodavanje bridova ne povećava nijednu udaljenost, pa dijametar ostaje $\le 4$; ostale boje se ne mijenjaju.</p>'''),
        (r'Kako podijeliti $\binom N2$ bridova na $N/2$ povezanih grafova malog dijametra?',
         r'''<p>Svaka boja mora imati približno $N - 1$ bridova — praktički razapinjuće stablo. Graf malog dijametra s malo bridova je „zvijezda” ili „dvostruka zvijezda”: svakoj boji $i$ dodijelimo par <em>predstavnika</em> $2i, 2i+1$ spojenih bridom boje $i$, a svaki drugi vrh spojimo bojom $i$ s <em>jednim</em> od njih. Tada je svaki vrh na udaljenosti $\le 1$ od predstavnika, a predstavnici su susjedni: dijametar $\le 3$.</p>'''),
        (r'Kako osigurati da svaki brid dobije točno jednu boju?',
         r'''<p>Brid između para $i$ i para $j$ ($i \lt j$) mora pripasti boji $i$ ili $j$, i to tako da svaki vrh para $j$ dobije točno jedan brid boje $i$ prema paru $i$, i obrnuto. Četiri brida između parova podijelimo na „paralelne” $(2i,2j), (2i+1,2j+1)$ — boja $i$ — i „ukrižene” $(2i,2j+1), (2i+1,2j)$ — boja $j$. Vrh $2j$ ima tada brid boje $i$ do $2i$, vrh $2j+1$ do $2i+1$; vrh $2i$ ima brid boje $j$ do $2j+1$, a $2i+1$ do $2j$. Za neparni $N$ zadnji vrh spojimo s vrhom $v$ bojom $\lfloor v/2 \rfloor$: susjedan je s oba predstavnika svake boje.</p>'''),
    ],
    'tips': [
        r'''Kod „podijeli sve bridove potpunog grafa na $K$ podgrafa sa svojstvom X” prvo prebroj: koliko bridova svaki podgraf <em>mora</em> imati (ovdje $\ge N-1$ zbog povezanosti) — to daje gornju granicu na $K$, a konstrukcija je onda obično najgušća moguća i simetrična.''',
        r'''Graf s $\approx N$ bridova i malim dijametrom gotovo uvijek je zvijezda ili dvostruka zvijezda; kad tražiš takve podgrafove, biraj „središta” (predstavnike) za svaku boju.''',
        r'''Kad je uvjet monoton na dodavanje bridova (dijametar ne raste), riješi ekstremni $K$ i manje $K$ dobij spajanjem boja.''',
        r'''Checker za konstruktivni izlaz neka ponovno provjeri svojstvo iz teksta (ovdje BFS po svakoj boji), a ne samo format.''',
    ],
    'detailed': r'''
<h3>1. Nužan uvjet: $K \le \lfloor N/2 \rfloor$</h3>
<p>Za boju $j$ promatramo graf $G_j$ na svih $N$ vrhova s bridovima boje $j$. Uvjet $d_j \le 4$ posebno znači da je $d_j$ konačan, tj. da je $G_j$ povezan. Povezan graf na $N$ vrhova ima barem $N-1$ bridova (razapinjuće stablo). Svaki brid potpunog grafa ima točno jednu boju, pa zbrajanjem po bojama dobivamo $K(N-1) \le \binom N2 = \frac{N(N-1)}{2}$, odakle $K \le \frac N2$. Kako je $K$ cijeli broj, $K \le \lfloor N/2 \rfloor$. U primjeru $N = 5$, $K = 10$: $10 \gt 2$, odgovor <code>NO</code>.</p>
<h3>2. Redukcija na $K = \lfloor N/2 \rfloor$</h3>
<p>Pretpostavimo da imamo valjano bojanje s $K_0 = \lfloor N/2 \rfloor$ boja $0, \dots, K_0 - 1$ i da je zadani $K \lt K_0$. Sve bridove boja $\ge K$ prebojimo u boju $0$. Grafovi boja $1, \dots, K-1$ ostaju isti. Graf boje $0$ dobiva nove bridove; udaljenost između dva vrha je duljina najkraćeg puta, a dodavanjem bridova skup puteva samo raste, pa se nijedna udaljenost ne povećava i dijametar ostaje $\le 4$. Dakle dovoljno je konstruirati bojanje za $K_0$.</p>
<h3>3. Konstrukcija za parni $N$</h3>
<p>Neka je $N = 2K_0$. Vrhove indeksiramo $0, \dots, N-1$ i grupiramo u parove $P_k = \{2k, 2k+1\}$, $0 \le k \lt K_0$; vrhove para $P_k$ zovemo <em>predstavnicima</em> boje $k$. Bojanje:</p>
<ul>
<li>brid unutar para, $(2k, 2k+1)$, ima boju $k$;</li>
<li>za $i \lt j$, od četiri brida između $P_i$ i $P_j$ „paralelni” bridovi $(2i, 2j)$ i $(2i+1, 2j+1)$ imaju boju $i$, a „ukriženi” $(2i, 2j+1)$ i $(2i+1, 2j)$ boju $j$.</li>
</ul>
<p>Svaki brid potpunog grafa je ili unutar nekog para ili između dva različita para, pa je obojen točno jednom. Prebrojimo bridove boje $i$: jedan unutar $P_i$, po dva prema svakom od ostalih $K_0 - 1$ parova, ukupno $1 + 2(K_0 - 1) = N - 1$ — dakle svaki $G_i$ je razapinjuće stablo, što je najmanje moguće (nužan uvjet je „tijesan”).</p>
<p><strong>Dijametar.</strong> Fiksirajmo boju $i$ i vrh $v \notin P_i$, $v \in P_j$. Ako je $i \lt j$: za $v = 2j$ brid $(2i, 2j)$ je paralelan i ima boju $i$; za $v = 2j+1$ brid $(2i+1, 2j+1)$ ima boju $i$. Ako je $j \lt i$: za $v = 2j$ ukriženi brid $(2j, 2i+1)$ ima boju $i$; za $v = 2j+1$ ukriženi brid $(2j+1, 2i)$ ima boju $i$. Dakle svaki vrh izvan $P_i$ susjedan je u $G_i$ s barem jednim predstavnikom, a predstavnici $2i$ i $2i+1$ su međusobno susjedni. Put između bilo koja dva vrha ide $u \to$ predstavnik $\to$ (drugi predstavnik) $\to v$, duljine najviše $3$. Time je $d_i \le 3 \le 4$ i $G_i$ je povezan. (Strukturno: $G_i$ je „dvostruka zvijezda” s centrima $2i$ i $2i+1$.)</p>
<h3>4. Neparni $N$</h3>
<p>Za $N = 2K_0 + 1$ konstruiramo bojanje za prvih $N - 1$ vrhova kao gore, a zadnji vrh $N - 1$ spojimo s vrhom $v \lt N-1$ bridom boje $\lfloor v/2 \rfloor$. Vrh $N-1$ je tako u boji $i$ susjedan s oba predstavnika $2i$ i $2i+1$, pa svojstvo „svaki vrh je na udaljenosti $\le 1$ od nekog predstavnika boje $i$” i dalje vrijedi za sve vrhove i dijametar ostaje $\le 3$. Svaki novi brid dobio je točno jednu boju.</p>
<h3>5. Primjer $N = 5$, $K = 2$</h3>
<p>Parovi $P_0 = \{0,1\}$, $P_1 = \{2,3\}$, dodatni vrh $4$. Boja $0$ (ispis $1$): $(0,1)$, $(0,2)$, $(1,3)$, $(4,0)$, $(4,1)$; boja $1$ (ispis $2$): $(2,3)$, $(0,3)$, $(1,2)$, $(4,2)$, $(4,3)$. U formatu zadatka redovi su <code>1</code> / <code>1 2</code> / <code>2 1 2</code> / <code>1 1 2 2</code> — svaki graf boje ima $5$ bridova i dijametar $\le 3$.</p>
<h3>6. Složenost i zamke</h3>
<p>Ispis matrice boja traje $O(N^2)$ po testu, ukupno $O(\sum N^2) \le 10^6$ operacija. Zamke: boje su u izlazu 1-indeksirane (interno računamo 0-indeksirano pa dodamo $1$); format izlaza traži u $i$-tom retku boje bridova $(j, i+1)$ za $j = 1, \dots, i$; ne zaboraviti spojiti dodatni vrh za neparni $N$; uvjet $K \le N(N-1)/2$ iz ulaza ne znači da je $K$ ostvariv.</p>
''',
    'verified': r'''uzorak 1/1 (checker); 300 slučajnih testova ($2 \le N \le 9$, uključujući $K$ iznad granice) provjereno checkerom koji zahtijeva <code>NO</code> točno za $K \gt \lfloor N/2 \rfloor$, a za <code>YES</code> BFS-om po svakoj boji provjerava povezanost i dijametar $\le 4$; 3 velika testa ($T = 100$, $N = 100$).''',
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
    'solution': r'''
<p>Rješenje ne postoji ako je $K = 1$ ili $K = 2 \times N \times (N-1) - 1$. Za $N \le 3$ može se primijeniti gruba sila; dalje pretpostavljamo $N \ge 4$.</p>
<p>Indeksirajmo od $0$ i nazovimo ćeliju $(i, j)$ neparnom ako je $i + j \equiv 1 \pmod 2$, a parnom inače. Prvo sve neparne ćelije obojimo jednom bojom (crno).</p>
<p>Neka je stupanj ćelije broj ćelija susjednih njoj. Želimo da zbroj stupnjeva crvenih ćelija bude jednak $K$. Za svaki $d = 2, 3, 4$ postoji pozitivan broj parnih ćelija stupnja $d$.</p>
<p>Dovoljno je proći parne ćelije po padajućem stupnju i pohlepno odlučivati hoćemo li ih uključiti, uz nekoliko malih prilagodbi.</p>
''',
    'coach': [
        (r'Koji je najveći mogući $K$ i koje bojanje ga postiže?',
         r'''<p>Susjednih parova ćelija ima točno $2N(N-1)$ ($N(N-1)$ vodoravnih i isto toliko okomitih), pa je $K \le 2N(N-1)$. Šahovnica čini <em>sve</em> parove raznobojnima, jer susjedne ćelije $(i,j)$ i $(i,j+1)$ ili $(i+1,j)$ uvijek imaju različit paritet zbroja $i + j$. To sugerira da paritet ćelije treba biti glavni alat.</p>'''),
        (r'Kako dobiti bojanje čiji se broj raznobojnih parova lako kontrolira?',
         r'''<p>Obojimo sve „neparne” ćelije ($i+j$ neparno) crno i biramo samo koje će „parne” ćelije biti crvene. Dvije parne ćelije nikad nisu susjedne, pa svaki susjedni par crvene parne ćelije čini raznobojni par, a par dviju crnih ćelija nije raznobojan. Broj raznobojnih parova je stoga točno <strong>zbroj stupnjeva</strong> (broja susjeda: $2$, $3$ ili $4$) odabranih crvenih parnih ćelija — zadatak postaje: odaberi podskup parnih ćelija sa zbrojem stupnjeva $K$.</p>'''),
        (r'Zašto su $K = 1$ i $K = 2N(N-1) - 1$ nemogući, i to za <em>svako</em> bojanje?',
         r'''<p>Svaki susjedni par je stranica nekog kvadrata $2 \times 2$ (za $N \ge 2$). Obilaskom četiriju ćelija kvadrata u krugu vraćamo se na početnu boju, pa je broj promjena boje — tj. broj raznobojnih parova u kvadratu — paran: $0$, $2$ ili $4$. Kad bi ukupno postojao točno jedan raznobojni par, kvadrat koji ga sadrži imao bi točno jedan — kontradikcija. Isto vrijedi za jednobojne parove (u kvadratu ih je $4 - \text{raznobojni}$, opet paran broj), pa ni „svi osim jednog” nije moguće. Za $N \le 3$ jednostavno isprobamo sva $2^{N^2} \le 512$ bojanja.</p>'''),
        (r'Koje zbrojeve stupnjeva možemo dobiti podskupom parnih ćelija za $N \ge 4$?',
         r'''<p>Sve $K \in [0, 2N(N-1)]$ osim $1$ i $2N(N-1) - 1$. Zbroj stupnjeva svih parnih ćelija je točno $2N(N-1)$ (svaki susjedni par ima točno jednu parnu ćeliju), pa komplement podskupa daje zbroj $2N(N-1) - K$: dovoljno je riješiti $K \le N(N-1)$. Za $N \ge 4$ postoje parne ćelije stupnja $2$ (kut), $3$ (rub) i $4$ (unutrašnjost), i to dovoljno mnogo; brojevi $\ge 2$ se prikazuju kao $4a + 3b + 2c$ s malim $b, c$, npr. $r = K \bmod 4$: $r = 0 \to$ samo četvorke, $r = 2 \to$ jedna dvojka, $r = 3 \to$ jedna trojka, $r = 1 \to$ jedna trojka i jedna dvojka umjesto jedne četvorke.</p>'''),
    ],
    'tips': [
        r'''Na mreži je paritet $i + j$ (šahovnica) prirodna bipartitna struktura: susjedne ćelije imaju različit paritet, a ćelije istog pariteta se ne dodiruju. Kad treba kontrolirati broj „loših” susjednih parova, fiksiraj jednu klasu i biraj u drugoj — doprinosi se tada zbrajaju neovisno.''',
        r'''Kad tražiš zbroj $K$ elemenata iz multiskupa s vrijednostima $\{2, 3, 4\}$, ne treba DP: uzmi što više najvećih i ostatak pokrij jednim ili dva mala elementa.''',
        r'''Male dimenzije riješi grubom silom umjesto da tražiš sve iznimke ručno; iznimke ($K = 1$ i $K_{\max} - 1$) provjeri i neovisnim argumentom (paritet u kvadratu $2 \times 2$).''',
        r'''Kad je ukupni zbroj poznat, simetrija „podskup $\leftrightarrow$ komplement” prepolovi broj slučajeva koje treba riješiti.''',
    ],
    'detailed': r'''
<h3>1. Osnovna struktura: parne i neparne ćelije</h3>
<p>Indeksirajmo ćelije $(i, j)$ s $0 \le i, j \lt N$ i nazovimo ćeliju <em>parnom</em> ako je $i + j$ paran, a <em>neparnom</em> inače. Susjedne ćelije (dijele stranicu) razlikuju se u točno jednoj koordinati za $1$, pa imaju različit paritet: mreža je bipartitni graf s klasama „parne” i „neparne”. Ukupan broj susjednih parova je $2N(N-1)$: u svakom od $N$ redaka ima $N-1$ vodoravnih parova, i simetrično za stupce. Zato je $K \le 2N(N-1)$, a šahovnica (parne crvene, neparne crne) postiže jednakost.</p>
<p>Definirajmo <em>stupanj</em> $\deg(c)$ ćelije kao broj njezinih susjeda: $4$ za unutarnje ćelije, $3$ za rubne koje nisu kutovi, $2$ za kutove (za $N \ge 2$). Zbroj stupnjeva svih parnih ćelija jednak je $2N(N-1)$, jer svaki susjedni par sadrži točno jednu parnu ćeliju i tako je prebrojen točno jednom.</p>
<h3>2. Redukcija na zbroj podskupa</h3>
<p>Obojimo sve neparne ćelije crno, a neki skup $R$ parnih ćelija crveno (ostale parne crno). Susjedni par je raznobojan ako i samo ako je njegova parna ćelija u $R$ (neparna je uvijek crna). Dakle broj raznobojnih parova je $\sum_{c \in R} \deg(c)$. Zadatak se svodi na: <strong>postoji li podskup parnih ćelija sa zbrojem stupnjeva točno $K$</strong>, i ako da, naći ga.</p>
<p>Uz to imamo simetriju: ako je $R$ podskup sa zbrojem $K$, komplement $\bar R$ (sve parne ćelije osim $R$) ima zbroj $2N(N-1) - K$. Zato je dovoljno riješiti $K \le N(N-1)$ i po potrebi uzeti komplement.</p>
<h3>3. Dostupni stupnjevi za $N \ge 4$</h3>
<p>Parne ćelije: kutovi $(0,0)$ i $(N-1,N-1)$ uvijek su parni (stupanj $2$), a kutovi $(0,N-1)$ i $(N-1,0)$ parni su samo za neparni $N$. Rubne ćelije stupnja $3$: npr. $(0, 2)$ i $(2, 0)$, postoje za $N \ge 4$. Unutarnje ćelije stupnja $4$: $(1,1)$, $(1,3)$, $(2,2)$, …; njihov broj je $\lceil (N-2)^2 / 2 \rceil \ge 2$ za $N \ge 4$. Označimo brojeve parnih ćelija stupnja $4$, $3$, $2$ s $c_4, c_3, c_2$; za $N \ge 4$ je $c_4 \ge 2$, $c_3 \ge 2$, $c_2 \ge 2$ (npr. $N = 4$: $c_4 = 2$, $c_3 = 4$, $c_2 = 2$; ukupno $8 + 12 + 4 = 24 = 2 \cdot 4 \cdot 3$).</p>
<h3>4. Koje zbrojeve možemo postići</h3>
<p>Tražimo $a \le c_4$, $b \le c_3$, $c \le c_2$ s $4a + 3b + 2c = K$. Za $2 \le K \le N(N-1)$ (polovica ukupnog zbroja) rješenje postoji: uzmemo $a = \lfloor K/4 \rfloor$ četvorki i pogledamo ostatak $r = K - 4a \in \{0,1,2,3\}$: $r = 0$ gotovo; $r = 2$ dodamo jednu dvojku; $r = 3$ jednu trojku; $r = 1$ (tada je $K \ge 5$, pa $a \ge 1$) zamijenimo jednu četvorku trojkom i dvojkom ($3 + 2 = 5$). Treba još paziti na zalihe: za velike $N$ je $4c_4 \approx 2N^2 \gt N(N-1) \ge K$, pa četvorki ima dovoljno, a za male $N$ ($4 \le N \le 6$) četvorki može ponestati (npr. $N = 4$, $K = 12$: $c_4 = 2$ daje samo $8$), no tada ostatak pokrivamo većim brojem trojki i dvojki ($12 = 4 + 4 + 2 + 2$). Zato kod ne koristi fiksnu formulu, nego za $a$ od najvećeg mogućeg prema dolje traži prikaz ostatka kao $3b + 2c$ s $b \le c_3$, $c \le c_2$ (za dani ostatak $r$ najmanji dopušteni $b$ računa se u $O(1)$). Provjerili smo iscrpno za sve $4 \le N \le 150$ i sve $K \le N(N-1)$ da prikaz postoji točno kad je $K \ne 1$; za velike $N$ to slijedi iz obilja četvorki.</p>
<p>$K = 0$: prazan skup. $K = 1$: nema ćelije stupnja $1$, nemoguće. Zajedno s komplementom: sve vrijednosti $K \in [0, 2N(N-1)]$ osim $1$ i $2N(N-1) - 1$ su ostvarive tim bojanjem.</p>
<h3>5. Zašto su $K = 1$ i $K = 2N(N-1)-1$ nemogući za <em>svako</em> bojanje</h3>
<p>Gornji argument pokazuje samo da ih naše specijalno bojanje ne postiže. Opći dokaz: promotrimo bilo koji $2 \times 2$ kvadrat mreže ($N \ge 2$). Obiđemo li njegove četiri ćelije u krugu, broj promjena boje duž ciklusa je paran (vratimo se na početnu boju), pa je broj raznobojnih parova unutar kvadrata $0$, $2$ ili $4$. Ako je ukupno točno jedan raznobojni par, on leži u nekom $2 \times 2$ kvadratu (svaki susjedni par je stranica barem jednog takvog kvadrata), a tada bi u tom kvadratu bio točno jedan raznobojni par — kontradikcija. Za $K = 2N(N-1) - 1$: točno jedan par je <em>jednobojan</em>; ali u kvadratu koji ga sadrži, broj jednobojnih parova je $4 - (\text{raznobojni}) \in \{0, 2, 4\}$ — opet kontradikcija.</p>
<h3>6. Mali $N$</h3>
<p>Za $N \le 3$ ima najviše $2^9 = 512$ bojanja; ispitamo ih sva i prebrojimo parove. Time izbjegavamo ručno traženje iznimaka (npr. za $N = 2$ moguće su samo $0, 2, 4$, a za $N = 3$ nedostaju i $1$ i $11$). Za $N = 1$ jedina je vrijednost $K = 0$.</p>
<h3>7. Algoritam, složenost, zamke</h3>
<ol>
<li>$N \le 3$: gruba sila.</li>
<li>Inače ako je $K \gt N(N-1)$, postavi $K \leftarrow 2N(N-1) - K$ i zapamti da treba komplement.</li>
<li>Razvrstaj parne ćelije po stupnju; nađi $a, b, c$ s $4a + 3b + 2c = K$; ako ne postoji — <code>Impossible</code> (u praksi samo $K = 1$).</li>
<li>Oboji odabrane (ili, uz komplement, neodabrane) parne ćelije crveno, sve ostalo crno, ispiši.</li>
</ol>
<p>Složenost $O(N^2)$ po testu, ukupno $O(\sum N^2) \le 10^6$. Zamke: $2N(N-1)$ za $N = 10^3$ je $\approx 2 \cdot 10^6$, stane u 32 bita, ali $K$ čitamo kao 64-bitni broj radi sigurnosti; pri komplementu paziti da se komplementiraju samo <em>parne</em> ćelije; provjeriti da su kutovi $(0, N-1)$ i $(N-1, 0)$ parni samo za neparni $N$ — zato stupnjeve računamo izravno iz koordinata, a ne po formuli.</p>
''',
    'verified': r'''uzorak 1/1 (checker); 300 slučajnih testova ($N \le 7$, uključujući rubne $K \in \{0, 1, K_{\max}, K_{\max}-1, K_{\max}-2\}$) provjereno checkerom koji za <code>Possible</code> prebroji raznobojne parove, a <code>Impossible</code> prihvaća za $N \le 4$ samo ako iscrpna pretraga svih bojanja potvrdi nemogućnost, a za $N \ge 5$ samo za $K \in \{1, 2N(N-1)-1\}$; 3 velika testa ($N = 1000$).''',
},
]
