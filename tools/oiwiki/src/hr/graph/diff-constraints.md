---
title: Sustavi razlika (difference constraints)
---

## Definicija

**Sustav razlika** (system of difference constraints) posebna je vrsta sustava od $n$ linearnih nejednadžbi: sadrži $n$ varijabli $x_1,x_2,\dots,x_n$ i $m$ ograničenja, a svako ograničenje razlika je dviju varijabli, oblika $x_i-x_j\leq c_k$, gdje je $1 \leq i, j \leq n, i \neq j, 1 \leq k \leq m$, a $c_k$ je konstanta (može biti nenegativna ili negativna). Problem koji rješavamo jest: pronaći rješenje $x_1=a_1,x_2=a_2,\dots,x_n=a_n$ koje zadovoljava sva ograničenja ili utvrditi da rješenja nema.

Svako ograničenje $x_i-x_j\leq c_k$ sustava razlika može se zapisati kao $x_i\leq x_j+c_k$, što je vrlo slično nejednakosti trokuta $dist[y]\leq dist[x]+z$ u problemu najkraćeg puta iz jednog izvora. Zato svaku varijablu $x_i$ promatramo kao vrh grafa, a za svako ograničenje $x_i-x_j\leq c_k$ povučemo usmjereni brid od vrha $j$ do vrha $i$ duljine $c_k$.

Uočimo: ako je $\{a_1,a_2,\dots,a_n\}$ rješenje sustava razlika, onda je za svaku konstantu $d$ i $\{a_1+d,a_2+d,\dots,a_n+d\}$ očito rješenje, jer se pri oduzimanju $d$ upravo poništi.

## Postupak

Postavimo $dist[0]=0$, iz vrha $0$ povučemo brid težine $0$ u svaki vrh i pokrenemo najkraći put iz jednog izvora. Ako graf sadrži negativni ciklus, sustav razlika nema rješenja; inače je $x_i=dist[i]$ jedno rješenje sustava.

## Svojstva

Postojanje negativnog ciklusa obično se provjerava Bellman–Fordom ili Bellman–Fordom s redom (popularno SPFA, koji je na nekim nasumičnim grafovima vrlo brz); najgora vremenska složenost je $O(nm)$.

## Uobičajene transformacije

### Primjer [Luogu P1993 小 K 的农场](https://www.luogu.com.cn/problem/P1993)

Sažetak zadatka: riješiti sustav razlika s $m$ ograničenja, svako oblika $x_a-x_b\geq c_k$, $x_a-x_b\leq c_k$ ili $x_a=x_b$; odrediti ima li sustav rješenje.

|      Ograničenje      |                   Pretvorba                   |            Brid            |
| :----------------: | :-----------------------------------------: | :---------------------------: |
| $x_a - x_b \geq c$ |             $x_b - x_a \leq -c$             |        `add(a, b, -c);`       |
| $x_a - x_b \leq c$ |              $x_a - x_b \leq c$             |        `add(b, a, c);`        |
|     $x_a = x_b$    | $x_a - x_b \leq 0, \space x_b - x_a \leq 0$ | `add(b, a, 0), add(a, b, 0);` |

Provjerimo negativni ciklus: ako ga nema, ispišemo `Yes`, inače `No`.

??? note "Referentni kod"
    ```cpp
    --8<-- "docs/graph/code/diff-constraints/diff-constraints_1.cpp"
    ```

### Primjer [P4926\[1007\] 倍杀测量者](https://www.luogu.com.cn/problem/P4926)

Ne razmatramo binarno pretraživanje i ostalo; ovdje opisujemo samo kako riješiti sustav oblika $\frac{x_i}{x_j}\leq c_k$.

Logaritmiranjem svakog $x_i,x_j$ i $c_k$ množenje pretvaramo u zbrajanje, tj. $\log x_i-\log x_j \leq \log c_k$, pa problem rješavamo kao sustav razlika.

## Implementacija provjere negativnog ciklusa Bellman–Fordom

Slijedi implementacija provjere postojanja negativnog ciklusa u grafu Bellman–Fordovim algoritmom; prije poziva osigurajte da je graf povezan.

???+ note "Implementacija"
    === "C++"
        ```cpp
        bool Bellman_Ford() {
          for (int i = 0; i < n; i++) {
            bool jud = false;
            for (int j = 1; j <= n; j++)
              for (int k = h[j]; ~k; k = nxt[k])
                if (dist[j] > dist[p[k]] + w[k])
                  dist[j] = dist[p[k]] + w[k], jud = true;
            if (!jud) break;
          }
          for (int i = 1; i <= n; i++)
            for (int j = h[i]; ~j; j = nxt[j])
              if (dist[i] > dist[p[j]] + w[j]) return false;
          return true;
        }
        ```
    
    === "Python"
        ```python
        def Bellman_Ford():
            for i in range(0, n):
                jud = False
                for j in range(1, n + 1):
                    while ~k:
                        k = h[j]
                        if dist[j] > dist[p[k]] + w[k]:
                            dist[j] = dist[p[k]] + w[k]
                            jud = True
                        k = nxt[k]
                if jud == False:
                    break
            for i in range(1, n + 1):
                while ~j:
                    j = h[i]
                    if dist[i] > dist[p[j]] + w[j]:
                        return False
                    j = nxt[j]
            return True
        ```

## Zadaci

[Usaco2006 Dec Wormholes](https://loj.ac/problem/10085)

[„SCOI2011” 糖果](https://loj.ac/problem/2436)

[POJ 1364 King](http://poj.org/problem?id=1364)

[POJ 2983 Is the Information Reliable?](http://poj.org/problem?id=2983)
