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
        ('Opažanje: stablo = izbor roditelja', r'''<p>$T_1$ je određen roditeljem svakog $x \in [2, n]$ (roditelj je manji), $T_2$ roditeljem svakog $x \in [1, n-1]$ (roditelj je veći). Ukupno $2n - 2$ mjesta koja treba popuniti, a ulaz sadrži točno $2n - 2$ bridova.</p>'''),
        ('Redukcija na dodjelu bridova mjestima', r'''<p>Brid $(x, y)$, $x \lt y$, može popuniti mjesto „$T_1$-roditelj od $y$” ili mjesto „$T_2$-roditelj od $x$”. Izgradi pomoćni graf čiji su vrhovi mjesta, a svaki ulazni brid spaja svoja dva moguća mjesta. Traži se dodjela u kojoj svako mjesto dobije točno jedan brid. Petlja $(x, x)$ ne može popuniti nijedno mjesto — odgovor je odmah $0$.</p>'''),
        ('Algoritam i složenost', r'''<p>Rješenje postoji ako i samo ako je pomoćni graf pseudošuma u kojoj svaka komponenta ima točno onoliko bridova koliko i vrhova (jedan ciklus po komponenti). Svaka komponenta tada ima točno $2$ dodjele (dvije orijentacije ciklusa), pa je odgovor $2^C$, gdje je $C$ broj komponenata. DSU ili DFS, $O(n)$.</p>'''),
    ],
    'solution': r'''
<p>Stablo možemo promatrati kao izbor roditelja za svaki vrh: zadatak traži da svaki vrh iz $[1, n-1]$ dobije većeg roditelja (u $T_2$), a svaki vrh iz $[2, n]$ manjeg roditelja (u $T_1$).</p>
<p>Brid koji spaja $x$ i $y$ ($x \le y$) može postati brid od $x$ prema njegovom roditelju u stablu s većim roditeljima ili brid od $y$ prema njegovom roditelju u stablu s manjim roditeljima. Cijeli zadatak svodi se na to da svaki brid uparimo s jednim „mjestom” (vrhom jednog od dvaju stabala kojemu treba roditelj).</p>
<p>Ukupno postoji $2n - 2$ mjesta kojima treba odrediti roditelja, a u ulazu je točno $2n - 2$ bridova. Konstruiramo graf na mjestima u kojem svaki ulazni brid spaja svoja dva moguća mjesta. Rješenje postoji ako i samo ako je taj graf šuma <em>pseudostabala</em> — u svakoj komponenti broj bridova jednak je broju vrhova (komponenta sadrži točno jedan ciklus). Tada svaka komponenta ima točno dvije valjane dodjele (ciklus se može „orijentirati” na dva načina, a stabla obješena na ciklus su prisiljena), pa je odgovor $2^C$, gdje je $C$ broj komponenata.</p>
<p>Petlja $(x, x)$ ne može popuniti nijedno mjesto (roditelj mora biti strogo manji odnosno strogo veći), pa je tada odgovor $0$. Ukupna složenost je $O(n)$.</p>
<p><em>Zanimljivost:</em> zadatak je svojedobno bio planiran kao zadatak za interno natjecanje kineske reprezentacije.</p>
''',
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
        ('Opažanje 1: što operacije mogu, a što ne mogu', r'''<p>Ako je $g$ cikličan ili ako su vrhovi povezani u $f$ nepovezani u $g$, odgovor je <code>NO</code>. Ako je u konačnom stanju $x$ roditelj od $y$, tada je $y$ u nekom koraku izravno spojen (<code>unite</code>) na $x$. Budući da <code>find</code> samo razbija odnose predak–potomak i nikad ne stvara nove, svako ograničenje „$x$ mora biti predak od $y$” koje vrijedi na kraju mora vrijediti u <em>svakom</em> trenutku nakon nastanka.</p>'''),
        ('Opažanje 2: ograničenja među korijenima', r'''<p>Neka početno stanje ima stabla $T_1, \dots, T_k$ s korijenima $r_1, \dots, r_k$ (pretpostavi da je konačno stanje jedno stablo; inače radi po komponentama). Ako u konačnom stanju podstablo od $r_x$ sadrži vrh $u$ koji je početno bio u stablu $r_y$, onda je u nekom trenutku $r_x$ bio predak od $r_y$. Tako dobivamo ograničenja oblika „$r_x$ mora biti predak od $r_y$”. Ako ograničenja tvore ciklus — <code>NO</code>. Inače uzmi bilo koji topološki poredak i po njemu konstruiraj rješenje.</p>'''),
        ('Alat: podizanje podstabla', r'''<p>Ako je $x$ korijen, $y$ dijete od $x$, a $z$ dijete od $y$, tada <code>find(z)</code> prebacuje $z$ (s njegovim podstablom) izravno pod $x$, a ostatak strukture ne mijenja. To je osnovni potez za „rastavljanje” početnih stabala. Nadalje, početno ne-korijenski vrh $t$ ostaje izravno dijete od $f[t]$ ako i samo ako nad $t$ nikad nije pozvan <code>find</code>; usporedbom s $g$ točno znamo nad kojim vrhovima treba pozvati <code>find</code>, a najbolje ih je pozvati odmah na početku.</p>'''),
        ('Algoritam i broj operacija', r'''<p>Najprije izvedi sve potrebne <code>find</code> pozive, zatim po topološkom poretku korijena sastavljaj ciljno stablo operacijama <code>unite</code> (koje spajaju korijene) i <code>find</code> (koji podižu podstabla na pravo mjesto). Obrada jednog vrha zahtijeva najviše $n$ operacija, pa je gruba gornja granica $n^2 + n \le 2n^2$.</p>'''),
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
        ('Lema I', r'''<p>Posljednji vrh bilo kojeg DFS poretka je list: da ima dijete, ono bi bilo posjećeno nakon njega.</p>'''),
        ('Lema II', r'''<p>Drugi vrh u DFS poretku $D_x$ izravno je susjedan s $x$ (prvi posjećeni vrh nakon korijena je jedno njegovo dijete).</p>'''),
        ('Algoritam i složenost', r'''<p>Uzmi bilo koji poredak, njegov posljednji vrh $v$ je list; u $D_v$ drugi element $u$ je susjed od $v$ — brid $(u, v)$. Ukloni $v$ iz svih poredaka (uklanjanje lista ostavlja valjane DFS poretke preostalog stabla) i ponavljaj. Ukupno $O(n^2)$ po testu, što uz $\sum n^2 \le 2 \cdot 10^6$ prolazi.</p>'''),
    ],
    'solution': r'''
<p><b>Lema I.</b> Posljednji vrh DFS poretka nužno je list.</p>
<p><b>Lema II.</b> Drugi vrh DFS poretka nužno je izravno susjedan prvom vrhu.</p>
<p>Stoga jednostavno neprestano uklanjamo listove: iz bilo kojeg poretka pročitamo posljednji vrh $v$ (list), iz poretka $D_v$ pročitamo drugi element — to je jedini susjed lista $v$ — zabilježimo brid, uklonimo $v$ iz svih poredaka i ponavljamo dok ne ostane jedan vrh. Složenost je $O(n^2)$ po testu.</p>
<p><em>Zanimljivost:</em> DFS Order bio je zadatak na EC-Finalu 2021, a DFS Order 2 na regionalnom natjecanju u Jinanu 2022.</p>
''',
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
        ('Opažanje: algebraizacija brisanja', r'''<p>Brisanje $s_i = s_{i+1}$ na susjednim pozicijama različitog pariteta. Odaberi tri slučajne invertibilne matrice $M_0, M_1, M_2$ (npr. $2 \times 2$ ili $3 \times 3$ modulo velik prost broj). Za parno $i$ neka je $A_i = M_{s_i}$, za neparno $A_i = M_{s_i}^{-1}$. Ako se interval može isprazniti, tada je $\prod_{i=l}^{r} A_i = I$ (svako brisanje uklanja par $M M^{-1}$ ili $M^{-1} M$). Obrat vrijedi s velikom vjerojatnošću (nekomutativnost matrica sprječava lažna poništavanja).</p>'''),
        ('Redukcija na strukturu podataka', r'''<p>Trebamo umnožak matrica na intervalu i operaciju „svim znakovima na intervalu dodaj $1 \bmod 3$”. Ta operacija ciklički permutira matrice $M_0 \to M_1 \to M_2 \to M_0$; u svakom čvoru segmentnog stabla čuvaj tri umnoška (za pomak $0, 1, 2$) i lijenu oznaku pomaka — ažuriranje je samo rotacija triju vrijednosti.</p>'''),
        ('Složenost', r'''<p>Segmentno stablo s lijenim propagiranjem: $O((n + q) \log n \cdot k^3)$ za matrice dimenzije $k$. Službeno rješenje postavlja i pitanje bi li jednostavnije afine funkcije $x \mapsto ax + b$ (inverz $x \mapsto a^{-1}x - a^{-1}b$) bile dovoljne — oprez, nekomutativnost je ključna.</p>'''),
    ],
    'solution': r'''
<p>Konstruiramo tri slučajne invertibilne matrice $M_0, M_1, M_2$.</p>
<p>Za svaki $i$: ako je $i \bmod 2 = 0$, stavimo $A_i = M_{s_i}$, inače $A_i = M_{s_i}^{-1}$.</p>
<p>Ako se interval može potpuno izbrisati, tada je $\prod_{i=l}^{r} A_i = I$ (svako brisanje para jednakih susjednih znakova uklanja umnožak matrice i njezina inverza). Obratno vrijedi s velikom vjerojatnošću.</p>
<p>Segmentnim stablom održavamo operaciju „dodaj $1$ modulo $3$ na intervalu” i umnožak matrica na intervalu (u čvoru čuvamo umnožak za svaki od tri moguća pomaka). Vremenska složenost je $O(n \log n \cdot k^3)$, gdje je $k$ dimenzija matrica.</p>
<p>Službeno rješenje ostavlja pitanje: bi li umjesto matrica poslužile afine funkcije $ax + b$ i $a^{-1}x - ba^{-1}$? (Primjer $02021210202121$ naveden je kao ilustracija za promišljanje.)</p>
<p><em>Zanimljivost:</em> Flower's Land bio je zadatak na Petrozavodsk Summer 2022: Qingyu, flower and their friends' Contest.</p>
''',
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
        ('Opažanje', r'''<p>CCPC niz sadrži točno jedan znak <code>p</code>, u položaju $2t + 1$ od $3t + 1$. Različiti parovi $(l, r)$ s istom pozicijom <code>p</code> odgovaraju različitim $t$.</p>'''),
        ('Redukcija', r'''<p>Za svaku poziciju $i$ na kojoj može biti <code>p</code> (znak <code>p</code> ili <code>?</code>): lijevo treba $2t$ znakova koji mogu biti <code>c</code> (tj. nisu <code>p</code>), desno $t$. Ako je $d_l$ duljina bloka ne-<code>p</code> znakova lijevo, a $d_r$ desno, valjani su $1 \le t \le \min(\lfloor d_l/2 \rfloor, d_r)$.</p>'''),
        ('Algoritam i složenost', r'''<p>$d_l, d_r$ izračunaj prolazom slijeva i zdesna (ili binarnim pretraživanjem po prefiksnim zbrojevima). Zbroj doprinosa svih $i$; $O(n)$ odnosno $O(n \log n)$.</p>'''),
    ],
    'solution': r'''
<p>Fiksirajmo poziciju $i$ znaka <code>p</code>. Binarnim pretraživanjem (ili izravnim predračunom) odredimo koliko je uzastopnih znakova koji nisu <code>p</code> lijevo ($d_l$) i desno ($d_r$) od $i$. Doprinos pozicije $i$ je $\min\left(\left\lfloor \frac{d_l}{2} \right\rfloor, d_r\right)$.</p>
<p>Vremenska složenost je $O(n \log n)$. Predračunom $d_l, d_r$ može se postići $O(n)$, no to nije potrebno.</p>
''',
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
        ('Opažanje: kad A pobjegne', r'''<p>Ako postoje $i, i+1$ s $\mathrm{dist}_{L_2}(i, i+1) \gt 2$, njihova $L_2$-susjedstva su disjunktna. A krene iz $i$ i u svakom potezu stane na onaj od $i, i+1$ koji nije na B-ovu položaju niti mu je $L_2$-susjedan (uvijek postoji jer B ne može biti susjedan objema). B ga nikad ne dostiže.</p>'''),
        ('Opažanje: kad B lovi', r'''<p>Ako je za svaki $i$ udaljenost $\mathrm{dist}_{L_2}(i, i+1) \le 2$, B jednostavno svaki potez ide jedan korak prema A duž $L_2$. Svaki A-ov potez mijenja njegov položaj na lancu $L_2$ za najviše $2$, pa A ne može „preskočiti” B-a bez da stane na B-a ili njemu susjedan vrh (gdje odmah biva ulovljen); dio lanca koji A ima na raspolaganju stalno se smanjuje i igra završava u konačno mnogo poteza.</p>'''),
        ('Algoritam i složenost', r'''<p>Neka je $\mathrm{pos}[v]$ indeks vrha $v$ u $p$ (inverzna permutacija). Odgovor je <code>Yes</code> ako i samo ako $|\mathrm{pos}[i] - \mathrm{pos}[i+1]| \le 2$ za sve $i$. $O(n)$.</p>'''),
    ],
    'solution': r'''
<p>Razmotrimo nužan i dovoljan uvjet za pobjedu igrača B.</p>
<p>Pretpostavimo da postoje vrhovi $i$ i $i + 1$ čija je udaljenost na lancu $L_2$ veća od $2$. Tada B sigurno ne može pobijediti, jer to znači da su susjedstva vrhova $i$ i $i+1$ na lancu $L_2$ disjunktna. Neka A počne na $i$ i u svakom potezu ode na onaj od vrhova $i, i+1$ koji nije susjedan (na $L_2$) vrhu na kojem se B trenutno nalazi — B nikad ne pobjeđuje.</p>
<p>S druge strane, ako je za svaki par susjednih vrhova $i, i+1$ njihova udaljenost na lancu $L_2$ najviše $2$, B sigurno pobjeđuje: dovoljno je da se u svakom potezu pomakne za jedan korak u smjeru igrača A.</p>
<p>Time smo dobili nužan i dovoljan uvjet: udaljenost na $L_2$ svih parova $(i, i+1)$ mora biti najviše $2$, što jednostavno provjerimo u $O(n)$.</p>
''',
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
        ('Opažanje: struktura ekipa', r'''<p>Ekipa od $2$ je brid, ekipa od $3$ je put $x$–$y$–$z$ u kojem je $y$ u vezi s $x$ i $z$. Bilo koji put ili ciklus s $\ge 2$ vrha može se rastaviti na puteve od $2$ ili $3$ vrha. Stoga: minimizirati izolirane $=$ odabrati podgraf u kojem svaki vrh ima stupanj $\le 2$ i što više vrhova ima stupanj $\ge 1$.</p>'''),
        ('Redukcija na tok minimalnog troška', r'''<p>Bipartitni graf: izvor → dječaci → djevojčice → ponor. Svaki vrh spojen je s izvorom (odn. ponorom) dvama bridovima kapaciteta $1$: prvi s troškom $-M$ ($M$ dovoljno velik), drugi s troškom $1$. Tok minimalnog troška prvo koristi sve $-M$ bridove koje može (svaki pokriven vrh donosi $-M$), a zatim što manje bridova s troškom $1$ — vrh stupnja $2$ odgovara tročlanoj ekipi.</p>'''),
        ('Algoritam', r'''<p>Uobičajeni MCMF s jednom augmentacijom po iteraciji prespor je. Ključno: duljine (troškovi) augmentirajućih puteva mogu biti samo $-2M$ ili $-M + 1$ (put troška $2$ nije isplativ). Zato za svaku razinu troška izračunamo graf najkraćih puteva i na njemu izvedemo višestruku augmentaciju Dinicom — ukupno nekoliko pokretanja maksimalnog toka.</p>'''),
        ('Složenost', r'''<p>$O(m \sqrt{n})$ (Dinic na jediničnim kapacitetima). Postoje i tumačenja bez toka minimalnog troška, no sva se svode na nekoliko problema maksimalnog toka na istom grafu.</p>'''),
    ],
    'solution': r'''
<p>Najprije razmotrimo minimizaciju broja izoliranih vrhova. Uočimo da se svaki ciklus ili put s više od jednog vrha sigurno može rastaviti na puteve s $2$ ili $3$ vrha.</p>
<p>Stoga je za minimizaciju izoliranih vrhova dovoljno pokrenuti tok u kojem svaki vrh ima protok najviše $2$, uz želju da što više vrhova ima protok različit od $0$ — što vodi na tok minimalnog troška. Svaki vrh spojimo s pripadnim izvorom odnosno ponorom dvama bridovima kapaciteta $1$, od kojih jedan ima trošak $-M$ ($M$ dovoljno velik broj); tako će se sigurno prvo augmentirati preko brida s manjim troškom.</p>
<p>Zatim želimo što manje vrhova stupnja $2$. Budući da je vrh stupnja $2$ ekvivalentan putu s $3$ vrha, drugom bridu dajemo trošak $1$.</p>
<p>Budući da tražimo minimalni trošak, prvo će se proći svi bridovi troška $-M$, a zatim što manje bridova troška $1$.</p>
<p>Izravna primjena uobičajenog algoritma za tok minimalnog troška prekoračuje vremensko ograničenje. Uočimo da duljina augmentirajućeg puta može biti samo $-2M$ ili $-M + 1$, pa nakon izračuna grafa najkraćih puteva koristimo Dinic (ili drugi ispravan algoritam za maksimalni tok) s višestrukim augmentacijama. Vremenska složenost je $O(m\sqrt{n})$.</p>
<p>Za ovaj zadatak postoje i neka tumačenja koja se ne temelje na toku minimalnog troška, no sva su na kraju ekvivalentna nekoliko puta rješavanju problema maksimalnog toka na ovom grafu.</p>
''',
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
        ('Opažanje: podniz nasuprot cijelom nizu', r'''<p>Skup $L$ ograničen na $(l, r]$ jednak je za $s[l..r]$ i za $s$. Jedina razlika: u podnizu se pozicija $l$ uvijek briše, dok se u cijelom nizu briše samo ako je početak bloka. Zato je $f(s[l..r])$ upravo $f(s)$ ograničen na pozicije $(l, r]$, tj. na $[l', r]$ gdje je $l'$ prva pozicija strogo iza $l$ koja je preživjela u $f(s)$. Induktivno: $f^k(s[l..r]) = f^k(s) \cap [l_k, r]$, gdje $l_0 = l$, a $l_j$ je prvi preživjeli element $f^j(s)$ strogo iza $l_{j-1}$.</p>'''),
        ('Redukcija: simulacija cijelog niza', r'''<p>Simuliraj $f$ na cijelom nizu $n$ puta: u svakom koraku briše se po jedan znak iz svakog bloka, ukupno najviše $n$ brisanja, pa je simulacija (uz povezanu listu blokova) linearna. Fenwickovo stablo nad originalnim indeksima čuva „živost” i daje rang bilo koje pozicije te broj preživjelih do $r$.</p>'''),
        ('Algoritam: pokazivači kao rangovi', r'''<p>Pokazivač upita čuvaj kao rang među preživjelima. Ako se u koraku brišu elementi rangova $d_1, d_2, \dots$ (u starom nizu), novi rang pokazivača $p$ je $p - \#\{d_t \le p\} + 1$ — to je točno rang prvog preživjelog iza starog $p$. Relativni poredak pokazivača nikad se ne mijenja, pa upite sortiraj po $l$ i drži rangove u segmentnom stablu: za svako brisanje ranga $d$ oduzmi $1$ na sufiksu pokazivača s vrijednošću $\ge d$ (granicu nađi binarnim spustom), a na kraju koraka dodaj $1$ svima.</p>'''),
        ('Odgovor i složenost', r'''<p>Upit $(l, r, k)$ odgovori nakon $k$-tog koraka: $\max(0,\ \mathrm{rang}(\text{najveći preživjeli} \le r) - \mathrm{rang}(l_k) + 1)$. Sve zajedno $O((n + q) \log n)$.</p>'''),
    ],
    'solution': r'''
<p>Uočimo odnos između upita na intervalu i operacije nad cijelim nizom: razlikuju se zapravo samo u jednoj, možda izbrisanoj, prvoj poziciji. Kad operaciju izvodimo nad cijelim nizom, pozicija $l$ koja bi se u podnizu izbrisala možda se ne izbriše.</p>
<p>Dok simuliramo $n$ operacija nad cijelim nizom, za svaki upit istodobno održavamo gdje se trenutno nalazi njegova prva pozicija (početno $l_i$). Kad nad cijelim nizom izvedemo jednu operaciju, $l_i$ se mijenja tako da: ako je ta pozicija u operaciji nad cijelim nizom već izbrisana, pomaknemo se za jedno mjesto udesno; inače je trebala biti izbrisana (kao prvi znak podniza), pa se svejedno pomaknemo za jedno mjesto udesno.</p>
<p>Oznake pozicija su dinamičke, pa ih treba dinamički održavati. Oznake izvornog niza lako se održavaju Fenwickovim stablom.</p>
<p>No $l_i$ upita zapravo označava „koji po redu” među trenutno preostalim znakovima. Kad brišemo, svim oznakama većim od određene vrijednosti treba oduzeti $1$. Uočimo da se relativni poredak oznaka od početka do kraja ne mijenja, pa nakon sortiranja to održavamo segmentnim stablom.</p>
<p>Za konačni odgovor dovoljno je od trenutne oznake još preostalog prethodnika pozicije $r_i$ oduzeti održavanu oznaku trenutne prve pozicije $l_i$ (uvećano za jedan, uz odgovor $0$ ako je razlika negativna).</p>
''',
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
        ('Opažanje: bitovi koje XOR dotiče', r'''<p>Neka je $m$ najmanji broj takav da $2^m \gt K$. Svaki $t \le K$ ima nule iznad bita $m-1$, pa $\oplus$ mijenja samo najnižih $m$ bitova. Grupiraj brojeve po $g(x) = \lfloor x / 2^m \rfloor$; $\oplus$ nikad ne mijenja grupu.</p>'''),
        ('Unutar iste grupe', r'''<p>Ako je $x = y$: $0$ koraka. Ako je $x \oplus y \le K$ ili $|x - y| \le 1$: $1$ korak. Inače $2$ koraka: $d = x \oplus y \lt 2^m$ i $d \gt K \ge 2^{m-1}$, pa $d$ ima bit $m-1$; $t_1 = 2^{m-1} \le K$ i $t_2 = d \oplus 2^{m-1} \lt 2^{m-1} \le K$ daju $y = x \oplus t_1 \oplus t_2$.</p>'''),
        ('Između grupa', r'''<p>Ako je $g(X) \lt g(Y)$, nužno prelazimo grupe operacijom $+1$ iz broja čijih je donjih $m$ bitova sve jedinice (inače ostajemo u grupi). Dakle: donje bitove postavi na $2^m - 1$ (cijena kao „unutar grupe”: $0$, $1$ ili $2$), pa $+1$. Za svaku međugrupu krećemo od donjih bitova $0$: ako je $K = 2^m - 1$, jedan $\oplus$ pa $+1$ — ukupno $2$ po grupi; inače $3$. Na kraju u grupi $g(Y)$ iz donjih bitova $0$ do $Y$ opet po pravilu „unutar grupe”. Slučaj $g(X) \gt g(Y)$ simetričan je (donje bitove spusti na $0$, pa $-1$).</p>'''),
        ('Složenost', r'''<p>Broj grupa koje treba prijeći može biti do $2^{60}$, pa se broj koraka računa aritmetički: $O(1)$ (ili $O(\log K)$) po testu; pazi na prekoračenje kod $K = 0$ ($m = 0$) i na 64-bitne tipove.</p>'''),
    ],
    'solution': r'''
<p>Dan je broj $x$ s operacijama $+1$, $-1$ i $\oplus$ s brojem koji ne prelazi $K$; tražimo najmanji broj koraka da postane $y$.</p>
<p>Promotrimo najmanji $m$ za koji vrijedi $2^m \gt K$: operacija $\oplus$ može promijeniti samo najnižih $m$ binarnih znamenki. Stoga sve brojeve grupiramo prema $\lfloor i / 2^m \rfloor$.</p>
<p>Za dva broja u istoj grupi: ako su jednaki, treba $0$ koraka; ako je njihov $\oplus$ najviše $K$ ili se razlikuju za najviše $1$, treba $1$ korak; inače trebaju $2$ koraka.</p>
<p>Za brojeve u različitim grupama nužno je najprije donjih $m$ bitova pretvoriti u $m$ jedinica, zatim dodati $1$ da se prijeđe u sljedeću grupu, i tako sve dok ne dođemo u istu grupu.</p>
<p>Za svaku grupu koju prelazimo trebaju $2$ koraka ako je $K = 2^m - 1$, a inače $3$ koraka.</p>
''',
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
        ('Opažanje: bitni su samo minimumi', r'''<p>„Poništi” u $a$ i $b$ veći element svakog stupca. Ako se nakon toga $a$ i $b$ podudaraju (isti minimum, isti redak, u svakom stupcu), uvijek postoji slijed zamjena koji izjednačava i izvorne nizove: možemo postići da stupac s $k$-tim najmanjim minimumom drži $k$-ti najmanji maksimum (tada svaki maksimum ostaje veći od minimuma u svom stupcu i zamjene su dopuštene), pa slobodno permutiramo maksimume. Time se zadatak svodi na izjednačavanje minimuma po stupcima.</p>'''),
        ('Očite nemogućnosti', r'''<p>Minimum stupca samo se smanjuje: ako je u nekom stupcu minimum od $a$ manji od minimuma od $b$ — nema rješenja. Ako su minimumi jednaki, ali u različitim recima — nema rješenja (element koji je minimum nikad se ne pomiče). Ako su u istom stupcu minimumi $m$ (u $a$) i $m' \lt m$ (u $b$) u istom retku: nova vrijednost stiže u redak <em>maksimuma</em>, pa je potreban „posredni” element $x$ s $m' \lt x \lt m$ iz stupca u kojem se minimumi od $a$ i $b$ još ne podudaraju; ako je $m' = m - 1$ ili takvog $x$ nema — nema rješenja.</p>'''),
        ('Konstrukcija i broj koraka', r'''<p>Ponavljaj: među nepodudarnim stupcima odaberi onaj s najmanjim ciljnim $m'$ i njegov $m'$ dovedi na mjesto izravno jednom zamjenom ili preko posrednog elementa dvjema zamjenama. Induktivno se pokazuje da se taj postupak može provoditi dok se svi minimumi ne podudare. Ukupno najviše $4n$ zamjena, unutar dopuštenih $5n$. Složenost $O(n^2)$ po testu uz $\sum n^2 \le 4 \cdot 10^6$.</p>'''),
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
        ('Opažanje 1: parnost i prosti brojevi', r'''<p>Treba točno $\frac{n+k}{2}$ jedinica, pa mora biti $n \equiv k \pmod 2$ (inače $-1$). Potpuno multiplikativna funkcija određena je vrijednostima na prostim brojevima.</p>'''),
        ('Opažanje 2: neovisnost velikih prostih brojeva', r'''<p>Kad su vrijednosti na prostim $p \le \sqrt{n}$ fiksirane, doprinos svakog prostog $p \gt \sqrt{n}$ neovisan je: u $[1, n]$ višekratnici od $p$ su $jp$ za $j \le n/p \lt \sqrt{n}$, a $f(jp) = f(j) f(p)$ s $f(j)$ već određenim. Doprinos je $f(p) \cdot \sum_{j \le n/p} f(j)$.</p>'''),
        ('Algoritam za $n \ge 200$', r'''<p>Stavi $f(p) = 1$ za sve $p \le \sqrt{n}$; tada je $f(j) = 1$ za sve $j \lt \sqrt{n}$ i svaki veliki prosti $p$ s $f(p) = -1$ smanjuje zbroj za $2 \lfloor n/p \rfloor$. Treba postići ukupno smanjenje $n - k$: ruksak nad vrijednostima $\lfloor n/p \rfloor$, koji zbog raspodjele prostih brojeva rješava greedy (od većih vrijednosti prema manjima; vrijednost $1$ ima mnogo prostih brojeva, što popunjava ostatak).</p>'''),
        ('Mali $n$ i složenost', r'''<p>Za $n \le 200$ postavljanje svih malih prostih brojeva na $1$ može dati previše jedinica (brojevi sastavljeni od malih prostih faktora čine više od polovice), pa se vrijednosti malih prostih brojeva odrede pretraživanjem ili nasumičnim pokušajima i predračunaju za sve $(n, k)$. Ukupno $O(n \log \log n)$ po testu (sito), uz $\sum n \le 2 \cdot 10^6$. Postoje i pristupi bez posebnog slučaja, koji podešavaju vrijednosti od malih prema velikim prostim brojevima, ali njihova ispravnost nije očita.</p>'''),
    ],
    'solution': r'''
<p>Uvjet je ekvivalentan tome da točno $\frac{n + k}{2}$ vrijednosti $f(i)$ bude jednako $1$.</p>
<p>Multiplikativna funkcija određena je vrijednostima na svim prostim brojevima. Kad odredimo vrijednosti na prostim brojevima do $\sqrt{n}$, doprinosi preostalih prostih brojeva odgovoru međusobno su neovisni.</p>
<p>Za $n \ge 200$ možemo sve proste brojeve do $\sqrt{n}$ postaviti na $1$; za preostale proste brojeve dobivamo problem ruksaka koji se, zbog svojstava raspodjele prostih brojeva, može riješiti greedy pristupom.</p>
<p>Za $n \le 200$ postavljanje svih prostih brojeva do $\sqrt{n}$ na $1$ može dovesti do toga da broj jedinica premaši polovicu; tada se vrijednosti malih prostih brojeva mogu odrediti pretraživanjem, randomizacijom i sličnim metodama, a odgovori se predračunaju.</p>
<p>Za ovaj zadatak postoje i pristupi bez posebnih slučajeva koji izravno podešavaju vrijednosti od malih prema velikim prostim brojevima, no njihova ispravnost nije nužno očita.</p>
''',
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
        ('Opažanje 1: doprinos pojedinog broja', r'''<p>Traženi zbroj je $(n-1)!$ puta očekivani rezultat za slučajni redoslijed izvršavanja operatora. Po linearnosti gledamo svaki $a_i$ zasebno: predznak od $a_i$ mijenja se kad god se izvrši operator $-$ koji u tom trenutku ima $a_i$ u desnom operandu.</p>'''),
        ('Opažanje 2: sufiksni rekordi', r'''<p>Operator $\mathrm{op}_j$ ($j \lt i$) ima $a_i$ u desnom operandu ako i samo ako se izvršava nakon svih operatora $\mathrm{op}_{j+1}, \dots, \mathrm{op}_{i-1}$, tj. njegov je trenutak izvršavanja najveći među $\mathrm{op}_j, \dots, \mathrm{op}_{i-1}$. Ako su rekordi na pozicijama $p_1 \lt p_2 \lt \dots \lt p_k = i - 1$, vjerojatnost je umnožak recipročnih duljina odgovarajućih sufiksa; događaji za različite $j$ su neovisni s vjerojatnošću $\frac{1}{i-j}$.</p>'''),
        ('Redukcija na formulu', r'''<p>Uz $\mathrm{sgn}_j = \pm 1$ za $+$/$-$, očekivani predznak od $a_i$ je $\prod_{j=1}^{i-1} \left( 1 - \frac{1}{i-j} + \frac{\mathrm{sgn}_j}{i-j} \right) = \frac{\mathrm{sgn}_{i-1}}{(i-1)!} \prod_{j=1}^{i-2} (\mathrm{sgn}_j + i - j - 1)$. Odgovor je $(n-1)! \left( a_1 + \sum_{i=2}^{n} \frac{a_i\, \mathrm{sgn}_{i-1}}{(i-1)!} \prod_{j=1}^{i-2} (\mathrm{sgn}_j + i - j - 1) \right)$. Provjera na $9-1+4-1$: predznaci $1, -1, 0, -\frac{1}{3}$, pa $6 \cdot (9 - 1 - \frac{1}{3}) = 46$.</p>'''),
        ('Algoritam: kako izračunati umnoške', r'''<p>Umnožak $\prod_{j=1}^{i-2}(i - c_j)$ s $c_j = j + 1 - \mathrm{sgn}_j$ za sve $i$. Tri puta: (1) <em>Four Russians</em> — podijeli $j$ u blokove duljine $B$, za svaki blok predračunaj sve mogućnosti; $O(n^2/B + \frac{n}{B} 2^B)$ uz pažljivu implementaciju. (2) <em>Diskretni logaritam</em>: umnožak postaje zbroj $\sum_j \log(i - c_j)$ — konvolucija; nulu i negativne vrijednosti obradi zasebno (faktor $0$ nulira umnožak). (3) <em>Polinomi</em>: $P(i) = P(x) \bmod (x - i)$, pa se zadatak svodi na umnožak polinoma $\prod (x - c_j)$ uz „evaluiraj pa pomnoži novim faktorom”, što rješava razdvoji-pa-vladaj FFT.</p>'''),
        ('Složenost', r'''<p>Pristup (2): $O(n \cdot T_{\log} + n \log n)$; pristup (3): razdvoji-pa-vladaj FFT (uobičajeno $O(n \log^2 n)$). Uz $n \le 2 \cdot 10^5$ i limit od $5$ s sva tri prolaze.</p>'''),
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
},
]
