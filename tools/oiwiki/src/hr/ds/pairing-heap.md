---
title: Pairing heap
---

## Uvod

Pairing heap (uparujući heap) struktura je podataka koja podržava umetanje, upit za minimum / brisanje minimuma, spajanje, izmjenu elemenata i druge operacije; riječ je o spojivom heapu (mergeable heap). Prednosti su mu brzina i jednostavna struktura, ali budući da mu je složenost amortizirana i temelji se na analizi potencijala, ne može se učiniti perzistentnim.

## Definicija

Pairing heap je težinsko stablo s proizvoljnim brojem djece koje zadovoljava svojstvo heapa (vidi sliku), tj. težina svakog čvora manja je ili jednaka težinama sve njegove djece (uzimamo min-heap kao primjer, kao i u nastavku).  
![](./images/pairingheap1.jpg)

Pairing heap obično pohranjujemo prikazom „dijete–brat” (vidi sliku): sva djeca jednog čvora čine jednostruko vezanu listu. Svaki čvor čuva pokazivač na prvo dijete, tj. na glavu te liste, i pokazivač na svojeg desnog brata.

Taj je način pogodan za implementaciju pairing heapa, a olakšava i analizu složenosti.

![](./images/pairingheap2.jpg)

```cpp
struct Node {
  T v;  // T je tip težine
  Node *child, *sibling;
  // child pokazuje na prvo dijete čvora, sibling na sljedećeg brata.
  // Ako čvor nema djece / sljedećeg brata, pokazivač je nullptr.
};
```

Iz definicije se vidi da, za razliku od ostalih uobičajenih heapova, pairing heap ne održava nikakve dodatne informacije poput veličine stabla, dubine ili ranga (binarni heap također ne održava dodatne informacije, ali složenost operacija osigurava održavanjem stroge strukture potpunog binarnog stabla), te da je svako stablo koje zadovoljava svojstvo heapa valjan pairing heap. Ta jednostavna, a vrlo fleksibilna struktura temelj je izvrsne praktične učinkovitosti pairing heapa; za usporedbu, loša konstanta Fibonaccijeva heapa posljedica je toga što on mora održavati mnogo dodatnih informacija.

Pairing heap ukupnu složenost osigurava pažljivo osmišljenim redoslijedom operacija; izvorni rad[^ref1] naziva ga „samoprilagođavajućim heapom” (Self Adjusting Heap). U tome je prilično sličan Splay stablu (koje se u izvornom radu naziva „Self Adjusting Binary Tree”).

## Postupak

### Upit za minimum

Iz definicije pairing heapa vidi se da korijen sigurno ima najmanju težinu, pa jednostavno vratimo korijen.

### Spajanje

Spajanje dvaju pairing heapova vrlo je jednostavno: najprije manji od dvaju korijena proglasimo novim korijenom, a zatim veći korijen umetnemo kao njegovo dijete (vidi sliku).

![](./images/pairingheap3.jpg)

Treba primijetiti da je lista djece jednog čvora poredana po vremenu umetanja: krajnji desni čvor najranije je postao dijete roditelja, a krajnji lijevi najkasnije.

???+ note "Implementacija"
    ```cpp
    Node* meld(Node* x, Node* y) {
      // ako je jedan prazan, vrati drugi
      if (x == nullptr) return y;
      if (y == nullptr) return x;
      if (x->v > y->v) std::swap(x, y);  // nakon swapa x je heap s manjom težinom, y s većom
      // y postaje dijete od x
      y->sibling = x->child;
      x->child = y;
      return x;  // novi korijen je x
    }
    ```

### Umetanje

Kad imamo spajanje, umetanje je jednostavno: novi element promatramo kao novi pairing heap i spojimo ga s izvornim heapom.

### Brisanje minimuma

Najprije treba spomenuti da su dosadašnje operacije prilično „lijene” i uopće ne održavaju strukturu podataka, pa operaciju brisanja minimuma moramo pažljivo osmisliti kako ukupna složenost ne bi stradala.

Korijen je minimum, pa brišemo korijen. Razmotrimo što se događa kad uklonimo korijen: sva dotadašnja djeca korijena čine šumu, a pairing heap mora biti stablo, pa tu djecu moramo spojiti nekim redoslijedom.

Prirodna je ideja funkcijom `meld` spajati djecu redom slijeva nadesno; ispravnost je očita, ali tako složenost jedne operacije degradira na $O(n)$.

Da bi se zajamčila ukupna amortizirana složenost, koristi se spajanje „u dva koraka”:

1.  djecu uparimo po dvoje i operacijom `meld` spojimo dva djeteta iz istog para (vidi sliku 1),
2.  novonastale heapove spajamo redom **zdesna nalijevo** (tj. od starijeg djeteta prema novijem) (vidi sliku 2).

![](./images/pairingheap4.jpg)

![](./images/pairingheap5.jpg)

Najprije implementirajmo pomoćnu funkciju `merges` koja spaja svu braću jednog čvora.

???+ note "Implementacija"
    ```cpp
    Node* merges(Node* x) {
      if (x == nullptr || x->sibling == nullptr)
        return x;  // ako je stablo prazno ili nema sljedećeg brata, nema što spajati, return.
      Node* y = x->sibling;                // y je sljedeći brat od x
      Node* c = y->sibling;                // c je brat iza njega
      x->sibling = y->sibling = nullptr;   // razdvoji
      return meld(merges(c), meld(x, y));  // ključni dio
    }
    ```

Posljednja naredba srž je funkcije i ima tri dijela:

1.  `meld(x,y)` „upari” x i y.
2.  `merges(c)` rekurzivno spaja c i njegovu braću.
3.  Dva nova stabla nastala u prethodna dva koraka spoje se.

Treba uočiti da je, kako je rečeno, smjer spajanja u drugom koraku propisan (zdesna nalijevo); ova rekurzivna implementacija već osigurava taj redoslijed. Ako čitatelj želi sam napisati iterativnu inačicu, svakako mora paziti na taj redoslijed, inače složenost više nije zajamčena.

Kad imamo funkciju `merges`, operacija `delete-min` je očita.

???+ note "Implementacija"
    ```cpp
    Node* delete_min(Node* x) {
      Node* t = merges(x->child);
      delete x;  // ako je potrebno oslobađanje memorije
      return t;
    }
    ```

### Smanjivanje vrijednosti elementa

Za ovu operaciju čvoru treba dodati pokazivač „otac”: ako čvor ima lijevog brata, pokazivač pokazuje na lijevog brata, a ne na stvarnog roditelja; inače pokazuje na roditelja.

Najprije definiciju čvora mijenjamo u:

???+ note "Implementacija"
    ```cpp
    struct Node {
      LL v;
      int id;
      Node *child, *sibling;
      Node *father;  // novo: pokazivač na oca; ako je čvor korijen, pokazuje na nullptr
    };
    ```

Operaciju `meld` mijenjamo u:

???+ note "Implementacija"
    ```cpp
    Node* meld(Node* x, Node* y) {
      if (x == nullptr) return y;
      if (y == nullptr) return x;
      if (x->v > y->v) std::swap(x, y);
      if (x->child != nullptr) {  // novo: održavanje pokazivača na oca
        x->child->father = y;
      }
      y->sibling = x->child;
      y->father = x;  // novo: održavanje pokazivača na oca
      x->child = y;
      return x;
    }
    ```

Operaciju `merges` mijenjamo u:

???+ note "Implementacija"
    ```cpp
    Node *merges(Node *x) {
      if (x == nullptr) return nullptr;
      x->father = nullptr;  // novo: održavanje pokazivača na oca
      if (x->sibling == nullptr) return x;
      Node *y = x->sibling, *c = y->sibling;
      y->father = nullptr;  // novo: održavanje pokazivača na oca
      x->sibling = y->sibling = nullptr;
      return meld(merges(c), meld(x, y));
    }
    ```

Razmotrimo sada kako implementirati operaciju `decrease-key`.  
Najprije uočimo: kad smanjimo težinu čvora `x`, podstablo s korijenom `x` i dalje zadovoljava svojstvo pairing heapa, ali između roditelja od `x` i `x` svojstvo heapa možda više ne vrijedi.  
Zato cijelo podstablo s korijenom `x` odrežemo; sada oba stabla zadovoljavaju svojstvo pairing heapa, pa ih spojimo i time je operacija dovršena.

???+ note "Implementacija"
    ```cpp
    // root je korijen heapa, x čvor nad kojim radimo, v nova težina; pri pozivu mora vrijediti v <= x->v
    // povratna vrijednost je novi korijen
    Node *decrease_key(Node *root, Node *x, LL v) {
      x->v = v;                 // ažuriraj težinu
      if (x == root) return x;  // ako je x korijen, odmah vrati
      // odreži x iz djece od fa; ovdje treba razlikovati položaj x-a.
      if (x->father->child == x) {
        x->father->child = x->sibling;
      } else {
        x->father->sibling = x->sibling;
      }
      if (x->sibling != nullptr) {
        x->sibling->father = x->father;
      }
      x->sibling = nullptr;
      x->father = nullptr;
      return meld(root, x);  // ponovno spoji x i korijen
    }
    ```

## Analiza složenosti

Struktura i implementacija pairing heapa jednostavne su, ali analiza vremenske složenosti nije laka.

Izvorni rad[^ref1] dokazao je samo da operacije `meld` i `delete-min` imaju amortiziranu složenost $O(\log n)$, ali je iznio pretpostavku da sve operacije imaju istu složenost kao kod Fibonaccijeva heapa.

Nažalost, poslije je otkriveno da kod pairing heapa koji ne održava dodatne informacije, za određene nizove operacija, donja granica amortizirane složenosti operacije `decrease-key` iznosi barem $\Omega (\log \log n)$[^ref2].

Trenutačno su razmjerno dobre procjene gornje granice složenosti: Iaconova $O(1)$ za `meld` i $O(\log n)$ za `decrease-key`[^ref3]; Pettiejeva $O(2^{2 \sqrt{\log \log n}})$ za `meld` i `decrease-key`[^ref4]. Treba naglasiti da su sve navedene složenosti amortizirane, pa se ne smije za svaku operaciju zasebno uzeti najmanji od rezultata.

## Literatura

[^ref1]: [The pairing heap: a new form of self-adjusting heap](http://www.cs.cmu.edu/~sleator/papers/pairing-heaps.pdf)

[^ref2]: [On the efficiency of pairing heaps and related data structures](https://dl.acm.org/doi/10.1145/320211.320214)

[^ref3]: [Improved upper bounds for pairing heaps](https://arxiv.org/abs/1110.4428)

[^ref4]: [Towards a Final Analysis of Pairing Heaps](http://web.eecs.umich.edu/~pettie/papers/focs05.pdf)

-   <https://en.wikipedia.org/wiki/Pairing_heap>
-   <https://brilliant.org/wiki/pairing-heap/>
