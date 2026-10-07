---
title: Generalizirani sufiksni automat
---

## Preduvjeti

Generalizirani sufiksni automat (general suffix automaton) temelji se na sljedećim pojmovima:

-   [trie (prefiksno stablo)](./trie.md)
-   [sufiksni automat](./sam.md)

Ovaj članak svakako čitajte tek kad ste s oba navedena pojma vrlo dobro upoznati, a osobito kad razumijete **sufiksne poveznice** u **sufiksnom automatu**.

## Uvod

### Podrijetlo

Generalizirani sufiksni automat struktura je koju je Liu Yanyi predložio u svom radu za kineski nacionalni tim 2015. „Proširenje sufiksnog automata na trie” (《后缀自动机在字典树上的拓展》): sufiksni automat gradi se izravno nad triejem.

> Većina problema na nizovima znakova koji se mogu riješiti sufiksnim automatom može se proširiti na trie. — Liu Yanyi

### Dogovori

Vidi [dogovore o nizovima znakova](./basic.md).

Nizova ima $k$, tj. $S_1, S_2, S_3 \dots S_k$.

Dogovorno je korijen trieja i generaliziranog sufiksnog automata čvor broj $0$.

### Pregled

Sufiksni automat (suffix automaton, SAM) moćan je alat za probleme o podnizovima jednog niza znakova.

Generalizirani sufiksni automat (general suffix automaton) pak ugrađuje sufiksni automat u trie kako bi rješavao probleme o podnizovima više nizova.

## Česti pseudo-generalizirani sufiksni automati

1.  Više nizova izravno se spoji posebnim znakovima, a zatim se izgradi SAM.
2.  Za svaki niz ponovno se gradi na istom SAM-u, a prije svake izgradnje pokazivač `last` postavi se na nulu.

Metode 1 i 2 jednostavne su za implementaciju i na zadacima obično postižu istu točnost kao generalizirani sufiksni automat. Zato se na internetu mnogi odlučuju za takav zapis; primjerice, posljednja primjena u članku o sufiksnom automatu koristi upravo metodu 1 [(poveznica na izvornik)](./sam.md).

No i kod metode 1 i kod metode 2 vremenska je složenost prilično opasna.

## Izgradnja generaliziranog sufiksnog automata

Prema opisu u izvornom radu, najprije treba nad više nizova izgraditi trie, a zatim na temelju trieja izgraditi generalizirani sufiksni automat.

### Korištenje trieja

Najprije za više nizova treba izgraditi trie, što nije nikakav problem: ako ste svladali preduvjete, izgradit ćete ga vrlo brzo. Radi ujednačenosti koda u nastavku, ovdje dajemo jedan mogući kôd trieja.

??? note "Implementacija"
    ```cpp
    constexpr int MAXN = 2000000;
    constexpr int CHAR_NUM = 30;
    
    struct Trie {
      int next[MAXN][CHAR_NUM];  // prijelazi
      int tot;                   // ukupan broj čvorova: [0, tot)
    
      void init() { tot = 1; }
    
      int insertTrie(int cur, int c) {
        if (next[cur][c]) return next[cur][c];
        return next[cur][c] = tot++;
      }
    
      void insert(const string &s) {
        int root = 0;
        for (auto ch : s) root = insertTrie(root, ch - 'a');
      }
    };
    ```

Tako smo dobili trie izgrađen na temelju polja `next`.

### Izgradnja sufiksnog automata

Ako takvo stablo izravno shvatimo kao sufiksni automat, dobivamo sljedeće zaključke:

-   za čvor `i` njegov `len[i]` jednak je njegovoj dubini u trieju;
-   ako trie topološki sortiramo, dobivamo niz čvorova čiji `len` ne pada; BFS daje isti rezultat.

Izgradnja sufiksnog automata može se pak shvatiti kao neprestano umetanje vrijednosti `len` koje strogo rastu, s razlikom $1$. Zato rezultat topološkog sortiranja trieja možemo uzeti kao red (queue) i zatim redom, prema tom redu, umetati čvorove u sufiksni automat.

U običnom sufiksnom automatu `len` prethodnog čvora fiksna je vrijednost, naime `len` čvora `last`. No u generaliziranom sufiksnom automatu red za umetanje nestrogo je rastući niz. Zato za svaku vrijednost njezin `last` mora biti poznat i fiksan: u trieju je to njezin roditelj.

Budući da u trieju već imamo približni sufiksni automat, dovoljno je strukturu cijelog trieja odgovarajuće obraditi da bismo je pretvorili u generalizirani sufiksni automat. Svaki čvor cijelog trieja možemo ažurirati redoslijedom iz gore spomenutog reda. Na kraju dobivamo generalizirani sufiksni automat.

Operaciju ažuriranja svakog čvora dobivamo manjom izmjenom operacije umetanja u SAM.

Tijekom cijelog postupka umetanja treba paziti na sljedeće: budući da umećemo redoslijedom nepadajućeg `len`, pri kopiranju podataka nakon operacije `clone` ne smijemo kopirati podatke čiji je `len` manji od trenutačnog `len`.

### Postupak

Prema gornjoj logici, cijeli se postupak izgradnje može opisati ovim koracima:

1.  umetni sve nizove u trie;
2.  od korijena trieja pokreni BFS, zabilježi redoslijed i roditelja svakog čvora;
3.  prema dobivenom BFS redoslijedu redom gradi svaki čvor na izvornom trieju, pazeći da ne diramo podatke čiji je `len` manji od trenutačnog `len`.

### Dokaz da je broj operacija linearan

Budući da obrađujemo samo niz dobiven BFS-om, zajamčeno je da svaki čvor trieja prolazimo samo jednom.

Za najgori slučaj promotrimo situaciju u kojoj sâm trie ima najviše čvorova, tj. kad nikoja dva niza nemaju zajednički prefiks; tada je broj čvorova $\sum_{i=1}^{k}|S_i|$, tj. zbroj duljina svih nizova.

Složenost operacije ažuriranja sufiksnog automata već je dokazana u članku [sufiksni automat](./sam.md).

Stoga se može dokazati da je složenost u najgorem slučaju linearna.

Obično je prosječna složenost pseudo-generaliziranog sufiksnog automata jednaka složenosti generaliziranog sufiksnog automata u najgorem slučaju; kod velikog broja nizova učinkovitost pseudo-generaliziranog sufiksnog automata daleko je ispod standardnog generaliziranog sufiksnog automata.

### Implementacija

Uz nekoliko nužnih izmjena funkcije za umetanje dobivamo potrebnu funkciju.

??? note "Primjer rješenja"
    ```cpp
    struct GSA {
      int len[MAXN];             // duljina čvora
      int link[MAXN];            // sufiksna poveznica, link
      int next[MAXN][CHAR_NUM];  // prijelazi
      int tot;                   // ukupan broj čvorova: [0, tot)
    
      int insertSAM(int last, int c) {
        int cur = next[last][c];
        len[cur] = len[last] + 1;
        int p = link[last];
        while (p != -1) {
          if (!next[p][c])
            next[p][c] = cur;
          else
            break;
          p = link[p];
        }
        if (p == -1) {
          link[cur] = 0;
          return cur;
        }
        int q = next[p][c];
        if (len[p] + 1 == len[q]) {
          link[cur] = q;
          return cur;
        }
        int clone = tot++;
        for (int i = 0; i < CHAR_NUM; ++i)
          next[clone][i] = len[next[q][i]] != 0 ? next[q][i] : 0;
        len[clone] = len[p] + 1;
        while (p != -1 && next[p][c] == q) {
          next[p][c] = clone;
          p = link[p];
        }
        link[clone] = link[q];
        link[cur] = clone;
        link[q] = clone;
        return cur;
      }
    
      void build() {
        queue<pair<int, int>> q;
        for (int i = 0; i < CHAR_NUM; ++i)
          if (next[0][i]) q.push({i, 0});
        while (!q.empty()) {
          auto item = q.front();
          q.pop();
          auto last = insertSAM(item.second, item.first);
          for (int i = 0; i < CHAR_NUM; ++i)
            if (next[last][i]) q.push({i, last});
        }
      }
    }
    ```

-   Budući da se u redoslijedu dobivenom BFS-om roditelj stalno mijenja, pokazivač `last` ne treba pamtiti.
-   U operaciji umetanja redak `int cur = next[last][c];` razlikuje se od `int cur = tot++;` u običnom sufiksnom automatu, jer čvor koji umećemo već postoji u stablastoj strukturi, pa ga samo treba izravno dohvatiti.
-   Pri kopiranju podataka nakon `clone` postoji provjera `next[clone][i] = len[next[q][i]] != 0 ? next[q][i] : 0;`, što se razlikuje od izravnog pridruživanja `next[clone][i] = next[q][i];` u običnom sufiksnom automatu; ovdje time izbjegavamo ažuriranje vrijednosti čiji je `len` veći od trenutačnog čvora. Naime, `len` u polju dobiva vrijednost tek onda kad BFS obiđe tu vrijednost i umetne je u sufiksni automat.

## Svojstva

1.  Struktura generaliziranog sufiksnog automata jednaka je strukturi sufiksnog automata; velika većina svojstava sufiksnog automata vrijedi i za generalizirani sufiksni automat ([svojstva sufiksnog automata](./sam.md)).
2.  Nakon izgradnje generaliziranog sufiksnog automata struktura trieja obično je uništena, tj. generalizirani sufiksni automat obično se ne može koristiti za rješavanje problema na trieju. Naravno, može se pripremiti dvostruko više prostora i sufiksni automat izgraditi u drugom prostoru.

## Primjene

### Broj različitih podnizova u svim nizovima

Prema svojstvima sufiksnog automata, broj podnizova koji završavaju u čvoru $i$ jednak je $len[i] - len[link[i]]$.

Dakle, odgovor dobivamo prolaskom kroz sve čvorove i zbrajanjem.

Primjer zadatka: [[predložak] Generalizirani sufiksni automat (generalizirani SAM)](https://www.luogu.com.cn/problem/P6139)

??? note "Primjer rješenja"
    ```cpp
    --8<-- "docs/string/code/general-sam/general-sam_1.cpp"
    ```

### Najdulji zajednički podniz više nizova

Za svaki čvor trebamo polje `flag` duljine $k$ (za ovaj zadatak dovoljno je polje oznaka; ako treba izračunati i broj pojavljivanja podniza, treba ga pretvoriti u polje brojača).

Pri umetanju niza u trie brojimo u svim čvorovima i bilježimo u polje koje pripada trenutačnom nizu.

Zatim obilazimo čvorove po padajućem `len` i preko sufiksnih poveznica spajamo `flag` trenutačnog čvora s ostalim čvorovima.

Prođemo sve čvorove i pronađemo čvor s najvećim `len` čiji je `flag` različit od $0$ za sve `k`; `len` tog čvora je rješenje.

Primjer zadatka: [SPOJ Longest Common Substring II](https://www.spoj.com/problems/LCS2/)

??? note "Primjer rješenja"
    ```cpp
    --8<-- "docs/string/code/general-sam/general-sam_2.cpp"
    ```
