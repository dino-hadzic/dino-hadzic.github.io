# -*- coding: utf-8 -*-
STAGE = {
    'no': 17,
    'name': 'Stage 17: Guangzhou',
    'source_name': 'The 2022 CCPC Final (Guangzhou), May 20-21, 2023',
    'source_html': r'''
<p>Zadatke je pripremio autorski tim CCPC Finala 2022 (Qingyu i suradnici). Prijevod službenog rješenja: <a href="https://contest.ucup.ac/download.php?type=attachments&amp;id=1244&amp;r=1">Tutorial (zh-cn)</a>. Tekst zadatka preveden je prema službenim <a href="https://contest.ucup.ac/download.php?type=attachments&amp;id=1244&amp;r=0">engleskim tekstovima zadataka</a>. Zadatak je dostupan na <a href="https://contest.ucup.ac/contest/1244">Universal Cup Judging System</a>.</p>
''',
}

PROBLEMS = [
# ---------------------------------------------------------------- A
{
    'letter': 'A', 'title': 'Graph Partitioning', 'title_hr': 'Particija grafa', 'slug': 'A_graph_partitioning',
    'tl': '3 s', 'ml': '1024 MiB',
    'statement': r'''
<p>Mala Plava Riba i Xiao Qing Yu imaju po jedno korijensko stablo s $n$ vrhova označenih $1, \dots, n$. Stablo $T_1$ ima korijen $1$ i za svaki $2 \le x \le n$ vrijedi $\mathrm{par}_{T_1}(x) \lt x$. Stablo $T_2$ ima korijen $n$ i za svaki $1 \le x \lt n$ vrijedi $\mathrm{par}_{T_2}(x) \gt x$.</p>
<p>Spojili su svoja stabla u graf $G = (V, E)$ na istom skupu vrhova, gdje je $E$ <em>multiskupovna</em> unija $E_1$ i $E_2$ (brid koji je u oba stabla pojavljuje se dvaput). Dani su bridovi grafa $G$; izračunaj koliko različitih parova stabala $(T_1, T_2)$ daje upravo takav $G$. Dva para su različita ako postoji brid koji je u jednom stablu, a nije u drugom; višestruki bridovi u $G$ smatraju se različitim bridovima. Odgovor ispiši modulo $998244353$.</p>
<h3>Ulaz</h3>
<p>$n$ ($1 \le n \le 5 \cdot 10^5$), zatim $2n - 2$ bridova $(u_i, v_i)$. U grafu mogu postojati višestruki bridovi i petlje; moguće je i da ne postoji nijedan valjan par $(T_1, T_2)$.</p>
<h3>Izlaz</h3>
<p>Broj parova modulo $998244353$.</p>
<h3>Primjeri</h3>
<p>$n = 2$, bridovi $(1,2), (1,2)$: odgovor $2$. $n = 1$: odgovor $1$. $n = 3$, bridovi $(1,2), (2,3), (1,3), (2,2)$: odgovor $0$. $n = 6$, bridovi $(3,4), (1,3), (3,5), (1,6), (6,5), (4,2), (5,4), (1,2), (4,1), (5,3)$: odgovor $2$.</p>
''',
    'hints': [
        r'''<p>Stablo je jednoznačno određeno izborom roditelja za svaki vrh koji nije korijen. U $T_1$ svaki $x \in [2, n]$ treba <em>manjeg</em> roditelja, u $T_2$ svaki $x \in [1, n-1]$ treba <em>većeg</em>. To je ukupno $2n - 2$ „mjesta” — točno koliko i bridova.</p>''',
        r'''<p>Brid $(x, y)$ s $x \lt y$ može poslužiti samo kao brid $y \to \mathrm{par}_{T_1}(y) = x$ ili kao brid $x \to \mathrm{par}_{T_2}(x) = y$. Dakle svaki brid mora biti dodijeljen jednom od dva mjesta — kad graf na mjestima ima „broj bridova = broj vrhova” u svakoj komponenti?</p>''',
    ],
    'coach': [
        (r'''Što zapravo znači „odabrati stablo” kad su nam pravila o roditeljima tako stroga?''',
         r'''<p>U $T_1$ svaki vrh $x \ge 2$ ima roditelja koji je <em>manji</em> od njega, a u $T_2$ svaki vrh $x \le n-1$ roditelja koji je <em>veći</em>. Kad za svaki vrh odaberemo takvog roditelja, cikl ne može nastati (duž bilo kojeg puta prema roditelju brojevi strogo padaju odnosno rastu), pa je svaki takav izbor automatski stablo. Dakle par $(T_1, T_2)$ nije ništa drugo nego popunjavanje $2n-2$ „mjesta”: <em>T1-roditelj od $y$</em> za $y = 2, \dots, n$ i <em>T2-roditelj od $x$</em> za $x = 1, \dots, n-1$.</p>'''),
        (r'''Na koliko načina jedan ulazni brid može poslužiti kao roditeljski brid?''',
         r'''<p>Brid $\{x, y\}$ s $x \lt y$ u $T_1$ može biti samo brid $y \to x$ (manji je roditelj), a u $T_2$ samo brid $x \to y$. Dakle svaki brid ima <em>točno dva</em> kandidata za mjesto: $T_1{:}y$ ili $T_2{:}x$. Petlja $\{x, x\}$ nema nijednog kandidata – čim je vidimo, odgovor je $0$. Budući da je bridova točno $2n-2$ koliko i mjesta, tražimo bijekciju: svako mjesto dobiva točno jedan brid, svaki brid odlazi na jedno od svoja dva mjesta.</p>'''),
        (r'''Koja poznata struktura opisuje „svaki objekt bira jedno od dva mjesta, svako mjesto prima točno jedan objekt”?''',
         r'''<p>Pomoćni graf: vrhovi su mjesta, a svaki ulazni brid je brid između svoja dva kandidata. Dodjela brida mjestu je orijentacija tog pomoćnog brida (usmjerimo ga prema mjestu koje popunjava). Traži se orijentacija u kojoj svaki vrh ima ulazni stupanj točno $1$. Takva orijentacija postoji ako i samo ako svaka komponenta ima jednako mnogo bridova i vrhova – tj. sadrži točno jedan ciklus (pseudostablo). Budući da je ukupno bridova jednako ukupno vrhova, dovoljno je provjeriti da nijedna komponenta nema „višak”.</p>'''),
        (r'''Koliko orijentacija s ulaznim stupnjem $1$ ima jedno pseudostablo?''',
         r'''<p>Točno dvije. Bridovi izvan ciklusa („repovi” obješeni na ciklus) prisiljeni su: list ima samo jedan brid, pa mora njime dobiti svoj jedan ulaz, i tako induktivno prema ciklusu. Na samom ciklusu svaki vrh mora dobiti ulaz iz jednog od dva ciklička brida, što je moguće samo ako sve bridove ciklusa usmjerimo „u krug” – u jednom od dva smjera. Dvostruki brid (ciklus duljine $2$) ne kvari argument – daje dvije orijentacije kao i svaki ciklus; petlji u pomoćnom grafu nema jer su mjesta $T_1{:}y$ i $T_2{:}x$ uvijek različita. Odgovor je $2^{C}$ za $C$ komponenata.</p>'''),
    ],
    'tips': [
        r'''Kad zadatak broji strukture „na $n$ vrhova s fiksnim korijenom i uređenjem po oznakama”, prvo provjeri je li struktura ekvivalentna nezavisnom izboru roditelja za svaki vrh – tada se brojanje stabala pretvara u brojanje dodjela.''',
        r'''„Svaki objekt bira jedno od dva mjesta, svako mjesto točno jednom” je orijentacija grafa s ulaznim stupnjem $1$: rješiva komponenta ima <em>točno</em> jedan ciklus i točno $2$ rješenja (ako je ciklus duljine $\ge 2$). Isti obrazac rješava i zadatke tipa „$n$ ljudi, $n$ stolica, svatko ima dvije dopuštene stolice”.''',
        r'''Za brojanje vrhova i bridova po komponentama DSU je dovoljan; izbjegni rekurzivni DFS na $10^6$ vrhova zbog dubine rekurzije.''',
    ],
    'solution': r'''
<p>Stablo možemo promatrati kao izbor roditelja za svaki vrh: zadatak traži da svaki vrh iz $[1, n-1]$ dobije većeg roditelja (u $T_2$), a svaki vrh iz $[2, n]$ manjeg roditelja (u $T_1$).</p>
<p>Brid koji spaja $x$ i $y$ ($x \le y$) može postati brid od $x$ prema njegovom roditelju u stablu s većim roditeljima ili brid od $y$ prema njegovom roditelju u stablu s manjim roditeljima. Cijeli zadatak svodi se na to da svaki brid uparimo s jednim „mjestom” (vrhom jednog od dvaju stabala kojemu treba roditelj).</p>
<p>Ukupno postoji $2n - 2$ mjesta kojima treba odrediti roditelja, a u ulazu je točno $2n - 2$ bridova. Konstruiramo graf na mjestima u kojem svaki ulazni brid spaja svoja dva moguća mjesta. Rješenje postoji ako i samo ako je taj graf šuma <em>pseudostabala</em> — u svakoj komponenti broj bridova jednak je broju vrhova (komponenta sadrži točno jedan ciklus). Tada svaka komponenta ima točno dvije valjane dodjele (ciklus se može „orijentirati” na dva načina, a stabla obješena na ciklus su prisiljena), pa je odgovor $2^C$, gdje je $C$ broj komponenata.</p>
<p>Petlja $(x, x)$ ne može popuniti nijedno mjesto (roditelj mora biti strogo manji odnosno strogo veći), pa je tada odgovor $0$. Ukupna složenost je $O(n)$.</p>
<p><em>Zanimljivost:</em> zadatak je svojedobno bio planiran kao zadatak za interno natjecanje kineske reprezentacije.</p>
''',
    'detailed': r'''
<h3>1. Stablo kao vektor roditelja</h3>
<p>Stablo $T_1$ ima korijen $1$ i za svaki $x \ge 2$ vrijedi $\mathrm{par}_{T_1}(x) \lt x$. Tvrdimo da je <em>bilo koji</em> izbor $\mathrm{par}(x) \in \{1, \dots, x-1\}$ za sve $x \ge 2$ valjano stablo, i obratno. Obrat je jasan. Za prvi smjer: krenemo li iz bilo kojeg vrha i stalno skačemo na roditelja, vrijednosti strogo padaju, pa nakon najviše $x-1$ skokova stignemo u $1$ – nema ciklusa, svaki vrh je povezan s korijenom, a $n-1$ bridova na $n$ vrhova povezanog grafa je stablo. Isto vrijedi za $T_2$ s korijenom $n$ i $\mathrm{par}_{T_2}(x) \gt x$.</p>
<p>Zato par $(T_1, T_2)$ potpuno opisuje popunjavanje točno $2n-2$ <strong>mjesta</strong>:</p>
<ul>
<li>mjesto $T_1{:}y$ za $y = 2, \dots, n$ (tko je roditelj od $y$ u $T_1$; brid je $\{y, \mathrm{par}_{T_1}(y)\}$ s manjim drugim krajem),</li>
<li>mjesto $T_2{:}x$ za $x = 1, \dots, n-1$ (tko je roditelj od $x$ u $T_2$; brid je $\{x, \mathrm{par}_{T_2}(x)\}$ s većim drugim krajem).</li>
</ul>
<p>Dva para su različita ako se razlikuju u nekom bridu; kako je u multiskupu $E$ svaki brid jedinstven objekt, različiti parovi odgovaraju različitim dodjelama bridova mjestima.</p>

<h3>2. Svaki brid ima točno dva kandidata</h3>
<p>Uzmimo ulazni brid $\{u, v\}$ i neka je $x = \min(u, v)$, $y = \max(u, v)$. Ako je taj brid u $T_1$, njegov „donji” kraj (dijete) mora biti veći: dijete je $y$, roditelj $x$ – brid popunjava mjesto $T_1{:}y$. Ako je u $T_2$, dijete je manji kraj $x$ – brid popunjava mjesto $T_2{:}x$. Drugih mogućnosti nema. Ako je $u = v$ (petlja), brid ne može popuniti ništa, pa je odgovor $0$ – to je prvi rubni slučaj koji rješenje mora provjeriti.</p>
<p>Zadatak je time sveden na: <em>zadano je $2n-2$ mjesta i $2n-2$ bridova, svaki brid ima dva dopuštena mjesta; na koliko načina možemo svakom bridu dodijeliti jedno od njegovih mjesta tako da svako mjesto dobije točno jedan brid?</em></p>

<h3>3. Pomoćni graf i orijentacije</h3>
<p>Napravimo graf $H$ čiji su vrhovi mjesta (ima ih $2n-2$), a svaki ulazni brid $\{x, y\}$ postaje brid $H$ između mjesta $T_1{:}y$ i $T_2{:}x$. Ta su dva mjesta uvijek različita (jedno je „T1-mjesto”, drugo „T2-mjesto”), pa $H$ nema petlji, ali može imati višestruke bridove (isti par $\{x,y\}$ dvaput u ulazu). Dodijeliti brid mjestu znači <strong>orijentirati</strong> ga prema tom mjestu; uvjet „svako mjesto točno jedan brid” postaje „svaki vrh grafa $H$ ima ulazni stupanj točno $1$”.</p>
<p><strong>Lema.</strong> Povezan graf s $V$ vrhova i $E$ bridova ima orijentaciju u kojoj svaki vrh ima ulazni stupanj $1$ ako i samo ako je $E = V$. Broj takvih orijentacija tada je $2$ (za ciklus duljine $\ge 2$; višestruki brid je ciklus duljine $2$).</p>
<p><em>Dokaz.</em> Nužnost: zbroj ulaznih stupnjeva je $E$, a mora biti $V$. Dovoljnost i brojanje: povezan graf s $E = V$ sadrži točno jedan ciklus (stablo ima $V-1$ bridova; dodatni brid zatvara točno jedan ciklus), a ostatak su stabla „obješena” na vrhove ciklusa. Orijentaciju gradimo od listova: list ima jedan brid, pa ga mora dobiti kao ulaz – brid je prisiljen usmjeren prema listu. Uklonimo list; njegov je susjed izgubio jedan brid, ali ne i potrebu za ulazom, pa se argument ponavlja sve dok ne ostane sam ciklus. Na ciklusu duljine $k$ imamo $k$ vrhova i $k$ bridova; svaki vrh treba točno jedan ulaz od svoja dva ciklička brida. Ako je brid $(v_1, v_2)$ usmjeren prema $v_2$, tada $v_2$ već ima ulaz, pa brid $(v_2, v_3)$ mora ići prema $v_3$, itd. – izbor prvog brida određuje sve, a oba su izbora konzistentna. Dakle točno $2$ orijentacije. $\square$</p>
<p>Budući da $H$ ukupno ima jednako mnogo bridova i vrhova, uvjet $E_i = V_i$ za svaku komponentu $i$ ekvivalentan je uvjetu $E_i \le V_i$ za sve (ili $E_i \ge V_i$ za sve). Ako neka komponenta ima $E_i \ne V_i$, odgovor je $0$; inače je odgovor $2^{C}$, gdje je $C$ broj komponenata. Komponente su nezavisne jer brid nikad ne povezuje mjesta iz različitih komponenata.</p>

<h3>4. Algoritam</h3>
<ol>
<li>Pročitaj $n$; ako je $n = 1$, nema bridova ni mjesta, $H$ je prazan, $C = 0$ i odgovor je $2^0 = 1$ (vrijedi i formalno, ali dobro je znati da nije poseban slučaj).</li>
<li>Indeksiraj mjesta: $T_1{:}y \mapsto y - 2$ ($y = 2..n$), $T_2{:}x \mapsto (n-1) + (x-1)$ ($x = 1..n-1$); ukupno $2n-2$ indeksa.</li>
<li>Za svaki brid $(u, v)$: ako je $u = v$, zapamti da je odgovor $0$ (bridove ipak treba pročitati do kraja). Inače $x = \min$, $y = \max$ i spoji u DSU-u mjesta $T_1{:}y$ i $T_2{:}x$; u korijenu komponente održavaj broj vrhova $V$ i broj bridova $E$ (kad su već u istoj komponenti samo $E{+}{+}$, inače se veličine zbrajaju i $E$ se povećava za $1$).</li>
<li>Na kraju prođi po korijenima: ako je negdje $V \ne E$, ispiši $0$; inače ispiši $2^{C} \bmod 998244353$.</li>
</ol>

<h3>5. Primjer</h3>
<p>$n = 2$, bridovi $(1,2), (1,2)$. Mjesta su $T_1{:}2$ i $T_2{:}1$. Oba brida spajaju ista dva mjesta: komponenta s $2$ vrha i $2$ brida – dvostruki brid je ciklus duljine $2$. Dvije orijentacije: prvi brid u $T_1$, drugi u $T_2$, ili obratno. Odgovor $2$. Za $n = 3$ s bridovima $(1,2),(2,3),(1,3),(2,2)$ petlja $(2,2)$ odmah daje $0$.</p>

<h3>6. Složenost i zamke</h3>
<p>DSU s kompresijom puta: $O(n\,\alpha(n))$ vremena i $O(n)$ memorije za $n \le 5 \cdot 10^5$. Potencijalne zamke: (a) petlju treba otkriti, a ne „progutati” pretvorbom u brid s $x = y$ (indeksi mjesta $T_1{:}x$ i $T_2{:}x$ tada postoje i ne bi izazvali grešku, ali bi dali kriv odgovor); (b) ne prekidaj čitanje ulaza pri petlji ako nakon toga išta ispisuješ; (c) potencija $2^C$ računa se modularno, $C$ može biti do $2n-2$.</p>
''',
    'verified': r'''uzorci 4/4; 300 slučajnih testova ($n \le 6$, slučajni multiskup od $2n-2$ bridova s petljama i dvostrukim bridovima) protiv brute forcea koji isprobava sve dodjele bridova mjestima; 3 velika testa s $n = 5 \cdot 10^5$ ($\lt 0.3$ s).''',
},
# ---------------------------------------------------------------- B
{
    'letter': 'B', 'title': 'Disjoint Set Union', 'title_hr': 'Disjunktni skupovi (DSU)', 'slug': 'B_disjoint_set_union',
    'tl': '4 s', 'ml': '1024 MiB',
    'statement': r'''
<p>DSU održava šumu korijenskih stabala na $n$ vrhova; vrh $x$ ima roditelja $f[x]$, a $x$ je korijen ako je $f[x] = x$. Operacije:</p>
<ul>
<li><code>find(x)</code>: vraća korijen stabla u kojem je $x$, uz <em>kompresiju puta</em> — svakom vrhu na putu od $x$ do korijena roditelj se postavlja izravno na korijen.</li>
<li><code>unite(x, y)</code>: $x' \leftarrow \mathrm{find}(x)$, $y' \leftarrow \mathrm{find}(y)$; ako je $x' \ne y'$, postavi $f[x'] \leftarrow y'$.</li>
</ul>
<p>Dan je niz $f$ nastao nekim slijedom takvih operacija iz početnog stanja $f[i] = i$, te ciljni niz $g$. Može li se dodatnim operacijama <code>find</code>/<code>unite</code> postići $f = g$? Ako može, ispiši slijed od najviše $2n^2$ operacija.</p>
<h3>Ulaz</h3>
<p>$T \le 10^5$ testova; $n$ ($3 \le n \le 1000$), nizovi $f$ i $g$. Jamči se da je $f$ ostvariv. $\sum n^2 \le 5 \cdot 10^6$.</p>
<h3>Izlaz</h3>
<p><code>NO</code>, ili <code>YES</code>, broj operacija $m \le 2n^2$ i operacije u obliku <code>1 x</code> (find) odnosno <code>2 x y</code> (unite).</p>
<h3>Primjer</h3>
<p>$f = (1,2,3,3)$, $g = (1,1,1,2)$: <code>YES</code>, npr. <code>2 3 2</code>, <code>1 4</code>, <code>2 2 1</code>, <code>1 3</code>. Za $f = (1,1,1,1,1)$, $g = (1,2,3,4,5)$: <code>NO</code>.</p>
''',
    'hints': [
        r'''<p>Očite nemogućnosti: $g$ mora biti šuma (bez ciklusa) i vrhovi koji su u $f$ u istom stablu moraju biti u istom stablu i u $g$ (skupovi se nikad ne razdvajaju).</p>''',
        r'''<p><code>find</code> može samo <em>razbiti</em> odnos predak–potomak (podstablo se „podiže” bliže korijenu), nikad stvoriti novi; nove odnose predak–potomak stvara samo <code>unite</code>, i to uvijek između korijena. Zaključi što to znači za korijene $r_1, \dots, r_k$ početnih stabala: ako se u $g$ podstablo od $r_x$ sadrži vrh koji je početno bio u stablu $r_y$, tada je u nekom trenutku $r_x$ bio predak od $r_y$. Ta ograničenja daju usmjereni graf — treba mu topološki poredak.</p>''',
        r'''<p>Vrh $t$ koji početno nije korijen ostaje izravno dijete od $f[t]$ u konačnom stanju ako i samo ako nad njim nikad nije pozvan <code>find</code>. Dakle iz $g$ se točno vidi za koje vrhove treba pozvati <code>find</code>, a najbolje je to učiniti odmah na početku.</p>''',
    ],
    'coach': [
        (r'''Što se uopće može promijeniti u polju $f$ jednom operacijom, i tko sve može postati nečiji roditelj?''',
         r'''<p><code>unite</code> mijenja roditelja samo <em>korijenu</em> (i to na drugi korijen), a <code>find</code> postavlja roditelja vrhova na putu na <em>trenutni korijen</em>. Korijen nikad ne nastaje iznova: skup korijena samo se smanjuje. Zato za svaki vrh $v$ vrijedi da je $g[v]$ ili nepromijenjeni $f[v]$ („zadržan”), ili neki <em>početni</em> korijen. Ako je $g[v] \ne f[v]$ i $g[v]$ nije početni korijen, odgovor je odmah <code>NO</code>; isto ako $g$ ima ciklus ili ako $g$ razdvaja vrhove koji su u $f$ povezani (skupovi se samo spajaju).</p>'''),
        (r'''Koje vrhove <code>find</code> nužno „povlači” sa sobom?''',
         r'''<p><code>find(x)</code> prolazi svim precima od $x$ do korijena i svakome od njih (osim djeci korijena) mijenja roditelja. Ako je $v$ pomaknut ($g[v] \ne f[v]$), onda je u trenutku pomicanja i njegov početni roditelj $f[v]$ bio na putu; ako je $f[v]$ početno na dubini $\ge 2$, njegov roditelj $f[f[v]]$ nije korijen (nije početni korijen, a drugih nema), pa je i $f[v]$ tada pomaknut. Uvjet: <em>pomaknut $v$ s $\mathrm{dub}(f[v]) \ge 2$ povlači pomaknut $f[v]$</em>. Obratno, vrhovi koje treba pomaknuti točno su oni s $g[v] \ne f[v]$ – nad njima ćemo pozvati <code>find</code> odmah na početku, čime svaki postaje dijete svog početnog korijena.</p>'''),
        (r'''U kojem redoslijedu početni korijeni smiju prestati biti korijeni?''',
         r'''<p>Neka vrh $v$ iz početnog stabla s korijenom $r_z$ ima cilj $g[v] = r_x \ne r_z$. Kad roditelj od $v$ posljednji put postaje $r_x$, $r_x$ je korijen stabla koje sadrži $v$, dakle i $r_z$ – pa $r_z$ tada više nije korijen. Ako s $t(r)$ označimo trenutak u kojem $r$ prestaje biti korijen (za konačne korijene $\infty$), dobivamo $t(r_z) \lt t(r_x)$: usmjereni brid $r_z \to r_x$. Ti bridovi moraju činiti DAG; ako imaju ciklus – <code>NO</code>. Topološki poredak DAG-a bit će redoslijed obrade.</p>'''),
        (r'''Kako iz topološkog poretka sastaviti stvarni niz operacija?''',
         r'''<p>Invarijanta: kad obrađujemo korijen $m$, svi „neriješeni” vrhovi u njegovu stablu (oni koji još nisu dijete svog cilja) nalaze se na dubini $\le 2$. <code>find</code> ih podiže na dubinu $1$ – oni s ciljem $m$ time su gotovi, jer <code>find</code> ne prolazi kroz gotove vrhove (djeca korijena se ne mijenjaju). Zatim $m$ spojimo (<code>unite</code>) pod neriješeni cilj s najmanjim $t$; svi vrhovi dubine $1$ postaju dubine $2$ – invarijanta ostaje. Lanac spajanja posjećuje ciljeve u rastućem $t$ i ne može preskočiti nijedan neriješeni (uvijek bira najmanji). Broj operacija: $\le n$ početnih <code>find</code>-ova, po korijenu $\le n$ podizanja i $1$ <code>unite</code>: ukupno $\le n^2 + 2n \le 2n^2$.</p>'''),
        (r'''Kako ovakvu konstrukciju uopće testirati kad izlaz nije jedinstven?''',
         r'''<p>Checkerom koji simulira DSU: primijeni ispisane operacije na $f$ i usporedi s $g$, provjeri $m \le 2n^2$, a presudu <code>YES</code>/<code>NO</code> usporedi s brute forceom koji za $n \le 6$ BFS-om pretražuje sva stanja (broj različitih polja $f$ je malen). Sam <code>sol.cpp</code> dodatno provjerava <code>assert</code>-om da simulacija njegovih operacija daje $g$.</p>'''),
    ],
    'tips': [
        r'''Kod „zadanih operacija koje treba reproducirati” (DSU, stog, heap…) prvo popiši <em>invarijante</em>: što se nikad ne mijenja (skup korijena samo pada), što jedina operacija smije promijeniti (roditelj postaje samo trenutni korijen). Nužni uvjeti obično su i dovoljni.''',
        r'''„$A$ mora prestati biti korijen prije $B$” i slična vremenska ograničenja = DAG + topološki poredak; ciklus u ograničenjima je čist dokaz nemogućnosti.''',
        r'''Konstrukciju provodi u fazama koje čuvaju jednostavnu invarijantu (ovdje: neriješeni vrhovi na dubini $\le 2$) – tada je dokaz ispravnosti kratak, a brojanje operacija mehaničko.''',
        r'''Konstruktivni zadatak s nejedinstvenim izlazom testiraj checkerom koji <em>simulira</em> operacije, a presudu uspoređuj s BFS-om po stanjima za sitne $n$.''',
    ],
    'solution': r'''
<p>Ako konačno stanje sadrži ciklus, ili ako su vrhovi koji su u početnom stanju povezani u konačnom stanju nepovezani, rješenja nema.</p>
<p>Neka početno stanje ima $k$ stabala $T_1, T_2, \dots, T_k$ s korijenima $r_1, r_2, \dots, r_k$. Pretpostavimo da se konačno stanje sastoji od jednog stabla (inače postupak provodimo za svaku komponentu zasebno) i promotrimo strukturu koju u konačnom stanju tvore ti $k$ korijeni.</p>
<p>Ako je $x$ roditelj od $y$ (u konačnom stanju), tada je nužno u nekom koraku $y$ izravno spojen na $x$. Budući da operacija <code>find</code> može samo razbiti odnos predak–potomak neke grupe vrhova, a nikad ne stvara nove odnose predak–potomak, ako u konačnom trenutku vrijedi ograničenje „$x$ mora biti predak od $y$”, to ograničenje mora biti zadovoljeno u svakom trenutku.</p>
<p>Nadalje, ako u konačnom stanju podstablo nekog $r_x$ sadrži vrh $u$ koji se početno nalazio u drugom stablu $r_y$, tada je u nekom trenutku stablo koje sadrži $r_y$ bilo pod $r_x$ (tj. $r_x$ je bio predak od $r_y$). Tako dobivamo niz ograničenja oblika „$r_x$ mora biti predak od $r_y$”. Ako ograničenja tvore ciklus, očito nema rješenja. Inače izračunamo bilo koji topološki poredak i po njemu konstruiramo rješenje.</p>
<p>Primijetimo: ako je $x$ korijen, $y$ neko dijete od $x$, a $z$ neko dijete od $y$, tada operacijom <code>find(z)</code> možemo podstablo od $z$ podignuti tako da $z$ postane dijete od $x$, bez utjecaja na ostatak strukture.</p>
<p>Istodobno, za početno ne-korijenski vrh $t$ vrijedi: $t$ i $f[t]$ u konačnom stanju u odnosu su roditelj–dijete ako i samo ako $t$ nikad nije bio obrađen (nad njim ili kroz njega nije pozvan <code>find</code>). Dakle, iz toga jesu li $x$ i njegov početni roditelj u konačnom stanju u izravnom odnosu roditelj–dijete možemo odlučiti treba li nad $x$ u nekom trenutku pozvati <code>find</code>. Tako znamo nad kojim vrhovima na početku treba izvesti <code>find</code>, a izvesti te operacije odmah na početku sigurno je optimalno.</p>
<p>Nakon toga jednostavno po topološkom poretku redom „obnavljamo” ciljno stablo. Budući da za obradu jednog vrha trošimo najviše $n$ operacija, ukupan broj operacija (čak i grubo procijenjen) ne prelazi $n^2 + n$.</p>
''',
    'detailed': r'''
<h3>1. Što operacije mogu, a što ne mogu</h3>
<p>Promotrimo kako se polje $f$ može mijenjati:</p>
<ul>
<li><code>unite(x, y)</code> mijenja samo $f[x']$ za korijen $x'$, i to na drugi korijen $y'$. Korijen $x'$ time prestaje biti korijen – <em>zauvijek</em>, jer nijedna operacija ne postavlja $f[v] = v$ za vrh koji to nije.</li>
<li><code>find(x)</code> svim vrhovima na putu od $x$ do korijena $r$ postavlja $f[\cdot] = r$. Roditelj se mijenja samo vrhovima na dubini $\ge 2$ (djeca korijena već imaju roditelja $r$).</li>
</ul>
<p>Posljedice. (a) Skup korijena samo se smanjuje; svaki korijen u bilo kojem trenutku je <em>početni</em> korijen. (b) Roditelj vrha $v$ mijenja se samo na trenutni korijen, dakle na početni korijen. Zato je $g[v] \in \{f[v]\} \cup \{\text{početni korijeni}\}$. (c) Skupovi (komponente) samo se spajaju. (d) $g$ mora biti šuma. Ako bilo što od toga ne vrijedi – <code>NO</code>.</p>
<p>Vrh $v$ zovemo <em>pomaknutim</em> ako je $g[v] \ne f[v]$ ($v$ nije početni korijen). Nad pomaknutim vrhom mora u nekom trenutku proći <code>find</code>; nad nepomaknutim ne smije proći nijedan <code>find</code> koji bi mu promijenio roditelja.</p>

<h3>2. Uvjet nasljeđivanja pomaka</h3>
<p><strong>Lema 1.</strong> Ako je $v$ pomaknut i njegov početni roditelj $p = f[v]$ ima početnu dubinu $\ge 2$, tada je i $p$ pomaknut.</p>
<p><em>Dokaz.</em> Prvi <code>find</code> koji mijenja roditelja od $v$ prolazi i kroz $p$ (roditelj od $v$ je do tog trenutka $f[v] = p$). Tada je roditelj od $p$ ili još $f[p]$ – koji nije početni korijen (dubina $\ge 2$), dakle po (a) nije ni trenutni korijen – ili je već promijenjen (pa je $p$ pomaknut). U prvom slučaju <code>find</code> mijenja roditelja od $p$ na korijen $\ne f[p]$, pa je $p$ pomaknut. $\square$</p>
<p>Ako je $\mathrm{dub}(f[v]) = 1$, $f[v]$ je dijete početnog korijena i <code>find</code> mu ne mijenja roditelja dok je taj korijen još korijen – nema ograničenja.</p>

<h3>3. Ograničenja među korijenima</h3>
<p>Neka su početni korijeni $r_1, \dots, r_k$ i neka $t(r)$ označava trenutak u kojem $r$ prestaje biti korijen ($\infty$ ako je korijen i u $g$). Svakom vrhu $v$ s $g[v] \ne f[v]$ (uključujući početne korijene koji u $g$ nisu korijeni) pridružimo <em>cilj</em> $\mathrm{cilj}(v) = g[v]$ – po odjeljku 1 to je početni korijen.</p>
<p><strong>Lema 2.</strong> Ako vrh $v$ iz početnog stabla s korijenom $r_z$ ima cilj $r_x \ne r_z$, tada je $t(r_z) \lt t(r_x)$.</p>
<p><em>Dokaz.</em> U trenutku kad roditelj od $v$ posljednji put postaje $r_x$ (bilo <code>find</code>-om, bilo <code>unite</code>-om ako je $v$ korijen), $r_x$ je korijen stabla koje sadrži $v$. To stablo sadrži i $r_z$ (komponente se ne razdvajaju), a stablo ima jedan korijen, pa $r_z$ više nije korijen: $t(r_z) \lt$ taj trenutak $\le t(r_x)$. $\square$</p>
<p>Bridovi $r_z \to r_x$ moraju stoga činiti aciklički graf; ako sadrže ciklus – <code>NO</code>. Inače uzmemo bilo koji topološki poredak i njegovu poziciju proglasimo za $t(r)$. Konačni korijeni ($g[r] = r$) nemaju izlaznih bridova, pa smiju biti bilo gdje iza svojih prethodnika.</p>

<h3>4. Konstrukcija</h3>
<p><strong>Faza 1.</strong> Za svaki pomaknuti vrh $v$ pozovemo <code>find(v)</code>, još u početnom stanju. Nakon toga je svaki pomaknuti vrh dijete svog početnog korijena. Nijedan nepomaknuti vrh nije promijenjen: <code>find(v)</code> mijenja roditelje pretcima od $v$ na dubini $\ge 2$ (relativno prema početnom stanju, prije bilo kakvog pomicanja – kompresija puta samo skraćuje puteve i ne uvodi nove pretke), a svi takvi su pomaknuti po Lemi 1 primijenjenoj induktivno duž puta.</p>
<p><strong>Faza 2.</strong> Obrađujemo početne korijene $m$ po topološkom poretku. Održavamo skup <code>members[m]</code> vrhova čije se stablo trenutno nalazi pod $m$ i invarijantu:</p>
<blockquote><p>Svi <em>neriješeni</em> vrhovi (imaju cilj, a još nisu njegovo dijete) u stablu korijena $m$ nalaze se na dubini $\le 2$.</p></blockquote>
<p>Nakon Faze 1 invarijanta vrijedi: neriješeni vrhovi su pomaknuti vrhovi (dubina $1$) i sam korijen (dubina $0$). Obrada korijena $m$:</p>
<ol>
<li>Za svaki neriješeni $v \ne m$ na dubini $2$ pozovemo <code>find(v)</code>: $v$ postaje dijete od $m$. Na putu je samo roditelj od $v$ (dijete korijena), kojem <code>find</code> ne mijenja ništa – nijedan gotov vrh ne strada. Ako je $\mathrm{cilj}(v) = m$, $v$ je sada riješen.</li>
<li>Ako je $g[m] = m$, $m$ je konačni korijen; po odjeljku 3 tada više nema neriješenih vrhova (svi ciljevi vrhova u ovom stablu imaju $t \lt t(m)$ – v. dolje) i gotovi smo s ovim stablom.</li>
<li>Inače neka je $b$ neriješeni cilj s najmanjim $t$ među svim članovima stabla (uključujući $\mathrm{cilj}(m) = g[m]$). Pozovemo <code>unite(m, b)</code>: $m$ postaje dijete od $b$ (ako je $\mathrm{cilj}(m) = b$, $m$ je riješen), a svi vrhovi dubine $1$ prelaze na dubinu $2$ – invarijanta za stablo $b$ vrijedi. Članove prebacimo u <code>members[b]</code>.</li>
</ol>
<p><strong>Zašto lanac posjeti svaki cilj.</strong> Stablo koje sadrži vrh $v$ s ciljem $x$ „putuje” po lancu spajanja, u svakom koraku pod neriješeni cilj s najmanjim $t$. Dok je $x$ neriješen, on je kandidat, pa se lanac nikad ne spaja pod korijen s $t$ većim od $t(x)$; budući da $t$ duž lanca strogo raste (po Lemi 2 svaki cilj ima veći $t$ od korijena koji se spaja), lanac u konačno mnogo koraka dolazi točno u $x$ i tamo <code>find(v)</code> rješava $v$. Isti argument pokazuje da spajanjem u $b$ ne mogu „doći” neriješeni ciljevi s $t \lt t(b)$: takav cilj bio bi kandidat već pri prethodnom spajanju. Zato je pri dolasku u konačni korijen sve riješeno, a $b$ je uvijek još korijen (prestaje to biti tek pri vlastitoj obradi, koja je kasnije u poretku).</p>
<p>Na kraju je za svaki vrh $v$: riješen ($f[v] = \mathrm{cilj}(v) = g[v]$), ili bez cilja (nepomaknut, $f[v] = g[v]$ jer ga nijedan <code>find</code> nije dirao, odnosno konačni korijen). Implementacija to i provjerava <code>assert</code>-om simulirajući vlastite operacije.</p>

<h3>5. Broj operacija i složenost</h3>
<p>Faza 1: $\le n$ operacija. Faza 2: pri obradi korijena $m$ najviše $|\text{members}| \le n$ <code>find</code>-ova i jedan <code>unite</code>; korijena je $\le n$. Ukupno $\le n^2 + 2n \le 2n^2$ za $n \ge 2$. Vrijeme $O(n^2)$ po testu (uz simulaciju DSU-a s kompresijom puta), što uz $\sum n^2 \le 5 \cdot 10^6$ prolazi lako; memorija $O(n)$ plus ispis do $2n^2$ redaka – ispisuj u buffer.</p>

<h3>6. Primjer</h3>
<p>$f = (1,2,3,3)$, $g = (1,1,1,2)$. Korijeni u $f$: $1, 2, 3$; vrh $4$ ima $f[4] = 3$, $g[4] = 2$ – pomaknut, cilj $2$ (početni korijen ✓). Ciljevi korijena: $\mathrm{cilj}(2) = 1$, $\mathrm{cilj}(3) = 1$. Bridovi: $3 \to 2$ (zbog vrha $4$), $2 \to 1$, $3 \to 1$; topološki $3, 2, 1$. Faza 1: <code>find(4)</code> (ništa ne mijenja, $4$ je već dijete korijena $3$). Obrada $3$: neriješeni $4$ (cilj $2$) i $3$ (cilj $1$); najmanji $t$ ima $2$ → <code>unite(3, 2)</code>: $f = (1,2,2,3)$. Obrada $2$: $4$ je na dubini $2$ → <code>find(4)</code>: $f = (1,2,2,2)$, $4$ riješen. Neriješeni: $3$ i $2$ s ciljem $1$ → <code>unite(2, 1)</code>: $f = (1,1,2,2)$. Obrada $1$: $3$ na dubini $2$ → <code>find(3)</code>: $f = (1,1,1,2) = g$ ✓. Ispis: <code>1 4</code>, <code>2 3 2</code>, <code>1 4</code>, <code>2 2 1</code>, <code>1 3</code> – $5 \le 2n^2 = 32$ operacija (službeni primjer koristi $4$; bilo koji valjan niz se prihvaća).</p>

<h3>7. Zamke</h3>
<ul>
<li>Provjeri <em>sve</em> nužne uvjete iz odjeljka 1 prije konstrukcije: $g$ šuma, komponente se ne razdvajaju, $g[v] \in \{f[v], \text{početni korijen}\}$, Lema 1, acikličnost ograničenja. Svaki od njih je i sam po sebi dovoljan za <code>NO</code>.</li>
<li>Simuliraj vlastite operacije stvarnom kompresijom puta – u odlukama Faze 2 (dubina $\le 2$) koristi <em>trenutno</em> stanje, ne početno.</li>
<li>Ograničenje $n \ge 3$ nije bitno za algoritam, ali $2n^2$ granica zahtijeva $n^2 + 2n \le 2n^2$, tj. $n \ge 2$.</li>
<li>$T$ do $10^5$ testova: alociraj strukture po $n$, ne po maksimalnom $n$.</li>
</ul>
''',
    'verified': r'''uzorak 1/1 (checker: presuda + simulacija operacija); 300 slučajnih testova ($n \le 6$, $f$ dobiven slučajnim operacijama, $g$ slučajnim daljnjim operacijama ili slučajnom šumom) – presuda uspoređena s BFS-om po svim DSU stanjima, a ispisane operacije simulirane checkerom; 3 velika testa ($\sum n^2 = 5 \cdot 10^6$: $5 \times n{=}1000$, $55 \times n{=}300$, $2000 \times n{=}50$; $\lt 0.1$ s).''',
},
# ---------------------------------------------------------------- C
{
    'letter': 'C', 'title': 'DFS Order 3', 'title_hr': 'DFS poredak 3', 'slug': 'C_dfs_order_3',
    'tl': '2 s', 'ml': '1024 MiB',
    'statement': r'''
<p>Za stablo s $n$ vrhova i svaki vrh $x$ zapisan je jedan valjani DFS poredak $D_x$ dobiven pokretanjem DFS-a iz korijena $x$ (djeca se obilaze u proizvoljnom poretku, koji može biti različit u svakom pokretanju). Rekonstruiraj stablo.</p>
<h3>Ulaz</h3>
<p>$T \le 10^5$ testova; $n$ ($1 \le n \le 1000$) i $n$ redaka $D_{i,1}, \dots, D_{i,n}$ s $D_{i,1} = i$. $\sum n^2 \le 2 \cdot 10^6$.</p>
<h3>Izlaz</h3>
<p>$n - 1$ bridova rekonstruiranog stabla (bilo koje valjano rješenje).</p>
<h3>Primjer</h3>
<p>$n = 4$, poreci $1\,2\,3\,4$, $2\,1\,3\,4$, $3\,2\,4\,1$, $4\,2\,1\,3$: stablo s bridovima $1$–$2$, $2$–$3$, $2$–$4$.</p>
''',
    'hints': [
        r'''<p>Koji vrh sigurno možemo identificirati iz jednog DFS poretka? Razmisli o <em>posljednjem</em> posjećenom vrhu.</p>''',
        r'''<p>Posljednji vrh u DFS poretku je list. Drugi vrh u DFS poretku $D_x$ je uvijek susjed od $x$. Spoji to dvoje i ponavljaj skidanje listova.</p>''',
    ],
    'coach': [
        (r'''Koji vrh sigurno možemo prepoznati iz samog DFS poretka, bez poznavanja stabla?''',
         r'''<p>Posljednji vrh $v$ u bilo kojem DFS poretku je list. Da nije list, imao bi barem dva susjeda; DFS u $v$ ulazi iz jednog od njih, a ostale susjede još nije posjetio (inače bi $v$ bio posjećen iz njih ranije), pa bi ih posjetio <em>nakon</em> $v$ – proturječje s tim da je $v$ posljednji.</p>'''),
        (r'''Kad znamo da je $v$ list, kako iz danih podataka pročitati njegova jedinog susjeda?''',
         r'''<p>Pogledaj poredak $D_v$ koji počinje u $v$: drugi vrh u DFS poretku uvijek je susjed korijena, jer DFS iz korijena najprije prelazi jedan brid. Kako je $v$ list, taj drugi vrh je <em>jedini</em> susjed, dakle brid stabla. To je prvi brid koji ispisujemo.</p>'''),
        (r'''Zašto smijemo list jednostavno ukloniti i nastaviti istim postupkom?''',
         r'''<p>Ako iz stabla uklonimo list $v$, a iz svakog $D_u$ ($u \ne v$) izbrišemo $v$, dobiveni nizovi su valjani DFS poredci manjeg stabla: DFS iz $u$ posjećuje $v$ odmah nakon njegova susjeda i iz njega se odmah vraća, pa brisanje $v$ ne mijenja redoslijed ostalih vrhova. Stablo s $n-1$ vrhova ima isti oblik ulaza, pa postupak ponavljamo $n-1$ puta i dobivamo sve bridove.</p>'''),
        (r'''Kako to izvesti u $O(n^2)$, a ne $O(n^3)$, kad brišemo vrhove iz $n$ nizova?''',
         r'''<p>Brisanja ne izvodimo fizički. Održavamo oznaku „uklonjen” po vrhu i dva tipa pokazivača: pokazivač na kraj $D_1$ (list preostalog stabla je posljednji <em>neuklonjeni</em> vrh u $D_1$, jer je $D_1$ bez uklonjenih vrhova DFS poredak preostalog stabla) i za svaki $v$ pokazivač na prvi neuklonjeni vrh u $D_v$ iza početka. Svaki pokazivač se samo pomiče naprijed, ukupno najviše $n$ koraka po nizu, pa je sve $O(n^2)$ – jednako čitanju ulaza.</p>'''),
    ],
    'tips': [
        r'''U zadacima o DFS poredcima dvije su činjenice gotovo uvijek korisne: <em>posljednji vrh je list</em> i <em>drugi vrh je susjed korijena</em>. Kad su dane sve DFS-permutacije, iz njih možeš „skidati listove” jedan po jedan.''',
        r'''Rekonstrukcija stabla „skidanjem listova” često se implementira bez ikakvog fizičkog brisanja: dovoljni su boolean niz <code>uklonjen[]</code> i pokazivači koji se pomiču samo u jednom smjeru (amortizirano linearno po nizu).''',
        r'''Kad rješenje nije jedinstveno u ispisu (bridovi u bilo kojem redoslijedu, bilo koji redoslijed krajeva), za stress-test napiši <code>check.py</code> koji provjerava svojstvo (ovdje: svaki $D_i$ je valjan DFS poredak ispisanog stabla) umjesto usporedbe s referentnim ispisom.''',
    ],
    'solution': r'''
<p><b>Lema I.</b> Posljednji vrh DFS poretka nužno je list.</p>
<p><b>Lema II.</b> Drugi vrh DFS poretka nužno je izravno susjedan prvom vrhu.</p>
<p>Stoga jednostavno neprestano uklanjamo listove: iz bilo kojeg poretka pročitamo posljednji vrh $v$ (list), iz poretka $D_v$ pročitamo drugi element — to je jedini susjed lista $v$ — zabilježimo brid, uklonimo $v$ iz svih poredaka i ponavljamo dok ne ostane jedan vrh. Složenost je $O(n^2)$ po testu.</p>
<p><em>Zanimljivost:</em> DFS Order bio je zadatak na EC-Finalu 2021, a DFS Order 2 na regionalnom natjecanju u Jinanu 2022.</p>
''',
    'detailed': r'''
<h3>1. Dvije leme o DFS poretku</h3>
<p><strong>Lema 1.</strong> Posljednji vrh $v$ DFS poretka stabla je list.<br>
<em>Dokaz.</em> Pretpostavimo da $v$ ima barem dva susjeda. DFS u $v$ ulazi iz nekog susjeda $p$ (ili je $v$ korijen – ali korijen s barem jednim susjedom nije posljednji ako je $n \ge 2$). Svaki drugi susjed $w \ne p$ u trenutku ulaska u $v$ još nije posjećen: kad bi bio posjećen prije, DFS bi iz $w$ pokušao ući u $v$ prije nego što se vratio, pa bi $v$ bio posjećen iz $w$, ne iz $p$ (u stablu je put između $v$ i $w$ jedinstven – sam brid). Zato DFS posjećuje $w$ nakon $v$, a to proturječi tome da je $v$ posljednji. $\square$</p>
<p><strong>Lema 2.</strong> Drugi vrh DFS poretka susjed je prvoga (korijena).<br>
<em>Dokaz.</em> DFS iz korijena $r$ u prvom koraku prelazi jedan brid iz $r$; vrh u koji stiže je drugi u poretku i susjed je $r$. $\square$</p>
<p>Spojimo leme: neka je $v$ posljednji vrh poretka $D_1$. Po Lemi 1 to je list. U poretku $D_v$ (koji počinje u $v$) drugi je vrh po Lemi 2 susjed od $v$, a kako $v$ ima samo jednog susjeda, to je upravo brid $\{v, D_v[2]\}$ stabla.</p>

<h3>2. Uklanjanje lista čuva valjanost svih poredaka</h3>
<p>Neka je $v$ list stabla $T$ sa susjedom $u$, i neka je $T' = T - v$. Za bilo koji korijen $r \ne v$ promotrimo DFS iz $r$ u $T$. U trenutku kad DFS prvi put dođe u $u$, prije ili poslije ostalih susjeda od $u$ posjetit će i $v$; iz $v$ nema kamo (list), pa se odmah vraća u $u$ i nastavlja <em>točno onako</em> kako bi nastavio u $T'$. Dakle poredak za $T'$ dobivamo brisanjem $v$ iz $D_r$ – ništa se drugo ne mijenja. Isto vrijedi za sve $r \ne v$ odjednom, pa nizovi $D_r \setminus \{v\}$ čine valjan ulaz za stablo $T'$ s $n-1$ vrhova, i na njega ponovno primjenjujemo Lemu 1 i Lemu 2.</p>
<p>Ovaj korak je ključan: on opravdava da postupak „nađi list, ispiši njegov brid, ukloni ga” možemo ponavljati $n-1$ puta i da će u svakom koraku posljednji <em>preostali</em> vrh u $D_1$ biti list <em>preostalog</em> stabla. Kad ostane samo korijen $1$, svih $n-1$ bridova je ispisano.</p>

<h3>3. Algoritam</h3>
<ol>
<li>Pročitaj $n$ i matricu $D$ ($D[i][\cdot]$ je DFS poredak s korijenom $i$).</li>
<li>Postavi <code>uklonjen[v] = false</code> za sve $v$, <code>kraj = n</code> (pokazivač na kraj $D_1$) i <code>pok[v] = 2</code> (pokazivač u $D_v$ na prvi kandidat za susjeda; $D_v[1] = v$).</li>
<li>Ponavljaj $n-1$ puta:
  <ul>
  <li>dok je $D_1[\mathrm{kraj}]$ uklonjen, smanjuj <code>kraj</code>; $v = D_1[\mathrm{kraj}]$ je list preostalog stabla;</li>
  <li>dok je $D_v[\mathrm{pok}[v]]$ uklonjen, povećavaj <code>pok[v]</code>; $u = D_v[\mathrm{pok}[v]]$ je susjed lista;</li>
  <li>ispiši brid $(v, u)$ i označi <code>uklonjen[v] = true</code>.</li>
  </ul></li>
</ol>
<p>Uočimo da se nikad ne dogodi $v = 1$: vrh $1$ je prvi u $D_1$, a mi uzimamo posljednji neuklonjeni, a ona su barem dva sve dok nismo ispisali $n-1$ bridova.</p>

<h3>4. Primjer</h3>
<p>Uzorak: $n = 4$, $D_1 = (1,2,3,4)$, $D_2 = (2,1,3,4)$, $D_3 = (3,2,4,1)$, $D_4 = (4,2,1,3)$. Korak 1: posljednji u $D_1$ je $4$; $D_4[2] = 2$, brid $(4,2)$, uklonimo $4$. Korak 2: posljednji neuklonjeni u $D_1$ je $3$; $D_3[2] = 2$, brid $(3,2)$, uklonimo $3$. Korak 3: preostaje $2$; $D_2[2] = 1$, brid $(2,1)$. Dobili smo stablo $1 - 2$, $2 - 3$, $2 - 4$. Da je ulaz bio npr. $D_2 = (2,4,1,3)$, u trećem bi koraku $D_2[2] = 4$ bio uklonjen i pokazivač bi preskočio na $D_2[3] = 1$.</p>

<h3>5. Složenost</h3>
<p>Čitanje ulaza je $O(n^2)$. Pokazivač <code>kraj</code> pomiče se ukupno najviše $n$ puta; svaki <code>pok[v]</code> pomiče se najviše $n$ puta, ali samo za vrhove koji postanu list, i ukupno preko svih $v$ najviše $n^2$. Dakle $O(n^2)$ vremena i $O(n^2)$ memorije po testu, što uz $\sum n^2 \le 2 \cdot 10^6$ prolazi trivijalno.</p>

<h3>6. Zamke u implementaciji</h3>
<ul>
<li>Odgovor nije jedinstven u ispisu (redoslijed bridova i krajeva je proizvoljan) – za lokalno testiranje treba checker, ne usporedba s uzorkom.</li>
<li>Ulaz je velik ($n^2$ brojeva po testu, do $2 \cdot 10^6$ ukupno); koristi brzo čitanje, a matricu alociraj po testu (ili globalno s ponovnom upotrebom) da izbjegneš $O(n^2)$ inicijalizacija koje ne trebaš.</li>
<li>Ne pretpostavljaj da je $D_v[2]$ pravi susjed: vrh $v$ koji je <em>postao</em> list tijekom postupka izvorno je imao više susjeda, a u $D_v$ iza $v$ najprije stoje cijela podstabla djece koja su možda već uklonjena. Zato pokazivač <code>pok[v]</code> preskače uklonjene vrhove; prvi neuklonjeni je prvi vrh podstabla jedinog preostalog susjeda $u$ – dakle sam $u$ (sva ostala podstabla su u cijelosti uklonjena, inače bi $v$ imao stupanj $\ge 2$).</li>
</ul>
''',
    'verified': r'''uzorak 1/1; 300 slučajnih testova ($n \le 8$, slučajna stabla s dugim lancima i slučajnim DFS poredcima) uz <code>check.py</code> koji provjerava da je ispis stablo i da je svaki $D_i$ valjan DFS poredak toga stabla; 3 velika testa ($n = 1000$, $\lt 0.2$ s).''',
},
# ---------------------------------------------------------------- D
{
    'letter': 'D', 'title': "Flower's Land 2", 'title_hr': 'Cvjetna zemlja 2', 'slug': 'D_flowers_land_2',
    'tl': '6 s', 'ml': '1024 MiB',
    'statement': r'''
<p>Igra na nizu znamenki iz $\{0, 1, 2\}$: dok postoji $i$ sa $s_i = s_{i+1}$, igrač bira takav $i$ i briše $s_i$ i $s_{i+1}$. Igrač pobjeđuje ako se niz može potpuno izbrisati.</p>
<p>Dan je niz $s$ duljine $n$ i $q$ upita dviju vrsta: <code>1 l r</code> — za sve $l \le i \le r$ postavi $s_i \leftarrow (s_i + 1) \bmod 3$; <code>2 l r</code> — može li igrač pobijediti igrajući na $t = s[l..r]$?</p>
<h3>Ulaz</h3>
<p>$n, q$ ($1 \le n, q \le 5 \cdot 10^5$), niz $s$ i $q$ upita s $1 \le l \le r \le n$.</p>
<h3>Izlaz</h3>
<p>Za svaki upit vrste 2: <code>Yes</code> ili <code>No</code>.</p>
<h3>Primjer</h3>
<p>$s = 01211012$: $s[4..5] = 11$ → <code>Yes</code>; $s[3..6] = 2110$ → <code>No</code>. Nakon dvije operacije <code>1 6 8</code> niz je $01211201$; $s[3..6] = 2112$ → <code>Yes</code> ($2112 \to 22 \to \varepsilon$).</p>
''',
    'hints': [
        r'''<p>Brisanje susjednog para jednakih znakova podsjeća na poništavanje $g \cdot g^{-1}$ u grupi. Kako niz pretvoriti u umnožak elemenata tako da se susjedni <em>jednaki</em> znakovi ponište, a različiti ne?</p>''',
        r'''<p>Znakovi na parnim pozicijama postaju $M_{s_i}$, na neparnim $M_{s_i}^{-1}$, za tri slučajne invertibilne matrice. Susjedni jednaki znakovi tada daju $M M^{-1} = I$. Umnožak nad intervalom održavaj segmentnim stablom; za operaciju $+1 \bmod 3$ u svakom čvoru čuvaj umnoške za sva tri pomaka.</p>''',
    ],
    'coach': [
        (r'''Ovisi li ishod igre o tome koje parove igrač briše, ili je „pobjeda” svojstvo samog niza?''',
         r'''<p>Ne ovisi o izboru. Brisanje susjednog para jednakih znakova je sustav prepisivanja $xx \to \varepsilon$, i on je <em>konfluentan</em>: dva različita brisanja koja se preklapaju ($xxx \to x$ na dva načina) daju isti rezultat, a disjunktna brisanja komutiraju. Zato svaki redoslijed vodi do iste <em>normalne forme</em> – niza bez susjednih jednakih znakova. Igrač pobjeđuje ako i samo ako je normalna forma prazna. Drugim riječima, pitanje je: je li produkt $s_l s_{l+1} \cdots s_r$ jednak jedinici u grupi u kojoj je svaki znak involucija ($x^2 = 1$) i nema drugih relacija – slobodnom produktu $\mathbb{Z}_2 * \mathbb{Z}_2 * \mathbb{Z}_2$?</p>'''),
        (r'''Kako grupu s relacijom $x^2 = 1$ pretvoriti u nešto što segmentno stablo može množiti?''',
         r'''<p>Homomorfizmom u matrice: znaku $c$ pridružimo slučajnu $2 \times 2$ matricu $A_c$ nad $\mathbb{Z}_p$ s $A_c^2 = I$ (npr. $\begin{pmatrix} a &amp; b \\ c' &amp; -a \end{pmatrix}$ s $a^2 + bc' = 1$). Tada je produkt izbrisivog niza sigurno $I$ (svako brisanje uklanja $A_c A_c = I$). Obrat – da neizbrisiv niz ne da $I$ – vrijedi samo s velikom vjerojatnošću, kao kod svakog hashiranja; nekomutativnost matrica je ključna, jer bi u komutativnoj grupi npr. $0110$ i $0101$ imali isti produkt. Alternativa iz službenog rješenja: matrice $M_c$ na parnim i $M_c^{-1}$ na neparnim pozicijama – susjedni jednaki znakovi tada daju $M M^{-1} = I$ bez uvjeta $M^2 = I$.</p>'''),
        (r'''Što operacija „$+1 mod 3$ na intervalu” radi s produktom i kako je učiniti lijenom?''',
         r'''<p>Ciklički permutira znakove $0 \to 1 \to 2 \to 0$, pa i matrice $A_0 \to A_1 \to A_2 \to A_0$. Produkt nakon pomaka nije izvediv iz produkta prije pomaka, ali pomaka ima samo tri: u svakom čvoru čuvamo tri produkta $P_0, P_1, P_2$ ($P_k$ = produkt segmenta ako svakom znaku dodamo $k$). Pomak za $d$ na cijelom čvoru je samo rotacija: novi $P_k$ = stari $P_{k+d}$. Lijena oznaka čvora je pomak $\in \{0,1,2\}$, a spajanje djece je $P_k = P_k^{L} P_k^{R}$ za svaki $k$.</p>'''),
        (r'''Zašto je vjerojatnost lažnog <code>Yes</code> zanemariva i koliko košta jedno množenje?''',
         r'''<p>Za fiksni neizbrisivi niz produkt je fiksni polinom u slučajnim ulazima matrica koji nije identički jednak $I$ (kad bi bio, niz bi bio trivijalan u <em>svakoj</em> reprezentaciji, a slobodni produkt $\mathbb{Z}_2 * \mathbb{Z}_2 * \mathbb{Z}_2$ ima vjerne reprezentacije $2\times 2$ matricama). Po Schwartz–Zippelu vjerojatnost da slučajna točka poništi netrivijalan polinom stupnja $\le r-l+1$ je najviše $(r-l+1)/p$; uz $p = 2^{61}-1$ i $5 \cdot 10^5$ upita to je ispod $10^{-6}$. Množenje $2\times 2$ matrica je $8$ množenja modulo $2^{61}-1$ (brzo množenje preko <code>__int128</code>), tri produkta po čvoru; ukupno $O((n+q)\log n)$ s malom konstantom.</p>'''),
    ],
    'tips': [
        r'''„Brisanje susjednih jednakih/inverznih parova” je redukcija riječi u grupi; pitanje „može li se sve izbrisati” je „je li produkt jedinica”. Za slobodne grupe i slobodne produkte hashiraj slučajnim <em>nekomutativnim</em> matricama – komutativni hash (zbroj, XOR) ne razlikuje $abab$ od $aabb$.''',
        r'''Ako operacija na intervalu permutira alfabet iz malog skupa permutacija (ovdje $3$ ciklička pomaka), u čvoru segmentnog stabla čuvaj agregat za <em>svaku</em> permutaciju; lijeno ažuriranje postaje puko preslagivanje polja.''',
        r'''Za hash modulo $2^{61}-1$ množenje se radi u <code>__int128</code> i redukcija s dva pomaka – brže je i sigurnije od dvostrukog moda s dva 32-bitna prosta broja.''',
        r'''Randomizirani algoritam sjemeni satom, a za stress-test brute force redukcijom stogom – konfluentnost jamči da je stog jedini potreban „igrač”.''',
    ],
    'solution': r'''
<p>Konstruiramo tri slučajne invertibilne matrice $M_0, M_1, M_2$.</p>
<p>Za svaki $i$: ako je $i \bmod 2 = 0$, stavimo $A_i = M_{s_i}$, inače $A_i = M_{s_i}^{-1}$.</p>
<p>Ako se interval može potpuno izbrisati, tada je $\prod_{i=l}^{r} A_i = I$ (svako brisanje para jednakih susjednih znakova uklanja umnožak matrice i njezina inverza). Obratno vrijedi s velikom vjerojatnošću.</p>
<p>Segmentnim stablom održavamo operaciju „dodaj $1$ modulo $3$ na intervalu” i umnožak matrica na intervalu (u čvoru čuvamo umnožak za svaki od tri moguća pomaka). Vremenska složenost je $O(n \log n \cdot k^3)$, gdje je $k$ dimenzija matrica.</p>
<p>Službeno rješenje ostavlja pitanje: bi li umjesto matrica poslužile afine funkcije $ax + b$ i $a^{-1}x - ba^{-1}$? (Primjer $02021210202121$ naveden je kao ilustracija za promišljanje.)</p>
<p><em>Zanimljivost:</em> Flower's Land bio je zadatak na Petrozavodsk Summer 2022: Qingyu, flower and their friends' Contest.</p>
''',
    'detailed': r'''
<h3>1. Igra ne ovisi o izboru poteza</h3>
<p>Potez briše dva susjedna jednaka znaka. Tvrdimo: bez obzira na redoslijed poteza, konačni niz (u kojem više nema susjednih jednakih znakova) uvijek je isti. To je <em>konfluentnost</em> sustava prepisivanja $xx \to \varepsilon$; dovoljno je provjeriti lokalnu konfluentnost (Newmanova lema, sustav očito završava jer se duljina smanjuje):</p>
<ul>
<li>dva disjunktna brisanja komutiraju – rezultat je isti u oba redoslijeda;</li>
<li>dva preklapajuća brisanja mogu se preklapati samo u jednom znaku, tj. na bloku $xxx$; brisanje prvog ili drugog para daje isti niz $x$.</li>
</ul>
<p>Dakle igrač pobjeđuje ako i samo ako je normalna forma niza $s[l..r]$ prazna. Normalnu formu računa stog: prolazimo znakove; ako je znak jednak vrhu stoga, skinemo vrh, inače ga stavimo na stog. Ovo je ujedno brute force za male testove.</p>

<h3>2. Algebarska formulacija</h3>
<p>Promatrajmo grupu $G = \langle x_0, x_1, x_2 \mid x_0^2 = x_1^2 = x_2^2 = 1 \rangle$ (slobodni produkt triju kopija $\mathbb{Z}_2$). Riječ $s_l s_{l+1} \cdots s_r$ predstavlja element $x_{s_l} x_{s_{l+1}} \cdots x_{s_r}$; brisanje $xx$ ne mijenja element. Standardna je činjenica da su reducirane riječi (bez susjednih jednakih slova) <em>normalne forme</em> elemenata slobodnog produkta – dvije različite reducirane riječi su različiti elementi. Zato: $s[l..r]$ je izbrisiv $\iff$ produkt je jedinica grupe $G$.</p>
<p>Provjeravati jednakost u $G$ egzaktno na intervalima je nezgodno, pa grupu <em>hashiramo</em>: odaberemo homomorfizam $\varphi : G \to GL_2(\mathbb{Z}_p)$, $p = 2^{61}-1$. Da bi $\varphi$ bio homomorfizam, dovoljno je $\varphi(x_c) = A_c$ s $A_c^2 = I$. Matrica $A = \begin{pmatrix} a &amp; b \\ c' &amp; -a \end{pmatrix}$ ima $A^2 = (a^2 + bc') I$, pa uzmemo slučajne $a, b \ne 0$ i $c' = (1 - a^2) b^{-1}$. Tada:</p>
<ul>
<li>ako je $s[l..r]$ izbrisiv, $\prod A_{s_i} = I$ <em>sigurno</em> (svako brisanje briše $A_c A_c = I$);</li>
<li>ako nije, produkt je $\varphi(w)$ za $w \ne 1$; može biti $I$ samo „nesretnim slučajem”.</li>
</ul>
<p><strong>Zašto je nesretan slučaj rijedak.</strong> Za fiksnu reduciranu riječ $w \ne 1$ duljine $L$ svaki element matrice $\varphi(w) - I$ je polinom stupnja $\le L$ u slučajnim parametrima $(a_c, b_c, c'_c)$. Taj polinom nije identički nula: slobodni produkt $\mathbb{Z}_2 * \mathbb{Z}_2 * \mathbb{Z}_2$ ima vjernu reprezentaciju $2 \times 2$ matricama (npr. nad $\mathbb{R}$ tri refleksije s „generičkim” kutovima generiraju slobodni produkt), pa postoji izbor parametara u kojem je $\varphi(w) \ne I$; polinom koji nije identički nula nad $\mathbb{Z}$ ostaje takav i modulo velikog prostog broja za sve osim konačno mnogo $p$, a Schwartz–Zippel daje vjerojatnost nule $\le L/p \le 5 \cdot 10^5 / 2^{61} \approx 2 \cdot 10^{-13}$ po upitu. Ukupno kroz $5 \cdot 10^5$ upita: $\lesssim 10^{-7}$. Zato je nekomutativnost bitna: u komutativnoj grupi bi $x_0 x_1 x_0 x_1$ i $x_0 x_0 x_1 x_1$ imali isti „hash”, a prvi nije izbrisiv.</p>
<p><em>Službena varijanta.</em> Umjesto uvjeta $A^2 = I$ službeno rješenje uzima tri slučajne invertibilne matrice $M_c$ i stavlja $A_i = M_{s_i}$ na parnim, $A_i = M_{s_i}^{-1}$ na neparnim pozicijama: susjedni jednaki znakovi su uvijek različitog pariteta, pa se poništavaju kao $M M^{-1}$ ili $M^{-1} M$. Obje varijante rade; naša ima jednostavnije ažuriranje jer ne ovisi o paritetu pozicije.</p>

<h3>3. Operacija $+1 \bmod 3$ na intervalu</h3>
<p>Ta operacija zamjenjuje znak $c$ znakom $(c+1) \bmod 3$, dakle matricu $A_c$ matricom $A_{(c+1) \bmod 3}$. Produkt segmenta nakon pomaka nije funkcija produkta prije pomaka, ali skup mogućih pomaka ima samo $3$ elementa. Zato u svakom čvoru segmentnog stabla čuvamo tri matrice
$$P_k[v] = \prod_{i \in \text{segment}(v)} A_{(s_i + k) \bmod 3}, \qquad k = 0, 1, 2,$$
uz lijenu oznaku $\mathrm{lz}[v] \in \{0,1,2\}$ (pomak koji još treba proslijediti djeci). Operacije:</p>
<ul>
<li><em>izgradnja</em>: list ima $P_k = A_{(s_i + k) \bmod 3}$; unutarnji čvor $P_k[v] = P_k[2v] \cdot P_k[2v+1]$ (redoslijed množenja slijeva nadesno!);</li>
<li><em>primjena pomaka $d$ na čvor</em>: $P_k \leftarrow P_{(k+d) \bmod 3}$ za sve $k$ (rotacija triju matrica) i $\mathrm{lz} \leftarrow (\mathrm{lz} + d) \bmod 3$;</li>
<li><em>ažuriranje intervala</em>: standardno lijeno – potpuno pokriven čvor dobiva pomak $1$, inače proslijedi oznaku djeci, spusti se, ponovno izračunaj $P_k$;</li>
<li><em>upit</em>: produkt $P_0$ pokrivenih čvorova slijeva nadesno; odgovor <code>Yes</code> ako je jednak $I$.</li>
</ul>
<p>Ispravnost rotacije: ako segment dobije pomak $d$, novi znakovi su $(s_i + d) \bmod 3$, pa je novi $P_k$ produkt $A_{(s_i + d + k) \bmod 3}$ – to je upravo stari $P_{(k+d) \bmod 3}$.</p>

<h3>4. Složenost</h3>
<p>Segmentno stablo ima $O(\log n)$ dubine; svaka operacija dotiče $O(\log n)$ čvorova, a u čvoru radimo najviše tri množenja $2 \times 2$ matrica ($3 \cdot 8 = 24$ modularnih množenja). Ukupno $O((n + q) \log n)$ vremena; memorija $3 \cdot 4 \cdot 8$ bajta po čvoru, $\approx 100$ MB za $2^{20}$ čvorova – daleko unutar $1024$ MiB. Uz $6$ s vremensko ograničenje je vrlo komotno (lokalno $\lt 1$ s za $n = q = 5 \cdot 10^5$).</p>

<h3>5. Primjer</h3>
<p>$s = 01211012$, upit $(4, 5)$: $s[4..5] = 11$, produkt $A_1 A_1 = I$ → <code>Yes</code>. Upit $(3, 6)$: $s[3..6] = 2110$; normalna forma je $20$ (nije prazna), produkt $A_2 A_1 A_1 A_0 = A_2 A_0 \ne I$ → <code>No</code>. Nakon dvije operacije <code>1 6 8</code> niz postaje $01211201$: $s[3..6] = 2112 \to 22 \to \varepsilon$, produkt $A_2 (A_1 A_1) A_2 = I$ → <code>Yes</code>.</p>

<h3>6. Zamke</h3>
<ul>
<li>Množenje matrica <em>nije</em> komutativno: pri spajanju djece i pri upitu strogo lijevo pa desno.</li>
<li>Množenje modulo $2^{61}-1$: produkt dvaju 61-bitnih brojeva ne stane u 64 bita – koristi <code>__uint128_t</code> i redukciju $(x \,\&amp;\, M) + (x \gg 61)$.</li>
<li>Sjeme generatora iz sata (ne fiksno) da bi hash bio nepredvidiv; $b$ mora biti $\ne 0$ da postoji $b^{-1}$.</li>
<li>Veličina stabla: $n \le 5 \cdot 10^5$ zahtijeva $2^{20}$ čvorova pri indeksiranju $2v, 2v+1$.</li>
<li>Izlaz od $5 \cdot 10^5$ redaka skupljaj u buffer pa ispiši jednom.</li>
</ul>
''',
    'verified': r'''uzorci 1/1; 300 slučajnih testova ($n, q \le 10$, alfabet veličine $1$–$3$) protiv brute forcea koji eksplicitno ažurira niz i redukciju radi stogom; 3 velika testa ($n = q = 5 \cdot 10^5$, uključujući niz oblika $ww^R$ s mnogo izbrisivih intervala, $\lt 1$ s).''',
},
# ---------------------------------------------------------------- E
{
    'letter': 'E', 'title': 'CCPC String', 'title_hr': 'CCPC niz', 'slug': 'E_ccpc_string',
    'tl': '1 s', 'ml': '1024 MiB',
    'statement': r'''
<p>Niz $s$ je <em>CCPC niz</em> ako postoji $t \ge 1$ takav da je $s = c^{2t} p\, c^{t}$ (npr. <code>ccpc</code>, <code>ccccpcc</code>). Dan je niz $S$ nad znakovima <code>c</code>, <code>p</code> i <code>?</code>. Prebroji parove $(l, r)$ takve da se upitnici u $S[l..r]$ mogu zamijeniti znakovima <code>c</code>/<code>p</code> tako da nastane CCPC niz.</p>
<h3>Ulaz</h3>
<p>$T \le 10^5$ testova, u svakom niz $S$; $\sum |S| \le 10^6$.</p>
<h3>Izlaz</h3>
<p>Broj parova.</p>
<h3>Primjer</h3>
<p><code>?cpc</code> → $1$; <code>???c???</code> → $4$; <code>?c?????cccp????</code> → $14$.</p>
''',
    'hints': [
        r'''<p>Svaki CCPC niz ima točno jedno <code>p</code>. Fiksiraj poziciju $i$ na kojoj će stajati <code>p</code> (znak <code>p</code> ili <code>?</code>) i pitaj se koliko vrijednosti $t$ radi.</p>''',
        r'''<p>Neka je $d_l$ broj uzastopnih znakova različitih od <code>p</code> neposredno lijevo od $i$, a $d_r$ desno. Broj valjanih $t$ je $\min(\lfloor d_l / 2 \rfloor, d_r)$.</p>''',
    ],
    'coach': [
        (r'''Koji je znak u CCPC nizu jedinstven i zašto je to dobra „kotva” za brojanje?''',
         r'''<p>U $c^{2t} p\, c^{t}$ postoji točno jedan znak <code>p</code>, na poziciji $2t+1$ od ukupno $3t+1$. Ako podniz $S[l..r]$ može postati CCPC niz, točno jedna pozicija $i \in [l, r]$ postaje <code>p</code>, a duljina $r - l + 1 = 3t + 1$ je određena s $t$. Dakle par $(l, r)$ jednoznačno određuje par $(i, t)$ – i obratno, $(i, t)$ daje $l = i - 2t$, $r = i + t$. Brojimo parove $(i, t)$ umjesto $(l, r)$.</p>'''),
        (r'''Za fiksnu poziciju $i$, koji su uvjeti na $t$?''',
         r'''<p>Znak $S_i$ mora moći biti <code>p</code>, tj. $S_i \in \{$<code>p</code>, <code>?</code>$\}$. Svih $2t$ znakova lijevo od $i$ i $t$ znakova desno mora moći biti <code>c</code>, tj. ne smiju biti <code>p</code>. Ako je $d_l$ duljina maksimalnog bloka znakova $\ne$ <code>p</code> koji završava na $i-1$, a $d_r$ duljina bloka koji počinje na $i+1$, uvjet je $2t \le d_l$ i $t \le d_r$, uz $t \ge 1$. Broj takvih $t$ je $\min(\lfloor d_l/2 \rfloor, d_r)$.</p>'''),
        (r'''Kako izračunati $d_l$ i $d_r$ za sve pozicije odjednom?''',
         r'''<p>Jednim prolazom slijeva: $L_i = L_{i-1} + 1$ ako $S_{i-1} \ne$ <code>p</code>, inače $0$; simetrično zdesna za $R_i$. Alternativa iz službenog rješenja – binarno pretraživanje po prefiksnom broju znakova <code>p</code> – daje $O(n \log n)$, ali linearni prolaz je i kraći i brži.</p>'''),
        (r'''Što provjeriti prije predaje?''',
         r'''<p>Odgovor može biti reda $n^2$ (npr. sve <code>?</code> daje $\sum_i \min(\lfloor (i-1)/2\rfloor, n-i) \approx n^2/6$), pa treba 64-bitni tip. Brojimo samo $t \ge 1$ – prazan „$c$-dio” nije dopušten. Provjera na <code>???c???</code>: pozicija $4$ je <code>c</code> pa ne pridonosi, a ostale daju $c_3 = \min(1,4) = 1$, $c_5 = \min(2,2) = 2$, $c_6 = \min(2,1) = 1$, dok su $c_1, c_2, c_7$ jednaki $0$; zbroj $4$ se slaže s primjerom.</p>'''),
    ],
    'tips': [
        r'''Kad tražena struktura ima <em>jedinstven</em> istaknuti element (jedno <code>p</code>, jedan maksimum, jedan separator), fiksiraj njegov položaj i broji koliko „širina” radi – brojanje podnizova $(l,r)$ pretvara se u zbroj po jednoj poziciji.''',
        r'''Duljine maksimalnih blokova „znakova koji zadovoljavaju uvjet” lijevo/desno od svake pozicije računaj jednim prolazom u svakom smjeru ($L_i = L_{i-1}+1$ ili $0$); to zamjenjuje binarno pretraživanje po prefiksnim zbrojevima.''',
        r'''Prije predaje procijeni najveći mogući odgovor: broj podnizova je reda $n^2$, pa za $n = 10^6$ 32-bitni tip ne dostaje.''',
    ],
    'solution': r'''
<p>Fiksirajmo poziciju $i$ znaka <code>p</code>. Binarnim pretraživanjem (ili izravnim predračunom) odredimo koliko je uzastopnih znakova koji nisu <code>p</code> lijevo ($d_l$) i desno ($d_r$) od $i$. Doprinos pozicije $i$ je $\min\left(\left\lfloor \frac{d_l}{2} \right\rfloor, d_r\right)$.</p>
<p>Vremenska složenost je $O(n \log n)$. Predračunom $d_l, d_r$ može se postići $O(n)$, no to nije potrebno.</p>
''',
    'detailed': r'''
<h3>1. Struktura CCPC niza</h3>
<p>CCPC niz je $c^{2t}\,p\,c^{t}$ za neki $t \ge 1$: duljina $3t+1$, a jedini znak <code>p</code> stoji na poziciji $2t+1$ (računajući od $1$ unutar niza). Iz toga slijede dvije činjenice koje nose cijelo rješenje:</p>
<ul>
<li>za zadanu duljinu $3t+1$ oblik niza je potpuno određen – nema slobode osim izbora $t$;</li>
<li>podniz $S[l..r]$ se može dopuniti u CCPC niz ako i samo ako je $r-l+1 = 3t+1$ za neki $t \ge 1$, znak $S_{l+2t}$ nije <code>c</code> (može biti <code>p</code>), a svi ostali znakovi u $[l, r]$ nisu <code>p</code> (mogu biti <code>c</code>).</li>
</ul>
<p>Znak <code>?</code> je „džoker” – može postati i <code>c</code> i <code>p</code> – pa je uvjet za pojedinu poziciju uvijek oblika „nije zabranjeni znak”.</p>

<h3>2. Bijekcija $(l, r) \leftrightarrow (i, t)$</h3>
<p>Paru $(l, r)$ koji se može dopuniti pridružimo $t = (r-l)/3$ i $i = l + 2t$ (pozicija <code>p</code>-a). Obratno, iz $(i, t)$ dobivamo $l = i - 2t$, $r = i + t$. Preslikavanje je bijekcija između valjanih parova $(l, r)$ i parova $(i, t)$ koji zadovoljavaju uvjete iz prve točke. Zato je odgovor $\sum_i c_i$, gdje je $c_i$ broj valjanih $t$ za fiksno $i$.</p>

<h3>3. Broj valjanih $t$ za fiksno $i$</h3>
<p>Ako je $S_i =$ <code>c</code>, tada je $c_i = 0$. Inače definiramo:</p>
<ul>
<li>$L_i$ = broj uzastopnih znakova različitih od <code>p</code> neposredno lijevo od $i$ (blok $S_{i-L_i}, \dots, S_{i-1}$, a $S_{i-L_i-1}$ je <code>p</code> ili početak niza);</li>
<li>$R_i$ = isto desno od $i$.</li>
</ul>
<p>Lijevih $2t$ znakova $S_{i-2t..i-1}$ svi su $\ne$ <code>p</code> ako i samo ako $2t \le L_i$ (blok je <em>maksimalan</em>, pa je uvjet i nužan: čim $2t \gt L_i$, zahvaćamo znak <code>p</code>). Slično desno: $t \le R_i$. Uz $t \ge 1$ dobivamo
$$c_i = \max\!\left(0,\ \min\!\left(\left\lfloor \tfrac{L_i}{2} \right\rfloor,\ R_i\right)\right) = \min\!\left(\left\lfloor \tfrac{L_i}{2} \right\rfloor,\ R_i\right),$$
jer su obje veličine nenegativne. Primijetimo da uvjet „$S_i$ nije <code>c</code>” već pokriva i to da $S_i$ nije dio lijevog ni desnog bloka – blokovi su definirani strogo lijevo/desno od $i$.</p>

<h3>4. Linearni izračun blokova</h3>
<p>$L_1 = 0$; za $i \ge 2$: $L_i = L_{i-1} + 1$ ako je $S_{i-1} \ne$ <code>p</code>, inače $L_i = 0$. Simetrično $R_n = 0$ i $R_i = R_{i+1} + 1$ ako $S_{i+1} \ne$ <code>p</code>, inače $0$. Oba niza dobivamo u $O(n)$. Službeno rješenje spominje binarno pretraživanje po prefiksnim brojačima znaka <code>p</code> ($O(n \log n)$) – ekvivalentno, ali sporije i duže za napisati.</p>

<h3>5. Primjer: <code>???c???</code></h3>
<p>Pozicije $1..7$. U nizu nema znaka <code>p</code> (a <code>c</code> na poziciji $4$ smije biti dio bloka), pa je $L = (0,1,2,3,4,5,6)$ i $R = (6,5,4,3,2,1,0)$. Kandidati za <code>p</code> su sve pozicije osim $4$: $c_1 = \min(0,6)=0$, $c_2 = \min(0,5)=0$, $c_3 = \min(1,4)=1$, $c_5 = \min(2,2)=2$, $c_6 = \min(2,1)=1$, $c_7 = \min(3,0)=0$. Zbroj $4$ – kao u primjeru (podnizovi <code>???c</code>, <code>??c?</code>, <code>?c??</code>, <code>???c???</code>).</p>

<h3>6. Složenost i zamke</h3>
<p>$O(|S|)$ vremena i memorije po testu, ukupno $O(\sum |S|) = O(10^6)$. Zamke: (a) odgovor ne stane u 32 bita (niz od $10^6$ upitnika daje oko $1.7 \cdot 10^{11}$); (b) $t = 0$ nije dopušten – formula s $\min$ to automatski isključuje jer $\lfloor L_i/2 \rfloor = 0$ kad je $L_i \le 1$; (c) blokovi se računaju <em>bez</em> same pozicije $i$; (d) čitanje $10^5$ nizova zahtijeva brz ulaz (<code>scanf("%s")</code> u dovoljno velik buffer).</p>
''',
    'verified': r'''uzorak 1/1; 300 slučajnih testova ($|S| \le 12$, težinski slučajni znakovi <code>c</code>/<code>p</code>/<code>?</code>) protiv brute forcea koji za svaki podniz provjerava može li postati CCPC niz; 3 velika testa ($\sum |S| = 10^6$, $\lt 0.1$ s).''',
},
# ---------------------------------------------------------------- F
{
    'letter': 'F', 'title': 'Chase Game 3', 'title_hr': 'Igra potjere 3', 'slug': 'F_chase_game_3',
    'tl': '1 s', 'ml': '1024 MiB',
    'statement': r'''
<p>Na $n$ vrhova zadana su dva lanca (puta): $L_1$ spaja $i$ i $i+1$, a $L_2$ spaja $p_i$ i $p_{i+1}$ za permutaciju $p$. Mala Plava Riba (A) bira početni vrh i miče se samo bridovima $L_1$; Xiao Qing Yu (B) bira početni vrh i miče se samo bridovima $L_2$. Igrači se izmjenjuju (A prvi); svaki u svom potezu može ostati ili prijeći jedan brid. B želi da se nađu na istom vrhu, A to želi spriječiti; obojica igraju optimalno.</p>
<p>Odredi može li B, bez obzira na početne vrhove obojice, u konačno mnogo poteza sigurno „uloviti” A.</p>
<h3>Ulaz</h3>
<p>$T \le 10^5$ testova; $n$ ($2 \le n \le 4 \cdot 10^5$) i permutacija $p$. $\sum n \le 4 \cdot 10^5$.</p>
<h3>Izlaz</h3>
<p><code>Yes</code> ili <code>No</code>.</p>
<h3>Primjer</h3>
<p>$p = (1, 4, 3, 2)$ → <code>No</code>; $p = (2, 3, 1)$ → <code>Yes</code>; $p = (1, 5, 2, 3, 4)$ → <code>No</code>.</p>
''',
    'hints': [
        r'''<p>A ima vrlo jednostavnu strategiju bijega ako postoje dva vrha $i$ i $i+1$ (susjedna u $L_1$) koja su u $L_2$ udaljena više od $2$: skakuće između njih.</p>''',
        r'''<p>Uvjet je nužan i dovoljan: B pobjeđuje ako i samo ako za svaki $i$ vrijedi $\mathrm{dist}_{L_2}(i, i+1) \le 2$. Provjeri preko inverzne permutacije.</p>''',
    ],
    'coach': [
        (r'''Kad igra potjere za progonitelja sigurno propada – koji je najjednostavniji „vječni bijeg”?''',
         r'''<p>Bjegunac A hoda po $L_1$, pa se može beskonačno njihati između dva susjedna vrha $i$ i $i+1$ (ili stajati). Progonitelj B lovi tek kad stane na A-ov vrh, a pomiče se po $L_2$ za najviše $1$. Ako su $i$ i $i+1$ na lancu $L_2$ udaljeni barem $3$, njihova zatvorena $L_2$-susjedstva (vrh i njegovi $L_2$-susjedi) su disjunktna. B tada nikad ne može istodobno „prijetiti” obojici: A u svom potezu stane na onaj od $i, i+1$ koji nije ni B-ov vrh ni njegov $L_2$-susjed, i B ga u sljedećem potezu ne dostiže. Time A bježi zauvijek. Dakle uvjet $\mathrm{dist}_{L_2}(i, i+1) \le 2$ za sve $i$ je <em>nužan</em>.</p>'''),
        (r'''Zašto je taj uvjet i dovoljan – što se točno događa kad B uvijek korakne prema A po $L_2$?''',
         r'''<p>Gledajmo položaje na lancu $L_2$: $\mathrm{pos}[v]$ je indeks vrha $v$ u permutaciji $p$. Svaki A-ov potez (ostati ili prijeći na $L_1$-susjeda) mijenja $\mathrm{pos}$ za najviše $2$ – to je upravo pretpostavka. Neka je $D = \mathrm{pos}[A] - \mathrm{pos}[B]$ i bez smanjenja općenitosti $D \gt 0$ na početku B-ova poteza. B korakne prema A, $D$ padne na $D - 1$; ako je $D - 1 = 0$, ulovio ga je. Inače A mijenja $D$ za najviše $2$: ako novi $D$ padne u $\{-1, 0, 1\}$, B ga u sljedećem potezu odmah ulovi (A stoji na B-u ili na B-ovu $L_2$-susjedu, a stajanje na B-u je hvatanje trenutno). Inače $D \ge 2$ i predznak se nije promijenio – A nije „prošao” pokraj B-a.</p>'''),
        (r'''Kako iz toga slijedi da potjera završava u konačno mnogo poteza, a ne samo da A ne može proći?''',
         r'''<p>Dok nema hvatanja, B-ov položaj $\mathrm{pos}[B]$ u svakom B-ovu potezu strogo raste (uvijek korakne prema A koji je desno). Položaj je ograničen s $n$, pa B napravi najviše $n$ poteza prije nego što je hvatanje neizbježno – tj. prije nego što $D$ uđe u $\{-1, 0, 1\}$. Isto vrijedi za bilo koje početne vrhove: B u prvom potezu samo odredi smjer. Zato B pobjeđuje iz svakog početnog stanja.</p>'''),
        (r'''Kako uvjet provjeriti u linearnom vremenu?''',
         r'''<p>Izgradi inverznu permutaciju $\mathrm{pos}[p_j] = j$ i provjeri $|\mathrm{pos}[i] - \mathrm{pos}[i+1]| \le 2$ za sve $i = 1, \dots, n-1$. To je $O(n)$ po testu, ukupno $O(\sum n)$. Uzorci: $p = (2,3,1)$ daje $\mathrm{pos} = (3,1,2)$, razlike $2$ i $1$ – <code>Yes</code>; $p = (1,4,3,2)$ daje $\mathrm{pos}[1] = 1$, $\mathrm{pos}[2] = 4$ – razlika $3$, <code>No</code>.</p>'''),
    ],
    'tips': [
        r'''U igrama potjere na grafovima uvijek najprije traži <em>jednostavnu strategiju za bjegunca</em> (dva vrha između kojih se može njihati, a progonitelj ne može prijetiti obama) – to daje nužan uvjet, koji je onda često i dovoljan.''',
        r'''Kad se igrači kreću po različitim grafovima nad istim vrhovima, prevedi sve položaje u koordinatu jednog od njih (ovdje indeks u permutaciji $p$) – tada „korak prema protivniku” postaje monotoni argument.''',
        r'''Za dokaz konačnosti potjere nađi <em>monotonu ograničenu veličinu</em> (ovdje: položaj progonitelja na lancu strogo raste dok ne ulovi).''',
        r'''Za male $n$ igru s izmjeničnim potezima uvijek možeš riješiti unatrag (retrogradna analiza nad stanjima $(A, B, \text{na potezu})$) – savršen brute force za stress-test.''',
    ],
    'solution': r'''
<p>Razmotrimo nužan i dovoljan uvjet za pobjedu igrača B.</p>
<p>Pretpostavimo da postoje vrhovi $i$ i $i + 1$ čija je udaljenost na lancu $L_2$ veća od $2$. Tada B sigurno ne može pobijediti, jer to znači da su susjedstva vrhova $i$ i $i+1$ na lancu $L_2$ disjunktna. Neka A počne na $i$ i u svakom potezu ode na onaj od vrhova $i, i+1$ koji nije susjedan (na $L_2$) vrhu na kojem se B trenutno nalazi — B nikad ne pobjeđuje.</p>
<p>S druge strane, ako je za svaki par susjednih vrhova $i, i+1$ njihova udaljenost na lancu $L_2$ najviše $2$, B sigurno pobjeđuje: dovoljno je da se u svakom potezu pomakne za jedan korak u smjeru igrača A.</p>
<p>Time smo dobili nužan i dovoljan uvjet: udaljenost na $L_2$ svih parova $(i, i+1)$ mora biti najviše $2$, što jednostavno provjerimo u $O(n)$.</p>
''',
    'detailed': r'''
<h3>1. Postavka u koordinatama lanca $L_2$</h3>
<p>Vrhovi su $1, \dots, n$. Bjegunac A hoda po $L_1$ ($i \leftrightarrow i+1$), progonitelj B po $L_2$ ($p_j \leftrightarrow p_{j+1}$). Definirajmo $\mathrm{pos}[v]$ = indeks $j$ s $p_j = v$ (inverzna permutacija). Tada je $L_2$ „lanac po $\mathrm{pos}$”: B u jednom potezu mijenja $\mathrm{pos}$ za najviše $1$, a udaljenost dvaju vrhova na $L_2$ je $|\mathrm{pos}[u] - \mathrm{pos}[v]|$. A-ov potez s $i$ na $i \pm 1$ mijenja njegov $\mathrm{pos}$ za $|\mathrm{pos}[i] - \mathrm{pos}[i\pm1]|$ – veličinu koju uvjet zadatka kontrolira.</p>
<p>Pitanje glasi: pobjeđuje li B <em>za sve</em> početne položaje obaju igrača (A bira prvi i igra prvi)? Tvrdimo: odgovor je <code>Yes</code> ako i samo ako
$$\Delta_i := |\mathrm{pos}[i] - \mathrm{pos}[i+1]| \le 2 \quad \text{za sve } i = 1, \dots, n-1.$$</p>

<h3>2. Nužnost: bijeg njihanjem</h3>
<p>Neka za neki $i$ vrijedi $\Delta_i \ge 3$. Zatvorena $L_2$-susjedstva $N[i] = \{v : |\mathrm{pos}[v] - \mathrm{pos}[i]| \le 1\}$ i $N[i+1]$ tada su disjunktna (elementi prvog imaju $\mathrm{pos}$ u $[\mathrm{pos}[i]-1, \mathrm{pos}[i]+1]$, drugog u $[\mathrm{pos}[i+1]-1, \mathrm{pos}[i+1]+1]$, a ta se dva intervala ne sijeku kad je razlika središta $\ge 3$).</p>
<p>A-ova strategija: počni na $i$. U svakom svom potezu pogledaj gdje je B. Ako je $B \in N[i]$ (prijeti vrhu $i$: stoji na njemu ili ga može dosegnuti jednim korakom), prijeđi na $i+1$ (ili ostani ako si već tamo); inače stani na $i$. Budući da $B$ ne može biti u oba susjedstva, A uvijek stoji na vrhu koji B ne može dosegnuti u sljedećem potezu, pa B nikad ne stane na A-ov vrh. Treba još paziti na sam početak: A bira prvi, ali B može stati baš na $i$; tada A u prvom potezu ode na $i+1 \notin N[i] \ni B$, i strategija se nastavlja. Dakle B ne može zajamčiti pobjedu – odgovor <code>No</code>.</p>

<h3>3. Dovoljnost: koračanje prema bjeguncu</h3>
<p>Pretpostavimo $\Delta_i \le 2$ za sve $i$. B-ova strategija: u svakom potezu korakni po $L_2$ prema A, tj. smanji $|\mathrm{pos}[A] - \mathrm{pos}[B]|$ za $1$ (ako je $0$, već ga je ulovio).</p>
<p>Neka je $D = \mathrm{pos}[A] - \mathrm{pos}[B]$ promatran na početku B-ova poteza, i pretpostavimo $D \gt 0$ (slučaj $D \lt 0$ je simetričan; $D = 0$ znači da je A stao na B-a – hvatanje). Provedimo jedan puni krug (potez B-a, potez A-a):</p>
<ol>
<li>B korakne: $D \leftarrow D - 1$. Ako je $D = 0$, kraj – B je pobijedio.</li>
<li>A se pomakne: $D$ se promijeni za najviše $2$ (uvjet $\Delta \le 2$ ili ostaje). Ako je novi $D \in \{-1, 0, 1\}$: za $D = 0$ A je sam stao na B-a (hvatanje), a za $D = \pm 1$ B u sljedećem potezu stane na A-ov vrh. Inače: prije A-ova poteza bilo je $D \ge 1$, pa je novi $D \ge 1 - 2 = -1$; isključivši $\{-1, 0, 1\}$ ostaje $D \ge 2$. Predznak je i dalje pozitivan – A nije „preskočio” B-a, jer bi za preskok trebao promijeniti $D$ za barem $3$.</li>
</ol>
<p><strong>Konačnost.</strong> U svakom krugu u kojem nema hvatanja B-ov $\mathrm{pos}$ strogo raste za $1$ (uvijek korača udesno prema A koji je s desne strane). Kako je $\mathrm{pos}[B] \le n$, takvih krugova ima najviše $n - 1$, nakon čega bi $D \ge 2$ bilo nemoguće ($\mathrm{pos}[A] \le n$). Dakle hvatanje se dogodi u $O(n)$ poteza. Argument ne ovisi o početnim vrhovima (B u prvom potezu samo odabere smjer), pa B pobjeđuje uvijek – odgovor <code>Yes</code>.</p>
<p>Uočimo gdje je uvjet ključan: skok koji mijenja $D$ za $3$ ili više omogućio bi A-u da iz $D = 2$ pređe na drugu stranu B-a bez da stane na B-a ili njegova susjeda, pa bi B-ov položaj prestao biti monoton – a to je upravo situacija koju bjegunac u odjeljku 2 iskorištava njihanjem.</p>

<h3>4. Algoritam</h3>
<ol>
<li>Pročitaj $n$ i $p$; izračunaj $\mathrm{pos}[p_j] = j$.</li>
<li>Prođi $i = 1, \dots, n-1$ i provjeri $|\mathrm{pos}[i] - \mathrm{pos}[i+1]| \le 2$.</li>
<li>Ispiši <code>Yes</code> ako svi zadovoljavaju, inače <code>No</code>.</li>
</ol>
<p>Složenost $O(n)$ po testu, ukupno $O(\sum n) = O(4 \cdot 10^5)$, memorija $O(n)$.</p>

<h3>5. Primjeri</h3>
<p>$p = (2, 3, 1)$: $\mathrm{pos} = (3, 1, 2)$; $\Delta_1 = 2$, $\Delta_2 = 1$ → <code>Yes</code>. $p = (1, 4, 3, 2)$: $\mathrm{pos} = (1, 4, 3, 2)$; $\Delta_1 = 3$ → <code>No</code> (A se njiše između $1$ i $2$, koji su na $L_2$ na krajevima lanca $1 - 4 - 3 - 2$). $p = (1, 5, 2, 3, 4)$: $\mathrm{pos}[1] = 1$, $\mathrm{pos}[2] = 3$, $\mathrm{pos}[3] = 4$, $\mathrm{pos}[4] = 5$, $\mathrm{pos}[5] = 2$; $\Delta_4 = |5 - 2| = 3$ → <code>No</code>.</p>

<h3>6. Zamke</h3>
<ul>
<li>Uvjet se provjerava za susjede na $L_1$ (parove $i, i+1$), a udaljenost mjeri na $L_2$ – lako je pomiješati smjer i provjeriti $|p_j - p_{j+1}|$ umjesto $|\mathrm{pos}[i] - \mathrm{pos}[i+1]|$; to su različiti uvjeti (drugi bi značio da A lovi B-a).</li>
<li>Za $n = 2$ uvijek je <code>Yes</code> (oba lanca su isti brid).</li>
<li>$T$ do $10^5$ testova – niz $\mathrm{pos}$ alociraj po testu veličine $n$, ne $4 \cdot 10^5$ svaki put.</li>
</ul>
''',
    'verified': r'''uzorak 1/1; 300 slučajnih testova ($n \le 7$, permutacije bliske identiteti i potpuno slučajne) protiv brute forcea koji retrogradnom analizom rješava igru za sve parove početnih vrhova; 3 velika testa ($\sum n = 4 \cdot 10^5$, $\lt 0.1$ s).''',
},
# ---------------------------------------------------------------- G
{
    'letter': 'G', 'title': 'Recover the String', 'title_hr': 'Rekonstrukcija niza', 'slug': 'G_recover_the_string',
    'tl': '8 s', 'ml': '1024 MiB',
    'statement': r'''
<p>Za niz $s$ malih slova zapisani su svi njegovi <em>različiti</em> podnizovi kao vrhovi; iz podniza $s_1$ ide usmjereni brid u $s_2$ ako je $s_2 = s_1 + c$ ili $s_2 = c + s_1$ za neko slovo $c$ (dvostruki bridovi uklonjeni). Nastaje DAG. Dan je samo taj DAG (bez oznaka vrhova); rekonstruiraj leksikografski najmanji mogući niz $s$.</p>
<h3>Ulaz</h3>
<p>$T \le 10^5$ testova; $n, m$ ($1 \le n \le 10^6$, $0 \le m \le 2 \cdot 10^6$) i $m$ bridova $u_i \to v_i$. Jamči se da rješenje postoji; $\sum n \le 10^6$, $\sum m \le 2 \cdot 10^6$.</p>
<h3>Izlaz</h3>
<p>Traženi niz.</p>
<h3>Primjer</h3>
<p>Za DAG s $5$ vrhova i bridovima $2 \to 4$, $2 \to 5$, $5 \to 3$, $4 \to 3$, $1 \to 5$, $1 \to 4$ odgovor je <code>aba</code> (vrhovi: <code>a</code>, <code>b</code>, <code>ab</code>, <code>ba</code>, <code>aba</code>). Za treći primjer iz zadatka ($8$ vrhova, $11$ bridova) odgovor je <code>aaba</code>.</p>
''',
    'hints': [
        r'''<p>Vrhovi ulaznog stupnja $0$ su pojedinačna slova (koja ne možemo razlikovati — dodijeli ih proizvoljno), a jedini vrh izlaznog stupnja $0$ je cijeli niz. Duljine svih vrhova slijede iz toga topološkim obilaskom.</p>''',
        r'''<p>Pokušaj dokazati: za svaki vrh $u$ postoji niz $S(u)$ takav da $u$ predstavlja $S(u)$ ili $\mathrm{rev}(S(u))$. Prethodnici od $u$ su $S(u)$ bez posljednjeg znaka i bez prvog znaka; ta dva prethodnika u pravilu imaju točno jednog zajedničkog prethodnika — iz njega se vidi kako se „lijepe”.</p>''',
        r'''<p>Posebni slučajevi: jedan prethodnik → niz od jednog ponovljenog slova; dva prethodnika s istim skupom prethodnika → niz koji alternira dva slova (nedostupno kojim redom). Klasificiraj vrhove u tri tipa i za treći tip održavaj koji je prethodnik lijevi, a koji desni dio.</p>''',
    ],
    'coach': [
        ('Opažanje 1: duljine i izvori', r'''<p>Ne razlikujemo „vrh” i „niz koji vrh predstavlja”. Vrhovi ulaznog stupnja $0$ predstavljaju pojedinačna slova; koje je slovo koji vrh ne može se razlučiti, pa dodijelimo proizvoljno. Duljine svih ostalih vrhova slijede topološkim obilaskom, uključujući duljinu izvornog niza (jedini vrh izlaznog stupnja $0$).</p>'''),
        ('Opažanje 2: svaki vrh je $S(u)$ ili $\mathrm{rev}(S(u))$', r'''<p>Vrh $u$ ima ulazni stupanj najviše $2$: prethodnici su $L(S(u))$ (bez posljednjeg znaka) i $R(S(u))$ (bez prvog znaka). Neka je $G(u)$ skup prethodnika. Općenito je $|G(u)| = 2$ i ta dva prethodnika imaju točno jednog zajedničkog prethodnika (nizu bez oba kraja). Iz $S(v_1)$ i $S(v_2)$ i njihova preklapanja preko zajedničkog prethodnika rekonstruiramo $S(u)$ do na obrat.</p>'''),
        ('Opažanje 3: tri tipa vrhova', r'''<p><b>Tip 1:</b> $|G(u)| = 1$, tj. $L(S(u)) = R(S(u))$ — $S(u)$ se sastoji od jednog slova; prethodnici tipa 1 su također tipa 1. <b>Tip 2:</b> $G(u) = \{v_1, v_2\}$ i $G(v_1) = G(v_2)$ — $S(u)$ alternira dva različita slova; možemo odrediti koja su, ali ne i kojim redom (niz je $S(u)$ ili $\mathrm{flip}(S(u))$). Ako je $|S(u)|$ neparan, $\mathrm{rev}(S(u)) \ne \mathrm{flip}(S(u))$! Pojedinačno slovo smatramo tipom 1, nizove duljine $2$ tipom 2. <b>Tip 3:</b> ostali vrhovi — niz je $S(u)$ ili $\mathrm{rev}(S(u))$.</p>'''),
        ('Algoritam za tip 3', r'''<p>Uz $S(u)$ za svaki $v \in G(u)$ održavamo podatak oblika „[$S(v)$ ili $\mathrm{rev}(S(v))$] predstavlja [$L(u)$ ili $R(u)$]”. Za $G(u) = \{v_1, v_2\}$: <b>slučaj 1</b> — nijedan nije tipa 2: podatak za $u$ računamo iz zajedničkog prethodnika $G(v_1) \cap G(v_2)$. <b>Slučaj 2</b> — točno jedan ($v_1$) je tipa 2, pa je $v_2$ tipa 3 i točno jedan od $L(S(v_2))$, $R(S(v_2))$ alternirajući je niz koji odgovara $S(v_1)$. Ako je $|S(v_2)| \gt 3$, $v_2$ je i sam u slučaju 2, pa održavamo koja je njegova strana alternirajuća i kako alternira. Ako je $|S(v_2)| = 3$, čuvamo cijeli niz i provjerimo grubom silom. Ukupno $O(n)$ informacija.</p>'''),
        ('Završetak i složenost', r'''<p>Na kraju dobivamo dva kandidata za izvorni niz ($S$ i $\mathrm{rev}(S)$, odnosno inačice s $\mathrm{flip}$). Svakom preimenujemo slova po redu prvog pojavljivanja (<code>a</code>, <code>b</code>, …) i uzmemo leksikografski manji. Ukupno $O(n + m)$.</p>'''),
    ],
    'solution': r'''
<p>Radi jednostavnosti u nastavku ponekad ne razlikujemo „vrh” i „niz koji vrh predstavlja” — npr. „duljina vrha” znači „duljina niza koji vrh predstavlja”.</p>
<p>Najprije, vrhovi ulaznog stupnja $0$ sigurno predstavljaju pojedinačna slova, ali se ne može razlučiti koje slovo predstavlja koji vrh, pa im slova dodijelimo proizvoljno. Zatim iz tih vrhova izvedemo duljinu svakog drugog vrha, uključujući duljinu izvornog niza (izvorni niz je jedini vrh izlaznog stupnja $0$).</p>
<p>Jednostavnom simulacijom može se naslutiti da je niz koji vrh predstavlja „prilično jedinstven”. Formalno: za svaki vrh $u$ postoji niz $S(u)$ takav da je niz koji $u$ stvarno predstavlja jednak $S(u)$ ili $\mathrm{rev}(S(u))$, gdje $\mathrm{rev}(s)$ označava obrnuti niz. Dokažimo tu tvrdnju induktivno.</p>
<p>Ulazni stupanj svakog vrha je najviše $2$: prethodnici su nizovi $S(u)$ bez posljednjeg odnosno bez prvog znaka. Neka $L(s)$ označava $s$ bez posljednjeg znaka, $R(s)$ niz $s$ bez prvog znaka, a $G(u)$ skup prethodnika vrha $u$.</p>
<p>U općem slučaju je $|G(u)| = 2$, a dva prethodnika imaju točno jednog zajedničkog prethodnika.</p>
<p>Analizirajmo najprije posebne slučajeve koji ne zadovoljavaju to svojstvo.</p>
<ul>
<li>Ako je $|G(u)| = 1$, tada je $L(S(u)) = R(S(u))$, tj. $S(u)$ se sastoji od jednog jedinog slova, koje možemo odrediti. Takve vrhove zovemo <b>vrhovima prvog tipa</b>. Prethodnici vrha prvog tipa također su prvog tipa.</li>
<li>Ako je $G(u) = \{v_1, v_2\}$, ali $G(v_1) = G(v_2)$, tada $S(u)$ nužno nastaje alterniranjem dvaju različitih slova. Ta dva slova možemo odrediti, ali ih samo pomoću vrhova iz kojih se može doći do $u$ ne možemo razlikovati. Niz takvog vrha je $S(u)$ ili $\mathrm{flip}(S(u))$, gdje $\mathrm{flip}(s)$ zamjenjuje dva slova u $s$. Pozor: ako je $|S(u)|$ neparan, tada je $\mathrm{rev}(S(u)) \ne \mathrm{flip}(S(u))$. Takve vrhove zovemo <b>vrhovima drugog tipa</b>; njihovi prethodnici također su drugog tipa. Posebno, pojedinačna slova smatramo prvim tipom, a nizove duljine $2$ drugim tipom.</li>
<li>Ostale vrhove zovemo <b>vrhovima trećeg tipa</b>; njihov niz ima oblik $S(u)$ ili $\mathrm{rev}(S(u))$.</li>
</ul>
<p>Za vrhove trećeg tipa, osim $S(u)$, održavamo i koji dio od $S(u)$ predstavlja koji prethodnik. Formalno, za $v \in G(u)$ održavamo informaciju oblika: „[$S(v)$ ili $\mathrm{rev}(S(v))$] predstavlja [$L(u)$ ili $R(u)$]”.</p>
<p>Za vrh $u$ trećeg tipa neka je $G(u) = \{v_1, v_2\}$.</p>
<ul>
<li><b>Slučaj 1:</b> ni $v_1$ ni $v_2$ nisu drugog tipa. Tada informaciju za $u$ izračunamo pomoću zajedničkog prethodnika skupova $G(v_1)$ i $G(v_2)$.</li>
<li><b>Slučaj 2:</b> inače je točno jedan od $v_1, v_2$ drugog tipa; neka je to $v_1$. Tada je $v_2$ trećeg tipa i točno jedan od $L(S(v_2))$, $R(S(v_2))$ je alternirajući niz koji se može uskladiti sa $S(v_1)$. Ako je $|S(v_2)| \gt 3$, točno jedan od $L(v_2)$, $R(v_2)$ je alternirajući, pa je i $v_2$ sam u obliku slučaja 2 — možemo održavati koja je strana od $v_2$ alternirajuća i kako alternira. Ako je $|S(v_2)| = 3$, izravno pamtimo niz koji $v_2$ predstavlja i provjeravamo grubom silom.</li>
</ul>
<p>Tako je dovoljno održavati $O(n)$ informacija. Na kraju dobivamo dva moguća kandidata za izvorni niz; u svakom preimenujemo slova tako da niz bude leksikografski najmanji i uzmemo manji od dvaju. Ukupna složenost je $O(n)$.</p>
''',
},
# ---------------------------------------------------------------- H
{
    'letter': 'H', 'title': 'This is not an Abnormal Team!', 'title_hr': 'Ovo nije abnormalan tim!', 'slug': 'H_this_is_not_an_abnormal_team',
    'tl': '5 s', 'ml': '1024 MiB',
    'statement': r'''
<p>U timu za trening je $n_1$ dječaka i $n_2$ djevojčica te $m$ parova (dječak, djevojčica) koji su u vezi. Treba ih podijeliti u ekipe od najviše $3$ člana; ako ekipa ima više od jednog člana, barem jedan član mora biti u vezi sa svim ostalim članovima. Najprije minimiziraj broj jednočlanih ekipa, a zatim, uz taj minimum, broj tročlanih ekipa.</p>
<h3>Ulaz</h3>
<p>$n_1, n_2, m$ ($1 \le n_1, n_2 \le 10^5$, $1 \le m \le 2 \cdot 10^5$) i $m$ različitih parova $(u_i, v_i)$.</p>
<h3>Izlaz</h3>
<p>Broj jednočlanih i broj tročlanih ekipa.</p>
<h3>Primjer</h3>
<p>$n_1 = 5$, $n_2 = 6$, veze $(1,1),(2,1),(2,2),(3,2),(4,2),(4,3),(5,3),(5,4),(5,5),(5,6)$: odgovor $1\ 2$.</p>
''',
    'hints': [
        r'''<p>Valjane ekipe: pojedinac, brid, ili put od $3$ vrha (srednji je u vezi s obojicom). Graf je bipartitan. Uoči: svaki put ili ciklus s više od jednog vrha može se rastaviti na puteve duljine $2$ i $3$ — pa je minimum izoliranih isto što i „odaberi podgraf sa stupnjevima $\le 2$ koji pokriva najviše vrhova”.</p>''',
        r'''<p>Tok: svaki vrh ima <em>dva</em> jedinična brida prema izvoru/ponoru — jedan s troškom $-M$ (velik), drugi s troškom $+1$. Tok minimalnog troška najprije pokrije što više vrhova, a zatim minimizira broj vrhova stupnja $2$ (= tročlane ekipe). Zašto standardni MCMF ne prolazi i kako pomaže Dinic po razinama troška?</p>''',
    ],
    'coach': [
        (r'''Kako izgleda skup ekipa kao podgraf i koje podgrafe možemo rastaviti na ekipe?''',
         r'''<p>Dvočlana ekipa je brid, tročlana je put $x - y - z$ u kojem je $y$ „centar” u vezi s obojicom (u bipartitnom grafu ekipa od $3$ ne može biti trokut). Unija bridova svih ekipa je podgraf $F$ u kojem svaki vrh ima stupanj $\le 2$. Obratno, svaki takav $F$ (disjunktna unija puteva i ciklusa) rastavlja se na ekipe: put s $v \ge 2$ vrhova rastavimo na parove i, ako je $v$ neparan, jednu trojku; ciklus (paran, jer je graf bipartitan) na same parove. Dakle „minimalno samaca” $=$ „podgraf sa stupnjevima $\le 2$ koji pokriva najviše vrhova”, a među takvima želimo najmanje trojki.</p>'''),
        (r'''Kako iz $F$ pročitati broj trojki i zašto je optimalan $F$ sastavljen samo od puteva s $1$ ili $2$ brida?''',
         r'''<p>Neka $F$ pokriva $C$ vrhova i ima $d_2$ vrhova stupnja $2$; tada je $|F| = (C + d_2)/2$. Put s $3$ ili više bridova može se zamijeniti disjunktnim bridovima koji pokrivaju iste vrhove (ili iste vrhove uz jednu trojku), a ciklus savršenim sparivanjem – oba smanjuju $d_2$ bez smanjenja $C$. Zato u optimalnom $F$ svaka komponenta ima $1$ ili $2$ brida, pa je <em>broj trojki točno $d_2$</em>, a broj samaca $n_1 + n_2 - C$. Treba minimizirati $-M \cdot C + d_2$ za velik $M$ (npr. $M \gt n_1 + n_2$).</p>'''),
        (r'''Koja mreža toka daje trošak $-M$ za prvi i $+1$ za drugi brid u vrhu?''',
         r'''<p>Izvor $S \to$ dječak $b$ s <em>dva</em> paralelna jedinična brida (trošak $-M$ i $+1$), $b \to g$ za svaku vezu (kapacitet $1$, trošak $0$), djevojčica $g \to T$ opet dva brida ($-M$, $+1$). Tok vrijednosti $|F|$ koji u vrhu $v$ prenosi $\deg_F(v)$ jedinica stoji $-M$ za prvu i $+1$ za drugu jedinicu, dakle ukupno $-MC + d_2$. Minimalni trošak toka (bilo koje vrijednosti) je upravo traženi optimum.</p>'''),
        (r'''Zašto klasični MCMF s jednim najkraćim putem po iteraciji ne prolazi, i koje cijene augmentirajući putevi uopće mogu imati?''',
         r'''<p>Put od $S$ do $T$ koristi točno jedan brid iz $S$ i jedan u $T$ (povratni bridovi $b \to S$ i $T \to g$ ne mogu biti na jednostavnom $S$–$T$ putu), a unutrašnji bridovi imaju trošak $0$. Zato je cijena puta $-2M$ (dva nova pokrivena vrha), $-M + 1$ (jedan novi vrh, jedan stari dobiva stupanj $2$) ili $+2$ (neisplativo – tu stajemo). Uzastopni najkraći putevi daju najprije $\nu$ puteva cijene $-2M$ (to je <em>maksimalno sparivanje</em>), zatim $k$ puteva cijene $-M+1$. Odgovor je $(n_1 + n_2 - 2\nu - k,\ k)$. Umjesto $\nu + k \le 10^5$ Bellman–Fordova, za svaku razinu cijene puštamo <em>maksimalni tok</em> na grafu najkraćih puteva (Dinic).</p>'''),
        (r'''Kako točno izgleda „graf najkraćih puteva” za razinu $-M+1$ nakon maksimalnog sparivanja?''',
         r'''<p>Neka je $R$ skup vrhova dosegnutih iz <em>nesparenih dječaka</em> alternirajućim putevima (nespareni brid $b \to g$, spareni $g \to b$). U maksimalnom sparivanju $R$ ne sadrži nesparenu djevojčicu i zatvoren je na alternirajuće korake. Put cijene $-M+1$ je stoga jednog od dva tipa: <strong>(A)</strong> od nesparenog dječaka (brid $-M$) alternirajuće do <em>sparene</em> djevojčice (brid $+1$) – cijeli u $R$; <strong>(B)</strong> od sparenog dječaka izvan $R$ (brid $+1$) alternirajuće do <em>nesparene</em> djevojčice (brid $-M$) – cijeli izvan $R$, jer se iz $R$ ne može izaći. Dva su tipa na disjunktnim skupovima vrhova i ne utječu jedan na drugoga, pa je $k = f_A + f_B$, gdje su $f_A, f_B$ maksimalni tokovi u dvjema mrežama. Ukupno tri Dinica na jediničnim mrežama: $O(m \sqrt{n})$.</p>'''),
    ],
    'tips': [
        r'''„Podijeli u grupe veličine $\le 3$ s centrom” u bipartitnom grafu $=$ podgraf sa stupnjevima $\le 2$; leksikografski cilj (najviše pokrivenih, pa najmanje stupnja $2$) modelira se <em>dva paralelna brida</em> po vrhu s troškovima $-M$ i $+1$.''',
        r'''Kad u MCMF-u sve cijene augmentirajućih puteva pripadaju maloj skupini vrijednosti, ne trebaš SPFA po augmentaciji: za svaku razinu cijene izračunaj graf najkraćih puteva i pusti Dinic – „MCMF po razinama”.''',
        r'''Nakon maksimalnog sparivanja skup $R$ dosegnut alternirajućim putevima iz nesparenih vrhova jedne strane (Hungarian forest) zatvoren je i ne sadrži nesparene vrhove druge strane – to je alat kojim se razdvajaju neovisni potproblemi (isti kao u dokazu Kőnigova teorema).''',
        r'''Brute force za takve zadatke: enumeriraj podskupove bridova ($m \le 10$), odbaci one sa stupnjem $\gt 2$ i izračunaj $(C, d_2)$ – neovisno o toku, savršeno za stress-test.''',
    ],
    'solution': r'''
<p>Najprije razmotrimo minimizaciju broja izoliranih vrhova. Uočimo da se svaki ciklus ili put s više od jednog vrha sigurno može rastaviti na puteve s $2$ ili $3$ vrha.</p>
<p>Stoga je za minimizaciju izoliranih vrhova dovoljno pokrenuti tok u kojem svaki vrh ima protok najviše $2$, uz želju da što više vrhova ima protok različit od $0$ — što vodi na tok minimalnog troška. Svaki vrh spojimo s pripadnim izvorom odnosno ponorom dvama bridovima kapaciteta $1$, od kojih jedan ima trošak $-M$ ($M$ dovoljno velik broj); tako će se sigurno prvo augmentirati preko brida s manjim troškom.</p>
<p>Zatim želimo što manje vrhova stupnja $2$. Budući da je vrh stupnja $2$ ekvivalentan putu s $3$ vrha, drugom bridu dajemo trošak $1$.</p>
<p>Budući da tražimo minimalni trošak, prvo će se proći svi bridovi troška $-M$, a zatim što manje bridova troška $1$.</p>
<p>Izravna primjena uobičajenog algoritma za tok minimalnog troška prekoračuje vremensko ograničenje. Uočimo da duljina augmentirajućeg puta može biti samo $-2M$ ili $-M + 1$, pa nakon izračuna grafa najkraćih puteva koristimo Dinic (ili drugi ispravan algoritam za maksimalni tok) s višestrukim augmentacijama. Vremenska složenost je $O(m\sqrt{n})$.</p>
<p>Za ovaj zadatak postoje i neka tumačenja koja se ne temelje na toku minimalnog troška, no sva su na kraju ekvivalentna nekoliko puta rješavanju problema maksimalnog toka na ovom grafu.</p>
''',
    'detailed': r'''
<h3>1. Ekipe kao podgraf sa stupnjevima $\le 2$</h3>
<p>Graf je bipartitan (veze su samo između dječaka i djevojčica). Dopuštene ekipe: pojedinac; par $\{x, y\}$ s bridom $xy$; trojka $\{x, y, z\}$ u kojoj je jedan član u vezi s ostala dva – zbog bipartitnosti trojka je uvijek put $x - y - z$ (centar $y$ i dva člana suprotne strane), nikad trokut.</p>
<p>Označimo s $F$ skup bridova koje ekipe „koriste” (brid para; dva brida trojke). U $F$ svaki vrh ima stupanj $\le 2$ (pojedinac $0$, član para ili krajnji član trojke $1$, centar trojke $2$). <strong>Obratno</strong>, svaki podgraf $F$ sa stupnjevima $\le 2$ je disjunktna unija puteva i ciklusa i može se rastaviti na ekipe: put s $v \ge 2$ vrhova rastavimo na $\lfloor v/2 \rfloor - [v \text{ neparan}]$ parova i $[v \text{ neparan}]$ trojki, uzimajući uzastopne bridove; ciklus je paran (bipartitnost) i rastavlja se na $v/2$ parova. Zato je zadatak ekvivalentan izboru $F$:</p>
<ul>
<li>broj samaca $= n_1 + n_2 - C$, gdje je $C$ broj vrhova stupnja $\ge 1$ u $F$ – <em>maksimiziraj $C$</em>;</li>
<li>uz maksimalan $C$, <em>minimiziraj broj trojki</em>.</li>
</ul>

<h3>2. Broj trojki i oblik optimalnog $F$</h3>
<p>Neka je $d_2$ broj vrhova stupnja $2$ u $F$, a $d_1$ stupnja $1$; $C = d_1 + d_2$ i $2|F| = d_1 + 2d_2 = C + d_2$. Tvrdimo: uz fiksan skup pokrivenih vrhova, $F$ se može izmijeniti tako da mu svaka komponenta ima $1$ ili $2$ brida, ne povećavajući $d_2$. Put s $v$ vrhova zamijenimo s $\lfloor v/2 \rfloor$ disjunktnih bridova ako je $v$ paran (isti pokriveni vrhovi, $d_2$ pada za $v-2$), odnosno s $(v-3)/2$ bridova i jednim putem od $2$ brida ako je neparan ($d_2$ pada za $v-3$); ciklus zamijenimo savršenim sparivanjem ($d_2$ pada za $v$). Nakon toga svaka komponenta s $2$ brida je točno jedna trojka, svaka s $1$ bridom jedan par, pa je <strong>broj trojki $= d_2$</strong>. Dakle tražimo $F$ koji minimizira $-M \cdot C + d_2$ za dovoljno velik $M$ (npr. $M \gt n_1 + n_2 \ge d_2$), jer tada svaki dodatni pokriveni vrh vrijedi više od bilo kojeg broja trojki.</p>

<h3>3. Model toka minimalnog troška</h3>
<p>Mreža: izvor $S$, ponor $T$; za dječaka $b$ dva paralelna brida $S \to b$ kapaciteta $1$ s troškovima $-M$ i $+1$; za vezu $(b, g)$ brid $b \to g$ kapaciteta $1$ i troška $0$; za djevojčicu $g$ dva brida $g \to T$ ($-M$ i $+1$). Cjelobrojni tok odgovara skupu bridova $F$ (bridovi $b \to g$ s protokom $1$), stupanj vrha je količina toka kroz njega ($\le 2$ zbog kapaciteta), a trošak najjeftinijeg načina da se ta količina provede kroz vrh je $-M$ za prvu i $+1$ za drugu jedinicu. Ukupni trošak toka je $-MC + d_2$ – upravo funkcija cilja. Traženi optimum je <em>tok minimalnog troška bilo koje vrijednosti</em>.</p>

<h3>4. Uzastopni najkraći putevi i njihove cijene</h3>
<p>Algoritam uzastopnih najkraćih puteva (SSP) polazi od nul-toka i augmentira po najjeftinijem $S$–$T$ putu u rezidualnoj mreži dok je njegova cijena negativna; poznato je da je nakon svake augmentacije dobiveni tok minimalnog troška za svoju vrijednost, a cijene puteva su nepadajuće. Kakve su ovdje cijene? Jednostavan $S$–$T$ put koristi točno jedan brid iz $S$ (povratni brid $b \to S$ vratio bi se u $S$) i jedan brid u $T$; unutrašnji bridovi $b \to g$ i njihovi povratni $g \to b$ imaju trošak $0$. Zato je cijena puta jedna od:</p>
<ul>
<li>$-2M$: oba krajnja brida su „$-M$” – pokrivamo novog dječaka i novu djevojčicu;</li>
<li>$-M+1$: jedan „$-M$” i jedan „$+1$” – jedan novi pokriveni vrh, jedan stari dobiva stupanj $2$;</li>
<li>$+2$: dva „$+1$” – pogoršava cilj, tu SSP staje.</li>
</ul>
<p>Putevi cijene $-2M$ su točno augmentirajući putevi sparivanja (nespareni brid naprijed, spareni natrag), pa ih je najviše $\nu$ – veličina maksimalnog sparivanja; nakon njih je tok maksimalno sparivanje. Neka zatim SSP nađe $k$ puteva cijene $-M+1$. Konačno $C = 2\nu + k$, $|F| = \nu + k$, pa $d_2 = 2|F| - C = k$. <strong>Odgovor je $(n_1 + n_2 - 2\nu - k,\ k)$.</strong></p>
<p>Izravni SSP s Bellman–Fordom/SPFA po augmentaciji radi $O((\nu + k) \cdot nm)$ u najgorem slučaju – prespor. No sve augmentacije iste razine cijene možemo izvesti odjednom kao maksimalni tok na podgrafu najkraćih puteva: razina $-2M$ je obično bipartitno sparivanje (Hopcroft–Karp ili Dinic na jediničnoj mreži), a razinu $-M+1$ analiziramo detaljnije.</p>

<h3>5. Razina $-M+1$: dva neovisna maksimalna toka</h3>
<p>Fiksirajmo maksimalno sparivanje $\mathcal{M}$ iz prve faze. Neka je $R$ skup vrhova dosegnutih iz svih <em>nesparenih dječaka</em> alternirajućim putevima: iz dječaka idemo nesparenim bridom do djevojčice, iz djevojčice sparenim bridom do njezina partnera. Dvije standardne činjenice:</p>
<ol>
<li>$R$ ne sadrži nesparenu djevojčicu – inače bi postojao augmentirajući put i $\mathcal{M}$ ne bi bilo maksimalno.</li>
<li>$R$ je zatvoren: iz dječaka u $R$ svi nespareni bridovi vode u $R$ (definicija), iz djevojčice u $R$ jedini spareni brid vodi u $R$; obratno, spareni partner dječaka iz $R$ je u $R$ (dječak je u $R$ ušao upravo preko svoje partnerice, osim nesparenih dječaka koji partnera nemaju).</li>
</ol>
<p>U rezidualnoj mreži nakon prve faze put cijene $-M+1$ počinje ili bridom $-M$ iz nesparenog dječaka i završava bridom $+1$ u sparenoj djevojčici (<strong>tip A</strong>), ili bridom $+1$ iz sparenog dječaka i završava bridom $-M$ u nesparenoj djevojčici (<strong>tip B</strong>). Unutrašnjost puta je alternirajući put (nespareni bridovi $b \to g$ imaju rezidualni kapacitet naprijed, spareni $g \to b$ natrag). Put tipa A počinje u $R$ i po zatvorenosti ostaje u $R$. Put tipa B završava u nesparenoj djevojčici, koja nije u $R$; kad bi ikad ušao u $R$, po zatvorenosti bi u $R$ i ostao – proturječje. Dakle put tipa B je u cijelosti izvan $R$, a dječak s kojeg kreće je spareni dječak izvan $R$ (svi nespareni su u $R$).</p>
<p>Ključno je da se ta podjela održava i tijekom augmentacija na ovoj razini: augmentacija tipa A mijenja bridove samo unutar $R$, tipa B samo izvan $R$, a zatvorenost $R$ (u smislu rezidualnih lukova) se čuva jer novi iskorišteni bridovi imaju oba kraja na istoj strani. Dva potproblema stoga ne dijele ni vrhove ni bridove i njihove augmentacije komutiraju; maksimalan broj augmentacija cijene $-M+1$ je $k = f_A + f_B$, gdje je:</p>
<ul>
<li>$f_A$ = maksimalni tok u mreži: $S \to$ nespareni dječaci; nespareni bridovi $b \to g$ i spareni $g \to b$ među vrhovima iz $R$; sparene djevojčice iz $R$ $\to T$;</li>
<li>$f_B$ = maksimalni tok u mreži: $S \to$ dječaci izvan $R$ (svi spareni); bridovi među vrhovima izvan $R$ (isto usmjereni); nesparene djevojčice $\to T$.</li>
</ul>
<p>Svi kapaciteti su $1$, pa su to obične jedinične mreže i Dinic na njima radi u $O(m\sqrt{n})$. Kombinacija maksimalnog toka po razini cijene daje tok jednak onome koji bi našao SSP, a taj je minimalnog troška; time je $k$ točan.</p>

<h3>6. Algoritam</h3>
<ol>
<li>Dinic za maksimalno bipartitno sparivanje: $\nu$, oznake <code>used</code> po bridovima, partneri <code>matchB</code>, <code>matchG</code>.</li>
<li>BFS iz nesparenih dječaka po alternirajućim koracima → skup $R$ (oznake <code>inRB</code>, <code>inRG</code>).</li>
<li>Dinic za $f_A$ na mreži iz $R$; Dinic za $f_B$ na mreži izvan $R$.</li>
<li>Ispiši $n_1 + n_2 - 2\nu - f_A - f_B$ i $f_A + f_B$.</li>
</ol>

<h3>7. Primjer</h3>
<p>$n_1 = 5$, $n_2 = 6$, veze $(1,1),(2,1),(2,2),(3,2),(4,2),(4,3),(5,3),(5,4),(5,5),(5,6)$. Dječaci $b_1, b_2, b_3$ imaju zajedno samo susjede $g_1, g_2$, pa je po Hallovu uvjetu $\nu \le 4$; sparivanje $b_1 g_1, b_2 g_2, b_4 g_3, b_5 g_4$ pokazuje $\nu = 4$. Nespareni dječak je $b_3$, nesparene djevojčice $g_5, g_6$. Alternirajući putevi iz $b_3$: $b_3 \to g_2 \to b_2 \to g_1 \to b_1$, pa je $R = \{b_3, g_2, b_2, g_1, b_1\}$ – bez nesparenih djevojčica, kako i mora biti. Tip A: $b_3$ ($-M$) $\to g_2$ ($+1$) – jedan put, $f_A = 1$ ($g_2$ postaje centar trojke $\{b_2, g_2, b_3\}$). Tip B izvan $R$: $b_5$ ($+1$) $\to g_5$ ($-M$) – $f_B = 1$ ($b_5$ centar trojke $\{g_4, b_5, g_5\}$); drugi put $b_5 \to g_6$ nije moguć jer bi $b_5$ dobio stupanj $3$, a $b_4$ nema nesparenih susjeda. Dakle $k = 2$, $C = 2 \cdot 4 + 2 = 10$, samaca $11 - 10 = 1$ ($g_6$), trojki $2$: ekipe $\{b_1, g_1\}$, $\{b_2, g_2, b_3\}$, $\{b_4, g_3\}$, $\{g_4, b_5, g_5\}$, $\{g_6\}$ – odgovor <code>1 2</code>.</p>

<h3>8. Složenost i zamke</h3>
<p>Tri Dinica na jediničnim mrežama s $O(n)$ vrhova i $O(m)$ bridova: $O(m\sqrt{n})$ ukupno, memorija $O(n + m)$. Zamke: (a) u tipu B moraju biti isključeni <em>svi</em> vrhovi iz $R$, uključujući sparene djevojčice iz $R$ – inače bi se putevi tipa B „ušuljali” u $R$ i završili u sparenoj djevojčici s cijenom $+2$; (b) rekurzivni DFS u Dinicu ima dubinu $O(n)$, što je za $10^5$ u redu, ali povećaj stog ako koristiš rekurzivni BFS/DFS drugdje; (c) ne zaboravi da su svi dječaci izvan $R$ spareni (izvor u tipu B ide na sve njih preko brida $+1$); (d) odgovor je $(\text{samci}, \text{trojke})$, ne $(\text{samci}, \text{parovi})$.</p>
''',
    'verified': r'''uzorak 1/1; 300 slučajnih testova ($n_1, n_2 \le 5$, $m \le 10$) protiv brute forcea koji enumerira sve podskupove bridova sa stupnjevima $\le 2$ i računa (samci, trojke) po komponentama; 3 velika testa ($n_1 = n_2 = 10^5$, $m = 2 \cdot 10^5$, uključujući zvijezde i gusta sparivanja, $\lt 0.5$ s).''',
},
# ---------------------------------------------------------------- I
{
    'letter': 'I', 'title': 'Not Another Range Query Problem', 'title_hr': 'Ne još jedan zadatak s upitima na intervalu', 'slug': 'I_not_another_range_query_problem',
    'tl': '3 s', 'ml': '1024 MiB',
    'statement': r'''
<p>Za binarni niz $s$ neka je $L(s)$ skup indeksa $i$ takvih da je $i = 1$ ili $s_i \ne s_{i-1}$ (počeci maksimalnih blokova jednakih znakova); $L(\varepsilon) = \emptyset$. Neka $f(s)$ briše iz $s$ sve znakove s indeksima u $L(s)$, npr. $f(0011100) = 0110$, $f(01) = \varepsilon$. Definiraj $f^0(s) = s$, $f^k(s) = f^{k-1}(f(s))$.</p>
<p>Dan je niz $s$ duljine $n$ i $q$ upita $(l, r, k)$: ispiši duljinu niza $f^k(s[l..r])$.</p>
<h3>Ulaz</h3>
<p>$n, q$ ($1 \le n, q \le 5 \cdot 10^5$), niz $s$ i $q$ upita s $1 \le l \le r \le n$, $0 \le k \le n$.</p>
<h3>Izlaz</h3>
<p>Za svaki upit tražena duljina.</p>
<h3>Primjer</h3>
<p>$s = 100110001$: $(2, 5, 1)$: $f(0011) = 01$ → $2$; $(4, 8, 2)$: $f^2(11000) = f(100) = 0$ → $1$; $(1, 9, 8)$ → $0$.</p>
''',
    'hints': [
        r'''<p>Usporedi jednu primjenu $f$ na podniz $s[l..r]$ s primjenom $f$ na cijeli niz $s$: blokovi unutar $[l, r]$ isti su, osim što je u podnizu pozicija $l$ <em>uvijek</em> početak bloka. Razlika je dakle samo u (možda) izbrisanom prvom znaku.</p>''',
        r'''<p>Zaključak: $f^k(s[l..r]) = f^k(s) \cap [l_k, r]$, gdje pokazivač $l_k$ u svakom koraku skoči na prvu preživjelu poziciju strogo desno od sebe. Simuliraj $n$ operacija na cijelom nizu (ukupno $\le n$ brisanja) i istodobno pomiči pokazivače svih upita — ali pokazivači se moraju pomicati skupno.</p>''',
        r'''<p>Pokazivače prikaži kao <em>rangove</em> (redni broj među preživjelima). Brisanje elementa ranga $d$ smanjuje za $1$ sve pokazivače s rangom $\ge d$, a zatim se svi pokazivači povećaju za $1$. Relativni poredak pokazivača nikad se ne mijenja — sortiraj upite po $l$ i koristi segmentno stablo s dodavanjem na sufiksu.</p>''',
    ],
    'coach': [
        (r'''Kako se jedna primjena $f$ na podniz $s[l..r]$ razlikuje od primjene $f$ na cijeli niz $s$?''',
         r'''<p>Znak na poziciji $i$ briše se ako je početak bloka – tj. ako je prvi u nizu ili se razlikuje od prethodnika. Za $i \in (l, r]$ prethodnik je isti u podnizu i u cijelom nizu, pa je odluka jednaka. Jedina razlika je pozicija $l$: u podnizu je prva pa se <em>uvijek</em> briše, a u cijelom nizu samo ako je početak bloka. Zaključak: $f(s[l..r])$ je točno $f(s)$ ograničen na pozicije $(l, r]$, tj. na $[l', r]$ gdje je $l'$ prva pozicija iza $l$ koja je preživjela u $f(s)$.</p>'''),
        (r'''Vrijedi li isto i nakon više koraka – što je invarijanta?''',
         r'''<p>Da, indukcijom. Neka je $S_j$ skup pozicija cijelog niza koje su preživjele $j$ koraka i pretpostavimo $f^j(s[l..r]) = S_j \cap [h_j, r]$ za neku „glavu” $h_j \in S_j$. Elementi tog skupa osim glave imaju u podnizu iste prethodnike kao u $S_j$ (prethodnik je $\ge h_j$ jer je $h_j$ preživio), pa se brišu točno kad se brišu u cijelom nizu; glava se briše sigurno. Dakle $f^{j+1}(s[l..r]) = S_{j+1} \cap [h_{j+1}, r]$, gdje je $h_{j+1}$ prvi element $S_{j+1}$ strogo veći od $h_j$. Odgovor na upit $(l, r, k)$ je $|S_k \cap [h_k, r]|$ uz $h_0 = l$.</p>'''),
        (r'''Kako brzo simulirati $f$ na cijelom nizu do $n$ puta?''',
         r'''<p>U jednom koraku brišu se svi počeci blokova. Nakon brisanja novi početak bloka može postati samo element čiji se prethodnik promijenio – dakle sljedbenik nekog izbrisanog elementa. Uz dvostruko povezanu listu svaki korak stoji $O(\#\text{izbrisanih})$, a svaki element se briše jednom: ukupno $O(n)$ (uz sortiranje kandidata $O(n \log n)$). Tako za svaku poziciju dobivamo <em>vrijeme smrti</em> $d(x)$, a Fenwickovo stablo nad „živim” pozicijama daje rang $\mathrm{rang}_j(x) = |S_j \cap [1, x]|$.</p>'''),
        (r'''Kako istodobno pomicati glave svih $q$ upita, kad se svaka mora pomaknuti na prvog preživjelog iza sebe?''',
         r'''<p>Glavu ne čuvamo kao poziciju nego kao <em>rang</em> u $S_j$. Ako se u koraku $j+1$ brišu elementi $p$ s pozicijama $\le h_j$ (njih $c$), tada je $\mathrm{rang}_{j+1}(h_{j+1}) = \mathrm{rang}_j(h_j) - c + 1$: preživjelih do $h_j$ je $\mathrm{rang}_j(h_j) - c$, a $h_{j+1}$ je prvi sljedeći. Glave upita sortiranih po $l$ ostaju sortirane (funkcija „prvi preživjeli iza” je monotona), pa za svaki izbrisani $p$ oduzimamo $1$ na <em>sufiksu</em> upita čiji je rang $\ge \mathrm{rang}_j(p)$ – granicu nađemo binarnim spustom po segmentnom stablu s maksimumom, a „$+1$ svima” držimo implicitno kao pomak $j$.</p>'''),
        (r'''Kako iz ranga glave dobiti odgovor?''',
         r'''<p>Nakon $k$ koraka, $|S_k \cap [h_k, r]| = \mathrm{rang}_k(r) - \mathrm{rang}_k(h_k) + 1$, gdje je $\mathrm{rang}_k(r) = |S_k \cap [1, r]|$ iz Fenwickova stabla. Ako je glava prešla $r$, razlika je negativna i odgovor je $0$. Upite grupiramo po $k$ i odgovaramo točno nakon $k$-tog koraka; ukupno $O((n + q) \log n)$.</p>'''),
    ],
    'tips': [
        r'''Kad se operacija na podnizu razlikuje od operacije na cijelom nizu samo „na rubu”, simuliraj proces jednom globalno i za svaki upit prati samo rub (glavu) – to je opći obrazac za upite oblika „$k$ primjena operacije na $s[l..r]$”.''',
        r'''Pokazivače koji se pomiču na „sljedećeg živog” čuvaj kao <em>rangove</em> među živima: brisanje tada postaje „$-1$ na sufiksu”, a ako je početni poredak monoton i preslikavanje monotono, sufiks je uvijek kontinuiran raspon – segmentno stablo s lijenim dodavanjem i binarnim spustom.''',
        r'''Simulacija „briši sve početke blokova” je amortizirano linearna jer se status početka bloka mijenja samo sljedbenicima izbrisanih – općenito: nakon lokalne promjene provjeri samo susjede promijenjenih.''',
        r'''U simulacijama s povezanom listom u kojima se u istom koraku briše više susjednih elemenata, pokazivači izbrisanih elemenata ostaju pokazivati na mrtve – ako ih kasnije čitaš („sljedbenik izbrisanog”), sažmi ih odmah; stress-test malih slučajnih testova protiv brute forcea takve greške pronalazi u nekoliko sekundi.''',
    ],
    'solution': r'''
<p>Uočimo odnos između upita na intervalu i operacije nad cijelim nizom: razlikuju se zapravo samo u jednoj, možda izbrisanoj, prvoj poziciji. Kad operaciju izvodimo nad cijelim nizom, pozicija $l$ koja bi se u podnizu izbrisala možda se ne izbriše.</p>
<p>Dok simuliramo $n$ operacija nad cijelim nizom, za svaki upit istodobno održavamo gdje se trenutno nalazi njegova prva pozicija (početno $l_i$). Kad nad cijelim nizom izvedemo jednu operaciju, $l_i$ se mijenja tako da: ako je ta pozicija u operaciji nad cijelim nizom već izbrisana, pomaknemo se za jedno mjesto udesno; inače je trebala biti izbrisana (kao prvi znak podniza), pa se svejedno pomaknemo za jedno mjesto udesno.</p>
<p>Oznake pozicija su dinamičke, pa ih treba dinamički održavati. Oznake izvornog niza lako se održavaju Fenwickovim stablom.</p>
<p>No $l_i$ upita zapravo označava „koji po redu” među trenutno preostalim znakovima. Kad brišemo, svim oznakama većim od određene vrijednosti treba oduzeti $1$. Uočimo da se relativni poredak oznaka od početka do kraja ne mijenja, pa nakon sortiranja to održavamo segmentnim stablom.</p>
<p>Za konačni odgovor dovoljno je od trenutne oznake još preostalog prethodnika pozicije $r_i$ oduzeti održavanu oznaku trenutne prve pozicije $l_i$ (uvećano za jedan, uz odgovor $0$ ako je razlika negativna).</p>
''',
    'detailed': r'''
<h3>1. Notacija</h3>
<p>Pozicije cijelog niza su $1, \dots, n$. Neka je $S_0 = \{1, \dots, n\}$ i $S_j$ skup pozicija koje su preživjele $j$ primjena $f$ na <em>cijeli</em> niz $s$ (kao niz znakova, $f^j(s)$ je upravo $s$ ograničen na $S_j$, u istom poretku). Za $x \in S_j$ neka je $\mathrm{rang}_j(x) = |S_j \cap [1, x]|$ redni broj među preživjelima; za bilo koju poziciju $x$ ista formula daje broj preživjelih do $x$ uključivo.</p>

<h3>2. Ključna lema: podniz $=$ cijeli niz ograničen na prozor</h3>
<p><strong>Lema.</strong> Za upit $(l, r)$ definiramo $h_0 = l$ i $h_{j+1} = \min\{x \in S_{j+1} : x \gt h_j\}$ (ako takvog nema, $h_{j+1} = n+1$). Tada je $f^j(s[l..r])$ (kao niz pozicija) jednak $S_j \cap [h_j, r]$ za svaki $j \ge 0$.</p>
<p><em>Dokaz indukcijom.</em> Za $j = 0$ tvrdnja glasi $[l, r] = S_0 \cap [l, r]$. Pretpostavimo $T_j := f^j(s[l..r]) = S_j \cap [h_j, r]$ s $h_j \in S_j$ (ili $T_j = \emptyset$, tada su i svi daljnji prazni). Primjena $f$ na $T_j$ briše element $x \in T_j$ ako je prvi u $T_j$ ili se razlikuje od svog prethodnika u $T_j$. Za $x \ne h_j$ prethodnik u $T_j$ jednak je prethodniku $x$ u $S_j$: to je najveći element $S_j$ manji od $x$, a on je $\ge h_j$ jer je $h_j \in S_j$ i $h_j \lt x$, pa leži u prozoru. Dakle $x$ se briše iz $T_j$ točno kad se briše iz $S_j$, tj. $x \in T_{j+1} \iff x \in S_{j+1}$ za $h_j \lt x \le r$. Glava $h_j$ briše se iz $T_j$ uvijek (prvi element). Zato $T_{j+1} = S_{j+1} \cap (h_j, r] = S_{j+1} \cap [h_{j+1}, r]$, i $h_{j+1} \in S_{j+1}$ ako je prozor neprazan. $\square$</p>
<p>Odgovor na upit $(l, r, k)$ je stoga $|S_k \cap [h_k, r]| = \max(0,\ \mathrm{rang}_k(r) - \mathrm{rang}_k(h_k) + 1)$. Za $k \gt$ broj koraka do potpunog brisanja niza odgovor je $0$; u implementaciji jednostavno simuliramo svih $n$ koraka (nakon što niz postane prazan, koraci više ništa ne mijenjaju).</p>

<h3>3. Simulacija na cijelom nizu u $O(n \log n)$</h3>
<p>Korak $f$ na cijelom nizu briše sve <em>početke blokova</em>: poziciju $x \in S_j$ koja je prva ili čiji se znak razlikuje od znaka njezina prethodnika u $S_j$. Održavamo dvostruko povezanu listu preživjelih (<code>prv</code>, <code>nxt</code>) i skup početaka blokova tekućeg koraka.</p>
<p><strong>Opažanje.</strong> Nakon brisanja skupa $D$ početaka, novi početak bloka može biti samo element $x \in S_{j+1}$ čiji se prethodnik promijenio – tj. čiji je stari prethodnik bio u $D$. Takvi su $x$ upravo prvi preživjeli sljedbenici izbrisanih elemenata. Zato u koraku: (1) svakom $p \in D$ zapišemo vrijeme smrti $d(p) = j+1$ i izbacimo ga iz liste; (2) za svaki $p \in D$ nađemo prvog živog iza njega (ako je <code>nxt[p]</code> također izbrisan u ovom koraku, preusmjerimo <code>nxt[p]</code> na <code>nxt[nxt[p]]</code>; obradom silazno po poziciji to je jedan skok) i provjerimo je li on sada početak bloka; (3) kandidate sortiramo i oni su $D$ sljedećeg koraka. U koraku s $|D|$ brisanja ima najviše $|D|$ kandidata (jedan po izbrisanom), a svaki element umre točno jednom, pa je $\sum_j |D_j| = n$ i cijela simulacija je $O(n)$ uz $O(n \log n)$ za sortiranja kandidata. Dobivamo $d(x)$ za svaku poziciju i skupove $D_j$ izbrisanih u koraku $j$.</p>
<p>Pogreška koju treba izbjeći: ako se $p$ i $\mathrm{nxt}[p]$ brišu u istom koraku, standardno izbacivanje iz liste ostavlja $\mathrm{nxt}[p]$ da pokazuje na mrtav element, pa je krivi kandidat proglašen početkom bloka. Preusmjeravanje pokazivača silazno po poziciji rješava to u jednom prolazu (put je već „sažet” za veće $p$).</p>

<h3>4. Rangovi umjesto pozicija</h3>
<p>Fenwickovo stablo nad pozicijama drži $1$ za žive elemente; nakon $j$ koraka $\mathrm{rang}_j(x)$ je prefiksni zbroj do $x$. Sada glave upita. Neka se u koraku $j+1$ briše skup $D_{j+1}$ i neka je $c = |\{p \in D_{j+1} : p \le h_j\}|$. Preživjelih u $S_{j+1}$ do $h_j$ uključivo ima $\mathrm{rang}_j(h_j) - c$, a $h_{j+1}$ je prvi element iza njih, pa
$$\mathrm{rang}_{j+1}(h_{j+1}) = \mathrm{rang}_j(h_j) - c + 1.$$
Ako je $h_j$ sam izbrisan, on je uračunat u $c$ – formula i dalje vrijedi. Isto vrijedi i za $h_j = n+1$ (rang $|S_j|+1$, ostaje „iza kraja”).</p>
<p><strong>Monotonost.</strong> Preslikavanje $h \mapsto$ „prvi element $S_{j+1}$ iza $h$” je monotono neopadajuće, pa ako upite sortiramo po $l$, njihove glave (i rangovi glava) ostaju sortirane u svakom koraku. Uvjet $p \le h_j$ za fiksni izbrisani $p$ ekvivalentan je $\mathrm{rang}_j(p) \le \mathrm{rang}_j(h_j)$ (rang je monoton po poziciji, a $\mathrm{rang}_j(p)$ računamo <em>prije</em> brisanja u tom koraku), pa upiti koje $p$ pogađa čine <em>sufiks</em> sortiranog niza upita. Segmentno stablo nad upitima (u poretku po $l$) čuva vrijednost $v_i = \mathrm{rang}_j(h_j^{(i)}) - j$ – pomak $-j$ apsorbira „$+1$ svima” iz svakog koraka. Za svaki $p \in D_{j+1}$: nađi prvi indeks s $v_i + j \ge \mathrm{rang}_j(p)$ binarnim spustom po maksimumima (niz je monoton, pa maksimum podstabla odlučuje na koju stranu ići) i dodaj $-1$ na sufiksu. Tek nakon svih $p$ iz koraka ažuriramo Fenwick (brisanja), da bi svi $\mathrm{rang}_j(p)$ bili u odnosu na $S_j$.</p>

<h3>5. Odgovaranje na upite</h3>
<p>Upite grupiramo po $k$. Nakon $k$-tog koraka (i za $k = 0$ prije prvog) za svaki upit s tim $k$ pročitamo $\mathrm{rang}_k(h_k) = v_i + k$ (točkasti upit u segmentnom stablu) i $\mathrm{rang}_k(r)$ iz Fenwicka te ispišemo $\max(0, \mathrm{rang}_k(r) - \mathrm{rang}_k(h_k) + 1)$.</p>

<h3>6. Primjer</h3>
<p>$s = 100110001$, upit $(4, 8, 2)$: $s[4..8] = 11000$. Globalno: počeci blokova u $S_0$ su $\{1, 2, 4, 6, 9\}$, pa $S_1 = \{3, 5, 7, 8\}$ (niz $0\,1\,0\,0$). Glava: $h_0 = 4$, $h_1 = 5$ (prvi u $S_1$ iza $4$); $S_1 \cap [5, 8] = \{5, 7, 8\}$, tj. $100 = f(11000)$ ✓. Drugi korak: počeci u $S_1$ su $\{3, 5, 7\}$, $S_2 = \{8\}$; $h_2 = 8$, $S_2 \cap [8, 8] = \{8\}$, odgovor $1$ – i doista $f(100) = 0$ ima duljinu $1$. Rangovima: $\mathrm{rang}_0(h_0) = 4$; u koraku $1$ izbrisani $\le 4$ su $\{1, 2, 4\}$, $c = 3$, $\mathrm{rang}_1(h_1) = 4 - 3 + 1 = 2$ (pozicija $5$ je druga u $S_1$ ✓); u koraku $2$ izbrisani $\le 5$ su $\{3, 5\}$, $\mathrm{rang}_2(h_2) = 2 - 2 + 1 = 1$; $\mathrm{rang}_2(8) = 1$; odgovor $1 - 1 + 1 = 1$.</p>

<h3>7. Složenost i zamke</h3>
<p>Simulacija $O(n \log n)$; svaki od $\le n$ brisanja izaziva jedan spust i jedno lijeno ažuriranje, $O(\log q)$; svaki upit jedan točkasti upit i jedan Fenwick upit. Ukupno $O((n + q) \log n)$ vremena i $O(n + q)$ memorije. Zamke:</p>
<ul>
<li>rangove računaj u odnosu na $S_j$ <em>prije</em> brisanja tekućeg koraka – Fenwick ažuriraj tek nakon obrade svih $p \in D_{j+1}$;</li>
<li>pokazivači <code>nxt</code> izbrisanih elemenata unutar istog koraka (odjeljak 3);</li>
<li>glava može prijeći $r$ ili $n$ – odgovor tada mora biti $0$, ne negativan;</li>
<li>$k$ može biti $0$ (odgovor $r - l + 1$) i $k$ može biti veći od broja koraka do praznog niza;</li>
<li>vrijednosti $v_i$ mogu biti negativne (pomak $-j$), koristi predznačeni tip; ispis $5 \cdot 10^5$ redaka skupi u buffer.</li>
</ul>
''',
    'verified': r'''uzorak 1/1; 300 slučajnih testova ($n \le 12$, $q \le 10$, binarni nizovi različite gustoće jedinica, $0 \le k \le n$) protiv brute forcea koji izravno simulira $f^k$ na podnizu; 3 velika testa ($n = q = 5 \cdot 10^5$: slučajan niz, niz s dugim blokovima i niz od dva bloka, $\lt 0.5$ s).''',
},
# ---------------------------------------------------------------- J
{
    'letter': 'J', 'title': 'Best Carry Player 3', 'title_hr': 'Najbolji igrač s prijenosom 3', 'slug': 'J_best_carry_player_3',
    'tl': '1 s', 'ml': '1024 MiB',
    'statement': r'''
<p>Dani su $X, Y, K$. Dopuštene operacije: $X \leftarrow X + 1$; $X \leftarrow X - 1$ (ako $X \gt 0$); $X \leftarrow X \oplus t$ za neki $0 \le t \le K$. Nađi najmanji broj operacija da $X$ postane $Y$.</p>
<h3>Ulaz</h3>
<p>$T \le 10^5$ testova; $X, Y, K$ ($0 \le X, Y, K \lt 2^{60}$).</p>
<h3>Izlaz</h3>
<p>Najmanji broj operacija.</p>
<h3>Primjer</h3>
<p>$(5, 8, 3)$: $5 \oplus 2 = 7$, $7 + 1 = 8$ → $2$. $(9, 2, 6)$: $9 - 1 - 1 = 7$, $7 \oplus 5 = 2$ → $3$. $(0, 2^{60} - 1, 1)$ → $2^{60} - 1$.</p>
''',
    'hints': [
        r'''<p>Neka je $m$ najmanji broj s $2^m \gt K$. Operacija $\oplus$ mijenja samo najnižih $m$ bitova, pa brojeve grupiraj po $\lfloor x / 2^m \rfloor$. Kako se najbrže kreće <em>unutar</em> grupe, a kako <em>između</em> grupa?</p>''',
        r'''<p>Unutar grupe: $0$ ako su jednaki; $1$ ako je $x \oplus y \le K$ ili $|x - y| \le 1$; inače $2$. Između grupa: postavi donjih $m$ bitova na sve jedinice, pa $+1$; po grupi to košta $2$ ako je $K = 2^m - 1$, inače $3$ (za $K = 0$ samo $1$).</p>''',
    ],
    'coach': [
        (r'''Koje bitove operacija $\oplus\, t$ s $t \le K$ uopće može promijeniti?''',
         r'''<p>Neka je $m$ najmanji broj s $2^m \gt K$ (dakle $K$ ima točno $m$ binarnih znamenki; za $K = 0$ je $m = 0$). Svaki $t \le K$ je manji od $2^m$, pa ima nule na svim bitovima $\ge m$. XOR s takvim $t$ mijenja samo najnižih $m$ bitova, tj. ne mijenja $\lfloor x / 2^m \rfloor$. Zato brojeve grupiramo po $g(x) = \lfloor x / 2^m \rfloor$: unutar grupe se krećemo XOR-om i s $\pm 1$, a <em>između</em> grupa isključivo s $\pm 1$, i to samo preko granice (iz $g \cdot 2^m + 2^m - 1$ u $(g+1) 2^m$ i obratno).</p>'''),
        (r'''Koliko poteza treba između dva broja iste grupe?''',
         r'''<p>$0$ ako su jednaki. $1$ ako je $x \oplus y \le K$ (jedan XOR) ili $|x - y| = 1$ (jedan $\pm 1$). Inače uvijek točno $2$: $d = x \oplus y \lt 2^m$ i $d \gt K \ge 2^{m-1}$, pa $d$ ima bit $m-1$ postavljen; napiši $d = 2^{m-1} \oplus d'$ s $d' \lt 2^{m-1} \le K$. Oba dijela su $\le K$, pa $x \oplus 2^{m-1} \oplus d' = y$ u dva XOR-a. Manje od $2$ ne ide jer smo isključili slučajeve za $0$ i $1$.</p>'''),
        (r'''Kako izgleda optimalni put ako su $X$ i $Y$ u različitim grupama, $g(X) \lt g(Y)$?''',
         r'''<p>Svaki potez mijenja grupu za najviše $1$ i to samo potezom $+1$ iz „vrha” grupe ($2^m - 1$ u donjim bitovima) u „dno” sljedeće ($0$ u donjim bitovima) – ili $-1$ obratno. Put od $X$ do $Y$ mora proći kroz sve grupe između, a vraćanje unatrag nikad ne pomaže (svaki prelazak preko iste granice u oba smjera može se izbaciti). Zato je optimalni put: $X \to$ vrh grupe $g(X)$, $+1$, dno $\to$ vrh sljedeće grupe, $+1$, …, dno grupe $g(Y) \to Y$. Svaki komad je kretanje unutar grupe s poznatom cijenom $0/1/2$; komad „dno $\to$ vrh” košta $1$ ako je $K = 2^m - 1$ (jedan XOR s $K$), inače $2$ (za $K = 0$ je dno $=$ vrh, cijena $0$).</p>'''),
        (r'''Zašto formulu smijemo primijeniti i kad je $X \gt Y$, i kako izbjeći prekoračenja?''',
         r'''<p>Sve tri operacije su reverzibilne ($+1 \leftrightarrow -1$, XOR je sam sebi inverz), pa je udaljenost simetrična i možemo zamijeniti $X$ i $Y$. Broj međugrupa $g(Y) - g(X) - 1$ može biti do $2^{60}$, pa se množi s cijenom po grupi u 64-bitnom tipu bez pomoćnog zbrajanja; ukupan odgovor je najviše oko $3 \cdot 2^{60}$, što stane u <code>unsigned long long</code>. Za $m = 60$ izraz $2^m$ još stane, ali $2^{m+1}$ ne bi – zato $m$ računamo petljom <code>while ((1ULL &lt;&lt; m) &lt;= K) m++</code>, a ne preko $2K$.</p>'''),
    ],
    'tips': [
        r'''Kad operacija XOR ima gornju granicu $t \le K$, ključna veličina je <em>najmanji</em> $m$ s $2^m \gt K$: donjih $m$ bitova je „slobodno” (svaka promjena u najviše $2$ XOR-a jer je $2^{m-1} \le K$), a gornji su nedodirljivi.''',
        r'''U zadacima „najmanji broj operacija” s reverzibilnim operacijama udaljenost je simetrična – sortiraj krajeve i obradi samo jedan smjer.''',
        r'''Kad odgovor može biti $\sim 2^{60}$, ne simuliraj, računaj aritmetički; koristi <code>unsigned long long</code> i pazi na pomak <code>1ULL &lt;&lt; 60</code> (nikad <code>1 &lt;&lt; m</code> s 32-bitnim <code>1</code>).''',
        r'''Za male granice BFS po vrijednostima do nekoliko puta $\max(X, Y, K)$ savršen je brute force za provjeru zatvorene formule.''',
    ],
    'solution': r'''
<p>Dan je broj $x$ s operacijama $+1$, $-1$ i $\oplus$ s brojem koji ne prelazi $K$; tražimo najmanji broj koraka da postane $y$.</p>
<p>Promotrimo najmanji $m$ za koji vrijedi $2^m \gt K$: operacija $\oplus$ može promijeniti samo najnižih $m$ binarnih znamenki. Stoga sve brojeve grupiramo prema $\lfloor i / 2^m \rfloor$.</p>
<p>Za dva broja u istoj grupi: ako su jednaki, treba $0$ koraka; ako je njihov $\oplus$ najviše $K$ ili se razlikuju za najviše $1$, treba $1$ korak; inače trebaju $2$ koraka.</p>
<p>Za brojeve u različitim grupama nužno je najprije donjih $m$ bitova pretvoriti u $m$ jedinica, zatim dodati $1$ da se prijeđe u sljedeću grupu, i tako sve dok ne dođemo u istu grupu.</p>
<p>Za svaku grupu koju prelazimo trebaju $2$ koraka ako je $K = 2^m - 1$, a inače $3$ koraka.</p>
''',
    'detailed': r'''
<h3>1. Grupe po gornjim bitovima</h3>
<p>Neka je $m$ najmanji nenegativan cijeli broj s $2^m \gt K$ i $B = 2^m$. Za $K = 0$ je $m = 0$, $B = 1$; za $K = 3$ je $m = 2$, $B = 4$; općenito $2^{m-1} \le K \lt 2^m$ kad je $K \ge 1$. Svaki $t \le K$ zadovoljava $t \lt B$, pa XOR s $t$ mijenja samo najnižih $m$ bitova. Definiramo <em>grupu</em> broja $x$ kao $g(x) = \lfloor x / B \rfloor$ i <em>ostatak</em> $x \bmod B$ (donjih $m$ bitova).</p>
<p><strong>Opažanje 1.</strong> XOR nikad ne mijenja grupu. Operacije $\pm 1$ mijenjaju grupu samo kad prelaze granicu: $+1$ iz broja s ostatkom $B - 1$ („vrh” grupe) u broj s ostatkom $0$ („dno” sljedeće grupe), i $-1$ obratno. To slijedi iz $g(x+1) = g(x)$ osim kad je $x \bmod B = B - 1$.</p>

<h3>2. Udaljenost unutar grupe</h3>
<p>Za $x, y$ s $g(x) = g(y)$ tvrdimo da je najmanji broj poteza
$$d(x, y) = \begin{cases} 0, & x = y,\\ 1, & x \oplus y \le K \ \text{ili}\ |x - y| = 1,\\ 2, & \text{inače.}\end{cases}$$
Slučajevi $0$ i $1$ su očiti (jedan XOR s $t = x \oplus y$ ili jedan $\pm 1$), a manje se ne može jer nijedna operacija ne postiže $y$ ako uvjet za $1$ ne vrijedi. Za gornju granicu $2$ u trećem slučaju: $d = x \oplus y$ ima nule iznad bita $m-1$ (ista grupa), pa $d \lt B = 2^m$; kako je $d \gt K \ge 2^{m-1}$, bit $m-1$ od $d$ je jedan. Rastavimo $d = 2^{m-1} \oplus d'$ gdje je $d' = d - 2^{m-1} \lt 2^{m-1} \le K$. Oba su $\le K$, pa $x \xrightarrow{\oplus 2^{m-1}} x \oplus 2^{m-1} \xrightarrow{\oplus d'} y$. (Slučaj $m = 0$, tj. $K = 0$: grupa je jednočlana, pa je uvijek $x = y$.)</p>
<p>Uočimo da smo u trećem slučaju pretpostavili $m \ge 1$ – što je ispunjeno jer za $K = 0$ treći slučaj ne nastupa. Također, ostanak u grupi tijekom ta dva poteza je zajamčen jer su oba XOR-i.</p>

<h3>3. Udaljenost između grupa</h3>
<p>Operacije su reverzibilne, pa je udaljenost simetrična; neka je $g(X) \lt g(Y)$ (inače zamijenimo). Svaki potez mijenja grupu za najviše $1$, pa put mora barem jednom prijeći svaku granicu $g \mid g+1$ za $g(X) \le g \lt g(Y)$, i to potezom $+1$ iz vrha grupe $g$ u dno grupe $g+1$. Optimalan put prelazi svaku granicu <em>točno</em> jednom: ako bi je prešao tri puta (gore-dolje-gore), izbacivanjem dijela između prvog i trećeg prelaska dobivamo kraći valjan put (oba su prelaska iz istog vrha u isto dno). Zato se optimalni put rastavlja na komade unutar pojedinih grupa:</p>
<ol>
<li>$X \to$ vrh grupe $g(X)$, tj. broj $g(X) B + B - 1$: cijena $d(X, g(X)B + B - 1)$;</li>
<li>$+1$: cijena $1$;</li>
<li>za svaku međugrupu $g(X) \lt g \lt g(Y)$: dno $\to$ vrh ($d(gB, gB + B - 1) = d(0, B-1)$, jer $d$ ovisi samo o ostacima) pa $+1$; cijena $c = d(0, B-1) + 1$;</li>
<li>u grupi $g(Y)$: dno $\to Y$, cijena $d(g(Y) B, Y)$.</li>
</ol>
<p>Cijena po međugrupi: $0 \oplus (B-1) = B - 1 = 2^m - 1$; ako je $K = 2^m - 1$, to je $\le K$ i $d(0, B-1) = 1$, pa $c = 2$; inače (za $m \ge 2$; za $m = 1$ je $K = 1 = 2^1 - 1$ nužno) $d = 2$ i $c = 3$; za $K = 0$ je $B = 1$, dno $=$ vrh, $c = 1$. Točno kako kaže službeno rješenje: „$2$ koraka ako je $K = 2^m - 1$, inače $3$”, uz poseban slučaj $K = 0$.</p>
<p>Ukupno: $$\mathrm{ans} = d(X, \text{vrh}_{g(X)}) + 1 + (g(Y) - g(X) - 1)\, c + d(\text{dno}_{g(Y)}, Y).$$</p>

<h3>4. Primjeri</h3>
<p>$(5, 8, 3)$: $m = 2$, $B = 4$; $g(5) = 1$, $g(8) = 2$. Vrh grupe $1$ je $7$: $5 \oplus 7 = 2 \le 3$, cijena $1$; $+1$ daje $8 = Y$, cijena $1$; dno grupe $2$ je $8 = Y$, cijena $0$. Ukupno $2$.<br>
$(9, 2, 6)$: zamijenimo u $(2, 9, 6)$; $m = 3$, $B = 8$; $g(2) = 0$, $g(9) = 1$. Vrh grupe $0$ je $7$: $2 \oplus 7 = 5 \le 6$, cijena $1$; $+1 \to 8$; $d(8, 9) = 1$. Ukupno $3$.<br>
$(0, 2^{60}-1, 1)$: $m = 1$, $B = 2$; $g(0) = 0$, $g(Y) = 2^{59} - 1$; $d(0, 1) = 1$, $+1$, po grupi $c = 2$, na kraju $d(Y-1, Y) = 1$. Ukupno $1 + 1 + (2^{59} - 2) \cdot 2 + 1 = 2^{60} - 1$.</p>

<h3>5. Složenost i zamke</h3>
<p>Po testu $O(\log K)$ za određivanje $m$ (ili $O(1)$ s <code>__builtin_clzll</code>), ukupno $O(T \log K)$; memorija $O(1)$.</p>
<ul>
<li>Sve u <code>unsigned long long</code>: $X, Y, K \lt 2^{60}$, ali odgovor može biti $\approx 3 \cdot 2^{60}$; broj međugrupa množi se s $c \le 3$.</li>
<li>Pomak <code>1ULL &lt;&lt; m</code> za $m \le 60$ je u redu; ne računaj $2K + 1$ ni $B \cdot 2$.</li>
<li>Uvjet $|x - y| = 1$ provjeravaj kao <code>x + 1 == y || y + 1 == x</code> – bez oduzimanja u neoznačenom tipu.</li>
<li>Slučaj $K = 0$: XOR je beskoristan, odgovor je $|X - Y|$; formula ga daje automatski ($m = 0$, $B = 1$, $c = 1$).</li>
</ul>
''',
    'verified': r'''uzorak 1/1; 300 slučajnih testova ($X, Y, K \le 40$, uključujući $K = 0$ i $K = 2^m - 1$) protiv BFS-a po vrijednostima u $[0, 4\max(X,Y,K) + 8)$; 3 velika testa ($T = 10^5$, vrijednosti do $2^{60}$, $\lt 0.1$ s).''',
},
# ---------------------------------------------------------------- K
{
    'letter': 'K', 'title': 'Balancing Sequences', 'title_hr': 'Uravnoteženi nizovi', 'slug': 'K_balancing_sequences',
    'tl': '3 s', 'ml': '1024 MiB',
    'statement': r'''
<p>Dana su dva niza $a_1, a_2$ duljine $n$ koji zajedno sadrže sve brojeve $1, \dots, 2n$, te ciljni nizovi $b_1, b_2$ s istim svojstvom. Jedina dopuštena operacija: odaberi $(x_1, x_2, y_1, y_2)$ s $x_1, y_1 \in \{1, 2\}$, $x_2 \ne y_2$, $a_{x_1, x_2} \gt a_{3 - x_1, x_2}$ i $a_{y_1, y_2} \gt a_{3 - y_1, y_2}$ (oba odabrana elementa su <em>veći</em> u svom stupcu) i zamijeni $a_{x_1, x_2}$ i $a_{y_1, y_2}$. Može li se $(a_1, a_2)$ pretvoriti u $(b_1, b_2)$? Ako da, ispiši plan s najviše $5n$ koraka.</p>
<h3>Ulaz</h3>
<p>$T \le 10^5$ testova; $n$ ($2 \le n \le 2000$) i nizovi $a_1, a_2, b_1, b_2$. $\sum n^2 \le 4 \cdot 10^6$.</p>
<h3>Izlaz</h3>
<p>$-1$, ili broj koraka $s \le 5n$ i koraci $x_1\ x_2\ y_1\ y_2$.</p>
<h3>Primjer</h3>
<p>$a = \begin{pmatrix} 1 &amp; 2 \\ 3 &amp; 4 \end{pmatrix}$, $b = \begin{pmatrix} 4 &amp; 3 \\ 2 &amp; 1 \end{pmatrix}$ → $-1$. $a = \begin{pmatrix} 1 &amp; 2 &amp; 4 \\ 3 &amp; 5 &amp; 6 \end{pmatrix}$, $b = \begin{pmatrix} 1 &amp; 2 &amp; 4 \\ 5 &amp; 3 &amp; 6 \end{pmatrix}$ → jedan korak <code>2 2 2 1</code>.</p>
''',
    'hints': [
        r'''<p>Operacija zamjenjuje samo <em>maksimume</em> stupaca. Minimum stupca može se promijeniti jedino tako da u stupac dođe manji element i postane novi minimum — dakle minimum stupca se nikad ne povećava, a minimum koji je „na mjestu” nikad se ne pomiče.</p>''',
        r'''<p>Podijeli zadatak u dva dijela: (1) postići da se minimumi po stupcima (vrijednost i redak) podudaraju s $b$; (2) kad se minimumi podudaraju, maksimumi se mogu proizvoljno permutirati zamjenama, uz pažnju da nova vrijednost ostane veća od minimuma — poredaj tako da $k$-ti najmanji minimum dobije $k$-ti najmanji maksimum.</p>''',
    ],
    'coach': [
        (r'''Koja se veličina u stupcu nikad ne povećava i što to znači za element koji je trenutno minimum?''',
         r'''<p>Operacija mijenja samo <em>maksimum</em> stupca: nova vrijednost ulazi na mjesto maksimuma, pa je novi minimum $\min(\text{stari min}, \text{nova})$ – minimum stupca nikad ne raste. Element koji je minimum ne može se pomaknuti dok je minimum (operacija ga ne bira), a redak minimuma mijenja se jedino tako da u suprotni redak uđe manja vrijednost. Odmah slijede dvije nemogućnosti: ako je $\min a_{\cdot, i} \lt \min b_{\cdot, i}$ – $-1$; ako su minimumi jednaki, ali u različitim recima – $-1$ (taj element više nikad neće otići).</p>'''),
        (r'''Ako se minimumi (vrijednost i redak) po stupcima već podudaraju, zašto maksimume možemo proizvoljno preurediti?''',
         r'''<p>Zamjena maksimuma stupaca $c$ i $d$ je „sigurna” ako obje nove vrijednosti ostaju veće od minimuma svojih stupaca: tada se minimumi (ni vrijednost ni redak) ne mijenjaju i ista zamjena ponovljena vraća stanje – sigurna zamjena je <em>reverzibilna</em>. Definiramo kanonsko stanje: stupac s $k$-tim najmanjim minimumom drži $k$-ti najmanji maksimum. Iz svakog stanja s danim minimumima dolazimo u kanonsko nizom sigurnih zamjena (obrađujemo stupce po rastućem minimumu i dovodimo traženi maksimum), a kanonsko stanje ovisi samo o minimumima. Zato $a \to \text{kanon} \to b$ (drugi dio unatrag) radi uvijek, s najviše $2(n-1)$ zamjena.</p>'''),
        (r'''Kako spustiti minimum stupca $c$ s $m$ na ciljni $m' \lt m$ i zašto redoslijed obrade po rastućem $m'$ nije slučajan?''',
         r'''<p>Nova vrijednost ulazi u redak maksimuma. Ako cilj $m'$ treba biti u <em>suprotnom</em> retku od trenutnog minimuma, dovoljna je jedna zamjena: dovedemo $m'$ u redak maksimuma, on postaje novi minimum. Ako treba biti u <em>istom</em> retku, minimum $m$ mora otići, a to može tek kad postane maksimum – trebamo posrednik $x \in (m', m)$: prvo $x$ ulazi u $c$ (postaje minimum u suprotnom retku), zatim $m$ (sad maksimum) zamijenimo s $m'$, koji ulazi u traženi redak i postaje minimum, a $x$ ponovno postaje maksimum. Da bi zamjene bile dopuštene, $m'$ i $x$ moraju u tom trenutku biti <em>maksimumi</em> svojih stupaca. Obradom po rastućem ciljnom $m'$ postižemo: svi minimumi manji od $m'$ već su na svojim mjestima, pa $m'$ nije ničiji minimum – nužno je maksimum.</p>'''),
        (r'''Zašto obrada jednog stupca ne pokvari druge i zašto je „nema posrednika” doista dokaz nemogućnosti?''',
         r'''<p>U svaki drugi stupac ulazi vrijednost veća od one koja izlazi (koja je bila maksimum), pa se tuđi minimumi ne mijenjaju. Ako pak u trenutku obrade stupca $c$ nijedna vrijednost iz $(m', m)$ nije maksimum, sve su one minimumi stupaca koji su ili „zaključani” (minimum se podudara s $b$ i nikad ne smije otići) ili neobrađeni s ciljem $\gt m'$. Promotrimo u <em>bilo kojem</em> rješenju prvu vrijednost $v$ iz tog intervala koja se pomakne: prije toga u njezin stupac morala je ući manja vrijednost $w$ – nemoguće za zaključani stupac, a za neobrađeni $w \ge \text{cilj} \gt m'$, pa je $w$ iz istog intervala i pomaknula se ranije – kontradikcija. Dakle nijedan posrednik nikad ne postaje dostupan, a $c$ bez posrednika ne može promijeniti minimum u istom retku: $-1$ je točan.</p>'''),
    ],
    'tips': [
        r'''Kod operacija koje smiju dirati samo „veći/aktivni” element tražite monotonu veličinu (ovdje minimum stupca nikad ne raste) – ona daje nužne uvjete i prirodan redoslijed obrade (po rastućem cilju).''',
        r'''Za preuređivanje „slobodnog” dijela stanja koristite <em>kanonski oblik</em> i reverzibilne poteze: $a \to$ kanon, pa unatrag kanon $\to b$. Dokaz je trivijalan, a broj poteza $2(n-1)$.''',
        r'''Argument „prva vrijednost koja se pomakne” (beskonačni spust) standardan je način da se pokaže da neka klasa elemenata nikad ne postaje dostupna.''',
        r'''Konstruktivni zadatak s presudom $-1$ testirajte i na <em>potpunosti</em>: BFS po svim stanjima za male $n$ daje točan skup dostižnih ciljeva, a checker simulira poteze – oboje treba proći.''',
    ],
    'solution': r'''
<p><em>Napomena:</em> službeno rješenje ovog zadatka (riješila ga je samo jedna ekipa) vrlo je sažeto; ovdje ga prenosimo vjerno, uz minimalna pojašnjenja.</p>
<p>Najprije u $a$ postavimo na nulu veći od brojeva $a_{1,i}$ i $a_{2,i}$ u svakom stupcu, a isto učinimo i s $b$.</p>
<p>Može se dokazati: ako su nakon te operacije $a$ i $b$ jednaki, tada uvijek možemo izvesti zamjene koje izjednačuju i izvorne $a$ i $b$. Konkretno, možemo postići da $k$-ti najmanji $\min(a_{1,i}, a_{2,i})$ odgovara $k$-tom najmanjem maksimumu; taj se korak jednostavno implementira.</p>
<p>Zadatak se time svodi na to kako postići da minimumi dvaju nizova budu jednaki na svakoj poziciji.</p>
<p>Zadržavši samo te pozicije, isključimo neke očito nerješive slučajeve:</p>
<ul>
<li>Budući da se minimum može samo monotono smanjivati, ako je minimum u $a$ manji od minimuma u $b$, nema rješenja.</li>
<li>Ako su minimumi na odgovarajućim pozicijama jednaki, ali nisu na istoj strani (u istom retku), očito nema rješenja.</li>
<li>Ako su minimumi na odgovarajućim pozicijama na istoj strani, označimo minimum u $a$ s $m$, a u $b$ s $m'$. Ako je $m' = m - 1$, ili ako ne postoji posredni element $x$ čija je vrijednost u intervalu $(m', m)$ i nalazi se na poziciji na kojoj se minimumi od $a$ i $b$ razlikuju, nema rješenja.</li>
</ul>
<p>Zatim svaki put odabiremo $m$ s najmanjim odgovarajućim $m'$ i dovodimo ga na mjesto izravno ili pomoću posrednog elementa dvjema zamjenama. Induktivno se može dokazati da se taj postupak uvijek može nastaviti dok minimumi dvaju nizova na odgovarajućim pozicijama ne postanu potpuno jednaki. Ukupan broj operacija je najviše $4n$, što prolazi.</p>
''',
    'detailed': r'''
<h3>1. Što operacija može, a što ne može</h3>
<p>Tablica je $2 \times n$; u svakom stupcu $i$ jedan je element <em>minimum</em> $m_i$, drugi <em>maksimum</em>. Operacija zamjenjuje maksimume dvaju različitih stupaca. Posljedice:</p>
<ul>
<li><strong>Minimum stupca nikad ne raste.</strong> Nova vrijednost ulazi na mjesto maksimuma; novi minimum je $\min(m_i, \text{nova}) \le m_i$.</li>
<li><strong>Minimum se ne miče dok je minimum.</strong> Operacija bira samo maksimume. Redak minimuma mijenja se jedino ako u suprotni redak uđe vrijednost manja od $m_i$.</li>
<li>Vrijednost koja ulazi u stupac i <em>veća</em> je od njegova minimuma postaje maksimum: minimum (vrijednost i redak) ostaje isti. Takvu zamjenu zovemo <em>sigurnom</em>; sigurna zamjena ponovljena na istim stupcima vraća prethodno stanje (reverzibilna je).</li>
</ul>

<h3>2. Nužni uvjeti</h3>
<p>Neka je $m_i$ minimum stupca $i$ u $a$ (u retku $s_i$), a $m'_i$ minimum u $b$ (u retku $s'_i$).</p>
<ul>
<li>$m_i \lt m'_i$: nemoguće (minimum ne raste).</li>
<li>$m_i = m'_i$, $s_i \ne s'_i$: nemoguće – minimum mora ostati $m_i$ zauvijek (ne smije se smanjiti jer se ne može vratiti), a dok je minimum ne miče se.</li>
<li>$m_i = m'_i$, $s_i = s'_i$: stupac je <em>zaključan</em> – u svakom rješenju njegov minimum ostaje netaknut (svaka manja vrijednost koja bi ušla trajno bi ga pokvarila). Maksimum mu se smije mijenjati, ali samo sigurnim zamjenama.</li>
<li>$m_i \gt m'_i$: stupac je <em>na čekanju</em>; njegov minimum treba spustiti na $m'_i$ u redak $s'_i$.</li>
</ul>

<h3>3. Faza 2: kad se minimumi podudaraju, maksimumi su slobodni</h3>
<p><strong>Lema.</strong> Ako $a$ i $b$ imaju u svakom stupcu isti minimum u istom retku, $a$ se sigurnim zamjenama može pretvoriti u $b$ s najviše $2(n-1)$ poteza.</p>
<p><em>Dokaz.</em> Definiramo <em>kanonsko</em> stanje za dane minimume: stupac s $k$-tim najmanjim minimumom drži $k$-ti najmanji maksimum (skup maksimuma je komplement skupa minimuma, pa je kanonsko stanje jednoznačno određeno minimumima – dakle isto za $a$ i $b$). Postupak <code>toCanon</code>: stupce poredamo po minimumu $\mu_0 \lt \mu_1 \lt \dots$, maksimume po veličini $M_0 \lt M_1 \lt \dots$; za $k = 0, 1, \dots$ ako stupac $c_k$ ne drži $M_k$, zamijenimo maksimum od $c_k$ s maksimumom stupca $j$ u kojem je $M_k$. Obje su zamjene sigurne:</p>
<ul>
<li>U $c_k$ ulazi $M_k$. Tvrdimo $M_k \gt \mu_k$: kad bi bilo $M_k \lt \mu_k$, svih $k+1$ maksimuma $M_0, \dots, M_k$ bilo bi $\lt \mu_k$, pa bi i minimumi njihovih $k+1$ stupaca bili $\lt \mu_k$ – ali samo $k$ minimuma je manje od $\mu_k$.</li>
<li>U $j$ ulazi stari maksimum $M_t$ stupca $c_k$; kako su $M_0, \dots, M_{k-1}$ već u obrađenim stupcima (koje kasnije ne diramo), $t \gt k$, pa $M_t \gt M_k \gt \mu_j$ (jer je $M_k$ bio maksimum stupca $j$).</li>
</ul>
<p>Zadnji stupac ne treba zamjenu, pa je najviše $n-1$ poteza. Konačno: $a \to \text{kanon}$ potezima $\mathrm{toCanon}(a)$, zatim $\text{kanon} \to b$ potezima $\mathrm{toCanon}(b)$ u obrnutom redoslijedu (svaki je reverzibilan, a obrnuti potez je opet zamjena trenutnih maksimuma istih stupaca). $\square$</p>

<h3>4. Faza 1: spuštanje minimuma</h3>
<p>Stupce na čekanju obrađujemo po <em>rastućem</em> ciljnom minimumu $m'_c$. Neka je $c$ na redu, trenutni minimum $m$ (u retku $s$), cilj $m' \lt m$ u retku $s'$.</p>
<p><strong>Tvrdnja A.</strong> U tom je trenutku $m'$ maksimum nekog stupca $d \ne c$. <em>Dokaz.</em> $m' \lt m = \min(c)$, pa $m' \notin c$. Kad bi $m'$ bio minimum stupca $d$: zaključani $d$ ima minimum $m'_d \ne m'$ (ciljni minimumi su različiti); već obrađeni $d$ ima minimum $m'_d \lt m'$; neobrađeni $d$ ima još početni minimum $m_d \gt m'_d \gt m'$ (Tvrdnja C kaže da se tuđi minimumi ne mijenjaju). Dakle $m'$ je maksimum. $\square$</p>
<ul>
<li><strong>Različiti reci</strong> ($s' \ne s$): jedna zamjena maksimuma stupaca $c$ i $d$. $m'$ ulazi u redak $3 - s = s'$, manji je od $m$, pa postaje minimum u traženom retku. U $d$ ulazi stari maksimum $M \gt m \gt m' \gt \min(d)$ – sigurno za $d$.</li>
<li><strong>Isti redak</strong> ($s' = s$): $m$ mora otići iz $c$, a može tek kad postane maksimum. Trebamo <em>posrednik</em> $x$ s $m' \lt x \lt m$ koji je trenutno maksimum svog stupca $e$. Potezi: (1) zamijeni maksimume $c$ i $e$ – $x$ ulazi u redak $3-s$, postaje minimum od $c$; u $e$ ulazi $M \gt m \gt x \gt \min(e)$ (sigurno). (2) Sada je $m$ maksimum od $c$ (u retku $s$); zamijeni maksimume $c$ i $d$ – $m'$ ulazi u redak $s$, $m' \lt x$, postaje minimum u traženom retku, a $x$ opet je maksimum; u $d$ ulazi $m \gt m' \gt \min(d)$ (sigurno). Ako takvog $x$ nema, odgovor je $-1$ (Tvrdnja B).</li>
</ul>
<p><strong>Tvrdnja C.</strong> Obrada stupca $c$ ne mijenja minimum nijednog drugog stupca. <em>Dokaz.</em> U svaki drugi stupac ulazi vrijednost veća od one koja iz njega izlazi, a ta je bila maksimum – pokazano u oba slučaja gore. $\square$ Zato je nakon obrade minimum od $c$ zauvijek $m'$ u retku $s'$ (nitko ga više ne dira osim sigurnim zamjenama u fazi 2).</p>

<h3>5. Tvrdnja B: „nema posrednika” je dokaz nemogućnosti</h3>
<p>Pretpostavimo da pri obradi $c$ (isti redak) nijedna vrijednost iz $I = (m', m)$ nije maksimum. Sve su one minimumi svojih stupaca. Kojih? Već obrađeni stupci imaju minimume $\lt m'$ – ne u $I$. Njihovi <em>početni</em> minimumi izašli su kao maksimumi (potez (2) šalje $m$ u $d$ kao maksimum) – da je neki od njih u $I$, bio bi dostupan posrednik. Posrednici ranijih obrada opet su maksimumi. Dakle su elementi od $I$ točno <em>početni</em> minimumi stupaca koji su ili zaključani ili neobrađeni (s ciljem $m'_d \gt m'$), i takvi su bili od početka.</p>
<p>Uzmimo bilo koji niz poteza koji iz početnog $a$ vodi u $b$. Da bi $c$ dobio minimum $m' \lt m$ u <em>istom</em> retku $s$, vrijednost $m$ mora otići, a prije toga u redak $3-s$ mora ući neka $y \lt m$; promotrimo posljednji trenutak kad se minimum vraća u redak $s$ – vrijednost $z$ koja tada ulazi ostaje minimum do kraja, pa je $z = m'$, a minimum koji je istisnula bio je $y' \in (m', m) = I$ i u nekom je trenutku ušao u $c$ – dakle se pomaknuo. Neka je $v \in I$ <em>prva</em> vrijednost iz $I$ koja se u tom nizu pomakne. Ona je početni minimum stupca $d$ i mora prije toga postati maksimum: u $d$ ulazi $w \lt v$. Ako je $d$ zaključan, njegov minimum trajno pada ispod $m'_d = v$ – kontradikcija. Ako je $d$ neobrađen, minimum od $d$ nikad ne smije pasti ispod $m'_d$, pa je $w \ge m'_d \gt m'$; dakle $w \in (m', v) \subset I$ i $w$ se pomaknula prije $v$ – kontradikcija s izborom $v$. Nijedna vrijednost iz $I$ nikad se ne pomiče, pa $c$ nema posrednika ni u jednom rješenju: rješenje ne postoji. $\square$</p>
<p>Napomena: posrednik smije biti i maksimum zaključanog stupca (zamjena je sigurna). Službeno rješenje uvjet formulira preko „pozicija na kojima se $a$ i $b$ razlikuju”; gornji dokaz koristi samo uvjet „$x \in (m', m)$ je trenutno maksimum”, a ispravnost presude potvrđena je i iscrpno (odjeljak 8).</p>

<h3>6. Algoritam</h3>
<ol>
<li>Za svaki stupac odredi $(m_i, s_i)$ i $(m'_i, s'_i)$; provjeri nužne uvjete iz odjeljka 2; stupce s $m_i \gt m'_i$ stavi na čekanje.</li>
<li>Stupce na čekanju sortiraj po $m'_i$ i obradi redom (1 ili 2 poteza); posrednik se traži linearno po vrijednostima $x = m'+1, \dots, m-1$ uz polje položaja <code>pr/pc</code> – $O(n)$ po stupcu.</li>
<li>$\mathrm{toCanon}(a)$ izvedi na $a$, zatim ispiši $\mathrm{toCanon}(b)$ unatrag (računa se na kopiji od $b$).</li>
</ol>
<p><strong>Broj poteza:</strong> faza 1 najviše $2$ po stupcu, dakle $\le 2n$; faza 2 $\le 2(n-1)$; ukupno $\le 4n - 2 \lt 5n$. <strong>Složenost:</strong> $O(n^2)$ po testu zbog traženja posrednika (moglo bi i $O(n \log n)$ strukturom, ali $\sum n^2 \le 4 \cdot 10^6$ to čini nepotrebnim); memorija $O(n)$.</p>

<h3>7. Primjer</h3>
<p>Drugi uzorak: $a = \begin{pmatrix} 1 &amp; 2 &amp; 4 \\ 3 &amp; 5 &amp; 6 \end{pmatrix}$, $b = \begin{pmatrix} 1 &amp; 2 &amp; 4 \\ 5 &amp; 3 &amp; 6 \end{pmatrix}$. Minimumi $1, 2, 4$ u prvom retku podudaraju se – samo faza 2. Sortirani maksimumi $3, 5, 6$: $a$ je već kanonski; u $b$ stupac $1$ (minimum $1$) treba $3$, koji je u stupcu $2$ – $\mathrm{toCanon}(b)$ ima jedan potez (zamjena maksimuma stupaca $1$ i $2$, oba u retku $2$), ispisan unatrag: <code>2 1 2 2</code>. Primjer za fazu 1: $a = \begin{pmatrix} 5 &amp; 1 &amp; 4 \\ 6 &amp; 2 &amp; 3 \end{pmatrix}$, $b = \begin{pmatrix} 2 &amp; 1 &amp; 6 \\ 5 &amp; 4 &amp; 3 \end{pmatrix}$. Stupci $2$ i $3$ su zaključani (minimumi $1$ u retku $1$ i $3$ u retku $2$); stupac $1$ ima $m = 5$ u retku $1$, cilj $m' = 2$ u istom retku. Posrednik iz $(2, 5)$ koji je maksimum: $3$ je minimum stupca $3$, ali $4$ je maksimum stupca $3$. Potez $(2,1)\leftrightarrow(1,3)$ daje $\begin{pmatrix} 5 &amp; 1 &amp; 6 \\ 4 &amp; 2 &amp; 3 \end{pmatrix}$ ($4$ je novi minimum stupca $1$ u retku $2$), potez $(1,1)\leftrightarrow(2,2)$ daje $\begin{pmatrix} 2 &amp; 1 &amp; 6 \\ 4 &amp; 5 &amp; 3 \end{pmatrix}$ – minimum $2$ u retku $1$ ✓. Faza 2: minimumi $1 \lt 2 \lt 3$ (stupci $2, 1, 3$) trebaju maksimume $4, 5, 6$; stupac $2$ drži $5$, a $4$ je u stupcu $1$ – potez $(2,2)\leftrightarrow(2,1)$ daje točno $b$ (koji je već kanonski). Ukupno $3$ poteza.</p>

<h3>8. Zamke i verifikacija</h3>
<ul>
<li>Ciljni redak odredi iz $b$ (gdje je $m'$ u $b$), a trenutni iz $a$; kod „istog retka” zamjena ide u dva koraka jer nova vrijednost uvijek ulazi u redak maksimuma.</li>
<li>Položaje vrijednosti ažuriraj pri svakoj zamjeni (<code>pr/pc</code>), inače traženje $m'$ i posrednika gleda zastarjelo stanje.</li>
<li>$\mathrm{toCanon}(b)$ računaj na kopiji – ne smije mijenjati $b$ s kojim se uspoređuje.</li>
<li>Ispis: do $5n$ redaka po testu, $\sum n \le \sqrt{T \sum n^2}$ – koristi izlazni buffer.</li>
<li>Presuda $-1$ je konstruktivnim dokazom nužna i dovoljna; dodatno je za $n \le 4$ provjerena BFS-om po svim stanjima (odjeljak <em>verified</em>).</li>
</ul>
''',
    'verified': r'''uzorci 2/2 (checker: valjanost poteza, $\le 5n$ koraka, konačno stanje, presuda $-1$); 300 slučajnih testova ($n \le 4$) protiv BFS-a po svim stanjima; iscrpno: za $n = 2$ sva, za $n = 3$ $400$ slučajnih početnih tablica $\times$ svih $720$ ciljeva, za $n = 4$ $40$ početnih tablica $\times$ svih $40\,320$ ciljeva ($1{,}6 \cdot 10^6$ testova) – presuda se poklapa s BFS-om, a svi ispisani planovi prolaze checker; 3 velika testa ($n = 2000$, $\sum n^2 = 4 \cdot 10^6$, $\lt 0.05$ s).''',
},
# ---------------------------------------------------------------- L
{
    'letter': 'L', 'title': 'Completely Multiplicative Function', 'title_hr': 'Potpuno multiplikativna funkcija', 'slug': 'L_completely_multiplicative_function',
    'tl': '2 s', 'ml': '1024 MiB',
    'statement': r'''
<p>Nađi potpuno multiplikativnu funkciju $f : \mathbb{N} \to \{-1, 1\}$ ($f(1) = 1$, $f(xy) = f(x) f(y)$) takvu da je $f(1) + f(2) + \dots + f(n) = k$, ili ispiši $-1$ ako ne postoji.</p>
<h3>Ulaz</h3>
<p>$T \le 10^5$ testova; $n, k$ ($0 \le k \le n \le 10^6$, $n \ge 1$). $\sum n \le 2 \cdot 10^6$.</p>
<h3>Izlaz</h3>
<p>$-1$ ili vrijednosti $f(1), \dots, f(n)$.</p>
<h3>Primjer</h3>
<p>$(4, 2)$: <code>1 -1 1 1</code>. $(10, 0)$: <code>1 -1 -1 1 1 1 -1 -1 1 -1</code>. $(10, 1)$: $-1$. $(10, 10)$: sve jedinice.</p>
''',
    'hints': [
        r'''<p>Zbroj $k$ znači da točno $\frac{n + k}{2}$ vrijednosti mora biti $1$ — nužno $n \equiv k \pmod 2$. Funkcija je određena vrijednostima na prostim brojevima.</p>''',
        r'''<p>Fiksiraj $f(p) = 1$ za sve proste $p \le \sqrt{n}$. Tada svaki prosti $p \gt \sqrt{n}$ utječe neovisno: brojevi $p, 2p, \dots, \lfloor n/p \rfloor p$ imaju sve ostale faktore male, pa $f(p) = -1$ smanjuje zbroj za točno $2 \lfloor n / p \rfloor$. Ostaje ruksak koji zbog gustoće prostih brojeva rješava greedy — bar za $n \ge 200$.</p>''',
    ],
    'coach': [
        (r'''Što uvjet „zbroj je $k$” govori o broju jedinica i koji je prvi nužni uvjet?''',
         r'''<p>Ako je $a$ vrijednosti $+1$ i $n - a$ vrijednosti $-1$, zbroj je $2a - n = k$, dakle $a = (n + k)/2$ – cijeli broj samo ako je $n \equiv k \pmod 2$. Inače je odgovor $-1$. Potpuno multiplikativna $f$ određena je vrijednostima na prostim brojevima: $f(p_1^{e_1} \cdots) = \prod f(p_i)^{e_i}$, i svaki izbor $f(p) \in \{\pm 1\}$ daje valjanu funkciju. Pitanje je dakle: koje se zbrojeve može dobiti izborom predznaka za proste brojeve?</p>'''),
        (r'''Zašto su prosti brojevi veći od $\sqrt{n}$ „neovisni” i koliki je doprinos svakog od njih?''',
         r'''<p>Broj $i \le n$ ima najviše jedan prosti faktor $p \gt \sqrt{n}$ (dva bi dala $i \gt n$), i to s eksponentom $1$. Višekratnici takvog $p$ u $[1, n]$ su $mp$ za $1 \le m \le \lfloor n/p \rfloor \lt \sqrt{n}$, pa je $f(mp) = f(m) f(p)$ gdje $m$ ima samo male proste faktore. Ako su vrijednosti na prostima $\le \sqrt{n}$ fiksirane, doprinos velikog prostog $p$ zbroju je $f(p) \cdot S(\lfloor n/p \rfloor)$, $S(x) = \sum_{m \le x} f(m)$, i ne ovisi o ostalim velikim prostima.</p>'''),
        (r'''Što se dogodi ako sve male proste brojeve postavimo na $+1$?''',
         r'''<p>Tada je $f(i) = +1$ za svaki $i$ bez velikog prostog faktora, a $S(x) = x$ za $x \lt \sqrt{n}$. Veliki prosti $p$ s $f(p) = -1$ pretvara točno $w_p = \lfloor n/p \rfloor$ jedinica u minus jedinice, tj. smanjuje zbroj za $2w_p$. Treba pretvoriti $D = (n - k)/2$ jedinica: <em>ruksak</em> s težinama $w_p$ – ali vrlo poseban: težine su $\lt \sqrt{n}$, težinu $1$ ima svaki prosti u $(n/2, n]$, a ukupni kapacitet $\sum w_p$ (broj brojeva do $n$ s velikim prostim faktorom, asimptotski $\ln 2 \cdot n \approx 0.69n$) prelazi $n/2 \ge D$.</p>'''),
        (r'''Zašto greedy „uzmi ako stane” po silaznim težinama uvijek uspije za $n \ge 200$?''',
         r'''<p>Ako nikad ne preskočimo, uzeli smo sve težine $\ge 2$ i ostatak $D' = D - \sum_{w_p \ge 2} w_p \le (\text{ukupni kapacitet}) - \sum_{w_p \ge 2} w_p = \#\{p : w_p = 1\}$ pokrivaju prosti težine $1$. Ako smo prvi put preskočili težinu $w$, otad je $D \lt w \lt \sqrt{n}$, a prostih težine $1$ ima $\pi(n) - \pi(n/2) \ge \sqrt{n}$ za $n \ge 200$ – opet dovoljno. Obje numeričke tvrdnje (kapacitet $\ge \lfloor n/2 \rfloor$ i $\pi(n) - \pi(n/2) \ge \lfloor\sqrt{n}\rfloor$) provjerene su za sve $200 \le n \le 10^6$.</p>'''),
        (r'''Zašto mali $n$ trebaju poseban tretman i kako ga učiniti egzaktnim?''',
         r'''<p>Za male $n$ brojevi bez velikog prostog faktora mogu činiti više od polovice, pa „svi mali prosti na $+1$” daje premalo kapaciteta. No za $n \lt 200$ jedini prosti $\le \sqrt{n} \lt 15$ su $2, 3, 5, 7, 11, 13$: isprobamo svih $2^6$ dodjela, a za svaki prosti $p \ge 17$ doprinos je $\pm S(\lfloor n/p \rfloor)$ neovisno – dostižne zbrojeve daje subset-sum bitsetom. To je <em>potpuna</em> enumeracija svih $f$, pa je $-1$ za mali $n$ egzaktan; predračun za sve $(n, k)$ traje zanemarivo.</p>'''),
    ],
    'tips': [
        r'''Potpuno multiplikativna $f$ sa vrijednostima $\pm 1$ = slobodan izbor predznaka na prostim brojevima; brojevi s velikim prostim faktorom ($\gt \sqrt{n}$) imaju ga točno jednog, pa su takvi prosti međusobno neovisni – standardna podjela „mali/veliki prosti” po $\sqrt{n}$.''',
        r'''Ruksak čije težine imaju mnogo primjeraka najmanje težine (ovdje $\ge \sqrt{n}$ jedinica) i ukupni kapacitet veći od cilja rješava se greedyjem po silaznim težinama: nakon prvog preskoka ostatak je manji od preskočene težine.''',
        r'''Kad tvrdnja o „raspodjeli prostih brojeva” ulazi u dokaz, provjeri je numerički za cijeli raspon ograničenja (sito do $10^6$ traje manje od sekunde) – to je dio verifikacije, ne dodatak.''',
        r'''Za male ulaze kod kojih asimptotski argument ne vrijedi, potpuna enumeracija po „stupnjevima slobode” (ovdje $2^6$ maski) plus subset-sum bitsetom daje egzaktnost bez nagađanja praga.''',
    ],
    'solution': r'''
<p>Uvjet je ekvivalentan tome da točno $\frac{n + k}{2}$ vrijednosti $f(i)$ bude jednako $1$.</p>
<p>Multiplikativna funkcija određena je vrijednostima na svim prostim brojevima. Kad odredimo vrijednosti na prostim brojevima do $\sqrt{n}$, doprinosi preostalih prostih brojeva odgovoru međusobno su neovisni.</p>
<p>Za $n \ge 200$ možemo sve proste brojeve do $\sqrt{n}$ postaviti na $1$; za preostale proste brojeve dobivamo problem ruksaka koji se, zbog svojstava raspodjele prostih brojeva, može riješiti greedy pristupom.</p>
<p>Za $n \le 200$ postavljanje svih prostih brojeva do $\sqrt{n}$ na $1$ može dovesti do toga da broj jedinica premaši polovicu; tada se vrijednosti malih prostih brojeva mogu odrediti pretraživanjem, randomizacijom i sličnim metodama, a odgovori se predračunaju.</p>
<p>Za ovaj zadatak postoje i pristupi bez posebnih slučajeva koji izravno podešavaju vrijednosti od malih prema velikim prostim brojevima, no njihova ispravnost nije nužno očita.</p>
''',
    'detailed': r'''
<h3>1. Parnost i stupnjevi slobode</h3>
<p>Neka $f$ ima $a$ vrijednosti $+1$ na $[1, n]$. Zbroj je $a - (n - a) = 2a - n = k$, pa je $a = (n+k)/2$; nužno $n \equiv k \pmod 2$, inače $-1$. Potpuno multiplikativna funkcija s vrijednostima u $\{\pm 1\}$ posve je određena vrijednostima $f(p)$ na prostim brojevima ($f(1) = 1$, $f(\prod p_i^{e_i}) = \prod f(p_i)^{e_i}$), i <em>svaki</em> izbor predznaka na prostima daje valjanu funkciju. Zadatak je stoga: izabrati predznake prostih brojeva $\le n$ tako da točno $(n+k)/2$ brojeva dobije $+1$.</p>

<h3>2. Mali i veliki prosti brojevi</h3>
<p>Neka je $s = \lfloor \sqrt{n} \rfloor$. Broj $i \le n$ ima najviše jedan prosti faktor $p \gt s$ i to u prvoj potenciji: dva takva faktora (ili $p^2$) dala bi $i \ge (s+1)^2 \gt n$. Za prosti $p \gt s$ višekratnici u $[1, n]$ su $p, 2p, \dots, w_p \cdot p$ s $w_p = \lfloor n/p \rfloor \le s$, a svaki množitelj $m \le w_p \lt p$ ima samo proste faktore $\le s$. Zato je $f(mp) = f(m) f(p)$, gdje je $f(m)$ određen malim prostima. Ako fiksiramo vrijednosti na prostima $\le s$, ukupni zbroj je
$$\sum_{i \le n} f(i) = B + \sum_{p \gt s} f(p) \, S(w_p), \qquad S(x) = \sum_{m \le x} f(m),$$
gdje je $B$ zbroj po brojevima bez velikog prostog faktora. Doprinosi velikih prostih brojeva su neovisni: svaki bira predznak svog člana $S(w_p)$.</p>

<h3>3. Veliki $n$ ($n \ge 200$): svi mali prosti na $+1$</h3>
<p>Stavimo $f(p) = +1$ za sve $p \le s$. Tada je $f(m) = +1$ za svaki $m$ bez velikog prostog faktora, pa $S(x) = x$ za $x \le s$ i $B$ = broj takvih $m$. Krenemo od $f \equiv +1$ (zbroj $n$) i za neke velike proste $p$ stavimo $f(p) = -1$: to pretvara točno $w_p$ jedinica (brojeve $p, 2p, \dots, w_p p$) u $-1$ i smanjuje zbroj za $2w_p$. Cilj: skup velikih prostih $P$ s $\sum_{p \in P} w_p = D := (n-k)/2$.</p>
<p>To je ruksak s vrlo posebnom strukturom:</p>
<ul>
<li>težine su $w_p \le s$; težinu $1$ imaju točno prosti u $(n/2, n]$, njih $c_1 = \pi(n) - \pi(n/2)$;</li>
<li>ukupni kapacitet $C = \sum_{p \gt s} w_p$ je broj brojeva $\le n$ s velikim prostim faktorom, asimptotski $(\ln 2) n \approx 0.69 n$.</li>
</ul>
<p><strong>Greedy.</strong> Prolazimo velike proste $p$ uzlazno (dakle težine $w_p$ silazno) i uzimamo $p$ ako $w_p \le D$, uz $D \leftarrow D - w_p$.</p>
<p><strong>Lema.</strong> Za $200 \le n \le 10^6$ greedy završava s $D = 0$.</p>
<p><em>Dokaz.</em> Koristimo dvije numeričke činjenice, provjerene sitom za svaki $n$ u tom rasponu: (i) $C \ge \lfloor n/2 \rfloor \ge D$ (najmanja rezerva je $2$); (ii) $c_1 \ge s$ (najmanja rezerva $3$). Slučaj A: greedy nikad ne preskoči prosti s $w_p \ge 2$. Tada je nakon njih $D' = D - \sum_{w_p \ge 2} w_p \le C - \sum_{w_p \ge 2} w_p = c_1$, pa preostalih $D'$ jedinica pokrijemo prostima težine $1$ (ima ih dovoljno, uzimamo prvih $D'$). Slučaj B: prvi preskok dogodi se pri težini $w \ge 2$; tada je $D \lt w \le s$, a $D$ dalje samo pada, pa pri dolasku na proste težine $1$ vrijedi $D \le s - 1 \lt c_1$ i opet ih ima dovoljno. $\square$</p>
<p>Napomena: preskok pri težini $w$ znači $D \lt w$, a svi kasniji prosti imaju težinu $\le w$; neki se možda još uzmu, ali $D \lt w$ ostaje. Za $n \lt 200$ činjenica (i) ne mora vrijediti (npr. za $n = 30$ brojeva bez prostog faktora $\gt 5$ ima $18 \gt 15$), zato poseban slučaj.</p>

<h3>4. Mali $n$ ($n \lt 200$): potpuna enumeracija</h3>
<p>Za $n \lt 200$ je $s \le 14$, pa su mali prosti samo $2, 3, 5, 7, 11, 13$ – $2^6 = 64$ dodjela. Za svaku dodjelu (masku) izračunamo $f$ na svim brojevima bez prostog faktora $\ge 17$ (jer $17^2 = 289 \gt 199$, svaki broj $\lt 200$ ima najviše jedan takav faktor), zbroj $B$ i za svaki prosti $p \ge 17$ doprinos $c_p = S(\lfloor n/p \rfloor)$, gdje je $\lfloor n/p \rfloor \le 11$ pa $S$ ovisi samo o maski. Zbroj je $B + \sum_p \pm c_p$; skup dostižnih zbrojeva računamo bitsetom (pomak $\pm |c_p|$, <code>reach = (reach &lt;&lt; a) | (reach &gt;&gt; a)</code> uz pomak indeksa $+2n$ da izbjegnemo negativne). Time za svaki par $(n, k)$ znamo postoji li rješenje i s kojom maskom; rekonstrukcija ide unatrag po bitsetima po prostima. Budući da smo isprobali <em>sve</em> vrijednosti na malim prostima i <em>sve</em> kombinacije predznaka velikih, odgovor $-1$ je za male $n$ egzaktan. (Pokazalo se – iscrpnim pokretanjem za sve $n \lt 300$ i sve $k$ – da rješenje postoji za svaki par s $n \equiv k \pmod 2$; algoritam to ne pretpostavlja.)</p>

<h3>5. Algoritam i složenost</h3>
<ol>
<li>Linearno sito do $10^6$: najmanji prosti faktor <code>lp[i]</code> i lista prostih.</li>
<li>Predračun za $n \lt 200$: $64$ maske $\times$ bitset duljine $1024$ $\times$ $\le 46$ prostih – zanemarivo.</li>
<li>Po testu: parnost; za $n \lt 200$ tablica + rekonstrukcija; za $n \ge 200$ greedy po prostima $\gt s$ (broj prostih do $n$ je $O(n / \log n)$), zatim $f(i) = f(\mathrm{lp}(i)) \cdot f(i / \mathrm{lp}(i))$ za sve $i \le n$ u $O(n)$.</li>
</ol>
<p>Ukupno $O(\sum n)$ nakon sita, uz $\sum n \le 2 \cdot 10^6$; ispis do $2 \cdot 10^6$ brojeva – u buffer. Memorija: $O(10^6)$ za sito.</p>

<h3>6. Primjer</h3>
<p>$(n, k) = (10, 0)$: $n \lt 200$, dakle enumeracija. Službeni izlaz <code>1 -1 -1 1 1 1 -1 -1 1 -1</code> odgovara $f(2) = f(3) = -1$, $f(5) = 1$, $f(7) = -1$: pet jedinica ($1, 4, 5, 6, 9$) i pet minus jedinica. Za veliki primjer $n = 1000$, $k = 0$: $s = 31$, $D = 500$; prvi veliki prosti $37$ ima $w = 27$, $41$ ima $24$, …; greedy uzima proste dok težine stanu, a ostatak $\lt 31$ pokrivaju prosti iz $(500, 1000]$ (ima ih $73$).</p>

<h3>7. Zamke</h3>
<ul>
<li>$k$ i $n$ iste parnosti je jedini razlog za $-1$ kod velikih $n$ – ali to je <em>posljedica</em> dokaza, ne pretpostavka; kod za male $n$ i dalje gleda tablicu.</li>
<li>$f$ na složenim brojevima računaj tek nakon što su svi $f(p)$ konačni (u malom slučaju veliki prosti privremeno imaju $+1$ tijekom računanja $B$).</li>
<li>Bitset indeksi: doprinosi mogu biti negativni; pomak $+2n$ i širina $1024 \ge 4n + 1$ za $n \lt 200$.</li>
<li>Sito do $10^6$ jednom, ne po testu ($T \le 10^5$).</li>
</ul>
''',
    'verified': r'''uzorak 1/1 (checker: multiplikativnost, vrijednosti $\pm 1$, zbroj $k$, presuda $-1$); 300 slučajnih testova ($T \le 6$, $n \le 30$) protiv iscrpnog brute forcea po svim dodjelama predznaka prostima; iscrpno svi parovi $(n, k)$ za $n \lt 300$ kroz checker; 3 velika testa ($\sum n = 2 \cdot 10^6$, uključujući $n = 10^6$ s $k \in \{0, 2, 10^6\}$, $\lt 0.2$ s); numerička provjera lema o kapacitetu i broju prostih u $(n/2, n]$ za sve $200 \le n \le 10^6$.''',
},
# ---------------------------------------------------------------- M
{
    'letter': 'M', 'title': 'Expression 3', 'title_hr': 'Izraz 3', 'slug': 'M_expression_3',
    'tl': '5 s', 'ml': '1024 MiB',
    'statement': r'''
<p>Dan je izraz $a_1\ \mathrm{op}_1\ a_2\ \mathrm{op}_2\ \cdots\ a_n$ s operatorima $+$ i $-$. U svakom od $n - 1$ koraka biraju se dva susjedna broja i operator među njima te se zamjenjuju rezultatom. Zbroji rezultate svih različitih slijedova operacija (dva slijeda su različita ako se u nekom koraku bira drugi par) i ispiši modulo $998244353$.</p>
<h3>Ulaz</h3>
<p>$n$ ($2 \le n \le 2 \cdot 10^5$), brojevi $a_i \le 10^9$ i niz operatora duljine $n - 1$.</p>
<h3>Izlaz</h3>
<p>Zbroj modulo $998244353$.</p>
<h3>Primjer</h3>
<p>$9 - 1 + 4 - 1$: šest slijedova s rezultatima $11, 11, 3, 5, 11, 5$ → $46$. $1 + 2 - 3 + 4 - 5$ → $998244313$.</p>
''',
    'hints': [
        r'''<p>Slijed operacija je permutacija operatora (redoslijed izvršavanja). Promatraj doprinos svakog $a_i$ zasebno: njegov se predznak mijenja svaki put kad se izvrši operator $-$ čiji desni operand sadrži $a_i$.</p>''',
        r'''<p>Operator $\mathrm{op}_j$ ($j \lt i$) sadrži $a_i$ u desnom operandu ako i samo ako se izvršava <em>nakon</em> svih $\mathrm{op}_{j+1}, \dots, \mathrm{op}_{i-1}$ — to je sufiksni rekord vremena izvršavanja. U slučajnoj permutaciji ti su događaji neovisni s vjerojatnošću $\frac{1}{i - j}$.</p>''',
        r'''<p>Očekivani predznak od $a_i$ je umnožak $\prod_j \frac{i - j - 1 + \mathrm{sgn}_j}{i - j}$; s $c_j = j + 1 - \mathrm{sgn}_j$ brojnik postaje $\prod_{j \le i-2}(i - c_j)$ — vrijednost polinoma u točki $i$ koja se mijenja množenjem jednim linearnim faktorom po koraku. Razmisli o diskretnom logaritmu + konvoluciji ili o razdvoji-pa-vladaj FFT-u.</p>''',
    ],
    'coach': [
        (r'''Kako zbroj po svim $(n-1)!$ slijedova pretvoriti u nešto što se računa po jednom broju $a_i$?''',
         r'''<p>Slijed operacija je permutacija $n-1$ operatora (redoslijed izvršavanja). Rezultat je uvijek $\sum_i \varepsilon_i a_i$ s predznacima $\varepsilon_i \in \{\pm 1\}$ koji ovise o permutaciji, pa je traženi zbroj $\sum_i a_i \sum_{\pi} \varepsilon_i(\pi) = (n-1)! \sum_i a_i \,\mathbb{E}[\varepsilon_i]$ za uniformno slučajnu permutaciju. Linearnost očekivanja razdvaja brojeve; ostaje izračunati očekivani predznak svakog $a_i$.</p>'''),
        (r'''Kada se predznak broja $a_i$ mijenja i koji operatori na to utječu?''',
         r'''<p>Pri izvršavanju operatora $\mathrm{op}_j$ ($x\ \mathrm{op}_j\ y$) desni blok $y$ ulazi u rezultat s predznakom $\mathrm{sgn}_j$; svaki broj u bloku $y$ tada „naslijedi” taj predznak (kod $-$ se svi okrenu). Dakle $\varepsilon_i = \prod \mathrm{sgn}_j$ po onim $j \lt i$ čiji desni operand u trenutku izvršavanja sadrži $a_i$. Desni operand od $\mathrm{op}_j$ je blok koji počinje s $a_{j+1}$ i seže do $a_i$ točno ako su svi operatori $\mathrm{op}_{j+1}, \dots, \mathrm{op}_{i-1}$ već izvršeni – $\mathrm{op}_j$ mora biti <em>sufiksni rekord</em> (najkasnije izvršen među $\mathrm{op}_j, \dots, \mathrm{op}_{i-1}$). Operatori desno od $a_i$ na njegov predznak ne utječu.</p>'''),
        (r'''Kolika je vjerojatnost da je $\mathrm{op}_j$ sufiksni rekord i zašto su ti događaji neovisni?''',
         r'''<p>U slučajnoj permutaciji vremena operatora $j, \dots, i-1$ svaki od $i-j$ operatora jednako je vjerojatno posljednji: $P = \frac{1}{i-j}$. Indikatori rekorda s desna za različite $j$ su <em>neovisni</em> (klasična činjenica: „je li $j$-ti element rekord” ovisi samo o relativnom poretku unutar sufiksa, a sufiksi se ugniježđuju – formalno, permutacija se bijektivno kodira nizom „relativnih rangova” koji su neovisni i uniformni). Zato $\mathbb{E}[\varepsilon_i] = \prod_{j \lt i} \left(1 - \frac{1}{i-j} + \frac{\mathrm{sgn}_j}{i-j}\right) = \prod_{j \lt i} \frac{i-j-1+\mathrm{sgn}_j}{i-j}$: faktor $1$ za $+$, $\frac{i-j-2}{i-j}$ za $-$.</p>'''),
        (r'''Kako za sve $i$ izračunati umnožak $V(i) = \prod_{j \lt i}(i - j - 1 + \mathrm{sgn}_j)$ brže od $O(n^2)$?''',
         r'''<p>Nazivnici daju $(i-1)!$. U brojniku je faktor $i-j$ za $+$ i $i-j-2$ za $-$; posebni su $j = i-1$ s $-$ (faktor $-1$) i $j = i-2$ s $-$ (faktor $0$, cijeli umnožak je $0$). Sve ostale faktore su pozitivni cijeli brojevi $\le n$, pa umnožak pretvorimo u <em>zbroj diskretnih logaritama</em> po bazi primitivnog korijena $g = 3$: $\log V(i) = \sum_{k} C[k]\, L(i-k)$, gdje je $L(d) = \log_g d$, a $C[k] = [\mathrm{op}_k = +] + [\mathrm{op}_{k-2} = -]$. To je jedna konvolucija (NTT).</p>'''),
        (r'''Kako dobiti diskretne logaritme svih brojeva do $n$ i zašto konvolucija ne smije ići „modulo $p$”?''',
         r'''<p>$L$ je potpuno aditivna: $L(ab) = L(a) + L(b) \pmod{p-1}$, pa je dovoljno izračunati $L(q)$ za proste $q \le n$ (njih $\approx n/\ln n$) i proširiti linearnim sitom. Za $p = 998244353$ je $p - 1 = 2^{23} \cdot 7 \cdot 17$ vrlo gladak, pa Pohlig–Hellman daje $L(q)$ u $O(23 \cdot 2 + 7 + 17)$ potenciranja. Zbroj logaritama je do $n \cdot 2^{30}$ i ne smije se reducirati modulo $p$ (treba modulo $p-1$!), pa $L$ rastavimo na tri dijela po $10$ bitova, svaki konvoluiramo egzaktno (zbrojevi $\lt 2 \cdot 10^8 \lt p$) i složimo natrag u 64-bitni broj. Ukupno $O(n \log n)$.</p>'''),
    ],
    'tips': [
        r'''„Zbroj rezultata po svim redoslijedima” $= (\#\text{redoslijeda}) \cdot \mathbb{E}[\text{rezultat}]$; linearnost očekivanja razdvaja doprinose pojedinih elemenata i pretvara kombinatoriku u vjerojatnost.''',
        r'''U slučajnoj permutaciji indikatori „$j$-ti element je (sufiksni) rekord” su neovisni s vjerojatnostima $1/(\text{duljina sufiksa})$ – vrlo korisna lema za očekivanja nad redoslijedima izvršavanja.''',
        r'''Umnožak oblika $\prod_j F(i - c_j)$ za sve $i$ je konvolucija <em>u logaritamskoj domeni</em>: diskretni logaritam po primitivnom korijenu pretvara množenje u zbrajanje; nule i negativne faktore izdvoji ručno. Za $998244353$ je $p-1 = 2^{23}\cdot 7 \cdot 17$, pa je Pohlig–Hellman trivijalan.''',
        r'''Kad konvolucija mora biti egzaktna (vrijednosti do $2^{30}$, zbrojevi do $2^{48}$), rastavi ulaz na komade od $\sim 10$ bitova i konvoluiraj svaki NTT-om – jeftinije i sigurnije od FFT-a s <code>double</code>.''',
    ],
    'solution': r'''
<p>Promotrimo konačni doprinos svakog broja odgovoru. Predznak broja $a_i$ mijenja se samo kad se $a_i$ nalazi na desnoj strani operacije čiji je operator minus.</p>
<p>Opažanjem se vidi da je dovoljno promatrati sufiksne minimume prioriteta operatora prije pozicije $i - 1$ (operatore koji se izvršavaju nakon svih operatora između njih i $a_i$).</p>
<p>Neka su pozicije tih operatora $p_1, p_2, \dots, p_k$ ($p_k = i - 1$). Vjerojatnost tog događaja je umnožak recipročnih vrijednosti duljina odgovarajućih sufiksa. Doprinos svake odabrane pozicije $j$ je $\mathrm{sgn}_j / (i - j - 1)$, a neodabrane $1$, pa je ukupni doprinos pozicije $j$ približno $\frac{\mathrm{sgn}_j + i - j - 1}{i - j - 1}$.</p>
<p>Treba dakle izračunati
$$a_1 + \sum_{i=2}^{n} \frac{a_i\, \mathrm{sgn}_{i-1}}{(i-1)!} \prod_{j=1}^{i-2} (\mathrm{sgn}_j + i - j - 1)$$
(i pomnožiti s $(n-1)!$, brojem svih slijedova).</p>
<p>Razmotrimo kako ubrzati izračun tog izraza. Nekoliko metoda prolazi zadatak:</p>
<ul>
<li>Riječ je o umnošku po $j$ od $1$ do $i - 2$ u kojem svaki član ima pomak $1$ ili $-1$. Može se primijeniti metoda <em>Four Russians</em>: podijelimo na blokove duljine $B$ i za svaki blok predračunamo sve mogućnosti; složenost $O(n^2 / B + \frac{n}{B} 2^B)$, uz pažljivu implementaciju.</li>
<li>Označimo $c_j = j + 1 - \mathrm{sgn}_j$. Umnožak je $\prod (i - c_j)$. Nad izrazom napravimo diskretni logaritam, uz dogovor da je logaritam negativnih brojeva i nule jednak $0$; problem postaje računanje $\sum \ln(i - c_j)$, što se rješava konvolucijom. Složenost $O(n \cdot (\text{diskretni logaritam}) + n \log n)$.</li>
<li>Uz $c_j = j + 1 - \mathrm{sgn}_j$ problem možemo gledati kao: za svaki $i$ najprije evaluiraj polinom u $i$, a zatim ga pomnoži s $(x - c_i)$. Uočimo $P(i) = P(x) \bmod (x - i) = [x^n]\, x^n P(1/x) / (1/x - i)$. Izvorni problem stoga je ekvivalentan umnošku polinoma uz računanje zbroja u kojem se svaki član dijeli razlomkom i množi koeficijentom, što se rješava razdvoji-pa-vladaj FFT-om.</li>
</ul>
<p><em>Napomena prevoditelja:</em> službeni tekst završava riječima „vremenska složenost je” bez navedene vrijednosti; za razdvoji-pa-vladaj FFT uobičajena je $O(n \log^2 n)$.</p>
''',
    'detailed': r'''
<h3>1. Od zbroja po slijedovima do očekivanja</h3>
<p>Slijed operacija je redoslijed u kojem se izvršava $n-1$ operatora – permutacija $\pi$ skupa $\{1, \dots, n-1\}$; svaka daje jedan od $(n-1)!$ slijedova (različit izbor para u nekom koraku $=$ različita permutacija). Rezultat je uvijek linearan u ulaznim brojevima, $R(\pi) = \sum_{i=1}^{n} \varepsilon_i(\pi) a_i$ s $\varepsilon_i(\pi) \in \{\pm 1\}$. Zato
$$\sum_\pi R(\pi) = \sum_i a_i \sum_\pi \varepsilon_i(\pi) = (n-1)! \sum_i a_i\, \mathbb{E}[\varepsilon_i],$$
gdje je očekivanje po uniformno slučajnoj permutaciji. Ostaje izračunati $\mathbb{E}[\varepsilon_i]$ za svaki $i$.</p>

<h3>2. Predznak broja $a_i$: sufiksni rekordi</h3>
<p>Kad izvršavamo $\mathrm{op}_j$, spajamo blok $X$ (završava s $a_j$) i blok $Y$ (počinje s $a_{j+1}$) u $X\ \mathrm{op}_j\ Y$. Predznaci brojeva u $X$ ostaju, predznaci brojeva u $Y$ množe se s $\mathrm{sgn}_j$ ($+1$ za $+$, $-1$ za $-$). Dakle
$$\varepsilon_i = \prod_{j \lt i,\ a_i \in Y_j} \mathrm{sgn}_j,$$
gdje je $Y_j$ desni operand u trenutku izvršavanja $\mathrm{op}_j$. Blok $Y_j$ počinje s $a_{j+1}$ i sadrži $a_i$ ($i \gt j$) ako i samo ako su svi operatori $\mathrm{op}_{j+1}, \dots, \mathrm{op}_{i-1}$ između njih već izvršeni – dakle ako $\mathrm{op}_j$ ima <em>najveće vrijeme izvršavanja</em> među $\mathrm{op}_j, \mathrm{op}_{j+1}, \dots, \mathrm{op}_{i-1}$. Takav $j$ zovemo sufiksnim rekordom (za $a_i$). Operatori $\mathrm{op}_j$ s $j \ge i$ imaju $a_i$ u lijevom operandu i ne mijenjaju mu predznak. Posebno, $a_1$ nikad nije u desnom operandu: $\varepsilon_1 = 1$.</p>

<h3>3. Vjerojatnost i neovisnost rekorda</h3>
<p>Za fiksni $i$ gledamo slučajnu permutaciju vremena $t_1, \dots, t_{i-1}$ (restrikcija uniformne permutacije na podskup je uniformna). Neka je $X_j = [\,t_j = \max(t_j, \dots, t_{i-1})\,]$. Tada je $P(X_j = 1) = \frac{1}{i-j}$ (svaki od $i-j$ elemenata sufiksa jednako je vjerojatno maksimum). Događaji $X_1, \dots, X_{i-1}$ su <em>neovisni</em>: permutaciju sufiksa $j, \dots, i-1$ jednoznačno određuju relativni rang $r_j$ elementa $t_j$ unutar tog sufiksa ($r_j \in \{1, \dots, i-j\}$) i permutacija sufiksa $j+1, \dots, i-1$; induktivno, $(r_1, \dots, r_{i-1})$ je bijekcija s permutacijama, pa su rangovi neovisni i uniformni, a $X_j = [r_j = i-j]$ je funkcija samo od $r_j$. Stoga
$$\mathbb{E}[\varepsilon_i] = \prod_{j=1}^{i-1} \mathbb{E}\big[\mathrm{sgn}_j^{X_j}\big] = \prod_{j=1}^{i-1}\left(1 - \tfrac{1}{i-j} + \tfrac{\mathrm{sgn}_j}{i-j}\right) = \prod_{j=1}^{i-1} \frac{i-j-1+\mathrm{sgn}_j}{i-j} = \frac{V(i)}{(i-1)!},$$
uz $V(i) = \prod_{j \lt i}(i - j - 1 + \mathrm{sgn}_j)$: faktor $i-j$ za $\mathrm{op}_j = +$, $i-j-2$ za $\mathrm{op}_j = -$.</p>
<p>Provjera na uzorku $9 - 1 + 4 - 1$ ($\mathrm{sgn} = (-,+,-)$): $\mathbb{E}[\varepsilon_1] = 1$; $\mathbb{E}[\varepsilon_2] = \frac{2-1-2}{1} = -1$; $\mathbb{E}[\varepsilon_3] = \frac{(3-1-2)}{2} \cdot \frac{3-2}{1} = 0$; $\mathbb{E}[\varepsilon_4] = \frac{1}{3} \cdot \frac{2}{2} \cdot \frac{-1}{1} = -\frac13$. Zbroj $9 - 1 + 0 - \frac13 = \frac{23}{3}$, puta $3! = 6$ daje $46$ ✓.</p>

<h3>4. Računanje $V(i)$ za sve $i$: logaritmi i konvolucija</h3>
<p>Naivno je $O(n^2)$. Razdvojimo faktore od $V(i)$:</p>
<ul>
<li>$j = i-1$ s $-$: faktor $i-(i-1)-2 = -1$;</li>
<li>$j = i-2$ s $-$: faktor $0$ – tada je $V(i) = 0$ ($\mathrm{op}_{i-2}$ je s vjerojatnošću $\frac12$ rekord, pa se doprinosi $\pm$ točno ponište);</li>
<li>svi ostali faktori su cijeli brojevi iz $[1, n]$: $i-j$ za $+$ ($j \le i-1$), $i-j-2$ za $-$ ($j \le i-3$).</li>
</ul>
<p>Neka je $g = 3$ primitivni korijen modulo $p = 998244353$ i $L(d) = \log_g d \in [0, p-2]$ diskretni logaritam. Za pozitivne faktore
$$\log_g V(i) \equiv \sum_{\substack{j \le i-1 \\ \mathrm{op}_j = +}} L(i-j) + \sum_{\substack{j \le i-3 \\ \mathrm{op}_j = -}} L(i-j-2) \pmod{p-1}.$$
Uvedimo $C[k] = [\mathrm{op}_k = +] + [\mathrm{op}_{k-2} = -]$ (za $-$ na poziciji $j$ stavljamo doprinos na $k = j+2$, jer je tada $i - j - 2 = i - k$). Obje sume postaju
$$E(i) = \sum_{k \lt i} C[k] \cdot L(i-k),$$
jedna konvolucija nizova $C$ i $L$ – točno oblik $\sum_k C[k] L[i-k]$ koji računa NTT. Zatim je $V(i) = \pm g^{E(i) \bmod (p-1)}$ (predznak iz prvog slučaja) ili $0$ (drugi slučaj).</p>

<h3>5. Diskretni logaritmi svih brojeva do $n$</h3>
<p>$L$ je potpuno aditivna: $L(ab) \equiv L(a) + L(b) \pmod{p-1}$. Linearnim sitom nađemo najmanji prosti faktor svakog $d \le n$ i $L(d) = L(\mathrm{lp}(d)) + L(d/\mathrm{lp}(d))$, pa treba izračunati $L(q)$ samo za proste $q \le n$, njih $\pi(n) \approx 18\,000$ za $n = 2 \cdot 10^5$.</p>
<p>Za jedan $L(q)$ koristimo Pohlig–Hellman jer je $p - 1 = 2^{23} \cdot 7 \cdot 17$: za svaki prosti faktor $r^e$ od $p-1$ računamo $x_r = L(q) \bmod r^e$ znamenku po znamenku u bazi $r$ ($e$ koraka, u svakom najviše $r$ pokušaja), a zatim složimo kineskim teoremom o ostacima. Trošak po prostom broju je nekoliko desetaka modularnih potenciranja – ukupno daleko ispod sekunde. (Alternativa je baby-step giant-step u $O(\sqrt{p})$ po broju, što bi bilo presporo za $18\,000$ prostih.)</p>

<h3>6. Egzaktna konvolucija velikih vrijednosti</h3>
<p>Vrijednosti $L(d) \lt 2^{30}$, a $E(i)$ je zbroj do $n$ takvih – do $\approx 2^{48}$. Konvolucija NTT-om daje rezultat <em>modulo $p$</em>, a nama treba $E(i)$ <em>modulo $p-1$</em>; reduciranje po krivom modulu potpuno bi uništilo rezultat. Zato $L$ rastavimo na tri dijela po $10$ bitova: $L = L_0 + 2^{10} L_1 + 2^{20} L_2$ s $L_t \lt 1024$. Konvolucija $C * L_t$ ima vrijednosti $\le n \cdot 2 \cdot 1023 \lt 4.1 \cdot 10^8 \lt p$, dakle egzaktna je; zbrojimo $E(i) = \sum_t 2^{10t} (C * L_t)(i)$ u 64-bitnom tipu i tek onda reduciramo modulo $p-1$. Tri NTT množenja duljine $2^{19}$.</p>

<h3>7. Algoritam i složenost</h3>
<ol>
<li>Linearno sito do $n$; Pohlig–Hellman za proste; $L(d)$ za sve $d \le n$. $O(n + \pi(n) \cdot \text{PH})$.</li>
<li>$C[k]$ iz operatora; $E = C * L$ u tri 10-bitna dijela NTT-om, $O(n \log n)$.</li>
<li>Za svaki $i$: $V(i) = 0$ ako je $\mathrm{op}_{i-2} = -$; inače $g^{E(i) \bmod (p-1)}$, negirano ako je $\mathrm{op}_{i-1} = -$.</li>
<li>Odgovor $(n-1)! \sum_i a_i V(i) / (i-1)! \bmod p$ uz predračunane inverze faktorijela.</li>
</ol>
<p>Ukupno $O(n \log n)$ vremena i $O(n)$ memorije; lokalno $\approx 0.2$ s za $n = 2 \cdot 10^5$ (limit $5$ s).</p>

<h3>8. Zamke</h3>
<ul>
<li>Eksponenti se reduciraju modulo $p-1$, koeficijenti modulo $p$ – ne miješati.</li>
<li>$a_i \le 10^9 \gt p$: reduciraj ulaz modulo $p$ prije množenja; $a_i \cdot V \cdot \mathrm{inv}$ množi u dva koraka da ne pretekne 64 bita.</li>
<li>Faktor $0$ (operator $-$ neposredno ispred $a_{i-1}$) i faktor $-1$ (operator $-$ neposredno ispred $a_i$) moraju biti izvan logaritamske domene.</li>
<li>Indeksiranje operatora: $\mathrm{op}_j$ stoji između $a_j$ i $a_{j+1}$; u nizu znakova je to indeks $j-1$.</li>
<li>Rezultat može biti „negativan” – drugi uzorak daje $998244313 \equiv -40$; ispiši nenegativni ostatak.</li>
</ul>
''',
    'verified': r'''uzorci 2/2; 300 slučajnih testova ($2 \le n \le 7$, $a_i \le 10$, slučajni operatori) protiv brute forcea koji enumerira svih $(n-1)!$ redoslijeda izvršavanja; 3 velika testa ($n = 2 \cdot 10^5$, $a_i \le 10^9$, $\approx 0.2$ s).''',
},
]
