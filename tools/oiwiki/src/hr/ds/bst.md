---
title: Binarno stablo pretraživanja i balansirana stabla
---

## Definicija

Binarno stablo pretraživanja (BST) stablasta je struktura podataka u obliku binarnog stabla, definirana ovako:

1.  Prazno stablo je binarno stablo pretraživanja.

2.  Ako lijevo podstablo binarnog stabla pretraživanja nije prazno, vrijednosti svih čvorova u njegovu lijevom podstablu manje su od vrijednosti korijena.

3.  Ako desno podstablo binarnog stabla pretraživanja nije prazno, vrijednosti svih čvorova u njegovu desnom podstablu veće su od vrijednosti korijena.

4.  Lijevo i desno podstablo binarnog stabla pretraživanja također su binarna stabla pretraživanja.

Vrijeme osnovnih operacija na binarnom stablu pretraživanja proporcionalno je visini stabla. Za binarno stablo pretraživanja s $n$ čvorova najbolja je vremenska složenost tih operacija $O(\log n)$, a najgora $O(n)$. Očekivana visina nasumično izgrađenog binarnog stabla pretraživanja je $O(\log n)$.

## Postupak

### Definicija čvora binarnog stabla pretraživanja

???+ note "Implementacija"
    ```cpp
    struct TreeNode {
      int key;
      TreeNode* left;
      TreeNode* right;
      // održavanje dodatnih informacija, npr. visine, broja čvorova itd.
      int size;   // veličina podstabla s korijenom u ovom čvoru
      int count;  // broj ponavljanja vrijednosti ovog čvora
    
      TreeNode(int value)
          : key(value), size(1), count(1), left(nullptr), right(nullptr) {}
    };
    ```

### Obilazak binarnog stabla pretraživanja

Iz rekurzivne definicije binarnog stabla pretraživanja slijedi da je niz vrijednosti dobiven inorder obilaskom nepadajući. Vremenska složenost je $O(n)$.

Kod za obilazak binarnog stabla pretraživanja:

???+ note "Implementacija"
    ```cpp
    void inorderTraversal(TreeNode* root) {
      if (root == nullptr) {
        return;
      }
      inorderTraversal(root->left);
      std::cout << root->key << " ";
      inorderTraversal(root->right);
    }
    ```

### Traženje minimuma/maksimuma

Iz svojstava binarnog stabla pretraživanja slijedi da je minimum stabla krajnji čvor njegova lijevog lanca, a maksimum krajnji čvor desnog lanca. Vremenska složenost je $O(h)$.

???+ note "Implementacija"
    ```cpp
    int findMin(TreeNode* root) {
      if (root == nullptr) {
        return -1;
      }
      while (root->left != nullptr) {
        root = root->left;
      }
      return root->key;
    }
    
    int findMax(TreeNode* root) {
      if (root == nullptr) {
        return -1;
      }
      while (root->right != nullptr) {
        root = root->right;
      }
      return root->key;
    }
    ```

### Pretraživanje elementa

U binarnom stablu pretraživanja s korijenom `root` tražimo čvor vrijednosti `value`.

Razlikujemo slučajeve:

-   Ako je `root` prazan, vrati `false`.
-   Ako je vrijednost od `root` jednaka `value`, vrati `true`.
-   Ako je vrijednost od `root` veća od `value`, nastavi pretraživanje u lijevom podstablu od `root`.
-   Ako je vrijednost od `root` manja od `value`, nastavi pretraživanje u desnom podstablu od `root`.

Vremenska složenost je $O(h)$.

???+ note "Implementacija"
    ```cpp
    bool search(TreeNode* root, int target) {
      if (root == nullptr) {
        return false;
      }
      if (root->key == target) {
        return true;
      } else if (target < root->key) {
        return search(root->left, target);
      } else {
        return search(root->right, target);
      }
    }
    ```

Umetanje, brisanje i izmjena prvo zahtijevaju pretraživanje u binarnom stablu pretraživanja.

### Umetanje elementa

U binarno stablo pretraživanja s korijenom `root` umećemo čvor vrijednosti `value`.

Razlikujemo slučajeve:

-   Ako je `root` prazan, izravno vrati novi čvor vrijednosti `value`.

-   Ako je vrijednost od `root` jednaka `value`, broj pojavljivanja te vrijednosti u dodatnom polju čvora uveća se za $1$.

-   Ako je vrijednost od `root` veća od `value`, umetni čvor vrijednosti `value` u lijevo podstablo od `root`.

-   Ako je vrijednost od `root` manja od `value`, umetni čvor vrijednosti `value` u desno podstablo od `root`.

Vremenska složenost je $O(h)$.

???+ note "Implementacija"
    ```cpp
    TreeNode* insert(TreeNode* root, int value) {
      if (root == nullptr) {
        return new TreeNode(value);
      }
      if (value < root->key) {
        root->left = insert(root->left, value);
      } else if (value > root->key) {
        root->right = insert(root->right, value);
      } else {
        root->count++;  // vrijednosti su jednake, uvećaj broj ponavljanja
      }
      root->size = root->count + (root->left ? root->left->size : 0) +
                   (root->right ? root->right->size : 0);  // ažuriraj veličinu podstabla čvora
      return root;
    }
    ```

### Brisanje elementa

Iz binarnog stabla pretraživanja s korijenom `root` brišemo čvor vrijednosti `value`.

Prvo u stablu pronađemo čvor vrijednosti `value`, a zatim razlikujemo slučajeve:

-   Ako je dodatno polje `count` tog čvora veće od $1$, dovoljno je umanjiti `count`.

-   Ako je `count` tog čvora jednak $1$:

    -   Ako je `root` list, jednostavno ga izbrišemo.

    -   Ako je `root` lančani čvor, tj. čvor sa samo jednim djetetom, vratimo to dijete.

    -   Ako `root` ima dva neprazna djeteta, obično ga zamijenimo maksimumom lijevog podstabla (najdesnjim čvorom lijevog podstabla) ili minimumom desnog podstabla (najljevijim čvorom desnog podstabla), a zatim taj čvor izbrišemo.

Vremenska složenost $O(h)$.

???+ note "Implementacija"
    Poziv `root = remove(root, 1)` briše čvor vrijednosti 1 iz stabla s korijenom `root` i vraća novi korijen.
    
    ```cpp
    // povratna vrijednost je novi root nakon brisanja value
    TreeNode* remove(TreeNode* root, int value) {
      if (root == nullptr) {
        return root;
      }
      if (value < root->key) {
        root->left = remove(root->left, value);
      } else if (value > root->key) {
        root->right = remove(root->right, value);
      } else {
        if (root->count > 1) {
          root->count--;  // broj ponavljanja veći od 1, umanji ga
        } else {
          if (root->left == nullptr) {
            TreeNode* temp = root->right;
            delete root;
            return temp;
          } else if (root->right == nullptr) {
            TreeNode* temp = root->left;
            delete root;
            return temp;
          } else {
            TreeNode* successor = findMinNode(root->right);
            root->key = successor->key;
            root->count = successor->count;  // ažuriraj broj ponavljanja
            // kad je successor->count > 1, taj čvor također treba izbrisati,
            // inače bi sljedeće brisanje samo umanjilo broj ponavljanja
            successor->count = 1;
            root->right = remove(root->right, successor->key);
          }
        }
      }
      // dalje održavamo size; ne pišemo --root->size;
      // jer value možda nije u stablu pa brisanje možda nije izvedeno
      root->size = root->count + (root->left ? root->left->size : 0) +
                   (root->right ? root->right->size : 0);
      return root;
    }
    
    // ovdje kao primjer uzimamo minimum desnog podstabla
    TreeNode* findMinNode(TreeNode* root) {
      while (root->left != nullptr) {
        root = root->left;
      }
      return root;
    }
    ```

### Rang elementa

Rang je definiran kao broj elemenata ispred prvog jednakog elementa nakon što se niz sortira uzlazno, uvećan za jedan.

Da bismo našli rang elementa, krećemo od korijena prema tom elementu; pri svakom skoku udesno odgovoru dodamo broj čvorova lijevog djeteta i broj ponavljanja trenutnog čvora, a na kraju dodamo veličinu lijevog podstabla odredišta uvećanu za jedan.

Vremenska složenost $O(h)$.

???+ note "Implementacija"
    ```cpp
    int queryRank(TreeNode* root, int v) {
      if (root == nullptr) return 0;
      if (root->key == v) return (root->left ? root->left->size : 0) + 1;
      if (root->key > v) return queryRank(root->left, v);
      return queryRank(root->right, v) + (root->left ? root->left->size : 0) +
             root->count;
    }
    ```

### Traženje elementa ranga k

U podstablu rang korijena ovisi o veličini njegova lijevog podstabla.

-   Ako je veličina lijevog podstabla veća ili jednaka $k$, element je u lijevom podstablu;

-   ako je veličina lijevog podstabla u intervalu $[k-\textit{count},k-1]$ (`count` je broj pojavljivanja vrijednosti trenutnog čvora), element je korijen podstabla;

-   ako je veličina lijevog podstabla manja od $k-\textit{count}$, element je u desnom podstablu.

Vremenska složenost $O(h)$.

???+ note "Implementacija"
    ```cpp
    int querykth(TreeNode* root, int k) {
      if (root == nullptr) return -1;  // ili po potrebi vrati neku drugu prikladnu vrijednost
      if (root->left) {
        if (root->left->size >= k) return querykth(root->left, k);
        if (root->left->size + root->count >= k) return root->key;
      } else {
        if (k <= root->count) return root->key;
      }
      return querykth(root->right,
                      k - (root->left ? root->left->size : 0) - root->count);
    }
    ```

## Uvod u balansirana stabla

Jedna je svrha stabla pretraživanja skratiti vrijeme umetanja, brisanja, izmjene i pretraživanja čvorova (umetanje, brisanje i izmjena uključuju pretraživanje).

Što se tiče učinkovitosti pretraživanja, ako stablo ima visinu $h$, u najgorem slučaju pretraživanje ključa zahtijeva $h$ usporedbi, pa vremenska složenost pretraživanja (ujedno prosječna duljina pretraživanja, ASL – Average Search Length) ne prelazi $O(h)$. U idealnom binarnom stablu pretraživanja vrijeme svih operacija može se skratiti na $O(\log n)$ ($n$ je ukupan broj čvorova).

Međutim, složenost $O(\log n)$ vrijedi samo u idealnom slučaju. U najgorem slučaju stablo pretraživanja može degenerirati u vezanu listu. Zamislite binarno stablo pretraživanja u kojem svaki čvor ima samo desno dijete: njegova su svojstva ista kao kod vezane liste i sve operacije (umetanje, brisanje, izmjena, pretraživanje) traju $O(n)$.

Vidimo da složenost operacija ovisi o visini stabla $h$. Odatle proizlaze balansirana stabla, koja određenim operacijama održavaju visinu stabla (balansiranost) i tako smanjuju složenost operacija.

### Definicija balansiranosti

Različita balansirana stabla različito definiraju što znači da je stablo pretraživanja „**balansirano**”. Primjerice, ako se u binarnom stablu pretraživanja s korijenom T visine lijevog i desnog podstabla jako razlikuju, ili je broj čvorova lijevog podstabla mnogo veći od broja čvorova desnog, stablo očito nije balansirano.

Za binarna stabla pretraživanja uobičajena je definicija balansiranosti: u stablu s korijenom T visine lijevog i desnog podstabla svakog čvora razlikuju se za najviše 1.

-   U [Splay stablu](splay.md) svaki pristup čvoru (pretraživanje, umetanje ili brisanje) premješta pristupljeni čvor u korijen stabla.

-   U [AVL stablu](avl.md) svaki čvor N održava visinu stabla s korijenom N. Definicija balansiranosti u AVL stablu: T je AVL stablo ako i samo ako su lijevo i desno podstablo također AVL stabla i $|height(T->left) - height(T->right)| \leq 1$.

-   U [Size Balanced Treeu](sbt.md) svaki čvor N održava broj čvorova `size` stabla s korijenom N. Definicija balansiranosti: `size` svakog čvora nije manji od `size` bilo kojeg djeteta (Nephew) njegova brata (Sibling).

Osim toga, za stabla pretraživanja s istim skupom vrijednosti balansirano stanje ne mora biti jedinstveno. Drugim riječima, dva različita stabla pretraživanja mogu sadržavati isti skup vrijednosti i oba biti balansirana.

### Postupak uspostavljanja balansa

Prilagodbom stabla pretraživanja koje ne zadovoljava uvjet balansiranosti može se ponovno uspostaviti balansiranost.

Kod binarnih balansiranih stabala operacije za uspostavljanje balansa su **lijeva rotacija (Left Rotate ili zag)** i **desna rotacija (Right Rotate ili zig)**. Budući da pri prilagodbi binarnog balansiranog stabla inorder niz mora ostati nepromijenjen, nijedna od tih dviju operacija ne mijenja inorder niz.

Prvo opisujemo desnu rotaciju, koja se naziva i „desna jednostruka rotacija” ili „LL rotacija”. Desna rotacija čvora $A$ znači: lijevo dijete $B$ od $A$ rotira se gore udesno i zamjenjuje $A$ kao korijen, čvor $A$ rotira se dolje udesno i postaje korijen desnog podstabla od $B$, a dosadašnje desno podstablo od $B$ postaje lijevo podstablo od $A$.

![bst-rotate](images/bst-rotate.svg)

Desna rotacija mijenja samo tri veze među čvorovima, što odgovara cikličkoj zamjeni triju bridova; stoga treba privremeno spremiti jedan čvor i zatim izvesti cikličko ažuriranje.

Uobičajeni redoslijed ažuriranja kod desne rotacije: privremeno spremi čvor $B$ (novi korijen), lijevo dijete od $A$ usmjeri na desno podstablo $T2$ od $B$, zatim pokazivač desnog djeteta od $B$ usmjeri na $A$, a na kraju roditelja od $A$ usmjeri na spremljeni $B$.

Potpuno analogno postoji lijeva rotacija, koja se naziva i „lijeva jednostruka rotacija” ili „RR rotacija”. Lijeva i desna rotacija zrcalne su slike jedna druge.

Slijedi kod lijeve i desne rotacije.

???+ note "Implementacija"
    ```cpp
    TreeNode* rotateLeft(TreeNode* root) {
      TreeNode* newRoot = root->right;
      root->right = newRoot->left;
      newRoot->left = root;
      // ažuriraj informacije zahvaćenih čvorova
      updateHeight(root);
      updateHeight(newRoot);
      return newRoot;  // vrati novi korijen
    }
    
    TreeNode* rotateRight(TreeNode* root) {
      TreeNode* newRoot = root->left;
      root->left = newRoot->right;
      newRoot->right = root;
      updateHeight(root);
      updateHeight(newRoot);
      return newRoot;
    }
    ```

U ovom primjeru koda pri pozivu treba sačuvati roditelja `pre` od `root`. Funkcija vraća pokazivač na novi korijen; dovoljno je `pre` usmjeriti na novi korijen.

#### Četiri slučaja narušavanja balansa

Iako se definicije različitih binarnih balansiranih stabala razlikuju, razlika je samo u informacijama koje čvorovi održavaju i u načinu njihova ažuriranja nakon rotacije. Balans binarnog balansiranog stabla može se narušiti samo na sljedeća četiri načina, a operacije za uspostavljanje balansa su samo lijeva i desna rotacija. Prvo opisujemo četiri slučaja, a zatim uspoređujemo različita binarna balansirana stabla.

Tip LL: lijevo podstablo lijevog djeteta od T predugo je i narušava balans.

Prilagodba: desna rotacija čvora T.

![bst-LL](images/bst-LL.svg)

Tip RR: slično tipu LL, desno podstablo desnog djeteta od T predugo je i narušava balans.

Prilagodba: lijeva rotacija čvora T.

![bst-RR](images/bst-RR.svg)

Tip LR: desno podstablo lijevog djeteta od T predugo je i narušava balans.

Prilagodba: prvo lijeva rotacija čvora L, čime nastaje tip LL, a zatim desna rotacija čvora T.

![bst-LR](images/bst-LR.svg)

Tip RL: slično tipu LR, lijevo podstablo desnog djeteta od T predugo je i narušava balans.

Prilagodba: prvo desna rotacija čvora R, čime nastaje tip RR, a zatim lijeva rotacija čvora T.

![bst-RL](images/bst-RL.svg)
