"""1st Universal Cup – Stage 10: Zhejiang. Uvezeno iz ručno pisanih stranica (import_legacy.py); naputci i
trenerski koraci iz nekadašnjeg retro_stage10.py."""

STAGE = {
    'no': 10,
    'name': 'Stage 10: Zhejiang',
    'source_name': '1st OCPC, Winter 2023, Day 6: Yuhao Du Contest 11',
    'source_html': r'''
<p>Prijevod službenog rješenja autora Yuhaa Dua: <a href="https://contest.ucup.ac/download.php?type=attachments&amp;id=1195&amp;r=1">Tutorial (en)</a>. Tekst zadatka preveden je prema službenim <a href="https://contest.ucup.ac/download.php?type=attachments&amp;id=1195&amp;r=0">engleskim tekstovima zadataka</a>. Zadatak je dostupan na <a href="https://contest.ucup.ac/contest/1195">Universal Cup Judging System</a>.</p>
''',
}

PROBLEMS = [
{
    'letter': 'A',
    'title': 'Atcoder Problem',
    'title_hr': 'Atcoder zadatak',
    'slug': 'A_atcoder_problem',
    'tl': '4 s',
    'ml': '1024 MB',
    'statement': r'''
<p>Ispiši broj, modulo $998244353$, cjelobrojnih nizova $A = (A_1, \dots, A_N)$ duljine $N$ takvih da $0 \le A_1 \le A_2 \le \dots \le A_N \le M$ i $A_1 \oplus A_2 \oplus \dots \oplus A_N = X$. Zadatak je prelagan, pa ispiši odgovor za svaki $N = 1, 2, \dots, N_{MAX}$.</p>
<h3>Ulaz</h3>
<p>$N_{MAX}, M, X$ ($1 \le N_{MAX} \le 10^5$, $0 \le M, X &lt; 2^{60}$).</p>
<h3>Izlaz</h3>
<p>$N_{MAX}$ redaka — odgovori za $N = 1, \dots, N_{MAX}$.</p>
''',
    'hints': [
        r'''
<p>Nepadajući niz = multiskup; broj multiskupova s XOR-om $X$ preko Burnsideove leme iz broja <em>uređenih</em> nizova $f_n$: permutacija s $p$ parnih i $q$ neparnih ciklusa fiksira $f_q (M+1)^p$ rješenja.</p>
''',
        r'''
<p>Uređeni slučaj: multiskup XOR-ova $i$ brojeva iz $[0,M]$ ima strukturu „$O(\log M)$ blokova oblika (visoki bitovi fiksni, niski uniformni)” — konvolucija s $[0,M]$ u $O(\log M)$ po koraku. Parni i neparni ciklusi razdvajaju se: EGF parnih je $\exp$ nečeg jednostavnog, neparni traže kompoziciju $F(\mathrm{ODD}(x))$ preko transponiranog algoritma u $O(n\log^2 n)$.</p>
''',
    ],
    'coach': [
        ('Opažanje 1: skini uređenje Burnsideom',
         r'''
<p>Nepadajući nizovi $\leftrightarrow$ orbite djelovanja $S_n$ na nizovima s XOR $X$. Element $g$ s ciklusnom strukturom fiksira niz $\iff$ konstantan na ciklusima; parni ciklus doprinosi $0$ XOR-u (bilo koja od $M+1$ vrijednosti), neparni doprinosi svoju vrijednost. Dakle $\#\mathrm{Fix}(g) = (M+1)^{\#\text{parnih}} f_{\#\text{neparnih}}$, gdje je $f_q$ broj uređenih $q$-torki iz $[0,M]$ s XOR-om $X$.</p>
'''),
        ('Opažanje 2: uređene torke — struktura multiskupa XOR-ova',
         r'''
<p>$[0, M]$ se rastavlja na $O(W)$ dijadskih blokova $[x2^k, x2^k + 2^k - 1]$. XOR bloka duljine $k_1$ s blokom duljine $k_2 \le k_1$ je blok duljine $k_1$ s množinom $\cdot 2^{k_2}$; skup blokova ostaje malen ($x \in \{0, 1, \lfloor M/2^k\rfloor, \lfloor M/2^k\rfloor \oplus 1\}$). Uz obradu po rastućem $k$ i spajanje kraćih blokova, korak je $O(W)$: $f_1..f_N$ u $O(NW)$.</p>
'''),
        ('Redukcija: razdvoji parne i neparne cikluse',
         r'''
<p>$\mathrm{ans}_n = \frac1{n!}\sum_{i+j=n}\binom{n}{i} e_i o_j$, gdje $e_i$ = težinski zbroj permutacija samo s parnim ciklusima (težina $(M+1)^{\#}$), $o_j$ isto za neparne s težinom $f_{\#}$. $E(x) = \exp\bigl(-\tfrac{M+1}{2}\ln(1-x^2)\bigr) = (1-x^2)^{-(M+1)/2}$ — jedan polinomni exp ili binomni red. $O(x) = F(\mathrm{ODD}(x))$ s $\mathrm{ODD} = \tfrac12\ln\frac{1+x}{1-x}$, $F$ EGF od $f$.</p>
'''),
        ('Algoritam: kompozicija preko transpozicije',
         r'''
<p>$o = G v$ gdje $G_{n,k}$ = broj permutacija $n$ elemenata s $k$ neparnih ciklusa, $v_k = f_k$. Transponirani problem $G^T u$: $\sum_n u_n [x^n] e^{z\,\mathrm{ODD}(x)}$; iz $\partial_x H = \frac{z}{1-x^2}H$ slijedi $iH_i = zH_{i-1} + (i-2)H_{i-2}$, pa je $G^Tu$ podijeli-pa-vladaj s FFT-om u $O(n\log^2 n)$; Tellegenov princip daje isti trošak za $Gv$. Ukupno $O(N\log M + N\log^2 N)$. Alternativa (drugo rješenje): FWT po $x$ i P-rekurzivni $\left(\frac{1+t}{1-t}\right)^a$ — $O(N \log M)$.</p>
'''),
    ],
    'solution': r'''
<p>Ovo je teža inačica jednog Atcoderovog zadatka. Možete najprije pročitati rješenje izvornog zadatka za osnovnu ideju, no, iskreno, rješenje iz Atcoderova editoriala daleko je od rješenja ovog zadatka.</p>
<h3>Prvo rješenje</h3>
<p>Rješenje ima tri glavna dijela:</p>
<ol>
    <li>riješiti zadatak bez uvjeta nepadajućosti;</li>
    <li>svesti zadatak na neuređenu inačicu;</li>
    <li>ubrzati drugi korak trikovima s funkcijama izvodnicama.</li>
</ol>
<h4>Prvi dio</h4>
<p>Rješavamo zadatak bez uvjeta nepadajućosti: treba izračunati broj nizova $A_i$ ($0 \le A_i \le M$) s $\bigoplus_{i=1}^{n} A_i = X$ za $n = 0, 1, \dots, N_{MAX}$.</p>
<p>Neka je $W = \lceil \log M \rceil$. Neka je $S_i$ multiskup XOR-ova $i$ brojeva iz $[0, M]$. Vrijedi $S_{i+1} = \{x \oplus y \mid x \in S_i,\ 0 \le y \le M\}$. Odgovor je broj pojavljivanja $X$ u $S_1, S_2, \dots, S_{N_{MAX}}$. Pokušajmo izravno održavati $S_i$ i računati nešto poput konvolucije $S_i$ i intervala $[0, M]$ da bismo dobili $S_{i+1}$.</p>
<p>$S_i$ možemo particionirati na nekoliko podskupova. Brojevi u svakom podskupu leže u $[x \cdot 2^k, x \cdot 2^k + (2^k - 1)]$ i svaki se pojavljuje $c$ puta; podskup označavamo $(x, k, c)$. Intuitivno: viši bitovi brojeva su fiksni, a niži su ravnomjerno raspoređeni. Broj $k$ zovemo duljinom podskupa.</p>
<p>Interval $[0, M]$ lako se particionira na $O(W)$ takvih skupova, a indukcijom se pokazuje da se svaki $S_i$ može prikazati s $O(W)$ skupova.</p>
<p>Konvoluciju $S_i$ i $[0, M]$ računamo kao zbroj konvolucija svih parova podskupova. Za par $(x_1, k_1, c_1)$ i $(x_2, k_2, c_2)$ (bez smanjenja općenitosti $k_1 \ge k_2$) nakon konvolucije nižih $k_1$ bitova ravnomjerno je raspoređeno, a broj pojavljivanja postaje $c_1 \cdot c_2 \cdot 2^{k_2}$. Viši bitovi su viši bitovi od $(x_1 \cdot 2^{k_1}) \oplus (x_2 \cdot 2^{k_2})$. Indukcijom se također dokazuje da za fiksni $k$ vrijedi $x \in \{0, 1, \lfloor M / 2^k \rfloor, \lfloor M / 2^k \rfloor \oplus 1\}$, pa se $S_i$ može prikazati s najviše $4W$ podskupova.</p>
<p>Tako dobivamo algoritam složenosti $O(W^2)$ za konvoluciju dvaju multiskupova, što možda nije dovoljno brzo. Uočimo: pri konvoluciji para podskupova duljina $k_1, k_2$ ($k_1 \ge k_2$) za podskup duljine $k_2$ bitni su samo viših $W - k_1$ bitova. Konvoluciju možemo raditi u rastućem poretku po $k$; svi podskupovi duljine manje od $k$ mogu se spojiti prema istim višim $W - k$ bitovima, pa ih nakon spajanja ostaje $O(1)$. Time konvolucija traje $O(W)$, a ovaj dio rješavamo u $O(NW)$.</p>
<p>Odgovor za $i$ brojeva označimo $f_i$.</p>
<h4>Drugi dio</h4>
<p>Svodimo izvorni zadatak na neuređenu inačicu. Na zadatak možemo gledati i ovako: i dalje rješavamo zadatak bez uvjeta nepadajućosti, ali dva rješenja $A_1, \dots, A_n$ i $B_1, \dots, B_n$ ekvivalentna su ako se preuređivanjem $A$ može dobiti $B$; tražimo broj klasa ekvivalencije. Očito je broj klasa jednak broju rješenja s uvjetom nepadajućosti.</p>
<p>Broj klasa ekvivalencije računamo Burnsideovom lemom:
$$\frac{1}{n!} \sum_{g \in S_n} (\text{broj rješenja koja } g \text{ fiksira}).$$
Permutaciju $g \in S_n$ rastavimo na cikluse. Ako $g$ fiksira rješenje, svi $A_i$ unutar jednog ciklusa jednaki su. Za ciklus parne duljine svi se $A_i$ poništavaju u XOR-u, pa za njega imamo $(M + 1)$ izbora. Za ciklus neparne duljine preostaje jedan $A_i$. Dakle za permutaciju s $p$ parnih i $q$ neparnih ciklusa broj fiksiranih rješenja je $f_q \times (M + 1)^p$.</p>
<p>Dinamičkim programiranjem ili drugim kombinatoričkim pristupom mogli bismo izračunati koliko permutacija ima $p$ parnih i $q$ neparnih ciklusa i sve zbrojiti, no složenost bi bila prevelika. Međutim, parne i neparne slučajeve možemo računati neovisno.</p>
<p>Za parne cikluse, neka je $e_n$ zbroj težina permutacija $n$ elemenata koje se sastoje samo od parnih ciklusa, s težinom $(M + 1)^{\#\text{ciklusa}}$. Za neparne, neka je $o_n$ zbroj težina permutacija $n$ elemenata samo s neparnim ciklusima, s težinom $f_{\#\text{ciklusa}}$.</p>
<p>Kad imamo $e_n$ i $o_n$, odgovor za $n$ je
$$\frac{1}{n!} \sum_{i + j = n} e_i \times o_j \times \binom{n}{i},$$
što je jednostavna konvolucija.</p>
<h4>Treći dio</h4>
<p>Funkcijama izvodnicama ubrzavamo računanje $e$ i $o$. Budući da su parni i neparni slučaj odvojeni, dinamičkim programiranjem može se dobiti bolje rješenje, no za $n = 10^5$ bez naprednijih tehnika to nije dovoljno.</p>
<p>Parni je slučaj lakši. EGF parnog ciklusa je $-\frac{1}{2}(\ln(1 - x) + \ln(1 + x))$, pa je EGF niza $e$ jednaka $\exp\left(-\frac{M+1}{2}(\ln(1 + x) + \ln(1 - x))\right)$, što se lako računa u $O(n \log n)$.</p>
<p>Neparni je slučaj složeniji. Neka je $\mathrm{ODD}(x) = \frac{1}{2}(\ln(1 + x) - \ln(1 - x))$ EGF neparnog ciklusa, a $F(x) = \sum_{i=0}^{n} f_i \frac{x^i}{i!}$ EGF niza $f$. Tada je
$$o_n = [x^n] \sum_{i=0}^{n} f_i \frac{\mathrm{ODD}^i}{i!} = [x^n] F(\mathrm{ODD}(x)),$$
dakle treba izračunati kompoziciju polinoma $F$ i $\mathrm{ODD}$. Kompozicija dvaju proizvoljnih polinoma teška je, ali $\mathrm{ODD}$ je vrlo poseban, pa je moguće u $O(n \log^2 n)$.</p>
<p>Postoji sličan zadatak s detaljnim tutorialom (u njemu se traži kompozicija proizvoljnog polinoma i EGF-a ciklusa duljine veće od 1); rješenja su gotovo ista. Ovdje dajemo kratku ideju. Za bolje razumijevanje preporučujemo najprije naučiti kako <b>princip transpozicije</b> (Tellegenov princip) funkcionira u manipulaciji funkcijama izvodnicama.</p>
<p>Definirajmo matricu $G_{n,k}$ kao broj permutacija $n$ elemenata s $k$ neparnih ciklusa i vektor $v_{k,1} = f_k$. Želimo $G \cdot v$. To je možda teško izravno, pa pogledajmo kako izračunati $G^T \cdot u$ za proizvoljan vektor $u$. Kako se svaki korak računanja $G^T \cdot u$ može shvatiti kao elementarna transformacija matrice, algoritam je umnožak mnogih elementarnih transformacija, pa $G \cdot v$ računamo transponirajući te transformacije. Ako $G^T \cdot u$ računamo u $O(T(n))$, i $G \cdot v$ računamo u $O(T(n))$.</p>
<p>Promotrimo dvovarijabilnu EGF za $G_{n,k}$: $H(x, z) = \sum G_{n,k} \frac{x^n}{n!} \frac{z^k}{k!}$. Vrijedi $H(x, z) = e^{z \cdot \mathrm{ODD}(x)} = e^{\frac{z}{2}(\ln(1+x) - \ln(1-x))}$. Neka je $H_i = [x^i] H$; iz diferencijalne jednadžbe
$$\frac{\partial H}{\partial x} = \frac{z}{2}\left(\frac{1}{1 + x} + \frac{1}{1 - x}\right) H = \frac{z}{1 - x^2} H$$
izvodimo linearnu rekurziju
$$i H_i = z H_{i-1} + (i - 2) H_{i-2}.$$
Definiramo $2 \times 2$ matricu $A_i$ s $[H_i, H_{i-1}]^T = A_i [H_{i-1}, H_{i-2}]^T$. Zbroj $\sum H_i \times u_i$ računamo algoritmom podijeli-pa-vladaj s FFT-om u $O(n \log^2 n)$. To je algoritam za $G^T \cdot u$, pa i $G \cdot v$ računamo u $O(n \log^2 n)$.</p>
<p>Ukupno smo zadatak riješili u $O(n \log M + n \log^2 n)$.</p>
<h3>Drugo rješenje</h3>
<p>Burnsideova lema ovdje nije nužna. Postoji vjerojatno mnogo kombinatoričkih rješenja; ovdje dajemo jedno temeljeno na funkcijama izvodnicama.</p>
<p>Neka je $x$ varijabla u „skupovnom“ FPS-u u kojem je množenje XOR-konvolucija, a $t$ varijabla koja bilježi koliko je brojeva odabrano. Odgovor je
$$[x^X t^N] \prod_{S=0}^{M} \frac{1}{1 - t x^S} = [x^X t^N] \prod_{S=0}^{M} \frac{1 + t x^S}{1 - t^2}.$$
Neka je $F = \prod_{S=0}^{M} \frac{1 + t x^S}{1 - t^2}$. FWT-om i IFWT-om izvlačimo koeficijent uz $x^X$:
$$[x^T] \mathrm{FWT}(F) = \prod_{S=0}^{M} \frac{1 + (-1)^{|S \cap T|} t}{1 - t^2},$$
$$[x^X] F = [x^X] \mathrm{IFWT}(\mathrm{FWT}(F)) = \frac{1}{2^L} \sum_{T=0}^{2^L - 1} (-1)^{|X \cap T|} \prod_{S=0}^{M} \frac{1 + (-1)^{|S \cap T|} t}{1 - t^2}.$$
Umnožak $\prod_{S=0}^{M} \frac{1 + (-1)^{|S \cap T|} t}{1 - t^2}$ ovisi samo o broju parnih i neparnih vrijednosti $|S \cap T|$. Neka je $g(T) = \sum_{S=0}^{M} [2 \mid |S \cap T|]$. Tada je
$$F = \frac{1}{2^L} \sum_{T=0}^{2^L - 1} (-1)^{|X \cap T|} \left(\frac{1 + t}{1 - t}\right)^{g(T)}.$$
Znamenkastim DP-om ili analizom Trie-strukture brojeva $0 \sim M$ vidi se da $g(T)$ poprima najviše $O(L)$ različitih vrijednosti, a $\sum (-1)^{|X \cap T|}$ po svim $T$ s istim $g(T)$ također se računa u $O(\mathrm{polylog}(M))$. Detalje izostavljamo.</p>
<p>Tako $F$ postaje polinom u $\frac{1 + t}{1 - t}$ s $O(\log M)$ nenul-članova. Neka je $P(t) = (1 + t)^a (1 - t)^{-a}$; tada je $P'(t) = \left(\frac{a}{1 + t} - \frac{a}{1 - t}\right) P(t)$, što je P-rekurzivno, pa prvih $N$ članova računamo u $O(N)$.</p>
<p>Zadatak se time rješava u $O(N \log M)$.</p>
''',
},
{
    'letter': 'B',
    'title': 'Best Problem',
    'title_hr': 'Najbolji zadatak',
    'slug': 'B_best_problem',
    'tl': '1 s',
    'ml': '1024 MB',
    'statement': r'''
<p>Zadan je binarni niz $S$. Proizvoljno mnogo puta smiješ zamijeniti podniz <code>0101</code> s <code>1010</code>. Koliko najviše operacija možeš izvesti?</p>
<h3>Ulaz</h3>
<p>Binarni niz $S$ ($1 \le |S| \le 5 \times 10^6$).</p>
<h3>Izlaz</h3>
<p>Jedan broj — odgovor.</p>
''',
    'hints': [
        r'''
<p>Promijeni prikaz: između susjednih bitova napiši <code>R</code> za 00, <code>L</code> za 11, <code>X</code> za 01/10. Operacija 0101→1010 pomiče <code>R</code> četiri mjesta udesno ili <code>L</code> četiri ulijevo preko X-ova, poništava par <code>R…L</code> na razmaku 4, ili iz 5 X-ova stvara <code>L…R</code>.</p>
''',
        r'''
<p>Pohlepno: poništi sve moguće RL parove, zatim gurni R-ove udesno i L-ove ulijevo dok se ne slože u grupe „RR…  …LL” koje gledaju jedna prema drugoj; na kraju DP po grupama gdje se za svaki par grupa pomiče samo jedna (maksimum kvadratne funkcije je na kraju intervala) — $O(n)$.</p>
''',
    ],
    'coach': [
        ('Opažanje 1: nađi invarijantu/lokalni opis',
         r'''
<p>Operacija mijenja samo 4 bita i pomiče „01” uzorke. U zapisu razlika susjednih bitova (R/L/X) operacija postaje pomak jednog simbola za točno 4 mjesta preko X-ova, što je čisti model tokena na traci. Dodaj <code>11</code> lijevo i <code>00</code> desno da se rubovi ponašaju uniformno.</p>
'''),
        ('Opažanje 2: paritet pozicija',
         r'''
<p>Pomaci su za 4, pa ostatak pozicije svakog L/R modulo 4 ostaje. Poništavanje (R 4 lijevo od L) i stvaranje (5 X-ova → L,R) su inverzi; nakon što se na početku poništi sve što se može, kasnije stvaranje–poništavanje samo bi vratilo stanje bez dobitka koraka.</p>
'''),
        ('Opažanje 3: pohlepno slaganje pa DP',
         r'''
<p>R-ovi se guraju desno dok ne naiđu na L ili drugi R (ostaju 0 ili 2 X-a između članova grupe), L-ovi lijevo. Ostaje niz grupa L…R R…L R…L …; grupe se međusobno približavaju po 4 mjesta. Broj koraka = ukupni pomak / 4 + stvaranja na kraju; funkcija cilja je po paru grupa kvadratna u točki susreta, maksimum na rubu, pa DP bilježi samo „koja grupa stoji”: $O(n)$.</p>
'''),
        ('Složenost',
         r'''
<p>$O(n)$ za $n \le 5\cdot10^6$; pazi na brz ulaz i 64-bitni odgovor.</p>
'''),
    ],
    'solution': r'''
<p>Najprije promijenimo notaciju. Za dva susjedna bita: ako su <code>00</code>, između njih pišemo R; ako su <code>11</code>, pišemo L; ako su <code>01</code> ili <code>10</code>, pišemo X. Bez smanjenja općenitosti dodajmo dvije jedinice lijevo i dvije nule desno od niza.</p>
<p>Pogledajmo kako se <code>0101</code> mijenja:</p>
<ol>
    <li><code>001010 → 010100</code>, tj. <code>RXXXX → XXXXR</code></li>
    <li><code>101011 → 110101</code>, tj. <code>XXXXL → LXXXX</code></li>
    <li><code>001011 → 010101</code>, tj. <code>RXXXL → XXXXX</code></li>
    <li><code>101010 → 110100</code>, tj. <code>XXXXX → LXXXR</code></li>
</ol>
<p>Novi zadatak: imamo niz; R možemo pomaknuti 4 polja udesno, L 4 polja ulijevo, a put od početka do odredišta mora se sastojati od X-ova. Par RL u kojem je R 4 polja lijevo od L može se poništiti. Iz uzastopnih X-ova možemo stvoriti par LR. Zbog pariteta između L i R mora biti neparan broj X-ova, a između LL i RR paran.</p>
<p>Najprije radimo operaciju 3: pohlepno poništimo sve uparene RL parove. Budući da se ostatci modulo 4 pozicija svih L i R ne mijenjaju, operacija 3 više neće biti korisna.</p>
<p>Zatim za dva uzastopna R lijevi R pohlepno pomičemo udesno prvom operacijom. Ako bismo koristili operacije 3 i 4, novonastali parovi bi se na kraju poništili, a broj koraka se ne bi promijenio. Slično za L.</p>
<p>Nakon tih pohlepnih koraka niz izgleda otprilike kao <code>L...RR..RR.......L..LL.......RR.........LL.....R</code>: mnogo LR grupa koje „gledaju“ jedna prema drugoj. Između članova iste L ili R grupe nula je ili dva X-a.</p>
<p>Zatim razmatramo pomicanje cijelih L ili R grupa 4 polja lijevo ili desno dok se ne sretnu, a na kraju stvaramo nove LR parove operacijom 4.</p>
<p>Napokon radimo DP koji bilježi kamo ide svaka L i R grupa i koliki je najveći broj koraka. Težina je kvadratna funkcija, pa se to može riješiti trikom konveksne ljuske. Štoviše, kako tražimo maksimum, on se postiže na krajnje lijevoj ili krajnje desnoj poziciji — za svaki par grupa pomiče se samo jedna od njih. Time izbjegavamo konveksnu ljusku i rješavamo zadatak u $O(n)$.</p>
''',
},
{
    'letter': 'C',
    'title': 'Cryptography Problem',
    'title_hr': 'Kriptografski zadatak',
    'slug': 'C_cryptography_problem',
    'tl': '5 s',
    'ml': '1024 MB',
    'statement': r'''
<p>Zadano je $m$ jednadžbi $a_i \cdot x + err_i \equiv c_i \pmod p$, gdje je $err_i$ nepoznata slučajna greška iz $[-\lfloor p/200 \rfloor, \lfloor p/200 \rfloor]$, a $a_i, c_i, p$ su poznati. Jednadžbe vrijede za neki nepoznati cijeli $x$; pronađi jedan takav $x$.</p>
<h3>Ulaz</h3>
<p>$T \le 500$ testova; u svakom $m, p$ ($50 \le m \le 100$, $10^{15} \le p \le 10^{18}$, $p$ prost) i $m$ parova $a_i, c_i$. Vrijednosti $a_i$ i $x$ uniformno su slučajne.</p>
<h3>Izlaz</h3>
<p>Za svaki test jedan $x$.</p>
''',
    'hints': [
        r'''
<p>To je LWE s jednom nepoznanicom (hidden number problem): $a_i x \approx c_i \pmod p$ s malom greškom. Cilj: linearne kombinacije jednadžbi s malim koeficijentom $A = \sum y_i a_i \bmod p$ i još malom ukupnom greškom $E = M\sum|y_i|$ — tada je $x$ u uniji kratkih intervala $[(C + ip - E)/A, (C + ip + E)/A]$.</p>
''',
        r'''
<p>Male kombinacije: „multi-tree” — sortiraj $a_i$, uzmi razlike bliskih parova (koeficijenti rastu 2$\times$, vrijednost pada $\sim m\times$), ponovi nekoliko puta. Presijecaj intervale, prvo s malim $A$ (grubo), pa s većim (fino). Alternativa: LLL nad rešetkom dimenzije $\approx 16$.</p>
''',
    ],
    'coach': [
        ('Opažanje 1: normaliziraj',
         r'''
<p>Zamijeni $x$ s $x' = (a_1 x - c_1 + M) \bmod p \in [0, 2M]$ ($M = \lfloor p/200\rfloor$): sada je nepoznanica malena, a svaka jednadžba postaje $a_i' x' + err \equiv c_i' \pmod p$. Male nepoznanice + male greške = klasična „skrivena mala vrijednost”.</p>
'''),
        ('Opažanje 2: kombiniranje jednadžbi',
         r'''
<p>$\sum y_i(\text{jedn}_i)$: koeficijent $A = \sum y_i a_i \bmod p$, greška $\le M\sum|y_i|$. Ako je $A \ll p/M$, jednadžba $Ax \in [C - E, C + E] + p\mathbb Z$ ograničava $x$ na $\approx A \cdot 2M/p$ intervala širine $2E/A$ — svaka dobra kombinacija reže skup kandidata.</p>
'''),
        ('Opažanje 3: kako naći male $A$',
         r'''
<p>Generaliziran rođendanski/„multi-tree” napad: iz sortiranog skupa vrijednosti gradimo razlike susjednih (do 5 dalje) — vrijednosti padaju faktor $\sim m$ dok $\sum|y|$ raste faktor 2. Nakon $r$ razina: $A \approx p/m^r$, $\sum|y| = 2^r$. Uz $m \approx 50$, $r = 5$: $A \approx p/3\cdot10^8$, greška $32M \approx p/6$ — dovoljno da intervali ostanu smisleni.</p>
'''),
        ('Algoritam',
         r'''
<p>Održavaj sortirani popis disjunktnih intervala za $x'$ (početno $[0, 2M]$); za kombinacije od najmanjeg $A$ prema većima presijeci s unijom intervala te kombinacije (intervali su periodični s periodom $p/A$ — samo oni koji sijeku trenutne kandidate). Kad ostane jedan kandidat (ili malo), provjeri sve jednadžbe. Druga opcija: rešetka $T+2$ dimenzije i LLL (CTF-standard).</p>
'''),
    ],
    'solution': r'''
<h3>Prvo rješenje</h3>
<p>Neka je $M = \lfloor p / 200 \rfloor$ i $x' = (a_1 x - c_1 + M) \bmod p$. Tada je $x' \in [0, 2M]$. Sve ostale jednadžbe prepišemo u terminima $x'$ i rješavamo $x'$ umjesto $x$ (dalje $x$ označava taj $x'$).</p>
<p>Osnovna ideja: naći slučajne linearne kombinacije jednadžbi koje daju mali koeficijent, a ne povećavaju previše grešku. Pomnožimo li $i$-tu jednadžbu s $y_i$ i sve zbrojimo, dobivamo $(\sum a_i y_i) \cdot x + \text{greška} \equiv \sum c_i y_i \pmod p$, gdje greška ne prelazi $(\sum |y_i|) \cdot M$.</p>
<p>Neka je $A = (\sum a_i y_i) \bmod p$, $E = (\sum |y_i|) \cdot M$, $C = (\sum c_i y_i) \bmod p$. Ako je koeficijent $A$ dovoljno malen, a greška $E$ ne prelazi $p/2$, skup rješenja te jednadžbe unija je intervala
$$\left[\frac{C + ip - E}{A}, \frac{C + ip + E}{A}\right].$$
Te intervale iterativno presijecamo s dosadašnjim skupom rješenja i održavamo skup intervala u kojima $x$ može biti. Ako linearne kombinacije biramo slučajno i presijecamo „prikladna“ rješenja, skup se eksponencijalno smanjuje. „Prikladno“ znači: kad su intervali malo manji, presijecamo s većim $A$ — inače se skup ne bi smanjivao dovoljno brzo.</p>
<p>Kako naći te slučajne linearne kombinacije? Tehnika se stalno koristi za razbijanje polinomnih hasheva i zove se <i>multi-tree attack</i>. Kratka ideja: imamo skup brojeva, sortiramo ga i generiramo novi skup iz razlika bliskih brojeva. Primjerice, ovdje iz sortiranog niza $a$ generiramo $\{a_i - a_j \mid j &lt; i \le j + 5\}$ i zadržimo najmanje brojeve; to ponovimo 5 puta. To je dovoljno za prolaz.</p>
<h3>Drugo rješenje</h3>
<p>Zadatak je dobro poznat u CTF zajednici (zahvala @oToToT i @toxicpie). Svodi se na problem najkraćeg vektora u rešetki (lattice) i rješava se bibliotečnim kodom.</p>
<p>Odaberemo bilo kojih $T$ jednadžbi i konstruiramo $T + 2$ vektora $e_1, \dots, e_{T+2}$ dimenzije $T + 2$:</p>
<ul>
    <li>za $i = 1, \dots, T$: $e_{i,i} = M_1 p$;</li>
    <li>za $i = T + 1$: $e_{i,j} = M_1 a_j$ za $j = 1, \dots, T$ i $e_{i,T+1} = 1$;</li>
    <li>za $i = T + 2$: $e_{i,j} = M_1 c_j$ za $j = 1, \dots, T$ i $e_{i,T+2} = p / M_2$.</li>
</ul>
<p>Ako je odgovor $x$, tada je $x e_{T+1} - e_{T+2} - \sum_{i=1}^{T} \lfloor a_i x / p \rfloor e_i$ kratak vektor u kojem je svaka koordinata otprilike $\max(p, M_1 \cdot \text{greška})$.</p>
<p>Izbor $T = 14$, $M_1 = 50$, $M_2 = 20$ dovoljan je za prolaz, ali treba dobro optimiziran LLL.</p>
''',
},
{
    'letter': 'D',
    'title': 'Digit Sum Problem',
    'title_hr': 'Zadatak o zbroju znamenki',
    'slug': 'D_digit_sum_problem',
    'tl': '3 s',
    'ml': '1024 MB',
    'statement': r'''
<p>Za nenegativan cijeli $x$ neka su $f(x)$ i $g(x)$ zbrojevi znamenki $x$ u binarnom odnosno ternarnom zapisu. Za zadane $n, a, b, c$ izračunaj
$$\left(\sum_{i=1}^{n} a^i b^{f(i)} c^{g(i)}\right) \bmod 998244353.$$</p>
<h3>Ulaz</h3>
<p>$n, a, b, c$ ($1 \le n \le 10^{13}$, $1 \le a, b, c &lt; 998244353$).</p>
<h3>Izlaz</h3>
<p>Jedan broj — odgovor.</p>
''',
    'hints': [
        r'''
<p>Podijeli $[1, n]$ svim višekratnicima $M_2 = 2^p \approx \sqrt n$ i $M_3 = 3^q \approx \sqrt n$ — $O(\sqrt n)$ dijelova. Unutar dijela viši binarni i ternarni prefiksi su konstantni: doprinos = $a^{\text{start}} b^{f(\text{prefiks})} c^{g(\text{prefiks})} \cdot S(\text{stanje})$.</p>
''',
        r'''
<p>„Stanje” dijela određeno je tipom krajeva (2-višekratnik / 3-višekratnik) i ostatkom početka modulo druge potencije — ukupno $O(M_2 + M_3)$ stanja. Predizračunaj $S$ za sve njih inkrementalno: iz tablice za $(M_2, M_3)$ tablicu za $(2M_2, M_3)$ dobiješ u $O(M_2 + M_3)$ jer se svako novo stanje razbija na $O(1)$ starih.</p>
''',
    ],
    'coach': [
        ('Opažanje 1: multiplikativnost po znamenkama',
         r'''
<p>$a^i b^{f(i)} c^{g(i)}$ je umnožak po pozicijama binarnog i ternarnog zapisa — ali dva zapisa ne dijele strukturu, pa klasični znamenkasti DP ne radi izravno. Ideja susreta u sredini: fiksiraj visoke znamenke oba zapisa, sumiraj po niskima.</p>
'''),
        ('Opažanje 2: rešetka prijelomnih točaka',
         r'''
<p>Na višekratnicima $2^p$ mijenjaju se visoki binarni bitovi, na višekratnicima $3^q$ visoke ternarne znamenke. Između dva uzastopna prijelomna broja obje su „glave” fiksne, pa je zbroj $= a^{\text{start}} b^{f_{hi}} c^{g_{hi}}\sum_{t} a^{t} b^{f(\text{lo}_2(t))} c^{g(\text{lo}_3(t))}$, što ovisi samo o klasi dijela.</p>
'''),
        ('Opažanje 3: mali broj klasa',
         r'''
<p>Dio počinje na $2^p$-višekratniku i završava prije sljedećeg $3^q$-višekratnika (ili obratno): duljina $\lt \min(M_2, M_3)$ i početna pozicija mod $M_3$ (odnosno mod $M_2$) određuju sve; tipovi (2,3), (3,2), (2,2), (3,3) — ukupno $O(\sqrt n)$ klasa, koje se grade postupno povećavajući $p$ ili $q$ i rastavljajući nove klase na $O(1)$ starih.</p>
'''),
        ('Složenost',
         r'''
<p>$O(\sqrt n)$ uz $n \le 10^{13}$ — oko $3\cdot10^6$ dijelova i sličan broj stanja; pazi na modularnu aritmetiku i predizračun potencija $a^{M}$.</p>
'''),
    ],
    'solution': r'''
<p>Glavna je ideja nešto poput sqrt-dekompozicije ili susreta u sredini.</p>
<p>Neka je $M = \sqrt{n}$, a $M_2 = 2^p$ i $M_3 = 3^q$ potencije najbliže $M$. Ispišemo li sve višekratnike $M_2$ i $M_3$, interval $1 \sim n$ dijeli se na $O(\sqrt{n})$ dijelova. Pitanje je kako izračunati zbroj za svaki dio u $O(1)$ uz pretprocesiranje.</p>
<p>Za svaki dio prefiks brojeva u binarnom i ternarnom zapisu je fiksan, pa prefiks ne moramo razmatrati. Krajevi intervala su višekratnici $M_2$ ili $M_3$, pa postoji najviše $O(M_2 + M_3)$ različitih stanja. Ako je jedan kraj višekratnik $M_2$, a drugi višekratnik $M_3$, stanje je određeno duljinom. Ako su oba kraja višekratnici $M_2$, stanje je određeno ostatkom prvog broja modulo $M_3$; slično za $M_3$.</p>
<p>Kako izračunati odgovore za ta stanja? Odgovor za $(2M_2, M_3)$ ili $(M_2, 3M_3)$ računamo iz $(M_2, M_3)$ u $O(M_2 + M_3)$: primjerice, svako stanje za $(2M_2, M_3)$ podijelimo višekratnicima $M_2$ i $M_3$ na $O(1)$ intervala i zbrojimo. Krenemo od $(1, 1)$ i povećavamo manju potenciju dok obje ne dosegnu $O(\sqrt{n})$.</p>
<p>Složenost je $O(\sqrt{n})$.</p>
''',
},
{
    'letter': 'E',
    'title': 'Elliptic Curve Problem',
    'title_hr': 'Zadatak o eliptičkoj krivulji',
    'slug': 'E_elliptic_curve_problem',
    'tl': '3 s',
    'ml': '1024 MB',
    'statement': r'''
<p>Neka je $p$ neparan prost broj. Izračunaj broj kvadratnih ostataka u $[l, r]$; $x$ je kvadratni ostatak modulo $p$ ako i samo ako $x^{(p-1)/2} \equiv 1 \pmod p$.</p>
<h3>Ulaz</h3>
<p>$p, l, r$ ($3 \le p \le 10^{11}$, $1 \le l \le r &lt; p$).</p>
<h3>Izlaz</h3>
<p>Jedan broj — odgovor.</p>
''',
    'hints': [
        r'''
<p>Kvadratni ostatci su točno $i^2 \bmod p$ za $i = 1..\frac{p-1}{2}$ (svi različiti). Indikator $[l \le v \le r]$ za $v = x \bmod p$ jednak je $\lfloor (x-l)/p\rfloor - \lfloor (x-r-1)/p\rfloor$.</p>
''',
        r'''
<p>Treba $\sum_{i \le (p-1)/2}\lfloor (i^2 + c)/p\rfloor$ — broj cjelobrojnih točaka pod parabolom. Kao za $\sum\lfloor n/i\rfloor$ uz Stern–Brocot/konveksnu ljusku: područje je konveksno, koordinate $O(p)$, pa ljuska ima $O(p^{2/3})$ bridova i zbroj se računa po bridovima.</p>
''',
    ],
    'coach': [
        ('Opažanje 1: ne treba Legendre',
         r'''
<p>Umjesto testiranja svakog $x \in [l,r]$ (do $10^{11}$), nabroji ostatke kao kvadrate: $\#\{i \le \frac{p-1}{2} : i^2 \bmod p \in [l, r]\}$. I to je $\sim 5\cdot10^{10}$ — treba pametna suma.</p>
'''),
        ('Opažanje 2: pretvori u floor-sumu',
         r'''
<p>$[l \le x \bmod p \le r] = \lfloor\frac{x - l}{p}\rfloor - \lfloor\frac{x - r - 1}{p}\rfloor$ (broj višekratnika $p$ u $(x - r - 1, x - l]$). Ostaje $\sum_i \lfloor (i^2 + c)/p \rfloor$ za dvije konstante $c$.</p>
'''),
        ('Opažanje 3: točke pod konveksnom krivuljom',
         r'''
<p>$\sum_i \lfloor h(i)\rfloor$ za konveksnu (ili konkavnu) $h$ = broj rešetkastih točaka ispod grafa; njihova gornja ovojnica je konveksni poligon s $O(N^{2/3})$ vrhova kad su koordinate $\le N$ (klasična ocjena). Ovojnicu gradi hodanjem po Stern–Brocotovu stablu nagiba (kao „univerzalni” algoritam za $\sum\lfloor (ai+b)/c\rfloor$, ali s testom „je li sljedeći nagib još ispod krivulje” preko $h$).</p>
'''),
        ('Algoritam i složenost',
         r'''
<p>Implementiraj generičku funkciju koja za konveksnu $h$ (ovdje $(x^2 + c)/p$, s derivacijom za odabir nagiba) vraća $\sum \lfloor h(i) \rfloor$ u $O(p^{2/3})$, uz <code>__int128</code> za $i^2$. Za $p \le 10^{11}$: $\approx 2\cdot10^7$ koraka.</p>
'''),
    ],
    'solution': r'''
<p>Uočimo da je $[l \le (x \bmod p) \le r] = \left\lfloor \frac{x - l}{p} \right\rfloor - \left\lfloor \frac{x - r - 1}{p} \right\rfloor$, te da su $1^2, 2^2, \dots, \left(\frac{p-1}{2}\right)^2$ svi različiti kvadratni ostatci modulo $p$.</p>
<p>Zadatak zato prepisujemo kao
$$\sum_{i=1}^{(p-1)/2} [l \le (i^2 \bmod p) \le r] = \sum \left(\left\lfloor \frac{i^2 - l}{p} \right\rfloor - \left\lfloor \frac{i^2 - r - 1}{p} \right\rfloor\right).$$
Treba dakle učinkovito računati $\sum \left\lfloor \frac{i^2 + c}{p} \right\rfloor$. Tehnika je vrlo slična računanju $\sum \lfloor n / i \rfloor$.</p>
<p>Osnovna ideja: brojimo cjelobrojne točke između parabole i pozitivne $x$-osi. Područje je konveksno, a koordinate točaka su u $[0, p + O(1)]$, pa konveksna ljuska ima $O(p^{2/3})$ bridova. Nađemo konveksnu ljusku i izračunamo odgovor.</p>
<p>Detalje tehnike ne navodimo; zainteresiranima autor preporučuje kratki pregled (na kineskom) o ovoj tehnici.</p>
''',
},
{
    'letter': 'F',
    'title': 'Full Clue Problem',
    'title_hr': 'Zadatak s punim naznakama',
    'slug': 'F_full_clue_problem',
    'tl': '1 s',
    'ml': '1024 MB',
    'statement': r'''
<p>Slitherlink se igra na $n \times n$ mreži: rješavač crta petlju duž bridova ćelija (bez grananja i samopresijecanja) tako da je broj u ćeliji jednak broju njezinih bridova koje petlja koristi. Konstruiraj $n \times n$ slitherlink s naznakama (brojevima $0..4$) u <b>svim</b> ćelijama koji ima više rješenja, i to takvih da postoji par različitih rješenja koja dijele najviše četiri brida.</p>
<h3>Ulaz</h3>
<p>$n$ ($2 \le n \le 20$); rješenje uvijek postoji.</p>
<h3>Izlaz</h3>
<p>Matrica $n \times n$ naznaka te dva rješenja kao $n \times n$ matrice ($1$ = unutar petlje, $0$ = izvan).</p>
''',
    'hints': [
        r'''
<p>Traži se mreža s dva rješenja koja dijele $\le 4$ brida. Razmisli o dvjema petljama koje su međusobno „komplementarne”: petlja A i petlja B čije se unutrašnjosti razlikuju gotovo posvuda, a naznake (broj korištenih bridova po ćeliji) im se podudaraju.</p>
''',
        r'''
<p>Za male $n$ napiši grubu silu: nabroji jednostavne petlje na mreži $n\times n$, grupiraj po vektoru naznaka, traži par s malim presjekom bridova. Zatim uoči uzorak koji se proteže na sve $n$ (npr. periodično ponavljanje bloka).</p>
''',
    ],
    'coach': [
        ('Opažanje 1: što naznake vide',
         r'''
<p>Naznaka ćelije broji bridove petlje na njezinom rubu. Dvije petlje daju istu tablicu ako oko svake ćelije koriste jednako mnogo bridova — ne nužno iste bridove. Cilj: par petlji s istom „lokalnom statistikom” a gotovo disjunktnim skupom bridova.</p>
'''),
        ('Opažanje 2: konstrukcijski zadatak = eksperiment',
         r'''
<p>Ovdje nema formule: službeno rješenje je slika. Strategija na natjecanju: brute force za $n = 2, 3, 4$ (petlja = podskup ćelija čija je granica jedna zatvorena krivulja; nabroji podskupove „unutra”), izvuci uzorak, generaliziraj, provjeri programom za sve $n \le 20$.</p>
'''),
        ('Provjera',
         r'''
<p>Napiši validator: iz matrice 0/1 (unutra/izvan) izračunaj bridove petlje (granica između različitih vrijednosti), provjeri da je granica jedan ciklus bez grananja, izračunaj naznake i presjek bridova dvaju rješenja ($\le 4$).</p>
'''),
    ],
    'solution': r'''
<p>Odgovor je u službenom tutorialu dan slikom (prikaz konstrukcije s dvama rješenjima) koju ovdje ne reproduciramo — pogledajte <a href="https://contest.ucup.ac/download.php?type=attachments&amp;id=1195&amp;r=1">izvorni PDF</a>, stranice 5–6.</p>
<p>Do konstrukcije se može doći pisanjem grube sile za male $n$ ili jednostavno igranjem rukom.</p>
''',
},
{
    'letter': 'G',
    'title': 'Graph Problem',
    'title_hr': 'Zadatak o grafu',
    'slug': 'G_graph_problem',
    'tl': '5 s',
    'ml': '1024 MB',
    'statement': r'''
<p>Zadan je usmjereni graf s $n$ vrhova i $m$ bridova te $q$ neovisnih upita. U svakom upitu zadano je $k_1$ vrhova $p_1, \dots, p_{k_1}$ koji se brišu i $k_2$ parova $(s_i, t_i)$; za svaki par odgovori postoji li put od $s_i$ do $t_i$ nakon brisanja. Upiti su šifrirani (online) prema zadanom pseudokodu.</p>
<h3>Ulaz</h3>
<p>$n \le 500$, $m \le n(n-1)$, $q \le 4 \times 10^5$, $1 \le k_1 \le \min(n - 2, 6)$, $\sum k_2 \le 4 \times 10^6$.</p>
<h3>Izlaz</h3>
<p>Za svaki upit binarni niz duljine $k_2$.</p>
''',
    'hints': [
        r'''
<p>Dostiživost preko algebre: sa slučajnim težinama bridova $W$ nad $\mathbb F_q$, $M = (I - W)^{-1}$ ima $M_{s,t} \ne 0$ točno kad postoji put (s velikom vjerojatnošću).</p>
''',
        r'''
<p>Brisanje $k_1 \le 6$ vrhova = ažuriranje ranga $k_1$; Woodburyjev identitet daje elemente novog inverza iz starog: $s \to t$ postoji $\iff M_{s,t} \ne \sum_{i,j} M_{s,p_i}(P^{-1})_{i,j}M_{p_j,t}$ gdje $P_{i,j} = M_{p_i,p_j}$. $O(n^3 + qk_1^3 + \sum k_2 \cdot k_1^2)$.</p>
''',
    ],
    'coach': [
        ('Opažanje 1: dostiživost kao (ne)nul element inverza',
         r'''
<p>$(I - W)^{-1} = \sum_k W^k$ formalno; $(W^k)_{s,t}$ je zbroj težina šetnji duljine $k$. Zbroj po svim šetnjama je racionalna funkcija težina, nenul-polinom (kao formalni izraz) $\iff$ postoji put; slučajna evaluacija nad velikim poljem (Schwartz–Zippel) pretvara to u test $\ne 0$. Jedna Gaussova inverzija $O(n^3)$ za $n = 500$.</p>
'''),
        ('Opažanje 2: brisanje vrhova = ažuriranje niskog ranga',
         r'''
<p>Ukloni izlazne bridove vrhova iz $p$: $N' = N + UV$ s $U$ ($n\times k$) selektor stupaca i $V$ ($k\times n$) redovi $W_{p_j,\cdot}$. Woodbury: $(N + UV)^{-1} = M - MU(I_k + VMU)^{-1}VM$.</p>
'''),
        ('Opažanje 3: pojednostavljenje međumatrice',
         r'''
<p>Iskoristi $NM = I$: $(VMU)_{i,j} = \sum_k (I - N)_{p_i,k}M_{k,p_j} = M_{p_i,p_j} - [i=j]$, pa je $I_k + VMU = P$ s $P_{i,j} = M_{p_i,p_j}$. Isto $(MU)_{s,i} = M_{s,p_i}$ i $(VM)_{j,t} = M_{p_j,t}$ (jer $t \notin p$). Novi element: $M_{s,t} - \sum_{i,j} M_{s,p_i}(P^{-1})_{i,j}M_{p_j,t}$.</p>
'''),
        ('Algoritam i složenost',
         r'''
<p>Predizračun $M$ nad $\mathbb F_q$ ($q$ prost $\approx 10^9$, ili dva modula radi sigurnosti). Po upitu: $P^{-1}$ u $O(k_1^3)$; po paru $(s,t)$: $O(k_1^2)$ (predmnoži $M_{s,p}\cdot P^{-1}$ za isti $s$ ako se ponavlja). Ukupno $O(n^3 + qk_1^3 + k_1^2\sum k_2) \approx 1.25\cdot10^8 + 8.6\cdot10^7 + 1.4\cdot10^8$. Online dekripcija upita prema pseudokodu.</p>
'''),
    ],
    'solution': r'''
<p>Neka je $A$ matrica susjedstva grafa. Matrica dostiživosti je nešto poput $I + A + A^2 + \dots = (I - A)^{-1}$ (konvergenciju ovdje ne razmatramo). U rješenju svakom bridu dodijelimo slučajnu težinu (novu težinsku matricu susjedstva označimo $W$), pa izračunamo $N = I - W$ i $M = (I - W)^{-1}$. Vrh $s$ dostiže $t$ ako i samo ako $M_{s,t} \ne 0$.</p>
<p>Brisanje nekoliko vrhova je ažuriranje matrice susjedstva niskog ranga, a nas zanimaju pojedini elementi nove inverzne matrice — što daje <b>Woodburyjev identitet</b>: za $n \times k$ matricu $U$ i $k \times n$ matricu $V$, ako je $B = A + UV$, tada
$$B^{-1} = A^{-1} - A^{-1} U (I_k + V A^{-1} U)^{-1} V A^{-1}.$$
Neka je $U_{i,j} = [i = p_j]$, $V_{j,i} = W_{p_j, i}$. Tada je $(UV)_{i,j} = \sum_k [i = p_k] W_{p_k, j}$, tj. $(UV)_{i,j} = W_{i,j}$ ako je $i$ u $p$. $N + UV$ je matrica u kojoj su uklonjeni svi izlazni bridovi vrhova iz $p$.</p>
<p>Izračunajmo međumatricu $I_k + VMU$:
$$(VMU)_{i,j} = \sum V_{i,k_1} M_{k_1,k_2} U_{k_2,j} = \sum W_{p_i,k_1} M_{k_1,p_j} = \sum (I_{p_i,k} - N_{p_i,k}) M_{k,p_j}.$$
Po definiciji inverza $\sum N_{p_i,k} M_{k,p_j} = [i = j]$, pa se $(I + VMU)_{i,j}$ pojednostavljuje u $M_{p_i,p_j}$.</p>
<p>Nadalje, $(MU)_{s,i} = \sum_k M_{s,k} U_{k,i} = M_{s,p_i}$, a $(VM)_{j,t} = \sum_k V_{j,k} M_{k,t} = \sum_k (I - N)_{p_j,k} M_{k,t} = M_{p_j,t} - [p_j = t]$. No $p_j \ne t$, pa je to $M_{p_j,t}$.</p>
<p>Zaključno, neka je $P_{i,j} = M_{p_i,p_j}$; $s$ dostiže $t$ ako i samo ako
$$M_{s,t} \ne \sum M_{s,p_i} P^{-1}_{i,j} M_{p_j,t}.$$</p>
<p>Za svaki upit računamo inverz međumatrice u $O(k_1^3)$ i odgovaramo na svaki par u $O(k_1^2)$. Složenost je $O\left(n^3 + q k_1^3 + (\sum k_2) k_1^2\right)$.</p>
''',
},
{
    'letter': 'H',
    'title': 'Hard Problem',
    'title_hr': 'Težak zadatak',
    'slug': 'H_hard_problem',
    'tl': '2 s',
    'ml': '1024 MB',
    'statement': r'''
<p>Zadan je niz nenegativnih cijelih brojeva $a_1, \dots, a_n$. Dopuštene su tri operacije: odabrati interval $[l, r]$ i smanjiti za 1 sve brojeve u njemu; samo one na neparnim indeksima; samo one na parnim indeksima. Ispiši najmanji broj operacija da svi brojevi postanu $0$.</p>
<h3>Ulaz</h3>
<p>$T \le 10$ testova; u svakom $n \le 10^5$ i $a_i \le 10^9$.</p>
<h3>Izlaz</h3>
<p>Za svaki test jedan broj.</p>
''',
    'hints': [
        r'''
<p>LP formulacija: minimiziraj broj operacija uz pokrivenost točno $a_i$; dual: dodijeli $y_i \in \{-1,0,1\}$ tako da zbroj $y$ po svakom intervalu (punom, neparnom ili parnom „s prazninama”) bude $\le 1$, maksimiziraj $\sum a_i y_i$. Optimum LP-a je cjelobrojan.</p>
''',
        r'''
<p>DP nad dualom: stanje $(i, j, k, l)$ gdje su $j, k, l \in \{0, 1\}$ (ili mali) maksimalni sufiksni zbrojevi za tri tipa intervala; prijelaz bira $y_{i+1}$. Alternativa: pohlepno održavanje broja otvorenih punih/parnih/neparnih intervala uz trik „zatvori $k$ i besplatno otvori $k$”.</p>
''',
    ],
    'coach': [
        ('Opažanje 1: samo dvije susjedne pozicije komuniciraju',
         r'''
<p>Operacija „s prazninama” pokriva svaku drugu poziciju: puni interval = neparni + parni interval istog raspona. Dakle operacije su intervali u tri „trake”: puna, samo neparni indeksi, samo parni indeksi, s pravilom da puna vrijedi jedan potez a pokriva obje trake — to sparivanje je izvor težine.</p>
'''),
        ('Opažanje 2: dualnost daje čist kombinatorni problem',
         r'''
<p>Primal: pokriveni multiskup intervala, minimalan broj. Dual: težine $y_i$ s ograničenjem $\sum_{i \in I} y_i \le 1$ za svaki od tri tipa intervala; maksimiziraj $\sum a_i y_i$. Optimum je cjelobrojan (službeno rješenje dokaz ostavlja čitatelju); ograničenje na $\{-1,0,1\}$ jer bi $y_i \lt -1$ mogli podići na $-1$ bez kršenja (zbroj se mijenja za najviše $+1$ tamo gdje je bio $\le 0$).</p>
'''),
        ('Redukcija: DP po sufiksnim zbrojevima',
         r'''
<p>Uvjet „svaki interval tipa $T$ ima zbroj $\le 1$” $\iff$ maksimalni sufiksni zbroj tipa $T$ na svakom prefiksu je $\le 1$. Sufiksni maksimumi su iz $\{0, 1\}$ nakon ograničavanja (Kadaneov trik: $\max(0, \text{prev} + y_i)$ za punu traku; za parnu/neparnu traku prev je zbroj do $i-2$). Stanje $(i, m_{\text{full}}, m_{\text{odd}}, m_{\text{even}})$ — $O(n)$ stanja, 3 izbora za $y$.</p>
'''),
        ('Alternativa: pohlepno',
         r'''
<p>Slijeva održavaj $z$ otvorenih punih i $b$ otvorenih intervala s prazninama koji dosežu $i$; ako $z + b \gt a_i$, zatvori $k = z + b - a_i$ od svakog tipa i besplatno otvori $k$ novih od $i$ (netto $-k$) — odgađanje odluke koje se zatvaraju. Rubni slučajevi kad $z \lt k$ ili $b \lt k$. Također $O(n)$, ali delikatnije.</p>
'''),
    ],
    'solution': r'''
<p>Zadatak se može riješiti na više načina.</p>
<h3>Prvi pristup — dual linearnog programiranja</h3>
<p>Postoji više načina odabira intervala (uključujući „intervale s prazninama“); označimo ih $I_1, \dots, I_m$. Neka je $x_j$ broj operacija na intervalu $I_j$. Uvjet je da za svaki $i$ ($1 \le i \le n$) vrijedi $\sum_{j : i \in I_j} x_j = a_i$, a minimiziramo $\sum x_j$. Rješenje ovog linearnog programa je cjelobrojno (dokažite sami).</p>
<p>Dual: $\sum_{j \in I_i} y_j \le 1$ za svaki interval, a maksimiziramo $\sum_{i=1}^{n} y_i a_i$; $y_j$ smiju biti negativni. I ovo rješenje je cjelobrojno. Kombinatorno značenje: svakoj poziciji dodjeljujemo težinu tako da zbroj težina svakog intervala ne prelazi $1$.</p>
<p>Uočimo da je $y_i \in \{-1, 0, 1\}$: ako je $y_i &lt; -1$, promijenimo ga u $-1$ — kako je zbroj svakog intervala najviše $1$, zbroj intervala koji sadrži $y_i$ i dalje je najviše $1 + (-1) + 1 = 1$.</p>
<p>Neka je $dp_{i,j,k,l}$ najveći zbroj $a_i y_i$ ako smo popunili prvih $i$ elemenata, a $j, k, l$ su najveći sufiksni zbrojevi do $i$ za uzastopni interval / interval s neparnim prazninama / interval s parnim prazninama. Nabrajamo vrijednost $y_{i+1}$ i ažuriramo ta tri zbroja.</p>
<p>Složenost $O(n)$.</p>
<h3>Drugi pristup — pohlepno</h3>
<p>Treba odabrati intervale i intervale s prazninama tako da pozicija $i$ bude pokrivena točno $a_i$ puta za svaki $i$.</p>
<p>Počnimo s prvim dvjema pozicijama $a_1, a_2$:</p>
<ul>
    <li>$a_1 &gt; 0$, $a_2 &gt; 0$: počinjemo $\min(a_1, a_2)$ intervala;</li>
    <li>$a_1 &gt; 0$, $a_2 = 0$: počinjemo $a_1$ intervala s prazninama;</li>
    <li>$a_1 = 0$, $a_2 &gt; 0$: preskačemo prvu poziciju.</li>
</ul>
<p>Na poziciji $i$ postoji $z$ nezatvorenih intervala i $b$ nezatvorenih intervala s prazninama koji dosežu $i$.</p>
<p>Ako je $z + b \le a_i$, oduzmemo $z + b$ od $a_i$ i produljimo te intervale.</p>
<p>Ako je $z + b &gt; a_i$, treba zatvoriti $z + b - a_i$ intervala, ali ne znamo koje — to može ovisiti o kasnijim pozicijama. Neka je $k = z + b - a_i$. Zatvorimo $k$ intervala i $k$ intervala s prazninama (možda je nemoguće zatvoriti $k$ intervala — vidjet ćemo kako to riješiti), a zatim od pozicije $i$ besplatno pokrenemo $k$ intervala obaju tipova. Dakle $a_i$ uvećamo za $k$, a odgovor umanjimo za $k$, jer ćemo iz $a_i$ pokrenuti $k$ intervala više, ali besplatno.</p>
<p>Ako je $z$ ili $b$ manji od $k$, možda je nemoguće zatvoriti $k$ intervala. Ako je $z &lt; k$, tj. $z &lt; z + b - a_i$, tj. $a_i &lt; b$, uvijek moramo zatvoriti $b - a_i$ intervala s prazninama i tada je $k' = z$. Taj slučaj nije teško obraditi; slično za $b &lt; k$.</p>
<p>Zadatak time rješavamo u $O(n)$. Redoslijed pohlepnih koraka pomalo je delikatan: pri obradi $a_i, a_{i+1}$ treba oduzeti intervale s prazninama koji dosežu $a_{i+1}$ i osigurati da dodatnih $k$ dodanih $a_i$ ne „potroše“ prethodni intervali. Za pojašnjenje autor upućuje na kod izvornog članka.</p>
''',
},
{
    'letter': 'I',
    'title': 'Interval Problem',
    'title_hr': 'Zadatak o intervalima',
    'slug': 'I_interval_problem',
    'tl': '2 s',
    'ml': '1024 MB',
    'statement': r'''
<p>Zadano je $n$ intervala $[l_i, r_i]$; intervali koji se sijeku spojeni su neusmjerenim bridom. Neka je $d(i, j)$ duljina najkraćeg puta između intervala $i$ i $j$ ($0$ ako put ne postoji). Za svaki $i$ ispiši $\sum_{j=1}^{n} d(i, j)$.</p>
<h3>Ulaz</h3>
<p>$n \le 2 \times 10^5$ i intervali s različitim krajevima $1 \le l_i &lt; r_i \le 2n$.</p>
<h3>Izlaz</h3>
<p>$n$ redaka.</p>
''',
    'hints': [
        r'''
<p>Sortiraj po $r$. Najkraći put od $j$ do $i$ ($r_j \lt r_i$): iz $j$ pohlepno skoči na interval koji siječe $j$ i ima najveći $r$ — to definira stablo („roditelj = najdesniji presjecatelj”).</p>
''',
        r'''
<p>Za fiksni $i$, intervali lijevo od njega imaju udaljenost = dubina u tom stablu relativno prema skupu susjeda $i$ (susjedi 1, njihova djeca 2, …). Simetrično za intervale desno (stablo po $l$). Intervali koji sadrže $i$ imaju udaljenost 1. Zbrojevi po podstablima daju $O(n\log n)$.</p>
''',
    ],
    'coach': [
        ('Opažanje 1: intervalni graf i pohlepni skok',
         r'''
<p>Intervalni grafovi imaju „pohlepne” najkraće puteve: da bi se od $j$ došlo dalje udesno, najbolje je uvijek preskočiti na susjeda s najvećim $r$. Definiraj $par(j)$ = interval s najvećim $r$ među onima koji sijeku $j$ (i $r \gt r_j$); to je šuma, a udaljenost od $j$ do bilo kojeg $i$ s $r_i \gt r_j$ dobiva se penjanjem po $par$ do prvog pretka koji siječe $i$, plus 1.</p>
'''),
        ('Opažanje 2: obrni smjer — zbroj po $j$ za fiksno $i$',
         r'''
<p>Za fiksno $i$: skup $S_1$ = intervali koji sijeku $i$ i imaju $r \lt r_i$ (udaljenost 1); $S_2$ = djeca čvorova iz $S_1$ u $par$-stablu koja nisu u $S_1$ (udaljenost 2); itd. Dakle za $j$ lijevo od $i$: $d(i,j) = 1 + (\text{dubina}(j) - \text{dubina}(\text{prvog pretka od } j \text{ koji siječe } i))$. Zbroj po $j$ preko podstablovnih zbrojeva dubina, uz prefiksne zbrojeve po sortiranim $r$.</p>
'''),
        ('Opažanje 3: simetrija i sadržavanje',
         r'''
<p>Isto napravi po $l$ (zrcali koordinate) za intervale desno od $i$. Intervali koji sadrže $i$ ($l_j \lt l_i$, $r_j \gt r_i$) su susjedi — udaljenost 1; broj takvih preko BIT-a. Ne broji dvaput: podijeli $j$-ove po $r_j \lt r_i$ / $l_j \gt l_i$ / sadržava $i$ (disjunktno jer su krajevi različiti i graf je intervalni).</p>
'''),
        ('Složenost',
         r'''
<p>Sortiranje + BIT + DP na dva stabla: $O(n\log n)$. Nepovezan graf: obradi svaku komponentu (interval-uniju) zasebno.</p>
'''),
    ],
    'solution': r'''
<p>Bez smanjenja općenitosti $r_1 &lt; r_2 &lt; \dots &lt; r_n$ i graf je povezan (inače odgovor računamo za svaku komponentu zasebno).</p>
<p>Najprije: kako izračunati udaljenost od intervala $j$ do intervala $i$ ($j &lt; i$)? Iz $j$ pohlepno skačemo na interval koji siječe $j$ i ima najdesniji kraj, dok ne dosegnemo $i$.</p>
<p>Tu se vidi struktura stabla: roditelj intervala $i$ je najdesniji interval koji ga siječe.</p>
<p>Udaljenost od $i$ do svih intervala $j$ s $r_j &lt; r_i$: za sve intervale koji sijeku $i$ udaljenost je $1$, za njihovu djecu $2$ itd. Odgovor dobivamo nečim poput DP-a na stablu i kumulativnih zbrojeva u $O(n)$.</p>
<p>Udaljenosti od $i$ do svih $j$ s $l_j &gt; l_i$ računamo na isti način. Za svaki interval s $l_j &lt; l_i$ i $r_j &gt; r_i$ odgovor je uvijek $1$.</p>
<p>Ukupno $O(n \log n)$.</p>
''',
},
{
    'letter': 'J',
    'title': 'Junk Problem',
    'title_hr': 'Bezvezni zadatak',
    'slug': 'J_junk_problem',
    'tl': '2 s',
    'ml': '1024 MB',
    'statement': r'''
<p>Zadana je mreža $n \times m$ u kojoj su bridovi usmjereni ($(x, y) \to (x + 1, y)$ i $(x, y) \to (x, y + 1)$), osim $k$ vodoravnih bridova koji su dvosmjerni (nikoja dva ne dijele vrh). Traži se $l$ vršno disjunktnih jednostavnih puteva od $(1, a_i)$ do $(n, b_i)$. Dvosmjerni brid je <i>loš</i> ako nijedan njegov kraj ne posjećuje nijedan put. Prebroji skupove $l$ vršno disjunktnih puteva bez loših bridova, modulo $998244353$.</p>
<h3>Ulaz</h3>
<p>$n, m \le 100$, $l \le 50$, $k \le 50$, nizovi $a$ i $b$ (strogo rastući) te $k$ dvosmjernih bridova.</p>
<h3>Izlaz</h3>
<p>Jedan broj — odgovor.</p>
''',
    'hints': [
        r'''
<p>Bez dvosmjernih bridova: LGV lema — $\det[\#\text{puteva}(a_i \to b_j)]$ jer u ovoj mreži nesijekući putevi odgovaraju samo identitetu (a, b rastući).</p>
''',
        r'''
<p>Uz dvosmjerne bridove težine $x$ koristi Talaskinu formulu (LGV s ciklusima): $\det M \cdot (1-x^2)^k = \sum_{\text{disjunktni putevi}} x^{\#\text{prijeđenih}}(1-x^2)^{\#\text{neposjećenih}}$. Traženi odgovor je vrijednost u $x = 1$ polinoma stupnja $\le 2k$: izračunaj u $2k+1$ točaka $x = 2, \dots, 2k+2$ i interpoliraj.</p>
''',
    ],
    'coach': [
        ('Opažanje 1: LGV i zašto ne radi izravno',
         r'''
<p>LGV zbraja po sustavima puteva s predznakom permutacije; u planarnoj DAG mreži s rastućim $a$, $b$ sijeku se svi osim identitetskog rasporeda, pa $\det$ broji disjunktne sustave. Dvosmjerni bridovi uvode cikluse (šetnje mogu oscilirati) i graf više nije DAG: obični LGV ne vrijedi.</p>
'''),
        ('Opažanje 2: Talaska — LGV za grafove s ciklusima',
         r'''
<p>Za težinske grafove s ciklusima $\det M$ (gdje $M_{ij}$ = zbroj težina svih šetnji, kao formalni red) $=$ (zbroj po kolekcijama nesijekućih puteva i vršno disjunktnih ciklusa) / (zbroj po kolekcijama disjunktnih ciklusa). Ovdje su jedini ciklusi „tamo-vamo” po dvosmjernom bridu, težine $x^2$, na $k$ disjunktnih bridova: nazivnik je $(1-x^2)^{-k}$, a ciklusi u brojniku smiju sjediti samo na neposjećenim bridovima — otud faktor $(1-x^2)^{\#\text{neposjećenih}}$ nakon množenja.</p>
'''),
        ('Opažanje 3: uvrsti $x = 1$ tek na kraju',
         r'''
<p>Traži se $\sum_{\text{putevi bez loših bridova}} 1$, tj. kolekcije gdje je svaki dvosmjerni brid posjećen (posjet kraja, ne nužno prelazak). Talaskin polinom pri $x = 1$ ubija članove s neposjećenim bridom ($(1-1)^{\gt 0} = 0$) i daje $1^{\#\text{prijeđenih}}$ — točno traženi broj. Ali $1/(1-x^2)$ pri $x = 1$ nije definirano u međukoracima: evaluiraj u $2k+1$ drugih točaka i interpoliraj polinom stupnja $\le 2k$.</p>
'''),
        ('Algoritam i složenost',
         r'''
<p>Za svaki $x \in \{2..2k+2\}$: DP po mreži za zbroj težina šetnji (dvosmjerni brid: lokalni geometrijski red $1/(1-x^2)$ ugrađen u prijelaz), matrica $l\times l$, determinanta $O(l^3)$, pomnoži s $(1-x^2)^k$. Ukupno $O(k\,(nm\,l + l^3))$, tj. oko $O(n^3 k)$ prema službenom.</p>
'''),
    ],
    'solution': r'''
<p>Bez dvosmjernih bridova zadatak se rješava LGV-lemom: neka je $M_{i,j}$ broj puteva od $(1, a_i)$ do $(n, b_j)$; odgovor je determinanta te matrice.</p>
<p>Za opći graf koristimo <b>Talaskinu formulu</b> (preporučujemo pročitati izvorni rad). Kratka ideja: za svaki dvosmjerni brid dodamo dva usmjerena brida težine $x$. Broj puteva između dvaju vrhova zamijenimo zbrojem težina svih puteva; puteva može biti beskonačno mnogo (npr. beskonačno hodanje po dvosmjernom bridu), a zbroj je $1 + x^2 + x^4 + \dots = \frac{1}{1 - x^2}$. Zbroj svih puteva zato je formalni red potencija, ali kako ćemo kasnije uvrštavati konkretne vrijednosti $x$, zbroj i dalje računamo jednostavnim DP-om.</p>
<p>Po Talaskinoj formuli determinanta nove matrice jednaka je zbroju po kolekcijama nesijekućih, samo-nesijekućih puteva i ciklusa, podijeljenom zbrojem po kolekcijama nesijekućih ciklusa. Konkretno, $\det(M) \times (1 - x^2)^k$ jednako je
$$\sum_{\text{svi disjunktni jednostavni putevi}} x^{\#\text{prijeđenih dvosmjernih bridova}} (1 - x^2)^{\#\text{neposjećenih dvosmjernih bridova}}.$$
To je polinom stupnja najviše $2k$. Uvrštavanjem $x = 1$ dobivamo odgovor, no ne možemo izravno uvrstiti $1$ jer nazivnik tijekom računanja može biti $0$. Zato uvrstimo $x = 2, 3, \dots, 2k + 2$ i polinom dobijemo interpolacijom.</p>
<p>Složenost $O(n^3 k)$.</p>
''',
},
{
    'letter': 'K',
    'title': 'Knapsack Problem',
    'title_hr': 'Zadatak o naprtnjači',
    'slug': 'K_knapsack_problem',
    'tl': '2 s',
    'ml': '1024 MB',
    'statement': r'''
<p>Zadano je $2^k - 1$ brojeva $c_1, \dots, c_{2^k - 1}$ i $k$ brojeva $a_0, \dots, a_{k-1}$. Pronađi nenegativne cijele $x_1, \dots, x_{2^k - 1}$ takve da za svaki $j$ ($0 \le j &lt; k$) vrijedi
$$\sum_{i=1}^{2^k - 1} \left(\lfloor i / 2^j \rfloor \bmod 2\right) x_i = a_j$$
i da je $\sum x_i c_i$ najveći mogući.</p>
<h3>Ulaz</h3>
<p>$T \le 100$ testova; u svakom $k$ ($2 \le k \le 4$), $c_i \le 10^8$, $1 \le a_i \le 10^9$.</p>
<h3>Izlaz</h3>
<p>Za svaki test jedan broj.</p>
''',
    'hints': [
        r'''
<p>To je $k$-dimenzionalna neograničena naprtnjača s jednakostima ($k \le 4$, kapaciteti do $10^9$). Predmet $i$ je bitmaska koja dodaje 1 svakoj dimenziji iz maske. Klasični DP po volumenu ne dolazi u obzir.</p>
''',
        r'''
<p>Znamenkasti DP po bitovima od najvišeg: odlučuj bit $b$ svakog $x_i$; preostali volumen u svakoj dimenziji, izražen u jedinicama $2^b$, ostaje malen (ako je $\gt 15$, ne može se popuniti nižim bitovima). Uz zamjenske argumente (u optimumu se pri jednom bitu koristi $\le 5$ različitih maski) granica pada na $\approx 9$, stanje $\le 10^4$.</p>
''',
    ],
    'coach': [
        ('Opažanje 1: ILP je mali po dimenziji, velik po volumenu',
         r'''
<p>Nepoznanica je $15$ (za $k=4$), ograničenja $4$, ali $a_j \le 10^9$. Rješenje LP relaksacije + zaokruživanje nije garantirano; treba egzaktnu strukturu: bitovi od $x_i$.</p>
'''),
        ('Opažanje 2: bit-po-bit s ograničenim prijenosom',
         r'''
<p>Zapiši $x_i = \sum_b x_{i,b}2^b$. Zbroj po dimenziji $j$: $\sum_b 2^b \sum_{i \ni j} x_{i,b} = a_j$. Obrađuj bitove od najvišeg: nakon odluke bitova $\ge b$, preostali $rem_j = a_j - \sum_{b' \ge b} 2^{b'}(\cdots)$ mora biti nenegativan i ostvariv s bitovima $\lt b$: najviše $8$ maski sadrži $j$, svaka doprinosi $\le 2^b - 1$, pa $rem_j \lt 8\cdot 2^b$; službeno rješenje reže pri $rem_j/2^b \gt 15$. Stanje: vektor od 4 malih brojeva.</p>
'''),
        ('Opažanje 3: zamjenski argument smanjuje stanja',
         r'''
<p>Ako su na istom bitu odabrane maske $S$ i $T$, možemo ih zamijeniti s $S\cap T$ i $S \cup T$ (isti zbroj po dimenzijama) — jedno od toga ne pogoršava cilj, pa optimum bira maske koje čine lanac; lanac u $\{0,1\}^4$ ima $\le 5$ članova (uključujući razmatranje parova), što spušta granicu $rem_j/2^b$ na $9$, dovoljno za $O(\log W \cdot 10^4 \cdot 15)$ po testu.</p>
'''),
        ('Algoritam',
         r'''
<p>DP od najvišeg bita ($\approx 30$): stanje $(r_0..r_3)$, $r_j \le 9$; prijelaz: za svaku masku odluči $x_{i,b} \in \{0,1\}$ (ili $\le$ granice) — enumeracija lanaca maski; nova stanja $2(r_j) + \text{bit}(a_j, b) - \#\{i \ni j : x_{i,b}=1\}$. Cilj: $\max \sum c_i x_i$ akumulirano s $2^b$. Odgovor u stanju $(0,0,0,0)$ nakon bita $0$.</p>
'''),
    ],
    'solution': r'''
<p>Zadatak se može riješiti linearnim programiranjem pa nabrajanjem zaokruživanja, kopiranjem ILP-rješavača ili heuristikama — ali to nije zamišljeno rješenje.</p>
<p>Zamišljeno rješenje je <b>znamenkasti DP</b>. Zadatak je u biti četverodimenzionalna naprtnjača; izravno rješavanje bilo bi barem $O(W^4)$, što je neprihvatljivo.</p>
<p>Umjesto toga vrijednosti $x_i$ fiksiramo bit po bit, od najvišeg prema najnižem, i bilježimo preostali volumen u četiri dimenzije. Ako je prije razmatranja $b$-tog bita preostali volumen neke dimenzije veći od $15$ (stvarni volumen je $15 \times 2^b + a_i \bmod 2^b$), ne može se popuniti ni ako za sve preostale bitove stavimo $x_i = 2^b - 1$. Tako dobivamo rješenje u $O(\log W \times 16^4)$, koje se zbog velike konstante teško uklapa u vremensko ograničenje.</p>
<p>Granica $15$ nije stroga. Primjerice, ako su brojevi podskupova $1, 1234, 12, 134$ pozitivni, uvijek se parovi $(1, 1234)$ i $(12, 134)$ mogu smanjiti odnosno povećati bez smanjenja odgovora. Dakle u optimalnom rješenju pri jednom bitu koristimo najviše 5 skupova, a gornja granica preostalih volumena spušta se na $9$, što je dovoljno za prolaz.</p>
<p>Suptilnijom analizom i stres-testom granica se može spustiti i na $7$.</p>
''',
},
{
    'letter': 'L',
    'title': 'Linear Congruential Generator Problem',
    'title_hr': 'Zadatak o linearnom kongruentnom generatoru',
    'slug': 'L_linear_congruential_generator_problem',
    'tl': '2 s',
    'ml': '1024 MB',
    'statement': r'''
<p>Zadani C++ kod generira pseudoslučajnu permutaciju: LCG $x \leftarrow (x \cdot a + b) \bmod p$, a permutacija se gradi tako da se za $i = 1..n$ postavi $perm[i] = i$ i zamijeni $perm[i]$ s $perm[\mathrm{rand}() \bmod i + 1]$. Zadani su $n, a, b, p$ i izlazna permutacija; pronađi početni $x$ ($0 \le x &lt; p$).</p>
<h3>Ulaz</h3>
<p>$n = 10^5$, permutacija, te $a, b, p$ ($2 \le a &lt; p$, $0 \le b &lt; p$, $500 \le p \le 10^{16}$, $p$ prost; $a, b, x$ uniformno slučajni).</p>
<h3>Izlaz</h3>
<p>Jedan $x$.</p>
''',
    'hints': [
        r'''
<p>Iz permutacije rekonstruiraš $r_i = \mathrm{rand}_i \bmod i$ za svaki $i$ (obrni zamjene unatrag). $\mathrm{rand}_i = (a_i \cdot seed + b_i) \bmod p$ gdje su $a_i = a^i$, $b_i$ iz kompozicije LCG-a — dobivaš $n$ jednadžbi $((a_i\,seed + b_i)\bmod p) \bmod i = r_i$.</p>
''',
        r'''
<p>Iz jednadžbe za $i = M_1 \approx n/2$: $x = M_1 t + c$, $t \le p/M_1$. Uvrsti u drugu jednadžbu i biraj $a_{M_2}$ tako da $k_1 = a_{M_2}M_1 \bmod p$ bude malen ($O(p/n)$); onda je kvocijent $q = \lfloor (k_1 t + k_2)/p \rfloor = O(p/n^2) \le 10^6$ — nabroji $q$ i riješi linearnu kongruenciju mod $M$ za $t$. Alternativa: svedi na zadatak C (LWE).</p>
''',
    ],
    'coach': [
        ('Opažanje 1: izvuci izlaz generatora',
         r'''
<p>Postupak je Fisher–Yates unaprijed: $perm[i] \leftrightarrow perm[\mathrm{rand}_i \bmod i + 1]$. Obrni petlju od $i = n$ prema $1$: pozicija na kojoj se nalazi $i$ (ili trag zamjene) daje $\mathrm{rand}_i \bmod i$. Tako iz $O(n)$ znamo „malo bitova” svakog izlaza.</p>
'''),
        ('Opažanje 2: LCG je afin u sjemenu',
         r'''
<p>$x_i = a x_{i-1} + b$ daje $x_i = a^i seed + b\frac{a^i - 1}{a - 1} \pmod p$: svaka jednadžba je $((\alpha_i\,seed + \beta_i)\bmod p) \bmod i = r_i$. Jedna jednadžba s velikim $i$ ostavlja $\approx p/i \approx 10^{11}$ kandidata — previše za brute force, ali pretraživanje u dvije razine spašava.</p>
'''),
        ('Opažanje 3: dvije jednadžbe, mali kvocijent',
         r'''
<p>Parametriziraj $x = M_1 t + c$ ($t \lt p/M_1$). Druga jednadžba: $((k_1 t + k_2) \bmod p) \bmod M = r_M$. Ako izaberemo $M_2$ tako da je $k_1 = \alpha_{M_2} M_1 \bmod p$ malen ($\approx p/n$ — među $n/2$ kandidata $M_2$ očekujemo takav), onda $k_1 t + k_2 \lt p^2/n^2 \cdot O(1)$, pa je „kvocijent” $q \lt O(p/n^2) \approx 10^6$. Za svaki $q$: $(k_1 t + k_2 - qp) \equiv r_M \pmod M$ — linearna kongruencija u $t$ na intervalu duljine $p/k_1 \approx n$, ima $O(n/M) = O(1)$ rješenja.</p>
'''),
        ('Algoritam',
         r'''
<p>Izračunaj $\alpha_i, \beta_i$ ($O(n)$), $r_i$ obrtanjem permutacije, izaberi $M_1 = n/2$ i $M_2$ s najmanjim $k_1$; za $q = 0..O(p/n^2)$ riješi kongruenciju (inverz $k_1$ mod $M$ ako je $\gcd = 1$, inače proširena verzija), za svako $t$ rekonstruiraj $seed$ i provjeri na nekoliko drugih jednadžbi. $O(p/n^2 + n)$ s <code>__int128</code>.</p>
'''),
    ],
    'solution': r'''
<h3>Prvo rješenje</h3>
<p>Iz permutacije možemo saznati rezultat $\mathrm{RNG} \bmod i$ nakon $i$-tog poziva. Kako je riječ o linearnom kongruentnom generatoru, dobivamo jednadžbe $((a_i \times seed + b_i) \bmod p) \bmod i = c_i$.</p>
<p>Rješavamo iz dviju jednadžbi. Odaberemo prvu jednadžbu $M_1$ (pokazat će se da je $M_1 = n/2$ dovoljno dobro) i neka je $x = (a_{M_1} \times seed + b_{M_1}) \bmod p$. Iz $x \bmod M_1 = c_{M_1}$ slijedi $x = M_1 t + c_{M_1}$, gdje je $t \le p / M_1$, tj. otprilike $O(p/n)$.</p>
<p>Zatim odaberemo drugu jednadžbu $M = M_1 + M_2$: $((a_{M_2} \times x + b_{M_2}) \bmod p) \bmod M = c_M$. Uvrstimo $x$ i dobijemo $((a_{M_2}(M_1 t + c_{M_1}) + b_{M_2}) \bmod p) \bmod M = c_M$, što označimo $((k_1 t + k_2) \bmod p) \bmod M = c_M$ — linearna kongruencija u $t$.</p>
<p>Pažljivo biramo $a_{M_2}$ tako da $k_1 = a_{M_2} M_1 \bmod p$ bude što manji, otprilike $O(p/n)$. Tada je $k_1 t + k_2$ reda $O(p^2/n^2)$. Neka je $q = \lfloor (k_1 t + k_2) / p \rfloor$; tada je $q$ reda $O(p/n^2)$ i $(k_1 t + k_2) \bmod p = k_1 t + k_2 - qp$.</p>
<p>Nabrajamo $q$ i rješavamo $(k_1 t + k_2 - qp) \bmod M = c_M$ za $t$ u rasponu određenom s $qp \le k_1 t + k_2 &lt; (q + 1) p$. Za svaki $q$ postoji oko $O(p / k_1 / M) = O(1)$ rješenja, pa sve mogućnosti provjerimo grubom silom; pogrešan $t$ odbacuje se u $O(1)$.</p>
<p>Složenost $O(p/n^2 + n)$.</p>
<h3>Drugo rješenje</h3>
<p>(Zahvala @toxicpie.) Imamo niz jednadžbi $((a_i x + b_i) \bmod p) \bmod i = p_i$. Uzmimo sve $i$ s $i \bmod 1000 = 0$; dobivamo 100 jednadžbi $((a_i x + b_i) \bmod p) \bmod 1000 = c_i$, tj. $(a_i x + b_i) \bmod p = 1000 k_i + c_i$ za neke $0 \le k_i \le p/1000$, pa
$$\frac{a_i}{1000} \times x - k_i \equiv \frac{c_i - b_i}{1000} \pmod p,$$
što je upravo zadatak C.</p>
''',
},
{
    'letter': 'M',
    'title': 'Minimum Element Problem',
    'title_hr': 'Zadatak o najmanjem elementu',
    'slug': 'M_minimum_element_problem',
    'tl': '2 s',
    'ml': '1024 MB',
    'statement': r'''
<p>Permutacije $p$ i $q$ duljine $n$ ekvivalentne su ako za svaki par $(i, j)$, $1 \le i \le j \le n$, indeks minimuma od $p_i, \dots, p_j$ i od $q_i, \dots, q_j$ isti. Za zadane $x$ i $y$ promotri sve permutacije s $p_x = y$; koliko ih najviše možeš odabrati tako da nikoje dvije nisu ekvivalentne? Ispiši odgovor modulo $998244353$ za svaki $y = 1, \dots, n$.</p>
<h3>Ulaz</h3>
<p>$n, x$ ($1 \le n \le 5 \times 10^5$, $1 \le x \le n$).</p>
<h3>Izlaz</h3>
<p>$n$ redaka — odgovori za $y = 1, \dots, n$.</p>
''',
    'hints': [
        r'''
<p>Ekvivalencija „isti indeks minimuma na svakom intervalu” $\iff$ isto kartezijevo stablo (po minimumu). Bez ograničenja klasa je $C_n$ (Catalan). Uvjet $p_x = y$ isključuje stabla u kojima je dubina $x$ veća od $y$ ili veličina podstabla $x$ veća od $n+1-y$ — i ta dva kršenja ne mogu nastupiti zajedno.</p>
''',
        r'''
<p>Broj stabala s dubinom($x$) $= d$: put do korijena isprepliće $p$ „lijevih” i $q$ „desnih” predaka, $p+q = d-1$; zbroj po pozicijama daje $k$-tu konvoluciju Catalanovih brojeva (zatvoreni oblik), pa $\sum_{p+q=d-1}\binom{p+q}{p}L_pR_q$ — konvolucija. Broj stabala s podstablom($x$) veličine $s$: $\sum_{p+q=s-1}C_pC_q\cdot C_{n-s}$ (sažmi podstablo u list; „$k$-ti vrh je list” daje $C_{n-1}$ neovisno o $k$). Sve u $O(n\log n)$ NTT-om.</p>
''',
    ],
    'coach': [
        ('Opažanje 1: prevedi na kartezijeva stabla',
         r'''
<p>Indeks minimuma svakog intervala određuje rekurzivno korijen i podstabla — to je kartezijevo stablo; obrat isto. Klase ekvivalencije = binarna stabla s in-order $1..n$: $C_n$ komada, svako ostvarivo permutacijom (npr. dodjela vrijednosti po BFS-u/dubini).</p>
'''),
        ('Opažanje 2: što $p_x = y$ zahtijeva od stabla',
         r'''
<p>$x$ mora biti veći od svih predaka (ima ih dubina$-1$) i manji od svih potomaka (ima ih $|sub(x)|-1$); uz $p_x = y$ točno je $y - 1$ manjih i $n - y$ većih vrijednosti. Uvjet: dubina $\le y$ i $|sub(x)| \le n + 1 - y$ — i dovoljno je (ostale vrijednosti rasporedi slobodno). Kršenja se isključuju (preci + potomci + $x$ bi prešli $n$), pa je odgovor $C_n - \#\{\text{dubina} \gt y\} - \#\{|sub| \gt n+1-y\}$.</p>
'''),
        ('Opažanje 3: brojanje po dubini',
         r'''
<p>Preci od $x$ dijele se na lijeve ($l_1 \lt \dots \lt l_p \lt x$) i desne; segmenti između uzastopnih lijevih predaka nezavisno tvore stabla ($C_{\text{duljina}}$), isprepletanje $\binom{p+q}{p}$. $L_p = \sum_{l} \prod C_{l_i - l_{i-1} - 1}$ = koeficijent u $C(z)^{p}$ pomaknut — $p$-struka konvolucija Catalana ima zatvoren oblik $\frac{p}{2m+p}\binom{2m+p}{m}$-tipa (izvedi iz Lagrangeove inverzije). Onda konvolucija $L$ i $R$ s binomnim faktorom (EGF-stil) daje sve dubine odjednom.</p>
'''),
        ('Opažanje 4: brojanje po veličini podstabla',
         r'''
<p>Sažmi $sub(x)$ u jedan list: broj stabala s $n - s + 1$ vrhova u kojima je zadani vrh list je $C_{n-s}$ (bijekcija, neovisno o poziciji). Unutar podstabla: lijevo $p$, desno $q$ vrhova, $p + q = s - 1$, $C_pC_q$. Sve veličine: konvolucija Catalana sa sobom, puta $C_{n-s}$.</p>
'''),
        ('Složenost',
         r'''
<p>Nekoliko NTT konvolucija duljine $n$ mod $998244353$ — $O(n\log n)$; sufiksni zbrojevi za „$\gt y$”.</p>
'''),
    ],
    'solution': r'''
<p>Dvije permutacije ekvivalentne su ako i samo ako su im kartezijeva stabla jednaka. Ako nijedan element nije fiksiran, odgovor je jednostavno $C_n = \frac{1}{n+1} \binom{2n}{n}$, jer za svako binarno stablo s $n$ vrhova postoji barem jedna permutacija.</p>
<p>Ako je $p_x = y$, dva slučaja postaju nevaljana:</p>
<ul>
    <li>dubina vrha $x$ veća je od $y$, jer $x$ mora biti veći od svih predaka;</li>
    <li>veličina podstabla vrha $x$ veća je od $n + 1 - y$, jer $x$ mora biti manji od svih potomaka.</li>
</ul>
<p>Ta su dva slučaja neovisna: kad bi $x$ kršio oba uvjeta, broj vrhova bio bi veći od $n$.</p>
<p>Zato ih rješavamo zasebno: računamo broj načina da dubina $x$ bude $y$ za $y = 1 \sim n$, i broj načina da veličina podstabla $x$ bude $y$ za $y = 1 \sim n$.</p>
<p><b>Dubina.</b> Promotrimo put od $x$ do korijena. Neka je na njemu $p$ vrhova lijevo od $x$ ($l_1 &lt; l_2 &lt; \dots &lt; l_p$) i $q$ vrhova desno od $x$ ($r_1 &gt; r_2 &gt; \dots &gt; r_q$), uz $l_0 = 0$, $l_{p+1} = x$, $r_0 = n + 1$, $r_{q+1} = x$. Broj načina je
$$\prod_{i=1}^{p} C_{l_i - l_{i-1} - 1} \times \prod_{i=1}^{q} C_{r_{i-1} - r_i - 1} \times \binom{p + q}{p}.$$
Elementi od $l_{i-1} + 1$ do $l_i - 1$ neovisno tvore binarno stablo, pa je broj načina $C_{l_i - l_{i-1} - 1}$; desna je strana slična. Postoji $\binom{p+q}{p}$ načina da se $l$ i $r$ isprepletu u put od $x$ do korijena.</p>
<p>Za fiksni $p$ postoji zatvorena formula (označimo je $L_p$) za $\sum_l \prod_{i=1}^{p} C_{l_i - l_{i-1} - 1}$, tzv. $k$-ta konvolucija Catalanovih brojeva, oblika otprilike $\frac{k+1}{n+k+1} \binom{2n+k}{n}$.</p>
<p>Dakle, ako je dubina $x$ jednaka $y$, broj načina je $\sum_{p+q = y-1} L_p \times R_q \times \binom{p+q}{p}$ — jednostavna konvolucija.</p>
<p><b>Podstablo.</b> Sve vrhove podstabla sažmemo u jedan vrh, koji je list. Podzadatak: broj binarnih stabala s $n$ vrhova u kojima je $k$-ti vrh list. Iznenađujuće, odgovor je $C_{n-1}$, neovisno o $k$: bijekcija se dobije uklanjanjem tog lista iz stabla s $n$ vrhova i dodavanjem lista na određeno mjesto u stablu s $n - 1$ vrhova.</p>
<p>Ako je veličina lijevog podstabla $x$ jednaka $p$, a desnog $q$, broj načina je $C_p \times C_q \times C_{n-p-q-1}$ — također jednostavna konvolucija.</p>
<p>Zadatak time rješavamo u $O(n \log n)$.</p>
''',
},
]
