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
        ('Broj ima do $4000$ znamenki – što uopće možemo isprobavati, a što sigurno ne?',
         r'''<p>Ne možemo isprobavati sve rastave $n = a + b$, ali repdigita je vrlo malo: repdigit je potpuno određen duljinom i znamenkom, pa ih s najviše $L$ znamenki ima samo $9L$. Zato je prirodna ideja fiksirati jedan pribrojnik (onaj veći, $a$) i drugi <em>izračunati</em> kao $b = n - a$; tada samo treba provjeriti je li $b$ repdigit. Ostaje pitanje koliko kandidata za $a$ zaista moramo pogledati.</p>'''),
        ('Koliko znamenki može imati veći pribrojnik $a$ u odnosu na $n$?',
         r'''<p>Uz $a \ge b \ge 1$ vrijedi $a < n = a + b \le 2a$. Iz $a < n$ slijedi $|a| \le |n|$. Iz $n \le 2a$ slijedi $|n| \le |2a| \le |a| + 1$, jer množenje s $2$ dodaje najviše jednu znamenku. Dakle $|a| \in \{|n| - 1, |n|\}$: veći pribrojnik ima ili jednako znamenki kao $n$ ili točno jednu manje.</p>'''),
        ('Zašto je onda dovoljno samo $18$ kandidata i kako se svaki provjerava?',
         r'''<p>Dvije duljine puta devet znamenki daje $18$ repdigita $a$. Za svaki izračunamo $b = n - a$ oduzimanjem znamenku po znamenku (školski algoritam s posudbom, $O(|n|)$), odbacimo slučaj $b \le 0$ i provjerimo da su sve znamenke od $b$ (nakon uklanjanja vodećih nula) jednake. Kako se jamči da rastav postoji, a naš skup kandidata sadrži veći pribrojnik <em>svakog</em> rastava, jedan kandidat sigurno prolazi.</p>'''),
        ('Koje sitnice u implementaciji najčešće ruše ovakav zadatak?',
         r'''<p>Tri stvari: (1) kandidat $a$ duljine $|n|$ može biti veći od $n$ – tada ga treba preskočiti prije oduzimanja; (2) rezultat oduzimanja može imati vodeće nule koje treba ukloniti prije provjere; (3) $b$ mora biti pozitivan, tj. $a = n$ nije rješenje. Ukupno radimo $18 \cdot O(|n|)$ posla po testu, a $\sum |n| \le 10^5$, pa je vrijeme zanemarivo.</p>'''),
    ],
    'tips': [
        r'''Kad je jedan dio odgovora iz <strong>malog skupa kandidata</strong> (repdigiti, potencije, palindromi fiksne duljine…), fiksiraj njega i drugi dio izračunaj – „isprobaj sve i provjeri” pobjeđuje bilo kakvu pametnu teoriju brojeva.''',
        r'''Za brojeve koji ne stanu u 64 bita, oduzimanje i usporedba nizova znamenki pišu se u nekoliko redaka; drži brojeve kao <code>string</code> bez vodećih nula i piši pomoćne funkcije <code>manji(a, b)</code> i <code>oduzmi(a, b)</code>.''',
        r'''Ograniči kandidate nejednakostima o duljini: iz $a \le n \le 2a$ odmah slijedi $|n| - 1 \le |a| \le |n|$. Slična ocjena „broj znamenki zbroja” vrijedi u mnogim zadacima s velikim brojevima.''',
    ],
    'solution': r'''
<p>Neka $|x|$ označava broj znamenki cijelog broja $x$. U $n = a + b$ bez smanjenja općenitosti neka je $a \ge b$. Lako se vidi da je $|n| - 1 \le |a| \le |n|$.</p>
<p>Dakle postoje samo $2$ mogućnosti za duljinu od $a$ i $9$ mogućnosti za znamenku od koje se $a$ sastoji — ukupno $18$ mogućnosti za $a$. Isprobamo svaku, izračunamo $b = n - a$ i provjerimo je li $b$ repdigit.</p>
''',
    'detailed': r'''
<h3>1. Zašto pretraga po kandidatima</h3>
<p>Broj $n$ ima do $4000$ znamenki, pa ne dolazi u obzir ništa što bi iteriralo po vrijednosti $n$. Ključna je struktura repdigita: repdigit je jednoznačno zadan duljinom $L$ i znamenkom $c \in \{1, \dots, 9\}$, tj. $a = c \cdot \underbrace{11\ldots1}_{L}$. Zato ih je s najviše $L$ znamenki samo $9L$. Ako uspijemo pokazati da veći pribrojnik $a$ ima samo nekoliko mogućih duljina, dovoljno je isprobati sve takve $a$, izračunati $b = n - a$ i provjeriti je li $b$ repdigit.</p>
<h3>2. Ocjena duljine većeg pribrojnika</h3>
<p>Neka je $n = a + b$ s $a \ge b \ge 1$. Tada vrijedi</p>
$$a < a + b = n \le a + a = 2a.$$
<p>Iz $a < n$ slijedi $|a| \le |n|$ (manji broj nema više znamenki). Iz $n \le 2a$ slijedi $|n| \le |2a|$, a množenje s $2$ povećava broj znamenki za najviše jedan (jer iz $a < 10^{|a|}$ slijedi $2a < 2 \cdot 10^{|a|} < 10^{|a| + 1}$), pa je $|n| \le |a| + 1$. Zajedno: $|a| \in \{|n| - 1, |n|\}$. To daje najviše $2 \cdot 9 = 18$ kandidata za $a$ (za jednoznamenkasti $n$ duljina $0$ otpada i ostaje $9$ kandidata).</p>
<p>Primijetimo da ovo <em>nije</em> tvrdnja da svaki od $18$ kandidata daje rješenje; tvrdnja je da veći pribrojnik svakog postojećeg rastava pripada tom skupu. Kako zadatak jamči da rastav postoji, barem jedan kandidat prolazi provjeru.</p>
<h3>3. Algoritam</h3>
<ol>
<li>Pročitaj $n$ kao niz znamenki; $L = |n|$.</li>
<li>Za svaku duljinu $\ell \in \{L - 1, L\}$ (uz $\ell \ge 1$) i svaku znamenku $c \in \{1, \dots, 9\}$ sastavi $a = cc\ldots c$ ($\ell$ znamenki).</li>
<li>Ako je $a \ge n$, preskoči (tada bi $b \le 0$). Usporedba velikih brojeva: kraći niz je manji, a pri jednakoj duljini odlučuje leksikografski poredak.</li>
<li>Izračunaj $b = n - a$ školskim oduzimanjem s posudbom, zdesna nalijevo; nakon toga ukloni vodeće nule.</li>
<li>Ako su sve znamenke od $b$ jednake (i $b$ nije prazan, tj. $b > 0$), ispiši $a$ i $b$ i prekini.</li>
</ol>
<p>Redoslijed ispisa nije bitan – bilo koji valjani par prolazi.</p>
<h3>4. Zašto ne treba i $|a| = |n| - 2$ ili više kandidata</h3>
<p>Kad bi $a$ imao $|n| - 2$ ili manje znamenki, i $b \le a$ bi imao toliko, pa bi $a + b < 2 \cdot 10^{|n| - 2} < 10^{|n| - 1} \le n$ – kontradikcija. Isto tako, kandidat s $|n| + 1$ znamenki premašuje $n$. Dakle skup od $18$ kandidata je i nužan i dovoljan za potpunost pretrage.</p>
<h3>5. Složenost</h3>
<p>Po testu radimo $18$ oduzimanja i provjera, svako u $O(|n|)$, dakle $O(18 \cdot |n|)$. Uz $\sum |n| \le 10^5$ to je ukupno oko $2 \cdot 10^6$ operacija nad znamenkama – daleko ispod ograničenja od $4$ sekunde.</p>
<h3>6. Zamke u implementaciji</h3>
<ul>
<li>Znamenke čuvaj kao znakove ili male cijele brojeve; nikada ne pokušavaj pretvoriti $n$ u brojevni tip (ne stane ni u <code>__int128</code>).</li>
<li>Posudba pri oduzimanju: ako je trenutna znamenka negativna, dodaj $10$ i prenesi $-1$ na sljedeću poziciju. Kako je $a < n$, na kraju nema neriješene posudbe.</li>
<li>Nakon oduzimanja ukloni vodeće nule prije provjere jednakosti znamenki; inače bi npr. $b = 0007$ bio krivo odbačen.</li>
<li>Poseban slučaj $|n| - 1 = 0$ (jednoznamenkasti $n$) – kandidati duljine $0$ ne postoje, jednostavno preskoči tu duljinu.</li>
</ul>
<h3>7. Primjer</h3>
<p>$n = 786$: kandidati duljine $3$ su $111, 222, \dots, 999$, a duljine $2$ su $11, \dots, 99$. Za $a = 777$ dobivamo $b = 9$ – repdigit, gotovo. Za $n = 10^{28} + 1 = 1\underbrace{00\ldots0}_{27}1$ svi kandidati duljine $29$ premašuju $n$ ($111\ldots1 > 100\ldots01$), pa prolazimo kandidate duljine $28$: $a = 99\ldots9$ daje $b = 10^{28} + 1 - (10^{28} - 1) = 2$.</p>
''',
    'verified': r'''uzorak 1/1 (tri službena para); 300 slučajnih testova ($n$ do $8$ znamenki, generiran kao zbroj dvaju slučajnih repdigita) protiv brute forcea u Pythonu, uz checker koji provjerava da su ispisani $a, b$ repdigiti sa zbrojem $n$; 3 velika testa ($25$ brojeva s $\approx 4000$ znamenki, $<0.01$ s).''',
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
        ('Što zapravo odlučuje može li skup $S$ „proći” – suci ili samo konačni bodovi?',
         r'''<p>Direktor može proizvoljno razriješiti izjednačenja i birati $p$, pa je $S$ moguć čim postoje konačni bodovi $b_i = a_i + (\text{glasovi}_i)$ s $\min_{i \in S} b_i \ge \max_{i \notin S} b_i$. Suci ulaze samo kroz ograničenja na broj glasova: svaki zadatak dobije između $0$ i $m$ glasova, a ukupno ih je točno $mv$. Zato se pitanje svodi na: postoji li raspodjela glasova $g_i \in [0, m]$, $\sum g_i = mv$, za koju $S$ „pobjeđuje”? Odmah sortiramo $a_1 \ge \dots \ge a_n$ da bi $S$ imao jednostavan oblik.</p>'''),
        ('Zašto se svaka raspodjela glasova $g_i \in [0, m]$ sa $\sum g_i = mv$ zaista može realizirati sucima koji biraju točno $v$ različitih zadataka?',
         r'''<p>Cikličkom konstrukcijom: zapiši niz s $g_1$ kopija broja $1$, $g_2$ kopija broja $2$, …, ukupno $mv$ elemenata, i neka sudac $j$ uzme pozicije $j, j + m, j + 2m, \dots$ ($v$ pozicija). Dva izabrana elementa istog suca udaljena su barem $m$, a svaki zadatak zauzima blok duljine $g_i \le m$, pa sudac nikad ne uzme isti zadatak dvaput. Time je uvjet na sucima potpuno zamijenjen uvjetom $0 \le g_i \le m$, $\sum g_i = mv$.</p>'''),
        ('Kako iz oblika skupa $S$ (sortirano po $a$) pročitati najmanje i najveće dopuštene glasove?',
         r'''<p>Neka je $x$ prvi indeks izvan $S$, $y$ zadnji indeks u $S$. Pobjednički prag može se postaviti na $b_x$ (zadatak $x$ ima najveći početni rezultat izvan $S$, a najbolje je da ne dobije glasove), pa svaki $i \in S$ mora dostići barem $a_x$: $l_i = \max(0, a_x - a_i)$, što je $0$ za $i < x$. Obratno, ako $S$ pobjeđuje, svi izbačeni moraju ostati ispod najslabijeg člana $S$, a on može imati najviše $a_y + m$: $r_i = \min(m, a_y + m - a_i)$ za $i \notin S$, $m$ inače. Kriterij: $a_y + m \ge a_x$ i $\sum l_i \le mv \le \sum r_i$ – između minimuma i maksimuma svaki ukupni zbroj glasova se postiže povećavanjem po jednog glasa.</p>'''),
        ('Zašto naivni ruksak po paru $(x, y)$ nije dovoljno brz i što ga spašava?',
         r'''<p>Za svaki par $(x, y)$ radili bismo ruksak po zadacima između njih: $O(n^2)$ parova puta $O(n \cdot mv)$ – prekoračuje $10^{10}$. No $l_i = a_x - a_i$ ovisi samo o $x$, a $r_i = a_y + m - a_i$ samo o $y$! Zato brojimo dvije stvari odvojeno: skupove s $\sum l > mv$ prolaskom po $x$ (DP unaprijed, $y$ je jednostavno zadnji uzeti element) i skupove s $\sum r < mv$ prolaskom po $y$ (DP unatrag). Kako je $l_i \le r_i$, ta dva loša događaja ne mogu nastupiti istodobno, pa je odgovor $\#\{a_y + m \ge a_x\} - \#\{\sum l > mv\} - \#\{\sum r < mv\}$.</p>'''),
        ('Kako držati ruksak malim kad je zbroj potencijalno velik?',
         r'''<p>Zanima nas samo je li zbroj $\le mv$ (odn. $\le m(n - v)$ za sufiksnu varijantu), pa sve zbrojeve veće od granice spojimo u jedno „preliveno” stanje. Ruksak ima $O(mv) \le 10^4$ stanja, po fiksiranom kraju obradimo $O(n)$ zadataka: ukupno $O(n^2 \cdot mv) \approx 10^8$ jednostavnih operacija za $n = m = 100$, uz $\sum n \le 100$ sasvim dovoljno.</p>'''),
    ],
    'tips': [
        r'''Kad procesi (suci, glasači, koraci) izgledaju složeno, pokušaj ih zamijeniti <strong>uvjetima na agregatima</strong> („svaki dobije između $0$ i $m$, ukupno $mv$”) i posebno dokaži da je svaki takav agregat ostvariv – ciklička konstrukcija $j, j + m, j + 2m, \dots$ standardni je alat.''',
        r'''Prebrojavanje skupova s uvjetom oblika $\min_{\text{u}} \ge \max_{\text{izvan}}$ gotovo uvijek počinje sortiranjem i opisom skupa preko „prvog izbačenog” i „zadnjeg uzetog” indeksa.''',
        r'''Kad DP mora vrijediti za dva parametra ($x$ i $y$), provjeri ovisi li težina svakog elementa zaista o oba – često ovisi samo o jednom, pa se dva prolaza (unaprijed i unatrag) zamijene za jednu dimenziju složenosti.''',
        r'''U ruksaku gdje pitamo samo „je li zbroj $\le C$”, spoji sva stanja $> C$ u jedno; to čuva točnost i ograničava memoriju na $C + 2$.''',
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
    'detailed': r'''
<h3>1. Od sudaca do raspodjele glasova</h3>
<p>Skup $S$ ulazi u „skup zadataka” ako direktor može odabrati $p = |S|$ i razriješiti izjednačenja tako da prvih $p$ u nerastućem poretku bude upravo $S$. To je moguće točno onda kada su konačni bodovi $b_i = a_i + g_i$ takvi da je $\min_{i \in S} b_i \ge \max_{i \notin S} b_i$ ($g_i$ = broj glasova zadatku $i$). Dakle suci su bitni samo kroz vektor glasova $g = (g_1, \dots, g_n)$.</p>
<p><b>Lema 1.</b> Vektor $g$ je ostvariv (postoji izbor $v$ različitih zadataka za svakog od $m$ sudaca s točno tim brojevima glasova) ako i samo ako $0 \le g_i \le m$ za sve $i$ i $\sum g_i = mv$.</p>
<p><i>Dokaz.</i> Nužnost je očita: svaki sudac glasa jednom za zadatak, a ukupno se podijeli $mv$ glasova. Dovoljnost: zapišimo niz od $g_1$ jedinica, $g_2$ dvojki, …, $g_n$ $n$-ova; duljina mu je $mv$. Sudac $j$ ($1 \le j \le m$) uzima pozicije $j, j + m, \dots, j + (v-1)m$. Dobije točno $v$ pozicija. Dvije njegove pozicije udaljene su barem $m$, a sve kopije istog zadatka čine blok duljine $g_i \le m$ (ako je $g_i = m$, blok ima točno $m$ elemenata, pa sudac uzme najviše jedan – pozicije $j$ i $j + m$ ne mogu obje biti u bloku duljine $m$). Dakle svaki sudac glasa za $v$ <em>različitih</em> zadataka, a zadatak $i$ dobije točno $g_i$ glasova. $\square$</p>
<p>Od sada je pitanje čisto kombinatoričko: postoji li $g \in [0, m]^n$ sa $\sum g_i = mv$ za koji $S$ pobjeđuje?</p>
<h3>2. Oblik skupa i kriterij</h3>
<p>Sortiramo $a_1 \ge a_2 \ge \dots \ge a_n$ (izjednačene proizvoljno – svaki podskup indeksa je i dalje različit skup zadataka, a brojimo skupove indeksa). Za $S$ neka je $x$ najmanji indeks izvan $S$, a $y$ najveći indeks u $S$. Ako je $x > y$, $S = \{1, \dots, y\}$ je prefiks; takvih je skupova $n$ i svi su mogući: glasove dijelimo najprije članovima $S$ (dok su izbačeni na $0$ glasova, prefiks vodi već po početnim bodovima), a kad svi članovi imaju $m$ glasova, ostatak izbačenima – oni tada ne mogu prijeći $a_y + m$. Neka je dalje $x < y$.</p>
<p><b>Najmanji glasovi.</b> Ako $S$ pobjeđuje uz $g$, tada je $b_i \ge b_x \ge a_x$ za svaki $i \in S$, pa je $g_i \ge a_x - a_i$. Definiramo $l_i = \max(0, a_x - a_i)$ za $i \in S$ i $l_i = 0$ inače. Za $i < x$ je $a_i \ge a_x$, pa je $l_i = 0$; jedini netrivijalni $l_i$ su za $i \in S$, $x < i \le y$, gdje je $l_i = a_x - a_i$.</p>
<p><b>Najveći glasovi.</b> Zadatak $y \in S$ može imati najviše $a_y + m$ bodova, pa svaki $i \notin S$ mora ostati na $b_i \le a_y + m$, tj. $g_i \le a_y + m - a_i$. Definiramo $r_i = \min(m, a_y + m - a_i)$ za $i \notin S$ i $r_i = m$ za $i \in S$. Za $i > y$ vrijedi $a_i \le a_y$, pa je $r_i = m$; netrivijalni $r_i$ su za $i \notin S$, $x \le i < y$, gdje je $r_i = a_y + m - a_i$. Ako je $a_y + m < a_x$, tada je $r_x < 0$ i $S$ je nemoguć.</p>
<p><b>Lema 2.</b> Vrijedi $l_i \le r_i$ za sve $i$ (uz $a_y + m \ge a_x$), a $S$ je moguć ako i samo ako</p>
$$\sum_i l_i \le mv \le \sum_i r_i.$$
<p><i>Dokaz.</i> Za $i \in S$: $l_i \le m$ jer je $a_x - a_i \le a_x - a_y \le m$, a $r_i = m$. Za $i \notin S$: $l_i = 0 \le r_i$. Nužnost uvjeta: svaki pobjednički $g$ zadovoljava $l_i \le g_i \le r_i$, pa je $\sum l \le \sum g = mv \le \sum r$. Dovoljnost: krenemo od $g = l$ i povećavamo koordinate za $1$, najprije zadacima u $S$ do $m$, zatim zadacima izvan $S$ do $r_i$, dok zbroj ne postane $mv$ (moguće jer je $\sum l \le mv \le \sum r$). Tvrdimo da tako dobiveni $g$ pobjeđuje: ako smo stali dok su još povećavani samo zadaci iz $S$, svi $i \in S$ imaju $b_i \ge a_x$, a svi $i \notin S$ imaju $g_i = 0$, tj. $b_i = a_i \le a_x$ – pobjeda uz prag $a_x$. Ako smo prešli na zadatke izvan $S$, svi $i \in S$ imaju $g_i = m$, dakle $b_i \ge a_y + m$, a svaki $i \notin S$ ima $b_i \le a_i + r_i \le a_y + m$ – pobjeda uz prag $a_y + m$. Po Lemi 1 takav $g$ je ostvariv. $\square$</p>
<h3>3. Komplementarno prebrojavanje</h3>
<p>Zbog $l_i \le r_i$ imamo $\sum l \le \sum r$, pa se događaji „$\sum l > mv$” i „$\sum r < mv$” <em>međusobno isključuju</em>. Stoga među skupovima s $x < y$ i $a_y + m \ge a_x$ vrijedi</p>
$$\#\{\text{mogući}\} = \#\{a_y + m \ge a_x\} - \#\{\textstyle\sum l > mv\} - \#\{\textstyle\sum r < mv\}.$$
<p>Prva dva člana zajedno daju $\#\{a_y + m \ge a_x \text{ i } \sum l \le mv\}$, što ćemo brojati DP-om po $x$; treći član brojimo DP-om po $y$. Na kraju dodamo $n$ prefiksnih skupova.</p>
<h3>4. Zašto se dimenzija $y$ (odnosno $x$) može izostaviti</h3>
<p>Ključno: $l_i = a_x - a_i$ ovisi samo o $x$, a ne o $y$. Fiksiramo $x$: zadaci $1, \dots, x - 1$ su u $S$, $x$ nije, a članovi $S$ iza $x$ su neprazan podskup indeksa $i > x$ s $a_i + m \ge a_x$ (uvjet $a_y + m \ge a_x$ za najveći od njih automatski vrijedi za sve manje jer je niz nerastući). Broj načina da zbroj $\sum_{i \in S, i > x} (a_x - a_i)$ bude $\le mv$ je običan ruksak $f(s)$ = broj podskupova sa zbrojem $s$, gdje zbrojeve $> mv$ spojimo u jedno stanje $mv + 1$. Element $y$ uopće ne treba pratiti – on je „zadnji uzeti”. Oduzmemo $1$ za prazan podskup (tada bi $S$ bio prefiks, već ubrojen).</p>
<p>Simetrično, $r_i = a_y + m - a_i$ ovisi samo o $y$. Fiksiramo $y$: $y \in S$, zadaci iza $y$ nisu, a izbačeni ispred $y$ čine neprazan podskup indeksa $i < y$ s $a_i \le a_y + m$; $x$ je najmanji od njih. Kako je $\sum r = nm - \sum_{i \notin S, i < y} (a_i - a_y)$, uvjet $\sum r < mv$ glasi $\sum_{i \notin S, i < y} (a_i - a_y) > m(n - v)$ – ruksak s granicom $m(n - v)$ i prelivenim stanjem, a brojimo upravo preliveno stanje.</p>
<h3>5. Algoritam</h3>
<ol>
<li>Sortiraj $a$ nerastuće. $\text{ans} = n$ (prefiksi).</li>
<li>Za svaki $x = 1..n$: ruksak po $i = x + 1, \dots$ dok je $a_i + m \ge a_x$, s težinama $a_x - a_i \in [0, m]$ i kapacitetom $mv$; dodaj $\left(\sum_{s \le mv} f(s)\right) - 1$.</li>
<li>Za svaki $y = 1..n$: ruksak po $i = y - 1, \dots$ dok je $a_i \le a_y + m$, s težinama $a_i - a_y \in [0, m]$ i kapacitetom $m(n - v)$; oduzmi $f(\text{preliveno})$.</li>
<li>Ispiši $\text{ans} \bmod 998244353$ (pazi na negativne međurezultate: dodaj $\text{MOD}$ prije uzimanja ostatka).</li>
</ol>
<h3>6. Složenost</h3>
<p>Po fiksiranom kraju obradimo $O(n)$ elemenata s ruksakom od $O(mv) \le 9900$ stanja: $O(n^2 \cdot mv) \approx 10^8$ operacija za najveći test, a $\sum n \le 100$ jamči da je to ujedno i ukupno. Memorija $O(mv)$. (Službena ocjena $O(n^3 a_n)$ odnosi se na varijantu ruksaka po vrijednosti bodova; ovdje je granica $mv$ prirodnija.)</p>
<h3>7. Zamke</h3>
<ul>
<li>Prelijevanje ruksaka: pri prijelazu <code>ns = min(cap + 1, s + w)</code> obavezno prođi i stanje $s = \text{cap} + 1$ (ono ostaje preliveno), inače se izgube brojevi.</li>
<li>Težina $w = 0$ (jednaki bodovi) je legitimna: podskup se udvostručuje bez promjene zbroja; iteriraj $s$ silazno da svaki element uđe najviše jednom.</li>
<li>Ne zaboravi uvjet $a_y + m \ge a_x$ – u DP-u po $x$ to je granica petlje, u DP-u po $y$ također; time se u oba prolaza broje isti skupovi pa se komplementarno oduzimanje slaže.</li>
</ul>
<h3>8. Primjer</h3>
<p>$n = 3$, $m = 1$, $v = 2$, sortirano $a = (3, 2, 1)$, $mv = 2$. Prefiksi: $\{1\}, \{1,2\}, \{1,2,3\}$ (izvorno $\{3\}, \{2,3\}, \{1,2,3\}$). $x = 1$: kandidati $i$ s $a_i + 1 \ge 3$ – samo $i = 2$; $S = \{2\}$, $\sum l = 1 \le 2$, $\sum r = 0 + 1 + 1 = 2 \ge 2$ – moguć. $x = 2$: $S = \{1, 3\}$, $\sum l = 1$, $\sum r = 1 + 0 + 1 = 2$ – moguć. Ukupno $5$, što se slaže s primjerom.</p>
''',
    'verified': r'''uzorak 1/1; 300 slučajnih testova ($n \le 5$, $m \le 3$, $a_i \le 8$) protiv brute forcea u Pythonu koji prolazi sve $\binom{n}{v}^m$ kombinacije glasova i skuplja moguće skupove; 3 velika testa ($n = m = 100$, $a_i \le 100$, najviše $0.03$ s).''',
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
        r'''<p>Umjesto cijepanja u sredini, cijepaj čvor točno na granici upita: $[x, y) \to [x, l), [l, y)$ — najviše $4$ nova čvora po upitu, $O(n)$ memorije. Ali visina može postati $\Omega(n)$; rotacije (AVL, splay) ili slučajni prioriteti (treap) vraćaju $O(\log n)$.</p>''',
    ],
    'coach': [
        ('Koja je to operacija zapravo – što se traži od strukture podataka?',
         r'''<p>Petlja „za svaki $j \in [l, r]$: $a_j \mathrel{+}= i$, $x \mathrel{+}= a_j$” je isto što i: dodaj $i$ svim elementima intervala, zatim pribroji $x$-u zbroj <em>novih</em> vrijednosti na intervalu. To su dvije klasične operacije (dodavanje na intervalu, zbroj intervala) koje lijeno segmentno stablo radi u $O(\log N)$. Sve se računa modulo $2^{30}$, pa je dovoljno računati u 32-bitnom tipu bez predznaka i na kraju maskirati – prirodno prelijevanje radi umjesto nas jer $2^{30} \mid 2^{32}$.</p>'''),
        ('Zašto obično dinamičko segmentno stablo ne prolazi kad je $N = 2^{30}$ i memorija $128$ MiB?',
         r'''<p>Nemamo $2^{30}$ elemenata, pa čvorove stvaramo po potrebi. No klasično dinamičko stablo dijeli segment na polovice: put od korijena do lista ima $m = 30$ razina, i svaki upit može stvoriti $O(m)$ novih čvorova na oba svoja kraja. Uz $n = 5 \cdot 10^5$ to je do $3 \cdot 10^7$ čvorova – s bar $16$–$24$ bajta po čvoru daleko iznad $128$ MiB.</p>'''),
        ('Što ako segment cijepamo točno na granici upita, a ne na polovici?',
         r'''<p>Tada je stablo skup „elementarnih segmenata” na kojima su svi elementi jednaki (počinjemo s jednim segmentom $[0, 2^m)$). Upit $[l, r]$ treba granice na $l$ i na $r + 1$; svaka od njih ili već postoji ili prepolovi točno jedan segment. Dakle najviše $2$ nova segmenta po upitu i $O(n)$ segmenata ukupno – memorija je riješena. Cijena: oblik stabla više ne prati binarnu strukturu indeksa, pa ugniježđeni upiti ($[i, N - 1 - i]$) daju visinu $\Theta(n)$.</p>'''),
        ('Kako vratiti logaritamsku visinu ako stablo više nije određeno indeksima?',
         r'''<p>Čvorovi su poredani po poziciji, a interval čvora je unija intervala njegova podstabla – to je točno struktura <em>implicitnog</em> balansiranog stabla pretraživanja (ključ = pozicija). Rotacije čuvaju uređaj i time semantiku; samo treba održavati agregate (ukupna duljina i zbroj podstabla) i lijenu oznaku. Najjednostavnije: implicitni treap sa slučajnim prioritetima, operacije <code>split</code> po duljini i <code>merge</code>; očekivana dubina je $O(\log n)$. AVL ili splay daju istu ocjenu deterministički odn. amortizirano.</p>'''),
        ('Kako izgleda jedan upit u tom modelu i koliko košta?',
         r'''<p><code>split(root, l)</code> daje $[0, l)$ i ostatak; <code>split(ostatak, r - l + 1)</code> odvaja $[l, r]$. Srednjem dijelu lijeno dodamo $i$ (njegov zbroj raste za $i \cdot (r - l + 1)$), pročitamo njegov zbroj u $x$, pa sve spojimo natrag. Tri <code>split</code>/<code>merge</code> operacije po upitu, svaka $O(\log n)$ očekivano: ukupno $O(n \log n)$ vremena i $O(n)$ memorije – s $n = 5 \cdot 10^5$ manje od sekunde.</p>'''),
    ],
    'tips': [
        r'''Kad je domena indeksa ogromna, a broj upita malen, razmisli o <strong>strukturi nad segmentima jednake vrijednosti</strong>: stanje je uvijek opisivo s $O(\text{broj upita})$ segmenata, bez obzira na $N$.''',
        r'''Implicitni treap sa <code>split</code>/<code>merge</code> po duljini univerzalna je zamjena za balansirano segmentno stablo: lijene oznake i agregati održavaju se u <code>push</code>/<code>update</code> na isti način kao u segmentnom stablu.''',
        r'''Modul oblika $2^k$ znači da smiješ računati u <code>unsigned</code> tipu i maskirati samo na kraju – nikakvog <code>%</code> u vrućoj petlji.''',
        r'''Prije nego što prihvatiš „$O(n)$ čvorova”, konstruiraj najgori slučaj za visinu (ugniježđeni ili monotoni intervali) i uvjeri se da balansiranje zaista postoji u tvojoj implementaciji – za treap to znači da svaki <em>novi</em> čvor dobiva svjež slučajan prioritet.''',
    ],
    'solution': r'''
<p>Zadatak izgleda kao standardni zadatak s dinamičkim segmentnim stablom. Početno stvorimo jedan čvor za segment $[0, 2^m)$. Kad dođe upit $[l, r]$, spuštamo se od vrha i dođemo do čvora bez djece koji odgovara segmentu $[x, y)$ s $x < l < y$; tada stvorimo dva nova čvora za $[x, \frac{x+y}{2})$ i $[\frac{x+y}{2}, y)$ i nastavimo. Slično za segment koji sadrži $r$.</p>
<p>Tako nastaje $O(m)$ novih čvorova po upitu, tj. $O(nm)$ memorije, što je možda previše jer je memorijsko ograničenje strogo.</p>
<p>Umjesto cijepanja $[x, y)$ na polovice, možemo cijepati na $[x, l)$ i $[l, y)$. Tada cijepamo samo jednom za $l$ i jednom za $r$, pa je ukupno potrebno $O(n)$ prostora (najviše $4$ nova čvora po upitu). Međutim, sada vrijeme može biti problem: visina stabla može narasti na $\Omega(n)$, npr. ako su svi upiti ugniježđeni.</p>
<p>Rješenje: rotacijama rebalansiramo segmentno stablo, slično kao u mnogim balansiranim binarnim stablima pretraživanja. Tehnikama AVL-stabla ili splay-stabla dobivamo $O(n \log n)$ vremena i $O(n)$ prostora.</p>
''',
    'detailed': r'''
<h3>1. Prevođenje operacije</h3>
<p>U $i$-tom koraku za svaki $j \in [l, r]$ redom radimo $a_j \mathrel{+}= i$ i $x \mathrel{+}= a_j$. Kako svaki $a_j$ u trenutku pribrajanja već sadrži dodatak $i$, ukupno je $x \mathrel{+}= \sum_{j=l}^{r} (a_j + i) = \big(\sum_{j=l}^{r} a_j\big) + i \cdot (r - l + 1)$, računano s vrijednostima <em>prije</em> koraka. Dakle upit je: (1) dodaj $i$ na intervalu, (2) pribroji zbroj intervala. Granice $l, r$ ovise o $x$ (mod $2^m$), pa upite moramo obrađivati online.</p>
<p>Sve se traži modulo $2^{30}$; kako je $2^{30} \mid 2^{32}$, možemo sve zbrojeve i umnoške držati u <code>uint32_t</code> i pustiti da se prirodno prelijevaju, a rezultat maskirati s $2^{30} - 1$. Umnožak $i \cdot (r - l + 1)$ je do $5 \cdot 10^5 \cdot 2^{30}$, ali nas zanima samo modulo $2^{32}$, pa je 32-bitno množenje ispravno.</p>
<h3>2. Zašto dinamičko segmentno stablo pada na memoriji</h3>
<p>Niz ima $N = 2^{30}$ elemenata, pa gradimo stablo samo za segmente koje upiti dotaknu. Klasična implementacija dijeli $[x, y)$ na polovice; za granicu $l$ upita spuštamo se kroz $m$ razina i na svakoj možda stvorimo čvor – $O(m)$ novih čvorova po granici, $O(2nm) \approx 3 \cdot 10^7$ ukupno. S bar $16$ bajta po čvoru (dva pokazivača, zbroj, lijena oznaka) to je pola gigabajta, a ograničenje je $128$ MiB.</p>
<h3>3. Segmenti jednake vrijednosti</h3>
<p>Ključno opažanje: sve što je upit ikad napravio nizu jest „dodaj konstantu na interval”. Zato je nakon $q$ upita niz <em>po dijelovima konstantan</em> s najviše $2q + 1$ dijelova: granice dijelova su samo pozicije $l$ i $r + 1$ prošlih upita. Umjesto stabla nad indeksima gradimo strukturu nad tim <em>elementarnim segmentima</em>: svaki čvor pamti duljinu segmenta $\text{len}$ i zajedničku vrijednost $\text{val}$ svih njegovih elemenata.</p>
<p>Za upit $[l, r]$ trebamo granice točno na $l$ i $r + 1$. Ako neka od njih pada strogo unutar segmenta $[x, y)$, prepolovimo ga na $[x, l)$ i $[l, y)$ (isti $\text{val}$) – jedan novi čvor. Dakle najviše $2$ nova čvora po upitu, ukupno $\le 2n + 1 \approx 10^6$ čvorova. Po $32$ bajta to je $32$ MiB. (Službeno rješenje govori o „najviše $4$” jer u njegovoj varijanti cijepanje segmenta stvara dva nova čvora umjesto da postojeći skrati; brojka je ista po redu veličine.)</p>
<h3>4. Zašto treba balansiranje i zašto ga rotacije smiju raditi</h3>
<p>Ako segmente držimo u binarnom stablu čiji oblik određuju redoslijedi cijepanja, ugniježđeni upiti $[i, N - 1 - i]$ svaki put cijepaju krajnje segmente i stablo raste u „lanac” visine $\Theta(n)$ – svaki upit tada košta $\Theta(n)$ i ukupno $\Theta(n^2)$.</p>
<p>Spas je u tome što stablo segmenata <em>nije</em> vezano za indekse: to je jednostavno uređeni slijed segmenata, gdje je interval unutarnjeg čvora unija intervala njegova podstabla. To je točno implicitno binarno stablo pretraživanja s ključem „pozicija”, a rotacije čuvaju in-order poredak, dakle i semantiku, pod uvjetom da nakon rotacije ponovno izračunamo agregate ($\text{sublen}$, $\text{subsum}$) i da prije nje spustimo lijenu oznaku. Time smijemo koristiti bilo koju tehniku balansiranja: AVL, splay ili treap.</p>
<h3>5. Implementacija treapom</h3>
<p>Naše rješenje koristi implicitni treap (slučajni prioriteti). Čvor: $\text{len}, \text{val}, \text{sublen}, \text{subsum}, \text{lazy}, \text{pri}, \text{lc}, \text{rc}$. Operacije:</p>
<ul>
<li><code>dodaj(t, d)</code>: $\text{val} \mathrel{+}= d$, $\text{subsum} \mathrel{+}= d \cdot \text{sublen}$, $\text{lazy} \mathrel{+}= d$ – lijeno dodavanje cijelom podstablu.</li>
<li><code>push(t)</code> spušta $\text{lazy}$ djeci; <code>update(t)</code> računa $\text{sublen}$ i $\text{subsum}$ iz djece i vlastitog segmenta ($\text{len} \cdot \text{val}$).</li>
<li><code>split(t, k)</code>: rascijepi na prvih $k$ jedinica duljine i ostatak. Spuštamo se po $\text{sublen}$ lijevog djeteta; ako granica padne strogo unutar segmenta čvora, čvor skratimo na $k$ jedinica i stvorimo novi čvor za ostatak sa <em>svježim</em> prioritetom, pa ga spojimo s desnim podstablom.</li>
<li><code>merge(a, b)</code>: klasično spajanje treapova po prioritetu (svi segmenti $a$ prethode segmentima $b$).</li>
</ul>
<p>Upit $[l, r]$ u koraku $i$: <code>split(root, l)</code> $\to A, B$; <code>split(B, r - l + 1)</code> $\to B, C$; <code>dodaj(B, i)</code>; $x \mathrel{+}= \text{subsum}(B)$; <code>root = merge(A, merge(B, C))</code>.</p>
<h3>6. Složenost</h3>
<p>Treap s $\le 2n + 1$ čvorova ima očekivanu dubinu $O(\log n)$ neovisno o redoslijedu operacija (prioriteti su slučajni, a novi čvorovi dobivaju svjež prioritet), pa su <code>split</code> i <code>merge</code> očekivano $O(\log n)$. Ukupno $O(n \log n)$ očekivano, $O(n)$ memorije (oko $32$ MiB). Na $5 \cdot 10^5$ upita s $m = 30$ rješenje radi ispod jedne sekunde uz ograničenje od $3$ s.</p>
<h3>7. Zamke</h3>
<ul>
<li>Granice upita: $l = (p + x) \bmod 2^m$, $r = (q + x) \bmod 2^m$, pa <em>zatim</em> $l \le r$ zamjenom; koristi masku $2^m - 1$ na 32-bitnom $x$ (točno jer $2^m \mid 2^{32}$).</li>
<li>Duljine segmenata dosežu $2^{30}$ – stanu u <code>uint32_t</code>, ali ne u <code>int</code> ako računaš $2^{31}$ ili više; kod $m = 30$ je $2^m = 2^{30}$ još u redu, ali ne zbrajaj dvije takve duljine u <code>int</code>.</li>
<li>Uvijek <code>push</code> prije nego što spustiš u djecu (u <code>split</code> i <code>merge</code>), i <code>update</code> nakon promjene djece.</li>
<li>Zamjena <code>scanf</code>-a brzim čitanjem isplati se: ulaz ima $10^6$ brojeva.</li>
<li>Rekurzija u <code>split</code>/<code>merge</code> ide do dubine stabla ($O(\log n)$ očekivano, u praksi $< 100$), pa nema opasnosti od prelijevanja stoga.</li>
</ul>
''',
    'verified': r'''uzorak 1/1; 300 slučajnih testova ($n \le 40$, $m \le 5$) protiv brute forcea koji izravno simulira niz; 3 velika testa s $n = 5 \cdot 10^5$, $m = 30$ (slučajni, ugniježđeni $[i, N - 1 - i]$ i kratki pomični intervali), najviše $0.91$ s i oko $34$ MB memorije.''',
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
        ('Kada je polje Youngova dijagrama pokriveno – ovisi li to o položaju drugih topova?',
         r'''<p>Redak $i$ dijagrama je neprekinuti prefiks $[1, a_i]$, a stupac $j$ neprekinuti prefiks redaka $[1, b_j]$. Zato top u retku $i$ „vidi” sva polja svog retka: ako mu put blokira drugi top, taj je bliži i sam pokriva ciljano polje. Polje $(i, j)$ je pokriveno točno onda kada je u retku $i$ <em>ili</em> stupcu $j$ neki top. Blokiranje je dakle nebitno, što cijeli zadatak pretvara u kombinatoriku redaka i stupaca.</p>'''),
        ('Koji dio dijagrama određuje donju granicu za broj topova?',
         r'''<p>Uz $a_1 \ge \dots \ge a_n$ niz $a_i - i$ strogo pada, pa je skup $\{i : a_i \ge i\}$ prefiks duljine $k$ – to je stranica najvećeg kvadrata koji se uklapa (redci $1..k$, stupci $1..k$). S manje od $k$ topova neki redak $i \le k$ i neki stupac $j \le k$ nemaju topa, a polje $(i, j)$ postoji ($j \le k \le a_k \le a_i$) i nije pokriveno. Dakle $r \ge k$.</p>'''),
        ('Zašto $k$ topova uvijek dostaje?',
         r'''<p>Topovi na dijagonali $(1,1), \dots, (k,k)$: polje u retku $i \le k$ pokriva top tog retka; polje u retku $i > k$ ima stupac $j \le a_i \le a_{k+1} \le k$ (jer $k$ je zadnji indeks s $a_k \ge k$), pa ga pokriva top stupca $j$. Znači svako polje leži u prvih $k$ redaka ili prvih $k$ stupaca – to je razlog zašto $r = k$ i ujedno struktura koju ćemo iskoristiti za brojanje.</p>'''),
        ('Kako izgledaju sva valjana postavljanja točno $k$ topova?',
         r'''<p>Ako neki redak $i \le k$ i neki stupac $j \le k$ ostanu bez topa, $(i, j)$ je nepokriveno. Dakle vrijedi (1) svaki od prvih $k$ redaka ima topa – tada su to svi topovi, po jedan u retku – ili (2) svaki od prvih $k$ stupaca ima topa. Pod (1) polja u recima $> k$ (stupci $1..t$, $t = a_{k+1}$) pokrivaju se samo stupcima, pa svaki od stupaca $1..t$ mora dobiti topa; sve ostalo je automatski pokriveno. (2) je ista situacija na transponiranom dijagramu, a presjek (1) $\cap$ (2) su permutacijske matrice unutar kvadrata: $k!$, sve valjane. Odgovor: $|(1)| + |(2)| - k!$.</p>'''),
        ('Kako prebrojati postavljanja „po jedan top u svakom od $k$ redaka, svaki od $t$ stupaca pogođen”?',
         r'''<p>Redak po redak; stupci $1..t$ postoje u svakom od prvih $k$ redaka jer $t \le k \le a_k$. Stanje je samo broj $j$ već pogođenih obveznih stupaca (koji točno – nije važno, jer su svi preostali redci dovoljno široki). Iz $f(i, j)$ top retka $i + 1$ ide u jedan od $t - j$ još nepogođenih obveznih stupaca ($\to j + 1$) ili u jedan od $a_{i+1} - (t - j)$ ostalih polja ($\to j$). Tražimo $f(k, t)$; $O(k \cdot t) \le O(n^2)$ vremena i $O(t)$ memorije s dva retka DP-a.</p>'''),
    ],
    'tips': [
        r'''Za topove na Youngovu dijagramu (ili bilo kojem „stubišnom” obliku) blokiranje je iluzija: pokrivenost polja ovisi samo o tome ima li topa u njegovu retku ili stupcu. Provjeri to prvo – često cijelu geometriju pretvara u brojanje.''',
        r'''Najveći kvadrat u Youngovu dijagramu (Durfeeov kvadrat) određen je s $k = \max\{i : a_i \ge i\}$ i simetričan je pri transponiranju – idealan je „svjedok” za donju granicu koja se ujedno postiže.''',
        r'''Kad je uvjet „A ili B” s jednostavnim presjekom, uključivanje–isključivanje $|A| + |B| - |A \cap B|$ dijeli problem na dva simetrična dijela; simetriju iskoristi doslovno – transponiraj ulaz i pozovi istu funkciju.''',
        r'''U DP-u tipa „koliko obveznih ciljeva je već pogođeno” pazi da stanje bude dovoljno: ovdje jest jer su svi obvezni stupci sadržani u svakom retku ($t \le a_k$); da nisu, trebalo bi pamtiti <em>koji</em> su pogođeni.''',
    ],
    'solution': r'''
<p>Radi praktičnosti obrnimo $a$ tako da je $a_1 \ge a_2 \ge \dots \ge a_n$.</p>
<p>Nađi stranicu $k$ najvećeg kvadrata koji se uklapa u dijagram: $k$ je jedini cijeli broj s $a_k \ge k$ i $a_{k+1} < k + 1$. Tada je najmanji broj topova jednak $k$: za pokrivanje kvadrata $k \times k$ potrebno je barem $k$ topova, a sva ostala polja pripadaju ili jednom od prvih $k$ redaka ili jednom od prvih $k$ stupaca, pa $k$ topova na glavnoj dijagonali kvadrata pokriva sve.</p>
<p>Prebrojimo valjana postavljanja $k$ topova. Barem jedan od uvjeta mora vrijediti: (1) svaki od prvih $k$ redaka sadrži topa; (2) svaki od prvih $k$ stupaca sadrži topa. Ako ne vrijedi nijedan, barem jedno polje u kvadratu nije pokriveno (polje u retku bez topa i stupcu bez topa). Odgovor je broj postavljanja koja zadovoljavaju (1) plus broj koja zadovoljavaju (2) minus broj koja zadovoljavaju oba — a zadnji je $k!$.</p>
<p>Prebrojimo postavljanja s uvjetom (1); (2) se dobiva analogno nakon transponiranja. Neka je $t = a_{k+1}$ — broj stupaca koji moraju sadržavati barem jednog topa da bi cijeli dijagram bio pokriven. Neka je $f(i, j)$ broj načina postavljanja topova u prvih $i$ redaka tako da točno $j$ od prvih $t$ stupaca sadrži barem jednog topa; $f(0, 0) = 1$, a tražimo $f(k, t)$. Prijelazi iz $(i, j)$: top u retku $i+1$ ide u jedan od $t - j$ stupaca koji trebaju topa a nemaju ga — stanje $(i+1, j+1)$, $t - j$ načina; inače broj pokrivenih obveznih stupaca ostaje isti — stanje $(i+1, j)$, $a_{i+1} - (t - j)$ načina.</p>
<p>Vremenska složenost: $O(n^2)$.</p>
''',
    'detailed': r'''
<h3>1. Postavka i pokrivenost</h3>
<p>Ulaz daje $a_1 \le \dots \le a_n$; obrnemo ga tako da je $a_1 \ge a_2 \ge \dots \ge a_n$ (redak $1$ je najširi). Redak $i$ sadrži polja $(i, 1), \dots, (i, a_i)$; stupac $j$ sadrži polja $(1, j), \dots, (b_j, j)$, gdje je $b_j = |\{i : a_i \ge j\}|$ – <em>transponirani</em> dijagram, također nerastući. Oba su prefiksi, bez rupa.</p>
<p><b>Lema 1.</b> Polje $(i, j)$ je pokriveno ako i samo ako se u retku $i$ ili u stupcu $j$ nalazi top.</p>
<p><i>Dokaz.</i> Ako je u retku $i$ top, uzmimo onaj najbliži polju $(i, j)$ (s bilo koje strane). Sva polja između njih pripadaju dijagramu (redak je neprekinut) i prazna su (bliži top ne postoji), pa top u jednom potezu dolazi na $(i, j)$. Analogno za stupac. Obratno, top se kreće samo po svom retku i stupcu. $\square$</p>
<h3>2. Najmanji broj topova</h3>
<p>Niz $a_i - i$ strogo pada (jer $a$ ne raste, a $i$ raste), pa je $\{i : a_i \ge i\} = \{1, \dots, k\}$ za jedinstveni $k \ge 1$ (jer $a_1 \ge 1$). Vrijedi $a_k \ge k$ i $a_{k+1} \le k$ (dogovorno $a_{n+1} = 0$). Kvadrat $\{1..k\} \times \{1..k\}$ leži u dijagramu jer $a_i \ge a_k \ge k$ za $i \le k$.</p>
<p><b>Donja granica.</b> Uz $r < k$ topova barem jedan redak $i \le k$ i barem jedan stupac $j \le k$ nemaju topa; polje $(i, j)$ postoji i po Lemi 1 nije pokriveno.</p>
<p><b>Gornja granica.</b> Topovi na $(1,1), \dots, (k,k)$ pokrivaju sve: polje $(i, j)$ s $i \le k$ pokriva top retka $i$; polje s $i > k$ ima $j \le a_i \le a_{k+1} \le k$, pa ga pokriva top stupca $j$. Dakle $r = k$. Usput smo dokazali: <em>svako polje dijagrama leži u jednom od prvih $k$ redaka ili jednom od prvih $k$ stupaca.</em></p>
<h3>3. Struktura valjanih postavljanja</h3>
<p>Promatramo postavljanja točno $k$ topova (na različita polja) koja pokrivaju cijeli dijagram.</p>
<p><b>Lema 2.</b> Svako valjano postavljanje zadovoljava (1) svaki od redaka $1..k$ sadrži topa, ili (2) svaki od stupaca $1..k$ sadrži topa.</p>
<p><i>Dokaz.</i> U suprotnom postoje redak $i \le k$ i stupac $j \le k$ bez topa, a $(i, j)$ je u kvadratu i nepokriveno. $\square$</p>
<p>Uvjet (1) s točno $k$ topova znači: u svakom od redaka $1..k$ točno jedan top, a u recima $> k$ nijedan. Koja su takva postavljanja valjana? Polja u recima $\le k$ pokrivena su vlastitim topom. Polja u recima $i > k$ imaju stupce $j \le a_i \le a_{k+1} =: t$; u njihovim recima topa nema, pa moraju biti pokrivena stupcem: <em>svaki od stupaca $1..t$ mora sadržavati topa</em>. Taj uvjet je i dovoljan (svako polje s $i > k$ tada ima topa u stupcu). Napomena: ako je $k = n$, tada je $t = 0$ i uvjet je prazan.</p>
<p>Uvjet (2) je isti problem na transponiranom dijagramu $b$: Durfeeov kvadrat je simetričan pa je $k$ isti, a ulogu $t$ preuzima $t' = b_{k+1}$ = broj redaka širine $\ge k + 1$.</p>
<p>Presjek (1) $\cap$ (2): $k$ topova, po jedan u svakom od redaka $1..k$ i u svakom od stupaca $1..k$ – dakle svi su unutar kvadrata i čine permutaciju: $k!$ postavljanja, i sva su valjana (svako polje je u tih $k$ redaka ili $k$ stupaca). Uključivanje–isključivanje:</p>
$$w = |(1)| + |(2)| - k!.$$
<h3>4. DP za uvjet (1)</h3>
<p>Treba prebrojati načine da se u redak $i$ ($1 \le i \le k$) stavi top na jedno od $a_i$ polja tako da svaki stupac $1..t$ dobije barem jednog topa. Ključno: $t = a_{k+1} \le k \le a_k \le a_i$, pa su svi obvezni stupci prisutni u <em>svakom</em> od $k$ redaka. Zato nije važno <em>koji</em> su obvezni stupci već pogođeni, nego samo <em>koliko</em> ih je – svaki redak nudi svaki nepogođeni obvezni stupac.</p>
<p>Definiramo $f(i, j)$ = broj načina da se topovi postave u prvih $i$ redaka tako da točno $j$ obveznih stupaca sadrži topa. $f(0, 0) = 1$, prijelazi iz $(i, j)$ u redak $i + 1$:</p>
<ul>
<li>top u jedan od $t - j$ nepogođenih obveznih stupaca: $f(i+1, j+1) \mathrel{+}= (t - j) \cdot f(i, j)$;</li>
<li>top u bilo koje od ostalih $a_{i+1} - (t - j)$ polja (pogođeni obvezni ili neobvezni stupci): $f(i+1, j) \mathrel{+}= (a_{i+1} - (t - j)) \cdot f(i, j)$.</li>
</ul>
<p>Svako postavljanje ulazi u točno jednu granu na svakom koraku, pa je $|(1)| = f(k, t)$. Isti kod na $(b, k, t')$ daje $|(2)|$.</p>
<h3>5. Složenost i memorija</h3>
<p>DP ima $k \cdot (t + 1) \le n(n + 1)$ stanja s $O(1)$ prijelaza: $O(n^2) \approx 2.5 \cdot 10^7$ za $n = 5000$. Držimo samo dva retka ($f$ i $g$), pa je memorija $O(n)$. Transponirani niz $b$ računa se u $O(n)$ dvostrukim pokazivačem po nerastućem $a$.</p>
<h3>6. Zamke</h3>
<ul>
<li>Ne zaboravi obrnuti ulaz (dan je rastuće) i računati $k$ 1-bazirano: $k$ je najveći $i$ s $a_i \ge i$.</li>
<li>Rubni slučaj $k = n$ (npr. puna ploča $a \equiv n$): $t = t' = 0$, oba DP-a daju $\prod a_i$, a odgovor je $2 \prod_{i} a_i - k!$; za $a \equiv n$ to je $2 n^n - n!$. Za $n = 1$: $r = 1$, $w = 1$.</li>
<li>Množitelj $a_{i+1} - (t - j)$ nikad nije negativan zbog $t \le a_{i+1}$ – ako u tvojoj implementaciji jest, $k$ ili $t$ su krivo izračunati.</li>
<li>Oduzimanje $k!$ radi modulo: dodaj $\text{MOD}$ prije $\%$.</li>
</ul>
<h3>7. Primjer</h3>
<p>$a = (1, 2, 3)$, obrnuto $(3, 2, 1)$: $a_1 = 3 \ge 1$, $a_2 = 2 \ge 2$, $a_3 = 1 < 3$, dakle $k = 2$, $t = a_3 = 1$. DP: nakon retka $1$ ($a_1 = 3$): $f(1, 1) = 1$, $f(1, 0) = 2$. Redak $2$ ($a_2 = 2$): iz $(1,1)$ ostala polja $2 - 0 = 2$ $\to f(2,1) \mathrel{+}= 2$; iz $(1,0)$ obvezni stupac $\to f(2,1) \mathrel{+}= 2 \cdot 1$, ostalo $\to f(2,0) \mathrel{+}= 2 \cdot 1$. $|(1)| = f(2, 1) = 4$. Dijagram je samokonjugiran ($b = (3, 2, 1)$), pa je $|(2)| = 4$. $w = 4 + 4 - 2! = 6$, $r = 2$ – kao u primjeru.</p>
''',
    'verified': r'''uzorak 1/1; 300 slučajnih testova ($n \le 5$) protiv brute forcea u Pythonu koji za $r = 1, 2, \dots$ isprobava sve rasporede $r$ topova i simulira pokrivenost; 3 velika testa s $n = 5000$ (slučajni, puna ploča $a \equiv n$, stubište $a_i = i$), najviše $0.02$ s.''',
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
        ('Što se iz zadatka D prenosi bez promjene, a što više ne prolazi?',
         r'''<p>Cijela struktura: $r = k$ (stranica najvećeg kvadrata), $w = |(1)| + |(2)| - k!$, gdje je $|(1)|$ broj načina da se u svaki od redaka $1..k$ (širine $a_1 \ge \dots \ge a_k$) stavi po jedan top tako da svaki od stupaca $1..t$ ($t = a_{k+1}$) bude pogođen, a $|(2)|$ isto na transponiranom dijagramu. Ne prolazi samo DP $f(i, j)$ s $O(k \cdot t)$ stanja: za $n \approx 1.3 \cdot 10^5$ to je $\sim 10^{10}$.</p>'''),
        ('Kako prebrojati „svaki obvezni stupac pogođen” bez pamćenja koliko ih je pogođeno?',
         r'''<p>Uvjet „svi pogođeni” je presjek uvjeta, pa je prirodan alat uključivanje–isključivanje po skupu $P$ <em>promašenih</em> obveznih stupaca: $|(1)| = \sum_{P \subseteq [t]} (-1)^{|P|} N(P)$, gdje je $N(P)$ broj postavljanja koja izbjegavaju sve stupce iz $P$. Kako svaki obvezni stupac postoji u svakom od $k$ redaka ($t \le a_k$), redak $i$ ima točno $a_i - |P|$ dopuštenih polja, dakle $N(P) = \prod_{i=1}^k (a_i - |P|)$ ovisi samo o $|P|$.</p>'''),
        ('Zašto je zbroj po $2^t$ podskupova zapravo zbroj po $t + 1$ članova?',
         r'''<p>Jer $N(P)$ ovisi samo o $p = |P|$, a podskupova veličine $p$ ima $\binom{t}{p}$: $|(1)| = \sum_{p=0}^{t} (-1)^p \binom{t}{p} f(p)$ uz $f(x) = \prod_{i=1}^k (a_i - x)$. Ostaje izračunati vrijednosti jednog polinoma stupnja $k$ u $t + 1 \le k + 1$ točaka – to je klasična zadaća „polinom iz nultočaka + višetočkovna evaluacija”.</p>'''),
        ('Kako dobiti koeficijente $f$ i vrijednosti $f(0), \dots, f(t)$ brže od $O(k^2)$?',
         r'''<p>Koeficijenti: podijeli-pa-vladaj – množimo polinome $(a_i - x)$ u stablu, na svakoj razini ukupni stupanj je $k$, pa NTT množenje daje $O(k \log^2 k)$. Vrijednosti: višetočkovna evaluacija stablom podprodukata – u čvoru sa skupom točaka $S$ držimo $f \bmod \prod_{p \in S}(x - p)$ (ostatak čuva vrijednosti u tim točkama), spuštamo se do listova, gdje ostatak postaje konstanta $f(p)$. Polinomsko dijeljenje s ostatkom radi se preko inverza obrnutog polinoma (Newtonova iteracija), također NTT-om: $O(k \log^2 k)$.</p>'''),
        ('Koje sitnice odlučuju hoće li ovo proći?',
         r'''<p>Modul $998244353 = 119 \cdot 2^{23} + 1$ podržava NTT do duljine $2^{23}$ – dovoljno za stupnjeve $\le 2^{18}$. Predznak $(-1)^p$ u modularnoj aritmetici: oduzimaj pa dodaj $\text{MOD}$. Ako je $t = 0$ (npr. $k = n$), zbroj je samo $f(0) = \prod a_i$. Sve to napravi dvaput – za $a$ i za transponirani $b$ – i oduzmi $k!$. Ukupno $O(n \log^2 n)$, oko $2.5$ s za najveći ulaz uz ograničenje $10$ s.</p>'''),
    ],
    'tips': [
        r'''Uvjet „svaki od $t$ ciljeva pogođen”, gdje su ciljevi <em>simetrični</em> (svaki redak ih vidi jednako), gotovo uvijek vodi na $\sum_p (-1)^p \binom{t}{p} \cdot (\text{broj načina uz } p \text{ zabranjenih})$ – i time na vrijednosti jednog polinoma u točkama $0..t$.''',
        r'''Polinom zadan nultočkama $\prod (x - a_i)$ gradi se podijeli-pa-vladaj u $O(n \log^2 n)$; njegove vrijednosti u $n$ točaka daje višetočkovna evaluacija istom složenošću. Ta dva alata idu u standardnu biblioteku NTT-a uz inverz i dijeljenje polinoma.''',
        r'''Kad ubrzavaš točan $O(n^2)$ DP FFT-om, zadrži stari DP kao referentnu implementaciju za stress test – dva potpuno različita puta do istog broja najbolja su provjera i NTT-a i formule.''',
        r'''Provjeri veličinu NTT-a unaprijed: modul $998244353$ dopušta transformacije do $2^{23}$, a stupnjevi u stablu podprodukata nikad ne prelaze $2k$.''',
    ],
    'solution': r'''
<p>Nadogradnja rješenja prethodnog zadatka: imamo $k$ redaka s $a_1 \ge a_2 \ge \dots \ge a_k$ polja i tražimo broj načina da se u svaki redak stavi top tako da svaki od prvih $t$ stupaca ($t \le a_k$) sadrži barem jednog topa.</p>
<p>Primijenimo uključivanje–isključivanje po skupu stupaca među prvih $t$ koji sadrže topa. Odgovor je broj načina da se topovi postave proizvoljno, minus broj načina da stupac $i$ nije pokriven (za svaki $i$), plus broj načina da stupci $i$ i $j$ nisu pokriveni (za sve $i < j$), itd.</p>
<p>Budući da su stupci nerazlučivi, iteriramo samo po broju nepokrivenih stupaca $p$. Broj načina da zadanih $p$ stupaca ne sadrži topove je $(a_1 - p)(a_2 - p)\cdots(a_k - p)$, a broj načina odabira $p$ stupaca od prvih $t$ je $\binom{t}{p}$. Ukupno:</p>
$$\sum_{p=0}^{t} (-1)^p \binom{t}{p} (a_1 - p)(a_2 - p)\cdots(a_k - p).$$
<p>Neka je $f(x) = (a_1 - x)(a_2 - x)\cdots(a_k - x)$ polinom. Njegove koeficijente nalazimo u $O(k \log^2 k)$ metodom podijeli-pa-vladaj i FFT-om, a vrijednosti $f(0), f(1), \dots, f(t)$ u $O(k \log^2 k)$ višetočkovnom evaluacijom. Odgovor je tada $\sum_{p=0}^t (-1)^p \binom{t}{p} f(p)$.</p>
''',
    'detailed': r'''
<h3>1. Što ostaje iz zadatka D</h3>
<p>Obrnemo $a$ u nerastući poredak, $k = \max\{i : a_i \ge i\}$ je stranica najvećeg kvadrata i $r = k$ (dokaz u zadatku D). Broj postavljanja je $w = W(a, t) + W(b, t') - k!$, gdje je $b$ transponirani dijagram ($b_j = |\{i : a_i \ge j\}|$), $t = a_{k+1}$, $t' = b_{k+1}$, a</p>
<p>$W(a, t)$ = broj načina da se u svaki od redaka $1..k$ (širina $a_1 \ge \dots \ge a_k$) stavi točno jedan top tako da svaki od stupaca $1..t$ sadrži barem jednog topa.</p>
<p>Sve to je dokazano u D; jedino DP $f(i, j)$ s $O(k t)$ stanja treba zamijeniti, jer za $n < 2^{17}$ ima do $\sim 4 \cdot 10^9$ stanja.</p>
<h3>2. Uključivanje–isključivanje</h3>
<p>Za skup $P \subseteq \{1, \dots, t\}$ neka je $N(P)$ broj postavljanja (jedan top po retku, bez daljnjih uvjeta) u kojima nijedan top nije u stupcu iz $P$. Po načelu uključivanja–isključivanja broj postavljanja koja pogađaju <em>svaki</em> obvezni stupac je</p>
$$W(a, t) = \sum_{P \subseteq [t]} (-1)^{|P|} N(P).$$
<p>(Standardni dokaz: postavljanje koje promaši točno skup $M$ obveznih stupaca doprinosi $\sum_{P \subseteq M} (-1)^{|P|} = [M = \emptyset]$.)</p>
<p>Sada ključna činjenica iz D: $t = a_{k+1} \le k \le a_k \le a_i$ za sve $i \le k$, pa se svaki obvezni stupac nalazi u svakom od $k$ redaka. Ako redak $i$ ne smije koristiti $p = |P|$ stupaca, preostaje mu točno $a_i - p$ polja, neovisno o tome <em>koji</em> su stupci u $P$. Dakle</p>
$$N(P) = \prod_{i=1}^{k} (a_i - p), \qquad W(a, t) = \sum_{p=0}^{t} (-1)^p \binom{t}{p} \prod_{i=1}^{k} (a_i - p).$$
<p>Faktor $a_i - p$ je uvijek $\ge 0$ jer $p \le t \le a_i$. Za $t = 0$ (slučaj $k = n$) formula daje $\prod a_i$, kao i treba.</p>
<h3>3. Svođenje na polinom</h3>
<p>Definiramo $f(x) = \prod_{i=1}^{k} (a_i - x)$, polinom stupnja $k$ nad $\mathbb{Z}_{998244353}$. Tada je $\prod_i (a_i - p) = f(p)$, pa trebamo vrijednosti $f(0), f(1), \dots, f(t)$ i binomne koeficijente $\binom{t}{p}$ (faktorijeli i inverzni faktorijeli do $n$). Dva su podproblema:</p>
<ol>
<li><b>Koeficijenti $f$.</b> Podijeli-pa-vladaj: $\text{produkt}(l, r) = \text{produkt}(l, m) \cdot \text{produkt}(m + 1, r)$, listovi su $(a_i - x)$. Na svakoj od $\lceil \log_2 k \rceil$ razina ukupni stupanj je $k$, a množenje NTT-om košta $O(d \log d)$ za stupanj $d$, dakle $O(k \log^2 k)$.</li>
<li><b>Višetočkovna evaluacija.</b> Gradimo stablo podprodukata nad točkama $0, \dots, t$: čvor s točkama $S$ čuva $g_S(x) = \prod_{p \in S} (x - p)$. Spuštamo $f$ od korijena: u čvoru $S$ zamijenimo $f$ s $f \bmod g_S$ – to ne mijenja vrijednosti u točkama iz $S$ (jer $g_S(p) = 0$ za $p \in S$), a stupanj pada na $< |S|$. U listu $\{p\}$ ostatak je konstanta $f(p)$. Svaka razina radi dijeljenja ukupnog stupnja $O(t)$, pa je i to $O(t \log^2 t)$.</li>
</ol>
<p>Polinomski ostatak $f \bmod g$: neka je $n = \deg f$, $m = \deg g$. Obrnuti polinomi $\tilde f = x^n f(1/x)$, $\tilde g = x^m g(1/x)$; kvocijent $q$ se dobiva kao $\tilde q = \tilde f \cdot \tilde g^{-1} \bmod x^{n - m + 1}$ (inverz reda potencija Newtonovom iteracijom $r \leftarrow r(2 - r\tilde g)$), a ostatak je $f - qg$ odsječen na stupanj $< m$. Sve operacije su NTT množenja, $O((n + m) \log)$.</p>
<h3>4. Algoritam</h3>
<ol>
<li>Obrni $a$; izračunaj $k$, $t = a_{k+1}$, transponirani $b$ i $t' = b_{k+1}$ ($O(n)$).</li>
<li>Faktorijeli i inverzni faktorijeli do $n + 1$.</li>
<li>$W(a, t)$: $f = \prod_{i \le k}(a_i - x)$ D&amp;C-om; $v_p = f(p)$ za $p = 0..t$ višetočkovnom evaluacijom; zbroj $\sum (-1)^p \binom{t}{p} v_p$.</li>
<li>Isto za $(b, t')$; ispiši $k$ i $(W(a,t) + W(b,t') - k!) \bmod 998244353$.</li>
</ol>
<h3>5. Složenost</h3>
<p>$O(n \log^2 n)$ vremena: D&amp;C produkt i višetočkovna evaluacija imaju po $O(\log n)$ razina s ukupnim NTT radom $O(n \log n)$ po razini; ostatak (Newtonov inverz) ima istu asimptotiku s većom konstantom. Memorija $O(n \log n)$ za stablo podprodukata (ukupni stupanj po razini $\le 2t$). Na najvećem testu ($n = 2^{17} - 1$, $k = t = n - 1$) rješenje radi oko $2.5$ s uz ograničenje $10$ s.</p>
<h3>6. Zamke</h3>
<ul>
<li>Vodeći koeficijent $f$ je $(-1)^k$, tj. $\text{MOD} - 1$ za neparan $k$ – sve drži u $[0, \text{MOD})$ i nakon svakog oduzimanja dodaj $\text{MOD}$.</li>
<li>U evaluaciji dijeli samo kad je $\deg f \ge \deg g_S$; inače proslijedi $f$ nepromijenjen (ostatak je već „mali”). Prazan ostatak tretiraj kao $0$.</li>
<li>Broj točaka je $t + 1 \le n$, ali pazi na $t = 0$: stablo s jednim listom i zbroj s jednim članom.</li>
<li>NTT duljina mora biti potencija dvojke veća od zbroja stupnjeva; modul $998244353$ ima primitivni korijen $3$ i podržava duljine do $2^{23}$.</li>
<li>Rekurzija D&amp;C i stabla podprodukata ima dubinu $O(\log n)$ – nema opasnosti za stog; velike privremene polinome ipak ne alociraj nepotrebno (koristi <code>resize</code> na točnu potrebnu duljinu).</li>
</ul>
<h3>7. Primjer</h3>
<p>$a = (1, 2, 3)$ (obrnuto $(3, 2, 1)$): $k = 2$, $t = 1$, $f(x) = (3 - x)(2 - x)$, $f(0) = 6$, $f(1) = 2$; $W = \binom{1}{0} \cdot 6 - \binom{1}{1} \cdot 2 = 4$ – točno vrijednost DP-a iz zadatka D. Transponirani dijagram je isti, pa je $w = 4 + 4 - 2 = 6$.</p>
''',
    'verified': r'''uzorak 1/1; 300 slučajnih testova ($n \le 60$, svaki četvrti $n \in [200, 400]$) protiv neovisne $O(n^2)$ DP implementacije iz zadatka D (koja je sama provjerena pravim brute forceom); veliki testovi s $n = 2^{17} - 1$ (generator ima četiri oblika: slučajni, dva stupnjevita te $k = t = n - 1$; standardni prolaz koristi 3, sva četiri pokrenuta zasebno), najviše $2.49$ s uz ograničenje $10$ s.''',
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
        ('Što jedan pritisak tipke geometrijski može, a što ne može?',
         r'''<p>Držanje tipke $c$ pomiče boju po dužini od trenutne točke $p$ prema vrhu $c$ kocke $[0, 255]^3$, brzinom $1$, i staje najkasnije u $c$. Dakle jednim pritiskom dosežemo točno točke dužine $[p, c]$ – ništa izvan tih $8$ dužina. Obratno: ako je cilj $x$ na dužini $[p, c]$, pritisak $c$ u trajanju $|x - p|$ pogađa ga <em>točno</em>. Zadatak je stoga: prikaži cilj kao kraj lanca od najviše $10$ dužina prema vrhovima, s početkom u crnoj.</p>'''),
        ('Koje su točke „lake”, i kako mjeriti koliko je točka daleko od lakih?',
         r'''<p>Vrhovi kocke su najlakši (jedan pritisak iz crne). Točke na bridu su sljedeće: brid spaja dva vrha $a, b$, pa idemo u $a$ i zatim prema $b$ i stanemo. Prirodna mjera je <em>rang</em> $f(p)$ = broj koordinata koje nisu ni $0$ ni $255$: vrh ima rang $0$, brid rang $1$, ploha rang $2$, unutrašnjost rang $3$. Cilj je smanjivati rang.</p>'''),
        ('Kako iz točke ranga $r$ doći do točke manjeg ranga na kojoj možemo „stati na vrijeme”?',
         r'''<p>Obrnimo smjer razmišljanja: zadnji pritisak dovodi u $p$ iz neke točke $q$ krećući se prema vrhu $v$, pa $p$ leži na dužini $[q, v]$, tj. $q$ je na polupravcu iz $v$ kroz $p$, iza $p$. Ako $v$ odaberemo tako da se s $p$ slaže u svim rubnim koordinatama, polupravac ostaje unutar iste plohe/brida kao $p$, a produljimo li ga do prvog trenutka kad neka slobodna koordinata dosegne $0$ ili $255$, dobivamo $q$ u kocki sa strogo manjim rangom. Rekurzivno dođemo do $q$, pa pritisnemo $v$ točno $|q - p|$ sekundi.</p>'''),
        ('Zašto je najviše $4$ pritiska i kako računati presjek s rubom?',
         r'''<p>Rang pada barem za $1$ po koraku, a rang $0$ košta jedan pritisak: $\le 1 + 3 = 4$. Konkretno, biramo $v_i = p_i$ za rubne, $v_i = 0$ za slobodne koordinate; tada je $p - v$ pozitivan samo na slobodnim koordinatama, pa je $q = v + s(p - v)$ sa $s = \min_{\text{slobodni } i} 255 / p_i > 1$ – koordinata koja postiže minimum postane točno $255$. Sve je $O(1)$ po testu; treba paziti samo na numeriku (zalijepi koordinatu na $255$ i ispiši trajanja s dovoljno decimala).</p>'''),
    ],
    'tips': [
        r'''Konstruktivne zadatke s „potezima” često je najlakše graditi <strong>unatrag</strong>: pitaj se iz kojih stanja jedan potez pogađa cilj točno, i među njima nađi ono koje je „jednostavnije” po nekoj mjeri (ovdje rang).''',
        r'''Definiraj potencijal koji se svakim korakom strogo smanjuje (broj slobodnih koordinata) – time ujedno dobivaš gornju granicu broja poteza, koju odmah možeš usporediti s dopuštenih $10$.''',
        r'''Kod polupravca iz vrha kocke kroz točku, presjek s rubom je uvijek na koordinati koja prva dosegne granicu: $s = \min_i 255 / p_i$ kad su slobodne koordinate vrha jednake $0$. Nema potrebe za općom geometrijom presjeka.''',
        r'''Za zadatke s tolerancijom $10^{-6}$ napiši vlastiti checker koji doslovno simulira postupak; on otkriva i greške u konstrukciji i greške u ispisu (premalo decimala, krivi redoslijed).''',
    ],
    'solution': r'''
<p>Definirajmo rang $f(p)$ točke $p = (r, g, b)$ kao broj njezinih koordinata različitih i od $0$ i od $255$.</p>
<p>Ako je $f(p) = 0$, $p$ je jedna od osnovnih boja i do nje idemo jednim potezom.</p>
<p>Ako je $f(p) = 1$, $p$ leži na bridu između dviju osnovnih boja $a$ i $b$: idi u $a$, zatim se kreni prema $b$ i stani u pravom trenutku.</p>
<p>Ako je $f(p) = 2$, $p$ leži unutar plohe kocke. Odaberi bilo koji vrh $v$ te plohe, povuci polupravac iz $v$ kroz $p$ i nađi gdje siječe brid kocke. Točka presjeka ima rang $0$ ili $1$, pa najprije dođi do nje kako je opisano, a zatim se iz nje kreni prema $v$ i stani u $p$.</p>
<p>Ako je $f(p) = 3$, $p$ je strogo unutar kocke. Odaberi bilo koji vrh $v$ kocke, povuci polupravac iz $v$ kroz $p$ i nađi gdje siječe plohu kocke. Točka presjeka ima rang $0$, $1$ ili $2$, pa najprije dođi do nje kako je opisano, a zatim se iz nje kreni prema $v$ i stani u $p$.</p>
''',
    'detailed': r'''
<h3>1. Model poteza</h3>
<p>Boja je točka $p \in K = [0, 255]^3$, a $8$ tipki su vrhovi kocke $K$ (sve kombinacije koordinata $0/255$). Držanje tipke $c$ tijekom $d$ sekundi pomiče $p$ po dužini prema $c$ brzinom $1$: nova točka je $p + \min(d, |c - p|) \cdot \frac{c - p}{|c - p|}$. Dva jednostavna, ali ključna zaključka:</p>
<ul>
<li>jednim pritiskom iz $p$ dosežemo <em>točno</em> točke dužina $[p, c]$ za $c$ vrh – ništa drugo;</li>
<li>ako je cilj $x \in [p, c]$, pritisak $c$ u trajanju $d = |x - p|$ pogađa $x$ egzaktno (ne dolazi do zaustavljanja u $c$ jer $|x - p| \le |c - p|$).</li>
</ul>
<p>Dopušteno je najviše $10$ pritisaka; pokazat ćemo da su uvijek dovoljna $4$.</p>
<h3>2. Rang točke</h3>
<p>Koordinatu nazovimo <em>rubnom</em> ako je $0$ ili $255$, inače <em>slobodnom</em>. Rang $f(p)$ je broj slobodnih koordinata: $f = 0$ za vrhove, $f = 1$ za točke na bridovima (bez vrhova), $f = 2$ za točke unutar ploha, $f = 3$ za unutrašnjost kocke. Rubne koordinate točke određuju najmanju plohu/brid kocke koja je sadrži.</p>
<h3>3. Korak smanjenja ranga</h3>
<p><b>Lema.</b> Neka je $f(p) \ge 1$. Neka je $v$ vrh kocke koji se s $p$ podudara u svim rubnim koordinatama, a u slobodnima ima $0$. Definiramo $s = \min_{i \text{ slobodna}} 255 / p_i$ i $q = v + s(p - v)$. Tada: (a) $q \in K$, (b) $f(q) \le f(p) - 1$, (c) $p \in [q, v]$ i $|q - p| < |q - v|$.</p>
<p><i>Dokaz.</i> Vektor $p - v$ ima nulu na rubnim koordinatama i $p_i \in (0, 255)$ na slobodnima, pa je $s > 1$ (jer $p_i < 255$). (a) Rubne koordinate $q$ jednake su onima od $p$; slobodne su $s p_i \le \frac{255}{p_i} p_i = 255$ i $> 0$. (b) Za koordinatu $i^*$ koja postiže minimum vrijedi $q_{i^*} = 255$ – postala je rubna, a rubne ostaju rubne. (c) $p = v + 1 \cdot (p - v)$, $q = v + s(p - v)$, $0 < 1 < s$, pa je $p$ između $v$ i $q$ i $|q - p| = (s - 1)|p - v| < s|p - v| = |q - v|$. $\square$</p>
<p>Posljedica: ako lampu dovedemo u $q$ i zatim držimo tipku $v$ točno $|q - p|$ sekundi, završavamo točno u $p$.</p>
<h3>4. Algoritam</h3>
<p>Rekurzivna funkcija $\text{rijesi}(p)$:</p>
<ol>
<li>Ako je $f(p) = 0$: $p$ je vrh; ako je $p \ne (0,0,0)$, dodaj potez $(p, |p|)$ (iz crne ravno u vrh); za crnu nije potreban nijedan potez.</li>
<li>Inače izračunaj $v$, $s$, $q$ kao u Lemi; zbog numerike koordinatu $q_{i^*}$ eksplicitno postavi na $255$ (izračun $255 / p_i \cdot p_i$ u pomičnom zarezu ne mora dati točno $255$). Pozovi $\text{rijesi}(q)$, pa dodaj potez $(v, |q - p|)$.</li>
</ol>
<p>Broj poteza: rang se svakim korakom smanjuje bar za $1$, dakle najviše $3$ rekurzivna koraka plus $1$ za vrh: $\le f(p) + 1 \le 4$ poteza. (Lanac nikad ne završi u crnoj osim za $p = (0,0,0)$, jer svaki $q$ ima koordinatu $255$.)</p>
<h3>5. Točnost i numerika</h3>
<p>Svaki potez je egzaktan u realnoj aritmetici; u <code>long double</code> greška je reda $10^{-15}$ po koraku, a ispisujemo trajanja s $12$ decimala, što daje ukupnu grešku daleko ispod tražene tolerancije $10^{-6}$. Jedina „opasna” operacija je odluka je li koordinata rubna – zato se $q_{i^*}$ eksplicitno zalijepi na $255$, a rubne koordinate od $p$ kopiraju bez računanja. Ulazne točke su cjelobrojne, pa se rubnost ulaza provjerava egzaktno.</p>
<h3>6. Složenost</h3>
<p>$O(1)$ po testu (najviše $4$ poteza, konstantan broj aritmetičkih operacija); $10^4$ testova je trivijalno.</p>
<h3>7. Primjeri</h3>
<ul>
<li>$p = (174, 174, 174)$, rang $3$: $v = (0,0,0)$, $s = 255/174$, $q = (255, 255, 255)$ – rang $0$. Potezi: $(255,255,255)$ u trajanju $255\sqrt{3} \approx 441.67$, pa $(0,0,0)$ u trajanju $|q - p| = 81\sqrt{3} \approx 140.30$. Dva poteza.</li>
<li>$p = (105, 255, 175)$, rang $2$: $v = (0, 255, 0)$, $s = \min(255/105, 255/175) = 255/175$, $q = (153, 255, 255)$ – rang $1$. Za $q$: $v' = (0, 255, 255)$, $s' = 255/153$, $q' = (255, 255, 255)$. Potezi: $(255,255,255)$ do vrha, $(0,255,255)$ u trajanju $|q' - q| = 102$, $(0,255,0)$ u trajanju $|q - p| = \sqrt{48^2 + 80^2} \approx 93.30$. Tri poteza.</li>
<li>$p = (0,0,0)$: nula poteza (dopušten je i ispis $0$).</li>
</ul>
''',
    'verified': r'''uzorak 1/1 (usporedba preko checkera koji simulira poteze i zahtijeva udaljenost $\le 10^{-6}$); 300 slučajnih testova (do $200$ boja po testu, s naglaskom na rubne vrijednosti $0, 1, 127, 128, 254, 255$) i 3 velika testa s $10^4$ boja, svi provjereni checkerom; dodatno mreža od $32^3 = 32768$ boja (sve kombinacije $32$ odabranih vrijednosti uključujući $0, 1, 2, 127, 128, 253, 254, 255$) – sve prošle, najviše $4$ poteza.''',
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
        ('Što uvjet „$S$ i $V \setminus S$ oba dominiraju” zapravo znači za pojedini vrh?',
         r'''<p>Vrh $v \in S$ je dominiran od $S$ automatski (sam je u $S$), pa je uvjet za njega da ima susjeda u $V \setminus S$; simetrično za $v \notin S$. Dakle: obojimo vrhove u dvije boje tako da <em>svaki vrh ima susjeda suprotne boje</em>, uz $|S| = \lfloor n/2 \rfloor$. To je u literaturi „even adjacency split” (EAS). Bez uvjeta na veličinu lako je (2-bojenje BFS-stabla po parnosti dubine); sav problem je balans.</p>'''),
        ('Koji su vrhovi prisilni i zašto je ograničenje „najviše dva lista po vrhu” prirodno?',
         r'''<p>List $\ell$ s jedinim susjedom $u$ mora biti suprotne boje od $u$. Ako $u$ ima tri lista, sva tri su iste boje, suprotne od $u$: zvijezda $K_{1,3}$ nema EAS ($4$ vrha, a jedina valjana podjela je $1 : 3$). Općenito, mnogo listova na jednom vrhu ruši balans – zato je uvjet zadatka točno onaj pod kojim članak Chestona i dr. dokazuje da EAS uvijek postoji (za grafove bez izoliranih vrhova) i daje linearni algoritam.</p>'''),
        ('Možemo li graditi podjelu postupno i brisati obrađene vrhove, a da ništa ne „pukne”?',
         r'''<p>Da, ako čuvamo dvije invarijante: (1) $\big||V_1| - |V_2|\big| \le 1$ i (2) svaki već raspoređeni vrh ima susjeda u suprotnom skupu <em>među već raspoređenima</em>. Raspoređeni vrh brišemo iz grafa – njegov je uvjet trajno zadovoljen. Opasnost: brisanjem vrha njegovi susjedi gube stupanj; novi list treba pamtiti tip – je li mu brid izbrisan prema $V_1$ ili $V_2$ – jer time već ima susjeda u tom skupu i nije više „prisilan” u odnosu na svog preostalog susjeda.</p>'''),
        ('Kojim redom obrađivati vrhove da svaki korak sačuva obje invarijante?',
         r'''<p>Prioritet: (a) ako neki vrh $x$ ima $\ge 3$ susjedna lista („trojka”, moguće samo zbog brisanja), riješi ga odmah – rasporedi $x$ i sve njegove listove; (b) inače ako postoji list $x$ sa susjedom $w$: $w$ ima najviše još jedan list $z$, stavimo $x, z$ u manji skup i $w$ u drugi (razlika ostaje $\le 1$); (c) inače nema listova – uzmi bilo koji brid $xy$, $x \to V_1$, $y \to V_2$. U svakom slučaju raspoređeni vrhovi imaju susjeda preko puta, a brišemo ih zajedno, pa se broj raspoređenih strogo povećava.</p>'''),
        ('Kako riješiti trojku – vrh s tri ili više listova – a zadržati razliku $\le 1$?',
         r'''<p>Ključno: najviše dva lista su izvorni (tip $0$); ostali su nastali brisanjem i već imaju susjeda u $V_1$ (tip $1$) ili $V_2$ (tip $2$). Stavimo $x$ u, recimo, $V_2$: tada listovi tipa $0$ i $2$ <em>moraju</em> u $V_1$, a listovi tipa $1$ su slobodni i njima balansiramo. Stranu za $x$ biramo prema tome kojih je slobodnih listova više; kad je $\#1 = \#2$, odlučuju $\#0$ i trenutna razlika. Analiza slučajeva u detaljnom rješenju pokazuje da razlika uvijek ostane $\le 1$.</p>'''),
        ('Kako sve to izvesti u $O(n + m)$?',
         r'''<p>Čuvamo stupnjeve, oznaku „živ”, tip lista, broj susjednih listova i dvije liste kandidata (listovi, trojke) s lijenom provjerom valjanosti pri vađenju. Brisanje vrha $x$ obilazi njegove bridove jednom; svaki brid se obriše najviše jednom, pa je ukupno $O(n + m)$.</p>'''),
    ],
    'tips': [
        r'''„$S$ i $V \setminus S$ oba dominirajuća” = „svaki vrh ima susjeda suprotne boje”. Prepoznaj tu preformulaciju odmah – s njom su listovi očito prisilni, a zvijezda $K_{1,3}$ odmah pokazuje zašto zadatak ograničava broj listova po vrhu.''',
        r'''Kod postupnih konstrukcija s brisanjem vrhova, uvjet koji brisani vrh već ispunjava treba biti <strong>trajno</strong> ispunjen (ovisi samo o već raspoređenim vrhovima). Formuliraj invarijante eksplicitno i za svaki tip koraka provjeri obje.''',
        r'''Kada je brute force nemoguć (odgovor nije jedinstven), napiši checker koji provjerava <em>definiciju</em> (veličina, različitost vrhova, uvjet dominacije) i iscrpno prođi sve male grafove – za ovakve algoritme s puno slučajeva to nalazi greške koje nasumični testovi promaše.''',
        r'''Ako službeno rješenje upućuje na članak, potraži u njemu odjeljak s pseudokodom i <em>dokazom invarijanti</em>, i implementiraj točno taj algoritam – vlastite „pojednostavljene” varijante takvih slučajnih analiza često propuštaju neki slučaj.''',
    ],
    'solution': r'''
<p>Službeno rješenje glasi: vidi članak <em>„The even adjacency split problem for graphs”</em>, odjeljak 3.</p>
<p>Napomena prevoditelja: službeni tutorial ne sadrži daljnji opis algoritma — cjelovita konstrukcija (podjela vrhova povezanog grafa na dvije strane jednake veličine tako da svaki vrh ima susjeda na drugoj strani, uz pretpostavku o najviše dva susjedna lista) nalazi se u navedenom članku. Algoritam iz članka (G. A. Cheston, S. T. Hedetniemi, A. L. Liestman, D. Stehman, <em>Discrete Applied Mathematics</em> 102 (2000)) opisan je i dokazan u detaljnom rješenju.</p>
''',
    'detailed': r'''
<h3>1. Preformulacija</h3>
<p>Vrh $v \in S$ je u $S$ pa ga $S$ dominira; $V \setminus S$ ga dominira ako i samo ako ima susjeda izvan $S$. Simetrično za $v \notin S$. Dakle tražimo particiju $V = V_1 \cup V_2$ ($S = V_1$ ili $V_2$) takvu da</p>
<ul>
<li>svaki vrh iz $V_1$ ima susjeda u $V_2$ i svaki vrh iz $V_2$ ima susjeda u $V_1$ (<em>adjacency split</em>),</li>
<li>$\big||V_1| - |V_2|\big| \le 1$ (<em>even</em>); tada jedan od skupova ima točno $\lfloor n/2 \rfloor$ elemenata.</li>
</ul>
<p>Članak Chestona, Hedetniemija, Liestmana i Stehmana pokazuje da je opći problem NP-težak, ali da za grafove bez izoliranih vrhova u kojima nijedan vrh nema više od dva susjedna lista EAS uvijek postoji i može se naći u $O(n + m)$. Zadatak jamči povezanost ($n \ge 2$, dakle nema izoliranih vrhova) i uvjet o listovima – upravo pretpostavke tog teorema.</p>
<h3>2. Zašto su listovi problem</h3>
<p>List $\ell$ ima jednog susjeda $u$, pa je uvjet za $\ell$ točno „$\ell$ i $u$ su na različitim stranama”. Vrh s $r$ listova ima svih $r$ listova na istoj strani, suprotnoj od svoje. Za zvijezdu $K_{1,3}$ to daje podjelu $1 : 3$, pa EAS ne postoji – uvjet „najviše dva lista” nije slučajan. S druge strane, bez uvjeta na veličine adjacency split postoji uvijek (2-bojenje razapinjućeg stabla po parnosti dubine: svaki vrh ima roditelja ili dijete suprotne boje); teškoća je istodobno postići balans.</p>
<h3>3. Ideja algoritma: raspoređuj i briši</h3>
<p>Vrhove postupno stavljamo u $V_1$ ili $V_2$ i <em>brišemo ih iz grafa</em>, čuvajući nakon svakog koraka dvije invarijante:</p>
<ol>
<li>$\big||V_1| - |V_2|\big| \le 1$;</li>
<li>svaki raspoređeni vrh ima raspoređenog susjeda u suprotnom skupu.</li>
</ol>
<p>Invarijanta (2) je „trajna”: brisanje kasnijih vrhova ne može je pokvariti. Kad graf postane prazan, $(V_1, V_2)$ je EAS. Brisanje, međutim, mijenja preostali graf: stupnjevi padaju, nastaju novi listovi, čak i vrhovi s $3$ i više susjednih listova. Zato svakom listu $u$ u tekućem grafu pridružujemo <em>tip</em>:</p>
<ul>
<li>$\text{tip}(u) = 0$ – $u$ je list već u izvornom grafu;</li>
<li>$\text{tip}(u) = 1$ (odn. $2$) – $u$ je postao list brisanjem brida do vrha koji je stavljen u $V_1$ (odn. $V_2$).</li>
</ul>
<p>List tipa $1$ već ima susjeda u $V_1$: ako ga stavimo u $V_2$, uvjet (2) za njega vrijedi bez obzira na to kamo ide njegov preostali susjed. Ta „sloboda” je ključ balansiranja. Uočimo i da vrh ima najviše dva susjedna lista tipa $0$ (uvjet zadatka), dok listova tipa $1/2$ može imati proizvoljno mnogo.</p>
<p>Održavamo: stupanj svakog živog vrha, broj susjednih (živih) listova, skup <em>Listovi</em> i skup <em>Trojke</em> (živi vrhovi s $\ge 3$ susjedna lista).</p>
<h3>4. Tri operacije</h3>
<p><b>Prune($x$)</b> – obriši $x$ i sve njegove bridove. Za svakog živog susjeda $u$: smanji stupanj; ako je $x$ bio list, smanji broj listova susjednih $u$-u. Ako $u$ postane list: $\text{tip}(u) \leftarrow$ skup u koji je stavljen $x$, dodaj $u$ u Listovi, i uvećaj broj listova njegova preostalog susjeda $z$ (ako dosegne $3$, $z$ ide u Trojke). Ako $u$ postane izoliran, a nije raspoređen, stavi ga u manji skup i obriši.</p>
<p><b>Glavna petlja</b> dok graf nije prazan:</p>
<ol>
<li>ako Trojke $\ne \emptyset$: uzmi $x \in$ Trojke, <b>RecoverTriple($x$)</b>;</li>
<li>inače ako Listovi $\ne \emptyset$: uzmi list $x$, <b>RecoverEndvertex($x$)</b>;</li>
<li>inače uzmi bilo koji živi vrh $x$ i bilo kojeg njegova susjeda $y$; $x \to V_1$, $y \to V_2$; Prune($x$), Prune($y$).</li>
</ol>
<p><b>RecoverEndvertex($x$)</b>: neka je $w$ jedini susjed lista $x$. Budući da Trojke $= \emptyset$, $w$ ima najviše još jedan susjedni list $z$. Stavi $x$ (i $z$, ako postoji) u <em>manji</em> od $V_1, V_2$, a $w$ u drugi; Prune($w$) (time nestaju i $x$, $z$).</p>
<p><b>RecoverTriple($x$)</b>: neka je $\#0, \#1, \#2$ broj susjednih listova tipa $0, 1, 2$. Ako je
$\#1 > \#2$, ili $\#1 = \#2$ i ( $\#0 = 0$ i $|V_1| = |V_2| + 1$, ili $\#0 = 2$ i $|V_1| = |V_2| - 1$ ), stavi $x \to V_2$, listove tipa $0$ i $2$ u $V_1$, a listove tipa $1$ raspodijeli tako da razlika ostane $\le 1$ (redom u trenutno manji skup). Inače simetrično: $x \to V_1$, tipovi $0$ i $1$ u $V_2$, tip $2$ balansira. Zatim Prune($x$).</p>
<h3>5. Dokaz invarijanti</h3>
<p><i>Korak 3 (nema listova).</i> $x$ i $y$ su susjedi u suprotnim skupovima – (2) vrijedi, a (1) jer su dodana po jedan u svaki. Može li Prune izolirati neraspoređen vrh $w$? Samo ako je $\deg w = 2$ i $w$ je susjed i $x$-u i $y$-u (u trenutku koraka nema listova, pa je $\deg w \ge 2$). Takav $w$ ima susjeda u oba skupa, pa ga slobodno stavljamo u manji – obje invarijante vrijede.</p>
<p><i>RecoverEndvertex.</i> $x$ (i $z$) suprotne su strane od $w$, njihova jedinog susjeda – (2) za $x, z$; $w$ ima $x$ preko puta – (2) za $w$. Za (1): ako u manji skup idu dva vrha i u veći jedan, razlika se mijenja za $\pm 1$ oko početne, pa ostaje $\le 1$ (ako je bila $0$, postaje $1$; ako je bila $1$ u korist većeg, postaje $0$). S jednim listom razlika se ne mijenja. U Prune($w$) izolirani vrhovi su samo $x, z$, već raspoređeni.</p>
<p><i>RecoverTriple, slučaj $x \to V_2$.</i> Uvjet (2): listovi tipa $0$ i $2$ u $V_1$ imaju $x \in V_2$ preko puta; listovi tipa $1$ već imaju susjeda u $V_1$ ako idu u $V_2$, a ako idu u $V_1$ imaju $x$; $x$ ima susjeda u $V_1$ jer je bar jedan list otišao u $V_1$: ako je $\#0 + \#2 \ge 1$ prisilno, a ako je $\#0 + \#2 = 0$ onda je $\#1 \ge 3$ i slobodni listovi idu redom u trenutno manji skup – nakon što je $x$ ušao u $V_2$, skup $V_1$ nije veći od $V_2$ (prije koraka razlika je bila $\le 1$), pa već prvi slobodni list ide u $V_1$. Uvjet (1): u $V_1$ prisilno ide $\#0 + \#2$ vrhova, u $V_2$ prisilno $1$ ($x$), a $\#1$ vrhova je slobodno.</p>
<p>Označimo $d = |V_1| - |V_2| \in \{-1, 0, 1\}$ prije koraka i $D$ razliku nakon prisilnih smještanja. Slobodne listove stavljamo redom u trenutno manji skup: dok je $|D| \ge 2$ svaki smanjuje $|D|$ za $1$, a kad je $|D| \le 1$ takvom ostaje. Zato je završna razlika $\le 1$ točno kad je broj slobodnih listova $\ge |D| - 1$.</p>
<ul>
<li>$\#1 > \#2$ (grana $x \to V_2$): $D = d + \#0 + \#2 - 1 \le 1 + 2 + \#2 - 1 = \#2 + 2 \le \#1 + 1$, a $D \ge -1 - 1 = -2$ i $\#1 \ge 1$; u oba smjera $\#1 \ge |D| - 1$.</li>
<li>$\#1 = \#2 = c$, $\#0 = 0$, $d = 1$ (grana $x \to V_2$): $D = 1 + c - 1 = c$, slobodnih $c \ge c - 1$.</li>
<li>$\#1 = \#2 = c$, $\#0 = 2$, $d = -1$ (grana $x \to V_2$): $D = -1 + c + 2 - 1 = c$, slobodnih $c$.</li>
<li>$\#2 > \#1$ (grana $x \to V_1$): simetrično prvom slučaju.</li>
<li>$\#1 = \#2 = c$, ostali slučajevi (grana $x \to V_1$): prisilno u $V_2$ ide $\#0 + c$, u $V_1$ ide $x$, pa $D = d + 1 - \#0 - c$. Gornja granica $D \le 2 - c \le c + 1$ jer je $c \ge 1$ (trojka ima $\ge 3$ lista, a $\#0 \le 2$). Donja granica $D \ge -c - 1$ traži $\#0 \le d + 2$, što ne vrijedi jedino za $\#0 = 2$, $d = -1$ – a to je upravo slučaj koji smo poslali u granu $x \to V_2$.</li>
</ul>
<p>Time je uvjet (1) sačuvan u svim slučajevima. Prune($x$) izolira samo listove, već raspoređene. Svaki korak rasporedi bar jedan vrh, pa algoritam završava; graf bez izoliranih vrhova jamči da u koraku 3 susjed $y$ postoji.</p>
<h3>6. Složenost i implementacija</h3>
<p>Svaki brid se briše najviše jednom (pri Prune jednog od krajeva), a sve ostale operacije su $O(1)$ po vrhu; Listovi i Trojke držimo kao stogove s lijenom provjerom valjanosti (vrh se pri vađenju preskoči ako više nije živ list, odn. nema $\ge 3$ listova). Ukupno $O(n + m)$ po testu, što uz sume $\sum n \le 2 \cdot 10^5$, $\sum m \le 5 \cdot 10^5$ prolazi trenutno.</p>
<p>Zamke:</p>
<ul>
<li>u Prune($x$) zapamti <em>prije</em> brisanja je li $x$ bio list – tada svakom susjedu treba smanjiti brojač susjednih listova;</li>
<li>jedinog živog susjeda novog lista $u$ nalazimo linearnim prolazom kroz listu susjedstva; vrh postaje list najviše jednom, pa je to ukupno $O(\sum \deg) = O(m)$;</li>
<li>vrh koji postane izoliran <em>i već je raspoređen</em> samo se obriše – ne smije se drugi put stavljati u skup;</li>
<li>u koraku 3 susjed $y$ mora biti živ – traži ga u listi susjedstva preskačući obrisane;</li>
<li>na kraju ispiši onaj od $V_1, V_2$ koji ima točno $\lfloor n/2 \rfloor$ elemenata (za paran $n$ oba; za neparan točno jedan).</li>
</ul>
<h3>7. Primjer</h3>
<p>Put $1 - 2 - 3$: listovi $1, 3$ (tip $0$), nema trojki. RecoverEndvertex($1$): $w = 2$ ima još list $z = 3$; $1, 3 \to V_1$, $2 \to V_2$. Graf prazan; $|V_2| = 1 = \lfloor 3/2 \rfloor$, pa $S = \{2\}$. </p>
<p>Uzorak s dva trokuta $\{1,2,3\}$, $\{4,5,6\}$ spojena bridom $3 - 4$ ($n = 6$): nema listova ni trojki, pa korak 3 uzima brid $1 - 2$: $1 \to V_1$, $2 \to V_2$. Prune($1$): vrh $2$ postaje list tipa $1$, ali se odmah briše u Prune($2$), pri čemu $3$ postaje list tipa $2$ (obrisan brid $2 - 3$ vodi u $V_2$) s jedinim susjedom $4$. RecoverEndvertex($3$): $w = 4$ nema drugih listova; skupovi su jednaki pa $3 \to V_1$, $4 \to V_2$; Prune($4$) čini $5$ i $6$ listovima tipa $2$ (susjedi jedan drugome). RecoverEndvertex($6$): $w = 5$, $6 \to V_1$, $5 \to V_2$. Rezultat $V_1 = \{1, 3, 6\}$, $V_2 = \{2, 4, 5\}$; provjera: $1 \leftrightarrow 2$, $3 \leftrightarrow 2$, $4 \leftrightarrow 3$, $5 \leftrightarrow 6$ – svaki vrh ima susjeda preko puta, $|V_1| = 3$, pa ispisujemo $S = \{1, 3, 6\}$.</p>
''',
    'verified': r'''uzorak 1/1 (checker: $|S| = \lfloor n/2 \rfloor$, različiti vrhovi, $S$ i $V \setminus S$ oba dominirajuća); 300 slučajnih testova (do $15$ povezanih grafova s $n \le 14$ po testu: slučajna stabla s dodatnim bridovima, gusjenice, putevi, ciklusi, „čvorišta” s po dva lista) i 3 velika testa ($n = 2 \cdot 10^5$, $m$ do $5 \cdot 10^5$; te $10^4$ malih grafova) provjereni checkerom; dodatno iscrpno svi povezani grafovi s $2 \le n \le 7$ vrhova koji zadovoljavaju uvjet o listovima ($1\,889\,294$ grafova) – svi prošli checker.''',
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
        ('Kako prikazati relaciju „dijele $x$ ili dijele $y$” tako da postane graf koji poznajemo?',
         r'''<p>Umjesto točaka kao vrhova (graf prijateljstva bio bi unija klika po pravcima – nezgodan), uzmimo <em>koordinate</em> za vrhove: po jedan vrh za svaku različitu $x$-vrijednost i za svaku $y$-vrijednost, a točka $(x_i, y_i)$ je brid između njih. Graf je bipartitan, bez višestrukih bridova (točke su različite), a dvije točke su prijateljske točno kad njihovi bridovi dijele vrh. Traži se: rastaviti što više bridova u parove susjednih bridova.</p>'''),
        ('Koja je očita gornja granica i može li se uvijek postići?',
         r'''<p>Par susjednih bridova leži u istoj komponenti, pa komponenta s $m_c$ bridova daje najviše $\lfloor m_c/2 \rfloor$ parova. Tvrdnja: ta se granica <em>uvijek</em> postiže – u povezanom grafu s $m$ bridova postoji rastav na $\lfloor m/2 \rfloor$ parova susjednih bridova (plus jedan brid viška ako je $m$ neparan). Preostali nespareni bridovi iz raznih komponenata sparuju se proizvoljno (neprijateljski).</p>'''),
        ('Koja struktura na grafu jamči da svaki brid ima „vrh u kojem ćemo ga obraditi”?',
         r'''<p>DFS-stablo. U neusmjerenom grafu svaki nestablasti brid spaja pretka i potomka (nema poprečnih bridova). Zato svakom bridu možemo dodijeliti <em>gornji</em> kraj: stablastom bridu roditelja, povratnom bridu pretka. Ideja: obrađuj vrhove od listova prema korijenu; u vrhu $v$ sparuj bridove koji su „ostali” $v$-u – svi imaju $v$ kao zajednički kraj, pa je svaki njihov par prijateljski.</p>'''),
        ('Što točno vrh $v$ sparuje i što ostavlja roditelju?',
         r'''<p>Skup $T(v)$: povratni bridovi iz $v$ prema potomcima te stablasti bridovi prema djeci koje dijete <em>nije</em> potrošilo. Sparujemo bridove iz $T(v)$ proizvoljno. Ako je $|T(v)|$ neparan, preostali spajamo s bridom $v$–roditelj (koji time „nestaje”); ako je paran, brid $v$–roditelj ostaje slobodan i dodajemo ga u $T(\text{roditelj})$. Invarijanta: nakon obrade $v$ svi bridovi u podstablu $v$ (uključivo povratne koji imaju oba kraja u podstablu) su spareni, osim eventualno brida prema roditelju. U korijenu ostaje najviše jedan brid – parnost $m$.</p>'''),
        ('Gdje su implementacijske zamke?',
         r'''<p>Dubina DFS-a može biti $2 \cdot 10^5$ – iterativni DFS ili povećan stog. Kompresija koordinata ($x$ i $y$ zasebno, $y$-vrhovi pomaknuti za broj $x$-vrhova). Obrada „od dna” = obrnuti redoslijed ulaska u DFS (preorder), bez rekurzije. Ispiši indekse točaka (bridova), ne vrhova; svih $n$ parova, i onih neprijateljskih.</p>'''),
    ],
    'tips': [
        r'''Relacija „dijele koordinatu” prirodno se modelira <strong>bipartitnim grafom koordinata</strong> u kojem su točke bridovi – ista ideja rješava mnoge zadatke s retcima/stupcima (npr. brisanje po retcima i stupcima, Eulerovi obilasci po mreži).''',
        r'''Rastav bridova povezanog grafa u parove susjednih bridova (sve osim najviše jednog) standardna je lema; dokaz preko DFS-stabla „od listova prema korijenu” korisno je znati kao gotov alat.''',
        r'''Kad gornja granica ovisi o komponentama ($\sum \lfloor m_c/2 \rfloor$), provjeri može li se po komponentama i postići – često je odgovor da, a konstrukcija je lokalna.''',
        r'''U neusmjerenom DFS-u <em>nema poprečnih bridova</em>: svaki nestablasti brid spaja pretka i potomka. To je često ključna činjenica u konstruktivnim zadacima na grafovima.''',
    ],
    'solution': r'''
<p>Izgradimo bipartitni graf koji ima vrh za svaku vrijednost $x$-koordinate i vrh za svaku vrijednost $y$-koordinate. Svaka točka $(x_i, y_i)$ postaje brid koji spaja vrhove $x = x_i$ i $y = y_i$. U tom grafu treba formirati najveći broj disjunktnih parova bridova sa zajedničkim vrhom.</p>
<p>Za svaku povezanu komponentu problem se rješava zasebno. Pokažimo da u povezanoj komponenti s $m$ bridova uvijek možemo formirati $\lfloor m/2 \rfloor$ parova.</p>
<p>Izgradi DFS-stablo komponente. U komponenti svaki brid ili pripada stablu ili ide od pretka prema potomku — nema poprečnih bridova.</p>
<p>Riješimo problem rekurzivno od dna prema vrhu. Za svako podstablo DFS-stabla podijelit ćemo sve bridove unutar njega u prijateljske parove, a brid od korijena podstabla prema roditelju iskoristit ćemo ako je broj bridova u podstablu neparan.</p>
<p>Rekurzivna funkcija $f(v)$: najprije pozovi $f(u)$ za svu djecu $u$ korijena podstabla $v$. Iz svakog $u$ ili iskoristimo brid $u - v$ ili ga ostavimo nesparenog. Formiraj skup $S$ svih takvih nesparenih bridova te svih bridova koji iz $v$ idu prema njegovim potomcima (koji nisu izravna djeca). Svi bridovi u $S$ imaju $v$ kao zajednički vrh. Podijeli ih u parove proizvoljno; ako je $|S|$ neparan, preostali brid spari s bridom od $v$ prema roditelju.</p>
<p>Na kraju smo sve bridove podijelili u prijateljske parove, osim možda jednog brida incidentnog s korijenom.</p>
''',
    'detailed': r'''
<h3>1. Model: točke su bridovi</h3>
<p>Napravimo graf $G$ čiji su vrhovi sve različite $x$-vrijednosti i sve različite $y$-vrijednosti koje se pojavljuju među točkama, a točka $P_i = (x_i, y_i)$ je brid između vrha „$x = x_i$” i vrha „$y = y_i$”. Graf je bipartitan ($x$-vrhovi nasuprot $y$-vrhovima) i nema višestrukih bridova jer su točke različite. Dvije točke su prijateljske ako i samo ako dijele $x$ ili $y$, tj. ako i samo ako njihovi bridovi imaju zajednički vrh. Zadatak postaje:</p>
<p><em>rastaviti što više bridova od $2n$ u disjunktne parove bridova sa zajedničkim vrhom</em>; preostale bridove sparujemo proizvoljno (ti parovi nisu prijateljski, ali moraju biti ispisani).</p>
<h3>2. Gornja granica</h3>
<p>Dva brida sa zajedničkim vrhom su u istoj povezanoj komponenti. Ako komponenta $c$ ima $m_c$ bridova, iz nje se može dobiti najviše $\lfloor m_c / 2 \rfloor$ prijateljskih parova. Dakle $k \le \sum_c \lfloor m_c / 2 \rfloor$.</p>
<h3>3. Lema: granica se postiže</h3>
<p><b>Lema.</b> Bridovi povezanog grafa s $m$ bridova mogu se rastaviti na $\lfloor m/2 \rfloor$ parova susjednih bridova (i jedan brid viška ako je $m$ neparan).</p>
<p><i>Dokaz (konstruktivan).</i> Uzmimo DFS-stablo $T$ s korijenom $r$. U neusmjerenom grafu svaki brid koji nije u $T$ spaja vrh s njegovim pretkom (<em>povratni brid</em>); poprečnih bridova nema, jer bi DFS u trenutku otkrivanja prvog kraja takvog brida prešao njime na drugi, još neposjećeni kraj. Svakom bridu pridružimo <em>gornji</em> kraj (bliži korijenu): stablastom bridu $u$–roditelj$(u)$ to je roditelj, povratnom bridu $u$–predak to je predak.</p>
<p>Obrađujemo vrhove u <em>obrnutom preorderu</em> (djeca prije roditelja) i za vrh $v$ održavamo skup $D(v)$ „dostupnih” bridova čiji je gornji kraj $v$ i koji još nisu spareni: na početku su to svi povratni bridovi iz $v$ prema potomcima. Kad obrađujemo $v$:</p>
<ol>
<li>bridove iz $D(v)$ sparujemo proizvoljno – svaki par dijeli vrh $v$, dakle je prijateljski;</li>
<li>ako je $|D(v)|$ neparan, preostali brid sparimo s bridom $e_v = v$–roditelj$(v)$ (dijele $v$); brid $e_v$ je time potrošen;</li>
<li>ako je $|D(v)|$ paran, $e_v$ ostaje slobodan i dodajemo ga u $D(\text{roditelj}(v))$ – njegov gornji kraj je roditelj, pa će on biti sparen tamo.</li>
</ol>
<p><i>Invarijanta.</i> Nakon obrade $v$, svi bridovi čiji je gornji kraj u podstablu $T_v$ spareni su, osim možda $e_v$. Dokaz indukcijom po visini: povratni bridovi s gornjim krajem $v$ i stablasti bridovi prema djeci koji nisu potrošeni sve su u $D(v)$ (djeca su obrađena ranije i po pretpostavci sve ostalo je već spareno); korak 1–3 spari sve iz $D(v)$ osim, u parnom slučaju, ništa, a u neparnom potroši $e_v$. U korijenu $r$ nema $e_r$, pa ostaje nesparen najviše jedan brid, i to točno kad je $m$ neparan (broj sparenih bridova je paran). $\square$</p>
<h3>4. Algoritam</h3>
<ol>
<li>Kompresiraj koordinate: sortiraj različite $x$-vrijednosti i $y$-vrijednosti; $x$-vrh dobiva indeks $0..X-1$, $y$-vrh indeks $X..X+Y-1$. Brid $i$ spaja $eu_i$ i $ev_i$.</li>
<li>Iterativni DFS kroz sve vrhove (svaka komponenta ima svoj korijen): zapiši vrijeme ulaska $tin$, roditeljski brid $parEdge$, redoslijed posjeta $order$ i oznaku stablastih bridova.</li>
<li>Svaki nestablasti brid dodaj u $D$ kraja s manjim $tin$ (to je predak).</li>
<li>Prođi $order$ unatrag; za vrh $v$ spari $D(v)$ po dva; neparan ostatak spari s $parEdge(v)$ ako postoji, inače (korijen) zapamti kao višak komponente; paran slučaj: $parEdge(v)$ dodaj u $D(\text{roditelj})$.</li>
<li>$k$ = broj dosad nastalih parova. Viškove komponenata (njih je paran broj jer je ukupno $2n$ bridova) spari proizvoljno. Ispiši $k$ i sve parove indeksa točaka.</li>
</ol>
<h3>5. Složenost</h3>
<p>Sortiranje za kompresiju $O(n \log n)$; DFS i sparivanje $O(V + E) = O(n)$ (svaki brid uđe u točno jedan skup $D$ i jednom se spari). Ukupno $O(n \log n)$ po testu, $\sum n \le 10^5$.</p>
<h3>6. Zamke</h3>
<ul>
<li>Rekurzivni DFS može imati dubinu $2 \cdot 10^5$ (npr. sve točke na „stepenicama” $(i, i), (i, i + 1)$) – koristi iterativni DFS ili eksplicitni stog.</li>
<li>Povratni brid pripada <em>pretku</em> (manji $tin$), ne potomku – u potomku bi mogao ostati nesparen s bridovima koji nemaju zajednički vrh.</li>
<li>Iz brida $e$ i jednog kraja $v$ drugi kraj je $eu_e \oplus ev_e \oplus v$.</li>
<li>Ispisuju se indeksi <em>točaka</em> (1-indeksirano), a broj $k$ mora točno odgovarati broju prijateljskih među ispisanim parovima – ne ispisuj „skoro prijateljske” parove ni jedan brid dvaput.</li>
<li>Koordinate do $10^9$ po apsolutnoj vrijednosti – <code>long long</code> ili barem pažljiv <code>int</code> (unutar 32 bita, ali kompresija radi s vrijednostima, ne razlikama).</li>
</ul>
<h3>7. Primjeri</h3>
<ul>
<li>Točke $(0,0),(0,1),(1,0),(1,1)$: vrhovi $x{=}0, x{=}1, y{=}0, y{=}1$, četiri brida čine ciklus duljine $4$; jedna komponenta s $m = 4$, pa $k = 2$ (npr. $\{1, 2\}$ dijele $x = 0$, $\{3, 4\}$ dijele $x = 1$).</li>
<li>Točke $(0,0),(1,1),(2,2),(3,3)$: četiri komponente s po jednim bridom, $\sum \lfloor 1/2 \rfloor = 0$; ispisujemo $0$ i bilo koje sparivanje.</li>
<li>Točke $(0,0),(0,1),(0,2),(0,3)$: zvijezda sa središtem $x = 0$ i $4$ brida; $k = 2$.</li>
</ul>
''',
    'verified': r'''uzorak 1/1 (checker: valjano sparivanje, točno $k$ prijateljskih, $k$ jednak brute-force optimumu); 300 slučajnih testova ($n \le 4$, koordinate iz raspona $[-3, 3]$ radi mnogo poklapanja) protiv Python brute forcea koji ispituje sva sparivanja; 3 velika testa ($n = 10^5$: slučajne točke u malom rasponu, „stepenasti” lanac s dubinom DFS-a $2 \cdot 10^5$, te $10^4$ malih testova) unutar $0.15$ s.''',
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
        ('Što nas prisiljava na prijateljske parove – koja je donja granica?',
         r'''<p>Ako neki pravac (vodoravan ili okomit) sadrži $k$ točaka, izvan njega je samo $2n - k$ točaka. Svaka točka pravca sparena s točkom izvan njega „troši” jednu vanjsku točku, pa barem $k - (2n - k) = 2k - 2n$ točaka pravca ostaje sparenih međusobno – to je barem $k - n$ prijateljskih parova. Za $k \le n$ granica je $0$. Prirodna hipoteza: odgovor je točno $\max(0, k - n)$, gdje je $k$ najveća popunjenost pravca.</p>'''),
        ('Zašto bi $k \le n$ uvijek dopuštao nula prijateljskih parova?',
         r'''<p>Indukcijom po $n$: dovoljno je naći jedan neprijateljski par $(a, b)$ takav da nakon uklanjanja i dalje vrijedi $k' \le n - 1$. Pravci s $< n$ točaka su bezopasni; opasni su pravci s <em>točno</em> $n$ točaka – svaki mora izgubiti točku. Koliko ih može biti? Dva paralelna s po $n$ točaka pokrivaju sve točke, pa ih svaki neprijateljski par automatski oba dotiče. Vodoravni $H$ i okomiti $V$ s po $n$ točaka: uzmi $a \in H \setminus V$, $b \in V \setminus H$ – par je neprijateljski ($a$ i $b$ nemaju ni zajednički $x$ ni $y$) i dotiče oba.</p>'''),
        ('Kako iz te indukcije dobiti jedan algoritam koji radi u oba režima?',
         r'''<p>Uvijek uzmi najpuniji vodoravni $H$ i najpuniji okomiti $V$ i spari točku s $H$ koja nije na $V$ s točkom s $V$ koja nije na $H$. Time se svaki pravac s $n$ točaka dotakne (takav je ili $H$, ili $V$, ili mu paralelni „blizanac” koji pokriva sve točke izvan $H$/$V$), a ako je $k > n$ prenapučeni pravac je $H$ ili $V$ pa gubi točku – $k$ i $n$ padaju zajedno. Stanemo kad su sve preostale točke na jednom pravcu; tada ih sparimo međusobno i to je točno $k - n$ prijateljskih parova.</p>'''),
        ('Koji rubni slučaj ruši „uzmi točku s $H$ koja nije na $V$”?',
         r'''<p>Kad $H$ ima samo jednu točku i ona leži na $V$ (tada svi vodoravni pravci imaju po jednu točku). Tu točku sparimo s bilo kojom točkom drugog najpunijeg okomitog pravca $V'$: par je neprijateljski (različiti $x$, a svi $y$ su različiti), dotiče $V$ (jedini mogući pravac s $\ge n$ točaka), a $V'$ postoji jer $V$ ne sadrži sve točke. Simetrično za $V$. Ako $H$ ili $V$ ima $\ge 2$ točke, točka izvan sjecišta uvijek postoji.</p>'''),
        ('Koja struktura daje „najpuniji pravac” uz brisanja?',
         r'''<p>Za svaku orijentaciju skup parova (broj živih točaka, pravac) u <code>std::set</code> – najveći i drugi najveći element u $O(\log n)$, brisanje točke ažurira jedan par. Točke pravca u vektoru s pozicijama za brisanje u $O(1)$. Ukupno $O(n \log n)$; moguće i $O(n)$ s listama po popunjenosti.</p>'''),
    ],
    'tips': [
        r'''Za „minimiziraj/maksimiziraj broj parova sa svojstvom” prvo izvedi jednostavnu <strong>brojčanu granicu</strong> (ovdje: pravac s $k$ točaka nasuprot $2n - k$ vanjskih) i onda pokušaj dokazati da se postiže – najčešće indukcijom koja skida jedan par.''',
        r'''U induktivnim konstrukcijama identificiraj <em>kritične</em> objekte (pravce s točno $n$ točaka) i dokaži da ih je malo te da ih jedan potez može sve dotaknuti – to je srž dokaza.''',
        r'''Greedy „uzmi trenutno najveće” uz uklanjanje elemenata implementira se sa <code>std::set</code> parova (ključ, id) ili s kantama po ključu kad je ključ ograničen ($\le 2n$).''',
        r'''Male stvari koje treba provjeriti u sparivanjima: $n = 1$, sve točke na jednom pravcu, mreža $\{0,1\}^2$ gdje su sva četiri pravca „kritična”.''',
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
    'detailed': r'''
<h3>1. Donja granica</h3>
<p>Pravac je vodoravan ($y = c$) ili okomit ($x = c$). Neka je $k$ najveći broj točaka na jednom pravcu $L$. Izvan $L$ ima $2n - k$ točaka, pa najviše $2n - k$ točaka s $L$ može biti spareno s vanjskom točkom; preostalih barem $k - (2n - k) = 2(k - n)$ točaka s $L$ sparene su međusobno, što je barem $k - n$ prijateljskih parova. Dakle</p>
$$\text{odgovor} \ge \max(0, k - n).$$
<p>Pokazat ćemo da se ta granica postiže, tj. da se može napraviti $\min(n, 2n - k)$ neprijateljskih parova.</p>
<h3>2. Indukcija: slučaj $k \le n$</h3>
<p><b>Tvrdnja.</b> Ako je $k \le n$, postoji sparivanje bez prijateljskih parova.</p>
<p><i>Dokaz</i> indukcijom po $n$ ($n = 0$ trivijalno). Dovoljno je naći neprijateljski par $(a, b)$ nakon čijeg uklanjanja preostalih $2(n-1)$ točaka opet zadovoljava $k' \le n - 1$. Pravac s $\le n - 1$ točaka ostaje u redu; <em>kritični</em> su pravci s točno $n$ točaka – svaki mora izgubiti bar jednu točku. Analiza:</p>
<ul>
<li>Dva paralelna kritična pravca (npr. vodoravni $H_1, H_2$) sadrže zajedno svih $2n$ točaka; <em>svaki</em> neprijateljski par tada ima po jednu točku na svakom od njih (dvije točke istog $H_i$ bile bi prijateljske). Trećeg paralelnog kritičnog nema (nema više točaka).</li>
<li>Vodoravni kritični $H$ i okomiti kritični $V$ sijeku se u najviše jednoj točki, pa za $n \ge 2$ postoje $a \in H \setminus V$ i $b \in V \setminus H$. Par $(a, b)$: $x_a \ne x_V = x_b$ i $y_a = y_H \ne y_b$, dakle neprijateljski, i dotiče oba. (Za $n = 1$ je $k = 1$ i jedini par je neprijateljski.)</li>
<li>Jedan kritični pravac $L$: izvan njega je $n$ točaka; točka $p$ izvan $L$ prijateljska je s najviše jednom točkom $L$ (onom s istom drugom koordinatom), pa za $n \ge 2$ postoji $q \in L$ takva da je $(p, q)$ neprijateljski par koji dotiče $L$.</li>
<li>Nijedan kritični: bilo koji neprijateljski par. Postoji, jer je točka $p$ prijateljska s najviše $2(k - 1) \le 2n - 2 < 2n - 1$ drugih točaka.</li>
</ul>
<p>Sve slučajeve istodobno pokriva izbor iz sljedećeg odjeljka. $\square$</p>
<h3>3. Slučaj $k > n$</h3>
<p>Samo jedan pravac $L$ ima više od $n$ točaka (dva takva pravca, bilo paralelna ili okomita, ne mogu oba stati u $2n$ točaka jer se sijeku u $\le 1$ točki). Ako je $k < 2n$, izaberemo neprijateljski par koji sadrži točku s $L$ i točku izvan $L$: $n$ i $k$ oba padnu za $1$, pa je $2n - k$ nepromijenjeno i indukcija daje $2(n-1) - (k-1) = 2n - k - 1$ daljnjih neprijateljskih parova, ukupno $2n - k$. Postupak završava kad su sve preostale točke na $L$ ($k = 2n$); tada ih sparimo međusobno – to su točno $k - n$ prijateljskih parova iz donje granice.</p>
<h3>4. Jedinstveno pravilo izbora</h3>
<p>Neka je $H$ vodoravni pravac s najviše živih točaka, $V$ okomiti s najviše.</p>
<ol>
<li>Ako $H$ ili $V$ sadrži sve žive točke – stani; ostatak spari proizvoljno (svi parovi prijateljski).</li>
<li>Ako $|H| = 1$ i jedina točka $a$ na $H$ leži na $V$: tada svi vodoravni pravci imaju po jednu točku. Spari $a$ s bilo kojom točkom $b$ drugog najpunijeg okomitog pravca $V'$ ($V'$ postoji jer $V$ ne sadrži sve). Par je neprijateljski (različiti $x$; svi $y$ različiti).</li>
<li>Simetrično ako $|V| = 1$ i njegova točka leži na $H$.</li>
<li>Inače uzmi $a \in H \setminus V$ i $b \in V \setminus H$ (postoje: ako pravac ima $\ge 2$ točke, najviše jedna je na sjecištu; ako ima $1$ točku, ona po 2./3. nije na drugom pravcu). Par je neprijateljski.</li>
</ol>
<p><b>Zašto pravilo čuva invarijante.</b> Kritični pravac s $n$ točaka (kad $k \le n$) je ili $H$, ili $V$, ili paralelan „blizanac” od $H$ odn. $V$ koji pokriva sve točke izvan njega – u svakom slučaju par ga dotiče: $a \in H$, $b \in V$, a točka koja nije na $H$ (to je $b$) leži na blizancu od $H$. U slučaju 2. jedini pravci s $\ge n$ točaka mogu biti okomiti; $V$ je dotaknut ($a \in V$), a okomiti blizanac $V'$ također ($b \in V'$). Kad je $k > n$, prenapučeni pravac je $H$ ili $V$ (to je maksimum svoje orijentacije) i gubi točku $a$ odnosno $b$. Time se u oba režima postiže optimum iz odjeljaka 2 i 3.</p>
<h3>5. Implementacija</h3>
<p>Kompresija koordinata daje indeks okomitog ($x$) i vodoravnog ($y$) pravca svake točke. Za svaku orijentaciju čuvamo: vektor živih točaka po pravcu s pozicijom svake točke (brisanje zamjenom s posljednjom, $O(1)$), brojač živih točaka i <code>std::set&lt;pair&lt;int,int&gt;&gt;</code> parova (brojač, pravac) za pravce s bar jednom točkom. Najpuniji pravac je zadnji element skupa, drugi najpuniji predzadnji. Brisanje točke: izbaci stari par, smanji brojač, vrati novi par. „Točka pravca različita od $p$” – zadnja u vektoru ili predzadnja.</p>
<p>Glavna petlja radi dok ima živih točaka i dok nijedan pravac ne sadrži sve žive točke; nakon nje preostale točke (sve na jednom pravcu, paran broj) sparimo redom i njihov broj parova je $k_{\text{odg}}$. Ispis: $k_{\text{odg}}$, zatim svi parovi (indeksi točaka 1-indeksirani); redoslijed parova nije bitan, važno je da broj prijateljskih među njima bude točno $k_{\text{odg}}$.</p>
<h3>6. Složenost i zamke</h3>
<p>Svaka točka se izbriše jednom: $O(\log n)$ po brisanju – ukupno $O(n \log n)$, uz $\sum n \le 10^5$ zanemarivo. Zamke:</p>
<ul>
<li>slučaj 2./3. mora doći <em>prije</em> općeg slučaja – u općem slučaju „zamjena drugom točkom” ne postoji kad pravac ima jednu točku;</li>
<li>za $n = 1$ s dvije točke na istom pravcu petlja odmah stane ($|H| = 2 = $ živih) i odgovor je $1$;</li>
<li>točke su različite, pa se $H$ i $V$ sijeku u najviše jednoj točki – na to se oslanjaju svi izbori;</li>
<li>koordinate do $10^9$ po apsolutnoj vrijednosti (predznak!) – kompresija sortiranjem, ne kao indeksi polja.</li>
</ul>
<h3>7. Primjeri</h3>
<ul>
<li>$(0,0),(0,1),(1,0),(1,1)$: $k = 2 = n$, odgovor $0$: $H = \{y = 0\}$, $V = \{x = 0\}$; $a = (1, 0)$, $b = (0, 1)$ – neprijateljski; ostaju $(0,0),(1,1)$ – opet neprijateljski.</li>
<li>$(0,0),(0,1),(0,2),(0,3)$: $k = 4 > n = 2$, odgovor $k - n = 2$; $V$ sadrži sve točke, petlja odmah stane.</li>
<li>$(0,0),(1,1),(2,2),(3,3)$: $k = 1$, odgovor $0$; svaki par je neprijateljski.</li>
</ul>
''',
    'verified': r'''uzorak 1/1 (checker: valjano sparivanje, točno $k$ prijateljskih, $k$ jednak brute-force minimumu); 300 slučajnih testova ($n \le 4$; točke iz malog raspona ili namjerno nagurane na jedan pravac s $k$ od $1$ do $2n$) protiv Python brute forcea koji ispituje sva sparivanja; 3 velika testa ($n = 10^5$: pravac s $k > n$ točaka plus samci, slučajne točke, $10^4$ malih testova) unutar $0.2$ s.''',
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
        ('Koja je jedina veličina o kojoj ovisi „sigurnost” u temu, i što to govori o strukturi rješenja?',
         r'''<p>Samo $k$ – ukupan broj naučenih tema. Naučena tema $i$ je sigurna ako i samo ako $b_i \le k$. Ako teme poredamo po $b$, sigurne naučene teme su upravo one naučene s najmanjim $b$ – <em>prefiks</em> naučenog skupa u tom poretku. Dakle skup naučenih tema ima dva dijela: sigurne (male $b$) i „punjenje” (velike $b$, uče se samo da $k$ bude dovoljno velik).</p>'''),
        ('Je li „mogu li biti siguran u barem $x$ tema” monotono?',
         r'''<p>Da: isti skup koji daje $\ge x$ sigurnih daje i $\ge x - 1$. Zato binarno pretražujemo najveći izvediv $x$ i trebamo samo <em>provjeru</em> za zadani $x$: postoji li skup $P$, $|P| = k \ge x$, takav da $x$-ta najmanja vrijednost $b$ u $P$ nije veća od $k$.</p>'''),
        ('Kako fiksirati dovoljno strukture da provjera postane greedy?',
         r'''<p>Fiksiraj temu $i$ kao $x$-tu naučenu po $b$ (ona s najvećim $b$ među sigurnima). Tada iz tema ispred $i$ (u poretku po $b$) učimo <em>točno</em> $x - 1$ tema – više ne smijemo (ušle bi među prvih $x$ i $i$ više ne bi bila $x$-ta), manje ne možemo. Iza $i$ učimo koliko treba da $k \ge b_i$: $\max(0, b_i - x)$ tema. Sve odabrane teme samo troše vrijeme, pa biramo najjeftinije: $x - 1$ najjeftinijih ispred i $b_i - x$ najjeftinijih iza. Provjera prolazi ako je za neki $i$ ukupno vrijeme $\le t$.</p>'''),
        ('Kako za sve $i$ brzo dobiti zbroj $m$ najjeftinijih u prefiksu i $c_i$ najjeftinijih u sufiksu?',
         r'''<p>Prefiks: $m = x - 1$ je fiksan; prolaz slijeva s max-gomilom veličine $m$ (dodaj, izbaci najveći ako ih je više od $m$) daje zbroj $m$ najmanjih u $O(\log n)$ po koraku. Sufiks: $c_i = \max(0, b_i - x)$ je <em>nerastući</em> kad $i$ pada (jer je $b$ sortiran), pa prolazom zdesna gomilu samo smanjujemo: prije čitanja $i$ izbacuj najveće dok veličina ne padne na $c_i$, zabilježi zbroj, pa dodaj $a_i$. Nikad ne treba vraćati izbačene elemente.</p>'''),
        ('Koja je složenost i kako rekonstruirati skup?',
         r'''<p>Provjera je $O(n \log n)$, binarno pretraživanje dodaje faktor $\log n$: $O(n \log^2 n)$ za $n = 2 \cdot 10^5$ je udobno unutar $6$ s. Za rekonstrukciju ponovno pozovi provjeru za najveći izvediv $x$, uzmi vraćeni $i$, i eksplicitno sortiraj teme ispred/iza $i$ po cijeni. Zbrojevi vremena idu do $2 \cdot 10^{14}$ – 64-bitni tipovi.</p>'''),
    ],
    'tips': [
        r'''Kad uvjet ovisi samo o <strong>broju</strong> odabranih elemenata ($b_i \le k$), sortiraj po pragu: odabrani elementi se raspadaju na „zadovoljene” (prefiks) i „punjenje” (ostatak), a to otvara vrata binarnom pretraživanju po broju zadovoljenih.''',
        r'''„Postoji li skup s $\ge x$ dobrih” monotono je u $x$ gotovo uvijek – binarno pretraživanje po odgovoru pretvara optimizaciju u provjeru s fiksnim $x$, koja je najčešće greedy.''',
        r'''Zbroj $m$ najmanjih na svim prefiksima (fiksni $m$) = prolaz s max-gomilom veličine $m$; ako se $m$ monotono mijenja u smjeru prolaza, gomilu treba samo smanjivati – provjeri monotonost prije nego što posegneš za složenijom strukturom.''',
        r'''Nakon binarnog pretraživanja rekonstrukciju radi <em>ponovnim pozivom provjere</em> s pamćenjem svjedoka ($i$), umjesto da provjeru kompliciraš pamćenjem odabira u svakom koraku.''',
    ],
    'solution': r'''
<p>Bez smanjenja općenitosti preuredimo teme tako da je $b_1 \le b_2 \le \dots \le b_n$.</p>
<p>Binarno pretražujemo $x$, broj tema u koje ćeš biti siguran. Kako provjeriti može li se biti siguran u $x$ tema?</p>
<p>Neka su $p_1 < p_2 < \dots < p_k$ teme koje učiš ($k \ge x$). Budući da su teme poredane po $b$, moraš biti siguran u teme $p_1, \dots, p_x$, pa mora vrijediti $k \ge b_{p_x}$.</p>
<p>Iterirajmo po temi $i$: može li biti $p_x = i$? Tada trebamo odabrati $x - 1$ tema s najmanjim $a_j$ među temama $1, \dots, i-1$ i $\max(0, b_i - x)$ tema s najmanjim $a_j$ među temama $i+1, \dots, n$. Ako ukupno vrijeme učenja odabranih tema (uključivo teme $i$) ne prelazi $t$, u redu je.</p>
<p>Za $x - 1$ tema s najmanjim $a_j$ na svakom prefiksu prolazimo niz slijeva nadesno s prioritetnim redom; za $\max(0, b_i - x)$ tema s najmanjim $a_j$ na svakom sufiksu prolazimo zdesna nalijevo, također s prioritetnim redom.</p>
<p>Ukupna vremenska složenost: $O(n \log^2 n)$ (jedan logaritam od binarnog pretraživanja po $x$, drugi od prioritetnog reda).</p>
''',
    'detailed': r'''
<h3>1. Struktura optimalnog skupa</h3>
<p>Neka je $P$ skup naučenih tema, $k = |P|$. Tema $i \in P$ je sigurna ako i samo ako $b_i \le k$ – uvjet ovisi samo o $k$, ne o tome <em>koje</em> su druge teme. Poredajmo teme neopadajuće po $b$ (izjednačene proizvoljno) i neka su naučene teme, u tom poretku, $p_1 < p_2 < \dots < p_k$. Sigurne su točno one s $b_{p_j} \le k$; kako $b_{p_j}$ ne pada s $j$, sigurne su $p_1, \dots, p_s$ za neki $s$ – prefiks. Drugim riječima, naučeni skup se sastoji od <em>sigurnih</em> tema (najmanji $b$ u skupu) i <em>punjenja</em> (teme većeg $b$ koje učimo samo da bi $k$ bio dovoljno velik).</p>
<h3>2. Monotonost i binarno pretraživanje</h3>
<p>Definirajmo $F(x)$ = „postoji dopustiv skup s barem $x$ sigurnih tema”. Ako $P$ svjedoči $F(x)$, isti $P$ svjedoči i $F(x - 1)$, pa je $F$ monotona: istinita za $x \le x^*$ i lažna iznad. Odgovor $x^*$ nalazimo binarnim pretraživanjem na $[0, n]$ ($F(0)$ vrijedi uz prazan skup) uz $O(\log n)$ poziva provjere.</p>
<p><b>Provjera $F(x)$, $x \ge 1$:</b> postoji li $P$ s $|P| = k \ge x$ i $b_{p_x} \le k$? Uvjet „barem $x$ sigurnih” je ekvivalentan s „$x$-ta po $b$ je sigurna”, jer su sigurne prefiks.</p>
<h3>3. Fiksiranje $x$-te teme čini provjeru pohlepnom</h3>
<p>Prođimo po svim temama $i$ i pitajmo: postoji li dopustiv $P$ u kojem je $p_x = i$? U takvom $P$:</p>
<ul>
<li>ispred $i$ (pozicije $< i$ u poretku po $b$) je <em>točno</em> $x - 1$ tema: manje ne može jer je $i$ $x$-ta, više ne može jer bi tada $x$-ta bila neka prije $i$;</li>
<li>iza $i$ je $r \ge 0$ tema, a uvjet sigurnosti glasi $k = x + r \ge b_i$, tj. $r \ge c_i := \max(0, b_i - x)$;</li>
<li>ukupno vrijeme je zbroj $a$ svih odabranih.</li>
</ul>
<p>Sve odabrane teme samo troše vrijeme, a nijedna druga osim $i$ ne utječe na uvjet. Zato je za fiksni $i$ najjeftiniji dopustivi skup: $x - 1$ <em>najjeftinijih</em> tema ispred $i$, tema $i$, i točno $c_i$ najjeftinijih tema iza $i$ (dodatne teme iza samo povećavaju cijenu). Ako je za neki $i$ taj minimum $\le t$ (i postoji dovoljno tema: $i - 1 \ge x - 1$, $n - i \ge c_i$), $F(x)$ vrijedi; inače ne, jer svaki svjedok ima neki $p_x = i$ i cijenu barem tog minimuma.</p>
<h3>4. Zbrojevi najjeftinijih u prefiksima i sufiksima</h3>
<p><b>Prefiks.</b> Traži se $\mathrm{pre}(i)$ = zbroj $x - 1$ najmanjih $a$ na pozicijama $< i$. Prolazimo slijeva i održavamo max-gomilu s najviše $x - 1$ elemenata: nakon dodavanja $a_i$ izbacimo najveći ako ih ima $x$. Gomila u svakom trenutku sadrži $\min(x-1, \text{pročitano})$ najmanjih, zbroj održavamo uz nju.</p>
<p><b>Sufiks.</b> Traži se $\mathrm{suf}(i)$ = zbroj $c_i$ najmanjih $a$ na pozicijama $> i$, gdje se $c_i = \max(0, b_i - x)$ <em>mijenja</em> s $i$. Ključno: $b$ je sortiran, pa je $c_i$ nerastuće kad $i$ pada. Prolazimo zdesna nalijevo s max-gomilom: prije obrade $i$ izbacujemo najveće dok veličina ne padne na $c_i$; ako je veličina točno $c_i$, zapišemo $\mathrm{suf}(i)$ = trenutni zbroj (inače nema dovoljno tema, $\mathrm{suf}(i) = -\infty$); zatim dodamo $a_i$ u gomilu. Invarijanta: prije skraćivanja za poziciju $i$ gomila je oblika (najjeftinijih $c_{i+1}$ među pozicijama $> i + 1$) $\cup \{a_{i+1}\}$, a taj skup sadrži $s$ najjeftinijih među pozicijama $> i$ za svaki $s \le c_{i+1}$; kako je $c_i \le c_{i+1}$, izbacivanje najvećih do veličine $c_i$ ostavlja točno $c_i$ najjeftinijih. Elementi izbačeni kao „preveliki” nikad kasnije ne postaju potrebni jer se $c$ samo smanjuje. Da je $c$ rastao, morali bismo vraćati izbačene elemente i trebala bi složenija struktura (npr. dvije gomile ili BIT po vrijednostima).</p>
<p>Provjera: $F(x) \iff \exists i:\ \mathrm{pre}(i) + a_i + \mathrm{suf}(i) \le t$, uz oba dijela definirana. Vraćamo takav $i$ kao svjedok.</p>
<h3>5. Rekonstrukcija</h3>
<p>Nakon binarnog pretraživanja ponovno pozovemo provjeru za $x^*$ i dobijemo svjedoka $i$. Skup: $x^* - 1$ najjeftinijih ispred $i$ (sortiramo prefiks po $a$), tema $i$, $c_i$ najjeftinijih iza $i$. Ispisujemo originalne indekse. Za $x^* = 0$ ispisujemo $0$ i prazan skup (bilo koji dopustiv skup je u redu, prazan je najjednostavniji).</p>
<h3>6. Složenost</h3>
<p>Sortiranje $O(n \log n)$; provjera – dva prolaza s gomilom – $O(n \log n)$; binarno pretraživanje $O(\log n)$ provjera. Ukupno $O(n \log^2 n)$, za $\sum n \le 2 \cdot 10^5$ oko $4 \cdot 10^7$ operacija na gomili, daleko ispod $6$ s.</p>
<h3>7. Zamke</h3>
<ul>
<li>Zbroj vremena do $2 \cdot 10^{14}$ ($t$) i do $2 \cdot 10^5 \cdot 10^9$ – <code>long long</code> za zbrojeve i $t$.</li>
<li>Točno $x - 1$ ispred $i$: prefiksna gomila mora imati veličinu <em>točno</em> $x - 1$ u trenutku provjere za $i$ (za $i \le x - 1$ nema dovoljno tema).</li>
<li>Redoslijed u sufiksnom prolazu: najprije skratiti gomilu na $c_i$ i očitati zbroj, <em>tek onda</em> dodati $a_i$ – tema $i$ ne smije biti u vlastitom sufiksu.</li>
<li>Izjednačeni $b$: bilo koji poredak; provjera prolazi kroz sve $i$ pa je svaki mogući $p_x$ pokriven.</li>
<li>Ispis: broj sigurnih, zatim $k$ i indeksi u bilo kojem poretku; broj sigurnih u ispisanom skupu mora točno odgovarati.</li>
</ul>
<h3>8. Primjer</h3>
<p>$t = 100$, teme $(a, b)$: $1{:}(20, 1)$, $2{:}(40, 4)$, $3{:}(60, 3)$, $4{:}(30, 3)$. Poredak po $b$: $1, 3, 4, 2$ ($b = 1, 3, 3, 4$). Provjera $x = 2$: kandidat $i = 4$ (druga po $b$ među odabranima): ispred jedna najjeftinija tema $\{1\}$ ($20$), $c = 3 - 2 = 1$ najjeftinija iza – tema $2$ ($40$); ukupno $20 + 30 + 40 = 90 \le 100$ – izvedivo. $x = 3$: bilo koji $i$ traži $2$ teme ispred plus $i$, npr. $i = 4$: $\{1, 3\} + 4 = 110 > 100$; $i = 2$: $b_2 = 4 > 3$ pa $c = 1$, ali iza teme $2$ nema tema – neizvedivo. Odgovor $2$, naučiti $\{1, 4, 2\}$.</p>
''',
    'verified': r'''uzorak 1/1 (checker: broj sigurnih jednak očekivanom, odabir valjan i unutar $t$); 300 slučajnih testova ($n \le 9$, mali $a$ i $t$) protiv Python brute forcea koji ispituje sve podskupove; 3 velika testa ($n = 2 \cdot 10^5$: slučajni, svi $b \ge n/2$ uz jeftine teme, te $10^4$ testova s $n = 20$) unutar $0.2$ s.''',
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
        ('Koji grad prijatelji biraju za zadani raspored?',
         r'''<p>Funkcija $S(v) = \sum_i |v - a_i|$ je konveksna po dijelovima linearna: pomak $v \to v + 1$ mijenja je za (broj $a_i \le v$) $-$ (broj $a_i > v$). Za sortirane $a_1 \le \dots \le a_k$ minimum je u medijanu: za neparan $k$ jedinstveno u $a_{(k+1)/2}$, za paran u svakom gradu segmenta $[a_{k/2}, a_{k/2+1}]$, a pravilo izjednačenja bira najmanji – $a_{k/2}$, <em>donji medijan</em>. Zadatak je dakle: zbroj donjeg medijana po svih $n^k$ nizova.</p>'''),
        ('Zašto je lakše računati očekivanje nego zbroj?',
         r'''<p>Zbroj po $n^k$ rasporeda jednak je $n^k \cdot E[\text{izbor}]$ kad svaki prijatelj bira grad uniformno i neovisno. Očekivanje dopušta <em>simetriju</em> i <em>linearnost</em>: refleksija $a \mapsto n + 1 - a$ čuva raspodjelu i preslikava $j$-tu statistiku poretka u $n + 1 - $ ($k + 1 - j$)-tu. Za neparan $k$ medijan se preslika u $n + 1 - $ medijan, pa je $E = \frac{n+1}{2}$ i odgovor $\frac{n+1}{2} n^k$ – gotovo bez računanja.</p>'''),
        ('Što se kvari za paran $k$ i kako to popraviti?',
         r'''<p>Donji medijan $a_{k/2}$ nije simetričan (refleksija ga šalje u gornji medijan $a_{k/2+1}$). Simetrična je <em>sredina</em> $m = \frac{a_{k/2} + a_{k/2+1}}{2}$, $E(m) = \frac{n+1}{2}$. Uz razmak $d = a_{k/2+1} - a_{k/2}$ vrijedi $a_{k/2} = m - d/2$, pa linearnost daje $E(a_{k/2}) = \frac{n+1}{2} - \frac{1}{2} E(d)$. Ostaje očekivani razmak medijana.</p>'''),
        ('Kako izračunati $E(d)$ bez zbrajanja po parovima vrijednosti medijana?',
         r'''<p>Razmak je broj jediničnih cesta $(i, i+1)$ između medijana: $d = \sum_{i=1}^{n-1} [a_{k/2} \le i < a_{k/2+1}]$. Linearnost: $E(d) = \sum_i p_i$, gdje je $p_i$ vjerojatnost da je točno $k/2$ prijatelja u $1..i$ i točno $k/2$ u $i+1..n$ (to je ekvivalentno s $a_{k/2} \le i$ i $a_{k/2+1} \ge i + 1$): $p_i = \binom{k}{k/2} \left(\frac{i}{n}\right)^{k/2} \left(\frac{n-i}{n}\right)^{k/2}$. Konačno $n^k E(a_{k/2}) = \frac{n+1}{2} n^k - \frac{1}{2} \binom{k}{k/2} \sum_{i=1}^{n-1} i^{k/2} (n-i)^{k/2}$.</p>'''),
        ('Kako to izračunati za $n, k \le 10^6$ modulo $998244353$?',
         r'''<p>Faktorijeli do $k$ za $\binom{k}{k/2}$, potencije $i^{k/2}$ brzim potenciranjem ($O(n \log k)$) ili linearno preko najmanjeg prostog faktora; dijeljenje s $2$ je množenje inverzom $\frac{p+1}{2}$. Sve u 64-bitnoj aritmetici s redukcijom nakon svakog množenja.</p>'''),
    ],
    'tips': [
        r'''„Zbroj po svim $n^k$ nizovima” = $n^k \cdot$ očekivanje uz uniformne neovisne izbore – prijelaz na očekivanje otključava <strong>linearnost</strong> i <strong>simetriju</strong> koje na zbroju nisu očite.''',
        r'''Nesimetričnu statistiku (donji medijan) izrazi kao simetričnu (sredina medijana) minus polovicu razlike; razliku dviju susjednih statistika poretka rastavi po jediničnim segmentima i koristi $E(\text{duljina}) = \sum P(\text{segment je unutra})$.''',
        r'''Minimum od $\sum |v - a_i|$ na cijelim brojevima uvijek je medijan; kod parnog $k$ cijeli segment $[a_{k/2}, a_{k/2+1}]$ – uvijek pročitaj pravilo izjednačenja u zadatku prije nego što odabereš „medijan”.''',
        r'''Uvijek provjeri zatvorenu formulu na najmanjem primjeru ručno (ovdje $n = 3$, $k = 2$: $18 - 4 = 14$) prije nego što ju implementiraš modularno.''',
    ],
    'solution': r'''
<p>Preuredimo gradove u kojima prijatelji žive tako da je $a_1 \le a_2 \le \dots \le a_k$. Ako je $k$ neparan, prijatelji se sastaju u gradu $a_{(k+1)/2}$; ako je $k$ paran, u gradu $a_{k/2}$. Usredotočimo se na očekivanu vrijednost odgovora uz pretpostavku da svaki prijatelj bira grad uniformno slučajno, i na kraju je pomnožimo s $n^k$.</p>
<p>Za neparan $k$ zbog simetrije vrijedi $E(a_{(k+1)/2}) = \frac{n+1}{2}$, pa je odgovor $\frac{n+1}{2} \cdot n^k$.</p>
<p>Za paran $k$ ne možemo isto zaključiti o $a_{k/2}$, ali možemo promatrati prosjek dvaju medijana $m = \frac{a_{k/2} + a_{k/2+1}}{2}$, za koji je $E(m) = \frac{n+1}{2}$. Neka je $d = a_{k/2+1} - a_{k/2}$ razmak dvaju medijana. Tada je $a_{k/2} = m - \frac{d}{2}$ i $E(a_{k/2}) = E(m) - E(\frac{d}{2}) = \frac{n+1}{2} - \frac{1}{2} E(d)$.</p>
<p>Kako naći $E(d)$? Za svaki $i = 1, \dots, n-1$ nađimo vjerojatnost $p_i$ da dužina između gradova $i$ i $i+1$ leži između dvaju medijana; tada je $E(d) = \sum_{i=1}^{n-1} p_i$. Za to je potrebno da točno $\frac{k}{2}$ prijatelja živi u gradovima $1, \dots, i$ i točno $\frac{k}{2}$ u gradovima $i+1, \dots, n$:</p>
$$p_i = \frac{i^{k/2} (n-i)^{k/2} \binom{k}{k/2}}{n^k}.$$
<p>Vremenska složenost: $O(n \log k + k)$.</p>
''',
    'detailed': r'''
<h3>1. Koji grad se bira: donji medijan</h3>
<p>Za fiksni raspored neka je $S(v) = \sum_{i=1}^{k} |v - a_i|$. Prijelaz s $v$ na $v + 1$ povećava udaljenost do svakog $a_i \le v$ za $1$ i smanjuje do svakog $a_i \ge v + 1$ za $1$, pa je</p>
$$S(v+1) - S(v) = \#\{i : a_i \le v\} - \#\{i : a_i \ge v + 1\}.$$
<p>Taj je izraz neopadajući u $v$, dakle $S$ je konveksna; minimum je u svim $v$ za koje je $S(v) - S(v-1) \le 0 \le S(v+1) - S(v)$. Neka je $a_1 \le \dots \le a_k$ sortirani raspored.</p>
<ul>
<li>$k$ neparan: za $v < a_{(k+1)/2}$ je $\#\{a_i \le v\} \le \frac{k-1}{2} < \#\{a_i \ge v+1\}$, pa $S$ strogo pada; za $v \ge a_{(k+1)/2}$ je $\#\{a_i \le v\} \ge \frac{k+1}{2} > \#\{a_i \ge v + 1\}$, pa strogo raste. Jedinstveni minimum: $a_{(k+1)/2}$.</li>
<li>$k$ paran: za $v < a_{k/2}$ $S$ strogo pada, za $a_{k/2} \le v < a_{k/2+1}$ razlika je $\frac{k}{2} - \frac{k}{2} = 0$ ($S$ konstantna), za $v \ge a_{k/2+1}$ strogo raste. Minimizatori su gradovi $a_{k/2}, \dots, a_{k/2+1}$, a pravilo bira najmanji: $a_{k/2}$.</li>
</ul>
<h3>2. Prijelaz na očekivanje</h3>
<p>Neka svaki prijatelj bira grad uniformno i neovisno. Traženi zbroj je $n^k \cdot E[X]$, gdje je $X$ odabrani grad. Refleksija $\phi(a) = n + 1 - a$ je bijekcija na $\{1..n\}^k$ koja čuva uniformnu raspodjelu i obrće poredak: $j$-ta najmanja vrijednost prelazi u $n + 1 - $ ($(k+1-j)$-ta najmanja). Zato za svaku statistiku poretka vrijedi $E(a_{(j)}) + E(a_{(k+1-j)}) = n + 1$.</p>
<h3>3. Neparan $k$</h3>
<p>$X = a_{((k+1)/2)}$ i $j = k + 1 - j$ za $j = \frac{k+1}{2}$, pa $2E(X) = n + 1$, $E(X) = \frac{n+1}{2}$. Odgovor $\frac{n+1}{2} \cdot n^k$ (cijeli broj jer je $n(n+1)$ paran; modularno množimo inverzom od $2$).</p>
<h3>4. Paran $k$: sredina i razmak medijana</h3>
<p>Neka je $L = a_{(k/2)}$ (donji medijan), $U = a_{(k/2+1)}$ (gornji), $m = \frac{L + U}{2}$, $d = U - L \ge 0$. Po odjeljku 2, $E(L) + E(U) = n + 1$, dakle $E(m) = \frac{n+1}{2}$. Kako je $L = m - \frac{d}{2}$, linearnost očekivanja daje</p>
$$E(L) = \frac{n+1}{2} - \frac{1}{2} E(d).$$
<h3>5. Očekivani razmak: rastav po cestama</h3>
<p>Cesta $i$ spaja gradove $i$ i $i + 1$ ($1 \le i \le n - 1$). Razmak $d$ jednak je broju cesta „između medijana”: $d = \sum_{i=1}^{n-1} [L \le i < U]$. Uvjet $L \le i$ znači da barem $k/2$ prijatelja živi u $1..i$; uvjet $U \ge i + 1$ znači da najviše $k/2$ prijatelja živi u $1..i$. Zajedno: <em>točno</em> $k/2$ prijatelja u $1..i$ (i točno $k/2$ u $i+1..n$). Prijatelji biraju neovisno, svaki je u $1..i$ s vjerojatnošću $\frac{i}{n}$, pa je to binomna vjerojatnost:</p>
$$p_i = \binom{k}{k/2} \left(\frac{i}{n}\right)^{k/2} \left(\frac{n-i}{n}\right)^{k/2}, \qquad E(d) = \sum_{i=1}^{n-1} p_i.$$
<h3>6. Konačna formula</h3>
$$\text{odgovor} = n^k E(L) = \frac{n+1}{2} n^k - \frac{1}{2} \binom{k}{k/2} \sum_{i=1}^{n-1} i^{k/2} (n-i)^{k/2} \pmod{998244353}.$$
<p>Sve su veličine cijeli brojevi ($n^k p_i$ je broj rasporeda), pa je modularno računanje s inverzom od $2$ legitimno.</p>
<h3>7. Implementacija i složenost</h3>
<ol>
<li>$n^k$ brzim potenciranjem; $\frac{n+1}{2}$ kao $(n+1) \cdot 2^{-1} \bmod p$.</li>
<li>Za paran $k$: faktorijeli do $k$ ($O(k)$), $\binom{k}{k/2} = \frac{k!}{(k/2)!^2}$ preko inverza Fermatom.</li>
<li>Zbroj $\sum_{i=1}^{n-1} i^{k/2} (n-i)^{k/2}$: $2(n-1)$ brzih potenciranja, $O(n \log k)$; po želji $O(n)$ linearnim sitom potencija ($i^{e}$ je multiplikativna funkcija).</li>
<li>Ukupno $O(n \log k + k)$ vremena i $O(k)$ memorije – oko $4 \cdot 10^7$ modularnih množenja, unutar $0.1$ s.</li>
</ol>
<h3>8. Zamke</h3>
<ul>
<li>Pravilo izjednačenja: donji, ne gornji medijan – s gornjim bi predznak popravka bio suprotan.</li>
<li>Faktor $\frac{1}{2}$ ispred popravka; bez njega odgovor za $n = 3$, $k = 2$ ispadne $10$ umjesto $14$.</li>
<li>Umnošci do $p^2 \approx 10^{18}$ stanu u 64 bita, ali <em>svaki</em> umnožak reducirati; oduzimanje modularno ($+p$ prije $\bmod$).</li>
<li>Granice zbroja: $i = 1..n-1$ (za $i = 0$ i $i = n$ je pribrojnik ionako $0$).</li>
</ul>
<h3>9. Primjeri</h3>
<p>$n = 3$, $k = 2$: $\frac{4}{2} \cdot 9 = 18$; $\binom{2}{1} = 2$; $\sum_{i=1}^{2} i (3-i) = 2 + 2 = 4$; popravak $\frac{1}{2} \cdot 2 \cdot 4 = 4$; odgovor $14$ – slaže se s ručnim brojanjem iz zadatka ($5 \cdot 1 + 3 \cdot 2 + 1 \cdot 3$).</p>
<p>$n = 5$, $k = 3$ (neparan): $\frac{6}{2} \cdot 125 = 375$.</p>
''',
    'verified': r'''uzorci 2/2; 300 slučajnih testova ($2 \le n, k \le 9$) protiv Python brute forcea koji prolazi svih $n^k$ rasporeda i bira grad po definiciji (minimalni zbroj udaljenosti, pa najmanji broj); 3 velika testa ($n, k$ do $10^6$) unutar $0.1$ s.''',
},
]
