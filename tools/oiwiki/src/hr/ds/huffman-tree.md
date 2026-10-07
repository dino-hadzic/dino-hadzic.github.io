---
title: Huffmanovo stablo
---

## Težinska duljina puteva stabla

Neka binarno stablo ima $n$ težinskih listova. Zbroj umnožaka duljine puta od korijena do svakog lista i težine tog lista naziva se **težinska duljina puteva stabla (Weighted Path Length of Tree, WPL)**.

Neka je $w_i$ težina $i$-tog lista binarnog stabla, a $l_i$ duljina puta od korijena do $i$-tog lista; tada se WPL računa formulom:

$$
WPL=\sum_{i=1}^nw_il_i
$$

![](./images/huffman-tree-1.svg)

Za stablo na slici izračun WPL-a i rezultat glase:

$$
WPL=2*2+3*2+4*2+7*2=4+6+8+14=32
$$

## Struktura

Za zadani skup listova s određenim težinama mogu se izgraditi različita binarna stabla; ono **binarno stablo s najmanjim WPL-om** naziva se **Huffmanovo stablo (Huffman tree)**.

U Huffmanovu stablu listovi manje težine dalje su od korijena, a listovi veće težine bliže su korijenu; osim toga, samo listovi imaju stupanj $0$, dok svi ostali čvorovi imaju stupanj $2$.

## Huffmanov algoritam

Huffmanov algoritam služi za izgradnju Huffmanova stabla, a koraci su sljedeći:

1.  **Inicijalizacija**: od zadanih $n$ težina izgradimo $n$ binarnih stabala koja se sastoje samo od korijena i tako dobijemo skup binarnih stabala $F$.
2.  **Odabir i spajanje**: iz skupa $F$ odaberemo **dva stabla s najmanjim** težinama korijena i od njih kao lijevog i desnog podstabla izgradimo novo binarno stablo; težina korijena novog stabla jednaka je zbroju težina korijena lijevog i desnog podstabla.
3.  **Brisanje i dodavanje**: iz $F$ izbrišemo dva stabla koja su postala lijevo i desno podstablo, a novoizgrađeno stablo dodamo u $F$.
4.  Ponavljamo korake 2 i 3; kad u skupu ostane samo jedno binarno stablo, to je stablo Huffmanovo.

![](./images/huffman-tree-2.svg)

### Dokaz ispravnosti

???+ note "Lema"
    U optimalnom stablu prefiksnog koda (Huffmanovu stablu) dva lista najmanje težine uvijek su najdublji listovi, a njihovo premještanje tako da postanu braća ne narušava optimalnost stabla koda.

??? note "Dokaz"
    Tvrdnju dokazujemo kontradikcijom. Pretpostavimo da u nekom optimalnom stablu prefiksnog koda postoje dva lista najmanje težine koja nisu najdublji listovi. Označimo ih s $a$ i $b$; njihova je dubina manja od dubine nekog najdubljeg lista. Za taj najdublji list $c$ možemo zamijeniti položaje $a$ i $c$ ili položaje $b$ i $c$. Budući da Huffmanov algoritam na svakoj razini spaja listove najmanje težine, nakon zamjene težinska duljina puteva (WPL) stabla se smanjuje. Time dobivamo kontradikciju, pa pretpostavka ne vrijedi; dakle, dva lista najmanje težine moraju biti najdublji listovi.
    
    Zatim pretpostavimo da su ta dva lista najmanje težine $a$ i $b$ i da su iste dubine. Ako u optimalnom stablu prefiksnog koda ta dva čvora nisu braća, pretpostavimo da postoje drugi čvorovi $c$ i $d$ koji su braća od $a$ odnosno $b$ (recimo da su $a$ i $c$ braća te $b$ i $d$ braća). Čvorove $a$ i $b$ možemo spojiti u jedno podstablo.
    
    -   Ako je zbroj težina $a$ i $b$ manji od težine $c$ ili $d$, spojeno podstablo možemo spojiti s čvorom veće težine (npr. $c$ ili $d$) u novo podstablo, pri čemu se WPL smanjuje.
    -   Ako zbroj težina $a$ i $b$ nije manji od težina $c$ i $d$, možemo izravno premjestiti $a$ i $b$ tako da budu braća, a $c$ i $d$ učiniti drugim parom braće; WPL se pri tome ne povećava.
    
    Dakle, takvim premještanjem optimalnost se ne narušava, što je i trebalo dokazati.

???+ note "Teorem"
    Stablo prefiksnog koda dobiveno Huffmanovim algoritmom optimalno je stablo prefiksnog koda.

??? note "Dokaz"
    Teorem dokazujemo matematičkom indukcijom.
    
    -   **Baza**: za broj slova $n = 2$ očito je stablo dobiveno izravnim spajanjem dvaju slova optimalno stablo koda.
    -   **Pretpostavka indukcije**: pretpostavimo da za broj slova $n = k$ ($k \geq 2$) Huffmanov algoritam daje optimalno stablo prefiksnog koda.
    -   **Korak indukcije**: za broj slova $n = k + 1$ među $k+1$ slova odaberemo dva slova najmanje težine i spojimo ih u podstablo, čiji korijen smatramo virtualnim slovom (virtualnim čvorom). Prema lemi, taj postupak ne narušava optimalnost stabla prefiksnog koda. Virtualno slovo zajedno s preostalih $k$ slova čini $k + 1$ slova; prema pretpostavci indukcije, za $k$ slova Huffmanov algoritam daje optimalno stablo prefiksnog koda.
    
    Stoga, matematičkom indukcijom, Huffmanov algoritam daje optimalno stablo prefiksnog koda za svaki broj slova $n$, što je i trebalo dokazati.

## Huffmanov kod

Pri programiranju se obično svakom znaku dodjeljuje zasebna šifra kojom se predstavlja skup znakova, tj. **kod**.

Ako pri binarnom kodiranju pretpostavimo da su sve šifre jednake duljine, za prikaz $n$ različitih znakova potrebno je $\left \lceil \log_2 n \right \rceil$ bitova; takav se kod naziva **kod jednake duljine**.

Ako su **učestalosti svih znakova jednake**, kod jednake duljine nesumnjivo je prostorno najučinkovitiji; ako se pak znakovi pojavljuju različito često, znakovima velike učestalosti možemo dodijeliti što kraće šifre, a znakovima male učestalosti što dulje, i tako izgraditi **kod nejednake duljine** koji je prostorno učinkovitiji.

Pri oblikovanju koda nejednake duljine treba voditi računa o jedinstvenosti dekodiranja: ako nijedna šifra u skupu šifara nije prefiks neke druge šifre, takav se skup naziva **prefiksni kod** i on jamči jedinstvenost dekodiranja.

Huffmanovo stablo može se iskoristiti za izgradnju **najkraćeg prefiksnog koda**, tj. **Huffmanova koda (Huffman code)**, a postupak je sljedeći:

1.  Neka je skup znakova koje treba kodirati $d_1,d_2,\dots,d_n$, a njihove učestalosti u nizu znakova $w_1,w_2,\dots,w_n$.
2.  S $d_1,d_2,\dots,d_n$ kao listovima i $w_1,w_2,\dots,w_n$ kao težinama listova izgradimo Huffmanovo stablo.
3.  Dogovorimo da lijeva grana Huffmanova stabla označava $0$, a desna $1$; tada niz znamenaka $0$ i $1$ na putu od korijena do lista predstavlja šifru znaka koji odgovara tom listu.

![](./images/huffman-tree-3.svg)

## Primjeri koda

??? note "Izgradnja Huffmanova stabla"
    ```cpp
    struct HNode {
      int weight;
      HNode *lchild, *rchild;
    };
    
    using Htree = HNode *;
    
    Htree createHuffmanTree(int arr[], int n) {
      Htree forest[N];
      Htree root = NULL;
      for (int i = 0; i < n; i++) {  // sve čvorove stavimo u šumu
        Htree temp;
        temp = (Htree)malloc(sizeof(HNode));
        temp->weight = arr[i];
        temp->lchild = temp->rchild = NULL;
        forest[i] = temp;
      }
    
      for (int i = 1; i < n; i++) {  // n-1 iteracija za izgradnju Huffmanova stabla
        int minn = -1, minnSub;  // minn je indeks korijena najmanje težine, minnsub indeks korijena druge najmanje težine
        for (int j = 0; j < n; j++) {
          if (forest[j] != NULL && minn == -1) {
            minn = j;
            continue;
          }
          if (forest[j] != NULL) {
            minnSub = j;
            break;
          }
        }
    
        for (int j = minnSub; j < n; j++) {  // određivanje minn i minnSub
          if (forest[j] != NULL) {
            if (forest[j]->weight < forest[minn]->weight) {
              minnSub = minn;
              minn = j;
            } else if (forest[j]->weight < forest[minnSub]->weight) {
              minnSub = j;
            }
          }
        }
    
        // izgradnja novog stabla
        root = (Htree)malloc(sizeof(HNode));
        root->weight = forest[minn]->weight + forest[minnSub]->weight;
        root->lchild = forest[minn];
        root->rchild = forest[minnSub];
    
        forest[minn] = root;     // pokazivač na novo stablo spremamo na mjesto minn
        forest[minnSub] = NULL;  // mjesto minnSub ostaje prazno
      }
      return root;
    }
    ```

??? note "Izračun WPL-a izgrađenog Huffmanova stabla"
    ```cpp
    struct HNode {
      int weight;
      HNode *lchild, *rchild;
    };
    
    using Htree = HNode *;
    
    int getWPL(Htree root, int len) {  // rekurzivna implementacija: računa WPL već izgrađenog Huffmanova stabla
      if (root == NULL)
        return 0;
      else {
        if (root->lchild == NULL && root->rchild == NULL)  // list
          return root->weight * len;
        else {
          int left = getWPL(root->lchild, len + 1);
          int right = getWPL(root->rchild, len + 1);
          return left + right;
        }
      }
    }
    ```

??? note "Izravan izračun WPL-a bez izgradnje Huffmanova stabla"
    ```cpp
    int getWPL(int arr[], int n) {  // WPL računamo izravno, bez izgradnje Huffmanova stabla
      priority_queue<int, vector<int>, greater<int>> huffman;  // min-heap
      for (int i = 0; i < n; i++) huffman.push(arr[i]);
    
      int res = 0;
      for (int i = 0; i < n - 1; i++) {
        int x = huffman.top();
        huffman.pop();
        int y = huffman.top();
        huffman.pop();
        int temp = x + y;
        res += temp;
        huffman.push(temp);
      }
      return res;
    }
    ```

??? note "Izračun Huffmanova koda za zadani niz"
    ```cpp
    struct HNode {
      int weight;
      HNode *lchild, *rchild;
    };
    
    using Htree = HNode *;
    
    void huffmanCoding(Htree root, int len, int arr[]) {  // izračun Huffmanova koda
      if (root != NULL) {
        if (root->lchild == NULL && root->rchild == NULL) {
          printf("结点为 %d 的字符的编码为: ", root->weight);
          for (int i = 0; i < len; i++) printf("%d", arr[i]);
          printf("\n");
        } else {
          arr[len] = 0;
          huffmanCoding(root->lchild, len + 1, arr);
          arr[len] = 1;
          huffmanCoding(root->rchild, len + 1, arr);
        }
      }
    }
    ```
