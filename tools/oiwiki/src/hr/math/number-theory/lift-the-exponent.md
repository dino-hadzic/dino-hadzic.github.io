---
title: Lema o podizanju eksponenta
---

## Sadržaj

Lema o podizanju eksponenta (Lift the Exponent, LTE) često je korišten teorem elementarne teorije brojeva.

Definirajmo $\nu_p(n)$ kao eksponent prostog faktora $p$ u kanonskom rastavu cijelog broja $n$, tj. $\nu_p(n)$ zadovoljava $p^{\nu_p(n)}\mid n$ i $p^{\nu_p(n)+1}\nmid n$.

Budući da je sadržaj leme o podizanju eksponenta poduži, podijelit ćemo ga u tri dijela:

U nastavku neka je $p$ prost broj, $x,y$ cijeli brojevi takvi da $p\nmid x$ i $p\nmid y$, a $n$ pozitivni cijeli broj.

### Prvi dio

Za sve proste brojeve $p$ i cijele brojeve $n$ takve da je $(n,p)=1$:

1.  Ako $p\mid x-y$, tada:

    $$
    \nu_p\left(x^n-y^n\right)=\nu_p(x-y)
    $$

2.  Ako $p\mid x+y$, tada za neparan $n$ vrijedi:

    $$
    \nu_p\left(x^n+y^n\right)=\nu_p(x+y)
    $$

???+ note "Dokaz"
    Ako $p\mid x-y$, nije teško uočiti da $p\mid x-y\iff x\equiv y\pmod p$, pa očito vrijedi:
    
    $$
    \sum_{i=0}^{n-1}x^iy^{n-1-i}\equiv nx^{n-1}\not\equiv 0\pmod p
    $$
    
    Nadalje, iz $x^n-y^n=(x-y)\sum_{i=0}^{n-1}x^iy^{n-1-i}$ slijedi tvrdnja.
    
    Za slučaj $p\mid x+y$ dokaz je sličan.

### Drugi dio

Ako je $p$ neparan prost broj:

1.  Ako $p\mid x-y$, tada:

    $$
    \nu_p\left(x^n-y^n\right)=\nu_p(x-y)+\nu_p(n)
    $$

2.  Ako $p\mid x+y$, tada za neparan $n$ vrijedi:

    $$
    \nu_p\left(x^n+y^n\right)=\nu_p(x+y)+\nu_p(n)
    $$

???+ note "Dokaz"
    Ako $p\mid x-y$, stavimo $y=x+kp$; dovoljno je dokazati slučaj $p\mid n$.
    
    -   Ako je $n=p$, prema binomnom teoremu:
    
        $$
        \begin{aligned}
            \sum_{i=0}^{p-1}x^{p-1-i}y^i&=\sum_{i=0}^{p-1}x^{p-1-i}\sum_{j=0}^i\binom{i}{j}x^j(kp)^{i-j}\\
            &\equiv px^{p-1} \pmod{p^2}\\
        \end{aligned}
        $$
    
        pa je
    
        $$
        \nu_p\left(x^n-y^n\right)=\nu_p(x-y)+1
        $$
    -   Ako je $n=p^a$, matematičkom indukcijom dobivamo
    
        $$
        \nu_p\left(x^n-y^n\right)=\nu_p(x-y)+a
        $$
    
    Time je tvrdnja dokazana.
    
    Za slučaj $p\mid x+y$ dokaz je sličan.

### Treći dio

Ako je $p=2$ i $p\mid x-y$:

1.  Za neparan $n$ vrijedi (isto kao u točki 1 prvog dijela):

    $$
    \nu_p\left(x^n-y^n\right)=\nu_p(x-y)
    $$

2.  Za paran $n$ vrijedi:

    $$
    \nu_p\left(x^n-y^n\right)=\nu_p(x-y)+\nu_p(x+y)+\nu_p(n)-1
    $$

Osim toga, za gornje $x,y,n$ vrijedi:

Ako $4\mid x-y$, tada:

-   $\nu_2(x+y)=1$
-   $\nu_2\left(x^n-y^n\right)=\nu_2(x-y)+\nu_2(n)$

???+ note "Dokaz"
    Dovoljno je dokazati slučaj kad je $n$ paran. Budući da sada $p\nmid \dbinom{p}{2}$, ne možemo dokazivati metodom iz drugog dijela.
    
    Stavimo $n=2^a b$, gdje je $a=\nu_p(n)$ i $2\nmid b$; tada je
    
    $$
    \begin{aligned}
        \nu_p\left(x^n-y^n\right)&=\nu_p\left(x^{2^a}-y^{2^a}\right)\\
        &=\nu_p\left((x-y)(x+y)\prod_{i=1}^{a-1}\left(x^{2^i}+y^{2^i}\right)\right)
    \end{aligned}
    $$
    
    Uočimo da $2\mid x-y\implies 4\mid x^2-y^2$, pa je $(\forall i\geq 1),~~x^{2^i}+y^{2^i}\equiv 2\pmod 4$, te gornji izraz postaje:
    
    $$
    \nu_p\left(x^n-y^n\right)=\nu_p(x-y)+\nu_p(x+y)+\nu_p(n)-1
    $$
    
    Time je tvrdnja dokazana.

## Literatura

1.  [Lifting-the-exponent lemma - Wikipedia](https://en.wikipedia.org/wiki/Lifting-the-exponent_lemma)
