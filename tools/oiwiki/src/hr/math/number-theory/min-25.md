---
title: Min_25 sito
---

## Definicija

Prema ideji na kojoj se temelji, ova se metoda sita naziva i „Extended Eratosthenes Sieve” (prošireno Eratostenovo sito).

Budući da ju je izumio i prvi počeo koristiti [Min\_25](https://web.archive.org/web/20211104125457/http://min-25.hatenablog.com/), naziva se „Min\_25 sito”.

## Svojstva

Može riješiti problem prefiksnih suma jedne klase **multiplikativnih funkcija** u vremenskoj složenosti $O\left(\frac{n^{\frac{3}{4}}}{\log{n}}\right)$ ili $\Theta\left(n^{1 - \epsilon}\right)$.

Zahtjevi: $f(p)$ je zbroj potpuno multiplikativnih funkcija u $p$ koje se mogu brzo evaluirati (npr. polinom); $f(p^{c})$ može se brzo evaluirati.

## Oznake

-   **Ako nije drukčije rečeno, sve varijable označene s $p$ u ovom odjeljku poprimaju vrijednosti iz skupa svih prostih brojeva.**
-   $x / y := \left\lfloor\frac{x}{y}\right\rfloor$
-   $\operatorname{isprime}(n) := [ |\{d : d \mid n\}| = 2 ]$, tj. vrijednost je $1$ ako je $n$ prost, inače $0$.
-   $p_{k}$: $k$-ti najmanji prost broj među svim prostim brojevima (npr. $p_{1} = 2, p_{2} = 3$). Posebno, stavljamo $p_{0} = 1$.
-   $\operatorname{lpf}(n) := [1 < n] \min\{p : p \mid n\} + [1 = n]$, tj. najmanji prosti faktor broja $n$. Posebno, za $n=1$ vrijednost je $1$.
-   $F_{\mathrm{prime}}(n) := \sum_{2 \le p \le n} f(p)$
-   $F_{k}(n) := \sum_{i = 2}^{n} [p_{k} \le \operatorname{lpf}(i)] f(i)$

## Objašnjenje

Promotrimo li definiciju $F_{k}(n)$, vidimo da je odgovor upravo $F_{1}(n) + f(1) = F_{1}(n) + 1$.

Razmotrimo kako izračunati $F_{k}(n)$. Nabrajanjem najmanjeg prostog faktora svakog $i$ i njegova eksponenta dobivamo rekurziju:

$$
\begin{aligned}
    F_{k}(n)
    &= \sum_{i = 2}^{n} [p_{k} \le \operatorname{lpf}(i)] f(i) \\
    &= \sum_{\substack{k \le i \\ p_{i}^{2} \le n}} \sum_{\substack{c \ge 1 \\ p_{i}^{c} \le n}} f\left(p_{i}^{c}\right) ([c > 1] + F_{i + 1}\left(n / p_{i}^{c}\right)) + \sum_{\substack{k \le i \\ p_{i} \le n}} f(p_{i}) \\
    &= \sum_{\substack{k \le i \\ p_{i}^{2} \le n}} \sum_{\substack{c \ge 1 \\ p_{i}^{c} \le n}} f\left(p_{i}^{c}\right) ([c > 1] + F_{i + 1}\left(n / p_{i}^{c}\right)) + F_{\mathrm{prime}}(n) - F_{\mathrm{prime}}(p_{k - 1}) \\
    &= \sum_{\substack{k \le i \\ p_{i}^{2} \le n}} \sum_{\substack{c \ge 1 \\ p_{i}^{c + 1} \le n}} \left(f\left(p_{i}^{c}\right) F_{i + 1}\left(n / p_{i}^{c}\right) + f\left(p_{i}^{c + 1}\right)\right) + F_{\mathrm{prime}}(n) - F_{\mathrm{prime}}(p_{k - 1})
\end{aligned}
$$

Posljednji korak izvoda temelji se na sljedećoj činjenici: za $c$ koje zadovoljava $p_{i}^{c} \le n < p_{i}^{c + 1}$ vrijedi $p_{i}^{c + 1} > n \iff n / p_{i}^{c} < p_{i} < p_{i + 1}$, pa je $F_{i + 1}\left(n / p_{i}^{c}\right) = 0$.  
Rubna je vrijednost $F_{k}(n) = 0 (p_{k} > n)$.

Pretpostavimo da smo već izračunali sve $F_{\mathrm{prime}}(n)$; tada postoje dva načina da izračunamo sve $F_{k}(n)$:

1.  Izravno računamo po rekurziji.
2.  Nabrajamo $p$ od najvećeg prema najmanjem i radimo prijelaze; doprinos prijelaza različit je od nule samo kad je $p^{2} < n$, pa je dovoljno rekurziju optimizirati sufiksnim sumama.

Razmotrimo sada kako izračunati $F_{\mathrm{prime}}{(n)}$.  
Promatrajući postupak računanja $F_{k}(n)$, lako je uočiti da su od vrijednosti $F_{\mathrm{prime}}$ korisne jedino one u $O(\sqrt{n})$ točaka $1, 2, \dots, \left\lfloor\sqrt{n}\right\rfloor, n / \sqrt{n}, \dots, n / 2, n$.  
U općem je slučaju $f(p)$ polinom niskog stupnja u $p$ i može se zapisati kao $f(p) = \sum a_{i} p^{c_{i}}$.  
Tada je za svaki $p^{c_{i}}$ njegov doprinos u $F_{\mathrm{prime}}(n)$ jednak $a_{i} \sum_{2 \le p \le n} p^{c_{i}}$.  
Promatramo li doprinos svakog $p^{c_{i}}$ zasebno, problem postaje: za zadane $n, s, g(p) = p^{s}$, za sve $m = n / i$ izračunati $\sum_{p \le m} g(p)$.

???+ tip "Napomena"
    $g(p) = p^{s}$ potpuno je multiplikativna funkcija!

Stavimo stoga $G_{k}(n) := \sum_{i = 2}^{n} \left[p_{k} < \operatorname{lpf}(i) \lor \operatorname{isprime}(i)\right] g(i)$, tj. zbroj vrijednosti $g$ brojeva koji preostaju nakon $k$-tog kruga Eratostenova sita.  
Za složeni broj $x \le n$ nužno vrijedi $\operatorname{lpf}(x) \le \sqrt{x} \le \sqrt{n}$. Neka je $p_{\ell(n)}$ najveći prost broj koji ne prelazi $\sqrt{n}$; tada je $\sum_{2\le p\le n}g(p) = G_{\ell(n)}(n)$, tj. nakon $\ell$ krugova Eratostenova sita preostaju samo prosti brojevi.
Razmotrimo rubnu vrijednost $G$; očito je $G_{0}(n) = \sum_{i = 2}^{n} g(i)$. (Sjećate se? Posebno smo dogovorili $p_{0} = 1$.)  
Za prijelaz razmotrimo postupak Eratostenova sita i zasebno raspravimo doprinos svakog dijela:

1.  Za dio gdje je $n < p_{k}^{2}$ vrijednost $G$ se ne mijenja, tj. $G_{k}(n) = G_{k - 1}(n)$.
2.  Za dio gdje je $p_{k}^{2} \le n$ izbačeni brojevi nužno imaju prosti faktor $p_{k}$, tj. $-g(p_{k}) G_{k - 1}(n / p_{k})$.
3.  U drugom dijelu, budući da je $p_{k}^{2} \le n \iff p_{k} \le n / p_{k}$, brojevi $i$ koji zadovoljavaju $\operatorname{lpf}(i) < p_{k}$ bit će oduzeti prekomjerno. Taj dio treba dodati natrag, tj. $g(p_{k}) G_{k - 1}(p_{k - 1})$.

Dakle:

$$
G_{k}(n) = G_{k - 1}(n) - \left[p_{k}^{2} \le n\right] g(p_{k}) (G_{k - 1}(n / p_{k}) - G_{k - 1}(p_{k - 1}))
$$

## Analiza složenosti

Za računanje $F_{k}(n)$ prvom metodom dokazana je vremenska složenost $O\left(n^{1 - \epsilon}\right)$ (vidi rad Zhu Zhentinga iz kineskog nacionalnog pripremnog tima [《一些特殊的数论函数求和问题》](https://github.com/OI-wiki/libs/blob/master/%E9%9B%86%E8%AE%AD%E9%98%9F%E5%8E%86%E5%B9%B4%E8%AE%BA%E6%96%87/%E5%9B%BD%E5%AE%B6%E9%9B%86%E8%AE%AD%E9%98%9F2018%E8%AE%BA%E6%96%87%E9%9B%86.pdf) (Neki posebni problemi sumacije teorijsko-brojevnih funkcija), odjeljak 2.3);  
druga je metoda u biti drugi dio Zhou sita, a spominje se i u radu Ren Zhizhoua [《积性函数求和的几种方法》](https://github.com/OI-wiki/libs/blob/master/%E9%9B%86%E8%AE%AD%E9%98%9F%E5%8E%86%E5%B9%B4%E8%AE%BA%E6%96%87/%E5%9B%BD%E5%AE%B6%E9%9B%86%E8%AE%AD%E9%98%9F2016%E8%AE%BA%E6%96%87%E9%9B%86.pdf) (Nekoliko metoda sumacije multiplikativnih funkcija) (6.5.4); dokazana joj je vremenska složenost $O\left(\frac{n^{\frac{3}{4}}}{\log{n}}\right)$.

Što se tiče računanja $F_{\mathrm{prime}}(n)$, njegova je implementacija zapravo jednaka prvom dijelu Zhou sita.  
Uočimo da za svaki $m = n / i$ vremenskoj složenosti doprinose samo prijelazi pri nabrajanju onih $p_{k}$ koji zadovoljavaju $p_{k}^{2} \le m$, pa se vremenska složenost može procijeniti kao:

$$
\begin{aligned}
    T(n)
    &= \sum_{i^{2} \le n} O\left(\pi\left(\sqrt{i}\right)\right) + \sum_{i^{2} \le n} O\left(\pi\left(\sqrt{\frac{n}{i}}\right)\right) \\
    &= \sum_{i^{2} \le n} O\left(\frac{\sqrt{i}}{\ln{\sqrt{i}}}\right) + \sum_{i^{2} \le n} O\left(\frac{\sqrt{\frac{n}{i}}}{\ln{\sqrt{\frac{n}{i}}}}\right) \\
    &= O\left(\int_{1}^{\sqrt{n}} \frac{\sqrt{\frac{n}{x}}}{\log{\sqrt{\frac{n}{x}}}} \mathrm{d} x\right) \\
    &= O\left(\frac{n^{\frac{3}{4}}}{\log{n}}\right)
\end{aligned}
$$

Što se tiče prostorne složenosti, vidimo da i $F_{k}$ i $F_{\mathrm{prime}}$ poprimaju korisne vrijednosti samo u točkama $n / i$, kojih je ukupno $O(\sqrt{n})$; pamtimo li samo korisne vrijednosti, prostorna se složenost može optimizirati na $O(\sqrt{n})$.

Prvo, jednim blokovskim dijeljenjem po cjelobrojnom kvocijentu možemo dobiti sve korisne vrijednosti i zapamtiti ih u nizu $\text{lis}$ veličine $O(\sqrt{n})$. Za korisnu vrijednost $v$ označimo s $\text{id}(v)$ indeks vrijednosti $v$ u nizu $\text{lis}$; lako se vidi da za sve korisne vrijednosti $v$ vrijedi $\text{id}(v) \le \sqrt{n}$.

Zatim zasebno razmotrimo korisne vrijednosti manje ili jednake $\sqrt{n}$ i one veće od $\sqrt{n}$: za korisnu vrijednost $v$ manju ili jednaku $\sqrt{n}$ njezin $\text{id}(v)$ pamtimo u nizu $\text{le}$, tj. $\text{le}_v = \text{id}(v)$; za korisnu vrijednost $v$ veću od $\sqrt{n}$ njezin $\text{id}(v)$ pamtimo u nizu $\text{ge}$, a kako je $v$ prevelik, $\text{id}(v)$ pamtimo pomoću $v' = n / v < \sqrt{n}$, tj. $\text{ge}_{v'} = \text{id}(v)$.

Tako pomoću dva niza veličine $O(\sqrt{n})$ možemo zapamtiti $\text{id}$ svih korisnih vrijednosti i dohvaćati ih u $O(1)$. Pri računanju $F_{k}$ ili $F_{\mathrm{prime}}$ kao indeks umjesto korisne vrijednosti koristimo njezin $\text{id}$, čime se prostorna složenost optimizira na $O(\sqrt{n})$.

## Postupak

Za računanje $F_{k}(n)$ u implementaciji obično biramo prvu metodu, koju je lakše implementirati; pri manjim veličinama ulaza ona se često ponaša bolje od druge metode.

Za računanje $F_{\mathrm{prime}}(n)$ dovoljno je izravno implementirati rekurziju.

Za $p_{k}^{2} \le n$ linearnim sitom možemo predračunati $s_{k} := F_{\mathrm{prime}}(p_{k})$ i njime zamijeniti $F_{\mathrm{prime}}(p_{k - 1})$ u rekurziji za $F_{k}$.  
Analogno, $G_{k - 1}(p_{k - 1}) = \sum_{i = 1}^{k - 1} g(p_{i})$ u rekurziji za $G$ također se može predračunati na isti način.

Kada Extended Eratosthenes Sieve koristimo za prefiksne sume **multiplikativne funkcije** $f$, treba razjasniti sljedeće:

-   kako brzo (obično u linearnoj vremenskoj složenosti) prosijati prvih $\sqrt{n}$ vrijednosti $f$;
-   polinomni zapis $f(p)$;
-   kako brzo izračunati $f(p^{c})$.

Kad je to razjašnjeno, dovoljno je redom implementirati sljedeće dijelove:

1.  prosijati proste brojeve u $[1, \sqrt{n}]$ i prvih $\sqrt{n}$ vrijednosti $f$;
2.  za svaki član polinomnog zapisa $f(p)$ prosijati odgovarajući $G$ i spajanjem dobiti sve $O(\sqrt{n})$ korisne vrijednosti $F_{\mathrm{prime}}$;
3.  implementirati rekurziju prema rekurzivnoj formuli za $F_{k}$ i izračunati $F_{1}(n)$.

## Primjeri zadataka

???+ example "[Luogu P4213【模板】杜教筛 (Predložak: Du sito)](https://www.luogu.com.cn/problem/P4213)"
    Izračunajte $\displaystyle \sum_{i = 1}^{n} \varphi(i)$ i $\displaystyle \sum_{i = 1}^{n} \mu(i)$.

??? note "Rješenje"
    Za prefiksnu sumu $\varphi(i)$ najprije lako vidimo $f(p) = p - 1$. Za linearni član $(p)$ funkcije $f(p)$ imamo $g(p) = p, G_{0}(n) = \sum_{i = 2}^{n} g(i) = \frac{(n + 2) (n - 1)}{2}$; za konstantni član $(-1)$ funkcije $f(p)$ imamo $g(p) = -1, G_{0}(n) = \sum_{i = 2}^{n} g(i) = -n + 1$. Prosijemo dvaput i zbrojimo te dobivamo sve $O(\sqrt{n})$ potrebne vrijednosti $F_{\mathrm{prime}}$.
    
    Za prefiksnu sumu $\mu(i)$ lako vidimo $f(p) = -1$. Tada je $g(p) = -1, G_{0}(n) = \sum_{i = 2}^{n} g(i) = -n + 1$. Izravnim sijanjem dobivamo sve $O(\sqrt{n})$ potrebne vrijednosti $F_{\mathrm{prime}}$.

???+ example "[LOJ 6053 简单的函数 (Jednostavna funkcija)](https://loj.ac/p/6053)"
    Zadana je $f(n)$:
    
    $$
    f(n) = \begin{cases}
        1 & n = 1 \\
        p \operatorname{xor} c & n = p^{c} \\
        f(a)f(b) & n = ab \land a \perp b
    \end{cases}
    $$
    
    Izračunajte $\displaystyle \sum_{i = 1}^{n} f(i)$.

??? note "Rješenje"
    Lako vidimo $f(p) = p - 1 + 2[p = 2]$. Sijemo, dakle, kao pri sijanju $\varphi$, uz poseban slučaj za $2$.

??? note "Referentni kod"
    ```cpp
    --8<-- "docs/math/code/min-25/min-25_1.cpp"
    ```
