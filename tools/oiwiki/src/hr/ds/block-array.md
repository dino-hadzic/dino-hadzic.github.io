---
title: Blokovni niz
---

## Izgradnja blokovnog niza

Blokovni niz (block array) jest niz podijeljen na nekoliko blokova: informacije unutar bloka čuvaju se za blok kao cjelinu, a ako pri upitu na rubovima naiđemo na nepotpune blokove, njih obradimo izravno (brute force). Obično je duljina bloka $O(\sqrt{n})$. Detaljnu analizu možete pročitati u radu Xu Mingkuana „Uvod u algoritme dekompozicije s nestandardnom veličinom bloka” iz zbornika kineske nacionalne reprezentacije 2017.

Evo izravno jednog načina izgradnje blokovnog niza u kodu.

???+ note "Implementacija"
    ```cpp
    num = sqrt(n);
    for (int i = 1; i <= num; i++)
      st[i] = n / num * (i - 1) + 1, ed[i] = n / num * i;
    ed[num] = n;
    for (int i = 1; i <= num; i++) {
      for (int j = st[i]; j <= ed[i]; j++) {
        belong[j] = i;
      }
      size[i] = ed[i] - st[i] + 1;
    }
    ```

Pritom su `st[i]` i `ed[i]` početak i kraj bloka, a `size[i]` veličina bloka.

## Čuvanje i izmjena informacija unutar bloka

### Primjer 1: [Učiteljeva magija](https://www.luogu.com.cn/problem/P2801)

Dvije operacije:

1.  svakom broju na intervalu $[x,y]$ dodaj $z$;
2.  izbroji koliko je brojeva na intervalu $[x,y]$ većih ili jednakih $z$.

Treba nam broj elemenata unutar bloka koji su veći ili jednaki zadanom broju, pa nam treba niz `t` sa sortiranim elementima bloka, dok je `a` izvorni (nesortirani) niz. Za izmjene cijelih blokova koristimo pristup sličan trajnim oznakama (permanentni lazy tag): niz `delta` pamti vrijednost koja je trenutno dodana cijelom bloku. Ako je $q$ ukupan broj upita i izmjena, vremenska je složenost $O(q\sqrt{n}\log n)$.

Nizom `delta` pamtimo vrijednost pridruženu svakom bloku kao cjelini.

???+ note "Implementacija"
    ```cpp
    void Sort(int k) {
      for (int i = st[k]; i <= ed[k]; i++) t[i] = a[i];
      sort(t + st[k], t + ed[k] + 1);
    }
    
    void Modify(int l, int r, int c) {
      int x = belong[l], y = belong[r];
      if (x == y)  // ako je interval unutar jednog bloka, izmijeni izravno
      {
        for (int i = l; i <= r; i++) a[i] += c;
        Sort(x);
        return;
      }
      for (int i = l; i <= ed[x]; i++) a[i] += c;     // izravno izmijeni početni dio
      for (int i = st[y]; i <= r; i++) a[i] += c;     // izravno izmijeni završni dio
      for (int i = x + 1; i < y; i++) delta[i] += c;  // srednje blokove označi kao cjelinu
      Sort(x);
      Sort(y);
    }
    
    int Answer(int l, int r, int c) {
      int ans = 0, x = belong[l], y = belong[r];
      if (x == y) {
        for (int i = l; i <= r; i++)
          if (a[i] + delta[x] >= c) ans++;
        return ans;
      }
      for (int i = l; i <= ed[x]; i++)
        if (a[i] + delta[x] >= c) ans++;
      for (int i = st[y]; i <= r; i++)
        if (a[i] + delta[y] >= c) ans++;
      for (int i = x + 1; i <= y - 1; i++)
        ans +=
            ed[i] - (lower_bound(t + st[i], t + ed[i] + 1, c - delta[i]) - t) + 1;
      // lower_bound-om nađi položaj prvog broja većeg ili jednakog c u svakom srednjem potpunom bloku
      return ans;
    }
    ```

### Primjer 2: Arka hladne noći

Dvije operacije:

1.  svaki broj na intervalu $[x,y]$ postavi na $z$;
2.  izbroji koliko je brojeva na intervalu $[x,y]$ manjih ili jednakih $z$.

Nizom `delta` pamtimo na koju je vrijednost blok trenutno postavljen kao cjelina. Ako blok nije postavljen kao cjelina, to označavamo posebnom vrijednošću (npr. `0x3f3f3f3f3f3f3f3fll`). Za rubne blokove prije upita treba napraviti `pushdown`, tj. informaciju pohranjenu za blok spustiti na svaki broj. Nakon postavljanja ne zaboravite ponovno pozvati `sort`. Ostalo je kao u prethodnom zadatku.

???+ note "Implementacija"
    ```cpp
    void Sort(int k) {
      for (int i = st[k]; i <= ed[k]; i++) t[i] = a[i];
      sort(t + st[k], t + ed[k] + 1);
    }
    
    void PushDown(int x) {
      if (delta[x] != 0x3f3f3f3f3f3f3f3fll)  // tom vrijednošću označavamo da blok nije postavljen kao cjelina
        for (int i = st[x]; i <= ed[x]; i++) a[i] = t[i] = delta[x];
      delta[x] = 0x3f3f3f3f3f3f3f3fll;
    }
    
    void Modify(int l, int r, int c) {
      int x = belong[l], y = belong[r];
      PushDown(x);
      if (x == y) {
        for (int i = l; i <= r; i++) a[i] = c;
        Sort(x);
        return;
      }
      PushDown(y);
      for (int i = l; i <= ed[x]; i++) a[i] = c;
      for (int i = st[y]; i <= r; i++) a[i] = c;
      Sort(x);
      Sort(y);
      for (int i = x + 1; i < y; i++) delta[i] = c;
    }
    
    int Binary_Search(int l, int r, int c) {
      int ans = l - 1, mid;
      while (l <= r) {
        mid = (l + r) / 2;
        if (t[mid] <= c)
          ans = mid, l = mid + 1;
        else
          r = mid - 1;
      }
      return ans;
    }
    
    int Answer(int l, int r, int c) {
      int ans = 0, x = belong[l], y = belong[r];
      PushDown(x);
      if (x == y) {
        for (int i = l; i <= r; i++)
          if (a[i] <= c) ans++;
        return ans;
      }
      PushDown(y);
      for (int i = l; i <= ed[x]; i++)
        if (a[i] <= c) ans++;
      for (int i = st[y]; i <= r; i++)
        if (a[i] <= c) ans++;
      for (int i = x + 1; i <= y - 1; i++) {
        if (0x3f3f3f3f3f3f3f3fll == delta[i])
          ans += Binary_Search(st[i], ed[i], c) - st[i] + 1;
        else if (delta[i] <= c)
          ans += size[i];
      }
      return ans;
    }
    ```

## Vježba

1.  [Izmjena točke, upit na intervalu](https://loj.ac/problem/130)
2.  [Izmjena intervala, upit na intervalu](https://loj.ac/problem/132)
3.  [„Predložak” Segment tree 2](https://www.luogu.com.cn/problem/P3373)
4.  [„Ynoi2019 probno natjecanje” Yuno loves sqrt technology III](https://www.luogu.com.cn/problem/P5048)
5.  [„Violet” Maslačak](https://www.luogu.com.cn/problem/P4168)
6.  [Pisanje pjesama](https://www.luogu.com.cn/problem/P4135)
