---
title: Hash tablica
---

## Uvod

![](images/hashtable.svg)

Hash tablica (hash table, raspršena tablica) struktura je podataka koja podatke pohranjuje u obliku parova „ključ–vrijednost” (key-value). Pohrana u obliku „ključ–vrijednost” znači da svaki ključ (key) jednoznačno odgovara nekom mjestu u memoriji. Dovoljno je zadati ključ koji tražimo da bismo brzo pronašli pripadnu vrijednost (value). Hash tablicu možemo shvatiti kao napredniji niz čiji indeksi mogu biti vrlo veliki cijeli brojevi, realni brojevi, stringovi, pa čak i strukture.

## Hash funkcija

Da bi ključ odgovarao mjestu u memoriji, za ključ treba izračunati indeks, odnosno izračunati kamo taj podatak treba spremiti. Funkcija koja iz ključa računa indeks zove se hash funkcija (funkcija raspršivanja). Primjerice, ako je ključ nečiji osobni identifikacijski broj, hash funkcija mogu biti posljednje četiri znamenke broja, a naravno i prve četiri. „Zadnje znamenke broja mobitela”, koje često koristimo u svakodnevnom životu, također su svojevrsna hash funkcija. U praksi ključevi mogu biti i složeniji, npr. realni brojevi, stringovi, strukture i sl., pa tada prema konkretnoj situaciji treba osmisliti prikladnu hash funkciju. Hash funkcija treba biti jednostavna za računanje i izračunate indekse treba raspodijeliti što ravnomjernije.

Kad za ključ znamo izračunati indeks, znamo i gdje treba spremiti vrijednost (value) koja pripada svakom ključu. Pretpostavimo da podatke spremamo u niz a i da je hash funkcija f; tada par `(key, value)` treba spremiti na `a[f(key)]`. Bez obzira na to kojeg je tipa ključ i koliki mu je raspon, `f(key)` je cijeli broj u prihvatljivom rasponu i može poslužiti kao indeks niza.

U natjecateljskom programiranju najčešći je slučaj da je ključ cijeli broj. Kad je raspon ključeva malen, ključ možemo izravno upotrijebiti kao indeks niza, ali kad je raspon velik, primjerice kad su ključevi cijeli brojevi do $10^9$, potrebna je hash tablica. Obično se kao indeks uzima ostatak ključa pri dijeljenju velikim prostim brojem, tj. hash funkcija je $f(x)=x \bmod M$.

Drugi je čest slučaj da je ključ string. Budući da se string ne može upotrijebiti kao indeks niza, a pretvaranje stringa u broj ujedno izbjegava višestruke usporedbe stringova, u natjecateljskom programiranju string se obično ne koristi izravno kao ključ, nego se najprije izračuna hash stringa pa se taj hash umetne u hash tablicu kao ključ. Hash stringa obično računamo na načelu pozicijskog zapisa: string zamišljamo kao broj u bazi $127$. Tada za svaki string $s$ duljine $n$ vrijedi:

$x = s_0 \cdot 127^0 + s_1 \cdot 127^1 + s_2 \cdot 127^2 + \dots + s_n \cdot 127^n$

Dobiveni $x$ možemo uzeti modulo $2^{64}$ (tj. najveću vrijednost tipa `unsigned long long`). Tako je prirodno prelijevanje (overflow) tipa `unsigned long long` ekvivalentno operaciji modula, što operacije čini jednostavnijima.

Ova je metoda jednostavna, ali nije savršena. Moguće je konstruirati podatke na kojima dolazi do kolizije (tj. dva stringa imaju jednak $x$ modulo $2^{64}$).  
Možemo upotrijebiti dvostruki hash: odaberemo dva velika prosta broja $a,b$. Dva stringa smatramo jednakima ako i samo ako su im hash vrijednosti jednake i modulo $a$ i modulo $b$. Time se vjerojatnost kolizije znatno smanjuje.

## Kolizije

Kad bi hash funkcija za svaki ključ davala različit indeks, bilo bi dovoljno par `(key, value)` smjestiti na mjesto koje određuje indeks. No u stvarnosti se često događa da dva različita ključa imaju isti indeks izračunat hash funkcijom. Tada su potrebne metode za razrješavanje kolizija. U natjecateljskom programiranju najčešća je metoda ulančavanje (chaining).

### Ulančavanje

Ulančavanje se naziva i otvoreno raspršivanje (open hashing).

Pri ulančavanju se na svakom mjestu za pohranu otvori vezana lista; ako više ključeva ima isti indeks, svi se jednostavno stave u listu na tom mjestu. Pri upitu treba proći cijelu listu na odgovarajućem mjestu i za svaki podatak usporediti njegov ključ s traženim. Ako su indeksi u rasponu $1\ldots M$, a veličina hash tablice je $N$, jedno umetanje ili upit zahtijeva u očekivanju $O(\frac{N}{M})$ usporedbi.

#### Implementacija

=== "C++"
    ```cpp
    constexpr int SIZE = 1000000;
    constexpr int M = 999997;
    
    struct HashTable {
      struct Node {
        int next, value, key;
      } data[SIZE];
    
      int head[M], size;
    
      int f(int key) { return (key % M + M) % M; }
    
      int get(int key) {
        for (int p = head[f(key)]; p; p = data[p].next)
          if (data[p].key == key) return data[p].value;
        return -1;
      }
    
      int modify(int key, int value) {
        for (int p = head[f(key)]; p; p = data[p].next)
          if (data[p].key == key) return data[p].value = value;
      }
    
      int add(int key, int value) {
        if (get(key) != -1) return -1;
        data[++size] = Node{head[f(key)], value, key};
        head[f(key)] = size;
        return value;
      }
    };
    ```

=== "Python"
    ```python
    M = 999997
    SIZE = 1000000
    
    
    class Node:
        def __init__(self, next=None, value=None, key=None):
            self.next = next
            self.value = value
            self.key = key
    
    
    data = [Node() for _ in range(SIZE)]
    head = [0] * M
    size = 0
    
    
    def f(key):
        return key % M
    
    
    def get(key):
        p = head[f(key)]
        while p:
            if data[p].key == key:
                return data[p].value
            p = data[p].next
        return -1
    
    
    def modify(key, value):
        p = head[f(key)]
        while p:
            if data[p].key == key:
                data[p].value = value
                return data[p].value
            p = data[p].next
    
    
    def add(key, value):
        if get(key) != -1:
            return -1
        size = size + 1
        data[size] = Node(head[f(key)], value, key)
        head[f(key)] = size
        return value
    ```

Evo još jednog zapakiranog predloška koji se može koristiti kao map, a kraći je:

```cpp
struct hash_map {  // predložak hash tablice

  struct data {
    long long u;
    int v, nex;
  };  // struktura „forward star” (liste susjedstva u nizu)

  data e[SZ << 1];  // SZ je const int koji označava veličinu
  int h[SZ], cnt;

  int hash(long long u) { return (u % SZ + SZ) % SZ; }

  // ovdje koristimo (u % SZ + SZ) % SZ umjesto u % SZ zato što
  // operacija % u C++-u ne pretvara negativne brojeve u pozitivne

  int& operator[](long long u) {
    int hu = hash(u);  // dohvati glavu liste
    for (int i = h[hu]; i; i = e[i].nex)
      if (e[i].u == u) return e[i].v;
    return e[++cnt] = data{u, -1, h[hu]}, h[hu] = cnt, e[cnt].v;
  }

  hash_map() {
    cnt = 0;
    memset(h, 0, sizeof(h));
  }
};
```

Ovdje je funkcija hash osmišljena za tip ključa i vraća glavu vezane liste za pretraživanje. U ovom predlošku napisali smo hash tablicu s parovima tipa `(long long, int)`, koja pri upitu za nepostojeći ključ vraća -1. Funkcija `hash_map()` služi za inicijalizaciju pri definiranju.

### Zatvoreno raspršivanje

Kod zatvorenog raspršivanja (closed hashing) svi se zapisi pohranjuju izravno u hash tablicu; ako dođe do kolizije, pretraživanje se nastavlja prema nekom pravilu.

Primjer je linearno ispitivanje (linear probing): ako dođe do kolizije na mjestu `d`, redom provjeravamo `d + 1`, `d + 2`, ...

#### Implementacija

```cpp
constexpr int N = 360007;  // N je najveći broj elemenata koji se mogu pohraniti

class Hash {
 private:
  int keys[N];
  int values[N];

 public:
  Hash() { memset(values, 0, sizeof(values)); }

  int& operator[](int n) {
    // vraća referencu na odgovarajući Hash[Key]
    // postavi na vrijednost različitu od 0; 0 se smatra praznim mjestom
    int idx = (n % N + N) % N, cnt = 1;
    while (keys[idx] != n && values[idx] != 0) {
      idx = (idx + cnt * cnt) % N;
      cnt += 1;
    }
    keys[idx] = n;
    return values[idx];
  }
};
```

## Primjer zadatka

[„JLOI2011” Brojevi bez ponavljanja](https://www.luogu.com.cn/problem/P4305)
