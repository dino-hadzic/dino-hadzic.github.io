# -*- coding: utf-8 -*-
STAGE = {
    'no': 11,
    'name': 'Stage 11: Shanghai',
    'source_name': 'The 2022 ICPC Asia East Continent Final Contest, EC-Final 2022',
    'source_html': r'''
<p>Prijevod službenog kratkog rješenja sudačkog tima EC-Final 2022 (EC Final 2022 裁判组): <a href="https://contest.ucup.ac/download.php?type=attachments&amp;id=1197&amp;r=2">Tutorial (zh-cn)</a>. Tekst zadatka preveden je prema službenim <a href="https://contest.ucup.ac/download.php?type=attachments&amp;id=1197&amp;r=1">engleskim tekstovima zadataka</a>. Zadatak je dostupan na <a href="https://contest.ucup.ac/contest/1197">Universal Cup Judging System</a>.</p>
''',
}

PROBLEMS = [
# ---------------------------------------------------------------- A
{
    'letter': 'A', 'title': 'Coloring', 'title_hr': 'Bojanje', 'slug': 'A_coloring',
    'tl': '2 s', 'ml': '1024 MB',
    'statement': r'''
<p>Dano je $n$ elemenata numeriranih od $1$ do $n$. Element $i$ ima vrijednost $w_i$ i boju $c_i$, a osim toga ima i pokazivač $a_i$ na neki drugi element ($a_i \ne i$).</p>
<p>Na početku je boja elementa $s$ jednaka $1$, a boja svih ostalih elemenata je $0$. Operaciju</p>
<ul>
    <li>postavi $c_i \leftarrow c_{a_i}$ uz cijenu $p_i$</li>
</ul>
<p>smiješ izvesti proizvoljno mnogo puta, za bilo koje $i$. Tvoj rezultat jednak je zbroju vrijednosti svih elemenata koji na kraju imaju boju $1$, umanjenom za zbroj cijena svih izvedenih operacija. Odredi najveći mogući rezultat.</p>
<h3>Ulaz</h3>
<p>Prvi redak sadrži cijele brojeve $n$ i $s$ ($1 \le s \le n \le 5 \cdot 10^3$). Drugi redak sadrži $w_1, \dots, w_n$ ($-10^9 \le w_i \le 10^9$), treći $p_1, \dots, p_n$ ($0 \le p_i \le 10^9$), a četvrti $a_1, \dots, a_n$ ($1 \le a_i \le n$, $a_i \ne i$).</p>
<h3>Izlaz</h3>
<p>Ispiši jedan cijeli broj — najveći mogući rezultat.</p>
<h3>Primjer</h3>
<p>Za $n = 3$, $s = 1$, $w = [-1, -1, 2]$, $p = [1, 0, 0]$, $a = [3, 1, 2]$ odgovor je $1$: redom izvedemo operacije na elementima $2, 1, 3, 2$ i dobijemo $c = [0, 0, 1]$ uz ukupnu cijenu $p_2 + p_1 + p_3 + p_2 = 1$, pa je rezultat $w_3 - 1 = 1$.</p>
''',
    'hints': [
        r'''<p>Svaki element ima točno jedan izlazni brid $i \to a_i$, pa graf pokazivača čini <em>funkcijski graf</em>: svaka komponenta je ciklus na koji su „nakačena” stabla. Boja se kroz operacije širi samo u smjeru suprotnom od pokazivača — od $a_i$ prema $i$.</p>''',
        r'''<p>Promatraj kako se boje mijenjaju duž ciklusa u vremenu: boja $1$ počinje u $s$ i može putovati oko ciklusa, a iza nje po želji „gasimo” elemente natrag na $0$. Tako svaki element ciklusa doživi niz izmjena $0 \to 1 \to 0 \to 1 \dots$; broj takvih izmjena je ključan parametar.</p>''',
        r'''<p>U podstablu koje visi na čvoru ciklusa svaki čvor može preuzeti boju roditelja u trenutku kad mu odgovara. Ako podstablo želi iskoristiti $k$ „slojeva” izmjena (npr. neki potomci boje $1$, neki $0$, pa opet $1$ …), ciklus se na tom mjestu mora promijeniti barem $k$ puta. Definiraj DP po podstablima: najbolji rezultat uz najviše $k$ izmjena.</p>''',
    ],
    'coach': [
        ('Kamo boja uopće može putovati? Što je s elementima izvan komponente od $s$?',
         r'''
<p>Operacija $c_i \leftarrow c_{a_i}$ prenosi boju iz $a_i$ u $i$, dakle <em>suprotno</em> smjeru pokazivača. Graf pokazivača je funkcijski graf (svaki vrh ima točno jedan izlazni brid), pa je svaka komponenta ciklus sa stablima „nakačenima” na njega, s bridovima usmjerenima prema ciklusu. Jedinica kreće iz $s$ i može teći samo prema vrhovima koji pokazuju na već obojene vrhove: ako je $s$ u stablu, samo u njegovo podstablo; ako je $s$ na ciklusu, oko ciklusa i u sva stabla. Sve ostalo zauvijek ostaje $0$, pa te vrhove možemo zaboraviti.</p>
'''),
        ('Kako izgleda skup jedinica na ciklusu u svakom trenutku i koje su jedine promjene moguće?',
         r'''
<p>Na ciklusu jedan vrh mijenja boju samo ako se razlikuje od prethodnika. Ako jedinice čine jedan neprekinuti blok, jedini vrh s bojom $0$ i prethodnikom $1$ je vrh odmah ispred bloka (blok se produlji sprijeda), a jedini vrh s bojom $1$ i prethodnikom $0$ je zadnji vrh bloka (blok se skrati straga). Blok dakle ostaje neprekinut i „vrti se” u smjeru toka; svaki vrh ciklusa doživljava izmjene $0 \to 1 \to 0 \to \dots$ i svaka ga izmjena košta $p_v$. Kad blok nestane ili prekrije cijeli ciklus, više se ništa ne događa.</p>
'''),
        ('Što vidi podstablo koje visi na vrhu $v$ ciklusa, i zašto je broj izmjena boje jedini bitan parametar?',
         r'''
<p>Dijete $c$ vrha $v$ može u bilo kojem trenutku kopirati <em>trenutnu</em> boju od $v$, pa je niz boja djeteta podniz niza boja roditelja (počevši od $0$). Ako roditelj promijeni boju $k$ puta, dijete ju može promijeniti najviše $k$ puta (a bilo koji manji broj također), i to vrijedi rekurzivno prema dolje. Dakle je za podstablo bitno samo koliko izmjena „sloj iznad” nudi: definiramo $f_v[k]$ = najbolji doprinos podstabla vrha $v$ ako $v$ promijeni boju točno $k$ puta, i $g_v[K] = \max_{k \le K} f_v[k]$.</p>
'''),
        ('Zašto DP po stablu nije preskup ako svaki vrh nosi tablicu duljine do $n$?',
         r'''
<p>Podstablo visine $h$ ne može iskoristiti više od $h + 1$ izmjena vrha $v$: list mijenja boju najviše jednom korisno ($0 \to 1$), a vrh iznad njega treba najviše jednu izmjenu više od svoje djece (npr. $0 \to 1 \to 0$ da bi dijete pokupilo jedinicu, a on sam ostao $0$). Zato je tablica vrha duga $h_v + 2$, a zbroj $\sum_v (h_v + 2)$ ne prelazi $O(n^2)$ ni u najgorem (lančastom) slučaju; tablice djece oslobađamo čim ih roditelj obradi.</p>
'''),
        ('Kako u $O(n^2)$ pobrojati sva moguća stanja ciklusa?',
         r'''
<p>Stanje ciklusa određeno je s tri broja: koliko je puta prednji kraj bloka obišao ciklus ($q$), te gdje su stali prednji i stražnji kraj u posljednjem, nedovršenom obilasku ($r$ i $r'$). Vrhovi ciklusa tada se dijele na tri susjedna segmenta s brojevima izmjena $2q+2$, $2q+1$ i $2q$ (ili $2q+1$, $2q$, $2q-1$, ovisno o tome završava li $s$ bojom $0$ ili $1$). Za fiksan $q$ vrijednost svakog vrha za svaki od tri režima je poznata, pa maksimum po $(r, r')$ nalazimo prefiksnim zbrojevima u $O(L)$. Kako $q$ ne treba premašiti polovicu najveće korisne kapacitete, ukupno je $O(n \cdot n)$.</p>
'''),
    ],
    'tips': [
        r'''Graf u kojem svaki vrh ima točno jedan izlazni brid je <em>funkcijski graf</em>: uvijek ga rastavi na ciklus + stabla i posebno riješi stablo (DP od listova) i ciklus (enumeracija stanja). Prvo provjeri u kojem smjeru „teče” informacija — ovdje suprotno od pokazivača.''',
        r'''Kad neki proces može ponavljati izmjene $0 \to 1 \to 0 \to \dots$, uvedi broj izmjena kao dimenziju DP-a i ograniči ga strukturno (ovdje visinom podstabla) — to često pretvara naizgled beskonačan prostor u $O(n^2)$.''',
        r'''U DP-u „najbolje uz najviše $K$” (a ne točno $K$) čuvaj prefiksne maksimume $g[K] = \max_{k \le K} f[k]$ i dopusti zasićenje za $K$ veći od tablice; to uklanja posebne slučajeve pri spajanju djece različitih visina.''',
        r'''Za male cikluse (ovdje duljine $2$) uvijek ručno provjeri opću enumeraciju: pravilo „blok se može i produljiti i skratiti” ne vrijedi kad bi produljenje prekrilo cijeli ciklus.''',
    ],
    'solution': r'''
<p>Graf u kojem svaki element pokazuje na točno jedan drugi element je funkcijski graf: svaka komponenta je jedan ciklus na koji su pridružena stabla (<em>ciklus sa stablima</em>). Boja se operacijom $c_i \leftarrow c_{a_i}$ prenosi s elementa $a_i$ na element $i$, dakle iz smjera ciklusa prema listovima, odnosno oko ciklusa.</p>
<p>Promotrimo ciklus. Nakon svake operacije ciklus se sastoji od jednog neprekinutog bloka jedinica i jednog bloka nula; operacije pomiču granice tih blokova, pa svaki čvor ciklusa kroz vrijeme doživljava niz izmjena boje $0 \to 1 \to 0 \to \dots$. Kako se blok jedinica vrti oko ciklusa, i podstabla „nakačena” na čvorove ciklusa postaju slojevita: čvor podstabla preuzima boju roditelja u trenutku koji mu odgovara, pa se podstablo dijeli na slojeve prema tome u kojoj je izmjeni koji čvor preuzeo boju.</p>
<p>Ako podstablo neki čvora ciklusa iskorištava najviše $k$ slojeva (izmjena), tada se boja tog čvora ciklusa mora promijeniti barem $k$ puta. Zato najprije napravimo <strong>DP po podstablima</strong>: za svaki čvor izvan ciklusa pamtimo najbolji doprinos podstabla za svaki dopušteni broj izmjena boje roditelja, uzimajući u obzir vrijednosti $w$ čvorova koji završe s bojom $1$ i cijene $p$ svih izvedenih operacija.</p>
<p>Zatim promatramo ciklus: enumeriramo koji susjedni segment ciklusa na kraju ostaje obojen jedinicom i koliko se puta boja oko ciklusa izmijenila; svaki čvor ciklusa doprinosi vrijednošću svog podstabla za taj broj izmjena umanjenom za cijenu vlastitih izmjena. Dio u kojem enumeriramo završni segment jedinica ubrzamo prefiksnim zbrojevima ili DP-om duž ciklusa.</p>
<p>Ukupna složenost je $O(n^2)$.</p>
''',
    'detailed': r'''
<h3>Struktura: funkcijski graf i smjer toka boje</h3>
<p>Svaki element $i$ ima točno jedan pokazivač $a_i \ne i$, pa je graf s bridovima $i \to a_i$ <em>funkcijski graf</em>: svaka slaba komponenta sastoji se od točno jednog usmjerenog ciklusa i stabala čiji bridovi vode prema ciklusu. Operacija $c_i \leftarrow c_{a_i}$ kopira boju <em>iz</em> $a_i$ <em>u</em> $i$, dakle boja putuje suprotno od pokazivača: od korijena (ciklusa) prema listovima, odnosno oko ciklusa u smjeru „$a_i \to i$”.</p>
<p>Jedina jedinica na početku je u $s$. Vrh $i$ može ikad dobiti jedinicu samo ako postoji lanac $s = v_0, v_1, \dots, v_t = i$ s $a_{v_{j+1}} = v_j$. Ako je $s$ u stablu, to su točno vrhovi podstabla od $s$ (u stablu s korijenom na ciklusu); ako je $s$ na ciklusu, to su svi vrhovi komponente. Sve ostale vrhove zanemarujemo — završavaju s bojom $0$ bez ikakva troška.</p>

<h3>Slučaj 1: $s$ nije na ciklusu</h3>
<p>Roditelj $a_s$ zauvijek ima boju $0$, pa $s$ može boju promijeniti najviše jednom (na $0$, uz cijenu $p_s$), a djeca od $s$ vide niz boja $1$ ili $1, 0$. Ostatak je čisti DP po stablu koji opisujemo u nastavku, uz sitnu razliku da $s$ počinje s bojom $1$.</p>

<h3>Ključna lema: jedinice na ciklusu čine jedan blok koji se vrti</h3>
<p>Neka su vrhovi ciklusa $v_0 = s, v_1, \dots, v_{L-1}$ poredani u smjeru toka ($a_{v_{j+1}} = v_j$). Vrh ciklusa mijenja boju samo ako se razlikuje od svog prethodnika. Pretpostavimo (induktivno) da jedinice čine neprekinut blok $v_x, \dots, v_y$. Jedini vrh s bojom $0$ čiji je prethodnik $1$ je $v_{y+1}$: operacija na njemu <em>produlji blok sprijeda</em>. Jedini vrh s bojom $1$ čiji je prethodnik $0$ je $v_x$: operacija na njemu <em>skrati blok straga</em>. Svaka druga operacija na ciklusu ne mijenja ništa. Dakle blok ostaje neprekinut, njegovi krajevi pomiču se samo u smjeru toka, a proces završava tek ako blok nestane (sve $0$) ili prekrije cijeli ciklus (sve $1$); nakon toga nijedna operacija ništa ne mijenja.</p>
<p>Posljedica: vrh ciklusa $v_i$ doživljava naizmjenične izmjene $0 \to 1$ (kad ga prijeđe prednji kraj) i $1 \to 0$ (kad ga prijeđe stražnji kraj), a $s$ počinje s $1$ pa kod njega redoslijed počinje izmjenom $1 \to 0$. Ako je $F_i$ broj prolazaka prednjeg, a $B_i$ stražnjeg kraja kroz $v_i$, vrh je promijenio boju $k_i = F_i + B_i$ puta (svaki put uz cijenu $p_{v_i}$) i završava s bojom $1$ točno kad je $F_i > B_i$ (za $s$: kad je $F_0 \ge B_0$). Budući da krajevi ne mogu jedan drugoga preteći dok je blok neprazan i nije cijeli ciklus, uvijek je $F_i - B_i \in \{0, 1\}$ za $i \ge 1$ i $B_0 - F_0 \in \{0, 1\}$.</p>

<h3>Što podstablo vidi: broj izmjena boje roditelja</h3>
<p>Neka vrh $v$ (izvan ciklusa) kroz vrijeme ima niz boja $0, 1, 0, 1, \dots$ s ukupno $k$ izmjena. Njegovo dijete $c$ počinje s $0$ i u proizvoljnim trenucima kopira <em>trenutnu</em> boju od $v$; kopiranje iste boje ništa ne mijenja, pa je niz boja djeteta podniz niza boja roditelja koji počinje s $0$ i strogo alternira. Zato dijete može imati bilo koji broj izmjena $k' \le k$, ali ne više. Isto vrijedi rekurzivno, a različita djeca su neovisna (svako bira svoje trenutke). Time je dokazano da je za podstablo vrha $v$ bitno <em>samo</em> koliko puta se $v$ promijeni.</p>
<p>Definiramo:</p>
<ul>
    <li>$f_v[k]$ — najbolji doprinos podstabla vrha $v$ (zbroj $w$ vrhova koji završavaju s bojom $1$ minus zbroj cijena svih operacija u podstablu, uključujući operacije na $v$) ako $v$ promijeni boju točno $k$ puta;</li>
    <li>$g_v[K] = \max_{0 \le k \le K} f_v[k]$ — najbolji doprinos ako $v$ smije promijeniti boju najviše $K$ puta.</li>
</ul>
<p>Prijelaz je zbrajanje po djeci: $f_v[k] = -k\,p_v + [k \text{ neparan}]\,w_v + \sum_{c \in \text{djeca}(v)} g_c[k]$, jer je nakon $k$ izmjena (od $0$) boja od $v$ jednaka parnosti od $k$, a svako dijete smije imati najviše $k$ izmjena.</p>
<p><strong>Ograničenje duljine tablice.</strong> Podstablo visine $h_v$ ne može korisno iskoristiti više od $h_v + 1$ izmjena: list ima korist samo od $k \in \{0, 1\}$, a induktivno, ako djeca koriste najviše $h_c + 1 \le h_v$ izmjena, vrhu $v$ treba najviše jedna izmjena više (da nakon što djeca pokupe zadnju boju sam vrati boju na povoljniju). Više izmjena samo povećava trošak, pa je $g_v[K] = g_v[h_v + 1]$ za sve veće $K$ („zasićenje”). Tablica vrha $v$ ima $h_v + 2$ elemenata, a računanje traje $O((h_v + 2)(1 + \deg v))$; zbroj po svim vrhovima je $O(n^2)$ (najgori je lanac). Tablice djece brišemo čim je roditelj obrađen, pa je i memorija $O(n)$. DP provodimo iterativno (redoslijed „djeca prije roditelja” dobiven iz eksplicitnog stoga), jer rekurzija dubine $5000$ nije opasna, ali ni potrebna.</p>
<p>Za vrhove ciklusa uzimamo isto: ako vrh ciklusa $v_i$ ($i \ge 1$) ima $k_i$ izmjena, svako njegovo dijete iz stabla dobiva kapacitet $K = k_i$; za $s$, koji počinje s bojom $1$ i ima niz $1, 0, 1, \dots$ s $k_0$ izmjena, dijete može pratiti $k_0 + 1$ stanja, pa mu je kapacitet $K = k_0 + 1$. U slučaju 1 (s nije na ciklusu) $k_s \in \{0, 1\}$ i odgovor je $\max_{k_s} \left( -k_s p_s + [k_s = 0] w_s + \sum_c g_c[k_s + 1] \right)$.</p>

<h3>Enumeracija stanja ciklusa u $O(n^2)$</h3>
<p>Završno stanje ciklusa potpuno opisuju: broj potpunih obilazaka $q$ i položaji $r, r'$ na kojima su stali prednji i stražnji kraj u posljednjem, nepotpunom obilasku. Dva su slučaja prema završnoj boji od $s$.</p>
<ul>
    <li><strong>Slučaj A</strong> ($s$ završava s $0$, $k_0 = 2q + 1$, tj. $F_0 = q$, $B_0 = q + 1$): za $i \ge 1$ vrijedi $k_i = 2q + 2$ i boja $0$ ako $i \le r'$ (oba kraja prošla $q + 1$ puta), $k_i = 2q + 1$ i boja $1$ ako $r' < i \le r$, te $k_i = 2q$ i boja $0$ ako $i > r$; uvjet je $0 \le r' \le r \le L - 1$ (za $r' = r$ blok je nestao).</li>
    <li><strong>Slučaj B</strong> ($s$ završava s $1$, $k_0 = 2q$): za $i \ge 1$ vrijedi $k_i = 2q + 1$ i boja $1$ ako $i \le r$, $k_i = 2q$ i boja $0$ ako $r < i \le r'$, te $k_i = 2q - 1$ i boja $1$ ako $i > r'$; uvjet je $r \le r'$, a za $q = 0$ nužno $r' = L - 1$ (blok tek kreće iz $s$).</li>
</ul>
<p>Sva ta stanja doista su dostižna: krajeve pomičemo naizmjence tako da je blok stalno neprazan i kraći od $L$ (za $L \ge 3$). Vrijednost vrha $v_i$ u režimu $(k, \text{boja}, K)$ je $\text{val}_i = [\text{boja}]\,w_{v_i} - k\,p_{v_i} + \sum_{c} g_c[K]$, gdje $K = k$ za $i \ge 1$ i $K = k + 1$ za $s$. Za fiksan $q$ izračunamo prefiksne zbrojeve triju režima po $i = 1, \dots, L-1$ i maksimum po parovima $(r', r)$ dobijemo jednim prolazom uz „najbolji dosad” (npr. u slučaju A: $\max_{r' \le r} (P_A[r'] - P_B[r']) + P_B[r] + (P_C[L-1] - P_C[r])$). Broj korisnih $q$ ograničen je kapacitetom: $2q$ ne treba premašiti najveću duljinu tablice među djecom vrhova ciklusa plus konstantu, pa je ukupno $O(L \cdot n) \subseteq O(n^2)$.</p>
<p><strong>Ciklus duljine $2$.</strong> Ovdje se blok duljine $1$ ne može „vrtjeti”: produljenje sprijeda odmah daje sve jedinice, skraćivanje straga sve nule, a u oba stanja proces staje. Postoje samo tri završna stanja (ništa; $v_1$ preuzme $1$; $s$ preuzme $0$), koja obradimo izravno.</p>

<h3>Primjer</h3>
<p>$n = 3$, $s = 1$, $a = [3, 1, 2]$: ciklus je $1 \to 3 \to 2 \to 1$ u smjeru pokazivača, a boja teče $1 \to 2 \to 3 \to 1$. Za $w = [-1, -1, 2]$, $p = [1, 0, 0]$ isplati se da blok jedinica prijeđe s $1$ na $2$ pa na $3$ i pritom „ugasi” $1$ i $2$: izmjene $2{:}\,0\to1\to0$ (cijena $0$), $1{:}\,1\to0$ (cijena $1$), $3{:}\,0\to1$ (cijena $0$). Rezultat je $w_3 - 1 = 1$, što odgovara slučaju A s $q = 0$, $r' = 1$, $r = 2$.</p>

<h3>Složenost i zamke</h3>
<ul>
    <li>Vrijeme $O(n^2)$, memorija $O(n)$ uz oslobađanje tablica djece (bez toga je $O(n^2)$ 64-bitnih brojeva, što je za $n = 5000$ još prihvatljivo, ali nepotrebno).</li>
    <li>Vrijednosti su do $5000 \cdot 10^9$ po predznaku, plus cijene do $n^2 \cdot 10^9 \approx 2.5 \cdot 10^{16}$ — koristi 64-bitne cijele brojeve i „minus beskonačno” reda $-10^{18}$ koje se smije zbrajati nekoliko puta bez prelijevanja.</li>
    <li>Smjer toka boje suprotan je pokazivačima; ciklus treba poredati tako da $v_{j+1}$ pokazuje na $v_j$ i rotirati da $v_0 = s$.</li>
    <li>Kapacitet djece vrha $s$ je $k_0 + 1$, a ne $k_0$, jer $s$ počinje s bojom $1$.</li>
</ul>
''',
    'verified': r'''uzorci 2/2; 300 slučajnih malih testova ($n \le 8$) protiv brute forcea koji Dijkstrom pretražuje svih $2^n$ obojenja po pravilima operacije; 3 velika testa s $n = 5000$ (dugi ciklus, ciklus duljine $2$ s dugim lancima, slučajan funkcijski graf), svaki ispod $0.05$ s.''',
},
# ---------------------------------------------------------------- B
{
    'letter': 'B', 'title': 'Binary String', 'title_hr': 'Binarni niz', 'slug': 'B_binary_string',
    'tl': '2 s', 'ml': '1024 MB',
    'statement': r'''
<p>Dan je binarni niz $a_0 a_1 \dots a_{n-1}$ raspoređen u krug. Svake sekunde istodobno se svaki par $01$ zamijeni u $10$: ako je $a_i = 0$ i $a_{(i+1) \bmod n} = 1$, ta se dva znaka zamijene. Primjerice, $100101110$ prelazi u $001010111$.</p>
<p>Koliko će se različitih nizova pojaviti tijekom beskonačno mnogo sekundi (uključujući početni)? Odgovor ispiši modulo $998244353$. Nizovi se uspoređuju po pozicijama, pa ciklički pomaci niza mogu biti međusobno različiti nizovi.</p>
<h3>Ulaz</h3>
<p>Prvi redak sadrži broj testnih primjera $T$ ($1 \le T \le 10^6$). Svaki testni primjer je jedan binarni niz. Zbroj duljina svih nizova ne prelazi $10^7$.</p>
<h3>Izlaz</h3>
<p>Za svaki testni primjer ispiši traženi broj u zasebnom retku.</p>
<h3>Primjer</h3>
<p>Za nizove $1$, $001001$ i $0001111$ odgovori su redom $1$, $3$ i $9$.</p>
''',
    'hints': [
        r'''<p>Gledaj jedinice kao čestice: jedinica se u sekundi pomakne ulijevo točno onda kad joj je lijevi susjed $0$. Kad se sve čestice pomiču istodobno, niz se samo ciklički rotira — od tog trenutka ništa novo ne nastaje.</p>''',
        r'''<p>Odgovor je (broj sekundi dok se neka čestica još „zaglavljuje”) + (najmanji ciklički period niza u tom trenutku). Prvi dio traži formulu za položaj $j$-te čestice u trenutku $t$: zapiši rekurziju $y_j(t+1) = \max(y_j(t) - 1,\ y_{j-1}(t) + 1)$ i „razmotaj” je.</p>''',
        r'''<p>Ako je jedinica više od nula, primijeni komplement i obrat niza — proces ostaje isti, a onda uvijek vrijedi $2m \le n$, što osigurava da svaka čestica u najviše $m$ koraka „nađe” prethodnicu koja ju ograničava.</p>''',
    ],
    'coach': [
        ('Što se zapravo pomiče — parovi $01$ ili pojedinačni znakovi? Kako to zapisati kao gibanje čestica?',
         r'''
<p>Zamjena $01 \to 10$ znači da se jedinica pomaknula za jedno mjesto ulijevo. Budući da se sve zamjene događaju istodobno, jedinica na položaju $y$ pomiče se točno onda kad je u trenutku $t$ polje $y - 1$ prazno; ako je tamo druga jedinica, ostaje (čak i ako se ta druga pomiče). Dakle jedinice su čestice koje putuju ulijevo brzinom $1$ i ne mogu se preteći. To je poznati stanični automat (pravilo 184 / paralelni TASEP), a cijela dinamika svodi se na gibanje čestica.</p>
'''),
        ('Zašto smijemo pretpostaviti da jedinica nema više od nula?',
         r'''
<p>Komplementiranje niza zamjenjuje uloge $0$ i $1$ (par $01$ postaje $10$ i „putuje” udesno), a obrat niza zamjenjuje smjerove. Kompozicija tih dviju bijekcija prevodi jedan korak procesa u jedan korak istog procesa na transformiranom nizu, pa je broj različitih nizova jednak. Zato uvijek možemo raditi s $m = $ broj jedinica $\le n/2$; tada je razmak između čestica u prosjeku $\ge 2$, što je ključno za granicu $t^* \le m - 1$.</p>
'''),
        ('Kako iz rekurzije $y_j(t+1) = \\max(y_j(t) - 1, y_{j-1}(t) + 1)$ dobiti zatvorenu formulu?',
         r'''
<p>Rekurzija je linearna u (max, +) algebri, pa se razmotava kao najdulji put: nakon $t$ koraka od kojih $d$ puta „preskočimo” na prethodnu česticu (+1) i $t - d$ puta se pomaknemo (−1), dobivamo $y_j(t) = \max_{0 \le d \le t} \left( Y_{j-d} + 2d - t \right) = -t + 2j + \max_{j - t \le i \le j} W_i$, gdje je $W_i = Y_i - 2i$, a $Y_i$ početni položaji produženi ciklički ($Y_{i-m} = Y_i - n$). Sve što treba znati o dinamici sadržano je u nizu $W$.</p>
'''),
        ('Kada se čestica $j$ u trenutku $t$ ne pomiče, izraženo preko $W$? Kada se više nijedna ne zaglavljuje?',
         r'''
<p>Razmak $y_j(t) - y_{j-1}(t) = 2 + M_j(t) - M_{j-1}(t)$, gdje su $M$ maksimumi od $W$ na prozorima $[j-t, j]$ i $[j-1-t, j-1]$. Kako $W$ po indeksu pada najviše za $1$, razmak je $1$ točno onda kad je $W_{j-1-t}$ strogo veći od svih $W_{j-t}, \dots, W_j$. Drugim riječima, indeks $i$ „koči” sve dok ne prođe $\mathrm{nxt}_i - 1$ sekundi, gdje je $\mathrm{nxt}_i$ udaljenost do prvog sljedećeg indeksa s $W \ge W_i$. Nakon $t^* = \max_i (\mathrm{nxt}_i - 1)$ svi se razmaci ustale na $\ge 2$ i niz se samo rotira.</p>
'''),
        ('Zašto je odgovor točno $t^* + $ period, a ne nešto složenije?',
         r'''
<p>Proces je deterministički, pa je niz stanja oblika „rep + ciklus”. Sva stanja od trenutka $t^*$ nadalje su ciklički pomaci istog niza (period $p$ = najmanji ciklički period niza $a(t^*)$, KMP-om), a u njima je svaka čestica slobodna. Sva ranija stanja imaju barem jednu zaglavljenu česticu, pa nisu na ciklusu, a međusobno su različita (inače bi se proces vrtio među njima i nikad ne bi postao slobodan). Ukupno različitih nizova: $t^* + p$.</p>
'''),
    ],
    'tips': [
        r'''Kad pravilo lokalno zamjenjuje susjedne znakove, provjeri može li se prevesti u gibanje „čestica” koje se ne mogu preteći — tada se dinamika često opisuje rekurzijom u (max, +) algebri koja se razmotava u zatvorenu formulu s prozorskim maksimumom.''',
        r'''Simetrije (komplement, obrat, ciklički pomak) iskoristi na početku da smanjiš broj slučajeva; pritom provjeri da simetrija doista komutira s jednim korakom procesa.''',
        r'''Broj različitih stanja determinističkog procesa je duljina repa plus duljina ciklusa; ciklus čistih rotacija ima duljinu jednaku najmanjem cikličkom periodu niza — računaj ga prefiksnom funkcijom: $p = n - \pi[n-1]$ ako $p \mid n$, inače $n$.''',
        r'''Za ulaze od $10^7$ znakova čitaj cijeli ulaz jednim <code>fread</code> i piši izlaz u vlastiti međuspremnik; standardni <code>cin</code> po znaku lako probije limit.''',
    ],
    'solution': r'''
<p>Promotrimo neprekinuti blok nula duljine veće od $1$, primjerice $\dots 0101000000101 \dots$. Nakon jedne sekunde on prelazi u $\dots 1010000001010 \dots$, što znači da se cijeli blok nula pomaknuo za jedno mjesto ulijevo. Analogno se blok jedinica duljine veće od $1$ pomiče za jedno mjesto udesno.</p>
<p>Ako su blok jedinica i blok nula susjedni, npr. $\dots 0111100001 \dots \to \dots 1011100010 \dots$, dva bloka se sudaraju i svakom se duljina smanji za $1$.</p>
<p>Taj se proces nastavlja dok postoje i blokovi nula i blokovi jedinica (duljine barem $2$). Bez smanjenja općenitosti pretpostavimo da je ukupna duljina blokova jedinica barem tolika kao ukupna duljina blokova nula. Tada postoji početna pozicija na krugu takva da u svakom prefiksu ukupna duljina blokova jedinica nije manja od ukupne duljine blokova nula. Krenuvši od te pozicije možemo za svaki blok nula izračunati u kojem trenutku nestaje, a time i niz koji nastaje nakon što nestanu svi blokovi nula. Od tog trenutka niz se samo ciklički pomiče, pa je preostalo izračunati najmanji period završnog niza: broj različitih nizova jednak je broju sekundi do stabilizacije uvećanom za taj najmanji period.</p>
<p>Vremenska složenost je $O(n)$.</p>
''',
    'detailed': r'''
<h3>Model: jedinice kao čestice</h3>
<p>Zamjena $01 \to 10$ pomiče jedinicu za jedno mjesto ulijevo. Sve se zamjene izvode istodobno prema stanju u trenutku $t$, pa se jedinica na položaju $y$ pomiče točno onda kad je polje $y - 1$ u trenutku $t$ prazno (nula). Ako je ondje druga jedinica, ona ostaje na mjestu, pa makar se ta druga jedinica u istoj sekundi pomaknula. Jedinice su dakle čestice koje se gibaju ulijevo brzinom najviše $1$ i nikad se ne pretječu; poredak čestica po krugu je očuvan.</p>
<p>Ako je $m$ broj jedinica i $m = 0$ ili $m = n$, niz se ne mijenja i odgovor je $1$. Ako je $2m > n$, primijenimo komplement i obrat: komplement pretvara pravilo „$01 \to 10$” u „$10 \to 01$” (nule postaju čestice koje putuju udesno), a obrat vraća smjer. Obje su operacije bijekcije koje komutiraju s jednim korakom procesa, pa je broj različitih nizova isti. Nadalje pretpostavljamo $2m \le n$.</p>

<h3>Rekurzija položaja i njezino rješenje</h3>
<p>Neka su $Y_0 < Y_1 < \dots < Y_{m-1}$ početni položaji čestica u $[0, n)$ i produžimo ih ciklički: $Y_{i - m} = Y_i - n$ za sve cijele $i$. Označimo s $y_j(t)$ položaj čestice $j$ u trenutku $t$ (isto produženo). Čestica $j$ se pomiče točno kad je $y_j(t) - y_{j-1}(t) \ge 2$; inače je razmak točno $1$ i ostaje. Zato</p>
<p>$$y_j(t+1) = \max\bigl(y_j(t) - 1,\ y_{j-1}(t) + 1\bigr),$$</p>
<p>jer je pri razmaku $\ge 2$ prvi član veći, a pri razmaku $1$ drugi član jednak $y_j(t)$. Rekurzija je linearna u $(\max, +)$ algebri i razmotava se kao „najdulji put”: u $t$ koraka $d$ puta biramo drugi član (prelazak na prethodnu česticu, $+1$) i $t - d$ puta prvi ($-1$), pa je</p>
<p>$$y_j(t) = \max_{0 \le d \le t} \bigl( Y_{j-d} + d - (t - d) \bigr) = -t + 2j + \max_{j - t \le i \le j} W_i, \qquad W_i := Y_i - 2i.$$</p>
<p>Niz $W$ ima dva svojstva: $W_i - W_{i-1} = (Y_i - Y_{i-1}) - 2 \ge -1$ (pada najviše za $1$ po koraku) i $W_{i+m} = W_i + (n - 2m) \ge W_i$ (zbog $2m \le n$).</p>

<h3>Kada je čestica zaglavljena i kada proces postaje rotacija</h3>
<p>Neka je $M_j(t) = \max_{[j-t, j]} W$. Razmak je $y_j(t) - y_{j-1}(t) = 2 + M_j(t) - M_{j-1}(t)$. Prozori $[j-t, j]$ i $[j-1-t, j-1]$ razlikuju se samo u krajnjim indeksima, pa je $M_{j-1}(t) > M_j(t)$ točno kad je $W_{j-1-t} > \max(W_{j-t}, \dots, W_j)$; tada je zbog pada od najviše $1$ razlika točno $1$, a razmak točno $1$ — čestica $j$ je zaglavljena. Definirajmo $\mathrm{nxt}_i = \min\{ d \ge 1 : W_{i+d} \ge W_i \}$ (postoji i $\le m$ jer je $W_{i+m} \ge W_i$). Indeks $i$ uzrokuje zaglavljivanje (čestice $j = i + 1 + t$) u svim trenucima $t < \mathrm{nxt}_i - 1$, i ni u jednom kasnijem. Zato je</p>
<p>$$t^* = \max_i \bigl(\mathrm{nxt}_i - 1\bigr) \le m - 1$$</p>
<p>prvi trenutak u kojem su sve čestice slobodne; skup „zaglavljenih trenutaka” je početni odsječak $\{0, \dots, t^* - 1\}$. Kad su sve čestice slobodne, svi se razmaci čuvaju, pa je svaki sljedeći niz ciklički pomak prethodnog za jedno mjesto ulijevo.</p>

<h3>Broj različitih nizova</h3>
<p>Proces je deterministički, pa je niz stanja „rep pa ciklus”. Stanja $a(t^*), a(t^*+1), \dots$ su rotacije istog niza; njihov broj je najmanji ciklički period $p$ niza $a(t^*)$ ($a$ pomaknut za $p$ jednak je $a$). Stanja $a(0), \dots, a(t^*-1)$ imaju barem jednu zaglavljenu česticu, dok su sva stanja na ciklusu slobodna, pa se rep i ciklus ne sijeku. Stanja repa su međusobno različita: kad bi $a(t_1) = a(t_2)$ za $t_1 < t_2 < t^*$, proces bi se zauvijek vrtio među zaglavljenim stanjima i nikad ne bi postao slobodan. Dakle odgovor je $t^* + p$ (modulo $998244353$, iako je zbroj $\le n + m < 2 \cdot 10^7$).</p>

<h3>Algoritam</h3>
<ol>
    <li>Ako je niz konstantan, ispiši $1$. Ako je $2m > n$, obrni i komplementiraj.</li>
    <li>Izračunaj $W_i$ za $i \in [-m, m)$: $W_0 = Y_0$, $W_i = W_{i-1} + (Y_i - Y_{i-1}) - 2$, $W_{i-m} = W_i - (n - 2m)$.</li>
    <li>Monotonim stogom zdesna nalijevo nađi za svaki $i \in [-m, 0)$ prvi indeks desno s $W \ge W_i$; $t^* = \max(\mathrm{nxt}_i - 1)$. (Dovoljan je jedan period indeksa jer je $\mathrm{nxt}_{i+m} = \mathrm{nxt}_i$.)</li>
    <li>Niz u trenutku $t^*$: $y_j = -t^* + 2j + \max_{[j - t^*, j]} W$ za $j \in [0, m)$, prozorski maksimum dequeom; položaje svedi modulo $n$.</li>
    <li>Prefiksnom funkcijom izračunaj najmanji period $p$ ($p = n - \pi[n-1]$ ako dijeli $n$, inače $p = n$) i ispiši $t^* + p$.</li>
</ol>
<p>Sve faze su linearne, dakle $O(n)$ po nizu, ukupno $O(\sum n) = O(10^7)$. Memorija je $O(n)$; ulaz od $10^7$ znakova i do $10^6$ redaka izlaza zahtijevaju vlastito čitanje (<code>fread</code>) i pisanje.</p>

<h3>Provjera na primjerima</h3>
<p>$001001$: $m = 2$, $Y = (2, 5)$, $W = (2, 3)$, $W_{-2} = 0$, $W_{-1} = 1$. Odmah je $\mathrm{nxt} = 1$ za oba, $t^* = 0$; period od $001001$ je $3$, odgovor $3$.</p>
<p>$0001111$: $m = 4 > 3.5$, pa obrat i komplement daju $0000111$, $m = 3$, $Y = (4, 5, 6)$, $W = (4, 3, 2)$ i $W_{-3..-1} = (3, 2, 1)$. Vrijednosti $\mathrm{nxt}_{-3} = 3$, $\mathrm{nxt}_{-2} = 2$, $\mathrm{nxt}_{-1} = 1$ daju $t^* = 2$. Položaji u trenutku $2$: $y_j = -2 + 2j + \max_{[j-2, j]} W = 2, 4, 6$, niz $0010101$ ima period $7$; odgovor $2 + 7 = 9$.</p>

<h3>Veza sa službenim rješenjem</h3>
<p>Službeno rješenje govori o blokovima: blok nula duljine $\ge 2$ putuje ulijevo, blok jedinica udesno, sudar oba skraćuje. U jeziku čestica isto je: unutar bloka jedinica samo prva (lijeva) čestica napreduje, a zaglavljene čestice su upravo one koje čekaju iza nje; $t^*$ je trenutak zadnjeg sudara. Formulacija preko $W$ i $\mathrm{nxt}$ samo izbjegava eksplicitno praćenje blokova stogom.</p>

<h3>Zamke</h3>
<ul>
    <li>Ne zaboravi slučaj $2m > n$; bez transformacije $\mathrm{nxt}_i$ ne mora postojati unutar $m$ indeksa.</li>
    <li>Indekse $W$ pomakni za $+m$ pri pohrani (negativni indeksi), a položaje $y_j$ svedi na $[0, n)$ s pravilnim rukovanjem negativnih ostataka.</li>
    <li>Period niza računaj na nizu u trenutku $t^*$, a ne na početnom.</li>
</ul>
''',
    'verified': r'''uzorak 1/1 (3 niza); 300 slučajnih testova (nizovi duljine $\le 12$) protiv brute forcea koji simulira proces do prvog ponavljanja; dodatno iscrpno svi binarni nizovi duljine $\le 13$; 3 velika testa (jedan niz od $10^7$ znakova, odnosno $10^6$ nizova) do $0.22$ s.''',
},
# ---------------------------------------------------------------- C
{
    'letter': 'C', 'title': 'Best Carry Player 2', 'title_hr': 'Najbolji igrač s prijenosom 2', 'slug': 'C_best_carry_player_2',
    'tl': '4 s', 'ml': '1024 MB',
    'statement': r'''
<p>Dan je pozitivan cijeli broj $x$. Pronađi najmanji pozitivan cijeli broj $y$ takav da pri pisanom zbrajanju $x + y$ u dekadskom sustavu (znamenku po znamenku, kao u osnovnoj školi) nastane točno $k$ prijenosa.</p>
<h3>Ulaz</h3>
<p>Prvi redak sadrži broj testnih primjera $T$ ($1 \le T \le 10^5$). Svaki testni primjer sadrži dva cijela broja $x$ i $k$ ($1 \le x < 10^{18}$, $0 \le k \le 18$).</p>
<h3>Izlaz</h3>
<p>Za svaki testni primjer ispiši traženi $y$, ili $-1$ ako rješenje ne postoji.</p>
<h3>Primjer</h3>
<p>Za $x = 12345678$ i $k = 0, 5, 18$ odgovori su $1$, $54322$ i $999999999987654322$; za $x = 990099$, $k = 5$ odgovor je $9910$.</p>
''',
    'hints': [
        r'''<p>Prijenos na nekoj poziciji ovisi samo o znamenkama $x$ i $y$ na toj poziciji i o tome je li došao prijenos s niže pozicije. To je klasična postavka za <em>DP po znamenkama</em>.</p>''',
        r'''<p>Najmanji $y$ znači: što manje znamenki, a zatim leksikografski najmanje od najviše znamenke. Za svako stanje (pozicija, broj dosad ostvarenih prijenosa, dolazi li prijenos) pamti najmanju vrijednost sufiksa $y$ koja ga ostvaruje.</p>''',
        r'''<p>Pazi na rubne slučajeve: $y$ mora biti pozitivan (poseban slučaj $k = 0$ kad $x$ završava nizom devetki), a odgovor može premašiti $10^{18}$ — npr. $x = 10^{17}$, $k = 18$. Ukloni završne nule iz $x$ ili koristi 128-bitne cijele brojeve.</p>''',
    ],
    'coach': [
        ('O čemu ovisi hoće li na poziciji $i$ nastati prijenos, i što se od odluke na toj poziciji „vidi” dalje?',
         r'''
<p>Prijenos na poziciji $i$ nastaje točno kad je $x_i + y_i + c_i \ge 10$, gdje je $c_i \in \{0, 1\}$ prijenos s niže pozicije. Jedino što viša pozicija vidi jest bit $c_{i+1}$. Ukupan broj prijenosa je zbroj po pozicijama. To je točno oblik u kojem se koristi <em>DP po znamenkama</em>: stanje je (pozicija, broj dosad nastalih prijenosa, ulazni prijenos).</p>
'''),
        ('Kako u DP-u osigurati da je $y$ najmanji, a ne samo da postoji?',
         r'''
<p>Obrađujemo pozicije od najniže prema najvišoj i za svako stanje pamtimo najmanji broj sastavljen od dosad odabranih znamenaka. Dva izbora koja vode u isto stanje imaju identičnu budućnost (iste dopuštene nastavke na višim pozicijama), a viša pozicija dodaje isti iznos objema granama, pa je manji djelomični broj uvijek bolji. Na pojedinoj poziciji dovoljno je isprobati dvije znamenke: najmanju koja ne stvara prijenos ($0$) i najmanju koja ga stvara ($10 - x_i - c_i$).</p>
'''),
        ('Zašto rješenje može imati više znamenaka od $x$, i koliko najviše?',
         r'''
<p>Iznad najviše znamenke od $x$ sve su znamenke $x$ nule. Ondje prijenos nastaje samo ako je $y_i = 9$ i dolazi prijenos odozdo — ali svaki takav korak <em>jest</em> jedan prijenos, kojih je najviše $k \le 18$. Dakle znamenke od $y$ sežu najviše do pozicije $17 + 17 = 34$, tj. $y$ ima do $35$ znamenaka i odgovor je reda $10^{35}$ (npr. $x = 10^{17}$, $k = 18$ daje $y = 10^{35} - 10^{17}$: $18$ devetki iza kojih slijedi $17$ nula). 64 bita nije dovoljno: koristi <code>__int128</code> ili ukloni završne nule od $x$.</p>
'''),
        ('Kako riješiti uvjet $y > 0$ bez posebnog slučaja izvan DP-a?',
         r'''
<p>Dodaj u stanje bit „je li $y$ već pozitivan”. Na poziciji na kojoj prijenos ne želimo, uz znamenku $0$ isprobaj i znamenku $1$ (ako ne izaziva prijenos, tj. $x_i + c_i \le 8$); ona postavlja bit. Znamenka koja stvara prijenos uvijek je $\ge 1$, pa također postavlja bit. Na kraju uzmi najbolje stanje s točno $k$ prijenosa i postavljenim bitom — time je i slučaj $k = 0$ pokriven automatski.</p>
'''),
    ],
    'tips': [
        r'''Zadaci o pisanom zbrajanju, prijenosima i zbroju znamenaka gotovo su uvijek DP po znamenkama sa stanjem (pozicija, prijenos, brojač); minimizaciju broja postiži obradom od najniže znamenke uz pamćenje najmanje djelomične vrijednosti po stanju.''',
        r'''Prije kodiranja procijeni najveći mogući odgovor na ekstremnom ulazu (ovdje $x = 10^{17}$, $k = 18$) — to otkriva potrebu za 128-bitnim brojevima prije nego što padne test.''',
        r'''Uvjete poput „$y$ mora biti pozitivan” najčišće je ubaciti u stanje DP-a kao dodatni bit umjesto naknadnih posebnih slučajeva.''',
        r'''Kad je broj testova velik ($10^5$) a DP malen, drži tablicu statičnom i resetiraj samo potrebne slojeve; $10^5 \cdot 37 \cdot 19 \cdot 4$ prijelaza je ispod $3 \cdot 10^8$ jednostavnih operacija.''',
    ],
    'solution': r'''
<p>Zadatak rješavamo dinamičkim programiranjem po znamenkama, od više znamenke prema nižoj: $dp[i][j][c]$ označava stanje u kojem smo obradili pozicije do $i$-te, ukupno je nastalo $j$ prijenosa, a $c$ kaže dolazi li s nižih pozicija prijenos na trenutnu poziciju. U svakom koraku odlučujemo hoće li na sljedećoj poziciji nastati prijenos ili ne, i u oba slučaja upisujemo najmanju znamenku $y$ koja to postiže (bez prijenosa to je $0$, s prijenosom $10 - x_i - c$; ako je $x_i + c \ge 10$, prijenos nastaje neovisno o znamenci). Za svako stanje pamtimo najmanji dosad izgrađeni broj.</p>
<p>Vremenska složenost je $O(\log^2 x)$ po testnom primjeru.</p>
<p>Treba paziti na nekoliko rubnih slučajeva:</p>
<ul>
    <li>$y$ mora biti pozitivan, pa slučaj $k = 0$ zahtijeva jednostavnu posebnu obradu (najmanja potencija broja $10$ na čijoj poziciji $x$ nema znamenku $9$);</li>
    <li>odgovor može premašiti $10^{18}$, npr. za $x = 10^{17}$ i $k = 18$. To rješavamo tako da prije računanja uklonimo sve završne nule broja $x$ (one nikad ne sudjeluju u prijenosu) i na kraju ih ponovno dopišemo, ili jednostavno koristimo 128-bitne cijele brojeve.</li>
</ul>
''',
    'detailed': r'''
<h3>Lokalnost prijenosa</h3>
<p>Neka su $x_i$ i $y_i$ znamenke na poziciji $i$ (pozicija $0$ je najniža), a $c_i \in \{0, 1\}$ prijenos koji na poziciju $i$ dolazi s niže pozicije ($c_0 = 0$). Prijenos s pozicije $i$ na $i + 1$ nastaje točno onda kad je $x_i + y_i + c_i \ge 10$. Odluka o $y_i$ utječe na više pozicije isključivo preko jednog bita $c_{i+1}$, a ukupan broj prijenosa je zbroj po pozicijama. To je upravo struktura koju rješava <em>dinamičko programiranje po znamenkama</em>.</p>

<h3>Koliko pozicija treba razmatrati</h3>
<p>Broj $x < 10^{18}$ ima znamenke na pozicijama $0, \dots, 17$; iznad toga je $x_i = 0$. Na takvoj poziciji prijenos nastaje samo ako je $c_i = 1$ i $y_i = 9$ — no tada je taj korak sam po sebi jedan od najviše $k \le 18$ prijenosa. Ako prvi prijenos nastane na poziciji $17$, preostalih $17$ prijenosa kroz nule od $x$ zauzima pozicije $18, \dots, 34$, pa znamenke od $y$ sežu najviše do pozicije $34$ ($35$ znamenaka; za $x = 10^{17}$, $k = 18$ odgovor je $10^{35} - 10^{17}$). Radi jednostavnosti obrađujemo pozicije $0, \dots, 36$ — $10^{37}$ još stane u <code>__int128</code> ($< 1.7 \cdot 10^{38}$), dok 64 bita ($< 9.3 \cdot 10^{18}$) očito nije dovoljno. Alternativa je ukloniti završne nule od $x$ (one s $y_i = 0$ nikad ne prave prijenos) i na kraju ih dopisati — no tada treba pažljivo ispisati broj s vodećim dijelom i nulama, pa je 128-bitna aritmetika jednostavnija.</p>

<h3>Stanje i prijelazi</h3>
<p>Definirajmo $dp[i][j][c][z]$ = najmanja vrijednost $\sum_{t < i} y_t 10^t$ (dosad izgrađeni niži dio broja $y$) takva da je na pozicijama $0, \dots, i-1$ nastalo točno $j$ prijenosa, prema poziciji $i$ ide prijenos $c$, a $z = 1$ ako je neka odabrana znamenka bila različita od nule ($y > 0$). Početno $dp[0][0][0][0] = 0$. Za poziciju $i$ uz $s = x_i + c$:</p>
<ul>
    <li>ako je $s \le 9$: znamenka $0$ ne stvara prijenos ($\to dp[i+1][j][0][z]$); znamenka $1$ također ne stvara prijenos ako je $s \le 8$, ali postavlja $z = 1$ ($+10^i$); znamenka $10 - s$ ($\ge 1$) stvara prijenos ($\to dp[i+1][j+1][1][1]$, $+ (10 - s) 10^i$), dopušteno ako je $j < k$;</li>
    <li>ako je $s = 10$ (tj. $x_i = 9$ i $c = 1$): prijenos nastaje neovisno o znamenci, najmanja je $0$ ($\to dp[i+1][j+1][1][z]$).</li>
</ul>
<p>Odgovor je $\min(dp[37][k][0][1], dp[37][k][1][1])$, odnosno $-1$ ako su oba beskonačna.</p>

<h3>Zašto je dovoljno isprobati samo dvije znamenke po poziciji i zašto je „min po stanju” ispravan</h3>
<p>Sve znamenke $y_i$ koje vode u isto sljedeće stanje $(j', c', z')$ imaju potpuno jednaku budućnost: dopušteni nastavci na višim pozicijama ovise samo o stanju, a doprinos viših pozicija je isti za sve grane. Konačna vrijednost je (niži dio) $+$ (viši dio), pa među granama u istom stanju pobjeđuje ona s najmanjim nižim dijelom — što opravdava pamćenje minimuma po stanju. Unutar iste klase („bez prijenosa” ili „s prijenosom”) najmanja znamenka daje najmanji niži dio; jedina iznimka je bit $z$, zbog kojeg uz $0$ probamo i $1$. Veće znamenke nikad nisu potrebne.</p>
<p>Napomena o usporedbi: za dva broja s različitim brojem znamenaka usporedba „po vrijednosti” automatski preferira kraći, pa nije potrebno posebno minimizirati duljinu.</p>

<h3>Rubni slučajevi</h3>
<ul>
    <li>$k = 0$: tražimo najmanji pozitivan $y$ bez ijednog prijenosa; DP ga nalazi kao $10^t$ za najmanju poziciju $t$ na kojoj je $x_t \le 8$ (npr. $x = 999$, $k = 0$ daje $y = 1000$).</li>
    <li>Nemoguć slučaj: $k$ prijenosa ne može nastati ako ih ni s najboljim izborom ne možemo nanizati — u praksi se za $k \le 18$ uvijek može (npr. $y = 10^{36} - x$ daje $36$ prijenosa u nizu, a manje se postiže ranijim prekidom lanca), pa se $-1$ ne pojavljuje; ipak ga ispisujemo ako je stanje nedostižno.</li>
    <li>Prijenos kroz devetke od $x$ ne košta znamenku (znamenka $0$), što DP prirodno iskorištava: za $x = 990099$, $k = 5$ dobiva se $y = 9910$ — prijenosi na pozicijama $1, 2$ (znamenke $1$ i $9$), zatim kroz $0$ i dvije devetke.</li>
</ul>

<h3>Primjer</h3>
<p>$x = 12345678$, $k = 5$: najjeftinije je pokrenuti lanac od najniže pozicije: $y_0 = 2$ ($8 + 2 = 10$), zatim $y_1 = 2$ ($7 + 2 + 1$), $y_2 = 3$, $y_3 = 4$, $y_4 = 5$ — pet prijenosa, a na poziciji $5$ dolazi prijenos uz $x_5 = 3$ i $y_5 = 0$, bez novog prijenosa. Dobivamo $y = 54322$. Pokretanje lanca više (npr. od pozicije $1$) dalo bi više znamenki ili veće znamenke.</p>

<h3>Složenost</h3>
<p>Po testu $37 \cdot 19 \cdot 2 \cdot 2$ stanja s $O(1)$ prijelaza, tj. oko $3000$ operacija; za $T = 10^5$ ukupno oko $3 \cdot 10^8$ vrlo jednostavnih operacija na 128-bitnim brojevima, što je unutar $4$ s (lokalno $0.3$ s). Memorija je zanemariva (dva sloja tablice).</p>
''',
    'verified': r'''uzorak 1/1; 300 slučajnih testova ($x \le 999$, $k \le 3$) protiv brute forcea koji isprobava $y = 1, 2, 3, \dots$ i izravno broji prijenose; 3 velika testa s $T = 10^5$ (uključujući $x$ oblika $10^t$ i $99\ldots9$ te $k = 18$), najviše $0.27$ s.''',
},
# ---------------------------------------------------------------- D
{
    'letter': 'D', 'title': 'Minimum Suffix', 'title_hr': 'Najmanji sufiks', 'slug': 'D_minimum_suffix',
    'tl': '3 s', 'ml': '1024 MB',
    'statement': r'''
<p>Za niz $s$ duljine $n$ definiramo $p_j = x$ ako je $s[x \dots j]$ najmanji sufiks prefiksa $s[1 \dots j]$, za sve $j = 1, \dots, n$. (Sufiks je najmanji ako je leksikografski manji od svih ostalih sufiksa tog niza.)</p>
<p>Iz zadanih $p_1, \dots, p_n$ rekonstruiraj $s$. Ako postoji više rješenja, ispiši leksikografski najmanje. Znakovi niza $s$ prikazuju se pozitivnim cijelim brojevima; manji broj znači manji znak.</p>
<h3>Ulaz</h3>
<p>Prvi redak sadrži broj testnih primjera $T$ ($1 \le T \le 10^5$). Svaki testni primjer sadrži $n$ ($1 \le n \le 3 \cdot 10^6$) i zatim $p_1, \dots, p_n$ ($1 \le p_i \le i$). Zbroj svih $n$ ne prelazi $3 \cdot 10^6$.</p>
<h3>Izlaz</h3>
<p>Za svaki testni primjer ispiši $-1$ ako rješenje ne postoji, inače leksikografski najmanji $s$. Preporučuje se brzo čitanje i pisanje.</p>
<h3>Primjer</h3>
<p>Za $p = [1, 1, 1]$ odgovor je $1\ 2\ 2$; za $p = [1, 1, 2]$ odgovor je $-1$; za $p = [1, 2, 3]$ odgovor je $1\ 1\ 1$.</p>
''',
    'hints': [
        r'''<p>Izravan problem (dan $s$, traži se $p$) rješava se <em>Lyndonovom faktorizacijom</em> i Duvalovim algoritmom u linearnom vremenu. Razmisli što Duvalov algoritam radi s vrijednostima $p_j$: kada je $p_j$ jednak nekom ranijem $p$, a kada „skoči”?</p>''',
        r'''<p>Niz $p$ zapravo opisuje Lyndonovu faktorizaciju svakog prefiksa: $p_j = p_{j-1}$ znači da se trenutni Lyndonov faktor nastavlja, a $p_j = j$ znači da počinje novi faktor. Iz toga se dobivaju relacije oblika „$s[a] = s[b]$” i „$s[a] < s[b]$” među znakovima.</p>''',
        r'''<p>Unutar jednog Lyndonovog faktora sve relacije idu „prema naprijed” (uspoređuju se pozicije s početkom faktora), pa se faktor može puniti greedy slijeva nadesno. Između faktora vrijedi da je svaki faktor $\ge$ sljedećeg — obradi ih zdesna nalijevo.</p>''',
    ],
    'coach': [
        ('Kako bismo riješili izravan problem — za dani niz naći početak najmanjeg sufiksa svakog prefiksa? Što nam to govori o inverznom?',
         r'''
<p>Najmanji sufiks niza je posljednji faktor njegove Lyndonove faktorizacije $s = w_1 w_2 \cdots w_k$ ($w_1 \ge w_2 \ge \dots \ge w_k$, svaki $w_i$ Lyndonova riječ). Duvalov algoritam faktorizaciju računa slijeva nadesno održavajući „pre-Lyndonov” segment $u^t u'$ i uspoređujući svaki novi znak sa znakom jedan period ranije. Ako nam je dan $p$, možemo taj algoritam „odvrtjeti unatrag”: svaki $p_m$ govori koja se od tri grane usporedbe dogodila, a to je relacija među dva znaka.</p>
'''),
        ('Gdje su granice Lyndonovih faktora cijelog niza?',
         r'''
<p>$p_n$ je početak posljednjeg faktora $w_k$. Prefiks $s[1..p_n - 1]$ ima faktorizaciju $w_1 \cdots w_{k-1}$, pa je $p_{p_n - 1}$ početak $w_{k-1}$, i tako dalje. Granice su dakle jednoznačno određene: $e = n$, $b = p_e$, $e \leftarrow b - 1$, … To ujedno nameće $p_e = b$ za svaki kraj faktora i $p_b = b$ za svaki početak (jednoslovna riječ je Lyndonova).</p>
'''),
        ('Što unutar faktora $[b, e]$ znači $p_m = b$, a što $p_m = p_{m-P} + P$?',
         r'''
<p>Prefiks $s[b..m]$ Lyndonove riječi $w$ ima oblik $u^t u'$ s periodom $P = |u|$. Ako je $s[m] > s[m - P]$, cijeli $s[b..m]$ postaje Lyndonova riječ i najmanji sufiks prefiksa $s[1..m]$ počinje na $b$ (jer je $s[b..m] \le w \le w_{k'}$ za prethodne faktore); novi period je $m - b + 1$. Ako je $s[m] = s[m - P]$, struktura $u^t u'$ se nastavlja i najmanji sufiks je najmanji sufiks od $u'$, koji se zbog periodičnosti nalazi točno $P$ mjesta iza onoga za prefiks $s[1..m-P]$: $p_m = p_{m-P} + P$. Slučaj $s[m] < s[m-P]$ zatvorio bi faktor prije $e$, pa je nemoguć. Svaki drugi $p_m$ (npr. $p_m < b$) je proturječje i odgovor je $-1$.</p>
'''),
        ('Zašto greedy slijeva nadesno unutar faktora daje najmanju riječ, i zašto faktore obrađujemo zdesna nalijevo?',
         r'''
<p>Sve relacije unutar faktora glase „$s[m] = s[r]$” ili „$s[m] > s[r]$” s $r < m$, pa su pri obradi pozicije $m$ sve referirane vrijednosti već poznate i najmanji dopušteni znak je $s[r]$ odnosno $s[r] + 1$; svaki veći izbor daje leksikografski veću riječ bez koristi. Između faktora vrijedi $w_j \ge w_{j+1}$. Funkcija „najmanja riječ koja poštuje relacije i $\ge v$” je monotona u $v$, pa minimizacija $w_k$, zatim $w_{k-1} \ge w_k$, … daje svaki faktor pojedinačno najmanji mogući — a to je istodobno i leksikografski najmanji cijeli niz.</p>
'''),
        ('Kako u linearnom vremenu naći najmanju riječ koja poštuje relacije i nije manja od zadane $v$?',
         r'''
<p>Prati $v$ znak po znak dok je to moguće (na „slobodnim” pozicijama s relacijom „$>$” stavi točno $v_m$ ako je dopušteno, na „kopirajućim” provjeri jednakost). Ako u nekom trenutku najmanji dopušteni znak premaši $v_m$ ili je $v$ pravi prefiks od $w$, ostatak popuni najmanjim znakovima — riječ je već veća. Ako kopirajuća pozicija prisilno daje znak manji od $v_m$ ili je $w$ pravi prefiks od $v$, vrati se na <em>posljednju slobodnu</em> poziciju na kojoj smo se poklopili s $v$, povećaj ondje znak za $1$ i ostatak popuni najmanjim znakovima. Početak faktora je uvijek slobodan, pa takva pozicija postoji.</p>
'''),
    ],
    'tips': [
        r'''„Najmanji sufiks svakog prefiksa”, „najmanja ciklička rotacija” i „Lyndonova faktorizacija” su isti krug ideja: najmanji sufiks je posljednji Lyndonov faktor, a Duvalov algoritam sve to računa u $O(n)$. Kad vidiš inverzni zadatak, odvrti algoritam unatrag i pretvori svaki korak u relaciju među znakovima.''',
        r'''Relacije koje sve pokazuju „unatrag” (na ranije pozicije) rješavaju se greedyjem slijeva nadesno; ako između blokova vrijedi lanac $\ge$, obradi blokove zdesna nalijevo — minimiziranje desnih blokova nikad ne šteti lijevima zbog monotonosti.''',
        r'''Za „najmanju riječ $\ge v$ uz ograničenja” standardni je obrazac: prati $v$ dok možeš, a pri neuspjehu se vrati na posljednju poziciju gdje si smio odabrati veći znak. Pamti tu poziciju tijekom prolaza umjesto da tražiš unatrag.''',
        r'''Kad brute force lako računa izravan problem (ovdje $p$ iz $s$), testiraj inverzno rješenje tako da za sve nizove male duljine izračunaš $p$, grupiraš po $p$ i usporediš s najmanjim $s$ u grupi — to hvata i pogrešne $-1$.''',
    ],
    'solution': r'''
<p>Razmotrimo najprije izravan problem: za dani niz odrediti najmanji sufiks svakog prefiksa. To se rješava teorijom <strong>Lyndonove faktorizacije</strong>: niz se rastavlja na Lyndonove riječi (riječi koje su strogo manje od svih svojih netrivijalnih cikličkih pomaka) tako da je svaka riječ veća ili jednaka sljedećoj, a Duvalov algoritam faktorizaciju računa u linearnom vremenu. Najmanji sufiks prefiksa uvijek počinje na početku njegova posljednjeg Lyndonovog faktora.</p>
<p>U našem je zadatku dano rješenje izravnog problema. Prateći korake Duvalova algoritma prema zadanim vrijednostima $p$, niz možemo prikazati kao slijed Lyndonovih riječi, pri čemu unutar svake riječi dobivamo relacije jednakosti i stroge nejednakosti među znakovima. Primjerice, za $p = [1, 2, 1, 4, 1]$ dobivamo $s_1 = s_2 < s_3$ i $s_1 = s_4 < s_5$. Između susjednih riječi vrijedi da je prethodna riječ veća ili jednaka sljedećoj. Ako je skup relacija proturječan, rješenje ne postoji.</p>
<p>Budući da tražimo leksikografski najmanji niz, unutar svake riječi znakove biramo greedy slijeva nadesno, a između riječi greedy zdesna nalijevo: za svaku riječ odabiremo najmanji niz koji je leksikografski veći ili jednak sljedećoj riječi. Zbog strukture Lyndonovih riječi sve relacije „manje” usmjerene su prema naprijed, pa se i ovdje znakovi mogu određivati jedan po jedan.</p>
<p>Vremenska složenost je $O(n)$.</p>
''',
    'detailed': r'''
<h3>Izravan problem i Lyndonova faktorizacija</h3>
<p>Riječ je <em>Lyndonova</em> ako je strogo manja od svih svojih netrivijalnih cikličkih pomaka (ekvivalentno: strogo manja od svih svojih pravih sufiksa). Svaki niz ima jedinstvenu <em>Lyndonovu faktorizaciju</em> $s = w_1 w_2 \cdots w_k$ u Lyndonove riječi s $w_1 \ge w_2 \ge \dots \ge w_k$. Ključna činjenica: <strong>najmanji sufiks niza je njegov posljednji Lyndonov faktor $w_k$</strong>. (Svaki sufiks koji počinje unutar $w_j$ za $j < k$ počinje pravim sufiksom od $w_j$, koji je $> w_j \ge w_k$, a sufiks koji počinje unutar $w_k$ je pravi sufiks od $w_k$, dakle $> w_k$.)</p>
<p>Duvalov algoritam gradi faktorizaciju slijeva nadesno: održava početak $b$ trenutnog segmenta i njegov najmanji period $P$, tako da je $s[b..m-1] = u^t u'$ ($|u| = P$, $u$ Lyndonova, $u'$ pravi prefiks od $u$). Za novi znak uspoređuje $s[m]$ i $s[m-P]$: ako su jednaki, oblik $u^t u'$ se nastavlja; ako je $s[m] > s[m-P]$, cijeli $s[b..m]$ postaje Lyndonova riječ i period postaje $m - b + 1$; ako je $s[m] < s[m-P]$, izdvaja se $t$ kopija riječi $u$ kao faktori i algoritam nastavlja od početka $u'$.</p>

<h3>Što $p$ govori o nizu</h3>
<p><strong>Granice faktora.</strong> $p_n$ je početak $w_k$. Prefiks $s[1..p_n - 1]$ ima faktorizaciju $w_1 \cdots w_{k-1}$, pa je $p_{p_n - 1}$ početak $w_{k-1}$ itd. Granice dobivamo petljom $e = n$, $b = p_e$, $e \leftarrow b - 1$, dok $e \ge 1$.</p>
<p><strong>Relacije unutar faktora $[b, e]$.</strong> Za $m \in [b, e]$ prefiks $s[b..m]$ je prefiks Lyndonove riječi $w = s[b..e]$, dakle oblika $u^t u'$ s periodom $P$ (na početku $P = 1$). Prefiks $s[1..m]$ cijelog niza ima faktorizaciju $w_1 \cdots w_{k'}\, u \cdots u\, (\text{faktorizacija } u')$, pa njegov najmanji sufiks počinje unutar $[b, m]$; točnije:</p>
<ul>
    <li>ako je $s[m] > s[m-P]$, tada je $s[b..m]$ Lyndonova riječ; kako je $s[b..m] \le w \le w_{k'}$, ona je posljednji faktor prefiksa i $p_m = b$; novi period je $P \leftarrow m - b + 1$;</li>
    <li>ako je $s[m] = s[m-P]$, oblik $u^t u'$ se nastavlja; najmanji sufiks prefiksa $s[1..m]$ je najmanji sufiks od $u'$ (ili posljednja kopija $u$ kad je $u'$ prazan), a isto vrijedi za $s[1..m-P]$ s $u'$ za jedan period ranije, pa je $p_m = p_{m-P} + P$;</li>
    <li>slučaj $s[m] < s[m-P]$ zatvorio bi faktor prije $e$, što je u suprotnosti s granicom faktora.</li>
</ul>
<p>Obratno, iz $p_m$ čitamo relaciju: $p_m = b$ znači „$s[m] > s[m-P]$” (pozicija $m$ je <em>slobodna</em>), $p_m = p_{m-P} + P$ znači „$s[m] = s[m-P]$” (pozicija je <em>kopija</em>), a svaka druga vrijednost (uključujući $p_m < b$ ili $p_b \ne b$) je proturječje i odgovor je $-1$. Ta dva slučaja se ne mogu preklopiti jer bi $p_{m-P} + P = b$ zahtijevalo $p_{m-P} < b$. Napomena: nije potrebno provjeravati je li dobiveni niz doista Lyndonov — relacije su upravo uvjet da Duval nikad ne zatvori faktor prije $e$, a na kraju $p_e = b$ jamči da je $s[b..e]$ Lyndonova riječ.</p>
<p>Primjer (iz službenog rješenja): $p = [1, 2, 1, 4, 1]$ daje jedan faktor $[1, 5]$ i relacije $s_2 = s_1$ ($P = 1$), $s_3 > s_2$ ($P \leftarrow 3$), $s_4 = s_1$, $s_5 > s_2$; najmanji niz je $1\,1\,2\,1\,2$.</p>

<h3>Uvjet između faktora i redoslijed obrade</h3>
<p>Faktori moraju zadovoljavati $w_1 \ge w_2 \ge \dots \ge w_k$ (jednakost dopuštena). Ako su relacije unutar faktora konzistentne i taj lanac vrijedi, niz $w_1 \cdots w_k$ ima točno tu Lyndonovu faktorizaciju, pa svi $p_i$ odgovaraju zadanima — konstrukcija je ispravna, a rješenje postoji uvijek kad nema unutarnjeg proturječja (znakovi su neograničeni pozitivni brojevi, pa se svaki $w_j$ može povećati koliko treba).</p>
<p>Sve relacije unutar faktora referiraju ranije pozicije, pa je za fiksni donji uvjet „$w \ge v$” najmanja riječ određena greedyjem slijeva nadesno. Funkcija $v \mapsto \min\{ w : w \text{ poštuje relacije},\ w \ge v \}$ je monotona. Zato faktore obrađujemo <strong>zdesna nalijevo</strong>: $w_k$ je najmanja riječ bez donjeg uvjeta, $w_{k-1}$ najmanja riječ $\ge w_k$, … Svaki faktor time dobiva najmanju vrijednost koju uopće može imati u nekom valjanom rješenju, a niz sastavljen od pojedinačno najmanjih faktora je leksikografski najmanji.</p>

<h3>Najmanja riječ $\ge v$ uz relacije, u linearnom vremenu</h3>
<p>Za poziciju $m$ neka je $\mathrm{lo}(m)$ najmanja dopuštena vrijednost: $s[r]$ za kopiju, $s[r] + 1$ za slobodnu poziciju s referencom $r$, a $1$ za početak faktora. Prolazimo $m = b, b+1, \dots$ i pratimo $v$:</p>
<ol>
    <li>Ako je $v$ već iscrpljen ($v$ je pravi prefiks od $w$): $w > v$, ostatak popuni s $\mathrm{lo}$.</li>
    <li>Ako je $\mathrm{lo}(m) > v_m$: postavi $\mathrm{lo}(m)$, riječ je veća od $v$, ostatak popuni s $\mathrm{lo}$.</li>
    <li>Ako je pozicija slobodna i $\mathrm{lo}(m) \le v_m$: postavi $s[m] = v_m$ i zapamti $m$ kao <em>posljednju slobodnu poklopljenu</em> poziciju.</li>
    <li>Ako je pozicija kopija i $\mathrm{lo}(m) = v_m$: postavi $v_m$ i nastavi.</li>
    <li>Ako je pozicija kopija i $\mathrm{lo}(m) < v_m$, ili je $w$ završio kao pravi prefiks od $v$: $w$ ne može pratiti $v$ dalje, pa mora biti veći na nekoj ranijoj poziciji; najmanja takva promjena je na posljednjoj slobodnoj poklopljenoj poziciji $f$: postavi $s[f] = v_{f-b+1} + 1$ (dopušteno, jer slobodna pozicija prima svaku vrijednost $> s[r]$) i ostatak od $f + 1$ popuni s $\mathrm{lo}$ (kopije preuzimaju nove vrijednosti).</li>
</ol>
<p>Pozicija $b$ je slobodna i u koraku 3 uvijek postaje kandidat, pa $f$ postoji kad god je potreban. Svaki se korak izvodi $O(1)$ puta po poziciji, faktor se obrađuje u $O(|w|)$, a cijeli test u $O(n)$.</p>

<h3>Primjeri</h3>
<ul>
    <li>$p = [1, 1, 1]$: jedan faktor, $s_2 > s_1$ ($P \leftarrow 2$), $s_3 > s_1$; najmanje: $1\,2\,2$.</li>
    <li>$p = [1, 1, 2]$: faktori $[2, 3]$ i $[1, 1]$, ali $p_2 = 1 \ne 2$ — proturječje, $-1$.</li>
    <li>$p = [1, 2, 3]$: tri jednoslovna faktora, svaki $\ge$ sljedećeg: $1\,1\,1$.</li>
</ul>

<h3>Složenost i implementacija</h3>
<ul>
    <li>Vrijeme $O(n)$ po testu, ukupno $O(\sum n) = O(3 \cdot 10^6)$; memorija $O(n)$.</li>
    <li>Ulaz ima do $3 \cdot 10^6$ brojeva, a izlaz isto toliko — koristi <code>fread</code>/vlastiti ispis; <code>cin</code>/<code>cout</code> bez sinkronizacije mogu probiti $1$ s.</li>
    <li>Sve indekse drži 1-indeksirano kao u zadatku; referenca $r = m - P$ uvijek je $\ge b$, a „referenca $0$” označava početak faktora.</li>
    <li>Vrijednosti znakova rastu najviše za $1$ po povećanju i ostaju $\le n$, pa je <code>int</code> dovoljan.</li>
</ul>
''',
    'verified': r'''uzorak 1/1 (3 testa); 300 slučajnih testova protiv brute forcea koji za $n \le 6$ iscrpno prolazi sve nizove nad abecedom $\{1, \dots, n\}$, računa njihov $p$ i uzima najmanji niz s traženim $p$ (odnosno $-1$); 3 velika testa s $\sum n = 3 \cdot 10^6$ (najviše $0.13$ s).''',
},
# ---------------------------------------------------------------- E
{
    'letter': 'E', 'title': 'Map', 'title_hr': 'Karta', 'slug': 'E_map',
    'tl': '1 s', 'ml': '1024 MB',
    'statement': r'''
<p>Park $P$ je pravokutnik. Karta parka $M$ je manji (ili jednak) sličan pravokutnik položen unutar parka, zajedno s bijekcijom $f : M \to P$ koja je sličnost s koeficijentom $r$: $|f(a) - f(b)| = r\,|a - b|$ za sve $a, b \in M$. Karta može biti položena i „naopako” (zrcalno).</p>
<p>Mio se može teleportirati pomoću karte: kad je u točki $x$ na karti (uključujući rub), može se teleportirati u točku $f(x)$ parka; kad je u točki $y$ parka, može se teleportirati u točku $f^{-1}(y)$ na karti. Budući da je karta unutar parka, Mio koja stoji na karti istodobno je i u parku, pa se može teleportirati u oba smjera. Teleportirati se može najviše $n$ puta, svaki teleport traje $k$ sekundi, a hoda brzinom $1$.</p>
<p>Za dane točke $s$ i $t$ odredi najmanje vrijeme potrebno da Mio od $s$ dođe do $t$.</p>
<h3>Ulaz</h3>
<p>Prvi redak sadrži $T$ ($1 \le T \le 100$). Svaki testni primjer: četiri vrha parka (redom po obodu), četiri vrha karte (i-ti vrh karte odgovara i-tom vrhu parka, čime je određena i eventualna zrcalnost), točke $s$ i $t$ te cijeli brojevi $k$ i $n$ ($0 \le k \le 2 \cdot 10^6$, $0 \le n \le 100$). Sve su koordinate cijeli brojevi apsolutne vrijednosti do $2 \cdot 10^6$.</p>
<h3>Izlaz</h3>
<p>Za svaki test ispiši najmanje vrijeme; prihvaća se apsolutna ili relativna greška do $10^{-9}$.</p>
''',
    'hints': [
        r'''<p>Teleport iz parka na kartu ($f^{-1}$) skuplja udaljenosti faktorom $1/r$, teleport s karte u park ($f$) ih množi s $r$. Kad se isplati hodati — kad su udaljenosti male ili velike?</p>''',
        r'''<p>Pokaži zamjenom redoslijeda da je optimalno: najprije se iz $s$ teleportirati $i$ puta „u kartu” (smanjivanje), zatim hodati, pa se $j$ puta teleportirati „iz karte” (uvećavanje) do $t$. Hodanje u sredini jednako je hodanju $f^{-i}(s) \to f^{-j}(t)$.</p>''',
        r'''<p>Sličnost ravnine najlakše je zapisati kompleksnim brojevima: $f(z) = Az + b$ (uz očuvanu orijentaciju) ili $f(z) = A\bar z + b$ (zrcalna). Iz para odgovarajućih vrhova odredi $A$ i $b$.</p>''',
    ],
    'coach': [
        ('Što teleport radi s udaljenostima, a ne samo s točkama?',
         r'''
<p>Sličnost $f$ množi sve udaljenosti s $r \ge 1$, a $f^{-1}$ ih dijeli s $r$. Ako Mio stoji u $x$ i želi u $y$, nakon što <em>obje</em> točke preslikamo s $f^{-1}$ hodanje između njih traje $r$ puta kraće. Dakle teleport „u kartu” prije hodanja štedi vrijeme hodanja, ali košta $k$; teleport „iz karte” nakon hodanja samo vraća u prave koordinate cilja. Pitanje je koliko puta isplati skupljati.</p>
'''),
        ('Zašto ne bismo hodali između teleporta ili miješali smjerove teleporta?',
         r'''
<p>Argument zamjene: „hod pa $f^{-1}$” zamijeni s „$f^{-1}$ pa hod” — novi hod ide od $f^{-1}(x)$ do $f^{-1}(y)$, obje točke su na karti (konveksnoj), a duljina mu je $|x - y| / r \le |x - y|$. Simetrično, „$f$ pa hod” zamijeni s „hod pa $f$” — hod od $x$ do $f^{-1}(y)$ ostaje na karti i kraći je $r$ puta. Ponavljanjem sve hodanje skupimo u jedan blok; teleporti prije bloka bez hodanja među njima ne smiju sadržavati par $f^{-1}f$ ili $ff^{-1}$ (identitet uz cijenu $2k$), a zadnji je $f^{-1}$, pa su svi $f^{-1}$; simetrično su svi nakon bloka $f$. Optimalan put je oblika $s \xrightarrow{(f^{-1})^i} \cdot \xrightarrow{\text{hod}} \cdot \xrightarrow{f^j} t$.</p>
'''),
        ('Kako iz oblika puta dobiti formulu i koliko kandidata treba provjeriti?',
         r'''
<p>Hod u sredini vodi od $s_i = f^{-i}(s)$ do točke koja nakon $j$ teleporta $f$ završi u $t$, dakle do $t_j = f^{-j}(t)$. Ukupno vrijeme je $(i + j)k + |s_i - t_j|$ uz $i + j \le n$, $i, j \ge 0$. Slučaj $i = j = 0$ je čisto hodanje. Kandidata je $O(n^2) \le 5151$, pa ih sve isprobamo; točke $s_i$, $t_j$ dobivamo uzastopnim primjenama $f^{-1}$.</p>
'''),
        ('Kako iz četiriju parova vrhova dobiti $f$, uključujući zrcalnu kartu?',
         r'''
<p>Svaka sličnost ravnine je $f(z) = Az + b$ (čuva orijentaciju) ili $f(z) = A\bar z + b$ (zrcalna), $A, b \in \mathbb{C}$. Orijentaciju očitamo iz predznaka vektorskog produkta $(P_2 - P_1) \times (P_3 - P_1)$ i istoga za kartu: različiti predznaci znače zrcaljenje. Zatim $A = (P_2 - P_1) / (M_2 - M_1)$ (u zrcalnom slučaju s $\overline{M_2 - M_1}$) i $b = P_1 - A M_1$ (odnosno $P_1 - A \overline{M_1}$). Inverz je $f^{-1}(w) = (w - b)/A$, u zrcalnom slučaju konjugiran.</p>
'''),
    ],
    'tips': [
        r'''Kad operacija množi sve udaljenosti konstantom (skaliranje, sličnost), promatraj njen učinak na <em>cijeli preostali put</em>, a ne na trenutnu točku: „skupi prije hodanja, raširi poslije” je tipičan oblik optimuma, a dokazuje se zamjenom susjednih koraka.''',
        r'''Sličnosti ravnine zapisuj kompleksnim brojevima: kompozicija, inverz i zrcaljenje svode se na množenje, dijeljenje i konjugiranje; <code>std::complex&lt;long double&gt;</code> ima sve potrebno.''',
        r'''Kad je optimum tvrdnja o obliku rješenja, u brute forceu ne provjeravaj samo formulu — generiraj nasumične dopuštene strategije i potvrdi da nijedna nije bolja od odgovora.''',
        r'''Za zadatke s tolerancijom $10^{-9}$ i koordinatama do $10^6$ koristi <code>long double</code> i ispisuj $10$ decimala; broj iteracija kontrakcije ($f^{-1}$) ne gomila grešku.''',
    ],
    'solution': r'''
<p>Može se pokazati da je optimalan put uvijek ovog oblika: najprije se iz $s$ nekoliko puta teleportiramo „iz velikog u malo” (parka na kartu), zatim hodamo, a onda se nekoliko puta teleportiramo „iz malog u veliko” (s karte u park) i stignemo u $t$. Naime, ako bismo hodali negdje usred niza teleporta, taj bismo dio hodanja mogli premjestiti na kraj i to nikad ne bi bilo lošije.</p>
<p>Zadatak se tako svodi na sljedeće: iz $s$ se $i$ puta teleportiramo prema karti i dođemo u $s'$, iz $t$ se $j$ puta (unatrag) teleportiramo prema karti i dođemo u $t'$, te hodamo od $s'$ do $t'$; ukupno vrijeme je $(i + j)\,k + |s' - t'|$. Budući da je ograničenje na broj teleporta malo ($n \le 100$), sve parove $(i, j)$ s $i + j \le n$ možemo isprobati u $O(n^2)$.</p>
<p>Što se tiče računanja same sličnosti, najjednostavnije je koristiti kompleksne brojeve: svaka se sličnost ravnine može zapisati kao $f(z) = Az + b$ ili, ako mijenja orijentaciju, kao $f(z) = A\bar{z} + b$, pri čemu koeficijente $A$ i $b$ odredimo iz odgovarajućih vrhova karte i parka.</p>
''',
    'detailed': r'''
<h3>Sličnost i njezin učinak</h3>
<p>Karta je slika parka pod sličnošću $f^{-1}$ s koeficijentom $1/r$, gdje je $r = |P_2 - P_1| / |M_2 - M_1| \ge 1$. Za svake dvije točke $x, y$ parka vrijedi $|f^{-1}(x) - f^{-1}(y)| = |x - y| / r$, a za točke karte $|f(x) - f(y)| = r|x - y|$. Mio može teleport $f^{-1}$ primijeniti iz bilo koje točke parka (rezultat je na karti, dakle i u parku), a teleport $f$ samo s karte. Hodanje je najbrže po dužini, a park je konveksan, pa je vrijeme hodanja između dviju točaka jednako njihovoj udaljenosti.</p>

<h3>Oblik optimalnog puta</h3>
<p>Put je niz koraka: hodanja i teleporta dvaju tipova. Dvije zamjene ne povećavaju vrijeme:</p>
<ul>
    <li><strong>Hod pa $f^{-1}$</strong> ($x \to y \to f^{-1}(y)$) zamijenimo s <strong>$f^{-1}$ pa hod</strong> ($x \to f^{-1}(x) \to f^{-1}(y)$). Isti teleport, a hod duljine $|x - y|$ postaje $|x - y| / r$. Obje krajnje točke novog hoda su na karti, dakle u parku.</li>
    <li><strong>$f$ pa hod</strong> ($x \to f(x) \to y$, $x$ na karti) zamijenimo s <strong>hod pa $f$</strong> ($x \to f^{-1}(y) \to y$). Hod duljine $|f(x) - y|$ postaje $|x - f^{-1}(y)| = |f(x) - y| / r$; obje točke su na karti, karta je konveksna, pa je $f$ primjenjiv na kraju.</li>
</ul>
<p>Primjenjujući zamjene dok je moguće, sva hodanja stanu u jedan blok (dva susjedna hodanja spajamo u jedno, ne dulje). Teleporti prije bloka nemaju hodanja među sobom; dva susjedna različitog tipa ($f^{-1}f$ ili $ff^{-1}$) daju identitet uz cijenu $2k \ge 0$ pa ih izbacujemo. Neposredno prije bloka ne može biti $f$ (inače bismo još zamjenjivali), pa su svi teleporti prije bloka tipa $f^{-1}$; simetrično su svi nakon bloka tipa $f$. Zaključak: postoji optimalan put oblika</p>
<p>$$s \xrightarrow{(f^{-1})^{\,i}} f^{-i}(s) \xrightarrow{\text{hod}} f^{-j}(t) \xrightarrow{f^{\,j}} t, \qquad i, j \ge 0,\ i + j \le n,$$</p>
<p>čije je trajanje $(i + j)k + |f^{-i}(s) - f^{-j}(t)|$. Točka $f^{-j}(t)$ je na karti za $j \ge 1$ (potrebno za primjenu $f$), a za $j = 0$ nema teleporta na kraju. Sve su točke $f^{-i}(s)$ u parku, pa je hod dopušten. Time je i dokazano da je odgovor točno $\min_{i + j \le n}\bigl((i + j)k + |f^{-i}(s) - f^{-j}(t)|\bigr)$ — svaki kandidat je ostvariv, a optimum je među kandidatima.</p>
<p>Intuicija: teleporti „u kartu” prije hodanja dijele preostalu udaljenost s $r$ po $k$ sekundi; isplate se dok je ušteda $|d|(1 - 1/r)$ veća od $k$. No cilj $t$ također treba „skupiti”, a ne nužno isto puta kao $s$ — zato dva neovisna brojača $i$ i $j$.</p>

<h3>Određivanje sličnosti</h3>
<p>Točke tumačimo kao kompleksne brojeve. Svaka sličnost ravnine je oblika $f(z) = Az + b$ (čuva orijentaciju: rotacija + skaliranje + translacija) ili $f(z) = A\bar z + b$ (zrcalna). Orijentaciju četverokuta daje predznak vektorskog produkta $(P_2 - P_1) \times (P_3 - P_1)$; ako se za park i kartu razlikuju, karta je zrcalna. Iz prvih dvaju odgovarajućih vrhova:</p>
<ul>
    <li>bez zrcaljenja: $A = \dfrac{P_2 - P_1}{M_2 - M_1}$, $b = P_1 - A M_1$;</li>
    <li>zrcalno: $A = \dfrac{P_2 - P_1}{\overline{M_2 - M_1}}$, $b = P_1 - A\overline{M_1}$.</li>
</ul>
<p>Inverz: $f^{-1}(w) = (w - b)/A$, odnosno $\overline{(w - b)/A}$ u zrcalnom slučaju. Vrhovi su različiti, pa dijeljenje nulom nije moguće. Za provjeru se može potvrditi da $f$ preslikava sva četiri vrha karte u vrhove parka.</p>

<h3>Algoritam</h3>
<ol>
    <li>Odredi orijentaciju, $A$ i $b$.</li>
    <li>Izračunaj $s_0 = s$, $s_{i} = f^{-1}(s_{i-1})$ i $t_0 = t$, $t_j = f^{-1}(t_{j-1})$ za $i, j \le n$.</li>
    <li>Odgovor je $\min_{i + j \le n} \bigl((i + j)k + |s_i - t_j|\bigr)$.</li>
</ol>
<p>Složenost $O(n^2)$ po testu ($n \le 100$), memorija $O(n)$.</p>

<h3>Rubni slučajevi i preciznost</h3>
<ul>
    <li>$r = 1$ (karta jednaka parku): $f$ je izometrija, teleporti ne mijenjaju udaljenost i formula prirodno daje $|s - t|$ (uz $k = 0$ daje isti rezultat s teleportima).</li>
    <li>$k = 0$: teleporti su besplatni; formula automatski uzima $i = j = n$ ako to smanjuje hod (ne nužno — točke se skupljaju prema fiksnoj točki sličnosti pa udaljenost pada).</li>
    <li>$n = 0$: samo hodanje.</li>
    <li>Koordinate do $2 \cdot 10^6$ i udaljenosti do $\approx 5.7 \cdot 10^6$; <code>long double</code> daje relativnu grešku $\approx 10^{-19}$ po operaciji, a $f^{-1}$ je kontrakcija pa se greške ne gomilaju. Ispiši npr. $10$ decimala.</li>
    <li>Vrhovi su dani „redom po obodu”, ali orijentacija (u smjeru kazaljke ili obratno) može se razlikovati između parka i karte — upravo to označava zrcaljenje, pa ju treba računati, a ne pretpostavljati.</li>
</ul>

<h3>Primjer</h3>
<p>Park $[0, 6] \times [0, 3]$ s vrhovima $(0,0),(6,0),(6,3),(0,3)$, karta $(0,0),(2,0),(2,1),(0,1)$ ($r = 3$, $f(z) = 3z$), $s = (6, 3)$, $t = (0, 0)$, $k = 1$, $n = 2$. Bez teleporta hod traje $\sqrt{45} \approx 6.708$. S $i = 1$: $f^{-1}(s) = (2, 1)$, hod $\sqrt 5 \approx 2.236$, ukupno $3.236$. S $i = 2$: $(2/3, 1/3)$, hod $\approx 0.745$, ukupno $2.745$ — najbolje. Teleporti $t$-a ($j \ge 1$) ništa ne mijenjaju jer je $t$ fiksna točka.</p>
''',
    'verified': r'''uzorak 1/1; 300 slučajnih testova (slučajni slični pravokutnici s cjelobrojnim vrhovima, sa i bez zrcaljenja) uspoređeno preko <code>check.py</code> s tolerancijom $10^{-6}$ protiv neovisne Python implementacije (sličnost kao matrica skaliranja/rotacije/zrcaljenja provjerena na sva četiri vrha) koja dodatno potvrđuje da 300 nasumičnih dopuštenih strategija nikad nije brže od formule; 3 velika testa s $T = 100$, $n = 100$ ($0.01$ s).''',
},
# ---------------------------------------------------------------- F
{
    'letter': 'F', 'title': 'Inversion', 'title_hr': 'Inverzija', 'slug': 'F_inversion',
    'tl': '2 s', 'ml': '1024 MB',
    'statement': r'''
<p><em>Interaktivni zadatak.</em> Skrivena je permutacija $p_1, \dots, p_n$ skupa $\{1, \dots, n\}$. Upitom „? $l$ $r$” dobivaš parnost broja inverzija podniza $p_l, \dots, p_r$, tj. $\left(\sum_{l \le i < j \le r} [p_i > p_j]\right) \bmod 2$.</p>
<p>Odredi permutaciju s najviše $4 \cdot 10^4$ upita i ispiši je u obliku „! $p_1$ $p_2$ $\dots$ $p_n$”.</p>
<h3>Protokol</h3>
<p>Najprije pročitaj $n$ ($1 \le n \le 2000$). Nakon svakog upita pročitaj odgovor ($0$ ili $1$). Nakon svakog ispisa isprazni izlazni međuspremnik. Permutacija je unaprijed fiksirana.</p>
<h3>Primjer</h3>
<p>Za $n = 3$ i skrivenu permutaciju $2\ 3\ 1$: upiti „? 1 2”, „? 1 3”, „? 2 3” daju odgovore $0$, $0$, $1$.</p>
''',
    'hints': [
        r'''<p>Označi $f(l, r)$ = odgovor na upit. Izrazi $[p_l > p_r]$ preko $f$ na četiri intervala (princip uključivanja–isključivanja po inverzijama koje uključuju obje krajnje točke).</p>''',
        r'''<p>Usporedba dvaju elemenata košta do četiri upita; obično sortiranje ($n \log n$ usporedbi) time premašuje limit. Koristi <em>sortiranje umetanjem s binarnim pretraživanjem</em>: kad umećeš $p_i$, prefiks $p_1..p_{i-1}$ već je poznat, pa neke vrijednosti $f$ možeš izračunati sam.</p>''',
        r'''<p>Pri usporedbi $p_j$ s $p_i$ (za $j < i$) vrijednosti $f(j, i-1)$ i $f(j+1, i-1)$ računaš iz poznatog prefiksa, a $f(j, i)$ i $f(j+1, i)$ pitaš — dva upita po usporedbi, ukupno $\approx 2 n \log_2 n \le 4 \cdot 10^4$.</p>''',
    ],
    'coach': [
        ('Što od parnosti inverzija na intervalima uopće možemo saznati o pojedinim elementima?',
         r'''
<p>Broj inverzija na $[l, r]$ je (inverzije unutar $[l+1, r]$) + (unutar $[l, r-1]$) − (unutar $[l+1, r-1]$, brojane dvaput) + $[p_l > p_r]$. Ta formula uključivanja–isključivanja vrijedi za brojeve, pa i modulo $2$: $[p_l > p_r] \equiv f(l,r) + f(l+1,r) + f(l,r-1) + f(l+1,r-1) \pmod 2$. Parnosti dakle omogućuju <em>usporedbu bilo kojih dvaju elemenata</em> — imamo komparator, a ne samo globalnu statistiku.</p>
'''),
        ('Koliko usporedbi smijemo potrošiti i zašto naivno sortiranje ne prolazi?',
         r'''
<p>Limit je $4 \cdot 10^4$ upita, a usporedba košta četiri upita, dakle najviše $10^4$ usporedbi. Svako sortiranje usporedbama treba $\log_2(n!) \approx n \log_2 n - 1.44n \approx 19\,000$ usporedbi za $n = 2000$. Nema izlaza osim da usporedba postane jeftinija: treba iskoristiti da neke od četiriju vrijednosti $f$ već znamo.</p>
'''),
        ('Koje vrijednosti $f$ možemo izračunati sami ako poznajemo relativni poredak nekog dijela permutacije?',
         r'''
<p>Parnost inverzija na $[l, r]$ ovisi samo o relativnom poretku elemenata $p_l, \dots, p_r$. Ako obrađujemo elemente redom i već znamo poredak prefiksa $p_1, \dots, p_{i-1}$, sve vrijednosti $f(l, r)$ s $r \le i - 1$ možemo izračunati offline. Pri usporedbi $p_j$ s $p_i$ su nam nepoznati samo $f(j, i)$ i $f(j+1, i)$ — dva upita umjesto četiri. To prirodno vodi na <em>sortiranje umetanjem</em>: novi element binarnim pretraživanjem umećemo u poznati poredak prefiksa.</p>
'''),
        ('Zašto binarno umetanje staje u limit, a običan merge sort ne bi?',
         r'''
<p>Umetanje $i$-tog elementa binarnim pretraživanjem treba $\lceil \log_2 i \rceil$ usporedbi, ukupno $\sum_{i=1}^{2000} \lceil \log_2 i \rceil = 19\,953$, dakle najviše $39\,906$ upita — ispod $40\,000$ za svaki ulaz. Kod merge sorta uspoređujemo elemente iz raznih dijelova niza, pa za njih nije poznat poredak <em>svih</em> elemenata između, i jeftini komparator ne radi. Trik je da uspoređujemo samo novi element $p_i$ s elementima prefiksa čiji poredak već znamo.</p>
'''),
        ('Kako brzo dobiti $f(j, i-1)$ za sve $j$, a da ukupno vrijeme ostane maleno?',
         r'''
<p>Za fiksan desni kraj $i - 1$ idemo $l = i-1, i-2, \dots, 1$ i održavamo parnost $\pi_l$ inverzija na $[l, i-1]$: $\pi_l = \pi_{l+1} \oplus (\text{broj elemenata } p_m < p_l,\ m \in (l, i-1]) \bmod 2$. Broj manjih elemenata dobivamo Fenwickovim stablom nad rangovima u prefiksu, $O(\log n)$ po koraku, dakle $O(n \log n)$ po umetanju i $O(n^2 \log n) \approx 4 \cdot 10^7$ ukupno. Čak i $O(n^2)$ po umetanju ($8 \cdot 10^9$) bi bilo previše, ali $O(n)$ po umetanju s BIT-om je sasvim udobno.</p>
'''),
    ],
    'tips': [
        r'''Kad upit vraća zbroj/parnost po intervalu, princip uključivanja–isključivanja s četiri intervala $[l,r],[l+1,r],[l,r-1],[l+1,r-1]$ izolira doprinos para krajnjih točaka — to je opći trik za „2D” statistike na intervalima.''',
        r'''U interaktivnim zadacima s tijesnim limitom uvijek izračunaj točan zbroj troška najgoreg slučaja ($\sum \lceil \log_2 i \rceil$, a ne $n \log_2 n$) i uspoređuj s limitom prije kodiranja; razlika od $10\%$ ovdje odlučuje.''',
        r'''Sortiranje umetanjem s binarnim pretraživanjem ima isti broj usporedbi kao merge sort, ali u svakom trenutku uspoređuje novi element sa <em>sortiranim prefiksom</em> — kad god komparator može iskoristiti znanje o prefiksu, biraj njega.''',
        r'''Za lokalno testiranje interaktivnog zadatka ugradi u rješenje simulator suca (skrivena permutacija u ulazu, brojač upita) — stress test tada radi bez posebnog interaktora, a rješenje se pred sucem ponaša identično.''',
    ],
    'solution': r'''
<p>Označimo s $f(l, r)$ odgovor na upit za interval $[l, r]$. Lako se vidi da vrijedi</p>
<p>$$[p_l > p_r] \equiv f(l, r) - f(l+1, r) - f(l, r-1) + f(l+1, r-1) \pmod 2,$$</p>
<p>jer se u razlici ponište sve inverzije koje ne uključuju istodobno pozicije $l$ i $r$.</p>
<p>Kad bismo permutaciju jednostavno sortirali usporedbama pomoću te formule, trebali bismo oko $4 n \log n$ upita, što je previše. Umjesto toga koristimo <strong>sortiranje umetanjem</strong>: elemente obrađujemo redom i za svaki novi element binarnim pretraživanjem tražimo njegovo mjesto među već obrađenima. Kad umećemo $p_i$, relativni poredak elemenata $p_1, \dots, p_{i-1}$ već je poznat, pa vrijednosti $f(j, i-1)$ i $f(j+1, i-1)$ možemo izračunati sami, bez upita; dovoljna su dva upita po usporedbi, $f(j, i)$ i $f(j+1, i)$.</p>
<p>Ukupan broj upita je približno $2 n \log n$, a vremenska složenost $O(n^2)$.</p>
''',
    'detailed': r'''
<h3>Komparator iz parnosti</h3>
<p>Neka je $I(l, r)$ broj inverzija u $p_l, \dots, p_r$ i $f(l, r) = I(l, r) \bmod 2$ odgovor suca ($f(l, l) = 0$). Parovi $(a, b)$ s $l \le a < b \le r$ dijele se na one koji ne sadrže $l$ (podskup $[l+1, r]$), one koji ne sadrže $r$ ($[l, r-1]$), pri čemu su parovi koji ne sadrže ni $l$ ni $r$ ($[l+1, r-1]$) brojani dvaput, i na jedini par koji sadrži oboje, $(l, r)$. Zato</p>
<p>$$I(l, r) = I(l+1, r) + I(l, r-1) - I(l+1, r-1) + [p_l > p_r],$$</p>
<p>pa modulo $2$ (gdje je oduzimanje jednako zbrajanju)</p>
<p>$$[p_l > p_r] \equiv f(l, r) \oplus f(l+1, r) \oplus f(l, r-1) \oplus f(l+1, r-1).$$</p>
<p>Svaka dva elementa mogu se usporediti s najviše četiri upita — no $4 \cdot 10^4 / 4 = 10^4$ usporedbi nije dovoljno ni za jedno sortiranje usporedbama na $n = 2000$ (treba $\ge \log_2 2000! \approx 19\,000$).</p>

<h3>Ključna ideja: pola vrijednosti izračunaj sam</h3>
<p>Parnost $f(l, r)$ ovisi samo o relativnom poretku elemenata $p_l, \dots, p_r$. Ako elemente obrađujemo redom i u trenutku obrade $p_i$ već znamo relativni poredak $p_1, \dots, p_{i-1}$, sve vrijednosti $f(l, r)$ s $r \le i-1$ znamo bez upita. Za usporedbu $p_j$ s $p_i$ ($j < i$) tada trebamo samo $f(j, i)$ i $f(j+1, i)$ od suca; $f(j, i-1)$ i $f(j+1, i-1)$ računamo sami. To je točno struktura <strong>sortiranja umetanjem</strong>: održavamo sortiranu listu indeksa prefiksa i novi indeks $i$ binarnim pretraživanjem umećemo na pravo mjesto, uspoređujući $p_i$ s elementima $p_{\text{order}[\text{mid}]}$.</p>

<h3>Broj upita</h3>
<p>Binarno pretraživanje među $i - 1$ elemenata treba $\lceil \log_2 i \rceil$ usporedbi, svaka po dva upita (uz $f(i, i) = 0$ besplatno i memoizaciju već postavljenih upita $f(\cdot, i)$, koja u praksi štedi još nekoliko posto). Najgori slučaj:</p>
<p>$$2 \sum_{i=1}^{2000} \lceil \log_2 i \rceil = 2 \cdot 19\,953 = 39\,906 < 40\,000.$$</p>
<p>Granica je tijesna, ali vrijedi za svaki ulaz; na slučajnim permutacijama mjerimo oko $38\,000$ upita, na sortiranoj oko $33\,000$.</p>

<h3>Računanje $f(l, i-1)$ za sve $l$</h3>
<p>Prije umetanja $p_i$ izračunamo $\pi_l = f(l, i-1)$ za sve $l \le i - 1$. Iz poznatog poretka prefiksa svakom indeksu dodijelimo rang $\mathrm{rk}[l] \in \{1, \dots, i-1\}$. Idemo $l = i-1, i-2, \dots, 1$ i održavamo Fenwickovo stablo nad rangovima elemenata $p_{l+1}, \dots, p_{i-1}$: broj elemenata manjih od $p_l$ među njima je prefiksni zbroj do $\mathrm{rk}[l] - 1$, a $\pi_l = \pi_{l+1} \oplus (\text{taj broj} \bmod 2)$, jer inverzije na $[l, i-1]$ čine inverzije na $[l+1, i-1]$ plus parovi $(l, m)$ s $p_l > p_m$. Cijena je $O(n \log n)$ po umetanju, ukupno $O(n^2 \log n) \approx 4 \cdot 10^7$ — daleko ispod limita.</p>

<h3>Algoritam</h3>
<ol>
    <li>Pročitaj $n$; <code>order</code> je prazna lista.</li>
    <li>Za $i = 1, \dots, n$:
        <ol>
            <li>izračunaj rangove prefiksa iz <code>order</code> i parnosti $\pi_l = f(l, i-1)$ Fenwickovim stablom;</li>
            <li>definiraj $\mathrm{greater}(j) = f(j, i) \oplus f(j+1, i) \oplus \pi_j \oplus \pi_{j+1}$, gdje se $f(\cdot, i)$ pita suca (uz memoizaciju, $f(i, i) = 0$);</li>
            <li>binarnim pretraživanjem nađi najmanju poziciju u <code>order</code> čiji je element veći od $p_i$ i umetni $i$ ondje.</li>
        </ol>
    </li>
    <li>Element na poziciji $j$ liste <code>order</code> ima vrijednost $j + 1$; ispiši „! $p_1 \dots p_n$”.</li>
</ol>

<h3>Primjer</h3>
<p>$n = 3$, skriveno $2\,3\,1$. $i = 2$: usporedba $p_1$ s $p_2$: $f(1,2) = 0$, $f(2,2) = 0$, $\pi_1 = \pi_2 = 0$ → $p_1 < p_2$, <code>order</code> $= [1, 2]$. $i = 3$: $\pi_2 = 0$, $\pi_1 = f(1,2) = 0$; usporedba s $p_2$ (sredina): $f(2,3) = 1$, $f(3,3) = 0$ → $p_2 > p_3$; zatim s $p_1$: $f(1,3) = 0$, $f(2,3) = 1$, $\pi_1 = \pi_2 = 0$ → $p_1 > p_3$; <code>order</code> $= [3, 1, 2]$, dakle $p = (2, 3, 1)$. Ukupno tri upita, kao u primjeru iz zadatka.</p>

<h3>Zamke</h3>
<ul>
    <li>Nakon svakog upita <code>fflush(stdout)</code>; pri čitanju odgovora provjeri kraj ulaza (sudac može prekinuti komunikaciju).</li>
    <li>Ne pitaj $f(l, r)$ za $l \ge r$ — vrijednost je $0$, a upit bi bio nevaljan ili bi trošio limit.</li>
    <li>Memoiziraj upite unutar jednog umetanja: susjedne usporedbe u binarnom pretraživanju često dijele $f(j+1, i)$.</li>
    <li>$n = 1$: nema upita, ispiši „! 1”.</li>
</ul>
''',
    'verified': r'''Interaktivni zadatak, pa je rješenje verificirano lokalnim simulatorom suca ugrađenim u <code>sol.cpp</code> (skrivena permutacija u ulazu, točne parnosti inverzija, brojač upita s limitom $4 \cdot 10^4$): uzorak 1/1, 100 slučajnih permutacija $n \le 9$ te 1 veliki test $n = 2000$ kroz harness, a dodatno ručno 8 permutacija $n = 2000$ (slučajne, sortirana, obrnuta) s najviše $38\,100$ upita; teoretska gornja granica je $39\,906$.''',
},
# ---------------------------------------------------------------- G
{
    'letter': 'G', 'title': 'Rectangle', 'title_hr': 'Pravokutnik', 'slug': 'G_rectangle',
    'tl': '8 s', 'ml': '1024 MB',
    'statement': r'''
<p>Dano je $n$ pravokutnika s cjelobrojnim koordinatama; $i$-ti ima donji lijevi vrh $(x_{i,1}, y_{i,1})$ i gornji desni $(x_{i,2}, y_{i,2})$. Pravokutnici se mogu preklapati.</p>
<p>Treba odabrati tri međusobno različita pravca oblika $x = a$ ili $y = a$, gdje je $a$ cijeli broj iz $[1, 10^9]$, tako da svaki pravokutnik dodiruje barem jedan pravac (pravac dodiruje pravokutnik ako siječe njegovu unutrašnjost ili rub). Izračunaj broj takvih neuređenih trojki pravaca modulo $998244353$.</p>
<h3>Ulaz</h3>
<p>Prvi redak sadrži $T$ ($1 \le T \le 10^5$). Svaki testni primjer sadrži $n$ ($1 \le n \le 10^5$) i zatim $n$ redaka s $x_{i,1}, y_{i,1}, x_{i,2}, y_{i,2}$ ($1 \le x_{i,1} < x_{i,2} \le 10^9$, $1 \le y_{i,1} < y_{i,2} \le 10^9$). Zbroj svih $n$ ne prelazi $2 \cdot 10^5$.</p>
<h3>Izlaz</h3>
<p>Za svaki testni primjer ispiši odgovor u zasebnom retku.</p>
''',
    'hints': [
        r'''<p>Podijeli po tipu trojke: tri okomita pravca, tri vodoravna, dva okomita + jedan vodoravni, jedan okomiti + dva vodoravna. Slučajevi su simetrični (zamjena osi), pa treba riješiti samo dva.</p>''',
        r'''<p>Tri paralelna pravca: to je jednodimenzionalan problem na projekcijama (intervalima). Enumeriraj položaj srednjeg pravca; lijevi pravac mora pokriti sve intervale lijevo od srednjeg koje on ne dodiruje, a desni sve takve desno — svaki od ta dva uvjeta određuje interval dopuštenih položaja (presjek intervala).</p>''',
        r'''<p>Jedan vodoravni + dva okomita: sweep line po vodoravnom pravcu; pravokutnici koje on dodiruje nestaju, a za preostale intervale $[l_i, r_i]$ trebaš broj parova $(L, R)$ koji ih sve pokrivaju. Za fiksirano $L$ gornja granica za $R$ je sufiksni minimum $\min\{r_i : l_i > L\}$, koji se mijenja pri dodavanju/brisanju — zbroj takvih sufiksnih minimuma održava segmentno stablo tehnikom „rekonstrukcije zgrada” (楼房重建), $O(\log^2 n)$ po promjeni.</p>''',
    ],
    'coach': [
        ('Kako razbiti trojku pravaca na slučajeve koje možemo brojati odvojeno, bez preklapanja?',
         r'''
<p>Svaki pravac je okomit ($x = a$) ili vodoravan ($y = a$), pa trojka po broju okomitih pripada točno jednoj od četiri klase: $3+0$, $0+3$, $2+1$, $1+2$. Klase su disjunktne, zbrajaju se, a zamjenom koordinata $x \leftrightarrow y$ klasa $0+3$ postaje $3+0$, a $1+2$ postaje $2+1$. Treba dakle riješiti samo dva potproblema: „tri paralelna pravca” i „dva paralelna + jedan okomit”.</p>
'''),
        ('Tri okomita pravca dodiruju pravokutnik čim dodiruju njegovu projekciju na os $x$ — kako brojati trojke točaka koje pogađaju sve intervale?',
         r'''
<p>Fiksiraj srednju točku $b$. Interval koji ne sadrži $b$ leži ili cijeli lijevo ($r_i < b$) ili cijeli desno ($l_i > b$). Sve lijeve mora pogoditi točka $a < b$, dakle $a$ leži u presjeku lijevih intervala (ili u $[1, b-1]$ ako lijevih nema); simetrično za $c$. Broj trojki s danim $b$ je umnožak duljina tih dvaju dopuštenih raspona. Skupovi „lijevi” i „desni” mijenjaju se samo u $2n$ točaka ($b = r_i + 1$ i $b = l_i$); između njih je svaki faktor afina funkcija od $b$ (konstanta ili $b - 1$ odnosno $10^9 - b$), pa se zbroj po $b$ računa zatvorenim formulama za $\sum b$ i $\sum b^2$.</p>
'''),
        ('Dva okomita pravca $L < R$ i jedan vodoravni $h$: koji je parametar prirodno „pomicati”?',
         r'''
<p>Vodoravni pravac $h$: pravokutnici koje dodiruje ($y_{i,1} \le h \le y_{i,2}$) su riješeni, a preostale mora pokriti par $(L, R)$ preko projekcija $[l_i, r_i]$ na os $x$. Dok $h$ prolazi $[1, 10^9]$, skup preostalih intervala mijenja se samo u $2n$ događaja (pravokutnik „nestaje” na $y_{i,1}$ i „vraća se” na $y_{i,2} + 1$). Odgovor ovog slučaja je $\sum_h \text{pairs}(h)$, pa trebamo strukturu koja nakon svakog umetanja/brisanja intervala brzo daje broj valjanih parova $(L, R)$.</p>
'''),
        ('Za fiksan skup intervala, kako izgleda skup parova $(L, R)$ koji ih sve pokrivaju?',
         r'''
<p>Neka je $M = \max l_i$ i $m = \min r_i$. Nužno je $L \le m$ (inače interval s najmanjim $r$ ne sadrži ništa). Ako je $L \ge M$, $L$ je u svim intervalima i svaki $R > L$ prolazi: $10^9 - L$ parova. Ako je $L < M$, intervali s $l_i > L$ ne sadrže $L$, pa $R$ mora biti u njihovu presjeku: $M \le R \le g(L) := \min\{r_i : l_i > L\}$, tj. $\max(0, g(L) - M + 1)$ parova. Funkcija $g$ je stepenasta: sortiramo intervale po $l$, a za $L$ u „komadu” između dvaju uzastopnih $l$-ova $g$ je sufiksni minimum $r$-ova od sljedeće pozicije. Traženi zbroj je $\sum_j \text{len}_j \cdot (\text{sufmin}_j - M + 1)$ po komadima s $\text{sufmin}_j \ge M$ (sufiksni minimumi su monotoni, pa je to sufiks komada), obrezano na $L \le m$.</p>
'''),
        ('Koja struktura podataka održava $\\sum_j \\text{len}_j \\cdot \\min(w_j, w_{j+1}, \\dots)$ uz promjene pojedinih $w_j$?',
         r'''
<p>Segmentno stablo tehnikom „rekonstrukcije zgrada”: čvor pamti $\min$ svojih $w$ i zbroj $\text{len}_j \cdot (\text{sufiksni minimum unutar čvora})$. Pri spajanju desni dio ostaje netaknut, a lijevi treba preračunati uz ograničenje $\text{bound} = \min$ desnog djeteta: funkcija $\text{calc}(\text{čvor}, \text{bound})$ silazi samo u jedno dijete (ako je minimum desnog djeteta $\le$ bound lijevi dio već pamtimo, inače je desni dio cijeli jednak $\text{bound} \cdot \sum \text{len}$), pa košta $O(\log n)$, a ažuriranje $O(\log^2 n)$. Upit za raspon komada obilazimo zdesna nalijevo prenoseći bound. Brisanje intervala je postavljanje $w_j = \infty$ (komadi ostaju definirani $l$-ovima svih intervala). Ukupno $O(n \log^2 n)$ po testu.</p>
'''),
    ],
    'tips': [
        r'''Kad brojiš kombinacije objekata dvaju tipova (okomiti/vodoravni), podijeli po broju objekata svakog tipa i iskoristi simetriju zamjene osi — rješavaš pola slučajeva, a disjunktnost jamči ispravan zbroj.''',
        r'''„Skup se mijenja samo u $O(n)$ točaka, a između njih je doprinos polinom” je standardni obrazac: pretvori zbroj po $10^9$ vrijednosti u $O(n)$ segmenata sa zatvorenim formulama $\sum_{b=s}^{e} b^k$; računaj ih u <code>__int128</code> prije uzimanja modula.''',
        r'''Zbroj oblika $\sum_j c_j \cdot \min(w_j, w_{j+1}, \dots)$ uz točkaste promjene je posao za segmentno stablo „楼房重建” (rekonstrukcija zgrada): spajanje u $O(\log n)$ jednim silaskom, ažuriranje $O(\log^2 n)$. Prepoznaj ga kad god sufiksni/prefiksni minimum ulazi u zbroj s težinama.''',
        r'''Brute force za geometrijsko brojanje: sažmi koordinate u segmente s konstantnim skupom „pogođenih” objekata i množi multiplicitetima — provjerava i formule s $10^9$ i modularnu aritmetiku, ne samo malu geometriju.''',
    ],
    'solution': r'''
<p>Razlikujemo slučajeve prema tipovima pravaca: tri vodoravna pravca, jedan vodoravni i dva okomita, te simetrični slučajevi (tri okomita, dva vodoravna i jedan okomiti), koje dobijemo zamjenom koordinata.</p>
<p><strong>Tri vodoravna pravca.</strong> Rješenje ovisi samo o $y$-koordinatama, tj. o intervalima $[y_{i,1}, y_{i,2}]$, pa je problem jednodimenzionalan. Enumeriramo položaj srednjeg pravca; gornji pravac tada mora ležati u presjeku svih intervala iznad srednjeg koje on ne pokriva, a donji u presjeku svih nepokrivenih intervala ispod. Ti se presjeci računaju prefiksnim/sufiksnim minimumima i maksimumima, a broj načina je umnožak duljina dopuštenih raspona.</p>
<p><strong>Jedan vodoravni i dva okomita pravca.</strong> Vodoravni pravac pomičemo sweep lineom. Pri tome se skup pravokutnika koje vodoravni pravac dodiruje mijenja, pa trebamo podržati brisanje i umetanje intervala $[l_i, r_i]$ (njihovih $x$-projekcija) i odgovoriti na pitanje: na koliko načina dvije točke $L$ i $R$ pokrivaju sve preostale intervale?</p>
<p>Neka su preostali intervali $[l_i, r_i]$. Za lijevu točku vrijedi $L \le \min r_i$, a za desnu $R \ge \max l_i$. Definirajmo $f(L)$ kao gornju granicu za $R$ ako je lijeva točka u $L$. Svaki umetnuti interval $[l, r]$ daje ograničenje: ako je $L < l$, onda mora biti $R \le r$. Dakle na prefiksu položaja $L$ imamo ograničenje „$\le r$”. Budući da se ograničenja moraju moći i brisati, ne možemo ih jednostavno prepisivati.</p>
<p>Umjesto toga ograničenja pohranimo u segmentno stablo i u njemu održavamo <em>sufiksne minimume</em> ograničenja i njihov zbroj. To je tehnika koja se u kineskoj literaturi obično naziva „楼房重建” (rekonstrukcija zgrada): u svakom čvoru pamtimo minimum na segmentu i zbroj sufiksnih minimuma, a pri spajanju djece doprinos lijevog djeteta preračunavamo silaskom u $O(\log n)$ ovisno o minimumu desnog djeteta.</p>
<p>Ukupna vremenska složenost je $O(n \log^2 n)$.</p>
''',
    'detailed': r'''
<h3>Podjela na slučajeve</h3>
<p>Pravac $x = a$ dodiruje pravokutnik $i$ točno kad je $a \in [x_{i,1}, x_{i,2}]$, a pravac $y = a$ kad je $a \in [y_{i,1}, y_{i,2}]$. Trojka različitih pravaca ima $3, 2, 1$ ili $0$ okomitih. Klase su disjunktne, a zamjenom uloga koordinata klasa „$0$ okomita” postaje „$3$ okomita”, a „$1$ okomit” postaje „$2$ okomita”. Odgovor je</p>
<p>$$\text{same}(X) + \text{same}(Y) + \text{two}(X, Y) + \text{two}(Y, X),$$</p>
<p>gdje su $X = \{[x_{i,1}, x_{i,2}]\}$ i $Y = \{[y_{i,1}, y_{i,2}]\}$ projekcije. Označimo $C = 10^9$.</p>

<h3>Tri paralelna pravca: $\text{same}(I)$</h3>
<p>Trebamo broj trojki cijelih brojeva $a < b < c$ u $[1, C]$ takvih da svaki interval iz $I$ sadrži barem jedan od njih. Fiksirajmo $b$. Interval koji ne sadrži $b$ je ili <em>lijevi</em> ($r_i < b$) ili <em>desni</em> ($l_i > b$). Lijeve intervale može pogoditi samo $a$, pa $a$ mora ležati u njihovu presjeku $[\max l, \min r]$ (automatski $< b$); ako lijevih nema, $a \in [1, b-1]$. Simetrično, $c$ leži u presjeku desnih, a ako ih nema, $c \in [b+1, C]$. Uvjet za sve intervale je time točno pokriven (intervali koji sadrže $b$ ne traže ništa), a izbori $a$ i $c$ su neovisni:</p>
<p>$$\text{same}(I) = \sum_{b=1}^{C} A(b) \cdot B(b), \qquad A(b) = \begin{cases} b - 1, & \text{nema lijevih}\\ \max(0, \min r - \max l + 1), & \text{inače}\end{cases}$$</p>
<p>i analogno $B(b)$ s $C - b$. Skup lijevih mijenja se kad $b$ prijeđe $r_i + 1$, skup desnih kad $b$ prijeđe $l_i$; između tih najviše $2n$ događaja $A$ i $B$ su afine funkcije od $b$, pa je $\sum_b A(b) B(b)$ na segmentu $[s, e]$ zbroj kvadratnog polinoma: $p_0 q_0 \sum 1 + (p_0 q_1 + p_1 q_0) \sum b + p_1 q_1 \sum b^2$, s formulama $\sum_{b=s}^{e} b = \frac{(s+e)(e-s+1)}{2}$ i $\sum_{b=1}^{e} b^2 = \frac{e(e+1)(2e+1)}{6}$, izračunanim točno u <code>__int128</code> (do $\approx 10^{27}$) prije modula. Sortiranjem po $r$ i po $l$ i sufiksnim minimumom $r$ nad poretkom po $l$ svaki se segment obradi u $O(1)$; ukupno $O(n \log n)$.</p>

<h3>Dva paralelna + jedan okomit: $\text{two}(I, J)$</h3>
<p>Dva pravca $L < R$ dodiruju preko intervala $I$, treći pravac $h$ preko intervala $J$. Pravokutnike s $h \in J_i$ pravac $h$ rješava; ostale moraju pokriti $L$ ili $R$. Zato</p>
<p>$$\text{two}(I, J) = \sum_{h=1}^{C} \text{pairs}(S_h), \qquad S_h = \{ I_i : h \notin J_i \},$$</p>
<p>gdje je $\text{pairs}(S)$ broj parova $L < R$ koji pokrivaju sve intervale iz $S$ (za $S = \emptyset$ to je $\binom{C}{2}$). Skup $S_h$ mijenja se samo u $2n$ događaja: interval $i$ napušta $S$ na $h = y_{i,1}$ i vraća se na $h = y_{i,2} + 1$. Sweep po $h$ zbraja $(\text{duljina segmenta}) \cdot \text{pairs}(S)$ između događaja.</p>

<h3>Struktura skupa valjanih parova</h3>
<p>Za neprazan $S$ neka je $M = \max l_i$ i $m = \min r_i$. Nužno je $L \le m$: inače interval s najmanjim $r$ ne sadrži ni $L$ ni $R$. Dva su slučaja:</p>
<ul>
    <li>$M \le L \le m$: $L$ leži u svakom intervalu, pa je svaki $R \in (L, C]$ dobar — $C - L$ parova. Zbroj po $L \in [M, m]$ je $\sum (C - L)$, opet zatvorena formula.</li>
    <li>$L < M$ (i $L \le m$): intervali s $l_i \le L$ sadrže $L$ (jer je $r_i \ge m \ge L$); intervali s $l_i > L$ moraju sadržavati $R$, pa je $R \in [M, g(L)]$ gdje je $g(L) = \min\{ r_i : l_i > L \}$ (interval s $l_i = M$ ima $l_i > L$, pa je $R \ge M$ nužno i dovoljno zajedno s $R \le g(L)$). Broj parova je $\max(0, g(L) - M + 1)$.</li>
</ul>
<p>Sortirajmo <em>sve</em> intervale (i trenutno odsutne) po $l$: $L_1 \le L_2 \le \dots \le L_n$, uz $L_0 = 1$. „Komad” $j$ ($0 \le j < n$) je raspon $L \in [L_j, L_{j+1} - 1]$ duljine $\text{len}_j = L_{j+1} - L_j$ (može biti $0$). Za $L$ u komadu $j$ vrijedi $g(L) = \min_{p \ge j+1} R_p =: \text{sufmin}_j$ nad prisutnim intervalima; odsutnima postavimo $R_p = \infty$. Doprinos slučaja $L < M$ je</p>
<p>$$\sum_{j} \text{len}_j \cdot \max(0, \text{sufmin}_j - M + 1),$$</p>
<p>po komadima koji leže lijevo od $M$ i ispod $m$. Sufiksni minimumi su nepadajući u $j$, pa je $\{j : \text{sufmin}_j \ge M\}$ sufiks — njegov početak $j_0$ nađemo silaskom po stablu (najdesnija pozicija s $w < M$, plus jedan). Ako je $m \ge M$, uzimamo cijele komade $j_0, \dots, j_{\max} - 1$ (gdje $L_{j_{\max}} = M$); ako je $m < M$, komad $c$ koji sadrži $m$ obrezujemo na $[L_c, m]$ i računamo posebno s $g = \text{sufmin}_c$. Zbroj $\sum \text{len}_j \cdot \text{sufmin}_j$ nad rasponom komada daje segmentno stablo, a $M$ i $m$ održavamo skupom prisutnih pozicija i multiskupom $r$-ova.</p>

<h3>Segmentno stablo za $\sum \text{len}_j \cdot \text{sufmin}_j$ uz točkaste promjene</h3>
<p>To je tehnika „rekonstrukcije zgrada” (楼房重建). Čvor pamti $\text{mn}$ = minimum $w$ u svom rasponu i $\text{sm}$ = $\sum_j \text{len}_j \cdot \min(w_j, \dots, w_{\text{kraj čvora}})$ (sufiksni minimum <em>unutar</em> čvora). Funkcija $\text{calc}(v, \beta)$ vraća $\sum_{j \in v} \text{len}_j \cdot \min(\text{sufmin}^{(v)}_j, \beta)$, tj. doprinos čvora kad desno od njega postoji ograničenje $\beta$:</p>
<ul>
    <li>ako je $\text{mn}[v] \ge \beta$, sve je jednako $\beta$: rezultat $\beta \cdot \sum \text{len}$;</li>
    <li>inače ako je $\text{mn}[\text{desno}] \le \beta$, desno dijete „zaklanja” $\beta$, pa je lijevi dio točno onaj već pohranjen: $\text{sm}[v] - \text{sm}[\text{desno}] + \text{calc}(\text{desno}, \beta)$;</li>
    <li>inače je desni dio cijeli $\beta$, a lijevi računamo rekurzivno: $\text{calc}(\text{lijevo}, \beta) + \beta \cdot \sum_{\text{desno}} \text{len}$.</li>
</ul>
<p>Rekurzija silazi u točno jedno dijete, dakle $O(\log n)$. Spajanje je $\text{sm}[v] = \text{sm}[\text{desno}] + \text{calc}(\text{lijevo}, \text{mn}[\text{desno}])$, pa točkasta promjena košta $O(\log^2 n)$. Upit za komade $[a, b]$ obilazi kanonske čvorove zdesna nalijevo, počinjući s $\beta = \min$ svih $w$ desno od $b$ i ažurirajući $\beta$ minimumom obiđenog čvora. Vrijednost $\infty$ biramo kao $4 \cdot 10^9$ (veće od svakog $r$, a $\text{len} \cdot \infty$ stane u <code>__int128</code> prije modula).</p>

<h3>Složenost i provjera</h3>
<p>Po testu: sortiranja i sweep s $2n$ događaja, svaki uz $O(\log^2 n)$ ažuriranje i $O(\log^2 n)$ upit — ukupno $O(n \log^2 n)$; za $\sum n = 2 \cdot 10^5$ lokalno oko $2$ s uz limit $8$ s. Memorija $O(n)$. Mali primjer: jedan pravokutnik $[1, 2] \times [1, 2]$ i $C = 10^9$: trojke s barem jednim od četiri pravca $x = 1, x = 2, y = 1, y = 2$; brute force nad sažetim koordinatama i formule daju isti rezultat, a slučaj $S = \emptyset$ (svi pravokutnici pogođeni s $h$) doprinosi $\binom{C}{2}$ po vrijednosti $h$.</p>

<h3>Zamke</h3>
<ul>
    <li>Sve zbrojeve $\sum b$, $\sum b^2$ i umnoške poput $\text{len} \cdot \text{bound}$ računaj u <code>__int128</code> ili nakon zasebnog modula — $C^3 \approx 10^{27}$ prelijeva 64 bita.</li>
    <li>Negativni koeficijenti afinih funkcija ($C - b$, $b - 1$) zahtijevaju normalizaciju modula (<code>md</code> koji vraća nenegativan ostatak).</li>
    <li>Komadi se definiraju iz $l$-ova <em>svih</em> intervala, a odsutnost se modelira s $w = \infty$; tako se pri umetanju/brisanju ne mijenja particija, samo jedna vrijednost.</li>
    <li>Komadi duljine $0$ (jednaki $l$-ovi) i intervali čiji je $l$ jednak $M$ ne smiju se izgubiti: $j_{\max}$ je <em>najveća</em> prisutna pozicija, a $\text{sufmin}$ komada $j$ počinje od pozicije $j + 1$.</li>
    <li>Događaji iznad $C$ ($r_i + 1 = C + 1$) samo zatvaraju posljednji segment.</li>
</ul>
''',
    'verified': r'''uzorak 1/1; 300 slučajnih testova ($n \le 5$, koordinate malene, ekstremne i slučajne do $10^9$) protiv brute forcea koji sažima koordinate u segmente s konstantnim skupom dodirnutih pravokutnika i izbraja sve trojke pravaca s multiplicitetima; 3 velika testa ($n = 10^5$ slučajnih i gusto preklopljenih pravokutnika te $10^5$ malih testova), najviše oko $2.6$ s uz limit $8$ s.''',
},
# ---------------------------------------------------------------- H
{
    'letter': 'H', 'title': 'Chinese Checker', 'title_hr': 'Kineska dama', 'slug': 'H_chinese_checker',
    'tl': '1 s', 'ml': '1024 MB',
    'statement': r'''
<p>Prof. Pang igra kinesku damu na standardnoj šesterokrakoj ploči (zvijezda sa $121$ poljem). Na ploči je $n$ figura. Jedan <em>potez</em> sastoji se od jednog ili više koraka: najprije se odabere figura $a$ koja se pomiče (ista tijekom cijelog poteza), a u svakom koraku odabere se druga figura $b$ kao „stožer” i $a$ se premjesti na položaj simetričan s obzirom na $b$, pri čemu:</p>
<ul>
    <li>spojnica $a$ i $b$ mora biti paralelna jednoj od triju osi šesterokutne ploče (susjednost nije nužna);</li>
    <li>na spojnici od $a$ do njezina simetričnog položaja ne smije biti drugih figura osim $b$;</li>
    <li>simetrični položaj mora biti na ploči i slobodan;</li>
    <li>korak koji vraća $a$ na njezin početni položaj (prije poteza) nije dopušten.</li>
</ul>
<p>Potez može stati nakon bilo kojeg koraka. Koliko različitih poteza postoji? Dva su poteza različita ako se skupovi zauzetih polja nakon njih razlikuju (figure su nerazlučive).</p>
<h3>Ulaz</h3>
<p>Prvi redak sadrži $T$ ($1 \le T \le 100$). Svaki test sadrži $n$ ($1 \le n \le 121$) i zatim $n$ redaka s parom (redak, položaj u retku), brojeći od vrha prema dnu i slijeva nadesno od $1$. Položaji su različiti.</p>
<h3>Izlaz</h3>
<p>Za svaki test ispiši broj različitih poteza.</p>
''',
    'hints': [
        r'''<p>Ploča ima samo $121$ polje; za svaku figuru koja se pomiče skup dostižnih polja u jednom potezu je malen. Kako bi izgledao BFS po položajima figure $a$?</p>''',
        r'''<p>Najveći dio posla je geometrija ploče: prikaži šesterokutnu mrežu u koordinatama u kojima su tri osi jednostavni pomaci (npr. „aksijalne” koordinate $(q, r)$ s smjerovima $(1,0)$, $(0,1)$, $(1,-1)$) i unaprijed izgradi skup valjanih polja.</p>''',
    ],
    'coach': [
        ('Što točno razlikuje dva poteza — i zašto je to dobra vijest?',
         r'''
<p>Potez je određen skupom zauzetih polja nakon njega: $S \setminus \{a\} \cup \{X\}$, gdje je $a$ početno polje pomaknute figure i $X$ njeno završno polje ($X \notin S$). Dva takva skupa jednaka su samo ako je $a = a'$ i $X = X'$ — vađenje različitih figura ostavlja različite rupe. Dakle potezi su u bijekciji s parovima (figura, završno polje $\ne$ početno), a redoslijed skokova unutar poteza ne igra ulogu. Umjesto brojanja nizova skokova brojimo <em>dostižna polja</em>.</p>
'''),
        ('Kako brojati dostižna polja jedne figure ako se tijekom poteza mijenja samo njezin položaj?',
         r'''
<p>Sve ostale figure su nepomične, a početno polje pomaknute figure je prazno od prvog koraka. Graf stanja je stoga graf na poljima ploče (najviše $121$ vrh) čiji su bridovi dopušteni skokovi uz fiksni skup „stožera”. BFS ili DFS iz početnog polja obiđe sve dostižne vrhove; rezultat za tu figuru je broj obiđenih polja bez početnog. Zabrana povratka na početno polje samo znači da ga ne smijemo dodati kao cilj — preskakivanje preko njega (prazno je) ostaje dopušteno.</p>
'''),
        ('Kako u kodu predstaviti šesterokutnu ploču da provjera „na istoj osi” i „simetrično polje” bude trivijalna?',
         r'''
<p>Redak $r$ ima $c_r$ polja; koordinatu $x$ zadamo u „pola koraka”: polja retka duljine $c$ imaju $x = -(c-1), -(c-3), \dots, c-1$. Tada su tri osi ploče vektori $(0, \pm 2)$, $(\pm 1, \pm 1)$, a polje je na ploči točno kad je $|x| \le c_r - 1$ i $x \equiv c_r - 1 \pmod 2$. Skok u smjeru $d$: idi korak po korak dok ne naiđeš na prvu figuru (stožer na udaljenosti $k$), zatim provjeri da je sljedećih $k$ polja na ploči i prazno; posljednje je cilj. Alternativa su kubne koordinate $(x, y, z)$, $x + y + z = 0$, gdje je ploča unija dvaju velikih trokuta — korisno za neovisnu provjeru.</p>
'''),
        ('Je li „idi ravno dok ne naiđeš na figuru” ispravno, ili pravac može napustiti ploču i vratiti se na nju?',
         r'''
<p>Ploča je pravilna šesterokraka zvijezda, simetrična na rotacije za $60^\circ$ koje permutiraju tri osi. Vodoravni redak je očito neprekinut, pa je zbog simetrije neprekinut i presjek ploče sa svakim pravcem paralelnim bilo kojoj osi. Kad pretraga izađe s ploče, može stati — ne postoji stožer „iza rupe”.</p>
'''),
    ],
    'tips': [
        r'''Kad se brojanje odnosi na <em>rezultate</em> (skupove, stanja), a ne na nizove poteza, prvo dokaži da rezultat jednoznačno određuje ono što ćeš nabrajati — obično se zadatak tada svede na dostižnost u malom grafu.''',
        r'''Za šesterokutne ploče izaberi koordinate u kojima su sve osi cjelobrojni vektori: „pola koraka” po retku ili kubne koordinate $(x, y, z)$, $x+y+z=0$. Provjera pripadnosti ploči i pomaci postaju aritmetika bez tablica.''',
        r'''Kad je ploča mala ($\le 121$ polje), a pravila zamršena, piši brute force u <em>drugom</em> koordinatnom sustavu i drugom stilu (DFS umjesto BFS, eksplicitno nabrajanje segmenta) — sličan kod ponavlja iste greške u čitanju pravila.''',
    ],
    'solution': r'''
<p>Enumeriramo koja se figura pomiče, a zatim prema pravilima zadatka napravimo BFS po poljima ploče: iz trenutnog polja u svakom od šest smjerova potražimo prvu figuru $b$, provjerimo da je simetrično polje na ploči i slobodno te da između $b$ i tog polja nema drugih figura, i to polje dodamo u red. Početno polje figure ne brojimo. Odgovor je zbroj broja posjećenih polja po svim figurama.</p>
<p>Glavni je posao točno modelirati šesterokutnu ploču (zvijezdu sa $121$ poljem) u koordinatama u kojima su tri osi jednostavni pomaci; zatim je sam algoritam trivijalan.</p>
''',
    'detailed': r'''
<h3>Što brojimo</h3>
<p>Figure su nerazlučive, a potez se prepoznaje po skupu zauzetih polja nakon njega. Ako se pomiče figura s početnog polja $a$ i završi na polju $X \ne a$, novi skup je $S' = (S \setminus \{a\}) \cup \{X\}$. Iz $S'$ jednoznačno čitamo $a$ (jedino polje iz $S$ koje više nije zauzeto) i $X$ (jedino novo polje). Zato je broj različitih poteza jednak</p>
<p>$$\sum_{\text{figura } a} \bigl|\{ X \ne a : X \text{ dostižno nizom skokova figure } a \}\bigr|.$$</p>
<p>Put kojim je figura došla do $X$ nije bitan — samo je važno postoji li barem jedan.</p>

<h3>Graf dostižnosti za jednu figuru</h3>
<p>Tijekom poteza se pomiče samo figura $a$; ostale $n - 1$ figure su fiksni stožeri, a polje $a$ je od prvog koraka prazno. Stanje je dakle samo trenutni položaj figure — najviše $121$ stanje. Iz položaja $P$ u svakom od šest smjerova osi napravimo najviše jedan skok: prvo zauzeto polje $B$ u tom smjeru (na udaljenosti $k$) je stožer, a cilj je $P' = 2B - P$ (udaljenost $k$ iza $B$); skok je dopušten ako su sva polja strogo između $B$ i $P'$ prazna i na ploči, $P'$ je na ploči i prazan te $P' \ne a$. Napomena: skok preko početnog polja $a$ je dopušten (prazno je), samo slijetanje na njega nije. BFS iz $a$ obiđe skup dostižnih polja; doprinos figure je (broj obiđenih) $- 1$.</p>
<p>Zabrana „korak koji vraća $a$ na početni položaj” točno je modelirana izbacivanjem $a$ iz skupa ciljeva: nijedan kasniji skok ne može krenuti iz $a$, pa se ništa drugo ne mijenja.</p>

<h3>Koordinate ploče</h3>
<p>Ploča ima $17$ redaka duljina $1, 2, 3, 4, 13, 12, 11, 10, 9, 10, 11, 12, 13, 4, 3, 2, 1$. Polje zadajemo parom $(r, x)$, gdje je $x$ vodoravna koordinata u polovicama koraka: redak duljine $c$ ima polja $x = -(c-1), -(c-3), \dots, c-1$ (susjedna polja u retku razlikuju se za $2$). Ulazni par (redak, položaj $j$) preslikava se u $x = -(c_r - 1) + 2(j - 1)$. Tri osi šesterokutne mreže tada su smjerovi $(0, \pm 2)$, $(+1, \pm 1)$ i $(-1, \pm 1)$; polje $(r, x)$ je na ploči točno kad je $1 \le r \le 17$, $|x| \le c_r - 1$ i $x + c_r - 1$ paran. Time su i pripadnost ploči i pomak po osi čista aritmetika.</p>
<p>Traženje stožera hodanjem korak po korak ispravno je jer je presjek ploče s bilo kojim pravcem paralelnim osi neprekinut: zvijezda je invarijantna na rotacije za $60^\circ$ (koje permutiraju osi), a vodoravni su reci neprekinuti. Kad hodanje napusti ploču, u tom smjeru nema stožera.</p>

<h3>Algoritam i složenost</h3>
<ol>
    <li>Pročitaj figure, pretvori u koordinate $(r, x)$ i spremi u skup zauzetih polja.</li>
    <li>Za svaku figuru: privremeno je ukloni iz skupa, BFS-om iz njenog početnog polja obiđi dostižna polja (6 smjerova, hodanje do stožera, provjera $k$ polja iza njega), dodaj $|\text{obiđeno}| - 1$, vrati figuru.</li>
</ol>
<p>Po figuri BFS obiđe najviše $121$ polje, svaki s $6$ smjerova i hodanjem duljine najviše $13$: oko $10^4$ operacija, dakle $n \cdot 10^4 \le 1.2 \cdot 10^6$ po testu i $\le 1.2 \cdot 10^8$ za $T = 100$ u najgorem slučaju (u praksi puno manje jer je pri $121$ figuri ploča puna i skokova nema). Memorija zanemariva. Odgovor stane u <code>int</code>, ali koristimo 64-bitni tip iz opreza.</p>

<h3>Primjer</h3>
<p>Za jednu figuru odgovor je $0$ — nema stožera. Za dvije susjedne figure na istoj osi, npr. u retku $5$ na položajima $1$ i $2$: figura na položaju $1$ preskače onu na $2$ i slijeće na $3$ (ako je prazno), zatim iz $3$ nema stožera (jedina druga figura je na $2$, a skok natrag vodi na početno polje $1$, što je zabranjeno). Figura na položaju $2$ preskače onu na $1$? Cilj bi bio položaj $0$, koji ne postoji — nije dopušteno. Ukupno $1$ potez. Provjeri isto u kubnim koordinatama: skok $P \to 2B - P$ i uvjeti na segmentu daju isti skup.</p>

<h3>Zamke</h3>
<ul>
    <li>Ne brkaj „stožer mora biti susjedan” (nije nužno) i „polja između stožera i cilja moraju biti prazna” (nužno, za sva $k - 1$ polja).</li>
    <li>Cilj je na udaljenosti $2k$ od početka, ne $k + 1$ — točka simetrična s obzirom na stožer.</li>
    <li>Početno polje pomaknute figure je prazno tijekom poteza: uklonimo ga iz skupa zauzetih prije BFS-a i vratimo poslije.</li>
    <li>Ulaz je 1-indeksiran po retku i položaju; retci $5$–$13$ imaju različite duljine, pa položaj $j$ nije isti stupac u svim recima — zato koordinata $x$ u polovicama koraka.</li>
</ul>
''',
    'verified': r'''uzorak 1/1; 300 slučajnih testova ($1$ do $121$ figura, uključujući gotovo praznu i gotovo punu ploču) protiv neovisne Python implementacije u kubnim koordinatama (ploča kao unija dvaju trokuta, DFS, eksplicitno nabrajanje polja skoka); 3 velika testa s $T = 100$ ($0.01$ s).''',
},
# ---------------------------------------------------------------- I
{
    'letter': 'I', 'title': 'Chase Game', 'title_hr': 'Igra potjere', 'slug': 'I_chase_game',
    'tl': '1 s', 'ml': '1024 MB',
    'statement': r'''
<p>Prof. Shou bježi od prof. Panga na neusmjerenom, netežinskom, jednostavnom povezanom grafu. Shou je u vrhu $1$ i želi do vrha $n$; Pang je u vrhu $k$ i ima domet napada $d$.</p>
<p>Svake sekunde Shou prijeđe u susjedni vrh, a zatim ga Pang napadne: šteta je $d - dis$, gdje je $dis$ udaljenost (broj bridova na najkraćem putu) između njih. Ako je $dis \ge d$, Pang se umjesto toga teleportira u Shouov vrh i nanese štetu $d$ (kad je $dis < d$, Pang ostaje na mjestu). Shou prima napad i pri dolasku u vrh $n$.</p>
<p>Odredi najmanju ukupnu štetu koju Shou mora primiti.</p>
<h3>Ulaz</h3>
<p>Prvi redak sadrži $n, m, k, d$ ($2 \le n \le 10^5$, $n - 1 \le m \le 2 \cdot 10^5$, $1 \le k \le n$, $1 \le d \le 2 \cdot 10^5$). Slijedi $m$ bridova $a\ b$. Graf je povezan.</p>
<h3>Izlaz</h3>
<p>Ispiši najmanju ukupnu štetu.</p>
''',
    'hints': [
        r'''<p>Što se dogodi nakon što Pang teleportira u Shouov vrh? Od tog trenutka Pang je uvijek na udaljenosti $1$ (ili se ponovno teleportira ako je $d = 1$), pa je šteta po koraku konstantna i optimalno je ići najkraćim putem do $n$.</p>''',
        r'''<p>Dok Pang stoji u $k$, šteta u vrhu $v$ ovisi samo o $\mathrm{dist}(k, v)$. Dakle stanje je samo trenutni vrh i „je li se teleport već dogodio” — a nakon teleporta odgovor je zatvorena formula.</p>''',
        r'''<p>Napravi BFS iz $k$ i iz $n$, zatim Dijkstra iz $1$ s težinom vrha $v$ jednakom $d - \mathrm{dist}(k, v)$ ako je to $\gt 0$; ulazak u vrh s $\mathrm{dist}(k, v) \ge d$ znači teleport, pa dodaj $d$ plus (preostali koraci do $n$) $\cdot$ (šteta po koraku) i ne nastavljaj dalje.</p>''',
    ],
    'coach': [
        ('Što se zapravo promijeni u trenutku kad se Pang prvi put teleportira?',
         r'''
<p>Do teleporta Pang miruje u $k$, pa šteta pri ulasku u vrh $v$ ovisi samo o $v$: iznosi $d - \operatorname{dist}(k, v)$, uvijek strogo pozitivna. Nakon teleporta Pang stoji točno na Shouovu vrhu i sve što slijedi ovisi samo o tome kamo Shou ide dalje — prošlost je nebitna. Zadatak se prirodno dijeli na „prije prvog teleporta” (fiksni Pang, težine na vrhovima) i „nakon prvog teleporta” (stanje potpuno opisano Shouovim vrhom).</p>
'''),
        ('Nakon teleporta u vrh $v$, zašto Shou ne može učiniti ništa bolje nego hodati najkraćim putem do $n$?',
         r'''
<p>Pang je u $v$. Nakon $i$ koraka Shou je od $v$ udaljen najviše $i$, pa je šteta $i$-tog koraka barem $d - \min(i, d-1)$ dok nema teleporta, a korak koji izazove novi teleport košta $d$ i moguć je tek kad udaljenost dosegne $d$, dakle najranije u koraku $d$. Odatle indukcijom po broju teleporta slijedi donja granica $g(L)$ za svaki put duljine $\ge L = \operatorname{dist}(v, n)$: blok od $d$ koraka košta barem $(d-1) + (d-2) + \dots + 1 + d = \frac{d(d+1)}{2}$, a ostatak od $r$ koraka barem $(d-1) + \dots + (d-r)$. Hodanje najkraćim putem postiže točno te vrijednosti jer je udaljenost od Panga nakon $i$ koraka točno $i$. Duži put nikad ne pomaže jer su svi članovi donje granice pozitivni.</p>
'''),
        ('Kako izgleda formula za cijenu ostatka i zašto ne treba simulirati korak po korak?',
         r'''
<p>Ako je $L = qd + r$ s $0 \le r < d$, onda $g(L) = q \cdot \frac{d(d+1)}{2} + rd - \frac{r(r+1)}{2}$. Svakih $d$ koraka slika je ista (Pang se teleportira na Shoua), pa zbrajamo $q$ punih blokova i jedan nepotpun. Formula je $O(1)$, a vrijednosti do $\approx 10^5 \cdot 2 \cdot 10^5$ traže 64-bitni tip.</p>
'''),
        ('Kako optimalno odabrati gdje će se prvi teleport dogoditi, ili hoće li se dogoditi uopće?',
         r'''
<p>Prije teleporta Shou se kreće samo po vrhovima s $\operatorname{dist}(k, v) < d$ i plaća $d - \operatorname{dist}(k, v) > 0$ pri svakom ulasku. To je najkraći put s pozitivnim težinama na vrhovima: Dijkstra iz vrha $1$ daje $D(u)$ za sve takve vrhove. Kandidati za odgovor su $D(n)$ (bez teleporta) i, za svaki brid $u \to v$ s $\operatorname{dist}(k, v) \ge d$, vrijednost $D(u) + d + g(\operatorname{dist}(v, n))$ — teleport u $v$ pa najkraći put. Minimum kandidata je odgovor jer smo pokrili sve moguće oblike optimalne strategije.</p>
'''),
    ],
    'tips': [
        r'''Kad se pravila igre „resetiraju” nekim događajem (teleport, obnova, prelazak granice), razdvoji problem na fazu prije događaja i fazu nakon njega i pitaj se je li stanje nakon događaja opisano malo brojem parametara — često je faza nakon događaja zatvorena formula.''',
        r'''Donje granice po koraku („u $i$-tom koraku udaljenost je najviše $i$”) i konstrukcija koja ih dostiže (najkraći put) standardni su par za dokaz optimalnosti pohlepnog ponašanja u zadacima potjere.''',
        r'''Težine na vrhovima pretvaraju se u težine bridova stavljanjem cijene na ulazak u vrh; kad su strogo pozitivne, Dijkstra radi bez izmjena. Uz „izlazne” bridove u posebno stanje (teleport) dovoljno je gledati kandidate na bridovima, bez novih vrhova.''',
        r'''Brute force za igre s determinističkim protivnikom: Dijkstra nad punim stanjem (položaj Shoua, položaj Panga) na malom grafu — provjerava i formulu i tvrdnju „poslije teleporta ide se najkraćim putem”.''',
    ],
    'solution': r'''
<p>Najprije uočimo: ako se Pang teleportira u Shouov vrh, od tog trenutka udaljenost među njima je uvijek $1$ (ili se, za $d = 1$, teleport ponavlja svaki korak), pa je šteta po koraku konstantna i Shou najbolje ide najkraćim putem do $n$. Dakle nakon teleporta odgovor možemo izračunati izravno formulom.</p>
<p>Zato treba razmatrati samo početni dio puta, dok se Pang još nije pomaknuo iz $k$. Šteta pri ulasku u vrh $v$ tada ovisi samo o $\mathrm{dist}(k, v)$, pa je broj korisnih stanja $O(n)$. Nakon što BFS-om izračunamo najkraće udaljenosti od $k$ i od $n$ do svih vrhova, pokrenemo Dijkstrin algoritam iz vrha $1$ s težinama $d - \mathrm{dist}(k, v)$; ulazak u vrh s $\mathrm{dist}(k, v) \ge d$ znači teleport i završava se formulom za ostatak puta.</p>
<p>Vremenska složenost je $O((n + m) \log n)$.</p>
''',
    'detailed': r'''
<h3>Dvije faze igre</h3>
<p>Neka je $\delta_k(v) = \operatorname{dist}(k, v)$ i $\delta_n(v) = \operatorname{dist}(v, n)$ (BFS, graf je netežinski). Dok Pang stoji u $k$, Shouov ulazak u vrh $v$ s $\delta_k(v) < d$ košta $d - \delta_k(v) \ge 1$, a ulazak u vrh s $\delta_k(v) \ge d$ izaziva teleport i košta $d$. Nakon teleporta Pang je na Shouovu vrhu, pa daljnja šteta ovisi samo o Shouovu položaju, a ne o $k$ ni o povijesti.</p>

<h3>Faza nakon teleporta: lema o najkraćem putu</h3>
<p><strong>Lema.</strong> Ako je Pang upravo teleportiran u vrh $v$ i $L = \delta_n(v)$, najmanja daljnja šteta iznosi</p>
<p>$$g(L) = q \cdot \frac{d(d+1)}{2} + rd - \frac{r(r+1)}{2}, \qquad L = qd + r,\ 0 \le r < d,$$</p>
<p>i postiže se hodanjem bilo kojim najkraćim putem od $v$ do $n$.</p>
<p><em>Dostižnost.</em> Na najkraćem putu Shou je nakon $i$ koraka od Panga udaljen točno $i$. Koraci $1, \dots, d-1$ koštaju $d-1, d-2, \dots, 1$; korak $d$ dovodi udaljenost na $d$, Pang se teleportira i naplaćuje $d$. Blok od $d$ koraka stoji $\frac{d(d-1)}{2} + d = \frac{d(d+1)}{2}$, a situacija je ista kao na početku, samo s $L - d$. Posljednjih $r$ koraka košta $(d-1) + \dots + (d-r) = rd - \frac{r(r+1)}{2}$.</p>
<p><em>Donja granica</em> (indukcija po broju teleporta na putu). Promatrajmo korake do sljedećeg teleporta ili do kraja. Nakon $i$ koraka Shou je od Panga udaljen najviše $i$, a bez teleporta i najviše $d-1$, pa $i$-ti korak košta barem $d - \min(i, d-1) \ge 1$. Ako put završi u $n$ bez novog teleporta nakon $s \ge L$ koraka, tada je $L \le d-1$ i šteta je barem $\sum_{i=1}^{L}(d-i) = g(L)$. Ako se novi teleport dogodi u koraku $s+1$ u vrhu $u$, udaljenost je morala narasti do $d$, pa je $s \ge d-1$; šteta tih $s+1$ koraka je barem $\sum_{i=1}^{d-1}(d-i) + d = \frac{d(d+1)}{2}$, a $\delta_n(u) \ge L - d$. Po induktivnoj pretpostavci ostatak stoji barem $g(\delta_n(u)) \ge g(L-d)$ jer je $g$ nepadajuća (svi pribrojnici su $\ge 0$), ukupno barem $\frac{d(d+1)}{2} + g(L - d) = g(L)$. $\square$</p>

<h3>Faza prije teleporta: Dijkstra</h3>
<p>Dok nema teleporta, Shou obilazi samo vrhove s $\delta_k(v) < d$ i pri svakom ulasku plaća poznatu pozitivnu težinu $w(v) = d - \delta_k(v)$. Najmanja šteta $D(u)$ s kojom Shou može stići u takav vrh $u$ bez teleporta je najkraći put s težinama na vrhovima — Dijkstra iz $1$ s $D(1) = 0$ (Shou u startu nije napadnut jer se napad događa nakon poteza), gdje je brid $u \to v$ dopušten samo ako je $\delta_k(v) < d$ i košta $w(v)$.</p>
<p>Prvi teleport događa se pri prelasku bridom $u \to v$ s $\delta_k(v) \ge d$ (zapravo točno $d$, jer se udaljenost mijenja za najviše $1$ po koraku). Nakon toga leme daju cijenu ostatka. Kandidati:</p>
<ul>
    <li>$D(n)$ — Shou stigne do $n$ bez teleporta (ako je $\delta_k(n) < d$ i $n$ dostižan takvim vrhovima);</li>
    <li>$D(u) + d + g(\delta_n(v))$ za svaki brid $\{u, v\}$ s $D(u) < \infty$ i $\delta_k(v) \ge d$.</li>
</ul>
<p>Svaka strategija Shoua ili nikad ne izazove teleport (pa je njena šteta $\ge D(n)$ jer je to najkraći put s tim težinama) ili prvi teleport izazove nekim bridom $u \to v$ nakon što je do $u$ stigla sa štetom $\ge D(u)$, a ostatak stoji $\ge g(\delta_n(v))$ po lemi. Zato je odgovor točno minimum kandidata.</p>

<h3>Algoritam</h3>
<ol>
    <li>BFS iz $k$ i iz $n$: $\delta_k$, $\delta_n$.</li>
    <li>Dijkstra iz $1$ po vrhovima s $\delta_k < d$, težina ulaska $d - \delta_k(v)$; kad se iz vrha $u$ gleda susjed $v$ s $\delta_k(v) \ge d$, ažuriraj odgovor s $D(u) + d + g(\delta_n(v))$.</li>
    <li>Ako je $n$ dosegnut Dijkstrom, ažuriraj odgovor s $D(n)$. Ispiši minimum.</li>
</ol>
<p>Složenost $O((n + m) \log n)$ za Dijkstru i $O(n + m)$ za BFS-ove; memorija $O(n + m)$.</p>

<h3>Primjer</h3>
<p>Put $1 - 2 - 3 - 4 - 5$, $k = 3$, $d = 2$. $\delta_k = (2, 1, 0, 1, 2)$. Ulazak u $2$ košta $2 - 1 = 1$, u $3$ košta $2$, u $4$ košta $1$; ulazak u $5$ ($\delta_k = 2 \ge d$) je teleport za $2$, a zatim $g(0) = 0$. Ukupno $1 + 2 + 1 + 2 = 6$. Alternativa da se teleport dogodi ranije ne postoji jer su svi vrhovi na putu osim $1$ i $5$ unutar dometa. Ako bi graf imao i $6$ iza $5$, ostatak bi bio $g(1) = d - 1 = 1$.</p>

<h3>Zamke</h3>
<ul>
    <li>Šteta se zbraja i pri dolasku u $n$ — uključena je u težinu ulaska odnosno u $g$.</li>
    <li>Kandidat s teleportom smije se uzeti samo iz vrha $u$ koji je zaista dostižan bez teleporta ($D(u) < \infty$); vrhovi s $\delta_k \ge d$ nisu u Dijkstri.</li>
    <li>$g(L)$ i $D$ prelaze $2^{31}$ (do $\approx nd \le 2 \cdot 10^{10}$): 64-bitni tipovi. Za $d = 1$ svaki korak nakon teleporta ponovno je teleport i $g(L) = L$ — formula to pokriva.</li>
    <li>Graf može imati $m$ do $2 \cdot 10^5$ bridova; Dijkstra s lijenim brisanjem (preskoči zastarjele unose) je dovoljna.</li>
</ul>
''',
    'verified': r'''uzorci 2/2; 300 slučajnih povezanih grafova ($n \le 8$, razni $k$, $d$) protiv brute forcea koji Dijkstrom pretražuje puno stanje igre (Shouov i Pangov položaj) uz doslovnu simulaciju napada i teleporta; 3 velika testa ($n = 10^5$, $m = 2 \cdot 10^5$, mali i veliki $d$) u najviše $0.05$ s.''',
},
# ---------------------------------------------------------------- J
{
    'letter': 'J', 'title': 'Chase Game 2', 'title_hr': 'Igra potjere 2', 'slug': 'J_chase_game_2',
    'tl': '1 s', 'ml': '1024 MB',
    'statement': r'''
<p>Karta igre je stablo s $n$ soba. Pang je u sobi $u$, Shou u sobi $v$ ($u \ne v$); igraju naizmjence, Shou prvi. U svom potezu igrač (znajući oba položaja) ostaje ili prelazi u susjednu sobu. Shou je uhvaćen kad su u istoj sobi. Pang želi uhvatiti Shoua u konačno mnogo poteza, Shou to želi izbjeći; oba igraju optimalno.</p>
<p>Prof. Fei će dodati što manje novih hodnika (bridova) tako da za <em>svaki</em> par početnih soba $(u, v)$ Pang ne može uhvatiti Shoua. Odredi najmanji broj dodanih hodnika ili $-1$ ako to nije moguće.</p>
<h3>Ulaz</h3>
<p>Prvi redak sadrži $T$ ($1 \le T \le 10^4$). Svaki test sadrži $n$ ($2 \le n \le 10^5$) i $n - 1$ bridova stabla. Zbroj svih $n$ ne prelazi $2 \cdot 10^5$.</p>
<h3>Izlaz</h3>
<p>Za svaki test ispiši najmanji broj dodanih hodnika ili $-1$.</p>
<h3>Primjer</h3>
<p>Za put od $4$ vrha odgovor je $1$; za zvijezdu s $3$ lista odgovor je $-1$; za stablo s bridovima $1\!-\!2, 2\!-\!3, 3\!-\!4, 3\!-\!5$ odgovor je $2$.</p>
''',
    'hints': [
        r'''<p>Kada Pang sigurno hvata Shoua? Ako je Shou u listu, a Pang u njegovu susjedu, Shou je uhvaćen odmah. Pokušaj tu situaciju poopćiti: koji uvjet na zatvorene susjedstva $N[v] \subseteq N[u]$ znači da je vrh $v$ „stjeran u kut”?</p>''',
        r'''<p>Nije dovoljno spojiti list samo s njegovim „bratom” (listom istog roditelja): Pang u roditelju i dalje hvata. Iz toga slijedi da zvijezda nema rješenja. Što s ostalim stablima?</p>''',
        r'''<p>Neka je $s$ broj listova, a $mx$ najveći broj listova s istim roditeljem. Donja granica je $\max\!\left(\lceil s/2 \rceil, mx\right)$ — i može se dostići uparivanjem listova različitih roditelja.</p>''',
    ],
    'coach': [
        ('Kada, na proizvoljnom grafu, Pang uspijeva uhvatiti Shoua iz nekog početnog para?',
         r'''
<p>Nazovimo vrh $v$ <em>kutom</em> ako postoji $u \ne v$ s $N[v] \subseteq N[u]$ (zatvorena susjedstva). Ako Shou stoji u kutu $v$, a Pang u $u$, Shou na potezu ostaje u $N[v] \subseteq N[u]$ i Pang ga sljedećim potezom hvata. Obratno, ako kutova nema, Shou iz položaja $s$ uz Panga u $p \ne s$ uvijek ima potez u $w \in N[s] \setminus N[p]$ — takav $w$ postoji jer $N[s] \not\subseteq N[p]$ — pa nakon Pangova poteza opet nisu u istom vrhu i situacija se ponavlja zauvijek. Dakle: Pang hvata iz nekog para točno kad graf ima kut, a zadatak traži najmanje bridova čije dodavanje uklanja <em>sve</em> kutove.</p>
'''),
        ('Koji su vrhovi stabla kutovi i zašto je zvijezda beznadna?',
         r'''
<p>List $\ell$ s roditeljem $p$ ima $N[\ell] = \{\ell, p\} \subseteq N[p]$ — kut. Vrh $v$ stupnja $\ge 2$ nije kut: $u$ bi morao biti susjed $v$-a i svih ostalih susjeda $v$-a, što bi dalo trokut, a stablo ga nema. U zvijezdi sa središtem $c$ vrijedi $N[c] = V$, pa je svaki drugi vrh kut bez obzira na dodane bridove — odgovor $-1$ (uključivo $n = 2$). Za ostala stabla treba „izvući iz kuta” svaki list, a pri tome ne stvoriti nove kutove.</p>
'''),
        ('Što jedan dodani brid može popraviti, a što ne može?',
         r'''
<p>List $\ell$ prestaje biti kut u odnosu na $p$ točno kad dobije susjeda $w \notin N[p]$. Brid koji ne dira $\ell$ ništa ne mijenja za $\ell$, pa svaki brid popravlja najviše dva lista: barem $\lceil s/2 \rceil$ bridova. Brid između dvaju listova istog roditelja $p$ ne popravlja nijedan (oba nova susjeda su u $N[p]$), pa za grupu od $mx$ listova istog roditelja treba barem $mx$ bridova s po jednim krajem u grupi. Donja granica: $\max(\lceil s/2 \rceil, mx)$.</p>
'''),
        ('Kako dostići granicu i istodobno se uvjeriti da nismo stvorili novi kut?',
         r'''
<p>Dodajemo samo bridove list–list između različitih roditelja. Ako je $mx \le s/2$, poredaj listove po grupama i upari $i$-ti s $(i + \lceil s/2 \rceil)$-tim — parovi su iz različitih grupa jer nijedna grupa nije veća od $s/2$; eventualni neuparen list spoji s već uparenim listom druge grupe. Ako je $mx > s/2$, svaki list izvan najveće grupe upari s listom najveće grupe, a preostalih $2mx - s$ listova najveće grupe spoji s bilo kojim listom druge grupe (postoji jer stablo nije zvijezda). Provjera kutova: listu $\ell$ svaki novi susjed je list drugog roditelja, koji nije u $N[p]$, a $p \notin N[\text{novi susjed}]$; vrh stupnja $\ge 2$ bio bi kut samo ako su dva njegova susjeda spojena — to bi bila dva brata, koje nikad ne spajamo. Ukupno točno $\max(\lceil s/2 \rceil, mx)$ bridova.</p>
'''),
    ],
    'tips': [
        r'''Igre potjere s jednim lovcem i potpunom informacijom rješavaju se lokalnim uvjetom na zatvorena susjedstva: bjegunac gubi točno kad postoji vrh $v$ s $N[v] \subseteq N[u]$ („kut”, isti pojam kao u karakterizaciji <em>cop-win</em> grafova). Kad zadatak pita „za svaki početni par”, traži se graf bez kutova.''',
        r'''Donje granice tipa „svaki brid popravlja najviše dva objekta” i „objekti iz iste grupe ne mogu se popravljati međusobno” zajedno daju $\max(\lceil s/2 \rceil, mx)$ — isti obrazac kao pri uparivanju elemenata multiskupa u parove različitih tipova, gdje je to i dostižno.''',
        r'''Kad konstrukciju dokazuješ, provjeri i vrhove koje nisi mijenjao: novi bridovi mogu stvoriti novu lošu konfiguraciju (ovdje trokut kroz roditelja). Brute force koji doslovno igra igru nad svim podskupovima dodanih bridova hvata takve previde.''',
    ],
    'solution': r'''
<p>Najprije, za svaki list nužno je dodati barem jedan brid: ako je Shou u listu a Pang u njegovu roditelju, Shou je odmah uhvaćen. Nadalje, list se ne može „spasiti” tako da ga spojimo samo s njegovim bratom (drugim listom istog roditelja), jer Pang u roditelju i dalje pokriva oba. Iz toga slijedi da za zvijezdu rješenje ne postoji: odgovor je $-1$.</p>
<p>U suprotnom, neka je $s$ ukupan broj listova, a $mx$ najveći broj listova koji imaju zajedničkog roditelja. Odgovor ne može biti manji od $\max\!\left(\lceil s/2 \rceil, mx\right)$: svaki dodani brid popravlja najviše dva lista, a listovi istog roditelja ne mogu se popravljati međusobno.</p>
<p>Nije teško dokazati da se ta donja granica može dostići: listove uparujemo tako da uparujemo listove različitih roditelja (uvijek uzimajući list iz trenutačno najveće grupe), a preostale listove najveće grupe spajamo s drugim, ne-susjednim vrhovima stabla, kojih ima jer stablo nije zvijezda. Dakle odgovor je $\max\!\left(\lceil s/2 \rceil, mx\right)$, a složenost $O(n)$.</p>
''',
    'detailed': r'''
<h3>Kada Pang hvata: kutovi</h3>
<p>Radimo na proizvoljnom grafu $H$ (stablo s dodanim bridovima). $N[v]$ je zatvoreno susjedstvo vrha $v$ (uključuje $v$). Vrh $v$ zovemo <em>kutom</em> ako postoji $u \ne v$ takav da je $N[v] \subseteq N[u]$.</p>
<p><strong>Tvrdnja.</strong> Pang može uhvatiti Shoua iz nekog početnog para $(u, v)$, $u \ne v$, točno onda kad $H$ ima kut.</p>
<ul>
    <li>Ako je $v$ kut s pripadnim $u$, počnimo sa Shouom u $v$ i Pangom u $u$. Shou na potezu ostaje ili prelazi u susjeda — u svakom slučaju u vrh $w \in N[v] \subseteq N[u]$. Pang zatim prelazi u $w$ (ili ostaje, ako je $w = u$) i hvata ga.</li>
    <li>Ako kutova nema, Shou ima strategiju vječnog bijega iz svakog položaja: neka je Shou u $s$, Pang u $p \ne s$, Shou na potezu. Budući da $N[s] \not\subseteq N[p]$, postoji $w \in N[s] \setminus N[p]$; Shou ode u $w$. Pang s poteza u $p$ dolazi u neki $p' \in N[p]$, a $w \notin N[p]$, pa $p' \ne w$ — Shou nije uhvaćen i nalazi se u istoj situaciji (Shou na potezu, različiti vrhovi). Indukcijom Pang ga nikad ne hvata.</li>
</ul>
<p>Zadatak se time svodi na: <em>najmanje bridova dodati stablu tako da rezultat nema kutova</em>.</p>

<h3>Kutovi u stablu</h3>
<p>List $\ell$ s roditeljem $p$ je kut: $N[\ell] = \{\ell, p\} \subseteq N[p]$. Vrh $v$ stupnja $\ge 2$ nije kut: iz $N[v] \subseteq N[u]$ slijedi da je $u$ susjed $v$-a i susjed svakog drugog susjeda $v$-a, što daje trokut — nemoguće u stablu. Dakle kutovi stabla su točno listovi.</p>
<p><strong>Zvijezda.</strong> Ako je neki vrh $c$ susjed svih ostalih ($n = 2$ ili $n - 1$ listova s istim roditeljem), onda $N[c] = V$ i svaki $v \ne c$ zadovoljava $N[v] \subseteq N[c]$ neovisno o dodanim bridovima. Kutovi se ne mogu ukloniti: odgovor je $-1$. Za sve ostale slučajeve pokazat ćemo da je odgovor konačan.</p>

<h3>Donja granica</h3>
<p>Neka je $s$ broj listova, a listove grupiramo po roditelju; $mx$ je veličina najveće grupe. List $\ell$ (roditelj $p$) prestaje biti kut u odnosu na $p$ samo ako dobije novog susjeda $w \notin N[p]$ (novi susjedi unutar $N[p]$ ne pomažu, a bez novih susjeda $N[\ell] = \{\ell, p\}$). Zato:</p>
<ul>
    <li>svaki dodani brid ima dva kraja, pa „popravlja” najviše dva lista: treba barem $\lceil s/2 \rceil$ bridova;</li>
    <li>brid između dvaju listova iste grupe (roditelj $p$) ne popravlja nijedan od njih, jer su oba u $N[p]$; svaki brid stoga popravlja najviše jedan list neke fiksne grupe, pa za najveću grupu treba barem $mx$ bridova.</li>
</ul>
<p>Ukupno barem $K = \max(\lceil s/2 \rceil, mx)$ bridova.</p>

<h3>Konstrukcija s točno $K$ bridova</h3>
<p>Stablo nije zvijezda, pa postoje barem dvije grupe listova: stablo bez listova $T'$ ima $\ge 2$ vrha, a svaki list stabla $T'$ ima u $T$ barem jedno dijete-list. Dodajemo isključivo bridove list–list između <em>različitih</em> grupa (takvi bridovi u stablu ne postoje, pa nema dvostrukih).</p>
<ol>
    <li><strong>$mx \le s/2$.</strong> Poredaj listove grupu za grupom u niz $\ell_0, \dots, \ell_{s-1}$ i spoji $\ell_i$ s $\ell_{i + \lceil s/2 \rceil}$ za $i = 0, \dots, \lfloor s/2 \rfloor - 1$. Dva lista iste grupe stoje u nizu na razmaku manjem od veličine grupe, a razmak $\lceil s/2 \rceil$ zahtijevao bi grupu veličine $\ge \lceil s/2 \rceil + 1 > s/2$ — takve nema, pa su svi parovi iz različitih grupa. Ako je $s$ neparan, list $\ell_{\lfloor s/2 \rfloor}$ ostaje neuparen; spoji ga s bilo kojim već uparenim listom druge grupe. Ukupno $\lceil s/2 \rceil = K$ bridova.</li>
    <li><strong>$mx > s/2$.</strong> Neka je $G$ najveća grupa (roditelj $p_G$). Svaki od $s - mx$ listova izvan $G$ spoji s različitim listom iz $G$; preostalih $2mx - s \ge 1$ listova iz $G$ spoji s bilo kojim listom izvan $G$ (postoji, jer ima barem dvije grupe). Ukupno $(s - mx) + (2mx - s) = mx = K$ bridova.</li>
</ol>
<p><strong>Rezultat nema kutova.</strong> Svaki list $\ell$ (roditelj $p$) dobio je $\ge 1$ novog susjeda, a svi su mu novi susjedi listovi drugih roditelja. Kandidati $u$ za $N[\ell] \subseteq N[u]$ su susjedi $\ell$-a: (a) $u = p$ — no novi susjed $w$ je list s roditeljem $p' \ne p$ čiji su svi susjedi listovi ili $p'$, pa $w \notin N[p]$; (b) $u = w$ novi susjed — no $p \notin N[w]$ iz istog razloga. Vrh $v$ stupnja $\ge 2$ u stablu bio bi kut samo za $u$ susjeda $v$-a koji je susjed i svim ostalim susjedima $v$-a; $v$ nije dobio nove bridove, pa je $u$ stablov susjed, a njegov brid do drugog stablova susjeda $a$ od $v$ mora biti nov, dakle $u$ i $a$ su listovi s istim roditeljem $v$ — a takve nikad ne spajamo. Nijedan vrh nije kut, pa Shou bježi iz svakog početnog para.</p>

<h3>Algoritam</h3>
<ol>
    <li>Izbroji stupnjeve; listovi su vrhovi stupnja $1$, roditelj lista je njegov jedini susjed.</li>
    <li>Ako je $n = 2$ ili neki vrh ima $n - 1$ listova-susjeda (zvijezda), ispiši $-1$.</li>
    <li>Inače ispiši $\max(\lceil s/2 \rceil, mx)$, gdje je $mx$ najveći broj listova s istim roditeljem.</li>
</ol>
<p>Složenost $O(n)$ po testu, memorija $O(n)$; konstrukcija se ne ispisuje, potrebna je samo za dokaz.</p>

<h3>Primjeri iz zadatka</h3>
<ul>
    <li>Put $1\!-\!2\!-\!3\!-\!4$: listovi $1, 4$ s roditeljima $2, 3$; $s = 2$, $mx = 1$, odgovor $1$ (brid $1\!-\!4$ daje ciklus $C_4$, koji nema kutova).</li>
    <li>Zvijezda s tri lista: $-1$.</li>
    <li>Stablo $1\!-\!2, 2\!-\!3, 3\!-\!4, 3\!-\!5$: listovi $1$ (roditelj $2$) i $4, 5$ (roditelj $3$); $s = 3$, $mx = 2$; odgovor $\max(2, 2) = 2$, npr. bridovi $1\!-\!4$ i $1\!-\!5$ (slučaj $mx > s/2$: list $1$ je „list izvan $G$” spojen s $4$, a preostali list $5$ također s $1$).</li>
</ul>

<h3>Zamke</h3>
<ul>
    <li>Provjera zvijezde preko $mx = n - 1$ pokriva i put od $3$ vrha; $n = 2$ treba posebno jer su oba vrha listovi i roditelji jedan drugom.</li>
    <li>Brid $1\!-\!4$ u primjeru pokazuje zašto je uvjet „različiti roditelji” bitan: spajanje $4\!-\!5$ u trećem primjeru ne bi pomoglo nijednom od njih.</li>
    <li>$T$ do $10^4$ testova: koristi nizove veličine $n + 1$ po testu, ne globalne veličine $10^5$ koje se brišu svaki put.</li>
</ul>
''',
    'verified': r'''uzorci 1/1 (3 primjera iz zadatka); 300 slučajnih stabala ($n \le 6$, uključujući lance, zvijezde i „dvostruke zvijezde”) protiv brute forcea koji za svaki podskup nedostajućih bridova (po rastućoj veličini) retrogradnom analizom doslovno odigra igru potjere iz <em>svakog</em> početnog para; 3 velika testa sa $\sum n = 2 \cdot 10^5$ ($0.02$ s).''',
},
# ---------------------------------------------------------------- K
{
    'letter': 'K', 'title': 'Magic', 'title_hr': 'Čarolija', 'slug': 'K_magic',
    'tl': '3 s', 'ml': '16 MB',
    'statement': r'''
<p><em>Upozorenje: neobično memorijsko ograničenje!</em></p>
<p>Dan je niz $a_0, \dots, a_{2n}$, na početku sve nule, i $n$ operacija; $i$-ta operacija zadana je brojevima $l_i, r_i$ ($1 \le l_i < r_i \le 2n$) i postavlja $a_{l_i}, \dots, a_{r_i - 1}$ na vrijednost $i$. Svi brojevi $l_1, \dots, l_n, r_1, \dots, r_n$ su međusobno različiti.</p>
<p>Svaku operaciju treba izvesti točno jednom, u proizvoljnom redoslijedu. Maksimiziraj broj indeksa $i$ ($0 \le i < 2n$) za koje je na kraju $a_i \ne a_{i+1}$.</p>
<h3>Ulaz</h3>
<p>Prvi redak sadrži $n$ ($1 \le n \le 5 \cdot 10^3$); slijedi $n$ redaka s $l_i, r_i$.</p>
<h3>Izlaz</h3>
<p>Ispiši najveći mogući broj takvih indeksa.</p>
<h3>Primjer</h3>
<p>Za intervale $[2,3], [6,7], [1,9], [5,10], [4,8]$ odgovor je $9$.</p>
''',
    'hints': [
        r'''<p>Promijeni perspektivu: granica $a_i \ne a_{i+1}$ može nastati samo na krajnjoj točki nekog intervala ($i = l_j$ ili $i = r_j$), i to samo ako je taj kraj „vidljiv” na kraju — interval $j$ je izveden nakon svih intervala koji tu točku pokrivaju iznutra. Koje skupove krajnjih točaka možemo istodobno učiniti vidljivima?</p>''',
        r'''<p>Ako se intervali $[l_1, r_1]$ i $[l_2, r_2]$ križaju ($l_1 < l_2 < r_1 < r_2$), vidljivost točke $l_2$ zahtijeva „$1$ prije $2$”, a vidljivost $r_1$ zahtijeva „$2$ prije $1$”. Dakle $r_1$ i $l_2$ su nekompatibilni — spoji ih bridom. Odabrani skup mora biti nezavisan skup u tom grafu.</p>''',
        r'''<p>Graf je bipartitan (bridovi idu samo između lijevih i desnih krajeva). Pokaži da nezavisnost dovoljna (poredak koji ostvaruje sve zahtjeve nema ciklus). Najveći nezavisan skup u bipartitnom grafu $= 2n - $ najveće sparivanje. Pazi na memoriju od $16$ MB — graf može imati $\Theta(n^2)$ bridova!</p>''',
    ],
    'coach': [
        ('Gdje uopće može nastati granica $a_i \\ne a_{i+1}$ i što je odlučuje?',
         r'''
<p>Susjedne ćelije $x - 1$ i $x$ pokrivaju isti intervali osim onih s krajem točno u $x$; kako su svi $2n$ krajevi različiti i leže u $[1, 2n]$, svaki $x \in [1, 2n]$ je kraj točno jednog intervala $j$, a kandidati za granicu su točno $2n$ mjesta. Intervali koji strogo sadrže $x$ ($l < x < r$) pokrivaju obje ćelije. Konačna vrijednost ćelije je posljednja operacija koja je pokriva, pa se ćelije razlikuju točno kad je $j$ izveden <em>nakon</em> svih intervala koji strogo sadrže $x$ — tada jedna ćelija ima vrijednost $j$, a druga ne. Kraj $x$ je tada „vidljiv”.</p>
'''),
        ('Koje kombinacije vidljivih krajeva su međusobno proturječne?',
         r'''
<p>Vidljivost kraja $x$ intervala $j$ zahtijeva „$a$ prije $j$” za svaki $a$ koji strogo sadrži $x$. Za ugniježđene intervale $b \subset a$ svi zahtjevi glase „$a$ prije $b$”, a disjunktni intervali nemaju zahtjeva — nema proturječja. Za križajuće $l_a < l_b < r_a < r_b$ kraj $l_b$ je unutar $a$ (zahtjev $a$ prije $b$), a kraj $r_a$ unutar $b$ (zahtjev $b$ prije $a$): $r_a$ i $l_b$ ne mogu biti vidljivi zajedno. Skup vidljivih krajeva mora biti nezavisan skup u grafu s bridom $r_a$–$l_b$ za svaki križajući par.</p>
'''),
        ('Zašto je nezavisnost i dovoljna — kako iz nezavisnog skupa izgraditi redoslijed?',
         r'''
<p>Treba pokazati da uvijek postoji interval koji smije ići prvi („izvor”): nijedan njegov odabrani kraj ne leži strogo unutar drugog preostalog intervala. Krenemo od intervala $z$ s najmanjim $l$; smeta samo njegov odabrani $r_z$ ako je unutar nekih intervala, a svi oni križaju $z$, pa im lijevi krajevi <em>nisu</em> odabrani. Uzmemo među njima onaj s najvećim $r$ i ponovimo: opet mu smeta samo desni kraj, opet ga sadrže samo intervali koji ga križaju (interval koji bi ga obuhvaćao bio bi kandidat u prethodnom koraku s većim $r$). Desni krajevi strogo rastu, pa postupak stane na izvoru. Uklanjanjem izvora i ponavljanjem dobivamo redoslijed koji ostvaruje sve odabrane krajeve.</p>
'''),
        ('Koji je najveći nezavisan skup u ovom grafu i kako ga izračunati?',
         r'''
<p>Bridovi spajaju isključivo desne krajeve s lijevima — graf je bipartitan. Po Kőnigovu teoremu najveći nezavisan skup bipartitnog grafa ima $2n - \nu$ vrhova, gdje je $\nu$ najveće sparivanje. Preostaje sparivanje na grafu s do $\Theta(n^2) \approx 10^7$ bridova.</p>
'''),
        ('Kako provesti sparivanje u $16$ MB memorije kad graf ima $10^7$ bridova?',
         r'''
<p>Ne pohranjujemo bridove — susjed desnog kraja $r_a$ je svaki interval $b$ s $l_a < l_b < r_a$ i $r_b > r_a$, što je raspon pozicija u poretku po $l$ uz uvjet na $r$. Segmentno stablo maksimuma $r$ nad tim poretkom u $O(\log n)$ nađe bilo koju neposjećenu poziciju u rasponu s $r_b > r_a$; posjećene brišemo postavljanjem na $-\infty$. Kuhnov algoritam tako po fazi troši $O(n \log n)$ i $O(n)$ memorije: ukupno $O(n^2 \log n)$, što za $n = 5000$ prolazi (lokalno $0.5$ s).</p>
'''),
    ],
    'tips': [
        r'''Kad operacije „prebojavaju” intervale, razmišljaj o <em>krajevima</em>: konačna slika ovisi samo o tome koje su krajnje točke vidljive, a vidljivost je uvjet „izvedi nakon svih koji te strogo sadrže”. Time se redoslijed operacija pretvara u skup relacija prethodnosti.''',
        r'''Skup parnih zabrana („ne oboje”) + dokaz da parne zabrane dovoljno opisuju ostvarivost = najveći nezavisan skup; ako se zabrane pojavljuju samo između dvaju tipova objekata, graf je bipartitan i vrijedi $\alpha = |V| - \nu$ (Kőnig).''',
        r'''Dovoljnost skupa relacija prethodnosti dokazuj postojanjem izvora (ili ponora) u svakoj podfamiliji — to je ekvivalentno acikličnosti i često lakše nego izravno loviti ciklus.''',
        r'''Sparivanje na gustom, ali implicitno zadanom grafu: susjede opisuj kao „raspon + uvjet” i traži neposjećene segmentnim stablom ili skupom — memorija pada s $O(n^2)$ na $O(n)$, a složenost dobiva samo faktor $\log n$.''',
    ],
    'solution': r'''
<p>Promijenimo način gledanja: odabiremo skup krajnjih točaka intervala koje će na kraju doprinijeti odgovoru (biti mjesta promjene vrijednosti), i želimo da taj skup bude što veći, a da postoji redoslijed operacija koji sve odabrane točke doista čini vidljivima.</p>
<p>Za intervale $[l_1, r_1]$ i $[l_2, r_2]$ s $l_1 < l_2 < r_1 < r_2$ vrijedi: ako odaberemo $l_2$, interval $[l_1, r_1]$ mora biti izveden prije $[l_2, r_2]$; ako odaberemo $r_1$, interval $[l_2, r_2]$ mora biti izveden prije $[l_1, r_1]$. Zato $r_1$ i $l_2$ ne mogu biti odabrani istodobno — spojimo ih bridom neusmjerenog grafa. Odabrani skup mora biti <strong>nezavisan skup</strong> u tom grafu.</p>
<p>Pokažimo da je to i dovoljno, tj. da relacije „prije” koje zadaje nezavisan skup ne stvaraju ciklus. Pretpostavimo da ciklus postoji i da u njemu neki brid dolazi od odabranog desnog kraja $r$ intervala $[l, r]$, što zahtijeva da taj interval bude izveden nakon nekog $[l', r']$ s $l < l' < r < r'$. Kako $l'$ nije odabran, sljedeći brid ciklusa nastaje zbog odabira $r'$; nastavljajući tako, desni krajevi duž lanca strogo rastu, pa se lanac ne može zatvoriti u ciklus. Dakle uvjet nezavisnosti je dovoljan.</p>
<p>Problem se time sveo na najveći nezavisan skup. Kako bridovi spajaju samo lijeve krajeve s desnima, graf je bipartitan, pa je najveći nezavisan skup jednak $2n$ minus veličina najvećeg sparivanja. Moguće implementacije:</p>
<ul>
    <li>mađarski (Kuhnov) algoritam ubrzan bitsetom: $O(n^3 / w)$;</li>
    <li>Dinic nad grafom izgrađenim perzistentnim segmentnim stablom: $O(n^2 \log n)$;</li>
    <li>Hopcroft–Karp uz segmentno stablo: $O(n^{1.5} \log n)$.</li>
</ul>
<p>Sva tri pristupa prolaze. Memorijsko ograničenje od $16$ MB postavljeno je kako bi se onemogućila optimizirana intervalna dinamička programiranja; uobičajene implementacije gornjih algoritama sparivanja nemaju problema s memorijom.</p>
''',
    'detailed': r'''
<h3>Što doprinosi odgovoru</h3>
<p>Operacija $i$ postavlja ćelije $l_i, \dots, r_i - 1$ na $i$; promatramo granice između ćelija $x - 1$ i $x$ za $x = 1, \dots, 2n$ (to su indeksi $i = x - 1$ iz zadatka). Ćelije $x - 1$ i $x$ pokriva isti skup intervala, osim onih kojima je $x$ kraj: interval $[l, r)$ pokriva $x - 1$ a ne $x$ ako je $r = x$, odnosno $x$ a ne $x - 1$ ako je $l = x$. Svi krajevi su različiti i leže u $[1, 2n]$, pa je svaki $x \in [1, 2n]$ kraj <em>točno jednog</em> intervala $j(x)$; granica na mjestima bez kraja ne postoji, a najveći mogući odgovor je $2n$.</p>
<p>Neka $C(x) = \{ a : l_a < x < r_a \}$ budu intervali koji strogo sadrže $x$ — oni pokrivaju obje ćelije. Konačna vrijednost ćelije jednaka je posljednjoj izvedenoj operaciji koja je pokriva. Ako je $j = j(x)$ izveden nakon svih intervala iz $C(x)$, ćelija koju $j$ pokriva ima vrijednost $j$, a druga ima vrijednost posljednjeg iz $C(x)$ (ili $0$) — različite. Ako je neki $a \in C(x)$ izveden nakon $j$, obje ćelije završe s istom vrijednošću (posljednji izvedeni iz $C(x)$). Dakle:</p>
<p><em>Granica na $x$ postoji točno kad je $j(x)$ izveden nakon svih intervala iz $C(x)$.</em> Takav kraj zovemo vidljivim.</p>

<h3>Uvjet kompatibilnosti</h3>
<p>Skup $S$ krajeva je ostvariv ako postoji redoslijed u kojem su svi krajevi iz $S$ vidljivi, tj. koji poštuje relacije „$a$ prije $j(x)$” za sve $x \in S$ i $a \in C(x)$. Pogledajmo parove intervala:</p>
<ul>
    <li><strong>Disjunktni:</strong> nijedan kraj jednoga nije unutar drugoga — nema relacija.</li>
    <li><strong>Ugniježđeni</strong> $l_a < l_b < r_b < r_a$: oba kraja $b$ su unutar $a$, krajevi $a$ nisu unutar $b$; sve relacije glase „$a$ prije $b$” — međusobno suglasne.</li>
    <li><strong>Križajući</strong> $l_a < l_b < r_a < r_b$: $l_b \in (l_a, r_a)$ daje „$a$ prije $b$” ako je $l_b \in S$; $r_a \in (l_b, r_b)$ daje „$b$ prije $a$” ako je $r_a \in S$. Oba zajedno su nemoguća: $r_a$ i $l_b$ su <em>u konfliktu</em>.</li>
</ul>
<p>Ostvariv skup je stoga <em>nezavisan skup</em> u grafu $G$ čiji su vrhovi $2n$ krajeva, a bridovi $\{r_a, l_b\}$ za svaki križajući par. Bridovi spajaju samo desne krajeve s lijevima: $G$ je bipartitan.</p>

<h3>Dovoljnost: svaki nezavisan skup je ostvariv</h3>
<p>Neka je $S$ nezavisan. Za familiju intervala $F$ nazovimo interval $z \in F$ <em>izvorom</em> ako nijedan njegov kraj iz $S$ ne leži strogo unutar nekog drugog intervala iz $F$. Izvor smije biti izveden prvi (nema relacije koja bi ga stavljala poslije nekoga iz $F$). Ako svaka neprazna podfamilija ima izvor, redom izvlačimo izvore i dobivamo redoslijed u kojem je svaki $x \in S$ vidljiv: kad je $j(x)$ izvučen, svi intervali iz $C(x)$ već su bili izvučeni.</p>
<p><strong>Lema.</strong> Svaka neprazna $F$ s nezavisnim $S$ ima izvor.</p>
<p><em>Dokaz.</em> Neka je $z_1$ interval s najmanjim $l$; $l_{z_1}$ nije ni u čijoj unutrašnjosti. Označimo $A(z) = \{ a \in F : l_a < r_z < r_a \}$ — intervali koji strogo sadrže $r_z$. Ako $r_{z_1} \notin S$ ili $A(z_1) = \emptyset$, $z_1$ je izvor. Inače svaki $a \in A(z_1)$ ima $l_a > l_{z_1}$, dakle križa $z_1$ ($l_{z_1} < l_a < r_{z_1} < r_a$), pa zbog $r_{z_1} \in S$ i nezavisnosti vrijedi $l_a \notin S$. Neka je $z_2$ element $A(z_1)$ s najvećim $r$. Općenito, za $k \ge 2$ vrijedi: (i) $l_{z_k} \notin S$, (ii) $z_k$ križa $z_{k-1}$, (iii) $z_k$ ima najveći $r$ u $A(z_{k-1})$. Ako $r_{z_k} \notin S$ ili $A(z_k) = \emptyset$, $z_k$ je izvor zbog (i). Inače uzmimo $a \in A(z_k)$. Kad bi bilo $l_a < l_{z_k}$, iz (ii) slijedi $l_a < l_{z_k} < r_{z_{k-1}} < r_{z_k} < r_a$, dakle $a \in A(z_{k-1})$ s $r_a > r_{z_k}$, što proturječi (iii). Zato $l_a > l_{z_k}$: $a$ križa $z_k$ i, jer je $r_{z_k} \in S$, $l_a \notin S$. Neka je $z_{k+1}$ element $A(z_k)$ s najvećim $r$; (i)–(iii) vrijede, a $r_{z_{k+1}} > r_{z_k}$. Desni krajevi strogo rastu, pa niz stane — na izvoru. $\square$</p>
<p>Odgovor je stoga točno veličina najvećeg nezavisnog skupa u $G$.</p>

<h3>Kőnig i sparivanje</h3>
<p>U bipartitnom grafu najveći nezavisan skup ima $|V| - \nu$ vrhova, gdje je $\nu$ najveće sparivanje (komplement najmanjeg vrhovnog pokrivača, Kőnigov teorem). Ovdje $|V| = 2n$, pa je odgovor $2n - \nu$. Graf može imati $\Theta(n^2)$ bridova (npr. $n/2$ intervala koji svi križaju drugih $n/2$): za $n = 5000$ to je do $\approx 6 \cdot 10^6$ parova, čija bi lista susjedstva (uz oznake) probila $16$ MB. Zato bridove ne pohranjujemo.</p>

<h3>Implicitno sparivanje segmentnim stablom</h3>
<p>Desni kraj intervala $a$ susjedan je lijevom kraju intervala $b$ točno kad je $l_a < l_b < r_a$ i $r_b > r_a$. Sortiramo intervale po $l$; tada su kandidati $b$ neprekinut raspon pozicija $(\text{pos}(a), \text{last}(r_a)]$ gdje je $\text{last}(r_a)$ posljednja pozicija s $l_b < r_a$ (binarno pretraživanje), a među njima trebamo one s $r_b > r_a$ koje još nismo posjetili u tekućoj fazi Kuhnova algoritma.</p>
<ul>
    <li>Segmentno stablo nad pozicijama čuva maksimum $r_b$; posjećenu poziciju postavimo na $-\infty$.</li>
    <li>Upit „bilo koja pozicija u rasponu s vrijednošću $> r_a$” silazi samo u čvorove čiji je maksimum $> r_a$: $O(\log n)$.</li>
    <li>Faza za desni kraj $a$: obnovi stablo ($O(n)$), pokreni DFS: uzmi neposjećenog susjeda $b$, označi ga, i ako je slobodan ili se njegov partner može preusmjeriti (rekurzivno), spari $b$ s $a$.</li>
</ul>
<p>Svaka pozicija se u jednoj fazi posjeti najviše jednom, pa faza košta $O(n \log n)$, ukupno $O(n^2 \log n) \approx 3 \cdot 10^8$ jednostavnih operacija (lokalno $0.5$ s uz limit $3$ s). Memorija: nekoliko nizova duljine $O(n)$, daleko ispod $16$ MB. Dubina rekurzije DFS-a je najviše $n = 5000$, što je sigurno.</p>

<h3>Primjer</h3>
<p>Intervali $[2,3], [6,7], [1,9], [5,10], [4,8]$. Križajući parovi: $[1,9]$ i $[5,10]$ (konflikt $9$–$5$), $[4,8]$ i $[5,10]$ (konflikt $8$–$5$); ostali su ugniježđeni ili disjunktni. Graf ima dva brida s zajedničkim vrhom $5$, $\nu = 1$, odgovor $2 \cdot 5 - 1 = 9$: sve krajeve osim $l = 5$ činimo vidljivima, npr. redoslijedom $[5,10], [1,9], [4,8], [2,3], [6,7]$.</p>

<h3>Zamke</h3>
<ul>
    <li>Uvjet križanja mora biti strog s obje strane ($l_a < l_b < r_a < r_b$); ugniježđeni parovi nisu konflikt.</li>
    <li>Vrhove grafa čine krajevi, ne intervali: sparivanje ide između desnih krajeva ($n$ vrhova) i lijevih krajeva ($n$ vrhova) — ista strana intervala nikad nije spojena sama sa sobom.</li>
    <li>Kuhnov algoritam bez implicitnih susjeda ili s <code>vector&lt;vector&gt;</code> lista susjedstva krši memoriju; $n \times n$ bitset ($3$ MB) bi prošao, ali $O(n^3 / w)$ je sporije od pristupa sa segmentnim stablom.</li>
    <li>$n = 1$: odgovor $2$ (oba kraja vidljiva).</li>
</ul>
''',
    'verified': r'''uzorak 1/1; 300 slučajnih testova ($n \le 6$, slučajno sparivanje $2n$ krajeva) protiv brute forcea koji isproba svih $n!$ redoslijeda i doslovno simulira niz; 3 velika testa s $n = 5000$ (svi intervali se međusobno križaju, slučajno sparivanje, sparivanje unutar prozora s mnogo križanja), najviše oko $0.5$ s uz limit $3$ s, memorija $O(n)$.''',
},
# ---------------------------------------------------------------- L
{
    'letter': 'L', 'title': 'Aqre', 'title_hr': 'Aqre', 'slug': 'L_aqre',
    'tl': '1 s', 'ml': '1024 MB',
    'statement': r'''
<p>Matricu $n \times m$ treba ispuniti nulama i jedinicama tako da:</p>
<ul>
    <li>ne postoje četiri uzastopne ćelije u istom retku ili stupcu ispunjene istim brojem;</li>
    <li>ćelije s jedinicama čine (bridno) povezano područje.</li>
</ul>
<p>Konstruiraj matricu s najvećim mogućim brojem jedinica; ispiši taj broj i matricu.</p>
<h3>Ulaz</h3>
<p>Prvi redak sadrži $T$ ($1 \le T \le 10^3$). Svaki test sadrži $n, m$ ($2 \le n, m \le 10^3$). Zbroj svih $n \cdot m$ ne prelazi $10^6$.</p>
<h3>Izlaz</h3>
<p>Za svaki test ispiši najveći broj jedinica i zatim matricu ($n$ redaka); bilo koje optimalno rješenje se prihvaća.</p>
<h3>Primjer</h3>
<p>Za $2 \times 2$ odgovor je $4$; za $3 \times 4$ odgovor je $9$ (npr. tri retka $1110$); za $3 \times 8$ odgovor je $18$.</p>
''',
    'hints': [
        r'''<p>Gornja granica: ako se ploča može podijeliti na disjunktne pravokutnike $1 \times 4$ (vodoravne ili okomite), svaki mora sadržavati barem jednu nulu. Oboji ćelije s $(i + j) \bmod 4$ — svaki $1 \times 4$ pokriva po jednu ćeliju svake od četiri „boje”.</p>''',
        r'''<p>Za $n, m \ge 4$ granica $nm - \min_c |\{(i,j): (i+j) \bmod 4 = c\}|$ je dostižna, i to periodičnim uzorkom $4 \times 4$. Ne moraš ga pogađati: isprobaj sve uzorke $4 \times 4$ s točno četiri nule i lokalno provjeri povezanost i valjanost za nekoliko dimenzija.</p>''',
        r'''<p>Za $n \le 3$ (ili $m \le 3$) okomitih $1 \times 4$ nema, pa argument ne prolazi doslovno; potrebna je zasebna analiza. Posebno je slučaj $3 \times (4k + 3)$ — tu treba posebna konstrukcija.</p>''',
    ],
    'coach': [
        ('Kako dobiti gornju granicu za broj jedinica — što svaki komad ploče „mora” sadržavati?',
         r'''
<p>Svaki pravokutnik $1 \times 4$ (u retku ili stupcu) sadrži barem jednu nulu, pa je nula barem koliko i disjunktnih pravokutnika $1 \times 4$ koje možemo smjestiti na ploču. Koliko ih najviše ima? Obojimo ćeliju $(i, j)$ bojom $(i + j) \bmod 4$: svaki $1 \times 4$ pokriva po jednu ćeliju svake boje, pa ih je najviše $\min_c k_c$, gdje je $k_c$ broj ćelija boje $c$. Za $n, m \ge 4$ toliko ih se doista može smjestiti (dokaz: skidanjem traka širine $4$ svodimo se na $4 \le n, m \le 7$ i tamo eksplicitno slažemo, npr. „vjetrenjačom” za $7 \times 7$). Dakle jedinica je najviše $nm - \min_c k_c$.</p>
'''),
        ('Zašto nule ne smijemo jednostavno staviti na sve ćelije jedne boje?',
         r'''
<p>Nule na cijeloj klasi $(i + j) \bmod 4 = c$ čine dijagonale koje presijecaju ploču — jedinice između susjednih dijagonala nisu povezane. Trebamo drugi raspored s istim brojem nula: po jednoj nuli u svaka četiri uzastopna polja retka i stupca, ali tako da jedinice ostanu povezane. Prirodni kandidat je periodičan uzorak $4 \times 4$ s po jednom nulom u svakom retku i stupcu (permutacijska matrica), obrezan na $n \times m$.</p>
'''),
        ('Kako se uvjeriti da obrezani periodični uzorak ima točno $nm - \\min_c k_c$ jedinica?',
         r'''
<p>Napišimo $n = 4a + r$, $m = 4b + s$ ($0 \le r, s \le 3$). Broj nula je $nb + as + t$, gdje je $t$ broj nula uzorka u kutnom bloku $r \times s$; s druge strane $\min_c k_c = (nm - rs)/4 + k_{\min}(r \times s)$ jer pune trake širine $4$ svakoj boji daju jednako. Uvjet je stoga $t = k_{\min}(r \times s)$, a to je konačna provjera: za oblike do $3 \times 3$ treba prozor uzorka s $0$, $1$ odnosno $2$ nule, što naš uzorak ima. Pomak (faza) uzorka bira se od $16$ mogućih, a povezanost se provjerava BFS-om.</p>
'''),
        ('Što se mijenja kad je $n \\le 3$ i zašto $3 \\times 7$ ne dostiže $18$?',
         r'''
<p>Okomitih $1 \times 4$ nema, pa je gruba granica samo $\lfloor m/4 \rfloor$ nula po retku. Za $m \equiv 2, 3 \pmod 4$ redak s točno $\lfloor m/4 \rfloor$ nula ima gotovo nametnut raspored nula, i pokazuje se da tada u nekom paru susjednih stupaca <em>svaki</em> redak ima nulu — granicu između tih stupaca nijedan put jedinica ne može prijeći, a jedinica ima s obje strane. Zato treba barem jedna nula više: optimum je $2m - \lfloor m/2 \rfloor$ za $n = 2$ i $3m - \lfloor m/4 \rfloor - \lfloor m/2 \rfloor$ za $n = 3$ ($3 \times 7 \to 17$), a dostiže ga jednostavan uzorak: nule na $j \equiv 3$ u gornjim redcima i $j \equiv 1 \pmod 4$ u zadnjem retku.</p>
'''),
        ('Kako implementaciju učiniti sigurnom kad je dokaz dug i pun slučajeva?',
         r'''
<p>Program prije ispisa sam provjeri ploču (pravilo $4$ uzastopnih, povezanost BFS-om, broj jedinica jednak formuli) i za guste ploče isproba faze dok jedna ne prođe. Ukupni trošak je $O(nm)$ po testu, a takva samoprovjera hvata svaku grešku u konstrukciji umjesto da je proslijedi sucu.</p>
'''),
    ],
    'tips': [
        r'''Gornje granice za „bez $k$ uzastopnih” zadatke dobivaju se pakiranjem disjunktnih $1 \times k$ pravokutnika, a njihov broj ograničava bojanje $(i + j) \bmod k$ — svaki pravokutnik pokriva svaku boju točno jednom.''',
        r'''Konstrukcije za velike ploče tražite kao periodične uzorke $k \times k$; kad uzorak pogađaš, napiši program koji enumerira sve kandidate i lokalno provjerava sve uvjete, umjesto da ga dokazuješ na papiru.''',
        r'''Uvjet povezanosti u uskim ploča ($2$–$3$ retka) lomi se argumentom „presjeka”: ako svaki redak ima nulu u istom paru susjednih stupaca, ništa ne prelazi tu granicu.''',
        r'''U konstruktivnim zadacima s puno slučajeva neka rješenje <em>samo</em> provjeri svoj izlaz (validator + BFS) prije ispisa — jeftino je i pretvara tihe greške u glasne.''',
    ],
    'solution': r'''
<p>Ako ploču možemo podijeliti na pravokutnike $1 \times 4$, svaki od njih mora sadržavati barem jednu nulu. Označimo ćelije brojem $(i + j) \bmod 4$; svaki pravokutnik $1 \times 4$ sadrži po jednu ćeliju s oznakama $0, 1, 2, 3$, pa broj disjunktnih pravokutnika $1 \times 4$ ne može premašiti najmanji broj ćelija neke oznake, a za $n, m \ge 4$ ta se granica i dostiže. Time dobivamo gornju granicu za broj jedinica: $nm$ minus najmanji broj ćelija jedne oznake.</p>
<p>Isprobavanjem se može uočiti da se ta gornja granica dostiže periodičnom konstrukcijom s uzorkom $4 \times 4$. Stoga možemo enumerirati sve načine na koje se uzorak $4 \times 4$ može ispuniti i lokalno (programom) provjeriti povezanost te dostiže li se maksimum, a zatim ispisati bilo koje rješenje koje zadovoljava uvjete.</p>
<p>Za $n \le 3$ (ili simetrično $m \le 3$) gornji dokaz ne prolazi: ploču ne možemo rezati okomito na pravokutnike $1 \times 4$, pa se granica temeljena na oznakama $0, 1, 2, 3$ ne dostiže. Također, zbog povezanosti, npr. ploču $3 \times 7$ možemo podijeliti samo na $3$ pravokutnika $1 \times 4$, a kad bismo htjeli dostići tu granicu, ostala bi dva nepovezana bloka $3 \times 3$, što nije dopušteno. Nakon analize ispada da samo slučaj $3 \times (4k + 3)$ zahtijeva posebnu konstrukciju; u svim ostalim slučajevima prethodna metoda i dalje daje optimalno rješenje.</p>
''',
    'detailed': r'''
<h3>Označavanje</h3>
<p>Ćelije indeksiramo $(i, j)$, $0 \le i < n$, $0 \le j < m$. Boja ćelije je $(i + j) \bmod 4$; $k_c$ je broj ćelija boje $c$, a $k_{\min} = \min_c k_c$. Pišemo $n = 4a + r$, $m = 4b + s$ s $0 \le r, s \le 3$. Tražimo najmanji broj nula $Z(n, m)$; odgovor je $nm - Z$.</p>

<h3>Gornja granica preko pakiranja</h3>
<p>Svaki pravokutnik $1 \times 4$ (vodoravan ili okomit) sadrži barem jednu nulu, jer četiri uzastopne jedinice nisu dopuštene. Ako na ploču možemo smjestiti $P$ disjunktnih takvih pravokutnika, onda je $Z \ge P$. Svaki $1 \times 4$ sadrži točno jednu ćeliju svake boje (četiri uzastopne vrijednosti $i + j$), pa je $P \le k_{\min}$.</p>
<p><strong>Tvrdnja.</strong> Za $n, m \ge 4$ postoji pakiranje s točno $k_{\min}$ pravokutnika; dakle $Z \ge k_{\min}$.</p>
<p><em>Dokaz.</em> Traka od $4$ uzastopna retka sadrži u svakom stupcu po jednu ćeliju svake boje, pa je $k_c(n \times m) = k_c((n-4) \times m) + m$ za svaku boju, tj. $k_{\min}$ raste točno za $m$ — koliko okomitih $1 \times 4$ stane u traku. Isto vrijedi za stupce. Skidanjem traka svodimo se na $4 \le n, m \le 7$. Tamo: za $n = 4$ ili $m = 4$ ploča se popločava cijela ($k_{\min} = nm/4$). Za ostale dimenzije $k_{\min}$ ostavlja nepokriveno $rs - 4k_{\min}(r \times s)$ ćelija (vidi dolje), i pakiranje se nalazi izravno: blok $4a \times 4b$, okomiti pravokutnici u desnoj traci širine $s$, vodoravni u donjoj traci visine $r$ pokrivaju sve osim kuta $r \times s$, što je dovoljno kad je $k_{\min}(r \times s) = 0$ (kut $1 \times s$, $2 \times 2$, i transponirani). Preostaju kutovi $2 \times 3$, $3 \times 2$ i $3 \times 3$, gdje treba pokriti još $4$ odnosno $8$ ćelija: npr. $7 \times 7$ se popločava „vjetrenjačom” od četiri bloka $3 \times 4$ oko središnjeg polja ($12 = k_{\min}$ pravokutnika), a $6 \times 7$ s $10$ pravokutnika koji ostavljaju samo dvije ćelije. $\square$</p>

<h3>Konstrukcija za $n, m \ge 4$: periodičan uzorak</h3>
<p>Nule na cijeloj klasi jedne boje daju dijagonalne pruge koje razdvajaju jedinice — ne valja. Umjesto toga koristimo uzorak $4 \times 4$ u kojem je nula u retku $i$ u stupcu $Z_i$, $Z = (2, 3, 1, 0)$:</p>
<pre>1101
1110
1011
0111</pre>
<p>$Z$ je permutacija, pa periodično proširenje ima u svakom retku i stupcu točno jednu nulu na svaka četiri uzastopna polja: nikad četiri jednake uzastopne. Uzorak smijemo pomaknuti za $(dx, dy) \in \{0,1,2,3\}^2$ — $16$ faza — i obrezati na $n \times m$.</p>
<p><strong>Broj nula.</strong> Redak sadrži $b$ punih perioda i još stupce $0 \le j < s$, pa je broj nula $nb + \#\{(i, j) : j < s,\ \text{nula}\}$; slično po stupcima dobivamo $nb + as + t$, gdje je $t$ broj nula u kutnom bloku $r \times s$ (redci $4a \le i < n$, stupci $4b \le j < m$). S druge strane, pune trake širine $4$ daju svakoj boji jednako, pa $k_c(n \times m) = k_c(r \times s) + (nm - rs)/4$ i $k_{\min}(n \times m) = k_{\min}(r \times s) + (nm - rs)/4$. Broj nula $nb + as + t = (nm - rs)/4 + t$, pa je uzorak optimalan točno kad je $t = k_{\min}(r \times s)$.</p>
<p>Za male kutove: $k_{\min} = 0$ ako je $r = 0$, $s = 0$, $\min(r, s) = 1$ ili $r = s = 2$ (neka boja nedostaje); $k_{\min}(2 \times 3) = k_{\min}(3 \times 2) = 1$; $k_{\min}(3 \times 3) = 2$. Uzorak ima prozore odgovarajućeg oblika s točno toliko nula (npr. redci $0,1$ i stupci $0,1$ bez nula; redci $0,1,2$ i stupci $0,1,2$ s dvije nule $(0,2), (2,1)$; redci $0,1$ i stupci $0,1,2$ s jednom nulom), a pomak faze dovodi taj prozor u kut. Time neka faza uvijek daje točno $nm - k_{\min}$ jedinica.</p>
<p><strong>Povezanost.</strong> Nule uzorka su izolirane (nikad dvije bridno susjedne), pa je unutrašnjost povezana; jedino rubno polje može biti odsječeno dvjema dijagonalno postavljenim nulama, što ovisi o fazi. Zato implementacija za svaku od $16$ faza prebroji jedinice i BFS-om provjeri povezanost te uzme prvu fazu koja prolazi. Lokalno smo potvrdili da za <em>sve</em> dimenzije $4 \le n, m \le 1000$ takva faza postoji.</p>

<h3>Uske ploče: $n \le 3$</h3>
<p>Ako je i $m \le 3$, nema četiri uzastopna polja, pa je cijela ploča jedinice ($Z = 0$). Neka je dalje $n \in \{2, 3\}$, $m \ge 4$ (slučaj $m \le 3$, $n \ge 4$ je transponiran). Okomitih $1 \times 4$ nema, pa gruba granica daje samo $Z \ge n \lfloor m/4 \rfloor$.</p>
<p><strong>Lema o presjeku.</strong> Ako svaki redak ima nulu u stupcu $c$ ili $c + 1$, nijedan par jedinica lijevo i desno od granice $c \mid c+1$ nije povezan: put bi morao prijeći granicu vodoravnim bridom u nekom retku, a takav redak ima jedinice u oba stupca $c, c+1$.</p>
<p><strong>Donja granica.</strong> Neka je $m = 4k + \rho$, $\rho \in \{0,1,2,3\}$, i pretpostavimo da svaki redak ima točno $k$ nula na pozicijama $z_1 < \dots < z_k$. Uvjeti $z_1 \le 3$, $z_{i+1} - z_i \le 4$, $m - 1 - z_k \le 3$ daju $4k + \rho - 4 \le z_k \le 4k - 1$.</p>
<ul>
    <li>$\rho = 3$: $z_k = 4k - 1$ i sve nejednakosti su jednakosti: $z_i = 4i - 1$. Svaki redak ima nulu u stupcu $3$, a jedinice postoje s obje strane (stupci $0$–$2$ i $4$ su jedinice) — prema lemi nepovezano. Dakle $Z \ge nk + 1$.</li>
    <li>$\rho = 2$: ukupni „manjak” je najviše $1$, pa je $z_i = 4i - 1$ za $i \le p$ i $z_i = 4i - 2$ za $i > p$, za neki $p \in [0, k]$ ovisan o retku. Neka je $p^*$ najmanji $p$ među redcima. Ako je $p^* = k$, svi redci imaju nulu u stupcu $3$. Inače za $i = p^* + 1$ redak s $p = p^*$ ima nulu u $4i - 2$, a svaki drugi redak u $4i - 2$ ili $4i - 1$; lema s $c = 4i - 2$ (jedinice postoje u stupcu $0$ i u stupcu $m - 1$) daje nepovezanost. Dakle $Z \ge nk + 1$.</li>
    <li>$\rho \in \{0, 1\}$: $Z \ge nk$, i to se dostiže (dolje).</li>
</ul>
<p>Ukupno: $Z(2, m) = \lfloor m/2 \rfloor$ i $Z(3, m) = \lfloor m/4 \rfloor + \lfloor m/2 \rfloor$ (provjeri: za $m = 4k + \rho$ obje formule daju $nk$ za $\rho \le 1$, a $nk + 1$ za $\rho \ge 2$).</p>
<p><strong>Konstrukcija.</strong> Redci $0, \dots, n - 2$ imaju nule na $j \equiv 3 \pmod 4$, zadnji redak na $j \equiv 1 \pmod 4$. Broj nula je $(n - 1)\lfloor m/4 \rfloor + \lfloor (m + 2)/4 \rfloor$, što je točno gornja formula. Nijedan redak nema četiri uzastopne jednake, stupaca visine $4$ nema. Povezanost: segment jedinica $[4t, 4t + 2]$ gornjih redaka dodiruje zadnji redak u stupcima $4t$ i $4t + 2$ (koji su tamo jedinice), a segmenti zadnjeg retka $[4t - 2, 4t]$ i $[4t + 2, 4t + 4]$ spojeni su preko gornjeg segmenta $[4t, 4t + 2]$; polje $(n - 1, 0)$ spojeno je s $(n - 2, 0)$. Primjer $3 \times 7$: <code>1110111 / 1110111 / 1011101</code>, $17$ jedinica — a ne $18$, jer bi $18$ zahtijevalo po jednu nulu u svakom retku, nužno u stupcu $3$, što ostavlja dva nepovezana bloka $3 \times 3$.</p>

<h3>Algoritam</h3>
<ol>
    <li>Ako su $n, m \le 3$: ispiši sve jedinice.</li>
    <li>Ako je $\min(n, m) \le 3$: uski uzorak (po potrebi transponiraj).</li>
    <li>Inače izračunaj $k_{\min}$, za $16$ faza periodičnog uzorka prebroji jedinice i provjeri validnost; ispiši prvu s $nm - k_{\min}$ jedinica koja prolazi.</li>
</ol>
<p>Složenost $O(nm)$ po testu (konstantni faktor $16$ za faze u najgorem slučaju, obično prva ili druga faza prolazi), ukupno $O(\sum nm) \le 1.6 \cdot 10^7$ jednostavnih operacija; memorija $O(nm)$ za tekuću ploču.</p>

<h3>Primjeri iz zadatka</h3>
<ul>
    <li>$2 \times 2$: sve jedinice, $4$.</li>
    <li>$3 \times 4$: $Z = 1 + 2 = 3$, odgovor $9$, npr. <code>1110 / 1110 / 1011</code>.</li>
    <li>$3 \times 8$: $Z = 2 + 4 = 6$, odgovor $18$, npr. <code>11101110 / 11101110 / 10111011</code>.</li>
</ul>

<h3>Zamke</h3>
<ul>
    <li>Ispravno prebrojavanje ćelija po bojama radi se u $O(nm)$ ili formulom; ne miješaj $0$- i $1$-indeksiranje u $(i + j) \bmod 4$ — pomak indeksa samo permutira boje, pa je $k_{\min}$ isti, ali uzorak i faza moraju biti dosljedni.</li>
    <li>Provjera povezanosti BFS-om po fazi mora biti $O(nm)$; ne alociraj $16$ ploča odjednom.</li>
    <li>Slučaj $\min(n, m) \le 3$ obradi <em>prije</em> gustog slučaja; $3 \times (4k + 3)$ nije iznimka u formuli $3m - \lfloor m/4 \rfloor - \lfloor m/2 \rfloor$, ali jest u odnosu na grubu granicu $3 \lfloor m/4 \rfloor$ nula.</li>
    <li>Ispis od do $10^6$ znakova radi po redcima (<code>puts</code>), ne znak po znak s <code>endl</code>.</li>
</ul>
''',
    'verified': r'''uzorak 1/1; 300 slučajnih skupina malih ploča ($2 \le n \le 6$, $2 \le m \le 12$, $nm \le 24$) uz checker koji provjerava format, pravilo četiri uzastopna polja, povezanost jedinica BFS-om i da je broj jedinica jednak optimumu brute forcea (enumeracija redaka); 3 velika testa (do $1000 \times 1000$, uske ploče $2 \times 1000$ i $3 \times 1000$, $\sum nm \le 10^6$), najviše $0.04$ s. Dodatno: egzaktni optimum (CP-SAT) za 55 dimenzija do $11 \times 11$ podudara se s formulom, a rješenje je prošlo checker za <em>svih</em> $20\,126$ parova $(n, m)$ s $2 \le n, m \le 1000$ (u 83 skupine s $\sum nm \le 10^6$).''',
},
# ---------------------------------------------------------------- M
{
    'letter': 'M', 'title': 'Dining Professors', 'title_hr': 'Profesori na večeri', 'slug': 'M_dining_professors',
    'tl': '1 s', 'ml': '256 MB',
    'statement': r'''
<p>Za okruglim stolom sjedi $n$ profesora; profesor $i$ susjedan je profesorima $(i \bmod n) + 1$ i $((i + n - 2) \bmod n) + 1$. Na stolu je $n$ pozicija, pozicija $i$ ispred profesora $i$; profesor $i$ doseže jela na pozicijama $i$ i dvije susjedne. Na svaku poziciju stavlja se točno jedno od $n$ jela, od kojih je $a$ ljutih i $n - a$ neljutih.</p>
<p>Neki profesori ne jedu ljuto. Zadovoljstvo profesora koji jede ljuto jednako je broju jela koja doseže (dakle $3$), a zadovoljstvo profesora koji ne jede ljuto jednako je broju neljutih jela koja doseže. Rasporedi jela tako da zbroj zadovoljstava bude najveći i ispiši taj zbroj.</p>
<h3>Ulaz</h3>
<p>Prvi redak sadrži $n, a$ ($3 \le n \le 10^5$, $0 \le a \le n$). Drugi redak sadrži $b_1, \dots, b_n \in \{0, 1\}$; $b_i = 1$ znači da profesor $i$ jede ljuto.</p>
<h3>Izlaz</h3>
<p>Ispiši najveći mogući zbroj zadovoljstava.</p>
<h3>Primjer</h3>
<p>Za $n = 5$, $a = 2$, $b = [1, 0, 1, 0, 1]$ odgovor je $13$.</p>
''',
    'hints': [
        r'''<p>Zamijeni perspektivu: umjesto po profesorima, računaj doprinos svakog <em>jela</em>. Neljuto jelo na poziciji $i$ zadovoljava sva tri profesora koji ga dosežu; ljuto jelo zadovoljava samo one među njima koji jedu ljuto.</p>''',
        r'''<p>Doprinosi pozicija su neovisni, a broj ljutih jela je fiksan ($a$). Greedy: ljuta jela stavi na $a$ pozicija na kojima najviše od trojice dosežućih profesora jede ljuto.</p>''',
    ],
    'coach': [
        ('Zbroj zadovoljstava zadan je po profesorima — može li se isti zbroj napisati po jelima?',
         r'''
<p>Zadovoljstvo profesora $p$ je broj jela koja doseže i smije jesti. To je zbroj indikatora po parovima (profesor, jelo koje doseže), pa zbroj po profesorima možemo preurediti u zbroj po jelima: jelo na poziciji $i$ doprinosi brojem profesora među $i - 1, i, i + 1$ (ciklički) koji ga smiju jesti. Zamjena redoslijeda zbrajanja je ključni korak jer profesori ovise o tri jela, a jela o tri profesora — no odluku donosimo po jelima.</p>
'''),
        ('Koliko doprinosi neljuto, a koliko ljuto jelo na poziciji $i$?',
         r'''
<p>Neljuto jelo smiju jesti svi, pa doprinosi točno $3$ bez obzira gdje stoji. Ljuto jelo na poziciji $i$ smiju jesti samo profesori koji jedu ljuto: doprinos je $c_i = b_{i-1} + b_i + b_{i+1} \in \{0, 1, 2, 3\}$. Doprinos svake pozicije ovisi samo o tome je li na njoj ljuto jelo — ne o rasporedu ostalih jela.</p>
'''),
        ('Zašto je optimalno ljuta jela staviti na pozicije s najvećim $c_i$, bez ikakve interakcije?',
         r'''
<p>Ako je $S$ skup pozicija s ljutim jelima ($|S| = a$), ukupni zbroj je $3(n - a) + \sum_{i \in S} c_i$: prvi član je konstanta, drugi je zbroj $a$ članova iz fiksnog niza $c$, a različiti $S$ se razlikuju samo po tome koje članove biraju. Zbroj $a$ članova je najveći kad biramo $a$ najvećih — zamjena bilo kojeg odabranog manjeg za neodabrani veći strogo povećava zbroj (argument zamjene). Nema drugih ograničenja: svaki podskup veličine $a$ je ostvariv raspored jer su jela međusobno zamjenjiva.</p>
'''),
        ('Treba li sortirati $n = 10^5$ vrijednosti?',
         r'''
<p>Vrijednosti $c_i$ su iz $\{0, 1, 2, 3\}$, pa dovoljno je prebrojati koliko pozicija ima svaku vrijednost i uzimati od $3$ prema $0$ dok ne podijelimo svih $a$ ljutih jela — $O(n)$ (sortiranje bi bilo $O(n \log n)$, također prolazi).</p>
'''),
    ],
    'tips': [
        r'''Kad je cilj zbroj doprinosa preko parova (agent, resurs), zamijeni redoslijed zbrajanja i računaj po onoj strani na kojoj donosiš odluke — ovdje po jelima, jer je vrsta jela ono što biramo.''',
        r'''„Odaberi točno $a$ od $n$ neovisnih stavki tako da zbroj bude najveći” rješava se biranjem $a$ najvećih; prije toga <em>provjeri</em> da su stavke doista neovisne (doprinos stavke ne ovisi o ostalim odabirima).''',
        r'''Ako vrijednosti dolaze iz malog skupa, sortiranje zamijeni brojanjem (counting) — kraće i brže.''',
        r'''Kod cikličkih susjeda koristi $(i + n - 1) \bmod n$ umjesto $(i - 1) \bmod n$ da izbjegneš negativan ostatak u C++-u.''',
    ],
    'solution': r'''
<p>Za svako jelo razmotrimo koliko ga profesora može jesti ako je ljuto, odnosno ako nije. Neljuto jelo mogu jesti sva tri profesora koji ga dosežu, a ljuto jelo na poziciji $i$ samo oni među profesorima $i-1$, $i$, $i+1$ (ciklički) koji jedu ljuto.</p>
<p>Želimo da što više profesora može jesti, pa jela raspoređujemo greedy: za svaku poziciju izračunamo koliko bi profesora moglo jesti ljuto jelo na njoj, te ljuta jela stavimo na $a$ pozicija s najvećim tim brojem. Odgovor je $3(n - a)$ plus zbroj odabranih vrijednosti.</p>
<p>Vremenska složenost je $O(n)$.</p>
''',
    'detailed': r'''
<h3>Preuređenje zbroja</h3>
<p>Neka je $b_p \in \{0, 1\}$ oznaka jede li profesor $p$ ljuto, a $x_i \in \{\text{ljuto}, \text{neljuto}\}$ vrsta jela na poziciji $i$; sve indekse gledamo ciklički modulo $n$. Profesor $p$ doseže pozicije $p - 1, p, p + 1$ i smije jesti jelo na poziciji $i$ ako je ono neljuto ili $b_p = 1$. Zbroj zadovoljstava je</p>
<p>$$\sum_{p} \sum_{i \in \{p-1, p, p+1\}} [\,x_i \text{ neljuto ili } b_p = 1\,] = \sum_{i} \sum_{p \in \{i-1, i, i+1\}} [\,x_i \text{ neljuto ili } b_p = 1\,],$$</p>
<p>jer je „profesor $p$ doseže poziciju $i$” simetrična relacija ($|p - i| \le 1$ ciklički). Vanjska suma sada ide po jelima. Za $n \ge 3$ su $i - 1, i, i + 1$ tri različita profesora.</p>

<h3>Doprinos jedne pozicije</h3>
<ul>
    <li>Neljuto jelo na poziciji $i$: sva tri profesora ga smiju jesti — doprinos $3$.</li>
    <li>Ljuto jelo na poziciji $i$: doprinos $c_i = b_{i-1} + b_i + b_{i+1} \in \{0, 1, 2, 3\}$.</li>
</ul>
<p>Doprinos pozicije ovisi isključivo o vrsti jela na <em>toj</em> poziciji, a ne o rasporedu ostalih jela: interakcije nema.</p>

<h3>Optimalnost odabira $a$ najvećih</h3>
<p>Neka je $S$ skup pozicija na kojima su ljuta jela; nužno $|S| = a$, a svaki podskup veličine $a$ je ostvariv (jela iste vrste su zamjenjiva). Ukupni zbroj je</p>
<p>$$F(S) = 3(n - a) + \sum_{i \in S} c_i.$$</p>
<p>Prvi član ne ovisi o $S$. Ako $S$ sadrži poziciju $i$ i ne sadrži $j$ s $c_j > c_i$, zamjena $S' = S \setminus \{i\} \cup \{j\}$ daje $F(S') = F(S) + c_j - c_i > F(S)$. Optimalan $S$ stoga ne dopušta takvu zamjenu, tj. sastoji se od $a$ najvećih vrijednosti (uz proizvoljan izbor među jednakima). Kako je $c_i \le 3$, ljuto jelo nikad ne daje više od neljutog, ali broj ljutih jela je fiksan, pa ih moramo smjestiti — i to gdje najmanje „bole”.</p>

<h3>Algoritam</h3>
<ol>
    <li>Za svaku poziciju izračunaj $c_i = b_{(i-1) \bmod n} + b_i + b_{(i+1) \bmod n}$.</li>
    <li>Prebroji $\text{cnt}[v]$ = broj pozicija s $c_i = v$, $v = 0, \dots, 3$.</li>
    <li>Odgovor $= 3(n - a) + \sum_{v = 3}^{0} v \cdot \min(\text{preostalo}, \text{cnt}[v])$, gdje $\text{preostalo}$ počinje s $a$ i smanjuje se za uzeti broj.</li>
</ol>
<p>Složenost $O(n)$ vremena i $O(n)$ memorije (za $b$; $c_i$ ne treba pamtiti). Rezultat je najviše $3n = 3 \cdot 10^5$, pa <code>int</code> dostaje; <code>long long</code> je samo navika.</p>

<h3>Primjer</h3>
<p>$n = 5$, $a = 2$, $b = [1, 0, 1, 0, 1]$. Vrijednosti $c$ (ciklički): $c_1 = b_5 + b_1 + b_2 = 2$, $c_2 = 1 + 0 + 1 = 2$, $c_3 = 0 + 1 + 0 = 1$, $c_4 = 1 + 0 + 1 = 2$, $c_5 = 0 + 1 + 1 = 2$. Dva ljuta jela idu na pozicije s $c = 2$: $3 \cdot 3 + 2 + 2 = 13$.</p>

<h3>Zamke</h3>
<ul>
    <li>$a = 0$ (sve neljuto, odgovor $3n$) i $a = n$ (odgovor $\sum c_i = 3 \sum b_i$) moraju proći bez posebnog koda — petlja s $\min(\text{preostalo}, \text{cnt}[v])$ to rješava.</li>
    <li>Ciklički indeksi: $(i + n - 1) \bmod n$, ne $(i - 1) \bmod n$, koji za $i = 0$ daje $-1$ u C++-u.</li>
    <li>Ne pokušavaj optimizirati po profesorima (npr. „daj ljuto onima koji ga jedu”): profesor doseže tri jela, pa se odluke preklapaju; tek preuređenje po jelima uklanja ovisnosti.</li>
</ul>
''',
    'verified': r'''uzorak 1/1; 300 slučajnih testova ($3 \le n \le 10$, sve vrijednosti $a$, razni udjeli ljubitelja ljutog) protiv brute forcea koji isproba sve rasporede $a$ ljutih jela na $n$ pozicija; 3 velika testa s $n = 10^5$ ($0.01$ s).''',
},
]
