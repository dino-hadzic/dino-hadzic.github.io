---
title: Powerful Number sito
---

## Definicija

Powerful Number sito (u nastavku kratko PN sito) slično je Du situ, odnosno ono je proširenje Du sita, i može se koristiti za računanje prefiksnih suma nekih multiplikativnih funkcija.

**Zahtjevi**:

-   Postoji funkcija $g$ koja zadovoljava:
    -   $g$ je multiplikativna funkcija.
    -   Prefiksne sume $g$ lako se računaju.
    -   Za prost broj $p$ vrijedi $g(p) = f(p)$.

Pretpostavimo da želimo izračunati prefiksnu sumu multiplikativne funkcije $f$, $F(n) = \sum_{i=1}^{n} f(i)$.

## Powerful Number

**Definicija**: Za pozitivan cijeli broj $n$ zapišimo rastav $n$ na proste faktore kao $n = \prod_{i=1}^{m} p_{i}^{e_{i}}$. $n$ je PN ako i samo ako $\forall 1 \le i \le m, e_{i} > 1$.

**Svojstvo 1**: Svaki PN može se zapisati u obliku $a^{2}b^{3}$.

**Dokaz**: Ako je $e_i$ paran, $p_{i}^{e_{i}}$ uključimo u $a^{2}$; ako je $e_i$ neparan, najprije $p_{i}^{3}$ uključimo u $b^{3}$, a zatim $p_{i}^{e_{i}-3}$ uključimo u $a^{2}$.

**Svojstvo 2**: PN-ova koji ne prelaze $n$ ima najviše $O(\sqrt{n})$.

**Dokaz**: Nabrajamo $a$ i zatim promatramo broj odgovarajućih $b$; broj PN-ova približno je jednak

$$
\int_{1}^{\sqrt{n}} \sqrt[3]{\frac{n}{x^2}} \mathrm{d}x = O(\sqrt{n})
$$

Kako, dakle, pronaći sve PN-ove koji ne prelaze $n$? Linearnim sitom pronađemo sve proste brojeve do $\sqrt{n}$, a zatim DFS-om pretražimo eksponente pojedinih prostih brojeva. Budući da PN-ova do $n$ ima najviše $O(\sqrt{n})$, pretraživanje ima najviše $O(\sqrt{n})$ koraka.

## PN sito

Najprije konstruiramo multiplikativnu funkciju $g$ čije se prefiksne sume lako računaju i koja za proste brojeve $p$ zadovoljava $g(p) = f(p)$. Označimo $G(n) = \sum_{i=1}^{n} g(i)$.

Zatim konstruiramo funkciju $h = f / g$, gdje $/$ označava dijeljenje u smislu Dirichletove konvolucije. Prema svojstvima Dirichletove konvolucije $h$ je također multiplikativna funkcija, pa je $h(1) = 1$. Vrijedi $f = g * h$, gdje $*$ označava Dirichletovu konvoluciju.

Za prost broj $p$ vrijedi $f(p) = g(1)h(p) + g(p)h(1) = h(p) + g(p) \implies h(p) = 0$. Iz $h(p)=0$ i multiplikativnosti $h$ slijedi da za broj $n$ koji nije PN vrijedi $h(n) = 0$, tj. $h$ poprima netrivijalne vrijednosti samo na PN-ovima.

Sada iz $f = g * h$ imamo

$$
\begin{aligned}
F(n) &= \sum_{i = 1}^{n} f(i)\\
     &= \sum_{i = 1}^{n} \sum_{d|i} h(d) g\left(\frac{i}{d}\right)\\
     &= \sum_{d=1}^{n} \sum_{i=1}^{\lfloor \frac{n}{d}\rfloor} h(d) g(i)\\
     &= \sum_{d=1}^{n} h(d) \sum_{i=1}^{\lfloor \frac{n}{d}\rfloor}  g(i) \\
     &= \sum_{d=1}^{n} h(d) G\left(\left\lfloor \frac{n}{d}\right\rfloor\right)\\
     &= \sum_{\substack{d=1 \\ d \text{ je PN}}}^{n}h(d) G\left(\left\lfloor \frac{n}{d}\right\rfloor\right)
\end{aligned}
$$

U $O(\sqrt{n})$ pronađemo sve PN-ove i izračunamo sve netrivijalne vrijednosti $h$. Za računanje netrivijalnih vrijednosti $h$ dovoljno je izračunati sve vrijednosti $h(p^c)$, a iz multiplikativnosti $h$ tada slijede sve netrivijalne vrijednosti $h$. Sada za svaku netrivijalnu vrijednost $d$ izračunamo $h(d)G\left(\left\lfloor \dfrac{n}{d} \right\rfloor\right)$ i zbrajanjem dobivamo $F(n)$.

Razmotrimo sada računanje $h(p^c)$; postoje dvije metode: prva je izravno izvesti formulu za $h(p^c)$ koja ovisi samo o $p, c$ te po njoj računati $h(p^c)$; druga je iz $f = g * h$ dobiti $f(p^c) = \sum_{i=0}^c g(p^i)h(p^{c-i})$, odakle prebacivanjem članova slijedi $h(p^c) = f(p^c) - \sum_{i=1}^{c}g(p^i)h(p^{c-i})$, pa sada možemo nabrajati proste brojeve $p$ i zatim eksponente $c$ te izračunati sve $h(p^c)$.

### Postupak

1.  Konstruiramo $g$
2.  Konstruiramo brz način računanja $G$
3.  Izračunamo $h(p^c)$
4.  Pretražujemo PN-ove i pritom akumuliramo odgovor
5.  Dobivamo rezultat

U 3. koraku možemo računati izravno po formuli, možemo nabrajanjem predračunati tablicu, a možemo i računati na licu mjesta kada pretraživanje dođe do odgovarajućeg broja.

### Svojstva

Analizu provodimo na primjeru druge metode računanja $h(p^c)$. Možemo je podijeliti na dva dijela: računanje $h(p^c)$ i pretraživanje.

Za prvi dio: budući da je broj prostih brojeva do $O(\sqrt{n})$ jednak $O\left(\dfrac{\sqrt{n}}{\log n}\right)$, eksponent $c$ svakog prostog broja $p$ iznosi najviše $\log n$, a računanje $h(p^c)$ zahtijeva $(c - 1)$ iteracija petlje, vremenska je složenost prvog dijela $O\left(\dfrac{\sqrt{n}}{\log n} \cdot \log n \cdot \log n\right) = O(\sqrt{n}\log{n})$, i to je labava gornja ograda. Ovisno o zadatku mogu se dodati razne optimizacije kojima se vremenska složenost prvog dijela smanjuje.

Za dio s pretraživanjem: budući da PN-ova do $n$ ima najviše $O(\sqrt{n})$, pretraživanje ima najviše $O(\sqrt{n})$ koraka. Za svaki PN vremenska složenost ovisi o načinu računanja $G$. Primjerice, ako je vremenska složenost računanja $G\left(\left\lfloor \dfrac{n}{d}\right\rfloor\right)$ jednaka $O(1)$, složenost drugog dijela iznosi $O(\sqrt{n})$.

Posebno, ako $G\left(\left\lfloor \dfrac{n}{d}\right\rfloor\right)$ računamo Du sitom, vremenska složenost drugog dijela jednaka je vremenskoj složenosti Du sita, tj. $O(n^{\frac{2}{3}})$. Naime, ako unaprijed jednom izračunamo $G(n)$, uz optimizaciju linearnim sitom i pamćenje većih vrijednosti u strukturi podataka s brzim slučajnim pristupom (kao što su `std::map` i `std::unordered_map` u C++-u), onda su sve vrijednosti $G\left(\left\lfloor \dfrac{n}{d}\right\rfloor\right)$ koje se koriste u Du situ ili zapamćene linearnim sitom ili zapamćene u `std::map`, što se može izravno provjeriti programom.

Što se tiče prostorne složenosti, usko grlo je pohrana $h(p^c)$. Ako koristimo dvodimenzionalni niz $a$ u kojem $a_{i,j}$ označava vrijednost $h(p_i^j)$, prostorna je složenost $O\left(\dfrac{\sqrt{n}}{\log n} \cdot \log n\right) = O(\sqrt{n})$.

## Primjeri zadataka

### [Luogu P5325【模板】Min\_25 筛 (Predložak: Min_25 sito)](https://www.luogu.com.cn/problem/P5325)

**Zadatak**: Zadana je multiplikativna funkcija $f(p^k) = p^k(p^k-1)$; izračunajte $\sum_{i=1}^{n} f(i)$.

Lako se vidi $f(p) = p(p-1) = \operatorname{id}(p)\varphi(p)$, pa konstruiramo $g(n) = \operatorname{id}(n)\varphi(n)$.

Za računanje $G(n)$ koristimo Du sito; iz $(\operatorname{id}\cdot \varphi) * \operatorname{id} = \operatorname{id}_2$ dobivamo $G(n)= \sum_{i=1}^{n} i^2 - \sum_{d=2}^{n} d \cdot G\left(\left\lfloor \dfrac{n}{d} \right\rfloor\right)$.

Nakon toga vrijednosti $h(p^k)$ možemo izračunati nabrajanjem; tu metodu ne ponavljamo.

Osim toga, u ovom zadatku možemo izravno izvesti formulu za $h(p^k)$ koja ovisi samo o $p, k$, i to ovako:

$$
\begin{aligned}
& f(p^k) = \sum_{i=0}^{k} g(p^{k-i})h(p^i)\\
\iff & p^k(p^k-1) = \sum_{i=0}^{k} p^{k-i}\varphi(p^{k-i}) h(p^i)\\
\iff & p^k(p^k-1) = \sum_{i=0}^{k} p^{2k-2i-1}(p - 1) h(p^i)\\
\iff & p^k(p^k-1) = h(p^k) + \sum_{i=0}^{k-1} p^{2k-2i-1}(p - 1) h(p^i)\\
\iff & h(p^k) = p^k(p^k-1) - \sum_{i=0}^{k-1} p^{2k-2i-1}(p - 1) h(p^i)\\
\iff & h(p^k) - p^2h(p^{k-1}) = p^{k}(p^k-1)-p^{k+1}(p^{k-1}-1) - p(p-1)h(p^{k-1})\\
\iff & h(p^k) - ph(p^{k-1}) = p^{k+1} - p^k\\
\iff & \frac{h(p^k)}{p^k} - \frac{h(p^{k-1})}{p^{k-1}} = p - 1\\
\end{aligned}
$$

Uz $h(p) = 0$ teleskopskim zbrajanjem dobivamo $h(p^k) = (k-1)(p-1)p^k$.

??? note "Referentni kod"
    ```cpp
    --8<-- "docs/math/code/powerful-number/powerful-number_1.cpp"
    ```

### [„LOJ #6053” 简单的函数 (Jednostavna funkcija)](https://loj.ac/problem/6053)

Zadana je $f(n)$:

$$
f(n) =
\begin{cases}
1 & n = 1 \\
p \oplus c & n=p^c \\
f(a)f(b) & n=ab \text{ i } a \perp b
\end{cases}
$$

Lako se vidi:

$$
f(p) =
\begin{cases}
p + 1 & p = 2 \\
p - 1 & \text{inače} \\
\end{cases}
$$

Konstruiramo $g$ kao

$$
g(n) =
\begin{cases}
3 \varphi(n) & 2 \mid n \\
\varphi(n) & \text{inače} \\
\end{cases}
$$

Lako se dokazuje da je $g(p) = f(p)$ i da je $g$ multiplikativna funkcija.

Razmotrimo sada računanje $G(n)$.

$$
\begin{aligned}
G(n)
&= \sum_{i=1}^{n}[i \bmod 2 = 1] \varphi(i) + 3 \sum_{i=1}^{n}[i \bmod 2 = 0] \varphi(i)\\
&= \sum_{i=1}^{n} \varphi(i) + 2\sum_{i=1}^{n} [i \bmod 2 = 0]\varphi(i) \\
&= \sum_{i=1}^{n} \varphi(i) + 2\sum_{i=1}^{\lfloor \frac{n}{2} \rfloor} \varphi(2i)
\end{aligned}
$$

Označimo $S_1(n) = \sum_{i=1}^{n} \varphi(i)$, $S_2(n) = \sum_{i=1}^{n} \varphi(2i)$; tada je $G(n) = S_1(n) + 2S_2\left(\left\lfloor \dfrac{n}{2} \right\rfloor\right)$.

Kada je $2 \mid n$, vrijedi

$$
\begin{aligned}
S_2(n)
&= \sum_{i=1}^{n} \varphi(2i) \\
&= \sum_{i=1}^{\frac{n}{2}} (\varphi(2(2i-1)) + \varphi(2(2i))) \\
&= \sum_{i=1}^{\frac{n}{2}} (\varphi(2i-1) + 2\varphi(2i)) \\
&= \sum_{i=1}^{\frac{n}{2}} (\varphi(2i-1) + \varphi(2i)) + \sum_{i=1}^{\frac{n}{2}} \varphi(2i) \\
&= \sum_{i=1}^{n} \varphi(i) + S_2\left(\frac{n}{2}\right)\\
&= S_1(n) + S_2\left(\left\lfloor \frac{n}{2} \right\rfloor\right)\\
\end{aligned}
$$

Kada je $2 \nmid n$, vrijedi

$$
\begin{aligned}
S_2(n)
&= S_2(n-1) + \varphi(2n) \\
&= S_2(n-1) + \varphi(n) \\
&= \sum_{i=1}^{n-1} \varphi(i) + S_2\left(\frac{n-1}{2}\right) + \varphi(n)\\
&= S_1(n) + S_2\left(\left\lfloor \frac{n}{2} \right\rfloor\right)\\
\end{aligned}
$$

Ukupno, vrijedi $S_2(n) = S_1(n) + S_2\left(\left\lfloor \dfrac{n}{2} \right\rfloor\right)$.

$S_1$ se može izračunati Du sitom, a $S_2$ izravno po formuli, pa tako možemo izračunati i $G$.

??? note "Referentni kod"
    ```cpp
    --8<-- "docs/math/code/powerful-number/powerful-number_2.cpp"
    ```

## Zadaci za vježbu

-   [PE708 Twos are all you need](https://projecteuler.net/problem=708)
-   [PE639 Summing a multiplicative function](https://projecteuler.net/problem=639)
-   [PE484 Arithmetic Derivative](https://projecteuler.net/problem=484)

## Literatura

-   [破壁人五号 - Powerful number 筛略解 (Kratko objašnjenje Powerful Number sita)](https://www.cnblogs.com/wallbreaker5th/p/13901487.html)
-   [command\_block - 杜教筛（+ 贝尔级数 + powerful number） (Du sito (+ Bellovi redovi + powerful number))](https://www.luogu.com.cn/blog/command-block/du-jiao-shai)
