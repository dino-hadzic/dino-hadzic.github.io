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
<p><em>Interaktivni zadatak.</em> Skup od $n$ točaka odabran je uniformno slučajno među svim skupovima točaka s pozitivnim cjelobrojnim koordinatama do $10^9$ u kojima nikoje tri točke nisu kolinearne. Točke ne vidiš; smiješ postavljati upite „<code>? i j k</code>”, na koje sudac odgovara $1$ ako je zaokret od $\overrightarrow{P_iP_j}$ prema $\overrightarrow{P_iP_k}$ u smjeru suprotnom od kazaljke na satu, a $-1$ inače (predznak vektorskog produkta). Odredi konveksnu ljusku i ispiši „<code>! k i_1 \dots i_k</code>” s indeksima vrhova ljuske u pozitivnom smjeru.</p>
<h3>Ograničenja</h3>
<p>$3 \le n \le 5000$, najviše $30\,000$ upita. Poredak točaka je također slučajan; interaktor nije adaptivan.</p>
''',
    'hints': [
        r'''<p>Bez koordinata ne možeš naći „najljeviju” točku ni sortirati kutove jeftino. Umjesto toga dodaj točke jednu po jednu i održavaj trenutnu ljusku: točka unutar ljuske ne mijenja ništa.</p>''',
        r'''<p>Provjera „je li nova točka unutar poligona” linearnim prolazom po stranicama troši previše upita. Binarno pretraživanje po dijagonalama poligona: jedan upit kaže na kojoj je strani dijagonale točka, čime se odbacuje pola poligona.</p>''',
        r'''<p>Očekivana veličina ljuske slučajnih točaka u kvadratu je $O(\log n)$, a vjerojatnost da $i$-ta točka mijenja ljusku je otprilike $H_i / i$ — zato je ukupan broj upita mali.</p>''',
    ],
    'coach': [
        ('Opažanje', r'''<p>Upit „$? i j k$” odgovara na pitanje u kojoj poluravnini u odnosu na pravac $P_iP_j$ leži $P_k$. Nova točka je unutar konveksnog poligona ako je s iste (unutarnje) strane svih pravaca stranica. Za slučajne točke ljuska je mala ($O(\log n)$ vrhova), a većina novih točaka pada unutra.</p>'''),
        ('Redukcija: lokalizacija binarnim pretraživanjem', r'''<p>Održavaj ljusku $H$ kao cikličku listu. Za novu točku $p$ odaberi dijagonalu koja dijeli poligon na dva približno jednaka dijela i pitaj na kojoj je strani $p$; nastavi u toj polovici. Nakon $\approx \log_2 |H|$ upita ostaje trokut; s još najviše $3$ upita znaš je li $p$ unutra ili preko koje stranice je izašla. Stranice koje su dijagonale izvornog poligona već su upitane, pa je trošak $\max(3, 2 + \log_2(|H| - 2))$.</p>'''),
        ('Algoritam: umetanje i popravak', r'''<p>Ako je $p$ vani preko stranice $(a, b)$, umetni $p$ između $a$ i $b$, a zatim uklanjaj susjede dok poligon nije konveksan (svaki test je jedan upit; svaka točka može biti uklonjena najviše jednom). Ukupno: $\le 2n + 3k + \sum_{i} \log_2 H_{i-1}$ upita, gdje je $k$ broj umetanja — očekivano $O(\log^2 n)$ umetanja i $O(n \log\log n)$ za lokalizaciju; službena rješenja troše $24\,000$–$27\,000$ upita.</p>'''),
        ('Složenost', r'''<p>$O(n \log n)$ vremena; broj upita ispod $30\,000$ u očekivanju (randomiziran ulaz, neadaptivan interaktor).</p>'''),
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
        ('Opažanje', r'''<p>Neka su $x, y$ susjedni s $x > y$. Fiksiraj bilo koji podniz koji sadrži $x$: dodavanje/uklanjanje $y$ ne mijenja broj rekorda ($y$ nije rekord jer je $x$ ispred njega i veći), ali mijenja parnost duljine. Takvi parovi podnizova daju $0$, pa sve podnizove koji sadrže $x$ možemo zanemariti — tj. izbaciti $x$ iz permutacije bez promjene odgovora.</p>'''),
        ('Redukcija', r'''<p>Ponavljaj dok postoji susjedni pad. Rezultat je rastući niz, i to točno onih elemenata koji su manji od svih elemenata desno od sebe (sufiksni minimumi). Neka ih je $m$.</p>'''),
        ('Algoritam i složenost', r'''<p>U rastućem nizu svaki je element podniza rekord, pa podniz s točno $k$ rekorda ima duljinu $k$: odgovor je $(-1)^k \binom{m}{k}$ (i $0$ ako $k > m$). Sufiksne minimume izbroji jednim prolazom zdesna, binomni koeficijent s faktorijelama — $O(n)$.</p>'''),
    ],
    'solution': r'''
<p>Promotrimo dva susjedna elementa $x$ i $y$ takva da je $x > y$. Uzmimo sve podnizove koji sadrže $x$; u njima $y$ nije rekord. Podijelimo li te podnizove u parove koji se razlikuju samo u $y$, u svakom paru podnizovi imaju isti broj rekorda, ali različitu parnost duljine. Svaki par stoga doprinosi $0$, pa element $x$ možemo potpuno izbaciti iz permutacije, a odgovor se neće promijeniti.</p>
<p>Ponavljamo to dok možemo. Na kraju dobivamo rastući niz; element ostaje u nizu ako i samo ako je manji od svega desno od sebe. U takvom nizu svaki podniz ima sve elemente kao rekorde, pa nas zanimaju podnizovi od $k$ elemenata. Odgovor je $\binom{m}{k} (-1)^k$, gdje je $m$ broj preostalih elemenata.</p>
''',
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
        ('Opažanje', r'''<p>Zapiši $A_{ij} = \sum_{k=0}^{K-1} 2^k A^{(k)}_{ij}$ s $A^{(k)}_{ij} = b_i^{(k)} \oplus c_j^{(k)}$. Za fiksni $k$, redak $i$ matrice $A^{(k)}$ jednak je $c^{(k)}$ ako je $b_i^{(k)} = 0$, a $\mathbf{1} - c^{(k)}$ ako je $b_i^{(k)} = 1$.</p>'''),
        ('Redukcija', r'''<p>Svaki redak $A$ je stoga linearna kombinacija $K + 1$ fiksnih vektora $c^{(0)}, \dots, c^{(K-1)}, \mathbf{1}$, pa $\operatorname{rank} A \le K + 1 = 61$. Ako je $n > 61$, $\det A = 0$.</p>'''),
        ('Algoritam i složenost', r'''<p>Za $n \le 61$ izračunaj determinantu Gaussovom eliminacijom modulo $998244353$ u $O(n^3)$; za veće $n$ ispiši $0$. Uz $\sum n \le 10^4$ sve prolazi trenutno.</p>'''),
    ],
    'solution': r'''
<p>Promotrimo binarni zapis svakog elementa $A$; on kaže kako element zapisati kao zbroj potencija dvojke. Neka je $A_{ij} = \sum_{k=0}^{K-1} 2^k A^{(k)}_{ij}$; tako definiramo $K$ $01$-matrica $A^{(k)}$ s $A = \sum_k 2^k A^{(k)}$.</p>
<p>Ali svaka $A^{(k)}$ određena je samo $k$-tim bitovima $b$ i $c$, a svaki joj je redak ili $c^{(k)}$ ili $c^{(k)} \oplus \mathbf{1}_n = \mathbf{1}_n - c^{(k)}$. To znači da se svaki redak $A$ može zapisati kao linearna kombinacija $c^{(0)}, c^{(1)}, \dots, c^{(K-1)}$ i $\mathbf{1}_n$. Stoga je $\operatorname{rank}(A) \le K + 1$, pa za $n > K + 1$ vrijedi $\det A = 0$. Inače determinantu računamo trivijalno u $O(n^3)$.</p>
''',
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
        ('Opažanje', r'''<p>Uvjet checkera je $\lfloor a_q / a_p \rfloor = \lfloor a_j / a_i \rfloor$. Za susjedne elemente kvocijent $\lfloor a_{t+1} / a_t \rfloor$ je $1$ točno kad je $a_{t+1} < 2 a_t$. Ako je kvocijent $\ge 2$, vrijednost se barem udvostručuje.</p>'''),
        ('Redukcija', r'''<p>Vrijednosti su $\le C = 10^{18}$, pa udvostručenja može biti najviše $\log_2 C \approx 60$. Ako je $n \ge \log_2 C + 3$, među $n - 1$ susjednih parova najviše $\approx 60$ ima kvocijent $\ge 2$, pa postoje barem dva <em>disjunktna</em> susjedna para $(i, i+1)$, $(p, p+1)$ s $i + 1 < p$ i kvocijentom $1$ — to je rješenje $i, i+1, p, p+1$.</p>'''),
        ('Algoritam i složenost', r'''<p>Ako je $n$ velik (npr. $n \ge 63$), skeniraj susjedne parove i uzmi prva dva disjunktna s kvocijentom $1$ (postoje po dokazu). Inače ($n \le 62$) iscrpno provjeri sve $\binom{n}{4}$ četvorke — oko $5 \cdot 10^5$ provjera. Ukupno $O(n + \binom{\min(n, 62)}{4})$.</p>'''),
    ],
    'solution': r'''
<p>Najprije treba uočiti da checker dijeli u tipu <code>long long</code>, pa rezultat zaokružuje prema dolje. Tada je jasno da s mnogo elemenata vrijednosti ne mogu svaki put udvostručiti, pa će postojati dva para s cjelobrojnim kvocijentom jednakim $1$. Preciznije, ako imamo barem $\log_2 C + 3$ elemenata, naći ćemo dva (disjunktna) para susjednih elemenata s kvocijentom $1$. U protivnom jednostavno probamo svih $\binom{n}{4}$ mogućnosti.</p>
''',
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
        r'''<p>Broji različite podnizove po blokovima: neka je $x$ broj različitih podnizova koji ne završavaju s $1$ (uključujući prazan), a $y$ broj onih koji ne završavaju s $0$. Što se dogodi s $(x, y)$ nakon dodavanja bloka od $t$ nula?</p>''',
        r'''<p>Dodavanje $t$ nula: $(x, y) \to (x + ty, y)$. Obrnuto — to je Euklidov algoritam! Niz je valjan ako i samo ako Euklidov postupak na $(x, y)$ završi u $(1, 1)$, tj. $\gcd(x, y) = 1$, uz $x + y = n + 2$. Broj takvih nizova je $\varphi(n + 2)$.</p>''',
        r'''<p>Ako je $x_1 > x_2$ i $y_1 < y_2$ (uz isti zbroj), niz $S(x_1, y_1)$ je leksikografski manji. Dakle $k$-ti niz odgovara $k$-tom broju $y$ iz $[1, n+1]$ koprostom s $n + 2$ — binarno pretraživanje + uključivanje–isključivanje po prostim faktorima.</p>''',
    ],
    'coach': [
        ('Opažanje: brojanje podnizova po blokovima', r'''<p>Obrađuj niz slijeva. Neka je $x$ broj različitih podnizova koji ne završavaju s $1$ (završavaju s $0$ ili su prazni), a $y$ broj onih koji ne završavaju s $0$. Pokaže se $x \le y$ prije bloka nula. Nakon jedne nule: podnizova koji ne završavaju s $1$ postaje $x + y$; nakon $t$ nula: $x + ty$. Simetrično za blok jedinica.</p>'''),
        ('Redukcija: Euklidov algoritam', r'''<p>Postupak unatrag je Euklidov algoritam: iz $(x, y)$ s $x > y$ oduzimamo $y$ od $x$ (jedna nula), s $x < y$ oduzimamo $x$ od $y$ (jedna jedinica). Prazan niz ima par $(1, 1)$, pa je niz valjan ako i samo ako Euklid iz $(x, y)$ stiže u $(1, 1)$ — tj. $\gcd(x, y) = 1$ — i pritom $x + y = n + 2$ (jer je $n$ nepraznih podnizova plus prazan, brojan dvaput). Slijedi: broj valjanih nizova je $\varphi(n + 2)$. Definiraj $S(x, y)$: $S(1,1) = \varepsilon$, $S(x, y) = 0 + S(x - y, y)$ za $x > y$, $S(x, y) = 1 + S(x, y - x)$ za $x < y$. Ako gradimo zdesna nalijevo (obrnuto), Euklid ispisuje blokove slijeva.</p>'''),
        ('Algoritam: $k$-ti u leksikografskom poretku', r'''<p>Indukcijom po $x_1 + x_2 + y_1 + y_2$: ako $x_1 > x_2$ i $y_1 < y_2$, onda $S(x_1, y_1) < S(x_2, y_2)$ (prvi znakovi: $0 < 1$; ako su jednaki, hipoteza vrijedi za sufikse). Svi zanimljivi parovi imaju isti zbroj, pa ih sortiramo po rastućem $y$: $k$-ti niz odgovara $k$-tom broju $y \in [1, n+1]$ koprostom s $n + 2$. Faktoriziraj $n + 2$ u $O(\sqrt{n})$, binarno pretraživanje po $y$ s brojanjem koprostih na prefiksu uključivanjem–isključivanjem ($\le 2^9$ članova). Zatim simuliraj Euklid s dijeljenjem (blokovi = kvocijenti), $O(\log n)$ blokova.</p>'''),
        ('Složenost', r'''<p>$O(\sqrt{n} + 2^{\omega(n+2)} \log n)$ po testnom primjeru.</p>'''),
    ],
    'solution': r'''
<p>Razmotrimo kako bismo izračunali broj različitih podnizova binarnog niza zadanog u obliku iz izlaza. Recimo da prije skupine od $t$ nula imamo $x$ različitih podnizova koji ne završavaju s $1$ (završavaju s $0$ ili su prazni) i $y$ različitih podnizova koji ne završavaju s $0$. Lako se pokaže $x \le y$. Nakon dodavanja jedne nule broj različitih podnizova koji ne završavaju s $1$ postaje $x + y$; nakon dvije nule $x + 2y$; nakon $t$ nula $x + ty$.</p>
<p>Sada uočavamo da je taj proces unatrag Euklidov algoritam. Umjesto računanja broja podnizova slijeva nadesno možemo to raditi zdesna nalijevo; tada Euklidov algoritam ispisuje skupine slijeva nadesno.</p>
<p>Prazan niz ima $1$ (prazan) podniz, pa mu je par $(x, y) = (1, 1)$. Dakle na kraju Euklidova algoritma moramo doći do $(1, 1)$, što se događa ako i samo ako krećemo od para $(x, y)$ s $\gcd(x, y) = 1$. Na početku niz mora imati $n$ različitih nepraznih podnizova, pa je $x + y = n + 2$. Ta su dva uvjeta nužna i dovoljna. Vrijedi $\gcd(n+2, y) = \gcd(n + 2 - y, y) = \gcd(x, y) = 1$, pa je npr. broj takvih nizova $\varphi(n + 2)$. Još treba dobiti $k$-ti od njih.</p>
<p>Nazovimo niz dobiven Euklidovim algoritmom iz $(x, y)$ (uz $\gcd(x, y) = 1$) $S(x, y)$: $S(1, 1) = \varepsilon$; za $x > y$, $S(x, y) = \text{“0”} + S(x - y, y)$; za $x < y$, $S(x, y) = \text{“1”} + S(x, y - x)$.</p>
<p>Tvrdimo: ako je $x_1 > x_2$ i $y_1 < y_2$, onda je $S(x_1, y_1) < S(x_2, y_2)$. Dokaz indukcijom po $x_1 + x_2 + y_1 + y_2$: ako su prvi znakovi različiti, $S(x_1, y_1)$ počinje s $0$, a $S(x_2, y_2)$ s $1$. Inače oba počinju istim znakom, recimo $0$; tada je $S(x_1, y_1) = \text{“0”} + S(x_1 - y_1, y_1)$, $S(x_2, y_2) = \text{“0”} + S(x_2 - y_2, y_2)$, a $x_1 - y_1 > x_2 - y_2$, pa primjenjujemo pretpostavku na sufikse.</p>
<p>Budući da svi zanimljivi parovi imaju isti zbroj, dovoljno ih je sortirati po rastućem $y$. Time smo zadatak sveli na traženje $k$-tog broja koprostog s $n + 2$: faktoriziramo $n + 2$ (dovoljno je $O(\sqrt{n})$), binarno pretražujemo odgovor, a broj brojeva na prefiksu koprostih sa zadanim brojem računamo uključivanjem–isključivanjem po prostim djeliteljima.</p>
''',
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
        r'''<p>Dok se sortirani prefiksi i sufiksi ne sijeku ($k \le n/2$), operacije su neovisne: dovoljno je sortirati najveći prefiks i najveći sufiks. Binarno pretraživanje po odgovoru s provjerom u $O(n)$ (counting sort).</p>''',
        r'''<p>Nakon što se prefiks i sufiks preklope, niz je spoj dvaju rastućih dijelova; održavaj ga kao [točan prefiks][sortirani dio 1][sortirani dio 2][točan sufiks] i svaku operaciju izvedi pomicanjem granica — ukupno $O(n)$.</p>''',
    ],
    'coach': [
        ('Opažanje: alternirajuće operacije', r'''<p>Uzmi optimalan niz operacija. Ako su operacije $k$ i $k+1$ istog tipa, operacija $k$ je beskorisna (operacija $k+1$ sortira nadskup), pa je smijemo zamijeniti drugim tipom bez pogoršanja. Zamjena na najdesnijem takvom paru pomiče problem ulijevo, pa induktivno postoji optimalno rješenje s alternacijom. Kandidati: <code>PSPS…</code> i <code>SPSP…</code>. Provjeri oba.</p>'''),
        ('Redukcija: neovisni dio ($m \le n/2$)', r'''<p>Dok je $k \le n/2$, prefiksi i sufiksi koji se sortiraju su disjunktni i ne utječu jedni na druge, pa je rezultat isti kao sortiranje najvećeg prefiksa i najvećeg sufiksa koji se pojavljuju. Provjera je li niz nakon $m$ operacija sortiran u $O(n)$ (counting sort na dijelovima); je li $m$ dovoljno je monotono, pa binarno pretraživanje.</p>'''),
        ('Algoritam: preklapajući dio ($m > n/2$)', r'''<p>Nakon prva dva preklapajuća sortiranja niz je spoj dvaju rastućih nizova. Održavaj oblik [točan prefiks][sortirani segment iz prve polovice][sortirani segment iz druge polovice][točan sufiks]. Sortiranje prefiksa odreže prefiks trećeg dijela i spoji ga u drugi, ali te vrijednosti postaju „točne”, pa zapravo produljuju točan prefiks: operacija se svodi na rezanje prefiksa drugog i trećeg dijela; simetrično za sufiks. Svako pomicanje granice smanjuje segment za jedan, dakle $O(n)$ ukupno. Alternativa: nakon $n/2$ ostaje $O(\sqrt{n})$ operacija koje se mogu simulirati izravno u $O(n \sqrt{n})$.</p>'''),
        ('Složenost', r'''<p>$O(n \log n)$ za binarno pretraživanje s $O(n)$ provjerom, plus $O(n)$ za preklapajući dio.</p>'''),
    ],
    'solution': r'''
<p>Nikad nije loše sortirati neki podsegment.</p>
<p>Uzmimo optimalan odgovor. Ako ima dvije uzastopne operacije istog tipa, prva je beskorisna, pa je možemo zamijeniti drugim tipom bez pogoršanja odgovora. Ako to primijenimo na najdesniji takav par, sigurno ćemo najdesniji par pomaknuti ulijevo (ili sve takve parove ukloniti), pa možemo eliminirati sve takve parove. To dokazuje da postoji optimalan odgovor s alternirajućim operacijama; takva su niza samo dva — probamo oba.</p>
<p>Sortiranje implementiramo u $O(n)$ (counting sort). Dok se prefiksi i sufiksi koje sortiramo ne sijeku, ne utječu jedni na druge, pa sortiramo samo najveći prefiks i najveći sufiks. Ako je odgovor najviše $n/2$, možemo binarno pretraživati odgovor s provjerom u $O(n)$.</p>
<p>Ako je odgovor veći od $n/2$, izvedemo prva dva sortiranja koja se sijeku; nakon toga je niz uvijek spoj dvaju rastućih nizova. Štoviše, trenutni niz održavamo u obliku <code>[točan prefiks] [sortirani segment iz prve polovice] [sortirani segment iz druge polovice] [točan sufiks]</code>. Pri sortiranju prefiksa odrezat ćemo prefiks trećeg dijela i spojiti ga u drugi, ali te vrijednosti zapravo postaju točne, pa produljuju točan prefiks. Operacija se dakle svodi na rezanje prefiksa drugog i trećeg dijela; isto vrijedi za sortiranje sufiksa i rezanje sufiksa dvaju segmenata. Obje se operacije implementiraju pomicanjem lijeve ili desne granice segmenata, a svakim pomicanjem veličina segmenta pada za jedan — ukupno $O(n)$ operacija.</p>
<p>Drugi način za drugi dio: nakon $n/2$ ostaje najviše $\sqrt{n}$ operacija, koje možemo implementirati u $O(n \sqrt{n})$; ovisno o konstanti to može proći.</p>
''',
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
        ('Opažanje', r'''<p>Palindromnih podsegmenata je barem $n$ (svaki znak). Palindrom duljine $\ge 2$ sadrži u sredini palindrom duljine $2$ ili $3$; dakle niz ima točno $n$ palindroma ako i samo ako nema $a_i = a_{i+1}$ ni $a_i = a_{i+2}$ — svaki element različit od dva prethodna.</p>'''),
        ('Redukcija: $m \ge 3$', r'''<p>Uvjet je ostvariv: $m$ izbora za prvi, $m - 1$ za drugi, $m - 2$ za svaki sljedeći, neovisno o ranijim izborima. Ukupno $m(m-1)(m-2)^{n-2}$ nizova (pazi na overflow, ograniči na $> 10^{18}$). $k$-ti niz: za svaku poziciju, dopuštene vrijednosti su sortirane, a svaka nosi jednak broj nastavaka $(m-2)^{\text{ostatak}}$ — odaberi odgovarajuću (poput zapisa broja u mješovitoj bazi).</p>'''),
        ('Algoritam: rubni slučajevi', r'''<p>$m = 1$: jedini niz je $1, 1, \dots, 1$ ($k = 1$), inače $-1$. $m = 2$: brute force pokazuje da za $n \ge 10$ postoji točno $12$ optimalnih nizova, svaki s periodom $6$ (npr. rotacije i komplementi uzorka $112122$); za $n < 10$ generiraj brute forceom. Za $m \ge 3$ koristi konstrukciju iz prethodnog koraka.</p>'''),
        ('Složenost', r'''<p>$O(n)$ za rekonstrukciju; potencije računaj uz kapu na $10^{18} + 1$.</p>'''),
    ],
    'solution': r'''
<p>Slučaj $m = 1$ je trivijalan.</p>
<p>Za $m \ge 3$ svaki znak možemo učiniti različitim od dva prethodna, čime ne nastaje nijedan palindrom duljine veće od $1$. Tada, neovisno o ranijim izborima, imamo $m$ mogućnosti za prvu poziciju, $m - 1$ za drugu i $m - 2$ za sve ostale. Odavde je lako naći $k$-ti niz.</p>
<p>Za $m = 2$ možete napisati brute force i uočiti da za $n \ge 10$ postoji točno $12$ valjanih nizova, svaki s periodom $6$.</p>
''',
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
        ('Opažanje: orijentacija po stupnju', r'''<p>Sortiraj vrhove po rastućem stupnju; za svaki vrh gledaj samo bridove prema vrhovima desno od njega, neka ih je $d_i$. Vrijedi $d_i \le \deg_i$, $\sum d_i = m$. Vrhovi sa $\deg_i \le \sqrt{2m}$ imaju $d_i \le \sqrt{2m}$; vrhova sa $\deg_i > \sqrt{2m}$ je manje od $\sqrt{2m}$ i oni su na kraju liste, pa i za njih $d_i < \sqrt{2m}$.</p>'''),
        ('Redukcija: $K_4$ kao trokut u pomoćnom grafu', r'''<p>Fiksiraj vrh $u$ kao najmanji (u sortiranom poretku) vrh klike. Sve trokute $(u, x, y)$ s $x, y$ desno od $u$ nađi iscrpno u $O(d_u (d_u + \sqrt{2m})) = O(d_u \sqrt{m})$ (za svaki izlazni susjed $x$ prođi njegove izlazne susjede i provjeri susjedstvo s $u$ preko označavanja). Izgradi mali graf na izlaznim susjedima $u$ u kojem brid $(x, y)$ znači trokut $(u, x, y)$. $K_4$ $(u, x, y, z)$ odgovara trokutu $(x, y, z)$ u malom grafu.</p>'''),
        ('Algoritam i složenost', r'''<p>Broj trokuta u malom grafu s $n_u = d_u$ vrhova i $m_u$ bridova računaj bitsetima: za svaki brid $(x, y)$ prebroji $|N(x) \cap N(y)|$ — $O(m_u n_u / w)$. Kako je $\sum_u m_u$ = broj trokuta $= O(m \sqrt{m})$ i $n_u \le \sqrt{2m}$, ukupno $O\!\left(\frac{m^2}{w}\right)$ — za $m = 10^5$ i $w = 64$ oko $1.6 \cdot 10^8$ riječi. Svaki $K_4$ brojan je točno jednom (kroz svoj najmanji vrh $u$), ali zbrajanje $|N(x) \cap N(y)|$ po bridovima malog grafa svaki trokut broji tri puta — podijeli s $3$ (ili broji samo susjede s indeksom većim od $x$ i $y$).</p>'''),
    ],
    'solution': r'''
<p>Sortirajmo vrhove po rastućem stupnju. Za svaki vrh promatramo samo bridove prema vrhovima desno od njega; neka je broj takvih bridova iz $i$-tog vrha $d_i$. Očito $d_i \le \deg_i$, $\sum_i d_i = m$, $\sum_i \deg_i = 2m$.</p>
<p>Za vrhove sa $\deg_i \le \sqrt{2m}$ jasno je $d_i \le \sqrt{2m}$. Vrhova sa $\deg_i > \sqrt{2m}$ može biti najviše $\sqrt{2m}$ i oni su na kraju liste sortirane po stupnju, pa je i za njih $d_i < \sqrt{2m}$.</p>
<p>Fiksirajmo prvi vrh $u$ mogućeg $K_4$. U $O(d_i(d_i + \sqrt{2m})) = O(d_i \sqrt{m})$ iscrpnim pretraživanjem nalazimo sve trokute ($K_3$) iz tog vrha. Izgradimo novi graf samo na susjedima fiksiranog vrha koji su desno od njega, u kojem brid $(x, y)$ znači da postoji trokut $(u, x, y)$ u izvornom grafu. Sada $K_4$ $(u, x, y, z)$ u izvornom grafu odgovara trokutu $(x, y, z)$ u novom malom grafu.</p>
<p>Dakle želimo prebrojati trokute u malom grafu. Ako on ima $n_u$ vrhova i $m_u$ bridova, to se lako radi u $O(m_u n_u / \omega)$ bitsetima. Pri tome je $n_u = d_u$, a $m_u$ je broj trokuta koji počinju u $u$. Vrijedi</p>
<p>$$\sum_u \frac{m_u n_u}{\omega} \le \frac{\sqrt{2m}}{\omega} \sum_u m_u, \qquad \sum_u m_u = O(m\sqrt{m}),$$</p>
<p>jer je to broj trokuta u grafu. Stoga rješenje radi u $O\!\left(\frac{m^2}{\omega}\right)$.</p>
''',
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
