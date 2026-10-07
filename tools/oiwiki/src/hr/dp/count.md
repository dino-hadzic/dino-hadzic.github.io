---
title: DP za prebrojavanje
---

**DP za prebrojavanje** (counting DP) metoda je memoiziranog pretraživanja slična DP-u (razlikuje se od DP-a u užem smislu, tj. od optimizacijskih problema) i služi za rješavanje problema prebrojavanja (i zbrajanja).

## Osnove

### Osnovna ideja

Problem prebrojavanja obično znači odrediti veličinu nekog skupa $S$. U natjecateljskom programiranju veličina skupa $S$ katkad doseže red $\Theta(n^n)$ ili čak $\Theta(2^{n!})$ (naravno, obično se traži ostatak modulo neki fiksni broj), gdje je $n$ veličina problema, pa elemente skupa $S$ ne možemo nabrajati jedan po jedan.

Ako skup $S$ uspijemo podijeliti na nekoliko disjunktnih podskupova, broj elemenata skupa $S$ jednak je zbroju brojeva elemenata tih dijelova. Ako je prebrojavanje tih podskupova upravo problem sličan izvornom, možemo ga riješiti metodom nalik dinamičkom programiranju.

### Primjer

???+ note "Primjer"
    Zadan je pozitivan cijeli broj $n$. Na koliko se načina $n$ može zapisati kao zbroj $k$ pozitivnih cijelih brojeva, ako se rasporedi s zamijenjenim položajima smatraju različitima?

Neka je $S_{n,k}$ skup uređenih k-torki pozitivnih cijelih brojeva $(a_1, \dots, a_k)$ takvih da je $a_1 + \dots + a_k = n$. Ako fiksiramo $a_k$, zaključujemo ovako: budući da je $a_1 + a_2 + \dots + a_{k-1} + a_k = n$, vrijedi $a_1 + a_2 + \dots + a_{k-1} = n - a_k$. Po definiciji $S_{n,k}$ slijedi $(a_1, a_2, \dots, a_{k-1}) \in S_{n - a_k, k - 1}$.

Budući da su $a_1, a_2, \dots, a_k$ pozitivni cijeli brojevi, $a_k$ poprima vrijednosti iz $[1, n - k + 1] \cap \mathbb Z$. Stoga se $S_{n,k}$ može podijeliti prema $a_k$ na $n - k + 1$ podskupova; za $a_k = i$ taj podskup glasi:

$$
\{(L, i) \mid L \in S_{n-i,k-1}\}.
$$

Broj elemenata tog podskupa očito je jednak $S_{n-i,k-1}$, a zbog različitih $i$ ti su podskupovi međusobno disjunktni. Dakle:

$$
|S_{n,k}| = \sum_{i=1}^{n-k+1} |S_{n-i,k-1}|.
$$

Tako to možemo obraditi metodom sličnom DP-u: neka je $f_{n,k}$ jednako $|S_{n,k}|$; jednadžba prijelaza stanja glasi:

$$
f_{n,k} = \sum_{i=1}^{n-k+1} f_{n-i,k-1}.
$$

Sada se zadatak može riješiti DP-om.

### Sličnosti i razlike s optimizacijskim DP-om

Uočimo da i DP za prebrojavanje i optimizacijski DP na nekom području $\Omega$ računaju jednu vrijednost (veličinu, optimum); ta se vrijednost dobiva tako da se svaki element iz $\Omega$ jednom obradi, a dobivene se vrijednosti zatim objedine.

Primjerice, u 0-1 problemu ruksaka elementi skupa $\Omega$ su skupovi predmeta koje stavljamo u ruksak; za jedan odabir $S$ iz $\Omega$ obradimo $S$ jednom, a rezultat obrade $w(S)$ je ukupna vrijednost predmeta u $S$, a od svih dobivenih vrijednosti uzimamo najveću i to je odgovor.

U problemu prebrojavanja elementi skupa $\Omega$ su elementi skupa $S$ čiju veličinu računamo; obrada svaki element skupa $S$ pretvara u $1$, a te se $1$ objedinjuju zbrajanjem. Budući da svakom elementu skupa $S$ odgovara jedan $1$, dobivena je vrijednost upravo broj elemenata skupa $S$.

Kad je operacija objedinjavanja maksimum/minimum, $\Omega$ možemo podijeliti na proizvoljne dijelove; dovoljno je da je njihova unija $\Omega$, disjunktnost nije potrebna. U problemu prebrojavanja to ne vrijedi, pa $\Omega$ moramo podijeliti na međusobno disjunktne dijelove. To je razlika u odnosu na optimizacijski DP.

## Primjer

???+ note "Primjer"
    Zadan je pozitivan cijeli broj $n$. Na koliko se načina $n$ može zapisati kao zbroj proizvoljno mnogo pozitivnih cijelih brojeva, ako se rasporedi s zamijenjenim položajima smatraju **istim** rastavom?

### Rješenje 1

Elementi skupa koji trebamo prebrojati multiskupovi su pozitivnih cijelih brojeva sa zbrojem $n$. No tako se očito teško izvodi rekurzija.

Ako multiskup $T$ sadrži samo pozitivne cijele brojeve $\le M$ i zbroj svih elemenata od $T$ je $n$, pišemo $T \in S_{n, M}$. Promotrimo koliko se puta pojavljuje $M$. Može se pojaviti $k \in \left[0, \left\lfloor \dfrac nM \right\rfloor\right] \cap \mathbb Z$ puta. Tada se prelazi u $S_{n - kM, M - 1}$. Dovoljno je zbrojiti. Složenost je $\Theta(n^2 \log n)$ ($\log$ dolazi od harmonijskog reda koji daje raspon vrijednosti $k$).

No to još nije dovoljno dobro. Promotrimo sljedeći primjer:

$$
\begin{aligned}
f_{8, 3} &= {\color{red}f_{8, 2} + f_{5, 2} + f_{2, 2}} \\
f_{9, 3} &= {\color{blue}f_{9, 2} + f_{6, 2} + f_{3, 2} + f_{0, 2}} \\
f_{10, 3} &= {\color{green}f_{10, 2} + f_{7, 2} + f_{4, 2} + f_{1, 2}}\\
f_{11, 3} &= f_{11, 2} + {\color{red}f_{8, 2} + f_{5, 2} + f_{2, 2}}\\
f_{12, 3} &= f_{12, 2} + {\color{blue}f_{9, 2} + f_{6, 2} + f_{3, 2} + f_{0, 2}}\\
f_{13, 3} &= f_{13, 2} + {\color{green}f_{10, 2} + f_{7, 2} + f_{4, 2} + f_{1, 2}}\\
\end{aligned}
$$

Zamjenom jednakih izraza dobivamo $f_{11, 3} = f_{11, 2} + f_{8, 3}$, $f_{12, 3} = f_{12, 2} + f_{9, 3}$, $f_{13, 3} = f_{13, 2} + f_{10, 3}$. Analogno dobivamo opću jednadžbu prijelaza stanja:

$$
f_{n, M} = f_{n, M - 1} + \begin{cases} f_{n - M, M} & n \ge M, \\ 0 & \text{otherwise}. \end{cases}
$$

Vremenska je složenost sada $\Theta(n^2)$.

### Rješenje 2

Uočimo da se svaki multiskup pozitivnih cijelih brojeva $T$ može dobiti dvjema operacijama: „uvećaj svaki element od $T$ za jedan” i „dodaj u $T$ element vrijednosti $1$”, pri čemu različiti nizovi operacija daju različite rezultate.

Tako prijelaz po $T$ postaje prijelaz po nizu operacija. Promotrimo posljednju operaciju u nizu operacija koji $n$ rastavlja na $m$ brojeva (sve takve nizove označimo $B_{n,m}$). Ako je to operacija $1$, broj se elemenata ne povećava, ali $\sum T$ raste za $m$. Da bi na kraju bilo $\sum T = n$, prethodni $T$ (označimo ga $T'$) mora imati zbroj $n-m$. Dakle $B_{n,m} \to B_{n-m,m}$. Ako je to operacija $2$, dodaje se jedan broj i $\sum T$ raste za $1$. Dakle $B_{n,m} \to B_{n-1,m-1}$.

Vremenska je složenost i ovdje $\Theta(n^2)$.

### Rješenje 3

Podijelimo $T$ na dio $T_1$ s elementima većima od $\sqrt n$ i dio $T_2$ s elementima manjima ili jednakima $\sqrt n$. $T_2$ se može prebrojati Rješenjem 1, a broj mogućih $T_1$ malo izmijenjenim Rješenjem 2: dvije operacije postaju „uvećaj svaki element od $T_1$ za jedan” i „dodaj u $T_1$ element vrijednosti $\lfloor \sqrt n \rfloor + 1$”. Jednadžbu prijelaza stanja lako je napisati.

Rastavimo $n$ na dva dijela, $A$ i $B$. Prolaskom po jednom od njih dobivamo drugi. Izračunamo broj $T_1$ sa $\sum T_1 = A$ i broj $T_2$ sa $\sum T_2 = B$, pomnožimo ih i zbrojimo po svim $A$; to je konačan rezultat.

Budući da je pri računanju broja $T_1$ vrijednost $M \le \sqrt n$, Rješenje 1 za $T_1$ ima vremensku složenost $\Theta(n^{3/2})$. Jednako tako, pri računanju broja $T_2$ vrijedi $|T_2| \le \dfrac{\sum T_2}{\sqrt n} \le \dfrac{n}{\sqrt n} = \sqrt n$, pa Rješenje 2 za $T_2$ također ima složenost $\Theta(n^{3/2})$. Ukupna je vremenska složenost stoga $\Theta(n^{3/2})$.
