---
title: Središte stabla
---

## Definicija

Ako je u stablu, kada čvor $x$ uzmemo kao korijen, najdulji lanac koji polazi iz $x$ najkraći mogući, čvor $x$ nazivamo središtem (center) stabla.

## Svojstva

-   Središte stabla nije nužno jedinstveno, ali ih ima najviše $2$ i ta su dva središta susjedna.
-   Središte stabla uvijek leži na promjeru stabla.
-   Putevi od svakog čvora stabla do njemu najudaljenijeg čvora svi prolaze kroz središte stabla.
-   Kada je središte stabla korijen, dva lanca od njega do krajeva promjera upravo su najdulji i drugi najdulji lanac.
-   Kada dva stabla spajamo jednim bridom u jedno stablo, spajanje njihovih središta daje novo stablo najmanjeg promjera.
-   Udaljenost od središta stabla do bilo kojeg drugog čvora ne premašuje polovinu promjera stabla.

## Postupak

Tražimo čvor $x$ takav da je, kada ga uzmemo kao korijen, duljina najduljeg lanca najmanja.

### Koraci

1.  Održavamo $len1_x$, najdulji lanac unutar podstabla čvora $x$.
2.  Održavamo $len2_x$, najdulji lanac koji se ne preklapa s $len1_x$.
3.  Održavamo $up_x$, najdulji lanac izvan podstabla čvora $x$; taj lanac nužno prolazi kroz roditelja čvora $x$.
4.  Pronađemo čvor $x$ za koji je $\max(len1_x, up_x)$ najmanji; taj je $x$ središte stabla.

???+ note "Primjer koda"
    ```cpp
    // ovaj kôd pretpostavlja da su čvorovi numerirani od 1, tj. i ∈ [1,n], a graf se pohranjuje vectorom
    int d1[N], d2[N], up[N], x, y, mini = 1e9;  // d1,d2 odgovaraju len1,len2 iz teksta
    
    struct node {
      int to, val;  // to je čvor u koji brid vodi, val je težina brida
    };
    
    vector<node> nbr[N];
    
    void dfsd(int cur, int fa) {  // računa len1 i len2
      for (node nxtn : nbr[cur]) {
        int nxt = nxtn.to, w = nxtn.val;  // nxt je čvor u koji ovaj brid vodi, val je težina brida
        if (nxt == fa) {
          continue;
        }
        dfsd(nxt, cur);
        if (d1[nxt] + w > d1[cur]) {  // možemo ažurirati najdulji lanac
          d2[cur] = d1[cur];
          d1[cur] = d1[nxt] + w;
        } else if (d1[nxt] + w > d2[cur]) {  // ne možemo ažurirati najdulji, ali možemo drugi najdulji lanac
          d2[cur] = d1[nxt] + w;
        }
      }
    }
    
    void dfsu(int cur, int fa) {
      for (node nxtn : nbr[cur]) {
        int nxt = nxtn.to, w = nxtn.val;
        if (nxt == fa) {
          continue;
        }
        up[nxt] = up[cur] + w;
        if (d1[nxt] + w != d1[cur]) {  // ako najdulji lanac u vlastitom podstablu nije u podstablu od nxt
          up[nxt] = max(up[nxt], d1[cur] + w);
        } else {  // najdulji lanac u vlastitom podstablu jest u podstablu od nxt, smijemo koristiti samo drugi najdulji
          up[nxt] = max(up[nxt], d2[cur] + w);
        }
        dfsu(nxt, cur);
      }
    }
    
    void GetTreeCenter() {  // određuje središta stabla, označena x i y (ako postoji)
      dfsd(1, 0);
      dfsu(1, 0);
      for (int i = 1; i <= n; i++) {
        if (max(d1[i], up[i]) < mini) {  // pronađen čvor s trenutačno najmanjim max(len1[x],up[x])
          mini = max(d1[i], up[i]);
          x = i;
          y = 0;
        } else if (max(d1[i], up[i]) == mini) {  // drugo središte
          y = i;
        }
      }
    }
    ```

### Primjer

Pretpostavimo da imamo sljedeće stablo:

```text
           A
          / \
         B   C
        / \   \
       D   E   F
```

-   Promjer stabla je $D \rightarrow B \rightarrow A \rightarrow C \rightarrow F$. Duljina promjera je $4$.
-   Središte stabla je čvor $A$, jer najdulji lanci iz $A$ (do $D$ ili do $F$) oba imaju duljinu $2$.
-   Ako bismo $B$ ili $C$ uzeli kao korijen, najdulji lanac iz tih čvorova bio bi dulji, pa oni nisu središte stabla.

### Vremenska složenost

Vremenska složenost gornjeg algoritma je $O(n)$, gdje je $n$ broj čvorova u stablu.

## Literatura

-   [TutorialsPoint: Centers of a Tree](https://www.tutorialspoint.com/centers-of-a-tree)
-   [ProofWiki: Definition of Center of Tree](https://proofwiki.org/wiki/Definition:Center_of_Tree)
-   [Wikipedia: Tree (graph theory)](https://en.wikipedia.org/wiki/Tree_%28graph_theory%29#Properties)
