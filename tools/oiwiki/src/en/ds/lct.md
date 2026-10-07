---
title: Link Cut Tree
---

## Introduction

The Link/Cut Tree is a data structure that we use to solve the **dynamic tree problem**.

The Link/Cut Tree is also called Link-Cut Tree, abbreviated LCT, but it is not called a "dynamic tree"; the dynamic tree is a class of problems.

The Splay Tree is the foundation of the LCT, but the Splay Tree used by the LCT differs in some details from an ordinary Splay (it has a few extensions).

## Motivating problem

Maintain a tree supporting the following operations:

-   modify the weights on the path between two nodes;
-   query the sum of weights on the path between two nodes;
-   modify the weights in the subtree of a node;
-   query the sum of weights in the subtree of a node.

This is a template problem for heavy-light decomposition.

But add one more operation:

-   disconnect and connect some edges, so that the result is still a tree.

The answers above must be computed online.

This becomes the dynamic tree problem, which can be solved with an LCT.

## The dynamic tree problem

Maintain a **forest**, supporting deletion of an edge and insertion of an edge, where it is guaranteed that the result remains a forest after each insertion or deletion. We want to maintain some information about this forest.

Typical operations are connectivity of two nodes, sum of weights on the path between two nodes, connecting two nodes and cutting an edge, modifying information, etc.

### Revisiting heavy-light decomposition from the LCT point of view

-   Decompose the whole tree by subtree size and renumber the nodes.
-   We notice that after renumbering, the tree splits into contiguous intervals by chains, and a segment tree can perform range operations on them.

### Turning to the dynamic tree problem

We notice that the decomposition we just described uses subtree size as the splitting criterion. Can we define a different decomposition that suits the dynamic tree problem better?

Consider what kind of chains the dynamic tree problem needs.

Since we maintain a forest dynamically, we obviously want the chains to be chosen by us, so that we can use them in the solution.

## Preferred-path decomposition

Among the edges from a node to all its children, we choose one edge ourselves for the decomposition; we call the chosen edge a solid edge and the other edges virtual edges. The child connected by a solid edge is called a solid child. A chain consisting of solid edges is likewise called a solid chain. Remember the most important reason for choosing this decomposition: we choose it, so it is flexible and changeable. Precisely because of this flexibility, we use a Splay Tree to maintain these solid chains.

## LCT

We can simply think of the LCT as a set of Splays maintaining a dynamic chain decomposition of a tree, in order to perform range operations on a dynamic tree. For each solid chain we build a Splay that maintains the information of the whole chain as an interval.

## The auxiliary tree

Let us first look at some properties of the auxiliary tree, and then understand its concrete structure through a figure.

In this article you may think of a set of Splays as forming an auxiliary tree, each auxiliary tree maintaining one tree, and a set of auxiliary trees forming the LCT, which maintains the whole forest.

1.  The auxiliary tree consists of several Splays; each Splay maintains one path of the original tree, and the sequence of nodes obtained by an in-order traversal of this Splay corresponds, from front to back, to a "top-down" path in the original tree.
2.  The nodes of the original tree and the Splay nodes of the auxiliary tree are in one-to-one correspondence.
3.  The Splays of the auxiliary tree are not independent of each other. The parent of the root of each Splay should be empty, but in an LCT the parent of the root of each Splay points to the parent of **this chain** in the original tree (i.e. the parent of the topmost node of the chain). This kind of parent link differs from the usual parent link of a Splay in that the child knows its parent but the parent does not know the child; it corresponds to a **virtual edge** of the original tree. Therefore every connected component has exactly one node whose parent is empty.
4.  Because of the above properties of the auxiliary tree, no operation requires us to maintain the original tree: the auxiliary tree can always yield a unique original tree, so we only need to maintain the auxiliary tree.

Now suppose we have an original tree as shown. (Bold edges are solid edges, dashed edges are virtual edges.)

![tree](images/lct-atree-1.svg)

By the definition just given, the structure of the auxiliary tree is as shown.

![auxtree](images/lct-atree-2.svg)

### The structural relationship between the original tree and the auxiliary tree

-   A solid chain in the original tree: in the auxiliary tree, all its nodes are in one Splay.
-   A virtual chain in the original tree: in the auxiliary tree, the Father of the Splay containing the child points to the parent, but neither child of the parent points to the child.
-   Note: the root of the original tree is not the root of the auxiliary tree.
-   The Father in the original tree is not the Father in the auxiliary tree.
-   The auxiliary tree can be re-rooted arbitrarily as long as the properties of the auxiliary tree and of the Splay hold.
-   Switching between virtual and solid chains is easy to do on the auxiliary tree, which is exactly what realizes the dynamic maintenance of the chain decomposition.

### Variable declarations used below

-   `ch[N][2]` left and right children
-   `f[N]` parent pointer
-   `sum[N]` sum of weights on the path
-   `val[N]` node weight
-   `tag[N]` reversal tag
-   `laz[N]` weight tag
-   `siz[N]` subtree size in the auxiliary tree
-   Other\_Vars

### Function declarations

#### Common data structure functions (self-explanatory)

1.  `PushUp(x)`
2.  `PushDown(x)`

#### Splay Tree functions

Below are the functions used in a Splay Tree; for details see [Splay Tree](./splay.md).

1.  `Get(x)` returns which child of its parent $x$ is.
2.  `Splay(x)` rotates $x$ to **the root of the current Splay** in cooperation with Rotate.
3.  `Rotate(x)` rotates $x$ up by one level.

#### New operations

1.  `Access(x)` puts all nodes from the root to $x$ into one solid chain, making the root-to-$x$ path a solid path contained in a single Splay. **Only this operation must be implemented; the others are implemented as the problem requires.**
2.  `IsRoot(x)` checks whether $x$ is the root of the tree it belongs to.
3.  `Update(x)` after an `Access`, recursively `PushDown`s from top to bottom to update the information.
4.  `MakeRoot(x)` makes $x$ the root of the tree it belongs to.
5.  `Link(x, y)` connects the nodes $x, y$ with an edge.
6.  `Cut(x, y)` deletes the edge between the nodes $x, y$.
7.  `Find(x)` finds the index of the root of the tree containing $x$.
8.  `Fix(x, v)` changes the weight of $x$ to $v$.
9.  `Split(x, y)` extracts the path between $x, y$, which makes range operations convenient.

### Macros

-   `#define ls ch[p][0]`
-   `#define rs ch[p][1]`

## Explanation of the functions

### `PushUp()`

```cpp
void PushUp(int p) {
  // maintain other variables
  siz[p] = siz[ls] + siz[rs] + 1;
}
```

### `PushDown()`

```cpp
void PushDown(int p) {
  if (tag[p] != std_tag) {
    // pushdown the tag
    tag[p] = std_tag;
  }
}
```

### `Splay() && Rotate()`

Here `Splay()` and `Rotate()` differ slightly from the Splay Tree implementation.

```cpp
#define Get(x) (ch[f[x]][1] == x)

void Rotate(int x) {
  int y = f[x], z = f[y], k = Get(x);
  if (!isRoot(y)) ch[z][ch[z][1] == y] = x;
  // the line above must come first; an ordinary Splay does not need it, because of isRoot  (explained later)
  ch[y][k] = ch[x][!k], f[ch[x][!k]] = y;
  ch[x][!k] = y, f[y] = x, f[x] = z;
  PushUp(y), PushUp(x);
}

void Splay(int x) {
  Update(
      x);  // we will see it right away; before Splay, PushDown all nodes on the path the rotations will pass through
  for (int fa; fa = f[x], !isRoot(x); Rotate(x)) {
    if (!isRoot(fa)) Rotate(Get(fa) == Get(x) ? fa : x);
  }
}
```

For the functions above, see [Splay Tree](./splay.md).

Below are the functions specific to the LCT.

### `isRoot()`

```cpp
// as said before, the LCT has the property that if a child is not a solid child, its parent cannot find it
// so when a node is neither the left nor the right child of its parent, it is the root of the current Splay
#define isRoot(x) (ch[f[x]][0] != x && ch[f[x]][1] != x)
```

### `Access()`

```cpp
// Access is the core operation of the LCT;
// imagine we want to process a path, and this path happens to be one of our current Splays:
// we can simply use its information. Let us look at the code first, then at the process with the figures
int Access(int x) {
  int p;
  for (p = 0; x; p = x, x = f[x]) {
    Splay(x), ch[x][1] = p, PushUp(x);
  }
  return p;
}
```

-   We have the following tree; solid lines are solid edges, dashed lines are virtual edges.

    ![initial tree](images/lct-access-1.svg)

-   Its auxiliary tree might look like this (with a different construction the structure of the LCT may differ).

    ![initial auxtree](images/lct-access-2.svg)

-   Now we want to `Access(N)`: make all edges on the path from $A$ to $N$ solid and pull them into one Splay.

    ![access tree](images/lct-access-3.svg)

-   The implementation updates the Splays step by step from bottom to top.

-   First we rotate $N$ to the root of the current Splay.

-   To preserve the properties of the AuxTree (auxiliary tree), the former solid edge from $N$ to $O$ must become virtual.

-   Thanks to the "child knows parent, parent does not know child" property, we can unilaterally set the child of $N$ to `NULL`.

-   So the former AuxTree changes from the figure below to the one after it.

    ![step 1 auxtree](images/lct-access-4.svg)

-   In the next step we also rotate $I$, the Father that $N$ points to, to the root of $I$'s Splay.

-   The former solid edge $I$—$K$ must be removed; now we point the right child of $I$ to $N$ and obtain the Splay $I$—$L$.

    ![step 2 auxtree](images/lct-access-5.svg)

-   Next, following the same steps, since the Father of $I$ points to $H$, we rotate $H$ to the root of its Splay Tree and then set the rs of $H$ to $I$.

-   The tree then looks like this.

    ![step 3 auxtree](images/lct-access-6.svg)

-   Similarly we `Splay(A)` and point the right child of $A$ to $H$.

-   So we obtain the following AuxTree, and we see that the whole path $A$—$N$ is now in a single Splay.

    ![step final auxtree](images/lct-access-7.svg)

```cpp
// let us review the code
int Access(int x) {
  int p;
  for (p = 0; x; p = x, x = f[x]) {
    Splay(x), ch[x][1] = p, PushUp(x);
  }
  return p;
}
```

We see that `Access()` is actually very easy and consists of just the following four steps:

1.  Rotate the current node to the root.
2.  Replace its child with the previous node.
3.  Update the information of the current node.
4.  Replace the current node with its parent and continue.

The Access given here also has a return value. This return value is the index of the parent node of the virtual edge at the last virtual/solid chain switch. The value has two meanings:

-   For two consecutive Access operations, the return value of the second Access equals the LCA of the two nodes.
-   It denotes the root of the Splay Tree containing the chain from $x$ to the root. This node has certainly already been rotated to the root, and its parent is certainly empty.

### `Update()`

```cpp
// just pushDown level by level from top to bottom
void Update(int p) {
  if (!isRoot(p)) Update(f[p]);
  pushDown(p);
}
```

### `makeRoot()`

-   `Make_Root()` is no less important than `Access()`. When we need to maintain path information, paths whose depth does not strictly increase inevitably occur, and by the properties of the AuxTree such a path cannot be in one Splay.
-   This is where we need `Make_Root()`.
-   `Make_Root()` makes the given node the root of the original tree; consider how to implement this operation.
-   Let the return value of `Access(x)` be $y$; then the path from $x$ to the current root forms exactly one Splay, and the root of this Splay is $y$.
-   Consider representing the tree as a directed graph, giving every edge a direction from child to parent. It is easy to see that re-rooting is equivalent to reversing all edges on the path from $x$ to the root (think about it carefully).
-   Therefore it suffices to reverse the path from $x$ to the current root.
-   Since $y$ is the root of the Splay representing the path from $x$ to the current root, it suffices to reverse the interval of the Splay Tree rooted at $y$.

```cpp
void makeRoot(int p) {
  p = Access(p);
  swap(ch[p][0], ch[p][1]);
  tag[p] ^= 1;
}
```

### `Link()`

-   Linking two nodes is actually simple: first `Make_Root(x)`, then point the parent of $x$ to $y$. Obviously this operation must not happen inside the same tree, so remember to check that first.

```cpp
void Link(int x, int p) {
  makeRoot(x);
  splay(x);
  f[x] = p;
}
```

### `Split()`

-   The meaning of `Split` is simple: take out a Splay that maintains the path from $x$ to $y$.
-   First `MakeRoot(x)`, then `Access(y)`. If $y$ should be the root, also `Splay(y)`.
-   These three steps of Split directly extract the needed path into the subtree of $y$, on which other operations can be performed.

### `Cut()`

-   `Cut` has two cases: validity guaranteed, and validity not necessarily guaranteed.
-   If validity is guaranteed, simply `Split(x, y)`; then $y$ is the root and $x$ is certainly its child, so just disconnect them in both directions. Like this:

```cpp
void Cut(int x, int p) { makeRoot(x), Access(p), Splay(p), ls = f[x] = 0; }
```

If validity is not guaranteed, we need to check whether the edge exists; one could store the edges in a `map`, but there is also a method that exploits the structure:

To delete an edge, the following three conditions must hold:

1.  $x,y$ are connected.
2.  There are no other chains on the path between $x,y$.
3.  $x$ has no right child.

In short, the three statements above mean one thing: there is an edge between $x,y$.

The concrete implementation is left as an exercise. Checking connectivity requires the `Find` described below; for the other two conditions, a little thought about the structure shows how to check them.

### `Find()`

-   `Find()` finds the root of the **original tree** containing $x$; do not confuse the root of the original tree with the root of the auxiliary tree. After `Access(p)`, do `Splay(p)`. Then the root is the node with the smallest depth in the tree: keep going to the left child, doing `PushDown` along the way.
-   Keep going until there is no ls; very simple.
-   Note: after each query, the node holding the answer must be `Splay`ed up to guarantee the complexity.

```cpp
int Find(int p) {
  Access(p);
  Splay(p);
  pushDown(p);
  while (ls) p = ls, pushDown(p);
  Splay(p);
  return p;
}
```

### Caveats

-   Before every operation, think about whether a `PushUp` or `PushDown` is needed; since the LCT is extremely flexible, one missing `Pushdown` or `Pushup` can apply a modification to the wrong node!
-   The `Rotate` of the LCT differs from that of the Splay: the `if (z)` must come first.
-   The `Splay` operation of the LCT rotates to the root; there is no "rotate to become the child of some node", because it is not needed.

## Time complexity

Most operations of the LCT are based on `Access`, and the time complexity of the other operations is constant, so we only need to analyze the time complexity of `Access`.

The time complexity of `Access` comes mainly from multiple splay operations and from visiting the virtual edges on the path; we analyze these two parts separately.

1.  splay

    -   Define $w(x) = \log size(x)$, where $size(x)$ denotes the total number of virtual and solid edges in the subtree rooted at $x$.

    -   Define the potential function $\Phi = \sum_{x \in T} w(x)$, where $T$ denotes the set of all nodes.

    From the analysis of the [time complexity of Splay](./splay.md#time-complexity) it easily follows that the amortized time complexity of a splay operation is $O(\log n)$.

2.  visiting virtual edges

    Following [heavy-light decomposition](../graph/hld.md#heavy-light-decomposition), define two kinds of virtual edges:

    -   **heavy virtual edge**: a virtual edge from node $v$ to its parent with $size(v) > \frac{1}{2} size(parent(v))$;

    -   **light virtual edge**: a virtual edge from node $v$ to its parent with $size(v) \leq \frac{1}{2} size(parent(v))$.

    For virtual edges we can use a potential analysis: define the potential function $\Phi$ as the number of heavy virtual edges, and the amortized cost $c_i = t_i + \Delta \Phi_i$, where $t_i$ is the actual cost of the operation and $\Delta \Phi_i$ the change in potential.

    -   After traversing a heavy virtual edge, it is converted into a solid edge, which decreases the potential by $1$, since it optimizes the tree structure by strengthening important connections. Since its actual cost is $O(1)$, this is offset by the decrease in potential, so it does not increase the amortized cost; all the amortized cost is concentrated on handling light virtual edges.

    -   Each `Access` traverses at most $O(\log n)$ light virtual edges, hence spends at most $O(\log n)$ actual cost and produces $O(\log n)$ heavy virtual edges, i.e. the potential increases at a cost of $O(\log n)$.

    Hence the final amortized complexity of visiting virtual edges is the sum of the actual cost and the change in potential, i.e. $O(\log n)$.

In summary, the time complexity of `Access` in an LCT is the sum of the complexities of splay and of visiting virtual edges, so the final amortized complexity is $O(\log n)$; that is, an LCT with n nodes performs m `Access` operations in $O(n \log n + m \log n)$, and consequently the amortized complexity of `Cut`, `Link`, `Findroot` and other operations based on `Access` is also $O(\log n)$.

## Exercises

-   [BZOJ 3282 Tree](https://hydro.ac/p/bzoj-P3282)
-   [HNOI2010 弹飞绵羊](https://www.luogu.com.cn/problem/P3203)

## Maintaining path information

Through the operation `Split(x,y)`, the LCT extracts the path from node $x$ to node $y$ into the Splay rooted at $y$, turning updates and queries of path information into operations on a balanced tree; this gives the LCT an advantage in maintaining path information. Furthermore, binary search along a path implemented with an LCT has one factor of $O(\log n)$ less than with heavy-light decomposition.

???+ note "Example problem [国家集训队 Tree II](https://www.luogu.com.cn/problem/P1501)"
    Given a tree with $n$ nodes, each with initial weight $1$. There are $q$ operations, each one of the following four:
    
    1.  `- u1 v1 u2 v2`: delete the edge between $u_1,v_1$ and connect $u_2,v_2$; it is guaranteed that the operation is valid and the result is still a tree.
    2.  `+ u v c`: add $c$ to the weight of every node on the path between $u,v$.
    3.  `* u v c`: multiply the weight of every node on the path between $u,v$ by $c$.
    4.  `/ u v`: output the sum of the weights of the nodes on the path between $u,v$ modulo $51061$.
    
        $1\le n,q\le 10^5,0\le c\le 10^4$
    
        The `-` operation is simply `Cut(u1,v1),Link(u2,v2)`.

To modify the path between $u,v$, first `Split(u,v)`.

This problem requires subtree addition, subtree multiplication and subtree sum on the auxiliary tree, so besides the subtree reversal tag that an ordinary LCT maintains, we also maintain a subtree addition tag and a subtree multiplication tag. The tags are handled the same way as in a Splay.

When applying and pushing down the addition tag, the change of the subtree sum depends on the number of nodes in the subtree, so we also maintain the subtree size `siz`.

When pushing down the tags, mind the order: push down the multiplication tag first, then the addition tag. The subtree reversal tag and the addition/multiplication tags do not conflict.

??? note "Sample code"
    ```cpp
    #include <algorithm>
    #include <cstdio>
    #include <cstring>
    using namespace std;
    constexpr long long MAXN = 100010;
    constexpr long long mod = 51061;
    long long n, q, u, v, c;
    char op;
    
    struct Splay {
      long long ch[MAXN][2], fa[MAXN], siz[MAXN], val[MAXN], sum[MAXN], rev[MAXN],
          add[MAXN], mul[MAXN];
    
      void clear(long long x) {
        ch[x][0] = ch[x][1] = fa[x] = siz[x] = val[x] = sum[x] = rev[x] = add[x] =
            0;
        mul[x] = 1;
      }
    
      long long getch(long long x) { return (ch[fa[x]][1] == x); }
    
      long long isroot(long long x) {
        clear(0);
        return ch[fa[x]][0] != x && ch[fa[x]][1] != x;
      }
    
      void maintain(long long x) {
        clear(0);
        siz[x] = (siz[ch[x][0]] + 1 + siz[ch[x][1]]) % mod;
        sum[x] = (sum[ch[x][0]] + val[x] + sum[ch[x][1]]) % mod;
      }
    
      void pushdown(long long x) {
        clear(0);
        if (mul[x] != 1) {
          if (ch[x][0])
            mul[ch[x][0]] = (mul[x] * mul[ch[x][0]]) % mod,
            val[ch[x][0]] = (val[ch[x][0]] * mul[x]) % mod,
            sum[ch[x][0]] = (sum[ch[x][0]] * mul[x]) % mod,
            add[ch[x][0]] = (add[ch[x][0]] * mul[x]) % mod;
          if (ch[x][1])
            mul[ch[x][1]] = (mul[x] * mul[ch[x][1]]) % mod,
            val[ch[x][1]] = (val[ch[x][1]] * mul[x]) % mod,
            sum[ch[x][1]] = (sum[ch[x][1]] * mul[x]) % mod,
            add[ch[x][1]] = (add[ch[x][1]] * mul[x]) % mod;
          mul[x] = 1;
        }
        if (add[x]) {
          if (ch[x][0])
            add[ch[x][0]] = (add[ch[x][0]] + add[x]) % mod,
            val[ch[x][0]] = (val[ch[x][0]] + add[x]) % mod,
            sum[ch[x][0]] = (sum[ch[x][0]] + add[x] * siz[ch[x][0]] % mod) % mod;
          if (ch[x][1])
            add[ch[x][1]] = (add[ch[x][1]] + add[x]) % mod,
            val[ch[x][1]] = (val[ch[x][1]] + add[x]) % mod,
            sum[ch[x][1]] = (sum[ch[x][1]] + add[x] * siz[ch[x][1]] % mod) % mod;
          add[x] = 0;
        }
        if (rev[x]) {
          if (ch[x][0]) rev[ch[x][0]] ^= 1, swap(ch[ch[x][0]][0], ch[ch[x][0]][1]);
          if (ch[x][1]) rev[ch[x][1]] ^= 1, swap(ch[ch[x][1]][0], ch[ch[x][1]][1]);
          rev[x] = 0;
        }
      }
    
      void update(long long x) {
        if (!isroot(x)) update(fa[x]);
        pushdown(x);
      }
    
      void print(long long x) {
        if (!x) return;
        pushdown(x);
        print(ch[x][0]);
        printf("%lld ", x);
        print(ch[x][1]);
      }
    
      void rotate(long long x) {
        long long y = fa[x], z = fa[y], chx = getch(x), chy = getch(y);
        fa[x] = z;
        if (!isroot(y)) ch[z][chy] = x;
        ch[y][chx] = ch[x][chx ^ 1];
        fa[ch[x][chx ^ 1]] = y;
        ch[x][chx ^ 1] = y;
        fa[y] = x;
        maintain(y);
        maintain(x);
        maintain(z);
      }
    
      void splay(long long x) {
        update(x);
        for (long long f = fa[x]; f = fa[x], !isroot(x); rotate(x))
          if (!isroot(f)) rotate(getch(x) == getch(f) ? f : x);
      }
    
      void access(long long x) {
        for (long long f = 0; x; f = x, x = fa[x])
          splay(x), ch[x][1] = f, maintain(x);
      }
    
      void makeroot(long long x) {
        access(x);
        splay(x);
        swap(ch[x][0], ch[x][1]);
        rev[x] ^= 1;
      }
    
      long long find(long long x) {
        access(x);
        splay(x);
        while (ch[x][0]) x = ch[x][0];
        splay(x);
        return x;
      }
    } st;
    
    main() {
      scanf("%lld%lld", &n, &q);
      for (long long i = 1; i <= n; i++) st.val[i] = 1, st.maintain(i);
      for (long long i = 1; i < n; i++) {
        scanf("%lld%lld", &u, &v);
        if (st.find(u) != st.find(v)) st.makeroot(u), st.fa[u] = v;
      }
      while (q--) {
        scanf(" %c%lld%lld", &op, &u, &v);
        if (op == '+') {
          scanf("%lld", &c);
          st.makeroot(u), st.access(v), st.splay(v);
          st.val[v] = (st.val[v] + c) % mod;
          st.sum[v] = (st.sum[v] + st.siz[v] * c % mod) % mod;
          st.add[v] = (st.add[v] + c) % mod;
        }
        if (op == '-') {
          st.makeroot(u);
          st.access(v);
          st.splay(v);
          if (st.ch[v][0] == u && !st.ch[u][1]) st.ch[v][0] = st.fa[u] = 0;
          scanf("%lld%lld", &u, &v);
          if (st.find(u) != st.find(v)) st.makeroot(u), st.fa[u] = v;
        }
        if (op == '*') {
          scanf("%lld", &c);
          st.makeroot(u), st.access(v), st.splay(v);
          st.val[v] = st.val[v] * c % mod;
          st.sum[v] = st.sum[v] * c % mod;
          st.mul[v] = st.mul[v] * c % mod;
        }
        if (op == '/')
          st.makeroot(u), st.access(v), st.splay(v), printf("%lld\n", st.sum[v]);
      }
      return 0;
    }
    ```

### Exercises

-   [Luogu P3690【模板】Link Cut Tree（动态树）](https://www.luogu.com.cn/problem/P3690)
-   [SDOI2011 染色](https://www.luogu.com.cn/problem/P2486)
-   [SHOI2014 三叉神经树](https://loj.ac/problem/2187)

## Maintaining connectivity

### Checking connectivity

With the `Find()` function of the LCT we can check whether two nodes of a dynamic forest are connected. If `Find(x)==Find(y)`, the nodes $x,y$ are in the same tree, i.e. connected.

???+ note "Example problem [SDOI2008 洞穴勘测](https://www.luogu.com.cn/problem/P2147)"
    Initially there are $n$ isolated nodes and $m$ operations. Each operation is one of the following:
    
    1.  `Connect u v`: connect the nodes $u,v$ with an edge.
    2.  `Destroy u v`: delete the edge between $u,v$; it is guaranteed that such an edge exists.
    3.  `Query u v`: ask whether $u,v$ are connected.
    
    It is guaranteed that the graph is a forest at all times.
    
    $n\le 10^4, m\le 2\times 10^5$

??? note "Sample code"
    ```cpp
    #include <algorithm>
    #include <cstdio>
    #include <cstring>
    using namespace std;
    constexpr int MAXN = 10010;
    
    struct Splay {
      int ch[MAXN][2], fa[MAXN], tag[MAXN];
    
      void clear(int x) { ch[x][0] = ch[x][1] = fa[x] = tag[x] = 0; }
    
      int getch(int x) { return ch[fa[x]][1] == x; }
    
      int isroot(int x) { return ch[fa[x]][0] != x && ch[fa[x]][1] != x; }
    
      void pushdown(int x) {
        if (tag[x]) {
          if (ch[x][0]) swap(ch[ch[x][0]][0], ch[ch[x][0]][1]), tag[ch[x][0]] ^= 1;
          if (ch[x][1]) swap(ch[ch[x][1]][0], ch[ch[x][1]][1]), tag[ch[x][1]] ^= 1;
          tag[x] = 0;
        }
      }
    
      void update(int x) {
        if (!isroot(x)) update(fa[x]);
        pushdown(x);
      }
    
      void rotate(int x) {
        int y = fa[x], z = fa[y], chx = getch(x), chy = getch(y);
        fa[x] = z;
        if (!isroot(y)) ch[z][chy] = x;
        ch[y][chx] = ch[x][chx ^ 1];
        fa[ch[x][chx ^ 1]] = y;
        ch[x][chx ^ 1] = y;
        fa[y] = x;
      }
    
      void splay(int x) {
        update(x);
        for (int f = fa[x]; f = fa[x], !isroot(x); rotate(x))
          if (!isroot(f)) rotate(getch(x) == getch(f) ? f : x);
      }
    
      void access(int x) {
        for (int f = 0; x; f = x, x = fa[x]) splay(x), ch[x][1] = f;
      }
    
      void makeroot(int x) {
        access(x);
        splay(x);
        swap(ch[x][0], ch[x][1]);
        tag[x] ^= 1;
      }
    
      int find(int x) {
        access(x);
        splay(x);
        while (ch[x][0]) x = ch[x][0];
        splay(x);
        return x;
      }
    } st;
    
    int n, q, x, y;
    char op[MAXN];
    
    int main() {
      scanf("%d%d", &n, &q);
      while (q--) {
        scanf("%s%d%d", op, &x, &y);
        if (op[0] == 'Q') {
          if (st.find(x) == st.find(y))
            printf("Yes\n");
          else
            printf("No\n");
        }
        if (op[0] == 'C')
          if (st.find(x) != st.find(y)) st.makeroot(x), st.fa[x] = y;
        if (op[0] == 'D') {
          st.makeroot(x);
          st.access(y);
          st.splay(y);
          if (st.ch[y][0] == x && !st.ch[x][1]) st.ch[y][0] = st.fa[x] = 0;
        }
      }
      return 0;
    }
    ```

### Maintaining 2-edge-connected components

If 2-edge-connected components must be contracted into single nodes: each time an edge is added, if the two tree nodes it connects are already connected, all nodes on that path are contracted into one node.

???+ note "Example problem [AHOI2005 航线规划](https://www.luogu.com.cn/problem/P2542)"
    Given $n$ nodes, initially $m$ undirected edges, and $q$ operations. Each operation is one of the following:
    
    1.  `0 u v`: delete the edge between $u,v$; it is guaranteed that such an edge exists at that moment.
    2.  `1 u v`: ask how many edges must be used by every possible path between $u,v$ at that moment.
    
    It is guaranteed that the graph is connected at all times.
    
    $1<n<3\times 10^4,1<m<10^5,0\le q\le 4\times 10^4$

One can see that the number of edges that every possible path between $u,v$ must use equals the number of nodes on the path between the node containing $u$ and the node containing $v$, after contracting all 2-edge-connected components, minus $1$.

Since the deletions in the problem are hard to perform, we process the operations offline in reverse order, turning deletions into insertions.

When adding an edge, if the two nodes were not connected before, connect them in the LCT; otherwise extract the path between the two nodes in the LCT before adding the edge, traverse this subtree of the auxiliary tree, which amounts to traversing this path, and merge these nodes, maintaining the merge information with a union-find.

The representative of the union-find after merging replaces the former path in the tree. Note that every subsequent operation must first find the representative of the node in the union-find and operate on it.

??? note "Sample code"
    ```cpp
    #include <algorithm>
    #include <cstdio>
    #include <cstring>
    #include <map>
    using namespace std;
    constexpr int MAXN = 200010;
    int f[MAXN];
    
    int findp(int x) { return f[x] ? f[x] = findp(f[x]) : x; }
    
    void merge(int x, int y) {
      x = findp(x);
      y = findp(y);
      if (x != y) f[x] = y;
    }
    
    struct Splay {
      int ch[MAXN][2], fa[MAXN], tag[MAXN], siz[MAXN];
    
      void clear(int x) { ch[x][0] = ch[x][1] = fa[x] = tag[x] = siz[x] = 0; }
    
      int getch(int x) { return ch[findp(fa[x])][1] == x; }
    
      int isroot(int x) {
        return ch[findp(fa[x])][0] != x && ch[findp(fa[x])][1] != x;
      }
    
      void maintain(int x) {
        clear(0);
        if (x) siz[x] = siz[ch[x][0]] + 1 + siz[ch[x][1]];
      }
    
      void pushdown(int x) {
        if (tag[x]) {
          if (ch[x][0]) tag[ch[x][0]] ^= 1, swap(ch[ch[x][0]][0], ch[ch[x][0]][1]);
          if (ch[x][1]) tag[ch[x][1]] ^= 1, swap(ch[ch[x][1]][0], ch[ch[x][1]][1]);
          tag[x] = 0;
        }
      }
    
      void print(int x) {
        if (!x) return;
        pushdown(x);
        print(ch[x][0]);
        printf("%d ", x);
        print(ch[x][1]);
      }
    
      void update(int x) {
        if (!isroot(x)) update(findp(fa[x]));
        pushdown(x);
      }
    
      void rotate(int x) {
        x = findp(x);
        int y = findp(fa[x]), z = findp(fa[y]), chx = getch(x), chy = getch(y);
        fa[x] = z;
        if (!isroot(y)) ch[z][chy] = x;
        ch[y][chx] = ch[x][chx ^ 1];
        fa[ch[x][chx ^ 1]] = y;
        ch[x][chx ^ 1] = y;
        fa[y] = x;
        maintain(y);
        maintain(x);
        if (z) maintain(z);
      }
    
      void splay(int x) {
        x = findp(x);
        update(x);
        for (int f = findp(fa[x]); f = findp(fa[x]), !isroot(x); rotate(x))
          if (!isroot(f)) rotate(getch(x) == getch(f) ? f : x);
      }
    
      void access(int x) {
        for (int f = 0; x; f = x, x = findp(fa[x]))
          splay(x), ch[x][1] = f, maintain(x);
      }
    
      void makeroot(int x) {
        x = findp(x);
        access(x);
        splay(x);
        tag[x] ^= 1;
        swap(ch[x][0], ch[x][1]);
      }
    
      int find(int x) {
        x = findp(x);
        access(x);
        splay(x);
        while (ch[x][0]) x = ch[x][0];
        splay(x);
        return x;
      }
    
      void dfs(int x) {
        pushdown(x);
        if (ch[x][0]) dfs(ch[x][0]), merge(ch[x][0], x);
        if (ch[x][1]) dfs(ch[x][1]), merge(ch[x][1], x);
      }
    } st;
    
    int n, m, q, x, y, cur, ans[MAXN];
    
    struct oper {
      int op, a, b;
    } s[MAXN];
    
    map<pair<int, int>, int> mp;
    
    int main() {
      scanf("%d%d", &n, &m);
      for (int i = 1; i <= n; i++) st.maintain(i);
      for (int i = 1; i <= m; i++)
        scanf("%d%d", &x, &y), mp[{x, y}] = mp[{y, x}] = 1;
      while (scanf("%d", &s[++q].op)) {
        if (s[q].op == -1) {
          q--;
          break;
        }
        scanf("%d%d", &s[q].a, &s[q].b);
        if (!s[q].op) mp[{s[q].a, s[q].b}] = mp[{s[q].b, s[q].a}] = 0;
      }
      reverse(s + 1, s + q + 1);
      for (map<pair<int, int>, int>::iterator it = mp.begin(); it != mp.end(); it++)
        if (it->second) {
          mp[{it->first.second, it->first.first}] = 0;
          x = findp(it->first.first);
          y = findp(it->first.second);
          if (st.find(x) != st.find(y))
            st.makeroot(x), st.fa[x] = y;
          else {
            if (x == y) continue;
            st.makeroot(x);
            st.access(y);
            st.splay(y);
            st.dfs(y);
            int t = findp(y);
            st.fa[t] = findp(st.fa[y]);
            st.ch[t][0] = st.ch[t][1] = 0;
            st.maintain(t);
          }
        }
      for (int i = 1; i <= q; i++) {
        if (s[i].op == 0) {
          x = findp(s[i].a);
          y = findp(s[i].b);
          st.makeroot(x);
          st.access(y);
          st.splay(y);
          st.dfs(y);
          int t = findp(y);
          st.fa[t] = st.fa[y];
          st.ch[t][0] = st.ch[t][1] = 0;
          st.maintain(t);
        }
        if (s[i].op == 1) {
          x = findp(s[i].a);
          y = findp(s[i].b);
          st.makeroot(x);
          st.access(y);
          st.splay(y);
          ans[++cur] = st.siz[y] - 1;
        }
      }
      for (int i = cur; i >= 1; i--) printf("%d\n", ans[i]);
      return 0;
    }
    ```

### Exercises

-   [Luogu P3950 部落冲突](https://www.luogu.com.cn/problem/P3950)
-   [BZOJ 4998 星球联盟](https://hydro.ac/p/bzoj-P4998)
-   [BZOJ 2959 长跑](https://hydro.ac/p/bzoj-P2959)

## Maintaining edge weights

The LCT cannot handle edge weights directly; in that case we create a corresponding node for every edge, which makes querying edge information on a chain convenient. With this trick one can maintain a spanning tree dynamically.

???+ note "Example problem [Luogu P4234 最小差值生成树](https://www.luogu.com.cn/problem/P4234)"
    Given a weighted undirected graph with $n$ nodes and $m$ edges, find the spanning tree with the smallest difference between its maximum and minimum edge weight, and output this difference.
    
    It is guaranteed that at least one spanning tree exists.
    
    $1\le n\le 5\times 10^4,1\le m\le 2\times 10^5,1\le w_i\le 10^4$

Sort the edges by weight in increasing order and enumerate the rightmost chosen edge; for the optimal solution, the weight of the lightest edge should be as large as possible.

Add the edges in order; if the two nodes to be connected are already connected, delete the edge with the smallest weight on the path between them. If the whole graph is already connected into a tree, update the answer with the current weight minus the minimum weight. The minimum weight can be updated with two pointers.

There is no fixed parent-child relationship in an LCT, so edge weights cannot be stored in node weights.

To record information about the edges on a chain, we can use **edge splitting**: create a corresponding node for each edge and connect it to both endpoints; the former link and cut operations each become two operations.

??? note "Sample code"
    ```cpp
    #include <algorithm>
    #include <cstdio>
    #include <cstring>
    #include <set>
    using namespace std;
    constexpr int MAXN = 5000010;
    
    struct Splay {
      int ch[MAXN][2], fa[MAXN], tag[MAXN], val[MAXN], minn[MAXN];
    
      void clear(int x) {
        ch[x][0] = ch[x][1] = fa[x] = tag[x] = val[x] = minn[x] = 0;
      }
    
      int getch(int x) { return ch[fa[x]][1] == x; }
    
      int isroot(int x) { return ch[fa[x]][0] != x && ch[fa[x]][1] != x; }
    
      void maintain(int x) {
        if (!x) return;
        minn[x] = x;
        if (ch[x][0]) {
          if (val[minn[ch[x][0]]] < val[minn[x]]) minn[x] = minn[ch[x][0]];
        }
        if (ch[x][1]) {
          if (val[minn[ch[x][1]]] < val[minn[x]]) minn[x] = minn[ch[x][1]];
        }
      }
    
      void pushdown(int x) {
        if (tag[x]) {
          if (ch[x][0]) tag[ch[x][0]] ^= 1, swap(ch[ch[x][0]][0], ch[ch[x][0]][1]);
          if (ch[x][1]) tag[ch[x][1]] ^= 1, swap(ch[ch[x][1]][0], ch[ch[x][1]][1]);
          tag[x] = 0;
        }
      }
    
      void update(int x) {
        if (!isroot(x)) update(fa[x]);
        pushdown(x);
      }
    
      void print(int x) {
        if (!x) return;
        pushdown(x);
        print(ch[x][0]);
        printf("%d ", x);
        print(ch[x][1]);
      }
    
      void rotate(int x) {
        int y = fa[x], z = fa[y], chx = getch(x), chy = getch(y);
        fa[x] = z;
        if (!isroot(y)) ch[z][chy] = x;
        ch[y][chx] = ch[x][chx ^ 1];
        fa[ch[x][chx ^ 1]] = y;
        ch[x][chx ^ 1] = y;
        fa[y] = x;
        maintain(y);
        maintain(x);
        if (z) maintain(z);
      }
    
      void splay(int x) {
        update(x);
        for (int f = fa[x]; f = fa[x], !isroot(x); rotate(x))
          if (!isroot(f)) rotate(getch(x) == getch(f) ? f : x);
      }
    
      void access(int x) {
        for (int f = 0; x; f = x, x = fa[x]) splay(x), ch[x][1] = f, maintain(x);
      }
    
      void makeroot(int x) {
        access(x);
        splay(x);
        tag[x] ^= 1;
        swap(ch[x][0], ch[x][1]);
      }
    
      int find(int x) {
        access(x);
        splay(x);
        while (ch[x][0]) x = ch[x][0];
        splay(x);
        return x;
      }
    
      void link(int x, int y) {
        makeroot(x);
        fa[x] = y;
      }
    
      void cut(int x, int y) {
        makeroot(x);
        access(y);
        splay(y);
        ch[y][0] = fa[x] = 0;
        maintain(y);
      }
    } st;
    
    constexpr int inf = 2e9 + 1;
    int n, m, ans, nww, x, y;
    
    struct Edge {
      int u, v, w;
    
      bool operator<(Edge x) const { return w < x.w; };
    } s[MAXN];
    
    multiset<int> mp;
    
    int main() {
      scanf("%d%d", &n, &m);
      for (int i = 1; i <= n; i++) st.val[i] = inf, st.maintain(i);
      for (int i = 1; i <= m; i++) scanf("%d%d%d", &s[i].u, &s[i].v, &s[i].w);
      sort(s + 1, s + m + 1);
      for (int i = 1; i <= m; i++) st.val[n + i] = s[i].w, st.maintain(n + i);
      for (int i = 1; i <= m; i++) {
        x = s[i].u;
        y = s[i].v;
        if (x == y) continue;
        if (st.find(x) != st.find(y)) {
          nww++;
          st.link(x, n + i);
          st.link(n + i, y);
          mp.insert(s[i].w);
          if (nww == n - 1) ans = s[i].w - (*(mp.begin()++));
        } else {
          st.makeroot(x);
          st.access(y);
          st.splay(y);
          int t = st.minn[y] - n;
          st.cut(s[t].u, t + n);
          st.cut(t + n, s[t].v);
          mp.erase(mp.find(s[t].w));
          st.link(x, n + i);
          st.link(n + i, y);
          mp.insert(s[i].w);
          if (nww == n - 1) ans = min(ans, s[i].w - (*(mp.begin()++)));
        }
      }
      printf("%d\n", ans);
      return 0;
    }
    ```

### Exercises

-   [WC2006 水管局长](https://www.luogu.com.cn/problem/P4172)
-   [BJWC2010 严格次小生成树](https://www.luogu.com.cn/problem/P4180)
-   [NOI2014 魔法森林](https://uoj.ac/problem/3)

## Maintaining subtree information

The LCT is not good at maintaining subtree information. By aggregating the information of all virtual subtrees of a node, one can obtain the information of the whole tree.

???+ note "Example problem [BJOI2014 大融合](https://loj.ac/problem/2230)"
    Given $n$ nodes and $q$ operations, each of the following form:
    
    1.  `A x y` connect the nodes $x$ and $y$ with an edge.
    2.  `Q x y` given an existing edge $(x,y)$, find how many simple paths contain the edge $(x,y)$.
    
    It is guaranteed that the graph is a forest at all times.
    
    $1\le n,q,x,y\le 10^5$

Consider another formulation of query `Q`: the answer equals the product of the number of nodes on the $x$ side of the edge $(x,y)$ and the number of nodes on the $y$ side, i.e. the sizes of the trees containing $x$ and $y$ respectively after cutting the edge $(x,y)$. To undo the effect of cutting, we reconnect the edge $(x,y)$ after the query.

The problem has both linking and cutting of edges, and guarantees a forest at all times, which naturally suggests an LCT. But here the LCT maintains subtree sizes rather than the chain information we are used to, and the LCT is built so that **the child knows the parent but the parent does not know the child**, which makes direct subtree aggregation inconvenient. What to do?

The method is to aggregate the contributions of the subtrees represented by all virtual children of a node $x$ (i.e. nodes whose parent is $x$ but which are not among the left and right children of $x$ in the Splay).

Define $siz2[x]$ as the number of nodes in the subtrees represented by all virtual children of node $x$, and $siz[x]$ as the number of nodes in the subtree of node $x$.

Unlike the usual way of maintaining the number of subtree nodes in a Splay, when computing the number of nodes in the subtree of $x$ we also add $siz2[x]$, i.e.

```cpp
void maintain(int x) {
  clear(0);
  if (x) siz[x] = siz[ch[x][0]] + 1 + siz[ch[x][1]] + siz2[x];
}
```

Moreover, when we **change the shape of the Splay** (i.e. change the left or right child pointer of a node in the Splay), we must update the value of $siz2[x]$ promptly.

In the `Rotate(),Splay()` operations we only change the relative positions of nodes within the Splay and do not change whether any edge is virtual or solid, so we do not modify $siz2[x]$ at all.

In the `access` operation, after every splay, the right child of the node just splayed changes, i.e. the virtual/solid status of the edge to its former right child and of the edge to its new right child changes; we need to add the contribution of the subtree whose edge just became virtual and subtract the contribution of the subtree whose edge just became solid. The code is as follows:

```cpp
void access(int x) {
  for (int f = 0; x; f = x, x = fa[x])
    splay(x), siz2[x] += siz[ch[x][1]] - siz[f], ch[x][1] = f, maintain(x);
}
```

In the `MakeRoot(),Find()` operations we only call the previous functions or walk along the Splay, so no modification is needed.

When linking two nodes, we change the parent of one node. We need to add the subtree size contribution of the new child to the $siz2$ value of the parent node.

```cpp
st.makeroot(x);
st.makeroot(y);
st.fa[x] = y;
st.siz2[y] += st.siz[x];
```

When cutting an edge, we only delete a solid edge in the Splay; the `Maintain` operation maintains this information, so no modification is needed.

Those are the details of the code changes; finally, let us summarize the requirements and the method for maintaining subtree information with an LCT:

1.  The maintained information must be **subtractable**, such as the number of subtree nodes or the subtree weight sum; subtree maximum/minimum cannot be maintained directly, because when a virtual edge becomes solid, the contribution of the former virtual edge must be excluded.
2.  Create an additional value storing the contribution of the virtual subtrees, add it to the node's answer when aggregating, and maintain it promptly when the virtual/solid status of an edge changes.
3.  The rest is the same as an ordinary LCT; when aggregating subtree information, always make the node the root.
4.  If the maintained information is not subtractable, e.g. a range maximum, one can keep a balanced tree for each node to maintain the extreme values in its virtual subtrees.

??? note "Sample code"
    ```cpp
    #include <algorithm>
    #include <cstdio>
    #include <cstring>
    using namespace std;
    constexpr int MAXN = 100010;
    using ll = long long;
    
    struct Splay {
      int ch[MAXN][2], fa[MAXN], siz[MAXN], siz2[MAXN], tag[MAXN];
    
      void clear(int x) {
        ch[x][0] = ch[x][1] = fa[x] = siz[x] = siz2[x] = tag[x] = 0;
      }
    
      int getch(int x) { return ch[fa[x]][1] == x; }
    
      int isroot(int x) { return ch[fa[x]][0] != x && ch[fa[x]][1] != x; }
    
      void maintain(int x) {
        clear(0);
        if (x) siz[x] = siz[ch[x][0]] + 1 + siz[ch[x][1]] + siz2[x];
      }
    
      void pushdown(int x) {
        if (tag[x]) {
          if (ch[x][0]) swap(ch[ch[x][0]][0], ch[ch[x][0]][1]), tag[ch[x][0]] ^= 1;
          if (ch[x][1]) swap(ch[ch[x][1]][0], ch[ch[x][1]][1]), tag[ch[x][1]] ^= 1;
          tag[x] = 0;
        }
      }
    
      void update(int x) {
        if (!isroot(x)) update(fa[x]);
        pushdown(x);
      }
    
      void rotate(int x) {
        int y = fa[x], z = fa[y], chx = getch(x), chy = getch(y);
        fa[x] = z;
        if (!isroot(y)) ch[z][chy] = x;
        ch[y][chx] = ch[x][chx ^ 1];
        fa[ch[x][chx ^ 1]] = y;
        ch[x][chx ^ 1] = y;
        fa[y] = x;
        maintain(y);
        maintain(x);
        maintain(z);
      }
    
      void splay(int x) {
        update(x);
        for (int f = fa[x]; f = fa[x], !isroot(x); rotate(x))
          if (!isroot(f)) rotate(getch(x) == getch(f) ? f : x);
      }
    
      void access(int x) {
        for (int f = 0; x; f = x, x = fa[x])
          splay(x), siz2[x] += siz[ch[x][1]] - siz[f], ch[x][1] = f, maintain(x);
      }
    
      void makeroot(int x) {
        access(x);
        splay(x);
        swap(ch[x][0], ch[x][1]);
        tag[x] ^= 1;
      }
    
      int find(int x) {
        access(x);
        splay(x);
        while (ch[x][0]) x = ch[x][0];
        splay(x);
        return x;
      }
    } st;
    
    int n, q, x, y;
    char op;
    
    int main() {
      scanf("%d%d", &n, &q);
      while (q--) {
        scanf(" %c%d%d", &op, &x, &y);
        if (op == 'A') {
          st.makeroot(x);
          st.makeroot(y);
          st.fa[x] = y;
          st.siz2[y] += st.siz[x];
        }
        if (op == 'Q') {
          st.makeroot(x);
          st.access(y);
          st.splay(y);
          st.ch[y][0] = st.fa[x] = 0;
          st.maintain(x);
          st.makeroot(x);
          st.makeroot(y);
          printf("%lld\n", (ll)(st.siz[x] * st.siz[y]));
          st.makeroot(x);
          st.makeroot(y);
          st.fa[x] = y;
          st.siz2[y] += st.siz[x];
        }
      }
      return 0;
    }
    ```

### Exercises

-   [Luogu P4299 首都](https://www.luogu.com.cn/problem/P4299)
-   [SPOJ QTREE5 - Query on a tree V](https://www.spoj.com/problems/QTREE5)
