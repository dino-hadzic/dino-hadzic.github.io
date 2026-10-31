---
title: Möbiusova inverzija
---

Predznanje: [blokovsko dijeljenje po cjelobrojnom kvocijentu](./sqrt-decomposition.md), [Dirichletova konvolucija](./dirichlet.md#dirichletova-konvolucija)

Möbiusova inverzija važan je dio teorije brojeva. Ako je za neku funkciju $f(n)$ teško izravno izračunati vrijednost, a lako je izračunati zbroj po višekratnicima ili zbroj po djeliteljima $g(n)$, Möbiusovom inverzijom može se pojednostavniti račun i dobiti vrijednost $f(n)$.

## Möbiusova funkcija

Möbiusova funkcija (Möbius function) definira se kao

$$
\mu(n)=
\begin{cases}
1,&n=1,\\
0,&n\text{ is divisible by a square }>1,\\
(-1)^k,&n\text{ is the product of }k\text{ distinct primes}.\\
\end{cases}
$$

Konkretno, neka pozitivan cijeli broj $n$ ima rastav na proste faktore $n=\prod_{i=1}^kp_i^{e_i}$, gdje su $p_i$ prosti brojevi, a $e_i$ pozitivni cijeli brojevi. Tada tri slučaja redom odgovaraju sljedećem:

1.  $\mu(1) = 1$;
2.  ako postoji $i$ takav da je $e_i > 1$, tj. ako se bilo koji prosti faktor pojavljuje više od jednom, onda je $\mu(n)=0$;
3.  inače, ako je $e_i = 1$ za sve $i$, tj. svaki se prosti faktor pojavljuje točno jednom, onda je $\mu(n)=(-1)^k$, gdje je $k$ broj različitih prostih faktora.

### Svojstva

Prema definiciji lako se provjerava da je Möbiusova funkcija $\mu(n)$ multiplikativna, ali ne i potpuno multiplikativna. Osim toga, najvažnije je svojstvo sljedeći identitet:

???+ note "Svojstvo"
    Za pozitivan cijeli broj $n$ vrijedi
    
    $$
    \sum_{d\mid n}\mu(d) = [n = 1] =
    \begin{cases}
    1,&n=1,\\
    0,&n\neq 1.\\
    \end{cases}
    $$
    
    Pritom je $[\cdot]$ Iversonova zagrada.

??? note "Dokaz"
    Neka je $n=\prod_{i=1}^kp_i^{e_i}$ i neka je $n' = \prod_{i=1}^kp_i$. Prema [binomnom teoremu](../combinatorics/combination.md#binomni-teorem) vrijedi
    
    $$
    \sum_{d\mid n}\mu(d) = \sum_{d\mid n'}\mu(d) = \sum_{i=0}^k\binom{k}{i}(-1)^i = (1 + (-1))^k = [k = 0] = [n = 1].
    $$

Pomoću Dirichletove konvolucije ovaj se izraz može zapisati kao $\varepsilon = 1 * \mu$. Drugim riječima, Möbiusova funkcija Dirichletov je inverz konstantne funkcije $1$.

Ovo svojstvo ima vrlo čestu primjenu:

$$
[i\perp j] = [\gcd(i,j) = 1] = \sum_{d\mid\gcd(i,j)} \mu(d) = \sum_{d}[d\mid i][d\mid j]\mu(d).
$$

Ono pretvara uvjet relativne prostosti u sumu po Möbiusovoj funkciji, što olakšava daljnje izvođenje.

### Računanje

Ako treba izračunati vrijednost Möbiusove funkcije $\mu(n)$ za jedan $n$, može se iskoristiti njegov [rastav na proste faktore](./pollard-rho.md). Primjerice, kada $n$ nije prevelik, $\mu(n)$ se može izračunati u vremenu $O(\sqrt{n})$.

???+ example "Referentna implementacija"
    === "C++"
        ```cpp
        --8<-- "docs/math/code/mobius/mobius-func-1.cpp:core"
        ```
    
    === "Python"
        ```python
        --8<-- "docs/math/code/mobius/mobius-func-1.py:core"
        ```

Ako treba unaprijed izračunati vrijednosti $\mu(n)$ za prvih $n$ pozitivnih cijelih brojeva, može se iskoristiti to što je ona multiplikativna i izračunati ih [linearnim sitom](./sieve.md#sito-za-möbiusovu-funkciju) u vremenu $O(n)$.

???+ example "Referentna implementacija"
    === "C++"
        ```cpp
        --8<-- "docs/math/code/mobius/mobius-func-2.cpp:core"
        ```
    
    === "Python"
        ```python
        --8<-- "docs/math/code/mobius/mobius-func-2.py:core"
        ```

## Möbiusova inverzija

Najvažnija primjena Möbiusove funkcije jest Möbiusova inverzija.

???+ note "Möbiusova inverzija"
    Neka su $f(n),g(n)$ dvije aritmetičke funkcije. Tada vrijedi
    
    $$
    f(n) = \sum_{d\mid n}g(d) \iff g(n) = \sum_{d\mid n}\mu\left(\dfrac{n}{d}\right)f(d).
    $$

??? note "Dokaz 1"
    Izravnom provjerom dobivamo:
    
    $$
    \begin{aligned}
    \sum_{d\mid n}\mu\left(\dfrac{n}{d}\right)f(d)
    &= \sum_{d\mid n}\mu\left(\dfrac{n}{d}\right)\sum_{k\mid d}g(k)\\
    &= \sum_{k\mid n}g(k)\sum_d[k\mid d\mid n]\mu\left(\dfrac{n}{d}\right)\\
    &= \sum_{k\mid n}g(k)\sum_{d\mid n}\left[\frac{n}{d}\mid\frac{n}{k}\right]\mu\left(\dfrac{n}{d}\right)\\
    &= \sum_{k\mid n}g(k)\left[\frac{n}{k} = 1\right] \\
    &= g(n).
    \end{aligned}
    $$
    
    Ključ preoblikovanja jest zamjena redoslijeda sumiranja i opažanje da je $k\mid d\mid n$ ekvivalentno s $\dfrac{n}{d}\mid\dfrac{n}{k}$. Pretposljednja jednakost odgovara sumiranju Möbiusove funkcije po djeliteljima $\dfrac{n}{d}$ broja $\dfrac{n}{k}$, pa je jednaka $\left[\dfrac{n}{k} = 1\right]$. Taj je izraz različit od $0$ samo za $n=k$, pa na kraju dobivamo $g(n)$.

??? note "Dokaz 2"
    Pomoću Dirichletove konvolucije tvrdnja je ekvivalentna s
    
    $$
    f = 1 * g \iff g = \mu * f.
    $$
    
    Pomoću $1 * \mu = \varepsilon$, konvolucijom obiju strana lijeve jednakosti s $\mu$ dobivamo
    
    $$
    f * \mu = (1 * g) * \mu = (1 * \mu) * g = \varepsilon * g = g.
    $$

U sumiranju aritmetičkih funkcija koje uključuje razne relacije djeljivosti Möbiusova inverzija moćan je alat za preoblikovanje.

???+ example "Primjer"
    1.  [Eulerova funkcija](./euler-totient.md) $\varphi(n)$ zadovoljava relaciju $n = \sum_{d\mid n}\varphi(d)$, tj. $\mathrm{id}=1*\varphi$. Inverzijom dobivamo $\varphi = \mu * \mathrm{id}$, tj.
    
        $$
        \varphi(n) = \sum_{d\mid n}d\mu\left(\dfrac{n}{d}\right).
        $$
    2.  Funkcija djelitelja $\sigma_k(n) = \sum_{d\mid n}d^k$, tj. $\sigma_k = 1 * \mathrm{id}_k$. Inverzijom dobivamo $\mathrm{id}_k = \mu * \sigma_k$, tj.
    
        $$
        n^k = \sum_{d\mid n}\mu\left(\dfrac{n}{d}\right)\sigma_k(d).
        $$
    3.  Funkcija broja različitih prostih faktora $\omega(n)=\sum_{d\mid n}[d\in\mathbf P]$, tj. $\omega = 1* \mathbf{1}_{\mathbf P}$, gdje je $\mathbf{1}_{\mathbf P}$ indikatorska funkcija skupa prostih brojeva $\mathbf P$. Inverzijom dobivamo $\mathbf{1}_{\mathbf P} = \mu * \omega$, tj.
    
        $$
        [n\in\mathbf P] = \sum_{d\mid n}\mu\left(\dfrac{n}{d}\right)\omega(d).
        $$
    4.  Promotrimo aritmetičku funkciju $\Lambda(n)$ koja zadovoljava $\log n = \sum_{d\mid n}\Lambda(d)$. To je Möbiusova inverzija logaritamske funkcije, a naziva se i von Mangoldtova funkcija:
    
        $$
        \Lambda(n) = \sum_{d\mid n}\mu\left(\dfrac{n}{d}\right)\log d = 
        \begin{cases}
        \log p, & n = p^e,~p\in\mathbf P,~e\in\mathbf N_+, \\
        0, &\text{otherwise}.
        \end{cases}
        $$

??? note "Dodatak: dokaz izraza za $\Lambda(n)$"
    Za potenciju prostog broja $n=p^e~(e\in\mathbf N_+)$ vrijedi
    
    $$
    \Lambda(n) = \sum_{i=0}^e\mu(p^{e-i})\log p^i = \log p^{e} - \log p^{e-1} = \log p.
    $$
    
    Za $n=1$ očito je $\Lambda(n)=\log 1=0$. Za ostale složene brojeve $n$ vrijedi
    
    $$
    \Lambda(n) = \sum_{d\mid n}\mu(d)(\log n-\log d) = \left(\sum_{d\mid n}\mu(d)\right)\log n-\sum_{d\mid n}\mu(d)\log d.
    $$
    
    Prema svojstvu Möbiusove funkcije, koeficijent uz $\log n$ jednak je $[n=1]=0$. Za drugi član, $d$ se može dalje rastaviti na umnožak prostih faktora. Za bilo koji prost broj $p\mid n$ neka je $n=p^em$ i $p\perp m$ (budući da $n$ nije potencija prostog broja, $m>1$); promotrimo koeficijent uz $\log p$ (doprinose samo $d$ bez kvadratnih faktora):
    
    $$
    -\sum_{p\mid d\mid n}\mu(d) = -\sum_{d'\mid m}\mu(pd') = \sum_{d'\mid m}\mu(d') = [m=1]=0.
    $$
    
    Stoga za složene brojeve $n$ s više od jednog prostog faktora vrijedi $\Lambda(n)=0$.

### Prošireni oblici

Osim gornjeg osnovnog oblika, Möbiusova inverzija ima i nekoliko čestih proširenih oblika. Najprije razmotrimo njezin oblik sa zbrojem po višekratnicima.

???+ note "Proširenje 1"
    Neka su $f(n),g(n)$ dvije aritmetičke funkcije. Tada vrijedi
    
    $$
    f(n) = \sum_{n\mid d}g(d) \iff g(n) = \sum_{n\mid d}\mu\left(\dfrac{d}{n}\right)f(d).
    $$

??? note "Dokaz"
    Izravnom provjerom dobivamo:
    
    $$
    \begin{aligned}
    \sum_{n\mid d}\mu\left(\dfrac{d}{n}\right)f(d)
    &= \sum_{n\mid d}\mu\left(\dfrac{d}{n}\right)\sum_{d\mid k}g(k)\\
    &= \sum_{n\mid k}g(k)\sum_{d}[n\mid d\mid k]\mu\left(\dfrac{d}{n}\right)\\
    &= \sum_{n\mid k}g(k)\sum_{n\mid d}\left[\dfrac{d}{n}\mid\dfrac{k}{n}\right]\mu\left(\dfrac{d}{n}\right)\\
    &= \sum_{n\mid k}g(k)\left[\dfrac{k}{n}=1\right]\\
    &= g(n).
    \end{aligned}
    $$
    
    To je potpuno dualno izvodu osnovnog oblika.

Drugo, Möbiusova inverzija nije ograničena na zbrajanje; ona zapravo vrijedi za operaciju u bilo kojoj [Abelovoj grupi](../algebra/basic.md#群). Primjerice, ima sljedeći multiplikativni oblik:

???+ note "Proširenje 2"
    Neka su $f(n),g(n)$ dvije aritmetičke funkcije. Tada vrijedi
    
    $$
    f(n) = \prod_{d\mid n}g(d) \iff g(n) = \prod_{d\mid n}f(d)^{\mu(n/d)}.
    $$

??? note "Dokaz"
    Izravnom provjerom dobivamo:
    
    $$
    \begin{aligned}
    \prod_{d\mid n}f(d)^{\mu(n/d)}
    &= \prod_{d\mid n}\left(\prod_{k\mid d}g(k)\right)^{\mu(n/d)}\\
    &= \prod_{k\mid n}g(k)\uparrow\left(\sum_d[k\mid d\mid n]\mu\left(\dfrac{n}{d}\right)\right)\\
    &= \prod_{k\mid n}g(k)\uparrow\left(\sum_{d\mid n}\left[\frac{n}{d}\mid\frac{n}{k}\right]\mu\left(\dfrac{n}{d}\right)\right)\\
    &= \prod_{k\mid n}g(k)\uparrow\left[\frac{n}{k} = 1\right] \\
    &= g(n).
    \end{aligned}
    $$
    
    Pritom je $a\uparrow b = a^b$ Knuthova strelica. Usporedbom s dokazom osnovnog oblika vidi se da je jedina razlika to što je zbrajanje zamijenjeno množenjem, a množenje potenciranjem.

Iz perspektive Dirichletove konvolucije, Möbiusova inverzija koristi samo činjenicu da je „Möbiusova funkcija Dirichletov inverz konstantne funkcije”. Lako je zamisliti da relacije slične Möbiusovoj inverziji vrijede i za opći [Dirichletov inverz](./dirichlet.md#dirichletova-konvolucija).

???+ note "Proširenje 3"
    Neka su $f(n),g(n),\alpha(n)$ aritmetičke funkcije i neka je $\alpha^{-1}(n)$ Dirichletov inverz od $\alpha(n)$, tj.
    
    $$
    [n=1] = \sum_{d\mid n}\alpha\left(\dfrac{n}{d}\right)\alpha^{-1}(d).
    $$
    
    Tada vrijedi
    
    $$
    f(n) = \sum_{d\mid n}\alpha\left(\dfrac{n}{d}\right)g(d) \iff g(n) = \sum_{d\mid n}\alpha^{-1}\left(\dfrac{n}{d}\right)f(d).
    $$

??? note "Dokaz"
    Izravnom provjerom dobivamo:
    
    $$
    \begin{aligned}
    \sum_{d\mid n}\alpha^{-1}\left(\dfrac{n}{d}\right)f(d)
    &= \sum_{d\mid n}\alpha^{-1}\left(\dfrac{n}{d}\right)\sum_{k\mid d}\alpha\left(\dfrac{d}{k}\right)g(k)\\
    &= \sum_{k\mid n}g(k)\sum_d[k\mid d\mid n]\alpha\left(\dfrac{d}{k}\right)\alpha^{-1}\left(\dfrac{n}{d}\right)\\
    &= \sum_{k\mid n}g(k)\sum_{d\mid n}\left[\frac{n}{d}\mid\frac{n}{k}\right]\alpha\left(\dfrac{d}{k}\right)\alpha^{-1}\left(\dfrac{n/k}{d/k}\right)\\
    &= \sum_{k\mid n}g(k)\left[\frac{n}{k} = 1\right] \\
    &= g(n).
    \end{aligned}
    $$
    
    U usporedbi s dokazom osnovnog oblika, treba samo pretposljednju jednakost zamijeniti definicijskom formulom Dirichletova inverza.

???+ note "Korolar"
    Neka su $f(n),g(n)$ aritmetičke funkcije i neka je $t(n)$ potpuno multiplikativna funkcija. Tada vrijedi
    
    $$
    f(n) = \sum_{d\mid n}t\left(\dfrac{n}{d}\right)g(d) \iff g(n) = \sum_{d\mid n}\mu\left(\dfrac{n}{d}\right)t\left(\dfrac{n}{d}\right)f(d).
    $$

??? note "Dokaz"
    Prema [svojstvima](./dirichlet.md#svojstva) Dirichletove konvolucije, Dirichletov inverz potpuno multiplikativne funkcije $t(n)$ jest $\mu(n)t(n)$.

Naposljetku, Möbiusova inverzija može se poopćiti i na kompleksne funkcije na $[1,+\infty)$, a ne samo na aritmetičke funkcije. Osnovni oblik Möbiusove inverzije može se shvatiti kao poseban slučaj u kojem kompleksna funkcija u svim necjelobrojnim točkama ima vrijednost nula.

???+ note "Proširenje 4"
    Neka su $F(x)$ i $G(x)$ kompleksne funkcije na $[1,+\infty)$. Tada vrijedi
    
    $$
    F(x) = \sum_{n = 1}^{\lfloor x\rfloor}G\left(\dfrac{x}{n}\right) \iff G(x) = \sum_{n = 1}^{\lfloor x\rfloor}\mu(n)F\left(\dfrac{x}{n}\right).
    $$

??? note "Dokaz"
    Bez smanjenja općenitosti proširimo definicije $F$ i $G$ tako da za $x < 1$ uvijek vrijedi $F(x)=G(x)=0$. Tada je tvrdnja ekvivalentna s:
    
    $$
    F(x) = \sum_n G\left(\dfrac{x}{n}\right) \iff G(x) = \sum_n \mu(n)F\left(\dfrac{x}{n}\right).
    $$
    
    Sve se ove sume uzimaju po $n\in\mathbf N_+$.
    
    Izravnom provjerom dobivamo:
    
    $$
    \begin{aligned}
    \sum_n \mu(n)F\left(\dfrac{x}{n}\right)
    &= \sum_n\mu(n)\sum_d G\left(\dfrac{x/n}{d}\right)\\
    &= \sum_k G\left(\dfrac{x}{k}\right)\sum_{n\mid k}\mu(n)\\
    &= \sum_k G\left(\dfrac{x}{k}\right)[k=1]\\
    &= G(x).
    \end{aligned}
    $$
    
    Pritom za drugu jednakost treba staviti $k = nd$.

???+ note "Korolar"
    Neka su $f(n),g(n)$ aritmetičke funkcije. Tada vrijedi
    
    $$
    f(n) = \sum_{k=1}^ng\left(\left\lfloor\dfrac{n}{k}\right\rfloor\right) \iff g(n)=\sum_{k=1}^n\mu(k)f\left(\left\lfloor\dfrac{n}{k}\right\rfloor\right).
    $$

??? note "Dokaz"
    Dovoljno je uzeti $F(x)=f(\lfloor x\rfloor)$ i $G(x)=g(\lfloor x\rfloor)$.

Ovi se prošireni oblici mogu međusobno kombinirati, čime se dobivaju složenije relacije inverzije.

### Dirichletove prefiksne sume

Predznanje: [Prefiksne sume i razlike](../../basic/prefix-sum.md)

Promotrimo osnovni oblik Möbiusove inverzije:

$$
f(n) = \sum_{d\mid n}g(d) \iff g(n) = \sum_{d\mid n}\mu\left(\dfrac{n}{d}\right)f(d).
$$

U lijevoj jednakosti vrijednost $f(n)$ zbroj je vrijednosti $g$ u svim djeliteljima od $n$. Ako $a\mid b$ shvatimo kao „$a$ je poredan prije $b$”, onda se $f(n)$ može shvatiti kao prefiksna suma od $g(n)$ u određenom smislu. Zato se u kineskoj natjecateljskoj zajednici postupak računanja $\{f(k)\}_{k=1}^n$ iz $\{g(k)\}_{k=1}^n$ naziva i **Dirichletova prefiksna suma**, a odgovarajući obrnuti postupak Dirichletova razlika. Ove se metode uglavnom pojavljuju kada treba unaprijed izračunati vrijednosti neke aritmetičke funkcije u prvih $N$ točaka.

Razmotrimo sada računanje Dirichletovih prefiksnih suma. Ako svaki prost broj promatramo kao jednu dimenziju, riječ je o vrsti višedimenzionalnih prefiksnih suma. Prisjetimo se [algoritma prefiksnih suma dimenziju po dimenziju](../../basic/prefix-sum.md#prefiksne-sume-dimenziju-po-dimenziju) za višedimenzionalne prefiksne sume: prolazimo redom sve dimenzije i vrijednost na svakoj poziciji pribrajamo sljedbeniku te pozicije u toj dimenziji. Za aritmetičke funkcije to znači: prolazimo sve proste brojeve $p$ od manjih prema većima i vrijednost funkcije u $n$ pribrajamo vrijednosti u $np$. To je isti redoslijed obilaska kao u [Eratostenovu situ](./sieve.md#eratostenovo-sito). Stoga ovaj algoritam računa Dirichletovu prefiksnu sumu niza duljine $n$ u vremenu $O(n\log\log n)$. Slično, razlikama dimenziju po dimenziju može se u istoj vremenskoj složenosti izračunati Dirichletova razlika niza.

???+ example "Referentna implementacija"
    === "Dirichletova prefiksna suma"
        ```cpp
        --8<-- "docs/math/code/mobius/mobius-func-3.cpp:presum"
        ```
    
    === "Dirichletova razlika"
        ```cpp
        --8<-- "docs/math/code/mobius/mobius-func-3.cpp:diff"
        ```

Ova se metoda računanja može poopćiti na zbroj po višekratnicima (proširenje 1), multiplikativni oblik (proširenje 2), zamjenu konstantne funkcije potpuno multiplikativnom funkcijom (korolar proširenja 3) i druge proširene oblike.

## Primjeri zadataka

Ovaj odjeljak kroz primjere zadataka pokazuje način primjene Möbiusove inverzije i neke česte tehnike preoblikovanja. Najprije se kroz jedan zadatak upoznajemo s osnovnom tehnikom obrade uvjeta s najvećim zajedničkim djeliteljem u sumama.

???+ example "[Luogu P2522 \[HAOI 2011\] Problem b](https://www.luogu.com.cn/problem/P2522)"
    $T$ skupova podataka. Za svaki skup izračunajte:
    
    $$
    \sum_{i=x}^{n}\sum_{j=y}^{m}[\gcd(i,j)=k].
    $$
    
    Ograničenja: $1\le T,x,y,n,m,k\le 5\times 10^4$.

??? note "Rješenje"
    Prema načelu uključivanja-isključivanja, izvorni izraz može se razbiti na $4$ dijela, a izraz svakog dijela ima oblik
    
    $$
    f(n,m,k)=\sum_{i=1}^{n}\sum_{j=1}^{m}[\gcd(i,j)=k].
    $$
    
    Za takve izraze slijedi standardni postupak izvođenja: izlučivanje zajedničkog faktora, primjena svojstva Möbiusove funkcije, zamjena redoslijeda sumiranja.
    
    Najprije, budući da $i,j$ mogu biti samo višekratnici od $k$, taj se faktor može izlučiti – to odgovara uvrštavanju $i=ki'$ i $j=kj'$, čime dobivamo:
    
    $$
    f(n,m,k)=\sum_{i=1}^{\lfloor n/k\rfloor}\sum_{j=1}^{\lfloor m/k\rfloor}[\gcd(i,j)=1].
    $$
    
    Zatim prema svojstvu Möbiusove funkcije vrijedi:
    
    $$
    [\gcd(i,j)=1] = \sum_{d\mid\gcd(i,j)}\mu(d) = \sum_d[d\mid i][d\mid j]\mu(d).
    $$
    
    Uvrštavanjem u izraz i zamjenom redoslijeda sumiranja dobivamo:
    
    $$
    f(n,m,k)=\sum_d\mu(d)\left(\sum_{i=1}^{\lfloor n/k\rfloor}[d\mid i]\right)\left(\sum_{j=1}^{\lfloor m/k\rfloor}[d\mid j]\right).
    $$
    
    Prednost ovog postupka jest to što se, za fiksni $d$, članovi sume koji ovise o $i$ i o $j$ međusobno razdvajaju pa se mogu zbrajati zasebno. Dalje, budući da je
    
    $$
    \sum_{i=1}^{\lfloor n/k\rfloor}[d\mid i] = \left\lfloor\dfrac{\lfloor n/k\rfloor}{d}\right\rfloor,~\sum_{j=1}^{\lfloor m/k\rfloor}[d\mid j]=\left\lfloor\dfrac{\lfloor m/k\rfloor}{d}\right\rfloor,
    $$
    
    vrijedi
    
    $$
    f(n,m,k)=\sum_d\mu(d)\left\lfloor\dfrac{\lfloor n/k\rfloor}{d}\right\rfloor\left\lfloor\dfrac{\lfloor m/k\rfloor}{d}\right\rfloor.
    $$
    
    Nakon što linearnim sitom unaprijed izračunamo $\mu(d)$ i njegove prefiksne sume, zadatak se rješava blokovskim dijeljenjem po cjelobrojnom kvocijentu. Ukupna vremenska složenost iznosi $O(N + T\sqrt{N})$, gdje je $N$ gornja granica za $n,m$, a $T$ broj skupova podataka.

??? note "Referentni kod"
    ```cpp
    --8<-- "docs/math/code/mobius/mobius_1.cpp"
    ```

Sljedeća dva zadatka pokazuju način obrade iteriranjem po zajedničkom faktoru te računanje vrijednosti općih multiplikativnih funkcija [sitom](./sieve.md#opće-multiplikativne-funkcije).

???+ example "[SPOJ LCMSUM](https://www.spoj.com/problems/LCMSUM/)"
    $T$ skupova podataka. Za svaki skup izračunajte:
    
    $$
    \sum_{i=1}^n \operatorname{lcm}(i,n).
    $$
    
    Ograničenja: $1\le T\le 3\times 10^5,~1\le n\le 10^6$.

??? note "Rješenje 1"
    Zadatak daje najmanji zajednički višekratnik, ali je najveći zajednički djelitelj često lakše obraditi. Stoga najprije preoblikujemo:
    
    $$
    f(n)=\sum_{i=1}^n \operatorname{lcm}(i,n) = \sum_{i=1}^n \frac{i\cdot n}{\gcd(i,n)}.
    $$
    
    Izlučimo $n$ i iterirajmo po najvećem zajedničkom djelitelju $k$:
    
    $$
    f(n)=n\sum_{k\mid n}\sum_{i=1}^n\dfrac{i}{k}[\gcd(i,n)=k].
    $$
    
    Unutarnja suma najčešći je oblik izraza s najvećim zajedničkim djeliteljem; ponavljanjem standardnog postupka dobivamo:
    
    $$
    \begin{aligned}
    f(n) &= n\sum_{k\mid n}\sum_{i=1}^{n/k}i\left[\gcd\left(i,\dfrac{n}{k}\right)=1\right]\\
    &= n\sum_{k\mid n}\sum_{i=1}^{n/k}i\sum_d\mu(d)[d\mid i]\left[d\mid \dfrac{n}{k}\right]\\
    &= n\sum_{k\mid n}\sum_d\mu(d)\left[d\mid \dfrac{n}{k}\right]\left(\sum_{i=1}^{n/k}i[d\mid i]\right).
    \end{aligned}
    $$
    
    Ponovno se suma po $i$ odvaja od ostatka pa se može obraditi zasebno. Posljednja suma zapravo je zbroj aritmetičkog niza (uz $i=di'$):
    
    $$
    \sum_{i=1}^{n/k}i[d\mid i] = d\frac{1}{2}\left(\dfrac{n}{kd}+1\right)\dfrac{n}{kd}=:dG\left(\dfrac{n}{kd}\right).
    $$
    
    Time dobivamo sljedeći izraz:
    
    $$
    f(n) = n\sum_{k\mid n}\sum_d\mu(d)\left[d\mid \dfrac{n}{k}\right]dG\left(\dfrac{n}{kd}\right).
    $$
    
    Nakon iteriranja po zajedničkom faktoru dvostruke sume ovakvog oblika vrlo su česte. I za njih postoji ustaljeni postupak: umnožak uvedemo kao novu varijablu $\ell=kd$ i zatim ponovno zamijenimo redoslijed sumiranja. Budući da je $d\mid(n/k)$ ekvivalentno s $d\mid\ell\mid n$, izvorni se izraz pretvara u:
    
    $$
    f(n) = n\sum_{\ell\mid n}G\left(\dfrac{n}{\ell}\right)\sum_{d\mid\ell}\mu(d)d.
    $$
    
    Neka je $F(\ell)=\sum_{d\mid\ell}\mu(d)d$; tada izvorni izraz ima oblik:
    
    $$
    f(n) = n\sum_{\ell\mid n}G\left(\dfrac{n}{\ell}\right)F(\ell).
    $$
    
    Budući da je $\mu(d)d$ multiplikativna funkcija, i njezina konvolucija $F(n)$ s konstantnom funkcijom $1$ multiplikativna je funkcija. Iako u gornjem izrazu suma ima oblik Dirichletove konvolucije, $G(n)$ nije multiplikativna funkcija pa ni suma u cjelini nije multiplikativna. Međutim, $G(n)$ je polinom pa je zapravo linearna kombinacija nekoliko potpuno multiplikativnih funkcija. Stoga vrijedi
    
    $$
    f(n) = \dfrac{1}{2}n\left(\sum_{\ell\mid n}\left(\dfrac{n}{\ell}\right)^2F(\ell) + \sum_{\ell\mid n}\dfrac{n}{\ell}F(\ell)\right).
    $$
    
    Oba člana (bez koeficijenata) multiplikativne su funkcije pa se mogu izravno unaprijed izračunati linearnim sitom (ili se unutarnja funkcija izračuna linearnim sitom, a zatim se Dirichletovim prefiksnim sumama sve unaprijed izračuna u vremenu $O(N\log\log N)$). Konkretno, neka je
    
    $$
    H_s(n) = \sum_{\ell\mid n}\left(\dfrac{n}{\ell}\right)^sF(\ell),~s=1,2.
    $$
    
    Za izvođenje njihovih izraza dovoljno je odrediti njihove vrijednosti na potencijama prostih brojeva. Za prost broj $p$ i pozitivan eksponent $e$ vrijedi
    
    $$
    \begin{aligned}
    F(p^e) &= \mu(1) + \mu(p)p + \sum_{j=2}^e\mu(p^j)p^j = 1-p,\\
    H_s(p^e) &= (p^e)^{s}F(1) + \sum_{j=1}^e(p^{e-j})^sF(p^j) = p^{es} + (1-p)\dfrac{1-p^{es}}{1-p^s},~s=1,2.
    \end{aligned}
    $$
    
    Posebno, $H_1(p^e)=1$ je konstantna funkcija, a
    
    $$
    H_2(p^e) = p^{2e} + (1-p)\dfrac{1-p^{2e}}{1-p^2} = H_2(p^{e-1}) + p^{2e} - p^{2e-1}.
    $$
    
    To se lako računa linearnim sitom. Nakon što se linearnim sitom unaprijed izračuna $H_2(n)$, pojedini se upit rješava izrazom $f(n)=(n/2)(H_2(n)+1)$ u vremenu $O(1)$. Ukupna vremenska složenost iznosi $O(N+T)$, gdje je $N$ gornja granica za $n$, a $T$ broj skupova podataka.
    
    U referentnoj implementaciji, koristeći posebnost izraza u ovom zadatku, dio s linearnim sitom dodatno je izveden, što nije nužno. Samo pomoću vrijednosti na potencijama prostih brojeva predračunavanje se i dalje može obaviti u vremenu $O(N)$. Ti su izvodi detaljno opisani u rješenju 2.

??? note "Rješenje 2"
    Za ovaj zadatak postoji i fleksibilniji pristup. Iz rješenja 1 vidi se da je
    
    $$
    f(n) = n\sum_{k\mid n}\sum_{i=1}^{n/k}i\left[\gcd\left(i,\dfrac{n}{k}\right)=1\right] = n\sum_{k\mid n}F\left(\dfrac{n}{k}\right).
    $$
    
    Ako u ovom koraku ne nastavimo s Möbiusovom inverzijom, nego uočimo da je suma koja slijedi zapravo zbroj cijelih brojeva koji ne premašuju $d=n/k$ i relativno su prosti s njime. Za $d>1$, budući da se brojevi relativno prosti s $d$ pojavljuju u parovima, tj. $i$ i $d-i$ nužno su istodobno relativno prosti s $d$, vrijedi
    
    $$
    F(d)=\sum_{i=1}^{d}i[i\perp d] = \sum_{i=1}^{d}(d-i)[i\perp d] = \dfrac{1}{2}d\sum_{i=1}^{d}[i\perp d] = \dfrac{1}{2}d\varphi(d).
    $$
    
    Za $d=1$ pak vrijedi
    
    $$
    F(d)=1=\dfrac{1}{2}+\dfrac{1}{2}d\varphi(d).
    $$
    
    Nadalje, izvorni se izraz može prikazati kao
    
    $$
    f(n) = \dfrac{1}{2}n\left(\sum_{d\mid n}d\varphi(d) + 1\right).
    $$
    
    Budući da je $G(n)=\sum_{d\mid n}d\varphi(d)$ Dirichletova konvolucija multiplikativne funkcije $n\varphi(n)$ i konstantne funkcije $1$, i ona je multiplikativna pa se može unaprijed izračunati linearnim sitom. U tu je svrhu dovoljno odrediti njezine vrijednosti na potencijama prostih brojeva. Za prost broj $p$ i pozitivan eksponent $e$ vrijedi
    
    $$
    G(p^e) = 1 + \sum_{i=1}^ep^i\cdot p^{i-1}(p-1) = G(p^{e-1}) + p^{2e} - p^{2e-1}.
    $$
    
    Vidi se da se ovaj izraz podudara s rezultatom izvedenim u rješenju 1. Ukupna vremenska složenost ove metode i dalje je $O(N+T)$.
    
    Naposljetku, pomoću izraza za multiplikativnu funkciju u ovom zadatku može se dodatno optimizirati računanje u linearnom situ. Za prost broj $p$ vrijedi
    
    $$
    G(p) = 1 - p + p^2.
    $$
    
    Ključ linearnog sita jest to što za opći $n$ treba izračunati vrijednost $G(pn)$. To se dalje dijeli na dva slučaja. Kada je $p\perp n$, budući da je $G$ multiplikativna, vrijedi
    
    $$
    G(pn) = G(p)G(n).
    $$
    
    Inače, kada je $p\mid n$, neka je $n=p^em$ uz $p\perp m$; tada je
    
    $$
    \begin{aligned}
    G(pn) &= G(p^{e+1})G(m)\\
    &= G(p^e)G(m) + (p^{2e+2} - p^{2e+1})G(m)\\
    &= G(n) + (p^{2e+2} - p^{2e+1})G(m).
    \end{aligned}
    $$
    
    Izravnom provjerom vidi se da ovaj izraz vrijedi i za slučaj $p\perp n$ (tj. $e=0$). A kada je $p\mid n$, vrijedi još
    
    $$
    G(n) - G\left(\dfrac{n}{p}\right) = (p^{2e}-p^{2e-1})G(m).
    $$
    
    Uvrštavanjem u gornji izraz dobivamo
    
    $$
    G(pn) = G(n) + p^2\left(G(n) - G\left(\dfrac{n}{p}\right)\right).
    $$
    
    To pojednostavnjuje računanje u dijelu s linearnim sitom. Dakako, ovaj izvod nije nužan; za multiplikativne funkcije bez posebnih svojstava računanje linearnim sitom može se obaviti izravno pomoću $G(pn)=G(p^{e+1})G(m)$.

??? note "Referentni kod"
    ```cpp
    --8<-- "docs/math/code/mobius/mobius_2.cpp"
    ```

???+ example "[BZOJ 2154 \[国家集训队\] Crash 的数字表格 (Crasheva brojčana tablica)](https://hydro.ac/p/bzoj-P2154)"
    Izračunajte:
    
    $$
    \sum_{i=1}^n\sum_{j=1}^m\operatorname{lcm}(i,j)\mod{20101009}.
    $$
    
    Ograničenja: $1\le n,m\le 10^7$.

??? note "Rješenje"
    U izvodu zanemarujemo modul. Neka je
    
    $$
    f(n,m) = \sum_{i=1}^n\sum_{j=1}^m\operatorname{lcm}(i,j).
    $$
    
    I dalje najmanji zajednički višekratnik pretvaramo u najveći zajednički djelitelj, iteriramo po zajedničkom djelitelju i primjenjujemo standardni postupak obrade, čime dobivamo
    
    $$
    \begin{aligned}
    f(n,m)
    &= \sum_k\sum_{i=1}^n\sum_{j=1}^m\dfrac{ij}{k}[\gcd(i,j)=k] \\
    &= \sum_k\sum_{i=1}^{\lfloor n/k\rfloor}\sum_{j=1}^{\lfloor m/k\rfloor} kij[\gcd(i,j)=1]\\
    &= \sum_k\sum_{i=1}^{\lfloor n/k\rfloor}\sum_{j=1}^{\lfloor m/k\rfloor} kij\sum_d\mu(d)[d\mid i][d\mid j]\\
    &= \sum_kk\sum_d\mu(d)\left(\sum_{i=1}^{\lfloor n/k\rfloor}i[d\mid i]\right)\left(\sum_{j=1}^{\lfloor m/k\rfloor}j[d\mid j]\right).
    \end{aligned}
    $$
    
    Ponovno se suma razdvaja po $i$ i $j$. Najprije izračunajmo te unutarnje sume; izlučivanjem faktora (tj. uz $i=di'$) dobivamo
    
    $$
    \sum_{i=1}^{\lfloor n/k\rfloor}i[d\mid i] = d\sum_{i=1}^{\lfloor\lfloor n/k\rfloor/d\rfloor}i = dG\left(\left\lfloor\dfrac{\lfloor n/k\rfloor}{d}\right\rfloor\right) = dG\left(\left\lfloor\dfrac{n}{kd}\right\rfloor\right).
    $$
    
    Pritom je $G(n)=\dfrac{1}{2}n(n+1)$ upravo zbroj aritmetičkog niza, a posljednja jednakost koristi svojstvo [funkcije najvećeg cijelog](./basic.md#funkcije-pod-i-strop). Simetrično, druga se suma računa analogno. Uvrštavanjem natrag u prethodni izraz dobivamo
    
    $$
    f(n,m) = \sum_k k\sum_{d}\mu(d)d^2G\left(\left\lfloor\dfrac{n}{kd}\right\rfloor\right)G\left(\left\lfloor\dfrac{m}{kd}\right\rfloor\right).
    $$
    
    Kao i prije, za ovakve izraze s iteriranjem po zajedničkom faktoru obično treba iterirati po umnošku $\ell = kd$ i ponovno zamijeniti redoslijed sumiranja:
    
    $$
    f(n,m) = \sum_{\ell}\left(\sum_{d\mid\ell}\mu(d)d\ell\right)G\left(\left\lfloor\dfrac{n}{\ell}\right\rfloor\right)G\left(\left\lfloor\dfrac{m}{\ell}\right\rfloor\right).
    $$
    
    Neka je
    
    $$
    F(\ell) = \sum_{d\mid\ell}\mu(d)d\ell.
    $$
    
    To je umnožak multiplikativne funkcije $\ell$ i multiplikativne funkcije $\sum_{d\mid\ell}\mu(d)d$, pa je i sama multiplikativna; može se izravno unaprijed izračunati linearnim sitom, kao i njezine prefiksne sume. Zatim se vrijednost $f(n,m)$ računa blokovskim dijeljenjem po cjelobrojnom kvocijentu. Ukupna vremenska složenost iznosi $O(\min\{n,m\})$.

??? note "Referentni kod"
    ```cpp
    --8<-- "docs/math/code/mobius/mobius_3.cpp"
    ```

Sljedeći je zadatak nešto poseban: zahtijeva pretvorbu funkcije broja djelitelja umnoška.

???+ example "[LOJ 2185. \[SDOI2015\] 约数个数和 (Zbroj broja djelitelja)](https://loj.ac/problem/2185)"
    $T$ skupova podataka. Za svaki skup izračunajte:
    
    $$
    \sum_{i=1}^n\sum_{j=1}^m\sigma_0(ij).
    $$
    
    Pritom $\sigma_0(n)=\sum_{d \mid n}1$ označava broj djelitelja od $n$.
    
    Ograničenja: $1\le n,m,T\le 5\times 10^4$.

??? note "Rješenje"
    Teškoća ovog zadatka jest pretvoriti $\sigma_0(ij)$ u izraz s najvećim zajedničkim djeliteljem. Budući da je $\sigma_0$ multiplikativna, najprije razmotrimo slučaj potencija prostih brojeva. Za prost broj $p$ i nenegativne eksponente $e_1,e_2$ neka je $i=p^{e_1},~j=p^{e_2}$; tada je
    
    $$
    \sigma_0(ij) = 1 + e_1 + e_2 = \sum_{x\mid i}\sum_{y\mid j}[x\perp y].
    $$
    
    U općem slučaju neka je $i=\prod_p i_p$ i $j=\prod_p j_p$, gdje su $i_p,j_p$ redom faktori koji su potencije prostog broja $p$ u rastavima $i,j$ na proste faktore. Tada vrijedi
    
    $$
    \sigma_0(ij) = \prod_p\sigma_0(i_pj_p)= \prod_p\sum_{x_p\mid i_p}\sum_{y_p\mid j_p}[x_p\perp y_p].
    $$
    
    Uočimo da je iteriranje po djeliteljima $x_p$ svakog faktora $i_p$ od $i$ koji je potencija prostog broja isto što i iteriranje po djeliteljima $x$ od $i$ te rastavljanje svakoga na faktore $x_p$ koji su potencije prostih brojeva; analogno za $j$. Stoga, prema distributivnosti množenja, izraz postaje
    
    $$
    \sigma_0(ij) = \sum_{x\mid i}\sum_{y\mid j}\prod_p[x_p\perp y_p] = \sum_{x\mid i}\sum_{y\mid j}[x\perp y].
    $$
    
    Posljednji korak koristi zaključak: $x\perp y$ ako i samo ako za svaki prosti faktor $p$ vrijedi $x_p\perp y_p$.
    
    Nakon što dobijemo ovaj izraz, možemo primijeniti standardni postupak obrade:
    
    $$
    \begin{aligned}
    \sigma_0(ij) 
    &= \sum_{x\mid i}\sum_{y\mid j}[x\perp y]\\
    &= \sum_{x\mid i}\sum_{y\mid j}\sum_d\mu(d)[d\mid x][d\mid y]\\
    &= \sum_d\mu(d)\left(\sum_{x}[d\mid x\mid i]\right)\left(\sum_{y}[d\mid y\mid j]\right)\\
    &= \sum_d\mu(d)[d\mid i][d\mid j]\sigma_0\left(\dfrac{i}{d}\right)\sigma_0\left(\dfrac{j}{d}\right).
    \end{aligned}
    $$
    
    Značenje posljednjeg koraka izvoda jest: funkcija je različita od nule samo kada je $d\mid i$ i $d\mid j$, a tada je iteriranje po $x$ koji zadovoljavaju $d\mid x\mid i$ isto što i iteriranje po djeliteljima $\dfrac{x}{d}$ broja $\dfrac{i}{d}$; analogno za iteriranje po $y$ koji zadovoljavaju $d\mid y\mid j$.
    
    Uvrstimo ovaj izraz natrag u izvorni i zamijenimo redoslijed sumiranja:
    
    $$
    \begin{aligned}
    f(n,m)
    &= \sum_{i=1}^n\sum_{j=1}^m\sigma_0(ij)\\
    &= \sum_{i=1}^n\sum_{j=1}^m\sum_d\mu(d)[d\mid i][d\mid j]\sigma_0\left(\dfrac{i}{d}\right)\sigma_0\left(\dfrac{j}{d}\right)\\
    &= \sum_d\mu(d)\left(\sum_{i=1}^n[d\mid i]\sigma_0\left(\dfrac{i}{d}\right)\right)\left(\sum_{j=1}^m[d\mid j]\sigma_0\left(\dfrac{j}{d}\right)\right)\\
    &= \sum_d\mu(d)\left(\sum_{i=1}^{\lfloor n/d\rfloor}\sigma_0(i)\right)\left(\sum_{j=1}^{\lfloor m/d\rfloor}\sigma_0(j)\right).
    \end{aligned}
    $$
    
    Neka je $G(n)=\sum_{i=1}^n\sigma_0(i)$; tada je
    
    $$
    f(n,m)=\sum_{d}\mu(d)G\left(\left\lfloor\dfrac{n}{d}\right\rfloor\right)G\left(\left\lfloor\dfrac{m}{d}\right\rfloor\right).
    $$
    
    To se rješava blokovskim dijeljenjem po cjelobrojnom kvocijentu. Dovoljno je unaprijed izračunati prefiksne sume od $\mu(n)$ i $\sigma_0(n)$. Ukupna vremenska složenost iznosi $O(N+T\sqrt{N})$, gdje je $N$ gornja granica za $n,m$, a $T$ broj skupova podataka.

??? note "Referentni kod"
    ```cpp
    --8<-- "docs/math/code/mobius/mobius_4.cpp"
    ```

Posljednji zadatak pokazuje kako primijeniti multiplikativnu inačicu Möbiusove inverzije.

???+ example "[Luogu P5221 Product](https://www.luogu.com.cn/problem/P5221)"
    Izračunajte:
    
    $$
    \prod_{i=1}^n\prod_{j=1}^n\dfrac{\operatorname{lcm}(i,j)}{\gcd(i,j)}\pmod{104857601}.
    $$
    
    Ograničenja: $1\le n\le 1\times 10^6$.

??? note "Rješenje 1"
    U izvodu zanemarujemo modul. Neka je
    
    $$
    f(n) = \prod_{i=1}^n\prod_{j=1}^n\dfrac{\operatorname{lcm}(i,j)}{\gcd(i,j)}.
    $$
    
    I dalje najmanji zajednički višekratnik pretvaramo u najveći zajednički djelitelj:
    
    $$
    f(n) = \prod_{i=1}^n\prod_{j=1}^n\dfrac{ij}{(\gcd(i,j))^2}.
    $$
    
    Uočimo da su umnošci ovih faktora međusobno neovisni pa se mogu računati zasebno. Neka je
    
    $$
    g(n) = \prod_{i=1}^n\prod_{j=1}^n\gcd(i,j).
    $$
    
    Izvorni je izraz tada jednak:
    
    $$
    f(n) = \dfrac{(n!)^{2n}}{g(n)^2}.
    $$
    
    Ključno je riješiti računanje $g(n)$. Postupak obrade sličan je prethodno opisanome, ali ga treba zamijeniti odgovarajućom multiplikativnom inačicom. Najprije iteriramo po zajedničkom djelitelju i izlučimo ga:
    
    $$
    \begin{aligned}
    g(n) &= \prod_k\prod_{i=1}^n\prod_{j=1}^nk\uparrow[\gcd(i,j)=k]\\
    &= \prod_k\prod_{i=1}^{\lfloor n/k\rfloor}\prod_{j=1}^{\lfloor n/k\rfloor}k\uparrow[\gcd(i,j)=1].
    \end{aligned}
    $$
    
    Pritom je $a\uparrow b=a^b$ Knuthova strelica. Zatim uvrstimo $[\gcd(i,j)=1]=\sum_d\mu(d)[d\mid i][d\mid j]$ i sumu u eksponentu pretvorimo u umnožak potencija, čime dobivamo:
    
    $$
    g(n) = \prod_k\prod_d\prod_{i=1}^{\lfloor n/k\rfloor}\prod_{j=1}^{\lfloor n/k\rfloor}k\uparrow(\mu(d)[d\mid i][d\mid j]).
    $$
    
    Dalje izlučimo faktor (tj. stavimo $i=di'$, $j=dj'$) i primijenimo svojstvo [funkcije najvećeg cijelog](./basic.md#funkcije-pod-i-strop), čime dobivamo:
    
    $$
    g(n) = \prod_k\prod_d\prod_{i=1}^{\lfloor n/(kd)\rfloor}\prod_{j=1}^{\lfloor n/(kd)\rfloor}k\uparrow\mu(d).
    $$
    
    Zatim razdvojimo umnoške po $i,j$ i uočimo da izraz u umnošku ne sadrži $i,j$, pa je to isto što i potenciranje tog izraza:
    
    $$
    g(n) = \prod_k\prod_d k\uparrow\left(\mu(d)\left\lfloor\dfrac{n}{kd}\right\rfloor^2\right).
    $$
    
    Budući da smo prije iterirali po zajedničkom djelitelju, za ovaj izraz treba ponovno zamijeniti redoslijed množenja. Uz $\ell = kd$ vrijedi:
    
    $$
    \begin{aligned}
    g(n) &= \prod_{\ell}\prod_{d\mid\ell}\left(\dfrac{\ell}{d}\right)\uparrow\left(\mu(d)\left\lfloor\dfrac{n}{\ell}\right\rfloor^2\right)\\
    &= \prod_\ell\left(\prod_{d\mid\ell}\left(\dfrac{\ell}{d}\right)\uparrow\mu(d)\right)\uparrow\left\lfloor\dfrac{n}{\ell}\right\rfloor^2.
    \end{aligned}
    $$
    
    Neka je
    
    $$
    F(n) = \prod_{d\mid n}\left(\dfrac{n}{d}\right)\uparrow\mu(d).
    $$
    
    Lako se vidi da je to Möbiusova inverzija funkcije $\tilde F(n)=n$ u multiplikativnom obliku. Čak i ako ne znamo njezin izraz, može se unaprijed izračunati metodom [Dirichletovih razlika](#dirichletove-prefiksne-sume) u vremenu $O(n\log\log n)$. Dakako, budući da je oblik $\tilde F(n)$ vrlo jednostavan, izraz za $F(n)$ može se izravno odrediti:
    
    $$
    F(n) = 
    \begin{cases}
    p, & n = p^e,~p\in\mathbf P,~e\in\mathbf N_+, \\
    1, &\text{otherwise}.
    \end{cases}
    $$
    
    [Von Mangoldtova funkcija](#möbiusova-inverzija) upravo je njezin prirodni logaritam. Nakon što dobijemo vrijednosti $F(n)$, izravnom primjenom multiplikativne inačice blokovskog dijeljenja po cjelobrojnom kvocijentu vrijednost $g(n)$ računa se u vremenu $O(\sqrt{n})$, a time i vrijednost $f(n)$. Ukupna vremenska složenost iznosi $O(n)$.
    
    Vrijedi napomenuti da je pri računanju s umnošcima često potreban [Eulerov teorem](./fermat.md), pa modul koji se koristi za eksponente nije isti kao modul zadan u zadatku.

??? note "Rješenje 2"
    Teškoća izvoda u multiplikativnoj inačici jest to što je baratanje umnošcima i potencijama razmjerno nepoznato; stoga se kod takvih zadataka može i logaritmirati pa tek onda izvoditi. Za ovaj zadatak razmotrimo samo izvod za $g(n)$. Nakon logaritmiranja vrijedi:
    
    $$
    \log g(n) = \sum_{i=1}^n\sum_{j=1}^n\log\gcd(i,j).
    $$
    
    Za ovakve izraze s najvećim zajedničkim djeliteljem izravnom primjenom standardnog postupka izvođenja dobivamo:
    
    $$
    \begin{aligned}
    \log g(n) 
    &= \sum_k\log k\sum_{i=1}^n\sum_{j=1}^n[\gcd(i,j)=k]\\
    &= \sum_k\log k\sum_{i=1}^{\lfloor n/k\rfloor}\sum_{j=1}^{\lfloor n/k\rfloor}[\gcd(i,j)=1]\\
    &= \sum_k\log k\sum_d\mu(d)\left(\sum_{i=1}^{\lfloor n/k\rfloor}[d\mid i]\right)\left(\sum_{j=1}^{\lfloor n/k\rfloor}[d\mid j]\right)\\
    &= \sum_k\log k\sum_d\mu(d)\left\lfloor\dfrac{n}{kd}\right\rfloor^2\\
    &= \sum_{\ell}\left(\sum_{d\mid\ell}\mu(d)\log\dfrac{\ell}{d}\right)\left\lfloor\dfrac{n}{\ell}\right\rfloor^2\\
    &= \sum_{\ell}\Lambda(\ell)\left\lfloor\dfrac{n}{\ell}\right\rfloor^2.
    \end{aligned}
    $$
    
    Pritom je $\Lambda(n)$ [von Mangoldtova funkcija](#möbiusova-inverzija). Potenciranjem ovog rezultata dobiva se rezultat iz rješenja 1.

??? note "Referentni kod"
    ```cpp
    --8<-- "docs/math/code/mobius/mobius_5.cpp"
    ```

## Zadaci za vježbu

-   [Luogu P3312 \[SDOI2014\] 数表 (Brojčana tablica)](https://www.luogu.com.cn/problem/P3312)
-   [Luogu P3700 \[CQOI2017\] 小 Q 的表格 (Tablica malog Q-a)](https://www.luogu.com.cn/problem/P3700)
-   [Luogu P3704 \[SDOI2017\] 数字表格 (Brojčana tablica)](https://www.luogu.com.cn/problem/P3704)
-   [Luogu P3768 简单的数学题 (Jednostavan matematički zadatak)](https://www.luogu.com.cn/problem/P3768)
-   [Luogu P4464 \[国家集训队\] JZPKIL](https://www.luogu.com.cn/problem/P4464)
-   [Luogu P4619 \[SDOI2018\] 旧试题 (Stari ispitni zadatak)](https://www.luogu.com.cn/problem/P4619)
-   [Luogu P5518 \[MtOI2019\] 幽灵乐团 (Orkestar duhova)](https://www.luogu.com.cn/problem/P5518)
-   [Luogu P6222 简单题 加强版 (Jednostavan zadatak, pojačana verzija)](https://www.luogu.com.cn/problem/P6222)
-   [Luogu P6825「EZEC-4」求和 (Zbrajanje)](https://www.luogu.com.cn/problem/P6825)
-   [Luogu P7486「Stoi2031」彩虹 (Duga)](https://www.luogu.com.cn/problem/P7486)
-   [AtCoder Grand Contest 038 C - LCMs](https://atcoder.jp/contests/agc038/tasks/agc038_c)
-   [Codeforces 1139 D. Steps to One](https://codeforces.com/problemset/problem/1139/D)

## Literatura

-   [Möbius function - Wikipedia](https://en.wikipedia.org/wiki/M%C3%B6bius_function)
-   [Möbius inversion formula - Wikipedia](https://en.wikipedia.org/wiki/M%C3%B6bius_inversion_formula)
-   [Von Mangoldt function - Wikipedia](https://en.wikipedia.org/wiki/Von_Mangoldt_function)
-   [algocode 算法博客 (algocode blog o algoritmima)](https://web.archive.org/web/20190523150159/https://algocode.net/2018/04/18/20180418-KB-Mobius-Inversion-Formula/)
