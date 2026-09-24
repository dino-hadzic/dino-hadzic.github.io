"""1st Universal Cup – Stage 4: Ukraine. Uvezeno iz ručno pisanih stranica (import_legacy.py); naputci i
trenerski koraci iz nekadašnjeg retro_stage4.py."""

STAGE = {
    'no': 4,
    'name': 'Stage 4: Ukraine',
    'source_name': '1st OCPC, Winter 2023, Day 1: Anton Trygub Contest 1',
    'source_html': r'''
<p>Prijevod službenog rješenja autora Antona Tryguba: <a href="https://contest.ucup.ac/download.php?type=attachments&amp;id=1106&amp;r=1">Tutorial (en)</a>. Tekst zadatka preveden je prema službenim <a href="https://contest.ucup.ac/download.php?type=attachments&amp;id=1106&amp;r=0">engleskim tekstovima zadataka</a>. Zadatak je dostupan na <a href="https://contest.ucup.ac/contest/1106">Universal Cup Judging System</a>.</p>
''',
}

PROBLEMS = [
{
    'letter': 'A',
    'title': 'Adjacent Product Sum',
    'title_hr': 'Zbroj umnožaka susjeda',
    'slug': 'A_adjacent_product_sum',
    'tl': '1 s',
    'ml': '256 MB',
    'statement': r'''
<p>Zadano je $n$ brojeva $a_1, \dots, a_n$. Rasporedi ih u krug tako da zbroj umnožaka susjednih parova $b_1 b_2 + b_2 b_3 + \dots + b_{n-1} b_n + b_n b_1$ bude najveći mogući, i ispiši tu vrijednost.</p>
<h3>Ulaz</h3>
<p>Prvi redak sadrži $t$ ($1 \le t \le 10^4$). Za svaki primjer: $n$ ($3 \le n \le 2 \cdot 10^5$) i $a_1, \dots, a_n$ ($-10^6 \le a_i \le 10^6$). Zbroj svih $n$ ne prelazi $2 \cdot 10^5$.</p>
<h3>Izlaz</h3>
<p>Za svaki primjer ispiši najveću moguću vrijednost izraza (odgovor ne mora stati u 32-bitni tip).</p>
''',
    'hints': [
        r'''
<p>Zamjenska nejednakost: za $a \ge b$, $c \ge d$ vrijedi $ac + bd \ge ad + bc$. Veliki brojevi „žele” biti susjedi velikima.</p>
''',
        r'''
<p>Sortiraj silazno i rasporedi: $a_1, a_3, a_5, \dots$ pa natrag $\dots, a_6, a_4, a_2$ (dvije „padine” s vrhom u $a_1$). Dokaz indukcijom obrtanjem luka kruga.</p>
''',
    ],
    'coach': [
        ('Opažanje 1: lokalna zamjena',
         r'''
<p>Obrtanje luka kruga između dva susjedna para mijenja samo dva umnoška: ako su $x$ i $y$ susjedi te $u$ i $v$ susjedi, obrat luka daje $xu + yv$ umjesto $xy + uv$ (ili slično). Nejednakost $(a-b)(c-d) \ge 0$ govori kad je to isplativo.</p>
'''),
        ('Opažanje 2: struktura optimuma',
         r'''
<p>Indukcijom: postoji optimum u kojem $a_1, \dots, a_k$ čine luk s $a_{k-1}$ i $a_k$ na krajevima. Novi element $a_{k+1}$ lijepi se na manji kraj luka; to daje raspored „neparni indeksi u jednom smjeru, parni u drugom”.</p>
'''),
        ('Algoritam i složenost',
         r'''
<p>Sortiraj, složi $a_1, a_3, \dots$ pa $\dots, a_4, a_2$, zbroji umnoške susjeda ciklički. $O(n \log n)$, 64-bitni rezultat (do $2 \cdot 10^5 \cdot 10^{12}$).</p>
'''),
    ],
    'solution': r'''
<p>Neka je $a_1 \ge a_2 \ge \dots \ge a_n$. Pokazat ćemo da je jedan od optimalnih rasporeda na krugu:
$$a_1, a_3, \dots, a_{2\lfloor \frac{n-1}{2} \rfloor + 1},\ a_{2\lfloor \frac{n}{2} \rfloor}, \dots, a_4, a_2.$$
Drugim riječima, najprije stavimo sve elemente s neparnih pozicija, a zatim sve s parnih, u obrnutom poretku. Za $n = 7$ to je $(a_1, a_3, a_5, a_7, a_6, a_4, a_2)$.</p>
<p>Dokažimo optimalnost. Koristimo jednostavnu činjenicu: ako je $a \ge b$ i $c \ge d$, onda je $ac + bd \ge ad + bc$ (ekvivalentno s $(a - b)(c - d) \ge 0$).</p>
<p>Indukcijom pokazujemo da za svaki $k$ postoji optimalan raspored u kojem elementi $a_1, \dots, a_k$ tvore uzastopni segment, a $a_{k-1}$ i $a_k$ su na krajevima tog segmenta. Za $k = 2$: pretpostavimo da $a_1$ i $a_2$ nisu susjedni. Neka je $a_x$ element neposredno iza $a_1$ u smjeru kazaljke na satu, a $a_y$ neposredno iza $a_2$. Obrnemo cijeli podsegment od $a_x$ do $a_2$ (gledano u smjeru kazaljke). Zbroj se promijeni za $a_1 a_2 + a_x a_y - a_1 a_x - a_2 a_y \ge 0$.</p>
<p>Korak indukcije: uzmimo optimalan raspored u kojem tvrdnja vrijedi za $k - 1$; bez smanjenja općenitosti u tom segmentu $a_{k-2}$ je prvi, a $a_{k-1}$ zadnji element u smjeru kazaljke. Pretpostavimo da $a_k$ nije susjedan s $a_{k-2}$. Neka je $a_x$ element neposredno prije $a_{k-2}$ (suprotno od kazaljke; po izboru $x &gt; k$), a $a_y$ neposredno prije $a_k$ (po izboru $y \ge k - 1$). Obrnemo segment od $a_k$ do $a_x$ (u smjeru kazaljke). Zbroj se promijeni za $a_k a_{k-2} + a_x a_y - a_{k-2} a_x - a_k a_y$, što je nenegativno jer je $a_{k-2} \ge a_y$ i $a_k \ge a_x$.</p>
<p>Dakle, sortiramo elemente, rasporedimo ih na opisani način i izračunamo zbroj umnožaka.</p>
''',
},
{
    'letter': 'B',
    'title': 'Binary Arrays and Sliding Sums',
    'title_hr': 'Binarni nizovi i klizne sume',
    'slug': 'B_binary_arrays_and_sliding_sums',
    'tl': '1 s',
    'ml': '256 MB',
    'statement': r'''
<p>Za binarni niz $a_1, \dots, a_n$ (ciklički: $a_{n+i} = a_i$) definiramo $f(a)_i = a_i + a_{i+1} + \dots + a_{i+k-1}$. Promotrimo svih $2^n$ nizova $a$ i za svaki izračunamo $f(a)$. Koliko je različitih nizova među njima? Ispiši odgovor modulo $998\,244\,353$.</p>
<h3>Ulaz</h3>
<p>Prvi redak sadrži $t$ ($1 \le t \le 10^5$). Svaki primjer sadrži $n, k$ ($2 \le k &lt; n \le 10^6$).</p>
<h3>Izlaz</h3>
<p>Za svaki primjer ispiši broj različitih nizova $f(a)$ modulo $998\,244\,353$.</p>
''',
    'hints': [
        r'''
<p>$b = f(a)$ određuje razlike $a_{i+k} - a_i = b_{i+1} - b_i$. Indeksi se raspadaju na $g = \gcd(n,k)$ ciklusa duljine $n/g$ (koraci po $k$).</p>
''',
        r'''
<p>Ciklus s barem jednom nenul razlikom je jednoznačno određen; konstantan ciklus može biti sav $0$ ili sav $1$, a $b$ ovisi samo o <em>broju</em> jediničnih konstantnih ciklusa. Prebroji klase: $\sum_t (t+1)\binom{g}{t}(2^{n/g}-2)^{g-t} = (a+1)^g + g(a+1)^{g-1}$ za $a = 2^{n/g} - 2$.</p>
''',
    ],
    'coach': [
        ('Opažanje 1: što $b$ otkriva o $a$',
         r'''
<p>$b_{i+1} - b_i = a_{i+k} - a_i \in \{-1, 0, 1\}$; vrijednost $\pm1$ jednoznačno daje oba bita. Duž ciklusa $i, i+k, i+2k, \dots$ (duljina $n/g$) jedan poznat bit određuje sve; ciklus je neodređen samo ako su sve razlike $0$ — tada je konstantan.</p>
'''),
        ('Opažanje 2: konstantni ciklusi su zamjenjivi',
         r'''
<p>Svaki prozor duljine $k$ siječe svaki ciklus u točno $k/g$ pozicija. Zato $b$ ovisi samo o tome koliko je konstantnih ciklusa jediničnih, ne kojih. Klasa ekvivalencije nizova $a$ s istim $b$: nekonstantni ciklusi fiksni, konstantni ciklusi s fiksnim brojem $x$ jediničnih.</p>
'''),
        ('Redukcija: prebrojavanje klasa',
         r'''
<p>Odaberi $t$ konstantnih ciklusa ($\binom{g}{t}$), ostale popuni nekonstantno ($(2^{n/g} - 2)^{g-t}$), izaberi $x \in \{0..t\}$ ($t+1$). Zbroj $\sum_t (t+1)\binom{g}{t}a^{g-t}$ s identitetom $t\binom{g}{t} = g\binom{g-1}{t-1}$ daje $(a+1)^g + g(a+1)^{g-1}$.</p>
'''),
        ('Složenost',
         r'''
<p>$O(\log n)$ po testu (brzo potenciranje), $t \le 10^5$.</p>
'''),
    ],
    'solution': r'''
<p>Pogledajmo kako izgledaju nizovi $a$ s istim $f(a) = b$. Znamo $a_{i+k} - a_i = b_{i+1} - b_i$. Promotrimo elemente $a_i, a_{i+k}, a_{i+2k}, \dots$ dok se ne vratimo u $a_i$; duljina tog ciklusa je $\frac{n}{\gcd(n, k)}$.</p>
<p>Neka je $S$ skup indeksa u tom ciklusu. Ako za barem jedan $i \in S$ vrijedi $b_{i+1} - b_i \ne 0$, vrijednosti $a_i$ za sve $i \in S$ jednoznačno su određene (jer $a_j - a_i = 1$ samo kad je $a_j = 1, a_i = 0$, a $-1$ samo kad je $a_j = 0, a_i = 1$). Ako su svi ti $b_i$ jednaki, svi su $a_i$ u ciklusu jednaki, ali imamo dva izbora: sve nule ili sve jedinice.</p>
<p>Pretpostavimo da postoji $t$ ciklusa u kojima svi $a_i$ moraju biti jednaki. Ako $x$ od njih ispunimo jedinicama, a ostale nulama, zbroj na svakom segmentu duljine $k$ poveća se za $x \cdot \frac{k}{\gcd(n,k)}$ (svaki ciklus siječe svaki segment duljine $k$ u točno $\frac{k}{\gcd(n,k)}$ polja). Dakle, za dani $a$ svi nizovi $a'$ s $f(a') = f(a)$ izgledaju ovako:</p>
<ul>
    <li>promatramo svih $\gcd(n, k)$ ciklusa $(a_i, a_{i+k}, a_{i+2k}, \dots)$ za $i = 1, \dots, \gcd(n, k)$;</li>
    <li>ako u ciklusu nisu svi elementi jednaki, u $a'$ su oni isti kao u $a$;</li>
    <li>ako je $t$ ciklusa s jednakim elementima od kojih je $x$ sastavljeno od jedinica, u $a'$ su elementi u tim ciklusima također jednaki i točno $x$ ciklusa je od jedinica.</li>
</ul>
<p>Prebrojimo klase ekvivalencije. Neka je $l = \gcd(n, k)$ i neka $t$ ciklusa ima sve jednake elemente. Postoji $\binom{l}{t}$ načina odabira tih ciklusa i $2^{n/l} - 2$ načina popunjavanja svakog od ostalih ciklusa. Za $t$ "konstantnih" ciklusa bitno je samo koliko ih je od jedinica — $t + 1$ mogućnosti. Tražimo dakle
$$\sum_{t=0}^{l} (t + 1) \binom{l}{t} \left(2^{n/l} - 2\right)^{l-t}.$$
Označimo $a = 2^{n/l} - 2$. Uočimo $t \binom{l}{t} = \frac{l!}{(l-t)!\,(t-1)!} = l \binom{l-1}{t-1}$. Tada je
$$\sum_{t=0}^{l} (t+1)\binom{l}{t} a^{l-t} = \sum_{t=0}^{l} \binom{l}{t} a^{l-t} + l \sum_{t=1}^{l} \binom{l-1}{t-1} a^{l-t} = (a + 1)^l + l\,(a + 1)^{l-1}$$
(koristili smo $(x + 1)^k = \sum_{t=0}^{k} x^t \binom{k}{t}$). Svaki primjer rješavamo u $O(\log)$ brzim potenciranjem.</p>
''',
},
{
    'letter': 'C',
    'title': 'Count Hamiltonian Cycles',
    'title_hr': 'Brojanje Hamiltonovih ciklusa',
    'slug': 'C_count_hamiltonian_cycles',
    'tl': '1 s',
    'ml': '256 MB',
    'statement': r'''
<p>Zadan je niz $s$ duljine $2n$ s $n$ znakova <code>W</code> i $n$ znakova <code>B</code>. Graf ima $2n$ vrhova; ako je $s_i \ne s_j$, postoji brid težine $|i - j|$ između $i$ i $j$. Prebroji najkraće Hamiltonove cikluse modulo $998\,244\,353$ (dva ciklusa su različita ako se razlikuju u skupu bridova).</p>
<h3>Ulaz</h3>
<p>Prvi redak sadrži $t$ ($1 \le t \le 10^4$). Za svaki primjer: $n$ ($2 \le n \le 10^6$) i niz $s$. Zbroj svih $n$ ne prelazi $10^6$.</p>
<h3>Izlaz</h3>
<p>Za svaki primjer ispiši broj najkraćih Hamiltonovih ciklusa modulo $998\,244\,353$.</p>
''',
    'hints': [
        r'''
<p>Duljina ciklusa = zbroj po rezovima $i \mid i+1$ broja bridova koji prelaze rez. Preko reza prelazi paran broj bridova, barem $2\max(1, |W_i - B_i|)$ gdje su $W_i, B_i$ brojevi znakova u prefiksu. Sve se ograde postižu istodobno.</p>
''',
        r'''
<p>U optimalnom ciklusu prefiks $[1..i]$ inducira točno $|W_i - B_i|$ alternirajućih putova (ili jedan ako je razlika $0$). DP po prefiksima broji <em>orijentirane</em> cikluse (da bi spajanje putova bilo brojivo), odgovor podijeli s $2$.</p>
''',
    ],
    'coach': [
        ('Opažanje 1: donja ograda po rezovima',
         r'''
<p>Brid $(u,v)$ prelazi $|u - v|$ rezova; duljina ciklusa $= \sum_i x_i$ gdje je $x_i$ broj bridova preko reza $i$. Stupnjevi $2$ daju $x_i$ paran; bridova unutar prefiksa $\le 2\min(W_i, B_i)$ (bipartitno), pa $x_i \ge 2|W_i - B_i|$, a povezanost $x_i \ge 2$.</p>
'''),
        ('Opažanje 2: struktura pri jednakosti',
         r'''
<p>Ako je $W_i \gt B_i$, prefiks inducira točno $W_i - B_i$ putova oblika <code>WBW…BW</code> (svaki B unutra ima oba susjeda). Za $W_i = B_i$: jedan put <code>WB…WB</code>. Postizanje jednakosti u svim rezovima je istodobno moguće — to je karakterizacija najkraćih ciklusa.</p>
'''),
        ('Redukcija: orijentacija',
         r'''
<p>Dodavanje B kad je $W_i - B_i = d \ge 2$: B spaja krajeve dvaju putova (smanjuje broj putova za $1$). Bez orijentacije bi trebalo razlikovati putove duljine $1$ (jedan kraj) od duljih. S orijentiranim putovima biraš jedan „desni” i jedan „lijevi” kraj: $d(d-1)$ načina; za $d = 1$ lanac se produžuje na $2$ načina (početak ili kraj). Na kraju podijeli s $2$.</p>
'''),
        ('Algoritam i složenost',
         r'''
<p>Prijelazi: W kad $W \gt B$: $\times 1$ (novi put); B kad $W - B = d \ge 2$: $\times d(d-1)$; $d = 1$: $\times 2$; $W = B$ pa W/B: $\times 1$ (mora nastaviti jedini lanac). Simetrično za $B \gt W$. $O(n)$.</p>
'''),
    ],
    'solution': r'''
<p>Najprije izvedimo trivijalne donje ograde za duljinu najkraćeg ciklusa. Uzmimo poziciju $i$ ($1 \le i \le 2n - 1$) i neka su $left_W$, $left_B$ brojevi znakova <code>W</code>, <code>B</code> u $s[1 : i]$.</p>
<p>Neka Hamiltonov ciklus ima $x$ bridova koji spajaju $\{1, \dots, i\}$ s $\{i+1, \dots, 2n\}$. Stupanj svakog vrha u ciklusu je $2$, pa je broj bridova unutar $\{1, \dots, i\}$ jednak $\frac{2i - x}{2}$; dakle $x$ je paran. Broj bridova unutar $\{1, \dots, i\}$ ne može premašiti $2\min(left_W, left_B)$, pa
$$\frac{2i - x}{2} \le 2\min(left_W, left_B) \implies x \ge 2(left_W + left_B) - 4\min(left_W, left_B) = 2|left_W - left_B|.$$
Također $x \ne 0$ (inače graf ne bi bio povezan), pa $x \ge 2\max(1, |left_W - left_B|)$. Duljina ciklusa je upravo zbroj tih $x$ po svim $i$ (brid $(u, v)$ prelazi preko $|u - v|$ "rezova"). Pokazuje se da su sve te ograde istodobno dostižne, pa duljinu najkraćeg ciklusa dobijemo zbrajanjem ograda po svim $i$.</p>
<p>Nas zanima broj takvih ciklusa, pa analizirajmo strukturu ciklusa u kojima sve ograde vrijede s jednakošću. Lako se vidi:</p>
<ul>
    <li>ako je $left_W &gt; left_B$, graf na $\{1, \dots, i\}$ sastoji se od $left_W - left_B$ putova oblika <code>WBWB…BW</code>;</li>
    <li>ako je $left_B &gt; left_W$, od $left_B - left_W$ putova oblika <code>BWBW…WB</code>;</li>
    <li>ako je $left_B = left_W$, od jednog puta <code>WBWB…WB</code>.</li>
</ul>
<p>Ako to vrijedi za svaki $i$, sve ograde na broj bridova između $\{1, \dots, i\}$ i $\{i+1, \dots, 2n\}$ postižu se točno.</p>
<p>Neka $dp_i$ označava broj načina spajanja bridova na prvih $i$ vrhova tako da vrijede prvih $i$ uvjeta. Pretpostavimo $left_W &gt; left_B + 1$. Ako je sljedeći znak <code>W</code>, dodajemo put od jednog vrha. Ako je <code>B</code>, moramo smanjiti broj putova za $1$ spajajući <code>B</code> s krajevima dvaju putova. Tu nastaje problem: bitno je ima li put duljinu veću od $1$ (dva "različita" kraja) ili ne. Zato malo izmijenimo problem: brojimo <b>orijentirane</b> Hamiltonove cikluse, a rezultat na kraju podijelimo s $2$. Svi uvjeti ostaju isti, samo putovi postaju orijentirani.</p>
<p>Sada je prijelaz jednostavan: pri obradi <code>B</code> u gornjem slučaju ne biramo dva kraja, nego jedan desni i jedan lijevi kraj — točno $(left_W - left_B)(left_W - left_B - 1)$ načina. Ukratko:</p>
<ul>
    <li>$left_W &gt; left_B$: ako je sljedeći znak <code>W</code>, $dp_{i+1} = dp_i$. Ako je <code>B</code>: za $left_W &gt; left_B + 1$ je $dp_{i+1} = dp_i (left_W - left_B)(left_W - left_B - 1)$; za $left_W = left_B + 1$ je $dp_{i+1} = 2\,dp_i$ (dva načina produljenja lanca).</li>
    <li>$left_B &gt; left_W$: simetrično.</li>
    <li>$left_W = left_B$: bez smanjenja općenitosti sljedeći znak je <code>W</code>; moramo ga spojiti s jedinim crnim krajem lanca, pa $dp_{i+1} = dp_i$.</li>
</ul>
<p>Sve se računa u $O(n)$.</p>
''',
},
{
    'letter': 'D',
    'title': 'Distance Parities',
    'title_hr': 'Parnosti udaljenosti',
    'slug': 'D_distance_parities',
    'tl': '1 s',
    'ml': '256 MB',
    'statement': r'''
<p>Andrii je imao povezan graf s $n$ vrhova i za svaki par vrhova zapamtio samo parnost $a_{i,j} = d_{i,j} \bmod 2$ najkraće udaljenosti. Konstruiraj graf koji odgovara zadanim parnostima ili utvrdi da ne postoji.</p>
<h3>Ulaz</h3>
<p>Prvi redak sadrži $t$ ($1 \le t \le 10^4$). Za svaki primjer: $n$ ($2 \le n \le 500$) i $n$ binarnih nizova duljine $n$ (matrica $a$, simetrična, s nulama na dijagonali). Zbroj svih $n^2$ ne prelazi $250\,000$.</p>
<h3>Izlaz</h3>
<p>Za svaki primjer ispiši <code>NO</code>, ili <code>YES</code>, broj bridova $m$ i $m$ različitih bridova povezanog grafa.</p>
''',
    'hints': [
        r'''
<p>Ako rješenje postoji, jedno konkretno rješenje je: brid između svakog para s $a_{i,j} = 1$ (neparna udaljenost).</p>
''',
        r'''
<p>Zašto: parovi s parnom udaljenošću $2t$ imaju na najkraćem putu vrh $k$ s $d(k,i) = 1$, $d(k,j) = 2t-1$ — oba neparna, pa su $(k,i)$, $(k,j)$ bridovi i udaljenost postaje $2$. Provjeri konstruirani graf Floyd–Warshallom ili $n$ BFS-ova.</p>
''',
    ],
    'coach': [
        ('Opažanje 1: kanonski kandidat',
         r'''
<p>U svakom grafu s traženim parnostima, parovi s neparnom udaljenošću mogu se direktno spojiti bridom — parnost $1$ se čuva. Pitanje: pokvari li to parne parove?</p>
'''),
        ('Opažanje 2: parni parovi ostaju parni',
         r'''
<p>Za $d(i,j) = 2t$ neka je $k$ susjed $i$ na najkraćem putu do $j$: $d(k,i) = 1$, $d(k,j) = 2t - 1$ neparno, pa novi graf sadrži $(i,k)$ i $(k,j)$: $d'(i,j) \le 2$, a $\ne 1$ jer $a_{i,j} = 0$. Dakle $d'(i,j) = 2$, parno.</p>
'''),
        ('Algoritam i složenost',
         r'''
<p>Konstruiraj graf svih „neparnih” parova; provjeri povezanost i sve parnosti udaljenosti ($n$ BFS-ova, $O(n^3)$ uz $\sum n^2 \le 2.5 \cdot 10^5$). Ako ne odgovara, <code>NO</code>.</p>
'''),
    ],
    'solution': r'''
<p>Dodajmo brid između svakog para $i, j$ čija je udaljenost neparna. Pokažimo: ako postoji bilo koji graf s traženim parnostima, i ovaj graf zadovoljava uvjete.</p>
<p>Za $i, j$ s neparnom udaljenošću parnost se očito podudara (brid, udaljenost $1$). Za $i, j$ s parnom udaljenošću, recimo $2t$, na najkraćem putu između njih postoji vrh $k$ s $d(k, i) = 1$ i $d(k, j) = 2t - 1$. Dakle nacrtali smo bridove $(k, i)$ i $(k, j)$, pa je udaljenost između $i$ i $j$ u našem grafu $2$ — parnosti se podudaraju (a ne može biti $1$ jer $a_{i,j} = 0$).</p>
<p>Dakle: dodamo sve te bridove, provjerimo je li graf povezan i podudaraju li se sve parnosti. Složenost $O(n^3)$ Floyd–Warshallovim algoritmom (ili $n$ BFS-ova).</p>
''',
},
{
    'letter': 'E',
    'title': 'Excellent XOR Problem',
    'title_hr': 'Izvrstan XOR zadatak',
    'slug': 'E_excellent_xor_problem',
    'tl': '1 s',
    'ml': '256 MB',
    'statement': r'''
<p>Težina niza je XOR svih njegovih elemenata. Zadan niz $a_1, \dots, a_n$ treba podijeliti na više od jednog uzastopnog podniza tako da težine svih podnizova budu međusobno različite, ili utvrditi da to nije moguće.</p>
<h3>Ulaz</h3>
<p>Prvi redak sadrži $t$ ($1 \le t \le 10^4$). Za svaki primjer: $n$ ($2 \le n \le 2 \cdot 10^5$) i $a_1, \dots, a_n$ ($0 \le a_i &lt; 2^{30}$). Zbroj svih $n$ ne prelazi $2 \cdot 10^5$.</p>
<h3>Izlaz</h3>
<p><code>NO</code>, ili <code>YES</code>, broj dijelova $k$ ($2 \le k \le n$) i $k$ segmenata $l_i, r_i$ koji pokrivaju sve pozicije.</p>
''',
    'hints': [
        r'''
<p>Ako je XOR cijelog niza $X \ne 0$, bilo koja podjela na dva dijela radi (jednaki XOR-ovi dali bi $X = 0$).</p>
''',
        r'''
<p>Ako je $X = 0$, treba $3$ dijela: prvi završava na prvom nenul elementu $a_x$; ostatak podijeli na dva dijela s XOR-om $\notin \{0, a_x\}$. Ako ni jedna podjela ne uspije, svi su elementi u $\{0, a_x\}$ i rješenja nema.</p>
''',
    ],
    'coach': [
        ('Opažanje 1: dva dijela',
         r'''
<p>Podjela na dva dijela s XOR-ovima $p, q$: $p \oplus q = X$. Različiti $\iff X \ne 0$.</p>
'''),
        ('Opažanje 2: tri dijela kad je $X = 0$',
         r'''
<p>Uzmi prefiks do prvog nenul $a_x$ (XOR $a_x$). Ostatak ima XOR $a_x$; podjela ostatka na $(p, q)$ daje $p \oplus q = a_x \ne 0$ pa su $p \ne q$; treba još $p, q \notin \{0, a_x\}$, tj. $p \notin \{0, a_x\}$.</p>
'''),
        ('Opažanje 3: kad ne postoji',
         r'''
<p>Ako je svaki prefiks-XOR ostatka u $\{0, a_x\}$, svaki element ostatka je u $\{0, a_x\}$, pa je cijeli niz u $\{0, a_x\}$ i XOR svakog segmenta je $0$ ili $a_x$ — nikakva podjela na $\ge 2$ dijela s različitim vrijednostima nije moguća (barem dva dijela dijele vrijednost). Dakle traženje je i potpuno.</p>
'''),
        ('Složenost',
         r'''
<p>$O(n)$ po testu.</p>
'''),
    ],
    'solution': r'''
<p>Neka je $X$ XOR svih elemenata. Ako je $X \ne 0$, podijelimo niz na dva dijela proizvoljno — njihovi XOR-ovi bit će različiti (kad bi bili jednaki, ukupni XOR bio bi $0$).</p>
<p>Ako je $X = 0$, pokušajmo podijeliti niz na $3$ dijela i vidimo kad je to nemoguće. Neka je $a_x$ prvi element različit od nule (ako su svi nule, rješenja očito nema). Prvi podniz je $a[1 : x]$ (s XOR-om $a_x$). Ostatak želimo podijeliti na dva dijela čiji XOR nije ni $0$ ni $a_x$ (XOR-ovi tih dvaju dijelova ne mogu biti međusobno jednaki, jer bi tada XOR cijelog niza bio $a_x \ne 0$).</p>
<p>Ako takve podjele nema, onda za svaki $y$ s $x + 1 \le y \le n$ XOR podniza $a[x+1 : y]$ iznosi $0$ ili $a_x$. To znači da je svaki element tog dijela $0$ ili $a_x$, dakle svi elementi niza su $0$ ili $a_x$. No tada je XOR svakog podniza uvijek $0$ ili $a_x$, pa nikakva podjela ne postoji.</p>
<p>Rješenje: ako je $X \ne 0$, podijeli proizvoljno. Ako je $X = 0$, pronađi prvi nenul element $a_x$, uzmi $a[1 : x]$ i probaj sve načine podjele ostatka na dva dijela. Ako nijedan ne uspije, rješenja nema.</p>
''',
},
{
    'letter': 'F',
    'title': 'F*** 3-Colorable Graphs',
    'title_hr': 'Prokleti 3-obojivi grafovi',
    'slug': 'F_3_colorable_graphs',
    'tl': '1 s',
    'ml': '256 MB',
    'statement': r'''
<p>Zadan je povezan bipartitni graf: prva strana su vrhovi $1..n$, druga $n+1..2n$. Graf je $2$-obojiv, a ti želiš dodati što manje bridova (dopušteno i unutar iste strane) tako da graf prestane biti $3$-obojiv. Ispiši najmanji broj bridova koje treba dodati.</p>
<h3>Ulaz</h3>
<p>Prvi redak sadrži $n, m$ ($2 \le n \le 10^4$, $2n - 1 \le m \le \min(n^2, 2 \cdot 10^5)$). Slijedi $m$ bridova $u_i, v_i$ ($1 \le u_i \le n &lt; v_i \le 2n$), bez ponavljanja; graf je povezan.</p>
<h3>Izlaz</h3>
<p>Ispiši najmanji broj bridova.</p>
''',
    'hints': [
        r'''
<p>Odgovor je uvijek $2$ ili $3$: jedan brid nikad ne pomaže (novi kraj oboji trećom bojom), a $K_4$ nije $3$-obojiv i može se dobiti s najviše $3$ dodana brida u povezanom bipartitnom grafu.</p>
''',
        r'''
<p>Dva brida dostaju točno kad postoji $4$-ciklus $u_1 v_2 v_1 u_2$ (dodaj $(u_1,v_1)$ i $(u_2,v_2)$ $\Rightarrow K_4$). Traži $4$-ciklus: za svaki vrh $v$ označi susjede susjeda; ponovljena oznaka = $4$-ciklus. $O(n^2)$ uz rano zaustavljanje.</p>
''',
    ],
    'coach': [
        ('Opažanje 1: donja ograda $2$',
         r'''
<p>Početno bojanje stranama (1, 2). Jedan dodani brid $(u,v)$: prebojaj $v$ u $3$ — ispravno. Dakle $\ge 2$.</p>
'''),
        ('Opažanje 2: kad su $2$ dovoljna',
         r'''
<p>Dva brida pokvare $3$-obojivost samo ako su oba unutar istih strana, disjunktni, i sva $4$ „križna” brida postoje — tj. dodani bridovi dopunjuju $4$-ciklus do $K_4$. Inače uvijek nađeš prebojavanje jednog kraja u boju $3$.</p>
'''),
        ('Opažanje 3: gornja ograda $3$',
         r'''
<p>Treba par bridova $(u_1, v_1)$, $(u_1, v_2)$, $(u_2, v_1)$ — put duljine $3$ s unutarnjim vrhovima koji imaju stupanj $\ge 2$ — pa dodaj $3$ brida do $K_4$. Ako takvog nema, na svakom bridu jedan kraj je list, pa je svaki ne-list okružen samo listovima: graf nepovezan, kontradikcija.</p>
'''),
        ('Algoritam',
         r'''
<p>Detekcija $4$-ciklusa: za svaki $v$ prođi susjede $u$ i njihove susjede $w \ne v$; označi $w$. Drugo označavanje istog $w$ znači $4$-ciklus. Prije stajanja svaki $w$ označen najviše jednom — $O(n)$ po $v$, ukupno $O(n^2)$; $n \le 10^4$.</p>
'''),
    ],
    'solution': r'''
<p>Pokazat ćemo da je odgovor uvijek $2$ ili $3$. Početno obojimo vrhove prve strane bojom $1$, a ostale bojom $2$. Bez dodanih bridova graf ostaje $2$-obojiv (dakle i $3$-obojiv). Dodamo li jedan brid $(u, v)$, obojimo $v$ bojom $3$ i bojanje ostaje ispravno.</p>
<p>Pretpostavimo da smo dodali dva brida i graf više nije $3$-obojiv. Ako jedan od bridova spaja vrhove iz različitih strana, a drugi je $(u, v)$, obojimo $v$ bojom $3$ — bojanje je ispravno. Dakle oba dodana brida spajaju vrhove iste strane. Neka su to $(u_1, v_1)$ i $(u_2, v_2)$. Ako dijele vrh, npr. $u_1 = u_2$, obojimo $u_1$ bojom $3$. Inače pokušajmo jedan kraj svakog od ta dva brida obojiti bojom $3$. Ako tako ne možemo dobiti ispravno bojanje, to znači da su svi bridovi $(u_1, u_2), (u_1, v_2), (v_1, u_2), (v_1, v_2)$ prisutni u grafu. I doista, ako graf sadrži takav ciklus duljine $4$, dodavanjem $(u_1, v_1)$ i $(u_2, v_2)$ dobijemo potpuni podgraf na $4$ vrha koji nije $3$-obojiv.</p>
<p>Čak i bez $4$-ciklusa uvijek možemo dodati najviše $3$ brida. Dovoljno je pokazati da postoje $u_1, v_1$ iz prve i $u_2, v_2$ iz druge strane takvi da su barem $3$ od bridova $(u_1, u_2), (u_1, v_2), (v_1, u_2), (v_1, v_2)$ prisutna (tada dodamo preostale bridove i dobijemo $K_4$). Pretpostavimo suprotno: ne postoji brid $(u, v)$ ($u$ iz prve, $v$ iz druge strane) takav da i $u$ i $v$ imaju još barem jedan brid. Tada je za svaki brid $(u, v)$ barem jedan od $u, v$ list. Uzmimo bilo koji vrh $u$ koji nije list — on može biti spojen samo s listovima, pa $u$ zajedno s tim listovima čini zasebnu komponentu i graf nije povezan, što je kontradikcija s uvjetom zadatka.</p>
<p>Dakle, odgovor je $2$ ako postoji $4$-ciklus $u_1, v_2, v_1, u_2$, a $3$ inače. Kako provjeriti postoji li $4$-ciklus? Za zadani vrh $v$ sa susjedima $u_1, \dots, u_k$: $v$ je u $4$-ciklusu ako i samo ako postoji vrh $v_1 \ne v$ spojen s barem dva od $u_1, \dots, u_k$. Prolazimo susjede svih $u_1, \dots, u_k$ i označavamo posjećene vrhove (osim $v$); ako neki vrh trebamo označiti dvaput, našli smo $4$-ciklus. Budući da svaki vrh označimo najviše jednom prije nego što stanemo, to je $O(n)$ po vrhu, dakle ukupno $O(n^2)$.</p>
''',
},
{
    'letter': 'G',
    'title': 'Graph Problem With Small n',
    'title_hr': 'Zadatak o grafu s malim n',
    'slug': 'G_graph_problem_with_small_n',
    'tl': '2 s',
    'ml': '256 MB',
    'statement': r'''
<p>Zadan je neusmjereni graf s $n$ vrhova. Za svaki par vrhova $(i, j)$, $i \ne j$, odredi postoji li Hamiltonov put koji počinje u $i$ i završava u $j$.</p>
<h3>Ulaz</h3>
<p>Prvi redak sadrži $n$ ($2 \le n \le 24$). Slijedi matrica susjedstva kao $n$ binarnih nizova duljine $n$.</p>
<h3>Izlaz</h3>
<p>Ispiši $n$ binarnih nizova duljine $n$; $j$-ti znak $i$-tog niza je <code>1</code> ako postoji Hamiltonov put od $i$ do $j$.</p>
''',
    'hints': [
        r'''
<p>Bitmask DP nad podskupovima: $dp[mask][u]$ = bitmaska krajeva $v$ za koje postoji Hamiltonov put $u \to v$ na $mask$. Prijelaz je jedan AND: $v$ je dodatan ako $dp[mask \setminus v][u]\ \&\ neigh_v \ne 0$. To je $O(2^n n^2)$.</p>
''',
        r'''
<p>Za $O(2^n n)$: fiksiraj vrh $n-1$ kao „sredinu”. Put $u \to v$ postoji ako postoji podjela vrhova na $mask_u \ni u$ i $mask_v \ni v$ (obje sadrže $n-1$) s $u \in dp[mask_u][n-1]$ i $v \in dp[mask_v][n-1]$. Prođi sve $mask_u$ i OR-aj.</p>
''',
    ],
    'coach': [
        ('Opažanje 1: osnovni DP',
         r'''
<p>$dp[mask][u][v]$ klasično: $O(2^n n^3)$ — preko $2^{24} \cdot 24^3$, presporo. Krajeve $v$ pakiraj u bitmasku po $u$: $dp_1[mask][u]$.</p>
'''),
        ('Opažanje 2: prijelaz u $O(1)$',
         r'''
<p>„Postoji $w \in mask$, $w \sim v$, s putom $u \to w$ na $mask \setminus v$” $\iff dp_1[mask \setminus v][u] \,\&\, neigh_v \ne 0$. Ukupno $O(2^n n^2) \approx 10^{10}$ bitovnih operacija — još presporo/rubno.</p>
'''),
        ('Redukcija: samo jedan izvor',
         r'''
<p>Računaj $dp_1[mask][n-1]$ za sve $mask$: $O(2^n n)$. Hamiltonov put $u \to v$ prolazi kroz $n-1$ i rastavlja se na put $u \to n-1$ na skupu $mask_u$ i $n-1 \to v$ na komplementu (plus $n-1$). Za svaki $mask_u$ komplement je određen, pa za $u \in dp_1[mask_u][n-1]$ napravi $ans_u \mathrel{|}= dp_1[mask_v][n-1]$.</p>
'''),
        ('Složenost',
         r'''
<p>$O(2^n n)$ vremena, $O(2^n)$ memorije (32-bitne maske); $n \le 24$.</p>
'''),
    ],
    'solution': r'''
<p>Vrhove numeriramo od $0$ do $n - 1$; podskup vrhova $\{i_1, \dots, i_k\}$ kodiramo brojem $mask = 2^{i_1} + \dots + 2^{i_k}$.</p>
<p><b>Rješenje u $O(2^n n^3)$.</b> Neka $dp[mask][u][v]$ kaže postoji li Hamiltonov put od $u$ do $v$ na vrhovima iz $mask$ (koji sadrži bitove $u$ i $v$). Početno $dp[2^v][v][v] = \text{true}$. Podskupove obrađujemo po rastućoj veličini; $dp[mask][u][v] = \text{true}$ ako i samo ako $mask$ sadrži vrh $w \ne v$ takav da je $w$ spojen s $v$ i $dp[mask - 2^v][u][w] = \text{true}$ ($w$ je prethodnik od $v$ na putu). Za dani $mask$ i par $(u, v)$ pretražujemo kandidate $w$ u $O(n)$.</p>
<p><b>Rješenje u $O(2^n n^2)$.</b> Umjesto booleove vrijednosti čuvamo broj $dp_1[mask][u]$ čiji je bit $v$ postavljen ako i samo ako je $dp[mask][u][v]$ istina. Za svaki vrh $u$ čuvamo i $neigh_u$ — masku susjeda. Uvjet "postoji $w \ne v$ u $mask$ spojen s $v$ takav da $dp[mask - 2^v][u][w]$" ekvivalentan je tome da $dp_1[mask - 2^v][u]$ i $neigh_v$ imaju barem jedan zajednički bit — jedna operacija AND. Za $mask, u$ računamo $dp_1[mask][u]$ u $O(n)$, ukupno $O(2^n n^2)$.</p>
<p><b>Rješenje u $O(2^n n)$.</b> Izračunajmo $dp_1[mask][n-1]$ za sve $mask$ u $O(2^n n)$. Svaki Hamiltonov put mora proći kroz vrh $n - 1$. Za dva vrha $u, v &lt; n - 1$ Hamiltonov put od $u$ do $v$ postoji ako i samo ako postoje $mask_u$, $mask_v$ takvi da:</p>
<ul>
    <li>$u \in mask_u$, $v \in mask_v$;</li>
    <li>svaki vrh osim $n - 1$ je u točno jednom od njih, a $n - 1$ u oba;</li>
    <li>$u \in dp_1[mask_u][n-1]$ i $v \in dp_1[mask_v][n-1]$.</li>
</ul>
<p>Drugim riječima, postoji podjela vrhova na dvije grupe (s $n - 1$ u obje) takva da postoji Hamiltonov put od $u$ do $n - 1$ u prvoj i od $n - 1$ do $v$ u drugoj. Za svaki $u$ čuvamo $ans_u$ čiji bit $v$ označava postojanje puta $u \to v$. Prolazimo sve $mask_u$ ($mask_v = 2^n - 1 - mask_u + 2^{n-1}$ je jednoznačno određen), i za svaki $u \in dp_1[mask_u][n-1]$ postavimo $ans_u \mathrel{|}= dp_1[mask_v][n-1]$. Ukupna složenost $O(2^n n)$.</p>
''',
},
{
    'letter': 'H',
    'title': 'Help Me to Get This Published',
    'title_hr': 'Pomozite mi da ovo objavim',
    'slug': 'H_help_me_to_get_this_published',
    'tl': '1 s',
    'ml': '256 MB',
    'statement': r'''
<p><b>Gallaijevo bojanje</b> potpunog grafa $K_n$ je bojanje bridova bez trokuta čija su tri brida obojena trima različitim bojama. <b>Bojni stupanj</b> $d(v)$ je broj različitih boja na bridovima incidentnima s $v$. Niz $(a_1, \dots, a_n)$ je valjan ako postoji Gallaijevo bojanje $K_n$ s $d(i) = a_i$. Zadani su neki $a_i$, a ostali su $-1$; prebroji načine zamjene vrijednosti $-1$ tako da niz bude valjan, modulo $998\,244\,353$.</p>
<h3>Ulaz</h3>
<p>Prvi redak sadrži $n$ ($2 \le n \le 100$), drugi $a_1, \dots, a_n$ ($1 \le a_i \le n - 1$ ili $a_i = -1$).</p>
<h3>Izlaz</h3>
<p>Ispiši broj načina modulo $998\,244\,353$.</p>
''',
    'hints': [
        r'''
<p>Nužan uvjet (Teorem 2): $\sum_i 2^{-d(i)} \ge 1$. Nije dovoljan.</p>
''',
        r'''
<p>Puni kriterij (Teorem 4): za sortirane stupnjeve $d(1) \le \dots \le d(n)$ i svaki $k$: $\sum_{i \ge k} 2^{-(d(i) - d(k-1))} \ge 1$ (uz $d(0) = 0$). Prebroji nizove DP-om po vrijednostima od $n-1$ prema $1$, čuvajući broj iskorištenih većih vrijednosti i (cijelobrojno skaliran) zbroj $\sum 2^{k - x}$.</p>
''',
    ],
    'coach': [
        ('Opažanje 1: struktura Gallaijevih bojanja',
         r'''
<p>S $\ge 3$ boja neka boja razapinje nepovezan graf. Za komponentu $A$ te boje i $w \notin A$ svi bridovi $w$–$A$ imaju istu boju (Lema 1). To omogućuje sažimanje $A$ u jedan vrh i indukciju.</p>
'''),
        ('Opažanje 2: nejednakost zbroja',
         r'''
<p>Indukcijom preko sažimanja: $\sum_i 2^{-d(i)} \ge 1$. Vrh s $d = n-1$ prisiljava stupnjeve $\{n-1, n-1, n-2, \dots, 1\}$ (turnir bez $3$-ciklusa je tranzitivan, Lema 3).</p>
'''),
        ('Opažanje 3: pojačani kriterij',
         r'''
<p>Za sortirane stupnjeve, vrh $i \ge k$ prema vrhovima $\lt k$ ima najviše $d(k-1)$ boja (inače Lema 3 daje još jedan vrh visokog stupnja među njima). Zato podgraf na $\{k..n\}$ ima stupnjeve $\ge d(i) - d(k-1)$ i Teorem 2 na njemu daje uvjet za svaki $k$. Dovoljnost: konstrukcija kloniranjem vrha.</p>
'''),
        ('Algoritam: DP po vrijednostima',
         r'''
<p>Obradi vrijednost $k$ od $n-1$ do $1$; stanje: koliko je pozicija dobilo vrijednost $\ge k$ ($cnt$) i $\lfloor\sum_{x \ge k} 2^{k - x}\rfloor$ (skalirani zbroj, $\le n$). Kad se spuštaš na $k-1$, zbroj se dijeli s $2$ i dodaju se novi elementi s vrijednošću $k-1$ (svaki doprinosi $1$); uvjet: zbroj $\ge 1$ kad god su sve vrijednosti $\ge k$ „zatvorene”. Zadane $a_i$ fiksiraju koliko pozicija mora dobiti koju vrijednost; slobodne pozicije biraj binomno. $O(n^4)$, $n \le 100$.</p>
'''),
    ],
    'solution': r'''
<p><i>Predgovor autora.</i> Pomozite mi da ovo objavim, molim. Ispričavam se za dugačko rješenje; treba samo jedan poznati rezultat:</p>
<p><b>Poznata činjenica.</b> Ako Gallaijevo bojanje sadrži barem tri različite boje, postoji boja koja razapinje nepovezan graf.</p>
<p>Boju brida između $i$ i $j$ označavamo $c(i, j)$.</p>
<p><b>Lema 1.</b> Neka boja $1$ razapinje nepovezan graf i neka je $A$ jedna njegova komponenta. Tada za sve $u, v \in A$ i $w \notin A$ vrijedi $c(u, w) = c(v, w)$.</p>
<p><i>Dokaz.</i> Za brid $(u_1, v_1)$ boje $1$ unutar $A$ i $w \notin A$ promotrimo trokut $u_1 v_1 w$: $c(u_1, v_1) = 1$, a $c(u_1, w) \ne 1$, $c(v_1, w) \ne 1$, pa $c(u_1, w) = c(v_1, w)$. Za proizvoljne $u, v \in A$ postoji put boje $1$ $x_0 = u, x_1, \dots, x_k = v$, pa $c(w, u) = c(w, x_0) = c(w, x_1) = \dots = c(w, v)$. $\square$</p>
<p><b>Teorem 2.</b> Za svako Gallaijevo bojanje vrijedi
$$\sum_{i=1}^{n} \frac{1}{2^{d(i)}} \ge 1.$$</p>
<p><i>Dokaz.</i> Indukcijom po $n$; trivijalno za $n \le 3$. Neka je $n \ge 4$. Ako ima najviše $2$ boje, $\sum \frac{1}{2^{d(i)}} \ge \frac{n}{4} \ge 1$. Inače postoji boja (neka je to $1$) koja razapinje nepovezan graf. Uzmimo komponentu $A$ boje $1$. Po Lemi 1 za svaki $v \notin A$ postoji boja $c(v)$ takva da svi bridovi između $v$ i $A$ imaju boju $c(v)$. Neka je $k$ broj različitih boja među $c(v)$. Sažmimo $A$ u jedan vrh $a$ s $d(a) = k$; po pretpostavci indukcije
$$\sum_{v \notin A} \frac{1}{2^{d(v)}} + \frac{1}{2^k} \ge 1.$$
Zasebno promotrimo graf na $A$ i neka je $d_1(v)$ bojni stupanj unutar njega; po indukciji $\sum_{v \in A} \frac{1}{2^{d_1(v)}} \ge 1$. Za $v \in A$ je $d(v) \le d_1(v) + k$, pa
$$\sum_{i=1}^{n} \frac{1}{2^{d(i)}} \ge \sum_{v \notin A} \frac{1}{2^{d(v)}} + \frac{1}{2^k} \sum_{v \in A} \frac{1}{2^{d_1(v)}} \ge \sum_{v \notin A} \frac{1}{2^{d(v)}} + \frac{1}{2^k} \ge 1.\ \square$$</p>
<p>To je nužan uvjet za niz stupnjeva, ali nije dovoljan.</p>
<p><b>Lema 3.</b> Ako u Gallaijevu bojanju $K_n$ neki bojni stupanj iznosi $n - 1$, tada su bojni stupnjevi $n-1, n-1, n-2, n-3, \dots, 1$ u nekom poretku.</p>
<p><i>Dokaz.</i> Neka je $d(n) = n - 1$; sve boje $c(i, n)$ su različite, neka je $c(i, n) = i$. Iz trokuta $ijn$ slijedi da je $c(i, j) \in \{i, j\}$. Usmjerimo $i \to j$ ako je $c(i, j) = i$, inače $j \to i$. Budući da nema "šarenih" trokuta, nema usmjerenih ciklusa duljine $3$. Turnir bez usmjerenog $3$-ciklusa je acikličan (promatrajući najkraći usmjereni ciklus $x_1, \dots, x_k$, $k \ge 4$: ovisno o orijentaciji brida $x_1 x_3$ dobijemo kraći ciklus). Dakle vrhovi $1, \dots, n-1$ mogu se poredati u red tako da svi bridovi idu slijeva nadesno; bojni stupanj $i$-tog vrha u redu je točno $i$. $\square$</p>
<p><b>Teorem 4.</b> Neka je $d(1) \le d(2) \le \dots \le d(n)$ niz bojnih stupnjeva Gallaijeva bojanja i $d(0) = 0$. Tada za svaki $1 \le k \le n$:
$$\sum_{i=k}^{n} \frac{1}{2^{d(i) - d(k-1)}} \ge 1.$$</p>
<p><i>Dokaz.</i> Za $k = 1$ to je Teorem 2. Neka je $k \ge 2$ i $i \ge k$. Ako iz $i$ prema vrhovima $1, \dots, k-1$ ide barem $x$ različitih boja, odaberimo po jedan brid svake boje s krajevima $v_1, \dots, v_x$. U podgrafu na $v_1, \dots, v_x, i$ vrh $i$ ima bojni stupanj $x$ (na $x + 1$ vrhova), pa po Lemi 3 još jedan vrh ima bojni stupanj $x$; stoga $x \le d(k-1)$. U podgrafu na $k, \dots, n$ bojni stupanj vrha $i$ je barem $d(i) - d(k-1)$; primijenimo Teorem 2. $\square$</p>
<p>Pokazuje se da je taj uvjet i dovoljan. Taj dio nije osobito zanimljiv; ideja je da Gallaijeva bojanja s takvim nizovima stupnjeva konstruiramo ovako: uzmemo bojanje $K_{n-1}$, kloniramo vrh $i$ i dodamo brid između $i$ i klona. Time postižemo $d(i) \to d(i), d(i)$ ili $d(i) \to d(i)+1, d(i)+1$, što omogućuje sve valjane nizove.</p>
<p>Konačno, kriterij koristimo za rješavanje zadatka dinamičkim programiranjem po stupnjevima od $n - 1$ prema $1$: kad smo na broju $k$, čuvamo broj načina da smo iskoristili $cnt$ brojeva $\ge k$ s trenutačnom vrijednošću $\lfloor \sum 2^{k - x} \rfloor = sum$ (gdje $x$ prolazi svih $cnt$ odabranih brojeva $\ge k$). To daje jednostavno $O(n^4)$ rješenje.</p>
''',
},
{
    'letter': 'I',
    'title': 'Increasing Grid',
    'title_hr': 'Rastuća mreža',
    'slug': 'I_increasing_grid',
    'tl': '1 s',
    'ml': '256 MB',
    'statement': r'''
<p>Tablicu $n \times m$ treba popuniti brojevima od $1$ do $n + m$ tako da su reci i stupci strogo rastući. Neke su vrijednosti zadane. Prebroji načine popunjavanja nepoznatih vrijednosti modulo $998\,244\,353$.</p>
<h3>Ulaz</h3>
<p>Prvi redak sadrži $t$ ($1 \le t \le 10^4$). Za svaki primjer: $n, m$ ($1 \le n, m \le 2 \cdot 10^5$, $nm \le 2 \cdot 10^5$) i tablica ($a_{i,j} \in [1, n+m]$ ili $-1$). Zbroj svih $nm$ ne prelazi $2 \cdot 10^5$.</p>
<h3>Izlaz</h3>
<p>Za svaki primjer ispiši broj načina.</p>
''',
    'hints': [
        r'''
<p>Oduzmi $i + j - 1$ od $a_{i,j}$: ostaje tablica iz $\{0,1\}$ nepadajuća po redcima i stupcima (jer je $a_{1,1} \ge 1$, $a_{n,m} \le n+m$).</p>
''',
        r'''
<p>Takva 0/1 tablica je monotoni put od donjeg lijevog do gornjeg desnog kuta (nule iznad-lijevo, jedinice ispod-desno). Prebroji putove DP-om po čvorovima rešetke koji poštuju zadane vrijednosti.</p>
''',
    ],
    'coach': [
        ('Opažanje 1: normalizacija',
         r'''
<p>Strogo rastući retci/stupci s vrijednostima u $[1, n+m]$: $a_{i,j} \ge i + j - 1$ i $a_{i,j} \le (n+m) - (n-i) - (m-j) = i + j$. Dakle $b_{i,j} = a_{i,j} - (i+j-1) \in \{0, 1\}$, i $b$ je nepadajuća po redcima i stupcima. Obrat vrijedi.</p>
'''),
        ('Opažanje 2: monotone 0/1 tablice = staze',
         r'''
<p>Skup jedinica je „stepenasti” skup zatvoren prema desno-dolje; granica je monotona staza gore/desno od $(n, 0)$ do $(0, m)$ po bridovima rešetke. Zadana $1$ traži da polje bude s jedne strane staze, zadana $0$ s druge.</p>
'''),
        ('Algoritam',
         r'''
<p>$dp_{i,j}$ = broj staza do čvora $(i,j)$; korak gore prolazi uz polje lijevo (mora biti $0$-kompatibilno) i desno (mora biti $1$-kompatibilno) — provjeri zadanu vrijednost polja uz korak s odgovarajuće strane. Ako je neka zadana vrijednost izvan $\{0,1\}$ nakon normalizacije, odgovor $0$.</p>
'''),
        ('Složenost',
         r'''
<p>$O(nm)$, $\sum nm \le 2 \cdot 10^5$.</p>
'''),
    ],
    'solution': r'''
<p>Oduzmimo od $a_{i,j}$ broj $i + j - 1$. Sada reci i stupci moraju biti nepadajući, uz $0 \le a_{1,1}$ i $a_{n,m} \le 1$; dakle svi su brojevi $0$ ili $1$. Uvjet je i dovoljan: ako je $0 \le a_{i,j} \le 1$, izvorna vrijednost bila je $i + j - 1$ ili $i + j$, tj. u rasponu od $1$ do $n + m$.</p>
<p>Zanimaju nas dakle tablice nula i jedinica nepadajuće po recima i stupcima, s nekim zadanim elementima (ako je $a_{i,j} - (i + j - 1) \notin \{0, 1\}$, odgovor je $0$). Za svaku jedinicu sve u pravokutniku desno-dolje od nje mora biti jedinica; za svaku nulu sve lijevo-gore mora biti nula. Ako je neka nula desno-dolje od neke jedinice, odgovor je $0$. Popunjavanje radimo tako da za svaki redak i stupac, ako je $a_{i,j} = 1$, postavimo i $a_{i+1,j}$ i $a_{i,j+1}$ na $1$; ako bismo pritom nulu morali pretvoriti u jedinicu, rješenja nema. Zatim isto s nulama.</p>
<p>Tablice nula i jedinica nepadajuće po recima i stupcima imaju sljedeći oblik: postoji put od donjeg lijevog do gornjeg desnog kuta koji ide samo gore i desno po rubovima polja, s nulama na jednoj i jedinicama na drugoj strani. Prebrojimo takve putove uz poznate vrijednosti. Čvorovi tablice su sjecišta $n + 1$ horizontalnih i $m + 1$ vertikalnih linija. Neka je $dp_{i,j}$ broj putova (samo gore i desno) od donjeg lijevog kuta (sjecište $n$-te horizontalne i $0$-te vertikalne) do čvora $(i, j)$ takvih da su svi brojevi lijevo od puta nule, a desno jedinice. Počinjemo s $dp_{n,0} = 1$ i tražimo $dp_{0,m}$. Prijelaz je jednostavan: $dp_{i,j}$ dobiva doprinose $dp_{i+1,j}$ i $dp_{i,j-1}$, ovisno o tome zadovoljava li put sve uvjete (polje uz korak mora biti kompatibilno sa stranom na kojoj se nalazi).</p>
<p>Složenost je $O(nm)$.</p>
''',
},
{
    'letter': 'J',
    'title': 'Jewel of Data Structure Problems',
    'title_hr': 'Dragulj zadataka o strukturama podataka',
    'slug': 'J_jewel_of_data_structure_problems',
    'tl': '1 s',
    'ml': '256 MB',
    'statement': r'''
<p>Niz je neparan ako ima neparan broj inverzija, inače je paran. Ljepota permutacije $p$ je duljina najduljeg neparnog podniza (ne nužno uzastopnog), ili $-1$ ako takav ne postoji. Zadana je permutacija i $q$ upita; nakon svakog upita zamijeni $p_{u_i}$ i $p_{v_i}$ i ispiši ljepotu.</p>
<h3>Ulaz</h3>
<p>Prvi redak sadrži $n, q$ ($1 \le n, q \le 2 \cdot 10^5$), drugi permutaciju, a zatim $q$ redaka s $u_i, v_i$ ($u_i \ne v_i$).</p>
<h3>Izlaz</h3>
<p>Ispiši $q$ brojeva — ljepotu nakon svakog upita.</p>
''',
    'hints': [
        r'''
<p>Ljepota je $n$ ako je permutacija neparna; inače $n-1$ ako neki element sudjeluje u neparno mnogo inverzija; inače $n-2$ ako postoji bilo koja inverzija; inače $-1$ (identiteta).</p>
''',
        r'''
<p>Broj inverzija koje sadrže $p_i$ ima parnost od $i + p_i$. Parnost permutacije = parnost $n - \#\text{ciklusa}$, a zamjena mijenja parnost. Održavaj: parnost, broj $i$ s $p_i \equiv i \pmod 2$, broj fiksnih točaka. $O(1)$ po upitu.</p>
''',
    ],
    'coach': [
        ('Opažanje 1: koliko izbaciti',
         r'''
<p>Izbacivanje elementa $p_i$ mijenja broj inverzija za $c_i$ (inverzije koje ga sadrže). Neparna permutacija: ljepota $n$. Parna s neparnim $c_i$: izbaci $i$, ljepota $n-1$. Svi $c_i$ parni i postoji inverzija $(i,j)$: izbaci oboje, broj pada za $c_i + c_j - 1$ (neparan) — ljepota $n-2$. Bez inverzija: $-1$.</p>
'''),
        ('Opažanje 2: parnost $c_i$',
         r'''
<p>Ako je $x$ broj $j \lt i$ s $p_j \lt p_i$: lijevo je $i - 1 - x$ inverzija, desno $p_i - 1 - x$; $c_i = i + p_i - 2(x+1) \equiv i + p_i \pmod 2$. Dakle „svi $c_i$ parni” $\iff$ $p_i \equiv i$ za sve $i$.</p>
'''),
        ('Algoritam',
         r'''
<p>Parnost permutacije preko broja ciklusa jednom na početku ($O(n)$), zatim svaka zamjena je transpozicija: parnost se okrene. Ažuriraj brojače $cnt_{par}$ ($p_i \equiv i$) i $cnt_{fix}$ ($p_i = i$) za dvije promijenjene pozicije. Odgovor po lancu uvjeta.</p>
'''),
        ('Složenost',
         r'''
<p>$O(n + q)$.</p>
'''),
    ],
    'solution': r'''
<p>Najprije odredimo ljepotu zadane permutacije. Ako je cijela permutacija neparna, ljepota je $n$. Neka je permutacija parna. Za $i$ označimo $c_i$ broj inverzija koje uključuju $p_i$. Ako je neki $c_i$ neparan, podniz svih elemenata osim $i$-tog je neparan, pa je ljepota $n - 1$.</p>
<p>Inače su svi $c_i$ parni. Ako postoji barem jedna inverzija, recimo $i &lt; j$ s $p_i &gt; p_j$, podniz bez $i$ i $j$ je neparan (uklonili smo sve inverzije koje sadrže $p_i$ ili $p_j$, ali inverziju $(p_i, p_j)$ samo jednom), pa je ljepota $n - 2$. Ako inverzija nema, permutacija je $(1, 2, \dots, n)$, svi su podnizovi parni i ljepota je $-1$.</p>
<p>Kako to brzo računati? Uočimo: $c_i$ je paran ako i samo ako $p_i \bmod 2 = i \bmod 2$. Neka je $x$ broj indeksa $j &lt; i$ s $p_j &lt; p_i$. Lijevo od $p_i$ je $i - 1 - x$ elemenata u inverziji s njim, desno $p_i - 1 - x$. Ukupno $c_i = (i + p_i) - 2(x + 1)$, pa je $c_i$ paran točno kad je $i + p_i$ paran.</p>
<p>Parnost permutacije: jednaka je parnosti $n - cycles$, gdje je $cycles$ broj ciklusa permutacije (zamjena dvaju elemenata mijenja parnost, a permutaciju sortiramo s točno $n - cycles$ zamjena). Uz to održavamo $cnt\_eq$ — broj indeksa s $p_i = i$, i $cnt\_same\_par$ — broj indeksa s $p_i \bmod 2 = i \bmod 2$; obje se vrijednosti lako ažuriraju nakon svake zamjene.</p>
<p>Odgovor na upit: ako je permutacija neparna, ljepota je $n$. Inače, ako $cnt\_same\_par \ne n$, ljepota je $n - 1$. Inače, ako $cnt\_eq \ne n$, ljepota je $n - 2$; inače je permutacija sortirana i ljepota je $-1$. Složenost $O(n + q)$.</p>
''',
},
{
    'letter': 'K',
    'title': 'King of Swapping',
    'title_hr': 'Kralj zamjena',
    'slug': 'K_king_of_swapping',
    'tl': '1 s',
    'ml': '256 MB',
    'statement': r'''
<p>Uređaj ima $m$ operacija $(a_i, b_i)$: ako je $p_{a_i} &gt; p_{b_i}$, zamijeni ta dva elementa, inače ne radi ništa. Operacije se smiju primjenjivati proizvoljno mnogo puta u bilo kojem redoslijedu. Odredi može li se iz svake permutacije dobiti svaka druga.</p>
<h3>Ulaz</h3>
<p>Prvi redak sadrži $t$ ($1 \le t \le 10^4$). Za svaki primjer: $n, m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$) i $m$ različitih parova $(a_i, b_i)$. Zbrojevi svih $n$ i svih $m$ ne prelaze $2 \cdot 10^5$.</p>
<h3>Izlaz</h3>
<p>Za svaki primjer ispiši <code>YES</code> ili <code>NO</code>.</p>
''',
    'hints': [
        r'''
<p>Najveći element $n$ mora doći na svaku poziciju; on se pomiče $u \to v$ točno operacijom $(u, v)$. Dakle usmjereni graf operacija mora biti jako povezan.</p>
''',
        r'''
<p>Jaka povezanost je i dovoljna: na svakom usmjerenom ciklusu elementi se mogu presložiti proizvoljno (indukcija: sortiraj guranjem najvećih, pa pokaži da se dobije obrnuti poredak, pa inverzne operacije), a svake dvije pozicije leže na zajedničkom ciklusu.</p>
''',
    ],
    'coach': [
        ('Opažanje 1: nužnost',
         r'''
<p>Element $n$ uvijek zadovoljava $p_u \gt p_v$, pa se kreće točno po bridovima $(a_i, b_i)$. Da bi $n$ stigao svugdje iz svakog početka, graf je jako povezan — provjeri s dva DFS-a (izvorni i obrnuti graf iz vrha $1$).</p>
'''),
        ('Opažanje 2: dovoljnost na ciklusu',
         r'''
<p>Na ciklusu $v_1 \to \dots \to v_k$: (1) iz svake permutacije možeš doći do „sortirane” guranjem $k$, pa $k-1$, … po ciklusu; (2) iz sortirane do cikličkog pomaka obrnute — indukcijom, stopivši $k$ i $k-1$ u jedan „blok” koji se pomiče zajedno; (3) obrnute operacije iz svake permutacije vode u obrnutu, pa naprijed-operacije iz obrnute vode u svaku.</p>
'''),
        ('Algoritam',
         r'''
<p>Samo test jake povezanosti: $O(n + m)$ po testu. Pazi na $n = 1$ (trivijalno YES) i izolirane vrhove (NO).</p>
'''),
    ],
    'solution': r'''
<p>Promotrimo poziciju na kojoj je broj $n$. Njega moramo moći pomaknuti na svaku poziciju, a $n$ se iz pozicije $u$ u poziciju $v$ pomiče (jednom operacijom) ako i samo ako postoji operacija $(u, v)$ (uvjet $p_u &gt; p_v$ je automatski ispunjen). Dakle, u usmjerenom grafu s bridovima $(a_i, b_i)$ svaki vrh mora biti dostižan iz svakog — graf mora biti <b>jako povezan</b>. To provjeravamo dvama DFS-ovima (iz vrha $1$ u izvornom i u obrnutom grafu), složenost $O(n + m)$.</p>
<p>Pokažimo da je uvjet i dovoljan. Uzmimo usmjereni ciklus $v_1, \dots, v_k$ s operacijama $(v_1, v_2), \dots, (v_k, v_1)$. Pokazat ćemo da na tom ciklusu elemente možemo presložiti po volji; bez smanjenja općenitosti na pozicijama $v_1, \dots, v_k$ su brojevi $1, \dots, k$.</p>
<p>Prvo, iz svake situacije možemo dobiti $p_{v_1} = 1, \dots, p_{v_k} = k$: najprije $k$ guramo po ciklusu dok ne dođe na $v_k$, zatim $k - 1$ itd. Zatim pokazujemo da iz $(1, 2, \dots, k)$ možemo dobiti neki ciklički pomak od $(k, k-1, \dots, 1)$, indukcijom (za $k = 1, 2$ očito). Korak: zamijenimo $k$ sa sljedećim brojem u ciklusu $k - 2$ puta i dobijemo $(2, 3, \dots, k-2, k, k-1, 1)$; sada $k$ i $k-1$ "stopimo u jedan element" (možemo ih zajedno pomicati: $(k, k-1, x) \to (k, x, k-1) \to (x, k, k-1)$) i primijenimo tvrdnju za $k - 1$.</p>
<p>Napokon, iz pomaka od $(k, k-1, \dots, 1)$ dobivamo bilo koju permutaciju: obrnimo sve operacije (umjesto $(u_i, v_i)$ promatramo $(v_i, u_i)$). Dovoljno je pokazati da tim obrnutim operacijama iz svake permutacije dolazimo do cikličkog pomaka od $(k, \dots, 1)$, a to radimo na isti način: najprije $k$ na mjesto, pa $k - 1$, …, $1$.</p>
<p>Time je tvrdnja za ciklus dokazana. Ako je graf jako povezan, za svake dvije pozicije $u \ne v$ postoji jednostavan ciklus koji ih sadrži; na njemu možemo elemente presložiti proizvoljno, pa i samo zamijeniti $p_u$ i $p_v$. Dakle možemo zamijeniti bilo koja dva elementa, a time i dobiti svaku permutaciju.</p>
''',
},
{
    'letter': 'L',
    'title': 'Least Annoying Constructive Problem',
    'title_hr': 'Najmanje dosadan konstruktivni zadatak',
    'slug': 'L_least_annoying_constructive_problem',
    'tl': '1 s',
    'ml': '256 MB',
    'statement': r'''
<p>Rasporedi svih $\frac{n(n-1)}{2}$ bridova potpunog grafa $K_n$ u krug tako da svakih $n - 1$ uzastopnih bridova tvori stablo. Može se dokazati da je to uvijek moguće.</p>
<h3>Ulaz</h3>
<p>Jedini redak sadrži $n$ ($3 \le n \le 500$).</p>
<h3>Izlaz</h3>
<p>Ispiši $\frac{n(n-1)}{2}$ redaka s bridovima $u_i &lt; v_i$; svi parovi različiti, a svaki ciklički prozor od $n - 1$ uzastopnih bridova mora biti stablo.</p>
''',
    'hints': [
        r'''
<p>Neparan $n = 2k+1$: vrhove stavi na kružnicu; blok $i$ je $k$ „paralelnih” bridova $(i - j, i + 1 + j)$, $j = 0..k-1$. Ispiši blokove redom $i = 1..n$.</p>
''',
        r'''
<p>Svaki prozor od $2k$ uzastopnih bridova sadrži cijeli jedan blok (sparivanje koje ostavlja jedan izolirani vrh) te sufiks prethodnog i prefiks sljedećeg — oni redom spajaju susjedne komponente pa nastaje stablo. Za paran $n$ dodaj središnji vrh spojen s „preostalim” vrhom svakog bloka.</p>
''',
    ],
    'coach': [
        ('Opažanje 1: sparivanja kao građevni blokovi',
         r'''
<p>Blok $i$ je savršeno sparivanje svih vrhova osim jednog ($i + k + 1$), i sva sparivanja zajedno pokrivaju svaki brid $K_{2k+1}$ točno jednom (bridovi po „smjeru” na kružnici — klasična rotacijska dekompozicija).</p>
'''),
        ('Opažanje 2: zašto je prozor stablo',
         r'''
<p>Prozor $= $ sufiks bloka $i-1$ duljine $x$ $+$ cijeli blok $i$ $+$ prefiks bloka $i+1$ duljine $k - x$. Nakon bloka $i$ imamo $k+1$ komponenata (parovi i izolirani vrh), poredanih po kružnici. $j$-ti brid bloka $i-1$ i $j$-ti brid bloka $i+1$ spajaju $j$-tu i $(j+1)$-u komponentu; sufiks jednog i prefiks drugog pokrivaju sve $k$ „spojeva” bez ponavljanja: $2k$ bridova, $2k+1$ vrhova, povezano $\Rightarrow$ stablo.</p>
'''),
        ('Algoritam: paran $n$',
         r'''
<p>$n = 2k+2$: $2k+1$ vrhova na kružnici + središte $c$. Blok $i$: $k$ paralelnih bridova + $(i + k + 1, c)$. Prozor od $2k+1$ bridova analizira se isto (središnji brid samo veže izolirani vrh na $c$). Ispis u $O(n^2)$.</p>
'''),
    ],
    'solution': r'''
<p><b>Neparan $n$.</b> Neka je $n = 2k + 1$. Vrhove zamislimo na kružnici, numerirane $1..n$, uz cikličku notaciju (vrh $n + i$ je vrh $i$). Za svaki $i$ od $1$ do $n$ ispišimo sljedećih $k$ bridova:
$$(i, i+1),\ (i-1, i+2),\ (i-2, i+3),\ \dots,\ (i-k+1, i+k).$$
Na kružnici su to $k$ bridova "paralelnih" bridu $(i, i+1)$; nazovimo ih <b>blok $i$</b>.</p>
<p>Zašto to radi? Promotrimo bilo kojih $n - 1 = 2k$ uzastopnih bridova. Oni u potpunosti sadrže neki blok, recimo blok $2$, te neki sufiks bloka $1$ duljine $x$ i prefiks bloka $3$ duljine $k - x$. Nakon što nacrtamo blok $2$, imamo $k + 1$ komponenti: $k$ bridova i izolirani vrh $3 + k$. Ključno je da $i$-ti brid bloka $1$ spaja $i$-tu i $(i+1)$-u od tih komponenti, a isto vrijedi za $i$-ti brid bloka $3$. Sufiks bloka $1$ duljine $x$ spaja zadnjih $x + 1$ komponenti u jednu, a prefiks bloka $3$ duljine $k - x$ spaja tu komponentu s prvih $k - x$ komponenti — dobili smo stablo.</p>
<p><b>Paran $n$.</b> Neka je $n = 2k + 2$. Ponovno nacrtamo $2k + 1$ vrhova na kružnici, a središte kružnice je vrh $2k + 2$. Točke na kružnici numeriramo ciklički modulo $2k + 1$ (to se ne odnosi na središnji vrh). Blok $i$, za $i$ od $1$ do $2k + 1$, čine bridovi
$$(i, i+1),\ (i-1, i+2),\ \dots,\ (i-k+1, i+k)\quad\text{i}\quad (i+k+1,\ 2k+2),$$
tj. $k$ bridova paralelnih s $(i, i+1)$ i brid od središta do jedine preostale točke. Ispišemo bridove blokova redom za $i = 1, \dots, 2k+1$. Dokaz je isti kao u neparnom slučaju.</p>
''',
},
{
    'letter': 'M',
    'title': 'Most Annoying Constructive Problem',
    'title_hr': 'Najdosadniji konstruktivni zadatak',
    'slug': 'M_most_annoying_constructive_problem',
    'tl': '1 s',
    'ml': '256 MB',
    'statement': r'''
<p>Niz je neparan ako ima neparan broj inverzija. Za zadane $n, k$ odredi postoji li permutacija brojeva $1..n$ s točno $k$ neparnih podnizova (uzastopnih), i ispiši je.</p>
<h3>Ulaz</h3>
<p>Prvi redak sadrži $t$ ($1 \le t \le 10^4$). Svaki primjer sadrži $n, k$ ($1 \le n \le 1000$, $0 \le k \le \frac{n(n-1)}{2}$). Zbroj svih $n^2$ ne prelazi $4 \cdot 10^6$.</p>
<h3>Izlaz</h3>
<p><code>NO</code>, ili <code>YES</code> i permutacija.</p>
''',
    'hints': [
        r'''
<p>Podnizovi duljine $1$ su parni. Za $n \ge 4$ postoji barem $\lfloor \frac{n-1}{2}\rfloor$ parnih podnizova duljine $\ge 2$, pa je maksimum $f(n) = \binom{n}{2} - \lfloor\frac{n-1}{2}\rfloor$; sve $0 \le k \le f(n)$ su dostižne.</p>
''',
        r'''
<p>Konstrukcija rekurzivno po $n-2$: dodavanje $n, n-1$ na kraj povećava broj neparnih točno za $n-1$; ekstremni slučaj $k = f(n)$ dolazi iz uzorka $4,1,6,3,8,5,\dots$; ostatak pokrivaju mali $k$ (jedna rotacija tri elementa) i biranje $p_1, p_n$ oko ekstremne permutacije duljine $n-2$.</p>
''',
    ],
    'coach': [
        ('Opažanje 1: gornja granica',
         r'''
<p>Lema: $n \ge 4 \Rightarrow$ barem $\lfloor\frac{n-1}{2}\rfloor$ parnih podnizova duljine $\ge 2$ (indukcija s rezanjem prva dva elementa; baze $n = 4, 5$ iscrpno). Uzorak $4,1,6,3,8,5,\dots$ (sažet na $[1..n]$) postiže točno toliko: jedini parni podnizovi su $a[2i..2i+1]$.</p>
'''),
        ('Opažanje 2: gradivni prijelazi',
         r'''
<p>Dodaj $n, n-1$ na kraj permutacije duljine $n-2$: $p[n-1..n]$ neparan, a za svaki $i$ parovi $p[i..n-1]$, $p[i..n]$ imaju različite parnosti — točno $n-1$ novih neparnih. Time se pokriva $n-1 \le k \le f(n-2) + n - 1$.</p>
'''),
        ('Algoritam: pokrivanje svih $k$',
         r'''
<p>$k = 0$: identiteta. $1 \le k \le n-2$: $[1..k-1, k+2, k, k+1, k+3..n]$. $k = f(n)$: uzorak. $f(n-2) + n \le k \lt f(n)$: unutra stavi ekstremnu permutaciju duljine $n-2$, a $p_1, p_n$ isprobaj među svih $n^2$ parova uz $O(n^2)$ predizračun doprinosa rubnih elemenata — svaki par u $O(1)$. Baze $n \le 5$ iscrpno.</p>
'''),
        ('Složenost',
         r'''
<p>$O(n^2)$ po testu; $\sum n^2 \le 4 \cdot 10^6$.</p>
'''),
    ],
    'solution': r'''
<p>Podnizove duljine $1$ potpuno zanemarujemo; "podniz" dalje znači podniz duljine $\ge 2$.</p>
<p>Neka je $f(n) = \frac{n(n-1)}{2} - \lfloor \frac{n-1}{2} \rfloor$. Tvrdnja: za $n \ge 4$ tražena permutacija postoji za sve $0 \le k \le f(n)$ i ne postoji za veće $k$. Slučajeve $n \le 3$ riješite sami.</p>
<p><b>Lema.</b> Za $n \ge 4$ mora postojati barem $\lfloor \frac{n-1}{2} \rfloor$ parnih podnizova.</p>
<p><i>Dokaz</i> indukcijom; za $n = 4, 5$ provjerimo iscrpnom pretragom. Neka je $n \ge 6$ i neka permutacija $p$ duljine $n$ ima najviše $\lfloor \frac{n-1}{2} \rfloor - 1$ parnih podnizova. Po indukciji $p[3 : n]$ ih mora imati barem toliko, pa ih $p$ ima točno toliko i svi su u $p[3 : n]$. Dakle $p_1 &gt; p_2 &gt; p_3$ (podnizovi $p[1:2]$, $p[2:3]$ su neparni) i za svaki $i \ge 3$ podnizovi $p[1 : i]$ i $p[2 : i]$ su neparni, pa je broj elemenata u $p[2 : i]$ manjih od $p_1$ paran. Kako su $p_2, p_3 &lt; p_1$, slijedi $p_4, \dots, p_n &gt; p_1$, tj. $p_1 = 3, p_2 = 2, p_3 = 1$. No tada je $p[2 : i]$ za $i \ge 4$ neparan, a $2$ tvori samo jednu inverziju (s $1$), pa je $p[3 : i]$ paran za sve $i \ge 4$ — to je $n - 3$ parnih podnizova, pa $n - 3 \le \lfloor \frac{n-1}{2} \rfloor - 1$, kontradikcija za $n \ge 6$. $\square$</p>
<p><b>Konstrukcija.</b> Za $n \le 5$ sve konstruiramo iscrpnom pretragom. Neka je $n \ge 6$ i pretpostavimo da znamo konstruirati permutacije za sve dopustive parove $(n_1, k)$ s $n_1 &lt; n$. Slučajevi:</p>
<ul>
    <li>$k = 0$: permutacija $[1, 2, \dots, n]$.</li>
    <li>$1 \le k \le n - 2$: permutacija $[1, 2, \dots, k-2, k-1, k+2, k, k+1, k+3, k+4, \dots, n]$.</li>
    <li>$n - 1 \le k \le f(n-2) + n - 1$: uzmimo permutaciju duljine $n - 2$ s $k - (n - 1)$ neparnih podnizova i dodajmo na kraj $n, n-1$. Podniz $p[n-1 : n]$ je neparan, a za svaki $1 \le i \le n-2$ podnizovi $p[i : n-1]$ i $p[i : n]$ imaju različite parnosti, pa smo dodali točno $n - 1$ neparnih podnizova.</li>
    <li>$k = f(n)$: promotrimo beskonačan niz $4, 1, 6, 3, 8, 5, 10, 7, 12, 9, 14, 11, 16, \dots$ (na neparnim pozicijama parni brojevi od $4$, na parnim neparni od $1$; $2$ nedostaje, ali to nije problem). Ključno je da su jedini parni podnizovi tog niza oblika $a[2i : 2i+1]$ (dokaz ostavljamo čitatelju). Uzmemo prvih $n$ elemenata i "sažmemo" ih u permutaciju — ona ima samo $\lfloor \frac{n-1}{2} \rfloor$ parnih podnizova.</li>
    <li>$f(n-2) + n \le k &lt; f(n)$: radi sljedeća konstrukcija — odaberemo $p_1$ i $p_n$, a preostale elemente u $p[2 : n-1]$ rasporedimo prema permutaciji za $(n - 2, f(n-2))$ (dokaz ostavljamo čitatelju). Probamo svih $n^2$ parova $(p_1, p_n)$ dok ne nađemo onaj koji radi; jedan par provjeravamo u $O(1)$ nakon što u $O(n^2)$ predizračunamo koliko neparnih podnizova dodaju pojedini prvi/zadnji elementi.</li>
</ul>
<p>Ukupna složenost $O(n^2)$. (Ako znate napisati provjeru brže od $O(n^2)$, javite autoru.)</p>
''',
},
{
    'letter': 'N',
    'title': 'No Zero-Sum Subsegment',
    'title_hr': 'Bez podsegmenta sa zbrojem nula',
    'slug': 'N_no_zero_sum_subsegment',
    'tl': '2 s',
    'ml': '256 MB',
    'statement': r'''
<p>Zadani su $A, B, C, D$. Prebroji nizove duljine $A + B + C + D$ koji sadrže točno $A$ elemenata $-2$, $B$ elemenata $-1$, $C$ elemenata $1$ i $D$ elemenata $2$, i nemaju podniz (uzastopni) sa zbrojem $0$. Odgovor modulo $998\,244\,353$.</p>
<h3>Ulaz</h3>
<p>Prvi redak sadrži $t$ ($1 \le t \le 10^5$). Svaki primjer sadrži $A, B, C, D$ ($0 \le A, B, C, D \le 10^6$, $A + B + C + D &gt; 0$).</p>
<h3>Izlaz</h3>
<p>Za svaki primjer ispiši odgovor.</p>
''',
    'hints': [
        r'''
<p>Prefiksne sume moraju biti različite: šetnja po $\mathbb{Z}$ skokovima $\pm1, \pm2$ koja ne posjećuje točku dvaput. Zbroj $S \ne 0$; simetrijom uzmi $S \gt 0$.</p>
''',
        r'''
<p>Jedinični segment $[L, L+1]$ može biti prijeđen najviše $3$ puta, i to samo uzorkom $L-1 \to L+1 \to L \to L+2$. Posljedica: šetnja lijevo od $0$ moguća je samo na početku (3 oblika), desno od $S$ samo na kraju (3 oblika); u sredini nema skokova $-2$, a svaki $-1$ je u bloku $+2, -1, +2$ — ostatak je multinomni koeficijent.</p>
''',
    ],
    'coach': [
        ('Opažanje 1: model šetnje',
         r'''
<p>Podsegment sa zbrojem $0$ $\iff$ dvije jednake prefiksne sume. Dakle šetnja iz $0$ s $A$ skokova $-2$, $B$ skokova $-1$, $C$ skokova $+1$, $D$ skokova $+2$, sve točke različite, završava u $S = 2D + C - B - 2A$.</p>
'''),
        ('Opažanje 2: prijelazi preko segmenta',
         r'''
<p>Skokovi koji prelaze $[L, L+1]$: $L \leftrightarrow L+1$, $L \leftrightarrow L+2$, $L-1 \leftrightarrow L+1$ — svaki koristi točke $L$ ili $L+1$, koje se smiju posjetiti jednom. Zato najviše $3$ prijelaza i tada u redoslijedu $L-1 \to L+1 \to L \to L+2$ (ili obrnuto). Nakon prvog ulaska u $\ge 1$ nikad više $\lt 0$.</p>
'''),
        ('Opažanje 3: sredina bez $-2$',
         r'''
<p>Unutar $[X, Y]$ skok $-2$ ($L+2 \to L$) povukao bi $L+1 \to L-1$, pa dalje $L \to L-2$, … beskonačno ulijevo — nemoguće. Skok $-1$ ($L+1 \to L$) mora biti okružen s $L-1 \to L+1$ prije i $L \to L+2$ poslije: blok $(+2, -1, +2)$. Sredina: $C$ jedinica, $B$ blokova, $D' = D - 2B$ dvojki u proizvoljnom poretku — $\frac{(C + B + D')!}{C!\,B!\,D'!}$.</p>
'''),
        ('Algoritam',
         r'''
<p>Početak ima $4$ oblika (bez izleta; $-1,+2$; $k\times(-2), -1, (k+1)\times(+2)$; $k\times(-2), +1, k\times(+2)$), kraj simetrično $4$. Svi $-2$ moraju se potrošiti u početku i kraju, pa za svaku od $16$ kombinacija zbroji po raspodjelama $k_1 + k_2 = A$ (broj rješenja je zatvoren izraz) i pomnoži multinomnim koeficijentom sredine. Faktorijeli do $3 \cdot 10^6$.</p>
'''),
        ('Složenost',
         r'''
<p>$O(1)$ po testu nakon predizračuna, $t \le 10^5$.</p>
'''),
    ],
    'solution': r'''
<p>Izračunajmo zbroj svih elemenata $S = 2D + C - B - 2A$. Ako je $S = 0$, rješenja nema. Ako je $S &lt; 0$, pomnožimo sve s $-1$ (zamijenimo $A \leftrightarrow D$, $B \leftrightarrow C$); odgovor se ne mijenja. Dalje $S &gt; 0$.</p>
<p>Modelirajmo situaciju kao šetnju po cjelobrojnom pravcu: krećemo iz $0$, trebamo napraviti $A$ skokova ulijevo za $2$, $B$ ulijevo za $1$, $C$ udesno za $1$, $D$ udesno za $2$, i nikad ne smijemo posjetiti istu točku dvaput (prefiksne sume moraju biti različite). Ruta završava u $S$.</p>
<p>Ako segment $[L, L+1]$ preskočimo barem $3$ puta: to je moguće samo na $3$ načina — $L \leftrightarrow L+2$, $L \leftrightarrow L+1$, $L-1 \leftrightarrow L+1$ — pa moramo iskoristiti sva tri, a ruta mora sadržavati $L-1 \to L+1 \to L \to L+2$ ili $L+2 \to L \to L+1 \to L-1$.</p>
<p>Promotrimo prvi trenutak kad dođemo u točku $\ge 1$. Nakon toga ne možemo doći u točku $&lt; 0$: to bi značilo da smo segment $[0, 1]$ preskočili triput, što je po gornjem nemoguće jer krećemo iz $0$. Dakle, ako ikad idemo lijevo od $0$, to radimo na samom početku, zatim se vraćamo u $1$ i ostajemo u području $&gt; 0$. Slično, ako ikad idemo u područje $&gt; S$, to je na samom kraju.</p>
<p>Načina da odemo u područje $&lt; 0$ i vratimo se u $1$ ima samo tri:</p>
<ul>
    <li>Način 1: skok ulijevo za $1$, pa udesno za $2$.</li>
    <li>Način 2: $k$ skokova ulijevo za $2$, zatim jedan ulijevo za $1$, zatim $k + 1$ skokova udesno za $2$.</li>
    <li>Način 3: $k$ skokova ulijevo za $2$, zatim jedan udesno za $1$, zatim $k$ skokova udesno za $2$.</li>
</ul>
<p>Načini odlaska u područje $&gt; S$ skokom iz $S - 1$ i povratka u $S$ su simetrični. Imamo dakle $4$ načina "početka" (tri odlaska u $&lt; 0$ ili bez odlaska) i $4$ načina "završetka". Fiksirajmo početak i kraj i promotrimo načine dolaska iz točke $X$ u točku $Y$ ($X \le Y$) s preostalim skokovima, bez izlaska iz $[X, Y]$.</p>
<p>Prvo, ne možemo skočiti ulijevo za $2$: ako skočimo $L+2 \to L$, segment $[L, L+1]$ preskačemo barem triput, pa ruta sadrži $L+2 \to L \to L+1 \to L-1$; ali onda zbog $L+1 \to L-1$ mora sadržavati i $[L, L-2]$, $[L-1, L-3]$ itd. — nemoguće. Drugo, svaki skok ulijevo za $1$, $L+1 \to L$, dio je podrute $L-1 \to L+1 \to L \to L+2$. Dakle mora biti $A = 0$ i $D \ge 2B$, a u konačnici samo slažemo $C$ skokova duljine $1$, $B$ "skokova" duljine $3$ (blokova $+2, -1, +2$) i $D - 2B$ skokova duljine $2$ u proizvoljnom poretku — to je multinomni koeficijent.</p>
<p>Prođimo sve kombinacije početka i kraja ($4^2 = 16$) i zbrojimo brojeve ruta. Za fiksiranu kombinaciju svi $-2$ moraju biti iskorišteni u početku i kraju, pa znamo točan broj svake vrste skoka u početku i kraju zajedno, no postoji nekoliko opcija raspodjele. Primjer: imamo $4$ skoka $-2$, početak je Način 2, a kraj Način 3. Početak koristi $k_1$ skokova $-2$, jedan $-1$ i $k_1 + 1$ skokova $+2$; kraj koristi $k_2$ skokova $-2$, jedan $+1$ i $k_2$ skokova $+2$. Ukupno: $4$ skoka $-2$, jedan $-1$, jedan $+1$ i $5$ skokova $+2$, a broj načina jednak je broju rješenja $k_1 + k_2 = 4$ u pozitivnim cijelim brojevima (tj. $3$). Budući da točno znamo koje skokove trošimo u početku i kraju, broj načina slaganja preostalih skokova računamo kako je opisano gore, i te brojeve pomnožimo.</p>
<p>Uz predizračunate faktorijele i inverzne faktorijele do $3 \cdot 10^6$, složenost je $O(1)$ po primjeru.</p>
''',
},
]
