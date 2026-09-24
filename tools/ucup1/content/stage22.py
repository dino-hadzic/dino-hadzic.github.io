# -*- coding: utf-8 -*-
STAGE = {
    'no': 22,
    'name': 'Stage 22: Shaanxi',
    'source_name': 'Jul 1st, 2023',
    'no_editorial': True,
    'source_html': r'''
<p>Tekst zadatka preveden je prema službenim <a href="https://contest.ucup.ac/download.php?type=attachments&amp;id=1287&amp;r=0">engleskim tekstovima zadataka</a>. Organizatori nisu objavili službena rješenja. Zadatak je dostupan na <a href="https://contest.ucup.ac/contest/1287">Universal Cup Judging System</a>.</p>
''',
}

PROBLEMS = [
# ---------------------------------------------------------------- A
{
    'letter': 'A', 'title': 'Moniphant Sleep', 'title_hr': 'Monifantov san', 'slug': 'A_moniphant_sleep',
    'tl': '3 s', 'ml': '1024 MiB',
    'statement': r'''
<p>Monifant putuje kroz razine sna; na svakoj razini je jedan Mofunfun. Četiri operacije:</p>
<ol>
<li><em>Spavaj</em>: silazi na sljedeću (za jedan dublju) razinu.</li>
<li><em>Probudi se</em>: vraća se na prethodnu (za jedan pliću) razinu.</li>
<li><em>Uvreda</em>: Mofunfun na trenutnoj razini postaje ljut.</li>
<li><em>Odmazda</em>: ako postoji ljuti Mofunfun, Monifant se vraća na najmanju razinu na kojoj je Mofunfun ljut i taj Mofunfun prestaje biti ljut; inače se ništa ne događa.</li>
</ol>
<p>Kad se Monifant vrati na manju razinu, Mofunfuni dubljih razina nestaju (zajedno sa svojom ljutnjom). Dan je niz od $n$ Monifanata; svaki je prije početka izveo operaciju <em>Spavaj</em> $5 \cdot 10^5$ puta. Treba izvršavati operacije $1$–$4$ nad svim Monifantima s indeksima u $[l, r]$ ili (operacija $5$, $l = r$) ispisati razinu sna $l$-tog Monifanta.</p>
<h3>Ulaz</h3>
<p>$1 \le n, q \le 5 \cdot 10^5$; zatim $q$ redaka <code>op l r</code>, $op \in \{1,\dots,5\}$, $1 \le l \le r \le n$.</p>
<h3>Izlaz</h3>
<p>Za svaku operaciju $5$ jedan broj.</p>
<h3>Primjer</h3>
<p>$n = 1$: operacije <code>1</code>, <code>1</code>, <code>1</code>, <code>3</code>, <code>2</code>, <code>1</code>, <code>1</code>, <code>4</code>, <code>5</code> (sve na $[1,1]$) daju $500004$. $n = 3$: <code>2 1 3</code>, <code>3 1 3</code>, <code>1 1 3</code>, <code>1 1 3</code>, <code>5 1 1</code>, <code>4 1 3</code>, <code>5 1 1</code> daju $500001$, $499999$.</p>
''',
    'solution': None,
},
# ---------------------------------------------------------------- B
{
    'letter': 'B', 'title': 'Click the Circle', 'title_hr': 'Klikni krug', 'slug': 'B_click_the_circle',
    'tl': '5 s', 'ml': '1024 MiB',
    'statement': r'''
<p>Izmijenjena verzija igre osu!. Dva tipa objekata, svi krugovi imaju polumjer $r$:</p>
<ol>
<li><em>Krug</em> $(c_x, c_y, t)$: središte $(c_x, c_y)$, prisutan u vremenu $[t - d, t + d]$.</li>
<li><em>Klizač</em> $(s_x, s_y, t_x, t_y, u, v)$: sastoji se od dva zasebna objekta — pokretnog kruga i okvira koji drži putanju. U trenutku $u - d$ krug i okvir se pojavljuju sa središtem kruga u $(s_x, s_y)$; od $u$ do $v$ središte se jednoliko giba do $(t_x, t_y)$; nakon $v + d$ oboje nestaju.</li>
</ol>
<p>Dva objekta se sijeku ako u nekom trenutku oba postoje i njihovi se oblici preklapaju (uključivo rubovi). Prebroji parove objekata koji se sijeku.</p>
<h3>Ulaz</h3>
<p>$1 \le n, r, d \le 10^3$; zatim $n$ objekata: <code>1 cx cy t</code> ili <code>2 sx sy tx ty u v</code>; koordinate u $[1, 10^4]$, $1 \le t, u, v \le 10^3$, $u \lt v$.</p>
<h3>Izlaz</h3>
<p>Broj parova.</p>
<h3>Primjer</h3>
<p>$r = d = 1$: krugovi $(1,1,2)$ i $(2,2,3)$: $1$; krugovi $(1,1,2)$ i $(3,2,3)$: $0$; krug $(3,3,2)$ i klizač $(5,5,5,1,2,4)$: $3$; klizači $(1,1,1,5,2,4)$ i $(5,5,5,1,2,4)$: $2$; klizači $(10,1,10,20,2,4)$ i $(1,10,20,10,2,4)$: $6$.</p>
''',
    'solution': None,
},
# ---------------------------------------------------------------- C
{
    'letter': 'C', 'title': 'Tree', 'title_hr': 'Stablo', 'slug': 'C_tree',
    'tl': '5 s', 'ml': '1024 MiB',
    'statement': r'''
<p>Stablo s $n$ vrhova; vrh $i$ ima boju $a_i$, a $i$-ti brid spaja $fa_i$ i $i + 1$, ima boju $fc_i$ i duljinu $fw_i$. Jednostavan put je <em>dobar</em> ako svi vrhovi na njemu imaju istu boju i svi bridovi na njemu imaju istu boju (boja vrhova i boja bridova mogu se razlikovati).</p>
<p>$q$ operacija: boja vrha $x_i$ postaje $c_i$. Na početku i nakon svake operacije ispiši najveću duljinu dobrog puta.</p>
<h3>Ulaz</h3>
<p>$1 \le n, q \le 2 \cdot 10^5$; $a_1..a_n$ ($1 \le a_i \le n$); $fa_2..fa_n$ ($1 \le fa_i \lt i$); $fc_2..fc_n$ ($1 \le fc_i \le n$); $fw_2..fw_n$ ($0 \le fw_i \le 10^9$); $q$ redaka $x_i\ c_i$.</p>
<h3>Izlaz</h3>
<p>$q + 1$ redaka.</p>
<h3>Primjer</h3>
<p>$n = 5$, $a = (5,4,3,4,5)$, $fa = (1,2,3,1)$, $fc = (2,2,2,2)$, $fw = (4,9,2,6)$, operacije $(2,5), (4,5), (5,4), (3,5), (2,1)$: izlaz $6, 10, 10, 4, 15, 2$.</p>
''',
    'solution': None,
},
# ---------------------------------------------------------------- D
{
    'letter': 'D', 'title': 'Alice and Bob', 'title_hr': 'Alice i Bob', 'slug': 'D_alice_and_bob',
    'tl': '1 s', 'ml': '1024 MiB',
    'statement': r'''
<p>Alice i Bob naizmjence (Alice prva) izvode operaciju nad permutacijom $p$: preslože elemente $p_1, \dots, p_{p_1}$ u proizvoljan redoslijed. Igrač koji izvede dvije operacije s istom vrijednošću $p_1$ gubi. Oba igraju optimalno.</p>
<p>Koliko permutacija veličine $n$ Bob dobiva? Odgovor modulo $998\,244\,353$.</p>
<h3>Ulaz</h3>
<p>$1 \le n \le 10^7$.</p>
<h3>Izlaz</h3>
<p>Jedan broj.</p>
<h3>Primjer</h3>
<p>$n = 1 \to 1$; $n = 2 \to 1$; $n = 10 \to 997920$; $n = 100 \to 188898954$.</p>
''',
    'solution': None,
},
# ---------------------------------------------------------------- E
{
    'letter': 'E', 'title': 'Neighbourhood', 'title_hr': 'Susjedstvo', 'slug': 'E_neighbourhood',
    'tl': '10 s', 'ml': '1024 MiB',
    'statement': r'''
<p>Stablo s $n$ vrhova i težinskim bridovima $w_i$. $q$ operacija:</p>
<ul>
<li><code>1 i c</code> — $w_i := c$;</li>
<li><code>2 x d</code> — prebroji vrhove $y$ za koje je udaljenost od $x$ do $y$ najviše $d$.</li>
</ul>
<h3>Ulaz</h3>
<p>$2 \le n \le 2 \cdot 10^5$, $1 \le q \le 2 \cdot 10^5$; $n - 1$ bridova $x_i\ y_i\ w_i$ ($1 \le w_i \le 10^9$); operacije s $1 \le i \le n - 1$, $1 \le c \le 10^9$, $0 \le d \le 2 \cdot 10^{14}$.</p>
<h3>Izlaz</h3>
<p>Za svaku operaciju tipa 2 jedan broj.</p>
<h3>Primjer</h3>
<p>Bridovi $(1,2,3), (2,3,1)$; operacije <code>2 2 1</code>, <code>2 1 3</code>, <code>2 3 4</code>, <code>1 1 1</code>, <code>2 2 1</code>, <code>2 1 0</code>, <code>2 3 1</code>: izlaz $2, 2, 3, 3, 1, 2$.</p>
''',
    'solution': None,
},
# ---------------------------------------------------------------- F
{
    'letter': 'F', 'title': 'Cover', 'title_hr': 'Pokrivanje', 'slug': 'F_cover',
    'tl': '5 s', 'ml': '1024 MiB',
    'statement': r'''
<p>Stablo s $n$ vrhova, stupanj svakog vrha najviše $k$. Dano je $m$ putova $(a_i, b_i)$ s težinama $w_i$; put pokriva brid $e$ ako uklanjanje $e$ razdvaja $a_i$ i $b_i$. Odaberi podskup $S$ putova tako da je svaki brid pokriven najviše jednim putem iz $S$ i $\sum_{i \in S} w_i$ bude najveći.</p>
<h3>Ulaz</h3>
<p>$2 \le n \le 10^5$, $0 \le m \le 5 \cdot 10^5$, $1 \le k \le 12$; $n - 1$ bridova; $m$ redaka $a_i\ b_i\ w_i$ ($a_i \ne b_i$, $0 \le w_i \le 10^9$).</p>
<h3>Izlaz</h3>
<p>Najveći zbroj.</p>
<h3>Primjer</h3>
<p>$n = 5$, bridovi $1\text{-}2, 1\text{-}3, 2\text{-}4, 2\text{-}5$; putovi $(3,2,8), (5,4,10), (3,1,2), (1,2,7), (2,1,2), (1,2,1), (5,2,3)$: $19$.</p>
''',
    'solution': None,
},
# ---------------------------------------------------------------- G
{
    'letter': 'G', 'title': 'Teleport', 'title_hr': 'Teleport', 'slug': 'G_teleport',
    'tl': '1 s', 'ml': '1024 MiB',
    'statement': r'''
<p>Mreža $n \times n$ točaka $(x, y)$, $1 \le x, y \le n$; neke su neprohodne (<code>*</code>), ostale prohodne (<code>.</code>). Iz $(x, y)$ se u jednoj sekundi može teleportirati u $(x \pm 1, y)$, $(x, y \pm 1)$ ili $f_i(x, y)$ za bilo koji $0 \le i \le k$, gdje je $f_0(x, y) = (x, y)$ i $f_i(x, y) = f_{i-1}(y + 1, x)$. Cilj izvan mreže ili neprohodan nije dopušten.</p>
<p>Nađi najkraće vrijeme od $(1,1)$ do $(n,n)$ ili $-1$.</p>
<h3>Ulaz</h3>
<p>$1 \le n, k \le 5000$; $n$ redaka po $n$ znakova; $(1,1)$ i $(n,n)$ su prohodne.</p>
<h3>Izlaz</h3>
<p>Jedan broj.</p>
<h3>Primjer</h3>
<p>Mreža <code>.*.</code>/<code>.*.</code>/<code>...</code>: za $k = 2$ odgovor je $3$, za $k = 3$ odgovor je $2$.</p>
''',
    'solution': None,
},
# ---------------------------------------------------------------- H
{
    'letter': 'H', 'title': 'Function', 'title_hr': 'Funkcija', 'slug': 'H_function',
    'tl': '1 s', 'ml': '1024 MiB',
    'statement': r'''
<p>Funkcija $f$ zadana je s $f(x) = 0$ za $x \gt n$ i $f(x) = 1 + \sum_{k=2}^{20210926} f(kx)$ inače. Izračunaj $f(1) \bmod 998\,244\,353$.</p>
<h3>Ulaz</h3>
<p>$1 \le n \le 10^9$.</p>
<h3>Izlaz</h3>
<p>Jedan broj.</p>
<h3>Primjer</h3>
<p>$n = 1 \to 1$; $n = 2 \to 2$; $n = 100 \to 949$.</p>
''',
    'solution': None,
},
# ---------------------------------------------------------------- I
{
    'letter': 'I', 'title': 'Digit', 'title_hr': 'Znamenka', 'slug': 'I_digit',
    'tl': '2.5 s', 'ml': '1024 MiB',
    'statement': r'''
<p>Dan je pozitivan $n$. U svakom koraku: uniformno slučajno odaberi znamenku $d$ dekadskog zapisa $n$ i postavi $n := n \cdot (d + 1)$. Izračunaj očekivani broj koraka dok $n$ ne prijeđe $N$, modulo $998\,244\,353$.</p>
<h3>Ulaz</h3>
<p>$1 \le T \le 200$ testova; $1 \le n \le N \le 10^{18}$.</p>
<h3>Izlaz</h3>
<p>Za svaki test jedan broj; dokazivo odgovor uvijek postoji.</p>
<h3>Primjer</h3>
<p>$(1, 10) \to 3$; $(1, 100) \to 4$; $(1, 1000) \to 942786340$.</p>
''',
    'solution': None,
},
# ---------------------------------------------------------------- J
{
    'letter': 'J', 'title': 'Leaves', 'title_hr': 'Listovi', 'slug': 'J_leaves',
    'tl': '2 s', 'ml': '64 MiB',
    'statement': r'''
<p>Binarno stablo s $n$ vrhova (svaki unutarnji vrh ima točno dva djeteta), listovi imaju oznake $a_u$. Obilazak stabla (lijevo dijete pa desno) daje niz oznaka listova. Točno $m$ puta: odaberi unutarnji vrh i zamijeni mu lijevo i desno dijete. Odredi leksikografski najmanji niz koji se može dobiti.</p>
<h3>Ulaz</h3>
<p>$n \le 1000$ neparan, $0 \le m \le \frac{n-1}{2}$; zatim $n$ redaka: <code>1 l r</code> (djeca vrha $i$, $l, r \gt i$) ili <code>2 a</code> (list s oznakom $1 \le a \le 10^9$).</p>
<h3>Izlaz</h3>
<p>$\frac{n+1}{2}$ brojeva.</p>
<h3>Primjer</h3>
<p>$n = 3$, $m = 0$, listovi $1, 2$: <code>1 2</code>. $n = 7$, vrh $1$ ima djecu $2,3$; $2$ ima $4,5$; $3$ ima $6,7$; listovi $4,2,3,1$: za $m = 1$ izlaz <code>2 4 3 1</code>, za $m = 2$ izlaz <code>1 3 4 2</code>.</p>
''',
    'solution': None,
},
# ---------------------------------------------------------------- K
{
    'letter': 'K', 'title': 'water235', 'title_hr': 'water235', 'slug': 'K_water235',
    'tl': '1 s', 'ml': '1024 MiB',
    'statement': r'''
<p>Matrica $N \times M$. Po pravilima Minecrafta, prazno polje s barem dva susjedna (po bridu) polja ispunjena vodom i samo se ispuni vodom; postupak se ponavlja dok je moguće. Odaberi najmanji broj polja koja početno ispuniš vodom tako da na kraju sva polja budu ispunjena.</p>
<h3>Ulaz</h3>
<p>$N$ i $M$, $1 \le N \cdot M \le 10^6$.</p>
<h3>Izlaz</h3>
<p>Najmanji broj jedinica, zatim $N$ redaka matrice $0/1$ ($1$ = početno ispunjeno). Bilo koje optimalno rješenje se prihvaća.</p>
<h3>Primjer</h3>
<p>$2 \times 1$: $2$, matrica <code>1</code>/<code>1</code>. $3 \times 3$: $3$, npr. <code>1 0 1</code>/<code>0 0 0</code>/<code>0 1 0</code>.</p>
''',
    'solution': None,
},
# ---------------------------------------------------------------- L
{
    'letter': 'L', 'title': 'Square', 'title_hr': 'Kvadrat', 'slug': 'L_square',
    'tl': '1 s', 'ml': '1024 MiB',
    'statement': r'''
<p>Pozitivan cijeli broj $x$ u jednoj operaciji možeš pretvoriti u $x - 1$ ili u $x + \left\lfloor \sqrt{2x} + 1.5 \right\rfloor$. Nađi najmanji broj operacija da od $x$ dobiješ $y$.</p>
<h3>Ulaz</h3>
<p>$1 \le T \le 10^5$ testova; $1 \le x, y \le 10^{18}$.</p>
<h3>Izlaz</h3>
<p>Za svaki test jedan broj.</p>
<h3>Primjer</h3>
<p>$5 \to 1$: $4$; $1 \to 5$: $3$.</p>
''',
    'solution': None,
},
# ---------------------------------------------------------------- M
{
    'letter': 'M', 'title': 'Delete the Tree', 'title_hr': 'Izbriši stablo', 'slug': 'M_delete_the_tree',
    'tl': '1 s', 'ml': '1024 MiB',
    'statement': r'''
<p>Dano je stablo s $n$ vrhova. Operacija: odaberi skup postojećih vrhova među kojima nema bridova; za svaki odabrani vrh $v$ dodaj brid između svakog para trenutnih susjeda od $v$, zatim izbriši $v$ i sve njegove bridove (redoslijed unutar jedne operacije ne utječe na rezultat; mogu nastati višestruki bridovi).</p>
<p>U najviše $10$ operacija izbriši sve vrhove. Rješenje sigurno postoji; ispiši bilo koje.</p>
<h3>Ulaz</h3>
<p>$3 \le n \le 500$; $n - 1$ različitih bridova $x_i \lt y_i$.</p>
<h3>Izlaz</h3>
<p>Broj operacija $m$ ($0 \le m \le 10$), zatim $m$ redaka: $k$ i $k$ različitih odabranih vrhova.</p>
<h3>Primjer</h3>
<p>Bridovi $1\text{-}2, 1\text{-}3, 1\text{-}4, 4\text{-}5$: npr. $4$ operacije — $\{1, 5\}$, $\{2\}$, $\{4\}$, $\{3\}$.</p>
''',
    'solution': None,
},
]
