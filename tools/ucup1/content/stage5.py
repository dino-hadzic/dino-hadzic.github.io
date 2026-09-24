"""1st Universal Cup – Stage 5: Osijek. Uvezeno iz ručno pisanih stranica (import_legacy.py); naputci i
trenerski koraci iz nekadašnjeg retro_stage5.py."""

STAGE = {
    'no': 5,
    'name': 'Stage 5: Osijek',
    'source_name': 'Osijek Competitive Programming Camp 2023, 25.–26. veljače',
    'source_html': r'''
<p>Prijevod službene analize zadataka (rukom pisane prezentacije s razjašnjenja zadataka): <a href="https://contest.ucup.ac/download.php?type=attachments&amp;id=1111&amp;r=1">Analysis (en)</a>. Tekst zadatka preveden je prema službenim <a href="https://contest.ucup.ac/download.php?type=attachments&amp;id=1111&amp;r=0">engleskim tekstovima zadataka</a>. Zadatak je dostupan na <a href="https://contest.ucup.ac/contest/1111">Universal Cup Judging System</a>.</p>
''',
}

PROBLEMS = [
{
    'letter': 'A',
    'title': 'And Xor Tree',
    'title_hr': 'Stablo AND-a i XOR-a',
    'slug': 'A_and_xor_tree',
    'tl': '5 s',
    'ml': '256 MB',
    'statement': r'''
<p>Zadano je stablo s $n$ čvorova; čvor $i$ ima nenegativnu cjelobrojnu vrijednost $v_i$. Svaki put (od čvora $i$ do čvora $j$) ima <i>and-vrijednost</i> $A_{ij}$ — bitovni AND vrijednosti svih čvorova na putu. Analogno su definirane <i>or-vrijednost</i> $O_{ij}$ i <i>xor-vrijednost</i> $X_{ij}$ (bitovni OR odnosno XOR).</p>
<p>Izračunaj
$$\sum_{i,j} A_{ij}^2, \qquad \sum_{i,j} O_{ij}^2, \qquad \sum_{i,j} X_{ij}^2,$$
gdje svaka suma ide po svih $n^2$ (uređenih) puteva u stablu. Rezultate ispiši modulo $998\,244\,353$.</p>
<h3>Ulaz</h3>
<p>Prvi redak sadrži $n$ ($1 \le n \le 10^5$). Drugi redak sadrži $v_1, \dots, v_n$ ($0 \le v_i &lt; 2^{25}$). Slijedi $n - 1$ redaka s bridovima $a_i$, $b_i$.</p>
<h3>Izlaz</h3>
<p>Ispiši tri cijela broja — zbroj kvadrata svih and-vrijednosti, or-vrijednosti i xor-vrijednosti, svaki modulo $998\,244\,353$.</p>
''',
    'hints': [
        r'''
<p>Kvadrat vrijednosti rastavi po parovima bitova: $X^2 = \sum_{i,j} 2^{i+j}[\text{bit } i][\text{bit } j]$. Za svaki od $25^2$ parova bitova riješi zaseban „da/ne” problem na stablu.</p>
''',
        r'''
<p>AND: zadrži samo čvorove s oba bita — komponenta veličine $s$ daje $s^2$ puteva. OR: komplementarno (čvorovi s oba bita $0$), oduzmi od $n^2$. XOR: DP po stablu s $4$ stanja (parnost bita $i$, parnost bita $j$) po čvoru, spajaj djecu i broji puteve s LCA u čvoru.</p>
''',
    ],
    'coach': [
        ('Opažanje 1: kvadrat kroz parove bitova',
         r'''
<p>$v^2 = \sum_{i,j} 2^{i+j} v_i v_j$. Zato je $\sum A_{uv}^2 = \sum_{i,j} 2^{i+j}\cdot\#\{(u,v) : A_{uv} \text{ ima bitove } i \text{ i } j\}$ — treba prebrojati puteve po svojstvu za $625$ parova bitova (ili $325$ zbog simetrije).</p>
'''),
        ('Opažanje 2: AND i OR su brojanje komponenata',
         r'''
<p>AND puta ima bit $i$ i $j$ $\iff$ svi čvorovi puta imaju oba bita; put leži u komponenti šume induciranoj tim čvorovima. Zbroj $s^2$ po komponentama — DSU ili DFS, $O(n)$ po paru. OR: put nema bit $i$ ni $j$ $\iff$ svi čvorovi imaju oba bita $0$; broj puteva s oba bita $= n^2 - (\text{bez } i) - (\text{bez } j) + (\text{bez oba})$ (uključivanje-isključivanje na komponentama).</p>
'''),
        ('Algoritam: XOR',
         r'''
<p>$dp[v][a][b]$ = broj puteva koji počinju u podstablu od $v$ i završavaju u $v$ s parnostima $(a, b)$ bitova. Pri spajanju djeteta $c$ u $v$: puteve s LCA $v$ dobiješ kombiniranjem $dp[v]$ (dosadašnje djece + sam $v$) s $dp[c]$ (pomaknuto za vrijednost $v$): traži $a = b = 1$. Zatim $dp[v] \mathrel{+}= dp[c] \oplus v$. $O(16 n)$ po paru bitova.</p>
'''),
        ('Složenost',
         r'''
<p>$O(25^2 \cdot n)$ s malom konstantom; koristi iterativni DFS (ili BFS-poredak) da izbjegneš duboku rekurziju.</p>
'''),
    ],
    'solution': r'''
<p><b>Zbroj $A^2$.</b> Ako su u $A_{uv}$ postavljeni $i$-ti i $j$-ti bit, taj par bitova pridonosi kvadratu iznos $2^{i+j}$. Zato za svaki par bitova $(i, j)$ zadržimo samo čvorove kojima su oba bita postavljena — dobivamo šumu — i u svakoj komponenti prebrojimo puteve (komponenta veličine $s$ daje $s^2$ uređenih puteva, uključujući one duljine $0$). Ukupno $O(25^2 \cdot n)$, što je dovoljno brzo.</p>
<p><b>Zbroj $O^2$.</b> Pretpostavimo da su početno svi bitovi postavljeni na svakom putu, pa oduzmimo doprinos puteva na kojima $i$-ti i $j$-ti bit <i>nisu</i> nikad postavljeni. To je simetrično slučaju AND-a: promatramo komponente sastavljene od čvorova kojima su oba bita $0$.</p>
<p><b>Zbroj $X^2$.</b> Za svaki par $(i, j)$ napravimo dinamiku po stablu: $dp[v][a][b]$ je broj puteva koji počinju u podstablu čvora $v$ i završavaju u $v$, gdje $a$ označava je li $i$-ti bit XOR-a postavljen, a $b$ je li $j$-ti bit postavljen. U svakom čvoru $v$ ažuriramo odgovor za puteve čiji je najniži zajednički predak upravo $v$ (kombiniranjem $dp$ tablica djece s vrijednošću $v$), a zatim spajamo tablice djece u $dp[v]$.</p>
''',
},
{
    'letter': 'B',
    'title': 'Balanced Permutations',
    'title_hr': 'Uravnotežene permutacije',
    'slug': 'B_balanced_permutations',
    'tl': '6 s',
    'ml': '256 MB',
    'statement': r'''
<p>Za permutaciju $p$ duljine $n$ kažemo da je (neprekidni) podniz <i>nestabilan</i> ako je njegov maksimum ujedno njegov prvi ili zadnji element. Permutacija je <i>uravnotežena</i> ako među svim permutacijama duljine $n$ ima najmanji mogući broj nestabilnih podnizova.</p>
<p>Zadani su $n$, $l$ i $k$. Ispiši $l$-tu leksikografski najmanju i $k$-tu leksikografski najveću uravnoteženu permutaciju duljine $n$; ako takva ne postoji, ispiši $-1$.</p>
<h3>Ulaz</h3>
<p>Jedini redak sadrži $n$, $l$ i $k$ ($1 \le n \le 10^5$, $1 \le l, k \le 10^{18}$).</p>
<h3>Izlaz</h3>
<p>Dva retka: $l$-ta leksikografski najmanja i $k$-ta leksikografski najveća uravnotežena permutacija (ili $-1$ ako ne postoji).</p>
''',
    'hints': [
        r'''
<p>Maksimum dijeli permutaciju na $A$ i $B$; podnizovi koji ga sadrže su nestabilni točno ako u njemu počinju ili završavaju ($n$ komada). Dakle $\mathrm{unst}(p) = \mathrm{unst}(A) + \mathrm{unst}(B) + n$ — rekurzija ovisi samo o duljinama.</p>
''',
        r'''
<p>Grubom silom nađi za svaki $n$ skup dopuštenih pozicija maksimuma (nije nužno samo sredina). Broj uravnoteženih permutacija eksplodira, pa je za $l, k \le 10^{18}$ nužno da je gotovo cijela lijeva strana leksikografski najmanja; svedi na $n \lesssim 40$ i radi „k-tu permutaciju” brojanjem prefiksa DP-om.</p>
''',
    ],
    'coach': [
        ('Opažanje 1: rekurzija',
         r'''
<p>Podniz koji sadrži maksimum $n$ strogo unutra ima maksimum unutra — stabilan. Oni koji počinju ili završavaju na $n$: $n$ komada (uključujući duljinu $1$). Dakle $g(n) = \min_{\ell}\bigl(g(\ell) + g(n-1-\ell)\bigr) + n$, a uravnotežene su one čija podjela postiže minimum na obje strane rekurzivno.</p>
'''),
        ('Opažanje 2: brojanje',
         r'''
<p>Broj uravnoteženih permutacija duljine $n$: $\sum_{\ell \in \text{dopuštene}} \binom{n-1}{\ell}\, cnt(\ell)\, cnt(n-1-\ell)$ (odaberi vrijednosti za lijevu stranu). Raste superekspoencijalno — za $n \gtrsim 40$ već $\gg 10^{18}$.</p>
'''),
        ('Redukcija: veliki $n$',
         r'''
<p>Ako je $cnt(\text{lijeva strana}) \gt 10^{18}$, leksikografski $l$-ta permutacija ima lijevu stranu jednaku leksikografski najmanjoj uravnoteženoj (rekurzivno). Konstruiraj je izravno i preostali „slobodni” dio ima duljinu $\le 40$.</p>
'''),
        ('Algoritam: $k$-ta po prefiksu',
         r'''
<p>Klasično: gradi permutaciju znak po znak; za kandidatsku vrijednost prebroji uravnotežene permutacije s tim prefiksom (DP po intervalima i položaju maksimuma, $O(n^4)$–$O(n^5)$ na $n \le 40$), preskoči ako je broj $\lt l$. Najveću dobiješ zrcalno (ili istim algoritmom na komplementu).</p>
'''),
    ],
    'solution': r'''
<p><b>Kako izgledaju uravnotežene permutacije?</b> Najveći element dijeli permutaciju na lijevi podniz $A$ i desni podniz $B$. Svi podnizovi koji počinju ili završavaju u maksimumu nestabilni su (ima ih točno $n$), dok podnizovi koji sadrže maksimum strogo u unutrašnjosti sigurno nisu nestabilni. Stoga
$$\mathrm{unstables}(p) = \mathrm{unstables}(A) + \mathrm{unstables}(B) + n.$$</p>
<p>Uravnoteženu permutaciju gradimo rekurzivno: maksimum stavimo "negdje u sredinu" (grubom silom za male $n$ otkrijemo obrazac dopuštenih pozicija — nije to samo jedna ili dvije pozicije), zatim za svaku stranu odaberemo uravnoteženu permutaciju odgovarajuće duljine i "raspakiramo" vrijednosti: postoji $\binom{n-1}{\ell}$ načina da odaberemo koje vrijednosti idu u lijevu polovicu duljine $\ell$.</p>
<p><b>Leksikografski najmanja.</b> Za velike $n$ lijeva polovica sigurno mora biti leksikografski najmanja (broj uravnoteženih permutacija brzo premašuje $10^{18}$), pa niz možemo znatno skratiti i pretpostaviti $n \le 40$. Tada primjenjujemo standardnu strategiju: naučimo odgovarati na upit "koliko uravnoteženih permutacija ima zadani prefiks" i odgovor gradimo pohlepno, znamenku po znamenku. Brojanje je dinamičko programiranje složenosti $O(n^4)$ ili $O(n^5)$ koje razmatra svaki podniz i svaku moguću vrijednost maksimuma u tom podnizu. Leksikografski najveća permutacija dobiva se simetrično.</p>
''',
},
{
    'letter': 'C',
    'title': 'Cyclic Shifts',
    'title_hr': 'Ciklički pomaci',
    'slug': 'C_cyclic_shifts',
    'tl': '3 s',
    'ml': '512 MB',
    'statement': r'''
<p>Zadana je permutacija $p$ brojeva od $1$ do $n$. U jednoj operaciji biramo $k &gt; 0$ indeksa $1 \le x_1 &lt; x_2 &lt; \dots &lt; x_k \le n$ i ciklički pomaknemo odgovarajuće elemente za jedno mjesto udesno:
$$p_{x_2} := p_{x_1},\ p_{x_3} := p_{x_2},\ \dots,\ p_{x_k} := p_{x_{k-1}},\ p_{x_1} := p_{x_k}.$$
Operacija s parametrom $k$ košta $\frac{1}{k}$ dolara (grader računa cijenu kao $10^{-8} \lceil 10^8 / k \rceil$). Sortiraj permutaciju uz ukupni trošak najviše $2$ dolara.</p>
<h3>Ulaz</h3>
<p>Prvi redak sadrži $n$ ($1 \le n \le 5 \cdot 10^3$), drugi redak permutaciju $p_1, \dots, p_n$.</p>
<h3>Izlaz</h3>
<p>Broj operacija $m$, a zatim $m$ binarnih nizova duljine $n$: $j$-ti znak $i$-tog niza je <code>1</code> ako je indeks $j$ uključen u $i$-ti ciklički pomak. Svaki niz mora sadržavati barem jednu jedinicu.</p>
''',
    'hints': [
        r'''
<p>Ciklički pomak svih pozicija osim skupa <em>nesusjednih</em> izostavljenih: svaki izostavljeni element zamijeni mjesto sa svojim prethodnikom, a cijeli niz se rotira za $1$. Trošak $\le 2/n$.</p>
''',
        r'''
<p>Parno-neparno sortiranje (odd-even transposition sort) sortira u $n$ prolaza zamjenama disjunktnih susjednih parova: $n \cdot \frac{2}{n} = 2$ dolara, a $n$ rotacija za $1$ se poništi.</p>
''',
    ],
    'coach': [
        ('Opažanje 1: što radi $k = n-1$',
         r'''
<p>Na <code>a b c d e f g h</code> uz izostavljen <code>e</code>: <code>h a b c e d f g</code> — izostavljeni element „preskoči” prethodnika, ostalo je rotacija. Više izostavljenih koji nisu susjedni: neovisne zamjene susjednih parova + globalna rotacija.</p>
'''),
        ('Opažanje 2: budžet',
         r'''
<p>Uz $\ge n/2$ uključenih indeksa jedna operacija košta $\le 2/n$; $n$ operacija $= 2$. Treba sortirati u $\le n$ rundi disjunktnih susjednih zamjena — točno što radi odd-even sort.</p>
'''),
        ('Algoritam',
         r'''
<p>Vodi „virtualnu” rotaciju: nakon $t$ operacija fizički niz je rotiran za $t$, pa parove biraj u logičkim indeksima i preslikaj ih. U rundi $t$ usporedi parove $(2i + (t \bmod 2), 2i + 1 + (t \bmod 2))$ i izostavi drugi element svakog para koji treba zamijeniti; uključi sve ostalo. Nakon $n$ rundi (rotacija $n \equiv 0$) niz je sortiran.</p>
'''),
        ('Složenost',
         r'''
<p>$O(n^2)$ vremena i ispisa, $n \le 5000$.</p>
'''),
    ],
    'solution': r'''
<p>Mali $k$ je skup, veliki $k$ je jeftin. Operacija s $k = n$ nije osobito korisna (samo rotira cijeli niz). Što je s $k = n - 1$? Ako izostavimo jedan element, npr. $e$ u nizu <code>a b c d e f g h</code>, dobivamo <code>(h) a b c e d f g h</code>: izostavljeni element zamijeni mjesto sa svojim prethodnikom, a cijeli se niz uz to rotira za jedno mjesto.</p>
<p>Isto se događa kad god nikoja dva izostavljena elementa nisu susjedna: iz <code>a b c d e f g h</code> uz izostavljene $b$, $e$, $g$ dobivamo <code>(h) b a c e d g f h</code>. Dakle jednom operacijom možemo zamijeniti bilo koji skup međusobno disjunktnih susjednih parova (uz globalnu rotaciju za $1$), a trošak je najviše $\frac{1}{n/2} = \frac{2}{n}$.</p>
<p>Sada primijenimo <b>parno-neparno sortiranje</b> (odd-even sort): u svakom prolazu zamijenimo one susjedne parove (naizmjence na neparnim i parnim pozicijama) koji su u krivom poretku. Može se pokazati da je dovoljno $n$ prolaza, pa je ukupni trošak $n \cdot \frac{2}{n} = 2$. Rotacije se poništavaju: nakon $n$ prolaza niz je rotiran za $n$ mjesta, tj. uopće nije rotiran.</p>
''',
},
{
    'letter': 'D',
    'title': 'Distinct Subsequences',
    'title_hr': 'Različiti podnizovi',
    'slug': 'D_distinct_subsequences',
    'tl': '6 s',
    'ml': '256 MB',
    'statement': r'''
<p>Ethan ima binarni niz $s$ duljine $n$ i želi Justinu pokloniti njegov podniz (ne nužno neprekidni) duljine točno $k$. Izračunaj broj <i>različitih</i> poklona — podniz koji se u $s$ pojavljuje na više mjesta broji se samo jednom. Odgovor ispiši modulo $998\,244\,353$.</p>
<h3>Ulaz</h3>
<p>Prvi redak sadrži $n$ i $k$ ($1 \le k \le n \le 2 \cdot 10^5$), drugi redak binarni niz $s$.</p>
<h3>Izlaz</h3>
<p>Broj različitih podnizova duljine $k$ modulo $998\,244\,353$.</p>
''',
    'hints': [
        r'''
<p>Broji svaki podniz kroz njegovo <em>najljevije</em> (pohlepno) uparivanje: uparivanje je kanonsko ako između uzastopnih uparenih pozicija nema ranijeg pojavljivanja sljedećeg znaka.</p>
''',
        r'''
<p>Podijeli pa vladaj + FFT: za svaki dio drži $dp[\text{prvi znak}][\text{koji znak se ne može dodati unutar dijela}][\text{duljina}]$; spajanje lijevog i desnog dijela je konvolucija po duljini uz uvjet da lijevi dio ne može „progutati” prvi znak desnog.</p>
''',
    ],
    'coach': [
        ('Opažanje 1: kanonska pojavljivanja',
         r'''
<p>Različitih podnizova $=$ broj kanonskih (pohlepnih) uparivanja. Uparivanje pozicija $p_1 \lt \dots \lt p_k$ je kanonsko $\iff$ za svaki $t$, znak $s_{p_{t+1}}$ ne pojavljuje se u $(p_t, p_{t+1})$. Klasični DP $f[i][k]$ je $O(nk)$ — presporo za $2\cdot10^5$.</p>
'''),
        ('Opažanje 2: što treba znati o dijelu pri spajanju',
         r'''
<p>Za kanonski podniz unutar segmenta bitni su: prvi znak (da desni dio zna je li lijevi „mogao progutati” njegov početak) i skup znakova koji se ne mogu dodati na kraj unutar segmenta (tj. koji se ne pojavljuju nakon zadnje uparene pozicije). Stanja: $2 \times 3$ po duljini.</p>
'''),
        ('Algoritam: podijeli pa vladaj s FFT-om',
         r'''
<p>Spoji $L$ i $R$: par (lijevi kanonski $x$, desni kanonski $y$) je kanonski u uniji $\iff$ prvi znak $y$ nije dodatljiv na kraj $x$ unutar $L$. Za svaku kombinaciju stanja (fiksna konstanta) konvoluiraj nizove po duljini (FFT/NTT mod $998\,244\,353$). Pripazi na prazan podniz ($k = 0$) i na to da se „nedodatljivost” u uniji određuje po $R$ (znakovi nakon zadnje pozicije).</p>
'''),
        ('Složenost',
         r'''
<p>$T(n) = 2T(n/2) + O(n \log n) = O(n \log^2 n)$; odgovor je koeficijent uz duljinu $k$.</p>
'''),
    ],
    'solution': r'''
<p>Svakom podnizu pridružimo njegovo <i>kanonsko</i> pojavljivanje — najljevije (pohlepno) uparivanje znakova. Tako svaki različiti podniz brojimo točno jednom.</p>
<p>Koristimo <b>podijeli pa vladaj</b>: niz podijelimo na dva približno jednaka dijela, za svaki dio izračunamo broj kanonskih podnizova svake duljine, pa rezultate spojimo. Da bismo znali koja se spajanja slažu s kanonskim pojavljivanjem, za svaki prebrojani podniz unutar dijela pamtimo: njegov prvi znak te može li se unutar promatranog dijela proširiti dodavanjem znaka <code>0</code>, odnosno <code>1</code> (kanonsko pojavljivanje pri spajanju zahtijeva da se lijevi dio <i>ne može</i> proširiti prvim znakom desnog dijela — inače bi pohlepno uparivanje uzelo taj raniji znak).</p>
<p>Definiramo $dp[a][b][k]$, gdje je $a \in \{0, 1\}$ prvi znak podniza, $b \in \{0, 1, 2\}$ opisuje koji se znak <i>ne može</i> dodati na kraj unutar dijela ($2$ znači da se mogu dodati oba), a $k$ je duljina. Na primjer, za dio <code>0110110010</code> podniz <code>0110010</code> (duljine $7$) doprinosi u $dp[0][1][7]$, ali ne i u $dp[0][0][7]$.</p>
<p>Pri spajanju lijevog dijela $L$ i desnog $R$ vrijedi, na primjer,
$$dp[0][2][k] = \sum_{i+j=k} dp_L[0][1][i] \cdot dp_R[1][2][j] + \sum_{i+j=k} dp_L[0][0][i] \cdot dp_R[0][2][j] + \dots$$
i analogno za ostala stanja; svaka je takva suma konvolucija pa je računamo <b>FFT-om</b>. Poseban oprez treba za duljinu $k = 0$ (prazan podniz).</p>
<p>Složenost: $T(n) = 2\,T(n/2) + O(n \log n)$, dakle $O(n \log^2 n)$.</p>
''',
},
{
    'letter': 'E',
    'title': 'Epidemic Escape',
    'title_hr': 'Bijeg od epidemije',
    'slug': 'E_epidemic_escape',
    'tl': '4 s',
    'ml': '256 MB',
    'statement': r'''
<p>Svemirski brod nalazi se u ishodištu ravnine, a u ravnini je $n$ točaka zaraze. U trenutku $t = 0$ svaka zaraza počinje se širiti kao krug radijusa $t$ oko svoje točke. Istodobno brod kreće brzinom $1$ po pravcu prema zadanoj točki $(x'_j, y'_j)$ (i nastavlja i nakon što je prođe) sa štitom razine $k_j$. Brod je uništen u trenutku kad ga sadrži barem $k_j$ krugova zaraze.</p>
<p>Za svaki od $q$ scenarija ispiši trenutak uništenja ili $-1$ ako brod preživi zauvijek.</p>
<h3>Ulaz</h3>
<p>$n$ ($1 \le n \le 10^5$) i $n$ točaka $x_i, y_i$ ($|x_i|, |y_i| \le 10^8$); zatim $q$ ($1 \le q \le 10^5$) i $q$ redaka $x'_j, y'_j, k_j$ ($|x'_j|, |y'_j| \le 10^8$, $1 \le k_j \le 5$).</p>
<h3>Izlaz</h3>
<p>Za svaki scenarij vrijeme uništenja (dopuštena apsolutna ili relativna greška $10^{-6}$) ili $-1$. Za $x'_j = y'_j = 0$ ispiši $-1$.</p>
''',
    'hints': [
        r'''
<p>Zaraza iz $P_i$ dostigne brod točno kad brod prijeđe simetralu dužine $OP_i$ (brod i zaraza imaju istu brzinu). Upit: kada zraka iz $O$ presiječe $k$-ti po redu od $n$ pravaca?</p>
''',
        r'''
<p>Pravci najbliži ishodištu tvore konveksni poligon (presjek poluravnina). Odgovor za $k$ je među stranicama prvih $k$ „slojeva” poligona (skidaj slojeve $5$ puta jer $k \le 5$) i njihovih nekoliko susjeda u smjeru zrake.</p>
''',
    ],
    'coach': [
        ('Opažanje 1: simetrala',
         r'''
<p>Brod u trenutku $t$ je na udaljenosti $t$ od $O$; krug zaraze $i$ ima radijus $t$. Brod je unutra $\iff |B - P_i| \le t = |B|$ $\iff$ $B$ je s $P_i$-ne strane simetrale od $OP_i$. Zraka iz $O$ presijeca svaku simetralu najviše jednom, i nakon prijelaza ostaje unutra.</p>
'''),
        ('Opažanje 2: slojevi poluravnina',
         r'''
<p>Za $k = 1$ odgovor je prvi pravac koji zraka pogodi — stranica poligona $\bigcap$ poluravnina koje sadrže $O$. Za $k = 2$: ili pravac susjedan probijenoj stranici u istom poligonu, ili pravac koji nije u poligonu — a među tima prvi je stranica poligona 2. sloja. Indukcijom: $k$-ti presjek je u prvih $k$ slojeva, i to unutar $O(k)$ stranica oko smjera zrake.</p>
'''),
        ('Algoritam',
         r'''
<p>Izgradi $5$ slojeva presjeka poluravnina (uklanjaj pravce koji su stranice, $O(n \log n)$ po sloju). Za upit: u svakom sloju binarno nađi stranicu u smjeru zrake, uzmi nju i po $4$ susjedne s obje strane; izračunaj sve presjeke zrake s tim pravcima, sortiraj i uzmi $k$-ti. Ako ih je manje od $k$ (ili je zraka paralelna/udaljava se), $-1$.</p>
'''),
        ('Složenost i numerika',
         r'''
<p>$O(n \log n + q \log n)$. Radi u <code>long double</code>; presjek zrake s pravcem $\{X : X \cdot P_i = |P_i|^2/2\}$ je $t = \frac{|P_i|^2}{2\, d \cdot P_i}$ za jedinični smjer $d$ (valjano ako je nazivnik $\gt 0$).</p>
'''),
    ],
    'solution': r'''
<p>Kada nas zaraza iz točke $P_i$ prvi put dostigne? Točno onda kad je naša udaljenost od ishodišta jednaka udaljenosti do $P_i$, tj. kad prijeđemo <b>simetralu</b> dužine između ishodišta i $P_i$. Izračunamo sve te pravce; upit postaje: "kada zraka iz ishodišta presiječe $k$-ti po redu pravac?"</p>
<p>Pravci najbliži ishodištu (u svakom smjeru) tvore konveksni poligon oko ishodišta — presjek poluravnina koje sadrže ishodište. Za $k = 1$ odgovor je stranica tog poligona kroz koju zraka izlazi. Za $k = 2$ odgovor je ili pravac koji je u poligonu susjedan probijenoj stranici, ili pravac koji uopće nije u poligonu.</p>
<p>Zato pravce koji čine poligon izbrišemo, pronađemo novi poligon od preostalih pravaca i postupak ponovimo — trebamo $5$ slojeva jer je $k \le 5$.</p>
<p>Odgovor na upit: zraku presiječemo sa svakim od $5$ poligona (slojeva); za svaki uzmemo probijenu stranicu te po $4$ susjedne stranice s obje strane u tom poligonu. Zraku presiječemo sa svim tako odabranim pravcima i uzmemo $k$-ti najmanji trenutak presjeka. Ako presjeka nema dovoljno, brod preživi.</p>
''',
},
{
    'letter': 'F',
    'title': 'Five Letter Warning',
    'title_hr': 'Upozorenje od pet slova',
    'slug': 'F_five_letter_warning',
    'tl': '4 s',
    'ml': '256 MB',
    'statement': r'''
<p>Za zadani niz $s$ prebroj sve palindromne podnizove (ne nužno neprekidne) duljine točno $5$. Ako se isti niz pojavljuje kao podniz na više mjesta, broji se svaki put. Odgovor ispiši modulo $M$.</p>
<h3>Ulaz</h3>
<p>Prvi redak sadrži $s$ ($1 \le |s| \le 10^6$, znakovi s ASCII kodovima od $33$ do $126$), drugi redak $M$ ($2 \le M \le 10^9$).</p>
<h3>Izlaz</h3>
<p>Broj palindromnih podnizova duljine $5$ modulo $M$.</p>
''',
    'hints': [
        r'''
<p>Traže se podnizovi oblika <code>ab?ba</code>. Prolaz slijeva s tablicama $dp_1[a]$, $dp_2[a][b]$, $dp_3[a][b]$ (<code>ab?</code>), $dp_4[a][b]$ (<code>ab?b</code>).</p>
''',
        r'''
<p>$dp_3$ se ne smije ažurirati za sve parove pri svakom znaku; ažuriraj lijeno kad se ponovno pojavi $b$: $dp_3[a][b] \mathrel{+}= dp_2[a][b] \cdot (i - \mathrm{last}_b)$ (koristi staru vrijednost $dp_2$). Redoslijed ažuriranja: od duljih stanja prema kraćima. $O(|s| \cdot |\Sigma|)$.</p>
''',
    ],
    'coach': [
        ('Opažanje 1: pet stanja',
         r'''
<p>Podniz duljine $5$ palindrom $\iff$ oblik <code>a b c b a</code> (c proizvoljan). Standardni automat-DP broji prefikse uzorka; problem su $|\Sigma|^2 \approx 10^4$ parova $(a,b)$ po znaku — $10^{10}$.</p>
'''),
        ('Opažanje 2: zamjena „?” brojem pozicija',
         r'''
<p>Podniz <code>ab?</code> nastaje iz <code>ab</code> dodavanjem bilo koje kasnije pozicije. Umjesto da za svaki znak dodaš $dp_2[a][b]$ u $dp_3[a][b]$ za sve $a,b$, primijeti da se $dp_3[a][b]$ treba tek kad dođe sljedeći $b$: tada dodaj $dp_2[a][b] \times (\text{broj pozicija od prošlog } b)$. Tako se po znaku obrađuje $O(|\Sigma|)$ parova.</p>
'''),
        ('Algoritam: redoslijed',
         r'''
<p>Pri znaku $c$ na poziciji $i$, od duljih stanja prema kraćima: (1) <code>ab?ba</code> završava znakom $a = c$: $ans \mathrel{+}= \sum_b dp_4[c][b]$; (2) za sve $a$: lijeno dovrši $dp_3[a][c] \mathrel{+}= dp_2[a][c]\cdot(i - \mathrm{last}_c)$ (nove pozicije od prošlog $c$), zatim $dp_4[a][c] \mathrel{+}= dp_3[a][c]$; (3) $dp_2[a][c] \mathrel{+}= dp_1[a]$; (4) $dp_1[c] \mathrel{+}= 1$; $\mathrm{last}_c = i$. Sve modulo $M$ ($M$ ne mora biti prost — koristimo samo zbrajanje i množenje).</p>
'''),
        ('Složenost',
         r'''
<p>$O(|s| \cdot |\Sigma|)$ vremena, $O(|\Sigma|^2)$ memorije.</p>
'''),
    ],
    'solution': r'''
<p>Tražimo podnizove oblika <code>ab?ba</code>. Duljina niza je do $10^6$, a alfabet ima oko $100$ znakova, pa moramo izbjeći i vrijeme $|s| \cdot 100^2$ i memoriju $|s| \cdot 100$.</p>
<p>Prolazimo niz slijeva nadesno i održavamo:</p>
<ul>
    <li>$dp_1[a]$ — broj podnizova <code>a</code>,</li>
    <li>$dp_2[a][b]$ — broj podnizova <code>ab</code>,</li>
    <li>$dp_3[a][b]$ — broj podnizova <code>ab?</code>,</li>
    <li>$dp_4[a][b]$ — broj podnizova <code>ab?b</code>.</li>
</ul>
<p>$dp_1$ i $dp_2$ ažuriramo izravno: za trenutačni znak $c$ vrijedi $dp_2[a][c] \mathrel{+}= dp_1[a]$ za sve $a$, zatim $dp_1[c] \mathrel{+}= 1$.</p>
<p>Stanje $dp_3[a][b]$ ne možemo ažurirati za sve parove pri svakom znaku (bilo bi $100^2$ po znaku). Umjesto toga ažuriramo ga lijeno, tek pri sljedećem pojavljivanju znaka $b$: broj novih podnizova <code>ab?</code> nastalih od zadnjeg pojavljivanja $b$ jednak je $dp_2[a][b] \cdot (i - \mathrm{last}_b)$, gdje je $\mathrm{last}_b$ pozicija prethodnog pojavljivanja $b$ (i to prije nego što $dp_2[a][b]$ promijenimo). Time se po znaku obavlja samo $O(100)$ posla.</p>
<p>Analogno, $dp_4[a][b] \mathrel{+}= dp_3[a][b]$ kad se pojavi $b$, a odgovor uvećavamo za $dp_4[a][b]$ kad se pojavi $a$. Ključno je stanja ažurirati u ispravnom redoslijedu (od dužih prema kraćima) kako se isti znak ne bi iskoristio dvaput. Ukupno $O(|s| \cdot |\Sigma|)$ vremena i $O(|\Sigma|^2)$ memorije.</p>
''',
},
{
    'letter': 'G',
    'title': 'Gridlandia',
    'title_hr': 'Gridlandija',
    'slug': 'G_gridlandia',
    'tl': '1 s',
    'ml': '256 MB',
    'statement': r'''
<p>Kontinent Gridlandija kvadrat je stranice $n$ podijeljen na $n^2$ kvadratnih država stranice $1$. Svaka država može odabrati najviše jednu od svojih četiriju stranica i na njoj izgraditi zid preko cijele stranice. Nikoja se dva zida ne smiju dodirivati, čak ni u krajnjim točkama.</p>
<p>Odredi najveći mogući broj zidova i konstruiraj takav raspored.</p>
<h3>Ulaz</h3>
<p>Jedini redak sadrži $n$ ($1 \le n \le 10^3$).</p>
<h3>Izlaz</h3>
<p>$n$ redaka po $n$ znakova: <code>.</code> za državu bez zida ili jedan od <code>U</code>, <code>D</code>, <code>L</code>, <code>R</code> za zid na gornjoj, donjoj, lijevoj odnosno desnoj stranici.</p>
''',
    'hints': [
        r'''
<p>Zid zauzima $2$ kuta mreže, a kutovi se ne smiju dijeliti: najviše $\lfloor (n+1)^2/2 \rfloor$ zidova (uparivanje u grafu kutova).</p>
''',
        r'''
<p>Granica se postiže: u svakom drugom stupcu složi horizontalne zidove <code>U</code> jedan iznad drugog, a preostale kutove uz rub pokrij vertikalnim zidovima <code>L</code>/<code>R</code> i donjim <code>D</code>. Vlasništvo zidova rasporedi tako da svaka država gradi najviše jedan.</p>
''',
    ],
    'coach': [
        ('Opažanje 1: gornja granica',
         r'''
<p>Vrhovi mreže $(n+1)^2$; zid = brid rešetke; „ne dodiruju se ni u krajnjim točkama” = uparivanje. Dakle $\le \lfloor (n+1)^2/2 \rfloor$. Uz dodatni uvjet: svaka država (polje) posjeduje $\le 1$ zid od svoje $4$ stranice.</p>
'''),
        ('Opažanje 2: gotovo savršeno uparivanje rešetke',
         r'''
<p>Rešetka $(n+1)\times(n+1)$ vrhova ima savršeno uparivanje kad je $(n+1)^2$ paran, inače ostaje jedan vrh. Horizontalni bridovi u svakom drugom stupcu polja pokrivaju parove stupaca vrhova; rubni stupac vrhova pokrij vertikalnim bridovima.</p>
'''),
        ('Algoritam: dodjela vlasnika',
         r'''
<p>Horizontalni zid između polja $(i, j)$ i $(i+1, j)$ može pripadati gornjem (<code>D</code>) ili donjem (<code>U</code>) polju; u stupcu s naslaganim zidovima svako polje dobije zid na svojoj gornjoj stranici (<code>U</code>), a zadnji redak zid ispod (<code>D</code>). Vertikalni rubni zidovi idu susjednim poljima kao <code>L</code>/<code>R</code> — ta polja su u stupcima bez zidova. Provjeri lokalno da svaki zid ima susjedno slobodno polje.</p>
'''),
        ('Složenost',
         r'''
<p>$O(n^2)$ ispisa.</p>
'''),
    ],
    'solution': r'''
<p>Svaki vrh mreže (kut) može pripadati najviše jednom zidu, a svaki zid zauzima dva kuta. Zato je broj zidova najviše
$$\left\lfloor \frac{\#\text{kutova}}{2} \right\rfloor = \left\lfloor \frac{(n+1)^2}{2} \right\rfloor.$$
(Usput, zadatak je zapravo bipartitno uparivanje: zidovi su bridovi mreže vrhova, a uvjet "ne dodiruju se" znači da je skup zidova uparivanje.)</p>
<p>Ta je granica dostiživa i za parne i za neparne $n$. Konstrukcija: u svakom drugom stupcu postavimo horizontalne zidove naslagane jedan iznad drugog (svaka država u stupcu gradi zid na gornjoj stranici, <code>U</code>), a preostale kutove uz rub mreže pokrijemo vertikalnim zidovima na lijevoj i desnoj strani (<code>L</code>/<code>R</code>) te donjim zidovima (<code>D</code>) u zadnjem retku. Vlasništvo se uvijek može dodijeliti tako da svaka država ima najviše jedan zid, jer je svaki zid susjedan barem jednoj državi koja nije iskoristila svoj zid.</p>
''',
},
{
    'letter': 'H',
    'title': 'Holiday Regifting',
    'title_hr': 'Blagdansko prepoklanjanje',
    'slug': 'H_holiday_regifting',
    'tl': '3 s',
    'ml': '256 MB',
    'statement': r'''
<p>U gradu živi $n$ ljudi; osoba $i$ u kući može pohraniti $c_i$ poklona. Postoji $m$ prijateljstava; u svakom je "mentor" prijatelj s većim indeksom. Svaki dan patuljak donosi jedan poklon osobi $1$. Ako bi poklon napunio kuću do kapaciteta, osoba izbaci sve svoje poklone i naredi patuljku da isporuči po jedan poklon svakom njezinu mentoru u rastućem poretku indeksa (preostali pokloni idu u spalionicu); te se narudžbe obrađuju rekurzivno (stog zahtjeva). Svaka osoba ima kapacitet barem jednak broju mentora.</p>
<p>Odredi prvi dan na kraju kojeg ni u jednoj kući nema poklona, modulo $998\,244\,353$, ili ispiši $-1$ ako takav dan ne postoji.</p>
<h3>Ulaz</h3>
<p>$n$ i $m$ ($1 \le n \le 10^4$, $0 \le m \le 3 \cdot 10^4$); $c_1, \dots, c_n$ ($2 \le c_i \le 10^5$); $m$ redaka $u_i, v_i$ ($1 \le u_i &lt; v_i \le n$).</p>
<h3>Izlaz</h3>
<p>Traženi dan modulo $998\,244\,353$ ili $-1$.</p>
''',
    'hints': [
        r'''
<p>Graf mentorstava je DAG po indeksima; kuća osobe $j$ prazni se točno svakim $c_j$-tim primljenim poklonom. Period ispraznjenja prvih $i$ osoba: $dp[i]$ dana, a $dp[i+1] = dp[i]\cdot\frac{c_{i+1}}{\gcd(c_{i+1}, S)}$ gdje je $S$ broj poklona koje $i+1$ primi u $dp[i]$ dana.</p>
''',
        r'''
<p>$S = \sum_{j \to i+1} \frac{dp[i]\cdot\mathrm{gifts}[j]}{dp[j]\cdot c_j}$. Brojevi su ogromni — drži ih faktorizirane (mapa prost $\to$ eksponent) i tek na kraju izračunaj modulo.</p>
''',
    ],
    'coach': [
        ('Opažanje 1: periodičnost',
         r'''
<p>Proces je deterministički i svako stanje (broj poklona po kući) vraća se u „sve prazno” periodično; osoba $1$ dobiva $1$ poklon dnevno pa se prazni svakih $c_1$ dana. Osoba $j$ prima poklone samo od mentoriranih s manjim indeksom — po topološkom redu period je dobro definiran.</p>
'''),
        ('Opažanje 2: lcm-struktura',
         r'''
<p>Ako se prvih $i$ kuća resetira svakih $dp[i]$ dana i u tom razdoblju $i+1$ primi $S$ poklona, ona se prazni kad je ukupni broj višekratnik $c_{i+1}$: nakon $\frac{c_{i+1}}{\gcd(c_{i+1}, S)}$ perioda. Odgovor je $dp[n]$ — nakon točno toliko dana sve su kuće istodobno prazne, a ranije to nije moguće jer je $dp[n]$ najmanji zajednički period.</p>
'''),
        ('Algoritam: računanje $S$',
         r'''
<p>$\mathrm{gifts}[j]$ = broj poklona koje $j$ primi tijekom svog perioda $dp[j]$. U $dp[i]$ dana ($dp[j] \mid dp[i]$) osoba $j$ primi $\mathrm{gifts}[j]\cdot dp[i]/dp[j]$ poklona i isprazni se svaki $c_j$-ti put, pa mentoru $i+1$ pošalje $\frac{dp[i]\,\mathrm{gifts}[j]}{dp[j]\,c_j}$ poklona. Svi članovi su cijeli brojevi, ali golemi: čuvaj $dp$ i $\mathrm{gifts}$ kao eksponente prostih faktora. Za $\gcd(c_{i+1}, S)$ bitni su samo prosti faktori $p$ od $c_{i+1}$ — izračunaj $S \bmod p^{e}$ (gdje $p^e \| c_{i+1}$) iz faktoriziranih članova i odredi eksponent $p$ u $S$.</p>
'''),
        ('Složenost',
         r'''
<p>$O((n + m)\cdot \omega)$ uz mali broj prostih faktora po $c_i$.</p>
'''),
    ],
    'solution': r'''
<p>Bridovi vode od manjeg prema većem indeksu, pa je graf usmjeren acikličan i osobe možemo obrađivati redom $1, 2, \dots, n$. Za prvih $i$ osoba neka je $dp[i]$ duljina <b>perioda</b> nakon kojeg su sve njihove kuće istodobno prazne (kuća osobe $j$ prazni se točno svaki $c_j$-ti primljeni poklon).</p>
<p>Dodajmo osobu $i + 1$. Neka ona tijekom jednog perioda $dp[i]$ primi $S$ poklona. Novi je period tada
$$dp[i+1] = dp[i] \cdot \frac{c_{i+1}}{\gcd(c_{i+1}, S)},$$
jer se njezina kuća prazni tek kad ukupan broj primljenih poklona bude višekratnik $c_{i+1}$.</p>
<p>Kako izračunati $S$? Za svaku osobu $j$ održavamo $\mathrm{gifts}[j]$ — broj poklona koje $j$ primi tijekom svog perioda $dp[j]$. Ako postoji brid $j \to i+1$, osoba $j$ se tijekom $dp[i]$ dana isprazni $\frac{dp[i] \cdot \mathrm{gifts}[j]}{dp[j] \cdot c_j}$ puta i svaki put pošalje jedan poklon osobi $i + 1$, pa je $S$ zbroj tih vrijednosti po svim mentorstvima. Odgovor je $dp[n]$; kako period može biti golem, računamo ga faktoriziran (kao višekratnike primitivnih faktora) odnosno modulo $998\,244\,353$ samo na kraju.</p>
''',
},
{
    'letter': 'I',
    'title': 'Julienne the Deck',
    'title_hr': 'Rezanje špila',
    'slug': 'I_julienne_the_deck',
    'tl': '1 s',
    'ml': '256 MB',
    'statement': r'''
<p>Daniel miješa špil od $n$ različitih karata novom operacijom: odabere $i$ ($1 \le i &lt; n$) te istodobno obrne prvih $i$ karata i zadnjih $n - i$ karata. Primjerice, iz $p = [1, 4, 3, 2, 5, 6]$ uz $i = 4$ nastaje $p' = [2, 3, 4, 1, 6, 5]$.</p>
<p>Koliko se različitih permutacija može dobiti iz sortiranog špila proizvoljnim brojem (moguće nula) takvih operacija? Odgovor ispiši modulo $998\,244\,353$.</p>
<h3>Ulaz</h3>
<p>Jedini redak sadrži $n$ ($1 \le n \le 10^{12}$).</p>
<h3>Izlaz</h3>
<p>Broj dostižnih permutacija modulo $998\,244\,353$.</p>
''',
    'hints': [
        r'''
<p>Zapiši špil na kružnicu: obrtanje prefiksa i sufiksa odgovara promjeni početne točke i smjera čitanja istog cikličkog niza.</p>
''',
        r'''
<p>Za $n \ge 3$ dostižno je svih $2n$ čitanja (svaka početna točka, oba smjera); $n=1 \Rightarrow 1$, $n = 2 \Rightarrow 2$.</p>
''',
    ],
    'coach': [
        ('Opažanje 1: invarijanta',
         r'''
<p><code>abcd|ef</code> $\to$ <code>dcba|fe</code>. Ciklički niz <code>abcdef</code> čitan unatrag od <code>d</code>: <code>d c b a f e</code>. Dakle ciklički poredak (do smjera) je invarijanta — najviše $2n$ permutacija.</p>
'''),
        ('Opažanje 2: sve se postiže',
         r'''
<p>Operacija s parametrom $i$ daje čitanje unatrag počevši od pozicije $i$; dvije uzastopne operacije daju čitanje unaprijed s pomaknutom početnom točkom. Za $n \ge 3$ izborom $i$ dosegneš svaku početnu točku u oba smjera — točno $2n$ različitih permutacija. Rubni slučajevi $n = 1$ i $n = 2$ ($2n$ čitanja nisu sva različita) provjeri ručno: $1$ odnosno $2$.</p>
'''),
        ('Algoritam',
         r'''
<p>$n = 1 \to 1$; $n = 2 \to 2$; inače $2n \bmod 998\,244\,353$.</p>
'''),
    ],
    'solution': r'''
<p>Zapišimo permutaciju na kružnicu. Obrtanje prefiksa i pripadnog sufiksa, npr. <code>abcd|ef</code> $\to$ <code>dcba|fe</code>, na kružnici odgovara odabiru druge početne točke i obrtanju smjera čitanja: niz ostaje isti ciklički niz, čitan unatrag od drugog mjesta.</p>
<p>Za $n &gt; 2$ na taj način možemo dobiti bilo koju početnu točku i bilo koji smjer, pa je odgovor $2n$. Rubni slučajevi: za $n = 1$ odgovor je $1$, a za $n = 2$ odgovor je $2$.</p>
''',
},
{
    'letter': 'J',
    'title': 'Knight’s Tour Redux',
    'title_hr': 'Skakačeva tura, ponovno',
    'slug': 'J_knights_tour_redux',
    'tl': '1 s',
    'ml': '256 MB',
    'statement': r'''
<p>Na ploči $n \times n$ nalazi se "dugi skakač" koji se s polja $(x, y)$ može pomaknuti na $(x', y')$ ako je $|x - x'| = 3$ i $|y - y'| = 1$, ili $|x - x'| = 1$ i $|y - y'| = 3$. Tura je niz polja $S_1, \dots, S_n$ u kojem je svaki prijelaz valjan potez; tura je <i>potpuna</i> ako posjeti svaki redak i svaki stupac točno jednom.</p>
<p>Odredi postoji li potpuna tura i konstruiraj je.</p>
<h3>Ulaz</h3>
<p>Jedini redak sadrži $n$ ($1 \le n \le 10^5$).</p>
<h3>Izlaz</h3>
<p><code>IMPOSSIBLE</code>, ili <code>POSSIBLE</code> i zatim $n$ redaka s koordinatama $x_i, y_i$ polja ture.</p>
''',
    'hints': [
        r'''
<p>Promatraj koordinate zasebno: $x$ i $y$ svaka mora biti permutacija $1..n$ s koracima $\pm1, \pm3$, i to komplementarno (kad je jedan korak kratak, drugi je dug).</p>
''',
        r'''
<p>Nađi eksplicitne parove nizova za $n = 5..12$ (ručno ili pretragom), pa ih nadovezuj: rješenja za $7, 9, 11$ lijepe se jedno na drugo, a $6, 8, 10$ dodaju na kraj. $n \in \{2,3,4\}$ nemoguće, $n = 1$ trivijalno.</p>
''',
    ],
    'coach': [
        ('Opažanje 1: dekompozicija po koordinatama',
         r'''
<p>Uvjet ture: $|\Delta x| \in \{1,3\}$, $|\Delta y| = 4 - |\Delta x|$; svaki redak i stupac točno jednom $\Rightarrow$ $(x_t)$ i $(y_t)$ su permutacije. Traže se dva „1D skakačka puta” s komplementarnim uzorkom kratki/dugi.</p>
'''),
        ('Opažanje 2: mali slučajevi i lijepljenje',
         r'''
<p>Za $n \le 4$ nema koraka $3$ i $1$ s dovoljno prostora u oba smjera (pretraga potvrđuje). Ako blok duljine $m$ počinje uzorkom koji odgovara završetku prethodnog bloka (npr. završava dugim korakom u $x$, sljedeći počinje kratkim), blokove možeš konkatenirati uz pomak koordinata za $m$ — ali prijelaz između blokova mora i sam biti valjan potez: odaberi blokove čiji krajevi/počeci to omogućuju (npr. zadnja $x$ u bloku $= m$, prva u sljedećem $= 1 \Rightarrow \Delta x = 1$, uz $\Delta y = 3$).</p>
'''),
        ('Algoritam',
         r'''
<p>Pohrani rješenja za $5..12$; za $n \ge 5$ zapiši $n = 7a + 9b + 11c + r$ s $r \in \{0, 6, 8, 10\}$ (uvijek moguće za $n \ge 5$ osim baznih slučajeva $5..12$ koji su izravni), ispiši blokove s pomacima. $O(n)$.</p>
'''),
    ],
    'solution': r'''
<p>Promotrimo samo $x$-koordinatu: u svakom potezu ona se mijenja za $-3$, $-1$, $+1$ ili $+3$, a mora posjetiti svaki stupac točno jednom. Isto vrijedi za $y$-koordinatu, uz dodatno ograničenje: kad $x$ napravi kratki skok ($\pm 1$), $y$ mora napraviti dugi ($\pm 3$), i obrnuto.</p>
<p>Zato zasebno konstruiramo jednodimenzionalne nizove za $x$ i za $y$ s komplementarnim vrstama skokova. Za $n = 5$ jedan takav par nizova ima skokove (dugi, kratki, dugi, kratki) za $x$ i (kratki, dugi, kratki, dugi) za $y$. Eksplicitna rješenja postoje za $n = 5$, $6$, $7$, $8$, $9$, $10$, $11$ i $12$.</p>
<p>Rješenja za $7$, $9$ i $11$ mogu se proizvoljno nadovezivati (konkatenirati) jedno na drugo, a rješenja za $6$, $8$ i $10$ mogu se dodati na kraj. Time dobivamo potpunu turu za svaki $n \ge 5$; za $n = 1$ tura je trivijalna, dok je za $n = 2, 3, 4$ tura nemoguća (ploča je premala za skok duljine $3$ u oba smjera potrebna za posjet svih redaka i stupaca).</p>
''',
},
]
