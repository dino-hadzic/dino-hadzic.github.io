# -*- coding: utf-8 -*-
STAGE = {
    'no': 19,
    'name': 'Stage 19: America',
    'source_name': '2022-2023 ICPC North America Championship',
    'no_editorial': True,
    'community': True,
    'source_html': r'''
<p>Zadaci potječu s natjecanja The 2023 ICPC North America Championship (NAC 2023). Tekst zadatka preveden je prema službenim <a href="https://contest.ucup.ac/download.php?type=attachments&amp;id=1248&amp;r=0">engleskim tekstovima zadataka</a>. Organizatori Universal Cupa nisu objavili editorial; rješenja su napisana prema <a href="http://serjudging.vanb.org/wp-content/uploads/nac.pdf">službenim slajdovima sudaca NAC 2023</a> i vlastitim, lokalno testiranim implementacijama. Zadatak je dostupan na <a href="https://contest.ucup.ac/contest/1248">Universal Cup Judging System</a>.</p>
''',
}

PROBLEMS = [
# ---------------------------------------------------------------- A
{
    'letter': 'A', 'title': 'Allergen Testing', 'title_hr': 'Testiranje alergena', 'slug': 'A_allergen_testing',
    'tl': '1 s', 'ml': '2 GiB',
    'statement': r'''
<p>Imaš $n$ spojeva i točno na jedan si alergičan; imaš $d$ dana da otkriješ koji. Na ruci pripremiš neki broj mjesta za testiranje. Svakog dana točno jednom: svaki spoj naneseš na neki (možda prazan) podskup mjesta (više spojeva na isto mjesto je dopušteno), zatim pogledaš koja mjesta reagiraju. Mjesto reagira ako i samo ako je na njega nanesen alergen; mjesto koje je reagiralo više se ne može koristiti.</p>
<p>Odredi najmanji broj mjesta koji jamči da ćeš u $d$ dana sigurno odrediti alergen.</p>
<h3>Ulaz</h3>
<p>$1 \le t \le 10^4$ testova; u svakom $n$ i $d$, $1 \le n, d \le 10^{18}$.</p>
<h3>Izlaz</h3>
<p>Za svaki test najmanji broj mjesta.</p>
<h3>Primjer</h3>
<p>$n = 4$, $d = 1$: $2$.</p>
''',
    'hints': [
        r'''
<p>Zaboravi na trenutak strategiju i broji <em>ishode</em>: što sve na kraju $d$ dana možeš znati o jednom mjestu na ruci?</p>
''',
        r'''
<p>Svako mjesto reagira najviše jednom, pa je njegova „povijest” samo jedan broj: dan reakcije ($1, \dots, d$) ili „nikad”. Koliko različitih povijesti ima $k$ mjesta zajedno?</p>
''',
        r'''
<p>Gornju granicu $(d+1)^k$ pokušaj i dostići: svakom spoju unaprijed dodijeli jednu povijest i nanesi ga na mjesto $j$ točno onog dana koji ta povijest predviđa.</p>
''',
    ],
    'coach': [
        ('Koliko je informacije uopće dostupno? Što je jedino što na kraju vidiš?',
         r'''
<p>Jedino što vidiš jesu reakcije mjesta. Mjesto koje je reagiralo više se ne koristi, pa se za svako mjesto na kraju zna točno jedna stvar: dan kad je reagiralo ($1,\dots,d$) ili da nije reagiralo. To je $d+1$ mogućnosti po mjestu, dakle najviše $(d+1)^k$ različitih ishoda s $k$ mjesta. Ako je $n > (d+1)^k$, dva spoja nužno dijele ishod i ne možeš ih razlikovati, bez obzira na strategiju (čak i adaptivnu!).</p>
'''),
        ('Je li granica dostižna, tj. možemo li stvarno „upisati” proizvoljnu povijest svakom spoju?',
         r'''
<p>Da. Spoju $c$ dodijelimo vektor $(s_1,\dots,s_k)$ gdje je $s_j \in \{1,\dots,d,\text{nikad}\}$, sve međusobno različite (ima ih $(d+1)^k \ge n$). Spoj $c$ nanosimo na mjesto $j$ samo onog dana $s_j$. Ako je $c$ alergen, mjesto $j$ reagira točno dana $s_j$ – prije ne može, jer reakciju uzrokuje samo alergen, a on na $j$ dolazi tek tada. Ostali spojevi ne reagiraju pa ne smetaju. Dakle, iz ishoda pročitamo vektor alergena, a on ga jednoznačno određuje. Strategija je čak neadaptivna.</p>
'''),
        ('Zašto se odgovor ne mijenja ako nam dopuste adaptivnu strategiju?',
         r'''
<p>Provjeri argument iz prvog koraka: brojanje ishoda ne ovisi o tome kako biramo podskupove, pa je $(d+1)^k$ gornja granica i za adaptivne strategije. Za sigurnost, u brute forceu se može izračunati $F(k,d)$ = najveći broj spojeva koji se sigurno razlikuje: alergen jednog dana reagira na nekom podskupu $S$ mjesta koja potom otpadaju, pa $F(k,d) = \sum_{j} \binom{k}{j} F(k-j,\,d-1)$, $F(k,0)=1$. Binomni teorem daje upravo $F(k,d) = (d+1)^k$.</p>
'''),
        ('Kako sigurno izračunati najmanji $k$ kad su $n, d \le 10^{18}$?',
         r'''
<p>Tražimo najmanji $k$ s $(d+1)^k \ge n$. Množimo redom $1, (d+1), (d+1)^2, \dots$ dok ne dosegnemo $n$; koraka je najviše $\lceil \log_2 10^{18} \rceil = 60$. Jedina zamka: $(d+1)^2$ može premašiti $10^{36}$, a to ne stane u 64 bita. Ili množi u <code>__int128</code>, ili prije množenja provjeri <code>moc > n / (d+1)</code> (tada odmah znaš da je sljedeća potencija $\ge n$). Poseban slučaj $n=1$ daje $k=0$.</p>
'''),
    ],
    'tips': [
        r'''<strong>Broji ishode, ne strategije.</strong> U zadacima tipa „najmanje testova/pitanja/vaganja” gornja granica gotovo uvijek dolazi iz broja razlučivih ishoda ($\text{ishodi} \ge \text{kandidati}$), a donja iz eksplicitne konstrukcije koja svaki ishod iskoristi.''',
        r'''Kad je odgovor oblika „najmanji $k$ s $b^k \ge n$”, ne koristi <code>log</code>/<code>pow</code> u pomičnom zarezu – zaokruživanje pri $10^{18}$ lako pokvari odgovor za $\pm 1$. Množi cijele brojeve i pazi na prelijevanje.''',
        r'''Kad nisi siguran vrijedi li zatvorena formula, napiši rekurziju po pravilima igre za male vrijednosti i usporedi – ovdje $F(k,d)=\sum_j \binom{k}{j}F(k-j,d-1)$ potvrđuje $(d+1)^k$.''',
    ],
    'solution': r'''
<p>Svako mjesto reagira najviše jednom, pa je na kraju za svako mjesto poznato samo kojeg je dana reagiralo ($1,\dots,d$) ili da nije. S $k$ mjesta razlučivo je stoga najviše $(d+1)^k$ ishoda, pa je potrebno $(d+1)^k \ge n$. Granica se postiže: svakom spoju dodijelimo različit vektor $(s_1,\dots,s_k)$, $s_j\in\{1,\dots,d,\text{nikad}\}$, i spoj nanosimo na mjesto $j$ točno dana $s_j$; ishod tada izravno otkriva vektor alergena. Odgovor je najmanji $k$ s $(d+1)^k\ge n$, koji nalazimo uzastopnim množenjem u najviše $60$ koraka (u <code>__int128</code> ili s provjerom prelijevanja).</p>
''',
    'detailed': r'''
<h3>1. Što se uopće može opaziti</h3>
<p>Pravila su asimetrična: samo alergen izaziva reakciju, a mjesto koje je reagiralo izlazi iz igre. Zato je cijela povijest jednog mjesta opisana jednim podatkom – <em>danom prve (i jedine) reakcije</em>, ili činjenicom da nije reagiralo. To je $d+1$ mogućnosti. Za $k$ mjesta ukupni ishod pokusa je $k$-torka takvih podataka, dakle najviše $(d+1)^k$ različitih ishoda.</p>
<p>Ishod je jedino što na kraju znamo. Ako je $n > (d+1)^k$, po Dirichletovu principu postoje dva spoja koja bi (kad bi bila alergen) dala isti ishod, pa ih nikako ne razlikujemo. Bitno je da ovaj argument <strong>ne pretpostavlja ništa o strategiji</strong>: vrijedi i ako svaki dan odlučujemo na temelju prethodnih reakcija (adaptivno). Dakle nužno je $(d+1)^k \ge n$.</p>
<h3>2. Konstrukcija koja granicu dostiže</h3>
<p>Uzmemo $k$ s $(d+1)^k \ge n$ i svakom od $n$ spojeva dodijelimo <em>različit</em> vektor $s^{(c)} = (s_1,\dots,s_k)$, $s_j \in \{1,2,\dots,d\} \cup \{\infty\}$, gdje $\infty$ znači „nikad”. Plan je jednostavan i unaprijed fiksiran: spoj $c$ nanosimo na mjesto $j$ jedino dana $s_j^{(c)}$ (ako je $s_j^{(c)}=\infty$, nikad ga ne nanosimo na $j$).</p>
<p>Zašto to radi? Neka je alergen spoj $a$. Mjesto $j$ ne može reagirati prije dana $s_j^{(a)}$ jer do tada na njega dolaze samo ne-alergeni. Dana $s_j^{(a)}$ na njega dolazi $a$ pa reagira (a mjesto je do tada sigurno neiskorišteno). Ako je $s_j^{(a)}=\infty$, mjesto $j$ nikad ne reagira. Tako je opaženi ishod upravo vektor $s^{(a)}$, a vektori su različiti, pa jednoznačno pročitamo $a$. Napomena: plan predviđa nanošenje drugih spojeva na mjesto $j$ i nakon što je ono reagiralo; ta nanošenja jednostavno ispuštamo – ona su služila samo „drugim granama” koje se više ne mogu dogoditi.</p>
<h3>3. Provjera preko rekurzije igre</h3>
<p>Ako sumnjamo u zatvorenu formulu, izračunajmo $F(k,d)$ = najveći broj spojeva koji se s $k$ mjesta u $d$ dana sigurno razlikuje. Prvog dana alergen reagira na nekom podskupu $S$ mjesta ($|S|=j$); ta mjesta otpadaju, a preostaju $k-j$ mjesta i $d-1$ dana za sve spojeve koji su bili na točno tom podskupu. Različiti podskupovi vode u različite grane, pa je optimalno svaku granu napuniti do maksimuma: $$F(k,d)=\sum_{j=0}^{k}\binom{k}{j}F(k-j,\,d-1),\qquad F(k,0)=1.$$ Indukcijom po $d$: ako je $F(\cdot,d-1)=d^{\,\cdot}$, onda $F(k,d)=\sum_j\binom{k}{j}d^{\,k-j}=(d+1)^k$ po binomnom teoremu. Ova rekurzija je i naš brute force.</p>
<h3>4. Računanje odgovora</h3>
<p>Tražimo najmanji $k\ge 0$ s $(d+1)^k\ge n$. Za $n=1$ odgovor je $0$ (nema što razlikovati). Inače krenemo od $\text{moc}=1$ i množimo s $d+1$ dok $\text{moc} < n$; kako je $d+1\ge 2$, petlja ima najviše $\lceil\log_2 n\rceil \le 60$ koraka, a za $t\le 10^4$ testova to je trenutno.</p>
<p>Jedina tehnička opasnost je prelijevanje: već $(d+1)^2$ može biti reda $10^{36}$. U kodu množimo u <code>__int128</code> (raspon do $\approx 1.7\cdot 10^{38}$, a nikad ne množimo broj $\ge n$, pa je umnožak $< n\cdot(d+1) \le 10^{36}+10^{18}$). Alternativa bez <code>__int128</code>: prije množenja provjeriti <code>moc > n / (d + 1)</code> i tada odmah zaključiti da je sljedeća potencija $\ge n$. Ne koristimo <code>log</code> ni <code>pow</code> u pomičnom zarezu – pri $10^{18}$ greška zaokruživanja lako pomakne odgovor za $1$.</p>
<h3>5. Složenost</h3>
<p>$O(t\log n)$ vremena, $O(1)$ memorije.</p>
''',
    'verified': r'''uzorak 1/1; 300 slučajnih testova ($n\le 100$, $d\le 10$, plus veliki $n,d\le 10^{18}$) protiv brute forcea koji računa $F(k,d)$ rekurzijom igre; 2 velika testa s $t=10^4$ ($<0.01$ s).''',
},
# ---------------------------------------------------------------- B
{
    'letter': 'B', 'title': 'A Tree and Two Edges', 'title_hr': 'Stablo i dva brida', 'slug': 'B_a_tree_and_two_edges',
    'tl': '3 s', 'ml': '2 GiB',
    'statement': r'''
<p>Dan je povezan jednostavan graf s $n$ vrhova i $n + 1$ bridova (stablo s dva dodatna brida). Za svaki od $q$ upita $(u, v)$, $u \ne v$, odredi broj jednostavnih putova (bez ponavljanja vrhova) između $u$ i $v$.</p>
<h3>Ulaz</h3>
<p>$4 \le n \le 5 \cdot 10^4$, $1 \le q \le 5 \cdot 10^4$; $n + 1$ različitih bridova $a \lt b$; $q$ upita $u \lt v$.</p>
<h3>Izlaz</h3>
<p>$q$ redaka s brojem putova.</p>
<h3>Primjer</h3>
<p>$n = 4$, bridovi $1\text{-}2, 1\text{-}3, 1\text{-}4, 2\text{-}3, 2\text{-}4$: upiti $(1,2), (1,3), (1,4), (2,3), (2,4), (3,4)$ daju $3, 3, 3, 3, 3, 4$. $n = 6$, bridovi $1\text{-}2, 1\text{-}3, 1\text{-}6, 2\text{-}3, 3\text{-}4, 3\text{-}5, 4\text{-}5$: upiti $(1,2), (1,3), (1,4), (1,6)$ daju $2, 2, 4, 1$.</p>
''',
    'hints': [
        r'''
<p>Izaberi razapinjuće stablo $T$; ostaju dva „dodatna” brida. Koliko puta jednostavan put može proći dodatnim bridom, i kako izgleda dio puta između dva prolaska dodatnim bridovima?</p>
''',
        r'''
<p>Između prolazaka dodatnim bridovima put koristi samo bridove stabla, dakle jedinstveni put u $T$. Kandidata je najviše $1 + 4 + 8 = 13$; kandidat je valjan točno kad su njegovi segmenti u stablu u parovima vršno disjunktni.</p>
''',
        r'''
<p>Dva puta u stablu se sijeku točno kad dublji od njihova dva LCA-a leži na drugom putu – jedan LCA i par provjera „je li predak” Eulerovim vremenima.</p>
''',
    ],
    'coach': [
        ('Kako iskoristiti to da graf ima samo dva brida više od stabla?',
         r'''
<p>Fiksirajmo razapinjuće stablo $T$ (npr. unijom-pronađi pri čitanju bridova); bridovi $e_1, e_2$ koji zatvaraju ciklus su „dodatni”. Jednostavan put ne ponavlja vrhove, pa svaki dodatni brid prolazi najviše jednom. Dio puta između dva uzastopna prolaska dodatnim bridovima (i prije prvog / poslije zadnjeg) koristi samo bridove stabla i ne ponavlja vrhove – a u stablu je takav put jedinstven. Dakle je put potpuno određen nizom dodatnih bridova koje koristi, s redoslijedom i smjerom.</p>
'''),
        ('Koliko kandidata ima i kako se razlikuju?',
         r'''
<p>Bez dodatnih bridova: $1$ (put u stablu). S jednim: $2$ brida $\times$ $2$ smjera $= 4$. S oba: $2$ redoslijeda $\times$ $2 \times 2$ smjera $= 8$. Ukupno najviše $13$. Različiti kandidati daju različite putove (put jednoznačno određuje koje dodatne bridove koristi, kojim redom i u kojem smjeru), pa nema dvostrukog brojanja. Kandidat $u \to p \xrightarrow{e} r \to v$ je jednostavan put točno kad su putovi u stablu $u\text{-}p$ i $r\text{-}v$ vršno disjunktni; za dva brida tri segmenta moraju biti disjunktni u parovima.</p>
'''),
        ('Kako u $O(\log n)$ provjeriti sijeku li se dva puta u stablu?',
         r'''
<p>Neka su $\ell_1 = \mathrm{lca}(x_1, y_1)$ i $\ell_2 = \mathrm{lca}(x_2, y_2)$, i neka je $\ell_1$ dublji (ili jednako dubok). Tvrdnja: putovi se sijeku točno kad $\ell_1$ leži na putu $x_2\text{-}y_2$. Ako je $w$ zajednički vrh, i $\ell_1$ i $\ell_2$ su preci od $w$, dakle usporedivi, pa je $\ell_1$ potomak od $\ell_2$; $w$ je na jednoj od dviju uzlaznih grana puta 2, recimo između $x_2$ i $\ell_2$, a $\ell_1$ je predak od $w$ i potomak od $\ell_2$, dakle na istoj grani. Obrat je trivijalan. Provjera „je li $a$ predak od $b$” je $O(1)$ preko Eulerovih vremena $tin/tout$, pa cijela provjera košta dva LCA-a.</p>
'''),
        ('Zašto je ukupna složenost u redu i na što paziti?',
         r'''
<p>Po upitu najviše $4 + 8 \cdot 3 = 28$ provjera presjeka, svaka s dva LCA-a binarnim podizanjem ($O(\log n)$): ukupno $O((n + q)\log n)$. Segment može biti jedan vrh ($u = p$) – formula radi i tada. Stablo gradimo iterativnim DFS-om (lanac od $5 \cdot 10^4$ vrhova može srušiti rekurziju), a dodatne bridove ne stavljamo u stablo.</p>
'''),
    ],
    'tips': [
        r'''„Stablo plus $c$ bridova” s malim $c$: fiksiraj stablo, nabroji podskupove/redoslijede dodatnih bridova ($O(c! \, 2^c)$ kandidata) i svaki provjeri pomoću upita nad stablom.''',
        r'''Presjek dvaju putova u stablu: dublji LCA mora ležati na drugom putu – standardna lema koju vrijedi zapamtiti; „$w$ na putu $x\text{-}y$” $\iff$ $\mathrm{lca}(x,y)$ predak od $w$ i $w$ predak od $x$ ili $y$.''',
        r'''Iterativni DFS ili eksplicitni stog za $n \ge 10^5$ (ovdje $5\cdot 10^4$ lanac) – rekurzija dubine $n$ nije sigurna u svakom okruženju.''',
    ],
    'solution': r'''
<p>Prema službenim rješenjima NAC 2023. Fiksiramo razapinjuće stablo $T$; dva dodatna brida $e_1, e_2$. Svaki jednostavan put koristi svaki dodatni brid najviše jednom, a između njih ide jedinstvenim putem u $T$, pa je kandidata najviše $13$: $1$ (put u stablu) $+ 4$ (jedan brid, dva smjera) $+ 8$ (oba brida, dva redoslijeda, smjerovi). Kandidat je jednostavan put točno kad su njegovi segmenti u stablu u parovima vršno disjunktni. Dva puta $x_1\text{-}y_1$, $x_2\text{-}y_2$ se sijeku točno kad dublji od $\mathrm{lca}(x_1,y_1)$, $\mathrm{lca}(x_2,y_2)$ leži na drugom putu, što provjeravamo Eulerovim vremenima. LCA binarnim podizanjem; $O((n+q)\log n)$.</p>
''',
    'detailed': r'''
<h3>1. Struktura jednostavnih putova</h3>
<p>Neka je $T$ bilo koje razapinjuće stablo grafa (gradimo ga unijom-pronađi pri čitanju: brid koji spaja već povezane vrhove je dodatni). Dodatni bridovi su $e_1 = (a_1, b_1)$ i $e_2 = (a_2, b_2)$. Promotrimo jednostavan put $P$ od $u$ do $v$. Kako ne ponavlja vrhove, ne ponavlja ni bridove, pa svaki dodatni brid koristi najviše jednom. Izbacimo li iz $P$ dodatne bridove, ostaju najviše tri komada; svaki komad je šetnja u stablu $T$ bez ponavljanja vrhova, dakle <em>jedinstveni</em> put u $T$ između svojih krajeva. Zato je $P$ potpuno određen nizom dodatnih bridova koje koristi, njihovim redoslijedom i smjerom prolaska.</p>
<p>Kandidati:</p>
<ul>
<li>bez dodatnih bridova: put $u\text{-}v$ u $T$ (uvijek valjan) – $1$;</li>
<li>jedan brid $(p, r)$ (dva brida, dva smjera): $u \leadsto p \to r \leadsto v$ – $4$;</li>
<li>oba brida: $u \leadsto p \to r \leadsto s \to t \leadsto v$, gdje je $(p,r)$ jedan brid u nekom smjeru, a $(s,t)$ drugi (dva redoslijeda, $2\times 2$ smjera) – $8$.</li>
</ul>
<p>Kandidat je jednostavan put točno kad su njegovi segmenti u stablu ($\leadsto$) u parovima vršno disjunktni: ako jesu, nijedan se vrh ne ponavlja (krajevi dodatnih bridova pripadaju segmentima); ako nisu, neki se vrh ponavlja. Različiti kandidati daju različite putove, pa je odgovor $1 +$ broj valjanih kandidata, najviše $13$.</p>
<h3>2. Presjek dvaju putova u stablu</h3>
<p><strong>Lema.</strong> Neka su $\ell_1 = \mathrm{lca}(x_1,y_1)$, $\ell_2 = \mathrm{lca}(x_2,y_2)$ i $\mathrm{dub}(\ell_1) \ge \mathrm{dub}(\ell_2)$. Putovi $x_1\text{-}y_1$ i $x_2\text{-}y_2$ imaju zajednički vrh točno kad $\ell_1$ leži na putu $x_2\text{-}y_2$.</p>
<p><em>Dokaz.</em> ($\Leftarrow$) $\ell_1$ je na oba puta. ($\Rightarrow$) Neka je $w$ zajednički vrh. Svaki vrh puta $x_1\text{-}y_1$ je potomak od $\ell_1$, pa je $\ell_1$ predak od $w$; isto je $\ell_2$ predak od $w$. Dva pretka istog vrha su usporediva, a $\ell_1$ je dublji, pa je $\ell_1$ potomak od $\ell_2$. Put $x_2\text{-}y_2$ sastoji se od grana $x_2 \nearrow \ell_2$ i $y_2 \nearrow \ell_2$; $w$ je na jednoj od njih, recimo $w$ je predak od $x_2$ i potomak od $\ell_2$. Tada je i $\ell_1$ (predak od $w$, potomak od $\ell_2$) na toj grani. $\square$</p>
<p>Implementacija: „$a$ je predak od $b$” $\iff$ $tin[a] \le tin[b]$ i $tout[b] \le tout[a]$ (Eulerova vremena). Provjera „$\ell_1$ na putu $x_2\text{-}y_2$” je: $\ell_2$ predak od $\ell_1$ i ($\ell_1$ predak od $x_2$ ili od $y_2$). Ukupno dva LCA-a i $O(1)$ dodatnih provjera.</p>
<h3>3. Algoritam</h3>
<ol>
<li>Pročitaj $n+1$ bridova; unijom-pronađi odvoji $n-1$ bridova stabla i $2$ dodatna.</li>
<li>Iterativni DFS iz vrha $1$: dubine, roditelji, $tin/tout$; tablica binarnog podizanja ($\lceil \log_2 n \rceil = 16$ razina).</li>
<li>Za svaki upit $(u,v)$: odgovor $= 1$; za svaki od $4$ kandidata s jednim bridom dodaj $1$ ako se $u\text{-}p$ i $r\text{-}v$ ne sijeku; za svaki od $8$ kandidata s oba brida dodaj $1$ ako se tri segmenta $u\text{-}p$, $r\text{-}s$, $t\text{-}v$ u parovima ne sijeku.</li>
</ol>
<h3>4. Primjer</h3>
<p>Prvi uzorak: stablo $1\text{-}2, 1\text{-}3, 1\text{-}4$, dodatni $2\text{-}3$ i $2\text{-}4$. Upit $(3,4)$: put u stablu $3\text{-}1\text{-}4$. Brid $2\text{-}3$ u smjeru $3 \to 2$: segmenti $\{3\}$ i $2\text{-}1\text{-}4$ su disjunktni – valjan; u smjeru $2 \to 3$: segmenti $3\text{-}1\text{-}2$ i $3\text{-}1\text{-}4$ dijele vrhove $3$ i $1$ – nije. Brid $2\text{-}4$ u smjeru $2 \to 4$: segmenti $3\text{-}1\text{-}2$ i $\{4\}$ – valjan; u smjeru $4 \to 2$: $3\text{-}1\text{-}4$ i $2\text{-}1\text{-}4$ dijele $1$ i $4$ – nije. Oba brida: jedino $3 \to 2 \to 4$ (segmenti $\{3\}, \{2\}, \{4\}$) je valjan. Ukupno $1 + 1 + 1 + 1 = 4$.</p>
<h3>5. Složenost i zamke</h3>
<ul>
<li>Po upitu najviše $4 + 8\cdot 3 = 28$ provjera presjeka po dva LCA-a: $O(q \log n)$, uz $O(n \log n)$ pripreme; na najvećim testovima oko $0.1$ s.</li>
<li>Segment duljine $0$ ($u = p$) je jedan vrh; lema i formula rade bez posebnog slučaja.</li>
<li>Bridovi su zadani kao $a \lt b$, ali dodatne bridove treba probati u <em>oba</em> smjera.</li>
<li>Rekurzivni DFS na lancu od $5\cdot10^4$ vrhova može prekoračiti stog – koristi iterativni DFS ili BFS.</li>
</ul>
''',
    'verified': r'''uzorci 2/2; 300 slučajnih malih testova ($n \le 9$, stabla oblika lanac/zvijezda/duboko/slučajno plus 2 slučajna dodatna brida) protiv brute forcea koji DFS-om nabraja sve jednostavne putove; 3 velika testa s $n = q = 5\cdot10^4$ uključujući lanac (najviše $0.10$ s).''',
},
# ---------------------------------------------------------------- C
{
    'letter': 'C', 'title': 'Broken Minimum Spanning Tree', 'title_hr': 'Pokvareno minimalno razapinjuće stablo', 'slug': 'C_broken_minimum_spanning_tree',
    'tl': '1 s', 'ml': '2 GiB',
    'statement': r'''
<p>Dan je povezan težinski graf (mogu postojati višestruki bridovi) i razapinjuće stablo koje čine prva $n - 1$ brida ulaza, a ne mora biti minimalno. Zamjena brida: ukloni jedan brid stabla i dodaj brid grafa koji nije u stablu; nakon svake zamjene rezultat mora biti razapinjuće stablo. Najmanjim brojem zamjena pretvori stablo u minimalno razapinjuće stablo.</p>
<h3>Ulaz</h3>
<p>$2 \le n \le 2000$, $n - 1 \le m \le 3000$; bridovi $u \ne v$, $1 \le w \le 10^9$, numerirani $1..m$.</p>
<h3>Izlaz</h3>
<p>Broj zamjena $k$, zatim $k$ redaka <code>a b</code> — indeks brida koji se uklanja i brida koji se dodaje. Bilo koji optimalan niz se prihvaća.</p>
<h3>Primjer</h3>
<p>$n = 4$, bridovi $(1,2,10), (2,3,3), (3,4,1), (1,4,4)$: $1$ zamjena, <code>1 4</code>.</p>
''',
    'hints': [
        r'''
<p>Svaka zamjena izbaci točno jedan brid. Ako je $F$ konačno (minimalno) stablo, treba barem $|T \setminus F|$ zamjena. Koje minimalno razapinjuće stablo $F$ minimizira taj broj?</p>
''',
        r'''
<p>Kruskal koji među bridovima jednake težine prvo uzima bridove početnog stabla daje MST $T^*$ s najvećim presjekom s $T$ (pohlepnost na matroidu unutar svake klase težine).</p>
''',
        r'''
<p>Dodaj brid iz $T^* \setminus T$: na nastalom ciklusu sigurno postoji brid koji nije u $T^*$ – njega izbaci. Svaka zamjena povećava $|T \cap T^*|$ za $1$.</p>
''',
    ],
    'coach': [
        ('Koja je očita donja granica za broj zamjena?',
         r'''
<p>Zamjena izbaci jedan brid stabla i doda jedan novi. Ako je konačno stablo $F$, svaki brid iz $T \setminus F$ mora u nekom trenutku biti izbačen, dakle zamjena je barem $|T \setminus F|$. Kako je $F$ nužno neko minimalno razapinjuće stablo, odgovor je barem $\min_{F \text{ MST}} |T \setminus F| = (n-1) - \max_F |T \cap F|$. Postavlja se pitanje koji MST ima najveći presjek s $T$ i može li se ta granica doista dostići.</p>
'''),
        ('Zašto Kruskal s preferencijom bridova stabla daje MST s najvećim presjekom?',
         r'''
<p>Svi MST-ovi imaju isti multiskup težina i, za svaku težinu $w$, isti skup komponenti grafa bridova težine $\lt w$ (standardno svojstvo Kruskala). Bridovi težine $w$ u bilo kojem MST-u tvore razapinjuću šumu multigrafa $G_w$ dobivenog sažimanjem tih komponenti, i obratno: svaki izbor takvih razapinjućih šuma po težinama daje MST. Broj bridova iz $T$ težine $w$ u MST-u je dakle veličina neovisnog skupa u grafičkom matroidu $G_w$ presječenog s $T$; pohlepni algoritam koji prvo uzima bridove iz $T$ (težina $1$) pa ostale (težina $0$) nalazi bazu maksimalne težine – to je točno Kruskal s tim redoslijedom. Zbroj po $w$ daje $\max_F |T \cap F|$.</p>
'''),
        ('Kako dostići donju granicu $|T \setminus T^*|$?',
         r'''
<p>Uzmimo brid $f \in T^* \setminus T_{\text{tren}}$ i dodajmo ga: nastaje točno jedan ciklus, $f$ plus put u stablu između krajeva $f$. Da su svi bridovi tog puta u $T^*$, $T^*$ bi sadržavao ciklus – kontradikcija. Dakle na putu postoji brid $e \notin T^*$; izbacimo ga. Rezultat je opet razapinjuće stablo (uklonili smo brid s ciklusa), $|T_{\text{tren}} \cap T^*|$ je narastao za $1$. Nakon $|T \setminus T^*|$ zamjena stablo je $T^*$.</p>
'''),
        ('Kako to učinkovito implementirati i što provjeriti?',
         r'''
<p>Put u stablu nalazimo DFS-om/BFS-om od jednog kraja $f$ do drugog, pamteći roditeljski brid, pa hodamo natrag i tražimo prvi brid koji nije u $T^*$: $O(n)$ po zamjeni, ukupno $O(n^2)$ uz $O(m \log m)$ za Kruskal – trivijalno za $n \le 2000$. Zbog višestrukih bridova pamtimo <em>indekse</em> bridova, ne parove vrhova. Provjera: broj zamjena jednak je broju bridova stabla koje Kruskal nije uzeo.</p>
'''),
    ],
    'tips': [
        r'''Kad se traži MST „najsličniji” zadanom skupu bridova, dovoljno je u Kruskalu razriješiti izjednačenja u korist tih bridova – svi MST-ovi dijele strukturu po klasama težina.''',
        r'''Zamjena bridova u stablu: dodavanje brida stvara točno jedan ciklus; izbaci s njega bilo koji „nepoželjan” brid i stablo ostaje razapinjuće – osnovni korak mnogih dokaza o razapinjućim stablima.''',
        r'''Brute force za male konstruktivne zadatke: BFS po svim stanjima (ovdje po svim razapinjućim stablima) daje neovisnu provjeru optimalnog broja koraka, a checker provjerava valjanost niza.''',
    ],
    'solution': r'''
<p>Prema službenim rješenjima NAC 2023. Kruskalom, koji među bridovima jednake težine prvo uzima bridove početnog stabla $T$, nađemo MST $T^*$ s najvećim presjekom s $T$. Odgovor je $k = |T \setminus T^*|$: donja granica jer svaka zamjena izbaci jedan brid, a dostiže se ovako: za svaki $f \in T^* \setminus T$ dodamo $f$, na nastalom ciklusu (put u trenutnom stablu) uvijek postoji brid $e \notin T^*$ (inače bi $T^*$ imao ciklus) i njega izbacimo. Put nalazimo DFS-om, $O(n)$ po zamjeni; ukupno $O(m \log m + n^2)$.</p>
''',
    'detailed': r'''
<h3>1. Donja granica</h3>
<p>Zamjena uklanja točno jedan brid stabla. Ako je konačno stablo $F$, svaki brid iz $T \setminus F$ mora biti uklonjen u zasebnoj zamjeni, pa je broj zamjena $\ge |T \setminus F|$. Konačno stablo je minimalno, dakle odgovor je $\ge \min_{F \in \mathcal{M}} |T \setminus F|$, gdje je $\mathcal{M}$ skup svih MST-ova.</p>
<h3>2. MST s najvećim presjekom s $T$</h3>
<p><strong>Lema.</strong> Neka je $T^*$ rezultat Kruskala koji bridove sortira po $(w, [\text{nije u } T])$, tj. među jednakim težinama prvo uzima bridove iz $T$. Tada je $|T \cap T^*| = \max_{F \in \mathcal{M}} |T \cap F|$.</p>
<p><em>Dokaz.</em> Za težinu $w$ neka je $G_{\lt w}$ graf svih bridova težine $\lt w$. Poznato svojstvo: za svaki MST $F$, bridovi $F$ težine $\lt w$ razapinju točno komponente od $G_{\lt w}$ (Kruskal ih spaja redom), a bridovi $F$ težine $w$ tvore razapinjuću šumu multigrafa $G_w$ koji nastaje sažimanjem komponenti $G_{\lt w}$ i dodavanjem bridova težine $w$. Obratno, biramo li za svaku težinu $w$ proizvoljnu razapinjuću šumu $G_w$, dobivamo MST. Zato je $\max_F |T \cap F| = \sum_w \max\{|B \cap T| : B \text{ razapinjuća šuma } G_w\}$. Razapinjuće šume su baze grafičkog matroida od $G_w$; baza s najviše elemenata iz $T$ je baza maksimalne težine za težine $[e \in T]$, a nju nalazi pohlepni algoritam: prvo bridovi iz $T$, zatim ostali, svaki uzet ako ne zatvara ciklus. To je upravo ono što Kruskal s našim redoslijedom radi unutar klase težine $w$ (unija-pronađi u tom trenutku predstavlja točno komponente $G_{\lt w}$ proširene već uzetim bridovima težine $w$). $\square$</p>
<h3>3. Konstrukcija s $|T \setminus T^*|$ zamjena</h3>
<p>Održavamo trenutno stablo $T_{\text{tren}}$ (početno $T$). Dok postoji $f \in T^* \setminus T_{\text{tren}}$:</p>
<ol>
<li>Dodavanjem $f$ nastaje točno jedan ciklus: $f$ i put $P$ u $T_{\text{tren}}$ između krajeva $f$.</li>
<li>Kad bi svi bridovi $P$ bili u $T^*$, ciklus $P + f$ bio bi sadržan u $T^*$ – nemoguće. Dakle postoji $e \in P$, $e \notin T^*$.</li>
<li>Zamjena $(e, f)$: rezultat je razapinjuće stablo (ima $n-1$ bridova i povezan je jer je $e$ uklonjen s ciklusa), $|T_{\text{tren}} \cap T^*|$ raste za $1$, a $|T_{\text{tren}} \setminus T^*|$ pada za $1$.</li>
</ol>
<p>Nakon točno $|T \setminus T^*|$ koraka $T_{\text{tren}} = T^*$, što je MST. Zajedno s donjom granicom to je optimum.</p>
<h3>4. Implementacija</h3>
<ul>
<li>Sortiranje bridova: $O(m \log m)$; unija-pronađi označi bridove koji ulaze u $T^*$.</li>
<li>Trenutno stablo čuvamo kao liste susjednosti s <em>indeksima bridova</em> (višestruki bridovi!). Za zamjenu radimo DFS od $U_f$ do $V_f$ pamteći roditeljski brid, zatim hodamo od $V_f$ natrag i vratimo prvi brid koji nije u $T^*$; $O(n)$.</li>
<li>Ukupno $O(m \log m + n \cdot |T\setminus T^*|) \subseteq O(m \log m + n^2)$, ovdje ispod $0.02$ s.</li>
<li>Ispis je u 1-indeksiranju: $(e+1, f+1)$.</li>
</ul>
<h3>5. Primjer</h3>
<p>Stablo $\{1,2,3\}$ težina $10, 3, 1$; brid $4$ ima težinu $4$. Kruskal: $3\,(1), 2\,(3), 4\,(4)$; brid $1\,(10)$ zatvara ciklus. $T^* = \{2,3,4\}$, $|T \setminus T^*| = 1$. Dodamo brid $4 = (1,4)$: put $1\text{-}2\text{-}3\text{-}4$ sadrži brid $1 \notin T^*$ – zamjena <code>1 4</code>.</p>
<h3>6. Zamke</h3>
<ul>
<li>Jednake težine: bez preferencije bridova iz $T$ Kruskal može odabrati MST s manjim presjekom i dati previše zamjena.</li>
<li>Višestruki bridovi između istih vrhova imaju različite indekse; put u stablu mora pamtiti brid, ne susjeda.</li>
<li>Već optimalno stablo: ispiši $0$.</li>
<li>Težine do $10^9$ – zbrajanje težina (ako ga radite radi provjere) u 64 bita.</li>
</ul>
''',
    'verified': r'''uzorak 1/1; 300 slučajnih malih testova ($n \le 6$, $m \le 8$, male težine s mnogo izjednačenja, višestruki bridovi) uz checker: broj zamjena uspoređen s brute forceom koji BFS-om po svim razapinjućim stablima nalazi najmanji broj zamjena, a niz zamjena provjeren korak po korak (svaki rezultat razapinjuće stablo, konačna težina jednaka težini MST-a); 6 velikih testova ($n = 2000$, $m = 3000$, uključujući sve jednake težine) prošlo checker (valjanost i $k = |T \setminus T^*|$), najviše $0.01$ s.''',
},
# ---------------------------------------------------------------- D
{
    'letter': 'D', 'title': 'Fail Fast', 'title_hr': 'Brzo padni', 'slug': 'D_fail_fast',
    'tl': '4 s', 'ml': '2 GiB',
    'statement': r'''
<p>$n$ automatskih testova izvodi se slijedno; pri prvom padu preostali se ne izvode. Trošak izvođenja je zbroj CPU-vremena svih testova do uključivo prvog palog; ako svi prođu, trošak je $0$. Test $i$ ima vrijeme $c_i$, vjerojatnost prolaska $p_i$ (neovisno) i eventualno jedan test $d_i$ od kojeg ovisi — $d_i$ se mora izvesti prije $i$ (ne nužno neposredno). Nema cikličkih ovisnosti.</p>
<p>Odredi redoslijed testova koji minimizira očekivani trošak.</p>
<h3>Ulaz</h3>
<p>$1 \le n \le 10^5$; za svaki test $c$ ($1 \le c \le 10^6$), $p$ ($0 \lt p \lt 1$, najviše $6$ decimala), $d$ ($0$ = bez ovisnosti).</p>
<h3>Izlaz</h3>
<p>$n$ redaka — indeksi testova redom izvođenja. Prihvaća se svaki redoslijed čiji je očekivani trošak unutar $10^{-6}$ (apsolutno ili relativno) od optimalnog.</p>
<h3>Primjer</h3>
<p>Testovi $(100, 0.5, 0), (200, 0.1, 1), (10, 0.5, 2), (10, 0.9, 0)$: redoslijed $4, 1, 2, 3$.</p>
''',
    'hints': [
        r'''
<p>Bez ovisnosti: usporedi dva susjedna testa $a, b$ – zamjena mijenja očekivani trošak samo kroz njih. Koji uvjet na $(c_a, p_a), (c_b, p_b)$ kaže da $a$ ide prije $b$?</p>
''',
        r'''
<p>Poredak je po omjeru $\rho = c/(1-p)$ rastuće. S ovisnostima: test s najmanjim $\rho$ među preostalima u optimalnom rasporedu ide odmah nakon svoje ovisnosti – ako je ona već izvedena, izvedi ga; inače ga „zalijepi” za roditelja u jednu jedinicu.</p>
''',
        r'''
<p>Jedinica (roditelj $P$ pa dijete $T$) ima $c = c_P + p_P c_T$, $p = p_P p_T$ – i dalje se uspoređuje omjerom $c/(1-p)$. Prioritetni red + unija-pronađi + povezane liste daju $O(n \log n)$.</p>
''',
    ],
    'coach': [
        ('Kako pojednostavniti izraz za očekivani trošak?',
         r'''
<p>Za redoslijed $S$ neka su $C_i = \sum_{j \le i} c_j$ i $P_i = \prod_{j \le i} p_j$. Tada $E(S) = \sum_i C_i P_{i-1}(1-p_i) = \sum_i C_i (P_{i-1} - P_i)$. Abelovom sumacijom to je $\sum_i c_i P_{i-1} - C_n P_n$, a $C_n P_n$ ne ovisi o redoslijedu. Dakle minimiziramo $F(S) = \sum_i c_i P_{i-1}$ – očekivani zbroj troškova testova koji se <em>stvarno izvedu</em>. Ovaj oblik je ugodan jer se spoj dvaju blokova $A$ pa $B$ ponaša kao jedan test: $c_{AB} = c_A + p_A c_B$, $p_{AB} = p_A p_B$.</p>
'''),
        ('Koji je optimalan poredak bez ovisnosti?',
         r'''
<p>Zamjena susjednih $a, b$ mijenja $F$ samo u njihovom doprinosu: $c_a + p_a c_b$ nasuprot $c_b + p_b c_a$ (pomnoženo zajedničkim $P$ ispred). $a$ prije $b$ je bolje točno kad $c_a(1-p_b) \le c_b(1-p_a)$, tj. $\rho_a \le \rho_b$ za $\rho = c/(1-p)$. Kako svaki poredak koji nije sortiran po $\rho$ ima susjedni par u krivom poretku čijom zamjenom trošak ne raste, sortiranje po $\rho$ je optimalno. Ista formula vrijedi i za blokove jer blok ima svoje $(c, p)$.</p>
'''),
        ('Zašto omjer spoja leži između omjera dijelova i zašto je to ključno za ovisnosti?',
         r'''
<p>$1 - p_A p_B = (1 - p_A) + p_A(1 - p_B)$, pa je $\rho_{AB} = \dfrac{c_A + p_A c_B}{(1-p_A) + p_A(1-p_B)}$ medijanta razlomaka $\dfrac{c_A}{1-p_A}$ i $\dfrac{p_A c_B}{p_A(1-p_B)}$, dakle $\min(\rho_A,\rho_B) \le \rho_{AB} \le \max(\rho_A,\rho_B)$. Posljedica: neka je $T$ jedinica s najmanjim $\rho$ među preostalima. U bilo kojem rasporedu blok $B$ između roditelja od $T$ i samog $T$ sastoji se od jedinica s $\rho \ge \rho_T$, pa je $\rho_B \ge \rho_T$; premještanje $T$ ispred $B$ je dopušteno (u $B$ nema potomaka od $T$, roditelj je već prije) i ne povećava trošak. Dakle postoji optimalan raspored u kojem $T$ ide <em>odmah</em> nakon svog roditelja (ili odmah, ako roditelja nema ili je izveden).</p>
'''),
        ('Kako iz te tvrdnje slijedi algoritam i kako ga izvesti u $O(n \log n)$?',
         r'''
<p>Uzmi jedinicu $T$ s najmanjim $\rho$. Ako je njezin roditelj izveden (ili ga nema), izvedi $T$ – ostatak je manji problem istog oblika. Inače spoji $T$ s roditeljskom jedinicom $P$ u jedinicu „$P$ pa $T$” s $c = c_P + p_P c_T$, $p = p_P p_T$; rasporedi nove instance točno odgovaraju rasporedima stare u kojima $T$ slijedi $P$, a među njima postoji optimalan. Implementacija: prioritetni red po $\rho$ s verzijama zapisa (lijeno brisanje), unija-pronađi koji za test vraća korijen jedinice (ovisnost testa $d_i$ prevodi se u jedinicu $\text{nadji}(d_i)$), povezane liste za redoslijed testova u jedinici (spajanje u $O(1)$). Svaki test se spoji najviše jednom, pa je ukupno $O(n \log n)$.</p>
'''),
    ],
    'tips': [
        r'''Kod „izvodi dok prvi ne padne” problema pretvori cilj u očekivani zbroj troškova izvedenih koraka ($\sum c_i P_{i-1}$) – tada se blokovi spajaju kao jedan korak $(c_A + p_A c_B,\ p_A p_B)$.''',
        r'''Poredak po omjeru i ovisnosti u obliku šume: opća shema (Sidney/Horn) – najmanji prioritet ide odmah nakon roditelja, pa ga spoji s roditeljem; uvjet za ispravnost je da prioritet spoja leži između prioriteta dijelova.''',
        r'''Prioritetni red s promjenjivim ključevima: umjesto brisanja spremi verziju zapisa i preskoči zastarjele.''',
        r'''Checker za „bilo koji optimalan redoslijed”: računaj trošak egzaktno razlomcima i dopusti zadanu toleranciju.''',
    ],
    'solution': r'''
<p>Prema službenim rješenjima NAC 2023. $E(S) = \sum_i c_i P_{i-1} - C_n P_n$, pa minimiziramo $F = \sum_i c_i P_{i-1}$. Susjedna zamjena daje poredak po $\rho = c/(1-p)$ rastuće; blok $A$ pa $B$ ponaša se kao test $(c_A + p_A c_B, p_A p_B)$, a $\rho_{AB}$ leži između $\rho_A$ i $\rho_B$. Zato jedinica s najmanjim $\rho$ u nekom optimalnom rasporedu ide odmah nakon svog roditelja: ako je roditelj izveden, izvedi je; inače je spoji s roditeljskom jedinicom i ubaci novi $\rho$. Prioritetni red s lijenim brisanjem, unija-pronađi za pripadnost jedinici i povezane liste za sadržaj jedinice: $O(n \log n)$.</p>
''',
    'detailed': r'''
<h3>1. Preoblikovanje cilja</h3>
<p>Za redoslijed $S = (s_1, \dots, s_n)$ s troškovima $c_i$ i vjerojatnostima prolaska $p_i$ (indeksirano po položaju) neka je $C_i = \sum_{j\le i} c_j$, $P_i = \prod_{j \le i} p_j$, $P_0 = 1$. Prvi pad na položaju $i$ ima vjerojatnost $P_{i-1}(1-p_i)$ i trošak $C_i$; ako svi prođu, trošak je $0$:</p>
$$E(S) = \sum_{i=1}^n C_i (P_{i-1} - P_i) = \sum_{i=1}^n c_i P_{i-1} - C_n P_n .$$
<p>(Abelova sumacija: $\sum_i C_i P_{i-1} - \sum_i C_i P_i$, pa se $C_i P_i$ pokrati s $C_{i+1}P_i$ do na $c_{i+1}P_i$.) Član $C_n P_n$ ne ovisi o redoslijedu, pa minimiziramo $F(S) = \sum_i c_i P_{i-1}$: očekivani zbroj troškova testova koji se izvedu (test $i$ izvodi se s vjerojatnošću $P_{i-1}$).</p>
<h3>2. Blokovi kao testovi</h3>
<p>Za niz testova $A$ definiramo $c_A = F(A)$ (očekivani trošak izvođenja niza) i $p_A = \prod_{i \in A} p_i$. Za spoj $A$ pa $B$: $c_{AB} = c_A + p_A c_B$ (do $B$ dolazimo s vjerojatnošću $p_A$), $p_{AB} = p_A p_B$. Doprinos bloka na položaju iza prefiksa s produktom $P$ je $P \cdot c_{\text{blok}}$. Time se sve tvrdnje o pojedinim testovima prenose na blokove.</p>
<h3>3. Susjedna zamjena i omjer</h3>
<p>Za susjedne blokove $A, B$ iza prefiksa $P$: $A$ pa $B$ daje $P(c_A + p_A c_B)$, $B$ pa $A$ daje $P(c_B + p_B c_A)$, ostatak je nepromijenjen ($P$ iza njih je isti). $A$ prije $B$ nije gore točno kad $c_A(1 - p_B) \le c_B (1 - p_A)$, tj. $\rho_A \le \rho_B$ uz</p>
$$\rho_X = \frac{c_X}{1 - p_X}.$$
<p>Bez ovisnosti: svaki poredak koji nije sortiran po $\rho$ ima susjedni par s $\rho_a \gt \rho_b$; zamjena ne povećava $F$ i smanjuje broj inverzija, pa je sortirani poredak optimalan (izjednačeni omjeri daju jednak trošak).</p>
<h3>4. Lema o medijanti</h3>
<p>$1 - p_A p_B = (1 - p_A) + p_A (1 - p_B)$, pa je</p>
$$\rho_{AB} = \frac{c_A + p_A c_B}{(1 - p_A) + p_A(1 - p_B)},$$
<p>medijanta razlomaka $\frac{c_A}{1-p_A} = \rho_A$ i $\frac{p_A c_B}{p_A(1-p_B)} = \rho_B$ (brojnici i nazivnici se zbrajaju, svi pozitivni), dakle $\min(\rho_A, \rho_B) \le \rho_{AB} \le \max(\rho_A, \rho_B)$. Indukcijom: blok sastavljen od jedinica s $\rho \ge r$ ima $\rho \ge r$.</p>
<h3>5. Ključna tvrdnja</h3>
<p>Ovisnosti tvore šumu (svaki test ima najviše jednog roditelja, nema ciklusa). Radimo s <em>jedinicama</em> – nizovima testova koji se izvode uzastopno; početno je svaki test jedinica, roditelj jedinice je jedinica koja sadrži ovisnost njezina prvog testa.</p>
<p><strong>Tvrdnja.</strong> Neka je $T$ jedinica s najmanjim $\rho$ među preostalima. Postoji optimalan raspored preostalih jedinica u kojem $T$ dolazi odmah nakon svoje roditeljske jedinice (odnosno na sam početak ako roditelja nema ili je već izveden).</p>
<p><em>Dokaz.</em> Uzmimo optimalan raspored i neka je $B$ blok jedinica strogo između roditelja od $T$ (ili početka) i $T$. Sve jedinice u $B$ imaju $\rho \ge \rho_T$, pa po lemi $\rho_B \ge \rho_T$. Raspored $\dots T\, B \dots$ je dopušten: roditelj od $T$ je i dalje prije $T$, a u $B$ nema potomaka od $T$ (oni moraju biti nakon $T$), dok su ovisnosti unutar $B$ i prema van netaknute jer je $B$ pomaknut kao cjelina iza $T$ koji im nije predak. Po odjeljku 3 trošak se ne povećava. $\square$</p>
<h3>6. Algoritam</h3>
<ol>
<li>Prioritetni red jedinica po $\rho$; unija-pronađi $\text{nadji}(x)$ = korijen jedinice koja sadrži test $x$; za svaku jedinicu $(c, p)$, glava/rep povezane liste testova i broj verzije.</li>
<li>Izvadi jedinicu $u$ s najmanjim $\rho$ (preskoči ako nije korijen ili je verzija zastarjela). Roditeljska jedinica je $r = \text{nadji}(d_{u})$, gdje je $d_u$ ovisnost korijenskog testa jedinice ($0$ = nema).</li>
<li>Ako $r$ ne postoji ili je izvedena: izvedi $u$ – ispiši testove njezine liste redom, označi izvedenom.</li>
<li>Inače spoji: $c_r \leftarrow c_r + p_r c_u$, $p_r \leftarrow p_r p_u$, nadoveži listu $u$ na kraj liste $r$, $\text{dsu}[u] \leftarrow r$, povećaj verziju $r$ i ubaci $(\rho_r, r, \text{verzija})$.</li>
</ol>
<p>Korak 4 je opravdan tvrdnjom: rasporedi nove instance (s jedinicom „$r$ pa $u$”) su točno rasporedi stare u kojima $u$ slijedi $r$, a među njima je optimalan. Korak 3 je slučaj „na sam početak”. Svaki test se spaja najviše jednom i svako spajanje/izvođenje ubaci $O(1)$ zapisa u red, pa je složenost $O(n \log n)$; ovdje ispod $0.1$ s za $n = 10^5$.</p>
<h3>7. Primjer</h3>
<p>$\rho$: $t_1 = 100/0.5 = 200$, $t_2 = 200/0.9 \approx 222.2$, $t_3 = 10/0.5 = 20$, $t_4 = 10/0.1 = 100$. Najmanji je $t_3$, roditelj $t_2$ nije izveden – spoj: $c = 200 + 0.1\cdot 10 = 201$, $p = 0.05$, $\rho \approx 211.6$. Zatim $t_4$ ($100$, bez roditelja) – izvedi; $t_1$ ($200$) – izvedi; jedinica $(t_2, t_3)$ – roditelj $t_1$ izveden, izvedi. Redoslijed $4, 1, 2, 3$.</p>
<h3>8. Preciznost i zamke</h3>
<ul>
<li>$0 \lt p \lt 1$ sa $6$ decimala, pa je $1 - p \ge 10^{-6}$; produkti $p$ mogu podbaciti na $0$ u <code>double</code>, ali tada je $\rho = c$ i sve ostaje ispravno. Tolerancija $10^{-6}$ na trošak oprašta izjednačene omjere.</li>
<li>Ovisnost testa prevodi se u <em>jedinicu</em> preko $\text{nadji}(d)$ – roditelj se mogao već spojiti s nečim.</li>
<li>Lijeno brisanje: provjeri i „je li korijen” i verziju, inače se spojena jedinica može izvesti dvaput.</li>
<li>Ispis od $10^5$ redaka – skupljaj u međuspremnik.</li>
</ul>
''',
    'verified': r'''uzorak 1/1; 300 slučajnih malih testova ($n \le 7$, šume/lanci/bez ovisnosti, vjerojatnosti s $1$–$6$ decimala) uz checker koji provjerava permutaciju i ovisnosti te egzaktno (razlomcima) uspoređuje očekivani trošak s optimalnim redoslijedom brute forcea po svim permutacijama; 8 velikih testova ($n = 10^5$: lanac, šuma, zvijezda, bez ovisnosti) prošlo provjeru valjanosti, najviše $0.09$ s.''',
},
# ---------------------------------------------------------------- E
{
    'letter': 'E', 'title': 'First Last', 'title_hr': 'Prvo i zadnje slovo', 'slug': 'E_first_last',
    'tl': '1 s', 'ml': '2 GiB',
    'statement': r'''
<p>Alice i Bob igraju s popisom riječi; Alice bira početnu riječ. Zatim igrač na potezu mora odabrati neiskorištenu riječ koja počinje slovom kojim završava prethodno odabrana riječ. Tko ne može odabrati riječ, gubi. Oba igraju optimalno.</p>
<p>Koliko riječi s popisa, odabranih kao prva, vodi do Aliceine pobjede?</p>
<h3>Ulaz</h3>
<p>$1 \le n \le 1000$ različitih riječi malih slova duljine $2$–$15$. Među svim prvim i posljednjim slovima riječi pojavljuju se najviše $3$ različita slova.</p>
<h3>Izlaz</h3>
<p>Broj pobjedničkih početnih riječi.</p>
<h3>Primjer</h3>
<p><code>attic</code>, <code>climb</code>, <code>alpha</code>: $2$. Popis od $22$ riječi iz zadatka (<code>agora</code>, <code>alpha</code>, …, <code>cynic</code>): $6$.</p>
''',
    'hints': [
        r'''
<p>Od riječi je bitno samo prvo i zadnje slovo: slova su vrhovi (najviše $3$), riječ je usmjereni brid. Igra postaje: igrač u vrhu bira neiskorišten izlazni brid i prelazi u njegov kraj.</p>
''',
        r'''
<p>Dvije petlje na istom vrhu, ili par bridova $u \to v$ i $v \to u$, možemo izbaciti bez promjene ishoda: tko god pobjeđuje bez njih, pobjeđuje i s njima „zrcaljenjem” (na protivnikovu upotrebu odgovori uparenim bridom i vrati isto stanje).</p>
''',
        r'''
<p>Nakon redukcije graf je 3-ciklus s najviše po jednom petljom ili acikličan; iz svakog stanja dostižno je samo $O(n)$ stanja pa memoizirani minimax prolazi.</p>
''',
    ],
    'coach': [
        ('Što je u riječi zaista bitno za igru?',
         r'''
<p>Samo prvo i zadnje slovo: riječ „prenosi” igru s prvog na zadnje slovo, a jedina veza među riječima je uvjet da se slova podudaraju. Zato riječ modeliramo kao usmjereni brid prvo $\to$ zadnje slovo u grafu s najviše $3$ vrha (ograničenje zadatka). Igrač koji je „u vrhu $x$” (prethodna riječ završava na $x$) bira neiskorišten brid iz $x$ i prelazi u njegov kraj; tko nema brida, gubi. Riječi iste klase $(u, v)$ su međusobno zamjenjive, pa je stanje igre: trenutni vrh i $9$ brojeva preostalih bridova.</p>
'''),
        ('Zašto je stanje s $9$ brojača prevelik prostor i kako ga smanjiti bez promjene ishoda?',
         r'''
<p>Brojači idu do $1000$, pa je stanja potencijalno previše. Tražimo redukcije koje čuvaju ishod. <em>Dvije petlje na istom vrhu $v$</em>: neka igrač $W$ pobjeđuje u igri $P'$ bez tih dviju petlji. U igri $P$ s njima $W$ igra po strategiji za $P'$; ako protivnik ikad iskoristi „višak” petlju (kad u simuliranoj igri $P'$ petlje na $v$ više nema), $W$ odgovori drugom višak-petljom: opet smo u $v$, u istom stanju igre $P'$, protivnik na potezu. Višak se troši samo u paru, pa $W$ pobjeđuje i u $P$. <em>Par $u \to v$, $v \to u$</em>: isto zrcaljenje – na protivnikov $u \to v$ odgovor $v \to u$ vraća igru u $u$ u isto stanje. Redukcije primjenjujemo do kraja: petlje ostaju najviše po jedna, a između svaka dva vrha bridovi idu samo u jednom smjeru.</p>
'''),
        ('Kako izgleda reducirani graf i zašto je prostor stanja sada malen?',
         r'''
<p>Na $3$ vrha bez dvosmjernih parova bridovi tvore ili 3-ciklus $0 \to 1 \to 2 \to 0$ ili acikličan graf, plus najviše tri petlje. U acikličnom slučaju partija ima najviše $3$ prijelaza i $3$ petlje – stanja je konstantno mnogo. U ciklusu igrači obilaze krug: nakon $t$ prijelaza brojači $(a, b, c)$ umanjeni su za $\lfloor t/3 \rfloor$ ili $\lceil t/3 \rceil$ ovisno o položaju u krugu, dakle potpuno određeni brojem $t$; jedina sloboda su petlje ($2^3$ stanja) i trenutni vrh. Dostižno je $O(3 \cdot 8 \cdot n)$ stanja, pa memoizirani minimax („pobjeđujem ako postoji potez u gubitničko stanje”) radi trenutno.</p>
'''),
        ('Kako iz vrijednosti stanja dobiti odgovor za Alice?',
         r'''
<p>Alice ne igra „iz vrha” – bira bilo koju riječ $u \to v$. Nakon nje Bob je u vrhu $v$ s tom riječju izbačenom; Alice pobjeđuje točno kad je to stanje gubitničko za igrača na potezu. Riječi iste klase daju isto stanje, pa za svaku klasu $(u,v)$ oduzmemo $1$, reduciramo, pozovemo minimax iz $v$ i, ako je gubitničko, dodamo broj riječi u klasi. Redukcija se primjenjuje <em>nakon</em> uklanjanja Aliceine riječi jer ona mijenja parnost petlje odnosno par $u\!\leftrightarrow\! v$.</p>
'''),
    ],
    'tips': [
        r'''Igre na grafu s malo vrhova i mnogo paralelnih bridova: traži „zrcalne” redukcije (par poteza koji vraća isto stanje) – one čuvaju ishod i drastično smanjuju stanja.''',
        r'''Prije procjene složenosti memoizacije pitaj se koja su stanja <em>dostižna</em>, ne koliko ih ima u kartezijevom produktu.''',
        r'''Brute force za igre: minimax nad bitmaskom preostalih poteza za $n \le 12$ je trivijalan i odlična provjera svake „pametne” redukcije.''',
    ],
    'solution': r'''
<p>Prema službenim rješenjima NAC 2023. Slova su vrhovi (najviše $3$), riječ je brid prvo $\to$ zadnje slovo; igrač u vrhu bira neiskorišten izlazni brid. Dvije petlje na istom vrhu ili par $u\to v$, $v \to u$ smijemo ukloniti bez promjene ishoda (pobjednik reducirane igre zrcali protivnikovu upotrebu viška uparenim bridom). Reducirani graf je 3-ciklus s $\le 1$ petljom po vrhu ili acikličan, pa je iz svakog stanja dostižno $O(n)$ stanja i memoizirani minimax je trenutan. Za svaku klasu riječi $(u,v)$ uklonimo jednu riječ, reduciramo i provjerimo je li stanje u $v$ gubitničko za Boba; zbrajamo veličine takvih klasa. $O(n)$ stanja, praktično $O(n \log n)$ zbog mape.</p>
''',
    'detailed': r'''
<h3>1. Model igre</h3>
<p>Za riječ su bitni samo prvo i zadnje slovo. Neka su $L$ slova koja se pojavljuju na tim pozicijama, $|L| \le 3$; svaka riječ je usmjereni brid $\text{prvo} \to \text{zadnje}$ (petlja ako su jednaka). Stanje igre je par (trenutni vrh $x$, multiskup preostalih bridova $C$) gdje je $C$ matrica $3\times3$ brojača $c_{uv}$; igrač u $x$ bira $y$ s $c_{xy} \gt 0$, smanjuje $c_{xy}$ i predaje vrh $y$ protivniku; bez poteza gubi. Riječi iste klase $(u,v)$ su ekvivalentne.</p>
<h3>2. Redukcije koje čuvaju ishod</h3>
<p><strong>Lema 1.</strong> Ako je $c_{vv} \ge 2$, ishod pozicije $(x, C)$ jednak je ishodu $(x, C')$ gdje $C'$ ima dvije petlje na $v$ manje.</p>
<p><strong>Lema 2.</strong> Ako je $c_{uv} \ge 1$ i $c_{vu} \ge 1$, $u \ne v$, ishod $(x, C)$ jednak je ishodu $(x, C'')$ gdje su $c_{uv}, c_{vu}$ umanjeni za $1$.</p>
<p><em>Dokaz (zrcaljenje).</em> Neka igrač $W$ ima pobjedničku strategiju u reduciranoj igri. U punoj igri $W$ vodi „simuliranu” reduciranu partiju: dok protivnik $L$ igra brid koji postoji i u simuliranoj partiji, $W$ ga tamo odigra i odgovori po strategiji (potez je legalan i u punoj igri jer su puni brojači $\ge$ simuliranim). Ako $L$ odigra brid kojeg u simuliranoj partiji više nema, to je nužno jedan od dva „višak” brida (puni brojači su simulirani plus par viška); $W$ odmah odgovori drugim bridom iz para – petljom na $v$ odnosno bridom $v \to u$ – čime se vraća u isti vrh i isto simulirano stanje, a $L$ je opet na potezu, sada bez viška. Kad $L$ u simuliranoj partiji nema poteza, u punoj ima najviše višak-brid, koji $W$ odzrcali, i $L$ je opet bez poteza. Dakle $W$ pobjeđuje i u punoj igri; kako pobjednik postoji točno jedan, ishodi su jednaki. $\square$</p>
<p>Primjenjujemo leme do kraja: $c_{vv} \leftarrow c_{vv} \bmod 2$ i za $u \lt v$: $m = \min(c_{uv}, c_{vu})$, oba umanjimo za $m$. Potezi u reduciranoj igri ne stvaraju nove parove pa reducirano stanje ostaje reducirano.</p>
<h3>3. Struktura reduciranog grafa i broj stanja</h3>
<p>Između svaka dva od tri vrha bridovi idu samo u jednom smjeru: orijentacija parova ili tvori 3-ciklus $0\to1\to2\to0$ ili je aciklična (tranzitivna). Uz to najviše tri petlje.</p>
<ul>
<li><em>Aciklično:</em> put kroz vrhove ima najviše $3$ prijelaza, uz najviše $3$ petlje – konstantan broj stanja.</li>
<li><em>3-ciklus s brojačima $(a, b, c)$:</em> jedini ne-petlja potezi su „idi dalje po krugu”. Nakon $t$ takvih prijelaza od početnog vrha brojači su jednoznačno određeni s $t$ (svaki brid smanji se za $\lfloor t/3 \rfloor$ ili $\lceil t/3 \rceil$ po položaju), jer se krug obilazi redom. Stanje je dakle (vrh, $t$, koje su petlje potrošene): najviše $3 \cdot (n+1) \cdot 8$ stanja.</li>
</ul>
<p>Zato je memoizirani minimax $\text{win}(x, C) = \exists y:\ c_{xy} \gt 0 \wedge \neg \text{win}(y, C - e_{xy})$ uz mapu $\langle x, C\rangle \mapsto$ ishod dovoljno brz; na $n = 1000$ posjeti reda tisuću stanja.</p>
<h3>4. Odgovor za Alice</h3>
<p>Alice bira riječ $u \to v$; Bob je zatim u $v$ s multiskupom $C - e_{uv}$. Alice tom riječju pobjeđuje točno kad je $\text{win}(v, \mathrm{red}(C - e_{uv}))$ laž. Za svaku od najviše $9$ klasa oduzmemo jedan brid, reduciramo, izračunamo i dodamo $c_{uv}$ ako je stanje gubitničko. Redukcija mora ići <em>nakon</em> oduzimanja Aliceine riječi (mijenja parnost).</p>
<h3>5. Primjer</h3>
<p><code>attic</code> $= a\to c$, <code>climb</code> $= c\to b$, <code>alpha</code> $= a \to a$. Alice <code>attic</code>: Bob u $c$ igra <code>climb</code>, Alice u $b$ nema riječi – gubi. <code>climb</code>: Bob u $b$ nema riječi – Alice pobjeđuje. <code>alpha</code>: Bob u $a$ mora <code>attic</code>, Alice <code>climb</code>, Bob u $b$ gubi. Odgovor $2$.</p>
<h3>6. Zamke</h3>
<ul>
<li>Kad je slova manje od $3$, brojači nedostajućih vrhova su nule – kod radi bez posebnog slučaja.</li>
<li>Petlja se reducira na parnost, ne na nulu: jedna petlja mijenja ishod (npr. <code>alpha</code> gore).</li>
<li>Ne reducirati početni multiskup prije oduzimanja Aliceine riječi, i ne zaboraviti da u istoj klasi sve riječi daju isti ishod (množimo brojem riječi u klasi).</li>
<li>Duljina riječi do $15$ – čitanje u dovoljno velik međuspremnik; bitni su samo prvi i zadnji znak.</li>
</ul>
''',
    'verified': r'''uzorci 2/2; 300 slučajnih malih testova ($n \le 12$, $1$–$3$ slova) protiv brute forcea koji radi potpuni minimax nad bitmaskom preostalih riječi bez redukcija; 3 velika testa s $n = 1000$ (3-ciklus s petljama, slučajno, mnogo petlji), najviše $0.00$ s.''',
},
# ---------------------------------------------------------------- F
{
    'letter': 'F', 'title': 'Four Square', 'title_hr': 'Četiri u kvadrat', 'slug': 'F_four_square',
    'tl': '4 s', 'ml': '2 GiB',
    'statement': r'''
<p>Dana su četiri pravokutna stakla dimenzija $w \times h$. Mogu li se (uz rotacije) složiti u kvadrat bez preklapanja i praznina?</p>
<h3>Ulaz</h3>
<p>Četiri retka $w\ h$, $1 \le w, h \le 1000$.</p>
<h3>Izlaz</h3>
<p>$1$ ako mogu, inače $0$.</p>
<h3>Primjer</h3>
<p>Četiri stakla $1 \times 1$: $1$. Stakla $3 \times 1, 3 \times 3, 2 \times 2, 3 \times 3$: $0$.</p>
''',
    'hints': [
        r'''
<p>Ukupna površina mora biti potpun kvadrat $S^2$ – to odmah određuje stranicu kvadrata. Što još mora vrijediti za pravokutnik u donjem lijevom kutu?</p>
''',
        r'''
<p>Pokušaj nacrtati popločavanje s četiri pravokutnika u kojem nijedan pravac (vodoravan ili okomit) ne prolazi „čisto” kroz cijeli kvadrat, ne presijecajući nijedan pravokutnik. Nećeš uspjeti: takav „vjetrenjača” raspored treba barem pet pravokutnika.</p>
''',
        r'''
<p>Dakle, postoji rez koji dijeli kvadrat na dva pravokutnika, svaki popločan podskupom stakala. Rekurzivno: za svaki podskup (bitmaska) i smjer reza dimenzija dijela slijedi iz njegove površine ($w_1 = P_A / H$ mora biti cijeli broj); jedno staklo odgovara pravokutniku ako se dimenzije poklapaju do rotacije.</p>
''',
    ],
    'coach': [
        ('Što je najjednostavniji nužni uvjet i koliko nam on sužava prostor?',
         r'''
<p>Zbroj površina $P = \sum w_i h_i$ mora biti $S^2$ za cijeli $S$ – inače je odgovor $0$. Ako je kvadrat, stranica $S$ je jedinstveno određena, pa problem postaje: može li se <em>konkretan</em> kvadrat $S \times S$ popločati zadanim staklima. Cjelobrojni korijen računamo bez pogrešaka pomičnog zareza (npr. <code>sqrt</code> pa korekcija za $\pm 1$).</p>
'''),
        ('Zašto ne trebamo razmatrati sve moguće položaje stakala u kvadratu?',
         r'''
<p>Jer svako popločavanje pravokutnika s najviše četiri pravokutnika ima <em>giljotinski rez</em>: pravac koji siječe cijeli pravokutnik i ne presijeca nijednu pločicu. Dokaz za četiri pločice: ako neka pločica dodiruje i lijevu i desnu stranicu (odnosno gornju i donju), pravac uz njegov rub je rez. Inače su pločice u četiri kuta međusobno različite (pločica u dva susjedna kuta bi premostila stranicu, u dva nasuprotna kuta bila bi cijeli kvadrat), dakle sve četiri pločice su kutne. Neka donji lijevi ima dimenzije $a \times b$, donji desni $(S-a) \times b_2$ (na donjoj stranici se moraju sastati, jer treća pločica na donjoj stranici ne postoji), gornji lijevi $c \times (S-b)$ i gornji desni $(S-c) \times (S-b_2)$. Zbroj površina je $S^2 + (a-c)(b-b_2)$, pa iz $= S^2$ slijedi $a = c$ (okomiti rez na $x = a$) ili $b = b_2$ (vodoravni rez na $y = b$). Kontradikcija s pretpostavkom da reza nema. Za tri ili manje pločica argument je isti: ne mogu sva četiri kuta biti pokrivena različitim pločicama, pa neka premošćuje stranicu.</p>
'''),
        ('Kako giljotinski rez pretvoriti u rekurziju i kako znati gdje je rez?',
         r'''
<p>Rez dijeli skup stakala na dva neprazna podskupa $A$ i $B$ i pravokutnik $W \times H$ na dva pravokutnika. Ako je rez okomit, lijevi dio ima visinu $H$ i površinu $P_A$, pa mu je širina nužno $w_1 = P_A / H$ – mora biti cijeli broj u $[1, W-1]$; položaj reza nije slobodan parametar. Analogno za vodoravni rez. Zato je funkcija $\text{može}(W, H, \text{maska})$ jednostavna: za jednu pločicu usporedi dimenzije (do rotacije), inače probaj sve podskupove maske i oba smjera reza. Prije toga provjeri $P_{\text{maska}} = W \cdot H$ – to odmah odbacuje većinu grana.</p>
'''),
        ('Koliko je to posla i gdje su zamke?',
         r'''
<p>Na vrhu ima $7$ podjela skupa od $4$ elementa na dva neprazna podskupa (do zamjene), na sljedećoj razini najviše $3$, i svaki poziv radi $O(1)$: ukupno nekoliko stotina operacija. Zamke: površina do $4 \cdot 10^6$ i umnošci poput $S^2$ stanu u 32 bita, ali korištenje 64-bitnih brojeva ništa ne košta; rotaciju dopuštamo samo pri usporedbi jednog stakla s pravokutnikom; treba paziti da je širina dijela strogo manja od $W$ (obje strane reza neprazne).</p>
'''),
    ],
    'tips': [
        r'''Kod „može li se složiti” zadataka s vrlo malo dijelova traži strukturni teorem koji ograničava oblik rješenja (ovdje: giljotinsko popločavanje), umjesto slijepog pretraživanja položaja.''',
        r'''Najmanje ne-giljotinsko popločavanje pravokutnika pravokutnicima je „vjetrenjača” s $5$ pločica; s $\le 4$ dijela uvijek postoji rez. Dokaz preko zbroja površina četiriju kutnih pločica vrijedi zapamtiti.''',
        r'''U rekurziji nad podskupovima neka dimenzije izvedeš iz površine (jedini stupanj slobode je izbor podskupa i smjera), a provjeru $P_{\text{maska}} = W \cdot H$ stavi na sam početak – to je i ispravnost i rezanje grana.''',
    ],
    'solution': r'''
<p>Prema službenim rješenjima NAC 2023. Ukupna površina mora biti $S^2$; inače $0$. Svako popločavanje pravokutnika s $\le 4$ pravokutnika ima giljotinski rez (pravac koji ne presijeca nijednu pločicu): ako nijedna pločica ne premošćuje kvadrat, sve su četiri pločice kutne, dimenzija $a\times b$, $(S-a)\times b_2$, $c \times (S-b)$, $(S-c)\times(S-b_2)$, a zbroj površina je $S^2 + (a-c)(b-b_2)$, pa je $a = c$ ili $b = b_2$ – rez postoji. Zato rekurzivno: $\text{može}(W,H,\text{maska})$ provjeri $P_{\text{maska}} = WH$, za jedno staklo usporedi dimenzije do rotacije, inače za svaki podskup $A$ maske i oba smjera reza izračuna dimenziju dijela iz površine ($w_1 = P_A/H$ ili $h_1 = P_A/W$, cijeli broj) i rekurzivno provjeri obje strane. Nekoliko stotina operacija.</p>
''',
    'detailed': r'''
<h3>1. Stranica kvadrata</h3>
<p>Ako stakla tvore kvadrat, njegova je površina zbroj površina $P = \sum_{i=1}^4 w_i h_i \le 4\cdot 10^6$, pa stranica mora biti $S = \sqrt{P}$, cijeli broj. Računamo $S = \lfloor \sqrt{P} \rfloor$ (uz korekciju $\pm 1$ zbog zaokruživanja) i ako je $S^2 \ne P$ odgovor je $0$. Primjer 2: $3 + 9 + 4 + 9 = 25 = 5^2$, dakle sam uvjet površine ne odbacuje ovaj slučaj – trebamo pravu provjeru.</p>
<h3>2. Teorem o giljotinskom rezu</h3>
<p><strong>Tvrdnja.</strong> U svakom popločavanju pravokutnika $W \times H$ s najviše četiri pravokutnika postoji pravac paralelan sa stranicom koji dijeli pravokutnik na dva dijela, a ne presijeca unutrašnjost nijedne pločice.</p>
<p><strong>Dokaz.</strong> Ako neka pločica dodiruje i lijevu i desnu stranicu, pravac duž njegova gornjeg (ili donjeg) ruba je traženi rez, osim ako je pločica cijeli pravokutnik (tada je popločavanje trivijalno). Analogno za pločicu koja dodiruje gornju i donju stranicu. Pretpostavimo da takve pločice nema. Pločica u donjem lijevom kutu tada ne dodiruje ni desnu ni gornju stranicu, pa je različita od pločica u ostalim kutovima; isto vrijedi za svaki kut. Dakle postoje četiri <em>različite</em> kutne pločice – s najviše četiri pločice to su sve. Označimo donji lijevi $T_1$ dimenzija $a \times b$ ($a \lt W$, $b \lt H$). Na donjoj stranici, desno od $T_1$, leži neka pločica; ona dodiruje donju stranicu i ne može biti gornja kutna pločica (tada bi premošćivala visinu), pa je to donji desni $T_2$, širine $W - a$, visine $b_2$. Isto tako $T_1$ i gornji lijevi $T_3$ (širine $c$, visine $H - b$) dijele lijevu stranicu, $T_3$ i gornji desni $T_4$ dijele gornju stranicu ($T_4$ širine $W - c$), a $T_2$ i $T_4$ desnu ($T_4$ visine $H - b_2$). Zbroj površina:</p>
<p>$$ab + (W-a)b_2 + c(H-b) + (W-c)(H-b_2) = WH + (a - c)(b - b_2).$$</p>
<p>Budući da pločice točno pokrivaju pravokutnik, zbroj je $WH$, pa je $a = c$ ili $b = b_2$. U prvom slučaju pravac $x = a$ ne presijeca nijednu pločicu ($T_1, T_3$ su lijevo, $T_2, T_4$ desno), u drugom pravac $y = b$. Kontradikcija. $\blacksquare$</p>
<p>Ovo je ujedno razlog zašto najmanja „vjetrenjača” (središnji kvadratić okružen s četiri pravokutnika) ima pet pločica: peta pločica kvari jednakost površina.</p>
<h3>3. Rekurzija nad podskupovima</h3>
<p>Definiramo $\text{može}(W, H, M)$ – može li se pravokutnik $W \times H$ točno popločati staklima iz skupa $M$ (bitmaska od $4$ bita).</p>
<ol>
<li>Ako $P_M \ne W \cdot H$, vrati <em>ne</em> (površine se moraju poklapati).</li>
<li>Ako $|M| = 1$, vrati <em>da</em> točno kad je $(w, h) = (W, H)$ ili $(w, h) = (H, W)$.</li>
<li>Inače po teoremu postoji rez koji stakla dijeli na neprazne skupove $A$ i $B = M \setminus A$. Za okomiti rez lijevi dio ima visinu $H$ i površinu $P_A$, dakle širinu $w_1 = P_A / H$; ako je $H \mid P_A$ i $1 \le w_1 \le W - 1$, provjeri $\text{može}(w_1, H, A) \wedge \text{može}(W - w_1, H, B)$. Za vodoravni rez analogno s $h_1 = P_A / W$. Isprobaj sve $A$ (svaki par $\{A, B\}$ jednom).</li>
</ol>
<p>Ispravnost: ako popločavanje postoji, teorem daje rez, rez određuje $A$ i $B$ te dimenzije dijelova (dimenzija dijela je jednoznačno određena površinom jer je druga dimenzija zajednička), a dijelovi su opet popločavanja s manje pločica – indukcija. Obrnuto, sve što rekurzija prihvati očito se može fizički složiti.</p>
<h3>4. Provjera na primjeru 2</h3>
<p>$S = 5$. Stakla $3\times1, 3\times3, 2\times2, 3\times3$. Rez koji odvaja jedno staklo: dio $5 \times h_1$ s $h_1 = P/5$ – nijedna od površina $3, 9, 4$ nije djeljiva s $5$. Rez koji dijeli $2 + 2$ stakla: površine parova su $12, 7, 12, 13, 18, 13$ – nijedna nije djeljiva s $5$. Nijedan rez ne prolazi, odgovor $0$. (Za primjer 1: $S = 2$, rez na dva dijela $1 \times 2$, svaki od dva stakla $1\times1$ – odgovor $1$.)</p>
<h3>5. Složenost i zamke</h3>
<ul>
<li>Vrh rekurzije ima $7$ podjela, svaka daje pozive s $\le 3$ stakla ($3$ podjele) itd.; ukupno ispod tisuću elementarnih operacija.</li>
<li>Rotacija se dopušta samo pri usporedbi jednog stakla s pravokutnikom; ne treba je „primjenjivati” ranije, jer smjer reza pokriva obje orijentacije.</li>
<li>Uvjet $1 \le w_1 \le W - 1$ (obje strane neprazne) i provjera djeljivosti prije dijeljenja.</li>
<li>Cjelobrojni korijen: <code>sqrt</code> u pomičnom zarezu pa korekcija, ili binarno pretraživanje; ne uspoređivati $\sqrt{P}$ s cijelim brojem izravno.</li>
</ul>
''',
    'verified': r'''uzorci 2/2; 300 slučajnih malih testova (dimenzije $\le 6$; oko $60\%$ slučajeva konstruirano kao slučajno giljotinsko popločavanje kvadrata, dio s jednim namjerno „pokvarenim” staklom iste površine, ostatak nasumično) protiv brute forcea koji backtrackingom fizički slaže stakla u mrežu $S \times S$; 3 velika testa s dimenzijama do $1000$ (<0.01 s).''',
},
# ---------------------------------------------------------------- G
{
    'letter': 'G', 'title': 'Frequent Flier', 'title_hr': 'Česti putnik', 'slug': 'G_frequent_flier',
    'tl': '2 s', 'ml': '2 GiB',
    'statement': r'''
<p>Program nagrađivanja s parametrima $m$ i $k$: u svakom razdoblju od $m$ uzastopnih mjeseci mora se platiti barem $k$ letova (ako ih je manje od $k$, svi se plaćaju); ostali su besplatni. Uvjet vrijedi za sve $m$-mjesečne intervale, uključujući one koji počinju prije prvog leta. Dan je plan letova $f_i$ za sljedećih $n$ mjeseci; odredi najmanji broj letova koje moraš platiti.</p>
<h3>Ulaz</h3>
<p>$1 \le n, m \le 2 \cdot 10^5$, $1 \le k \le 10^9$; zatim $n$ brojeva $1 \le f_i \le 10^9$.</p>
<h3>Izlaz</h3>
<p>Najmanji broj plaćenih letova.</p>
<h3>Primjer</h3>
<p>$m = 3$, $k = 2$, $f = (3, 1, 4, 1, 5, 9, 2, 6)$: $8$.</p>
''',
    'hints': [
        r'''
<p>Zapiši uvjet formalno: za svaki prozor $W$ od $m$ uzastopnih mjeseci, broj plaćenih letova u $W$ mora biti barem $\min(k, F_W)$, gdje je $F_W$ broj letova u $W$. Prozori koji vire izvan $[1, n]$ (i na početku i na kraju!) također se broje – provjeri na primjeru da bez prozora nakon $n$-tog mjeseca ne dobiješ $8$.</p>
''',
        r'''
<p>Obrađuj prozore redom po desnom kraju. Kad prozoru nedostaje plaćenih letova, koji neplaćeni let u prozoru je najbolje platiti – najstariji ili najnoviji?</p>
''',
        r'''
<p>Najnoviji: on pripada svim budućim prozorima kojima pripada i bilo koji stariji let iz istog prozora. Neplaćene letove drži na stogu (mjesec, broj) – vrh stoga je uvijek najnoviji neplaćeni mjesec, a ukupno plaćenih letova u prozoru održavaj kliznim prozorom.</p>
''',
    ],
    'coach': [
        ('Koji su prozori zapravo relevantni i kako glasi uvjet?',
         r'''
<p>Za prozor $W = [l, r]$ označimo $F_W$ ukupan broj letova i $P_W$ broj plaćenih letova u njemu; uvjet je $P_W \ge \min(k, F_W)$. Mjeseci izvan $[1, n]$ imaju $0$ letova, ali prozori koji ih sadrže nisu prazni: zadatak izričito kaže da vrijede prozori koji počinju prije prvog leta, a jednako tako i oni koji završavaju nakon $n$-tog mjeseca (u primjeru prozor $[8, 10]$ sadrži samo $6$ letova 8. mjeseca i zahtijeva $2$ plaćena; bez toga bi odgovor bio $6$, a ne $8$). Dovoljno je promatrati prozore s desnim krajem $r = 1, \dots, n + m - 1$, tj. $[\max(1, r-m+1), \min(n, r)]$.</p>
'''),
        ('Zašto plaćati tek kad smo prisiljeni, i zašto baš najnoviji let?',
         r'''
<p>Plaćeni let je „točka” u vremenu koja pomaže svim prozorima koji je sadrže. Obrađujemo prozore po desnom kraju. Kad prozor $[l, r]$ ima manjak $d = \min(k, F_W) - P_W \gt 0$, moramo dodati $d$ plaćenih letova unutar $[l, r]$. Neplaćeni let u mjesecu $j' \gt j$ (oba u prozoru) pripada svakom <em>budućem</em> prozoru $[l', r']$, $r' \ge r$, kojem pripada let u $j$ (jer $l' \le j \lt j' \le r \le r'$), a prošli prozori su već zadovoljeni. Dakle plaćanje najnovijeg leta nikad nije lošije – to je klasična zamjena kod pokrivanja intervala točkama.</p>
'''),
        ('Kako argument zamjene pretvoriti u dokaz optimalnosti?',
         r'''
<p>Invarijanta: postoji optimalno rješenje $O$ koje sadrži sve letove koje je pohlepni algoritam do sada platio. Kad pohlepni na prozoru $W$ plati skup $A$ od $d$ najnovijih dostupnih letova, $O$ (koje je dopustivo i sadrži prethodne pohlepne odluke) ima u $W$ barem $d$ „svojih” dodatnih letova $B$. Svaki let iz $B \setminus A$ nije među $d$ najnovijih dostupnih, pa je stariji ili jednak svakom letu iz $A \setminus B$. Zamijenimo ih jedan za jedan: prošli prozori ostaju zadovoljeni (sadrže pohlepne letove), budući prozori koji sadrže stariji let sadrže i noviji, trošak je isti. Novo $O$ sadrži $A$, invarijanta vrijedi, a na kraju $|O| \ge |G|$. Pohlepni nikad ne zapne jer je $\min(k, F_W) \le F_W$.</p>
'''),
        ('Koja struktura podataka daje „najnoviji neplaćeni let u prozoru” u amortiziranom $O(1)$?',
         r'''
<p>Stog parova (mjesec, broj neplaćenih). Mjeseci dolaze rastućim redom, pa je vrh stoga uvijek najnoviji mjesec koji ima neplaćenih letova. Ne treba ni izbacivati mjesece koji su izašli iz prozora: ako je manjak $d \gt 0$, u prozoru postoji neplaćeni let, on je na stogu s mjesecom $\ge l$, a vrh je još noviji – dakle vrh je u prozoru. Svako skidanje s vrha ili isprazni mjesec (najviše $n$ puta ukupno) ili je zadnje u tom prozoru (najviše jedno po prozoru), pa je ukupno $O(n + m)$. Broj plaćenih i ukupnih letova u prozoru održavamo kliznim prozorom (dodaj mjesec $r$, oduzmi mjesec $r - m$).</p>
'''),
    ],
    'tips': [
        r'''Uvjete oblika „u svakom intervalu barem $c$ odabranih” rješavaj pohlepno po desnom kraju i biraj najdesnije (najkasnije) elemente – to je isti obrazac kao „najmanje točaka koje probijaju sve intervale”.''',
        r'''Kad zadatak spominje intervale koji „vire” izvan raspona podataka, ručno provjeri na uzorku uključuješ li ih; ovdje bez prozora iza $n$-tog mjeseca odgovor na uzorku ispada $6$ umjesto $8$.''',
        r'''Stog s parovima (pozicija, količina) je dovoljan umjesto multiseta ili segmentnog stabla kad elementi dolaze sortirano i uvijek uzimaš najnoviji – zastarjele elemente na dnu ne moraš ni čistiti ako dokažeš da ih nikad nećeš dotaknuti.''',
    ],
    'solution': r'''
<p>Prema službenim rješenjima NAC 2023. Za prozor $W$ s $F_W$ letova uvjet je $P_W \ge \min(k, F_W)$ plaćenih; relevantni su prozori $[\max(1, r-m+1), \min(n, r)]$ za $r = 1, \dots, n+m-1$ (uključujući one koji vire izvan $[1, n]$). Prozore obrađujemo po desnom kraju, kliznim prozorom držimo $F_W$ i $P_W$; ako je manjak $d = \min(k, F_W) - P_W \gt 0$, platimo $d$ <em>najnovijih</em> neplaćenih letova u prozoru, uzimajući ih s vrha stoga (mjesec, neplaćeno). Optimalnost slijedi argumentom zamjene: noviji let pripada svim budućim prozorima kojima pripada stariji iz istog prozora. Složenost $O(n + m)$, odgovor u 64-bitnom tipu.</p>
''',
    'detailed': r'''
<h3>1. Formalizacija</h3>
<p>Neka je $p_j$ broj plaćenih letova u mjesecu $j$, $0 \le p_j \le f_j$, uz $f_j = 0$ za $j \notin [1, n]$. Za prozor $W = [l, l+m-1]$ označimo $F_W = \sum_{j \in W} f_j$ i $P_W = \sum_{j \in W} p_j$. Uvjet programa: $P_W \ge \min(k, F_W)$ za <em>svaki</em> prozor. Prozori koji ne sijeku $[1, n]$ imaju $F_W = 0$ i trivijalni su; ostali imaju desni kraj $r \in [1, n+m-1]$ i dovoljno je promatrati njihov presjek s $[1, n]$: $[\max(1, r-m+1), \min(n, r)]$. Prozori koji vire izvan podataka nisu formalnost: u primjeru ($m = 3$, $k = 2$) prozor $[8, 10]$ sadrži samo $6$ letova 8. mjeseca i zahtijeva $2$ plaćena, a prozor $[7, 9]$ zahtijeva $2$ plaćena među letovima 7. i 8. mjeseca.</p>
<h3>2. Pohlepni algoritam</h3>
<ol>
<li>Za $r = 1, 2, \dots, n + m - 1$: ako je $r \le n$, dodaj mjesec $r$ u prozor ($F \mathrel{+}= f_r$, na stog stavi $(r, f_r)$); ako je $r - m \ge 1$, izbaci mjesec $r - m$ ($F \mathrel{-}= f_{r-m}$, $P \mathrel{-}= p_{r-m}$).</li>
<li>Izračunaj manjak $d = \min(k, F) - P$. Dok je $d \gt 0$: uzmi vrh stoga $(j, u)$, plati $\min(d, u)$ letova mjeseca $j$ (povećaj $p_j$, $P$ i ukupni odgovor, smanji $d$ i $u$); ako je $u$ palo na $0$, skini vrh.</li>
</ol>
<p>Zašto je vrh stoga uvijek unutar prozora kad je $d \gt 0$? Ako je $d \gt 0$, onda je $P \lt F$, pa u prozoru postoji mjesec $j \ge l$ s neplaćenim letovima; on je na stogu (mjeseci se skidaju tek kad su potpuno plaćeni), a vrh stoga ima mjesec $\ge j \ge l$. Zato zastarjele mjesece na dnu stoga ne treba čistiti. Pohlepni nikad ne zapne jer je $\min(k, F) \le F$: uvijek ima dovoljno letova za platiti.</p>
<h3>3. Dokaz optimalnosti (argument zamjene)</h3>
<p>Gledajmo svaki let kao zaseban „utor” (mjesec $j$ ima $f_j$ utora); rješenje je skup plaćenih utora. Tvrdimo da tijekom algoritma postoji optimalno rješenje $O$ koje sadrži sve utore koje je pohlepni $G$ do tada platio. Na početku je to bilo koje optimalno rješenje. Neka pohlepni na prozoru $W$ (desni kraj $r$) plati skup $A$ od $d$ najnovijih još neplaćenih utora u $W$. Kako je $O \supseteq G$ dopustivo, $O$ sadrži u $W$ barem $\min(k, F_W) = |G \cap W| + d$ utora, dakle skup $B$ od barem $d$ utora izvan $G$. Svaki utor $b \in B \setminus A$ je dostupan (nije u $G$), a nije među $d$ najnovijih dostupnih, pa je njegov mjesec $\le$ mjesecu svakog $a \in A \setminus B$. Zamijenimo redom svaki $a \in A \setminus B$ za neki $b \in B \setminus A$ (ima ih dovoljno jer $|B| \ge |A|$): $O' = O \setminus \{b\} \cup \{a\}$.</p>
<ul>
<li>Trošak je isti, a utori su različiti pa kapaciteti $p_j \le f_j$ vrijede.</li>
<li>Prozori s desnim krajem $\lt r$ su zadovoljeni već samim $G$, a $G \subseteq O'$.</li>
<li>Prozor s desnim krajem $r' \ge r$ koji sadrži $b$ (mjesec $j_b \ge l$) sadrži i $a$, jer je $l' \le j_b \le j_a \le r \le r'$. Ostali prozori nisu izgubili utor.</li>
</ul>
<p>Dakle $O'$ je dopustivo, optimalno i sadrži $G \cup A$. Na kraju algoritma $O \supseteq G$, pa je $|G| \le |O|$, a $G$ je dopustivo po konstrukciji – $G$ je optimalno.</p>
<h3>4. Prolaz kroz primjer</h3>
<p>$m = 3$, $k = 2$, $f = (3,1,4,1,5,9,2,6)$. $r=1$: $[1,1]$, $F=3$, treba $2$: plati $2$ u 1. mjesecu. $r=2,3$: prozori $[1,2],[1,3]$ imaju $P = 2$. $r=4$: $[2,4]$, $P = 0$: plati $1$ u 4. mjesecu (sve), pa $1$ u 3. mjesecu; ukupno $4$. $r=5$: $[3,5]$, $P=2$. $r=6$: $[4,6]$, $P=1$: plati $1$ u 6. mjesecu ($5$). $r=7$: $[5,7]$, $P=1$: plati $1$ u 7. ($6$). $r=8$: $[6,8]$, $P=2$. $r=9$: $[7,8]$, $P=1$: plati $1$ u 8. ($7$). $r=10$: $[8,8]$, $F = 6$, $P = 1$: plati još $1$ ($8$). Odgovor $8$.</p>
<h3>5. Složenost i zamke</h3>
<ul>
<li>Vrijeme $O(n + m)$: svaka iteracija unutarnje petlje ili isprazni jedan mjesec (ukupno $\le n$) ili je posljednja za taj prozor (ukupno $\le n+m-1$). Memorija $O(n)$.</li>
<li>$F_W$ do $2\cdot 10^{14}$ i odgovor do $\sum f_j$ – obavezno 64-bitni tipovi; $k$ do $10^9$ stane u 32 bita, ali $\min(k, F_W)$ računaj u 64 bita.</li>
<li>Petlja mora ići do $r = n + m - 1$, ne do $n$; mjesec $r - m$ izbacuj tek kad je $\ge 1$.</li>
<li>Ne „čisti” stog po lijevom kraju prozora skidanjem s dna – nije potrebno, a pogrešno implementirano može izbaciti mjesece koji su još u prozoru.</li>
</ul>
''',
    'verified': r'''uzorak 1/1; 300 slučajnih malih testova ($n \le 6$, $m \le 5$, $f_i \le 3$, $k$ do $\sum f + 1$) protiv brute forcea koji iscrpno ispituje sve vektore plaćenih letova i sve prozore $r = 1..n+m-1$; 3 velika testa s $n, m$ do $2\cdot 10^5$ i $f_i, k$ do $10^9$ (najviše $0.02$ s).''',
},
# ---------------------------------------------------------------- H
{
    'letter': 'H', 'title': 'Game Show Elimination', 'title_hr': 'Eliminacijski kviz', 'slug': 'H_game_show_elimination',
    'tl': '8 s', 'ml': '2 GiB',
    'statement': r'''
<p>$n$ natjecatelja; natjecatelj $i$ svaki tjedan dobiva rezultat — slučajan realan broj uniformno iz $[i, i + k]$. Natjecatelji se rangiraju po rezultatu; pobjednik tjedna eliminira drugoplasiranog. Nastavlja se dok ne ostane jedan. Konačni rang: zadnji preostali ima rang $1$, predzadnji $2$ itd.</p>
<p>Izračunaj očekivani rang svakog natjecatelja.</p>
<h3>Ulaz</h3>
<p>$2 \le n \le 1000$, $2 \le k \le 10$.</p>
<h3>Izlaz</h3>
<p>$n$ redaka s očekivanim rangovima (greška $\le 10^{-6}$).</p>
<h3>Primjer</h3>
<p>$n = 3$, $k = 2$: $2.109375$, $2.625000$, $1.265625$.</p>
''',
    'hints': [
        r'''
<p>Natjecatelj $i$ sigurno pobjeđuje svakoga s brojem $\le i - k$. Tko onda uopće može biti drugoplasiran ako su $M \gt j$ dva najviša preostala natjecatelja?</p>
''',
        r'''
<p>Samo netko iz $(j-k, j]$ ili $M$. Posljedica: svi natjecatelji $\le j - k$ još su uvijek u igri, pa je stanje potpuno opisano s $j$, maskom prisutnosti za $j-k+1, \dots, j-1$ i razmakom $M - j$ (koji možemo „odrezati” na $k$).</p>
''',
        r'''
<p>Za prijelaze treba razdioba drugoplasiranog za skup od najviše $2k$ ljudi: fiksiraj cijeli dio rezultata svakoga (uniformno među $k$ „kanti”); unutar iste kante svi su poredci jednako vjerojatni. Razdioba ovisi samo o relativnom rasporedu pa je računaj lijeno i pamti.</p>
''',
    ],
    'coach': [
        ('Što se sigurno zna o ishodu usporedbe dvaju natjecatelja koji su daleko po broju?',
         r'''
<p>Rezultat natjecatelja $i$ je u $[i, i+k]$, a natjecatelja $i' \le i - k$ u $[i', i'+k] \subseteq (-\infty, i]$. Dakle $i$ pobjeđuje $i'$ s vjerojatnošću $1$ (izjednačenje ima vjerojatnost $0$). Samo parovi na udaljenosti $\lt k$ mogu se „zamijeniti”, što daje nadu da stanje ne treba pamtiti cijeli podskup preostalih, nego samo lokalnu sliku oko vrha.</p>
'''),
        ('Tko može biti drugoplasiran i što to govori o strukturi skupa preostalih?',
         r'''
<p>Neka su $M \gt j$ dva najviša preostala. Natjecatelj $p \le j - k$ sigurno gubi i od $M$ i od $j$, pa je najbolje treći – nikad ne ispada. Dakle ispada netko iz $(j-k, j] \cup \{M\}$. Kako $j$ (drugi najviši) tijekom igre samo pada, svatko tko je ikad ispao bio je $\gt j' - k \ge j - k$ za tadašnji $j'$. Zaključak: u svakom trenutku su <em>svi</em> natjecatelji $\le j-k$ prisutni, a stanje lanca je trojka $(j, \text{mask}, \text{above})$: maska prisutnosti $k-1$ ljudi $j-k+1..j-1$ i $\text{above} = M - j$.</p>
'''),
        ('Zašto se razmak $M - j \ge k$ ne mora pamtiti točno?',
         r'''
<p>Ako je $M \ge j + k$, $M$ sigurno pobjeđuje svaki tjedan, nikad ne ispada i na kraju dobiva rang $1$. Tko ispada određuje se isključivo među ostalima (pobjednik među njima), neovisno o točnom $M$. Zato u trenutku kad $\text{above}$ prvi put postane $\ge k$ pripišemo $M$-u rang $1$ s vjerojatnošću tog stanja i dalje pamtimo samo $\text{above} = k$. Broj stanja pada s $O(n^2 2^k)$ na $O(n k 2^{k-1})$, oko $5 \cdot 10^6$ za $n = 1000$, $k = 10$.</p>
'''),
        ('Kako za dano stanje izračunati vjerojatnost da je baš osoba $p$ drugoplasirana?',
         r'''
<p>Na drugoplasiranog utječu samo ljudi koji nekoga iz $(j-k, j]$ mogu pobijediti, dakle oni $\gt j - 2k$: maska, $j$, $M$ i do $k-1$ sigurno prisutnih ispod maske. Razdioba ovisi samo o njihovom relativnom rasporedu, pa je ključ $(\text{mask}, \text{above}, \text{brojDolje})$ – najviše $k^2 2^{k-1}$ različitih, računamo ih lijeno. Za skup pozicija: cijeli dio rezultata osobe $i$ je uniforman na $\{i, \dots, i+k-1\}$ („kante”), a unutar iste kante rezultati su i.i.d. uniformni, pa su svi poredci jednako vjerojatni. Osoba $p$ je druga točno kad je (a) u najvišoj nepraznoj kanti s još $x \ge 1$ ljudi (vjerojatnost $1/(x+1)$ da je druga) ili (b) točno je jedna osoba iznad njezine kante, a u njezinoj kanti je još $x$ ljudi (vjerojatnost $1/(x+1)$ da je prva u kanti). Za fiksnu kantu $b$ osobe $p$, DP po ostalima sa stanjem (koliko ih je iznad $b$: $0$ ili $1$; koliko ih je točno u $b$) daje obje vjerojatnosti u $O(t^2)$, $t \le 2k$.</p>
'''),
        ('Kako iz vjerojatnosti stanja dobiti očekivane rangove?',
         r'''
<p>Ako u stanju s $|S|$ preostalih ispada osoba $p$, ona dobiva rang $|S|$ (posljednji koji ostaje ima rang $1$). Zato $E[\text{rang}_p] = \sum_{s} \Pr[s] \cdot \Pr[p \text{ ispada u } s] \cdot |S(s)| + \Pr[p \text{ pobjeđuje}]$. Stanja obrađujemo po padajućem $j$ i padajućoj maski (prijelazi idu samo u takva stanja), propagiramo vjerojatnosti i usput zbrajamo doprinose. Provjera: $\sum_i E[\text{rang}_i] = n(n+1)/2$.</p>
'''),
    ],
    'tips': [
        r'''Kod slučajnih procesa na „skoro sortiranim” ulazima traži tvrdnju oblika „$i$ sigurno pobjeđuje $i-k$” – ona obično sažima stanje na prozor širine $O(k)$ i bitmasku.''',
        r'''Za uniformne rezultate na cjelobrojnim intervalima diskretiziraj cijelim dijelom: unutar iste jedinične kante svi su poredci jednako vjerojatni, pa se poredak dobiva kombinatorički, bez integriranja.''',
        r'''Kad je jedan igrač nepobjediv za sve preostale, njegov identitet više nije bitan – „odreži” parametar stanja na graničnu vrijednost i pripiši mu ishod odmah.''',
        r'''Za očekivane vrijednosti u Markovljevom lancu propagiraj vjerojatnosti stanja unaprijed i zbrajaj doprinose pri svakom prijelazu; suma očekivanih rangova mora biti $n(n+1)/2$ – jeftina provjera.''',
    ],
    'solution': r'''
<p>Prema službenim rješenjima NAC 2023. Natjecatelj $i$ sigurno pobjeđuje svakoga $\le i-k$, pa ako su $M \gt j$ dva najviša preostala, ispada netko iz $(j-k, j] \cup \{M\}$ i svi $\le j-k$ su uvijek prisutni. Stanje: $(j, \text{mask}, \text{above})$ – maska prisutnosti za $j-k+1..j-1$ i $\text{above} = M-j$, odrezano na $k$ (za $M \ge j+k$ $M$ sigurno pobjeđuje pa mu odmah pripišemo rang $1$). Stanja ($O(nk2^{k-1})$) obrađujemo po padajućem $j$ i maski, propagiramo vjerojatnosti; onaj koji ispada iz stanja s $|S|$ preostalih dobiva rang $|S|$. Razdiobu drugoplasiranog za relativni raspored ljudi iz $(j-2k, j] \cup \{M\}$ računamo lijeno i pamtimo po ključu $(\text{mask}, \text{above}, \text{brojDolje})$: cijeli dio rezultata je uniforman na $k$ kanti, unutar kante su svi poredci jednako vjerojatni; DP po ostalima sa stanjem (broj iznad kante $\in\{0,1\}$, broj u kanti) daje $\Pr[p \text{ drugi}]$ u $O(k \cdot t^2)$, $t \le 2k$. Ukupno oko $1$ s za $n = 1000$, $k = 10$.</p>
''',
    'detailed': r'''
<h3>1. Tko može ispasti</h3>
<p>Rezultat natjecatelja $i$ je uniforman na $[i, i+k]$. Za $i' \le i - k$ vrijedi $i' + k \le i$, pa $i$ pobjeđuje $i'$ s vjerojatnošću $1$. Neka su $M \gt j$ dva najviša preostala natjecatelja. Svatko $p \le j - k$ gubi i od $j$ i od $M$, dakle nije ni prvi ni drugi. <strong>Ispada uvijek netko iz $(j-k, j] \cup \{M\}$.</strong></p>
<p><strong>Posljedica.</strong> Drugi najviši preostali $j$ tijekom igre nikad ne raste (ispadanjem $M$ ili $j$ postaje sljedeći niži; ispadanjem nekog iz maske ostaje isti). Ako je natjecatelj $p$ ispao dok je drugi najviši bio $j' \ge j$, onda $p \gt j' - k \ge j - k$. Dakle u svakom trenutku su svi natjecatelji $\le j - k$ prisutni. Skup preostalih je stoga u potpunosti opisan trojkom</p>
<ul>
<li>$j$ – drugi najviši preostali,</li>
<li>$\text{mask}$ – $k-1$ bitova prisutnosti natjecatelja $j-k+1, \dots, j-1$ (pozicije $\le 0$ su uvijek $0$),</li>
<li>$\text{above} = M - j \ge 1$.</li>
</ul>
<p>Broj preostalih je $|S| = \max(0, j-k) + \text{popcount}(\text{mask}) + 2$.</p>
<h3>2. Rezanje razmaka</h3>
<p>Ako je $\text{above} \ge k$, $M$ sigurno pobjeđuje svaki tjedan i nikad ne ispada – na kraju dobiva rang $1$. Ostali ispadaju redoslijedom koji ne ovisi o točnoj vrijednosti $M$ (ispada pobjednik među ostalima). Zato: pri prijelazu u stanje s $\text{above}' \ge k$ dodamo $E[\text{rang}_{M}] \mathrel{+}= \Pr$, a stanje spremimo s $\text{above}' = k$ i u njemu $M$-u dajemo vjerojatnost ispadanja $0$. Broj stanja je tada $n \cdot k \cdot 2^{k-1} \le 5.12 \cdot 10^6$.</p>
<h3>3. Prijelazi</h3>
<p>Iz stanja $(j, \text{mask}, \text{above})$ s vjerojatnošću $\Pr[s]$ i razdiobom $q_p = \Pr[p \text{ drugi} \mid s]$:</p>
<ol>
<li>Ispada $p$ iz maske: $E[\text{rang}_p] \mathrel{+}= \Pr[s]\, q_p\, |S|$; novo stanje $(j, \text{mask} \setminus p, \text{above})$.</li>
<li>Ispada $j$ ili $M$: rang jednako; ako je $|S| = 2$, preostali dobiva rang $1$ (osim ako je $M$ odrezan – njemu je već pripisan). Inače novi drugi najviši je $j' = $ najviši bit maske ili, ako je maska prazna, $j - k$; $d = j - j'$. Nova maska je stara pomaknuta za $d$ ulijevo, uz $d$ novih donjih bitova postavljenih za pozicije $\ge 1$ (to su ljudi iz sloja $\le j-k$, sigurno prisutni). Novi razmak: $\text{above} + d$ ako je ispao $j$ (tada $M$ ostaje), odnosno $d$ ako je ispao $M$ (novi vrh je $j$). Ako je novi razmak $\ge k$, primijeni rezanje iz odjeljka 2.</li>
</ol>
<p>Prijelazi idu u stanja s manjim $j$ ili istim $j$ i manjom maskom, pa je dovoljno obrađivati $j$ od $n-1$ prema $1$, a maske silazno. Početno stanje: $j = n-1$, $\text{above} = 1$, maska = svi postojeći. Ukupno najviše $(k+1)$ prijelaza po stanju, oko $5 \cdot 10^7$.</p>
<h3>4. Razdioba drugoplasiranog</h3>
<p>Tko je drugi ovisi o svima koji mogu pobijediti nekoga iz $(j-k, j]$, tj. o ljudima $\gt j - 2k$: maska, $j$, $M$ i do $k-1$ sigurno prisutnih $j-2k+2, \dots, j-k$ (postoje li, ovisi o $j$: $\text{brojDolje} = \min(k-1, \max(0, j-k))$). Razdioba ovisi samo o relativnom rasporedu, pa je pamtimo po ključu $(\text{mask}, \text{above}, \text{brojDolje})$ – najviše $k^2 2^{k-1} = 51\,200$ ključeva, računa se lijeno.</p>
<p><strong>Kante.</strong> Cijeli dio rezultata osobe na poziciji $i$ je uniforman na $\{i, \dots, i+k-1\}$, svaka kanta s vjerojatnošću $1/k$. Uvjetno na kante, ljudi u različitim kantama poredani su po kanti, a rezultati unutar iste kante su nezavisni i uniformni na istom intervalu, pa su svi poredci unutar kante jednako vjerojatni. Osoba $p$ je drugoplasirana točno u dva slučaja:</p>
<ul>
<li>(a) $p$ je u najvišoj nepraznoj kanti zajedno s još $x \ge 1$ ljudi: vjerojatnost da je druga među njima je $1/(x+1)$;</li>
<li>(b) iznad kante osobe $p$ je točno jedna osoba, a u kanti osobe $p$ je još $x \ge 0$ ljudi: $p$ je druga ako je prva u svojoj kanti, vjerojatnost $1/(x+1)$.</li>
</ul>
<p>Za fiksnu kantu $b$ osobe $p$ ($\Pr = 1/k$) radimo DP po ostalim osobama $r$ sa stanjem $(a, x)$: $a \in \{0, 1\}$ broj osoba iznad $b$ (stanje $a = 2$ odbacujemo), $x$ broj osoba točno u $b$. Za osobu $r$ na poziciji $i$: $\Pr[\text{iznad}] = \max(0, \min(k, i+k-1-b))/k$, $\Pr[\text{u } b] = [i \le b \le i+k-1]/k$, $\Pr[\text{ispod}] = \max(0, \min(k, b - i))/k$. Na kraju $\Pr[p \text{ drugi}] = \frac1k \sum_b \left( \sum_{x \ge 1} \frac{dp_0[x]}{x+1} + \sum_{x \ge 0} \frac{dp_1[x]}{x+1} \right)$. Složenost po ključu $O(k \cdot t^2)$ po kandidatu, $t \le 2k$, kandidata najviše $k+1$; sve zajedno ispod $0.5$ s jer je dostižnih ključeva mnogo manje od maksimuma.</p>
<h3>5. Provjera na primjeru</h3>
<p>$n = 3$, $k = 2$: rezultati $X_1, X_2, X_3$ uniformni na $[1,3], [2,4], [3,5]$. Početno stanje $(j=2, \text{mask}=\{1\}, \text{above}=1)$, $|S| = 3$. Osoba $3$ je druga točno kad je $X_2 \gt X_3$ (osoba $1$ je nikad ne pobjeđuje jer $X_1 \le 3 \le X_3$): oba rezultata moraju biti u $[3,4]$ i $X_2$ veći, $\Pr = \frac12 \cdot \frac12 \cdot \frac12 = \frac18$. Isto tako osoba $1$ je druga točno kad $X_1 \gt X_2$, $\Pr = \frac18$; osoba $2$ s $\frac34$. Ako ispadne $2$, ostaju $\{1, 3\}$ i $3$ sigurno pobjeđuje; ako ispadne $1$, u $\{2, 3\}$ osoba $3$ ispada (rang $2$) s $\Pr[X_2 \gt X_3] = \frac18$. Dakle $E[\text{rang}_3] = 3 \cdot \frac18 + \frac34 \cdot 1 + \frac18\left(2 \cdot \frac18 + 1 \cdot \frac78\right) = 1.265625$. Provjera: $2.109375 + 2.625 + 1.265625 = 6 = n(n+1)/2$.</p>
<h3>6. Zamke</h3>
<ul>
<li>Bit maske za poziciju $\le 0$ mora biti $0$ (mali $n$ ili $j \lt k$); $\text{brojDolje}$ također ovisi o postojanju ljudi.</li>
<li>Ne pripisati rang $1$ dvaput: nakon rezanja, u stanju $|S| = 2$ preostali $M$ više ne dobiva ništa.</li>
<li>U slučaju (a) treba $x \ge 1$ – $p$ sam u najvišoj kanti je pobjednik, ne drugi.</li>
<li>Memorija: $n k 2^{k-1}$ double-ova $\approx 41$ MB; ispis s barem $7$ decimala.</li>
</ul>
''',
    'verified': r'''uzorak 1/1; 300 slučajnih malih testova ($n \le 7$, $k \le 10$) protiv egzaktnog brute forcea (Markovljev lanac po svim podskupovima; vjerojatnost drugoplasiranog računa neovisno o kantama, integriranjem umnoška po dijelovima linearnih funkcija razdiobe u racionalnoj aritmetici), dodatno ručno $n \le 12$, $k \le 4$; usporedba checkerom s greškom $10^{-6}$; 3 velika testa s $n \approx 1000$, $k = 10$ (najviše $1.3$ s, ograničenje $8$ s).''',
},
# ---------------------------------------------------------------- I
{
    'letter': 'I', 'title': 'Power of Divisors', 'title_hr': 'Potencija broja djelitelja', 'slug': 'I_power_of_divisors',
    'tl': '1 s', 'ml': '2 GiB',
    'statement': r'''
<p>Neka je $f(n)$ broj pozitivnih djelitelja od $n$ (npr. $f(8) = 4$). Za dani $x$ nađi najmanji $n$ takav da je $n^{f(n)} = x$.</p>
<h3>Ulaz</h3>
<p>$1 \le x \le 10^{18}$.</p>
<h3>Izlaz</h3>
<p>Najmanji $n$ ili $-1$ ako ne postoji.</p>
<h3>Primjer</h3>
<p>$x = 15625 \to 25$; $x = 64000000 \to 20$; $x = 65536 \to -1$.</p>
''',
    'hints': [
        r'''
<p>Ne traži $n$ izravno – traži $f(n)$. Ako je $n^{f(n)} = x$, što to govori o $x$ kao potenciji?</p>
''',
        r'''
<p>$x$ mora biti točna $f(n)$-ta potencija. Za $n \ge 2$ je $f(n) \ge 2$, pa je $n^{f(n)} \ge 2^{f(n)}$: koliko najviše može biti $f(n)$ ako je $x \le 10^{18}$?</p>
''',
        r'''
<p>Za svaki $\tau \in \{2,\dots,60\}$ izračunaj cjelobrojni $\tau$-ti korijen $n$ od $x$ (binarno pretraživanje s množenjem koje ne prelijeva), provjeri $n^\tau = x$ i $f(n) = \tau$ probnim dijeljenjem, te uzmi najmanji takav $n$.</p>
''',
    ],
    'coach': [
        ('Koja je nepoznanica „manja”: $n$ ili eksponent $f(n)$?',
         r'''
<p>Eksponent. $n$ može biti do $10^9$, ali eksponent $\tau = f(n)$ je za $n \ge 2$ barem $2$, a $n^\tau \le 10^{18}$ daje $2^\tau \le 10^{18}$, dakle $\tau \le 59$. Zato fiksiramo $\tau$ (najviše $60$ kandidata) i iz njega izvedemo $n$.</p>
'''),
        ('Kad je $\tau$ fiksiran, koliko je kandidata za $n$?',
         r'''
<p>Točno jedan: $n$ mora biti cjelobrojni $\tau$-ti korijen od $x$, tj. $n = \sqrt[\tau]{x}$, a to postoji samo ako je $x$ točna $\tau$-ta potencija. Korijen nađemo binarnim pretraživanjem po $n \in [1, 2\cdot 10^9]$ uz „zasićeno” množenje (ako međurezultat premaši $2\cdot 10^{18}$, prekinemo) – tako izbjegavamo prelijevanje i ne oslanjamo se na <code>pow</code> u pomičnom zarezu.</p>
'''),
        ('Je li dovoljno da je $x = n^\tau$?',
         r'''
<p>Nije – još treba $f(n) = \tau$, jer inače $n^{f(n)} \ne x$. Broj djelitelja računamo probnim dijeljenjem do $\sqrt{n}$; najgori slučaj je $\tau = 2$ s $n \approx 10^9$, dakle oko $3\cdot 10^4$ dijeljenja – trivijalno.</p>
'''),
        ('Kako među više valjanih $\tau$ odabrati najmanji $n$ i koji su rubni slučajevi?',
         r'''
<p>Različiti $\tau$ daju različite $n$ (veći $\tau$ daje manji korijen), pa jednostavno pamtimo minimum svih $n$ koji prolaze obje provjere. Rubni slučaj $x = 1$: $n = 1$ jer $f(1) = 1$ i $1^1 = 1$; za $x \ge 2$ kandidat $n = 1$ nikad ne prolazi, a $\tau = 1$ bi zahtijevao $n = x$ s $f(x) = 1$, što vrijedi samo za $x = 1$.</p>
'''),
    ],
    'tips': [
        r'''Kad je u jednadžbi nepoznanica i u bazi i u eksponentu, fiksiraj onu s <em>malim</em> rasponom (eksponent je ograničen logaritmom) i drugu izvedi.''',
        r'''Cjelobrojne korijene velikih brojeva računaj binarnim pretraživanjem sa „zasićenim” množenjem ili u <code>__int128</code>; <code>pow</code>/<code>cbrt</code> u pomičnom zarezu treba barem provjeriti za $\pm 1$.''',
        r'''Uvijek zapiši rubne slučajeve poput $x = 1$ ili $n = 1$ prije nego što napišeš glavnu petlju – u ovakvim zadacima to su najčešći uzroci pogrešnog odgovora.''',
    ],
    'solution': r'''
<p>Prema službenim rješenjima NAC 2023. Ako je $n^{f(n)} = x$, onda je $x$ točna $\tau$-ta potencija za $\tau = f(n)$. Za $n \ge 2$ vrijedi $\tau \ge 2$ i $2^\tau \le n^\tau = x \le 10^{18}$, pa je $\tau \le 59$. Za svaki $\tau \in \{2,\dots,60\}$ binarnim pretraživanjem (množenje sa zaštitom od prelijevanja) nađemo $n = \lfloor \sqrt[\tau]{x} \rfloor$, provjerimo $n^\tau = x$ i probnim dijeljenjem $f(n) = \tau$, te ispišemo najmanji takav $n$; ako nijedan ne prolazi, $-1$. Poseban slučaj $x = 1 \to n = 1$. Složenost $O(60\cdot(\log x \cdot 60 + \sqrt{n}))$, zanemarivo.</p>
''',
    'detailed': r'''
<h3>1. Preokret: fiksiramo eksponent</h3>
<p>Jednadžba $n^{f(n)} = x$ ima nepoznanicu i u bazi i u eksponentu, ali eksponent je „mali”. Neka je $\tau = f(n)$. Za $n = 1$ je $\tau = 1$ i $x = 1$. Za $n \ge 2$ broj $n$ ima barem djelitelje $1$ i $n$, pa je $\tau \ge 2$; tada je $x = n^\tau \ge 2^\tau$, a iz $x \le 10^{18} < 2^{60}$ slijedi $\tau \le 59$. Dakle postoji najviše $58$ mogućih eksponenata i možemo ih sve probati.</p>
<h3>2. Za fiksni $\tau$ postoji najviše jedan $n$</h3>
<p>Funkcija $n \mapsto n^\tau$ je strogo rastuća, pa je $n$ jedinstveno određen kao $\sqrt[\tau]{x}$ i mora biti cijeli broj. Računamo $r = \max\{n : n^\tau \le x\}$ binarnim pretraživanjem na $[1, 2\cdot 10^9]$ (za $\tau \ge 2$ korijen je $\le 10^9$) i provjerimo $r^\tau = x$. Potenciju računamo u petlji s <em>zasićenjem</em>: prije množenja provjerimo <code>r &gt; LIMIT / n</code> i tada vratimo „preveliko” – tako nikad ne prelijevamo 64-bitni broj. To je pouzdanije od <code>pow(x, 1.0/tau)</code>, koji za $x \approx 10^{18}$ ima grešku zaokruživanja i lako promaši za $1$.</p>
<h3>3. Provjera broja djelitelja</h3>
<p>Kandidat $n = r$ vrijedi samo ako je stvarno $f(n) = \tau$ – inače je $n^{f(n)} \ne x$. Broj djelitelja računamo iz faktorizacije probnim dijeljenjem do $\sqrt{n}$: $f(n) = \prod (e_i + 1)$. Najveći $n$ nastaje za $\tau = 2$, $n \le 10^9$, dakle najviše $\approx 31623$ koraka; za sve $\tau$ zajedno to je i dalje daleko ispod milisekunde.</p>
<h3>4. Najmanji $n$ i točnost</h3>
<p>Ako više eksponenata prolazi obje provjere, tražimo najmanji $n$. (Zapravo je $n = x^{1/\tau}$ strogo padajuće u $\tau$, pa bi bilo dovoljno uzeti najveći valjani $\tau$, ali čuvanje minimuma je jednostavnije i jednako brzo.) Algoritam je točan jer <em>svaki</em> $n$ koji zadovoljava $n^{f(n)} = x$ nužno ima $\tau = f(n) \in [2, 59]$ i bit će pronađen upravo pri tom $\tau$; obrnuto, sve što ispišemo prolazi izravnu provjeru $n^\tau = x$, $f(n) = \tau$.</p>
<h3>5. Rubni slučajevi</h3>
<ul>
<li>$x = 1$: odgovor $1$ ($1^{f(1)} = 1^1 = 1$). Petlja za $\tau \ge 2$ bi vratila $r = 1$, što odbacujemo jer $f(1) = 1 \ne \tau$; zato $x = 1$ obrađujemo posebno.</li>
<li>$x$ prost ili nije potencija: nijedan $\tau$ ne prolazi, ispisujemo $-1$.</li>
<li>$x = 65536 = 2^{16} = 4^8 = 16^4 = 256^2$: $f(2)=2$, $f(4)=3$, $f(16)=5$, $f(256)=9$ – ništa ne odgovara eksponentu, dakle $-1$, kao u primjeru.</li>
<li>$x = 10^{18} = 100^9$ i $f(100) = 9$: odgovor $100$.</li>
</ul>
<h3>6. Složenost</h3>
<p>$O\big(60 \cdot (60 \log x + \sqrt{x^{1/2}})\big) \approx O(10^5)$ operacija; memorija $O(1)$.</p>
''',
    'verified': r'''uzorci 3/3; 300 slučajnih malih testova ($x \le 3\cdot 10^6$, uključujući točne potencije $n^{f(n)}$ i „lažne” potencije) protiv brute forcea koji iscrpno računa $n^{f(n)}$ za $n \le \sqrt{x}$; 3 velika testa s $x \le 10^{18}$ (<0.01 s), ručno provjereni $x = 1$ i $x = 10^{18}$.''',
},
# ---------------------------------------------------------------- J
{
    'letter': 'J', 'title': 'Repetitive String Invention', 'title_hr': 'Izum ponavljajućeg niza', 'slug': 'J_repetitive_string_invention',
    'tl': '2 s', 'ml': '2 GiB',
    'statement': r'''
<p>String je <em>ponavljajući</em> ako je parne duljine i prva mu je polovica jednaka drugoj (<code>lulu</code>, <code>abcabc</code>, <code>xx</code>). Lulu bira dva neprazna podstringa svog stringa $s$ koji se ne preklapaju i spaja ih redom kojim se pojavljuju u $s$.</p>
<p>Na koliko načina (parovi pozicija podstringova) dobiva ponavljajući string? Za <code>aaaa</code>: $6$ načina za <code>aa</code> i $3$ za <code>aaaa</code>, ukupno $9$.</p>
<h3>Ulaz</h3>
<p>String $s$, $1 \le |s| \le 800$, mala engleska slova.</p>
<h3>Izlaz</h3>
<p>Broj načina.</p>
<h3>Primjer</h3>
<p><code>aaaa</code> $\to 9$; <code>axabxbcxcdxd</code> $\to 22$.</p>
''',
    'hints': [
        r'''
<p>Neka je spoj $T = XY$ s $|X| \ne |Y|$ i $T = WW$. Napiši što jednakost polovica znači za duži od dva podstringa: kakav oblik mora imati?</p>
''',
        r'''
<p>Duži podstring je oblika $ABA$, a kraći je točno $B$ (u oba redoslijeda). Slučaj $|X| = |Y|$ znači jednostavno $X = Y$.</p>
''',
        r'''
<p>Tablica $\mathrm{lcp}[i][j]$ (najdulji zajednički prefiks sufiksa) u $O(n^2)$ omogućuje $O(1)$ usporedbu podstringova. Fiksiraj $B = s[a..b]$ unutar dužeg podstringa, prefiksnim sumama prebroji početke kopija $B$, pa prođi po početku dužeg podstringa – $O(n^3)$ s vrlo malom konstantom.</p>
''',
    ],
    'coach': [
        ('Kako iz $XY = WW$ izgleda struktura podstringova kad su duljine jednake, a kako kad nisu?',
         r'''
<p>Neka je $|X| = L_1$, $|Y| = L_2$, $L_1 + L_2 = 2h$. Ako je $L_1 = L_2 = h$, polovice su točno $X$ i $Y$, pa je uvjet $X = Y$. Ako je $L_1 \gt L_2$, prva polovica je $X[0..h-1]$, a druga je $X[h..L_1-1]$ spojeno s $Y$. Jednakost polovica daje $X[0..L_1-h-1] = X[h..L_1-1] =: A$ i $X[L_1-h..h-1] = Y$. Dakle $X = A\,Y\,A$ s $|A| = L_1 - h = (L_1-L_2)/2 \ge 1$. Ako je $L_1 \lt L_2$, potpuno simetrično dobivamo $Y = A\,X\,A$. Zaključak: kraći podstring je $B$, a duži $ABA$ – to je cijela kombinatorika zadatka.</p>
'''),
        ('Kako prebrojati parove jednake duljine bez ponavljanja?',
         r'''
<p>Par je određen početcima $a \lt c$ i duljinom $h$; uvjeti su $s[a..a+h-1] = s[c..c+h-1]$ i nepreklapanje $a + h \le c$. Prvi uvjet je $h \le \mathrm{lcp}[a][c]$, drugi $h \le c - a$, pa je za fiksni par početaka broj valjanih duljina $\min(\mathrm{lcp}[a][c],\, c-a)$. Zbrajanjem po svim parovima dobivamo $O(n^2)$ rješenje ovog dijela, a tablica $\mathrm{lcp}$ računa se rekurzijom $\mathrm{lcp}[i][j] = [s_i = s_j]\,(1 + \mathrm{lcp}[i+1][j+1])$ unatrag.</p>
'''),
        ('Što fiksirati u slučaju $ABA$ + $B$ da svaki par pozicija prebrojimo točno jednom?',
         r'''
<p>Par pozicija (duži podstring $[d, e]$, kraći $[c, c+|B|-1]$) jednoznačno određuje $|A| = (|\text{duži}| - |\text{kraći}|)/2$, a time i položaj $B$ unutar dužeg: $[a, b] = [d + |A|, e - |A|]$. Obrnuto, trojka $(a, b, d)$ određuje $|A| = a - d$, $e = b + |A|$ i traži $c$ – dakle bijekcija, nema dvostrukog brojanja. Fiksiramo $B = s[a..b]$ i početak $d \lt a$ dužeg podstringa; uvjet $s[d..a-1] = s[b+1..e]$ je $\mathrm{lcp}[d][b+1] \ge a - d$, a $e \le n - 1$ ograničava $d$.</p>
'''),
        ('Kako za fiksne $(a, b, d)$ u $O(1)$ prebrojati moguće položaje kraćeg podstringa?',
         r'''
<p>Kraći podstring je kopija $B$ na početku $c$: $\mathrm{lcp}[a][c] \ge |B|$. Za fiksni $(a, b)$ napravimo prefiksne sume $\mathrm{pre}[c] = \#\{c' \lt c : \mathrm{lcp}[a][c'] \ge |B|\}$ u $O(n)$. Kad je duži prvi, kraći mora početi iza $e$: $\mathrm{pre}[n] - \mathrm{pre}[e+1]$. Kad je kraći prvi, mora završiti prije $d$: $c \le d - |B|$, tj. $\mathrm{pre}[d - |B| + 1]$. Prolaz po svim $(a, b)$ i $d$ daje $O(n^3)$ s oko $n^3/6$ koraka unutarnje petlje plus $n^3/2$ za prefiksne sume – za $n = 800$ ispod $0.2$ s.</p>
'''),
    ],
    'tips': [
        r'''Kad se spoj dvaju stringova mora podudarati sa samim sobom pomaknuto, zapiši jednakost po dijelovima (crtež s dvije trake) – iz toga gotovo uvijek ispadne struktura tipa $ABA$, $AB=BA$ ili periodičnost.''',
        r'''Za $n \le 1000$ tablica $\mathrm{lcp}[i][j]$ svih parova sufiksa ($O(n^2)$ memorije i vremena, jednostavna rekurzija unatrag) zamjenjuje hashiranje i sufiksne strukture i daje $O(1)$ usporedbu bilo kojih dvaju podstringova.''',
        r'''Kod brojanja parova objekata odaberi parametrizaciju koja je bijekcija s onim što brojiš (ovdje $(a, b, d)$ + prebrojani $c$) i eksplicitno provjeri da slučajevi ne preklapaju (jednake vs. različite duljine, duži prvi vs. kraći prvi).''',
        r'''Odgovor može biti reda $n^4/24 \approx 10^{10}$ (za $a^{800}$ točno $8\,554\,693\,400$) – 64-bitni tip.''',
    ],
    'solution': r'''
<p>Prema službenim rješenjima NAC 2023. Neka je $T = XY = WW$. Ako je $|X| = |Y|$, uvjet je $X = Y$; inače duži podstring ima oblik $ABA$, a kraći je $B$, s $|A| = (|\text{duži}|-|\text{kraći}|)/2$ (zapiši jednakost polovica). Izračunamo $\mathrm{lcp}[i][j]$ za sve sufikse u $O(n^2)$. Jednake duljine: $\sum_{a \lt c} \min(\mathrm{lcp}[a][c], c-a)$. Različite: za svaki $B = s[a..b]$ prefiksnim sumama prebrojimo početke $c$ s $\mathrm{lcp}[a][c] \ge |B|$, zatim za svaki početak $d \lt a$ dužeg podstringa ($|A| = a-d$, kraj $e = b + |A| \lt n$, uvjet $\mathrm{lcp}[d][b+1] \ge |A|$) dodamo broj $c \gt e$ (duži prvi) i broj $c \le d - |B|$ (kraći prvi). Ukupno $O(n^3)$, za $n = 800$ oko $0.15$ s; odgovor u 64 bita.</p>
''',
    'detailed': r'''
<h3>1. Struktura ponavljajućeg spoja</h3>
<p>Neka su $X = s[a_1..b_1]$ i $Y = s[c_1..d_1]$ s $b_1 \lt c_1$ i $T = XY = WW$, $|W| = h$, $|X| = L_1$, $|Y| = L_2$, $L_1 + L_2 = 2h$.</p>
<ul>
<li><strong>$L_1 = L_2$.</strong> Tada je $W = X = Y$; uvjet je jednostavno $X = Y$.</li>
<li><strong>$L_1 \gt L_2$.</strong> Prva polovica $T$ je $X[0..h-1]$, druga je $X[h..L_1-1]\,Y$. Uspoređujući ih znak po znak: prvih $L_1 - h$ znakova daje $X[0..L_1-h-1] = X[h..L_1-1]$; nazovimo taj string $A$, $|A| = L_1 - h = (L_1 - L_2)/2 \ge 1$. Preostalih $L_2$ znakova daje $X[L_1-h..h-1] = Y$. Dakle $X = A\,Y\,A$.</li>
<li><strong>$L_1 \lt L_2$.</strong> Prva polovica je $X\,Y[0..h-L_1-1]$, druga $Y[h-L_1..L_2-1]$. Prvih $L_1$ znakova: $X = Y[h-L_1..h-1]$; ostatak: $Y[0..h-L_1-1] = Y[h..L_2-1] =: A$. Dakle $Y = A\,X\,A$.</li>
</ul>
<p>Obrat je očit: $(ABA)(B)$ i $(B)(ABA)$ su oblika $(AB)(AB)$ odnosno $(BA)(BA)$. Zaključak: par podstringova daje ponavljajući string točno kad su jednaki, ili kad je duži oblika $ABA$ a kraći jednak $B$, gdje je $|A| = (|\text{duži}| - |\text{kraći}|)/2$ (posebno, razlika duljina mora biti parna).</p>
<h3>2. Tablica lcp</h3>
<p>$\mathrm{lcp}[i][j]$ = duljina najduljeg zajedničkog prefiksa sufiksa $s[i..]$ i $s[j..]$. Rekurzija unatrag: $\mathrm{lcp}[i][j] = 1 + \mathrm{lcp}[i+1][j+1]$ ako je $s_i = s_j$, inače $0$, s $\mathrm{lcp}[n][\cdot] = \mathrm{lcp}[\cdot][n] = 0$. Tada je $s[i..i+\ell-1] = s[j..j+\ell-1]$ ekvivalentno s $\mathrm{lcp}[i][j] \ge \ell$ (što ujedno jamči da oba podstringa stanu u $s$). Tablica ima $801^2$ 32-bitnih brojeva, oko $2.6$ MB.</p>
<h3>3. Brojanje: jednake duljine</h3>
<p>Par je određen početcima $a \lt c$ i duljinom $h \ge 1$; treba $h \le \mathrm{lcp}[a][c]$ (jednakost) i $a + h \le c$ (nepreklapanje). Broj valjanih $h$ je $\min(\mathrm{lcp}[a][c], c - a)$, pa je doprinos $\sum_{a \lt c} \min(\mathrm{lcp}[a][c], c-a)$ u $O(n^2)$. Za <code>aaaa</code>: parovi $(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)$ daju $1+2+1+1+1+1 = 7$.</p>
<h3>4. Brojanje: različite duljine</h3>
<p>Par (duži $[d, e]$, kraći $[c, c+|B|-1]$) jednoznačno određuje $|A|$ i položaj $B$ unutar dužeg: $[a, b] = [d + |A|, e - |A|]$. Obrnuto, iz $(a, b, d)$ s $d \lt a$ slijedi $|A| = a - d$ i $e = b + |A|$. Dakle brojimo trojke $(a, b, d)$ uz uvjete $e \le n-1$ i $s[d..a-1] = s[b+1..e]$, tj. $\mathrm{lcp}[d][b+1] \ge a - d$, i za svaku prebrojimo položaje $c$ kopije $B$ (uvjet $\mathrm{lcp}[a][c] \ge |B|$) koji se ne preklapaju s $[d, e]$:</p>
<ol>
<li>Za fiksni $(a, b)$ izračunamo $\mathrm{pre}[c] = \#\{c' \lt c : \mathrm{lcp}[a][c'] \ge b - a + 1\}$ u $O(n)$.</li>
<li>Za $d = a-1, a-2, \dots$ dok je $e = b + (a-d) \le n-1$: ako $\mathrm{lcp}[d][b+1] \ge a-d$, dodaj $\mathrm{pre}[n] - \mathrm{pre}[e+1]$ (kraći iza dužeg, $c \gt e$) i, ako je $d - |B| \ge 0$, $\mathrm{pre}[d - |B| + 1]$ (kraći ispred dužeg, $c + |B| - 1 \lt d$).</li>
</ol>
<p>Slučajevi „jednake duljine”, „duži prvi” i „kraći prvi” su disjunktni, a unutar svakog je parametrizacija bijekcija, pa nema dvostrukog brojanja. Za <code>aaaa</code>: $B = $ <code>a</code> na $a = b = 1$, $d = 0$, $e = 2$: kopija na $c = 3$ ($+1$); $a = b = 2$, $d = 1$, $e = 3$: kopija na $c = 0$ ($+1$). Ukupno $7 + 2 = 9$.</p>
<h3>5. Složenost i zamke</h3>
<ul>
<li>Prefiksne sume: $\binom{n}{2} \cdot n \approx n^3/2$ jednostavnih operacija; unutarnja petlja po $d$: broj trojki $(d \lt a \le b)$ s $e \lt n$ je oko $n^3/6$. Za $n = 800$ to je ispod $0.2$ s (mjereno $0.15$ s na $a^{800}$).</li>
<li>Odgovor za $a^{800}$ je $8\,554\,693\,400 \gt 2^{31}$ – koristi 64-bitni tip.</li>
<li>Indeksi: $\mathrm{lcp}[d][b+1]$ za $b = n-1$ čita stupac $n$ koji mora biti $0$ – dimenzioniraj tablicu na $(n+1)^2$.</li>
<li>$|A| \ge 1$ je automatski ($d \lt a$); slučaj $|A| = 0$ bi bio slučaj jednakih duljina i ne smije se brojati dvaput.</li>
</ul>
''',
    'verified': r'''uzorci 2/2; 300 slučajnih malih testova ($|s| \le 12$, abecede od 1–3 slova) protiv brute forcea koji provjerava sve četvorke $(a, b, c, d)$; 3 velika testa s $|s| = 800$ (sve isto slovo, periodični i slučajni stringovi; najviše $0.15$ s).''',
},
# ---------------------------------------------------------------- K
{
    'letter': 'K', 'title': 'Space Alignment', 'title_hr': 'Poravnanje razmacima', 'slug': 'K_space_alignment',
    'tl': '1 s', 'ml': '2 GiB',
    'statement': r'''
<p>Datoteka s $n$ redaka koda uvlačena je miješano tabulatorima i razmacima. Uvlačenje je dosljedno ako redak na dubini ugniježđenosti $k \ge 0$ ima ispred prvog nepraznog znaka točno $k \cdot i$ razmaka za neki fiksni $i \gt 0$. Može li se svaki tabulator zamijeniti istim brojem razmaka tako da uvlačenje bude dosljedno?</p>
<h3>Ulaz</h3>
<p>$2 \le n \le 100$ redaka; svaki je niz znakova <code>s</code> (razmak) i <code>t</code> (tabulator) iza kojeg slijedi <code>{</code> ili <code>}</code>, najviše $1000$ znakova. Prvi redak je <code>{</code>, posljednji <code>}</code>, zagrade su uparene.</p>
<h3>Izlaz</h3>
<p>Najmanji pozitivan broj razmaka po tabulatoru, ili $-1$.</p>
<h3>Primjer</h3>
<p>Redci <code>{</code>, <code>ss{</code>, <code>sts{</code>, <code>tt}</code>, <code>t}</code>, <code>t{</code>, <code>ss}</code>, <code>}</code>, <code>{</code>, <code>}</code>: $2$.</p>
''',
    'hints': [
        r'''
<p>Za svaki redak izračunaj tri broja: dubinu ugniježđenosti $p$ (pazi: redak sa <code>}</code> je na dubini bloka koji zatvara), broj tabulatora $t$ i broj razmaka $s$. Što redak zahtijeva ako tabulator vrijedi $k$ razmaka?</p>
''',
        r'''
<p>Zahtjev je $t k + s = p \cdot i$ za zajednički $i \gt 0$. Kad je $k$ fiksan, sve je linearno i provjera je $O(n)$ – zato je prirodno isprobati $k = 1, 2, 3, \dots$ redom. Pitanje je samo do kuda.</p>
''',
        r'''
<p>Ako dva retka „ne biraju” isti $k$, iz njihovih jednadžbi slijedi $k = \dfrac{p_1 s_2 - p_2 s_1}{p_2 t_1 - p_1 t_2}$, a brojnik je po apsolutnoj vrijednosti najviše $49 \cdot 999$. Dakle je dovoljno provjeriti $k \le 50\,000$.</p>
''',
    ],
    'coach': [
        ('Koje podatke o retku uopće trebamo, a što je nebitno?',
         r'''
<p>Redoslijed znakova <code>s</code> i <code>t</code> u retku je nebitan – nakon zamjene svaki redak ima $t k + s$ razmaka, gdje je $t$ broj tabulatora, $s$ broj razmaka i $k$ tražena širina tabulatora. Osim toga trebamo dubinu $p$ retka: redak koji otvara blok (<code>{</code>) je na trenutnoj dubini i nakon njega dubina raste, a redak koji zatvara (<code>}</code>) najprije spusti dubinu i onda je na toj (novoj) dubini – zatvarajuća zagrada se poravnava s otvarajućom.</p>
'''),
        ('Zašto ne možemo jednostavno riješiti sustav jednadžbi po $k$ i $i$?',
         r'''
<p>Možemo, ali je nezgodno: uvjet je $t_j k + s_j = p_j i$ za sve retke s $p_j \gt 0$ (a redci na dubini $0$ moraju imati $t_j = s_j = 0$), s dvije cjelobrojne nepoznanice, pozitivnošću, mnogim zavisnim jednadžbama i traženjem <em>najmanjeg</em> $k$. Puno je lakše primijetiti da je za <em>fiksni</em> $k$ provjera trivijalna: prvi uvučeni redak određuje $i = (t_1 k + s_1)/p_1$ (mora biti pozitivan cijeli broj), a svaki drugi redak mora dati isti $i$. To je $O(n)$ po kandidatu.</p>
'''),
        ('Do koje granice moramo isprobavati $k$?',
         r'''
<p>Uzmimo dva uvučena retka. Množenjem jednadžbi s $p_2$ odnosno $p_1$ i oduzimanjem nestaje $i$: $k\,(p_2 t_1 - p_1 t_2) = p_1 s_2 - p_2 s_1$. Ako je zagrada različita od nule, $k$ je jednoznačno određen i $|k| \le |p_1 s_2 - p_2 s_1| \le 49 \cdot 999 \lt 50\,000$ (dubina je najviše $49$ jer ima najviše $100$ redaka, a $s \le 999$). Ako je zagrada nula za <em>sve</em> parove, svi su retci „proporcionalni” ($t_j/p_j$ i $s_j/p_j$ su konstante $c$ i $e$), pa je $i = ck + e$ i jedini uvjet je da $i$ bude pozitivan cijeli broj – nazivnici od $c$ i $e$ dijele sve $p_j \le 49$, pa neki $k \le 49$ radi. Zaključak: ako rješenje postoji, najmanje je $\lt 50\,000$; inače ispisujemo $-1$.</p>
'''),
        ('Je li granica $1000$ iz službenih slajdova dovoljna?',
         r'''
<p>Nije općenito. Službeno rješenje isprobava $k \le 1000$, što vrijedi kad dva retka <em>iste</em> dubine određuju $k$. No za retke <code>{</code>, <code>s</code>$^{999}$<code>{</code> (dubina $1$), <code>t{</code> (dubina $2$) i <code>ts</code>$^{999}$<code>{</code> (dubina $3$) dobivamo $i = 999$, $k = 2i = 1998$ i $k + 999 = 3i$ – jedinstveno rješenje $k = 1998 \gt 1000$. Zato koristimo dokazanu granicu $50\,000$; ukupno $5\cdot 10^4 \cdot 100 = 5 \cdot 10^6$ jednostavnih operacija, daleko unutar limita.</p>
'''),
    ],
    'tips': [
        r'''Kad su nepoznanice cjelobrojne i jedna od njih ima mali raspon, „isprobaj sve vrijednosti i provjeri u $O(n)$” često pobjeđuje elegantno rješavanje sustava – ali dokaži granicu raspona, ne pogađaj je.''',
        r'''Iz dviju linearnih jednadžbi s dvije nepoznanice eliminiraj jednu množenjem i oduzimanjem; tako se dobiva eksplicitna gornja međa za drugu nepoznanicu (brojnik ograničen podacima, nazivnik cijeli broj $\ge 1$).''',
        r'''Pri simulaciji dubine zagrada pazi na redoslijed: otvarajuća zagrada „pripada” vanjskoj razini (najprije zabilježi dubinu, pa povećaj), zatvarajuća se poravnava s otvarajućom (najprije smanji, pa zabilježi).''',
    ],
    'solution': r'''
<p>Prema službenim rješenjima NAC 2023 (uz strožu granicu pretrage). Za svaki redak odredimo dubinu $p$, broj tabulatora $t$ i razmaka $s$; zatvarajuća zagrada je na dubini bloka koji zatvara. Za fiksni broj razmaka po tabulatoru $k$ redak zahtijeva $t k + s = p \cdot i$ za zajednički cijeli $i \gt 0$ (redci na dubini $0$ moraju imati $t = s = 0$), što se provjeri u $O(n)$. Isprobamo $k = 1, 2, \dots, 50\,000$ i ispišemo prvi koji prolazi, inače $-1$. Granica: ako dva retka određuju $k$, onda $k = \frac{p_1 s_2 - p_2 s_1}{p_2 t_1 - p_1 t_2}$ pa $|k| \le 49 \cdot 999$; ako nijedan par ne određuje $k$, radi neki $k \le 49$. Složenost $O(50\,000 \cdot n)$.</p>
''',
    'detailed': r'''
<h3>1. Što redak zapravo zahtijeva</h3>
<p>Nakon što svaki tabulator zamijenimo s $k$ razmaka, redak s $t$ tabulatora i $s$ razmaka ima točno $t k + s$ razmaka ispred zagrade – redoslijed znakova je nebitan. Dosljedno uvlačenje traži da to bude $p \cdot i$, gdje je $p$ dubina ugniježđenosti retka, a $i \gt 0$ jedna zajednička širina uvlake za cijelu datoteku. Dubinu računamo jednim prolazom: redak s <code>{</code> je na trenutnoj dubini $d$ i nakon njega $d$ raste za $1$; redak s <code>}</code> najprije smanji $d$ i tada je na dubini $d$ (zatvarajuća zagrada se poravnava s otvarajućom). Provjera na primjeru: redak <code>tt}</code> zatvara blok otvoren retkom <code>sts{</code>, oba su na dubini $2$; s $k = 2$ prvi ima $4$, drugi $2 + 2 = 4$ razmaka i $i = 2$.</p>
<p>Uz $n \le 100$ redaka i uparene zagrade dubina nikad ne prelazi $49$: da bi neki redak bio na dubini $50$, prije njega bi moralo biti barem $50$ otvaranja, a poslije njega $50$ zatvaranja, ukupno $101$ redak.</p>
<h3>2. Provjera za fiksni $k$</h3>
<p>Ako $k$ znamo, sve postaje linearno. Redak na dubini $0$ ne smije imati nikakvo uvlačenje: $t k + s = 0$, tj. $t = s = 0$ (neovisno o $k$). Za retke s $p \gt 0$ količina $u_j = t_j k + s_j$ mora biti djeljiva s $p_j$ i kvocijent $u_j / p_j$ mora biti isti pozitivan cijeli broj $i$ za sve takve retke. Algoritam: prođi retke, za prvi uvučeni redak postavi $i = u_j / p_j$ (ako nije cijeli ili je $0$, $k$ otpada), za ostale usporedi. Ako nema nijednog uvučenog retka (npr. datoteka <code>{</code>, <code>}</code>), svaki $k$ radi i odgovor je $1$. Provjera traje $O(n)$.</p>
<h3>3. Zašto je pretraga $k \le 50\,000$ dovoljna (dokaz)</h3>
<p>Neka rješenje postoji i neka su $(t_1, s_1, p_1)$ i $(t_2, s_2, p_2)$ dva uvučena retka. Iz $t_1 k + s_1 = p_1 i$ i $t_2 k + s_2 = p_2 i$ množenjem prve s $p_2$, druge s $p_1$ i oduzimanjem dobivamo</p>
<p>$$k\,(p_2 t_1 - p_1 t_2) = p_1 s_2 - p_2 s_1 .$$</p>
<ul>
<li><strong>Slučaj A:</strong> za neki par je $p_2 t_1 - p_1 t_2 \ne 0$. Tada je $k$ jednoznačno određen kao kvocijent dvaju cijelih brojeva s nazivnikom $\ge 1$ po apsolutnoj vrijednosti, pa $k \le |p_1 s_2 - p_2 s_1| \le \max(p_1 s_2, p_2 s_1) \le 49 \cdot 999 = 48\,951 \lt 50\,000$. (Svaki redak ima najviše $1000$ znakova uključujući zagradu, dakle $s \le 999$.)</li>
<li><strong>Slučaj B:</strong> za sve parove je $p_2 t_1 = p_1 t_2$, tj. omjer $t_j / p_j = c$ je isti za sve uvučene retke. Tada iz $t_j k + s_j = p_j i$ slijedi $s_j / p_j = i - ck =: e$, također konstanta. Jednadžbe se svode na jednu: $i = ck + e$, i jedini uvjet je da $i$ bude pozitivan cijeli broj. Nazivnici razlomaka $c = a/b$ i $e = f/g$ (u skraćenom obliku) dijele sve $p_j$, pa za $k$ višekratnik od $\operatorname{lcm}(b, g)$ – koji dijeli $p_1 \le 49$ – vrijednost $c k + e$ je cijela, a pozitivna je jer je $c \ge 0$, $e \ge 0$ i nisu oba nula (inače bi uvučeni redak imao $t = s = 0$, što ne može dati $i \gt 0$). Dakle neki $k \le 49$ prolazi.</li>
</ul>
<p>U oba slučaja najmanje valjano $k$ je manje od $50\,000$; ako nijedan $k$ u tom rasponu ne prolazi, rješenja nema i odgovor je $-1$. Petlja od $50\,000$ kandidata s $O(n)$ provjerom daje $5 \cdot 10^6$ operacija.</p>
<h3>4. Napomena o službenoj granici $1000$</h3>
<p>Službeni slajdovi NAC 2023 predlažu $k \le 1000$, s argumentom da dva retka <em>iste</em> dubine daju $k = (s_2 - s_1)/(t_1 - t_2)$. Za retke različitih dubina to ne vrijedi: datoteka <code>{</code>, <code>s</code>$^{999}$<code>{</code>, <code>t{</code>, <code>ts</code>$^{999}$<code>{</code>, <code>ts</code>$^{999}$<code>}</code>, <code>t}</code>, <code>s</code>$^{999}$<code>}</code>, <code>}</code> ima jedinstveno rješenje $i = 999$, $k = 1998$ (iz $k = 2i$ i $k + 999 = 3i$). Naše rješenje i brute force na tom testu ispisuju $1998$; petlja do $1000$ bi pogrešno ispisala $-1$. Zato koristimo dokazanu granicu – cijena je zanemariva.</p>
<h3>5. Implementacija i zamke</h3>
<ul>
<li>Ne treba fizički graditi nizove razmaka – dovoljno je brojati <code>t</code> i <code>s</code> po retku; koristimo <code>long long</code> jer $t k \le 999 \cdot 50\,000$ prelazi $2^{31}$ tek u teoriji, ali sigurnije je.</li>
<li>Redoslijed ažuriranja dubine (točka 1) je najčešća greška: zatvarajuću zagradu treba staviti na dubinu <em>nakon</em> smanjenja.</li>
<li>Redci na dubini $0$ s uvlakom (npr. <code>s{</code> odmah nakon zatvaranja svega) odmah znače $-1$, bez obzira na $k$.</li>
<li>Kvocijent $u_j / p_j$ mora biti strogo pozitivan: uvučeni redak s $t = s = 0$ znači $i = 0$, što je zabranjeno.</li>
</ul>
<h3>6. Složenost</h3>
<p>Vrijeme $O(K_{\max} \cdot n) = O(5 \cdot 10^6)$, memorija $O(n)$ uz čitanje redaka.</p>
''',
    'verified': r'''uzorak 1/1; 300 slučajnih malih testova ($n \le 10$, konstruirana dosljedna uvlačenja s nasumičnim $k, i$ i pokvarenim retcima te posve nasumični redci) protiv brute forcea koji za $k \le 60\,000$ doslovno zamjenjuje tabulatore i provjerava uvlačenje; 3 velika testa ($n = 100$, redci do $1000$ znakova, $k$ do $49\,000$) usporedena s brute forceom (<0.01 s); ručno provjeren test s odgovorom $1998 \gt 1000$.''',
},
# ---------------------------------------------------------------- L
{
    'letter': 'L', 'title': 'Splitting Pairs', 'title_hr': 'Razdvajanje parova', 'slug': 'L_splitting_pairs',
    'tl': '1 s', 'ml': '2 GiB',
    'statement': r'''
<p>Modificirani Nim: $n$ nepraznih hrpi kamenja, Alice počinje. U potezu igrač redom: ukloni neki broj hrpi (barem jednu, najviše polovicu broja hrpi), zatim odabere isto toliko preostalih hrpi i svaku podijeli na dvije neprazne. Broj hrpi tako ostaje $n$. Tko ne može izvesti potez, gubi.</p>
<p>Za svaku igru odredi pobjednika uz optimalnu igru.</p>
<h3>Ulaz</h3>
<p>$1 \le t \le 1000$ igara; $2 \le n \le 50$, veličine hrpi $1 \le s \le 10^{12}$.</p>
<h3>Izlaz</h3>
<p>Za svaku igru $1$ ako pobjeđuje Alice, $0$ ako Bob.</p>
<h3>Primjer</h3>
<p>$(1, 1, 1) \to 0$; $(1, 1, 2) \to 1$; $(2, 2, 2) \to 0$; $(4, 4, 4, 4) \to 1$.</p>
''',
    'hints': [
        r'''
<p>Igra je konačna (ukupan broj kamenja strogo pada), a jedino stanje bez poteza je „sve hrpe imaju jedan kamen”. Odigraj ručno male slučajeve s parnim $n$ i pogledaj parnost hrpi.</p>
''',
        r'''
<p>Za paran $n$: iz stanja u kojem su sve hrpe neparne <em>svaki</em> potez stvara parnu hrpu (neparan broj se dijeli na paran + neparan). Obrnuto, ako postoji parna hrpa, možeš li uvijek u jednom potezu doći do stanja „sve neparne”?</p>
''',
        r'''
<p>Za neparan $n$ pravu invarijantu vidiš tek nakon dijeljenja s najvećom potencijom dvojke koja dijeli sve hrpe: gubitničko je stanje točno kad sve hrpe imaju <em>isti</em> broj dvojki u rastavu, $v_2(s_1) = \dots = v_2(s_n)$.</p>
''',
    ],
    'coach': [
        ('Koje je jedino završno stanje i kako iz njega „unatrag” naslutiti invarijantu?',
         r'''
<p>Potez ne postoji točno kad nijedna hrpa nema barem dva kamena, tj. sve su hrpe jedinice. To je gubitničko stanje i ono ima svojstvo „sve hrpe neparne” (i, još jače, sve hrpe imaju isti broj dvojki u rastavu, nula). Igra je konačna jer uklanjanje $k \ge 1$ hrpi smanjuje ukupan broj kamenja, a dijeljenje ga čuva. Kod ovakvih igara tražimo svojstvo $P$ za koje vrijedi: (1) iz stanja s $P$ nijedan potez ne vodi u stanje s $P$, (2) iz stanja bez $P$ postoji potez u stanje s $P$, (3) završno stanje ima $P$. Tada su stanja s $P$ točno gubitnička.</p>
'''),
        ('Zašto je za paran $n$ svojstvo „sve hrpe neparne” upravo to $P$?',
         r'''
<p>(1) Ako su sve hrpe neparne, dijeljenje neparne hrpe $x = a + b$ daje jedan paran i jedan neparan dio, pa nakon poteza sigurno postoji parna hrpa. (2) Neka je $e \ge 1$ broj parnih hrpi. Ako je $e \le n/2$: uklonimo $e$ neparnih hrpi (ima ih $n - e \ge n/2 \ge e$) i svaku parnu hrpu $x$ podijelimo na $1$ i $x - 1$, oba neparna – sve postaje neparno. Ako je $e \gt n/2$: uzmemo $k = n/2$, podijelimo $n/2$ parnih hrpi na neparno + neparno, a uklonimo preostalih $e - n/2$ parnih hrpi i sve $n - e$ neparnih hrpi (zajedno točno $n/2$ hrpi). (3) Sve jedinice su neparne. Dakle za paran $n$ Alice pobjeđuje točno kad postoji parna hrpa.</p>
'''),
        ('Zašto za neparan $n$ isto svojstvo ne radi i što ga zamjenjuje?',
         r'''
<p>Uzorak $(2,2,2) \to 0$ pokazuje da stanje sa svim parnim hrpama može biti gubitničko kad je $n$ neparan: uklonimo li jednu hrpu i podijelimo drugu na $1 + 1$, ostaje $(1,1,2)$ koje je pobjedničko za protivnika – a to je jedini mogući potez (iz $(1,1,2)$ protivnik ukloni jedinicu i podijeli dvojku u $(1,1,1)$). Ključ je da za neparan $n$ nakon poteza uvijek ostaje barem $n - 2k \ge 1$ netaknuta hrpa. Označimo $v(x)$ broj dvojki u rastavu od $x$. Tvrdnja: gubitnička su točno stanja u kojima sve hrpe imaju istu vrijednost $v$, tj. nakon dijeljenja s najvećom zajedničkom potencijom dvojke sve su hrpe neparne.</p>
'''),
        ('Kako dokazati tvrdnju za neparan $n$?',
         r'''
<p>(1) Neka sve hrpe imaju $v = p$. Dijelimo $x = 2^p u$ ($u$ neparan) na $a + b$. Ako je $v(a) \lt p$, onda je i $v(b) = v(a) \lt p$; ako je $v(a) \ge p$, pišemo $a = 2^p u_1$, $b = 2^p u_2$ s $u_1 + u_2 = u$ neparnim, pa je točno jedan od $u_1, u_2$ paran – jedan dio ima $v = p$, drugi $v \gt p$. U oba slučaja novo stanje sadrži dvije različite vrijednosti $v$ (u prvom zato što netaknuta hrpa ima $v = p$, a dijelovi $v \lt p$). (2) Ako nisu sve $v$ jednake, neka je $p$ najmanja i $e$ broj hrpi s $v \gt p$, $1 \le e \le n - 1$. Hrpu $x$ s $v(x) \gt p$ dijelimo na $2^p$ i $x - 2^p$: oba dijela imaju $v = p$ jer je $x/2^p$ paran, pa je $x/2^p - 1$ neparan. Zatim točno kao u parnom slučaju: ako je $e \le (n-1)/2$, podijelimo sve takve hrpe i uklonimo $e$ hrpi s $v = p$; inače podijelimo $(n-1)/2$ njih, a uklonimo ostale „visoke” i sve „niske” hrpe (ukupno $(n-1)/2$). Rezultat: sve hrpe imaju $v = p$. (3) Završno stanje ima sve $v = 0$. Za paran $n$ ista tvrdnja s $p = 0$ daje ranije pravilo – ali za paran $n$ stanje sa svim $v = p \gt 0$ je pobjedničko (npr. $(2,2)$: ukloni jednu, podijeli drugu na $1+1$), jer tada može nestati svaka netaknuta hrpa.</p>
'''),
    ],
    'tips': [
        r'''Za igre s neobičnim potezima ne traži odmah Sprague-Grundyjeve vrijednosti; prvo brute forceom ispiši gubitnička stanja za male ulaze i traži invarijantu tipa parnost, valuacija dvojkom ili suma modulo nečega.''',
        r'''Standardni dokazni obrazac za karakterizaciju gubitničkih stanja: (1) iz $P$ se ne može u $P$, (2) iz ne-$P$ se može u $P$, (3) završna stanja su u $P$. Napiši sva tri koraka eksplicitno – ovdje se točno na koraku (2) vidi razlika između parnog i neparnog $n$.''',
        r'''Kad hipoteza „sve neparno” pukne na nekom uzorku, probaj je „skalirati”: podijeli sve vrijednosti najvećom zajedničkom potencijom dvojke (ili NZD-om) i ponovno provjeri.''',
    ],
    'solution': r'''
<p>Prema službenim rješenjima NAC 2023. Neka je $v(x)$ broj dvojki u rastavu od $x$. Gubitnička su stanja: za paran $n$ ona u kojima su sve hrpe neparne, a za neparan $n$ ona u kojima sve hrpe imaju istu vrijednost $v$. Dokaz: iz takvog stanja svaki potez uništi svojstvo (dijeljenje $2^p u$, $u$ neparan, daje dijelove s različitim ili manjim $v$, a za neparan $n$ barem jedna hrpa ostaje netaknuta), a iz stanja bez svojstva podijelimo do $\lfloor n/2 \rfloor$ hrpi s najvećim $v$ na $2^p + (x - 2^p)$ i uklonimo odgovarajući broj drugih hrpi tako da sve hrpe dobiju $v = p$. Odgovor je $1$ točno kad stanje nije gubitničko; $O(n \log s)$ po igri.</p>
''',
    'detailed': r'''
<h3>1. Struktura igre</h3>
<p>Potez uklanja $k$ hrpi ($1 \le k \le \lfloor n/2 \rfloor$) i zatim $k$ preostalih hrpi s barem dva kamena dijeli na dvije neprazne. Broj hrpi ostaje $n$, a ukupan broj kamenja strogo pada (uklonjene hrpe su neprazne), pa igra završava. Potez ne postoji točno kad nema $k \ge 1$ hrpi s barem dva kamena među preostalima – s obzirom na to da možemo uklanjati po volji, to znači: <em>nema poteza točno kad su sve hrpe jedinice</em> (ako postoji hrpa $\ge 2$, uklonimo neku drugu hrpu i podijelimo nju). Za neparan $n$ vrijedi $n - 2k \ge 1$: barem jedna hrpa uvijek ostane netaknuta; za paran $n$ i $k = n/2$ svaka hrpa je ili uklonjena ili podijeljena.</p>
<h3>2. Metoda: karakterizacija gubitničkih stanja</h3>
<p>Skup stanja $L$ je točno skup gubitničkih stanja ako vrijedi: (1) iz stanja u $L$ nijedan potez ne vodi u $L$; (2) iz stanja izvan $L$ postoji potez u $L$; (3) sva završna stanja su u $L$. Dokaz indukcijom po ukupnom broju kamenja: u stanju iz $L$ svaki potez vodi u stanje izvan $L$, koje je po indukciji pobjedničko za protivnika; u stanju izvan $L$ potez iz (2) vodi u gubitničko stanje za protivnika.</p>
<h3>3. Paran $n$: $L = \{$sve hrpe neparne$\}$</h3>
<ul>
<li>(1) Neparna hrpa $x = a + b$ ima jedan paran i jedan neparan dio, pa nakon bilo kojeg poteza (barem jedno dijeljenje) postoji parna hrpa.</li>
<li>(2) Neka je $e \ge 1$ broj parnih hrpi. Parnu hrpu $x$ dijelimo na $1$ i $x-1$ (oba neparna). Ako je $e \le n/2$: uzmemo $k = e$, uklonimo $e$ neparnih hrpi (ima ih $n - e \ge e$), podijelimo svih $e$ parnih. Ako je $e \gt n/2$: $k = n/2$, podijelimo $n/2$ parnih, a uklonimo preostalih $e - n/2$ parnih i svih $n - e$ neparnih hrpi; zbroj uklonjenih je $(e - n/2) + (n - e) = n/2 = k$. U oba slučaja sve hrpe postaju neparne.</li>
<li>(3) Sve jedinice su neparne.</li>
</ul>
<p>Dakle Alice pobjeđuje točno kad postoji barem jedna parna hrpa. Primjer $(4,4,4,4) \to 1$.</p>
<h3>4. Neparan $n$: $L = \{$sve hrpe imaju istu valuaciju $v\}$</h3>
<p>Ovdje $v(x)$ označava najveći $p$ takav da $2^p \mid x$. Uzorak $(2,2,2) \to 0$ pokazuje da „sve neparne” nije dovoljno – gubitnička su i stanja koja se, nakon dijeljenja svih hrpi zajedničkom potencijom dvojke, svode na „sve neparne”.</p>
<ul>
<li>(1) Neka sve hrpe imaju $v = p$ i dijelimo $x = 2^p u$, $u$ neparan, na $a + b$. Ako je $v(a) \lt p$, onda je $v(b) = v(a)$ (zbroj dvaju brojeva različitih valuacija ima manju od njih, a $v(x) = p \gt v(a)$ pa mora biti $v(b) = v(a)$); tada dijelovi imaju $v \lt p$, a netaknuta hrpa (postoji jer je $n$ neparan) ima $v = p$. Ako je $v(a) \ge p$, onda $a = 2^p u_1$, $b = 2^p u_2$, $u_1 + u_2 = u$ neparan, pa je točno jedan od $u_1, u_2$ paran: dijelovi imaju $v = p$ i $v \gt p$. U svakom slučaju nakon poteza postoje dvije različite valuacije, tj. napustili smo $L$.</li>
<li>(2) Neka valuacije nisu sve jednake; $p = \min v$, a $e$ broj hrpi s $v \gt p$, $1 \le e \le n - 1$. Hrpu $x$ s $v(x) \gt p$ dijelimo na $2^p$ i $x - 2^p = 2^p (x/2^p - 1)$; kako je $x / 2^p$ paran, $x/2^p - 1$ je neparan i oba dijela imaju $v = p$. Ako je $e \le (n-1)/2$: $k = e$, podijelimo sve „visoke” hrpe i uklonimo $e$ „niskih” (ima ih $n - e \ge e$). Ako je $e \gt (n-1)/2$: $k = (n-1)/2$, podijelimo $k$ visokih, uklonimo ostalih $e - k$ visokih i $k - (e - k) = n - 1 - e$ niskih (ima ih $n - e \ge n - 1 - e$). Sve hrpe sada imaju $v = p$.</li>
<li>(3) Završno stanje (sve jedinice) ima sve $v = 0$.</li>
</ul>
<p>Zašto isti argument ne daje isto pravilo za paran $n$? Korak (1) koristi netaknutu hrpu s $v = p$ kad dijelovi padnu na $v \lt p$; za paran $n$ i $k = n/2$ takve hrpe nema, npr. $(2,2)$: uklonimo jednu, drugu podijelimo na $1 + 1$ i protivnik gubi. Za paran $n$ zato ostaje pravilo s $p = 0$ – ono je, uostalom, poseban slučaj ovog pravila jer za $p = 0$ „dijelovi s $v \lt 0$” ne postoje.</p>
<h3>5. Algoritam</h3>
<ol>
<li>Za paran $n$: ispiši $0$ ako su sve hrpe neparne, inače $1$.</li>
<li>Za neparan $n$: izračunaj $v(s_i)$ za sve hrpe (petlja dijeljenja s $2$, najviše $40$ koraka jer $s \le 10^{12} \lt 2^{40}$); ispiši $0$ ako su sve jednake, inače $1$.</li>
</ol>
<p>Provjera na uzorcima: $(1,1,1)$ sve $v = 0 \to 0$; $(1,1,2)$ valuacije $0,0,1 \to 1$; $(2,2,2)$ sve $v = 1 \to 0$; $(4,4,4,4)$ paran $n$, postoji parna hrpa $\to 1$.</p>
<h3>6. Složenost i zamke</h3>
<p>$O(n \log s)$ po igri, ukupno zanemarivo. Hrpe do $10^{12}$ zahtijevaju 64-bitne cijele brojeve; pravilo za paran $n$ ne smije se zamijeniti pravilom za neparan (stanje $(2,2)$ je pobjedničko, a $(2,2,2)$ gubitničko).</p>
''',
    'verified': r'''uzorak 1/1; 300 slučajnih malih testova ($n \le 5$, hrpe $\le 8$, uključujući stanja s jednakim valuacijama i „gotovo jednakim”) protiv brute forcea koji potpunim pretraživanjem igre s memoizacijom (svi izbori uklonjenih hrpi, podijeljenih hrpi i načina dijeljenja) određuje pobjednika; 3 velika testa s $t = 1000$, $n \le 50$, hrpe do $10^{12}$ (<0.01 s).''',
},
# ---------------------------------------------------------------- M
{
    'letter': 'M', 'title': 'Who Watches the Watchmen?', 'title_hr': 'Tko čuva čuvare?', 'slug': 'M_who_watches_the_watchmen',
    'tl': '4 s', 'ml': '2 GiB',
    'statement': r'''
<p>$n$ stražarskih dronova u 3D prostoru; dron u $(x, y, z)$ sa smjerom $(v_x, v_y, v_z)$ vidi točke $(x + t v_x, y + t v_y, z + t v_z)$, $t \ge 0$, ako između njega i točke nije drugi dron. Cilj: svaki dron gleda nekog drugog drona i svaki je dron viđen od <em>točno jednog</em> drugog.</p>
<p>Promjena smjera stoji $1$, premještanje na novu lokaciju $1000$ (oboje $1001$); nakon premještanja pozicija ne mora biti cjelobrojna, a dva drona ne smiju biti na istom mjestu. Odredi najmanju ukupnu energiju.</p>
<h3>Ulaz</h3>
<p>$1 \le n \le 500$; za svaki dron $x, y, z, v_x, v_y, v_z$ iz $[-10^6, 10^6]$, smjer nije nul-vektor, pozicije različite.</p>
<h3>Izlaz</h3>
<p>Najmanja energija ili $-1$ ako je nemoguće.</p>
<h3>Primjer</h3>
<p>Dronovi $(66,45,10; 73,39,36)$, $(95,14,26; 47,84,59)$, $(14,66,89; 89,36,78)$, $(16,27,94; 79,24,24)$: $4$.</p>
''',
    'hints': [
        r'''
<p>„Svaki gleda točno jednog i svakoga gleda točno jedan” je permutacija bez fiksnih točaka – unija ciklusa duljine $\ge 2$. Koji parovi $(i, j)$ smiju biti brid? Koliko stoji brid koji već postoji?</p>
''',
        r'''
<p>Premještanje ($1000$) je skuplje od okretanja svih ($n \le 500$), pa se isplati samo kad bez njega nema rješenja. Kad graf vidljivosti nema pokrivanje ciklusima? Sortiraj točke po generičkom smjeru – susjedne su uvijek međusobno vidljive.</p>
''',
        r'''
<p>Bipartitno uparivanje minimalne cijene ($0/1/\infty$, mađarski algoritam). Poseban slučaj: $n$ neparan i svi kolinearni – pomakni točno jednog izvan pravca; on je u ciklusu sa susjednim komadom pravca, ostatak se uparuje; okrete za njega i njegova „gledača” određuje presjek dviju zraka u 3D.</p>
''',
    ],
    'coach': [
        ('Kako izgleda tražena konfiguracija kao graf?',
         r'''
<p>Svaki dron gleda točno jednog (prvog na svojoj zraci), svakoga gleda točno jedan: to je funkcija $\sigma$ na dronovima bez fiksne točke koja je bijekcija – permutacija čiji su ciklusi duljine $\ge 2$ (dvociklus = dva drona koja gledaju jedno drugo). Brid $i \to \sigma(i)$ moguć je točno kad na otvorenom segmentu $(P_i, P_{\sigma(i)})$ nema drugog drona (tada se $i$ može okrenuti prema $\sigma(i)$ i vidjet će baš njega). Cijena brida: $0$ ako $\sigma(i)$ već jest prvi dron na zraci $i$, inače $1$.</p>
'''),
        ('Zašto premještanje gotovo nikad nije isplativo?',
         r'''
<p>Okretanje <em>svih</em> dronova stoji $n \le 500 \lt 1000$. Ako bez premještanja postoji ikakvo rješenje, njegova je cijena $\le n$, pa je premještanje suvišno. Zato je zadatak: minimalno uparivanje u bipartitnom grafu (lijeva kopija „tko gleda”, desna „koga gleda”) s cijenama $0/1/\infty$ – mađarski algoritam u $O(n^3)$; a premještamo samo ako savršeno uparivanje ne postoji, i tada točno jednog (dva premještanja stoje $2000 \gt 1000 + n$).</p>
'''),
        ('Kad pokrivanje ciklusima ne postoji?',
         r'''
<p>Sortiraj točke po projekciji na generički smjer $d$ (sve projekcije različite). Ako je $R$ strogo unutar segmenta $AB$, njegova je projekcija strogo između, pa su <em>susjedne</em> točke u tom poretku uvijek vidljive: graf sadrži Hamiltonov put $P_1 \dots P_n$. Za paran $n$ upari $(P_1P_2)(P_3P_4)\dots$. Za neparan $n$ trebamo neparan ciklus: ako je neka trojka $P_i, P_{i+1}, P_{i+2}$ s neparnim $i$ nekolinearna, ona je trokut ($P_i$–$P_{i+2}$ blokira samo $P_{i+1}$, a on nije na segmentu), ostatak se uparuje. Inače su sve trojke $(P_{2k-1}, P_{2k}, P_{2k+1})$ kolinearne; ako točke nisu sve na jednom pravcu, dvije susjedne takve trojke leže na različitim pravcima $L_1 \ne L_2$ kroz zajedničku točku $c = P_{2k+1}$: za $a,b,c \in L_1$ i $c,d,e \in L_2$ (u poretku projekcija) vrijedi da $a$ vidi $d$ i $e$ te $d$ vidi $e$ (svaki blokator bi značio $L_1 = L_2$), pa trokut $(a, d, e)$ + par $(b, c)$ + upareni ostatak. Dakle rješenje bez premještanja ne postoji točno kad je $n = 1$ ili kad je $n$ neparan i svi su dronovi kolinearni (graf vidljivosti je put, a put nema ciklusa).</p>
'''),
        ('Kako riješiti kolinearan neparan slučaj?',
         r'''
<p>Pomaknemo točno jedan dron $M$ izvan pravca $L$ (na $L$ bi ostalo kolinearno i neparno). Preostalih $n - 1$ točaka na $L$ čini put $Q_0, \dots, Q_{n-2}$, a $M$ vidi sve njih i sve one vide $M$. $M$ leži u ciklusu $M \to Q_i \to \dots \to Q_j \to M$ (ili obrnuto) sa <em>susjednim</em> komadom puta; lijevo i desno od komada moraju ostati parni blokovi, pa je $i$ paran i $j$ neparan (0-indeksirano). Cijene na pravcu su jednostavne: $Q_a$ gleda $Q_{a+1}$ besplatno točno kad je $v_{Q_a}$ paralelan s $L$ u pozitivnom smjeru (nakon uklanjanja $M$ između njih više nema nikoga). Za $M$ i njegova gledača $W$: $M$ ne treba okret ako ga stavimo na $P_T - t v_M$ ($t \gt 0$; mora biti $v_M \nparallel L$), $W$ ne treba okret ako je $M = P_W + s v_W$ ($s \gt 0$, $v_W \nparallel L$); oboje besplatno ako se te dvije zrake sijeku (egzaktno u cijelim brojevima: komplanarnost i predznaci $t, s$ preko vektorskih produkata). Za svaki $M$ i svaki $(i, j)$ ukupno $1000 + $ (upareni prefiks) $+$ (upareni sufiks) $+ \min$(dvije orijentacije) – prefiksne sume daju $O(n^3/4)$.</p>
'''),
    ],
    'tips': [
        r'''„Svaki pokazuje na točno jednog, na svakoga pokazuje točno jedan” = permutacija; ograničenja na bridove čine to bipartitnim uparivanjem (lijevo izvor, desno cilj), a cijene $0/1$ rješava mađarski algoritam.''',
        r'''Prije nego se upustiš u skupe operacije, usporedi ih s cijenom „napravi sve jeftino”: $1000 \gt n$ odmah kaže da se premješta najviše jednom i samo kad je nužno.''',
        r'''Vidljivost u skupu točaka: točke sortirane po generičkom smjeru su susjedno vidljive; za sve parove usporedi normalizirani smjer $(\Delta x, \Delta y, \Delta z)/\gcd$ – vidljiv je samo najbliži u svakom smjeru.''',
        r'''3D presjek zraka računaj egzaktno: $t\,(u\times w) = D\times w$, komplanarnost $D\cdot(u\times w) = 0$; produkti do $10^{25}$ traže <code>__int128</code>.''',
    ],
    'solution': r'''
<p>Prema službenim rješenjima NAC 2023. Cilj je permutacija bez fiksnih točaka: brid $i \to j$ postoji ako na segmentu nema drugog drona (cijena $1$, ili $0$ ako $i$ već gleda $j$). Premještanje ($1000 \gt n$) isplati se samo kad nema rješenja bez njega: $n = 1$ ($-1$) ili $n$ neparan i svi kolinearni; inače mađarski algoritam na bipartitnom grafu s cijenama $0/1/\infty$, $O(n^3)$. Kolinearan neparan slučaj: pomakni točno jednog $M$ izvan pravca; ostali čine put $Q_0..Q_{n-2}$, $M$ je u ciklusu sa susjednim komadom $Q_i..Q_j$ ($i$ paran, $j$ neparan), ostatak upareni susjedi; okreti $M$ i njegova gledača su $0/1/2$ ovisno o egzaktnom presjeku zrake gledača i zrake unazad od cilja. Prefiksne sume, $O(n^3)$.</p>
''',
    'detailed': r'''
<h3>1. Model</h3>
<p>Dron gleda prvog drona na svojoj zraci (ili nikoga). Konačno stanje: funkcija $\sigma$ „$i$ gleda $\sigma(i)$”, $\sigma(i) \ne i$, i svaki je dron slika točno jednog – dakle permutacija bez fiksnih točaka, tj. disjunktni ciklusi duljine $\ge 2$. Brid $i \to j$ moguć je točno kad je $j$ <em>vidljiv</em> iz $i$: na otvorenom segmentu $(P_i, P_j)$ nema drugog drona (tada okret prema $j$ vidi baš $j$; ako netko jest na segmentu, $i$ nikad ne može vidjeti $j$ bez premještanja). Cijena brida je $0$ ako je $j$ već prvi dron na zraci $i$, inače $1$. Vidljivost je simetrična.</p>
<h3>2. Premještanje je (gotovo) nikad</h3>
<p>Okret svih $n \le 500$ dronova stoji $\lt 1000$. Ako postoji ikakvo pokrivanje ciklusima u grafu vidljivosti, optimalno rješenje ne premješta nikoga. Ako ne postoji, premješta se točno jedan dron (dva stoje $2000 \gt 1000 + n$). Zato prvo riješimo <em>bez</em> premještanja i utvrdimo kada to nije moguće.</p>
<h3>3. Kad postoji pokrivanje ciklusima?</h3>
<p><strong>Lema 1.</strong> Za generički smjer $d$ (sve projekcije $d \cdot P_i$ različite) sortirajmo točke: $P_1, \dots, P_n$. Tada su $P_i$ i $P_{i+1}$ vidljive. <em>Dokaz:</em> točka strogo unutar segmenta ima projekciju strogo između, a takve nema. $\square$</p>
<p><strong>Lema 2.</strong> $P_i$ i $P_{i+2}$ su vidljive točno kad $P_i, P_{i+1}, P_{i+2}$ nisu kolinearne (jedini kandidat za blokatora je $P_{i+1}$). $\square$</p>
<p><strong>Tvrdnja.</strong> Pokrivanje ciklusima postoji točno kad $n \ge 2$ i (ili je $n$ paran ili točke nisu sve kolinearne).</p>
<p><em>Nužnost:</em> $n = 1$ nema koga gledati; za sve kolinearne točke graf vidljivosti je put (vidljivi su samo susjedi na pravcu), put nema ciklusa duljine $\ge 3$, a savršeno uparivanje puta s neparno mnogo vrhova ne postoji.</p>
<p><em>Dovoljnost:</em> $n$ paran – upari $(P_1P_2), (P_3P_4), \dots$ po Lemi 1. $n$ neparan, nekolinearne: (a) ako je za neki <em>neparan</em> $i$ trojka $P_i, P_{i+1}, P_{i+2}$ nekolinearna, po Lemama 1–2 to je trokut (ciklus duljine 3), a $P_1..P_{i-1}$ i $P_{i+3}..P_n$ imaju paran broj točaka i uparuju se susjedno. (b) Inače su sve trojke $(P_{2k-1}, P_{2k}, P_{2k+1})$ kolinearne; kad bi svi ti pravci bili isti, sve bi točke bile kolinearne, pa postoje susjedne trojke na pravcima $L_1 \ne L_2$ sa zajedničkom točkom $c = P_{2k+1}$. Označimo $a = P_{2k-1}, b = P_{2k} \in L_1$ i $d = P_{2k+2}, e = P_{2k+3} \in L_2$. Kandidati za blokatore segmenta $ad$ su $b$ i $c$; da je $b$ na $ad$, točka $d$ bila bi na $L_1$, pa bi $c, d \in L_1 \cap L_2$ dalo $L_1 = L_2$; isto za $c$ na $ad$. Analogno, blokatori $ae$ ($b, c, d$) i $de$ (nitko, susjedni) ne postoje. Dakle $(a, d, e)$ je trokut, $(b, c)$ par (susjedi), a $P_1..P_{2k-2}$ i $P_{2k+4}..P_n$ imaju paran broj točaka. $\square$</p>
<h3>4. Opći slučaj: uparivanje minimalne cijene</h3>
<p>Bipartitni graf: lijeva kopija $i$ (tko gleda), desna kopija $j$ (koga gleda), brid $(i, j)$, $i \ne j$, s cijenom $0$ (već gleda), $1$ (vidljiv) ili $\infty$. Savršeno uparivanje $\leftrightarrow$ permutacija bez fiksnih točaka po dopuštenim bridovima, a njegova cijena je broj okreta. Mađarski algoritam, $O(n^3) \approx 1.25 \cdot 10^8$. Vidljivost za sve parove u $O(n^2 \log n)$: za fiksni $i$ svaki $j$ svrstaj po normaliziranom smjeru $(P_j - P_i)/\gcd$; vidljiv je samo najbliži u svakom smjeru, a $i$ „već gleda” najbližega u smjeru $v_i/\gcd$.</p>
<h3>5. Kolinearan neparan slučaj ($n \ge 3$)</h3>
<p>Neka je $L$ pravac. Pomičemo točno jedan dron $M$; mora otići <em>izvan</em> $L$ (inače ostaje kolinearno i neparno). Preostale točke, sortirane duž $L$, čine put $Q_0, \dots, Q_{n-2}$ ($n - 1$ paran). $M$ izvan $L$ vidi sve $Q$-ove i oni vide njega (segment $MQ$ siječe $L$ samo u $Q$), a $M$ ne može blokirati ništa na $L$.</p>
<p><strong>Struktura.</strong> Ciklusi koji ne sadrže $M$ su parovi susjeda. Ciklus s $M$ je $M \to Q_i \to Q_{i+1} \to \dots \to Q_j \to M$ ili obrnuti (put $Q_i..Q_j$ mora biti susjedni komad). Lijevo ostaje $i$ točaka, desno $n - 2 - j$; oba broja moraju biti parna: $i$ paran, $j$ neparan (jer je $n - 2$ neparan). Posebno, dvociklus $(M, Q_i)$ nije moguć.</p>
<p><strong>Cijene na pravcu.</strong> Nakon uklanjanja $M$ između $Q_a$ i $Q_{a+1}$ nema nikoga, pa $Q_a$ gleda $Q_{a+1}$ besplatno točno kad je $v_{Q_a} \parallel L$ u pozitivnom smjeru (znak $+1$); analogno znak $-1$ za $Q_{a-1}$. Cijena para $(Q_a, Q_{a+1})$ je $[\text{znak}(Q_a) \ne +1] + [\text{znak}(Q_{a+1}) \ne -1]$; prefiksne sume $\mathrm{L}[i]$ (upareni $Q_0..Q_{i-1}$), $\mathrm{R}[j]$ (upareni $Q_{j+1}..Q_{n-2}$), te prefiksne sume „naprijed” i „natrag” za komad $Q_i..Q_j$.</p>
<p><strong>Cijena za $M$ i njegova gledača $W$</strong> ($T$ = cilj $M$-a, $W$ = zadnji u komadu koji gleda $M$):</p>
<ul>
<li>$M$ bez okreta: $M = P_T - t\, v_M$, $t \gt 0$; moguće samo ako $v_M \nparallel L$ (inače je $M \in L$). Tada je $T$ prvi na zraci $M$-a.</li>
<li>$W$ bez okreta: $M = P_W + s\, v_W$, $s \gt 0$; moguće samo ako $v_W \nparallel L$.</li>
<li>Oboje bez okreta: zrake $P_T - t v_M$ i $P_W + s v_W$ moraju se sjeći. Ako su pravci isti, to je pravac $L$ (sadrži $P_T \ne P_W$) – nevaljano. Inače: $u = -v_M$, $w = v_W$, $D = P_W - P_T$, $N = u \times w \ne 0$; presjek postoji ako $D \cdot N = 0$, a $t\,|N|^2 = (D \times w)\cdot N$, $s\,|N|^2 = (D \times u)\cdot N$ moraju biti $\gt 0$. Vrijednosti dosežu $\sim 10^{25}$, pa <code>__int128</code>.</li>
<li>Ukupno: $0$ ako se zrake sijeku (uz oba uvjeta $\nparallel$), $1$ ako je jedan od dva uvjeta ispunjen (stavi $M$ na tu zraku, drugi se okrene), inače $2$ ($M$ bilo gdje izvan $L$).</li>
</ul>
<p>Odgovor $= \min_{M,\, i,\, j} \big(1000 + \mathrm{L}[i] + \mathrm{R}[j] + \min(\text{naprijed}(i,j) + \text{extra}(T{=}Q_i, W{=}Q_j),\ \text{natrag}(i,j) + \text{extra}(T{=}Q_j, W{=}Q_i))\big)$. Parova $(i, j)$ je $\approx (n/2)^2$, pa je ukupno $O(n^3/4)$ jeftinih operacija ($\approx 0.15$ s).</p>
<h3>6. Zamke</h3>
<ul>
<li>$n = 1 \Rightarrow -1$; $n = 2$ je uvijek kolinearno, ali parno – rješava ga uparivanje.</li>
<li>Cijena $0$ traži da je cilj <em>prvi</em> dron na zraci, ne samo da leži na njoj.</li>
<li>Normalizacija smjera dijeljenjem s $\gcd$ svih triju komponenti (i predznak ostaje!) – ključ za „najbliži u smjeru”.</li>
<li>Kvadrat udaljenosti do $1.2 \cdot 10^{13}$ – <code>long long</code>; skalarni produkti trostrukih produkata – <code>__int128</code>.</li>
<li>U kolinearnom slučaju znak smjera određuj prema referentnom vektoru pravca, a poredak po skalarnom produktu s njim.</li>
</ul>
''',
    'verified': r'''uzorak 1/1; 300 slučajnih malih testova ($n \le 7$: slučajne točke, točke na 1–3 pravca, cijele mreže, svi kolinearni – 65 testova kolinearno-neparnih; smjerovi često ciljaju druge dronove) protiv brute forcea koji ispituje sve derangemente s provjerom vidljivosti, a za slučaj premještanja egzaktno (razlomcima) prolazi kandidatske pozicije na zrakama, njihovim presjecima i generičkoj točki; 11 velikih testova ($n = 497$–$500$, sve vrste) najviše $0.14$ s.''',
},
]
