---
title: Uvod u polinome i funkcije izvodnice
---

## Polinomi i funkcije izvodnice

Rad s polinomima s konačno odnosno beskonačno mnogo članova važan je dio matematike u OI-ju, osobito kod funkcija izvodnica.

Polinomni algoritmi, kojima je temelj [brza Fourierova transformacija](./fft.md), daju natjecateljima mogućnost izravnog rada s funkcijama izvodnicama.

## Osnovni pojmovi

Za sumu $\sum a_nx^n$: ako se zbraja konačno mnogo članova, zove se polinom i zapisuje se $f(x)=\sum_{n=0}^m a_nx^n$.

Suma s prebrojivo mnogo članova zove se red. U sumi $\sum_{n=0}^\infty a_nx^n$ svaki je član potencija s nenegativnim cjelobrojnim eksponentom pomnožena konstantnim koeficijentom; red takvog oblika zove se red potencija.

Pri proučavanju aritmetike polinoma najprije razmatramo jednostavnije polinome, a pojam reda potencija služi samo lakšem razumijevanju. U matematičkoj analizi dalje se proučava konvergencija redova potencija.

Opće definicije prstena, polja i iz njih izvedenih struktura vidi u članku [Osnovni pojmovi apstraktne algebre](../algebra/basic.md).

Za opći prsten $R$ definira se **prsten polinoma** (polynomial ring) $R[x]$ nad $R$.

Svaki element $f$ zove se **polinom** (polynomial) nad $R$ i može se prikazati kao

$$
f=\left<f_0,f_1,f_2,\cdots,f_n\right>\quad(f_0,f_1,f_2,\cdots,f_n\in R)
$$

Drugim riječima, polinom izravno definiramo kao niz koeficijenata. Može se zapisati i kao

$$
f(x)=f_0+f_1x+f_2x^2+\cdots+f_nx^n
$$

Ovdje $x$ smatramo samo **formalnim simbolom**, oznakom za položaj koeficijenta.

Dopustimo li i beskonačno mnogo članova, tj.

$$
f(x)=f_0+f_1x+f_2x^2+\cdots
$$

dobivamo **prsten formalnih redova potencija** (formal power series ring) $R[[x]]$, čiji se svaki element $f$ zove **formalni red potencija** (formal power series), u nastavku skraćeno red potencija.

### Stupanj polinoma

Za polinom $f(x)$ stupanj njegova člana najvišeg stupnja zove se **stupanj (degree)** tog polinoma i označava se $\operatorname{deg}{f}$.

### Množenje polinoma

Najvažnija je operacija množenje dvaju polinoma, tj. za zadane polinome $f(x)$ i $g(x)$:

$$
\begin{alignedat}{3}
f(x)&=a_0+a_1x+\dots+a_nx^n\quad \quad &(1)\\
g(x)&=b_0+b_1x+\dots+b_mx^m\quad \quad &(2)
\end{alignedat}
$$

treba izračunati polinom $Q(x)=f(x)\cdot g(x)$:

$$
\boxed {Q(x) = \sum \limits_ {i = 0} ^ n \sum \limits_ {j = 0 } ^ m a_i b_j x ^ {i + j}} = c_0 + c_1 x + \dots + c_ {n + m} x ^ {n + m}
$$

Množenje polinoma ili redova potencija asocijativno je i distributivno prema zbrajanju. Ako je $R$ komutativan prsten ili prsten s jedinicom, množenje je u skladu s tim komutativno, odnosno ima jedinični element.

Ako nad $R$ postoji korijen jedinice reda $2^n$, [brza Fourierova transformacija](./fft.md) omogućuje nam da produkt dvaju polinoma stupnja $2^n$ izračunamo u vremenu $O(n2^n)$ umjesto $O(2^{2n})$.

### Kompozicija

Potenciju elementa $f$ iz $R[[x]]$ definiramo kao

$$
f^1=f,f^k=f^{k-1}\times f
$$

Na temelju toga kompoziciju elemenata $f,g$ iz $R[[x]]$ definiramo kao

$$
(f\circ g)(x)=f(g(x))=f_0+\sum_{k=1}^{+\infty}f_kg^k(x)
$$

Dogovaramo se da $f\circ g$ postoji ako i samo ako $f$ ima konačno mnogo članova ili je $g_0=0$; tako ne ulazimo u limese nad $R$.

$\circ$ je asocijativna (kad $(f\circ g)\circ h$ i $f\circ (g\circ h)$ oba postoje), a nije komutativna. Kad je $R$ prsten s jedinicom, $\circ$ ima jedinični element $1\times x$.

Za kompoziciju polinoma (i kompozicijski inverz) postoji postupak složenosti $\Theta(n\log^2 n)$, koji su 2024. predložili Yasunori Kinoshita i Li Baitian (李白天); vidi [Kompozicija formalnih redova potencija | kompozicijski inverz](./comp-rev.md).

### Derivacija

Iako u općem prstenu limesi ne moraju ni postojati,  
ipak možemo definirati **formalnu derivaciju** (formal derivative) formalnog reda potencija kao

$$
\left(\sum_{k=0}^{+\infty}f_kx^k\right)'=\sum_{k=1}^{+\infty}kf_kx^{k-1}
$$

gdje je

$$
kf_k=\underbrace{f_k+f_k+\cdots+f_k}_{k \text{ puta } f_k}
$$

Osnovna pravila deriviranja — pravilo zbroja, pravilo produkta, lančano pravilo (kad je kompozicija dopuštena) — i dalje vrijede.

Ako je nad $R$ dopušteno dijeljenje, analogno se može definirati i **formalni neodređeni integral** (formal indefinite integral) formalnog reda potencija.

### Multiplikativni inverz

Iz primjera

$$
\dfrac{1}{1-x}=1+x+x^2+\cdots
$$

vidimo da se recipročna vrijednost polinoma može razviti u beskonačan red. Recipročna vrijednost postoji ako i samo ako slobodni član nije $0$, a i slobodni član recipročne vrijednosti nije $0$.

Stoga definiramo: za formalni red potencija $f$ s $f_0\not=0$ njegov **multiplikativni inverz** (multiplicative inversion) $f^{-1}$ drugi je formalni red potencija koji zadovoljava

$$
f\times f^{-1}=f^{-1}\times f=1
$$

Raspišemo li taj izraz prema definiciji množenja formalnih redova potencija, dobivamo rekurziju za koeficijente od $f^{-1}$

$$
f^{-1}_0=\dfrac{1}{f_0},f^{-1}_n=\dfrac{-1}{f_0}\sum_{k=0}^{n-1}f^{-1}_kf_{n-k}
$$

Izravno računanje prvih $n$ članova rekurzijom ima složenost $O(n^2)$; [primjenom FFT-a](./elementary-func.md#多项式求逆) dobiva se algoritam složenosti $O(n\log n)$.

???+ note "Napomena"
    Lako se vidi da je recipročna vrijednost od $f(x)$ upravo beskonačni Maclaurinov razvoj od $\frac{1}{f(x)}$ (beskonačni Taylorov razvoj u točki $x=0$).

### Uobičajeni razvoji u red potencija

U matematičkoj analizi funkcija jedne varijable koja je u nekoj točki ili na nekom intervalu određeni broj puta derivabilna može se na odgovarajućem području razviti u polinom; to se općenito naziva Taylorovim razvojem, a ako se razvija u točki $0$, naziva se i Maclaurinovim razvojem.

Ako je beskonačno puta derivabilna, može se razviti u red potencija. Najčešći je i dalje razvoj u točki $0$.

U kompleksnoj analizi neke se funkcije u singularitetima ne mogu razviti u Taylorov red, ali se mogu razviti u Laurentov red.

Sljedeće jednakosti vrijede samo kad red potencija konvergira, a ne vrijede kad ne konvergira. Ovdje navodimo samo razvoje, bez rasprave o području konvergencije.

Osnovna su dva razvoja, eksponencijalne funkcije i potencije:

$$
\mathrm{e}^x=1+x+\frac{1}{2!}x^2+\ldots+\frac{1}{n!}x^n+\ldots
$$

$$
(1+x)^a=1+ax+\frac{a(a-1)}{2!}x^2+\ldots+\frac{a(a-1)\ldots(a-n+1)}{n!}x^n+\ldots
$$

Daljnji razvoji često se dobivaju preoblikovanjem gornjih dvaju. Primjerice, kosinus i sinus dobivaju se uvrštavanjem kompleksnih brojeva u eksponencijalnu funkciju:

$$
\cos x=1-\frac{1}{2!}x^2+\frac{1}{4!}x^4+\ldots+\frac{(-1)^n}{(2n)!}x^{2n}+\ldots
$$

$$
\sin x=x-\frac{1}{3!}x^3+\frac{1}{5!}x^5+\ldots+\frac{(-1)^n}{(2n+1)!}x^{2n+1}+\ldots
$$

Logaritam te arkus tangens i arkus sinus dobivaju se integriranjem:

$$
\frac{1}{1+x}=1-x+x^2+\ldots+{(-1)}^n x^n+\ldots
$$

$$
\ln(1+x)=x-\frac{1}{2}x^2+\frac{1}{3}x^3+\ldots+\frac{{(-1)}^{n-1}}{n}x^n+\ldots
$$

$$
\frac{1}{1+x^2}=1-x^2+x^4+\ldots+{(-1)}^n x^{2n}+\ldots
$$

$$
\arctan x=x-\frac{1}{3}x^3+\frac{1}{5}x^5+\ldots+\frac{{(-1)}^{n}}{2n+1}x^{2n+1}+\ldots
$$

$$
\frac{1}{\sqrt{1+x}}=1-\frac{1}{2}x+\frac{3}{8}x^2+\ldots+{(-1)}^n\frac{(2n)!}{{(n!)}^2 4^n} x^{n}+\ldots
$$

$$
\frac{1}{\sqrt{1-x^2}}=1+\frac{1}{2}x^2+\frac{3}{8}x^4+\ldots+\frac{(2n)!}{{(n!)}^2 4^n} x^{2n}+\ldots
$$

$$
\arcsin x=x+\frac{1}{6}x^3+\frac{3}{40}x^5+\ldots+\frac{(2n)!}{{(n!)}^2(2n+1)4^n} x^{2n+1}+\ldots
$$

### Kompozicijski inverz

**Kompozicijski inverz** (compound inversion) poopćenje je pojma inverzne funkcije na prsten formalnih redova potencija.

Za formalni red potencija $f$ koji zadovoljava $f_0=0$ i $f_1\not=0$ njegov je kompozicijski inverz formalni red potencija $g$ koji zadovoljava $g(f(x))=f(g(x))=x$. Iz Lagrangeove inverzije slijedi da za sve cijele brojeve $n,k$ vrijedi

$$
n[x^n]f^k=k[x^{n-k}]\left(\dfrac{x}{g}\right)^n
$$

gdje $[x^k]f(x)$ označava koeficijent od $f(x)$ uz $x^k$.

### Djeljivost polinoma

Za polinome $f(x)$ i $g(x)$, ako postoji polinom $h(x)$ takav da:

$$
f(x)=g(x)h(x)
$$

onda polinom $g(x)$ dijeli polinom $f(x)$.

Očito polinom $g(x)$ dijeli polinom $f(x)$ ako i samo ako su svi korijeni od $g(x)$ ujedno korijeni od $f(x)$ i njihova kratnost u $g(x)$ ne premašuje odgovarajuću kratnost u $f(x)$.

### Ostatak i kvocijent polinoma

Za polinome $f(x), g(x)$ postoje **jedinstveni** $Q(x), R(x)$ takvi da:

$$
\begin{aligned}
    f(x) &= Q(x) g(x) + R(x) \\
    \operatorname{deg}{R} &< \operatorname{deg}{g}
\end{aligned}
$$

Kad je $\operatorname{deg}{f} \ge \operatorname{deg}{g}$, vrijedi $\operatorname{deg}{Q} = \operatorname{deg}{f} - \operatorname{deg}{g}$, a inače je $Q(x) = 0$. $Q(x)$ zovemo **kvocijentom (quotient)** pri dijeljenju $f(x)$ s $g(x)$, a $R(x)$ **ostatkom (remainder)** pri dijeljenju $f(x)$ s $g(x)$.

## Polinomi modulo polinom

Polinomi modulo polinom čine potprsten prstena polinoma, dobiven dijeljenjem prstena polinoma relacijom ekvivalencije kongruencije.

U gore spomenutom dijeljenju s ostatkom polinom $f(x)$ i njegov ostatak $R(x)$ kongruentni su modulo polinom $g(x)$.

$$
f(x) \equiv R(x) \pmod{g(x)}
$$

Ta kongruencija također znači da za svaki korijen $x_0$ polinoma $g(x)$ uvrštavanje u $f(x)$ i u $R(x)$ daje jednaku vrijednost. Tj.:

$$
f(x_0)=R(x_0)
$$

Štoviše, ako je kratnost korijena $x_0$ u polinomu $g(x)$ jednaka $k$, tj. $(x-x_0)^k$ dijeli $g(x)$, onda za svaki cijeli broj $t$ veći ili jednak $0$ i manji od $k$ vrijedi:

$$
f^{t}(x_0)=R^{t}(x_0)
$$

Ovdje oznaka označava $t$-tu derivaciju.

Kongruencija modulo polinom može se primijeniti na redove potencija. Red potencija s beskonačno mnogo članova može, modulo konkretan polinom, biti kongruentan polinomu s konačno mnogo članova. Na primjer:

$$
1+x+x^2+x^3+\ldots \equiv 1+x+\ldots+x^{n-1} \pmod{x^n}
$$

Očito su svi preostali članovi djeljivi s $x^n$, pa je operacija modulo $x^n$ ekvivalentna „odsijecanju”: red potencija s beskonačno mnogo članova odsiječemo na prvih $n$ članova, a informacija u višim članovima izravno se gubi.

U nekim posebnim slučajevima može se računati i modulo drugih polinoma; takvi se slučajevi objašnjavaju u nastavku.

### Evaluacija polinoma u više točaka i interpolacija

**Evaluacija polinoma u više točaka (multi-point evaluation)** znači: za zadani polinom $f(x)$ i $n$ točaka $x_{1}, x_{2}, \dots, x_{n}$ izračunati

$$
f(x_{1}), f(x_{2}), \dots, f(x_{n})
$$

**Interpolacija polinoma (interpolation)** znači: za zadanih $n+1$ točaka

$$
(x_{0}, y_{0}), (x_{1}, y_{1}), \dots, (x_{n}, y_{n})
$$

naći polinom $f(x)$ stupnja $n$ takav da svih $n+1$ točaka leži na $f(x)$.

Bit je tih dviju operacija prevođenje polinoma između **prikaza koeficijentima** i **prikaza vrijednostima u točkama**. Evaluacija u više točaka prevodi prikaz polinoma koeficijentima u prikaz vrijednostima u točkama, a interpolacija prevodi prikaz vrijednostima u točkama u prikaz koeficijentima.

???+ note "Napomena"
    Gledano sa stajališta redova potencija, evaluacija u više točaka odgovara „sažimanju” informacije o beskonačno mnogo članova u prikaz konačno mnogo vrijednostima u točkama, pa se dio informacije gubi, dok interpolacija odgovara vraćanju u prikaz koeficijentima odgovarajućeg stupnja.
    
    Evaluacija i interpolacija uobičajene u programiranju, npr. diskretna Fourierova transformacija (i njezin inverz), biraju $n+1$ točaka od kojih svaka ima kratnost $1$, tj. sve su međusobno različite, čime se izbjegava gnjavaža s deriviranjem.
    
    Takvo „sažimanje” jamči jedino podudaranje u $n+1$ točaka. Prema gornjem objašnjenju kongruencije modulo polinom, ako red potencija $f(x)$ evaluiramo u točkama od $x_0$ do $x_n$ pa interpoliramo i dobijemo polinom $R(x)$, onda za polinom:
    
    $$
    g(x)=(x-x_0)\ldots(x-x_n)
    $$
    
    vrijedi:
    
    $$
    f(x) \equiv R(x) \pmod{g(x)}
    $$
    
    Budući da je stupanj od $R(x)$ strogo manji od stupnja od $g(x)$, $R(x)$ dobiven evaluacijom i interpolacijom upravo je ostatak. Dakle, u tom slučaju, ako se red potencija može evaluirati u korijenima, može se računati modulo polinom. Jedan protuprimjer:

    $$
    \frac{1}{1-x}=1+x+x^2+x^3+\ldots
    $$
    
    ne može se evaluirati u $x=1$, pa se red $1+x+x^2+x^3+\ldots$ ne može računati modulo polinom $x-1$.
    
    Budući da vrijednost derivacije bilo kojeg reda reda potencija u točki $0$ uvijek postoji, modulo $x^n$ uvijek se može računati, što se slaže s gornjim značenjem „odsijecanja”. Diskretna Fourierova transformacija (i njezin inverz) odgovara računanju modulo polinom $x^n-1$.

### Faktorizacija i Euklidov algoritam

Mnogi rezultati elementarne teorije brojeva mogu se poopćiti na polinome.

Nad poljem kompleksnih brojeva iz osnovnog teorema algebre slijedi da za polinom $f$ stupnja $n$ jednadžba

$$
f(x)=0
$$

ima točno $n$ rješenja (višestruki korijeni broje se s kratnošću).

Stoga se $f(x)$ nad poljem kompleksnih brojeva može jedinstveno faktorizirati u obliku

$$
a(x-x_1)^{c_1}(x-x_2)^{c_2}\cdots(x-x_m)^{c_m}
$$

$$
c_1+c_2+\cdots+c_m=n,x_1,x_2,\cdots,x_m \text{ međusobno različiti}
$$

Tada se, analogno najvećem zajedničkom djelitelju pozitivnih cijelih brojeva, dobiva [**najveći zajednički djelitelj**](../number-theory/gcd.md) polinoma  
(greatest common divisor, gcd). Može se izračunati Euklidovim algoritmom

$$
\gcd(f,0)=f,\gcd(f,g)=\gcd(g,f\bmod g)
$$

To se svojstvo može poopćiti na općenitiju situaciju:

> Za prsten polinoma $P[x]$ nad proizvoljnim poljem $P$  
> polinomi se mogu jedinstveno faktorizirati, a najveći zajednički djelitelj može se računati Euklidovim algoritmom.
> Treba napomenuti da za polinome nad općim prstenom taj rezultat ne mora vrijediti.

Kad Euklidov algoritam vrijedi, proširenim Euklidovim algoritmom može se dati jedno partikularno rješenje $(P(x),Q(x))$ neodređene jednadžbe

$$
f(x)P(x)+g(x)Q(x)=\gcd(f(x),g(x))
$$

a [Bézoutovim teoremom](../number-theory/bezouts.md) odrediti rješivost neodređene jednadžbe

$$
f(x)P(x)+g(x)Q(x)=h(x)
$$

[HALF-GCD](https://loj.ac/p/172) omogućuje nam računanje Euklidova algoritma za polinome u vremenu $O(n\log^2 n)$.

### Multiplikativni inverz modulo polinom

Modulo polinom $h(x)$ red potencija $f(x)$ ponekad ima inverz. Inverz je upravo ostatak recipročne vrijednosti reda potencija $f(x)$ modulo polinom $h(x)$.

Ta je definicija ekvivalentna i ovoj: za polinom $f(x)$, ako postoji $g(x)$ takav da:

$$
\begin{aligned}
    f(x) g(x) & \equiv 1 \pmod{h(x)}
\end{aligned}
$$

onda $g(x)$ zovemo **inverzom (inverse element)** od $f(x)$ modulo $h(x)$. Kad je Euklidov algoritam za polinome dopušten, inverz postoji ako i samo ako je $\gcd(f,h)=1$.

Inverz modulo polinom $h(x)$ uvijek je jedinstven. Ako je i stupanj polinoma $f(x)$ manji od stupnja od $h(x)$, dobiveni $g(x)$ i $f(x)$ međusobno su inverzi.

Imajući na umu pojam „odsijecanja”, inverz modulo $x^n$ obično se označava $f^{-1}(x)$ i to je pojam inverza koji se podrazumijeva u nastavku. Ako nije drukčije rečeno, modul inverza je $x^n$.

???+ note "Napomena"
    Postavlja se pitanje može li se „inverz” izravno izračunati raznim interpolacijskim transformacijama, npr. računanjem:
    
    $$
    IDFT\left(\frac{DFT(1)}{DFT(f(x))}\right)
    $$
    
    Odgovor je niječan, to se ne smije. Prema gornjem objašnjenju, inverz izravno dobiven diskretnom Fourierovom transformacijom (i njezinim inverzom) inverz je modulo polinom $x^n-1$, a ne uobičajeni inverz modulo polinom $x^n$. Osim toga, budući da izvorni polinom u pojedinim točkama može imati vrijednost $0$, to računanje ne mora uvijek biti izvedivo.

## Funkcije izvodnice

Funkcija izvodnica (generating function), zvana i generirajuća funkcija, formalni je red potencija čiji koeficijenti pružaju informacije o nekom nizu.

Postoji mnogo različitih vrsta funkcija izvodnica, ali većina se može prikazati u jedinstvenom obliku:

$$
F(x)=\sum_n a_nk_n(x)
$$

gdje se $k_n(x)$ zove jezgrena funkcija. Različite jezgrene funkcije daju različite funkcije izvodnice s različitim svojstvima. Na primjer:

1.  Obična funkcija izvodnica: $k_n(x)=x^n$.
2.  Eksponencijalna funkcija izvodnica: $k_n(x)=\dfrac{x^n}{n!}$.
3.  [Dirichletova funkcija izvodnica](../number-theory/dirichlet.md#dirichlet-生成函数): $k_n(x)=\dfrac{1}{n^x}$.

## Literatura i daljnje čitanje

-   [**Picks's Blog**](https://picks.logdown.com)
-   [**Miskcoo's Space**](https://blog.miskcoo.com)
-   [**Polynomial ring - Wikipedia**](https://en.wikipedia.org/wiki/Polynomial_ring)
-   [**Formal power series - Wikipedia**](https://en.wikipedia.org/wiki/Formal_power_series#The_ring_of_formal_power_series)
-   《信息学竞赛中的生成函数计算理论框架》 (Teorijski okvir za računanje funkcija izvodnica na informatičkim natjecanjima)
