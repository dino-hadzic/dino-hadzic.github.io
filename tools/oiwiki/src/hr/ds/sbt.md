---
title: Size Balanced Tree
---

Size Balanced Tree (SBT) je samobalansirajuće binarno stablo pretraživanja (Self-Balanced Binary Search Tree, SBBST) koje je 2007. predložio kineski OI natjecatelj Chen Qifeng. Ravnotežu održava provjerom broja čvorova u podstablima. Za razliku od uobičajenih samobalansirajućih binarnih stabala pretraživanja, kao što su crveno-crna i AVL stabla, Size Balanced Tree podržava upite o rangu (rank) određenog ključa u stablu u vremenskoj složenosti $O(\log n)$.

## Definicija čvora

U usporedbi s običnim binarnim stablom pretraživanja, svaki čvor $N$ SBT-a treba održavati samo jedno dodatno cjelobrojno polje `size`, koje pohranjuje broj čvorova u podstablu s korijenom $N$. Tip čvora `Node` definiran je ovako:

| Identifikator | Tip     | Opis |
| ---------- | ------- | --------------- |
| `left`     | `Node*` | Pokazivač na lijevo dijete |
| `right`    | `Node*` | Pokazivač na desno dijete |
| `size`     | `int`   | Broj čvorova u podstablu s ovim čvorom kao korijenom |

## Svojstva

Svaki čvor $N$ stabla Size Balanced Tree zadovoljava sljedeća svojstva:

```text
size(N.left) >= size(N.right.left)
size(N.left) >= size(N.right.right)
size(N.right) >= size(N.left.left)
size(N.right) >= size(N.left.right)
```

Drugim riječima, `size` bilo kojeg čvora nije manji od vrijednosti `size` bilo kojeg djeteta njegova brata (nephew).

## Održavanje ravnoteže

### Rotacije

SBT održava ravnotežu uglavnom rotacijama koje mijenjaju njegovu visinu. Rotacije su slične onima u većini samobalansirajućih binarnih stabala pretraživanja. Jedina je razlika u tome što nakon rotacije treba ažurirati `size` čvorova kojima se promijenilo lijevo ili desno dijete. Primjer koda:

```cpp
void updateSize() {
  USize leftSize = this->left != nullptr ? this->left->size : 0;
  USize rightSize = this->right != nullptr ? this->right->size : 0;
  this->size = leftSize + rightSize + 1;
}

static void rotateLeft(NodePtr& node) {
  assert(node != nullptr);
  // clang-format off
  //     |                       |
  //     N                       S
  //    / \     l-rotate(N)     / \
  //   L   S    ==========>    N   R
  //      / \                 / \
  //     M   R               L   M
  // clang-format on
  NodePtr successor = node->right;
  node->right = successor->left;
  successor->left = node;

  node->updateSize();
  successor->updateSize();

  node = successor;
}

static void rotateRight(NodePtr& node) {
  assert(node != nullptr);
  // clang-format off
  //       |                   |
  //       N                   S
  //      / \   r-rotate(N)   / \
  //     S   R  ==========>  L   N
  //    / \                     / \
  //   L   M                   M   R
  // clang-format on
  NodePtr successor = node->left;
  node->left = successor->right;
  successor->right = node;

  node->updateSize();
  successor->updateSize();

  node = successor;
}
```

### Održavanje

#### Slučaj 1

`size(N.left) < size(N.right.left)`

```cpp
if (size(node->right->left) > size(node->left)) {
  // clang-format off
  //     |                     |                      |
  //     N                     N                     [M]
  //    / \    r-rotate(R)    / \     l-rotate(N)    / \
  //  <L>  R   ==========>  <L> [M]   ==========>   N   R
  //      /                       \                /
  //    [M]                        R             <L>
  // clang-format on
  rotateRight(node->right);
  rotateLeft(node);
  fixBalance(node->left);
  fixBalance(node->right);
  fixBalance(node);
  return;
}
```

#### Slučaj 2

`size(N.left) < size(N.right.right)`

```cpp
if (size(node->right->right) > size(node->left)) {
  // clang-format off
  //     |                       |
  //     N                       R
  //    / \     l-rotate(N)     / \
  //  <L>  R    ==========>    N  [M]
  //        \                 /
  //        [M]             <L>
  // clang-format on
  rotateLeft(node);
  fixBalance(node->left);
  fixBalance(node);
  return;
}
```

#### Slučaj 3

`size(N.right) < size(N.left.left)`

```cpp
if (size(node->left->left) > size(node->right)) {
  // clang-format off
  //       |                       |
  //       N                       L
  //      / \     r-rotate(N)     / \
  //     L  <R>   ==========>   [M]  N
  //    /                             \
  //  [M]                             <R>
  // clang-format on
  rotateRight(node);
  fixBalance(node->right);
  fixBalance(node);
  return;
}
```

#### Slučaj 4

`size(N.right) < size(N.left.right)`

```cpp
if (size(node->left->right) > size(node->right)) {
  // clang-format off
  //     |                     |                      |
  //     N                     N                     [M]
  //    / \    l-rotate(L)    / \     r-rotate(N)    / \
  //   L  <R>  ==========>  [M] <R>   ==========>   L   N
  //    \                   /                            \
  //    [M]                L                             <R>
  // clang-format on
  rotateLeft(node->left);
  rotateRight(node);
  fixBalance(node->left);
  fixBalance(node->right);
  fixBalance(node);
  return;
}
```

## Operacije

### Umetanje

Pri umetanju u SBT nakon običnog umetanja u binarno stablo pretraživanja rekurzivno ažuriramo polje `size` čvorova i održavamo ravnotežu. Primjer koda:

```cpp
if (compare(key, node->key)) {
  /* key < node->key */
  if (node->left == nullptr) {
    node->left = Node::from(key, value);
    node->updateSize();
  } else {
    insert(node->left, key, value, replace);
    node->updateSize();
    fixBalance(node);
  }
} else {
  /* key > node->key */
  if (node->right == nullptr) {
    node->right = Node::from(key, value);
    node->updateSize();
  } else {
    insert(node->right, key, value, replace);
    node->updateSize();
    fixBalance(node);
  }
}
```

### Brisanje

Chen Qifeng, autor stabla Size Balanced Tree, ovako opisuje brisanje u svojem radu:

> Ono može narušiti svojstva SBT-a. Međutim, uz prethodno opisano umetanje visina BST-a i dalje ostaje $O(\log n)$, gdje je $n$ ukupan broj umetanja, a ne trenutačna veličina.

Iako brisanje može narušiti svojstva SBT-a, ono ne povećava visinu stabla pa ne utječe na učinkovitost kasnijih operacija. U praksi, međutim, ako nakon skupine umetanja slijedi samo velik broj brisanja i upita, neravnoteža stabla ipak može utjecati na ukupnu učinkovitost. Zato implementacija brisanja u ovom članku ipak uključuje održavanje ravnoteže. Referentni kod:

```cpp
bool remove(NodePtr& node, K key, NodeConsumer action) {
  assert(node != nullptr);

  if (key != node->key) {
    if (compare(key, node->key)) {
      /* key < node->key */
      NodePtr& left = node->left;
      if (left != nullptr && remove(left, key, action)) {
        node->updateSize();
        fixBalance(node);
        return true;
      } else {
        return false;
      }
    } else {
      /* key > node->key */
      NodePtr& right = node->right;
      if (right != nullptr && remove(right, key, action)) {
        node->updateSize();
        fixBalance(node);
        return true;
      } else {
        return false;
      }
    }
  }

  assert(key == node->key);
  action(node);

  if (node->isLeaf()) {
    // Slučaj 1: nema djece
    node = nullptr;
  } else if (node->right == nullptr) {
    // Slučaj 2: samo lijevo dijete
    // clang-format off
    //     P
    //     |  remove(N)  P
    //     N  ========>  |
    //    /              L
    //   L
    // clang-format on
    node = node->left;
  } else if (node->left == nullptr) {
    // Slučaj 3: samo desno dijete
    // clang-format off
    //   P
    //   |    remove(N)  P
    //   N    ========>  |
    //    \              R
    //     R
    // clang-format on
    node = node->right;
  } else if (node->right->left == nullptr) {
    // Slučaj 4: lijevo i desno dijete, desno dijete nema lijevog djeteta
    // clang-format off
    //    |                 |
    //    N    remove(N)    R
    //   / \   ========>   /
    //  L   R             L
    // clang-format on
    NodePtr right = node->right;
    swapNode(node, right);
    right->right = node->right;
    node = right;
    node->updateSize();
    fixBalance(node);
  } else {
    // Slučaj 5: lijevo i desno dijete, desno dijete nije list
    // clang-format off
    //   Korak 1. pronađi čvor N s najmanjim ključem
    //           i njegova roditelja P u desnom podstablu
    //   Korak 2. zamijeni S i N
    //   Korak 3. ukloni čvor N kao u slučaju 1 ili 3
    //   Korak 4. ažuriraj veličine svih čvorova na putu
    //           od S do P
    //     |                  |
    //     N                  S                 |
    //    / \                / \                S
    //   L  ..  swap(N, S)  L  ..  remove(N)   / \
    //       |  =========>      |  ========>  L  ..
    //       P                  P                 |
    //      / \                / \                P
    //     S  ..              N  ..              / \
    //      \                  \                R  ..
    //       R                  R
    //
    // clang-format on

    std::stack<NodePtr> path;

    // Korak 1
    NodePtr successor = node->right;
    NodePtr parent = node;
    path.push(node);

    while (successor->left != nullptr) {
      path.push(successor);
      parent = successor;
      successor = parent->left;
    }

    // Korak 2
    swapNode(node, successor);

    // Korak 3
    parent->left = node->right;
    // Vrati čvor
    node = successor;

    // Korak 4
    while (!path.empty()) {
      path.top()->updateSize();
      path.pop();
    }
  }

  return true;
}
```

Valja primijetiti da u slučaju 5 prethodnog koda, nakon zamjene čvora $N$ koji brišemo njegovim sljedbenikom $S$ (može se odabrati i prethodnik) i brisanja premještenog čvora $N$, treba ažurirati polje `size` svih čvorova na putu od izvornog roditelja $P$ čvora $S$ do novog položaja čvora $S$, kao što prikazuje komentar u kodu. Ova implementacija sprema čvorove na putu na stog, a zatim ih skida i ažurira obrnutim redoslijedom obilaska.

### Upiti o rangu

Budući da čvorovi SBT-a pohranjuju broj čvorova u podstablu, rang određenog ključa `key` (ili broj čvorova većih/manjih od tog ključa) možemo odrediti u vremenskoj složenosti $O(\log n)$. Primjer koda:

```cpp
USize countLess(ConstNodePtr node, K key, bool countEqual = false) const {
  if (node == nullptr) {
    return 0;
  } else if (key < node->key) {
    return countLess(node->left, key, countEqual);
  } else if (key > node->key) {
    return size(node->left) + 1 + countLess(node->right, key, countEqual);
  } else {
    return size(node->left) + (countEqual ? 1 : 0);
  }
}

USize countGreater(ConstNodePtr node, K key, bool countEqual = false) const {
  if (node == nullptr) {
    return 0;
  } else if (key < node->key) {
    return size(node->right) + 1 + countGreater(node->left, key, countEqual);
  } else if (key > node->key) {
    return countGreater(node->right, key, countEqual);
  } else {
    return size(node->right) + (countEqual ? 1 : 0);
  }
}
```

## Referentni kod

Sljedeći kod implementira `Map`, odnosno uređeno preslikavanje bez ponovljenih ključeva, pomoću SBT-a:

??? note "Potpuni kod"
    ```cpp
    --8<-- "docs/ds/code/size-balanced-tree/SizeBalancedTreeMap.hpp"
    ```
