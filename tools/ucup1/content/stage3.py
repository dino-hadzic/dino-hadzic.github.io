# -*- coding: utf-8 -*-
STAGE = {
    'no': 3,
    'name': 'Stage 3: Poland',
    'source_name': 'February 11-12, 2023',
    'no_editorial': True,
    'community': True,
    'source_html': r'''
<p>Zadaci potječu s natjecanja AMPPZ 2022 (Akademickie Mistrzostwa Polski w Programowaniu Zespołowym — The 2022 ICPC Polish Collegiate Programming Contest, Kraków, 30. 10. 2022.). Tekst zadatka preveden je prema službenim <a href="https://contest.ucup.ac/download.php?type=attachments&amp;id=1103&amp;r=1">engleskim tekstovima zadataka</a>. Organizatori nisu objavili službena rješenja. Zadatak je dostupan na <a href="https://contest.ucup.ac/contest/1103">Universal Cup Judging System</a>.</p>
''',
}

PROBLEMS = [
# ---------------------------------------------------------------- A
{
    'letter': 'A', 'title': 'Aliases', 'title_hr': 'Nadimci', 'slug': 'A_aliases',
    'tl': '42 s', 'ml': '1024 MiB',
    'statement': r'''
<p>Za $n$ natjecatelja treba napraviti korisnička imena (nadimke) po istom pravilu: prvih $a$ slova imena, zatim prvih $b$ slova prezimena i na kraju $c$ znamenaka po vlastitom izboru. Ako ime ima manje od $a$ slova (ili prezime manje od $b$), uzimaju se sva slova. Npr. za $a = b = c = 3$ James Bond može dobiti <code>jambon007</code>, a Lady Di <code>laddi123</code>.</p>
<p>Svi nadimci moraju biti međusobno različiti. Nađi nenegativne $a, b, c$ (ne sve tri nule) za koje je to moguće i za koje je $a + b + c$ najmanje moguće.</p>
<h3>Ulaz</h3>
<p>$z \le 6$ testova. U svakom $n \le 200\,000$ parova ime prezime (mala engleska slova); ukupna duljina svih imena i prezimena u testu je najviše $1\,500\,000$. Dvoje sudionika može imati isto ime i prezime (i tada moraju dobiti različite nadimke).</p>
<h3>Izlaz</h3>
<p>Za svaki test tri broja $a$, $b$, $c$ s najmanjim zbrojem. Ako ima više rješenja, ispiši bilo koje.</p>
<h3>Primjer</h3>
<p>Za $11$ sudionika (sven eriksson, erik svensson, sven svensson, erik eriksson, bjorn eriksson, bjorn svensson, bjorn bjornsson, erik bjornsson, sven bjornsson, thor odinsson, odin thorsson) odgovor je <code>1 1 0</code> — inicijali su svima različiti. Točan je i odgovor <code>1 0 1</code>.</p>
''',
    'hints': [
        r'''
<p>Koliko najviše mogu iznositi $a$, $b$ i $c$ u optimalnom rješenju? Razmisli što se dogodi s $a = b = 0$ i nekim ne prevelikim $c$.</p>
''',
        r'''
<p>Za fiksne $a$ i $b$ slovni dio nadimka je određen; ljudi s istim slovnim dijelom razlikuju se samo znamenkama. Koliko ih najviše smije dijeliti isti slovni dio ako imamo $c$ znamenaka?</p>
''',
        r'''
<p>Kandidata $(a, b, c)$ je jako malo. Isprobaj ih po rastućem zbroju $a+b+c$ i za svaki izračunaj najveću skupinu jednakih slovnih dijelova (sortiranjem ili hash-tablicom).</p>
''',
    ],
    'coach': [
        ('Zašto je odgovor uvijek mali, tj. zašto ne moramo gledati velike $a$, $b$, $c$?',
         r'''
<p>Uzmemo li $a = b = 0$ i $c = 6$, svi nadimci su šesteroznamenkasti nizovi, a njih ima $10^6 \ge 200\,000 \ge n$. Dakle uvijek postoji rješenje sa zbrojem $6$, pa optimalno rješenje ima $a + b + c \le 6$. To ostavlja samo $\binom{6+3}{3} = 84$ trojke, a među njima nas zanimaju one s najmanjim zbrojem.</p>
'''),
        ('Kad je konkretna trojka $(a, b, c)$ dobra? Što točno treba biti različito?',
         r'''
<p>Za fiksne $a$ i $b$ svaki sudionik ima <em>slovni dio</em>: prvih $a$ slova imena (ili cijelo kraće ime) spojeno s prvih $b$ slova prezimena. Dva sudionika s različitim slovnim dijelovima uvijek dobiju različite nadimke. Sudionici s jednakim slovnim dijelom razlikuju se samo sufiksom od $c$ znamenaka, a takvih sufiksa ima točno $10^c$ (za $c = 0$ samo jedan, prazan). Trojka je dobra ako i samo ako nijedna skupina jednakih slovnih dijelova nema više od $10^c$ članova.</p>
'''),
        ('Kako brzo naći najveću skupinu jednakih slovnih dijelova?',
         r'''
<p>Slovni dio ima najviše $a + b \le 6$ slova. Kodiramo ga kao broj u bazi $27$ (slovo $\to 1..26$) — to je injektivno za nizove do $6$ slova i stane u 64 bita, pa nema kolizija kao kod hashiranja. Sortiramo $n$ ključeva i prebrojimo najdulji blok jednakih. Za jedan par $(a,b)$ to je $O(n \log n)$, a parova s $a + b \le 6$ ima $28$.</p>
'''),
        ('U kojem redoslijedu isprobavati trojke da prva dobra bude i optimalna?',
         r'''
<p>Po rastućem zbroju $s = a+b+c = 1, 2, \dots$; za svaki $s$ prođemo sve $(a, b)$ s $a + b \le s$ i stavimo $c = s - a - b$. Prva dobra trojka ima najmanji zbroj, pa je odgovor. Ako više trojki ima isti zbroj, bilo koja je točna.</p>
'''),
    ],
    'tips': [
        r'''Kad je odgovor omeđen malim brojem (ovdje $a+b+c \le 6$), potpuna pretraga po kandidatima uz brzu provjeru često pobjeđuje „pametnu” konstrukciju.''',
        r'''Kratke nizove slova kodiraj kao cijele brojeve u bazi $27$ umjesto da ih hashiraš — provjera je egzaktna, a sortiranje brojeva puno je brže od sortiranja stringova.''',
        r'''Pripazi na tekst zadatka: uspoređuje se <em>cijeli</em> nadimak kao string. Ime „a” + prezime „bc” i ime „ab” + prezime „c” daju isti slovni dio „abc” i moraju se razlikovati znamenkama.''',
    ],
    'solution': r'''
<p>Prema javnim analizama natjecanja AMPPZ 2022 i vlastitoj razradi. Sa $a = b = 0$, $c = 6$ nadimaka je $10^6 \ge n$, pa je optimalno $a + b + c \le 6$. Za fiksne $(a, b)$ slovni dio nadimka (prefiks imena spojen s prefiksom prezimena) određuje skupinu, a unutar skupine sudionici se razlikuju samo $c$ znamenaka; trojka je dobra ako i samo ako najveća skupina jednakih slovnih dijelova ima najviše $10^c$ članova. Trojke ispitujemo po rastućem zbroju; za svaki od $28$ parova $(a, b)$ s $a + b \le 6$ slovne dijelove kodiramo kao brojeve u bazi $27$, sortiramo i nađemo najveću skupinu u $O(n \log n)$. Prva dobra trojka je odgovor.</p>
''',
    'detailed': r'''
<h3>1. Odgovor je omeđen</h3>
<p>Ako uzmemo $a = b = 0$ i $c = 6$, nadimak je isključivo niz od $6$ znamenaka, a takvih nizova ima $10^6$. Kako je $n \le 200\,000 \lt 10^6$, svakom sudioniku možemo dodijeliti različit niz, pa je trojka $(0, 0, 6)$ uvijek dopustiva. Optimalna trojka stoga ima zbroj $a + b + c \le 6$, tj. $a, b, c \le 6$. Kandidata je najviše $\binom{9}{3} = 84$, pa ih smijemo sve isprobati.</p>
<h3>2. Kriterij dopustivosti trojke</h3>
<p>Fiksirajmo $(a, b, c)$. Nadimak sudionika $i$ je $L_i + S_i$, gdje je $L_i$ <em>slovni dio</em> (prvih $a$ slova imena — ili cijelo ime ako je kraće — pa prvih $b$ slova prezimena, s istom napomenom) i $S_i$ niz od točno $c$ znamenaka koji sami biramo. Svi nadimci imaju slovni dio duljine najviše $a+b$ i znamenkasti dio duljine točno $c$, pa je nadimak jednoznačno rastavljen: znamenke su uvijek posljednjih $c$ znakova. Dakle dva nadimka su jednaka ako i samo ako su im jednaki slovni dijelovi <em>i</em> znamenkasti dijelovi.</p>
<p>Podijelimo sudionike u skupine po jednakom slovnom dijelu $L_i$. Sudionici iz različitih skupina automatski dobivaju različite nadimke. Unutar skupine veličine $g$ svi moraju dobiti različite znamenkaste dijelove, a na raspolaganju ih je točno $10^c$ (za $c = 0$ samo prazan niz). To je moguće ako i samo ako je $g \le 10^c$. Zaključak: <strong>trojka je dopustiva ako i samo ako najveća skupina jednakih slovnih dijelova ima najviše $10^c$ članova.</strong></p>
<p>Važna sitnica: slovni dio je <em>string</em>, ne par (prefiks imena, prefiks prezimena). Za $a = b = 2$ sudionik s imenom „a” i prezimenom „bc” te sudionik s imenom „ab” i prezimenom „c” imaju isti slovni dio „abc”, pa pripadaju istoj skupini. Zato ključ računamo iz spojenog niza slova, bez razdjelnika.</p>
<h3>3. Brzo računanje najveće skupine</h3>
<p>Za par $(a, b)$ slovni dio ima najviše $a + b \le 6$ slova. Kodiramo ga kao broj u bazi $27$: krenemo od $0$ i za svako slovo $x$ računamo $k \leftarrow 27k + (x - \text{'a'} + 1)$. Znamenke $1..26$ nikad nisu $0$, pa nizovi različite duljine daju različite brojeve, a najveći broj je manji od $27^6 \lt 4 \cdot 10^8$ — čak stane u 32 bita. Kodiranje je injektivno, pa nema lažnih kolizija kao kod hashiranja.</p>
<p>Ključeve sortiramo i jednim prolazom nađemo najdulji blok jednakih vrijednosti; to je veličina najveće skupine. Trošak po paru $(a, b)$ je $O(\text{ukupna duljina} + n \log n)$, a parova s $a + b \le 6$ ima $\binom{8}{2} = 28$. Uz $\sum |\text{ime}| + |\text{prezime}| \le 1.5 \cdot 10^6$ i $n \le 2 \cdot 10^5$ to je daleko unutar ograničenja.</p>
<h3>4. Redoslijed ispitivanja</h3>
<p>Prolazimo zbrojeve $s = 1, 2, \dots$ (nula nije dopuštena jer tada svi imaju prazan nadimak; zbroj $6$ je sigurno dovoljan, a $7$ je u kodu samo rezerva). Za svaki $s$ prolazimo $a = 0..s$, $b = 0..s-a$, $c = s - a - b$ i provjeravamo kriterij. Prva dopustiva trojka ima najmanji mogući zbroj i ispisujemo je; zadatak prihvaća bilo koju optimalnu. Za isti par $(a, b)$ veličina najveće skupine ne ovisi o $c$, pa bi se mogla i memoizirati, ali nije potrebno.</p>
<h3>5. Složenost i zamke</h3>
<p>Vrijeme $O(28 \cdot (T + n \log n))$ po testu, gdje je $T$ ukupna duljina imena; memorija $O(T)$. Zamke: (1) ime kraće od $a$ slova uzima se cijelo, ne dopunjava se; (2) skupinu treba računati po spojenom nizu (vidi odjeljak 2); (3) $c = 0$ znači da slovni dijelovi moraju biti međusobno različiti ($10^0 = 1$); (4) dva sudionika s istim imenom i prezimenom uvijek završe u istoj skupini pa sile $c \ge 1$, što je u skladu sa zadatkom.</p>
''',
    'verified': r'''uzorak 1/1 (prihvaća se bilo koja optimalna trojka, pa odgovor provjerava <code>check.py</code>: trojka daje jedinstvene nadimke i ima isti zbroj $a+b+c$ kao očekivana); 300 slučajnih malih testova ($n \le 12$, imena i prezimena do $4$ slova nad malim abecedama s mnogo ponavljanja) protiv brute forcea koji za sve trojke po rastućem zbroju izravno gradi nadimke i provjerava jedinstvenost; 3 velika testa (po $2$ skupa s $n = 200\,000$: kratka imena nad $\{a, b\}$ s mnogo kolizija i slučajna imena do $7$ slova), najsporiji $1.09$ s.''',
},
# ---------------------------------------------------------------- B
{
    'letter': 'B', 'title': 'Bars', 'title_hr': 'Barovi', 'slug': 'B_bars',
    'tl': '6 s', 'ml': '1024 MiB',
    'statement': r'''
<p>Kuće $n$ stanovnika ($1..n$) leže redom uz jednu ravnu cestu. Svaki stanovnik želi otvoriti bar; $i$-ti obećava porez od $p_i$ zlatnika po svakom gostu. Ti odabireš neprazan podskup stanovnika kojima daješ dozvolu.</p>
<p>Svaki stanovnik (imao bar ili ne) postaje gost dvaju barova: najbližeg <em>strogo lijevo</em> i najbližeg <em>strogo desno</em> od svoje kuće (ako postoje; vlastiti bar se ne računa). Svaki otvoreni bar donosi $p_i$ zlatnika po gostu. Npr. za $n = 5$ i otvorene barove $3$ i $5$, treći ima $4$ gosta, a peti $2$: prihod je $4 p_3 + 2 p_5$.</p>
<p>Odredi najveći mogući ukupni prihod.</p>
<h3>Ulaz</h3>
<p>$z \le 10\,000$ testova; $2 \le n \le 500\,000$, $1 \le p_i \le 10^9$; $\sum n \le 3 \cdot 10^6$.</p>
<h3>Izlaz</h3>
<p>Za svaki test najveći ukupni prihod.</p>
<h3>Primjer</h3>
<p>$p = (5, 2, 2, 6)$: otvori prvi i posljednji bar, svaki ima $3$ gosta, prihod $3 \cdot 5 + 3 \cdot 6 = 33$. $p = (1, 5, 4, 4, 1)$: otvori sve osim trećeg, prihod $1 \cdot 1 + 3 \cdot 5 + 3 \cdot 4 + 1 \cdot 1 = 29$ (svi otvoreni dali bi samo $28$).</p>
''',
    'hints': [
        r'''
<p>Zapiši prihod formulom. Ako su otvoreni barovi $i_1 \lt i_2 \lt \dots \lt i_m$, koliko gostiju ima bar $i_j$? Izrazi to preko susjednih otvorenih barova.</p>
''',
        r'''
<p>Pokaži da se otvaranjem bara $1$ i bara $n$ prihod nikad ne smanjuje. Zatim nacrtaj točke $(i, p_i)$ i izlomljenu liniju kroz otvorene barove: prihod je dvostruka površina ispod nje.</p>
''',
        r'''
<p>Površinu ispod izlomljene linije kroz podskup točaka s fiksnim krajevima maksimizira gornja konveksna ljuska. Izračunaj je monotonim stogom u $O(n)$.</p>
''',
    ],
    'coach': [
        ('Koliko gostiju ima pojedini bar i kako se to zapisuje preko susjednih otvorenih barova?',
         r'''
<p>Neka su otvoreni $i_1 \lt \dots \lt i_m$. Stanovnici između $i_{j-1}$ i $i_j$ (uključivo $i_{j-1}$) imaju $i_j$ kao najbliži bar strogo desno, a stanovnici između $i_j$ i $i_{j+1}$ (uključivo $i_{j+1}$) kao najbliži strogo lijevo. Ukupno bar $i_j$ ima $i_{j+1} - i_{j-1}$ gostiju. Krajnji barovi nemaju jednog susjeda: prvi ima $i_2 - 1$ gostiju, a posljednji $n - i_{m-1}$, što je ista formula uz „virtualne” susjede $i_0 = 1$ i $i_{m+1} = n$. Prihod je $\sum_j p_{i_j}\,(i_{j+1} - i_{j-1})$.</p>
'''),
        ('Zašto se smije pretpostaviti da su barovi $1$ i $n$ otvoreni?',
         r'''
<p>Otvorimo bar $1$ uz već odabran skup. Broj gostiju dosadašnjeg prvog bara $i_1$ ostaje $i_2 - 1$ (virtualni susjed $1$ postaje pravi), ostali se ne mijenjaju, a novi bar donosi $p_1 (i_1 - 1) \ge 0$. Isto vrijedi za bar $n$. Dakle postoji optimalno rješenje s otvorenim krajevima, pa krajeve fiksiramo.</p>
'''),
        ('Kakvu geometrijsku interpretaciju ima $\sum_j p_{i_j}(i_{j+1} - i_{j-1})$ kad su krajevi otvoreni?',
         r'''
<p>Spojimo točke $(i_j, p_{i_j})$ izlomljenom linijom. Dvostruka površina ispod nje (iznad osi $x$, od $x = 1$ do $x = n$) je zbroj trapeza $\sum_j (p_{i_j} + p_{i_{j+1}})(i_{j+1} - i_j)$. Raspišemo li ga po točkama, svaki $p_{i_j}$ množi $(i_{j+1} - i_j) + (i_j - i_{j-1}) = i_{j+1} - i_{j-1}$, a krajevi $(i_2 - i_1)$ i $(i_m - i_{m-1})$ upravo odgovaraju $i_1 = 1$, $i_m = n$. Prihod je točno dvostruka površina ispod izlomljene linije.</p>
'''),
        ('Koji podskup točaka daje najveću površinu?',
         r'''
<p>Gornja konveksna ljuska. Svaka točka $(i, p_i)$ leži na ljusci ili strogo ispod nje, pa je svaka izlomljena linija kroz podskup točaka (s fiksnim krajevima) po točkama ispod ljuske — površina ispod nje nije veća. Linija kroz vrhove ljuske se poklapa s ljuskom i postiže maksimum. Točke koje leže <em>na</em> bridu ljuske možemo uključiti ili ne — površina je ista.</p>
'''),
        ('Kako izračunati gornju ljusku u linearnom vremenu i bez prelijevanja?',
         r'''
<p>Točke su već sortirane po $x$ (indeksu). Prolazimo ih redom i držimo stog: dok su zadnje dvije točke stoga $A, B$ i nova točka $C$ takve da $B$ nije strogo iznad spojnice $AC$ (vektorski produkt $(B - A) \times (C - A) \ge 0$), izbacimo $B$. Svaka točka uđe i izađe najviše jednom: $O(n)$. Vektorski produkt je reda $n \cdot 10^9 \le 5 \cdot 10^{14}$ pa stane u 64 bita; ukupni prihod je do $2 n \cdot 10^9 = 10^{15}$, također 64-bitni.</p>
'''),
    ],
    'tips': [
        r'''Prihod tipa „svatko plaća susjednim odabranim elementima” prvo zapiši kao zbroj po odabranima s doprinosom $p_{i_j}(i_{j+1} - i_{j-1})$ — takav zbroj je često trapezna formula, tj. površina ispod izlomljene linije.''',
        r'''Rubni slučajevi (prvi/posljednji odabrani) rješavaju se dodavanjem virtualnih susjeda; zatim pokaži da su rubni elementi <em>uvijek</em> u optimumu i fiksiraj ih.''',
        r'''Maksimum površine ispod linije kroz podskup točaka = gornja konveksna ljuska; minimum = donja. Kad su točke sortirane po $x$, monotoni stog daje ljusku u $O(n)$ — nema potrebe za $O(n \log n)$ sortiranjem.''',
        r'''Uz $\sum n \le 3 \cdot 10^6$ i do $10^4$ testova, koristi brzi ulaz (<code>scanf</code>/vlastiti čitač) i ne alociraj vektore iznova za svaki test bez potrebe.''',
    ],
    'solution': r'''
<p>Prema javnim analizama natjecanja AMPPZ 2022 i vlastitoj razradi. Ako su otvoreni barovi $i_1 \lt \dots \lt i_m$, bar $i_j$ ima $i_{j+1} - i_{j-1}$ gostiju uz virtualne susjede $i_0 = 1$ i $i_{m+1} = n$. Otvaranje barova $1$ i $n$ nikad ne smanjuje prihod, pa ih fiksiramo; tada je prihod $\sum_j p_{i_j}(i_{j+1} - i_{j-1})$ točno dvostruka površina ispod izlomljene linije kroz točke $(i_j, p_{i_j})$ od $x = 1$ do $x = n$. Tu površinu maksimizira gornja konveksna ljuska skupa točaka $(i, p_i)$, koju nalazimo monotonim stogom u $O(n)$; odgovor je zbroj trapeza između susjednih vrhova ljuske.</p>
''',
    'detailed': r'''
<h3>1. Formula za prihod</h3>
<p>Neka su otvoreni barovi $i_1 \lt i_2 \lt \dots \lt i_m$. Stanovnik $x$ s $i_{j-1} \le x \lt i_j$ ima bar $i_j$ kao najbliži strogo desno, a stanovnik $x$ s $i_j \lt x \le i_{j+1}$ ima ga kao najbliži strogo lijevo. Bar $i_j$ zato ima $(i_j - i_{j-1}) + (i_{j+1} - i_j) = i_{j+1} - i_{j-1}$ gostiju. Prvi bar nema lijevog susjeda: njegovi gosti su svi $x \lt i_1$ i svi $i_1 \lt x \le i_2$, dakle $i_2 - 1$; slično posljednji ima $n - i_{m-1}$. Uvedemo li virtualne susjede $i_0 = 1$ i $i_{m+1} = n$, ista formula vrijedi za sve, pa je prihod</p>
<p>$$P(i_1, \dots, i_m) = \sum_{j=1}^{m} p_{i_j}\,(i_{j+1} - i_{j-1}).$$</p>
<p>Za $m = 1$ dobivamo $p_{i_1}(n - 1)$, što je točno (svi ostali su gosti jedinog bara).</p>
<h3>2. Krajevi su uvijek otvoreni</h3>
<p>Dodajmo bar $1$ skupu u kojem ga nema. Bar $i_1$ i dalje ima $i_2 - 1$ gostiju (sada je $1$ pravi susjed umjesto virtualnog), ostali barovi ne mijenjaju susjede, a bar $1$ donosi $p_1 (i_1 - 1) \ge 0$. Prihod se ne smanjuje. Simetrično za bar $n$. Zato postoji optimalno rješenje s $i_1 = 1$ i $i_m = n$ i ubuduće to pretpostavljamo.</p>
<h3>3. Prihod kao površina</h3>
<p>Promatrajmo točke $T_j = (i_j, p_{i_j})$ i izlomljenu liniju $T_1 T_2 \dots T_m$ od $x = 1$ do $x = n$. Dvostruka površina ispod nje je zbroj trapeza $\sum_{j=1}^{m-1} (p_{i_j} + p_{i_{j+1}})(i_{j+1} - i_j)$. Skupimo članove uz svaki $p_{i_j}$: za $1 \lt j \lt m$ dobivamo $p_{i_j}\big[(i_{j+1} - i_j) + (i_j - i_{j-1})\big] = p_{i_j}(i_{j+1} - i_{j-1})$, za $j = 1$ dobivamo $p_{i_1}(i_2 - i_1) = p_{i_1}(i_2 - 1)$, a za $j = m$ dobivamo $p_{i_m}(i_m - i_{m-1}) = p_{i_m}(n - i_{m-1})$. To je upravo formula iz odjeljka 1. <strong>Prihod = dvostruka površina ispod izlomljene linije kroz odabrane točke.</strong></p>
<h3>4. Maksimum daje gornja konveksna ljuska</h3>
<p>Skup točaka $\{(i, p_i)\}$ ima gornju konveksnu ljusku $H$ (konkavna izlomljena linija od $(1, p_1)$ do $(n, p_n)$). Svaka točka skupa leži na $H$ ili strogo ispod nje. Uzmimo bilo koji podskup s fiksnim krajevima i njegovu izlomljenu liniju $L$. Svaki segment linije $L$ spaja dvije točke koje su ispod ili na $H$; kako je $H$ konkavna, i cijeli segment je ispod ili na $H$. Dakle $L \le H$ po točkama i površina ispod $L$ nije veća od površine ispod $H$. Podskup vrhova ljuske daje $L = H$, pa postiže maksimum. Točke koje leže točno na bridu ljuske možemo po volji uključiti — površina se ne mijenja, pa ih u kodu izbacujemo (uvjet $\ge 0$ na vektorskom produktu).</p>
<h3>5. Algoritam</h3>
<ol>
<li>Prođi indekse $i = 1..n$ redom i održavaj stog vrhova ljuske. Dok stog ima barem dvije točke $A$ (predzadnja) i $B$ (zadnja) i vrijedi $(B - A) \times (T_i - A) \ge 0$ (točka $B$ nije strogo iznad pravca $A T_i$), izbaci $B$. Zatim stavi $T_i$ na stog.</li>
<li>Zbroji trapeze između susjednih vrhova stoga: $\sum (p_a + p_b)(b - a)$. To je odgovor (dvostruka površina, pa nema dijeljenja).</li>
</ol>
<p>Svaka točka uđe i izađe iz stoga najviše jednom, pa je prolaz $O(n)$. Vektorski produkt $(b - a)(p_i - p_a) - (p_b - p_a)(i - a)$ ima apsolutnu vrijednost do $n \cdot 10^9 \le 5 \cdot 10^{14}$, a odgovor do $(n-1) \cdot 2 \cdot 10^9 \le 10^{15}$ — oboje stane u 64-bitni cijeli broj.</p>
<h3>6. Provjera na primjerima</h3>
<p>Za $p = (5, 2, 2, 6)$ ljuska je samo $(1,5)$–$(4,6)$: $(5+6) \cdot 3 = 33$. Za $p = (1, 5, 4, 4, 1)$ ljuska je $(1,1), (2,5), (4,4), (5,1)$; točka $(3,4)$ je ispod spojnice $(2,5)$–$(4,4)$ (na $x = 3$ spojnica ima visinu $4.5$) pa ispada. Zbroj trapeza: $6 \cdot 1 + 9 \cdot 2 + 5 \cdot 1 = 29$, kao u primjeru.</p>
<h3>7. Složenost i zamke</h3>
<p>$O(n)$ vremena i memorije po testu, ukupno $O(\sum n)$. Zamke: 64-bitna aritmetika za produkt i zbroj; uključivanje krajeva $1$ i $n$ bez obzira na $p_1, p_n$; brzi ulaz zbog $3 \cdot 10^6$ brojeva.</p>
''',
    'verified': r'''uzorak 1/1; 300 slučajnih malih testova ($n \le 10$, $p_i$ do $3$, $10$ ili $10^9$) protiv brute forcea koji ispituje sve neprazne podskupove barova i računa prihod izravno po definiciji; 3 velika testa (po $6$ skupova s $n = 500\,000$: konstantan, slučajan, konkavan, linearan i profil s malim cijenama), najsporiji $0.17$ s.''',
},
# ---------------------------------------------------------------- C
{
    'letter': 'C', 'title': 'Ctrl+C Ctrl+V', 'title_hr': 'Ctrl+C Ctrl+V', 'slug': 'C_ctrl_c_ctrl_v',
    'tl': '5 s', 'ml': '1024 MiB',
    'statement': r'''
<p>Dan je string $s$ malih engleskih slova (Anijina autobiografija). Odredi najmanji broj znakova koje treba promijeniti da $s$ više ne sadrži riječ <code>ania</code> kao podniz uzastopnih znakova.</p>
<h3>Ulaz</h3>
<p>$z \le 10\,000$ testova; svaki je jedan string duljine $l \le 10^6$; $\sum l \le 5\,000\,000$.</p>
<h3>Izlaz</h3>
<p>Za svaki test najmanji broj promjena.</p>
<h3>Primjer</h3>
<p><code>aniasieurodzilaapotemnicsieniedzialo</code> $\to 1$; <code>nicciekawegouanianiagnieszkianialicji</code> $\to 2$; <code>jeszczekrotszaautobiografiaani</code> $\to 0$.</p>
''',
    'hints': [
        r'''
<p>Svaka pojava riječi <code>ania</code> zauzima $4$ uzastopna znaka. Jedna promjena znaka „pokvari” svaku pojavu koja sadrži taj znak. Koji klasični problem to podsjeća?</p>
''',
        r'''
<p>Zamisli pojave kao intervale $[i, i+3]$ i traži najmanji broj točaka koje pogađaju sve intervale. Koja je pohlepna strategija optimalna i zašto?</p>
''',
        r'''
<p>Kad promijeniš znak, možeš li time <em>stvoriti</em> novu pojavu? Odaberi znak zamjene tako da ne možeš (npr. <code>#</code> ili bilo koje slovo koje nije u <code>ania</code>) i pazi da nova pojava ne nastane ni preklapanjem.</p>
''',
    ],
    'coach': [
        ('Kako se promjena jednog znaka odražava na pojave riječi <code>ania</code>?',
         r'''
<p>Pojava na poziciji $i$ zauzima znakove $i, i+1, i+2, i+3$. Promjena znaka $j$ uništava sve pojave s $i \le j \le i+3$ — najviše četiri. Zadatak je pogoditi svaku pojavu barem jednom promjenom, dakle „pogađanje intervala točkama” s intervalima duljine $4$.</p>
'''),
        ('Zašto je pohlepno biranje „najranijeg kraja” optimalno?',
         r'''
<p>Standardni argument zamjene: pojava koja završava najranije (kraj $e$) mora biti pogođena nekom točkom $\le e$. Svaki interval koji sadrži takvu točku sadrži i točku $e$ (intervali su duljine $4$ i završavaju najranije na $e$, pa počinju najranije... ne prije od $e - 3$, a točka $\le e$ koja ih pogađa leži u $[e-3, e]$; interval koji sadrži nju sadrži i $e$ jer završava na $\ge e$). Zato smijemo pomaknuti tu točku na $e$ bez gubitka. Ponavljamo za preostale nepogođene pojave.</p>
'''),
        ('Može li promjena znaka stvoriti novu pojavu, pa da algoritam podcijeni odgovor?',
         r'''
<p>Ako novi znak nije <code>a</code>, <code>n</code> ni <code>i</code>, nijedna pojava ne može sadržavati promijenjeni znak, pa nove pojave nema. U kodu na mjesto zadnjeg <code>a</code> pohlepno odabrane pojave stavljamo <code>#</code>; zamjena je „mehanizam brojanja”, a stvarni sadržaj zamjene u izlazu nije bitan jer se traži samo broj.</p>
'''),
        ('Kako to izvesti u jednom prolazu?',
         r'''
<p>Prolazimo $i = 3, \dots, L-1$ i provjeravamo je li $s[i-3..i]$ jednako <code>ania</code>. Ako jest, to je nepogođena pojava s najranijim krajem (sve ranije su već razriješene), pa povećamo odgovor i postavimo $s[i] = $ <code>#</code>. Time su pokvarene i sve pojave koje počinju na $i-2, i-1, i$ (one sadrže znak $i$), što je točno učinak točke na kraju intervala. Složenost $O(L)$.</p>
'''),
    ],
    'tips': [
        r'''Zadaci „najmanji broj promjena da se uzorak više ne pojavljuje” za uzorak fiksne duljine su pogađanje intervala točkama: pohlepno biraj kraj najranije završavajućeg nepogođenog intervala.''',
        r'''Pri mijenjanju znakova uvijek provjeri može li promjena stvoriti novu pojavu uzorka; biraj znak koji se ne pojavljuje u uzorku.''',
        r'''Kad je uzorak fiksan i kratak, provjera „završava li pojava na $i$” u $O(1)$ je dovoljna — nema potrebe za KMP-om.''',
    ],
    'solution': r'''
<p>Prema javnim analizama natjecanja AMPPZ 2022 i vlastitoj razradi. Svaka pojava riječi <code>ania</code> je interval od $4$ uzastopna znaka, a promjena znaka uništava sve pojave koje ga sadrže; tražimo najmanji broj točaka koje pogađaju sve intervale. Klasična pohlepa je optimalna: prođi string slijeva, i kad god $s[i-3..i]$ glasi <code>ania</code>, povećaj odgovor i zamijeni $s[i]$ znakom koji nije u uzorku (npr. <code>#</code>) — time su uništene i sve pojave koje sadrže znak $i$, a nova ne može nastati. Složenost $O(L)$.</p>
''',
    'detailed': r'''
<h3>1. Model: pogađanje intervala točkama</h3>
<p>Neka string $s$ ima duljinu $L$ i neka je $I = \{ [i, i+3] : s[i..i+3] = \text{ania} \}$ skup početnih pojava. Ako promijenimo znak na poziciji $j$ u nešto što nije slovo iz uzorka, nestaju točno pojave čiji interval sadrži $j$, a nove pojave ne nastaju (svaka pojava bi morala sadržavati znak $j$, a on nije ni <code>a</code>, ni <code>n</code>, ni <code>i</code>). Dakle nakon skupa promjena $J$ string je „čist” ako i samo ako svaki interval iz $I$ sadrži barem jednu točku iz $J$. Tražimo najmanji takav $J$: klasični problem <em>pogađanja intervala točkama</em>.</p>
<p>Bi li mogla pomoći zamjena znakom iz uzorka (npr. <code>a</code>)? Ne: svaka promjena pozicije $j$, bez obzira na novi znak, uništava sve stare pojave koje sadrže $j$, a najviše što još može učiniti jest stvoriti nove pojave, što nikad ne pomaže. Zato je optimalni broj promjena jednak optimalnom broju točaka za $I$.</p>
<h3>2. Pohlepa i njezin dokaz</h3>
<p>Algoritam: dok postoji nepogođen interval, uzmi onaj s najmanjim desnim krajem $e$ i stavi točku u $e$. Dokaz optimalnosti argumentom zamjene: u bilo kojem optimalnom rješenju interval $[e-3, e]$ pogađa neka točka $t \in [e-3, e]$. Svaki drugi interval koji sadrži $t$ završava na barem $e$ (jer $e$ je najmanji kraj), a počinje na $\le t \le e$, pa sadrži i $e$. Zamjenom $t \to e$ rješenje ostaje valjano i jednako veliko. Indukcijom po broju intervala, pohlepno rješenje ima najmanje točaka.</p>
<h3>3. Jedan prolaz</h3>
<p>Kako svi intervali imaju istu duljinu, poredak po lijevom kraju jednak je poretku po desnom. Prolazimo $i = 3, 4, \dots, L-1$:</p>
<ul>
<li>ako je $s[i-3..i] = $ <code>ania</code>, tada je to nepogođen interval s najmanjim krajem (svi raniji su već obrađeni ili pokvareni), pa: <code>++odgovor</code>, $s[i] \leftarrow$ <code>#</code>;</li>
<li>inače ništa.</li>
</ul>
<p>Postavljanje $s[i]$ na <code>#</code> automatski „pokvari” provjere za $i+1, i+2, i+3$ koje bi sadržavale taj znak — to su upravo intervali koje točka $e = i$ pogađa. Nova pojava ne može nastati jer <code>#</code> nije u uzorku.</p>
<h3>4. Primjer</h3>
<p>Za <code>aniaania</code> na $i = 3$ nalazimo pojavu, mijenjamo $s[3]$; na $i = 7$ nalazimo drugu (znakovi $4..7$ netaknuti), ukupno $2$. Za <code>aniania</code> (pojave na $0$ i $3$ se preklapaju u znaku $3$) na $i = 3$ mijenjamo $s[3]$ (zadnje <code>a</code> prve pojave, ujedno prvo <code>a</code> druge), pa druga pojava više ne postoji: odgovor $1$.</p>
<h3>5. Složenost i zamke</h3>
<p>$O(L)$ vremena i $O(1)$ dodatne memorije (rad u ulaznom spremniku). Zamke: string može biti dug (ulaz čitati odjednom, ne znak po znak s <code>cin</code>); pri provjeri koristiti indekse $i-3..i$ tako da se preklapajuće pojave ispravno ponište; ne zaboraviti da promjena nekog drugog znaka umjesto zadnjeg (npr. prvog <code>a</code>) ne bi pokvarila preklapajuću sljedeću pojavu.</p>
''',
    'verified': r'''uzorak 1/1; 300 slučajnih malih testova (nizovi duljine do $8$ nad $\{a, n, i, z\}$) protiv brute forcea koji ispituje sve nizove iste duljine nad $\{a, n, i, z\}$ bez podniza <code>ania</code> i uzima najmanju Hammingovu udaljenost (slova izvan <code>ania</code> su međusobno ravnopravna, pa jedno dodatno slovo dostaje); 3 velika testa (po $5$ nizova duljine $10^6$: <code>ania</code> u nizu, periodički <code>ani</code>, slučajni nad $\{a,n,i\}$ i nad cijelom abecedom), najsporiji $0.02$ s.''',
},
# ---------------------------------------------------------------- D
{
    'letter': 'D', 'title': 'Dazzling Mountain', 'title_hr': 'Blistava planina', 'slug': 'D_dazzling_mountain',
    'tl': '10 s', 'ml': '1024 MiB',
    'statement': r'''
<p>Na planini je $n$ planinarskih domova povezanih s $n - 1$ stazom u stablo s korijenom u domu $1$ (vrh planine). Domovi s točno jednom stazom (osim doma $1$) nalaze se u podnožju. Tradicionalni uspon počinje u nekom domu u podnožju i završava na vrhu.</p>
<p>Iz doma $x$ vide se točno domovi čiji put do $1$ prolazi kroz $x$ (uključujući $x$), tj. veličina podstabla od $x$. Uprava želi izgraditi vidikovac u svakom domu iz kojeg se vidi točno $d$ domova.</p>
<p>Nađi sve vrijednosti $d$ za koje će svaki planinar, bez obzira na to iz kojeg doma u podnožju kreće, na putu do vrha proći kroz barem jedan vidikovac.</p>
<h3>Ulaz</h3>
<p>$z \le 10\,000$ testova; $2 \le n \le 1\,000\,000$, zatim $n - 1$ bridova $a_i, b_i$; $\sum n \le 3 \cdot 10^6$.</p>
<h3>Izlaz</h3>
<p>Za svaki test dva retka: broj traženih vrijednosti $d$, pa te vrijednosti uzlazno.</p>
<h3>Primjer</h3>
<p>Stablo s $9$ vrhova i bridovima $1\text{-}2, 2\text{-}3, 3\text{-}4, 3\text{-}5, 2\text{-}6, 6\text{-}7, 7\text{-}8, 7\text{-}9$: odgovor su $4$ vrijednosti, $1\ 3\ 8\ 9$.</p>
''',
    'hints': [
        r'''
<p>Fiksiraj $d$. Vidikovci su svi vrhovi s veličinom podstabla $d$. Što treba vrijediti da svaki list (dom u podnožju) na putu do korijena prođe kroz jedan od njih?</p>
''',
        r'''
<p>Mogu li dva različita vrha iste veličine podstabla biti jedan u podstablu drugoga? Što to znači za podstabla vidikovaca za fiksni $d$?</p>
''',
        r'''
<p>Kad su podstabla disjunktna, listove koje pokrivaju možeš jednostavno zbrojiti. Zbroji broj listova po veličini podstabla i usporedi s ukupnim brojem listova.</p>
''',
    ],
    'coach': [
        ('Kad list $\ell$ prolazi kroz vidikovac $x$ na putu do vrha?',
         r'''
<p>Točno kad je $\ell$ u podstablu od $x$ (put od $\ell$ do korijena prolazi kroz sve pretke od $\ell$ i samo njih; $x$ je pretk od $\ell$ ili $\ell$ sam). Dakle $d$ je dobar ako i samo ako je svaki list sadržan u podstablu nekog vrha veličine $d$.</p>
'''),
        ('Zašto su podstabla dvaju različitih vrhova iste veličine disjunktna?',
         r'''
<p>Dva podstabla u ukorijenjenom stablu su ili disjunktna ili je jedno sadržano u drugome. Ako je podstablo od $y$ strogo sadržano u podstablu od $x$, tada je $|T_y| \lt |T_x|$ (barem $x$ nije u $T_y$). Stoga vrhovi iste veličine $d$ imaju međusobno disjunktna podstabla.</p>
'''),
        ('Kako iz disjunktnosti dobiti brz kriterij?',
         r'''
<p>Broj listova pokrivenih vidikovcima veličine $d$ jednak je $\sum_{x : |T_x| = d} \text{list}(x)$, gdje je $\text{list}(x)$ broj listova u $T_x$ — zbog disjunktnosti nema dvostrukog brojanja. Dakle $d$ je dobar ako i samo ako je taj zbroj jednak ukupnom broju listova $L$. Zbrojeve po $d$ skupimo u polje <code>pokriveno[d]</code> jednim prolazom po vrhovima.</p>
'''),
        ('Kako izračunati veličine podstabala i brojeve listova za $n$ do $10^6$ bez rekurzije?',
         r'''
<p>BFS-om od korijena dobijemo redoslijed u kojem je roditelj uvijek prije djeteta; prolazeći taj redoslijed <em>unatrag</em> dodajemo $|T_v|$ i $\text{list}(v)$ roditelju. List je vrh $\ne 1$ stupnja $1$ (i za $n = 2$ vrh $2$ je list). Sve je $O(n)$; rekurzija bi na lančastom stablu s $10^6$ vrhova preplavila stog.</p>
'''),
    ],
    'tips': [
        r'''Podstabla jednake veličine u ukorijenjenom stablu su disjunktna — koristan trik kad treba „pokrivanje po veličini podstabla” bez presjeka.''',
        r'''Za stabla s $10^6$ vrhova izbjegavaj rekurzivni DFS; BFS redoslijed pa obrada unatrag daje iste podatke iterativno.''',
        r'''Kad je $\sum n$ velik i testova mnogo, alociraj polja jednom (veličine maksimalnog $n$) i čisti samo prvih $n$ elemenata.''',
    ],
    'solution': r'''
<p>Prema javnim analizama natjecanja AMPPZ 2022 i vlastitoj razradi. Za fiksni $d$ vidikovci su vrhovi s veličinom podstabla $d$, a list prolazi kroz vidikovac $x$ točno ako je u podstablu od $x$. Podstabla različitih vrhova iste veličine su disjunktna (ugniježđena podstabla imaju različite veličine), pa je broj pokrivenih listova jednak $\sum_{|T_x| = d} \text{list}(x)$. Vrijednost $d$ je dobra ako i samo ako je taj zbroj jednak ukupnom broju listova. Veličine podstabala i brojeve listova računamo iterativno (BFS redoslijed pa prolaz unatrag), zbrojimo po veličinama i ispišemo dobre $d$ — sve u $O(n)$.</p>
''',
    'detailed': r'''
<h3>1. Prevođenje uvjeta</h3>
<p>Ukorijenimo stablo u $1$. Podstablo $T_x$ čine vrhovi čiji put do korijena prolazi kroz $x$, a $|T_x|$ je broj domova koji se vide iz $x$. Za zadani $d$ vidikovci su $V_d = \{x : |T_x| = d\}$. List (dom u podnožju) je vrh $\ell \ne 1$ stupnja $1$; njegov uspon je put $\ell \to$ roditelj $\to \dots \to 1$, tj. skup svih predaka od $\ell$ uključujući $\ell$. Put prolazi kroz $x$ ako i samo ako je $x$ pretk od $\ell$ ili $x = \ell$, što je isto kao $\ell \in T_x$. Dakle:</p>
<p><strong>$d$ je dobar $\iff$ svaki list leži u $\bigcup_{x \in V_d} T_x$.</strong></p>
<h3>2. Ključno opažanje: podstabla iste veličine su disjunktna</h3>
<p>U ukorijenjenom stablu za bilo koja dva vrha $x \ne y$ vrijedi točno jedno: $T_x \cap T_y = \emptyset$, $T_y \subsetneq T_x$ ili $T_x \subsetneq T_y$ (jer je $y \in T_x$ ekvivalentno tomu da je $x$ pretk od $y$). Ako je $T_y \subsetneq T_x$, onda $|T_y| \le |T_x| - 1$ jer $x \in T_x \setminus T_y$. Zato dva različita vrha s $|T_x| = |T_y| = d$ nužno imaju disjunktna podstabla.</p>
<h3>3. Brojanje pokrivenih listova</h3>
<p>Neka je $\text{list}(x)$ broj listova u $T_x$ i $L$ ukupan broj listova. Zbog disjunktnosti je broj listova koje pokrivaju vidikovci iz $V_d$ točno $$\text{pokriveno}[d] = \sum_{x : |T_x| = d} \text{list}(x),$$ bez ikakvog dvostrukog brojanja. Uvjet iz odjeljka 1 postaje $\text{pokriveno}[d] = L$. Primijetimo da je $\text{pokriveno}[d] \le L$ uvijek, pa je jednakost isto što i „nijedan list nije izostavljen”.</p>
<h3>4. Algoritam</h3>
<ol>
<li>Učitaj bridove, izgradi liste susjedstva (za $n$ do $10^6$ koristi CSR polja ili unaprijed alocirane vektore).</li>
<li>BFS od vrha $1$ daje redoslijed obilaska i roditelja svakog vrha; u tom redoslijedu roditelj je uvijek prije djeteta.</li>
<li>Postavi $|T_v| = 1$ za sve $v$ i $\text{list}(v) = 1$ ako je $v \ne 1$ stupnja $1$, inače $0$. Prođi BFS redoslijed unatrag i dodaj $|T_v|$ i $\text{list}(v)$ vrijednostima roditelja. Nakon toga su sve vrijednosti točne (svako dijete je obrađeno prije roditelja).</li>
<li>Za svaki $v$ dodaj $\text{list}(v)$ u $\text{pokriveno}[|T_v|]$.</li>
<li>Ispiši sve $d \in [1, n]$ s $\text{pokriveno}[d] = L$, uzlazno, s njihovim brojem.</li>
</ol>
<p>Vrijednost $d = n$ je uvijek dobra (korijen pokriva sve), a $d = 1$ također (svaki list je vidikovac). Za primjer iz zadatka ($9$ vrhova) dobivamo $d \in \{1, 3, 8, 9\}$: vrhovi veličine $3$ su $3$ (listovi $4, 5$) i $7$ (listovi $8, 9$), što pokriva sva četiri lista; veličina $2$ ima samo vrh $6$, koji pokriva $8, 9$ ali ne i $4, 5$.</p>
<h3>5. Složenost i zamke</h3>
<p>$O(n)$ vremena i memorije po testu, dakle $O(\sum n)$ ukupno. Zamke: (1) rekurzivni DFS na lančastom stablu s $10^6$ vrhova ruši stog — obrada mora biti iterativna; (2) korijen se ne smatra listom čak ni kad ima stupanj $1$ (npr. $n = 2$: jedini list je vrh $2$, a $d = 2$ je dobar jer korijen pokriva sve); (3) $z$ može biti do $10^4$, pa polja ne alociraj iznova za svaki test nego ih čisti do $n$; (4) ulaz ima do $6 \cdot 10^6$ brojeva — koristi brzi čitač.</p>
''',
    'verified': r'''uzorak 1/1; 300 slučajnih malih testova ($n \le 9$, slučajna, lančasta i duboka stabla) protiv brute forcea koji za svaki $d$ označi vidikovce i izravno provjeri put svakog lista do korijena; 3 velika testa ($n = 10^6$: slučajno, lanac, duboko stablo), najsporiji $0.60$ s.''',
},
# ---------------------------------------------------------------- E
{
    'letter': 'E', 'title': 'Euclidean Algorithm', 'title_hr': 'Euklidov algoritam', 'slug': 'E_euclidean_algorithm',
    'tl': '30 s', 'ml': '8 MiB',
    'statement': r'''
<p>„Algoritam” za $\gcd(x, y)$: na ploči su brojevi $x$ i $y$. U jednom koraku odaberi bilo koja dva već napisana broja $a$ i $b$ i napiši $c = 2a - b$, uz uvjet $c \gt 0$. Rezultat za par $(x, y)$ je najmanji broj koji se može pojaviti na ploči nakon proizvoljno mnogo (možda nula) koraka.</p>
<p>Za $(10, 14)$ algoritam daje $2$ ($2 \cdot 10 - 14 = 6$, $2 \cdot 6 - 10 = 2$), što je točno; za $(10, 16)$ daje $4$, a točan je $\gcd$ jednak $2$.</p>
<p>Za dani $n$ odredi broj parova $(x, y)$, $1 \le x \lt y \le n$, za koje algoritam vraća točno $\gcd(x, y)$. (Ako je $\gcd(x, y) = x$, algoritam radi ispravno jer je $x$ već na ploči.)</p>
<h3>Ulaz</h3>
<p>$z \ge 1$ testova, svaki je jedan broj $n \ge 2$. Ulaz pripada jednoj od tri skupine: $z \le 3000, n \le 10^6$; $z = 30, n \le 10^9$; $z = 3, n \le 10^{11}$. <strong>Memorijsko ograničenje je samo 8 MB.</strong></p>
<h3>Izlaz</h3>
<p>Za svaki test broj traženih parova.</p>
<h3>Primjer</h3>
<p>$n = 2 \to 1$; $n = 5 \to 9$; $n = 14 \to 62$.</p>
''',
    'hints': [
        r'''
<p>Koji brojevi uopće mogu nastati iz $x$ i $y$? Pogledaj sve brojeve na ploči modulo $g = y - x$ i pokaži da se dobiju točno svi pozitivni brojevi kongruentni $x$ modulo $g$.</p>
''',
        r'''
<p>Algoritam vraća ostatak $x \bmod g$ (ili $g$ ako je $0$). Kada je to jednako $\gcd(x, y)$? Zapiši $x = qg + r$ i pokaži da treba $r \mid g$. Parametriziraj sve dobre parove kao $x = d(1 + pk)$, $y = d(1 + (p+1)k)$.</p>
''',
        r'''
<p>Broj dobrih parova za fiksni $d$ je $D(\lfloor n/d \rfloor - 1)$, gdje je $D(m) = \sum_{i \le m} \lfloor m/i \rfloor$. Grupiraj $d$ po jednakom $\lfloor n/d \rfloor$; male vrijednosti $D$ izračunaj sitom broja djelitelja u segmentima (memorija!), velike formulom u $O(\sqrt m)$.</p>
''',
    ],
    'coach': [
        ('Koji se brojevi mogu pojaviti na ploči i koji je najmanji?',
         r'''
<p>Neka je $g = y - x \gt 0$. Ako su $a \equiv b \equiv x \pmod g$, onda i $2a - b \equiv x \pmod g$; indukcijom su svi brojevi na ploči kongruentni $x$ modulo $g$. Obratno, iz susjednih $a$ i $a + g$ dobivamo $2a - (a+g) = a - g$ i $2(a+g) - a = a + 2g$, pa počevši od $x, x+g$ dosežemo svaki pozitivan broj $\equiv x \pmod g$. Najmanji takav je $r = x \bmod g$ ako je $r \gt 0$, inače $g$.</p>
'''),
        ('Kad je rezultat algoritma jednak $\gcd(x, y)$?',
         r'''
<p>Vrijedi $\gcd(x, y) = \gcd(x, g)$. Ako $g \mid x$, algoritam vraća $g$, a $\gcd(x, g) = g$ — točno. Inače vraća $r = x \bmod g$ s $0 \lt r \lt g$, a $\gcd(x, g) = \gcd(r, g)$; jednakost $r = \gcd(r, g)$ znači točno $r \mid g$. Dakle: <em>algoritam je točan ako i samo ako $x \bmod g$ dijeli $g$ (uz konvenciju da $0$ „dijeli”, tj. slučaj $g \mid x$)</em>.</p>
'''),
        ('Kako prebrojati parove koji zadovoljavaju taj uvjet?',
         r'''
<p>Neka je $d = \gcd(x, y)$ i $g = dk$. Uvjet daje $x = d(1 + pk)$ i $y = x + g = d(1 + (p+1)k)$ za neke $k \ge 1$, $p \ge 0$ (slučaj $k = 1$ je $g \mid x$). Prikaz je jednoznačan: $g$ i $d$ određuju $k$, a $x$ zatim $p$. Za fiksni $d$ i $m = \lfloor n/d \rfloor$ trebamo $1 + (p+1)k \le m$, tj. broj parova $(k, q)$ s $q k \le m - 1$, $q = p+1 \ge 1$ — to je $D(m-1) = \sum_{i=1}^{m-1} \lfloor (m-1)/i \rfloor$. Odgovor je $\sum_{d=1}^{n} D(\lfloor n/d \rfloor - 1)$.</p>
'''),
        ('Zašto naivno zbrajanje ne prolazi za $n = 10^{11}$ i što ga zamjenjuje?',
         r'''
<p>Vrijednost $v = \lfloor n/d \rfloor$ poprima $O(\sqrt n)$ različitih vrijednosti; za svaki blok jednakih $v$ dodamo $(\text{broj } d) \cdot D(v-1)$. Formula $D(m) = 2\sum_{i \le \sqrt m} \lfloor m/i \rfloor - \lfloor \sqrt m \rfloor^2$ radi u $O(\sqrt m)$, ali zbroj $\sum_{d} \sqrt{n/d}$ je reda $n^{3/4} \approx 10^{8.25}$ — pregranično. Zato za $m \le T \approx n^{2/3}$ vrijednosti $D(m)$ uzimamo iz sita: $D(m) = \sum_{i \le m} \tau(i)$ gdje je $\tau$ broj djelitelja, a $D$ pozivamo za rastuće $m$. Za $m \gt T$ (samo $d \lt n/T \approx n^{1/3}$) koristimo formulu; ukupno $O(n^{2/3} \log n)$.</p>
'''),
        ('Kako sito stane u 8 MB kad je $T \approx 2 \cdot 10^7$?',
         r'''
<p>Ne čuvamo cijelo polje $\tau$: obrađujemo segmente od $2^{18}$ brojeva (polje <code>unsigned short</code>, $0.5$ MB). Za segment $[L, R)$ za svaki $i$ s $i^2 \lt R$ dodamo $2$ svakom višekratniku $m = i \cdot j$ s $j \gt i$ u segmentu (i $1$ za $m = i^2$) — tako svaki par djelitelja $(i, m/i)$ brojimo jednom. Prefiksni zbroj $\sum \tau$ održavamo tekuće dok $m$ raste, pa segmente posjećujemo redom i točno jednom.</p>
'''),
    ],
    'tips': [
        r'''Kod operacija tipa $2a - b$ (refleksija) prvo gledaj invarijantu modulo razlike početnih brojeva — često skup dosežnih vrijednosti postaje cijela aritmetička progresija.''',
        r'''Zbroj $\sum_{d \le n} f(\lfloor n/d \rfloor)$ računaj po blokovima jednakih kvocijenata ($O(\sqrt n)$ blokova); ako je $f$ i sama „teška”, male argumente predračunaj sitom, velike formulom — prag $n^{2/3}$ balansira ukupno vrijeme.''',
        r'''Kad je memorija stroga, sito radi segmentirano: dovoljno je da se argumenti obrađuju monotono, pa jedan prozor prolazi kroz cijeli raspon.''',
        r'''Odgovor može prijeći $2^{63}$? Ovdje je $\le \binom{n}{2} \lt 5 \cdot 10^{21}$ za $n = 10^{11}$ — no zapravo dobrih parova je znatno manje ($\approx 0.5\,n \ln^2 n$), pa <code>unsigned long long</code> dostaje; provjeri to procjenom prije predaje.''',
    ],
    'solution': r'''
<p>Prema javnim analizama natjecanja AMPPZ 2022 i vlastitoj razradi. Uz $g = y - x$ svi brojevi na ploči kongruentni su $x$ modulo $g$ i svaki pozitivan takav broj se može dobiti, pa algoritam vraća $x \bmod g$ (ili $g$). To je jednako $\gcd(x, y)$ točno kad $x \bmod g$ dijeli $g$, tj. kad je $x = d(1 + pk)$, $y = d(1 + (p+1)k)$ za $d, k \ge 1$, $p \ge 0$ (jednoznačno). Za fiksni $d$ dobrih parova je $D(\lfloor n/d \rfloor - 1)$, gdje je $D(m) = \sum_{i \le m} \lfloor m/i \rfloor$ djeliteljska sumatorna funkcija. Zbrajamo po blokovima jednakih $\lfloor n/d \rfloor$; $D(m)$ za $m \le T \approx n^{2/3}$ uzimamo kao prefiksni zbroj broja djelitelja iz segmentiranog sita (zbog 8 MB), a za veće $m$ formulom u $O(\sqrt m)$. Ukupno $O(n^{2/3} \log n)$, što za $n = 10^{11}$ traje ispod sekunde.</p>
''',
    'detailed': r'''
<h3>1. Što algoritam zapravo računa</h3>
<p>Neka je $g = y - x \gt 0$. Tvrdnja: skup brojeva koji se mogu pojaviti na ploči je točno $\{c \gt 0 : c \equiv x \pmod g\}$.</p>
<p><em>Nužnost.</em> Početno su $x \equiv y \equiv x \pmod g$. Ako su $a \equiv b \equiv x$, onda $2a - b \equiv 2x - x = x \pmod g$. Indukcijom po broju koraka svi zapisani brojevi su $\equiv x \pmod g$.</p>
<p><em>Dostatnost.</em> Ako su $a$ i $a + g$ na ploči, dobivamo $2a - (a + g) = a - g$ (ako je pozitivan) i $2(a + g) - a = a + 2g$; sada su $a - g$ i $a$ susjedni, kao i $a + g$ i $a + 2g$, pa indukcijom dolazimo do svakog pozitivnog člana progresije $x + tg$, $t \in \mathbb{Z}$.</p>
<p>Najmanji pozitivni broj $\equiv x \pmod g$ je $r = x \bmod g$ ako je $r \gt 0$, a $g$ ako $g \mid x$. To je rezultat „algoritma”.</p>
<h3>2. Kad je rezultat točan</h3>
<p>Vrijedi $\gcd(x, y) = \gcd(x, y - x) = \gcd(x, g)$.</p>
<ul>
<li>Ako $g \mid x$: rezultat je $g$, a $\gcd(x, g) = g$. Točno.</li>
<li>Inače $x = qg + r$ s $0 \lt r \lt g$, rezultat je $r$, a $\gcd(x, g) = \gcd(r, g)$. Jednakost $r = \gcd(r, g)$ vrijedi točno kad $r \mid g$.</li>
</ul>
<p>Objedinimo: neka je $d = \gcd(x, y)$ i $g = dk$, $k \ge 1$. U prvom slučaju $k = 1$ (jer je $d = g$) i $x = d(1 + p)$ za $p = x/d - 1 \ge 0$. U drugom slučaju $r = d$ (jer $r \mid g$ i $r \mid x$ daje $r \mid \gcd = d$, a $d \mid r$ jer $d \mid x$ i $d \mid g$), pa $x = qg + d = d(1 + qk)$ s $k = g/d \ge 2$ (jer $r \lt g$). U oba slučaja:</p>
<p>$$x = d\,(1 + pk), \qquad y = x + g = d\,(1 + (p+1)k), \qquad d \ge 1,\; k \ge 1,\; p \ge 0.$$</p>
<p>Obratno, svaki takav par je dobar: $g = dk$, $x \bmod g = d$ (za $k \ge 2$) ili $0$ (za $k = 1$), a $\gcd(x, y) = d \gcd(1 + pk, 1 + (p+1)k) = d \gcd(1 + pk, k) = d$. Prikaz je jednoznačan jer $d = \gcd(x,y)$ i $g$ određuju $k$, a onda $x$ određuje $p$. Provjera na primjeru: $(10, 14)$ je $d = 2, k = 2, p = 2$; $(10, 16)$ ima $g = 6, d = 2, k = 3$, ali $x/d = 5 = 1 + pk$ nema rješenja — nije dobar, kao u zadatku.</p>
<h3>3. Brojanje</h3>
<p>Za fiksni $d$ neka je $m = \lfloor n/d \rfloor$. Uvjet $y \le n$ glasi $1 + (p+1)k \le m$, tj. $qk \le m - 1$ uz $q = p + 1 \ge 1$, $k \ge 1$ ($x \lt y$ je automatski). Broj takvih parova $(k, q)$ je</p>
<p>$$D(m-1), \qquad D(M) = \sum_{i=1}^{M} \left\lfloor \frac{M}{i} \right\rfloor = \sum_{i=1}^{M} \tau(i),$$</p>
<p>gdje je $\tau(i)$ broj djelitelja. Odgovor je $\sum_{d=1}^{n} D(\lfloor n/d \rfloor - 1)$. Za $n = 5$: $d = 1$ daje $D(4) = 8$, $d = 2$ daje $D(1) = 1$, ostali $D(0) = 0$; ukupno $9$ — točno.</p>
<h3>4. Brzo računanje za $n \le 10^{11}$</h3>
<p><strong>Blokovi kvocijenata.</strong> $\lfloor n/d \rfloor$ poprima najviše $2\sqrt n$ različitih vrijednosti; za blok $d \in [d_{lo}, d_{hi}]$ s istim $v$ dodamo $(d_{hi} - d_{lo} + 1) \cdot D(v - 1)$. Blokove prolazimo od velikih $d$ (mali $v$) prema malima, pa argumenti $D$ rastu.</p>
<p><strong>Dvije metode za $D$.</strong> Formula $D(M) = 2\sum_{i=1}^{s} \lfloor M/i \rfloor - s^2$, $s = \lfloor \sqrt M \rfloor$ (simetrija hiperbole $ij \le M$), stoji $O(\sqrt M)$. Kad bismo je zvali za sve blokove, trošak bi bio $\sum_d \sqrt{n/d} \approx 2 n^{3/4}$, previše za $n = 10^{11}$. Zato uvedemo prag $T = \lfloor n^{1/3} \rfloor^2 \approx n^{2/3}$: za $M \le T$ vrijednost $D(M) = \sum_{i \le M} \tau(i)$ čitamo kao prefiksni zbroj iz sita, a formulu zovemo samo za $M \gt T$, što se događa jedino za $d \lt n/T \approx n^{1/3}$; trošak formule je $\sum_{d \le n^{1/3}} \sqrt{n/d} = O(n^{1/2} \cdot n^{1/6}) = O(n^{2/3})$. Sito do $T$ stoji $O(T \log T)$. Ukupno $O(n^{2/3} \log n) \approx 2 \cdot 10^7 \cdot 17$ operacija za najveći test.</p>
<p><strong>Segmentirano sito (8 MB).</strong> Polje $\tau$ do $2 \cdot 10^7$ ne stane u memoriju ako je 32-bitno i sve se čuva. Zato držimo samo prozor $[L, L + 2^{18})$ kao <code>unsigned short</code> ($\tau(i) \lt 2^{16}$ za $i \le 10^{11}$) i tekući prefiksni zbroj. Prozor punimo tako da za svaki $i$ s $i^2 \lt R$ obiđemo višekratnike $m = i j \ge i^2$ u prozoru i dodamo $2$ (par djelitelja $i$ i $j \gt i$) odnosno $1$ za $m = i^2$. Kako $D$ pozivamo s nepadajućim argumentom, prozor se pomiče samo udesno i svaki segment obrađujemo jednom.</p>
<h3>5. Složenost i zamke</h3>
<p>Vrijeme $O(n^{2/3} \log n)$ po testu; memorija $\approx 0.5$ MB. Za skupinu $z \le 3000$, $n \le 10^6$ trošak je $\approx 3000 \cdot 10^4 \cdot \log$ — u redu. Zamke: (1) $\lfloor \sqrt M \rfloor$ računati cjelobrojno s korekcijom, ne pouzdati se u <code>sqrt</code> za $M \approx 10^{11}$; (2) odgovor premašuje 32 bita (za $n = 10^{11}$ reda je $10^{13}$), pa koristi 64-bitni tip; (3) $D(0) = 0$ za $v = 1$ (tj. $d \gt n/2$); (4) prag $T$ ne smije biti veći od $n$.</p>
''',
    'verified': r'''uzorak 1/1 ($n = 2, 5, 14$); 300 slučajnih malih testova ($n \le 40$) protiv brute forcea koji za svaki par BFS-om po ploči izravno računa najmanji dosežni broj i uspoređuje ga s $\gcd$; formula $\sum_d D(\lfloor n/d\rfloor - 1)$ dodatno uspoređena s neovisnom implementacijom u Pythonu za $n \le 10^{5}$; 3 velika testa ($n \approx 10^{11}$), najsporiji $0.86$ s uz sito od $0.5$ MB.''',
},
# ---------------------------------------------------------------- F
{
    'letter': 'F', 'title': 'Flower Garden', 'title_hr': 'Cvjetni vrt', 'slug': 'F_flower_garden',
    'tl': '30 s', 'ml': '1024 MiB',
    'statement': r'''
<p>U red od $3n$ gredica sade se ljubičice (F) i ruže (R). Kraljevski dekret ima $q$ uvjeta; $i$-ti glasi: <em>barem jedno</em> od sljedećeg vrijedi — sve gredice $a_i..b_i$ su ruže, ili sve gredice $c_i..d_i$ su ljubičice. Na raspolaganju je $2n$ ruža i $2n$ ljubičica (pa nijedne vrste ne smije biti više od $2n$).</p>
<p>Nađi raspored koji zadovoljava sve uvjete ili utvrdi da ne postoji.</p>
<h3>Ulaz</h3>
<p>$z \le 10^5$ testova; $1 \le n \le 33\,333$, $1 \le q \le 10^5$, zatim $q$ četvorki $a_i \le b_i$, $c_i \le d_i$ iz $[1, 3n]$; $\sum n \le 333\,333$, $\sum q \le 10^6$.</p>
<h3>Izlaz</h3>
<p>Za svaki test <code>TAK</code> i u sljedećem retku string duljine $3n$ od znakova <code>F</code>/<code>R</code> (najviše $2n$ svakog), ili <code>NIE</code>.</p>
<h3>Primjer</h3>
<p>$n = 1$, uvjeti $(1,1,2,2), (1,2,3,3), (1,1,3,3)$: <code>TAK</code>, <code>RFF</code>. $n = 1$, uvjeti $(1,1,2,2), (2,2,3,3), (3,3,1,1)$: <code>NIE</code>.</p>
''',
    'hints': [
        r'''
<p>Uvedi za svaku gredicu $p$ logičku varijablu $x_p$ = „na $p$ je ljubičica”. Kako se uvjet „sve u $[a,b]$ ruže ILI sve u $[c,d]$ ljubičice” zapisuje kao implikacija među tim varijablama?</p>
''',
        r'''
<p>Uvjet je $x_p \Rightarrow x_q$ za sve $p \in [a,b]$, $q \in [c,d]$ — to je $O(n^2)$ bridova po uvjetu. Kako s dva segmentna stabla (jedno „ulazno”, jedno „izlazno”) i pomoćnim vrhom dobiti $O(\log n)$ bridova po uvjetu?</p>
''',
        r'''
<p>Skup ljubičica mora biti zatvoren prema sljedbenicima u grafu implikacija, a veličine mu je u $[n, 2n]$. Sažmi graf u jako povezane komponente (težina komponente = broj gredica u njoj) i traži zatvoren skup komponenti odgovarajuće težine.</p>
''',
    ],
    'coach': [
        ('Kako se dekret prevodi u implikacije i što je „rješenje” u tom jeziku?',
         r'''
<p>Uvjet „$[a,b]$ sve ruže ili $[c,d]$ sve ljubičice” je ekvivalentan: <em>ako je bilo koja gredica $p \in [a,b]$ ljubičica, onda su sve gredice $q \in [c,d]$ ljubičice</em>, tj. $x_p \Rightarrow x_q$ za sve takve $p, q$. Raspored je valjan ako i samo ako skup $F$ ljubičica ne krši nijednu implikaciju, tj. $F$ je <strong>zatvoren prema sljedbenicima</strong> u usmjerenom grafu implikacija. Ograničenje na broj cvjetova ($\le 2n$ svake vrste od ukupno $3n$) daje $n \le |F| \le 2n$.</p>
'''),
        ('Kako izbjeći $O(|[a,b]| \cdot |[c,d]|)$ bridova po uvjetu?',
         r'''
<p>Standardni trik sa segmentnim stablima. <em>Ulazno</em> stablo ima bridove dijete $\to$ roditelj, pa se iz gredice $p$ dolazi do svakog čvora čiji segment sadrži $p$. <em>Izlazno</em> stablo ima bridove roditelj $\to$ dijete, pa se iz čvora dolazi do svih gredica njegova segmenta. Za uvjet dodamo pomoćni vrh $h$: bridovi iz $O(\log n)$ ulaznih čvorova koji rastavljaju $[a,b]$ u $h$, i iz $h$ u $O(\log n)$ izlaznih čvorova koji rastavljaju $[c,d]$. Put $p \to \dots \to h \to \dots \to q$ postoji točno za $p \in [a,b]$, $q \in [c,d]$. Ukupno $O(n + q \log n)$ bridova.</p>
'''),
        ('Zašto sažimanje u jako povezane komponente i što je težina komponente?',
         r'''
<p>Ako su $x_p$ i $x_q$ u istoj jako povezanoj komponenti, $p \in F \iff q \in F$. Zatvoreni skupovi su zato unije cijelih komponenti, zatvorene prema sljedbenicima u kondenzaciji (DAG-u). Težina komponente je broj <em>gredica</em> u njoj (čvorovi stabala i pomoćni vrhovi ne nose cvjetove, težina $0$). Tražimo zatvoren skup komponenti ukupne težine u $[n, 2n]$.</p>
'''),
        ('Kako naći zatvoren skup težine u $[n, 2n]$?',
         r'''
<p>Dva slučaja. (1) Postoji komponenta težine $\ge n$ (najviše tri takve): njezino zatvaranje (sve dosežne komponente) izračunamo DFS-om; ako mu je težina $\le 2n$, to je rješenje. (2) Inače svaka komponenta koja se smije uzeti ima težinu $\lt n$; komponente iz kojih se dosegne neka „velika” komponenta su zabranjene (njihovo zatvaranje bi imalo težinu $\gt 2n$, jer bi inače slučaj (1) uspio). Preostale komponente dodajemo u obrnutom topološkom redu (ponori prvi) — svaki prefiks tog niza je zatvoren skup — dok težina ne dosegne $n$; kako svaki korak dodaje $\lt n$, težina u tom trenutku ne premašuje $2n$. Ako ukupna dopuštena težina ne dosegne $n$, odgovor je <code>NIE</code>.</p>
'''),
        ('Zašto <code>NIE</code> u tom slučaju zaista znači da rješenja nema?',
         r'''
<p>Svako rješenje $F$ je zatvoren skup težine u $[n, 2n]$. Sadrži li $F$ veliku komponentu, sadrži i njezino zatvaranje, pa bi ono imalo težinu $\le 2n$ i slučaj (1) bi ga našao. Inače $F$ ne sadrži nijednu veliku komponentu ni komponentu koja do velike vodi (zatvorenost), pa se sastoji samo od dopuštenih komponenti, čija je ukupna težina stoga $\ge |F| \ge n$ — i pohlepno dodavanje uspijeva. Dakle, algoritam ne uspijeva samo kad rješenja nema.</p>
'''),
    ],
    'tips': [
        r'''Uvjet oblika „(sve u $A$ imaju svojstvo $0$) ILI (sve u $B$ imaju svojstvo $1$)” je skup implikacija $A \Rightarrow B$; kad su $A$ i $B$ intervali, graf gradi preko ulaznog i izlaznog segmentnog stabla s pomoćnim vrhom po uvjetu.''',
        r'''Rješenja monotone implikacijske strukture su zatvoreni skupovi; nakon kondenzacije u SCC-ove svaki prefiks obrnutog topološkog reda (koji Tarjanov algoritam daje besplatno) je zatvoren skup.''',
        r'''Kad ukupna težina treba pasti u interval širine $\ge$ najveće „nedjeljive” težine, pohlepno dodavanje po komadima automatski pogađa interval — provjeri samo komade veće od širine posebno.''',
        r'''Tarjanov algoritam za graf s $\sim 10^6$ vrhova piši iterativno (vlastiti stog) — rekurzija ruši stog.''',
    ],
    'solution': r'''
<p>Prema javnim analizama natjecanja AMPPZ 2022 i vlastitoj razradi. Neka je $x_p$ istina ako je na gredici $p$ ljubičica. Uvjet „$[a,b]$ sve ruže ili $[c,d]$ sve ljubičice” je skup implikacija $x_p \Rightarrow x_q$ za $p \in [a,b]$, $q \in [c,d]$, pa je raspored valjan ako i samo ako je skup ljubičica zatvoren prema sljedbenicima u grafu implikacija i ima veličinu u $[n, 2n]$. Graf gradimo s $O((n + q)\log n)$ bridova pomoću ulaznog i izlaznog segmentnog stabla i pomoćnog vrha po uvjetu, sažmemo ga u jako povezane komponente (iterativni Tarjan) i svakoj damo težinu = broj gredica. Ako neka komponenta težine $\ge n$ ima zatvaranje težine $\le 2n$, to je odgovor; inače zabranimo komponente iz kojih se dosegne komponenta težine $\ge n$ i preostale dodajemo u obrnutom topološkom redu dok težina ne dosegne $n$ (svaki korak dodaje $\lt n$, pa ne prelazimo $2n$). Ako to ne uspije, rješenja nema.</p>
''',
    'detailed': r'''
<h3>1. Logički model</h3>
<p>Gredice numeriramo $1..N$, $N = 3n$, i uvedemo $x_p \in \{0, 1\}$: $x_p = 1$ znači ljubičica (F), $x_p = 0$ ruža (R). Uvjet $i$ glasi $(\forall p \in [a_i, b_i]: x_p = 0) \lor (\forall q \in [c_i, d_i]: x_q = 1)$. Negiramo li prvi disjunkt, dobivamo ekvivalentan zapis: $(\exists p \in [a_i,b_i]: x_p = 1) \Rightarrow (\forall q \in [c_i,d_i]: x_q = 1)$, tj. skup implikacija $x_p \Rightarrow x_q$ za sve $p \in [a_i, b_i]$, $q \in [c_i, d_i]$. Neka je $G$ usmjereni graf na gredicama s tim bridovima. Skup ljubičica $F = \{p : x_p = 1\}$ zadovoljava sve uvjete ako i samo ako je <strong>zatvoren prema sljedbenicima</strong>: $p \in F$ i $p \to q$ povlači $q \in F$. Uz to je $|F| \le 2n$ (ljubičice) i $N - |F| \le 2n$ (ruže), tj. $n \le |F| \le 2n$.</p>
<p>Uočimo posebne slučajeve: ako se $[a_i,b_i]$ i $[c_i,d_i]$ sijeku, gredica $p$ u presjeku ima brid $p \to p$ (bezopasno) i implikacije prema ostatku $[c_i, d_i]$; sve je pokriveno općim modelom.</p>
<h3>2. Sažeta gradnja grafa</h3>
<p>Izravnih bridova je do $|[a,b]| \cdot |[c,d]|$, previše. Dodajemo dva segmentna stabla nad $[1, N]$ čiji su listovi upravo gredice:</p>
<ul>
<li><em>ulazno</em> stablo IN: brid iz svakog čvora u njegova roditelja. Iz gredice $p$ se tako dosežu točno čvorovi čiji segment sadrži $p$;</li>
<li><em>izlazno</em> stablo OUT: brid iz svakog čvora u oba djeteta. Iz čvora se dosežu točno gredice njegova segmenta.</li>
</ul>
<p>Za uvjet $i$ dodamo pomoćni vrh $h_i$, bridove iz $O(\log N)$ IN-čvorova koji rastavljaju $[a_i, b_i]$ u $h_i$ te iz $h_i$ u $O(\log N)$ OUT-čvorova koji rastavljaju $[c_i, d_i]$. Tada postoji put $p \leadsto q$ kroz $h_i$ ako i samo ako $p \in [a_i, b_i]$ i $q \in [c_i, d_i]$; putovi kroz stabla bez pomoćnih vrhova vode samo iz gredice u IN-čvorove ili iz OUT-čvorova u gredice, pa ne stvaraju lažne implikacije među gredicama. Graf ima $O(N + q)$ vrhova i $O(N + q \log N)$ bridova; za $N = 10^5$, $q = 10^5$ to je oko $4 \cdot 10^6$ bridova.</p>
<p>Zatvorenost skupa $F$ prema sljedbenicima u novom grafu prevodimo ovako: proširimo $F$ svim čvorovima dosežnim iz gredica u $F$; to proširenje ne dodaje nove <em>gredice</em> točno kad je $F$ zatvoren u $G$. Zato ubuduće radimo s proširenim skupovima i brojimo samo gredice.</p>
<h3>3. Jako povezane komponente i težine</h3>
<p>Ako su dva vrha u istoj jako povezanoj komponenti (SCC), u zatvorenom skupu su ili oba ili nijedan. Kondenzacija je DAG; zatvoreni skupovi su točno unije komponenti zatvorene prema sljedbenicima u DAG-u. Težina $w(C)$ komponente $C$ je broj gredica u njoj; čvorovi stabala i pomoćni vrhovi imaju težinu $0$. Tražimo zatvoren skup komponenti $S$ s $n \le w(S) \le 2n$.</p>
<p>Komponente računamo iterativnim Tarjanovim algoritmom (vlastiti stog umjesto rekurzije zbog $\sim 10^6$ vrhova); on komponente ispisuje u <em>obrnutom topološkom redu</em> — komponenta dobije indeks tek nakon što su svi njezini sljedbenici već dobili manji indeks.</p>
<h3>4. Traženje zatvorenog skupa težine u $[n, 2n]$</h3>
<p><strong>Slučaj 1: „velike” komponente.</strong> Komponenta je velika ako je $w(C) \ge n$; kako je $\sum w = 3n$, velikih je najviše tri. Za svaku veliku $C$ DFS-om po kondenzaciji izračunamo zatvaranje $\mathrm{cl}(C)$ (sve dosežne komponente) i njegovu težinu; ako je $\le 2n$, skup $\mathrm{cl}(C)$ je zatvoren i težine u $[n, 2n]$ — rješenje.</p>
<p><strong>Slučaj 2: sve velike komponente imaju zatvaranje težine $\gt 2n$.</strong> Tada nijedna velika komponenta ne može biti u rješenju, kao ni komponenta iz koje se velika dosegne (zatvoren skup koji je sadrži sadržavao bi i zatvaranje velike). Označimo takve komponente <em>zabranjenima</em>: prolazeći komponente u Tarjanovu redu (ponori prvi), komponenta je zabranjena ako je velika ili ima zabranjenog sljedbenika. Preostale, <em>dopuštene</em>, komponente imaju $w \lt n$, a svi njihovi sljedbenici su dopušteni. Dodajemo ih u Tarjanovu redu: prefiks tog niza je zatvoren skup, jer su sljedbenici svake komponente ranije u redu i dopušteni. Zbrajamo težine dok zbroj ne dosegne $n$; kako je prije toga zbroj $\lt n$ i dodajemo $\lt n$, završni zbroj je $\lt 2n$. Ako je ukupna težina dopuštenih komponenti $\lt n$, ispisujemo <code>NIE</code>.</p>
<p><strong>Točnost odgovora <code>NIE</code>.</strong> Neka postoji valjan raspored $F$; on je zatvoren skup težine u $[n, 2n]$. Ako $F$ sadrži veliku komponentu $C$, sadrži i $\mathrm{cl}(C)$, pa je $w(\mathrm{cl}(C)) \le w(F) \le 2n$ i slučaj 1 bi našao rješenje. Inače $F$ ne sadrži nijednu zabranjenu komponentu, pa je $F$ unija dopuštenih komponenti i njihova ukupna težina je barem $w(F) \ge n$ — slučaj 2 uspijeva. Algoritam dakle vraća <code>NIE</code> samo kad rješenja nema.</p>
<h3>5. Ispis</h3>
<p>Gredice u odabranim komponentama dobivaju <code>F</code>, ostale <code>R</code>. Zatvorenost jamči sve uvjete, a težina u $[n, 2n]$ jamči da nijedne vrste nije više od $2n$.</p>
<h3>6. Složenost i zamke</h3>
<p>Vrijeme i memorija $O(N + q \log N)$ po testu; ukupno uz $\sum n \le 333\,333$ i $\sum q \le 10^6$ oko $4 \cdot 10^7$ bridova, što se izvodi u pola sekunde uz pažljivu (CSR ili unaprijed rezervirane vektore) reprezentaciju. Zamke: (1) rekurzivni Tarjan ruši stog; (2) težine treba pripisati samo listovima-gredicama, ne unutarnjim čvorovima; (3) za $n = 1$ imamo $N = 3$ i granica $[1, 2]$ — algoritam radi i tada; (4) granični slučaj kad je zatvaranje velike komponente točno $2n$ ili točno $n$ je dopušten; (5) veliki ulaz ($\sum q$ četvorki) zahtijeva brzi čitač.</p>
''',
    'verified': r'''uzorak 1/1 (odgovori se provjeravaju validatorom <code>check.py</code>: dopušteni znakovi, duljina $3n$, najviše $2n$ svake vrste, svaki uvjet ispunjen; za <code>NIE</code> se zahtijeva da ni brute force nema rješenja); 300 slučajnih malih testova ($n \le 3$, $q \le 6$) protiv brute forcea koji ispituje sve $2^{3n}$ rasporede; 3 velika testa ($n = 33\,333$, $q = 10^5$, mješavina kratkih i dugih intervala), najsporiji $0.54$ s.''',
},
# ---------------------------------------------------------------- G
{
    'letter': 'G', 'title': 'Great Chase', 'title_hr': 'Velika potjera', 'slug': 'G_great_chase',
    'tl': '5 s', 'ml': '1024 MiB',
    'statement': r'''
<p>Na brojevnom pravcu razbojnik stoji u $0$, a $n$ policajaca s obje njegove strane (barem jedan na svakoj). Svaki policajac trči prema razbojniku svojom brzinom $v_i$; razbojnik bježi brzinom $v$ većom od svih $v_i$, početno udesno. Kad god razbojnik dođe do prvog policajca koji mu trči ususret, trenutno se okreće i trči u suprotnom smjeru. To se ponavlja dok se dva policajca iz suprotnih smjerova ne sretnu s razbojnikom između njih.</p>
<p>Odredi ukupni put koji razbojnik prijeđe.</p>
<h3>Ulaz</h3>
<p>$z \le 10\,000$ testova; $2 \le n \le 400\,000$, $1 \lt v \le 10^6$, zatim $n$ parova $p_i$ ($|p_i| \le 10^{12}$, $p_i \ne 0$) i $v_i$ ($1 \le v_i \lt v$); $\sum n \le 2 \cdot 10^6$.</p>
<h3>Izlaz</h3>
<p>Za svaki test realan broj (decimalni zapis, ne znanstveni, najviše $20$ decimala); prihvaća se relativna ili apsolutna greška do $10^{-8}$, tj. $\frac{|a - b|}{\max(1, b)} \le 10^{-8}$.</p>
<h3>Primjer</h3>
<p>$v = 9$, policajci $(10, 2), (-7, 2), (-6, 1), (7, 1)$: $38.25$. $v = 8$, policajci $(-1, 7), (1, 6)$: $1.23076923$. $v = 3$, policajci $(-10^{12}, 1), (10^{12}, 1)$: $3\,000\,000\,000\,000$ (zbog relativne greške prihvaća se svaki odgovor unutar $30\,000$).</p>
''',
    'hints': [
        r'''
<p>Razbojnik je brži od svih policajaca i mijenja smjer trenutno, pa cijelo vrijeme trči brzinom $v$. Što onda određuje ukupni put — treba li uopće simulirati okretanja?</p>
''',
        r'''
<p>Potjera završava kad se najbliži lijevi i najbliži desni policajac sretnu. Lijeva „fronta” je $L(t) = \max_i (p_i + v_i t)$ po lijevim policajcima, desna $R(t) = \min_j (p_j - v_j t)$ po desnima. Kakvog su oblika te funkcije i koliko rješenja ima $L(t) = R(t)$?</p>
''',
        r'''
<p>$L$ raste, $R$ pada, pa je $L(t) \lt R(t)$ monotono svojstvo u $t$. Binarno pretraži prvi trenutak $T$ u kojem više ne vrijedi i ispiši $v \cdot T$; pazi na preciznost ($10^{-8}$ relativno) i koristi <code>long double</code>.</p>
''',
    ],
    'coach': [
        ('Trebamo li simulirati svako okretanje razbojnika?',
         r'''
<p>Ne. Razbojnik trči brzinom $v$ bez prekida — okret je trenutan — pa je prijeđeni put jednostavno $v \cdot T$, gdje je $T$ trenutak završetka potjere. Smjerovi i broj okreta ne utječu na duljinu puta. Preostaje odrediti $T$.</p>
'''),
        ('Kad potjera završava i zašto to ne ovisi o razbojnikovoj putanji?',
         r'''
<p>Razbojnik je brži od svih policajaca, kreće iz $0$ između njih i okreće se kad dođe do policajca, pa je stalno strogo između najbližeg lijevog i najbližeg desnog policajca (nikad ih ne može „prestići”, jer se okreće čim ih dotakne). Potjera završava točno kad se ti dvoje sretnu, tj. u najranijem trenutku $T$ s $L(T) \ge R(T)$, gdje je $L(t) = \max_{p_i \lt 0}(p_i + v_i t)$ položaj najdesnijeg lijevog policajca, a $R(t) = \min_{p_j \gt 0}(p_j - v_j t)$ položaj najljevijeg desnog. Tko je „najbliži” može se mijenjati kroz vrijeme (brži sustižu sporije), ali maksimum i minimum to automatski prate.</p>
'''),
        ('Zašto je $T$ jednoznačan i kako ga pronaći?',
         r'''
<p>$L$ je maksimum rastućih linearnih funkcija — strogo rastuća; $R$ je minimum padajućih — strogo padajuća. Zato je $L(t) \lt R(t)$ istina na $[0, T)$ i laž nakon $T$: monotono svojstvo. Binarnim pretraživanjem po $t$ s provjerom u $O(n)$ nalazimo $T$. Gornja granica: razmak je $\le 2 \cdot 10^{12}$, a brzine $\ge 1$, pa je $T \le 2 \cdot 10^{12}$ (do tada se sretnu i najsporiji par).</p>
'''),
        ('Kolika je preciznost potrebna i kako je postići?',
         r'''
<p>Traži se relativna/apsolutna greška $10^{-8}$. Sa $100$ iteracija binarnog pretraživanja interval širine $2 \cdot 10^{12}$ pada daleko ispod strojne preciznosti; preciznost je ograničena tipom — <code>long double</code> (64-bitna mantisa, relativna greška $\sim 10^{-19}$) je sasvim dovoljan; s <code>double</code> ($\sim 10^{-16}$) bi također prošlo, ali margina je manja jer $p_i v_i$ za $t \approx 10^{12}$ daje vrijednosti reda $10^{18}$. Odgovor ispisujemo u decimalnom zapisu s npr. $9$ decimala (ne znanstveno).</p>
'''),
        ('Može li se $T$ izračunati i egzaktno, bez binarnog pretraživanja?',
         r'''
<p>Da: $L(t) \ge R(t)$ vrijedi točno kad postoji par (lijevi $i$, desni $j$) s $p_i + v_i t \ge p_j - v_j t$, pa je $T = \min_{i,j} \frac{p_j - p_i}{v_i + v_j}$. To je $O(n^2)$ parova — koristimo ga u brute forceu s egzaktnim razlomcima; za $n$ do $4 \cdot 10^5$ binarno pretraživanje s $O(n \log)$ je jednostavnije od geometrijskih trikova.</p>
'''),
    ],
    'tips': [
        r'''Kad se objekt giba konstantnom brzinom s trenutnim okretima, ukupni put je brzina puta trajanje — ne simuliraj putanju, odredi samo trenutak završetka.''',
        r'''Događaj „dva skupa se sretnu” često je presjek strogo rastuće i strogo padajuće funkcije: binarno pretraživanje po vremenu s $O(n)$ provjerom.''',
        r'''Za brojeve reda $10^{12} \cdot 10^6 = 10^{18}$ u realnoj aritmetici koristi <code>long double</code> i fiksan broj iteracija (npr. $100$) umjesto uvjeta na epsilon.''',
        r'''Ako zadatak traži zapis bez eksponenta, ispiši s <code>%.9Lf</code>/<code>fixed</code>; znanstveni zapis se ne prihvaća.''',
    ],
    'solution': r'''
<p>Prema javnim analizama natjecanja AMPPZ 2022 i vlastitoj razradi. Razbojnik cijelo vrijeme trči brzinom $v$ (okreti su trenutni), pa je put $v \cdot T$, gdje je $T$ trenutak završetka. Budući da je brži od svih, uvijek je između najbližeg lijevog i najbližeg desnog policajca, pa potjera završava kad se sretnu lijeva fronta $L(t) = \max_{p_i \lt 0}(p_i + v_i t)$ i desna fronta $R(t) = \min_{p_j \gt 0}(p_j - v_j t)$. $L$ strogo raste, $R$ strogo pada, pa je $T$ jedinstven i nalazimo ga binarnim pretraživanjem po $t \in [0, 2 \cdot 10^{12}]$ s provjerom $L(t) \lt R(t)$ u $O(n)$; $100$ iteracija u <code>long double</code> daje traženu preciznost. Ispis $v \cdot T$ u decimalnom zapisu.</p>
''',
    'detailed': r'''
<h3>1. Put ne ovisi o putanji</h3>
<p>Razbojnik trči brzinom $v$ od početka do kraja potjere, a okret pri susretu s policajcem je trenutan. Prijeđeni put je zato $v \cdot T$, gdje je $T$ trajanje potjere. Broj i mjesta okreta su za odgovor nebitni; sve što treba jest $T$.</p>
<h3>2. Kada potjera završava</h3>
<p>Podijelimo policajce na lijeve ($p_i \lt 0$, trče udesno) i desne ($p_j \gt 0$, trče ulijevo); po uvjetu zadatka svaka skupina je neprazna. Definirajmo $L(t) = \max_{i \text{ lijevi}} (p_i + v_i t)$ i $R(t) = \min_{j \text{ desni}} (p_j - v_j t)$ — položaje najbližeg lijevog i najbližeg desnog policajca u trenutku $t$ (tko je najbliži može se mijenjati; maksimum i minimum to obuhvaćaju).</p>
<p>Tvrdnja: razbojnik je u svakom trenutku $t \lt T$ strogo unutar $(L(t), R(t))$, gdje je $T$ prvi trenutak s $L(T) = R(T)$. Doista, na početku je $L(0) \lt 0 \lt R(0)$. Razbojnik mijenja smjer točno kad dođe do policajca koji mu trči ususret, a tada se odmah udaljava od njega brzinom $v \gt v_i$, pa ga taj policajac više ne dostiže; policajac s druge strane prilazi, ali razbojnik ga „dotakne” tek kad do njega dođe i opet se okrene. Dakle nikad ne izlazi izvan $(L, R)$, a kad se $L$ i $R$ sretnu, sretnu se s razbojnikom između njih — točno kraj potjere iz zadatka. Stoga je $T$ najmanje $t \ge 0$ s $L(t) \ge R(t)$.</p>
<h3>3. Jedinstvenost i monotonost</h3>
<p>$L$ je maksimum konačno mnogo strogo rastućih linearnih funkcija, pa je strogo rastuća (i konveksna); $R$ je minimum strogo padajućih, pa je strogo padajuća (i konkavna). Razlika $R - L$ strogo pada, pozitivna je u $0$, a negativna za velike $t$, pa ima točno jednu nultočku $T$. Predikat „$L(t) \lt R(t)$” vrijedi točno na $[0, T)$ — idealan za binarno pretraživanje.</p>
<h3>4. Algoritam</h3>
<ol>
<li>Učitaj policajce, razdvoji ih po znaku $p_i$.</li>
<li>Postavi $lo = 0$, $hi = 2 \cdot 10^{12}$. Gornja granica je sigurna: razmak bilo kojeg lijevog i desnog policajca je $\le 2 \cdot 10^{12}$, a približavaju se brzinom $v_i + v_j \ge 2$, pa se sretnu najkasnije u $t = 10^{12}$.</li>
<li>Ponavljaj $100$ puta: $mid = (lo + hi)/2$; izračunaj $L(mid)$ i $R(mid)$ u $O(n)$; ako je $L \lt R$, $lo = mid$, inače $hi = mid$.</li>
<li>Ispiši $v \cdot lo$ s fiksnim brojem decimala.</li>
</ol>
<p>Egzaktna alternativa: $L(t) \ge R(t)$ vrijedi točno kad postoji par $(i, j)$ s $p_i + v_i t \ge p_j - v_j t$, tj. $t \ge \frac{p_j - p_i}{v_i + v_j}$, pa je $T = \min_{i,j} \frac{p_j - p_i}{v_i + v_j}$. To je $O(n^2)$ i služi kao neovisna provjera (brute force s razlomcima), dok je binarno pretraživanje $O(n \log(\text{raspon}/\varepsilon))$.</p>
<h3>5. Preciznost</h3>
<p>Traži se $\frac{|a - b|}{\max(1, b)} \le 10^{-8}$. Vrijednosti $p_i + v_i t$ za $t \le 2 \cdot 10^{12}$ i $v_i \lt 10^6$ su reda $10^{18}$; u <code>long double</code> (64-bitna mantisa) relativna pogreška jednog izračuna je $\sim 5 \cdot 10^{-20}$, što je apsolutno $\sim 10^{-1}$ na skali $10^{18}$, ali presudno je da se pogreška u $T$ prenosi relativno: za $T \ge 1$ relativna greška ostaje $\ll 10^{-8}$. Nakon $100$ polovljenja interval je širine $2 \cdot 10^{12} / 2^{100} \approx 10^{-18}$, pa binarno pretraživanje ne ograničava preciznost. Za primjer $v = 3$, $p = \pm 10^{12}$, $v_i = 1$: $T = 10^{12}$, odgovor $3 \cdot 10^{12}$, točno kao u zadatku.</p>
<h3>6. Složenost i zamke</h3>
<p>$O(100 \cdot n)$ po testu, tj. $O(\sum n)$ s malom konstantom; memorija $O(n)$. Zamke: (1) ne miješati lijeve i desne policajce — policajac s $p_i \lt 0$ trči <em>udesno</em>; (2) ispis mora biti u decimalnom zapisu (npr. <code>%.9Lf</code>), ne znanstvenom; (3) $v$ i $p_i$ treba čitati u 64-bitne tipove ($|p_i| \le 10^{12}$); (4) ne prekidati binarno pretraživanje uvjetom $hi - lo \lt \varepsilon$ s apsolutnim $\varepsilon$ — pri $10^{12}$ to može zakazati; fiksan broj iteracija je sigurniji.</p>
''',
    'verified': r'''uzorak 1/1 (odgovore uspoređuje <code>check.py</code> s tolerancijom $10^{-8}$ relativno/apsolutno); 300 slučajnih malih testova ($n \le 7$, položaji do $10^{12}$, brzine do $10^6$) protiv brute forcea koji trenutak susreta računa egzaktno u razlomcima kao $\min_{i,j} (p_j - p_i)/(v_i + v_j)$; 3 velika testa ($5$ testova po $n = 400\,000$ u svakom), najsporiji $0.73$ s.''',
},
# ---------------------------------------------------------------- H
{
    'letter': 'H', 'title': 'Hyperloop', 'title_hr': 'Hyperloop', 'slug': 'H_hyperloop',
    'tl': '45 s', 'ml': '64 MiB',
    'statement': r'''
<p>Na obali otoka leži $n$ gradova $1, 2, \dots, n$ redom. Trajekti voze između $i$ i $i+1$ te između $n$ i $1$; uz to postoje Hyperloop veze između nekih parova nesusjednih gradova. Sve su veze dvosmjerne s trajanjem $d_i$ i tretiraju se jednako.</p>
<p>Traži se najkraći put od $1$ do $n$. Među najkraćim putovima preferiraju se oni s <em>najduljim</em> pojedinačnim vezama: za svaki put ispiši duljine njegovih veza (s ponavljanjima), sortiraj nerastuće i odaberi leksikografski najveći niz. (Nizovi imaju isti zbroj, pa nijedan nije prefiks drugoga.)</p>
<p><strong>Memorijsko ograničenje je samo 64 MB.</strong></p>
<h3>Ulaz</h3>
<p>$z \le 600$ testova; $3 \le n \le 100\,000$, $n \le m \le 300\,000$, zatim $m$ veza $u_i, v_i, d_i$ ($1 \le d_i \le 50\,000$), među kojima su sigurno $(1,2), (2,3), \dots, (n,1)$; između para gradova najviše jedna veza. $\sum n \le 400\,000$, $\sum m \le 800\,000$.</p>
<h3>Izlaz</h3>
<p>Za svaki test broj gradova $k$ na optimalnom putu, pa $k$ različitih gradova redom od $1$ do $n$. Ako ima više optimalnih putova, bilo koji.</p>
<h3>Primjer</h3>
<p>$n = 4$, veze $(1,2,1), (1,3,2), (2,3,1), (2,4,2), (3,4,1), (1,4,4)$: najkraća udaljenost je $3$, postižu je $1 \to 2 \to 4$, $1 \to 3 \to 4$ i $1 \to 2 \to 3 \to 4$; prva dva su bolja jer je $(2,1) \gt (1,1,1)$. Odgovor npr. <code>3</code>, <code>1 2 4</code>. U drugom primjeru ($n = 6$, $m = 11$) odgovor je <code>5</code>, <code>1 2 5 3 6</code> jer je $(9, 8, 2, 1) \gt (9, 5, 3, 2, 1)$.</p>
''',
    'hints': [
        r'''
<p>Prvo Dijkstra od grada $1$. Koje veze uopće mogu biti na najkraćem putu? Zadrži samo bridove $(u, v, d)$ s $\mathrm{dist}[u] + d = \mathrm{dist}[v]$ — dobivaš DAG najkraćih putova.</p>
''',
        r'''
<p>Kako se uspoređuju dva nerastuće sortirana niza jednakog zbroja? Pokaži da je to isto što i usporedba brojača po težinama od najveće težine nadolje, i da dodavanje istog elementa oba niza ne mijenja ishod usporedbe — pa vrijedi optimalna podstruktura na DAG-u.</p>
''',
        r'''
<p>Multiskup duljina za svaki vrh čuvaj u perzistentnom segmentnom stablu po težinama $1..50\,000$ s 64-bitnim hashom po čvoru: usporedba dvaju multiskupova je spust do najveće težine na kojoj se hashevi razlikuju, $O(\log W)$. Stvaraj nove čvorove samo za pobjednički brid svakog vrha — memorija je 64 MB.</p>
''',
    ],
    'coach': [
        ('Kako svesti problem na DAG?',
         r'''
<p>Dijkstrom od $1$ izračunamo $\mathrm{dist}$. Put $1 \to n$ je najkraći ako i samo ako za svaki njegov brid $(u, v, d)$ vrijedi $\mathrm{dist}[u] + d = \mathrm{dist}[v]$ (zbroj takvih jednakosti daje $\mathrm{dist}[n]$; obrnuto, svaki brid najkraćeg puta je „napet”). Zadržimo samo napete bridove: to je DAG (udaljenost strogo raste), a svaki put $1 \to n$ u njemu je najkraći put i svaki najkraći put je u njemu.</p>
'''),
        ('Što točno znači „leksikografski najveći nerastuće sortirani niz” i zašto je usporediv preko brojača?',
         r'''
<p>Za multiskup $M$ neka je $c_M(w)$ broj elemenata težine $w$. Sortirani nerastući nizovi $A \gt B$ (istog zbroja) točno kad na najvećoj težini $w$ s $c_A(w) \ne c_B(w)$ vrijedi $c_A(w) \gt c_B(w)$: sve veće težine se podudaraju, pa se nizovi podudaraju do pozicije na kojoj $A$ ima $w$, a $B$ nešto manje. Ključno svojstvo: <strong>dodavanje istog elementa $d$ u oba multiskupa ne mijenja ishod</strong> (brojači se promijene jednako). Zato ako je $M_1 \ge M_2$, i $M_1 \cup \{d\} \ge M_2 \cup \{d\}$.</p>
'''),
        ('Zašto onda vrijedi dinamičko programiranje po DAG-u?',
         r'''
<p>Neka je $\mathrm{best}[v]$ najveći multiskup među svim putovima $1 \leadsto v$ u DAG-u. Optimalni put do $v$ završava bridom $(u, v, d)$; kad bi njegov prefiks do $u$ bio lošiji od $\mathrm{best}[u]$, zamjena prefiksa bi (po svojstvu iz prethodnog koraka) dala bolji put do $v$. Dakle $\mathrm{best}[v] = \max_{(u,v,d)} \big(\mathrm{best}[u] \cup \{d\}\big)$, obrađujući vrhove po rastućoj udaljenosti. Pamtimo i pobjednički prethodnik za ispis puta.</p>
'''),
        ('Kako usporediti multiskupove brzo i u malo memorije?',
         r'''
<p>Multiskup prikazujemo perzistentnim segmentnim stablom nad težinama $1..W$ ($W = 50\,000$); svaki čvor čuva 64-bitni hash $\sum_w c(w)\, r_w$ sa slučajnim $r_w$. Dva multiskupa uspoređujemo spustom: ako se hashevi podstabala podudaraju, tu nema razlike; inače najprije u desno (veće težine) dijete. Najveća težina s različitim brojačem nađe se u $O(\log W)$, a brojači se pročitaju spustom. Usporedba $\mathrm{best}[u] \cup \{d_1\}$ s $\mathrm{best}[u'] \cup \{d_2\}$ radi se bez stvaranja čvorova (dodani elementi se uračunaju „virtualno”), a novih $O(\log W)$ čvorova stvaramo samo za pobjednički brid. To je $\approx n \log W \approx 1.7 \cdot 10^6$ čvorova po $16$ B, oko $27$ MB.</p>
'''),
        ('Koje su zamke s memorijom i hashiranjem?',
         r'''
<p>Kad bismo stvarali čvorove za svaki od $m$ DAG-bridova, bilo bi ih $3\times$ više i memorija bi pukla; zato prvo usporedimo, pa umetnemo. Hash kolizija bi dala krivu odluku; s 64-bitnim slučajnim vrijednostima vjerojatnost je zanemariva ($\sim 2^{-64}$ po usporedbi). Testova je do $600$, pa spremnik čvorova praznimo između testova, a graf držimo u CSR poljima.</p>
'''),
    ],
    'tips': [
        r'''„Među najkraćim putovima onaj s najboljim X” gotovo uvijek znači: Dijkstra, zatim DAG napetih bridova, zatim DP po DAG-u — provjeri samo da X ima optimalnu podstrukturu (dodavanje istog brida ne mijenja usporedbu).''',
        r'''Leksikografska usporedba sortiranih nizova jednakog zbroja svodi se na usporedbu multiskupova „od najveće težine nadolje”; multiskupove drži u perzistentnom segmentnom stablu s hashevima da usporedba bude $O(\log W)$.''',
        r'''Kad je memorijsko ograničenje strogo, ne materijaliziraj kandidate — usporedi ih virtualno, a strukturu proširi samo za pobjednika.''',
    ],
    'solution': r'''
<p>Prema javnim analizama natjecanja AMPPZ 2022 i vlastitoj razradi. Dijkstrom od $1$ dobijemo $\mathrm{dist}$ i zadržimo samo napete bridove $\mathrm{dist}[u] + d = \mathrm{dist}[v]$ — DAG svih najkraćih putova. Nerastuće sortirane nizove jednakog zbroja uspoređujemo po brojačima težina od najveće nadolje; dodavanje istog elementa ne mijenja ishod, pa vrijedi DP po DAG-u: $\mathrm{best}[v] = \max_{(u,v,d)} (\mathrm{best}[u] \cup \{d\})$ po rastućoj udaljenosti. Multiskupove čuvamo u perzistentnom segmentnom stablu po težinama $1..50\,000$ s 64-bitnim hashevima; usporedba dvaju kandidata je spust do najveće težine na kojoj se hashevi razlikuju, $O(\log W)$, bez stvaranja čvorova, a novih $O(\log W)$ čvorova dodajemo samo za pobjednički brid svakog vrha ($\approx 27$ MB). Put rekonstruiramo po pobjedničkim prethodnicima.</p>
''',
    'detailed': r'''
<h3>1. DAG najkraćih putova</h3>
<p>Neka je $\mathrm{dist}[v]$ najkraća udaljenost od $1$ (Dijkstra, $O(m \log n)$). Brid $(u, v, d)$ je <em>napet</em> ako $\mathrm{dist}[u] + d = \mathrm{dist}[v]$. Za put $1 = x_0, x_1, \dots, x_k = n$ duljine $\sum d_i$ vrijedi $\mathrm{dist}[x_{i}] \le \mathrm{dist}[x_{i-1}] + d_i$ za sve $i$; zbrojimo li, put je najkraći točno kad su sve nejednakosti jednakosti, tj. kad su svi bridovi napeti. Graf napetih bridova (usmjerenih od manjeg $\mathrm{dist}$ prema većem) je acikličan jer $\mathrm{dist}$ strogo raste ($d \ge 1$), a njegovi putovi $1 \leadsto n$ su točno najkraći putovi. Vrhovi nedosežni iz $1$ u DAG-u nas ne zanimaju; svaki vrh dosežan u DAG-u posjetit ćemo po rastućoj udaljenosti (Dijkstrin redoslijed).</p>
<h3>2. Usporedba nizova = usporedba brojača</h3>
<p>Za multiskup $M$ pozitivnih težina i $w \in [1, W]$ neka je $c_M(w)$ broj elemenata težine $w$. Neka su $A, B$ multiskupovi jednakog zbroja i $s_A, s_B$ njihovi nerastuće sortirani nizovi.</p>
<p><em>Lema 1.</em> $s_A \gt s_B$ leksikografski $\iff$ postoji $w$ s $c_A(w) \gt c_B(w)$ i $c_A(w') = c_B(w')$ za sve $w' \gt w$. Dokaz: neka je $w$ najveća težina s različitim brojačima (postoji, jer bi inače $A = B$). Elementi veći od $w$ su isti u oba niza i čine zajednički prefiks. Odmah nakon prefiksa oba niza imaju blok težine $w$: $A$ dulji ako je $c_A(w) \gt c_B(w)$, pa na prvoj poziciji razlike $A$ ima $w$, a $B$ nešto $\lt w$ ili ništa; kako su zbrojevi jednaki, $B$ ne može biti prefiks od $A$, pa $s_B$ tu ima element $\lt w$. Dakle $s_A \gt s_B$. Obrat analogno.</p>
<p><em>Lema 2.</em> Ako $A \ge B$ (u gornjem smislu) onda $A \cup \{d\} \ge B \cup \{d\}$. Dokaz: dodavanje $d$ povećava $c_A(d)$ i $c_B(d)$ za $1$, pa se skup težina na kojima se brojači razlikuju i predznaci razlika ne mijenjaju.</p>
<h3>3. Dinamičko programiranje</h3>
<p>Neka je $\mathrm{best}[v]$ najveći multiskup duljina među svim putovima $1 \leadsto v$ u DAG-u, $\mathrm{best}[1] = \emptyset$. Tvrdimo $\mathrm{best}[v] = \max_{(u, v, d) \text{ napet}} \big(\mathrm{best}[u] \cup \{d\}\big)$. Naime, optimalni put do $v$ ima zadnji brid $(u, v, d)$; njegov prefiks $P$ do $u$ zadovoljava $P \le \mathrm{best}[u]$, pa po Lemi 2 $P \cup \{d\} \le \mathrm{best}[u] \cup \{d\}$, a desna strana je također ostvariva putem. Vrhove obrađujemo po rastućem $\mathrm{dist}$ (svi prethodnici imaju manji $\mathrm{dist}$) i za svaki pamtimo pobjednički prethodnik $\mathrm{prev}[v]$; odgovor rekonstruiramo od $n$ unatrag. Svi multiskupovi kandidata za isti $v$ imaju jednak zbroj $\mathrm{dist}[v]$, pa je usporedba iz Leme 1 primjenjiva.</p>
<h3>4. Perzistentno segmentno stablo s hashevima</h3>
<p>Multiskup prikazujemo verzijom perzistentnog segmentnog stabla nad $[1, W]$, $W = 50\,000$. Čvor čuva indekse djece i 64-bitni hash $h = \sum_{w \in \text{segment}} c(w)\, r_w \pmod{2^{64}}$ sa slučajnim 64-bitnim $r_w$. Umetanje elementa $d$ stvara novi put od korijena do lista $d$ ($\lceil \log_2 W \rceil + 1 = 17$ čvorova) i ostale čvorove dijeli s prethodnom verzijom. Brojač $c(w)$ se čita spustom do lista (hash lista je $c(w) r_w$, a čuvamo i brojač preko polja <code>l</code> u listu).</p>
<p><strong>Razlika.</strong> Funkcija $\mathrm{razlika}(a, b, [lo, hi])$ vraća najveću težinu u $[lo, hi]$ na kojoj se verzije $a$ i $b$ razlikuju: ako su indeksi čvorova jednaki ili se hashevi podudaraju (i segment je unutar $[lo, hi]$), razlike nema; inače se spuštamo najprije u desno dijete. Zbog hasheva se svaki spust „zaustavlja” na jednakim podstablima, pa je trošak $O(\log W)$.</p>
<p><strong>Usporedba kandidata</strong> $\mathrm{best}[u] \cup \{d_1\}$ i $\mathrm{best}[u'] \cup \{d_2\}$ radi se bez umetanja: uz $d_1 \ge d_2$ redom provjeravamo područje težina $\gt d_1$ (tu dodani elementi ne utječu), zatim težinu $d_1$ (brojač prvog je uvećan za $1$), zatim područje $(d_2, d_1)$, težinu $d_2$ (brojač drugog uvećan za $1$) i konačno područje $\lt d_2$; prva pronađena razlika određuje ishod. To je nekoliko poziva razlike i brojača, ukupno $O(\log W)$.</p>
<h3>5. Memorija</h3>
<p>Kad bismo umetali $d$ za svaki napeti brid, čvorova bi bilo do $m \cdot 17 \approx 5 \cdot 10^6$ ($\approx 80$ MB) — previše za 64 MB. Zato za svaki vrh prvo virtualno usporedimo sve ulazne kandidate i tek pobjednika umetnemo: $n \cdot 17 \approx 1.7 \cdot 10^6$ čvorova po $16$ B $\approx 27$ MB. Uz graf u CSR obliku i Dijkstrine strukture izmjereno je $\approx 44$ MB. Između testova spremnik čvorova praznimo (ne dealociramo), a slučajne težine $r_w$ generiramo jednom.</p>
<h3>6. Složenost i točnost</h3>
<p>Dijkstra $O(m \log n)$; DP $O(m \log W)$ usporedbi i $O(n \log W)$ novih čvorova; ukupno uz $\sum m \le 8 \cdot 10^5$ ispod pola sekunde. Točnost ovisi o hashu: kriva odluka zahtijeva koliziju dviju različitih 64-bitnih vrijednosti, vjerojatnost po usporedbi je $2^{-64}$, ukupno zanemarivo. Zamke: (1) ispisati broj gradova $k$ i zatim put od $1$ do $n$ (rekonstrukcija unatrag pa obrat); (2) ne zaboraviti da su trajekti $(i, i+1)$ i $(n, 1)$ obični bridovi — graf je povezan; (3) $d_i$ do $50\,000$ i $\mathrm{dist}$ do $5 \cdot 10^9$ — 64-bitni tip za udaljenosti; (4) čuvati indekse čvorova u 32 bita, a ne pokazivače, zbog memorije.</p>
''',
    'verified': r'''uzorak 1/1 (odgovor provjerava <code>check.py</code>: valjan put $1 \to n$ bez ponavljanja gradova, minimalna duljina i sortirani niz duljina jednak nizu koji daje brute force); 300 slučajnih malih testova ($n \le 7$, $m \le n + 5$, težine do $4$) protiv brute forcea koji nabraja sve jednostavne putove; 3 velika testa ($n = 10^5$, $m = 3 \cdot 10^5$: slučajne težine do $50\,000$, težine $\{1,2,3\}$ s mnogo jednakih najkraćih putova, izabrane težine), najsporiji $0.31$ s, vršna memorija $\approx 44$ MB.''',
},
# ---------------------------------------------------------------- I
{
    'letter': 'I', 'title': 'Investors', 'title_hr': 'Investitori', 'slug': 'I_investors',
    'tl': '8 s', 'ml': '1024 MiB',
    'statement': r'''
<p>Financijski rezultati su niz $a_1, \dots, a_n$. Jedna operacija: odaberi neprazan uzastopni interval niza i sve njegove članove uvećaj za isti pozitivan cijeli broj (u različitim operacijama različiti brojevi). Smiješ izvesti najviše $k$ operacija.</p>
<p>Minimiziraj broj inverzija (parova $i \lt j$ s $a_i \gt a_j$) u konačnom nizu.</p>
<h3>Ulaz</h3>
<p>$z \le 400$ testova; $1 \le n \le 6000$, $0 \le k \le n$, $0 \le a_i \le 10^9$; $\sum n \le 6000$.</p>
<h3>Izlaz</h3>
<p>Za svaki test najmanji mogući broj inverzija.</p>
<h3>Primjer</h3>
<p>$a = (4, 5, 6, 2, 2, 1)$: za $k = 1$ odgovor je $2$, za $k = 2$ odgovor je $0$.</p>
''',
    'hints': [
        r'''
<p>Što se dogodi s brojem inverzija ako operaciju na intervalu $[l, r]$ proširiš do kraja niza, na $[l, n]$? Usporedi parove po tome gdje su im indeksi u odnosu na $l$ i $r$.</p>
''',
        r'''
<p>Ako su sve operacije sufiksi, konačni prirast je nepadajuća stepenasta funkcija s najviše $k$ skokova — niz je podijeljen u najviše $k+1$ blokova. Što možeš postići s jako velikim skokovima i zašto ne možeš bolje?</p>
''',
        r'''
<p>Ostaje: podijeli niz na $\min(k+1, n)$ blokova tako da je zbroj inverzija <em>unutar</em> blokova najmanji. Cijena bloka zadovoljava nejednakost četverokuta, pa DP po slojevima ide u $O(n \log n)$ po sloju s optimizacijom „podijeli pa vladaj”; inverzije svih intervala predračunaj u $O(n^2)$.</p>
''',
    ],
    'coach': [
        ('Zašto smijemo pretpostaviti da je svaka operacija sufiks niza?',
         r'''
<p>Uzmimo operaciju $+t$ na $[l, r]$ s $r \lt n$ i proširimo je na $[l, n]$: elementi na $(r, n]$ dodatno dobiju $+t$. Parovi $i \lt j$ s oba indeksa unutar $(r, n]$ ili oba izvan ostaju isti. Parovi $i \in [l, r]$, $j \gt r$: oba su sada uvećana za $t$, relativni poredak nepromijenjen. Parovi $i \lt l$, $j \gt r$: $a_j$ raste, $a_i$ ne — inverzija može samo nestati. Dakle proširenje nikad ne povećava broj inverzija, pa postoji optimalno rješenje u kojem su sve operacije sufiksi.</p>
'''),
        ('Što točno mogu $k$ sufiksnih operacija i koja je donja granica?',
         r'''
<p>Sufiksi $[l_1, n], \dots, [l_k, n]$ dijele niz na najviše $k+1$ blokova; unutar bloka svi elementi dobiju isti prirast, pa inverzije unutar bloka ostaju točno one iz $a$. Zato je broj inverzija barem zbroj inverzija unutar blokova. Obratno, odaberemo li ogromne, međusobno različite priraste (npr. $t_j = j \cdot 10^{10}$), svaki element kasnijeg bloka veći je od svakog elementa ranijeg bloka pa među blokovima nema inverzija i donja granica se postiže. Odgovor je dakle najmanji zbroj unutarblokovskih inverzija po podjelama na $\le k+1$ blokova — a jednako je uzeti točno $K = \min(k+1, n)$ blokova jer cijepanje bloka nikad ne škodi.</p>
'''),
        ('Kako računati DP dovoljno brzo za $n = 6000$?',
         r'''
<p>Neka je $\mathrm{inv}(l, r)$ broj inverzija u $a_l..a_r$; sve vrijednosti dobijemo u $O(n^2)$ iz $\mathrm{inv}(l, r) = \mathrm{inv}(l, r-1) + \#\{i \in [l, r-1] : a_i \gt a_r\}$ (brojač koji se smanjujući $l$ inkrementalno ažurira). DP: $f_j(i) = \min_{p \lt i} f_{j-1}(p) + \mathrm{inv}(p+1, i)$ za $j = 1..K$. Naivno je $O(K n^2)$, previše za $K \approx n$.</p>
'''),
        ('Zašto vrijedi optimizacija „podijeli pa vladaj” i kolika je složenost?',
         r'''
<p>Za $a \le b \le c \le d$: $\mathrm{inv}(a, d) + \mathrm{inv}(b, c) - \mathrm{inv}(a, c) - \mathrm{inv}(b, d) = \#\{(i, j) : i \in [a, b), j \in (c, d], a_i \gt a_j\} \ge 0$, tj. cijena zadovoljava nejednakost četverokuta (Mongeovo svojstvo). Tada je optimalna točka prijelaza $\mathrm{opt}_j(i)$ nepadajuća u $i$, pa sloj $j$ računamo rekurzivno: za srednji $i$ nađemo optimum linearno, a lijevoj/desnoj polovici ograničimo raspon kandidata. Sloj stoji $O(n \log n)$, ukupno $O(K n \log n) \le 6000^2 \cdot 13 \approx 4.7 \cdot 10^8$ jednostavnih operacija, uz tablicu inverzija od $(n+1)^2$ 32-bitnih brojeva ($\approx 144$ MB, dopušteno je 1024 MB).</p>
'''),
    ],
    'tips': [
        r'''Kad operacija „dodaj konstantu na interval” smije biti proizvoljno velika, pitaj se može li se interval proširiti bez štete — često optimalna rješenja koriste samo prefikse/sufikse i problem postaje podjela na blokove.''',
        r'''Cijene oblika „broj parova unutar intervala s nekim svojstvom” zadovoljavaju nejednakost četverokuta; za DP „podijeli niz na $K$ blokova” to daje $O(K n \log n)$ optimizacijom podijeli pa vladaj (ili $O(n^2)$ Knuthovom).''',
        r'''Tablicu $\mathrm{inv}(l, r)$ za $n = 6000$ drži kao jednodimenzionalno polje 32-bitnih brojeva (do $\binom{6000}{2} \lt 2 \cdot 10^7$) — $144$ MB umjesto $288$ MB s 64-bitnim tipom.''',
    ],
    'solution': r'''
<p>Prema javnim analizama natjecanja AMPPZ 2022 i vlastitoj razradi. Proširenje operacije s $[l, r]$ na $[l, n]$ nikad ne povećava broj inverzija (parovi unutar sufiksa i parovi koji ga ne diraju ostaju isti, a parovi „lijevo–sufiks” mogu samo izgubiti inverziju), pa postoji optimalno rješenje sa samo sufiksnim operacijama. One dijele niz na najviše $k+1$ blokova; s ogromnim različitim prirastima nestaju sve inverzije među blokovima, dok inverzije unutar blokova ostaju. Odgovor je zato najmanji zbroj inverzija unutar blokova pri podjeli na $K = \min(k+1, n)$ blokova. Predračunamo $\mathrm{inv}(l, r)$ za sve intervale u $O(n^2)$; cijena zadovoljava nejednakost četverokuta, pa DP $f_j(i) = \min_p f_{j-1}(p) + \mathrm{inv}(p+1, i)$ računamo optimizacijom „podijeli pa vladaj” u $O(K n \log n)$.</p>
''',
    'detailed': r'''
<h3>1. Svaka operacija smije biti sufiks</h3>
<p>Neka rješenje sadrži operaciju $+t$ ($t \gt 0$) na intervalu $[l, r]$, $r \lt n$. Zamijenimo je operacijom $+t$ na $[l, n]$; jedina razlika je da elementi na pozicijama $(r, n]$ dobiju dodatnih $+t$. Pogledajmo svaki par $i \lt j$ u konačnom nizu:</p>
<ul>
<li>$i, j \le r$ ili $i, j \gt r$: obje vrijednosti se mijenjaju jednako (za $0$ odnosno $t$), pa inverzija ostaje kakva je bila;</li>
<li>$l \le i \le r \lt j$: element $i$ je već dobio $+t$ u izvornoj operaciji, a sada ga dobiva i $j$ — razlika $a_i - a_j$ vraća se na onu bez ove operacije, tj. obje se strane pomaknu jednako; poredak je isti kao da operacije nema, a to je isto što i s izvornom operacijom (obje su tada uvećane za $t$). Inverzija nepromijenjena;</li>
<li>$i \lt l$, $j \gt r$: $a_j$ raste, $a_i$ ne — inverzija $a_i \gt a_j$ može samo nestati.</li>
</ul>
<p>Broj inverzija se ne povećava, a broj operacija ostaje isti. Ponavljanjem za sve operacije dobivamo optimalno rješenje u kojem je svaka operacija sufiks $[l, n]$.</p>
<h3>2. Svođenje na podjelu u blokove</h3>
<p>Uz $k' \le k$ sufiksnih operacija s lijevim krajevima $l_1 \le \dots \le l_{k'}$ konačni prirast $f(i) = \sum_{j : l_j \le i} t_j$ je nepadajuća stepenasta funkcija konstantna na najviše $k' + 1$ blokova (maksimalnih intervala s istim $f$). Inverzije unutar bloka su točno inverzije izvornog niza na tom intervalu (svi elementi pomaknuti jednako). Zato je za svaku takvu operaciju konačni broj inverzija $\ge \sum_{\text{blokovi}} \mathrm{inv}(\text{blok})$.</p>
<p>Obratno, za bilo koju podjelu na $K \le k+1$ blokova odaberimo priraste $t_j = j \cdot 10^{10}$ (različiti pozitivni cijeli brojevi, kako zadatak dopušta). Element bloka $q$ tada ima vrijednost u $[c_q, c_q + 10^9]$ s $c_q = \sum_{j \lt q} t_j$, a $c_{q+1} - c_q = q \cdot 10^{10} \gt 10^9$, pa je svaki element kasnijeg bloka strogo veći od svakog elementa ranijeg — među blokovima nema inverzija. Donja granica se postiže. Zaključno:</p>
<p>$$\text{odgovor} = \min_{\text{podjela na} \le k+1 \text{ blokova}} \sum_{\text{blok } [l, r]} \mathrm{inv}(l, r).$$</p>
<p>Cijepanje bloka na dva ne povećava zbroj (gubimo parove preko reza), pa je optimalno koristiti točno $K = \min(k+1, n)$ nepraznih blokova; za $K = n$ odgovor je $0$.</p>
<h3>3. Predračun inverzija po intervalima</h3>
<p>Za fiksni desni kraj $r$ spuštamo $l$ od $r - 1$ do $1$ i održavamo $c = \#\{i \in [l, r-1] : a_i \gt a_r\}$; tada $\mathrm{inv}(l, r) = \mathrm{inv}(l, r-1) + c$. Ukupno $O(n^2)$ vremena i $(n+1)^2$ 32-bitnih vrijednosti ($\mathrm{inv} \le \binom{6000}{2} \lt 1.8 \cdot 10^7$ stane u <code>int</code>), tj. oko $144$ MB — unutar ograničenja od 1024 MB. Tablicu držimo kao jednodimenzionalno polje s indeksom $l(n+1) + r$ zbog brzine pristupa.</p>
<h3>4. Dinamičko programiranje s optimizacijom „podijeli pa vladaj”</h3>
<p>Neka je $f_j(i)$ najmanji zbroj cijena za prefiks $a_1..a_i$ podijeljen na točno $j$ blokova: $f_0(0) = 0$, $f_j(i) = \min_{j-1 \le p \lt i} f_{j-1}(p) + \mathrm{inv}(p+1, i)$. Odgovor je $f_K(n)$.</p>
<p><em>Nejednakost četverokuta.</em> Za $a \le b \le c \le d$ vrijedi $\mathrm{inv}(a, d) + \mathrm{inv}(b, c) \ge \mathrm{inv}(a, c) + \mathrm{inv}(b, d)$: lijeva strana broji svaki par unutar $[b, c]$ dvaput i sve parove unutar $[a, d]$ jednom, desna strana broji parove unutar $[a, c]$ i unutar $[b, d]$; razlika je točno broj inverznih parova $(i, j)$ s $i \in [a, b)$, $j \in (c, d]$, što je $\ge 0$. Iz toga slijedi (standardno) da je najmanji optimalni prijelaz $\mathrm{opt}_j(i)$ nepadajuć u $i$.</p>
<p><em>Postupak.</em> Sloj $j$ računamo funkcijom $\mathrm{rijesi}(lo, hi, optlo, opthi)$: za $mid = \lfloor (lo + hi)/2 \rfloor$ nađemo najbolji $p \in [optlo, \min(opthi, mid-1)]$ linearno, zapišemo $f_j(mid)$ i rekurzivno riješimo $[lo, mid-1]$ s kandidatima $[optlo, p^*]$ te $[mid+1, hi]$ s $[p^*, opthi]$. Na svakoj razini rekurzije ukupni raspon kandidata je $O(n)$, razina je $O(\log n)$, pa sloj stoji $O(n \log n)$ i cijeli DP $O(K n \log n)$. Slojevi trebaju samo prethodni sloj, pa su dovoljna dva polja duljine $n+1$. Za $n = 6000$, $K \approx 6000$ to je oko $4.7 \cdot 10^8$ zbrajanja i usporedbi — izmjereno ispod $0.2$ s.</p>
<h3>5. Primjer</h3>
<p>$a = (4, 5, 6, 2, 2, 1)$, $k = 1$: dva bloka $(4, 5, 6) \mid (2, 2, 1)$ daju $0 + 2 = 2$ (inverzije unutar $(2,2,1)$: dva para), što je optimalno. Za $k = 2$: $(4,5,6) \mid (2,2) \mid (1)$ daje $0$.</p>
<h3>6. Složenost i zamke</h3>
<p>Vrijeme $O(n^2 + K n \log n)$, memorija $O(n^2)$ 32-bitnih brojeva. Zamke: (1) $k$ može biti $0$ — tada je odgovor broj inverzija cijelog niza ($K = 1$); (2) $K = n$ daje $0$ bez računanja tablice; (3) $f$ mora biti 64-bitno? Ne — $\le \binom{n}{2} \lt 2^{31}$, ali koristimo <code>long long</code> s $\infty$ za nedostižna stanja radi jednostavnosti; (4) u rekurziji ograničiti $p \le mid - 1$ da blokovi budu neprazni; (5) ne alocirati tablicu za svaki test iznova ako je $\sum n \le 6000$ — ovdje je samo jedan veliki test moguć pa je alokacija bezopasna.</p>
''',
    'verified': r'''uzorak 1/1 ($k = 1$ i $k = 2$); 300 slučajnih malih testova ($n \le 6$, $k \le 2$, $a_i \le 3$) protiv brute forcea koji izravno po definiciji ispituje sve nizove od najviše $k$ operacija (svi intervali, prirasti $1..4$) i broji inverzije; 3 velika testa ($n = 6000$, $k \in \{1, 50, 3000, 5990\}$, $a_i \le 10^9$), najsporiji $0.14$ s, memorija $\approx 145$ MB.''',
},
# ---------------------------------------------------------------- J
{
    'letter': 'J', 'title': 'Job for a Hobbit', 'title_hr': 'Posao za hobita', 'slug': 'J_job_for_a_hobbit',
    'tl': '2 s', 'ml': '1024 MiB',
    'statement': r'''
<p>U redu je $n$ stupova, na svakom točno $k$ obojenih prstenova (boje su brojevi). Dodana su dva prazna stupa, $0$ i $n+1$, pa ih je ukupno $n + 2$. U jednom potezu hobit skida gornji prsten s nekog stupa i stavlja ga na vrh <em>susjednog</em> stupa; nijedan stup ne smije imati više od $k$ prstenova.</p>
<p>Cilj: svaki stup jednobojan (ili prazan). Odredi je li moguće i, ako jest, ispiši plan od najviše $10^6$ poteza.</p>
<h3>Ulaz</h3>
<p>$z \le 25$ testova; $1 \le n \le 50$, $1 \le k \le 10$, zatim $n$ redaka s po $k$ brojeva $a_{i1}, \dots, a_{ik}$ ($0 \le a_{ij} \le 10^9$) — prstenovi $i$-tog stupa odozdo prema gore; $\sum n \le 50$.</p>
<h3>Izlaz</h3>
<p><code>TAK</code>, broj poteza $p \le 10^6$ i $p$ redaka $a_i\ b_i$ ($0 \le a_i, b_i \le n+1$, $|a_i - b_i| = 1$): premjesti gornji prsten sa stupa $a_i$ na stup $b_i$ (stup $a_i$ neprazan, $b_i$ ima manje od $k$ prstenova). Inače <code>NIE</code>. Bilo koji valjani plan se prihvaća.</p>
<h3>Primjer</h3>
<p>$n = 2$, $k = 2$, stupovi $(1, 2)$ i $(2, 1)$: <code>TAK</code>, $2$ poteza: <code>1 0</code>, <code>2 1</code>. $n = 1$, $k = 4$, stup $(1, 2, 3, 4)$: <code>NIE</code>.</p>
''',
    'hints': [
        r'''
<p>Na kraju je svaki stup jednobojan, pa boja s $c$ prstenova zauzima barem $\lceil c/k \rceil$ stupova. Koji nužan uvjet iz toga slijedi? Zadatak tvrdi (i mi ćemo konstrukcijom pokazati) da je on i dovoljan.</p>
''',
        r'''
<p>Dva prazna stupa su „radni prostor”. Najprije premjesti sve za jedan stup udesno tako da su stupovi $0$ i $1$ prazni, a zatim gradi zbijeni sortirani raspored stup po stup: traženi prsten „hodaj” ulijevo koristeći rupu koja putuje s njim.</p>
''',
        r'''
<p>Kad je zbijeni raspored (sve boje uzastopne u redoslijedu čitanja) gotov, obradi prstene od zadnjeg prema prvom i svaki pomakni $0$–$2$ stupa udesno na njegov konačni stup. Broji poteze: $O(n^2 k^2) \approx 2.5 \cdot 10^5 \ll 10^6$.</p>
''',
    ],
    'coach': [
        ('Koji je nužan uvjet za rješivost?',
         r'''
<p>Neka boja $c$ ima $\mathrm{cnt}_c$ prstenova. U završnom rasporedu svaki stup je jednobojan s najviše $k$ prstenova, pa boja $c$ zauzima barem $\lceil \mathrm{cnt}_c / k \rceil$ stupova, a stupova je $n + 2$. Nužno je $\sum_c \lceil \mathrm{cnt}_c / k \rceil \le n + 2$. Ako je $k = 1$, uvjet je trivijalno ispunjen i početni raspored već je rješenje ($0$ poteza).</p>
'''),
        ('Kako iskoristiti dva prazna stupa da bilo koji prsten dovedemo na željeno mjesto?',
         r'''
<p>Najprije sve pomaknemo za jedan stup udesno (stup $n$ na $n+1$, …, stup $1$ na $2$; svaki od tih $n$ prijenosa je $k$ poteza u susjedni prazan stup), pa su prazni stupovi $0$ i $1$. Gradimo stup $i$ dok su stupovi $i$ (djelomično izgrađen) i $i+1$ prazni ili radni, a desno je ostatak. Ključna operacija: „rupa” (prazan stup) je na $p-1$, traženi prsten $v$ je u stupu $p$ na visini $y$. Prstene od $v$ nagore prebacimo na $p-1$ (v završi na vrhu), a zatim sadržaj stupa $p-2$ prebacimo <em>preko</em> $p-1$ na $p$ dok ima mjesta, ostatak ostaje na $p-1$ iznad $v$. Sada je $p-2$ prazan, a $v$ je u $p-1$: par (rupa, prsten) pomaknuo se za jedan stup ulijevo. Kapacitet je dovoljan jer je ukupno prstenova u tri stupa $\le 2k$ nakon što je jedan ispražnjen.</p>
'''),
        ('Što ako je $v$ na dnu punog stupa?',
         r'''
<p>Tada bi prebacivanje svih $k$ prstenova napunilo $p-1$ i ne bi ostalo mjesta za prolaz sadržaja stupa $p-2$. Zato najprije oslobodimo jedno mjesto na $p-2$ (pomaknemo po jedan gornji prsten ulijevo od $p-2$ do prvog nepunog stupa — stup $i$ sigurno nije pun), gornji prsten stupa $p$ privremeno spremimo na $p-2$, preostalih $k-1$ prstenova prebacimo na $p-1$ ($v$ na vrhu, jedno mjesto slobodno), sadržaj $p-2$ prebacimo kroz $p-1$ na sada prazan $p$, vratimo pomaknute prstene i eventualni ostatak s $p-2$ stavimo na $p-1$. Učinak je isti: rupa i $v$ pomaknuti za jedan ulijevo.</p>
'''),
        ('Kako od zbijenog sortiranog rasporeda doći do jednobojnih stupova?',
         r'''
<p>Zbijeni raspored ima stupove $0..n-1$ pune s bojama u nepadajućem redoslijedu čitanja (stup po stup, odozdo prema gore), a stupovi $n$ i $n+1$ prazni. Unaprijed odredimo konačni stup svakog prstena: boje redom, boja $c$ zauzima sljedećih $\lceil \mathrm{cnt}_c/k \rceil$ stupova — ukupno $\le n+2$ po uvjetu. Prsten na indeksu $t$ (stup $\lfloor t/k \rfloor$) ide na stup $\ge \lfloor t/k \rfloor$, a razlika je najviše $2$ (samo dva dodatna stupa). Obrađujemo prstene od zadnjeg prema prvom; svaki je u tom trenutku na vrhu svog stupa i sva mjesta desno od njega na putu su slobodna ili već popunjena „svojim” bojama s mjesta, pa ga pomaknemo susjed po susjed udesno.</p>
'''),
        ('Koliko poteza konstrukcija troši?',
         r'''
<p>Za jedan prsten faza 1 pomiče rupu do njegovog stupa ($O(nk)$ poteza) i zatim ga hoda ulijevo najviše $n$ koraka po $O(k)$ poteza; nakon svakog izgrađenog stupa zgušnjavanje udesno stoji $O(nk)$. Ukupno $O(n^2 k^2) \approx 50^2 \cdot 10^2 = 2.5 \cdot 10^5$, mjereno oko $2 \cdot 10^5$ za $n = 50$, $k = 10$ — unutar $10^6$. Faza 2 dodaje najviše $2nk$ poteza.</p>
'''),
    ],
    'tips': [
        r'''Kod „Hanoi” zadataka s ograničenim kapacitetom i susjednim potezima prvo odredi nužni uvjet brojanjem (koliko stupova treba svaka boja), a zatim pokušaj konstrukciju koja ga dostiže — dva prazna stupa obično su dovoljan radni prostor.''',
        r'''Gradi rješenje u fazama s jasnom invarijantom (npr. „stupovi $i$, $i+1$ prazni, lijevo gotovo, desno ostatak”) i nakon svake faze eksplicitno obnovi invarijantu (zgušnjavanje).''',
        r'''U kodu koristi jednu funkciju <code>pomak(a, b)</code> koja provjerava legalnost poteza (<code>assert</code>) i bilježi ga — tako svaki bug u konstrukciji odmah pukne umjesto da proizvede neispravan plan.''',
        r'''Za konstruktivne zadatke napiši validator koji simulira ispisani plan i provjerava završno stanje, te BFS brute force za male $n, k$ koji neovisno odlučuje TAK/NIE.''',
    ],
    'solution': r'''
<p>Prema javnoj analizi natjecanja AMPPZ 2022 (kineski blogovi o Universal Cupu) i vlastitoj razradi. Rješenje postoji točno kad $\sum_c \lceil \mathrm{cnt}_c / k \rceil \le n + 2$: nužnost je brojanje jednobojnih stupova, dovoljnost daje konstrukcija u dvije faze. (1) Sve pomaknemo za jedan stup udesno pa su stupovi $0, 1$ prazni; zatim gradimo <em>zbijeni sortirani</em> raspored (stupovi $0..n-1$ puni, boje nepadajuće u redoslijedu čitanja) stup po stup: traženi prsten hodamo ulijevo tako da par (rupa, stup s prstenom) pomičemo za jedan korak — prstene od traženog nagore prebacimo u rupu, a sadržaj stupa lijevo od rupe preko nje udesno; poseban je slučaj prsten na dnu punog stupa, gdje prvo oslobodimo jedno mjesto. Nakon svakog izgrađenog stupa ostatak zgusnemo udesno da opet imamo dva prazna stupa. (2) Iz zbijenog rasporeda prstene obradimo od zadnjeg prema prvom i svaki pomaknemo $0$–$2$ stupa udesno na unaprijed određeni konačni stup svoje boje. Ukupno $O(n^2 k^2) \approx 2 \cdot 10^5$ poteza za $n = 50$, $k = 10$.</p>
''',
    'detailed': r'''
<h3>1. Kriterij rješivosti</h3>
<p>Neka boja $c$ ima $\mathrm{cnt}_c$ prstenova. U ciljnom stanju je svaki stup jednobojan i ima $\le k$ prstenova, pa boja $c$ zauzima barem $\lceil \mathrm{cnt}_c / k \rceil$ stupova. Stupova je $n+2$, pa je <strong>nužno</strong> $\sum_c \lceil \mathrm{cnt}_c / k \rceil \le n + 2$. Pokazat ćemo konstrukcijom da je uvjet i <strong>dovoljan</strong> (za $k \ge 2$; za $k = 1$ je svaki stup već jednobojan i uvjet trivijalno vrijedi). Primjer $n = 1$, $k = 4$, stup $(1, 2, 3, 4)$: treba $4$ stupa, a ima ih $3$ — <code>NIE</code>.</p>
<h3>2. Ciljni zbijeni raspored</h3>
<p>Sortirajmo boje (bilo kojim redom, npr. po vrijednosti) i zapišimo sve $nk$ prstenova u niz $b$ u kojem su jednake boje uzastopne. <em>Zbijeni raspored</em> znači: stup $j \in [0, n-1]$ sadrži $b_{jk}, \dots, b_{jk+k-1}$ odozdo prema gore, a stupovi $n, n+1$ su prazni. Cilj faze 1 je doći do zbijenog rasporeda; faza 2 ga pretvara u jednobojne stupove.</p>
<h3>3. Faza 1: gradnja zbijenog rasporeda</h3>
<p><strong>Priprema.</strong> Redom za $p = n, n-1, \dots, 1$ prebacimo cijeli stup $p$ na (prazan) stup $p+1$: $nk$ poteza, nakon čega su stupovi $0$ i $1$ prazni, a $2..n+1$ puni.</p>
<p><strong>Invarijanta.</strong> Gradimo stup $i$; stupovi $0..i-1$ su gotovi (zbijeni), stup $i$ sadrži prvih $j$ traženih prstenova, stup $i+1$ je prazan, a preostali prstenovi su u stupovima $i+2..n+1$ (na početku gradnje stupa $i$ svi su puni). Sadržaj stupova $0..i$ više ne diramo (osim što stup $i$ služi kao „sigurno nepun” stup u posebnom slučaju, gdje mu privremeno dodamo i vratimo prsten).</p>
<p><strong>Dohvat prstena $v = b_{ik + j}$.</strong> Nađemo najljevlji stup $x \ge i+2$ koji sadrži $v$ i u njemu najviši takav prsten (visina $y$, računano od $1$). Rupu (prazan stup $i+1$) dovedemo do $x-1$ tako da redom za $p = i+2, \dots, x-1$ prebacimo cijeli stup $p$ na $p-1$ — svaki je prijenos u prazan susjedni stup, pa je legalan. Sada je rupa na $x - 1$, a $v$ u stupu $p = x$.</p>
<p><strong>Korak hodanja ulijevo</strong> (dok je $p \gt i+2$): rupa je $p-1$, $v$ je u $p$ na visini $y$, stup $G = p-2$ ima $g \le k$ prstenova.</p>
<ul>
<li><em>Obični slučaj</em> (nije $y = 1$ s punim stupom $p$): prebacimo sve prstene stupa $p$ od visine $y$ nagore na $p-1$; $v$ završi na vrhu $p-1$ na visini $y' = |p| - y + 1 \le k - 1$, u stupu $p$ ostane $y - 1$ prstenova. Zatim prebacujemo sadržaj $G$ jedan po jedan na $p-1$ i odmah dalje na $p$ dok $p$ nije pun; kad se $p$ napuni, ostatak ostaje na $p-1$ iznad $v$. Kapacitet: slobodnih mjesta na $p$ i iznad $v$ na $p-1$ je $(k - y + 1) + (k - y') = 2k - |p| \ge k \ge g$, pa sve stane. Rezultat: $G$ je prazan (nova rupa $p-2$), $v$ je u $p-1$ na visini $y'$, a raspored ostalih prstenova je promijenjen samo unutar tri stupa. Postavimo $p \leftarrow p-1$, $y \leftarrow y'$.</li>
<li><em>Poseban slučaj</em> ($y = 1$, $|p| = k$): obični postupak bi napunio $p-1$ do vrha i ne bi bilo prolaza za $G$. Zato: (a) nađemo najbliži nepuni stup $w \le p-2$ (stup $i$ je sigurno nepun) i pomaknemo gornji prsten svakog stupa $q = w+1, \dots, p-2$ na $q-1$ — sad $p-2$ ima slobodno mjesto; (b) gornji prsten stupa $p$ prebacimo preko $p-1$ na $p-2$; (c) preostalih $k-1$ prstenova stupa $p$ prebacimo na $p-1$ — $v$ je na vrhu na visini $k-1$; (d) sadržaj $p-2$ (točno $k$ prstenova) prebacimo kroz $p-1$ (jedno slobodno mjesto) na prazan $p$; (e) vratimo prstene iz koraka (a) udesno ($q = p-3, \dots, w$: gornji prsten $q \to q+1$) — na $p-2$ se tako vrati najviše jedan prsten; (f) taj prsten prebacimo na $p-1$. Ishod: $p-2$ prazan, $v$ u $p-1$ na visini $y' = k-1$, ostali prstenovi su tamo gdje su bili (do permutacije unutar tri stupa). Svaki pojedini potez je legalan jer uvijek prebacujemo na stup s barem jednim slobodnim mjestom, što slijedi iz brojanja u svakom koraku.</li>
</ul>
<p><strong>Završetak dohvata</strong> ($p = i+2$, rupa $i+1$): prstene stupa $p$ od visine $y$ nagore prebacimo na $i+1$ ($v$ na vrhu), $v$ prebacimo na stup $i$ (ima $j \lt k$ prstenova), a ostatak s $i+1$ vratimo na $i+2$ (ima mjesta jer smo ih odande uzeli). Stup $i+1$ je opet prazan.</p>
<p><strong>Zgušnjavanje.</strong> Nakon što stup $i$ dobije svih $k$ prstenova, desni dio $i+2..n+1$ ima točno $k$ slobodnih mjesta, ali raspršenih. Za $p = n, \dots, i+2$: dok je stup $p$ neprazan i $p+1$ nije pun, gornji prsten stupa $p$ guramo udesno dok god je sljedeći stup nepun. Nakon toga svaki neprazan stup ima punog desnog susjeda, pa su svih $k$ slobodnih mjesta u najljevljem stupu $i+2$ — on je prazan, i invarijanta za $i+1$ (stupovi $i+1$, $i+2$ prazni) vrijedi. Napomena: bez tog koraka konstrukcija zakaže (rupa $i+2$ ne bi bila prazna), što se otkriva tek na većim testovima.</p>
<h3>4. Faza 2: jednobojni stupovi</h3>
<p>Boje obrađujemo u istom redoslijedu kao u $b$; boja $c$ dobiva sljedećih $\lceil \mathrm{cnt}_c / k \rceil$ stupova, pa prsten $b_t$ ima konačni stup $\mathrm{cilj}(t)$, nepadajuć u $t$, s $\mathrm{cilj}(t) \ge \lfloor t/k \rfloor$ (prije njega je barem $\lfloor t/k \rfloor$ punih stupova vrijedno prstenova) i $\mathrm{cilj}(t) \le \lfloor t/k \rfloor + 2$ (ukupno stupova $\le n+2$, a zbijeni ih koristi $n$). Prolazimo $t = nk-1, \dots, 0$: prsten $b_t$ je u tom trenutku na vrhu stupa $\lfloor t/k \rfloor$ (svi kasniji prstenovi su već otišli udesno), a stupovi $\lfloor t/k \rfloor + 1, \dots, \mathrm{cilj}(t)$ sadrže samo prstene s indeksima $\gt t$ smještene na svoja konačna mjesta; na svakom od njih koji je usput ima mjesta (ako bi bio pun, konačni stup od $b_t$ bio bi dalje, što je u suprotnosti s time da je $\mathrm{cilj}$ nepadajuć i da stup $\mathrm{cilj}(t)$ još ima mjesto za $b_t$). Zato $b_t$ pomičemo susjed po susjed do $\mathrm{cilj}(t)$; najviše $2$ poteza po prstenu.</p>
<h3>5. Broj poteza i složenost</h3>
<p>Faza 1: dohvat jednog prstena stoji $O(nk)$ (pomicanje rupe i do $n$ koraka hodanja po $O(k)$ poteza), prstenova je $nk$, plus $n$ zgušnjavanja po $O(nk)$: ukupno $O(n^2 k^2) \le 2.5 \cdot 10^5$ za $n = 50$, $k = 10$ (mjereno $\approx 2 \cdot 10^5$). Faza 2: $\le 2nk$. Sve je daleko ispod $10^6$, a vrijeme izvođenja zanemarivo. Zamke: (1) $k = 1$ obraditi posebno (odgovor $0$ poteza); (2) u fazi 1 uvijek uzimati <em>najviši</em> $v$ u najljevljem stupu — tako je $y$ dobro definiran i broj prebačenih prstenova najmanji; (3) ne zaboraviti zgušnjavanje; (4) svaki potez provući kroz funkciju koja provjerava $|a - b| = 1$, nepraznost izvora i kapacitet odredišta.</p>
''',
    'verified': r'''uzorak 1/1 (plan provjerava <code>check.py</code> simulacijom svih poteza: susjednost, nepraznost izvora, kapacitet $k$, najviše $10^6$ poteza i jednobojnost svih stupova na kraju; <code>NIE</code> se prihvaća samo kad ni brute force nema rješenja); 300 slučajnih malih testova ($n, k \le 3$) protiv brute forcea koji BFS-om po svim stanjima neovisno odlučuje postoji li plan; 3 velika testa ($n = 50$, $k = 10$ s $n$, $n+1$ i $n+2$ potrebnih stupova te $n \in \{37, 50\}$ s malim $k$), najviše $\approx 2 \cdot 10^5$ poteza, najsporiji $0.03$ s.''',
},
# ---------------------------------------------------------------- K
{
    'letter': 'K', 'title': 'Kooky Tic-Tac-Toe', 'title_hr': 'Otkačeni križić-kružić', 'slug': 'K_kooky_tic_tac_toe',
    'tl': '6 s', 'ml': '1024 MiB',
    'statement': r'''
<p>Križić-kružić na ploči $n \times n$: igrači naizmjence stavljaju svoj znak (x ili o) na prazno polje; prvi potez može odigrati bilo koji igrač. Ako se nakon poteza pojavi $k$ istih znakova uzastopno u retku, stupcu, dijagonali ili antidijagonali, taj igrač pobjeđuje i igra završava. Ako nitko ne pobijedi i ploča je puna, igra je neriješena.</p>
<p>Dana je ploča s križićima, kružićima i praznim poljima. Postoji li ispravna igra (igrači ne moraju igrati optimalno, samo po pravilima) koja je <em>završila</em> upravo u ovoj poziciji?</p>
<h3>Ulaz</h3>
<p>$z \le 10\,000$ testova; $3 \le n \le 6$, $2 \le k \le n$, zatim $n$ redaka po $n$ znakova <code>.</code>, <code>x</code>, <code>o</code>.</p>
<h3>Izlaz</h3>
<p><code>TAK</code> i zatim redoslijed poteza — u $i$-tom retku $x_i\ y_i$ (redak od vrha, stupac od lijeva) polja popunjenog u $i$-tom potezu; inače <code>NIE</code>. Bilo koja valjana igra se prihvaća.</p>
<h3>Primjer</h3>
<p>Za $n = k = 3$ ploča <code>x.o / xxx / o.o</code> daje <code>TAK</code> (križić je pobijedio u posljednjem potezu). Ploča <code>xoo / oxx / xoo</code> s $k = 3$ je neriješena — <code>TAK</code>; ista ploča s $k = 2$ je <code>NIE</code> (netko bi pobijedio prije devetog poteza). <code>xox / .o. / xox</code>: <code>NIE</code> (križić je morao odigrati posljednji potez, a kružić je pobijedio). <code>xo. / ..x / xo.</code> s $k=2$: <code>NIE</code> (igra nije završena). <code>x.. / .x. / ..x</code>: <code>NIE</code> (tri križića, nijedan kružić).</p>
''',
    'hints': [
        r'''
<p>Igra staje odmah nakon pobjedničkog poteza. Što to govori o zadnjem potezu pobjednika u odnosu na <em>sve</em> njegove pobjedničke linije na ploči? I mogu li oba igrača imati liniju?</p>
''',
        r'''
<p>Igrači se izmjenjuju, ali bilo tko smije početi: dakle $|\#x - \#o| \le 1$, a ako je pobijedio $P$, on je odigrao zadnji potez pa $\#P \ge \#Q$. Bez pobjednika igra završava samo na punoj ploči.</p>
''',
        r'''
<p>Kad ti uvjeti vrijede, poredak poteza je lako izgraditi: naizmjence, prvi igra onaj s više znakova (ili bilo tko pri jednakosti), pobjednikovo polje koje leži na svim njegovim linijama ide na kraj. Provjeri zašto se ni u jednom ranijem trenutku ne pojavljuje linija.</p>
''',
    ],
    'coach': [
        ('Koji su nužni uvjeti na broj znakova?',
         r'''
<p>Potezi se izmjenjuju, a početi može bilo tko, pa je $|\#x - \#o| \le 1$. Ako je pobijedio igrač $P$, igra je stala odmah nakon njegova poteza, pa je on odigrao zadnji potez: ako je $P$ počeo, $\#P = \#Q + 1$; ako je $Q$ počeo, $\#P = \#Q$. Dakle $\#P \ge \#Q$. U primjeru <code>x.. / .x. / ..x</code> je $\#x = 3$, $\#o = 0$ — NIE.</p>
'''),
        ('Zašto zadnji potez mora ležati na svim pobjedničkim linijama i zašto ne mogu oba igrača imati liniju?',
         r'''
<p>Prije zadnjeg poteza na ploči nije bilo nijedne linije (inače bi igra već stala). Zadnji potez dodaje jedno polje $P$-a; svaka linija $P$-a na završnoj ploči koja ne sadrži to polje postojala je već prije — nemoguće. Dakle presjek svih $P$-ovih linija sadrži zadnji potez, pa mora biti neprazan. Linija igrača $Q$ nije nastala zadnjim potezom (on je $P$-ov), pa bi postojala ranije — nemoguće; zato $Q$ nema liniju.</p>
'''),
        ('Što ako nitko nema liniju?',
         r'''
<p>Igra završava samo pobjedom ili punom pločom, pa ploča mora biti puna; uz $|\#x - \#o| \le 1$ to je remi. Primjer <code>xo. / ..x / xo.</code> s $k = 2$ nema linije, a ploča nije puna — igra nije završila, NIE.</p>
'''),
        ('Zašto su ti uvjeti i dovoljni, tj. kako izgraditi partiju?',
         r'''
<p>Ako uvjeti vrijede, poredamo poteze naizmjence: prvi igra igrač s više znakova (pri jednakosti onaj koji <em>nije</em> zadnji), a ostala polja u bilo kojem redoslijedu, s tim da pobjednikovo polje iz presjeka svih njegovih linija stavimo na kraj. Svako međustanje je podskup završne ploče bez tog polja: $Q$ nema linija ni na cijeloj ploči, a svaka $P$-ova linija sadrži izostavljeno polje, pa ni $P$ nema linije prije zadnjeg poteza. Igra se dakle ne prekida ranije, a zadnji potez stvara pobjedu (ili popunjava ploču za remi).</p>
'''),
        ('Kako to učinkovito provjeriti za $10^4$ testova?',
         r'''
<p>Ploča ima $\le 36$ polja: sve linije duljine $k$ u četiri smjera nabrojimo u $O(n^2 \cdot 4 \cdot k)$, svaku prikažemo 64-bitnom maskom i presjek $P$-ovih linija računamo AND-om. Prvi postavljeni bit presjeka je zadnji potez. Ukupno nekoliko stotina operacija po testu.</p>
'''),
    ],
    'tips': [
        r'''Za „je li završna pozicija dostižna” zadatke krenite od <em>zadnjeg</em> poteza: pravilo o trenutnom završetku daje najjače uvjete upravo na njega.''',
        r'''Dovoljnost dokažite konstrukcijom: pokažite da svako međustanje (podskup završne ploče) ne krši pravila — obično je dovoljno jedno pažljivo odabrano polje ostaviti za kraj.''',
        r'''Male ploče ($\le 64$ polja) prikazujte bitmaskama: presjeci i unije linija postaju jedna AND/OR operacija.''',
        r'''Napišite brute force koji doslovno simulira pravila (pretraga po podskupovima odigranih polja) i usporedite na tisućama slučajnih i „pokvarenih” ploča — u ovakvim zadacima najčešće griješimo u samim uvjetima završetka.''',
    ],
    'solution': r'''
<p>Prema javnim analizama natjecanja AMPPZ 2022 i vlastitoj razradi. Nužni i dovoljni uvjeti: (1) $|\#x - \#o| \le 1$ i ploča nije prazna; (2) ne mogu oba igrača imati liniju od $k$ znakova; (3) ako nitko nema liniju, ploča mora biti puna (remi); (4) ako liniju ima $P$, onda $\#P \ge \#Q$ (zadnji potez je $P$-ov) i presjek svih $P$-ovih linija je neprazan — zadnji potez mora ležati na svakoj od njih, jer bi inače linija postojala ranije i igra bi stala. Dovoljnost: poteze poredamo naizmjence (počinje igrač s više znakova), a polje iz presjeka na kraj; svako međustanje je podskup završne ploče bez tog polja pa nema linija. Linije nabrajamo izravno i prikazujemo 64-bitnim maskama ($n \le 6$), presjek je AND — $O(n^2 k)$ po testu.</p>
''',
    'detailed': r'''
<h3>1. Pravila i njihove posljedice</h3>
<p>Igrači se izmjenjuju, počinje bilo tko, igra staje <em>odmah</em> nakon poteza koji stvara $k$ istih znakova u nizu (redak, stupac, dijagonala, antidijagonala) ili kad je ploča puna. Neka je $\#x$, $\#o$ broj znakova, a <em>linija</em> igrača bilo koji niz od $k$ njegovih uzastopnih polja u jednom od četiri smjera.</p>
<h3>2. Nužni uvjeti</h3>
<ol>
<li><strong>Brojevi.</strong> Zbog izmjenjivanja $|\#x - \#o| \le 1$. Prazna ploča nije završena igra (već prvi potez je moguć), pa $\#x + \#o \ge 1$.</li>
<li><strong>Najviše jedan pobjednik.</strong> Prije zadnjeg poteza nije bilo linija (inače bi igra stala). Zadnji potez dodaje jedno polje jednog igrača, pa samo taj igrač može dobiti linije.</li>
<li><strong>Bez pobjednika $\Rightarrow$ puna ploča.</strong> Jedini drugi način završetka je popunjena ploča.</li>
<li><strong>Pobjednik $P$.</strong> Zadnji potez je $P$-ov, pa $\#P \ge \#Q$ (točno: $\#P = \#Q + 1$ ako je $P$ počeo, $\#P = \#Q$ ako je $Q$ počeo). Nadalje, svaka $P$-ova linija na završnoj ploči mora sadržavati polje zadnjeg poteza — linija koja ga ne sadrži postojala bi već prije zadnjeg poteza. Dakle <strong>presjek svih $P$-ovih linija je neprazan</strong>.</li>
</ol>
<p>Primjeri iz zadatka: <code>xox / .o. / xox</code>, $k = 3$: $\#x = 4 \gt \#o = 1$ krši uvjet 1 (razlika $3$) — NIE (zadatak to opisuje kao „križić je morao odigrati posljednji potez, a kružić je pobijedio”; s $\#x = \#o + 1$ bi zadnji bio x, a o ima liniju, što krši uvjet 4). <code>xoo / oxx / xoo</code>, $k = 2$: oba igrača imaju linije — NIE. Ista ploča, $k = 3$: bez linija, puna — TAK.</p>
<h3>3. Dovoljnost — konstrukcija partije</h3>
<p>Pretpostavimo da uvjeti 1–4 vrijede. Odredimo tko igra prvi: igrač s više znakova; pri jednakosti, u slučaju pobjednika $P$, prvi je $Q$ (da zadnji, $(\#x + \#o)$-ti potez pripadne $P$-u), a u remiju bilo tko. Polja svakog igrača poredamo proizvoljno, osim što $P$-ovo polje $\ell$ iz presjeka svih njegovih linija stavimo na kraj $P$-ova niza; poteze zatim ispisujemo naizmjence. Provjerimo legalnost: stanje nakon $t \lt \#x + \#o$ poteza je podskup završne ploče koji ne sadrži $\ell$. Linija nekog igrača u tom stanju bila bi linija i na završnoj ploči; $Q$ ih nema (uvjet 2/4), a svaka $P$-ova sadrži $\ell$ (uvjet 4) pa ne može biti popunjena. Ploča prije zadnjeg poteza nije puna. Dakle igra se ne prekida do zadnjeg poteza, a nakon njega završava pobjedom $P$-a odnosno remijem na punoj ploči — točno zadana pozicija.</p>
<h3>4. Algoritam</h3>
<ol>
<li>Prebroji $\#x$, $\#o$; ako $|\#x - \#o| \gt 1$ ili ploča prazna: NIE.</li>
<li>Za svaki simbol nabroji sve linije: za svako polje i svaki od 4 smjera provjeri $k$ polja; liniju prikaži 64-bitnom maskom polja ($n^2 \le 36$). Zapamti broj linija i presjek (AND) svih maski.</li>
<li>Oba imaju linije: NIE. Nitko: TAK ako je ploča puna. Samo $P$: TAK ako $\#P \ge \#Q$ i presjek $\ne 0$; zadnji potez je bilo koje polje iz presjeka (npr. najniži bit).</li>
<li>Izgradi redoslijed kako je opisano i ispiši koordinate (redak, stupac) od $1$.</li>
</ol>
<h3>5. Složenost i zamke</h3>
<p>Po testu $O(n^2 \cdot 4 \cdot k) \le 6^2 \cdot 4 \cdot 6 = 864$ provjera polja — $10^4$ testova zanemarivo. Zamke: (1) linije dulje od $k$ (npr. $k+1$ istih znakova) sadrže dvije linije duljine $k$ — presjek to pravilno obrađuje (zadnji potez mora biti u njihovu presjeku); (2) u slučaju $\#P = \#Q$ prvi igra $Q$, ne $P$; (3) remi s $\#x = \#o$ dopušta bilo koga kao prvog; (4) izlaz je „redak stupac” od gornjeg lijevog kuta, indeksiran od $1$; (5) $k = 2$ čini gotovo svaku puniju ploču nemogućom — brute force to potvrđuje.</p>
''',
    'verified': r'''uzorak 1/1 ($5$ ploča; redoslijed poteza provjerava <code>check.py</code> simulacijom pravila do završne pozicije, a <code>NIE</code> se prihvaća samo kad ga daje i brute force); 300 slučajnih malih testova ($n \in \{3, 4\}$: slučajno odigrane partije, partije s jednim pokvarenim poljem i potpuno slučajne ploče) protiv brute forcea s memoiziranom pretragom po podskupu odigranih polja; 3 velika testa (po $10\,000$ ploča $6 \times 6$), najsporiji $0.02$ s.''',
},
# ---------------------------------------------------------------- L
{
    'letter': 'L', 'title': 'Line Replacements', 'title_hr': 'Zamjenske linije', 'slug': 'L_line_replacements',
    'tl': '15 s', 'ml': '1024 MiB',
    'statement': r'''
<p>Tramvajska mreža je stablo s $n$ raskrižja i $n - 1$ pruga; na $p$ raskrižja nalaze se okretišta (svaki list je okretište, a mogu biti i drugdje). Byteasar je odabrao $k$ pruga i svake od sljedećih $k$ noći ukrast će jednu od njih.</p>
<p>Za svaki dan $j = 0, 1, \dots, k$ (nakon $j$ krađa) mora postojati mreža zamjenskih linija: svaka linija je jednostavan put koji počinje i završava u okretištima i vozi neki (pozitivan) broj vožnji na sat, ne prolazi ukradenim prugama, a za svaku neukradenu prugu $i$ ukupan broj vožnji svih linija kroz nju mora biti točno $c_i$.</p>
<p>Nađi redoslijed krađa za koji to vrijedi svaki dan, ili utvrdi da ne postoji (uključujući slučaj da već za $j = 0$ vrijednosti $c_i$ ne opisuju valjanu mrežu).</p>
<h3>Ulaz</h3>
<p>$z \le 15\,000$ testova; $2 \le p \le n \le 500\,000$; $p$ raskrižja s okretištima (uzlazno); $n - 1$ pruga $u_i, v_i, c_i$ ($1 \le c_i \le 10^9$), pruga $i$ je $i$-ta u ulazu; $k$ ($1 \le k \le n-1$) i $k$ različitih indeksa pruga uzlazno; $\sum n \le 2\,000\,000$.</p>
<h3>Izlaz</h3>
<p><code>TAK</code> i $k$ indeksa pruga u redoslijedu krađe (svaka od odabranih točno jednom; bilo koji valjani redoslijed), ili <code>NIE</code>.</p>
<h3>Primjer</h3>
<p>Stablo sa $7$ raskrižja, okretišta $1, 2, 3, 4, 6$, pruge $(7,1,3), (7,2,4), (7,3,4), (7,4,3), (5,3,1), (5,6,1)$. Krađa pruga $\{2, 3\}$: <code>TAK</code>, <code>2 3</code> (i <code>3 2</code> je točno). Krađa pruga $\{2, 3, 5, 6\}$: <code>NIE</code> — nakon krađe bilo koje od pruga $5$, $6$ drugu nije moguće ispravno opslužiti.</p>
''',
    'hints': [
        r'''
<p>Kad se zadana opterećenja $c_e$ na šumi mogu rastaviti na jednostavne putove među okretištima? Pogledaj vrh bez okretišta: svaki put koji njime prolazi koristi točno dvije njegove pruge. Što to znači za zbroj $S_v$ opterećenja oko $v$ i za najveće opterećenje?</p>
''',
        r'''
<p>Uvjet je lokalan: u svakom vrhu bez okretišta $S_v$ paran i $2 \max_e c_e \le S_v$ (i dovoljan je — sparivanje „polubridova” u vrhu i praćenje kroz stablo daje putove). Kako se $S_v$ mijenja krađom pruge?</p>
''',
        r'''
<p>Obrni vrijeme: kreni od stanja nakon svih krađa i <em>dodaji</em> pruge. Pruga težine $c$ smije se dodati kad je $c$ paran i $c \le S_v$ u oba kraja bez okretišta; dodavanje samo povećava $S$, pa je pohlepno dodavanje dopuštenih pruga (red s čekanjem, pruge po vrhu sortirane po težini) točno.</p>
''',
    ],
    'coach': [
        ('Koji je nužan uvjet da opterećenja odgovaraju nekoj mreži linija?',
         r'''
<p>Linija je jednostavan put među okretištima. U vrhu $v$ <em>bez</em> okretišta nijedna linija ne počinje ni ne završava, pa svaki prolazak linije koristi točno dvije pruge kod $v$. Zbroj opterećenja aktivnih pruga kod $v$, $S_v$, je zato $2 \cdot (\text{broj prolazaka})$ — paran. Svaki prolazak koristi zadanu prugu $e$ najviše jednom, pa $c_e \le S_v / 2$, tj. $2 \max_e c_e \le S_v$. U vrhovima s okretištem nema uvjeta.</p>
'''),
        ('Zašto su ti lokalni uvjeti i dovoljni?',
         r'''
<p>U vrhu bez okretišta imamo $S_v$ „polubridova” ($c_e$ kopija pruge $e$); uz $S_v$ paran i $2\max \le S_v$ možemo ih spariti tako da nijedan par ne sadrži dvije kopije iste pruge (klasična tvrdnja: sortiraj kopije po prugi u niz i spari $i$-tu s $(i + S_v/2)$-tom). Sada slijedimo kopiju pruge kroz stablo: u vrhu bez okretišta nastavljamo sparenom kopijom (druge pruge), u okretištu stajemo. Šetnja bez trenutnog povratka u stablu je jednostavan put, pa završava — a završiti može samo u okretištu (u listu bez okretišta uvjet $2\max \le S$ ne bi vrijedio, ali listovi su ionako okretišta). Svaka kopija tako pripada točno jednom putu među okretištima i opterećenja se točno podudaraju.</p>
'''),
        ('Kako krađa mijenja uvjete i zašto je zgodno okrenuti vrijeme?',
         r'''
<p>Krađa pruge $e = (u, v)$ težine $c$ smanjuje $S_u$ i $S_v$ za $c$ i uklanja kandidata za maksimum — uvjeti se mogu i pokvariti i popraviti, pa je teško rasuđivati unaprijed. Unatrag, od stanja nakon svih krađa, pruge <em>dodajemo</em>: dodavanje $e$ u vrh $u$ bez okretišta čuva parnost točno kad je $c$ paran, a uvjet maksimuma $2\max(m_u, c) \le S_u + c$ svodi se (uz već ispunjeno $2 m_u \le S_u$) na $c \le S_u$. Dopuštenost dodavanja ovisi samo o $S_u$ i $S_v$, a oni dodavanjem samo rastu.</p>
'''),
        ('Zašto pohlepno dodavanje bilo koje dopuštene pruge ne može zakazati?',
         r'''
<p>Monotonost: jednom dopuštena pruga ostaje dopuštena. Pretpostavimo da postoji valjani redoslijed krađa, tj. valjani redoslijed dodavanja, i da je pohlepa zapela sa skupom $R$ nedodanih pruga. U valjanom redoslijedu prva dodana pruga iz $R$ dodaje se u stanju čiji je skup aktivnih pruga podskup našeg (sve prije nje su izvan $R$, dakle već dodane), pa su $S$ tada $\le$ našima — a bila je dopuštena; onda je dopuštena i sada, proturječje. Uz to početno stanje (nakon svih krađa) mora samo zadovoljavati lokalne uvjete, a to provjerimo izravno.</p>
'''),
        ('Kako to implementirati u $O(n \log n)$?',
         r'''
<p>Za svaki vrh bez okretišta držimo ukradene pruge kod njega sortirane po težini i pokazivač; brojač <code>treba[e]</code> govori koliko krajeva još čeka dopuštenje. Kad $S_v$ poraste, pomičemo pokazivač dok je $c \le S_v$ i smanjujemo brojače; pruga s brojačem $0$ ide u red. Obrađujemo red, dodajemo prugu, povećavamo $S$ krajeva i otvaramo nove. Ako red presuši prije $k$ pruga: NIE; inače je redoslijed krađa obrnuti redoslijed dodavanja.</p>
'''),
    ],
    'tips': [
        r'''Rastav opterećenja na putove u stablu provjeravaj <em>lokalno</em> po vrhovima: parnost zbroja i uvjet $2\max \le$ zbroj su tipičan „uvjet sparivanja” koji je u stablu i dovoljan.''',
        r'''Kad se stanje kroz proces samo pogoršava/poboljšava u jednom smjeru, okreni vrijeme: brisanje postaje dodavanje, a dodavanje je često monotono pa dopušta pohlepni algoritam s redom čekanja.''',
        r'''Za pohlepu „dodaj bilo koji dopušten element” s uvjetom oblika $c \le S_v$ drži kandidate po vrhu sortirane i pomiči pokazivač — svaki element se otvori točno jednom.''',
        r'''Zbrojevi $S_v$ mogu doseći $n \cdot 10^9$ — koristi 64-bitne tipove.''',
    ],
    'solution': r'''
<p>Prema javnim analizama natjecanja AMPPZ 2022 i vlastitoj razradi. Opterećenja $c_e$ na trenutnoj šumi odgovaraju nekoj mreži linija ako i samo ako je u svakom vrhu $v$ bez okretišta zbroj $S_v$ opterećenja aktivnih pruga paran i $2 \max_e c_e \le S_v$ (nužno jer svaki prolazak koristi dvije pruge; dovoljno jer se kopije pruga u vrhu mogu spariti bez ponavljanja i pratiti kroz stablo do okretišta). Proces obrnemo: krenemo od stanja nakon svih krađa (koje mora zadovoljavati uvjet) i dodajemo pruge; pruga težine $c$ smije se dodati kad je $c$ paran i $c \le S_v$ u svakom kraju bez okretišta. Dodavanje samo povećava $S_v$, pa je pohlepno dodavanje bilo koje dopuštene pruge (red čekanja; po vrhu ukradene pruge sortirane po težini s pokazivačem) točno, a redoslijed krađa je obrnuti redoslijed dodavanja. $O(n \log n)$.</p>
''',
    'detailed': r'''
<h3>1. Kad opterećenja opisuju valjanu mrežu linija</h3>
<p>Promatramo aktivne (neukradene) pruge šume s opterećenjima $c_e \ge 1$. Linija je jednostavan put s krajevima u okretištima i pozitivnim brojem vožnji; mreža je valjana ako se zbroj vožnji kroz svaku aktivnu prugu podudara s $c_e$. Za vrh $v$ neka je $S_v = \sum_{e \ni v \text{ aktivna}} c_e$ i $m_v = \max_{e \ni v} c_e$.</p>
<p><strong>Tvrdnja.</strong> Valjana mreža postoji ako i samo ako za svaki vrh $v$ bez okretišta vrijedi: $S_v$ je paran i $2 m_v \le S_v$.</p>
<p><em>Nužnost.</em> U vrhu bez okretišta linije niti počinju niti završavaju, pa svaki „prolazak” neke linije (računajući višekratnost) koristi točno dvije različite pruge kod $v$. Zato je $S_v = 2 \cdot (\text{broj prolazaka})$, paran. Pruga $e$ kod $v$ sudjeluje u $c_e$ prolazaka, svaki prolazak najviše jednom, pa $c_e \le S_v / 2$.</p>
<p><em>Dostatnost.</em> U svakom vrhu $v$ bez okretišta zamislimo $S_v$ kopija („polubridova”): $c_e$ kopija za svaku aktivnu prugu $e \ni v$. Poredamo ih u niz grupirano po prugi i sparimo $i$-tu s $(i + S_v/2)$-tom: kako nijedna pruga nema više od $S_v/2$ kopija, spareni polubridovi pripadaju različitim prugama. Sada gradimo putove: uzmemo bilo koju još neiskorištenu kopiju pruge $e = (u, v)$ i širimo je u oba smjera — u vrhu bez okretišta prelazimo na sparenu kopiju (druga pruga), u okretištu stajemo. Šetnja nikad ne ide odmah natrag istom prugom, a u stablu takva šetnja ne ponavlja vrhove, pa je konačna i jednostavna; stati može samo u okretištu (u vrhu bez okretišta uvijek postoji nastavak, a list bez okretišta ne postoji po zadatku — i inače bi kršio $2 m_v \le S_v$). Ponavljanjem sve kopije podijelimo u jednostavne putove među okretištima, a svaka pruga $e$ je pokrivena točno $c_e$ puta. Jednake putove spojimo u jednu liniju s odgovarajućim brojem vožnji.</p>
<p>Za sam vrh s okretištem nema uvjeta: linije tamo smiju počinjati i završavati u proizvoljnom broju.</p>
<h3>2. Obrat vremena</h3>
<p>Dani $j = 0, \dots, k$ odgovaraju stanjima s $j$ ukradenih pruga; svako mora zadovoljavati tvrdnju iz 1. Promatramo proces unatrag: stanje $k$ (nakon svih krađa) i zatim <em>dodavanje</em> ukradenih pruga jedne po jedne do stanja $0$. Redoslijed krađa je obrnuti redoslijed dodavanja.</p>
<p><strong>Uvjet dodavanja.</strong> Neka trenutno stanje zadovoljava uvjete i dodajemo prugu $e = (u, v)$ težine $c$. U kraju $u$ s okretištem nema uvjeta. U kraju $u$ bez okretišta novi zbroj je $S_u + c$ i novi maksimum $\max(m_u, c)$. Parnost traži da je $c$ paran. Uvjet maksimuma: $2 m_u \le S_u \lt S_u + c$ već vrijedi, a $2c \le S_u + c \iff c \le S_u$. Dakle: <strong>$e$ se smije dodati $\iff$ ($c$ paran ili oba kraja imaju okretišta) i $c \le S_u$ za svaki kraj $u$ bez okretišta.</strong> (Pruga s neparnim $c$ i krajem bez okretišta nikad se ne može dodati, pa odmah NIE — u primjeru su to pruge $5$ i $6$ težine $1$ kod vrha $5$.)</p>
<h3>3. Monotonost i pohlepni algoritam</h3>
<p>Dodavanjem pruga zbrojevi $S_u$ samo rastu, pa <em>jednom dopuštena pruga ostaje dopuštena</em>. Algoritam: provjeri uvjete stanja $k$; zatim ponavljaj — dodaj bilo koju dopuštenu još nedodanu prugu — dok ih ima. Ako su sve dodane, obrnuti redoslijed je odgovor; inače NIE.</p>
<p><strong>Točnost.</strong> Svako međustanje zadovoljava uvjete (indukcijom, po 2), pa je proizvedeni redoslijed valjan. Obratno, neka postoji valjani redoslijed krađa, tj. valjani redoslijed dodavanja $e_1, \dots, e_k$ počevši od stanja $k$, i neka je pohlepa zapela sa skupom nedodanih $R \ne \emptyset$. Neka je $e_t$ prva pruga iz $R$ u valjanom redoslijedu. U trenutku njezina dodavanja aktivne su pruge stanja $k$ i $e_1, \dots, e_{t-1} \notin R$ — sve su i u našem stanju, pa su naši zbrojevi $S$ barem toliki. Kako je $e_t$ tada bila dopuštena, dopuštena je i u našem stanju, suprotno pretpostavci da je pohlepa zapela. Također, ako stanje $k$ ne zadovoljava uvjete, rješenja nema jer je dan $k$ obavezan.</p>
<h3>4. Implementacija u $O(n \log n)$</h3>
<ol>
<li>Učitaj stablo, okretišta, opterećenja i skup ukradenih pruga; izračunaj $S_v$ i $m_v$ po aktivnim prugama; provjeri uvjete u vrhovima bez okretišta.</li>
<li>Za svaku ukradenu prugu $e$ i svaki njezin kraj bez okretišta: ako je $c_e$ neparan — NIE; inače dodaj $e$ u listu <code>kod[v]</code> i povećaj <code>treba[e]</code>.</li>
<li>Sortiraj svaku listu <code>kod[v]</code> po težini; pokazivač <code>ptr[v]</code>. Funkcija <code>otvori(v)</code> pomiče pokazivač dok je $c_e \le S_v$ i smanjuje <code>treba[e]</code>; pruga s <code>treba[e] = 0</code> ide u red (pruge kojima oba kraja imaju okretišta idu odmah).</li>
<li>Obrađuj red: dodaj prugu, $S_u \mathrel{+}= c$, $S_v \mathrel{+}= c$, <code>otvori(u)</code>, <code>otvori(v)</code>.</li>
<li>Ako je dodano $k$ pruga: TAK i redoslijed obrnut; inače NIE.</li>
</ol>
<p>Svaka pruga uđe u red najviše jednom, pokazivači se pomiču ukupno $O(k)$ puta, sortiranje je $O(k \log k)$. Provjera na primjeru: krađa $\{2, 3\}$ — stanje nakon krađa ima kod vrha $7$ (bez okretišta) $S_7 = 3 + 3 = 6$, $m = 3$; dodajemo prugu $2$ ($c = 4 \le 6$, parno) pa prugu $3$ ($c = 4 \le 10$): redoslijed krađa $3, 2$ ili, dodavši ih obrnuto, $2, 3$ — oboje se prihvaća.</p>
<h3>5. Zamke</h3>
<p>(1) $S_v$ do $5 \cdot 10^5 \cdot 10^9$ — 64-bitni tipovi; (2) uvjet parnosti primjenjuje se samo na krajeve bez okretišta; (3) pruga kojoj oba kraja imaju okretišta uvijek je dopuštena; (4) ulaz je velik ($\sum n \le 2 \cdot 10^6$) — brzi ulaz i izlaz, polja alocirana po testu u $O(n)$; (5) dan $0$ nije posebno provjeravan — njegova valjanost slijedi iz zadnjeg dodavanja.</p>
''',
    'verified': r'''uzorak 1/1 (redoslijed provjerava <code>check.py</code>: permutacija zadanih pruga i za svaki dan $j = 0..k$ lokalni uvjeti, a <code>NIE</code> se prihvaća samo kad ga daje i brute force); 300 slučajnih malih testova ($n \le 6$, $c_i \le 3$) protiv brute forcea koji ispituje sve permutacije krađa, a valjanost svakog dana provjerava <em>izravno po definiciji</em> — backtrackingom po nenegativnim višekratnostima svih jednostavnih putova među okretištima; 3 velika testa (po $4$ stabla s $n = 500\,000$, slučajna i duboka, $k$ do $500\,000$), najsporiji $0.46$ s.''',
},
# ---------------------------------------------------------------- M
{
    'letter': 'M', 'title': 'Minor Evil', 'title_hr': 'Manje zlo', 'slug': 'M_minor_evil',
    'tl': '16 s', 'ml': '1024 MiB',
    'statement': r'''
<p>Sljedećih $k$ dana vještac Gebyte susreće po jedan par ljudi u sukobu: $i$-tog dana osobe $a_i$ i $b_i$, i ubit će $b_i$ („manje zlo”). Susret se održava samo ako su obje osobe još žive. Prije bilo kojeg susreta možeš baciti čaroliju — tada tog dana Gebyte ne ubija nikoga. Čarolija možeš baciti koliko god želiš.</p>
<p>Dan je skup od $s$ tvojih neprijatelja. Možeš li osigurati da svi oni poginu od Gebyteove ruke? Isti par se može pojaviti više puta, pa i s obrnutom odlukom.</p>
<h3>Ulaz</h3>
<p>$z \le 1000$ testova; $2 \le n \le 10^6$, $1 \le k \le 10^6$, $k$ parova $a_i \ne b_i$; $s$ i $s$ različitih neprijatelja uzlazno; $\sum n, \sum k \le 4\,000\,000$.</p>
<h3>Izlaz</h3>
<p><code>TAK</code> i string od $k$ slova <code>T</code>/<code>N</code>: <code>T</code> — $i$-tog dana pusti Gebytea da ubije $b_i$, <code>N</code> — spriječi ga. (Ako se susret ne održava, slovo nije bitno.) Prihvaća se ako nijedan neprijatelj ne preživi. Inače <code>NIE</code>.</p>
<h3>Primjer</h3>
<p>$n = 5$, susreti $(1,2), (2,1), (2,5), (2,3), (2,4), (4,2)$, neprijatelji $1, 2, 3$: <code>TAK</code>, <code>NTTTNT</code> — Gebyte ubija $1$ (2. dan), $5$ (3. dan), $3$ (4. dan) i $2$ (6. dan); točno je i <code>NTNTNT</code>. $n = 3$, susreti $(1,2), (2,3)$, neprijatelji $2, 3$: <code>NIE</code>.</p>
''',
    'hints': [
        r'''
<p>Neprijatelj $v$ mora poginuti na nekom susretu $(a_i, v)$ na kojem su oboje živi. Ne-neprijatelje nikad ne moramo ubiti — što dobivamo ako ih pustimo da svi prežive?</p>
''',
        r'''
<p>Isplati li se neprijatelja ubiti ranije ili kasnije? Što se dogodi sa susretima u kojima je on $a_j$ (potreban živ) ako ga ubijemo kasnije?</p>
''',
        r'''
<p>Obrađuj susrete od zadnjeg prema prvom: ako $b_i$ još treba umrijeti, a $a_i$ nije neprijatelj koji tek treba umrijeti (na ranijem susretu), ubij $b_i$ ovdje. Na kraju provjeri je li svaki neprijatelj dobio susret. $O(n + k)$.</p>
''',
    ],
    'coach': [
        ('Trebamo li ikad ubiti nekoga tko nije neprijatelj?',
         r'''
<p>Ne. Smrt ne-neprijatelja samo uklanja susrete (na kojima bismo možda ubili neprijatelja) — nikad ne pomaže. Zato u svakom susretu s $b_i$ koji nije neprijatelj bacimo čaroliju; ne-neprijatelji su uvijek živi i nikad ne blokiraju susret kao $a_i$.</p>
'''),
        ('Zašto neprijatelja treba ubiti što kasnije?',
         r'''
<p>Neprijatelj $v$ mora umrijeti točno jednom, na susretu $(a_i, v)$ gdje su oboje živi. Dok je živ, $v$ može kao $a_j$ omogućavati susrete na kojima umiru drugi neprijatelji; mrtav ništa ne omogućuje. Kasnija smrt $v$-a zato nikome ne šteti (susreti u kojima je $v$ žrtva a ne želimo ga ubiti — samo čarolija), a može pomoći. Idealno: svaki neprijatelj gine na <em>najkasnijem</em> susretu na kojem je to legalno.</p>
'''),
        ('Kako obrada unatrag točno odlučuje što je „legalno”?',
         r'''
<p>Idemo od $i = k$ do $1$ i držimo skup $M$ neprijatelja koji još nemaju dodijeljenu smrt (na susretu $\gt i$). Za susret $i$: ako $b_i \in M$ i $a_i \notin M$, dodijelimo $b_i$ susret $i$ ($T$) i uklonimo ga iz $M$. Uvjet $a_i \notin M$ znači: $a_i$ je ne-neprijatelj (uvijek živ) ili neprijatelj koji gine kasnije — dakle u trenutku $i$ je živ i susret se održava. Ako je $a_i \in M$, on mora umrijeti prije susreta $i$, pa se susret $i$ ne bi ni održao — ubojstvo tu nije moguće.</p>
'''),
        ('Zašto pohlepa uspijeva kad god postoji rješenje?',
         r'''
<p>Neka valjani plan ubija neprijatelja $v$ na susretu $d(v)$, a pohlepa mu dodjeljuje $g(v)$. Tvrdimo $g(v) \ge d(v)$ za sve $v$ (pa je svaki dodijeljen). Indukcija unatrag po $i$: pogledajmo $i = d(v)$, $b_i = v$. Ako je $v$ već dodijeljen, $g(v) \gt i$. Inače je $v \in M$; u valjanom planu $a_i$ je živ na susretu $i$, pa je $a_i$ ne-neprijatelj ili neprijatelj s $d(a_i) \gt i$, a po induktivnoj pretpostavci $g(a_i) \ge d(a_i) \gt i$, tj. $a_i \notin M$. Pohlepa dakle uzima $i$: $g(v) = i$. Konstruirani plan je valjan: svaki susret označen $T$ se održava (žrtva živa do tada, $a_i$ živ jer umire kasnije ili nikad), a svaki neprijatelj umire.</p>
'''),
    ],
    'tips': [
        r'''Kad događaje smiješ preskočiti, a svaki cilj treba „pogoditi” jednim događajem uz uvjete na živost sudionika, obrada unatrag s pravilom „što kasnije” često daje pohlepu s jednostavnim dokazom razmjenom.''',
        r'''Razdvoji uloge: koga <em>moramo</em> ubiti, koga <em>nikad</em> ne trebamo (ne-neprijatelji) — drugi nikad ne blokiraju susrete.''',
        r'''Dokaz pohlepe unatrag: usporedi s proizvoljnim valjanim planom i pokaži induktivno da pohlepa svakoga obradi „barem toliko kasno”.''',
        r'''Ulaz od $4 \cdot 10^6$ parova traži brzi čitač; izlaz gradi kao jedan string.''',
    ],
    'solution': r'''
<p>Prema javnim analizama natjecanja AMPPZ 2022 i vlastitoj razradi. Ne-neprijatelje nikad ne ubijamo (njihova smrt samo uklanja susrete), a svakog neprijatelja isplati se ubiti što kasnije, jer živ može kao $a_j$ omogućavati kasnije susrete. Obrađujemo susrete od zadnjeg prema prvom i držimo skup $M$ neprijatelja bez dodijeljene smrti: ako je $b_i \in M$ i $a_i \notin M$, susret $i$ označimo $T$ i uklonimo $b_i$ iz $M$ (uvjet $a_i \notin M$ jamči da je $a_i$ tada živ, a $a_i \in M$ bi značilo da mora umrijeti prije $i$, pa se susret ne bi održao). Ako na kraju $M$ nije prazan — NIE. Razmjenom (indukcija unatrag) pokazuje se da pohlepa svakog neprijatelja dodijeli barem toliko kasno kao bilo koji valjani plan, pa uspijeva kad god rješenje postoji. $O(n + k)$.</p>
''',
    'detailed': r'''
<h3>1. Model</h3>
<p>Susret $i$ (dan $i$) između $a_i$ i $b_i$ održava se ako su oboje živi; tada biramo $T$ (Gebyte ubija $b_i$) ili $N$ (čarolija, nitko ne gine). Neprijatelji $E$ moraju svi poginuti. Plan je niz slova; rezultat je određen simulacijom unaprijed.</p>
<h3>2. Dva pojednostavljenja</h3>
<p><strong>Ne-neprijatelji uvijek preživljavaju.</strong> Uzmimo valjani plan u kojem ne-neprijatelj $w$ pogiba na susretu $i$; promijenimo slovo $i$ u $N$. Nakon toga je $w$ živ, pa se skup održanih susreta može samo <em>povećati</em> (susreti kojih $w$ sudionik više nisu blokirani), a svaki susret koji se održavao i prije održava se i dalje s istim slovom — osim što $w$ nije umro. Novo održani susreti s $b_j = w$ i slovom $T$ mogli bi ubiti $w$ kasnije; ponovimo postupak (od najranijeg takvog). Konačno svi neprijatelji i dalje pogibaju jer se njihovi susreti održavaju s istim slovima. Dakle bez smanjenja općenitosti ne-neprijatelji nikad ne umiru i nikad ne blokiraju susrete.</p>
<p><strong>Svaki neprijatelj umire točno jednom</strong>, na susretu $(a_i, v)$ na kojem su oboje živi; svi ostali susreti s $b_j = v$ dobivaju $N$ (ili su nebitni jer se ne održavaju).</p>
<h3>3. Pohlepni algoritam unatrag</h3>
<p>Prolazimo $i = k, k-1, \dots, 1$ i održavamo skup $M \subseteq E$ neprijatelja kojima još nije dodijeljen susret smrti (početno $M = E$). Za susret $i$:</p>
<ul>
<li>ako $b_i \in M$ i $a_i \notin M$: postavi slovo $T$, $M \leftarrow M \setminus \{b_i\}$;</li>
<li>inače slovo $N$.</li>
</ul>
<p>Na kraju: TAK s dobivenim nizom ako je $M = \emptyset$, inače NIE. Skup $M$ je polje logičkih vrijednosti; ukupno $O(n + k)$.</p>
<h3>4. Konstruirani plan je valjan</h3>
<p>Neka je $g(v)$ susret dodijeljen neprijatelju $v$ (svaki je dobio točno jedan, jer se uklanja iz $M$ pri dodjeli). Tvrdnja: pri simulaciji unaprijed svaki susret $g(v)$ se održava i na njemu umire $v$, a nitko ne umire drugdje. Slova $T$ nose samo susreti $g(v)$; pokažimo indukcijom po vremenu da su na susretu $i = g(v)$ oboje živi. $v$ je živ, jer umire samo na $g(v)$. $a_i$: u trenutku dodjele $a_i \notin M$, što znači da je $a_i$ ne-neprijatelj (nikad ne umire) ili neprijatelj već dodijeljen susretu $g(a_i) \gt i$ (obrada ide unatrag), pa je na susretu $i$ živ. Susret se dakle održava i $v$ pogiba. Svi neprijatelji umiru — plan je valjan.</p>
<h3>5. Pohlepa uspijeva kad god rješenje postoji</h3>
<p>Neka postoji valjani plan i u njemu neprijatelj $v$ umire na susretu $d(v)$ (po odjeljku 2 možemo pretpostaviti da ne-neprijatelji ne umiru). Tvrdimo: pohlepa dodijeli svakom $v$ susret $g(v) \ge d(v)$. Indukcija unatrag po $i$; pretpostavimo da je tvrdnja točna za sve neprijatelje s $d \gt i$ i promotrimo $i = d(v)$ (tu je $b_i = v$). Ako je $v$ već dodijeljen, $g(v) \gt i = d(v)$. Inače $v \in M$. U valjanom planu susret $i$ se održao, pa je $a_i$ živ: ili je ne-neprijatelj ($a_i \notin M$ uvijek) ili neprijatelj s $d(a_i) \gt i$, a tada po pretpostavci $g(a_i) \ge d(a_i) \gt i$, pa je $a_i$ već uklonjen iz $M$. Pohlepa dakle uzima $g(v) = i$. Svaki neprijatelj biva dodijeljen — pohlepa vraća TAK.</p>
<h3>6. Primjer</h3>
<p>Susreti $(1,2), (2,1), (2,5), (2,3), (2,4), (4,2)$, $E = \{1, 2, 3\}$. Unatrag: $i = 6$: $b = 2 \in M$, $a = 4 \notin M$ — $T$, $M = \{1, 3\}$. $i = 5$: $b = 4 \notin M$ — $N$. $i = 4$: $b = 3 \in M$, $a = 2 \notin M$ — $T$, $M = \{1\}$. $i = 3$: $b = 5$ — $N$. $i = 2$: $b = 1 \in M$, $a = 2 \notin M$ — $T$, $M = \emptyset$. $i = 1$: $N$. Plan <code>NTNTNT</code>, koji zadatak navodi kao ispravan. Drugi primjer: $(1,2), (2,3)$, $E = \{2, 3\}$: $i = 2$: $b = 3$, $a = 2 \in M$ — ne može ($2$ mora umrijeti ranije); $i = 1$: $b = 2$ — $T$. Ostaje $M = \{3\}$: NIE.</p>
<h3>7. Zamke</h3>
<p>(1) Isti par se može pojaviti više puta i u oba smjera — algoritam to prirodno obrađuje; (2) slova susreta koji se ne održavaju su nebitna, ali ih ispisujemo kao $N$; (3) ulaz do $4 \cdot 10^6$ parova — brzi čitač i ispis stringa odjednom; (4) $M$ resetirati po testu u $O(n)$.</p>
''',
    'verified': r'''uzorak 1/1 (plan provjerava <code>check.py</code> simulacijom susreta unaprijed — svi neprijatelji moraju poginuti; <code>NIE</code> se prihvaća samo kad ga daje i brute force); 300 slučajnih malih testova ($n \le 6$, $k \le 10$) protiv brute forcea koji ispituje sve $2^k$ nizove slova; 3 velika testa ($n = k = 10^6$), najsporiji $0.11$ s.''',
},
]
