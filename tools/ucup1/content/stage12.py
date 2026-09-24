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
        ('Opažanje', r'''<p>Odabir lista mijenja boju cijelog puta do korijena. Vrh $v$ promijeni boju jednom za svaki odabrani list u svom podstablu, pa mu je konačna boja $A_v \oplus (\text{broj odabranih listova u podstablu} \bmod 2)$. Odabir istog lista dvaput se poništava — bitna je samo parnost.</p>'''),
        ('Redukcija', r'''<p>Svakom vrhu pridružujemo parnost $p_v \in \{0, 1\}$ broja odabranih listova u njegovu podstablu. Za list je $p_v$ slobodna varijabla; za unutarnji vrh $p_v = \bigoplus_{c} p_c$ po djeci $c$. Vrh $v$ je crn ako je $A_v \oplus p_v = 1$. Treba maksimizirati broj crnih vrhova nad svim izborima parnosti listova.</p>'''),
        ('Algoritam i složenost', r'''<p>$dp[v][i]$ = najveći broj crnih vrhova u podstablu $v$ uz $p_v = i$. Za list: $dp[v][i] = [A_v \oplus i = 1]$. Za unutarnji vrh spajaj djecu redom, kao konvoluciju parnosti: $new[i \oplus j] = \max(cur[i] + dp[c][j])$, pa na kraju dodaj $[A_v \oplus i = 1]$. Odgovor je $\max(dp[1][0], dp[1][1])$. Složenost $O(N)$.</p>'''),
    ],
    'solution': r'''
<p>Boja vrha $v$ određena je brojem odabranih listova u podstablu vrha $v$. Budući da odabir dvaju listova vraća boju vrha $v$ u početno stanje, bitno je samo je li iz podstabla vrha $v$ odabran paran ili neparan broj listova.</p>
<p>Zadatak zato rješavamo sljedećim dinamičkim programiranjem po stablu:</p>
<p>$dp[v][i]$ — najveći broj crnih vrhova u podstablu vrha $v$ ako je broj odabranih listova u podstablu vrha $v$ kongruentan $i$ modulo $2$.</p>
<p>Vremenska složenost je $O(N)$.</p>
''',
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
        ('Opažanje', r'''<p>Čarolija je besplatna i neograničena, pa iznos u novčaniku zapravo predstavlja klasu ekvivalencije — multiskup znamenki. Predstavnik klase neka bude najveći broj $m(j)$ koji se iz $j$ može dobiti.</p>'''),
        ('Redukcija', r'''<p>$dp[i][j]$ = najveći broj kupljenih proizvoda nakon $i$ trgovina uz iznos $j$ (normaliziran, $j = m(j)$). Iz $dp[i][j]$: preskoči trgovinu ($dp[i+1][j]$) ili za svaku permutaciju $k \in p(j)$ s $k \ge A_i$ kupi i prijeđi u $dp[i+1][m(k - A_i)]$ s $+1$.</p>'''),
        ('Algoritam i složenost', r'''<p>Brojevi imaju najviše $4$ znamenke, pa $|p(j)| \le 24$. Ukupno $O(N \cdot 10^4 \cdot 24)$ operacija — trivijalno unutar limita. Odgovor je $\max_j dp[N][j]$.</p>'''),
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
        ('Opažanje: donja granica', r'''<p>Duljina bilo kojeg niza nakon $L$ instrukcija je najviše $2^L$, pa $L \ge \lceil \log_2 N \rceil$. U svakoj instrukciji nastaju najviše $4$ nova niza, a svi $N$ prefiksa osim $A[1]$ moraju nastati, pa $L \ge \lceil (N-1)/4 \rceil$. Za $N \le 8$ prva granica je jača i dostiže se (klasična paralelna prefiksna suma), za $N \ge 9$ potrebna je finija analiza (vidi tešku verziju).</p>'''),
        ('Redukcija', r'''<p>Umjesto općeg dokaza za malu verziju, primijeni tablicu iz službenog rješenja i pripremi šest fiksnih programa: $N = 2$ ($L = 1$), $4$ ($2$), $8$ ($3$), $11$ ($4$), $13$ ($5$), $16$ ($6$). Za ulazni $N$ ispiši najmanji od tih programa koji pokriva $N$ — dodatni prefiksi $A[i]$ za $i > N$ ne smetaju.</p>'''),
        ('Algoritam: kako naći programe', r'''<p>Napiši pretraživanje (DFS/BFS s odrezivanjem) nad skupom već izgrađenih intervala $[l, r]$: stanje je skup dostupnih intervala, potez je odabir do $4$ parova susjednih intervala koji se spajaju. Iskoristi opažanje da su korisni samo intervali oblika $[l, r]$ i da se $[1, i]$ mora izgraditi za svaki $i \le N$. Za $N \le 16$ pretraživanje s heuristikom (svaki korak mora „napredovati” prefiksni lanac) brzo pronalazi rješenja; alternativno konstruiraj ručno po ideji blokova iz teške verzije.</p>'''),
    ],
    'solution': r'''
<p>Veza između $N$ i najmanjeg broja instrukcija $L$ je sljedeća:</p>
<table>
    <tr><th>$N$</th><td>$2$</td><td>$3$–$4$</td><td>$5$–$8$</td><td>$9$–$11$</td><td>$12$–$13$</td><td>$14$–$16$</td></tr>
    <tr><th>$L$</th><td>$1$</td><td>$2$</td><td>$3$</td><td>$4$</td><td>$5$</td><td>$6$</td></tr>
</table>
<p>Zadatak se stoga može riješiti pažljivo napisanim programom za iscrpno pretraživanje koji pronalazi rješenja, ili ručnom konstrukcijom rješenja za $N = 2, 4, 8, 11, 13, 16$ (rješenje za veći $N$ ujedno je rješenje za svaki manji $N$ s istim $L$). Službeno rješenje daje i primjer programa za $N = 16$ u šest instrukcija; opća konstrukcija koja dostiže donju granicu opisana je u teškoj verziji zadatka (D).</p>
''',
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
        ('Opažanje: dvije donje granice', r'''<p>(1) Niz nakon $L$ instrukcija ima duljinu $\le 2^L$, dakle $L \ge \log_2 N$. (2) Za $N \ge 9$ dokazujemo $L \ge \frac{2}{5}(N-1)$: korisni su samo nizovi oblika $[l, r]$; svaki nastaje najviše jednom; graf „koji interval iz kojih” je skup binarnih stabala s korijenima $[1,1], \dots, [1, N]$. Dio potreban za $[1, N]$ je binarno stablo $T$ s $2N - 1$ vrhova i $N - 1$ spajanja, u kojem su svaka dva intervala ili disjunktna ili ugniježđena.</p>'''),
        ('Redukcija: kombiniranje granica', r'''<p>Neka je $S$ ukupan broj spajanja, pa $L \ge S/4$. Neka je $A$ broj vrhova oblika $[1, i]$ u $T$; oni ovise jedan o drugom u lancu, pa $L \ge A - 1$ (ako bi se koristio rezultat od prije više od dva koraka, u $T$ bi se pojavili intervali koji se križaju). Za $N - A$ prefiksa koji nisu u $T$ treba još barem po jedno spajanje: $(N-1) + (N-A) \le S$, tj. $A \ge 2N - 1 - S$ i $L \ge 2N - 2 - S$. Zato $L \ge \max(S/4,\ 2N - 2 - S) \ge \frac{2}{5}(N-1)$. Konačno $L = \max\!\left(\lceil \log_2 N \rceil, \lceil \frac{2}{5}(N-1) \rceil\right)$.</p>'''),
        ('Algoritam: konstrukcija koja dostiže granicu', r'''<p>Podijeli $A_1..A_N$ na $L + 1$ blokova. U svakom koraku jedan procesor produžuje globalni prefiks za cijeli sljedeći blok (spajanje $[1, \text{kraj prethodnog}] + [\text{blok}]$), a preostali procesori računaju prefikse unutar blokova i nadopunjuju „sufiksne” dijelove blokova tako da se svaki element $i$ dobije kao $[1, \text{kraj bloka}] + [\text{početak bloka}, i]$ ili izravno. Kako globalni prefiks napreduje po jednom bloku po koraku, blok $k$ smije se „dovršavati” $k$ koraka; zato blokovi rastu s indeksom sve dok kapacitet od $4$ spajanja po koraku dopušta, a ostatak se računa izravno. Programski: simuliraj konstrukciju za dani $N$ i ispiši instrukcije; provjeri lokalno da broj koraka odgovara formuli.</p>'''),
        ('Složenost', r'''<p>Konstrukcija ima $O(L) = O(N)$ instrukcija po $4$ spajanja; izgradnja i ispis su $O(N)$.</p>'''),
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
        ('Opažanje', r'''<p>Zbroj medijana $= \sum_{x} x \cdot (\text{broj petorki u kojima je } x \text{ medijan})$. Za jednake vrijednosti uvedi dosljedno razbijanje neodlučnosti (npr. po indeksu), tako da je „ispred/iza” dobro definirano.</p>'''),
        ('Redukcija', r'''<p>Sortiraj $5N$ parova (vrijednost, oznaka niza). Element $F_k$ s oznakom $t_k$ je medijan petorke točno kad iz preostala četiri niza uzmemo dva elementa s pozicijama $< k$ i dva s pozicijama $> k$. Za odabir para oznaka $\{t_i, t_j\}$ koji su ispred, broj načina je $pre_{t_i}(k) \cdot pre_{t_j}(k) \cdot suf_{t_l}(k) \cdot suf_{t_m}(k)$, gdje su $pre_t(k)$ i $suf_t(k)$ brojevi elemenata s oznakom $t$ ispred, odnosno iza pozicije $k$.</p>'''),
        ('Algoritam i složenost', r'''<p>Sortiranje $O(N \log N)$, zatim jedan prolaz s prefiksnim brojačima po $5$ oznaka i $6$ kombinacija po elementu — $O(N)$. Sve modulo $998244353$.</p>'''),
    ],
    'solution': r'''
<p>Trebamo prebrojati koliko se puta svaka vrijednost pojavljuje kao medijan.</p>
<p>Najprije sortiramo svih $5N$ brojeva zajedno s oznakama koje govore iz kojeg od pet nizova dolaze; neka je $F = ((F_1, t_1), \dots, (F_{5N}, t_{5N}))$ sortirani niz, gdje je $t_i$ oznaka. Za svaki $k = 1, \dots, 5N$ trebamo prebrojati četvorke $(i, j, l, m)$ takve da je $1 \le i < j < k < l < m \le 5N$ i $\{t_i, t_j, t_k, t_l, t_m\} = \{A, B, C, D, E\}$. To možemo izračunati u $O(1)$ po $k$ enumeracijom svih parova $\{t_i, t_j\}$ i korištenjem prefiksnih zbrojeva (brojača po oznakama).</p>
<p>Vremenska složenost je $O(N \log N)$.</p>
''',
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
        ('Opažanje: prijelaz na vjerojatnosti', r'''<p>Zbroj po svim $2^{N-1}$ podskupova $= 2^{N-1} \cdot \mathbb{E}[\text{rezultat}]$ kad se svaki brid neovisno zadrži s vjerojatnošću $1/2$. Rezultat je zbroj po komponentama, a svaka komponenta ima jedinstveni <em>najplići</em> vrh $v$ (najbliži korijenu). Zato $\mathbb{E}[\text{rezultat}] = \sum_v \mathbb{E}[\min \text{komponente s najpličim vrhom } v]$, gdje je doprinos vrha $v$ pomnožen s vjerojatnošću $1/2$ da je brid prema roditelju prerezan (za korijen $1$).</p>'''),
        ('Redukcija: DP s distribucijom minimuma', r'''<p>$dp[v][x]$ = vjerojatnost da komponenta koja sadrži $v$ unutar podstabla $T_v$ ima minimum $x$. Početno $dp[v][A_v] = 1$. Dodavanje djeteta $c$: s vjerojatnošću $1/2$ brid je prerezan (distribucija ostaje), s $1/2$ komponente se spajaju i minimum postaje $\min(x, y)$ — to je „min-konvolucija” dviju distribucija, izračunljiva prefiksnim zbrojevima nad sortiranim ključevima u vremenu linearnom u broju ključeva. Odgovor: $\sum_v [\text{brid prema roditelju prerezan}] \cdot \sum_x x \cdot dp[v][x]$.</p>'''),
        ('Algoritam: efikasno spajanje', r'''<p>Ključeva u $dp[v]$ je najviše $size(v)$. Spajanje dvaju djece u $O(size(c_1) + size(c_2))$ i spajanje po parovima (kao merge-sort po djeci) daje $O(N \log N)$. Alternative: spajanje segmentnih stabala s lijenim množenjem (segment tree merge, $O(N \log A)$ uz optimizaciju) ili top tree sa četiri komponente podataka u $O(N \log N)$.</p>'''),
        ('Složenost', r'''<p>$O(N \log N)$ uz spajanje po parovima; sve u modularnoj aritmetici s inverzom broja $2$.</p>'''),
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
        ('Opažanje', r'''<p>Uvjet zabranjuje $P_i$ u istom bloku kao $i$. Direktno brojanje je teško, ali komplementarne događaje („pozicija $i$ ima vrijednost iz svog bloka”) lako je brojati — klasična situacija za uključivanje–isključivanje.</p>'''),
        ('Redukcija', r'''<p>Fiksiraj $(k_0, \dots, k_{N-1})$: u bloku $j$ odaberi $k_j$ pozicija ($\binom{M}{k_j}$) i dodijeli im različite vrijednosti iz bloka $j$ ($M!/(M-k_j)!$); preostalih $NM - \sum k_j$ pozicija popuni proizvoljno ($(NM - \sum k_j)!$). Uključivanje–isključivanje: $\text{odgovor} = \sum_{(k_j)} (-1)^{\sum k_j} (NM - \sum k_j)! \prod_j \frac{M!}{((M-k_j)!)^2 k_j!}$.</p>'''),
        ('Algoritam', r'''<p>Ovisnost o blokovima ide samo kroz $s = \sum k_j$. Definiraj $f(x) = \sum_{k=0}^{M} \frac{M!}{((M-k)!)^2 k!} (-x)^k$ i $g = f^N$ (potenciranje polinoma NTT-om, stupanj $NM \le 10^6$). Odgovor je $\sum_{s} (NM - s)! \, [x^s] g(x)$.</p>'''),
        ('Složenost', r'''<p>$O(NM \log(NM))$ uz NTT (npr. $\log$/$\exp$ polinoma ili binarno potenciranje s dijeljenjem stupnja).</p>'''),
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
        ('Opažanje: Ehrhartov polinom', r'''<p>Za konveksni politop $P$ s cjelobrojnim vrhovima, $L(k) = |kP \cap \mathbb{Z}^3|$ je polinom u $k$ stupnja $3$ (Ehrhart). Dakle odgovor $L(K)$ dobivamo iz $L(0) = 1$, $L(1)$, $L(2)$, $L(3)$ Lagrangeovom interpolacijom, modulo $998244353$ (uz $K \bmod p$).</p>'''),
        ('Redukcija: računanje $L(k)$ za male $k$', r'''<p>Konstruiraj ravnine 3D konveksne ljuske: za svaku trojku nekolinearnih točaka uzmi ravninu i provjeri leže li sve točke s iste strane — $O(N^4)$, dovoljno za $N \le 100$. Zatim za $k \in \{1, 2, 3\}$ i za svaki cjelobrojni par $(x, y)$ s $|x|, |y| \le kX$ (gdje $X = \max |\text{koord}|$) izračunaj interval $z$ koji leži unutar svih poluprostora (za svaku ravninu dobivaš gornju ili donju granicu za $z$, ili uvjet neovisan o $z$) i pribroji broj cijelih $z$.</p>'''),
        ('Algoritam i složenost', r'''<p>$O(N^4)$ za ljusku (ili $O(N^2)$ pravim 3D hull algoritmom) plus $O(F \cdot X^2)$ za brojanje, gdje je $F$ broj ravnina ljuske. S $X \le 600$ i $F \le 2N$ to je oko $10^8$ jednostavnih operacija — unutar $4$ s. Interpolacija je $O(1)$.</p>'''),
        ('Alternativa', r'''<p>Umjesto $k = 1, 2, 3$ dovoljno je za $k = 1$ znati volumen (vodeći koeficijent), $L(1)$ i broj strogo unutarnjih točaka $L(-1)$ po reciprocnosti ($L(-k) = (-1)^3 \cdot |\text{int}(kP) \cap \mathbb{Z}^3|$); uz $L(0) = 1$ to su četiri uvjeta. S dodatnim trudom složenost pada na $O(N \log N + NX \log X)$.</p>'''),
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
        ('Opažanje', r'''<p>Neriješene kombinacije: $RRR, PPP, SSS, RPS, PSR, SRP, RSP, PRS, SPR$ (redom oznake $1..9$). Ako se vrsta $t$ pojavljuje $X_t$ puta, rasporeda je $\frac{N!}{X_1! \cdots X_9!}$. Treba zbrojiti to po svim $(X_t)$ koji poštuju kvote igrača.</p>'''),
        ('Redukcija: rješavanje sustava', r'''<p>Kvote daju $9$ jednadžbi (npr. $X_1 + X_4 + X_7 = A_R$, $X_2 + X_5 + X_8 = A_P$, …), ali sustav ima rang $7$. Uvedi $Y_2 = X_2 - X_1$, $Y_3 = X_3 - X_1$, $Y_5 = X_5 - X_4$, $Y_6 = X_6 - X_4$, $Y_8 = X_8 - X_7$, $Y_9 = X_9 - X_7$; dobiva se regularni $6 \times 6$ sustav s desnom stranom $(A_P - A_R, A_S - A_R, B_P - B_R, \dots)$, pa su $Y$-i jedinstveni (moraju biti cijeli, inače odgovor $0$). Preostaju slobodni $x_1, x_4, x_7 \ge$ donje granice (da svi $X_t \ge 0$) sa zbrojem $C$.</p>'''),
        ('Algoritam: konvolucija', r'''<p>Traži se $N! \sum_{x_1 + x_4 + x_7 = C} a(x_1)\, b(x_4)\, c(x_7)$, gdje je $a(x) = \frac{1}{x!(x+Y_2)!(x+Y_3)!}$ za dopuštene $x$ (inače $0$), analogno $b, c$. Dvije konvolucije NTT-om nad nizovima duljine $O(N)$ i uzmi koeficijent uz $C$.</p>'''),
        ('Složenost', r'''<p>$O(N \log N)$ uz predizračunate faktorijele do $N$ (i inverze).</p>'''),
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
        ('Opažanje', r'''<p>Uvjet $A_{i-1} + A_{i+1} \ge 2A_i$ znači da su točke $(i, A_i)$ konveksne (grafikon niza je konveksna funkcija). Skup konveksnih nizova ograničenih odozgo s $R$ ima najveći element: donju konveksnu ljusku točaka $(i, R_i)$, jer je ona konveksna, $\le R$, i svaki konveksan niz $\le R$ leži ispod nje (konveksna funkcija ispod točaka je ispod njihove donje ljuske).</p>'''),
        ('Redukcija', r'''<p>Neka je $T_i$ vrijednost donje ljuske u $x = i$. Rješenje postoji ako i samo ako $L_i \le T_i$ za sve $i$: ako vrijedi, $A = T$ je rješenje; ako ne, za neki $i$ je $A_i \le T_i < L_i$ za svaki dopušteni $A$.</p>'''),
        ('Algoritam i složenost', r'''<p>Andrewov monotoni lanac nad točkama $(1, R_1), \dots, (N, R_N)$ (već sortirane po $x$) daje donju ljusku u $O(N)$; za svaki $i$ između dvaju vrhova ljuske izračunaj $T_i$ linearnom interpolacijom i usporedi s $L_i$ — radi razlomaka usporedbu izvedi u cijelim brojevima (množenjem s razlikom apscisa), 64-bitno je dovoljno.</p>'''),
    ],
    'solution': r'''
<p>Neka je $S$ konveksna ljuska skupa točaka $\{(i, y) \mid y \ge R_i\}$ i definirajmo niz $T$ s $T_i = \min\{y \mid (i, y) \in S\}$ — drugim riječima, $T$ je donja konveksna ljuska niza $R$.</p>
<p>Tako dobiveni $T$ je „najveći” niz koji zadovoljava sve uvjete zadatka osim uvjeta koji se tiče $L$. Preciznije, za svaki niz $A$ koji zadovoljava $A_i \le R_i$ za sve $i$ i $A_{i-1} + A_{i+1} \ge 2A_i$ za sve $2 \le i \le N-1$ vrijedi $A_i \le T_i$; to slijedi iz definicije konveksne ljuske.</p>
<p>Stoga je odgovor Yes ako $T$ zadovoljava $L_i \le T_i$ za sve $i$, a inače No. Niz $T$ računamo u $O(N)$ npr. Andrewovim algoritmom monotonog lanca.</p>
''',
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
        ('Opažanje', r'''<p>Indeksiraj od $0$. Aritmetički niz $A_i = A_0 + id$ zadovoljava uvjete ako i samo ako za svaki $i$ vrijedi $L_i - id \le A_0 \le R_i - id$, tj. $\ell(d) := \max_i (L_i - id) \le A_0 \le u(d) := \min_i (R_i - id)$. Broj rješenja $= \sum_{d \in \mathbb{Z}} \max(0, \lfloor u(d) \rfloor - \lceil \ell(d) \rceil + 1)$; kako su $L, R$ cijeli, $\ell$ i $u$ su cijeli za cijeli $d$.</p>'''),
        ('Redukcija: ovojnice', r'''<p>$\ell(d)$ je gornja ovojnica pravaca s nagibima $-i$ (već sortirani po nagibu!), pa se računa monotonim stogom u $O(N)$ (CHT). Analogno $u(d)$ je donja ovojnica. Obje su izlomljene linije s $O(N)$ segmenata. Raspon relevantnih $d$ je ograničen (npr. $|d| \le \max R$), a izvan područja gdje je $\ell \le u$ doprinos je $0$.</p>'''),
        ('Algoritam', r'''<p>Spoji točke loma obje ovojnice u sortirani niz lomova; na svakom intervalu $[d_1, d_2]$ između uzastopnih lomova $\ell$ i $u$ su linearne s cjelobrojnim koeficijentima (nagib $-i$, odsječak $L_i$ ili $R_i$). Broj cjelobrojnih točaka je $\sum_{d = d_1}^{d_2} (u(d) - \ell(d) + 1)$ ograničeno na dio gdje je razlika $\ge 0$; kako je $u - \ell$ linearna na intervalu, nul-točku nađi dijeljenjem, a zatim zbroj aritmetičkog niza u $O(1)$ (koristi 128-bitne brojeve ili modularnu aritmetiku s oprezom jer vrijednosti dosežu $10^{12} \cdot 3 \cdot 10^5$).</p>'''),
        ('Složenost', r'''<p>$O(N)$ nakon što uočimo da su nagibi već sortirani; s sortiranjem lomova $O(N \log N)$ također prolazi.</p>'''),
    ],
    'solution': r'''
<p>Radi jednostavnosti indeksiramo $L$, $R$ i $A$ od nule i označimo $X = \max_i R_i$.</p>
<p>Fiksirajmo razliku $d$. Dopušteni raspon početnog člana $A_0$ je</p>
<p>$$\max_i \{ -id + L_i \} \le A_0 \le \min_i \{ -id + R_i \}.$$</p>
<p>Za svaki $i$ je $-id + L_i$ linearna funkcija u $d$, pa je maksimum tih funkcija, $\max_i \{-id + L_i\}$, po dijelovima linearna krivulja konveksna prema dolje u varijabli $d$. Nju možemo izračunati u $O(N)$ tehnikom poput Convex Hull Tricka. Slično, uvjeti za $R$ tvore po dijelovima linearnu krivulju konkavnu prema gore.</p>
<p>Treba prebrojati cjelobrojne točke u područje omeđenom tim dvjema po dijelovima linearnim funkcijama. Podijelimo li raspon $d$ na $O(N)$ intervala na prikladan način, područje se rastavlja na trapeze, a broj cjelobrojnih točaka u svakom trapezu računamo u $O(1)$.</p>
<p>Vremenska složenost je $O(N)$.</p>
''',
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
        ('Opažanje: simetrija', r'''<p>Raspišimo $\prod_i (x_i + A_i) = \sum_{S \subseteq [N]} \prod_{i \in S} x_i \prod_{i \notin S} A_i$. Skup $X$ je invarijantan na permutacije koordinata, pa $\sum_{X} \prod_{i \in S} x_i$ ovisi samo o $k = |S|$. Označimo $S_k = \sum_{x_1 \cdots x_N = M} x_1 x_2 \cdots x_k$. Tada je odgovor $\sum_{k=0}^{N} B_k S_k$, gdje je $B_k = [x^k] \prod_i (x + A_i)$.</p>'''),
        ('Redukcija: multiplikativnost', r'''<p>$P \mapsto \sum_{x_1 \cdots x_N = P} x_1 \cdots x_k$ je multiplikativna funkcija (faktorizacija $x_i$ po prostim brojevima je neovisna po prostim faktorima). Za $M = \prod_j p_j^{e_j}$: $S_k = \prod_j S_k(p_j^{e_j})$. Za prostu potenciju $p^e$: raspodijeli $e$ jedinica eksponenta na $N$ mjesta; ako $d$ jedinica padne na prvih $k$ mjesta, faktor je $p^d$, a broj raspodjela je $\binom{d+k-1}{k-1}\binom{e-d+N-k-1}{N-k-1}$.</p>'''),
        ('Algoritam', r'''<p>1) Faktoriziraj $M$ probnim dijeljenjem do $\sqrt{M} = 10^6$. 2) Izračunaj $B_0..B_N$ množenjem $N$ linearnih polinoma metodom dijeli-pa-vladaj s NTT-om: $O(N \log^2 N)$. 3) Za svaki $k$ i svaki prosti faktor izračunaj $S_k(p^e)$ zbrojem po $d = 0..e$ (ukupno $O(N \log M)$ jer $\sum e_j \le \log_2 M$); rubni slučajevi $k = 0$: $\binom{e+N-1}{N-1}$, $k = N$: $p^e \binom{e+N-1}{N-1}$. 4) Zbroji $B_k S_k$.</p>'''),
        ('Složenost', r'''<p>$O(N \log^2 N + \sqrt{M} + N \log M)$ uz predizračunate faktorijele do $N + \log M$.</p>'''),
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
        ('Opažanje', r'''<p>Dva vrha iste SCC imaju puteve u oba smjera, pa cijelu SCC obojimo isto. Nakon kondenzacije dobivamo DAG; skup vrhova iste boje mora biti totalno uređen relacijom dostižnosti — tj. <em>lanac</em>. Minimalan broj boja = minimalno pokrivanje DAG-a lancima = (Dilworth) najveći antilanac; algoritamski, minimalno pokrivanje putevima u tranzitivnom zatvaraču.</p>'''),
        ('Redukcija: pokrivanje putevima bez zatvarača', r'''<p>Klasično: broj puteva $= N' - \nu$, gdje je $\nu$ najveće sparivanje u bipartitnom grafu $(U, V)$ s bridom $U_i V_j$ za svaki brid $i \to j$ tranzitivnog zatvarača. Zatvarač može imati $\Theta(N^2)$ bridova — ne stane u $64$ MB. Trik: u mreži toka dopusti da put prolazi kroz već pokriveni vrh dodavanjem bridova $U_i \to V_i$ neograničenog kapaciteta; tok tada simulira puteve u zatvaraču koristeći samo izvorne bridove.</p>'''),
        ('Algoritam', r'''<p>Vrhovi mreže: $src, dst, U_1..U_N, V_1..V_N$. Bridovi: $src \to V_i$ (kapacitet $1$), $U_i \to dst$ ($1$), $V_{A_j} \to U_{B_j}$ ($\infty$) za svaki brid DAG-a, $U_i \to V_i$ ($\infty$). Najveći tok $\nu$ nađi Ford–Fulkersonom (najviše $N$ augmentacija po $O(N + M)$) — $O(N(N + M))$ vremena i $O(N + M)$ memorije. Zatim rekonstruiraj lance: iz toka na bridovima $V_{A} \to U_{B}$ i $U \to V$ prati kamo „ide” svaki vrh (tok kroz $U_i \to V_i$ znači da lanac prolazi kroz $i$ bez da $i$ bude njegov član — $i$ je već pokriven drugim lancem), dodjeljujući boje u $O(N^2)$ vremena i $O(N)$ memorije. Na kraju boje SCC-ova proširi na izvorne vrhove.</p>'''),
        ('Složenost', r'''<p>$O(N(N + M))$ vremena, $O(N + M)$ memorije — u skladu s limitom od $64$ MB.</p>'''),
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
        ('Opažanje: struktura uvjeta', r'''<p>$C \oplus D < K$: promatraj bitove od najvišeg. Na prvom bitu gdje se $C \oplus D$ i $K$ razlikuju, $K$ mora imati $1$, a $C \oplus D$ nulu. Za svaki bit $b$ na kojem $K$ ima $1$, skup $D$ koji se s $K$ podudaraju iznad $b$ (u XOR-u s $C$) i imaju $0$ na $b$ je jedan interval duljine $2^b$ u prostoru $D$ (potomci čvora binarnog trie-a). Dakle najviše $30$ intervala po bridu.</p>'''),
        ('Redukcija: offline dinamička povezanost', r'''<p>Sortiraj $D_1..D_Q$; brid $j$ je „prisutan” u upitima čiji $D$ pada u neki od njegovih intervala — to je unija najviše $30$ segmenata u indeksima upita (binarno pretraživanje granica). Dobivamo do $30M$ dodavanja/brisanja bridova na vremenskoj osi duljine $Q$; treba za svaki trenutak broj povezanih parova.</p>'''),
        ('Algoritam', r'''<p>Segmentno stablo nad vremenom $[1, Q]$; svaki interval prisutnosti brida stavi u $O(\log Q)$ čvorova. DFS po stablu: pri ulasku u čvor spoji sve njegove bridove u DSU-u (bez sažimanja putova, s union by size, uz stog promjena), ažurirajući $ans \mathrel{+}= sz_a \cdot sz_b$; u listu zabilježi odgovor za upit; pri izlasku poništi spajanja (rollback). Svaki brid-interval spaja se $O(\log Q)$ puta, spajanje košta $O(\log N)$.</p>'''),
        ('Složenost', r'''<p>$O((Q + M \log N) \log \text{MAX})$ prema službenom rješenju, praktično $O(30 M \log Q \log N)$ — s $M = 10^5$ to je oko $10^9$ jednostavnih operacija, pa treba pažljiva implementacija (limit je $3$ s).</p>'''),
    ],
    'solution': r'''
<p>Promatramo $D = 0, 1, \dots, 2^{30} - 1$ redom. Za svaki brid $j$ skup vrijednosti $D$ takvih da je $(C_j \oplus D) < K$ rastavlja se na najviše $30$ intervala. Time se zadatak svodi na <strong>offline dinamičku povezanost</strong> s $30M$ dodavanja i brisanja bridova.</p>
<p>To rješavamo DSU-om s poništavanjem (rollback) i dijeli-pa-vladaj postupkom po vremenu (segmentno stablo nad upitima sortiranim po $D$), održavajući pritom broj povezanih parova $\sum \binom{sz}{2}$.</p>
<p>Vremenska složenost je $O((Q + M \log N) \log \mathrm{MAX})$.</p>
''',
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
        ('Opažanje', r'''<p>Vrijednost stanja definiramo kao buduću razliku (s gledišta igrača na potezu). Prijelaz koji uzima dragulj $w$ vodi u manji skup i daje $w - \text{val}(\text{sljedeće stanje})$ (negacija jer se perspektiva mijenja). Prijelazi bez dragulja ostaju u istom skupu — tu su ciklusi.</p>'''),
        ('Redukcija: rješavanje jednog sloja', r'''<p>Za fiksni skup dragulja $S$ imamo graf stanja $(p, q)$ s poznatim vrijednostima izlaza u manje skupove. Igrač na potezu bira maksimum po izlazima. Retrogradna analiza: (1) stanje čije su sve opcije određene dobiva vrijednost $\max$ (u perspektivi igrača, uz negaciju za protivnika). (2) Ako ostaju neodređena stanja, pogledaj sva određena odredišta iz njih; ako neka daje strogo pozitivnu vrijednost, igrač će je sigurno uzeti (bolje od bilo kakvog ciklusa koji vrijedi $0$) — odredi to stanje s najvećom takvom vrijednošću i ponovi. (3) Kad više nema pozitivnih izlaza, sva preostala stanja imaju vrijednost $0$ (optimalno je ostati u ciklusu / ponoviti stanje).</p>'''),
        ('Algoritam', r'''<p>Obradi skupove $S$ po rastućem broju elemenata ($2^K$ slojeva). U svakom sloju vodi brojač neodređenih izlaza po stanju i prioritetni red (max-heap) kandidata; sljedeće stanje za određivanje je ono s najvećom određenom vrijednošću izlaza, čim je ona pozitivna ili su svi izlazi određeni. Zapamti da u sloju stanja s najvećom vrijednošću treba obrađivati globalno silazno, čime se opravdava korak (2). Odgovor je vrijednost početnog stanja (svi dragulji, Alice u $A$, Bob u $B$).</p>'''),
        ('Složenost', r'''<p>$O(2^K \cdot N \cdot (N + M) \log N)$ — s $K \le 10$ i $N \le 30$ sasvim dovoljno.</p>'''),
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
},
]
