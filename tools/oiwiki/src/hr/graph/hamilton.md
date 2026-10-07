---
title: Hamiltonovi grafovi
---

## Definicija

Put koji prolazi kroz svaki vrh grafa točno jednom zove se Hamiltonov put.

Ciklus koji prolazi kroz svaki vrh grafa točno jednom zove se Hamiltonov ciklus.

Graf koji ima Hamiltonov ciklus zove se Hamiltonov graf.

Graf koji ima Hamiltonov put, ali nema Hamiltonov ciklus, zove se polu-Hamiltonov graf.

## Svojstva

Neka je $G=\langle V, E\rangle$ Hamiltonov graf. Tada za svaki neprazni pravi podskup $V_1$ skupa $V$ vrijedi $p(G-V_1) \leq |V_1|$, gdje je $p(x)$ broj komponenata povezanosti grafa $x$.

Posljedica: neka je $G=\langle V, E\rangle$ polu-Hamiltonov graf. Tada za svaki neprazni pravi podskup $V_1$ skupa $V$ vrijedi $p(G-V_1) \leq |V_1|+1$, gdje je $p(x)$ broj komponenata povezanosti grafa $x$.

Potpuni graf $K_{2k+1} (k \geq 1)$ sadrži $k$ bridno disjunktnih Hamiltonovih ciklusa, i tih $k$ bridno disjunktnih Hamiltonovih ciklusa sadrži sve bridove grafa $K_{2k+1}$.

Potpuni graf $K_{2k} (k \geq 2)$ sadrži $k-1$ bridno disjunktnih Hamiltonovih ciklusa; graf koji ostane kad se iz $K_{2k}$ uklone ta $k-1$ bridno disjunktna Hamiltonova ciklusa sadrži $k$ međusobno nesusjednih bridova.

## Dovoljni uvjeti

Neka je $G$ jednostavan neusmjereni graf s $n(n \geq 2)$ vrhova. Ako za svaka dva nesusjedna vrha $v_i, v_j$ grafa $G$ vrijedi $d(v_i)+ d(v_j) \geq n - 1$, tada u $G$ postoji Hamiltonov put.

Posljedica 1: neka je $G$ jednostavan neusmjereni graf s $n(n \geq 3)$ vrhova. Ako za svaka dva nesusjedna vrha $v_i, v_j$ grafa $G$ vrijedi $d(v_i)+ d(v_j) \geq n$, tada u $G$ postoji Hamiltonov ciklus, pa je $G$ Hamiltonov graf.

Posljedica 2: neka je $G$ jednostavan neusmjereni graf s $n(n \geq 3)$ vrhova. Ako za svaki vrh $v_i$ grafa $G$ vrijedi $d(v_i) \geq \frac{n}{2}$, tada u $G$ postoji Hamiltonov ciklus, pa je $G$ Hamiltonov graf.

Neka je $D$ turnir reda $n(n \geq 2)$. Tada $D$ ima Hamiltonov put.

Ako $D$ sadrži turnir reda $n(n \geq 2)$ kao podgraf, tada $D$ ima Hamiltonov put.

Jako povezan turnir je Hamiltonov graf.

Ako $D$ sadrži jako povezan turnir reda $n(n \geq 2)$ kao podgraf, tada $D$ ima Hamiltonov ciklus.
