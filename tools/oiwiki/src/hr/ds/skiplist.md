---
title: Skip list
---

Skip list (lista s preskakanjem) struktura je podataka za pretraživanje koju je izumio William Pugh. Podržava brzo pretraživanje, umetanje i brisanje podataka.

Očekivana prostorna složenost skip liste je $O(n)$, a očekivana vremenska složenost pretraživanja, umetanja i brisanja je $O(\log n)$.

## Osnovna ideja

Kao što ime sugerira, skip list je struktura podataka slična povezanom popisu. Točnije, ona je poboljšanje uređenog povezanog popisa.

Radi jednostavnosti, u nastavku pretpostavljamo da su svi uređeni povezani popisi sortirani **uzlazno**.

Pretraživanje uređenog povezanog popisa počinje od početka i uspoređuje čvorove jedan po jedan dok vrijednost trenutačnog čvora ne postane veća ili jednaka traženoj vrijednosti. Očito je složenost te operacije $O(n)$.

Skip list uređenom povezanom popisu dodaje pojam **razina**. Svaka razina skip liste uređeni je povezani popis, a najniža razina izvorni je uređeni povezani popis. Svaki čvor na razini $i$ pojavljuje se na razini $i+1$ s vjerojatnošću $p$, gdje je $p$ konstanta.

U skip listi s $n$ čvorova označimo s $L(n)$ razinu koja očekivano sadrži $\frac{1}{p}$ elemenata. Lako dobivamo $L(n) = \log_{\frac{1}{p}}n$.

Pretraživanje skip liste počinje na razini $L(n)$. Vodoravno uspoređujemo čvorove dok sljedeći čvor ne postane veći ili jednak traženom, a zatim se spuštamo za jednu razinu. Ponavljamo dok ne dođemo do prve razine i više ne možemo nastaviti. Ako je tada sljedeći čvor traženi čvor, pretraživanje je uspjelo; inače element ne postoji. Tako preskačemo nepotrebne usporedbe, pa je pretraživanje skip liste brže od pretraživanja uređenog povezanog popisa. Može se dokazati da je prosječna složenost pretraživanja $O(\log n)$.

## Dokaz složenosti

### Prostorna složenost

Za pojedini čvor vjerojatnost da mu je najviša razina $i$ iznosi $p^{i-1}(1 - p)$. Zato je očekivani broj razina skip liste $\sum_{i\ge 1} ip^{i - 1}(1-p) = \frac{1}{1 - p}$. Budući da je $p$ konstanta, **očekivana prostorna složenost** skip liste je $O(n)$.

U najgorem slučaju uređeni popis na svakoj razini jednak je izvornom uređenom popisu, pa je **najgora prostorna složenost** skip liste $O(n \log n)$.

### Vremenska složenost

Analizirajmo put pretraživanja unatrag. Postupak dijelimo na uspon od najniže razine do razine $L(n)$ i preostale korake. Pretpostavljamo da detalji o čvoru nisu poznati dok ga ne posjetimo.

Pretpostavimo da smo trenutačno na razini $i$ u čvoru $x$. Ne znamo najvišu razinu čvora $x$ ni čvorova lijevo od čvora $x$; znamo samo da je najviša razina čvora $x$ barem $i$. Ako je najviša razina čvora $x$ veća od $i$, sljedeći korak ide prema gore, što se događa s vjerojatnošću $p$. Ako je najviša razina čvora $x$ jednaka $i$, sljedeći korak ide ulijevo, što se događa s vjerojatnošću $1-p$.

Neka je $C(i)$ očekivani trošak uspona za $i$ razina u beskonačno dugoj skip listi. Tada vrijedi:

$$
\begin{aligned}
C(0) & = 0 \\
C(i) & = (1-p)(1+C(i)) + p(1+C(i-1))
\end{aligned}
$$

Rješavanjem dobivamo $C(i)=\frac{i}{p}$.

Slijedi da je u skip listi duljine $n$ očekivani broj koraka od najniže razine do razine $L(n)$ odozgo omeđen s $\frac{L(n) - 1}{p}$.

Preostaje analizirati koliko je još koraka potrebno nakon dolaska na razinu $L(n)$. Nakon dolaska na razinu $L(n)$ broj koraka ulijevo ne prelazi ukupan broj čvorova na razini $L(n)$ i višim razinama, čije je očekivanje $\frac{1}{p}$. Zato je očekivani broj koraka ulijevo nakon dolaska na razinu $L(n)$ odozgo omeđen s $\frac{1}{p}$. Slično je i očekivani broj koraka prema gore nakon dolaska na razinu $L(n)$ odozgo omeđen s $\frac{1}{p}$.

Stoga je očekivani broj koraka pretraživanja $\frac{L(n) - 1}{p} + \frac{2}{p}$. Budući da je $L(n)=\log_{\frac{1}{p}}n$, **očekivana vremenska složenost** pretraživanja skip liste je $O(\log n)$.

U najgorem slučaju uređeni popis na svakoj razini jednak je izvornom popisu. Pretraživanje tada odgovara pretraživanju uređenog popisa na najvišoj razini, pa je **najgora vremenska složenost** pretraživanja skip liste $O(n)$.

Umetanje i brisanje prolaze postupak pretraživanja, pritom bilježe čvorove koje treba promijeniti i na kraju provode izmjene. Na svakoj razini treba promijeniti najviše jedan čvor. Budući da je očekivani broj razina skip liste $\log_{\frac{1}{p}}n$, i **očekivana vremenska složenost** umetanja i izmjene je $O(\log n)$.

## Implementacija

### Određivanje najviše razine čvora

Simuliramo dodavanje još jedne razine s vjerojatnošću $p$, a na kraju uzimamo minimum dobivenog broja i gornje granice.

```cpp
int randomLevel() {
  int lv = 1;
  // MAXL = 32, S = 0xFFFF, PS = S * P, P = 1 / 4
  while ((rand() & S) < PS) ++lv;
  return min(MAXL, lv);
}
```

### Pretraživanje

Provjeravamo postoji li u skip listi čvor s ključem `key`. U implementaciji možemo postaviti dva stražarska čvora kako bismo smanjili broj rubnih slučajeva.

```cpp
V& find(const K& key) {
  SkipListNode<K, V>* p = head;

  // Pronađi posljednji čvor na ovoj razini s ključem manjim od key, pa se spusti
  for (int i = level; i >= 0; --i) {
    while (p->forward[i]->key < key) {
      p = p->forward[i];
    }
  }
  // Trenutačni je ključ još manji, pa treba još jedan korak naprijed
  p = p->forward[0];

  // Čvor je pronađen
  if (p->key == key) return p->value;

  // Čvor ne postoji, vrati INVALID
  return tail->value;
}
```

### Umetanje

Umećemo čvor `(key, value)`. Najprije provodimo pretraživanje i pritom bilježimo nakon kojih čvorova treba umetnuti novi čvor, a zatim ga umećemo. Na svakoj razini treba promijeniti posljednji čvor s ključem manjim od `key`.

```cpp
void insert(const K &key, const V &value) {
  // Bilježi čvorove koje treba promijeniti
  SkipListNode<K, V> *update[MAXL + 1];

  SkipListNode<K, V> *p = head;
  for (int i = level; i >= 0; --i) {
    while (p->forward[i]->key < key) {
      p = p->forward[i];
    }
    // Na razini i treba promijeniti čvor p
    update[i] = p;
  }
  p = p->forward[0];

  // Ako čvor već postoji, promijeni mu vrijednost
  if (p->key == key) {
    p->value = value;
    return;
  }

  // Odredi najvišu razinu novog čvora
  int lv = randomLevel();
  if (lv > level) {
    lv = ++level;
    update[lv] = head;
  }

  // Stvori novi čvor
  SkipListNode<K, V> *newNode = new SkipListNode<K, V>(key, value, lv);
  // Umetni novi čvor na razinama 0~lv
  for (int i = lv; i >= 0; --i) {
    p = update[i];
    newNode->forward[i] = p->forward[i];
    p->forward[i] = newNode;
  }

  ++length;
}
```

### Brisanje

Brišemo čvor s ključem `key`. Najprije provodimo pretraživanje i pritom bilježimo nakon kojih se čvorova nalazi čvor koji brišemo, a zatim ga brišemo. Na svakoj razini treba promijeniti posljednji čvor s ključem manjim od `key`.

```cpp
bool erase(const K &key) {
  // Bilježi čvorove koje treba promijeniti
  SkipListNode<K, V> *update[MAXL + 1];

  SkipListNode<K, V> *p = head;
  for (int i = level; i >= 0; --i) {
    while (p->forward[i]->key < key) {
      p = p->forward[i];
    }
    // Na razini i treba promijeniti čvor p
    update[i] = p;
  }
  p = p->forward[0];

  // Čvor ne postoji
  if (p->key != key) return false;

  // Počni brisanje od najniže razine
  for (int i = 0; i <= level; ++i) {
    // Ako na ovoj razini nema p, brisanje je gotovo
    if (update[i]->forward[i] != p) {
      break;
    }
    // Prekini vezu prema p
    update[i]->forward[i] = p->forward[i];
  }

  // Oslobodi memoriju
  delete p;

  // Brisanje čvora može smanjiti najvišu razinu
  while (level > 0 && head->forward[level] == tail) --level;

  // Duljina skip liste
  --length;
  return true;
}
```

### Potpuni kod

Sljedeći kod implementira mapu pomoću skip liste. Nije temeljito testiran i služi samo kao referenca.

??? note "Referentni kod"
    ```cpp
    #include <cassert>
    #include <climits>
    #include <ctime>
    #include <iostream>
    #include <map>
    using namespace std;
    
    template <typename K, typename V>
    struct SkipListNode {
      int level;
      K key;
      V value;
      SkipListNode **forward;
    
      SkipListNode() {}
    
      SkipListNode(K k, V v, int l, SkipListNode *nxt = NULL) {
        key = k;
        value = v;
        level = l;
        forward = new SkipListNode *[l + 1];
        for (int i = 0; i <= l; ++i) forward[i] = nxt;
      }
    
      ~SkipListNode() {
        if (forward != NULL) delete[] forward;
      }
    };
    
    template <typename K, typename V>
    struct SkipList {
      static constexpr int MAXL = 32;
      static constexpr int P = 4;
      static constexpr int S = 0xFFFF;
      static constexpr int PS = S / P;
      static constexpr int INVALID = INT_MAX;
    
      SkipListNode<K, V> *head, *tail;
      int length;
      int level;
    
      SkipList() {
        srand(time(nullptr));
    
        level = length = 0;
        tail = new SkipListNode<K, V>(INVALID, 0, 0);
        head = new SkipListNode<K, V>(INVALID, 0, MAXL, tail);
      }
    
      ~SkipList() {
        delete head;
        delete tail;
      }
    
      int randomLevel() {
        int lv = 1;
        while ((rand() & S) < PS) ++lv;
        return MAXL > lv ? lv : MAXL;
      }
    
      void insert(const K &key, const V &value) {
        SkipListNode<K, V> *update[MAXL + 1];
    
        SkipListNode<K, V> *p = head;
        for (int i = level; i >= 0; --i) {
          while (p->forward[i]->key < key) {
            p = p->forward[i];
          }
          update[i] = p;
        }
        p = p->forward[0];
    
        if (p->key == key) {
          p->value = value;
          return;
        }
    
        int lv = randomLevel();
        if (lv > level) {
          lv = ++level;
          update[lv] = head;
        }
    
        SkipListNode<K, V> *newNode = new SkipListNode<K, V>(key, value, lv);
        for (int i = lv; i >= 0; --i) {
          p = update[i];
          newNode->forward[i] = p->forward[i];
          p->forward[i] = newNode;
        }
    
        ++length;
      }
    
      bool erase(const K &key) {
        SkipListNode<K, V> *update[MAXL + 1];
        SkipListNode<K, V> *p = head;
    
        for (int i = level; i >= 0; --i) {
          while (p->forward[i]->key < key) {
            p = p->forward[i];
          }
          update[i] = p;
        }
        p = p->forward[0];
    
        if (p->key != key) return false;
    
        for (int i = 0; i <= level; ++i) {
          if (update[i]->forward[i] != p) {
            break;
          }
          update[i]->forward[i] = p->forward[i];
        }
    
        delete p;
    
        while (level > 0 && head->forward[level] == tail) --level;
        --length;
        return true;
      }
    
      V &operator[](const K &key) {
        V v = find(key);
        if (v == tail->value) insert(key, 0);
        return find(key);
      }
    
      V &find(const K &key) {
        SkipListNode<K, V> *p = head;
        for (int i = level; i >= 0; --i) {
          while (p->forward[i]->key < key) {
            p = p->forward[i];
          }
        }
        p = p->forward[0];
        if (p->key == key) return p->value;
        return tail->value;
      }
    
      bool count(const K &key) { return find(key) != tail->value; }
    };
    
    int main() {
      SkipList<int, int> L;
      map<int, int> M;
    
      clock_t s = clock();
    
      for (int i = 0; i < 1e5; ++i) {
        int key = rand(), value = rand();
        L[key] = value;
        M[key] = value;
      }
    
      for (int i = 0; i < 1e5; ++i) {
        int key = rand();
        if (i & 1) {
          L.erase(key);
          M.erase(key);
        } else {
          int r1 = L.count(key) ? L[key] : 0;
          int r2 = M.count(key) ? M[key] : 0;
          assert(r1 == r2);
        }
      }
    
      clock_t e = clock();
      cout << "Time elapsed: " << (double)(e - s) / CLOCKS_PER_SEC << endl;
      // oko 0,2 s
    
      return 0;
    }
    ```

## Optimizacija pristupa po indeksu u skip listi

Pristup $k$-tom čvoru skip liste jednak je pristupu $k$-tom čvoru izvornog uređenog povezanog popisa. Očito je vremenska složenost te operacije $O(n)$, što nije dovoljno dobro.

Pristup po indeksu optimiziramo tako da uz svaki pokazivač prema naprijed održavamo i njegovu duljinu. Neka su $A$ i $B$ čvorovi skip liste, pri čemu je $A$ čvor na položaju $a$, a $B$ čvor na položaju $b$ $(a < b)$. Ako na nekoj razini pokazivač čvora $A$ pokazuje na $B$, duljina tog pokazivača iznosi $b - a$.

Sada za pristup $k$-tom čvoru krećemo s najviše razine i vodoravno obilazimo njezin popis dok zbroj položaja trenutačnog čvora i duljine njegova pokazivača na toj razini ne postane veći ili jednak $k$, pa se spuštamo za jednu razinu. Ponavljamo dok ne dođemo do prve razine i više ne možemo nastaviti. Tada je trenutačni čvor upravo $k$-ti čvor skip liste.

Tako možemo brzo pristupiti $k$-tom elementu skip liste. Može se dokazati da je vremenska složenost te operacije $O(\log n)$.

## Literatura

1.  [Skip Lists: A Probabilistic Alternative to Balanced Trees](https://15721.courses.cs.cmu.edu/spring2018/papers/08-oltpindexes1/pugh-skiplists-cacm1990.pdf)
2.  [Skip List](https://en.wikipedia.org/wiki/Skip_list)
3.  [A Skip List Cookbook](http://cglab.ca/~morin/teaching/5408/refs/p90b.pdf)
