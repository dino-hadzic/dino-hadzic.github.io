# -*- coding: utf-8 -*-
STAGE = {
    'no': 16,
    'name': 'Stage 16: Gomel',
    'source_name': '44th Petrozavodsk Programming Camp, Winter 2023, Day 7: Gennady Korotkevich Contest 7',
    'source_html': r'''
<p>Autor zadataka i rješenja: Gennady Korotkevich (tourist). Prijevod službenog rješenja: <a href="https://contest.ucup.ac/download.php?type=attachments&amp;id=1223&amp;r=2">Tutorial (en)</a>. Tekst zadatka preveden je prema službenim <a href="https://contest.ucup.ac/download.php?type=attachments&amp;id=1223&amp;r=1">engleskim tekstovima zadataka</a>. Zadatak je dostupan na <a href="https://contest.ucup.ac/contest/1223">Universal Cup Judging System</a>.</p>
''',
}

PROBLEMS = [
# ---------------------------------------------------------------- A
{
    'letter': 'A', 'title': 'Classical A+B Problem', 'title_hr': 'Klasični zadatak A+B', 'slug': 'A_classical_a_plus_b_problem',
    'tl': '4 s', 'ml': '512 MiB',
    'statement': r'''
<p><em>Repdigit</em> je pozitivan cijeli broj čiji se dekadski zapis sastoji od ponavljanja iste znamenke ($1$, $666$, $4444$). Dan je $n$ za koji se jamči da je $n = a + b$ za neka dva repdigita $a, b$. Ispiši bilo koji takav par.</p>
<h3>Ulaz</h3>
<p>$t \le 10^4$ testova; $2 \le n < 10^{4000}$, ukupno najviše $10^5$ znamenki.</p>
<h3>Izlaz</h3>
<p>$a$ i $b$.</p>
<h3>Primjer</h3>
<p>$786 = 777 + 9$; $89110 = 88888 + 222$; $10^{28} + 1 = 99\ldots9 + 2$.</p>
''',
    'hints': [
        r'''<p>Neka je $a \ge b$. Koliko znamenki može imati $a$ u odnosu na $n$? Zbroj dvaju brojeva od kojih je veći $a$ ima $|a|$ ili $|a| + 1$ znamenki.</p>''',
        r'''<p>Dakle $|a| \in \{|n| - 1, |n|\}$ i znamenka od $a$ je jedna od $9$: ukupno $18$ kandidata. Za svaki izračunaj $b = n - a$ (oduzimanje velikih brojeva u $O(|n|)$) i provjeri je li repdigit.</p>''',
    ],
    'coach': [
        ('Opažanje', r'''<p>Neka $|x|$ označava broj znamenki. Uz $a \ge b$ vrijedi $a \le n < 2a$, pa je $|n| - 1 \le |a| \le |n|$.</p>'''),
        ('Redukcija', r'''<p>Samo $2$ mogućnosti za duljinu i $9$ za znamenku od $a$ — $18$ kandidata. Za svakog izračunaj $b = n - a$ i provjeri je li pozitivan repdigit.</p>'''),
        ('Algoritam i složenost', r'''<p>Oduzimanje kao nizovi znamenki, $O(|n|)$ po kandidatu; ukupno $O(18 \cdot \sum |n|)$. Pazi na vodeće nule kod $b$ i na $b > 0$.</p>'''),
    ],
    'solution': r'''
<p>Neka $|x|$ označava broj znamenki cijelog broja $x$. U $n = a + b$ bez smanjenja općenitosti neka je $a \ge b$. Lako se vidi da je $|n| - 1 \le |a| \le |n|$.</p>
<p>Dakle postoje samo $2$ mogućnosti za duljinu od $a$ i $9$ mogućnosti za znamenku od koje se $a$ sastoji — ukupno $18$ mogućnosti za $a$. Isprobamo svaku, izračunamo $b = n - a$ i provjerimo je li $b$ repdigit.</p>
''',
},
# ---------------------------------------------------------------- B
{
    'letter': 'B', 'title': 'Classical Counting Problem', 'title_hr': 'Klasični zadatak prebrojavanja', 'slug': 'B_classical_counting_problem',
    'tl': '2 s', 'ml': '512 MiB',
    'statement': r'''
<p>Predloženo je $n$ zadataka s početnim bodovima $a_i$. Svaki od $m$ sudaca bira točno $v$ zadataka i svakom povećava bodove za $1$. Zatim se zadaci sortiraju po bodovima nerastuće (izjednačeni proizvoljno, odlučuje direktor) i prvih $p$ ($1 \le p \le n$, proizvoljno) ulazi u skup zadataka. Koliko je različitih skupova zadataka moguće? Modulo $998244353$.</p>
<h3>Ulaz</h3>
<p>$t \le 50$ testova; $n, m, v$ ($2 \le n \le 100$, $1 \le m \le 100$, $1 \le v \le n - 1$), $a_i \le 100$. $\sum n \le 100$.</p>
<h3>Izlaz</h3>
<p>Broj mogućih skupova.</p>
<h3>Primjer</h3>
<p>$n = 3, m = 1, v = 2$, $a = (1, 2, 3)$: mogući skupovi $\{2\}, \{3\}, \{1,3\}, \{2,3\}, \{1,2,3\}$ — odgovor $5$.</p>
''',
    'hints': [
        r'''<p>Sortiraj $a_1 \ge \dots \ge a_n$. Za fiksni podskup $S$: neka je $x$ najmanji indeks izvan $S$, $y$ najveći indeks u $S$. $S$ je moguć ako i samo ako postoje konačni bodovi $b_i$ (s $a_i \le b_i \le a_i + m$, $\sum (b_i - a_i) = mv$) takvi da je $\min_{i \in S} b_i \ge \max_{i \notin S} b_i$ — glasovi se uvijek mogu realizirati (cikličko dodjeljivanje).</p>''',
        r'''<p>Za svaki $i$ odredi najmanji ($l_i$) i najveći ($r_i$) broj glasova koji mu treba/smije da bi $S$ bio moguć; kriterij je $\sum l_i \le mv \le \sum r_i$. $l_i$ ovise samo o $x$, $r_i$ samo o $y$ — dva ruksak-DP-a, komplementarno prebrojavanje.</p>''',
    ],
    'coach': [
        ('Opažanje: kriterij za podskup', r'''<p>Sortiraj $a_1 \ge a_2 \ge \dots \ge a_n$. Za podskup $S$ neka je $x$ najmanji indeks koji nije u $S$, a $y$ najveći indeks koji jest. Ako je $a_y + m < a_x$, $S$ nije moguć. Inače definiraj $l_i$ = najmanji broj glasova koji zadatak $i$ mora dobiti: $l_y = a_x - a_y$, za $i \in S \cap (x, y)$: $l_i = a_x - a_i$, ostalo $0$. I $r_i$ = najveći broj glasova koji smije dobiti: $r_x = a_y + m - a_x$, za $i \notin S$, $i \in (x, y)$: $r_i = a_y + m - a_i$, ostalo $m$. Vrijedi $l_i \le r_i$.</p>'''),
        ('Tvrdnja', r'''<p>$S$ je moguć ako i samo ako $\sum l_i \le mv \le \sum r_i$. Dokaz: odaberi $b_i \in [l_i, r_i]$ sa $\sum b_i = mv$ (kreni od $l_i$, povećavaj najprije zadatke u $S$); zatim zapiši niz od $b_1$ jedinica, $b_2$ dvojki, … (duljina $mv$) i sudac $j$ glasa za pozicije $j, m + j, 2m + j, \dots$ — svaki glasa za $v$ različitih zadataka, a zadatak $i$ dobije točno $b_i$ glasova.</p>'''),
        ('Algoritam', r'''<p>Broj mogućih $S$ = (broj $S$ sa $\sum r_i \ge mv$) $-$ (broj $S$ sa $\sum l_i > mv$). Naivno fiksiraj $x, y$ i radi ruksak po $i \in (x, y)$: $O(n^4 a_n)$, presporo. Ali $l_i$ ovise samo o $x$: fiksiraj $x$ (zadaci $1..x-1$ u $S$, $x$ nije) i radi DP unaprijed po $i = x+1..n$ nad zbrojem $\sum l$; $y$ je implicitno zadnji uzeti. Slično $r_i$ ovise samo o $y$: fiksiraj $y$ i radi DP unatrag po $i = y-1..1$. Pazi na doprinos $l_y$ odn. $r_x$ (ovisi o drugom kraju — uključi ga kad DP „zatvara” $y$ odn. $x$).</p>'''),
        ('Složenost', r'''<p>$O(n^3 a_n)$ po testu, uz $\sum n \le 100$.</p>'''),
    ],
    'solution': r'''
<p>Bez smanjenja općenitosti neka je $a_1 \ge a_2 \ge \dots \ge a_n$. Fiksirajmo podskup zadataka $S$ i osmislimo kriterij može li se $S$ odabrati kao skup zadataka.</p>
<p>Neka je $x$ zadatak s najmanjim indeksom koji ne pripada $S$, a $y$ zadatak s najvećim indeksom koji pripada $S$. Zadaci $1, \dots, x-1$ sigurno su u $S$, zadaci $y+1, \dots, n$ sigurno nisu, a zadaci $x+1, \dots, y-1$ mogu i ne moraju biti.</p>
<p>Ako je $a_y + m < a_x$, $S$ nije valjan. Inače, neka je $l_i$ najmanji broj glasova koji zadatak $i$ mora dobiti da bi $S$ mogao biti odabran: za $i \in \{1, \dots, x-1, x, y+1, \dots, n\}$ je $l_i = 0$; $l_y = a_x - a_y$; za ostale $i \in \{x+1, \dots, y-1\}$: ako je $i \in S$, $l_i = a_x - a_i$, inače $l_i = 0$. Slično, $r_i$ je najveći broj glasova koji zadatak $i$ smije dobiti: za $i \in \{1, \dots, x-1, y, y+1, \dots, n\}$ je $r_i = m$ (nijedan zadatak ne može dobiti više od $m$ glasova); $r_x = (a_y + m) - a_x$; za ostale $i \in \{x+1, \dots, y-1\}$: ako je $i \in S$, $r_i = m$, inače $r_i = (a_y + m) - a_i$. Vrijedi $l_i \le r_i$ za sve $i$.</p>
<p><b>Tvrdnja.</b> Ako je $\sum_{i=1}^n l_i \le m \cdot v \le \sum_{i=1}^n r_i$, tada se $S$ može odabrati kao skup zadataka.</p>
<p><i>Dokaz.</i> Najprije nađi brojeve glasova $b_1, \dots, b_n$ takve da $l_i \le b_i \le r_i$, $\sum b_i = mv$ i da se $S$ može odabrati: npr. kreni s $b_i = l_i$ i povećavaj glasove zadacima u $S$ (do $r_i$), a zatim zadacima izvan $S$, dok zbroj ne postane $mv$. Zatim zapiši niz: $b_1$ kopija broja $1$, $b_2$ kopija broja $2$, …, $b_n$ kopija broja $n$; duljina mu je $mv$. Sudac $1$ glasa za zadatke na pozicijama $1, m+1, 2m+1, \dots, (v-1)m+1$; sudac $2$ za pozicije $2, m+2, \dots$; itd. Svaki sudac glasa za točno $v$ različitih zadataka, a svaki zadatak $i$ dobiva točno $b_i$ glasova. $\square$</p>
<p>Sada, da bismo prebrojali moguće skupove $S$, prebrojimo skupove koji zadovoljavaju $\sum r_i \ge mv$ i oduzmemo broj skupova koji zadovoljavaju $\sum l_i > mv$.</p>
<p>Jedan način: iteriraj po $x$ i $y$ i pokreni ruksak-DP za zadatke $x+1, \dots, y-1$, npr. $f(i, s)$ — broj načina da se odabere podskup zadataka $x+1, \dots, i$ tako da je zbroj $l_j$ (odn. $r_j$) u tom rasponu jednak $s$. DP ima $O(n^2 a_n)$ stanja i $O(1)$ prijelaza, a pokreće se $O(n^2)$ puta: $O(n^4 a_n)$, moguće presporo.</p>
<p>Optimizacija: vrijednosti $l_i$ ovise samo o $x$. Zato je za prebrojavanje skupova sa $\sum l_i > mv$ dovoljno fiksirati $x$, bez fiksiranja $y$ — DP jednostavno teče unaprijed za $i = x+1, \dots, n$. Slično, $r_i$ ovise samo o $y$, pa je za $\sum r_i \ge mv$ dovoljno fiksirati $y$ i pokrenuti DP unatrag za $i = y-1, \dots, 1$.</p>
<p>Time se vremenska složenost poboljšava na $O(n^3 a_n)$.</p>
''',
},
# ---------------------------------------------------------------- C
{
    'letter': 'C', 'title': 'Classical Data Structure Problem', 'title_hr': 'Klasični zadatak sa strukturom podataka', 'slug': 'C_classical_data_structure_problem',
    'tl': '3 s', 'ml': '128 MiB',
    'statement': r'''
<p>Niz $A$ duljine $2^m$ nula i varijabla $x = 0$. Za $i = 1..n$: $p' = (p_i + x) \bmod 2^m$, $q' = (q_i + x) \bmod 2^m$, $l = \min, r = \max$; za svaki $j \in [l, r]$: $a_j \mathrel{+}= i$, zatim $x \mathrel{+}= a_j$. Ispiši $x \bmod 2^{30}$.</p>
<h3>Ulaz</h3>
<p>$n \le 500\,000$, $m \le 30$, parovi $p_i, q_i < 2^m$.</p>
<h3>Izlaz</h3>
<p>$x \bmod 2^{30}$.</p>
''',
    'hints': [
        r'''<p>Dodavanje na intervalu i zbroj na intervalu: lijeno segmentno stablo. No $2^{30}$ indeksa i memorija $128$ MiB — dinamičko stablo stvara $O(m)$ čvorova po upitu, tj. $O(nm)$ ukupno, previše.</p>''',
        r'''<p>Umjesto cijepanja u sredini, cijepaj čvor točno na granici upita: $[x, y) \to [x, l), [l, y)$ — najviše $4$ nova čvora po upitu, $O(n)$ memorije. Ali visina može postati $\Omega(n)$; rotacije (kao AVL/splay) vraćaju $O(\log n)$.</p>''',
    ],
    'coach': [
        ('Opažanje', r'''<p>Operacija je: dodaj $i$ na $[l, r]$, pa $x \mathrel{+}= \sum_{j=l}^r a_j$ (nakon dodavanja). Sve modulo $2^{30}$ (prirodni overflow 32-bitnog tipa uz masku). Standardno lijeno segmentno stablo, ali domena je $2^m \le 2^{30}$.</p>'''),
        ('Redukcija: memorija', r'''<p>Dinamičko segmentno stablo koje cijepa $[x, y)$ na polovice stvara $O(m)$ čvorova po upitu — $O(nm) \approx 1.5 \cdot 10^7$ čvorova, previše za $128$ MiB. Cijepaj umjesto toga na $[x, l)$ i $[l, y)$ (i slično za $r + 1$): najviše $4$ nova čvora po upitu, $O(n)$ prostora.</p>'''),
        ('Algoritam: balansiranje', r'''<p>Takvo stablo može degenerirati (ugniježđeni upiti daju visinu $\Omega(n)$). Čvorovi predstavljaju intervale koji se spajaju, pa rotacije čuvaju semantiku (kao u balansiranim BST-ovima) — održavaj lijene oznake i zbrojeve pri rotaciji. Uz AVL ili splay tehniku: $O(n \log n)$ vremena, $O(n)$ prostora.</p>'''),
    ],
    'solution': r'''
<p>Zadatak izgleda kao standardni zadatak s dinamičkim segmentnim stablom. Početno stvorimo jedan čvor za segment $[0, 2^m)$. Kad dođe upit $[l, r]$, spuštamo se od vrha i dođemo do čvora bez djece koji odgovara segmentu $[x, y)$ s $x < l < y$; tada stvorimo dva nova čvora za $[x, \frac{x+y}{2})$ i $[\frac{x+y}{2}, y)$ i nastavimo. Slično za segment koji sadrži $r$.</p>
<p>Tako nastaje $O(m)$ novih čvorova po upitu, tj. $O(nm)$ memorije, što je možda previše jer je memorijsko ograničenje strogo.</p>
<p>Umjesto cijepanja $[x, y)$ na polovice, možemo cijepati na $[x, l)$ i $[l, y)$. Tada cijepamo samo jednom za $l$ i jednom za $r$, pa je ukupno potrebno $O(n)$ prostora (najviše $4$ nova čvora po upitu). Međutim, sada vrijeme može biti problem: visina stabla može narasti na $\Omega(n)$, npr. ako su svi upiti ugniježđeni.</p>
<p>Rješenje: rotacijama rebalansiramo segmentno stablo, slično kao u mnogim balansiranim binarnim stablima pretraživanja. Tehnikama AVL-stabla ili splay-stabla dobivamo $O(n \log n)$ vremena i $O(n)$ prostora.</p>
''',
},
# ---------------------------------------------------------------- D
{
    'letter': 'D', 'title': 'Classical DP Problem', 'title_hr': 'Klasični DP zadatak', 'slug': 'D_classical_dp_problem',
    'tl': '2 s', 'ml': '512 MiB',
    'statement': r'''
<p>Youngov dijagram: u $i$-tom retku ostalo je prvih $a_i$ polja, $a_1 \le \dots \le a_n \le n$. Polje je <em>pokriveno</em> ako sadrži topa ili top može doći na njega u jednom potezu (kroz prazna polja). Nađi najmanji broj topova $r$ koji pokrivaju sva polja i broj načina $w$ za postavljanje $r$ topova (mod $998244353$).</p>
<h3>Ulaz</h3>
<p>$n \le 5000$ i $a_i$.</p>
<h3>Izlaz</h3>
<p>$r$ i $w$.</p>
<h3>Primjer</h3>
<p>$a = (1, 2, 3)$: $r = 2$, $w = 6$.</p>
''',
    'hints': [
        r'''<p>Obrni redoslijed tako da je $a_1 \ge \dots \ge a_n$. Najveći kvadrat $k \times k$ u dijagramu ($a_k \ge k$, $a_{k+1} < k+1$) treba barem $k$ topova — a $k$ topova na dijagonali pokriva sve (svako polje je u prvih $k$ redaka ili prvih $k$ stupaca). Dakle $r = k$.</p>''',
        r'''<p>S $k$ topova mora vrijediti: svaki od prvih $k$ redaka ima topa ILI svaki od prvih $k$ stupaca ima topa (inače polje u praznom retku i praznom stupcu kvadrata nije pokriveno). Uključivanje–isključivanje: $|R| + |C| - k!$; $|R|$ DP-om po recima uz brojanje koliko od $t = a_{k+1}$ obveznih stupaca ima topa.</p>''',
    ],
    'coach': [
        ('Opažanje: koliko topova', r'''<p>Uz $a_1 \ge \dots \ge a_n$ neka je $k$ jedini cijeli broj s $a_k \ge k$ i $a_{k+1} < k + 1$ — stranica najvećeg kvadrata koji se uklapa. Za pokrivanje kvadrata $k \times k$ treba barem $k$ topova; a svako drugo polje leži u prvih $k$ redaka ili prvih $k$ stupaca, pa $k$ topova na glavnoj dijagonali kvadrata pokriva sve. $r = k$.</p>'''),
        ('Redukcija: struktura pokrivanja', r'''<p>Postavljanje $k$ topova valja samo ako (1) svaki od prvih $k$ redaka sadrži topa, ili (2) svaki od prvih $k$ stupaca sadrži topa; inače je polje u retku bez topa i stupcu bez topa unutar kvadrata nepokriveno. Odgovor je $|\text{(1)}| + |\text{(2)}| - |\text{(1)} \cap \text{(2)}|$, a zadnji je $k!$ (permutacije unutar kvadrata). (2) se dobiva kao (1) na transponiranom dijagramu.</p>'''),
        ('Algoritam: DP za uvjet (1)', r'''<p>Neka $t = a_{k+1}$ — toliko stupaca (izvan prvih $k$ redaka ima polja samo u prvih $t$ stupaca) mora imati topa. $f(i, j)$ = broj načina postavljanja topova u prvih $i$ redaka (jedan po retku) tako da točno $j$ od prvih $t$ stupaca sadrži topa. $f(0, 0) = 1$; iz $(i, j)$ top u retku $i+1$ ide u jedan od $t - j$ nepokrivenih obveznih stupaca ($\to (i+1, j+1)$) ili u jedan od $a_{i+1} - (t - j)$ ostalih ($\to (i+1, j)$). Traženo $f(k, t)$.</p>'''),
        ('Složenost', r'''<p>$O(n^2)$ vremena, $O(n)$ memorije s klizanjem po $i$.</p>'''),
    ],
    'solution': r'''
<p>Radi praktičnosti obrnimo $a$ tako da je $a_1 \ge a_2 \ge \dots \ge a_n$.</p>
<p>Nađi stranicu $k$ najvećeg kvadrata koji se uklapa u dijagram: $k$ je jedini cijeli broj s $a_k \ge k$ i $a_{k+1} < k + 1$. Tada je najmanji broj topova jednak $k$: za pokrivanje kvadrata $k \times k$ potrebno je barem $k$ topova, a sva ostala polja pripadaju ili jednom od prvih $k$ redaka ili jednom od prvih $k$ stupaca, pa $k$ topova na glavnoj dijagonali kvadrata pokriva sve.</p>
<p>Prebrojimo valjana postavljanja $k$ topova. Barem jedan od uvjeta mora vrijediti: (1) svaki od prvih $k$ redaka sadrži topa; (2) svaki od prvih $k$ stupaca sadrži topa. Ako ne vrijedi nijedan, barem jedno polje u kvadratu nije pokriveno (polje u retku bez topa i stupcu bez topa). Odgovor je broj postavljanja koja zadovoljavaju (1) plus broj koja zadovoljavaju (2) minus broj koja zadovoljavaju oba — a zadnji je $k!$.</p>
<p>Prebrojimo postavljanja s uvjetom (1); (2) se dobiva analogno nakon transponiranja. Neka je $t = a_{k+1}$ — broj stupaca koji moraju sadržavati barem jednog topa da bi cijeli dijagram bio pokriven. Neka je $f(i, j)$ broj načina postavljanja topova u prvih $i$ redaka tako da točno $j$ od prvih $t$ stupaca sadrži barem jednog topa; $f(0, 0) = 1$, a tražimo $f(k, t)$. Prijelazi iz $(i, j)$: top u retku $i+1$ ide u jedan od $t - j$ stupaca koji trebaju topa a nemaju ga — stanje $(i+1, j+1)$, $t - j$ načina; inače broj pokrivenih obveznih stupaca ostaje isti — stanje $(i+1, j)$, $a_{i+1} - (t - j)$ načina.</p>
<p>Vremenska složenost: $O(n^2)$.</p>
''',
},
# ---------------------------------------------------------------- E
{
    'letter': 'E', 'title': 'Classical FFT Problem', 'title_hr': 'Klasični FFT zadatak', 'slug': 'E_classical_fft_problem',
    'tl': '10 s', 'ml': '512 MiB',
    'statement': r'''
<p>Isti zadatak kao D (najmanji broj topova koji pokrivaju Youngov dijagram i broj načina mod $998244353$), ali $n < 2^{17}$.</p>
<h3>Ulaz</h3>
<p>$n < 2^{17}$ i $a_1 \le \dots \le a_n \le n$.</p>
<h3>Izlaz</h3>
<p>$r$ i $w$.</p>
''',
    'hints': [
        r'''<p>Iz D: treba prebrojati načine da se u $k$ redaka duljina $a_1 \ge \dots \ge a_k$ postavi po jedan top tako da svaki od prvih $t$ stupaca ($t \le a_k$) ima topa. Uključivanje–isključivanje po skupu nepokrivenih obveznih stupaca: stupci su nerazlučivi, pa iteriraj samo po broju $p$.</p>''',
        r'''<p>Broj načina da zadanih $p$ stupaca ostane prazno je $\prod_i (a_i - p) = f(p)$ za polinom $f(x) = \prod (a_i - x)$. Odgovor $\sum_{p=0}^t (-1)^p \binom{t}{p} f(p)$: koeficijente od $f$ nađi D&amp;C + NTT-om, vrijednosti $f(0..t)$ višetočkovnom evaluacijom.</p>''',
    ],
    'coach': [
        ('Opažanje', r'''<p>Struktura odgovora iz zadatka D ostaje: $r = k$, $w = |\text{(1)}| + |\text{(2)}| - k!$, gdje se (1) svodi na: $k$ redaka s $a_1 \ge \dots \ge a_k$ polja, po jedan top u svakom retku, svaki od prvih $t$ stupaca pokriven. DP $O(n^2)$ više ne prolazi za $n \approx 1.3 \cdot 10^5$.</p>'''),
        ('Redukcija: uključivanje–isključivanje', r'''<p>Broj postavljanja = (sva) $-$ (stupac $i$ prazan, $\forall i$) $+$ (stupci $i, j$ prazni) $- \dots$. Ako je zadanih $p$ obveznih stupaca prazno, redak $i$ ima $a_i - p$ mogućnosti (svi ti stupci su unutar svakog retka jer $p \le t \le a_k$): $\prod_{i=1}^k (a_i - p)$. Stupci su nerazlučivi, pa je odgovor $\sum_{p=0}^{t} (-1)^p \binom{t}{p} \prod_i (a_i - p)$.</p>'''),
        ('Algoritam', r'''<p>Neka je $f(x) = \prod_{i=1}^k (a_i - x)$. Koeficijente izračunaj množenjem linearnih faktora metodom podijeli-pa-vladaj s NTT-om (mod $998244353$) u $O(k \log^2 k)$; vrijednosti $f(0), \dots, f(t)$ višetočkovnom evaluacijom u $O(k \log^2 k)$. Zbroji s binomnim koeficijentima i predznacima. Isto ponovi za transponirani dijagram.</p>'''),
        ('Složenost', r'''<p>$O(n \log^2 n)$.</p>'''),
    ],
    'solution': r'''
<p>Nadogradnja rješenja prethodnog zadatka: imamo $k$ redaka s $a_1 \ge a_2 \ge \dots \ge a_k$ polja i tražimo broj načina da se u svaki redak stavi top tako da svaki od prvih $t$ stupaca ($t \le a_k$) sadrži barem jednog topa.</p>
<p>Primijenimo uključivanje–isključivanje po skupu stupaca među prvih $t$ koji sadrže topa. Odgovor je broj načina da se topovi postave proizvoljno, minus broj načina da stupac $i$ nije pokriven (za svaki $i$), plus broj načina da stupci $i$ i $j$ nisu pokriveni (za sve $i < j$), itd.</p>
<p>Budući da su stupci nerazlučivi, iteriramo samo po broju nepokrivenih stupaca $p$. Broj načina da zadanih $p$ stupaca ne sadrži topove je $(a_1 - p)(a_2 - p)\cdots(a_k - p)$, a broj načina odabira $p$ stupaca od prvih $t$ je $\binom{t}{p}$. Ukupno:</p>
$$\sum_{p=0}^{t} (-1)^p \binom{t}{p} (a_1 - p)(a_2 - p)\cdots(a_k - p).$$
<p>Neka je $f(x) = (a_1 - x)(a_2 - x)\cdots(a_k - x)$ polinom. Njegove koeficijente nalazimo u $O(k \log^2 k)$ metodom podijeli-pa-vladaj i FFT-om, a vrijednosti $f(0), f(1), \dots, f(t)$ u $O(k \log^2 k)$ višetočkovnom evaluacijom. Odgovor je tada $\sum_{p=0}^t (-1)^p \binom{t}{p} f(p)$.</p>
''',
},
# ---------------------------------------------------------------- F
{
    'letter': 'F', 'title': 'Classical Geometry Problem', 'title_hr': 'Klasični geometrijski zadatak', 'slug': 'F_classical_geometry_problem',
    'tl': '2 s', 'ml': '512 MiB',
    'statement': r'''
<p>Boje su točke $(r, g, b) \in [0, 255]^3$. Lampa ima $8$ tipki — vrhovi kocke (sve kombinacije $0/255$). Držanje tipke boje $c$ tijekom $d$ sekundi pomiče trenutnu boju $p$ linearno prema $c$ brzinom $1$, najviše do $c$. Iz crne $(0,0,0)$ dosegni zadanu cjelobrojnu boju s najviše $10$ pritisaka (tolerancija $10^{-6}$).</p>
<h3>Ulaz</h3>
<p>$t \le 10^4$ testova; $r, g, b \in [0, 255]$.</p>
<h3>Izlaz</h3>
<p>$m \le 10$ i redaka <code>rc gc bc d</code>.</p>
''',
    'hints': [
        r'''<p>Definiraj rang točke kao broj koordinata koje nisu $0$ ni $255$. Rang $0$: vrh kocke — jedan pritisak. Rang $1$: na bridu između vrhova $a, b$ — idi u $a$, pa prema $b$ i stani na vrijeme.</p>''',
        r'''<p>Rang $2$ (na plohi) i $3$ (unutrašnjost): odaberi vrh $v$ te plohe/kocke, povuci polupravac iz $v$ kroz $p$ do ruba (brida odn. plohe); ta točka ima manji rang — dođi do nje rekurzivno, pa se kreni prema $v$ i stani u $p$. Najviše $4$ pritiska.</p>''',
    ],
    'coach': [
        ('Opažanje', r'''<p>Kretanje prema tipki $c$ je pravocrtno prema vrhu kocke. Točku na dužini između trenutne pozicije i nekog vrha dosežemo jednim pritiskom (s odgovarajućim $d$). Definiraj rang $f(p)$ = broj koordinata $p$ koje nisu ni $0$ ni $255$.</p>'''),
        ('Redukcija po rangu', r'''<p>$f = 0$: $p$ je vrh — jedan pritisak (iz crne). $f = 1$: $p$ je na bridu između vrhova $a$ i $b$ — idi u $a$ (držanjem $a$ dovoljno dugo), zatim prema $b$ i zaustavi se na udaljenosti $|p - a|$. $f = 2$: $p$ je na plohi; uzmi vrh $v$ plohe, polupravac iz $v$ kroz $p$ siječe brid plohe u točki $q$ ranga $\le 1$; dođi do $q$, pa drži $v$ točno $|q - p|$ sekundi. $f = 3$: $p$ u unutrašnjosti; vrh $v$ kocke, polupravac $v \to p$ siječe plohu u $q$ ranga $\le 2$; rekurzivno do $q$, pa prema $v$.</p>'''),
        ('Algoritam i složenost', r'''<p>Rekurzija dubine $\le 3$ s po jednim dodatnim pritiskom po razini: najviše $1 + 1 + 1 + 1 = 4$ pritiska. Presjek polupravca s rubom: skaliraj vektor $p - v$ faktorom $\lambda \ge 1$ najmanjim takvim da neka koordinata dosegne $0$ ili $255$. Ispis s dovoljno decimala; $O(1)$ po testu.</p>'''),
    ],
    'solution': r'''
<p>Definirajmo rang $f(p)$ točke $p = (r, g, b)$ kao broj njezinih koordinata različitih i od $0$ i od $255$.</p>
<p>Ako je $f(p) = 0$, $p$ je jedna od osnovnih boja i do nje idemo jednim potezom.</p>
<p>Ako je $f(p) = 1$, $p$ leži na bridu između dviju osnovnih boja $a$ i $b$: idi u $a$, zatim se kreni prema $b$ i stani u pravom trenutku.</p>
<p>Ako je $f(p) = 2$, $p$ leži unutar plohe kocke. Odaberi bilo koji vrh $v$ te plohe, povuci polupravac iz $v$ kroz $p$ i nađi gdje siječe brid kocke. Točka presjeka ima rang $0$ ili $1$, pa najprije dođi do nje kako je opisano, a zatim se iz nje kreni prema $v$ i stani u $p$.</p>
<p>Ako je $f(p) = 3$, $p$ je strogo unutar kocke. Odaberi bilo koji vrh $v$ kocke, povuci polupravac iz $v$ kroz $p$ i nađi gdje siječe plohu kocke. Točka presjeka ima rang $0$, $1$ ili $2$, pa najprije dođi do nje kako je opisano, a zatim se iz nje kreni prema $v$ i stani u $p$.</p>
''',
},
# ---------------------------------------------------------------- G
{
    'letter': 'G', 'title': 'Classical Graph Theory Problem', 'title_hr': 'Klasični zadatak iz teorije grafova', 'slug': 'G_classical_graph_theory_problem',
    'tl': '4 s', 'ml': '512 MiB',
    'statement': r'''
<p>Povezan neusmjeren graf $G$ u kojem svaki vrh ima najviše dva susjedna lista. Nađi $S \subset V$ takav da su i $S$ i $V \setminus S$ dominirajući skupovi te $|S| = \lfloor |V| / 2 \rfloor$. Jamči se postojanje.</p>
<h3>Ulaz</h3>
<p>$t \le 10^4$ testova; $n \le 2 \cdot 10^5$, $m \le 5 \cdot 10^5$ (sume ograničene), bridovi.</p>
<h3>Izlaz</h3>
<p>Vrhovi skupa $S$.</p>
<h3>Primjer</h3>
<p>Put $1 - 2 - 3$: $S = \{2\}$.</p>
''',
    'hints': [
        r'''<p>Uvjet „$S$ i $V \setminus S$ oba dominiraju” znači: svaki vrh ima susjeda na suprotnoj strani od sebe. Za list $v$ s jedinim susjedom $u$ to znači da su $v$ i $u$ na različitim stranama — listovi su prisilni.</p>''',
        r'''<p>Ovo je poznati problem „even adjacency split”: podjela vrhova na dvije (gotovo) jednake strane tako da svaki vrh ima susjeda na drugoj strani. Službeno rješenje upućuje na konstrukciju iz literature (vidi rješenje).</p>''',
    ],
    'coach': [
        ('Opažanje', r'''<p>Preformulacija: obojimo vrhove u dvije boje tako da svaki vrh ima susjeda suprotne boje, a boje su uravnotežene ($\lfloor n/2 \rfloor$ u $S$). List mora biti suprotne boje od svog jedinog susjeda; vrh s dva lista stoga ima oba lista iste boje, suprotne svojoj.</p>'''),
        ('Redukcija', r'''<p>Uvjet „svaki vrh ima susjeda suprotne boje” lako se ispuni bez uvjeta balansa (npr. razapinjuće stablo, 2-bojenje po dubini). Poteškoća je balans; ograničenje „najviše dva lista po vrhu” točno je ono koje jamči rješivost — to je predmet članka na koji upućuje službeno rješenje.</p>'''),
        ('Algoritam', r'''<p>Službeni tutorial ne daje vlastiti opis algoritma, već upućuje na članak <em>„The even adjacency split problem for graphs”</em>, odjeljak 3, gdje je opisana konstrukcija u linearnom vremenu. Na ovoj stranici zato ne reproduciramo korake koji nisu u službenom materijalu.</p>'''),
    ],
    'solution': r'''
<p>Službeno rješenje glasi: vidi članak <em>„The even adjacency split problem for graphs”</em>, odjeljak 3.</p>
<p>Napomena prevoditelja: službeni tutorial ne sadrži daljnji opis algoritma — cjelovita konstrukcija (podjela vrhova povezanog grafa na dvije strane jednake veličine tako da svaki vrh ima susjeda na drugoj strani, uz pretpostavku o najviše dva susjedna lista) nalazi se u navedenom članku.</p>
''',
},
# ---------------------------------------------------------------- H
{
    'letter': 'H', 'title': 'Classical Maximization Problem', 'title_hr': 'Klasični zadatak maksimizacije', 'slug': 'H_classical_maximization_problem',
    'tl': '2 s', 'ml': '512 MiB',
    'statement': r'''
<p>Dano je $2n$ različitih točaka. Par točaka je <em>prijateljski</em> ako dijele $x$ ili $y$ koordinatu. Podijeli točke u $n$ parova tako da je broj prijateljskih parova najveći; ispiši ga i parove.</p>
<h3>Ulaz</h3>
<p>$t \le 10^4$ testova; $n \le 10^5$ ($\sum n \le 10^5$), koordinate do $10^9$.</p>
<h3>Izlaz</h3>
<p>$k$ i parovi.</p>
''',
    'hints': [
        r'''<p>Bipartitni graf: vrh za svaku $x$-koordinatu i za svaku $y$-koordinatu; točka $(x_i, y_i)$ je brid. Prijateljski par = dva brida sa zajedničkim vrhom. Traži se najveći broj disjunktnih parova susjednih bridova.</p>''',
        r'''<p>U svakoj povezanoj komponenti s $m$ bridova može se postići $\lfloor m/2 \rfloor$ parova: DFS-stablo (nema poprečnih bridova!), rekurzivno od dna sparuj bridove kroz vrh $v$: nespareni bridovi prema djeci + povratni bridovi prema potomcima; ako ih je neparno, preostali spari s bridom prema roditelju.</p>''',
    ],
    'coach': [
        ('Opažanje', r'''<p>Točke su bridovi bipartitnog grafa ($x$-vrijednosti nasuprot $y$-vrijednostima); prijateljski par = dva brida koji dijele vrh. Problem: rastaviti što više bridova u parove susjednih bridova. Komponente su neovisne, a gornja granica po komponenti je $\lfloor m_c / 2 \rfloor$.</p>'''),
        ('Redukcija', r'''<p>Tvrdnja: u povezanoj komponenti s $m$ bridova uvijek se dobije $\lfloor m/2 \rfloor$ parova. Uzmi DFS-stablo: u neusmjerenom grafu svaki nestablasti brid spaja pretka i potomka (nema poprečnih bridova).</p>'''),
        ('Algoritam', r'''<p>Rekurzivno $f(v)$: pozovi $f(u)$ za svu djecu $u$; svako dijete ili „potroši” brid $u - v$ (ako je broj bridova u podstablu $u$ neparan) ili ga ostavi nesparenog. Skup $T$ = nespareni bridovi $v - u$ + svi povratni bridovi iz $v$ prema potomcima koji nisu djeca (bridovi prema precima obrađuje predak). Svi bridovi u $T$ imaju zajednički vrh $v$: spari ih proizvoljno; ako je $|T|$ neparan, preostali spari s bridom $v$ – roditelj. Na kraju ostaje najviše jedan nespareni brid uz korijen komponente. Nesparene točke iz svih komponenata spari proizvoljno.</p>'''),
        ('Složenost', r'''<p>$O(n)$ uz kompresiju koordinata ($O(n \log n)$ s mapom). Iterativni DFS zbog dubine do $2 \cdot 10^5$.</p>'''),
    ],
    'solution': r'''
<p>Izgradimo bipartitni graf koji ima vrh za svaku vrijednost $x$-koordinate i vrh za svaku vrijednost $y$-koordinate. Svaka točka $(x_i, y_i)$ postaje brid koji spaja vrhove $x = x_i$ i $y = y_i$. U tom grafu treba formirati najveći broj disjunktnih parova bridova sa zajedničkim vrhom.</p>
<p>Za svaku povezanu komponentu problem se rješava zasebno. Pokažimo da u povezanoj komponenti s $m$ bridova uvijek možemo formirati $\lfloor m/2 \rfloor$ parova.</p>
<p>Izgradi DFS-stablo komponente. U komponenti svaki brid ili pripada stablu ili ide od pretka prema potomku — nema poprečnih bridova.</p>
<p>Riješimo problem rekurzivno od dna prema vrhu. Za svako podstablo DFS-stabla podijelit ćemo sve bridove unutar njega u prijateljske parove, a brid od korijena podstabla prema roditelju iskoristit ćemo ako je broj bridova u podstablu neparan.</p>
<p>Rekurzivna funkcija $f(v)$: najprije pozovi $f(u)$ za svu djecu $u$ korijena podstabla $v$. Iz svakog $u$ ili iskoristimo brid $u - v$ ili ga ostavimo nesparenog. Formiraj skup $S$ svih takvih nesparenih bridova te svih bridova koji iz $v$ idu prema njegovim potomcima (koji nisu izravna djeca). Svi bridovi u $S$ imaju $v$ kao zajednički vrh. Podijeli ih u parove proizvoljno; ako je $|S|$ neparan, preostali brid spari s bridom od $v$ prema roditelju.</p>
<p>Na kraju smo sve bridove podijelili u prijateljske parove, osim možda jednog brida incidentnog s korijenom.</p>
''',
},
# ---------------------------------------------------------------- I
{
    'letter': 'I', 'title': 'Classical Minimization Problem', 'title_hr': 'Klasični zadatak minimizacije', 'slug': 'I_classical_minimization_problem',
    'tl': '2 s', 'ml': '512 MiB',
    'statement': r'''
<p>Kao H, ali broj prijateljskih parova (zajednički $x$ ili $y$) treba <em>minimizirati</em>.</p>
<h3>Ulaz</h3>
<p>$t \le 10^4$ testova; $n \le 10^5$ ($\sum n \le 10^5$), $2n$ različitih točaka.</p>
<h3>Izlaz</h3>
<p>$k$ i parovi.</p>
''',
    'hints': [
        r'''<p>Neka je $k$ najveći broj točaka na jednom (vodoravnom ili okomitom) pravcu. Ako je $k > n$, barem $k - n$ parova mora biti unutar tog pravca — i točno toliko je dovoljno. Ako je $k \le n$, može se postići $0$ prijateljskih parova.</p>''',
        r'''<p>Gradi parove jedan po jedan, indukcijom, čuvajući invarijantu $k \le n$: uvijek spari točku s najpunijeg vodoravnog pravca $H$ s točkom s najpunijeg okomitog $V$ (uz pažljive posebne slučajeve kad se $H$ i $V$ sijeku u jedinoj točki). Prioritetni redovi ili liste po broju točaka.</p>''',
    ],
    'coach': [
        ('Opažanje', r'''<p>Neka je $k$ najveći broj točaka na istom vodoravnom ili okomitom pravcu. Ako je $k > n$, najviše jedan pravac ima više od $n$ točaka, a među $n$ parova barem $k - n$ ih spaja dvije točke tog pravca — dakle neprijateljskih parova najviše $2n - k$. Ako je $k \le n$, tvrdimo da neprijateljskih može biti $n$ (nula prijateljskih).</p>'''),
        ('Redukcija: indukcija po $n$', r'''<p>Slučaj $k > n$: formiraj par s jednom točkom s prenapučenog pravca (i bilo kojom drugom točkom koja nije na njemu, ili čak s njega) — $n$ i $k$ oba padnu za $1$, pa induktivno dobijemo $2n - k$ neprijateljskih. Slučaj $k \le n$: trebamo par koji koristi po jednu točku sa <em>svakog</em> pravca koji ima točno $n$ točaka (da invarijanta $k' \le n - 1$ preživi). Ako postoje i vodoravni i okomiti pravac s $n$ točaka, par uzima po točku s oba; ako samo jedan, par ga dotiče; inače bilo koji valjan par. Dva vodoravna pravca s $n$ točaka: svaki neprijateljski par tada nužno dotiče oba.</p>'''),
        ('Algoritam', r'''<p>Ponavljaj: $H$ = vodoravni pravac s najviše točaka, $V$ = okomiti s najviše. Ako $H$ ili $V$ sadrži svih $2n$ točaka — stani (ostatak sparuj unutar pravca). Ako $H$ ima samo $1$ točku i ona leži na $V$: spari je s točkom s drugog najpunijeg okomitog $V'$. Simetrično za $V$. Inače uzmi $h \in H$, $v \in V$; ako $h \in V$ zamijeni $h$ drugom točkom s $H$, ako $v \in H$ zamijeni $v$ (moguće jer oba imaju $\ge 2$ točke); spari $h, v$.</p>'''),
        ('Složenost', r'''<p>$O(n \log n)$ s prioritetnim redovima, ili $O(n)$ s $2n$ vezanih lista indeksiranih brojem točaka na pravcu.</p>'''),
    ],
    'solution': r'''
<p>Želimo formirati što više neprijateljskih parova. Neka je $k$ najveći broj točaka na istom okomitom ili vodoravnom pravcu. Ako je $k \le n$, pokazat ćemo da je odgovor (broj neprijateljskih parova) $n$. Ako je $k > n$, odgovor očito ne prelazi $2n - k$, a pokazat ćemo da je točno toliko.</p>
<p>Tvrdnje dokazujemo indukcijom po $n$, formirajući parove jedan po jedan.</p>
<p>Ako je $k > n$: najviše jedan pravac može sadržavati više od $n$ točaka, pa trebamo formirati par koji koristi točku s tog pravca. Tada se i $n$ i $k$ smanje za $1$, a ako od ostatka formiramo $2(n-1) - (k-1) = 2n - k - 1$ parova, ukupno dobivamo $2n - k$.</p>
<p>Ako je $k \le n$, trebamo formirati par koji koristi barem jednu točku sa svakog pravca koji sadrži $n$ točaka: ako postoje i vodoravni i okomiti pravac s $n$ točaka, par sadrži po točku s oba; ako postoji samo vodoravni ili samo okomiti, par uključuje točku s njega; ako takvih pravaca nema, bilo koji valjan par. Mogu postojati dva vodoravna (ili dva okomita) pravca s $n$ točaka, ali tada svaki valjan par koristi po točku s oba, što nam odgovara.</p>
<p>Algoritam koji pokriva sve slučajeve — ponavljaj:</p>
<ul>
<li>Nađi $H$, vodoravni pravac s najviše točaka, i $V$, okomiti pravac s najviše točaka.</li>
<li>Ako $H$ ili $V$ sadrži svih $2n$ točaka, stani — više se parova ne može formirati.</li>
<li>Ako $H$ sadrži samo $1$ točku i ona leži na $V$, neka je $V'$ okomiti pravac s drugim najvećim brojem točaka; formiraj par iz jedine točke na $H$ i bilo koje točke na $V'$.</li>
<li>Inače, ako $V$ sadrži samo $1$ točku i ona leži na $H$, neka je $H'$ vodoravni pravac s drugim najvećim brojem točaka; formiraj par iz jedine točke na $V$ i bilo koje točke na $H'$.</li>
<li>Inače neka je $h$ bilo koja točka na $H$ i $v$ bilo koja točka na $V$. Ako $h$ leži na $V$, zamijeni $h$ drugom točkom s $H$; ako $v$ leži na $H$, zamijeni $v$ drugom točkom s $V$ (moguće jer $H$ i $V$ imaju barem $2$ točke). Formiraj par $(h, v)$.</li>
</ul>
<p>Za implementaciju mogu se koristiti prioritetni redovi za $H$ i $V$ — $O(n \log n)$. Budući da je broj točaka na pravcu ograničen s $2n$, može se koristiti i $2n$ vezanih lista (lista $i$ sadrži pravce s $i$ točaka) uz pokazivače na najveće neprazne liste — $O(n)$.</p>
''',
},
# ---------------------------------------------------------------- J
{
    'letter': 'J', 'title': 'Classical Scheduling Problem', 'title_hr': 'Klasični zadatak raspoređivanja', 'slug': 'J_classical_scheduling_problem',
    'tl': '6 s', 'ml': '512 MiB',
    'statement': r'''
<p>Imaš $t$ minuta; tema $i$ uči se $a_i$ minuta, a siguran si u nju samo ako ukupno naučiš barem $b_i$ tema. Odaberi teme (zbroj $a \le t$) tako da je broj tema u koje si siguran najveći; ispiši ga i odabrane teme.</p>
<h3>Ulaz</h3>
<p>$q \le 10^4$ testova; $n \le 2 \cdot 10^5$ ($\sum n \le 2 \cdot 10^5$), $t \le 2 \cdot 10^{14}$, $a_i \le 10^9$, $1 \le b_i \le n$.</p>
<h3>Izlaz</h3>
<p>Broj sigurnih tema, $k$ i indeksi.</p>
<h3>Primjer</h3>
<p>$t = 100$, teme $(20,1), (40,4), (60,3), (30,3)$: nauči $1, 2, 4$ ($90$ min), siguran u $2$ teme.</p>
''',
    'hints': [
        r'''<p>Sortiraj po $b$. Binarno pretraživanje po $x$ = broj sigurnih tema: ako učiš $k \ge x$ tema $p_1 < \dots < p_k$ (po $b$), siguran si upravo u prvih $x$ — uvjet je $k \ge b_{p_x}$.</p>''',
        r'''<p>Fiksiraj $i = p_x$ (tema s najvećim $b$ među sigurnima): uzmi $x - 1$ najjeftinijih tema iz $1..i-1$ i $\max(0, b_i - x)$ najjeftinijih iz $i+1..n$ (kao „punjenje”). Provjeri zbroj $\le t$. Prefiksne/sufiksne najmanje $a$ s prioritetnim redom.</p>''',
    ],
    'coach': [
        ('Opažanje', r'''<p>Preuredi teme tako da je $b_1 \le b_2 \le \dots \le b_n$. Ako naučiš $k$ tema, siguran si u one s $b \le k$ — to su one s najmanjim $b$ među naučenima, dakle prefiks naučenih u ovom poretku.</p>'''),
        ('Redukcija: binarno pretraživanje', r'''<p>„Mogu li biti siguran u barem $x$ tema” je monotono u $x$. Provjera: naučene teme $p_1 < \dots < p_k$, $k \ge x$; siguran u $p_1..p_x$ ako i samo ako $k \ge b_{p_x}$.</p>'''),
        ('Algoritam: provjera za $x$', r'''<p>Iteriraj po $i$ kao kandidatu za $p_x$. Tada iz $1..i-1$ biramo $x - 1$ tema s najmanjim $a$ (sigurne), a iz $i+1..n$ biramo $\max(0, b_i - x)$ tema s najmanjim $a$ (samo za dopunu broja $k$ do $b_i$). Ako ukupno vrijeme (uključivo $a_i$) $\le t$, $x$ je izvedivo. Prefiksne sume „$x - 1$ najmanjih” dobiju se prolazom slijeva s max-heapom veličine $x - 1$; sufiksne „$j$ najmanjih” za promjenjivo $j = b_i - x$… budući da $b_i$ raste s $i$, potrebni $j$ raste, a sufiks se skraćuje — održavaj heap zdesna s dinamičkom veličinom (ili predizračunaj sufiksne „$j$ najmanjih” za potrebne $j$ prolazom zdesna, gdje $j$ pada kad $i$ pada).</p>'''),
        ('Složenost', r'''<p>$O(n \log^2 n)$ — jedan log od binarnog pretraživanja, drugi od prioritetnog reda.</p>'''),
    ],
    'solution': r'''
<p>Bez smanjenja općenitosti preuredimo teme tako da je $b_1 \le b_2 \le \dots \le b_n$.</p>
<p>Binarno pretražujemo $x$, broj tema u koje ćeš biti siguran. Kako provjeriti može li se biti siguran u $x$ tema?</p>
<p>Neka su $p_1 < p_2 < \dots < p_k$ teme koje učiš ($k \ge x$). Budući da su teme poredane po $b$, moraš biti siguran u teme $p_1, \dots, p_x$, pa mora vrijediti $k \ge b_{p_x}$.</p>
<p>Iterirajmo po temi $i$: može li biti $p_x = i$? Tada trebamo odabrati $x - 1$ tema s najmanjim $a_j$ među temama $1, \dots, i-1$ i $\max(0, b_i - x)$ tema s najmanjim $a_j$ među temama $i+1, \dots, n$. Ako ukupno vrijeme učenja odabranih tema (uključivo teme $i$) ne prelazi $t$, u redu je.</p>
<p>Za $x - 1$ tema s najmanjim $a_j$ na svakom prefiksu prolazimo niz slijeva nadesno s prioritetnim redom; za $\max(0, b_i - x)$ tema s najmanjim $a_j$ na svakom sufiksu prolazimo zdesna nalijevo, također s prioritetnim redom.</p>
<p>Ukupna vremenska složenost: $O(n \log^2 n)$ (jedan logaritam od binarnog pretraživanja po $x$, drugi od prioritetnog reda).</p>
''',
},
# ---------------------------------------------------------------- K
{
    'letter': 'K', 'title': 'Classical Summation Problem', 'title_hr': 'Klasični zadatak zbrajanja', 'slug': 'K_classical_summation_problem',
    'tl': '2 s', 'ml': '512 MiB',
    'statement': r'''
<p>Gradovi $1..n$ na putu, $d(u, v) = |u - v|$. $k$ prijatelja živi u gradovima $a_1..a_k$ i sastaju se u gradu $v$ koji minimizira $\sum d(v, a_i)$ (kod izjednačenja najmanji broj). Po svih $n^k$ rasporeda prijatelja, zbroji brojeve odabranih gradova, modulo $998244353$.</p>
<h3>Ulaz</h3>
<p>$n, k$ ($2 \le n, k \le 10^6$).</p>
<h3>Izlaz</h3>
<p>Zbroj.</p>
''',
    'hints': [
        r'''<p>Sortiraj $a$: za neparan $k$ sastaju se u medijanu $a_{(k+1)/2}$, za paran u donjem medijanu $a_{k/2}$. Radi s očekivanjem uz uniformno slučajne gradove i na kraju pomnoži s $n^k$.</p>''',
        r'''<p>Neparan $k$: simetrija daje $E = (n+1)/2$. Paran $k$: $E$ srednje vrijednosti dvaju medijana je $(n+1)/2$; donji medijan je manji za $d/2$, gdje je $d$ razmak medijana; $E(d) = \sum_{i=1}^{n-1} P(\text{segment } (i, i+1) \text{ je između medijana}) = \sum_i \binom{k}{k/2} i^{k/2} (n-i)^{k/2} / n^k$.</p>''',
    ],
    'coach': [
        ('Opažanje', r'''<p>Sortiraj $a_1 \le \dots \le a_k$. Zbroj udaljenosti minimizira se u medijanu; za neparan $k$ to je $a_{(k+1)/2}$, za paran bilo koji grad u $[a_{k/2}, a_{k/2+1}]$, a bira se najmanji — $a_{k/2}$. Gledajmo očekivanje kad svaki prijatelj bira grad uniformno i neovisno; odgovor je $E \cdot n^k$.</p>'''),
        ('Redukcija: neparan $k$', r'''<p>Preslikavanje $a \mapsto n + 1 - a$ čuva raspodjelu i preslikava medijan u $n + 1 - $ medijan, pa $E(a_{(k+1)/2}) = \frac{n+1}{2}$. Odgovor: $\frac{n+1}{2} \cdot n^k$ (modularno s inverzom od $2$).</p>'''),
        ('Redukcija: paran $k$', r'''<p>Neka je $m = \frac{a_{k/2} + a_{k/2+1}}{2}$ i $d = a_{k/2+1} - a_{k/2}$. Simetrijom $E(m) = \frac{n+1}{2}$, a $a_{k/2} = m - d/2$, pa $E(a_{k/2}) = \frac{n+1}{2} - \frac{1}{2} E(d)$. $d$ je broj segmenata $(i, i+1)$ koji leže između dvaju medijana; segment $(i, i+1)$ je između njih ako i samo ako točno $k/2$ prijatelja živi u $1..i$ i točno $k/2$ u $i+1..n$: $p_i = \binom{k}{k/2} i^{k/2} (n-i)^{k/2} / n^k$; $E(d) = \sum_{i=1}^{n-1} p_i$.</p>'''),
        ('Algoritam i složenost', r'''<p>Odgovor za paran $k$: $\frac{n+1}{2} n^k - \frac{1}{2} \binom{k}{k/2} \sum_{i=1}^{n-1} i^{k/2} (n-i)^{k/2}$, sve mod $998244353$. Potencije brzim potenciranjem: $O(n \log k + k)$ (faktorijeli za binomni koeficijent).</p>'''),
    ],
    'solution': r'''
<p>Preuredimo gradove u kojima prijatelji žive tako da je $a_1 \le a_2 \le \dots \le a_k$. Ako je $k$ neparan, prijatelji se sastaju u gradu $a_{(k+1)/2}$; ako je $k$ paran, u gradu $a_{k/2}$. Usredotočimo se na očekivanu vrijednost odgovora uz pretpostavku da svaki prijatelj bira grad uniformno slučajno, i na kraju je pomnožimo s $n^k$.</p>
<p>Za neparan $k$ zbog simetrije vrijedi $E(a_{(k+1)/2}) = \frac{n+1}{2}$, pa je odgovor $\frac{n+1}{2} \cdot n^k$.</p>
<p>Za paran $k$ ne možemo isto zaključiti o $a_{k/2}$, ali možemo promatrati prosjek dvaju medijana $m = \frac{a_{k/2} + a_{k/2+1}}{2}$, za koji je $E(m) = \frac{n+1}{2}$. Neka je $d = a_{k/2+1} - a_{k/2}$ razmak dvaju medijana. Tada je $a_{k/2} = m - \frac{d}{2}$ i $E(a_{k/2}) = E(m) - E(\frac{d}{2}) = \frac{n+1}{2} - \frac{1}{2} E(d)$.</p>
<p>Kako naći $E(d)$? Za svaki $i = 1, \dots, n-1$ nađimo vjerojatnost $p_i$ da dužina između gradova $i$ i $i+1$ leži između dvaju medijana; tada je $E(d) = \sum_{i=1}^{n-1} p_i$. Za to je potrebno da točno $\frac{k}{2}$ prijatelja živi u gradovima $1, \dots, i$ i točno $\frac{k}{2}$ u gradovima $i+1, \dots, n$:</p>
$$p_i = \frac{i^{k/2} (n-i)^{k/2} \binom{k}{k/2}}{n^k}.$$
<p>Vremenska složenost: $O(n \log k + k)$.</p>
''',
},
]
