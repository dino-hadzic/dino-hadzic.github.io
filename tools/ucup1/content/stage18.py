# -*- coding: utf-8 -*-
STAGE = {
    'no': 18,
    'name': 'Stage 18: Shenzhen',
    'source_name': 'May 27-28, 2023',
    'no_editorial': True,
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
    'solution': None,
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
    'solution': None,
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
    'solution': None,
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
    'solution': None,
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
    'solution': None,
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
    'solution': None,
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
    'solution': None,
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
    'solution': None,
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
    'solution': None,
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
    'solution': None,
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
    'solution': None,
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
    'solution': None,
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
    'solution': None,
},
]
