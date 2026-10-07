---
title: Automat podnizova
---

Prije ovog članka pročitajte članak [Automati](../misc/fsm.md).

## Definicija

Automat podnizova (subsequence automaton) jest automat koji prihvaća točno sve podnizove zadanog stringa.

U ovom članku taj string označavamo s $s$.

### Stanja

Ako $s$ sadrži $n$ znakova, njegov automat podnizova ima $n+1$ stanja.

Neka je $t$ podniz stringa $s$. Tada je $\delta(start, t)$ završna pozicija prvog pojavljivanja podniza $t$ u $s$.

Drugim riječima, stanje $i$ predstavlja razliku skupa podnizova prefiksa $s[1..i]$ i skupa podnizova prefiksa $s[1..i-1]$.

Sva stanja automata podnizova prihvatljiva su stanja.

### Prijelazi

Iz definicije stanja slijedi $\delta(u, c)=\min\{i|i>u,s[i]=c\}$, odnosno pozicija sljedećeg pojavljivanja znaka $c$.

Zašto baš „sljedeće” pojavljivanje? Ako je $i>j$, podnizovi sufiksa $s[i..|s|]$ čine podskup podnizova sufiksa $s[j..|s|]$, pa je uvijek optimalno odabrati što ranije pojavljivanje.

## Implementacija

Prolazimo zdesna nalijevo i pritom održavamo najraniju poziciju pojavljivanja svakog znaka:

$$
\begin{array}{ll}
1 & \textbf{Input. } \text{A string } S\\
2 & \textbf{Output. } \text{The state transition of the sequence automaton of }S \\
3 & \textbf{Method. }  \\
4 & \textbf{for }c\in\Sigma\\
5 & \qquad next[c]\gets null\\
6 & \textbf{for }i\gets|S|\textbf{ downto }1\\
7 & \qquad next[S[i]]\gets i\\
8 & \qquad \textbf{for }c\in\Sigma\\
9 & \qquad\qquad \delta(i-1,c)\gets next[c]\\
10 & \textbf{return }\delta
\end{array}
$$

Složenost ovakve konstrukcije jest $O(n|\Sigma|)$.

## Primjer zadatka

???+ example "[HEOI2015: Najkraći nezajednički podstring](https://loj.ac/problem/2123)"
    Zadana su dva stringa $A$ i $B$ sastavljena od malih slova engleske abecede ($1\le |A|, |B|\le 2000$). Pronađite:
    
    1.  najkraći podstring stringa $A$ koji nije podstring stringa $B$;
    2.  najkraći podstring stringa $A$ koji nije podniz stringa $B$;
    3.  najkraći podniz stringa $A$ koji nije podstring stringa $B$;
    4.  najkraći podniz stringa $A$ koji nije podniz stringa $B$.

??? note "Rješenje"
    Za prvi i treći dio potrebni su sufiksni automati, a postupci su slični. Ovdje objašnjavamo samo drugi i četvrti dio.
    
    Drugi je dio jednostavan: isprobamo podstringove stringa A i propuštamo ih kroz automat podnizova stringa B. Ako podstring nije prihvaćen, uzimamo ga kao kandidata za odgovor.
    
    Za četvrti dio potreban je DP. Neka $f(i, j)$ označava koliko znakova još treba dodati da dobijemo podniz koji nije zajednički, ako smo u stanju $i$ automata podnizova stringa A i stanju $j$ automata podnizova stringa B. Prijelaz je:
    
    $$
    f(i, j)=\min_{\delta_A(i,c)\ne \textit{null}}f(\delta_A(i, c), \delta_B(j, c))+1.
    $$
    
    Početno je stanje $f(i, \textit{null})=0$.

??? note "Referentni kôd"
    ```cpp
    --8<-- "docs/string/code/seq-automaton/seq-automaton_1.cpp"
    ```
