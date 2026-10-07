---
title: Osnove stabala
---

## Uvod

Stablo u teoriji grafova izgleda kao stablo u stvarnom životu, samo što pri rješavanju zadataka korijen obično stavljamo gore. Ta struktura podataka izgleda kao naopako okrenuto stablo, pa je po tome i dobila ime.

## Definicija

Stablo bez fiksiranog korijenskog čvora naziva se **nekorijensko stablo** (unrooted tree). Nekorijensko stablo ima nekoliko ekvivalentnih formalnih definicija:

-   povezan neusmjeren graf s $n$ čvorova i $n-1$ bridova

-   neusmjeren povezan graf bez ciklusa

-   neusmjeren graf u kojem između svaka dva čvora postoji točno jedan jednostavni put

-   povezan graf u kojem je svaki brid most

-   graf bez ciklusa u kojem dodavanje brida između bilo koja dva različita čvora daje graf s točno jednim ciklusom

Ako u nekorijenskom stablu odaberemo jedan čvor i nazovemo ga **korijenom**, dobivamo **korijensko stablo** (rooted tree). Korijensko stablo često se i dalje prikazuje kao neusmjeren graf, samo što je među čvorovima određen odnos nadređenosti; više o tome u nastavku.

## Pojmovi vezani uz stabla

### Vrijede za nekorijenska i korijenska stabla

-   **Šuma (forest)**: graf u kojem je svaka komponenta povezanosti stablo. Po definiciji je i jedno stablo šuma.

-   **Razapinjuće stablo (spanning tree)**: razapinjući podgraf povezanog neusmjerenog grafa koji je ujedno stablo. Drugim riječima, iz skupa bridova grafa odaberemo $n - 1$ bridova koji povezuju sve vrhove.

-   **List (leaf node) nekorijenskog stabla**: čvor stupnja najviše $1$.

    ???+ question "Zašto ne stupnja točno $1$?"
        Razmotrite $n = 1$.

-   **List (leaf node) korijenskog stabla**: čvor bez djece.

### Vrijede samo za korijenska stabla

-   **Roditelj (parent node)**: za svaki čvor osim korijena, drugi čvor na putu od tog čvora do korijena.  
    Korijen nema roditelja.
-   **Predak (ancestor)**: čvorovi na putu od čvora do korijena, osim samog čvora.  
    Skup predaka korijena je prazan.
-   **Dijete (child node)**: ako je $u$ roditelj od $v$, onda je $v$ dijete od $u$.  
    Redoslijed djece u pravilu se ne razlikuje; iznimka su binarna stabla.
-   **Dubina čvora (depth)**: broj bridova na putu do korijena.
-   **Visina stabla (height)**: najveća dubina među svim čvorovima.
-   **Braća (sibling)**: djeca istog roditelja međusobno su braća.
-   **Potomak (descendant)**: djeca i potomci djece.  
    Ili drukčije: ako je $u$ predak od $v$, onda je $v$ potomak od $u$.

![tree-definition.svg](images/tree-definition.svg)

-   **Podstablo (subtree)**: podgraf u kojem se čvor nalazi nakon što uklonimo brid prema njegovu roditelju.

    ![tree-definition-subtree.svg](images/tree-definition-subtree.svg)

## Posebna stabla

-   **Lanac (chain/path graph)**: stablo u kojem je svaki čvor incidentan s najviše $2$ brida.

-   **Zvijezda (star)**: stablo u kojem postoji čvor $u$ takav da su svi čvorovi osim $u$ povezani s $u$.

-   **Korijensko binarno stablo (rooted binary tree)**: korijensko stablo u kojem svaki čvor ima najviše dvoje djece. Često se razlikuje redoslijed dvoje djece pa ih zovemo lijevo i desno dijete.  
    U većini slučajeva izraz **binarno stablo** označava korijensko binarno stablo.

-   **Puno binarno stablo (full/proper binary tree)**: binarno stablo u kojem svaki čvor ima 0 ili 2 djece. Drugim riječima, svaki je čvor ili list ili su mu i lijevo i desno podstablo neprazni.

    ![](images/tree-binary-proper.svg)

-   **Potpuno binarno stablo (complete binary tree)**: samo čvorovi na najdonje dvije razine smiju imati stupanj manji od 2, a čvorovi najdonje razine zauzimaju uzastopna mjesta skroz lijevo na toj razini.

    ![](images/tree-binary-complete.svg)

-   **Savršeno binarno stablo (perfect binary tree)**: binarno stablo u kojem svi listovi imaju istu dubinu i svaki čvor koji nije list ima točno 2 djece.

    ![](images/tree-binary-perfect.svg)

???+ warning "Upozorenje"
    Kineski prijevod naziva „proper binary tree” nije ustaljen, a definicije potpunog i punog binarnog stabla razlikuju se od udžbenika do udžbenika, pa pri susretu s tim pojmovima treba suditi prema kontekstu.

Kad natjecatelji kažu „puno binarno stablo” (满二叉树), najčešće misle na savršeno binarno stablo.

## Pohrana

### Pohrana samo roditelja

Poljem `parent[N]` bilježimo roditelja svakog čvora.

Ovako dobivamo malo informacija i nije pogodno za obilazak odozgo prema dolje. Često se koristi u zadacima s rekurzijom odozdo prema gore.

### Lista susjedstva

-   Za nekorijensko stablo: za svaki čvor otvorimo linearnu listu u koju bilježimo sve čvorove povezane s njim.
    ```cpp
    std::vector<int> adj[N];
    ```
-   Za korijensko stablo:
    -   Prvi način: ako je zadan neusmjeren graf, i dalje ga možemo pohraniti na gornji način. U nastavku ćemo opisati kako razlikovati odnos nadređenosti među čvorovima.
    -   Drugi način: ako ulazni podaci jamče odnos nadređenosti među čvorovima, možemo to iskoristiti. Za svaki čvor otvorimo linearnu listu u koju bilježimo svu njegovu djecu; po potrebi u zasebnom polju bilježimo i roditelja.
        ```cpp
        std::vector<int> children[N];
        int parent[N];
        ```
        Naravno, `std::vector` se može zamijeniti drugom strukturom (npr. vezanom listom).

### Prikaz „lijevo dijete, desni brat”

#### Postupak

Za korijenska stabla postoji jednostavan način prikaza.

Najprije za svaki čvor proizvoljno odredimo redoslijed njegove djece.

Zatim za svaki čvor pamtimo dvije vrijednosti: njegovo **prvo dijete** `child[u]` i njegova **sljedećeg brata** `sib[u]`. Ako čvor nema djece, `child[u]` je prazan; ako je čvor posljednje dijete svog roditelja, `sib[u]` je prazan.

#### Implementacija

Obilazak sve djece nekog čvora može se implementirati ovako.

```cpp
int v = child[u];  // krećemo od prvog djeteta
while (v != EMPTY_NODE) {
  // ...
  // obradi dijete v
  // ...
  v = sib[v];  // prijeđi na sljedeće dijete, tj. brata od v
}
```

Može se i skraćeno zapisati ovako.

```cpp
for (int v = child[u]; v != EMPTY_NODE; v = sib[v]) {
  // ...
  // obradi dijete v
  // ...
}
```

### Binarno stablo

Treba zabilježiti lijevo i desno dijete svakog čvora.

???+ note "Implementacija"
    ```cpp
    int parent[N];
    int lch[N], rch[N];
    // -- or --
    int child[N][2];
    ```

## Obilazak stabla

### DFS na stablu

DFS na stablu teče ovako: najprije posjetimo korijen, a zatim redom obiđemo podstablo svakog djeteta korijena.

Tako možemo izračunati dubinu, roditelja i druge podatke za svaki čvor.

### DFS obilasci binarnog stabla

#### Preorder obilazak

![preorder](images/tree-basic-preorder.svg)

Binarno stablo obilazimo u redoslijedu **korijen, lijevo, desno**.

???+ note "Implementacija"
    ```cpp
    void preorder(BiTree* root) {
      if (root) {
        cout << root->key << " ";
        preorder(root->left);
        preorder(root->right);
      }
    }
    ```

#### Inorder obilazak

![inorder](images/tree-basic-inorder.svg)

Binarno stablo obilazimo u redoslijedu **lijevo, korijen, desno**.

???+ note "Implementacija"
    ```cpp
    void inorder(BiTree* root) {
      if (root) {
        inorder(root->left);
        cout << root->key << " ";
        inorder(root->right);
      }
    }
    ```

#### Postorder obilazak

![postorder](images/tree-basic-postorder.svg)

Binarno stablo obilazimo u redoslijedu **lijevo, desno, korijen**.

???+ note "Implementacija"
    ```cpp
    void postorder(BiTree* root) {
      if (root) {
        postorder(root->left);
        postorder(root->right);
        cout << root->key << " ";
      }
    }
    ```

#### Rekonstrukcija

Iz inorder niza i još jednog niza može se odrediti treći niz.

![reverse](images/tree-basic-reverse.svg)

1.  Prvi element preorder niza je `root`, a posljednji element postorder niza je `root`.
2.  Najprije odredimo korijen, a zatim prema inorder nizu: ono lijevo od korijena je lijevo podstablo, a ono desno je desno podstablo.
3.  Svako podstablo možemo promatrati kao posve novo stablo za koje i dalje vrijede gornja pravila.

### BFS na stablu

Krećemo od korijena i čvorove posjećujemo strogo po razinama.

Tijekom BFS-a usput možemo izračunati dubinu i roditelja svakog čvora.

#### Obilazak stabla po razinama

Obilazak po razinama (level-order) znači da čvorove obilazimo vodoravno, razinu po razinu, prema hijerarhiji od korijena do listova. Prema definiciji BFS-a, redoslijed koji daje BFS jest jedan obilazak po razinama. No obilazak po razinama zahtijeva da se razine međusobno razlikuju, pa se rezultat obično prikazuje kao dvodimenzionalno polje.

Primjerice, obilazak stabla na slici po razinama daje `[[1], [2, 3, 4], [5, 6]]` (svaka razina slijeva nadesno).

![tree-basic-levelOrder](images/tree-basic-levelOrder.svg)

???+ note "Implementacija"
    ```cpp
    vector<vector<int>> levelOrder(Node* root) {
      if (!root) {
        return {};
      }
      vector<vector<int>> res;
      queue<Node*> q;
      q.push(root);
      while (!q.empty()) {
        int currentLevelSize = q.size();  // broj čvorova na trenutačnoj razini
        res.push_back(vector<int>());
        for (int i = 0; i < currentLevelSize; ++i) {
          Node* cur = q.front();
          q.pop();
          res.back().push_back(cur->val);
          for (Node* child : cur->children) {  // dodaj svu djecu
            q.push(child);
          }
        }
      }
      return res;
    }
    ```

### Morrisov obilazak binarnog stabla

Središnji problem obilaska binarnog stabla jest kako se, nakon što obiđemo djecu trenutačnog čvora, vratiti u njega i nastaviti obilazak. I rekurzivni i nerekurzivni obilazak binarnog stabla koriste stog za bilježenje povratnog puta i tako ostvaruju kretanje s niže razine na višu. Prostorna složenost toga je u najboljem slučaju $O(\log n)$, a u najgorem $O(n)$ (binarno stablo je lanac).

Bit Morrisova obilaska jest izbjeći stog: slobodne pokazivače `right` donjih čvorova iskorištavamo da pokazuju natrag na neki čvor više razine i tako ostvarujemo kretanje odozdo prema gore.

#### Postupak Morrisova obilaska

Neka smo u trenutačnom čvoru `cur`; na početku je to korijen.

1.  Ako je `cur` prazan, obilazak staje; inače radimo sljedeće.
2.  Ako `cur` nema lijevo podstablo, `cur` se pomiče udesno (`cur = cur->right`).
3.  Ako `cur` ima lijevo podstablo, pronađemo krajnji desni čvor lijevog podstabla, označimo ga `mostRight`.
    -   Ako pokazivač `right` čvora `mostRight` pokazuje na prazno, postavimo ga da pokazuje na `cur`, a zatim se `cur` pomiče ulijevo (`cur = cur->left`).
    -   Ako pokazivač `right` čvora `mostRight` pokazuje na `cur`, vratimo ga na `null`, a zatim se `cur` pomiče udesno (`cur = cur->right`).

Primjerice, `cur` kreće od čvora 1.

![tree-basic-morris-1](images/tree-basic-morris-1.svg)

Kad `cur` prvi put posjeti čvor 2, pronađe krajnji desni čvor lijevog podstabla, čvor 4, i postavi pokazivač `right` čvora 4 na `cur` (čvor 2).

![tree-basic-morris-2](images/tree-basic-morris-2.svg)

`cur` se preko pokazivača `right` čvora 4 vraća na višu razinu; kad drugi put posjeti čvor 2, pronađe krajnji desni čvor lijevog podstabla, čvor 4, vrati pokazivač `right` čvora 4 na `null` i nastavi obilazak desnog podstabla. Ostatak postupka izostavljamo.

![tree-basic-morris-1](images/tree-basic-morris-1.svg)

Redoslijed posjećivanja cijelog stabla je `1242513637`. Vidimo da se čvorovi s lijevim podstablom posjećuju dvaput, a čvorovi bez lijevog podstabla samo jednom.

???+ note "Implementacija"
    ```cpp
    void morris(TreeNode* root) {
      TreeNode* cur = root;
      while (cur) {
        if (!cur->left) {
          // ako trenutačni čvor nema lijevo dijete, ispiši njegovu vrijednost i prijeđi u desno podstablo
          std::cout << cur->val << " ";
          cur = cur->right;
          continue;
        }
        // pronađi krajnji desni čvor lijevog podstabla trenutačnog čvora
        TreeNode* mostRight = cur->left;
        while (mostRight->right && mostRight->right != cur) {
          mostRight = mostRight->right;
        }
        if (!mostRight->right) {
          // ako je pokazivač right krajnjeg desnog čvora prazan, usmjeri ga na trenutačni čvor i prijeđi u lijevo podstablo
          mostRight->right = cur;
          cur = cur->left;
        } else {
          // ako pokazivač right krajnjeg desnog čvora pokazuje na trenutačni čvor, lijevo je podstablo obiđeno; ispiši vrijednost trenutačnog čvora i prijeđi u desno podstablo
          mostRight->right = nullptr;
          std::cout << cur->val << " ";
          cur = cur->right;
        }
      }
    }
    ```

### Nekorijensko stablo

#### Postupak

Stablo se obično obilazi u dubinu, a pritom najviše treba paziti da se čvorovi ne posjećuju više puta.

Budući da je stablo graf bez ciklusa, dovoljno je zabilježiti iz kojeg smo čvora došli u trenutačni, a zatim ući u sve susjedne čvorove osim tog jednog; tako izbjegavamo ponovno posjećivanje.

???+ note "Implementacija"
    ```cpp
    void dfs(int u, int from) {
      // rekurzivno uđi u svu djecu osim from
      // za polazni čvor from je prazan, pa se posjećuju svi susjedi, što i želimo
      for (int v : adj[u])
        if (v != from) {
          dfs(v, u);
        }
    }
    
    // na početku obilaska
    int EMPTY_NODE = -1;  // nepostojeći indeks
    int root = 0;         // proizvoljan čvor kao polazište
    dfs(root, EMPTY_NODE);
    ```

### Korijensko stablo

Kod korijenskog stabla treba razlikovati odnos nadređenosti među čvorovima.

Pogledamo li gornji postupak obilaska: ako krenemo od korijena, vrijednost `from` pri posjetu nekom čvoru upravo je indeks njegova roditelja.

Na taj način iz neusmjerenog ulaza možemo odrediti roditelja svakog čvora i popise djece.

**Dio sadržaja ove stranice preuzet je iz članka [二叉树：前序遍历、中序遍历、后续遍历](https://blog.csdn.net/weixin_43357638/article/details/99730284) (Binarno stablo: preorder, inorder i postorder obilazak), pod licencijom CC 4.0 BY-SA.**
