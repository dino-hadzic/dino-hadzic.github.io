---
title: Red
---

Ova stranica predstavlja strukture podataka povezane s redovima i njihove primjene.

![](./images/queue.svg)

## Uvod

Red (queue) je lista sa svojstvom da element koji ranije uđe u red mora ranije i izaći iz njega. Zato se red zove i FIFO lista (first in, first out), odnosno lista koja slijedi načelo „prvi ušao, prvi izašao”.

## Implementacija

### Implementacija reda poljem

Red se obično simulira poljem i dvjema varijablama koje označavaju njegov početak i kraj.

```cpp
int q[SIZE], ql = 1, qr;
```

Operacijama nad redom odgovara sljedeći kôd:

-   Umetanje elementa: `q[++qr] = x;`
-   Uklanjanje elementa: `ql++;`
-   Pristup početku: `q[ql]`
-   Pristup kraju: `q[qr]`
-   Pražnjenje reda: `ql = 1; qr = 0;`

??? example "[Luogu B3616: Red (predložak)](https://www.luogu.com.cn/problem/B3616) — implementacija poljem"
    ```cpp
    --8<-- "docs/ds/code/queue/queue_1.cpp"
    ```

### Implementacija reda dvama stogovima

Manje poznat način simulira red pomoću dvaju [stogova](./stack.md).

Koristimo dva stoga, $F$ i $S$, pri čemu $F$ predstavlja kraj reda, a $S$ njegov početak. Operacije push (umetanje na kraj) i pop (uklanjanje s početka) podržavamo ovako:

-   push: umetni u stog $F$.
-   pop: ako $S$ nije prazan, ukloni element s $S$. Inače prebaci elemente $F$ u $S$ obrnutim redoslijedom (uklanjaj i umeći jedan po jedan, čime se redoslijed obrće), a zatim ukloni element s $S$.

Svaki se element umeće, prebacuje i uklanja samo jednom, pa je amortizirana složenost $O(1)$.

??? example "[Luogu B3616: Red (predložak)](https://www.luogu.com.cn/problem/B3616) — implementacija dvama stogovima"
    ```cpp
    --8<-- "docs/ds/code/queue/queue_2.cpp"
    ```

## Redovi u C++ STL-u

C++ STL nudi spremnik `std::queue`. Prije korištenja treba uključiti zaglavlje `<queue>`.

???+ info "Definicija spremnika `queue` u STL-u"
    ```cpp
    // clang-format off
    template<
        class T,
        class Container = std::deque<T>
    > class queue;
    ```
    
    `T` je tip podataka pohranjenih u redu.
    
    `Container` je tip temeljnog spremnika za pohranu elemenata. Mora pružati sljedeće funkcije s njihovim uobičajenim značenjem:
    
    -   `back()`
    -   `front()`
    -   `push_back()`
    -   `pop_front()`
    
    STL spremnici `std::deque` i `std::list` zadovoljavaju te zahtjeve. Ako nije drukčije navedeno, zadani temeljni spremnik jest `std::deque`.

Spremnik `queue` u STL-u pruža niz članskih funkcija. Često se koriste:

-   Pristup elementima
    -   `q.front()` vraća element na početku reda
    -   `q.back()` vraća element na kraju reda
-   Izmjene
    -   `q.push()` umeće element na kraj reda
    -   `q.pop()` uklanja element s početka reda
-   Kapacitet
    -   `q.empty()` vraća je li red prazan
    -   `q.size()` vraća broj elemenata u redu

Spremnik `queue` pruža i nekoliko operatora. Često se koristi operator pridruživanja `=`, kao u ovom primjeru:

```cpp
std::queue<int> q1, q2;

// Umetni 1 na kraj reda q1
q1.push(1);

// Pridruži q1 redu q2
q2 = q1;

// Ispiši element na početku reda q2
std::cout << q2.front() << std::endl;
// Ispis: 1
```

## Posebni redovi

### Dvostrani redovi

Dvostrani red (deque) dopušta umetanje i uklanjanje na početku i na kraju. Kombinira funkcionalnost stoga i reda. Konkretno, podržava četiri operacije:

-   Umetanje elementa na početak
-   Umetanje elementa na kraj
-   Uklanjanje elementa s početka
-   Uklanjanje elementa s kraja

Simulacija dvostranog reda poljem radi jednako kao za običan red.

Dvostrani red možemo održavati i pristupom s dvama stogovima. No kad je jedan stog prazan, naizmjenični upiti o početku i kraju narušavaju amortiziranu analizu. Umjesto toga u prazni stog premjestimo samo polovinu elemenata nepraznog stoga, uz očuvanje uloga početnog i završnog stoga. Time i dalje postižemo amortizirano konstantno vrijeme umetanja i uklanjanja.

??? note "Kratak dokaz"
    Umetanje doprinosi samo konstantnu složenost, pa promatramo uklanjanje. Pretpostavimo da red na početku sadrži $m$ elemenata. Računamo vrijeme potrebno da ih sve uklonimo, s bilo kojeg kraja. Prvo balansiranje traje $O(m)$, nakon čega svaki stog sadrži $\frac{m}{2}$ elemenata. Pražnjenje jednog stoga tada traje $O(\frac{m}{2})$ i pokreće novo balansiranje složenosti $O(\frac{m}{2})$, i tako dalje dok ne uklonimo sve elemente. Ukupna je složenost zato
    
    $$
    T(m)=T\left(\frac{m}{2}\right)+O(m)
    $$
    
    Prema glavnom teoremu dobivamo $T(m)=O(m)$. Zato ovaj pristup i dalje ima amortizirano konstantnu složenost.

??? example "[Luogu B3656: Dvostrani red 1 (predložak)](https://www.luogu.com.cn/problem/B3656) — referentna implementacija"
    ```cpp
    --8<-- "docs/ds/code/queue/queue_3.cpp"
    ```

#### Dvostrani redovi u C++ STL-u

C++ STL nudi i spremnik `std::deque`. Prije korištenja treba uključiti zaglavlje `<deque>`.

??? info "Definicija spremnika `deque` u STL-u"
    ```cpp
    // clang-format off
    template<
        class T,
        class Allocator = std::allocator<T>
    > class deque;
    ```
    
    `T` je tip podataka pohranjenih u dvostranom redu.
    
    `Allocator` je alokator. Ovdje ga ne objašnjavamo detaljnije; zadana vrijednost obično je dovoljna.

Spremnik `deque` u STL-u pruža niz članskih funkcija. Često se koriste:

-   Pristup elementima
    -   `q.front()` vraća element na početku reda
    -   `q.back()` vraća element na kraju reda
-   Izmjene
    -   `q.push_back()` umeće element na kraj reda
    -   `q.pop_back()` uklanja element s kraja reda
    -   `q.push_front()` umeće element na početak reda
    -   `q.pop_front()` uklanja element s početka reda
    -   `q.insert()` umeće element ispred zadane pozicije (predaju se iterator i element)
    -   `q.erase()` uklanja element na zadanoj poziciji (predaje se iterator)
-   Kapacitet
    -   `q.empty()` vraća je li dvostrani red prazan
    -   `q.size()` vraća broj elemenata u dvostranom redu

Spremnik `deque` pruža i nekoliko operatora. Često se koriste:

-   Operator pridruživanja `=` pridružuje vrijednost spremniku `deque`, kao za `queue`.
-   Operator `[]` pristupa elementima, kao za `vector`.

Zaglavlje `<queue>` pruža i prioritetni red `std::priority_queue`. Budući da je sličniji strukturi [heap](./heap.md), ovdje ga ne razmatramo detaljnije.

#### Dvostrani redovi u Pythonu

U Pythonu spremnik dvostranog reda pruža `collections.deque`.

Primjer:

???+ note "Implementacija"
    ```python
    from collections import deque
    
    # Stvori deque s početnim sadržajem [1, 2, 3]
    queue = deque([1, 2, 3])
    
    # Umetni 4 na kraj
    queue.append(4)
    
    # Umetni 0 na početak
    queue.appendleft(0)
    
    # Pristup redu
    # >>> queue
    # deque([0, 1, 2, 3, 4])
    ```

### Kružni redovi

Simulacija reda poljem stvara problem: s vremenom se cijeli red pomiče prema kraju polja. Kad dosegne kraj, novo umetanje uzrokuje prekoračenje iako na početku polja još ima slobodnih mjesta. Takvo prekoračenje unatoč slobodnom prostoru zove se „lažno prekoračenje”.

Lažno prekoračenje izbjegavamo kružnom organizacijom polja: poziciju s indeksom 0 smatramo sljedbenikom posljednje pozicije. Sljedbenik indeksa `x` jest `(x + 1) % SIZE`. Time dobivamo kružni red.

## Literatura

1.  [std::queue - zh.cppreference.com](https://zh.cppreference.com/w/cpp/container/queue)
2.  [std::deque - zh.cppreference.com](https://zh.cppreference.com/w/cpp/container/deque)
