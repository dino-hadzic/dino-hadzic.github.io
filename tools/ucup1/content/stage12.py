# -*- coding: utf-8 -*-
STAGE = {
    'no': 12,
    'name': 'Stage 12: Ōokayama',
    'source_name': 'Tokyo Tech Programming Contest 2022, TTPC 2022',
    'source_html': r'''
<p>Prijevod službenog rješenja autorskog tima TTPC 2022: <a href="https://contest.ucup.ac/download.php?type=attachments&amp;id=1207&amp;r=1">Tutorial (en)</a>. Tekst zadatka preveden je prema službenim <a href="https://contest.ucup.ac/download.php?type=attachments&amp;id=1207&amp;r=0">engleskim tekstovima zadataka</a>. Zadatak je dostupan na <a href="https://contest.ucup.ac/contest/1207">Universal Cup Judging System</a>.</p>
''',
}

PROBLEMS = [
# ---------------------------------------------------------------- A
{
    'letter': 'A', 'title': 'XOR Tree Path', 'title_hr': 'XOR put u stablu', 'slug': 'A_xor_tree_path',
    'tl': '2 s', 'ml': '1024 MB',
    'statement': r'''
<p>Dano je korijensko stablo s $N$ vrhova (korijen je vrh $1$). Svaki je vrh obojen bijelo ($A_i = 0$) ili crno ($A_i = 1$). Operacija: odaberi list $x$ i promijeni boju svim vrhovima na putu od korijena do $x$ (uključivo). Operaciju možeš izvesti proizvoljno mnogo puta. Koliko najviše crnih vrhova možeš postići?</p>
<h3>Ulaz</h3>
<p>$N$ ($2 \le N \le 10^5$), zatim $A_1, \dots, A_N$ i $N - 1$ bridova $U_i\ V_i$.</p>
<h3>Izlaz</h3>
<p>Najveći mogući broj crnih vrhova.</p>
<h3>Primjer</h3>
<p>Za stablo s bridovima $1\!-\!2, 1\!-\!3, 3\!-\!4, 3\!-\!5$ i bojama $1, 0, 0, 1, 0$ odgovor je $5$: operacija na listu $2$, pa na listu $5$.</p>
''',
    'hints': [
        r'''<p>Boja vrha $v$ na kraju ovisi samo o tome koliko je listova iz podstabla vrha $v$ odabrano — točnije, o <em>parnosti</em> tog broja.</p>''',
        r'''<p>DP po stablu sa stanjem (vrh, parnost broja odabranih listova u podstablu). Kako se spajaju djeca? Parnosti djece se zbrajaju modulo $2$.</p>''',
    ],
    'coach': [
        ('Što se točno događa s vrhom $v$ kad odaberemo neki list $x$?',
         r'''
<p>Boja vrha $v$ promijeni se točno onda kad put od korijena do $x$ prolazi kroz $v$, a to je točno onda kad je $x$ u podstablu vrha $v$. Dakle, nakon svih operacija vrh $v$ je promijenio boju onoliko puta koliko je odabranih listova (s ponavljanjem) u njegovu podstablu. Boja ovisi samo o tom broju, ne o redoslijedu.</p>
'''),
        ('Ima li smisla isti list odabrati dvaput? Koja je veličina koja jedino odlučuje o boji?',
         r'''
<p>Dva odabira istog lista promijene svaki vrh na putu dvaput – to je identitet. Zato je za svaki list bitno samo je li odabran neparan broj puta ($1$) ili paran ($0$), a za vrh $v$ bitna je samo <em>parnost</em> $p_v$ broja odabranih listova u podstablu. Konačna boja je $A_v \oplus p_v$. Time smo beskonačan prostor nizova operacija sveli na $2^{\#\text{listova}}$ konačnih izbora, a i to je previše za pretragu – treba struktura.</p>
'''),
        ('Kako je parnost $p_v$ unutarnjeg vrha povezana s parnostima njegove djece?',
         r'''
<p>Skup listova u podstablu vrha $v$ disjunktna je unija skupova listova podstabala djece, pa je broj odabranih listova zbroj po djeci, a parnost zbroja je XOR parnosti: $p_v = \bigoplus_c p_c$. To je lokalno pravilo – odluka o podstablu vrha $v$ komunicira s ostatkom stabla isključivo kroz jedan bit $p_v$. Upravo takva situacija poziva na dinamičko programiranje po stablu s tim bitom kao stanjem.</p>
'''),
        ('Zašto je stanje (vrh, parnost) dovoljno – ne gubimo li informaciju o tome koji su listovi odabrani?',
         r'''
<p>Broj crnih vrhova u podstablu vrha $v$ ovisi samo o odabirima unutar podstabla, a utjecaj tih odabira na vrhove <em>izvan</em> podstabla (na pretke) ide samo preko $p_v$. Dvije konfiguracije s istom parnošću $p_v$ jednako djeluju na ostatak stabla, pa je od njih dovoljno pamtiti bolju: $dp[v][p]$ = najveći broj crnih vrhova u podstablu uz parnost $p$. Djecu spajamo kao „ruksak po parnosti”: $new[x \oplus y] = \max(cur[x] + dp[c][y])$, a na kraju dodamo $[A_v \oplus p = 1]$ za sam vrh $v$.</p>
'''),
        ('Koliko to košta i na što treba paziti u implementaciji?',
         r'''
<p>Svaki vrh spaja se s roditeljem u $O(1)$ (četiri kombinacije parnosti), pa je ukupno $O(N)$. Za $N = 10^5$ i lančasto stablo rekurzija može biti duboka $10^5$, pa je sigurnije obraditi vrhove u obrnutom BFS redoslijedu. Rubni slučaj: korijen nije list čak ni kad ima samo jedno dijete (uvjet $N \ge 2$ to jamči), a nedostižne kombinacije parnosti označavamo s $-\infty$.</p>
'''),
    ],
    'tips': [
        r'''<strong>Operacija primijenjena dvaput = identitet</strong> je znak da su bitne samo parnosti. Čim to vidiš, prostor stanja pada s „koliko puta” na jedan bit po objektu.''',
        r'''Kad se odluke u podstablu prema ostatku stabla „vide” samo kroz malu sažetu informaciju (jedan bit, jedan broj), to je točno stanje za DP po stablu; spajanje djece je konvolucija po toj informaciji.''',
        r'''Za $N \ge 10^5$ izbjegavaj rekurzivni DFS bez potrebe: BFS redoslijed i obrada od kraja daju isti poredak „djeca prije roditelja” bez rizika prelijevanja stoga.''',
        r'''Nedostižna stanja u max-DP-u označi velikim negativnim brojem i eksplicitno ih preskoči pri spajanju – inače se $-\infty + (\text{nešto})$ lako pretvori u „valjanu” vrijednost.''',
    ],
    'solution': r'''
<p>Boja vrha $v$ određena je brojem odabranih listova u podstablu vrha $v$. Budući da odabir dvaju listova vraća boju vrha $v$ u početno stanje, bitno je samo je li iz podstabla vrha $v$ odabran paran ili neparan broj listova.</p>
<p>Zadatak zato rješavamo sljedećim dinamičkim programiranjem po stablu:</p>
<p>$dp[v][i]$ — najveći broj crnih vrhova u podstablu vrha $v$ ako je broj odabranih listova u podstablu vrha $v$ kongruentan $i$ modulo $2$.</p>
<p>Vremenska složenost je $O(N)$.</p>
''',
    'detailed': r'''
<h3>1. Što operacija radi i zašto je bitna samo parnost</h3>
<p>Odabir lista $x$ mijenja boju svakom vrhu na putu od korijena do $x$. Vrh $v$ leži na tom putu točno onda kad je $x$ u podstablu $T_v$ vrha $v$ (u korijenskom stablu put od korijena do $x$ prolazi kroz sve pretke od $x$, i ni kroz što drugo). Dakle, ako je multiskup odabranih listova $S$, vrh $v$ mijenja boju $|S \cap T_v|$ puta i konačna boja mu je</p>
<p>$$A_v \oplus \bigl(|S \cap T_v| \bmod 2\bigr).$$</p>
<p>Dva odabira istog lista poništavaju se, pa svaki list ima smisla odabrati najviše jednom; nadalje $S$ je običan skup listova. Označimo $p_v = |S \cap T_v| \bmod 2$. Cilj je odabrati $S$ tako da broj vrhova s $A_v \oplus p_v = 1$ bude najveći.</p>
<h3>2. Lokalno pravilo za parnosti</h3>
<p>Za list $\ell$ je $p_\ell = [\ell \in S]$ – slobodan bit. Za unutarnji vrh $v$ s djecom $c_1, \dots, c_k$ skupovi listova podstabala $T_{c_1}, \dots, T_{c_k}$ disjunktni su i njihova unija su svi listovi $T_v$ (sam $v$ nije list). Zato je $|S \cap T_v| = \sum_j |S \cap T_{c_j}|$, a parnost zbroja je XOR parnosti:</p>
<p>$$p_v = p_{c_1} \oplus p_{c_2} \oplus \dots \oplus p_{c_k}.$$</p>
<p>Obratno, svaka kombinacija bitova na listovima je dostižna (svaki list odaberemo ili ne), pa je zadatak: odaberi bitove na listovima, izračunaj $p_v$ pravilom gore i maksimiziraj $\sum_v [A_v \oplus p_v = 1]$.</p>
<h3>3. Zašto je DP stanje (vrh, parnost) dovoljno</h3>
<p>Promotrimo podstablo $T_v$. Odabiri listova unutar $T_v$ utječu na boje vrhova u $T_v$ (to brojimo unutar podstabla) i na boje predaka vrha $v$ – ali na pretke utječu <em>isključivo</em> kroz vrijednost $p_v$, jer predak $u$ vidi samo $|S \cap T_u| \bmod 2$, a doprinos $T_v$ tome je upravo $p_v$. Dvije konfiguracije odabira unutar $T_v$ s istom parnošću $p_v$ potpuno su zamjenjive s gledišta ostatka stabla, pa je dovoljno za svaku parnost pamtiti onu s najviše crnih vrhova:</p>
<p>$$dp[v][p] = \max\bigl\{\#\text{crnih u } T_v \;:\; \text{odabir listova u } T_v \text{ s parnošću } p\bigr\},$$</p>
<p>ili $-\infty$ ako takav odabir ne postoji.</p>
<p><strong>List:</strong> $dp[\ell][0] = A_\ell$ (ne odabran, boja ostaje), $dp[\ell][1] = 1 - A_\ell$ (odabran, boja se mijenja).</p>
<p><strong>Unutarnji vrh:</strong> djecu dodajemo jedno po jedno. Neka $cur[x]$ označava najbolji rezultat već obrađene djece uz XOR njihovih parnosti jednak $x$ (početno $cur = (0, -\infty)$). Dodavanje djeteta $c$:</p>
<p>$$new[x \oplus y] = \max_{x, y}\bigl(cur[x] + dp[c][y]\bigr),$$</p>
<p>gdje kombiniramo samo konačne vrijednosti. To je točno zato što su odabiri u različitim podstablima neovisni, a rezultat (broj crnih) im se zbraja, dok se parnosti XOR-aju. Nakon sve djece dodamo doprinos samog vrha: $dp[v][p] = cur[p] + [A_v \oplus p = 1]$.</p>
<p>Odgovor je $\max(dp[1][0], dp[1][1])$ – korijen nema pretka pa je bilo koja parnost dopuštena.</p>
<h3>4. Provjera na primjeru</h3>
<p>Stablo $1\!-\!2$, $1\!-\!3$, $3\!-\!4$, $3\!-\!5$, boje $A = (1, 0, 0, 1, 0)$. Listovi: $dp[2] = (0, 1)$, $dp[4] = (1, 0)$, $dp[5] = (0, 1)$. Vrh $3$: spajanje $4$ i $5$ daje $cur = (\max(1+0), \max(1+1, 0+0)) = (1, 2)$; dodamo $[0 \oplus p = 1]$: $dp[3] = (1, 3)$. Korijen: spajanje $2$ i $3$: $cur[0] = \max(0+1, 1+3) = 4$, $cur[1] = \max(0+3, 1+1) = 3$; dodamo $[1 \oplus p = 1]$, što je $1$ za $p = 0$ i $0$ za $p = 1$: $dp[1] = (5, 3)$. Odgovor je $5$, u skladu s primjerom. Vrijednost $cur[0] = 4$ dolazi od $p_2 = 1, p_3 = 1$, tj. od odabira listova $2$ i $5$: crni postaju $2, 3, 4, 5$, a korijen ostaje crn jer je parnost u njegovu podstablu $0$. Ovakav ručni prolaz dobar je test da su smjer XOR-a i trenutak dodavanja $[A_v \oplus p = 1]$ ispravni.</p>
<h3>5. Složenost i implementacija</h3>
<p>Svaki vrh se točno jednom spoji sa svojim roditeljem uz $4$ kombinacije parnosti, pa je ukupno $O(N)$ vremena i $O(N)$ memorije. U kodu vrhove obrađujemo u obrnutom BFS redoslijedu (djeca prije roditelja) bez rekurzije, jer lanac od $10^5$ vrhova može srušiti rekurzivni DFS. Listove prepoznajemo kao vrhove bez djece (korijen s jednim djetetom nije list; zbog $N \ge 2$ korijen uvijek ima dijete). Nedostižne kombinacije čuvamo kao $-10^{18}$ i preskačemo ih u spajanju; vrijednosti su $\le N$, pa 64-bitni tip nema problema.</p>
''',
    'verified': r'''uzorci 3/3; 300 slučajnih malih stabala ($N \le 12$: slučajna, lančasta i zvjezdasta) protiv brute forcea koji iscrpno prolazi sve podskupove listova; 3 velika testa s $N = 10^5$ (slučajno stablo, lanac dubine $10^5$, zvijezda), najsporiji $0.03$ s.''',
},
# ---------------------------------------------------------------- B
{
    'letter': 'B', 'title': 'Magical Wallet', 'title_hr': 'Čarobni novčanik', 'slug': 'B_magical_wallet',
    'tl': '2 s', 'ml': '1024 MB',
    'statement': r'''
<p>Imaš čarobni novčanik s $X$ jena. Čarolijom u bilo kojem trenutku možeš permutirati znamenke iznosa u novčaniku (npr. $120 \to 12, 21, 102, 120, 201, 210$; vodeće nule se zanemaruju). Redom posjećuješ $N$ trgovina; u $i$-toj se prodaje proizvod za $A_i$ jena i možeš ga kupiti ako imaš barem $A_i$ jena. Koliko najviše proizvoda možeš kupiti?</p>
<h3>Ulaz</h3>
<p>$N$ i $X$ ($1 \le N \le 100$, $1 \le X < 10^4$), zatim $A_1, \dots, A_N$ ($1 \le A_i < 10^4$).</p>
<h3>Izlaz</h3>
<p>Najveći broj kupljenih proizvoda.</p>
<h3>Primjer</h3>
<p>Za $X = 120$ i cijene $142, 90$ odgovor je $2$: $120 \to 201$, kupimo za $142$ (ostaje $59$), $59 \to 95$, kupimo za $90$.</p>
''',
    'hints': [
        r'''<p>Iznos je uvijek manji od $10^4$, a stanje ovisi samo o multiskupu znamenki. DP po trgovinama s iznosom u novčaniku kao stanjem ima $100 \cdot 10^4$ stanja.</p>''',
        r'''<p>Da bi prijelazi bili jednostavni, normaliziraj stanje: uvijek pamti <em>najveći</em> broj koji se može dobiti permutacijom znamenki (on predstavlja cijelu klasu). Pri kupnji prođi sve permutacije $k$ tog broja s $k \ge A_i$.</p>''',
    ],
    'coach': [
        ('Što je zapravo „stanje” novčanika ako je čarolija besplatna i neograničena?',
         r'''
<p>Ako u novčaniku imamo $j$ jena, u svakom trenutku možemo prijeći u bilo koji broj $k$ s istim multiskupom znamenki (vodeće nule ispadaju). Dakle iznosi $120$, $201$, $12$ i ostale permutacije potpuno su zamjenjivi: sve što se može učiniti iz jednog može se i iz drugoga. Pravo stanje nije broj, nego <em>klasa</em> brojeva s istim znamenkama; najprirodniji predstavnik klase je najveći broj u njoj, $m(j)$ (znamenke silazno).</p>
'''),
        ('Zašto ne možemo jednostavno biti pohlepni – uvijek kupiti kad možemo, ili uvijek platiti najvećom permutacijom?',
         r'''
<p>Kupnja mijenja znamenke ostatka, a one određuju što ćemo moći platiti kasnije. Primjer iz zadatka: s $120$ i cijenama $142, 90$ plaćamo $142$ iz $201$ (ne iz najveće permutacije $210$!) jer ostatak $59 \to 95 \ge 90$, dok $210 - 142 = 68 \to 86 < 90$. Dakle izbor permutacije pri plaćanju i odluka „kupiti ili preskočiti” imaju posljedice na budućnost – to je klasičan signal za dinamičko programiranje po redoslijedu trgovina.</p>
'''),
        ('Koliko stanja ima DP i jesu li prijelazi dovoljno jeftini?',
         r'''
<p>Iznos je uvijek $< 10^4$ (nikad ne raste), pa ima najviše $10^4$ mogućih vrijednosti, a još manje kanonskih klasa. $dp[i][j]$ = najveći broj kupljenih proizvoda nakon $i$ trgovina s kanonskim iznosom $j$. Prijelazi iz $dp[i][j]$: preskoči trgovinu ili za svaku permutaciju $k$ znamenki broja $j$ s $k \ge A_i$ kupi i prijeđi u $m(k - A_i)$. Broj ima najviše $4$ znamenke, pa permutacija ima najviše $4! = 24$; ukupno $\le 100 \cdot 10^4 \cdot 24 = 2.4 \cdot 10^7$ operacija.</p>
'''),
        ('Gdje se lako pogriješi s vodećim nulama?',
         r'''
<p>Skup permutacija treba računati iz zapisa broja <em>bez</em> dopunjavanja nulama. Iz $120$ smijemo dobiti $12$ (nula je znamenka i ide na početak), ali iz $12$ ne smijemo dobiti $120$ – nema nule među znamenkama. Ako broj dopunimo na četiri znamenke ($0012$), lažno dobivamo $1200$ i odgovor postaje prevelik (upravo to ruši službene primjere). Zato je $m(12) = 21$, a ne $2100$.</p>
'''),
    ],
    'tips': [
        r'''Kad je neka operacija <strong>besplatna i reverzibilna</strong>, stanja koja ona povezuje su ekvivalentna: odaberi kanonskog predstavnika klase (npr. sortirane znamenke) i DP vodi samo po predstavnicima.''',
        r'''Prije nego što posumnjaš u DP, brzo isprobaj pohlepne varijante na službenim primjerima – ovdje primjer $120 \to 201$ odmah pokazuje da „plati najvećim” nije optimalno.''',
        r'''Radi s tekstualnim zapisom broja bez dopunjavanja nulama kad su vodeće nule zanemarene po tekstu zadatka; <code>std::next_permutation</code> nad sortiranim znamenkama i <code>stoi</code> zajedno rade točno to.''',
    ],
    'solution': r'''
<p>Zadatak rješavamo dinamičkim programiranjem: $dp[i][j]$ je najveći broj proizvoda koje možemo kupiti ako nakon posjeta $i$-toj trgovini u novčaniku imamo $j$ jena.</p>
<p>Radi jednostavnijih prijelaza pretpostavljamo da je iznos u novčaniku $j$ uvijek najveći mogući (najveći broj koji se može dobiti permutacijom znamenki). Neka je $p(j)$ skup brojeva koji se dobivaju permutiranjem znamenki broja $j$, a $m(j) = \max p(j)$. Prijelazi:</p>
<ul>
    <li>$dp[0][m(X)] \leftarrow 0$;</li>
    <li>$dp[i+1][j] \leftarrow dp[i][j]$;</li>
    <li>ako je $j = m(j)$: za svaki $k \in p(j)$ s $k \ge A_i$, $dp[i+1][m(k - A_i)] \leftarrow dp[i][j] + 1$.</li>
</ul>
<p>Vremenska složenost je $O(N \cdot M)$, gdje je $M = 10^4$ raspon iznosa.</p>
''',
    'detailed': r'''
<h3>1. Klase ekvivalencije iznosa</h3>
<p>Čaroliju možemo primijeniti kad god želimo i koliko god puta želimo, a ona je i reverzibilna (permutiranje unatrag). Zato su dva iznosa s istim multiskupom znamenki (nakon što se zanemare vodeće nule) potpuno ravnopravna: iz svakoga možemo besplatno doći u drugi, pa imaju identičan skup mogućih budućnosti. Prirodno stanje DP-a je stoga klasa, a kao predstavnika biramo najveći broj u klasi, $m(j)$ – znamenke sortirane silazno. Skup svih članova klase označimo $p(j)$; to su svi brojevi koji se dobiju permutiranjem znamenki broja $j$, pri čemu permutacija koja počinje nulom daje kraći broj (npr. $012 = 12$).</p>
<p>Važno: $p(j)$ računamo iz zapisa broja $j$ <em>onakvog kakav jest</em>. Broj $12$ ima znamenke $\{1, 2\}$, pa $p(12) = \{12, 21\}$; nema načina da iz njega nastane $120$, jer nula nije među znamenkama. S druge strane $p(120) \ni 12$. Ako bismo brojeve dopunjavali na četiri znamenke, iz $12$ bismo pogrešno dobili i $1200$ – takva implementacija pada već na službenim primjerima (daje $5$ umjesto $3$ i $7$ umjesto $5$).</p>
<h3>2. Zašto pohlepni pristup ne radi i zašto DP radi</h3>
<p>Odluka u trgovini $i$ (preskočiti; ili kupiti plaćajući iz neke permutacije $k$) određuje multiskup znamenki ostatka, a taj multiskup određuje što se može kupiti dalje. Primjer iz teksta ($X = 120$, cijene $142, 90$) pokazuje da nije optimalno ni platiti iz najveće permutacije ($210 - 142 = 68$, klasa $\{68, 86\}$, ne stiže do $90$), nego iz $201$ ($201 - 142 = 59$, klasa $\{59, 95\}$, $95 \ge 90$). Dakle moramo pamtiti sve dostižne klase.</p>
<p>Ključno je da je buduća vrijednost potpuno određena parom (indeks trgovine, klasa iznosa): nakon trgovine $i$ jedino što nosimo dalje je iznos u novčaniku, a iznosi iste klase su zamjenjivi. To je točno svojstvo optimalne podstrukture koje DP zahtijeva – od svih načina da se stigne u $(i, j)$ dovoljno je pamtiti onaj s najviše kupljenih proizvoda.</p>
<h3>3. Prijelazi</h3>
<p>$dp[i][j]$ = najveći broj kupljenih proizvoda nakon prvih $i$ trgovina ako je kanonski iznos $j$ ($j = m(j)$), ili $-1$ ako je nedostižno. Početno $dp[0][m(X)] = 0$. Za trgovinu $i$ s cijenom $A_i$ i za svaki dostižni $j$:</p>
<ul>
    <li><strong>preskoči:</strong> $dp[i+1][j] \leftarrow dp[i][j]$;</li>
    <li><strong>kupi:</strong> za svaki $k \in p(j)$ s $k \ge A_i$: $dp[i+1][m(k - A_i)] \leftarrow dp[i][j] + 1$.</li>
</ul>
<p>Odgovor je $\max_j dp[N][j]$. Prijelaz „kupi” enumerira <em>sve</em> permutacije, pa ne propuštamo ni jednu mogućnost; prijelaz „preskoči” pokriva odluku da ne kupimo čak i ako možemo (što je ponekad korisno – npr. sačuvati znamenke za skuplji proizvod poslije).</p>
<h3>4. Složenost</h3>
<p>Iznos nikad ne raste, pa je uvijek $< 10^4$; kanonskih klasa ima najviše $10^4$. Svaki broj ima najviše $4$ znamenke, pa $|p(j)| \le 24$. Prijelaza po trgovini je najviše $10^4 \cdot 24$, ukupno $O(N \cdot 10^4 \cdot 24) \approx 2.4 \cdot 10^7$ – daleko ispod limita. Tablice $m(\cdot)$ i $p(\cdot)$ predizračunamo jednom za sve $v < 10^4$ (za $p$ samo za kanonske $v$).</p>
<h3>5. Rubni slučajevi</h3>
<ul>
    <li>$X$ i cijene su barem $1$, ali ostatak $k - A_i$ može biti $0$; klasa $\{0\}$ je legitimno stanje (ništa se više ne može kupiti, ali preskakanje i dalje radi).</li>
    <li>Znamenke koje se ponavljaju (npr. $1121$) daju manje od $24$ različitih permutacija – u kodu ih deduplicira skup.</li>
    <li>Kanonizacija $m(\cdot)$ radi se nad zapisom bez vodećih nula: $m(120) = 210$, $m(12) = 21$, $m(0) = 0$.</li>
    <li>Provjera na primjeru: $dp[0][210] = 0$; trgovina $142$: iz $p(210) = \{12, 21, 102, 120, 201, 210\}$ dopušteni su $201$ i $210$, dajući $m(59) = 95$ i $m(68) = 86$ s vrijednošću $1$; trgovina $90$: iz $95$ kupujemo ($p(95) \ni 95 \ge 90$), $m(5) = 5$ s vrijednošću $2$; iz $86$ ne možemo. Odgovor $2$.</li>
</ul>
''',
    'verified': r'''uzorci 4/4; 300 slučajnih malih testova ($N \le 6$, iznosi do $9999$ i posebno mali iznosi radi gustih kupnji) protiv neovisnog brute forcea koji vodi skup svih točnih dostižnih iznosa (bez kanonizacije) i u svakoj trgovini isprobava sve permutacije; 3 velika testa s $N = 100$ ($<0.01$ s).''',
},
# ---------------------------------------------------------------- C
{
    'letter': 'C', 'title': 'Parallel Processing (Easy)', 'title_hr': 'Paralelna obrada (lakša verzija)', 'slug': 'C_parallel_processing_easy',
    'tl': '2 s', 'ml': '1024 MB',
    'statement': r'''
<p>Dan je monoid $(M, \oplus)$ i $4$ procesora. Treba paralelno izračunati sve prefiksne „zbrojeve” niza $A_1, \dots, A_N$ uz najmanji broj instrukcija.</p>
<p>Program koristi varijable $A[1], \dots, A[2000]$ (početno $A[i] = (i)$) te $C_1, \dots, C_4$. Jedna instrukcija ima $12$ brojeva $c_1, a_1, b_1, \dots, c_4, a_4, b_4$ iz $[1, 2000]$ i izvodi: $C_t \leftarrow \mathrm{concat}(A[a_t], A[b_t])$ za $t = 1..4$, a zatim $A[c_t] \leftarrow C_t$ za $t = 1..4$. Na kraju mora vrijediti $A[i] = (1, 2, \dots, i)$ za sve $1 \le i \le N$.</p>
<p>Ispiši program s najmanjim mogućim brojem instrukcija $L$.</p>
<h3>Ulaz</h3>
<p>$N$ ($2 \le N \le 16$).</p>
<h3>Izlaz</h3>
<p>$L$ i zatim $L$ instrukcija (svaka u $4$ retka po $3$ broja).</p>
''',
    'hints': [
        r'''<p>Jedna instrukcija najviše udvostručuje duljinu niza, pa je $L \ge \lceil \log_2 N \rceil$. No četiri procesora ne mogu u $\lceil \log_2 N \rceil$ koraka proizvesti svih $N$ prefiksa — treba prebrojati koliko se nizova može dovršiti.</p>''',
        r'''<p>Optimalne vrijednosti za $N \le 16$: $L = 1$ za $N = 2$; $2$ za $3\text{–}4$; $3$ za $5\text{–}8$; $4$ za $9\text{–}11$; $5$ za $12\text{–}13$; $6$ za $14\text{–}16$. Dovoljno je ručno ili pretraživanjem konstruirati rješenja za $N = 2, 4, 8, 11, 13, 16$ (rješenje za veći $N$ vrijedi za manji).</p>''',
    ],
    'coach': [
        ('Koje su očite donje granice za broj instrukcija $L$?',
         r'''
<p>Prva: jedno spajanje najviše udvostručuje duljinu niza, pa je nakon $L$ instrukcija svaka varijabla duga najviše $2^L$; kako treba izgraditi $A[N]$ duljine $N$, vrijedi $L \ge \lceil \log_2 N \rceil$. Druga, gruba: mora nastati $N - 1$ novih prefiksa, a instrukcija proizvodi najviše $4$ niza, pa $L \ge \lceil (N-1)/4 \rceil$. Za $N \le 8$ prva je granica jača i dostiže se klasičnom paralelnom prefiksnom shemom; za $N \ge 9$ obje su preslabe – pravi je odgovor veći.</p>
'''),
        ('Zašto četiri procesora ne mogu dovršiti jedan prefiks po procesoru po koraku? Koje intervale je uopće korisno graditi?',
         r'''
<p>Spajanjem nastaje prefiks $[1, i]$ samo iz $[1, d]$ i $[d+1, i]$, pa su korisni samo <em>intervali</em>, i to na dva načina: ili produžujemo već gotov prefiks, ili gradimo „desni komad” $[d+1, i]$ koji sam nije prefiks. Svaki desni komad duljine $\ge 2$ košta dodatna spajanja koja ne proizvode nijedan prefiks. Ako pak prefikse gradimo samo produžujući prethodni prefiks za po jedan element, oni ovise jedan o drugome u lancu i treba $N - 1$ koraka. Optimum balansira ta dva troška – to je ideja dokaza donje granice $\frac{2}{5}(N-1)$ (vidi tešku verziju D).</p>
'''),
        ('Kako iz donjih granica nastaje tablica $L(N)$ za $N \le 16$?',
         r'''
<p>$L = \max(\lceil \log_2 N \rceil, \lceil 2(N-1)/5 \rceil)$: za $N = 2$ to je $1$; $N = 3, 4$: $2$; $N = 5..8$: $3$; $N = 9, 10, 11$: $\lceil 16/5 \rceil = \dots = \lceil 20/5 \rceil = 4$; $N = 12, 13$: $5$; $N = 14, 15, 16$: $6$. To je točno tablica iz službenog rješenja. Program za veći $N$ s istim $L$ vrijedi i za manji $N$ (uvjet za $i > N$ nikome ne smeta), pa je dovoljno znati konstrukcije za $N = 2, 4, 8, 11, 13, 16$ – ili jednu opću konstrukciju koja radi za svaki $N$.</p>
'''),
        ('Kako izgleda konstrukcija koja tu granicu stvarno dostiže?',
         r'''
<p>Niz podijelimo na $L + 1$ blokova, prvi je $\{1\}$. U svakom bloku $t$ lančano računamo unutarnje prefikse $[l_t, x]$ (jedno spajanje po koraku, gotovo do koraka $t - 2$), u koraku $t - 1$ jedan procesor spoji globalni prefiks $[1, r_{t-1}]$ s cijelim blokom $[l_t, r_t]$, a ostatak bloka dovršava se kasnije spajanjima $[1, r_{t-1}] + [l_t, x]$. Ukupno spajanja je $L + 2(N - 1 - L) = 2N - 2 - L$, što stane u $4L$ slotova točno kad je $L \ge 2(N-1)/5$. Blokovi trebaju biti duljine oko $2.5$ i ne dulji od $t - 1$ (lanac mora stati u dostupne korake).</p>
'''),
        ('Kako biti siguran da je ispis ispravan kad postoji mnogo valjanih programa?',
         r'''
<p>Ne uspoređujemo s jednim „točnim” izlazom, nego napišemo <em>checker</em>: simulira sve $2000$ varijabli i $4$ procesora (sva čitanja prije svih pisanja u instrukciji), provjeri $A[i] = (1, \dots, i)$ za $i \le N$ i usporedi $L$ s formulom. Za $N \le 16$ takvu provjeru napravimo za svih $15$ vrijednosti – to je iscrpna verifikacija.</p>
'''),
    ],
    'tips': [
        r'''Kod konstruktivnih zadataka „minimalan broj koraka” prvo izvedi <strong>više neovisnih donjih granica</strong> (informacijsku poput $\log_2$, brojačku poput „koliko objekata mora nastati”) – prava vrijednost je često maksimum nekoliko takvih granica, a tablica u tekstu odaje koja gdje prevladava.''',
        r'''Rješenje za veći $N$ s istim optimumom automatski je rješenje za manji $N$: umjesto $15$ posebnih slučajeva dovoljno je nekoliko „graničnih”, ili jedna opća konstrukcija.''',
        r'''Za zadatke s više valjanih izlaza napiši checker koji doslovno simulira pravila iz teksta (uključujući redoslijed čitanja i pisanja) – to je jedini pouzdan test, a ujedno i najbrži način da uhvatiš pogrešku u redoslijedu operacija.''',
    ],
    'solution': r'''
<p>Veza između $N$ i najmanjeg broja instrukcija $L$ je sljedeća:</p>
<table>
    <tr><th>$N$</th><td>$2$</td><td>$3$–$4$</td><td>$5$–$8$</td><td>$9$–$11$</td><td>$12$–$13$</td><td>$14$–$16$</td></tr>
    <tr><th>$L$</th><td>$1$</td><td>$2$</td><td>$3$</td><td>$4$</td><td>$5$</td><td>$6$</td></tr>
</table>
<p>Zadatak se stoga može riješiti pažljivo napisanim programom za iscrpno pretraživanje koji pronalazi rješenja, ili ručnom konstrukcijom rješenja za $N = 2, 4, 8, 11, 13, 16$ (rješenje za veći $N$ ujedno je rješenje za svaki manji $N$ s istim $L$). Službeno rješenje daje i primjer programa za $N = 16$ u šest instrukcija; opća konstrukcija koja dostiže donju granicu opisana je u teškoj verziji zadatka (D).</p>
''',
    'detailed': r'''
<h3>1. Što jedna instrukcija može, a što ne može</h3>
<p>Instrukcija najprije izračuna četiri spajanja $C_t = \mathrm{concat}(A[a_t], A[b_t])$ iz <em>starih</em> vrijednosti, a tek zatim upiše rezultate. Zato unutar jedne instrukcije rezultat jednog procesora ne može biti ulaz drugom – ovisni izračuni troše zasebne korake. Cilj su nizovi $A[i] = (1, \dots, i)$, tj. intervali $[1, i]$. Ako je $\mathrm{concat}(x, y) = [1, i]$, tada je $x$ prefiks tog niza, dakle $x = [1, d]$ i $y = [d+1, i]$. Indukcijom: bilo koji niz koji ikad sudjeluje u gradnji prefiksa i sam je interval $[l, r]$. Nizove koji nisu intervali nema smisla graditi.</p>
<h3>2. Donje granice</h3>
<p><strong>Logaritamska.</strong> Duljina niza u varijabli nakon $k$ instrukcija najviše je $2^k$ (spajanje dvaju nizova duljine $\le 2^{k-1}$). Budući da $A[N]$ mora imati duljinu $N$, vrijedi $L \ge \lceil \log_2 N \rceil$.</p>
<p><strong>Brojačka, $L \ge \frac{2}{5}(N-1)$.</strong> Ovo je bit zadatka i detaljno je dokazano u rješenju teške verzije (D). Skica: gradnja prefiksa $[1, N]$ tvori binarno stablo $T$ s listovima $[1,1], \dots, [N,N]$ i $N - 1$ spajanja. Prefiksi $[1, i]$ unutar $T$ čine lanac od korijena, pa ako ih je $A$, treba $L \ge A - 1$ koraka. Preostalih $N - A$ prefiksa gradi se izvan $T$, svaki barem jednim dodatnim spajanjem, pa je ukupan broj spajanja $S \ge (N-1) + (N-A)$. Uz $L \ge S/4$ dobivamo $L \ge \max(S/4,\ 2N-2-S) \ge \frac{2}{5}(N-1)$.</p>
<p>Konačno $L(N) = \max\bigl(\lceil \log_2 N \rceil, \lceil \tfrac{2}{5}(N-1) \rceil\bigr)$, što daje tablicu iz sažetka: $1$ za $N = 2$; $2$ za $3\text{–}4$; $3$ za $5\text{–}8$; $4$ za $9\text{–}11$; $5$ za $12\text{–}13$; $6$ za $14\text{–}16$. Za $N \le 8$ dominira logaritamska granica, od $N = 9$ brojačka.</p>
<h3>3. Konstrukcija za $N \le 8$: klasična paralelna prefiksna suma</h3>
<p>Tri instrukcije (svaka „$A[c] \leftarrow A[a] + A[b]$”):</p>
<ol>
    <li>$A[2] \leftarrow A[1] + A[2]$, $A[4] \leftarrow A[3] + A[4]$, $A[6] \leftarrow A[5] + A[6]$, $A[8] \leftarrow A[7] + A[8]$ – parovi;</li>
    <li>$A[3] \leftarrow A[2] + A[3]$, $A[4] \leftarrow A[2] + A[4]$, $A[7] \leftarrow A[6] + A[7]$, $A[8] \leftarrow A[6] + A[8]$ – prefiksi unutar polovica $[1,4]$ i $[5,8]$;</li>
    <li>$A[5..8] \leftarrow A[4] + A[5..8]$ – globalni prefiks preskače preko prve polovice.</li>
</ol>
<p>Za $N < 8$ jednostavno ispustimo operacije čiji je cilj $c > N$; korak koji ostane prazan ne ispisujemo. Tako za $N = 2$ ostaje jedna instrukcija, za $N = 3, 4$ dvije, za $N = 5..8$ tri – točno $\lceil \log_2 N \rceil$.</p>
<h3>4. Konstrukcija za $N \ge 9$: blokovi</h3>
<p>Niz dijelimo na $L + 1$ blokova $[l_t, r_t]$, $t = 1, \dots, L+1$, gdje je blok $1 = \{1\}$ (već gotov). Za blok $t \ge 2$ duljine $m_t$ izvodimo tri vrste spajanja:</p>
<ul>
    <li><strong>lančana</strong> ($m_t - 1$ komada): $A[x] \leftarrow A[x-1] + A[x]$ za $x = l_t + 1, \dots, r_t$ redom, pa je $A[x] = [l_t, x]$; ovise jedno o drugome pa idu u različite korake, i moraju završiti do koraka $t - 2$;</li>
    <li><strong>prefiksno</strong> (jedno): u koraku $t - 1$: $A[r_t] \leftarrow A[r_{t-1}] + A[r_t] = [1, r_{t-1}] + [l_t, r_t] = [1, r_t]$ – globalni prefiks napreduje za točno jedan blok po koraku, pa nakon $L$ koraka stigne do $r_{L+1} = N$;</li>
    <li><strong>završna</strong> ($m_t - 1$ komada): od koraka $t - 1$ nadalje, $A[x] \leftarrow A[r_{t-1}] + A[x] = [1, x]$ za $l_t \le x < r_t$; ta spajanja ni o čemu ne ovise dalje pa ih slažemo u slobodne slotove.</li>
</ul>
<p>Ukupno spajanja: $L + 2\sum_t (m_t - 1) = L + 2(N - 1 - L) = 2N - 2 - L$. Slotova je $4L$, pa sve stane točno kad je $2N - 2 - L \le 4L$, tj. $L \ge \frac{2}{5}(N-1)$ – konstrukcija je usklađena s donjom granicom (u njoj je $A = L + 1$ i $S = 2N - 2 - L$, obje nejednakosti iz dokaza su „napete”).</p>
<p><strong>Duljine blokova.</strong> Lanac bloka $t$ mora stati u korake $1, \dots, t-2$, dakle $m_t \le t - 1$. Preostalih $N - 1$ elemenata dijelimo na $L$ blokova što ravnomjernije (duljine $\lfloor (N-1)/L \rfloor$ ili za jedan više), a višak koji krši $m_t \le t - 1$ prebacujemo u sljedeći blok. Prosječna duljina je $\approx 2.5$, što odgovara „$1$ prefiksno $+ 2(m-1)$ ostalih $= 4$ spajanja po koraku”.</p>
<p><strong>Raspored po koracima.</strong> U koraku $j$ najprije ide prefiksno spajanje bloka $j + 1$, zatim do tri lančana spajanja blokova s najranijim rokom (najmanji $t \ge j + 2$ kojemu lanac još nije gotov – „earliest deadline first”), a preostale slotove pune završna spajanja koja čekaju u redu. Prazne slotove popunimo bezopasnom operacijom $A[2000] \leftarrow A[2000] + A[2000]$ ($2000 > N$).</p>
<h3>5. Primjer: $N = 11$, $L = 4$</h3>
<p>Blokovi: $\{1\}, \{2\}, [3,4], [5,7], [8,11]$ (duljine $1, 1, 2, 3, 4$; ravnomjerna podjela $10 = 3+2+3+2$ korigirana je uvjetom $m_t \le t-1$). Instrukcije (svaki redak $c\ a\ b$ znači $A[c] \leftarrow A[a] + A[b]$):</p>
<ol>
    <li>$2\,1\,2$ (prefiks $[1,2]$), $4\,3\,4$, $6\,5\,6$, $9\,8\,9$ (lanci blokova $3, 4, 5$);</li>
    <li>$4\,2\,4$ (prefiks $[1,4]$), $7\,6\,7$, $10\,9\,10$ (lanci), $3\,2\,3$ (završno: $[1,3]$);</li>
    <li>$7\,4\,7$ (prefiks $[1,7]$), $11\,10\,11$ (lanac), $5\,4\,5$, $6\,4\,6$ (završna);</li>
    <li>$11\,7\,11$ (prefiks $[1,11]$), $8\,7\,8$, $9\,7\,9$, $10\,7\,10$ (završna).</li>
</ol>
<p>Ukupno $16 = 2 \cdot 11 - 2 - 4$ spajanja u $16$ slotova; svaki $A[i]$, $i \le 11$, na kraju je $(1, \dots, i)$.</p>
<h3>6. Provjera i složenost</h3>
<p>Budući da je valjanih programa mnogo, ispravnost provjeravamo checkerom koji simulira program po pravilima iz teksta (sva čitanja u instrukciji prije svih pisanja), provjerava sve prefikse i uspoređuje $L$ s formulom; u lakšoj verziji provjerili smo svih $15$ vrijednosti $N \in [2, 16]$, a isti kod i za svih $984$ vrijednosti teške verzije. Vrijeme izvođenja je $O(N)$; sve vrijednosti su mali cijeli brojevi.</p>
''',
    'verified': r'''uzorci 2/2 (checker; službeni $L$ jednak formuli); checkerom, koji simulira program i provjerava sve prefikse te optimalnost $L$, provjereno svih $15$ vrijednosti $N \in [2, 16]$ (300 pokretanja generatora koji ciklički prolazi kroz njih); isti kod prošao je checker i za svih $984$ vrijednosti $N \in [17, 1000]$ (zadatak D).''',
},
# ---------------------------------------------------------------- D
{
    'letter': 'D', 'title': 'Parallel Processing (Hard)', 'title_hr': 'Paralelna obrada (teža verzija)', 'slug': 'D_parallel_processing_hard',
    'tl': '2 s', 'ml': '1024 MB',
    'statement': r'''
<p>Isti zadatak kao C, ali s $17 \le N \le 1000$: koristeći $4$ procesora i instrukcije koje istodobno računaju $4$ spajanja $\mathrm{concat}(A[a_t], A[b_t])$ te ih upisuju u $A[c_t]$, postigni $A[i] = (1, \dots, i)$ za sve $i \le N$ uz najmanji broj instrukcija $L$.</p>
<h3>Ulaz</h3>
<p>$N$ ($17 \le N \le 1000$).</p>
<h3>Izlaz</h3>
<p>$L$ i zatim $L$ instrukcija, svaka u $4$ retka $c_t\ a_t\ b_t$ (brojevi iz $[1, 2000]$).</p>
''',
    'hints': [
        r'''<p>Očita donja granica je $\lceil \log_2 N \rceil$. Druga dolazi iz brojanja operacija: svaki prefiks $[1, i]$ nastaje jednim spajanjem, a spajanje $[1, i]$ ovisi o prethodno izračunatom $[1, d]$ — ta ovisnost čini lanac. Pokušaj dokazati $L \ge \frac{2}{5}(N - 1)$.</p>''',
        r'''<p>Ključ dokaza: neka $S$ bude ukupan broj spajanja ($L \ge S / 4$), a $A$ broj prefiksa $[1, i]$ koji se koriste u „stablu” izgradnje $[1, N]$ ($L \ge A - 1$ zbog lanca ovisnosti). Pokaži $(N - 1) + (N - A) \le S$ i kombiniraj.</p>''',
        r'''<p>Konstrukcija: podijeli niz na $L + 1$ blokova. Za svaki blok računaj njegove unutarnje prefikse, a paralelno „vuci” globalni prefiks do kraja bloka — jedan korak zaostatka po bloku. Blokove čini što duljima dok god globalni prefiks stiže napredovati.</p>''',
    ],
    'coach': [
        ('Koje nizove je uopće korisno graditi i kako izgleda „povijest” prefiksa $[1, N]$?',
         r'''
<p>Ako je $\mathrm{concat}(x, y)$ interval $[l, r]$, onda je $x = [l, d]$ i $y = [d+1, r]$ – dakle sve što sudjeluje u gradnji prefiksa i samo je interval. Ako još dopustimo (kao relaksaciju koja može samo pomoći) da svi izgrađeni nizovi ostaju dostupni i da se svaki interval gradi najviše jednom, gradnja $[1, N]$ postaje binarno stablo $T$: listovi su $[i, i]$, svaki unutarnji čvor $[l, r]$ ima djecu $[l, d]$ i $[d+1, r]$. Ono ima $N - 1$ unutarnjih čvorova, dakle $N - 1$ spajanja, i svi su mu intervali međusobno ugniježđeni ili disjunktni.</p>
'''),
        ('Zašto ne možemo jednostavno paralelizirati – koja je veličina koja mora rasti sekvencijalno?',
         r'''
<p>Prefiksi $[1, i]$ koji se nalaze u $T$ čine lanac od korijena prema listu $[1, 1]$: roditelj prefiksa je opet prefiks (sadrži ga i počinje s $1$). Svaki se prefiks u lancu gradi iz prethodnog, pa se gradi u strogo kasnijem koraku. Ako lanac ima $A$ članova, treba barem $A - 1$ koraka: $L \ge A - 1$. Dugačak lanac znači malo posla izvan $T$, ali mnogo sekvencijalnih koraka.</p>
'''),
        ('Što se događa s prefiksima koji nisu u $T$ i kako to kombinirati u jednu nejednakost?',
         r'''
<p>Svih $N$ prefiksa mora nastati. $A$ ih je u $T$ (uključujući list $[1,1]$), a preostalih $N - A$ nije – svaki od njih zahtijeva vlastito spajanje koje nije među $N - 1$ spajanja stabla $T$. Ukupan broj spajanja $S$ stoga zadovoljava $S \ge (N - 1) + (N - A)$, tj. $A \ge 2N - 1 - S$. Kombiniramo s $L \ge A - 1 \ge 2N - 2 - S$ i s očitim $L \ge S/4$ (četiri spajanja po instrukciji). Minimum od $\max(S/4,\ 2N-2-S)$ po $S$ postiže se kad su jednaki, $S = \frac{8(N-1)}{5}$, i iznosi $\frac{2}{5}(N-1)$.</p>
'''),
        ('Kako konstruirati program koji tu granicu dostiže, tj. ima točno $L + 1$ prefiksa u lancu i točno $2N - 2 - L$ spajanja?',
         r'''
<p>Podijelimo niz na $L + 1$ blokova, prvi je $\{1\}$. Lanac prefiksa u $T$ neka bude točno „po jedan blok po koraku”: u koraku $t - 1$ spajamo $[1, r_{t-1}]$ s cijelim blokom $[l_t, r_t]$. Da bi blok bio gotov, unutar njega prethodno lančano gradimo $[l_t, x]$ ($m_t - 1$ spajanja, jedno po koraku, do koraka $t-2$), a nakon što je globalni prefiks stigao do $r_{t-1}$, elemente $x < r_t$ dovršimo kao $[1, r_{t-1}] + [l_t, x]$ (još $m_t - 1$ spajanja). Ukupno $L + 2(N - 1 - L) = 2N - 2 - L \le 4L$ točno kad je $L \ge \frac{2}{5}(N-1)$.</p>
'''),
        ('Kako odabrati duljine blokova i rasporediti spajanja tako da svi rokovi budu ispunjeni?',
         r'''
<p>Lanac bloka $t$ mora stati u korake $1..t-2$, pa $m_t \le t - 1$; s druge strane prosječna duljina mora biti $\frac{N-1}{L} \approx 2.5$. Zato duljine dijelimo što ravnomjernije, a višak s početka (gdje je ograničenje $t - 1$ malo) guramo prema kraju. U svakom koraku prvo ide prefiksno spajanje, zatim lančana spajanja blokova s najbližim rokom, a slobodni slotovi pune se završnim spajanjima koja čekaju. Umjesto općeg dokaza da raspored uvijek uspijeva, ispravnost za svaki $N \le 1000$ potvrđujemo checkerom koji simulira program.</p>
'''),
    ],
    'tips': [
        r'''Donje granice tipa „kritični put” ($L \ge$ duljina lanca ovisnosti) i „ukupni rad” ($L \ge$ posao$/$broj procesora) često se <strong>ne mogu istodobno napeti</strong>: izrazi obje kroz istu pomoćnu veličinu (ovdje $S$) i minimiziraj njihov maksimum.''',
        r'''Relaksacije koje protivniku daju više slobode (bez prepisivanja varijabli, sve izgrađeno ostaje dostupno) legitimno su sredstvo za donje granice – bound koji vrijedi u lakšem modelu vrijedi i u pravom.''',
        r'''Kad konstrukcija dostiže granicu, provjeri da su sve nejednakosti iz dokaza jednakosti u tvojoj konstrukciji – to je odličan „sanity check” da nisi ništa prebrojao krivo.''',
        r'''Raspoređivanje poslova s rokovima na fiksan broj strojeva: pravilo „najraniji rok prvi” (EDF) je prirodni pohlepni izbor; kad je teško dokazati, iscrpno simuliraj sve dopuštene ulaze (ovdje ih je samo $984$).''',
    ],
    'solution': r'''
<p>Zaključak: najmanji broj instrukcija je</p>
<p>$$L = \max\!\left( \left\lceil \log_2 N \right\rceil,\ \left\lceil \tfrac{2}{5}(N - 1) \right\rceil \right).$$</p>
<h3>Donja granica 1: $\log_2 N$</h3>
<p>Slijedi iz činjenice da niz izgrađen u $L$ instrukcija ima duljinu najviše $2^L$.</p>
<h3>Donja granica 2: $\frac{2}{5}(N-1)$</h3>
<p>Pretpostavimo $N \ge 9$.</p>
<ul>
    <li>Nema smisla graditi nizove koji nisu oblika $(l, l+1, \dots, r)$.</li>
    <li>Olabavimo uvjete i pretpostavimo da se svi ranije izgrađeni nizovi mogu koristiti bez prepisivanja varijabli.</li>
    <li>Nema smisla isti interval graditi više puta.</li>
    <li>Budući da se svaki interval gradi samo jednom, za interval $[l, r]$ postoji jedinstveno $d$ ($l \le d < r$) takvo da $[l, d] + [d+1, r]$ daje $[l, r]$.</li>
    <li>Graf „koji se interval gradi iz kojih” ima strukturu binarnih stabala s korijenima $[1,1], [1,2], \dots, [1,N]$.</li>
    <li>Uzmemo li samo dio potreban za izgradnju $[1, N]$, dobivamo binarno stablo $T$ s $2N-1$ vrhova i $2N-2$ bridova koje sadrži $N-1$ operacija $\oplus$.</li>
    <li>Gledajući $T$ od korijena nadolje, ono ponavljano dijeli interval na dva dijela; stoga su svaka dva intervala iz $T$ ili disjunktna ili ugniježđena.</li>
    <li>Fiksirajmo ukupan broj operacija $\oplus$ na $S$; tada $L \ge S/4$.</li>
    <li>Neka je $A$ broj vrhova u $T$ oblika $[1, i]$. Oni ovise o prethodnim rezultatima, pa $L \ge A - 1$. (Kad bismo koristili rezultat stariji od dva koraka, u $T$ bi postojala dva intervala koja se sijeku, a nisu ugniježđena.)</li>
    <li>Za izračun $T$ treba $N-1$ operacija, a za vrhove izvan $T$ još barem $N - A$, pa $(N-1) + (N-A) \le S$.</li>
    <li>Odatle $A \ge 2N-1-S$ i $L \ge 2N-2-S$.</li>
    <li>Dakle $L \ge \max\!\left(\tfrac{S}{4},\ 2N-2-S\right) \ge \tfrac{2}{5}(N-1)$.</li>
</ul>
<h3>Dostizanje granice $L = \lceil \frac{2}{5}(N-1) \rceil$</h3>
<p>Ideja: podijelimo niz $A_1, \dots, A_N$ na $L+1$ blokova. Zatim računamo prefiksne zbrojeve unutar svakog bloka i istodobno prefiksni zbroj po cijelim blokovima. Budući da blokova ima $L + 1$, računanje prefiksa po blokovima mora napredovati za jedan blok u svakoj instrukciji.</p>
<p>Prema tome dijelimo blokove: pazeći da prefiks po blokovima napreduje u svakom koraku, svaki blok činimo što duljim. Kad su blokovi dovoljno dugi, umjesto daljnjeg produljivanja blokova izračunamo preostali dio. Time se dostiže donja granica od $\lceil \frac{2}{5}(N-1) \rceil$ instrukcija.</p>
''',
    'detailed': r'''
<h3>1. Model i pojednostavljenja</h3>
<p>Instrukcija najprije izračuna četiri spajanja iz starih vrijednosti pa upiše rezultate, dakle ovisna spajanja idu u različite korake. Cilj su intervali $[1, i]$ za $i \le N$. Ako je $\mathrm{concat}(x, y) = [l, r]$, tada je $x$ prefiks pa $x = [l, d]$, $y = [d+1, r]$; indukcijom, samo intervali ikad sudjeluju u gradnji prefiksa i ostale nizove ne gradimo.</p>
<p>Za donju granicu dopuštamo protivniku više nego što pravila daju: (i) izgrađeni nizovi nikad se ne gube (nema prepisivanja), (ii) svaki interval gradi se najviše jednom (drugo građenje istog intervala uvijek se može izbaciti). Svaka donja granica u ovom lakšem modelu vrijedi i za pravi model.</p>
<h3>2. Stablo $T$ gradnje prefiksa $[1, N]$</h3>
<p>Za svaki izgrađeni interval $[l, r]$ s $l < r$ postoji jedinstveni $d$ takav da je nastao kao $[l, d] + [d+1, r]$. Graf „iz čega je što nastalo” je stoga skup binarnih stabala. Uzmimo samo dio potreban za $[1, N]$ i nazovimo ga $T$: korijen $[1, N]$, listovi su singletoni $[i, i]$ (početne vrijednosti), svaki unutarnji čvor $[l, r]$ ima djecu $[l, d]$ i $[d+1, r]$. Puno binarno stablo s $N$ listova ima $N - 1$ unutarnjih čvorova, dakle $T$ sadrži točno $N - 1$ spajanja. Kako svaki čvor dijeli svoj interval na dva dijela, svaka dva intervala u $T$ su ili disjunktna ili ugniježđena.</p>
<h3>3. Lanac prefiksa u $T$</h3>
<p>Neka je $A$ broj čvorova u $T$ oblika $[1, i]$. Ako je $[1, i]$ u $T$ i $i < N$, njegov roditelj je interval koji ga sadrži i stoga počinje s $1$ – opet prefiks. Dakle prefiksi u $T$ čine lanac $[1, N] = [1, i_A] \supset [1, i_{A-1}] \supset \dots \supset [1, i_1] = [1, 1]$, i $[1, i_{k+1}]$ nastaje spajanjem $[1, i_k] + [i_k + 1, i_{k+1}]$. Svaki član lanca gradi se u strogo kasnijem koraku od prethodnog, pa program ima barem $A - 1$ instrukcija:</p>
<p>$$L \ge A - 1.$$</p>
<h3>4. Brojanje spajanja</h3>
<p>Svaki od $N$ prefiksa mora biti izgrađen (za $i = 1$ je već tu). $A$ ih je u $T$, a $N - A$ nije. Prefiks izvan $T$ nastaje spajanjem koje nije nijedno od $N - 1$ spajanja stabla $T$ (ta proizvode točno unutarnje čvorove $T$-a). Zato je ukupan broj spajanja $S \ge (N - 1) + (N - A)$, odnosno $A \ge 2N - 1 - S$, pa</p>
<p>$$L \ge A - 1 \ge 2N - 2 - S.$$</p>
<p>S druge strane, svaka instrukcija izvodi najviše četiri spajanja, pa $L \ge S/4$. Dakle</p>
<p>$$L \ge \max\Bigl(\frac{S}{4},\ 2N - 2 - S\Bigr) \ge \frac{2}{5}(N-1),$$</p>
<p>jer je maksimum najmanji kad su izrazi jednaki: $S/4 = 2N - 2 - S \iff S = \frac{8(N-1)}{5}$, a tada oba iznose $\frac{2(N-1)}{5}$. Zajedno s očitom granicom $L \ge \lceil \log_2 N \rceil$ (duljina niza najviše se udvostručuje po koraku) dobivamo</p>
<p>$$L \ge \max\Bigl(\lceil \log_2 N \rceil,\ \Bigl\lceil \tfrac{2}{5}(N-1) \Bigr\rceil\Bigr).$$</p>
<p>Za $N \ge 9$ (kao i za sve $N \ge 17$ u ovoj verziji) veća je druga granica: $\lceil 2 \cdot 16/5 \rceil = 7 > 5$ za $N = 17$, a razlika dalje samo raste.</p>
<h3>5. Konstrukcija koja granicu dostiže</h3>
<p>Ideja: napraviti da su sve nejednakosti iz dokaza jednakosti. Lanac prefiksa u $T$ neka ima točno $L + 1$ članova (jedan po koraku), a ukupno spajanja neka bude točno $2N - 2 - L$.</p>
<p>Niz podijelimo na $L + 1$ uzastopnih blokova $[l_t, r_t]$, $t = 1, \dots, L + 1$, uz $l_1 = r_1 = 1$ i $r_{L+1} = N$. Za blok $t \ge 2$ duljine $m_t = r_t - l_t + 1$ izvodimo:</p>
<ul>
    <li><strong>Lančana spajanja</strong> ($m_t - 1$): $A[x] \leftarrow A[x - 1] + A[x]$ za $x = l_t + 1, \dots, r_t$ redom. Nakon njih $A[x] = [l_t, x]$. Ovise jedno o drugome, pa svako ide u zaseban korak, i sva moraju završiti do koraka $t - 2$.</li>
    <li><strong>Prefiksno spajanje</strong> (1), u koraku $t - 1$: $A[r_t] \leftarrow A[r_{t-1}] + A[r_t]$. Induktivno je $A[r_{t-1}] = [1, r_{t-1}]$ od koraka $t - 2$, a $A[r_t] = [l_t, r_t]$ nakon lanca, pa dobivamo $[1, r_t]$. U koraku $L$ tako nastaje $[1, r_{L+1}] = [1, N]$.</li>
    <li><strong>Završna spajanja</strong> ($m_t - 1$), od koraka $t - 1$ nadalje: $A[x] \leftarrow A[r_{t-1}] + A[x] = [1, r_{t-1}] + [l_t, x] = [1, x]$ za $l_t \le x < r_t$. Ona ništa dalje ne blokiraju.</li>
</ul>
<p>Svaki prefiks nastaje točno jednom: $[1, r_t]$ prefiksnim spajanjem, ostali završnim. Broj spajanja je $L + 2\sum_{t \ge 2}(m_t - 1) = L + 2(N - 1 - L) = 2N - 2 - L$, a slotova je $4L$; $2N - 2 - L \le 4L \iff L \ge \frac{2}{5}(N-1)$. Dakle za $L = \lceil \frac{2}{5}(N-1) \rceil$ posao stane u slotove.</p>
<h3>6. Duljine blokova i raspored</h3>
<p><strong>Ograničenje na duljine.</strong> Lanac bloka $t$ ima $m_t - 1$ sekvencijalnih spajanja koja moraju stati u korake $1, \dots, t - 2$, pa je nužno $m_t \le t - 1$ (posebno $m_2 = 1$). Preostalih $N - 1$ elemenata dijelimo na blokove $2, \dots, L+1$ što ravnomjernije (duljine $\lfloor \frac{N-1}{L} \rfloor$ ili za jedan veće, s viškom raspoređenim jednoliko), a zatim za $t = 2, 3, \dots$ redom višak $m_t - (t - 1)$ prebacujemo u blok $t + 1$. Kako je $\sum_{t=2}^{L+1} (t-1) = \frac{L(L+1)}{2} \ge N - 1$ za sve $N \ge 9$ s ovim $L$, uvijek ima mjesta; provjerom za sve $N \le 1000$ potvrđeno je da tada i posljednji blok zadovoljava $m_{L+1} \le L$.</p>
<p><strong>Raspored unutar koraka $j$.</strong> (1) Prefiksno spajanje bloka $j + 1$. (2) Do tri lančana spajanja: među blokovima $t \ge j + 2$ kojima lanac nije gotov uzimamo one s najmanjim $t$ (najbliži rok), po jedno spajanje po bloku (sljedeći element lanca). (3) Preostale slotove pune završna spajanja iz reda čekanja (blok $t$ stavlja svojih $m_t - 1$ završnih spajanja u red u koraku $t - 1$). Prazne slotove ispunjavamo bezopasnim $A[2000] \leftarrow A[2000] + A[2000]$ (indeks $2000 > N$ ne utječe na rezultat).</p>
<p>Zašto to uspijeva: prosječna duljina bloka je $\approx 2.5$, pa blok u prosjeku treba $\approx 1.5$ lančanih spajanja, a u svakom koraku imamo tri slota za lance blokova čiji su rokovi u budućnosti – kapacitet je dovoljan, a EDF pravilo osigurava da se ranije rokove ne propušta zbog kasnijih. Umjesto formalnog dokaza za sve $N$, ispravnost smo utvrdili iscrpno: checker simulira program za svaki $N \in [17, 1000]$ (i $[2, 16]$ za lakšu verziju).</p>
<h3>7. Primjer: $N = 11$, $L = 4$ (ista shema vrijedi za veliki $N$)</h3>
<p>Blokovi $\{1\}, \{2\}, [3,4], [5,7], [8,11]$. Korak 1: $[1,2]$; lanci $A[4] = [3,4]$, $A[6] = [5,6]$, $A[9] = [8,9]$. Korak 2: $[1,4] = [1,2] + [3,4]$; lanci $A[7] = [5,7]$, $A[10] = [8,10]$; završno $A[3] = [1,2] + [3]$. Korak 3: $[1,7] = [1,4] + [5,7]$; lanac $A[11] = [8,11]$; završna $A[5], A[6] = [1,4] + [5,\cdot]$. Korak 4: $[1,11] = [1,7] + [8,11]$; završna $A[8], A[9], A[10] = [1,7] + [8, \cdot]$. Ukupno $16 = 2 \cdot 11 - 2 - 4$ spajanja u $16$ slotova.</p>
<h3>8. Složenost i provjera</h3>
<p>Konstrukcija je $O(N)$ (svako spajanje $O(1)$, redova čekanja $O(N)$). Izlaz ima $4L + 1 \le 1601$ redaka. Kako je valjanih programa mnogo, verifikacija ide checkerom koji doslovno simulira $2000$ varijabli i redoslijed „sva čitanja, pa sva pisanja”, provjerava $A[i] = (1..i)$ za $i \le N$ i uspoređuje $L$ s formulom $\max(\lceil \log_2 N \rceil, \lceil 2(N-1)/5 \rceil)$.</p>
''',
    'verified': r'''zadatak nema službenih primjera; checkerom koji simulira program (sva čitanja pa sva pisanja), provjerava sve prefikse i optimalnost $L$ prošlo je svih $984$ vrijednosti $N \in [17, 1000]$ (generator ih ciklički prolazi) te 3 velika testa s $N$ između $995$ i $1000$ ($<0.01$ s); isti kod prošao je i oba službena primjera lakše verzije C.''',
},
# ---------------------------------------------------------------- E
{
    'letter': 'E', 'title': 'Five Med Sum', 'title_hr': 'Zbroj medijana petorki', 'slug': 'E_five_med_sum',
    'tl': '2 s', 'ml': '1024 MB',
    'statement': r'''
<p>Dano je pet nizova $A, B, C, D, E$ duljine $N$. Izračunaj</p>
<p>$$\sum_{i=1}^{N} \sum_{j=1}^{N} \sum_{k=1}^{N} \sum_{l=1}^{N} \sum_{m=1}^{N} \mathrm{med}(A_i, B_j, C_k, D_l, E_m) \pmod{998244353},$$</p>
<p>gdje je $\mathrm{med}$ medijan pet brojeva.</p>
<h3>Ulaz</h3>
<p>$N$ ($1 \le N \le 10^5$) i pet redaka s po $N$ brojeva iz $[0, 998244353)$.</p>
<h3>Izlaz</h3>
<p>Traženi zbroj.</p>
''',
    'hints': [
        r'''<p>Umjesto po petorkama, računaj doprinos svakog elementa: koliko je puta on medijan? Sortiraj svih $5N$ brojeva zajedno s oznakom niza iz kojeg dolaze.</p>''',
        r'''<p>Element na poziciji $k$ sortiranog niza je medijan petorke ako su točno dva elementa petorke ispred njega, a dva iza — i pet oznaka mora biti različitih. Enumeriraj koje dvije oznake su „ispred” ($\binom{4}{2} = 6$ mogućnosti) i koristi prefiksne brojače po oznakama.</p>''',
    ],
    'coach': [
        ('Zbroj po $N^5$ petorki je nedostižan – što možemo zbrajati umjesto po petorkama?',
         r'''
<p>Po <em>vrijednostima</em>. Svaka petorka ima točno jedan medijan, pa je $\sum \mathrm{med} = \sum_{x} x \cdot (\text{broj petorki kojima je } x \text{ medijan})$, gdje $x$ prolazi svih $5N$ elemenata. To je standardna zamjena poretka zbrajanja („contribution technique”): umjesto vrijednosti po objektu brojimo objekte po vrijednosti. Ostaje pitanje kako za pojedini element brzo izbrojati petorke kojima je medijan.</p>
'''),
        ('Kad je element $x$ iz niza $t$ medijan petorke $(a, b, c, d, e)$?',
         r'''
<p>Petorka uzima po jedan element iz svakog niza; $x$ je treći po veličini točno kad su dva od preostala četiri elementa manja od $x$, a dva veća. Ako sve elemente sortiramo zajedno (uz oznaku niza), „manji” znači „lijevo od $x$ u sortiranom poretku”, a „veći” znači „desno”. Za svaki od preostala četiri niza dakle biramo element lijevo ili desno, s uvjetom da su točno dva lijevo.</p>
'''),
        ('Što s jednakim vrijednostima – je li „lijevo/desno” dobro definirano?',
         r'''
<p>Ako sortirani poredak fiksiramo (jednake vrijednosti poredamo proizvoljno, ali jednom zauvijek), svaka petorka ima točno jednog „trećeg po poretku” i on ima vrijednost medijana – medijan kao vrijednost ne ovisi o tome kako smo razbili neodlučnost među jednakima. Zato svaku petorku brojimo točno jednom, a pribrajamo joj ispravnu vrijednost. Bez fiksiranja poretka petorka s jednakim vrijednostima brojila bi se više puta.</p>
'''),
        ('Kako broj načina izraziti tako da bude $O(1)$ po elementu?',
         r'''
<p>Neka je $pre_s$ broj elemenata niza $s$ lijevo od trenutnog položaja, a $suf_s = N - pre_s - [s = t]$ broj desno (za $s \ne t$ to je $N - pre_s$). Biramo par nizova $\{p, q\}$ koji daju manje elemente ($\binom{4}{2} = 6$ izbora), a ostala dva $\{r, u\}$ daju veće: broj petorki je $pre_p \, pre_q \, suf_r \, suf_u$. Zbroj po $6$ izbora, pomnožen s vrijednošću, je doprinos elementa. Prolazeći sortirani niz slijeva, brojači $pre_s$ ažuriraju se u $O(1)$.</p>
'''),
        ('Koliko to košta i gdje vreba prelijevanje?',
         r'''
<p>Sortiranje $5N$ elemenata: $O(N \log N)$; prolaz: $5N \cdot 6$ umnožaka – $O(N)$. Umnošci su reda $N^4 \le 10^{20}$, što ne stane u 64 bita, pa svaki faktor reduciramo modulo $998244353$ i množimo postupno; vrijednosti elemenata već su $< 998244353$.</p>
'''),
    ],
    'tips': [
        r'''<strong>Zbroj po uređenim skupovima = zbroj doprinosa po elementima.</strong> Kad se traži zbroj minimuma/maksimuma/medijana po svim podskupovima ili $k$-torkama, sortiraj i za svaki element prebroji u koliko je objekata on „taj” element.''',
        r'''Jednake vrijednosti riješi jednim potezom: fiksiraj strogi totalni poredak (npr. po vrijednosti pa po indeksu) i broji „po poretku”, ne „po vrijednosti”. Tada svaki objekt ima jedinstvenog predstavnika.''',
        r'''Kad su faktori umnoška veliki brojači ($N \le 10^5$, četiri faktora), reduciraj svaki modulo $p$ prije množenja – $N^4$ prelijeva 64 bita.''',
    ],
    'solution': r'''
<p>Trebamo prebrojati koliko se puta svaka vrijednost pojavljuje kao medijan.</p>
<p>Najprije sortiramo svih $5N$ brojeva zajedno s oznakama koje govore iz kojeg od pet nizova dolaze; neka je $F = ((F_1, t_1), \dots, (F_{5N}, t_{5N}))$ sortirani niz, gdje je $t_i$ oznaka. Za svaki $k = 1, \dots, 5N$ trebamo prebrojati četvorke $(i, j, l, m)$ takve da je $1 \le i < j < k < l < m \le 5N$ i $\{t_i, t_j, t_k, t_l, t_m\} = \{A, B, C, D, E\}$. To možemo izračunati u $O(1)$ po $k$ enumeracijom svih parova $\{t_i, t_j\}$ i korištenjem prefiksnih zbrojeva (brojača po oznakama).</p>
<p>Vremenska složenost je $O(N \log N)$.</p>
''',
    'detailed': r'''
<h3>1. Prijelaz na doprinose</h3>
<p>Traži se $\sum \mathrm{med}(a, b, c, d, e)$ po svim $N^5$ petorkama s po jednim elementom iz svakog od pet nizova. Svaka petorka ima točno jedan medijan (treći po veličini), pa možemo pisati</p>
<p>$$\sum_{\text{petorke}} \mathrm{med} = \sum_{x} x \cdot c(x),$$</p>
<p>gdje $x$ prolazi svih $5N$ elemenata (kao <em>pozicija</em>, ne kao vrijednost – vidi točku 2), a $c(x)$ je broj petorki kojima je $x$ medijan. Time se problem svodi na računanje $c(x)$.</p>
<h3>2. Fiksiranje poretka i jednake vrijednosti</h3>
<p>Sortirajmo svih $5N$ parova (vrijednost, oznaka niza) leksikografski; jednake vrijednosti dobivaju neki fiksan redoslijed. Neka je $F = ((F_1, t_1), \dots, (F_{5N}, t_{5N}))$ taj poredak. Za petorku s elementima na pozicijama $i_1 < i_2 < i_3 < i_4 < i_5$ (jedna iz svakog niza) definiramo njezina „predstavnika” kao poziciju $i_3$. Vrijednost $F_{i_3}$ jest medijan petorke: tri su elementa (pozicije $i_1, i_2, i_3$) s vrijednošću $\le F_{i_3}$ i tri (pozicije $i_3, i_4, i_5$) s vrijednošću $\ge F_{i_3}$, što je definicija medijana pet brojeva – i to bez obzira na to kako su jednake vrijednosti poredane. Svaka petorka ima točno jednog predstavnika, pa je</p>
<p>$$\sum_{\text{petorke}} \mathrm{med} = \sum_{k=1}^{5N} F_k \cdot c(k), \qquad c(k) = \#\{\text{petorke s predstavnikom } k\}.$$</p>
<p>Ovo je ključno: brojimo po pozicijama u fiksnom poretku, a ne po vrijednostima, pa nema dvostrukog brojanja među jednakim elementima.</p>
<h3>3. Formula za $c(k)$</h3>
<p>Petorka s predstavnikom $k$ (oznaka niza $t = t_k$) sastoji se od $F_k$ i po jednog elementa iz preostala četiri niza, od kojih su točno dva na pozicijama $< k$, a dva na pozicijama $> k$. Označimo za niz $s$: $pre_s(k)$ = broj elemenata niza $s$ na pozicijama $< k$, $suf_s(k)$ = broj na pozicijama $> k$; za $s \ne t$ je $suf_s(k) = N - pre_s(k)$. Odabir koje dvije oznake $\{p, q\} \subset \{A,B,C,D,E\} \setminus \{t\}$ daju „lijeve” elemente ima $\binom{4}{2} = 6$ mogućnosti, preostale dvije $\{r, u\}$ daju „desne”, a izbori su neovisni:</p>
<p>$$c(k) = \sum_{\{p, q\}} pre_p(k) \cdot pre_q(k) \cdot suf_r(k) \cdot suf_u(k).$$</p>
<p>Različiti izbori $\{p, q\}$ daju disjunktne skupove petorki (razlikuju se po tome koji su nizovi lijevo), pa je zbroj točan.</p>
<h3>4. Algoritam</h3>
<ol>
    <li>Učitaj pet nizova kao parove (vrijednost, oznaka), sortiraj svih $5N$ parova.</li>
    <li>Održavaj brojače $pre_0, \dots, pre_4$ (početno $0$). Prolazi $k = 1, \dots, 5N$: izračunaj $c(k)$ po formuli (6 članova, svaki po 4 faktora), pribroji $F_k \cdot c(k)$ odgovoru, zatim povećaj $pre_{t_k}$.</li>
    <li>Ispiši odgovor modulo $998244353$.</li>
</ol>
<h3>5. Složenost i tehnički detalji</h3>
<p>Sortiranje $O(N \log N)$, prolaz $O(N)$ s konstantom $6 \cdot 4$. Brojači su do $N = 10^5$, pa umnožak četiriju faktora doseže $10^{20}$ i prelijeva 64-bitni tip; zato svaki faktor reduciramo modulo $p$ prije množenja i množimo postupno uz redukciju. Vrijednosti elemenata su $< p$, pa $F_k \cdot c(k)$ stane u 64 bita nakon redukcije $c(k)$. Rubni slučaj $N = 1$: samo jedna petorka, algoritam daje točno njezin medijan jer je $pre$ i $suf$ za sve nizove $0$ ili $1$ na pravim mjestima. Nule među vrijednostima ne stvaraju probleme (doprinos im je $0$, ali i dalje ispravno brojimo petorke u kojima su lijevo/desno).</p>
<h3>6. Provjera na malom primjeru</h3>
<p>$N = 1$, nizovi $(3), (1), (2), (5), (4)$. Sortirano: $1(B), 2(C), 3(A), 4(E), 5(D)$. Za $k = 3$ (vrijednost $3$, niz $A$): lijevo su $B, C$ ($pre = 1$), desno $D, E$ ($suf = 1$); jedini izbor $\{p,q\} = \{B, C\}$ daje $1$, ostali izbori imaju neki $pre = 0$ ili $suf = 0$. Ostale pozicije imaju $c = 0$. Odgovor $3$ – medijan jedine petorke.</p>
''',
    'verified': r'''uzorci 2/2; 300 slučajnih malih testova ($N \le 5$, vrijednosti iz malog raspona radi mnogo jednakih elemenata, te iz punog raspona) protiv brute forcea koji prolazi svih $N^5$ petorki; 3 velika testa s $N = 10^5$ (uključujući vrijednosti samo iz $\{0,1,2,3\}$), najsporiji $0.09$ s.''',
},
# ---------------------------------------------------------------- F
{
    'letter': 'F', 'title': 'Forestry', 'title_hr': 'Šumarstvo', 'slug': 'F_forestry',
    'tl': '4 s', 'ml': '1024 MB',
    'statement': r'''
<p>Dano je stablo $T$ s $N$ vrhova; na vrhu $v$ piše broj $A_v$. Za svaki od $2^{N-1}$ podskupova bridova definiramo rezultat: ukloni neodabrane bridove i zbroji minimume $A$ po komponentama povezanosti. Izračunaj zbroj rezultata po svim podskupovima modulo $998244353$.</p>
<h3>Ulaz</h3>
<p>$N$ ($2 \le N \le 3 \cdot 10^5$), zatim $A_1, \dots, A_N$ ($1 \le A_i \le 10^9$) i $N - 1$ bridova.</p>
<h3>Izlaz</h3>
<p>Traženi zbroj.</p>
<h3>Primjer</h3>
<p>Za stablo s bridovima $1\!-\!2, 2\!-\!4, 3\!-\!2$ i $A = (1, 2, 3, 4)$ odgovor je $44$.</p>
''',
    'hints': [
        r'''<p>Preformuliraj: svaki brid neovisno reži s vjerojatnošću $1/2$; traži se očekivani rezultat pomnožen s $2^{N-1}$. Očekivanje je linearno po komponentama.</p>''',
        r'''<p>Ukorijeni stablo. Za vrh $v$ definiraj $dp[v][x]$ = vjerojatnost da komponenta koja sadrži $v$ (unutar podstabla) ima minimum $x$. Vrijednosti $x$ koje imaju vjerojatnost $\ne 0$ su samo vrijednosti vrhova podstabla — pamti samo njih.</p>''',
        r'''<p>Spajanje dvaju djece s prefiksnim zbrojevima traje $O(size(c_1) + size(c_2))$; s više djece spajaj u parovima ili koristi segment tree merge / small-to-large da bi ukupno bilo $O(N \log N)$.</p>''',
    ],
    'coach': [
        ('Zbroj po $2^{N-1}$ podskupova bridova – po čemu možemo zbrajati umjesto po podskupovima?',
         r'''
<p>Po komponentama. Rezultat podskupa je zbroj minimuma po komponentama, pa je ukupni zbroj jednak $\sum_C \min(C) \cdot \#\{\text{podskupovi u kojima je } C \text{ komponenta}\}$, gdje $C$ prolazi sve <em>povezane</em> podskupove vrhova. Skup $C$ je komponenta točno kad su svi bridovi unutar $C$ zadržani, a svi bridovi koji izlaze iz $C$ prerezani; ostali bridovi su slobodni. To daje $2^{N-2} \prod_{u \in C} 2^{1 - \deg u}$ – umnožak po vrhovima, što je ključ za DP na stablu.</p>
'''),
        ('Kako se riješiti faktora $\min(C)$, koji ovisi o cijelom skupu, a ne o pojedinom vrhu?',
         r'''
<p>Pragovima: za padajuće različite vrijednosti $v_1 > v_2 > \dots > v_k$ (i $v_{k+1} = 0$) vrijedi $\min(C) = \sum_j (v_j - v_{j+1}) \, [\min(C) \ge v_j]$ – teleskopski zbroj. Uvjet $\min(C) \ge v_j$ znači da $C$ leži u skupu „živih” vrhova $\{u : A_u \ge v_j\}$. Dakle $\sum_C \min(C) \prod w_u = \sum_j (v_j - v_{j+1}) \, G_j$, gdje je $G_j$ zbroj težina povezanih podskupova živih vrhova. Vrhove oživljavamo u padajućem redoslijedu po $A$ i trebamo $G$ nakon svake grupe.</p>
'''),
        ('Kako izračunati zbroj težina svih povezanih podskupova, i kako ga održavati kad se vrhovi dodaju?',
         r'''
<p>Ukorijenimo stablo. $D(u)$ = zbroj težina povezanih podskupova čiji je najplići vrh $u$: $D(u) = [u \text{ živ}] \cdot w_u \prod_{c \text{ dijete}} (1 + D(c))$ – svako dijete ili nije uključeno ($1$) ili doprinosi povezanim podskupom kojem je ono vrh ($D(c)$). $G = \sum_u D(u)$. Oživljavanje vrha mijenja $D$ svim precima – u lancu $O(N)$ po ažuriranju. Trebamo strukturu koja to radi u polilogaritamskom vremenu: „dinamički DP” preko HLD-a.</p>
'''),
        ('Zašto je HLD sa segmentnim stablom prava struktura za ovaj DP?',
         r'''
<p>Na teškom putu $D(v) = c_v \cdot (1 + D(\text{teško dijete}))$, gdje je $c_v = [v \text{ živ}] \, w_v \prod_{\text{laka djeca}} (1 + D(c))$. To je afino preslikavanje $x \mapsto c_v + c_v x$; kompozicija afinih preslikavanja je afina, pa segmentno stablo nad putem računa $D(\text{glave})$ u $O(\log N)$. Uz koeficijente afinog preslikavanja u čvoru čuvamo i zbroj svih $D$ na segmentu (kao afinu funkciju od ulaza) pa $G$ ažuriramo razlikom zbrojeva. Promjena $D(\text{glave})$ mijenja jedan faktor u umnošku lakih djece roditelja; put do korijena prelazi $O(\log N)$ teških puteva, pa je ažuriranje $O(\log^2 N)$.</p>
'''),
        ('Koje zamke vrebaju u modularnoj aritmetici i implementaciji?',
         r'''
<p>Faktor $1 + D(c)$ može biti $\equiv 0 \pmod p$, a tada ga ne možemo „podijeliti van” iz umnoška – zato umnožak lakih djece čuvamo kao (umnožak nenultih faktora, broj nula). Težina $w_u = 2^{1-\deg u}$ ima negativan eksponent, računamo je kao $(2^{-1})^{\deg u - 1}$. Vrhove jednake vrijednosti oživimo sve prije nego što pribrojimo $(v_j - v_{j+1}) G$. Sve obilaske pišemo iterativno (BFS redoslijed, eksplicitni stog) zbog $N = 3 \cdot 10^5$ i lančastih stabala.</p>
'''),
    ],
    'tips': [
        r'''Zbroj po podskupovima bridova stabla često se pretvori u zbroj po <strong>povezanim podskupovima vrhova</strong> s multiplikativnom težinom – čim je težina umnožak po vrhovima, radi klasični DP $D(u) = w_u \prod (1 + D(c))$.''',
        r'''Faktor oblika $\min$ ili $\max$ po skupu rastavi teleskopski po pragovima: $\min(C) = \sum_j (v_j - v_{j+1}) [\min C \ge v_j]$. Tako se „skupno” svojstvo pretvara u „koji su vrhovi živi”.''',
        r'''Dinamički DP na stablu (promjene vrijednosti vrhova, upit nad cijelim stablom): HLD + segmentno stablo afinih (ili matričnih) preslikavanja daje $O(\log^2 N)$ po promjeni; laka djeca ulaze kao skalar u čvor teškog puta.''',
        r'''Kad održavaš umnožak modulo prost broj uz dijeljenje, pamti posebno broj faktora jednakih nuli – inverz nule ne postoji, a nula se pojavi točno onda kad je test najveći.''',
    ],
    'solution': r'''
<p>Preformulirajmo zadatak kao traženje očekivanog rezultata kad se svaki brid neovisno reže s vjerojatnošću $1/2$ (na kraju pomnožimo s $2^{N-1}$).</p>
<p>Odaberimo proizvoljan korijen. Za vrh $v$ neka je $T'$ njegovo podstablo i $size(v)$ broj vrhova u njemu. Definiramo DP:</p>
<p>$dp[v][x]$ — vjerojatnost da komponenta povezanosti od $T'$ koja sadrži $v$ ima minimum $x$, kad se bridovi $T'$ nasumično režu.</p>
<p>Odgovor dobivamo zbrajanjem, po svim $v$, „doprinosa svih povezanih podgrafova stabla $T$ kojima je $v$ najplići vrh”. Drugi argument $x$ može poprimiti do $10^9$ vrijednosti, ali samo $size(v)$ njih ima vjerojatnost različitu od nule, pa tablicu komprimiramo čuvajući samo te vrijednosti.</p>
<p>Ako vrh $v$ ima dvoje djece $c_1, c_2$, $dp[v][*]$ računamo iz $dp[c_1][*]$ i $dp[c_2][*]$ prefiksnim zbrojevima u $O(size(c_1) + size(c_2))$. Ako ima troje ili više djece, spajamo ih u parovima i dobivamo $dp[v][*]$ u $O(size(v) \log N)$.</p>
<h3>Metoda spajanja segmentnih stabala</h3>
<p>Izračun $dp[v][*]$ iz $dp[c_1][*]$ i $dp[c_2][*]$ može se promatrati kao ažuriranje u jednoj točki ili množenje na intervalu nad $dp[c_1][*]$ pomoću podataka iz $dp[c_2][*]$. Ako ih držimo u segmentnom stablu s lijenom propagacijom koje stvara samo potrebne elemente, spajanje traje $O(\min(size(c_1), size(c_2)) \log A)$, ukupno $O(N \log N \log A)$, a uz efikasno spajanje segmentnih stabala $O(N \log A)$ (vidi <a href="https://codeforces.com/blog/entry/49446">ovaj članak</a>).</p>
<h3>Metoda s top tree strukturom</h3>
<p>Koristimo tehniku kao u zadatku <a href="https://atcoder.jp/contests/abc269/tasks/abc269_h">ABC269 Ex</a>. Za povezani podgraf $C$ stabla $T$ koji je s okolinom povezan samo preko vrhova $u$ i $v$ održavamo: za svaki $x$ vjerojatnost da su $u$ i $v$ povezani i minimum njihove komponente je $x$; za svaki $x$ vjerojatnost da nisu povezani i minimum komponente vrha $u$ je $x$; isto za vrh $v$; te doprinos odgovoru komponenata koje ne sadrže ni $u$ ni $v$. Dva takva zapisa spajaju se u linearnom vremenu u zbroju broja vrhova, pa je ukupna složenost $O(N \log N)$.</p>
''',
    'detailed': r'''
<h3>1. Od podskupova bridova do povezanih podskupova vrhova</h3>
<p>Rezultat podskupa bridova je zbroj minimuma po komponentama. Zamijenimo poredak zbrajanja: za svaki povezan podskup vrhova $C$ pitamo se u koliko podskupova bridova je $C$ komponenta. To se događa točno kad su svih $|C| - 1$ bridova unutar $C$ zadržani, a svi bridovi s jednim krajem u $C$ i drugim izvan prerezani; takvih „izlaznih” bridova je $\sum_{u \in C} \deg u - 2(|C| - 1)$. Preostali bridovi su slobodni, a ima ih</p>
<p>$$(N - 1) - (|C| - 1) - \Bigl(\sum_{u \in C} \deg u - 2(|C| - 1)\Bigr) = N - 2 + \sum_{u \in C} (1 - \deg u).$$</p>
<p>Dakle</p>
<p>$$\text{odgovor} = \sum_{C \text{ povezan}} \min(C) \cdot 2^{N-2} \prod_{u \in C} 2^{1 - \deg u} = 2^{N-2} \sum_C \min(C) \prod_{u \in C} w_u, \qquad w_u = 2^{1 - \deg u}.$$</p>
<p>Eksponent je nenegativan (za $C$ = cijelo stablo iznosi $0$), ali u modularnoj aritmetici jednostavno računamo $w_u = (2^{-1})^{\deg u - 1}$. Provjera na primjeru ($1\!-\!2, 2\!-\!4, 3\!-\!2$, $A = (1,2,3,4)$): $w = (1, \tfrac14, 1, 1)$, zbroj $\min(C) \prod w$ po $11$ povezanih podskupova iznosi $11$, pomnoženo s $2^{N-2} = 4$ daje $44$.</p>
<h3>2. Rastav minimuma po pragovima</h3>
<p>Neka su $v_1 > v_2 > \dots > v_k$ različite vrijednosti u $A$ i $v_{k+1} = 0$. Za svaki $C$ vrijedi teleskopski identitet</p>
<p>$$\min(C) = \sum_{j : v_j \le \min(C)} (v_j - v_{j+1}) = \sum_{j=1}^{k} (v_j - v_{j+1}) \, [\min(C) \ge v_j],$$</p>
<p>jer zbroj po $j$ od indeksa vrijednosti $\min(C)$ do $k$ daje $\min(C) - v_{k+1} = \min(C)$. Uvjet $\min(C) \ge v_j$ znači da su svi vrhovi $C$ u skupu $S_j = \{u : A_u \ge v_j\}$. Zato</p>
<p>$$\sum_C \min(C) \prod_{u \in C} w_u = \sum_{j=1}^{k} (v_j - v_{j+1}) \, G_j, \qquad G_j = \sum_{C \subseteq S_j \text{ povezan}} \prod_{u \in C} w_u.$$</p>
<p>Skupovi $S_j$ rastu: $S_1 \subset S_2 \subset \dots \subset S_k = V$. Obrađujemo vrhove u padajućem redoslijedu po $A$, „oživljavamo” cijelu grupu jednake vrijednosti i zatim pribrajamo $(v_j - v_{j+1}) \cdot G$.</p>
<h3>3. Zbroj težina povezanih podskupova živih vrhova</h3>
<p>Ukorijenimo stablo u $1$. Za vrh $u$ neka je $D(u)$ zbroj težina povezanih podskupova živih vrhova čiji je najplići vrh upravo $u$. Takav podskup sadrži $u$ (mora biti živ) i za svako dijete $c$ ili ne sadrži ništa iz podstabla $c$, ili sadrži povezan podskup s vrhom $c$ (jer mora biti povezan s $u$ preko $c$). Izbori po djeci su neovisni, pa</p>
<p>$$D(u) = [u \text{ živ}] \cdot w_u \prod_{c \text{ dijete } u} \bigl(1 + D(c)\bigr), \qquad G = \sum_u D(u).$$</p>
<p>Statički to je $O(N)$, ali nakon svakog oživljavanja mijenjaju se $D$ svih predaka, a grupa vrijednosti može biti proizvoljna – naivno $O(N^2)$ u lancu.</p>
<h3>4. Dinamički DP: HLD i afina preslikavanja</h3>
<p>Napravimo dekompoziciju na teške putove (heavy-light). Za vrh $v$ neka je $c_v = [v \text{ živ}] \cdot w_v \cdot \prod_{c \text{ lako dijete}} (1 + D(c))$. Tada je $D(v) = c_v \,(1 + x)$, gdje je $x = D(\text{teško dijete})$ (ili $x = 0$ na dnu puta). To je afina funkcija $x \mapsto a + b x$ s $a = b = c_v$. Kompozicija duž puta: ako gornji segment daje $D(\text{vrh}) = a_1 + b_1 y$ uz $y = D(\text{vrh donjeg segmenta}) = a_2 + b_2 x$, onda je ukupno $a = a_1 + b_1 a_2$, $b = b_1 b_2$. Istodobno pratimo zbroj svih $D$ na segmentu kao afinu funkciju $s + t x$: za gornji $(s_1, t_1)$ i donji $(s_2, t_2)$ vrijedi $s = s_1 + t_1 a_2 + s_2$, $t = t_1 b_2 + t_2$. Mrtav vrh ima $(a, b, s, t) = (0, 0, 0, 0)$: njegov $D$ je $0$ bez obzira na ulaz i ništa ne pridonosi zbroju.</p>
<p>Svaki teški put je neprekinut segment pozicija, pa upit nad njim uz $x = 0$ daje $D(\text{glave}) = a$ i zbroj $D$ po putu $= s$. Oživljavanje vrha $u$:</p>
<ol>
    <li>Na teškom putu glave $h = \mathrm{head}(u)$ pročitamo stari zbroj i staro $D(h)$, promijenimo list $u$ na $(c_u, c_u, c_u, c_u)$, pročitamo novi zbroj i novo $D(h)$. $G$ povećamo za razliku zbrojeva.</li>
    <li>Ako $h$ nije korijen, brid $(\mathrm{par}(h), h)$ je lak: u umnošku lakih djece vrha $p = \mathrm{par}(h)$ zamijenimo faktor $1 + D_{\text{staro}}(h)$ s $1 + D_{\text{novo}}(h)$, pa ponovimo korak 1 za $u := p$.</li>
</ol>
<p>Put do korijena siječe $O(\log N)$ teških puteva, a svaki korak je $O(\log N)$ na segmentnom stablu, dakle $O(\log^2 N)$ po oživljavanju i $O(N \log^2 N)$ ukupno.</p>
<h3>5. Zašto je zbroj $s$ točan i zašto se $G$ smije ažurirati razlikom</h3>
<p>Segment predstavlja skup vrhova teškog puta; njegov $s + t x$ je zbroj $D$-ova <em>tih</em> vrhova, a $D$-ovi vrhova izvan puta (laka podstabla) ulaze u $c_v$ i u $D$-ove vlastitih puteva. Svaki vrh pripada točno jednom teškom putu, pa je $G$ zbroj vrijednosti $s$ po svim putevima (uz $x = 0$). Oživljavanje $u$ mijenja $D$ samo precima od $u$, a oni leže na putevima koje obilazimo u koracima 1–2, pa razlike zbrojeva na tim putevima točno pokrivaju promjenu $G$.</p>
<h3>6. Nule u umnošku</h3>
<p>Faktor $1 + D(c)$ je ostatak modulo $p$ i može biti $0$. Dijeljenje starim faktorom tada nije moguće, pa umnožak lakih djece čuvamo kao par (umnožak nenultih faktora, broj nultih faktora); vrijednost je $0$ ako je brojač nula pozitivan. Dijeljenje nenultim faktorom je množenje inverzom (Fermat), $O(\log p)$.</p>
<h3>7. Algoritam u cjelini</h3>
<ol>
    <li>BFS iz korijena: roditelji, veličine podstabala, teško dijete; eksplicitnim stogom dodijelimo pozicije tako da je svaki teški put neprekinut segment (glava ima najmanju poziciju) i zapamtimo dno svakog puta.</li>
    <li>Segmentno stablo inicijaliziramo mrtvim vrhovima; $G = 0$.</li>
    <li>Sortiramo vrhove padajuće po $A$. Za svaku grupu jednakih vrijednosti $v_j$: oživimo sve vrhove grupe (postupak iz točke 4), zatim $\text{ans} \mathrel{+}= (v_j - v_{j+1}) \cdot G$, gdje je $v_{j+1}$ sljedeća manja vrijednost ili $0$.</li>
    <li>Ispišemo $\text{ans} \cdot 2^{N-2} \bmod p$.</li>
</ol>
<h3>8. Složenost i rubni slučajevi</h3>
<p>Vrijeme $O(N \log^2 N)$ (uz $O(\log p)$ za inverze pri prelasku lakih bridova), memorija $O(N)$. Za $N = 3 \cdot 10^5$ najsporiji test (lanac s rastućim vrijednostima, gdje svako oživljavanje mijenja dugačak put) traje ispod sekunde. $N = 2$: $2^{N-2} = 1$, sve radi. Sve vrijednosti su modulo $p$; razlika $v_j - v_{j+1}$ je pozitivna pa nema negativnih ostataka, ali razliku zbrojeva $s$ normaliziramo dodavanjem $p$. Nema rekurzije, pa lanac dubine $3 \cdot 10^5$ nije problem.</p>
<p>Napomena: službeno rješenje (vidi sažetak) vodi distribuciju minimuma $dp[v][x]$ i spaja djecu; naš je pristup drugačiji put do iste sume – umjesto po vrhu-predstavniku komponente i njegovu minimumu, zbrajamo po pragovima i povezanim podskupovima.</p>
''',
    'verified': r'''uzorci 2/2; 300 slučajnih malih stabala ($N \le 10$, slučajna/lančasta/zvjezdasta/„metla”, vrijednosti iz malog i punog raspona) protiv brute forcea koji prolazi sva $2^{N-1}$ podskupa bridova; 3 velika testa s $N = 3 \cdot 10^5$ (lanac s rastućim vrijednostima kao najgori slučaj propagacije, zvijezda, slučajno), najsporiji $0.82$ s.''',
},
# ---------------------------------------------------------------- G
{
    'letter': 'G', 'title': 'Range NEQ', 'title_hr': 'Različiti blokovi', 'slug': 'G_range_neq',
    'tl': '2 s', 'ml': '1024 MB',
    'statement': r'''
<p>Dani su $N$ i $M$. Prebroji permutacije $P = (P_0, \dots, P_{NM-1})$ skupa $\{0, \dots, NM-1\}$ takve da za sve $i$ vrijedi $\left\lfloor \frac{i}{M} \right\rfloor \ne \left\lfloor \frac{P_i}{M} \right\rfloor$, modulo $998244353$.</p>
<h3>Ulaz</h3>
<p>$N$ i $M$ ($2 \le N \le 1000$, $1 \le M \le 1000$).</p>
<h3>Izlaz</h3>
<p>Broj takvih permutacija.</p>
<h3>Primjer</h3>
<p>Za $N = M = 2$ odgovor je $4$; za $N = 5$, $M = 1$ odgovor je $44$ (broj derangementa).</p>
''',
    'hints': [
        r'''<p>Ovo je poopćenje derangementa: pozicije i vrijednosti podijeljene su u $N$ blokova po $M$, i element ne smije ostati u „svom” bloku. Princip uključivanja–isključivanja po broju „loših” pozicija u svakom bloku.</p>''',
        r'''<p>Ako u bloku $j$ točno $k_j$ pozicija dobiva vrijednost iz istog bloka, broj načina je $\binom{M}{k_j} \cdot \frac{M!}{(M-k_j)!}$. Blokovi su međusobno neovisni, a ostatak je $(NM - \sum k_j)!$ — zato generirajuća funkcija jednog bloka dignuta na $N$-tu potenciju.</p>''',
    ],
    'coach': [
        ('Uvjet „$P_i$ nije u bloku pozicije $i$” teško je brojati izravno – koji je komplementarni događaj lak?',
         r'''
<p>Za $M = 1$ to su derangementi, a njih brojimo uključivanjem–isključivanjem po skupu fiksnih točaka. Ovdje analogno: „loša” pozicija $i$ je ona za koju je $P_i$ u istom bloku kao $i$. Za <em>zadani</em> skup $S$ pozicija lako je izbrojati permutacije u kojima su sve pozicije iz $S$ loše (ostale su proizvoljne) – to je točno ono što uključivanje–isključivanje traži: $\text{odgovor} = \sum_S (-1)^{|S|} \, \#\{P : \text{sve pozicije iz } S \text{ loše}\}$.</p>
'''),
        ('Koliko permutacija ima sve pozicije iz $S$ loše, i od čega taj broj zapravo ovisi?',
         r'''
<p>Neka $S$ sadrži $k_j$ pozicija iz bloka $j$. Tim pozicijama moramo dodijeliti <em>različite</em> vrijednosti iz bloka $j$ (ima ih $M$): $\frac{M!}{(M - k_j)!}$ načina, neovisno po blokovima. Preostalih $NM - \sum k_j$ pozicija dobiva preostale vrijednosti proizvoljno: $(NM - \sum k_j)!$. Broj ovisi samo o vektoru $(k_0, \dots, k_{N-1})$, a skupova $S$ s tim vektorom ima $\prod_j \binom{M}{k_j}$. Zato je odgovor</p>
<p>$$\sum_{(k_j)} (-1)^{\sum k_j} \Bigl(NM - \sum_j k_j\Bigr)! \prod_j \binom{M}{k_j} \frac{M!}{(M - k_j)!}, \qquad \binom{M}{k} \frac{M!}{(M-k)!} = \frac{(M!)^2}{((M-k)!)^2 \, k!}.$$</p>
'''),
        ('Zbroj po $N$-torkama ima $(M+1)^N$ članova – što je jedina veličina kroz koju blokovi međusobno ovise?',
         r'''
<p>Samo zbroj $s = \sum_j k_j$ (kroz faktor $(NM - s)!$). Sve ostalo je umnožak po blokovima. Zbroj umnožaka po svim rastavima $s$ na $N$ pribrojnika je točno koeficijent uz $x^s$ u $N$-toj potenciji polinoma $f(x) = \sum_{k=0}^{M} \frac{(M!)^2}{((M-k)!)^2 k!} (-x)^k$ – predznak $(-1)^{k}$ smjestimo u $(-x)^k$. Dakle $\text{odgovor} = \sum_{s=0}^{NM} (NM - s)! \, [x^s] f(x)^N$.</p>
'''),
        ('Kako izračunati $f^N$ stupnja $NM \le 10^6$ u vremenu?',
         r'''
<p>NTT-om nad $998244353$: transformiramo $f$ u duljini $2^k \ge NM + 1$ (dovoljno da se $f^N$, stupnja točno $NM$, ne „omota” ciklički), svaku točku dignemo na $N$-tu potenciju binarnim potenciranjem, pa inverzni NTT. Složenost $O(NM \log(NM) + NM \log N)$ – jedan par transformacija duljine $2^{20}$, nema potrebe za polinomskim $\exp/\log$.</p>
'''),
        ('Kako provjeriti formulu prije pisanja NTT-a?',
         r'''
<p>Na $N = M = 2$: $f(x) = 1 - 4x + 2x^2$, $f^2 = 1 - 8x + 20x^2 - 16x^3 + 4x^4$, odgovor $24 - 48 + 40 - 16 + 4 = 4$, kao u primjeru. Ista provjera otkriva i tipfeler u službenom rješenju, gdje u brojniku stoji $M!$ umjesto $(M!)^2$ (s $M!$ dobije se $1$).</p>
'''),
    ],
    'tips': [
        r'''Uvjete „ne smije” brojimo <strong>uključivanjem–isključivanjem</strong> kad je „mora za zadani skup” lako: $\sum_S (-1)^{|S|} \cdot \#\{\text{sve iz } S \text{ loše}\}$. Derangementi su najjednostavniji slučaj i dobar model.''',
        r'''Kad se ukupni izraz faktorizira po neovisnim dijelovima, a dijelovi su vezani samo zbrojem jednog parametra, taj je zbroj <strong>konvolucija</strong>: koeficijent u umnošku (potenciji) generirajućih funkcija.''',
        r'''Potenciju $f^N$ za jedan konkretan $N$ računaj kao NTT $\to$ potenciranje po točkama $\to$ inverzni NTT, uz duljinu $> \deg f^N$; to je jednostavnije i brže od općeg polinomskog $\exp(N \log f)$.''',
        r'''Svaku kombinatoričku formulu iz editorijala provjeri ručno na najmanjem primjeru – tipfeleri u faktorijelima su česti, a takva provjera traje minutu.''',
    ],
    'solution': r'''
<p>Zadatak rješavamo principom uključivanja–isključivanja.</p>
<p>Promotrimo niz $(k_0, \dots, k_{N-1})$ i slučajeve u kojima točno $k_j$ indeksa $i$ s $\lfloor i/M \rfloor = j$ zadovoljava $\lfloor P_i/M \rfloor = j$, za svaki $j = 0, \dots, N-1$. Broj načina da odaberemo tih $k_j$ indeksa je $\binom{M}{k_j}$, a broj načina da im dodijelimo vrijednosti je $\frac{M!}{(M-k_j)!}$. Preostalih $NM - \sum_j k_j$ indeksa možemo popuniti na $(NM - \sum_j k_j)!$ načina. Stoga broj permutacija za dani $(k_0, \dots, k_{N-1})$ iznosi</p>
<p>$$\Bigl(NM - \sum_{j} k_j\Bigr)!\ \prod_{j=0}^{N-1} \frac{M!}{((M-k_j)!)^2\, k_j!},$$</p>
<p>pa je po principu uključivanja–isključivanja odgovor</p>
<p>$$\sum_{(k_0, \dots, k_{N-1})} (-1)^{\sum_j k_j} \Bigl(NM - \sum_{j} k_j\Bigr)!\ \prod_{j=0}^{N-1} \frac{M!}{((M-k_j)!)^2\, k_j!}.$$</p>
<p>To računamo generirajućim funkcijama. Neka je</p>
<p>$$f(x) = \sum_{k=0}^{M} \frac{M!}{((M-k)!)^2\, k!}\,(-x)^k, \qquad g(x) = f(x)^N.$$</p>
<p>Tada je odgovor $\sum_{s=0}^{NM} (NM - s)!\,[x^s]\,g(x)$. Vremenska složenost je $O(NM \log(NM))$.</p>
''',
    'detailed': r'''
<h3>1. Uključivanje–isključivanje</h3>
<p>Pozicije i vrijednosti podijeljene su u $N$ blokova po $M$: blok pozicije $i$ je $\lfloor i/M \rfloor$. Pozicija $i$ je „loša” u permutaciji $P$ ako je $P_i$ u istom bloku kao $i$. Tražimo permutacije bez loših pozicija. Po principu uključivanja–isključivanja (za događaje $E_i$ = „pozicija $i$ je loša”):</p>
<p>$$\text{odgovor} = \sum_{S \subseteq \{0, \dots, NM-1\}} (-1)^{|S|} \, \#\{P : E_i \text{ za sve } i \in S\}.$$</p>
<p>Fiksirajmo $S$ i neka $S$ sadrži $k_j$ pozicija iz bloka $j$. Permutaciju u kojoj su sve pozicije iz $S$ loše konstruiramo tako da: (a) pozicijama iz $S$ u bloku $j$ dodijelimo međusobno različite vrijednosti iz bloka $j$ – uređeni odabir $k_j$ od $M$ vrijednosti, $\frac{M!}{(M-k_j)!}$ načina, neovisno za svaki blok jer su skupovi vrijednosti blokova disjunktni; (b) preostalih $NM - \sum_j k_j$ pozicija dobiva preostale vrijednosti u proizvoljnom poretku, $(NM - \sum_j k_j)!$ načina. Broj takvih $P$ ovisi samo o $(k_0, \dots, k_{N-1})$, a broj skupova $S$ s tim profilom je $\prod_j \binom{M}{k_j}$. Zato</p>
<p>$$\text{odgovor} = \sum_{(k_0, \dots, k_{N-1}) \in \{0..M\}^N} (-1)^{\sum_j k_j} \Bigl(NM - \sum_j k_j\Bigr)! \prod_{j=0}^{N-1} c_{k_j}, \qquad c_k = \binom{M}{k} \frac{M!}{(M-k)!} = \frac{(M!)^2}{((M-k)!)^2 \, k!}.$$</p>
<p><strong>Napomena o službenom editorijalu.</strong> U službenom tekstu (i u izvornom prijevodu u sažetku) brojnik je bio $M!$ umjesto $(M!)^2$; to je tipfeler – s $M!$ za $N = M = 2$ dobili bismo $1$ umjesto $4$. Ispravljeno je u sažetku iznad.</p>
<h3>2. Prelazak na generirajuću funkciju</h3>
<p>Jedina veza među blokovima je zbroj $s = \sum_j k_j$. Grupirajmo članove po $s$:</p>
<p>$$\text{odgovor} = \sum_{s=0}^{NM} (NM - s)! \cdot \Bigl[\sum_{k_0 + \dots + k_{N-1} = s} \prod_j (-1)^{k_j} c_{k_j}\Bigr].$$</p>
<p>Unutarnji zbroj je po definiciji umnoška polinoma koeficijent uz $x^s$ u $f(x)^N$, gdje je</p>
<p>$$f(x) = \sum_{k=0}^{M} c_k (-x)^k = \sum_{k=0}^{M} \frac{(M!)^2}{((M-k)!)^2 \, k!} (-1)^k x^k.$$</p>
<p>Dakle $\text{odgovor} = \sum_{s=0}^{NM} (NM - s)! \, [x^s] f(x)^N$. Stupanj $f^N$ je točno $NM \le 10^6$.</p>
<h3>3. Računanje $f^N$ NTT-om</h3>
<p>Modul $998244353 = 119 \cdot 2^{23} + 1$ podržava NTT duljine do $2^{23}$ s primitivnim korijenom $3$. Uzmemo duljinu $L = 2^k$ najmanju s $L \ge NM + 1$ (najviše $2^{20}$ za $NM \le 10^6$, jer $2^{20} = 1048576 > 10^6$). Postupak:</p>
<ol>
    <li>predizračunaj faktorijele i inverzne faktorijele do $NM$;</li>
    <li>popuni $f$ koeficijentima $c_k$ s predznakom $(-1)^k$ za $k = 0..M$, ostatak nule;</li>
    <li>NTT$(f)$; svaku od $L$ vrijednosti digni na $N$-tu potenciju (binarno potenciranje, $O(\log N)$);</li>
    <li>inverzni NTT – dobivamo koeficijente $f^N$ bez cikličkog preklapanja jer je $\deg f^N = NM < L$;</li>
    <li>$\text{odgovor} = \sum_{s=0}^{NM} (NM - s)! \cdot [x^s] f^N \bmod p$.</li>
</ol>
<p>Zašto potenciranje po točkama radi: NTT je evaluacija polinoma u $L$ korijena jedinice; evaluacija umnoška je umnožak evaluacija, pa su vrijednosti $f^N$ u tim točkama upravo $N$-te potencije. Interpolacija (inverzni NTT) vraća jedinstveni polinom stupnja $< L$ s tim vrijednostima, a to je $f^N$ jer mu je stupanj $< L$.</p>
<h3>4. Složenost i detalji</h3>
<p>Faktorijeli $O(NM)$, dva NTT-a $O(L \log L)$, potenciranje $O(L \log N)$, završni zbroj $O(NM)$; ukupno oko $2 \cdot 10^7$ modularnih množenja – daleko unutar $2$ s. Memorija: nekoliko nizova duljine $2^{20}$ 64-bitnih brojeva ($\approx 25$ MB). Negativne koeficijente držimo kao $p - v$. Rubni slučajevi: $M = 1$ daje $f(x) = 1 - x$ i klasičnu formulu za derangemente $\sum_s (-1)^s \binom{N}{s} (N-s)!$ (primjer $N = 5$: $44$); $N M$ do $10^6$ traži $L = 2^{20}$, pa niz ne smije biti fiksirane manje duljine.</p>
<h3>5. Provjera na primjeru $N = M = 2$</h3>
<p>$c_0 = 1$, $c_1 = \binom{2}{1} \cdot 2 = 4$, $c_2 = 1 \cdot 2 = 2$, pa $f(x) = 1 - 4x + 2x^2$ i $f^2 = 1 - 8x + 20x^2 - 16x^3 + 4x^4$. Odgovor: $4! \cdot 1 - 3! \cdot 8 + 2! \cdot 20 - 1! \cdot 16 + 0! \cdot 4 = 24 - 48 + 40 - 16 + 4 = 4$. Doista, od $24$ permutacija skupa $\{0,1,2,3\}$ uvjet zadovoljavaju one koje $\{0,1\}$ preslikavaju na $\{2,3\}$ i obrnuto: $2 \cdot 2 = 4$.</p>
''',
    'verified': r'''uzorci 3/3; 300 slučajnih malih testova ($NM \le 8$) protiv brute forcea koji prolazi sve permutacije; 3 velika testa s $NM \approx 10^6$ ($N, M \in \{997, 999, 1000\}$), najsporiji $0.09$ s.''',
},
# ---------------------------------------------------------------- H
{
    'letter': 'H', 'title': 'Expanded Hull', 'title_hr': 'Proširena ljuska', 'slug': 'H_expanded_hull',
    'tl': '4 s', 'ml': '1024 MB',
    'statement': r'''
<p>Dani su $N$, $K$ i $N$ točaka $(X_i, Y_i, Z_i)$ u prostoru. Neka je $V$ konveksna ljuska točaka $(KX_i, KY_i, KZ_i)$. Prebroji cjelobrojne točke u unutrašnjosti ili na rubu $V$, modulo $998244353$.</p>
<h3>Ulaz</h3>
<p>$N$, $K$ ($4 \le N \le 100$, $1 \le K \le 10^{15}$) i $N$ različitih točaka s koordinatama u $[-200, 200]$; točke ne leže u jednoj ravnini.</p>
<h3>Izlaz</h3>
<p>Broj cjelobrojnih točaka.</p>
<h3>Primjer</h3>
<p>Za tetraedar $(0,0,0), (1,0,0), (0,1,0), (0,0,1)$ i $K = 2$ odgovor je $10$.</p>
''',
    'hints': [
        r'''<p>Broj cjelobrojnih točaka u $k$-tom uvećanju cjelobrojnog politopa dimenzije $3$ je polinom u $k$ stupnja $3$ — <em>Ehrhartov polinom</em>. Dovoljno ga je odrediti za $k = 0, 1, 2, 3$ i interpolirati u $K$.</p>''',
        r'''<p>Za male $k$ točke se mogu izbrojati izravno: koordinate su do $600$, pa za svaki par $(x, y)$ nađi presjek pravca s ljuskom (interval po $z$) — $O(NX^2)$ ravnina puta stupaca.</p>''',
        r'''<p>Alternativa: iz volumena, broja unutarnjih i broja rubnih točaka za $k = 1$ također se rekonstruira Ehrhartov polinom (koeficijenti: vodeći je volumen, $L(-k)$ broji unutrašnjost — Ehrhart–Macdonaldova reciprocnost).</p>''',
    ],
    'coach': [
        ('$K$ je do $10^{15}$ – što se događa s brojem cjelobrojnih točaka kad politop skaliramo cijelim faktorom $k$?',
         r'''
<p>Za politop $P$ s cjelobrojnim vrhovima broj $L(k) = |kP \cap \mathbb{Z}^3|$ je <em>polinom</em> u $k$ stupnja $\dim P = 3$ (Ehrhartov teorem). Intuicija: $P$ se može triangulirati na simplekse s cjelobrojnim vrhovima, a za simpleks se točke u $kP$ broje po „slojevima” konusa nad njim, što daje binomne koeficijente u $k$ – polinome. Dakle ne trebamo brojati u $KP$, nego odrediti kubni polinom i izvrijedniti ga u $K$ modulo $p$.</p>
'''),
        ('Koje četiri vrijednosti polinoma možemo dobiti dovoljno jeftino?',
         r'''
<p>$L(0) = 1$ besplatno (samo ishodište). $L(1)$ i $L(2)$ brojimo izravno – koordinate su do $200$, odnosno $400$. Umjesto skupljeg $L(3)$ iskoristimo Ehrhart–Macdonaldovu recipročnost: $L(-k) = (-1)^3 \cdot |\text{int}(kP) \cap \mathbb{Z}^3|$, pa je $L(-1) = -I(1)$, gdje je $I(1)$ broj <em>strogo unutarnjih</em> točaka u $P$ – dobiva se istim prolazom kao $L(1)$, samo sa strogim nejednakostima. Četiri točke $-1, 0, 1, 2$ jednoznačno određuju kubni polinom.</p>
'''),
        ('Kako uopće brojati cjelobrojne točke u konveksnoj ljusci u 3D?',
         r'''
<p>Konveksni politop je presjek poluprostora svojih stranica: $a x + b y + c z \le d$. Za fiksan cjelobrojni stupac $(x, y)$ svaka stranica daje gornju granicu za $z$ (ako $c > 0$), donju (ako $c < 0$) ili uvjet neovisan o $z$ (ako $c = 0$); presjek je interval $[lo, hi]$ i pridonosi $\max(0, hi - lo + 1)$ točaka. Ravnine stranica nalazimo u $O(N^4)$: za svaku nekolinearnu trojku točaka ravnina je stranica ako su sve točke s iste strane; normalizacijom (gcd, orijentacija) uklonimo duplikate koplanarnih trojki.</p>
'''),
        ('Kako iz četiri vrijednosti dobiti $L(K) \bmod p$ kad je $K$ ogroman i polinom ima racionalne koeficijente?',
         r'''
<p>Lagrangeovom interpolacijom: $L(K) = \sum_i y_i \prod_{j \ne i} \frac{K - x_j}{x_i - x_j}$. Ta jednakost vrijedi u $\mathbb{Q}$, a nazivnici su umnošci razlika iz $\{-1, 0, 1, 2\}$, dakle djelitelji od $6$ – invertibilni modulo $p$. Zato smijemo sve računati modulo $p$ uz $K \bmod p$: rezultat je cijeli broj $L(K)$ reduciran modulo $p$.</p>
'''),
        ('Koliko to košta i gdje su zamke?',
         r'''
<p>Stranica ima najviše $2N - 4 \le 196$. Prolaz za $k = 2$ obrađuje $(2 \cdot 2 \cdot 200 + 1)^2 \approx 6.4 \cdot 10^5$ stupaca po $\le 196$ ravnina, oko $1.3 \cdot 10^8$ cjelobrojnih operacija; $k = 1$ (dvaput) je četiri puta jeftiniji. Zamke: cjelobrojno dijeljenje zaokružuje prema nuli pa treba pravi $\lfloor \cdot \rfloor$ i $\lceil \cdot \rceil$ za negativne brojeve; stroga nejednakost $< r$ za cijele brojeve je $\le r - 1$; koeficijenti ravnina su do $\sim 3 \cdot 10^5$ i $d$ do $\sim 2 \cdot 10^8$ – 64-bitni tip.</p>
'''),
    ],
    'tips': [
        r'''<strong>Ehrhartov polinom:</strong> broj cjelobrojnih točaka u $kP$ za cjelobrojni politop $P$ dimenzije $d$ je polinom stupnja $d$ u $k$; kad je parametar skaliranja ogroman, izračunaj $d + 1$ malih vrijednosti i interpoliraj.''',
        r'''Ehrhart–Macdonaldova recipročnost $L(-k) = (-1)^d \, I(k)$ daje dodatne točke interpolacije „besplatno” – strogo unutarnje točke za $k = 1$ broje se istim kodom kao i rubne.''',
        r'''Cjelobrojne točke u konveksnom tijelu broji po stupcima: fiksiraj sve koordinate osim jedne i sjeci poluprostore u interval; pripazi na $\lfloor \cdot \rfloor$ za negativne brojnike.''',
        r'''Za brojanje u malim dimenzijama uz $N \le 100$ ne trebaš pravi 3D hull algoritam – $O(N^4)$ provjera „sve točke s iste strane ravnine” je kraća i sigurnija.''',
    ],
    'solution': r'''
<p>Kad $K$ varira, odgovor je polinom trećeg stupnja u $K$ — <a href="https://en.wikipedia.org/wiki/Ehrhart_polynomial">Ehrhartov polinom</a>. Zato postupamo ovako. Neka je $X = \max_i \{|x_i|, |y_i|, |z_i|\}$.</p>
<ol>
    <li>Nađemo ravnine koje čine 3D konveksnu ljusku. Dovoljan je algoritam složenosti $O(N^4)$: fiksiramo tri nekolinearne točke i izračunamo kandidatsku ravninu; ako sve točke leže s iste strane, ravnina je valjana.</li>
    <li>Za $k = 1, 2, 3$ pomnožimo koordinate s $k$ i prebrojimo cjelobrojne točke unutar (uključujući rub) nastale ljuske: fiksiramo $x$ i $y$ u rasponu $-kX \le x, y \le kX$ i izračunamo presjek pravca s ljuskom.</li>
    <li>Interpoliramo Ehrhartov polinom i izvrijednimo ga u $K$.</li>
</ol>
<p>Vremenska složenost je $O(N^4 + NX^2)$.</p>
<p>Umjesto brojanja točaka za $k = 1, 2, 3$, Ehrhartov polinom možemo dobiti i iz triju veličina za $k = 1$: volumena ljuske, broja cjelobrojnih točaka unutar ljuske uključujući rub, te broja cjelobrojnih točaka strogo u unutrašnjosti. Uz dodatan trud složenost se može smanjiti na $O(N \log N + NX \log X)$. Sretno s implementacijom!</p>
''',
    'detailed': r'''
<h3>1. Zašto je odgovor polinom u $K$</h3>
<p>Neka je $P$ konveksna ljuska zadanih točaka; kako točke nisu koplanarne, $P$ je trodimenzionalan politop s cjelobrojnim vrhovima (svi vrhovi ljuske su neke od ulaznih točaka). Konveksna ljuska točaka $(KX_i, KY_i, KZ_i)$ je upravo $KP = \{K p : p \in P\}$. Ehrhartov teorem kaže da je za cjelobrojni politop dimenzije $d$ funkcija $L(k) = |kP \cap \mathbb{Z}^d|$, $k \in \mathbb{Z}_{\ge 0}$, polinom u $k$ stupnja $d$ s vodećim koeficijentom jednakim volumenu $P$. Skica razloga: $P$ se može triangulirati na simplekse s cjelobrojnim vrhovima (bez novih vrhova); za simpleks $\Delta$ točke u $k\Delta$ odgovaraju cjelobrojnim točkama u konusu nad $\Delta$ na „visini” $k$, a njih se broji kao konačan zbroj članova oblika $\binom{k + c}{d}$, dakle polinoma stupnja $d$; uključivanje–isključivanje po presjecima simpleksa (koji su također cjelobrojni simpleksi nižih dimenzija) daje polinom za cijeli $P$. Uz to vrijedi $L(0) = 1$ (samo ishodište) i <em>Ehrhart–Macdonaldova recipročnost</em>: $L(-k) = (-1)^d \, I(k)$, gdje je $I(k)$ broj cjelobrojnih točaka strogo u unutrašnjosti $kP$.</p>
<p>Za $d = 3$ polinom je kubni; četiri vrijednosti ga jednoznačno određuju. Biramo čvorove $k \in \{-1, 0, 1, 2\}$: $L(-1) = -I(1)$, $L(0) = 1$, $L(1)$ i $L(2)$ brojimo izravno. Time izbjegavamo najskuplje brojanje za $k = 3$ (koordinate do $600$).</p>
<h3>2. Ravnine stranica</h3>
<p>Konveksni politop je presjek poluprostora određenih ravninama svojih stranica. Za svaku trojku točaka $P_i, P_j, P_k$ izračunamo normalu $\vec n = (P_j - P_i) \times (P_k - P_i)$; ako je $\vec n = 0$, točke su kolinearne i preskačemo ih. Inače ravnina $\vec n \cdot p = d$ ($d = \vec n \cdot P_i$) je ravnina stranice točno ako su sve točke na istoj strani: svi $\vec n \cdot P_t - d$ istog znaka ili nula. Orijentiramo je tako da vrijedi $\vec n \cdot p \le d$ za sve točke, podijelimo $(a, b, c, d)$ najvećim zajedničkim djeliteljem i spremimo u skup – tako se ravnina stranice s više koplanarnih točaka broji jednom. Složenost $O(N^3 \cdot N) = O(N^4)$, za $N = 100$ oko $1.6 \cdot 10^7$ operacija. Koordinate su do $200$, pa su komponente normale do $2 \cdot 400^2 = 3.2 \cdot 10^5$, a $d$ do $\approx 2 \cdot 10^8$ – sve u 64-bitnoj aritmetici.</p>
<p>Svaka stranica ljuske ima barem tri nekolinearne točke, pa ćemo je naći; obrnuto, ravnina sa svim točkama na jednoj strani i tri nekolinearne točke na sebi jest ravnina stranice (ili sadrži stranicu). Zato je presjek dobivenih poluprostora točno $P$.</p>
<h3>3. Brojanje točaka u $kP$ i u njegovoj unutrašnjosti</h3>
<p>$kP$ je opisan nejednadžbama $a x + b y + c z \le k d$ (ista normala, skalirani $d$). Neka je $X = \max |{\rm koord}|$; sve točke $kP$ imaju koordinate u $[-kX, kX]$. Za svaki cjelobrojni par $(x, y)$ iz tog kvadrata prolazimo sve ravnine i održavamo interval dopuštenih $z$, početno $[-kX, kX]$:</p>
<ul>
    <li>$c = 0$: uvjet $a x + b y \le k d$ ne ovisi o $z$; ako nije ispunjen, stupac je prazan;</li>
    <li>$c > 0$: $z \le \lfloor (k d - a x - b y) / c \rfloor$ – ažuriramo gornju granicu;</li>
    <li>$c < 0$: $z \ge \lceil (a x + b y - k d) / (-c) \rceil$ – ažuriramo donju granicu.</li>
</ul>
<p>Stupac pridonosi $hi - lo + 1$ točaka ako je $lo \le hi$. Za strogo unutarnje točke svaku nejednakost zamijenimo strogom; za cijele brojeve $a x + b y + c z < k d$ ekvivalentno je $\le k d - 1$, pa je dovoljno smanjiti desnu stranu za $1$ i ponoviti isti postupak. Točka je strogo u unutrašnjosti točno kad strogo zadovoljava sve nejednadžbe stranica – to je standardna karakterizacija unutrašnjosti presjeka poluprostora.</p>
<p>Cjelobrojno dijeljenje u C++ zaokružuje prema nuli, pa za negativne brojnike pišemo vlastite $\lfloor p/q \rfloor$ i $\lceil p/q \rceil = -\lfloor -p/q \rfloor$.</p>
<h3>4. Interpolacija modulo $p$</h3>
<p>Imamo $(x_i, y_i) = (-1, -I(1)), (0, 1), (1, L(1)), (2, L(2))$. Lagrangeova formula $L(K) = \sum_i y_i \prod_{j \ne i} \frac{K - x_j}{x_i - x_j}$ je identitet racionalnih funkcija; nazivnici $\prod_{j \ne i}(x_i - x_j)$ su iz $\{-6, 2, -2, 6\}$, relativno prosti s $p$. Ako cijeli broj $L(K)$ napišemo kao $\frac{A}{6}$ s cijelim $A$, tada je $L(K) \bmod p = A \cdot 6^{-1} \bmod p$ – upravo ono što modularno računanje daje. Zato uvrštavamo $K \bmod p$, računamo brojnike i inverze nazivnika modulo $p$ i dobivamo točan ostatak. Negativnu vrijednost $y_0 = -I(1)$ normaliziramo dodavanjem $p$.</p>
<h3>5. Složenost</h3>
<p>Ravnine: $O(N^4)$, u praksi $\approx 1.6 \cdot 10^7$. Brojanje: broj stranica $F \le 2N - 4 = 196$ (Eulerova formula za trianguliranu sferu); za $k = 2$ imamo $(4X + 1)^2 \le 801^2 \approx 6.4 \cdot 10^5$ stupaca $\times F$, oko $1.3 \cdot 10^8$ jednostavnih operacija, a dva prolaza za $k = 1$ su po četiri puta manja. Ukupno ispod pola sekunde uz limit $4$ s. Interpolacija je $O(1)$.</p>
<h3>6. Provjera na primjeru</h3>
<p>Standardni tetraedar $(0,0,0), (1,0,0), (0,1,0), (0,0,1)$: $L(k) = \binom{k+3}{3}$. Naši čvorovi: $I(1) = 0$ pa $L(-1) = 0 = \binom{2}{3}$; $L(0) = 1$; $L(1) = 4$; $L(2) = 10$. Kubni polinom kroz te točke je $\binom{K+3}{3}$, pa je za $K = 2$ odgovor $10$, kao u primjeru. Za velike $K$, npr. $K = 10^{15}$, formula daje $\binom{K+3}{3} \bmod p$ bez ikakvog brojanja.</p>
<h3>7. Rubni slučajevi</h3>
<ul>
    <li>$K = 1$: interpolacija vraća točno $L(1)$.</li>
    <li>Stranice s više od tri koplanarne točke: deduplikacija po normaliziranoj četvorci $(a, b, c, d)$ je nužna, inače bismo isti poluprostor primjenjivali više puta (rezultat bi ostao točan, ali sporije).</li>
    <li>Ulazne točke koje nisu vrhovi ljuske (unutarnje ili na stranici) ne smetaju: uvjet „sve s iste strane” koristi sve točke, a ravnine stranica ne ovise o njima.</li>
    <li>Točke smiju biti negativne; zato prolaz ide po $[-kX, kX]$, a ne po $[0, kX]$.</li>
</ul>
''',
    'verified': r'''uzorci 3/3; 300 slučajnih malih testova ($4 \le N \le 6$, koordinate u $[-3, 3]$, $K \le 4$) protiv brute forcea koji izravno prolazi sve cjelobrojne točke kutije i provjerava pripadnost ljusci preko Carathéodoryjeva teorema (točka je u ljusci ako je u nekom nedegeneriranom tetraedru ulaznih točaka); 3 velika testa s $N = 100$, koordinatama do $200$ (uključujući točke na sferi, gdje ljuska ima najviše stranica) i $K$ do $10^{15}$, najsporiji $0.45$ s.''',
},
# ---------------------------------------------------------------- I
{
    'letter': 'I', 'title': 'Peaceful Results', 'title_hr': 'Miroljubivi rezultati', 'slug': 'I_peaceful_results',
    'tl': '2 s', 'ml': '1024 MB',
    'statement': r'''
<p>Alice, Bob i Chris igraju kamen–papir–škare $N$ puta. Alice mora odigrati kamen točno $A_R$ puta, papir $A_P$ i škare $A_S$ puta; analogno Bob ($B_R, B_P, B_S$) i Chris ($C_R, C_P, C_S$). Žele da svaka od $N$ igara bude neriješena. Prebroji načine odabira poteza svih triju igrača kroz $N$ rundi, modulo $998244353$.</p>
<h3>Ulaz</h3>
<p>$N$ ($1 \le N \le 1.5 \cdot 10^6$) i tri retka s po tri broja; svaki redak ima zbroj $N$.</p>
<h3>Izlaz</h3>
<p>Broj načina.</p>
<h3>Primjer</h3>
<p>Za $N = 2$, Alice $(2, 0, 0)$, Bob $(1, 1, 0)$, Chris $(1, 0, 1)$ odgovor je $2$.</p>
''',
    'hints': [
        r'''<p>Runda je neriješena u točno $9$ kombinacija: $RRR, PPP, SSS$ i šest permutacija $RPS$. Neka je $X_1..X_9$ broj rundi svake vrste; broj rasporeda je multinomni koeficijent $N!/\prod X_t!$.</p>''',
        r'''<p>Ograničenja igrača daju $9$ linearnih jednadžbi ranga $7$. Razlike $Y_2 = X_2 - X_1$, $Y_3 = X_3 - X_1$, $Y_5 = X_5 - X_4$, … određene su jednoznačno, a slobodni ostaju $x_1, x_4, x_7$ s uvjetom $x_1 + x_4 + x_7 = C$.</p>''',
        r'''<p>Zbroj $\sum \frac{N!}{x_1!(x_1+Y_2)!(x_1+Y_3)! \cdots}$ po $x_1 + x_4 + x_7 = C$ je konvolucija triju nizova — FFT/NTT.</p>''',
    ],
    'coach': [
        ('Što znači „runda je neriješena” s tri igrača i koliko je takvih kombinacija poteza?',
         r'''
<p>Runda ima pobjednika točno kad se pojave točno dva različita simbola (npr. $R, R, P$ – papir pobjeđuje). Neriješeno je dakle ako su sva tri simbola jednaka ($RRR, PPP, SSS$) ili sva tri različita ($3! = 6$ rasporeda simbola $R, P, S$ po igračima). Ukupno $9$ tipova rundi. Označimo brojeve rundi po tipu: $a_1, a_2, a_3$ za jednake, $b_1, b_2, b_3$ za „cikličke” $(R,P,S), (P,S,R), (S,R,P)$ i $c_1, c_2, c_3$ za „anticikličke” $(R,S,P), (P,R,S), (S,P,R)$ (redom Alice, Bob, Chris).</p>
'''),
        ('Ako znamo koliko je rundi svakog tipa, koliko je načina odigravanja? I koje uvjete tipovi moraju zadovoljiti?',
         r'''
<p>Rasporediti $N$ rundi po tipovima je multinomni koeficijent $\frac{N!}{\prod a_j! \prod b_j! \prod c_j!}$ – tipovi potpuno određuju poteze svih igrača u toj rundi. Uvjeti: Alice igra kamen u tipovima $a_1, b_1, c_1$, pa $a_1 + b_1 + c_1 = A_R$; slično za $9$ kvota. Dakle $9$ linearnih jednadžbi u $9$ nepoznanica – ali nisu neovisne (zbrojevi redaka su svi $N$), rang je $7$, pa ostaju $2$ slobodna parametra. Naivno bismo zbrajali po $O(N^2)$ rješenja s $O(1)$ po članu – previše za $N = 1.5 \cdot 10^6$.</p>
'''),
        ('Koje su veličine određene jednoznačno, a koje slobodne?',
         r'''
<p>Oduzmimo Bobove i Chrisove kvote od Aliceinih: razlike $A_R - B_R$, $A_P - B_P$, $A_R - C_R$, $A_P - C_P$ ne sadrže $a_j$ (svi igraju isto) i ovise samo o razlikama unutar cikličke i anticikličke skupine: $\beta_2 = b_2 - b_1$, $\beta_3 = b_3 - b_1$, $\gamma_2 = c_2 - c_1$, $\gamma_3 = c_3 - c_1$. To je regularan $4 \times 4$ sustav s determinantom djeljivom s $3$: rješenja imaju nazivnik $3$, pa ako brojnici nisu djeljivi s $3$, odgovor je $0$. Slobodni ostaju $s = b_1$ i $t = c_1$; tada je $b = (s, s + \beta_2, s + \beta_3)$, $c = (t, t + \gamma_2, t + \gamma_3)$ i $a_j = \alpha_j - (s + t)$ za konstante $\alpha_j$.</p>
'''),
        ('Zbroj po parovima $(s, t)$ ima $O(N^2)$ članova – koja mu struktura dopušta $O(N \log N)$?',
         r'''
<p>Član se rastavlja na $F(s) \cdot G(t) \cdot H(s + t)$, gdje $F$ ovisi samo o $b$-ovima, $G$ samo o $c$-ovima, a $H$ o $a$-ovima kroz $u = s + t$. Zbroj po $s + t = u$ od $F(s) G(t)$ je konvolucija $(F * G)(u)$, izračunljiva NTT-om, a zatim je odgovor $N! \sum_u H(u) (F * G)(u)$. Nenegativnost svih devet brojeva daje donje granice $s \ge s_{\min}$, $t \ge t_{\min}$ i gornju $u \le u_{\max} = \min_j \alpha_j$.</p>
'''),
        ('Gdje se lako pogriješi?',
         r'''
<p>U indeksiranju faktorijela: $F(s)$ računamo samo za $s \le u_{\max} - t_{\min}$ (i simetrično $G$), jer tada su svi indeksi $\le N$ i ostali članovi ionako ne ulaze u odgovor; provjeri djeljivost s $3$ pravilno za negativne brojeve; duljina NTT-a mora biti barem $2(u_{\max} + 1)$, do $2^{22}$ za $N = 1.5 \cdot 10^6$; i odgovor je $0$ ako je $s_{\min} + t_{\min} > u_{\max}$ ili neki $\alpha_j < 0$.</p>
'''),
    ],
    'tips': [
        r'''Brojanje nizova s kvotama po simbolima obično ide kroz <strong>multinomni koeficijent</strong> po tipovima pozicija plus linearni sustav na brojeve tipova; prvo odredi rang sustava – broj slobodnih parametara je dimenzija zbroja koji ostaje.''',
        r'''Kad zbroj po dva slobodna parametra ima oblik $\sum_{s,t} F(s) G(t) H(s+t)$, to je <strong>konvolucija</strong> $F * G$ pa skalarni umnožak s $H$ – $O(N \log N)$ NTT-om.''',
        r'''Eliminiraj zajedničke članove oduzimanjem jednadžbi (ovdje $a_j$ nestaju u razlikama kvota igrača) – manji, regularan sustav rješava se ručno i daje uvjete cjelobrojnosti (djeljivost s determinantom).''',
        r'''Prije NTT-a provjeri sve rubne uvjete (negativne granice, prazan raspon) i ispiši $0$ – tako ni faktorijeli negativnog argumenta ni prazna konvolucija ne mogu srušiti program.''',
    ],
    'solution': r'''
<p>Kombinacije poteza koje daju neriješenu rundu su $RRR, PPP, SSS, RPS, PSR, SRP, RSP, PRS, SPR$. Neka je $X_1, \dots, X_9$ broj pojavljivanja svake kombinacije u $N$ rundi. Tada je broj načina odigravanja $N$ rundi s tim brojevima jednak $\frac{N!}{X_1! X_2! \cdots X_9!}$.</p>
<p>Razmotrimo uvjete na $X_1, \dots, X_9$. Iz ukupnog broja korištenja svakog poteza dobivamo sustav:</p>
<p>$$\begin{aligned}
X_1 + X_4 + X_7 &= A_R, & X_2 + X_5 + X_8 &= A_P, & X_3 + X_6 + X_9 &= A_S,\\
X_1 + X_6 + X_8 &= B_R, & X_2 + X_4 + X_9 &= B_P, & X_3 + X_5 + X_7 &= B_S,\\
X_1 + X_5 + X_9 &= C_R, & X_2 + X_6 + X_7 &= C_P, & X_3 + X_4 + X_8 &= C_S.
\end{aligned}$$</p>
<p>Rang ove $9 \times 9$ matrice je $7$, pa $X_1, \dots, X_9$ nisu jednoznačno određeni. Definiramo li $Y_2 = X_2 - X_1$, $Y_3 = X_3 - X_1$, $Y_5 = X_5 - X_4$, $Y_6 = X_6 - X_4$, $Y_8 = X_8 - X_7$, $Y_9 = X_9 - X_7$, dobivamo $6 \times 6$ sustav punog ranga s desnom stranom $(A_P - A_R, A_S - A_R, B_P - B_R, B_S - B_R, C_P - C_R, C_S - C_R)$, pa su $Y_2, Y_3, Y_5, Y_6, Y_8, Y_9$ jednoznačno određeni; nužno je da budu cijeli brojevi.</p>
<p>Stoga se $(X_1, \dots, X_9)$ može zapisati kao $(x_1, x_1 + Y_2, x_1 + Y_3, x_4, x_4 + Y_5, x_4 + Y_6, x_7, x_7 + Y_8, x_7 + Y_9)$ s tri cjelobrojne varijable $x_1, x_4, x_7$ i šest konstanti. Kako svi moraju biti nenegativni i zbroj im mora biti $N$, postoje nenegativne konstante $C, l_1, l_4, l_7$ takve da je $x_1 + x_4 + x_7 = C$, $x_1 \ge l_1$, $x_4 \ge l_4$, $x_7 \ge l_7$, a unutar tih uvjeta $x_1, x_4, x_7$ su slobodni.</p>
<p>Treba izračunati zbroj izraza</p>
<p>$$\frac{N!}{x_1!\,(x_1+Y_2)!\,(x_1+Y_3)!\ x_4!\,(x_4+Y_5)!\,(x_4+Y_6)!\ x_7!\,(x_7+Y_8)!\,(x_7+Y_9)!}$$</p>
<p>po svim dopuštenim $x_1, x_4, x_7$, što se efikasno računa FFT-om (konvolucijom triju nizova). Vremenska složenost je $O(N \log N)$.</p>
''',
    'detailed': r'''
<h3>1. Devet tipova neriješene runde i multinomni koeficijent</h3>
<p>Runda s tri igrača ima pobjednika točno kad se pojave točno dva različita simbola; neriješena je ako su svi jednaki ili svi različiti. Tipove označimo (potezi Alice, Bob, Chris):</p>
<ul>
    <li>$a_1 = RRR$, $a_2 = PPP$, $a_3 = SSS$;</li>
    <li>ciklički: $b_1 = (R,P,S)$, $b_2 = (P,S,R)$, $b_3 = (S,R,P)$;</li>
    <li>anticiklički: $c_1 = (R,S,P)$, $c_2 = (P,R,S)$, $c_3 = (S,P,R)$.</li>
</ul>
<p>Za zadane brojeve rundi po tipovima (sa zbrojem $N$) broj načina odigravanja je multinomni koeficijent $\dfrac{N!}{\prod_j a_j! \, b_j! \, c_j!}$: biramo koje runde pripadaju kojem tipu, a tip određuje poteze svih troje. Odgovor je zbroj tog izraza po svim nenegativnim cjelobrojnim $(a, b, c)$ koji poštuju kvote.</p>
<h3>2. Kvote kao linearni sustav</h3>
<p>Alice igra $R$ u tipovima $a_1, b_1, c_1$, $P$ u $a_2, b_2, c_2$, $S$ u $a_3, b_3, c_3$. Bob igra $R$ u $a_1, b_3, c_2$; $P$ u $a_2, b_1, c_3$; $S$ u $a_3, b_2, c_1$. Chris igra $R$ u $a_1, b_2, c_3$; $P$ u $a_2, b_3, c_1$; $S$ u $a_3, b_1, c_2$. Devet jednadžbi:</p>
<p>$$\begin{aligned}
a_1 + b_1 + c_1 &= A_R, & a_2 + b_2 + c_2 &= A_P, & a_3 + b_3 + c_3 &= A_S,\\
a_1 + b_3 + c_2 &= B_R, & a_2 + b_1 + c_3 &= B_P, & a_3 + b_2 + c_1 &= B_S,\\
a_1 + b_2 + c_3 &= C_R, & a_2 + b_3 + c_1 &= C_P, & a_3 + b_1 + c_2 &= C_S.
\end{aligned}$$</p>
<p>Zbroj svakog retka je $N$, pa su jednadžbe zavisne; rang je $7$ i rješenje ima dva slobodna parametra. (Ako kvote nisu konzistentne, sustav nema rješenja i odgovor je $0$; to će se očitovati u uvjetima ispod.)</p>
<h3>3. Eliminacija zajedničkih članova</h3>
<p>Oduzmimo Bobove kvote od Aliceinih i Chrisove od Aliceinih za simbole $R$ i $P$; $a_j$ se pokrate:</p>
<p>$$\begin{aligned}
D_{1R} &= A_R - B_R = (b_1 - b_3) + (c_1 - c_2), & D_{1P} &= A_P - B_P = (b_2 - b_1) + (c_2 - c_3),\\
D_{2R} &= A_R - C_R = (b_1 - b_2) + (c_1 - c_3), & D_{2P} &= A_P - C_P = (b_2 - b_3) + (c_2 - c_1).
\end{aligned}$$</p>
<p>Uvedimo $\beta_2 = b_2 - b_1$, $\beta_3 = b_3 - b_1$, $\gamma_2 = c_2 - c_1$, $\gamma_3 = c_3 - c_1$. Tada je $D_{1R} = -\beta_3 - \gamma_2$, $D_{1P} = \beta_2 + \gamma_2 - \gamma_3$, $D_{2R} = -\beta_2 - \gamma_3$, $D_{2P} = \beta_2 - \beta_3 + \gamma_2$. Iz prve i treće: $\gamma_2 = -\beta_3 - D_{1R}$, $\gamma_3 = -\beta_2 - D_{2R}$; uvrštavanjem u ostale dvije dobivamo $2\beta_2 - \beta_3 = D_{1P} + D_{1R} - D_{2R}$ i $\beta_2 - 2\beta_3 = D_{2P} + D_{1R}$, odakle</p>
<p>$$\beta_2 = \frac{2D_{1P} + D_{1R} - D_{2P} - 2D_{2R}}{3}, \quad \beta_3 = \frac{D_{1P} - D_{1R} - 2D_{2P} - D_{2R}}{3}, \quad \gamma_2 = -\frac{D_{1P} + 2D_{1R} - 2D_{2P} - D_{2R}}{3}, \quad \gamma_3 = -\frac{2D_{1P} + D_{1R} - D_{2P} + D_{2R}}{3}.$$</p>
<p>Sustav je regularan pa su razlike jednoznačne; ako neki brojnik nije djeljiv s $3$, cjelobrojnog rješenja nema i odgovor je $0$. Razlike za simbol $S$ ($A_S - B_S$ itd.) automatski su zadovoljene jer su zbrojevi redaka jednaki $N$.</p>
<h3>4. Parametrizacija svih rješenja</h3>
<p>Slobodni parametri: $s = b_1$, $t = c_1$. Tada $b = (s, s + \beta_2, s + \beta_3)$, $c = (t, t + \gamma_2, t + \gamma_3)$, a iz Aliceinih kvota</p>
<p>$$a_1 = A_R - s - t, \quad a_2 = A_P - \beta_2 - \gamma_2 - (s + t), \quad a_3 = A_S - \beta_3 - \gamma_3 - (s + t),$$</p>
<p>tj. $a_j = \alpha_j - u$ uz $u = s + t$ i konstante $\alpha_1 = A_R$, $\alpha_2 = A_P - \beta_2 - \gamma_2$, $\alpha_3 = A_S - \beta_3 - \gamma_3$. Sve preostale jednadžbe (Bob, Chris) tada vrijede jer smo ih iskoristili kroz razlike, a ukupni zbroj je $A_R + A_P + A_S = N$. Nenegativnost: $s \ge s_{\min} = \max(0, -\beta_2, -\beta_3)$, $t \ge t_{\min} = \max(0, -\gamma_2, -\gamma_3)$, $u \le u_{\max} = \min_j \alpha_j$. Ako je $u_{\max} < 0$ ili $s_{\min} + t_{\min} > u_{\max}$, odgovor je $0$.</p>
<h3>5. Konvolucija</h3>
<p>Definirajmo</p>
<p>$$F(s) = \frac{1}{s! \,(s + \beta_2)! \,(s + \beta_3)!}, \qquad G(t) = \frac{1}{t! \,(t + \gamma_2)! \,(t + \gamma_3)!}, \qquad H(u) = \frac{1}{(\alpha_1 - u)! \,(\alpha_2 - u)! \,(\alpha_3 - u)!}$$</p>
<p>(nula izvan dopuštenih raspona). Tada je</p>
<p>$$\text{odgovor} = N! \sum_{u = 0}^{u_{\max}} H(u) \sum_{s + t = u} F(s) \, G(t) = N! \sum_{u} H(u) \, (F * G)(u).$$</p>
<p>Konvoluciju računamo NTT-om modulo $998244353$ u duljini $2^k \ge 2(u_{\max} + 1)$; za $N = 1.5 \cdot 10^6$ to je $2^{22}$. Faktorijeli i inverzni faktorijeli do $N$ predizračunaju se u $O(N)$.</p>
<h3>6. Indeksi faktorijela</h3>
<p>Za $s \le u_{\max} - t_{\min}$ postoji $t \ge t_{\min}$ s $s + t \le u_{\max}$, pa je $b_2 = s + \beta_2 = A_P - a_2 - c_2 \le A_P \le N$ (jer $a_2, c_2 \ge 0$), slično $b_3 \le A_S$; za veće $s$ konvolucija daje samo indekse $u > u_{\max}$ koji ne ulaze u odgovor, pa $F(s)$ tamo ne računamo. Isto za $G$ do $u_{\max} - s_{\min}$. Time su svi argumenti faktorijela u $[0, N]$ i tablica duljine $N + 1$ dostaje.</p>
<h3>7. Složenost i provjera</h3>
<p>$O(N \log N)$ za NTT, $O(N)$ ostalo; memorija nekoliko nizova od $2^{22}$ 64-bitnih brojeva ($\approx 100$ MB od dopuštenih $1024$). Primjer $N = 2$, $A = (2,0,0)$, $B = (1,1,0)$, $C = (1,0,1)$: $D_{1R} = 1$, $D_{1P} = -1$, $D_{2R} = 1$, $D_{2P} = 0$; $\beta_2 = (-2 + 1 - 0 - 2)/3 = -1$, $\beta_3 = (-1 - 1 - 0 - 1)/3 = -1$, $\gamma_2 = -(-1 + 2 - 0 - 1)/3 = 0$, $\gamma_3 = -(-2 + 1 - 0 + 1)/3 = 0$. Dakle $b = (s, s-1, s-1)$, $c = (t, t, t)$, $\alpha = (2, 0 + 1 - 0, 0 + 1 - 0) = (2, 1, 1)$, $u_{\max} = 1$, $s_{\min} = 1$, $t_{\min} = 0$. Jedino rješenje: $s = 1, t = 0$: $b = (1, 0, 0)$, $c = (0,0,0)$, $a = (1, 0, 0)$ – jedna runda $RRR$ i jedna $(R, P, S)$, u dva moguća redoslijeda: $\frac{2!}{1! \, 1!} = 2$. Točno.</p>
''',
    'verified': r'''uzorci 3/3; 300 slučajnih malih testova ($N \le 6$; $60\,\%$ generirano iz stvarnih neriješenih nizova, ostalo proizvoljne kvote s odgovorom često $0$) protiv brute forcea koji prolazi svih $9^N$ nizova neriješenih tipova rundi i provjerava kvote; dodatno $3000$ nasumičnih kvota uz AddressSanitizer bez grešaka u indeksiranju; 3 velika testa s $N = 1.5 \cdot 10^6$, najsporiji $0.11$ s.''',
},
# ---------------------------------------------------------------- J
{
    'letter': 'J', 'title': 'Make Convex Sequence', 'title_hr': 'Napravi konveksan niz', 'slug': 'J_make_convex_sequence',
    'tl': '2 s', 'ml': '1024 MB',
    'statement': r'''
<p>Dani su nizovi $L$ i $R$ duljine $N$. Postoji li niz realnih brojeva $A$ takav da je $L_i \le A_i \le R_i$ za sve $i$ i $A_{i-1} + A_{i+1} \ge 2A_i$ za sve $2 \le i \le N-1$ (niz je konveksan)?</p>
<h3>Ulaz</h3>
<p>$N$ ($3 \le N \le 3 \cdot 10^5$), zatim $L_1..L_N$ i $R_1..R_N$ ($1 \le L_i \le R_i \le 10^9$).</p>
<h3>Izlaz</h3>
<p><code>Yes</code> ili <code>No</code>.</p>
<h3>Primjer</h3>
<p>Za $L = (2, 1, 2, 5)$, $R = (4, 6, 5, 8)$ odgovor je Yes, npr. $A = (4, 3/2, 3, 7)$.</p>
''',
    'hints': [
        r'''<p>Konveksni nizovi su zatvoreni na pointwise maksimum. Zato među svim konveksnim nizovima s $A_i \le R_i$ postoji najveći — to je donja konveksna ljuska točaka $(i, R_i)$.</p>''',
        r'''<p>Ako najveći takav niz $T$ zadovoljava $L_i \le T_i$, odgovor je Yes; inače nijedan drugi ne može (svi su $\le T$). Donju ljusku računaj monotonim lancem (Andrew) u $O(N)$.</p>''',
    ],
    'coach': [
        ('Uvjeti su linearni – možemo li ih riješiti kao linearni program? Što je posebno u strukturi ovih uvjeta?',
         r'''
<p>Općeniti LP s $3 \cdot 10^5$ varijabli je prespor, ali uvjeti imaju posebnu strukturu: $A_{i-1} + A_{i+1} \ge 2 A_i$ znači da su razlike $A_{i+1} - A_i$ neopadajuće – graf niza je <em>konveksna</em> izlomljena linija. Konveksne funkcije imaju svojstvo koje LP nema općenito: <strong>maksimum po točkama dviju konveksnih funkcija je konveksan</strong> ($\max$ konveksnih je konveksno). Zato skup dopuštenih nizova (bez uvjeta $L$) ima najveći element.</p>
'''),
        ('Ako uzmemo samo uvjete „konveksan” i „$A \le R$”, koji je najveći takav niz?',
         r'''
<p>Donja konveksna ljuska točaka $(i, R_i)$, označimo je $T$. Ona je konveksna (ljuska je konveksan skup pa je njezin donji rub konveksna funkcija), vrijedi $T_i \le R_i$ (točka $(i, R_i)$ je u ljusci, iznad donjeg ruba), a za svaki konveksan niz $A \le R$ vrijedi $A \le T$: neka je $i$ između uzastopnih vrhova ljuske $p < q$; zbog konveksnosti $A_i$ leži ispod tetive kroz $(p, A_p)$ i $(q, A_q)$, a ona je ispod tetive kroz $(p, R_p)$ i $(q, R_q)$, što je upravo $T$ na $[p, q]$.</p>
'''),
        ('Zašto je onda dovoljno provjeriti samo $T$ protiv $L$?',
         r'''
<p>Ako $L_i \le T_i$ za sve $i$, niz $A = T$ zadovoljava sve uvjete (konveksan, $L \le T \le R$) – odgovor je Yes. Ako za neki $i$ vrijedi $T_i < L_i$, tada za <em>svaki</em> konveksan $A \le R$ vrijedi $A_i \le T_i < L_i$, pa rješenja nema – odgovor je No. Uvjeti za $L$ ne „guraju” niz prema gore na koristan način: gornja granica $T$ ne ovisi o $L$.</p>
'''),
        ('Kako izračunati $T$ i usporediti ga s $L$ bez realnih brojeva?',
         r'''
<p>Točke $(i, R_i)$ već su sortirane po $x$, pa Andrewov monotoni lanac daje donju ljusku u $O(N)$ jednim prolazom sa stogom: novi indeks izbacuje vrh dok trojka ne čini lijevi zavoj (vektorski produkt $> 0$). Između vrhova $p < q$ ljuske vrijednost $T_i$ je linearna interpolacija; uvjet $L_i \le T_i$ pomnožimo s $(q - p) > 0$: $L_i (q - p) \le R_p (q - p) + (R_q - R_p)(i - p)$ – sve cjelobrojno, veličine do $10^9 \cdot 3 \cdot 10^5 = 3 \cdot 10^{14}$, stane u 64 bita.</p>
'''),
    ],
    'tips': [
        r'''Uvjet $A_{i-1} + A_{i+1} \ge 2A_i$ prepoznaj kao <strong>konveksnost niza</strong> (neopadajuće razlike); konveksne su funkcije zatvorene na maksimum, konkavne na minimum – to često daje „najveće/najmanje dopušteno rješenje” bez LP-a.''',
        r'''Kad su uvjeti oblika „$A \le R$ + svojstvo zatvoreno na max”, izračunaj najveći dopušteni $A$ i tek onda provjeri donje granice; izvedivost se svodi na jednu usporedbu.''',
        r'''Donja konveksna ljuska točaka sortiranih po $x$ računa se u $O(N)$ monotonim lancem; interpolacije uspoređuj pomnožene nazivnikom da izbjegneš razlomke i grešku realnih brojeva.''',
        r'''Provjeri ovakve zadatke Fourier–Motzkinovom eliminacijom ili LP-om na malim primjerima – to je egzaktan brute force za sustave linearnih nejednakosti.''',
    ],
    'solution': r'''
<p>Neka je $S$ konveksna ljuska skupa točaka $\{(i, y) \mid y \ge R_i\}$ i definirajmo niz $T$ s $T_i = \min\{y \mid (i, y) \in S\}$ — drugim riječima, $T$ je donja konveksna ljuska niza $R$.</p>
<p>Tako dobiveni $T$ je „najveći” niz koji zadovoljava sve uvjete zadatka osim uvjeta koji se tiče $L$. Preciznije, za svaki niz $A$ koji zadovoljava $A_i \le R_i$ za sve $i$ i $A_{i-1} + A_{i+1} \ge 2A_i$ za sve $2 \le i \le N-1$ vrijedi $A_i \le T_i$; to slijedi iz definicije konveksne ljuske.</p>
<p>Stoga je odgovor Yes ako $T$ zadovoljava $L_i \le T_i$ za sve $i$, a inače No. Niz $T$ računamo u $O(N)$ npr. Andrewovim algoritmom monotonog lanca.</p>
''',
    'detailed': r'''
<h3>1. Konveksnost i zatvorenost na maksimum</h3>
<p>Uvjet $A_{i-1} + A_{i+1} \ge 2A_i$ ekvivalentan je $A_{i+1} - A_i \ge A_i - A_{i-1}$: razlike su neopadajuće, tj. niz je konveksan. Iz toga slijedi <em>svojstvo tetive</em>: za $p \le i \le q$ vrijedi $A_i \le \frac{(q - i) A_p + (i - p) A_q}{q - p}$. Dokaz: neka su $\delta_j = A_{j+1} - A_j$ neopadajuće; tada je $A_i - A_p = \sum_{j=p}^{i-1} \delta_j \le (i - p)\,\delta_{i-1}$ i $A_q - A_i = \sum_{j=i}^{q-1} \delta_j \ge (q - i)\,\delta_i \ge (q - i)\,\delta_{i-1}$, pa $(q - i)(A_i - A_p) \le (i - p)(A_q - A_i)$, što je prestrojeno traženo. Obrnuto, niz koji zadovoljava svojstvo tetive za sve trojke $p < i < q$ zadovoljava ga i za $q = p + 2$, što je upravo izvorni uvjet.</p>
<p>Ako su $A$ i $B$ konveksni, $C_i = \max(A_i, B_i)$ je konveksan: $C_{i-1} + C_{i+1} \ge A_{i-1} + A_{i+1} \ge 2A_i$ i isto za $B$, pa $C_{i-1} + C_{i+1} \ge 2\max(A_i, B_i) = 2C_i$. Skup konveksnih nizova s $A \le R$ zato je zatvoren na konačne maksimume i, kako je odozgo ograničen, ima najveći element (točkovni supremum svih elemenata; on je i sam konveksan jer se konveksnost čuva pri supremumu).</p>
<h3>2. Najveći element je donja ljuska</h3>
<p>Neka je $T$ donja konveksna ljuska točaka $(i, R_i)$, tj. $T_i = \min\{y : (i, y) \in \text{conv}\{(j, R_j)\}\}$. Tvrdnja: $T$ je najveći konveksan niz ispod $R$.</p>
<ul>
    <li><strong>$T$ je konveksan.</strong> Donji rub konveksnog skupa je konveksna funkcija (za točke $(i, T_i)$ i $(k, T_k)$ u skupu i tetiva je u skupu, pa je $T$ ispod tetive).</li>
    <li><strong>$T \le R$.</strong> Točka $(i, R_i)$ pripada ljusci, a $T_i$ je najmanja ordinata ljuske nad $i$.</li>
    <li><strong>Svaki konveksan $A \le R$ zadovoljava $A \le T$.</strong> Ljuska je izlomljena linija s vrhovima $h_0 < h_1 < \dots < h_m$ (indeksi ulaznih točaka; $h_0$ je prvi, a $h_m$ posljednji indeks). Za $i \in [p, q] = [h_s, h_{s+1}]$ vrijedi $T_i = \frac{(q - i) R_p + (i - p) R_q}{q - p}$. Po svojstvu tetive $A_i \le \frac{(q - i) A_p + (i - p) A_q}{q - p} \le \frac{(q - i) R_p + (i - p) R_q}{q - p} = T_i$, jer $A_p \le R_p$, $A_q \le R_q$ i težine su nenegativne.</li>
</ul>
<h3>3. Kriterij</h3>
<p>Ako je $L_i \le T_i$ za sve $i$, tada je $A = T$ rješenje (konveksan, $L \le T \le R$). Inače postoji $i$ s $T_i < L_i$, a za svaki dopušteni $A$ (konveksan i $\le R$) vrijedi $A_i \le T_i < L_i$ – kontradikcija s $A_i \ge L_i$. Dakle: <strong>odgovor je Yes ako i samo ako $L \le T$ po točkama.</strong></p>
<h3>4. Algoritam</h3>
<ol>
    <li>Prođi indekse $i = 0, \dots, N-1$ (0-indeksirano) i održavaj stog vrhova donje ljuske: dok stog ima barem dva vrha $a, b$ i vektorski produkt $(b - a)(R_i - R_a) - (i - a)(R_b - R_a) \le 0$ (točka $b$ nije strogo iznad tetive $a \to i$, tj. nije lijevi zavoj), izbaci $b$; zatim stavi $i$. Kolinearne točke izbacujemo ($\le 0$), što ne mijenja $T$.</li>
    <li>Za svaki par uzastopnih vrhova $p < q$ i svaki $i \in [p, q]$ provjeri $L_i (q - p) \le R_p (q - p) + (R_q - R_p)(i - p)$. Ako ikad ne vrijedi, ispiši No; inače Yes.</li>
</ol>
<p>Prvi i posljednji indeks uvijek su vrhovi ljuske, pa segmenti pokrivaju sve indekse. Svaki indeks se stavlja i izbacuje najviše jednom, a provjera obiđe svaki indeks jednom (rubni indeksi segmenata dvaput): ukupno $O(N)$.</p>
<h3>5. Cjelobrojna aritmetika</h3>
<p>Vektorski produkt: $(b - a) \le 3 \cdot 10^5$, $|R_i - R_a| < 10^9$, umnožak $< 3 \cdot 10^{14}$; usporedba interpolacije: $L_i (q - p) \le 10^9 \cdot 3 \cdot 10^5 = 3 \cdot 10^{14}$. Sve u <code>long long</code>, bez realnih brojeva i bez dijeljenja, pa nema pogrešaka zaokruživanja (rješenje $T$ je racionalno, a usporedba s cijelim $L_i$ mora biti egzaktna).</p>
<h3>6. Primjer</h3>
<p>$L = (2, 1, 2, 5)$, $R = (4, 6, 5, 8)$; točke $(0,4), (1,6), (2,5), (3,8)$. Lanac: $\{0\}$, $\{0,1\}$; za $i = 2$: vektorski produkt $(1-0)(5-4) - (2-0)(6-4) = 1 - 4 < 0$, izbacujemo $1$ (točka $(1,6)$ je iznad tetive $0 \to 2$), stog $\{0, 2\}$; za $i = 3$: $(2-0)(8-4) - (3-0)(5-4) = 8 - 3 > 0$, stog $\{0, 2, 3\}$. $T = (4, 4.5, 5, 8)$; provjera na segmentu $[0, 2]$: $L_1 \cdot 2 = 2 \le 4 \cdot 2 + 1 \cdot 1 = 9$ ✓, $L_2 \cdot 2 = 4 \le 8 + 2 = 10$ ✓; na $[2, 3]$: $L_3 = 5 \le 8$ ✓. Odgovor Yes (primjer iz zadatka nudi drugi valjani niz $(4, 3/2, 3, 7)$ – rješenje nije jedinstveno, ali $T$ je uvijek jedno od njih kad ono postoji).</p>
<h3>7. Rubni slučajevi</h3>
<p>$N = 3$: ljuska ima dva ili tri vrha, provjera je trivijalna. Svi $R_i$ jednaki: $T$ je konstanta $R$, odgovor Yes ako i samo ako $L \le R$ (uvijek). Strogo konkavan $R$ (npr. $R_i = -i^2$ pomaknuto): ljuska je jedna tetiva od prvog do zadnjeg indeksa, pa $T$ može biti daleko ispod $R$ u sredini – tu $L$ obično ruši rješenje.</p>
''',
    'verified': r'''uzorci 2/2; 300 slučajnih malih testova ($3 \le N \le 6$, vrijednosti do $12$) protiv egzaktnog brute forcea koji Fourier–Motzkinovom eliminacijom nad razlomcima provjerava izvedivost sustava linearnih nejednakosti; 3 velika testa s $N = 3 \cdot 10^5$ (slučajni intervali i gotovo napeti konveksni oblik), najsporiji $0.04$ s.''',
},
# ---------------------------------------------------------------- K
{
    'letter': 'K', 'title': 'Count Arithmetic Progression', 'title_hr': 'Prebroji aritmetičke nizove', 'slug': 'K_count_arithmetic_progression',
    'tl': '2 s', 'ml': '1024 MB',
    'statement': r'''
<p>Dani su nizovi $L$ i $R$ duljine $N$. Prebroji cjelobrojne aritmetičke nizove $A$ (tj. $A_{i+1} - A_i = d$ za sve $i$, uz isti $d$) takve da je $L_i \le A_i \le R_i$ za sve $i$, modulo $998244353$.</p>
<h3>Ulaz</h3>
<p>$N$ ($2 \le N \le 3 \cdot 10^5$), zatim $L_1..L_N$ i $R_1..R_N$ ($1 \le L_i \le R_i \le 10^{12}$).</p>
<h3>Izlaz</h3>
<p>Broj nizova.</p>
<h3>Primjer</h3>
<p>Za $L = (5, 5, 2)$, $R = (7, 6, 7)$ odgovor je $6$.</p>
''',
    'hints': [
        r'''<p>Niz je određen parom $(A_0, d)$. Za fiksni $d$ uvjeti $L_i \le A_0 + id \le R_i$ daju $\max_i (L_i - id) \le A_0 \le \min_i (R_i - id)$.</p>''',
        r'''<p>$\max_i (L_i - id)$ je maksimum linearnih funkcija u $d$ — konveksna izlomljena linija (gornja ovojnica, Convex Hull Trick); $\min_i (R_i - id)$ je konkavna. Traži se broj cjelobrojnih točaka $(d, A_0)$ između njih.</p>''',
        r'''<p>Podijeli os $d$ na $O(N)$ intervala na kojima su obje ovojnice linearne; na svakom intervalu broj cjelobrojnih točaka između dviju linearnih funkcija je zbroj aritmetičkog niza — $O(1)$, ali pazi na zaokruživanja (floor/ceil) i na prazne intervale.</p>''',
    ],
    'coach': [
        ('Aritmetički niz ima dva parametra – kako uvjete na $N$ članova pretvoriti u uvjete na ta dva parametra?',
         r'''
<p>Indeksirajmo od $0$: $A_i = A_0 + i d$. Uvjet $L_i \le A_0 + i d \le R_i$ je $L_i - i d \le A_0 \le R_i - i d$. Za fiksan cjelobrojni $d$ svi uvjeti zajedno daju interval za $A_0$: $\ell(d) = \max_i (L_i - i d) \le A_0 \le u(d) = \min_i (R_i - i d)$, a kako su $L, R, d$ cijeli, i granice su cijele. Odgovor je $\sum_{d} \max(0, u(d) - \ell(d) + 1)$. Raspon $d$ je konačan: iz $i = 0, 1$ slijedi $d = A_1 - A_0 \in [L_1 - R_0, R_1 - L_0]$.</p>
'''),
        ('Raspon $d$ ima do $2 \cdot 10^{12}$ vrijednosti – kakve su funkcije $\ell$ i $u$ i kako ih opisati s $O(N)$ podataka?',
         r'''
<p>$\ell(d)$ je maksimum $N$ pravaca $y = -i \cdot d + L_i$ – konveksna izlomljena linija (gornja ovojnica), $u(d)$ minimum pravaca $y = -i \cdot d + R_i$ – konkavna (donja ovojnica). Svaki pravac je „aktivan” na najviše jednom intervalu, pa ovojnica ima $O(N)$ komada. Nagibi $-i$ su različiti i već sortirani, pa se ovojnica gradi standardnim trikom konveksne ljuske stogom u $O(N)$: pravac na vrhu stoga izbacujemo ako ga novi pravac i onaj pod njim potpuno „pokriju” (usporedba sjecišta bez dijeljenja).</p>
'''),
        ('Kad znamo komade, kako zbrojiti $\max(0, u(d) - \ell(d) + 1)$ po svim cjelobrojnim $d$ u $O(1)$ po komadu?',
         r'''
<p>Presjecimo raspon $[d_{\min}, d_{\max}]$ točkama loma obiju ovojnica (dva pokazivača): dobijemo $O(N)$ intervala na kojima su aktivni pravci fiksni, pa je $c(d) = u(d) - \ell(d) + 1$ linearna s cjelobrojnim koeficijentima $c(d) = \alpha d + \beta$. Uvjet $c(d) \ge 1$ rješavamo dijeljenjem s pravilnim $\lfloor \cdot \rfloor / \lceil \cdot \rceil$ (podinterval $[s, t]$), a $\sum_{d=s}^{t} (\alpha d + \beta) = \alpha \cdot \frac{(s+t)(t-s+1)}{2} + \beta (t - s + 1)$ – zbroj aritmetičkog niza.</p>
'''),
        ('Koliko su veliki brojevi u međukoracima?',
         r'''
<p>Odsječci do $10^{12}$, nagibi do $3 \cdot 10^5$: pri usporedbi sjecišta množe se razlike odsječaka ($\le 10^{12}$) i razlike nagiba ($\le 3 \cdot 10^5$) – do $3 \cdot 10^{17}$, još u 64 bita, ali $\sum d$ na intervalu duljine $2 \cdot 10^{12}$ doseže $\sim 4 \cdot 10^{24}$. Zato međurezultate držimo u 128-bitnim brojevima (<code>__int128</code>) i tek zbroj reduciramo modulo $998244353$; negativne vrijednosti prije redukcije normaliziramo.</p>
'''),
        ('Kako se uvjeriti da nema pogreške u zaokruživanju granica?',
         r'''
<p>Ručna provjera na primjeru: $L = (5,5,2)$, $R = (7,6,7)$, $d \in [-2, 1]$; $u(d) - \ell(d) + 1$ redom za $d = -2, -1, 0, 1$ iznosi $1, 2, 2, 1$, zbroj $6$. U brute forceu za male testove jednostavno prođemo sve $(A_0, d)$; razlike se najčešće pojave upravo na granicama $\lceil \cdot \rceil$ negativnih brojeva – zato $\lfloor p/q \rfloor$ implementiramo eksplicitno, a ne operatorom <code>/</code>.</p>
'''),
    ],
    'tips': [
        r'''Brojanje objekata s malo parametara ($A_0$ i $d$) počinje fiksiranjem jednog parametra: uvjeti postaju interval za drugi, a broj rješenja zbroj duljina intervala.''',
        r'''$\max_i (a_i x + b_i)$ i $\min_i (a_i x + b_i)$ su izlomljene linije s $O(N)$ komada – <strong>Convex Hull Trick</strong>; ako su nagibi već sortirani (ovdje $-i$), ovojnica se gradi u $O(N)$ stogom.''',
        r'''Zbroj linearne funkcije po cjelobrojnom intervalu je zbroj aritmetičkog niza – $O(1)$; granicu iz uvjeta $\alpha d + \beta \ge 1$ računaj vlastitim $\lfloor \cdot \rfloor$/$\lceil \cdot \rceil$ jer C++ dijeljenje zaokružuje prema nuli.''',
        r'''Kad se množe vrijednosti $\sim 10^{12}$ s duljinama intervala $\sim 10^{12}$, prijeđi na <code>__int128</code> i reduciraj modulo tek na kraju – jednostavnije od gomile modularnih operacija i lakše za provjeru.''',
    ],
    'solution': r'''
<p>Radi jednostavnosti indeksiramo $L$, $R$ i $A$ od nule i označimo $X = \max_i R_i$.</p>
<p>Fiksirajmo razliku $d$. Dopušteni raspon početnog člana $A_0$ je</p>
<p>$$\max_i \{ -id + L_i \} \le A_0 \le \min_i \{ -id + R_i \}.$$</p>
<p>Za svaki $i$ je $-id + L_i$ linearna funkcija u $d$, pa je maksimum tih funkcija, $\max_i \{-id + L_i\}$, po dijelovima linearna krivulja konveksna prema dolje u varijabli $d$. Nju možemo izračunati u $O(N)$ tehnikom poput Convex Hull Tricka. Slično, uvjeti za $R$ tvore po dijelovima linearnu krivulju konkavnu prema gore.</p>
<p>Treba prebrojati cjelobrojne točke u područje omeđenom tim dvjema po dijelovima linearnim funkcijama. Podijelimo li raspon $d$ na $O(N)$ intervala na prikladan način, područje se rastavlja na trapeze, a broj cjelobrojnih točaka u svakom trapezu računamo u $O(1)$.</p>
<p>Vremenska složenost je $O(N)$.</p>
''',
    'detailed': r'''
<h3>1. Svođenje na dva parametra</h3>
<p>Indeksiramo od $0$ i pišemo $A_i = A_0 + i d$ ($A_0, d \in \mathbb{Z}$). Niz je dopušten ako i samo ako za svaki $i$ vrijedi $L_i - i d \le A_0 \le R_i - i d$, tj.</p>
<p>$$\ell(d) := \max_{i} (L_i - i d) \;\le\; A_0 \;\le\; u(d) := \min_{i} (R_i - i d).$$</p>
<p>Za fiksan $d$ broj dopuštenih $A_0$ je $\max(0, u(d) - \ell(d) + 1)$ (granice su cijele jer su $L_i, R_i, i, d$ cijeli). Ukupno: $\sum_{d \in \mathbb{Z}} \max(0, u(d) - \ell(d) + 1)$. Raspon $d$ s mogućim rješenjima ograničen je uvjetima za $i = 0$ i $i = 1$ (postoje jer $N \ge 2$): $d = A_1 - A_0 \in [L_1 - R_0, R_1 - L_0] =: [d_{\min}, d_{\max}]$; izvan njega je $u(d) < \ell(d)$. Raspon ima do $2 \cdot 10^{12}$ cijelih brojeva, pa ne možemo iterirati.</p>
<h3>2. Ovojnice pravaca</h3>
<p>$\ell(d)$ je maksimum pravaca $y = -i \cdot d + L_i$; maksimum linearnih funkcija je konveksna izlomljena linija. Uz različite nagibe svaki pravac čini najviše jedan komad ovojnice, a komadi su poredani po nagibu: za $d \to -\infty$ dominira najmanji nagib ($-(N-1)$), za $d \to +\infty$ najveći ($0$). Građenje stogom (trik konveksne ljuske): pravce obrađujemo po rastućem nagibu; pravac $l_2$ na vrhu stoga izbacujemo ako je sjecište $l_1$ (pod njim) i novog $l_3$ lijevo od ili u sjecištu $l_1$ i $l_2$, jer tada $l_2$ nigdje nije strogo najveći. Usporedbu sjecišta $\frac{b_1 - b_3}{a_3 - a_1} \le \frac{b_1 - b_2}{a_2 - a_1}$ izvodimo množenjem (nazivnici su pozitivni), bez razlomaka. Komad pravca $h_k$ završava na $\lceil x_k \rceil - 1$, gdje je $x_k$ sjecište $h_k$ i $h_{k+1}$; komad $h_{k+1}$ počinje na $\lceil x_k \rceil$ (u $x_k$, ako je cijeli, obje vrijednosti su jednake pa izbor ne mijenja $\ell$). Prazni komadi (cjelobrojno prazni) se preskaču.</p>
<p>$u(d) = \min_i (R_i - i d) = -\max_i (i d - R_i)$, pa donju ovojnicu dobivamo istom rutinom na pravcima $y = i \cdot d - R_i$ i negiramo. Svaka ovojnica ima najviše $N$ komada koji zajedno pokrivaju sve cijele $d$.</p>
<h3>3. Zbrajanje po komadima</h3>
<p>Prolazimo $d$ od $d_{\min}$ do $d_{\max}$ s dva pokazivača (po komad za $\ell$ i za $u$). Na intervalu $[cur, end]$, gdje je $end$ najmanji od krajeva oba aktivna komada i $d_{\max}$, oba su pravca fiksna: $\ell(d) = a_\ell d + b_\ell$, $u(d) = a_u d + b_u$, pa</p>
<p>$$c(d) = u(d) - \ell(d) + 1 = \alpha d + \beta, \qquad \alpha = a_u - a_\ell, \; \beta = b_u - b_\ell + 1.$$</p>
<p>Doprinos su $c(d)$ za one $d \in [cur, end]$ s $c(d) \ge 1$ (za $c(d) \le 0$ doprinos je $0$). Rješavamo $\alpha d \ge 1 - \beta$: za $\alpha = 0$ interval je cijeli ili prazan; za $\alpha > 0$ $d \ge \lceil (1 - \beta)/\alpha \rceil$; za $\alpha < 0$ $d \le \lfloor (\beta - 1)/(-\alpha) \rfloor$. Na dobivenom $[s, t]$ zbroj je</p>
<p>$$\sum_{d=s}^{t} (\alpha d + \beta) = \alpha \cdot \frac{(s + t)(t - s + 1)}{2} + \beta \,(t - s + 1).$$</p>
<p>Zatim $cur = end + 1$. Svaki korak petlje troši jedan kraj komada ili završava, pa ima $O(N)$ koraka.</p>
<h3>4. Složenost</h3>
<p>Ovojnice: $O(N)$ nakon sortiranja po nagibu (nagibi su $-i$, tj. već sortirani; implementacija ih radi sigurnosti sortira – $O(N \log N)$, zanemarivo). Spajanje komada: $O(N)$. Ukupno $O(N \log N)$ s vrlo malom konstantom, oko $0.06$ s za $N = 3 \cdot 10^5$.</p>
<h3>5. Veličine brojeva i zamke</h3>
<ul>
    <li>Sjecišta: umnožak razlike odsječaka ($\le 10^{12}$) i razlike nagiba ($\le 3 \cdot 10^5$) je $\le 3 \cdot 10^{17}$; stane u 64 bita, ali koristimo <code>__int128</code> radi jednostavnosti.</li>
    <li>Zbroj aritmetičkog niza: $t - s + 1 \le 2 \cdot 10^{12}$, $(s + t)(t - s + 1) \sim 10^{25}$ – obavezno <code>__int128</code>; tek zatim redukcija modulo $p$ uz normalizaciju negativnih ($((x \bmod p) + p) \bmod p$).</li>
    <li>$\lfloor p/q \rfloor$ za negativan $p$: C++ operator <code>/</code> zaokružuje prema nuli; implementiramo <code>floordiv</code> s korekcijom i $\lceil p/q \rceil = -\lfloor -p/q \rfloor$.</li>
    <li>Krajevi ovojnica u $\pm\infty$: koristimo sentinel $\pm 4 \cdot 10^{18}$; petlja ionako ide samo po $[d_{\min}, d_{\max}]$.</li>
    <li>$N = 2$: obje ovojnice imaju jedan lom, sve radi bez posebnog slučaja.</li>
</ul>
<h3>6. Primjer</h3>
<p>$L = (5, 5, 2)$, $R = (7, 6, 7)$: $d \in [5 - 7, 6 - 5] = [-2, 1]$. $\ell(d) = \max(5, 5 - d, 2 - 2d)$, $u(d) = \min(7, 6 - d, 7 - 2d)$:</p>
<ul>
    <li>$d = -2$: $\ell = 7$, $u = 7$, doprinos $1$ (niz $7, 5, 3$);</li>
    <li>$d = -1$: $\ell = 6$, $u = 7$, doprinos $2$;</li>
    <li>$d = 0$: $\ell = 5$, $u = 6$, doprinos $2$;</li>
    <li>$d = 1$: $\ell = 5$, $u = 5$, doprinos $1$ (niz $5, 6, 7$).</li>
</ul>
<p>Ukupno $6$. Ovojnica $\ell$ ima komade $2 - 2d$ (za $d \le -3$), $5 - d$ (za $-3 \le d \le 0$) i $5$ (za $d \ge 0$), a $u$ komade $7$ (za $d \le -1$), $6 - d$ (za $-1 \le d \le 1$) i $7 - 2d$ (za $d \ge 1$); algoritam njihove lomove unutar $[-2, 1]$ spaja u intervale $[-2, -1]$, $[0, 0]$, $[1, 1]$ i na svakom zbraja linearnu funkciju.</p>
''',
    'verified': r'''uzorci 2/2; 300 slučajnih malih testova ($2 \le N \le 6$, vrijednosti do $40$) protiv brute forcea koji prolazi sve parove $(A_0, d)$; 3 velika testa s $N = 3 \cdot 10^5$ i vrijednostima do $10^{12}$ (široki intervali s ogromnim odgovorom, uski intervali oko fiksnog niza, slučajni intervali), najsporiji $0.06$ s.''',
},
# ---------------------------------------------------------------- L
{
    'letter': 'L', 'title': 'Many Products', 'title_hr': 'Mnogo umnožaka', 'slug': 'L_many_products',
    'tl': '3 s', 'ml': '1024 MB',
    'statement': r'''
<p>Dani su $N$, $M$ i niz $A_1, \dots, A_N$. Neka je $X$ skup svih $N$-torki pozitivnih cijelih brojeva $(x_1, \dots, x_N)$ s $\prod_i x_i = M$. Izračunaj</p>
<p>$$\sum_{(x_1, \dots, x_N) \in X} \prod_{i=1}^{N} (x_i + A_i) \pmod{998244353}.$$</p>
<h3>Ulaz</h3>
<p>$N$, $M$ ($1 \le N \le 2 \cdot 10^5$, $1 \le M \le 10^{12}$) i $A_1, \dots, A_N$ ($0 \le A_i < 998244353$).</p>
<h3>Izlaz</h3>
<p>Tražena vrijednost.</p>
<h3>Primjer</h3>
<p>Za $N = 2$, $M = 3$, $A = (0, 1)$: $X = \{(1,3), (3,1)\}$ i odgovor je $(1+0)(3+1) + (3+0)(1+1) = 10$.</p>
''',
    'hints': [
        r'''<p>Raspiši $\prod (x_i + A_i)$ kao zbroj $2^N$ članova. Zbog simetrije po $X$ (permutacije $x$-eva čuvaju $X$), bitno je samo <em>koliko</em> se $x$-eva pojavljuje u članu, ne kojih.</p>''',
        r'''<p>Dakle odgovor je $\sum_k B_k \cdot S_k$, gdje su $B_k$ koeficijenti polinoma $\prod_i (x + A_i)$ (dijeli-pa-vladaj s NTT-om), a $S_k = \sum_{x_1 \cdots x_N = M} x_1 \cdots x_k$.</p>''',
        r'''<p>$S_k$ je multiplikativna funkcija od $M$: rastavi $M = \prod p_j^{e_j}$ i za svaki prosti faktor prebroji raspodjele eksponenata na $N$ mjesta — „štapići i kuglice” s težinom $p^{d}$ za eksponent $d$ raspoređen među prvih $k$ mjesta.</p>''',
    ],
    'coach': [
        ('Skup $X$ može biti ogroman – koja simetrija $X$-a nam dopušta da izraz „zaboravi” indekse?',
         r'''
<p>$X$ je invarijantan na permutacije koordinata: ako je $\prod x_i = M$, isto vrijedi za bilo koji preraspored. Raspišimo $\prod_i (x_i + A_i) = \sum_{S \subseteq [N]} \bigl(\prod_{i \in S} x_i\bigr)\bigl(\prod_{i \notin S} A_i\bigr)$ i zamijenimo redoslijed zbrajanja. Za fiksan $S$ je $\sum_{X} \prod_{i \in S} x_i$ jednak $\sum_X x_1 \cdots x_{|S|}$ (preimenovanjem koordinata) – ovisi samo o $k = |S|$. Označimo $S_k := \sum_{x_1 \cdots x_N = M} x_1 \cdots x_k$; tada je odgovor $\sum_k B_k S_k$, gdje $B_k = \sum_{|S| = k} \prod_{i \notin S} A_i = [x^k] \prod_i (x + A_i)$.</p>
'''),
        ('Kako izračunati sve koeficijente $B_k$ polinoma $\prod_{i=1}^{N} (x + A_i)$ za $N = 2 \cdot 10^5$?',
         r'''
<p>Naivno množenje jedan po jedan je $O(N^2)$. Umnožak $N$ linearnih polinoma računamo metodom „podijeli pa vladaj”: pomnoži lijevu i desnu polovicu rekurzivno, a rezultate spoji NTT-om. Na svakoj razini rekurzije ukupni stupanj je $N$, pa razina košta $O(N \log N)$; razina je $O(\log N)$ – ukupno $O(N \log^2 N)$.</p>
'''),
        ('Kako izračunati $S_k = \sum_{x_1 \cdots x_N = M} x_1 \cdots x_k$ za sve $k$, kad je $M$ do $10^{12}$?',
         r'''
<p>Funkcija $P \mapsto \sum_{x_1 \cdots x_N = P} x_1 \cdots x_k$ je <em>multiplikativna</em>: rastav $P = \prod_j p_j^{e_j}$ znači da se za svaki $i$ eksponent svakog prostog broja bira neovisno, a umnožak $x_1 \cdots x_k$ se faktorizira po prostim brojevima. Zato je $S_k = \prod_j S_k(p_j^{e_j})$, a za prostu potenciju treba raspodijeliti $e$ jedinica eksponenta na $N$ mjesta: ako $d$ jedinica padne na prvih $k$ mjesta, faktor je $p^d$, a raspodjela ima $\binom{d + k - 1}{k - 1}\binom{e - d + N - k - 1}{N - k - 1}$ (štapići i kuglice). Ukupno $O(N \sum_j e_j) = O(N \log M)$.</p>
'''),
        ('Što se događa na rubovima $k = 0$ i $k = N$ i u malim slučajevima?',
         r'''
<p>Za $k = 0$ nema „prvih $k$ mjesta”, pa je jedino $d = 0$ moguće i $S_0 = \binom{e + N - 1}{N - 1}$ – broj rastava $p^e$ na $N$ faktora; za $k = N$ jedino $d = e$: $S_N = p^e \binom{e + N - 1}{N - 1}$. U općoj formuli to odgovara konvenciji $\binom{-1}{-1} = 1$, koju je sigurnije zapisati posebnim slučajem. $N = 1$: $X = \{(M)\}$, odgovor $M + A_1$ – formula daje $B_0 S_0 + B_1 S_1 = A_1 \cdot 1 + 1 \cdot M$. $M = 1$: svi $x_i = 1$, odgovor $\prod (1 + A_i)$.</p>
'''),
    ],
    'tips': [
        r'''Zbroj po simetričnom skupu $N$-torki: raspiši umnožak, zamijeni redoslijed zbrajanja i iskoristi da zbroj ovisi samo o <strong>broju</strong> odabranih koordinata – tada se svi $A_i$ sažimaju u koeficijente polinoma $\prod (x + A_i)$.''',
        r'''Umnožak mnogo malih polinoma računaj <strong>dijeli-pa-vladaj s NTT-om</strong> u $O(N \log^2 N)$; za male podprobleme prijeđi na naivno množenje (brže zbog konstante).''',
        r'''Zbrojevi po rastavima $M = x_1 \cdots x_N$ s multiplikativnom težinom su multiplikativni u $M$ – računaj ih po prostim potencijama i množi; eksponenti su mali ($\sum e_j \le 40$ za $M \le 10^{12}$).''',
        r'''Raspodjela $e$ jednakih jedinica na $m$ mjesta (s ponavljanjem) ima $\binom{e + m - 1}{m - 1}$ načina – <strong>štapići i kuglice</strong>; tablice faktorijela dimenzioniraj do $N + \max e_j$.''',
    ],
    'solution': r'''
<p>Radi kratkoće pišemo $\sum_{x_1 \cdots x_N = M}$ umjesto $\sum_{(x_1, \dots, x_N) \in X}$.</p>
<p>Raspišemo li $\prod_{i=1}^{N} (x_i + A_i)$ kao zbroj $2^N$ članova $T_1, \dots, T_{2^N}$, imamo</p>
<p>$$\sum_{x_1 \cdots x_N = M} \sum_{s} T_s = \sum_{s} \sum_{x_1 \cdots x_N = M} T_s.$$</p>
<p>Zato nije bitno koji se od $x_1, \dots, x_N$ pojavljuju u $T_s$, nego samo koliko ih se pojavljuje. Zanemarimo li indekse, možemo pisati $\prod_{i=1}^{N} (x + A_i) = B_0 + B_1 x + \dots + B_N x^N$, a odgovor je</p>
<p>$$\sum_{k=0}^{N} B_k \Bigl( \sum_{x_1 \cdots x_N = M} x_1 x_2 \cdots x_k \Bigr).$$</p>
<p>Izraz $\sum_{x_1 \cdots x_N = P} x_1 \cdots x_k$ je multiplikativan u $P$. Rastavimo li $M = p_1^{e_1} \cdots p_c^{e_c}$, vrijedi</p>
<p>$$\sum_{x_1 \cdots x_N = M} x_1 \cdots x_k = \prod_{j=1}^{c} \Bigl( \sum_{x_1 \cdots x_N = p_j^{e_j}} x_1 \cdots x_k \Bigr),$$</p>
<p>a zbroj za prostu potenciju ima jednostavan oblik s binomnim koeficijentima:</p>
<p>$$\sum_{x_1 \cdots x_N = p^{e}} x_1 \cdots x_k = \begin{cases} \binom{e+N-1}{N-1} & (k = 0) \\[4pt] \displaystyle\sum_{d=0}^{e} p^{d} \binom{d+k-1}{k-1} \binom{e-d+N-k-1}{N-k-1} & (0 < k < N) \\[4pt] p^{e} \binom{e+N-1}{N-1} & (k = N). \end{cases}$$</p>
<p>Koeficijente $B_0, \dots, B_N$ računamo konvolucijom (dijeli-pa-vladaj s NTT-om) u $O(N \log^2 N)$. Faktorizacija $M$ traje $O(\sqrt{M})$, a ostatak računanja $O(N \log M)$.</p>
''',
    'detailed': r'''
<h3>1. Simetrija i polinom $\prod (x + A_i)$</h3>
<p>Za svaku $N$-torku $(x_1, \dots, x_N) \in X$ vrijedi $\prod_{i=1}^{N} (x_i + A_i) = \sum_{S \subseteq [N]} \Bigl(\prod_{i \in S} x_i\Bigr) \Bigl(\prod_{i \notin S} A_i\Bigr)$ (distributivnost: iz svake zagrade biramo $x_i$ ili $A_i$; $S$ je skup zagrada iz kojih smo uzeli $x_i$). Zamjenom redoslijeda zbrajanja</p>
<p>$$\text{odgovor} = \sum_{S \subseteq [N]} \Bigl(\prod_{i \notin S} A_i\Bigr) \sum_{x \in X} \prod_{i \in S} x_i.$$</p>
<p>Skup $X$ je zatvoren na permutacije koordinata (uvjet $\prod x_i = M$ je simetričan), pa preimenovanje koordinata bijektivno preslikava $X$ na sebe i $\sum_{x \in X} \prod_{i \in S} x_i = \sum_{x \in X} x_1 x_2 \cdots x_{|S|} =: S_{|S|}$. Grupiranjem po $k = |S|$:</p>
<p>$$\text{odgovor} = \sum_{k=0}^{N} B_k \, S_k, \qquad B_k = \sum_{|S| = k} \prod_{i \notin S} A_i = [x^k] \prod_{i=1}^{N} (x + A_i).$$</p>
<p>Zadnja jednakost je ista distributivnost primijenjena na polinom u jednoj varijabli $x$: član $x^k$ nastaje odabirom $x$ iz točno $k$ zagrada.</p>
<h3>2. Koeficijenti $B_k$: dijeli-pa-vladaj s NTT-om</h3>
<p>Funkcija <code>prodRange(l, r)</code> vraća $\prod_{i \in [l, r)} (x + A_i)$: za jedan faktor $\{A_l, 1\}$, inače pomnoži rezultate polovica. Množenje polinoma stupnjeva $a, b$ NTT-om košta $O((a + b) \log(a + b))$; za male stupnjeve ($\le 32$) naivno množenje je brže. Na dubini $j$ rekurzije ima $2^j$ podproblema ukupnog stupnja $N$, pa razina košta $O(N \log N)$ i sveukupno $O(N \log^2 N)$ – za $N = 2 \cdot 10^5$ oko $0.2$ s. Alternativa je heap malih polinoma po stupnju (isti red složenosti). Sve modulo $998244353$, koji je NTT-prijateljski ($2^{23} \mid p - 1$).</p>
<h3>3. Multiplikativnost $S_k$</h3>
<p>Neka je $f_k(P) = \sum_{x_1 \cdots x_N = P} x_1 \cdots x_k$. Tvrdnja: $f_k(PQ) = f_k(P) f_k(Q)$ za $\gcd(P, Q) = 1$. Dokaz: svaki rastav $x_1 \cdots x_N = PQ$ jednoznačno se rastavlja na $x_i = y_i z_i$ s $y_i = \gcd(x_i, P)$, $\prod y_i = P$, $\prod z_i = Q$ (jer su $P, Q$ relativno prosti, prosti faktori svakog $x_i$ dijele se na one iz $P$ i one iz $Q$), i obrnuto svaki par rastava daje rastav $PQ$. Težina se množi: $x_1 \cdots x_k = (y_1 \cdots y_k)(z_1 \cdots z_k)$. Zbroj po parovima je umnožak zbrojeva. Zato za $M = \prod_j p_j^{e_j}$ vrijedi $S_k = \prod_j f_k(p_j^{e_j})$.</p>
<h3>4. Formula za prostu potenciju</h3>
<p>Rastav $p^e = x_1 \cdots x_N$ znači $x_i = p^{a_i}$ s $a_i \ge 0$, $\sum a_i = e$. Težina je $x_1 \cdots x_k = p^{a_1 + \dots + a_k} = p^d$, $d := \sum_{i \le k} a_i$. Za fiksan $d$: broj načina da se $d$ raspodijeli na $k$ nenegativnih dijelova je $\binom{d + k - 1}{k - 1}$ (štapići i kuglice: $d$ kuglica i $k - 1$ pregrada), a $e - d$ na preostalih $N - k$ dijelova $\binom{e - d + N - k - 1}{N - k - 1}$. Dakle</p>
<p>$$f_k(p^e) = \sum_{d=0}^{e} p^{d} \binom{d + k - 1}{k - 1} \binom{e - d + N - k - 1}{N - k - 1},$$</p>
<p>uz rubne slučajeve: za $k = 0$ jedino $d = 0$ ($f_0(p^e) = \binom{e + N - 1}{N - 1}$), za $k = N$ jedino $d = e$ ($f_N(p^e) = p^e \binom{e + N - 1}{N - 1}$); u kodu su to eksplicitne grane jer bi $\binom{-1}{-1}$ inače bilo $0$. Faktorijeli trebaju ići do $N + \max_j e_j$; $\max e_j \le 39$ za $M \le 10^{12}$. Potenciju $p^d$ računamo modulo $p_{\text{mod}}$ – $p$ može biti do $10^{12}$, pa ga prvo reduciramo.</p>
<h3>5. Faktorizacija i ukupna složenost</h3>
<p>Probno dijeljenje do $\sqrt{M} = 10^6$: $O(\sqrt{M})$, oko $10^6$ dijeljenja. Preostali kofaktor $> 1$ je prost. Zatim za svaki $k \in [0, N]$ i svaki prosti faktor petlja po $d \le e_j$: $O(N \sum_j e_j) \le O(N \log_2 M) \approx 8 \cdot 10^6$ operacija. Ukupno $O(N \log^2 N + \sqrt{M} + N \log M)$, u praksi ispod $0.3$ s uz limit $3$ s.</p>
<h3>6. Primjer</h3>
<p>$N = 2$, $M = 3$, $A = (0, 1)$: $\prod (x + A_i) = x(x + 1) = x + x^2$, pa $B = (0, 1, 1)$. $M = 3^1$: $f_0 = \binom{2}{1} = 2$, $f_1 = \sum_{d=0}^{1} 3^d \binom{d}{0}\binom{1 - d}{0} = 1 + 3 = 4$, $f_2 = 3 \cdot \binom{2}{1} = 6$. Odgovor $0 \cdot 2 + 1 \cdot 4 + 1 \cdot 6 = 10$, kao u zadatku ($X = \{(1,3), (3,1)\}$: $1 \cdot 4 + 3 \cdot 2 = 10$).</p>
<h3>7. Rubni slučajevi</h3>
<ul>
    <li>$M = 1$: nema prostih faktora, $S_k = 1$ za sve $k$, odgovor $\sum_k B_k = \prod (1 + A_i)$ – ispravno, jer je jedini rastav $(1, \dots, 1)$.</li>
    <li>$M$ prost blizu $10^{12}$: petlja do $10^6$ ne nalazi djelitelj, ostatak je $M$ sam.</li>
    <li>$A_i = 0$: polinom ima faktor $x$; NTT s nulama radi bez posebnih slučajeva.</li>
    <li>$N = 1$: rekurzija vraća $\{A_1, 1\}$, odgovor $A_1 + M \bmod p$.</li>
</ul>
''',
    'verified': r'''uzorci 3/3; 300 slučajnih malih testova ($N \le 5$, $M \le 100$ ili mala potencija dvojke, $A_i$ mali ili blizu modula) protiv brute forcea koji rekurzivno nabraja sve rastave $M$ na $N$ faktora; 3 velika testa s $N = 2 \cdot 10^5$ i $M$ slučajno iz $\{963761198400 \text{ (visoko složen)}, 10^{12}, 999999999989 \text{ (prost)}, 2^{39}\}$, najsporiji $0.26$ s.''',
},
# ---------------------------------------------------------------- M
{
    'letter': 'M', 'title': 'Colorful Graph', 'title_hr': 'Šareni graf', 'slug': 'M_colorful_graph',
    'tl': '8 s', 'ml': '64 MB',
    'statement': r'''
<p>Dan je usmjereni graf s $N$ vrhova i $M$ bridova. Oboji vrhove bojama $1..N$ tako da za svaka dva vrha iste boje postoji put od jednog do drugog (u barem jednom smjeru), a najveća korištena boja bude najmanja moguća. Ispiši jedno takvo bojanje.</p>
<h3>Ulaz</h3>
<p>$N$, $M$ ($1 \le N \le 7 \cdot 10^3$, $0 \le M \le 7 \cdot 10^3$) i $M$ bridova $A_i \to B_i$ (bez petlji i višestrukih bridova).</p>
<h3>Izlaz</h3>
<p>Boje $c_1, \dots, c_N$. <em>Memorijsko ograničenje je 64 MB.</em></p>
''',
    'hints': [
        r'''<p>Vrhovi iste jako povezane komponente mogu dijeliti boju. Kondenziraj SCC-ove u DAG; sada „ista boja” znači da su vrhovi na zajedničkom putu, tj. u lancu. Traži se <em>minimalno pokrivanje lancima</em> (putevi koji smiju preskakati — tranzitivni zatvarač).</p>''',
        r'''<p>Pokrivanje DAG-a putevima = $N - $ (najveće sparivanje u bipartitnom grafu $U_i \to V_j$ za brid $i \to j$). Za lance treba tranzitivni zatvarač, koji ima $\Theta(N^2)$ bridova — memorija! Umjesto toga dodaj bridove $U_i \to V_i$ kapaciteta $\infty$ u mreži toka: put može „proći kroz” već pokriveni vrh.</p>''',
        r'''<p>Mreža: $src \to V_i$ (kap. $1$), $U_i \to dst$ (kap. $1$), $V_{A_j} \to U_{B_j}$ ($\infty$), $U_i \to V_i$ ($\infty$). Najviše $3N + M$ bridova, tok $\le N$, Ford–Fulkerson u $O(N(N+M))$.</p>''',
    ],
    'coach': [
        ('Koji vrhovi „sigurno” smiju dijeliti boju, i što ostaje nakon što ih sažmemo?',
         r'''
<p>Vrhovi iste jako povezane komponente (SCC) međusobno su dostižni u oba smjera, pa su pairwise usporedivi sa svima s kojima je usporediv bilo koji od njih – dostižnost ovisi samo o SCC-u. Sažimanjem SCC-ova nastaje DAG kondenzacije s $K$ vrhova; uvjet „dva vrha iste boje su usporediva” postaje uvjet na SCC-ovima. Optimum se ne mijenja: iz bojanja izvornog grafa s $c$ boja dobijemo bojanje kondenzacije s $\le c$ boja (svaki SCC preuzme boju jednog svog predstavnika – predstavnici iste boje pairwise su usporedivi), a bojanje kondenzacije prenosimo natrag bez promjene broja boja.</p>
'''),
        ('Kako izgleda skup vrhova iste boje u DAG-u?',
         r'''
<p>Dostižnost u DAG-u je parcijalni uređaj; skup pairwise usporedivih vrhova je <em>lanac</em>, tj. totalno uređen: $v_1 \prec v_2 \prec \dots \prec v_t$, gdje svaki dostiže sljedeći. To je put u <strong>tranzitivnom zatvaraču</strong>. Minimalan broj boja = minimalan broj lanaca koji pokrivaju sve vrhove = minimalno pokrivanje putevima u tranzitivnom zatvaraču (po Dilworthu jednak najvećem antilancu, ali nama treba konstrukcija, ne samo broj).</p>
'''),
        ('Minimalno pokrivanje DAG-a vrhovno-disjunktnim putevima je klasika – zašto je ovdje ne možemo primijeniti izravno?',
         r'''
<p>Klasika: broj puteva $= K - \nu$, gdje je $\nu$ najveće sparivanje u bipartitnom grafu s bridom $V_i U_j$ za svaki brid $i \to j$. Ali treba nam pokrivanje u <em>zatvaraču</em>, koji ima do $\Theta(K^2) \approx 2.5 \cdot 10^7$ bridova – s $64$ MB memorije ne stane (a i računanje zatvarača bitsetima je na granici). Želimo sparivanje u zatvaraču bez da ga eksplicitno izgradimo.</p>
'''),
        ('Kako tok može „simulirati” bridove zatvarača koristeći samo izvorne bridove?',
         r'''
<p>Put $i \to a \to b \to \dots \to k$ u DAG-u odgovara bridu $i \to k$ zatvarača. U mreži sparivanja stavimo za svaki izvorni brid $a \to b$ brid $V_a \to U_b$ kapaciteta $\infty$, a za svaki vrh $b$ brid $U_b \to V_b$ kapaciteta $\infty$ („prolaz kroz $b$”). Tada je svaki put $src \to V_i \to U_a \to V_a \to \dots \to U_k \to dst$ u mreži točno jedan put $i \leadsto k$ u DAG-u, a kapaciteti $1$ na $src \to V_i$ i $U_k \to dst$ osiguravaju da svaki vrh ima najviše jednog sljedbenika i najviše jednog prethodnika – tok jedinica od $\nu$ je sparivanje u zatvaraču. Mreža ima $2K + 2$ vrhova i $3K + M$ bridova.</p>
'''),
        ('Kako iz toka dobiti same lance, i zašto to stane u vrijeme i memoriju?',
         r'''
<p>Dekompozicija toka: za svaki $V_i$ s tokom iz $src$ pratimo jedinicu toka bridovima s pozitivnim tokom (skidajući je) do $U_k \to dst$; par $(i, k)$ kaže „$k$ slijedi $i$ u lancu”. Svaki vrh ima $\le 1$ sljedbenika i $\le 1$ prethodnika, a DAG isključuje cikluse, pa parovi tvore $K - \nu$ lanaca; svaki lanac dobije jednu boju. Ford–Fulkerson: $\le K$ augmentacija po $O(K + M)$, ukupno $O(K(K + M)) \le 10^8$; memorija $O(K + M)$ – nekoliko stotina KB.</p>
'''),
    ],
    'tips': [
        r'''Uvjete na „međusobnu dostižnost” prvo svedi na <strong>kondenzaciju SCC-ova</strong>: unutar SCC-a sve je dostižno, a preostali problem živi na DAG-u, gdje je dostižnost parcijalni uređaj.''',
        r'''Skup pairwise usporedivih elemenata parcijalnog uređaja je lanac; <strong>minimalno pokrivanje lancima</strong> = pokrivanje putevima u tranzitivnom zatvaraču = $K - $ najveće sparivanje (Dilworth/König).''',
        r'''Kad je zatvarač prevelik, zamijeni ga u mreži toka bridovima „prolaz kroz vrh” ($U_i \to V_i$, kapacitet $\infty$): tok tada smije proći kroz vrh koji drugi put već koristi, što točno modelira bridove zatvarača.''',
        r'''Uz mali memorijski limit izbjegavaj $O(K^2)$ matrice i duboku rekurziju (iterativni Tarjan); Ford–Fulkerson s DFS-om dovoljan je kad je vrijednost toka mala ($\le K$).''',
    ],
    'solution': r'''
<p>Vrhove iste jako povezane komponente možemo obojiti istom bojom. Kondenziramo komponente u po jedan vrh i dobivamo DAG.</p>
<p>Ako postoje bridovi $i \to j$ i $j \to k$, dodamo i brid $i \to k$; time se zadatak svodi na <a href="https://en.wikipedia.org/wiki/Maximum_flow_problem#Minimum_path_cover_in_directed_acyclic_graph">minimalno pokrivanje DAG-a putevima</a>, rješivo najvećim tokom. Međutim, broj bridova tada može doseći $\Theta(N^2)$, što ne stane u memoriju.</p>
<p>Broj bridova smanjujemo ovako. Pripremimo vrhove $src$, $dst$, $U_1, \dots, U_N$, $V_1, \dots, V_N$ i bridove:</p>
<ul>
    <li>iz $src$ u svaki $V_i$ kapaciteta $1$;</li>
    <li>iz svakog $U_i$ u $dst$ kapaciteta $1$;</li>
    <li>za svaki brid $j = 1, \dots, M$ iz $V_{A_j}$ u $U_{B_j}$ kapaciteta $\infty$;</li>
    <li>za svaki $i$ iz $U_i$ u $V_i$ kapaciteta $\infty$.</li>
</ul>
<p>Najveći tok ove mreže je najviše $N$, a bridova je najviše $3N + M$, pa je Ford–Fulkersonov algoritam složenosti $O(N(N + M))$ vremena i $O(N + M)$ memorije. Nakon što nađemo najveći tok, bojanje rekonstruiramo gledajući tok po bridovima, u $O(N^2)$ vremena i $O(N)$ memorije. Na kraju bojanje kondenziranog grafa prenesemo natrag na izvorni graf.</p>
<p>Ukupna vremenska složenost je $O(N(N + M))$, a memorijska $O(N + M)$.</p>
''',
    'detailed': r'''
<h3>1. Sažimanje jako povezanih komponenata</h3>
<p>Definirajmo relaciju $u \sim v$: „postoji put $u \to v$ ili $v \to u$”. Bojanje je valjano ako su vrhovi iste boje pairwise u relaciji $\sim$. Dostižnost $u \to v$ ovisi samo o SCC-ovima $[u], [v]$ (unutar SCC-a sve je međusobno dostižno), pa isto vrijedi za $\sim$.</p>
<p><strong>Tvrdnja:</strong> minimalan broj boja za izvorni graf jednak je minimalnom broju boja za DAG kondenzacije (uz istu relaciju). <em>Dokaz.</em> ($\le$) Iz valjanog bojanja kondenzacije obojimo sve vrhove SCC-a bojom njegovog čvora; dva vrha iste boje su ili u istom SCC-u (dostižni u oba smjera) ili u različitim SCC-ovima iste boje, koji su usporedivi. ($\ge$) Iz valjanog bojanja izvornog grafa s $c$ boja odaberimo u svakom SCC-u proizvoljan predstavnik i dodijelimo SCC-u njegovu boju; SCC-ovi iste boje imaju predstavnike iste boje, pairwise u relaciji $\sim$, pa su i SCC-ovi usporedivi. $\square$</p>
<p>SCC-ove računamo Tarjanovim algoritmom, iterativno (eksplicitan stog okvira), jer ulaz može biti lanac dubine $7000$; rekurzija bi vjerojatno prošla, ali uz $64$ MB radije ne riskiramo. Dobivamo $K \le N$ čvorova i $\le M$ bridova između različitih SCC-ova (bridove unutar SCC-a odbacujemo).</p>
<h3>2. Boje su lanci; minimalno pokrivanje lancima</h3>
<p>U DAG-u je dostižnost $\preceq$ parcijalni uređaj (refleksivan, tranzitivan, antisimetričan jer nema ciklusa). Skup $S$ pairwise usporedivih čvorova je lanac: totalno uređen, $v_1 \prec v_2 \prec \dots \prec v_t$, tj. put $v_1 \to v_2 \to \dots \to v_t$ u <em>tranzitivnom zatvaraču</em> $G^+$ (brid $u \to w$ za svaki par $u \prec w$). Obrnuto, svaki put u $G^+$ je lanac. Dakle:</p>
<p>$$\text{min. broj boja} = \text{min. broj vrhovno disjunktnih puteva u } G^+ \text{ koji pokrivaju sve čvorove}.$$</p>
<p>(Disjunktnost smijemo zahtijevati: ako se dva lanca preklapaju, izbacimo zajedničke čvorove iz jednog – ostaje lanac.) Klasičan rezultat: minimalno pokrivanje DAG-a $H$ vrhovno disjunktnim putevima ima $|V(H)| - \nu(H)$ puteva, gdje je $\nu(H)$ najveće sparivanje u bipartitnom grafu $B(H)$ s lijevim kopijama $V_i$, desnim kopijama $U_j$ i bridom $V_i U_j$ za svaki brid $i \to j$ u $H$. <em>Zašto:</em> u pokrivanju putevima svaki čvor ima najviše jednog sljedbenika i najviše jednog prethodnika – to je točno sparivanje (brid $V_i U_j$ za „$j$ slijedi $i$”); broj puteva je broj čvorova bez sljedbenika, tj. $|V| - (\text{broj sparenih bridova})$. Bez ciklusa (DAG) svako sparivanje daje valjanu dekompoziciju na puteve. Maksimalno sparivanje minimizira broj puteva.</p>
<h3>3. Problem: zatvarač je prevelik</h3>
<p>$G^+$ može imati $\Theta(K^2)$ bridova, za $K = 7000$ do $2.5 \cdot 10^7$ – u mreži toka s povratnim bridovima to je stotine MB, daleko iznad $64$ MB. (Bitset-zatvarač bi stao u $\approx 6$ MB, ali onda sparivanje Hopcroft–Karpom nad $10^7$ bridova opet treba eksplicitne liste ili spor prolaz bitsetima; službeno rješenje ide drugim putem.)</p>
<h3>4. Mreža koja simulira zatvarač</h3>
<p>Vrhovi: $src$, $dst$, $V_1..V_K$, $U_1..U_K$. Bridovi:</p>
<ul>
    <li>$src \to V_i$, kapacitet $1$ (čvor $i$ ima najviše jednog sljedbenika);</li>
    <li>$U_i \to dst$, kapacitet $1$ (čvor $i$ ima najviše jednog prethodnika);</li>
    <li>$V_a \to U_b$, kapacitet $\infty$, za svaki brid $a \to b$ kondenzacije;</li>
    <li>$U_b \to V_b$, kapacitet $\infty$ – „prolaz kroz $b$”.</li>
</ul>
<p><strong>Tvrdnja:</strong> najveći tok jednak je $\nu(G^+)$. ($\ge$) Za sparivanje $\{(i_r, k_r)\}$ u $B(G^+)$ uzmimo za svaki par put $i_r = a_0 \to a_1 \to \dots \to a_t = k_r$ u DAG-u i pošaljimo jedinicu toka $src \to V_{a_0} \to U_{a_1} \to V_{a_1} \to U_{a_2} \to \dots \to U_{a_t} \to dst$. Bridovi kapaciteta $1$ koriste se po jednom jer su $i_r$ različiti i $k_r$ različiti; unutarnji bridovi imaju kapacitet $\infty$. ($\le$) Cjelobrojni tok vrijednosti $\nu$ dekomponiramo na $\nu$ puteva $src \to dst$; svaki oblika $src \to V_{a_0} \to U_{a_1} \to V_{a_1} \to \dots \to U_{a_t} \to dst$ (jedini bridovi iz $V$ idu u $U$, a iz $U$ u $V$ istog indeksa ili u $dst$), što je put $a_0 \leadsto a_t$ u DAG-u, dakle brid $a_0 \to a_t$ zatvarača (i $a_0 \ne a_t$, jer bi inače postojao ciklus). Zbog kapaciteta $1$ su početci međusobno različiti i krajevi međusobno različiti – dobili smo sparivanje veličine $\nu$. $\square$</p>
<p>Mreža ima $2K + 2$ vrhova i $3K + M'$ bridova ($M' \le M$), s povratnim bridovima najviše $2(3 \cdot 7000 + 7000) = 56\,000$ zapisa – nekoliko stotina KB.</p>
<h3>5. Najveći tok i rekonstrukcija lanaca</h3>
<p>Vrijednost toka je $\le K$, pa Ford–Fulkerson s DFS-om (svaka augmentacija $O(V + E)$) radi u $O(K \cdot (K + M)) \approx 7000 \cdot 3.5 \cdot 10^4 \approx 2.5 \cdot 10^8$ u najgorem slučaju, u praksi puno manje; limit je $8$ s. Umjesto brisanja oznaka posjećenosti koristimo vremenski pečat.</p>
<p>Dekompozicija: za svaki $i$ čiji brid $src \to V_i$ nosi tok krenemo iz $V_i$ i idemo bridom s pozitivnim tokom (izvorni brid čija povratna kopija ima pozitivan kapacitet), skidajući jedinicu toka, dok ne stignemo u $dst$; zadnji posjećeni $U_k$ daje $\text{nxt}[i] = k$. Skidanje toka jamči da će sljedeće praćenje koristiti druge jedinice, a pokazivač po listi susjedstva svakog vrha čini ukupno praćenje $O(V + E + \sum \text{duljina})$. Rezultat: svaki čvor ima $\le 1$ sljedbenika i $\le 1$ prethodnika, nema ciklusa, pa parovi $(i, \text{nxt}[i])$ tvore $K - \nu$ lanaca. Krenemo od čvorova bez prethodnika i svakom lancu dodijelimo novu boju; boje SCC-ova zatim prenesemo na izvorne vrhove.</p>
<h3>6. Složenost i memorija</h3>
<p>Tarjan $O(N + M)$; tok $O(K(K + M))$; rekonstrukcija $O(K + M + \sum \text{duljina puteva}) = O(K^2)$ u najgorem slučaju; ukupno $O(N(N + M))$ vremena i $O(N + M)$ memorije. Na najvećim testovima (slučajni graf, lanac dubine $7000$ s bridovima unaprijed, veliki ciklus s granama) program troši $< 0.1$ s i nekoliko MB.</p>
<h3>7. Primjer</h3>
<p>Prvi primjer: bridovi $1 \to 4$, $2 \to 3$, $1 \to 3$, $2 \to 5$, $5 \to 1$ – graf je već DAG. Zatvarač sadrži npr. $2 \to 1$, $2 \to 4$, $5 \to 3$. Najveće sparivanje ima $3$ brida (npr. $2 \to 5$, $5 \to 1$, $1 \to 3$), pa je minimalno $5 - 3 = 2$ lanca: $\{2, 5, 1, 3\}$ i $\{4\}$ – ili, kao u službenom izlazu, $\{2, 3\}$ i $\{1, 4, 5\}$ ($5 \to 1 \to 4$). Svako bojanje s dvije boje u kojem su klase lanci je prihvatljivo; provjerivač to i provjerava.</p>
<h3>8. Zamke</h3>
<ul>
    <li>Ne zaboraviti odbaciti bridove unutar SCC-a (inače bi $V_a \to U_a$ dopustio „put” $a \leadsto a$ i lažno sparivanje).</li>
    <li>Kapacitete $\infty$ predstaviti kao veliki <code>int</code> ($10^9$) – tok je $\le K$, pa nema prelijevanja.</li>
    <li>$M = 0$: $K = N$, tok $0$, svaki vrh svoja boja – ispis $1, 2, \dots, N$.</li>
    <li>$N = 1$: jedna boja.</li>
</ul>
''',
    'verified': r'''uzorci 3/3 (preko provjerivača, jer optimalno bojanje nije jedinstveno); 300 slučajnih malih testova ($N \le 8$, $M \le 12$) protiv brute forcea koji iscrpnim pretraživanjem nalazi minimalan broj boja, uz provjerivač koji za izlaz provjerava valjanost (iste boje $\Rightarrow$ dostižnost) i jednak broj boja; 3 velika testa s $N = M = 7000$ (slučajni graf, lanac dubine $7000$ s bridovima unaprijed, ciklus od $3000$ vrhova s granama), najsporiji $0.09$ s, čiju je valjanost (svaka klasa boje je lanac u kondenzaciji) potvrdila zasebna skripta s bitset-dostižnošću.''',
},
# ---------------------------------------------------------------- N
{
    'letter': 'N', 'title': 'XOR Reachable', 'title_hr': 'XOR dostižnost', 'slug': 'N_xor_reachable',
    'tl': '3 s', 'ml': '1024 MB',
    'statement': r'''
<p>Dan je neusmjereni graf s $N$ vrhova i $M$ bridova; brid $i$ spaja $A_i$ i $B_i$ i ima težinu $C_i$. Dan je i $K$. Za svaki od $Q$ upita $D_i$ odredi broj parova $u < v$ takvih da se od $u$ do $v$ može doći koristeći samo bridove $j$ s $(C_j \oplus D_i) < K$.</p>
<h3>Ulaz</h3>
<p>$N, M, K$ ($2 \le N \le 10^5$, $1 \le M \le 10^5$, $0 \le K < 2^{30}$), $M$ bridova ($0 \le C_i < 2^{30}$), $Q$ ($1 \le Q \le 10^5$) i upiti $D_i$ ($0 \le D_i < 2^{30}$).</p>
<h3>Izlaz</h3>
<p>$Q$ redaka s odgovorima.</p>
''',
    'hints': [
        r'''<p>Za fiksni brid s težinom $C$, skup vrijednosti $D$ za koje je $C \oplus D < K$ je unija najviše $30$ intervala (po bitovima $K$: za svaki bit gdje $K$ ima $1$, jedan poddrvo-interval binarnog trie-a).</p>''',
        r'''<p>Sortiraj upite po $D$ i tretiraj to kao vremensku os: svaki brid je aktivan u $\le 30$ vremenskih intervala. To je <em>offline dinamička povezanost</em>: dijeli-pa-vladaj po vremenu + DSU s poništavanjem (rollback).</p>''',
        r'''<p>Odgovor upita je $\sum$ po komponentama $\binom{sz}{2}$; održavaj ga inkrementalno pri spajanju i vraćaj pri rollbacku.</p>''',
    ],
    'coach': [
        ('Za koji skup vrijednosti $D$ je jedan brid s težinom $C$ aktivan, tj. $C \oplus D < K$?',
         r'''
<p>Usporedba brojeva ide od najvišeg bita: $C \oplus D < K$ točno ako na prvom bitu $b$ gdje se $C \oplus D$ i $K$ razlikuju vrijedi $K_b = 1$ i $(C \oplus D)_b = 0$, a iznad $b$ se podudaraju. Neka je $P = C \oplus K$. „$C \oplus D$ se podudara s $K$ iznad $b$” isto je što i „$D$ se podudara s $P$ iznad $b$”, a $(C \oplus D)_b = 0$ znači $D_b = C_b = 1 - P_b$ (jer $K_b = 1$). Dakle za svaki bit $b$ s $K_b = 1$ dobivamo skup $D$-ova: prefiks iznad $b$ jednak prefiksu $P$, bit $b$ suprotan od $P_b$, niži bitovi proizvoljni – jedan interval duljine $2^b$, tj. jedno podstablo binarnog trie-a nad $D$. Skupovi za različite $b$ su disjunktni (razlikuje ih prvi bit neslaganja), a ima ih najviše $30$.</p>
'''),
        ('Ako brid „živi” u $\le 30$ podstabala trie-a, kako obraditi sve upite $D$ odjednom?',
         r'''
<p>Sortiramo upite po $D$ i spuštamo se rekurzivno po trie-u bitova $D$ (od bita $29$ do $0$), noseći: raspon upita čiji $D$ ima trenutni prefiks i popis bridova čiji $P$ ima isti prefiks (samo oni još mogu postati aktivni dublje – brid čiji se $P$ već razišao od $D$ ili je već aktiviran ili nikad neće biti). U čvoru na bitu $b$ s $K_b = 1$: bridovi s $P_b = 1$ aktivni su u <em>cijelom</em> podstablu djeteta $0$ (tamo je $D_b = 0 = 1 - P_b$), pa ih spojimo u DSU prije silaska u to dijete, a bridovi s $P_b = 0$ analogno prije silaska u dijete $1$. Bridovi s $P_b = D_b$ idu dalje u odgovarajuće dijete. Ako je $K_b = 0$, samo dijelimo. U listu je $D$ potpuno određen, DSU sadrži točno aktivne bridove i odgovor je trenutni broj povezanih parova.</p>
'''),
        ('Spojili smo bridove za jedno podstablo – kako ih „odspojiti” za sestrinsko podstablo?',
         r'''
<p>DSU s poništavanjem (rollback): unija po veličini bez sažimanja putova, svaka unija zapiše na stog što je promijenila; nakon povratka iz djeteta vratimo stog na zapamćenu visinu. Bez sažimanja putova <code>find</code> je $O(\log N)$, ali su operacije reverzibilne. Broj parova održavamo inkrementalno: pri spajanju komponenata veličina $s_a, s_b$ dodamo $s_a s_b$, pri poništavanju oduzmemo.</p>
'''),
        ('Zašto je to brzo, i kako se odnosi na službeno rješenje s intervalima i segmentnim stablom?',
         r'''
<p>Na svakoj razini svaki brid pripada popisu točno jednog čvora (onog čiji je prefiks jednak prefiksu njegova $P$) i tamo se ili aktivira jednom ili proslijedi; dakle $O(30 M)$ operacija podjele i $O(30 M)$ unija po $O(\log N)$, plus $O(Q)$ za listove – ukupno $O(30 (M \log N + Q))$. Podstabla u kojima nema upita preskačemo. Službeno rješenje isto stanje opisuje kao $\le 30$ intervala aktivnosti po bridu na vremenskoj osi sortiranih upita, ubačenih u segmentno stablo nad upitima; naša rekurzija po bitovima je to isto stablo, samo indeksirano bitovima $D$ umjesto pozicijama upita, pa nije potrebno binarno tražiti granice intervala.</p>
'''),
        ('Koje su zamke u implementaciji?',
         r'''
<p>Odgovor doseže $\binom{10^5}{2} \approx 5 \cdot 10^9$ – <code>long long</code>. Pri poništavanju treba oduzeti točno ono što je dodano (zapamtiti oba korijena, a veličine rekonstruirati iz trenutnih vrijednosti). Unija koja ništa ne mijenja (isti korijen) također ide na stog kao prazan zapis, ili se preskače – ali dosljedno. Rekurzija je dubine $30$, pa nema problema sa stogom, a upiti s istim $D$ prirodno završe u istom listu.</p>
'''),
    ],
    'tips': [
        r'''Uvjet $C \oplus D < K$ (ili $\le$, $>$) rastavi po <strong>prvom bitu neslaganja s $K$</strong>: za svaki bit gdje $K$ ima $1$ dobivaš jedno podstablo binarnog trie-a – najviše $\log$ disjunktnih intervala za $D$.''',
        r'''Kad je svaki objekt aktivan na nekoliko intervala „vremena” i treba odgovoriti na sve trenutke, koristi <strong>offline dinamičku povezanost</strong>: dijeli-pa-vladaj po vremenu s DSU-om s poništavanjem (unija po veličini, bez sažimanja putova, stog promjena).''',
        r'''Ako je „vrijeme” zapravo vrijednost s bitovnom strukturom, rekurzija po bitovima zamjenjuje segmentno stablo nad sortiranim upitima – jednostavnija implementacija, ista složenost.''',
        r'''Broj povezanih parova $\sum \binom{sz}{2}$ održavaj inkrementalno: spajanje komponenata veličina $a$ i $b$ dodaje točno $ab$ parova.''',
    ],
    'solution': r'''
<p>Promatramo $D = 0, 1, \dots, 2^{30} - 1$ redom. Za svaki brid $j$ skup vrijednosti $D$ takvih da je $(C_j \oplus D) < K$ rastavlja se na najviše $30$ intervala. Time se zadatak svodi na <strong>offline dinamičku povezanost</strong> s $30M$ dodavanja i brisanja bridova.</p>
<p>To rješavamo DSU-om s poništavanjem (rollback) i dijeli-pa-vladaj postupkom po vremenu (segmentno stablo nad upitima sortiranim po $D$), održavajući pritom broj povezanih parova $\sum \binom{sz}{2}$.</p>
<p>Vremenska složenost je $O((Q + M \log N) \log \mathrm{MAX})$.</p>
''',
    'detailed': r'''
<h3>1. Kad je brid aktivan</h3>
<p>Fiksirajmo brid s težinom $C$ i promatrajmo uvjet $C \oplus D < K$ kao funkciju od $D$. Dva različita broja uspoređujemo po najvišem bitu na kojem se razlikuju. Zato je $C \oplus D < K$ ekvivalentno: postoji bit $b$ takav da (i) $C \oplus D$ i $K$ imaju jednake bitove iznad $b$, (ii) $K_b = 1$ i $(C \oplus D)_b = 0$. Za različite $b$ ti su uvjeti međusobno isključivi (bit $b$ je jedinstveno određen kao najviši bit neslaganja), pa je skup dopuštenih $D$ <em>disjunktna unija</em> po bitovima $b$ s $K_b = 1$.</p>
<p>Neka je $P = C \oplus K$. XOR-anjem s $C$: bitovi $C \oplus D$ iznad $b$ jednaki su bitovima $K$ $\iff$ bitovi $D$ iznad $b$ jednaki su bitovima $P$. Nadalje $(C \oplus D)_b = 0 \iff D_b = C_b$, a kako je $K_b = 1$, $C_b = P_b \oplus 1$. Zaključak: za svaki $b$ s $K_b = 1$ skup dopuštenih $D$ je</p>
<p>$$T_b(P) = \{ D : D \gg (b+1) = P \gg (b+1), \; D_b = 1 - P_b \},$$</p>
<p>interval od $2^b$ uzastopnih vrijednosti – u binarnom trie-u nad $D$ to je podstablo <em>brata</em> čvora na putu $P$ na dubini $b$. Primjer: $K = 5 = 101_2$, $C = 4$: $P = 1 = 001_2$; za $b = 2$: $D$ iznad bita $2$ jednak $0$ i $D_2 = 1$, tj. $D \in [4, 7]$; za $b = 0$: $D \gg 1 = 0$ i $D_0 = 0$, tj. $D = 0$. Doista, $4 \oplus D < 5$ vrijedi točno za $D \in \{0, 4, 5, 6, 7\}$.</p>
<h3>2. Rekurzija po bitovima $D$</h3>
<p>Sortiramo upite po $D$; upiti s zajedničkim prefiksom bitova čine susjedan raspon. Definirajmo rekurziju $\text{solve}(b, E, [l, r))$: obrađujemo čvor trie-a na bitu $b$ za raspon upita $[l, r)$ (svi imaju jednak prefiks iznad $b$), a $E$ je popis bridova čiji $P$ ima taj isti prefiks iznad $b$. <strong>Invarijanta:</strong> DSU trenutno sadrži točno one bridove koji su aktivni za <em>sve</em> $D$ u ovom podstablu, tj. bridove kojima je neki $T_{b'}(P)$, $b' > b$, obuhvatio cijelo podstablo; a bridovi izvan $E$ koji nisu u DSU-u nisu aktivni ni za jedan $D$ u podstablu (njihov se $P$ razišao od prefiksa na nekom bitu $b' > b$ – ako je $K_{b'} = 1$ i razlika je bila „pravog smjera”, već su spojeni; inače uvjet (i) ne može biti ispunjen ni za jedan niži bit).</p>
<p>Korak: razdvojimo upite po bitu $b$ na $[l, mid)$ (s $D_b = 0$) i $[mid, r)$ (s $D_b = 1$), a $E$ na $E_0$, $E_1$ po $P_b$. Ako je $K_b = 1$: bridovi iz $E_1$ zadovoljavaju $D_b = 0 = 1 - P_b$ za sve $D$ u djetetu $0$, pa pripadaju $T_b(P)$ cijelog tog podstabla – spojimo ih, rekurzivno riješimo $\text{solve}(b-1, E_0, [l, mid))$ i poništimo; simetrično bridove iz $E_0$ spojimo prije $\text{solve}(b-1, E_1, [mid, r))$. Ako je $K_b = 0$: nema aktivacije, samo $\text{solve}(b-1, E_0, [l, mid))$ i $\text{solve}(b-1, E_1, [mid, r))$. Prazne raspone upita preskačemo. U listu ($b < 0$) svi upiti raspona imaju isti $D$; po invarijanti DSU sadrži točno aktivne bridove pa je odgovor trenutni broj povezanih parova.</p>
<p>Invarijanta se čuva: brid iz $E$ prelazi u dijete samo ako se $P_b$ podudara s $D_b$ (ostaje na putu prefiksa); ako se ne podudara, ili je aktiviran ($K_b = 1$) ili odbačen ($K_b = 0$, uvjet (i) više nikad ne može vrijediti jer se $C \oplus D$ i $K$ razlikuju na bitu $b$ uz $K_b = 0$, dakle $C \oplus D > K$ na tom prefiksu).</p>
<h3>3. DSU s poništavanjem</h3>
<p>Unija po veličini bez sažimanja putova: <code>find</code> se penje do korijena u $O(\log N)$ koraka (stablo veličine $s$ ima dubinu $\le \log_2 s$ jer se manje stablo uvijek vješa pod veće). Svaka unija zapisuje par (pripojeni korijen $b$, novi korijen $a$) na stog; neuspjela unija (isti korijen) zapisuje prazan zapis kako bi visina stoga bila neovisna o ishodu (nije nužno, ali pojednostavljuje). Broj povezanih parova: pri spajanju komponenata veličina $s_a$ i $s_b$ raste za $s_a s_b$ (svaki par „preko granice” postaje povezan); pri poništavanju oduzimamo isto ($s_b \cdot (s_a' - s_b)$, gdje je $s_a'$ trenutna veličina spojene komponente). Rollback do zapamćene visine stoga vraća DSU u točno prijašnje stanje jer operacije poništavamo u obrnutom redoslijedu.</p>
<h3>4. Složenost</h3>
<p>Na razini $b$ svaki brid pripada popisu $E$ najviše jednog čvora (onog čiji prefiks odgovara $P$), a njegov je udio u radu $O(1)$ za podjelu i najviše jedna unija $O(\log N)$. Dakle ukupno $O(30 \cdot M \log N)$ za bridove; upiti se dijele $O(30 Q)$ puta (skeniranje raspona za nalaženje $mid$; moglo bi i binarno, ali skeniranje je ukupno $O(30 Q)$). Sortiranje $O(Q \log Q)$. Ukupno $O(30 (M \log N + Q) + Q \log Q)$, oko $5 \cdot 10^7$ jednostavnih operacija – $0.12$ s uz limit $3$ s. Memorija: popisi bridova duž jednog puta rekurzije ukupno $\le 30 M$ cijelih brojeva u najgorem slučaju (obično mnogo manje), DSU $O(N)$, stog $O(M)$.</p>
<h3>5. Veza sa službenim rješenjem</h3>
<p>Službeno rješenje formulira zadatak kao offline dinamičku povezanost: svaki brid je aktivan na $\le 30$ intervala vrijednosti $D$, tj. na $\le 30$ intervala indeksa sortiranih upita, koji se ubace u segmentno stablo nad upitima i obrađuju DFS-om s rollback DSU-om. Intervali $T_b(P)$ upravo su podstabla trie-a, a naša rekurzija je isti obilazak stabla nad upitima – samo što je stablo određeno bitovima $D$, pa granice intervala ne treba binarno tražiti niti ih zapisivati u čvorove; brid se „prirodno” aktivira u trenutku kad se njegov put razdvoji od puta upita. Složenost je ista: $O((Q + M \log N) \log \max)$.</p>
<h3>6. Primjer</h3>
<p>$N = 4$, $K = 5$, bridovi $(1,2,17), (1,3,4), (2,3,20), (2,4,3), (3,4,5)$. Za $D = 7$: $17 \oplus 7 = 22$, $4 \oplus 7 = 3$, $20 \oplus 7 = 19$, $3 \oplus 7 = 4$, $5 \oplus 7 = 2$ – aktivni su bridovi $(1,3), (2,4), (3,4)$, sve je povezano, odgovor $\binom{4}{2} = 6$. Za $D = 16$: aktivni $(1,2)$ ($17 \oplus 16 = 1$) i $(2,3)$ ($20 \oplus 16 = 4$), komponenta $\{1,2,3\}$ daje $3$. Za $D = 167$ nijedan XOR nije $< 5$, odgovor $0$. Svi se slažu sa službenim izlazom $2, 6, 3, 0$.</p>
''',
    'verified': r'''uzorci 2/2; 300 slučajnih malih testova ($N \le 6$, $M \le 8$, $Q \le 6$, težine i $K$ s $2$–$8$ bitova) protiv brute forcea koji za svaki upit iznova gradi DSU po aktivnim bridovima; 4 velika testa s $N = M = Q = 10^5$ i $30$-bitnim vrijednostima ($K$ slučajno iz $\{2^{30} - 1, \text{slučajan}, 2^{29}, \texttt{0x2AAAAAAA}\}$), najsporiji $0.12$ s.''',
},
# ---------------------------------------------------------------- O
{
    'letter': 'O', 'title': 'Jewel Game', 'title_hr': 'Igra dragulja', 'slug': 'O_jewel_game',
    'tl': '3 s', 'ml': '1024 MB',
    'statement': r'''
<p>Dan je usmjereni graf s $N$ vrhova i $M$ bridova (mogu postojati petlje; iz svakog vrha izlazi barem jedan brid). Na nekim vrhovima je $K$ dragulja; $i$-ti je na vrhu $X_i$ i vrijedi $W_i$. Alice je u $A$, Bob u $B$; naizmjence (Alice prva) igrač prelazi bridom u susjedni vrh i uzima dragulj ako je ondje. Igra završava kad su svi dragulji uzeti ili kad se stanje (na potezu, položaji, preostali dragulji) ponovi. Rezultat je (Aliceina vrijednost) $-$ (Bobova vrijednost); Alice maksimizira, Bob minimizira. Odredi rezultat pri optimalnoj igri.</p>
<h3>Ulaz</h3>
<p>$N, M, A, B$ ($2 \le N \le 30$), $M$ bridova, $K$ ($1 \le K \le 10$) i $K$ redaka $X_i\ W_i$ ($X_i \notin \{A, B\}$, $1 \le W_i \le 10^8$).</p>
<h3>Izlaz</h3>
<p>Rezultat igre.</p>
''',
    'hints': [
        r'''<p>Stanje: (skup preostalih dragulja, položaj igrača na potezu, položaj drugog igrača), ukupno $2^K \cdot N^2 \cdot 2$ stanja. Prijelazi unutar istog skupa dragulja mogu tvoriti cikluse — obična rekurzija ne radi.</p>''',
        r'''<p>Uzimanjem dragulja skup se strogo smanjuje, pa cikluse imaju samo prijelazi koji ne uzimaju dragulj. Rješavaj skupove po rastućoj veličini; za fiksni skup koristi <em>retrogradnu analizu</em> (backward induction) kao za igre s ciklusima, ali s vrijednostima umjesto pobjeda/poraza.</p>''',
        r'''<p>Ponavljanje stanja završava igru s trenutnim rezultatom — dakle vrijednost „ostanka u ciklusu” je $0$ (daljnji doprinos). Igrač će ući u ciklus samo ako mu nijedan izlaz ne donosi pozitivnu vrijednost.</p>''',
    ],
    'coach': [
        ('Što čini stanje igre i koliko ih ima?',
         r'''
<p>Stanje je (skup preostalih dragulja, tko je na potezu, položaj Alice, položaj Boba) – najviše $2^{10} \cdot 2 \cdot 30^2 \approx 1.8 \cdot 10^6$ stanja, a iz svakog izlazi najviše $\deg$ poteza; graf stanja ima $O(2^K N M)$ bridova, što je sasvim obradivo. Vrijednost stanja definiramo kao <em>buduću</em> razliku (Alice $-$ Bob) pri optimalnoj igri; Alice traži maksimum, Bob minimum po potezima. Odgovor je vrijednost početnog stanja.</p>
'''),
        ('Zašto obična rekurzija (memoizirani minimax) ne radi?',
         r'''
<p>Potezi bez uzimanja dragulja ostavljaju skup dragulja istim, pa graf stanja ima cikluse: rekurzija bi se vrtjela, a Bellmanova jednadžba $V(s) = \max/\min V(\text{sljedbenik})$ nema jedinstveno rješenje (na ciklusu je svaka konstanta rješenje). Jedini potezi koji „napreduju” su oni koji uzimaju dragulj – oni vode u strogo manji skup. Zato skupove obrađujemo po rastućem broju dragulja: unutar jednog sloja (fiksni skup) sve su vrijednosti izlaza u manje slojeve već poznate, a ostaje ciklički graf s $2N^2$ stanja.</p>
'''),
        ('Koliko „vrijedi” ostati u ciklusu?',
         r'''
<p>Pravilo ponavljanja: kad se stanje ponovi, igra završava s dosad skupljenim rezultatom. Unutar sloja potezi ne mijenjaju rezultat, pa igra koja ostane u sloju zauvijek ima buduću vrijednost točno $0$. Zato Alice ima interes izaći iz sloja samo potezom pozitivne vrijednosti, Bob samo potezom negativne vrijednosti; ako nitko nema takav izlaz, obojica radije „kruže” i vrijednost je $0$.</p>
'''),
        ('Kako riješiti jedan ciklički sloj kad su vrijednosti u pitanju, a ne samo pobjeda/poraz?',
         r'''
<p>Retrogradna analiza s tri pravila. (a) Stanje čiji su svi sljedbenici određeni dobiva max (Alice) ili min (Bob) njihovih vrijednosti. (b) Ako pravilo (a) više nije primjenjivo, među neodređenim stanjima uzmemo ono s <em>najvećom apsolutnom</em> vrijednošću već određene opcije, pod uvjetom da je predznak „pravi” (pozitivna za Alice, negativna za Boba), i tu mu vrijednost dodijelimo: taj igrač ne može dobiti ništa bolje – protivnik u svakom neodređenom stanju ima neodređenog sljedbenika (inače bi (a) vrijedilo) i može ostati unutra dok igrač ne izađe nekim izlazom koji po izboru nije bolji, ili do ponavljanja ($0$). (c) Kad nema kandidata, sva preostala stanja imaju vrijednost $0$: svaki igrač može ostati unutra, a protivnikovi izlazi mu ne štete.</p>
'''),
        ('Kako to efikasno implementirati i zašto je (b) sigurno s obzirom na pravilo ponavljanja?',
         r'''
<p>Za svako stanje čuvamo broj neodređenih unutarnjih sljedbenika i najbolju određenu opciju; red za pravilo (a) i max-heap po apsolutnoj vrijednosti za pravilo (b) (zastarjele unose preskačemo). Kad stanje odredimo, ažuriramo prethodnike preko obrnutih bridova. Dokaz korektnosti ide preko strategije „slijedi izbor iz trenutka određivanja”: pokazuje se da svaki Bobov potez iz stanja $u$ vodi u stanje vrijednosti $\ge V(u)$ (i simetrično za Alice), a pozitivan ciklus konstantne vrijednosti ne može nastati jer se u njemu indeks određivanja strogo smanjuje – pa ponavljanje može zatvoriti igru samo kad je $V \le 0$, što Alice ne šteti. Ukupno $O(2^K \cdot N M \log(NM))$.</p>
'''),
    ],
    'tips': [
        r'''Igre s ciklusima rješavaj <strong>retrogradnom analizom</strong> (unatrag od stanja čiji su svi sljedbenici poznati); kad umjesto pobjede/poraza imaš vrijednosti, redoslijed određivanja ide po najvećoj apsolutnoj vrijednosti, jer igrač s takvom opcijom nikad ne može dobiti bolje od nje.''',
        r'''Nađi <strong>monotonu komponentu stanja</strong> (ovdje skup preostalih dragulja) i obradi ju po slojevima – ciklusi ostaju samo unutar sloja, gdje je graf malen.''',
        r'''Pravilo „ponavljanje završava igru” znači da beskonačno kruženje vrijedi $0$ dodatno; stanje bez korisnog izlaza za igrača na potezu ima vrijednost $0$, ne $-\infty$.''',
        r'''Vrijednosti čuvaj u <em>apsolutnoj</em> perspektivi (Alice $-$ Bob) s eksplicitnim tko-je-na-potezu umjesto negamaxa – lakše je pratiti predznake u pravilu (b) i u heapu.''',
    ],
    'solution': r'''
<p>Budući da je $K \le 10$, htjeli bismo DP oblika $dp[\text{skup preostalih dragulja}][\text{položaj igrača na potezu}][\text{položaj drugog igrača}] = \text{rezultat igre}$. Međutim, u računanju postoje ciklusi, pa vrijednosti ne možemo odrediti izravno.</p>
<p>Jedan način analize igara s ciklusima je retrogradna analiza (backward induction), koja se obično koristi za određivanje pobjede, poraza ili neriješenog ishoda, ali njome možemo odrediti i rezultat igre.</p>
<p>Ako u računanju postoje ciklusi, skup preostalih dragulja unutar ciklusa se ne mijenja. Stoga vrijednosti određujemo retrogradnom analizom po rastućoj veličini skupa preostalih dragulja. Konkretno, retrogradnu analizu izvodimo $2^K$ puta, po rastućoj veličini skupa preostalih dragulja:</p>
<ol>
    <li>Ako postoji vrh čije su vrijednosti svih izlaznih bridova već određene, možemo odrediti vrijednost tog vrha.</li>
    <li>Ako još postoje vrhovi s neodređenom vrijednošću, pogledamo odredišta svih izlaznih bridova iz tih vrhova i odaberemo najveću vrijednost ako je pozitivna; tada određujemo vrijednost vrha iz kojeg taj brid izlazi.</li>
    <li>Ako se vrijednost i dalje ne može odrediti, ona je $0$.</li>
</ol>
<p>Vremenska složenost je $O(2^K N (N + M) \log N)$.</p>
''',
    'detailed': r'''
<h3>1. Stanja i slojevi</h3>
<p>Stanje je $(S, t, a, b)$: skup preostalih dragulja $S \subseteq \{1..K\}$, tko je na potezu $t \in \{\text{Alice}, \text{Bob}\}$, položaji $a, b$. Neka je $V(S, t, a, b)$ buduća razlika (Alice $-$ Bob) pri optimalnoj igri iz tog stanja (rezultat skupljen ranije samo se pribraja). Potez iz $(S, A, a, b)$ bridom $a \to v$: ako je na $v$ dragulj $j \in S$, prelazimo u $(S \setminus \{j\}, B, v, b)$ s dobitkom $+W_j$; inače u $(S, B, v, b)$ bez dobitka. Bob analogno s dobitkom $-W_j$. Kad je $S = \emptyset$, igra je gotova: $V = 0$.</p>
<p>Potezi koji uzimaju dragulj strogo smanjuju $S$; potezi bez dragulja ostaju u istom $S$. Zato slojeve $S$ obrađujemo po rastućem $|S|$ (ili po rastućem broju bitova maske): kad radimo sloj $S$, sve vrijednosti stanja u manjim slojevima već su poznate. Unutar sloja ostaje graf od $2N^2$ stanja s <em>unutarnjim</em> bridovima (potezi bez dragulja, ostaju u sloju) i <em>izlazima</em> (potezi s draguljem, poznata vrijednost $\pm W_j + V(\text{manji sloj})$). Unutarnji bridovi mogu tvoriti cikluse.</p>
<h3>2. Ponavljanje i vrijednost ciklusa</h3>
<p>Pravilo „igra završava kad se stanje ponovi” zajedno s konačnim brojem stanja jamči da je igra konačna. Ako igra iz nekog trenutka ostane zauvijek u sloju $S$, ne mijenja se rezultat (nema uzimanja dragulja) – buduća vrijednost je $0$. To je ključ: „kruženje” vrijedi točno $0$ za oba igrača.</p>
<h3>3. Retrogradna analiza jednog sloja</h3>
<p>Za svako stanje $s$ sloja vodimo $\text{cnt}[s]$ = broj još neodređenih unutarnjih sljedbenika i $\text{best}[s]$ = najbolja (max za Alice, min za Boba) vrijednost među već određenim opcijama (izlazi + određeni unutarnji sljedbenici). Pravila, primjenjivana dok ima posla:</p>
<ol>
    <li><strong>(a)</strong> Ako je $\text{cnt}[s] = 0$, sve su opcije poznate: $V(s) = \text{best}[s]$.</li>
    <li><strong>(b)</strong> Inače među neodređenim stanjima s „pravim” predznakom ($\text{best} > 0$ za Alice na potezu, $\text{best} < 0$ za Boba) uzmemo ono s najvećom $|\text{best}[s]|$ i stavimo $V(s) = \text{best}[s]$.</li>
    <li><strong>(c)</strong> Ako više nema ni (a) ni (b), sva preostala stanja imaju $V = 0$.</li>
</ol>
<p>Kad odredimo $V(s)$, prođemo prethodnike $p$ preko obrnutih bridova (protivnik je došao na svoj trenutni vrh bez dragulja): smanjimo $\text{cnt}[p]$, ažuriramo $\text{best}[p]$, stavimo $p$ u red za (a) ako je $\text{cnt}[p]$ pao na $0$, odnosno u heap za (b) ako je $\text{best}[p]$ dobio pravi predznak ili se poboljšao. U heapu su unosi (|best|, stanje); zastarjele (stanje već određeno ili |best| se promijenio) preskačemo. Red za (a) ima prednost pred heapom.</p>
<h3>4. Zašto je (b) ispravno: intuicija</h3>
<p>Neka je $s$ Aliceino stanje s $\text{best}[s] = v > 0$, najveće apsolutne vrijednosti među kandidatima. Alice iz $s$ sigurno može dobiti $v$ (odigra tu opciju; ako je to unutarnji određeni sljedbenik, njegova vrijednost je već dokazana). Može li više? Svaka druga opcija ili je određena (vrijednost $\le v$ po definiciji best) ili je neodređeno stanje $t$. Bob u svakom neodređenom stanju ima neodređenog sljedbenika (inače bi (a) vrijedilo), pa može „ostati unutra”. Tada igra iz $t$ ili završi ponavljanjem (vrijednost $0 < v$) ili Alice u nekom neodređenom stanju $u$ izađe određenom opcijom vrijednosti $\le \text{best}[u] \le v$ (za neodređena Aliceina stanja best je ili $\le 0$ ili kandidat s $|\text{best}| \le v$). Dakle $V(t) \le v$ i $V(s) = v$. Za Bobove kandidate simetrično. Pravilo (c): kad nema kandidata, svaki igrač može ostati unutra, a protivnikovi izlazi mu nisu štetni (Aliceini $\le 0$, Bobovi $\ge 0$), pa je vrijednost $0$.</p>
<h3>5. Strogi dokaz (s pravilom ponavljanja)</h3>
<p>Gornja intuicija prešutno rabi „vrijednost određenog stanja” kao da je neovisna o povijesti, a s pravilom ponavljanja ulazak u već posjećeno stanje završava igru s $0$ umjesto s $V$. Zato dokazujemo izravno da je $V(s_0)$ vrijednost igre iz početnog stanja. Neka je $\tau(s)$ redni broj određivanja stanja $s$ (stanja iz pravila (c) određena su na kraju).</p>
<p><strong>Lema 1 (monotonost).</strong> Za svako Bobovo stanje $u$ i svaku njegovu opciju $x$ (izlaz ili unutarnji sljedbenik) vrijedi $V(x) \ge V(u)$, a za opciju odabranu pri određivanju vrijedi jednakost i $\tau(x) < \tau(u)$ (ili je $x$ izlaz). Simetrično za Alice s $\le$. <em>Dokaz.</em> Za $u$ određeno po (a) sve su opcije već određene i $V(u)$ je njihov minimum. Za $u$ određeno po (b) s $V(u) = -m$ ($m$ = najveća apsolutna vrijednost u tom trenutku) treba pokazati da svako tada neodređeno stanje $x$ na kraju dobije $V(x) \ge -m$. Pretpostavimo suprotno i uzmimo prvo takvo $z$ (po $\tau$) s $V(z) < -m$. Ako je $z$ određeno po (c), $V(z) = 0$ – nemoguće. Ako je $z$ Aliceino po (b), $V(z) > 0$ – nemoguće. Ako je $z$ Aliceino po (a), $V(z)$ je maksimum svih njegovih opcija, pa su sve $< -m$; barem je jedna bila neodređena u trenutku određivanja $u$ (inače bi $z$ bilo određeno po (a) prije $u$), a ona je određena prije $z$ s vrijednošću $< -m$ – proturječje s minimalnošću. Ako je $z$ Bobovo (po (a) ili (b)), $V(z) = \text{best}[z]$ potječe od neke opcije vrijednosti $\le V(z) < -m$: ako je ta opcija bila određena već pri određivanju $u$, tada je $\text{best}[z] < -m$ već tada, pa bi $z$ bio kandidat veće apsolutne vrijednosti od $u$ – proturječje; inače je određena kasnije, a prije $z$ – proturječje s minimalnošću. Za $u$ određeno po (c): $V(u) = 0$, izlazi i određeni sljedbenici su $\ge 0$ (inače bi $u$ bio kandidat), a neodređeni sljedbenici su (c)-stanja vrijednosti $0$; odabrana opcija je jedan (c)-sljedbenik (postoji jer je $\text{cnt}[u] > 0$). $\square$</p>
<p><strong>Lema 2 (strategija).</strong> Alice, igrajući iz svakog određenog stanja opciju odabranu pri određivanju, a iz (c)-stanja u (c)-sljedbenika, postiže barem $V(s_0)$ iz početnog stanja sloja $s_0$ (uz indukciju po slojevima za izlaze). <em>Dokaz.</em> Duž odigrane partije unutar sloja $V$ je nepadajuća: Alicein potez čuva $V$ (Lema 1, jednakost), Bobov potez ne smanjuje $V$ (Lema 1). Ako partija izađe iz sloja izlazom vrijednosti $g + V(\text{manji sloj})$, po indukciji Alice u manjem sloju dobiva barem $V(\text{manji sloj})$, ukupno $\ge V(\text{trenutno}) \ge V(s_0)$. Ako partija završi ponavljanjem, dobitak od ulaska u sloj je $0$; tvrdimo $V(s_0) \le 0$. Ponavljanje sadrži ciklus stanja duž kojeg je $V$ nepadajuća i vraća se na istu vrijednost, dakle konstantna, recimo $c \ge V(s_0)$. Kad bi bilo $c > 0$: sva su stanja ciklusa određena po (a) ili (b) (ne po (c), jer je $V \ne 0$), Bobova stanja ciklusa određena su po (a) (Bobovo (b) daje negativnu vrijednost), pa su pri njihovu određivanju svi sljedbenici već bili određeni – Bobov potez strogo smanjuje $\tau$; Alicein potez strogo smanjuje $\tau$ po Lemi 1. Duž ciklusa bi $\tau$ strogo padao i vratio se na početak – proturječje. Dakle $c \le 0$, pa $V(s_0) \le 0$ i ponavljanje Alici ne šteti. $\square$</p>
<p>Simetrično Bob postiže najviše $V(s_0)$, pa je $V(s_0)$ točna vrijednost igre. Za početno stanje cijele igre (svi dragulji, Alice na $A$, Bob na $B$) to je traženi odgovor.</p>
<h3>6. Složenost i memorija</h3>
<p>Po sloju: inicijalizacija prolazi izlazne bridove igrača na potezu za svako stanje – $\sum_{t, a, b} \deg(\text{igrač na potezu}) = 2N \sum_v \deg(v) = 2NM$; određivanje svakog stanja prolazi obrnute bridove dolaska – ukupno opet $O(NM)$; svako poboljšanje $\text{best}$ gura unos u heap, $O(NM)$ unosa, $O(NM \log(NM))$. Ukupno $O(2^K \cdot NM \log(NM))$; s $K = 10$, $N = 30$, $M = 900$ to je oko $1024 \cdot 5.4 \cdot 10^4 \cdot \log \approx 10^9$ elementarnih koraka u najgorem slučaju po grubom računu, u praksi $0.34$ s za potpuni graf. Memorija: $2^K \cdot 2(N+1)^2$ vrijednosti tipa <code>long long</code> $\approx 16$ MB.</p>
<h3>7. Primjer</h3>
<p>U prvom primjeru Alice i Bob kreću s vrha $1$, iz kojeg vode bridovi u $2, 3, 4, 5$ (dragulji $4, 84, 38, 96$), a među vrhovima $2..5$ vode bridovi u sve ostale osim natrag u $1$. Alice uzme $96$ (vrh $5$), Bob $84$, Alice $38$, Bob $4$: $96 - 84 + 38 - 4 = 46$. Da je Alice počela s $84$, Bob bi uzeo $96$ i završila bi lošije; algoritam to nalazi kroz vrijednosti manjih slojeva.</p>
<h3>8. Zamke</h3>
<ul>
    <li>Vrijednosti do $10 \cdot 10^8 = 10^9$ – stanu u <code>int</code>, ali s međuzbrojevima $\pm$ radi sigurnosti <code>long long</code>.</li>
    <li>Petlje ($u \to u$) su dopuštene: unutarnji brid u isto stanje sa zamijenjenim igračem na potezu – ništa posebno, ali prethodnike treba skupljati preko obrnutih bridova, ne pretpostavkom $u \ne v$.</li>
    <li>Prethodnici određenog stanja $(t, a, b)$: protivnik je došao na svoj vrh potezom bez dragulja, pa ako je na tom vrhu dragulj koji je još u skupu, stanje nema unutarnjih prethodnika.</li>
    <li>Zastarjeli unosi u heapu: provjeri da je stanje još neodređeno i da mu je $|\text{best}|$ jednak zapisanom.</li>
    <li>Red za (a) uvijek prazniti prije heapa – dokaz pravila (b) pretpostavlja da neodređena stanja imaju neodređenog sljedbenika.</li>
</ul>
''',
    'verified': r'''uzorci 2/2; 300 slučajnih malih testova ($N \le 4$, $K \le 2$) te dodatnih 150 s $N \in [4, 6]$, $K \in [2, 3]$ protiv brute forcea koji doslovno simulira igru s pravilom ponavljanja (minimax nad povijesti posjećenih stanja); 3 velika testa s $N = 30$, $K = 10$ i gustoćom bridova $0.15$, $0.5$ i $1$ (potpuni graf), najsporiji $0.34$ s.''',
},
]
