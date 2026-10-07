// --8<-- [start:full]
/**
 * @file rbtree.hpp
 * @brief Implementacija skupa pomoću crveno-crnog stabla
 * @details Skup je uređen prema zadanoj funkciji {@code compare_t}
 * usporedbe; ova implementacija omogućuje find, insert, remove, određivanje ranga i
 * pronalaženje ključa po rangu u vremenu O(log(n)).
 * @author [Tiphereth-A](https://github.com/Tiphereth-A)
 */

#ifndef RBTREE_HPP
#define RBTREE_HPP

// --8<-- [start:class]
#include <cassert>
#include <cstdint>
#include <functional>

using std::size_t;

// --8<-- [start:class-node1]
/**
 * Implementacija skupa pomoću crveno-crnog stabla
 *
 * @tparam key_t tip ključa
 * @tparam compare_t funkcija usporedbe
 */
template <typename key_t, typename compare_t = std::less<key_t>>
struct rb_tree {
  /**
   * Čvor stabla
   */
  struct node_t {
    node_t *fa;     // == nullptr ako je korijen stabla, inače roditelj
    node_t *ch[2];  // == nullptr ako je dijete prazno
                    // ch[0]: lijevo dijete, ch[1]: desno dijete
    key_t data;
    size_t sz;  // Veličina podstabla
    bool red;   // == true ako je čvor crven, inače crn

    /**
     * Dohvaća smjer trenutačnog nepraznog čvora u odnosu na roditelja
     *
     * @return true ako je ovaj čvor desno dijete svojeg roditelja, inače false
     */
    auto child_dir() const -> bool { return this == fa->ch[1]; }
  };

  using pointer = node_t *;
  using const_pointer = const node_t *;
  using pointer_const = node_t *const;

  const compare_t compare;
  pointer root;

  rb_tree() : compare{}, root{nullptr} {}

  // --8<-- [end:class-node1]

  ~rb_tree() {
    post_order([](auto it) { delete it; });
  }

  auto size() const -> size_t { return size(root); }

  template <typename F>
  void pre_order(F callback) {
    auto f = [&](auto &&f, pointer p) {
      if (!p) return;
      callback(p), f(f, p->ch[0]), f(f, p->ch[1]);
    };
    f(f, root);
  }

  template <typename F>
  void in_order(F callback) {
    auto f = [&](auto &&f, pointer p) {
      if (!p) return;
      f(f, p->ch[0]), callback(p), f(f, p->ch[1]);
    };
    f(f, root);
  }

  template <typename F>
  void post_order(F callback) {
    auto f = [&](auto &&f, pointer p) {
      if (!p) return;
      f(f, p->ch[0]), f(f, p->ch[1]), callback(p);
    };
    f(f, root);
  }

  auto leftmost(const_pointer p) const { return most(p, 0); }

  auto rightmost(const_pointer p) const { return most(p, 1); }

  auto prev(const_pointer p) const { return neighbour(p, 0); }

  auto next(const_pointer p) const { return neighbour(p, 1); }

  auto lower_bound(const key_t &key) const -> pointer {
    const_pointer now = root, ans = nullptr;
    while (now) {
      if (!compare(now->data, key))
        ans = now, now = now->ch[0];
      else
        now = now->ch[1];
    }
    return (pointer)ans;
  }

  auto upper_bound(const key_t &key) const -> pointer {
    const_pointer now = root, ans = nullptr;
    while (now) {
      if (compare(key, now->data))
        ans = now, now = now->ch[0];
      else
        now = now->ch[1];
    }
    return (pointer)ans;
  }

  // Rang počinje od 0
  auto order_of_key(const key_t &key) const -> size_t {
    size_t ans = 0;
    auto now = root;
    while (now) {
      if (!compare(now->data, key))
        now = now->ch[0];
      else
        ans += size(now->ch[0]) + 1, now = now->ch[1];
    }
    return ans;
  }

  // Rang počinje od 0
  auto find_by_order(size_t order) const -> const_pointer {
    const_pointer now = root, ans = nullptr;
    while (now && now->sz >= order) {
      auto lsize = size(now->ch[0]);
      if (order < lsize)
        now = now->ch[0];
      else {
        ans = now;
        if (order == lsize) break;
        now = now->ch[1], order -= lsize + 1;
      }
    }
    return ans;
  }

  // --8<-- [start:insert]
  /**
   * @return nullptr ako umetanje nije uspjelo, inače pokazivač na umetnuti čvor
   */
  auto insert(const key_t &data) -> const_pointer {
    pointer n = new node_t;
    n->fa = n->ch[0] = n->ch[1] = nullptr;
    n->data = data, n->sz = 1;
    pointer now = root, p = nullptr;
    bool dir = 0;
    while (now) {
      p = now;
      dir = compare(now->data, data);
      now = now->ch[dir];
    }
    insert_fixup_leaf(p, n, dir);
    return n;
  }

  // --8<-- [end:insert]
  // --8<-- [start:delete]
  /**
   * @return je li operacija uspjela
   */
  auto erase(const key_t &key) -> bool {
    auto p = lower_bound(key);
    if (!p || p->data != key) return false;
    erase(p);
    return true;
  }

  /**
   * @return {@code next(p)}
   */
  auto erase(pointer p) -> const_pointer {
    if (!p) return nullptr;
    pointer result;
    if (p->ch[0] && p->ch[1]) {
      auto s = leftmost(p->ch[1]);
      std::swap(s->data, p->data);
      result = p, p = s;
    } else
      result = next(p);
    erase_fixup_branch_or_leaf(p);
    delete p;
    return result;
  }

  // --8<-- [end:delete]
 private:
  static auto size(const_pointer p) -> size_t { return p ? p->sz : 0; }

  static auto is_red(const_pointer p) -> bool { return p ? p->red : false; }

  /**
   * @param dir 0: krajnje lijevo, 1: krajnje desno
   */
  auto most(const_pointer p, bool dir) const -> pointer {
    if (!p) return nullptr;
    while (p->ch[dir]) p = p->ch[dir];
    return (pointer)p;
  }

  /**
   * @param dir 0: prethodni, 1: sljedeći
   */
  auto neighbour(const_pointer p, bool dir) const -> pointer {
    if (!p) return nullptr;
    if (p->ch[dir]) return most(p->ch[dir], !dir);
    if (p == root) return nullptr;
    while (p && p->fa && p->child_dir() == dir) p = p->fa;
    return p ? p->fa : nullptr;
  }

  // --8<-- [start:insert-leaf]
  /**
   * Umeće list {@code n} u {@code p}
   *
   * @param p roditelj čvora koji će biti umetnut
   * @param n list koji će biti umetnut
   * @param dir smjer čvora n, 0: lijevo; 1: desno
   */
  void insert_leaf(pointer_const p, pointer_const n, bool dir) {
    if (!p) {
      root = n;
      return;
    }
    p->ch[dir] = n, n->fa = p;
    auto now = p;
    while (now) now->sz++, now = now->fa;
  }

  // --8<-- [end:insert-leaf]
  // --8<-- [start:delete-leaf]
  /**
   * Briše čvor {@code n}
   *
   * @param n čvor koji će biti izbrisan, smije imati najviše 2 djeteta
   */
  void erase_branch_or_leaf(pointer_const n) {
    auto p = n->fa, s = n->ch[0] ? n->ch[0] : n->ch[1];
    if (s) s->fa = p;
    if (!p) {
      root = s;
      return;
    }
    p->ch[n->child_dir()] = s;
    auto now = p;
    while (now) now->sz--, now = now->fa;
  }

  // --8<-- [end:delete-leaf]
  // --8<-- [start:rotate]
  /**
   * @param p korijen podstabla (može biti jednak {@code root})
   * @param dir smjer. 0: lijeva rotacija; 1: desna rotacija
   * @return novi korijen podstabla
   */
  auto rotate(pointer p, bool dir) -> pointer {
    auto g = p->fa;
    auto s = p->ch[!dir];  // novi korijen podstabla
    assert(s);             // potreban je pokazivač na stvarni čvor
    s->sz = p->sz, p->sz = size(p->ch[dir]) + size(s->ch[dir]) + 1;
    auto c = s->ch[dir];
    if (c) c->fa = p;
    p->ch[!dir] = c, s->ch[dir] = p;
    p->fa = s, s->fa = g;
    if (g)
      g->ch[p == g->ch[1]] = s;
    else
      root = s;
    return s;
  }

  // --8<-- [end:rotate]
#pragma GCC diagnostic ignored "-Wcomment"

  // --8<-- [start:insert-fixup1]
  /**
   * Umeće list {@code n} u {@code p}, zatim popravlja ravnotežu
   *
   * @param p roditelj čvora koji će biti umetnut
   * @param n čvor koji će biti umetnut
   * @param dir smjer čvora n, 0: lijevo; 1: desno
   */
  void insert_fixup_leaf(pointer p, pointer n, bool dir) {
    n->red = p;
    insert_leaf(p, n, dir);
    // Ispravi dva uzastopna crvena čvora
    // --8<-- [end:insert-fixup1]
    // --8<-- [start:insert-aux1]
    while (is_red(p = n->fa)) {
      bool p_dir = p->child_dir();
      auto g = p->fa, u = g->ch[!p_dir];
      // --8<-- [end:insert-aux1]
      // --8<-- [start:insert-case1]
      // Slučaj 1: i p i u crveni su
      //      g              [g]
      //     / \             / \
      //   [p] [u]   ==>    p   u
      //   /               /
      // [n]             [n]
      if (is_red(u)) {
        p->red = u->red = false;
        g->red = true;
        n = g;
        continue;
      }
      // --8<-- [end:insert-case1]
      // --8<-- [start:insert-case2]
      // p je crven, a u je crn
      // Slučaj 2: smjer čvora n razlikuje se od smjera čvora p
      //    g              g
      //   / \            / \
      // [p]  u   ==>   [n]  u
      //   \            /
      //   [n]        [p]
      if (n->child_dir() != p_dir) rotate(p, p_dir), std::swap(n, p);
      // --8<-- [end:insert-case2]
      // --8<-- [start:insert-case3]
      // Slučaj 3: p je crven, u je crn, a n i p imaju isti smjer
      //      g             p
      //     / \           / \
      //   [p]  u   ==>  [n] [g]
      //   /                   \
      // [n]                    u
      p->red = false, g->red = true;
      rotate(g, !p_dir);
      // --8<-- [end:insert-case3]
      // --8<-- [start:insert-aux2]
    }
    // --8<-- [end:insert-aux2]
    // --8<-- [start:insert-fixup2]
    // Završna obrada: oboji korijen u crno
    root->red = false;
  }

  // --8<-- [end:insert-fixup2]
  // --8<-- [start:delete-fixup1]
  /**
   * Briše čvor {@code n}, zatim popravlja ravnotežu
   *
   * @param n čvor koji će biti izbrisan, smije imati najviše 2 djeteta
   */
  void erase_fixup_branch_or_leaf(pointer n) {
    bool n_dir = n == root ? false : n->child_dir();
    erase_branch_or_leaf(n);
    auto p = n->fa;
    if (!p) {  // n je korijen
      if (root) root->red = false;
      return;
    } else {
      auto s = p->ch[n_dir];
      if (s) {  // n ima 1 dijete
        // n mora biti crn, a s crven, pa trebamo obojiti s u crno
        s->red = false;
        return;
      }
    }
    // n nije korijen, nego crni list; treba popraviti ravnotežu
    // --8<-- [end:delete-fixup1]
    // --8<-- [start:delete-aux1]
    while (p && !n->red) {
      auto s = p->ch[!n_dir];
      // --8<-- [end:delete-aux1]
      // --8<-- [start:delete-case1]
      // Slučaj 1: s je crven
      //    p               s
      //   / \             / \
      // |n| [s]   ==>   [p]  d
      //     / \         / \
      //    c   d      |n|  c
      if (is_red(s)) {
        s->red = false, p->red = true;
        rotate(p, n_dir);
        s = p->ch[!n_dir];
      }
      // --8<-- [end:delete-case1]
      // --8<-- [start:delete-aux2]
      // s mora biti crn
      auto c = s->ch[n_dir], d = s->ch[!n_dir];
      // --8<-- [end:delete-aux2]
      // --8<-- [start:delete-case2]
      // Slučaj 2: i c i d crni su
      //   {p}          {p}
      //   / \          / \
      // |n|  s   ==> |n| [s]
      //     / \          / \
      //    c   d        c   d
      // p će na kraju biti obojen u crno
      if (!is_red(c) && !is_red(d)) {
        s->red = true;
        n = p;
        goto end_erase_fixup;
      }
      // --8<-- [end:delete-case2]
      // --8<-- [start:delete-case3]
      // Slučaj 3: c je crven, a d je crn
      //   {p}          {p}
      //   / \          / \
      // |n|  s   ==> |n|  c
      //     / \            \
      //   [c]  d           [s]
      //                      \
      //                       d
      if (!is_red(d)) {
        c->red = false, s->red = true;
        rotate(s, !n_dir);
        s = p->ch[!n_dir], c = s->ch[n_dir], d = s->ch[!n_dir];
      }
      // --8<-- [end:delete-case3]
      // --8<-- [start:delete-case4]
      // Slučaj 4: d je crven
      //   {p}            {s}
      //   / \            / \
      // |n|  s   ==>    p   d
      //     / \        / \
      //   {c} [d]    |n| {c}
      s->red = p->red, p->red = d->red = false;
      rotate(p, n_dir), n = root;
      // --8<-- [end:delete-case4]
      // --8<-- [start:delete-aux3]
    end_erase_fixup:
      p = n->fa;
      if (!p) break;
      n_dir = n->child_dir();
    }
    // --8<-- [end:delete-aux3]
    // --8<-- [start:delete-fixup2]
    // Završna obrada: vidi slučajeve 2 i 4
    n->red = false;
  }

  // --8<-- [end:delete-fixup2]
  // --8<-- [start:class-node2]
};

// --8<-- [end:class-node2]
#pragma GCC diagnostic warning "-Wcomment"

// --8<-- [end:class]
#endif  // RBTREE_HPP
        // --8<-- [end:full]