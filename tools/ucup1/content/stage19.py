# -*- coding: utf-8 -*-
STAGE = {
    'no': 19,
    'name': 'Stage 19: America',
    'source_name': '2022-2023 ICPC North America Championship',
    'no_editorial': True,
    'community': True,
    'source_html': r'''
<p>Zadaci potječu s natjecanja The 2023 ICPC North America Championship (NAC 2023). Tekst zadatka preveden je prema službenim <a href="https://contest.ucup.ac/download.php?type=attachments&amp;id=1248&amp;r=0">engleskim tekstovima zadataka</a>. Organizatori nisu objavili službena rješenja. Zadatak je dostupan na <a href="https://contest.ucup.ac/contest/1248">Universal Cup Judging System</a>.</p>
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
    'solution': None,
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
    'solution': None,
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
    'solution': None,
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
    'solution': None,
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
    'solution': None,
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
    'solution': None,
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
    'solution': None,
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
    'solution': None,
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
    'solution': None,
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
    'solution': None,
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
    'solution': None,
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
    'solution': None,
},
]
