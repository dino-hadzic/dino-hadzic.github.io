---
title: Slučajna šetnja po stablu
---

Zadano je korijensko stablo; na nekom vrhu stabla nalazi se novčić koji se u svakom trenutku s jednakom vjerojatnošću pomiče na susjedni vrh. Pitamo se kolika je očekivana udaljenost koju novčić prijeđe do susjednog vrha.

## Potrebne definicije

-   $T=(V,E)$: stablo koje promatramo
-   $d(u)$: stupanj vrha $u$
-   $w(u,v)$: težina brida između vrhova $u$ i $v$
-   $p_u$: roditelj vrha $u$
-   $\textit{root}$: korijen stabla
-   $\textit{son}_u$: skup djece vrha $u$
-   $\textit{sibling}_u$: skup braće vrha $u$

## Očekivana udaljenost do roditelja

Neka $f(u)$ označava očekivanu udaljenost koju treba prijeći od vrha $u$ do njegova roditelja $p_u$. Tada je:

$$
f(u) = \cfrac{w(u,p_u) + \sum\limits_{v \in \textit{son}_u}(w(u,v) + f(v) + f(u))}{d(u)}
$$

Prvi dio brojnika odgovara izravnom odlasku u roditelja, a drugi dio odlasku u dijete, povratku iz djeteta i tek onda odlasku u roditelja; nazivnik $d(u)$ znači da iz vrha $u$ u svaki susjedni vrh idemo s jednakom vjerojatnošću.

Pojednostavnimo:

$$
\begin{aligned}
    f(u) &= \cfrac{w(u,p_u) + \sum\limits_{v \in \textit{son}_u}(w(u,v) + f(v) + f(u))}{d(u)} \\
         &= \cfrac{w(u,p_u) + \sum\limits_{v \in \textit{son}_u}(w(u,v) + f(v)) + (d(u)-1)f(u)}{d(u)} \\
         &= w(u,p_u) + \sum\limits_{v \in \textit{son}_u}(w(u,v) + f(v)) \\
         &= \sum\limits_{(u,t) \in E}w(u,t) + \sum\limits_{v \in \textit{son}_u}f(v)
\end{aligned}
$$

Za list $l$ početno je stanje $f(l) = w(p_l, l)$.

Kad su sve težine bridova u stablu jednake $1$, gornja se formula svodi na:

$$
f(u) = d(u) + \sum\limits_{v \in \textit{son}_u}f(v)
$$

tj. zbroj stupnjeva svih vrhova podstabla vrha $u$, što je dvostruka veličina podstabla vrha $u$ $-1$ (svaki vrh ima točno jedan brid prema roditelju; osim brida između $u$ i $p_u$, koji pridonosi samo $1$ stupanj, svaki brid pridonosi $2$ stupnja).

## Očekivana udaljenost do djeteta

Neka $g(u)$ označava očekivanu udaljenost koju treba prijeći od vrha $p_u$ do njegova djeteta $u$. Tada je:

$$
g(u) = \cfrac{w(p_u,u) + \left(w(p_u,p_{p_u})+g(p_u)+g(u)\right) + \sum\limits_{s \in \textit{sibling}_u}(w(p_u,s)+f(s)+g(u))}{d(p_u)}
$$

Prvi dio brojnika odgovara izravnom odlasku u dijete $u$; drugi dio odlasku u roditelja, povratku iz roditelja i tek onda odlasku u $u$; treći dio odlasku u brata vrha $u$, povratku iz njega i tek onda odlasku u $u$. Nazivnik $d(p_u)$ znači da iz vrha $p_u$ u svaki susjedni vrh idemo s jednakom vjerojatnošću.

Pojednostavnimo:

$$
\begin{aligned}
    g(u) &= \cfrac{w(p_u,u) + \left(w(p_u,p_{p_u})+g(p_u)+g(u)\right) + \sum\limits_{s \in \textit{sibling}_u}(w(p_u,s)+f(s)+g(u))}{d(p_u)} \\
         &= \cfrac{w(p_u,u) + w(p_u,p_{p_u}) + g(p_u) + \sum\limits_{s \in \textit{sibling}_u}\left(w(p_u,s)+f(s)\right)+(d(p_u)-1)g(u)}{d(p_u)} \\
         &= w(p_u,u) + w(p_u,p_{p_u}) + g(p_u) + \sum\limits_{s \in \textit{sibling}_u}(w(p_u,s)+f(s)) \\
         &= \sum\limits_{(p_u,t) \in E}w(p_u,t) + g(p_u) + \sum\limits_{s \in \textit{sibling}_u}f(s) \\
         &= \sum\limits_{(p_u,t) \in E}w(p_u,t) + g(p_u) + \left(f(p_u)-\sum\limits_{(p_u,t) \in E}w(p_u,t)-f(u)\right) \\
         &= g(p_u) + f(p_u) - f(u)
\end{aligned}
$$

Početno je stanje $g(\text{root}) = 0$.

## Implementacija (na primjeru netežinskog stabla)

```cpp
vector<int> G[MAXN];

void dfs1(int u, int p) {
  f[u] = G[u].size();
  for (auto v : G[u]) {
    if (v == p) continue;
    dfs1(v, u);
    f[u] += f[v];
  }
}

void dfs2(int u, int p) {
  if (u != root) g[u] = g[p] + f[p] - f[u];
  for (auto v : G[u]) {
    if (v == p) continue;
    dfs2(v, u);
  }
}
```
