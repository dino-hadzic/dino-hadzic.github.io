---
title: Trie (prefiksno stablo)
---

## Definicija

Prefiksno stablo, engleski trie (od „retrieval”). Kako ime kaže, to je stablo nalik rječniku.

## Uvod

Pogledajmo najprije sliku:

![trie1](./images/trie1.png)

Vidimo da ovaj trie slova predstavlja bridovima, a put od korijena do nekog čvora stabla predstavlja string. Na primjer, $1\to4\to 8\to 12$ predstavlja string `caa`.

Struktura trieja vrlo je jednostavna: s $\delta(u,c)$ označavamo sljedeći čvor na koji iz čvora $u$ pokazuje znak $c$, odnosno čvor koji predstavlja string dobiven dodavanjem znaka $c$ na kraj stringa čvora $u$. (Raspon vrijednosti $c$ ovisi o veličini abecede i nije nužno $0\sim 26$.)

Ponekad treba označiti koji su stringovi umetnuti u trie; dovoljno je nakon svakog umetanja označiti čvor koji predstavlja taj string.

## Implementacija

Evo predloška zapakiranog u strukturu:

=== "C++"
    ```cpp
    struct trie {
      int nex[100000][26], cnt;
      bool exist[100000];  // postoji li string koji završava u ovom čvoru
    
      void insert(char *s, int l) {  // umetanje stringa
        int p = 0;
        for (int i = 0; i < l; i++) {
          int c = s[i] - 'a';
          if (!nex[p][c]) nex[p][c] = ++cnt;  // ako ne postoji, dodaj čvor
          p = nex[p][c];
        }
        exist[p] = true;
      }
    
      bool find(char *s, int l) {  // traženje stringa
        int p = 0;
        for (int i = 0; i < l; i++) {
          int c = s[i] - 'a';
          if (!nex[p][c]) return 0;
          p = nex[p][c];
        }
        return exist[p];
      }
    };
    ```

=== "Python"
    ```python
    class trie:
        def __init__(self):
            self.nex = [[0 for i in range(26)] for j in range(100000)]
            self.cnt = 0
            self.exist = [False] * 100000  # postoji li string koji završava u ovom čvoru
    
        def insert(self, s):  # umetanje stringa
            p = 0
            for i in s:
                c = ord(i) - ord("a")
                if not self.nex[p][c]:
                    self.cnt += 1
                    self.nex[p][c] = self.cnt  # ako ne postoji, dodaj čvor
                p = self.nex[p][c]
            self.exist[p] = True
    
        def find(self, s):  # traženje stringa
            p = 0
            for i in s:
                c = ord(i) - ord("a")
                if not self.nex[p][c]:
                    return False
                p = self.nex[p][c]
            return self.exist[p]
    ```

=== "Java"
    ```java
    public class Trie {
        int[][] tree = new int[10000][26];
        int cnt = 0;
        boolean[] end = new boolean[10000];
        
        public void insert(String word) {
            int p = 0;
            char[] chars = word.toCharArray();
            for (int i = 0; i < chars.length; i++) {
                int c = chars[i] - 'a';
                if (tree[p][c] == 0) {
                    tree[p][c] = ++cnt;
                }
                p = tree[p][c];
            }
            end[p] = true;
        }
        
        public boolean find(String word) {
            int p = 0;
            char[] chars = word.toCharArray();
            for (int i = 0; i < chars.length; i++) {
                int c = chars[i] - 'a';
                if (tree[p][c] == 0) {
                    return false;
                }
                p = tree[p][c];
            }
            return end[p];
        }
    }
    ```

## Primjene

### Pretraživanje stringova

Najosnovnija primjena trieja: provjera pojavljuje li se string u „rječniku”.

???+ note "[I tako je počela pogrešna prozivka (Luogu P2580)](https://www.luogu.com.cn/problem/P2580)"
    Zadano je $n$ imena, a zatim se izvodi $m$ prozivki; za svaku treba odgovoriti jednim od: „ime ne postoji”, „ime je prozvano prvi put”, „ime je već prozvano”.
    
    $1\le n\le 10^4$, $1\le m\le 10^5$, duljina svakog stringa ne premašuje $50$.
    
    ??? note "Rješenje"
        Izgradimo trie od svih imena, a zatim u trieju provjeravamo postoji li string i je li već prozvan; pri prvoj prozivci označimo ga kao prozvanog.
    
    ??? note "Referentni kôd"
        ```cpp
        --8<-- "docs/string/code/trie/trie_1.cpp"
        ```

### Aho–Corasick automat

Trie je dio [Aho–Corasick automata](./ac-automaton.md).

### Održavanje ekstrema XOR-a

Ako binarni zapis broja shvatimo kao string, možemo izgraditi trie nad abecedom $\{0,1\}$.

???+ note "[BZOJ1954 Najdulji XOR put](https://hydro.ac/p/bzoj-P1954)"
    Zadano je stablo s težinama na bridovima; treba pronaći $(u, v)$ tako da XOR težina bridova na putu od $u$ do $v$ bude najveći i ispisati taj maksimum. XOR puta ovdje znači XOR svih težina bridova na njemu.
    
    Broj čvorova ne premašuje $10^5$, težine bridova su u $[0,2^{31})$.
    
    ??? note "Rješenje"
        Odaberimo proizvoljan korijen $root$ i neka $T(u, v)$ označava XOR težina bridova na putu između $u$ i $v$; tada je $T(u,v)=T(root, u)\oplus T(root,v)$, jer se dio iznad [LCA](../graph/lca.md) pojavljuje dvaput i XOR ga poništi.
        
        Ako sve vrijednosti $T(root, u)$ umetnemo u trie, za svaki $T(root, u)$ brzo možemo naći $T(root, v)$ s kojim daje najveći XOR:
        
        krenemo od korijena trieja i, ako možemo prijeći u podstablo čiji se bit razlikuje od trenutnog bita $T(root, u)$, idemo onamo; inače nemamo izbora.
        
        Ispravnost greedy pristupa: ako tako krenemo, ovaj je bit $1$; ako ne, ovaj je bit $0$. A viši bitovi imaju prednost i trebaju biti što veći.
    
    ??? note "Referentni kôd"
        ```cpp
        --8<-- "docs/string/code/trie/trie_2.cpp"
        ```

### Održavanje XOR-sume

01-trie je trie nad abecedom $\{0,1\}$. 01-trie može održavati XOR-sumu skupa brojeva, uz podršku za izmjene (brisanje + ponovno umetanje) i globalno uvećanje za jedan (tj. svim se vrijednostima koje održava doda `1`; to je u biti posebna vrsta izmjene).

Ako želimo održavati XOR-sumu, trie treba graditi po bitovima vrijednosti od najnižeg prema najvišem.

**Dogovor**: u tekstu „prema gore” od trenutnog čvora znači put od trenutnog čvora do korijena, a „prema dolje” znači podstablo trenutnog čvora.

#### Umetanje i brisanje

Ako održavamo XOR-sumu, **dovoljno je** znati **parnost** broja nula i jedinica na pojedinom bitu; tj. za znamenku `1`, znamenka na tom bitu je `1` ako i samo ako je broj jedinica na tom bitu neparan. Imajte stalno na umu: ako samo održavamo XOR-sumu, dovoljno je znati broj jedinica na pojedinom bitu, a ne treba nam koje točno brojeve trie sadrži.

Za svaki čvor pamtimo sljedeće tri veličine:

-   `ch[o][0/1]` su dva djeteta čvora `o`; `ch[o][0]` znači da je sljedeći bit `0`, a analogno `ch[o][1]` znači da je sljedeći bit `1`.
-   `w[o]` je broj vrijednosti koje prolaze bridom od čvora `o` do njegova roditelja (težina). Pri svakom umetanju broja `x` težine na putu u trieju koji odgovara binarnom zapisu `x` uvećaju se za `1`.
-   `xorv[o]` je XOR-suma koju održava podstablo s korijenom `o`.

Kôd za održavanje čvora izgleda ovako.

```cpp
void maintain(int o) {
  w[o] = xorv[o] = 0;
  if (ch[o][0]) {
    w[o] += w[ch[o][0]];
    xorv[o] ^= xorv[ch[o][0]] << 1;
  }
  if (ch[o][1]) {
    w[o] += w[ch[o][1]];
    xorv[o] ^= (xorv[ch[o][1]] << 1) | (w[ch[o][1]] & 1);
  }
  // w[o] = w[o] & 1;
  // Dovoljno je znati parnost, točna vrijednost nije potrebna. Naravno, ovaj se redak može i izbrisati, jer gore koristimo samo njegovu parnost.
}
```

Kôd za umetanje i brisanje vrlo je sličan.

Na što treba paziti:

-   `MAXH` ovdje označava dubinu trieja, tj. prisiljavamo da udaljenost svakog lista od korijena bude `MAXH`. Za manje vrijednosti možda ne bismo morali graditi tako duboko (npr. pri umetanju broja `4`, čiji je binarni zapis `100`, od korijena bi bilo dovoljno umetnuti tri bita `001`), ali ipak prisilno umećemo `MAXH` bitova. Svrha je toga lakša obrada prijenosa pri globalnom `+1`. Na primjer, ako je izvorni broj `3` (`11`), nakon uvećanja postaje `4` (`100`); da smo pri umetanju broja `3` umetnuli samo `2` bita, prijenos bi se izgubio.

-   Pri umetanju i brisanju dovoljno je izmijeniti `w[]` lista, a zatim pri povratku iz rekurzije usput održavati čvorove.

???+ note "Implementacija"
    ```cpp
    namespace trie {
    constexpr int MAXH = 21;
    int ch[_ * (MAXH + 1)][2], w[_ * (MAXH + 1)], xorv[_ * (MAXH + 1)];
    int tot = 0;
    
    int mknode() {
      ++tot;
      ch[tot][1] = ch[tot][0] = w[tot] = xorv[tot] = 0;
      return tot;
    }
    
    void maintain(int o) {
      w[o] = xorv[o] = 0;
      if (ch[o][0]) {
        w[o] += w[ch[o][0]];
        xorv[o] ^= xorv[ch[o][0]] << 1;
      }
      if (ch[o][1]) {
        w[o] += w[ch[o][1]];
        xorv[o] ^= (xorv[ch[o][1]] << 1) | (w[ch[o][1]] & 1);
      }
      w[o] = w[o] & 1;
    }
    
    void insert(int &o, int x, int dp) {
      if (!o) o = mknode();
      if (dp > MAXH) return (void)(w[o]++);
      insert(ch[o][x & 1], x >> 1, dp + 1);
      maintain(o);
    }
    
    void erase(int o, int x, int dp) {
      if (dp > 20) return (void)(w[o]--);
      erase(ch[o][x & 1], x >> 1, dp + 1);
      maintain(o);
    }
    }  // namespace trie
    ```

#### Globalno uvećanje za jedan

Globalno uvećanje za jedan znači da se sve vrijednosti u trieju uvećaju za `1`.

Formalno, ako trie održava vrijednosti $V_1, V_2, V_3 \dots V_n$, nakon globalnog uvećanja za jedan održavane vrijednosti trebaju postati $V_1+1, V_2+1, V_3+1 \dots V_n+1$

```cpp
void addall(int o) {
  swap(ch[o][0], ch[o][1]);
  if (ch[o][0]) addall(ch[o][0]);
  maintain(o);
}
```

##### Postupak

Razmislimo kako se `+1` izvodi u binarnom zapisu.

Dovoljno je od najnižeg bita prema najvišem naći prvu `0`, pretvoriti je u `1`, a sve `1` ispod tog položaja pretvoriti u `0`.

Evo nekoliko primjera za osjećaj (brojevi u zagradama su odgovarajuće dekadske vrijednosti):

    1000(8)  + 1 = 1001(9)  ;
    10011(19) + 1 = 10100(20) ;
    11111(31) + 1 = 100000(32);
    10101(21) + 1 = 10110(22) ;
    100000000111111(16447) + 1 = 100000001000000(16448);

U trieju to odgovara zamjeni lijevog i desnog djeteta, a zatim rekurzivnom nastavku niz brid `0` **nakon zamjene**.

Prisjetimo se definicije `w[o]`: `w[o]` je broj vrijednosti koje prolaze bridom od čvora `o` do njegova roditelja (težina).

Čini li vam se ta definicija pomalo čudnom? Možda bi bilo uobičajenije u roditelju čuvati težine bridova prema dvoje djece. No ovdje, kad zamjenjujemo lijevo i desno dijete, očito je zgodnije u djetetu čuvati težinu brida prema roditelju.

### Spajanje 01-trieja

Riječ je o spajanju dvaju gore opisanih 01-trieja uz istodobno spajanje informacija koje održavaju.

Članaka o spajanju trieja možda je malo, ali ideja spajanja trieja vrlo je slična spajanju segment treeova, pa se može potražiti „spajanje segment treeova” (segment tree merging) da bi se naučilo kako spajati trieje.

Spajanje trieja zapravo je vrlo jednostavno: zamislimo funkciju `int merge(int a, int b)` koja prima brojeve čvorova dvaju trieja na istom relativnom položaju i nakon spajanja vraća broj spojenog čvora.

#### Postupak

Kako to implementirati?

Razlikujemo tri slučaja:

-   ako `a` nema čvor na tom položaju, novi spojeni čvor je `b`;
-   ako `b` nema čvor na tom položaju, novi spojeni čvor je `a`;
-   ako postoje i `a` i `b`, informacije iz `b` spojimo u `a`, novi spojeni čvor je `a`, a zatim rekurzivno obradimo lijevo i desno dijete čvora a.

    **Napomena**: ako je potrebno spojiti a i b u novo stablo, ovdje se može stvoriti novi čvor i spojiti u njega; ova implementacija samo spaja informacije iz b u a.

#### Implementacija

```cpp
int merge(int a, int b) {
  if (!a) return b;  // ako a nema čvor na ovom položaju, vrati b
  if (!b) return a;  // ako b nema čvor na ovom položaju, vrati a
  /*
    Ako postoje i `a` i `b`,
    spoji informacije iz `b` u `a`.
  */
  w[a] = w[a] + w[b];
  xorv[a] ^= xorv[b];
  /* Ne koristiti maintain():
    maintain() spaja informacije dvoje djece čvora a,
    a ovdje treba spojiti informacije čvorova a i b.
   */
  ch[a][0] = merge(ch[a][0], ch[b][0]);
  ch[a][1] = merge(ch[a][1], ch[b][1]);
  return a;
}
```

Zapravo se svaki trie može spajati; drugim riječima, spajanje trieja nije ograničeno na 01-trie.

???+ note "[【luogu-P6018】【Ynoi2010】Fusion tree](https://www.luogu.com.cn/problem/P6018)"
    Zadano je stablo s $n$ čvorova, svaki čvor ima vrijednost. Slijedi $m$ operacija.
    Treba podržati sljedeće operacije.
    
    -   Vrijednost svih čvorova na udaljenosti $1$ od čvora $x$: $+1$. Udaljenost dvaju čvorova u stablu definira se kao broj bridova na najkraćem putu između njih.
    
    -   Vrijednost čvora $x$: $-v$.
    
    -   Ispiši XOR-sumu vrijednosti svih čvorova na udaljenosti $1$ od čvora $x$.
        Za $100\%$ testova vrijedi $1\le n \le 5\times 10^5$, $1\le m \le 5\times 10^5$, $0\le a_i \le 10^5$, $1 \le x \le n$, $opt\in\{1,2,3\}$.
        Jamči se da je vrijednost svakog čvora u svakom trenutku nenegativna.
    
    ??? note "Rješenje"
        Za svaki čvor izgradimo trie koji održava vrijednosti njegove djece; trie mora podržavati globalno uvećanje za jedan.
        U svakom čvoru možemo držati lijenu oznaku koja bilježi za koliko su se uvećale vrijednosti djece.
    
    ??? note "Referentni kôd"
        ```cpp
        --8<-- "docs/string/code/trie/trie_3.cpp"
        ```

???+ note "[【luogu-P6623】【Pokrajinski izbori 2020, verzija A】Stablo](https://www.luogu.com.cn/problem/P6623)"
    Zadano je korijensko stablo $T$ s $n$ čvorova numeriranih od $1$, s korijenom u čvoru $1$; svaki čvor ima pozitivnu cjelobrojnu vrijednost $v_i$.
    Neka su $c_1,c_2,\dots,c_k$ brojevi svih čvorova u podstablu čvora $x$ (uključujući sam $x$); vrijednost čvora $x$ definira se kao:  
    $val(x)=(v_{c_1}+d(c_1,x)) \oplus (v_{c_2}+d(c_2,x)) \oplus \cdots \oplus (v_{c_k}+d(c_k, x))$, gdje $d(x,y)$  
    označava broj bridova na jedinstvenom jednostavnom putu između čvorova $x$ i $y$ u stablu, $d(x,x) = 0$. $\oplus$ označava operaciju XOR.
    Izračunaj $\sum\limits_{i=1}^n val(i)$.
    
    ??? note "Rješenje"
        Promatramo doprinos svakog čvora svim njegovim precima.
        Za svaki čvor izgradimo trie koji na početku sadrži samo vrijednost tog čvora; zatim odozdo prema gore spajamo trieje djece, pa izvedemo globalno uvećanje za jedan, a nakon toga pribrojimo odgovor.
    
    ??? note "Referentni kôd"
        ```cpp
        constexpr int _ = 526010;
        int n;
        int V[_];
        int debug = 0;
        
        namespace trie {
        constexpr int MAXH = 21;
        int ch[_ * (MAXH + 1)][2], w[_ * (MAXH + 1)], xorv[_ * (MAXH + 1)];
        int tot = 0;
        
        int mknode() {
          ++tot;
          ch[tot][1] = ch[tot][0] = w[tot] = xorv[tot] = 0;
          return tot;
        }
        
        void maintain(int o) {
          w[o] = xorv[o] = 0;
          if (ch[o][0]) {
            w[o] += w[ch[o][0]];
            xorv[o] ^= xorv[ch[o][0]] << 1;
          }
          if (ch[o][1]) {
            w[o] += w[ch[o][1]];
            xorv[o] ^= (xorv[ch[o][1]] << 1) | (w[ch[o][1]] & 1);
          }
          w[o] = w[o] & 1;
        }
        
        void insert(int &o, int x, int dp) {
          if (!o) o = mknode();
          if (dp > MAXH) return (void)(w[o]++);
          insert(ch[o][x & 1], x >> 1, dp + 1);
          maintain(o);
        }
        
        int merge(int a, int b) {
          if (!a) return b;
          if (!b) return a;
          w[a] = w[a] + w[b];
          xorv[a] ^= xorv[b];
          ch[a][0] = merge(ch[a][0], ch[b][0]);
          ch[a][1] = merge(ch[a][1], ch[b][1]);
          return a;
        }
        
        void addall(int o) {
          swap(ch[o][0], ch[o][1]);
          if (ch[o][0]) addall(ch[o][0]);
          maintain(o);
        }
        }  // namespace trie
        
        int rt[_];
        long long Ans = 0;
        vector<int> E[_];
        
        void dfs0(int o) {
          for (int i = 0; i < E[o].size(); i++) {
            int node = E[o][i];
            dfs0(node);
            rt[o] = trie::merge(rt[o], rt[node]);
          }
          trie::addall(rt[o]);
          trie::insert(rt[o], V[o], 0);
          Ans += trie::xorv[rt[o]];
        }
        
        int main() {
          n = read();
          for (int i = 1; i <= n; i++) V[i] = read();
          for (int i = 2; i <= n; i++) E[read()].push_back(i);
          dfs0(1);
          printf("%lld", Ans);
          return 0;
        }
        ```

### Perzistentni trie

Vidi [Perzistentni trie](../ds/persistent-trie.md).
