"""1st Universal Cup – Stage 7: Zaporizhzhia. Uvezeno iz ručno pisanih stranica (import_legacy.py); naputci i
trenerski koraci iz nekadašnjeg retro_stage7.py."""

STAGE = {
    'no': 7,
    'name': 'Stage 7: Zaporizhzhia',
    'source_name': '1st OCPC, Winter 2023, Day 2: Oleksandr Kulkov Contest 3',
    'source_html': r'''
<p>Prijevod službenog rješenja autora Oleksandra Kulkova: <a href="https://contest.ucup.ac/download.php?type=attachments&amp;id=1129&amp;r=1">Tutorial (en)</a>. Tekst zadatka preveden je prema službenim <a href="https://contest.ucup.ac/download.php?type=attachments&amp;id=1129&amp;r=0">engleskim tekstovima zadataka</a>. Zadatak je dostupan na <a href="https://contest.ucup.ac/contest/1129">Universal Cup Judging System</a>.</p>
''',
}

PROBLEMS = [
{
    'letter': 'A',
    'title': 'Square Sum',
    'title_hr': 'Zbroj kvadrata',
    'slug': 'A_square_sum',
    'tl': '2 s',
    'ml': '256 MB',
    'statement': r'''
<p>Zadani su cijeli broj $m$ i niz $z_1, \dots, z_n$. Za svaki $z_i$ izračunaj broj parova cijelih brojeva $x, y$ ($0 \le x, y &lt; m$) takvih da
$$x^2 + y^2 \equiv z_i \pmod m.$$</p>
<h3>Ulaz</h3>
<p>$m$ ($1 \le m \le 10^9$) i $n$ ($1 \le n \le 10^5$), zatim $n$ brojeva $z_i$ ($0 \le z_i &lt; m$).</p>
<h3>Izlaz</h3>
<p>Za svaki $z_i$ broj traženih parova.</p>
''',
    'hints': [
        r'''
<p>Kineski teorem o ostatcima: broj rješenja modulo $m$ je umnožak brojeva rješenja modulo $p^k$ za svaki prosti faktor. Faktoriziraj $m \le 10^9$ probnim dijeljenjem do $\sqrt m$.</p>
''',
        r'''
<p>Modulo $p^k$: podijeli rješenja na ona s $p \nmid \gcd(x,y)$ (broj $f$; Henselovo podizanje daje $f(z,k+1) = p\,f(z,k)$ za $p$ neparan) i ona s $p \mid x, y$ (svode se na $z/p^2$ modulo $p^{k-2}$, s faktorom $p^2$). Baza $k=1$: $p \equiv 1 \pmod 4$: $f = p-1$ ($2(p-1)$ za $z \equiv 0$); $p \equiv 3$: $f = p+1$ ($0$ za $z\equiv0$). Za $p = 2$ gruba sila do $2^3$ pa udvostručavanje.</p>
''',
    ],
    'coach': [
        ('Opažanje 1: CRT rastav',
         r'''
<p>$x^2 + y^2 \equiv z \pmod m$ rastavlja se po prostim potencijama; parovi $(x,y)$ modulo $m$ odgovaraju bijektivno vektorima parova modulo $p_i^{k_i}$. Odgovor za $z$ je $\prod_i N_{p_i^{k_i}}(z \bmod p_i^{k_i})$.</p>
'''),
        ('Opažanje 2: podizanje s $p^k$ na $p^{k+1}$',
         r'''
<p>$x = x_0 + p^k x_1$: uvjet postaje $2(x_0 x_1 + y_0 y_1) \equiv u \pmod p$ — linearna jednadžba u $(x_1, y_1)$. Ako je $p \nmid x_0$ ili $p \nmid y_0$ (i $p \ne 2$), ima točno $p$ rješenja: svako „primitivno” rješenje mod $p^k$ podiže se na $p$ rješenja. Ako $p \mid x_0, y_0$: onda $p^2 \mid z$ i svodi se na $(x/p)^2 + (y/p)^2 \equiv z/p^2 \pmod{p^{k-2}}$ s $p^2$ kopija po rješenju.</p>
'''),
        ('Opažanje 3: baza i $p = 2$',
         r'''
<p>Broj rješenja $x^2 + y^2 \equiv z \pmod p$ je klasičan (Gaussove/Jacobijeve sume): $p - \left(\frac{-1}{p}\right)$ za $z \ne 0$, i $1 + (p-1)\left(1 + \left(\frac{-1}{p}\right)\right)$ za $z = 0$; oduzmi rješenje $(0,0)$ za $f$. Za $p = 2$ linearizacija ne radi (faktor $2$), pa izračunaj $2^1..2^3$ grubom silom i koristi $f(z,k+1) = 2 f(z,k)$ za $k \ge 3$.</p>
'''),
        ('Algoritam i složenost',
         r'''
<p>Faktoriziraj $m$ ($O(\sqrt m)$), za svaki upit izračunaj $g(z \bmod p^k, k)$ rekurzivno (dubina $\le k/2$) za svaki prosti faktor i pomnoži — $O(\log m)$ po upitu. 64-bitna aritmetika (odgovor do $10^{18}$).</p>
'''),
    ],
    'solution': r'''
<p>Neka je $m = p_1^{k_1} \cdots p_n^{k_n}$, gdje su $p_i$ prosti i $k_i &gt; 0$. Prema Kineskom teoremu o ostatcima zadatak možemo riješiti neovisno modulo svaki $p_i^{k_i}$ i pomnožiti rezultate. Neka je $z = z_0 + p^k z_1$ i promotrimo jednadžbu
$$x^2 + y^2 \equiv z \pmod{p^{k+1}}.$$
Zapišemo li $x = x_0 + p^k x_1$ i $y = y_0 + p^k y_1$, uočavamo da je
$$x_0^2 + y_0^2 \equiv z_0 \pmod{p^k},$$
pa jednadžbu možemo prepisati kao
$$2p^k(x_0 x_1 + y_0 y_1) \equiv u p^k \pmod{p^{k+1}},$$
gdje je $u p^k \equiv z - x_0^2 - y_0^2 \pmod{p^{k+1}}$. Dijeljenjem s $p^k$ dobivamo
$$2(x_0 x_1 + y_0 y_1) \equiv u \pmod p.$$
Sada razlikujemo nekoliko slučajeva.</p>
<h3>Slučaj $p &gt; 2$</h3>
<p>Uz poznate $x_0$, $y_0$ i $u$ jednadžbu zapišemo kao
$$\alpha x_1 + \beta y_1 \equiv \gamma \pmod p,$$
gdje su $\alpha, \beta, \gamma$ konstante. Ako je $\alpha \not\equiv 0 \pmod p$ ili $\beta \not\equiv 0 \pmod p$, postoji točno $p$ valjanih parova $(x_1, y_1)$, jer barem jednu nepoznanicu jednoznačno određujemo iz druge.</p>
<p>Što ako je $\alpha \equiv \beta \equiv 0 \pmod p$? Svako takvo rješenje modulo $p^{k+1}$ dobiva se iz rješenja jednadžbe
$$\left(\frac{x}{p}\right)^2 + \left(\frac{y}{p}\right)^2 = \frac{z}{p^2} \pmod{p^{k-1}},$$
pa iz svakog rješenja za $\frac{z}{p^2}$ modulo $p^{k-1}$ dobivamo $p^2$ rješenja. Drugim riječima, neka je $f(z, k)$ broj rješenja $x^2 + y^2 \equiv z \pmod{p^k}$ u kojima barem jedan od $x, y$ nije djeljiv s $p$, a $g(z, k)$ ukupan broj rješenja. Tada je $f(z, k+1) = p f(z, k)$, a
$$g(z, k) = \begin{cases} f(z, k) + p^2 g\!\left(\frac{z}{p^2}, k - 2\right), &amp; z \equiv 0 \pmod{p^2}, \\ f(z, k), &amp; z \not\equiv 0 \pmod{p^2}. \end{cases}$$
Iz $f(z, k+1) = p f(z, k)$ slijedi $f(z, k+1) = p^k f(z, 1)$, pa je bitan samo slučaj $k = 1$.</p>
<h3>Slučaj $p = 2$</h3>
<p>Za $p = 2$ općenito vrijedi
$$x^2 + y^2 \equiv (x_0 + 2^k x_1)^2 + (y_0 + 2^k y_1)^2 \equiv x_0^2 + y_0^2 \pmod{2^{k+1}}.$$
To znači da $k$-ti bit brojeva $x$ i $y$ može biti proizvoljan čim je $x_0^2 + y_0^2 \equiv z \pmod{2^{k+1}}$. Zato $x$ i $y$ tražimo u obliku $x = x_0 + 2^{k-1} x_1$ i $y = y_0 + 2^{k-1} y_1$, gdje je $x_0^2 + y_0^2 \equiv z \pmod{2^k}$ i $x_0, y_0 &lt; 2^{k-1}$. Prema gornjoj činjenici takvih parova $(x_0, y_0)$ ima točno $\frac{f(z, k)}{4}$. Dobivamo
$$2^k(x_0 x_1 + y_0 y_1) \equiv u 2^k \pmod{2^{k+1}}.$$
Identitet vrijedi dok je $2(k-1) \ge k+1$, tj. $k + 1 \ge 4$, i ima $8$ rješenja za $x_1, y_1 &lt; 4$. Zajedno s činjenicom da parova $(x_0, y_0)$ ima $\frac{f(z, k)}{4}$, za $k &gt; 3$ vrijedi $f(z, k+1) = 2 f(z, k)$, a za $k \le 3$ odgovor nalazimo grubom silom.</p>
<h3>Slučaj $k = 1$</h3>
<p>Gornje rješenje daje rekurziju za $p^k$, ali treba obraditi bazni slučaj $k = 1$. Za $p &gt; 2$ može se dokazati (vidi npr. <a href="https://math.stackexchange.com/questions/398200/">math.stackexchange</a>):</p>
<ol>
    <li>Ako je $p \equiv 1 \pmod 4$, tada je $f(z, 1) = 2(p - 1)$ za $z \equiv 0 \pmod p$ i $f(z, 1) = p - 1$ inače.</li>
    <li>Ako je $p \equiv 3 \pmod 4$, tada je $f(z, 1) = 0$ za $z \equiv 0 \pmod p$ i $f(z, 1) = p + 1$ inače.</li>
</ol>
''',
},
{
    'letter': 'B',
    'title': 'Super Meat Bros',
    'title_hr': 'Super Meat Bros',
    'slug': 'B_super_meat_bros',
    'tl': '5 s',
    'ml': '256 MB',
    'statement': r'''
<p>Dva brata imaju neovisne priče. Priča o svakom bratu nastaje tako da se, dok se mangaka ne zasiti, odabere $k \le n$ i doda novi luk priče od $k$ brojeva časopisa: za prvog brata na jedan od $a_k$ načina, za drugog na jedan od $b_k$ načina. Gotove se priče zatim spajaju u jednu uz čuvanje unutarnjeg poretka svake od njih (inače proizvoljno). Zadani su $a_1, \dots, a_n$ i $b_1, \dots, b_n$; izračunaj broj načina da se stvori cjelina od točno $m$ brojeva, modulo $10^9 + 9$.</p>
<h3>Ulaz</h3>
<p>$n$ ($1 \le n \le 300$) i $m$ ($1 \le m \le 10^9$), zatim $a_1, \dots, a_n$ i $b_1, \dots, b_n$ ($1 \le a_i, b_i \le 10^9$).</p>
<h3>Izlaz</h3>
<p>Broj načina modulo $10^9 + 9$.</p>
''',
    'hints': [
        r'''
<p>Funkcije izvodnice: $C = 1/(1-A)$, $D = 1/(1-B)$, a spajanje s čuvanjem poretka daje $f_m = \sum_{i+j=m}\binom{m}{i} c_i d_j$ (binomna konvolucija). Problem je $m \le 10^9$.</p>
''',
        r'''
<p>$c$ i $d$ zadovoljavaju linearne rekurzije stupnja $n$ s korijenima $\lambda_i$, $\mu_j$; tada $f$ zadovoljava linearnu rekurziju stupnja $n^2$ s korijenima $\lambda_i + \mu_j$. Njezin karakteristični polinom izračunaj preko zbrojeva potencija (Newtonovi identiteti: $r_k = \sum_i \binom{k}{i} s_i t_{k-i}$) i polinomnog exp/log, pa $x^m \bmod f(x)$.</p>
''',
    ],
    'coach': [
        ('Opažanje 1: model s funkcijama izvodnicama',
         r'''
<p>Prva priča: nizovi lukova, $C(x) = \sum_k A(x)^k = 1/(1-A(x))$. Isto $D$. Spajanje dvaju nizova duljina $i$, $j$ uz čuvanje poretka: $\binom{i+j}{i}$ načina. Dakle $f_m/m! = \sum (c_i/i!)(d_j/j!)$ — eksponencijalna funkcija izvodnica $F = \hat C \cdot \hat D$.</p>
'''),
        ('Opažanje 2: umnožak EGF-ova linearno rekurzivnih nizova',
         r'''
<p>$c_i = \sum_a \alpha_a \lambda_a^i$, $d_j = \sum_b \beta_b \mu_b^j$ (korijeni karakterističnih polinoma). Tada $f_m = \sum_{a,b} \alpha_a\beta_b (\lambda_a + \mu_b)^m$ — linearna rekurzija čiji su korijeni $\lambda_a + \mu_b$ ($n^2$ komada). Karakteristični polinom: $f(x) = \prod_{a,b}(x - \lambda_a - \mu_b)$, koji leži u idealu $\langle a(c), b(d)\rangle$ (umbralni argument iz rješenja).</p>
'''),
        ('Redukcija: računanje $f(x)$ bez korijena',
         r'''
<p>Zbrojevi potencija korijena: $s_k = \sum \lambda_a^k$ iz $a(x)$ preko $\log$ obrnutog polinoma ($-\sum s_k x^k/k$), isto $t_k$. Zbrojevi potencija $\lambda_a + \mu_b$: $r_k = \sum_{i}\binom{k}{i} s_i t_{k-i}$ (binomna konvolucija). Onda $x^{n^2} f(1/x) = \exp(-\sum r_k x^k / k)$ — polinomni exp do stupnja $n^2 = 9\cdot10^4$.</p>
'''),
        ('Algoritam i složenost',
         r'''
<p>(1) $f_0..f_{n^2-1}$: $c$, $d$ rekurzijom, binomna konvolucija. (2) $f(x)$ kao gore; modul $10^9+9$ nije NTT-prijateljski, pa treba FFT s rastavom koeficijenata ili tri NTT modula + CRT. (3) $x^m \bmod f(x)$ brzim potenciranjem polinoma. Ukupno $O(n^2 \log n^2 \log m)$ uz brzo množenje.</p>
'''),
    ],
    'solution': r'''
<p><b>Formalna formulacija.</b> Održavamo dva niza. Postoji $a_k$ načina da se $k$ objekata doda prvom nizu i $b_k$ načina za drugi niz. Zadani su $a_1, \dots, a_n$ i $b_1, \dots, b_n$. Novi niz nastaje ovako:</p>
<ol>
    <li>nula ili više puta dodamo proizvoljan broj objekata prvom nizu;</li>
    <li>nula ili više puta dodamo proizvoljan broj objekata drugom nizu;</li>
    <li>spojimo dva niza u jedan čuvajući unutarnji poredak početnih nizova.</li>
</ol>
<p>Koliko različitih završnih nizova ima točno $m$ objekata?</p>
<h3>1. Binomni koeficijenti</h3>
<p>Neka je $A(x) = a_1 x + a_2 x^2 + \dots + a_n x^n$ i $B(x) = b_1 x + b_2 x^2 + \dots + b_n x^n$. Tada je
$$C = \frac{1}{1 - A} = 1 + A + A^2 + \dots = c_0 + c_1 x + c_2 x^2 + \dots$$
funkcija izvodnica niza dobivenog u prvom koraku, a
$$D = \frac{1}{1 - B} = 1 + B + B^2 + \dots = d_0 + d_1 x + d_2 x^2 + \dots$$
funkcija izvodnica niza dobivenog u drugom koraku. Konačno,
$$F = \sum_{i,j} \binom{i+j}{i} c_i d_j x^{i+j} = f_0 + f_1 x + f_2 x^2 + \dots$$
je funkcija izvodnica završnog niza, pa je naš cilj izračunati $f_m$. Za male $m$ svi $f_m$ računaju se istodobno kao konvolucija nizova $\frac{c_k}{k!}$ i $\frac{d_k}{k!}$. Međutim, u ovom zadatku $m$ može biti proizvoljno velik. Ključno je uočiti da je $f_0, f_1, \dots$ zapravo linearna rekurzija stupnja najviše $n^2$.</p>
<h3>2. Umbralni račun</h3>
<p>Neka je $T : R[c, d] \to R$ linearni funkcional takav da
$$T(c^i d^j) = c_i d_j.$$
Tada možemo pisati
$$T((c + d)^k) = f_k.$$
Iz teksta zadatka znamo
$$c_m = a_1 c_{m-1} + a_2 c_{m-2} + \dots + a_n c_{m-n}, \qquad d_m = b_1 d_{m-1} + b_2 d_{m-2} + \dots + b_n d_{m-n}.$$
Neka su $a(x) = x^n - a_1 x^{n-1} - \dots - a_n$ i $b(x) = x^n - b_1 x^{n-1} - \dots - b_n$ karakteristični polinomi nizova $c_i$ odnosno $d_j$. Tada vrijedi
$$T(c^i d^j a(c)) = T(c^i d^j b(d)) = 0$$
za sve $i, j \ge 0$. Isto vrijedi i za linearnu ljusku takvih polinoma. Drugim riječima,
$$T(X) = T(Y)$$
za sve $X(c, d)$ i $Y(c, d)$ takve da $X - Y \in \langle a(c), b(d) \rangle$, gdje je $\langle a, b \rangle$ ideal generiran s $a$ i $b$.</p>
<h3>3. Složeni zbroj</h3>
<p>Da bismo dokazali da je $f_m$ linearna rekurzija, trebamo naći $f(c + d)$ takav da
$$T(X) = T(Y)$$
za sve $X(c + d)$ i $Y(c + d)$ ako je $X - Y \in \langle f(c + d) \rangle$. To očito vrijedi ako je $f(c + d) \in \langle a(c), b(d) \rangle$, pa se problem svodi na pronalazak bilo kojeg polinoma $f(c + d)$ u idealu $\langle a(c), b(d) \rangle$. Neka je
$$a(c) = \prod_{i=1}^{n} (c - \lambda_i), \qquad b(d) = \prod_{j=1}^{n} (d - \mu_j).$$
U tom prikazu možemo definirati polinom
$$f(c + d) = \prod_{i=1}^{n} \prod_{j=1}^{n} \bigl[(c + d) - (\lambda_i + \mu_j)\bigr].$$
Alternativno,
$$f(c + d) = \prod_{i=1}^{n} \prod_{j=1}^{n} \bigl[(c - \lambda_i) + (d - \mu_j)\bigr] = \sum_{d_{ij} \in \{0, 1\}} \prod_{i=1}^{n} \prod_{j=1}^{n} (c - \lambda_i)^{d_{ij}} (d - \mu_j)^{1 - d_{ij}}.$$
Zbroj ima $2^{n^2}$ pribrojnika, svaki djeljiv s $a(c)$ ili $b(d)$, dakle $f(c + d) \in \langle a(c), b(d) \rangle$.</p>
<p><i>Napomena:</i> može se dokazati da je
$$f(c \diamond d) = \prod_{i=1}^{n} \prod_{j=1}^{n} \bigl[(c \diamond d) - (\lambda_i \diamond \mu_j)\bigr] \in \langle a(c), b(d) \rangle$$
za gotovo proizvoljnu dobro definiranu binarnu operaciju $\diamond$.</p>
<h3>4. Logaritmi</h3>
<p>Računanje $f_m$ sada se svodi na sljedeće zadatke:</p>
<ol>
    <li>izračunati $f_0, f_1, \dots, f_{n^2 - 1}$;</li>
    <li>izračunati polinom $f(x)$;</li>
    <li>izračunati $x^m \bmod f(x)$ da dobijemo koeficijente uz $f_0, f_1, \dots, f_{n^2-1}$ koji čine $f_m$.</li>
</ol>
<p>Prvi korak je binomna konvolucija nizova $c_0, c_1, \dots$ i $d_0, d_1, \dots$; treći korak izvodi se postupkom opisanim na <a href="https://cp-algorithms.com/algebra/polynomial.html">CP-Algorithms</a>. Za drugi korak promotrimo logaritam obrnutog polinoma $x^n a(x^{-1})$:
$$\log x^n a(x^{-1}) = \log \prod_{i=1}^{n} (1 - \lambda_i x) = \sum_{i=1}^{n} \log(1 - \lambda_i x) = -\sum_{i=1}^{n} \sum_{k=1}^{\infty} \frac{\lambda_i^k x^k}{k}.$$
Neka je $s_i = \lambda_1^i + \dots + \lambda_n^i$, $t_j = \mu_1^j + \dots + \mu_n^j$ i
$$r_k = \sum_{i=1}^{n} \sum_{j=1}^{n} (\lambda_i + \mu_j)^k = \sum_{i=0}^{k} \binom{k}{i} s_i t_{k-i};$$
tada je
$$\log x^n a(x^{-1}) = -\sum_{k=1}^{\infty} \frac{s_k x^k}{k}, \qquad \log x^n b(x^{-1}) = -\sum_{k=1}^{\infty} \frac{t_k x^k}{k}, \qquad \log x^{n^2} f(x^{-1}) = -\sum_{k=1}^{\infty} \frac{r_k x^k}{k}.$$
Niz $r_0, r_1, \dots$ računamo kao binomnu konvoluciju nizova $s_0, s_1, \dots$ i $t_0, t_1, \dots$, nakon čega $f(x)$ dobivamo polinomnim eksponentom.</p>
''',
},
{
    'letter': 'C',
    'title': 'Testing Subjects Usually Die',
    'title_hr': 'Ispitanici obično umiru',
    'slug': 'C_testing_subjects_usually_die',
    'tl': '1 s',
    'ml': '256 MB',
    'statement': r'''
<p>Umjetna inteligencija bira broj od $1$ do $n$ tako da broj $k$ ima vjerojatnost $\frac{p_k}{p_1 + \dots + p_n}$. Trebaš ga pogoditi. Nakon svakog pogrešnog pokušaja pamćenje ti se briše, a odabrani broj s vjerojatnošću $c$ posto ponovno se bira istim postupkom, a s vjerojatnošću $100 - c$ posto ostaje isti. Ti biraš distribuciju $q_1, \dots, q_n$ i svaki put kažeš broj $k$ s vjerojatnošću $q_k$. Koliki je najmanji očekivani broj pokušaja?</p>
<h3>Ulaz</h3>
<p>$n$ i $c$ ($2 \le n \le 10^5$, $0 \le c \le 100$), zatim $p_1, \dots, p_n$ ($1 \le p_i \le 10^3$).</p>
<h3>Izlaz</h3>
<p>Najmanji očekivani broj pokušaja; dopuštena relativna ili apsolutna greška $10^{-6}$.</p>
''',
    'hints': [
        r'''
<p>Izrazi očekivanje kao funkciju $q$: uz $c \in (0,1)$, $E(q) = \dfrac{\sum_i p_i/(c + (1-c)q_i)}{\sum_i p_i q_i/(c + (1-c)q_i)}$; posebni slučajevi $c = 1$ ($1/\sum p_i q_i$) i $c = 0$ ($\sum p_i/q_i$).</p>
''',
        r'''
<p>Lagrangeovi multiplikatori daju $c + (1-c)q_i \propto \sqrt{p_i}$; negativni $q_i$ postavi na $0$ — sortiraj $p$ silazno i probaj svaki prefiks $k$ nenul $q$-ova, $O(n \log n)$.</p>
''',
    ],
    'coach': [
        ('Opažanje 1: stanje nakon promašaja',
         r'''
<p>Pamćenje se briše, pa je strategija stacionarna distribucija $q$. Očekivanje $E$ zadovoljava sustav: iz „skriveni broj je $i$” očekivano $d_i$ pokušaja, $d_i = 1 + (1-q_i)\bigl(cE + (1-c)d_i\bigr)$; $E = \sum p_i d_i$ uz normalizaciju $p$.</p>
'''),
        ('Opažanje 2: zatvoreni oblik',
         r'''
<p>Riješi $d_i$ pa uvrsti: $E = f(q)/g(q)$ kao u naputku. Za $c = 0$ nema resetiranja i $E = \sum p_i/q_i$, minimum pri $q_i \propto \sqrt{p_i}$ (Cauchy–Schwarz). Za $c = 1$ svaki je pokušaj neovisan: $E = 1/\sum p_i q_i$, minimum je staviti sve na najveći $p_i$.</p>
'''),
        ('Opažanje 3: stacionarna točka',
         r'''
<p>$\nabla(f/g) = \lambda\vec 1$ daje $p_i/(c + (1-c)q_i)^2 = $ konst., dakle $q_i = (C\sqrt{p_i} - c)/(1-c)$ s $C$ iz $\sum q_i = 1$. Nula-ograničenja: ako neki $q_i \lt 0$, u optimumu su najmanji $p_i$ na nuli (monotonost), pa probaj sve prefikse po sortiranom $p$.</p>
'''),
        ('Algoritam',
         r'''
<p>Sortiraj $p$ silazno, prefiksni zbroj $\sqrt{p_i}$; za svaki $k$ izračunaj $C_k$, provjeri $q_k \ge 0$, izračunaj $E$ — uz $c + (1-c)q_i = C_k\sqrt{p_i}$ brojnik i nazivnik postaju zbrojevi $\sqrt{p_i}$ i $p_i$ po prefiksu (plus članovi s $q_i = 0$ preko sufiksnih zbrojeva), dakle $O(1)$ po $k$. Uzmi minimum. Radi u <code>long double</code>.</p>
'''),
    ],
    'solution': r'''
<p><b>Formalna formulacija.</b> Zadani su $p_1, \dots, p_n$ i $c$. Početno se broj $p$ bira tako da je jednak $k$ s vjerojatnošću $p_k$. Ti biraš distribuciju $q_1, \dots, q_n$; zatim se bira broj $q$ koji je jednak $k$ s vjerojatnošću $q_k$. Ako je $p = q$, igra završava. Inače se $p$ s vjerojatnošću $c$ bira iznova, a s vjerojatnošću $1 - c$ ostaje isti, pa se $q$ bira ponovno. Koliki je najmanji mogući očekivani broj pokušaja $E$ do $p = q$?</p>
<h3>Rješenje</h3>
<p>Ako je $c = 1$:
$$E = \frac{1}{p_1 q_1 + \dots + p_n q_n}.$$
Ako je $c = 0$:
$$E = \frac{p_1}{q_1} + \dots + \frac{p_n}{q_n}.$$
Inače:
$$E = \sum_{i=1}^{n} p_i \bigl[1 + (1 - q_i) d_i\bigr],$$
$$d_i = cE + (1 - c)\bigl[1 + (1 - q_i) d_i\bigr],$$
$$d_i = \frac{cE + (1 - c)}{1 - (1 - c)(1 - q_i)},$$
$$1 + (1 - q_i) d_i = \frac{1 + (1 - q_i) p E}{c + q_i - c q_i}.$$
Uvrštavanjem natrag u zbroj dobivamo eksplicitan izraz za $E$. Neka je $a_i = \frac{1}{c + q_i - c q_i}$ i $b_i = \frac{q_i}{c + q_i - c q_i}$; tada je $E = \frac{a^T p}{b^T p}$, dakle
$$E = \frac{\sum_{i=1}^{n} \frac{p_i}{c + (1 - c) q_i}}{\sum_{i=1}^{n} \frac{p_i q_i}{c + (1 - c) q_i}} = \frac{f(q)}{g(q)} \to \min, \qquad q_1 + \dots + q_n = 1.$$
Problem minimizacije s ograničenjem rješavamo Lagrangeovim multiplikatorima. Lagrangian:
$$L(q, \lambda) = \frac{f(q)}{g(q)} - \lambda(\vec{1}^T q - 1).$$
Njegov gradijent:
$$\nabla L = \frac{g(q) \nabla f(q) - f(q) \nabla g(q)}{g^2(q)} - \lambda \vec{1}.$$
Derivacije su
$$\frac{\partial f(q)}{\partial q_i} = \frac{-p_i(1 - c)}{[c + (1 - c) q_i]^2}, \qquad \frac{\partial g(q)}{\partial q_i} = \frac{p_i c}{[c + (1 - c) q_i]^2}.$$
Uvrštavanjem:
$$p_i \frac{cf + (1 - c) g}{[c + (1 - c) q_i]^2} = \lambda.$$
Dakle za proizvoljne $i$ i $j$ vrijedi
$$\frac{p_i}{[c + (1 - c) q_i]^2} = \frac{p_j}{[c + (1 - c) q_j]^2} = \frac{\lambda}{cf + (1 - c) g}.$$
Iz toga,
$$c + (1 - c) q_i \sim \sqrt{p_i},$$
pa je rješenje
$$q_i = \frac{C \sqrt{p_i} - c}{1 - c}.$$
Konstantu nalazimo iz
$$\sum_{i=1}^{n} \frac{C \sqrt{p_i} - c}{1 - c} = 1, \qquad C = \frac{1 + c(n - 1)}{\sqrt{p_1} + \dots + \sqrt{p_n}}.$$
Ovo rješenje ne uzima u obzir uvjet $q_i \ge 0$, pa vrijedi samo kada je $q_i \ge 0$ globalno optimalno uz $q_1 + \dots + q_n = 1$. S druge strane, „očito“ je da ako je $p_i$ nerastući, takav je i $q_i$; zato grubom silom probamo $k$ takav da je $q_i = 0$ za $i &gt; k$, a za $i \le k$ koristimo gornje rješenje.</p>
<p>Ukupna složenost je $O(n \log n)$ zbog sortiranja $p_1, \dots, p_n$.</p>
''',
},
{
    'letter': 'D',
    'title': 'Triterminant',
    'title_hr': 'Triterminanta',
    'slug': 'D_triterminant',
    'tl': '1 s',
    'ml': '256 MB',
    'statement': r'''
<p>Za niz cijelih brojeva $b_1, \dots, b_n$ definiran je niz polinoma $A_k(x)$ kao determinanta tridijagonalne $k \times k$ matrice s $x$ na dijagonali, $b_i$ iznad dijagonale i $1$ ispod nje. Niz je <i>dobar</i> ako za sve $k$ svi koeficijenti $A_k$ po apsolutnoj vrijednosti ne prelaze $1$. Zadan je niz $c_1, \dots, c_n$ s $c_k \in \{-1, 1\}$; možeš promijeniti $c_k$ u $-c_k$. Koliko najmanje elemenata treba promijeniti da niz postane dobar (ili $-1$ ako je nemoguće)?</p>
<h3>Ulaz</h3>
<p>$t \le 10^5$ testova; u svakom $n$ ($1 \le n \le 10^5$, zbroj $n$ ne prelazi $10^5$) i $c_1, \dots, c_n$.</p>
<h3>Izlaz</h3>
<p>Za svaki test najmanji broj promjena ili $-1$.</p>
''',
    'hints': [
        r'''
<p>Koeficijenti $a_{ij} = [x^j]A_i$ zadovoljavaju $a_{ij} = a_{i-1,j-1} + b_i a_{i-2,j}$. Kad su oba pribrojnika nenul (svaki je $\pm$ umnožak nekih $b$), zbroj smije biti samo $0$ — svaka takva ćelija daje jednadžbu oblika (umnožak) + (umnožak) $= 0$.</p>
''',
        r'''
<p>Sve se jednadžbe svode na $b_{2k+1} = -b_{2k}$ i $b_{2^t(2k-1)} = -b_{2^t(2k+1)}$ — graf „različite boje” koji je šuma. U svakoj komponenti izaberi jeftinije od dva bipartitna bojanja u odnosu na zadani $c$.</p>
''',
    ],
    'coach': [
        ('Opažanje 1: tablica koeficijenata',
         r'''
<p>Normaliziraj znak ($b \to -b$) da rekurzija bude $A_k = xA_{k-1} + b_k A_{k-2}$. U trokutastoj tablici $a_{ij}$ svaka ćelija je $0$ ili $\pm\prod$ podskupa $b$-ova; uvjet $|a_{ij}| \le 1$ znači: gdje god su oba roditelja nenul, moraju se poništiti.</p>
'''),
        ('Opažanje 2: jednadžbe ne ovise o $j$',
         r'''
<p>Ćelija s $t$ nenul roditelja sa svake strane daje $\prod(\text{lijevi put}) + \prod(\text{desni put}) = 0$ s $t$ faktora svaki; $t$ je potencija dvojke, prva pojava za $i = 2^n + 2^{n-1}$, period $2^n$. Pomoću već izvedenih jednadžbi nižeg reda faktori se krate parovima do $b_{2^{n-1}(2k-1)} + b_{2^{n-1}(2k+1)} = 0$.</p>
'''),
        ('Redukcija: graf ograničenja',
         r'''
<p>Vrhovi $1..n$, bridovi $(2k, 2k+1)$ i $(2^t(2k-1), 2^t(2k+1))$ — za svaki $t$ oko $n/2^t$ bridova, ukupno $O(n)$. Graf je šuma (svaki brid povezuje po „razinama” bez ciklusa), pa je 2-bojanje uvijek moguće.</p>
'''),
        ('Algoritam',
         r'''
<p>DFS/DSU s parnošću po komponentama; za svaku komponentu broj neslaganja s $c$ pri bojanju $\chi$ i pri $1-\chi$, dodaj manji. Odgovor nikad nije $-1$. $O(n \log n)$ ili $O(n)$.</p>
'''),
    ],
    'solution': r'''
<p><b>Formalna formulacija.</b> Neka je $A_{-1}, A_0, A_1, \dots, A_n$ niz polinoma takav da
$$A_{-1} = 1, \quad A_0 = x, \qquad A_k = x \cdot A_{k-1} - b_k \cdot A_{k-2}.$$
Niz $b_1, \dots, b_n$ zovemo dobrim ako svaki koeficijent svakog $A_k$ po apsolutnoj vrijednosti ne prelazi $1$. Zadani su $c_1, \dots, c_n$ s $c_k \in \{-1, 1\}$; u jednoj operaciji možeš pomnožiti bilo koji $c_k$ s $-1$. Koliko je najmanje operacija potrebno da $c_1, \dots, c_n$ postane dobar?</p>
<h3>Opažanja</h3>
<p>Pomnožimo sve $b_i$ s $-1$ tako da rekurzija ima znak $+$ umjesto $-$.</p>
<p>Analizirajmo kako $b_1, \dots, b_n$ utječu na koeficijente $A_1, \dots, A_n$. Neka je $a_{ij} = [x^j] A_i$; tada
$$a_{ij} = a_{(i-1)(j-1)} + b_i a_{(i-2)j}.$$
Kada su $a_{(i-1)(j-1)}$ i $a_{(i-2)j}$ oba različita od nule, $b_i$ mora biti takav da $a_{ij} = 0$. Iz toga slijedi da je, potpuno raspisan, svaki $a_{ij}$ ili $0$ ili jednak umnošku svih elemenata nekog podskupa niza $b_1, \dots, b_n$. Imajući to na umu, uz pretpostavku da je $b_1, b_2, \dots$ beskonačan, sve vrijednosti $a_{ij}$ možemo organizirati u trokutastu tablicu u kojoj su iznad ćelije $a_{ij}$ ćelije $a_{(i-1)(j-1)}$ lijevo i $a_{(i-2)j}$ desno (u službenom rješenju nalazi se slika te tablice).</p>
<p>Na slici se, radi jednostavnosti, polinomi promatraju počevši od $A_0 = 1$ i $A_1 = x$ umjesto $A_{-1} = 1$ i $A_0 = x$, kako bi vrijedilo $\deg A_k = k$. Svaka je ćelija posebno obojena. Ako odgovarajući koeficijent mora biti različit od nule, ćelija je siva.</p>
<p>Inače boja ćelije ovisi o strukturi njezinih roditelja. Općenito, svaka nul-ćelija ima $t$ ne-nul roditelja u oba smjera (lijevo i desno). Primjerice, ćelija $a_{62}$ ima ne-nul roditelje $a_{40}$ i $a_{51}$ lijevo te $a_{42}$ i $a_{22}$ desno. Na slici:</p>
<ul>
    <li>bijele ćelije imaju $0$ takvih roditelja (tj. nalaze se izravno ispod ćelija koje su također $0$),</li>
    <li>crvene ćelije imaju $1$ takvog roditelja sa svake strane,</li>
    <li>narančaste ćelije imaju $2$ takva roditelja sa svake strane,</li>
    <li>žute ćelije imaju $4$ takva roditelja sa svake strane,</li>
    <li>zelene ćelije imaju $8$ takvih roditelja sa svake strane.</li>
</ul>
<p>Kada se iz sivog čvora spustimo udesno u drugi sivi čvor, on kopira vrijednost iz tog čvora, a ako se spustimo ulijevo u čvor $a_{ij}$, vrijednost se množi s $b_i$. S druge strane, ako ne-sivi čvor ima $t$ sivih roditelja, oni će za $t$ koraka doseći zajedničkog roditelja. Drugim riječima, svaki ne-sivi čvor $a_{ij}$ s $t &gt; 0$ sivih roditelja definira jednadžbu oblika
$$b_{i-t-2(t-1)} b_{i-t-2(t-2)} b_{i-t-2(t-3)} \dots b_{i-t} + b_i b_{i-2} b_{i-4} \dots b_{i-2(t-1)} = 0.$$
Prvi pribrojnik dobiva se množenjem $t$ komada $b_k$ s lijevog puta do zajedničkog roditelja, a drugi množenjem $t$ komada $b_k$ s desnog puta. Primjerice, ćelija $a_{97}$ s $t = 1$ definira jednadžbu $b_8 + b_9 = 0$, a ćelija $a_{62}$ jednadžbu $b_2 b_4 + b_4 b_6 = 0$. Te jednadžbe još nisu u zgodnom obliku, ali njihovo je zadovoljavanje nužno i dovoljno da bi svaki $a_{ij}$ bio $-1$, $0$ ili $1$.</p>
<p>Vrlo je zgodno da jednadžbe definirane s $a_{ij}$ uopće ne ovise o $j$!</p>
<p>Jednadžbe možemo pojednostavniti indukcijom. Prvo, crvene jednadžbe pojavljuju se samo za neparne $i$, pa uz $i = 2k + 1$ glase
$$b_{2k+1} + b_{2k} = 0$$
za svaki $k \ge 1$. Narančaste jednadžbe? Prva se pojavljuje u $a_{62}$, za $i = 6$, glasi $b_2 b_4 + b_4 b_6 = 0$ i ponavlja se s korakom $4$:
$$b_{4k-2} b_{4k} + b_{4k} b_{4k+2} = 0 \iff b_{2(2k-1)} + b_{2(2k+1)} = 0.$$
Prva žuta jednadžba pojavljuje se za $i = 12$, ponavlja se s korakom $8$ i glasi
$$b_{8k-6} b_{8k-4} b_{8k-2} b_{8k} + b_{8k-2} b_{8k} b_{8k+2} b_{8k+4} = 0.$$
S druge strane znamo $b_{2(4k-3)} + b_{2(4k-1)} = 0$ i $b_{2(4k-1)} + b_{2(4k+1)} = 0$, pa se to svodi na
$$b_{8k-4} b_{8k} + b_{8k} b_{8k+4} = 0 \iff b_{4(2k-1)} + b_{4(2k+1)} = 0.$$
Općenito, jednadžba s $t = 2^{n-1}$ prvi se put pojavljuje za $i = 2^n + 2^{n-1}$ i ponavlja se svakih $2^n$ koraka, dakle
$$b_{2^n k - 2(t-1)} \dots b_{2^n k} + b_{2^n k - (t-2)} \dots b_{2^n k + (t-2)} b_{2^n k + t} = 0.$$
Indukcijom se dokazuje da se ona pojednostavljuje na
$$b_{2^{n-1}(2k-1)} + b_{2^{n-1}(2k+1)} = 0.$$
Za to primijetimo da možemo pažljivo pokratiti svaki neparni faktor dok u svakom pribrojniku ne ostanu samo dva faktora, od kojih je jedan $b_{2^n k}$. Primjerice, za $t = 8$ krećemo od
$$b_{16k-14} b_{16k-12} \dots b_{16k-2} b_{16k} + b_{16k-6} b_{16k-4} \dots b_{16k+6} b_{16k+8} = 0.$$
U prvom koraku kratimo sljedeće parove:</p>
<ol>
    <li>u prvom pribrojniku $b_{2(8k-7)}$ i $b_{2(8k-5)}$, zatim $b_{2(8k-3)}$ i $b_{2(8k-1)}$;</li>
    <li>u drugom pribrojniku $b_{2(8k-3)}$ i $b_{2(8k-1)}$, zatim $b_{2(8k+1)}$ i $b_{2(8k+3)}$;</li>
</ol>
<p>nakon čega ostaje
$$b_{16k-12} b_{16k-8} b_{16k-4} b_{16k} + b_{16k-4} b_{16k} b_{16k+4} b_{16k+8} = 0,$$
pa ponovno kratimo:</p>
<ol>
    <li>u prvom pribrojniku $b_{4(4k-3)}$ i $b_{4(4k-1)}$;</li>
    <li>u drugom pribrojniku $b_{4(4k-1)}$ i $b_{4(4k+1)}$;</li>
</ol>
<p>nakon čega ostaje
$$b_{16k-8} b_{16k} + b_{16k} b_{16k+8} = 0 \iff b_{8(2k-1)} + b_{8(2k+1)} = 0.$$
Formalni dokaz za sve $n, k \ge 1$ pomalo je zamoran, ali slijedi iz gornjeg postupka.</p>
<h3>Rješenje</h3>
<p>Sažimajući, sve smo sveli na sustav jednadžbi
$$\begin{cases} b_{2k+1} + b_{2k} = 0, &amp; \forall k \ge 1, \\ b_{2^n(2k-1)} + b_{2^n(2k+1)} = 0, &amp; \forall n, k \ge 1, \end{cases}$$
koji je nužan i dovoljan za traženi uvjet. Za zadane $c_1, \dots, c_n$ to znači da imamo najviše $O(n \log n)$ ograničenja oblika „ova dva elementa moraju imati različite boje“. Njih rješavamo tako da nađemo komponente povezanosti tako definiranog grafa te usporedimo boje vrhova u bipartitnom bojanju sa zadanim $c_1, \dots, c_n$, birajući da prebojimo manji broj vrhova potreban da bojanje postane ispravno.</p>
<p>Bojanje uvijek postoji jer gornja ograničenja definiraju šumu.</p>
''',
},
{
    'letter': 'E',
    'title': 'Garbage Disposal',
    'title_hr': 'Odlaganje otpada',
    'slug': 'E_garbage_disposal',
    'tl': '1 s',
    'ml': '256 MB',
    'statement': r'''
<p>Otpad tipa $x$ smije se odložiti u kantu tipa $y$ samo ako je $\gcd(x, y) = 1$. Postoje otpad i kante svih tipova od $L$ do $R$; svaki komad otpada treba baciti u različitu kantu. Pronađi valjanu raspodjelu ili javi da ne postoji.</p>
<h3>Ulaz</h3>
<p>$t \le 10^5$ testova; u svakom $L, R$ ($1 \le L \le R \le 10^9$), zbroj $R - L + 1$ ne prelazi $10^5$.</p>
<h3>Izlaz</h3>
<p>$-1$ ili $R - L + 1$ različitih brojeva $y_L, \dots, y_R$ ($L \le y_i \le R$) takvih da $\gcd(y_i, i) = 1$.</p>
''',
    'hints': [
        r'''
<p>$\gcd(i, i+1) = 1$: susjedne brojeve spari križno. Problem su rubovi kad je duljina neparna.</p>
''',
        r'''
<p>Nemoguće: $L = R \ne 1$, ili $L$ i $R$ oba parna (tada parnih ima više nego neparnih, a parni se smiju sparivati samo s neparnima). Inače za neparnu duljinu s neparnim $L$ koristi ciklus $L \to L+1 \to L+2 \to L$ ($\gcd(L, L+2) = 1$ jer je $L$ neparan).</p>
''',
    ],
    'coach': [
        ('Opažanje 1: parnost kao bipartitnost',
         r'''
<p>Parni tip otpada ide samo u neparnu kantu. Ako je $R - L + 1$ neparan i $L$, $R$ parni, parnih je $\frac{R-L}{2}+1 \gt$ neparnih — Hallov uvjet pada. Za $L = R$: $\gcd(L, L) = L$ pa treba $L = 1$.</p>
'''),
        ('Opažanje 2: konstrukcija',
         r'''
<p>Parna duljina: parovi $(L, L+1), (L+2, L+3), \dots$ zamijenjeni križno. Neparna duljina s neparnim $L$: trojka $L, L+1, L+2$ kao ciklički pomak ($y_L = L+1$, $y_{L+1} = L+2$, $y_{L+2} = L$; $\gcd(L+2, L) = \gcd(L, 2) = 1$), ostatak parovima. Neparna duljina znači da su $L$ i $R$ iste parnosti; slučaj oba parna već je isključen.</p>
'''),
        ('Složenost',
         r'''
<p>$O(R - L + 1)$ po testu.</p>
'''),
    ],
    'solution': r'''
<p>Komad otpada $i$ uvijek možemo spariti s kantom tipa $i + 1$ i obrnuto.</p>
<p>Ako je $R = L \ne 1$, ili ako je $L \equiv R \equiv 0 \pmod 2$, odlaganje je nemoguće.</p>
<p>Inače $i$ i $i + 1$ sparujemo „križno“ ($y_i = i + 1$, $y_{i+1} = i$), a po potrebi $L, L + 1, L + 2$ cikličkim pomakom.</p>
''',
},
{
    'letter': 'F',
    'title': 'Palindromic Polynomial',
    'title_hr': 'Palindromni polinom',
    'slug': 'F_palindromic_polynomial',
    'tl': '2 s',
    'ml': '256 MB',
    'statement': r'''
<p>Palindromni polinom je nenul-polinom čiji se koeficijenti čitaju jednako u oba smjera. Zadano je $n$ različitih točaka $(x_i, y_i)$ modulo $10^9 + 9$. Pronađi bilo koji palindromni polinom $A(x) = a_d x^d + \dots + a_0$ stupnja $0 \le d \le 10^4$ ($a_d \ne 0$, $a_i = a_{d-i}$) takav da $A(x_i) \equiv y_i \pmod{10^9 + 9}$ za sve $i$, ili ispiši $-1$ ako ne postoji.</p>
<h3>Ulaz</h3>
<p>$t \le 100$ testova; u svakom $n$ ($1 \le n \le 10^3$, zbroj $n$ ne prelazi $10^3$), različiti $x_1, \dots, x_n$ i $y_1, \dots, y_n$ ($0 \le x_i, y_i &lt; 10^9 + 9$).</p>
<h3>Izlaz</h3>
<p>Za svaki test $-1$ ili stupanj $d$ i koeficijenti $a_0, \dots, a_d$.</p>
''',
    'hints': [
        r'''
<p>Palindromnost $\iff A(x) = x^d A(1/x)$. Ako skup točaka za svaki $x$ sadrži i $(x^{-1}, x^{-d}y)$ („$d$-palindroman skup”), interpolacijski polinom stupnja $\lt |X|$ automatski je $d$-palindroman (razlika $A - x^dA(1/x)$ ima previše nultočaka).</p>
''',
        r'''
<p>Točke $x = 0, \pm 1$ i parovi $x, x^{-1}$ u ulazu daju ograničenja na $d$ oblika $x^d = r$; odredi skup dopuštenih $d \le 10^4$ u $O(n \cdot d_{max})$. Ako postoji dopušten $d \gt m = |X'|$, rješenje uvijek postoji (interpoliraj sredinu i dodaj $a_0$ na oba kraja); inače je dopušten najviše jedan $d$ i provjeri ga izravno.</p>
''',
    ],
    'coach': [
        ('Opažanje 1: simetrija kao funkcijska jednadžba',
         r'''
<p>$A$ je $k$-palindroman ($a_i = a_{k-i}$, $\deg A \le k$) $\iff A(x) = x^k A(x^{-1})$ za $x \ne 0$. Skup $k$-palindromnih polinoma je vektorski prostor — zbroj i skalar čuvaju svojstvo.</p>
'''),
        ('Opažanje 2: interpolacija čuva palindromnost',
         r'''
<p>Ako je skup $X$ veličine $m$ zatvoren na $x \mapsto x^{-1}$ s $y$ usklađenim ($y_i = x_i^{k} y_j$), i $A = \mathrm{Interpolate}(X)$ ($\deg \lt m$), onda $A' = x^k A(1/x)$ također prolazi kroz $X$; za $k = m-1$ imaju isti stupanj i podudaraju se u $m$ točaka $\Rightarrow$ jednaki. Za $k = m$ treba još jednu točku: $x = 1$ (ako nije u $X$), jer $A(1) = A'(1)$ uvijek.</p>
'''),
        ('Redukcija: priprema skupa',
         r'''
<p>Za svaku točku: $x = 0$ daje $a_0$ (mora biti $\ne 0$), $x = 1$ ništa, $x = -1$ uvjet na parnost $d$, par $(x, x^{-1})$ oba prisutna daje uvjet $y_1 = x^d y_2$, inače dodaj zrcalnu točku s vrijednošću ovisnom o $d$. Rezultat: $d$-palindroman skup $X'$ ($m \le 2n$), možda $a_0$, i uvjeti $x^d = r$.</p>
'''),
        ('Algoritam po slučajevima',
         r'''
<p>Dopušteni $d$ provjeri izravno za sve $d \le 10^4$ ($O(n\,d_{max})$). Ako ima $d \gt m$: $A = a_0 x^d + x^k R(x) + a_0$ gdje $R$ interpolira pomaknute vrijednosti (Lema 2/3; slučaj s $x = 1$ i parnim razmakom dodaje $b\cdot S(x)x^k$ za korekciju). Ako je jedini dopušten $d \le m$: interpoliraj (uz $a_0$ ili izvedi $a_0$ iz $a_0 = a_d$ preko Lagrangeove baze $L_0$) i provjeri stupanj i palindromnost. Newtonova interpolacija $O(m^2)$.</p>
'''),
        ('Složenost',
         r'''
<p>$O(n \cdot d_{max} \cdot \log \mathrm{MOD} + n^2)$ po testu; $\sum n \le 10^3$.</p>
'''),
    ],
    'solution': r'''
<h3>Natuknice</h3>
<ol>
    <li>Iskoristi svojstvo palindromnog polinoma $A(x) = x^d A(1/x)$.</li>
    <li>Pretpostavi $m = d + 1$ i da je za svaki par $(x, y)$ u ulazu zadan i $(x^{-1}, y \cdot x^{-n})$. Dokaži da interpolacijom dobivamo palindromni polinom (iako možda s vodećim nulama).</li>
    <li>Pokušaj riješiti zadatak kad je stupanj $d$ zadan.</li>
    <li>Ulaz može implicitno ograničavati $d$.</li>
</ol>
<h3>Korak 1</h3>
<p>Polinom $A(x) = \sum_{i=0}^{d} a_i x^i$ nazovimo <i>$k$-palindromnim</i> ako je $d \le k$ i za sve $i = 0, \dots, k$ vrijedi $a_i = a_{k-i}$. Primjerice, $A(x) = 2x^4 + 3x^3 + 3x^2 + 2x$ je $5$-palindroman jer je $[0, 2, 3, 3, 2, 0]$ palindrom. Palindromni polinom stupnja $k$ je $k$-palindroman. Zbroj $k$-palindromnih polinoma je $k$-palindroman, a množenje $k$-palindromnog polinoma brojem daje $k$-palindromni polinom.</p>
<p><b>Lema 1.</b> Ako je $A(x)$ $k$-palindroman i $x \ne 0$, tada je $A(x) = x^k A(x^{-1})$.</p>
<p>Dokaz:
$$A(x) = \sum_{i=0}^{d} a_i x^i = \sum_{i=0}^{d} a_{k-i} x^i = \sum_{i=0}^{d} a_i x^{k-i} = x^k \sum_{i=0}^{d} a_i x^{-i} = x^k A(x^{-1}).$$</p>
<p>Glavna je ideja rješenja iskoristiti to svojstvo: zadani skup točaka dopunimo tako da za svaki $x$ sadrži i $x^{-1}$, a zatim interpoliramo novi skup. Pod određenim uvjetima rezultat interpolacije automatski je palindroman.</p>
<h3>Korak 2. Interpolacija</h3>
<p>Popis parova $X = \{(x_i, y_i)\}_{i=1..m}$ zovemo „skup podataka“. Neka je $A = \mathrm{Interpolate}(X)$ polinom koji je rezultat interpolacije skupa $X$, tj. polinom najmanjeg stupnja koji prolazi kroz sve točke skupa. Tada je $\deg A &lt; |X|$. Štoviše, postoji točno jedan polinom stupnja manjeg od $|X|$ koji zadovoljava $X$, i to je $A$.</p>
<p>Za računanje $\mathrm{Interpolate}(X)$ predlažemo Newtonove interpolacijske polinome, složenosti $O(|X|^2)$.</p>
<h3>Korak 3</h3>
<p>Skup podataka zovemo <i>$k$-palindromnim</i> ako:</p>
<ul>
    <li>svi su $x_i$ različiti;</li>
    <li>ne sadrži točku $x = 0$;</li>
    <li>za svaki $i$ postoji $j$ takav da $x_i x_j = 1$ i $y_i = x_i^k y_j$.</li>
</ul>
<p><b>Lema 2.</b> Interpolacija $(m-1)$-palindromnog skupa podataka veličine $m$ daje $(m-1)$-palindromni polinom.</p>
<p><b>Dokaz.</b> Neka je $X = \{(x_i, y_i)\}_{i=1..m}$ $(m-1)$-palindroman skup. Neka je $A(x) = \sum_{i=0}^{m-1} a_i x^i$ rezultat interpolacije; tada je $\deg A \le m - 1$ i $A(x_i) = y_i$ za sve $(x_i, y_i) \in X$. Neka je $A'(x) = \sum_{i=0}^{m-1} a_i x^{m-1-i} = x^{m-1} A(x^{-1})$; stupanj mu je najviše $m - 1$. Za svaki $i \in 1..m$, po definiciji $k$-palindromnog skupa, $A'(x_i) = x_i^{m-1} A(x_i^{-1}) = x_i^{m-1} A(x_j) = x_i^{m-1} y_j = y_i = A(x_i)$, gdje je $x_j = x_i^{-1}$. Promotrimo polinom $f(x) = A(x) - A'(x)$ stupnja najviše $m - 1$. Za $i = 1..m$ vrijedi $f(x_i) = A(x_i) - A'(x_i) = 0$, pa $f$ ima barem $m$ nultočaka, a stupanj mu je najviše $m - 1$. Polinom stupnja $m - 1$ može imati najviše $m - 1$ nultočaka ako nije identički nula, pa je $f(x) \equiv 0$. Dakle $A(x) \equiv A'(x)$, tj. $A(x)$ je $(m-1)$-palindroman.</p>
<p><b>Lema 3.</b> Interpolacija $m$-palindromnog skupa podataka veličine $m$ <b>koji ne sadrži točku $x = 1$</b> daje $m$-palindromni polinom.</p>
<p><b>Dokaz.</b> Gotovo identičan dokazu Leme 2. Sada je stupanj $A'(x)$ i $f(x)$ najviše $m$, ali iz činjenice $A(1) = A'(1) = \sum_{i=0}^{m-1} a_i$ zaključujemo da $f(x)$ ima barem $m + 1$ nultočaka ($m$ točaka skupa plus $x = 1$). Dakle $f(x) \equiv 0$, tj. $A(x)$ je palindroman.</p>
<p><i>Napomena.</i> Polinom iz Leme 3 ima stupanj manji od $m$, pa je $a_0 = a_m = 0$.</p>
<h3>Korak 4. Priprema skupa podataka</h3>
<p>Neka je $X$ skup podataka iz ulaza. Obradimo ga ovako:</p>
<ul>
    <li>Ako sadrži $(0, 0)$ — rješenja nema (to bi značilo $a_d = a_0 = 0$).</li>
    <li>Ako sadrži $(0, y)$ — uklonimo tu točku iz skupa i stavimo je u poseban jednočlani skup $X_0 = \{(0, y)\}$.</li>
    <li>Ako sadrži $(1, x)$ — ne radimo ništa (ne dodajemo novu točku ni ograničenje na $d$).</li>
    <li>Ako sadrži $(-1, y)$ — dodamo ograničenje $[y \cdot (-1)^d = y]$.</li>
    <li>Ako sadrži $(x, y)$, $x \ne 0$, $x \ne \pm 1$, ali ne sadrži $x^{-1}$ — dodamo točku $(x^{-1}, x^{-d} y)$.</li>
    <li>Ako sadrži dvije točke $(x, y_1)$ i $(x^{-1}, y_2)$ — dodamo ograničenje $[y_1 = x^d y_2]$.</li>
</ul>
<p>Rezultat:</p>
<ul>
    <li>skup $X'$, koji je $d$-palindroman, $0 \le |X'| \le 2n$; neke su vrijednosti u njemu simbolički izrazi ovisni o $d$, koji u ovom trenutku još nije poznat;</li>
    <li>skup $X_0$, koji je prazan ili sadrži jedan par $(0, a_0)$, $a_0 \ne 0$;</li>
    <li>skup ograničenja $C$ na $d$, sva oblika $[y_1 = x^d y_2]$.</li>
</ul>
<p>Ako postoji palindromni polinom $A$ stupnja $d$ koji prolazi kroz sve točke $X$, on mora prolaziti i kroz točke $X' \cup X_0$, a $d$ mora zadovoljavati sva ograničenja iz $C$.</p>
<h3>Korak 5. Rješavanje za fiksni $d$</h3>
<p>Fiksirajmo stupanj $d \in [0, d_{max}]$ koji zadovoljava sva ograničenja iz $C$ i riješimo zadatak za taj $d$. Sada možemo izračunati sve vrijednosti u $X'$ koje su ovisile o $d$. Označimo $m = |X'|$. Postoji 6 slučajeva.</p>
<p><b>Slučaj 1.</b> $d &lt; m$ ili ($d = m$ i $|X_0| = 1$). Tada je $d &lt; |X' \cup X_0|$. Neka je $A(x) = \mathrm{Interpolate}(X' \cup X_0)$. Ako $A$ ima stupanj $d$ i palindroman je, to je odgovor; inače rješenja nema.</p>
<p><i>Dokaz.</i> Nijedan polinom stupnja $d$ osim $A(x)$ ne zadovoljava $X$, pa ako $A(x)$ ne zadovoljava sve uvjete, ne zadovoljava ih ni jedan drugi polinom stupnja $d$.</p>
<p><i>Upozorenje.</i> U ovom slučaju treba posebno provjeriti nije li interpolirani polinom identički nula (što se može dogoditi za $d = 0$); tada za zadani $d$ vraćamo „nema rješenja“.</p>
<p><b>Slučaj 2.</b> $d = m$, $X_0 = \emptyset$, $(1, y) \notin X'$. Rješenje uvijek postoji:
$$A(x) = a_0 x^d + R(x) + a_0,$$
gdje $a_0 \ne 0$ biramo proizvoljno (npr. $a_0 = 1$), a $R(x) = \mathrm{Interpolate}(X'')$, $X'' = \{(x, y - a_0(x^d + 1)) \mid (x, y) \in X'\}$.</p>
<p><i>Dokaz.</i> Po Lemi 3, $R(x) = \mathrm{Interpolate}(X'')$ je $m$-palindroman s $r_0 = r_m = 0$, pa je $A(x)$ palindroman. $A(x)$ zadovoljava $X'$ jer je $A(x_i) = a_0 x_i^d + R(x_i) + a_0 = a_0(x_i^d + 1) + y_i - a_0(x_i^d + 1) = y_i$.</p>
<p><b>Slučaj 3.</b> $d = m$, $X_0 = \emptyset$, $(x_1 = 1, y_1) \in X'$. Pretpostavimo da rješenje $A(x)$ postoji. Neka je $a_0 = A(0)$; $a_0 \ne 0$ jer je $a_0 = a_d \ne 0$. Tada je $A(x) = \mathrm{Interpolate}(X \cup \{(0, a_0)\})$ i pomoću Lagrangeovih interpolacijskih polinoma možemo pisati
$$A(x) = P(x) + a_0 L_0(x),$$
gdje je $L_0(x) = \frac{(x - x_1)\cdots(x - x_m)}{(0 - x_1)\cdots(0 - x_m)}$ bazni Lagrangeov polinom za točku $x = 0$, a $P(x) = \mathrm{Interpolate}(\{X \cup \{(0, 0)\}\})$. Izračunajmo ih eksplicitno.</p>
<p>Brojnik $L_0(x)$ ima stupanj $m$. To je umnožak polinoma oblika $(x - x_i)(x - x_i^{-1}) = x^2 - (x_i + x_i^{-1}) + 1$, možda $(x + 1)$, i nužno $(x - 1)$ (jer $X'$ sadrži $1$). Umnožak palindromnih polinoma je palindroman, pa je $L_0(x)$ umnožak palindromnog polinoma stupnja $m - 1$ i $(x - 1)$. Zato je $l_d = -l_0$ i $l_m \ne 0$; za dokaz je potrebno da $l_d \ne l_0$.</p>
<p>Pogledajmo koeficijente $A(x)$. Mora biti $a_0 = a_m$, dakle $p_0 + a_0 l_0 = p_d = a_d l_d$, pa je $a_0 = \frac{p_0 - p_d}{l_d - l_0}$.</p>
<p>Kad znamo $a_0$, izračunamo $A(x)$. Po konstrukciji zadovoljava $X'$; treba provjeriti ima li stupanj $d$ i je li palindroman. Ako da, to je odgovor; inače rješenje ne postoji.</p>
<p><b>Slučaj 4.</b> $d = m + 2k - 1$ ($k \ge 1$). Rješenje uvijek postoji:
$$A(x) = a_0 x^d + R(x) \cdot x^k + a_0,$$
gdje je $R(x) = \mathrm{Interpolate}(X'')$, $X'' = \{(x, (y - a_0(x^d + 1)) \cdot x^{-k}) \mid (x, y) \in X'\}$. Vrijednost $a_0$ uzimamo iz $X_0$ ako je $X_0 \ne \emptyset$, inače proizvoljno, npr. $a_0 = 1$.</p>
<p><i>Dokaz.</i> $X''$ je $(m-1)$-palindroman skup. Po Lemi 2, $R(x)$ je $(m-1)$-palindromni polinom stupnja najviše $m - 1$, pa je $R(x) \cdot x^k$ $(m + 2k - 1)$-palindroman. Stoga je $A(x)$ palindroman kao zbroj palindromnih polinoma $a_0 x^d + a_0$ i $R(x)$. Manje formalno: računamo $m$ koeficijenata $R$ koji tvore palindrom, dodamo $k$ nula s obje strane i na kraju $a_0$ s obje strane.</p>
<p><b>Slučaj 5.</b> $d = m + 2k$ ($k \ge 1$), $(1, y) \notin X'$. Rješenje uvijek postoji:
$$A(x) = a_0 x^d + R(x) \cdot x^k + a_0,$$
gdje je $R(x) = \mathrm{Interpolate}(X'')$, $X'' = \{(x, (y - a_0(x^d + 1)) \cdot x^{-k}) \mid (x, y) \in X'\}$. Formula je identična Slučaju 4; dokaz je gotovo isti, samo koristimo Lemu 3 (zato zahtijevamo da $1$ nije u $X'$).</p>
<p><b>Slučaj 6.</b> $d = m + 2k$ ($k \ge 1$), $(1, y_1) \in X$. Rješenje uvijek postoji:
$$A(x) = R(x) + b \cdot S(x) \cdot x^k,$$
gdje je $R(x)$ rješenje za skup s uklonjenim parom $(1, y_1)$ (vidi Slučaj 4), a $S(x)$ palindromni polinom stupnja $m$ konstruiran tako da je $S(x_i) = 0$ za sve točke skupa osim $1$, a $S(1) \ne 0$:
$$S(x) = (x - x_2)(x - x_3)\cdots(x - x_m) \cdot (x + 1).$$
Konačno, $b = \frac{y_1 - R(1)}{S(1)}$.</p>
<p>Svaki slučaj ima složenost $O(m^2 + d) = O(n^2 + d_{max})$ (podsjetimo, $m \le 2n$).</p>
<p>Ukratko: ako $d$ zadovoljava sva ograničenja iz $C$ i $d &gt; m$, rješenje uvijek postoji; ako je $d \le m$, rješenje može, ali ne mora postojati.</p>
<h3>Korak 6. Sve zajedno</h3>
<p>Mogli bismo provjeriti sve $d$ od $0$ do $d_{max}$ i za svaki provjeriti zadovoljava li ograničenja te postoji li rješenje. No to bi trajalo predugo ($O(d_{max} \cdot n^2)$).</p>
<p>Umjesto toga izračunamo skup $D$ svih $d$ koji zadovoljavaju sva ograničenja iz $C$, izravno provjeravajući sve $d$ od $0$ do $d_{max}$. To traje $O(n \cdot d_{max})$. Mogli bismo koristiti i diskretni logaritam za $O(n\sqrt{M})$, ali uz zadana ograničenja to ne bi bilo brže.</p>
<p>Ako je $D$ prazan, rješenja nema.</p>
<p>Ako postoji $d \in D$ takav da $d &gt; m$, uzmemo ga i riješimo Slučajem 4, 5 ili 6 — rješenje sigurno postoji.</p>
<p>Inače postoji točno jedan $d \le m$ koji zadovoljava sva ograničenja iz $C$ (Lema 4). Provjerimo ga Slučajevima 1, 2 ili 3; ako rješenje za taj $d$ postoji, ispišemo ga, inače rješenja nema.</p>
<p>Dobili smo rješenje s pretprocesiranjem $O(n \cdot d_{max})$ koje zatim rješava zadatak za točno jednu vrijednost $d$ u $O(n^2 + d_{max})$. Ukupna složenost je $O(n \cdot d_{max})$ uz pretpostavku da aritmetičke operacije traju $O(1)$; uzmemo li u obzir dijeljenja modulo $MOD$ u $O(\log MOD)$, složenost je $O(n \cdot d_{max} \cdot \log MOD)$.</p>
<p><b>Lema 4.</b> Ako je $D \ne \emptyset$ i $d \le m$ za sve $d \in D$, tada je $|D| = 1$.</p>
<p><b>Dokaz.</b> Dokazat ćemo: ako $D$ ima barem dva broja u $[0, m]$, mora imati još barem jedan u $[m + 1, d_{max}]$. Pretpostavimo da postoje $d_1 &lt; d_2 \le m$ u $D$. Svako ograničenje ima oblik $x_k^d = r_k$. Ako $d_1$ i $d_2$ oba zadovoljavaju ograničenje, tada $x_k^{d_1} = x_k^{d_2} \Rightarrow x_k^{d_2 - d_1} = 1$. Označimo $\Delta = d_2 - d_1 \le m$. Tada za svaki cijeli $k$ vrijedi $x^{d_1 + k\Delta} = x^{d_1} = r_k$. To vrijedi za svako ograničenje, pa je $d_1 + k \cdot \Delta \in D$. Uzmimo $k = \lceil \frac{m + 1 - d_1}{\Delta} \rceil$ i $d_3 = d_1 + \Delta k$. Tada $\frac{m + 1 - d}{\Delta} \le k &lt; \frac{m + 1 - d}{\Delta} + 1 \Rightarrow m + 1 \le d_3 &lt; m + 1 + \Delta$. Kako je $\Delta \le m$ i $m \le 2n$, vrijedi $m + 1 \le d_3 \le 2m \le 4n$. Sve dok je $d_{max} \ge 4n$, postoji $d_3 \in [m + 1, d_{max}]$ koji zadovoljava sva ograničenja. U ovom je zadatku $n \le 1000$, $d_{max} = 10000$, pa je uvjet $d_{max} \ge 4n$ ispunjen.</p>
''',
},
{
    'letter': 'G',
    'title': 'Palindromic Differences',
    'title_hr': 'Palindromne razlike',
    'slug': 'G_palindromic_differences',
    'tl': '2 s',
    'ml': '256 MB',
    'statement': r'''
<p>Niz razlika niza $a = [a_1, \dots, a_n]$ je $[a_2 - a_1, \dots, a_n - a_{n-1}]$. Zadan je niz $a$ duljine $n$; pronađi broj različitih permutacija niza $a$ čiji je niz razlika palindrom, modulo $10^9 + 9$.</p>
<h3>Ulaz</h3>
<p>$t \le 100$ testova; u svakom $n$ ($2 \le n \le 5 \cdot 10^5$, zbroj $n$ ne prelazi $5 \cdot 10^5$) i $a_1, \dots, a_n$ ($|a_i| \le 10^9$).</p>
<h3>Izlaz</h3>
<p>Za svaki test odgovor modulo $10^9 + 9$.</p>
''',
    'hints': [
        r'''
<p>Niz razlika palindrom $\iff a_i + a_{n+1-i}$ je konstanta za sve $i$ (zrcalni elementi simetrični oko istog $mid$). Sortiraj i provjeri; ako ne vrijedi, odgovor je $0$.</p>
''',
        r'''
<p>Ako vrijedi, dobre permutacije nastaju iz $k = \lfloor n/2\rfloor$ zrcalnih parova: rasporedi parove ($k!$) i zamijeni unutar para ($2^k$). Duplikati: $k!$ postaje multinomni koeficijent po frekvencijama u $a[1..k]$, a $2^k$ postaje $2^{k - l}$ gdje je $l$ broj parova s jednakim elementima.</p>
''',
    ],
    'coach': [
        ('Opažanje 1: karakterizacija',
         r'''
<p>$d_i = d_{n-i}$ za sve $i$ znači $a_{i+1} - a_i = a_{n+1-i} - a_{n-i}$; zbrajanjem $a_i + a_{n+1-i} = a_{i+1} + a_{n-i}$ — sve zrcalne sume jednake. Obrat je očit.</p>
'''),
        ('Opažanje 2: struktura dobrih permutacija',
         r'''
<p>Multiskup vrijednosti fiksira zrcalne parove: sortirani niz mora biti dobar (najmanji ide s najvećim itd.), a svaka dobra permutacija je raspored tih parova na zrcalne pozicije + orijentacija svakog para; središnji element (neparan $n$) je fiksan $= mid$.</p>
'''),
        ('Opažanje 3: duplikati',
         r'''
<p>Parovi kao objekti: par $(a_i, a_{n+1-i})$ za $i \le k$ određen je s $a_i$ (jer je $a_{n+1-i} = 2mid - a_i$). Permutacije parova koje daju isti niz: multinomni koeficijent $k!/\prod c_v!$ po frekvencijama vrijednosti $a_1..a_k$. Orijentacija para s $a_i = a_{n+1-i}$ ne mijenja ništa: faktor $2^{k-l}$.</p>
'''),
        ('Algoritam',
         r'''
<p>Sortiraj ($O(n \log n)$), provjeri zrcalne sume, izračunaj faktorijele i inverzne faktorijele do $n$, pomnoži. Modul $10^9+9$ je prost.</p>
'''),
    ],
    'solution': r'''
<h3>Natuknice</h3>
<ol>
    <li>Kako prepoznati je li odgovor $0$ ili barem $1$?</li>
    <li>Koje permutacije niza čuvaju svojstvo „niz razlika je palindrom“?</li>
    <li>Riješi zadatak za $a = [1, 2, \dots, n]$.</li>
    <li>Kad je odgovor pozitivan i svi su elementi različiti, odgovor je isti kao za $a = [1, 2, \dots, n]$. Kako obraditi duplikate?</li>
</ol>
<h3>Korak 1 — permutacije</h3>
<p>Niz čiji je niz razlika palindrom kratko zovemo <b>dobrim</b>. Promotrimo slučaj $a = [1, 2, \dots, n]$ i označimo $k = \lfloor \frac{n}{2} \rfloor$. Sam $a$ je dobar. Dvije vrste transformacija čuvaju dobrotu niza:</p>
<ol>
    <li>zamjena dvaju elemenata na zrcalnim pozicijama, tj. $a_i$ i $a_{n+1-i}$;</li>
    <li>zamjena bilo koja dva elementa $a_i, a_j$ uz istodobnu zamjenu njima zrcalnih elemenata $a_{n+1-i}, a_{n+1-j}$.</li>
</ol>
<p>Može se pokazati da su svi dobri nizovi dostižni iz $[1, 2, \dots, n]$ tim operacijama. Drugim riječima, dobar niz konstruiramo ovako: promotrimo $k$ parova $(1, n); (2, n-1); \dots; (k, n+1-k)$. Elementi svakog para moraju biti na zrcalnim pozicijama. Ako je $n$ neparan, postoji i broj $k + 1$ koji je uvijek na $(k+1)$-oj poziciji.</p>
<p>Koliko ima načina da se konstruira dobar niz? Postoji $k!$ načina da se parovi rasporede po parovima zrcalnih pozicija i još $2^k$ načina za zamjenu elemenata unutar svakog para. Odgovor je $k! \cdot 2^k$.</p>
<h3>Korak 2 — proizvoljan niz bez duplikata</h3>
<p>Neka $a$ ima proizvoljne cjelobrojne elemente, ali bez duplikata. Ako ga se može preurediti u dobar niz, istim operacijama kao u Koraku 1 dostižemo sve dobre nizove.</p>
<p>Svaki dobar niz ima svojstvo da su elementi na zrcalnim pozicijama zrcalni u odnosu na isti broj $mid$: $a_i = mid - \Delta_i$, $a_{n+1-i} = mid + \Delta_i$, $i = 1, \dots, k$. Za neparan $n$ središnji element mora biti jednak $mid$.</p>
<p>Dakle, da provjerimo može li se niz preurediti u dobar, dovoljno ga je sortirati i provjeriti je li sortirani niz dobar.</p>
<h3>Korak 3 — duplikati</h3>
<p>Neka je $a$ sortiran i dobar, ali s duplikatima. I dalje postoji $k! \cdot 2^k$ dobrih permutacija, ali neke su identične. Kako to uračunati?</p>
<p>Prvo, $k!$ zamijenimo brojem različitih permutacija prvih $k$ elemenata niza $a$, tj. multinomnim koeficijentom $\frac{k!}{c_1! c_2! \cdots c_d!}$, gdje je $d$ broj različitih vrijednosti u $a[1..k]$, a $c_1, \dots, c_d$ njihove frekvencije.</p>
<p>Drugo, neke su zamjene zamjene jednakih elemenata. Zato $2^k$ zamijenimo s $2^{k-l}$, gdje je $l$ broj indeksa $i \in [1, k]$ takvih da $a_i = a_{n+1-i}$.</p>
<h3>Korak 4 — rješenje</h3>
<p>Sortiraj niz $a$ i izračunaj njegov niz razlika. Ako nije palindrom, odgovor je $0$. Inače je odgovor
$$\frac{k!}{c_1! c_2! \cdots c_d!} \cdot 2^{k-l},$$
gdje je $k = \lfloor \frac{n}{2} \rfloor$, $d$ broj različitih elemenata u $a[1..k]$, $c_1, \dots, c_d$ frekvencije različitih elemenata u $a[1..k]$, a $l$ broj indeksa $i \in [1, k]$ takvih da $a_i = a_{n+1-i}$.</p>
''',
},
{
    'letter': 'H',
    'title': 'Graph Isomorphism',
    'title_hr': 'Izomorfizam grafova',
    'slug': 'H_graph_isomorphism',
    'tl': '1 s',
    'ml': '256 MB',
    'statement': r'''
<p>Dva neusmjerena grafa s $n$ vrhova izomorfna su ako postoji permutacija $p$ takva da je $(u, v)$ brid prvog ako i samo ako je $(p_u, p_v)$ brid drugog. Za zadani graf $G$ odredi ima li najviše $n$ različitih grafova izomorfnih s $G$ (grafovi su različiti ako su im skupovi bridova različiti).</p>
<h3>Ulaz</h3>
<p>$t \le 10^5$ testova; u svakom $n, m$ ($1 \le n, m \le 10^5$, zbrojevi $n$ i $m$ ne prelaze $10^5$) i $m$ bridova. Nema petlji ni višestrukih bridova.</p>
<h3>Izlaz</h3>
<p><code>YES</code> ili <code>NO</code> za svaki test.</p>
''',
    'hints': [
        r'''
<p>Broj grafova izomorfnih $G$ je $n!/|\mathrm{Aut}(G)|$. Uvjet $\le n$ znači $|\mathrm{Aut}(G)| \ge (n-1)!$ — grupa automorfizama je gotovo cijela $S_n$.</p>
''',
        r'''
<p>Podgrupe $S_n$ reda $\ge (n-1)!$ za $n \gt 4$ su $S_n$, $A_n$ i stabilizatori točke $S_{n-1}$; $A_n$ fiksira samo prazan i potpun graf. Grafovi: prazan, potpun, zvijezda, komplement zvijezde. Za $n \le 4$ provjeri sve grafove.</p>
''',
    ],
    'coach': [
        ('Opažanje 1: orbit–stabilizator',
         r'''
<p>$S_n$ djeluje na označenim grafovima; orbita $G$ (izomorfni grafovi) ima $n!/|\mathrm{Aut}(G)|$ elemenata. Traži se $|\mathrm{Aut}(G)| \ge (n-1)!$.</p>
'''),
        ('Opažanje 2: velike podgrupe $S_n$',
         r'''
<p>Za $n \ge 5$ podgrupa indeksa $\le n$ u $S_n$ je $S_n$, $A_n$ ili konjugat $S_{n-1}$ (klasičan rezultat). $A_n$ je 2-tranzitivna na parovima za $n \ge 5$ pa fiksira samo prazan ili potpun graf. $S_{n-1}$ koja fiksira vrh $v$: bridovi među ostalima svi ili nijedan, i bridovi iz $v$ svi ili nijedan — zvijezda, komplement zvijezde, prazan, potpun.</p>
'''),
        ('Algoritam',
         r'''
<p>$n \le 4$: brute-force automorfizmi ($4! = 24$ permutacija). $n \ge 5$: provjeri $m = 0$; $m = \binom n2$; $m = n-1$ sa svim bridovima iz jednog vrha (stupanj $n-1$, ostali $1$); $m = \binom n2 - (n-1)$ s jednim vrhom stupnja $0$ i ostalima $n-2$. Provjera po stupnjevima, $O(n + m)$.</p>
'''),
    ],
    'solution': r'''
<p>Graf ima najviše $n$ izomorfnih grafova $\iff$ ima barem $(n-1)!$ automorfizama. To je vrlo specifično ograničenje i za $n &gt; 4$ u biti znači da je ili svaka permutacija automorfizam, ili su automorfizmi sve permutacije s određenom fiksnom točkom.</p>
<p>Za $n &gt; 4$ jedini grafovi za koje to vrijedi su:</p>
<ol>
    <li>prazan graf;</li>
    <li>„zvijezda“;</li>
    <li>komplement „zvijezde“;</li>
    <li>potpun graf.</li>
</ol>
<p>Za $n \le 4$ broj automorfizama grafa treba provjeriti ručno.</p>
''',
},
{
    'letter': 'I',
    'title': 'DAG Generation',
    'title_hr': 'Generiranje DAG-a',
    'slug': 'I_dag_generation',
    'tl': '1 s',
    'ml': '256 MB',
    'statement': r'''
<p>DAG na $n$ vrhova generira se tako da se, počevši od praznog skupa $A$ i skupa kandidata $B = \{1, \dots, n\}$, u svakom koraku uniformno slučajno odaberu podskup $X \subseteq A$ i vrh $u \in B$, dodaju lukovi iz svih vrhova $X$ u $u$, a $u$ prebaci iz $B$ u $A$. Postupak je izveden dvaput; kolika je vjerojatnost da su dobivena dva DAG-a različita (kao skupovi usmjerenih bridova)? Odgovor ispiši modulo $10^9 + 9$.</p>
<h3>Ulaz</h3>
<p>$t \le 10^5$ testova, svaki jedan broj $n$ ($1 \le n \le 10^5$).</p>
<h3>Izlaz</h3>
<p>Za svaki test tražena vjerojatnost modulo $10^9 + 9$.</p>
''',
    'hints': [
        r'''
<p>Ishod generiranja = (DAG, topološki poredak), svih $2^{\binom n2} n!$ jednako vjerojatnih. Vjerojatnost da su dva DAG-a jednaka je $\sum_G \bigl(\mathrm{top}(G)\bigr)^2 / (2^{\binom n2} n!)^2$.</p>
''',
        r'''
<p>Zamijeni redoslijed zbrajanja: $\sum_G \mathrm{top}(G)^2 = \#\{(G, \pi_1, \pi_2)\}$; fiksiraj $\pi_1 = id$ (faktor $n!$), pa za permutaciju $\pi_2$ dopušteni bridovi su parovi u istom poretku u obje; zbroj po $\pi_2$ od $2^{\#\text{neinverzija}}$ je $\prod_{k=1}^n (2^k - 1)$.</p>
''',
    ],
    'coach': [
        ('Opažanje 1: jednako vjerojatni ishodi',
         r'''
<p>Svaki korak bira uniformno vrh iz $B$ i podskup $A$; niz odabranih vrhova je slučajna permutacija, a skup bridova prema svakom novom vrhu uniformni podskup prethodnika: ishod (DAG s topološkim poretkom) uniforman među $n!\,2^{\binom n2}$.</p>
'''),
        ('Opažanje 2: vjerojatnost jednakosti',
         r'''
<p>$P(G_1 = G_2) = \sum_G P(G)^2 = \sum_G \mathrm{top}(G)^2/N^2$. Brojanje topoloških poredaka pojedinog DAG-a je #P-teško, ali zbroj kvadrata po svim DAG-ovima je brojanje trojki $(G, \pi_1, \pi_2)$ — DAG-ova kompatibilnih s dvije permutacije.</p>
'''),
        ('Redukcija: zbroj po permutacijama',
         r'''
<p>Uz $\pi_1 = id$: brid $j \to i$ dopušten $\iff j \lt i$ i $\pi_2(j) \lt \pi_2(i)$; DAG-ova je $2^{\#\text{parova u istom poretku}}$. Zbroj po $\pi_2$: gradi permutaciju umetanjem $k$-te vrijednosti — doprinos $1 + 2 + \dots + 2^{k-1} = 2^k - 1$ neovisno o ostalom. Umnožak $\prod_{k=1}^n (2^k - 1)$.</p>
'''),
        ('Algoritam',
         r'''
<p>Odgovor $1 - \dfrac{n!\prod_k(2^k-1)}{(2^{\binom n2} n!)^2} = 1 - \dfrac{\prod_{k=1}^n (2^k - 1)}{2^{n(n-1)}\, n!}$. Predizračunaj prefiksne umnoške do $10^5$; $O(1)$ po upitu uz modularni inverz.</p>
'''),
    ],
    'solution': r'''
<p>Riješimo zadatak za svaki mogući DAG zasebno: kolika je vjerojatnost da baš on bude generiran? Može se zapisati kao
$$\frac{\text{broj ishoda u kojima se graf generira}}{\text{ukupan broj ishoda}}.$$
Što je točno ishod generiranja? To je DAG plus jedan od njegovih topoloških poredaka. Svi su ishodi jednako vjerojatni jer svaki nastaje na točno jedan način.</p>
<p>Broj ishoda koji daju zadani graf jednak je broju njegovih topoloških poredaka. Dakle, po svim DAG-ovima trebamo zbrojiti
$$\frac{(\text{broj topoloških poredaka DAG-a})^2}{(\text{ukupan broj ishoda})^2}.$$
Ukupan broj ishoda je $2^{\binom{n}{2}} n!$: za svaki od $n!$ mogućih topoloških poredaka postoji $2^{\binom{n}{2}}$ DAG-ova kompatibilnih s njim. Zato se usredotočimo na kvadrat broja topoloških poredaka. Prebrojati topološke poretke zadanog grafa teško je, ali prebrojati grafove za zadani poredak nije.</p>
<p>Kvadrat broja topoloških poredaka DAG-a u biti je broj parova njegovih poredaka. Zamijenimo redoslijed zbrajanja: umjesto parova poredaka za svaki DAG brojimo DAG-ove za svaki par poredaka. Nadalje, prvi poredak možemo fiksirati na $e = (1, 2, \dots, n)$ i rezultat pomnožiti s $n!$, jer se za sve vrijednosti prvog poretka zbroj po drugom ne mijenja.</p>
<p>Sada po svim poredcima $p = (p_1, \dots, p_n)$ računamo broj DAG-ova koji zadovoljavaju i $p$ i $e$. Koji vrhovi mogu biti spojeni s $p_i$? Oni koji dolaze prije $p_i$ u oba poretka, tj. vrhovi $j$ s $j &lt; i$ i $p_j &lt; p_i$ istodobno. Prebrojavanje kompatibilnih DAG-ova po svim permutacijama $p$ daje umnožak
$$(1)(1 + 2)(1 + 2 + 4) \cdots (1 + 2 + \dots + 2^{n-1}) = (2^1 - 1)(2^2 - 1)(2^3 - 1) \cdots (2^n - 1).$$
Ovdje $1 + 2 + \dots + 2^{k-1}$ obuhvaća sve mogućnosti za broj parova $\{p_j &lt; p_i, j &lt; i\}$ uz $p_i = k$.</p>
<p>Konačan odgovor je
$$1 - \frac{(2^1 - 1)(2^2 - 1) \cdots (2^n - 1)}{2^{n(n-1)} n!}.$$</p>
''',
},
{
    'letter': 'J',
    'title': 'Persian Casino',
    'title_hr': 'Perzijski kasino',
    'slug': 'J_persian_casino',
    'tl': '1 s',
    'ml': '256 MB',
    'statement': r'''
<p>Princ počinje s jednim zlatnikom i igra rulet: u svakoj oklade bira crveno ili crno i ulaže pozitivan cijeli broj zlatnika; dobitak vraća dvostruki ulog, a gubitak odnosi ulog. Ishodi su uniformni i neovisni. Nakon što se ishod sazna, princ se može vratiti u vrijeme prije oklade i ponoviti je drukčije (ishod ruleta se ne mijenja). Želi napraviti točno $n$ oklada uz najviše $m$ vraćanja, tako da prije svake oklade ima barem $1$ zlatnik, i pritom maksimizirati očekivani broj zlatnika na kraju. Ispiši očekivani iznos modulo $10^9 + 9$ ili <code>bankrupt</code> ako se $n$ valjanih oklada ne može jamčiti.</p>
<h3>Ulaz</h3>
<p>$t \le 10^5$ testova; u svakom $n, m$ ($1 \le n, m \le 10^5$, zbroj $m$ ne prelazi $10^6$).</p>
<h3>Izlaz</h3>
<p>Za svaki test očekivani iznos modulo $10^9 + 9$ ili <code>bankrupt</code>.</p>
''',
    'hints': [
        r'''
<p>Dok ima vraćanja: uloži sve i vrati se ako izgubiš — siguran dvostruki dobitak. Nakon što ih potrošiš, očekivanje svake oklade je $0$; ulaži $1$ da nikad ne bankrotiraš.</p>
''',
        r'''
<p>Bankrot je moguć ako $2^M \lt N - M$ (najgori slučaj: svih $M$ vraćanja potrošeno odmah, pa $N - M$ gubitaka po $1$). Inače je odgovor $\sum_{i=0}^{M}\binom{N}{i}$ (hockey-stick identitet za $\sum_k 2^k p_k$).</p>
''',
    ],
    'coach': [
        ('Opažanje 1: dvije faze',
         r'''
<p>Vraćanje pretvara okladu u sigurnu — tada je optimalno all-in (udvostruči). Bez vraćanja svaka oklada ima očekivanje $0$ neovisno o ulogu, ali ulog $\gt 1$ povećava rizik bankrota; ulog $1$ uz dovoljno zlatnika jamči $N$ oklada.</p>
'''),
        ('Opažanje 2: kada je bankrot moguć',
         r'''
<p>Vraćanje trošimo samo na gubitak; nakon $M$ vraćanja imamo $2^{k}$ zlatnika gdje je $k$ broj dosad odigranih oklada ($\ge M$). Najgori slučaj: gubici na prvih $M$ oklada (sve ispravljene $\Rightarrow$ $2^M$ zlatnika), pa preostalih $N - M$ oklada svi gubici po $1$: treba $2^M \ge N - M$. Ako ne, <code>bankrupt</code>.</p>
'''),
        ('Opažanje 3: očekivanje',
         r'''
<p>Ako je $M$-ti gubitak na okladi $k$ (vjerojatnost $\binom{k-1}{M-1}/2^k$), završni iznos je u očekivanju $2^k$ (nakon toga fer oklade). Ako je gubitaka manje od $M$, iznos je $2^N$. Zbroj: $\sum_{k=M}^{N}\binom{k-1}{M-1} + \sum_{i \lt M}\binom{N}{i} = \binom{N}{M} + \sum_{i \lt M}\binom{N}{i}$.</p>
'''),
        ('Algoritam',
         r'''
<p>Faktorijeli do $10^5$; $\sum_{i=0}^{\min(M,N)} \binom N i$ u $O(M)$ po testu, $\sum M \le 10^6$. Provjera $2^M \lt N - M$ samo za $M \le 17$.</p>
'''),
    ],
    'solution': r'''
<p>Dok se ne potroše sva vraćanja, optimalno je uložiti sve što imamo i vratiti se ako oklada nije uspjela. Nakon toga do kraja igre ulažemo $1$ zlatnik. Naime, prije svakog okretanja možemo odlučiti hoćemo li ga ispraviti ako ne uspije. Ako ćemo ga ispraviti, optimalno je uložiti sve jer smo sigurni u dobitak. Inače je očekivana vrijednost dobitka $0$ bez obzira na ulog, pa je optimalno uložiti $1$ da ne ostanemo bez novca.</p>
<p>Nakon toga je očekivana vrijednost svake oklade $0$, pa zapravo nije važno koliko ulažemo, dok god princ može jamčiti da neće bankrotirati.</p>
<p>Ako je $2^M &lt; N - M$, princ bi u vrlo malo vjerojatnom scenariju mogao bankrotirati, što treba ispisati.</p>
<p>Inače je odgovor zbroj $2^k p_k$ za $M \le k \le N$, gdje je $p_k$ vjerojatnost da princ iskoristi $M$-to vraćanje na $k$-toj okladi, plus $2^N$ puta vjerojatnost da tijekom igre izgubi manje od $M$ oklada. Potonje je
$$\frac{\binom{N}{0} + \binom{N}{1} + \dots + \binom{N}{M-1}}{2^N}.$$
A za $p_k$ formula je $\frac{\binom{k-1}{M-1}}{2^k}$.</p>
<p>Stoga bi odgovor na cijeli zadatak trebao biti
$$\binom{N}{0} + \binom{N}{1} + \dots + \binom{N}{M-1} + \binom{N}{M},$$
jer zbrajanjem $2^k p_k$ dobivamo
$$\binom{M-1}{M-1} + \binom{M}{M-1} + \dots + \binom{N-1}{M-1} = \binom{N}{M}.$$
Isto se može objasniti i dinamičkim programiranjem.</p>
''',
},
{
    'letter': 'K',
    'title': 'Determinant, or...?',
    'title_hr': 'Determinanta, ili...?',
    'slug': 'K_determinant_or',
    'tl': '1 s',
    'ml': '256 MB',
    'statement': r'''
<p>Zadan je niz $a_0, \dots, a_{2^n - 1}$. Promotri matricu $A$ dimenzija $2^n \times 2^n$ s $A_{ij} = a_{i | j}$, gdje je $i | j$ bitovni ILI. Izračunaj $\det A$ modulo $10^9 + 9$.</p>
<h3>Ulaz</h3>
<p>$n$ ($1 \le n \le 20$) i $2^n$ brojeva $a_i$ ($0 \le a_i &lt; 10^9 + 9$).</p>
<h3>Izlaz</h3>
<p>Determinanta modulo $10^9 + 9$.</p>
''',
    'hints': [
        r'''
<p>Po najvišem bitu indeksa matrica je blok $\begin{bmatrix} A &amp; B \\ B &amp; B\end{bmatrix}$ ($A$: oba bita $0$; $B$: barem jedan $1$ — tada je $i|j$ isti u sva tri bloka).</p>
''',
        r'''
<p>Oduzmi donji blok redaka od gornjeg: $\det = \det(A - B)\det(B)$. Rekurzivno po bitovima — to je „OR-transformacija” niza (subset-sum inverz): $\det = \prod_{S} \hat a_S$ gdje je $\hat a$ Möbiusova transformacija $a$ po podskupovima.</p>
''',
    ],
    'coach': [
        ('Opažanje 1: rekurzivna blok-struktura',
         r'''
<p>Indeksi s najvišim bitom: $i|j$ ima taj bit ako ga ima $i$ ili $j$. Blok $(1,1)$: $a_{i|j}$ za $i, j \lt 2^{n-1}$ — matrica istog tipa za niz $a_0..a_{2^{n-1}-1}$. Ostala tri bloka: $a_{(i|j) + 2^{n-1}}$ — matrica istog tipa za gornju polovicu niza.</p>
'''),
        ('Opažanje 2: eliminacija blokova',
         r'''
<p>Redak-operacije: gornji blok redaka minus donji daje $\begin{bmatrix} A - B &amp; 0 \\ B &amp; B \end{bmatrix}$, blok-donjetrokutasta $\Rightarrow \det = \det(A-B)\cdot\det B$. $A - B$ je matrica istog tipa za niz $a_S - a_{S \cup \{bit\}}$.</p>
'''),
        ('Redukcija: transformacija niza',
         r'''
<p>Rekurzija po bitovima primjenjuje na niz operaciju „za svaki $S$ bez bita: $a_S \leftarrow a_S - a_{S\cup bit}$” po svim bitovima — superset-Möbiusova transformacija. Na kraju $1 \times 1$ matrice: $\det = \prod_S \hat a_S$ gdje je $\hat a_S = \sum_{T \supseteq S} (-1)^{|T|-|S|} a_T$.</p>
'''),
        ('Algoritam i složenost',
         r'''
<p>In-place transformacija $O(n 2^n)$ ($20 \cdot 10^6$), umnožak modulo $10^9+9$.</p>
'''),
    ],
    'solution': r'''
<p>Tako opisana matrica općenito je blok-matrica
$$\begin{bmatrix} A &amp; B \\ B &amp; B \end{bmatrix},$$
gdje su $A$ i $B$ matrice istog oblika manje dimenzije. Iz Gaussove eliminacije znamo da oduzimanje jednog retka matrice od drugog ne mijenja determinantu, pa možemo početi oduzimanjem donje polovice redaka od gornje:
$$\begin{bmatrix} A - B &amp; 0 \\ B &amp; B \end{bmatrix}.$$
Postupak zatim ponavljamo za $A - B$ i $B$ dok ne postanu donjetrokutaste, nakon čega determinantu računamo rekurzivno kao $\det(A - B) \det B$.</p>
''',
},
{
    'letter': 'L',
    'title': 'Directed Vertex Cacti',
    'title_hr': 'Usmjereni vršni kaktusi',
    'slug': 'L_directed_vertex_cacti',
    'tl': '1 s',
    'ml': '256 MB',
    'statement': r'''
<p>Zadani su $n$ i $m$. Prebroji usmjerene grafove bez petlji i višestrukih bridova s točno $n$ označenih vrhova u kojima svaki vrh leži na najviše jednom jednostavnom ciklusu i točno $m$ bridova ne pripada nijednom ciklusu. Odgovor ispiši modulo $10^9 + 9$.</p>
<h3>Ulaz</h3>
<p>$n, m$ ($1 \le n, m \le 10^6$).</p>
<h3>Izlaz</h3>
<p>Odgovor modulo $10^9 + 9$.</p>
''',
    'hints': [
        r'''
<p>Odgovor je $\binom{\binom n2}{m}\cdot n!$ — za svaki skup od $m$ ne-cikličkih bridova postoji točno $n!$ dovršenja (orijentacija + ciklusi).</p>
''',
        r'''
<p>Dokaz bijekcijom s permutacijama: krenuvši od praznog skupa bridova (ciklusi = zapis permutacije) dodavanje brida $(u,v)$ mijenja strukturu na točno jedan način (orijentacija po usporedivosti ciklusa ili transpozicija $(u\,v)$), i to reverzibilno.</p>
''',
    ],
    'coach': [
        ('Opažanje 1: eksperimentiraj s malim $n$',
         r'''
<p>$m = 0$: usmjereni vršni kaktus bez ne-cikličkih bridova je disjunktna unija usmjerenih ciklusa (duljine $\ge 2$; petlje nisu dopuštene, fiksne točke = izolirani vrhovi) — točno $n!$ (permutacije u cikličkom zapisu). Sumnja: broj ne ovisi o skupu ne-cikličkih bridova.</p>
'''),
        ('Opažanje 2: invarijantnost',
         r'''
<p>Dodavanje ne-cikličkog brida $(u,v)$ u skup: konstruiraj bijekciju između kaktusa na starom skupu i na novom. Ako $u$, $v$ u različitim ciklusima koji su već povezani (usporedivi), orijentacija je prisiljena da ne nastane novi ciklus; ako nepovezani, izaberi kanonsku orijentaciju; ako u istom ciklusu, rascijepi ciklus transpozicijom i orijentiraj kanonski. Svaki slučaj je reverzibilan pa je broj dovršenja konstantan $= n!$.</p>
'''),
        ('Algoritam',
         r'''
<p>$\binom{N}{m}$ s $N = \binom n2 \le 5\cdot10^{11}$ i $m \le 10^6$: računaj $\prod_{i=0}^{m-1}(N - i)/m!$ modulo prostog $10^9+9$ (pazi: $N$ može biti $\ge$ modula — reduciraj $N - i$; ako je neki faktor $\equiv 0$, odgovor je $0$, što je ispravno po Lucasu jer $m \lt p$). $O(m)$.</p>
'''),
    ],
    'solution': r'''
<p>Odgovor je točno $\binom{\binom{n}{2}}{m} n!$.</p>
<p>Vjerojatno najljepši način da se to dobije: za svaki od $\binom{\binom{n}{2}}{m}$ skupova ne-cikličkih bridova postoji točno $n!$ načina da im se odabere orijentacija i dodaju ciklusi tako da nastane usmjereni kaktus.</p>
<p>To vrijedi za $m = 0$, jer tada nema ne-cikličkih bridova, a postoji $n!$ načina da se neki vrhovi spoje u cikluse (što odgovara zapisu permutacije pomoću ciklusa). Pretpostavimo da smo pokazali da postoji $n!$ načina za neki graf $G$ i dodajmo brid $(u, v)$:</p>
<ul>
    <li>ako $u$ i $v$ pripadaju različitim usporedivim ciklusima, brid $(u, v)$ orijentiramo na jedini mogući način;</li>
    <li>ako $u$ i $v$ pripadaju različitim neusporedivim ciklusima, brid $(u, v)$ orijentiramo od manjeg vrha prema većem;</li>
    <li>ako $u$ i $v$ pripadaju istom ciklusu, na permutaciju predstavljenu jako povezanim komponentama kao ciklusima primijenimo transpoziciju $(u\,v)$, a brid $(u, v)$ orijentiramo od većeg vrha prema manjem.</li>
</ul>
<p>Postupak je reverzibilan, pa je broj načina za odabir orijentacija i ciklusa jednak za sve moguće neusmjerene grafove ne-cikličkih bridova.</p>
''',
},
{
    'letter': 'M',
    'title': 'Siteswap',
    'title_hr': 'Siteswap',
    'slug': 'M_siteswap',
    'tl': '1 s',
    'ml': '256 MB',
    'statement': r'''
<p>Siteswap je žonglerska notacija: niz $a_1, \dots, a_n$ u kojem $a_k$ znači da se predmet bačen na $k$-tom otkucaju hvata i ponovno baca na $(k + a_k)$-om otkucaju; ruke se izmjenjuju po otkucajima, a $0$ znači praznu ruku. Za zadani valjani uzorak odredi broj predmeta koje baca samo prva ruka (neparni otkucaji), samo druga ruka (parni otkucaji) i broj predmeta koje bacaju obje ruke.</p>
<h3>Ulaz</h3>
<p>$t \le 100$ testova; u svakom $n$ ($1 \le n \le 10^5$, zbroj $n$ ne prelazi $10^5$) i valjani uzorak $a_1, \dots, a_n$ ($0 \le a_i \le 10^9$).</p>
<h3>Izlaz</h3>
<p>Tri tražena broja za svaki test.</p>
''',
    'hints': [
        r'''
<p>Valjani siteswap: $i \mapsto (i + a_i) \bmod n$ je permutacija. Svaki ciklus permutacije je putanja jedne lopte (u jednom periodu), a $0$ znači bez lopte.</p>
''',
        r'''
<p>Lopta ostaje u istoj ruci $\iff$ svi otkucaji njezinog ciklusa iste parnosti (uz paran $n$). Za neparan $n$ ruke se u sljedećem periodu zamjenjuju, pa lopte koje „ne mijenjaju” ruku unutar perioda ipak mijenjaju — pravi period je $2n$.</p>
''',
    ],
    'coach': [
        ('Opažanje 1: putanje lopti = ciklusi',
         r'''
<p>Uzorak je periodičan, pa bacanje s otkucaja $i$ pada na otkucaj klase $(i + a_i) \bmod n$; valjanost znači da je to permutacija $p$ na $\{1..n\}$. Lopta koja slijedi ciklus $C$ permutacije uvijek se baca s otkucaja iz $C$; broj lopti na ciklusu $C$ je $\sum_{i\in C} a_i / n$ (ukupno $\frac1n\sum a_i$).</p>
'''),
        ('Opažanje 2: ruke i parnost',
         r'''
<p>Ruka ovisi o parnosti otkucaja. Lopta bačena s otkucaja $i$ mijenja ruku $\iff a_i$ neparan. Ciklus s otkucajima obje parnosti $\Rightarrow$ njegove lopte koriste obje ruke; ciklus s otkucajima iste parnosti $\Rightarrow$ ista ruka unutar perioda.</p>
'''),
        ('Opažanje 3: neparan $n$',
         r'''
<p>Ako je $n$ neparan, u sljedećem ponavljanju uzorka otkucaj $i$ ima suprotnu parnost (otkucaj $i+n$), pa lopte na „isto-parnim” ciklusima zapravo alterniraju ruke između perioda — pola tih lopti u svakom trenutku je u lijevoj, pola u desnoj (ekvivalentno: promatraj udvostručeni uzorak duljine $2n$).</p>
'''),
        ('Algoritam',
         r'''
<p>Nađi cikluse permutacije $p$, zbroji $a_i$ po ciklusu, podijeli s $n$, klasificiraj po parnosti otkucaja. $O(n)$.</p>
'''),
    ],
    'solution': r'''
<p>Siteswap niz $a_1, \dots, a_n$ definira permutaciju $p_i \equiv i + a_i \pmod n$. Treba naći cikluse te permutacije i za svaki provjeriti sadrži li dva elementa različite parnosti. Ako sadrži, lopta na tom ciklusu mijenja ruke; inače je baca uvijek ista ruka. Ako lopte ne mijenjaju ruku, a $n$ je neparan, to znači da polovica lopti ide u lijevu, a polovica u desnu ruku, jer se pri ponavljanju uzorka ruke izmjenjuju.</p>
''',
},
]
