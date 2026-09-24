"""1st Universal Cup – Stage 6: Taiwan. Uvezeno iz ručno pisanih stranica (import_legacy.py); naputci i
trenerski koraci iz nekadašnjeg retro_stage6.py."""

STAGE = {
    'no': 6,
    'name': 'Stage 6: Taiwan',
    'source_name': 'The 2022 ICPC Asia Taoyuan Regional Contest',
    'source_html': r'''
<p>Prijevod službenih uputa za rješavanje autorskog tima ICPC Taoyuan regionalnog natjecanja 2022: <a href="https://contest.ucup.ac/download.php?type=attachments&amp;id=1124&amp;r=1">Solution Sketches (en)</a>. Službene upute su vrlo sažete, pa su i prijevodi rješenja kratki. Tekst zadatka preveden je prema službenim <a href="https://contest.ucup.ac/download.php?type=attachments&amp;id=1124&amp;r=0">engleskim tekstovima zadataka</a>. Zadatak je dostupan na <a href="https://contest.ucup.ac/contest/1124">Universal Cup Judging System</a>.</p>
''',
}

PROBLEMS = [
{
    'letter': 'A',
    'title': 'Simplified Genome Translation',
    'title_hr': 'Pojednostavljena translacija genoma',
    'slug': 'A_simplified_genome_translation',
    'tl': '3 s',
    'ml': '1024 MB',
    'statement': r'''
<p>Translacija pretvara mRNA u protein: svaka se tri RNA nukleotida (kodon) prema kodonskoj tablici prevode u jednu aminokiselinu. Na primjer, za $R = $ <code>CUCAGCGUUACCUAGUUUCAUUGUGCU</code> kodoni su <code>CUC AGC GUU ACC UAG ...</code>, a rezultat je $P = $ <code>LSVT</code>, jer je <code>UAG</code> jedan od tri stop-kodona (<code>UAA</code>, <code>UAG</code>, <code>UGA</code>) koji zaustavljaju translaciju.</p>
<h3>Ulaz</h3>
<p>Broj testnih primjera $T$ ($1 \le T \le 50$), zatim po jedan RNA niz $R$ nad alfabetom $\{A, C, G, U\}$ po primjeru; $|R| = 3n$, $1 \le n \le 333$. Stop-kodon nikad nije na početku.</p>
<h3>Izlaz</h3>
<p>Za svaki primjer ispiši prevedeni niz aminokiselina $P$ (do prvog stop-kodona ili do kraja niza).</p>
''',
    'hints': [
        r'''
<p>Tablica kodona ima $64$ unosa — upiši je u mapu <code>string → char</code> i čitaj niz po tri znaka.</p>
''',
        r'''
<p>Stani na prvom stop-kodonu (<code>UAA</code>, <code>UAG</code>, <code>UGA</code>) ili na kraju niza.</p>
''',
    ],
    'coach': [
        ('Opažanje: čista simulacija',
         r'''
<p>Nema algoritamske dubine; sav rizik je u točnom prepisivanju kodonske tablice iz teksta zadatka. Kodon $\to$ aminokiselina je funkcija, pa je <code>unordered_map</code>/<code>map</code> ili $4^3$ tablica indeksirana bazom $4$ prirodan izbor.</p>
'''),
        ('Redukcija: petlja po trojkama',
         r'''
<p>Za $i = 0, 3, 6, \dots$: uzmi $R[i..i+2]$; ako je stop, prekini; inače dodaj slovo. Stop-kodon nije nikad na početku, pa izlaz nije prazan.</p>
'''),
        ('Složenost',
         r'''
<p>$O(|R|)$ po primjeru.</p>
'''),
    ],
    'solution': r'''
<p>Translaciju implementiramo tablicom raspršivanja (hash-mapom) u kojoj su ključevi kodoni mRNA, a vrijednosti odgovarajuće aminokiseline. Niz čitamo po tri znaka i prevodimo dok ne naiđemo na stop-kodon.</p>
''',
},
{
    'letter': 'B',
    'title': 'Multi-Ladders',
    'title_hr': 'Više ljestava',
    'slug': 'B_multi_ladders',
    'tl': '4 s',
    'ml': '1024 MB',
    'statement': r'''
<p>Neonski natpis sastoji se od $k$ ljestvi: graf ljestava $L_n = P_n \times P_2$ ima $2n$ vrhova i $3n - 2$ bridova. Okvir je pravilni $k$-terokut $C_k$, a svaki brid $k$-terokuta poklapa se s gornjim bridom jedne ljestve $L_n$. Dobiveni graf $G$ treba <i>ispravno</i> obojiti s najviše $\lambda$ boja (susjedni vrhovi različitih boja); vrhovi su označeni, pa se bojanja razlikuju kao funkcije. Izračunaj broj ispravnih bojanja modulo $10^9 + 7$.</p>
<h3>Ulaz</h3>
<p>Broj testnih primjera $L$ ($L \le 20$), zatim po retku $n$, $k$, $\lambda$ ($1 \le n \le 10^9$, $3 \le k \le 10^9$, $0 \le \lambda \le 10^9$).</p>
<h3>Izlaz</h3>
<p>Za svaki primjer broj ispravnih bojanja modulo $10^9 + 7$.</p>
''',
    'hints': [
        r'''
<p>Kromatski polinom: brisanje–kontrakcija na gornjem bridu ljestvi daje $P(L_n) = \lambda(\lambda-1)(\lambda^2 - 3\lambda + 3)^{n-1}$; za ciklus $P(C_k) = (\lambda-1)^k + (-1)^k(\lambda-1)$.</p>
''',
        r'''
<p>Lijepljenje dvaju grafova po zajedničkom bridu: $P(G_1 \cup G_2) = \frac{P(G_1)P(G_2)}{\lambda(\lambda-1)}$. Zalijepi $k$ ljestvi na $C_k$: $P = P(C_k)\,(\lambda^2 - 3\lambda + 3)^{k(n-1)}$ — dijeljenje se pokrati.</p>
''',
    ],
    'coach': [
        ('Opažanje 1: bojanja = kromatski polinom',
         r'''
<p>Broj ispravnih bojanja s $\le \lambda$ boja je polinom u $\lambda$. Graf je „ciklus s $k$ ljestvi zalijepljenih po bridovima” — gradi ga iz jednostavnih blokova.</p>
'''),
        ('Opažanje 2: ljestve rekurzivno',
         r'''
<p>Ukloni gornji brid $uv$ ljestvi visine $n$: $P(G - uv) = (\lambda-1)^2 P(L_{n-1})$ (dva viseća lista). Kontrahiraj: stopljeni vrh tvori trokut s gornjim bridom $L_{n-1}$: $P(G/uv) = (\lambda - 2) P(L_{n-1})$. Razlika: faktor $\lambda^2 - 3\lambda + 3$ po katu, baza $\lambda(\lambda-1)$.</p>
'''),
        ('Opažanje 3: lijepljenje po bridu',
         r'''
<p>Ako je $G_1 \cap G_2 = K_2$, bojanje $G$ je par bojanja koja se slažu na zajedničkom bridu; od $\lambda(\lambda-1)$ mogućih boja brida svako je jednako vjerojatno, otud dijeljenje. Ukupno: $P(C_k)\cdot\bigl(P(L_n)/(\lambda(\lambda-1))\bigr)^k$.</p>
'''),
        ('Algoritam i složenost',
         r'''
<p>Brzo potenciranje mod $10^9+7$: $\bigl((\lambda-1)^k + (-1)^k(\lambda-1)\bigr)\cdot(\lambda^2-3\lambda+3)^{k(n-1)}$; eksponent $k(n-1)$ do $10^{18}$ — koristi 64-bitni ili reduciraj mod $p-1$. Pazi na $\lambda \in \{0, 1, 2\}$: formula je i dalje točna (daje $0$ za $\lambda \le 1$, a za $\lambda=2$ ovisi o parnosti $k$).</p>
'''),
    ],
    'solution': r'''
<p>Neka je $P(G, \lambda)$ <b>kromatski polinom</b> grafa $G$ — broj ispravnih bojanja s najviše $\lambda$ boja.</p>
<p><b>Ljestve.</b> Primijenimo rekurziju brisanja i kontrakcije na gornji brid $uv$ ljestava $G_n = L_n$: $P(G_n, \lambda) = P(G_n - uv, \lambda) - P(G_n / uv, \lambda)$. Graf $G_n - uv$ su ljestve visine $n - 1$ s dva viseća vrha na vrhu; svaki od njih boji se na $\lambda - 1$ načina (mora se razlikovati samo od vrha na koji je pričvršćen), pa je $P(G_n - uv, \lambda) = (\lambda - 1)^2 P(G_{n-1}, \lambda)$. U $G_n / uv$ dva gornja vrha stopljena su u jedan koji s gornjim bridom $G_{n-1}$ tvori trokut, pa je $P(G_n / uv, \lambda) = (\lambda - 2) P(G_{n-1}, \lambda)$. Slijedi
$$P(G_n, \lambda) = \bigl((\lambda - 1)^2 - (\lambda - 2)\bigr) P(G_{n-1}, \lambda) = (\lambda^2 - 3\lambda + 3)\, P(G_{n-1}, \lambda).$$
Ljestve visine $1$ su put s dva vrha i imaju $\lambda(\lambda - 1)$ bojanja, dakle
$$P(L_n, \lambda) = \lambda(\lambda - 1)(\lambda^2 - 3\lambda + 3)^{\,n-1}. \tag{1}$$</p>
<p><b>Ciklus.</b> Kromatski polinom ciklusa $C_k$ dobro je poznat:
$$P(C_k, \lambda) = (\lambda - 1)^k + (-1)^k (\lambda - 1). \tag{2}$$</p>
<p><b>Lijepljenje po bridu.</b> Ako je $G = G_1 \cup G_2$ i $G_1 \cap G_2 = K_2$ (zajednički je točno jedan brid), tada
$$P(G, \lambda) = \frac{P(G_1, \lambda) \cdot P(G_2, \lambda)}{\lambda(\lambda - 1)}. \tag{3}$$</p>
<p><b>Algoritam.</b> Krenemo od $G_0 = C_k$ i $k$ puta zalijepimo po jednu ljestvu $L_n$ na brid $k$-terokuta pomoću (3), koristeći (1) i (2):
$$P(G, \lambda) = P(C_k, \lambda) \cdot \left(\frac{P(L_n, \lambda)}{\lambda(\lambda - 1)}\right)^{k} = \bigl((\lambda - 1)^k + (-1)^k(\lambda - 1)\bigr)\,(\lambda^2 - 3\lambda + 3)^{k(n-1)}.$$
Vrijednost računamo brzim potenciranjem modulo $10^9 + 7$ (pri čemu treba paziti na dijeljenje: u konačnoj formuli ono se pokrati, pa dijeljenja modulo zapravo nema).</p>
''',
},
{
    'letter': 'C',
    'title': 'Distance Calculator',
    'title_hr': 'Računanje udaljenosti',
    'slug': 'C_distance_calculator',
    'tl': '3 s',
    'ml': '1024 MB',
    'statement': r'''
<p>Kraljevstvo ima $n!$ gradova; svaki je kodiran permutacijom $d_1 d_2 \dots d_n$ brojeva $1, \dots, n$, a dvorac je u gradu $1\,2\,\dots\,n$. Gradovi $A$ i $B$ spojeni su cestom duljine $1$ ako se njihovi kodovi razlikuju točno u zamjeni dva susjedna elementa ($a_i = b_{i+1}$, $b_i = a_{i+1}$, ostalo jednako). Za zadani grad izračunaj udaljenost do dvorca.</p>
<h3>Ulaz</h3>
<p>Broj primjera $m$ ($1 \le m \le 50$); za svaki $n$ ($3 \le n \le 100$) i permutacija.</p>
<h3>Izlaz</h3>
<p>Za svaki primjer udaljenost zadanog grada do dvorca.</p>
''',
    'hints': [
        r'''
<p>Brid = zamjena susjednih elemenata. Koju veličinu jedna takva zamjena mijenja za točno $\pm 1$?</p>
''',
        r'''
<p>Broj inverzija: donja ograda zbog $\pm 1$, a bubble sort pokazuje da je dostiživa.</p>
''',
    ],
    'coach': [
        ('Opažanje 1: invarijanta',
         r'''
<p>Zamjena susjednih $a_i \gt a_{i+1}$ smanjuje broj inverzija za točno $1$; suprotna ga povećava za $1$. Dakle udaljenost $\ge \#\text{inv}$.</p>
'''),
        ('Opažanje 2: dostižnost',
         r'''
<p>Bubble sort uvijek nađe susjedni par u krivom poretku dok permutacija nije sortirana, pa se $\#\text{inv}$ zamjena i postiže. Udaljenost $= \#\text{inv}$.</p>
'''),
        ('Algoritam',
         r'''
<p>$n \le 100$: dvostruka petlja $O(n^2)$ (ili BIT za veće $n$).</p>
'''),
    ],
    'solution': r'''
<p>Svaki je grad vrh grafa $G = (V, E)$, a bridovi odgovaraju zamjeni dva susjedna broja. Udaljenost do dvorca (sortirane permutacije) jednaka je najmanjem broju zamjena susjednih elemenata potrebnom za sortiranje, a taj broj daje algoritam <b>sortiranja mjehuričastim postupkom</b> (bubble sort) — jednak je broju inverzija u permutaciji. Uz $n \le 100$ dovoljno je jednostavno prebrojati parove $(i, j)$, $i &lt; j$, s $d_i &gt; d_j$.</p>
''',
},
{
    'letter': 'D',
    'title': 'Tangle: A DAG for storing transactions',
    'title_hr': 'Tangle: DAG za pohranu transakcija',
    'slug': 'D_tangle',
    'tl': '3 s',
    'ml': '1024 MB',
    'statement': r'''
<p>Tangle je usmjereni aciklički graf transakcija: svaka nova transakcija $X$ odobrava dvije prethodne ($Y$ i $Z$) i ima vlastitu težinu $W_X$. <i>Kumulativna težina</i> $CW_X$ zbroj je težine $X$ i težina svih transakcija koje $X$ odobravaju izravno ili neizravno. Transakcija je potvrđena kad je $CW_X \ge TH$.</p>
<h3>Ulaz</h3>
<p>$n$ i $TH$; zatim $n$ redaka <code>X Y Z W_X</code> u rastućem poretku $X$ ($2 \le X \le n + 1$, $0 \le Y, Z \le X - 1$, $Y \ne Z$, $1 \le W_X \le 5$, $1 \le n \le 10^4$).</p>
<h3>Izlaz</h3>
<p>Za svaku transakciju $T_X$ ($X \ge 2$) s $CW_X \ge TH$ ispiši <code>X CW_X</code> u rastućem poretku $X$, a na kraju ukupan broj potvrđenih transakcija.</p>
''',
    'hints': [
        r'''
<p>$CW_X$ = zbroj težina svih transakcija iz kojih je $X$ dostižan usmjerenim bridovima (obrnuti graf), uključujući $X$.</p>
''',
        r'''
<p>$n \le 10^4$: pokreni jedan DFS/BFS po obrnutim bridovima iz svakog $X$ — $O(n(n+m))$ s $m = 2n$ je oko $3\cdot10^8$ jednostavnih koraka, prihvatljivo uz $3$ s; ili koristi bitset dostižnosti.</p>
''',
    ],
    'coach': [
        ('Opažanje 1: što se broji',
         r'''
<p>„Odobrava izravno ili neizravno” = dostižnost u DAG-u. Pazi: $CW_X$ nije zbroj $CW_Y + CW_Z + W_X$ (dvostruko brojanje zajedničkih predaka) — trebaš uniju skupova, ne zbroj.</p>
'''),
        ('Opažanje 2: obrnuti graf',
         r'''
<p>Transakcije koje odobravaju $X$ su one iz kojih vodi put do $X$. Obrni bridove ($X \to Y, X \to Z$ postaje $Y \to X, Z \to X$) i traži dostižne iz $X$.</p>
'''),
        ('Algoritam',
         r'''
<p>Za svaki $X$ BFS po obrnutom grafu, zbrajaj $W$ posjećenih. Alternativa: <code>bitset&lt;n+2&gt;</code> po vrhu u topološkom (rastućem) redu — $reach[X] = \{X\} \cup reach$ svih koji ga odobravaju — $O(n^2/64)$. Ispiši one s $CW \ge TH$ i njihov broj.</p>
'''),
    ],
    'solution': r'''
<p>Nakon učitavanja svake transakcije problem rješavamo obilaskom grafa u dubinu (DFS) ili širinu (BFS): kumulativna težina transakcije $X$ zbroj je težina svih transakcija iz kojih je $X$ dostižan po usmjerenim bridovima (uključujući $X$). Za svaku transakciju pokrenemo obilazak po obrnutim bridovima i zbrojimo težine posjećenih vrhova; uz $n \le 10^4$ to je dovoljno brzo.</p>
''',
},
{
    'letter': 'E',
    'title': 'Printing Stickers',
    'title_hr': 'Ispis naljepnica',
    'slug': 'E_printing_stickers',
    'tl': '30 s',
    'ml': '1024 MB',
    'statement': r'''
<p>List naljepnica je mreža $M \times N$ polja, svako podijeljeno dijagonalom na dva trokuta od kojih su neki ispunjeni tintom. List se reže duž rubova trokuta, ali rez ne smije ići uz rub ispunjenog trokuta. Komadi bez ispunjenih trokuta se odbacuju; na svakoj preostaloj naljepnici svi su ispunjeni trokuti povezani. Rub svake naljepnice (uključujući rupe) polira se: horizontalni segment košta $H$, vertikalni $V$, a dijagonalni u polju $(i, j)$ košta $D_{ij}$. Za svaku naljepnicu izračunaj najmanji trošak poliranja (može se pokazati da sve naljepnice mogu istodobno postići minimum).</p>
<h3>Ulaz</h3>
<p>$T \le 50$ primjera; u svakom $M, N, H, V$ ($4 \le MN \le 10^4$), $M$ redaka smjerova dijagonala (<code>/</code> ili <code>\</code>), $M$ redaka duljine $2N$ s ispunjenošću lijevog i desnog trokuta (<code>#</code>/<code>.</code>) te $M$ redaka s $D_{ij}$ ($1 \le H, V, D_{ij} \le 1000$). Naljepnica je najviše $1000$.</p>
<h3>Izlaz</h3>
<p>Broj naljepnica $k$ te $k$ minimalnih troškova u nepadajućem poretku.</p>
''',
    'hints': [
        r'''
<p>Modeliraj: trokuti su vrhovi, susjedni trokuti spojeni bridom težine = cijena poliranja zajedničkog segmenta; ispunjene trokute jedne naljepnice stopi u terminal. Trošak naljepnice = minimalni rez koji odvaja njezin terminal od svih ostalih terminala (izolirajući rez).</p>
''',
        r'''
<p>Ne trebaš $|T|$ tokova: $\log|T|$ rezova po bitovima indeksa terminala, presjek strana $X_v$ za svaki $v$, i konačni tok u kontrahiranom grafu ($\sum |X_v| \le |V|$). Ili podijeli-pa-vladaj s jednim tokom po razini.</p>
''',
    ],
    'coach': [
        ('Opažanje 1: rezanje kao rez u grafu',
         r'''
<p>Naljepnica je komponenta lista nakon rezanja; njezin rub su segmenti između „unutra” i „vani”. Minimalni trošak ruba $=$ minimalni $s$–$t$ rez gdje je $s$ terminal naljepnice, a $t$ sve ostale naljepnice i vanjski rub (rez ne smije ići uz ispunjeni trokut — takvi bridovi imaju težinu $\infty$ ili se trokuti stapaju).</p>
'''),
        ('Opažanje 2: izolirajući rezovi',
         r'''
<p>Klasični rezultat (Dahlhaus i dr.): minimalni izolirajući rezovi za sve terminale zajedno mogu se izračunati s $O(\log |T|)$ maksimalnih tokova + jednim „skupnim” tokom, jer minimalni izolirajući rez za $v$ leži unutar presjeka strana rezova koji odvajaju $v$ od ostalih po bitovima.</p>
'''),
        ('Algoritam',
         r'''
<p>(1) Izgradi planarni graf trokuta, stopi terminale. (2) Za bit $i$: izvor = terminali s bitom $0$, ponor = s bitom $1$; nađi min-rez i zapamti stranu svakog vrha. (3) $X_v$ = presjek strana u kojima je $v$. (4) Za svaki $v$: kontrahiraj $V \setminus X_v$ u $\bar v$ i računaj tok $v \to \bar v$. Ispiši sortirane troškove.</p>
'''),
        ('Složenost',
         r'''
<p>$O(\log|T|)$ Dinic-tokova na grafu s $\le 2\cdot 10^4$ vrhova plus jedan ekvivalent; jednostavnije $|T|$ tokova također prolazi uz 30 s.</p>
'''),
    ],
    'solution': r'''
<p>Zadatak se može formulirati kao problem <b>minimalnih izolirajućih rezova</b> (minimum isolating cuts): u grafu $G$ (trokuti su vrhovi, susjedni trokuti spojeni bridom težine jednakoj cijeni poliranja zajedničkog segmenta) zadan je skup terminala $T$ — po jedan za svaku naljepnicu (njezini ispunjeni trokuti, stopljeni u jedan vrh). Za svaki terminal $v \in T$ tražimo minimalni rez koji odvaja $v$ od svih ostalih terminala $T \setminus \{v\}$.</p>
<ul>
    <li>Trivijalno rješenje zahtijeva $|T|$ izračuna maksimalnog toka. S učinkovitom implementacijom to prolazi (primijetimo da je konstruirani graf planaran).</li>
    <li>Postoji algoritam koji zahtijeva samo $2 + \log |T|$ izračuna maksimalnog toka. Terminale označimo brojevima od $0$ do $|T| - 1$ u binarnom zapisu. Za svaki $i = 0, 1, \dots, \log |T|$ izračunamo bilo koji minimalni rez koji odvaja sve terminale s $i$-tim bitom $0$ od svih terminala s $i$-tim bitom $1$. Svaki rez $(X_i, V \setminus X_i)$ ima dvije strane. Za svaki terminal $v$ uzmemo presjek $X_v$ svih strana kojima $v$ pripada. Može se pokazati: ako sve izvan $X_v$ kontrahiramo u jedan vrh $\bar v$, minimalni rez između $v$ i $\bar v$ upravo je minimalni izolirajući rez za $v$. Svi ti završni izračuni zajedno stoje najviše kao $2$ izračuna maksimalnog toka na izvornom grafu (jer su skupovi $X_v$ disjunktni).</li>
    <li>Nešto učinkovitija izvedba iste ideje koristi podijeli pa vladaj: naljepnice podijelimo u dva skupa i izračunamo maksimalni tok koji odvaja prvi skup od drugog. Rezultat dijeli graf na dva dijela, pa u svakom dijelu rekurzivno ponovno dijelimo naljepnice.</li>
</ul>
''',
},
{
    'letter': 'F',
    'title': 'AA Country and King Dreamoon',
    'title_hr': 'Zemlja AA i kralj Dreamoon',
    'slug': 'F_aa_country_and_king_dreamoon',
    'tl': '2 s',
    'ml': '1024 MB',
    'statement': r'''
<p>Zemlja AA je stablo s $n$ gradova. Kralj planira obilazak: zatvorenu šetnju s $2n - 2$ bridova koja počinje i završava u gradu $1$ i posjećuje sve gradove (redoslijed gradova zapisuje na papir, ukupno $2n - 1$ brojeva). Dio zapisa je nečitak — neki <b>uzastopni</b> brojevi zamijenjeni su nulama. Rekonstruiraj leksikografski najmanji valjani zapis; rješenje sigurno postoji.</p>
<h3>Ulaz</h3>
<p>$T \le 3 \cdot 10^4$ primjera; u svakom $n$ ($1 \le n \le 3 \cdot 10^5$, zbroj svih $n$ ne prelazi $3 \cdot 10^5$) i $2n - 1$ brojeva od $0$ do $n$ (nule su uzastopne i postoji barem jedna).</p>
<h3>Izlaz</h3>
<p>Za svaki primjer rekonstruirani leksikografski najmanji zapis.</p>
''',
    'hints': [
        r'''
<p>Zapis je Eulerov obilazak stabla (DFS iz $1$): svaki korak je ili spust u <em>novi</em> čvor ili povratak roditelju.</p>
''',
        r'''
<p>Popunjavaj nule pohlepno: u svakom koraku odaberi manji od (najmanji nekorišteni čvor, roditelj trenutnog) — uz uvjet da preostali broj nula dopušta da se zapis spoji s poznatim nastavkom (točan broj potrebnih povrataka i spustova).</p>
''',
    ],
    'coach': [
        ('Opažanje 1: struktura zapisa',
         r'''
<p>Šetnja s $2n-2$ bridova koja obiđe svako od $n$ čvorova stabla i vrati se u $1$ prelazi svaki brid točno dvaput — to je točno DFS obilazak. Poznati dijelovi zapisa fiksiraju neke bridove; nule su jedan uzastopni blok.</p>
'''),
        ('Opažanje 2: stanje na rubovima praznine',
         r'''
<p>Iz prefiksa prije praznine znaš stog DFS-a (trenutni put od korijena) i skup posjećenih. Iz sufiksa poslije praznine (čitanog unatrag) znaš u kojem čvoru moraš biti kad praznina završi i koji čvorovi moraju još biti neposjećeni (pojavljuju se prvi put kasnije). Duljina praznine = (broj povrataka) + (broj spustova).</p>
'''),
        ('Algoritam: pohlepno s provjerom izvedivosti',
         r'''
<p>U svakom koraku praznine: kandidat A = roditelj (povratak), kandidat B = najmanji čvor koji nije posjećen i ne pojavljuje se u sufiksu kao „prvi ulaz”. Uzmi manji kandidat ako nakon njega ostaje moguće doći do zahtijevanog stanja u preostalom broju koraka (dubina i broj čvorova koje treba još posjetiti i vratiti se). Inače uzmi drugi.</p>
'''),
        ('Složenost',
         r'''
<p>$\Theta(n)$ po testu uz pokazivač na najmanji slobodni čvor (monotono raste).</p>
'''),
    ],
    'solution': r'''
<ul>
    <li>Kraljev put ekvivalentan je nekom obilasku stabla u dubinu (DFS) — zapis je Eulerov obilazak stabla.</li>
    <li>U svakom koraku DFS-a postoje dvije vrste poteza: posjet novom čvoru ili povratak roditelju.</li>
    <li>Nečitke pozicije popunjavamo pohlepno: u svakom koraku provjerimo koja vrsta poteza daje leksikografski manji nastavak (najmanji još neposjećeni broj nasuprot roditelju) i odaberemo ga.</li>
    <li>Pritom treba paziti da nakon svakog odabira zapis i dalje može biti valjani DFS obilazak — poznati dio zapisa (nakon nula) određuje koji su bridovi već fiksirani, a broj posjeta i povrataka mora se poklopiti s duljinom praznine.</li>
    <li>Vremenska složenost je $\Theta(n)$.</li>
</ul>
''',
},
{
    'letter': 'G',
    'title': 'Repetitive Elements',
    'title_hr': 'Ponavljajući elementi',
    'slug': 'G_repetitive_elements',
    'tl': '3 s',
    'ml': '1024 MB',
    'statement': r'''
<p>Genom je niz nad alfabetom $\{A, T, C, G\}$. Ponavljajući element je uzorak koji se u genomu pojavljuje više puta <i>bez preklapanja</i>. Za zadani niz $S$ pronađi najdulji ponavljajući element $R$; ako ih je više, onaj koji se pojavljuje prvi.</p>
<h3>Ulaz</h3>
<p>$T \le 50$ primjera, svaki jedan niz $S$ ($15 \le |S| \le 100$).</p>
<h3>Izlaz</h3>
<p>Za svaki primjer niz $R$.</p>
''',
    'hints': [
        r'''
<p>$dp(i,j)$ = duljina zajedničkog sufiksa prefiksa $S[..i]$ i $S[..j]$ ($i \lt j$): $dp(i,j) = dp(i-1,j-1)+1$ ako $S_i = S_j$, inače $0$.</p>
''',
        r'''
<p>Zabrani preklapanje: vrijednost ograniči na $j - i$ (pojavljivanja koja završavaju na $i$ i $j$ ne preklapaju se ako duljina $\le j - i$).</p>
''',
    ],
    'coach': [
        ('Opažanje 1: najdulji ponovljeni podniz',
         r'''
<p>Klasični „longest repeated substring” preko $dp$ na paru pozicija — $O(|S|^2)$, s $|S| \le 100$ trivijalno. Novost je zabrana preklapanja.</p>
'''),
        ('Opažanje 2: uvjet nepreklapanja',
         r'''
<p>Ako se pojavljivanja završavaju na $i \lt j$ i imaju duljinu $L$, prvo zauzima $[i-L+1, i]$, drugo $[j-L+1, j]$; disjunktna su $\iff L \le j - i$. Zato $dp(i,j) = \min(dp(i-1,j-1) + 1,\ j - i)$ kad $S_i = S_j$.</p>
'''),
        ('Algoritam',
         r'''
<p>Maksimum po svim $i \lt j$; pri jednakosti uzmi ono s manjim početkom $i - L + 1$ (pri istoj duljini stroga usporedba). Ispiši podniz.</p>
'''),
    ],
    'solution': r'''
<p>Dinamičko programiranje. Neka $dp(i, j)$ označava duljinu zajedničkog podniza koji završava na pozicijama $i$ i $j$ genoma $S$ (gdje je $S_i$ $i$-ti nukleotid):
$$dp(i, j) = \begin{cases} 0, &amp; S_i \ne S_j, \\ dp(i - 1, j - 1) + 1, &amp; S_i = S_j. \end{cases}$$
Preklapanja isključujemo uvjetom $(j - i) &gt; dp(i - 1, j - 1)$: duljinu produžujemo samo dok se dva pojavljivanja ne dodiruju. Odgovor je najveća vrijednost $dp(i, j)$ za $i &lt; j$, uz pravilo da pri jednakoj duljini biramo pojavljivanje s manjim početnim indeksom.</p>
''',
},
{
    'letter': 'H',
    'title': 'Meeting Places',
    'title_hr': 'Mjesta sastanaka',
    'slug': 'H_meeting_places',
    'tl': '2 s',
    'ml': '1024 MB',
    'statement': r'''
<p>$N$ autora zadataka (točke u ravnini) podijeljeno je u $K$ grupa uzastopno numeriranih autora. Cijena grupe je polumjer najmanje kružnice koja obuhvaća sve njezine članove (najveća udaljenost od mjesta sastanka). Pronađi najmanji zbroj cijena. Točke se generiraju formulom
$X_i = Y_{i-1} \cdot 233811181 + 1 \pmod{2^{31} - 1}$ za $i \ge 2$ i $Y_i = X_i \cdot 233811181 + 1 \pmod{2^{31} - 1}$ za $i \ge 1$.</p>
<h3>Ulaz</h3>
<p>$N$, $K$, $X_1$ ($1 \le K \le N \le 2000$, $1 \le X_1 \le 8831$).</p>
<h3>Izlaz</h3>
<p>Najmanji zbroj polumjera; dopuštena relativna ili apsolutna greška $10^{-6}$.</p>
''',
    'hints': [
        r'''
<p>$dp[k][i] = \min_j\bigl(dp[k-1][j-1] + \mathrm{cost}(j, i)\bigr)$ gdje je $\mathrm{cost}$ polumjer najmanje obuhvaćajuće kružnice segmenta — treba sve $\mathrm{cost}(j,i)$ u $O(N^2)$.</p>
''',
        r'''
<p>Točke su pseudoslučajne: inkrementalna najmanja kružnica (Welzl bez permutacije) pri dodavanju točke očekivano rijetko mijenja kružnicu, pa za svaki početak $j$ prošireni $\mathrm{cost}(j, \cdot)$ računaš u očekivano $O(N)$.</p>
''',
    ],
    'coach': [
        ('Opažanje 1: DP po particiji',
         r'''
<p>Uzastopne grupe $\Rightarrow$ $dp[k][i]$ nad prefiksom duljine $i$ s $k$ grupa, prijelaz po početku zadnje grupe. S predizračunatom tablicom $\mathrm{cost}(j,i)$ svaki prijelaz je $O(1)$; $KN$ stanja s $O(N)$ prijelaza je $O(KN^2)$ u najgorem slučaju, no za slučajne točke $\mathrm{cost}(j,i)$ vrlo brzo postaje konstantan po $j$ (mala kružnica koja pokriva puno točaka), pa se prijelazi mogu rezati; službeno rješenje navodi $O(N^2 + KN)$ uz monotonost cijene po uključivanju.</p>
'''),
        ('Opažanje 2: cijene',
         r'''
<p>Fiksiraj $j$, dodavaj točke $j, j+1, \dots$ i održavaj najmanju kružnicu inkrementalno: ako je nova točka unutra, ništa; inače ponovno izračunaj s tom točkom na rubu (očekivano $O(1)$ puta za slučajne točke). Ukupno $O(N^2)$ za sve $\mathrm{cost}(j, i)$.</p>
'''),
        ('Algoritam',
         r'''
<p>Generiraj točke zadanom LCG formulom (64-bitna aritmetika), izračunaj $\mathrm{cost}$, DP s realnim brojevima (<code>double</code>), ispiši $dp[K][N]$.</p>
'''),
    ],
    'solution': r'''
<p>Neka $dp[K][N]$ označava optimalan odgovor za podjelu prvih $N$ točaka u $K$ segmenata. Očito je
$$dp[K][N] = \min_{1 \le i \le N} \bigl( dp[K-1][i-1] + \mathrm{cost}(i, N) \bigr),$$
gdje je $\mathrm{cost}(i, N)$ polumjer najmanje obuhvaćajuće kružnice točaka $i, \dots, N$.</p>
<p>Budući da su točke generirane slučajno, pri proširivanju segmenta za jednu točku najmanja obuhvaćajuća kružnica poveća se samo za očekivano $O(1)$ točaka. Zato sve vrijednosti $\mathrm{cost}(i, N)$ možemo izračunati u ukupno $O(N^2)$ (inkrementalni algoritam za najmanju kružnicu s očekivano konstantnim brojem ponovnih izračuna), a zatim dinamika traje $O(KN)$. Ukupna složenost je $O(N^2 + KN)$.</p>
''',
},
{
    'letter': 'I',
    'title': 'Cell Nuclei Detection',
    'title_hr': 'Detekcija staničnih jezgara',
    'slug': 'I_cell_nuclei_detection',
    'tl': '6 s',
    'ml': '1024 MB',
    'statement': r'''
<p>Zadano je $m$ referentnih (ground-truth) i $n$ detektiranih okvira (pravokutnika s cjelobrojnim koordinatama u $[0, 2000]$, širine i visine najviše $4$). Referentni okvir $G$ je detektiran okvirom $D$ ako je $|D \cap G| / |G| \ge 1/2$; svaki detektirani okvir može detektirati najviše jedan referentni. Odredi najveći broj detektiranih jezgara.</p>
<h3>Ulaz</h3>
<p>$t \le 5$ primjera; u svakom $m, n \le 5 \cdot 10^4$ i $m + n$ četvorki $(x_1, y_1, x_2, y_2)$. Nema dva referentna (ni dva detektirana) okvira od kojih jedan sadrži drugi.</p>
<h3>Izlaz</h3>
<p>Za svaki primjer najveći broj detektiranih jezgara.</p>
''',
    'hints': [
        r'''
<p>Bipartitni graf referentni–detektirani, brid ako je $|D \cap G| \ge |G|/2$. Okviri su veličine $\le 4$, pa su kandidati za $G$ samo detektirani okviri sa središtem u okolini $\pm 2$ — $O(1)$ po okviru preko mape/rešetke po koordinatama.</p>
''',
        r'''
<p>Najveće uparivanje: Hopcroft–Karp / Dinic u $O(E\sqrt V)$.</p>
''',
    ],
    'coach': [
        ('Opažanje 1: model',
         r'''
<p>Svaki detektirani okvir detektira najviše jednu jezgru, svaka jezgra broji se jednom: maksimalno bipartitno uparivanje.</p>
'''),
        ('Opažanje 2: rijetki bridovi',
         r'''
<p>Presjek dvaju okvira dimenzija $\le 4$ je neprazan samo ako su im lijevi donji kutovi udaljeni $\lt 4$ po obje osi. Indeksiraj detektirane okvire po kutu u rešetku $2001\times2001$ (ili mapu) i provjeri $\le 7\times7$ susjednih ćelija — $E = O(n)$.</p>
'''),
        ('Algoritam i složenost',
         r'''
<p>Izgradnja $O((m+n))$, Hopcroft–Karp $O(E\sqrt{V})$ s $V \le 10^5$. Površine su cijeli brojevi — uspoređuj $2|D\cap G| \ge |G|$ bez razlomaka.</p>
'''),
    ],
    'solution': r'''
<ul>
    <li>Izgradimo bipartitni graf: jedna strana su referentni okviri, druga detektirani.</li>
    <li>Središta detektiranih okvira pohranimo u mapu (po koordinatama).</li>
    <li>Za svaki referentni okvir provjerimo površinu presjeka s obližnjim detektiranim okvirima i tako odredimo relaciju "detektiran". Kako su širina i visina okvira ograničene s $4$, središta relevantnih detektiranih okvira udaljena su od središta referentnog okvira najviše $2$ (po svakoj koordinati), pa je kandidata po okviru $O(1)$.</li>
    <li>Najveće bipartitno uparivanje pronađemo Dinicovim algoritmom (Hopcroft–Karp) u $O(\sqrt{V} \, E)$.</li>
</ul>
''',
},
{
    'letter': 'J',
    'title': 'Traveling in Jade City',
    'title_hr': 'Putovanje po Gradu žada',
    'slug': 'J_traveling_in_jade_city',
    'tl': '3 s',
    'ml': '1024 MB',
    'statement': r'''
<p>Kružna pruga ima $N$ stanica $1, \dots, N$ (u smjeru kazaljke). Dodatna linija spaja stanice $1$ i $K$ preko $M$ novih stanica $N + 1, \dots, N + M$. Pruge $c_i$ (kružnica) i $x_j$ (dodatna linija) imaju zadana vremena putovanja i mogu se privremeno isključiti. Obradi $Q$ operacija: upit <code>q u v</code> — najkraće vrijeme od $u$ do $v$ (ili <code>impossible</code>); <code>c i</code> / <code>x j</code> — promijeni dostupnost pruge $c_i$ odnosno $x_j$.</p>
<h3>Ulaz</h3>
<p>$N, K, M, Q \le 10^6$; vremena pruga su nenegativni cijeli brojevi $\le 200$.</p>
<h3>Izlaz</h3>
<p>Odgovor na svaki upit.</p>
''',
    'hints': [
        r'''
<p>Tri puta između čvorišta $1$ i $K$: luk $1..K$, luk $K..N,1$ i dodatna linija. Na svakom putu drži prefiksne sume vremena i uređeni skup isključenih pruga.</p>
''',
        r'''
<p>Upit: ako su $u, v$ na istom putu — izravno (ako između nema isključene pruge) ili obilazak preko $1$ i $K$; inače put nužno prolazi kroz $1$ ili $K$. Konstantan broj kombinacija, svaka $O(\log)$.</p>
''',
    ],
    'coach': [
        ('Opažanje 1: graf je „theta”',
         r'''
<p>Kružnica + tetiva $=$ tri disjunktna puta između $1$ i $K$. Svaki najkraći put je ili unutar jednog puta, ili prolazi kroz čvorište i koristi dijelove najviše dva puta (plus možda cijeli treći za prijelaz $1 \leftrightarrow K$).</p>
'''),
        ('Opažanje 2: prohodnost segmenta',
         r'''
<p>Segment stanica $[a, b]$ na putu je prohodan $\iff$ nema isključene pruge s indeksom u $[a, b)$ — <code>std::set</code> isključenih po putu, <code>lower_bound</code>. Duljina segmenta = razlika prefiksnih suma.</p>
'''),
        ('Algoritam',
         r'''
<p>$d(1, K)$ = min od tri puta (ako prohodni). Za $u, v$: kandidati su izravni segment (isti put), $d(u \to 1) + d(1 \to v)$, $d(u \to K) + d(K \to v)$, $d(u \to 1) + d(1,K) + d(K \to v)$ i simetrično — sve preko prohodnih segmenata. Uzmi minimum ili <code>impossible</code>.</p>
'''),
        ('Složenost',
         r'''
<p>$O((N + M + Q)\log)$; koristi brzi I/O ($10^6$ upita).</p>
'''),
    ],
    'solution': r'''
<ul>
    <li>Željeznički sustav podijelimo na tri puta: luk kružnice od $1$ do $K$ (stanice $1, \dots, K$), luk kružnice od $K$ natrag do $1$ (stanice $K, \dots, N, 1$) i dodatnu liniju (stanice $1, N + 1, \dots, N + M, K$). Svaki od njih spaja "čvorišta" $1$ i $K$.</li>
    <li>Na svakom putu prefiksnim sumama održavamo vremena putovanja između stanica.</li>
    <li>Na svakom putu binarnim stablom pretraživanja (uređenim skupom) čuvamo isključene pruge, pa u $O(\log)$ provjeravamo je li segment između dvije stanice povezan (nema isključene pruge između njih) i koja je prva isključena pruga u nekom smjeru.</li>
    <li>Najkraći put računamo provjerom konstantnog broja slučajeva: ako su $u$ i $v$ na istom putu, kandidat je izravna vožnja (ako je segment prohodan) te obilazak preko čvorišta $1$ i $K$ drugim putevima; ako su na različitim putevima, put nužno prolazi kroz čvorište $1$ ili $K$, pa kombiniramo udaljenosti do čvorišta s (mogućim) prijelazom između $1$ i $K$ preko trećeg puta. Uzimamo najmanju izvedivu kombinaciju.</li>
</ul>
''',
},
{
    'letter': 'K',
    'title': 'Group Guests',
    'title_hr': 'Grupiranje gostiju',
    'slug': 'K_group_guests',
    'tl': '4 s',
    'ml': '1024 MB',
    'statement': r'''
<p>Na zabavi je $n$ gostiju, svaki s točno dva različita hobija (nema dva gosta s istim parom hobija). Goste treba podijeliti u grupe od $2$ ili $3$ osobe u kojima svaka dva gosta imaju zajednički hobi: tip A — dva gosta sa zajedničkim hobijem; tip B — tri gosta koji svi dijele isti hobi; tip C — tri gosta od kojih svaki par dijeli hobi, ali ne isti za sve. Minimiziraj broj $\alpha$ neraspoređenih gostiju, a zatim broj $\beta$ grupa tipa B.</p>
<h3>Ulaz</h3>
<p>$n$ i $h$ ($2 \le n \le 10^6$, $3 \le h \le 2n$), zatim $n$ parova hobija $x, y$.</p>
<h3>Izlaz</h3>
<p>$\alpha$ i $\beta$.</p>
''',
    'hints': [
        r'''
<p>Hobiji = vrhovi, gosti = bridovi. Grupa A = put s $2$ brida ($P_3$), C = trokut ($C_3$), B = zvijezda s $3$ brida ($S_3$). Treba particija skupa bridova.</p>
''',
        r'''
<p>Komponenta s parnim brojem bridova uvijek se particionira na $P_3$-ove. Neparna: pokušaj ukloniti trokut tako da ostatak bude paran (bez B), inače zvijezdu (B, $\beta{+}{+}$), inače jedan brid ostaje ($\alpha{+}{+}$).</p>
''',
    ],
    'coach': [
        ('Opažanje 1: parnost komponente',
         r'''
<p>Povezan graf s parnim brojem bridova ima particiju na putove duljine $2$ (klasična lema; konstruktivno preko DFS-stabla, sparujući bridove odozdo). Neparan broj bridova: barem jedan brid mora ići u trokut, zvijezdu ili ostati.</p>
'''),
        ('Opažanje 2: uklanjanje jednog $C_3$ ili $S_3$',
         r'''
<p>Nakon uklanjanja tri brida neparne komponente ostaje paran broj bridova, ali komponenta se može raspasti — sve nove komponente moraju biti parne. Trokut nikad ne razdvaja vrhove više nego što ih ima; provjeri parnost dijelova preko DFS-a s uklonjenim bridovima (za trokut: $3$ brida na $3$ vrha; za zvijezdu: $3$ brida iz jednog centra).</p>
'''),
        ('Algoritam',
         r'''
<p>Po komponentama: parna $\Rightarrow$ sve $P_3$. Neparna: nabroji trokute (algoritam s orijentacijom po stupnju, $O(m\sqrt m)$) i za svaki provjeri parnost ostatka — iskoristi strukturu blokova (mostovi/2-povezane komponente) da provjera bude brza; ako nema, probaj zvijezde (centar stupnja $\ge 3$); inače $\alpha \mathrel{+}= 1$. Minimiziraj $\alpha$, zatim $\beta$.</p>
'''),
        ('Složenost',
         r'''
<p>$O(n\sqrt{n/\log n})$ za trokute uz linearni ostatak; $n \le 10^6$.</p>
'''),
    ],
    'solution': r'''
<p>Hobiji su vrhovi, a gosti bridovi neusmjerenog grafa. Zadatak je particionirati skup bridova na puteve duljine $2$ ($P_3$, grupa tipa A), cikluse duljine $3$ ($C_3$, tip C) i zvijezde s $4$ vrha ($S_3$, tip B).</p>
<ul>
    <li>Particija bridova na same $P_3$-ove moguća je ako i samo ako svaka komponenta ima paran broj bridova (<i>parna komponenta</i>).</li>
    <li>Particija na $P_3$-ove i $C_3$-ove moguća je ako i samo ako postoji $C_3$ čijim uklanjanjem sve komponente postaju parne.</li>
    <li>Particija na $P_3$-ove i $S_3$-ove moguća je ako i samo ako postoji $S_3$ čijim uklanjanjem sve komponente postaju parne.</li>
</ul>
<p>Kombinirajući ta tri svojstva zadatak rješavamo u polinomnom vremenu: komponente s parnim brojem bridova pokrivamo $P_3$-ovima; u neparnoj komponenti pokušavamo ukloniti jedan $C_3$ (bez grupe tipa B), a tek ako to nije moguće koristimo $S_3$ (tip B, povećava $\beta$), inače jedan brid ostaje nepokriven (povećava $\alpha$). Usko grlo je provjera postojanja odgovarajućeg $C_3$ (trokuta), što se može izvesti u $O(n \sqrt{n / \log n})$.</p>
''',
},
{
    'letter': 'L',
    'title': 'Programmable Virus',
    'title_hr': 'Programabilni virus',
    'slug': 'L_programmable_virus',
    'tl': '3 s',
    'ml': '1024 MB',
    'statement': r'''
<p>Enzim izvršava program zapisan RNA-kodonima: $11$ kodona kodira znamenke od $-1$ do $9$ i naredbe <code>STOP</code>, <code>NEXT</code>, <code>PREV</code>, <code>INC</code>, <code>DEC</code>, <code>OUT</code>, <code>IN</code>, <code>BEGIN</code>, <code>END</code> (pomak stanja, uvećanje/umanjenje uz ciklički prijelaz $9 \to -1$, ispis, čitanje ulaza, petlja s uparenim <code>BEGIN</code>/<code>END</code>). Napiši program koji čita niz nenegativnih znamenaka kao dekadski broj i ispisuje je li djeljiv sa $k$, uz duljinu programa i broj koraka najviše $10^6$.</p>
<h3>Ulaz i izlaz</h3>
<p>Zadatak je konstrukcijski: ispisuje se sam RNA program (detalji formata i simulator <code>simu.c</code> nalaze se u službenom tekstu zadatka).</p>
''',
    'hints': [
        r'''
<p>Skup naredbi je brainfuck s drugim imenima: <code>NEXT/PREV</code> = <code>&gt;/&lt;</code>, <code>INC/DEC</code> = <code>+/-</code>, <code>OUT/IN</code> = <code>./,</code>, <code>BEGIN/END</code> = <code>[/]</code>. Ćelije su znamenke $-1..9$ s cikličkim prijelazom.</p>
''',
        r'''
<p>Održavaj ostatak modulo $k$ u nekoliko ćelija; za svaku pročitanu znamenku $d$: $r \leftarrow (10r + d) \bmod k$ — implementiraj množenje i redukciju petljama.</p>
''',
    ],
    'coach': [
        ('Opažanje 1: prepoznaj jezik',
         r'''
<p>Petlja <code>BEGIN…END</code> izvršava se dok ćelija nije $0$ — brainfuck semantika. Znamenke $-1..9$ s ciklusom znače da ćelija ima $11$ stanja; koristi $-1$ kao „sentinel” za kraj ulaza ako <code>IN</code> na kraju vraća $-1$ (provjeri službeni tekst).</p>
'''),
        ('Opažanje 2: aritmetika mod $k$ s malim ćelijama',
         r'''
<p>Ostatak $r \lt k$ možda ne stane u jednu ćeliju; predstavi ga unarno u traci od $k$ ćelija (pokazivač na poziciji $r$) ili kao više znamenki. Prijelaz $r \to (10r + d) \bmod k$ je tada pomak pokazivača za $10r + d$ mjesta uz „omatanje” — jednostavno za implementaciju kao petlja koja pomiče pokazivač i provjerava kraj trake.</p>
'''),
        ('Algoritam',
         r'''
<p>Generiraj program skriptom (Python) za zadani $k$, provjeri ga priloženim simulatorom <code>simu.c</code>, pazi na granicu duljine i broja koraka $10^6$.</p>
'''),
    ],
    'solution': r'''
<p>Jezik je gotovo izomorfan jeziku <b>brainfuck</b> (jedina razlika je oznaka kraja, <code>STOP</code>): <code>NEXT</code>/<code>PREV</code> odgovaraju <code>&gt;</code>/<code>&lt;</code>, <code>INC</code>/<code>DEC</code> naredbama <code>+</code>/<code>-</code>, <code>OUT</code>/<code>IN</code> naredbama <code>.</code>/<code>,</code>, a <code>BEGIN</code>/<code>END</code> zagradama <code>[</code>/<code>]</code>. Stoga zadatak rješavamo kao brainfuck program koji čita znamenke jednu po jednu i održava ostatak pročitanog prefiksa modulo $k$.</p>
''',
},
{
    'letter': 'M',
    'title': 'Connectivity Problem',
    'title_hr': 'Problem povezanosti',
    'slug': 'M_connectivity_problem',
    'tl': '3 s',
    'ml': '1024 MB',
    'statement': r'''
<p>Kapetan Jack ima otoke označene brojevima $0 \le p, q &lt; 1000$; početno nema mostova. Za svaki od $n$ upita $(p, q)$ ispiši <code>Y</code> ako se od $p$ do $q$ može doći postojećim mostovima, inače ispiši <code>N</code> i izgradi most između $p$ i $q$.</p>
<h3>Ulaz</h3>
<p>$n$ ($1 \le n \le 10^4$) i $n$ parova $p, q$ ($p \ne q$).</p>
<h3>Izlaz</h3>
<p>Za svaki upit <code>Y</code> ili <code>N</code>.</p>
''',
    'hints': [
        r'''
<p>Mostovi se samo grade, nikad ne ruše — koja struktura odgovara na „jesu li u istoj komponenti?” uz dodavanje bridova?</p>
''',
        r'''
<p>Union-Find: <code>find(p) == find(q)</code> $\Rightarrow$ <code>Y</code>; inače <code>N</code> i <code>union(p, q)</code>.</p>
''',
    ],
    'coach': [
        ('Opažanje 1: online povezanost samo s dodavanjem bridova',
         r'''
<p>Bridovi se samo dodaju, nikad ne brišu — savršen slučaj za DSU s kompresijom puta i unijom po rangu/veličini.</p>
'''),
        ('Opažanje 2: alternativa',
         r'''
<p>Uz $1000$ otoka i $10^4$ upita prošao bi i BFS po trenutnom grafu za svaki upit ($O(nq)$), ali DSU je kraći i standardan.</p>
'''),
        ('Algoritam i složenost',
         r'''
<p>$1000$ otoka, $10^4$ upita: $O(n\,\alpha(1000))$, praktički linearno.</p>
'''),
    ],
    'solution': r'''
<p>Zadatak rješavamo strukturom <b>disjunktnih skupova</b> (Union-Find): za upit $(p, q)$ provjerimo jesu li $p$ i $q$ u istom skupu; ako jesu, ispišemo <code>Y</code>, a inače ispišemo <code>N</code> i spojimo njihove skupove.</p>
''',
},
]
