---
title: Dirichletova konvolucija
---

Ovaj članak predstavlja Dirichletovu konvoluciju i Dirichletove funkcije izvodnice.

## Dirichletova konvolucija

**Dirichletova konvolucija** (Dirichlet convolution) aritmetičkih funkcija $f(n)$ i $g(n)$, u oznaci $f \ast g$, definira se kao aritmetička funkcija

$$
(f \ast g)(n) = \sum_{k\mid n}f(k)g\left(\dfrac{n}{k}\right) = \sum_{k\ell=n}f(k)g(\ell).
$$

Dirichletova konvolucija važna je operacija na aritmetičkim funkcijama. Mnoga svojstva aritmetičkih funkcija otkrivaju se upravo pomoću te operacije.

???+ example "Primjer"
    1.  Jedinična funkcija $\varepsilon$ Dirichletova je konvolucija Möbiusove funkcije $\mu$ i konstantne funkcije $1$:
    
        $$
        \varepsilon=\mu \ast 1 \iff\varepsilon(n)=\sum_{d\mid n}\mu(d).
        $$
    
    2.  Funkcija broja djelitelja $\tau$ Dirichletova je konvolucija konstantne funkcije $1$ sa samom sobom:
    
        $$
        \tau=1 \ast 1 \iff \tau(n)=\sum_{d\mid n}1.
        $$
    
    3.  Funkcija zbroja djelitelja $\sigma$ Dirichletova je konvolucija identitete $\mathrm{id}$ i konstantne funkcije $1$:
    
        $$
        \sigma=\mathrm{id} \ast 1 \iff\sigma(n)=\sum_{d\mid n}d.
        $$
    
    4.  Eulerova funkcija $\varphi$ Dirichletova je konvolucija identitete $\mathrm{id}$ i Möbiusove funkcije $\mu$:
    
        $$
        \varphi=\mathrm{id}\ast \mu \iff\varphi(n)=\sum_{d\mid n}d\cdot\mu\left(\frac{n}{d}\right).
        $$

[Möbiusova inverzija](./mobius.md) upravo je preoblikovanje identiteta među aritmetičkim funkcijama pomoću $\varepsilon=\mu \ast 1$.

### Svojstva

Dirichletova konvolucija ima niz algebarskih svojstava.

???+ note "Teorem"
    Neka su $f,g,h$ aritmetičke funkcije. Tada vrijedi:
    
    1.  **Komutativnost**: $f\ast g=g\ast f$.
    2.  **Asocijativnost**: $(f\ast g)\ast h=f\ast(g\ast h)$.
    3.  **Distributivnost**: $(f+g)\ast h = f\ast h + g\ast h$.
    4.  **Neutralni element**: $f\ast\varepsilon = \varepsilon \ast f = f$, gdje je $\varepsilon(n) = [n=1]$ neutralni element konvolucije, a $[\cdot]$ Iversonova zagrada.
    5.  **Inverz**: $g$ takav da je $f\ast g=g\ast f=\varepsilon$ postoji ako i samo ako je $f(1)\neq 0$, i $g$ se naziva **Dirichletov inverz** (Dirichlet inverse) od $f$ te se može označiti s $f^{-1}$. Štoviše, inverz $g$ zadovoljava rekurzivnu formulu
    
        $$
        g(n) = \dfrac{\varepsilon(n) - \sum_{k\ell = n,~k\neq 1}f(k)g(\ell)}{f(1)}.
        $$

??? note "Dokaz"
    Za provjeru komutativnosti izravnim računom dobivamo
    
    $$
    (f\ast g)(n) = \sum_{k\ell=n}f(k)g(\ell) = (g\ast f)(n).
    $$
    
    Za provjeru asocijativnosti izravnim računom dobivamo
    
    $$
    ((f\ast g)\ast h)(n) = \sum_{k\ell m = n}f(k)g(\ell)h(m) = (f\ast (g\ast h))(n).
    $$
    
    Za provjeru distributivnosti izravnim računom dobivamo
    
    $$
    \begin{aligned}
    ((f+g)\ast h)(n) &= \sum_{k\ell = n}(f(k) + g(k))h(\ell) \\
    &= \sum_{k\ell=n}f(k)h(\ell) + \sum_{k\ell=n}g(k)h(\ell) = (f\ast h+g\ast h)(n).
    \end{aligned}
    $$
    
    Za provjeru da je $\varepsilon(n)$ neutralni element izravnim računom dobivamo
    
    $$
    (f\ast\varepsilon)(n) = \sum_{k\ell = n}f(k)\varepsilon(\ell) = f(n).
    $$
    
    Druga jednakost vrijedi jer $\varepsilon(\ell)$ poprima vrijednost različitu od nule samo za $\ell=1$, tj. $k=n$.
    
    Naposljetku treba dokazati da $f^{-1}$ postoji ako i samo ako je $f(1)\neq 0$. Za proizvoljnu $f$ pretpostavimo da postoji $g$ takva da je $f\ast g=\varepsilon$. To znači
    
    $$
    (f\ast g)(n) = \sum_{k\ell = n}f(k)g(\ell) = \varepsilon(n).
    $$
    
    To je zapravo sustav jednadžbi za vrijednosti $g(n)$ iz kojeg se $g(n)$ može izravno izračunati. Posebno, za $n=1$ jednadžba postaje $f(1)g(1)=1$, pa postojanje $g$ zahtijeva barem $f(1)\neq 0$. A čim je $f(1)\neq 0$, izravno se dobiva
    
    $$
    g(n) = \dfrac{\varepsilon(n) - \sum_{k\ell = n,~k\neq 1}f(k)g(\ell)}{f(1)}.
    $$
    
    To se može upotrijebiti za rekurzivno računanje vrijednosti $g(n)$. Stoga inverz $g$ postoji ako i samo ako je $f(1)\neq 0$.

Jezikom apstraktne algebre, ova algebarska svojstva pokazuju da sve aritmetičke funkcije s (točkovnim) zbrajanjem i Dirichletovom konvolucijom čine [komutativni prsten](../algebra/basic.md#环), a njegovi invertibilni elementi upravo su funkcije koje u $n=1$ poprimaju vrijednost različitu od nule. Taj se prsten naziva **Dirichletov prsten** (Dirichlet ring).

Multiplikativne funkcije poseban su razred aritmetičkih funkcija. Zatvorene su i na Dirichletovu konvoluciju i na Dirichletov inverz.

???+ note "Teorem"
    Neka su $f,g$ multiplikativne funkcije. Tada je i $f\ast g$ multiplikativna funkcija. Štoviše, inverz $f^{-1}$ sigurno postoji i također je multiplikativna funkcija.

??? note "Dokaz"
    Za prvu tvrdnju neka je $h=f\ast g$; izravnom provjerom, za $n_1\perp n_2$ vrijedi
    
    $$
    \begin{aligned}
    h(n_1)h(n_2) &= \left(\sum_{k_1\ell_1=n_1}f(k_1)g(\ell_1)\right)\left(\sum_{k_2\ell_2=n_2}f(k_2)g(\ell_2)\right)\\
    &= \sum_{k_1\ell_1=n_1,~k_2\ell_2=n_2}f(k_1)f(k_2)g(\ell_1)g(\ell_2)\\
    &= \sum_{k\ell = n_1n_2}f(k)g(\ell) \\
    &= h(n_1n_2).
    \end{aligned}
    $$
    
    Pritom treća jednakost koristi multiplikativnost od $f,g$, a logika promjene redoslijeda sumiranja jest sljedeća: kada $k$ prolazi djeliteljima od $n_1n_2$, prosti faktori od $k$ mogu se podijeliti u dvije skupine prema tome jesu li prosti faktori od $n_1$ ili od $n_2$; množenjem prostih faktora svake skupine (s višestrukostima) dobivaju se $k_1$ i $k_2$, koji redom prolaze djeliteljima od $n_1$ i $n_2$; obratno, iz djelitelja $k_1$ i $k_2$ od $n_1$ i $n_2$ uvijek se dobiva djelitelj $k=k_1k_2$ od $n_1n_2$.
    
    Za drugu tvrdnju neka je $g=f^{-1}$ i primijenimo matematičku indukciju. Najprije, $g(1)=1/f(1)=1$. Rekurzivna formula za inverz tada se može zapisati kao
    
    $$
    g(n) = \varepsilon(n) - \sum_{k\ell = n,~k\neq 1} f(k)g(\ell).
    $$
    
    Stoga za $n_1\perp n_2$ i $n_1n_2 > 1$ vrijedi
    
    $$
    \begin{aligned}
    g(n_1n_2) &= -\sum_{k\ell=n_1n_2,~k\neq 1}f(k)g(\ell) \\
    &= -\sum_{k_1\ell_1=n_1,~k_2\ell_2=n_2,~k_1k_2\neq 1}f(k_1)f(k_2)g(\ell_1)g(\ell_2)\\
    &= f(1)f(1)g(n_1)g(n_2) - \sum_{k_1\ell_1=n_1,~k_2\ell_2=n_2}f(k_1)f(k_2)g(\ell_1)g(\ell_2)\\
    &= g(n_1)g(n_2) - \left(\sum_{k_1\ell_1=n_1}f(k_1)g(\ell_1)\right)\left(\sum_{k_2\ell_2=n_2}f(k_2)g(\ell_2)\right) \\
    &= g(n_1)g(n_2) - \varepsilon(n_1)\varepsilon(n_2)\\
    &= g(n_1)g(n_2).
    \end{aligned}
    $$
    
    Pritom druga jednakost koristi pretpostavku indukcije, tj. da za $\ell_1\ell_2 < n_1n_2$ i $\ell_1\perp\ell_2$ vrijedi $g(\ell_1\ell_2)=g(\ell_1)g(\ell_2)$.

Jezikom apstraktne algebre, sve multiplikativne funkcije s Dirichletovom konvolucijom čine [podgrupu](../algebra/group-theory.md#子群) multiplikativne grupe Dirichletova prstena.

Još su posebnije potpuno multiplikativne funkcije.

???+ note "Teorem"
    Neka je $\alpha$ potpuno multiplikativna funkcija, a $f,g$ aritmetičke funkcije. Tada vrijedi:
    
    1.  Distributivnost: $(\alpha f)\ast(\alpha g) = \alpha\cdot(f\ast g)$.
    2.  Inverz: $(\alpha f)^{-1}=\alpha f^{-1}$, čim $f^{-1}$ postoji.
    3.  Multiplikativna funkcija $f$ potpuno je multiplikativna ako i samo ako je $f^{-1}=\mu f$, gdje je $\mu$ [Möbiusova funkcija](./mobius.md#möbiusova-funkcija).

??? note "Dokaz"
    Za prvu tvrdnju izravnom provjerom dobivamo
    
    $$
    \begin{aligned}
    ((\alpha f)\ast(\alpha g))(n) &= \sum_{k\ell = n}(\alpha f)(k)(\alpha g)(\ell) \\
    &= \sum_{k\ell = n}\alpha(k)f(k)\alpha(\ell)g(\ell) \\
    &= \sum_{k\ell = n}\alpha(n)f(k)g(\ell) \\
    &= \alpha(n)(f\ast g)(n).
    \end{aligned}
    $$
    
    Pritom treća jednakost koristi svojstvo potpuno multiplikativne funkcije: $\alpha(n)=\alpha(k)\alpha(\ell)$ vrijedi za sve $n=k\ell$.
    
    Za drugu tvrdnju, prema prvoj vrijedi
    
    $$
    (\alpha f)\ast(\alpha f^{-1}) = \alpha(f\ast f^{-1}) = \alpha\varepsilon = \varepsilon.
    $$
    
    Pritom posljednja jednakost koristi samo $\alpha(1)=1$. Prema definiciji inverza, $(\alpha f)^{-1}=\alpha f^{-1}$.
    
    Za treću tvrdnju, prema drugoj tvrdnji i $1^{-1}=\mu$, ako je $f$ potpuno multiplikativna funkcija, onda je
    
    $$
    f^{-1} = (1f)^{-1} = 1^{-1}\cdot f = \mu f.
    $$
    
    Pritom je $1$ konstantna funkcija. Obratno, ako je $f$ multiplikativna funkcija i $f^{-1}=\mu f$, dovoljno je dokazati da za sve proste brojeve $p$ i $e\in\mathbf N_+$ vrijedi $f(p^e)=f(p)^e$ kako bi se dokazalo da je $f$ potpuno multiplikativna. U tu svrhu primijenimo matematičku indukciju po $e\in\mathbf N_+$. U bazi $e=1$ tvrdnja očito vrijedi. Za proizvoljan $e > 1$, primjenom rekurzivne formule za inverz dobivamo
    
    $$
    \begin{aligned}
    f^{-1}(p^e) &= -\sum_{i=1}^{e}f(p^i)f^{-1}(p^{e-i}) \\
    &= -\sum_{i=1}^{e}f(p^i)\mu(p^{e-i})f(p^{e-i})\\
    &= -f(p^e)f(1)\mu(1) - f(p^{e-1})\mu(p)f(p)\\
    &= -f(p^e) + f(p)^e.
    \end{aligned}
    $$
    
    Pritom posljednja jednakost koristi pretpostavku indukcije $f(p^{e-1})=f(p)^{e-1}$. Primjenom $f^{-1}=\mu f$ dobivamo
    
    $$
    f^{-1}(p^e) = \mu(p^e)f(p^e) = 0.
    $$
    
    Uvrštavanjem u prethodni izraz dobivamo
    
    $$
    f(p^e) = f(p)^e.
    $$
    
    Time je korak indukcije dokazan, a time i izvorna tvrdnja.

Jezikom apstraktne algebre, ako je $\alpha$ potpuno multiplikativna funkcija, preslikavanje $f\mapsto \alpha f$ jest [endomorfizam](../algebra/ring-theory.md#理想) Dirichletova prstena.

## Dirichletova funkcija izvodnica

S Dirichletovom konvolucijom usko je povezana Dirichletova funkcija izvodnica.

**Dirichletova funkcija izvodnica** (Dirichlet series generating function, DGF) pridružena aritmetičkoj funkciji $f(n)$ – odnosno nizu $\{f(n)\}$ – definira se kao formalni Dirichletov red (formal Dirichlet series):

$$
F(s) = \sum_{n=1}^{\infty}\dfrac{f(n)}{n^s}.
$$

Ovdje je $s$ formalna varijabla. Kod uobičajenih Dirichletovih funkcija izvodnica $s$ se često može promatrati kao kompleksna varijabla i zatim proučavati analitička svojstva Dirichletovih redova, no to izlazi iz okvira algoritamskih natjecanja.

Umnožak Dirichletovih funkcija izvodnica odgovara Dirichletovoj konvoluciji pripadnih aritmetičkih funkcija:

???+ note "Teorem"
    Za aritmetičke funkcije $f,g$ i njihove Dirichletove funkcije izvodnice $F,G$, funkcija izvodnica njihove Dirichletove konvolucije $f\ast g$ jednaka je $F\cdot G$.

??? note "Dokaz"
    Izravna provjera:
    
    $$
    \begin{aligned}
    F(s)G(s) &= \left(\sum_{k=1}^\infty\dfrac{f(k)}{k^s}\right)\left(\sum_{\ell=1}^\infty\dfrac{g(\ell)}{\ell^s}\right)= \sum_{k=1}^\infty\sum_{\ell=1}^\infty\dfrac{f(k)g(\ell)}{(k\ell)^s}\\
    &= \sum_{n=1}^{\infty}\dfrac{\sum_{k\ell = n}f(k)g(\ell)}{n^s} = \sum_{n=1}^\infty\dfrac{(f\ast g)(n)}{n^s}.
    \end{aligned}
    $$

Koristeći vezu između Dirichletove konvolucije i umnoška Dirichletovih funkcija izvodnica, svojstva Dirichletove konvolucije mogu se razumjeti iz perspektive Dirichletovih funkcija izvodnica. Budući da množenje formalnih Dirichletovih redova zadovoljava komutativnost, asocijativnost i distributivnost prema zbrajanju, Dirichletova konvolucija aritmetičkih funkcija zadovoljava ista algebarska svojstva.

### Eulerov produkt

Posebnost multiplikativnih funkcija odražava se i na Dirichletovim funkcijama izvodnicama. Zbog [teorema o jedinstvenoj faktorizaciji](./basic.md#算术基本定理) cijelih brojeva, funkcija izvodnica $F(s)$ multiplikativne funkcije $f(n)$ može se zapisati u sljedećem obliku:

$$
\begin{aligned}
F(s) &= \sum_{n=1}^{\infty}\dfrac{f(n)}{n^s} = \sum_{n=1}^{\infty}\prod_{p\in\mathbf P}\dfrac{f(p^{\nu_p(n)})}{p^{\nu_p(n)s}} = \prod_{p\in\mathbf P}\sum_{e=0}^{\infty}\dfrac{f(p^e)}{p^{es}}\\
&= \prod_{p\in\mathbf P}\left(1 + \dfrac{f(p)}{p^s} + \dfrac{f(p^2)}{p^{2s}} + \dfrac{f(p^3)}{p^{3s}} + \cdots\right).
\end{aligned}
$$

Pritom $\nu_p(n)$ označava eksponent od $p$ u rastavu broja $n$ na proste faktore. To znači da se $F(s)$ može rastaviti na umnožak faktora $F_p(s)=\sum_{e=0}^{\infty}f(p^e)p^{-es}$, pri čemu aritmetička funkcija koja odgovara svakom $F_p(s)$ može biti različita od nule samo na potencijama od $p$. Taj se beskonačni umnožak naziva i **Eulerov produkt** (Euler product). Ako se i $F(s)$ i $G(s)$ mogu rastaviti u takav oblik, onda može i njihov umnožak; prevedeno na aritmetičke funkcije, to znači da je Dirichletova konvolucija multiplikativnih funkcija ponovno multiplikativna funkcija.

Nadalje, ako je $f(n)$ k tome potpuno multiplikativna funkcija, onda je $f(p^e)=f(p)^e$ pa se gornji izraz može dodatno pojednostavniti:

$$
F(s) = \prod_{p\in\mathbf P}\sum_{e=0}^{\infty}\dfrac{f(p)^e}{p^{es}} = \prod_{p\in\mathbf P}\left(1-\dfrac{f(p)}{p^s}\right)^{-1}.
$$

Za razliku od multiplikativnih funkcija, oblik Dirichletove funkcije izvodnice potpuno multiplikativne funkcije nije zatvoren na množenje; stoga Dirichletova konvolucija i Dirichletov inverz potpuno multiplikativnih funkcija ne moraju biti potpuno multiplikativne funkcije, ali su sigurno multiplikativne.

???+ example "Primjer"
    1.  Jedinična funkcija $\varepsilon(n)$ potpuno je multiplikativna funkcija. Njezina Dirichletova funkcija izvodnica konstantna je funkcija neodređenice $s$
    
        $$
        E(s) = \sum_{n=1}^{\infty}\dfrac{\varepsilon(n)}{n^s} = 1.
        $$
    
    2.  Konstantna funkcija $1(n)$ potpuno je multiplikativna funkcija. Njezina Dirichletova funkcija izvodnica Riemannova je zeta-funkcija ζ
    
        $$
        I(s) = \sum_{n=1}^{\infty}\dfrac{1}{n^s} = \prod_{p\in\mathbf P}\dfrac{1}{1-p^{-s}} = \zeta(s).
        $$
    
    3.  Möbiusova funkcija $\mu(n)$ Dirichletov je inverz konstantne funkcije. Njezina Dirichletova funkcija izvodnica recipročna je vrijednost od $\zeta(s)$:
    
        $$
        M(s) = \sum_{n=1}^{\infty}\dfrac{\mu(n)}{n^s} = \prod_{p\in\mathbf P}(1-p^{-s}) = \dfrac{1}{\zeta(s)}.
        $$
    
    4.  Potencija $\operatorname{id}_k(n)=n^k$ potpuno je multiplikativna funkcija. Posebno, za $k=0$ to je konstantna funkcija, a za $k=1$ identiteta. Njezina Dirichletova funkcija izvodnica jest
    
        $$
        I_k(s) = \sum_{n=1}^{\infty}\dfrac{n^k}{n^s} = \prod_{p\in\mathbf P}\dfrac{1}{1-p^{k-s}} = \zeta(s-k).
        $$
    
    5.  Eulerova funkcija $\varphi(n)$ multiplikativna je funkcija. Njezina Dirichletova funkcija izvodnica jest
    
        $$
        \begin{aligned}
        \Phi(s) &= \prod_{p\in\mathbf P}\left(1+\dfrac{p-1}{p^s} + \dfrac{p(p-1)}{p^{2s}} + \dfrac{p^2(p-1)}{p^{3s}}+\cdots\right)\\
        &= \prod_{p\in\mathbf P}\left(\dfrac{1}{1-p^{1-s}}-\dfrac{1}{p^s}\dfrac{1}{1-p^{1-s}}\right) = \prod_{p\in\mathbf P}\dfrac{1-p^{-s}}{1-p^{1-s}} = \dfrac{\zeta(s-1)}{\zeta(s)}.
        \end{aligned}
        $$
    
        U kombinaciji s izrazom za Dirichletovu funkciju izvodnicu potencije dobiva se $\mathrm{id} = \varphi\ast 1$.
    
    6.  Funkcija djelitelja $\sigma_k(n)=\sum_{d\mid n}d^k$ multiplikativna je funkcija. Njezina Dirichletova funkcija izvodnica jest
    
        $$
        \begin{aligned}
        \Sigma_k(s) &= \prod_{p\in\mathbf P}\left(1+\dfrac{1+p^k}{p^s}+\dfrac{1+p^k+p^{2k}}{p^{2s}}+\dfrac{1+p^k+p^{2k}+p^{3k}}{p^{3s}}+\cdots\right) \\
        &= \prod_{p\in\mathbf P}\dfrac{1}{1-p^k}\left((1-p^k)+\dfrac{1-p^{2k}}{p^s}+\dfrac{1-p^{3k}}{p^{2s}}+\dfrac{1-p^{4k}}{p^{3s}}+\cdots\right)\\
        &= \prod_{p\in\mathbf P}\dfrac{1}{1-p^k}\left(\dfrac{1}{1-p^{-s}} - \dfrac{p^k}{1-p^{k-s}}\right)\\
        &= \prod_{p\in\mathbf P}\dfrac{1}{(1-p^{-s})(1-p^{k-s})} = \zeta(s-k)\zeta(s).
        \end{aligned}
        $$
    
        U kombinaciji s izrazom za Dirichletovu funkciju izvodnicu potencije dobiva se $\sigma_k = \mathrm{id}_k\ast 1$. To je upravo definicijska formula za $\sigma_k$.
    
    7.  Indikatorska funkcija brojeva bez kvadratnih faktora $u(n)=|\mu(n)|=\mu^2(n)$ multiplikativna je funkcija. Njezina Dirichletova funkcija izvodnica jest
    
        $$
        U(s) = \prod_{p\in\mathbf P}(1+p^{-s}) = \prod_{p\in\mathbf P}\dfrac{1-p^{-2s}}{1-p^{-s}} = \dfrac{\zeta(s)}{\zeta(2s)}.
        $$

### Bellov red

Eulerov produkt pokazuje da se Dirichletova funkcija izvodnica multiplikativne funkcije može rastaviti na umnožak lokalnih faktora $F_p(s)$. Ako nas zanimaju samo informacije u jednom prostom broju, $p^{-s}$ možemo u cijelosti promatrati kao formalnu varijablu; tako se dobiva Bellov red.

Za multiplikativnu funkciju $f$ i prost broj $p$, **Bellov red** (Bell series) funkcije $f$ s obzirom na $p$ definira se kao formalni red potencija

$$
f_p(x) = \sum_{e=0}^{\infty} f(p^e)x^e = 1 + f(p)x + f(p^2)x^2 + \cdots.
$$

Usporedbom s izrazom za Eulerov produkt vidi se da je $f_p(x)$ upravo rezultat zamjene $p^{-s}$ s $x$ u $F_p(s)$, tj. $F_p(s) = f_p(p^{-s})$, pa je

$$
F(s) = \prod_{p\in\mathbf P}f_p(p^{-s}).
$$

Nakon uvođenja ove oznake vidi se da je Dirichletova konvolucija nakon lokalizacije samo obično množenje redova potencija.

Prevođenjem rezultata o Dirichletovim funkcijama izvodnicama na Bellove redove dobivaju se sljedeća svojstva:

1.  Za multiplikativne funkcije $f,g$ i svaki prost broj $p$ vrijedi $(f\ast g)_p(x) = f_p(x)g_p(x)$.
2.  Multiplikativna funkcija $f$ potpuno je multiplikativna ako i samo ako za svaki prost broj $p$ vrijedi $f_p(x) = \dfrac{1}{1-f(p)x}$.
3.  Dirichletov inverz multiplikativne funkcije uvijek postoji i $(f^{-1})_p(x) = \dfrac{1}{f_p(x)}$.

Budući da je multiplikativna funkcija jednoznačno određena svojim vrijednostima na potencijama prostih brojeva, multiplikativne funkcije i skupovi svih njihovih Bellovih redova $\{f_p\}_{p\in\mathbf P}$ u bijektivnoj su korespondenciji. Stoga se mnogi problemi o Dirichletovoj konvoluciji multiplikativnih funkcija mogu, prost broj po prost broj, svesti na probleme o formalnim redovima potencija. U usporedbi s izravnom uporabom Dirichletovih funkcija izvodnica, to je formalno nešto jednostavnije. Primjerice, treće svojstvo kaže da je za Dirichletov inverz dovoljno za svaki prost broj zasebno naći inverz formalnog reda potencija; u praktičnom računanju, budući da je potreban samo dio s $p^e\le n$, za svaki prost broj red se odsiječe najviše do člana $x^{\lfloor\log_p n\rfloor}$.

???+ example "Primjer"
    Bellovi redovi multiplikativnih funkcija iz prethodnih primjera jesu:
    
    |    $f$   | $\varepsilon$ |        $1$       | $\mu$ | $\operatorname{id}_k$ |      $\varphi$      |         $\sigma_k$         | $\lvert\mu\rvert=\mu^2$ |
    | :------: | :-----------: | :--------------: | :---: | :-------------------: | :-----------------: | :------------------------: | :---------------------: |
    | $f_p(x)$ |      $1$      | $\dfrac{1}{1-x}$ | $1-x$ |  $\dfrac{1}{1-p^kx}$  | $\dfrac{1-x}{1-px}$ | $\dfrac{1}{(1-x)(1-p^kx)}$ |          $1+x$          |
    
    Pomoću gornje tablice uobičajene se relacije Dirichletove konvolucije mogu izravno provjeriti. Primjerice, $\mu\ast 1=\varepsilon$ odgovara
    
    $$
    (1-x)\cdot\dfrac{1}{1-x} = 1,
    $$
    
    a $\varphi\ast 1=\operatorname{id}$ odgovara
    
    $$
    \dfrac{1-x}{1-px}\cdot\dfrac{1}{1-x} = \dfrac{1}{1-px}.
    $$

### Primjene

Dirichletove funkcije izvodnice mogu se upotrijebiti za prikaz aritmetičkih funkcija kao Dirichletovih konvolucija.

Primjerice, u Du situ za računanje prefiksnih suma aritmetičke funkcije $f$ treba naći drugu aritmetičku funkciju $g$ takvu da se prefiksne sume i od $f\ast g$ i od $g$ mogu brzo izračunati. Taj se postupak može izvesti pomoću Dirichletovih funkcija izvodnica.

Uzmimo za primjer zadatak iz odjeljka o Du situ [Luogu P3768 简单的数学题 (Jednostavan matematički zadatak)](../number-theory/hyperbola.md#例题): za $f(n)=n^2\varphi(n)$ treba konstruirati aritmetičku funkciju $g(n)$ koja zadovoljava gornje uvjete. Budući da je $f$ multiplikativna funkcija, njezina Dirichletova funkcija izvodnica jest

$$
F(s) = \prod_{p\in\mathbf P}\left(1 + \sum_{k=1}^{\infty}\dfrac{p^{3k-1}(p-1)}{p^{ks}}\right) = \prod_{p\in\mathbf P}\dfrac{1-p^{2-s}}{1-p^{3-s}} = \dfrac{\zeta(s-3)}{\zeta(s-2)}.
$$

Usporedbom s Dirichletovom funkcijom izvodnicom potencije vidi se da je dovoljno uzeti $g = \mathrm{id}_2$ pa je $f \ast g = \mathrm{id}_3$. Prefiksne sume obiju funkcija mogu se brzo izračunati.

Budući da su aritmetičke funkcije u uobičajenim zadacima multiplikativne, u praksi je često zgodnije koristiti Bellove redove. Primjerice, u upravo navedenom primjeru Bellov red funkcije $f(n)$ izravno se iz $f(p^e)=p^{3e-1}(p-1)$ dobiva kao

$$
f_p(x) = 1 + \dfrac{p-1}{p}\sum_{e=1}^{\infty}(p^3x)^e = 1 + \dfrac{(p-1)p^2x}{1-p^3x} = \dfrac{1-p^2x}{1-p^3x}.
$$

Usporedbom s Bellovim redom potencije odmah se dobiva $f \ast \mathrm{id}_2 = \mathrm{id}_3$.

## Računanje Dirichletove konvolucije

Ovaj odjeljak razmatra problem računanja Dirichletove konvolucije: za zadane nizove $\{f(k)\}_{k=1}^n$ i $\{g(k)\}_{k=1}^n$ treba odrediti prvih nekoliko članova $\{h(k)\}_{k=1}^n$ Dirichletove konvolucije $h=f\ast g$. Ovisno o svojstvima uključenih funkcija, složenost algoritma malo se razlikuje.

### Opći slučaj

Ako $f,g,h$ nemaju posebnih svojstava, Dirichletova konvolucija može se izračunati samo prema definiciji:

$$
h(n) = \sum_{k\ell = n}f(k)g(\ell).
$$

Dovoljno je iterirati po $k$ i $\ell$ te doprinos $f(k)g(\ell)$ pribrojiti u $h(k\ell)$. Složenost iteriranja iznosi

$$
O\left(\sum_{k=1}^{n}\dfrac{n}{k}\right) = O(n\log n).
$$

Referentna implementacija:

???+ example "Referentna implementacija"
    ```cpp
    --8<-- "docs/math/code/dirichlet/dirichlet-1.cpp:core"
    ```

### Konvolucija s multiplikativnom funkcijom

Ako je $g$ multiplikativna funkcija, računanje Dirichletove konvolucije može se ubrzati pomoću Eulerova produkta. Računanje $h$ jednako je računanju koeficijenata njezine Dirichletove funkcije izvodnice $H$. Budući da je

$$
H(s) = F(s)G(s) = F(s)\prod_{p\in\mathbf P}G_p(s).
$$

Pritom je $G_p(s)$ faktor u rastavu $G(s)$ na Eulerov produkt, koji sadrži samo koeficijente na potencijama od $p$:

$$
G_p(s) = \sum_{p^k\le n}\dfrac{g(p^k)}{p^{ks}} = 1 + \dfrac{g(p)}{p^s} + \dfrac{g(p^2)}{p^{2s}} + \cdots.
$$

Dakle, krenuvši od $F(s)$, prolazeći sve proste brojeve $p$ koji ne premašuju $n$ i množeći redom s $G_p(s)$, također se dobiva konačni rezultat $H(s)$. Pri množenju s $G_p(s)$ dovoljno je izravno primijeniti algoritam grubom silom iz općeg slučaja. Ukupan broj iteracija

$$
\sum_{p\in\mathbf P,~p\le n}\sum_{k=1}^{\infty}\left\lfloor\dfrac{n}{p^k}\right\rfloor \le \sum_{p\in\mathbf P,~p\le n}\dfrac{n}{p-1} \le \sum_{p\in\mathbf P,~p\le n}\dfrac{2n}{p} \in O(n\log\log n).
$$

Posljednji korak ocjene složenosti podudara se s dokazom složenosti [Eratostenova sita](./sieve.md#埃拉托斯特尼筛法). Stoga je vremenska složenost ovog algoritma $O(n\log\log n)$.

Referentna implementacija:

???+ example "Referentna implementacija"
    ```cpp
    --8<-- "docs/math/code/dirichlet/dirichlet-2.cpp:core"
    ```

Posebno, kada je multiplikativna funkcija $g$ potpuno multiplikativna ili njezin Dirichletov inverz, primjerice kada je $g = 1$ ili $g = \mu$, algoritam se može dodatno pojednostavniti. Tada se za računanje Dirichletove konvolucije $h = f\ast g$ može upotrijebiti algoritam [Dirichletovih prefiksnih suma/razlika](./mobius.md#dirichletove-prefiksne-sume) s manjom konstantom, no vremenska složenost algoritma i dalje je $O(n\log\log n)$.

### Slučaj kada je rezultat multiplikativna funkcija

Naposljetku razmotrimo slučaj kada je $h$ multiplikativna funkcija. Posebno, kada su $f,g$ obje multiplikativne, $h=f \ast g$ je multiplikativna. Za računanje $h$ dovoljno je odrediti njezine vrijednosti na potencijama prostih brojeva, a zatim se ona može izračunati [linearnim sitom](./sieve.md#线性筛法) u vremenu $O(n)$. Vrijednosti $h(p^e)$ na potencijama prostih brojeva $p^e$ računaju se izravno grubom silom:

$$
h(p^e) = \sum_{i=0}^e f(p^i)g(p^{e-i}).
$$

Broj iteracija potreban za ta računanja grubom silom iznosi

$$
\begin{aligned}
\sum_{p\in\mathbf P,~p\le n}\sum_{e=1}^{\lfloor\log_p n\rfloor}(e+1) &\le \sum_{p\in\mathbf P,~p\le\sqrt{n}}2\lfloor\log_p n\rfloor^2 + \sum_{p\in\mathbf P,~\sqrt{n} < p\le n}2 \\
&\le 2\sqrt{n}(\log_2 n)^2 + 2n \in O(n).
\end{aligned}
$$

Stoga je ukupna vremenska složenost ovog algoritma $O(n)$.

Referentna implementacija:

???+ example "Referentna implementacija"
    ```cpp
    --8<-- "docs/math/code/dirichlet/dirichlet-3.cpp:core"
    ```

## Literatura i napomene

-   [Dirichlet convolution - Wikipedia](https://en.wikipedia.org/wiki/Dirichlet_convolution)
-   [Dirichlet series - Wikipedia](https://en.wikipedia.org/wiki/Dirichlet_series)
-   [Euler product - Wikipedia](https://en.wikipedia.org/wiki/Euler_product)
-   [Bell series - Wikipedia](https://en.wikipedia.org/wiki/Bell_series)
-   [Dirichlet 積と、数論関数の累積和 (Dirichletov produkt i prefiksne sume aritmetičkih funkcija) by maspy](https://maspypy.com/dirichlet-%e7%a9%8d%e3%81%a8%e3%80%81%e6%95%b0%e8%ab%96%e9%96%a2%e6%95%b0%e3%81%ae%e7%b4%af%e7%a9%8d%e5%92%8c)
-   [杜教筛（+ 贝尔级数 + powerful number）(Du sito (+ Bellovi redovi + powerful number)) by command\_block - Luogu](https://www.luogu.com.cn/article/ygfzawod)
