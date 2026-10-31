---
title: Diskretni logaritam
---

## Definicija

Predznanje: [Red elementa i primitivni korijen](./primitive-root.md).

Diskretni logaritam definira se slično logaritmu. Uzmimo pozitivan cijeli modul $m$ koji ima primitivni korijen i neka je $g$ jedan njegov primitivni korijen. Za cijeli broj $a$ takav da je $(a,m)=1$ znamo da nužno postoji jedinstven cijeli broj $0\leq k<\varphi(m)$ takav da je

$$
g^k\equiv a\pmod m
$$

Taj $k$ nazivamo diskretnim logaritmom po bazi $g$ modulo $m$ i pišemo $k=\operatorname{ind}_g a$; kad nema opasnosti od zabune, možemo pisati $\operatorname{ind} a$.

Očito je $\operatorname{ind}_g 1=0$, $\operatorname{ind}_g g=1$.

## Svojstva

I svojstva diskretnog logaritma u mnogočemu nalikuju svojstvima logaritma.

???+ note "Svojstva"
    Neka je $g$ primitivni korijen modulo $m$ i $(a,m)=(b,m)=1$. Tada:
    
    1.  $\operatorname{ind}_g(ab)\equiv\operatorname{ind}_g a+\operatorname{ind}_g b\pmod{\varphi(m)}$
    
        Nadalje, $(\forall n\in\mathbf{N}),~~\operatorname{ind}_g a^n\equiv n\operatorname{ind}_g a\pmod{\varphi(m)}$
    2.  Ako je i $g_1$ primitivni korijen modulo $m$, onda je $\operatorname{ind}_g a\equiv\operatorname{ind}_{g_1}a \cdot \operatorname{ind}_g g_1\pmod{\varphi(m)}$
    3.  $a\equiv b\pmod m\iff \operatorname{ind}_g a=\operatorname{ind}_g b$

???+ note "Dokaz"
    1.  $g^{\operatorname{ind}_g(ab)}\equiv ab\equiv g^{\operatorname{ind}_g a}g^{\operatorname{ind}_g b}\equiv g^{\operatorname{ind}_g a+\operatorname{ind}_g b}\pmod m$
    2.  Neka je $x=\operatorname{ind}_{g_1}a$; tada je $a\equiv g_1^x\pmod m$. Neka je još $y=\operatorname{ind}_g g_1$; tada je $g_1\equiv g^y\pmod m$.
    
        Stoga je $a\equiv g^{xy}\pmod m$, tj. $\operatorname{ind}_g a\equiv xy\equiv\operatorname{ind}_{g_1}a \cdot \operatorname{ind}_g g_1\pmod{\varphi(m)}$
    3.  Uočimo da
    
        $$
        \begin{aligned}
            \operatorname{ind}_g a=\operatorname{ind}_g b&\iff \operatorname{ind}_g a\equiv\operatorname{ind}_g b\pmod{\varphi(m)}\\
            &\iff g^{\operatorname{ind}_g a}\equiv g^{\operatorname{ind}_g b}\pmod m\\
            &\iff a\equiv b\pmod m
        \end{aligned}
        $$

## Algoritam baby-step giant-step

Za problem diskretnog logaritma još ne postoji klasični algoritam polinomnog vremena (veličina ulaza problema diskretnog logaritma jest broj bitova ulaznih podataka). U kriptografiji su na tome zasnovani mnogi asimetrični kriptosustavi, npr. [Ed25519](https://en.wikipedia.org/wiki/EdDSA#Ed25519).

Na algoritamskim natjecanjima za rješavanje problema diskretnog logaritma često se koristi BSGS (baby-step giant-step). Formalno, za $a,b,m\in\mathbf{Z}^+$ taj algoritam u vremenu $O(\sqrt{m})$ rješava

$$
a^x \equiv b \pmod m
$$

gdje je $a\perp m$. Rješenje $x$ jednadžbe zadovoljava $0 \le x < m$. (Napomena: $m$ ne mora biti prost.)

### Opis algoritma

Neka je $x = A \left \lceil \sqrt m \right \rceil - B$, gdje je $0\le A,B \le \left \lceil \sqrt m \right \rceil$. Tada je $a^{A\left \lceil \sqrt m \right \rceil -B} \equiv b \pmod m$, a nakon male preinake $a^{A\left \lceil \sqrt m \right \rceil} \equiv ba^B \pmod m$.

Poznati su nam $a,b$, pa možemo najprije izračunati sve vrijednosti $ba^B$ s desne strane jednakosti, iterirajući po $B$, i spremiti ih u `hash`/`map`; zatim redom računamo $a^{A\left \lceil \sqrt m \right \rceil}$, iterirajući po $A$, i tražimo postoji li jednaka vrijednost $ba^B$; tako dobivamo sve $x$, $x=A \left \lceil \sqrt m \right \rceil - B$.

Uočimo da su $A,B$ oba manji od $\left \lceil \sqrt m \right \rceil$, pa je vremenska složenost $\Theta\left  (\sqrt m\right )$; uz `map` dolazi još faktor $\log$.

??? note "Zašto se zahtijeva da su $a$ i $m$ relativno prosti"
    Uočimo da mi zapravo nalazimo $A,B$, pa moramo osigurati da se iz $a^{A\left \lceil \sqrt m \right \rceil} \equiv ba^B \pmod m$ može natrag zaključiti $a^{A\left \lceil \sqrt m \right \rceil -B} \equiv b \pmod m$. Druga se kongruencija dobiva dijeljenjem obiju strana prve s $a^B$, pa mora vrijediti $a^B \perp m$, tj. $a\perp m$.

## Prošireni BSGS algoritam

Za $a,b,m\in\mathbf{Z}^+$ rješavamo

$$
a^x\equiv b\pmod m
$$

gdje $a,m$ ne moraju biti relativno prosti.

Kad je $(a, m)=1$, $a$ ima inverz modulo $m$, pa se može primijeniti BSGS algoritam. Zato ćemo pokušati učiniti ih relativno prostima.

Konkretno, neka je $d_1=(a, m)$. Ako $d_1\nmid b$, izvorna jednadžba nema rješenja. U suprotnom podijelimo jednadžbu s $d_1$ i dobijemo

$$
\frac{a}{d_1}\cdot a^{x-1}\equiv \frac{b}{d_1}\pmod{\frac{m}{d_1}}
$$

Ako $a$ i $\frac{m}{d_1}$ još nisu relativno prosti, dijelimo opet: neka je $d_2=\left(a, \frac{m}{d_1}\right)$. Ako $d_2\nmid \frac{b}{d_1}$, jednadžba nema rješenja; inače dijelimo s $d_2$ i dobivamo

$$
\frac{a^2}{d_1d_2}\cdot a^{x-2}≡\frac{b}{d_1d_2} \pmod{\frac{m}{d_1d_2}}
$$

Na isti način nastavljamo provjeravati sve dok ne bude $a\perp \dfrac{m}{d_1d_2\cdots d_k}$.

Označimo $D=\prod_{i=1}^kd_i$; jednadžba tada poprima oblik:

$$
\frac{a^k}{D}\cdot a^{x-k}\equiv\frac{b}{D} \pmod{\frac{m}{D}}
$$

Budući da je $a\perp\dfrac{m}{D}$, slijedi $\dfrac{a^k}{D}\perp \dfrac{m}{D}$. Tako $\dfrac{a^k}{D}$ ima inverz, pa ga prebacimo na desnu stranu jednadžbe i dobijemo običan BSGS problem; riješimo ga za $x-k$ i dodamo $k$ – to je rješenje izvorne jednadžbe.

Napomena: nije isključeno da je rješenje manje ili jednako $k$, pa prije uklanjanja faktora napravimo iteraciju u $\Theta(k)$ koraka i izravno provjerimo $a^i\equiv b \pmod m$; time taj slučaj izbjegavamo.

## Brzi diskretni logaritam s pretprocesiranjem po rasponu vrijednosti

Vremenska složenost prethodnog BSGS algoritma iznosi $O(\sqrt m)$ po upitu, što je neučinkovito kad je broj upita velik. Ako je modul u svakom upitu isti fiksni prost broj $p$, imamo brz algoritam zasnovan na pretprocesiranju po rasponu vrijednosti.

Već znamo da je $\operatorname{ind}_g(ab)\equiv\operatorname{ind}_g a+\operatorname{ind}_g b\pmod{p-1}$, pa diskretne logaritme BSGS algoritmom možemo računati samo za proste brojeve, a diskretni logaritam složenog broja tom se formulom svodi na zbroj nekoliko već poznatih diskretnih logaritama prostih brojeva. Složenost tada još nije dobra, pa razmotrimo pretprocesiranje samo dijela diskretnih logaritama; konkretno, pretprocesiramo diskretne logaritme od $1$ do $L = \lfloor\sqrt p\rfloor + 1$. Primijetimo da duljina bloka $B$ u BSGS-u sada **ne smije** biti $O(\sqrt{L})$, jer je složenost pretprocesiranja u BSGS-u (umetanje u hash tablicu) $O(B)$, a upita je ukupno $O(\pi(L))$, pa je ukupna vremenska složenost $O\left(B+\dfrac{\pi(L)p}{B}\right)$; optimalno je tek $B=O(\sqrt{\pi(L)p})$. Prema [teoremu o prostim brojevima](./prime.md) $\pi(n)\sim\dfrac{n}{\log n}$, pa se ukupna složenost pretprocesiranja može uravnotežiti na $O\left(\dfrac{p^{3/4}}{\log^{1/2} p}\right)$.

Slijedi kako izračunati odgovor. Pretpostavimo da trenutačno tražimo $\operatorname{ind}_g y$. Ako je $y\le L$, odgovor izravno vraćamo; inače neka je $p=vy+r$, pa je $v=\left\lfloor\dfrac{p}{y}\right\rfloor<L$, $r=p\bmod y$, $y=\dfrac{p-r}{v}$, odakle

$$
\begin{aligned}
\operatorname{ind}_g y &\equiv \operatorname{ind}_g (p-r)-\operatorname{ind}_g v\\
&\equiv \operatorname{ind}_g (-r)-\operatorname{ind}_g v\\
&\equiv \operatorname{ind}_g (p-1)+\operatorname{ind}_g r-\operatorname{ind}_g v \pmod{p-1}.
\end{aligned}
$$

Uočimo da je $\operatorname{ind}_g (p-1)=(p-1)/2$, pa je dovoljno rekurzivno izračunati diskretni logaritam od $r$.

Možemo razmotriti i drugi zapis broja $y$: uočimo da je $p=vy+r=(v+1)y+r-y$, pa je $y=\dfrac{p-r+y}{v+1}$, odakle

$$
\operatorname{ind}_g y\equiv \operatorname{ind}_g (y-r)-\operatorname{ind}_g (v+1) \pmod{p-1}.
$$

Vrijedi $v+1 \le L$, pa je dovoljno rekurzivno izračunati diskretni logaritam od $y-r$.

Kombiniranjem tih dvaju načina računanja imamo $\min\{r,y-r\}\le \dfrac{y}{2}$, pa rekurzivnim računanjem manjeg od njih postižemo složenost upita $O(\log p)$.

Time smo dobili algoritam vremenske složenosti $O\left(\dfrac{p^{3/4}}{\log^{1/2} p}\right)-O(\log p)$.

??? example "[Luogu11175【模板】基于值域预处理的快速离散对数 (predložak: brzi diskretni logaritam s pretprocesiranjem po rasponu vrijednosti)](https://www.luogu.com.cn/problem/P11175)"
    ```cpp
    --8<-- "docs/math/code/discrete-logarithm/discrete-logarithm-1.cpp"
    ```

## Zadaci za vježbu

-   [SPOJ MOD](https://www.spoj.com/problems/MOD/) predložak
-   [SDOI2013 随机数生成器 (Generator slučajnih brojeva)](https://www.luogu.com.cn/problem/P3306)
-   [SGU261 Discrete Roots](https://codeforces.com/problemsets/acmsguru/problem/99999/261) predložak
-   [SDOI2011 计算器 (Kalkulator)](https://loj.ac/problem/10214) predložak
-   [Luogu4195【模板】exBSGS/Spoj3105 Mod](https://www.luogu.com.cn/problem/P4195) predložak
-   [Codeforces - Lunar New Year and a Recursive Sequence](https://codeforces.com/contest/1106/problem/F)
-   [LOJ6542 离散对数 (Diskretni logaritam)](https://loj.ac/problem/6542) metoda index calculus, nije predložak

**Dio sadržaja i koda na ovoj stranici preveden je iz blog-zapisa [Дискретное извлечение корня](http://e-maxx.ru/algo/discrete_root) i njegova engleskog prijevoda [Discrete Root](https://cp-algorithms.com/algebra/discrete-root.html). Ruska je inačica objavljena pod licencijom Public Domain + Leave a Link, a engleska pod licencijom CC-BY-SA 4.0.**

## Literatura

1.  [Discrete logarithm - Wikipedia](https://en.wikipedia.org/wiki/Discrete_logarithm)
2.  潘承洞, 潘承彪. 初等数论 (Elementarna teorija brojeva).
3.  冯克勤. 初等数论及其应用 (Elementarna teorija brojeva i njezine primjene).
