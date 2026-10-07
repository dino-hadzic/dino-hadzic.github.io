---
title: Lijevo nagnuto crveno-crno stablo
---

author: c-forrest, Enter-tainer, giiiiiithub, hly1204, iamtwz, Ir1d, kigawas, ksyx, luxuryspark567, mgt, orzAtalod, sandyzikun, SunsetGlow95, Tiphereth-A, current2020, untitledunrevised, yuhuoji

Lijevo nagnuto crveno-crno stablo (left-leaning red-black tree) inačica je [crveno-crnog stabla](./rbtree.md) koja ograničava položaje crvenih bridova (čvorova), tako da njegove operacije umetanja i brisanja odgovaraju jedan-na-jedan operacijama [2-3 stabla](https://en.wikipedia.org/wiki/2%E2%80%933_tree).

Pretpostavljamo da čitatelj već poznaje barem jednu vrstu balansiranog stabla koje se temelji na rotacijama, pa rotacije ovdje ne objašnjavamo.

## Crveno-crno stablo

### Svojstva

Crveno-crno stablo zadovoljava sljedeća svojstva:

1.  Čvorovi su crveni ili crni;
2.  NIL čvorovi (prazni listovi) crni su;
3.  Sva djeca crvenog čvora moraju biti crna; drugim riječima, ni na jednom putu od lista do korijena ne smiju postojati dva uzastopna crvena čvora;
4.  Svi jednostavni putovi od bilo kojeg čvora do svakog lista u njegovu podstablu sadrže jednak broj crnih čvorova (ravnoteža crne visine).

To jamči da najdulji put od korijena do lista (naizmjenično crveni i crni čvorovi) nije dulji od dvostruke duljine najkraćeg puta (svi čvorovi crni), čime se osigurava ravnoteža stabla.

Održavanje tih svojstava prilično je složeno. Novi čvor najprije moramo obojiti u crveno jer bismo inače narušili svojstvo 4. I tada možemo narušiti svojstvo 3, pa su potrebne prilagodbe. Brisanje je još nezgodnije: slično umetanju, ne možemo izbrisati crni čvor jer bismo narušili ravnotežu crne visine. Kako te probleme jednostavno riješiti?

## Lijevo nagnuto crveno-crno stablo (Left Leaning Red Black Tree)

### Objašnjenje

Lijevo nagnuto crveno-crno stablo inačica je crveno-crnog stabla koju je lako implementirati.

Na sljedećim prikazima lijevo nagnutog crveno-crnog stabla boju imaju bridovi, a ne čvorovi. Bojom čvora uobičajeno nazivamo boju brida prema njegovu roditelju.

Lijevo nagnuto crveno-crno stablo dodatno ograničava crveno-crno stablo: lijevo i desno dijete crnog čvora:

-   ili oba crna;
-   ili lijevo crveno, a desno crno.

Dopušteni slučajevi:

![llrbt1](./images/llrbt-1.png)

Nedopušteni slučajevi:

![llrbt2](./images/llrbt-2.png)

To je svojstvo „lijeve nagnutosti”: crveni bridovi mogu biti nagnuti samo ulijevo.

### Postupak

#### Umetanje

Najprije običnim BST umetanjem dodamo crveni list na dno stabla. Zatim prilagodbama odozdo prema gore ponovno uspostavljamo svojstva lijevo nagnutog crveno-crnog stabla. Postupak prilagodbe opisan je u nastavku:

![llrbt3](./images/llrbt-3.png)

Nakon umetanja može nastati crveni brid nagnut udesno. Tada izvodimo jednu lijevu rotaciju:

![llrbt4](./images/llrbt-4.png)

Razmotrimo slučaj kada nakon lijeve rotacije nastanu dva uzastopna crvena brida nagnuta ulijevo:

![llrbt5](./images/llrbt-5.png)

Tada treba izvesti desnu rotaciju. Nakon nje primjenjujemo `color_flip`, odnosno obrnemo boju tog čvora i obaju njegovih sinova.

![llrbt6](./images/llrbt-6.png)

Time uklanjamo crveni brid nagnut udesno.

??? note "Referentni kod (dio)"
    ```cpp
    template <class Key, class Compare>
    typename Set<Key, Compare>::Node *Set<Key, Compare>::fix_up(
        Set::Node *root) const {
      if (is_red(root->rc) && !is_red(root->lc))  // ispravi crvenu vezu nagnutu udesno
        root = rotate_left(root);
      if (is_red(root->lc) &&
          is_red(root->lc->lc))  // ispravi dvije uzastopne crvene veze nagnute ulijevo
        // ako je (root->lc == nullptr), drugi se izraz neće izračunati
        root = rotate_right(root);
      if (is_red(root->lc) && is_red(root->rc))
        // razdvoji 4-čvor
        color_flip(root);
      root->size = size(root->lc) + size(root->rc) + 1;
      return root;
    }
    
    template <class Key, class Compare>
    typename Set<Key, Compare>::Node_Set<Key, Compare>::insert(
        Set::Node_root, const Key &key) const {
      if (root == nullptr) return new Node(key, kRed, 1);
      if (root->key == key)
        ;
      else if (cmp\_(key, root->key))  // if (key < root->key)
        root->lc = insert(root->lc, key);
      else
        root->rc = insert(root->rc, key);
      return fix_up(root);
    }
    ```

#### Brisanje

Brisanje se temelji na sljedećoj ideji: ne možemo izbrisati crni čvor jer bismo narušili crnu visinu. Zato trebamo osigurati da čvor koji na kraju brišemo bude crven.

##### Brisanje čvora s najmanjom vrijednošću

Najprije pokušajmo izbrisati najmanju vrijednost u cijelom stablu.

Kako osigurati da čvor koji na kraju brišemo bude crven? Pri rekurzivnom spuštanju moramo održavati jedno svojstvo: ako je trenutačni čvor `h`, onda `h` ili `h->lc` mora biti crven.

Zašto je to ispravno? Ako različitim rotacijama i obrtanjem boja uspješno održavamo to svojstvo, kada dođemo do najmanjeg čvora `h_min`, crven je ili `h_min` ili njegovo lijevo podstablo — ali `h_min` uopće nema lijevo podstablo! Time je zajamčeno da je najmanji čvor crven. Možemo ga bez bojazni izbrisati i zatim prilagoditi stablo istom idejom kao pri umetanju.

Sada razmotrimo kako održavati to svojstvo. Pri rekurzivnom spuštanju **privremeno** narušavamo neka svojstva lijevo nagnutog crveno-crnog stabla, ali ih pri povratku iz rekurzije obnavljamo.

Donja slika prikazuje jednostavniji slučaj: `h->rc->lc` je crn, pa je dovoljno jedno obrtanje boja:

![llrbt-7](./images/llrbt-7.png)

Nakon prikazanog obrtanja `h->rc` i `h->rc->lc` neće tvoriti dva uzastopna crvena brida.

No ako je `h->rc->lc` crven, slučaj je složeniji:

![llrbt-8](./images/llrbt-8.png)

Samo obrtanje boja stvorilo bi uzastopne crvene bridove koje pri povratku iz rekurzije ne bismo mogli popraviti, pa taj slučaj treba posebno obraditi.

Zatim možemo provesti brisanje:

??? note "Referentni kod (dio)"
    ```cpp
    template <class Key, class Compare>
    typename Set<Key, Compare>::Node *Set<Key, Compare>::move_red_left(
        Set::Node *root) const {
      color_flip(root);
      if (is_red(root->rc->lc)) {
        // pretpostavimo da vrijedi root->rc != nullptr pri pozivu ove funkcije
        root->rc = rotate_right(root->rc);
        root = rotate_left(root);
        color_flip(root);
      }
      return root;
    }
    
    template <class Key, class Compare>
    typename Set<Key, Compare>::Node *Set<Key, Compare>::delete_min(
        Set::Node *root) const {
      if (root->lc == nullptr) {
        delete root;
        return nullptr;
      }
      if (!is_red(root->lc) && !is_red(root->lc->lc)) {
        // osiguraj da je root->lc ili root->lc->lc crven
        // tako osiguravamo da ćemo na kraju izbrisati crveni čvor
        root = move_red_left(root);
      }
      root->lc = delete_min(root->lc);
      return fix_up(root);
    }
    ```

##### Brisanje proizvoljnog čvora

Najprije razmotrimo brisanje lista. Kao pri brisanju minimuma, i pri brisanju proizvoljne vrijednosti održavamo svojstvo. Sada se, međutim, ne krećemo samo ulijevo, nego u oba smjera. Zato održavamo sljedeće: ako idemo ulijevo iz trenutačnog čvora `h`, onda `h` ili `h->lc` mora biti crven; ako idemo udesno iz trenutačnog čvora `h`, onda `h` ili `h->rc` mora biti crven. Time jamčimo da ćemo na kraju uvijek izbrisati crveni čvor.

Za brisanje čvora koji nije list dovoljno je pronaći najmanji čvor u njegovu desnom podstablu (ako ono postoji), zamijeniti vrijednost tog čvora najmanjom vrijednošću desnog podstabla, a zatim izbrisati najmanji čvor iz desnog podstabla.

![llrbt-9](./images/llrbt-9.png)

Što ako nema desnog podstabla? Rotacijom premjestimo lijevo podstablo na desnu stranu i problem nestaje.

??? note "Referentni kod (dio)"
    ```cpp
    template <class Key, class Compare>
    typename Set<Key, Compare>::Node *Set<Key, Compare>::delete_arbitrary(
        Set::Node *root, Key key) const {
      if (cmp_(key, root->key)) {
        // key < root->key
        if (!is_red(root->lc) && !(is_red(root->lc->lc)))
          root = move_red_left(root);
        // održi invarijantu: root->lc ili root->lc->lc (odnosno root i
        // root->lc nakon ulaska u funkciju) crven je, da bismo
        // na kraju izbrisali crveni čvor. Tako nećemo narušiti ravnotežu crne
        // visine
        root->lc = delete_arbitrary(root->lc, key);
      } else {
        // key >= root->key
        if (is_red(root->lc)) root = rotate_right(root);
        if (key == root->key && root->rc == nullptr) {
          delete root;
          return nullptr;
        }
        if (!is_red(root->rc) && !is_red(root->rc->lc)) root = move_red_right(root);
        if (key == root->key) {
          root->key = get_min(root->rc);
          root->rc = delete_min(root->rc);
        } else {
          root->rc = delete_arbitrary(root->rc, key);
        }
      }
      return fix_up(root);
    }
    ```

## Implementacija

Sljedeći kod implementira `Set`, odnosno uređeni skup bez ponovljenih elemenata, pomoću lijevo nagnutog crveno-crnog stabla:

??? note "Referentni kod"
    ```cpp
    #include <algorithm>
    #include <memory>
    #include <vector>
    
    template <class Key, class Compare = std::less<Key>>
    class Set {
     private:
      enum NodeColor { kBlack = 0, kRed = 1 };
    
      struct Node {
        Key key;
        Node *lc{nullptr}, *rc{nullptr};
        size_t size{0};
        NodeColor color;  // boja veze prema roditelju
    
        Node(Key key, NodeColor color, size_t size)
            : key(key), color(color), size(size) {}
    
        Node() = default;
      };
    
      void destroyTree(Node *root) const {
        if (root != nullptr) {
          destroyTree(root->lc);
          destroyTree(root->rc);
          root->lc = root->rc = nullptr;
          delete root;
        }
      }
    
      bool is_red(const Node *nd) const {
        return nd == nullptr ? false : nd->color;  // kRed == 1, kBlack == 0
      }
    
      size_t size(const Node *nd) const { return nd == nullptr ? 0 : nd->size; }
    
      Node *rotate_left(Node *node) const {
        // lijeva rotacija crvene veze
        //          <1>                   <2>
        //        /    \\               //    \
        //       *      <2>    ==>     <1>     *
        //             /   \          /   \
        //            *     *        *     *
        Node *res = node->rc;
        node->rc = res->lc;
        res->lc = node;
        res->color = node->color;
        node->color = kRed;
        res->size = node->size;
        node->size = size(node->lc) + size(node->rc) + 1;
        return res;
      }
    
      Node *rotate_right(Node *node) const {
        // desna rotacija crvene veze
        //            <1>               <2>
        //          //    \           /    \\
        //         <2>     *   ==>   *      <1>
        //        /   \                    /   \
        //       *     *                  *     *
        Node *res = node->lc;
        node->lc = res->rc;
        res->rc = node;
        res->color = node->color;
        node->color = kRed;
        res->size = node->size;
        node->size = size(node->lc) + size(node->rc) + 1;
        return res;
      }
    
      NodeColor neg_color(NodeColor n) const { return n == kBlack ? kRed : kBlack; }
    
      void color_flip(Node *node) const {
        node->color = neg_color(node->color);
        node->lc->color = neg_color(node->lc->color);
        node->rc->color = neg_color(node->rc->color);
      }
    
      Node *insert(Node *root, const Key &key) const;
      Node *delete_arbitrary(Node *root, Key key) const;
      Node *delete_min(Node *root) const;
      Node *move_red_right(Node *root) const;
      Node *move_red_left(Node *root) const;
      Node *fix_up(Node *root) const;
      const Key &get_min(Node *root) const;
      void serialize(Node *root, std::vector<Key> *) const;
      void print_tree(Set::Node *root, int indent) const;
      Compare cmp_ = Compare();
      Node *root_{nullptr};
    
     public:
      using KeyType = Key;
      using ValueType = Key;
      using SizeType = std::size_t;
      using DifferenceType = std::ptrdiff_t;
      using KeyCompare = Compare;
      using ValueCompare = Compare;
      using Reference = Key &;
      using ConstReference = const Key &;
    
      Set() = default;
    
      Set(Set &) = default;
    
      Set(Set &&) noexcept = default;
    
      ~Set() { destroyTree(root_); }
    
      SizeType size() const;
    
      SizeType count(const KeyType &key) const;
    
      SizeType erase(const KeyType &key);
    
      void clear();
    
      void insert(const KeyType &key);
    
      bool empty() const;
    
      std::vector<Key> serialize() const;
    
      void print_tree() const;
    };
    
    template <class Key, class Compare>
    typename Set<Key, Compare>::SizeType Set<Key, Compare>::count(
        ConstReference key) const {
      Node *x = root_;
      while (x != nullptr) {
        if (key == x->key) return 1;
        if (cmp_(key, x->key))  // if (key < x->key)
          x = x->lc;
        else
          x = x->rc;
      }
      return 0;
    }
    
    template <class Key, class Compare>
    typename Set<Key, Compare>::SizeType Set<Key, Compare>::erase(
        const KeyType &key) {
      if (count(key) > 0) {
        if (!is_red(root_->lc) && !(is_red(root_->rc))) root_->color = kRed;
        root_ = delete_arbitrary(root_, key);
        if (root_ != nullptr) root_->color = kBlack;
        return 1;
      } else {
        return 0;
      }
    }
    
    template <class Key, class Compare>
    void Set<Key, Compare>::clear() {
      destroyTree(root_);
      root_ = nullptr;
    }
    
    template <class Key, class Compare>
    void Set<Key, Compare>::insert(const KeyType &key) {
      root_ = insert(root_, key);
      root_->color = kBlack;
    }
    
    template <class Key, class Compare>
    bool Set<Key, Compare>::empty() const {
      return size(root_) == 0;
    }
    
    template <class Key, class Compare>
    typename Set<Key, Compare>::Node *Set<Key, Compare>::insert(
        Set::Node *root, const Key &key) const {
      if (root == nullptr) return new Node(key, kRed, 1);
      if (root->key == key)
        ;
      else if (cmp_(key, root->key))  // if (key < root->key)
        root->lc = insert(root->lc, key);
      else
        root->rc = insert(root->rc, key);
      return fix_up(root);
    }
    
    template <class Key, class Compare>
    typename Set<Key, Compare>::Node *Set<Key, Compare>::delete_min(
        Set::Node *root) const {
      if (root->lc == nullptr) {
        delete root;
        return nullptr;
      }
      if (!is_red(root->lc) && !is_red(root->lc->lc)) {
        // osiguraj da je root->lc ili root->lc->lc crven
        // tako osiguravamo da ćemo na kraju izbrisati crveni čvor
        root = move_red_left(root);
      }
      root->lc = delete_min(root->lc);
      return fix_up(root);
    }
    
    template <class Key, class Compare>
    typename Set<Key, Compare>::Node *Set<Key, Compare>::move_red_right(
        Set::Node *root) const {
      color_flip(root);
      if (is_red(root->lc->lc)) {  // pretpostavimo da vrijedi root->lc != nullptr pri pozivu
                                   // ove funkcije
        root = rotate_right(root);
        color_flip(root);
      }
      return root;
    }
    
    template <class Key, class Compare>
    typename Set<Key, Compare>::Node *Set<Key, Compare>::move_red_left(
        Set::Node *root) const {
      color_flip(root);
      if (is_red(root->rc->lc)) {
        // pretpostavimo da vrijedi root->rc != nullptr pri pozivu ove funkcije
        root->rc = rotate_right(root->rc);
        root = rotate_left(root);
        color_flip(root);
      }
      return root;
    }
    
    template <class Key, class Compare>
    typename Set<Key, Compare>::Node *Set<Key, Compare>::fix_up(
        Set::Node *root) const {
      if (is_red(root->rc) && !is_red(root->lc))  // ispravi crvenu vezu nagnutu udesno
        root = rotate_left(root);
      if (is_red(root->lc) &&
          is_red(root->lc->lc))  // ispravi dvije uzastopne crvene veze nagnute ulijevo
        // ako je (root->lc == nullptr), drugi se izraz neće izračunati
        root = rotate_right(root);
      if (is_red(root->lc) && is_red(root->rc))
        // razdvoji 4-čvor
        color_flip(root);
      root->size = size(root->lc) + size(root->rc) + 1;
      return root;
    }
    
    template <class Key, class Compare>
    const Key &Set<Key, Compare>::get_min(Set::Node *root) const {
      Node *x = root;
      // namjerno će se srušiti ako je root == nullptr
      for (; x->lc != nullptr; x = x->lc);
      return x->key;
    }
    
    template <class Key, class Compare>
    typename Set<Key, Compare>::SizeType Set<Key, Compare>::size() const {
      return size(root_);
    }
    
    template <class Key, class Compare>
    typename Set<Key, Compare>::Node *Set<Key, Compare>::delete_arbitrary(
        Set::Node *root, Key key) const {
      if (cmp_(key, root->key)) {
        // key < root->key
        if (!is_red(root->lc) && !(is_red(root->lc->lc)))
          root = move_red_left(root);
        // održi invarijantu: root->lc ili root->lc->lc (odnosno root i
        // root->lc nakon ulaska u funkciju) crven je, da bismo
        // na kraju izbrisali crveni čvor. Tako nećemo narušiti ravnotežu crne
        // visine
        root->lc = delete_arbitrary(root->lc, key);
      } else {
        // key >= root->key
        if (is_red(root->lc)) root = rotate_right(root);
        if (key == root->key && root->rc == nullptr) {
          delete root;
          return nullptr;
        }
        if (!is_red(root->rc) && !is_red(root->rc->lc)) root = move_red_right(root);
        if (key == root->key) {
          root->key = get_min(root->rc);
          root->rc = delete_min(root->rc);
        } else {
          root->rc = delete_arbitrary(root->rc, key);
        }
      }
      return fix_up(root);
    }
    
    template <class Key, class Compare>
    std::vector<Key> Set<Key, Compare>::serialize() const {
      std::vector<int> v;
      serialize(root_, &v);
      return v;
    }
    
    template <class Key, class Compare>
    void Set<Key, Compare>::serialize(Set::Node *root,
                                      std::vector<Key> *res) const {
      if (root == nullptr) return;
      serialize(root->lc, res);
      res->push_back(root->key);
      serialize(root->rc, res);
    }
    
    template <class Key, class Compare>
    void Set<Key, Compare>::print_tree(Set::Node *root, int indent) const {
      if (root == nullptr) return;
      print_tree(root->lc, indent + 4);
      std::cout << std::string(indent, '-') << root->key << std::endl;
      print_tree(root->rc, indent + 4);
    }
    
    template <class Key, class Compare>
    void Set<Key, Compare>::print_tree() const {
      print_tree(root_, 0);
    }
    ```

## Veza s 2-3 stablima

2-3 stablo B-stablo je reda 3. Svaki je čvor 2-čvor ili 3-čvor i pohranjuje jedan ili dva podatkovna elementa. Unutarnji 2-čvorovi imaju točno dvoje, a 3-čvorovi točno troje djece. Svi su podaci u 2-3 stablu uređeni.

2-3 stabla i lijevo nagnuta crveno-crna stabla u biti su ekvivalentna. Čvor 2-3 stabla može pohraniti 1 ili 2 elementa, dok čvor crveno-crnog stabla može pohraniti samo jedan. Kao na donjoj slici, 2-čvor odgovara jednom crnom čvoru, a 3-čvor jednom crvenom i jednom crnom čvoru (b i c možemo promatrati kao čvorove na istoj razini).

![2-3-tree-rbt](images/2-3-tree-rbt-1.svg)

![2-3-tree-rbt](images/2-3-tree-rbt-2.svg)

Donja slika prikazuje lijevo nagnuto crveno-crno stablo koje odgovara jednom 2-3 stablu.

![2-3-tree-rbt](images/2-3-tree-rbt-3.svg)

Operacije umetanja i brisanja u 2-3 stablima i lijevo nagnutim crveno-crnim stablima odgovaraju jedan-na-jedan.[^23-vs-llrbt]

## Literatura i dodatni materijali

-   [Left-Leaning Red-Black Trees](https://sedgewick.io/wp-content/themes/sedgewick/papers/2008LLRB.pdf)-  Robert Sedgewick Princeton University
-   [Balanced Search Trees](https://algs4.cs.princeton.edu/lectures/keynote/33BalancedSearchTrees-2x2.pdf)-\_Algorithms\_Robert Sedgewick | Kevin Wayne

[^23-vs-llrbt]: [Ovaj članak na blogu](https://riteme.site/blog/2016-3-12/2-3-tree-and-red-black-tree.html) daje detaljan opis. Izraz „crveno-crno stablo” u njemu zapravo označava „lijevo nagnuto crveno-crno stablo”.
