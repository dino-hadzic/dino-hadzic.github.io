---
title: Osnove stringova
---

## Definicije

### Abeceda

**Abeceda** (skup znakova) $\Sigma$ skup je na kojem je zadan [totalni uređaj](../math/order-theory.md#偏序集), što znači da se bilo koja dva različita elementa $\alpha$ i $\beta$ iz $\Sigma$ mogu usporediti: vrijedi ili $\alpha<\beta$ ili $\beta<\alpha$. Elementi abecede $\Sigma$ zovu se znakovi.

### String

**String** (znakovni niz) $S$ niz je dobiven redanjem $n\ (n\ge 0)$ znakova; $n$ se zove duljina stringa $S$ i označava se $|S|$. Posebno, za $n=0$ string $S$ ne sadrži nijedan znak i zove se **prazan string**, u oznaci $\varepsilon$.

Ako se indeksi stringa broje od $1$, $i$-ti znak stringa $S$ označava se $S[i]$;

ako se indeksi stringa broje od $0$, $i$-ti znak stringa $S$ označava se $S[i-1]$.

### Podstring

**Podstring** stringa $S$, $S[i..j]，i≤j$, dio je stringa $S$ od položaja $i$ do položaja $j$, tj. string dobiven redanjem $S[i],S[i+1],\ldots,S[j]$.

Ponekad se $S[i..j]$ s $i>j$ koristi za označavanje praznog stringa $\varepsilon$.

### Podniz

**Podniz** (subsequence) stringa $S$ niz je dobiven izdvajanjem nekoliko elemenata iz $S$ bez promjene njihova relativnog poretka, tj. $S[p_1],S[p_2],\ldots,S[p_k]$, $1\le p_1< p_2<\cdots< p_k\le|S|$, $k\ge 0$.

### Sufiks

**Sufiks** je poseban podstring koji počinje na nekom položaju $i$ i završava na kraju cijelog stringa. Sufiks stringa $S$ koji počinje na položaju $i$ označava se $\textit{Suffix(S,i)}$, tj. $\textit{Suffix(S,i)}=S[i..|S|-1]$.

**Pravi sufiks** je svaki sufiks stringa $S$ osim samog $S$.

Na primjer, svi sufiksi stringa `abcabcd` su `{ε, d, cd, bcd, abcd, cabcd, bcabcd, abcabcd}`, a njegovi pravi sufiksi su `{ε, d, cd, bcd, abcd, cabcd, bcabcd}`.

### Prefiks

**Prefiks** je poseban podstring koji počinje na početku stringa i završava na nekom položaju $i$. Prefiks stringa $S$ koji završava na položaju $i$ označava se $\textit{Prefix(S,i)}$, tj. $\textit{Prefix(S,i)}=S[0..i]$.

**Pravi prefiks** je svaki prefiks stringa $S$ osim samog $S$.

Na primjer, svi prefiksi stringa `abcabcd` su `{ε, a, ab, abc, abca, abcab, abcabc, abcabcd}`, a njegovi pravi prefiksi su `{ε, a, ab, abc, abca, abcab, abcabc}`.

### Leksikografski poredak

Stringovi se uspoređuju tako da je $i$-ti znak $i$-ti ključ usporedbe; prazan znak manji je od svakog znaka abecede (tj. $a< aa$).

### Palindrom

**Palindrom** je string koji se jednako čita s početka i s kraja, tj. string $s$ za koji vrijedi $\forall 1\le i\le|s|, s[i]=s[|s|+1-i]$.

### Hammingova udaljenost

**Hammingova udaljenost** udaljenost je između dvaju stringova jednake duljine: broj položaja na kojima se odgovarajući znakovi dvaju stringova razlikuju.

Pojednostavljeno, ako nad dvama stringovima izvedemo operaciju XOR, broj znamenki $1$ u rezultatu jest Hammingova udaljenost tih stringova.

## Pohrana stringova

-   Pohrana u polju tipa `char`, pri čemu prazni znak `\0` označava kraj stringa (stringovi u stilu jezika C).
-   Korištenje [klase `string`](../lang/csl/string.md) iz standardne biblioteke jezika C++.
-   Konstantni stringovi mogu se zapisati kao string literali (stringovi u dvostrukim navodnicima).
