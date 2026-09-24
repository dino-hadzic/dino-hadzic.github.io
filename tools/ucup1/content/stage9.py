# -*- coding: utf-8 -*-
STAGE = {
    'no': 9,
    'name': 'Stage 9: Qingdao',
    'source_name': 'March 25-26, 2023',
    'no_editorial': True,
    'source_html': r'''
<p>Zadaci potječu s natjecanja The 2018 ICPC Asia Qingdao Regional Contest. Tekst zadatka preveden je prema službenim <a href="https://contest.ucup.ac/download.php?type=attachments&amp;id=1187&amp;r=1">engleskim tekstovima zadataka</a>. Organizatori nisu objavili službena rješenja. Zadatak je dostupan na <a href="https://contest.ucup.ac/contest/1187">Universal Cup Judging System</a>.</p>
''',
}

PROBLEMS = [
# ---------------------------------------------------------------- A
{
    'letter': 'A', 'title': 'Sequence and Sequence', 'title_hr': 'Niz i niz', 'slug': 'A_sequence_and_sequence',
    'tl': '10 s', 'ml': '256 MiB',
    'statement': r'''
<p>Niz $P$ je sortiran niz u kojem se svaki pozitivan cijeli broj $k$ pojavljuje točno $k + 1$ puta: $P = \{1, 1, 2, 2, 2, 3, 3, 3, 3, 4, \dots\}$. Niz $Q$ zadan je s $Q(1) = 1$ i $Q(i) = Q(i-1) + Q(P(i))$ za $i \gt 1$: $Q = \{1, 2, 4, 6, 8, 12, 16, 20, 24, 30, 36, 42, 48, 54, 62, \dots\}$.</p>
<p>Za dani $n$ izračunaj $Q(n)$.</p>
<h3>Ulaz</h3>
<p>$T \approx 10^4$ testova; u svakom jedan broj $n$, $1 \le n \le 10^{40}$.</p>
<h3>Izlaz</h3>
<p>Za svaki test $Q(n)$.</p>
<h3>Primjer</h3>
<p>$Q(10) = 30$, $Q(100) = 2522$, $Q(1000) = 244274$, $Q(987654321123456789) = 235139898689017607381017686096176798$.</p>
''',
    'solution': None,
},
# ---------------------------------------------------------------- B
{
    'letter': 'B', 'title': 'Kawa Exam', 'title_hr': 'Ispit iz Kawe', 'slug': 'B_kawa_exam',
    'tl': '3 s', 'ml': '512 MiB',
    'statement': r'''
<p>Ispit ima $n$ pitanja s jednim točnim odgovorom $a_i$ (od $10^5$ ponuđenih). Sustav ima $m$ grešaka; $i$-ta greška $(u_i, v_i)$ znači da BaoBao na pitanja $u_i$ i $v_i$ mora dati isti odgovor (i kad je pogrešan). Programeri stignu popraviti samo jednu grešku.</p>
<p>Za svaku grešku $i = 1..m$ odredi najveći broj pitanja koje BaoBao može točno odgovoriti ako se popravi upravo $i$-ta greška (ostale ostaju na snazi).</p>
<h3>Ulaz</h3>
<p>$T$ testova; $1 \le n, m \le 10^5$, $1 \le a_i \le 10^5$, zatim $m$ parova $u_i, v_i$ (mogu se ponavljati, može $u_i = v_i$); $\sum n, \sum m \le 10^6$.</p>
<h3>Izlaz</h3>
<p>Za svaki test jedan redak s $m$ brojeva $c_1, \dots, c_m$ razdvojenih razmakom (bez razmaka na kraju).</p>
<h3>Primjer</h3>
<p>$a = (1, 2, 1, 2, 1, 2, 1)$, greške $(1,2), (1,3), (2,4), (5,6), (5,7)$: <code>6 5 5 5 4</code>. $a = (1, 2, 3)$, greške $(1,2), (1,3), (2,3)$: <code>1 1 1</code>. $a = (12345, 54321)$, greške $(1,2), (1,2)$: <code>1 1</code> — popravkom jedne kopije greške druga i dalje vrijedi.</p>
''',
    'solution': None,
},
# ---------------------------------------------------------------- C
{
    'letter': 'C', 'title': 'Flippy Sequence', 'title_hr': 'Preokretni niz', 'slug': 'C_flippy_sequence',
    'tl': '1 s', 'ml': '256 MiB',
    'statement': r'''
<p>Dani su binarni nizovi $s$ i $t$ duljine $n$. Operacija: odaberi $1 \le l \le r \le n$ i invertiraj $s_l, \dots, s_r$. Operaciju treba izvesti <em>točno dvaput</em> tako da nakon toga bude $s = t$.</p>
<p>Prebroji uređene četvorke $(a_1, a_2, a_3, a_4)$ — prva operacija $[a_1, a_2]$, druga $[a_3, a_4]$ — koje to postižu; četvorke su različite ako se razlikuju u bilo kojoj komponenti.</p>
<h3>Ulaz</h3>
<p>$T$ testova; $1 \le n \le 10^6$ i stringovi $s$, $t$; $\sum n \le 10^7$.</p>
<h3>Izlaz</h3>
<p>Za svaki test broj načina.</p>
<h3>Primjer</h3>
<p>$s = 1, t = 0 \to 0$. $s = 00, t = 11 \to 2$ (četvorke $(1,1,2,2)$ i $(2,2,1,1)$). $s = 01010, t = 00111 \to 6$.</p>
''',
    'solution': None,
},
# ---------------------------------------------------------------- D
{
    'letter': 'D', 'title': 'Magic Multiplication', 'title_hr': 'Čarobno množenje', 'slug': 'D_magic_multiplication',
    'tl': '1 s', 'ml': '256 MiB',
    'statement': r'''
<p>Za $A = a_1 a_2 \dots a_n$ i $B = b_1 b_2 \dots b_m$ (znamenke) definiramo $A \otimes B$ kao <em>konkatenaciju</em> stringova $a_i b_j$ (dekadski zapis umnoška, bez vodećih nula; $0$ se piše kao jedna nula) redom za $i = 1..n$, $j = 1..m$. Npr. $23 \otimes 45 = 8101215$.</p>
<p>Dani su $n$, $m$ i rezultat $C$. Rekonstruiraj $A$ i $B$ (pozitivni, bez vodećih nula, točno $n$ odnosno $m$ znamenaka); ako ima više rješenja, ono s najmanjim $A$, pa najmanjim $B$.</p>
<h3>Ulaz</h3>
<p>$T$ testova; $1 \le n, m \le 2 \cdot 10^5$; $C$ bez vodećih nula duljine najviše $2 \cdot 10^5$; $\sum |C| \le 2 \cdot 10^6$.</p>
<h3>Izlaz</h3>
<p>Za svaki test <code>A B</code> ili <code>Impossible</code>.</p>
<h3>Primjer</h3>
<p>$n = m = 2$, $C = 8101215 \to$ <code>23 45</code>. $n = 3, m = 4$, $C = 100000001000 \to$ <code>101 1000</code>. $n = m = 2$, $C = 80101215 \to$ <code>Impossible</code>. $n = 3, m = 4$, $C = 1000000010000 \to$ <code>Impossible</code>.</p>
''',
    'solution': None,
},
# ---------------------------------------------------------------- E
{
    'letter': 'E', 'title': 'Plants vs. Zombies', 'title_hr': 'Biljke protiv zombija', 'slug': 'E_plants_vs_zombies',
    'tl': '1 s', 'ml': '256 MiB',
    'statement': r'''
<p>$n$ biljaka u nizu; $i$-ta je $i$ metara istočno od kuće, ima obranu $d_i = 0$ i brzinu rasta $a_i$. Robot kreće iz kuće (pozicija $0$); u jednom koraku pomakne se točno $1$ m istočno ili zapadno, a ako se nakon pomaka nalazi na biljci $i$, zalije je: $d_i \mathrel{+}= a_i$. Dopušteno je najviše $m$ koraka (robot smije otići i istočno od $n$ ili zapadno od kuće).</p>
<p>Maksimiziraj obranu vrta $\min_i d_i$.</p>
<h3>Ulaz</h3>
<p>$T$ testova; $2 \le n \le 10^5$, $0 \le m \le 10^{12}$, $1 \le a_i \le 10^5$; $\sum n \le 10^6$.</p>
<h3>Izlaz</h3>
<p>Za svaki test najveća moguća obrana vrta.</p>
<h3>Primjer</h3>
<p>$n = 4, m = 8$, $a = (3, 2, 6, 6) \to 6$ (npr. EEWEEWEE daje $d = (6, 6, 12, 6)$). $n = 3, m = 9$, $a = (10, 10, 1) \to 4$.</p>
''',
    'solution': None,
},
# ---------------------------------------------------------------- F
{
    'letter': 'F', 'title': 'Tournament', 'title_hr': 'Turnir', 'slug': 'F_tournament',
    'tl': '1 s', 'ml': '256 MiB',
    'statement': r'''
<p>$n$ vitezova, $k$ kola. U svakom kolu svaki vitez ima točno jedan dvoboj; svaki par vitezova bori se najviše jednom u svih $k$ kola. Dodatno, za različita kola $i \ne j$ i četiri različita viteza $a, b, c, d$: ako se u kolu $i$ bore $a$–$b$ i $c$–$d$, a u kolu $j$ $a$–$c$, tada se u kolu $j$ moraju boriti $b$–$d$.</p>
<p>Napravi raspored svih dvoboja.</p>
<h3>Ulaz</h3>
<p>$T$ testova; $1 \le n, k \le 1000$; $\sum n, \sum k \le 5000$.</p>
<h3>Izlaz</h3>
<p>Ako je moguće, $k$ redaka; u $i$-tom $n$ brojeva $c_{i,1}, \dots, c_{i,n}$ — u kolu $i$ vitez $j$ bori se protiv $c_{i,j}$. Od svih valjanih rasporeda ispiši leksikografski najmanji (uspoređuje se redak po redak, pa broj po broj). Inače <code>Impossible</code>. Bez razmaka na kraju retka.</p>
<h3>Primjer</h3>
<p>$n = 3, k = 1 \to$ <code>Impossible</code>. $n = 4, k = 3 \to$ <code>2 1 4 3</code> / <code>3 4 1 2</code> / <code>4 3 2 1</code>.</p>
''',
    'solution': None,
},
# ---------------------------------------------------------------- G
{
    'letter': 'G', 'title': 'Repair the Artwork', 'title_hr': 'Popravi umjetničko djelo', 'slug': 'G_repair_the_artwork',
    'tl': '6 s', 'ml': '256 MiB',
    'statement': r'''
<p>Papirna traka s $n$ polja; $a_i = 0$ prazno, $a_i = 1$ DreamGridov uzorak, $a_i = 2$ BaoBaoov uzorak. Operacija: odaberi $1 \le l \le r \le n$ takve da nijedno polje u $[l, r]$ ne sadrži DreamGridov uzorak i isprazni sva polja $[l, r]$.</p>
<p>Na koliko načina (nizovi od $m$ uređenih parova $(l, r)$) se točno $m$ operacija može izvesti tako da na kraju nema BaoBaoovih uzoraka? Odgovor modulo $10^9 + 7$.</p>
<h3>Ulaz</h3>
<p>$1 \le T \le 1000$ testova; $1 \le n \le 100$, $1 \le m \le 10^9$, $a_i \in \{0, 1, 2\}$; najviše $50$ testova ima $n \gt 50$.</p>
<h3>Izlaz</h3>
<p>Za svaki test broj načina modulo $10^9 + 7$.</p>
<h3>Primjer</h3>
<p>$a = (2, 0)$, $m = 2 \to 8$. $a = (2, 1, 0)$, $m = 2 \to 3$. $a = (2, 1, 0)$, $m = 1 \to 1$.</p>
''',
    'solution': None,
},
# ---------------------------------------------------------------- H
{
    'letter': 'H', 'title': 'Mirror', 'title_hr': 'Zrcalo', 'slug': 'H_mirror',
    'tl': '15 s', 'ml': '1024 MiB',
    'statement': r'''
<p>U ravnini su neprozirna trokutasta prepreka i jednostrano zrcalo — usmjerena dužina od $(x_{m,1}, y_{m,1})$ do $(x_{m,2}, y_{m,2})$ čija je desna strana reflektirajuća. U točki $(x_1, y_1)$ je $m$ kamenova koje DreamGrid nosi jedan po jedan do $(x_2, y_2)$; kamen koji podigne smije spustiti samo u cilju. U svakoj točki svog puta mora vidjeti sve kamenove — izravno ili preko zrcala.</p>
<p>Pravila: linija vida koja prolazi unutrašnjošću prepreke ne vrijedi (dodirivanje vrha ili brida je dopušteno); ako linija vida prolazi krajnjom točkom zrcala, vidi i „u zrcalu” i „kroz zrcalo”; refleksija po zakonu odbijanja (upadni i odbijeni zrak u istoj poluravnini); linija vida paralelna zrcalu ne reflektira se i zrcalo tada nije prepreka; DreamGrid se ne smije kretati unutrašnjošću prepreke (smije po bridovima i vrhovima) ni prolaziti kroz zrcalo (smije hodati po njemu, ali s unutrašnjosti zrcala vidi samo stranu s koje je došao).</p>
<p>Odredi najkraći ukupni put za prijenos svih kamenova.</p>
<h3>Ulaz</h3>
<p>$T \approx 100$ testova; $1 \le m \le 10^6$; $x_1, y_1, x_2, y_2$; koordinate zrcala; tri vrha prepreke. Sve koordinate su cijeli brojevi s $|{\cdot}| \le 100$; početak i cilj su izvan prepreke i zrcala; zrcalo i prepreka nemaju zajedničkih točaka; nikoje tri točke nisu kolinearne.</p>
<h3>Izlaz</h3>
<p>Za svaki test realan broj (apsolutna ili relativna greška $\lt 10^{-6}$) ili $-1$ ako je nemoguće.</p>
<h3>Primjer</h3>
<p>$m = 2$, $A = (-2, 0)$, $B = (2, 0)$, zrcalo $(-3, 3) \to (3, 3)$, trokut $(0, 1), (-3, -2), (3, -2)$: $13.416407864999$ (put $A \to C \to B \to C \to A \to C \to B$). Isto, ali zrcalo $(-3, 3) \to (-1, 3)$: $-1$ jer se $A$ ne vidi iz $B$.</p>
''',
    'solution': None,
},
# ---------------------------------------------------------------- I
{
    'letter': 'I', 'title': 'Soldier Game', 'title_hr': 'Igra vojnika', 'slug': 'I_soldier_game',
    'tl': '4 s', 'ml': '256 MiB',
    'statement': r'''
<p>$n$ vojnika sa snagom $a_i$ treba podijeliti u timove od $1$ ili $2$ vojnika; tim od dvojice mora činiti susjedne vojnike ($|i - j| = 1$). Snaga tima je zbroj snaga članova.</p>
<p>Minimiziraj razliku između najveće i najmanje snage tima.</p>
<h3>Ulaz</h3>
<p>$T$ testova; $1 \le n \le 10^5$, $-10^9 \le a_i \le 10^9$; $\sum n \le 10^6$.</p>
<h3>Izlaz</h3>
<p>Za svaki test najmanja razlika.</p>
<h3>Primjer</h3>
<p>$a = (-1, 4, 2, 1, 1) \to 1$ (podjela $[-1, 4], [2], [1, 1]$). $a = (1, 3, 2, 4) \to 2$. $a = (7) \to 0$.</p>
''',
    'solution': None,
},
# ---------------------------------------------------------------- J
{
    'letter': 'J', 'title': 'Books', 'title_hr': 'Knjige', 'slug': 'J_books',
    'tl': '1 s', 'ml': '256 MiB',
    'statement': r'''
<p>U knjižari je $n$ knjiga s cijenama $a_i$. DreamGrid ih pregledava redom $1..n$; ako ima dovoljno novca (barem cijena knjige), kupuje je i novac mu se smanji za cijenu, inače je preskače. Poznato je da je kupio točno $m$ knjiga.</p>
<p>Odredi najveću moguću početnu količinu novca (nenegativan cijeli broj).</p>
<h3>Ulaz</h3>
<p>$T$ testova; $1 \le n \le 10^5$, $0 \le m \le n$, $0 \le a_i \le 10^9$; $\sum n \le 10^6$.</p>
<h3>Izlaz</h3>
<p><code>Impossible</code> ako ni za koju početnu količinu ne kupuje točno $m$ knjiga; <code>Richman</code> ako novac može biti neograničen; inače najveća količina.</p>
<h3>Primjer</h3>
<p>$a = (1, 2, 4, 8)$, $m = 2 \to 6$. $a = (100, 99, 98, 97)$, $m = 0 \to 96$. $a = (10000, 10000)$, $m = 2 \to$ <code>Richman</code>. $a = (0, 0, 0, 0, 1)$, $m = 3 \to$ <code>Impossible</code>.</p>
''',
    'solution': None,
},
# ---------------------------------------------------------------- K
{
    'letter': 'K', 'title': 'Airdrop', 'title_hr': 'Zračna pošiljka', 'slug': 'K_airdrop',
    'tl': '1 s', 'ml': '256 MiB',
    'statement': r'''
<p>Pošiljka je pala u $(x_0, y_0)$; $n$ igrača kreće iz $(x_i, y_i)$. U svakoj jedinici vremena igrač koji nije u $(x_0, y_0)$ prelazi u onu od točaka $(x, y-1), (x, y+1), (x-1, y), (x+1, y)$ koja je Manhattan udaljenošću najbliža pošiljci; pri izjednačenju prioritet je tim redom. Igrač na pošiljci ostaje tamo. Ako se dva ili više igrača nađu u istoj točki različitoj od $(x_0, y_0)$, svi oni ginu.</p>
<p>Poznat je $y_0$, ali ne $x_0$. Po svim cijelim $x_0$ odredi najmanji i najveći mogući broj igrača koji stignu do pošiljke.</p>
<h3>Ulaz</h3>
<p>$T$ testova; $1 \le n \le 10^5$, $1 \le y_0 \le 10^5$, $1 \le x_i, y_i \le 10^5$, sve početne pozicije različite; $\sum n \le 10^6$.</p>
<h3>Izlaz</h3>
<p>Za svaki test <code>p_min p_max</code>.</p>
<h3>Primjer</h3>
<p>$y_0 = 2$, igrači $(1,2), (2,1), (3,5)$: <code>1 3</code> ($x_0 = 3$ daje $1$: prva dva se sudaraju u $(2,2)$; $x_0 = 2$ daje $3$). $y_0 = 3$, igrači $(2,1), (2,5), (4,3)$: <code>0 3</code>. $y_0 = 3$, igrači $(1,3), (4,3)$: <code>2 2</code>.</p>
''',
    'solution': None,
},
# ---------------------------------------------------------------- L
{
    'letter': 'L', 'title': 'Sub-cycle Graph', 'title_hr': 'Podciklički graf', 'slug': 'L_sub_cycle_graph',
    'tl': '2 s', 'ml': '512 MiB',
    'statement': r'''
<p>Jednostavan neusmjeren graf s $n \ge 3$ označenih vrhova i $m$ bridova je <em>podciklički</em> ako mu se dodavanjem nenegativnog broja bridova može dobiti točno jedan jednostavan ciklus na svih $n$ vrhova (povezan graf, svaki vrh stupnja $2$).</p>
<p>Za dane $n$ i $m$ prebroji podcikličke grafove (grafovi su različiti ako imaju različite skupove bridova), modulo $10^9 + 7$.</p>
<h3>Ulaz</h3>
<p>$T \approx 2 \cdot 10^4$ testova; $3 \le n \le 10^5$, $0 \le m \le \frac{n(n-1)}{2}$; $\sum n \le 3 \cdot 10^7$.</p>
<h3>Izlaz</h3>
<p>Za svaki test broj grafova modulo $10^9 + 7$.</p>
<h3>Primjer</h3>
<p>$(4, 2) \to 15$; $(4, 3) \to 12$; $(5, 3) \to 90$.</p>
''',
    'solution': None,
},
# ---------------------------------------------------------------- M
{
    'letter': 'M', 'title': 'Function and Function', 'title_hr': 'Funkcija i funkcija', 'slug': 'M_function_and_function',
    'tl': '1 s', 'ml': '256 MiB',
    'statement': r'''
<p>$f(x)$ je ukupan broj zatvorenih područja („rupa”) u znamenkama broja $x$: znamenke $0, 4, 6, 9$ imaju $1$ rupu, $8$ ima $2$, ostale $0$. Npr. $f(1234) = 1$, $f(5678) = 3$. Definiramo $g_0(x) = x$ i $g_k(x) = f(g_{k-1}(x))$ za $k \ge 1$.</p>
<p>Za dane $x$ i $k$ izračunaj $g_k(x)$.</p>
<h3>Ulaz</h3>
<p>$T \approx 10^5$ testova; $0 \le x, k \le 10^9$ (nula se zadaje kao jedna znamenka <code>0</code>).</p>
<h3>Izlaz</h3>
<p>Za svaki test $g_k(x)$.</p>
<h3>Primjer</h3>
<p>$g_1(123456789) = 5$; $g_1(888888888) = 18$; $g_2(888888888) = 2$; $g_{999999999}(888888888) = 0$; $g_{12345}(98640) = 0$; $g_0(10^9) = 10^9$.</p>
''',
    'solution': None,
},
]
