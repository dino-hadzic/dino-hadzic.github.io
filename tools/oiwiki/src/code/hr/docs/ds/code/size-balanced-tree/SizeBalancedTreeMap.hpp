/**
 * @file SizeBalancedTreeMap.hpp
 * @brief Implementacija mape pomoću stabla Size Balanced Tree
 * @details Mapa je uređena prema prirodnom poretku svojih
 *  ključeva ili zadanoj funkciji {@code Compare}; ova implementacija
 *  jamči vremensku složenost log(n) za operacije contains, get, insert
 *  i remove.
 * @author [r.ivance](https://github.com/RIvance)
 */

#ifndef SIZE_BALANCED_TREE_MAP_HPP
#define SIZE_BALANCED_TREE_MAP_HPP

#include <cassert>
#include <cstddef>
#include <cstdint>
#include <functional>
#include <memory>
#include <stack>
#include <utility>
#include <vector>

/**
 * Implementacija mape pomoću stabla Size Balanced Tree
 * http://wcipeg.com/wiki/Size_Balanced_Tree
 * @tparam Key tip ključeva u ovoj mapi
 * @tparam Value tip pridruženih vrijednosti
 * @tparam Compare funkcija usporedbe
 */
template <typename Key, typename Value, typename Compare = std::less<Key> >
class SizeBalancedTreeMap {
 private:
  using USize = size_t;

  Compare compare = Compare();

 public:
  struct Entry {
    Key key;
    Value value;

    bool operator==(const Entry &rhs) const noexcept {
      return this->key == rhs.key && this->value == rhs.value;
    }

    bool operator!=(const Entry &rhs) const noexcept {
      return this->key != rhs.key || this->value != rhs.value;
    }
  };

 private:
  struct Node {
    using Ptr = std::shared_ptr<Node>;
    using Provider = const std::function<Ptr(void)> &;
    using Consumer = const std::function<void(const Ptr &)> &;

    Key key;
    Value value{};

    Ptr left = nullptr;
    Ptr right = nullptr;

    USize size = 1;

    explicit Node(Key k) : key(std::move(k)) {}

    explicit Node(Key k, Value v) : key(std::move(k)), value(std::move(v)) {}

    ~Node() = default;

    inline bool isLeaf() const noexcept {
      return this->left == nullptr && this->right == nullptr;
    }

    inline void updateSize() {
      USize leftSize = this->left != nullptr ? this->left->size : 0;
      USize rightSize = this->right != nullptr ? this->right->size : 0;
      this->size = leftSize + rightSize + 1;
    }

    inline Entry entry() const { return Entry{key, value}; }

    static Ptr from(const Key &k) { return std::make_shared<Node>(Node(k)); }

    static Ptr from(const Key &k, const Value &v) {
      return std::make_shared<Node>(Node(k, v));
    }
  };

  using NodePtr = typename Node::Ptr;
  using ConstNodePtr = const NodePtr &;
  using NodeProvider = typename Node::Provider;
  using NodeConsumer = typename Node::Consumer;

  NodePtr root = nullptr;

  using K = const Key &;
  using V = const Value &;

 public:
  using EntryList = std::vector<Entry>;
  using KeyValueConsumer = const std::function<void(K, V)> &;
  using MutKeyValueConsumer = const std::function<void(K, Value &)> &;
  using KeyValueFilter = const std::function<bool(K, V)> &;

  class NoSuchMappingException : protected std::exception {
   private:
    const char *message;

   public:
    explicit NoSuchMappingException(const char *msg) : message(msg) {}

    const char *what() const noexcept override { return message; }
  };

  SizeBalancedTreeMap() noexcept = default;

  /**
   * Vraća broj unosa u ovoj mapi.
   * @return size_t
   */
  inline USize size() const noexcept {
    if (this->root != nullptr) {
      return this->root->size;
    } else {
      return 0;
    }
  }

  /**
   * Vraća true ako ova kolekcija nema elemenata.
   * @return bool
   */
  inline bool empty() const noexcept { return this->root == nullptr; }

  /**
   * Uklanja sve elemente iz ove mape.
   */
  void clear() noexcept { this->root = nullptr; }

  /**
   * Vraća vrijednost pridruženu zadanom ključu; ako ova mapa
   * nema unos za taj ključ, iznimka {@code NoSuchMappingException} bit će
   * bačena.
   * @param key
   * @return SizeBalancedTreeMap<Key, Value>::Value
   * @throws NoSuchMappingException
   */
  Value get(K key) const {
    if (this->root == nullptr) {
      throw NoSuchMappingException("Invalid key");
    } else {
      NodePtr node = this->getNode(this->root, key);
      if (node != nullptr) {
        return node->value;
      } else {
        throw NoSuchMappingException("Invalid key");
      }
    }
  }

  /**
   * Vraća vrijednost pridruženu zadanom ključu; ako ova mapa
   * nema unos za taj ključ, novi unos sa zadanom vrijednošću
   * bit će umetnut.
   * @param key
   * @return SizeBalancedTreeMap<Key, Value>::Value &
   */
  Value &getOrDefault(K key) {
    if (this->root == nullptr) {
      this->root = Node::from(key);
      return this->root->value;
    } else {
      return this
          ->getNodeOrProvide(this->root, key,
                             [&key]() { return Node::from(key); })
          ->value;
    }
  }

  /**
   * Vraća true ako ova mapa sadrži unos za zadani ključ.
   * @param key
   * @return bool
   */
  bool contains(K key) const {
    return this->getNode(this->root, key) != nullptr;
  }

  /**
   * Pridružuje zadanu vrijednost zadanom ključu u ovoj mapi.
   * @param key
   * @param value
   */
  void insert(K key, V value) {
    if (this->root == nullptr) {
      this->root = Node::from(key, value);
    } else {
      this->insert(this->root, key, value);
    }
  }

  /**
   * Ako zadani ključ još nema pridruženu vrijednost, pridružuje
   * mu zadanu vrijednost i vraća true, inače vraća false.
   * @param key
   * @param value
   * @return bool
   */
  bool insertIfAbsent(K key, V value) {
    USize sizeBeforeInsertion = this->size();
    if (this->root == nullptr) {
      this->root = Node::from(key, value);
    } else {
      this->insert(this->root, key, value, false);
    }
    return this->size() > sizeBeforeInsertion;
  }

  /**
   * Ako zadani ključ još nema pridruženu vrijednost, pridružuje
   * mu zadanu vrijednost i vraća je, inače vraća pridruženu
   * vrijednost.
   * @param key
   * @param value
   * @return SizeBalancedTreeMap<Key, Value>::Value &
   */
  Value &getOrInsert(K key, V value) {
    if (this->root == nullptr) {
      this->root = Node::from(key, value);
      return root->value;
    } else {
      NodePtr node = getNodeOrProvide(this->root, key,
                                      [&]() { return Node::from(key, value); });
      return node->value;
    }
  }

  Value operator[](K key) const { return this->get(key); }

  Value &operator[](K key) { return this->getOrDefault(key); }

  /**
   * Uklanja unos za ključ iz ove mape ako postoji;
   * Vraća true ako unos postoji, inače vraća false
   * @param key ključ unosa
   * @return bool
   */
  bool remove(K key) {
    if (this->root == nullptr) {
      return false;
    } else {
      return this->remove(this->root, key, [](ConstNodePtr) {});
    }
  }

  /**
   * Uklanja unos za ključ iz ove mape ako postoji i vraća
   * vrijednost pridruženu ključu; ako ova mapa nema unos za
   * ključ, baca se iznimka {@code NoSuchMappingException}.
   * @param key
   * @return SizeBalancedTreeMap<Key, Value>::Value
   * @throws NoSuchMappingException
   */
  Value getAndRemove(K key) {
    Value result;
    NodeConsumer action = [&](ConstNodePtr node) { result = node->value; };

    if (root == nullptr) {
      throw NoSuchMappingException("Invalid key");
    } else {
      if (remove(this->root, key, action)) {
        return result;
      } else {
        throw NoSuchMappingException("Invalid key");
      }
    }
  }

  /**
   * Dohvaća unos koji odgovara zadanom ključu; ako takav unos ne
   * postoji, vraća unos za najmanji ključ veći od zadanog
   * ključa; ako takav unos ne postoji (tj. najveći ključ u stablu manji je
   * od zadanog ključa), baca se iznimka {@code NoSuchMappingException}.
   * @param key
   * @return SizeBalancedTreeMap<Key, Value>::Entry
   * @throws NoSuchMappingException
   */
  Entry getCeilingEntry(K key) const {
    if (this->root == nullptr) {
      throw NoSuchMappingException("No ceiling entry in this map");
    }

    NodePtr node = this->root;
    std::stack<NodePtr> ancestors;

    while (node != nullptr) {
      if (key == node->key) {
        return node->entry();
      }

      if (compare(key, node->key)) {
        /* key < node->key */
        if (node->left != nullptr) {
          ancestors.push(node);
          node = node->left;
        } else {
          return node->entry();
        }
      } else {
        /* key > node->key */
        if (node->right != nullptr) {
          ancestors.push(node);
          node = node->right;
        } else {
          if (ancestors.empty()) {
            throw NoSuchMappingException("No ceiling entry in this map");
          }

          NodePtr parent = ancestors.top();
          ancestors.pop();

          while (node == parent->right) {
            node = parent;
            if (!ancestors.empty()) {
              parent = ancestors.top();
              ancestors.pop();
            } else {
              throw NoSuchMappingException("No ceiling entry in this map");
            }
          }

          return parent->entry();
        }
      }
    }

    throw NoSuchMappingException("No ceiling entry in this map");
  }

  /**
   * Dohvaća unos koji odgovara zadanom ključu; ako takav unos ne postoji,
   * vraća unos za najveći ključ manji od zadanog ključa;
   * ako takav unos ne postoji, baca se iznimka {@code NoSuchMappingException}.
   * @param key
   * @return SizeBalancedTreeMap<Key, Value>::Entry
   * @throws NoSuchMappingException
   */
  Entry getFloorEntry(K key) const {
    if (this->root == nullptr) {
      throw NoSuchMappingException("No floor entry exists in this map");
    }

    NodePtr node = this->root;
    std::stack<NodePtr> ancestors;

    while (node != nullptr) {
      if (key == node->key) {
        return node->entry();
      }

      if (compare(key, node->key)) {
        /* key < node->key */
        if (node->left != nullptr) {
          ancestors.push(node);
          node = node->left;
        } else {
          if (ancestors.empty()) {
            throw NoSuchMappingException("No floor entry exists in this map");
          }

          NodePtr parent = ancestors.top();
          ancestors.pop();

          while (node == parent->left) {
            node = parent;
            if (!ancestors.empty()) {
              parent = ancestors.top();
              ancestors.pop();
            } else {
              throw NoSuchMappingException("No floor entry exists in this map");
            }
          }

          return parent->entry();
        }
      } else {
        /* key > node->key */
        if (node->right != nullptr) {
          ancestors.push(node);
          node = node->right;
        } else {
          return node->entry();
        }
      }
    }

    throw NoSuchMappingException("No floor entry exists in this map");
  }

  /**
   * Dohvaća unos za najmanji ključ veći od zadanog
   * ključa; ako takav unos ne postoji, vraća unos za najmanji
   * ključ veći od zadanog ključa; ako takav unos ne postoji,
   * baca se iznimka {@code NoSuchMappingException}.
   * @param key
   * @return SizeBalancedTreeMap<Key, Value>::Entry
   * @throws NoSuchMappingException
   */
  Entry getHigherEntry(K key) {
    if (this->root == nullptr) {
      throw NoSuchMappingException("No higher entry exists in this map");
    }

    NodePtr node = this->root;
    std::stack<NodePtr> ancestors;

    while (node != nullptr) {
      if (compare(key, node->key)) {
        /* key < node->key */
        if (node->left != nullptr) {
          ancestors.push(node);
          node = node->left;
        } else {
          return node->entry();
        }
      } else {
        /* key >= node->key */
        if (node->right != nullptr) {
          ancestors.push(node);
          node = node->right;
        } else {
          if (ancestors.empty()) {
            throw NoSuchMappingException("No higher entry exists in this map");
          }

          NodePtr parent = ancestors.top();
          ancestors.pop();

          while (node == parent->right) {
            node = parent;
            if (!ancestors.empty()) {
              parent = ancestors.top();
              ancestors.pop();
            } else {
              throw NoSuchMappingException(
                  "No higher entry exists in this map");
            }
          }

          return parent->entry();
        }
      }
    }

    throw NoSuchMappingException("No higher entry exists in this map");
  }

  /**
   * Vraća unos za najveći ključ manji od zadanog ključa; ako
   * takav unos ne postoji (tj. najmanji ključ u stablu veći je od
   * zadanog ključa), baca se iznimka {@code NoSuchMappingException}.
   * @param key
   * @return SizeBalancedTreeMap<Key, Value>::Entry
   * @throws NoSuchMappingException
   */
  Entry getLowerEntry(K key) const {
    if (this->root == nullptr) {
      throw NoSuchMappingException("No lower entry exists in this map");
    }

    NodePtr node = this->root;
    std::stack<NodePtr> ancestors;

    while (node != nullptr) {
      if (compare(key, node->key) || key == node->key) {
        /* key <= node->key */
        if (node->left != nullptr) {
          ancestors.push(node);
          node = node->left;
        } else {
          if (ancestors.empty()) {
            throw NoSuchMappingException("No lower entry exists in this map");
          }

          NodePtr parent = ancestors.top();
          ancestors.pop();

          while (node == parent->left) {
            node = parent;
            if (!ancestors.empty()) {
              parent = ancestors.top();
              ancestors.pop();
            } else {
              throw NoSuchMappingException("No lower entry exists in this map");
            }
          }

          return parent->entry();
        }
      } else {
        /* key > node->key */
        if (node->right != nullptr) {
          ancestors.push(node);
          node = node->right;
        } else {
          return node->entry();
        }
      }
    }

    throw NoSuchMappingException("No lower entry exists in this map");
  }

  /**
   * Broji unose s ključem manjim od zadanog ključa
   * @param key
   * @return USize
   */
  USize countLessThan(K key) { return this->countLess(this->root, key); }

  /**
   * Broji unose s ključem manjim ili jednakim zadanom ključu
   * @param key
   * @return USize
   */
  USize countLessOrEqualTo(K key) {
    return this->countLess(this->root, key, true);
  }

  /**
   * Broji unose s ključem većim od zadanog ključa
   * @param key
   * @return USize
   */
  USize countGreaterThan(K key) { return this->countGreater(this->root, key); }

  /**
   * Broji unose s ključem većim ili jednakim zadanom ključu
   * @param key
   * @return USize
   */
  USize countGreaterOrEqualTo(K key) {
    return this->countGreater(this->root, key, true);
  }

  /**
   * Uklanja sve unose koji zadovoljavaju uvjet filtra.
   * @param filter
   */
  void removeAll(KeyValueFilter filter) {
    std::vector<Key> keys;
    this->inorderTraversal([&](ConstNodePtr node) {
      if (filter(node->key, node->value)) {
        keys.push_back(node->key);
      }
    });
    for (const Key &key : keys) {
      this->remove(key);
    }
  }

  /**
   * Izvršava zadanu radnju za svaki par ključa i vrijednosti u ovoj mapi.
   * Radnja ne može mijenjati vrijednost.
   * @param action
   */
  void forEach(KeyValueConsumer action) const {
    this->inorderTraversal(
        [&](ConstNodePtr node) { action(node->key, node->value); });
  }

  /**
   * Izvršava zadanu radnju za svaki par ključa i vrijednosti u ovoj mapi.
   * Radnja može mijenjati vrijednost.
   * @param action
   */
  void forEachMut(MutKeyValueConsumer action) {
    this->inorderTraversal(
        [&](ConstNodePtr node) { action(node->key, node->value); });
  }

  /**
   * Vraća popis svih unosa u ovoj mapi.
   * @return SizeBalancedTreeMap<Key, Value>::EntryList
   */
  EntryList toEntryList() const {
    EntryList entryList;
    this->inorderTraversal(
        [&](ConstNodePtr node) { entryList.push_back(node->entry()); });
    return entryList;
  }

 private:
  static USize size(ConstNodePtr node) {
    return node != nullptr ? node->size : 0;
  }

  static void rotateLeft(NodePtr &node) {
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

  static void rotateRight(NodePtr &node) {
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

  static void swapNode(NodePtr &lhs, NodePtr &rhs) {
    std::swap(lhs->key, rhs->key);
    std::swap(lhs->value, rhs->value);
    std::swap(lhs, rhs);
  }

  static void fixBalance(NodePtr &node) {
    if (node == nullptr) {
      return;
    }

    if (node->left != nullptr) {
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
      } else if (size(node->left->right) > size(node->right)) {
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
    }

    if (node->right != nullptr) {
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
      } else if (size(node->right->left) > size(node->left)) {
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
    }
  }

  NodePtr getNodeOrProvide(NodePtr &node, K key, NodeProvider provide) {
    assert(node != nullptr);

    if (key == node->key) {
      return node;
    }

    assert(key != node->key);

    NodePtr result;

    if (compare(key, node->key)) {
      /* key < node->key */
      if (node->left == nullptr) {
        result = node->left = provide();
        node->updateSize();
      } else {
        result = getNodeOrProvide(node->left, key, provide);
        node->updateSize();
        fixBalance(node);
      }
    } else {
      /* key > node->key */
      if (node->right == nullptr) {
        result = node->right = provide();
        node->updateSize();
      } else {
        result = getNodeOrProvide(node->right, key, provide);
        node->updateSize();
        fixBalance(node);
      }
    }

    return result;
  }

  NodePtr getNode(ConstNodePtr node, K key) const {
    assert(node != nullptr);

    if (key == node->key) {
      return node;
    }

    if (compare(key, node->key)) {
      /* key < node->key */
      return node->left == nullptr ? nullptr : getNode(node->left, key);
    } else {
      /* key > node->key */
      return node->right == nullptr ? nullptr : getNode(node->right, key);
    }
  }

  void insert(NodePtr &node, K key, V value, bool replace = true) {
    assert(node != nullptr);

    if (key == node->key) {
      if (replace) {
        node->value = value;
      }
      return;
    }

    assert(key != node->key);

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
  }

  bool remove(NodePtr &node, K key, NodeConsumer action) {
    assert(node != nullptr);

    if (key != node->key) {
      if (compare(key, node->key)) {
        /* key < node->key */
        NodePtr &left = node->left;
        if (left != nullptr && remove(left, key, action)) {
          node->updateSize();
          fixBalance(node);
          return true;
        } else {
          return false;
        }
      } else {
        /* key > node->key */
        NodePtr &right = node->right;
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
      // clang-format off
      // Slučaj 2: samo lijevo dijete
      //     P
      //     |  remove(N)  P
      //     N  ========>  |
      //    /              L
      //   L
      // clang-format on
      node = node->left;
    } else if (node->left == nullptr) {
      // clang-format off
      // Slučaj 3: samo desno dijete
      //   P
      //   |    remove(N)  P
      //   N    ========>  |
      //    \              R
      //     R
      // clang-format on
      node = node->right;
    } else if (node->right->left == nullptr) {
      // clang-format off
      // Slučaj 4: lijevo i desno dijete, desno dijete nema lijevog djeteta
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
      // clang-format off
      // Slučaj 5: lijevo i desno dijete, desno dijete nije list
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

  void inorderTraversal(NodeConsumer action) const {
    if (this->root == nullptr) {
      return;
    }

    std::stack<NodePtr> stack;
    NodePtr node = this->root;

    while (node != nullptr || !stack.empty()) {
      while (node != nullptr) {
        stack.push(node);
        node = node->left;
      }
      if (!stack.empty()) {
        node = stack.top();
        stack.pop();
        action(node);
        node = node->right;
      }
    }
  }
};

#endif  // SIZE_BALANCED_TREE_MAP_HPP
