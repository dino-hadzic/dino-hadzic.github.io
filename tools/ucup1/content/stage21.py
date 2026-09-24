# -*- coding: utf-8 -*-
STAGE = {
    'no': 21,
    'name': 'Stage 21: Shandong',
    'source_name': 'Jul 1st, 2023',
    'no_editorial': True,
    'source_html': r'''
<p>Tekst zadatka preveden je prema službenim <a href="https://contest.ucup.ac/download.php?type=attachments&amp;id=1277&amp;r=0">engleskim tekstovima zadataka</a>. Organizatori nisu objavili službena rješenja. Zadatak je dostupan na <a href="https://contest.ucup.ac/contest/1277">Universal Cup Judging System</a>.</p>
''',
}

PROBLEMS = [
# ---------------------------------------------------------------- A
{
    'letter': 'A', 'title': 'Colorful Segments', 'title_hr': 'Šareni segmenti', 'slug': 'A_colorful_segments',
    'tl': '4 s', 'ml': '1024 MiB',
    'statement': r'''
<p>Na brojevnom pravcu je $n$ segmenata $[l_i, r_i]$ boje $c_i \in \{0, 1\}$ ($0$ crvena, $1$ plava). Odaberi podskup segmenata (može i prazan) tako da svaka dva odabrana segmenta koja se preklapaju imaju istu boju. Segmenti $i$ i $j$ se preklapaju ako postoji realan $x$ s $l_i \le x \le r_i$ i $l_j \le x \le r_j$.</p>
<p>Izračunaj broj načina odabira modulo $998\,244\,353$.</p>
<h3>Ulaz</h3>
<p>$T$ testova; u svakom $1 \le n \le 10^5$ i $n$ redaka $l_i\ r_i\ c_i$ ($1 \le l_i \le r_i \le 10^9$). Zbroj $n$ ne prelazi $5 \cdot 10^5$.</p>
<h3>Izlaz</h3>
<p>Za svaki test jedan broj.</p>
<h3>Primjer</h3>
<p>Segmenti $[1,5]_0, [3,6]_1, [4,7]_0$: $5$ (ne mogu se zajedno uzeti 1. i 2., ni 2. i 3.). Segmenti $[1,5]_0, [7,9]_1, [3,6]_0$: $8$.</p>
''',
    'solution': None,
},
# ---------------------------------------------------------------- B
{
    'letter': 'B', 'title': 'Be Careful 2', 'title_hr': 'Budi oprezan 2', 'slug': 'B_be_careful_2',
    'tl': '12 s', 'ml': '1024 MiB',
    'statement': r'''
<p>Pravokutnik s donjim lijevim kutom $(0,0)$ i gornjim desnim $(n, m)$ sadrži $k$ zabranjenih točaka $(x_i, y_i)$. Kvadrat s donjim lijevim kutom $(x, y)$ i stranicom $d$ smije se nacrtati ako su $x, y$ nenegativni cijeli, $d$ pozitivan cijeli, $x + d \le n$, $y + d \le m$ i ni za jednu zabranjenu točku ne vrijedi $x \lt x_i \lt x + d$ i $y \lt y_i \lt y + d$ (točke na rubu kvadrata su dopuštene).</p>
<p>Izračunaj zbroj površina svih dopuštenih kvadrata modulo $998\,244\,353$.</p>
<h3>Ulaz</h3>
<p>$2 \le n, m \le 10^9$, $1 \le k \le 5 \cdot 10^3$; zatim $k$ različitih točaka, $0 \lt x_i \lt n$, $0 \lt y_i \lt m$.</p>
<h3>Izlaz</h3>
<p>Jedan broj.</p>
<h3>Primjer</h3>
<p>$n = m = 3$, točka $(2,2)$: $21$ ($9$ kvadrata stranice $1$ i $3$ kvadrata stranice $2$). $n = m = 5$, točke $(2,1), (2,4)$: $126$.</p>
''',
    'solution': None,
},
# ---------------------------------------------------------------- C
{
    'letter': 'C', 'title': 'Connected Intervals', 'title_hr': 'Povezani intervali', 'slug': 'C_connected_intervals',
    'tl': '1 s', 'ml': '256 MiB',
    'statement': r'''
<p>Dano je stablo s $n$ vrhova. Interval $[l, r]$ je <em>povezan</em> ako inducirani podgraf na skupu vrhova $\{v_l, \dots, v_r\}$ ima točno jednu komponentu povezanosti. Prebroji povezane intervale.</p>
<h3>Ulaz</h3>
<p>$T$ testova; $1 \le n \le 3 \cdot 10^5$, zatim $n - 1$ bridova. Zbroj $n$ ne prelazi $3 \cdot 10^5$.</p>
<h3>Izlaz</h3>
<p>Za svaki test broj povezanih intervala.</p>
<h3>Primjer</h3>
<p>Put $1\text{-}2\text{-}3\text{-}4$: $10$. Zvijezda s bridovima $1\text{-}2, 2\text{-}3, 2\text{-}4$: $9$ (svi osim $[3,4]$).</p>
''',
    'solution': None,
},
# ---------------------------------------------------------------- D
{
    'letter': 'D', 'title': 'DS Team Selection 2', 'title_hr': 'Odabir tima za strukture podataka 2', 'slug': 'D_ds_team_selection_2',
    'tl': '2 s', 'ml': '1024 MiB',
    'statement': r'''
<p>Niz $a$ duljine $n$ i $q$ upita:</p>
<ol>
<li><code>1 v</code> — svaki $a_i$ postaje $\min(a_i, v)$;</li>
<li><code>2</code> — svaki $a_i$ postaje $a_i + i$;</li>
<li><code>3 l r</code> — ispiši $\sum_{i=l}^{r} a_i$.</li>
</ol>
<h3>Ulaz</h3>
<p>$1 \le n, q \le 2 \cdot 10^5$; $0 \le a_i \le 10^{12}$; $0 \le v \le 10^{12}$; $1 \le l \le r \le n$.</p>
<h3>Izlaz</h3>
<p>Za svaki upit tipa 3 jedan broj.</p>
<h3>Primjer</h3>
<p>$a = (6, 14, 14, 6, 3, 6, 4, 13, 10, 3, 12, 5, 11)$, upiti <code>1 2</code>, <code>2</code>, <code>2</code>, <code>2</code>, <code>1 11</code>, <code>3 4 6</code>, <code>2</code>, <code>1 6</code>, <code>2</code>, <code>1 9</code>, <code>3 2 13</code>: izlaz $33$, $107$.</p>
''',
    'solution': None,
},
# ---------------------------------------------------------------- E
{
    'letter': 'E', 'title': 'Computational Geometry', 'title_hr': 'Računalna geometrija', 'slug': 'E_computational_geometry',
    'tl': '2 s', 'ml': '1024 MiB',
    'statement': r'''
<p>Dan je konveksan poligon $P$ s $n$ vrhova. Odaberi tri vrha $a, b, c$ u smjeru suprotnom od kazaljke na satu tako da od $b$ do $c$ (u tom smjeru) ima točno $k$ bridova poligona ($a$ nije krajnja točka tih bridova). Neka je $Q$ poligon omeđen dužinama $ab$, $ac$ i tih $k$ bridova (ima $k + 2$ stranice; $ab$ i $ac$ se smiju poklapati s bridovima $P$).</p>
<p>Nađi najveću moguću površinu $Q$.</p>
<h3>Ulaz</h3>
<p>$T$ testova; $3 \le n \le 10^5$, $1 \le k \le n - 2$; vrhovi $(x_i, y_i)$, $|x_i|, |y_i| \le 10^9$, u pozitivnom smjeru, površina pozitivna, bez ponovljenih vrhova (tri vrha mogu biti kolinearna). Zbroj $n$ ne prelazi $10^5$.</p>
<h3>Izlaz</h3>
<p>Za svaki test realan broj; dopuštena relativna ili apsolutna greška $\lt 10^{-9}$.</p>
<h3>Primjer</h3>
<p>Trokut $(0,0),(1,0),(0,1)$, $k = 1$: $0.5$. Osmerokut $(1,2),(3,1),(5,1),(7,3),(8,6),(5,8),(3,7),(1,5)$, $k = 3$: $26.5$. Sedmerokut $(3,6),(1,1),(3,1),(7,1),(8,1),(5,6),(4,6)$, $k = 2$: $20$.</p>
''',
    'solution': None,
},
# ---------------------------------------------------------------- F
{
    'letter': 'F', 'title': 'Puzzle: Sashigane', 'title_hr': 'Zagonetka: Sashigane', 'slug': 'F_puzzle_sashigane',
    'tl': '1 s', 'ml': '1024 MiB',
    'statement': r'''
<p>Ploča $n \times n$ ima točno jedno crno polje $(b_i, b_j)$; ostala su bijela. Pokrij sva bijela polja L-oblicima tako da je svako bijelo polje pokriveno točno jednim L-oblikom, crno nijednim, a oblici ne izlaze iz ploče.</p>
<p>L-oblik je zadan s $(r, c, h, w)$: $(r, c)$ je pregib, $h \ne 0$ i $w \ne 0$ zadaju smjer i duljinu krakova, $1 \le r + h \le n$, $1 \le c + w \le n$. Oblik sadrži polja $(i, c)$ za $i$ između $r$ i $r + h$ te polja $(r, j)$ za $j$ između $c$ i $c + w$.</p>
<h3>Ulaz</h3>
<p>$1 \le n \le 10^3$, $1 \le b_i, b_j \le n$.</p>
<h3>Izlaz</h3>
<p>Ako rješenje postoji, <code>Yes</code>, zatim broj oblika $k$ ($0 \le k \le \frac{n^2 - 1}{3}$) i $k$ redaka <code>r c h w</code>; bilo koje ispravno rješenje se prihvaća. Inače <code>No</code>.</p>
<h3>Primjer</h3>
<p>$n = 5$, crno $(3,4)$: <code>Yes</code>, npr. $6$ oblika <code>5 1 -1 3</code>, <code>1 2 1 3</code>, <code>3 1 -2 1</code>, <code>4 3 -1 -1</code>, <code>4 5 1 -1</code>, <code>2 5 1 -2</code>. $n = 1$: <code>Yes</code>, $0$.</p>
''',
    'solution': None,
},
# ---------------------------------------------------------------- G
{
    'letter': 'G', 'title': 'Gem Island 2', 'title_hr': 'Otok dragulja 2', 'slug': 'G_gem_island_2',
    'tl': '2 s', 'ml': '1024 MiB',
    'statement': r'''
<p>$n$ kutija u nizu, u svakoj početno jedna kuglica. Točno $d$ puta: odaberi uniformno slučajno kuglicu među svima i u njezinu kutiju dodaj još jednu (u $i$-toj operaciji svaka kuglica ima vjerojatnost $\frac{1}{n + i - 1}$). Neka su brojevi kuglica poredani nerastuće $a_1 \ge a_2 \ge \dots \ge a_n$.</p>
<p>Izračunaj očekivanje $\sum_{i=1}^{r} a_i$ modulo $998\,244\,353$.</p>
<h3>Ulaz</h3>
<p>$1 \le n, d \le 1.5 \cdot 10^7$, $1 \le r \le n$.</p>
<h3>Izlaz</h3>
<p>Jedan broj.</p>
<h3>Primjer</h3>
<p>$(2, 3, 1) \to 499122180$; $(3, 3, 2) \to 698771052$; $(5, 10, 3) \to 176512750$.</p>
''',
    'solution': None,
},
# ---------------------------------------------------------------- H
{
    'letter': 'H', 'title': 'Not Another Path Query Problem', 'title_hr': 'Ne još jedan upit o putovima', 'slug': 'H_not_another_path_query_problem',
    'tl': '4 s', 'ml': '1024 MiB',
    'statement': r'''
<p>Graf s $n$ vrhova i $m$ neusmjerenih bridova težina $w_i$. Vrijednost puta je bitovni AND težina svih bridova na njemu. Za konstantu $V$ i svaki od $q$ upita $(u, v)$ odredi postoji li put od $u$ do $v$ vrijednosti barem $V$.</p>
<h3>Ulaz</h3>
<p>$1 \le n \le 10^5$, $0 \le m \le 5 \cdot 10^5$, $1 \le q \le 5 \cdot 10^5$, $0 \le V \lt 2^{60}$; bridovi $u_i \ne v_i$, $0 \le w_i \lt 2^{60}$ (mogući višestruki bridovi); upiti $u_i \ne v_i$.</p>
<h3>Izlaz</h3>
<p>Za svaki upit <code>Yes</code> ili <code>No</code>.</p>
<h3>Primjer</h3>
<p>$n = 9$, $V = 5$, bridovi $(1,2,8), (1,3,7), (2,4,1), (3,4,14), (2,5,9), (4,5,7), (5,6,6), (3,7,15)$: upiti $(1,6), (2,7), (7,6), (1,8)$ daju <code>Yes</code>, <code>No</code>, <code>Yes</code>, <code>No</code> (npr. $1 \to 3 \to 4 \to 5 \to 6$ ima vrijednost $7 \,\&\, 14 \,\&\, 7 \,\&\, 6 = 6 \ge 5$). $n = 3$, $V = 4$, bridovi $(1,2,3), (1,2,5), (2,3,2), (2,3,6)$, upit $(1,3)$: <code>Yes</code> ($5 \,\&\, 6 = 4$).</p>
''',
    'solution': None,
},
# ---------------------------------------------------------------- I
{
    'letter': 'I', 'title': 'Heap', 'title_hr': 'Gomila', 'slug': 'I_heap',
    'tl': '1 s', 'ml': '256 MiB',
    'statement': r'''
<p>Gomila (heap) veličine $n$ je niz $a_1, \dots, a_n$ u kojem za sve $2 \le i \le n$ vrijedi $a_{\lfloor i/2 \rfloor} \le a_i$ (min-gomila) ili za sve $a_{\lfloor i/2 \rfloor} \ge a_i$ (max-gomila). Umetanje vrijednosti $v$: stavi $a_n := v$, $i := n$; dok je $i \gt 1$: ako je <code>is_max</code> lažno i $a_{\lfloor i/2 \rfloor} \le a_i$, stani; ako je <code>is_max</code> istinito i $a_{\lfloor i/2 \rfloor} \ge a_i$, stani; inače zamijeni $a_{\lfloor i/2 \rfloor}$ i $a_i$ te $i := \lfloor i/2 \rfloor$.</p>
<p>BaoBao je u prazan niz redom umetao $v_1, \dots, v_n$, ali je za $i$-to umetanje vrijednost <code>is_max</code> odredio prema binarnom stringu $b$: $b_i = 0$ znači lažno, $b_i = 1$ istinito. Dani su $v$ i konačni niz $a$; rekonstruiraj leksikografski najmanji $b$.</p>
<h3>Ulaz</h3>
<p>$T$ testova; $1 \le n \le 10^5$; $v_1, \dots, v_n$ ($1 \le v_i \le 10^9$); $a_1, \dots, a_n$ — permutacija od $v$. Zbroj $n$ ne prelazi $10^6$.</p>
<h3>Izlaz</h3>
<p>Za svaki test leksikografski najmanji $b$ ili <code>Impossible</code>.</p>
<h3>Primjer</h3>
<p>$v = (2,3,1,4)$, $a = (4,1,3,2)$: <code>0101</code> (nizovi nakon umetanja: $\{2\}, \{3,2\}, \{1,2,3\}, \{4,1,3,2\}$). $v = (4,5,1,2,3)$, $a = (3,4,1,5,2)$: <code>Impossible</code>. $v = (1,1,2)$, $a = (2,1,1)$: <code>001</code>.</p>
''',
    'solution': None,
},
# ---------------------------------------------------------------- J
{
    'letter': 'J', 'title': 'Triangle City', 'title_hr': 'Trokutasti grad', 'slug': 'J_triangle_city',
    'tl': '2 s', 'ml': '256 MiB',
    'statement': r'''
<p>Grad ima $\frac{n(n+1)}{2}$ raskrižja u $n$ redova; $i$-ti red ima $i$ raskrižja $(i, 1), \dots, (i, i)$. Za sve $1 \le j \le i \lt n$ postoje ceste: $(i,j)\text{-}(i+1,j)$ duljine $a_{i,j}$, $(i,j)\text{-}(i+1,j+1)$ duljine $b_{i,j}$ i $(i+1,j)\text{-}(i+1,j+1)$ duljine $c_{i,j}$, pri čemu $a_{i,j}, b_{i,j}, c_{i,j}$ zadovoljavaju nejednakost trokuta.</p>
<p>Nađi najdulji put od $(1,1)$ do $(n,n)$ koji svaku cestu koristi najviše jednom.</p>
<h3>Ulaz</h3>
<p>$T$ testova; $2 \le n \le 300$; zatim $n-1$ redaka s $a_{i,\cdot}$, $n-1$ redaka s $b_{i,\cdot}$ i $n-1$ redaka s $c_{i,\cdot}$ ($1 \le \cdot \le 10^9$). Zbroj $n$ ne prelazi $5 \cdot 10^3$.</p>
<h3>Izlaz</h3>
<p>Za svaki test tri retka: duljina $l$, broj raskrižja $m$ na putu i $2m$ brojeva $i_1\ j_1\ \dots\ i_m\ j_m$ redom, s $(i_1,j_1) = (1,1)$ i $(i_m,j_m) = (n,n)$. Bilo koje optimalno rješenje se prihvaća; bez suvišnih razmaka na kraju retka.</p>
<h3>Primjer</h3>
<p>$n = 2$, $a = 3$, $b = 2$, $c = 4$: $7$, put $(1,1),(2,1),(2,2)$. $n = 2$, $a = b = c = 1$: $2$, put $(1,1),(2,1),(2,2)$. $n = 3$, $a = (100; 100, 100)$, $b = (1; 100, 1)$, $c = (100; 100, 100)$: $700$, put od $8$ raskrižja $(1,1),(2,1),(3,2),(2,2),(2,1),(3,1),(3,2),(3,3)$.</p>
''',
    'solution': None,
},
# ---------------------------------------------------------------- K
{
    'letter': 'K', 'title': 'Are you a bot?', 'title_hr': 'Jesi li ti bot?', 'slug': 'K_are_you_a_bot',
    'tl': '3 s', 'ml': '1024 MiB',
    'statement': r'''
<p>Niz $a$ je permutacija od $1..n$. Neka je $A_i$ niz $a$ bez $i$-tog elementa. Za niz $p$ različitih elemenata, $G(p)$ je neusmjeren graf s vrhovima $1..|p|$ u kojem su $i \lt j$ spojeni bridom ako za sve $k \in [i, j]$ vrijedi $p_k \in [\min(p_i, p_j), \max(p_i, p_j)]$. $F(p)$ je duljina najkraćeg puta (broj bridova) od $1$ do $|p|$ u $G(p)$. Neka je $f(a) = [F(A_1), \dots, F(A_n)]$.</p>
<p>Za dani niz $b$ nađi bilo koju permutaciju $a$ s $f(a) = b$. Rješenje sigurno postoji.</p>
<h3>Ulaz</h3>
<p>$1 \le T \le 40\,000$ testova; $4 \le n \le 10^5$ i niz $b_1, \dots, b_n$. Zbroj $n$ ne prelazi $5 \cdot 10^5$.</p>
<h3>Izlaz</h3>
<p>Za svaki test jedna permutacija.</p>
<h3>Primjer</h3>
<p>$b = (2,2,1,1) \to$ npr. $1\ 2\ 4\ 3$; $b = (2,2,2,2) \to 2\ 1\ 4\ 3$; $b = (2,1,1,2) \to 1\ 3\ 2\ 4$; $b = (5,5,4,4,4,5,5) \to 3\ 1\ 7\ 2\ 6\ 4\ 5$.</p>
''',
    'solution': None,
},
# ---------------------------------------------------------------- L
{
    'letter': 'L', 'title': 'Difficult Constructive Problem', 'title_hr': 'Težak konstruktivni zadatak', 'slug': 'L_difficult_constructive_problem',
    'tl': '1 s', 'ml': '1024 MiB',
    'statement': r'''
<p>Dan je string $s_1 \dots s_n$ nad $\{0, 1, ?\}$ i broj $k$. Zamijeni svaki <code>?</code> znakom <code>0</code> ili <code>1</code> (različiti upitnici neovisno) tako da broj indeksa $1 \le i \lt n$ sa $s_i \ne s_{i+1}$ bude točno $k$. Među rješenjima ispiši leksikografski najmanje.</p>
<h3>Ulaz</h3>
<p>$T$ testova; $1 \le n \le 10^5$, $0 \le k \lt n$, string $s$. Zbroj $n$ ne prelazi $10^6$.</p>
<h3>Izlaz</h3>
<p>Za svaki test leksikografski najmanji popunjeni string ili <code>Impossible</code>.</p>
<h3>Primjer</h3>
<p><code>1?010??01</code>, $k = 6 \to$ <code>100100101</code>; isti string, $k = 5 \to$ <code>Impossible</code>; <code>100101101</code>, $k = 6 \to$ <code>100101101</code>; $k = 5 \to$ <code>Impossible</code>; <code>????????1</code>, $k = 3 \to$ <code>000000101</code>.</p>
''',
    'solution': None,
},
# ---------------------------------------------------------------- M
{
    'letter': 'M', 'title': 'Trie', 'title_hr': 'Prefiksno stablo', 'slug': 'M_trie',
    'tl': '1 s', 'ml': '1024 MiB',
    'statement': r'''
<p>Prefiksno stablo (trie) je korijensko stablo u kojem je svaki brid označen znakom; korijen predstavlja prazan string, a dijete $v$ roditelja $u$ preko brida sa znakom $c$ predstavlja $s(v) = s(u) + c$; svi predstavljeni stringovi su različiti.</p>
<p>Dano je korijensko stablo s vrhovima $0..n$ (korijen $0$) i $m$ ključnih vrhova $k_1, \dots, k_m$; svi listovi su ključni. Označi svaki brid malim engleskim slovom tako da stablo postane trie. Neka je $B$ niz stringova ključnih vrhova sortiran leksikografski uzlazno. Označi bridove tako da $B$ bude najmanji (nizovi se uspoređuju leksikografski po elementima); među takvim označavanjima ispiši leksikografski najmanji string oznaka.</p>
<h3>Ulaz</h3>
<p>$T$ testova; $1 \le m \le n \le 2 \cdot 10^5$; roditelji $a_1, \dots, a_n$ ($0 \le a_i \lt i$, svaki vrh ima najviše $26$ djece); ključni vrhovi $k_1, \dots, k_m$ (različiti). Zbroj $n$ ne prelazi $2 \cdot 10^5$.</p>
<h3>Izlaz</h3>
<p>Za svaki test string $c_1 \dots c_n$, gdje je $c_i$ slovo na bridu $(a_i, i)$.</p>
<h3>Primjer</h3>
<p>$n = 5$, roditelji $(0,1,1,2,2)$, ključni $1,4,3,5$: <code>abaab</code> ($B = \{$<code>a</code>, <code>aa</code>, <code>aba</code>, <code>abb</code>$\}$). $n = 1$, roditelj $0$, ključni $1$: <code>a</code>.</p>
''',
    'solution': None,
},
]
