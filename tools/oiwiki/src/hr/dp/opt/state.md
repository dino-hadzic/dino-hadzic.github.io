---
title: Optimizacija dizajna stanja
---

## Pregled

Pri optimiranju DP-a ne moramo krenuti samo od prijelaza i ubrzavati ih. Ponekad se može krenuti od definicije stanja i promjenom načina na koji dizajniramo stanja postići bolju složenost.

Nezgodno je to što ove optimizacije uglavnom nisu općenite, tj. ne mogu se šablonski primijeniti na mnogo zadataka. Zato ćemo u nastavku krenuti od konkretnih primjera i pokušati dati poticaj za razmišljanje, u nadi da će čitatelju biti od koristi.

## Primjer 1

???+ note "Zadatak"
    Zadana su dva stringa $A,B$ duljina $n,m$ sastavljena samo od malih slova; odredi najdulji zajednički podniz stringova $A,B$. $(n\le 10^6,m\le 10^3)$

### Naivno rješenje

Odmah vidite rješenje – pa to je šablonski zadatak!

Definiramo stanje $f_{i,j}$ kao duljinu najduljeg zajedničkog podniza prvih $i$ znakova stringa $A$ i prvih $j$ znakova stringa $B$; tada vrijedi

$$
f_{i,j}=
\begin{cases}
\max(f_{i-1,j},f_{i,j-1}) & ,A_i \neq B_j \\
f_{i-1,j-1}+1 & ,A_i = B_j 
\end{cases}
$$

Vremenska složenost ovog pristupa je $O(nm)$, što nije dovoljno za ovaj zadatak.

### Bolje rješenje

Pažljivije razmislimo i uočimo svojstvo: konačni odgovor ne premašuje $m$.

Razmislimo još malo i uočimo da LCS ima greedy svojstvo.

Promijenimo definiciju stanja: $f_{i,j}$ neka je duljina najkraćeg prefiksa stringa $A$ čiji najdulji zajednički podniz s prvih $i$ znakova stringa $B$ ima duljinu $j$ (tj. zamijenimo odgovor naivnog rješenja i prvu dimenziju stanja).

Ako za svaki položaj u $A$ unaprijed izračunamo sljedeće pojavljivanje svakog od znakova $a,b,\cdots,z$, prijelaz prema naprijed radi se u $O(1)$.

Složenost je $O(m^2+26n)$, što prolazi.

## Primjer 2

???+ note "Zadatak"
    Zadan je netežinski usmjereni graf s $n$ vrhova; odredi postoji li u njemu Hamiltonov ciklus. $(2\le n\le 20)$

### Naivno rješenje

Vidjevši ograničenja, razmišljamo o bitmask DP-u.

Neka $f_{s,i}$ označava može li se iz vrha $1$, prolazeći samo kroz vrhove iz skupa $s$, doći do vrha $i$. Neka je $g$ matrica susjedstva grafa. Tada vrijedi

$$
f_{s, i} = \bigvee_{j\in s, j\neq i}f_{s \setminus \{i\}, j}\wedge g_{j, i} \left(i\in s\right)
$$

Vremenska složenost je $O(n^2 \times 2^n)$; uz urednu implementaciju možda i prođe, ali nije elegantno.

### Bolje rješenje

U gornjem dizajnu stanja svaka vrijednost $dp$-a predstavlja samo jedan `bool`, što djeluje rasipno.

Možemo za svako stanje $s$ spakirati $f_{s,1},f_{s,2},\dots,f_{s,n}$ u jedan `int`; uočimo da se, ako jednako spakiramo i matricu susjedstva, prijelaz može izvesti u $O(1)$.

Vremenska složenost je $O(n^2/w\times 2^n)$, što prolazi, pri čemu je $w$ broj bitova tipa `int`.

## Primjer 3

???+ note "Zadatak"
    Običan problem ruksaka. $n$ je broj predmeta, $m$ kapacitet ruksaka, a $v_i, w_i$ volumen i vrijednost $i$-tog predmeta; $1 \le n \le 10^3$, $1 \le m, v_i \le \color{red}{10^{18}}$, $1 \le \sum w_i \le 10^3$.

### Naivno rješenje

Ovo je šablonski zadatak o ruksaku.

Definiramo stanje $f_{i, j}$ kao najveći zbroj vrijednosti ako smo birali među prvih $i$ predmeta i trenutno je u ruksaku zauzet kapacitet $j$.

Lako se dobije $f_{i, j} = \max(f_{i - 1, j}, f_{i - 1, j - v_i} + w_i)$.

Budući da je $v_i \le 10^{18}$, ovo ne prolazi.

### Bolje rješenje

Zamijenimo odgovor i drugu dimenziju stanja: neka je $f_{i, j}$ najmanji ukupni volumen ako smo birali među prvih $i$ predmeta i predmeti u ruksaku **imaju ukupnu vrijednost $j$**.

I dalje se lako dobije $f_{i, j} = \min(f_{i - 1, j}, f_{i - 1, j - w_i} + v_i)$.

Uočimo da se nakon promjene druge dimenzije stanja mora promijeniti i prijelaz.

Vremenska složenost je $O(n \sum w_i)$, što prolazi.
