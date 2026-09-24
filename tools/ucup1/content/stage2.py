"""1st Universal Cup – Stage 2: Hong Kong. Uvezeno iz ručno pisanih stranica (import_legacy.py); naputci i
trenerski koraci iz nekadašnjeg retro_stage2.py."""

STAGE = {
    'no': 2,
    'name': 'Stage 2: Hong Kong',
    'source_name': 'The 2022 ICPC Asia Hong Kong Regional Contest',
    'source_html': r'''
<p>Prijevod službene analize zadataka autorskog tima Sveučilišta Zhejiang: <a href="https://contest.ucup.ac/download.php?type=attachments&amp;id=1099&amp;r=2">Tutorial (en)</a>. Tekst zadatka preveden je prema službenim <a href="https://contest.ucup.ac/download.php?type=attachments&amp;id=1099&amp;r=1">engleskim tekstovima zadataka</a>. Zadatak je dostupan na <a href="https://contest.ucup.ac/contest/1099">Universal Cup Judging System</a>.</p>
''',
}

PROBLEMS = [
{
    'letter': 'A',
    'title': 'TreeScript',
    'title_hr': 'TreeScript',
    'slug': 'A_treescript',
    'tl': '1 s',
    'ml': '1024 MB',
    'statement': r'''
<p>U jeziku TreeScript čvorovi stabla stvaraju se naredbom <code>r[i] = create(r[j], k)</code>: stvara se čvor broj $k$ čiji je roditelj čvor na adresi pohranjenoj u registru <code>r[j]</code>, a adresa novog čvora zapisuje se u <code>r[i]</code> (dopušteno je $i = j$). Korijen je već stvoren i nalazi se u <code>r[0]</code>. Zadano je korijensko stablo s $n$ čvorova (roditelj čvora $i$ je $p_i &lt; i$); treba ga izgraditi s $n - 1$ naredbi uz najmanji mogući broj registara.</p>
<h3>Ulaz</h3>
<p>Prvi redak sadrži broj testnih primjera $T$ ($1 \le T \le 10^5$). Za svaki primjer: $n$ ($2 \le n \le 2 \times 10^5$) te $p_1, \dots, p_n$ ($p_1 = 0$, $1 \le p_i &lt; i$ za $i &gt; 1$). Zbroj svih $n$ ne prelazi $2 \times 10^5$.</p>
<h3>Izlaz</h3>
<p>Za svaki primjer ispiši najmanji potreban broj registara.</p>
''',
    'hints': [
        r'''
<p>Dok gradiš podstabla djece nekog čvora, adresa tog čvora mora ostati u nekom registru sve dok ne kreneš u <em>posljednje</em> dijete — za posljednje dijete taj registar se može ponovno iskoristiti.</p>
''',
        r'''
<p>Obradi djecu po padajućoj „potrebi” registara: $dp_u = \max(dp_{v_1}, dp_{v_2} + 1)$ gdje su $dp_{v_1} \ge dp_{v_2} \ge \dots$, list ima $dp = 1$.</p>
''',
    ],
    'coach': [
        ('Opažanje 1: što se čuva',
         r'''
<p>Naredba <code>create</code> treba adresu roditelja. Nakon što je stvoreno zadnje dijete čvora $u$, adresa $u$ više nikad nije potrebna — može se prebrisati.</p>
'''),
        ('Opažanje 2: redoslijed djece',
         r'''
<p>Podstablo djeteta $v$ gradi se s $dp_v$ registara; dok se gradi, ako $u$ ima još nezavršene djece, treba $+1$ registar za adresu $u$. Zato najskuplje dijete gradi se posljednje (bez dodatka), a ostala s dodatkom $1$ — zamjena poretka nikad ne pomaže.</p>
'''),
        ('Algoritam i složenost',
         r'''
<p>DP po stablu: sortiraj $dp$ djece silazno, $dp_u = \max(dp_{v_1}, dp_{v_2} + 1)$ (samo drugo najveće dijete bitno, ostala su manja ili jednaka). Jedan prolaz: $O(n)$ (ili $O(n \log n)$ sa sortiranjem).</p>
'''),
    ],
    'solution': r'''
<p>Prvo stvaramo "mala" podstabla. Dok stvaramo sva podstabla djece osim "najvećeg", trebamo jedan dodatni registar u kojem čuvamo adresu trenutačnog korijena (jer nam je kasnije još potreban za preostalu djecu). Za najveće podstablo taj registar više nije potreban, pa ga možemo osloboditi.</p>
<p>Dobivamo rekurziju
$$dp_u = \max(dp_{v_1},\ dp_{v_2} + 1),$$
gdje su $v_i$ djeca čvora $u$ poredana tako da vrijedi $dp_{v_1} \ge dp_{v_2} \ge \cdots$ (list ima $dp = 1$). Odgovor je $dp_{\text{korijen}}$, a složenost je $O(n)$.</p>
''',
},
{
    'letter': 'B',
    'title': 'Big Picture',
    'title_hr': 'Velika slika',
    'slug': 'B_big_picture',
    'tl': '1 s',
    'ml': '1024 MB',
    'statement': r'''
<p>Slika ima $n + 1$ redaka i $m + 1$ stupaca. U $i$-tom retku Grammy oboji najljevijih $j$ ($1 \le j \le m$) polja crno s vjerojatnošću $p_{i,j}$, a u $j$-tom stupcu najgornjih $i$ ($1 \le i \le n$) polja crno s vjerojatnošću $q_{i,j}$. Operacije su neovisne, polje može biti obojeno više puta. <b>Ljepota</b> slike je broj maksimalnih 4-povezanih područja iste boje. Izračunaj očekivanu ljepotu modulo $998\,244\,353$.</p>
<h3>Ulaz</h3>
<p>Prvi redak sadrži $n$ i $m$ ($1 \le n, m \le 1000$). Slijedi $n$ redaka s $m$ brojeva $p_{i,j}$ (vjerojatnosti modulo $998\,244\,353$; zbroj po retku je $1$), zatim $n$ redaka s $m$ brojeva $q_{i,j}$ (zbroj po stupcu je $1$).</p>
<h3>Izlaz</h3>
<p>Ispiši očekivanu ljepotu modulo $998\,244\,353$.</p>
''',
    'hints': [
        r'''
<p>Sva su obojena polja povezana preko prvog retka i prvog stupca — crnih komponenata je uvijek točno $1$. Treba očekivani broj bijelih komponenata.</p>
''',
        r'''
<p>Svaka bijela komponenta ima točno jedno polje čiji su i desni i donji susjed obojeni (njezin donje-desni „kut”). Linearnost očekivanja: zbroji po poljima vjerojatnost tog događaja, koju daju prefiksni/sufiksni zbrojevi $p$ po redcima i $q$ po stupcima.</p>
''',
    ],
    'coach': [
        ('Opažanje 1: crne komponente',
         r'''
<p>Svaki obojeni redak i stupac dodiruje polje $(i, 1)$ odn. $(1, j)$, a ona su sva povezana u prvom retku/stupcu, koji su u cijelosti obojeni ($j, i \ge 1$). Dakle točno jedna crna komponenta.</p>
'''),
        ('Opažanje 2: karakterizacija bijelih komponenata',
         r'''
<p>Bijela regija je „stepenasta” (obojena polja tvore Youngov dijagram u gornjem lijevom kutu proširen dodatnim segmentima); svaka bijela komponenta ima jedinstveno polje kojemu su desni i donji susjed crni (ili izvan slike — zato dodatni redak i stupac). Bijelih komponenata $= \#\{(i,j) \text{ bijelo}, (i, j+1) \text{ crno}, (i+1, j) \text{ crno}\}$.</p>
'''),
        ('Algoritam: linearnost očekivanja',
         r'''
<p>Polje $(i,j)$ je bijelo ako redak $i$ boji manje od $j$ i stupac $j$ boji manje od $i$ polja: $P = \bigl(\sum_{t \lt j} p_{i,t}\bigr)\bigl(\sum_{t \lt i} q_{t,j}\bigr)$. Susjedi su obojeni: kombiniraj isto s komplementima (desni susjed $(i, j+1)$ je crn ako redak $i$ boji $\ge j+1$ <em>ili</em> stupac $j+1$ boji $\ge i$), pazeći na neovisnost redaka i stupaca — događaji za redak $i$, stupce $j$ i $j+1$ i redak $i+1$ su neovisni.</p>
'''),
        ('Složenost',
         r'''
<p>$\Theta(nm)$ uz prefiksne zbrojeve modulo $998\,244\,353$.</p>
'''),
    ],
    'solution': r'''
<p>Lako je uočiti da je broj crnih povezanih područja uvijek točno $1$ (sva obojena polja povezana su preko prvog retka i prvog stupca).</p>
<p>Za svako neobojeno povezano područje postoji točno jedno polje čiji su i desni i donji susjed obojeni (njegov "donji desni kut"). Stoga je dovoljno izračunati očekivani broj neobojenih polja čiji su desni i donji susjed oba obojena, a to se radi tako da se za svako polje zasebno izračuna vjerojatnost tog događaja (iz prefiksnih/sufiksnih suma vjerojatnosti $p$ po recima i $q$ po stupcima).</p>
<p>Vremenska složenost je $\Theta(nm)$.</p>
''',
},
{
    'letter': 'C',
    'title': 'Painting Grid',
    'title_hr': 'Bojanje mreže',
    'slug': 'C_painting_grid',
    'tl': '1 s',
    'ml': '1024 MB',
    'statement': r'''
<p>Oboji polja mreže $n \times m$ crno i bijelo tako da:</p>
<ol>
    <li>broj bijelih polja jednak je broju crnih;</li>
    <li>nema dva jednaka retka;</li>
    <li>nema dva jednaka stupca.</li>
</ol>
<h3>Ulaz</h3>
<p>Prvi redak sadrži broj testnih primjera $T$ ($1 \le T \le 2000$). Svaki primjer sadrži $n$ i $m$ ($1 \le n, m \le 1000$). Zbroj svih $nm$ ne prelazi $10^6$.</p>
<h3>Izlaz</h3>
<p>Za svaki primjer ispiši <code>NO</code> ako rješenje ne postoji, inače <code>YES</code> i $n$ redaka po $m$ znakova (<code>0</code> bijelo, <code>1</code> crno).</p>
''',
    'hints': [
        r'''
<p>Nemoguće ako su $n$ i $m$ oba neparni (ukupan broj polja neparan) ili ako je $n \gt 2^m$ odn. $m \gt 2^n$ (Dirichlet). Inače postoji konstrukcija.</p>
''',
        r'''
<p>Neka je $m$ paran. Prvih $\lceil \log_2 m \rceil$ redaka napravi „binarno” tako da su svi stupci različiti, svaki redak balansiran i lijeva polovica komplement desne. Ostale retke dodaj u parovima $s, \neg s$ (par je balansiran), preskačući nizove već korištene; na kraju upotrijebi odbačene.</p>
''',
    ],
    'coach': [
        ('Opažanje 1: nužni uvjeti',
         r'''
<p>Balans traži paran $nm$; različiti retci traže $n \le 2^m$, različiti stupci $m \le 2^n$. Tvrdnja: ti uvjeti su i dovoljni.</p>
'''),
        ('Opažanje 2: osiguraj različite stupce rano',
         r'''
<p>Uz paran $m$ (bez smanjenja općenitosti), $\lceil \log_2 m \rceil$ redaka dovoljno je da svi stupci budu različiti. Podijeli pa vladaj: redak $t$ dijeli blokove na pola i boji ih naizmjence, uz trik da je desna polovica komplement lijeve — tako je svaki redak balansiran.</p>
'''),
        ('Algoritam: ostatak u komplementarnim parovima',
         r'''
<p>Nizovi duljine $m$ dolaze u parovima $(s, \neg s)$ s ukupno $m$ crnih polja. Dodavanje para ne mijenja balans niti stvara jednake stupce (stupci su već različiti; dodavanje redaka ih ne može izjednačiti). Parove u kojima je jedan član već upotrijebljen odloži; popuni parovima do kraja, a preostale (neparan broj) retke popuni odloženim pojedinačnim nizovima — njihovi su parnjaci već u mreži, pa balans ostaje.</p>
'''),
        ('Složenost',
         r'''
<p>$O(nm)$ po testu; $\sum nm \le 10^6$. Ako je $n$ paran i $m$ neparan, transponiraj.</p>
'''),
    ],
    'solution': r'''
<p>Ako su $n$ i $m$ oba neparni, rješenje ne postoji. Ako je $n &gt; 2^m$ ili $m &gt; 2^n$, po Dirichletovu principu rješenje ne postoji (ne može biti više različitih redaka nego binarnih nizova duljine $m$). Inače rješenje postoji; barem jedan od $n$, $m$ je paran, pa bez smanjenja općenitosti neka je $m$ paran.</p>
        <p>Za prvih $\lceil \log_2 m \rceil$ redaka osiguramo sljedeća svojstva: svaki redak ima jednak broj crnih i bijelih polja, nema jednakih redaka i nema jednakih stupaca. To se postiže metodom "podijeli pa vladaj". Primjer za $m = 10$ prikazan je dolje; uočimo da se prvih $5$ stupaca može dobiti iz zadnjih $5$ zamjenom $0 \leftrightarrow 1$:</p>
        <pre>0000011111
0101010101
0011011001
0000111110</pre>
        <p>Preostale retke promatramo kao binarne nizove i sparujemo niz $s$ s njegovim komplementom $\neg s$. Ako oba niza iz para stavimo u mrežu, ukupan broj crnih i bijelih polja ostaje jednak. Ako se jedan od nizova para već pojavio među prethodnim recima, taj par privremeno odbacujemo (barem jedan redak bit će odbačen). Preostale sparene retke stavljamo u mrežu koliko god možemo; ostat će nekoliko nepopunjenih redaka, dok popunjeni reci zadovoljavaju sva tri uvjeta. U zadnjem koraku nepopunjene retke popunimo prethodno odbačenim recima — tri uvjeta ostaju zadovoljena.</p>
''',
},
{
    'letter': 'D',
    'title': 'Shortest Path Query',
    'title_hr': 'Upit najkraćeg puta',
    'slug': 'D_shortest_path_query',
    'tl': '2 s',
    'ml': '1024 MB',
    'statement': r'''
<p>Zadan je usmjereni aciklički graf s $n$ vrhova i $m$ bridova; svaki brid je crn ili bijel, a svaki je vrh dostižan iz vrha $1$. Za svaki od $q$ upita $(a_i, b_i, x_i)$ ispiši duljinu najkraćeg puta od vrha $1$ do vrha $x_i$ ako svaki crni brid ima duljinu $a_i$, a svaki bijeli duljinu $b_i$.</p>
<h3>Ulaz</h3>
<p>Prvi redak sadrži $n$ i $m$ ($1 \le n \le 50\,000$, $1 \le m \le 100\,000$). Slijedi $m$ bridova $u_i, v_i, c_i$ ($1 \le u_i &lt; v_i \le n$, $v_i - u_i \le 1000$, $c_i \in \{0, 1\}$; $0$ je crno). Zatim $q$ ($1 \le q \le 50\,000$) upita $a_i, b_i, x_i$ ($1 \le a_i, b_i \le 10\,000$).</p>
<h3>Izlaz</h3>
<p>Za svaki upit ispiši duljinu najkraćeg puta.</p>
''',
    'hints': [
        r'''
<p>Najkraći put za upit $(a, b)$ je $\min_{\text{putovi}}(a \cdot \#\text{crnih} + b \cdot \#\text{bijelih})$: minimizacija linearne funkcije nad skupom točaka $(\#\text{crnih}, \#\text{bijelih})$ — bitna je samo donja konveksna ljuska.</p>
''',
        r'''
<p>Za svaki vrh drži samo točke na konveksnoj ljusci; ljuska vrha $v$ = ljuska unije ljusaka prethodnika pomaknutih za $(1,0)$ ili $(0,1)$. Ljuska ima $O(n^{2/3})$ točaka (broj cjelobrojnih točaka na konveksnoj krivulji u kvadratu stranice $n$), pa upit prođe sve točke.</p>
''',
    ],
    'coach': [
        ('Opažanje 1: DP po broju crnih bridova',
         r'''
<p>$f_{i,j}$ = najmanje bijelih bridova do vrha $i$ uz točno $j$ crnih. Odgovor za upit $x$: $\min_j (a j + b f_{x,j})$. Stanja $O(n^2)$ — previše.</p>
'''),
        ('Opažanje 2: samo konveksna ljuska',
         r'''
<p>Minimum linearne funkcije $a j + b f$ s $a, b \gt 0$ nad skupom točaka postiže se na donjoj-lijevoj konveksnoj ljusci. Ljuska Minkowskijeva zbroja / unije: $\mathrm{hull}(v) = \mathrm{hull}\bigl(\bigcup_{u \to v} \mathrm{hull}(u) + e_{c}\bigr)$, gdje je $e_c$ jedinični pomak ovisno o boji.</p>
'''),
        ('Opažanje 3: veličina ljuske',
         r'''
<p>Konveksni poligon s cjelobrojnim vrhovima u $[0,n]^2$ ima $O(n^{2/3})$ vrhova (različiti primitivni smjerovi bridova rastu kubično po duljini). Zato je ukupan rad $O((m + q) n^{2/3})$.</p>
'''),
        ('Algoritam',
         r'''
<p>Topološki poredak je zadan ($u \lt v$). Za svaki vrh spoji ljuske prethodnika (sortirano po $x$ pa Andrewov monotoni lanac) i za upite prođi točke ljuske vrha $x_i$. Uvjet $v - u \le 1000$ omogućuje odbacivanje ljusaka vrhova koji više neće biti prethodnici, radi memorije.</p>
'''),
        ('Složenost',
         r'''
<p>$\Theta((m + q) n^{2/3})$ vremena.</p>
'''),
    ],
    'solution': r'''
<p>Razmotrimo jednostavno dinamičko programiranje: $f_{i,j}$ je najmanji broj bijelih bridova kojima moramo proći od vrha $1$ do vrha $i$ ako smo prošli točno $j$ crnih bridova. Stanja ima $\Theta(n^2)$, što je nažalost presporo.</p>
<p><b>Lema 1.</b> Za fiksni vrh $i$, ako svako stanje $f_{i,j}$ nacrtamo kao točku $(j, f_{i,j})$ u ravnini, na odgovor utječu samo stanja na (donjoj) konveksnoj ljusci — jer je za upit cilj $\min_j (a \cdot j + b \cdot f_{i,j})$, a to je minimizacija linearne funkcije nad skupom točaka.</p>
<p><b>Lema 2.</b> Za fiksni vrh $i$ na konveksnoj ljusci ima najviše $\Theta(n^{2/3})$ stanja.</p>
<p>Stoga za svaki vrh čuvamo samo stanja na konveksnoj ljusci (ljusku vrha $v$ gradimo spajanjem ljusaka prethodnika pomaknutih za $(1, 0)$ ili $(0, 1)$ ovisno o boji brida), a na upit odgovaramo tako da jednostavno prođemo sve točke ljuske vrha $x_i$. Vremenska složenost je $\Theta((m + q)\, n^{2/3})$.</p>
''',
},
{
    'letter': 'E',
    'title': 'Goose, goose, DUCK?',
    'title_hr': 'Guska, guska, PATKA?',
    'slug': 'E_goose_goose_duck',
    'tl': '5 s',
    'ml': '1024 MB',
    'statement': r'''
<p>Zadan je niz $a$ duljine $n$ (guska $i$ obavlja zadatak $a_i$) i broj $k$. Plan je interval $[l, r]$ gusaka. Plan je opasan ako postoji zadatak koji u tom intervalu obavlja <b>točno</b> $k$ gusaka. Prebroji planove koji nisu opasni, tj. intervale u kojima se nijedna vrijednost ne pojavljuje točno $k$ puta.</p>
<h3>Ulaz</h3>
<p>Prvi redak sadrži $n$ i $k$ ($1 \le n, k \le 10^6$). Drugi redak sadrži $a_1, \dots, a_n$ ($1 \le a_i \le 10^6$).</p>
<h3>Izlaz</h3>
<p>Ispiši broj neopasnih planova.</p>
''',
    'hints': [
        r'''
<p>Fiksiraj desni kraj $r$ i pitaj: koji su lijevi krajevi $l$ „loši”? Vrijednost $x$ s pojavama $p_1 \lt \dots \lt p_m$ u $[1,r]$ ($m \ge k$) zabranjuje točno $l \in (p_{m-k}, p_{m-k+1}]$.</p>
''',
        r'''
<p>Pomicanjem $r$ mijenja se samo interval vrijednosti $a_r$: stari $-1$, novi $+1$. Segmentno stablo s dodavanjem na interval i (minimum, broj minimuma): ako je minimum $0$, broj minimuma je broj dobrih $l$.</p>
''',
    ],
    'coach': [
        ('Opažanje 1: skup loših lijevih krajeva po vrijednosti',
         r'''
<p>Za fiksni $r$ i vrijednost $x$, broj pojava u $[l, r]$ jednak je $k$ točno kad $l$ leži između $(m-k)$-te i $(m-k+1)$-ve pojave — jedan kontinuirani interval. Interval $[l, r]$ je dobar ako ne leži ni u jednom takvom intervalu.</p>
'''),
        ('Opažanje 2: inkrementalno po $r$',
         r'''
<p>Prelaskom $r \to r+1$ mijenja se samo lista pojava od $a_{r+1}$; njezin zabranjeni interval se pomiče (stari se briše, novi dodaje). Ostale vrijednosti ostaju netaknute.</p>
'''),
        ('Algoritam: brojanje nula',
         r'''
<p>Polje $c_l$ = broj vrijednosti koje zabranjuju $l$. Treba: dodaj $\pm1$ na interval, prebroji $l \le r$ s $c_l = 0$. Kako je $c_l \ge 0$, to je „broj pojavljivanja minimuma ako je minimum $0$” — klasično lijeno segmentno stablo s parom (min, count).</p>
'''),
        ('Složenost',
         r'''
<p>$\Theta(n \log n)$.</p>
'''),
    ],
    'solution': r'''
<p>Prolazimo po desnom kraju intervala $r$ i za svaki $l \le r$ održavamo je li $l$ dopušten lijevi kraj.</p>
<p>Za element $x$ neka su njegove pojave u $[1, r]$ na pozicijama $p_1, p_2, \dots, p_m$ uz $m \ge k$. Tada su nedopušteni lijevi krajevi (zbog $x$) točno oni u intervalu $[p_{m-k} + 1,\ p_{m-k+1}]$ (uz $p_0 = 0$). Kada $r$ prijeđe iz $r - 1$ u $r$, mijenja se samo interval elementa $a_r$: stari interval uklonimo (dodamo $-1$), novi dodamo ($+1$). Za svaki $l$ održavamo broj elemenata zbog kojih je $l$ nedopušten; problem se svodi na dodavanje $\pm 1$ na interval i brojanje pozicija na kojima je globalni minimum (ako je minimum $0$, to je broj dopuštenih lijevih krajeva). To se radi segmentnim stablom koje čuva minimum i broj pojavljivanja minimuma.</p>
<p>Vremenska složenost je $\Theta(n \log n)$.</p>
''',
},
{
    'letter': 'F',
    'title': 'Sum of Numbers',
    'title_hr': 'Zbroj brojeva',
    'slug': 'F_sum_of_numbers',
    'tl': '1 s',
    'ml': '1024 MB',
    'statement': r'''
<p>Zadano je $n$ znamenki od <code>1</code> do <code>9</code>. Umetni točno $k$ znakova <code>+</code> tako da izraz (zbroj $k + 1$ brojeva) ima najmanju moguću vrijednost.</p>
<h3>Ulaz</h3>
<p>Prvi redak sadrži broj testnih primjera $T$ ($1 \le T \le 2 \times 10^4$). Za svaki primjer: $n$ i $k$ ($2 \le n \le 2 \times 10^5$, $1 \le k \le 6$, $k &lt; n$) te niz od $n$ znamenki. Zbroj svih $n$ ne prelazi $2 \times 10^5$.</p>
<h3>Izlaz</h3>
<p>Za svaki primjer ispiši najmanju vrijednost izraza.</p>
''',
    'hints': [
        r'''
<p>Duljine susjednih brojeva u optimalnom rješenju razlikuju se najviše za $1$ (dulji broj za red veličine više košta), pa su sve duljine $\approx \frac{n}{k+1}$: $L$ ili $L \pm 1$.</p>
''',
        r'''
<p>Prođi sve $3^k$ (zapravo $\approx 3^k/(k+1)$ s točnim zbrojem $n$) rasporede duljina i za svaki zbroji $k+1$ velikih brojeva u $O(n)$; usporedi zbrojeve kao stringove. $k \le 6$ pa je to brzo.</p>
''',
    ],
    'coach': [
        ('Opažanje: gotovo jednake duljine',
         r'''
<p>Ako se dva broja razlikuju u duljini za $\ge 2$, prijenos jedne znamenke s duljeg na kraći smanjuje zbroj (znamenke su $\ge 1$, a dulji broj gubi barem $10^{d-1}$). Zato su duljine $\lfloor \frac{n}{k+1}\rfloor$ ili $\lceil \frac{n}{k+1} \rceil$, s malim odstupanjima $\pm1$ oko baze.</p>
'''),
        ('Redukcija: enumeracija',
         r'''
<p>Fiksiraj baznu duljinu $L$ i za svaki od $k+1$ brojeva odaberi $L-1, L, L+1$ (uz pozitivnost); zadrži rasporede sa zbrojem $n$. Ima ih $O(3^k)$, s $k \le 6$ najviše $729$.</p>
'''),
        ('Algoritam i složenost',
         r'''
<p>Za raspored: rastavi niz, zbroji brojeve kao velike brojeve (ili od kraja prema početku, $O(n)$), zadrži minimum. Ukupno $O\!\left(\frac{3^k}{k+1} n\right)$ po testu; $\sum n \le 2 \cdot 10^5$.</p>
'''),
    ],
    'solution': r'''
<p>Očito je da se duljine dvaju susjednih brojeva u optimalnom rješenju smiju razlikovati samo za $-1$, $0$ ili $1$ (svi brojevi trebaju biti približno jednake duljine $\approx n/(k+1)$, jer bi dulji broj imao za red veličine veću vrijednost). Stoga postoji $3^k$ načina odabira niza duljina, ali samo otprilike $\frac{1}{k+1}$ njih ima ispravan ukupni zbroj duljina — koji točno ovisi o $n \bmod (k + 1)$. Dobivamo rješenje složenosti
$$O\!\left(\frac{3^k}{k+1}\, n\right),$$
jer za svaki raspored duljina trebamo zbrojiti velike brojeve u $O(n)$. Moguće je dodati odsijecanja radi brzine, ali i naivna implementacija je dovoljno brza.</p>
''',
},
{
    'letter': 'G',
    'title': 'Paddle Star',
    'title_hr': 'Zvijezda veslo',
    'slug': 'G_paddle_star',
    'tl': '1 s',
    'ml': '1024 MB',
    'statement': r'''
<p>Zoe iz točke $X$ ispaljuje zvijezdu koja putuje po lomljenoj liniji $X \to Y \to Z$, gdje je $|XY| = \ell_1$ i $|YZ| = \ell_2$. Kut između smjera gledanja i $\overrightarrow{XY}$ je $\theta \in [-\alpha, \alpha]$, a kut između $\overrightarrow{XY}$ i $\overrightarrow{YZ}$ je $\varphi \in [-\beta, \beta]$. Izračunaj ukupnu površinu koju zvijezda može pogoditi (uniju svih mogućih putanja).</p>
<h3>Ulaz</h3>
<p>Prvi redak sadrži $T$ ($1 \le T \le 10^5$). Svaki primjer sadrži $\ell_1, \ell_2, \alpha, \beta$ ($1 \le \ell_2 \le \ell_1 \le 10^9$, $0 \le \alpha \le 90$, $0 \le \beta &lt; 180$; kutovi u stupnjevima).</p>
<h3>Izlaz</h3>
<p>Za svaki primjer ispiši površinu; dopuštena je apsolutna ili relativna greška $10^{-6}$.</p>
''',
    'hints': [
        r'''
<p>Unija putanja = kružni isječak polumjera $\ell_1 + \ell_2$ s kutom $2\alpha$ plus područja koja opisuje drugi štap $YZ$ okretanjem za $\varphi \in [-\beta, \beta]$ na rubnim položajima $\theta = \pm\alpha$.</p>
''',
        r'''
<p>Za $\beta \le 90^\circ$: $(\ell_1+\ell_2)^2\alpha + \ell_2^2\beta$ (radijani). Za $\beta \gt 90^\circ$ zvijezda „prelazi” iza točke $Y$, pa se pojavljuje dodatna površina ispod isječka; razlikuj slučajeve po odnosu $2\alpha$ i kuta $\angle CBA$ te $\angle BCA$ i $\frac{\pi}{2}$.</p>
''',
    ],
    'coach': [
        ('Opažanje 1: rastav unije',
         r'''
<p>Za fiksni $\theta$, štap $YZ$ pomiče se po luku i pokriva isječak polumjera $\ell_2$ oko $Y$ s kutom $2\beta$; kad $\theta$ prelazi $[-\alpha, \alpha]$, $Y$ ide po luku polumjera $\ell_1$. Za $\beta \le \frac{\pi}{2}$ unija je „veliki isječak + dva bočna isječka polumjera $\ell_2$ kuta $\beta$”.</p>
'''),
        ('Opažanje 2: veliki $\x08eta$',
         r'''
<p>Ako je $\beta \gt \frac{\pi}{2}$, krajnja točka $Z$ na rubnom položaju može biti niže (bliže $X$) od $Y$; najniža točka štapa nije više cijeli štap, pa se ispod velikog isječka dodaje površina omeđena lukom polumjera $\ell_2$ i dužinama prema $X$. Nacrtaj trokut $A = X$, $B = Y$, $C = Z$ na rubnom položaju $\varphi = \beta$.</p>
'''),
        ('Algoritam: analiza slučajeva',
         r'''
<p>Razlikuj: (1) je li $2\alpha$ veći od kuta $\angle CBA$ (preklapaju li se dodatne površine dviju strana), (2) je li $\angle BCA \ge \frac{\pi}{2}$ (je li najbliža točka štapa $X$-u sam $C$ ili nožište okomice). Svaki slučaj daje zbroj kružnih isječaka i trokuta; formule po $\ell_1, \ell_2, \alpha, \beta$.</p>
'''),
        ('Numerika i složenost',
         r'''
<p>Argumente $\arccos/\arcsin$ stegni na $[-1, 1]$ prije poziva (zaokruživanje!). $\Theta(1)$ po upitu, $T \le 10^5$.</p>
'''),
    ],
    'solution': r'''
<p>Kada je $\beta \le \frac{\pi}{2}$, odgovor je
$$(\ell_1 + \ell_2)^2 \alpha + \ell_2^2 \beta$$
(kutovi u radijanima): kružni isječak polumjera $\ell_1 + \ell_2$ s kutom $2\alpha$ plus dva isječka polumjera $\ell_2$ s kutom $\beta$ na krajevima.</p>
<p>U suprotnom ($\beta &gt; \frac{\pi}{2}$) "najniža točka" segmenta $BC$ (tj. $YZ$) više nije cijeli štap, nego jedna točka na $BC$, pa se ispod isječka pojavljuje dodatna površina. Pretpostavimo da je $\varphi$ dosegnuo $\beta$; tada treba razlikovati slučajeve prema odnosu</p>
<ul>
    <li>$2\alpha$ i kuta $\angle CBA$,</li>
    <li>$\angle BCA$ i $\frac{\pi}{2}$,</li>
</ul>
<p>što daje četiri situacije koje se zasebno računaju (površine kružnih isječaka i trokuta). Pri pozivanju inverznih trigonometrijskih funkcija budite oprezni — zbog grešaka zaokruživanja argument može ispasti izvan $[-1, 1]$ i rezultat postati <code>nan</code>.</p>
<p>Vremenska složenost je $\Theta(1)$ po upitu.</p>
''',
},
{
    'letter': 'H',
    'title': 'Another Goose Goose Duck Problem',
    'title_hr': 'Još jedan zadatak o guskama i patki',
    'slug': 'H_another_goose_goose_duck_problem',
    'tl': '1 s',
    'ml': '1024 MB',
    'statement': r'''
<p>Patka ima vještinu ubijanja čije hlađenje traje $a$ sekundi, gdje $a$ može biti proizvoljan cijeli broj iz $[l, r]$. Patka susreće gusku svakih $b$ sekundi; gusku može ubiti samo ako je vještina spremna, inače guska pobjegne. Koliko je najmanje vremena potrebno da ubije točno $k$ gusaka?</p>
<h3>Ulaz</h3>
<p>Jedan redak sadrži $l, r, b, k$ ($1 \le l \le r \le 10^9$, $1 \le b, k \le 10^9$).</p>
<h3>Izlaz</h3>
<p>Ispiši traženo vrijeme.</p>
''',
    'hints': [
        r'''
<p>Kraće hlađenje nikad ne šteti: uzmi $a = l$.</p>
''',
        r'''
<p>Guske dolaze u trenucima $b, 2b, 3b, \dots$; nakon ubojstva sljedeće je moguće u prvom višekratniku od $b$ koji je $\ge$ trenutak $+\, l$, tj. nakon $\lceil l/b \rceil b$ sekundi. Ukupno $\lceil l/b \rceil \cdot b \cdot k$.</p>
''',
    ],
    'coach': [
        ('Opažanje',
         r'''
<p>Broj $a$ je parametar koji biramo; svaka strategija s $a \gt l$ izvediva je i s $a = l$ (vještina je ranije spremna), pa je $a = l$ optimalno.</p>
'''),
        ('Redukcija',
         r'''
<p>Ubojstva su u trenucima koji su višekratnici od $b$ i međusobno razmaknuti barem $l$ sekundi (vještina se puni od trenutka uporabe). Najmanji dopušteni razmak je $\lceil l/b \rceil b$, a isti razmak vrijedi i do prvog ubojstva, pa je $k$-to ubojstvo najranije u trenutku $k \cdot \lceil l/b \rceil b$.</p>
'''),
        ('Algoritam',
         r'''
<p>$\lceil l/b \rceil \cdot b \cdot k$ u 64-bitnoj aritmetici ($\le 10^9 \cdot 2 \cdot 10^9$ ne stane u 32 bita). $\Theta(1)$.</p>
'''),
    ],
    'solution': r'''
<p>Uvijek je najbolje odabrati najkraće hlađenje, $a = l$ sekundi. Između dva ubojstva prođe najmanje $l$ sekundi, a guske dolaze u trenucima koji su višekratnici od $b$, pa je razmak između ubojstava $\lceil l / b \rceil \cdot b$. Odgovor je
$$\left\lceil \frac{l}{b} \right\rceil \cdot b \cdot k.$$</p>
<p>Vremenska složenost je $\Theta(1)$.</p>
''',
},
{
    'letter': 'I',
    'title': 'Range Closest Pair of Points Query',
    'title_hr': 'Upit najbližeg para točaka na intervalu',
    'slug': 'I_range_closest_pair_of_points_query',
    'tl': '9 s',
    'ml': '1024 MB',
    'statement': r'''
<p>Zadano je $n$ točaka $p_1, \dots, p_n$ u ravnini. Za svaki od $q$ upita $(l_i, r_i)$ pronađi par točaka $(u, v)$ s $l_i \le u &lt; v \le r_i$ s najmanjom euklidskom udaljenosti i ispiši kvadrat te udaljenosti.</p>
<h3>Ulaz</h3>
<p>Prvi redak sadrži $n$ i $q$ ($2 \le n \le 250\,000$, $1 \le q \le 250\,000$). Slijedi $n$ točaka $x_i, y_i$ ($1 \le x_i, y_i \le 10^8$) i $q$ upita $l_i, r_i$ ($1 \le l_i &lt; r_i \le n$).</p>
<h3>Izlaz</h3>
<p>Za svaki upit ispiši $(x_u - x_v)^2 + (y_u - y_v)^2$.</p>
''',
    'hints': [
        r'''
<p>Podijeli udaljenosti po skali: sustav ćelija $k$ (ćelije $2^{k+1} \times 2^{k+1}$) hvata parove s udaljenosti u $[2^k, 2^{k+1})$ — takvi su u istoj ili susjednoj ćeliji ($3 \times 3$).</p>
''',
        r'''
<p>Offline po rastućem desnom kraju $r$: kad dodaš $p_r$, u svakom sustavu provjeri $3\times3$ okolinu; ako nađeš $p_j$ na udaljenosti $\lt 2^k$, iz sustava $k$ izbaci sve točke s indeksom $\le j$ (za intervale koji sadrže $i$ i $j$ ne mogu dati bolji par). Tada ćelija drži $O(1)$ točaka. Ažuriranja „za sve $l \le j$: ans $= \min(\cdot, d)$” + upiti — Fenwick po $l$ s prefiks-minimumom.</p>
''',
    ],
    'coach': [
        ('Opažanje 1: skale',
         r'''
<p>Ako je $\mathrm{dist}(p_i, p_j) \in [2^k, 2^{k+1})$, točke leže u susjednim ćelijama mreže koraka $2^{k+1}$. Skala ima $\log 10^8 \approx 27$; po skali gledamo $9$ ćelija.</p>
'''),
        ('Opažanje 2: pročišćavanje (pruning)',
         r'''
<p>Ako je $\mathrm{dist}(p_i, p_j) \lt 2^k$ i $j \lt i$, svaki upit koji uključuje $i$ i $j$ ima odgovor $\lt 2^k$, pa točke s indeksom $\le j$ u sustavu $k$ nikad više nisu korisne — sve buduće $r \ge i$. Nakon brisanja svake dvije preostale točke u sustavu $k$ su udaljene $\ge 2^k$, pa u ćeliju $2^{k+1}\times 2^{k+1}$ stane $O(1)$ točaka.</p>
'''),
        ('Redukcija: kandidatni parovi',
         r'''
<p>Svako $r$ proizvede $O(\log 10^8)$ parova $(j, d)$: „za sve upite s $l \le j$ i $r' \ge r$ odgovor $\le d$”. Offline po $r$: treba strukturu za prefiks-min ažuriranja po $l$ i točkovne upite $\min$ po $l$ — Fenwick ($O(\log n)$) ili sqrt-dekompozicija ($O(1)$ ažuriranje, $O(\sqrt n)$ upit).</p>
'''),
        ('Složenost',
         r'''
<p>$\Theta(n \log n \log 10^8 + q \log n)$ ili $\Theta(n \log 10^8 + q\sqrt n)$; hash-mapa po ćelijama, brisanje pokazivačem „najmanji živi indeks” po sustavu.</p>
'''),
    ],
    'solution': r'''
<p>Napravimo $\Theta(\log 10^8)$ <b>sustava ćelija</b>. Sustav $k$ pomaže nam pronaći parove točaka čija je udaljenost u $[2^k, 2^{k+1})$: u njemu se točka $(x, y)$ smješta u ćeliju $\left(\lfloor x / 2^{k+1} \rfloor, \lfloor y / 2^{k+1} \rfloor\right)$.</p>
<p>Upite rješavamo offline: pomičemo desni kraj udesno i za svaki lijevi kraj pamtimo odgovor. Kada desni kraj dođe na poziciju $i$ (točka $p_i$), trebamo pronaći neke točke s indeksom manjim od $i$ i ažurirati odgovor. U svakom sustavu ćelija na odgovor mogu utjecati samo točke u ćelijama susjednima ćeliji u koju upada $p_i$; zato u svakom sustavu prođemo sve točke u susjednih $3 \times 3$ ćelija i zatim $p_i$ dodamo u sustav.</p>
<p>Da bismo ograničili broj točaka po ćeliji: ako pronađemo točku $p_j$ čija je udaljenost od $p_i$ manja od $2^k$, iz $k$-tog sustava uklonimo sve točke s indeksom $\le j$ (za bilo koji upit koji sadrži $i$ i $j$ one više ne mogu dati bolji par u tom rasponu udaljenosti). Budući da je ćelija veličine $2^{k+1} \times 2^{k+1}$, a svake su dvije preostale točke udaljene barem $2^k$, u svakoj ćeliji ostaje $\Theta(1)$ točaka. Dakle, pri svakom pomaku desnog kraja pronađemo $\Theta(\log 10^8)$ parova točaka kojima ažuriramo odgovor.</p>
<p>Preostaje struktura podataka za $\Theta(n \log 10^8)$ ažuriranja oblika "za sve lijeve krajeve $\le j$ odgovor je $\min$ s vrijednošću $d$" i $\Theta(q)$ upita. Možemo koristiti Fenwickovo stablo ($\Theta(\log n)$ – $\Theta(\log n)$) ili sqrt-dekompoziciju ($\Theta(1)$ – $\Theta(\sqrt n)$). Ukupna složenost je $\Theta(n \log n \log 10^8 + q \log n)$, odnosno $\Theta(n \log 10^8 + q \sqrt n)$.</p>
''',
},
{
    'letter': 'J',
    'title': 'Dice Game',
    'title_hr': 'Igra s kockicom',
    'slug': 'J_dice_game',
    'tl': '5 s',
    'ml': '1024 MB',
    'statement': r'''
<p>Kockica ima $n$ strana s brojevima $0, \dots, n - 1$. Putata baci kockicu i dobije $x$. Budada zatim može završiti igru (rezultat $x$) ili baciti kockicu još jednom, dobiti $y$, i tada je rezultat $x \oplus y$. Oboje igraju optimalno kako bi maksimizirali rezultat. Za zadani $n$ izračunaj očekivani rezultat modulo $998\,244\,353$, tj.
$$\frac{1}{n^2} \sum_{i=0}^{n-1} \max\!\left(\sum_{j=0}^{n-1} i \oplus j,\ i \cdot n\right).$$</p>
<h3>Ulaz</h3>
<p>Prvi redak sadrži $T$ ($1 \le T \le 10^4$). Slijedi $T$ redaka s $n$ ($1 \le n \le 998\,244\,352$).</p>
<h3>Izlaz</h3>
<p>Za svaki primjer ispiši odgovor modulo $998\,244\,353$.</p>
''',
    'hints': [
        r'''
<p>$\max(\sum_j i \oplus j,\ i n) = i n + \max(f(i), 0)$ gdje je $f(i) = \sum_j (i \oplus j) - i n$. Rastavi po bitovima: $f(i) = \sum_b 2^b\, C_b \cdot (\pm 1)$ s predznakom $+$ ako je bit $b$ od $i$ nula, $-$ inače, uz $C_b = \#\{j \lt n : j_b = 1\}$ (računa se u $O(1)$).</p>
''',
        r'''
<p>Težine $|w_b| = C_b 2^b$ rastu približno geometrijski (faktor $\ge 2$) za bitove ispod vodećeg bita $n$, pa predznak od $f$ određuju viši bitovi: $f$ mijenja predznak na $\le \approx 20$ intervala. Nađi ih rekurzijom po bitovima s min/max od $f$ na blokovima $[p 2^k, (p+1)2^k)$.</p>
''',
    ],
    'coach': [
        ('Opažanje 1: formula za $f$',
         r'''
<p>$\sum_{j=0}^{n-1} (i \oplus j) = \sum_b 2^b \cdot \#\{j : (i\oplus j)_b = 1\} = \sum_b 2^b \bigl([i_b=0] C_b + [i_b=1](n - C_b)\bigr)$, a $i n = \sum_b 2^b [i_b = 1] n$. Razlika: $f(i) = \sum_b 2^b\, d_b\, C_b$ s $d_b = +1$ za $i_b = 0$, $-1$ za $i_b = 1$. $C_b(0, n-1)$ je $\Theta(1)$ formula (period $2^{b+1}$).</p>
'''),
        ('Opažanje 2: gotovo geometrijski rast',
         r'''
<p>Za $b$ ispod vodećeg bita $p$ od $n$, $C_b \approx n/2$, pa $|w_b| \approx 2^{b-1} n$: svaki viši bit nadjačava zbroj svih nižih. Predznak $f$ na bloku fiksnih viših bitova skoro je konstantan; ukupno $O(\log n)$ (praktično $\le 20$) maksimalnih intervala konstantnog predznaka.</p>
'''),
        ('Algoritam: podijeli pa vladaj po bitovima',
         r'''
<p>Rekurzija po bloku $[p 2^k, (p+1)2^k) \cap [0, n)$: min i max od $f$ na bloku su $\text{fiksni dio} \pm \sum_{b \lt k} |w_b|$. Ako je min $\ge 0$, dodaj $\sum f$ na bloku (zatvorena formula: svaki niži bit doprinosi po pola); ako je max $\le 0$, ništa; inače podijeli. Doprinos $\sum_i i n$ je $n \cdot \frac{n(n-1)}{2}$. Podijeli s $n^2$ modularnim inverzom.</p>
'''),
        ('Složenost',
         r'''
<p>$\Theta(k \log n)$ po upitu, $k$ = broj intervala; $T \le 10^4$.</p>
'''),
    ],
    'solution': r'''
<p>Neka je $C_i(l, r) = \sum_{t=l}^{r} [\,t \bmod 2^{i+1} \ge 2^i\,]$ broj cijelih brojeva u $[l, r]$ koji imaju jedinicu na $i$-tom bitu; računa se u $\Theta(1)$ jer je funkcija periodična s periodom $2^{i+1}$.</p>
<p>Neka je $f(i) = \left(\sum_{j=0}^{n-1} i \oplus j\right) - i \cdot n$. Formulu prepišemo kao
$$\sum_{i=0}^{n-1} i \cdot n + \sum_{i=0}^{n-1} \max(f(i), 0).$$
Vrijedi $f(i) = \sum_{j=0}^{29} d_j\, C_j(0, n-1) \cdot 2^j$, gdje je $d_j = 1$ ako je $j$-ti bit broja $i$ jednak $1$, a $d_j = -1$ inače.</p>
<p>Neka je $p$ najznačajniji bit broja $n$ i $w_j = d_j C_j(0, n-1) \cdot 2^j$. Za $k &lt; p$ vrijedi $\left|\frac{w_k}{w_{k-1}}\right| \gtrsim 2$, pa ako zanemarimo najznačajniji bit, čim su viši bitovi broja $i$ određeni, predznak funkcije $f$ je "gotovo" određen. Zato nema mnogo maksimalnih intervala na kojima $f$ ima isti predznak — zapravo ih je najviše oko $20$ za $n \le 10^9$. Te intervale možemo pronaći binarnim pretraživanjem ili metodom "podijeli pa vladaj" i za svaki izračunati doprinos.</p>
<p>Treba još znati, za interval $[l, r]$, ima li $f$ isti predznak na cijelom intervalu. Za to izračunamo najveću i najmanju vrijednost $f$ na intervalu — dinamičkim programiranjem po bitovima, ili tako da intervale uvijek biramo oblika $[p \cdot 2^k, (p+1) \cdot 2^k)$ i vrijednosti dobijemo iz predizračuna.</p>
<p>Složenost po upitu je $\Theta(k \log^2 n)$ ili $\Theta(k \log n)$, gdje je $k$ broj intervala.</p>
''',
},
{
    'letter': 'K',
    'title': 'Maximum GCD',
    'title_hr': 'Najveći GCD',
    'slug': 'K_maximum_gcd',
    'tl': '1 s',
    'ml': '1024 MB',
    'statement': r'''
<p>Zadan je niz $a$. Operacija: odaberi element $a_i$ i cijeli broj $x$ te zamijeni $a_i$ s $(a_i \bmod x)$; nakon operacije u nizu ne smije biti $0$. Maksimiziraj najveći zajednički djelitelj (GCD) niza nakon proizvoljnog broja operacija.</p>
<h3>Ulaz</h3>
<p>Prvi redak sadrži $n$ ($1 \le n \le 10^5$), drugi $a_1, \dots, a_n$ ($1 \le a_i \le 10^9$).</p>
<h3>Izlaz</h3>
<p>Ispiši najveći mogući GCD.</p>
''',
    'hints': [
        r'''
<p>Elementi se ne mogu povećati, pa je odgovor $\le a_{\min}$. Element $a_i$ može postati bilo koji broj iz $[1, \lfloor (a_i - 1)/2 \rfloor]$ ili ostati $a_i$.</p>
''',
        r'''
<p>Provjeri $x = a_{\min}$: svaki $a_i$ mora biti višekratnik od $x$ ili $a_i \ge 2x + 1$. Inače je odgovor $\lfloor a_{\min}/2 \rfloor$ — to uvijek radi.</p>
''',
    ],
    'coach': [
        ('Opažanje 1: doseg jedne operacije',
         r'''
<p>$a \bmod x \le \frac{a-1}{2}$ za $x \le a$ (ostatak je $\lt x$ i $\le a - x$); a s $x \gt a$ ostaje $a$. Svaki cilj $t \le \frac{a-1}{2}$ postiže se $x = a - t$ ($x \gt t$).</p>
'''),
        ('Opažanje 2: gornja granica i test',
         r'''
<p>GCD $\le$ najmanji element, a najmanji element ne može rasti: odgovor $\le a_{\min}$. $x = a_{\min}$ radi ako je svaki $a_i$ ili višekratnik od $x$ ili pretvoriv u $x$ ($x \le \lfloor (a_i-1)/2 \rfloor$).</p>
'''),
        ('Algoritam',
         r'''
<p>Ako test za $a_{\min}$ prolazi, odgovor $a_{\min}$. Inače $y = \lfloor a_{\min}/2 \rfloor$: svaki $a_i \ge a_{\min}$ pretvoriv je u $y$ ($y \le \lfloor (a_i - 1)/2 \rfloor$ jer $a_i \ge a_{\min}$), a $a_{\min}$ je ili paran (višekratnik od $y$) ili pretvoriv u $y = \lfloor (a_{\min}-1)/2 \rfloor$. Ništa između $y$ i $a_{\min}$ ne radi jer $a_{\min}$ mora postati $\le \lfloor(a_{\min}-1)/2\rfloor$ ili ostati. $O(n)$.</p>
'''),
    ],
    'solution': r'''
<p>Gornja granica odgovora je najmanji element niza $a_{\min}$ (elementi se ne mogu povećati). Treba provjeriti može li $a_{\min}$ biti odgovor.</p>
<p>Broj $a_i$ može se pretvoriti u bilo koji cijeli broj iz $[1, \lfloor \frac{a_i - 1}{2} \rfloor] \cup \{a_i\}$ (ostatak pri dijeljenju s $x$ je najviše $\lfloor (a_i-1)/2 \rfloor$ ako je $x \le a_i$, ili $a_i$ ako je $x &gt; a_i$). Ako je $a_i$ paran, on je višekratnik broja $a_i / 2$.</p>
<p>Ako je $x$ odgovor, svaki element niza mora zadovoljavati barem jedan od uvjeta:</p>
<ol>
    <li>$a_i$ se može pretvoriti u $x$, tj. $x \in [1, \lfloor \frac{a_i - 1}{2} \rfloor] \cup \{a_i\}$;</li>
    <li>$a_i$ je višekratnik od $x$.</li>
</ol>
<p>Ako $x = a_{\min}$ ne zadovoljava uvjete, odgovor je uvijek $\lfloor a_{\min} / 2 \rfloor$, jer za $x = \lfloor a_{\min} / 2 \rfloor$ svi elementi uvijek zadovoljavaju uvjete (svaki $a_i \ge a_{\min}$ može se pretvoriti u $x$, a sam $a_{\min}$ ili je višekratnik od $x$ — ako je paran — ili se pretvara u $x = \lfloor (a_{\min}-1)/2 \rfloor$ ako je neparan).</p>
''',
},
{
    'letter': 'L',
    'title': 'Permutation Compression',
    'title_hr': 'Sažimanje permutacije',
    'slug': 'L_permutation_compression',
    'tl': '1 s',
    'ml': '1024 MB',
    'statement': r'''
<p>Zadana je permutacija $a$ duljine $n$ i $k$ čarobnih alata; $i$-ti alat briše najveći element nekog intervala duljine <b>točno</b> $l_i$ (u trenutačnom nizu) i može se upotrijebiti najviše jednom. Zadan je i ciljni niz $b$ od $m$ različitih elemenata. Odredi može li se $a$ brisanjima pretvoriti u $b$.</p>
<h3>Ulaz</h3>
<p>Prvi redak sadrži $T$ ($1 \le T \le 10^5$). Za svaki primjer: $n, m, k$ ($1 \le m \le n \le 2 \times 10^5$, $1 \le k \le 2 \times 10^5$), zatim permutacija $a$, niz $b$ i duljine $l_1, \dots, l_k$ ($1 \le l_i \le n$). Zbroj svih $n$ i zbroj svih $k$ ne prelaze $2 \times 10^5$.</p>
<h3>Izlaz</h3>
<p>Za svaki primjer ispiši <code>YES</code> ili <code>NO</code>.</p>
''',
    'hints': [
        r'''
<p>Najprije: $b$ mora biti podniz od $a$. Zatim: brisanja se mogu preurediti tako da idu od najvećeg izbrisanog elementa prema najmanjem (veći element ostaje maksimum svog intervala neovisno o manjima).</p>
''',
        r'''
<p>Obradi vrijednosti od $n$ prema $1$: element koji ostaje (u $b$) postaje „zid” koji dijeli niz; izbrisani element $v$ u trenutačnom segmentu duljine $x$ (između zidova, uključujući manje neizbrisane) treba alat $l_j \le x$. Skupi sve $x$ i pohlepno spari s alatima (multiset).</p>
''',
    ],
    'coach': [
        ('Opažanje 1: poredak brisanja',
         r'''
<p>Ako se brišu $d_i \gt d_{i+1}$ uzastopno, zamjena redoslijeda je valjana: interval za $d_i$ i dalje ga ima za maksimum (brisanje $d_{i+1}$ prije samo smanjuje niz za manji element; duljinu intervala možemo prilagoditi jer $d_{i+1}$ nije u njemu ili je manji). Dakle briši silazno.</p>
'''),
        ('Opažanje 2: zidovi',
         r'''
<p>Kad je brisanje silazno, u trenutku brisanja $v$ svi veći elementi su ili već izbrisani ili ostaju zauvijek (u $b$). Interval za $v$ ne smije sadržavati veći element, pa je ograničen susjednim većim „zidovima”; maksimalna duljina intervala = broj trenutačno prisutnih elemenata između zidova.</p>
'''),
        ('Algoritam',
         r'''
<p>Prođi vrijednosti $n \to 1$; zidove drži u <code>std::set</code> pozicija, broj živih elemenata na intervalu Fenwickovim stablom (brisanje $= -1$). Za izbrisani $v$ zapiši $x_v$. Zatim sparivanje: sortiraj $x$ uzlazno i svakom dodijeli najmanji preostali $l_j \le x$ (multiset, <code>upper_bound</code> pa prethodnik); ako ne postoji, <code>NO</code>.</p>
'''),
        ('Složenost',
         r'''
<p>$\Theta((n + k)\log n)$ po testu.</p>
'''),
    ],
    'solution': r'''
<p>(Najprije provjerimo da je $b$ podniz od $a$ u istom redoslijedu; inače je odgovor <code>NO</code>.)</p>
<p>Uočimo da elemente možemo brisati jedan po jedan od najvećeg prema najmanjem. Naime, ako je $d_i$ $i$-ti izbrisani element i $d_i &gt; d_{i+1}$, možemo zamijeniti redoslijed brisanja $d_i$ i $d_{i+1}$ i niz brisanja ostaje valjan (veći element ostaje najveći na svom intervalu neovisno o tome je li manji već izbrisan).</p>
<p>Sada elemente promatramo od najvećeg prema najmanjem. Ako element $i$ <b>nije</b> izbrisan (nalazi se u $b$), nijedan kasniji interval brisanja ne može prelaziti preko njega, pa on dijeli niz na dva neovisna dijela. Ako $i$ <b>jest</b> izbrisan i dio u kojem se nalazi trenutačno ima $x$ preostalih elemenata (računajući i one manje od $i$ koji još nisu izbrisani), moramo upotrijebiti neki alat s $l_j \le x$.</p>
<p>Granice dijelova održavamo u <code>std::set</code>, a broj preostalih elemenata između dviju granica Fenwickovim stablom (svako brisanje smanjuje broj za $1$). Tako dobijemo sve vrijednosti $x$ i trebamo provjeriti mogu li se spariti sa zadanim duljinama $l_j$ (svaki $x$ dobiva različit alat s $l_j \le x$), što se rješava pohlepno: sortiramo i najmanjem $x$ dodjeljujemo najmanji dostupni $l_j$, ili pak koristimo multiset.</p>
<p>Vremenska složenost je $\Theta(n \log n)$.</p>
''',
},
]
