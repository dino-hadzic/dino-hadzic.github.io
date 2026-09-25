# -*- coding: utf-8 -*-
STAGE = {
    'no': 13,
    'name': 'Stage 13: Iberia',
    'source_name': '44th Petrozavodsk Programming Camp, Day 6: Um_nik mod 998 244 353 Contest',
    'source_html': r'''
<p>Prijevod službenog rješenja autorskog tima (Um_nik, 998batrr, 244mhq, 353cerega): <a href="https://contest.ucup.ac/download.php?type=attachments&amp;id=1212&amp;r=2">Tutorial (en)</a>. Tekst zadatka preveden je prema službenim <a href="https://contest.ucup.ac/download.php?type=attachments&amp;id=1212&amp;r=1">engleskim tekstovima zadataka</a>. Zadatak je dostupan na <a href="https://contest.ucup.ac/contest/1212">Universal Cup Judging System</a>.</p>
''',
}

PROBLEMS = [
# ---------------------------------------------------------------- A
{
    'letter': 'A', 'title': 'The Best Problem of 2021', 'title_hr': 'Najbolji zadatak 2021.', 'slug': 'A_the_best_problem_of_2021',
    'tl': '2 s', 'ml': '512 MiB',
    'statement': r'''
<p>Dan je niz $B$ od $n$ brojeva i broj $X$; svi su zadani kao binarni nizovi duljine točno $m$. Brojeve promatramo kao vektore nad $\mathbb{Z}_2$ s bitovnim XOR-om kao zbrajanjem. Izračunaj, modulo $998244353$, broj podskupova $S \subseteq \{1, 2, \dots, X\}$ kojima je $B$ jedna od baza: $B$ je baza skupa $S$ ako je to niz najmanje veličine takav da se svaki element skupa $S$ može zapisati kao XOR nekih elemenata iz $B$.</p>
<h3>Ulaz</h3>
<p>$n$ i $m$ ($1 \le n, m \le 2000$), zatim $n$ binarnih nizova duljine $m$ (elementi $B$) i binarni niz duljine $m$ ($X$).</p>
<h3>Izlaz</h3>
<p>Traženi broj.</p>
<h3>Primjer</h3>
<p>Za $B = \{0001, 0010, 0100, 1000\}$ i $X = 1101$ odgovor je $7364$.</p>
''',
    'hints': [],
    'coach': [],
    'solution': None,
},
# ---------------------------------------------------------------- B
{
    'letter': 'B', 'title': 'Random Interactive Convex Hull Bot', 'title_hr': 'Slučajna interaktivna konveksna ljuska', 'slug': 'B_random_interactive_convex_hull_bot',
    'tl': '4 s', 'ml': '512 MiB',
    'statement': r'''
<p><em>Interaktivni zadatak.</em> Skup od $n$ točaka odabran je uniformno slučajno među svim skupovima točaka s pozitivnim cjelobrojnim koordinatama do $10^9$ u kojima nikoje tri točke nisu kolinearne. Točke ne vidiš; smiješ postavljati upite „<code>? i j k</code>”, na koje sudac odgovara $1$ ako je zaokret od $\overrightarrow{P_iP_j}$ prema $\overrightarrow{P_iP_k}$ u smjeru suprotnom od kazaljke na satu, a $-1$ inače (predznak vektorskog produkta). Odredi konveksnu ljusku i ispiši „<code>! k i_1 … i_k</code>” s indeksima vrhova ljuske u pozitivnom smjeru.</p>
<h3>Ograničenja</h3>
<p>$3 \le n \le 5000$, najviše $30\,000$ upita. Poredak točaka je također slučajan; interaktor nije adaptivan.</p>
''',
    'hints': [
        r'''<p>Bez koordinata ne možeš naći „najljeviju” točku ni sortirati kutove jeftino. Umjesto toga dodaj točke jednu po jednu i održavaj trenutnu ljusku: točka unutar ljuske ne mijenja ništa.</p>''',
        r'''<p>Provjera „je li nova točka unutar poligona” linearnim prolazom po stranicama troši previše upita. Binarno pretraživanje po dijagonalama poligona: jedan upit kaže na kojoj je strani dijagonale točka, čime se odbacuje pola poligona.</p>''',
        r'''<p>Očekivana veličina ljuske slučajnih točaka u kvadratu je $O(\log n)$, a vjerojatnost da $i$-ta točka mijenja ljusku je otprilike $H_i / i$ — zato je ukupan broj upita mali.</p>''',
    ],
    'coach': [
        ('Što točno saznajemo jednim upitom i kako se iz toga provjerava je li točka unutar konveksnog poligona?', r'''<p>Upit „<code>? i j k</code>” vraća predznak vektorskog produkta $\overrightarrow{P_iP_j} \times \overrightarrow{P_iP_k}$, tj. kaže je li $P_k$ <em>lijevo</em> ($+1$) ili <em>desno</em> ($-1$) od usmjerenog pravca $P_i \to P_j$; nule nema jer nikoje tri točke nisu kolinearne. Konveksan poligon zadan vrhovima u pozitivnom smjeru (suprotno od kazaljke) leži lijevo od svakog svog usmjerenog brida, pa je točka unutra ako i samo ako je lijevo od svih $H$ bridova. To je $H$ upita po točki — prevelik trošak, ali pokazuje da je „lijevo od pravca” jedini alat koji imamo.</p>'''),
        ('Zašto ne možemo primijeniti Grahamov ili Andrewov algoritam i zašto je inkrementalni pristup prirodan baš za slučajne točke?', r'''<p>Ti algoritmi sortiraju točke po koordinati ili kutu, a mi nemamo koordinate: sortiranje $5000$ točaka usporedbama tražilo bi $\approx n \log_2 n \approx 60\,000$ upita, više od limita. S druge strane, konveksna ljuska $i$ slučajnih točaka u kvadratu ima očekivano samo $\Theta(\log i)$ vrhova (za $i = 5000$ oko $20$), a nova slučajna točka pada izvan trenutne ljuske s vjerojatnošću reda $H_i / i$. Dodajemo li točke jednu po jednu, gotovo svaka je unutra i ljusku treba mijenjati samo $O(\log^2 n)$ puta; pitanje se svodi na to koliko upita košta test „je li nova točka unutar poligona od $H$ vrhova”.</p>'''),
        (r'Kako uz $O(\log H)$ upita saznati je li točka unutra, a ako nije — preko kojeg je brida izašla?', r'''<p>Fiksiramo jedan vrh ljuske kao <em>pivot</em> $h_0$ i gledamo lepezu zraka $h_0 \to h_1, \dots, h_0 \to h_{H-1}$; one se okreću u pozitivnom smjeru i zajedno pokrivaju kut manji od $180^\circ$. Za točku $q$ predikat $L(t) = $ „$q$ je lijevo od $h_0 \to h_t$” je, kad je $q$ unutar toga kuta, oblika istina, …, istina, laž, …, laž — pa binarno pretraživanje s $\lceil \log_2 H \rceil$ upita nađe trokut lepeze $(h_0, h_t, h_{t+1})$ u kojem $q$ leži. Dvije stranice tog trokuta su zrake za koje već znamo stranu, pa još jedan upit za brid $h_t \to h_{t+1}$ odlučuje: lijevo znači unutra, desno znači da je baš taj brid vidljiv iz $q$. Ako je $q$ izvan kuta lepeze („iza” pivota), predikat je ili konstantan ili oblika laž…istina, a binarno pretraživanje tada završi na jednom od dva kraja — i u oba je slučaja odgovarajući brid uz pivot vidljiv, pa je zaključak i tada točan.</p>'''),
        ('Kako se ljuska popravlja kad je točka vani i zašto je to jeftino?', r'''<p>Bridovi vidljivi iz vanjske točke čine neprekinut lanac na konveksnom poligonu, a mi već znamo jedan njegov brid. Hodamo od njega u oba smjera i pitamo za susjedni brid dok je vidljiv; svaki korak ukloni jedan vrh i košta jedan upit, a dva zadnja upita zaustavljaju hodanje. Novi poligon je $h_{lo}, q, h_{hi}, \dots$ i ostaje konveksan i pozitivno orijentiran. Svaki vrh može biti uklonjen najviše jednom, pa je ukupni trošak popravaka $O(n + \text{broj umetanja})$ upita.</p>'''),
        (r'Je li $30\,000$ upita doista dovoljno i kako binarno pretraživanje učiniti jeftinijim od $\lceil \log_2 H \rceil$?', r'''<p>Gruba procjena $\sum_i (1 + \lceil \log_2 H_{i-1} \rceil) \approx 5000 \cdot 6$ je opasno blizu limita. Trokuti lepeze imaju vrlo različite površine (uz kutove ljuske su sitni, prema suprotnim stranama kvadrata veliki), a nova točka je uniformno slučajna — vjerojatnost da padne u trokut proporcionalna je njegovoj površini. Površine ne znamo, ali ih procjenjujemo brojem ranijih točaka koje su pale u pojedini trokut, pa u binarnom pretraživanju dijelimo lepezu po <em>težini</em>, a ne po broju zraka. Očekivani broj upita tada pada s $\log_2 H$ na približno entropiju te raspodjele (oko $3$–$4$ bita). Ispravnost ne ovisi o težinama, samo brzina; mjereno na lokalnom interaktoru: prosječno $\approx 23\,500$, najviše $26\,529$ upita za $n = 5000$.</p>'''),
    ],
    'tips': [
        r'''U interaktivnim zadacima svaki odgovor je jedan bit informacije: prebroji koliko bitova trebaš (npr. $\log_2$ broja mogućih ishoda) i usporedi s limitom prije nego što kreneš kodirati — ako je procjena blizu limita, treba ideja koja smanjuje očekivani broj upita, ne samo najgori slučaj.''',
        r'''Kad ulaz obećava slučajnost, iskoristi je: ljuska slučajnih točaka ima $O(\log n)$ vrhova, a empirijske frekvencije ranijih točaka izvrsna su procjena vjerojatnosti za buduće — tim se procjenama može voditi „težinsko” binarno pretraživanje.''',
        r'''Za interaktivne zadatke napiši vlastiti interaktor (skripta koja generira ulaz, odgovara na upite i provjerava ispis) i mjeri najgori broj upita na mnogo slučajnih testova — to je jedini pošten lokalni test.''',
        r'''Predikat „točka je lijevo od usmjerenog pravca” monoton je duž lepeze zraka iz jednog vrha konveksnog poligona samo unutar kuta lepeze; uvijek provjeri što se događa s krajnjim slučajevima (točka „iza” pivota) i dokaži da pretraga i tada daje smislen odgovor.''',
    ],
    'solution': r'''
<p>Budući da nemamo pristup koordinatama, teško je koristiti standardne algoritme koji se oslanjaju na traženje najljevije točke; i sortiranje točaka zahtijevalo bi previše upita. Trebamo drugačiji pristup.</p>
<p>Umećemo točke jednu po jednu i održavamo trenutnu konveksnu ljusku. Ako je točka unutar trenutne ljuske, ništa ne mijenjamo; inače je umećemo na pravo mjesto i uklanjamo točke koje više nisu na ljusci.</p>
<p>Upit interpretiramo kao pitanje „u kojoj poluravnini u odnosu na pravac $(P_iP_j)$ leži $P_k$?”. Želimo provjeriti leži li nova točka u istoj poluravnini kao ostatak poligona za sve pravce koji sadrže stranice poligona, i ako ne, pronaći „lošu” stranicu. Linearno pretraživanje troši previše upita, ali kako je zadatak interaktivan, koristimo binarno pretraživanje.</p>
<p>Odaberemo dijagonalu poligona i pitamo u kojoj poluravnini leži nova točka; tada možemo odbaciti sve stranice u drugoj poluravnini. Ako biramo dijagonalu koja dijeli poligon na pola, odbacujemo gotovo polovicu točaka, pa u $\log_2 H$ upita ($H$ je trenutna veličina ljuske) problem svodimo na trokut. U još $3$ upita saznajemo leži li nova točka u trokutu.</p>
<p>Ako leži, gotovi smo. Ako ne, znamo kamo je umetnuti, a zatim uklanjamo točke u njezinoj blizini dok poligon nije konveksan.</p>
<p>Procijenimo broj upita. Ako novu točku umećemo $k$ puta, točke uklanjamo najviše $k$ puta, pa nakon utvrđivanja da smo izvan trokuta trošimo najviše $3k$ upita. U dijelu s trokutom ne trebamo pitati za stranice koje su dijagonale izvornog poligona jer smo ih već pitali, što broj upita smanjuje na $\max(3, 2 + \log_2(H - 2))$; s dodatnim doradama može se postići $\max(3, 1 + \log_2(H - 1))$, no to nije nužno.</p>
<p>Ukupan broj upita ograničen je s $2n + 3k + \sum_{i=3}^{n} \log_2(H_{i-1})$. Poznato je da je očekivana veličina konveksne ljuske $m$ slučajnih točaka u kvadratu $O(\log m)$, a kako je prefiks (više-manje) slučajan skup, taj zbroj je $O(n \log \log n)$. Vjerojatnost da nakon dodavanja $i$-te točke moramo popraviti ljusku je otprilike $H_i / i$, pa je $k = O(\log^2 n)$. To ulazi u limit; naše implementacije troše između $24\,000$ i $27\,000$ upita.</p>
''',
    'detailed': r'''
<h3>1. Što upit zapravo govori</h3>
<p>Odgovor na „<code>? i j k</code>” je predznak vektorskog produkta $\overrightarrow{P_iP_j}\times\overrightarrow{P_iP_k}$. Predznak $+1$ znači da je $P_k$ <em>lijevo</em> od usmjerenog pravca $P_i\to P_j$, a $-1$ da je desno; nula se ne pojavljuje jer je zajamčeno da nikoje tri točke nisu kolinearne. To je jedini alat koji imamo — nemamo koordinate, ne možemo uspoređivati po $x$ ni sortirati po kutu bez mnogo upita. Cijelo rješenje treba izgraditi iz pitanja oblika „na kojoj je strani pravca točka”.</p>
<p>Za konveksan poligon $h_0,h_1,\dots,h_{m-1}$ zadan u pozitivnom smjeru (suprotno od kazaljke na satu) unutrašnjost je presjek lijevih poluravnina svih usmjerenih bridova $h_t\to h_{t+1}$. Kažemo da je brid $h_t\to h_{t+1}$ <em>vidljiv</em> iz točke $q$ ako je $q$ desno od njega; točka je izvan poligona ako i samo ako vidi barem jedan brid, a bridovi koje vidi čine neprekinut (ciklički) lanac.</p>

<h3>2. Zašto inkrementalno i zašto to za slučajne točke radi</h3>
<p>Ulaz je slučajan i redoslijed točaka je slučajan, a to je ključno. Poznato je da konveksna ljuska $i$ uniformno slučajnih točaka u kvadratu ima očekivano $\frac{8}{3}\ln i + O(1)$ vrhova, dakle oko $20$ za $i=5000$. Ako točke dodajemo redom $1,2,\dots,n$ i održavamo ljusku dosad viđenih točaka, tada je $i$-ta točka (po simetriji – svaka od prvih $i$ točaka jednako je vjerojatno „zadnja”) vrh ljuske prvih $i$ točaka s vjerojatnošću $H_i/i$, pa je očekivani broj umetanja $\sum_i H_i/i = O(\log^2 n)$, u praksi oko $80$–$100$. Gotovo sve točke su, dakle, unutra, i glavno je pitanje koliko upita košta test „je li $q$ unutar trenutne ljuske”, a ako nije, koji je brid vidljiv.</p>
<p>Početak: točke $1,2,3$ čine trokut; jedan upit „<code>? 1 2 3</code>” kaže je li redoslijed $1,2,3$ pozitivan (tada je ljuska $[1,2,3]$) ili treba $[1,3,2]$. Za $n=3$ to je sve.</p>

<h3>3. Lokalizacija lepezom iz pivota</h3>
<p>Ljusku držimo u vektoru <code>ljuska</code>, u pozitivnom smjeru, i njezin prvi vrh $h_0$ zovemo <em>pivot</em>. Zrake $h_0\to h_1, h_0\to h_2,\dots,h_0\to h_{m-1}$ okreću se u pozitivnom smjeru i zajedno zatvaraju kut manji od $180^\circ$ (unutarnji kut konveksnog poligona u vrhu $h_0$). Za novu točku $q$ definiramo predikat $L(t)=$ „$q$ je lijevo od $h_0\to h_t$”, $1\le t\le m-1$, i dogovorno $L(0)=\text{istina}$, $L(m)=\text{laž}$. Ravninu oko $h_0$ dijelimo na <em>utore</em>:</p>
<ul>
<li>utor $0$: desno od zrake $h_0\to h_1$ (izvan poligona, iza brida $h_0h_1$);</li>
<li>utor $s$, $1\le s\le m-2$: između zraka $h_0\to h_s$ i $h_0\to h_{s+1}$ — to je trokut lepeze $(h_0,h_s,h_{s+1})$ produljen preko brida $h_sh_{s+1}$;</li>
<li>utor $m-1$: lijevo od zrake $h_0\to h_{m-1}$ (izvan poligona, iza brida $h_{m-1}h_0$).</li>
</ul>
<p>Tražimo $s$ takvo da vrijedi $L(s)$ i ne vrijedi $L(s+1)$. Binarno pretraživanje održava $lo\le s\le hi$ (početno $lo=0$, $hi=m-1$): pita za $t\in(lo,hi]$; ako $L(t)$ vrijedi, $lo\leftarrow t$, inače $hi\leftarrow t-1$. Ono je ispravno kad je $L$ „monotono”: istina za male $t$, laž za velike. Kada je to slučaj?</p>
<p><strong>Tvrdnja.</strong> Označimo smjer zrake $h_0\to h_t$ kutom $\theta_t$ ($\theta_1\lt \theta_2\lt \dots\lt \theta_{m-1}$, raspon manji od $\pi$) i smjer $h_0\to q$ kutom $\varphi$. $L(t)$ vrijedi točno kad je $\varphi-\theta_t\in(0,\pi)$ (mod $2\pi$).</p>
<ul>
<li>Ako je $\varphi\in(\theta_1,\theta_{m-1})$ ($q$ je u kutu lepeze), tada je $L(t)$ istina točno za $\theta_t\lt \varphi$, dakle za $t=1,\dots,s$ i laž za $t>s$: predikat je monoton, a pronađeni utor $s\in[1,m-2]$ zaista je trokut lepeze koji sadrži $q$ (odnosno njegovo produljenje).</li>
<li>Ako je $q$ lijevo od svih zraka, $L\equiv$ istina, pretraga završi u utoru $m-1$; ako je desno od svih, $L\equiv$ laž i završi u utoru $0$. Oba su slučaja opisana ispravno.</li>
<li>Ako je $q$ „iza” pivota ($\varphi\in(\theta_1+\pi,\theta_{m-1}+\pi)$), predikat je oblika laž, …, laž, istina, …, istina — u <em>krivom</em> smjeru. No pretraga i tada završi u utoru $0$ ili $m-1$: na kraju je $lo=hi=s$, pri čemu je $L(s)$ bila upitana i istinita (ili je $s=0$) i $L(s+1)$ upitana i lažna (ili je $s=m-1$). Za $1\le s\le m-2$ to bi značilo istina pa laž u rastućem predikatu — nemoguće. Dakle $s=0$ (pa znamo $L(1)$ laž) ili $s=m-1$ (pa znamo $L(m-1)$ istina).</li>
</ul>
<p>Sad zaključujemo: utor $0$ znači „$q$ desno od $h_0\to h_1$”, što je točno definicija vidljivosti brida $h_0h_1$; utor $m-1$ znači „$q$ lijevo od $h_0\to h_{m-1}$”, tj. desno od $h_{m-1}\to h_0$, pa je vidljiv brid $h_{m-1}h_0$. Za utor $1\le s\le m-2$ postavljamo još jedan upit, za brid $h_s\to h_{s+1}$: ako je $q$ lijevo, $q$ je u trokutu $(h_0,h_s,h_{s+1})\subseteq$ ljuska, dakle unutra; ako je desno, brid $h_sh_{s+1}$ je vidljiv. U svakom slučaju ili znamo da je točka unutra ili imamo jedan vidljiv brid, uz $\lceil\log_2 m\rceil+1$ upita u najgorem slučaju.</p>

<h3>4. Težinsko dijeljenje umjesto dijeljenja na pola</h3>
<p>Sami $\lceil\log_2 H\rceil+1$ upita po točki dali bi za $H\approx 20$ oko $6$ upita, tj. $\approx 30\,000$ ukupno — preblizu limitu. Poboljšanje dolazi iz slučajnosti: nova točka je uniformna u kvadratu, pa je vjerojatnost da padne u utor $s$ proporcionalna njegovoj površini unutar kvadrata. Te su površine vrlo neujednačene (trokuti uz „kutove” ljuske su sitni, oni prema suprotnim stranama veliki). Površine ne znamo, ali imamo njihovu prirodnu procjenu: broj <em>ranijih</em> točaka koje su pale u pojedini utor, koji pamtimo u <code>tezina[s]</code>. U binarnom pretraživanju zato ne biramo sredinu indeksa nego $t$ za koji su zbrojevi težina utora $[lo,t-1]$ i $[t,hi]$ što ujednačeniji (uz $+1$ po utoru da prazni utori ne budu potpuno „nevidljivi”). To je, u biti, Huffmanovo/entropijsko kodiranje: očekivani broj upita je približno entropija raspodjele točaka po utorima, koja je za ovakve lepeze oko $3$–$4$ bita umjesto $\log_2 20\approx 4.3$. Bitno: <strong>težine utječu samo na broj upita, ne na ispravnost</strong> — dokaz iz odjeljka 3 vrijedi za bilo koji izbor $t\in(lo,hi]$.</p>

<h3>5. Umetanje vanjske točke</h3>
<p>Neka je $e$ indeks vidljivog brida $h_e\to h_{e+1}$. Od njega hodamo unatrag: dok je brid $h_{lo-1}\to h_{lo}$ vidljiv (jedan upit po koraku), pomičemo $lo$ unatrag; i unaprijed: dok je $h_{hi}\to h_{hi+1}$ vidljiv, pomičemo $hi$. Kako vidljivi bridovi vanjske točke čine neprekinut lanac, a ne mogu biti vidljivi svi bridovi, hodanje se zaustavlja i dobivamo točno lanac $h_{lo},\dots,h_{hi}$. Vrhovi strogo između njih (ciklički) više nisu na ljusci; nova ljuska je $h_{lo},q,h_{hi},h_{hi+1},\dots$ i ostaje konveksna u pozitivnom smjeru. Trošak: po jedan upit za svaki uklonjeni vrh plus dva upita koja zaustavljaju hodanje; kako svaka točka može biti uklonjena najviše jednom, sve umetanja zajedno stoje $O(n+\text{broj umetanja})$ upita.</p>
<p>Održavanje težina: utori s indeksom manjim od $lo$ i većim od $hi$ ne mijenjaju se (zrake do tih vrhova ostaju iste). Utori koji nestaju zbroje se i podijele na dva nova utora (između zraka na $h_{lo}$ i $q$ te između zraka na $q$ i $h_{hi}$); ako je neki od tih novih utora vanjski (kad je $lo=0$ ili $hi=0$, tj. novi utor $0$ ili $m'-1$), dobiva težinu $0$ jer vanjske točke odmah završavaju u umetanju. Ako je pivot uklonjen ($0$ je strogo unutar cikličkog raspona $(lo,hi)$), novi pivot postaje $h_{hi}$, a težine jednostavno resetiramo na jednolike — to se događa rijetko i ne utječe na ispravnost.</p>

<h3>6. Broj upita i vremenska složenost</h3>
<p>Po točki: $1$ upit za početni trokut, za unutarnje točke $b_i+1$ upita, gdje je $b_i$ broj koraka težinskog binarnog pretraživanja; za vanjske točke $b_i$ (plus eventualno $1$) i još broj uklonjenih vrhova $+2$. Ukupno $\le n\cdot(\max_i b_i+1)+2\cdot\text{umetanja}+n$, a u očekivanju znatno manje. Na lokalnom interaktoru za $n=5000$ dobivamo prosječno oko $23\,500$ i najviše $26\,529$ upita u $143$ pokretanja, što je u skladu sa službenim rješenjima ($24\,000$–$27\,000$). Vrijeme rada je zanemarivo: $O(nH)$ operacija uz $H=O(\log n)$, sav trošak je u komunikaciji.</p>

<h3>7. Rubni slučajevi i zamke</h3>
<ul>
<li>Nakon svakog upita obavezno <code>fflush(stdout)</code>; ako čitanje odgovora ne uspije, program treba prekinuti.</li>
<li>Indeksi ljuske su ciklički: susjed od $0$ unatrag je $m-1$; pri uklanjanju vrhova treba razlikovati raspon koji se „omata” preko indeksa $0$ (tada pivot nestaje) od raspona s $hi=0$ (uklonjeni su samo vrhovi $lo+1,\dots,m-1$, pivot ostaje).</li>
<li>Ljuska ima uvijek barem $3$ vrha, pa binarno pretraživanje uvijek ima barem dva utora i pretraga za utor $0$ ili $m-1$ doista upita $L(1)$ odnosno $L(m-1)$ (na to se dokaz iz odjeljka 3 oslanja).</li>
<li>Odgovor se ispisuje kao „<code>! k i_1 … i_k</code>” u pozitivnom smjeru; početni vrh je proizvoljan, pa naš vektor <code>ljuska</code> ispisujemo kakav jest.</li>
<li>Broj upita valja mjeriti na mnogo slučajnih testova, ne na jednom: raspodjela ima „rep”, a limit je strog.</li>
</ul>

<h3>8. Kako smo to provjerili</h3>
<p>Uobičajeni stress harness ne može testirati interaktivan zadatak, pa je uz rješenje priložena skripta <code>interactor.py</code>: generira slučajne različite točke s cjelobrojnim koordinatama do $10^9$ (kolinearne trojke su pri takvim koordinatama praktički nemoguće; ako bi ih upit ipak pogodio, skripta test prekida s greškom), odgovara na upite predznakom vektorskog produkta, broji upite i na kraju uspoređuje ispisani ciklički niz s ljuskom izračunatom Andrewovim algoritmom. Time smo potvrdili točnost i izmjerili broj upita za $n$ od $3$ do $5000$.</p>
''',
    'verified': r'''Interaktivan zadatak – stress harness nije primjenjiv; lokalni interaktor (<code>interactor.py</code> u mapi rješenja, s provjerom ljuske Andrewovim algoritmom i limita od $30\,000$ upita): 143 testa s $n=5000$ (najviše $26\,529$ upita, prosjek $\approx 23\,500$; dodatnih 20 testova s $n=5000$ nakon završnog uređivanja koda, najviše $25\,662$ upita), 50 testova $n=2500$, po 200–300 testova za $n\in\{3,4,5,6,7,8,12,20,30,50,100,1000\}$ — svi točni.''',
},
# ---------------------------------------------------------------- C
{
    'letter': 'C', 'title': 'Record Parity', 'title_hr': 'Parnost rekorda', 'slug': 'C_record_parity',
    'tl': '1 s', 'ml': '512 MiB',
    'statement': r'''
<p>Dana je permutacija duljine $n$ i broj $k$. Element je <em>rekord</em> ako je strogo veći od svih elemenata prije njega. Izračunaj $\sum (-1)^{len}$ po svim podnizovima (ne nužno uzastopnim) s točno $k$ rekorda, gdje je $len$ duljina podniza, modulo $998244353$.</p>
<h3>Ulaz</h3>
<p>$n$, $k$ ($1 \le k \le n \le 10^6$) i permutacija $p_1, \dots, p_n$.</p>
<h3>Izlaz</h3>
<p>Traženi zbroj.</p>
<h3>Primjer</h3>
<p>Za $p = (4, 1, 2, 5, 3)$ i $k = 2$ odgovor je $3$. Za identitetu duljine $7$ i $k = 3$ odgovor je $-\binom{7}{3} = -35 \equiv 998244318$.</p>
''',
    'hints': [
        r'''<p>Promotri susjedne elemente $x, y$ s $x > y$. U podnizovima koji sadrže $x$, $y$ nikad nije rekord — uparivanje podnizova koji se razlikuju samo u prisutnosti $y$ poništava doprinos.</p>''',
        r'''<p>Nakon uklanjanja svih takvih $x$ ostaje rastući niz: element ostaje ako i samo ako je manji od svega desno od sebe. U njemu su svi elementi rekordi — traže se podnizovi duljine točno $k$.</p>''',
    ],
    'coach': [
        ('Što se dogodi s brojem rekorda nekog podniza ako u njega dodamo, ili iz njega izbacimo, element $y$ koji u permutaciji stoji odmah iza većeg elementa $x$?', r'''<p>Ništa — pod uvjetom da podniz sadrži $x$. Sam $y$ nije rekord jer je $x$ ispred njega i veći. Elementi ispred $y$ ne vide ga uopće, a za svaki element $z$ iza $y$ prefiksni maksimum sadrži $x > y$, pa dodavanje $y$ ne mijenja je li $z$ rekord. Dakle podnizovi koji sadrže $x$ dolaze u parovima (bez $y$, s $y$) s istim brojem rekorda i suprotnom parnošću duljine: doprinos svakog para zbroju $\sum(-1)^{len}$ je nula. To je klasična <em>involucija koja mijenja predznak</em>.</p>'''),
        ('Zašto smijemo iz permutacije izbaciti cijeli element $x$, a ne samo podnizove koji sadrže $x$ i $y$?', r'''<p>Podijelimo sve podnizove na one koji sadrže $x$ i one koji ga ne sadrže. Prva skupina daje ukupno $0$ po prethodnom argumentu. Druga skupina su točno podnizovi permutacije $p \setminus \{x\}$, a broj rekorda podniza ovisi samo o njegovim elementima i njihovu redoslijedu — ne o tome što je izbačeno iz okoline. Zato je traženi zbroj za $p$ jednak zbroju za $p$ bez $x$: skratili smo niz za jedan element bez promjene odgovora, i postupak možemo ponavljati.</p>'''),
        ('Koji elementi prežive ponavljanje tog postupka i ovisi li rezultat o redoslijedu izbacivanja?', r'''<p>Element $x$ može biti izbačen samo ako iza njega postoji manji element (inače nikad ne bi bio lijevi član pada). Obratno, ako iza $x$ postoji manji element, uzmemo prvi takav $y$; svi elementi između su veći od $y$, pa se, izbacujući redom onaj neposredno ispred $y$, dođe do trenutka kad su $x$ i $y$ susjedni i $x$ nestaje. Izbacivanje elemenata nikad ne stvara nove manje elemente desno od nekoga, pa element koji je manji od svega desno od sebe (<em>sufiksni minimum</em>) preživi u svakom redoslijedu. Konačan niz su, neovisno o redoslijedu, točno sufiksni minimumi — rastući niz duljine $m$.</p>'''),
        ('Kako izgleda zbroj na rastućem nizu od $m$ elemenata?', r'''<p>U rastućem nizu svaki element svakog podniza veći je od svih prethodnih, pa podniz duljine $\ell$ ima točno $\ell$ rekorda. Podnizovi s točno $k$ rekorda su podnizovi duljine $k$, ima ih $\binom{m}{k}$ i svaki pridonosi $(-1)^k$. Odgovor je $(-1)^k\binom{m}{k}$, uz $0$ kad je $k > m$. Za računanje trebaju samo sufiksni minimumi (jedan prolaz zdesna) i binomni koeficijent modulo prost broj.</p>'''),
    ],
    'tips': [
        r'''Zbroj s predznakom $\sum (-1)^{|S|}$ po podskupovima gotovo uvijek pada uparivanjem: nađi <em>involuciju koja mijenja predznak</em> (podskup $\leftrightarrow$ podskup s jednim elementom više/manje) koja čuva promatranu statistiku; sve što se ne uparuje su fiksne točke, i samo njih treba prebrojati.''',
        r'''Kad tvrdiš „element se smije izbaciti bez promjene odgovora”, provjeri obje klase odvojeno: podskupovi koji ga sadrže (moraju dati $0$) i podskupovi koji ga ne sadrže (moraju biti točno podskupovi manje instance).''',
        r'''Ako postupak „izbacuj dok možeš” završava neovisno o redoslijedu, opiši konačno stanje izravno (ovdje sufiksni minimumi) i računaj ga u jednom prolazu, umjesto da simuliraš izbacivanja.''',
        r'''Binomni koeficijenti modulo prost broj: predračunaj faktorijele i inverzne faktorijele u $O(n)$, vrati $0$ za $k>m$ i normaliziraj negativne vrijednosti izrazom <code>(x % MOD + MOD) % MOD</code>.''',
    ],
    'solution': r'''
<p>Promotrimo dva susjedna elementa $x$ i $y$ takva da je $x > y$. Uzmimo sve podnizove koji sadrže $x$; u njima $y$ nije rekord. Podijelimo li te podnizove u parove koji se razlikuju samo u $y$, u svakom paru podnizovi imaju isti broj rekorda, ali različitu parnost duljine. Svaki par stoga doprinosi $0$, pa element $x$ možemo potpuno izbaciti iz permutacije, a odgovor se neće promijeniti.</p>
<p>Ponavljamo to dok možemo. Na kraju dobivamo rastući niz; element ostaje u nizu ako i samo ako je manji od svega desno od sebe. U takvom nizu svaki podniz ima sve elemente kao rekorde, pa nas zanimaju podnizovi od $k$ elemenata. Odgovor je $\binom{m}{k} (-1)^k$, gdje je $m$ broj preostalih elemenata.</p>
''',
    'detailed': r'''
<h3>1. Postavka i oznake</h3>
<p>Za podniz $S$ permutacije $p$ (bilo koji neprazan podskup pozicija, u izvornom redoslijedu) označimo s $\mathrm{rec}(S)$ broj rekorda — elemenata strogo većih od svih elemenata podniza ispred njih — i s $|S|$ njegovu duljinu. Tražimo
$$F(p,k)=\sum_{S:\ \mathrm{rec}(S)=k}(-1)^{|S|} \pmod{998244353}.$$
Broj podnizova je $2^n-1$, pa direktno nabrajanje otpada; treba pronaći strukturu koja većinu članova poništi.</p>

<h3>2. Ključno opažanje: susjedni pad poništava sve što ga sadrži</h3>
<p>Neka su $x=p_i$ i $y=p_{i+1}$ susjedni elementi s $x>y$. Promotrimo bilo koji podniz $S$ koji sadrži $x$, ali ne $y$, i njegovog para $S'=S\cup\{y\}$. Tvrdimo $\mathrm{rec}(S)=\mathrm{rec}(S')$.</p>
<ul>
<li>Sam $y$ u $S'$ nije rekord: element $x$ je u $S'$ ispred njega (odmah ispred, jer su susjedni u $p$ i ništa između ne postoji) i $x>y$.</li>
<li>Elementi ispred $y$ imaju u $S$ i $S'$ isti prefiks, pa im se status ne mijenja.</li>
<li>Za element $z$ iza $y$ prefiksni maksimum u $S'$ je $\max(\text{prefiksni maksimum u }S,\ y)$. No taj prefiks sadrži $x>y$, pa je maksimum isti kao u $S$. Status $z$ se ne mijenja.</li>
</ul>
<p>Duljine $S$ i $S'$ razlikuju se za $1$, pa je $(-1)^{|S|}+(-1)^{|S'|}=0$. Preslikavanje $S\leftrightarrow S'$ je bijekcija (involucija) na skupu podnizova koji sadrže $x$, čuva broj rekorda i mijenja predznak. Zato je <strong>ukupni doprinos svih podnizova koji sadrže $x$ jednak nuli</strong>, za svaki $k$.</p>

<h3>3. Redukcija: izbacivanje $x$ ne mijenja odgovor</h3>
<p>Podnizovi koji ne sadrže $x$ točno su podnizovi niza $p'$ dobivenog brisanjem $x$ iz $p$, a broj rekorda podniza ovisi samo o njegovim vlastitim elementima. Slijedi
$$F(p,k)=\underbrace{\sum_{S\ni x}(-1)^{|S|}[\mathrm{rec}(S)=k]}_{=0}+\sum_{S\not\ni x}(-1)^{|S|}[\mathrm{rec}(S)=k]=F(p',k).$$
Postupak ponavljamo dok u nizu postoji susjedni pad $p_i>p_{i+1}$. Završava jer se niz svaki put skrati, a završno stanje je rastući niz.</p>

<h3>4. Što ostaje: sufiksni minimumi, neovisno o redoslijedu</h3>
<p><strong>Tvrdnja.</strong> Bez obzira na to koji se pad izabere u kojem koraku, konačni niz čine točno oni elementi $p_i$ koji su manji od svih elemenata desno od sebe (sufiksni minimumi).</p>
<p><em>Sufiksni minimum preživi.</em> Da bi $x$ bio izbačen, mora u nekom trenutku biti neposredno ispred manjeg elementa; taj je manji element bio desno od $x$ i u izvornoj permutaciji (brisanje ne mijenja relativni redoslijed). Sufiksni minimum nema manjih elemenata desno, pa nikad nije lijevi član pada.</p>
<p><em>Ostali nestaju.</em> Neka $x$ nije sufiksni minimum i neka je $y$ prvi element desno od $x$ manji od $x$. Svi elementi strogo između $x$ i $y$ veći su od $x>y$, pa dok ih ima, element neposredno ispred $y$ čini pad s $y$ i može biti izbačen; kada ih više nema, $x$ i $y$ su susjedni i $x$ je izbačen. U bilo kojem redoslijedu izbacivanja, dok se u nizu nalazi bilo koji element koji nije sufiksni minimum, postoji pad (rastući niz je upravo niz u kojem su svi elementi sufiksni minimumi), pa proces ne može stati prije nego nestanu svi takvi elementi. Stoga je završni niz jednoznačan.</p>
<p>Neka je $m$ broj sufiksnih minimuma. Računamo ga jednim prolazom zdesna: pamtimo dosadašnji minimum $\mu$ (početno $+\infty$) i za svaki $p_i$ provjerimo $p_i\lt \mu$, pa ažuriramo $\mu$. Zadnji element uvijek je sufiksni minimum, pa je $m\ge1$.</p>

<h3>5. Formula na rastućem nizu</h3>
<p>U rastućem nizu $q_1\lt q_2\lt \dots\lt q_m$ svaki je element svakog podniza veći od svih elemenata ispred sebe, pa je $\mathrm{rec}(S)=|S|$. Podnizova s točno $k$ rekorda ima $\binom{m}{k}$ i svaki ima predznak $(-1)^k$. Konačno
$$F(p,k)=(-1)^k\binom{m}{k},\qquad \text{uz }F=0\text{ za }k>m.$$</p>

<h3>6. Algoritam</h3>
<ol>
<li>Pročitaj $n$, $k$ i permutaciju.</li>
<li>Prođi zdesna nalijevo i prebroji sufiksne minimume: $m$.</li>
<li>Ako je $k>m$, ispiši $0$.</li>
<li>Inače izračunaj $\binom{m}{k}\bmod P$ preko faktorijela i inverznih faktorijela (Fermatov mali teorem, $P$ je prost) i ispiši $\binom{m}{k}$ ako je $k$ paran, a $P-\binom{m}{k}$ ako je neparan (i ako je binom različit od $0$; za $\binom{m}{k}=0$ nema što negirati).</li>
</ol>

<h3>7. Složenost</h3>
<p>Jedan prolaz po permutaciji i predračun faktorijela do $n$: $O(n)$ vremena i $O(n)$ memorije (faktorijeli) — za $n=10^6$ trenutno. Bez predračuna, jedan binom može se izračunati i u $O(k)$ množenja s jednim modularnim inverzom na kraju.</p>

<h3>8. Rubni slučajevi i zamke</h3>
<ul>
<li>$k>m$: odgovor $0$ (npr. permutacija koja pada, $m=1$, $k=2$).</li>
<li>Negativan rezultat: $(-1)^k\binom mk$ za neparan $k$ ispisujemo kao $P-\binom mk$, ne kao negativan broj.</li>
<li>Rastuća permutacija: svi su elementi sufiksni minimumi, $m=n$.</li>
<li>Brzo čitanje ulaza: $10^6$ brojeva, koristi <code>scanf</code> ili ubrzani <code>cin</code>.</li>
<li>Ne treba dva puta koristiti definiciju „rekord = veći od svih prije” i „preživljava = manji od svih poslije”; lako ih je zamijeniti. Sufiksni minimumi su elementi manji od svega <em>desno</em>.</li>
</ul>

<h3>9. Provjera na primjeru</h3>
<p>$p=(4,1,2,5,3)$, $k=2$. Zdesna: $3$ je minimum ($\mu=3$), $5$ nije, $2<3$ jest ($\mu=2$), $1<2$ jest ($\mu=1$), $4$ nije. Dakle $m=3$ i odgovor $(-1)^2\binom32=3$, kao u primjeru. Za identitetu duljine $7$ i $k=3$: $m=7$, odgovor $-\binom73=-35\equiv 998244318$.</p>
''',
    'verified': r'''uzorci 3/3; 300 slučajnih permutacija ($n\le 12$, svi $k$) protiv brute forcea koji prolazi svih $2^n$ podnizova i broji rekorde; 3 velika testa s $n=10^6$ (najviše $0.06$ s).''',
},
# ---------------------------------------------------------------- D
{
    'letter': 'D', 'title': 'XOR Determinant', 'title_hr': 'XOR determinanta', 'slug': 'D_xor_determinant',
    'tl': '1 s', 'ml': '512 MiB',
    'statement': r'''
<p>Dani su nizovi $b$ i $c$ duljine $n$ nenegativnih cijelih brojeva. Matrica $A$ dimenzija $n \times n$ zadana je s $A_{ij} = b_i \oplus c_j$. Izračunaj $\det A$ modulo $998244353$.</p>
<h3>Ulaz</h3>
<p>$t$ ($1 \le t \le 1000$) testnih primjera; u svakom $n$ ($1 \le n \le 5000$), zatim $b_1..b_n$ i $c_1..c_n$ ($0 \le b_i, c_i < 2^{60}$). Zbroj svih $n$ ne prelazi $10^4$.</p>
<h3>Izlaz</h3>
<p>Determinanta za svaki testni primjer.</p>
<h3>Primjer</h3>
<p>Za $b = (2, 5)$, $c = (4, 1)$: $A = \begin{pmatrix} 6 & 3 \\ 1 & 4 \end{pmatrix}$, $\det A = 21$.</p>
''',
    'hints': [
        r'''<p>Rastavi $A$ po bitovima: $A = \sum_k 2^k A^{(k)}$, gdje je $A^{(k)}$ $01$-matrica $k$-tih bitova. Koliko različitih redaka može imati $A^{(k)}$?</p>''',
        r'''<p>Svaki redak $A^{(k)}$ je ili $c^{(k)}$ ili njegov komplement $\mathbf{1} - c^{(k)}$. Dakle svaki redak $A$ je linearna kombinacija vektora $c^{(0)}, \dots, c^{(59)}$ i $\mathbf{1}$ — rang je najviše $61$.</p>''',
    ],
    'coach': [
        (r'Kako izgleda matrica $A_{ij}=b_i\oplus c_j$ ako promatramo samo jedan bit, recimo $k$-ti?', r'''<p>Označimo $k$-te bitove s $\beta_i=\lfloor b_i/2^k\rfloor \bmod 2$ i $\gamma_j=\lfloor c_j/2^k\rfloor\bmod 2$. Matrica $k$-tih bitova $A^{(k)}_{ij}=\beta_i\oplus\gamma_j$ ima vrlo jednostavne retke: ako je $\beta_i=0$, $i$-ti redak je vektor $\gamma=(\gamma_1,\dots,\gamma_n)$; ako je $\beta_i=1$, redak je $\mathbf 1-\gamma$, gdje je $\mathbf 1$ vektor jedinica. Svaki redak $A^{(k)}$ leži dakle u linearnom potprostoru razapetom s dva vektora, $\gamma^{(k)}$ i $\mathbf 1$ — i to nad racionalnim brojevima, ne samo modulo $2$, jer smo $\oplus$ zapisali kao običnu razliku.</p>'''),
        ('Zašto rastav po bitovima govori nešto o rangu cijele matrice, a ne samo o matricama pojedinih bitova?', r'''<p>Jer je cijela matrica <em>obična</em> (ne XOR) linearna kombinacija bit-matrica: $A=\sum_{k=0}^{59}2^k A^{(k)}$, budući da je $b_i\oplus c_j=\sum_k 2^k(\beta^{(k)}_i\oplus\gamma^{(k)}_j)$. Stoga je $i$-ti redak $A$ jednak $\sum_k 2^k\bigl(\beta_i^{(k)}\mathbf 1+(1-2\beta_i^{(k)})\gamma^{(k)}\bigr)$ — linearna kombinacija $61$ fiksnih vektora $\gamma^{(0)},\dots,\gamma^{(59)},\mathbf 1$ koji ne ovise o $i$. Svi reci leže u potprostoru dimenzije najviše $61$, pa je $\operatorname{rang}A\le 61$.</p>'''),
        ('Što iz ograničenog ranga slijedi za determinantu kad je $n>61$, i zašto to vrijedi i modulo prostog broja?', r'''<p>Ako je $n>61$, redaka je više od dimenzije potprostora u kojem leže, pa su linearno zavisni nad $\mathbb Q$ i $\det A=0$ kao <em>cijeli broj</em>. Ostatak nule modulo bilo kojeg broja je nula, pa je odgovor $0$ bez ikakva računanja. (Isto se vidi i izravno nad $\mathbb F_p$: koeficijenti $2^k$ i $\pm1$ su cijeli brojevi, pa reci ostaju u potprostoru dimenzije $\le61$ i nad $\mathbb F_p$.)</p>'''),
        (r'Kako izračunati determinantu za $n\le 61$ kad su elementi do $2^{60}$?', r'''<p>Svaki element najprije svedemo modulo $p=998244353$ (XOR računamo u 64-bitnoj aritmetici — vrijednosti su $<2^{60}$, pa nema prelijevanja — i tek onda uzmemo ostatak), a zatim provedemo Gaussovu eliminaciju nad $\mathbb F_p$: za svaki stupac nađemo redak s nenultim pivotom, zamijenimo retke (svaka zamjena mijenja predznak determinante), pomnožimo inverzom pivota (Fermatov mali teorem) i poništimo elemente ispod. Determinanta je umnožak pivota s pripadnim predznakom, ili $0$ ako pivota nema. Trošak $O(n^3)\le 61^3$ po testu, a zbog $\sum n\le 10^4$ takvih je testova najviše $\approx 164$.</p>'''),
    ],
    'tips': [
        r'''Kad je matrica zadana formulom $A_{ij}=f(b_i,c_j)$, prvo pitanje je <em>rang</em>: ako se $f$ može zapisati kao $\sum_{t=1}^{r}u_t(b_i)v_t(c_j)$ s malim $r$, rang je $\le r$ i determinanta je $0$ za $n>r$. Bitovni rastav XOR-a, AND-a, OR-a i sl. daje $r=O(\text{broj bitova})$.''',
        r'''Bitovne operacije na cijelim brojevima su <em>obične</em> linearne kombinacije po bitovima: $x=\sum_k 2^k x^{(k)}$. Argumente o rangu i linearnoj zavisnosti tako prenosiš s $\{0,1\}$-matrica na prave brojeve.''',
        r'''Determinanta modulo prost broj: Gaussova eliminacija s modularnim inverzom pivota; prati predznak pri zamjeni redaka, elemente svedi modulo $p$ prije računa i množi u 64-bitnom tipu.''',
        r'''Zadaci s $\sum n\le 10^4$, ali pojedinačnim $n\le5000$ često skrivaju „prag”: za velike $n$ odgovor je trivijalan, a teški dio treba raditi samo do neke konstante.''',
    ],
    'solution': r'''
<p>Promotrimo binarni zapis svakog elementa $A$; on kaže kako element zapisati kao zbroj potencija dvojke. Neka je $A_{ij} = \sum_{k=0}^{K-1} 2^k A^{(k)}_{ij}$; tako definiramo $K$ $01$-matrica $A^{(k)}$ s $A = \sum_k 2^k A^{(k)}$.</p>
<p>Ali svaka $A^{(k)}$ određena je samo $k$-tim bitovima $b$ i $c$, a svaki joj je redak ili $c^{(k)}$ ili $c^{(k)} \oplus \mathbf{1}_n = \mathbf{1}_n - c^{(k)}$. To znači da se svaki redak $A$ može zapisati kao linearna kombinacija $c^{(0)}, c^{(1)}, \dots, c^{(K-1)}$ i $\mathbf{1}_n$. Stoga je $\operatorname{rank}(A) \le K + 1$, pa za $n > K + 1$ vrijedi $\det A = 0$. Inače determinantu računamo trivijalno u $O(n^3)$.</p>
''',
    'detailed': r'''
<h3>1. Što je sumnjivo u postavci</h3>
<p>Determinanta matrice $5000\times5000$ u $O(n^3)$ nije izračunljiva u jednoj sekundi, a ograničenje $\sum n\le10^4$ ipak dopušta jedan test s $n=5000$. To sugerira da za velike $n$ odgovor mora biti „besplatan”. Jedini prirodan razlog da determinanta velike matrice bude očito $0$ je mali rang, pa ispitujemo rang matrice $A_{ij}=b_i\oplus c_j$.</p>

<h3>2. Rastav po bitovima</h3>
<p>Za $0\le k<60$ označimo $k$-ti bit brojeva s $\beta^{(k)}_i=\lfloor b_i/2^k\rfloor\bmod2$ i $\gamma^{(k)}_j=\lfloor c_j/2^k\rfloor\bmod2$. Kako XOR djeluje bit po bit i nema prijenosa,
$$A_{ij}=b_i\oplus c_j=\sum_{k=0}^{59}2^k\bigl(\beta^{(k)}_i\oplus\gamma^{(k)}_j\bigr).$$
Ovo je obična suma cijelih brojeva — bitovi su međusobno nezavisni, pa se XOR dviju znamenki pretvara u pravu znamenku rezultata. Zapišimo XOR dvaju bitova bez XOR-a: za $\beta,\gamma\in\{0,1\}$ vrijedi $\beta\oplus\gamma=\beta+\gamma-2\beta\gamma=\beta+(1-2\beta)\gamma$. Uvrštavanjem,
$$A_{ij}=\sum_{k=0}^{59}2^k\Bigl(\beta^{(k)}_i\cdot 1+(1-2\beta^{(k)}_i)\,\gamma^{(k)}_j\Bigr).$$</p>

<h3>3. Reci leže u potprostoru dimenzije $\le 61$</h3>
<p>Fiksirajmo redak $i$ i gledajmo ga kao vektor po $j$. Gornja formula kaže
$$A_{i,\cdot}=\Bigl(\sum_k 2^k\beta^{(k)}_i\Bigr)\mathbf 1+\sum_{k=0}^{59}2^k(1-2\beta^{(k)}_i)\,\gamma^{(k)},$$
gdje je $\mathbf 1=(1,\dots,1)$ i $\gamma^{(k)}=(\gamma^{(k)}_1,\dots,\gamma^{(k)}_n)$. Vektori $\mathbf1,\gamma^{(0)},\dots,\gamma^{(59)}$ <strong>ne ovise o $i$</strong>; o retku ovise samo koeficijenti (prvi je upravo $b_i$, ostali su $\pm2^k$). Dakle svaki redak leži u potprostoru $V=\operatorname{span}\{\mathbf 1,\gamma^{(0)},\dots,\gamma^{(59)}\}$ dimenzije najviše $61$, pa je $\operatorname{rang}A\le 61$.</p>
<p>Argument vrijedi nad $\mathbb Q$ (koeficijenti su cijeli brojevi), a isto tako nad $\mathbb F_p$ za bilo koji prost $p$: ista jednakost redaka vrijedi nakon redukcije modulo $p$, jer smo koristili samo zbrajanje i množenje cijelih brojeva.</p>

<h3>4. Posljedica za determinantu</h3>
<p>Ako je $n>61$, imamo $n$ vektora u prostoru dimenzije $\le61$, pa su linearno zavisni: neki je redak linearna kombinacija ostalih, a determinanta matrice sa zavisnim recima je $0$. To je $0$ kao cijeli broj, dakle i $0\bmod 998244353$. <strong>Za $n\ge62$ odgovor je $0$ bez računanja.</strong> (Granica $61$ ne mora biti dostignuta — za male brojeve $\gamma^{(k)}$ su nul-vektori za visoke bitove — ali nam treba samo gornja ograda.)</p>

<h3>5. Mali $n$: Gaussova eliminacija nad $\mathbb F_p$</h3>
<p>Za $n\le61$ računamo determinantu izravno:</p>
<ol>
<li>Popunimo $M_{ij}=(b_i\oplus c_j)\bmod p$. XOR računamo u <code>unsigned long long</code> (operandi su $<2^{60}$, rezultat također), a zatim uzmemo ostatak.</li>
<li>Za stupac $c=0,1,\dots,n-1$: nađemo redak $r\ge c$ s $M_{rc}\ne0$. Ako ga nema, determinanta je $0$. Ako je $r\ne c$, zamijenimo retke i pomnožimo tekući predznak s $-1$.</li>
<li>Pomnožimo akumulirani rezultat s $M_{cc}$, izračunamo $\text{inv}=M_{cc}^{\,p-2}\bmod p$ (Fermatov mali teorem) i za svaki redak $r>c$ oduzmemo $M_{rc}\cdot\text{inv}$ puta redak $c$, čime stupac $c$ ispod dijagonale postaje $0$. Oduzimanje višekratnika retka ne mijenja determinantu.</li>
<li>Na kraju je $\det=\text{predznak}\cdot\prod_c M_{cc}\bmod p$; negativan rezultat normaliziramo u $[0,p)$.</li>
</ol>
<p>Zašto je to točno: elementarne operacije redaka mijenjaju determinantu na poznat način (zamjena redaka: predznak; dodavanje višekratnika: bez promjene), a determinanta gornjotrokutaste matrice je umnožak dijagonale. Sve vrijedi u svakom polju, pa i u $\mathbb F_p$, a determinanta cjelobrojne matrice modulo $p$ jednaka je determinanti matrice ostataka nad $\mathbb F_p$ jer je determinanta polinom s cjelobrojnim koeficijentima u elementima.</p>

<h3>6. Složenost</h3>
<p>Za $n\ge62$: $O(n)$ (samo čitanje). Za $n\le61$: $O(n^3)\le 61^3\approx2.3\cdot10^5$ operacija plus $n$ modularnih potenciranja; kako je $\sum n\le10^4$, testova s $n\le61$ koji zahtijevaju eliminaciju ima najviše $10^4$, ali ukupno $\sum n^3\le 61^2\sum n\approx3.7\cdot10^7$ — trenutno. Memorija $O(n^2)$ za $n\le61$, inače samo nizovi $b$ i $c$.</p>

<h3>7. Rubni slučajevi i zamke</h3>
<ul>
<li>$n=1$: $\det=(b_1\oplus c_1)\bmod p$ — eliminacija to pokriva, ali provjeri da petlja radi za $n=1$.</li>
<li>Vrijednosti do $2^{60}-1$ ne stanu u 32 bita; čitaj ih u 64-bitni tip (<code>%llu</code> ili <code>long long</code>). XOR prije redukcije, ne poslije: $(b\bmod p)\oplus(c\bmod p)\ne(b\oplus c)\bmod p$.</li>
<li>Množenje dvaju ostataka ($\lt p<2^{30}$) stane u 64-bitni tip; ne množi tri faktora bez međuredukcije.</li>
<li>Predznak: broj zamjena redaka može biti neparan — lako se zaboravi.</li>
<li>Kod $n\ge62$ ulaz treba svejedno pročitati do kraja jer slijedi sljedeći test.</li>
</ul>

<h3>8. Primjer</h3>
<p>$b=(2,5)$, $c=(4,1)$: $A=\begin{pmatrix}2\oplus4&2\oplus1\\5\oplus4&5\oplus1\end{pmatrix}=\begin{pmatrix}6&3\\1&4\end{pmatrix}$, $\det=24-3=21$. Rastav iz odjeljka 3 za prvi redak: $b_1=2$ pa je $\beta^{(1)}_1=1$, ostali bitovi $0$; $\gamma^{(0)}=(0,1)$, $\gamma^{(1)}=(0,0)$, $\gamma^{(2)}=(1,0)$. Redak je $2\cdot\mathbf1+1\cdot\gamma^{(0)}+(-2)\gamma^{(1)}+4\gamma^{(2)}=(2,2)+(0,1)+(0,0)+(4,0)=(6,3)$ — točno.</p>
''',
    'verified': r'''uzorak 1/1 (tri službena primjera u jednoj datoteci); 300 slučajnih testova (matrice $n\le6$ s $1$–$60$-bitnim vrijednostima te rubni slučajevi $n\in[58,64]$) protiv Python brute forcea (Leibnizova formula za $n\le6$, cjelobrojni Bareissov algoritam inače); 3 velika testa ($n=5000$ plus 81 test s $n=61$, $\sum n\approx10^4$), najviše $0.01$ s.''',
},
# ---------------------------------------------------------------- E
{
    'letter': 'E', 'title': 'Egor Has a Problem', 'title_hr': 'Egor ima problem', 'slug': 'E_egor_has_a_problem',
    'tl': '1 s', 'ml': '512 MiB',
    'statement': r'''
<p>Egor je zadao: za strogo rastući niz $a$ od $n$ pozitivnih cijelih brojeva nađi indekse $i < j < p < q$ takve da je $a_i \cdot a_q = a_j \cdot a_p$. No njegov checker, da izbjegne overflow, provjerava uvjet <code>a[q] / a[p] == a[j] / a[i]</code> u cjelobrojnoj (long long) aritmetici — dakle uspoređuje <em>cjelobrojne kvocijente</em>.</p>
<p>Ispiši <code>YES</code> i četiri indeksa koje će checker prihvatiti, ili <code>NO</code> ako takvi ne postoje.</p>
<h3>Ulaz</h3>
<p>$n$ ($4 \le n \le 5 \cdot 10^5$) i $a_1 < a_2 < \dots < a_n \le 10^{18}$.</p>
<h3>Izlaz</h3>
<p><code>YES</code> i indeksi $i, j, p, q$, ili <code>NO</code>.</p>
<h3>Primjer</h3>
<p>Za $a = (2, 6, 11, 21, 47, 120)$ odgovor je YES $1\ 3\ 4\ 6$ ($\lfloor 120/21 \rfloor = 5 = \lfloor 11/2 \rfloor$).</p>
''',
    'hints': [
        r'''<p>Dijeljenje je cjelobrojno — traži se jednakost $\lfloor a_q / a_p \rfloor = \lfloor a_j / a_i \rfloor$, što je puno slabiji uvjet od jednakosti umnožaka.</p>''',
        r'''<p>Ako susjedni omjeri $a_{t+1} / a_t$ često imaju cjelobrojni kvocijent $\ge 2$, niz raste barem eksponencijalno i brzo premaši $10^{18}$. Dakle kod dovoljno velikog $n$ sigurno postoje dva disjunktna susjedna para s kvocijentom $1$.</p>''',
    ],
    'coach': [
        ('Što checker zapravo provjerava — jednakost omjera $a_j/a_i=a_q/a_p$ ili nešto slabije?', r'''<p>Nešto puno slabije. Checker je pisan u cjelobrojnoj aritmetici, pa uspoređuje <em>cjelobrojne kvocijente</em> $\lfloor a_j/a_i\rfloor$ i $\lfloor a_q/a_p\rfloor$. Matematički bi tražena jednakost $a_ia_q=a_ja_p$ za slučajne velike brojeve gotovo nikad ne vrijedila, no s podnim dijeljenjem su, primjerice, <em>svi</em> parovi s $a_i\lt a_j<2a_i$ jednaki: kvocijent im je $1$. Zadatak se time pretvara iz teorije brojeva u zadatak o „malim skokovima” u rastućem nizu.</p>'''),
        (r'Koliko susjednih parova rastućeg niza može imati kvocijent $\ge2$ ako su svi članovi $\le10^{18}$?', r'''<p>Najviše $59$. Ako je $\lfloor a_{t+1}/a_t\rfloor\ge2$, tada je $a_{t+1}\ge2a_t$ — vrijednost se barem udvostruči. Krenemo li od $a_1\ge1$, nakon $d$ udvostručenja vrijednost je $\ge2^d$, a $2^{60}>10^{18}$, pa je $d\le59$. Preostalih barem $n-1-59=n-60$ susjednih parova ima kvocijent točno $1$ (jer je niz strogo rastući, kvocijent je $\ge1$).</p>'''),
        ('Zašto su nam potrebna dva <em>disjunktna</em> susjedna para i od kojeg su $n$ zajamčena?', r'''<p>Traže se indeksi $i\lt j\lt p\lt q$, pa parovi $(i,j)=(t,t+1)$ i $(p,q)=(t',t'+1)$ ne smiju dijeliti indeks ni se preklapati: treba $t'\ge t+2$. Dva susjedna para s kvocijentom $1$ mogu biti u sukobu samo ako su im početni indeksi na udaljenosti $1$; među bilo koja <em>tri</em> takva para s početnim indeksima $t_1\lt t_2\lt t_3$ vrijedi $t_3\ge t_1+2$, pa su prvi i treći disjunktni. Dakle dovoljno je $n-60\ge3$, tj. $n\ge63$: tada odgovor sigurno postoji i nađemo ga jednim prolazom.</p>'''),
        ('Što raditi za manje $n$, i zašto je to dovoljno brzo i točno?', r'''<p>Za $n\le62$ jednostavno probamo sve četvorke $i\lt j\lt p\lt q$: ima ih $\binom{62}{4}=557\,845$, svaka košta dva cjelobrojna dijeljenja, što je zanemarivo. Iscrpna provjera je očito točna i pokriva i slučajeve u kojima odgovor ne postoji (npr. nizovi koji brzo eksponencijalno rastu), gdje moramo ispisati <code>NO</code>.</p>'''),
    ],
    'tips': [
        r'''Kad zadatak spominje checker ili „ono što se uspoređuje”, pročitaj <em>točno</em> kako se uspoređuje: cjelobrojno dijeljenje, pomični zarez, prelijevanje i sl. mogu uvjet koji izgleda nemoguće pretvoriti u trivijalan.''',
        r'''Strogo rastući niz ograničen odozgo s $C$ ima najviše $\log_2 C$ „velikih skokova” (udvostručenja); sve ostalo su mali koraci. Taj princip golublja rupa često daje konstantnu granicu $\approx 60$ za $C\le10^{18}$.''',
        r'''Prag $T$: ako strukturni argument jamči odgovor za $n\ge T$, a $T$ je konstanta, za $n\lt T$ smije se raditi brute force u $O(T^4)$ — hibrid je i brz i očito točan.''',
        r'''Za parove (ili četvorke) susjednih indeksa disjunktnost je uvjet o razmaku početaka; među tri kandidata uvijek su dva disjunktna.''',
    ],
    'solution': r'''
<p>Najprije treba uočiti da checker dijeli u tipu <code>long long</code>, pa rezultat zaokružuje prema dolje. Tada je jasno da s mnogo elemenata vrijednosti ne mogu svaki put udvostručiti, pa će postojati dva para s cjelobrojnim kvocijentom jednakim $1$. Preciznije, ako imamo barem $\log_2 C + 3$ elemenata, naći ćemo dva (disjunktna) para susjednih elemenata s kvocijentom $1$. U protivnom jednostavno probamo svih $\binom{n}{4}$ mogućnosti.</p>
''',
    'detailed': r'''
<h3>1. Što se doista traži</h3>
<p>Zadatak traži $i\lt j\lt p\lt q$ takve da checker prihvati $a_j/a_i=a_q/a_p$, a checker dijeli cjelobrojno. Uvjet je stoga
$$\Bigl\lfloor \frac{a_j}{a_i}\Bigr\rfloor=\Bigl\lfloor\frac{a_q}{a_p}\Bigr\rfloor .$$
Egzaktna jednakost omjera bila bi teška i za velike slučajne brojeve gotovo uvijek nemoguća; podno dijeljenje uvjet čini vrlo blagim. Posebno, za svaka dva para s $a_i\lt a_j<2a_i$ i $a_p\lt a_q<2a_p$ oba su kvocijenta jednaka $1$ i četvorka je valjana. Pitanje postaje: postoje li u nizu dva disjunktna „mala skoka”?</p>

<h3>2. Ograničen broj velikih skokova</h3>
<p>Promotrimo susjedne parove $(a_t,a_{t+1})$, $t=1,\dots,n-1$. Niz je strogo rastući, pa je $\lfloor a_{t+1}/a_t\rfloor\ge1$. Par nazovimo <em>velikim</em> ako je taj kvocijent $\ge2$, tj. $a_{t+1}\ge2a_t$, a <em>malim</em> ako je kvocijent točno $1$.</p>
<p><strong>Lema.</strong> Velikih parova ima najviše $59$.</p>
<p><em>Dokaz.</em> Svaki veliki par barem udvostručuje vrijednost, a mali je par ne smanjuje ($a_{t+1}>a_t$). Ako je velikih parova $d$, onda je $a_n\ge 2^d a_1\ge2^d$. Kako je $a_n\le10^{18}<2^{60}\approx1.15\cdot10^{18}$, slijedi $d\le59$. $\square$</p>
<p>Posljedica: malih parova ima barem $(n-1)-59=n-60$.</p>

<h3>3. Dva disjunktna mala para</h3>
<p>Ako uzmemo $(i,j)=(t,t+1)$ i $(p,q)=(t',t'+1)$ za dva mala para, uvjet $i\lt j\lt p\lt q$ znači $t+1\lt t'$, tj. $t'\ge t+2$. Dva mala para s početnim indeksima na razmaku $1$ (npr. $(3,4)$ i $(4,5)$) nisu upotrebljiva zajedno. Ali među <em>tri</em> mala para s početnim indeksima $t_1\lt t_2\lt t_3$ sigurno je $t_3\ge t_1+2$, pa su prvi i treći disjunktni.</p>
<p>Dakle, ako je $n-60\ge3$, tj. <strong>$n\ge63$</strong>, odgovor uvijek postoji: uzmemo prvi mali par $(t_1,t_1+1)$, a zatim prvi mali par s početkom $\ge t_1+2$. Oba kvocijenta su $1$ i checker ih prihvaća.</p>

<h3>4. Mali $n$: iscrpna provjera</h3>
<p>Za $n\le62$ argument ne jamči rješenje (niz može imati mnogo velikih skokova, npr. potencije od $2$ pomiješane s nečim), i odgovor može biti <code>NO</code>. Zato jednostavno prolazimo sve četvorke $i\lt j\lt p\lt q$ i za svaku usporedimo $\lfloor a_j/a_i\rfloor$ i $\lfloor a_q/a_p\rfloor$. Broj četvorki je $\binom{62}{4}=557\,845$, dakle oko milijun cjelobrojnih dijeljenja — trenutno. Ako nijedna ne prolazi, ispišemo <code>NO</code>.</p>
<p>Napomena: uvjet možemo bez gubitka općenitosti provjeravati baš tako; ne pokušavamo pametovati o omjerima — iscrpna provjera je točna po definiciji, a i pokriva slučaj u kojem su valjane samo četvorke s kvocijentom $\ge2$ (npr. $a=(1,2,5,10)$: $\lfloor2/1\rfloor=\lfloor10/5\rfloor=2$).</p>

<h3>5. Algoritam</h3>
<ol>
<li>Pročitaj $n$ i niz.</li>
<li>Ako je $n\ge63$: prođi $t=1,\dots,n-1$ i nađi prvi indeks $t_1$ s $a_{t_1+1}<2a_{t_1}$; nastavi od $t_1+2$ i nađi prvi $t_2$ s istim svojstvom. Ispiši <code>YES</code> i $t_1,\ t_1+1,\ t_2,\ t_2+1$. (Po lemi oba postoje.)</li>
<li>Inače četverostrukom petljom provjeri sve četvorke; ispiši prvu valjanu ili <code>NO</code>.</li>
</ol>
<p>Kako je više odgovora valjano, sudac koristi checker; naš ispis ne mora biti jednak službenom.</p>

<h3>6. Složenost</h3>
<p>$O(n)$ za $n\ge63$ i $O(\min(n,62)^4)$ inače — ukupno $O(n)$ uz konstantu od oko $10^6$ operacija. Memorija $O(n)$.</p>

<h3>7. Rubni slučajevi i zamke</h3>
<ul>
<li>Vrijednosti do $10^{18}$ traže 64-bitni tip; test $a_{t+1}<2a_t$ radi u <code>long long</code> jer je $2\cdot10^{18}<9.2\cdot10^{18}$, a još je sigurnije usporediti $a_{t+1}/a_t=1$ dijeljenjem.</li>
<li>Nikad ne množi $a_ia_q$ i $a_ja_p$ — to prelijeva ($10^{36}$) i, važnije, nije ono što checker provjerava.</li>
<li>$n=4$ je najmanji dopušteni $n$: tada postoji samo jedna četvorka, $(1,2,3,4)$.</li>
<li>Indeksi se ispisuju 1-indeksirani i u rastućem poretku $i\lt j\lt p\lt q$.</li>
<li>Ne pretpostavljaj da je prag točno $63$ „napamet”: izvedi ga iz $2^{60}>10^{18}$ i potrebe za tri mala para; s granicom $10^{18}$ i $a_1\ge1$ prag $63$ je dovoljan.</li>
</ul>

<h3>8. Primjer</h3>
<p>$a=(2,6,11,21,47,120)$, $n=6$: iscrpna provjera. Četvorka $(1,2,3,4)$ ne prolazi ($\lfloor6/2\rfloor=3\ne\lfloor21/11\rfloor=1$), a $(1,3,4,6)$ prolazi: $\lfloor11/2\rfloor=5=\lfloor120/21\rfloor$ — kao u službenom primjeru (u ovom je primjeru to ujedno jedina valjana četvorka, pa se iscrpna provjera i službeni ispis podudaraju). Za $a=(1,2,6,30,210)$ svi su kvocijenti susjednih parova veliki i različiti ($2,3,5,7$), a ni ostale četvorke ne prolaze, pa je odgovor <code>NO</code>. Za $a=(1,2,4,8)$ jedini par disjunktnih susjednih parova $(1,2),(3,4)$ daje $2=2$ — <code>YES 1 2 3 4</code>.</p>
''',
    'verified': r'''uzorci 4/4 (checker); 300 slučajnih testova (rastući nizovi $n\le9$ iz raznih raspodjela — gusti, eksponencijalni, do $10^{18}$ — te svaki peti test s $n\in[63,66]$ i $55$ udvostručenja) — <code>check.py</code> provjerava valjanost četvorke u cjelobrojnoj aritmetici i uspoređuje YES/NO s iscrpnim brute forceom; 3 velika testa ($n=5\cdot10^5$), najviše $0.04$ s.''',
},
# ---------------------------------------------------------------- F
{
    'letter': 'F', 'title': 'Is This FFT?', 'title_hr': 'Je li ovo FFT?', 'slug': 'F_is_this_fft',
    'tl': '15 s', 'ml': '998244353 B',
    'statement': r'''
<p>Slučajno stablo na $n$ vrhova generira se ovako: uzmi svih $n(n-1)/2$ bridova u uniformno slučajnom poretku, kreni od praznog grafa i dodaj brid ako spaja dvije različite komponente. Za sve $n$ od $2$ do $N$ izračunaj vjerojatnost da tako nastane <em>bambus</em> (stablo u kojem su svi stupnjevi $\le 2$), modulo zadanog prostog $P$ s $P \equiv 1 \pmod{2^{16}}$.</p>
<p>Napomena iz teksta zadatka: modul je zadan ulazom, pa autori preporučuju Barrettovu redukciju za brže množenje; ne jamče da je zadatak rješiv bez brzog množenja.</p>
<h3>Ulaz</h3>
<p>$N$ i $P$ ($2 \le N \le 250$, $2 < P < 10^9$, $P$ prost, $P \bmod 2^{16} = 1$).</p>
<h3>Izlaz</h3>
<p>$N - 1$ brojeva — odgovori za $n = 2, \dots, N$.</p>
''',
    'hints': [],
    'coach': [],
    'solution': None,
},
# ---------------------------------------------------------------- G
{
    'letter': 'G', 'title': 'MIT', 'title_hr': 'MIT', 'slug': 'G_mit',
    'tl': '5 s', 'ml': '998244353 B',
    'statement': r'''
<p>Dano je težinsko stablo $T$ s $n$ vrhova; $d_{uv}$ je zbroj težina na jedinstvenom putu od $u$ do $v$. Promotri potpuni težinski graf $G$ s težinom brida $(u, v)$ jednakom $d_{uv}$. Za svaki $k$ od $1$ do $\lfloor n/2 \rfloor$ izračunaj najveću moguću težinu sparivanja veličine $k$ u $G$ (skup od $k$ bridova bez zajedničkih vrhova).</p>
<h3>Ulaz</h3>
<p>$n$ ($2 \le n \le 10^5$) i $n - 1$ bridova $u_i\ v_i\ w_i$ ($1 \le w_i \le 10^8$).</p>
<h3>Izlaz</h3>
<p>$\lfloor n/2 \rfloor$ brojeva.</p>
<h3>Primjer</h3>
<p>Za stablo s bridovima $(1,3,99), (2,3,82), (3,4,4), (4,5,43), (5,6,5), (4,7,3)$ odgovor je $181\ 280\ 287$.</p>
''',
    'hints': [],
    'coach': [],
    'solution': None,
},
# ---------------------------------------------------------------- H
{
    'letter': 'H', 'title': 'Exact Subsequences', 'title_hr': 'Točan broj podnizova', 'slug': 'H_exact_subsequences',
    'tl': '1 s', 'ml': '512 MiB',
    'statement': r'''
<p>Promotri sve binarne nizove koji imaju točno $n$ različitih nepraznih podnizova (različitih po sadržaju). Poredaj ih leksikografski i nađi $k$-ti.</p>
<h3>Ulaz</h3>
<p>$t$ ($1 \le t \le 100$) testnih primjera, svaki s $n$ i $k$ ($1 \le n, k \le 10^9$).</p>
<h3>Izlaz</h3>
<p>Za svaki primjer: $-1$ ako takvih nizova ima manje od $k$; inače niz opisan brojem blokova $m$ i prvim znakom $c$ u prvom retku, te duljinama blokova $L_1, \dots, L_m$ u drugom.</p>
<h3>Primjer</h3>
<p>Za $n = 3$ nizovi su redom $000, 01, 10, 111$ ($k = 5$ daje $-1$).</p>
''',
    'hints': [
        r'''<p>Broji različite podnizove gradeći niz s desna na lijevo: neka je $x$ broj različitih podnizova koji ne počinju s $1$ (uključujući prazan), a $y$ broj onih koji ne počinju s $0$. Što se dogodi s $(x, y)$ kad ispred niza dodamo blok od $t$ nula?</p>''',
        r'''<p>Dodavanje $t$ nula ispred: $(x, y) \to (x + ty, y)$. Obrnuto — to je Euklidov algoritam! Niz je valjan ako i samo ako Euklidov postupak na $(x, y)$ završi u $(1, 1)$, tj. $\gcd(x, y) = 1$, uz $x + y = n + 2$. Broj takvih nizova je $\varphi(n + 2)$.</p>''',
        r'''<p>Ako je $x_1 > x_2$ i $y_1 < y_2$ (uz isti zbroj), niz $S(x_1, y_1)$ je leksikografski manji. Dakle $k$-ti niz odgovara $k$-tom broju $y$ iz $[1, n+1]$ koprostom s $n + 2$ — binarno pretraživanje + uključivanje–isključivanje po prostim faktorima.</p>''',
    ],
    'coach': [
        ('Kako se broj različitih podnizova mijenja kad nizu <em>ispred</em> dodamo jedan znak, i zašto je prirodno pratiti dva broja umjesto jednog?', r'''<p>Novi podnizovi koji počinju dodanim znakom $c$ su točno $c\cdot s$ za <em>svaki</em> različiti podniz $s$ starog niza (uključujući prazan), a svi ostali podnizovi koji počinju s $c$ već su bili te oblike. Zato je ukupan broj sam po sebi nedovoljan: trebamo znati koliko podnizova počinje s $0$, a koliko s $1$. Pratimo $x$ = broj različitih podnizova koji ne počinju s $1$ (počinju s $0$ ili su prazni) i $y$ = broj onih koji ne počinju s $0$. Dodavanje $0$ ispred: $(x,y)\to(x+y,y)$; dodavanje $1$: $(x,y)\to(x,x+y)$. Prazan niz je $(1,1)$, a nepraznih različitih podnizova ima $x+y-2$.</p>'''),
        ('Zašto je postupak unatrag Euklidov algoritam i što to govori o tome koji su parovi $(x,y)$ dostižni?', r'''<p>Nakon dodavanja $0$ vrijedi $x>y$, nakon dodavanja $1$ vrijedi $y>x$; za neprazan niz nikad nije $x=y$. Dakle veći od dva broja otkriva prvi znak, a njegovim oduzimanjem manjeg dobivamo par kraćeg niza: to je Euklidov algoritam oduzimanjem, koji čuva $\gcd$ i staje kad su brojevi jednaki. Par je dostižan iz $(1,1)$ točno kad postupak završi u $(1,1)$, tj. kad je $\gcd(x,y)=1$; niz je tada jednoznačno određen. Uz $x+y=n+2$ valjanih nizova ima točno $\varphi(n+2)$ (broj $y\in[1,n+1]$ koprostih s $n+2$).</p>'''),
        ('Kako usporediti leksikografski dva niza ako znamo samo njihove parove $(x,y)$?', r'''<p>Niz se iz para čita s početka: ako je $x>y$, prvi je znak $0$ i ostatak ima par $(x-y,y)$, inače je $1$ i ostatak ima par $(x,y-x)$. Indukcijom se dokaže: ako je $x_1\ge x_2$ i $y_1\le y_2$ (a parovi su različiti), onda je ili $S(x_2,y_2)$ prefiks od $S(x_1,y_1)$ ili je $S(x_1,y_1)$ na prvom različitom mjestu manji. Dva niza s istim $n$ ne mogu biti jedan drugome prefiks (dulji ima strogo više podnizova), pa je uz fiksni zbroj $x+y=n+2$ leksikografski poredak upravo <strong>rastući $y$</strong>. Tražimo dakle $k$-ti broj $y\in[1,n+1]$ koprost s $n+2$.</p>'''),
        ('Kako naći $k$-ti broj koprost s $N=n+2$ bez prolaska po svim brojevima do $10^9$?', r'''<p>Broj brojeva u $[1,v]$ koprostih s $N$ računa se uključivanjem–isključivanjem po skupovima različitih prostih djelitelja $N$: $\sum_{d\mid\mathrm{rad}(N)}\mu(d)\lfloor v/d\rfloor$. Broj do $10^9+2$ ima najviše $9$ različitih prostih faktora, dakle najviše $512$ pribrojnika. Funkcija $v\mapsto$ (broj koprostih do $v$) je neopadajuća, pa binarnim pretraživanjem nađemo najmanji $v$ s vrijednošću $\ge k$ — to je traženi $y$ — u $\approx30$ koraka. Ako je već ukupan broj $\varphi(N)\lt k$, odgovor je $-1$.</p>'''),
        (r'Kako iz para $(x,y)$ ispisati niz kad njegova duljina može biti $\approx10^9$?', r'''<p>Ispisujemo blokove: dok je $x>y$ dodajemo nule, a Euklidov korak s dijeljenjem daje cijeli blok odjednom — duljina bloka je $\lfloor x/y\rfloor$ (a $x-1$ kad je $y=1$), nakon čega $x\leftarrow x\bmod y$; simetrično za jedinice. Zbog $\gcd=1$ ostatak nikad nije $0$ prije kraja, pa se postupak zaustavi u $(1,1)$ nakon $O(\log n)$ blokova, koliko i traži izlazni format.</p>'''),
    ],
    'tips': [
        r'''Broj različitih podnizova računa se standardnom dinamikom „novi podnizovi s zadnjim (ili prvim) znakom $c$ = svi različiti podnizovi dosad”; ne zaboravi prazan podniz kao početno stanje i pazi kako se broji na kraju.''',
        r'''Rekurzije oblika $(x,y)\to(x+y,y)$ i $(x,y)\to(x,x+y)$ su Stern–Brocotovo/Calkin–Wilfovo stablo: unatrag ih vodi Euklidov algoritam, dostižni su točno koprosti parovi, a dijeljenje umjesto oduzimanja obrađuje cijeli blok jednakih poteza u jednom koraku.''',
        r'''„$k$-ti broj u $[1,M]$ koprost s $N$” = binarno pretraživanje po $v$ uz brojanje uključivanjem–isključivanjem; brojevi do $10^9$ imaju $\le9$ različitih prostih faktora, pa je $2^9$ pribrojnika zanemarivo.''',
        r'''Prije nego što povjeruješ tvrdnji o leksikografskom poretku, provjeri je li uopće moguće da je jedan kandidat prefiks drugoga — često baš to ruši ili spašava dokaz.''',
    ],
    'solution': r'''
<p>Razmotrimo kako bismo izračunali broj različitih podnizova binarnog niza zadanog u obliku iz izlaza. Recimo da prije skupine od $t$ nula imamo $x$ različitih podnizova koji ne završavaju s $1$ (završavaju s $0$ ili su prazni) i $y$ različitih podnizova koji ne završavaju s $0$. Lako se pokaže $x \le y$. Nakon dodavanja jedne nule broj različitih podnizova koji ne završavaju s $1$ postaje $x + y$; nakon dvije nule $x + 2y$; nakon $t$ nula $x + ty$.</p>
<p>Sada uočavamo da je taj proces unatrag Euklidov algoritam. Umjesto računanja broja podnizova slijeva nadesno možemo to raditi zdesna nalijevo; tada Euklidov algoritam ispisuje skupine slijeva nadesno.</p>
<p>Prazan niz ima $1$ (prazan) podniz, pa mu je par $(x, y) = (1, 1)$. Dakle na kraju Euklidova algoritma moramo doći do $(1, 1)$, što se događa ako i samo ako krećemo od para $(x, y)$ s $\gcd(x, y) = 1$. Na početku niz mora imati $n$ različitih nepraznih podnizova, pa je $x + y = n + 2$. Ta su dva uvjeta nužna i dovoljna. Vrijedi $\gcd(n+2, y) = \gcd(n + 2 - y, y) = \gcd(x, y) = 1$, pa je npr. broj takvih nizova $\varphi(n + 2)$. Još treba dobiti $k$-ti od njih.</p>
<p>Nazovimo niz dobiven Euklidovim algoritmom iz $(x, y)$ (uz $\gcd(x, y) = 1$) $S(x, y)$: $S(1, 1) = \varepsilon$; za $x > y$, $S(x, y) = \text{“0”} + S(x - y, y)$; za $x < y$, $S(x, y) = \text{“1”} + S(x, y - x)$.</p>
<p>Tvrdimo: ako je $x_1 > x_2$ i $y_1 < y_2$, onda je $S(x_1, y_1) < S(x_2, y_2)$. Dokaz indukcijom po $x_1 + x_2 + y_1 + y_2$: ako su prvi znakovi različiti, $S(x_1, y_1)$ počinje s $0$, a $S(x_2, y_2)$ s $1$. Inače oba počinju istim znakom, recimo $0$; tada je $S(x_1, y_1) = \text{“0”} + S(x_1 - y_1, y_1)$, $S(x_2, y_2) = \text{“0”} + S(x_2 - y_2, y_2)$, a $x_1 - y_1 > x_2 - y_2$, pa primjenjujemo pretpostavku na sufikse.</p>
<p>Budući da svi zanimljivi parovi imaju isti zbroj, dovoljno ih je sortirati po rastućem $y$. Time smo zadatak sveli na traženje $k$-tog broja koprostog s $n + 2$: faktoriziramo $n + 2$ (dovoljno je $O(\sqrt{n})$), binarno pretražujemo odgovor, a broj brojeva na prefiksu koprostih sa zadanim brojem računamo uključivanjem–isključivanjem po prostim djeliteljima.</p>
''',
    'detailed': r'''
<h3>1. Brojanje različitih podnizova s dva brojača</h3>
<p>Gradimo niz s desna na lijevo, tj. dodajemo znakove <em>ispred</em> postojećeg niza. Za niz $s$ označimo $x(s)$ = broj različitih podnizova koji <strong>ne počinju s $1$</strong> (dakle počinju s $0$ ili su prazni) i $y(s)$ = broj različitih podnizova koji ne počinju s $0$. Prazan podniz ubrojen je u oba, pa je broj različitih nepraznih podnizova $x+y-2$. Za prazan niz $(x,y)=(1,1)$.</p>
<p><strong>Lema 1.</strong> Ako ispred $s$ dodamo $0$, novi par je $(x+y,\,y)$; ako dodamo $1$, novi par je $(x,\,x+y)$.</p>
<p><em>Dokaz.</em> Neka je $s'=0s$. Podnizovi od $s'$ koji počinju s $1$ ne mogu koristiti dodanu nulu, pa su to točno podnizovi od $s$ koji počinju s $1$: $y$ se ne mijenja. Podnizovi od $s'$ koji počinju s $0$: svaki je oblika $0t$ gdje je $t$ neki podniz od $s$ (uzmemo li prvu odabranu nulu — dodanu ili neku iz $s$ — ostatak je podniz od $s$ iza nje, dakle podniz od $s$). Obratno, za svaki različiti podniz $t$ od $s$ (uključujući prazan) niz $0t$ je podniz od $s'$, a različiti $t$ daju različite $0t$. Takvih je $x+y-1$, plus prazan podniz: $x'=x+y$. Simetrično za $1$. $\square$</p>
<p>Za niz koji ima točno $n$ različitih nepraznih podnizova vrijedi, dakle, $x+y=n+2$.</p>

<h3>2. Unatrag: Euklidov algoritam i karakterizacija valjanih parova</h3>
<p>Nakon dodavanja $0$ vrijedi $x'=x+y>y=y'$, a nakon dodavanja $1$ vrijedi $y'>x'$. Neprazan niz zato nikad nema $x=y$, a veći od brojeva govori koji je prvi znak. Uklanjanjem prvog znaka par prelazi u $(x-y,y)$ odnosno $(x,y-x)$ — to je Euklidov algoritam oduzimanjem.</p>
<p><strong>Lema 2.</strong> Par $(x,y)$ pozitivnih brojeva je par nekog binarnog niza ako i samo ako je $\gcd(x,y)=1$; taj je niz tada jedinstven.</p>
<p><em>Dokaz.</em> Postupak oduzimanja čuva $\gcd$ i strogo smanjuje zbroj dok su brojevi različiti, pa završava u $(g,g)$ s $g=\gcd(x,y)$. Ako je par nastao iz niza, postupak rekonstruira niz znak po znak unatrag i mora završiti u paru praznog niza $(1,1)$, dakle $g=1$. Obratno, za $\gcd=1$ postupak završava u $(1,1)$ i svaki korak jednoznačno određuje znak, pa čitanjem tih znakova dobivamo niz s parom $(x,y)$ (po Lemi 1). Jedinstvenost slijedi iz determinističnosti koraka. $\square$</p>
<p><strong>Posljedica.</strong> Nizovi s točno $n$ različitih nepraznih podnizova u bijekciji su s brojevima $y\in[1,n+1]$ za koje je $\gcd(n+2-y,\,y)=\gcd(n+2,\,y)=1$. Ima ih $\varphi(n+2)$. Ako je $k>\varphi(n+2)$, odgovor je $-1$.</p>

<h3>3. Leksikografski poredak = poredak po $y$</h3>
<p>Označimo $S(x,y)$ niz s parom $(x,y)$. Iz odjeljka 2: $S(x,y)=0\,S(x-y,y)$ za $x>y$, $S(x,y)=1\,S(x,y-x)$ za $x\lt y$, $S(1,1)=\varepsilon$.</p>
<p><strong>Lema 3.</strong> Ako je $x_1\ge x_2$, $y_1\le y_2$ i $(x_1,y_1)\ne(x_2,y_2)$, onda je ili $S(x_2,y_2)$ pravi prefiks od $S(x_1,y_1)$, ili se nizovi razlikuju na nekom mjestu i na prvom takvom $S(x_1,y_1)$ ima $0$, a $S(x_2,y_2)$ ima $1$.</p>
<p><em>Dokaz</em> indukcijom po $x_1+y_1+x_2+y_2$. Ako je $(x_2,y_2)=(1,1)$, $S(x_2,y_2)$ je prazan niz — pravi prefiks. Inače, ako $S(x_2,y_2)$ počinje s $0$ ($x_2>y_2$), onda je $x_1\ge x_2>y_2\ge y_1$, pa i $S(x_1,y_1)$ počinje s $0$; ostatci imaju parove $(x_1-y_1,y_1)$ i $(x_2-y_2,y_2)$ koji opet zadovoljavaju pretpostavke ($x_1-y_1\ge x_2-y_2$, $y_1\le y_2$, različiti) i manji su, pa vrijedi indukcija. Ako $S(x_2,y_2)$ počinje s $1$ ($x_2\lt y_2$): ili $S(x_1,y_1)$ počinje s $0$ — tada je tvrdnja gotova na prvom mjestu — ili počinje s $1$ ($x_1\lt y_1$), a ostatci $(x_1,y_1-x_1)$ i $(x_2,y_2-x_2)$ zadovoljavaju pretpostavke i vrijedi indukcija. $\square$</p>
<p><strong>Lema 4.</strong> Dva različita niza s istim brojem $n$ različitih nepraznih podnizova nisu jedan drugome prefiks.</p>
<p><em>Dokaz.</em> Dodavanje znaka na kraj niza $s$ stvara novi podniz $s\,c$ dulji od svih dotadašnjih, pa se broj različitih podnizova strogo povećava; pravi prefiks ima strogo manje podnizova. $\square$</p>
<p>Za dva valjana niza s $x_1+y_1=x_2+y_2=n+2$ i $y_1\lt y_2$ vrijedi $x_1>x_2$, pa po Lemi 3 i Lemi 4 (prefiks je isključen) $S(x_1,y_1)$ je leksikografski manji. <strong>Poredak valjanih nizova je rastući poredak po $y$</strong>, i $k$-ti niz odgovara $k$-tom broju $y\in[1,n+1]$ koprostom s $N=n+2$.</p>
<p>Provjera na $n=3$, $N=5$: $y=1,2,3,4$ redom daju $S(4,1)=000$, $S(3,2)=0\,S(1,2)=01$, $S(2,3)=1\,S(2,1)=10$, $S(1,4)=111$ — točno redoslijed iz primjera.</p>

<h3>4. $k$-ti koprost broj: uključivanje–isključivanje i binarno pretraživanje</h3>
<p>Faktoriziramo $N$ probnim dijeljenjem do $\sqrt N\approx31\,623$ i dobijemo različite proste faktore $p_1,\dots,p_\omega$. Broj brojeva u $[1,v]$ koprostih s $N$ je
$$C(v)=\sum_{T\subseteq\{1..\omega\}}(-1)^{|T|}\Bigl\lfloor\frac{v}{\prod_{i\in T}p_i}\Bigr\rfloor,$$
jer uključivanje–isključivanje broji one koji nisu djeljivi ni s jednim $p_i$. Kako je $2\cdot3\cdot5\cdots23=223\,092\,870\le10^9+2<2\cdot3\cdots29$, vrijedi $\omega\le9$, dakle najviše $512$ pribrojnika. Ako je $C(N-1)=\varphi(N)\lt k$, ispišemo $-1$. Inače je $C$ neopadajuća, pa binarnim pretraživanjem po $v\in[1,N-1]$ nađemo najmanji $v$ s $C(v)\ge k$; to je $y$ (njemu je $C$ upravo porasla, dakle $\gcd(y,N)=1$), a $x=N-y$.</p>

<h3>5. Ispis u blokovima: Euklid s dijeljenjem</h3>
<p>Niz $S(x,y)$ može imati $\approx10^9$ znakova (npr. sve nule), zato ga ispisujemo kao blokove jednakih znakova. Dok je $x>y$, znakovi su nule; u koraku oduzimanja $x\leftarrow x-y$ ponavljamo dok ne postane $x\lt y$. Ako je $y=1$, nakon $x-1$ koraka stižemo u $(1,1)$: blok od $x-1$ nula i kraj. Ako je $y\ge2$, zbog $\gcd(x,y)=1$ nikad ne dobijemo $x=y$ ni $x=0$, pa je broj koraka točno $\lfloor x/y\rfloor$ i novi $x$ je $x\bmod y\in[1,y-1]$. Simetrično za jedinice. Svaki blok mijenja koji je broj veći, pa se blokovi nula i jedinica izmjenjuju; prvi znak je $0$ ako je $x>y$, inače $1$. Broj blokova je broj koraka Euklidova algoritma s dijeljenjem, $O(\log N)$, što odgovara izlaznom formatu ($m$, prvi znak, duljine).</p>

<h3>6. Složenost</h3>
<p>Po testu: faktorizacija $O(\sqrt N)$, binarno pretraživanje $O(2^\omega\log N)\le512\cdot31$, ispis $O(\log N)$. Za $t\le100$ ukupno oko $5\cdot10^6$ operacija. Memorija $O(\log N)$.</p>

<h3>7. Rubni slučajevi i zamke</h3>
<ul>
<li>$k>\varphi(n+2)$: ispiši $-1$ (npr. $n=3$, $k=5$).</li>
<li>$y=1$: sve nule, jedan blok duljine $n$ ($x=n+1$, $x-1=n$). $y=n+1$: sve jedinice. Slučaj $y=1$ odnosno $x=1$ treba obraditi posebno u Euklidu, jer bi $\lfloor x/1\rfloor=x$ dalo jedan znak previše.</li>
<li>$n=1$: $N=3$, $\varphi=2$, nizovi $0$ i $1$; $n=2$: $N=4$, $\varphi=2$, nizovi $00$ i $11$ (niz $01$ ima $3$ podniza).</li>
<li>Brojevi do $10^9+2$ i umnošci prostih djelitelja stanu u 64 bita bez problema; koristi <code>long long</code> da izbjegneš razmišljanje o granicama $2^{31}$.</li>
<li>Faktorizacija: dijeli $N$ do $\sqrt N$ i ne zaboravi preostali faktor $>1$ (velik prost broj).</li>
<li>U uključivanju–isključivanju predznak ovisi o parnosti veličine podskupa; $\varphi(N)$ dobiveno kao $C(N-1)$ je ujedno i provjera ispravnosti (može se usporediti s formulom $N\prod(1-1/p_i)$).</li>
</ul>

<h3>8. Primjer</h3>
<p>$n=3$, $k=2$: $N=5$, prosti faktori $\{5\}$, $C(v)=v-\lfloor v/5\rfloor$; $C(4)=4\ge2$, binarno pretraživanje daje $y=2$, $x=3$. Euklid: $(3,2)$, $x>y$, $y\ne1$: blok $\lfloor3/2\rfloor=1$ nula, $x=1$; $(1,2)$, $x\lt y$, $x=1$: blok $y-1=1$ jedinica; kraj. Ispis: <code>2 0</code> i <code>1 1</code>, tj. niz $01$ — kao u primjeru. Za $n=10^9$, $k=1$: $y=1$, jedan blok od $10^9$ nula.</p>
''',
    'verified': r'''uzorak 1/1 (osam službenih primjera u jednoj datoteci, uključujući $n=10^9$); 300 slučajnih testova ($n\le11$, $k\le n+3$) protiv Python brute forcea koji nabraja sve binarne nizove duljine do $n$, broji različite podnizove skupom, sortira valjane i $k$-ti zapisuje u blokovima; 3 velika testa ($t=100$, $n$ do $10^9$ s raznim faktorizacijama), najviše $0.00$ s.''',
},
# ---------------------------------------------------------------- I
{
    'letter': 'I', 'title': 'SPPPSPSS.', 'title_hr': 'SPPPSPSS.', 'slug': 'I_spppspss',
    'tl': '1 s', 'ml': '512 MiB',
    'statement': r'''
<p>Dana je permutacija $p$ duljine $n$. Želiš je sortirati uzlazno najmanjim brojem operacija; u $k$-toj operaciji odabireš prefiks duljine $k$ <em>ili</em> sufiks duljine $k$ i sortiraš ga uzlazno.</p>
<h3>Ulaz</h3>
<p>$n$ ($1 \le n \le 10^6$) i permutacija.</p>
<h3>Izlaz</h3>
<p>Niz znakova <code>P</code>/<code>S</code> duljine $m$ (najmanji broj operacija) i završna točka „<code>.</code>”.</p>
<h3>Primjer</h3>
<p>Za $p = (3, 2, 4, 1, 5, 6, 7, 9, 8)$ odgovor je <code>SSSP.</code></p>
''',
    'hints': [
        r'''<p>Sortiranje nikad ne šteti. Ako optimalno rješenje ima dvije uzastopne operacije istog tipa, prva je beskorisna (druga sortira nadskup) — zamijeni je drugim tipom. Zaključak: postoji optimalno rješenje s alternirajućim operacijama, dakle samo dva kandidata (počinje s P ili sa S).</p>''',
        r'''<p>Dok se sortirani prefiksi i sufiksi ne sijeku ($k \le n/2$), operacije su neovisne: stanje je „sortiran najveći prefiks i najveći sufiks, sredina netaknuta”. Možeš li u $O(1)$ (uz prefiksne maksimume i sufiksne minimume) provjeriti je li takvo stanje sortirano?</p>''',
        r'''<p>Nakon što se prefiks i sufiks preklope, niz je spoj dvaju rastućih dijelova; održavaj ga kao [točan prefiks][sortirani dio 1][sortirani dio 2][točan sufiks] i svaku operaciju izvedi pomicanjem granica — ukupno $O(n)$.</p>''',
    ],
    'coach': [
        ('Može li sortiranje nekog segmenta ikad „pokvariti” niz za operacije koje slijede?', r'''<p>Ne, i to se može precizno dokazati. Permutacija je sortirana točno kad je za svaki prag $t$ 0/1-niz $[p_i>t]$ sortiran, a sortiranje segmenta permutacije sortira taj segment u svakom pragovnom nizu. Za 0/1-nizove uvedimo uređaj „$a\preceq b$ ako svaki prefiks od $b$ ima najviše toliko jedinica koliko isti prefiks od $a$” (jedinice su u $b$ više desno). Sortiranje segmenta (1) podiže niz u tom uređaju i (2) čuva uređaj, jer se broj jedinica u prefiksu unutar segmenta računa kao $\max(c_{l-1},\,c_r-(r-i))$, monotono po prefiksnim brojačima. Sortirani niz je maksimum, pa ako slijed operacija sortira $a$, sortira i svaki $a'\succeq a$ — posebno $a$ s bilo kojim sortiranim segmentom.</p>'''),
        ('Zašto onda postoji optimalno rješenje u kojem se P i S strogo izmjenjuju?', r'''<p>Ako su operacije $k$ i $k+1$ obje P, sortiranje prefiksa $k$ pa prefiksa $k+1$ daje isto što i samo sortiranje prefiksa $k+1$ — operacija $k$ je beskorisna. Zamijenimo je sa S$_k$: to samo sortira neki segment, pa po prethodnom argumentu ostatak niza operacija i dalje sortira. Zamjenom na najdesnijem takvom paru svi parovi desno ostaju različiti, a najdesniji „loš” par pomiče se ulijevo; indukcijom dobijemo izmjenični niz iste duljine. Kandidati su samo <code>PSPS…</code> i <code>SPSP…</code>, za oba nađemo najmanji $m$ i uzmemo bolji.</p>'''),
        ('Što je stanje niza dok se sortirani prefiksi i sufiksi još ne sijeku, i kako ga provjeriti u $O(1)$?', r'''<p>Nakon $m$ koraka izmjeničnog niza sortirani su prefiks duljine $a$ i sufiks duljine $b$ s $\{a,b\}=\{m,m-1\}$; disjunktni su dok je $a+b=2m-1\le n$, tj. $m\le\lfloor(n+1)/2\rfloor$. Operacije na disjunktnim pozicijama komutiraju, a sortiranje ugniježđenih prefiksa jednako je sortiranju najvećeg, pa je stanje: „sortiraj $p[1..a]$ i $p[n-b+1..n]$, sredinu ne diraj”. To je sortirano točno kad je $\max p[1..a]=a$, $\min p[n-b+1..n]=n-b+1$ i u sredini je $p_i=i$ — tri $O(1)$ provjere uz prefiksne maksimume, sufiksne minimume i prefiksni brojač „krivih” pozicija.</p>'''),
        ('Kako izgleda niz nakon prvog preklapanja i zašto svaku daljnju operaciju možemo izvesti samo pomicanjem granica?', r'''<p>Prva preklapajuća operacija sortira prefiks (ili sufiks) koji seže u već sortirani sufiks (prefiks); rezultat je spoj dva rastuća bloka. Zapišimo ga kao $[1..L][A][B][n-R+1..n]$, gdje su $A$ i $B$ rastući, $\min B=L+1$ i $\max A=n-R$. Operacija P duljine $k$ obuhvaća $[1..L]$, cijeli $A$ i prvih $j$ elemenata $B$; sve vrijednosti manje od $v$ (prvog elementa $B$ koji ostaje) tvore točno skup $\{1,\dots,v-1\}$ i nakon sortiranja sjednu na svoja mjesta, pa točan prefiks postane $[1..v-1]$, $A$ izgubi elemente $\lt v$, a $B$ prvih $j$. Isto simetrično za S. Granice se pomiču samo u jednom smjeru, pa je ukupno $O(n)$.</p>'''),
        ('Kako spojiti sve u jedno rješenje i koja je složenost?', r'''<p>Za svaki od dva izmjenična niza: faza 1 prolazi $m=0,1,\dots,\lfloor(n+1)/2\rfloor$ s provjerom u $O(1)$; ako nije gotovo, izračunamo stanje nakon prvog preklapanja u $O(n)$ i nastavimo fazom 2 s pomicanjem granica, najviše do $k=n$ (operacija duljine $n$ sve sortira). Ukupno $O(n)$ vremena i memorije, što je nužno za $n=10^6$; ispis je niz P/S duljine $m$ i točka.</p>'''),
    ],
    'tips': [
        r'''„Operacija nikad ne šteti” dokazuje se pronalaskom parcijalnog uređaja koji operacija čuva i u kojem cilj postaje maksimum; za sortiranje su to pragovni 0/1-nizovi i prefiksni brojači jedinica (dominacija).''',
        r'''Argument zamjene (exchange argument) na <em>najdesnijem</em> lošem paru daje čistu indukciju — pokazuje da se skup kandidata smanjuje na konstantan broj, pa se svaki kandidat samo provjeri.''',
        r'''Sortiranje ugniježđenih segmenata jednako je sortiranju najvećeg; operacije na disjunktnim indeksima komutiraju. Ova dva pravila često sažimaju dugu povijest operacija u jedno stanje s $O(1)$ parametara.''',
        r'''Kad je struktura „nekoliko rastućih blokova s granicama koje se pomiču samo u jednom smjeru”, amortizirana analiza odmah daje $O(n)$ — traži takvu reprezentaciju umjesto simulacije.''',
    ],
    'solution': r'''
<p>Nikad nije loše sortirati neki podsegment.</p>
<p>Uzmimo optimalan odgovor. Ako ima dvije uzastopne operacije istog tipa, prva je beskorisna, pa je možemo zamijeniti drugim tipom bez pogoršanja odgovora. Ako to primijenimo na najdesniji takav par, sigurno ćemo najdesniji par pomaknuti ulijevo (ili sve takve parove ukloniti), pa možemo eliminirati sve takve parove. To dokazuje da postoji optimalan odgovor s alternirajućim operacijama; takva su niza samo dva — probamo oba.</p>
<p>Sortiranje implementiramo u $O(n)$ (counting sort). Dok se prefiksi i sufiksi koje sortiramo ne sijeku, ne utječu jedni na druge, pa sortiramo samo najveći prefiks i najveći sufiks. Ako je odgovor najviše $n/2$, možemo binarno pretraživati odgovor s provjerom u $O(n)$.</p>
<p>Ako je odgovor veći od $n/2$, izvedemo prva dva sortiranja koja se sijeku; nakon toga je niz uvijek spoj dvaju rastućih nizova. Štoviše, trenutni niz održavamo u obliku <code>[točan prefiks] [sortirani segment iz prve polovice] [sortirani segment iz druge polovice] [točan sufiks]</code>. Pri sortiranju prefiksa odrezat ćemo prefiks trećeg dijela i spojiti ga u drugi, ali te vrijednosti zapravo postaju točne, pa produljuju točan prefiks. Operacija se dakle svodi na rezanje prefiksa drugog i trećeg dijela; isto vrijedi za sortiranje sufiksa i rezanje sufiksa dvaju segmenata. Obje se operacije implementiraju pomicanjem lijeve ili desne granice segmenata, a svakim pomicanjem veličina segmenta pada za jedan — ukupno $O(n)$ operacija.</p>
<p>Drugi način za drugi dio: nakon $n/2$ ostaje najviše $\sqrt{n}$ operacija, koje možemo implementirati u $O(n \sqrt{n})$; ovisno o konstanti to može proći.</p>
''',
    'detailed': r'''
<h3>1. Sortiranje segmenta nikad ne šteti</h3>
<p>Za permutaciju $p$ i prag $t\in\{0,\dots,n\}$ definiramo 0/1-niz $p^{(t)}_i=[p_i>t]$. Permutacija je sortirana točno kad su svi $p^{(t)}$ sortirani (nule pa jedinice), a sortiranje segmenta $[l,r]$ permutacije sortira segment $[l,r]$ svakog $p^{(t)}$ (poredak vrijednosti čuva se pragom). Zato je dovoljno promatrati 0/1-nizove.</p>
<p>Za 0/1-nizove $a,b$ iste duljine i istog broja jedinica pišimo $a\preceq b$ ako za svaki prefiks $i$ vrijedi $c_a(i)\ge c_b(i)$, gdje je $c(i)$ broj jedinica u prvih $i$ pozicija („u $b$ su jedinice više desno”). Sortirani niz je najveći element tog uređaja.</p>
<p><strong>Lema 1.</strong> Neka $\sigma$ označava sortiranje segmenta $[l,r]$. Tada (i) $a\preceq\sigma(a)$ i (ii) $a\preceq b\Rightarrow\sigma(a)\preceq\sigma(b)$.</p>
<p><em>Dokaz.</em> Za $i\lt l$ i $i\ge r$ prefiksni brojači se ne mijenjaju (multiskup segmenta je isti). Za $l\le i\lt r$ nakon sortiranja segment ima $c(r)-c(l-1)$ jedinica gurnutih na kraj, pa je $c_{\sigma(a)}(i)=\max\bigl(c_a(l-1),\,c_a(r)-(r-i)\bigr)$. To je $\le c_a(i)$ (jer je $c_a(i)\ge c_a(l-1)$ i $c_a(i)\ge c_a(r)-(r-i)$), što daje (i); a kao maksimum neopadajućih funkcija brojača $c_a$ monotono je po $\preceq$, što daje (ii). $\square$</p>
<p><strong>Posljedica.</strong> Ako slijed operacija $\tau$ (kompozicija sortiranja segmenata) sortira $a$, sortira i svaki $a'\succeq a$: po (ii) je $\tau(a)\preceq\tau(a')$, a $\tau(a)$ je maksimum. Posebno, ako ostatak operacija sortira $A$, sortira i $A$ s prethodno sortiranim bilo kojim segmentom.</p>

<h3>2. Postoji optimalno rješenje s izmjeničnim operacijama</h3>
<p>Uzmimo optimalan niz od $m$ operacija i neka su operacije $k$ i $k+1$ obje P (za S simetrično). Sortiranje prefiksa duljine $k$ pa duljine $k+1$ daje isto što i samo sortiranje prefiksa $k+1$: multiskup prvih $k+1$ elemenata isti je, ostatak netaknut. Dakle ostatak operacija $k+1,\dots,m$ sortira stanje $A$ prije operacije $k$ i bez nje. Zamijenimo operaciju $k$ sa S$_k$: stanje postaje $A$ sa sortiranim sufiksom, pa po Posljedici ostatak i dalje sortira. Primijenimo to na <em>najdesniji</em> par istog tipa: parovi desno od njega ostaju različiti, par $(k,k+1)$ postaje različit, a jedini novi loš par može biti $(k-1,k)$ — dakle najdesniji loš par pomiče se strogo ulijevo i postupak stane. Dobili smo optimalan niz iste duljine u kojem se P i S izmjenjuju: <code>PSPS…</code> ili <code>SPSP…</code>. Za oba kandidata izračunamo najmanji broj koraka nakon kojega je niz sortiran i ispišemo bolji (uz $m=0$ ako je permutacija već sortirana; tada ispisujemo samo točku).</p>

<h3>3. Faza 1: dok se prefiks i sufiks ne sijeku</h3>
<p>Nakon $m$ koraka izmjeničnog niza sortirani su prefiks duljine $a$ i sufiks duljine $b$, $\{a,b\}=\{m,m-1\}$. Dok je $a+b=2m-1\le n$, tj. $m\le M_1=\lfloor(n+1)/2\rfloor$, svi P-prefiksi i S-sufiksi su disjunktni. Operacije na disjunktnim pozicijama komutiraju, a sortiranje ugniježđenih prefiksa jednako je sortiranju najvećeg (isti multiskup, sortiran). Stanje je stoga: $p[1..a]$ sortiran, $p[n-b+1..n]$ sortiran, sredina originalna.</p>
<p>To je stanje sortirano točno kad prefiks sadrži skup $\{1,\dots,a\}$, sufiks skup $\{n-b+1,\dots,n\}$ i u sredini je $p_i=i$. U permutaciji $a$ različitih vrijednosti $\le a$ znači točno $\{1..a\}$, pa je prvi uvjet $\max p[1..a]=a$; slično $\min p[n-b+1..n]=n-b+1$; treći provjeravamo prefiksnim brojačem pozicija s $p_i\ne i$. Tri provjere u $O(1)$ za svaki $m=0,1,\dots,M_1$; prvi uspjeh je odgovor kandidata.</p>

<h3>4. Faza 2: nakon preklapanja niz je spoj dva rastuća bloka</h3>
<p>Ako faza 1 ne završi, izgradimo stanje nakon $M_1$ koraka eksplicitno u $O(n)$ (obilježimo vrijednosti prefiksa/sufiksa i ispišemo ih uzlazno). Korak $k=M_1+1$ prvi se put preklapa: ako je P, sortira se prefiks $[1..k]$, a pozicije $k+1..n$ leže u već sortiranom sufiksu (jer je $k+1\ge n-M_1+1$), pa je niz spoj rastućeg bloka duljine $x=k$ i rastućeg bloka duljine $n-k$; ako je S, simetrično s $x=n-k$.</p>
<p>Zapišimo niz kao $[1..L]\,[A]\,[B]\,[n-R+1..n]$: točan prefiks, rastući ostatak prvog bloka, rastući ostatak drugog bloka, točan sufiks. Ako je jedan od $A,B$ prazan, drugi je rastući niz na skupu $\{L+1..n-R\}$ i sve je sortirano. Inače vrijedi <strong>$\min B=L+1$</strong> (vrijednost $L+1$ nije na poziciji $L+1$, gdje je $\min A$, pa je u $B$) i simetrično $\max A=n-R$.</p>
<p><strong>Operacija P duljine $k$.</strong> Ako je $k\le L+|A|$, prefiks je već sortiran — ništa se ne mijenja. Inače prefiks obuhvaća $[1..L]$, $A$ i prvih $j=k-L-|A|$ elemenata $B$. Ako je $j\ge|B|$, sortira se sve osim točnog sufiksa i niz je gotov. Inače neka je $v$ prvi element $B$ koji ostaje izvan prefiksa. Sve vrijednosti manje od $v$ nalaze se u $[1..L]$, u $A$ ili među prvih $j$ elemenata $B$ (ostatak $B$ i sufiks su $\ge v$), pa je $\{1,\dots,v-1\}$ upravo skup tih vrijednosti; nakon sortiranja prefiksa one zauzmu pozicije $1..v-1$. Ostatak sortiranog prefiksa čine elementi $A$ veći od $v$ (u $A$ nema $v$), i dalje rastući. Novo stanje: $L\leftarrow v-1$, $A\leftarrow\{a\in A:a>v\}$, $B\leftarrow B$ bez prvih $j$ elemenata; invarijanta $\min B=L+1$ vrijedi jer je $\min B=v$. Operacija S simetrična je s ulogama zamijenjenima ($v$ = najveći element $A$ koji ostaje, $R\leftarrow n-v$).</p>
<p>Održavamo $A$ i $B$ kao podsegmente niza izgrađenog nakon prvog preklapanja: $A=\mathrm{arr}[lo_A..hi_A]$, $B=\mathrm{arr}[lo_B..hi_B]$. P pomiče $lo_B$ udesno za $j$ i $lo_A$ udesno dok je $\mathrm{arr}[lo_A]\lt v$; S pomiče $hi_A$ ulijevo za $j$ i $hi_B$ ulijevo dok je $\mathrm{arr}[hi_B]>v$. Sve četiri granice miču se samo u jednom smjeru, pa je faza 2 ukupno $O(n)$. Nadalje, operacija duljine $n$ sortira sve, pa faza 2 sigurno završi do koraka $n$.</p>

<h3>5. Algoritam</h3>
<ol>
<li>Učitaj $p$; izračunaj prefiksne maksimume, sufiksne minimume i prefiksni brojač pozicija s $p_i\ne i$.</li>
<li>Za $c\in\{$počinje s P, počinje sa S$\}$: faza 1 za $m=0..M_1$ (O(1) provjera); ako nije gotovo, izgradi stanje nakon $M_1$, izvedi korak $M_1+1$ i dobiveni niz od dva bloka; odredi $L,R,A,B$; faza 2 s pomicanjem granica do prvog $k$ u kojem se sve sortira.</li>
<li>Uzmi $c$ s manjim $m$ (pri jednakosti bilo koji — sudac koristi checker jer optimalnih nizova može biti više) i ispiši $m$ znakova P/S i točku.</li>
</ol>

<h3>6. Složenost</h3>
<p>Predračun $O(n)$; faza 1 $O(n)$ provjera po $O(1)$; izgradnja stanja $O(n)$ (obilježavanje umjesto sortiranja); faza 2 amortizirano $O(n)$. Ukupno $O(n)$ vremena i $O(n)$ memorije za $n\le10^6$. Ulaz je velik, pa treba brzo čitanje (<code>scanf</code>/vlastiti čitač).</p>

<h3>7. Rubni slučajevi i zamke</h3>
<ul>
<li>Već sortirana permutacija (uključujući $n=1$): $m=0$, ispis je samo „<code>.</code>”.</li>
<li>Operacija duljine $1$ ne mijenja ništa, ali se broji; zato npr. za $p=(2,1)$ odgovor ima dvije operacije (<code>SP.</code> ili <code>PS.</code>).</li>
<li>Prag $M_1=\lfloor(n+1)/2\rfloor$: pri $m=M_1$ vrijedi $2M_1-1\le n$, pa se prefiks i sufiks još ne sijeku; korak $M_1+1$ uvijek se preklapa jer je $2M_1+1>n$.</li>
<li>Sufiks duljine $0$ u fazi 1 treba posebno tretirati ($\min$ praznog skupa).</li>
<li>U fazi 2 slučajevi $j\le0$ (operacija ne mijenja niz) i $j\ge|B|$ (kraj) moraju se provjeriti prije pristupa $\mathrm{arr}[lo_B+j]$.</li>
<li>Službeni izlaz ne mora biti izmjeničan (npr. <code>SSSP.</code>); naš je <code>SPSP.</code> — obje su optimalne i checker ih prihvaća.</li>
</ul>

<h3>8. Primjer (četvrti službeni primjer)</h3>
<p>$p=(2,9,5,7,10,6,3,1,8,4)$, $n=10$, $M_1=5$. Kandidat koji počinje sa S: faza 1 ne uspijeva ni za jedan $m\le5$ (npr. za $m=4$ prefiks $[2,9,5,7]$ ima maksimum $9\ne4$). Stanje nakon 5 koraka (prefiks 4 i sufiks 5 sortirani): $(2,5,7,9,10,\,1,3,4,6,8)$. Korak 6 je P: sortira se $[1..6]$ i niz je $(1,2,5,7,9,10\mid3,4,6,8)$ — dva rastuća bloka. Točan prefiks $L=2$, $R=0$, $A=(5,7,9,10)$, $B=(3,4,6,8)$. Korak 7 je S, duljina 7: sufiks obuhvaća $B$ i zadnja $j=7-4=3$ elementa $A$, tj. $7,9,10$; ostaje $v=5$; vrijednosti veće od $5$ su $6,7,8,9,10$ i sjedaju na kraj: $R=5$, $A=(5)$, $B=(3,4)$, niz $(1,2,5,3,4,6,7,8,9,10)$. Korak 8 je P, duljina 8: $j=8-(2+1)=5\ge|B|$, sve se sortira. Odgovor: 8 operacija, <code>SPSPSPSP.</code> (službeni <code>SPPPSPSS.</code> također ima 8). Kandidat koji počinje s P daje 9, pa se ne odabire.</p>
''',
    'verified': r'''uzorci 4/4 (checker: niz operacija mora sortirati permutaciju i biti jednako dug kao optimum iz brute forcea); 800 slučajnih permutacija $n\le11$ protiv Python brute forcea koji isprobava sve nizove P/S rastuće duljine; 3 velika testa ($n=10^6$: slučajna permutacija, obrnuta, gotovo sortirana i s izmiješanom sredinom), najviše $0.07$ s.''',
},
# ---------------------------------------------------------------- J
{
    'letter': 'J', 'title': 'Kth Lex Min Min Min Subpalindromes', 'title_hr': 'K-ti leksikografski najmanji s najmanje podpalindroma', 'slug': 'J_kth_lex_min_min_min_subpalindromes',
    'tl': '3 s', 'ml': '512 MiB',
    'statement': r'''
<p>Promotri sve nizove duljine $n$ s elementima iz $\{1, \dots, m\}$. Neka je $P$ najmanji mogući broj palindromnih uzastopnih podnizova (podsegmenata) u takvom nizu. Među nizovima koji imaju točno $P$ palindromnih podsegmenata nađi $k$-ti leksikografski najmanji, ili ispiši $-1$ ako ih je manje od $k$.</p>
<h3>Ulaz</h3>
<p>$n$, $m$, $k$ ($1 \le n, m \le 10^6$, $1 \le k \le 10^{18}$).</p>
<h3>Izlaz</h3>
<p>Traženi niz ili $-1$.</p>
<h3>Primjer</h3>
<p>Za $n = 3$, $m = 3$, $k = 3$ odgovor je $2\ 1\ 3$.</p>
''',
    'hints': [
        r'''<p>Svaki element je palindrom duljine $1$, pa je $P \ge n$. Kad se $P = n$ može postići? Treba izbjeći palindrome duljine $2$ ($aa$) i $3$ ($aba$) — dulji palindromi sadrže jedan od njih u sredini.</p>''',
        r'''<p>Za $m \ge 3$: svaki element različit od dva prethodna daje $m (m-1) (m-2)^{n-2}$ nizova s $P = n$, a $k$-ti se izravno rekonstruira. Za $m = 2$ napiši brute force za male $n$ i pogledaj što se događa za $n \ge 10$.</p>''',
    ],
    'coach': [
        ('Koja je donja granica za broj palindromnih podsegmenata i kad se ona dostiže?', r'''<p>Svaki od $n$ znakova sam je palindrom, pa je $P\ge n$. Palindrom duljine $\ge2$ ima u sredini palindrom duljine $2$ ($aa$) ili $3$ ($aba$) — skidanjem krajnjih znakova palindrom ostaje palindrom. Dakle $P=n$ vrijedi točno kad nema $a_i=a_{i+1}$ ni $a_i=a_{i+2}$, tj. kad se svaki element razlikuje od dva prethodna. To je ostvarivo čim je $m\ge3$.</p>'''),
        (r'Zašto se za $m\ge3$ $k$-ti optimalni niz čita kao broj u mješovitoj bazi?', r'''<p>Na prvoj poziciji ima $m$ dopuštenih vrijednosti, na drugoj $m-1$, a na svakoj sljedećoj točno $m-2$ (dva su zabranjena i međusobno različita) — <em>neovisno o tome što smo izabrali</em>. Zato svaka dopuštena vrijednost na poziciji $i$ nosi jednak broj nastavaka, $(m-2)^{n-1-i}$ (odnosno $(m-1)(m-2)^{n-2}$ za $i=0$), i leksikografski $k$-ti niz određujemo pohlepno: indeks izbora je $\lfloor k/\text{nastavaka}\rfloor$ među <em>sortiranim</em> dopuštenim vrijednostima. Ukupno ih je $m(m-1)(m-2)^{n-2}$; ako je to $\lt k$, odgovor je $-1$.</p>'''),
        (r'Kako izbjeći prelijevanje kad je $m(m-1)(m-2)^{n-2}$ astronomski velik, a $k\le10^{18}$?', r'''<p>Zanima nas samo usporedba s $k$, pa množimo „s kapom”: rezultat koji prijeđe $2\cdot10^{18}$ zamijenimo tom konstantom (množenje u <code>__int128</code> ili provjerom dijeljenjem). Kapa je apsorbirajuća, pa i potencije $(m-2)^j$ s kapom daju ispravne kvocijente $\lfloor k/\text{nastavaka}\rfloor$ — čim je broj nastavaka veći od preostalog $k$, kvocijent je $0$ bez obzira na točnu vrijednost.</p>'''),
        ('Što je drugačije kod $m=2$ i kako doći do pouzdane tvrdnje o „točno 12 nizova s periodom 6”?', r'''<p>S dva znaka ne možemo izbjeći i $aa$ i $aba$, pa je $P>n$. Za svaku unutarnju poziciju $i$ među $a_{i-1},a_i,a_{i+1}$ dva su jednaka, što daje palindrom duljine $2$ ili $3$ koji sadrži $i$; pažljivim dodjeljivanjem (uz popravak za uzorak $baab$) ta je dodjela injektivna, pa je $P\ge n+(n-2)=2n-2$. Brute force do $n=14$ pokazuje da se $2n-2$ dostiže točno kad niz ne sadrži nijedan od $10$ zabranjenih uzoraka duljine $\le6$; konačnom provjerom svih konteksta pokaže se da svaki takav uzorak „troši” dodatni palindrom, a nizovi duljine $10$ bez zabranjenih uzoraka su točno $12$ rotacija/komplemenata riječi $001011$, čije je produljenje bez zabranjenih uzoraka jedinstveno. Za $n<10$ optimalne nizove jednostavno nabrojimo ($2^n\le512$).</p>'''),
    ],
    'tips': [
        r'''Svaki palindrom duljine $\ge2$ sadrži centrirani palindrom duljine $2$ ili $3$; zato se „nema palindroma duljih od $1$” svodi na lokalne uvjete $a_i\ne a_{i+1}$, $a_i\ne a_{i+2}$.''',
        r'''Ako je broj dopuštenih izbora na svakoj poziciji konstantan bez obzira na prošlost, $k$-ti leksikografski objekt čita se kao zapis broja $k-1$ u mješovitoj bazi — bez ikakve dinamike.''',
        r'''Brojeve koji smiju biti veći od $10^{18}$ drži „s kapom”: kapa je apsorbirajuća za množenje i ne kvari usporedbe s $k$ ni kvocijente $\lfloor k/x\rfloor$.''',
        r'''Kad tvrdnja ovisi o malom alfabetu ($m=2$), brute force za male $n$ nije samo eksperiment: kombiniran s lokalnim argumentom (zabranjeni uzorci ograničene duljine, jedinstveno produljenje) postaje strog dokaz za sve $n$.''',
    ],
    'solution': r'''
<p>Slučaj $m = 1$ je trivijalan.</p>
<p>Za $m \ge 3$ svaki znak možemo učiniti različitim od dva prethodna, čime ne nastaje nijedan palindrom duljine veće od $1$. Tada, neovisno o ranijim izborima, imamo $m$ mogućnosti za prvu poziciju, $m - 1$ za drugu i $m - 2$ za sve ostale. Odavde je lako naći $k$-ti niz.</p>
<p>Za $m = 2$ možete napisati brute force i uočiti da za $n \ge 10$ postoji točno $12$ valjanih nizova, svaki s periodom $6$.</p>
''',
    'detailed': r'''
<h3>1. Donja granica $P\ge n$ i kad je dostižna</h3>
<p>Svaki znak je palindromni podsegment duljine $1$, pa je $P\ge n$. Ako je $a[l..r]$ palindrom duljine $\ge2$, onda je i $a[l+1..r-1]$ palindrom; ponavljanjem stižemo do palindroma duljine $2$ (za parnu) ili $3$ (za neparnu duljinu). Dakle:</p>
<p><strong>Lema 1.</strong> Niz ima točno $n$ palindromnih podsegmenata ako i samo ako za sve $i$ vrijedi $a_i\ne a_{i+1}$ i $a_i\ne a_{i+2}$ („svaki element različit od dva prethodna”).</p>

<h3>2. Slučaj $m\ge3$: brojanje i $k$-ti niz</h3>
<p>Uvjet Leme 1 je ostvariv: za $a_1$ biramo bilo koju od $m$ vrijednosti, za $a_2$ bilo koju od $m-1$ (ne $a_1$), a za $a_i$, $i\ge3$, bilo koju od $m-2$ vrijednosti — zabranjene $a_{i-1}$ i $a_{i-2}$ su međusobno različite, pa ih je točno dvije. Ključno: <strong>broj dopuštenih vrijednosti na svakoj poziciji ne ovisi o ranijim izborima.</strong> Zato je ukupan broj optimalnih nizova
$$N=m(m-1)(m-2)^{n-2}\quad(n\ge2),\qquad N=m\ (n=1),$$
i, važnije, svaka dopuštena vrijednost na poziciji $i$ (0-indeksirano) ima jednak broj nastavaka:
$$c_0=(m-1)(m-2)^{n-2},\qquad c_i=(m-2)^{n-1-i}\ (i\ge1).$$
Leksikografski poredak optimalnih nizova stoga je poredak „brojeva” u mješovitoj bazi: $k$-ti niz (s $k\leftarrow k-1$, 0-indeksirano) dobivamo pohlepno: na poziciji $i$ uzmemo $\mathrm{idx}=\lfloor k/c_i\rfloor$-tu najmanju dopuštenu vrijednost i stavimo $k\leftarrow k-\mathrm{idx}\cdot c_i$. Dopuštene vrijednosti su $\{1..m\}$ bez $z_1\lt z_2$ (zabranjenih); $\mathrm{idx}$-ta najmanja je $v=\mathrm{idx}+1$, uvećano za $1$ ako je $v\ge z_1$, i još za $1$ ako je nakon toga $v\ge z_2$.</p>
<p><em>Zašto je pohlepno ispravno.</em> Svi optimalni nizovi koji počinju manjom dopuštenom vrijednošću na poziciji $i$ (uz isti prefiks) leksikografski su manji od onih s većom, a svaka grupa ima točno $c_i$ članova; $k$-ti niz zato pada u grupu s indeksom $\lfloor k/c_i\rfloor$, a unutar nje je $(k\bmod c_i)$-ti — upravo rekurzija gore.</p>

<h3>3. Prelijevanje: aritmetika s kapom</h3>
<p>$N$ i $c_i$ mogu biti golemi ($m,n\le10^6$), ali nas zanimaju samo usporedbe s $k\le10^{18}$ i kvocijenti $\lfloor k/c_i\rfloor$. Uvedimo kapu $K=2\cdot10^{18}$ i množenje $a\otimes b=\min(ab,K)$ (umnožak u <code>__int128</code>). Kapa je apsorbirajuća ($K\otimes b=K$ za $b\ge1$), pa je $c_i$ s kapom jednak pravom $c_i$ kad je on $\le K$, a inače je $K>k$. U oba slučaja $\lfloor k/c_i\rfloor$ ispada točno (u drugom je $0$). Potencije $(m-2)^j$ računamo unaprijed s kapom u $O(n)$; kad su jednom na kapi, ostaju.</p>

<h3>4. Slučaj $m=1$</h3>
<p>Postoji samo niz $1,1,\dots,1$ (svaki podsegment mu je palindrom, $P=n(n+1)/2$, ali je jedini). Za $k=1$ ispišemo ga, inače $-1$.</p>

<h3>5. Slučaj $m=2$</h3>
<p>Za binarne nizove ne možemo izbjeći i $aa$ i $aba$ (ako je $a_i\ne a_{i+1}$ za sve $i$, niz je $0101\ldots$ i sadrži $aba$). Pokazat ćemo $P_{\min}=2n-2$ i da su za $n\ge10$ optimalni nizovi točno $12$ periodičnih nizova.</p>
<p><strong>Lema 2 (donja granica).</strong> Za $n\ge2$ svaki binarni niz ima $P\ge2n-2$.</p>
<p><em>Dokaz.</em> Uz $n$ jednočlanih palindroma pokažimo $n-2$ različitih palindroma duljine $\ge2$. Svakoj unutarnjoj poziciji $i$ ($1\le i\le n-2$, 0-indeksirano) dodijelimo palindrom $\phi(i)$: ako je $a_{i-1}=a_{i+1}$, $\phi(i)=[i-1,i+1]$; inače su $a_{i-1}\ne a_{i+1}$, pa je $a_i$ jednak točno jednom od njih: $\phi(i)=[i-1,i]$ ako je $a_i=a_{i-1}$, inače $\phi(i)=[i,i+1]$. Kolizije: palindrom $[i-1,i+1]$ ima jedinstveno središte $i$. Palindrom $[i,i+1]$ mogu dobiti $i$ (treći slučaj: $a_i=a_{i+1}$, $a_{i-1}\ne a_{i+1}$) i $i+1$ (drugi slučaj: $a_{i+1}=a_i$, $a_i\ne a_{i+2}$) — tada je $a_{i-1}=a_{i+2}\ne a_i=a_{i+1}$, tj. uzorak $baab$, i $[i-1,i+2]$ je palindrom duljine $4$ sa središtem između $i$ i $i+1$; njega dodijelimo poziciji $i+1$. Palindromi duljine $4$ dodjeljuju se samo tako, po jedan po središtu, pa je konačna dodjela injektivna. $\square$</p>
<p><strong>Karakterizacija jednakosti.</strong> $P=2n-2$ znači da je <em>svaki</em> palindrom duljine $\ge2$ u slici dodjele $\phi$. Je li neki palindrom „nepreuzet” lokalno je svojstvo: slika $\phi(p)$ ovisi o $a_{p-2..p+2}$. Neka je $F$ skup od $10$ uzoraka
$$000,\ 111,\ 01010,\ 10101,\ 00100,\ 11011,\ 010010,\ 101101,\ 110011,\ 001100 .$$
Konačnom provjerom (skripta <code>provjera_leme.py</code> uz rješenje) utvrđeno je: (a) za $3\le n\le14$ niz ima $P=2n-2$ ako i samo ako ne sadrži nijedan uzorak iz $F$; (b) svaka pojava uzorka iz $F$, u <em>svakom</em> kontekstu (svi binarni nizovi do $6$ znakova sa svake strane, uključujući rubove niza — više od toga ne utječe na dodjelu pozicija u blizini uzorka), ostavlja barem jedan palindrom u blizini uzorka nepreuzet, pa niz s uzorkom iz $F$ ima $P\ge2n-1$. Zbog lokalnosti je (b) dokaz za sve $n$, ne samo male.</p>
<p><strong>Lema 3 (struktura).</strong> Binarni nizovi duljine $n\ge10$ bez uzoraka iz $F$ su točno $12$ prefiksa beskonačnih periodičnih nizova s periodom $6$: šest rotacija riječi $001011$ i njihovi komplementi (u zapisu $1/2$: rotacije $112122$ i $221211$).</p>
<p><em>Dokaz.</em> Iscrpno: nizova duljine $10$ bez $F$ ima točno $12$ i to su prefiksi navedenih periodičnih riječi (svi različiti). Nadalje, za svaki prozor od $5$ uzastopnih znakova periodične riječi postoji <em>jedinstven</em> znak čijim dodavanjem ne nastaje uzorak iz $F$ (uzorci imaju duljinu $\le6$, pa novi uzorak može završavati samo na dodanom znaku), i to je upravo sljedeći znak periodične riječi. Indukcijom po $n$: niz duljine $n\ge10$ bez $F$ ima prefiks duljine $10$ koji je prefiks neke periodične riječi $w^\infty$, a svaki sljedeći znak je forsiran, pa je cijeli niz prefiks od $w^\infty$. $\square$</p>
<p><strong>Lema 4.</strong> Svaki od tih $12$ nizova ima točno $2n-2$ palindromnih podsegmenata.</p>
<p><em>Dokaz.</em> Provjerom svih prozora periodične riječi: nema palindroma duljine $5$ ni $6$, dakle ni duljih (dulji bi sadržavao centrirani palindrom duljine $5$ ili $6$). Broj palindroma koji završavaju na poziciji $i$ zato ovisi samo o zadnja četiri znaka i kroz cijeli period iznosi točno $2$; uz $P(10)=18=2\cdot10-2$ dobivamo $P(n)=18+2(n-10)=2n-2$. $\square$</p>
<p><strong>Zaključak za $m=2$.</strong> Za $n\ge10$: minimum je $2n-2$ (Leme 2 i 4), a optimalni nizovi su točno oni bez uzoraka iz $F$ ((b) i Lema 4), dakle točno $12$ periodičnih (Lema 3). Za $k\le12$ ispisujemo $k$-ti u sortiranom poretku tih $12$ nizova, inače $-1$. Za $n<10$ jednostavno nabrojimo svih $2^n\le512$ nizova, izbrojimo palindrome u $O(n^2)$ i zadržimo minimalne — nema potrebe za lemom.</p>

<h3>6. Algoritam</h3>
<ol>
<li>$m=1$: ispiši $n$ jedinica ako je $k=1$, inače $-1$.</li>
<li>$m=2$, $n<10$: iscrpno; $n\ge10$: generiraj $12$ periodičnih nizova duljine $n$, sortiraj, ispiši $k$-ti ili $-1$.</li>
<li>$m\ge3$: izračunaj $N$ s kapom; ako je $N\lt k$, $-1$. Inače potencije $(m-2)^j$ s kapom, pa pohlepna rekonstrukcija po pozicijama uz izbor $\mathrm{idx}$-te najmanje dopuštene vrijednosti.</li>
</ol>

<h3>7. Složenost</h3>
<p>$O(n)$ za $m\ge3$ i za periodični slučaj; $O(2^n n^2)$ za $m=2$, $n<10$, što je ispod $10^5$ operacija. Ispis od $10^6$ brojeva treba raditi brzo (skupljanje u jedan string).</p>

<h3>8. Rubni slučajevi i zamke</h3>
<ul>
<li>$n=1$: $N=m$, odgovor je sam broj $k$ ako je $k\le m$. $n=2$, $m\ge3$: $N=m(m-1)$, $c_0=m-1$ (formula s $(m-2)^{n-2}$ mora dati $1$, ne $0$).</li>
<li>Zabranjene vrijednosti: na poziciji $1$ postoji samo jedna, na poziciji $0$ nijedna; pri „preskakanju” prvo usporedi s manjom pa s većom zabranjenom vrijednošću.</li>
<li>Bez kape $m(m-1)(m-2)^{n-2}$ prelijeva već za $n\approx 30$; kapa mora biti $>10^{18}$ (npr. $2\cdot10^{18}$) i množenje s kapom mora se raditi u 128-bitnoj aritmetici ili provjerom $a>K/b$.</li>
<li>$m=2$, $n<10$: među optimalnima za $n=2$ su $12$ i $21$ (oba imaju $P=2$), pa je za $k=2$ odgovor $2\ 1$ — kao u primjeru; za $n=1$ optimalni su $1$ i $2$.</li>
<li>Znakovi se ispisuju kao $1..m$; kod binarnog slučaja pretvori $0/1$ u $1/2$.</li>
</ul>

<h3>9. Primjer</h3>
<p>$n=3$, $m=3$, $k=3$: $N=3\cdot2\cdot1=6$, $c_0=2$, $c_1=1$, $c_2=1$. $k\leftarrow2$. Pozicija 0: $\mathrm{idx}=\lfloor2/2\rfloor=1$, dopuštene $\{1,2,3\}$, druga najmanja je $2$; $k\leftarrow0$. Pozicija 1: $\mathrm{idx}=0$, zabranjena $2$, najmanja dopuštena je $1$. Pozicija 2: $\mathrm{idx}=0$, zabranjene $1$ i $2$, ostaje $3$. Odgovor $2\ 1\ 3$ — poredak optimalnih nizova je $123,132,213,231,312,321$, i treći je doista $213$. Za $n=10$, $m=7$, $k=998244353$: $N=7\cdot6\cdot5^8=16\,406\,250\lt k$, odgovor $-1$.</p>
''',
    'verified': r'''uzorci 6/6; 300 slučajnih testova ($n\le12$, $m\le6$ uz $m^n\le6\cdot10^4$, $k$ do $10^{18}$) protiv Python brute forcea koji nabraja svih $m^n$ nizova, broji palindrome i sortira optimalne; 3 velika testa ($n=10^6$, $m\in\{1,2,3,4,10^6,\dots\}$, $k$ do $10^{18}$), najviše $0.03$ s; konačne leme za $m=2$ provjerene skriptom <code>provjera_leme.py</code>.''',
},
# ---------------------------------------------------------------- K
{
    'letter': 'K', 'title': '4', 'title_hr': '4', 'slug': 'K_4',
    'tl': '1 s', 'ml': '512 MiB',
    'statement': r'''
<p>Dan je jednostavan neusmjereni graf. Prebroji njegove podgrafe $K_4$ (skupove od $4$ vrha među kojima postoji svih $6$ bridova).</p>
<h3>Ulaz</h3>
<p>$n$, $m$ ($4 \le n \le 10^5$, $0 \le m \le 10^5$) i $m$ bridova; bez petlji i višestrukih bridova.</p>
<h3>Izlaz</h3>
<p>Broj $K_4$.</p>
<h3>Primjer</h3>
<p>Za $K_5$ bez jednog brida ($n = 5$, $m = 9$) odgovor je $2$.</p>
''',
    'hints': [
        r'''<p>Klasična orijentacija po stupnju: sortiraj vrhove po stupnju i svaki brid usmjeri prema vrhu većeg stupnja. Tada je izlazni stupanj svakog vrha $d_i = O(\sqrt{m})$.</p>''',
        r'''<p>Fiksiraj najmanji vrh $u$ klike. Trokuti kroz $u$ nalaze se u $O(d_u \sqrt{m})$; oni čine mali graf na $d_u$ izlaznih susjeda, a $K_4$ kroz $u$ odgovara trokutu u tom malom grafu.</p>''',
        r'''<p>Trokute u malom grafu s $n_u$ vrhova i $m_u$ bridova broji bitsetom u $O(m_u n_u / w)$; zbroj $m_u$ po svim $u$ je broj trokuta, $O(m \sqrt{m})$.</p>''',
    ],
    'coach': [
        ('Zašto ne možemo jednostavno za svaki trokut provjeriti sve četvrte vrhove, i koja veličina ograničava posao?', r'''<p>Trokuta može biti $\Theta(m\sqrt m)\approx1.5\cdot10^7$, a četvrti vrh bismo tražili među susjedima — presporo i puno dvostrukog brojanja. Standardni lijek je <strong>orijentacija po stupnju</strong>: poredamo vrhove po stupnju (uz indeks kao sekundarni ključ, da poredak bude strog) i svaki brid usmjerimo od manjeg prema većem vrhu. Ključna veličina je izlazni stupanj $d_u$: ako je $u$ na poziciji $r$ od kraja, iza njega je $r-1$ vrhova sa stupnjem $\ge\deg u$, pa je $r\cdot\deg u\le2m$; kako je $d_u\le\min(\deg u,\,r-1)$, slijedi $d_u\le\min(2m/r,\,r)\le\sqrt{2m}<448$.</p>'''),
        ('Kako svaki $K_4$ prebrojati točno jednom i pritom se osloniti na mali izlazni stupanj?', r'''<p>U svakom $K_4$ postoji jedinstven najmanji vrh $u$ u našem poretku; ostala tri vrha su njegovi <em>izlazni</em> susjedi. Dakle $K_4$ kroz $u$ kao najmanji vrh je trojka $x,y,z\in N^+(u)$ koja je međusobno povezana — a to je <strong>trokut u pomoćnom grafu</strong> $G_u$ na skupu $N^+(u)$ (veličine $d_u\le\sqrt{2m}$) čiji je brid $(x,y)$ točno kad je $(x,y)$ brid izvornog grafa, tj. kad je $(u,x,y)$ trokut. Zbrajanjem po svim $u$ svaki je $K_4$ ubrojan jednom.</p>'''),
        ('Kako brzo izgraditi $G_u$ i koliko ukupno ima bridova u svim $G_u$?', r'''<p>Označimo pozicije izlaznih susjeda $u$ u nizu <code>pozicija[]</code>; za svaki $x\in N^+(u)$ prođemo njegove izlazne susjede $y$ i, ako je $y$ označen, dodamo brid $(x,y)$ u $G_u$ (svaki brid izvornog grafa među izlaznim susjedima ima točno jedan „manji” kraj, pa ga nađemo točno jednom). Trošak je $\sum_{x\in N^+(u)}d_x\le d_u\sqrt{2m}$, ukupno $\sum_u d_u\sqrt{2m}=m\sqrt{2m}$. Ukupan broj bridova svih $G_u$ jednak je broju trokuta grafa, $O(m\sqrt m)$.</p>'''),
        ('Koja struktura broji trokute u malom gustom grafu najbrže, i kako izbjeći višestruko brojanje?', r'''<p>Bitsetovi: matrica susjedstva $G_u$ kao $d_u$ bitsetova širine $512\ge\sqrt{2m}$. Za svaki brid $(i,j)$, $i\lt j$, broj zajedničkih susjeda je <code>(B[i]&amp;B[j]).count()</code> — $8$ 64-bitnih riječi. Svaki trokut $\{i,j,l\}$ tako je ubrojan jednom po svakom svom bridu, dakle tri puta, pa zbroj podijelimo s $3$. Ukupno $O\bigl(\sum_u m_u\cdot d_u/w\bigr)=O(m^2/w)$, uz $m=10^5$ oko $10^8$ operacija na riječima — daleko ispod limita.</p>'''),
    ],
    'tips': [
        r'''Orijentacija po stupnju (svaki brid od manjeg prema većem stupnju) jamči izlazni stupanj $\le\sqrt{2m}$; to je univerzalni ulaz u brojanje trokuta, $K_4$ i drugih malih gustih podgrafa u $O(m\sqrt m)$-ish vremenu.''',
        r'''Svaku kliku broj kroz njezin jedinstveni „najmanji” vrh u strogom totalnom poretku — automatski dobivaš svaki podgraf točno jednom, bez dijeljenja s $4!$ i bez skupova.''',
        r'''Kad je pomoćni graf malen ($\le$ nekoliko stotina vrhova) ali gust, bitset matrica susjedstva pobjeđuje liste: presjek susjedstava košta $d/64$ riječi.''',
        r'''Prije ispisa procijeni veličinu odgovora: $\binom{447}{4}\approx1.6\cdot10^9$ ne stane u 32 bita.''',
    ],
    'solution': r'''
<p>Sortirajmo vrhove po rastućem stupnju. Za svaki vrh promatramo samo bridove prema vrhovima desno od njega; neka je broj takvih bridova iz $i$-tog vrha $d_i$. Očito $d_i \le \deg_i$, $\sum_i d_i = m$, $\sum_i \deg_i = 2m$.</p>
<p>Za vrhove sa $\deg_i \le \sqrt{2m}$ jasno je $d_i \le \sqrt{2m}$. Vrhova sa $\deg_i > \sqrt{2m}$ može biti najviše $\sqrt{2m}$ i oni su na kraju liste sortirane po stupnju, pa je i za njih $d_i < \sqrt{2m}$.</p>
<p>Fiksirajmo prvi vrh $u$ mogućeg $K_4$. U $O(d_i(d_i + \sqrt{2m})) = O(d_i \sqrt{m})$ iscrpnim pretraživanjem nalazimo sve trokute ($K_3$) iz tog vrha. Izgradimo novi graf samo na susjedima fiksiranog vrha koji su desno od njega, u kojem brid $(x, y)$ znači da postoji trokut $(u, x, y)$ u izvornom grafu. Sada $K_4$ $(u, x, y, z)$ u izvornom grafu odgovara trokutu $(x, y, z)$ u novom malom grafu.</p>
<p>Dakle želimo prebrojati trokute u malom grafu. Ako on ima $n_u$ vrhova i $m_u$ bridova, to se lako radi u $O(m_u n_u / \omega)$ bitsetima. Pri tome je $n_u = d_u$, a $m_u$ je broj trokuta koji počinju u $u$. Vrijedi</p>
<p>$$\sum_u \frac{m_u n_u}{\omega} \le \frac{\sqrt{2m}}{\omega} \sum_u m_u, \qquad \sum_u m_u = O(m\sqrt{m}),$$</p>
<p>jer je to broj trokuta u grafu. Stoga rješenje radi u $O\!\left(\frac{m^2}{\omega}\right)$.</p>
''',
    'detailed': r'''
<h3>1. Orijentacija po stupnju</h3>
<p>Poredajmo vrhove po rastućem stupnju, a pri jednakom stupnju po indeksu, tako da dobijemo strog totalni poredak $\prec$. Svaki brid $\{a,b\}$ usmjerimo od manjeg prema većem vrhu: $a\to b$ ako je $a\prec b$. Neka je $N^+(u)$ skup izlaznih susjeda i $d_u=|N^+(u)|$. Očito $\sum_u d_u=m$.</p>
<p><strong>Lema 1.</strong> Za svaki vrh $d_u\le\sqrt{2m}$.</p>
<p><em>Dokaz.</em> Neka je $u$ $r$-ti vrh od kraja poretka ($r\ge1$). Svih $r-1$ vrhova iza njega ima stupanj $\ge\deg u$, pa je $r\cdot\deg u\le\sum_v\deg v=2m$, tj. $\deg u\le2m/r$. S druge strane, izlazni susjedi su među $r-1$ vrhova iza $u$, pa je $d_u\le r-1\lt r$. Zato je $d_u\le\min(\deg u,\,r)\le\min(2m/r,\,r)\le\sqrt{2m}$, jer je $\min(2m/r,r)$ najveći kad je $r=\sqrt{2m}$. $\square$</p>
<p>Za $m=10^5$ to je $d_u\le447$, pa bitset širine $512$ pokriva svaki $N^+(u)$.</p>

<h3>2. $K_4$ = trokut u pomoćnom grafu najmanjeg vrha</h3>
<p>Svaki $K_4$ $\{u,x,y,z\}$ ima jedinstven najmanji vrh $u$ u poretku $\prec$; tada su $x,y,z\in N^+(u)$ (bridovi iz $u$ vode „prema gore”). Definirajmo za fiksni $u$ pomoćni graf $G_u$ s vrhovima $N^+(u)$ i bridom $\{x,y\}$ točno kad je $\{x,y\}$ brid izvornog grafa — tj. kad je $(u,x,y)$ trokut.</p>
<p><strong>Lema 2.</strong> Broj $K_4$ u grafu jednak je $\sum_u T(G_u)$, gdje je $T$ broj trokuta.</p>
<p><em>Dokaz.</em> Trokut $\{x,y,z\}$ u $G_u$ znači da su $x,y,z$ izlazni susjedi $u$ i međusobno spojeni: $\{u,x,y,z\}$ ima svih šest bridova, pa je $K_4$ s najmanjim vrhom $u$. Obratno, svaki $K_4$ daje trokut u $G_u$ za svoj najmanji vrh $u$, i ni za koji drugi $u'$ (jer bi tada $u\in N^+(u')$, tj. $u'\prec u$, protivno minimalnosti $u$). Pridruživanje je bijekcija između $K_4$-ova i parova ($u$, trokut u $G_u$). $\square$</p>

<h3>3. Izgradnja $G_u$</h3>
<p>Za fiksni $u$ upišemo <code>pozicija[x]=i</code> za $i$-tog izlaznog susjeda $x$ (ostali vrhovi imaju $-1$). Za svaki $x\in N^+(u)$ prolazimo njegove izlazne susjede $y$; ako je <code>pozicija[y]>=0</code>, dodamo brid $(i,j)$ u $G_u$ (u oba bitseta). Svaki brid $\{x,y\}$ izvornog grafa s $x,y\in N^+(u)$ nađen je točno jednom — iz svog manjeg kraja — pa je $G_u$ točno graf iz Leme 2. Nakon obrade $u$ oznake vratimo na $-1$, što košta $O(d_u)$.</p>
<p>Trošak izgradnje je $\sum_{x\in N^+(u)}d_x\le d_u\sqrt{2m}$ po Lemi 1, ukupno $\sum_u d_u\sqrt{2m}=m\sqrt{2m}\approx4.5\cdot10^7$ koraka.</p>

<h3>4. Brojanje trokuta bitsetima</h3>
<p>$G_u$ ima $n_u=d_u\le447$ vrhova i $m_u$ bridova; njegovu matricu susjedstva držimo kao $n_u$ bitsetova širine $512$. Za svaki brid $(i,j)$ s $i\lt j$ (prolazimo postavljene bitove <code>B[i]</code> iza pozicije $i$) broj zajedničkih susjeda je $|B[i]\cap B[j]|$ = <code>(B[i]&amp;B[j]).count()</code>, $8$ riječi. Trokut $\{i,j,l\}$ ubrojan je jednom za svaki od svoja tri brida, pa je $T(G_u)$ = zbroj podijeljen s $3$ (zbroj je uvijek djeljiv s $3$). Alternativa bez dijeljenja: brojati samo $l>j$ maskiranjem, ali dijeljenje je jednostavnije i jednako brzo.</p>

<h3>5. Složenost</h3>
<p>Sortiranje $O(n\log n)$; izgradnja svih $G_u$ $O(m\sqrt m)$. Brojanje: $\sum_u m_u\cdot\lceil512/64\rceil$ operacija na riječima, a $\sum_u m_u$ je točno broj trokuta izvornog grafa. Broj trokuta je $O(m\sqrt m)$: svaki trokut ima najmanji vrh $u$ i dva njegova izlazna susjeda, pa ih je $\le\sum_u\binom{d_u}{2}\le\frac{\sqrt{2m}}2\sum_u d_u=O(m\sqrt m)$. Ukupno $O(m\sqrt m\cdot\sqrt m/w)=O(m^2/w)\approx1.6\cdot10^8$ jednostavnih operacija — u praksi ispod pola sekunde i za najgori slučaj (potpuni graf na $447$ vrhova, gdje je trokuta $\approx1.5\cdot10^7$). Memorija: bitsetovi za jedan $u$ odjednom, $447\cdot64$ B, plus liste susjedstva $O(n+m)$.</p>

<h3>6. Rubni slučajevi i zamke</h3>
<ul>
<li>Odgovor može biti do $\binom{447}{4}\approx1.65\cdot10^9$ — <code>long long</code>.</li>
<li>Poredak mora biti <em>strog</em> (stupanj, pa indeks); inače se brid između dva vrha istog stupnja može orijentirati nedosljedno i klika se izgubi ili udvostruči.</li>
<li>Vrhovi s $d_u<3$ ne mogu biti najmanji vrh $K_4$ — preskačemo ih, što ujedno štedi vrijeme na rijetkim grafovima.</li>
<li>$m=0$ ili graf bez trokuta: odgovor $0$; petlje i višestruki bridovi ne postoje po uvjetu zadatka.</li>
<li>Širina bitseta mora biti $\ge\max d_u$; $512>447=\lfloor\sqrt{2\cdot10^5}\rfloor$ je sigurno. Za drukčija ograničenja ponovno izračunaj $\sqrt{2m}$.</li>
<li>Oznake <code>pozicija[]</code> obavezno očistiti nakon svakog $u$; alternativa je vremenski pečat.</li>
</ul>

<h3>7. Primjer</h3>
<p>$K_5$ bez brida $\{4,5\}$: stupnjevi $\deg1=\deg2=\deg3=4$, $\deg4=\deg5=3$, poredak $4\prec5\prec1\prec2\prec3$. Izlazni susjedi: $N^+(4)=\{1,2,3\}$, $N^+(5)=\{1,2,3\}$, $N^+(1)=\{2,3\}$, $N^+(2)=\{3\}$, $N^+(3)=\emptyset$. Za $u=4$: $G_4$ na $\{1,2,3\}$ ima sva tri brida — jedan trokut, dakle $K_4$ $\{4,1,2,3\}$; isto za $u=5$. Ostali vrhovi imaju $d_u<3$. Odgovor $2$ — kao u primjeru. Drugi primjer, $n=4$, $m=0$: odgovor $0$.</p>
''',
    'verified': r'''uzorci 2/2; 300 slučajnih grafova ($n\le12$, gustoća $0.2$–$1$) protiv brute forcea koji provjerava sve $\binom n4$ četvorke; 3 velika testa ($m=10^5$: potpuni graf na $447$ vrhova, gust slučajni graf na $500$ vrhova, rijedak graf sa $20$ klika veličine $60$), najviše $0.37$ s.''',
},
# ---------------------------------------------------------------- L
{
    'letter': 'L', 'title': '5', 'title_hr': '5', 'slug': 'L_5',
    'tl': '5 s', 'ml': '555 MiB',
    'statement': r'''
<p>Dan je niz $a$ duljine $n$ nenegativnih cijelih brojeva sa zbrojem $S$. Prebroji parove $(k, T)$ takve da postoji podniz od $a$ duljine $k$ sa zbrojem $T$. Zajamčeno je da barem $S/5$ elemenata niza iznosi $1$.</p>
<h3>Ulaz</h3>
<p>$n$, $S$ ($1 \le n, S \le 2 \cdot 10^5$) i niz $a$ ($0 \le a_i \le S$, $\sum a_i = S$).</p>
<h3>Izlaz</h3>
<p>Broj parova $(k, T)$.</p>
<h3>Primjer</h3>
<p>Za $a = (0, 0, 0, 1, 1, 2, 5)$ odgovor je $42$.</p>
''',
    'hints': [],
    'coach': [],
    'solution': None,
},
]
