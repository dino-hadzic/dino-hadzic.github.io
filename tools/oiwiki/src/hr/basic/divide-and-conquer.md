---
title: Rekurzija i podijeli pa vladaj
---

Ova stranica predstavlja razliku između rekurzije i algoritama „podijeli pa vladaj” te njihovu zajedničku primjenu.

## Rekurzija

### Definicija

**Rekurzija** (recursion) u matematici i računarstvu označava korištenje same funkcije u njezinoj definiciji; u računarstvu dodatno označava metodu rješavanja problema ponovljenim rastavljanjem na potprobleme istog tipa.

### Uvod

Da biste razumjeli rekurziju, prvo morate razumjeti što je rekurzija.

Osnovna ideja rekurzije jest da funkcija izravno ili neizravno poziva samu sebe; time se rješavanje izvornog problema svodi na mnogo potproblema istih svojstava, ali manje veličine. Pri rješavanju treba samo paziti kako izvorni problem podijeliti na odgovarajuće potprobleme, a ne previše razmišljati o tome kako se potproblem rješava.

Nekoliko primjera koji pomažu razumjeti rekurziju:

1.  [Što je rekurzija?](./divide-and-conquer.md)
2.  Kako sortirati hrpu brojeva? Odgovor: podijeli ih na dvije polovice, sortiraj lijevu pa desnu i na kraju ih spoji; a kako sortirati lijevu i desnu – pročitaj ponovno ovu rečenicu.
3.  Koliko imaš godina? Odgovor: godinu više nego prošle godine; rođen sam 1999.
4.  ![primjer za razumijevanje rekurzije](images/divide-and-conquer-1.png)

Rekurzija je vrlo česta u matematici. Primjerice, formalna definicija prirodnih brojeva u teoriji skupova glasi: 1 je prirodan broj; svaki prirodan broj ima sljedbenika i taj je sljedbenik također prirodan broj.

Dvije najvažnije značajke rekurzivnog koda su uvjet zaustavljanja i poziv samog sebe. Poziv samog sebe rješava potprobleme, a uvjet zaustavljanja definira odgovor na najjednostavniji potproblem.

```cpp
int func(ulazna vrijednost) {
  if (uvjet zaustavljanja) return rješenje najmanjeg potproblema;
  return func(smanjena veličina);
}
```

### Zašto pisati rekurzivno

1.  Jasna struktura i čitljivost. Primjerice, [merge sort](./merge-sort.md) implementiran na dva načina:

    === "C++"
        ```cpp
        --8<-- "docs/basic/code/divide-and-conquer/divide-and-conquer_1.cpp:sort"
        ```

    === "Python"
        ```python
        --8<-- "docs/basic/code/divide-and-conquer/divide-and-conquer_1.py:sort"
        ```

    U oba koda `merge(a, front, mid, end)` u mjestu spaja dva sortirana zatvorena intervala `[front,mid]` i `[mid+1,end]` istog niza.

2.  Vježba analize strukture problema. Kad se primijeti da se problem može rastaviti na manje probleme iste strukture, s puno napisane rekurzije tu značajku brzo prepoznajemo i problem učinkovito rješavamo.

### Nedostaci rekurzije

Pri izvođenju programa rekurzija se ostvaruje pomoću stoga. Pri svakom ulasku u poziv funkcije stog dobiva novi okvir (stack frame), a pri svakom povratku okvir se uklanja. Stog nije neograničen, pa prevelika dubina rekurzije dovodi do **prekoračenja stoga** (stack overflow).

Rekurzivna implementacija može zahtijevati dodatni stog poziva, dok iterativna može koristiti samo konstantan pomoćni prostor. Primjerice, zadana je glava vezane liste; izračunaj njezinu duljinu:

```cpp
// Tipičan iterativni obilazak
int size(Node *head) {
  int size = 0;
  for (Node *p = head; p != nullptr; p = p->next) size++;
  return size;
}

// Rekurzivni obilazak, svaka razina obrađuje jedan čvor
int size_recursion(Node *head) {
  if (head == nullptr) return 0;
  return size_recursion(head->next) + 1;
}
```

[![usporedba obje inačice](images/divide-and-conquer-2.svg)](https://quick-bench.com/q/rZ7jWPmSdltparOO5ndLgmS9BVc)

### Optimizacija rekurzije

Glavne stranice: [Optimizacija pretraživanja](../search/opt.md) i [Memoizacija](../dp/memo.md)

Jednostavne rekurzivne implementacije mogu imati previše poziva i lako prekoračiti vremensko ograničenje. Tada rekurziju treba optimirati.[^ref1]

## Podijeli pa vladaj

### Definicija

**Podijeli pa vladaj** (divide and conquer) doslovno znači „podijeli i vladaj”: složen se problem dijeli na dva ili više jednakih ili sličnih potproblema, sve dok se potproblemi ne mogu izravno riješiti; rješenje izvornog problema je spoj rješenja potproblema.

### Postupak

Središnja ideja algoritama „podijeli pa vladaj” jest upravo „podijeli i vladaj”.

Okvirni tijek ima tri koraka: podijeli -> riješi -> spoji.

1.  Rastavi izvorni problem na potprobleme iste strukture;
2.  kad se dođe do granice na kojoj se problem lako rješava, riješi ga rekurzivno;
3.  spoji rješenja potproblema u rješenje izvornog problema.

Problemi rješivi metodom „podijeli pa vladaj” obično imaju ova svojstva:

-   Kad se veličina problema dovoljno smanji, problem se lako rješava.
-   Problem se može rastaviti na nekoliko manjih problema istog tipa, tj. ima svojstvo optimalne podstrukture; rješenja dobivenih potproblema mogu se spojiti u rješenje problema.
-   Potproblemi na koje se problem rastavlja međusobno su neovisni, tj. nemaju zajedničkih potproblema.

???+ warning "Napomena"
    Ako potproblemi nisu neovisni, metoda „podijeli pa vladaj” više puta rješava zajedničke potprobleme i radi mnogo nepotrebnog posla. I tada se metoda može koristiti, ali je obično bolje [dinamičko programiranje](../dp/basic.md).

Uzmimo merge sort kao primjer. Neka se funkcija koja implementira merge sort zove `merge_sort`. Jasno odredimo njezinu zadaću: **sortirati zadani niz**. Taj se problem očito može rastaviti: sortirati niz znači sortirati zasebno njegovu lijevu i desnu polovicu i zatim ih spojiti u jedan niz.

```cpp
void merge_sort(neki niz) {
  if (lako se obradi) return;
  merge_sort(lijeva polovica niza);
  merge_sort(desna polovica niza);
  merge(lijeva polovica niza, desna polovica niza);
}
```

Predamo li joj polovicu niza, nakon obrade ta je polovica sortirana. Uočimo da je `merge_sort` vrlo sličan predlošku post-order obilaska binarnog stabla. Obrazac metode je **podijeli -> riješi (dno) -> spoji (povratak)**: najprije dijelimo lijevo i desno, zatim obrađujemo spajanje; povratak je izlazak iz stoga, što odgovara post-order obilasku.

Funkcija `merge` implementira se jednako kao spajanje dviju sortiranih vezanih lista.

## Ključne točke

### Kako pisati rekurziju

**Shvati što funkcija radi i vjeruj da će to obaviti; nikako ne uskači u funkciju pokušavajući istražiti detalje** – inače ćeš se utopiti u beskrajnim detaljima; koliko razina stoga ljudski mozak može držati?

Uzmimo obilazak binarnog stabla.

```cpp
void traverse(TreeNode* root) {
  if (root == nullptr) return;
  traverse(root->left);
  traverse(root->right);
}
```

Tih nekoliko redaka dovoljno je za obilazak bilo kojeg binarnog stabla. Za rekurzivnu funkciju `traverse(root)` dovoljno je vjerovati da će, kad joj damo korijen `root`, obići to stablo. Zato joj samo treba proslijediti lijevo i desno dijete čvora.

Isto se proširuje na obilazak $N$-arnog stabla; zapis je potpuno isti kao za binarno. Naravno, kod $N$-arnog stabla očito nema in-order obilaska.

```cpp
void traverse(TreeNode* root) {
  if (root == nullptr) return;
  for (auto child : root->children) traverse(child);
}
```

## Razlike

### Rekurzija i nabrajanje

Razlika između rekurzije i nabrajanja: nabrajanje problem dijeli vodoravno i redom rješava potprobleme; rekurzija problem rastavlja razinu po razinu, okomito.

### Rekurzija i podijeli pa vladaj

Rekurzija je programska tehnika, način razmišljanja o rješavanju problema; algoritam „podijeli pa vladaj” uvelike se temelji na rekurziji, ali je algoritamska ideja za rješavanje konkretnijih problema.

## Riješeni primjer

???+ note "[437. Path Sum III](https://leetcode.com/problems/path-sum-iii/)"
    Zadano je binarno stablo u čijem svakom čvoru piše cijeli broj.
    
    Odredi broj putova čiji je zbroj jednak zadanoj vrijednosti.
    
    Put ne mora početi u korijenu ni završiti u listu, ali mora ići prema dolje (samo od roditelja prema djetetu).
    
    Stablo ima najviše 1000 čvorova, a vrijednosti u čvorovima su cijeli brojevi iz $[-10^6,10^6]$.
    
    Primjer:
    
    ```text
    root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8
    
          10
         /  \
        5   -3
       / \    \
      3   2   11
     / \   \
    3  -2   1
    
    Rezultat je 3. Putovi sa zbrojem 8 su:
    
    1.  5 -> 3
    2.  5 -> 2 -> 1
    3. -3 -> 11
    ```
    
    ```cpp
    --8<-- "docs/basic/code/divide-and-conquer/divide-and-conquer_2.h"
    ```

??? note "Primjer rješenja"
    ```cpp
    --8<-- "docs/basic/code/divide-and-conquer/divide-and-conquer_2.cpp"
    ```

??? note "Analiza zadatka"
    Zadatak izgleda složeno, ali je kôd iznimno sažet.
    
    Prvo, rekurzivno rješavanje problema na stablu nužno obilazi cijelo stablo, pa se okvir obilaska binarnog stabla (rekurzivni poziv funkcije na lijevom i desnom podstablu) nužno pojavljuje u glavnoj funkciji `pathSum`. Što onda treba raditi svaki čvor? Treba pogledati koliko odgovarajućih putova sadrže on i njegovo podstablo. I to je sve.
    
    Prema ranije opisanoj tehnici, iz ove analize jasno definiramo što svaka rekurzivna funkcija radi:
    
    funkcija `pathSum`: za zadani čvor i ciljnu vrijednost vraća broj putova sa zbrojem jednakim cilju u stablu s korijenom u tom čvoru.
    
    funkcija `count`: za zadani čvor i ciljnu vrijednost vraća broj putova koji počinju u tom čvoru i imaju zbroj jednak cilju.
    
    ??? note "Primjer rješenja"
        ```cpp
        --8<-- "docs/basic/code/divide-and-conquer/divide-and-conquer_2.cpp"
        ```
    
    Opet ista rečenica: **shvati što svaka funkcija radi i vjeruj da će to obaviti.**
    
    Ukratko, `pathSum` daje okvir obilaska binarnog stabla i tijekom obilaska za svaki čvor poziva `count` (ovdje pre-order, ali bi radio i in-order ili post-order). I `count` je obilazak binarnog stabla, koji traži putove s ciljnim zbrojem koji počinju u tom čvoru.

## Zadaci za vježbu

-   [Vježbe o rekurziji na LeetCodeu](https://leetcode.com/explore/learn/card/recursion-i/)
-   [Zadaci „podijeli pa vladaj” na LeetCodeu](https://leetcode.com/tag/divide-and-conquer/)

## Literatura i bilješke

[^ref1]: [labuladong 的算法小抄 – Rekurzija (kineski)](https://labuladong.gitbook.io/algo/suan-fa-si-wei-xi-lie/di-gui-xiang-jie)
