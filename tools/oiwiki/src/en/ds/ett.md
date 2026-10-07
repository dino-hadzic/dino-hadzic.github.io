---
title: Euler Tour Tree
---

author: Backl1ght

The Euler Tour Tree (hereafter ETT) is a data structure that can solve **dynamic tree** problems. ETT turns operations on a dynamic tree into interval operations on its DFS sequence, and then maintains those interval operations with some other data structure, thereby maintaining the dynamic tree operations. For example, ETT turns adding an edge to a dynamic tree into several sequence split and sequence merge operations; if we can maintain sequence splits and merges, we can maintain edge insertion in a dynamic tree.

LCT is also a data structure for dynamic tree problems and is much more common than ETT. LCT is actually better suited to maintaining information about tree paths, whereas ETT is better suited to maintaining information about **subtrees**. For example, ETT can maintain the minimum of a subtree while LCT cannot.

ETT can be maintained with any data structure, as long as that structure supports the corresponding interval operations on sequences and meets the complexity requirements. Usually the sequence is maintained with a balanced binary search tree such as a Splay tree or a Treap; the complexity of interval operations in these structures is $O(\log n)$, so the dynamic tree operations can also be maintained in $O(\log n)$ time. If the interval operations are maintained with a multiway balanced search tree such as a B-tree, even better complexity can be achieved.

In fact, ETT can be understood as an idea: by maintaining some sequence in one-to-one correspondence with the original tree, we achieve the goal of maintaining the original tree; this article only describes some feasible implementations and applications of that idea.

## Euler tour representation of a tree

If every tree edge is viewed as two directed edges, a tree can be represented as an Euler tour of a directed graph; this is called the Euler tour representation (ETR) of the tree.

The sequence we will maintain later is actually a variant of the ETR in which the vertices of the tree are also added as self-loops, but since the authors of the original paper did not give it a new name, we will keep calling it ETR.

The Euler tour representation of a tree $T$ can be obtained with the following algorithm:

$$
\begin{array}{ll}
1 & \textbf{Input. } \text{A rooted tree }T\\
2 & \textbf{Output. } \text{The dfs sequence of rooted tree }T\\
3 & \operatorname{ET}(u)\\
4 & \qquad \text{visit vertex }u\\
5 & \qquad \text{for all child } v \text{ of } u\\
6 & \qquad \qquad \text{visit directed edge } u \to v\\
7 & \qquad \qquad \operatorname{ET}(v)\\
8 & \qquad \qquad \text{visit directed edge } v \to u\\
\end{array}
$$

The Euler tour representation $\operatorname{ETR}(T)$ of a tree $T$ is initially empty; during the DFS, every time a vertex or a directed edge is visited it is appended to the end of $\operatorname{ETR}(T)$, which yields $\operatorname{ETR}(T)$.

If $T$ contains $n$ vertices, it contains $2n - 2$ directed edges, and during the DFS every vertex and every directed edge is visited exactly once, so the length of $\operatorname{ETR}(T)$ is $3n - 2$.

If a vertex $u$ is viewed as a self-loop, $\operatorname{ETR}(T)$ can be seen as an Euler tour in a directed graph. The Euler tour can be cut at some point and viewed as a chain of edges joined end to end; such a chain can be glued back together at the cut to become an Euler tour again; and by adding a few edges, two such chains can be joined into a new Euler tour.

In what follows, unless stated otherwise, the maintained sequence is the Euler tour representation of the tree.

## Basic operations of ETT

The following three operations are considered the basic operations of ETT; each can be turned into a constant number of sequence operations, so their complexity is of the same order as that of the sequence operations.

What is given here is only one feasible implementation; any approach works as long as the sequence corresponding to the modified tree can be assembled with a constant number of sequence operations.

### MakeRoot(u)

That is, rerooting. In ETT, rerooting is turned into one sequence split and one sequence merge, which can also be understood as one cyclic shift of an interval.

Let $T$ be the tree containing vertex $u$, let its current root be $r$, and suppose we want to make $u$ the root. Let $L$ be the sequence corresponding to $T$. Split $L$ at $(u, u)$ into sequences $L^1$ and $L^2$, where the former contains the elements of $L$ before $(u, u)$ together with $(u, u)$, and the latter contains the remaining elements. Then the sequence obtained by merging $L^2$ and $L^1$ in that order is the sequence corresponding to the tree after rerooting.

This can be understood as rotating the Euler tour: an Euler tour is a cycle, and a rotation does not change the structure of the Euler tour, hence does not change the structure of the tree; it merely rotates vertex $u$ into the root position.

### Insert(u, v)

That is, edge insertion. In ETT, edge insertion is turned into two sequence splits and five sequence merges.

Let $T_1$ be the tree containing vertex $u$ and $T_2$ the tree containing vertex $v$; after inserting the edge, the two trees merge into one tree $T$. Let $L_1$ be the sequence corresponding to $T_1$ and $L_2$ the sequence corresponding to $T_2$.

Split $L_1$ at $(u, u)$ into sequences $L_1^1$ and $L_1^2$, where the former contains the elements of $L_1$ before $(u, u)$ together with $(u, u)$, and the latter contains the remaining elements. Similarly split $L_2$ at $(v, v)$ into sequences $L_2^1$ and $L_2^2$. Merging $L_1^2, L_1^1, [(u, v)], L_2^2, L_2^1,  [(v, u)]$ in that order gives the sequence $L$ corresponding to tree $T$.

This can be understood as two rerooting operations, after which the two Euler tours are cut at the position of their current roots and joined into a new Euler tour with the two newly added directed edges.

### Delete(u, v)

That is, edge deletion. In ETT, edge deletion is turned into four sequence splits and one sequence merge.

Let $T$ be the tree containing edges $(u, v)$ and $(v, u)$, with corresponding sequence $L$. After deleting the edge, $T$ splits into two trees.

Split $L$ into $L_1, [(u, v)], L_2, [(v, u)], L_3$; the sequences corresponding to the two trees formed by the deletion are $L_2$ and $L_1, L_3$ respectively. Note that in sequence $L$, $[(u, v)]$ may appear after $[(v, u)]$; in that case, first swap the values of $u$ and $v$ and then perform the operation.

This can be understood as cutting the Euler tour at two directed edges into two chains, after which each chain joins its own ends to form a new Euler tour.

## Implementation

Below we describe an implementation of ETT using a rotation-free Treap as an example; the reader should already be familiar with maintaining interval operations with a rotation-free Treap.

`Split` and `Merge` are basic operations of the rotation-free Treap and are not repeated here.

### SplitUp2(u)

Suppose $L$ is the sequence containing $u$; split $L$ at $u$ into sequences $L^1$ and $L^2$, where the former contains the elements of $L$ before $u$ together with $u$, and the latter contains the remaining elements.

If every Treap node additionally maintains its parent, the position in the sequence of the element corresponding to a Treap node can be computed in $O(\log n)$ time, and then a `Split` by position achieves the desired functionality.

The same can also be achieved by splitting bottom-up, which is more efficient than the method above. Concretely, while climbing from the node corresponding to $u$ towards the root, by the binary search tree property we can determine for each node whether it lies before or after $u$ in $L$; from this we can compute the position of $u$ in the sequence and also determine which of the two trees after the split each node belongs to.

```cpp
/*
 * Bottom up split treap p into 2 treaps a and b.
 *   - a: a treap containing nodes with position less than or equal to p.
 *   - b: a treap containing nodes with postion greater than p.
 *
 * In the other word, split sequence containning p into two sequences, the first
 * one contains elements before p and element p, the second one contains
 * elements after p.
 */
static std::pair<Node*, Node*> SplitUp2(Node* p) {
  Node *a = nullptr, *b = nullptr;
  b = p->right_;
  if (b) b->parent_ = nullptr;
  p->right_ = nullptr;

  bool is_p_left_child_of_parent = false;
  bool is_from_left_child = false;
  while (p) {
    Node* parent = p->parent_;

    if (parent) {
      is_p_left_child_of_parent = (parent->left_ == p);
      if (is_p_left_child_of_parent) {
        parent->left_ = nullptr;
      } else {
        parent->right_ = nullptr;
      }
      p->parent_ = nullptr;
    }

    if (!is_from_left_child) {
      a = Merge(p, a);
    } else {
      b = Merge(b, p);
    }

    is_from_left_child = is_p_left_child_of_parent;
    p->Maintain();
    p = parent;
  }

  return {a, b};
}
```

### SplitUp3(u)

Suppose $L$ is the sequence containing $u$; split $L$ at $u$ into sequences $L^1$, $u$ and $L^2$, where the former contains the elements of $L$ before $u$ and the latter contains the remaining elements.

A slight modification of `SplitUp2` suffices.

### MakeRoot(u)

Easily obtained from `SplitUp2` and `Merge`.

```cpp
void MakeRoot(int u) {
  Node* vertex_u = vertices_[u];
  auto [L1, L2] = Treap::SplitUp2(vertex_u);
  Treap::Merge(L2, L1);
}
```

### Insert(u, v)

Easily obtained from `SplitUp2` and `Merge`.

```cpp
void Insert(int u, int v) {
  Node* vertex_u = vertices_[u];
  Node* vertex_v = vertices_[v];

  Node* edge_uv = AllocateNode(u, v);
  Node* edge_vu = AllocateNode(v, u);
  tree_edges_[u][v] = edge_uv;
  tree_edges_[v][u] = edge_vu;

  auto [L11, L12] = Treap::SplitUp2(vertex_u);
  auto [L21, L22] = Treap::SplitUp2(vertex_v);

  Node* L = L12;
  L = Treap::Merge(L, L11);
  L = Treap::Merge(L, edge_uv);
  L = Treap::Merge(L, L22);
  L = Treap::Merge(L, L21);
  L = Treap::Merge(L, edge_vu);
}
```

### Delete(u, v)

Easily obtained from `SplitUp3` and `Merge`.

```cpp
void Delete(int u, int v) {
  Node* edge_uv = tree_edges_[u][v];
  Node* edge_vu = tree_edges_[v][u];
  tree_edges_[u].erase(v);
  tree_edges_[v].erase(u);

  int position_uv = Treap::GetPosition(edge_uv);
  int position_vu = Treap::GetPosition(edge_vu);
  if (position_uv > position_vu) {
    std::swap(edge_uv, edge_vu);
    std::swap(position_uv, position_vu);
  }

  auto [L1, uv, _] = Treap::SplitUp3(edge_uv);
  auto [L2, vu, L3] = Treap::SplitUp3(edge_vu);
  Treap::Merge(L1, L3);

  FreeNode(edge_uv);
  FreeNode(edge_vu);
}
```

## Maintaining connectivity

Vertices $u$ and $v$ are connected if and only if they belong to the same tree $T$, i.e. $(u, u)$ and $(v, v)$ belong to $\operatorname{ETR}(T)$; this can be checked by comparing whether the roots of the Treaps containing the Treap nodes corresponding to $u$ and $v$ are the same.

### Example [P2147 \[SDOI2008\] 洞穴勘测](https://www.luogu.com.cn/problem/P2147)

A template problem for maintaining connectivity.

??? note "Sample code"
    ```cpp
    --8<-- "docs/ds/code/ett/ett_connectivity.cpp"
    ```

## Maintaining subtree information

Below we use the number of vertices in a subtree as an example.

For every element of $\operatorname{ETR}(T)$, if the element corresponds to a vertex of the tree, give it weight $1$; if it corresponds to an edge of the tree, give it weight $0$. Now the number of vertices of tree $T$ can be viewed as the sum of the weights of the elements in $\operatorname{ETR}(T)$, so to maintain the subtree vertex count it suffices to additionally maintain the weight sum of the sequence. Maintaining the weight sum of a sequence is a classic operation of the rotation-free Treap.

Similarly, operations such as the subtree minimum can be turned into classic balanced-tree operations such as the sequence minimum and maintained that way.

### Example [LOJ #2230. "BJOI2014" 大融合](https://loj.ac/p/2230)

??? note "Sample code"
    ```cpp
    --8<-- "docs/ds/code/ett/ett_subtree_size.cpp"
    ```

## Maintaining path information

A fairly common trick can be used: with the properties of the bracket sequence, turn path information into interval information, and then maintain the path information by maintaining the sequence with a data structure. However, this trick requires the maintained information to be **subtractable** (invertible).

The sequence operations corresponding to the dynamic tree operations described earlier may move a right bracket of the bracket sequence in front of its left bracket, so when maintaining information such as the sum of vertex weights on a path, extra care is needed: the operations must not change the relative order of matching left and right brackets, which may require rethinking which sequence operations correspond to the dynamic tree operations, or even rethinking which DFS sequence to maintain.

Moreover, ETT has great difficulty maintaining path modifications.

### Example ["星际探索"](https://hydro.ac/p/bzoj-P3786)

The only dynamic tree operation in this problem is changing the parent, which can be viewed as deleting an edge and then adding an edge, but doing so may change the relative order of matching brackets.

We can turn vertex weights into edge weights, maintain the bracket sequence of the tree, and turn the parent change into moving the bracket sequence of the whole subtree to just after the left bracket of the parent.

??? note "Sample code"
    ```cpp
    --8<-- "docs/ds/code/ett/ett_1.cpp"
    ```

## References

-   Dynamic trees as search trees via euler tours, applied to the network simplex algorithm - Robert E. Tarjan
-   Randomized fully dynamic graph algorithms with polylogarithmic time per operation - Henzinger et al.
