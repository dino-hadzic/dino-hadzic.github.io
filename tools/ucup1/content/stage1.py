"""1st Universal Cup – Stage 1: Shenyang. Uvezeno iz ručno pisanih stranica (import_legacy.py); naputci i
trenerski koraci iz nekadašnjeg retro_stage1.py."""

STAGE = {
    'no': 1,
    'name': 'Stage 1: Shenyang',
    'source_name': 'The 2022 ICPC Asia Shenyang Regional Contest',
    'source_html': r'''
<p>Prijevod službenog rješenja autorskog tima Sveučilišta Northeastern (东北大学命题组): <a href="https://contest.ucup.ac/download.php?type=attachments&amp;id=1096&amp;r=2">Tutorial (zh-cn)</a>. Tekst zadatka preveden je prema službenim <a href="https://contest.ucup.ac/download.php?type=attachments&amp;id=1096&amp;r=1">engleskim tekstovima zadataka</a>. Zadatak je dostupan na <a href="https://contest.ucup.ac/contest/1096">Universal Cup Judging System</a>.</p>
''',
}

PROBLEMS = [
{
    'letter': 'A',
    'title': 'Absolute Difference',
    'title_hr': 'Apsolutna razlika',
    'slug': 'A_absolute_difference',
    'tl': '1 s',
    'ml': '512 MB',
    'statement': r'''
<p>Alice i Bob svaki imaju skup realnih brojeva, a oba su skupa unija nekoliko međusobno disjunktnih zatvorenih intervala. Svatko od njih neovisno bira uniformno slučajan realan broj iz svog skupa, a ti trebaš izračunati očekivanu apsolutnu razliku ta dva broja.</p>
<p>Formalnije, za skup $S = \bigcup [l, r]$ uniformno slučajan izbor broja $x$ iz $S$ znači da za bilo koja dva intervala $[l_1, r_1], [l_2, r_2] \subseteq S$ jednake duljine (tj. $r_1 - l_1 = r_2 - l_2$) vrijedi $P(x \in [l_1, r_1]) = P(x \in [l_2, r_2])$.</p>
<h3>Ulaz</h3>
<p>Prvi redak sadrži dva cijela broja $n$ i $m$ ($1 \le n, m \le 10^5$) — broj intervala koji čine Aliceov, odnosno Bobov skup. Svaki od sljedećih $n + m$ redaka sadrži dva cijela broja $l$ i $r$ ($-10^9 \le l \le r \le 10^9$) koji opisuju zatvoreni interval $[l, r]$; prvih $n$ intervala čini Aliceov, a preostalih $m$ Bobov skup. Interval s $l = r$ je degeneriran i sadrži samo jedan realan broj. Intervali unutar istog skupa su međusobno disjunktni.</p>
<h3>Izlaz</h3>
<p>Ispiši očekivanu apsolutnu razliku. Odgovor se prihvaća ako mu apsolutna ili relativna greška ne prelazi $10^{-9}$.</p>
<h3>Primjer</h3>
<p>Ako oba skupa iznose $[0, 1]$, očekivana razlika je $\int_0^1 \int_0^1 |x - y|\,dx\,dy = \frac{1}{3}$. Ako Alice bira iz $[0, 1]$, a Bob može odabrati samo broj $1$, očekivana razlika je $\int_0^1 |x - 1|\,dx = \frac{1}{2}$.</p>
''',
    'hints': [
        r'''
<p>Očekivanje je zbroj po svim parovima intervala $(S_1, S_2)$ integrala $\int\!\int |x - y|$, podijeljen umnoškom ukupnih duljina. Za disjunktne parove apsolutna vrijednost nestaje — integral je zatvorena formula u $l_1, r_1, l_2, r_2$ koja se zbraja prefiksnim zbrojevima.</p>
''',
        r'''
<p>Parova koji se sijeku ima samo $O(n + m)$ (intervali unutar skupa su disjunktni): svaki rastavi na presjek (par jednakih intervala, integral $\frac{L^3}{3}$) i najviše $3$ disjunktna para. Degenerirane skupove (sve točke) tretiraj težinom $1$ po točki.</p>
''',
    ],
    'coach': [
        ('Opažanje 1: linearnost očekivanja',
         r'''
<p>$E|x - y| = \frac{1}{|A||B|}\sum_{S_1 \subseteq A}\sum_{S_2 \subseteq B}\int_{S_1}\int_{S_2}|x-y|$. Problem je broj parova, $O(nm)$.</p>
'''),
        ('Opažanje 2: disjunktni parovi imaju zatvorenu formulu',
         r'''
<p>Ako je $S_1$ lijevo od $S_2$, $|x - y| = y - x$ i integral je $|S_1||S_2|\bigl(\mathrm{sred}(S_2) - \mathrm{sred}(S_1)\bigr)$. Sortiraj intervale; za fiksni $S_2$ zbroj po svim $S_1$ lijevo od njega treba samo $\sum |S_1|$ i $\sum |S_1|\,\mathrm{sred}(S_1)$ — prefiksni zbrojevi.</p>
'''),
        ('Redukcija: parovi koji se sijeku',
         r'''
<p>Zbog disjunktnosti unutar skupa, svaki interval iz $A$ siječe se s intervalima iz $B$ čiji ukupan broj je $O(n + m)$ (dva pokazivača). Za takav par rastavi $S_1, S_2$ oko presjeka $I$: par $(I, I)$ daje $\frac{|I|^3}{3}$, a ostali dijelovi su disjunktni parovi.</p>
'''),
        ('Algoritam i složenost',
         r'''
<p>Degenerirani skup (svi intervali točke): uniformni izbor točke — svakom intervalu daj težinu $1$ umjesto duljine i koristi istu formulu s težinama. Sortiranje + prefiksni zbrojevi + dva pokazivača: $O((n + m)\log(n + m))$. Pazi na preciznost (koristi <code>long double</code> ili razlomke gdje treba).</p>
'''),
    ],
    'solution': r'''
<p>Najprije zanemarimo slučaj u kojem su svi intervali nekog od skupova degenerirani. Zadatak se tada svodi na sljedeće: iz skupa $A$ odaberemo interval $S_1 = [l_1, r_1]$, iz skupa $B$ interval $S_2 = [l_2, r_2]$, izračunamo
$$\int_{l_1}^{r_1} \int_{l_2}^{r_2} |x - y| \,dx\,dy$$
i to pribrojimo odgovoru. Na kraju odgovor podijelimo umnoškom ukupnih duljina intervala u svakom od dva skupa.</p>
<p>Ako se $S_1$ i $S_2$ ne sijeku (strogo), apsolutnu vrijednost možemo odmah rastaviti i integrirati neovisno po $x$ i po $y$; nakon što izvedemo formulu, računanje za sve parove ubrzamo prefiksnim sumama. U suprotnom $S_1$ i $S_2$ rastavimo na presječni dio i dijelove izvan presjeka, čime dobijemo jedan par jednakih intervala i najviše $3$ para disjunktnih intervala, koje računamo kao gore. Budući da su intervali unutar jednog skupa međusobno disjunktni, parova $S_1$, $S_2$ koji se sijeku ima samo $O(n + m)$, pa taj dio možemo izračunati izravno.</p>
<p>Slučaj u kojem su svi intervali nekog skupa degenerirani odgovara uniformnom slučajnom izboru jedne od nekoliko točaka. U predobradi svakom intervalu dodijelimo težinu: $1$ ako su svi intervali njegova skupa degenerirani, a inače duljinu intervala. Tako možemo ponovno iskoristiti logiku nedegeneriranog slučaja i smanjiti složenost implementacije.</p>
''',
},
{
    'letter': 'B',
    'title': 'Binary Substrings',
    'title_hr': 'Binarni podnizovi',
    'slug': 'B_binary_substrings',
    'tl': '2 s',
    'ml': '512 MB',
    'statement': r'''
<p>Za zadani cijeli broj $n$ pronađi niz duljine $n$ koji se sastoji samo od znakova 0 i 1 i koji ima najveći mogući broj različitih nepraznih podnizova (uzastopnih dijelova niza).</p>
<h3>Ulaz</h3>
<p>Jedini redak sadrži cijeli broj $n$ ($1 \le n \le 2 \times 10^5$) — duljinu 01-niza.</p>
<h3>Izlaz</h3>
<p>Ispiši jedan 01-niz duljine $n$ koji među svim 01-nizovima duljine $n$ ima najveći broj različitih nepraznih podnizova. Ako ima više rješenja, ispiši bilo koje.</p>
<h3>Primjer</h3>
<p>Za $n = 2$ jedno rješenje je <code>01</code> (3 različita podniza: 0, 1, 01). Za $n = 5$ jedno rješenje je <code>00110</code> s 12 različitih podnizova.</p>
''',
    'hints': [
        r'''
<p>Različitih podnizova duljine $i$ ima najviše $\min(2^i, n - i + 1)$. Odaberi $k$ s $2^k + k - 1 \le n \lt 2^{k+1} + k$: cilj je da se svih $2^k$ nizova duljine $k$ pojavi i da su svi podnizovi duljine $k+1$ različiti.</p>
''',
        r'''
<p>Za $n = 2^k + k - 1$ to je točno de Bruijnov niz — Eulerov ciklus u de Bruijnovu grafu s $2^{k-1}$ vrhova. Za veće $n$ produlji ga Eulerovim putom u grafu s $2^k$ vrhova (nakon uklanjanja već iskorištenih bridova), ili kreni od Eulerova ciklusa u većem grafu i uzmi prefiks; slučajnost + višestruki pokušaji pokrivaju sve $n$.</p>
''',
    ],
    'coach': [
        ('Opažanje: gornja granica',
         r'''
<p>Broj različitih podnizova $\le \sum_{i=1}^n \min(2^i, n-i+1)$. Granica se postiže ako su za male duljine prisutni <em>svi</em> nizovi, a za velike duljine svi podnizovi međusobno različiti. Prijelomna duljina je $k$ s $2^k + k - 1 \le n \lt 2^{k+1} + k$.</p>
'''),
        ('Redukcija: de Bruijnov graf',
         r'''
<p>Vrhovi = nizovi duljine $k-1$, brid = niz duljine $k$ (dodavanje $0$/$1$ i odbacivanje prvog znaka). Graf je Eulerov; Eulerov ciklus daje niz duljine $2^k + k - 1$ koji sadrži svaki niz duljine $k$ točno jednom — de Bruijnov niz. Isti ciklus je Hamiltonov ciklus u grafu s $2^k$ vrhova.</p>
'''),
        ('Algoritam za veće $n$',
         r'''
<p>Pristup 1 (mali $n$ u rasponu): iz Hamiltonova puta u grafu $2^k$ vrhova ukloni iskorištene bridove i iz zadnjeg vrha traži Eulerov put — dobiveni niz ima do $2^{k+1} + k - 1$ znakova, uzmi prefiks. Pristup 2 (veliki $n$): Eulerov ciklus u grafu s $2^k$ vrhova, uzmi prefiks duljine $n$ i provjeri da sadrži sve nizove duljine $k$. Slučajan poredak bridova i više pokušaja; provjeri lokalno da su za svaki od $O(\log n)$ vrijednosti $k$ pokrivene sve duljine.</p>
'''),
        ('Složenost',
         r'''
<p>Hierholzer u $O(2^k) = O(n)$ po pokušaju, konstantan broj pokušaja. Provjera valjanosti: hashiranje podnizova duljine $k$ i $k+1$.</p>
'''),
    ],
    'solution': r'''
<p>Najprije analizirajmo broj različitih podnizova. Budući da 01-nizova duljine $i$ ima najviše $\min(2^i, n - i + 1)$, broj različitih podnizova ne prelazi
$$\sum_{i=1}^{n} \min(2^i, n - i + 1).$$
Slučaj $n = 1$ obradimo posebno. Zatim odaberemo prirodan broj $k$ takav da vrijedi $2^k + k - 1 \le n &lt; 2^{k+1} + (k+1) - 1$. Tada trebamo postići da se svih $2^k$ različitih 01-nizova duljine $k$ pojavi kao podniz i da su svi podnizovi duljine $k + 1$ međusobno različiti.</p>
<p>Kada je $n = 2^k + k - 1$, riječ je o konstrukciji <b>de Bruijnova niza</b>. Konstruiramo usmjereni graf s $2^{k-1}$ vrhova, numeriranih od $0$ do $2^{k-1} - 1$; svaki vrh predstavlja niz duljine $k - 1$ (zajednički dio dvaju susjednih podnizova duljine $k$). Iz svakog niza vodi usmjereni brid u sufiks duljine $k - 1$ niza dobivenog dodavanjem znaka 0 ili 1 na kraj. To je de Bruijnov graf; može se dokazati da u njemu postoji Eulerov ciklus, a iz jednog Eulerova ciklusa dobivamo valjano rješenje.</p>
<p>Kada je $n &gt; 2^k + k - 1$, gornji niz treba produljiti. Najprije nađemo Eulerov ciklus u grafu s $2^{k-1}$ vrhova — to je istodobno Hamiltonov ciklus u de Bruijnovu grafu s $2^k$ vrhova. Ako na tom Hamiltonovu ciklusu prekinemo brid koji izlazi iz vrha $0$, dobijemo Hamiltonov put koji svaki podniz duljine $k$ obilazi točno jednom. Nakon što taj put uklonimo iz de Bruijnova grafa s $2^k$ vrhova, iz vrha $0$ tražimo Eulerov put kojim proširujemo prethodni put. U najboljem slučaju prođemo sve bridove osim petlje u vrhu $2^k - 1$, čime dobijemo niz duljine $2^{k+1} + (k+1) - 2$, pa je dovoljno uzeti njegov prefiks duljine $n$. Valja primijetiti da se nakon uklanjanja bridova graf može raspasti na više slabo povezanih komponenti, pa ne dobijemo teoretski najdulji niz — ali ovaj pristup već rješava relativno male vrijednosti $n$.</p>
<p>Za relativno velike $n$ probajmo drugi algoritam: izravno pronađemo Eulerov ciklus u de Bruijnovu grafu s $2^k$ vrhova, uzmemo $0$ kao prvi podniz duljine $k$ i tako konstruiramo niz, a zatim pronađemo najkraći prefiks koji sadrži sve bitno različite podnizove duljine $k$. Za veće $n$ opet je dovoljno uzeti prefiks duljine $n$.</p>
<p>U oba algoritma pri traženju Eulerova ciklusa uvedemo slučajnost (npr. slučajan početni vrh i slučajan poredak izlaznih bridova) i postupak ponovimo više puta neovisno, čime se najveći $n$ koji rješava prvi algoritam i najmanji $n$ koji rješava drugi algoritam sve više približavaju. Cilj je da za dani $k$ pokrijemo sve $n$ koji zadovoljavaju $2^k + k - 1 \le n &lt; 2^{k+1} + (k+1) - 1$. Budući da različitih $k$ ima samo $O(\log n)$, lokalno možemo provjeriti brzinu izvođenja za razna sjemena generatora slučajnih brojeva te je li dobiveno rješenje valjano.</p>
''',
},
{
    'letter': 'C',
    'title': 'Clamped Sequence',
    'title_hr': 'Stegnuti niz',
    'slug': 'C_clamped_sequence',
    'tl': '1 s',
    'ml': '512 MB',
    'statement': r'''
<p>Zadan je niz cijelih brojeva $a_1, a_2, \dots, a_n$ i prirodan broj $d$. Niz treba "stegnuti" (engl. <i>clamp</i>) na raspon $[l, r]$ za koji vrijedi $0 \le r - l \le d$, tako da se maksimizira $\sum_{i=1}^{n-1} |a_i - a_{i+1}|$.</p>
<p>Stezanje niza na raspon $[l, r]$ svaki element pretvara u
$$a_i := \begin{cases} l, &amp; a_i &lt; l; \\ a_i, &amp; l \le a_i \le r; \\ r, &amp; a_i &gt; r. \end{cases}$$
Brojevi $l$ i $r$ su proizvoljni realni brojevi koje biraš ti, uz zadano ograničenje. Može se pokazati da je maksimalna suma uvijek cijeli broj.</p>
<h3>Ulaz</h3>
<p>Prvi redak sadrži cijele brojeve $n$ ($2 \le n \le 5\,000$) i $d$ ($1 \le d \le 10^9$). Drugi redak sadrži $n$ cijelih brojeva $a_1, \dots, a_n$ ($-10^9 \le a_i \le 10^9$).</p>
<h3>Izlaz</h3>
<p>Ispiši jedan cijeli broj — maksimalnu sumu.</p>
<h3>Primjer</h3>
<p>Za $n = 8$, $d = 3$ i niz $3\ 1\ 4\ 1\ 5\ 9\ 2\ 6$ odgovor je $15$: stezanjem na $[1, 4]$ dobivamo $[3, 1, 4, 1, 4, 4, 2, 4]$.</p>
''',
    'hints': [
        r'''
<p>Uvijek je optimalno uzeti $r = l + d$ (širi raspon nikad ne smanjuje razlike). Ostaje jedan realan parametar $l$.</p>
''',
        r'''
<p>Svaki $|a_i - a_{i+1}|$ nakon stezanja je po dijelovima linearna funkcija od $l$ s lomovima u $a_i$ i $a_i - d$. Maksimum po dijelovima linearne funkcije postiže se u lomu: isprobaj $O(n)$ kandidata za $l$.</p>
''',
    ],
    'coach': [
        ('Opažanje 1: $r = l + d$',
         r'''
<p>Za fiksni $l$, povećanje $r$ može samo smanjiti stezanje elemenata iznad $r$, a $|\cdot|$ između stegnutih vrijednosti se time ne smanjuje. Dakle $r = l + d$.</p>
'''),
        ('Opažanje 2: po dijelovima linearna funkcija',
         r'''
<p>$\mathrm{clamp}(a_i)$ kao funkcija od $l$ mijenja nagib samo u $l = a_i$ i $l = a_i - d$; razlika dvaju takvih izraza ima lomove u uniji tih točaka. Zbroj po dijelovima linearnih funkcija maksimum postiže u nekom lomu — $2n$ kandidata.</p>
'''),
        ('Algoritam i složenost',
         r'''
<p>Za svaki kandidat $l$ izračunaj zbroj u $O(n)$: ukupno $O(n^2)$ uz $n \le 5000$. Brže: sortiraj kandidate i sweepom održavaj doprinos svakog člana inkrementalno, $O(n \log n)$.</p>
'''),
    ],
    'solution': r'''
<p>Očito je optimalno uzeti $r = l + d$. Doprinos svakog člana $|a_i - a_{i+1}|$ ukupnoj sumi je po dijelovima linearna funkcija od $l$. Stoga možemo isprobati $O(n)$ ključnih vrijednosti $l$ (točke u kojima se neka od tih funkcija "lomi", tj. vrijednosti $a_i$ i $a_i - d$) i za svaku izračunati odgovor, što daje složenost $O(n^2)$. Alternativno, metodom pomične linije (<i>sweep line</i>) doprinose možemo održavati inkrementalno i postići složenost $O(n \log n)$.</p>
''',
},
{
    'letter': 'D',
    'title': 'DRX vs. T1',
    'title_hr': 'DRX protiv T1',
    'slug': 'D_drx_vs_t1',
    'tl': '1 s',
    'ml': '512 MB',
    'statement': r'''
<p>Finale svjetskog prvenstva u League of Legendsu 2022. igra se između timova DRX i T1. Tim koji pobijedi u tri od pet igara osvaja naslov. Zadan je predviđeni rezultat finala kao niz duljine $5$ koji se sastoji od znakova <code>D</code>, <code>T</code> i <code>?</code>: $i$-ti znak označava pobjednika $i$-te igre (<code>D</code> — DRX, <code>T</code> — T1), a <code>?</code> znači da igra nije potrebna jer je neki tim već pobijedio u $3$ igre.</p>
<h3>Ulaz</h3>
<p>Jedini redak sadrži niz duljine $5$ od znakova <code>D</code>, <code>T</code> i <code>?</code>. Zajamčeno je da je rezultat valjan BO5 rezultat: nijedan <code>?</code> ne dolazi prije nekog <code>D</code> ili <code>T</code>, i točno jedan tim ima točno tri pobjede.</p>
<h3>Izlaz</h3>
<p>Ispiši <code>DRX</code> ako je prvak DRX, odnosno <code>T1</code> ako je prvak T1.</p>
<h3>Primjer</h3>
<p>Za ulaz <code>TDTT?</code> odgovor je <code>T1</code>; za ulaz <code>DTDD?</code> odgovor je <code>DRX</code>.</p>
''',
    'hints': [
        r'''
<p>Ne treba ništa pamtiti osim broja pobjeda: prvak je tim koji ima tri slova u nizu.</p>
''',
        r'''
<p>Prebroji znakove <code>D</code>; ako ih je $3$, odgovor je <code>DRX</code>, inače <code>T1</code>.</p>
''',
    ],
    'coach': [
        ('Opažanje',
         r'''
<p>Ulaz je zajamčeno valjan BO5 rezultat: točno jedan tim ima točno tri pobjede.</p>
'''),
        ('Redukcija',
         r'''
<p>Nije bitan redoslijed ni pozicije upitnika — samo broj pojavljivanja svakog slova.</p>
'''),
        ('Algoritam',
         r'''
<p>Jedan prolaz po $5$ znakova, $O(1)$.</p>
'''),
    ],
    'solution': r'''
<p>Dovoljno je simulirati postupak opisan u tekstu zadatka: prebrojimo pobjede svakog tima (znakove <code>D</code> i <code>T</code>) i ispišemo tim koji ih ima tri.</p>
''',
},
{
    'letter': 'E',
    'title': 'Graph Completing',
    'title_hr': 'Dopunjavanje grafa',
    'slug': 'E_graph_completing',
    'tl': '1 s',
    'ml': '512 MB',
    'statement': r'''
<p>Zadan je jednostavan povezan neusmjereni graf s $n$ vrhova i $m$ bridova. Smiješ dodati proizvoljno mnogo bridova (moguće i nijedan). Prebroji, modulo $998\,244\,353$, na koliko različitih načina to možeš učiniti tako da graf postane <b>bridno dvostruko povezan</b> i ostane jednostavan. Dva načina dodavanja smatraju se različitima ako postoji brid $(u, v)$ dodan u jednom, a ne i u drugom.</p>
<ul>
    <li>Jednostavan graf nema petlji ni višestrukih bridova.</li>
    <li>U povezanom grafu između svaka dva različita vrha postoji barem jedan put.</li>
    <li>U bridno dvostruko povezanom grafu između svaka dva različita vrha postoje barem dva puta koji nemaju zajedničkih bridova.</li>
</ul>
<h3>Ulaz</h3>
<p>Prvi redak sadrži cijele brojeve $n$ ($2 \le n \le 5\,000$) i $m$ ($n - 1 \le m \le \min(\frac{n(n-1)}{2}, 10\,000)$). Slijedi $m$ redaka s bridovima $u$, $v$ ($1 \le u, v \le n$).</p>
<h3>Izlaz</h3>
<p>Ispiši broj načina modulo $998\,244\,353$.</p>
<h3>Primjer</h3>
<p>Za put $1 - 2 - 3$ odgovor je $1$ (jedini način je dodati brid $(1, 3)$). Za ciklus na $4$ vrha odgovor je $4$.</p>
''',
    'hints': [
        r'''
<p>Kontrahiraj bridno dvostruko povezane komponente — ostaje stablo (bridovi stabla su mostovi). Dodani brid $(u, v)$ „pokriva” put u stablu; treba pokriti sve bridove stabla.</p>
''',
        r'''
<p>Uključivanje-isključivanje po skupu <em>nepokrivenih</em> bridova stabla: uklanjanje tih bridova dijeli stablo na komponente, a bridovi se smiju dodavati samo unutar komponente ($2^{\text{broj mogućih bridova}}$). To se računa DP-om na stablu $dp_{u,i}$ = komponenta vrha $u$ ima veličinu $i$ (zbroj izvornih vrhova).</p>
''',
    ],
    'coach': [
        ('Opažanje 1: kontrakcija',
         r'''
<p>Bridovi koji nisu mostovi već su u „ciklusu”. Nakon kontrakcije 2-bridno-povezanih komponenata graf je stablo; graf postaje 2-bridno-povezan ako i samo ako svaki brid stabla leži na ciklusu, tj. pokriven je nekim dodanim bridom.</p>
'''),
        ('Opažanje 2: uključivanje-isključivanje',
         r'''
<p>Brojanje skupova dodanih bridova koji pokrivaju <em>sve</em> bridove stabla: $\sum_{F \subseteq E_T} (-1)^{|F|}\cdot(\text{broj skupova koji ne pokrivaju nijedan brid iz } F)$. Ako bridovi iz $F$ nisu pokriveni, dodani bridovi idu samo unutar komponenata stabla $\setminus F$; broj je $\prod_{\text{komp}} 2^{\binom{s}{2} - m_{\text{unutar}}}$, gdje je $s$ broj izvornih vrhova komponente.</p>
'''),
        ('Algoritam: DP po stablu',
         r'''
<p>$dp_{u,i}$ = zbroj s predznakom po podstablu od $u$ ako komponenta koja sadrži $u$ trenutno ima $i$ izvornih vrhova. Za dijete $v$: ili brid $(u,v)$ nije u $F$ — stopi komponente ($i + j$, množi brojem bridova koji se sada smiju dodati između njih), ili je u $F$ — komponenta od $v$ se zatvara, pomnoži s $-1$ i s $2^{\binom{j}{2} - m_v}$. Klasična analiza „ruksaka po veličinama podstabala” daje $O(n^2)$.</p>
'''),
        ('Složenost',
         r'''
<p>$O(n + m)$ za mostove i kontrakciju, $O(n^2)$ za DP; $n \le 5000$.</p>
'''),
    ],
    'solution': r'''
<p>Najprije kontrahiramo bridno dvostruko povezane komponente (2-edge-connected components) početnog grafa. Budući da je graf povezan, nakon kontrakcije dobivamo stablo. Svaki dodani nestablasti brid $(u, v)$ "pokriva" put u stablu od $u$ do $v$; graf postaje bridno dvostruko povezan točno onda kada su svi bridovi stabla pokriveni.</p>
<p>Primijenimo formulu uključivanja-isključivanja na pokrivenost bridova stabla: fiksiramo skup bridova stabla koji sigurno <i>nisu</i> pokriveni. Uklanjanjem tih bridova stablo se raspada na nekoliko povezanih komponenti, a bridovi se smiju dodavati samo unutar pojedine komponente.</p>
<p>Taj postupak uključivanja-isključivanja računamo dinamičkim programiranjem: $dp_{u,i}$ označava broj načina unutar podstabla s korijenom $u$ ako komponenta koja sadrži $u$ ima veličinu $i$. Pri prijelazu za svako dijete $v$ odlučujemo hoće li se njegova komponenta spojiti s komponentom vrha $u$: ako se spaja, između dviju komponenti smijemo dodati proizvoljan podskup bridova i komponente stopimo u jednu; ako se ne spaja, brid $(u, v)$ ostaje nepokriven i pribraja se s predznakom prema uključivanju-isključivanju. Druga dimenzija ide najviše do veličine podstabla, pa se standardnom analizom može dokazati da je ukupna složenost $O(n^2)$.</p>
''',
},
{
    'letter': 'F',
    'title': 'Half Mixed',
    'title_hr': 'Pola miješano',
    'slug': 'F_half_mixed',
    'tl': '2 s',
    'ml': '512 MB',
    'statement': r'''
<p>Za zadane cijele brojeve $n$ i $m$ konstruiraj matricu $M$ takvu da:</p>
<ul>
    <li>$M$ ima $n$ redaka i $m$ stupaca;</li>
    <li>$M$ sadrži samo nule i jedinice, tj. $M_{i,j} \in \{0, 1\}$;</li>
    <li>broj <b>miješanih</b> podpravokutnika jednak je broju <b>čistih</b> podpravokutnika. Podpravokutnik koji sadrži i nule i jedinice je miješan, a inače je čist. Podpravokutnik je presjek nekoliko uzastopnih redaka i nekoliko uzastopnih stupaca.</li>
</ul>
<p>Ako postoji više rješenja, ispiši bilo koje; ako rješenje ne postoji, to javi.</p>
<h3>Ulaz</h3>
<p>Prvi redak sadrži broj testnih primjera $T$ ($1 \le T \le 10^5$). Svaki testni primjer sadrži $n$ i $m$ ($1 \le n, m \le 10^6$, $1 \le n \times m \le 10^6$). Zbroj $n \times m$ po svim primjerima ne prelazi $5 \times 10^6$.</p>
<h3>Izlaz</h3>
<p>Za svaki primjer ispiši <code>No</code> ako rješenje ne postoji, a inače <code>Yes</code> i zatim $n$ redaka matrice.</p>
<h3>Primjer</h3>
<p>Za $2 \times 3$ jedno rješenje je <code>0 1 1</code> / <code>1 1 0</code> (po $9$ miješanih i čistih podpravokutnika). Za $1 \times 1$ rješenje ne postoji.</p>
''',
    'hints': [
        r'''
<p>Ukupno je $\frac{n(n+1)}{2}\cdot\frac{m(m+1)}{2}$ podpravokutnika; ako je neparno, nema rješenja. Inače je jedan od faktora paran — recimo $\frac{m(m+1)}{2}$. Tada je dovoljno riješiti $1 \times m$ i redak ponoviti u svih $n$ redaka.</p>
''',
        r'''
<p>U retku s jednobojnim segmentima duljina $l_1, \dots, l_k$ čistih podintervala je $\sum \frac{l_i(l_i+1)}{2}$; treba točno $\frac{m(m+1)}{4}$. Gradi pohlepno: uvijek uzmi najveći $l$ koji ne prekoračuje preostali cilj.</p>
''',
    ],
    'coach': [
        ('Opažanje 1: nužan uvjet i redukcija na $1 \times m$',
         r'''
<p>Miješanih = čistih $\Rightarrow$ ukupan broj podpravokutnika paran. Ako je $\frac{m(m+1)}{2}$ paran, matrica s jednakim redcima ima čistih podpravokutnika $\frac{n(n+1)}{2}\cdot(\text{čisti podintervali retka})$, pa je dovoljno da redak ima točno pola čistih podintervala.</p>
'''),
        ('Opažanje 2: struktura retka',
         r'''
<p>Podinterval je čist ako i samo ako je unutar jednog jednobojnog segmenta: $\sum_i \frac{l_i(l_i+1)}{2}$. Boje segmenata alterniraju, pa je bitna samo particija $m = \sum l_i$.</p>
'''),
        ('Algoritam: pohlepna particija',
         r'''
<p>Preostali cilj $T = \frac{m(m+1)}{4}$, preostala duljina $m$. Uzmi najveći $l$ s $\frac{l(l+1)}{2} \le T - (\text{preostala duljina} - l)$ (svaki preostali znak mora dati barem $1$), smanji $T$ i duljinu, ponovi. Pohlepa uvijek uspijeva jer su trokutasti brojevi „gusti” u odnosu na ostatak.</p>
'''),
        ('Složenost',
         r'''
<p>$O(nm)$ po testu za ispis; $\sum nm \le 5 \cdot 10^6$.</p>
'''),
    ],
    'solution': r'''
<p>Ukupan broj podpravokutnika je $\frac{n(n+1)}{2} \times \frac{m(m+1)}{2}$. Ako je taj broj neparan, rješenje očito ne postoji. Inače je barem jedan od brojeva $\frac{n(n+1)}{2}$ i $\frac{m(m+1)}{2}$ paran; bez smanjenja općenitosti neka je $\frac{m(m+1)}{2}$ paran. Tada je dovoljno riješiti problem dimenzija $1 \times m$ i dobiveni redak ponoviti $n$ puta (složiti $n$ jednakih redaka).</p>
<p>U problemu $1 \times m$ broj podintervala je $\frac{m(m+1)}{2}$. Označimo duljine jednobojnih segmenata retka s $l_1, l_2, \dots, l_k$; broj čistih podintervala tada je $\sum_{i=1}^{k} \frac{l_i(l_i+1)}{2}$. Dovoljno je pronaći rješenje koje zadovoljava sljedeća dva uvjeta:
$$\sum_{i=1}^{k} l_i = m, \qquad \sum_{i=1}^{k} \frac{l_i(l_i+1)}{2} = \frac{m(m+1)}{4}.$$</p>
<p>Rješenje konstruiramo pohlepno: u svakom koraku uzmemo najveći mogući $l_i$ (najveći koji ne prekoračuje preostali potrebni broj čistih podintervala) i tako dalje dok ne popunimo cijeli redak.</p>
''',
},
{
    'letter': 'G',
    'title': 'Meet in the Middle',
    'title_hr': 'Susret na pola puta',
    'slug': 'G_meet_in_the_middle',
    'tl': '5 s',
    'ml': '512 MB',
    'statement': r'''
<p>Bajtlandija ima $n$ gradova numeriranih od $1$ do $n$, te $n - 1$ dvosmjernih cesta i $n - 1$ dvosmjernih željezničkih pruga. Između svaka dva grada može se putovati samo cestama, a isto tako i samo prugama (i ceste i pruge tvore stablo).</p>
<p>Alice i Bob planiraju $q$ putovanja. U svakom putovanju Alice kreće iz grada $a$ i putuje isključivo cestama, a Bob kreće iz grada $b$ i putuje isključivo prugama. Oboje na kraju stižu u isti odredišni grad, ne posjećujući nijedan grad više puta. Za svako putovanje pronađi najveću moguću ukupnu duljinu njihovih ruta među svim izborima odredišnog grada.</p>
<h3>Ulaz</h3>
<p>Prvi redak sadrži $n$ ($2 \le n \le 10^5$) i $q$ ($1 \le q \le 5 \times 10^5$). Slijedi $n - 1$ redaka s cestama $u$, $v$, $w$ ($1 \le w \le 10^9$), zatim $n - 1$ redaka s prugama u istom obliku, te $q$ redaka s upitima $a$, $b$.</p>
<h3>Izlaz</h3>
<p>Za svaki upit ispiši najveću ukupnu duljinu Aliceine i Bobove rute.</p>
''',
    'hints': [
        r'''
<p>Tražimo $\max_j \bigl(dis_1(a, j) + dis_2(b, j)\bigr)$. Zamisli da na svaki vrh $j$ drugog stabla objesiš list $j'$ bridom težine $dis_1(a, j)$: tražimo najudaljeniji vrh od $b$ u novom stablu — a to je uvijek kraj dijametra.</p>
''',
        r'''
<p>Offline po $a$: DFS-om po prvom stablu, prijelaz $a \to$ dijete mijenja $dis_1(a, \cdot)$ za $+w$ izvan podstabla i $-w$ unutra. Dijametar skupa vrhova (krajevi) spaja se iz dva dijela u $O(1)$ LCA-upita, pa ga drži u segmentnom stablu nad DFS poretkom prvog stabla.</p>
''',
    ],
    'coach': [
        ('Opažanje 1: dijametar rješava „najdalji od $b$”',
         r'''
<p>U stablu s težinama, vrh najudaljeniji od bilo kojeg $b$ je jedan od dvaju krajeva dijametra. Nakon što objesimo listove $j'$ s težinom $dis_1(a, j)$, odgovor za $(a, b)$ je $\max$ po dva kraja dijametra od $dis_2(b, j) + dis_1(a, j)$.</p>
'''),
        ('Opažanje 2: spajanje dijametara',
         r'''
<p>Dijametar unije dvaju skupova vrhova ima krajeve među $4$ kraja dijametara dijelova — $6$ kandidatskih parova, svaki u $O(1)$ s LCA preko Eulerova obilaska + sparse table. Zato dijametar možemo držati u segmentnom stablu.</p>
'''),
        ('Redukcija: offline po $a$',
         r'''
<p>Grupiraj upite po $a$ i obiđi prvo stablo DFS-om. Prelazak $a \to v$ (dijete, brid $w$): $dis_1$ za sve $j$ u podstablu od $v$ pada za $w$, a za ostale raste za $w$. Pomak cijelog skupa za konstantu ne mijenja krajeve dijametra; mijenjaju se samo čvorovi segmentnog stabla koji „razdvajaju” DFS interval podstabla — $O(\log n)$ čvorova, svaki se ponovno spaja iz djece.</p>
'''),
        ('Složenost',
         r'''
<p>$O(n \log n)$ za sva ažuriranja i $O(1)$ po upitu (čitanje korijena): $O(n \log n + q)$.</p>
'''),
    ],
    'solution': r'''
<p>Udaljenost vrhova $u$ i $v$ u prvom stablu označimo s $dis_1(u, v)$, a u drugom stablu s $dis_2(u, v)$. Za upit $(a, b)$ tražimo $\max_j \left( dis_1(a, j) + dis_2(b, j) \right)$.</p>
<p>Upite rješavamo offline. Obilazimo prvo stablo DFS-om po vrhu $a$ iz upita. Zamislimo da u drugom stablu na svaki vrh $j$ objesimo novi vrh $j'$ bridom težine $dis_1(a, j)$. Problem se tada svodi na sljedeće: u novom stablu, dobivenom dodavanjem tih vrhova drugom stablu, pronaći vrh najudaljeniji od $b$ — a to je uvijek jedan od krajeva (bilo kojeg) dijametra novog stabla.</p>
<p>Razmotrimo kako održavati dijametar novog stabla. Nad DFS poretkom prvog stabla izgradimo segmentno stablo; svaki čvor segmentnog stabla čuva dijametar skupa vrhova drugog stabla koji odgovaraju vrhovima $i$ čiji DFS indeks pada u interval tog čvora (čuvamo krajeve dijametra, a ne njegovu duljinu). Kada se $a$ pomiče po prvom stablu (prelazi na dijete ili natrag na roditelja), vrijednosti $dis_1(a, i)$ za sve $i$ unutar nekog DFS intervala (podstabla) mijenjaju se za istu konstantu, a za sve $i$ izvan tog intervala za drugu konstantu. Dovoljno je stoga spustiti se segmentnim stablom duž tog DFS intervala i pritom ponovno izračunati dijametre pogođenih čvorova (spajanjem dijametara djece); u intervalima koji nisu pogođeni sve se vrijednosti $dis_1(a, i)$ mijenjaju za istu konstantu, što ne mijenja dijametar. Za upit $(a, b)$ pročitamo dijametar novog stabla iz korijena, za oba kraja $j'$ izračunamo $dis_1(a, j) + dis_2(b, j)$ preko odgovarajućih $j$ i ažuriramo odgovor.</p>
<p>Za upite LCA, a time i duljine putova u stablima, koristimo Eulerov obilazak (DFS poredak) i ST tablicu (sparse table), pa je ukupna vremenska složenost $O(n \log n + q)$.</p>
''',
},
{
    'letter': 'H',
    'title': 'P-P-Palindrome',
    'title_hr': 'P-P-Palindrom',
    'slug': 'H_p_p_palindrome',
    'tl': '3 s',
    'ml': '512 MB',
    'statement': r'''
<p>Zadano je $n$ nizova $S_1, S_2, \dots, S_n$. Izračunaj broj različitih P-P-palindroma određenih tim nizovima.</p>
<p>Palindrom je niz koji se čita jednako slijeva nadesno i zdesna nalijevo (npr. <code>a</code>, <code>level</code>, <code>otto</code>). <b>P-P-palindrom</b> je uređeni par nepraznih palindroma $(P, Q)$ takvih da su i $P$ i $Q$ podnizovi nekih od nizova $S_1, \dots, S_n$, a $P + Q$ (konkatenacija $P$ pa $Q$) također je palindrom. Dva P-P-palindroma su različita ako se razlikuju u $P$ ili u $Q$.</p>
<h3>Ulaz</h3>
<p>Prvi redak sadrži $n$ ($1 \le n \le 10^6$). Slijedi $n$ redaka s nizovima $S_i$ ($1 \le |S_i| \le 10^6$) od malih slova engleske abecede. Ukupna duljina svih nizova ne prelazi $10^6$.</p>
<h3>Izlaz</h3>
<p>Ispiši broj različitih P-P-palindroma.</p>
<h3>Primjer</h3>
<p>Za nizove <code>aaaa</code> i <code>aaa</code> odgovor je $16$. Za nizove <code>abaaa</code>, <code>abbbba</code>, <code>bbbaba</code> odgovor je $28$.</p>
''',
    'hints': [
        r'''
<p>Ako je $P + Q$ palindrom, $P$ i $Q$ palindromi, tada su $P$ i $Q$ potencije istog najmanjeg perioda $R$ (i $R$ je palindrom). Zaključak: parovi su točno parovi palindroma s istim najmanjim periodom.</p>
''',
        r'''
<p>Izdvoji sve različite palindromske podnizove (eertree ili Manacher), svakom odredi najmanji period (najmanji palindromski border čija duljina dijeli duljinu) i grupiraj: grupa veličine $c$ daje $c^2$ parova.</p>
''',
    ],
    'coach': [
        ('Opažanje 1: borderi palindroma',
         r'''
<p>Border palindroma (istodobno prefiks i sufiks) također je palindrom. Ako je $PQ$ palindrom s $|P| \le |Q|$, $P$ je border od $Q$ pa $Q$ ima period $|P|$; nastavljanjem argumenta $P$ i $Q$ imaju isti najmanji period $R$, koji je i sam palindrom.</p>
'''),
        ('Opažanje 2: obrat',
         r'''
<p>Ako su $P = R^a$ i $Q = R^b$ s palindromom $R$, tada je $PQ = R^{a+b}$ palindrom. Dakle broj P-P-palindroma je $\sum_R c_R^2$, gdje je $c_R$ broj različitih palindromskih podnizova čiji je najmanji period $R$.</p>
'''),
        ('Algoritam',
         r'''
<p>Palindromsko stablo (eertree) nad svim nizovima (razdvojenima) daje sve različite palindromske podnizove, ukupno $O(\sum |S_i|)$. Za svaki palindrom čvora obradi po duljini rastuće: najmanji period je najmanji palindromski border $B$ s $|B| \mid L$ (prati lanac sufiks-linkova ili koristi hashiranje), inače cijeli palindrom. Grupiraj po hashu perioda.</p>
'''),
        ('Složenost',
         r'''
<p>$O(\sum |S_i| \cdot \log)$ ili linearno s pažljivim hashiranjem; ukupna duljina $\le 10^6$.</p>
'''),
    ],
    'solution': r'''
<p>Koristimo činjenicu da je svaki <i>border</i> (istodobno prefiks i sufiks) palindroma također palindrom. Iz toga se može izvesti da dva palindromska podniza $P$ i $Q$ koja se mogu spojiti u P-P-palindrom nužno imaju isti <b>najmanji period</b> (najkraći niz $R$ takav da je palindrom oblika $R^k$). Budući da je period palindroma ujedno njegov border, i sam period je palindrom.</p>
<p>Ako palindrom ima najmanji period $R$ koji se ponavlja $k$ puta, tada su svi nizovi $R, R^2, R^3, \dots, R^k$ valjani palindromski podnizovi. Dakle, za svaki najmanji period $R$ potrebno je prebrojati koliko različitih palindromskih podnizova ima $R$ za najmanji period — ako ih je $c$, oni doprinose $c^2$ uređenih parova.</p>
<p>Manacherovim algoritmom ili palindromskim stablom (<i>eertree</i>) izdvojimo sve bitno različite palindromske podnizove, zatim npr. hashiranjem, obrađujući palindrome po duljini od najmanje prema najvećoj, odredimo najmanji period svakog od njih (najmanji period palindroma duljine $L$ jest njegov najmanji palindromski border čija duljina dijeli $L$, ili sam palindrom), te na kraju prebrojimo odgovor.</p>
''',
},
{
    'letter': 'I',
    'title': 'Quartz Collection',
    'title_hr': 'Skupljanje kvarca',
    'slug': 'I_quartz_collection',
    'tl': '2 s',
    'ml': '512 MB',
    'statement': r'''
<p>U trgovini u Bajtlandiji prodaje se $n$ vrsta kvarca. Od svake vrste dnevno su u prodaji samo dva komada, a drugi komad dolazi u prodaju tek nakon što je prvi prodan.</p>
<p>Čarobnjaci Alice i Bob skupljaju svih $n$ vrsta kvarca. Dogovorili su se da svatko od njih svaki dan kupi točno jedan komad svake vrste. Oboje žele minimizirati vlastiti trošak. Zbog pravednosti, Alice prvo kupi jedan komad, a zatim Bob i Alice naizmjence kupuju po dva komada dok ne ostane samo jedan komad; posljednji komad kupuje onaj tko još nema sve vrste.</p>
<p>U svakom od sljedećih $m$ dana trajno se mijenjaju cijene dvaju komada jedne vrste kvarca. Alice želi znati svoj minimalni trošak za skupljanje svih vrsta prvog dana i svakog od sljedećih $m$ dana, ako oboje igraju optimalno.</p>
<h3>Ulaz</h3>
<p>Prvi redak sadrži $n$ i $m$ ($1 \le n, m \le 10^5$). Slijedi $n$ redaka s cijenama $a$ i $b$ ($1 \le a, b \le 10^5$) prvog i drugog komada $i$-te vrste, zatim $m$ redaka s $t$, $x$, $y$: cijene komada $t$-te vrste postaju $x$ i $y$.</p>
<h3>Izlaz</h3>
<p>Ispiši $m + 1$ redaka — Alicein minimalni trošak prvog dana i nakon svake promjene.</p>
''',
    'hints': [
        r'''
<p>Zbroj svih cijena je fiksan, pa vrsta $i$ igraču koji je uzme <em>prvi</em> donosi „dobit” $b_i - a_i$ u odnosu na protivnika. Igra se svodi na to tko uzima koje vrijednosti $b_i - a_i$.</p>
''',
        r'''
<p>Sortiraj po $b_i - a_i$ silazno. Pozitivne vrijednosti oba igrača žele što prije; negativne što kasnije. Uz redoslijed poteza $1, 2, 2, 2, \dots$ raspored pozicija Alice/Bob je periodičan (period $4$) i ovisi samo o broju pozitivnih vrijednosti; drži zbrojeve po klasama pozicija u segmentnom stablu nad domenom vrijednosti.</p>
''',
    ],
    'coach': [
        ('Opažanje 1: preformulacija na dobiti',
         r'''
<p>Alice plaća $\sum(\text{ono što uzme})$; ukupno se plati $\sum(a_i + b_i)$. Za vrstu $i$ prvi kupac plati $a_i$, drugi $b_i$. Neka $d_i = b_i - a_i$: prvi kupac vrste $i$ „dobije” $d_i$ nad protivnikom. Alicein trošak $= \frac{1}{2}\bigl(\sum(a_i+b_i) - \sum_{i \in \text{Alice prva}} d_i + \sum_{i \in \text{Bob prvi}} d_i\bigr)$.</p>
'''),
        ('Opažanje 2: pohlepni poredak',
         r'''
<p>Optimalno: dok postoje $d_i \gt 0$, oba igrača uzimaju najveće preostale $d_i$; nakon toga oba igrača uzimaju „druge komade” (dobit $0$) kad god mogu, a negativne vrste ostavljaju protivniku — što prisiljava suprotnog igrača da prvi uzme najveći gubitak. Uz potez-uzorak $1, 2, 2, \dots$ dobiva se fiksni periodični raspored: u sortiranom poretku pozitivnih vrijednosti Alice uzima pozicije $\equiv 1, 0 \pmod 4$ (1., 4., 5., 8., …), a negativne se dijele od najmanje prema većoj po analognom uzorku koji ovisi o parnosti broja pozitivnih.</p>
'''),
        ('Algoritam',
         r'''
<p>Segmentno stablo nad domenom vrijednosti $d \in [-10^5, 10^5]$ (ili offline nad svim vrijednostima); svaki čvor čuva broj elemenata i zbrojeve elemenata po pozicijama modulo $4$ unutar čvora — spajanje djece pomiče ostatke lijevog djeteta. Ažuriranje cijene je brisanje + umetanje, upit čita korijen: $O(\log)$ po danu.</p>
'''),
        ('Složenost',
         r'''
<p>$O((n + m)\log V)$.</p>
'''),
    ],
    'solution': r'''
<p>Zbroj svih cijena je fiksan, pa možemo gledati da za svaku vrstu kvarca igrač koji je kupi <i>prvi</i> ostvaruje "dobit" $b_i - a_i$ (u odnosu na drugog), a igrač koji je kupi drugi ima dobit $0$; svaki igrač želi maksimizirati zbroj svojih dobiti.</p>
<p>Očito, za vrste s pozitivnom dobiti oba igrača žele što ranije uzeti one s najvećom dobiti; za vrste s negativnom dobiti oba igrača žele što kasnije uzeti (tj. prepustiti protivniku) one s najvećim gubitkom.</p>
<p>Nakon sortiranja po $b_i - a_i$ silazno može se točno odrediti koje pozicije u tom poretku uzima Alice, a koje Bob (pozicije se raspoređuju po fiksnom periodičnom uzorku koji ovisi samo o redoslijedu poteza $1, 2, 2, 2, \dots$ i o broju pozitivnih vrijednosti). Promjene cijena održavamo segmentnim stablom nad domenom vrijednosti (ili balansiranim binarnim stablom) koje za svaku klasu pozicija čuva zbroj vrijednosti, pa svaki upit odgovaramo u $O(\log)$.</p>
''',
},
{
    'letter': 'J',
    'title': 'Referee Without Red',
    'title_hr': 'Sudac bez crvenog',
    'slug': 'J_referee_without_red',
    'tl': '3 s',
    'ml': '512 MB',
    'statement': r'''
<p>Plesna skupina raspoređena je u matricu s $n$ redaka i $m$ stupaca. Vrsta svakog plesača označena je prirodnim brojem ne većim od $3 \times 10^6$; više plesača može biti iste vrste. Dva rasporeda su različita ako postoji pozicija na kojoj se vrste plesača razlikuju.</p>
<p>Voditelj Referee pokazuje karte:</p>
<ul>
    <li>Bijela karta s brojem $k$ ($1 \le k \le n$): plesači u $k$-tom retku odbroje $1, 2, \dots, m$ slijeva nadesno; oni koji su izgovorili paran broj odmah odlaze na desni kraj retka (zadržavajući međusobni redoslijed), a zatim se svi poravnaju.</li>
    <li>Crna karta s brojem $k$ ($1 \le k \le m$): plesači u $k$-tom stupcu odbroje $1, 2, \dots, n$ sprijeda prema natrag; oni s parnim brojem odlaze na stražnji kraj stupca.</li>
</ul>
<p>Referee može pokazivati karte proizvoljno mnogo puta (moguće nijednom). Izračunaj broj različitih rasporeda koje može dobiti, modulo $998\,244\,353$.</p>
<h3>Ulaz</h3>
<p>Prvi redak sadrži broj testnih primjera $T$ ($1 \le T \le 10^5$). Za svaki primjer: $n$ i $m$ ($2 \le n, m \le 10^6$), zatim $n$ redaka po $m$ brojeva $a_{i,j}$ ($1 \le a_{i,j} \le 3 \times 10^6$). Zbroj $n \times m$ po svim primjerima ne prelazi $3 \times 10^6$.</p>
<h3>Izlaz</h3>
<p>Za svaki primjer ispiši broj različitih rasporeda modulo $998\,244\,353$.</p>
''',
    'hints': [
        r'''
<p>Karta na retku primjenjuje fiksnu permutaciju stupaca (isto za sve retke); rastavi je na cikluse. Preimenovanjem stupaca ciklusi postaju uzastopne grupe, a karta = istodobni ciklički pomak unutar svake grupe. Isto za stupce. Matrica se dijeli na $n' \times m'$ ploča.</p>
''',
        r'''
<p>Ploče visine ili širine $1$: ciklički pomak u jednom smjeru, broj rasporeda = najmanji period (KMP), a zajedno LCM perioda. Za veće ploče: pomaci u sva $4$ smjera daju „L-rotaciju” tri elementa, pa ploča s ponovljenim brojevima postiže sve rasporede, a ploča s različitim brojevima sve rasporede iste parnosti — parnost se mijenja pomakom parnog broja elemenata, sinkrono za cijelu grupu.</p>
''',
    ],
    'coach': [
        ('Opažanje 1: grupe i ploče',
         r'''
<p>Bijela karta na retku $k$ primjenjuje permutaciju $\pi$ na $m$ pozicija; crna na stupcu permutaciju $\sigma$ na $n$ pozicija. Elementi se kreću unutar orbita (ciklusa) — preimenuj tako da ciklusi budu uzastopni. Sada operacija = ciklički pomak jedne grupe stupaca unutar jednog retka (odn. grupe redaka unutar stupca). Presjek grupe redaka i grupe stupaca je ploča; brojevi nikad ne napuštaju ploču.</p>
'''),
        ('Opažanje 2: „tanke” ploče',
         r'''
<p>Ploča visine $1$ (grupa redaka veličine $1$) može se samo ciklički pomicati po stupcima, i to sinkrono sa svim ostalim pločama istog retka koje pripadaju istoj grupi stupaca. Broj različitih stanja jedne takve ploče je njezin najmanji period (KMP); više ploča koje se pomiču zajedno daje LCM perioda.</p>
'''),
        ('Opažanje 3: parnost kod „debelih” ploča',
         r'''
<p>Inverz pomaka dobiva se ponavljanjem, pa su dostupni pomaci u sva $4$ smjera. Kombinacijom se dobije rotacija tri ćelije u obliku slova L, čime se svaki element može dovesti na mjesto — do zadnja dva. Ploča s ponovljenim vrijednostima zato postiže sve rasporede (permutacije s ponavljanjem); ploča s različitim vrijednostima sve rasporede iste parnosti (polovica $s!$). Parnost ploče mijenja pomak koji pomiče paran broj elemenata — grupa parne veličine — i to sinkrono za sve ploče te grupe.</p>
'''),
        ('Algoritam: prebrojavanje parnosti',
         r'''
<p>Ploča „neparna × parna” grupa: parnost joj se može mijenjati, ali zajedno sa svim raznolikim pločama iste parne grupe — $2$ mogućnosti po takvoj grupi. Ploče „parna × parna”: graf s virtualnim vrhom po parnoj grupi i bridom po raznolikoj ploči; parnosti se mogu birati neovisno na razapinjućoj šumi: $2^{\#\text{bridova šume}}$. Pomnoži sve: LCM tankih ploča $\times$ $2^{\cdots}$ $\times$ $\prod$ (permutacije s ponavljanjem / pola permutacija).</p>
'''),
        ('Složenost',
         r'''
<p>$O(nm)$ po testu uz KMP i DSU.</p>
'''),
    ],
    'solution': r'''
<p>Permutacija koju bijela karta primjenjuje na redak rastavlja se na nekoliko ciklusa. Zato možemo prerasporediti (preimenovati) stupce tako da stupci iz istog ciklusa budu uzastopni i čine jednu <b>grupu</b>; tada je primjena permutacije ekvivalentna istodobnom cikličkom pomaku unutar svake grupe. Analogno vrijedi za permutaciju koju crna karta primjenjuje na stupce. Neka redci imaju $n'$ grupa, a stupci $m'$ grupa; nova matrica se time dijeli na $n' \times m'$ pravokutnih <b>ploča</b>.</p>
<p>Počnimo od grupa veličine $1$: ploče koje ih uključuju imaju visinu ili širinu $1$, pa se različiti rasporedi mogu dobiti samo cikličkim pomakom u jednom smjeru. Broj rasporeda jedne takve ploče jednak je njezinu najmanjem periodu, koji se može izračunati KMP algoritmom; broj rasporeda svih tih ploča zajedno je najmanji zajednički višekratnik (LCM) tih perioda.</p>
<p>Za ploče kojima su i visina i širina veće od $1$, ploču nazivamo <b>raznolikom</b> ako su svi brojevi u njoj međusobno različiti, a inače <b>neraznolikom</b>. Uočimo:</p>
<ul>
    <li>Brojevi jedne ploče nikada ne mogu prijeći u drugu ploču.</li>
    <li>Višestrukom primjenom permutacije dobivamo i njezin inverz, pa ciklički pomaci postoje u sva četiri smjera: gore, dolje, lijevo i desno.</li>
    <li>Definirajmo parnost raznolike ploče kao parnost broja inverzija niza dobivenog čitanjem svih brojeva na fiksan način (npr. redak po redak odozgo prema dolje). Zamjena bilo koja dva broja mijenja parnost, pa jedan ciklički pomak mijenja parnost ako i samo ako pomiče paran broj elemenata.</li>
</ul>
<p>Stoga možemo naslutiti: raznolika ploča može, bez mijenjanja ostalih ploča, poprimiti bilo koji raspored iste parnosti, a neraznolika ploča može poprimiti bilo koji raspored. Dokaz je konstruktivan: nizom pomaka ostvarimo "L-oblikovanu" rotaciju triju brojeva (orijentacija slova L i smjer rotacije ovise o redoslijedu operacija), pa brojeve jedan po jedan vraćamo na mjesto dok ne ostanu samo dva.</p>
<p>U cjelini: najprije nizom cikličkih pomaka "zaključamo" parnost svake raznolike ploče, a zatim uređujemo raspored unutar svake ploče. Ako je visina ili širina ploče parna, parnost raznolike ploče može se mijenjati, ali budući da se ciklički pomaci grupe primjenjuju sinkrono na sve ploče u istom retku odnosno stupcu grupa, parnost ostalih ploča iste grupe može se pritom promijeniti.</p>
<ul>
    <li>Primjerice, ploče nastale presjekom grupe neparne veličine i grupe parne veličine mogu mijenjati parnost samo istodobno, pa za njih postoje $2$ mogućnosti.</li>
    <li>Nadalje, svakoj grupi parne veličine pridružimo virtualni vrh; svaka raznolika ploča nastala presjekom dviju takvih grupa odgovara bridu između odgovarajućih virtualnih vrhova. Broj mogućih rasporeda parnosti tih ploča tada je $2$ na potenciju broja bridova u razapinjućoj šumi tog grafa.</li>
</ul>
<p>Primjenom pravila umnoška posebno prebrojimo globalne mogućnosti parnosti, a zatim kombinatorno izračunamo broj rasporeda unutar svake ploče (permutacije s ponavljanjem za neraznolike ploče, odnosno polovica permutacija za raznolike ploče) i sve pomnožimo u konačan odgovor. Vremenska složenost može biti $O(nm)$.</p>
''',
},
{
    'letter': 'K',
    'title': 'Security at Museums',
    'title_hr': 'Sigurnost u muzejima',
    'slug': 'K_security_at_museums',
    'tl': '1 s',
    'ml': '512 MB',
    'statement': r'''
<p>Muzej je modeliran kao jednostavan poligon, a na svakom vrhu poligona nalazi se jedno umjetničko djelo. Skupina lopova odabrala je barem dva djela koja će istodobno krasti. Zbog sigurnosti su djela odabrali tako da se svaka dva lopova međusobno vide: svaka točka dužine između njih leži u unutrašnjosti ili na rubu muzeja.</p>
<p>Izračunaj broj različitih skupova djela koje lopovi mogu odabrati, modulo $998\,244\,353$.</p>
<h3>Ulaz</h3>
<p>Prvi redak sadrži $n$ ($3 \le n \le 200$) — broj vrhova poligona. Slijedi $n$ redaka s koordinatama $x$, $y$ ($-10^6 \le x, y \le 10^6$) vrhova u smjeru suprotnom od kazaljke na satu. Poligon je jednostavan (nema samopresjeka), a nikoja dva uzastopna brida nisu kolinearna.</p>
<h3>Izlaz</h3>
<p>Ispiši broj skupova modulo $998\,244\,353$.</p>
<h3>Primjer</h3>
<p>Za trokut su valjani svi skupovi s barem dva vrha, pa je odgovor $4$.</p>
''',
    'hints': [
        r'''
<p>Skup vrhova je valjan ako i samo ako su svi parovi međusobno vidljivi; može se pokazati da tada unutrašnjost njihove konveksne ljuske ne sadrži nijedan drugi vrh poligona. Prvo u $O(n^3)$ za svaki par odredi vidljivost (dužina ne siječe strogo nijedan brid; podijeli je vrhovima koji leže na njoj i provjeri polovišta).</p>
''',
        r'''
<p>Fiksiraj najniži (leksikografski najmanji) odabrani vrh $s$ i prebroji konveksne poligone (lance po rastućem polarnom kutu) sastavljene od vidljivih dužina među vrhovima $\ge s$: DP $dp_{i,j}$ = stigli smo u $j$ koristeći bridove $i \le 3$ različitih kutova (da razlikuješ degenerirane „kolinearne” skupove).</p>
''',
    ],
    'coach': [
        ('Opažanje 1: vidljivost para',
         r'''
<p>Dužina $uv$ leži u poligonu ako i samo ako ne siječe strogo nijedan brid i sve njezine „komadiće” između vrhova koji leže na njoj imaju polovište unutar poligona (ili na rubu). Rekurzivna podjela s memoizacijom: $O(n^3)$ ukupno.</p>
'''),
        ('Opažanje 2: struktura valjanog skupa',
         r'''
<p>Konveksna ljuska odabranih vrhova ne smije u unutrašnjosti sadržavati druge vrhove poligona (inače bi neka dijagonala izlazila iz poligona). Zato valjane skupove možemo prebrojavati kao konveksne poligone/lance čiji su svi bridovi vidljive dužine.</p>
'''),
        ('Redukcija: obilazak po polarnom kutu',
         r'''
<p>Fiksiraj $s$ = leksikografski najmanji vrh skupa; ostali vrhovi su $\ge s$. Sortiraj sve vidljive usmjerene dužine po polarnom kutu i nadovezuj ih u neopadajućem kutu počevši i završavajući u $s$ — svaki konveksni skup se tako dobije točno jednom, uz oprez kod kolinearnih točaka: dopusti ili samo jedan kut (skup na pravcu) ili barem tri različita kuta (pravi poligon), ne dva (odlazak i povratak).</p>
'''),
        ('Algoritam',
         r'''
<p>$dp_{i,j}$ = broj načina od $s$ do $j$ s $i \in \{1,2,3\}$ (3 znači $\ge 3$) različitih kutova. Obradi kutove grupirano (grupni ruksak); unutar grupe redoslijed po bridovima mora dopustiti nadovezivanje više bridova istog kuta. Ukupno $O(n^3)$ za sve $s$.</p>
'''),
        ('Složenost',
         r'''
<p>$O(n^3)$, $n \le 200$.</p>
'''),
    ],
    'solution': r'''
<p>Zadatak traži da odaberemo barem dva vrha jednostavnog poligona tako da dužina između svaka dva odabrana vrha u cijelosti leži unutar poligona (uključujući rub). Budući da je jednostavan poligon jednostavno povezano područje, može se pokazati da unutrašnjost konveksne ljuske odabranih vrhova (bez ruba) ne smije sadržavati nijedan drugi vrh poligona.</p>
<p>Najprije za svaki par vrhova u predobradi odredimo leži li spojnica unutar poligona. Ako se spojnica strogo siječe s nekim bridom poligona, sigurno nije unutar poligona. Inače, ako se u unutrašnjosti spojnice nalazi neki vrh poligona, njime rekurzivno podijelimo spojnicu na dva dijela i nastavimo, sve dok u unutrašnjosti dijela više nema vrhova; tada je dovoljno provjeriti nalazi li se polovište tog dijela unutar poligona. Uz memoizaciju, složenost ovog dijela je $O(n^3)$.</p>
<p>Zatim fiksiramo odabrani vrh s leksikografski najmanjim koordinatama $(x, y)$ i ne razmatramo vrhove s manjim koordinatama. Sve valjane spojnice među preostalim vrhovima sortiramo po polarnom kutu. Ako biramo spojnice u neopadajućem poretku polarnog kuta i nadovezujemo ih jednu na drugu (kraj jedne je početak sljedeće), dobivamo konveksnu ljusku, a njezini vrhovi čine jedno valjano rješenje. Zbog mogućih kolinearnih točaka, kako ne bismo isti skup brojali više puta (odlaskom "tamo i natrag"), zahtijevamo da se ili biraju bridovi samo jednog polarnog kuta, ili bridovi barem tri različita polarna kuta.</p>
<p>Nakon što sve bridove unaprijed sortiramo po polarnom kutu, za svaki početni vrh $s$ računamo $dp_{i,j}$ — broj načina da iz $s$ dođemo u $j$ koristeći bridove $i$ različitih polarnih kutova, gdje je dovoljno pamtiti $i$ samo do $3$. Prijelaze radimo kao grupni ruksak (bridovi grupirani po polarnom kutu), pri čemu treba paziti na redoslijed obrade bridova unutar iste grupe kako ne bismo propustili rješenja koja koriste više bridova iz iste grupe zaredom. Složenost ovog dijela također je $O(n^3)$.</p>
''',
},
{
    'letter': 'L',
    'title': 'Tavern Chess',
    'title_hr': 'Tavern Chess',
    'slug': 'L_tavern_chess',
    'tl': '4 s',
    'ml': '512 MB',
    'statement': r'''
<p>Alice i Bob igraju igru "Tavern Chess" u kojoj svaki igrač sastavlja tim od najviše $7$ slugu (<i>minions</i>). Svaki sluga ima bodove života (HP) i napad (ATK), pri čemu je HP na početku jednak ATK-u. Sluga s pozitivnim HP-om je živ; umire čim mu HP nakon napada padne na nulu ili niže.</p>
<p>Borba traje dok svi sluge jednog tima ne umru — tada drugi tim pobjeđuje. Ako posljednji živi sluge oba tima umru istodobno, borba završava neriješeno.</p>
<p>Timovi napadaju naizmjence; prvi napada tim s više slugu, a u slučaju jednakog broja bacanjem novčića (50 % : 50 %). Kada tim napada, napada njegov <b>najljeviji</b> sluga među onima koji su dosad napadali <b>najmanje puta</b>, i to uniformno slučajno odabranog živog slugu protivničkog tima; zatim napada drugi tim. Kada sluga s $(h_1, a_1)$ napadne slugu s $(h_2, a_2)$, oba nanose štetu jednaku svom ATK-u: napadač ostaje s $h_1 - a_2$, a napadnuti s $h_2 - a_1$ HP-a.</p>
<p>Za zadane timove izračunaj vjerojatnosti da pobijedi Alice, da pobijedi Bob i da borba završi neriješeno.</p>
<h3>Ulaz</h3>
<p>Prvi redak sadrži $n$ i $m$ ($1 \le n, m \le 7$). Drugi redak sadrži $a_1, \dots, a_n$, a treći $b_1, \dots, b_m$ ($1 \le a_i, b_i \le 10^9$) — HP (i ATK) slugu slijeva nadesno.</p>
<h3>Izlaz</h3>
<p>Ispiši tri realna broja: vjerojatnosti Aliceine pobjede, Bobove pobjede i neriješenog ishoda. Apsolutna greška ne smije prelaziti $10^{-9}$.</p>
''',
    'hints': [
        r'''
<p>HP = ATK na početku, pa u svakom sudaru barem jedan sluga umire (onaj s manjim HP-om prima štetu $\ge$ svom HP-u). Broj slugu pada svakim napadom: igra traje najviše $n + m - 1$ napada.</p>
''',
        r'''
<p>Stanje: živi sluge s HP-om, koliko je puta svaki napadao, tko je na potezu. Grananje po slučajnom cilju s jednakim vjerojatnostima, rekurzivno; broj stanja je malen ($\le (7!)^2$ po ocjeni službenog rješenja).</p>
''',
    ],
    'coach': [
        ('Opažanje: kratka borba',
         r'''
<p>Napadač $(h_1, a_1)$ vs. napadnuti $(h_2, a_2)$ s $h_i \le a_i$ (HP nikad ne raste, ATK je konstantan): onaj s manjim HP-om dobije barem toliko štete. Dakle svaki napad ubija barem jednoga.</p>
'''),
        ('Redukcija: potpuno pretraživanje',
         r'''
<p>Igra je stablo odluka samo slučajnosti (nema izbora igrača): tko napada je određen pravilima, cilj je uniforman među živim protivnicima. Vjerojatnost ishoda = zbroj po listovima umnožaka $\frac{1}{\#\text{živih}}$.</p>
'''),
        ('Algoritam',
         r'''
<p>Rekurzija sa stanjem (HP-ovi, brojači napada, tko je na potezu); prvi napadač: tim s više slugu, ili $\frac12/\frac12$. Dubina $\le 13$, grananje $\le 7$, ali svakim korakom nestaje sluga pa je ukupno stanja malo. Bez memoizacije prolazi.</p>
'''),
    ],
    'solution': r'''
<p>Pravila su preuzeta iz igre <i>Hearthstone Battlegrounds</i>. Svi sluge imaju početni HP jednak ATK-u, pa se lako vidi da pri svakom sudaru dvaju slugu barem jedan od njih pada: onaj s manjim (ili jednakim) HP-om prima štetu barem jednaku svom HP-u. Zato se ukupan broj slugu smanjuje pri svakom napadu i borba je kratka.</p>
<p>Rekurzivno obiđemo sva moguća stanja igre (koji su sluge živi, njihov preostali HP, koliko je puta svaki napadao i tko je na potezu), pri čemu se svaki slučajni izbor cilja grana s jednakim vjerojatnostima. Broj obiđenih stanja ne prelazi $(7!)^2$, što je dovoljno brzo.</p>
''',
},
{
    'letter': 'M',
    'title': 'Vulpecula',
    'title_hr': 'Vulpecula (Lisica)',
    'slug': 'M_vulpecula',
    'tl': '5 s',
    'ml': '512 MB',
    'statement': r'''
<p>Zviježđe Vulpecula ima $n$ zvijezda numeriranih od $1$ do $n$, povezanih $n - 1$ zamišljenim linijama tako da tvore stablo; udaljenost dviju zvijezda je broj linija na putu između njih.</p>
<p>Mu fokusira teleskop na jednu zvijezdu i postavlja žarišnu udaljenost $d$ ($0 \le d \le n - 1$): vidi sve zvijezde čija udaljenost od fokusirane nije veća od $d$. Vidljivost $a_i$ zvijezde $i$ na početku je $0$. Filter $(i, x)$ odnosi se samo na zvijezdu $i$ i, kad se ugradi, $a_i$ postaje $a_i \oplus x$ ($\oplus$ je isključivo ILI po bitovima). Mu može ugraditi proizvoljan podskup svojih filtera u proizvoljnom redoslijedu (uključujući nijedan ili više jednakih).</p>
<p>Mu želi da sve zvijezde u vidnom polju imaju <b>jednaku i najveću moguću</b> vidljivost. Neka je $f(d)$ ta najveća vidljivost pri žarišnoj udaljenosti $d$. Za svaku zvijezdu kao fokusiranu izračunaj $\sum_{d=0}^{n-1} f(d)$ modulo $2^{64}$.</p>
<h3>Ulaz</h3>
<p>Prvi redak sadrži $n$ ($2 \le n \le 5 \times 10^4$). Drugi redak sadrži $p_1, \dots, p_{n-1}$ ($1 \le p_i \le i$): linija spaja zvijezde $p_i$ i $i + 1$. U $i$-tom od sljedećih $n$ redaka nalazi se $m_i$ ($m_i \ge 0$) i zatim $m_i$ brojeva $x_{i,j}$ ($0 \le x_{i,j} &lt; 2^{64}$) — filteri zvijezde $i$. Zbroj svih $m_i$ ne prelazi $2 \times 10^6$.</p>
<h3>Izlaz</h3>
<p>Ispiši $n$ redaka; $i$-ti sadrži traženi zbroj modulo $2^{64}$ ako je fokusirana zvijezda $i$.</p>
''',
    'hints': [
        r'''
<p>Za svaki vrh izgradi XOR-bazu njegovih filtera. $f(d)$ = najveći element <em>presjeka</em> baza svih vrhova na udaljenosti $\le d$. Presjek se s rastom $d$ samo smanjuje, mijenja se $\le \log W$ puta — ali presjeke je teško održavati izravno.</p>
''',
        r'''
<p>Presjek prostora = ortogonalni komplement unije komplemenata: $(A \cap B)^\perp = A^\perp + B^\perp$. Uniju baza po okolini je lako računati DP-om na stablu (svakom vektoru pridruži najmanji $d$ pri kojem ulazi). Maksimum prostora čitaj izravno iz ortogonalne baze pohlepno po bitovima, jer $x \in A, y \in A^\perp \Rightarrow |x \& y|$ paran.</p>
''',
    ],
    'coach': [
        ('Opažanje 1: preformulacija',
         r'''
<p>Vrijednost $a_i$ može biti bilo koji element XOR-prostora $V_i$ filtera vrha $i$. Zajednička vrijednost za sve vrhove u $d$-okolini: element $\bigcap V_j$; treba maksimum. Padajući lanac potprostora ima $\le 64$ promjene, pa je $\sum_d f(d)$ zbroj nekoliko članova pomnoženih duljinama „platoa”.</p>
'''),
        ('Opažanje 2: unija je lakša od presjeka',
         r'''
<p>Za uniju (zbroj) prostora po rastućoj okolini: DP na stablu koji za svaki vrh daje $\le 64$ vektora s „vremenom ulaska” $t$ (najmanji $d$ pri kojem vektor uđe u zbroj). Spajanje dviju takvih „vremenskih baza” zadržava po svakom vodećem bitu vektor s manjim vremenom (kao MST na vektorima) — $O(\log^2 W)$ po spajanju, ukupno $O(n \log^2 W)$ uz rerooting.</p>
'''),
        ('Redukcija: dualnost',
         r'''
<p>Opiši prostor indikatorom nad $\{0,1\}^{64}$; Walsh–Hadamard transformacija indikatora prostora $A$ je (do konstante) indikator komplementa $A^\perp$. XOR-konvolucija (zbroj prostora) prelazi u množenje po točkama (presjek komplemenata). Dakle $\bigcap V_j = \bigl(\sum V_j^\perp\bigr)^\perp$: presjek vrati na uniju komplemenata.</p>
'''),
        ('Algoritam: maksimum bez povratka u primarni prostor',
         r'''
<p>Računanje $A^\perp$ košta $O(\log^2 W)$; ne smijemo ga raditi za svaki $(v, d)$. Umjesto toga vektore komplementa drži u reduciranom obliku s vodećim bitom na <em>najnižoj</em> poziciji. Maksimum od $A$ gradi bit po bit od najvišeg: bit smije biti $1$ ako to ne krši uvjet „paran broj zajedničkih jedinica” sa svakim vektorom komplementa (eliminacijom odozdo uvjeti su neovisni). Zbroji po platoima modulo $2^{64}$ (prirodno prelijevanje <code>unsigned long long</code>).</p>
'''),
        ('Složenost',
         r'''
<p>$O\!\left(\sum m_i \cdot \log W + n \log^2 W\right)$.</p>
'''),
    ],
    'solution': r'''
<p>Za svaki vrh izgradimo <b>linearnu (XOR) bazu</b> koja opisuje skup vrijednosti koje se mogu dobiti XOR-anjem njegovih filtera. Tada za svaki vrh i svako $d$ treba odrediti <b>presjek</b> linearnih baza svih vrhova u $d$-okolini tog vrha u stablu i u njemu naći najveći element. Nije teško uočiti da se za fiksni vrh, kako $d$ raste, prostor razapet presjekom samo smanjuje (prelazi u potprostor) i mijenja se najviše $\log W$ puta, gdje je $W$ raspon vrijednosti. Problem je, međutim, kako održavati vektore baze koji se pri svakom smanjenju "odljepljuju" iz presjeka.</p>
<p>Razmotrimo srodan ("blizanački") problem: <b>uniju</b> linearnih baza u okolini vrha u stablu. Za svaki vektor baze dodatno održavamo vrijednost koja kaže koliko veliko mora biti $d$ da bi se taj vektor pridružio bazi; ako se vektor može dobiti XOR-anjem filtera samog promatranog vrha, ta vrijednost je $0$. Dinamičkim programiranjem po stablu možemo u složenosti $O(n \log^2 W)$ za svaki vrh dobiti svih $O(\log W)$ vektora koji se pridružuju bazi te trenutke u kojima se pridružuju. Upiti najveće vrijednosti nad svim tim bazama također ukupno stanu u $O(n \log^2 W)$.</p>
<p>Možemo li "odljepljivanje" pretvoriti u "pridruživanje"? Opišimo linearnu bazu formalnim redom potencija nad skupovima (<i>set power series</i>) čiji je $x$-ti koeficijent $1$ odnosno $0$ ovisno o tome je li $x$ u linearnom prostoru ili nije. Red potencija $C$ unije dviju linearnih baza $A$ i $B$ jednak je XOR-konvoluciji njihovih redova podijeljenoj konstantom koja ovisi o dimenzijama baza; zapisujemo $C = \frac{1}{k}(A \oplus B)$, odnosno $\mathrm{FWT}(C) = \frac{1}{k}\left(\mathrm{FWT}(A) * \mathrm{FWT}(B)\right)$, gdje je $*$ množenje po točkama, a FWT brza Walsh–Hadamardova transformacija. Uočimo da $\mathrm{FWT}(A)$ zapravo opisuje <b>ortogonalni komplement</b> od $A$; označimo linearnu bazu tog komplementa s $A^\perp$ (ortogonalna baza). Množenje po točkama tada zapravo računa presjek $A^\perp$ i $B^\perp$. Obratno, presjek više linearnih baza ekvivalentan je uniji njihovih ortogonalnih baza — čime smo problem sveli na blizanački problem.</p>
<p>Računanje ortogonalne baze košta $O(\log^2 W)$, pa pri upitima ne možemo za svaku okolinu ortogonalnu bazu "vraćati" natrag u običnu. Umjesto toga, u ortogonalnoj bazi svaki vektor pohranimo u obliku s vodećim bitom na najnižoj poziciji (eliminacijom od najnižeg bita). Koristeći svojstvo $x \in A,\ y \in A^\perp \Rightarrow |x \,\&amp;\, y| \bmod 2 = 0$ (broj zajedničkih jedinica je paran), najveći element prostora $A$ možemo pohlepno graditi bit po bit izravno u ortogonalnom smislu. Ukupna vremenska složenost je $O(n \log^2 W)$.</p>
''',
},
]
