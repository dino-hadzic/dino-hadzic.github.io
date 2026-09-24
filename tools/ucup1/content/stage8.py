"""1st Universal Cup – Stage 8: Slovenia. Uvezeno iz ručno pisanih stranica (import_legacy.py); naputci i
trenerski koraci iz nekadašnjeg retro_stage8.py."""

STAGE = {
    'no': 8,
    'name': 'Stage 8: Slovenia',
    'source_name': 'The 2022 ICPC Central Europe Regional Contest (CERC 2022), Ljubljana',
    'source_html': r'''
<p>Prijevod službene prezentacije rješenja CERC-a 2022 (Ljubljana, 27. 11. 2022): <a href="https://contest.ucup.ac/download.php?type=attachments&amp;id=1070&amp;r=1">Solution Presentation (en)</a>. Izvornik je skup prezentacijskih slajdova s natuknicama, pa su i prijevodi rješenja u tom obliku. Tekst zadatka preveden je prema službenim <a href="https://contest.ucup.ac/download.php?type=attachments&amp;id=1070&amp;r=0">engleskim tekstovima zadataka</a>. Zadatak je dostupan na <a href="https://contest.ucup.ac/contest/1070">Universal Cup Judging System</a>.</p>
''',
}

PROBLEMS = [
{
    'letter': 'A',
    'title': 'Bandits',
    'title_hr': 'Banditi',
    'slug': 'A_bandits',
    'tl': '5 s',
    'ml': '512 MB',
    'statement': r'''
<p>Kraljevstvo je stablo s $N$ sela i $N - 1$ cesta duljina $C_i$. Sigurnosni ugovor sa sjedištem u selu $X_j$ i radijusom $R_j$ štiti sve ceste koje leže na nekom putu duljine najviše $R_j$ iz $X_j$. Obradi $Q$ upita: <code>+ X R</code> dodaje novi ugovor, a <code>? Y</code> pita koliko ugovora trenutačno štiti cestu $Y$.</p>
<h3>Ulaz</h3>
<p>$N$, opis $N - 1$ cesta ($A_i, B_i, C_i$), zatim $Q$ upita. $1 \le N, Q \le 10^5$, $0 \le C_i, R_j \le 10^9$.</p>
<h3>Izlaz</h3>
<p>Za svaki upit <code>?</code> trenutačan broj ugovora koji štite tu cestu.</p>
''',
    'hints': [
        r'''
<p>Ugovor $(X, R)$ pokriva brid $e$ ako je $d(X, \text{dalji kraj } e) \le R$. Upiti „koliko ugovora pokriva brid” s dodavanjem ugovora — klasičan posao za centroidnu dekompoziciju.</p>
''',
        r'''
<p>Za svaki centroid $A$ na putu od $X$ do korijena dekompozicije pohrani „preostali radijus” $R - d(X, A)$ u sortiranu strukturu (BIT nad komprimiranim vrijednostima). Za brid $(U, V)$ zbroji po njegovim centroidnim predcima broj radijusa $\ge$ udaljenost do daljeg kraja, uz oduzimanje doprinosa iz istog podstabla (da se ne broji dvaput).</p>
''',
    ],
    'coach': [
        ('Opažanje 1: uvjet pokrivanja',
         r'''
<p>Put duljine $\le R$ iz $X$ prolazi bridom $e = (U, V)$ ako i samo ako $\min(d(X,U), d(X,V)) + \ell(e) \le R$, tj. dalji kraj je unutar $R$. Dakle brid je pokriven $\iff$ udaljenost od $X$ do daljeg kraja $\le R$.</p>
'''),
        ('Opažanje 2: centroidna dekompozicija razbija „udaljenost”',
         r'''
<p>Za bilo koja dva vrha $X$, $Y$ postoji zajednički centroidni predak $A$ s $d(X,Y) = d(X,A) + d(A,Y)$ (najviši na kojem se putovi razdvajaju). Uvjet $d(X,A) + d(A,Y) \le R$ postaje $d(A,Y) \le R - d(X,A)$: u $A$ pohrani vrijednost $R - d(X,A)$; upit za $Y$ broji pohranjene vrijednosti $\ge d(A, Y)$.</p>
'''),
        ('Opažanje 3: bez dvostrukog brojanja',
         r'''
<p>Ako su $X$ i $Y$ u istom djetetu-podstablu centroida $A$, par je već obrađen na nižem centroidu — zato u svakom $A$ držimo i strukturu po djetetu-podstablu iz kojeg je $X$ došao, čiji doprinos oduzimamo (standardni trik s „isključi podstablo”).</p>
'''),
        ('Algoritam i složenost',
         r'''
<p>Offline: prikupi sve vrijednosti koje će ući u svaku strukturu, komprimiraj, BIT po centroidu. Dodavanje: $O(\log N)$ centroida $\times$ $O(\log N)$ BIT. Upit za brid: dalji kraj $Y$ (u odnosu na svaki centroidni predak treba paziti koji je kraj dalji — koristi $\min(d(U,A), d(V,A)) + \ell$). Ukupno $O((N+Q)\log^2 N)$.</p>
'''),
    ],
    'solution': r'''
<p>Zaštititi čvorove stabla na udaljenosti najviše $r$ od $X$ i odgovarati na upite o razini zaštite ceste $Y$.</p>
<ul>
    <li><b>Centroidna dekompozicija.</b></li>
    <li>Novi sigurnosni ugovor u $X$ s radijusom $r$:
        <ul>
            <li>označimo dijelove stabla kao zaštićene — $O(\log^2 n)$;</li>
            <li>u svakom centroidu $A$ na putu od $X$ prema korijenu dekompozicije pohranimo preostalu udaljenost $r - d(X, A)$ u strukturu (stablo) nad udaljenostima, isključujući podstablo iz kojeg smo došli.</li>
        </ul>
    </li>
    <li>Pokrivenost brida $U$–$V$ duljine $l$ (neka je $V$ „važniji“ centroid, tj. viši u dekompoziciji):
        <ul>
            <li>zaštita koja potječe iz podkomponenti centroida $V$ (npr. iz $U$, $X$, $A$) i ulazi preko $U$: broj oznaka s vrijednošću $\ge l + d(U, A)$, isključujući podstablo od $X$;</li>
            <li>zaštita iz velikih komponenti (npr. $C$) koje sadrže i $U$ i $V$: broj oznaka s vrijednošću $\ge l + \min(d(U, C), d(V, C))$, isključujući podstablo od $B$.</li>
        </ul>
    </li>
    <li>Ukupno $O(Q \log^2 N)$.</li>
</ul>
''',
},
{
    'letter': 'B',
    'title': 'Combination Locks',
    'title_hr': 'Brave s kombinacijom',
    'slug': 'B_combination_locks',
    'tl': '2 s',
    'ml': '256 MB',
    'statement': r'''
<p>Alice i Bob imaju brave s $N$ znamenki. Charlie prati samo <i>uzorak razlika</i> $S$ (znak <code>=</code> ili <code>.</code> na svakoj poziciji, ovisno o tome poklapaju li se znamenke). Igrači naizmjence (Alice prva) mijenjaju jednu znamenku svoje brave tako da se uzorak razlika promijeni; uzorak se ne smije ponoviti tijekom igre niti biti jedan od $C$ zabranjenih uzoraka $P_i$. Tko ne može odigrati potez, gubi. Odredi pobjednika uz optimalnu igru.</p>
<h3>Ulaz</h3>
<p>$T \le 20$ testova; u svakom $N$ ($1 \le N \le 10$), $C$ ($0 \le C \le 1000$), početne konfiguracije obiju brava i $C$ zabranjenih uzoraka.</p>
<h3>Izlaz</h3>
<p>Ime pobjednika za svaki test.</p>
''',
    'hints': [
        r'''
<p>Stanje igre je samo uzorak razlika (niz od $N$ bitova). Potez = promjena točno jednog bita (promjena znamenke mijenja jednakost samo na toj poziciji). Graf je hiperkocka $Q_N$ bez zabranjenih vrhova, $2^{10}$ vrhova.</p>
''',
        r'''
<p>Igra „gradi jednostavan put, tko ne može produljiti gubi” na grafu: prvi igrač pobjeđuje $\iff$ početni vrh je u svakom najvećem uparivanju. Izračunaj najveće uparivanje (graf je bipartitan po parnosti), pa provjeri postoji li najveće uparivanje koje ne sadrži start (ukloni start i usporedi veličine).</p>
''',
    ],
    'coach': [
        ('Opažanje 1: sažmi stanje',
         r'''
<p>Znamenke same nisu bitne — Charlie vidi samo uzorak i pravilo zabranjuje ponavljanje uzorka. Svaki igrač uvijek može postaviti bilo koji bit (izabere znamenku jednaku ili različitu suparnikovoj), pa su potezi iz uzorka $u$ upravo susjedi u hiperkocki.</p>
'''),
        ('Opažanje 2: Undirected Vertex Geography',
         r'''
<p>Igra na grafu s pravilom „vrh se ne ponavlja” je klasična igra u kojoj je pozicija $v$ pobjednička za igrača na potezu $\iff$ $v$ leži u svakom najvećem uparivanju. Dokaz: ako postoji najveće uparivanje $M$ bez $v$, drugi igrač uvijek odgovara uparenim bridom (zapinjanje bi dalo uvećavajući put); ako je $v$ u svakom $M$, prvi igrač igra uparenim bridom iz $v$.</p>
'''),
        ('Algoritam',
         r'''
<p>Vrhovi: uzorci osim zabranjenih ($\le 1024$), bridovi po bitovima. Bipartitan po broju jedinica: Hopcroft–Karp ili Kuhn ($\le 1024 \cdot 10$ bridova). Izračunaj $|M|$ na cijelom grafu i $|M'|$ na grafu bez starta: Alice pobjeđuje $\iff |M'| \lt |M|$. $O(E\sqrt V)$ po testu.</p>
'''),
    ],
    'solution': r'''
<p>Naći pobjednika igre za dva igrača u kojoj se stanja ne ponavljaju.</p>
<ul>
    <li>Graf je <b>hiperkocka</b>: čvor je uzorak razlika, neki su čvorovi zabranjeni; potez vodi u bilo koji susjedni čvor. Graf je bipartitan.</li>
    <li>Igrači naizmjence grade jednostavan put u grafu.</li>
    <li>Moguća strategija: slijediti bridove najvećeg uparivanja.</li>
    <li>Postoji li najveće uparivanje koje ne uključuje početni čvor?
        <ul>
            <li>Da: Bob slijedi uparene bridove. Kad bi zapeo u neuparenom čvoru, postojao bi uvećavajući put — kontradikcija s maksimalnošću.</li>
            <li>Ne: Alice slijedi uparene bridove. Kad bi zapela u neuparenom čvoru, preokretom bridova duž puta dobili bismo najveće uparivanje s neuparenim početnim čvorom — kontradikcija.</li>
        </ul>
    </li>
</ul>
''',
},
{
    'letter': 'C',
    'title': 'Constellations',
    'title_hr': 'Zviježđa',
    'slug': 'C_constellations',
    'tl': '10 s',
    'ml': '512 MB',
    'statement': r'''
<p>Početno je svaka zvijezda vlastito zviježđe. U svakom koraku spajaju se dva najbliža zviježđa, gdje je udaljenost prosjek kvadrata euklidskih udaljenosti parova zvijezda:
$$d(A, B) = \frac{1}{|A||B|} \sum_{a \in A} \sum_{b \in B} \|a - b\|^2.$$
Pri jednakim udaljenostima prednost ima par sa starijim zviježđem, zatim onaj s mlađim starijim. Ispiši veličinu novonastalog zviježđa nakon svakog od $N - 1$ koraka.</p>
<h3>Ulaz</h3>
<p>$N$ ($2 \le N \le 2000$) zvijezda s cjelobrojnim koordinatama u $[-1000, 1000]$, od najstarije do najmlađe; sve su točke različite.</p>
<h3>Izlaz</h3>
<p>$N - 1$ redaka s veličinama novih zviježđa.</p>
''',
    'hints': [
        r'''
<p>Označi $D(A,B) = \sum_{a\in A}\sum_{b\in B}\|a-b\|^2$ (bez dijeljenja). Tada je $D(A\cup B, C) = D(A,C) + D(B,C)$ — spajanje ažurira udaljenosti prema svim ostalima zbrajanjem.</p>
''',
        r'''
<p>Red s prioritetom parova $(d, \text{starije}, \text{mlađe})$ s lijenim brisanjem zastarjelih unosa; $O(n)$ spajanja $\times$ $O(n)$ novih parova $\times$ $O(\log n)$. Usporedbe drži egzaktno u cijelim brojevima: $d = D/(|A||B|)$, uspoređuj $D_1 |A_2||B_2|$ s $D_2 |A_1||B_1|$ (do $\approx 10^{7}\cdot 4\cdot10^6\cdot 4\cdot 10^6$ — <code>__int128</code> ili pažljivo).</p>
''',
    ],
    'coach': [
        ('Opažanje 1: udaljenost je aditivna po skupovima',
         r'''
<p>Prosjek kvadrata udaljenosti je $D(A,B)/(|A||B|)$; brojnik $D$ je zbroj po parovima, pa se razdvaja po uniji. Alternativno: $D(A,B) = |B|\sum_A \|a\|^2 + |A|\sum_B\|b\|^2 - 2\langle \sum_A a, \sum_B b\rangle$ — dovoljno je pamtiti $|A|$, $\sum a$, $\sum\|a\|^2$ po zviježđu i računati $D$ u $O(1)$.</p>
'''),
        ('Opažanje 2: hijerarhijsko grupiranje s redom prioriteta',
         r'''
<p>U svakom koraku treba globalno najbliži par. Naivno $O(n^2)$ po koraku ($O(n^3)$ ukupno, $8\cdot10^9$ — preblizu). Red prioriteta: nakon spajanja $A$, $B$ u $M$, dodaj $(D(M,C), \dots)$ za sve aktivne $C$; unose s mrtvim zviježđima preskoči pri vađenju.</p>
'''),
        ('Opažanje 3: pravilo prednosti',
         r'''
<p>Ključ usporedbe: $(d, \text{indeks starijeg}, \text{indeks mlađeg})$ — novom zviježđu daj novi indeks ($n, n+1, \dots$) jer je mlađe od svih dosadašnjih. Usporedba razlomaka bez pomičnog zareza da ne bude pogreške pri jednakostima.</p>
'''),
        ('Složenost',
         r'''
<p>$O(n^2 \log n)$ vremena, $O(n^2)$ memorije u redu (oko $4\cdot 10^6$ unosa uz lijeno brisanje — lijeno brisanje ukupno unosa $\le n^2$).</p>
'''),
    ],
    'solution': r'''
<p>Izračunati hijerarhijsko grupiranje točaka uz kvadrat euklidske udaljenosti.</p>
<ul>
    <li>Gruba sila: $O(n^5)$, odnosno $O(n^3)$ uz pametnije računanje udaljenosti.</li>
    <li>Zviježđe je popis zvijezda.</li>
    <li>Red s prioritetom potencijalnih spajanja: trojke $(\text{udaljenost}, \min(a, b), \max(a, b))$.</li>
    <li>Spajanje i ažuriranje udaljenosti: uz $d'(A, B) = \sum_{a \in A} \sum_{b \in B} \|a - b\|^2$ vrijedi
    $$d'(A + B, C) = d'(A, C) + d'(B, C),$$
    pa se nove udaljenosti dobivaju zbrajanjem (a $d = d' / (|A||B|)$).</li>
    <li>Složenost $O(n^2 \log n)$: nastaje $O(n)$ zviježđa, a pri svakom spajanju ažuriramo $O(n)$ udaljenosti u $O(\log n)$.</li>
</ul>
''',
},
{
    'letter': 'D',
    'title': 'Deforestation',
    'title_hr': 'Sječa stabla',
    'slug': 'D_deforestation',
    'tl': '2 s',
    'ml': '256 MB',
    'statement': r'''
<p>Stablo (deblo koje se grana) treba izrezati na komade težine najviše $W$ uz najmanji broj komada. Rezati se može bilo gdje na segmentu, uključujući neposredno prije ili poslije grananja.</p>
<h3>Ulaz</h3>
<p>$W$, zatim rekurzivni opis debla: težina segmenta $M$ i broj grana $N$ na njegovom kraju, iza čega slijede opisi grana. $1 \le W, M \le 10^9$; ukupna težina $\le 10^9$; ukupno najviše $10^5$ segmenata.</p>
<h3>Izlaz</h3>
<p>Broj komada.</p>
''',
    'hints': [
        r'''
<p>Pohlepno od listova: iz svakog segmenta izreži komade težine točno $W$ dok ne ostane „panj” $\lt W$ koji se prenosi roditelju.</p>
''',
        r'''
<p>U čvoru s panjevima djece $x_1, \dots, x_k$ ($\lt W$): dok je $\sum x_i \gt W$, odreži najveći panj kao samostalan komad (jedan rez); ostatak $\le W$ spoji s roditeljskim segmentom. Sortiranje panjeva daje $O(n\log n)$.</p>
''',
    ],
    'coach': [
        ('Opažanje 1: režemo odozdo',
         r'''
<p>Komad koji sadrži list može se odrezati na točno $W$ bez gubitka (zamjenski argument: bilo koje optimalno rješenje može se preurediti da svaki „donji” rez bude što viši). Dakle svaki segment težine $M$ s panjem $s$ ispod daje $\lfloor (M + s)/W \rfloor$ komada i ostatak.</p>
'''),
        ('Opažanje 2: grananje',
         r'''
<p>Panjevi djece $x_i \lt W$ svi su spojeni na isti čvor grananja. Ako $\sum x_i \le W$, ostaju zajedno i prenose se gore. Inače neki moraju postati vlastiti komadi: isplati se odvojiti najveće (svaki odvojen panj košta jedan komad, a najveći najviše smanjuje zbroj), dok zbroj ne padne na $\le W$; rez „neposredno prije grananja” to dopušta.</p>
'''),
        ('Opažanje 3: zašto je pohlepno optimalno',
         r'''
<p>Broj komada = broj rezova + 1. Odvajanje najvećeg panja dominira odvajanje bilo kojeg manjeg (isti trošak, manji ostatak koji putuje gore). Ostatak koji ide gore uvijek želimo najmanji uz isti broj rezova.</p>
'''),
        ('Algoritam i složenost',
         r'''
<p>Rekurzija/eksplicitni stog po ulaznom opisu (dubina do $10^5$ — koristi iterativno ili povećaj stog). Sortiraj panjeve djece: $O(n\log n)$. Težine do $10^9$, zbrojevi u 64 bita.</p>
'''),
    ],
    'solution': r'''
<p>Izrezati stablo na dijelove veličine najviše $W$ s najmanjim brojem rezova.</p>
<ul>
    <li>Rekurzivan ulaz.</li>
    <li>Pohlepna strategija: stablo „obrezujemo“ od listova prema korijenu — odrezujemo komade veličine točno $W$.</li>
    <li>Čvor s „panjevima“ (ostatcima) djece veličina $x_i &lt; W$:
        <ul>
            <li>ako je $\sum x_i &gt; W$, odrezujemo najveće panjeve (dok zbroj ne padne na najviše $W$);</li>
            <li>ako je $\sum x_i \le W$, ostatak prenosimo u roditeljski segment i njega režemo.</li>
        </ul>
    </li>
    <li>$\mathrm{solve}(a)$ — optimalno rezanje podstabla s korijenom u $a$: vraća najmanji broj rezova i preostalu veličinu panja.</li>
    <li>Složenost $O(n \log n)$ (zbog sortiranja panjeva); izazov: $O(n)$.</li>
</ul>
''',
},
{
    'letter': 'E',
    'title': 'Denormalization',
    'title_hr': 'Denormalizacija',
    'slug': 'E_denormalization',
    'tl': '5 s',
    'ml': '256 MB',
    'statement': r'''
<p>Popis cijelih brojeva $A = [a_1, \dots, a_N]$ ($1 \le a_i \le 10\,000$, $\gcd = 1$) normaliziran je dijeljenjem s $d = \sqrt{\sum a_i^2}$ i zaokružen na 12 decimala u $X = [x_1, \dots, x_N]$. Rekonstruiraj bilo koji popis $R$ cijelih brojeva iz $[1, 10\,000]$ s $\gcd = 1$ čija se normalizacija razlikuje od $X$ za najviše $10^{-6}$ po komponenti.</p>
<h3>Ulaz</h3>
<p>$N$ ($2 \le N \le 10\,000$) i $N$ brojeva $x_i$ ($0 &lt; x_i &lt; 1$) s točno 12 decimala.</p>
<h3>Izlaz</h3>
<p>$N$ rekonstruiranih cijelih brojeva.</p>
''',
    'hints': [
        r'''
<p>Omjeri $a_i/a_{\min}$ vidljivi su iz $x_i/x_{\min}$ (do greške zaokruživanja). Nepoznat je samo $a_{\min} = k \in [1, 10^4]$.</p>
''',
        r'''
<p>Za svaki $k$ izračunaj $r_i = k\,x_i/x_{\min}$ i provjeri jesu li svi blizu cijelih brojeva (tolerancija izvedena iz $10^{-6}$ relativno) — prvi $k$ koji prođe je odgovor; $\gcd$ se automatski slaže jer je rezultat unutar tolerancije. $O(10^4 \cdot N)$ s ranim prekidom.</p>
''',
    ],
    'coach': [
        ('Opažanje 1: što je izgubljeno',
         r'''
<p>Normalizacija gubi samo skalar $d$; omjeri komponenti ostaju (do $10^{-12}$). Umjesto da pogađamo $d$ (kontinuum), pogađamo jednu cjelobrojnu komponentu — npr. najmanju, $k \le 10^4$.</p>
'''),
        ('Opažanje 2: provjera kandidata',
         r'''
<p>$r_i = k\cdot x_i/x_{\min}$ treba biti cijeli broj $\le 10^4$; zaokruži $R_i = \mathrm{round}(r_i)$ i provjeri $|R_i/\|R\| - x_i| \le 10^{-6}$ (ili jednostavnije $|r_i - R_i|$ malen). Prvi valjani $k$ je najmanji, pa je $\gcd(R) = 1$ (inače bi $k/\gcd$ prošao ranije).</p>
'''),
        ('Algoritam i složenost',
         r'''
<p>Petlja $k = 1..10^4$, unutarnja provjera prekida pri prvom lošem $i$ — u praksi brzo. Najgore $O(A\cdot N) = 10^8$ jednostavnih operacija, unutar 5 s. Koristi <code>double</code>/<code>long double</code>.</p>
'''),
    ],
    'solution': r'''
<p>Poništiti normalizaciju popisa malih cijelih brojeva.</p>
<ul>
    <li>Mogućih duljina vektora $d = \sqrt{\sum a_i^2}$ previše je da bismo ih sve probali.</li>
    <li>Međukorak: normalizirajmo na $\min = 1$ (podijelimo s $k = \min(a)$).</li>
    <li>Obrnuti smjer:
        <ul>
            <li>norm $\to$ min: podijelimo sve $x_i$ s $\min(x)$;</li>
            <li>min $\to$ $a$: $a_i = \mathrm{min}_i \cdot k$ za $1 \le k \le 10\,000$; tražimo cijeli $k$ za koji su $a_i$ najbliži cijelim brojevima i unutar dopuštenog raspona.</li>
        </ul>
    </li>
    <li>Složenost $O(AN)$, gdje je $A = 10\,000$ gornja granica vrijednosti.</li>
    <li>Ideja se svodi na pretpostavku o vrijednosti $\min(a)$ ili $\max(a)$.</li>
</ul>
<p>Primjer: $a = (5, 6, 10, 15, 30, 6)$, $x/\text{norm} = (0.138, 0.165, 0.275, 0.413, 0.825, 0.165)$, nakon dijeljenja s minimumom $(1.000, 1.196, 1.993, 2.993, 5.978, 1.196)$; množenje s $k = 5$ daje cijele brojeve.</p>
''',
},
{
    'letter': 'F',
    'title': 'Differences',
    'title_hr': 'Razlike',
    'slug': 'F_differences',
    'tl': '2 s',
    'ml': '256 MB',
    'statement': r'''
<p>Zadano je $N$ nizova duljine $M$ nad alfabetom $\{A, B, C, D\}$. Udaljenost dvaju nizova je broj pozicija na kojima se razlikuju (Hammingova udaljenost). Točno jedan poseban niz ima udaljenost $K$ do svih ostalih; pronađi njegov indeks.</p>
<h3>Ulaz</h3>
<p>$N, M, K$ ($2 \le N, M \le 10^5$, $1 \le K \le M$, $NM \le 2 \cdot 10^7$) i $N$ nizova.</p>
<h3>Izlaz</h3>
<p>Indeks posebnog niza.</p>
''',
    'hints': [
        r'''
<p>Za niz $S_x$ udaljenost do svih ostalih zbrajanjem po pozicijama: $\sum_j \#\{i : S_{i,j} \ne S_{x,j}\}$ daje zbroj udaljenosti, ali zbroj nije dovoljan — treba „svi jednaki $K$”.</p>
''',
        r'''
<p>Umjesto brojeva koristi polinomni hash po indeksu niza: $f(j,c) = \sum_{i:\,S_{i,j}=c} p^i$. Vektor udaljenosti od $S_x$ hashiran je kao $\sum_j (g(j) - f(j, S_{x,j}))$; usporedi s hashem ciljnog vektora $K\sum_i p^i - K p^x$. $O(NM)$.</p>
''',
    ],
    'coach': [
        ('Opažanje 1: potreban je cijeli vektor, ne zbroj',
         r'''
<p>Poseban niz ima vektor udaljenosti $(K, \dots, K, 0, K, \dots)$. Zbroj $K(N-1)$ mogu imati i drugi nizovi (npr. $K-1$ i $K+1$), pa provjera zbrojem nije dovoljna, ali izračun zbroja vodi na ideju.</p>
'''),
        ('Opažanje 2: linearnost po pozicijama',
         r'''
<p>Vektor udaljenosti od $S_x$ je $\sum_j \mathbf 1[S_{\cdot, j} \ne S_{x,j}]$ — zbroj indikatorskih vektora po pozicijama. Indikatorski vektor „razlikuje se na $j$” = (svi) $-$ (oni sa znakom $S_{x,j}$ na $j$). Za sve $x$ odjednom treba samo $4M$ različitih vektora.</p>
'''),
        ('Redukcija: hash umjesto vektora',
         r'''
<p>Zamijeni vektor $v$ skalarom $H(v) = \sum_i v_i p^i \bmod q$ — linearno, pa je $H(\text{vektor od } S_x) = \sum_j \bigl(G_j - F_{j, S_{x,j}}\bigr)$ s $F_{j,c} = \sum_{i: S_{i,j} = c} p^i$, $G_j = \sum_c F_{j,c}$. Cilj: $H = K\cdot\sum_i p^i - K p^x$. Dva modula ili 64-bitni za sigurnost; poseban niz je jedinstven po uvjetu zadatka.</p>
'''),
        ('Složenost',
         r'''
<p>Predizračun $F$: $O(NM)$; provjera po $x$: $O(M)$; ukupno $O(NM) \le 2\cdot10^7$.</p>
'''),
    ],
    'solution': r'''
<p>Naći niz s Hammingovom udaljenošću $K$ do svih ostalih nizova.</p>
<ul>
    <li>$O(N^2 M)$ je prespor.</li>
    <li>Unaprijed izračunamo skupove nizova koji imaju znak $c$ na poziciji $j$: $f(j, c)$.</li>
    <li>Skup nizova koji se od $S_x$ razlikuju na poziciji $j$ je unija skupova $f(j, c)$ za $c \ne S_{x,j}$; zbrajanjem po pozicijama dobivamo Hammingove udaljenosti od $S_x$.</li>
    <li>Ubrzanje: skupove predstaviti bitmaskama? Bolje — <b>polinomnim hashevima</b>, ukupno $O(NM)$.</li>
    <li>Npr. $f(0, A) = (p^0 + p^2) \bmod mod$ ako nizovi $0$ i $2$ imaju $A$ na poziciji $0$; $g(j) = \sum_c f(j, c)$.</li>
    <li>Za $S_x$: $\sum_j \bigl(g(j) - f(j, S_{x,j})\bigr)$ treba biti jednako $\sum_i K p^i - K p^x$ (udaljenost $K$ do svih ostalih, $0$ do sebe).</li>
</ul>
<p>Primjer: $S = \{AB, BA, AB, CA, CA, CC\}$, $S_x = CA$: $d = [2, 1, 2, 0, 0, 1]$, cilj: $[K, K, K, 0, K, K]$.</p>
''',
},
{
    'letter': 'G',
    'title': 'Greedy Drawers',
    'title_hr': 'Pohlepne ladice',
    'slug': 'G_greedy_drawers',
    'tl': '2 s',
    'ml': '256 MB',
    'statement': r'''
<p>Janko ima $N$ bilježnica $(A_i, B_i)$ i $N$ ladica $(X_j, Y_j)$; bilježnica se može rotirati i stane u ladicu ako joj stranice ne prelaze odgovarajuće stranice ladice. Janko pohlepno bira objekt (bilježnicu ili ladicu) s najmanje mogućnosti i slučajno mu dodjeljuje jednu od njih. Konstruiraj ulaz (dimenzije od $1$ do $1000$) za koji potpuno pridruživanje postoji, ali Jankov postupak ne uspijeva.</p>
<h3>Ulaz</h3>
<p>$N$ ($150 \le N \le 250$).</p>
<h3>Izlaz</h3>
<p>$N$ bilježnica, prazan redak, $N$ ladica. Ocjenjuje se na 20 testova s fiksnim sjemenom slučajnosti; postupak mora zakazati na svima.</p>
''',
    'hints': [
        r'''
<p>Jankov postupak bira objekt s najmanje opcija, ali kad ih je više s istim brojem, bira slučajno — konstruiraj mali „gadget” u kojem slučajni odabir s vjerojatnošću $1/2$ vodi u slijepu ulicu, pa ga ponovi mnogo puta neovisno.</p>
''',
        r'''
<p>Npr. 8 objekata po gadgetu: bilježnice i ladice sa simetričnim rasponima tako da postoji jedinstveno savršeno uparivanje, ali je prvi izbor dvosmislen. S $\ge 150/8 \approx 18$ neovisnih kopija, vjerojatnost da sve prođu je $2^{-18}$; ostale bilježnice/ladice popuni trivijalnim parovima koji ne smetaju (npr. jedinstvene dimenzije).</p>
''',
    ],
    'coach': [
        ('Opažanje 1: gdje pohlepnost griješi',
         r'''
<p>„Objekt s najmanje mogućnosti” je dobra heuristika, ali slučajni odabir među njegovim opcijama nije: ako bilježnica stane u dvije ladice, a jedna od tih ladica jedina je opcija za neku drugu bilježnicu koja će biti razmotrena kasnije (jer sada ima više opcija), greška je vjerojatnosti $1/2$.</p>
'''),
        ('Opažanje 2: neovisnost gadgeta',
         r'''
<p>Da kopije ne interferiraju, dimenzije gadgeta $t$ smjesti u vlastiti raspon (npr. pomak $4t$) tako da bilježnice jednog gadgeta ne stanu u ladice drugog. Rotacija: koristi dimenzije s $A \le B$ i $X \le Y$ pa je usporedba jednostavna. Granice $1..1000$ dopuštaju $\ge 200$ gadgeta.</p>
'''),
        ('Opažanje 3: potvrda vjerojatnosti',
         r'''
<p>Postupak s fiksnim sjemenom mora zakazati na svih 20 testova: $P(\text{uspjeh}) = \bigl(1 - 2^{-g}\bigr)^{20}$ s $g \approx 18$ kopija $\Rightarrow \approx 99.99\%$. Ako sumnjaš, simuliraj Jankov algoritam lokalno na svojoj konstrukciji.</p>
'''),
    ],
    'solution': r'''
<p>Konstruirati kontraprimjer za pohlepno pridruživanje bilježnica ladicama.</p>
<ul>
    <li>Stane li bilježnica u ladicu? Dovoljno je promatrati vodoravnu orijentaciju.</li>
    <li>Mogući kontraprimjer:
        <ul>
            <li>bilježnice dimenzija $(1, x), (2, x-1), \dots, (x, x)$;</li>
            <li>ladica može primiti raspon bilježnica;</li>
            <li>u malom uzorku postoji 50 % šanse za suboptimalno pridruživanje;</li>
            <li>uzorak ponavljamo.</li>
        </ul>
    </li>
    <li>Vjerojatnost uspjeha (pohlepni postupak nađe suboptimalno rješenje): za jedan test $p_1 = 1 - 0.5^{150/8}$, za svih 20 testova $p = p_1^{20} \approx 99.995\,\%$.</li>
</ul>
''',
},
{
    'letter': 'H',
    'title': 'Insertions',
    'title_hr': 'Umetanja',
    'slug': 'H_insertions',
    'tl': '1 s',
    'ml': '256 MB',
    'statement': r'''
<p>Zadani su nizovi $s$, $t$ i $p$. Umetanje $t$ u $s$ na poziciji $k$ ($0 \le k \le |s|$) daje niz od prvih $k$ znakova $s$, cijelog $t$ i ostatka $s$. Odaberi $k$ tako da rezultat sadrži najviše (moguće preklapajućih) pojavljivanja $p$. Ispiši maksimum, broj takvih $k$, najmanji i najveći takav $k$.</p>
<h3>Ulaz</h3>
<p>$s$, $t$, $p$ (mala slova, duljine do $10^5$).</p>
<h3>Izlaz</h3>
<p>Četiri tražena broja.</p>
''',
    'hints': [
        r'''
<p>Za svaki $k$: broj pojavljivanja $= \mathrm{occ}(S) + \mathrm{occ}(T) - (\text{pojavljivanja u } S \text{ koja } k \text{ razbija}) + (\text{nova pojavljivanja preko granica})$. Prva dva su konstante, treće je prefiksni zbroj nad početcima pojavljivanja u $S$ (KMP).</p>
''',
        r'''
<p>Nova pojavljivanja s $|P| \le |T|$ prelaze točno jednu granicu ($S[:k]|T$ ili $T|S[k:]$): za granicu lijevo treba prefiks $P$ koji je sufiks $S[:k]$ (KMP stanje i njegov lanac neuspjeha) uparen s odgovarajućim sufiksom $P$ koji je prefiks $T$ (Z-funkcija $P$ vs $T$). Za $|P| \gt |T|$ pojavljivanje može obuhvatiti cijeli $T$: treba brojati parove (prefiks $P$ na kraju $S[:k]$, sufiks $P$ na početku $S[k:]$) čije duljine zbrojene s $|T|$ daju $|P|$ i $T$ sjeda na sredinu — rješava se na stablima funkcija neuspjeha uz sqrt-dekompoziciju, $O(|P|^{1.5})$.</p>
''',
    ],
    'coach': [
        ('Opažanje 1: rastavi doprinos',
         r'''
<p>Pojavljivanja u rezultatu: unutar $S[:k]$, unutar $T$, unutar $S[k:]$ (konstante uz prefiksne zbrojeve), ili preko granica. Razbijena pojavljivanja u $S$: ona s početkom $b$ takvim da $b \lt k \lt b + |P|$ — prefiksni zbroj indikatorskih početaka.</p>
'''),
        ('Opažanje 2: jedna granica ($|P| \\le |T|$)',
         r'''
<p>Pojavljivanje preko lijeve granice = prefiks $P$ duljine $\ell$ koji je sufiks $S[:k]$ i $P[\ell:]$ prefiks $T$. Skup takvih $\ell$ za $S[:k]$ je lanac funkcije neuspjeha iz KMP stanja $\pi_k$; skup $\ell$ za koje je $P[\ell:]$ prefiks $T$ je fiksan (iz Z-funkcije $P\#T$). Broj u presjeku: DP po lancu neuspjeha $\mathrm{cnt}[\ell] = \mathrm{cnt}[\mathrm{fail}(\ell)] + [\ell \text{ dobar}]$. Simetrično za desnu granicu s obrnutim nizovima.</p>
'''),
        ('Opažanje 3: preko cijelog $T$ ($|P| \\gt |T|$)',
         r'''
<p>Treba $\ell$ (prefiks $P$ na kraju $S[:k]$), $r$ (sufiks $P$ na početku $S[k:]$) s $\ell + |T| + r = |P|$ i $P[\ell : \ell + |T|] = T$ (pozicije gdje se $T$ pojavljuje u $P$, KMP). Par $(\ell, r)$ leži na lancima neuspjeha dvaju automata ($P$ i obrnuti $P$). Funkcija $x(i, j)$ = broj kompatibilnih parova na lancima iz $i$ i $j$; rekurzija $x(i,j) = x(i, g(j)) + \mathrm{match}$; sqrt-dekompozicija stabla neuspjeha: pretprocesiraj $x$ za $O(\sqrt{|P|})$ „posebnih” čvorova pa svaki upit skoči do najbližeg posebnog u $O(\sqrt{|P|})$ koraka.</p>
'''),
        ('Složenost',
         r'''
<p>$O(|S| + |T| + |P|^{1.5})$; napomena: mnogi timovi prolaze i s jednostavnijim $O(|S|\cdot\sqrt{|P|})$ ili hashiranjem uz pažljivu implementaciju.</p>
'''),
    ],
    'solution': r'''
<p>Umetnuti $T$ u $S$ tako da broj pojavljivanja uzorka $P$ bude najveći.</p>
<ul>
    <li>Promatramo sva umetanja nakon $k$ znakova.</li>
    <li>Prebrojimo pojavljivanja $P$ u $S$ i u $T$, oduzmemo ona u $S$ koja umetanje razbija (KMP daje pozicije $P$ u $S$ i $T$) i dodamo nova pojavljivanja koja prelaze granice umetnutog $T$.</li>
</ul>
<h3>a) Mali uzorci, $|P| \le |T|$</h3>
<ul>
    <li>$p$ = duljina najduljeg prefiksa $P$ koji je sufiks $S[:k]$ (faza pretraživanja KMP-a).</li>
    <li>Postoji li odgovarajući sufiks $P$ (duljine $x = |P| - p$) na početku $T$? Odnosno: je li duljina najduljeg sufiksa $P$ koji završava u $T[L]$ (Z-algoritam) jednaka $L$?</li>
    <li>Unaprijed izračunamo podudaranja i za kraće prefikse (funkcija neuspjeha KMP-a).</li>
    <li>Simetrično za granicu između $T$ i $S[k:]$.</li>
    <li>$O(|S| + |T| + |P|)$.</li>
</ul>
<h3>b) Veliki uzorci, $|P| &gt; |T|$</h3>
<ul>
    <li>Pojavljivanje se može protezati preko cijelog $T$.</li>
    <li>Podudara li se $T$ s pomaknutim $P$? KMP pretraživanje $T$ u $P$.</li>
    <li>Koliko se prefiksa $P$ na kraju $S[:k]$ podudara sa sufiksima $P$ na početku $S[k:]$ (uz $T$ između)?
        <ul>
            <li>svi parovi kraćih prefiksa i sufiksa: $O(|S| \cdot |P|^2)$;</li>
            <li>samo kraći prefiksi: $O(|S| \cdot |P|)$ — kao kod malih uzoraka (Z-algoritam).</li>
        </ul>
    </li>
    <li>Stabla funkcija neuspjeha KMP-a $f(i)$ za $P$ i $g(j)$ za obrnuti $P$:
        <ul>
            <li>$x(i, j)$ = broj podudarnih čvorova (s ispravnim zbrojem duljina) na putevima od $i$ i $j$ do korijena;</li>
            <li>$x(i, j) = x(i, g(j)) + \mathrm{match}_j(i) = x(f(i), j) + \mathrm{match}_i(j)$;</li>
            <li>pretprocesiranje $O(|P|^{1.5})$: $x(i, 0)$ te $x(i', j)$ za dobro raspoređene posebne čvorove $i'$ (uključujući korijen) — podstabla veličine $\sqrt{n}$;</li>
            <li>$x(i, j)$: pomičemo se prema korijenu do prvog posebnog čvora ($\le \sqrt{n}$ koraka).</li>
        </ul>
    </li>
    <li>Ukupno $O(|S| + |T| + |P|^{1.5})$.</li>
</ul>
''',
},
{
    'letter': 'I',
    'title': 'Money Laundering',
    'title_hr': 'Pranje novca',
    'slug': 'I_money_laundering',
    'tl': '2 s',
    'ml': '256 MB',
    'statement': r'''
<p>Tvrtke su djelomično u vlasništvu osoba i drugih tvrtki (uključujući sebe). Krajnji vlasnički udio osobe u tvrtki dobiva se beskonačnim ponavljanjem isplate dobiti vlasnicima proporcionalno udjelima. Tvrtke su organizirane u sektore: između tvrtki različitih sektora vlasništvo (ni neizravno) ne može ići u oba smjera; sektor ima manje od $10$ tvrtki. Za svaku tvrtku ispiši krajnje udjele svih osoba.</p>
<h3>Ulaz</h3>
<p>$c$ tvrtki i $p$ osoba ($\le 10^3$); za svaku tvrtku broj vlasnika i unosi <code>Px:udio</code> / <code>Cy:udio</code> (postotci s jednom decimalom, zbroj $100$). Ukupno najviše $10^4$ unosa; svaka tvrtka ima barem jednog krajnjeg vlasnika.</p>
<h3>Izlaz</h3>
<p>Za svaku tvrtku udjeli svih $p$ osoba (greška $&lt; 10^{-4}$).</p>
''',
    'hints': [
        r'''
<p>Isplata je linearna: vektor prihoda tvrtki $x \mapsto Ax$, gdje $A_{ij}$ = udio koji tvrtka $i$ drži u $j$. Ukupno isplaćeno osobama $= P\,(I + A + A^2 + \dots)x = P(I-A)^{-1}x$.</p>
''',
        r'''
<p>Sektor = jako povezana komponenta, veličine $\lt 10$: obradi SCC-ove u topološkom poretku, unutar svake riješi sustav $(I - A_S)y = x$ Gaussovom eliminacijom ($10^3$ operacija), pa raspodijeli osobama i tvrtkama nizvodno. $O(\sum S^3 + K\cdot p)$.</p>
''',
    ],
    'coach': [
        ('Opažanje 1: beskonačna isplata kao geometrijski red',
         r'''
<p>Tvrtka $j$ isplaćuje dobit vlasnicima proporcionalno; dio ide osobama (izlazi iz sustava), dio drugim tvrtkama (ostaje). Jer svaka tvrtka ima krajnjeg vlasnika, $A^k \to 0$ i $\sum A^k = (I-A)^{-1}$ postoji. Krajnji udio osobe $u$ u tvrtki $j$ je $u$-ta komponenta od $P(I-A)^{-1}e_j$.</p>
'''),
        ('Opažanje 2: struktura — mali SCC-ovi',
         r'''
<p>Puna inverzija $1000\times1000$ za svaki od $1000$ stupaca je preskupa; ali vlasništvo među sektorima ide samo jednosmjerno, pa je graf tvrtki DAG sektora s komponentama $\le 9$ tvrtki. Riješi sektor po sektor u topološkom poretku: prihod koji uđe u sektor (iz izvorne tvrtke $j$ ili iz uzvodnih sektora) preraspodijeli unutar sektora malim sustavom, pa proslijedi osobama i nizvodnim tvrtkama.</p>
'''),
        ('Algoritam',
         r'''
<p>Za svaku početnu tvrtku $j$ (ili vektorizirano: matrica $X$, $X_{i,j}$ = prihod $i$ koji potječe od $j$): Tarjan za SCC, topološki poredak, za komponentu $S$ riješi $(I - A_{SS})Y = X_S$ (Gauss, $S \le 9$, $C$ desnih strana), $X_{\text{nizvodno}} \mathrel{+}= A_{\cdot S} Y$, udjeli osoba $\mathrel{+}= P_{\cdot S} Y$. Složenost: eliminacija po komponenti $O(S^3)$ plus $O(S^2)$ po desnoj strani, ukupno $O(\frac{C}{S}S^3 + C^2 S + KC)$ — uz $C \le 10^3$, $S \lt 10$ daleko unutar limita.</p>
'''),
    ],
    'solution': r'''
<p>Izračunati udjele osoba u mreži vlasništva tvrtki.</p>
<ul>
    <li>Simuliramo preraspodjelu: $x = [x_1, \dots, x_n]^T$ je vektor prihoda tvrtki, $A$ matrica preraspodjele, $x' = Ax$, gdje je $A_{i,j}$ udio koji $i$ prima od $j$. $A^k$ konvergira u $0$.</li>
    <li>Akumuliramo isplaćene vrijednosti: $o = x + Ax + A^2 x + \dots$
        <ol type="a">
            <li>geometrijski red: $o = (I - A)^{-1} x$; inverz Gauss–Jordanovom eliminacijom;</li>
            <li>metoda potenciranja: $y = [x_1, \dots, x_n, o_1, \dots, o_n]^T$, $B = \begin{bmatrix} A &amp; 0 \\ I &amp; I \end{bmatrix}$, $y' = By$; $B^{\text{velik}}$ brzim potenciranjem.</li>
        </ol>
    </li>
    <li>Industrijski sektori = jako povezane komponente (Tarjan, Kosaraju, …) — male su!</li>
    <li>Vlasnička struktura (prihod) dolazi iz prethodnih tvrtki u topološkom poretku komponenti.</li>
    <li>Matrica $X$: $X_{i,j}$ je prihod koji tvrtka $i$ prima od tvrtke $j$. Za svaku komponentu izdvojimo relevantnu podmatricu (dimenzija $S \times C$), propagiramo prihod unutar komponente i raspodijelimo ga osobama i tvrtkama.</li>
    <li>Složenost $O(\frac{C}{S} S^3 + KC)$, gdje je $C$ broj tvrtki, $K$ broj bridova, $S$ najveća veličina komponente.</li>
</ul>
''',
},
{
    'letter': 'J',
    'title': 'Mortgage',
    'title_hr': 'Hipoteka',
    'slug': 'J_mortgage',
    'tl': '3 s',
    'ml': '512 MB',
    'statement': r'''
<p>Andrej u svakom od $n$ mjeseci ima prihod $a_i$ (može biti negativan). Hipoteka od $x$ mjesečno tijekom $k$ mjeseci od mjeseca $s$ priuštiva je ako svaki mjesec može platiti $x$ koristeći prihod tog mjeseca i uštedu iz prethodnih mjeseci unutar intervala (prije $s$ ništa ne štedi). Za $m$ intervala $(s_i, k_i)$ odredi najveći cjelobrojni $x$; ako je negativan, ispiši <code>stay with parents</code>.</p>
<h3>Ulaz</h3>
<p>$n, m \le 2 \cdot 10^5$, $|a_i| \le 10^9$, $m$ intervala.</p>
<h3>Izlaz</h3>
<p>$m$ odgovora.</p>
''',
    'hints': [
        r'''
<p>Prefiksni zbrojevi $c_i = \sum_{j\le i} a_j$. Rata $x$ priuštiva na $[L, R]$ $\iff$ za sve $i \in [L, R]$: $c_i - c_{L-1} \ge (i - L + 1)x$. Dakle $x \le \min_i \frac{c_i - c_{L-1}}{i - L + 1}$ — najmanji nagib iz točke $(L-1, c_{L-1})$ prema točkama raspona.</p>
''',
        r'''
<p>Geometrija: najstrmiji pravac iz $(L-1, c_{L-1})$ ispod svih točaka $(i, c_i)$, $i\in[L,R]$, dodiruje donju konveksnu ovojnicu. Segmentno stablo s donjom ovojnicom po čvoru, upit = $O(\log n)$ čvorova $\times$ binarno pretraživanje tangente. $O(n\log n + m\log^2 n)$.</p>
''',
    ],
    'coach': [
        ('Opažanje 1: prevedi uvjet u nagibe',
         r'''
<p>Stanje nakon $i$-tog mjeseca je $c_i - c_{L-1} - (i-L+1)x \ge 0$. Maksimalni cijeli $x$ je $\lfloor \min_i (c_i - c_{L-1})/(i-L+1) \rfloor$ — minimalni nagib pravca kroz $(L-1, c_{L-1})$ i točku raspona.</p>
'''),
        ('Opažanje 2: konveksna ovojnica daje minimum nagiba',
         r'''
<p>Točka raspona s najmanjim nagibom prema fiksnoj točki lijevo od svih leži na donjoj konveksnoj ovojnici skupa; tangenta se nalazi binarnim (ternarnim) pretraživanjem po ovojnici jer je nagib unimodalan duž nje.</p>
'''),
        ('Redukcija: struktura za raspon',
         r'''
<p>Segmentno stablo: čvor drži donju ovojnicu svojih točaka ($O(n\log n)$ memorije i vremena izgradnje spajanjem sortiranih po $x$). Upit rastavlja $[L,R]$ na $O(\log n)$ čvorova; u svakom binarno pretraživanje $O(\log n)$. Alternativa: binarno pretraživanje po $x$ s donjom ovojnicom linearnih funkcija $s_i(x) = c_i - ix$ (isti red složenosti).</p>
'''),
        ('Detalji',
         r'''
<p>Prekoračenje: $c_i$ do $2\cdot10^{14}$, umnošci u usporedbi nagiba do $\approx 4\cdot10^{19}$ — <code>__int128</code> ili usporedba razlomaka pažljivo. Negativan rezultat $\Rightarrow$ <code>stay with parents</code>; $x = 0$ je dopušten.</p>
'''),
    ],
    'solution': r'''
<p>Za zadane mjesečne prihode izračunati najveću mjesečnu ratu koju si možemo priuštiti u rasponu mjeseci $[L, R]$.</p>
<h3>a) Algebarski pristup</h3>
<ul>
    <li>Za fiksnu ratu $x$: $b_j$ = stanje na kraju mjeseca $j$; uvjet je da su sva stanja u $[L, R]$ nenegativna — upit minimuma na rasponu (segmentno stablo).</li>
    <li>Nepoznat $x$? Uz prefiksne sume, $s_j(x) = \sum_{i \le j} a_i - jx$ linearna je funkcija od $x$; u svakom čvoru stabla pohranimo donju ovojnicu $s'(x)$ funkcija $s_j(x)$.</li>
    <li>Binarno tražimo $x$ tako da na rasponu vrijedi $s(x) \ge s_{L-1}(x)$; funkcija $s_{L-1}$ je najplića.</li>
    <li>$O(n \log n + m \log^2 n)$.</li>
</ul>
<h3>b) Geometrijski pristup</h3>
<ul>
    <li>Točke $(i, c_i)$, $c_i = \sum_{j=1}^{i} a_j$; upit $[L, R]$ traži najstrmiji pravac iz točke $L - 1$ koji leži ispod svih točaka raspona.</li>
    <li>Točke podijelimo u grupe; za svaku grupu donja ovojnica (hull), a grupe organiziramo u stablo: ukupno $O(n)$ grupa, a $O(\log n)$ grupa pokriva svaki upit.</li>
    <li>Binarno pretraživanje unutar grupe: najdulji prefiks ovojnice čiji su segmenti „u smjeru kazaljke“ u odnosu na pravac iz $L - 1$.</li>
    <li>Oprez s prekoračenjima (overflow).</li>
    <li>$O(n \log n + m \log^2 n)$.</li>
</ul>
''',
},
{
    'letter': 'K',
    'title': 'Skills in Pills',
    'title_hr': 'Vještine u pilulama',
    'slug': 'K_skills_in_pills',
    'tl': '1 s',
    'ml': '256 MB',
    'statement': r'''
<p>Pilula A uzima se tako da nema $k$ uzastopnih dana bez nje, pilula B tako da nema $j$ uzastopnih dana bez nje; obje se ne smiju uzeti istog dana. Koliko je najmanje pilula potrebno u $n$ dana?</p>
<h3>Ulaz</h3>
<p>$k, j, n$ ($2 \le n \le 10^6$, $2 \le k, j \le n$).</p>
<h3>Izlaz</h3>
<p>Najmanji broj pilula.</p>
''',
    'hints': [
        r'''
<p>Bez zabrane istog dana optimalno je uzimati što kasnije: A na dane $k, 2k, \dots$, B na $j, 2j, \dots$. Sudari nastaju na višekratnicima $\mathrm{lcm}(k,j)$.</p>
''',
        r'''
<p>Pri sudaru jednu pilulu uzmi dan ranije — što pomiče cijeli njezin daljnji raspored. Stanje: „upravo smo uzeli A pa B (ili B pa A) u dva uzastopna dana”; $f(\text{preostali dani}, AB/BA)$ — izračunaj sljedeći sudar u $O(1)$ i probaj obje varijante. Sudara je $O(n/\mathrm{lcm})$, DP je $O(n)$.</p>
''',
    ],
    'coach': [
        ('Opažanje 1: „što kasnije” je optimalno bez interakcije',
         r'''
<p>Za jednu pilulu s periodom $k$ minimalni broj u $n$ dana je $\lfloor n/k\rfloor$, postignut na danima $k, 2k, \dots$; svako ranije uzimanje samo pomiče raspored ulijevo (isto ili više pilula).</p>
'''),
        ('Opažanje 2: sudar i njegovo razrješenje',
         r'''
<p>Ako su A i B oba „dužna” na isti dan $d$, jedna se mora uzeti na $d-1$ (kasnije nije dopušteno). Nakon toga imamo A na $d-1$, B na $d$ (ili obrnuto) i rasporedi su fazno pomaknuti za $1$; sljedeći sudar ovisi samo o tom poretku, ne o povijesti — stanje je (dan, poredak).</p>
'''),
        ('Algoritam',
         r'''
<p>Simuliraj od zadnjeg sudara unatrag ili memoiziraj $f(d, \text{poredak})$: iz stanja izračunaj sljedeći dan $d'$ kad se rasporedi ponovno sudare (aritmetika po $k$, $j$: A dužna na $d-1 + k t$, B na $d + j s$) i broj pilula do tada, pa $\min$ od dvije mogućnosti. Stanja $O(n)$, prijelaz $O(1)$ ili $O(\log)$ s formulom.</p>
'''),
        ('Izazov',
         r'''
<p>Sublinearno: pohlepno pravilo (uvijek pomakni pilulu s većim periodom?) nije očito ispravno — primjer $k=2, j=3, n=8$ pokazuje da izbor mijenja rezultat (6 vs 7).</p>
'''),
    ],
    'solution': r'''
<p>Naći raspored s najmanjim brojem pilula koji izbjegava uzimanje obiju pilula istog dana.</p>
<ul>
    <li>Kad bismo smjeli uzeti obje pilule istog dana: pilulu uzimamo što kasnije (A svaki $k$-ti, B svaki $j$-ti dan).</li>
    <li>Razriješimo prvi „sudar“: jednu od pilula pomaknemo dan ranije — ali koju?</li>
    <li>Dinamičko programiranje: $f(n, AB)$ = najmanji broj pilula u preostalih $n$ dana ako smo u prethodna dva dana uzeli A pa B (i simetrično $f(n, BA)$). Izračunamo sljedeći sudar i probamo obje mogućnosti pomaka.</li>
    <li>$O(n)$.</li>
    <li>Izazov: sublinearno pohlepno rješenje.</li>
</ul>
<p>Primjer $k = 2$, $j = 3$, $N = 8$: „uzmi A ranije“ daje 6 pilula, „uzmi B ranije“ daje 7 pilula.</p>
''',
},
{
    'letter': 'L',
    'title': 'The Game',
    'title_hr': 'The Game',
    'slug': 'L_the_game',
    'tl': '1 s',
    'ml': '256 MB',
    'statement': r'''
<p>Solo kartaška igra: 98 karata $2, \dots, 99$, dva rastuća reda (od 1) i dva padajuća (od 100). U svakom potezu igrač iz ruke (8 karata) odigra dvije karte prema pravilima (veća na rastući, manja na padajući red, ili „trik unatrag“ ako je razlika točno 10), zatim vuče dvije. Vladimir igra po strogim prioritetima (najprije trik unatrag krajnje lijevom kartom i najgornjim redom, inače potez s najmanjom apsolutnom razlikom, krajnje lijeva karta, najgornji red). Za zadani špil ispiši završno stanje.</p>
<h3>Ulaz</h3>
<p>Permutacija skupa $\{2, \dots, 99\}$ — špil odozgo prema dolje.</p>
<h3>Izlaz</h3>
<p>Četiri reda, preostala ruka i preostali špil.</p>
''',
    'hints': [
        r'''
<p>Čista simulacija — pažljivo modeliraj stanje: 4 reda (vrh), ruka (uređena, redoslijed bitan za „krajnje lijeva”), špil.</p>
''',
        r'''
<p>Redoslijed odluka po potezu: (1) postoji li trik unatrag — uzmi krajnje lijevu kartu koja ga ima, na najgornji red; (2) inače među svim valjanim (karta, red) parovima izaberi najmanju apsolutnu razliku, pa najmanju poziciju u ruci, pa najgornji red. Dvije karte po potezu, zatim vuci dvije (ili manje ako špil presuši); stani kad nema poteza.</p>
''',
    ],
    'coach': [
        ('Opažanje 1: pravila u pseudokod',
         r'''
<p>Napiši funkcije <code>valid(card, row)</code> (rastući: <code>card &gt; top</code> ili <code>card == top-10</code>; padajući: <code>card &lt; top</code> ili <code>card == top+10</code>), <code>isBackwards(card, row)</code>, i <code>pickMove()</code> koji vraća par prema prioritetima. Igrač odigra točno dvije karte po potezu prije vučenja — provjeri uvjet završetka između njih.</p>
'''),
        ('Opažanje 2: uvjeti završetka i ispisa',
         r'''
<p>Ako igrač ne može odigrati potrebnu kartu (nema valjanog poteza), igra staje — ispiši redove, preostalu ruku (u trenutnom poretku) i preostali špil. Pazi na kraj špila: kad je špil prazan, i dalje igra dok ima poteza.</p>
'''),
        ('Provjera',
         r'''
<p>Testiraj na primjeru iz zadatka i na ručno konstruiranim rubnim slučajevima (trik unatrag na oba reda istodobno, razlike jednake na dva reda).</p>
'''),
    ],
    'solution': r'''
<p>Simuliraj opisanu kartašku igru.</p>
<ul>
    <li>Održavamo popise karata: redovi, ruka, špil.</li>
    <li>Pažljiva implementacija:
        <ul>
            <li>prioritet imaju potezi unatrag (trik s razlikom 10);</li>
            <li>inače odabir najboljeg običnog poteza;</li>
            <li>sortiranje po (apsolutna razlika, pozicija u ruci, red).</li>
        </ul>
    </li>
</ul>
''',
},
]
