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
        ('Koliko informacije daje jedan odgovor i koliko koraka smijemo potrošiti?',
         r'''<p>Odgovor je jedan nenegativan broj, ali u praksi razlikuje samo nekoliko slučajeva. Budžet je $40$ upita, a $\log_2 10^6 \approx 20$: dakle smijemo si dopustiti <em>dva</em> upita po koraku binarnog pretraživanja, ali ne više. To odmah sugerira plan: održavaj interval kandidata $[l, r]$ i u svakom koraku ga (barem približno) prepolovi s najviše dva upita.</p>'''),
        ('Što točno znamo o upaljenim svjetlima dok pretraživanje traje?',
         r'''<p>Sva do sada upaljena svjetla nalaze se <em>izvan</em> intervala kandidata: $c_l$ ih je u $[1, l-1]$, a $c_r$ u $[r+1, n]$. To je invarijanta koju održavamo – svjetlo koje upalimo unutar intervala odmah izbacujemo iz intervala (postaje $m$-ta granica ili je samo rješenje). Zato nakon paljenja svjetla $x \in [l, r]$ odgovor ovisi samo o $c_l$, $c_r$ i tome je li skriveno svjetlo $f$ lijevo od $x$, desno od $x$ ili baš $x$.</p>'''),
        ('Zašto sredina intervala ponekad ne razlikuje sve slučajeve?',
         r'''<p>Upalimo $m$. Ako je $f > m$, lijevo od $f$ ima $c_l + 1$ upaljenih, pa je odgovor $|c_l + 1 - c_r|$; ako je $f < m$, odgovor je $|c_l - c_r - 1|$; ako je $f = m$, odgovor je $|c_l - c_r|$. Uz $d = c_l - c_r$ to su $|d+1|$, $|d-1|$ i $|d|$. Za $d \ne 0$ ta su tri broja međusobno različita (npr. $d = 2$: $3, 1, 2$), pa jedan upit odlučuje. Za $d = 0$ dobivamo $1, 1, 0$ – lijevo i desno se ne razlikuju!</p>'''),
        ('Kako jeftino razbiti simetriju $c_l = c_r$?',
         r'''<p>Umjesto sredine upali <em>rub</em> intervala, svjetlo $r$. Ako je $f = r$, odgovor je $|c_l - c_r| = 0$ i gotovi smo. Inače je $f \in [l, r-1]$, a $r$ je upaljeno desno od $f$, pa $c_r$ raste za jedan i sada je $d = -1 \ne 0$ – sljedeći upit u sredini opet razlikuje sve tri slučaja. Ravnoteža se dakle popravlja jednim upitom, a nakon koraka sa sredinom $d$ se opet mijenja za $\pm 1$ i može ponovno postati $0$; zato je u najgorem slučaju ukupno oko $2\log_2 n \le 40$ upita.</p>'''),
        ('Smeta li nam adaptivan interaktor?',
         r'''<p>Ne. Svaki naš zaključak vrijedi za <em>svako</em> skriveno svjetlo koje je konzistentno s dosadašnjim odgovorima: nakon svakog upita skup kandidata je točno interval $[l, r]$ i interaktor mora odabrati nešto iz njega. Kako broj upita ovisi samo o duljini intervala, adaptivnost ne može povećati broj upita iznad analizirane granice.</p>'''),
    ],
    'tips': [
        r'''Kod interaktivnih zadataka prvo izračunaj $\lceil\log_2 n\rceil$ i usporedi s dopuštenim brojem upita: omjer (ovdje $2$) odmah kaže koliko upita po koraku binarnog pretraživanja smiješ potrošiti.''',
        r'''Kad odgovor ovisi o apsolutnoj vrijednosti razlike, provjeri degenerirani slučaj u kojem su dvije grane simetrične (ovdje $c_l = c_r$) i potroši jedan upit da simetriju razbiješ, umjesto da gubiš informaciju.''',
        r'''Interaktivne zadatke testiraj lokalnim sucem koji simulira <em>sve</em> moguće skrivene vrijednosti za male $n$ i broji najgori broj upita – to je jedini način da se uvjeriš da granica upita nikad nije prekoračena.''',
        r'''Ne zaboravi <code>fflush(stdout)</code> (ili <code>endl</code>) nakon svakog upita; bez toga interaktivno rješenje visi iako je algoritam ispravan.''',
    ],
    'detailed': r'''
<h3>1. Model odgovora</h3>
<p>Skriveno je svjetlo $f$. Nakon upita „<code>? x</code>” svjetlo $x$ je upaljeno (ako već nije bilo) i interaktor vraća $|L - R|$, gdje je $L$ broj upaljenih svjetala s indeksom $< f$, a $R$ broj upaljenih s indeksom $> f$. Svjetlo $f$ samo, ako je upaljeno, ne ulazi ni u $L$ ni u $R$.</p>
<p>Održavamo interval kandidata $[l, r]$ s ovom <strong>invarijantom</strong>: sva upaljena svjetla su izvan intervala, i to $c_l$ u $[1, l-1]$ i $c_r$ u $[r+1, n]$. Na početku je $[l, r] = [1, n]$, $c_l = c_r = 0$. Invarijanta znači da za svako svjetlo $x \in [l, r]$ koje upravo palimo vrijedi:</p>
<ul>
<li>$f > x$: lijevo od $f$ je $c_l + 1$ upaljenih, desno $c_r$; odgovor $|c_l + 1 - c_r|$;</li>
<li>$f < x$: odgovor $|c_l - c_r - 1|$;</li>
<li>$f = x$: odgovor $|c_l - c_r|$.</li>
</ul>
<p>Označimo $d = c_l - c_r$. Tri moguća odgovora su $|d+1|$, $|d|$, $|d-1|$.</p>
<h3>2. Ključno opažanje: kada jedan upit razlikuje sve tri slučaja</h3>
<p>Ako je $d \ne 0$, brojevi $|d-1|, |d|, |d+1|$ su međusobno različiti. Dokaz: za $d \ge 1$ to su $d-1 < d < d+1$; za $d \le -1$ to su $|d|+1 > |d| > |d|-1$. Dakle iz odgovora jednoznačno čitamo je li $f < x$, $f = x$ ili $f > x$. Ako je $d = 0$, odgovori su $1, 0, 1$: znamo jedino je li $f = x$; lijevo i desno se ne razlikuju.</p>
<h3>3. Korak binarnog pretraživanja</h3>
<ol>
<li>Ako je $l = r$, odgovor je $l$ (bez upita).</li>
<li>Ako je $c_l = c_r$: upali $r$. Odgovor $0$ znači $f = r$ – gotovo. Inače je $f \in [l, r-1]$; svjetlo $r$ sada je upaljeno desno od $f$, postavimo $r \gets r - 1$, $c_r \gets c_r + 1$. Sada je $d = -1 \ne 0$. (Ako je novi interval jednočlan, gotovi smo.)</li>
<li>Upali $m = \lfloor (l+r)/2 \rfloor$. Prema odgovoru: $|d|$ $\Rightarrow$ $f = m$; $|d-1|$ $\Rightarrow$ $f < m$, pa $r \gets m-1$, $c_r \gets c_r + 1$; $|d+1|$ $\Rightarrow$ $f > m$, pa $l \gets m+1$, $c_l \gets c_l + 1$.</li>
</ol>
<p>Invarijanta se očito održava: svako upaljeno svjetlo izbacujemo iz intervala i pribrajamo odgovarajućem brojaču. Ispravnost slijedi izravno iz točke 2.</p>
<h3>4. Broj upita</h3>
<p>Korak s upitom na $m$ smanjuje duljinu intervala s $s$ na najviše $\lfloor s/2 \rfloor$. Korak na $r$ smanjuje duljinu za $1$ i troši jedan upit, ali se može dogoditi najviše jednom između dva upita na $m$ (nakon njega je $d \ne 0$). Zato je u najgorem slučaju po dva upita za svako polovljenje: ukupno najviše $2\lceil \log_2 n \rceil = 40$ za $n = 10^6$ ($2^{20} > 10^6$). Lokalni sudac koji simulira <em>sva</em> skrivena svjetla potvrđuje da granica nikad nije prekoračena: za $n = 10^6$ najveći broj upita po svim $f$ iznosi $37$.</p>
<h3>5. Adaptivnost</h3>
<p>Interaktor smije mijenjati $f$ dok god je konzistentan s prethodnim odgovorima. Nakon svakog našeg upita skup konzistentnih $f$ je točno naš interval $[l, r]$ (za $d \ne 0$ odgovor jednoznačno određuje stranu; za $d = 0$ upit na rub jednoznačno odlučuje o $r$). Dakle interaktor bira samo unutar intervala, a broj upita ovisi jedino o duljini intervala – analiza iz točke 4 vrijedi i protiv adaptivnog suca.</p>
<h3>6. Primjer</h3>
<p>$n = 5$, $f = 2$. $[1,5]$, $c_l = c_r = 0$: upali $5$ → odgovor $1$ (nije $5$), $[1,4]$, $c_r = 1$, $d = -1$. Upali $m = 2$: kandidati $|d+1| = 0$ ($f > 2$), $|d| = 1$ ($f = 2$), $|d-1| = 2$ ($f < 2$); interaktor vraća $1$ → ispis „<code>! 2</code>”. Ukupno $2$ upita.</p>
<h3>7. Implementacijske napomene</h3>
<ul>
<li>Nakon svakog upita obavezno isprazni izlazni međuspremnik; nakon „<code>! x</code>” završi bez daljnjeg čitanja.</li>
<li>Slučaj $n = 1$: odmah „<code>! 1</code>”.</li>
<li>Ne pali isto svjetlo dvaput – algoritam to i ne čini, jer svako upaljeno svjetlo napušta interval.</li>
<li>Za lokalno testiranje korisno je u isti izvorni kod ugraditi simulator suca (ovdje: ako ulaz sadrži i drugi broj, program sam glumi suca i za $s = 0$ provjerava sva skrivena svjetla te ispisuje najveći broj upita).</li>
</ul>
''',
    'verified': r'''Interaktivni zadatak: lokalni sudac u samom programu (za n ≤ 60 iscrpno sve skrivene lampice, za n = 10^6 sve pozicije s najviše 37 upita) te odvojeni sudac preko cijevi (interactor.py: iscrpno n ≤ 60 i 30 velikih n); uzorak 1/1, 300 slučajnih testova provjereno checkerom, 3 velika testa (najviše 0.12 s).''',
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
        ('Što zapravo ograničava „složenost $\le 9$” – koliko je izraz velik?',
         r'''<p>Nacrtaj izraz kao stablo: listovi su $x$, unarni čvorovi $\sin/\cos$ imaju jedno dijete, binarni $+,-,\times,\div$ dva. Zagrade su samo zapis. Složenost je $2 \cdot (\text{broj binarnih}) + (\text{broj unarnih})$; stablo s $b$ binarnih čvorova ima točno $b+1$ listova, pa je ukupan broj čvorova $2b + 1 + u \le 10$. Izrazi su, dakle, sitni – to je znak da je nabrajanje realno.</p>'''),
        ('Zašto je gruba procjena $7^{10}$ preoptimistična u lošem smjeru i kako izbrojati stvarne kandidate?',
         r'''<p>Prefiksni zapis s $10$ simbola iz $\{x, \sin, \cos, +, -, \times, \div\}$ daje $7^{10} \approx 2.8 \cdot 10^8$ nizova, ali gotovo nijedan nije valjan izraz (broj listova mora odgovarati broju binarnih čvorova). Prebroji valjane po složenosti: $f_0 = 1$, $f_c = 2 f_{c-1} + 4 \sum_{i+j=c-2} f_i f_j$. Dobivamo $1, 2, 8, 32, 144, 672, 3264, 16256, 82688, 427520$ – ukupno oko $5.3 \cdot 10^5$ stabala. Svako treba evaluirati u $n \le 20$ točaka: reda $10^7$ operacija, posve prihvatljivo.</p>'''),
        ('Kako ih generirati bez ponavljanja posla i bez rekurzije po nizovima simbola?',
         r'''<p>Gradi odozdo prema gore po složenosti: $f_c$ je lista izraza složenosti točno $c$, a svaki izraz pamti <em>vektor vrijednosti</em> u zadanim točkama i svoj tekst. Unarni operator preslikava $f_{c-1} \to f_c$, binarni $f_i \times f_j \to f_{i+j+2}$. Vrijednosti novog izraza računaju se u $O(n)$ iz vrijednosti djece, pa se nijedan podizraz ne evaluira dvaput. Prvi izraz koji zadovolji toleranciju na svim točkama odmah ispišemo.</p>'''),
        ('Što s dijeljenjem i s ispisom – gdje vrebaju pogreške?',
         r'''<p>Dijeljenje s nazivnikom $|q| < 0.01$ u bilo kojoj točki čini izraz nevaljanim, pa ga uopće ne dodajemo u listu (time se ne gubi ništa: sudac takav izraz ne bi prihvatio, a ni njegovi nadizrazi ne bi bili valjani). Pri ispisu svaki operand koji je sam binarni izraz stavi u zagrade – tako prioritet i asocijativnost ne mogu promijeniti značenje (npr. $x-(x-x)$ vs. $x-x-x$), a duljina ostaje daleko ispod $1000$ znakova.</p>'''),
    ],
    'tips': [
        r'''Kad zadatak traži „bilo koji izraz/program iz male gramatike”, prvo prebroji <em>valjane</em> objekte dinamikom po veličini – često ih je za nekoliko redova veličine manje nego što sugerira broj nizova simbola.''',
        r'''Nabrajanje odozdo prema gore uz spremanje <em>vektora vrijednosti</em> (umjesto ponovne evaluacije stabla) pretvara $O(\text{veličina})$ evaluaciju u $O(1)$ po čvoru: to je standardni trik za pretraživanja po izrazima.''',
        r'''Pri ispisu izraza ne pokušavaj biti štedljiv sa zagradama: potpuno zagrađivanje binarnih operanada je uvijek ispravno, a sudac ionako parsira.''',
    ],
    'detailed': r'''
<h3>1. Veličina izraza</h3>
<p>Prikažimo izraz stablom: list je $x$, unarni čvor ($\sin$, $\cos$) ima jedno dijete, binarni čvor ($+$, $-$, $\times$, $\div$) dva. Zagrade nisu čvorovi. Složenost je definirana kao $2b + u$, gdje je $b$ broj binarnih, a $u$ broj unarnih čvorova. Stablo s $b$ binarnih čvorova ima $b + 1$ listova, dakle $2b + 1 + u$ čvorova; uvjet $2b + u \le 9$ daje najviše $10$ čvorova i najviše $4$ binarna operatora.</p>
<h3>2. Koliko ima kandidata</h3>
<p>Neka je $f_c$ broj (sintaktičkih) stabala složenosti točno $c$. Korijen je ili unarni čvor nad stablom složenosti $c-1$ (dvije mogućnosti), ili binarni čvor nad stablima složenosti $i$ i $j$ s $i + j + 2 = c$ (četiri operatora): $$f_0 = 1, \qquad f_c = 2 f_{c-1} + 4 \sum_{i+j=c-2} f_i f_j .$$ Brojevi su $1, 2, 8, 32, 144, 672, 3264, 16256, 82688, 427520$, ukupno $530\,587$. (Službeno rješenje navodi „oko $4 \cdot 10^5$”, jer stabla s nevaljanim dijeljenjem otpadaju.) Svaki izraz evaluiramo u $n \le 20$ točaka, što je oko $10^7$ aritmetičkih operacija – daleko ispod limita.</p>
<h3>3. Izgradnja odozdo prema gore</h3>
<p>Za $c = 0, 1, \dots, 9$ gradimo listu $f_c$; svaki element pamti tekst izraza, vektor vrijednosti $(e(x_1), \dots, e(x_n))$ i zastavicu „korijen je binaran” (zbog zagrada). Postupak:</p>
<ol>
<li>$f_0 = \{x\}$ s vrijednostima $(x_1, \dots, x_n)$.</li>
<li>Za svaki $e \in f_{c-1}$ dodaj $\sin(e)$ i $\cos(e)$; vrijednosti su $\sin(e(x_t))$, $\cos(e(x_t))$.</li>
<li>Za svaki par $(i, j)$ s $i + j + 2 = c$ i svaki $a \in f_i$, $b \in f_j$ dodaj $a \circ b$ za $\circ \in \{+, -, \times, \div\}$. Dijeljenje odbacujemo ako je $|b(x_t)| < 0.01$ za neki $t$.</li>
<li>Svakog kandidata odmah provjerimo: ako je $|e(x_t) - y_t| \le 10^{-3} \max(1, |y_t|)$ za sve $t$, ispišemo tekst i završimo.</li>
</ol>
<p>Izraze složenosti $9$ ne treba spremati (nitko ih ne koristi kao podizraz), što štedi memoriju: spremljeno je oko $10^5$ izraza.</p>
<h3>4. Zašto smijemo odbaciti nevaljana dijeljenja</h3>
<p>Sudac zahtijeva $|q| \ge 0.01$ za svaki nazivnik u svakoj ulaznoj točki. Ako podizraz krši taj uvjet, krši ga i svaki izraz koji ga sadrži (nazivnik se evaluira u istoj točki), pa takav podizraz ne može biti dio valjanog odgovora. Zadatak jamči da postoji rješenje čiji su nazivnici po modulu $\ge 0.02$, dakle ono sigurno preživi naš filtar $0.01$ i pretraživanje ga nađe (ili nađe neko drugo valjano prije njega).</p>
<h3>5. Ispis</h3>
<p>Tekst izraza gradimo iz tekstova djece. Operand koji je sam binarni izraz stavljamo u zagrade; unarne i list ne treba. Time je značenje jednoznačno (npr. $x - (x - x)$ se ne stopi u $x - x - x$, a $(x + x) \times x$ ne postane $x + x \times x$). Najdulji tekst ima nekoliko desetaka znakova, daleko ispod dopuštenih $1000$.</p>
<h3>6. Numerika</h3>
<p>Sve vrijednosti su reda veličine najviše $10^{3 \cdot 5} = 10^{15}$ (npr. $x^5$ nastaje s četiri množenja, složenost $8$), što <code>double</code> podnosi bez problema; $\sin$ i $\cos$ su uvijek konačni. Provjera tolerancije koristi relativnu pogrešku $10^{-3} \max(1, |y|)$, točno kako je definirano u zadatku – zbog toga se rezultat ne mijenja ni s malim razlikama u redoslijedu evaluacije.</p>
<h3>7. Složenost</h3>
<p>Vrijeme $\Theta(n \cdot T(9))$, gdje je $T(9) \approx 5.3 \cdot 10^5$ ukupan broj kandidata; u praksi ispod $0.1$ s. Memorija: $O(n \cdot T(8))$ realnih brojeva za spremljene vektore vrijednosti.</p>
<h3>8. Primjer</h3>
<p>Za točke $(1, 1), (2, 4), (3, 9)$ prvi kandidat složenosti $2$ koji prolazi je $x \times x$ (ispis <code>x*x</code>). Za drugi primjer, $y \approx 1/x^2 \cdot \sin(x)$, pretraživanje nađe izraz složenosti $5$, npr. <code>sin(x)/(x*x)</code>.</p>
''',
    'verified': r'''Konstruktivni zadatak: uzorci 2/2, 300 slučajnih testova provjereno checkerom (gramatika, složenost ≤ 9, duljina ≤ 1000, nazivnici ≥ 0.01, tolerancija 10^-3), 3 velika testa (najviše 0.00 s).''',
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
        ('Koji brid smije koristiti koji put – što nam govori uvjet „svaki brid najviše jednom”?',
         r'''<p>Promotri brid $(v, p_v)$ i podstablo vrha $v$. Svaki par čiji je put kroz taj brid ima točno jedan kraj u podstablu. Kako brid smije koristiti najviše jedan put, iz podstabla „izlazi” najviše jedan označeni vrh; svi ostali označeni vrhovi podstabla spareni su međusobno. Dakle: broj označenih u podstablu paran $\Rightarrow$ ništa ne izlazi; neparan $\Rightarrow$ točno jedan izlazi. Parnost je unaprijed poznata, pa je za svaki brid <em>unaprijed</em> poznato hoće li ga neki put koristiti.</p>'''),
        ('Gdje se par „sklapa” i što se u tom trenutku zna?',
         r'''<p>Put između dva vrha prolazi kroz njihov najniži zajednički predak (LCA). Obrađujemo li stablo od listova prema korijenu, u vrhu $v$ se sastaju kandidati: sam $v$ (ako je označen) i po najviše jedan vrh iz svakog djeteta (onaj koji iz djetetova podstabla izlazi). Parovi koji se ovdje sklapaju koriste različite bridove prema djeci, pa su automatski bridno disjunktni. Iz $v$ prema gore smije otići najviše jedan kandidat, i to samo ako je ukupan broj označenih u podstablu neparan.</p>'''),
        ('Kako spariti kandidate u jednom vrhu i kako znati je li to uopće moguće?',
         r'''<p>Tong se sparuje samo s Tongom <em>iste</em> dubine: u svakoj dubinskoj klasi parovi se sklapaju proizvoljno, a neparna klasa ostavlja jednog kandidata koji mora gore (dvije neparne klase $\Rightarrow$ <code>NO</code>). Chang se sparuje s Duanom tako da je Chang dublji. Sortiraj Changove $C_1 \le \dots \le C_c$ i Duanove $D_1 \le \dots \le D_d$ po dubini: savršeno sparivanje postoji ako i samo ako je $\operatorname{dep}(C_i) > \operatorname{dep}(D_i)$ za sve $i$ (ako ne vrijedi za neko $i$, Changovi $C_1, \dots, C_i$ trebali bi $i$ različitih Duanova strogo plićih od $\operatorname{dep}(C_i)$, a ima ih najviše $i-1$). Brojevi $c$ i $d$ smiju se razlikovati najviše za $1$.</p>'''),
        ('Ako jedan Chang mora otići gore, zašto baš najdublji koji se može zadržati?',
         r'''<p>Vrh koji ide gore sparit će se negdje iznad s Duanom manje dubine (ili se neće moći spariti). Dublji Chang može se spariti sa <em>svakim</em> Duanom s kojim može i plići, pa je poslati dublji uvijek barem jednako dobro – pod uvjetom da ostatak kandidata u $v$ i dalje ima savršeno sparivanje („zadrživ”). Simetrično, od Duanova gore ide najplići zadrživ. Standardni argument zamjene: bilo koje rješenje možemo prepraviti tako da u svakom vrhu šalje gore upravo pohlepni izbor, a da ostane valjano.</p>'''),
        ('Kako provjeriti „zadrživost” svakog kandidata u linearnom vremenu?',
         r'''<p>Ako iz sortiranog niza izbacimo $C_j$, ostatak se sparuje kao $D_i$–$C_i$ za $i < j$ i $D_i$–$C_{i+1}$ za $i \ge j$. Uvjet je konjunkcija prefiksnog dijela ($\operatorname{dep}(C_i) > \operatorname{dep}(D_i)$ za $i < j$) i sufiksnog ($\operatorname{dep}(C_{i+1}) > \operatorname{dep}(D_i)$ za $i \ge j$), a oba se predizračunaju prefiksnim/sufiksnim AND-om u $O(c)$. Prolazimo $j$ od najvećeg prema manjem i uzimamo prvi zadrživ.</p>'''),
    ],
    'tips': [
        r'''Kad su putovi u stablu bridno disjunktni, promatraj svaki brid zasebno: parnost broja „posebnih” vrhova u podstablu odlučuje o njemu. Ta parnosna invarijanta pojavljuje se u mnogim zadacima o sparivanju u stablima.''',
        r'''Sparivanje dviju sortiranih lista uz uvjet „$a_i > b_{\pi(i)}$” provjeravaj sparivanjem $i$-tog s $i$-tim; ispravnost slijedi iz Hallova uvjeta i to je uvijek brže od bilo kakvog općeg algoritma sparivanja.''',
        r'''Za pitanje „koji element smijem izbaciti da ostatak ostane valjan” koristi prefiksne i sufiksne provjere: izbacivanje jednog elementa pomiče indekse samo iza njega.''',
        r'''U rekurziji od listova prema korijenu obradi vrhove u redoslijedu padajućih indeksa kad je zajamčeno $p_i < i$ – nema DFS-a, nema opasnosti od dubine rekurzije.''',
    ],
    'detailed': r'''
<h3>1. Parnosna invarijanta</h3>
<p>Neka je $s_v$ broj označenih vrhova u podstablu vrha $v$ (uključujući $v$). Put para $(a, b)$ prolazi bridom $(v, p_v)$ ako i samo ako je točno jedan od $a, b$ u podstablu od $v$. Budući da svaki brid smije pripadati najviše jednom putu, kroz $(v, p_v)$ prolazi najviše jedan put, tj. najviše jedan označeni vrh podstabla sparen je izvan njega. Preostali označeni vrhovi podstabla spareni su međusobno, a to zahtijeva paran broj. Dakle:</p>
<ul>
<li>$s_v$ paran $\Rightarrow$ nijedan put ne koristi $(v, p_v)$ i podstablo je „zatvoreno”;</li>
<li>$s_v$ neparan $\Rightarrow$ točno jedan vrh iz podstabla sparen je izvan njega, kroz $(v, p_v)$.</li>
</ul>
<p>Posebno, ako je ukupan broj označenih vrhova neparan (ili ako u korijenu ostane nespareni kandidat), rješenja nema.</p>
<h3>2. Struktura svakog rješenja</h3>
<p>Put para prolazi njegovim LCA-om $w$; dva kraja dolaze iz dvaju različitih djece od $w$ ili je jedan kraj sam $w$. Zato svako valjano rješenje ima ovaj oblik: obradimo vrhove od listova prema korijenu; u vrhu $v$ „kandidati” su $v$ (ako je označen) i po jedan vrh iz svakog djeteta s neparnim $s$; neki se kandidati spare međusobno (to su parovi s LCA-om $v$), a najviše jedan ide dalje gore (točno jedan ako je $s_v$ neparan, nijedan inače). Parovi sklopljeni u $v$ koriste bridove prema različitoj djeci i putove unutar podstabala koji su već „rezervirani” izlaskom kandidata, pa su svi putovi bridno disjunktni. Time smo zadatak sveli na lokalni problem u svakom vrhu plus odluku <em>koji</em> kandidat ide gore.</p>
<h3>3. Lokalno sparivanje u vrhu</h3>
<p><strong>Tong.</strong> Sparuje se samo s Tongom jednake dubine, pa kandidate tipa Tong grupiramo po dubini (mapa dubina $\to$ lista). U svakoj grupi sparimo ih redom; grupa neparne veličine ostavlja jednog kandidata koji nužno ide gore. Ako su dvije grupe neparne, dva bi vrha morala izaći istim bridom – <code>NO</code>.</p>
<p><strong>Chang–Duan.</strong> Sortirajmo Changove $C_1, \dots, C_c$ i Duanove $D_1, \dots, D_d$ po dubini. Savršeno sparivanje (pri $c = d$) u kojem je svaki Chang dublji od svog Duana postoji ako i samo ako $\operatorname{dep}(C_i) > \operatorname{dep}(D_i)$ za sve $i$.</p>
<p><em>Dokaz.</em> Ako uvjet vrijedi, sparivanje $C_i$–$D_i$ je valjano. Obratno, neka je $\operatorname{dep}(C_i) \le \operatorname{dep}(D_i)$ za neko $i$. Changovi $C_1, \dots, C_i$ imaju dubinu $\le \operatorname{dep}(C_i)$, pa svaki od njih treba Duana dubine $< \operatorname{dep}(C_i) \le \operatorname{dep}(D_i)$; takvi su Duanovi samo među $D_1, \dots, D_{i-1}$, njih najviše $i - 1$ za $i$ Changova – kontradikcija (Hallov uvjet). $\square$</p>
<p>Ako je $|c - d| \ge 2$, ili $|c - d| = 1$ a neki Tong već mora gore, rješenja nema (previše bi kandidata izlazilo).</p>
<h3>4. Koga poslati gore – pohlepno pravilo i dokaz</h3>
<p>Neka je $c = d + 1$ (slučaj $d = c + 1$ je simetričan). Jedan Chang mora otići gore, a ostali se moraju savršeno spariti s Duanovima. Kažemo da je $C_j$ <em>zadrživ</em> ako ostatak $\{C_i\}_{i \ne j}$ ima savršeno sparivanje s $\{D_i\}$. Pohlepno pravilo: gore šaljemo <strong>najdublji zadrživ</strong> Chang; ako je Duanova više, šaljemo <strong>najplići zadrživ</strong> Duan.</p>
<p><em>Dokaz ispravnosti (argument zamjene).</em> Pretpostavimo da postoji valjano rješenje $R$ i promotrimo prvi vrh $v$ u redoslijedu obrade (djeca prije roditelja) u kojem $R$ šalje gore neki drugi kandidat $u'$ umjesto pohlepnog $u$. Do tog trenutka su se $R$ i pohlepni postupak podudarali, pa su kandidati u $v$ isti; tip izlaznog kandidata određen je brojevima kandidata, pa su $u$ i $u'$ oba Changovi, a $\operatorname{dep}(u) \ge \operatorname{dep}(u')$ jer je $u$ najdublji zadrživ (Tong koji mora gore je jednoznačan do na zamjenu vrhova iste dubine, pa tamo razlike nema). U $R$ je $u'$ iznad $v$ sparen s Duanom $w$ dubine $< \operatorname{dep}(u') \le \operatorname{dep}(u)$. Prepravimo: unutar $v$ ostatak bez $u$ sparimo savršeno (moguće jer je $u$ zadrživ), a $u$ pošaljimo gore i sparimo s $w$ istim putem izvan podstabla (put od $v$ do $w$ isti je kao prije; dio unutar podstabla od $v$ ionako je rezerviran za izlazni kandidat). Uvjet „Chang dublji od Duana” vrijedi jer je $\operatorname{dep}(u) > \operatorname{dep}(w)$. Novo rješenje je valjano i podudara se s pohlepnim u $v$ i svim dubljim vrhovima; indukcijom po vrhovima dobivamo rješenje koje se u potpunosti podudara s pohlepnim. Dakle, ako rješenje postoji, pohlepni postupak ga nalazi; ako pohlepni postupak naiđe na nemogućnost, rješenja nema. $\square$</p>
<p>Napomena: nakon prepravke, kandidati u precima od $v$ mogu se razlikovati od onih u izvornom $R$ – to nije problem, jer smo dobili <em>novo</em> valjano rješenje koje se s pohlepnim podudara u jednom vrhu više, pa argument ponavljamo.</p>
<h3>5. Provjera zadrživosti u $O(c)$</h3>
<p>Izbacimo li $C_j$ iz sortiranog niza, preostali se sparuju kao $D_i$–$C_i$ ($i < j$) i $D_i$–$C_{i+1}$ ($i \ge j$). Definiramo $\text{pref}[j] = \bigwedge_{i<j} [\operatorname{dep}(C_i) > \operatorname{dep}(D_i)]$ i $\text{suf}[j] = \bigwedge_{i \ge j} [\operatorname{dep}(C_{i+1}) > \operatorname{dep}(D_i)]$; $C_j$ je zadrživ ako i samo ako $\text{pref}[j] \wedge \text{suf}[j]$. Oba niza računamo jednim prolazom. Zatim prolazimo $j = c-1, c-2, \dots$ i uzimamo prvi zadrživ; ako ga nema – <code>NO</code>. Za Duanove analogno, s $j$ od najmanjeg.</p>
<h3>6. Algoritam</h3>
<ol>
<li>Pročitaj stablo; dubine $\operatorname{dep}(i) = \operatorname{dep}(p_i) + 1$ računaj redom jer je $p_i < i$.</li>
<li>Obrađuj vrhove $v = n, n-1, \dots, 1$ (djeca prije roditelja). Skupi kandidate: $v$ ako je označen, plus $\text{gore}[u]$ za svako dijete $u$ s $\text{gore}[u] \ne 0$.</li>
<li>Tong: grupiraj po dubini, spari, zapamti eventualni neparni ostatak.</li>
<li>Chang/Duan: sortiraj, provjeri $|c - d| \le 1$ i sukladnost s Tong ostatkom, odaberi izlaznog kandidata prema točki 5, spari ostatak $C_i$–$D_i$ uz provjeru $\operatorname{dep}(C_i) > \operatorname{dep}(D_i)$.</li>
<li>Postavi $\text{gore}[v]$; na kraju, ako je $\text{gore}[1] \ne 0$ – <code>NO</code>; inače ispiši <code>YES</code> i sve sklopljene parove.</li>
</ol>
<h3>7. Složenost</h3>
<p>Vrh $v$ obrađuje najviše $\deg(v) + 1$ kandidata, pa je ukupan broj kandidata $O(n)$; sortiranja i mapa daju $O(n \log n)$ vremena, $O(n)$ memorije. Nema rekurzije – redoslijed padajućih indeksa je već topološki.</p>
<h3>8. Rubni slučajevi</h3>
<ul>
<li>Nijedan označeni vrh: <code>YES</code> bez parova.</li>
<li>Korijen $1$ nije označen; kandidat koji „izađe” iz korijena znači <code>NO</code>.</li>
<li>Chang i Duan iste dubine ne smiju biti par (stroga nejednakost); Tongovi različitih dubina ne smiju biti par.</li>
<li>Više valjanih rasporeda parova je moguće – provjeravač mora provjeravati uvjete, a ne uspoređivati s jednim ispisom.</li>
</ul>
''',
    'verified': r'''Uzorci 2/2, 300 slučajnih malih testova protiv brute forcea (checker uspoređuje YES/NO i provjerava ispisano sparivanje), 3 velika testa (najviše 0.02 s).''',
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
        ('Što se zapravo plaća – ovisi li cijena o tome na koje elemente primjenjujemo pomak?',
         r'''<p>Ne: operacija s pomakom $y$ košta $w_y$ bez obzira na veličinu podskupa $T$. Zato je cijena cijelog postupka jednaka zbroju cijena <em>kupljenih pomaka</em> (multiskup $Y$), a pitanje je samo koje elemente svaki kupljeni pomak pogađa. Element $x$ završi u $0$ ako i samo ako je zbroj pomaka koji su ga pogodili $\equiv -x \pmod n$.</p>'''),
        ('Kad multiskup kupljenih pomaka $Y$ uspijeva poništiti cijeli skup $S$?',
         r'''<p>Svaki element bira svoj podskup od $Y$ (svaka operacija ima vlastiti $T$, pa izbori različitih elemenata ne smetaju jedni drugima). Dakle $Y$ poništava $S$ ako i samo ako je za svaki $x \in S$ ostatak $-x \bmod n$ <em>podzbroj</em> nekog pod-multiskupa od $Y$. Označimo $\Sigma(Y) \subseteq \mathbb{Z}_n$ skup svih podzbrojeva (uvijek sadrži $0$). Uvjet je $-S \subseteq \Sigma(Y)$, pa je $f(S) = \min\{\operatorname{cijena}(Y) : -S \subseteq \Sigma(Y)\}$.</p>'''),
        ('Kako se $\Sigma(Y)$ mijenja dodavanjem jednog pomaka i kako to iskoristiti kao stanje?',
         r'''<p>$\Sigma(Y \cup \{y\}) = \Sigma(Y) \cup (\Sigma(Y) + y)$, gdje je $\Sigma(Y) + y$ ciklički pomak skupa za $y$. Ako skup zapišemo kao bitmasku $R$ duljine $n$, pomak je rotacija maske, a unija je OR. Stanje DP-a je dakle sama maska $R$: $g[R]$ = najmanja cijena multiskupa $Y$ sa $\Sigma(Y) = R$ točno. Prijelaz: $g[R \lor \operatorname{rot}_y(R)] \leftarrow g[R] + w_y$. Kako je nova maska nadskup stare, kao cijeli broj je veća, pa obrada maski u rastućem poretku jamči da je $g[R]$ konačan kad ga koristimo.</p>'''),
        ('Zašto ne možemo jednostavno pročitati $f(S) = g[-S]$?',
         r'''<p>Jer optimalan $Y$ obično generira <em>više</em> ostataka nego što $S$ traži – npr. $Y = \{1, 1\}$ generira $\{0, 1, 2\}$, a to je najjeftiniji način da se dobije $\{1, 2\}$. Točan izraz je $f(S) = \min_{R \supseteq -S} g[R]$. Minimum po nadskupovima za sve maske istodobno računa se standardnim SOS-DP-om (po bitovima: $h[M] \leftarrow \min(h[M], h[M \cup \{b\}])$) u $O(n 2^n)$. Prije toga masku treba „negirati”: $h[S] = g[-S]$.</p>'''),
        ('Kolika je konačna složenost i pazimo li na prelijevanje?',
         r'''<p>Prijelazi: $2^n$ maski $\times$ $n$ pomaka, svaki $O(1)$ bitovnih operacija – za $n = 22$ oko $9 \cdot 10^7$. SOS-DP još $n 2^n$. Cijene su do $22 \cdot 10^9$, pa $g$ držimo u 64-bitnim cijelim brojevima; u završnom zbroju $\sum_S f(S) \cdot \sum_{v \in S} 2^v$ množimo modulo $998244353$ tek nakon što oba faktora svedemo modulo $p$.</p>'''),
    ],
    'tips': [
        r'''Kad cijena operacije ne ovisi o tome na koliko se elemenata primjenjuje, razdvoji „što kupujemo” od „kako to raspoređujemo” – problem se često raspadne na neovisne uvjete po elementima.''',
        r'''Skup ostataka modulo $n$ kao bitmaska: zbrajanje konstante je rotacija maske (<code>((R &lt;&lt; y) | (R &gt;&gt; (n - y))) &amp; full</code>), a unija je OR. Prijelazi ruksaka postaju $O(1)$.''',
        r'''„Minimum/zbroj po svim nadskupovima (ili podskupovima)” za sve maske odjednom je SOS-DP u $O(n 2^n)$ – prepoznaj ga čim se u formuli pojavi $\min_{R \supseteq S}$.''',
        r'''Kad DP-om obrađuješ maske u rastućem poretku i prijelazi vode samo u nadskupove, ne treba ti nikakav poredak po veličini skupa – nadskup je uvijek numerički veći.''',
    ],
    'detailed': r'''
<h3>1. Preoblikovanje: kupovanje pomaka</h3>
<p>Jedna operacija bira podskup $T$ trenutnog multiskupa i pomak $y$ te svaki $x \in T$ zamjenjuje s $(x + y) \bmod n$ uz cijenu $w_y$, <em>neovisno o $|T|$</em>. Promotrimo cijeli postupak kao niz kupnji pomaka $y_1, y_2, \dots, y_k$ (multiskup $Y$) ukupne cijene $\sum w_{y_i}$; pri $i$-toj kupnji svaki element odluči hoće li biti pogođen. Element koji je krenuo od $x$ završi u $0$ ako i samo ako je zbroj pomaka koji su ga pogodili $\equiv -x \pmod n$.</p>
<p>Označimo $\Sigma(Y) = \{\sum_{y \in Y'} y \bmod n : Y' \subseteq Y\}$ skup podzbrojeva (ostataka) multiskupa $Y$; uvijek je $0 \in \Sigma(Y)$ (prazan podskup). Odluke različitih elemenata su neovisne (svaka operacija ima vlastiti $T$), pa vrijedi:</p>
<p style="text-align:center">$Y$ poništava $S$ $\iff$ $-S := \{(-x) \bmod n : x \in S\} \subseteq \Sigma(Y)$,</p>
<p>a time $f(S) = \min \{ \operatorname{cijena}(Y) : -S \subseteq \Sigma(Y) \}$. Redoslijed kupnji nije bitan.</p>
<h3>2. Stanje DP-a: skup podzbrojeva kao bitmaska</h3>
<p>Skup $R \subseteq \mathbb{Z}_n$ zapisujemo kao bitmasku od $n$ bitova. Dodavanje pomaka $y$ u multiskup mijenja skup podzbrojeva prema $$\Sigma(Y \cup \{y\}) = \Sigma(Y) \cup \bigl(\Sigma(Y) + y\bigr),$$ jer novi podskupovi ili ne sadrže $y$ (stari zbrojevi) ili ga sadrže (stari zbroj $+ y$). U bitovima: $R \mapsto R \lor \operatorname{rot}_y(R)$, gdje je $\operatorname{rot}_y$ ciklička rotacija maske za $y$ mjesta: <code>((R &lt;&lt; y) | (R &gt;&gt; (n - y))) &amp; full</code>.</p>
<p>Definiramo $g[R]$ = najmanja cijena multiskupa $Y$ sa $\Sigma(Y) = R$ <em>točno</em>; $g[\{0\}] = 0$ (prazan multiskup), ostalo $\infty$. Prijelaz za svaki $R$ i svaki $y \in [0, n)$: $$g[R \lor \operatorname{rot}_y(R)] \leftarrow \min\bigl(\cdot,\; g[R] + w_y\bigr).$$</p>
<p><strong>Zašto je redoslijed po rastućoj masci ispravan.</strong> Nova maska $R' = R \lor \operatorname{rot}_y(R)$ je nadskup od $R$; ako je $R' \ne R$, kao cijeli broj je strogo veća. Zato svaki multiskup $Y$ s $\Sigma(Y) = R'$ nastaje dodavanjem posljednjeg pomaka nekom $Y_0$ s $\Sigma(Y_0) = R_0 \subsetneq R'$, a $R_0 < R'$ numerički je već obrađen kad dođemo do $R'$. Prijelazi s $R' = R$ ništa ne mijenjaju i smijemo ih preskočiti. (Zbog komutativnosti smijemo pretpostaviti da je „posljednji” pomak bilo koji, pa $g$ zaista pokriva sve multiskupove.) Svaka konačna vrijednost $g[R]$ pripada nekom stvarnom multiskupu, pa je $g$ točno.</p>
<h3>3. Od $g$ do $f$: minimum po nadskupovima</h3>
<p>$f(S) = \min_{R \supseteq -S} g[R]$. Definiramo $h[M] = g[-M]$ (negacija maske: bit $v$ ide na bit $(n - v) \bmod n$), pa je $f(S) = \min_{M \supseteq S} h[M]$. To je klasični SOS-DP po nadskupovima: za svaki bit $b$ i svaku masku $M$ bez bita $b$ postavimo $h[M] \leftarrow \min(h[M], h[M \cup \{b\}])$. Nakon obrade svih bitova $h[S]$ je upravo $f(S)$. Ispravnost: nakon obrade bitova $b_1, \dots, b_k$, $h[M]$ je minimum po svim maskama koje se od $M$ razlikuju samo dodavanjem nekih od tih bitova; indukcija po $k$.</p>
<p>Minimum je uvijek konačan: multiskup od $n - 1$ kopija pomaka $1$ generira sve ostatke, pa je puna maska dostižna.</p>
<h3>4. Odgovor</h3>
<p>$\sum_{\emptyset \ne S} f(S) \cdot \sum_{v \in S} 2^v \bmod 998244353$. Drugi faktor je upravo maska $S$ pročitana kao cijeli broj. $f(S) \le n \cdot 10^9 < 2^{35}$ stane u 64 bita; prije množenja oba faktora svedemo modulo $p$.</p>
<h3>5. Provjera na primjeru</h3>
<p>$n = 3$, $w = (2, 1, 2)$. Vrijednosti $f$: $f(\{0\}) = 0$; $f(\{1\})$ traži ostatak $2$: $Y = \{2\}$ ili $\{1, 1\}$, cijena $2$; $f(\{2\})$ traži $1$: $Y = \{1\}$, cijena $1$; $f(\{1, 2\})$ traži $\{1, 2\}$: $Y = \{1, 1\}$ generira $\{0, 1, 2\}$ za cijenu $2$ (ovdje se vidi zašto treba minimum po <em>nadskupovima</em>); $f(\{0, 1\}) = 2$, $f(\{0, 2\}) = 1$, $f(\{0, 1, 2\}) = 2$. Zbroj $0 \cdot 1 + 2 \cdot 2 + 1 \cdot 4 + 2 \cdot 3 + 1 \cdot 5 + 2 \cdot 6 + 2 \cdot 7 = 45$.</p>
<h3>6. Složenost i implementacija</h3>
<ul>
<li>Prijelazi: $n \cdot 2^n$ rotacija i OR-ova; za $n = 22$ oko $9.2 \cdot 10^7$ jednostavnih operacija.</li>
<li>SOS-DP: $n \cdot 2^n$ minimuma.</li>
<li>Memorija: dva niza od $2^{22}$ 64-bitnih brojeva (po $32$ MB) ili jedan uz negaciju „u mjestu”.</li>
<li>Rotacija za $y = 0$ je identitet (preskoči); pri $y > 0$ pomak <code>R &gt;&gt; (n - y)</code> je dobro definiran jer je $0 < n - y < n \le 22$.</li>
<li>Skupovi $S$ u zadatku nemaju duplikata, pa maska jednoznačno opisuje $S$; početni multiskup s duplikatima ne bi ništa promijenio, jer element dva puta ista vrijednost traži isti ostatak.</li>
</ul>
<p>Ukupno $\Theta(n 2^n)$ vremena i $\Theta(2^n)$ memorije.</p>
''',
    'verified': r'''Uzorci 2/2, 300 slučajnih malih testova protiv brute forcea, 3 velika testa (najviše 0.10 s).''',
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
        r'''<p>Trag s punim brojem ima sve susjede zasjenjene; trag s brojem za jedan manjim („umanjen”) ima točno jednu praznu susjednu ćeliju. Prebroji koliko tragova dodiruje svaka ćelija bez traga: ćelija između dva susjedna traga dodiruje točno $2$, ćelija dijagonalno između četiri traga točno $4$.</p>''',
        r'''<p>Prazna ćelija između dva umanjena traga zadovoljava oba odjednom: sparuj umanjene tragove! Dijagonalna ćelija koja služi četvorici tragova uvijek se može zamijeniti dvjema „stranicama”. Ostaje bipartitno sparivanje — ali uvjet <em>uzastopnosti</em> zabranjuje neka sparivanja (rubni trag s unutarnjim).</p>''',
    ],
    'coach': [
        ('Što uvjet „točno toliko zasjenjenih” govori o pojedinom tragu?',
         r'''<p>Broj na tragu je ili jednak broju susjednih ćelija (sve su zasjenjene) ili za jedan manji (točno jedna susjedna ćelija je prazna). Tragove druge vrste zovimo <em>umanjeni</em>. Cijela sloboda odlučivanja je: za svaki umanjeni trag odabrati <em>koja</em> mu je susjedna ćelija prazna; sve ostale ćelije bez traga su zasjenjene.</p>'''),
        ('Koje tragove pogađa jedna prazna ćelija?',
         r'''<p>Tragovi su na ćelijama s oba neparna indeksa. Ćelija s točno jednim neparnim indeksom leži na „stranici” između dva ortogonalno susjedna traga i dodiruje točno njih dva (dijagonalni susjedi takve ćelije imaju oba indeksa parna, dakle nisu tragovi). Ćelija s oba parna indeksa dodiruje četiri traga dijagonalno. Rubovi ne stvaraju posebne slučajeve, jer je mreža dimenzija $(2n-1) \times (2m-1)$ pa su sve rubne ćelije tragovi ili stranice između dvaju rubnih tragova. Ako je ćelija prazna, <em>svi</em> tragovi koje dodiruje moraju biti umanjeni i to im je jedina prazna ćelija.</p>'''),
        ('Trebamo li uopće prazne dijagonalne ćelije?',
         r'''<p>Ne. Prazna dijagonalna ćelija $(i+1, j+1)$ opslužuje četiri traga $(i,j), (i,j+2), (i+2,j), (i+2,j+2)$. Umjesto nje ispraznimo stranice $(i, j+1)$ i $(i+2, j+1)$: svaki od četiri traga i dalje ima točno jednu praznu susjednu ćeliju, a stranice ne dodiruju druge tragove. Provjera uzastopnosti: za unutarnji trag svaka od $8$ susjednih ćelija smije biti prazna (ostalih $7$ je uvijek povezan luk), pa zamjena ništa ne kvari. Dakle dovoljno je sparivati umanjene tragove u <em>ortogonalno susjedne</em> parove.</p>'''),
        ('Gdje uvjet uzastopnosti zabranjuje par?',
         r'''<p>Rubni trag nema puni krug susjeda nego luk: kutni trag ima $3$ susjeda, rubni $5$. Ako je prazna ćelija u <em>unutrašnjosti</em> luka, preostale zasjenjene ćelije nisu uzastopne. Krajevi luka su upravo stranice uz rub mreže, pa rubni umanjeni trag može biti sparen samo s rubnim susjedom <em>duž istog ruba</em>; par „rubni – unutarnji” (preko stranice okomite na rub) nije dopušten. To je ono što službeno rješenje zove „vanjski rubni tragovi i središnja $7$ ne mogu se spariti”.</p>'''),
        ('Koji algoritam rješava „spari sve umanjene tragove u dopuštene parove”?',
         r'''<p>Graf s vrhovima u umanjenim tragovima i bridovima među dopuštenim ortogonalnim parovima je podgraf mreže, a mreža je bipartitna (šahovsko bojenje po parnosti $a + b$ za trag $(2a, 2b)$). Trebamo savršeno sparivanje: Kuhnov algoritam u $O(V E)$ s $V \le 2500$, $E \le 5000$ je više nego dovoljan; Hopcroft–Karp daje $O(E \sqrt V)$. Ako savršeno sparivanje ne postoji – <code>NO</code>; inače ispraznimo stranice između sparenih tragova, ostalo zasjenimo.</p>'''),
    ],
    'tips': [
        r'''Kod zadataka „konstruiraj raspored koji zadovoljava lokalne brojčane uvjete” prvo prebroji koliko slobode uopće ima: ovdje je svaki trag ili potpuno određen ili ima točno jednu odluku, pa problem odmah postaje kombinatoran, a ne pretraživanje.''',
        r'''Kad jedan odabir može zadovoljiti više uvjeta odjednom (prazna ćelija „hrani” dva traga), pokušaj pokazati da se složeniji odabiri (ćelija za četiri traga) mogu zamijeniti kombinacijom jednostavnih – redukcija na sparivanje tada postaje čista.''',
        r'''Mrežasti grafovi su bipartitni (šahovsko bojenje) – „spari susjedne ćelije” gotovo uvijek znači bipartitno sparivanje, a za $\le 10^4$ vrhova Kuhnov algoritam je posve dovoljan.''',
        r'''Uvjete poput „zasjenjene ćelije moraju biti uzastopne” provjeri zasebno za kutne, rubne i unutarnje slučajeve – ograničenja se razlikuju upravo tamo gdje je susjedstvo nepotpuno.''',
    ],
    'detailed': r'''
<h3>1. Što se uopće odlučuje</h3>
<p>Trag na ćeliji $(2a, 2b)$ (indeksi od $0$) ima $k$ susjednih ćelija: $3$ u kutu, $5$ na rubu, $8$ u unutrašnjosti. Vrijednost traga je $k$ ili $k - 1$. Ako je $k$, sve su mu susjedne ćelije zasjenjene; ako je $k - 1$ (<em>umanjen</em> trag), točno jedna susjedna ćelija je prazna. Svaka ćelija bez traga susjedna je barem jednom tragu, pa je jedina sloboda: za svaki umanjeni trag odabrati praznu susjednu ćeliju. Ćelija koja nije odabrana ni za jedan trag mora biti zasjenjena.</p>
<h3>2. Koje tragove dodiruje ćelija bez traga</h3>
<ul>
<li><strong>Stranica</strong> – ćelija s točno jednim neparnim indeksom, npr. $(2a, 2b+1)$. Njezini susjedi s oba parna indeksa su tragovi $(2a, 2b)$ i $(2a, 2b+2)$; dijagonalni susjedi $(2a \pm 1, 2b)$, $(2a \pm 1, 2b + 2)$ imaju jedan neparan indeks, pa nisu tragovi. Dodiruje točno $2$ traga, i oba postoje jer je $2b + 2 \le 2m - 2$.</li>
<li><strong>Dijagonalna ćelija</strong> – oba indeksa neparna, $(2a+1, 2b+1)$; dodiruje četiri traga $(2a, 2b)$, $(2a, 2b+2)$, $(2a+2, 2b)$, $(2a+2, 2b+2)$.</li>
</ul>
<p>Ako je ćelija prazna, svaki trag koji dodiruje mora biti umanjen i ta mu je ćelija jedina prazna. Dakle prazna stranica „sparuje” dva ortogonalno susjedna umanjena traga, a prazna dijagonalna ćelija četiri traga.</p>
<h3>3. Dijagonalne ćelije nisu potrebne</h3>
<p>Neka je u nekom valjanom rješenju prazna dijagonalna ćelija $(2a+1, 2b+1)$. Sva četiri traga oko nje moraju biti unutarnja: za rubni trag dijagonalna ćelija leži u unutrašnjosti njegova luka susjeda, pa bi preostale zasjenjene ćelije bile nepovezane (točka 4). Zamijenimo tu ćeliju zasjenjenom i ispraznimo stranice $(2a, 2b+1)$ i $(2a+2, 2b+1)$. Tragovi $(2a, 2b)$ i $(2a, 2b+2)$ sada dijele prvu stranicu, $(2a+2, 2b)$ i $(2a+2, 2b+2)$ drugu; svaki od četvorice i dalje ima točno jednu praznu ćeliju, a stranice ne dodiruju nijedan drugi trag. Za unutarnji trag svaka pojedina prazna susjedna ćelija ostavlja preostalih $7$ uzastopnih, pa zamjena čuva valjanost. Zaključak: <strong>postoji rješenje ako i samo ako postoji rješenje bez praznih dijagonalnih ćelija</strong>.</p>
<h3>4. Uvjet uzastopnosti i rubni tragovi</h3>
<p>Susjedne ćelije traga u kružnom poretku čine: puni krug od $8$ (unutarnji trag), luk od $5$ (rubni) ili luk od $3$ (kutni). Ako iz kruga izbacimo jednu ćeliju, ostatak je uvijek uzastopan. Ako iz luka izbacimo ćeliju iz unutrašnjosti, ostatak se raspada na dva dijela – zabranjeno; smijemo izbaciti samo krajnju ćeliju luka. Krajnje ćelije luka rubnog traga $(0, 2b)$ su $(0, 2b-1)$ i $(0, 2b+1)$ – stranice <em>uz rub</em>; kutnog traga $(0,0)$ krajevi su $(0,1)$ i $(1,0)$. Zaključak: rubni umanjeni trag može biti sparen samo s rubnim susjedom duž istog ruba. Par rubnog traga s unutarnjim (preko stranice okomite na rub, npr. $(1, 2b)$ između $(0,2b)$ i $(2,2b)$) nije dopušten – to je slučaj „vanjski rubni trag i središnja $7$” iz službenog rješenja. Dva unutarnja umanjena traga (dvije $7$) smiju se spariti preko bilo koje zajedničke stranice.</p>
<h3>5. Redukcija na bipartitno sparivanje</h3>
<p>Vrhovi: umanjeni tragovi. Brid: između ortogonalno susjednih umanjenih tragova, osim ako je jedan od njih rubni a stranica između njih nije na rubu mreže. Tražimo <strong>savršeno sparivanje</strong> (svaki umanjeni trag točno jedan par). Graf je bipartitan: trag $(2a, 2b)$ bojamo parnošću $a + b$, a ortogonalno susjedni tragovi imaju različitu parnost. Ako savršeno sparivanje ne postoji, rješenja nema (svako rješenje bez dijagonalnih ćelija je savršeno sparivanje, a po točki 3 dovoljno je gledati takva). Ako postoji, konstrukcija: sve ćelije bez traga zasjenimo, a za svaki par $(2a,2b)$–$(2a',2b')$ ispraznimo stranicu $(a + a', b + b')$. Svaki umanjeni trag tada ima točno jednu praznu susjednu ćeliju (stranice različitih parova dodiruju disjunktne skupove tragova), neumanjeni tragovi nemaju nijednu, a uzastopnost vrijedi po točki 4.</p>
<h3>6. Algoritam i složenost</h3>
<ol>
<li>Za svaki trag izbroji susjede i odredi je li umanjen.</li>
<li>Za umanjene tragove parne boje dodaj bridove prema dopuštenim umanjenim susjedima.</li>
<li>Kuhnov algoritam (DFS po povećavajućim putovima) – $V = nm \le 2500$, $E \le 2V$, složenost $O(VE) \approx 10^7$ u najgorem slučaju, u praksi puno brže.</li>
<li>Ako je broj sparenih parova $\cdot 2 \ne$ broj umanjenih tragova – <code>NO</code>; inače ispiši mrežu.</li>
</ol>
<h3>7. Rubni slučajevi</h3>
<ul>
<li>Nijedan umanjeni trag: <code>YES</code>, sve ćelije bez traga zasjenjene.</li>
<li>Neparan broj umanjenih tragova: nužno <code>NO</code> (sparivanje to automatski otkrije).</li>
<li>Vrijednost traga koja nije ni $k$ ni $k-1$ zadatak ne dopušta, pa je ne treba obrađivati.</li>
<li>Više valjanih rasporeda je moguće, pa provjeravač mora ponovno izbrojati zasjenjene susjede i provjeriti uzastopnost umjesto uspoređivanja s jednim ispisom.</li>
</ul>
''',
    'verified': r'''Uzorci 3/3, 300 slučajnih malih testova protiv brute forcea (checker uspoređuje YES/NO i provjerava valjanost ispisane mreže), 3 velika testa (najviše 0.00 s).''',
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
        ('Što se događa s nulom i zašto je to poseban slučaj?',
         r'''<p>$0 \in S_c$ vrijedi ako i samo ako je $c = 0$ ili $0 \in S$. Ako $0 \notin S$, svi $c \ne 0$ daju $\operatorname{mex} = 0$, a $c = 0$ daje $S_0 = \{0\}$ s mexom $1$ – odgovor je samo $c = 0$. Ako je $0 \in S$, nula je u svakom $S_c$, a $c = 0$ daje mex $1$; zanimljivi su $c \ne 0$, gdje množenje s $c$ permutira nenul ostatke.</p>'''),
        ('Kako uvjet „$\operatorname{mex}(S_c) \ge W$” prevesti u uvjet na $S$?',
         r'''<p>$\operatorname{mex}(S_c) \ge W$ znači $\{0, 1, \dots, W-1\} \subseteq S_c$. Za $c \ne 0$ i $d = c^{-1} \bmod p$: $k \in S_c \iff k d \in S$. Dakle $\operatorname{mex}(S_c) \ge W \iff d, 2d, \dots, (W-1)d \in S$. Uvjet je monoton u $W$, pa najveći mex nalazimo binarnim pretraživanjem po $W \in [1, n]$ (mex ne može premašiti $|S_c| = n$); u svakom koraku moramo za <em>sve</em> $d$ istodobno provjeriti vrijedi li uvjet.</p>'''),
        ('Kako množenje modulo $p$ pretvoriti u nešto što znamo brzo računati?',
         r'''<p>Uzmemo primitivni korijen $g$: svaki $x \in [1, p)$ je $g^{I(x)}$ za jedinstveni eksponent $I(x) \in \mathbb{Z}_{p-1}$, a množenje postaje zbrajanje eksponenata modulo $L = p - 1$. Uvjet „$kd \in S$ za sve $k < W$” glasi „$I(k) + x \in I(S)$ za sve $k \in [1, W)$”, gdje je $d = g^x$. Zbrajanje indeksa = pomak niza, pa je „koliko od $W-1$ traženih pomaka pogađa $S$” ciklička korelacija indikatora skupa $I(S)$ i indikatora skupa $\{I(1), \dots, I(W-1)\}$, koja se računa NTT-om.</p>'''),
        ('Kako iz konvolucije izvući točan broj pogodaka i zašto je to dovoljno?',
         r'''<p>Neka je $A[i] = [g^i \in S]$ i $B[t] = [\,t \equiv -I(k) \text{ za neki } k \in [1, W)\,]$. Tada $(A * B)[x] = \sum_{k<W} A[x + I(k)]$ točno broji koliko je od potrebnih elemenata $kd$ u $S$; vrijednost $W - 1$ znači da su svi. Konvolucija je ciklička duljine $L$, pa linearnu konvoluciju duljine $2L$ „preklopimo”: $C[x] = P[x] + P[x + L]$. Brojevi su najviše $W - 1 < p$, daleko ispod modula NTT-a, pa nema dvosmislenosti.</p>'''),
        ('Kolika je složenost i koje su zamke u implementaciji?',
         r'''<p>Diskretni logaritmi svih ostataka računaju se jednim prolazom po potencijama $g$ u $O(p)$. Binarno pretraživanje ima $O(\log n)$ koraka, svaki jedan NTT unaprijed (transformirani $A$ računamo jednom) plus množenje i inverzni NTT veličine $2^{\lceil \log_2 2L \rceil}$: ukupno $O(p \log^2 p)$. Zamke: $p = 2$ (tada $L = 1$, $g = 1$); $S = \{0\}$ (mex $1$ za svaki $c$, ispisuju se svi $c$); pretvorba natrag $c = d^{-1} = g^{-x} = g^{(L - x) \bmod L}$; ispis $c$-ova rastuće (treba sortirati).</p>'''),
    ],
    'tips': [
        r'''Množenje modulo prostog broja preko primitivnog korijena postaje zbrajanje eksponenata – čim vidiš „$c \cdot x \bmod p$ za sve $c$”, pomisli na diskretni logaritam i konvoluciju.''',
        r'''„Postoji li pomak $x$ takav da cijeli skup $T + x$ upada u $S$” = ciklička korelacija indikatora; vrijednost $|T|$ znači potpun pogodak. FFT/NTT to rješava u $O(p \log p)$ za sve $x$ odjednom.''',
        r'''Kad je svojstvo monotono („mex $\ge W$”), binarno pretraži prag i pri svakom koraku ponovno iskoristi već transformirani, nepromijenjeni faktor konvolucije – štedi trećinu vremena.''',
        r'''Diskretne logaritme za <em>sve</em> ostatke ne računaj BSGS-om po elementu: jedna petlja po potencijama $g$ daje tablicu $\log$ u $O(p)$.''',
    ],
    'detailed': r'''
<h3>1. Nula i $c = 0$</h3>
<p>$S_c = \{c x \bmod p : x \in S\}$. Za $c = 0$ je $S_0 = \{0\}$, mex $= 1$. Za $c \ne 0$ množenje s $c$ je bijekcija na $\mathbb{Z}_p$ koja fiksira $0$, pa $0 \in S_c \iff 0 \in S$. Ako $0 \notin S$, svi $c \ne 0$ imaju mex $0$, a jedini maksimum ($1$) postiže $c = 0$: ispis <code>1 1</code> i <code>0</code>. Dalje pretpostavljamo $0 \in S$; tada je mex svakog $S_c$ barem $1$.</p>
<h3>2. Uvjet za mex $\ge W$</h3>
<p>Za $c \ne 0$ i $d = c^{-1}$: $k \in S_c \iff k d \in S$. Stoga $$\operatorname{mex}(S_c) \ge W \iff d, 2d, \dots, (W-1)d \in S .$$ Svojstvo je monotono u $W$, a mex ne može premašiti $|S_c| = n$ (a ni $p$), pa najveći mogući mex $W^\ast$ nalazimo binarnim pretraživanjem na $[1, n]$: provjera za zadano $W$ mora reći postoji li barem jedan $d$ koji zadovoljava uvjet, a na kraju i naći sve takve $d$. Skup $c$-ova s $\operatorname{mex} = W^\ast$ je tada točno skup $c = d^{-1}$ za sve takve $d$ (nitko nema mex $\ge W^\ast + 1$). Ako je $W^\ast = 1$, svi $c \in [0, p)$ imaju mex $1$ pa ispisujemo sve.</p>
<h3>3. Primitivni korijen i diskretni logaritam</h3>
<p>Za prost $p$ postoji $g$ čije potencije $g^0, g^1, \dots, g^{p-2}$ prolaze sve nenul ostatke. Nađemo ga tako da faktoriziramo $p - 1$ i provjerimo za kandidate $g = 2, 3, \dots$ da je $g^{(p-1)/q} \ne 1$ za sve proste $q \mid p - 1$ (očekivano vrlo malo kandidata). Zatim jednim prolazom izračunamo $\operatorname{potg}[i] = g^i$ i $\operatorname{lg}[g^i] = i$ za $i \in [0, L)$, $L = p - 1$ – to su diskretni logaritmi $I(x)$ za sve $x \ne 0$ u $O(p)$.</p>
<p>Uz $d = g^x$ i $k = g^{I(k)}$ imamo $kd = g^{I(k) + x}$ (eksponenti modulo $L$). Uvjet iz točke 2 glasi: $$I(k) + x \in I(S \setminus \{0\}) \quad \text{za sve } k \in [1, W) .$$</p>
<h3>4. Ciklička korelacija NTT-om</h3>
<p>Neka je $A[i] = [g^i \in S]$ za $i \in [0, L)$ i $B[t] = [\,t \equiv -I(k) \pmod L \text{ za neki } k \in [1, W)\,]$ (svi $I(k)$ su različiti jer su $k$ različiti). Ciklička konvolucija $$C[x] = \sum_{t} B[t] \, A[(x - t) \bmod L] = \sum_{k=1}^{W-1} A[(x + I(k)) \bmod L]$$ broji koliko je od potrebnih elemenata $kd$ u $S$. Dakle $d = g^x$ zadovoljava uvjet ako i samo ako $C[x] = W - 1$.</p>
<p>NTT računa linearnu konvoluciju; zato uzmemo veličinu transformacije $\text{sz} \ge 2L$, izračunamo linearni umnožak $P$ i preklopimo ga: $C[x] = P[x] + P[x + L]$ za $x \in [0, L)$. Vrijednosti su cijeli brojevi $\le W - 1 < 2 \cdot 10^5$, daleko manje od modula $998244353$, pa ih čitamo bez dvosmislenosti. Transformirani $A$ ne ovisi o $W$, pa ga transformiramo jednom; po koraku binarnog pretraživanja treba jedan NTT za $B$, množenje po točkama i jedan inverzni NTT.</p>
<h3>5. Algoritam</h3>
<ol>
<li>Pročitaj $S$; ako $0 \notin S$, ispiši <code>1 1</code> / <code>0</code>.</li>
<li>Nađi $g$, tablice $\operatorname{potg}$ i $\operatorname{lg}$; izračunaj $\hat A = \operatorname{NTT}(A)$.</li>
<li>Binarno pretraživanje $W \in [1, n]$: $W = 1$ uvijek vrijedi; za $W \ge 2$ izgradi $B$, izračunaj $C$ i provjeri postoji li $x$ s $C[x] = W - 1$.</li>
<li>Za konačni $W^\ast$: ako je $1$, odgovor su svi $c \in [0, p)$; inače za svaki $x$ s $C[x] = W^\ast - 1$ uzmi $c = g^{-x} = \operatorname{potg}[(L - x) \bmod L]$, sortiraj i ispiši.</li>
</ol>
<h3>6. Složenost</h3>
<p>Faktorizacija $p - 1$ u $O(\sqrt p)$, tablice u $O(p)$. Binarno pretraživanje: $O(\log n)$ koraka, svaki $O(\text{sz} \log \text{sz})$ sa $\text{sz} < 4p$. Ukupno $O(p \log^2 p)$ po testu; zbog $\sum p \le 2 \cdot 10^5$ to je i ukupna složenost (za $p \approx 2 \cdot 10^5$ NTT veličine $2^{19}$, oko $18$ koraka – ispod sekunde). Memorija $O(p)$.</p>
<h3>7. Rubni slučajevi i zamke</h3>
<ul>
<li>$p = 2$: $L = 1$, $g = 1$, $\operatorname{lg}[1] = 0$; sve formule i dalje vrijede (sz $= 2$).</li>
<li>$S = \{0\}$: $n = 1$, pa je $W^\ast = 1$ i ispisuju se svi $c$ – uključujući $c = 0$.</li>
<li>Kad je $W^\ast \ge 2$, $c = 0$ nikad nije u odgovoru (njegov mex je $1$).</li>
<li>$c$-ovi izlaze iz konvolucije u poretku eksponenata, ne po vrijednosti – obavezno sortirati.</li>
<li>$n = p$: mex može biti $p$ (npr. $S = \mathbb{Z}_p$, tada svaki $c \ne 0$ daje mex $p$); binarno pretraživanje s $\text{hi} = n = p$ to pokriva.</li>
</ul>
<h3>8. Primjer</h3>
<p>$S = \{2, 3, 4\}$, $p = 5$: $0 \notin S$, pa je odgovor samo $c = 0$ s mexom $1$. Drugi primjer: $S = \{0, 1, 2\}$, $p = 5$, $g = 2$ ($2^0..2^3 = 1, 2, 4, 3$), $I(1) = 0$, $I(2) = 1$. $W = 3$: tražimo $d$ s $d, 2d \in \{1, 2\}$, tj. $x$ s $x, x + 1 \in I(\{1, 2\}) = \{0, 1\}$: $x = 0$, $d = 1$, $c = 1$. $W = 4$ bi trebao i $3d \in S$, $3 \notin S$ – ne. Odgovor: <code>1 3</code> / <code>1</code>.</p>
''',
    'verified': r'''Uzorak 1/1, 300 slučajnih malih testova protiv brute forcea, 3 velika testa (najviše 0.74 s).''',
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
        ('Zašto je „najbolji multiskup do stupa $i$” dobro definirano DP stanje?',
         r'''<p>Neka je $f_i$ leksikografski najveći nerastuće sortirani niz jagoda na nekom putu $1 \to i$. Ako iz $j$ skačemo na $i$, novi niz je $f_j$ s umetnutim $a_i$. Ključno: umetanje istog elementa u dva multiskupa <em>čuva njihov poredak</em>. Naime, poredak određuje najveća vrijednost $v$ čije se brojnosti razlikuju (multiskup s više kopija $v$ je veći, jer se dotad nizovi podudaraju, a onda jedan ima $v$, drugi nešto manje ili kraj); dodavanje $a_i$ mijenja brojnosti obaju multiskupova jednako, pa $v$ i smjer nejednakosti ostaju isti. Zato vrijedi optimalna podstruktura: $f_i = \max_j f_j \cup \{a_i\}$ po dopuštenim $j$.</p>'''),
        ('Koji su $j$ dopušteni i kako izbjeći $\Theta(n^2)$ prijelaza?',
         r'''<p>Uvjet $L \le x_i - x_j \le R$ je $x_j \in [x_i - R, x_i - L]$. Kako su $x_i$ rastući, taj se prozor s rastućim $i$ samo pomiče udesno: stupovi ulaze i izlaze u istom redoslijedu. Za maksimum u kliznom prozoru koristimo monotoni deque (red s dvostrukim krajem): pri ulasku $j$ izbacujemo sa stražnjeg kraja sve $f$ koji nisu veći od $f_j$, s prednjeg kraja izbacujemo prestare, a maksimum je uvijek sprijeda. Svaki $f_j$ uđe i izađe jednom: $O(n)$ usporedbi ukupno.</p>'''),
        ('Kako usporediti dva sortirana niza brže nego u $O(n)$?',
         r'''<p>Trebamo najveću vrijednost s različitim brojnostima. Prikažimo multiskup segmentnim stablom nad vrijednostima $1..n$ u kojem svaki čvor pamti <em>hash</em> svog podstabla: zbroj $h(v) \cdot \operatorname{cnt}(v)$ po vrijednostima u čvoru, gdje su $h(v)$ slučajni 64-bitni brojevi. Dva podstabla s jednakim sadržajem imaju jednak hash, različit sadržaj daje različit hash s vjerojatnošću koja se od $1$ razlikuje za red veličine $2^{-64} n$. Spuštamo se paralelno u oba stabla: ako se desni sinovi razlikuju, idemo desno (tamo je veća vrijednost s razlikom), inače lijevo. $O(\log n)$ po usporedbi.</p>'''),
        ('Kako imati segmentno stablo za svaki od $n$ multiskupova, a ne potrošiti $O(n^2)$?',
         r'''<p>Perzistentno segmentno stablo: umetanje $a_i$ u stablo od $f_j$ stvara samo $O(\log n)$ novih čvorova duž jednog puta, a ostatak dijeli s $f_j$. Svi $f_i$ zajedno zauzimaju $O(n \log n)$ čvorova. Usporedba iz prethodnog koraka radi nepromijenjeno, jer čita samo hasheve i sinove. Ispis rezultata je obilazak stabla $f_n$ zdesna nalijevo.</p>'''),
        ('Gdje su zamke u implementaciji za $\sum n \le 10^6$?',
         r'''<p>Memorija: oko $n(\lceil \log_2 n \rceil + 2)$ čvorova, svaki s dva indeksa i 64-bitnim hashom – oko $350$ MB za $n = 10^6$, dopušteno uz $1024$ MB, ali nizove treba alocirati jednom i ponovno koristiti među testovima. Ulaz/izlaz: brzo čitanje i izlaz sastavljen u jednom <code>string</code>-u. Koordinate do $10^9$ uz $R$ do $10^9$: $x_i - R$ računaj u 64 bita ili pazi na negativne vrijednosti. Nedostižni stupovi ne ulaze u deque; ako je $f_n$ nedefiniran, ispis je $-1$.</p>'''),
    ],
    'tips': [
        r'''Leksikografski poredak sortiranih multiskupova određuje <em>najveća vrijednost s različitom brojnošću</em>; segmentno stablo nad vrijednostima s hashevima nalazi je u $O(\log n)$ – to je standardni alat za DP čija su stanja cijeli nizovi.''',
        r'''Prije nego što optimiziraš DP nad nizovima, dokaži da operacija prijelaza (ovdje umetanje elementa) čuva poredak stanja – bez toga „uzmi maksimum pa dodaj” nije ispravno.''',
        r'''Prozor $[x_i - R, x_i - L]$ nad rastućim koordinatama je klizni prozor: monotoni deque daje maksimum u amortiziranom $O(1)$ usporedbi po elementu.''',
        r'''Kad trebaš „verziju” strukture za svako stanje DP-a, perzistentnost (kopiranje jednog puta od korijena do lista) košta $O(\log n)$ po verziji umjesto $O(n)$.''',
    ],
    'detailed': r'''
<h3>1. DP nad multiskupovima i zašto je ispravan</h3>
<p>Skupljene jagode ovise samo o skupu posjećenih stupova, a ispis je nerastuće sortiran niz – dakle multiskup vrijednosti. Za multiskupove $A, B$ definiramo $A \succ B$ ako je sortirani niz od $A$ leksikografski veći (kraći niz koji je prefiks duljeg je manji). Neka je $f_i$ najveći multiskup po svim putovima $1 \to i$ (ili „nedostižno”).</p>
<p><strong>Lema.</strong> Poredak $A \succ B$ određen je najvećom vrijednošću $v$ za koju je $\operatorname{cnt}_A(v) \ne \operatorname{cnt}_B(v)$: $A \succ B \iff \operatorname{cnt}_A(v) > \operatorname{cnt}_B(v)$. <em>Dokaz.</em> Elementi $> v$ imaju jednake brojnosti, pa se nizovi podudaraju na tom prefiksu. Zatim slijede kopije $v$: niz s više kopija na prvoj razlici ima $v$, a drugi ima element $< v$ ili završava – u oba slučaja je prvi veći. $\square$</p>
<p><strong>Korolar (čuvanje poretka).</strong> $A \succ B \Rightarrow A \cup \{a\} \succ B \cup \{a\}$, jer dodavanje $a$ objema mijenja brojnost iste vrijednosti za $1$ pa najveća razlikujuća vrijednost i smjer nejednakosti ostaju isti. Zato vrijedi rekurzija $$f_i = \Bigl(\max_{j:\; L \le x_i - x_j \le R,\; f_j \text{ def.}} f_j\Bigr) \cup \{a_i\}, \qquad f_1 = \{a_1\},$$ i odgovor je $f_n$. (Optimalni put do $i$ prolazi kroz neki $j$; zamijenimo li njegov dio do $j$ s $f_j$, dobivamo po korolaru barem jednako dobar put.)</p>
<h3>2. Klizni prozor</h3>
<p>Dopušteni $j$ zadovoljavaju $x_j \in [x_i - R, x_i - L]$. Budući da su $x$ strogo rastući, obje granice prozora rastu s $i$: stup $j$ ulazi u prozor kad $x_j \le x_i - L$ (pokazivač <code>ptr</code>) i izlazi kad $x_j < x_i - R$. Održavamo deque indeksa čiji su $f$ strogo padajući od prednjeg prema stražnjem kraju: pri ulasku $j$ (ako je dostižan) uklanjamo sa stražnjeg kraja sve $k$ s $f_k \preceq f_j$ (ti $k$ više nikad ne mogu biti maksimum, jer izlaze prije $j$ i nisu bolji), zatim dodajemo $j$; s prednjeg kraja uklanjamo prestare; maksimum je sprijeda. Svaki indeks uđe i izađe najviše jednom, pa je ukupno $O(n)$ usporedbi.</p>
<h3>3. Usporedba u $O(\log n)$: segmentno stablo s hashevima</h3>
<p>Multiskup prikazujemo segmentnim stablom nad vrijednostima $[1, n]$; list $v$ pamti $\operatorname{cnt}(v)$. Svakoj vrijednosti unaprijed dodijelimo slučajni 64-bitni $h(v)$; hash čvora je $\sum_{v \in \text{čvor}} h(v) \operatorname{cnt}(v)$ (zbrajanje modulo $2^{64}$, prirodno prelijevanje), pa je hash roditelja zbroj hasheva sinova i umetanje ažurira $O(\log n)$ hasheva.</p>
<p>Usporedba korijena $u$ i $v$: ako su hashevi jednaki, multiskupovi su jednaki (uz zanemarivu vjerojatnost pogreške). Inače: ako se hashevi desnih sinova razlikuju, najveća razlikujuća vrijednost je u desnoj polovici – spuštamo se desno; inače lijevo. U listu usporedimo brojnosti. To je $O(\log n)$ koraka i po lemi daje točan poredak.</p>
<p><em>Vjerojatnost pogreške.</em> Različiti multiskupovi imaju jednake hasheve samo ako je $\sum h(v) \,(\operatorname{cnt}_A(v) - \operatorname{cnt}_B(v)) \equiv 0 \pmod{2^{64}}$; uz slučajne $h(v)$ i barem jedan koeficijent $d \ne 0$ to se događa s vjerojatnošću najviše $2^{-64} \cdot \gcd(d, 2^{64}) \le n / 2^{64}$ po paru čvorova. Uz $O(n \log n)$ usporedbi podstabala ukupna vjerojatnost pogreške je reda $10^{-6}$ u najgorem teoretskom slučaju, a u praksi mnogo manja.</p>
<h3>4. Perzistentnost</h3>
<p>$f_i$ nastaje iz $f_j$ umetanjem $a_i$. Umjesto kopiranja cijelog stabla stvaramo nove čvorove samo na putu od korijena do lista $a_i$ ($\lceil \log_2 n \rceil + 1$ čvorova), a sinove izvan puta dijelimo sa stablom od $f_j$. Sva stabla zajedno imaju $O(n \log n)$ čvorova; čvor $0$ je zajedničko prazno stablo. Usporedba i ispis rade samo čitanjem, pa im dijeljenje čvorova ne smeta.</p>
<h3>5. Algoritam</h3>
<ol>
<li>Za svaki test: alociraj (ili ponovno iskoristi) nizove za $n(\lceil\log_2 n\rceil + 2) + 2$ čvorova; slučajni $h(v)$ za $v \in [1, n]$.</li>
<li>$\text{korijen}[1] \gets$ umetni $a_1$ u prazno stablo; ostali korijeni $-1$ (nedostižno).</li>
<li>Za $i = 2..n$: pomakni <code>ptr</code> i ubaci dostižne stupove u deque uz izbacivanje sa stražnjeg kraja; izbaci prestare sprijeda; ako deque nije prazan, $\text{korijen}[i] \gets$ umetni $a_i$ u stablo prednjeg elementa.</li>
<li>Ako je $\text{korijen}[n] = -1$, ispiši $-1$; inače obiđi stablo zdesna nalijevo i ispiši brojnosti (duljina niza = broj posjećenih stupova).</li>
</ol>
<h3>6. Složenost</h3>
<p>Umetanja: $n$ puta $O(\log n)$. Usporedbe: $O(n)$ puta $O(\log n)$. Ispis: $O(n)$. Ukupno $\Theta(n \log n)$ vremena i $\Theta(n \log n)$ memorije; za $n = 10^6$ oko $2.2 \cdot 10^7$ čvorova po $16$ bajtova ($\approx 350$ MB, unutar $1024$ MB). Na najvećem testu rješenje radi ispod $1$ s.</p>
<h3>7. Zamke</h3>
<ul>
<li>$x_i - R$ može biti negativno; koordinate i $L, R$ drži u 64-bitnim tipovima ili pazi na predznak.</li>
<li>Stup $1$ je uvijek dostižan; ako je $n = 1$, odgovor je $1$ i $a_1$ (deque se ne koristi).</li>
<li>Deque smije sadržavati samo dostižne stupove; nedostižan $j$ preskoči pri ulasku.</li>
<li>Brzi ulaz/izlaz je nužan: ulaz ima do $2 \cdot 10^6$ brojeva, izlaz do $10^6$.</li>
<li>Hashevi neka su neparni (npr. <code>rng() | 1</code>) da razlika brojnosti $1$ nikad ne da hash $0$.</li>
</ul>
''',
    'verified': r'''Uzorak 1/1, 300 slučajnih malih testova protiv brute forcea, 3 velika testa (najviše 0.71 s).''',
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
        ('Kako se „maksimiziraj minimum” gotovo uvijek napada?',
         r'''<p>Binarnim pretraživanjem po odgovoru. Predikat $P(w)$: „postoji $k$ točaka čiji su svi međusobni nagibi $\ge w$”. Ako vrijedi $P(w)$, vrijedi i $P(w')$ za svako $w' < w$ (isti izbor točaka), pa je $P$ monoton i odgovor je najveći $w$ za koji vrijedi. Preostaje brzo odlučiti $P(w)$ za zadano $w$.</p>'''),
        ('Kako uvjet o nagibu pretvoriti u uvjet o poretku?',
         r'''<p>Za $i < j$ je $x_i < x_j$, pa je $\frac{y_j - y_i}{x_j - x_i} \ge w \iff y_j - y_i \ge w (x_j - x_i) \iff y_i - w x_i \le y_j - w x_j$. Uz $z_i = y_i - w x_i$, skup točaka ima sve nagibe $\ge w$ ako i samo ako je $z$ na njemu (u poretku po $x$) <em>neopadajući</em>. Geometrijski: $z_i$ je odsječak na $y$-osi pravca nagiba $w$ kroz točku $i$, a uvjet kaže da ti pravci idu „prema gore”.</p>'''),
        ('Koji klasični problem sad prepoznajemo?',
         r'''<p>$P(w)$ vrijedi ako i samo ako niz $z_1, \dots, z_n$ ima neopadajući podniz duljine $\ge k$ – najdulji neopadajući podniz (LNDS) u $O(n \log n)$: održavamo niz $\text{kraj}[\ell]$ = najmanja završna vrijednost neopadajućeg podniza duljine $\ell$ i za svaki $z_i$ zamijenimo prvi element <em>strogo veći</em> od $z_i$ (<code>upper_bound</code>, jer su jednake vrijednosti dopuštene) ili ga dodamo na kraj.</p>'''),
        ('Koliko iteracija i kakav uvjet zaustavljanja koristiti u pomičnom zarezu?',
         r'''<p>Nagibi su u $[-10^9, 10^9]$ (razlike koordinata do $10^9$, $\Delta x \ge 1$). Svaka iteracija polovi interval; nakon $\approx 50$ iteracija širina je $2 \cdot 10^9 / 2^{50} \approx 2 \cdot 10^{-6}$, pa $60$–$100$ iteracija sigurno daje traženu točnost $10^{-6}$. Uvjet oblika <code>while (hi - lo &gt; eps)</code> je opasan: kad su $lo$ i $hi$ susjedni reprezentabilni brojevi, $(lo + hi)/2$ se više ne mijenja i petlja može postati beskonačna. Zato fiksan broj iteracija.</p>'''),
        ('Zašto je dovoljno gledati sve parove, a ne samo susjedne odabrane točke?',
         r'''<p>Uvjet zadatka je nad <em>svim</em> parovima, a transformacija u $z$ to točno hvata: neopadajući niz ima $z_i \le z_j$ za svaki par $i < j$. (Ekvivalentno: nagib između dviju nesusjednih odabranih točaka je težinski prosjek nagiba susjednih parova između njih, pa minimum po svim parovima jednak je minimumu po susjednima.) Nema dakle nikakvih skrivenih uvjeta.</p>'''),
    ],
    'tips': [
        r'''„Maksimiziraj minimum” / „minimiziraj maksimum” ⇒ binarno pretraživanje po odgovoru čim je predikat monoton; sav trud ide u brzu provjeru predikata.''',
        r'''Uvjet oblika $\frac{y_j - y_i}{x_j - x_i} \ge w$ uz $x_i < x_j$ pomnoži s nazivnikom i grupiraj po indeksu: dobije se usporedba $y_i - w x_i \le y_j - w x_j$, tj. poredak – to je standardna „rotacija koordinata”.''',
        r'''Za LNDS (jednaki dopušteni) koristi <code>upper_bound</code>, za strogo rastući LIS <code>lower_bound</code>; zamjena jednog s drugim je klasična greška.''',
        r'''Binarno pretraživanje nad realnim brojevima izvodi fiksan broj iteracija (npr. $100$), nikad uvjet $hi - lo < \varepsilon$ – on može zaglaviti zbog zaokruživanja.''',
    ],
    'detailed': r'''
<h3>1. Monotonost i binarno pretraživanje</h3>
<p>Neka je $P(w)$ tvrdnja „postoji izbor $k$ točaka takav da je nagib između svakog para odabranih točaka $\ge w$”. Ako $P(w)$ vrijedi, isti izbor svjedoči i $P(w')$ za svako $w' \le w$, pa je $P$ monotona: vrijedi na $(-\infty, w^\ast]$ i ne vrijedi iznad. Odgovor zadatka je upravo $w^\ast$ – najveći postignuti minimalni nagib (za optimalan izbor, njegov najmanji nagib je $w^\ast$). Binarno pretraživanje na $[-10^9 - 1, 10^9 + 1]$ (nagibi su u $[-10^9, 10^9]$ jer $0 \le x, y \le 10^9$ i $\Delta x \ge 1$) svodi zadatak na brzu provjeru $P(w)$.</p>
<h3>2. Transformacija nagiba u poredak</h3>
<p>Za $i < j$ vrijedi $x_i < x_j$, pa množenje s pozitivnim $x_j - x_i$ ne mijenja smjer nejednakosti: $$\frac{y_j - y_i}{x_j - x_i} \ge w \iff y_j - y_i \ge w x_j - w x_i \iff y_i - w x_i \le y_j - w x_j .$$ Definiramo $z_i = y_i - w x_i$. Skup indeksa $i_1 < i_2 < \dots < i_k$ zadovoljava uvjet za sve parove ako i samo ako $z_{i_1} \le z_{i_2} \le \dots \le z_{i_k}$. Dakle $P(w) \iff$ niz $z$ ima neopadajući podniz duljine $\ge k$.</p>
<p>Geometrijska interpretacija: $z_i$ je odsječak na $y$-osi pravca nagiba $w$ kroz $(x_i, y_i)$; točke gledane „u smjeru nagiba $w$” moraju ići prema gore.</p>
<h3>3. Najdulji neopadajući podniz u $O(n \log n)$</h3>
<p>Održavamo niz $\text{kraj}$ u kojem je $\text{kraj}[\ell - 1]$ najmanja moguća završna vrijednost neopadajućeg podniza duljine $\ell$ među dosad obrađenim elementima; niz je neopadajući. Za novi $z_i$: nađemo prvi element <em>strogo veći</em> od $z_i$ (<code>upper_bound</code>) i zamijenimo ga sa $z_i$; ako takvog nema, $z_i$ dodajemo na kraj (podniz je produljen). Duljina niza $\text{kraj}$ je duljina LNDS-a. Koristimo <code>upper_bound</code>, a ne <code>lower_bound</code>, jer jednake vrijednosti smiju stajati jedna za drugom (nagib točno $w$ je dopušten). Ispravnost je standardna: nakon obrade prefiksa, $\text{kraj}[\ell-1]$ je točno minimum završnih vrijednosti po svim neopadajućim podnizovima duljine $\ell$ u tom prefiksu (indukcija po $i$).</p>
<p>Čim duljina dosegne $k$, možemo prekinuti provjeru s odgovorom „da”.</p>
<h3>4. Točnost i broj iteracija</h3>
<p>Početni interval ima širinu oko $2 \cdot 10^9$; nakon $t$ iteracija širina je $2 \cdot 10^9 / 2^t$. Za $t = 50$ to je $\approx 1.8 \cdot 10^{-6}$, za $t = 60$ oko $1.7 \cdot 10^{-9}$. Koristimo $100$ iteracija u <code>long double</code> – dodatne iteracije ništa ne koštaju ($100 \cdot n \log n \approx 1.7 \cdot 10^8$ jednostavnih operacija, u praksi ispod $0.1$ s), a uvjet zaustavljanja <code>hi - lo &gt; eps</code> namjerno izbjegavamo: kad $lo$ i $hi$ postanu susjedni reprezentabilni brojevi, sredina je jednaka jednom od njih i petlja se ne bi zaustavila.</p>
<p>Zaokruživanje: $z_i = y_i - w x_i$ je po modulu do $\approx |w| \cdot 10^9$, pa je apsolutna pogreška pojedinog $z_i$ oko $\varepsilon |w| \cdot 10^9$ ($\varepsilon$ = strojna preciznost). Usporedba $z_i \le z_j$ može biti kriva samo ako je $|z_j - z_i| = |(\text{nagib}_{ij} - w)| \cdot \Delta x$ manje od te pogreške, tj. kad je $|w - \text{nagib}_{ij}| \lesssim 2 \varepsilon |w| \cdot 10^9 / \Delta x$. Uz <code>long double</code> ($\varepsilon \approx 5 \cdot 10^{-20}$) to je najviše $\approx 10^{-10} |w|$ – daleko unutar dopuštene relativne tolerancije $10^{-6}$; s običnim <code>double</code> ($\varepsilon \approx 10^{-16}$) granica je $\approx 2 \cdot 10^{-7} |w|$, što je već blizu tolerancije. Potpuno egzaktna alternativa bila bi binarno pretraživanje po razlomcima s usporedbama u <code>__int128</code>, ali ovdje nije potrebna.</p>
<h3>5. Algoritam</h3>
<ol>
<li>Pročitaj točke (već sortirane po $x$).</li>
<li>$lo = -10^9 - 1$, $hi = 10^9 + 1$; $100$ puta: $mid = (lo + hi)/2$; ako $P(mid)$, $lo = mid$, inače $hi = mid$.</li>
<li>Ispiši $lo$ s dovoljno decimala (npr. $9$).</li>
</ol>
<h3>6. Složenost</h3>
<p>$\Theta(n \log n)$ po provjeri, $\Theta(n \log n \log X)$ ukupno, gdje je $\log X$ broj iteracija ($\approx 100$). Memorija $O(n)$.</p>
<h3>7. Primjer</h3>
<p>Točke $(1,2), (2,4), (3,3), (4,1)$, $k = 3$. Za $w = -1$: $z = 3, 6, 6, 5$; neopadajući podniz $3, 6, 6$ (točke $1, 2, 3$) ima duljinu $3$, pa $P(-1)$ vrijedi. Za $w = -0.99$: $z = 2.99, 5.98, 5.97, 4.96$; najdulji neopadajući podniz ima duljinu $2$, pa ne vrijedi. Odgovor $-1$ (nagib između točaka $2$ i $3$).</p>
''',
    'verified': r'''Uzorci 2/2, 300 slučajnih malih testova protiv brute forcea (usporedba realnog odgovora s tolerancijom 10^-6), 3 velika testa (najviše 0.06 s).''',
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
        ('Moramo li uopće graditi cijelo razapinjuće stablo?',
         r'''<p>Ne. Ako imamo šumu $F$ čije težine bridova su točno $\{0, 1, \dots, K-1\}$ (svaka jednom), graf je povezan pa se $F$ može dopuniti do razapinjućeg stabla bilo kojim bridovima (Kruskalovo dopunjavanje), a dodavanje bridova skupu težina može MEX samo povećati ili ostaviti. Obratno, stablo s MEX-om $\ge K$ sadrži po jedan brid svake težine $0..K-1$, a oni čine takvu šumu. Dakle: odgovor je najveći $K$ za koji postoji šuma s po jednim bridom svake težine $0, \dots, K-1$.</p>'''),
        ('Koje su dvije strukture „nezavisnosti” u igri?',
         r'''<p>„Skup bridova bez ciklusa” – nezavisni skupovi <em>grafovskog matroida</em>. „Skup bridova s najviše jednim bridom svake težine” – nezavisni skupovi <em>particijskog matroida</em> (klase = težine, kapacitet $1$). Tražimo skup nezavisan u oba, tj. zajednički nezavisan skup – to je problem <em>presjeka matroida</em>, koji je (za razliku od presjeka triju matroida) rješiv u polinomnom vremenu.</p>'''),
        ('Zašto je dovoljno tražiti zajednički nezavisan skup veličine $K+1$ među bridovima težine $\le K$?',
         r'''<p>Među bridovima težine $\le K$ postoji samo $K+1$ težinskih klasa, pa zajednički nezavisan skup veličine $K+1$ mora uzeti točno jedan brid iz svake – to je upravo šuma s težinama $0..K$. Stoga: MEX $\ge K+1 \iff$ najveći zajednički nezavisan skup nad $E_{\le K}$ ima veličinu $K+1$.</p>'''),
        ('Kako od zajedničkog nezavisnog skupa $S$ doći do većeg?',
         r'''<p>Teorem o presjeku matroida: ako $S$ nije najveći, postoji <em>povećavajući put</em> u grafu razmjene. Vrhovi su bridovi; izvori su $x \notin S$ s $S + x$ šumom (spaja dvije komponente), ponori su $x \notin S$ čija je težinska klasa u $S$ slobodna (ovdje: težina $K$). Lukovi $y \to x$ ($y \in S$, $x \notin S$) ako je $S - y + x$ šuma ($y$ leži na putu u šumi između krajeva $x$), i $x \to y$ ako $S - y + x$ poštuje težine ($y$ je jedini brid u $S$ iste težine kao $x$). Simetrična razlika $S$ i <em>najkraćeg</em> takvog puta (BFS) je zajednički nezavisan skup veličine $|S| + 1$.</p>'''),
        ('Zašto možemo ići inkrementalno po $K$ umjesto binarnog pretraživanja?',
         r'''<p>Nakon što nađemo šumu $S_K$ s težinama $0..K-1$, ona je zajednički nezavisan skup i nad $E_{\le K}$; pokušavamo je jednim povećanjem proširiti bridom težine $K$. Ako povećavajući put ne postoji, po teoremu je $S_K$ najveći, pa MEX $K+1$ nije moguć i odgovor je $K$. Ako težine $K$ nema u grafu, također stajemo. Svaki $K$ košta jedno traženje puta: $O(m \cdot n)$ za izgradnju lukova (svaki brid izvan $S$ ima put duljine $\le n-1$ u šumi) plus BFS; ukupno najviše $n$ krugova.</p>'''),
    ],
    'tips': [
        r'''Dva neovisna ograničenja „bez ciklusa” i „najviše $c$ po klasi/boji” (ili „stupanj $\le d$ u bipartitnom grafu”) gotovo su uvijek presjek dvaju matroida – prepoznaj obrazac i posegni za algoritmom povećavajućih putova.''',
        r'''MEX ograničenja često se svode na „prefiks” $\{0..K-1\}$: monotono svojstvo po $K$ omogućuje inkrementalno dodavanje ili binarno pretraživanje.''',
        r'''U presjeku matroida obavezno koristi <em>najkraći</em> povećavajući put (BFS); duži put može pokvariti nezavisnost u jednom od matroida.''',
        r'''Provjeri „je li $S - y + x$ nezavisan” za grafovski matroid jednostavno: ukorijeni šumu i pogledaj leži li $y$ na putu između krajeva $x$.''',
    ],
    'detailed': r'''
<h3>1. Svođenje na šumu s prefiksom težina</h3>
<p><strong>Lema.</strong> Odgovor je najveći $K$ za koji postoji šuma (podskup bridova bez ciklusa) s točno jednim bridom svake težine $0, 1, \dots, K-1$ i nijednim drugim.</p>
<p><em>Dokaz.</em> ($\Rightarrow$) Razapinjuće stablo s MEX-om $\ge K$ sadrži bridove težina $0..K-1$; odaberemo po jedan za svaku težinu – podskup stabla je šuma. ($\Leftarrow$) Šumu $F$ dopunimo do razapinjućeg stabla: prolazimo bridove grafa i dodajemo svaki koji ne zatvara ciklus; kako je graf povezan, na kraju dobivamo stablo (Kruskalov argument). Skup težina samo je narastao, pa je MEX $\ge K$. $\square$</p>
<h3>2. Dva matroida</h3>
<p><em>Matroid</em> na skupu $E$ je familija „nezavisnih” podskupova zatvorena na podskupove i sa svojstvom zamjene: ako su $A, B$ nezavisni i $|A| < |B|$, postoji $b \in B \setminus A$ s $A + b$ nezavisnim.</p>
<ul>
<li><strong>Grafovski matroid $M_1$:</strong> nezavisni su skupovi bridova bez ciklusa (šume). Svojstvo zamjene: šuma $B$ s više bridova ima manje komponenata nego $A$, pa neki brid iz $B$ spaja dvije komponente od $A$.</li>
<li><strong>Particijski matroid $M_2$:</strong> nezavisni su skupovi s najviše jednim bridom svake težine. Svojstvo zamjene: $B$ pokriva više težinskih klasa nego $A$, pa neka klasa iz $B$ u $A$ nije zauzeta.</li>
</ul>
<p>Šuma iz leme je zajednički nezavisan skup veličine $K$ nad $E_{\le K-1}$, gdje je $E_{\le K} = \{e : w_e \le K\}$. Ključ: nad $E_{\le K}$ postoji samo $K+1$ klasa, pa svaki zajednički nezavisan skup veličine $K+1$ uzima točno jednu iz svake – to je šuma s težinama $0..K$. Dakle $$\text{MEX} \ge K+1 \iff \max\{|S| : S \subseteq E_{\le K},\ S \in \mathcal I_1 \cap \mathcal I_2\} = K+1 .$$</p>
<h3>3. Povećavajući put u grafu razmjene</h3>
<p>Za zajednički nezavisan $S$ definiramo usmjereni graf $D_S$ na skupu bridova:</p>
<ul>
<li>$X_1 = \{x \notin S : S + x \in \mathcal I_1\}$ – bridovi čiji su krajevi u različitim komponentama šume $S$ (izvori);</li>
<li>$X_2 = \{x \notin S : S + x \in \mathcal I_2\}$ – bridovi čija težinska klasa u $S$ nije zauzeta (ponori);</li>
<li>luk $y \to x$ za $y \in S$, $x \notin S$ ako $S - y + x \in \mathcal I_1$: krajevi $x$ su u istoj komponenti, a $y$ leži na jedinstvenom putu u šumi između njih;</li>
<li>luk $x \to y$ za $x \notin S$, $y \in S$ ako $S - y + x \in \mathcal I_2$: $y$ je brid iste težine kao $x$ (jedini takav u $S$).</li>
</ul>
<p><strong>Teorem (Edmonds; Lawler).</strong> Ako postoji zajednički nezavisan skup veći od $S$, u $D_S$ postoji put od $X_1$ do $X_2$; za <em>najkraći</em> takav put $P$ (bez prečaca) skup $S \triangle P$ je zajednički nezavisan i ima $|S| + 1$ element. Ako puta nema, $S$ je najveći. Intuicija: put $x_0 \to y_1 \to x_1 \to \dots \to y_t \to x_t$ izbacuje $y_i$ i ubacuje $x_{i-1}$ te $x_t$; svaka zamjena $S - y_i + x_{i-1}$ čuva $M_1$ (luk $y_i \to x_{i-1}$), a $S - y_i + x_i$ čuva $M_2$ (luk $x_i \to y_i$); minimalnost puta sprječava da se zamjene međusobno pokvare (svojstvo „bez prečaca” jamči jedinstveno sparivanje u lemi o zamjeni). Dokaz je standardan u literaturi o matroidima i ovdje ga preskačemo.</p>
<p>U našem grafu je posebno jednostavno: klase $0..K-1$ su zauzete, pa je $X_2$ točno skup bridova težine $K$ izvan $S$; luk $x \to y$ vodi u jedinstveni „predstavnik” težine $w_x$ u $S$.</p>
<h3>4. Inkrementalni algoritam</h3>
<ol>
<li>$S \gets \emptyset$, $K \gets 0$.</li>
<li>Ako nijedan brid nema težinu $K$, stani – odgovor $K$.</li>
<li>Ukorijeni šumu $S$ (roditelj, dubina, komponenta). Za svaki $x \notin S$ težine $\le K$: ako spaja dvije komponente, $x \in X_1$ (udaljenost $0$ u BFS-u); inače za svaki brid $y$ na putu u šumi između krajeva $x$ dodaj luk $y \to x$.</li>
<li>BFS iz $X_1$: iz $x \notin S$ idi u predstavnika njegove težine (ili stani ako je $w_x = K$); iz $y \in S$ idi po lukovima $y \to x$. Ako BFS ne dosegne brid težine $K$, stani – odgovor $K$.</li>
<li>Inače $S \gets S \triangle P$ duž nađenog najkraćeg puta; osvježi predstavnike; $K \gets K + 1$; natrag na 2.</li>
</ol>
<p>Zašto smijemo krenuti od prethodnog $S$? Skup $S_K$ s težinama $0..K-1$ zajednički je nezavisan i nad $E_{\le K}$, a teorem vrijedi za bilo koji zajednički nezavisan početni skup – ne mora biti dobiven „iz nule”. Kako svaka klasa smije dati najviše jedan brid, veličina se u svakom krugu poveća za točno $1$ ili algoritam stane.</p>
<h3>5. Složenost</h3>
<p>Krug $K$: ukorjenjivanje $O(n + m)$, izgradnja lukova $O(m \cdot n)$ u najgorem slučaju (put u šumi duljine do $n - 1$ za svaki od $\le m$ bridova), BFS $O(m + \text{broj lukova})$. Krugova je najviše $\min(n, \text{broj različitih težina}) \le n$. Grubo $O(n^2 m) \approx 10^9$ elementarnih operacija u teoretski najgorem slučaju, ali u praksi znatno manje (putovi su kratki, mnogo bridova ispada zbog težine $> K$); na najvećim testovima rješenje radi u stotinkama sekunde. Editorijal navodi $\Theta(n^{2.5})$ uz pažljiviju izvedbu (npr. binarno pretraživanje po $K$ i brzu implementaciju presjeka), što za $n, m \le 1000$ nije potrebno.</p>
<h3>6. Rubni slučajevi</h3>
<ul>
<li>Nema brida težine $0$ (uključujući $m = 0$, $n = 1$): odgovor $0$.</li>
<li>Petlje $u = v$ (ako se pojave) nikad nisu u šumi – u kodu spadaju pod „krajevi u istoj komponenti”, put je prazan, pa nemaju ulazne lukove i nikad ne ulaze u $S$.</li>
<li>Paralelni bridovi su dopušteni: brid iste težine kao neki u $S$ i s krajevima u istoj komponenti može ipak biti koristan kroz dulji povećavajući put.</li>
<li>Odgovor je najviše $\min(n-1, \text{broj različitih težina})$; kod stane sam kad nestane bridova težine $K$, pa gornja granica nije potrebna.</li>
</ul>
<h3>7. Primjer</h3>
<p>Bridovi $(1,2,0), (2,3,1), (1,3,1), (3,4,2)$. $K = 0$: $S = \{(1,2,0)\}$. $K = 1$: $(2,3,1)$ spaja komponente, težina $1$ – odmah ponor; $S = \{(1,2,0), (2,3,1)\}$. $K = 2$: $(3,4,2)$ spaja komponente; $S$ ima $3$ brida. $K = 3$: nema brida težine $3$ – odgovor $3$.</p>
''',
    'verified': r'''Uzorak 1/1, 300 slučajnih malih testova protiv brute forcea, 3 velika testa (najviše 0.03 s).''',
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
        ('Zašto se par „stranica × upit” ne može provjeriti izravno i što se s time može učiniti?',
         r'''<p>Parova je do $4 \cdot 10^{10}$. Trebamo strukturu koja parove grupira. Poligon je <em>jednostavan</em>: stranice se ne sijeku. Ideja: podijeli-pa-vladaj po $x$-koordinati. U čvoru koji obrađuje pojas $l \le x \le r$ dužina (stranica ili upit) koja siječe obje okomice $x = l$ i $x = r$ zovemo <em>raspinjućom</em>; takva se dužina obradi u tom čvoru i ne ide dublje, ostale idu u djecu $[l, mid]$ i $[mid, r]$. Svaka dužina je neraspinjuća u najviše dva čvora po razini (krajnji čvorovi koje dotiče), pa se pojavljuje u $O(\log V)$ čvorova, $V = 6 \cdot 10^4$ širina koordinata.</p>'''),
        ('Što je posebno kod raspinjućih stranica u pojasu?',
         r'''<p>Unutar pojasa one su međusobno disjunktne dužine koje idu od lijevog do desnog ruba, pa su <em>potpuno uređene po visini</em>: poredak po $y$ na $x = l$ jednak je poretku na svakom $x' \in [l, r]$ (da se poredak promijeni, dvije bi se stranice morale presjeći). Područja između susjednih raspinjućih stranica su konveksna (presjek pojasa i dviju poluravnina). Upitna dužina, odrezana na pojas, siječe neku raspinjuću stranicu ako i samo ako joj krajevi padnu u različita područja ili neki kraj leži točno na stranici – binarno pretraživanje po sortiranim stranicama, $O(\log n)$ po upitu.</p>'''),
        ('Kako izgleda ostatak ruba unutar pojasa i kako ga „vidi” raspinjući upit?',
         r'''<p>Neraspinjuće stranice u pojasu čine <em>izlomljene linije</em> (komade ruba) čiji unutarnji vrhovi imaju $l < x < r$, a oba kraja leže na rubovima pojasa (vrh na rubu ili stranica odrezana na rubu). Raspinjući upit je unutar pojasa cijeli pravac, pa dijeli pojas na „iznad” i „ispod”. Komad ga siječe ako i samo ako ima točku na ili iznad <em>i</em> točku na ili ispod pravca; kako komad na svakom rubu dotiče poznate visine, dovoljno je: (1) ako visina upita na rubu $x = l$ padne između dviju dodirnih visina komada, sijeku se (Jordanov argument); (2) inače komad koji na $x = l$ dotiče <em>iznad</em> upita siječe ga točno ako mu je neki vrh na ili ispod pravca, i simetrično.</p>'''),
        ('Kako za mnogo upita brzo odgovoriti „postoji li vrh na ili ispod pravca” za točan skup komada?',
         r'''<p>Vrh $p$ je na ili ispod pravca $y = t x + c$ ako je $y_p - t x_p \le c$. Za fiksan skup vrhova to je $\min_p (y_p - t x_p) \le c$ – minimum linearnih funkcija u varijabli $t$: <em>Li Chao stablo</em> nad svim nagibima upita u čvoru. Skup komada „iznad upita” raste kad upit ide prema dolje, pa sortiramo komade po dodirnoj visini silazno i upite po visini na rubu silazno te umećemo vrhove offline. Četiri simetrične varijante (lijevi/desni rub, iznad/ispod) dobivamo zrcaljenjem koordinata i istim kodom.</p>'''),
        ('Gdje su rubni slučajevi koje shema lako promaši?',
         r'''<p>Okomite dužine nikad nisu raspinjuće (uvjet $x_1 \le l < r \le x_2$), pa okomitu stranicu i okomiti upit na istom $x$ obradimo posebno (sortirani intervali po $x$). Dodir u jednoj točki s cjelobrojnim $x$ mora dobiti čvor u kojem je jedna dužina raspinjuća: zato početni pojas proširimo na $[x_{\min} - 1, x_{\max} + 1]$ da postoje jedinični pojasi uz sam rub poligona. Ako je cijeli poligon strogo unutar pojasa, komad je <em>zatvoren</em> (bez dodira s rubovima): tada upit siječe ako ima vrhova i iznad i ispod. Sve usporedbe su egzaktne razlomcima s <code>__int128</code>.</p>'''),
    ],
    'tips': [
        r'''Podijeli-pa-vladaj po koordinati s pojmom „raspinjuće” dužine (siječe obje granice pojasa) klasičan je način da se $O(nq)$ geometrijskih parova svede na $O((n+q)\log V)$ pojavljivanja s jednostavnijom lokalnom strukturom.''',
        r'''Disjunktne dužine koje presijecaju cijeli pojas potpuno su uređene po visini – dovoljno ih je sortirati na jednom rubu i binarno pretraživati.''',
        r'''„Postoji li točka skupa na ili ispod pravca $y = tx + c$” = $\min_p (y_p - t x_p) \le c$: minimum linearnih funkcija u $t$ – Li Chao stablo ili konveksna ljuska; offline uz monotono rastući skup.''',
        r'''U cjelobrojnoj geometriji s dijeljenjem koristi razlomke i <code>__int128</code> za usporedbe – tolerancija u pomičnom zarezu je izvor krivih odgovora kod dodira.''',
    ],
    'detailed': r'''
<h3>1. Struktura: podijeli-pa-vladaj po $x$</h3>
<p>Neka je $[x_{\min}, x_{\max}]$ raspon $x$-koordinata poligona. Postavimo korijen na pojas $[L_0, R_0] = [x_{\min} - 1, x_{\max} + 1]$; upiti koji uopće ne dotiču taj raspon odmah dobivaju <code>NO</code>. Funkcija $\mathrm{solve}(l, r, E, Q)$ dobiva skup stranica $E$ i upita $Q$ koji dotiču pojas $l \le x \le r$. Dužina s $x$-rasponom $[x_1, x_2]$ je <em>raspinjuća</em> u pojasu ako $x_1 \le l$ i $x_2 \ge r$. Podijelimo $E = E_s \cup E_n$ i $Q = Q_s \cup Q_n$ (raspinjući / neraspinjući) i u čvoru obradimo:</p>
<ol>
<li>$E_s$ protiv <em>svih</em> upita iz $Q$ (odjeljak 2);</li>
<li>$Q_s$ protiv $E_n$ (odjeljak 3);</li>
<li>ako je $r - l \ge 2$, s $mid = \lfloor (l + r)/2 \rfloor$ pozovemo $\mathrm{solve}(l, mid)$ s dužinama iz $E_n, Q_n$ koje imaju $x_1 \le mid$ i $\mathrm{solve}(mid, r)$ s onima koje imaju $x_2 \ge mid$.</li>
</ol>
<p><strong>Potpunost.</strong> Neka se stranica $e$ i upit $s$ sijeku u točki s apscisom $X$. U svakom čvoru $[l, r]$ s $l \le X \le r$ obje su dužine prisutne (indukcija: neraspinjuća dužina koja sadrži $X \le mid$ ima $x_1 \le mid$, itd.). Ako je u tom čvoru bar jedna raspinjuća, par je provjeren (raspinjuća stranica protiv svih upita; raspinjući upit protiv svih neraspinjućih stranica; oba raspinjuća – prvi slučaj). Inače obje silaze u dijete koje sadrži $X$. Do lista $[l, l+1]$ obje neraspinjuće znači da svaka ima $x_2 \le l$ ili $x_1 \ge l + 1$: cjelobrojno je pa je svaka okomita ili završava u $X \in \{l, l+1\}$. Tada pak u nekom pretku s $mid = X$ obje idu u <em>oba</em> djeteta, a u lancu čvorova $[X, r']$ (odn. $[l', X]$) neokomita dužina koja se od $X$ pruža udesno (ulijevo) u nekom trenutku postane raspinjuća – najkasnije u listu $[X, X+1]$ odn. $[X-1, X]$ – dok je druga dužina ondje prisutna i neraspinjuća, pa se par provjeri – osim ako su obje okomite na istom $x$, što obrađujemo zasebno. Upravo zbog listova $[x_{\min}-1, x_{\min}]$ i $[x_{\max}, x_{\max}+1]$ pojas je proširen za $1$.</p>
<p><strong>Broj pojavljivanja.</strong> Na jednoj razini dužina siječe uzastopan niz pojaseva; sve unutarnje pojaseve raspinje (i ondje staje), pa u sljedeću razinu prolazi u najviše dva čvora. Ukupno $O(\log V)$ čvorova po dužini, $V = R_0 - L_0 \le 6 \cdot 10^4 + 2$.</p>
<h3>2. Raspinjuće stranice protiv upita</h3>
<p><strong>Lema 1.</strong> Raspinjuće stranice u pojasu $[l, r]$ potpuno su uređene po visini: ako je $y_a(l) < y_b(l)$ (ili $y_a(l) = y_b(l)$ i $y_a(r) < y_b(r)$), tada je $y_a(x) \le y_b(x)$ za sve $x \in [l, r]$. <em>Dokaz.</em> Dvije stranice jednostavnog poligona ne sijeku se osim u zajedničkom vrhu; zajednički vrh raspinjućih stranica može biti samo na $x = l$ ili $x = r$, jer raspinjuća stranica nema vrhova strogo unutar pojasa. Dvije dužine nad istim intervalom $[l, r]$ koje se ne sijeku u unutrašnjosti čuvaju poredak po visini po teoremu o međuvrijednosti. $\square$</p>
<p>Sortiramo $E_s$ po $(y(l), y(r))$ egzaktno. Za upit $s$ odrežemo ga na pojas: $X_1 = \max(x_1, l)$, $X_2 = \min(x_2, r)$ i pripadne visine $y_s(X_1), y_s(X_2)$ (za okomit upit $X_1 = X_2 = x$, visine su donji i gornji kraj). Binarnim pretraživanjem nađemo za svaki od dva kraja broj raspinjućih stranica <em>strogo ispod</em> njega i zabilježimo dodir (jednakost). <strong>Lema 2.</strong> Odrezani upit siječe neku raspinjuću stranicu ako i samo ako se ti brojevi razlikuju ili postoji dodir. <em>Dokaz.</em> Područje između susjednih raspinjućih stranica (ili iznad najviše / ispod najniže) je $\{(x, y) : l \le x \le r,\ f(x) < y < g(x)\}$ s linearnim $f, g$ – konveksno, pa dužina s oba kraja u istom području ostaje u njemu i ne dira stranice. Ako su krajevi u različitim područjima, po neprekidnosti dužina prelazi stranicu između njih. $\square$</p>
<h3>3. Raspinjući upiti protiv ostatka ruba</h3>
<p><strong>Komadi.</strong> Neraspinjuće stranice iz $E_n$ spajamo u maksimalne lance po poretku poligona: iz stranice $e$ prelazimo na sljedeću stranicu ako je i ona u $E_n$ i ako je zajednički vrh <em>strogo</em> unutar pojasa ($l < x < r$). Krajeve lanca koji su izvan pojasa odrežemo na okomicu $x = l$ odn. $x = r$ (egzaktno računamo $y$ na rubu). Rezultat su izlomljene linije – <em>komadi</em> – s oba kraja na rubovima pojasa i svim ostalim vrhovima strogo unutra. Komadi su međusobno disjunktni (dijelovi ruba jednostavnog poligona), osim mogućih zajedničkih krajeva na rubovima. Ako nijedan lanac nema početak (sve stranice u $E_n$ i svi vrhovi strogo unutra), cijeli je poligon <em>zatvoren komad</em> unutar pojasa.</p>
<p>Raspinjući upit $s$ u pojasu je cijeli odsječak pravca $\ell$ od $x = l$ do $x = r$, pa: <em>komad siječe $s$ ako i samo ako ima točku na ili iznad $\ell$ i točku na ili ispod $\ell$</em> (povezanost + neprekidnost; točke na ekstremu udaljenosti od pravca su vrhovi jer su stranice linearne).</p>
<p><strong>Korak 1 – pokrivenost.</strong> Neka komad $C$ dotiče rub $x = l$ na visinama iz $[lo, hi]$ (oba kraja na $x = l$: $lo$ i $hi$ su njihove visine; jedan kraj: $lo = hi$). Ako $y_s(l) \in [lo, hi]$, sijeku se. <em>Dokaz.</em> Za $lo = hi$ ili jednakost je to dodir kraja komada. Inače $C$ zajedno s okomitim odsječkom od $(l, lo)$ do $(l, hi)$ čini zatvorenu krivulju koja cijela leži u $x < r$; točka $(l, y_s(l))$ je na njoj, a odmah desno je unutrašnjost krivulje (lijevo od $x = l$ je vanjština). Odsječak upita završava u $(r, y_s(r))$ izvan krivulje, pa je mora presjeći, a okomiti odsječak ne može (ima $x > l$) – siječe $C$. $\square$ Implementacija: sortiramo intervale po $lo$, upite po $y_s(l)$, i jednim prolazom održavamo najveći $hi$ među intervalima s $lo \le y_s(l)$.</p>
<p><strong>Korak 2 – komadi iznad upita.</strong> Komad s $lo > y_s(l)$ počinje iznad $\ell$; siječe $\ell$ točno ako ima vrh $p$ na ili ispod $\ell$. Za $\ell : y = t x + c$ to je $y_p - t x_p \le c$, tj. $\min_{p} g_p(t) \le c$, gdje je $g_p(t) = y_p - x_p t$ linearna funkcija u $t$. Skup komada s $lo > y_s(l)$ raste kad $y_s(l)$ pada, pa upite obrađujemo po $y_s(l)$ silazno, umećući vrhove komada čim njihov $lo$ prijeđe visinu upita, i pitamo $\min$ pri $t = t_s$. To je <em>Li Chao stablo</em> nad sortiranim (diskretiziranim) nagibima svih upita u čvoru: umetanje linearne funkcije $O(\log Q)$, upit minimuma u točki $O(\log Q)$.</p>
<p><strong>Ostale tri varijante.</strong> „Komadi ispod upita” dobivamo zrcaljenjem $y \to -y$ (minimum postaje maksimum, ali nakon zrcaljenja opet tražimo minimum); komadi koji dotiču <em>desni</em> rub $x = r$ dobivamo zrcaljenjem $x \to -x$ (rub $x = r$ postaje $x = -r$ „lijevi”). Isti kod pozovemo četiri puta s parametrima zrcaljenja. Svaki komad dotiče bar jedan rub pa je pokriven; komad koji dotiče oba ruba provjeri se dvaput, što je neškodljivo.</p>
<p><strong>Zatvoren komad.</strong> Ako je poligon cijeli unutar pojasa (bez dodira s rubovima), upit ga siječe ako postoji vrh na ili ispod <em>i</em> vrh na ili iznad $\ell$: dva Li Chao stabla (minimum i maksimum, parametar <code>znak</code>).</p>
<h3>4. Okomite dužine</h3>
<p>Okomita dužina ($x_1 = x_2$) nikad nije raspinjuća jer je $l < r$. Okomita stranica protiv neokomitog upita i okomit upit protiv neokomite stranice pokriveni su odjeljcima 2 i 3 (okomita stranica je komad s oba kraja na istom rubu, okomit upit se u odjeljku 2 obrađuje krajevima $(x, y_{\min})$ i $(x, y_{\max})$). Ostaje okomita stranica protiv okomitog upita na istom $x$: za svaki $x$ držimo sortirane (disjunktne) $y$-intervale okomitih stranica i binarnim pretraživanjem provjerimo preklapa li se interval upita s nekim od njih.</p>
<h3>5. Egzaktna aritmetika</h3>
<p>Visina dužine na okomici $x = X$ je razlomak $\frac{y_1 (x_2 - x_1) + (y_2 - y_1)(X - x_1)}{x_2 - x_1}$ s brojnikom do $\approx 5.4 \cdot 10^9$ i nazivnikom do $6 \cdot 10^4$. Usporedbe razlomaka množenjem križno ulaze u $\approx 3 \cdot 10^{14}$ (stane u 64 bita), ali usporedba dviju linearnih funkcija $g_p(t)$ u Li Chao stablu množi tri razlomka: brojnik do $\approx 5.4 \cdot 10^9 \cdot 6 \cdot 10^4 \cdot 6 \cdot 10^4 \approx 2 \cdot 10^{19}$ – iznad $2^{63}$, pa koristimo <code>__int128</code>. Nema pomičnog zareza, pa su dodiri (jednakosti) točni – što je nužno jer se dodir računa kao presjek.</p>
<h3>6. Složenost</h3>
<p>Svaka stranica i upit pojavljuje se u $O(\log V)$ čvorova. U čvoru s $a$ stranica i $b$ upita: sortiranje $O((a + b) \log(a + b))$, binarna pretraživanja $O(b \log a)$, komadi $O(a)$, Li Chao $O((a + b) \log b)$. Ukupno $O\bigl((n + q) \log V \log (n + q)\bigr)$ uz egzaktnu aritmetiku u 128 bita; za $n = q = 2 \cdot 10^5$ rješenje radi oko $1.4$ s (limit $4$ s). Memorija $O((n + q) \log V)$ u najgorem slučaju za liste po čvorovima, ali se liste oslobađaju pri povratku iz rekurzije.</p>
<h3>7. Usporedba s editorijalom</h3>
<p>Editorijal umjesto Li Chao stabla za korak 2 gradi konveksne ljuske komada (inkrementalno, sweep po visini dodira) i testira presjek pravca s ljuskom binarnim pretraživanjem – ista podjela na četiri klase i ista složenost. Ovdje je izabran Li Chao jer je pitanje „postoji li vrh ispod pravca” izravno minimum linearnih funkcija i ne zahtijeva spajanje ljusaka.</p>
<h3>8. Zamke</h3>
<ul>
<li>Upit koji je već označen kao <code>YES</code> preskačemo u svim kasnijim čvorovima (i ne šaljemo ga u djecu) – važno za brzinu.</li>
<li>Normaliziraj sve dužine na $x_1 \le x_2$; za razlomke drži pozitivan nazivnik.</li>
<li>Zrcaljenje $x \to -x$ zamjenjuje krajeve dužine – ne zaboravi zamijeniti i $y$.</li>
<li>U jedinstvenom pojasu $[l, l+1]$ nema rekurzije; upravo se tu razrješuju dodiri u cjelobrojnim točkama.</li>
</ul>
''',
    'verified': r'''Uzorak 1/1 (svih 6 upita), 300 slučajnih malih testova protiv brute forcea (egzaktna geometrija u Pythonu), 3 velika testa (najviše 1.40 s); dodatno prošlo i ~3000 daljnjih slučajnih sjemena.''',
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
        ('Kako izgleda najkraća zatvorena šetnja kroz zadani skup vrhova stabla?',
         r'''<p>Šetnja mora posjetiti sve vrhove skupa $S$, pa prolazi kroz svaki brid minimalnog povezanog podstabla koje ih sadrži (Steinerovo stablo $T_S$); zatvorena je, pa svaki takav brid prelazi barem dvaput (ulazak i povratak). Obilazak $T_S$ u dubinu prelazi svaki brid točno dvaput, dakle odgovor je $2 \cdot w(T_S)$. Zadatak je: brzo računati težinu Steinerova stabla skupa „otvoreni vrhovi s indeksima u $[l, r]$” uz promjene statusa.</p>'''),
        ('Kako težinu Steinerova stabla izraziti preko nečega što se lako agregira?',
         r'''<p>Ukorijenimo stablo u $1$. Unija putova od svih $s \in S$ do korijena sadrži $T_S$ i još put od $\operatorname{LCA}(S)$ do korijena, pa $$w(T_S) = w\Bigl(\bigcup_{s \in S} \text{put}(s, 1)\Bigr) - \operatorname{dub}(\operatorname{LCA}(S)),$$ gdje je $\operatorname{dub}$ težinska dubina. $\operatorname{LCA}(S)$ je $\operatorname{LCA}$ vrha s najmanjim i vrha s najvećim DFS-ulaznim vremenom u $S$ – dovoljno je pamtiti min i max ulaznog vremena, što se agregira trivijalno.</p>'''),
        ('Kako iskoristiti to što stablo ima najviše $50$ listova?',
         r'''<p>Rastavimo stablo na lance: obilazimo vrhove u preorderu i iz svakog još nedodijeljenog vrha spuštamo lanac do lista kroz nedodijeljenu djecu. Svaki lanac završava u drugom listu, pa je lanaca $k \le 50$. Unija putova do korijena presječena s lancem $c$ je uvijek <em>prefiks lanca</em> od njegova vrha do najdublje „potrebne” točke: najdubljeg $s \in S$ na lancu ili točke vješanja nekog nižeg lanca koji sadrži potrebne točke. Dakle za lanac trebamo samo <em>najdublji</em> otvoreni vrh u $[l, r]$ – jedan broj po lancu, agregacija je $\max$.</p>'''),
        ('Koja struktura odgovara na „max po lancu nad indeksima $[l, r]$” uz promjene?',
         r'''<p>Segmentno stablo po indeksima $1..n$ u čijem svakom čvoru stoji $k$ brojeva (najdublja pozicija otvorenog vrha svakog lanca u rasponu) plus min i max ulaznog vremena. Spajanje čvorova je $O(k)$, pa su ažuriranje i upit $O(k \log n)$. Iz $k$ dobivenih dubina rekonstruiramo uniju putova obrađujući lance od najdublje postavljenih vrhova prema gore: lanac $c$ s potrebnom dubinom $D$ doprinosi $D - \operatorname{dub}(\text{par}(\text{vrh}_c))$ i „potrebu” $\operatorname{dub}(\text{par}(\text{vrh}_c))$ prenosi lancu roditelja.</p>'''),
        ('Zašto redoslijed obrade lanaca mora biti po dubini vrha lanca i koje su zamke?',
         r'''<p>Potreba se prenosi s lanca na lanac njegova roditelja, čiji je vrh strogo plići; obrada silazno po dubini vrha jamči da lanac primi sve prenesene potrebe prije nego što ga obradimo. Zamke: težine do $10^9$ i $n$ do $2 \cdot 10^5$ daju dubine do $2 \cdot 10^{14}$ – <code>long long</code>; LCA binarnim skakanjem traži <em>razinu</em> (broj bridova), ne težinsku dubinu; prazan skup $\Rightarrow -1$; jedan vrh $\Rightarrow 0$; memorija segmentnog stabla $2 \cdot 2^{18} \cdot 50$ cijelih brojeva ($\approx 105$ MB) – jedno ravno polje, ne vektor vektora.</p>'''),
    ],
    'tips': [
        r'''Zatvorena šetnja kroz skup vrhova stabla = $2 \times$ težina Steinerova stabla; Steinerovo stablo = unija putova do korijena minus put od LCA-a skupa do korijena.''',
        r'''LCA skupa vrhova jednak je LCA-u vrhova s najmanjim i najvećim DFS-ulaznim vremenom – zato se LCA skupa agregira (min, max) u segmentnom stablu.''',
        r'''Ograničenje „najviše $k$ listova” gotovo uvijek znači „rastavi stablo na $\le k$ lanaca i za svaki lanac pamti jedan sažetak”; cijena je faktor $k$ po operaciji.''',
        r'''Kad čvor segmentnog stabla nosi $k$ brojeva, pohrani ih u jedno ravno polje <code>[čvor * k + c]</code> – bolja lokalnost i bez $2^{18}$ zasebnih alokacija.''',
    ],
    'detailed': r'''
<h3>1. Od šetnje do Steinerova stabla</h3>
<p>Za neprazan skup vrhova $S$ neka je $T_S$ minimalno povezano podstablo koje sadrži $S$ (Steinerovo stablo; u stablu je jedinstveno – unija putova između svih parova iz $S$). <strong>Tvrdnja:</strong> najkraća zatvorena šetnja koja posjećuje sve vrhove iz $S$ ima duljinu $2 \, w(T_S)$. <em>Dokaz.</em> Uklanjanjem brida $e \in T_S$ stablo se raspada na dva dijela, svaki sadrži vrh iz $S$ (inače $e$ ne bi bio u minimalnom podstablu). Zatvorena šetnja koja posjećuje oba dijela prelazi $e$ paran broj puta, dakle bar dvaput: donja granica $2 w(T_S)$. Obilazak $T_S$ u dubinu (Eulerova tura) prelazi svaki brid točno dvaput i vraća se na početak: gornja granica. $\square$ Za $S = \emptyset$ odgovor je $-1$, za $|S| = 1$ je $0$.</p>
<h3>2. Rastav težine Steinerova stabla</h3>
<p>Ukorijenimo stablo u vrhu $1$; $\operatorname{dub}(v)$ = težinska udaljenost od korijena, $\operatorname{niv}(v)$ = broj bridova do korijena. Neka je $U_S = \bigcup_{s \in S} \text{put}(s, 1)$. $U_S$ je povezano podstablo koje sadrži $S$ i korijen; ono je točno $T_S \cup \text{put}(\operatorname{LCA}(S), 1)$, a ta dva dijela dijele samo vrh $\operatorname{LCA}(S)$ (sve od $S$ visi ispod LCA-a, a put do korijena ide iznad). Stoga $$w(T_S) = w(U_S) - \operatorname{dub}(\operatorname{LCA}(S)).$$</p>
<p><strong>LCA skupa.</strong> Neka su $a, b \in S$ vrhovi s najmanjim odn. najvećim ulaznim vremenom $\operatorname{tin}$ u DFS-u, $L = \operatorname{LCA}(a, b)$. Podstablo svakog vrha je u preorderu neprekinut interval; interval od $L$ sadrži $\operatorname{tin}(a)$ i $\operatorname{tin}(b)$, dakle i $\operatorname{tin}(s)$ za svaki $s \in S$ – $L$ je zajednički predak svih. Dublji zajednički predak ne postoji jer je $L$ već najdublji zajednički predak od $a$ i $b$. Dakle $\operatorname{LCA}(S) = \operatorname{LCA}(a, b)$; LCA para računamo binarnim skakanjem po razinama u $O(\log n)$.</p>
<h3>3. Lanci</h3>
<p>Rastav: prolazimo vrhove u preorderu; ako vrh $v$ još nema lanac, otvorimo novi lanac s vrhom (glavom) $v$ i spuštamo se kroz bilo koje nedodijeljeno dijete dok ne dođemo do lista. Djeca su u preorderu iza roditelja, pa kad lanac krene iz $v$ nijedno dijete nije zauzeto – lanac uvijek završi u listu, a različiti lanci u različitim listovima. Broj lanaca je $k \le 50$. Svaki vrh ima lanac $\operatorname{lanac}(v)$ i poziciju $\operatorname{poz}(v)$ (dubina unutar lanca); glava lanca $c$ (osim korijenskog) ima roditelja $p_c$ na nekom plićem lancu.</p>
<p><strong>Lema.</strong> $U_S \cap c$ je za svaki lanac $c$ ili prazan ili prefiks lanca od glave do neke točke $t_c$. <em>Dokaz.</em> Ako $v \in U_S \cap c$, cijeli put od $v$ do korijena je u $U_S$, a njegov početak do glave lanca leži na $c$. $\square$ Najdublja točka $t_c$ je najdublji od: najdubljeg $s \in S$ na $c$ i točaka $p_{c'}$ za lance $c'$ koji vise s $c$ i imaju $U_S \cap c' \ne \emptyset$.</p>
<p>Zato $$w(U_S) = \sum_{c :\, t_c \text{ postoji}} \bigl(\operatorname{dub}(t_c) - \operatorname{dub}(p_c)\bigr),$$ gdje za korijenski lanac uzimamo $\operatorname{dub}(p_c) = 0$; član uključuje brid $p_c \to \text{glava}_c$. Računamo ga obradom lanaca silazno po $\operatorname{dub}(\text{glava}_c)$: kad obradimo $c$ s potrebnom dubinom $D_c$, dodamo $D_c - \operatorname{dub}(p_c)$ i postavimo $D_{\operatorname{lanac}(p_c)} \gets \max(D_{\operatorname{lanac}(p_c)}, \operatorname{dub}(p_c))$. Glava lanca roditelja je predak od $p_c$, dakle strogo plića od glave $c$, pa je taj lanac još neobrađen – redoslijed je ispravan.</p>
<h3>4. Segmentno stablo po indeksima</h3>
<p>Skup $S$ upita je „otvoreni vrhovi s indeksima u $[l, r]$”. Trebamo, za svaki lanac, <em>najveću poziciju</em> otvorenog vrha tog lanca s indeksom u $[l, r]$ te min/max $\operatorname{tin}$. Sve su to operacije $\max$/$\min$ – asocijativne i komutativne – pa ih čuva segmentno stablo po indeksima: čvor za raspon indeksa pamti $k$ maksimuma (ravno polje veličine $2 \cdot \text{sz} \cdot k$) te $\operatorname{tin}_{\min}$, $\operatorname{tin}_{\max}$. List indeksa $i$: ako je $i$ otvoren, $\operatorname{mx}[\operatorname{lanac}(i)] = \operatorname{poz}(i)$, $\operatorname{tin}_{\min} = \operatorname{tin}_{\max} = \operatorname{tin}(i)$; inače sve $-1$ / $\infty$.</p>
<ul>
<li><strong>Promjena statusa</strong> vrha $x$: prepiši list, ponovno spoji $\log n$ predaka: $O(k \log n)$.</li>
<li><strong>Upit</strong> $[l, r]$: iterativno spoji $O(\log n)$ čvorova u akumulator od $k$ maksimuma i par (min, max) tin-a: $O(k \log n)$. Ako je $\operatorname{tin}_{\max} = -1$, skup je prazan – ispiši $-1$. Inače $D_c = \operatorname{dub}(\text{vrh lanca } c \text{ na poziciji } \operatorname{mx}[c])$ za lance s $\operatorname{mx}[c] \ge 0$, izračunaj $w(U_S)$ po odjeljku 3, oduzmi $\operatorname{dub}(\operatorname{LCA}(a, b))$ i ispiši dvostruko.</li>
</ul>
<h3>5. Složenost</h3>
<p>Predobrada: DFS $O(n)$, lanci $O(n)$, tablica skakanja $O(n \log n)$, izgradnja segmentnog stabla $O(\text{sz} \cdot k)$. Operacija: $O(k \log n)$; rekonstrukcija $O(k)$; LCA $O(\log n)$. Ukupno $O(n \log n + nk + q k \log n)$; za $n = q = 2 \cdot 10^5$, $k = 50$ oko $2 \cdot 10^8$ jednostavnih operacija na kompaktnim poljima – oko pola sekunde. Memorija: $2 \cdot 2^{18} \cdot 50$ 32-bitnih brojeva $\approx 105$ MB plus $O(n \log n)$ za skakanje.</p>
<h3>6. Rubni slučajevi i zamke</h3>
<ul>
<li>Dubine su do $2 \cdot 10^5 \cdot 10^9 = 2 \cdot 10^{14}$: <code>long long</code>; odgovor je do $4 \cdot 10^{14}$.</li>
<li>LCA binarnim skakanjem uspoređuje <em>razine</em> (broj bridova), ne težinske dubine – miješanje ta dva pojma daje pogrešan LCA.</li>
<li>Korijen $1$ smije biti list (stupanj $1$); on je glava korijenskog lanca i njegov član u zbroju je $D_c - 0$.</li>
<li>Rekurzivni DFS na $2 \cdot 10^5$ vrhova može prekoračiti stog na nekim sustavima – iterativni DFS.</li>
<li>Svi vrhovi zatvoreni ili nijedan otvoren u $[l, r]$: $-1$; jedan otvoren: $0$ (formula daje $\operatorname{dub}(v) - \operatorname{dub}(v)$).</li>
</ul>
''',
    'verified': r'''Uzorak 1/1, 300 slučajnih malih testova protiv brute forcea, 3 velika testa (najviše 0.45 s).''',
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
        ('Što ograničenja na broj upita s $k = 2$ i $k = 3$ sugeriraju?',
         r'''<p>$66000$ upita s $k = 1$, $660$ s $k = 2$, $6$ s $k = 3$ – omjer je faktor $\approx 100$ po dodatnom izbačenom elementu. To je jasan signal da se očekuje rješenje složenosti $O(C^k)$ po upitu za neko $C \approx 60$–$100$: za svaki izbačeni element imamo $C$ kandidata i rekurzivno grananje.</p>'''),
        ('Zašto kandidata za položaj izbačenog elementa ima samo $O(\log V)$?',
         r'''<p>Prefiksni gcd $g(l, x) = \gcd(a_l, \dots, a_x)$ je nerastuć u $x$ i svaka promjena ga <em>dijeli</em>, dakle bar upola smanjuje: različitih vrijednosti ima najviše $\lfloor \log_2 10^{18} \rfloor + 1 \approx 61$. Pozicije $x$ na kojima se $g(l, x)$ mijenja („točke promjene”) za svaki $l$ možemo unaprijed izračunati zdesna nalijevo: $g(l, t) = \gcd(a_l, g(l+1, t))$, pa se lista za $l$ dobiva iz liste za $l+1$ u $O(\log V)$.</p>'''),
        ('Zašto je unutar bloka konstantnog prefiksnog gcd-a najbolje izbaciti najdešnji element?',
         r'''<p>Neka su $x < x'$ u istom bloku: $g(l, x-1) = g(l, x'-1) = v$. Za bilo koje rješenje s najljevijim izbačenim $x$ koje zadržava skup $K$, konstruiramo rješenje s najljevijim $x'$ koje zadržava $K'' = [l, x'-1] \cup (K \cap [x'+1, r])$ dopunjeno izbacivanjima u $[x'+1, r]$ do točno $k$. Vrijedi $\gcd(K'') = \gcd(v, K \cap [x'+1, r]) \ge \gcd(K)$, jer je $K \supseteq [l, x-1] \cup (K \cap [x'+1, r])$, a gcd podskupa je višekratnik gcd-a nadskupa. Uvjet: $x' \le r - k + 1$ da ostane dovoljno mjesta za preostala izbacivanja.</p>'''),
        ('Zašto se prefiksni gcd mora prenositi u rekurziju, a ne samo „uzeti maksimum”?',
         r'''<p>Nakon fiksiranja najljevijeg izbačenog $x$ preostaje izbaciti $k-1$ elemenata iz $[x+1, r]$, a konačan odgovor je $\gcd(v, \text{gcd zadržanih iz } [x+1, r])$. Funkcija $\gcd(v, \cdot)$ <em>nije</em> monotona: veći gcd ostatka ne znači veći $\gcd(v, \cdot)$ (npr. $v = 4$: ostatak $6$ daje $2$, ostatak $4$ daje $4$). Zato rekurzija prima nakupljeni gcd $\text{cur}$ i maksimizira $\gcd(\text{cur}, \cdot)$ na dnu, u bazi $k = 0$, gdje je odgovor $\gcd(\text{cur}, g(l, r))$ iz sparse tablice.</p>'''),
        ('Kolika je ukupna složenost i što s brzinom gcd-a nad 64-bitnim brojevima?',
         r'''<p>Po upitu $O((\log V)^k)$ listova rekurzije, svaki s $O(1)$ upita na sparse tablicu ($O(1)$ gcd-ova). Ukupno $\approx 66000 \cdot 61 + 660 \cdot 61^2 + 6 \cdot 61^3 \approx 8 \cdot 10^6$ gcd-ova plus $n \log n$ za tablicu. Svaki gcd nad $10^{18}$ ima do $\approx 90$ koraka Euklida s dijeljenjem; binarni gcd (<code>__builtin_ctzll</code>, oduzimanje) višestruko je brži i vrijedi ga upotrijebiti. Vrijednosti do $10^{18}$ stanu u <code>unsigned long long</code>.</p>'''),
    ],
    'tips': [
        r'''Prefiksni gcd (kao i prefiksni AND/OR) mijenja se najviše $O(\log V)$ puta – „za svaki $l$ pamti točke promjene” standardna je predobrada u $O(n \log V)$.''',
        r'''Neobične kvote upita ($66000 / 660 / 6$) su poruka autora: složenost po upitu smije rasti eksponencijalno u $k$ s bazom oko $60$–$100$.''',
        r'''Kad kombiniraš djelomične rezultate funkcijom koja nije monotona (gcd, xor…), ne uzimaj maksimum podproblema – prenesi kontekst u rekurziju i uspoređuj tek konačne vrijednosti.''',
        r'''Za mnogo gcd-ova 64-bitnih brojeva koristi binarni gcd s <code>ctz</code>; sparse tablica za gcd radi jer je gcd idempotentan ($\gcd(x, x) = x$) pa se preklapajući blokovi smiju kombinirati.''',
    ],
    'detailed': r'''
<h3>1. Oznake i predobrada</h3>
<p>$g(l, r) = \gcd(a_l, \dots, a_r)$, $g(l, r) = 0$ za $l > r$ (neutral za gcd). <strong>Sparse tablica</strong> $\text{sp}[j][i] = g(i, i + 2^j - 1)$ daje $g(l, r)$ u $O(1)$: gcd dvaju preklapajućih blokova duljine $2^{\lfloor \log_2 (r-l+1) \rfloor}$ (idempotentnost). Izgradnja $O(n \log n)$ gcd-ova.</p>
<p><strong>Točke promjene.</strong> Za fiksan $l$, $g(l, x)$ je nerastuć u $x$ i svaka promjena je pravi djelitelj prethodne vrijednosti, pa vrijednost padne bar dvostruko: najviše $\lfloor \log_2 10^{18} \rfloor + 1 = 60$ različitih vrijednosti (sve su $\ge 1$). Lista $\text{chg}[l] = [(t_0 = l, v_0), (t_1, v_1), \dots]$ sadrži pozicije $t_i$ na kojima $g(l, \cdot)$ poprimi novu vrijednost $v_i$; $g(l, x) = v_i$ za $x \in [t_i, t_{i+1} - 1]$. Računamo zdesna nalijevo: $g(l, t) = \gcd(a_l, g(l+1, t))$, pa listu za $l$ dobijemo tako da prođemo listu za $l+1$, primijenimo $\gcd(a_l, \cdot)$ i zadržimo samo mjesta gdje se vrijednost stvarno promijeni. Ukupno $O(n \log V)$ gcd-ova i memorije.</p>
<h3>2. Struktura optimalnog rješenja</h3>
<p>Neka je $x$ najljeviji izbačeni indeks. Zadržani su svi iz $[l, x-1]$ (gcd $= g(l, x-1)$) i $r - x - (k-1)$ elemenata iz $[x+1, r]$ ($k-1$ izbačenih). Odgovor je $\max_x \gcd\bigl(g(l, x-1),\ \text{najbolji ostatak}\bigr)$, ali „najbolji ostatak” ovisi o $g(l, x-1)$ jer gcd nije monoton – zato definiramo rekurzivno $$F(l, r, k, \text{cur}) = \max_{K \subseteq [l, r],\ |K| = r-l+1-k} \gcd(\text{cur}, \gcd K),$$ s bazom $F(l, r, 0, \text{cur}) = \gcd(\text{cur}, g(l, r))$ i odgovorom $F(l, r, k, 0)$.</p>
<p><strong>Lema (najdešnji u bloku).</strong> Neka $x < x'$ leže u istom bloku, tj. $g(l, x-1) = g(l, x'-1) = v$, i $x' \le r - k + 1$. Tada za svaki dopušteni skup $K$ s najljevijim izbačenim $x$ postoji dopušteni $K''$ s najljevijim izbačenim $x'$ i $\gcd(\text{cur}, K'') \ge \gcd(\text{cur}, K)$. <em>Dokaz.</em> Krenimo od $K'' := [l, x'-1] \cup (K \cap [x'+1, r])$. Skup $K$ u $[x'+1, r]$ ima izbačeno najviše $k-1$ elemenata; iz $K'' \cap [x'+1, r]$ izbacimo još elemenata tako da ih u $[x'+1, r]$ bude izbačeno točno $k-1$ – moguće jer $r - x' \ge k - 1$. Sada je iz $[l, r]$ izbačeno točno $k$ ($x'$ i $k-1$ desno), najljeviji izbačeni je $x'$, i vrijedi $K'' \cap [x'+1, r] \subseteq K \cap [x'+1, r]$. Neka je $K_0 = [l, x-1] \cup (K'' \cap [x'+1, r]) \subseteq K$. Gcd nadskupa dijeli gcd podskupa, pa $\gcd(K_0) \ge \gcd(K)$. S druge strane $\gcd(K'') = \gcd\bigl(v, K'' \cap [x'+1, r]\bigr) = \gcd\bigl(g(l, x-1), K'' \cap [x'+1, r]\bigr) = \gcd(K_0)$. Dakle $\gcd(K'') \ge \gcd(K)$; isti argument s $\text{cur}$ dodanim u sve skupove daje $\gcd(\text{cur}, K'') \ge \gcd(\text{cur}, K)$. $\square$</p>
<p>Posljedica: dovoljno je probati $x = l$ (prazan prefiks) i za svaki blok $[t_i, t_{i+1} - 1]$ prefiksnog gcd-a kandidata $x = \min(t_{i+1}, r - k + 1)$ (najdešnji $x$ s $x - 1$ u bloku, uz gornju granicu), ako je $x - 1 \ge t_i$. To je $O(\log V)$ kandidata.</p>
<h3>3. Rekurzija</h3>
<p>$F(l, r, k, \text{cur})$:</p>
<ol>
<li>Ako je $k = 0$, vrati $\gcd(\text{cur}, g(l, r))$.</li>
<li>$\text{best} \gets F(l+1, r, k-1, \text{cur})$ (slučaj $x = l$, prazan prefiks).</li>
<li>Za svaki blok $(t_i, v_i)$ iz $\text{chg}[l]$ s $t_i \le r$: $x \gets \min(t_{i+1}, r - k + 1)$ (za zadnji blok $x \gets r - k + 1$); ako je $x - 1 \ge t_i$, $\text{best} \gets \max\bigl(\text{best},\ F(x+1, r, k-1, \gcd(\text{cur}, v_i))\bigr)$.</li>
<li>Vrati $\text{best}$.</li>
</ol>
<p>Baza $k = 0$ koristi sparse tablicu; ako je $l > r$, $g = 0$ i rezultat je $\text{cur}$ (svi elementi desno izbačeni, zadržan je samo prefiks). Podpoziv smije imati $k = r - l + 1$ (izbaci sve preostale) jer je tada $\text{cur} \ne 0$, tj. nešto je već zadržano; na najvišoj razini uvjet $k \le r - l$ jamči neprazan zadržani skup.</p>
<h3>4. Složenost</h3>
<p>Broj listova rekurzije po upitu je $\le (\log V + 1)^k \approx 61^k$: $k=1$: $61$; $k=2$: $\approx 3700$; $k=3$: $\approx 2.3 \cdot 10^5$. Uz kvote upita: $66000 \cdot 61 + 660 \cdot 3721 + 6 \cdot 226981 \approx 4.0 \cdot 10^6 + 2.5 \cdot 10^6 + 1.4 \cdot 10^6 \approx 8 \cdot 10^6$ gcd-ova, plus $\approx 1.7 \cdot 10^6$ za sparse tablicu i $\approx 6 \cdot 10^6$ za točke promjene. S binarnim gcd-om to je desetinke sekunde (limit $1$ s). Memorija $O(n \log n + n \log V)$ 64-bitnih brojeva $\approx 20$ MB.</p>
<h3>5. Zamke</h3>
<ul>
<li>$a_i \le 10^{18} < 2^{63}$, ali koristi <code>unsigned long long</code> (i <code>%llu</code>) – bez predznaka nema iznenađenja u binarnom gcd-u.</li>
<li>Binarni gcd: nakon uklanjanja zajedničkih faktora $2$, u petlji <code>b -= a</code> s $a \le b$; ne zaboravi vratiti pomak $s$.</li>
<li>Kandidat $x$ mora biti $\le r - k + 1$; inače za preostala izbacivanja ne bi bilo mjesta i skup bi mogao ostati prazan.</li>
<li>Rekurzija ne smije zamijeniti $\max$ podproblema i $\gcd$ – uvijek prenosi $\text{cur}$.</li>
</ul>
<h3>6. Primjer</h3>
<p>$a = (3, 2, 6, 4)$, upit $(1, 4, 2)$, $r - k + 1 = 3$. $\text{chg}[1] = [(1, 3), (2, 1)]$ ($g(1,1) = 3$, $g(1, 2..4) = 1$).</p>
<ul>
<li>$x = 1$: $F(2, 4, 1, 0)$. $\text{chg}[2] = [(2, 2)]$ (sve $2$). Kandidati: $x = 2 \Rightarrow \gcd(6, 4) = 2$; blok $(2, 2)$: $x = 4$, $F(5, 4, 0, 2) = 2$. Rezultat $2$.</li>
<li>Blok $(1, 3)$: $x = \min(2, 3) = 2$, $F(3, 4, 1, 3)$. $\text{chg}[3] = [(3, 6), (4, 2)]$. Kandidati: $x = 3 \Rightarrow \gcd(3, 4) = 1$; blok $(3, 6)$: $x = 4$, $F(5, 4, 0, \gcd(3, 6)) = 3$; blok $(4, 2)$: $x = 4$, ali $x - 1 = 3 < 4$ – preskok. Rezultat $3$.</li>
<li>Blok $(2, 1)$: $x = 3$, $F(4, 4, 1, 1)$: $x = 4 \Rightarrow F(5, 4, 0, 1) = 1$. Rezultat $1$.</li>
</ul>
<p>Odgovor $3$ (zadržani $3$ i $6$, izbačeni $2$ i $4$).</p>
''',
    'verified': r'''Uzorak 1/1, 300 slučajnih malih testova protiv brute forcea, 3 velika testa (najviše 0.11 s).''',
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
        ('Što od kretanja po grafu uopće ostaje bitno kad je teleport u $1$ besplatan?',
         r'''<p>Samo <em>redoslijed</em> borbi. Čudovište $v$ možemo napasti čim postoji put $1 \to \dots \to v$ čiji su svi unutarnji vrhovi već pobijeđeni; indukcijom je skup pobijeđenih uvijek „zatvoren prema dolje” (svaki pobijeđeni vrh ima pobijeđenog prethodnika ili prethodnika $1$), pa je uvjet ekvivalentan: $v$ ima barem jednog prethodnika u $\{1\} \cup \text{pobijeđeni}$. HP se mijenja samo u borbama, dakle tražimo poredak svih čudovišta, u kojem svako ima ranije pobijeđenog prethodnika, koji minimizira potreban početni HP.</p>'''),
        ('Kako se potreban početni HP za zadani poredak računa unatrag?',
         r'''<p>Ako nakon borbe s $x$ za ostatak treba $R$ HP-a, prije borbe treba $X \ge a_x$ i $X - a_x + b_x \ge R$, tj. $X \ge a_x + \max(R - b_x, 0)$. To je oblik koji se lako slaže u DP po skupu preostalih čudovišta: $f_S = \min_{x \in S \text{ dostupan}} \bigl(a_x + \max(f_{S \setminus x} - b_x, 0)\bigr)$, gdje je $x$ dostupan ako ima prethodnika izvan $S$ (već pobijeđenog ili $1$). Stanje je samo skup $S$ jer potreban HP ovisi samo o tome što preostaje. $O(n 2^{n-1})$ – dovoljno za $n \le 26$.</p>'''),
        ('Što nam daje $n + m \le 72$ kad je $n$ velik?',
         r'''<p>Za $n \ge 27$ je $m \le 45$. Svaki vrh $v \ne 1$ ima bar jedan ulazni luk; ako svakom odaberemo točno jednog „roditelja”, dobijemo korijensko stablo, a broj izbora je $\prod_v \deg^-(v) \le 2^{m - (n-1)} \le 2^{19}$. U optimalnom poretku za DAG svaki vrh ima <em>prvog pobijeđenog</em> prethodnika – uzmemo li njega za roditelja, poredak je valjan i za to stablo. Obratno, poredak valjan za bilo koje stablo valjan je za DAG. Dakle: odgovor DAG-a $=$ minimum optimuma po svim stablima, a na stablu postoji brz pohlepni algoritam.</p>'''),
        ('Kako izgleda optimalan poredak bez ograničenja i zašto?',
         r'''<p>Blok borbi opišimo parom $(A, D)$: potreban HP i neto promjena. Spajanje: $(A_p, D_p) \oplus (A_q, D_q) = (\max(A_p, A_q - D_p), D_p + D_q)$. Zamjena dvaju susjednih blokova mijenja samo cijenu tog para (ukupni $D$ para je isti), pa je optimalan poredak sortiranje po pravilu susjedne zamjene: blokovi s $D \ge 0$ ispred onih s $D < 0$; među $D \ge 0$ po rastućem $A$; među $D < 0$ po padajućem $A + D$. Provjera po slučajevima pokazuje $\text{cijena}(x, y) \le \text{cijena}(y, x)$ kad god pravilo stavlja $x$ ispred $y$.</p>'''),
        ('Kako ograničenje „roditelj prije djeteta” uklopiti u pohlepni poredak?',
         r'''<p>Uzmemo nekorijenski blok $x$ najvišeg prioriteta. U optimalnom poretku (u kojem su dosadašnji blokovi uzastopni) između bloka roditelja $h$ i $x$ stoje neki blokovi $y_1, \dots, y_t$; nijedan nije potomak $x$-a, a svaki ima prioritet $\le x$. Zamjenama susjeda pomaknemo $x$ neposredno iza $h$ bez povećanja cijene, a ograničenja ostaju zadovoljena. Zato $x$ smijemo <em>spojiti</em> u $h$ operacijom $\oplus$; stablo se smanji za jedan vrh. Nakon $n-1$ spajanja korijenski blok ima $A$ = odgovor. $O(n^2)$ po stablu, ukupno $O(2^{m-n+1} n^2)$.</p>'''),
    ],
    'tips': [
        r'''Kad je ukupno „$n + m \le C$”, razmisli o dva režima: mali $n$ (eksponencijalno u $n$, npr. DP po podskupovima) i mali $m - n$ (eksponencijalno u broju „viška” lukova); rješenje bira jeftiniji.''',
        r'''Nizove borbi/poslova s pragom i promjenom opisuj parom $(A, D)$ sa spajanjem $(\max(A_p, A_q - D_p), D_p + D_q)$ – to je asocijativna operacija i temelj svih argumenata zamjene.''',
        r'''Pravilo susjedne zamjene daje optimalan poredak bez ograničenja; s ograničenjima oblika stabla (roditelj prije djeteta) standardno se pretvara u „spoji element najvišeg prioriteta s roditeljem”.''',
        r'''U DP-u po podskupovima s uvjetom dostupnosti provjeri uvjet bit-maskom prethodnika: $\text{maska}(v) \,\&\, \lnot S \ne 0$ u $O(1)$ umjesto petlje po lukovima.''',
    ],
    'detailed': r'''
<h3>1. Svođenje na poredak</h3>
<p>Kretanje lukovima je besplatno, teleport u $1$ također, HP se mijenja samo u prvoj borbi na svakom vrhu. Da bismo napali $v$, trebamo put $1 \to \dots \to v$ čiji su svi unutarnji vrhovi već pobijeđeni. <strong>Tvrdnja:</strong> to je moguće ako i samo ako $v$ ima prethodnika $u$ koji je vrh $1$ ili već pobijeđen. Smjer $\Rightarrow$ je očit; za $\Leftarrow$ indukcijom po broju pobijeđenih: svaki pobijeđeni vrh $u$ imao je u trenutku svoje borbe put kroz pobijeđene vrhove, koji i dalje postoji, pa ga produljimo lukom $u \to v$. $\square$</p>
<p>Zadatak je stoga: naći poredak $\pi$ svih čudovišta $2..n$ u kojem svako ima ranije pobijeđenog prethodnika (ili prethodnika $1$) i koji minimizira potreban početni HP $X(\pi)$.</p>
<h3>2. Potreban HP i blokovi</h3>
<p>Za niz borbi $x_1, \dots, x_t$ potreban početni HP zadovoljava: $X \ge a_{x_1}$ i $X - a_{x_1} + b_{x_1} \ge$ (potreban HP za ostatak). Označimo blok uzastopnih borbi parom $(A, D)$: $A$ = najmanji HP s kojim se blok može odraditi, $D = \sum (b - a)$ = neto promjena HP-a. Pojedinačno čudovište je $(a_v, b_v - a_v)$, vrh $1$ je $(0, 0)$. <strong>Spajanje</strong> blokova $p$ pa $q$: $$p \oplus q = \bigl(\max(A_p,\ A_q - D_p),\ D_p + D_q\bigr),$$ jer nakon $p$ imamo $X + D_p$ HP-a i treba $X + D_p \ge A_q$. Operacija je asocijativna (odgovara nadovezivanju nizova). Vrijednosti su do $72 \cdot 10^{15} < 2^{63}$: <code>long long</code>.</p>
<h3>3. Režim $n \le 26$: DP po podskupovima</h3>
<p>Neka je $f_S$ najmanji HP potreban u trenutku kad je skup <em>preostalih</em> čudovišta $S$ (sva ostala pobijeđena). $f_\emptyset = 0$ i $$f_S = \min_{x \in S,\ x \text{ dostupan}} \bigl(a_x + \max(f_{S \setminus \{x\}} - b_x,\ 0)\bigr),$$ gdje je $x$ dostupan ako ima prethodnika izvan $S$ (pobijeđen ili $1$); odgovor je $f_{\{2..n\}}$. Ispravnost: potreban HP ovisi samo o skupu preostalih i poretku u kojem ćemo ih riješiti, a formula je upravo optimizacija po prvom sljedećem $x$. Dostupnost provjeravamo bit-maskom prethodnika u $O(1)$. Složenost $O(n 2^{n-1})$; za $n = 26$ oko $8.7 \cdot 10^8$ jednostavnih operacija i $2^{25}$ 64-bitnih vrijednosti ($256$ MB) – unutar limita ($7$ s, $1024$ MB).</p>
<h3>4. Režim velikog $n$: nabrajanje stabala</h3>
<p>Iz $n + m \le 72$ i $n \ge 27$ slijedi $m \le 45$. Svaki vrh $v \ne 1$ ima $d_v \ge 1$ ulaznih lukova, $\sum d_v = m$. Izbor po jednog ulaznog luka za svaki $v$ daje korijensko stablo; broj izbora je $\prod d_v \le \prod 2^{d_v - 1} = 2^{m - (n-1)} \le 2^{19}$ (jer $d \le 2^{d-1}$ za $d \ge 1$).</p>
<p><strong>Lema.</strong> $\min_\pi X(\pi)$ po poredcima valjanim za DAG jednak je minimumu po svim stablima $T$ od $\min_\pi X(\pi)$ po poredcima valjanim za $T$ (roditelj prije djeteta). <em>Dokaz.</em> Poredak valjan za stablo valjan je za DAG (roditelj je prethodnik). Obratno, za optimalan DAG-poredak $\pi^\ast$ svakom $v$ dodijelimo kao roditelja njegova <em>prvog pobijeđenog</em> prethodnika (ili $1$); $\pi^\ast$ je valjan za to stablo. $\square$</p>
<h3>5. Pohlepni algoritam na stablu</h3>
<p><strong>Pravilo prioriteta (bez ograničenja).</strong> Za blokove $x, y$ neka je $x \prec y$ („$x$ ide prije”) ako: $D_x \ge 0 > D_y$; ili $D_x, D_y \ge 0$ i $A_x < A_y$; ili $D_x, D_y < 0$ i $A_x + D_x > A_y + D_y$. <strong>Lema o zamjeni.</strong> Ako $x \prec y$ (ili su neusporedivi), tada $\text{cijena}(x, y) := \max(A_x, A_y - D_x) \le \text{cijena}(y, x) = \max(A_y, A_x - D_y)$.</p>
<ul>
<li>$D_x \ge 0 > D_y$: $\text{cijena}(x, y) \le \max(A_x, A_y)$ jer $A_y - D_x \le A_y$; $\text{cijena}(y, x) \ge \max(A_y, A_x)$ jer $A_x - D_y > A_x$.</li>
<li>$D_x, D_y \ge 0$, $A_x \le A_y$: $\text{cijena}(x, y) \le \max(A_x, A_y) = A_y \le \text{cijena}(y, x)$.</li>
<li>$D_x, D_y < 0$, $A_x + D_x \ge A_y + D_y$: tada $A_y - D_x \le A_x - D_y$, a $A_x < A_x - D_y$; dakle $\text{cijena}(x, y) \le A_x - D_y \le \text{cijena}(y, x)$.</li>
</ul>
<p>Zamjena dvaju susjednih blokova ne mijenja ništa za blokove prije (isti početni HP) ni poslije (isti ukupni $D$ para), pa je poredak sortiran po $\prec$ optimalan bez ograničenja.</p>
<p><strong>Ograničenja stabla.</strong> Održavamo blokove (početno pojedinačni vrhovi; korijen $1$ je blok $(0,0)$) i strukturu stabla nad blokovima. <em>Tvrdnja:</em> ako je $x$ nekorijenski blok najvišeg prioriteta, postoji optimalan poredak u kojem $x$ dolazi neposredno nakon bloka $h$ koji sadrži njegova roditelja. <em>Dokaz.</em> Indukcijom pretpostavimo da postoji optimalan poredak u kojem je svaki dosadašnji blok uzastopan. Neka između $h$ i $x$ stoje blokovi $y_1, \dots, y_t$. Nijedan $y_i$ nije potomak $x$-a (potomci dolaze iza $x$), a svaki ima prioritet $\le$ prioriteta $x$. Pomicanje $x$ ispred $y_t$, pa ispred $y_{t-1}$, … susjednim zamjenama ne povećava cijenu (lema o zamjeni) i ne krši ograničenja: $x$ ostaje iza $h$, a $y_i$ ostaju iza svojih roditelja. $\square$ Zato $x$ spajamo u $h$: $\text{blok}(h) \gets \text{blok}(h) \oplus \text{blok}(x)$, djeca $x$-a postaju djeca $h$-a (union–find nad vrhovima). Nakon $n - 1$ spajanja ostaje korijenski blok; njegov $A$ je potreban početni HP.</p>
<p>Implementacija: u svakom koraku linearno nađi blok najvišeg prioriteta ($O(n)$), spoji ($O(1)$ uz union–find): $O(n^2)$ po stablu; sortiranje bi dalo $O(n \log n)$, ali za $n \le 72$ nije potrebno. Stabla nabrajamo brojačem u miješanoj bazi (indeks izabranog ulaznog luka za svaki vrh).</p>
<h3>6. Izbor režima i složenost</h3>
<p>Procijenimo $c_{\text{stabla}} = n^2 \prod d_v$ i $c_{\text{DP}} = n 2^{n-1}$ i pokrenemo jeftiniji (procjena u <code>double</code>, jer $\prod d_v$ može biti golem kad je $n$ malen). Za $n \le 26$ DP je $\le 8.7 \cdot 10^8$; za $n \ge 27$ stabla su $\le 2^{19} \cdot 72^2 \approx 2.7 \cdot 10^9$ u apsolutno najgorem slučaju, no tada je $n \le 45$ pa je realno $\le 2^{19} \cdot 45^2 \approx 10^9$ vrlo jednostavnih operacija – u praksi ispod sekunde (limit $7$ s). Često je $\prod d_v$ mnogo manji od granice pa se stabla isplate i za $n \le 26$.</p>
<h3>7. Primjer</h3>
<p>$n = 4$, $(a, b) = (4, 2), (5, 3), (2, 6)$ za vrhove $2, 3, 4$; lukovi $1 \to 2, 1 \to 3, 2 \to 4, 3 \to 4$. Blokovi: $2: (4, -2)$, $3: (5, -2)$, $4: (2, +4)$. Najviši prioritet ima $4$ ($D \ge 0$); stablo s roditeljem $2$: $\text{blok}(2) = (4, -2) \oplus (2, 4) = (\max(4, 2 + 2), 2) = (4, 2)$. Sad su blokovi $2': (4, 2)$ i $3: (5, -2)$; prioritet ima $2'$, spajamo u korijen: $(0,0) \oplus (4, 2) = (4, 2)$; zatim $3$: $(4, 2) \oplus (5, -2) = (\max(4, 3), 0) = (4, 0)$. Odgovor $4$ (poredak $2, 4, 3$: HP $4 \to 2 \to 6 \to 4$). Stablo s roditeljem $3$ za vrh $4$ daje $5$, pa je minimum $4$.</p>
''',
    'verified': r'''Uzorak 1/1, 300 slučajnih malih testova protiv brute forcea (oba režima – DP i stabla – forsirana i međusobno uspoređena), 3 velika testa (najviše 0.50 s).''',
    'solution': r'''
<p>Ako je $n \le 26$, koristimo DP po podskupovima. Neka je $f_S$ najmanji početni HP potreban kad je skup pobijeđenih čudovišta $S$. Nabrajamo prethodno pobijeđeno čudovište $x$ i ažuriramo $f_{S \cup \{x\}}$ vrijednošću $\max(f_S - b_x, 0) + a_x$, gdje $x \notin S$, a $S$ ne sadrži sve vrhove koji imaju luk prema $x$ (tj. $x$ je dostupan). Vremenska složenost: $O(n 2^{n-1})$.</p>
<p>Ako je $n \ge 27$, iz uvjeta $n + m \le 72$ slijedi $m \le 45$. Budući da vrh $1$ dostiže sve ostale vrhove, preostalih $n - 1$ vrhova ima barem jedan ulazni luk; nakon uklanjanja tih lukova najviše $19$ vrhova ima ulazni stupanj veći od $1$.</p>
<p>Za svaki vrh nabrojimo jedan ulazni luk kao roditeljski, čime dobivamo korijensko stablo. Ukupno ima $2^{m-n+1}$ mogućih stabala, a potproblem na korijenskom stablu klasičan je pohlepni algoritam.</p>
<p>Zanemarimo li ograničenje roditelja, optimalni redoslijed napada dobiva se sortiranjem. Uzmemo prvo čudovište koje treba pobijediti u optimalnom poretku; čim je njegov roditelj pobijeđen, odmah moramo pobijediti i njega. Stoga ga spojimo s roditeljem, smanjujući veličinu problema za $1$, i ponavljamo $n - 1$ krugova dok problem ne postane veličine $1$.</p>
<p>Složenost svakog potproblema je $O(n \log n)$, pa je ukupna vremenska složenost $O(2^{m-n+1} n \log n)$.</p>
''',
},
]
