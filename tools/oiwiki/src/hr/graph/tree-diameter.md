---
title: Promjer stabla
---

Najdulji jednostavni put između bilo koja dva čvora stabla naziva se „promjer” (diameter) stabla.

Predznanje: [Osnove stabala](./tree-basic.md).

## Uvod

Očito stablo može imati više promjera i svi su jednake duljine.

Promjer stabla može se izračunati u vremenu $O(n)$ dvama DFS-ovima ili DP-om na stablu.

## Dva DFS-a

Najprije iz proizvoljnog čvora $y$ pokrenemo prvi DFS i dođemo do njemu najudaljenijeg čvora, označimo ga $z$; zatim iz $z$ pokrenemo drugi DFS i dođemo do čvora najudaljenijeg od $z$, označimo ga $z'$. Tada je $\delta(z,z')$ promjer stabla.

Očito, ako je čvor $z$ do kojeg dolazi prvi DFS jedan kraj promjera, onda je čvor $z'$ do kojeg dolazi drugi DFS sigurno kraj promjera. Trebamo samo dokazati da je $z$ u svakom slučaju kraj promjera.

Teorem: u stablu, ako iz proizvoljnog čvora $y$ pokrenemo DFS, najudaljeniji čvor $z$ do kojeg dođemo nužno je kraj promjera.

???+ note "Dokaz"
    Dokazujemo kontradikcijom. Neka je polazni čvor $y$. Neka je pravi promjer $\delta(s,t)$, a čvor $z$ do kojeg dolazi prvi DFS iz $y$ kao najudaljeniji nije ni $t$ ni $s$. Razlikujemo tri slučaja:
    
    -   Ako $y$ leži na $\delta(s,t)$:
    
    ![y leži na s-t](./images/tree-diameter1.svg)
    
    Vrijedi $\delta(y,z) > \delta(y,t) \Longrightarrow \delta(x,z) > \delta(x,t) \Longrightarrow \delta(s,z) > \delta(s,t)$, što je u kontradikciji s time da je $\delta(s,t)$ najdulji jednostavni put između bilo koja dva čvora stabla.
    
    -   Ako $y$ ne leži na $\delta(s,t)$, a $\delta(y,z)$ i $\delta(s,t)$ imaju zajednički dio puta:
    
    ![y ne leži na s-t, y-z i s-t imaju zajednički dio puta](./images/tree-diameter2.svg)
    
    Vrijedi $\delta(y,z) > \delta(y,t) \Longrightarrow \delta(x,z) > \delta(x,t) \Longrightarrow \delta(s,z) > \delta(s,t)$, što je u kontradikciji s time da je $\delta(s,t)$ najdulji jednostavni put između bilo koja dva čvora stabla.
    
    -   Ako $y$ ne leži na $\delta(s,t)$, a $\delta(y,z)$ i $\delta(s,t)$ nemaju zajednički dio puta:
    
    ![y ne leži na s-t, y-z i s-t nemaju zajednički dio puta](./images/tree-diameter3.svg)
    
    Vrijedi $\delta(y,z) > \delta(y,t) \Longrightarrow \delta(x',z) > \delta(x',t) \Longrightarrow \delta(x,z) > \delta(x,t) \Longrightarrow \delta(s,z) > \delta(s,t)$, što je u kontradikciji s time da je $\delta(s,t)$ najdulji jednostavni put između bilo koja dva čvora stabla.
    
    Dakle, u sva tri slučaja pretpostavka vodi u kontradikciju, čime je teorem dokazan.

???+ warning "Bridovi negativne težine"
    Gornji dokaz pretpostavlja da nijedan put nema negativnu duljinu. Ako u stablu postoje bridovi negativne težine, dokaz ne vrijedi. Stoga se, ako postoje negativni bridovi, promjer ne može odrediti metodom dvaju DFS-ova.

Ako treba odrediti sve čvorove na nekom promjeru, tijekom drugog DFS-a možemo za svaki čvor zabilježiti prethodnika; tada od jednog kraja promjera idemo unatrag i prolazimo sve čvorove na promjeru.

## DP na stablu

### Metoda 1

Uzmemo $1$ za korijen stabla i za svaki čvor, kao korijen svog podstabla, zabilježimo duljinu najduljeg puta prema dolje $d_1$ i duljinu drugog najduljeg puta (bez zajedničkih bridova s najduljim) $d_2$. Promjer je tada najveća vrijednost koju $d_1 + d_2$ poprima po svim čvorovima.

DP na stablu može odrediti promjer i kad postoje bridovi negativne težine.

Ako treba odrediti sve čvorove na nekom promjeru, tijekom DP-a za svaki čvor zabilježimo dijete koje odgovara najduljem odnosno drugom najduljem putu prema dolje (definicije kao gore); pri računanju $d$ zapamtimo pripadni čvor $u$ za koji je $d = d_1[u] + d_2[u]$. Tada od $u$ redom slijedimo djecu koja odgovaraju najduljem i drugom najduljem putu u jednom smjeru (za nekorijensko stablo, iako smo ovdje odabrali $1$ za korijen, ipak treba bilježiti smjer skoka za svaki čvor; za korijensko stablo dovoljno je ići prema gore) i tako prođemo sve čvorove na promjeru.

### Metoda 2

Ovdje dajemo metodu DP-a na stablu koja koristi samo jedno polje.

Definiramo $dp[u]$ kao najdulji put koji polazi iz $u$ unutar podstabla s korijenom $u$. Lako se dobiva prijelaz: $dp[u] = \max(dp[u], dp[v] + w(u, v))$, gdje je $v$ dijete čvora $u$, a $w(u, v)$ težina prijeđenog brida.

Promjer stabla zapravo se može dobiti kao najveći zbroj dvaju različitih puteva koji polaze iz nekog čvora. Stoga je tijekom DP-a dovoljno, prije ažuriranja $dp[u]$, izračunati $d = \max(d, dp[u] + dp[v] + w(u, v))$, čime dobivamo promjer $d$.

## Primjer zadatka

???+ example "[Luogu B4016 Promjer stabla](https://www.luogu.com.cn/problem/B4016)"
    Zadano je stablo s $n$ čvorova; odredite duljinu njegova promjera. $1\leq n\leq 10^5$.

??? note "Primjer implementacije dvama DFS-ovima"
    ```cpp
    --8<-- "docs/graph/code/tree-diameter/tree-diameter_1.cpp"
    ```

??? note "Primjer implementacije DP-om na stablu s dva polja"
    ```cpp
    --8<-- "docs/graph/code/tree-diameter/tree-diameter_2.cpp"
    ```

??? note "Primjer implementacije DP-om na stablu s jednim poljem"
    ```cpp
    --8<-- "docs/graph/code/tree-diameter/tree-diameter_3.cpp"
    ```

## Svojstva

Promjer stabla ima sljedeće svojstvo: ako su sve težine bridova u stablu pozitivne, polovišta svih promjera stabla se podudaraju.

???+ note "Dokaz"
    Dokaz: kontradikcijom. Neka su dva promjera s različitim polovištima $\delta(s,t)$ i $\delta(s',t')$, s polovištima $x$ odnosno $x'$. Očito je $\delta(s,x) = \delta(x,t) = \delta(s',x') = \delta(x',t')$.
    
    ![polovišta svih promjera stabla bez negativnih bridova se podudaraju](./images/tree-diameter4.svg)
    
    Vrijedi $\delta(s,t') = \delta(s,x) + \delta(x,x') + \delta(x',t') > \delta(s,x) + \delta(x,t) = \delta(s,t)$, što je u kontradikciji s time da je $\delta(s,t)$ najdulji jednostavni put između bilo koja dva čvora stabla; time je svojstvo dokazano.

## Zadaci za vježbu

-   [CodeChef, Diameter of Tree](https://www.codechef.com/problems/DTREE)
-   [Educational Codeforces Round 35, Problem F, Tree Destruction](https://codeforces.com/contest/911/problem/F)
-   [ZOJ 3820 Building Fire Stations](https://pintia.cn/problem-sets/91827364500/exam/problems/type/7?problemSetProblemId=91827369872&page=28)
-   [CEOI2019/CodeForces 1192B. Dynamic Diameter](https://codeforces.com/contest/1192/problem/B)
-   [ICPC 2019 Shanghai online contest, Lightning Routing I](https://vjudge.net/problem/%E8%AE%A1%E8%92%9C%E5%AE%A2-A2290)
-   [NOIP2007 senior, Jezgra mreže stabla](https://www.luogu.com.cn/problem/P1099)
-   [SDOI2011 Vatrogasci](https://www.luogu.com.cn/problem/P2491)
-   [APIO2010 Patrola](https://www.luogu.com.cn/problem/P3629)
