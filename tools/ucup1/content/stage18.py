# -*- coding: utf-8 -*-
STAGE = {
    'no': 18,
    'name': 'Stage 18: Shenzhen',
    'source_name': 'May 27-28, 2023',
    'no_editorial': True,
    'community': True,
    'source_html': r'''
<p>Zadaci potječu s natjecanja The 2023 Guangdong Provincial Collegiate Programming Contest (GDCPC 2023). Tekst zadatka preveden je prema službenim <a href="https://contest.ucup.ac/download.php?type=attachments&amp;id=1245&amp;r=1">engleskim tekstovima zadataka</a>. Organizatori nisu objavili službena rješenja. Zadatak je dostupan na <a href="https://contest.ucup.ac/contest/1245">Universal Cup Judging System</a>.</p>
''',
}

PROBLEMS = [
# ---------------------------------------------------------------- A
{
    'letter': 'A', 'title': 'Is it well known in Poland?', 'title_hr': 'Je li to dobro poznato u Poljskoj?', 'slug': 'A_is_it_well_known_in_poland',
    'tl': '1 s', 'ml': '256 MiB',
    'statement': r'''
<p>Zadana je šuma korijenskih stabala u kojoj svaki vrh $u$ ima pozitivnu vrijednost $A_u$. Mali A i Mali B igraju naizmjence, A počinje. Igrač na potezu bira točno jedan <em>korijen</em> nekog stabla, uklanja ga i dobiva njegovu vrijednost; djeca uklonjenog korijena postaju novi korijeni. Igra završava kad su svi vrhovi uklonjeni; rezultat igrača je zbroj vrijednosti vrhova koje je uklonio.</p>
<p>Oba igrača igraju optimalno (maksimiziraju vlastiti rezultat). Početno je zadano jedno stablo s $n$ vrhova i korijenom $1$. Odredi konačni rezultat Malog A.</p>
<h3>Ulaz</h3>
<p>$2 \le n \le 10^5$; vrijednosti $1 \le a_i \le 10^9$; zatim $n - 1$ bridova.</p>
<h3>Izlaz</h3>
<p>Rezultat Malog A.</p>
<h3>Primjer</h3>
<p>$n = 5$, $a = (1, 5, 3, 2, 4)$, bridovi $1\text{-}2, 1\text{-}3, 2\text{-}4, 2\text{-}5$: $7$.</p>
''',
    'hints': [
        r'''
<p>Naslov aludira na poljski zadatak „Termity” (Potyczki Algorytmiczne 2013) – igru uklanjanja krajeva puta. Ovdje je verzija na stablu. Razmisli o vrhu $M$ s <em>najvećom</em> vrijednošću: ako je dostupan (korijen), zašto ga igrač na potezu uvijek uzima?</p>
''',
        r'''
<p>Ako $M$ nije korijen, tko god uzme njegova roditelja $x$, protivnik odmah uzima $M$. Par $(x,M)$ se dakle ponaša kao jedan „blok” koji otvaraču donosi neto $a_x-a_M\le0$ i vraća mu potez (dva poteza). Generaliziraj: blokovi s neto vrijednošću $d$ i parnošću broja vrhova.</p>
''',
        r'''
<p>Uvijek promatraj neparan blok $v$ s najvećim $d$: ako je korijen, igrač na potezu ga uzima; inače ga spoji s roditeljskim blokom $p$ (neparan $p$: $d_p-d_v$, postaje paran; paran $p$: $d_p+d_v$, postaje neparan). Prioritetni red + DSU daje $O(n\log n)$. Na kraju igrač na potezu uzima sve preostale parne blokove.</p>
''',
    ],
    'coach': [
        ('Kako uopće opisati rezultat igre s dva igrača koji zbrajaju vrijednosti?',
         r'''
<p>Ukupan zbroj $\Sigma=\sum a_v$ je fiksan, pa je dovoljno pratiti razliku $\text{net}=A-B$ pri optimalnoj igri; tada je $A=(\Sigma+\text{net})/2$. Igra je nul-sumska po razlici: igrač na potezu maksimizira $a_v-\text{val}(\text{ostatak})$, gdje je $\text{val}$ vrijednost ostatka za sljedećeg igrača.</p>
'''),
        ('Zašto igrač na potezu uvijek uzima dostupan vrh $M$ s globalno najvećom vrijednošću?',
         r'''
<p>To je <em>načelo pohlepnog poteza</em>: $\text{val}(G)=a_M-\text{val}(G\setminus M)$. Ideja dokaza (Idziaszek, „Termity”): ako igrač na potezu odigra nešto drugo, protivnik može odmah uzeti $M$; zamjenom uloga i „jekom” (kopiranjem) svih ostalih poteza pokaže se da igrač koji odgodi uzimanje najvrjednijeg dostupnog vrha ne može profitirati, jer $a_M$ nije manje ni od jednog drugog vrha koji bi mogao uzeti umjesto njega.</p>
'''),
        ('Što ako najvrjedniji vrh $M$ nije korijen?',
         r'''
<p>Neka je $x$ roditelj od $M$ ($a_x\le a_M$). Tko god ukloni $x$, otkriva $M$, koji je najvrjedniji dostupan vrh, pa ga protivnik odmah uzima. Dakle $x$ i $M$ uvijek nestaju u dva uzastopna poteza različitih igrača: otvarač para dobiva neto $a_x-a_M\le0$, a potez se vraća njemu, dok djeca od $M$ postaju korijeni. Zato par $(x,M)$ smijemo zamijeniti jednim <em>parnim blokom</em> neto vrijednosti $d=a_x-a_M$ na mjestu vrha $x$ (<em>načelo fuzije</em>). Igra na novom stablu ima istu vrijednost.</p>
'''),
        ('Kako se ista ideja ponavlja kad već imamo blokove?',
         r'''
<p>Svaki blok ima neto vrijednost $d$ (što otvarač dobije kroz sve poteze bloka) i parnost: neparan blok predaje potez protivniku, paran ga vraća otvaraču. Neparan blok $v$ s najvećim $d$ među neparnima igra ulogu najvrjednijeg vrha. Ako je korijen, igrač na potezu ga uzima: $\text{net}\mathrel{+}=\pm d_v$, potez prelazi. Inače neka je $p$ njegov roditeljski blok: tko otvori $p$, nakon $p$-ovih poteza netko otvara $v$. Ako je $p$ neparan, potez je prešao protivniku pa on uzima $v$: novi blok je paran s $d_p-d_v$. Ako je $p$ paran, potez se vratio otvaraču pa on sam uzima $v$: novi blok je neparan s $d_p+d_v$ i vraća se u red kandidata. Vrijednosti novih blokova nisu veće od $d_v$, pa obrada po padajućem $d$ ostaje konzistentna.</p>
'''),
        ('Što ostaje na kraju i zašto to uzima igrač na potezu?',
         r'''
<p>Kad više nema neparnih blokova, svi preostali blokovi su parni korijeni s $d\le0$ (paran blok nastaje kao $d_p-d_v$ uz $d_v\ge d_p$). Igrač na potezu mora otvoriti neki paran blok; nakon njegovih poteza potez mu se vraća u istoj situaciji, pa on otvara sve preostale blokove i plaća $\sum d$ (<em>načelo besplodnog poteza</em>). Time je $\text{net}$ potpuno određen.</p>
'''),
        ('Kako to učinkovito implementirati?',
         r'''
<p>Prioritetni red parova $(d_v,v)$ s lijenim brisanjem zastarjelih zapisa (blok je predstavnik DSU-a, neparan, ne uklonjen, $d$ jednak zapisanom); blokovi se spajaju DSU-om, a roditeljski blok nalazimo kao $\text{find}(\text{par}[\text{head}[v]])$ gdje je $\text{head}$ vršni vrh bloka. Svaki vrh uđe u red najviše jednom kao početni blok, a svako spajanje doda najviše jedan zapis: $O(n\log n)$.</p>
'''),
    ],
    'tips': [
        r'''<strong>Igre s uklanjanjem korijena/krajeva:</strong> prati razliku $A-B$ i traži lokalna načela (pohlepni potez za maksimum, fuzija roditelj–maksimum, besplodni potezi) koja sažimaju igru bez promjene vrijednosti.''',
        r'''Sažimanje u „blokove” s neto vrijednošću i parnošću je standardna forma tih igara; parnost govori komu se vraća potez, a to određuje predznak pri spajanju.''',
        r'''Prioritetni red s lijenim brisanjem (provjera da je zapis još aktualan) + DSU za spajanje čvorova stabla daje $O(n\log n)$ bez složenih struktura.''',
        r'''Za takve igre uvijek napiši minimax brute force na malim stablima ($n\le 10$) i usporedi – pogreške u predznacima parnosti inače je gotovo nemoguće uočiti.''',
    ],
    'solution': r'''
<p>Igra je verzija poljskog zadatka „Termity” na stablu. Pratimo $\text{net}=A-B$. Tri načela: (1) <em>pohlepni potez</em> – dostupan vrh najveće vrijednosti igrač na potezu uzima; (2) <em>fuzija</em> – ako najvrjedniji vrh $M$ ima roditelja $x$, tko god uzme $x$, protivnik odmah uzima $M$, pa se $(x,M)$ zamjenjuje parnim blokom neto vrijednosti $a_x-a_M$; (3) <em>besplodni potez</em> – parne blokove ($d\le0$) na kraju otvara i plaća igrač na potezu. Općenito održavamo blokove $(d,\text{parnost})$ i uvijek obrađujemo neparan blok $v$ s najvećim $d$: ako je korijen, $\text{net}\mathrel{+}=\pm d_v$ i potez prelazi; inače ga spajamo s roditeljskim blokom $p$: neparan $p\to$ paran s $d_p-d_v$, paran $p\to$ neparan s $d_p+d_v$ (natrag u red). Na kraju igrač na potezu dobiva zbroj preostalih parnih blokova; $A=(\sum a+\text{net})/2$. Prioritetni red + DSU, $O(n\log n)$. Ideja slijedi rad T. Idziaszeka o igri „Termity” (načela pohlepnog poteza, fuzije i besplodnog poteza) proširen na stabla, uz analizu prihvaćenih predaja; implementacija je napisana iznova i iscrpno provjerena minimaxom na malim stablima.</p>
''',
    'detailed': r'''
<h3>1. Postavka</h3>
<p>Neka je $\Sigma=\sum_v a_v$ i $\text{net}=A-B$ pri optimalnoj igri. Oba igrača maksimiziraju svoj zbroj, što je uz fiksni $\Sigma$ isto kao maksimizirati razliku u svoju korist; igra je dakle nul-sumska po $\text{net}$ i vrijedi $\text{val}(G)=\max_{\text{korijen }v}\big(a_v-\text{val}(G\setminus v)\big)$, gdje je $\text{val}$ razlika za igrača na potezu. Na kraju $A=(\Sigma+\text{net})/2$.</p>
<h3>2. Načelo pohlepnog poteza</h3>
<p><em>Tvrdnja.</em> Ako je korijen $M$ vrh s najvećom vrijednošću u cijeloj šumi, tada $\text{val}(G)=a_M-\text{val}(G\setminus M)$.</p>
<p><em>Skica dokaza</em> (prema radu o igri „Termity”): pretpostavimo da optimalna strategija $\sigma$ prvo uzima $v\ne M$. Promotrimo strategiju $\sigma'$ koja prvo uzima $M$, a zatim „jekom” kopira poteze igre u kojoj je $\sigma$ igrala protiv protivnika koji odmah uzima $M$ – s time da $\sigma'$ uzima $v$ u trenutku kad bi ga u toj igri uzeo protivnik, i obrnuto. Svi ostali vrhovi završe kod istih igrača, a $M$ i $v$ zamijene vlasnike: $\sigma'$ dobije $a_M-a_v\ge0$ više. Dostupnost vrhova pritom nije narušena jer je $M$ korijen (uklanjanje $M$ ne blokira ništa), a $v$ je bio dostupan već na početku. Dakle uzimanje $M$ nije lošije od bilo kojeg drugog poteza.</p>
<h3>3. Načelo fuzije</h3>
<p>Neka je $M$ globalno najvrjedniji vrh koji nije korijen i $x$ njegov roditelj ($a_x\le a_M$). Čim netko ukloni $x$, $M$ postaje korijen s najvećom vrijednošću, pa ga po načelu 2 protivnik odmah uzima. Zato u svakoj optimalnoj partiji $x$ i $M$ nestaju u dva uzastopna poteza različitih igrača; igrač koji otvori $x$ dobiva neto $a_x-a_M\le0$, potez se vraća njemu, a djeca od $M$ postaju korijeni. Igra je stoga ekvivalentna igri na stablu u kojem su $x$ i $M$ zamijenjeni jednim <em>parnim blokom</em> s neto vrijednošću $d=a_x-a_M$, čija su djeca (u stablu) djeca od $x$ osim $M$ te djeca od $M$: otvaranje bloka igraču donosi $d$ i potez mu se vraća.</p>
<h3>4. Blokovi s parnošću</h3>
<p>Općenito radimo s blokovima: povezani skup vrhova s vršnim vrhom (<em>head</em>), neto vrijednošću $d$ (ono što otvarač ukupno dobije umjesto protivnika tijekom poteza bloka) i parnošću broja vrhova. Neparan blok predaje potez protivniku, paran ga vraća otvaraču. Početno je svaki vrh neparan blok s $d=a_v$.</p>
<p>Uzmimo neparan blok $v$ s najvećim $d_v$ među neparnima. Tvrdimo da se $v$ ponaša kao „najvrjedniji vrh”: parni blokovi imaju $d\le0$ i nikome se ne isplati otvarati ih dok ima neparnih (vidi 5), a među neparnima je $v$ najprivlačniji.</p>
<ul>
<li>Ako je $v$ korijen: igrač na potezu ga uzima (načelo pohlepnog poteza), $\text{net}\mathrel{+}=s\cdot d_v$ gdje je $s=\pm1$ oznaka igrača na potezu; zatim $s\gets-s$ jer neparan blok predaje potez.</li>
<li>Ako $v$ ima roditeljski blok $p$ (blok koji sadrži roditelja vrha $\text{head}(v)$): tko god otvori $p$, nakon svih poteza bloka $p$ blok $v$ postaje dostupan i najvrjedniji, pa ga uzima igrač koji je tada na potezu. Ako je $p$ neparan, to je protivnik otvarača: spojeni blok je paran s $d_p-d_v$. Ako je $p$ paran, to je sam otvarač: spojeni blok je neparan s $d_p+d_v$ i vraćamo ga u red.</li>
</ul>
<p>Konzistentnost poretka: neparan $p$ ima $d_p\le d_v$ pa je novi paran blok $\le0$; paran $p$ ima $d_p\le0$ pa je $d_p+d_v\le d_v$ – nova vrijednost nikad ne premašuje trenutačni maksimum, dakle obrada po padajućem $d$ je valjana.</p>
<h3>5. Načelo besplodnog poteza</h3>
<p>Kad neparnih blokova više nema, svi preostali blokovi su parni korijeni s $d\le0$. Igrač na potezu mora otvoriti jedan od njih, dobiva $d\le0$ i potez mu se vraća u analognoj situaciji; indukcijom otvara sve i plaća $\sum d$: $\text{net}\mathrel{+}=s\cdot\sum d$. (U izvornom radu: $\text{val}(G)=\text{val}(G')+(-1)^{n}(a_x-a_M)$ za besplodni par, gdje je $n$ broj vrhova.)</p>
<h3>6. Algoritam</h3>
<ol>
<li>BFS iz korijena $1$ radi roditelja.</li>
<li>Svaki vrh je neparan blok $d_v=a_v$; svi u prioritetni red (max po $d$).</li>
<li>Dok red nije prazan: izvadi $(d,v)$; preskoči zastarjele zapise ($v$ nije predstavnik DSU-a, uklonjen je, paran je, ili $d\ne d_v$). Nađi roditeljski blok $p=\text{find}(\text{par}[\text{head}[v]])$ (ili nema ga / uklonjen je). Primijeni pravilo iz točke 4.</li>
<li>Preostale parne blokove pribroji sa znakom $s$; ispiši $(\Sigma+\text{net})/2$.</li>
</ol>
<h3>7. Složenost i zamke</h3>
<p>Svaki vrh uđe u red jednom, svako spajanje doda najviše jedan zapis; spajanja je $\le n-1$, pa je $O(n\log n)$ uz DSU. Vrijednosti do $10^9\cdot10^5$ – <code>long long</code>. Pri spajanju $v$ u $p$ vršni vrh bloka ostaje $\text{head}(p)$; roditelj bloka se određuje preko $\text{head}$, ne preko predstavnika DSU-a. Zapis u redu treba uspoređivati s trenutačnim $d_v$ jer se $d$ mijenja fuzijama. $\Sigma+\text{net}$ je uvijek paran ($\Sigma=A+B$, $\text{net}=A-B$).</p>
<h3>8. Primjer</h3>
<p>$a=(1,5,3,2,4)$, korijen $1$ s djecom $2,3$; $2$ ima djecu $4,5$. Najveći neparan blok je $2$ ($d=5$), roditelj blok $1$ (neparan, $d=1$): spajanje u paran blok $\{1,2\}$ s $d=-4$. Sljedeći: $5$ ($d=4$), roditelj je paran blok $\{1,2\}$: novi neparan blok $\{1,2,5\}$ s $d=0$. Sljedeći: $3$ ($d=3$), roditelj $\{1,2,5\}$ neparan: paran blok $d=0-3=-3$. Sljedeći: $4$ ($d=2$), roditelj paran ($-3$): neparan blok $d=-1$, sada korijen: A ga uzima, $\text{net}=-1$, potez B-u; ništa ne ostaje. $A=(15-1)/2=7$. Provjera partije: A uzima vrh $1$ (vrijednost $1$), B vrh $2$ ($5$), A vrh $5$ ($4$), B vrh $3$ ($3$), A vrh $4$ ($2$): $1+4+2=7$.</p>
''',
    'verified': r'''uzorak 1/1; 300 slučajnih stabala ($n\le 10$) protiv minimax brute forcea po podskupovima uklonjenih vrhova, plus dodatnih 4000 slučajnih šuma/stabala u lokalnoj skripti bez odstupanja; 3 velika testa ($n=10^5$: dugačak lanac, slučajno stablo, stablo blisko lancu), najsporiji $0.06$ s.''',
},
# ---------------------------------------------------------------- B
{
    'letter': 'B', 'title': 'Path Planning', 'title_hr': 'Planiranje puta', 'slug': 'B_path_planning',
    'tl': '3 s', 'ml': '1024 MiB',
    'statement': r'''
<p>Tablica $n \times m$ sadrži svaki cijeli broj od $0$ do $nm - 1$ točno jednom. Krećeš iz $(1, 1)$ do $(n, m)$ pomicanjem desno ili dolje. Neka je $S$ skup brojeva na putu (uključujući krajeve). Maksimiziraj $\operatorname{mex}(S)$ — najmanji nenegativan cijeli broj koji nije u $S$.</p>
<h3>Ulaz</h3>
<p>$T$ testova; $1 \le n, m \le 10^6$, $nm \le 10^6$, zatim tablica; $\sum nm \le 10^6$.</p>
<h3>Izlaz</h3>
<p>Za svaki test najveći mogući $\operatorname{mex}(S)$.</p>
<h3>Primjer</h3>
<p>Tablica $\begin{smallmatrix}1 & 2 & 4\\ 3 & 0 & 5\end{smallmatrix}$: $3$ (put $1, 2, 0, 5$). Redak $1\ 3\ 0\ 4\ 2$: $5$.</p>
''',
    'hints': [
        r'''
<p>Umjesto „koji put daje najveći mex” pitaj se: za zadani $x$, može li $\operatorname{mex} \ge x$? Što to znači za ćelije s vrijednostima $0, 1, \dots, x-1$?</p>
''',
        r'''
<p>Ako se $x$ može postići, može se i svaki manji $x$ – svojstvo je monotono, pa se odgovor može binarno pretraživati.</p>
''',
        r'''
<p>Skup ćelija leži na jednom monotonom (desno/dolje) putu točno onda kada, gledano po redovima odozgo prema dolje, raspon stupaca nikad ne „pada”: najmanji stupac u nekom retku nije manji od najvećeg stupca u prethodnim posjećenim redovima.</p>
''',
    ],
    'coach': [
        ('Koji je oblik odgovora i zašto je teško izravno maksimizirati mex duž puta?',
         r'''
<p>Mex ovisi o cijelom skupu vrijednosti na putu, a ne o zbroju ili maksimumu, pa klasično dinamičko programiranje po ćelijama nema malo stanje. Zato promijenimo pitanje: fiksirajmo prag $x$ i pitajmo se postoji li put s $\operatorname{mex} \ge x$. To vrijedi točno onda kada put prolazi kroz <em>sve</em> ćelije s vrijednostima $0, \dots, x-1$ (svaka je vrijednost u tablici točno jednom).</p>
'''),
        ('Zašto je svojstvo „postoji put kroz sve ćelije s vrijednostima $< x$” monotono u $x$?',
         r'''
<p>Ako put prolazi kroz sve ćelije s vrijednostima $< x$, prolazi i kroz sve ćelije s vrijednostima $< x'$ za $x' < x$ (to je podskup). Dakle skup dobrih $x$ je $\{0, 1, \dots, X\}$ i odgovor je najveći dobar $x$, koji nalazimo binarnim pretraživanjem u $O(\log(nm))$ provjera.</p>
'''),
        ('Kako u linearnom vremenu provjeriti leži li zadani skup ćelija na jednom monotonom putu?',
         r'''
<p>Put ide samo desno ili dolje, pa je uzduž puta redak nepadajući i stupac nepadajući. Skup ćelija je na jednom putu točno onda kada, poredamo li ih po retku pa po stupcu, stupci čine nepadajući niz. Za svaki redak dovoljno je pamtiti najmanji i najveći stupac zauzete ćelije: prolazimo retke odozgo, pamtimo najveći dosad viđeni stupac $\text{last}$ i zahtijevamo $\text{lo}_i \ge \text{last}$, nakon čega $\text{last} \gets \text{hi}_i$. Ako uvjet vrijedi, put očito možemo „provući”: unutar retka idemo desno od $\text{lo}_i$ do $\text{hi}_i$, potom dolje do sljedećeg zauzetog retka.</p>
'''),
        ('Koja je ukupna složenost i staje li u ograničenja?',
         r'''
<p>Jedna provjera je $O(x + n) \le O(nm)$ (obilazak $x$ vrijednosti i $n$ redaka), a provjera ima $O(\log(nm))$. Uz $\sum nm \le 10^6$ to je oko $2\cdot 10^7$ jednostavnih operacija – daleko unutar 3 s.</p>
'''),
    ],
    'tips': [
        r'''<strong>Prebaci maksimizaciju u odlučivanje.</strong> „Najveći mex” = „najveći $x$ takav da su sve vrijednosti $< x$ dostupne” – tipičan monoton predikat za binarno pretraživanje.''',
        r'''Skup ćelija leži na jednom monotonom (desno/dolje) putu akko poredan po (redak, stupac) ima nepadajuće stupce – provjera je linearna i vrijedi u mnogim zadacima s rešetkama.''',
        r'''Kad je $nm \le 10^6$, a $n$ ili $m$ može biti $10^6$, radi s nizovima duljine $nm$ indeksiranim vrijednošću (pozicija svake vrijednosti) umjesto dvodimenzionalne strukture.''',
    ],
    'solution': r'''
<p>Za prag $x$ vrijedi $\operatorname{mex}(S) \ge x$ točno onda kada put prolazi kroz sve ćelije s vrijednostima $0, \dots, x-1$. Skup ćelija leži na jednom monotonom putu akko, poredan po retku pa stupcu, ima nepadajuće stupce; to provjeravamo u $O(x+n)$ pamteći za svaki redak najmanji i najveći zauzeti stupac. Svojstvo je monotono u $x$, pa odgovor nađemo binarnim pretraživanjem: ukupno $O(nm \log(nm))$. Ideja slijedi službeno rješenje GDCPC-a 2023 i analizu prihvaćenih predaja; implementacija je napisana iznova.</p>
''',
    'detailed': r'''
<h3>1. Preformulacija</h3>
<p>Svaki broj od $0$ do $nm-1$ pojavljuje se točno jednom, pa je $\operatorname{mex}(S) \ge x$ ekvivalentno tvrdnji „put sadrži ćelije s vrijednostima $0, 1, \dots, x-1$”. Neka je $P_x$ skup tih $x$ ćelija. Odgovor je najveći $x$ za koji postoji monoton put koji sadrži cijeli $P_x$.</p>
<h3>2. Monotonost i binarno pretraživanje</h3>
<p>Ako put sadrži $P_x$, sadrži i $P_{x'} \subseteq P_x$ za svako $x' \le x$. Dakle predikat $\text{ok}(x)$ = „postoji put koji sadrži $P_x$” je nepadajući u „lažno” smjeru: $\text{ok}(0)$ je istina (prazan skup), a nakon prve laži sve je laž. Najveći istinit $x$ nalazimo binarnim pretraživanjem na $[0, nm]$; potrebno je $\lceil \log_2(nm+1) \rceil \le 20$ provjera.</p>
<h3>3. Kada skup ćelija leži na jednom monotonom putu</h3>
<p><strong>Tvrdnja.</strong> Skup ćelija $Q$ leži na nekom monotonom (desno/dolje) putu od $(1,1)$ do $(n,m)$ ako i samo ako za svake dvije ćelije $(r_1, c_1), (r_2, c_2) \in Q$ s $r_1 < r_2$ vrijedi $c_1 \le c_2$.</p>
<p><em>Nužnost.</em> Uzduž puta redak i stupac nikad ne padaju; ako je ćelija s manjim retkom posjećena prije (mora biti, jer se redak ne smanjuje), njezin stupac nije veći.</p>
<p><em>Dovoljnost.</em> Poredajmo $Q$ po retku, pa po stupcu. Uvjet kaže da je i stupac nepadajući, pa uzastopne ćelije $(r, c) \to (r', c')$ zadovoljavaju $r \le r'$ i $c \le c'$: spojimo ih tako da idemo dolje $r'-r$ puta pa desno $c'-c$ puta. Prvu ćeliju spojimo s $(1,1)$, zadnju s $(n,m)$ na isti način.</p>
<p>Uvjet po svim parovima svodi se na uvjet po redcima: za svaki redak $i$ koji sadrži ćelije iz $Q$ neka su $\text{lo}_i$ i $\text{hi}_i$ najmanji i najveći stupac. Prolazimo retke odozgo, pamtimo $\text{last}$ = najveći stupac u dosad obrađenim zauzetim redcima i zahtijevamo $\text{lo}_i \ge \text{last}$; nakon toga $\text{last} \gets \text{hi}_i$. Ako to vrijedi za sve retke, vrijedi i za sve parove (par u istom retku uvjet ne ograničava).</p>
<h3>4. Algoritam</h3>
<ol>
<li>Pročitaj tablicu i zapamti za svaku vrijednost $v$ njezin redak $\text{posR}[v]$ i stupac $\text{posC}[v]$.</li>
<li>$\text{ok}(x)$: postavi $\text{lo}_i = +\infty$, $\text{hi}_i = -\infty$; za $v = 0, \dots, x-1$ ažuriraj $\text{lo}, \text{hi}$ retka $\text{posR}[v]$; zatim provjeri uvjet iz točke 3 po redcima.</li>
<li>Binarno pretraži najveći $x \in [0, nm]$ s $\text{ok}(x)$ i ispiši ga.</li>
</ol>
<h3>5. Složenost</h3>
<p>Jedna provjera troši $O(x + n) = O(nm)$, provjera ima $O(\log(nm))$, ukupno $O(nm\log(nm))$ po testu, a $\sum nm \le 10^6$. Memorija $O(nm)$ za pozicije vrijednosti.</p>
<h3>6. Zamke</h3>
<ul>
<li>$n$ ili $m$ može biti $10^6$ (drugi jednak $1$) – ne alociraj matricu $n \times m$ po testu putem vektora vektora; koristi dva niza duljine $nm$.</li>
<li>Odgovor može biti $nm$ (svi brojevi na putu, npr. tablica $1 \times m$) – gornja granica pretraživanja mora biti $nm$, ne $nm-1$.</li>
<li>Ne zaboravi resetirati $\text{lo}/\text{hi}$ između provjera; radi samo po redcima koji su zauzeti (prazne retke preskoči, oni ne mijenjaju $\text{last}$).</li>
</ul>
<h3>7. Primjer</h3>
<p>Tablica $\begin{smallmatrix}1 & 2 & 4\\ 3 & 0 & 5\end{smallmatrix}$: $P_3 = \{(1,1),(1,2),(2,2)\}$ – redak 1 ima stupce $[1,2]$, redak 2 stupac $2 \ge 2$, uvjet vrijedi, pa $\text{ok}(3)$. $P_4$ dodaje $(2,1)$: redak 2 sada ima $\text{lo}=1 < 2$, uvjet pada. Odgovor $3$.</p>
''',
    'verified': r'''uzorci 2/2; 300 slučajnih testova ($nm \le 12$) protiv brute forcea koji nabraja sve monotone putove; 3 velika testa ($nm = 10^6$, uključujući $1 \times 10^6$ i $10^6 \times 1$), najsporiji $0.09$ s.''',
},
# ---------------------------------------------------------------- C
{
    'letter': 'C', 'title': 'New but Nostalgic Problem', 'title_hr': 'Nov, ali nostalgičan zadatak', 'slug': 'C_new_but_nostalgic_problem',
    'tl': '2 s', 'ml': '1024 MiB',
    'statement': r'''
<p>Dano je $n$ stringova $w_1, \dots, w_n$. Odaberi skup $S$ od $k$ različitih indeksa tako da string
$$v = \max_{i, j \in S,\ i \ne j} \operatorname{lcp}(w_i, w_j)$$
bude leksikografski <em>najmanji</em> mogući, gdje je $\operatorname{lcp}$ najdulji zajednički prefiks, a $\max$ uspoređuje stringove leksikografski (prazan string je najmanji; prefiks je manji od stringa). Ispiši optimalni $v$.</p>
<h3>Ulaz</h3>
<p>$T$ testova; $2 \le n \le 10^6$, $2 \le k \le n$, zatim stringovi malih engleskih slova; ukupna duljina svih stringova u svim testovima $\le 10^6$.</p>
<h3>Izlaz</h3>
<p>Za svaki test string $v$, ili <code>EMPTY</code> ako je prazan.</p>
<h3>Primjer</h3>
<p>$k = 3$, stringovi <code>gdcpc</code>, <code>gdcpcpcp</code>, <code>suasua</code>, <code>suas</code>, <code>sususua</code>: <code>gdcpc</code>. $k = 3$, stringovi <code>a</code>, <code>b</code>, <code>c</code>: <code>EMPTY</code>.</p>
''',
    'hints': [
        r'''
<p>Ubaci sve stringove u trie. Najdulji zajednički prefiks dvaju stringova je čvor trie-a (njihov najniži zajednički predak), pa je i odgovor $v$ neki čvor trie-a.</p>
''',
        r'''
<p>Fiksiraj kandidata $v$. Koliko najviše stringova možeš odabrati tako da svaki par ima $\operatorname{lcp} \le v$? Razmisli o tome gdje se, u odnosu na put od korijena do $v$, nalazi $\operatorname{lcp}$ para: na putu, u podstablu koje skreće manjim slovom ili u podstablu koje skreće većim slovom.</p>
''',
        r'''
<p>Odgovor gradi slovo po slovo: u trenutnom čvoru provjeri može li se stati; ako ne, spusti se u najmanje dijete čije podstablo još dopušta barem $k$ stringova (gornja granica je dostižna u listu).</p>
''',
    ],
    'coach': [
        ('Gdje uopće „žive” mogući odgovori i kako uspoređivati $\operatorname{lcp}$ vrijednosti?',
         r'''
<p>Za svaki par stringova $\operatorname{lcp}(w_i, w_j)$ je čvor trie-a: njihov najniži zajednički predak. Optimalni $v$ je maksimum takvih vrijednosti po parovima odabranog skupa, dakle i sam čvor trie-a. Uspoređujemo leksikografski: čvor $u$ je $\le v$ ako je $u$ predak od $v$ (uključivo $v$) ili se put do $u$ odvaja od puta do $v$ manjim slovom.</p>
'''),
        ('Za fiksni čvor $v$, koliko najviše stringova možemo odabrati tako da svi parovi imaju $\operatorname{lcp} \le v$?',
         r'''
<p>Promatraj put korijen $\to v$. Stringovi koji završavaju u čvoru puta imaju s bilo kime $\operatorname{lcp}$ koji je prefiks od $v$ – svi smiju ući. Podstablo djeteta koje s puta skreće <em>manjim</em> slovom: bilo koja dva stringa iz njega imaju $\operatorname{lcp}$ unutar tog podstabla, dakle $< v$ – ulazi cijelo. Podstablo koje skreće <em>većim</em> slovom: dva stringa iz njega imaju $\operatorname{lcp} > v$, pa smije najviše jedan. Iz svakog djeteta od $v$ također najviše jedan (njihov $\operatorname{lcp}$ bi bio strogo dulji od $v$). Zbroj tih doprinosa je $f(v)$ i to je točan maksimum, jer je takav izbor dopušten.</p>
'''),
        ('Kako od uvjeta $f(v) \ge k$ doći do leksikografski najmanjeg $v$ bez računanja $f$ u svakom čvoru?',
         r'''
<p>Spuštaj se od korijena. U čvoru $u$ akumulirani doprinos predaka je $\text{acc}$; ako $\text{acc} + \text{cntEnd}(u) + \deg(u) \ge k$, sam $u$ je odgovor – svi leksikografski manji kandidati odbačeni su ranije, a $u$ je najmanji string sa svojim prefiksom. Inače odgovor ima prefiks $u$ plus još jedno slovo. Za dijete $d$ gornja je granica za sve $v$ u njegovu podstablu $\text{acc} + \text{cntEnd}(u) + \sum_{c<d}\text{sz}(c) + \#\{c > d\} + \text{sz}(d)$ (cijelo podstablo $d$ najviše može ući). Idemo u najmanje $d$ s granicom $\ge k$.</p>
'''),
        ('Zašto je ta gornja granica dostižna i zašto neko dijete uvijek zadovoljava?',
         r'''
<p>Unutar podstabla $d$ doprinos čvora $v$ iznosi $\text{sz}(d) - \sum_{c\text{ dijete od }v}(\text{sz}(c) - 1)$ ako se spuštamo uvijek u najveće dijete (manja djeca ulaze cijela, većih nema). U listu je to točno $\text{sz}(d)$, pa se granica postiže. Nadalje vrijedi invarijanta $\text{acc} + \text{sz}(u) \ge k$ (u korijenu $n \ge k$; ulazak u $d$ čuva je jer je upravo granica $\ge k$), a granica za najveće dijete jednaka je $\text{acc} + \text{sz}(u)$, pa uvijek postoji izbor.</p>
'''),
        ('Kolika je složenost uz ukupnu duljinu $10^6$?',
         r'''
<p>Trie ima najviše $10^6+1$ čvorova; izgradnja je $O(L)$. Spuštanje posjećuje jedan put i u svakom čvoru radi $O(26)$ za nabrajanje djece plus $O(26)$ po postojećem djetetu, ukupno $O(26 L)$. Memorija $26 \cdot 10^6$ cijelih brojeva ($\approx 104$ MB) uz limit 1 GiB.</p>
'''),
    ],
    'tips': [
        r'''<strong>„Najmanji maksimum lcp-a” je pitanje o trieu:</strong> lcp para = najniži zajednički predak u trieu, a leksikografski poredak odgovara poretku obilaska trie-a.''',
        r'''Leksikografski najmanji odgovor tipično se gradi znak po znak: u svakom koraku provjeri „može li se ovdje stati”, a zatim uzmi najmanje slovo za koje postoji ijedno dovršenje – dovoljna je dostižna gornja granica po podstablu.''',
        r'''Kod globalnog polja <code>ch[MAXN][26]</code> resetiraj samo čvorove koje si koristio (u <code>newNode</code>), nikad cijelo polje po testu – $T$ može biti velik.''',
        r'''Ulaz od $10^6$ znakova čitaj vlastitim brzim čitačem (<code>fread</code>), ne <code>cin</code> bez <code>sync_with_stdio(false)</code>.''',
    ],
    'solution': r'''
<p>Sve stringove ubacimo u trie; $\operatorname{lcp}$ para je njihov najniži zajednički predak, pa je odgovor $v$ čvor trie-a. Za kandidat $v$ najveći broj stringova s parnim $\operatorname{lcp} \le v$ jest: svi stringovi koji završavaju na putu korijen$\to v$, cijela podstabla djece puta koja skreću manjim slovom, po jedan string iz svakog podstabla koje skreće većim slovom i po jedan iz svakog djeteta od $v$. Odgovor je leksikografski najmanji $v$ s $f(v) \ge k$; nalazimo ga pohlepnim spuštanjem: u čvoru $u$ stanemo ako $\text{acc} + \text{cntEnd}(u) + \deg(u) \ge k$, inače idemo u najmanje dijete $d$ čija dostižna gornja granica $\text{acc} + \text{cntEnd}(u) + \sum_{c<d}\text{sz}(c) + \#\{c>d\} + \text{sz}(d)$ iznosi barem $k$. Složenost $O(26 L)$. Ideja slijedi službeno rješenje GDCPC-a 2023 i analizu prihvaćenih predaja; implementacija je napisana iznova.</p>
''',
    'detailed': r'''
<h3>1. Trie i poredak</h3>
<p>Ubacimo svih $n$ stringova u trie; u svakom čvoru pamtimo $\text{sz}(u)$ (broj stringova u podstablu) i $\text{cntEnd}(u)$ (broj stringova koji točno tu završavaju). $\operatorname{lcp}(w_i, w_j)$ je čvor – najniži zajednički predak listova $w_i$ i $w_j$. Optimalni $v$ je maksimum takvih čvorova po parovima nekog skupa, dakle čvor trie-a.</p>
<p>Leksikografski poredak čvorova: $u \le v$ ako je $u$ predak od $v$ (prefiks, uključivo $u=v$), ili ako se u najnižem zajedničkom pretku $p$ put prema $u$ nastavlja manjim slovom nego put prema $v$. Inače je $u > v$ – to su čvorovi ispod $v$ i čvorovi u podstablima koja se od puta korijen$\to v$ odvajaju većim slovom.</p>
<h3>2. Funkcija $f(v)$</h3>
<p>Neka je $f(v)$ najveći broj stringova koje možemo odabrati tako da svaki par ima $\operatorname{lcp} \le v$. Razvrstajmo stringove prema putu $P$ od korijena do $v$:</p>
<ul>
<li>stringovi koji završavaju u čvoru $p \in P$: njihov $\operatorname{lcp}$ s bilo kojim stringom je predak od $p$, dakle prefiks od $v$ – svi smiju ući;</li>
<li>podstablo djeteta $c$ nekog $p \in P \setminus\{v\}$ koje skreće <em>manjim</em> slovom: dva stringa iz njega imaju $\operatorname{lcp}$ u tom podstablu ($< v$), a string iz njega s bilo kojim drugim ima $\operatorname{lcp}$ predak od $p$ – cijelo podstablo smije ući;</li>
<li>podstablo djeteta $c$ nekog $p \in P\setminus\{v\}$ koje skreće <em>većim</em> slovom: dva stringa iz njega imaju $\operatorname{lcp} \ge c > v$ – najviše jedan;</li>
<li>podstablo djeteta $c$ od $v$: dva stringa iz njega imaju $\operatorname{lcp} \ge c > v$ – najviše jedan.</li>
</ul>
<p>Uzmemo li sve dopuštene, svaki par zaista ima $\operatorname{lcp} \le v$ (provjerom po slučajevima: dva stringa iz različitih grupa sastaju se u čvoru puta $P$). Zato je
$$f(v) = \sum_{p\in P}\text{cntEnd}(p) + \sum_{p \in P\setminus\{v\}}\Big(\sum_{c<\text{smjer}}\text{sz}(c) + \#\{c > \text{smjer}\}\Big) + \deg(v).$$</p>
<p><strong>Odgovor je leksikografski najmanji čvor $v$ s $f(v)\ge k$.</strong> Naime, ako je $f(v)\ge k$, postoji skup od $k$ stringova s maksimalnim lcp-om $\le v$, pa je optimum $\le v$; obrnuto, za optimalni skup vrijedi $f(v^*) \ge k$ gdje je $v^*$ njegov maksimalni lcp.</p>
<h3>3. Pohlepno spuštanje</h3>
<p>Krenemo od korijena s $\text{acc}=0$ (zbroj doprinosa pravih predaka trenutnog čvora). U čvoru $u$:</p>
<ol>
<li>Ako je $\text{acc} + \text{cntEnd}(u) + \deg(u) \ge k$, ispiši $u$. Svi kandidati manji od $u$ isključeni su u ranijim koracima (vidjeti dolje), a $u$ je najmanji string sa svojim prefiksom.</li>
<li>Inače odgovor ima prefiks $u$ i još barem jedno slovo. Za djecu $d$ redom od <code>a</code> do <code>z</code> računamo granicu $B(d) = \text{acc} + \text{cntEnd}(u) + \sum_{c<d}\text{sz}(c) + \#\{c>d\} + \text{sz}(d)$. Ona je gornja granica za $f$ svakog $v$ u podstablu $d$ (iz podstabla $d$ ne može ući više od $\text{sz}(d)$ stringova). Odaberemo najmanje $d$ s $B(d)\ge k$, postavimo $\text{acc} \gets \text{acc} + \text{cntEnd}(u) + \sum_{c<d}\text{sz}(c) + \#\{c>d\}$ i spustimo se.</li>
</ol>
<p><em>Dostižnost granice.</em> U podstablu $d$ spuštajmo se uvijek u najveće dijete dok ne dođemo u list $\ell$. Svaki čvor $p$ na tom putu doprinosi $\text{cntEnd}(p)$ + veličine sve svoje ostale djece (sva su manja), a list doprinosi $\text{cntEnd}(\ell)$; zbroj je točno $\text{sz}(d)$. Dakle $\max_{v\in\text{podstablo}(d)} f(v) = B(d)$, pa preskakanje djece s $B(d)<k$ ne gubi rješenje, a ulazak u prvo dijete s $B(d)\ge k$ jamči da rješenje tamo postoji.</p>
<p><em>Postojanje izbora.</em> Za najveće dijete $d_{\max}$ vrijedi $B(d_{\max}) = \text{acc} + \text{sz}(u)$. Invarijanta $\text{acc}+\text{sz}(u)\ge k$ vrijedi u korijenu ($n\ge k$) i čuva se pri spuštanju (nova vrijednost je upravo $B(d)\ge k$).</p>
<h3>4. Složenost</h3>
<p>Izgradnja trie-a $O(L)$, $L=\sum|w_i|\le 10^6$. Spuštanje obiđe jedan put duljine $\le \max|w_i|$; po čvoru $O(26)$ za popis djece i $O(26)$ po postojećem djetetu za brojanje veće djece – ukupno $O(26L)$. Memorija: polje <code>ch[10^6+5][26]</code> ($\approx 104$ MB) plus dva niza – unutar 1 GiB.</p>
<h3>5. Zamke</h3>
<ul>
<li>Odgovor može biti prazan (korijen): to je slučaj $\deg(\text{korijen}) + \text{cntEnd}(\text{korijen}) \ge k$, tj. barem $k$ različitih prvih slova. Tada ispiši <code>EMPTY</code>.</li>
<li>Duplikati stringova završavaju u istom čvoru – zato brojimo $\text{cntEnd}$, ne samo označavamo kraj.</li>
<li>Reset trie-a između testova radi po čvoru pri stvaranju, a ne <code>memset</code> cijelog polja.</li>
<li>Brzo čitanje: ukupno do $10^6$ znakova i do $T$ testova, koristi <code>fread</code>.</li>
</ul>
<h3>6. Primjer</h3>
<p>Stringovi <code>gdcpc</code>, <code>gdcpcpcp</code>, <code>suasua</code>, <code>suas</code>, <code>sususua</code>, $k=3$. U korijenu: $\deg = 2$ (<code>g</code>, <code>s</code>), $\text{cntEnd}=0$, $2<3$. Dijete <code>g</code>: $B = 0 + 0 + 1 + 2 = 3 \ge 3$, ulazimo ($\text{acc}=1$: jedan string iz podstabla <code>s</code>). Spuštamo se <code>g d c p c</code>: u čvoru <code>gdcpc</code> je $\text{cntEnd}=1$, $\deg=1$, $1+1+1=3\ge 3$ – odgovor <code>gdcpc</code> (skup <code>gdcpc</code>, <code>gdcpcpcp</code> i jedan string na <code>s</code>).</p>
''',
    'verified': r'''uzorci 2/2; 300 slučajnih testova ($n\le 8$, kratki stringovi nad malom abecedom) protiv brute forcea koji nabraja sve $k$-podskupove; 3 velika testa (ukupna duljina $10^6$, uključujući jedan vrlo dug string i mnogo kratkih), najsporiji $0.01$ s.''',
},
# ---------------------------------------------------------------- D
{
    'letter': 'D', 'title': 'Computational Geometry', 'title_hr': 'Računalna geometrija', 'slug': 'D_computational_geometry',
    'tl': '4 s', 'ml': '1024 MiB',
    'statement': r'''
<p>Dan je konveksan poligon $P$ s $n$ vrhova. Odaberi dva vrha tako da ih spojnica dijeli $P$ na dva poligona $Q$ i $R$ pozitivne površine. Neka je $d(\cdot)$ dijametar (najveća udaljenost dviju točaka poligona). Minimiziraj $d(Q)^2 + d(R)^2$.</p>
<h3>Ulaz</h3>
<p>$T$ testova; $4 \le n \le 5000$, vrhovi $0 \le x_i, y_i \le 10^9$ u smjeru suprotnom od kazaljke na satu, površina pozitivna, vrhovi različiti, ali tri vrha mogu biti kolinearna; $\sum n \le 5000$.</p>
<h3>Izlaz</h3>
<p>Za svaki test najmanja vrijednost (cijeli broj).</p>
<h3>Primjer</h3>
<p>Vrhovi $(1,0), (2,0), (1,1), (0,0)$: $4$ (jedini dopušteni par je $(1,0)$–$(1,1)$). Vrhovi $(10,4), (9,7), (5,7), (4,5), (6,4), (9,3)$: $44$.</p>
''',
    'hints': [
        r'''
<p>Dijametar konveksnog poligona jednak je najvećoj udaljenosti dvaju <em>vrhova</em>. Dijelovi $Q$ i $R$ su poligoni na kružnim lukovima vrhova $i, i+1, \dots, j$ i $j, \dots, n-1, 0, \dots, i$.</p>
''',
        r'''
<p>Uz $\sum n \le 5000$ dopušteno je $O(n^2)$: izračunaj $f(i,j)$ = kvadrat dijametra luka $i..j$ za sve parove. Kako se $f(i,j)$ dobiva iz $f(i+1,j)$ i $f(i,j-1)$?</p>
''',
        r'''
<p>Isto napravi za komplementarne lukove (počni od najduljih), a zatim po svim dijagonalama uzmi $\min f + g$, preskačući dijagonale čiji je jedan dio degeneriran (svi vrhovi kolinearni).</p>
''',
    ],
    'coach': [
        ('Kako se računa dijametar poligona i zašto smijemo gledati samo vrhove?',
         r'''
<p>Udaljenost je konveksna funkcija svake od točaka, a maksimum konveksne funkcije na konveksnom skupu (poligonu) postiže se u ekstremnoj točki – vrhu. Primijenjeno na oba argumenta, $d(Q)=\max_{u,v\in V(Q)}|uv|$. Radimo s kvadratima udaljenosti pa je sve cjelobrojno.</p>
'''),
        ('Koje su „figure” koje moramo znati i koliko ih ima?',
         r'''
<p>Dijagonala $(i,j)$ dijeli poligon na luk vrhova $i,i+1,\dots,j$ i luk $j,\dots,n-1,0,\dots,i$. Dakle trebamo dijametar svakog kružnog luka vrhova – parova $(i,j)$ ima $O(n^2)$, što je uz $\sum n\le 5000$ oko $2.5\cdot10^7$ vrijednosti, prihvatljivo i za vrijeme i za memoriju ($200$ MB uz 64-bitne brojeve, limit je 1 GiB).</p>
'''),
        ('Kako dijametar luka izraziti pomoću manjih lukova?',
         r'''
<p>Svaki par vrhova $(a,b)$ u luku $i..j$ ili ne sadrži $i$ (pa je u luku $i+1..j$), ili ne sadrži $j$ (u luku $i..j-1$), ili je točno $(i,j)$. Zato $f(i,j)=\max\big(f(i+1,j),\,f(i,j-1),\,|P_iP_j|^2\big)$ – intervalno dinamičko programiranje po duljini luka, $O(1)$ po stanju. Za komplementarne lukove $g(i,j)$ (vrhovi $j..n-1,0..i$) vrijedi ista rekurzija: izbacimo $i$ ili $j$, pri čemu rubni slučajevi $i=0$ ili $j=n-1$ prelaze u običan luk; računamo od najduljih prema kraćima.</p>
'''),
        ('Koje dijagonale nisu dopuštene i kako to prepoznati?',
         r'''
<p>Dio mora imati pozitivnu površinu: treba barem tri vrha i ne smiju svi biti kolinearni. Kod konveksnog poligona luk $i..j$ je degeneriran točno kada su $P_i, P_{i+1}, P_j$ kolinearni (vektorski produkt $0$) – tada svi vrhovi između leže na istom pravcu. Isto provjeravamo za luk $j..i$ preko $P_j, P_{j+1}, P_i$. Zadatak jamči da barem jedna dopuštena dijagonala postoji.</p>
'''),
        ('Gdje vreba prelijevanje?',
         r'''
<p>Koordinate su do $10^9$, pa je $|P_iP_j|^2\le 2\cdot10^{18}$, a zbroj dvaju kvadrata do $4\cdot10^{18}$ – to prelazi <code>long long</code> ($\approx 9.2\cdot10^{18}$ još stane, ali oprez pri međuzbrajanjima) i sigurno je držati u <code>unsigned long long</code>. Vektorski produkt je do $2\cdot 10^{18}$, staje u <code>long long</code>.</p>
'''),
    ],
    'tips': [
        r'''<strong>Dijametar konveksnog skupa</strong> postiže se na vrhovima (maksimum konveksne funkcije). Ako je $n$ mali, ne treba rotirajući kaliper – kvadratna tablica po lukovima često je dovoljna i jednostavnija.''',
        r'''Rekurzija „luk $i..j$ = luk bez $i$, luk bez $j$, par $(i,j)$” pokriva sve parove i daje $O(1)$ prijelaz za svaku funkciju oblika $\max$ po parovima.''',
        r'''Kod cikličkih intervala pohrani komplementarni luk u „drugu polovicu” iste tablice (<code>tab[j][i]</code> za $i<j$) i posebno obradi rubove $i=0$ i $j=n-1$.''',
        r'''Kolinearnost triju uzastopnih vrhova provjeravaj cjelobrojnim vektorskim produktom – bez pomičnog zareza.''',
    ],
    'solution': r'''
<p>Dijametar konveksnog poligona je najveća udaljenost dvaju vrhova. Za luk vrhova $i..j$ definiramo $f(i,j)$ = kvadrat dijametra; vrijedi $f(i,j)=\max(f(i+1,j),f(i,j-1),|P_iP_j|^2)$ jer svaki par vrhova luka ili izostavlja $i$, ili izostavlja $j$, ili je baš $(i,j)$. Analogno računamo $g(i,j)$ za komplementarni luk $j..n-1,0..i$ (od najduljih prema kraćim, s rubnim slučajevima $i=0$, $j=n-1$). Odgovor je $\min f(i,j)+g(i,j)$ po dijagonalama kod kojih nijedan dio nije degeneriran ($P_i,P_{i+1},P_j$ odnosno $P_j,P_{j+1},P_i$ nisu kolinearni). Složenost $O(n^2)$ vremena i memorije, računamo u <code>unsigned long long</code>. Ideja slijedi službeno rješenje GDCPC-a 2023 i analizu prihvaćenih predaja; implementacija je napisana iznova.</p>
''',
    'detailed': r'''
<h3>1. Dijametar preko vrhova</h3>
<p>Za fiksnu točku $u$ funkcija $v\mapsto|uv|$ je konveksna, pa na konveksnom poligonu maksimum postiže u vrhu; primijenimo to na oba argumenta i dobijemo $d(Q)=\max_{u,v\in V(Q)}|uv|$. Radimo s kvadratima udaljenosti, koji su cijeli brojevi.</p>
<h3>2. Struktura dijelova</h3>
<p>Vrhovi su $P_0,\dots,P_{n-1}$ u smjeru suprotnom od kazaljke na satu. Dijagonala $(i,j)$, $i<j$, dijeli poligon na $Q$ s vrhovima $P_i,P_{i+1},\dots,P_j$ i $R$ s vrhovima $P_j,\dots,P_{n-1},P_0,\dots,P_i$. Oba su konveksna. Trebamo dakle kvadrate dijametara svih „lukova” vrhova.</p>
<h3>3. Intervalno dinamičko programiranje</h3>
<p>Neka je $f(i,j)$ kvadrat dijametra luka $i..j$ ($i\le j$). Za $j=i$ je $0$, za $j=i+1$ je $|P_iP_j|^2$, a općenito
$$f(i,j)=\max\big(f(i+1,j),\ f(i,j-1),\ |P_iP_j|^2\big).$$
<em>Dokaz.</em> Neka je $(a,b)$ par vrhova luka koji postiže maksimum. Ako $a\ne i$, par je u luku $i+1..j$; ako $b\ne j$, u luku $i..j-1$; inače je $(a,b)=(i,j)$. Obrnuto, sve tri veličine su maksimumi po podskupovima parova luka, pa su $\le f(i,j)$. Računamo po rastućoj duljini $j-i$.</p>
<p>Za komplementarni luk $g(i,j)$ (vrhovi $j,\dots,n-1,0,\dots,i$) isti argument daje $g(i,j)=\max(|P_iP_j|^2,\ \text{luk bez }i,\ \text{luk bez }j)$, gdje je „luk bez $i$” komplementarni luk $g(i-1,j)$ ako $i>0$, a za $i=0$ običan luk $f(j,n-1)$; „luk bez $j$” je $g(i,j+1)$ ako $j<n-1$, a za $j=n-1$ običan luk $f(0,i)$. Ovdje duljina luka raste kad se $j-i$ smanjuje, pa računamo od najvećeg $j-i$ prema manjem. U implementaciji $f(i,j)$ držimo u <code>tab[i][j]</code>, a $g(i,j)$ u <code>tab[j][i]</code>.</p>
<h3>4. Dopuštene dijagonale</h3>
<p>Dio mora imati pozitivnu površinu. Luk $i..j$ ima $j-i+1$ vrhova, komplementarni $n-(j-i)+1$; oba trebaju barem $3$, dakle $2\le j-i\le n-2$. Osim toga vrhovi mogu biti kolinearni: luk $i..j$ je degeneriran akko su $P_i,P_{i+1},P_j$ kolinearni – kod konveksnog poligona to znači da su $P_{i+1},\dots,P_{j-1}$ svi na segmentu $P_iP_j$ (sve točke poligona su s iste strane pravca $P_iP_{i+1}$, a $P_j$ je na njemu, pa je taj pravac potporni i svi vrhovi luka leže na njemu). Slično za komplementarni luk s $P_j,P_{j+1},P_i$. Kolinearnost provjeravamo vektorskim produktom $(P_{i+1}-P_i)\times(P_j-P_i)=0$.</p>
<h3>5. Algoritam i složenost</h3>
<ol>
<li>Učitaj vrhove; tablica $n\times n$ 64-bitnih brojeva.</li>
<li>Ispuni $f$ po rastućoj duljini, zatim $g$ po padajućoj razlici $j-i$.</li>
<li>Po svim $i<j$ s $2\le j-i\le n-2$ i nedegeneriranim dijelovima uzmi $\min f(i,j)+g(i,j)$.</li>
</ol>
<p>Vrijeme $O(n^2)$ po testu, memorija $O(n^2)$: uz $n=5000$ tablica ima $2.5\cdot10^7$ 64-bitnih polja ($200$ MB), unutar 1 GiB; $\sum n\le5000$ pa je ukupno vrijeme sitno.</p>
<h3>6. Prelijevanje</h3>
<p>$|P_iP_j|^2\le 2\cdot(10^9)^2=2\cdot10^{18}$; zbroj $f+g\le 4\cdot10^{18}$. To još stane u <code>long long</code>, ali u <code>unsigned long long</code> je sigurnije i ispisuje se s <code>%llu</code>. Vektorski produkt je po apsolutnoj vrijednosti $\le 2\cdot10^{18}$ – <code>long long</code> dovoljan.</p>
<h3>7. Primjer</h3>
<p>Vrhovi $(1,0),(2,0),(1,1),(0,0)$: jedini par s $2\le j-i\le 2$ su $(0,2)$ i $(1,3)$. Dijagonala $(1,3)$: luk $1..3$ je $(2,0),(1,1),(0,0)$ – nekolinearni, drugi dio $(0,0),(1,0),(2,0)$ – kolinearan, odbačeno. Dijagonala $(0,2)$: dijelovi $(1,0),(2,0),(1,1)$ i $(1,1),(0,0),(1,0)$, dijametri $2$ i $2$, odgovor $4$.</p>
''',
    'verified': r'''uzorci 2/2; 300 slučajnih malih konveksnih poligona ($n\le 9$, s kolinearnim trojkama) protiv brute forcea koji za svaku dijagonalu izravno računa dijametre po svim parovima; 3 velika testa ($n=5000$, koordinate do $10^9$), najsporiji $0.33$ s.''',
},
# ---------------------------------------------------------------- E
{
    'letter': 'E', 'title': 'Not Another Linear Algebra Problem', 'title_hr': 'Ne još jedan zadatak iz linearne algebre', 'slug': 'E_not_another_linear_algebra_problem',
    'tl': '5 s', 'ml': '1024 MiB',
    'statement': r'''
<p>Dan je prost broj $q$. Za $n \times n$ matricu $B$ nad $\mathbb{F}_q$ neka je $f(B)$ broj matrica $A$ s elementima iz $\{0, \dots, q-1\}$ takvih da $AB \equiv A \pmod q$. Izračunaj
$$\sum_{B \in M_n(\mathbb{F}_q)} [\det B \ne 0]\, 3^{f(B)}$$
modulo zadani prost broj $\mathit{mod}$.</p>
<h3>Ulaz</h3>
<p>Tri broja $n$, $q$, $\mathit{mod}$: $1 \le n \le 10^7$, $2 \le q \lt \mathit{mod}$, $10^8 \le \mathit{mod} \le 10^9 + 7$; $q$ i $\mathit{mod}$ su prosti.</p>
<h3>Izlaz</h3>
<p>Odgovor modulo $\mathit{mod}$.</p>
<h3>Primjer</h3>
<p>$n = 2$, $q = 2$, $\mathit{mod} = 10^9 + 7$: $43046970$ ($= 3^4 + 3^1 + 3^{16} + 3^4 + 3^4 + 3^1$ po šest regularnih matrica). $n = 100$, $q = 127$, $\mathit{mod} = 998244353$: $881381862$.</p>
''',
    'hints': [
        r'''
<p>$AB=A$ je isto što i $A(B-I)=0$: svaki redak od $A$ mora ležati u (lijevoj) jezgri od $B-I$. Ako je $k=\dim\ker(B-I)$ (dimenzija prostora fiksnih vektora od $B$), koliko je $f(B)$?</p>
''',
        r'''
<p>$f(B)=q^{nk}$ ovisi samo o $k$, pa je odgovor $\sum_{k=0}^{n}N_k\cdot3^{q^{nk}}$, gdje je $N_k$ broj regularnih matrica s točno $k$-dimenzionalnim prostorom fiksnih vektora. Prebroji matrice koje fiksiraju <em>zadani</em> $k$-dimenzionalni potprostor po točkama (blok-oblik $\begin{pmatrix}I&*\\0&C\end{pmatrix}$) i primijeni $q$-binomnu inverziju.</p>
''',
        r'''
<p>Rezultat inverzije: $N_k=\dfrac{|GL_n|}{|GL_k|}\sum_{i=0}^{n-k}\dfrac{q^{-ki}}{(q;q)_i}$ s $(q;q)_i=\prod_{j\le i}(1-q^j)$. Za $n=10^7$ treba sve te sume u $O(n)$: iz identiteta $(1-x)E_m(x)=E_{m+1}(qx)-x^{m+1}/(q;q)_{m+1}$ za $E_m(x)=\sum_{i\le m}x^i/(q;q)_i$ slijedi rekurzija $U_k=\big(U_{k-1}-q^{-k(n-k+1)}/(q;q)_{n-k+1}\big)/(1-q^{-k})$. Eksponent $q^{nk}$ računaj modulo $\mathit{mod}-1$.</p>
''',
    ],
    'coach': [
        ('Što uvjet $AB=A$ govori o retcima matrice $A$?',
         r'''
<p>$AB=A\iff A(B-I)=0$. Ako je $a$ redak od $A$, uvjet glasi $a(B-I)=0$, tj. $a$ pripada lijevoj jezgri matrice $B-I$, potprostoru dimenzije $n-\operatorname{rang}(B-I)=\dim\ker(B-I)=:k$ (lijeva i desna jezgra imaju istu dimenziju). Retci se biraju neovisno, pa je $f(B)=(q^k)^n=q^{nk}$. Prostor $\ker(B-I)$ je prostor fiksnih vektora $\{v: Bv=v\}$.</p>
'''),
        ('Kako se suma po svim regularnim $B$ svodi na $n+1$ pribrojnika?',
         r'''
<p>$f(B)$ ovisi samo o $k=\dim\operatorname{Fix}(B)$, pa je odgovor $\sum_{k=0}^{n}N_k\,3^{q^{nk}}$, gdje je $N_k=\#\{B\in GL_n(\mathbb F_q):\dim\operatorname{Fix}(B)=k\}$. Ostaje prebrojati $N_k$ – klasično pitanje o $GL_n(\mathbb F_q)$.</p>
'''),
        ('Kako prebrojati regularne matrice koje fiksiraju točno $k$-dimenzionalan prostor, kad je „točno” teško?',
         r'''
<p>Standardni obrat: prebroji „barem”, pa invertiraj. Za fiksni $k$-dimenzionalni potprostor $W$ broj regularnih $B$ koje fiksiraju $W$ po točkama je $q^{k(n-k)}|GL_{n-k}|$ (u bazi koja proširuje bazu od $W$: $B=\begin{pmatrix}I_k&*\\0&C\end{pmatrix}$, $*$ proizvoljan, $C\in GL_{n-k}$). Zbrojimo po svim $\binom nk_q$ potprostora $W$: svaki $B$ s $\dim\operatorname{Fix}=j$ brojan je $\binom jk_q$ puta, pa
$$S_k:=\sum_{j}N_j\binom jk_q=\binom nk_q\,q^{k(n-k)}|GL_{n-k}|=\frac{|GL_n|}{|GL_k|}$$
(zadnja jednakost provjerom eksponenata: $k(n-k)+\binom{n-k}2=\binom n2-\binom k2$).</p>
'''),
        ('Kako iz $S_k$ dobiti $N_k$ i zašto rezultat ima tako jednostavan oblik?',
         r'''
<p>Gaussova ($q$-binomna) inverzija: $N_k=\sum_{j\ge k}(-1)^{j-k}q^{\binom{j-k}2}\binom jk_qS_j$. Uvrstimo $S_j=|GL_n|/|GL_j|$, $|GL_j|=q^{\binom j2}(-1)^j(q;q)_j$ i $\binom jk_q=\frac{(q;q)_j}{(q;q)_k(q;q)_{j-k}}$; uz $i=j-k$ svi se $(q;q)_j$ pokrate, a eksponenti daju $\binom i2-\binom{i+k}2=-ik-\binom k2$, pa
$$N_k=\frac{|GL_n|}{|GL_k|}\;U_k,\qquad U_k=\sum_{i=0}^{n-k}\frac{q^{-ki}}{(q;q)_i}.$$</p>
'''),
        ('Kako sve $U_k$ izračunati u $O(n)$ za $n=10^7$?',
         r'''
<p>Izravno je $O(n^2)$. Neka je $E_m(x)=\sum_{i=0}^{m}x^i/(q;q)_i$. Iz $\frac1{(q;q)_i}-\frac1{(q;q)_{i-1}}=\frac{q^i}{(q;q)_i}$ slijedi $(1-x)E_m(x)=E_m(qx)-\frac{x^{m+1}}{(q;q)_m}=E_{m+1}(qx)-\frac{x^{m+1}}{(q;q)_{m+1}}$ (jer $\frac{q^{m+1}}{(q;q)_{m+1}}+\frac1{(q;q)_m}=\frac1{(q;q)_{m+1}}$). Uz $x=q^{-k}$, $m=n-k$: $U_k=E_{n-k}(q^{-k})$, $U_{k-1}=E_{n-k+1}(q^{-k+1})$, dakle
$$U_k=\frac{U_{k-1}-q^{-k(n-k+1)}/(q;q)_{n-k+1}}{1-q^{-k}},\qquad \frac1{1-q^{-k}}=\frac{q^k}{q^k-1}.$$
Uz predračunate $q^i$, $1/(q^i-1)$ (skupni inverz) i $1/(q;q)_i$ svaki korak je $O(1)$.</p>
'''),
        ('Kako izračunati $3^{q^{nk}}$ za $10^7$ vrijednosti $k$?',
         r'''
<p>$\mathit{mod}$ je prost i $\ne3$, pa po malom Fermatovu teoremu eksponent smijemo uzeti modulo $\mathit{mod}-1$: $e_k=q^{nk}\bmod(\mathit{mod}-1)$, $e_k=e_{k-1}\cdot(q^n\bmod(\mathit{mod}-1))$. Zatim $3^{e}$ u $O(1)$ preko dvije tablice („baby-step/giant-step” potencije): $3^{e}=3^{e\bmod 2^{15}}\cdot(3^{2^{15}})^{\lfloor e/2^{15}\rfloor}$, jer je $e\lt2^{30}$.</p>
'''),
    ],
    'tips': [
        r'''<strong>Brojanje u $GL_n(\mathbb F_q)$:</strong> „točno $k$-dimenzionalan fiksni potprostor” prebroji kroz „fiksira zadani potprostor” i $q$-binomnu (Gaussovu) inverziju; formule za $|GL_n|$, $\binom nk_q$ i $(q;q)_n$ drži pri ruci.''',
        r'''Kad linearan uvjet vrijedi za svaki redak matrice neovisno, broj rješenja je $(\text{broj rješenja po retku})^{n}$ – matrica se raspada na retke.''',
        r'''Za $O(n)$ evaluaciju familije odrezanih $q$-redova traži funkcijsku jednadžbu (ovdje $(1-x)E(x)=E(qx)$) i prati što se događa s odrezanim članovima.''',
        r'''Eksponente ogromnih potencija reduciraj modulo $\varphi(\mathit{mod})$, a milijune potencija iste baze računaj tablicama $3^{\text{lo}}\cdot(3^{2^{B}})^{\text{hi}}$; skupni inverz (prefiksni produkti) zamjenjuje $n$ brzih potenciranja.''',
    ],
    'solution': r'''
<p>$AB=A\iff A(B-I)=0$, pa je svaki redak od $A$ u jezgri od $B-I$: $f(B)=q^{nk}$, $k=\dim\ker(B-I)$. Odgovor je $\sum_{k=0}^{n}N_k\,3^{q^{nk}}$ s $N_k=\#\{B\in GL_n:\dim\operatorname{Fix}B=k\}$. Broj regularnih $B$ koje fiksiraju zadani $k$-dimenzionalni potprostor je $q^{k(n-k)}|GL_{n-k}|$, pa $\sum_jN_j\binom jk_q=\binom nk_qq^{k(n-k)}|GL_{n-k}|=|GL_n|/|GL_k|$; $q$-binomna inverzija daje $N_k=\frac{|GL_n|}{|GL_k|}U_k$, $U_k=\sum_{i=0}^{n-k}q^{-ki}/(q;q)_i$. Sve $U_k$ dobivamo u $O(n)$ rekurzijom $U_k=\big(U_{k-1}-q^{-k(n-k+1)}/(q;q)_{n-k+1}\big)\cdot\frac{q^k}{q^k-1}$ (iz $(1-x)E_m(x)=E_{m+1}(qx)-x^{m+1}/(q;q)_{m+1}$), a $|GL_n|/|GL_k|$ dijeljenjem s $q^{k-1}(q^k-1)$; inverze $q^i-1$ računamo skupno. Eksponent $q^{nk}$ vodimo modulo $\mathit{mod}-1$, a $3^e$ računamo u $O(1)$ dvjema tablicama. Ukupno $O(n)$ vremena i memorije, uz pretpostavku da su $q^i-1$ ($i\le n+1$) invertibilni modulo $\mathit{mod}$. Ideja je izvedena vlastitom analizom strukture problema (jezgra od $B-I$, brojanje u $GL_n(\mathbb F_q)$) uz uvid u pristup prihvaćenih predaja na QOJ-u; implementacija je napisana iznova i provjerena iscrpnim nabrajanjem za male $n,q$.</p>
''',
    'detailed': r'''
<h3>1. Svođenje $f(B)$ na dimenziju</h3>
<p>$AB=A$ ekvivalentno je $A(B-I)=0$. Zapišemo li $A$ po retcima $a_1,\dots,a_n$, uvjet se raspada na $n$ neovisnih uvjeta $a_r(B-I)=0$, tj. $a_r$ leži u lijevoj jezgri matrice $B-I$. Lijeva jezgra ima dimenziju $n-\operatorname{rang}(B-I)$, jednako kao i (desna) jezgra $\ker(B-I)=\{v:Bv=v\}$ – prostor fiksnih vektora. Označimo $k=\dim\ker(B-I)$; svaki redak ima $q^k$ mogućnosti, dakle
$$f(B)=q^{nk}.$$</p>
<h3>2. Preoblikovanje sume</h3>
<p>$$\sum_{B\in GL_n(\mathbb F_q)}3^{f(B)}=\sum_{k=0}^{n}N_k\cdot3^{q^{nk}},\qquad N_k=\#\{B\in GL_n:\dim\operatorname{Fix}(B)=k\}.$$
Primjer $n=2,q=2$: $GL_2(\mathbb F_2)$ ima $6$ elemenata – $I$ ($k=2$, $3^{16}$), tri involucije ($k=1$, $3^4$) i dva elementa reda $3$ ($k=0$, $3^1$): $3^{16}+3\cdot3^4+2\cdot3=43046970$.</p>
<h3>3. Brojanje $N_k$: „barem” pa inverzija</h3>
<p><em>Lema.</em> Za fiksni potprostor $W$ dimenzije $k$, broj $B\in GL_n$ s $Bw=w$ za sve $w\in W$ iznosi $q^{k(n-k)}|GL_{n-k}|$.<br>
<em>Dokaz.</em> U bazi $\mathbb F_q^n$ čijih prvih $k$ vektora čini bazu od $W$, $B$ fiksira $W$ po točkama akko ima blok-oblik $\begin{pmatrix}I_k&X\\0&C\end{pmatrix}$ s proizvoljnim $X\in\mathbb F_q^{k\times(n-k)}$ i $C\in\mathbb F_q^{(n-k)\times(n-k)}$; $\det B=\det C$, pa je $B$ regularna akko $C\in GL_{n-k}$. $\square$</p>
<p>Zbrojimo lemu po svim $\binom nk_q$ potprostora dimenzije $k$. Matrica $B$ s $\dim\operatorname{Fix}(B)=j$ fiksira po točkama upravo $\binom jk_q$ potprostora dimenzije $k$ (potprostore od $\operatorname{Fix}(B)$). Dakle
$$S_k:=\sum_{j=k}^{n}N_j\binom jk_q=\binom nk_q\,q^{k(n-k)}\,|GL_{n-k}|.$$
Uz $|GL_m|=q^{\binom m2}\prod_{i=1}^{m}(q^i-1)$ i $\binom nk_q=\dfrac{\prod_{i=n-k+1}^{n}(q^i-1)}{\prod_{i=1}^{k}(q^i-1)}$ desna strana je $q^{k(n-k)+\binom{n-k}2}\dfrac{\prod_{i=1}^{n}(q^i-1)}{\prod_{i=1}^{k}(q^i-1)}$, a $k(n-k)+\binom{n-k}2=\dfrac{(n-k)(n+k-1)}2=\binom n2-\binom k2$, pa je $S_k=|GL_n|/|GL_k|$.</p>
<p><em>Gaussova inverzija.</em> Ako je $S_k=\sum_{j}\binom jk_qN_j$, onda je $N_k=\sum_{j\ge k}(-1)^{j-k}q^{\binom{j-k}2}\binom jk_qS_j$ ($q$-analog binomne inverzije; slijedi iz $q$-binomnog teorema $\sum_i(-1)^iq^{\binom i2}\binom mi_q=[m=0]$). Uvrstimo $(q;q)_m=\prod_{i=1}^{m}(1-q^i)$, $|GL_j|=q^{\binom j2}(-1)^j(q;q)_j$, $\binom jk_q=\frac{(q;q)_j}{(q;q)_k(q;q)_{j-k}}$ i $i=j-k$:
$$N_k=|GL_n|\sum_{i=0}^{n-k}\frac{(-1)^{i}q^{\binom i2}}{(q;q)_k(q;q)_i}\cdot\frac{1}{q^{\binom{i+k}2}(-1)^{i+k}}=\frac{|GL_n|(-1)^k}{(q;q)_k}\sum_{i=0}^{n-k}\frac{q^{\binom i2-\binom{i+k}2}}{(q;q)_i}.$$
Budući da je $\binom i2-\binom{i+k}2=-ik-\binom k2$ i $\frac{(-1)^k}{(q;q)_k}q^{-\binom k2}=\frac1{|GL_k|}$, dobivamo
$$\boxed{N_k=\frac{|GL_n|}{|GL_k|}\,U_k,\qquad U_k=\sum_{i=0}^{n-k}\frac{q^{-ki}}{(q;q)_i}.}$$
Provjera za $n=2,q=2$: $|GL_2|=6$, $U_2=1$, $U_1=1+\frac{1/2}{-1}=\frac12$, $U_0=1+\frac1{-1}+\frac1{(-1)(-3)}=\frac13$; $N_2=1$, $N_1=6\cdot\frac12=3$, $N_0=6\cdot\frac13=2$. $\checkmark$</p>
<h3>4. Sve $U_k$ u $O(n)$</h3>
<p>Neka je $E_m(x)=\sum_{i=0}^{m}\frac{x^i}{(q;q)_i}$. Kako je $\frac1{(q;q)_i}-\frac1{(q;q)_{i-1}}=\frac{1-(1-q^i)}{(q;q)_i}=\frac{q^i}{(q;q)_i}$,
$$(1-x)E_m(x)=\sum_{i=0}^{m}\frac{(qx)^i}{(q;q)_i}-\frac{x^{m+1}}{(q;q)_m}=E_{m+1}(qx)-x^{m+1}\Big(\frac{q^{m+1}}{(q;q)_{m+1}}+\frac1{(q;q)_m}\Big)=E_{m+1}(qx)-\frac{x^{m+1}}{(q;q)_{m+1}}.$$
Uz $x=q^{-k}$ i $m=n-k$ imamo $U_k=E_{n-k}(q^{-k})$ i $U_{k-1}=E_{n-k+1}(q^{-(k-1)})=E_{m+1}(qx)$, pa
$$U_k=\frac{U_{k-1}-q^{-k(n-k+1)}/(q;q)_{n-k+1}}{1-q^{-k}}=\Big(U_{k-1}-\frac{q^{-k(n-k+1)}}{(q;q)_{n-k+1}}\Big)\cdot\frac{q^k}{q^k-1}.$$
$U_0=\sum_{i=0}^{n}1/(q;q)_i$ računamo izravno. Eksponent $k(n-k+1)$ raste za $n-2k+2$ pri $k\to k+1$, pa $q^{-k(n-k+1)}$ održavamo množenjem s $q^{-(n-2k+2)}$, koje se pak množi s $q^{2}$ svaki korak – bez potenciranja u petlji.</p>
<h3>5. Ostale komponente</h3>
<ul>
<li>$q^i$ za $i\le n+1$ i skupni inverz svih $q^i-1$ (prefiksni produkti + jedno potenciranje); $\frac1{(q;q)_i}=(-1)^i\prod_{j\le i}\frac1{q^j-1}$.</li>
<li>$\frac{|GL_n|}{|GL_k|}$: krenemo od $|GL_n|$ ($k=0$) i za svaki $k$ podijelimo s $q^{k-1}(q^k-1)$.</li>
<li>$3^{q^{nk}}$: $\mathit{mod}$ je prost $\ge10^8$, pa $3^{e}$ ovisi samo o $e\bmod(\mathit{mod}-1)$. Održavamo $e_k=q^{nk}\bmod(\mathit{mod}-1)$ množenjem s $q^n\bmod(\mathit{mod}-1)$ (128-bitno množenje jer $\mathit{mod}-1$ nije prost i ne smijemo ga miješati s aritmetikom modulo $\mathit{mod}$). $3^{e}$ za $e\lt2^{30}$ računamo u $O(1)$ tablicama $3^{0..2^{15}-1}$ i $(3^{2^{15}})^{0..2^{15}-1}$.</li>
</ul>
<h3>6. Složenost i memorija</h3>
<p>Sve petlje su $O(n)$ s konstantnim brojem modularnih množenja; $n=10^7$ traje ispod sekunde. Memorija: tri polja duljine $n+2$ (64-bitna) $\approx 240$ MB plus privremeno polje prefiksnih produkata – unutar $1024$ MiB.</p>
<h3>7. Zamke i pretpostavke</h3>
<ul>
<li>Sve modularne operacije u 64-bitnim tipovima s redukcijom nakon svakog množenja ($\mathit{mod}\lt2^{30}$, umnožak $\lt2^{60}$).</li>
<li>Rekurzija dijeli s $q^k-1$ i $(q;q)_i$, tj. pretpostavlja $q^i\not\equiv1\pmod{\mathit{mod}}$ za $1\le i\le n+1$ (red od $q$ modulo $\mathit{mod}$ veći od $n+1$). Tu pretpostavku koriste i prihvaćena rješenja; za $q\lt\mathit{mod}$ i slučajne parametre gotovo je uvijek ispunjena, ali strogo govoreći bi ulaz s malim redom od $q$ zahtijevao drugačiji postupak.</li>
<li>Eksponent $nk$ u $q^{nk}$ ne smije se računati u 64 bita izravno ($10^{14}$ je u redu, ali $q^{nk}$ nije) – zato redukcija modulo $\mathit{mod}-1$.</li>
<li>Slučaj $n=1$: $GL_1=\mathbb F_q^*$, $N_1=1$ ($B=1$), $N_0=q-2$; formula to daje.</li>
</ul>
''',
    'verified': r'''uzorci 2/2; 300 slučajnih testova ($n\le 3$, $q\le 7$, razni moduli) protiv brute forcea koji nabraja sve matrice $B$ nad $\mathbb F_q$, provjerava $\det B\ne0$ i računa $f(B)$ nabrajanjem matrica $A$ (za najmanje ulaze) ili preko $\dim\ker(B-I)$; 3 velika testa ($n=10^7$, razni $q$ i moduli), najsporiji $0.79$ s.''',
},
# ---------------------------------------------------------------- F
{
    'letter': 'F', 'title': 'X Equals Y', 'title_hr': 'X jednako Y', 'slug': 'F_x_equals_y',
    'tl': '3 s', 'ml': '1024 MiB',
    'statement': r'''
<p>Za $X \ge 1$ i bazu $b \ge 2$ neka je $f(X, b)$ niz znamenaka zapisa $X$ u bazi $b$, od najmanje značajne: $f(6, 2) = \{0, 1, 1\}$, $f(233, 17) = \{12, 13\}$.</p>
<p>Za dane $x, y, A, B$ nađi $2 \le a \le A$ i $2 \le b \le B$ takve da je $f(x, a) = f(y, b)$.</p>
<h3>Ulaz</h3>
<p>$1 \le T \le 1000$ testova; $1 \le x, y \le 10^9$, $2 \le A, B \le 10^9$; najviše $50$ testova ima $\max(x, y) \gt 10^6$.</p>
<h3>Izlaz</h3>
<p><code>YES</code> i u sljedećem retku <code>a b</code> (bilo koje valjano rješenje), ili <code>NO</code>.</p>
<h3>Primjer</h3>
<p>$(1, 1, 1000, 1000) \to$ <code>YES</code>, <code>2 2</code>; $(1, 2, 1000, 1000) \to$ <code>NO</code>; $(3, 11, 1000, 1000) \to$ <code>YES</code>, <code>2 10</code>; $(157, 291, 5, 6) \to$ <code>YES</code>, <code>4 5</code>; $(157, 291, 3, 6) \to$ <code>NO</code>; $(10126, 114514, 789, 12345) \to$ <code>YES</code>, <code>779 9478</code>.</p>
''',
    'hints': [
        r'''
<p>Podijeli prema <em>duljini</em> zajedničkog zapisa. Ako zapis ima $L\ge 3$ znamenaka, koliko velika može biti baza? A ako ima točno jednu znamenku?</p>
''',
        r'''
<p>Za $L\ge3$ je $a^2\le x$ i $b^2\le y$, pa baza ima najviše $\sqrt{10^9}\approx 31623$ kandidata – sve zapise možeš izračunati i usporediti (hash + provjera).</p>
''',
        r'''
<p>Za $L=2$ zapis je $(t,d)$: $x=ta+d$, $y=tb+d$, pa $y-x=t(b-a)$. Enumeriraj vodeću znamenku $t<\sqrt{x}$; tada je $b-a$ određen, a $a$ mora ležati u presjeku nekoliko intervala.</p>
''',
    ],
    'coach': [
        ('Što je „isti zapis” i koje su prirodne podjele problema?',
         r'''
<p>Zapisi su jednaki ako imaju istu duljinu $L$ i iste znamenke. Duljina zapisa $x$ u bazi $a$ je $L$ akko $a^{L-1}\le x<a^L$. Za veliki $L$ baza je mala: $a\le x^{1/(L-1)}$. Zato su prirodne kategorije $L=1$, $L=2$ i $L\ge3$ – u posljednjoj je $a\le\sqrt{x}\le 31623$, što se može nabrojati.</p>
'''),
        ('Kako riješiti $L=1$?',
         r'''
<p>Jednoznamenkasti zapis je $\{x\}$ odnosno $\{y\}$, pa treba $x=y$ (uz $a>x$, $b>y$). Ako je $x=y$, i sami zapisi u bilo kojoj istoj bazi su jednaki – ispišemo <code>2 2</code>. Ako je $x\ne y$, slučaj $L=1$ otpada.</p>
'''),
        ('Kako riješiti $L\ge3$ bez pretraživanja parova $(a,b)$?',
         r'''
<p>Zbog $a\le\sqrt x$ i $b\le\sqrt y$ za svaku od najviše $31623$ baza izračunamo niz znamenaka (duljine $\le 30$) i spremimo hash zapisa od $x$ u tablicu (hash $\to$ baza). Zatim za svaki $b$ potražimo hash zapisa od $y$; pri pogotku eksplicitno usporedimo nizove da isključimo koliziju. Trošak je $O(\sqrt{x}\log x)$ po testu, a takvih „velikih” testova ima najviše $50$.</p>
'''),
        ('Zašto je $L=2$ poseban i kako ga svesti na aritmetiku?',
         r'''
<p>Za $L=2$ baze mogu biti do $10^9$, pa ih ne možemo nabrojati. No zapis je $(t,d)$ s $x=ta+d$, $y=tb+d$, $1\le t<a,b$, $0\le d$. Oduzimanjem $y-x=t(b-a)$: za fiksni $t$ razlika $\delta=b-a=(y-x)/t$ mora biti cijela. Kako je $t<a$ i $ta\le x$, vrijedi $t^2<x$ (i $t^2<y$), pa $t$ enumeriramo do $\sqrt{\min(x,y)}$. Uvjeti $ta\le x<(t+1)a$, $a>t$, $2\le a\le A$ te isti uvjeti za $b=a+\delta$ daju intervale za $a$; uzmemo bilo koji $a$ iz njihova presjeka. Znamenka $d=x-ta=y-tb$ tada se automatski podudara.</p>
'''),
        ('Koje granice i zamke treba provjeriti?',
         r'''
<p>$x<(t+1)a \iff a>\lfloor x/(t+1)\rfloor$; $ta\le x\iff a\le\lfloor x/t\rfloor$. Sve stane u 64 bita. Ne zaboravi $a\le A$, $b\le B$ i $a,b\ge2$. Treba paziti da se slučaj $x=y$ obradi prije (inače $\delta=0$ nije problem, ali $L=1$ je najjednostavniji ispis).</p>
'''),
    ],
    'tips': [
        r'''<strong>Podjela po duljini zapisa</strong> je standardni trik za „baza je nepoznata”: za $L\ge3$ baza je $\le\sqrt{x}$ (nabrajanje), za $L=2$ ostaje čista aritmetika s vodećom znamenkom, za $L=1$ trivijalno.''',
        r'''Kad uspoređuješ mnogo kratkih nizova, hashiraj ih u tablicu, ali pri pogotku eksplicitno provjeri jednakost – to čini rješenje otpornim na kolizije bez gubitka brzine.''',
        r'''Pri uvjetima oblika $ta\le x<(t+1)a$ prevedi ih u zatvorene cjelobrojne intervale za $a$ (<code>x/(t+1)+1 .. x/t</code>) i traži presjek – manje grešaka nego s petljama.''',
    ],
    'solution': r'''
<p>Dijelimo po duljini zajedničkog zapisa. $L=1$: moguće samo za $x=y$ (ispišemo <code>2 2</code>). $L=2$: $x=ta+d$, $y=tb+d$ pa $y-x=t(b-a)$; enumeriramo vodeću znamenku $t$ s $t^2<\min(x,y)$, dobijemo $\delta=(y-x)/t$ (mora biti cijeli), a $a$ tražimo u presjeku intervala iz $ta\le x<(t+1)a$, $a>t$, $2\le a\le A$ i istih uvjeta za $b=a+\delta$. $L\ge3$: tada $a\le\sqrt x$, $b\le\sqrt y$, pa za svaku bazu izračunamo zapis, hashiramo zapise od $x$ u tablicu i tražimo jednak zapis od $y$ (uz eksplicitnu provjeru pri pogotku). Složenost $O(\sqrt{x}\log x)$ po testu. Ideja slijedi službeno rješenje GDCPC-a 2023 i analizu prihvaćenih predaja; implementacija je napisana iznova.</p>
''',
    'detailed': r'''
<h3>1. Duljina zapisa ograničava bazu</h3>
<p>Zapis broja $x$ u bazi $a$ ima $L$ znamenaka akko $a^{L-1}\le x<a^L$. Jednaki zapisi imaju jednaku duljinu $L$, pa razlikujemo tri slučaja: $L=1$, $L=2$ i $L\ge3$. U posljednjem je $a^2\le a^{L-1}\le x$, tj. $a\le\sqrt x\le 31623$, i analogno $b\le\sqrt y$.</p>
<h3>2. Slučaj $L=1$</h3>
<p>Zapis je $\{x\}$ odnosno $\{y\}$ (uz $a>x$, $b>y$), pa je nužno $x=y$. Obrnuto, ako je $x=y$, bilo koja zajednička baza radi; ispisujemo <code>2 2</code>. Za $x\ne y$ slučaj otpada.</p>
<h3>3. Slučaj $L\ge3$: nabrajanje baza</h3>
<p>Za svaki $a\in[2,\min(A,\lfloor\sqrt x\rfloor)]$ izračunamo znamenke $x$ u bazi $a$ (najviše $\log_2 10^9\approx 30$ dijeljenja) i spremimo par (hash zapisa, $a$) u hash-tablicu. Zatim za svaki $b\in[2,\min(B,\lfloor\sqrt y\rfloor)]$ izračunamo zapis $y$ u bazi $b$, potražimo hash i pri pogotku usporedimo nizove znak po znak – kolizija tako ne može dati krivi odgovor. Napomena: nabrajamo i baze koje daju duljinu $2$ (ako je $a\le\sqrt{x}$); to ne šteti, jer su takvi parovi i dalje valjani odgovori.</p>
<p>Trošak je $O((\sqrt x+\sqrt y)\log x)$ po testu, tj. oko $2\cdot 10^6$ operacija za $x,y\approx10^9$; takvih je testova najviše $50$, a preostali imaju $\sqrt{x}\le 1000$.</p>
<h3>4. Slučaj $L=2$: aritmetika vodeće znamenke</h3>
<p>Dvoznamenkasti zapis je $(d,t)$ (od najmanje značajne): $x=ta+d$, $y=tb+d$ s $1\le t<\min(a,b)$ i $0\le d<\min(a,b)$. Oduzimanjem: $y-x=t(b-a)$. Kako je $t<a$ i $ta\le x$, slijedi $t^2<ta\le x$; jednako $t^2<y$. Zato enumeriramo $t=1,2,\dots$ dok je $t^2<\min(x,y)$ – najviše $\sqrt{10^9}$ koraka.</p>
<p>Za fiksni $t$: ako $t\nmid(y-x)$, preskoči; inače $\delta=(y-x)/t$ i $b=a+\delta$. Uvjeti na $a$:</p>
<ul>
<li>$ta\le x<(t+1)a \iff \lfloor x/(t+1)\rfloor+1\le a\le\lfloor x/t\rfloor$ (drugi dio jamči $d=x-ta<a$, a prvi $d\ge0$);</li>
<li>$a>t$ (vodeća znamenka $t$ mora biti valjana znamenka) i $2\le a\le A$;</li>
<li>isti uvjeti za $b=a+\delta$: $\lfloor y/(t+1)\rfloor+1\le a+\delta\le\lfloor y/t\rfloor$, $a+\delta>t$, $2\le a+\delta\le B$.</li>
</ul>
<p>Presjek tih intervala je interval $[\text{lo},\text{hi}]$; ako je neprazan, $a=\text{lo}$, $b=\text{lo}+\delta$ je rješenje. Znamenka $d$ podudara se automatski: $y-tb=y-ta-t\delta=y-ta-(y-x)=x-ta$. Obrnuto, svako rješenje s $L=2$ ima neku vodeću znamenku $t$ i zadovoljava sve nabrojene uvjete, pa ga enumeracija nalazi.</p>
<h3>5. Algoritam</h3>
<ol>
<li>Ako $x=y$: <code>YES</code>, <code>2 2</code>.</li>
<li>Petlja po $t$ za $L=2$; pri prvom nepraznom presjeku ispiši rješenje.</li>
<li>Inače nabrajanje baza za $L\ge3$ s hash-tablicom; ispiši rješenje ili <code>NO</code>.</li>
</ol>
<h3>6. Složenost i zamke</h3>
<p>Po testu $O(\sqrt{\min(x,y)})$ za $L=2$ i $O(\sqrt{x}\log x)$ za $L\ge3$; ukupno uz $T\le1000$ i najviše $50$ „velikih” testova to je nekoliko desetaka milijuna operacija. Sve vrijednosti staju u <code>long long</code>. Zamke: $t$ mora biti strogo manji od baze (uvjet $a>t$), $A$ ili $B$ mogu biti manji od $\sqrt{x}$ – ograniči petlje i s njima; hash-tablicu rezerviraj unaprijed.</p>
<h3>7. Primjer</h3>
<p>$(157,291,5,6)$: $L=2$, $t=1$: $\delta=134$, $a\in[79,157]$ – ali $a\le5$, prazno; $t=2$: $134/2=67$, $a\in[53,78]$, prazno; i tako dalje – nijedan $t\le 12$ ne prolazi. $L\ge3$: $a\in\{2,\dots,5\}$; $157_4=(1,3,1,2)$ od najmanje značajne, $291_5=(1,3,1,2)$ – pogodak, <code>4 5</code>. Uz $A=3$ baza $4$ nije dopuštena i odgovor je <code>NO</code>.</p>
''',
    'verified': r'''uzorci 6/6; 300 slučajnih testova ($x,y\le 60$, $A,B\le 60$) protiv brute forcea koji isprobava sve parove baza, uz <code>check.py</code> koji provjerava valjanost ispisanog para i podudarnost odgovora <code>YES</code>/<code>NO</code>; 3 velika testa ($T=1000$, $50$ testova s $x,y\approx10^9$), najsporiji $0.17$ s.''',
},
# ---------------------------------------------------------------- G
{
    'letter': 'G', 'title': 'Classic Problem', 'title_hr': 'Klasičan zadatak', 'slug': 'G_classic_problem',
    'tl': '8 s', 'ml': '1024 MiB',
    'statement': r'''
<p>Potpun graf s $n$ vrhova i $m$ trojki $(u_i, v_i, w_i)$, $u_i \lt v_i$, s različitim parovima. Težina brida $\{x, y\}$ je $w_i$ ako postoji trojka s $(u_i, v_i) = (x, y)$, a inače $|x - y|$. Izračunaj težinu minimalnog razapinjućeg stabla.</p>
<h3>Ulaz</h3>
<p>$1 \le T \le 10^5$ testova; $1 \le n \le 10^9$, $0 \le m \le 10^5$, $0 \le w_i \le 10^9$; $\sum m \le 5 \cdot 10^5$.</p>
<h3>Izlaz</h3>
<p>Za svaki test težina MST-a.</p>
<h3>Primjer</h3>
<p>$n = 5$, trojke $(1,2,5), (2,3,4), (1,5,0)$: $4$. $n = 5$, $m = 0$: $4$. $n = 5$, trojke $(1, j, 10^9)$ za $j = 2..5$: $1000000003$.</p>
''',
    'hints': [
        r'''
<p>Bez trojki MST je put $1-2-\dots-n$ težine $n-1$. Vrhovi koji se ne pojavljuju ni u jednoj trojki („obični”) između dva „posebna” vrha tvore segment uzastopnih brojeva; što se može reći o bridovima težine $1$ unutar segmenta?</p>
''',
        r'''
<p>Bridovi težine $1$ unutar segmenta običnih vrhova uvijek su u nekom MST-u, pa segment možemo sažeti u jedan čvor. Ostaje potpun graf s $O(m)$ čvorova u kojem je težina brida ili trojka ili udaljenost intervala.</p>
''',
        r'''
<p>Na potpunom grafu s implicitnim težinama koristi Borůvku: za svaki čvor najjeftiniji brid u drugu komponentu je ili neka njegova trojka ili udaljenosni brid do najbližeg čvora druge komponente (lijevo/desno) s kojim nije povezan trojkom.</p>
''',
    ],
    'coach': [
        ('Kako uopće raditi s grafom od $10^9$ vrhova?',
         r'''
<p>Samo $\le 2m$ vrhova („posebni”) sudjeluje u trojkama; svi ostali imaju isključivo bridove težine $|x-y|$. Ako se ograničimo na strukturu koja ovisi samo o posebnim vrhovima i o segmentima običnih vrhova između njih, graf ima $O(m)$ relevantnih dijelova.</p>
'''),
        ('Zašto se bridovi težine $1$ unutar segmenta običnih vrhova smiju odmah uzeti?',
         r'''
<p>Zamislimo Kruskala koji među bridovima težine $1$ prvo obrađuje bridove $(x,x+1)$ unutar segmenata. Prije njih dodani su samo bridovi težine $0$, a to su trojke između posebnih vrhova – ne dodiruju obične vrhove. Bridovi unutar segmenata čine putove po običnim vrhovima, pa nikad ne zatvaraju ciklus i Kruskal ih sve uzima. Dakle postoji MST koji ih sadrži; sažmemo svaki segment $[l,r]$ u jedan čvor i pribrojimo $r-l$.</p>
'''),
        ('Kako izgleda sažeti graf i koje su težine njegovih bridova?',
         r'''
<p>Čvorovi su posebni vrhovi (intervali duljine $1$) i segmenti (intervali običnih vrhova), poredani po položaju; ima ih $K\le 4m+1$. Između čvorova $i$ i $y$ najjeftiniji je izvorni brid: ako su oba posebna i povezana trojkom, težina je $w$; inače je to udaljenost između intervala, $L_i-R_y$ ili $L_y-R_i$ (najbliži krajevi). Segmenti nemaju trojki, pa su njihovi bridovi uvijek udaljenosni.</p>
'''),
        ('Koji MST algoritam radi na potpunom grafu s $O(m)$ čvorova bez nabrajanja $O(m^2)$ bridova?',
         r'''
<p>Borůvka: u svakoj od $O(\log K)$ faza za svaku komponentu nađemo najjeftiniji izlazni brid i sve ih dodamo. Za čvor $i$ kandidati su: (1) njegove trojke prema drugoj komponenti – $O(\deg i)$; (2) udaljenosni brid do najbližeg čvora druge komponente lijevo i desno <em>koji nije povezan trojkom s $i$</em> (ti su parovi već pokriveni trojkom). Udaljenost raste s razmakom, pa je najbliži takav čvor optimalan. Predračunamo za svaki položaj najbliži čvor lijevo i najbliži lijevo iz komponente različite od njegove (isto desno) – to daje najbliži čvor iz komponente $\ne C$ u $O(1)$, a preskakanje trojkom povezanih čvorova košta ukupno $O(\deg i)$.</p>
'''),
        ('Kako izbjeći probleme s jednakim težinama u Borůvki i kolika je složenost?',
         r'''
<p>Bridove uspoređujemo leksikografski po $(w,u,v)$ – strogi uređaj jamči da skup odabranih najjeftinijih bridova ne sadrži ciklus, a pri dodavanju ionako provjeravamo DSU. Faza košta $O(K+m)$, faza je $O(\log K)$, dakle $O((m)\log m)$ po testu uz $\sum m\le5\cdot10^5$ i $T\le10^5$ (brzo čitanje ulaza je nužno).</p>
'''),
    ],
    'tips': [
        r'''<strong>Ogroman potpun graf s „pravilnim” težinama:</strong> nađi bridove koji su sigurno u nekom MST-u (argumentom o Kruskalovu poretku), sažmi ih i radi na $O(m)$ čvorova.''',
        r'''Borůvka je prirodan izbor kad se najjeftiniji izlazni brid čvora može naći implicitno (najbliži po položaju, po bitovima, po geometriji…) bez nabrajanja svih bridova.''',
        r'''Za „najbliži element iz druge komponente” pamti dva kandidata: najbliži uopće i najbliži iz komponente različite od njegove – jedan od njih je uvijek dobar.''',
        r'''Pri Borůvki uvijek razbij jednakosti težina strogim uređajem (npr. $(w,u,v)$), inače se mogu odabrati bridovi koji zatvaraju ciklus.''',
    ],
    'solution': r'''
<p>Krajevi trojki su posebni vrhovi ($\le2m$); obični vrhovi između njih tvore segmente uzastopnih brojeva. Bridovi težine $1$ unutar segmenta sigurno su u nekom MST-u (Kruskal koji ih obradi prve među težinama $1$ nikad ne zatvara ciklus), pa svaki segment sažmemo u čvor i pribrojimo njegovu duljinu minus $1$. Na sažetom potpunom grafu s $K\le4m+1$ čvorova (težina = trojka ili udaljenost intervala) pokrenemo Borůvku: najjeftiniji brid čvora u drugu komponentu je ili njegova trojka, ili udaljenosni brid do najbližeg čvora druge komponente lijevo/desno s kojim nije povezan trojkom; te kandidate nalazimo u $O(1)$ preko dva najbliža susjeda po komponenti uz preskakanje trojkom povezanih čvorova. Težine uspoređujemo po $(w,u,v)$. Složenost $O(m\log m)$ po testu. Ideja slijedi službeno rješenje GDCPC-a 2023 i analizu prihvaćenih predaja; implementacija je napisana iznova.</p>
''',
    'detailed': r'''
<h3>1. Posebni i obični vrhovi</h3>
<p>Neka je $S$ skup vrhova koji se pojavljuju u trojkama, $|S|\le2m$. Vrh izvan $S$ zovemo običnim: svi njegovi bridovi imaju težinu $|x-y|$. Sortirani $S$ dijeli $[1,n]$ na maksimalne segmente uzastopnih običnih vrhova.</p>
<h3>2. Bridovi unutar segmenta su u MST-u</h3>
<p>Promotrimo Kruskala s ovim poretkom: prvo svi bridovi težine $0$ (samo trojke), zatim među bridovima težine $1$ najprije bridovi $(x,x+1)$ s oba kraja u istom segmentu, pa ostali. Kad obrađujemo brid $(x,x+1)$ unutar segmenta, jedini dosad dodani bridovi koji dodiruju obične vrhove su drugi takvi bridovi, a oni čine putove; brid $(x,x+1)$ spaja dva dotad nepovezana dijela puta, pa ne zatvara ciklus i biva dodan. Kruskal daje MST, dakle postoji MST koji sadrži sve bridove unutar segmenata. Sažimanjem svakog segmenta $[l,r]$ u jedan čvor (i pribrajanjem $r-l$) dobivamo manji graf čiji MST, zajedno s tim bridovima, čini MST izvornog grafa (standardno svojstvo sažimanja bridova koji su u nekom MST-u).</p>
<h3>3. Sažeti graf</h3>
<p>Čvorovi $0..K-1$ su, po položaju, posebni vrhovi (intervali $[s,s]$) i segmenti $[l,r]$; $K\le 2m+(2m+1)$. Težina između čvorova $i\ne y$ je najjeftiniji izvorni brid među njihovim vrhovima: ako su oba posebna i postoji trojka $(i,y,w)$, to je $w$ (jedini izvorni brid); inače je to udaljenost intervala $\text{dist}(i,y)=L_{\max}-R_{\min}$ – najbliži krajevi.</p>
<h3>4. Borůvka s implicitnim bridovima</h3>
<p>U svakoj fazi za svaku komponentu $C$ tražimo najjeftiniji brid prema drugoj komponenti. Za čvor $i\in C$:</p>
<ul>
<li>ako je $i$ poseban, nudimo sve njegove trojke $(i,y,w)$ s $\text{comp}(y)\ne C$;</li>
<li>nudimo udaljenosni brid do najbližeg čvora $y$ lijevo od $i$ s $\text{comp}(y)\ne C$ koji nije trojkom povezan s $i$, i analogno desno. Udaljenost je monotona u razmaku položaja, pa je najbliži takav čvor najbolji među udaljenosnim bridovima; parovi povezani trojkom nemaju udaljenosni brid, ali su pokriveni prvom točkom.</li>
</ul>
<p>Najbližeg lijevo iz komponente $\ne C$ nalazimo u $O(1)$: za svaki položaj $t$ predračunamo $L_1[t]$ (najbliži čvor lijevo) i $L_2[t]$ (najbliži lijevo čija je komponenta različita od $\text{comp}(L_1[t])$); odgovor je $L_1[t]$ ako mu komponenta nije $C$, inače $L_2[t]$. Označimo li trojkom povezane čvorove od $i$ oznakom $i$, preskačemo ih skokovima $y\gets\text{nearLeft}(y,C)$ – svaki skok prelazi preko čvora povezanog trojkom s $i$, pa je ukupni trošak $O(\deg i)$.</p>
<p>Za svaku komponentu pamtimo najbolji ponuđeni brid; bridove uspoređujemo strogo po $(w,u,v)$, što je ekvivalentno jedinstvenom MST-u u grafu s perturbiranim težinama i jamči da odabrani bridovi ne zatvaraju ciklus. Zatim ih dodajemo uz DSU provjeru i zbrajamo težine. Svaka faza barem prepolovi broj komponenata.</p>
<h3>5. Složenost i implementacija</h3>
<p>Po fazi $O(K+m)$, faza je $O(\log K)$, dakle $O((m)\log m)$ po testu; $\sum m\le5\cdot10^5$. Uz $T\le10^5$ testova važno je brzo čitanje (<code>fread</code>) i izbjegavanje alokacija ovisnih o $n$ (koji je do $10^9$!). Težine zbrajamo u <code>long long</code>: MST može imati do $10^5$ bridova težine $10^9$ plus segmenti.</p>
<h3>6. Rubni slučajevi</h3>
<ul>
<li>$m=0$: jedan segment $[1,n]$, odgovor $n-1$ ($0$ za $n=1$).</li>
<li>Segment ispred prvog posebnog vrha ($1..s_1-1$) i iza posljednjeg ($s_k+1..n$) – ne zaboraviti ih.</li>
<li>Trojka može biti skuplja od udaljenosti ($w=10^9$ za susjedne vrhove): tada udaljenosni brid među njima ne postoji, ali se veza postiže obilaznim putem preko drugih vrhova – Borůvka to prirodno rješava (treći primjer, $10^9+3$).</li>
</ul>
<h3>7. Primjer</h3>
<p>$n=5$, trojke $(1,2,5),(2,3,4),(1,5,0)$: posebni $\{1,2,3,5\}$, segment $[4,4]$. Sažeti čvorovi: $1,2,3,[4],5$. Borůvka: $1$ bira $(1,5,0)$; $2$ bira udaljenosni brid do $[4]$ težine $2$ (brid do $1$ i $3$ su trojke $5$ i $4$); $3$ i $[4]$ biraju $(3,[4],1)$; $5$ bira $(1,5,0)$ ili $([4],5,1)$. Nakon spajanja ukupno $0+1+1+2=4$.</p>
''',
    'verified': r'''uzorci 3/3; 300 slučajnih testova ($n\le 9$, $m\le 8$) protiv brute forcea koji gradi cijeli graf i pokreće Kruskala; 3 velika testa ($T$ do $10^5$ malih testova odnosno $m=10^5$, $n=10^9$), najsporiji $0.11$ s.''',
},
# ---------------------------------------------------------------- H
{
    'letter': 'H', 'title': 'Swapping Operation', 'title_hr': 'Operacija zamjene', 'slug': 'H_swapping_operation',
    'tl': '1 s', 'ml': '1024 MiB',
    'statement': r'''
<p>Za niz nenegativnih cijelih brojeva $A = a_1, \dots, a_n$ definiramo
$$F(A) = \max_{1 \le k \lt n} \bigl((a_1 \mathbin{\&} \dots \mathbin{\&} a_k) + (a_{k+1} \mathbin{\&} \dots \mathbin{\&} a_n)\bigr),$$
gdje je $\&$ bitovni I. Smiješ najviše jednom zamijeniti dva elementa $a_i$ i $a_j$ ($i \lt j$). Odredi najveći mogući $F(A)$.</p>
<h3>Ulaz</h3>
<p>$T$ testova; $2 \le n \le 10^5$, $0 \le a_i \le 10^9$; $\sum n \le 10^5$.</p>
<h3>Izlaz</h3>
<p>Za svaki test najveći $F(A)$.</p>
<h3>Primjer</h3>
<p>$(6, 5, 4, 3, 5, 6) \to 7$ (zamijeni $a_4, a_6$, $k = 5$). $(1, 2, 1, 1, 2, 2) \to 3$. $(1, 1, 2, 2, 2) \to 3$ (bez zamjene).</p>
''',
    'hints': [
        r'''
<p>Prefiksni AND $p_k=a_1\,\&\dots\&\,a_k$ mijenja se u najviše $\approx 31$ „ključnoj” poziciji (svaka promjena briše barem jedan bit). Isto vrijedi za sufiksni AND.</p>
''',
        r'''
<p>Ako $a_i$ nije ključan za prefiks, izbacivanje $a_i$ iz bilo kojeg prefiksa $1..k$ ($k\ge i$) ne mijenja AND. Što to znači za zamjenu dvaju neključnih elemenata?</p>
''',
        r'''
<p>Dovoljno je gledati zamjene u kojima je $a_i$ ključan za prefiks ili $a_j$ ključan za sufiks. Ključ–ključ parova ima $\le 31^2$ po rezu; za ključ i proizvoljni $a_j$ vrijednost „AND prefiksa bez $a_i$” poprima $\le 31$ različitih vrijednosti po $k$, pa se za svaku traži $\max_j (v\,\&\,a_j)$ sufiksnim prolazom.</p>
''',
    ],
    'coach': [
        ('Koliko različitih vrijednosti može poprimiti prefiksni AND?',
         r'''
<p>Kad $k$ raste, $p_k$ može samo gubiti bitove; $a_i<2^{30}$, pa ima najviše $31$ promjena (početna vrijednost „svi bitovi” računa se kao prva). Pozicije u kojima se $p$ mijenja zovemo ključnim za prefiks; slično za sufiksni AND $s_k=a_k\,\&\dots\&\,a_n$ i ključne pozicije sufiksa. Ukupno je ključnih $O(\log \max a)$.</p>
'''),
        ('Što izbacivanje neključnog elementa čini AND-u?',
         r'''
<p>Ako $i$ nije ključan, $p_i=p_{i-1}$, tj. $a_i\supseteq p_{i-1}$ (kao skupovi bitova). Za svaki $k\ge i$ tada je $\text{AND}(1..k\setminus\{i\})=p_{i-1}\,\&\,\text{AND}(i+1..k)=p_{i-1}\,\&\,a_i\,\&\,\text{AND}(i+1..k)=p_k$. Isto za sufiks. Zaključak: zamjena $a_i\leftrightarrow a_j$ ($i\le k<j$) u kojoj je $i$ neključan za prefiks daje lijevi AND $p_k\,\&\,a_j\le p_k$; ako je i $j$ neključan za sufiks, desni AND je $s_{k+1}\,\&\,a_i\le s_{k+1}$ – ukupno ne bolje od „bez zamjene” pri istom rezu. Dakle u korisnoj zamjeni barem je jedan od $i$ (za prefiks) i $j$ (za sufiks) ključan.</p>
'''),
        ('Kako obraditi zamjene ključ–ključ?',
         r'''
<p>Za rez $k$, ključne $i\le k$ i $j>k$: vrijednost je $(\text{AND}(1..k\setminus\{i\})\,\&\,a_j)+(\text{AND}(k+1..n\setminus\{j\})\,\&\,a_i)$. Veličine $\text{AND}(1..k\setminus\{i\})$ za sve ključne $i$ održavamo inkrementalno dok $k$ raste (tablica $pa[k][x]$, $O(31n)$ memorije), a $\text{AND}(k+1..n\setminus\{j\})$ dok $k$ pada. Po rezu ima $\le 31\cdot31$ parova, ukupno $O(31^2 n)$ – u praksi znatno manje jer ključnih rijetko ima 31.</p>
'''),
        ('Kako obraditi zamjenu ključnog $a_i$ s proizvoljnim $a_j$ na drugoj strani?',
         r'''
<p>Ako je $j$ neključan za sufiks, desni AND je točno $s_{k+1}\,\&\,a_i$ (ne ovisi o $j$), a lijevi je $v_k\,\&\,a_j$ gdje je $v_k=\text{AND}(1..k\setminus\{i\})$. Za fiksni ključni $i$ niz $v_k$ ($k\ge i$) je nerastući po bitovima, dakle konstantan na $\le31$ komada. Na komadu s vrijednošću $v$ treba $\max_{j>k}(v\,\&\,a_j)$ za svaki $k$ – jedan prolaz zdesna sa sufiksnim maksimumom. Trošak $O(31\cdot n)$ po ključnom $i$, tj. $O(31^2n)$ ukupno. Za ključne $j$ i proizvoljne $i$ radimo zrcalno. Ako $j$ ipak jest ključan, formula daje donju ogradu stvarne vrijednosti (ispravno se računa u slučaju ključ–ključ), pa nikad ne precjenjujemo.</p>
'''),
        ('Zašto je rezultat ispravan i koje su zamke?',
         r'''
<p>Svaka kandidatska vrijednost koju izračunamo dostižna je (ili je donja ograda dostižne), a svaka optimalna zamjena pripada jednom od slučajeva: bez zamjene, ključ–ključ, ključ–neključ, neključ–ključ (neključ–neključ je dominiran). Zbroj dvaju AND-ova može biti do $2\cdot10^9$ – <code>long long</code>. „Svi bitovi” inicijaliziramo kao $-1$ (sve jedinice u dvojnom komplementu), pa je $\text{FULL}\,\&\,x=x$.</p>
'''),
    ],
    'tips': [
        r'''<strong>AND/OR prefiksi mijenjaju se $O(\log V)$ puta</strong> – to ograničava broj „zanimljivih” pozicija i pretvara kvadratne pretrage u $O(n\log^2 V)$.''',
        r'''Kod „najviše jedna zamjena/promjena” pokaži da promjena elemenata koji ne utječu na agregat ne može pomoći – ostaje malo kandidata koje se isplati nabrojati.''',
        r'''Kad je jedna strana izraza konstantna na komadima, a druga ovisi o $\max_{j>k}(v\,\&\,a_j)$, sufiksni maksimum po komadu daje sve odgovore u jednom prolazu.''',
        r'''Za „AND svih osim jednog” u prefiksu koristi $p_{i-1}\,\&\,\text{AND}(i+1..k)$ i održavaj drugi faktor inkrementalno dok $k$ raste.''',
    ],
    'solution': r'''
<p>Prefiksni AND $p_k$ mijenja se u $\le31$ ključnih pozicija; isto sufiksni $s_k$. Ako $i$ nije ključan za prefiks, izbacivanje $a_i$ iz prefiksa $1..k$ ne mijenja AND, pa zamjena dvaju neključnih elemenata nije bolja od „bez zamjene”. Preostaju: (a) bez zamjene, $\max_k p_k+s_{k+1}$; (b) ključ–ključ: za svaki rez $k$ i par ključnih $i\le k<j$ vrijednost $(\text{AND}(1..k\setminus i)\,\&\,a_j)+(\text{AND}(k+1..n\setminus j)\,\&\,a_i)$, uz inkrementalno održavane AND-ove bez jednog elementa; (c) ključni $i$ s proizvoljnim $j>k$: desni dio je $s_{k+1}\,\&\,a_i$, lijevi $v_k\,\&\,a_j$ gdje je $v_k$ konstantan na $\le31$ komada, pa na svakom komadu prolazom zdesna računamo $\max_{j>k}(v\,\&\,a_j)$; (c') zrcalno za ključni $j$. Složenost $O(n\log^2 V)$, u praksi puno brže. Ideja slijedi službeno rješenje GDCPC-a 2023 i analizu prihvaćenih predaja; implementacija je napisana iznova.</p>
''',
    'detailed': r'''
<h3>1. Ključne pozicije</h3>
<p>Neka je $p_k=a_1\,\&\dots\&\,a_k$ ($p_0$ = svi bitovi) i $s_k=a_k\,\&\dots\&\,a_n$ ($s_{n+1}$ = svi bitovi). Niz $p_k$ je po bitovima nerastući, pa se mijenja u najviše $31$ pozicija (svaka promjena briše bar jedan od $\le 30$ bitova; prva pozicija se uvijek računa). Pozicije $i$ s $p_i\ne p_{i-1}$ su <em>ključne za prefiks</em> ($P\le31$ njih); analogno $j$ s $s_j\ne s_{j+1}$ su ključne za sufiks ($S\le 31$).</p>
<h3>2. Lema o neključnim elementima</h3>
<p><em>Ako $i$ nije ključan za prefiks, tada za svaki $k\ge i$ vrijedi $\text{AND}(1..k\setminus\{i\})=p_k$.</em> Dokaz: $p_i=p_{i-1}$ znači $p_{i-1}\,\&\,a_i=p_{i-1}$. Tada $\text{AND}(1..k\setminus\{i\})=p_{i-1}\,\&\,\text{AND}(i+1..k)=(p_{i-1}\,\&\,a_i)\,\&\,\text{AND}(i+1..k)=p_k$. Simetrično za sufiks.</p>
<p><em>Posljedica.</em> Zamjena $a_i\leftrightarrow a_j$, $i\le k<j$, daje vrijednost $(\text{AND}(1..k\setminus i)\,\&\,a_j)+(\text{AND}(k+1..n\setminus j)\,\&\,a_i)$. Ako je $i$ neključan za prefiks, prvi pribrojnik je $p_k\,\&\,a_j\le p_k$; ako je $j$ neključan za sufiks, drugi je $s_{k+1}\,\&\,a_i\le s_{k+1}$. Kad su oba neključna, vrijednost je $\le p_k+s_{k+1}$ – ne bolja od reza $k$ bez zamjene. Zato se optimum postiže u jednom od slučajeva: bez zamjene; $i$ i $j$ ključni; $i$ ključan, $j$ neključan; $i$ neključan, $j$ ključan.</p>
<h3>3. AND bez jednog elementa</h3>
<p>Za ključni $i=pk[x]$ i $k\ge i$ definiramo $pa[k][x]=\text{AND}(1..k\setminus\{i\})=p_{i-1}\,\&\,\text{AND}(i+1..k)$; drugi faktor održavamo inkrementalno dok $k$ raste: $O(P\,n)$ vremena i memorije ($31\cdot10^5$ cijelih brojeva). Zrcalno $sa[k][y]=\text{AND}(k+1..n\setminus\{sk[y]\})$ za $sk[y]>k$.</p>
<h3>4. Slučaj ključ–ključ</h3>
<p>Prolazimo $k$ od $n-1$ do $1$, održavamo $sa$ za trenutačni $k$, i za sve ključne $i\le k$ i $j>k$ računamo $(pa[k][x]\,\&\,a_j)+(sa[y]\,\&\,a_i)$. Vrijednost je točna (oba AND-a su bez zamijenjenog elementa). Najviše $P\cdot S\le 31^2$ parova po rezu.</p>
<h3>5. Slučaj ključni $i$, proizvoljni $j$</h3>
<p>Za neključni $j$ desni AND je točno $s_{k+1}\,\&\,a_i$ po lemi, a lijevi $v_k\,\&\,a_j$ s $v_k=pa[k][x]$. Za fiksni $x$ niz $v_k$ je nerastući po bitovima (dodavanje elemenata samo briše bitove) i konstantan na $\le31$ maksimalnih komada $[k_0,k_{\text{end}}]$. Za komad s vrijednošću $v$ trebamo $M_k=\max_{j>k}(v\,\&\,a_j)$ za sve $k$ u komadu; prolazimo $j$ od $n$ prema $k_0+1$ održavajući sufiksni maksimum $\text{sm}$, i za $k=j-1$ u komadu ažuriramo odgovor s $\text{sm}+(s_{j}\,\&\,a_i)$. Trošak po komadu $O(n)$, po ključnom $i$ $O(31n)$. Ako je $j$ ipak ključan, $s_{k+1}\,\&\,a_i\le\text{AND}(k+1..n\setminus j)\,\&\,a_i$, pa je izračunata vrijednost donja ograda dostižne vrijednosti – ne kvari maksimum, a točna se vrijednost računa u slučaju 4. Slučaj „ključni $j$, proizvoljni $i$” obrađujemo zrcalno s tablicom $sa2[k][y]$ i prefiksnim maksimumom.</p>
<h3>6. Algoritam i složenost</h3>
<ol>
<li>Izračunaj $p$, $s$, ključne pozicije $pk$, $sk$.</li>
<li>$\text{best}=\max_k p_k+s_{k+1}$.</li>
<li>Tablica $pa$; slučaj ključ–ključ prolazom zdesna.</li>
<li>Slučaj (c) po komadima za svaki $x$; tablica $sa2$ i slučaj (c') zrcalno.</li>
</ol>
<p>Vrijeme $O(n\cdot P\cdot S+n\cdot P\cdot 31+n\cdot S\cdot 31)=O(n\log^2 V)$ u najgorem slučaju (oko $10^8$ jednostavnih operacija za $n=10^5$, $P=S=31$); memorija $O(n\log V)$. Na stvarnim testovima $P,S$ su obično znatno manji od $31$.</p>
<h3>7. Zamke</h3>
<ul>
<li>Neutralni element za AND je „svi bitovi”: koristimo <code>-1</code> (sve jedinice), jer $a_i\ge0$ pa je rezultat uvijek nenegativan.</li>
<li>Zbroj dviju vrijednosti do $10^9$ traži <code>long long</code>.</li>
<li>Rez $k$ ide od $1$ do $n-1$ – obje strane moraju biti neprazne; pri zamjeni $i\le k<j$.</li>
<li>Prva pozicija $1$ i posljednja $n$ uvijek su ključne (promjena s „svi bitovi”).</li>
</ul>
<h3>8. Primjer</h3>
<p>$(6,5,4,3,5,6)$: $p=(6,4,4,0,0,0)$, ključne za prefiks $\{1,2,4\}$; $s=(0,0,0,0,4,6)$ (indeksi $1..6$), ključne za sufiks $\{6,5,4\}$. Bez zamjene najbolje je $6$ ($k=1$: $6+0$ ili $k=5$: $0+6$). Ključ–ključ $i=4$, $j=6$, $k=5$: lijevo $\text{AND}(6,5,4,5)\,\&\,6=4\,\&\,6=4$, desno $\text{AND}(\emptyset)\,\&\,3=3$, ukupno $7$ – odgovor.</p>
''',
    'verified': r'''uzorci 3/3; 300 slučajnih testova ($n\le 8$, male vrijednosti s gustim bitovima) protiv brute forcea koji isprobava sve zamjene i sve rezove; 3 velika testa ($n=10^5$, vrijednosti do $10^9$ uz konstrukciju s $\approx 30$ ključnih pozicija na obje strane), najsporiji $0.03$ s.''',
},
# ---------------------------------------------------------------- I
{
    'letter': 'I', 'title': 'Digit Mode', 'title_hr': 'Mod znamenaka', 'slug': 'I_digit_mode',
    'tl': '2 s', 'ml': '256 MiB',
    'statement': r'''
<p>Neka je $m(x)$ mod znamenaka dekadskog zapisa od $x$ — najveća znamenka među onima koje se pojavljuju najčešće: $m(15532) = 5$, $m(25252) = 2$, $m(103000) = 0$, $m(364364) = 6$, $m(114514) = 1$, $m(889464) = 8$.</p>
<p>Za dani $n$ izračunaj $\left(\sum_{x=1}^{n} m(x)\right) \bmod (10^9 + 7)$.</p>
<h3>Ulaz</h3>
<p>$T$ testova; $1 \le n \lt 10^{50}$ bez vodećih nula; $\sum |n| \le 50$ (broj znamenaka).</p>
<h3>Izlaz</h3>
<p>Za svaki test tražena vrijednost.</p>
<h3>Primjer</h3>
<p>$n = 9 \to 45$; $99 \to 615$; $999 \to 6570$; $99999 \to 597600$; $999999 \to 5689830$.</p>
''',
    'hints': [
        r'''
<p>Klasična digit-DP dekompozicija: svaki $x\le n$ ima ili manje znamenaka, ili dijeli s $n$ prefiks pa na nekoj poziciji ima manju znamenku – nakon toga je $r$ pozicija potpuno slobodno. Fiksiranih prefiksa ima samo $O(9\cdot|n|)$.</p>
''',
        r'''
<p>Za fiksni prefiks (poznat multiskup znamenaka $\text{cnt}$) i $r$ slobodnih pozicija, zbroj modova je $\sum_m m\cdot\#\{\text{popunjavanja s modom }m\}$. Mod je $m$ akko je njegova ukupna frekvencija $c$ barem jednaka frekvencijama manjih znamenaka i strogo veća od frekvencija većih.</p>
''',
        r'''
<p>Fiksiraj i $c$. Broj popunjavanja je multinomni koeficijent $\dfrac{r!}{(c-\text{cnt}_m)!\prod_e k_e!}$ zbrojen po svim $(k_e)$ s ograničenjima $k_e\le\text{cap}_e$; zbroj $\prod 1/k_e!$ računaj DP-om po znamenkama (kao produkt eksponencijalnih generirajućih funkcija).</p>
''',
    ],
    'coach': [
        ('Kako svesti zbroj po $x\le n$ na malen broj „slobodnih” podproblema?',
         r'''
<p>Brojevi $x\le n$ dijele se na: (a) brojeve s manje znamenaka – vodeća znamenka $d\in\{1..9\}$ pa $\ell-1$ slobodnih pozicija; (b) brojeve iste duljine koji se s $n$ podudaraju na prefiksu duljine $p$, na poziciji $p$ imaju znamenku $d<n_p$ (za $p=0$ i $d\ge1$), a preostalih $r=|n|-1-p$ pozicija je slobodno; (c) sam $n$. U svakom slučaju poznat je multiskup već fiksiranih znamenaka $\text{cnt}[0..9]$ i broj slobodnih pozicija $r$; takvih podproblema ima najviše $9|n|+9|n|+1$.</p>
'''),
        ('Kako izraziti „mod je $m$” preko frekvencija?',
         r'''
<p>Mod je najveća znamenka među najčešćima: $m$ je mod akko je $\text{freq}(m)\ge\text{freq}(e)$ za $e<m$ i $\text{freq}(m)>\text{freq}(e)$ za $e>m$. Ako fiksiramo $m$ i njegovu ukupnu frekvenciju $c$ (od $\max(\text{cnt}_m,1)$ do $\text{cnt}_m+r$), ograničenja za ostale znamenke postaju neovisna: ukupno $\le c$ za $e<m$, $\le c-1$ za $e>m$, tj. na slobodnim pozicijama $k_e\le\text{cap}_e=(c\text{ ili }c-1)-\text{cnt}_e$. Ako je neki $\text{cap}_e<0$, kombinacija $(m,c)$ je nemoguća.</p>
'''),
        ('Koliko popunjavanja slobodnih pozicija ima za fiksne $(m,c)$?',
         r'''
<p>Znamenka $m$ zauzima točno $c-\text{cnt}_m$ slobodnih pozicija, ostalih $\text{rest}=r-(c-\text{cnt}_m)$ pozicija popunjavaju ostale znamenke s frekvencijama $k_e\le\text{cap}_e$, $\sum k_e=\text{rest}$. Broj nizova s danim frekvencijama je multinomni koeficijent $\frac{r!}{(c-\text{cnt}_m)!\prod_e k_e!}$. Dakle treba $S=\sum_{(k_e)}\prod_e\frac1{k_e!}$, što je koeficijent uz $x^{\text{rest}}$ u produktu odrezanih eksponencijalnih redova $\prod_{e\ne m}\sum_{k=0}^{\text{cap}_e}\frac{x^k}{k!}$ – računamo ga DP-om (knapsack) po znamenkama u $O(9\cdot\text{rest}\cdot\max\text{cap})$. Ukupno popunjavanja je $S\cdot r!/(c-\text{cnt}_m)!$.</p>
'''),
        ('Je li ukupna složenost prihvatljiva i što s modularnom aritmetikom?',
         r'''
<p>Podproblema je $O(9|n|)$, po podproblemu $10$ izbora $m$, $O(r)$ izbora $c$ i DP $O(9r^2)$ – reda $10^8$ jednostavnih operacija za $|n|=50$ u najgorem slučaju, ali uz $\sum|n|\le 50$ i mnogo neizvedivih kombinacija stvarno je znatno manje (mjereno $<0.3$ s). Faktorijele i inverzne faktorijele do $50$ predračunamo; $1/k!$ je modularni inverz jer je $10^9+7$ prost.</p>
'''),
        ('Koje rubne slučajeve treba posebno gledati?',
         r'''
<p>Znamenka $m$ mora se pojaviti barem jednom ($c\ge1$), inače nije kandidat; vodeća znamenka nikad nije $0$; sam broj $n$ pribrajamo zasebno, izravno računajući njegov mod; kod $|n|=1$ nema kraćih brojeva i petlje se prirodno preskaču.</p>
'''),
    ],
    'tips': [
        r'''<strong>Digit DP + brojanje multiskupova:</strong> kad svojstvo ovisi o frekvencijama znamenaka, a ne o poretku, fiksiraj prefiks i broji popunjavanja preostalih pozicija multinomnim koeficijentima.''',
        r'''Uvjet „maksimum s pravilom za neriješeno” (najveći među najčešćima) rastavi na neovisna ograničenja: $\le c$ za manje, $\le c-1$ za veće kandidate.''',
        r'''Zbroj $\prod 1/k_e!$ uz ograničenja $k_e\le\text{cap}_e$ je koeficijent produkta odrezanih eksponencijalnih redova – knapsack DP po vrstama, a na kraju pomnoži s $r!$.''',
        r'''Za male granice ($r\le 50$) faktorijele i inverzne faktorijele predračunaj jednom; sve umnoške odmah reduciraj modulo $10^9+7$ u 64 bita.''',
    ],
    'solution': r'''
<p>Digit DP: svaki $x\le n$ ima manje znamenaka ili dijeli s $n$ prefiks pa ima manju znamenku – tada je poznat multiskup fiksiranih znamenaka $\text{cnt}$ i $r$ slobodnih pozicija. Za takav podproblem zbroj modova je $\sum_m m\cdot N(m)$, a $N(m)$ računamo po ukupnoj frekvenciji $c$ znamenke $m$: ostale znamenke $e$ smiju na slobodnim pozicijama doći najviše $\text{cap}_e=c-\text{cnt}_e$ puta ($e<m$) odnosno $c-1-\text{cnt}_e$ puta ($e>m$). Broj popunjavanja je $\frac{r!}{(c-\text{cnt}_m)!}\sum\prod_e\frac1{k_e!}$ po $(k_e)$ sa $\sum k_e=r-(c-\text{cnt}_m)$, $k_e\le\text{cap}_e$; unutarnji zbroj je koeficijent produkta odrezanih eksponencijalnih redova, koji računamo knapsack DP-om po znamenkama. Sam $n$ dodamo izravno. Složenost $O(|n|\cdot 10\cdot|n|\cdot 9|n|^2)$ u najgorem slučaju, u praksi ispod $0.3$ s. Ideja slijedi službeno rješenje izvornog zadatka (2019 Shaanxi Provincial Contest, objavljeno na SUA wikiju) i analizu prihvaćenih predaja; implementacija je napisana iznova.</p>
''',
    'detailed': r'''
<h3>1. Dekompozicija po prefiksu</h3>
<p>Neka $n$ ima $L$ znamenaka $n_0n_1\dots n_{L-1}$. Svaki $x$ s $1\le x\le n$ pripada točno jednoj od klasa:</p>
<ul>
<li>$x$ ima $\ell<L$ znamenaka s vodećom $d\in\{1,\dots,9\}$; preostalih $r=\ell-1$ pozicija je proizvoljno;</li>
<li>$x$ ima $L$ znamenaka, podudara se s $n$ na pozicijama $0..p-1$, na poziciji $p$ ima $d<n_p$ ($d\ge1$ ako $p=0$); preostalih $r=L-1-p$ pozicija je proizvoljno;</li>
<li>$x=n$.</li>
</ul>
<p>U prve dvije klase fiksirani dio određuje vektor frekvencija $\text{cnt}[0..9]$, a slobodne pozicije primaju bilo koje znamenke (uključivo $0$). Definiramo $F(\text{cnt},r)=\sum$ moda po svih $10^r$ popunjavanja. Odgovor je zbroj $F$ po klasama plus $m(n)$.</p>
<h3>2. Karakterizacija moda</h3>
<p>Za konačni broj neka je $\text{freq}(e)$ ukupna frekvencija znamenke $e$. Znamenka $m$ je mod akko $\text{freq}(m)\ge\text{freq}(e)$ za sve $e<m$ i $\text{freq}(m)>\text{freq}(e)$ za sve $e>m$ (najveća među najčešćima). Ta su ograničenja po znamenkama neovisna čim fiksiramo $c=\text{freq}(m)$.</p>
<h3>3. Brojanje za fiksne $(m,c)$</h3>
<p>Neka je $c\in[\max(\text{cnt}_m,1),\ \text{cnt}_m+r]$. Znamenka $m$ zauzima točno $u=c-\text{cnt}_m$ slobodnih pozicija; preostalih $\text{rest}=r-u$ pozicija dijele ostale znamenke s frekvencijama $k_e$ takvima da $\text{cnt}_e+k_e\le c$ ($e<m$) odnosno $\le c-1$ ($e>m$); označimo $\text{cap}_e$ pripadnu gornju granicu za $k_e$. Ako je neki $\text{cap}_e<0$, već fiksirani dio krši uvjet i $(m,c)$ ne doprinosi.</p>
<p>Broj nizova duljine $r$ s točno $u$ znamenaka $m$ i $k_e$ znamenaka $e$ je multinomni koeficijent $\dfrac{r!}{u!\prod_e k_e!}$. Zbrojimo po svim dopuštenim $(k_e)$:
$$N(m,c)=\frac{r!}{u!}\sum_{\substack{\sum k_e=\text{rest}\\ 0\le k_e\le\text{cap}_e}}\ \prod_{e\ne m}\frac{1}{k_e!}.$$
Unutarnji zbroj je koeficijent uz $x^{\text{rest}}$ u $\prod_{e\ne m}\big(\sum_{k=0}^{\text{cap}_e}x^k/k!\big)$ – produkt odrezanih eksponencijalnih generirajućih funkcija. Računamo ga knapsack DP-om: $f[0]=1$, za svaku znamenku $e\ne m$ i $j$ od $\text{rest}$ prema dolje $f[j]\gets\sum_{k=0}^{\min(\text{cap}_e,j)}f[j-k]/k!$ (obrada od većeg $j$ prema manjem omogućuje rad na mjestu). Na kraju $N(m,c)=f[\text{rest}]\cdot r!\cdot(u!)^{-1}$.</p>
<p>$F(\text{cnt},r)=\sum_{m=0}^{9}m\sum_c N(m,c)$. Za $m=0$ doprinos je $0$, ali petlja je uredna i tako.</p>
<h3>4. Algoritam</h3>
<ol>
<li>Predračunaj $k!$ i $(k!)^{-1}$ za $k\le 50$ modulo $10^9+7$ (Fermatov mali teorem).</li>
<li>Za $\ell=1..L-1$ i $d=1..9$: $\text{cnt}=\{d\}$, dodaj $F(\text{cnt},\ell-1)$.</li>
<li>Prolazi pozicije $p=0..L-1$ održavajući $\text{cnt}$ prefiksa od $n$; za svaku $d<n_p$ (uz $d\ge1$ ako $p=0$) privremeno dodaj $d$ i dodaj $F(\text{cnt},L-1-p)$; zatim dodaj $n_p$ u $\text{cnt}$.</li>
<li>Dodaj $m(n)$ (najveća znamenka s najvećim $\text{cnt}$).</li>
</ol>
<h3>5. Složenost</h3>
<p>Podproblema je $O(9L)$; po podproblemu $10$ kandidata $m$, do $r+1$ vrijednosti $c$ i DP s $9$ znamenaka i $O(r\cdot\min(\text{cap},r))$ koraka, dakle $O(9L\cdot10\cdot L\cdot 9L^2)=O(810L^4)$, oko $5\cdot10^9$ u vrlo pesimističnoj procjeni za $L=50$; stvarno je znatno manje jer $\text{rest}$ i $\text{cap}$ padaju s $c$, mnogi $(m,c)$ su neizvedivi, a $\sum L\le50$. Mjereno vrijeme za $|n|=50$ je ispod $0.3$ s. Memorija $O(L)$.</p>
<h3>6. Zamke</h3>
<ul>
<li>Vodeća znamenka nije $0$ – u klasama (a) i (b) za $p=0$ počni od $d=1$.</li>
<li>Kandidat $m$ mora se pojaviti barem jednom: $c\ge1$ (npr. mod od $103000$ je $0$ jer se $0$ pojavljuje tri puta).</li>
<li>Izračun $m(n)$ za sam $n$ radi zasebno; petlja s $\ge$ od $0$ do $9$ automatski bira najveću među najčešćima.</li>
<li>Sve množi u 64 bita i reduciraj modulo nakon svakog umnoška.</li>
</ul>
<h3>7. Primjer</h3>
<p>$n=99$: brojevi $1..9$ daju $45$ (klasa (a) s $r=0$: mod je sama znamenka). Za $p=0$, $d\in\{1..8\}$, $r=1$: popunjavanje znamenkom $e$; ako $e=d$ mod je $d$, ako $e\ne d$ mod je $\max(d,e)$. Za $p=1$, $d\in\{0..8\}$ uz prefiks $9$, $r=0$: mod je $9$ (frekvencije $1$ i $1$, veća znamenka). Plus $m(99)=9$. Zbroj je $615$, kao u primjeru.</p>
''',
    'verified': r'''uzorci 5/5; 300 slučajnih testova ($n\le 3\cdot10^4$, više testova po ulazu) protiv brute forcea koji za svaki $x$ izravno računa mod znamenaka; 3 velika testa ($|n|=50$), najsporiji $0.29$ s.''',
},
# ---------------------------------------------------------------- J
{
    'letter': 'J', 'title': 'Escape Plan', 'title_hr': 'Plan bijega', 'slug': 'J_escape_plan',
    'tl': '3 s', 'ml': '256 MiB',
    'statement': r'''
<p>Grad ima $n$ mjesta i $m$ neusmjerenih staza duljine $w_i$. BaoBao kreće iz mjesta $1$ i mora doći do bilo kojeg od $k$ izlaza $e_1, \dots, e_k$. Odmah nakon što stigne u mjesto $i$, čudovišta blokiraju najviše $d_i$ staza iz tog mjesta (pri svakom posjetu iznova, možda različite). BaoBao ne zna unaprijed koje.</p>
<p>Odredi najkraće vrijeme za bijeg u najgorem slučaju.</p>
<h3>Ulaz</h3>
<p>$T \approx 100$ testova; $1 \le n \le 10^5$, $1 \le m \le 10^6$, $1 \le k \le n$; izlazi; $0 \le d_i \le m$; staze $x_i \ne y_i$, $1 \le w_i \le 10^4$; $\sum n \le 10^6$, $\sum m \le 3 \cdot 10^6$.</p>
<h3>Izlaz</h3>
<p>Za svaki test najkraće vrijeme u najgorem slučaju ili $-1$ ako bijeg nije zajamčen.</p>
<h3>Primjer</h3>
<p>$n = 3$, izlaz $3$, $d = (1, 1, 1)$, staze $(1,2,1), (1,2,2), (2,3,1), (2,3,2)$: $4$. $n = 3$, izlazi $2, 3$, $d = (2, 0, 0)$, staze $(1,2,1), (1,3,1)$: $-1$.</p>
''',
    'hints': [
        r'''
<p>Definiraj $f(v)$ = najgore vrijeme bijega iz $v$. Kad BaoBao stoji u $v$, čudovišta blokiraju najviše $d_v$ staza, a on bira najbolju preostalu. Koji je „rang” staze koju će na kraju moći upotrijebiti?</p>
''',
        r'''
<p>$f(v)$ je $(d_v+1)$-va najmanja vrijednost među $w+f(u)$ po svim stazama $(v,u,w)$ (paralelne staze brojimo zasebno); ako ih je manje od $d_v+1$, $f(v)=\infty$. Za izlaze $f=0$.</p>
''',
        r'''
<p>To je fiksna točka Dijkstrina tipa: pokreni Dijkstru unatrag iz svih izlaza i vrh $v$ proglasi konačnim tek kad ga iz reda izvadiš $(d_v+1)$-vi put.</p>
''',
    ],
    'coach': [
        ('Kako formalizirati „najgori slučaj” kad čudovišta biraju nakon dolaska?',
         r'''
<p>Igra je memorijska samo lokalno: u trenutku kad BaoBao stigne u $v$, budućnost ovisi samo o $v$ (pri svakom posjetu čudovišta biraju iznova). Neka je $f(v)$ najkraće zajamčeno vrijeme iz $v$; za izlaz $f=0$. Čudovišta blokiraju do $d_v$ staza, BaoBao zatim bira stazu $(v,u,w)$ koja minimizira $w+f(u)$ među neblokiranima. Protivnik će blokirati upravo $d_v$ najboljih, pa je $f(v)$ $(d_v+1)$-va najmanja vrijednost $w+f(u)$, odnosno $\infty$ ako staza nema dovoljno.</p>
'''),
        ('Zašto se povratak u već posjećeno mjesto nikad ne isplati i zašto rekurzija ima jedinstveno rješenje?',
         r'''
<p>Sve su težine $w\ge1$, pa svaki korak strogo povećava vrijeme; vrijednost $f(v)$ ovisi samo o vrhovima s manjim $f$. Zato se $f$ može računati u rastućem poretku – baš kao udaljenosti u Dijkstri, gdje se relaksacija oslanja samo na već konačne vrhove.</p>
'''),
        ('Kako Dijkstru prilagoditi „$(d_v+1)$-vom najmanjem” umjesto minimumu?',
         r'''
<p>Pokrenemo Dijkstru unatrag iz svih izlaza (svi s $0$ u redu). Kad konačan vrh $u$ s vrijednošću $f(u)$ obradimo, za svaku stazu $(u,v,w)$ u red stavimo kandidata $(f(u)+w,v)$. Vrh $v$ (koji nije izlaz) postaje konačan tek kad ga iz reda izvadimo $(d_v+1)$-vi put – s vrijednošću tog kandidata. Kandidati izlaze iz reda u nepadajućem poretku, a svi kandidati za $v$ nastaju iz konačnih susjeda s $f(u)\le$ trenutačna vrijednost; kandidati koji još nisu nastali imaju vrijednost $>$ trenutačne. Zato je $(d_v+1)$-vi izvađeni kandidat upravo $(d_v+1)$-va najmanja vrijednost $w+f(u)$.</p>
'''),
        ('Što s paralelnim stazama, izlazima i nedostižnim vrhovima?',
         r'''
<p>Paralelne staze su različite staze – čudovišta blokiraju staze, ne susjede – pa svaka daje vlastitog kandidata (prvi primjer: $f(2)$ je druga najmanja od $\{1,2\}$, tj. $2$, a $f(1)$ druga najmanja od $\{3,4\}$, tj. $4$). Izlazi su konačni odmah s $0$ i brojač ih ne dira. Ako vrh $1$ nikad ne postane konačan, odgovor je $-1$ (drugi primjer: $d_1=2$ blokira obje staze).</p>
'''),
        ('Kolika je složenost i na što paziti u implementaciji?',
         r'''
<p>Svaka staza generira najviše dva kandidata (jednom iz svakog kraja), pa je red veličine $O(m)$ i složenost $O((n+m)\log m)$. Uz $\sum m\le3\cdot10^6$ potrebno je brzo čitanje ulaza i kompaktna CSR reprezentacija grafa; udaljenosti staju u <code>long long</code> (najviše $10^4\cdot 10^5$, staje i u 32 bita, ali sigurnije je 64).</p>
'''),
    ],
    'tips': [
        r'''<strong>„Protivnik blokira $k$ najboljih opcija” = $(k+1)$-va najmanja vrijednost.</strong> U Dijkstri to znači: vrh postaje konačan pri $(k+1)$-vom vađenju iz reda, ne pri prvom.''',
        r'''Kad je cilj skup vrhova (više izlaza), obrni smjer i kreni iz svih ciljeva istovremeno s udaljenošću $0$.''',
        r'''Kod igara u kojima protivnik bira nakon svakog poteza, provjeri je li situacija „bez memorije” – tada je rekurzija po vrhovima dovoljna i ne treba pamtiti povijest.''',
        r'''Za $m\sim10^6$ po testu koristi <code>fread</code> i CSR (kompaktne liste susjedstva) umjesto <code>vector&lt;vector&gt;</code>.''',
    ],
    'solution': r'''
<p>Neka je $f(v)$ najgore vrijeme bijega iz $v$; za izlaze $f=0$. Čudovišta blokiraju $d_v$ najboljih staza, pa je $f(v)$ $(d_v+1)$-va najmanja vrijednost među $w+f(u)$ po stazama $(v,u,w)$ (paralelne staze zasebno), ili $\infty$ ako staza nema dovoljno. Budući da su težine pozitivne, $f$ računamo Dijkstrom unatrag iz svih izlaza: vrh $v$ postaje konačan tek kad ga iz prioritetnog reda izvadimo $(d_v+1)$-vi put, jer kandidati izlaze u nepadajućem poretku i svi manji kandidati za $v$ već su nastali. Odgovor je $f(1)$ ili $-1$. Složenost $O((n+m)\log m)$ uz brzo čitanje i CSR graf. Ideja slijedi službeno rješenje izvornog zadatka (2019 Shaanxi Provincial Contest, objavljeno na SUA wikiju) i analizu prihvaćenih predaja; implementacija je napisana iznova.</p>
''',
    'detailed': r'''
<h3>1. Model najgoreg slučaja</h3>
<p>Kad BaoBao stigne u mjesto $v$, čudovišta odabiru do $d_v$ staza iz $v$ koje blokiraju, a on zatim bira među preostalima. Budući da se pri svakom posjetu blokira iznova i BaoBao ne zna unaprijed, buduće vrijeme ovisi samo o mjestu u kojem se nalazi; definiramo $f(v)$ = najkraće vrijeme koje BaoBao može <em>zajamčiti</em> iz $v$. Za izlaz je $f=0$.</p>
<h3>2. Rekurzija</h3>
<p>Za neizlazni $v$ neka su $c_1\le c_2\le\dots\le c_{\deg v}$ sortirane vrijednosti $w+f(u)$ po svim stazama $(v,u,w)$ (paralelne staze zasebno). BaoBao bi izabrao najmanju neblokiranu; čudovišta, koja mu žele naštetiti, blokiraju $c_1,\dots,c_{d_v}$ (blokiranje bilo koje druge kombinacije ostavlja mu bolju ili jednaku opciju). Stoga
$$f(v)=c_{d_v+1},\qquad f(v)=\infty\ \text{ako }\deg v\le d_v.$$
To je istodobno donja ograda (protivnik to može postići) i dostižna (BaoBao uvijek uzme najbolju neblokiranu stazu).</p>
<p>Rekurzija je dobro definirana: $w\ge1$, pa je $f(v)>f(u)$ za stazu koja ostvaruje $c_{d_v+1}$; dakle $f(v)$ ovisi samo o vrhovima s strogo manjom vrijednošću, a vrhovi iz kojih se bijeg ne može zajamčiti dobivaju $\infty$ (nikakav ciklus ne može „pomoći” jer vrijeme samo raste).</p>
<h3>3. Dijkstra unatrag s brojačem</h3>
<p>Stavimo sve izlaze u min-red s vrijednošću $0$. Ponavljamo: izvadimo $(D,v)$ s najmanjim $D$.</p>
<ul>
<li>Ako je $v$ već konačan, preskoči.</li>
<li>Ako $v$ nije izlaz: $\text{cnt}[v]\mathrel{+}=1$; ako $\text{cnt}[v]\le d_v$, preskoči (to je jedan od $d_v$ najboljih kandidata koje čudovišta blokiraju).</li>
<li>Inače $f(v)=D$ i za svaku stazu $(v,u,w)$ s nekonačnim $u$ stavimo $(D+w,u)$ u red.</li>
</ul>
<p><em>Ispravnost.</em> Vrijednosti izvađene iz reda su nepadajuće (svaki umetnuti kandidat je $\ge$ trenutačno izvađenog jer $w\ge1$). Kad $v$ postane konačan s vrijednošću $D$, prethodno je izvađeno točno $d_v$ kandidata za $v$, svi $\le D$; svaki kandidat $w+f(u)$ za $v$ nastaje kad $u$ postane konačan, a $u$ s $f(u)\ge D$ (još nekonačni) daju kandidate $>D$. Dakle $D$ je $(d_v+1)$-va najmanja vrijednost, tj. $f(v)$. Indukcijom po poretku vađenja sve su vrijednosti točne. Vrhovi koji nikad ne postanu konačni imaju $f=\infty$: za njih se ne pojavi dovoljno kandidata, što odgovara $\deg v\le d_v$ u stvarnom (konačnom) dijelu grafa.</p>
<h3>4. Algoritam i složenost</h3>
<ol>
<li>Brzo učitaj $n,m,k$, izlaze, $d_i$ i staze; izgradi CSR liste susjedstva ($2m$ zapisa).</li>
<li>Dijkstra s brojačem kako je opisano.</li>
<li>Ispiši $f(1)$ ili $-1$.</li>
</ol>
<p>Svaka staza ubaci najviše dva kandidata, red ima $O(m)$ elemenata, složenost $O((n+m)\log m)$; za $\sum m\le 3\cdot10^6$ to je brzo. Memorija $O(n+m)$.</p>
<h3>5. Rubni slučajevi i zamke</h3>
<ul>
<li>Vrh $1$ može biti izlaz: odgovor $0$.</li>
<li>$d_i$ može biti veće od stupnja – tada vrh nikad ne postane konačan.</li>
<li>Izlazi se ne broje: kad BaoBao stigne na izlaz, pobjegao je.</li>
<li>Paralelne staze i višestruki kandidati istog susjeda su legitimni – ne dedupliciraj po susjedu.</li>
<li>$T\approx100$ testova s velikim $n$: alociraj strukture po testu veličine $n$, ne globalnog maksimuma svaki put.</li>
</ul>
<h3>6. Primjer</h3>
<p>Prvi primjer: izlaz $3$, $f(3)=0$. Kandidati za $2$: $1$ i $2$ (dvije staze do $3$); $d_2=1$ pa $f(2)=2$. Kandidati za $1$: $2+1=3$ i $2+2=4$; $d_1=1$ pa $f(1)=4$. Drugi primjer: $f(2)=f(3)=0$, kandidati za $1$: $1,1$, ali $d_1=2$ blokira oba – $f(1)=\infty$, ispis $-1$.</p>
''',
    'verified': r'''uzorci 2/2; 300 slučajnih testova (više malih grafova po ulazu, $n\le 6$, $m\le 8$, paralelne staze) protiv brute forcea koji rekurziju rješava iterativno do fiksne točke; 3 velika testa ($n=10^5$, $m=10^6$), najsporiji $0.27$ s.''',
},
# ---------------------------------------------------------------- K
{
    'letter': 'K', 'title': 'Final Defense Line', 'title_hr': 'Posljednja obrambena linija', 'slug': 'K_final_defense_line',
    'tl': '1 s', 'ml': '64 MiB',
    'statement': r'''
<p>Kružnica nepoznatog središta i radijusa. Za tri različite točke $A$, $B$, $C$ poznata je najkraća udaljenost do kružnice s predznakom: $0$ — na kružnici, $\gt 0$ — unutar kruga, $\lt 0$ — izvan (udaljenost je apsolutna vrijednost). Pravac se ne smatra kružnicom.</p>
<p>Odredi broj mogućih kružnica i radijus najmanje.</p>
<h3>Ulaz</h3>
<p>$1 \le T \le 2 \cdot 10^5$ testova; $A = (x_a, 0)$, $d_a$; $B = (x_b, 0)$, $d_b$ ($-100 \le x \le 100$, $1 \le d \le 100$); $C = (x_c, y_c)$, $d_c$ ($|{\cdot}| \le 100$, $d_c \ne 0$). Najmanji mogući radijus je $\le 10^4$.</p>
<h3>Izlaz</h3>
<p>$-1$ ako je kružnica beskonačno mnogo; $0$ ako nema nijedne; inače <code>m r</code> — broj kružnica i radijus najmanje (relativna greška $\le 10^{-6}$).</p>
<h3>Primjer</h3>
<p>$A = (0, 0), d_a = 1$; $B = (3, 0), d_b = 2$; $C = (10, 2), d_c = 2$: <code>2 10.327329213474</code>. Isto s $d_c = -2$: <code>2 5.341730785446</code>.</p>
''',
    'hints': [
        r'''
<p>Točka s predznačenom udaljenošću $d_i$ do kružnice $(x,y,R)$ zadovoljava $\sqrt{(x-x_i)^2+(y-y_i)^2}=R-d_i$ u oba slučaja ($d_i\gt0$ unutra, $d_i\lt0$ vani), uz $R\ge\max d_i$. To je Apolonijev problem: tražena kružnica dodiruje tri kružnice polumjera $|d_i|$ (iznutra ili izvana).</p>
''',
        r'''
<p>Oduzimanjem jednadžbi $(x-x_i)^2+(y-y_i)^2=(R-d_i)^2$ kvadratni članovi $x^2+y^2-R^2$ nestaju: razlike su <em>linearne</em> u $x,y,R$. Ako središta nisu kolinearna ($y_c\ne0$), $x$ i $y$ su linearne funkcije od $R$; uvrštavanjem u jednu jednadžbu dobivaš kvadratnu jednadžbu po $R$.</p>
''',
        r'''
<p>Ako su sva tri središta na osi $x$, dvije razlike čine linearan sustav po $(x,R)$, a $y$ slijedi iz $y^2=(R-d_a)^2-(x-x_a)^2$ (dva, jedno ili nijedno rješenje; degenerirani sustav daje $0$ ili beskonačno). Broj rješenja odlučuj egzaktno u cijelim brojevima (<code>__int128</code>), polumjer računaj u <code>long double</code>.</p>
''',
    ],
    'coach': [
        ('Kako prevesti „predznačenu udaljenost do kružnice” u jednadžbu?',
         r'''
<p>Za točku unutar kruga udaljenost do kružnice je $R-\rho$, gdje je $\rho$ udaljenost do središta; za točku izvan je $\rho-R$. Zadatak daje $d_i=R-\rho_i$ za unutrašnje i $d_i=-(\rho_i-R)=R-\rho_i$ za vanjske točke – ista formula! Dakle $\rho_i=R-d_i$, tj. $(x-x_i)^2+(y-y_i)^2=(R-d_i)^2$ uz uvjet $R-d_i\ge0$ za sve $i$, odnosno $R\ge M=\max d_i$ (za negativne $d_i$ to je automatski). Točka na kružnici ima $d_i=0$.</p>
'''),
        ('Zašto je sustav triju kvadratnih jednadžbi zapravo „gotovo linearan”?',
         r'''
<p>Sve tri jednadžbe imaju isti kvadratni dio $x^2+y^2-R^2$. Oduzmemo li jednadžbu za $A$ od one za $B$ i $C$, ostaju dvije linearne jednadžbe u $x,y,R$. Kod nas su $A$ i $B$ na osi $x$ pa $B-A$ ne sadrži $y$: $2(x_b-x_a)x=P_1+Q_1R$ daje $x$ kao linearnu funkciju od $R$ ($x_a\ne x_b$ jer su točke različite). $C-A$ glasi $2(x_c-x_a)x+2y_cy=K_2+Q_2R$.</p>
'''),
        ('Što kad središta nisu kolinearna?',
         r'''
<p>Ako $y_c\ne0$, iz $C-A$ dobivamo i $y$ kao linearnu funkciju od $R$. Uvrštavanjem $x=(X_0+X_1R)/D_2$, $y=(P_2+Q_2'R)/D_2$ u jednadžbu za $A$ i množenjem s $D_2^2$ dobivamo kvadratnu jednadžbu $aR^2+bR+c=0$ s <em>cjelobrojnim</em> koeficijentima (do $\sim10^{15}$, a diskriminanta do $\sim10^{30}$ – računamo u <code>__int128</code>). Svaki korijen $R\ge M$ daje točno jednu kružnicu. Slučajevi: $a=b=c=0$ – beskonačno (svaki $R$ radi); $a=b=0\ne c$ – nijedna; $a=0$ – linearna, jedan kandidat $R=-c/b$; inače diskriminanta $D=b^2-4ac$: $D\lt0$ nijedna, $D=0$ jedan, $D\gt0$ dva kandidata, od kojih brojimo one $\ge M$.</p>
'''),
        ('Kako egzaktno prebrojati korijene kvadratne jednadžbe koji su $\ge M$?',
         r'''
<p>Supstitucijom $S=R-M$ dobivamo $aS^2+b'S+c'=0$ s $b'=2aM+b$, $c'=aM^2+bM+c$; brojimo korijene $S\ge0$. Za $D\gt0$ korijeni su različiti, njihov umnožak je $c'/a$, a zbroj $-b'/a$: ako je umnožak $\lt0$, točno jedan je $\ge0$; ako je $0$, jedan je $0$ i drugi je $\ge0$ akko zbroj $\gt0$; ako je umnožak $\gt0$, oba su istog predznaka – oba $\ge0$ akko zbroj $\gt0$, inače nijedan. Sve su to samo predznaci cjelobrojnih izraza, bez pomičnog zareza. Najmanji korijen računamo stabilno u <code>long double</code> ($q=-(b\pm\sqrt D)/2$, korijeni $q/a$ i $c/q$).</p>
'''),
        ('Što kad su sva tri središta kolinearna ($y_c=0$)?',
         r'''
<p>Tada $C-A$ ne sadrži $y$, pa $B-A$ i $C-A$ čine linearan sustav po $(x,R)$. Ako je determinanta $\ne0$, dobivamo jedinstvene $x=X_n/\det$ i $R=R_n/\det$; treba $R\ge M$, a $y$ slijedi iz $y^2=(R-d_a)^2-(x-x_a)^2$: dva rješenja ($y=\pm$), jedno ($y=0$) ili nijedno. Ako je determinanta $0$, jednadžbe su ili nekonzistentne (nijedna kružnica) ili identične; tada za svaki $R\ge M$ postoji kružnica akko $G(R)=D_1^2(R-d_a)^2-(P_1+Q_1R-x_aD_1)^2\ge0$ – kvadratna nejednadžba: beskonačno mnogo rješenja ako je $G\gt0$ na nekom podintervalu $[M,\infty)$, jedno ako je $G\ge0$ samo u jednoj točki, inače nijedno. Odlučujemo po predznaku vodećeg koeficijenta, vrijednosti $G(M)$ i položaju vrha parabole u odnosu na $M$.</p>
'''),
        ('Koje numeričke i implementacijske zamke prijete?',
         r'''
<p>Koeficijenti su umnošci brojeva do $\sim10^4$–$10^6$, pa $b^2$ prelazi $10^{18}$ – nužan je <code>__int128</code>. Odluke „koliko rješenja” donosimo isključivo egzaktno; pomični zarez rabimo samo za ispis polumjera (relativna greška $10^{-6}$). $T$ do $2\cdot10^5$ – izlaz spremaj u međuspremnik. Ne zaboravi uvjet $R\ge M$: negativan ili premali $R$ nije kružnica (a pravac – „beskonačan polumjer” – nije dopušten).</p>
'''),
    ],
    'tips': [
        r'''<strong>Apolonijev problem algebarski:</strong> oduzimanjem jednadžbi kružnica kvadratni dio nestaje; dvije razlike izraze $x,y$ linearno kroz $R$, a povratno uvrštavanje daje kvadratnu jednadžbu po $R$.''',
        r'''Pri prebrojavanju rješenja geometrijskih zadataka s cjelobrojnim ulazom odluke donosi egzaktno (predznaci diskriminante, Vièteove formule u <code>__int128</code>), a pomični zarez koristi samo za konačni ispis.''',
        r'''Korijene kvadratne jednadžbe računaj stabilno: $q=-(b+\operatorname{sgn}(b)\sqrt D)/2$, pa $q/a$ i $c/q$ – izbjegava se oduzimanje bliskih brojeva.''',
        r'''Uvijek zasebno obradi degenerirane slučajeve (kolinearna središta, determinanta $0$, identične jednadžbe) – tu se skrivaju odgovori $0$ i $-1$.''',
    ],
    'solution': r'''
<p>Predznačena udaljenost $d_i$ znači $\rho_i=R-d_i$ za udaljenost $\rho_i$ točke do središta, u oba slučaja, pa tražimo $(x,y,R)$ s $(x-x_i)^2+(y-y_i)^2=(R-d_i)^2$ i $R\ge M=\max d_i$ – Apolonijev problem. Razlike jednadžbi su linearne u $x,y,R$. Ako $y_c\ne0$, iz $B-A$ i $C-A$ izrazimo $x$ i $y$ linearno kroz $R$, uvrstimo u jednadžbu za $A$ i dobijemo kvadratnu jednadžbu po $R$ s cjelobrojnim koeficijentima (<code>__int128</code>); broj korijena $\ge M$ odredimo egzaktno preko predznaka (supstitucija $S=R-M$, Vièteove formule), degenerirani slučajevi $a=0$ odnosno $a=b=c=0$ daju linearnu jednadžbu odnosno beskonačno rješenja. Ako $y_c=0$, razlike čine linearan sustav po $(x,R)$: regularan sustav daje $R$, a $y^2=(R-d_a)^2-(x-x_a)^2$ broj kružnica ($2$, $1$ ili $0$); singularan je nekonzistentan ($0$) ili identičan, kad kvadratna nejednadžba $G(R)\ge0$ na $[M,\infty)$ odlučuje između beskonačno, jedne i nijedne. Polumjer najmanje kružnice računamo u <code>long double</code>. $O(1)$ po testu. Ideja slijedi službeno rješenje izvornog zadatka (2017 Zhejiang Provincial Contest, SUA wiki) i analizu prihvaćenih predaja; implementacija (uključivo egzaktno prebrojavanje) napisana je iznova.</p>
''',
    'detailed': r'''
<h3>1. Prevod u jednadžbe</h3>
<p>Neka je tražena kružnica sa središtem $(x,y)$ i polumjerom $R\gt0$, a $\rho_i$ udaljenost točke $i$ do središta. Točka unutar kruga ima udaljenost do kružnice $R-\rho_i$, točka izvan $\rho_i-R$; sa zadanim predznakom obje daju $d_i=R-\rho_i$, a točka na kružnici $d_i=0$. Dakle
$$(x-x_i)^2+(y-y_i)^2=(R-d_i)^2,\qquad R\ge d_i\ (i\in\{a,b,c\}).$$
Uvjet $R\ge d_i$ bitan je za pozitivne $d_i$ (točka mora biti unutra) i skupno glasi $R\ge M=\max(d_a,d_b,d_c)\ge1$. Geometrijski: tražimo kružnicu koja dodiruje kružnice polumjera $|d_i|$ oko točaka – iznutra za $d_i\gt0$, izvana za $d_i\lt0$ – što je klasični Apolonijev problem.</p>
<h3>2. Linearizacija</h3>
<p>Sve tri jednadžbe imaju isti kvadratni dio $x^2+y^2-R^2$. $B-A$ (uz $y_a=y_b=0$):
$$2(x_b-x_a)\,x=\underbrace{x_b^2-x_a^2+d_a^2-d_b^2}_{P_1}+\underbrace{2(d_b-d_a)}_{Q_1}R\quad\Rightarrow\quad x=\frac{P_1+Q_1R}{D_1},\ D_1=2(x_b-x_a)\ne0.$$
$C-A$: $2(x_c-x_a)x+2y_cy=K_2+Q_2R$ s $K_2=x_c^2+y_c^2-x_a^2+d_a^2-d_c^2$, $Q_2=2(d_c-d_a)$.</p>
<h3>3. Nekolinearna središta ($y_c\ne0$)</h3>
<p>Uvrstimo $x$ u $C-A$: $y=\dfrac{P_2+Q_2'R}{D_2}$ s $D_2=2y_cD_1$, $P_2=-2(x_c-x_a)P_1+D_1K_2$, $Q_2'=-2(x_c-x_a)Q_1+D_1Q_2$. Također $x-x_a=\dfrac{X_0+X_1R}{D_2}$ s $X_0=2y_cP_1-x_aD_2$, $X_1=2y_cQ_1$. Jednadžba za $A$ pomnožena s $D_2^2$:
$$(X_0+X_1R)^2+(P_2+Q_2'R)^2=D_2^2(R-d_a)^2,$$
tj. $aR^2+bR+c=0$ s $a=X_1^2+Q_2'^2-D_2^2$, $b=2(X_0X_1+P_2Q_2'+D_2^2d_a)$, $c=X_0^2+P_2^2-D_2^2d_a^2$. Svaki korijen $R\ge M$ jednoznačno određuje $(x,y)$, pa je broj kružnica = broj takvih korijena.</p>
<ul>
<li>$a=b=c=0$: identitet – beskonačno mnogo kružnica, ispis $-1$.</li>
<li>$a=b=0$, $c\ne0$: nijedna.</li>
<li>$a=0$, $b\ne0$: $R=-c/b$; kružnica postoji akko $R\ge M$, što provjeravamo predznakom $(-c-bM)\cdot b\ge0$.</li>
<li>$a\ne0$: $D=b^2-4ac$. $D\lt0$: nijedna. Inače prebrojimo korijene $\ge M$ (točka 5).</li>
</ul>
<h3>4. Kolinearna središta ($y_c=0$)</h3>
<p>Tada $C-A$ glasi $E_1x=K_2+Q_2R$ s $E_1=2(x_c-x_a)\ne0$, pa $B-A$ i $C-A$ tvore sustav
$D_1x-Q_1R=P_1$, $E_1x-Q_2R=K_2$ s determinantom $\det=-D_1Q_2+Q_1E_1$.</p>
<ul>
<li>$\det\ne0$: $R=R_n/\det$, $x=X_n/\det$ (Cramer). Ako $R\lt M$: nijedna. Inače $y^2=(R-d_a)^2-(x-x_a)^2$; pomnoženo s $\det^2$ to je cjelobrojni izraz $u^2-v^2$ s $u=R_n-d_a\det$, $v=X_n-x_a\det$: $\gt0$ dvije kružnice (simetrične u odnosu na os), $=0$ jedna, $\lt0$ nijedna.</li>
<li>$\det=0$, sustav nekonzistentan ($D_1K_2-E_1P_1\ne0$): nijedna.</li>
<li>$\det=0$ i jednadžbe identične: $x=(P_1+Q_1R)/D_1$ za svaki $R$, a kružnica postoji akko $y^2\ge0$, tj. $G(R)=D_1^2(R-d_a)^2-(P_1+Q_1R-x_aD_1)^2\ge0$, uz $R\ge M$. $G$ je kvadratna (ili degenerirana) funkcija s cjelobrojnim koeficijentima $\alpha,\beta,\gamma$. Ako je $G\gt0$ na nekom intervalu unutar $[M,\infty)$, kružnica je beskonačno; ako je $G\ge0$ na $[M,\infty)$ samo u jednoj točki, jedna (polumjer je ta točka); inače nijedna. Odlučujemo po slučajevima: $\alpha\gt0$ ili ($\alpha=0$, $\beta\gt0$) – beskonačno; $\alpha=\beta=0$ – konstanta ($\gamma\gt0$ beskonačno, $\gamma=0$ beskonačno, $\gamma\lt0$ nijedna); $\alpha=0$, $\beta\lt0$ – $G\ge0$ lijevo od korijena $r_0$: beskonačno ako $r_0\gt M$, jedna ($R=M$) ako $r_0=M$, nijedna inače; $\alpha\lt0$ – $G\ge0$ između korijena: uz $D\gt0$ usporedimo $G(M)$ i položaj vrha $-\beta/(2\alpha)$ prema $M$ (ako $G(M)\gt0$ ili je $M$ lijevo od većeg korijena – beskonačno; ako je $M$ upravo veći korijen – jedna), uz $D=0$ jedna ako je dvostruki korijen $\ge M$, uz $D\lt0$ nijedna.</li>
</ul>
<h3>5. Egzaktno prebrojavanje korijena $\ge M$</h3>
<p>Za $aR^2+bR+c=0$ s $D\ge0$ supstituiramo $S=R-M$: $aS^2+b'S+c'=0$, $b'=2aM+b$, $c'=aM^2+bM+c$. Za $D=0$ jedini korijen $S=-b'/(2a)$ je $\ge0$ akko $\operatorname{sgn}(-b')\operatorname{sgn}(a)\ge0$. Za $D\gt0$ korijeni $S_1\ne S_2$ imaju umnožak $c'/a$ i zbroj $-b'/a$: umnožak $\lt0$ – točno jedan nenegativan; umnožak $=0$ – jedan je nula, drugi nenegativan akko zbroj $\gt0$; umnožak $\gt0$ – oba nenegativna akko zbroj $\gt0$, inače nijedan. Sve su to predznaci cjelobrojnih izraza u <code>__int128</code> (koeficijenti su do $\sim10^{15}$, $b^2$ do $\sim10^{30}$, pa 64 bita ne dostaju).</p>
<h3>6. Polumjer najmanje kružnice</h3>
<p>Korijene računamo stabilno: $q=-(b+\operatorname{sgn}(b)\sqrt D)/2$, $R_1=q/a$, $R_2=c/q$. Ako su dva korijena $\ge M$, uzmemo manji; ako je samo jedan, to je veći od dvaju. U kolinearnom slučaju $R=R_n/\det$, u degeneriranom „jedna kružnica” $R=M$ ili dvostruki korijen $-\beta/(2\alpha)$. Ispis s 12 decimala u <code>long double</code>; zadatak jamči da je najmanji polumjer $\le10^4$, pa je relativna greška zanemariva.</p>
<h3>7. Složenost i zamke</h3>
<p>$O(1)$ po testu, $T\le2\cdot10^5$ – izlaz skupljamo u string. Zamke: zaboravljen uvjet $R\ge M$ (npr. korijen $R$ manji od $d_a$ ne odgovara točki unutar kruga); miješanje predznaka pri prelasku na $S=R-M$ kad je $a\lt0$; slučaj $\det=0$ s identičnim jednadžbama daje odgovore $-1$; „pravac” (beskonačan $R$) se ne broji, što je u algebri automatski jer brojimo samo konačne korijene.</p>
<h3>8. Primjer</h3>
<p>$A=(0,0),d_a=1$; $B=(3,0),d_b=2$; $C=(10,2),d_c=2$: kružnica prolazi unutar-unutar-unutar, $M=2$. $B-A$: $6x=9+1-4+2R=6+2R$, dakle $x=1+R/3$. $C-A$: $20x+4y=104+1-4+2R$, pa $y=(101+2R-20x)/4=(81-14R/3)/4$. Uvrštavanje u $x^2+y^2=(R-1)^2$ daje kvadratnu jednadžbu s dva korijena $\ge2$; manji je $R\approx10.3273$. S $d_c=-2$ ($C$ izvana) predznak $Q_2$ se mijenja i manji korijen je $R\approx5.3417$.</p>
''',
    'verified': r'''uzorci 2/2; 300 slučajnih testova (koordinate i udaljenosti u malom rasponu, uključivo kolinearne i degenerirane konfiguracije) protiv neovisnog Python referentnog rješenja s <code>Fraction</code> aritmetikom i <code>check.py</code> koji uspoređuje $-1$/$0$ egzaktno, a polumjer s relativnom tolerancijom $10^{-6}$; 3 velika testa ($T=2\cdot10^5$), najsporiji $0.08$ s.''',
},
# ---------------------------------------------------------------- L
{
    'letter': 'L', 'title': 'New Houses', 'title_hr': 'Nove kuće', 'slug': 'L_new_houses',
    'tl': '1 s', 'ml': '1024 MiB',
    'statement': r'''
<p>$n$ ljudi useljava u $m$ kuća u nizu ($n \le m$), najviše jedna osoba po kući; kuće $u$ i $v$ su susjedne ako $|u - v| = 1$. Sreća $i$-te osobe je $a_i$ ako ima barem jednog susjeda, a $b_i$ ako nema nijednog. Maksimiziraj ukupnu sreću.</p>
<h3>Ulaz</h3>
<p>$T$ testova; $1 \le n \le 5 \cdot 10^5$, $n \le m \le 10^9$, $1 \le a_i, b_i \le 10^9$; $\sum n \le 10^6$.</p>
<h3>Izlaz</h3>
<p>Za svaki test najveća ukupna sreća.</p>
<h3>Primjer</h3>
<p>$m = 5$, $(a, b) = (1, 100), (100, 1), (100, 1), (100, 1)$: $400$. $m = 2$, $(1, 10), (1, 10)$: $2$. $m = 3$, $(100, 50), (1, 1000)$: $1050$.</p>
''',
    'hints': [
        r'''
<p>Jedino što o rasporedu treba znati jest <em>koji</em> ljudi imaju susjeda. Koliko najmanje kuća treba ako točno $k$ ljudi ima susjeda, a $n-k$ ih je izolirano?</p>
''',
        r'''
<p>Sve ljude sa susjedima stavi u jedan blok; svaki izolirani treba jednu praznu kuću uz sebe. Dobiješ $2n-k$ kuća za $k\ge 2$ i $2n-1$ za $k=0$ ($k=1$ je nemoguć).</p>
''',
        r'''
<p>Za fiksni $k$ susjeda odaberi $k$ ljudi s najvećim $a_i - b_i$; isprobaj sve dopuštene $k$ uz sortirani niz razlika i prefiksne sume.</p>
''',
    ],
    'coach': [
        ('Što je jedina informacija koja određuje ukupnu sreću?',
         r'''
<p>Sreća osobe ovisi samo o tome ima li barem jednog susjeda. Dakle raspored je važan jedino kroz skup $S$ ljudi sa susjedima; ukupna sreća je $\sum_{i\in S} a_i + \sum_{i\notin S} b_i = \sum_i b_i + \sum_{i\in S}(a_i-b_i)$.</p>
'''),
        ('Koji skupovi $S$ su ostvarivi u $m$ kuća?',
         r'''
<p>Neka je $|S|=k$. Skup $S$ s $k=1$ je nemoguć (susjedstvo je simetrično). Za $k\ge 2$ najštedljiviji raspored stavi svih $k$ u jedan blok uzastopnih kuća, a svaku od $n-k$ izoliranih osoba odvoji jednom praznom kućom: ukupno $k + 2(n-k) = 2n-k$ kuća. Manje nije moguće: zauzete kuće čine barem $(n-k)+1$ komponenata (svaki izolirani je svoja komponenta, plus barem jedna za $S$), a između uzastopnih komponenata je barem jedna prazna kuća, pa treba $\ge n + (n-k) = 2n-k$ kuća. Za $k=0$ ista računica daje $2n-1$. Ostvarivo je dakle točno: $k=0$ ako $2n-1\le m$, te svaki $k\ge 2$ s $2n-k\le m$ – uočimo da $k=n$ uvijek vrijedi jer $m\ge n$.</p>
'''),
        ('Za fiksni $k$, koje ljude staviti u $S$?',
         r'''
<p>Sreća je $\sum b_i + \sum_{i\in S}(a_i-b_i)$, a ostvarivost ovisi samo o $|S|$, ne o tome tko je u $S$. Zato za fiksni $k$ uzmemo $k$ najvećih razlika $d_i=a_i-b_i$ (moguće i negativnih – tada je manji $k$ vjerojatno bolji, ali možda nije dopušten).</p>
'''),
        ('Kako sve to izračunati u $O(n\log n)$?',
         r'''
<p>Sortiraj $d_i$ silazno, računaj prefiksne sume $D_k$; odgovor je $\max$ od $\sum b_i$ (ako $2n-1\le m$) i $\sum b_i + D_k$ po svim $k\ge 2$ s $k \ge 2n-m$. Vrijednosti do $5\cdot 10^5\cdot 10^9$ zahtijevaju 64-bitne cijele brojeve.</p>
'''),
    ],
    'tips': [
        r'''<strong>Odvoji „tko” od „koliko”:</strong> kad izvedivost ovisi samo o veličini skupa, a cilj je zbroj po skupu, optimum za svaku veličinu daju najveći pojedinačni doprinosi – sortiraj i koristi prefiksne sume.''',
        r'''Donje granice na broj kuća/mjesta dokazuj brojanjem komponenata i obveznih razmaka između njih – to je standardni argument za „pakiranje na pravac”.''',
        r'''Provjeri degenerirane veličine: $k=1$ ovdje ne postoji, a $k=0$ ima drukčiju formulu ($2n-1$).''',
    ],
    'solution': r'''
<p>Sreća ovisi samo o skupu $S$ ljudi koji imaju susjeda: iznosi $\sum_i b_i + \sum_{i\in S}(a_i-b_i)$. Skup s $|S|=k$ ostvariv je akko je $k=0$ i $2n-1\le m$, ili $k\ge2$ i $2n-k\le m$ (susjede stavimo u jedan blok, izolirane odvojimo praznim kućama; brojanje komponenata pokazuje da manje kuća ne dostaje). Za fiksni $k$ optimalno je uzeti $k$ najvećih razlika $a_i-b_i$; sortiramo razlike, računamo prefiksne sume i uzmemo maksimum po svim dopuštenim $k$. Složenost $O(n\log n)$. Ideja slijedi službeno rješenje GDCPC-a 2023 i analizu prihvaćenih predaja; implementacija je napisana iznova.</p>
''',
    'detailed': r'''
<h3>1. Što određuje rezultat</h3>
<p>Osoba $i$ doprinosi $a_i$ ako ima barem jednog susjeda, inače $b_i$. Neka je $S$ skup osoba sa susjedom. Ukupna sreća je
$$\sum_{i\in S}a_i + \sum_{i\notin S}b_i = \sum_{i=1}^n b_i + \sum_{i\in S}(a_i-b_i).$$
Raspored kuća utječe samo na to koji je $S$ ostvariv.</p>
<h3>2. Koje veličine $|S|$ su ostvarive</h3>
<p>Neka je $k=|S|$. Ako netko ima susjeda, i taj susjed ima susjeda, pa je $k\ne 1$.</p>
<p><strong>Gornja konstrukcija.</strong> Za $k\ge 2$: postavimo svih $k$ ljudi iz $S$ u kuće $1,\dots,k$ (svaki ima susjeda), zatim naizmjence praznu kuću i izoliranu osobu: kuće $k+2, k+4, \dots$. Ukupno zauzimamo $k + 2(n-k) = 2n-k$ kuća. Za $k=0$: osobe u kućama $1,3,5,\dots$, ukupno $2n-1$ kuća.</p>
<p><strong>Donja granica.</strong> Promotrimo maksimalne blokove uzastopno zauzetih kuća (komponente). Svaka izolirana osoba je komponenta veličine $1$, a osobe iz $S$ leže u komponentama veličine $\ge 2$; ako je $k\ge 2$, postoji barem jedna takva. Dakle komponenata je barem $(n-k)+1$ za $k\ge2$, odnosno $n$ za $k=0$. Između dviju uzastopnih komponenata je barem jedna prazna kuća, pa je potrebno barem $n + (n-k+1) - 1 = 2n-k$ kuća (za $k=0$: $n + n - 1 = 2n-1$). Konstrukcija je dakle optimalna.</p>
<p>Zaključak: skup veličine $k$ je ostvariv akko ($k=0$ i $2n-1\le m$) ili ($k\ge2$ i $2n-k\le m$). Kako je $m\ge n$, $k=n$ je uvijek ostvariv, pa rješenje postoji.</p>
<h3>3. Izbor ljudi za fiksni $k$</h3>
<p>Ostvarivost ovisi samo o $k$, a cilj je $\sum b_i + \sum_{i\in S}(a_i-b_i)$. Za fiksni $k$ maksimum se postiže odabirom $k$ najvećih razlika $d_i=a_i-b_i$ (zamjenom bilo kojeg člana $S$ nekim s većom razlikom zbroj ne pada). Neka je $d$ sortiran silazno i $D_k=\sum_{j\le k} d_j$ (prefiksne sume, $D_0=0$).</p>
<h3>4. Algoritam</h3>
<ol>
<li>Pročitaj parove, izračunaj $B=\sum b_i$ i razlike $d_i$.</li>
<li>Sortiraj $d$ silazno i računaj prefiksne sume.</li>
<li>$\text{best} = B$ ako $2n-1\le m$; za svaki $k$ od $2$ do $n$ s $2n-k\le m$ ažuriraj $\text{best}=\max(\text{best}, B+D_k)$.</li>
<li>Ispiši $\text{best}$.</li>
</ol>
<p>Nije dovoljno uzeti samo najmanji dopušteni $k$: razlike mogu biti pozitivne, pa veći $k$ može biti bolji; nije dovoljno ni uzeti sve pozitivne razlike, jer njihov broj može biti $1$ ili premali za $m$. Zato prolazimo sve dopuštene $k$.</p>
<h3>5. Složenost i zamke</h3>
<p>$O(n\log n)$ po testu zbog sortiranja; $\sum n\le 10^6$. Zbrojevi dosežu $5\cdot10^5\cdot10^9 = 5\cdot 10^{14}$ – obvezno <code>long long</code>; $m$ do $10^9$ također ne smije biti množen u 32 bita ($2n$ stane, ali računaj u 64 bita radi sigurnosti).</p>
<h3>6. Primjeri</h3>
<p>$m=5$, $(1,100),(100,1),(100,1),(100,1)$: $B=103$, $d=(99,99,99,-99)$. $k=0$ zahtijeva $7\le5$ – ne; $k=2$: $6\le5$ – ne; $k=3$: $5\le5$, $103+297=400$; $k=4$: $103+198=301$. Odgovor $400$. Drugi primjer $m=2$, $(1,10),(1,10)$: samo $k=2$ je dopušten ($2n-1=3>2$), rezultat $2$.</p>
''',
    'verified': r'''uzorci 3/3; 300 slučajnih testova ($n\le 6$, $m\le 12$) protiv brute forcea koji nabraja sve rasporede ljudi po kućama; 3 velika testa ($n=5\cdot10^5$, $m$ do $10^9$), najsporiji $0.15$ s.''',
},
# ---------------------------------------------------------------- M
{
    'letter': 'M', 'title': 'Canvas', 'title_hr': 'Platno', 'slug': 'M_canvas',
    'tl': '3 s', 'ml': '1024 MiB',
    'statement': r'''
<p>Niz duljine $n$ početno je sav nula. $i$-ta od $m$ operacija postavlja $l_i$-ti element na $x_i$ i $r_i$-ti element na $y_i$ ($l_i \lt r_i$, $x_i, y_i \in \{1, 2\}$). Svaka se operacija izvodi točno jednom. Nađi redoslijed koji maksimizira konačni zbroj niza.</p>
<h3>Ulaz</h3>
<p>$T$ testova; $2 \le n, m \le 5 \cdot 10^5$, zatim $m$ četvorki $l_i, x_i, r_i, y_i$; $\sum n, \sum m \le 5 \cdot 10^5$.</p>
<h3>Izlaz</h3>
<p>Za svaki test najveći zbroj i u sljedećem retku permutaciju indeksa operacija (bilo koju optimalnu).</p>
<h3>Primjer</h3>
<p>$n = 4$, operacije $(1,1,2,2), (3,2,4,1), (1,2,3,2), (2,1,4,1)$: $7$, redoslijed <code>4 1 3 2</code> daje $\{2, 2, 2, 1\}$. $n = 4$, operacije $(3,2,4,1), (1,2,3,1)$: $5$, <code>2 1</code>.</p>
''',
    'hints': [
        r'''
<p>Konačnu vrijednost pozicije određuje <em>posljednja</em> operacija koja je dotakne. Gledaj redoslijed unatrag: prva operacija (u obrnutom vremenu) koja dotakne poziciju odlučuje. Gdje očito idu operacije $(2,2)$, a gdje $(1,1)$?</p>
''',
        r'''
<p>Miješana operacija (jedan kraj dobiva $1$, drugi $2$) je usmjereni brid $u\to v$ od kraja koji dobiva $1$ prema kraju koji dobiva $2$. Ako DFS iz vrha $s$ „ispisuje” bridove redom obilaska (u obrnutom vremenu), svi dosegnuti vrhovi osim $s$ dobivaju $2$.</p>
''',
        r'''
<p>Koliko najmanje vrhova mora dobiti $1$? Barem jedan po svakoj izvorišnoj jako povezanoj komponenti bez vrha „zaključanog” operacijom $(2,2)$. Kreni DFS-ove iz zaključanih vrhova, a zatim iz nepohođenih vrhova po padajućem vremenu završetka (Kosarajuov poredak) – bez eksplicitnog računanja SCC-ova.</p>
''',
    ],
    'coach': [
        ('Što određuje konačnu vrijednost pojedine pozicije?',
         r'''
<p>Samo posljednja operacija koja piše na tu poziciju; ranije su prebrisane. Zato je prirodno gledati redoslijed <em>obrnuto</em>: u obrnutom vremenu prva operacija koja dotakne poziciju „zaključava” njezinu vrijednost. Nedotaknute pozicije ostaju $0$, dotaknute su $1$ ili $2$; zbroj je (broj dotaknutih) $+$ (broj pozicija s $2$), pa maksimiziramo broj dvojki.</p>
'''),
        ('Gdje u redoslijedu idu operacije $(2,2)$ i $(1,1)$ i zašto to nikad ne šteti?',
         r'''
<p>Operacija $(2,2)$ daje objema pozicijama najveću moguću vrijednost; premjestimo li je na sam kraj (prvu u obrnutom vremenu), njezine pozicije postaju $2$, a ostale se ne mijenjaju – zbroj se ne smanjuje. Operacija $(1,1)$ piše samo jedinice; premjestimo li je na sam početak, sve što je dotakla dobiva vrijednost od kasnijih operacija (barem $1$ ako ih ima), inače ostaje $1$ – opet bez gubitka. Pozicije dotaknute nekom $(2,2)$ zovemo <em>zaključanima</em>: one su $2$ bez obzira na ostalo.</p>
'''),
        ('Kako modelirati miješane operacije?',
         r'''
<p>Operacija koja poziciji $u$ daje $1$, a $v$ daje $2$ je usmjereni brid $u\to v$. U obrnutom vremenu, kad brid obradimo: $v$ dobiva $2$ ako još nije dotaknut, $u$ dobiva $1$ ako još nije dotaknut. Vrh koji je prvi put dotaknut kao <em>glava</em> nekog brida postaje $2$; vrh prvi put dotaknut kao <em>rep</em> postaje $1$. Želimo da što više vrhova bude prvi put dotaknuto kao glava.</p>
'''),
        ('Zašto DFS daje dobar redoslijed bridova?',
         r'''
<p>Pokrenimo DFS iz $s$ i zapisujmo bridove redom kojim ih istražujemo (uključivo one prema već posjećenima). Svaki brid $v\to z$ istražujemo iz vrha $v$ koji je ili $s$ ili je već dosegnut nekim bridom u kojem je bio glava – dakle $v$ je već $2$ (ili je $s$). Vrh $z$, ako je nov, prvi je put dotaknut kao glava: dobiva $2$. Dakle svi vrhovi dosegnuti iz $s$ dobivaju $2$, a samo $s$ dobiva $1$ (osim ako je zaključan ili već dosegnut ranije).</p>
'''),
        ('Koja je donja ograda na broj jedinica i kako je dostići?',
         r'''
<p>Neka je $S$ izvorišna jako povezana komponenta grafa bridova (nijedan brid ne ulazi u $S$) koja nema zaključanih vrhova i ima barem jedan brid s repom u $S$. U bilo kojem redoslijedu promotrimo prvi (u obrnutom vremenu) brid s repom $u\in S$: svi raniji bridovi imaju rep izvan $S$, pa i glavu izvan $S$ (ništa ne ulazi u $S$), dakle $u$ još nije dotaknut i dobiva $1$. Svaka takva komponenta daje barem jednu jedinicu. Dostižnost: prvo DFS-ovi iz zaključanih vrhova (korijen je $2$, sve dosegnuto $2$), zatim iz preostalih nepohođenih vrhova – ako svaki novi korijen leži u izvorišnoj SCC preostalog grafa, jedinice dobivaju točno korijeni, po jedan po takvoj komponenti. Preostali skup je „zatvoren prema unatrag” (uklonjeno je sve dohvatljivo iz posjećenih), pa su izvorišne SCC preostalog grafa ujedno izvorišne SCC cijelog grafa bez zaključanih vrhova.</p>
'''),
        ('Kako pronaći vrh u izvorišnoj komponenti bez računanja SCC-ova?',
         r'''
<p>Kosarajuova lema: nakon DFS-a cijelog grafa, ako brid vodi iz komponente $C$ u $C'$, najveće vrijeme završetka u $C$ veće je od najvećeg u $C'$. Zato nepohođeni vrh s najvećim vremenom završetka leži u izvorišnoj SCC preostalog grafa. Dovoljan je dakle jedan DFS za vremena završetka i zatim DFS-ovi po padajućem vremenu, oba iterativno (dubina do $5\cdot10^5$). Ukupno $O(n+m)$.</p>
'''),
    ],
    'tips': [
        r'''<strong>„Zadnje pisanje pobjeđuje”</strong> – gledaj proces obrnuto u vremenu, gdje prvo pisanje odlučuje; to pretvara pitanje redoslijeda u pitanje pokrivanja/dohvatljivosti.''',
        r'''Operacije koje su dominantno dobre ili dominantno loše (ovdje $(2,2)$ i $(1,1)$) izdvoji zamjenskim argumentom na krajeve redoslijeda; ostatak modeliraj grafom.''',
        r'''Poredak završetka DFS-a (Kosaraju) daje vrh u izvorišnoj SCC preostalog grafa – često zamjenjuje eksplicitnu kondenzaciju grafa.''',
        r'''Za konstruktivne zadatke s više optimalnih rješenja piši <code>check.py</code> koji simulira ispisani redoslijed i uspoređuje samo optimalnu vrijednost s brute forceom.''',
    ],
    'solution': r'''
<p>Konačnu vrijednost pozicije određuje posljednja operacija koja je dotakne, pa gledamo redoslijed unatrag. Operacije $(2,2)$ stavljamo na kraj (u obrnutom vremenu prve) – njihove pozicije su „zaključane” na $2$; operacije $(1,1)$ na početak. Miješana operacija je brid $u\to v$ od pozicije koja dobiva $1$ do one koja dobiva $2$; u obrnutom vremenu vrh prvi put dotaknut kao glava postaje $2$, kao rep $1$. DFS iz $s$ koji ispisuje bridove redom obilaska daje svim dosegnutim vrhovima $2$, a samo $s$ dobiva $1$. Donja ograda: svaka izvorišna SCC bez zaključanog vrha (s barem jednim bridom) daje barem jednu jedinicu. Dostižemo je DFS-ovima iz zaključanih vrhova, a zatim iz nepohođenih vrhova po padajućem vremenu završetka (Kosarajuov poredak jamči da je korijen u izvorišnoj SCC preostalog grafa). Stvarni redoslijed: $(1,1)$, miješane u obratu DFS-ispisa, $(2,2)$. Sve iterativno, $O(n+m)$. Ideja slijedi službeno rješenje GDCPC-a 2023 (SUA wiki) i analizu prihvaćenih predaja; implementacija je napisana iznova.</p>
''',
    'detailed': r'''
<h3>1. Obrnuto vrijeme</h3>
<p>Pozicija $p$ na kraju ima vrijednost koju je upisala <em>posljednja</em> operacija koja ju je dotakla, ili $0$ ako je nedotaknuta. Fiksirajmo redoslijed $\pi$ i čitajmo ga unatrag: prva operacija u obrnutom čitanju koja dotakne $p$ određuje joj vrijednost. Skup dotaknutih pozicija $D$ ne ovisi o redoslijedu; zbroj je $|D|+\#\{p\in D: a_p=2\}$. Treba dakle maksimizirati broj dvojki, odnosno minimizirati broj jedinica.</p>
<h3>2. Operacije $(2,2)$ i $(1,1)$</h3>
<p><em>Tvrdnja 1.</em> Postoji optimalan redoslijed u kojem su sve operacije $(2,2)$ na kraju, a sve $(1,1)$ na početku.<br>
<em>Dokaz.</em> Uzmimo bilo koji redoslijed i premjestimo jednu $(2,2)$ operaciju na sam kraj. Njezine dvije pozicije postaju $2$ (maksimum), a nijedna druga pozicija ne mijenja svoju posljednju operaciju – zbroj se ne smanjuje. Premjestimo li $(1,1)$ na početak, njezine pozicije dobivaju vrijednost sljedeće operacije koja ih dotiče (u $\{1,2\}$, dakle $\ge1$) ili ostaju $1$ ako takve nema – opet bez smanjenja; ostale pozicije nepromijenjene. Ponavljanjem dobivamo traženi oblik. $\square$</p>
<p>Pozicije dotaknute barem jednom $(2,2)$ operacijom zovemo <em>zaključanima</em> ($\text{locked}$): u obrnutom vremenu one su prve dobile $2$. Pozicije dotaknute samo $(1,1)$ operacijama nužno su $1$.</p>
<h3>3. Graf miješanih operacija</h3>
<p>Miješana operacija koja poziciji $u$ daje $1$ i poziciji $v$ daje $2$ (bilo $x_i=1,y_i=2$ pa $u=l_i,v=r_i$, bilo obrnuto) je usmjereni brid $u\to v$. U obrnutom vremenu, nakon svih $(2,2)$, obrađujemo bridove u nekom poretku; vrh koji je prvi put dotaknut kao glava dobiva $2$, kao rep $1$; zaključani vrhovi ostaju $2$. Neka je $V'$ skup nezaključanih vrhova koji su krajevi barem jednog brida. Broj jedinica je broj vrhova iz $V'$ koji su prvi put dotaknuti kao rep.</p>
<h3>4. Donja ograda</h3>
<p><em>Tvrdnja 2.</em> Neka je $S$ jako povezana komponenta grafa bridova bez ulaznih bridova iz drugih komponenata (izvorišna SCC), bez zaključanih vrhova, koja sadrži rep barem jednog brida. Tada u svakom poretku bridova barem jedan vrh iz $S$ dobiva $1$.<br>
<em>Dokaz.</em> Promotrimo prvi brid u poretku čiji je rep $u\in S$. Svi raniji bridovi imaju rep izvan $S$; kako u $S$ ne ulazi nijedan brid, imaju i glavu izvan $S$. Dakle $u$ nije dotaknut ranije, nije zaključan, pa dobiva $1$. $\square$</p>
<p>Označimo $\sigma$ broj takvih komponenata. Broj jedinica je $\ge\sigma$.</p>
<h3>5. Konstrukcija koja dostiže $\sigma$</h3>
<p><em>Lema (DFS-ispis).</em> Pokrenimo DFS iz vrha $s$ nad nepohođenim vrhovima i zapisujmo svaki brid $v\to z$ u trenutku kad ga istražimo (i kad $z$ već jest posjećen). Ako bridove obradimo u tom poretku, svi vrhovi dosegnuti u ovom DFS-u osim $s$ dobivaju $2$; $s$ dobiva $1$ ako ranije nije dotaknut ni zaključan.<br>
<em>Dokaz.</em> Indukcijom po poretku: brid $v\to z$ istražujemo iz $v$ koji je ili $s$ ili je u ovaj DFS ušao kao glava nekog ranije zapisanog brida (tada je već $2$). Ako je $z$ nov, prvi je put dotaknut kao glava – dobiva $2$; ako nije nov, već ima vrijednost. $\square$</p>
<p>Algoritam: (a) DFS cijelog grafa radi vremena završetka; (b) DFS-ispis iz svakog zaključanog nepohođenog vrha – korijeni su $2$, sve dosegnuto je $2$; (c) dok postoji nepohođen vrh, DFS-ispis iz nepohođenog vrha $r$ s najvećim vremenom završetka.</p>
<p><em>Zašto je $r$ u izvorišnoj SCC bez zaključanih vrhova?</em> Kosarajuova lema: ako postoji brid iz komponente $C$ u komponentu $C'\ne C$, tada je $\max_{C}\text{fin}\gt\max_{C'}\text{fin}$. Skup posjećenih vrhova $P$ nakon svakog DFS-a zatvoren je prema dohvatljivosti (iz $P$ ne izlazi brid u nepohođen vrh), pa su SCC-ovi grafa induciranog na $V\setminus P$ upravo SCC-ovi cijelog grafa koji leže u $V\setminus P$, s istim bridovima među njima, a u njih ne ulazi nijedan brid iz $P$. Vrh $r$ s najvećim vremenom završetka u $V\setminus P$ stoga leži u komponenti bez ulaznih bridova iz $V\setminus P$, dakle i bez ulaznih bridova uopće – izvorišnoj SCC cijelog grafa. Zaključani vrhovi su svi posjećeni u (b), pa ih ta komponenta nema. Ako $r$ nema izlaznih bridova, DFS ništa ne zapiše: takav $r$ nema ni ulaznih bridova (iz $P$ ne izlaze bridovi u $V\setminus P$, a brid $x\to r$ s $x\in V\setminus P$ značio bi da su $x$ i $r$ u istoj izvorišnoj SCC, pa bi $r$ imao izlazni brid), dakle $r$ je izoliran i nije u $V'$. Inače korijen $r$ dobiva $1$, i to je jedina jedinica njegove komponente. Svaki korijen iz (c) leži u drugoj izvorišnoj komponenti (nakon DFS-a cijela je komponenta posjećena), pa je broj jedinica točno $\sigma$. $\square$</p>
<h3>6. Sastavljanje odgovora</h3>
<p>Poredak bridova iz (b) i (c) je u obrnutom vremenu; stvarni redoslijed je: sve $(1,1)$ operacije, zatim miješane u <em>obratu</em> zapisanog poretka, zatim sve $(2,2)$. Zbroj računamo simulacijom (ili kao $|D|+\#\text{dvojki}$). Redoslijed nije jedinstven – zadatak prihvaća bilo koji optimalan.</p>
<h3>7. Složenost i zamke</h3>
<p>Dva DFS-a i simulacija: $O(n+m)$ po testu, ukupno $O(\sum n+\sum m)$. DFS mora biti iterativan (lanci duljine $5\cdot10^5$ ruše rekurziju). Bridovi prema već posjećenim vrhovima također se zapisuju – svaka operacija mora se pojaviti točno jednom. Zbroj do $2n\le10^6$ stane u <code>int</code>, ali izlaz treba skupljati u međuspremnik ($\sum m$ brojeva). Paziti na smjer brida: rep je kraj koji dobiva $1$.</p>
<h3>8. Primjer</h3>
<p>Prvi primjer: op. 1 $(1,1,2,2)$ je brid $1\to2$; op. 2 $(3,2,4,1)$ je brid $4\to3$; op. 3 $(1,2,3,2)$ zaključava $1$ i $3$; op. 4 $(2,1,4,1)$ je $(1,1)$. DFS-ispis iz zaključanog $1$: brid $1\to2$ (op. 1); iz $3$: ništa. Nepohođen ostaje $4$: brid $4\to3$ (op. 2). Zapisani poredak (obrnuto vrijeme): op. 1, op. 2. Stvarni redoslijed: op. 4, op. 2, op. 1, op. 3 – simulacija daje $(2,2,2,1)$, zbroj $7$; pozicija $4$ nužno je $1$ (izvorišna SCC $\{4\}$).</p>
''',
    'verified': r'''uzorak 1/1 (oba primjera iz teksta); 300 slučajnih testova (do 4 slučaja po ulazu, $n,m\le 6$) protiv brute forcea koji ispituje sve permutacije operacija, uz <code>check.py</code> koji provjerava da je ispis permutacija, simulira ga i uspoređuje zbroj s optimumom; 3 velika testa ($n=m=5\cdot10^5$: slučajni, lančasti/dubinski i lokalni bridovi), najsporiji $0.12$ s.''',
},
]
