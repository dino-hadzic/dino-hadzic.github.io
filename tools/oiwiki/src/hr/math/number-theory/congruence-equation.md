---
title: Kongruencije
---

## Definicija

???+ abstract "Kongruencija"
    Za prirodan broj $m$ i polinom jedne varijable s cjelobrojnim koeficijentima $f(x)=\sum_{i=0}^n a_ix^i$, gdje je nepoznanica $x\in\mathbf{Z}_m$, jednadžba oblika
    
    $$
    f(x)\equiv 0\pmod m\tag{1}
    $$
    
    naziva se **kongruencija** (congruence equation) jedne nepoznanice $x$ po modulu $m$.
    
    Ako je $a_n\not\equiv 0\pmod m$, gornja se jednadžba naziva kongruencijom $n$-tog stupnja.
    
    Analogno se definira sustav kongruencija.

O kongruencijama prvog stupnja i njihovim sustavima vidi [Linearne kongruencije](./linear-equation.md) i [Kineski teorem o ostatcima](./crt.md).

U ovom se članku najprije proučavaju rješivost kongruencija i struktura skupa rješenja, a zatim se ukratko opisuju metode rješavanja kongruencija višeg stupnja.

Prema [kineskom teoremu o ostatcima](./crt.md), rješavanje kongruencije po složenom modulu $m$ može se svesti na rješavanje po modulu koji je potencija prostog broja. Stoga u nastavku predstavljamo samo teoriju kongruencija po modulu koji je potencija prostog broja i kongruencija po prostom modulu.

## Kongruencije po modulu koji je potencija prostog broja

U nastavku pretpostavljamo da je modul $m=p^e~(p\in\mathbf{P},~e\in\mathbf{Z}_{>1})$.

Uočimo: ako je $x_0$ rješenje jednadžbe

$$
f(x)\equiv 0\pmod{p^e}
$$

tada je $x_0$ rješenje jednadžbe

$$
f(x)\equiv 0\pmod{p^{e-1}}
$$

To nas potiče da pokušamo iz rješenja po nižoj potenciji modula konstruirati rješenja po višoj potenciji. Vrijedi sljedeći teorem:

???+ note "Teorem 1 (Henselova lema)"
    Za prost broj $p$ i cijeli broj $e>1$ uzmimo polinom s cjelobrojnim koeficijentima $f(x)=\sum_{i=0}^na_ix^i~(p^e\nmid a_n)$ i neka je $f'(x)=\sum_{i=1}^nia_ix^{i-1}$ njegova derivacija. Neka je $x_0$ rješenje jednadžbe
    
    $$
    f(x)\equiv 0\pmod{p^{e-1}}\tag{2}
    $$
    
    Tada:
    
    1.  Ako je $f'(x_0)\not\equiv 0\pmod p$, postoji cijeli broj $t$ takav da je
    
        $$
        x=x_0+p^{e-1}t \tag{3}
        $$
    
        rješenje jednadžbe
    
        $$
        f(x)\equiv 0\pmod{p^e} \tag{4}
        $$
    
    2.  Ako je $f'(x_0)\equiv 0\pmod p$ i $f(x_0)\equiv 0\pmod{p^e}$, tada su za $t=0,1,\dots,p-1$ svi $x$ određeni formulom $(3)$ rješenja jednadžbe $(4)$.
    3.  Ako je $f'(x_0)\equiv 0\pmod p$ i $f(x_0)\not\equiv 0\pmod{p^e}$, tada se formulom $(3)$ ne može konstruirati rješenje jednadžbe $(4)$.

???+ note "Dokaz"
    Pretpostavimo da je $(3)$ rješenje jednadžbe $(4)$, tj.
    
    $$
    f(x_0+p^{e-1}t)\equiv 0\pmod{p^e}
    $$
    
    Sređivanjem dobivamo
    
    $$
    f(x_0)+p^{e-1}tf'(x_0)\equiv 0\pmod{p^e}
    $$
    
    pa je
    
    $$
    tf'(x_0)\equiv -\frac{f(x_0)}{p^{e-1}}\pmod p\tag{5}
    $$
    
    1.  Ako je $f'(x_0)\not\equiv 0\pmod p$, jednadžba $(5)$ po $t$ ima jedinstveno rješenje $t_0$; uvrštavanjem u $(3)$ provjerava se da je to rješenje jednadžbe $(4)$.
    2.  Ako je $f'(x_0)\equiv 0\pmod p$ i $f(x_0)\equiv 0\pmod{p^e}$, svaki $t$ zadovoljava jednadžbu $(5)$; uvrštavanjem u $(3)$ provjerava se da su svi oni rješenja jednadžbe $(4)$.
    3.  Ako je $f'(x_0)\equiv 0\pmod p$ i $f(x_0)\not\equiv 0\pmod{p^e}$, jednadžba $(5)$ nema rješenja, pa se formulom $(3)$ ne može konstruirati rješenje jednadžbe $(4)$.

Odatle slijedi korolar:

???+ note "Korolar 1"
    Za $p$, $e$, $f(x)$, $x_0$ iz teorema 1:
    
    1.  Ako je $s$ rješenje jednadžbe $f(x)\equiv 0\pmod p$ i $f'(s)\not\equiv 0\pmod p$, postoji $x_s\in\mathbf{Z}_{p^e}$, $x_s\equiv s\pmod p$, takav da je $x_s$ rješenje jednadžbe $(4)$.
    2.  Ako jednadžbe $f(x)\equiv 0\pmod p$ i $f'(x)\equiv 0\pmod p$ nemaju zajedničko rješenje, jednadžba $(4)$ i jednadžba $f(x)\equiv 0\pmod p$ imaju jednak broj rješenja.

Time kongruencije po modulu koji je potencija prostog broja možemo svesti na slučaj kongruencija po prostom modulu.

## Kongruencije po prostom modulu

U nastavku neka je $p\in\mathbf{P}$, $f(x)=\sum_{i=0}^na_ix^i$ polinom s cjelobrojnim koeficijentima, gdje je $p\nmid a_n$, i $x\in\mathbf{Z}_p$.

???+ note "Teorem 2"
    Ako jednadžba
    
    $$
    f(x)\equiv 0\pmod p\tag{6}
    $$
    
    ima $k$ različitih rješenja $x_1,x_2,\dots,x_k~(k\leq n)$, tada je
    
    $$
    f(x)\equiv g(x)\prod_{i=1}^k(x-x_i)\pmod p,
    $$
    
    gdje je $\deg g=n-k$ i $[x^{n-k}]g(x)=a_n$.

???+ note "Dokaz"
    Matematičkom indukcijom po $k$.
    
    -   Za $k=1$ dijeljenjem polinoma s ostatkom dobivamo $f(x)=(x-x_1)g(x)+r$, gdje je $r\in\mathbf{Z}$.
    
        Iz $f(x_1)\equiv 0\pmod p$ slijedi $r\equiv 0\pmod p$, pa je $f(x)\equiv(x-x_1)g(x)\pmod p$.
    -   Pretpostavimo da tvrdnja vrijedi za $k-1$ ($k>1$) i neka sada $f(x)$ ima $k$ različitih rješenja $x_1,x_2,\dots,x_k$; tada je $f(x)\equiv(x-x_1)h(x)\pmod p$, pa vrijedi
    
        $$
        (\forall i=2,3,\dots,k),~~0\equiv f(x_i)\equiv (x_i-x_1)h(x_i)\pmod p
        $$
    
        Stoga $h(x)$ ima $k-1$ različitih rješenja $x_2,x_3,\dots,x_k$, pa po pretpostavci indukcije vrijedi
    
        $$
        h(x)\equiv g(x)\prod_{i=2}^k(x-x_i)\pmod p
        $$
    
        gdje je $\deg g=n-k$ i $[x^{n-k}]g(x)=a_n$.
    
        Time je tvrdnja dokazana.

???+ note "Korolar 2"
    Za prost broj $p$:
    
    -   $(\forall x\in\mathbf{Z}),~~x^{p-1}-1 \equiv \prod_{i=1}^{p-1}(x-i)\pmod p$.
    -   ([Wilsonov teorem](./factorial.md#wilsonov-teorem)) $(p-1)! \equiv -1 \pmod p$.

???+ note "Teorem 3 (Lagrangeov teorem)"
    Jednadžba $(6)$ ima najviše $n$ različitih rješenja.

???+ note "Dokaz"
    Pretpostavimo da $f(x)$ ima $n+1$ različitih rješenja $x_1,x_2,\dots,x_{n+1}$; tada prema teoremu 2 za $x_1,x_2,\dots,x_n$ vrijedi
    
    $$
    f(x)\equiv a_n\prod_{i=1}^n(x-x_i)\pmod p
    $$
    
    Stavimo $x=x_{n+1}$; tada je
    
    $$
    0\equiv f(x_{n+1})\equiv a_n\prod_{i=1}^n(x_{n+1}-x_i)\pmod p
    $$
    
    a desna strana očito nije višekratnik broja $p$, pa je pretpostavka kontradiktorna.

???+ note "Korolar 3"
    Ako kongruencija $\sum_{i=0}^nb_ix^i\equiv 0\pmod p$ ima više od $n$ rješenja, tada je
    
    $$
    (\forall i=0,1,\dots,n),~~p\mid b_i.
    $$

???+ note "Teorem 4"
    Ako broj rješenja jednadžbe $(6)$ nije $p$, tada nužno postoji polinom s cjelobrojnim koeficijentima $r(x)$ s $\deg r<p$ takav da $f(x)\equiv 0\pmod p$ i $r(x)\equiv 0\pmod p$ imaju isti skup rješenja.

???+ note "Dokaz"
    Bez smanjenja općenitosti neka je $n\geq p$; podijelimo $f(x)$ s ostatkom:
    
    $$
    f(x)=g(x)\left(x^p-x\right)+r(x)
    $$
    
    gdje je $\deg r<p$.
    
    Prema [malom Fermatovu teoremu](./fermat.md) za svaki cijeli broj $x$ vrijedi $x^p\equiv x\pmod p$, pa
    
    -   ako je $r(x)\equiv 0\pmod p$, prema korolaru 2 $f(x)$ ima $p$ različitih rješenja;
    -   ako je $r(x)\not\equiv 0\pmod p$, iz $f(x)\equiv r(x)\pmod p$ slijedi da $f(x)$ i $r(x)$ imaju isti skup rješenja.

Pomoću ovog teorema možemo sniziti stupanj kongruencije.

???+ note "Teorem 5"
    Neka je $n\leq p$. Jednadžba
    
    $$
    x^n+\sum_{i=0}^{n-1}a_ix^i\equiv 0\pmod p\tag{7}
    $$
    
    ima $n$ rješenja ako i samo ako postoje polinomi s cjelobrojnim koeficijentima $q(x)$, $r(x)~(\deg r < n)$ takvi da je
    
    $$
    x^p-x=f(x)q(x)+pr(x). \tag{8}
    $$

???+ note "Dokaz"
    -   Nužnost: dijeljenjem polinoma znamo da postoje polinomi s cjelobrojnim koeficijentima $q(x)$, $r_1(x)~(\deg r_1 < n)$ takvi da je
    
        $$
        x^p-x=f(x)q(x)+r_1(x).
        $$
    
        Ako jednadžba $(7)$ ima $n$ rješenja, tada i $r_1\equiv 0\pmod p$ ima tih istih $n$ rješenja, pa prema korolaru 3 postoji polinom s cjelobrojnim koeficijentima $r(x)$ takav da je $r_1(x)=pr(x)$; time je tvrdnja dokazana.
    -   Dovoljnost: ako vrijedi $(8)$, prema [malom Fermatovu teoremu](./fermat.md) za svaki cijeli broj $x$ vrijedi
    
        $$
        0\equiv x^p-x\equiv f(x)q(x)\pmod p.
        $$
    
        Dakle, jednadžba $f(x)q(x)\equiv 0\pmod p$ ima $p$ rješenja.
    
        Neka je $s$ broj rješenja jednadžbe $(7)$; prema Lagrangeovu teoremu $s\leq n$.
    
        Nadalje, budući da je $\deg q=p-n$, prema Lagrangeovu teoremu broj rješenja jednadžbe $q(x)\equiv 0\pmod p$ ne premašuje $p-n$, a skup rješenja jednadžbe $f(x)q(x)\equiv 0\pmod p$ unija je skupa rješenja jednadžbe $f(x)\equiv 0\pmod p$ i skupa rješenja jednadžbe $q(x)\equiv 0\pmod p$, pa je $s+(p-n)\geq p$, tj. $s\geq n$.
    
        Stoga je $s=n$.

Za polinome koji nisu normirani, budući da je $\mathbf{Z}_p$ polje, mogu se svesti na normirane polinome, pa se teorem može primijeniti.

???+ note "Teorem 6"
    Neka je $n\mid p-1$ i $p\nmid a$. Jednadžba
    
    $$
    x^n\equiv a\pmod p\tag{9}
    $$
    
    ima rješenje ako i samo ako je
    
    $$
    a^{\frac{p-1}{n}}\equiv 1\pmod p.
    $$
    
    Štoviše, ako $(9)$ ima rješenje, broj rješenja iznosi $n$.

???+ note "Napomena"
    Konkretna struktura skupa rješenja jednadžbe $(9)$ opisana je u članku [Ostatci k-tog reda](./residue.md).

???+ note "Dokaz"
    -   Nužnost: ako jednadžba $(9)$ ima rješenje $x_0$, tada je
    
        $$
        a^{\frac{p-1}{n}}\equiv {\left(x_0^n\right)}^{\frac{p-1}{n}}\equiv 1\pmod p
        $$
    -   Dovoljnost: ako je $a^{\frac{p-1}{n}}\equiv 1\pmod p$, tada je
    
        $$
        \begin{aligned}
            x^p-x&=x\left(x^{p-1}-1\right)\\
            &=x\left(\left(x^n\right)^{\frac{p-1}{n}}-a^{\frac{p-1}{n}}+a^{\frac{p-1}{n}}-1\right)\\
            &=\left(x^n-a\right)P(x)+x\left(a^{\frac{p-1}{n}}-1\right)\\
        \end{aligned}
        $$
    
        gdje je $P(x)$ neki polinom s cjelobrojnim koeficijentima, pa prema teoremu 5 jednadžba $(9)$ ima $n$ rješenja.

## Metode rješavanja kongruencija (i sustava) višeg stupnja

Najprije pomoću [kineskog teorema o ostatcima](./crt.md) rješavanje **sustava kongruencija** svodimo na rješavanje **kongruencija**, a rješavanje kongruencije po **složenom** modulu $m$ na rješavanje kongruencija po modulu koji je **potencija prostog broja**. Zatim pomoću [teorema 1](#kongruencije-po-modulu-koji-je-potencija-prostog-broja) rješavanje kongruencije po modulu koji je **potencija prostog broja** svodimo na rješavanje kongruencije po **prostom** modulu.

Uzimajući u obzir teoreme o kongruencijama po prostom modulu, dovoljno je razmotriti rješavanje jednadžbe

$$
x^n+\sum_{i=0}^{n-1}a_ix^i\equiv 0\pmod p
$$

gdje je $p$ prost broj, a $n<p$.

Zamjenom $x$ s $x-\dfrac{a_{n-1}}{n}$ možemo ukloniti član $x^{n-1}$, pa je dovoljno razmotriti rješavanje jednadžbe

$$
x^n+\sum_{i=0}^{n-2}a_ix^i\equiv 0\pmod p\tag{10}
$$

gdje je $p$ prost broj, a $n<p$.

-   Za $n=1$ postupak je opisan u članku [Linearne kongruencije](./linear-equation.md).
-   Za $n=2$ postupak je opisan u članku [Kvadratni ostatci](./quad-residue.md).
-   Ako se jednadžba $(10)$ može svesti na oblik

    $$
    x^n\equiv a\pmod p,
    $$

    postupak je opisan u članku [Ostatci k-tog reda](./residue.md).

## Literatura

1.  [Congruence Equation -- from Wolfram MathWorld](https://mathworld.wolfram.com/CongruenceEquation.html)
2.  [Lagrange's theorem (number theory) - Wikipedia](https://en.wikipedia.org/wiki/Lagrange%27s_theorem_%28number_theory%29)
3.  潘承洞, 潘承彪 (Pan Chengdong, Pan Chengbiao). 初等数论 (Elementarna teorija brojeva).
4.  冯克勤 (Feng Keqin). 初等数论及其应用 (Elementarna teorija brojeva i njezine primjene).
5.  闵嗣鹤, 严士健 (Min Sihe, Yan Shijian). 初等数论 (Elementarna teorija brojeva).
