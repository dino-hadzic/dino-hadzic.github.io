---
title: Randomizirani inkrementalni algoritam
---

## Uvod

Randomizirani inkrementalni algoritam važan je algoritam računalne geometrije: ne zahtijeva mnogo teorijskog znanja, ima nisku vremensku složenost i širok raspon primjena.

Ideja inkrementalnog algoritma (incremental algorithm) slična je prvom načelu matematičke indukcije; u biti se problem svodi na potproblem točno za jednu razinu manji. Nakon što riješimo potproblem, dodajemo trenutačni objekt. Zapisano kao rekurzija:

$$
T(n)=T(n-1)+g(n)
$$

Inkrementalni je algoritam jednostavna oblika i može se primijeniti na mnoge geometrijske zadatke.

Inkrementalni se algoritam često kombinira s randomizacijom, čime dobivamo randomizirani inkrementalni algoritam.

Ideja randomiziranog inkrementalnog algoritma glasi: pri svakom dodavanju novog objekta, ako se odgovor promijeni, lokalno ga ponovno izračunamo. Zato randomizirani inkrementalni algoritam obično zahtijeva da se lako i brzo može provjeriti mijenja li dodavanje elementa odgovor te da je u slučajnom redoslijedu očekivani broj promjena odgovora malen.

Randomizirani inkrementalni algoritam često se koristi za rješavanje problema [najmanje obuhvatne kružnice](smallest-enclosing-circle.md), a može se primijeniti i na presjek poluprostora, konveksnu ljusku u višim dimenzijama, randomiziranu Delaunayjevu triangulaciju i druge probleme.

## Zadaci za vježbu

[最小圆覆盖 (Najmanja obuhvatna kružnica)](https://www.luogu.com.cn/problem/P1742)

[「HNOI2012」射箭 (Streličarstvo)](https://www.luogu.com.cn/problem/P3222)

[CodeForces 442E](https://codeforces.com/problemset/problem/442/E)

## Literatura i dodatno štivo

[随机增量算法 (Randomizirani inkrementalni algoritam) – Xie Yilun](https://github.com/hzwer/shareOI/blob/master/%E8%AE%A1%E7%AE%97%E5%87%A0%E4%BD%95/%E9%9A%8F%E6%9C%BA%E5%A2%9E%E9%87%8F%E7%AE%97%E6%B3%95_%E8%A7%A3%E8%BD%B6%E4%BC%A6.pdf)

<https://www.cnblogs.com/aininot260/p/9635757.html>

<https://blog.csdn.net/u014609452/article/details/62039612>

[随机 Delaunay 三角剖分 (Randomizirana Delaunayjeva triangulacija)](https://zhuanlan.zhihu.com/p/364390356)
