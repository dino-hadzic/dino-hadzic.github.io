# -*- coding: utf-8 -*-
STAGE = {
    'no': 15,
    'name': 'Stage 15: Hangzhou',
    'source_name': 'The 20th Zhejiang Provincial Collegiate Programming Contest, 2023',
    'source_html': r'''
<p>Zadatke i rješenja pripremilo je Sveučilište Zhejiang. Prijevod službenog rješenja: <a href="https://contest.ucup.ac/download.php?type=attachments&amp;id=1221&amp;r=1">Tutorial (en)</a>. Tekst zadatka preveden je prema službenim <a href="https://contest.ucup.ac/download.php?type=attachments&amp;id=1221&amp;r=0">engleskim tekstovima zadataka</a>. Zadatak je dostupan na <a href="https://contest.ucup.ac/contest/1221">Universal Cup Judging System</a>.</p>
''',
}

PROBLEMS = [
# ---------------------------------------------------------------- A
{
    'letter': 'A', 'title': 'Turn on the Light', 'title_hr': 'Upali svjetlo', 'slug': 'A_turn_on_the_light',
    'tl': '2 s', 'ml': '1024 MB',
    'statement': r'''
<p><em>Interaktivni zadatak.</em> Postoji $n$ svjetala $1..n$, sva ugašena; jedno skriveno je omiljeno. Upit „<code>? x</code>” upali svjetlo $x$ (ako je ugašeno; gašenje nije moguće) i vraća $|$broj upaljenih lijevo od omiljenog $-$ broj upaljenih desno$|$. Nađi omiljeno svjetlo s najviše $40$ upita. Interaktor je adaptivan.</p>
<h3>Ulaz</h3>
<p>$n$ ($1 \le n \le 10^6$).</p>
<h3>Izlaz</h3>
<p>Upiti „<code>? x</code>”, na kraju „<code>! x</code>”.</p>
''',
    'hints': [
        r'''<p>$\log_2 10^6 \approx 20$, a imaš $40$ upita — dakle otprilike dva upita po koraku binarnog pretraživanja. Održavaj interval $[l, r]$ te brojeve upaljenih svjetala lijevo ($c_l$) i desno ($c_r$) od intervala.</p>''',
        r'''<p>Ako je $c_l \ne c_r$, paljenje sredine $m$ i odgovor odmah kažu je li omiljeno svjetlo lijevo ili desno od $m$ (ili je to $m$). Ako je $c_l = c_r$, odgovor bi bio $1$ u oba slučaja — najprije potroši jedan upit na rub intervala da razbiješ simetriju.</p>''',
    ],
    'coach': [
        ('Opažanje', r'''<p>Nakon upita $x$ odgovor je $|\,(\text{upaljeni lijevo od } f) - (\text{upaljeni desno od } f)\,|$. Za trenutni interval kandidata $[l, r]$ sva upaljena svjetla su izvan njega ($c_l$ lijevo, $c_r$ desno) osim onih koje sad palimo unutar intervala.</p>'''),
        ('Redukcija', r'''<p>Neka je $m = \lfloor (l + r) / 2 \rfloor$. Ako je $c_l \ne c_r$, nakon paljenja $m$ odgovor je $|c_l + 1 - c_r|$ ako je $f > m$, $|c_l - c_r - 1|$ ako je $f < m$, a $|c_l - c_r|$ ako je $f = m$ — tri različite vrijednosti, pa znamo u koju polovicu ići. Ako je $c_l = c_r$, upali najprije svjetlo $r$: odgovor $0$ znači $f = r$, inače je $f \in [l, r-1]$ i sada je $c_r$ za jedan veći od $c_l$, pa se sljedeći korak ponaša kao u prvom slučaju.</p>'''),
        ('Algoritam i složenost', r'''<p>Binarno pretraživanje s najviše dva upita po koraku: oko $2 \log_2 n \le 40$ upita. Adaptivnost interaktora ne smeta jer svaki odgovor deterministički sužava skup kandidata.</p>'''),
    ],
    'solution': r'''
<p>Razmotrimo binarno pretraživanje. Neka je trenutni interval $[l, r]$, $c_l$ broj upaljenih svjetala u $[1, l-1]$, a $c_r$ broj upaljenih u $[r+1, n]$.</p>
<p>Neka je $m = \lfloor (l+r)/2 \rfloor$. Nakon paljenja svjetla $m$, ako je $c_l \ne c_r$, možemo odrediti s koje je strane od $m$ skriveno svjetlo — $[l, m-1]$ ili $[m+1, r]$ — i rekurzivno nastaviti.</p>
<p>Dakle upit na $r$ trebamo samo kad je $c_l = c_r$; tada saznajemo je li skriveno svjetlo $r$ ili je u $[l, r-1]$, i rekurzivno nastavljamo.</p>
<p>Broj upita je približno $2\log_2 n$.</p>
''',
},
# ---------------------------------------------------------------- B
{
    'letter': 'B', 'title': 'Equation Discovering', 'title_hr': 'Otkrivanje jednadžbe', 'slug': 'B_equation_discovering',
    'tl': '2 s', 'ml': '1024 MB',
    'statement': r'''
<p>Dano je $n$ parova $(x, y)$. Pronađi izraz $f(x)$ generiran gramatikom $S \to S+S \mid S-S \mid S\times S \mid S\div S \mid \sin(S) \mid \cos(S) \mid (S) \mid x$ čija je <em>složenost</em> (dvostruki broj binarnih operatora plus broj unarnih) najviše $9$, takav da za svaki par vrijedi $|f(x) - y| / \max(1, |y|) \le 10^{-3}$, a pri dijeljenju je $|$djelitelj$| \ge 0.01$ (za službeno rješenje jamči se $\ge 0.02$).</p>
<h3>Ulaz</h3>
<p>$n$ ($1 \le n \le 20$) i $n$ parova realnih brojeva sa $6$ decimala, $|x|, |y| < 10^3$.</p>
<h3>Izlaz</h3>
<p>Bilo koji valjani izraz (najviše $1000$ znakova), npr. <code>x*x</code> ili <code>sin(x)/(x*x)</code>.</p>
''',
    'hints': [
        r'''<p>Složenost $\le 9$ znači stablo izraza s najviše $10$ čvorova. Iscrpno pretraživanje po prefiksnom zapisu sa $7$ simbola daje $7^{10} \approx 3 \cdot 10^8$ kandidata — previše. Ali koliko je valjanih stabala zapravo?</p>''',
        r'''<p>Gradi izraze odozdo prema gore po složenosti: $f_i$ = skup izraza složenosti $i$; unarni operator vodi $f_i \to f_{i+1}$, binarni $f_i, f_j \to f_{i+j+2}$. Ukupno ih je manje od $4 \cdot 10^5$ — evaluiraj svaki na svih $n$ točaka.</p>''',
    ],
    'coach': [
        ('Opažanje', r'''<p>Zapiši izraz kao stablo. Složenost $\le 9$ znači najviše $10$ čvorova (list $x$ ima složenost $0$, unarni čvor dodaje $1$, binarni $2$). Zagrade su samo zapis, ne dio stabla.</p>'''),
        ('Redukcija', r'''<p>Broj sintaktički valjanih stabala puno je manji od $7^{10}$; DP po složenosti pokazuje da ih je najviše oko $4 \cdot 10^5$ (tretirajući izraze kao različite objekte, uz očite duplikate). Toliko izraza možemo izravno nabrojati i provjeriti.</p>'''),
        ('Algoritam', r'''<p>Neka je $f_i$ lista izraza složenosti točno $i$ (svaki pamti tekst i vektor vrijednosti na $n$ ulaznih točaka). $f_0 = \{x\}$. Za $i = 1..9$: iz svakog $e \in f_{i-1}$ dodaj $\sin(e), \cos(e)$; za sve $j + k + 2 = i$ i $e_1 \in f_j$, $e_2 \in f_k$ dodaj $e_1 \circ e_2$ za $\circ \in \{+, -, \times, \div\}$ (dijeljenje samo ako je $|e_2(x)| \ge 0.02$ na svim točkama). Vrijednosti računaj inkrementalno; ispisuj s potpunim zagradama oko podizraza. Prvi izraz koji zadovolji toleranciju $10^{-3}$ na svim točkama je odgovor.</p>'''),
        ('Složenost', r'''<p>$\Theta(n \cdot T(9))$, gdje je $T(9)$ broj izraza složenosti $\le 9$. Jedno testersko rješenje ima svega $830$ bajtova.</p>'''),
    ],
    'solution': r'''
<p>Zapišimo konačni odgovor u obliku stabla izraza. Složenost najviše $9$ znači da stablo ima najviše $10$ čvorova.</p>
<p>Gruba analiza: promotrimo prefiksni obilazak stabla; svaki element može biti jedan od $7$ simbola, pa postoji do $7^{10} \approx 3 \cdot 10^8$ mogućih stabala. U stvarnosti ih je puno manje: DP-om se izračuna da valjanih stabala izraza nema više od $4 \cdot 10^5$, pa ih možemo izravno nabrojati.</p>
<p>Metoda izgradnje stabla odozdo prema gore: neka je $f_i$ skup izraza složenosti $i$; prijelazi su iz $f_i$ u $f_{i+1}$ (unarni operator) te iz $f_i, f_j$ u $f_{i+j+2}$ (binarni operator). Ta je metoda relativno laka za implementaciju; jedan je tester priložio kôd od samo $830$ bajtova.</p>
<p>Ako je $T(x)$ broj izraza složenosti najviše $x$, vremenska složenost je $\Theta(n\,T(9))$.</p>
''',
},
# ---------------------------------------------------------------- C
{
    'letter': 'C', 'title': 'Puzzle: Kusabi', 'title_hr': 'Slagalica: Kusabi', 'slug': 'C_puzzle_kusabi',
    'tl': '1 s', 'ml': '1024 MB',
    'statement': r'''
<p>Dano je korijensko stablo s korijenom $1$ (neoznačen). Označeni vrhovi nose „Chang” (dulji), „Duan” (kraći) ili „Tong” (jednako). Treba sve označene vrhove spariti tako da: put između sparenih vrhova označi sve svoje bridove, svaki brid označen je najviše jednom; „Chang” vrh mora biti dublji od svog para, „Duan” plići, „Tong” jednako dubok.</p>
<h3>Ulaz</h3>
<p>$n$ ($1 \le n \le 10^5$), zatim za $i = 2..n$: $p_i$ ($p_i < i$) i tip $t_i \in \{$Chang, Duan, Tong, -$\}$.</p>
<h3>Izlaz</h3>
<p><code>NO</code> ili <code>YES</code> i parovi.</p>
''',
    'hints': [
        r'''<p>Bridovi se ne smiju dijeliti, pa iz podstabla svakog vrha prema roditelju može „izaći” najviše jedan nespareni vrh. Hoće li nešto izaći određeno je parnošću broja označenih vrhova u podstablu.</p>''',
        r'''<p>Obrađuj vrhove od listova prema korijenu. U svakom vrhu spari što više parova unutar podstabla: „Tong” s „Tong” iste dubine; „Chang” s „Duan” pri čemu Chang mora biti dublji. Ako više od jednog vrha ostane nespareno — <code>NO</code>. Koje ostaviti? Za Chang višak zadrži najdublji, za Duan višak najplići (najlakše ih je kasnije spariti).</p>''',
    ],
    'coach': [
        ('Opažanje', r'''<p>Ako je broj označenih vrhova u podstablu vrha $v$ paran, nijedan put ne smije prijeći brid $(v, p_v)$ (inače bi neparan broj krajeva ostao u podstablu, a brid se koristi najviše jednom). Ako je neparan, točno jedan vrh iz podstabla sparuje se izvan njega. Ukupan neparan broj označenih vrhova odmah znači <code>NO</code>.</p>'''),
        ('Redukcija: pohlepno od listova', r'''<p>U vrhu $v$ skupljamo nesparene vrhove iz svih djece (najviše jedan po djetetu) plus $v$ sam. Sparivanja: Tong–Tong zahtijevaju istu dubinu (grupiraj po dubini — svaka grupa mora imati paran broj, inače najviše jedan ostaje). Chang–Duan: Chang dublji od Duana. Zbog uvjeta „najviše jedan izlazi”, ako su broj Changova i Duanova različiti za više od $1$ (nakon što se Tong grupe riješe), odgovor je <code>NO</code>.</p>'''),
        ('Algoritam: koga zadržati', r'''<p>Ako Changova ima više nego Duanova, pokušaj zadržati (poslati gore) <em>najdublji</em> Chang koji se može zadržati tako da ostatak ima savršeno sparivanje — dubok Chang lako nalazi plići Duan gore; ako Duanova ima više, zadrži <em>najplići</em> Duan. Sparivanje Chang–Duan provjeri pohlepno: sortiraj, svakom Duanu dubine $d$ daj Chang dubine $> d$. Struktura s multiskupovima (<code>std::multiset</code>) po tipu i dubini; spajanje manjeg u veći.</p>'''),
        ('Složenost', r'''<p>$\Theta(n \log n)$.</p>'''),
    ],
    'solution': r'''
<p>Podstablo svakog vrha može prema korijenu proslijediti najviše jedan put, a hoće li se put proslijediti ovisi samo o parnosti broja ključnih vrhova u podstablu. Zato se može primijeniti pohlepan pristup, obrađujući vrhove redom od listova prema korijenu.</p>
<p>Za vrhove tipa C (Tong) svaku dubinu obrađuj zasebno. Ako u podstablu ima više vrhova tipa A (Chang) nego tipa B (Duan), pokušaj zadržati najdublji A vrh koji se može zadržati; ako ima više B nego A, pokušaj zadržati najplići B vrh koji se može zadržati.</p>
<p>Ako se pokaže da broj vrhova koje treba zadržati prelazi jedan ili da sparivanje A i B ne uspije, zadatak nema rješenja. Rješenja nema ni kad je ukupan broj posebnih vrhova neparan.</p>
<p>Vremenska složenost: $\Theta(n \log n)$.</p>
''',
},
# ---------------------------------------------------------------- D
{
    'letter': 'D', 'title': 'Master of Both III', 'title_hr': 'Majstor obojega III', 'slug': 'D_master_of_both_iii',
    'tl': '2 s', 'ml': '1024 MB',
    'statement': r'''
<p>Dan je $n$ i težine $w_0, \dots, w_{n-1}$. Za multiskup $S \subseteq \{0..n-1\}$, operacija: odaberi $T \subseteq S$ i $y$, zamijeni $T$ s $\{(x + y) \bmod n : x \in T\}$ uz cijenu $w_y$. $f(S)$ je najmanja ukupna cijena da svi elementi postanu $0$. Izračunaj $\sum_{\emptyset \ne S} f(S) \cdot \sum_{v \in S} 2^v \pmod{998244353}$ po svim nepraznim skupovima $S$ (bez duplikata).</p>
<h3>Ulaz</h3>
<p>$n$ ($1 \le n \le 22$) i $w_0..w_{n-1}$ ($1 \le w_i \le 10^9$).</p>
<h3>Izlaz</h3>
<p>Traženi zbroj.</p>
<h3>Primjer</h3>
<p>$n = 3$, $w = (2, 1, 2)$: odgovor $45$.</p>
''',
    'hints': [
        r'''<p>Obrnuti smjer: element $x$ dovodimo u $0$ pomacima čiji je zbroj $\equiv -x \pmod n$. Ako kupimo skup pomaka $Y$ (svaki plaćen jednom, jer se isti pomak može primijeniti na bilo koji podskup), možemo poništiti sve $x$ koji su zbrojevi (s ponavljanjem) elemenata iz $Y$.</p>''',
        r'''<p>Neka je $g_S$ najmanja cijena skupa pomaka koji generira sve elemente skupa $S$ (kao podskup-suma s ponavljanjem, modulo $n$). Onda je $f(S) = \min_{S \subseteq S'} g_{S'}$: minimum po nadskupovima (SOS-DP).</p>''',
    ],
    'coach': [
        ('Opažanje', r'''<p>Redoslijed operacija nije bitan: element $x$ postaje $0$ ako je zbroj primijenjenih pomaka $\equiv -x$. Isti pomak $y$ kupljen jednom (cijena $w_y$) može se primijeniti na proizvoljan podskup, a ponovna primjena istog $y$ na isti element košta ponovno — ali kako biramo $T$ slobodno, svaki $y$ plaćamo najviše onoliko puta koliko ga najviše puta koristi jedan element. Zadatak se svodi na: odaberi multiskup pomaka $Y$ minimalne cijene tako da je svaki $-x$ ($x \in S$) zbroj nekog podmultiskupa od $Y$.</p>'''),
        ('Redukcija', r'''<p>Neka je $g_S$ najmanja cijena multiskupa pomaka čiji skup podmultiskup-zbrojeva (mod $n$) sadrži $S$ — ekvivalentno, minimalna cijena da se točno skup $S$ svih „dostižnih” ostataka generira. Prijelaz: dodavanjem pomaka $y$ skupu dostižnih ostataka $S$ dobivamo $S \cup \operatorname{rot}_y(S)$, gdje je $\operatorname{rot}_y$ ciklički pomak bitmaske za $y$ — $O(1)$ bitovnim operacijama na maski od $n$ bitova. To je DP po ruksaku nad skupovima: $g_{S \cup \operatorname{rot}_y(S)} \gets \min(g_{S \cup \operatorname{rot}_y(S)}, g_S + w_y)$.</p>'''),
        ('Algoritam i složenost', r'''<p>Nakon što izračunamo $g$ za sve maske ($n 2^n$ prijelaza), $f(S) = \min_{S' \supseteq S} g_{S'}$ — minimum po nadskupovima računamo SOS-DP-om u $O(n 2^n)$. Odgovor je $\sum_S f(S) \cdot \text{mask}(S) \bmod 998244353$. Ukupno $\Theta(n 2^n) \approx 9 \cdot 10^7$.</p>'''),
    ],
    'solution': r'''
<p>Najprije zadatak preoblikujemo u odabir skupa $S$ (pomaka) koji može generirati sve brojeve skupa $T$, uz minimizaciju zbroja cijena $\sum_{x \in S} w_x$.</p>
<p>Neka je $f_S$ najmanja cijena generiranja svih brojeva iz skupa $S$. Bitovnim operacijama učinkovito prenosimo stanje dodavanjem $x$ u ruksak skupa $S$.</p>
<p>Zatim za svaki $S$ nađemo minimum po nadskupovima, što daje odgovor za skup $S$.</p>
<p>Vremenska složenost: $\Theta(n 2^n)$.</p>
''',
},
# ---------------------------------------------------------------- E
{
    'letter': 'E', 'title': 'Puzzle: Tapa', 'title_hr': 'Slagalica: Tapa', 'slug': 'E_puzzle_tapa',
    'tl': '1 s', 'ml': '1024 MB',
    'statement': r'''
<p>Mreža $(2n-1) \times (2m-1)$ ima $n \times m$ tragova na ćelijama s oba neparna indeksa. Svaki trag je broj jednak broju susjednih ćelija (8 uključivo dijagonalno) ili za jedan manji: u kutu $2$ ili $3$, na rubu $4$ ili $5$, u sredini $7$ ili $8$. Zasjeni neke ćelije tako da su sve ćelije s tragom nezasjenjene i da je oko svakog traga točno toliko <em>uzastopnih</em> zasjenjenih ćelija (u kružnom redoslijedu).</p>
<h3>Ulaz</h3>
<p>$n, m$ ($2 \le n, m \le 50$) i mreža.</p>
<h3>Izlaz</h3>
<p><code>NO</code> ili <code>YES</code> i mreža s <code>#</code> za zasjenjene ćelije.</p>
''',
    'hints': [
        r'''<p>Trag s punim brojem ima sve susjede zasjenjene; trag s brojem za jedan manjim ima točno jednu praznu susjednu ćeliju. Svaka ćelija bez traga susjedna je s $1$, $2$ ili $4$ traga (na rubu/između/dijagonalno).</p>''',
        r'''<p>Prazna ćelija između dva „umanjena” traga zadovoljava oba: sparuj umanjene tragove! Ćelija dijagonalno susjedna četvorici tragova može poslužiti kao par dvaju parova. Gradi bipartitni graf sparivanja — ali pazi: uvjet <em>uzastopnosti</em> zabranjuje neka sparivanja (rubni trag s unutarnjim $7$).</p>''',
    ],
    'coach': [
        ('Opažanje', r'''<p>Oko svakog traga najviše je jedna prazna ćelija. Ako je prazna ćelija dijagonalno susjedna četvorici tragova, dijele je dva para tragova. Dakle problem je: umanjene tragove spariti tako da svaki par dijeli zajedničku praznu ćeliju, a svaka prazna ćelija poslužuje najviše jedan par (ili dva para ako je „dijagonalna” ćelija).</p>'''),
        ('Redukcija: koja su sparivanja dopuštena', r'''<p>Zasjenjene ćelije oko traga moraju biti uzastopne. Prazna ćelija na <em>stranici</em> između dva susjedna traga (ista redak/stupac) rasporeda kod oba ostavlja povezan luk — dopušteno, i za rubne i za unutarnje tragove. Rubni (vanjski) trag ne može se spariti sa središnjom $7$ preko dijagonalne ćelije jer bi zasjenjene ćelije oko nekog od njih postale nepovezane; dvije središnje $7$ mogu se spariti dijagonalno. Parni rubni tragovi mogu se sparivati s drugim rubnim (parnim) tragovima.</p>'''),
        ('Algoritam', r'''<p>Umanjeni tragovi čine vrhove; brid između dvaju tragova ako postoji dopuštena zajednička prazna ćelija. Mreža tragova je bipartitna (šahovsko bojenje po $(i + j)/2$), pa je to bipartitno sparivanje; dijagonalne ćelije mogu poslužiti dvama parovima ($(i,j)$–$(i+2,j+2)$ i $(i,j+2)$–$(i+2,j)$), što ne stvara sukob. Ako savršeno sparivanje umanjenih tragova ne postoji — <code>NO</code>; inače zasjeni sve ćelije bez traga osim odabranih praznih.</p>'''),
        ('Složenost', r'''<p>$\Theta((nm)^2)$ Kuhnovim algoritmom ili $\Theta((nm)^{1.5})$ Hopcroft–Karpom.</p>'''),
    ],
    'solution': r'''
<p>Svaki trag može imati najviše jednu praznu susjednu ćeliju. Ako je prazna ćelija dijagonalno susjedna s četiri traga, mogu je dijeliti dva para tragova. Stoga se možemo usredotočiti na sparivanje tragova u parove.</p>
<p>Parni tragovi uz rub mogu se spariti s drugim parnim tragovima. Vanjski rubni tragovi i središnja $7$ ne mogu se spariti, jer tada zasjenjene ćelije oko tragova ne bi činile povezano područje. Međutim, dvije središnje $7$ mogu se spariti.</p>
<p>Riješi bipartitno sparivanje bilo kojim algoritmom, npr. Kuhnovim (mađarskim) ili Hopcroft–Karpovim.</p>
<p>Vremenska složenost: $\Theta((nm)^2)$ ili $\Theta((nm)^{1.5})$, ovisno o algoritmu.</p>
''',
},
# ---------------------------------------------------------------- F
{
    'letter': 'F', 'title': 'Classic: Classical Problem', 'title_hr': 'Klasika: klasičan zadatak', 'slug': 'F_classic_classical_problem',
    'tl': '5 s', 'ml': '1024 MB',
    'statement': r'''
<p>Dan je skup $S$ od $n$ različitih brojeva iz $[0, p)$ i prost $p$. Nađi sve $c \in [0, p)$ za koje je $\operatorname{mex}(S_c)$ najveći, gdje je $S_c = \{(c \cdot x) \bmod p : x \in S\}$.</p>
<h3>Ulaz</h3>
<p>$T$ testova; u svakom $n, p$ ($1 \le n \le p \le 2 \cdot 10^5$) i elementi. $\sum p \le 2 \cdot 10^5$.</p>
<h3>Izlaz</h3>
<p>Broj takvih $c$ i maksimalni mex, zatim svi $c$ rastuće.</p>
<h3>Primjer</h3>
<p>$S = \{2, 3, 4\}$, $p = 5$: $c = 0$ daje mex $1$ (jedini maksimum) — ispis <code>1 1</code> / <code>0</code>.</p>
''',
    'hints': [
        r'''<p>Ako $0 \notin S$, mex je barem $1$ samo za $c = 0$ (tada $S_0 = \{0\}$, mex $= 1$), a za $c \ne 0$ mex je $0$. Poseban slučaj. Inače $0 \in S$ i množenje s $c \ne 0$ je permutacija $\mathbb{Z}_p^*$.</p>''',
        r'''<p>Primitivni korijen $g$ pretvara množenje u zbrajanje eksponenata modulo $p - 1$. Uvjet „$1, \dots, w-1 \in S_c$” postaje „$I(1) - x, \dots, I(w-1) - x \in I(S)$” za $x = I(c)$: cikličko podudaranje uzoraka koje se provjerava jednom konvolucijom (FFT). Binarno traži najveći $w$.</p>''',
    ],
    'coach': [
        ('Opažanje', r'''<p>Poseban slučaj: $0 \notin S$. Tada je $\operatorname{mex}(S_c) = 0$ za $c \ne 0$ i $1$ za $c = 0$; odgovor je jedino $c = 0$. Dalje pretpostavljamo $0 \in S$ (i $c \ne 0$ je kandidat; $c = 0$ daje mex $1$, što je kandidat samo ako je maksimum $1$).</p>'''),
        ('Redukcija: diskretni logaritam', r'''<p>Nađi primitivni korijen $g$ modulo $p$ i pretvori svaki $x \ne 0$ u $I(x)$ s $g^{I(x)} \equiv x$. Množenje s $c$ postaje zbrajanje $I(c)$ modulo $p - 1$. $\operatorname{mex}(S_c) \ge w$ ako i samo ako su $1, \dots, w-1 \in S_c$, tj. $I(1) - I(c), \dots, I(w-1) - I(c) \in I(S \setminus \{0\})$ (mod $p - 1$).</p>'''),
        ('Algoritam', r'''<p>Binarno pretraživanje po $w$ (uvjet je monoton). Provjera: neka je $f$ indikatorski polinom skupa $I(S)$, a $g_w$ indikator skupa $\{I(1), \dots, I(w-1)\}$. Ciklička konvolucija $g_w(x) \cdot f(1/x)$ (duljine $p - 1$) na poziciji $t$ broji koliko je elemenata $I(j) - t$ u $I(S)$; $t$ je dobar ako je koeficijent $\ge w - 1$. Konvolucija FFT-om u $O(p \log p)$. Na kraju za maksimalni $w$ ispiši sve dobre $t$, pretvorene natrag u $c = g^t$, sortirane.</p>'''),
        ('Složenost', r'''<p>$\Theta(p \log^2 p)$ zbog binarnog pretraživanja s FFT-om u svakom koraku.</p>'''),
    ],
    'solution': r'''
<p>Poseban slučaj: $0$ nije u skupu.</p>
<p>Najprije nađi primitivni korijen $g$ prostog broja $p$ i pretvori svaki broj $x$ u $I(x)$, gdje je $x \equiv g^{I(x)} \pmod p$.</p>
<p>Binarno pretražuj odgovor $w$ i razmotri kako ga provjeriti. Treba provjeriti postoji li cijeli $x$ takav da su $I(1) - x, I(2) - x, \dots, I(w-1) - x$ svi u skupu; pritom se računa modulo $p - 1$.</p>
<p>Ako je $f(x)$ funkcija izvodnica skupa $S$, a $g(x)$ funkcija izvodnica skupa $I(1), \dots, I(w-1)$, izračunaj cikličku konvoluciju $g(x)$ i $f(1/x)$ i provjeri je li koeficijent na nekoj poziciji barem $w - 1$ (tj. odgovara svim potrebnim elementima).</p>
<p>Konvoluciju računaj FFT-om; vremenska složenost $\Theta(p \log^2 p)$.</p>
''',
},
# ---------------------------------------------------------------- G
{
    'letter': 'G', 'title': 'Game: Celeste', 'title_hr': 'Igra: Celeste', 'slug': 'G_game_celeste',
    'tl': '2.5 s', 'ml': '1024 MB',
    'statement': r'''
<p>$n$ stupova na pozicijama $x_1 < \dots < x_n$, na $i$-tom jagoda veličine $a_i$. Madeline kreće sa stupa $1$ i skokom prelazi s pozicije $x$ na neki stup u $[x + L, x + R]$; na svakom posjećenom stupu skuplja jagodu. Nakon dolaska na stup $n$ skupljene jagode sortira nerastuće; želi leksikografski najveći takav niz. Ispiši ga, ili $-1$ ako stup $n$ nije dostižan.</p>
<h3>Ulaz</h3>
<p>$T$ testova; $n, L, R$ ($1 \le n \le 10^6$, $1 \le L \le R \le 10^9$), pozicije $x_i \le 10^9$, veličine $1 \le a_i \le n$. $\sum n \le 10^6$.</p>
<h3>Izlaz</h3>
<p>$k$ i niz, ili $-1$.</p>
''',
    'hints': [
        r'''<p>DP: $f_i$ = najbolji (leksikografski najveći sortirani) multiskup jagoda kojim se stiže na stup $i$; $f_i = \max_{L \le x_i - x_j \le R} f_j \cup \{a_i\}$. Dopušteni $j$ čine interval koji se pomiče udesno — klizni prozor s monotonim redom (deque).</p>''',
        r'''<p>Usporedba dvaju multiskupova i umetanje elementa: perzistentno segmentno stablo nad vrijednostima s brojačima i slučajnim hashem po čvoru — prvu razliku nalaziš spustom u $O(\log n)$, umetanje mijenja $O(\log n)$ čvorova.</p>''',
    ],
    'coach': [
        ('Opažanje', r'''<p>Neka je $f_i$ leksikografski najveći sortirani niz jagoda dostižan skokovima od $1$ do $i$. Vrijedi $f_i = \max_{L \le x_i - x_j \le R} f_j + a_i$, gdje $+$ znači umetanje $a_i$ u sortirani niz. Umetanje istog elementa čuva poredak nizova, pa je DP ispravan. Izravno: $\Theta(n^3)$.</p>'''),
        ('Redukcija: klizni prozor', r'''<p>Uvjet $x_i - R \le x_j \le x_i - L$ znači da je skup kandidata $j$ interval koji se s rastućim $i$ pomiče udesno — klasični klizni prozor; monotoni red (deque) daje maksimum $f_j$ u prozoru amortizirano $O(1)$ usporedbi. Time smo na $\Theta(n^2)$ zbog cijene usporedbe/umetanja.</p>'''),
        ('Algoritam: hashirano perzistentno segmentno stablo', r'''<p>Predstavi $f_i$ segmentnim stablom nad vrijednostima $1..n$ koje čuva broj pojavljivanja svake vrijednosti; svakoj vrijednosti dodijeli slučajan hash, čvor čuva zbroj hasheva svojih elemenata. Usporedba dvaju nizova: spusti se od korijena tražeći najveću vrijednost na kojoj se brojači razlikuju (prvo gledaj desno dijete — veće vrijednosti su na početku sortiranog niza) — $O(\log n)$; ono s više te vrijednosti je veće. Ponovna izgradnja za svaki $i$ je preskupa, pa stablo učini perzistentnim: umetanje $a_i$ stvara $O(\log n)$ novih čvorova. Na kraju rekonstruiraj niz iz $f_n$.</p>'''),
        ('Složenost', r'''<p>$\Theta(n \log n)$ vremena i memorije.</p>'''),
    ],
    'solution': r'''
<p>Razmotrimo dinamičko programiranje. Neka je $f_i$ leksikografski najveći sortirani niz brojeva dobiven skokovima od $1$ do $i$. Prijelaz je $f_i = \max_{L \le x_i - x_j \le R} f_j + a_i$, gdje $+$ označava umetanje $a_i$ u sortirani niz. Izravni prijelazi imaju složenost $\Theta(n^3)$, što je teško provući.</p>
<p>Najprije uvjet $L \le x_i - x_j \le R$: vrijedi $x_i - R \le x_j \le x_i - L$, pa se svaka točka može prenijeti iz intervala koji se kontinuirano pomiče udesno. To je klasični problem kliznog prozora, rješiv održavanjem monotono rastućeg reda. Složenost je sada $\Theta(n^2)$, pa razmatramo daljnju optimizaciju.</p>
<p>Usko grlo je usporedba dvaju sortiranih nizova i umetanje broja u niz. Segmentnim stablom održavamo niz frekvencija pojavljivanja svake vrijednosti. Svakoj vrijednosti slučajno dodijelimo hash; hash čvora je zbroj hasheva svih brojeva u čvoru, čime se najveća pozicija na kojoj se dva niza razlikuju nalazi u $\Theta(\log n)$ na segmentnom stablu.</p>
<p>Međutim, ponovna izgradnja segmentnog stabla svaki put previše je spora, pa segmentno stablo činimo perzistentnim: pri svakoj promjeni mijenja se samo $\Theta(\log n)$ čvorova.</p>
<p>Vremenska složenost: $\Theta(n \log n)$.</p>
''',
},
# ---------------------------------------------------------------- H
{
    'letter': 'H', 'title': 'Classic: N Real DNA Pots', 'title_hr': 'Klasika: N pravih DNA posuda', 'slug': 'H_classic_n_real_dna_pots',
    'tl': '2 s', 'ml': '1024 MB',
    'statement': r'''
<p>Dano je $n$ točaka $(x_i, y_i)$ s $x_1 < x_2 < \dots < x_n$. Odaberi $k$ točaka tako da je najmanji nagib dužine između bilo koje dvije odabrane točke najveći mogući. Ispiši taj najmanji nagib (tolerancija $10^{-6}$).</p>
<h3>Ulaz</h3>
<p>$n, k$ ($2 \le k \le n \le 10^5$) i točke s koordinatama do $10^9$.</p>
<h3>Izlaz</h3>
<p>Realan broj.</p>
<h3>Primjer</h3>
<p>Točke $(1,2),(2,4),(3,3),(4,1)$, $k = 3$: odgovor $-1.0$. Točke $(1,1),(5,3)$, $k = 2$: $0.5$.</p>
''',
    'hints': [
        r'''<p>Binarno pretraživanje po odgovoru $w$: mogu li se odabrati $k$ točaka tako da su svi nagibi $\ge w$? Za $i < j$ uvjet $\frac{y_j - y_i}{x_j - x_i} \ge w$ ekvivalentan je $y_i - w x_i \le y_j - w x_j$.</p>''',
        r'''<p>Dakle traži se najdulji neopadajući podniz niza $z_i = y_i - w x_i$ — $O(n \log n)$. Provjeri je li duljina $\ge k$. Umjesto uvjeta $r - l < \varepsilon$ iteriraj fiksan broj puta (npr. 60–100).</p>''',
    ],
    'coach': [
        ('Opažanje', r'''<p>Funkcija „postoji li izbor $k$ točaka sa svim nagibima $\ge w$” je monotona u $w$, pa binarno pretražujemo $w$ (nagibi mogu biti negativni; početni interval npr. $[-10^9, 10^9]$).</p>'''),
        ('Redukcija', r'''<p>Za $i < j$ (dakle $x_i < x_j$): $\frac{y_j - y_i}{x_j - x_i} \ge w \iff y_j - y_i \ge w(x_j - x_i) \iff y_i - w x_i \le y_j - w x_j$. Uz $z_i = y_i - w x_i$, skup točaka je dopustiv ako i samo ako je $z$ na njemu neopadajući. Traži se najdulji neopadajući podniz.</p>'''),
        ('Algoritam i složenost', r'''<p>LIS u $O(n \log n)$ (binarno pretraživanje u nizu „najmanjih završnih vrijednosti”, s <code>upper_bound</code> jer su jednaki dopušteni). Provjera $\text{LIS} \ge k$. Fiksan broj iteracija binarnog pretraživanja umjesto usporedbe $r - l < \varepsilon$ zbog preciznosti. Ukupno $\Theta(n \log n \log X)$.</p>'''),
    ],
    'solution': r'''
<p>Binarnim pretraživanjem tražimo odgovor $w$. Dvije točke $i < j$ mogu se zajedno odabrati ako i samo ako je $\frac{y_j - y_i}{x_j - x_i} \ge w$, što se pojednostavljuje u $y_i - w x_i \le y_j - w x_j$.</p>
<p>Tretiraj elemente kao $y_i - w x_i$; problem postaje traženje najduljeg rastućeg (neopadajućeg) podniza niza. Provjeri je li duljina barem $k$.</p>
<p>Napomena: pri binarnom pretraživanju provjera $r - l < \varepsilon$ može zbog preciznosti dovesti do prekoračenja vremena; radije provjeravaj relativnu grešku ili iteriraj fiksan broj puta.</p>
<p>Vremenska složenost: $\Theta(n \log n \log x)$.</p>
''',
},
# ---------------------------------------------------------------- I
{
    'letter': 'I', 'title': 'MEXimum Spanning Tree', 'title_hr': 'MEXimalno razapinjuće stablo', 'slug': 'I_meximum_spanning_tree',
    'tl': '2 s', 'ml': '256 MB',
    'statement': r'''
<p>Dan je povezan težinski graf. Nađi razapinjuće stablo s najvećim MEX-om težina bridova (MEX = najmanji prirodni broj, uključivo $0$, koji se ne pojavljuje).</p>
<h3>Ulaz</h3>
<p>$n, m$ ($1 \le n \le 1000$, $0 \le m \le 1000$) i bridovi $u_i\ v_i\ w_i$ ($0 \le w_i \le n$).</p>
<h3>Izlaz</h3>
<p>Najveći MEX.</p>
<h3>Primjer</h3>
<p>Bridovi $(1,2,0),(2,3,1),(1,3,1),(3,4,2)$: odgovor $3$.</p>
''',
    'hints': [
        r'''<p>Dovoljno je naći <em>šumu</em> s najviše jednim bridom svake težine koja sadrži težine $0, 1, \dots, w-1$; ostatak stabla dopuni bilo kakvim bridovima — MEX se ne smanjuje.</p>''',
        r'''<p>„Bez ciklusa” je grafovski matroid, „najviše jedan brid po težini” particijski matroid. Najveći zajednički nezavisan skup s bridovima dodavanim redom po težini: presjek matroida.</p>''',
    ],
    'coach': [
        ('Opažanje', r'''<p>Ako imamo šumu $F$ s najviše jednim bridom svake težine iz $\{0, \dots, w-1\}$, možemo je proširiti do razapinjućeg stabla (graf je povezan) dodatnim bridovima; dodavanje bridova ne smanjuje MEX. Dakle odgovor je najveći $w$ za koji postoji šuma s bridovima težina točno $0, 1, \dots, w-1$.</p>'''),
        ('Redukcija: presjek matroida', r'''<p>Skupovi bridova bez ciklusa čine grafovski matroid; skupovi s najviše jednim bridom po težini čine particijski matroid. Skup težina $\{0..w-1\}$ je „prefiks”. Ako ograničimo bridove na težine $< w$, tražimo zajednički nezavisan skup veličine $w$ — postoji ako i samo ako je najveći presjek za te bridove veličine $w$.</p>'''),
        ('Algoritam i složenost', r'''<p>Binarno pretraživanje po $w$ + algoritam presjeka matroida (augmentirajući putovi u grafu razmjene s BFS-om) daje odgovor. Alternativno, dodavaj bridove po rastućoj težini i inkrementalno održavaj najveći zajednički nezavisan skup: nakon dodavanja svih bridova težine $w$, ako se veličina presjeka nije povećala na $w+1$, odgovor je $w$. Složenost $\Theta(n^{2.5})$ (odn. $O(m \cdot r \cdot (m + n))$ u naivnoj izvedbi za $m \le 1000$).</p>'''),
    ],
    'solution': r'''
<p>Promotrimo bilo koju šumu koja sadrži najviše jedan brid svake težine; dodatni bridovi mogu se dodati da se dobije stablo bez smanjenja MEX-a.</p>
<p>Stoga presijecamo matroid boja (najviše jedan brid svake težine) i grafovski matroid (bez ciklusa), dodajući bridove u rastućem poretku težine.</p>
<p>Vremenska složenost: $\Theta(n^{2.5})$. Binarno pretraživanje s presjekom matroida također prolazi.</p>
''',
},
# ---------------------------------------------------------------- J
{
    'letter': 'J', 'title': 'Master of Polygon', 'title_hr': 'Majstor poligona', 'slug': 'J_master_of_polygon',
    'tl': '4 s', 'ml': '1024 MB',
    'statement': r'''
<p>Dan je jednostavan poligon s $n$ vrhova (cjelobrojne koordinate do $30\,000$, bez kolinearnih uzastopnih stranica). Za $q$ upita (dužina $PQ$) odgovori siječe li dužina rub poligona (dodir se računa).</p>
<h3>Ulaz</h3>
<p>$n, q$ ($3 \le n \le 2 \cdot 10^5$, $1 \le q \le 2 \cdot 10^5$), vrhovi, upiti.</p>
<h3>Izlaz</h3>
<p><code>YES</code>/<code>NO</code> za svaki upit.</p>
''',
    'hints': [
        r'''<p>Podijeli-pa-vladaj po $x$-koordinati: $\mathrm{solve}(l, r)$ gleda samo dio slike s $x \in [l, r]$. Dužina (stranica ili upit) koja siječe obje okomice $x = l$ i $x = r$ tretira se kao „pravac” u ovom čvoru i ne ide u rekurziju; ostale idu u lijevu i/ili desnu polovicu. Svaka dužina se pojavi u $O(\log V)$ čvorova.</p>''',
        r'''<p>Stranice-pravci u čvoru se ne sijeku (poligon je jednostavan), pa ih se može sortirati po $y$ na $x = l$ i taj poredak vrijedi na cijelom $[l, r]$ — binarno pretraživanje lokalizira upit. Dio poligona unutar trake raspada se na povezane lomljene linije koje dodiruju rub trake; za upit-pravac provjeri sudara li se s njihovim konveksnim ljuskama.</p>''',
    ],
    'coach': [
        ('Opažanje: podijeli-pa-vladaj po apscisi', r'''<p>Neka $\mathrm{solve}(l, r)$ ($l < r$) rješava sve što je unutar trake $l \le x \le r$; kreni od $[x_{\min}, x_{\max}]$ poligona (upiti izvan toga očito ne sijeku). U čvoru s $mid$ svaka stranica ili upitna dužina: (a) siječe obje okomice $A: x = l$ i $B: x = r$ — postaje „pravac” ovog čvora i ne rekurzira; (b) inače ide u $\mathrm{solve}(l, mid)$ i/ili $\mathrm{solve}(mid, r)$. Slučaj kad su i stranica i upit okomiti na $x$-os obradi zasebno (uvjet $l < r$ ga preskače).</p>'''),
        ('Redukcija: stranice kao pravci', r'''<p>Stranice-pravci u čvoru međusobno se ne sijeku unutar trake, pa ih sortiramo po $y$-koordinati presjeka s $A$; poredak je isti za svaki $x' \in [l, r]$. Za svaku upitnu dužinu (bilo koju u čvoru) binarnim pretraživanjem nađemo stranice-pravce neposredno iznad/ispod njezinih krajeva i provjerimo presjek — $O(\log n)$.</p>'''),
        ('Algoritam: upiti kao pravci', r'''<p>Dio poligona u traci raspada se na povezane lomljene linije, svaka dotiče barem jednu od okomica $A$, $B$. Za svaku lomljenu liniju spojenu s $A$ zapamti $[y_l, y_r]$ — raspon $y$ njezinih presjeka s $A$; ako je $y$ presjeka upita s $A$ pokriven nekim rasponom, postoji presjek (isto za $B$). Inače podijeli lomljene linije u četiri klase: spojene s $A$ iznad/ispod upita, spojene s $B$ iznad/ispod upita. Za svaku klasu: upit-pravac siječe lomljene linije ako i samo ako siječe njihovu zajedničku konveksnu ljusku. Sortiraj lomljene linije i upite po $y$ presjeka s rubom i inkrementalno gradi ljusku (sweep po $y$): zbog svojstava jednostavnog poligona nova ljuska je prefiks stare + dio nove, pa se spaja linearnim prolazom po novoj; test „pravac siječe konveksnu ljusku” binarnim pretraživanjem.</p>'''),
        ('Složenost', r'''<p>Svaka stranica/upit obrađuje se $O(\log V)$ puta uz $O(\log(n + q))$ po obradi: $O((n + q) \log(n + q) \log V)$; diskretizacijom koordinata $O((n + q) \log^2 (n + q))$.</p>'''),
    ],
    'solution': r'''
<p>Podijeli-pa-vladaj po apscisi: neka $\mathrm{solve}(l, r)$ označava potproblem koji razmatra samo dio slike s apscisama u $[l, r]$, gdje je $l < r$. Neka su $x_l$ i $x_r$ najmanja i najveća apscisa vrhova poligona. Najprije ukloni sve upite koji ne prolaze kroz $[x_l, x_r]$ (očito ne sijeku poligon), a zatim pozovi $\mathrm{solve}(x_l, x_r)$. Uvjet $l < r$ može propustiti slučaj kad su i upitna dužina i stranica poligona okomite na $x$-os — obradi ga zasebno.</p>
<p>U $\mathrm{solve}(l, r)$ uzmi $mid = \lfloor (l+r)/2 \rfloor$ i dvije okomice $A: x = l$, $B: x = r$. Svaka stranica poligona ili upitna dužina ima jednu od tri mogućnosti: siječe i $A$ i $B$ — može se tretirati kao pravac i ne rekurzira dalje; siječe potproblem $\mathrm{solve}(l, mid)$ — rekurzivni poziv; siječe $\mathrm{solve}(mid, r)$ — rekurzivni poziv.</p>
<p><b>Stranice kao pravci.</b> Sortiraj sve takve stranice po rastućoj $y$-koordinati presjeka s pravcem $A$. Za svaki $x' \in [l, r]$ njihov relativni poredak po $y$ presjeka s $x = x'$ ostaje isti. Prođi sve upitne dužine i binarnim pretraživanjem u $O(\log n)$ nađi stranice koje sijeku.</p>
<p><b>Upitne dužine kao pravci.</b> Dio poligona unutar $[l, r]$ podijeljen je na više povezanih lomljenih linija, od kojih svaka siječe barem jednu od dviju okomica. Za svaku lomljenu liniju spojenu s lijevom granicom predizračunaj najmanju i najveću $y$-koordinatu presjeka s lijevom granicom, $y_l$ i $y_r$. Ako je $y$-koordinata presjeka upitne dužine s $A$ pokrivena nekim intervalom $[y_l, y_r]$, postoji presjek. Isto za desnu granicu $B$.</p>
<p>Zatim provjeri siječe li pravac upita neki dio lomljene linije iznad ili ispod njega. Podijeli povezane lomljene linije u četiri kategorije. Slučaj 1: lomljena linija spojena je s lijevom granicom i presjek s njom je iznad presjeka upitnog pravca s lijevom granicom — upitni pravac siječe te linije ako i samo ako siječe njihovu konveksnu ljusku. Slučaj 2: analogno za desnu granicu. Dva slučaja s lomljenim linijama ispod upitnog pravca obrađuju se jednako.</p>
<p>Sortiraj lomljene linije i upitne dužine po $y$-koordinati presjeka s granicom, zadržavajući samo točke na konveksnim ljuskama. Problem se svodi na održavanje konveksne ljuske uz spajanje s danom ljuskom i upit siječe li dani pravac ljusku. Budući da su $y$-koordinate granica novih ljuski monotone, a prema geometrijskim svojstvima jednostavnih poligona, postoji dijelišna točka takva da raniji dio spojene ljuske dolazi iz stare, a kasniji iz nove ljuske; nađi je prolazom po novoj ljusci. Za klasični upit „siječe li pravac konveksnu ljusku” koristi binarno pretraživanje po ljusci.</p>
<p>Neka je raspon koordinata $v$. Svaka stranica i upit obrađuju se rekurzivno $O(\log v)$ puta, svaki put s cijenom $O(\log(n+q))$ za sortiranje ili binarno pretraživanje. Ukupno $O((n+q) \log(n+q) \log v)$; diskretizacijom koordinata $O((n+q) \log^2(n+q))$.</p>
''',
},
# ---------------------------------------------------------------- K
{
    'letter': 'K', 'title': 'Shuttle Tour', 'title_hr': 'Kružna tura', 'slug': 'K_shuttle_tour',
    'tl': '4 s', 'ml': '1024 MB',
    'statement': r'''
<p>Težinsko stablo s $n$ lokacija, s najviše $50$ listova. Svaka lokacija je otvorena ili zatvorena. Operacije: <code>1 x</code> — promijeni status $x$; <code>2 l r</code> — najkraća zatvorena šetnja koja posjećuje sve otvorene lokacije s indeksima u $[l, r]$ (ili $-1$ ako ih nema).</p>
<h3>Ulaz</h3>
<p>$n, q \le 2 \cdot 10^5$, početni statusi, bridovi ($w \le 10^9$), operacije.</p>
<h3>Izlaz</h3>
<p>Odgovor za svaki upit tipa 2.</p>
''',
    'hints': [
        r'''<p>Najkraća zatvorena šetnja kroz skup vrhova stabla = $2 \times$ zbroj težina bridova minimalnog podstabla koje ih povezuje, tj. bridova koji imaju odabrane vrhove na obje strane.</p>''',
        r'''<p>Najviše $50$ listova znači da se stablo raspada na najviše $k = 50$ lanaca (od svakog lista prema gore). Na svakom lancu skup odabranih vrhova u lancu je određen najmanjom i najvećom dubinom — segmentno stablo po indeksima s po $k$ parova (min, max dubine) u svakom čvoru.</p>''',
    ],
    'coach': [
        ('Opažanje', r'''<p>Odgovor je dvostruki zbroj težina bridova stabla kojima na obje strane postoji otvoren vrh iz $[l, r]$ — tj. dvostruka težina Steinerova podstabla odabranih vrhova.</p>'''),
        ('Redukcija: lanci od listova', r'''<p>Iz korijena $1$ provedi bilo koju dekompoziciju na lance (npr. svaki list ide prema gore do prvog već pokrivenog vrha): najviše $k \le 50$ lanaca, jer svaki lanac završava u listu. Dio Steinerova podstabla unutar lanca $c$ je put od najplićeg do najdubljeg odabranog vrha u tom lancu, produljen prema gore do točke gdje se lanac spaja s ostatkom Steinerova stabla (ako ispod/iznad postoje odabrani vrhovi u drugim lancima koji vise s tog lanca).</p>'''),
        ('Algoritam', r'''<p>Segmentno stablo po indeksima lokacija $1..n$: čvor za raspon indeksa čuva, za svaki lanac $c$, najmanju i najveću dubinu otvorenih vrhova tog lanca s indeksom u rasponu ($k$ parova). Spajanje dvaju čvorova: $O(k)$ (min/max po lancu). Upit $[l, r]$ daje $k$ parova; iz njih rekurzijom po strukturi lanaca (lanac visi s roditeljskog lanca u poznatoj točki) izračunaj težinu Steinerova stabla: za lanac s odabranim vrhovima ili odabranim potomcima, doprinos je duljina od najniže relevantne točke do najviše, pa prema gore do točke vješanja, ako je i drugdje nešto odabrano. Ažuriranje: $O(k \log n)$.</p>'''),
        ('Složenost', r'''<p>$O(nk + qk \log n)$ s $k \le 50$.</p>'''),
    ],
    'solution': r'''
<p>Odgovor je očito dvostruki zbroj težina bridova stabla kojima se na obje strane nalaze uključeni (ON) vrhovi.</p>
<p>Polazeći od korijena $1$, provedi bilo koju dekompoziciju stabla na lance; dobije se najviše $k = 50$ lanaca.</p>
<p>Izgradi segmentno stablo po indeksima; svaki čvor za odgovarajući raspon indeksa pamti najmanju i najveću dubinu uključenih vrhova na svakom lancu. Odgovor se tada dobiva rekurzivnim relacijama.</p>
<p>Vremenska složenost: $O(nk + qk \log n)$.</p>
''',
},
# ---------------------------------------------------------------- L
{
    'letter': 'L', 'title': 'Barkley', 'title_hr': 'Barkley', 'slug': 'L_barkley',
    'tl': '1 s', 'ml': '1024 MB',
    'statement': r'''
<p>Dan je niz $a_1..a_n$ ($a_i \le 10^{18}$). Za svaki od $q$ upita $(l, r, k)$ ukloni točno $k$ elemenata iz $[l, r]$ tako da je $\gcd$ preostalih najveći; ispiši ga.</p>
<h3>Ulaz</h3>
<p>$n \le 10^5$, $q \le 66666$; upiti s $1 \le k \le \min(3, r - l)$; najviše $66000$ upita s $k = 1$, $660$ s $k = 2$, $6$ s $k = 3$.</p>
<h3>Izlaz</h3>
<p>Odgovori.</p>
<h3>Primjer</h3>
<p>$a = (3, 2, 6, 4)$: upit $(1, 3, 1) \to 3$; $(1, 4, 2) \to 3$; $(1, 4, 3) \to 6$.</p>
''',
    'hints': [
        r'''<p>Neka je $g(l, r)$ gcd intervala. Za $k = 1$: $\max_x \gcd(g(l, x-1), g(x+1, r))$. Funkcija $g(l, \cdot)$ poprima samo $O(\log V)$ različitih vrijednosti (svaka promjena barem upola smanjuje).</p>''',
        r'''<p>Ako je $g(l, x) = g(l, x+1) = \dots = g(l, t)$, među brisanjima pozicija $x+1..t+1$ optimalno je izbrisati $t + 1$ (lijevi gcd isti, desni sufiks najkraći). Dakle dovoljno je probati $O(\log V)$ kandidata; $g(x+1, r)$ dohvaćaj sparse tableom. Za $k = 2, 3$ isprobaj prvu poziciju brisanja i rekurzivno riješi $k - 1$.</p>''',
    ],
    'coach': [
        ('Opažanje', r'''<p>$g(l, x)$ kao funkcija od $x$ je nerastuća u smislu djeljivosti: svaka promjena vrijednosti dijeli prethodnu, pa ima $O(\log V)$ različitih vrijednosti i intervali konstantnosti su blokovi. Isto za $g(\cdot, r)$.</p>'''),
        ('Redukcija za $k = 1$', r'''<p>Brišemo $x$; rezultat je $\gcd(g(l, x-1), g(x+1, r))$. Unutar bloka $g(l, x) = \dots = g(l, t)$ brisanje bilo kojeg od $x+1, \dots, t+1$ daje isti lijevi dio, a desni dio $g(y+1, r)$ je najveći (djeljivošću) za najveći $y = t+1$. Dakle kandidati su samo krajevi blokova: $O(\log V)$ pozicija po upitu, svaka s upitom gcd-a intervala (sparse table, $O(1)$ ili $O(\log n)$). Blokove $g(l, \cdot)$ predizračunaj za sve $l$ rekurzivno iz $g(l+1, \cdot)$ (lista od $O(\log V)$ parova (vrijednost, kraj)).</p>'''),
        ('Algoritam za $k = 2, 3$', r'''<p>Isprobaj poziciju prvog (najljevijeg) brisanja među kandidatima — opet dovoljno krajevi blokova $g(l, \cdot)$ — i rekurzivno riješi potproblem s $k - 1$ na ostatku (interval se raspada na dva dijela; lijevi gcd je fiksan, a desni dio je novi upit). Grananje $O(\log V)$ po razini, dubina $k$.</p>'''),
        ('Složenost', r'''<p>$\Theta(n \log^2 V + \sum_{\text{upiti}} \log^{k+1} V)$ — ograničenja na broj upita s $k = 2, 3$ to čine izvedivim.</p>'''),
    ],
    'solution': r'''
<p>Neka je $g(l, r)$ gcd svih brojeva u intervalu $[l, r]$.</p>
<p>Za $k = 1$ tražimo $\max_{l \le x \le r} \gcd(g(l, x-1), g(x+1, r))$. Ako u $g(l, \cdot)$ postoje uzastopne jednake vrijednosti, recimo $g(l, x) = g(l, x+1) = \dots = g(l, t)$, tada je među brisanjima iz $[x+1, t+1]$ optimalno izbrisati $t+1$. Postoji samo $\Theta(\log V)$ različitih vrijednosti $g(l, \cdot)$, pa najdesniju poziciju brisanja možemo učinkovito nabrojati. $g(l, \cdot)$ možemo predizračunati rekurzivno iz $g(l+1, \cdot)$.</p>
<p>Za $k = 2, 3$ pretražuj poziciju prvog brisanja i rekurzivno rješavaj potprobleme.</p>
<p>Vremenska složenost: $\Theta(n \log^2 V + \sum \log^{k+1} V)$.</p>
''',
},
# ---------------------------------------------------------------- M
{
    'letter': 'M', 'title': 'Stage Clear', 'title_hr': 'Prolazak razine', 'slug': 'M_stage_clear',
    'tl': '7 s', 'ml': '1024 MB',
    'statement': r'''
<p>DAG s $n$ vrhova i $m$ lukova ($u_i < v_i$); igrač kreće iz $1$ s $X$ HP-a. Na svakom vrhu $i \ne 1$ je čudovište: pri prvom posjetu igrač gubi $a_i$ HP (HP ne smije pasti ispod $0$), a nakon pobjede dobiva $b_i$ HP. Igrač se kreće lukovima ili se u bilo kojem trenutku teleportira u $1$. Nađi najmanji početni HP dovoljan da se pobijede sva čudovišta.</p>
<h3>Ulaz</h3>
<p>$n, m$ ($n + m \le 72$, $n \ge 2$, $m \ge n - 1$), parovi $a_i, b_i \le 10^{15}$ za $i = 2..n$, lukovi. Svaki vrh dostižan iz $1$.</p>
<h3>Izlaz</h3>
<p>Najmanji početni HP.</p>
<h3>Primjer</h3>
<p>$n = 4$: $(a, b) = (4,2), (5,3), (2,6)$, lukovi $1\to2, 1\to3, 2\to4, 3\to4$: odgovor $4$.</p>
''',
    'hints': [
        r'''<p>Teleport u $1$ je besplatan, pa je bitno samo <em>u kojem redoslijedu</em> pobjeđujemo čudovišta: vrh $v$ smije biti sljedeći ako mu je barem jedan prethodnik već pobijeđen (ili je to $1$). Za $n \le 26$: DP po podskupovima pobijeđenih.</p>''',
        r'''<p>Za $n \ge 27$ je $m \le 45$, pa najviše $m - (n-1) \le 19$ „viška” lukova: nabroji koji je ulazni luk svakog vrha „roditeljski” ($2^{m-n+1}$ korijenskih stabala). Na stablu vrijedi klasična pohlepnost: najbolji redoslijed bez ograničenja roditelja dobiva se sortiranjem; prvog čudovišta u tom poretku spoji s roditeljem (moraju se boriti odmah jedno za drugim).</p>''',
    ],
    'coach': [
        ('Opažanje', r'''<p>Kretanje je slobodno (lukovi + teleport), pa je jedina restrikcija: čudovište $v$ može se napasti tek kad je pobijeđen neki njegov prethodnik (ili $v$ ima luk iz $1$). Tražimo poredak svih čudovišta koji minimizira potrebni početni HP; potrebni HP za poredak računa se unatrag: $\text{need}(x, \text{ostatak}) = a_x + \max(\text{need}(\text{ostatak}) - b_x, 0)$.</p>'''),
        ('Redukcija 1: $n \le 26$', r'''<p>DP po podskupovima: $f_S$ = najmanji HP potreban da se pobijede sva čudovišta iz $S$ kad su sva ostala već pobijeđena. $f_\emptyset = 0$; $f_{S \cup \{x\}} = \min_x \big(a_x + \max(f_S - b_x, 0)\big)$ po $x \notin S$ koji su „dostupni” — imaju prethodnika izvan $S \cup \{x\}$ (već pobijeđen) ili prethodnika $1$. Odgovor $f_{\{2..n\}}$; $O(n 2^{n-1})$.</p>'''),
        ('Redukcija 2: $n \ge 27$', r'''<p>Iz $n + m \le 72$ slijedi $m \le 45$; svih $n - 1$ vrhova ima ulazni luk, pa nakon uklanjanja jednog ulaznog luka po vrhu ostaje najviše $m - n + 1 \le 19$ lukova — najviše $19$ vrhova ima ulazni stupanj $> 1$. Za svaki vrh odaberi jedan ulazni luk kao roditeljski: $2^{m-n+1}$ korijenskih stabala, a optimalno rješenje DAG-a je optimum nekog stabla (u optimalnom poretku svaki vrh ima prvog pobijeđenog prethodnika — to mu je roditelj).</p>'''),
        ('Algoritam na stablu: pohlepno spajanje', r'''<p>Bez ograničenja roditelja optimalan poredak dobiva se sortiranjem: prvo čudovišta s $a_i \le b_i$ po rastućem $a_i$, zatim ona s $a_i > b_i$ po padajućem $b_i$. Uzmi prvo čudovište $x$ u tom poretku: čim je njegov roditelj $p$ pobijeđen, odmah treba pobijediti $x$. Spoji $x$ u $p$ u jedno „složeno” čudovište s $(a, b)$ jednakima potrebnom HP-u i neto dobitku niza $p, x$: $a' = a_p + \max(a_x - b_p, 0)$, $b' = b_p + b_x - a_x + (a' - a_p)$ (ekvivalentno: $b' = a' - a_p - a_x + b_p + b_x$). Problem se smanji za $1$; ponovi $n - 1$ puta. Po stablu $O(n \log n)$; ukupno $O(2^{m-n+1} n \log n)$.</p>'''),
    ],
    'solution': r'''
<p>Ako je $n \le 26$, koristimo DP po podskupovima. Neka je $f_S$ najmanji početni HP potreban kad je skup pobijeđenih čudovišta $S$. Nabrajamo prethodno pobijeđeno čudovište $x$ i ažuriramo $f_{S \cup \{x\}}$ vrijednošću $\max(f_S - b_x, 0) + a_x$, gdje $x \notin S$, a $S$ ne sadrži sve vrhove koji imaju luk prema $x$ (tj. $x$ je dostupan). Vremenska složenost: $O(n 2^{n-1})$.</p>
<p>Ako je $n \ge 27$, iz uvjeta $n + m \le 72$ slijedi $m \le 45$. Budući da vrh $1$ dostiže sve ostale vrhove, preostalih $n - 1$ vrhova ima barem jedan ulazni luk; nakon uklanjanja tih lukova najviše $19$ vrhova ima ulazni stupanj veći od $1$.</p>
<p>Za svaki vrh nabrojimo jedan ulazni luk kao roditeljski, čime dobivamo korijensko stablo. Ukupno ima $2^{m-n+1}$ mogućih stabala, a potproblem na korijenskom stablu klasičan je pohlepni algoritam.</p>
<p>Zanemarimo li ograničenje roditelja, optimalni redoslijed napada dobiva se sortiranjem. Uzmemo prvo čudovište koje treba pobijediti u optimalnom poretku; čim je njegov roditelj pobijeđen, odmah moramo pobijediti i njega. Stoga ga spojimo s roditeljem, smanjujući veličinu problema za $1$, i ponavljamo $n - 1$ krugova dok problem ne postane veličine $1$.</p>
<p>Složenost svakog potproblema je $O(n \log n)$, pa je ukupna vremenska složenost $O(2^{m-n+1} n \log n)$.</p>
''',
},
]
