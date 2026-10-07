---
title: DFS (pretraživanje)
---

## Uvod

DFS je pojam iz teorije grafova, vidi stranicu [DFS (teorija grafova)](../graph/dfs.md). U **algoritmima pretraživanja** taj naziv često označava algoritam koji rekurzivnom funkcijom jednostavno ostvaruje iscrpno nabrajanje (brute force); on je donekle sličan DFS-u iz teorije grafova, ali nije posve isti.

## Objašnjenje

Razmotrimo ovaj primjer:

???+ note "Primjer"
    Rastavite prirodan broj $n$ na zbroj $3$ prirodnih brojeva, npr. $6=1+2+3$, pri čemu svaki sljedeći broj mora biti veći ili jednak prethodnome. Ispišite sve načine.

Kako bismo riješili ovaj zadatak da ne znamo za pretraživanje? Naravno, trostrukom petljom; primjer koda:

???+ note "Implementacija"
    === "C++"
        ```cpp
        for (int i = 1; i <= n; ++i)
          for (int j = i; j <= n; ++j)
            for (int k = j; k <= n; ++k)
              if (i + j + k == n) printf("%d = %d + %d + %d\n", n, i, j, k);
        ```
    
    === "Python"
        ```python
        for i in range(1, n + 1):
            for j in range(i, n + 1):
                for k in range(j, n + 1):
                    if i + j + k == n:
                        print("%d = %d + %d + %d" % (n, i, j, k))
        ```
    
    === "Java"
        ```Java
        for (int i = 1; i < n + 1; i++) {
            for (int j = i; j < n + 1; j++) {
                for (int k = j; k < n + 1; k++) {
                    if (i + j + k == n) System.out.printf("%d = %d + %d + %d%n", n, i, j, k);
                }
            }
        }
        ```

A što ako treba rastaviti na četiri broja? Dodati još jednu petlju? A ako treba rastaviti na najviše $m$ brojeva?

Tada nam treba rekurzivno pretraživanje. Osobitost je ove vrste algoritama da se cilj pretraživanja dijeli na nekoliko „razina”; na svakoj razini odluka se donosi na temelju stanja prethodnih razina, sve dok se ne dosegne ciljno stanje.

Razmotrimo gornji zadatak: prirodan broj $n$ treba rastaviti na zbroj najviše $m$ prirodnih brojeva tako da svaki sljedeći broj bude veći ili jednak prethodnome, i ispisati sve načine.

Neka jedan način rastavlja prirodan broj $n$ na zbroj $k$ prirodnih brojeva $a_1, a_2, \ldots, a_k$. Podijelimo problem na razine: na $i$-toj razini odlučuje se o $a_i$. Da bismo donijeli odluku na $i$-toj razini, trebamo pamtiti tri varijable stanja: $n-\sum_{j=1}^i{a_j}$, zbroj svih preostalih brojeva; $a_{i-1}$, broj s prethodne razine, koji osigurava da brojevi ne padaju; i $i$, koji osigurava da ispišemo najviše $m$ brojeva. Način zapisujemo u niz `arr`, čiji je $i$-ti element $a_i$. Uočimo da je `arr` zapravo stog duljine $i$.

Kod je sljedeći:

???+ note "Implementacija"
    === "C++"
        ```cpp
        int m, arr[103];  // arr pamti trenutni način
        
        void dfs(int n, int i, int a) {
          if (n == 0) {
            for (int j = 1; j <= i - 1; ++j) printf("%d ", arr[j]);
            printf("\n");
          }
          if (i <= m) {
            for (int j = a; j <= n; ++j) {
              arr[i] = j;
              dfs(n - j, i + 1, j);  // Dobro razmislite što znači ovaj redak.
            }
          }
        }
        
        // glavni program
        scanf("%d%d", &n, &m);
        dfs(n, 1, 1);
        ```
    
    === "Python"
        ```python
        arr = [0] * 103  # arr pamti trenutni način
        
        
        def dfs(n, i, a):
            if n == 0:
                print(arr[1:i])
            if i <= m:
                for j in range(a, n + 1):
                    arr[i] = j
                    dfs(n - j, i + 1, j)  # Dobro razmislite što znači ovaj redak.
        
        
        # glavni program
        n, m = map(int, input().split())
        dfs(n, 1, 1)
        ```
    
    === "Java"
        ```Java
        static int m;
        
        // arr pamti trenutni način
        static int[] arr = new int[103];
        
        public static void dfs(int n, int i, int a) {
            if (n == 0) {
                for (int j = 1; j <= i - 1; j++) System.out.printf("%d ", arr[j]);
                System.out.println();
            }
            if (i <= m) {
                for (int j = a; j <= n; ++j) {
                    arr[i] = j;
                    dfs(n - j, i + 1, j); // Dobro razmislite što znači ovaj redak.
                }
            }
        }
        
        // glavni program
        final int N = new Scanner(System.in).nextInt();
        m = new Scanner(System.in).nextInt();
        dfs(N, 1, 1);
        ```

## Riješeni primjer

???+ note "[Luogu P1706 Sve permutacije](https://www.luogu.com.cn/problem/P1706)"
    ```cpp
    --8<-- "docs/search/code/dfs/dfs_1.cpp"
    ```
