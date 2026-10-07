---
title: PQ tree
---

author: isdanni,xyf007

A PQ tree is a tree-based data structure representing a family of permutations of a set of elements; it was discovered and named by Kellogg S. Booth and George S. Lueker in 1976 and is used to solve the following problem:

> Given $m$ sets $S_i$, find a permutation of $1\sim n$ such that the elements of each set are adjacent.

A PQ tree can be built in $O(n+\sum|S_i|)$ time. The construction method described in this article has time complexity $O(nm)$.

## Definition

A PQ tree has three kinds of nodes: **leaf nodes**, **P nodes** and **Q nodes**. A leaf node represents an element of the permutation, a P node means its children can be permuted arbitrarily, and a Q node means the order of its children can be reversed. All non-leaf nodes are either P nodes or Q nodes. A P node has at least 2 children and a Q node has at least 3 children.  
Because of the node definitions, the PQ tree itself represents **all** valid solutions, and its preorder traversal is one of them.  
The figure below shows a PQ tree.  
![](https://gregable.com/2008/11/i/pq-tree.webp)  
Its preorder traversal 1,2,3,4,5 represents a valid solution. If the children of the P node are rearranged to 4,2,3, we get another valid solution 1,4,2,3,5. Keeping the order of the P node's children and reversing the order of the Q node's children gives another valid solution 5,3,2,4,1.

## Construction

**The PQ tree uses the child-sibling representation.**

We build a PQ tree incrementally.

First build a tree whose root is a P node with $n$ children $1,2,\ldots,n$, representing the PQ tree without any constraints. As constraints are added, we keep modifying this tree.

When a new constraint set $S$ is added, we mark all leaf nodes belonging to this set **black** and the leaf nodes not in the set **white**. For every non-leaf node, if all its children are black, mark it black too; if all its children are white, mark it white too; otherwise mark it **grey**. In the figures below, black, white and grey nodes are drawn in black, grey, and half black half grey respectively.

We require the nodes of the PQ tree to be sorted by color.

### Bottom-up method

The smallest subtree containing all black nodes is called the **pertinent subtree**, and the root of the pertinent subtree (not necessarily the root of the whole tree) is called the **pertinent root**.

The process of adding one constraint is called a reduction. A reduction has two phases: the bubbling phase and the reduction phase.

#### Bubbling phase

The bubbling phase only processes the pertinent subtree. We mark all nodes of the pertinent subtree black or grey and compute for every node the number of pertinent children it has. To do this efficiently, we process the pertinent subtree from the leaves towards the root. This requires recording each node's parent, but in the reduction phase a node's parent is often changed. To achieve linear-time construction, only the children of P nodes and **the last child of a Q node** always record the correct parent. For the other children of a Q node, their parent is updated in the bubbling phase with the parent of the last child.

When we meet a node in the middle, we check whether its siblings already have a valid parent. If not, mark it **blocked**. If later its sibling gets a valid parent, update this node's parent and remove the mark. If at the end of the bubbling phase there is still a run of consecutive blocked nodes (as in case Q3 below), a parentless "pseudo-node" becomes the parent of that block and is removed in the reduction phase.

#### Reduction phase

The reduction phase processes nodes with a queue. First push all leaf nodes in the constraint into the queue. Each time take the node $u$ at the front of the queue and process it. If the parent of $u$ is also a node of the pertinent subtree, push $\mathit{fa}_u$ into the queue.  
For every node $u$ we distinguish cases. If it fits none of them, there is no solution.

##### Leaf node

Mark $u$ black.

##### P node

If all children are black, mark $u$ black.  
![](https://gregable.com/2008/11/i/p1-template.png)  
![](https://gregable.com/2008/11/i/p1-replacement.png)

If $u$ has black children and white children, and $u$ is the pertinent root, create a new P node $v$ to become the root of all its black children.  
![](https://gregable.com/2008/11/i/p2-template.png)  
![](https://gregable.com/2008/11/i/p2-replacement.png)

If $u$ has black children and white children, and $u$ is not the pertinent root, do the following:

-   Create a new P node $f$ to become the root of all black children.
-   Create a new P node $e$ to become the root of all white children.
-   If $e$ (and/or $f$) has only one child, do not create a new node; instead set $e$ (and/or $f$) directly to that child.
-   Turn $u$ into a Q node with children $e$ and $f$, and mark it grey.

Note that by the earlier definition a Q node has at least 3 children, so this $u$ is treated as a "pseudo-node" and will be processed further later.  
![](https://gregable.com/2008/11/i/p3-template.png)  
![](https://gregable.com/2008/11/i/p3-replacement.png)

If $u$ has one grey child $p$ and $u$ is the pertinent root, create a new P node $v$ as the root of all its black children, set the sibling of $v$ to the last black child of $p$, and then make $v$ the last child of $p$.  
![](https://gregable.com/2008/11/i/p4-template.png)  
![](https://gregable.com/2008/11/i/p4-replacement.png)

If $u$ has one grey child $p$ and $u$ is not the pertinent root, do the following:

-   Create a new P node $f$ to become the root of all black children.
-   Create a new P node $e$ to become the root of all white children.
-   If $e$ (and/or $f$) has only one child, do not create a new node; instead set $e$ (and/or $f$) directly to that child.
-   Set the sibling of $e$ to the last white child of $p$, then make $e$ the last child of $p$.
-   Set the sibling of $f$ to the last black child of $p$, then make $f$ the last child of $p$.

![](https://gregable.com/2008/11/i/p5-template.png)  
![](https://gregable.com/2008/11/i/p5-replacement.png)

If $u$ has exactly two grey children $p_1,p_2$, do the following:

-   Create a new P node $f$ to become the root of all black children.
-   If $f$ has only one child, do not create a new node; instead set $f$ directly to that child.
-   Set the sibling of the last black child of $p_1$ to $f$.
-   Set the sibling of $f$ to the last black child of $p_2$.
-   Set the last child of $p_2$ to the last white child of $p_2$.

One can see that in this way $p_2$ is merged into $p_1$.  
![](https://gregable.com/2008/11/i/p6-template.png)  
![](https://gregable.com/2008/11/i/p6-replacement.png)

##### Q node

If $u$ only has black children, mark $u$ black. (The shape in the figure below is wrong.)  
![](https://gregable.com/2008/11/i/q1-template.png)  
![](https://gregable.com/2008/11/i/q1-replacement.png)

If $u$ has one grey child $p$ and all children with the same mark appear consecutively, do the following:

-   Let $p_f$ be the last black child of $p$, $p_e$ the last white child of $p$, $f$ the black sibling of $p$ and $e$ the white sibling of $p$.
-   Set the sibling of $f$ to $p_f$ and the sibling of $e$ to $p_e$.
-   If $p$ has no white sibling or no black sibling, set the last child of $u$ to the last child of $p$.
-   Delete $p$.

![](https://gregable.com/2008/11/i/q2-template.png)  
![](https://gregable.com/2008/11/i/q2-replacement.png)

If $u$ has exactly two grey children $p_1,p_2$ and all children with the same mark appear consecutively, just apply the previous operation to both $p_1$ and $p_2$.  
![](https://gregable.com/2008/11/i/q3-template.png)  
![](https://gregable.com/2008/11/i/q3-replacement.png)

This construction method is the one from the original paper, but it is inconvenient to implement.

### Top-down method

Most implementations in competitive programming currently use this method. The method is actually similar; the cases appearing below can basically all be found above.

Note that according to the coloring process above, all black and white nodes already satisfy the condition, so we **only need to process grey nodes**.

#### P node

-   If $u$ has more than two grey children, there is no solution.
-   If $u$ has only one grey child and no black children, recursively process the grey child.
-   Otherwise first clear the children of $u$, then add all white children. Create a new Q node $q_1$ as a child of $u$. Add all grey children to $q_1$. Create a new P node $p$ as the root of all black children, and insert $p$ in the middle of $q_1$. (This corresponds to all P node cases of the bottom-up method.)

Note that we will require, for the two grey nodes, that all white nodes are on the left and all black nodes on the right (or vice versa), so we need to implement a split function `split` that splits the nodes of this subtree into a black part and a white part while preserving **all possibilities** of the nodes of the resulting subtrees.

#### Q node

-   Find the positions $l,r$ of the leftmost and rightmost non-white nodes. If there is a non-black node inside $[l+1,r-1]$, there is no solution.
-   If there are no black nodes and only one grey node, recursively process that grey node; otherwise it suffices to split the nodes at positions $l$ and $r$.

#### Split function

Let the node to split be $u$; we want to split $u$ into a forest with all white on the left and all black on the right. If $u$ is not grey, return the subtree directly. We only consider grey nodes.
If $u$ is a P node:

-   If $u$ has at least two grey children, there is no solution.
-   Otherwise the left part is all white children, the middle is the recursively processed grey child, and the right part is all black children. Note that to preserve all possibilities, two new P nodes are created as the roots of the white children and the black children respectively. (This corresponds to case P4 of the bottom-up method.)
-   Delete $u$.

If $u$ is a Q node:

-   If neither the forward nor the reversed order satisfies white-grey-black, there is no solution.
-   If there are at least two grey children, there is also no solution.
-   Otherwise recursively split the grey child.
-   Delete $u$.

Finally delete all redundant nodes (nodes with only one child).

## Implementation

```cpp
class PQTree {
 public:
  PQTree() {}

  void Init(int n) {
    n_ = n, rt_ = tot_ = n + 1;
    for (int i = 1; i <= n; i++) g_[rt_].emplace_back(i);
  }

  void Insert(const std::string &s) {
    s_ = s;
    Dfs0(rt_);
    Work(rt_);
    while (g_[rt_].size() == 1) rt_ = g_[rt_][0];
    Remove(rt_);
  }

  std::vector<int> ans() {
    DfsAns(rt_);
    return ans_;
  }

  ~PQTree() {}

 private:
  int n_, rt_, tot_, pool_[100001], top_, typ_[100001] /* 0-P 1-Q */,
      col_[100001] /* 0-black 1-white 2-grey */;
  std::vector<int> g_[100001], ans_;
  std::string s_;

  void Fail() {
    std::cout << "NO\n";
    std::exit(0);
  }

  int NewNode(int ty) {
    int x = top_ ? pool_[top_--] : ++tot_;
    typ_[x] = ty;
    return x;
  }

  void Delete(int u) { g_[u].clear(), pool_[++top_] = u; }

  void Dfs0(int u) {  // get color of each node
    if (u >= 1 && u <= n_) {
      col_[u] = s_[u] == '1';
      return;
    }
    bool c0 = false, c1 = false;
    for (auto &&v : g_[u]) {
      Dfs0(v);
      if (col_[v]) c1 = true;
      if (col_[v] != 1) c0 = true;
    }
    if (c0 && !c1)
      col_[u] = 0;
    else if (!c0 && c1)
      col_[u] = 1;
    else
      col_[u] = 2;
  }

  bool Check(const std::vector<int> &v) {
    int p2 = -1;
    for (int i = 0; i < static_cast<int>(v.size()); i++)
      if (col_[v[i]] == 2) {
        if (p2 != -1) return false;
        p2 = i;
      }
    if (p2 == -1)
      for (int i = 0; i < static_cast<int>(v.size()); i++)
        if (col_[v[i]]) {
          p2 = i;
          break;
        }
    for (int i = 0; i < p2; i++)
      if (col_[v[i]]) return false;
    for (int i = p2 + 1; i < static_cast<int>(v.size()); i++)
      if (col_[v[i]] != 1) return false;
    return true;
  }

  std::vector<int> Split(int u) {
    if (col_[u] != 2) return {u};
    std::vector<int> ng;
    if (typ_[u]) {  // Q
      if (!Check(g_[u])) {
        std::reverse(g_[u].begin(), g_[u].end());
        if (!Check(g_[u])) Fail();
      }
      for (auto &&v : g_[u])
        if (col_[v] != 2) {
          ng.emplace_back(v);
        } else {
          auto s = Split(v);
          ng.insert(ng.end(), s.begin(), s.end());
        }
    } else {  // P
      std::vector<int> son[3];
      for (auto &&x : g_[u]) son[col_[x]].emplace_back(x);
      if (son[2].size() > 1) Fail();
      if (!son[0].empty()) {
        int n0 = NewNode(0);
        g_[n0] = son[0];
        ng.emplace_back(n0);
      }
      if (!son[2].empty()) {
        auto s = Split(son[2][0]);
        ng.insert(ng.end(), s.begin(), s.end());
      }
      if (!son[1].empty()) {
        int n1 = NewNode(0);
        g_[n1] = son[1];
        ng.emplace_back(n1);
      }
    }
    Delete(u);
    return ng;
  }

  void Work(int u) {
    if (col_[u] != 2) return;
    if (typ_[u]) {  // Q
      int l = 1e9, r = -1e9;
      for (int i = 0; i < static_cast<int>(g_[u].size()); i++)
        if (col_[g_[u][i]]) checkmin(l, i), checkmax(r, i);
      for (int i = l + 1; i < r; i++)
        if (col_[g_[u][i]] != 1) Fail();
      if (l == r && col_[g_[u][l]] == 2) {
        Work(g_[u][l]);
        return;
      }
      std::vector<int> ng;
      for (int i = 0; i < l; i++) ng.emplace_back(g_[u][i]);
      auto s = Split(g_[u][l]);
      ng.insert(ng.end(), s.begin(), s.end());
      for (int i = l + 1; i < r; i++) ng.emplace_back(g_[u][i]);
      if (l != r) {
        s = Split(g_[u][r]);
        std::reverse(s.begin(), s.end());
        ng.insert(ng.end(), s.begin(), s.end());
      }
      for (int i = r + 1; i < static_cast<int>(g_[u].size()); i++)
        ng.emplace_back(g_[u][i]);
      g_[u] = ng;
    } else {  // P
      std::vector<int> son[3];
      for (auto &&x : g_[u]) son[col_[x]].emplace_back(x);
      if (son[1].empty() && son[2].size() == 1) {
        Work(son[2][0]);
        return;
      }
      g_[u].clear();
      if (son[2].size() > 2) Fail();
      g_[u] = son[0];
      int n1 = NewNode(1);
      g_[u].emplace_back(n1);
      if (son[2].size() >= 1) {
        auto s = Split(son[2][0]);
        g_[n1].insert(g_[n1].end(), s.begin(), s.end());
      }
      if (son[1].size()) {
        int n2 = NewNode(0);
        g_[n1].emplace_back(n2);
        g_[n2] = son[1];
      }
      if (son[2].size() >= 2) {
        auto s = Split(son[2][1]);
        std::reverse(s.begin(), s.end());
        g_[n1].insert(g_[n1].end(), s.begin(), s.end());
      }
    }
  }

  void Remove(int u) {  // remove the nodes with only one child
    for (auto &&v : g_[u]) {
      int tv = v;
      while (g_[tv].size() == 1) {
        int t = tv;
        tv = g_[tv][0];
        Delete(t);
      }
      v = tv, Remove(v);
    }
  }

  void DfsAns(int u) {
    if (u >= 1 && u <= n_) {
      ans_.emplace_back(u);
      return;
    }
    for (auto &&v : g_[u]) DfsAns(v);
  }
} T;
```

## Exercises

-   [CF243E Matrix](https://codeforces.com/problemset/problem/243/E)
-   [CF1552I Organizing a Music Festival](https://codeforces.com/contest/1552/problem/I)

## References

-   Booth, Kellogg S. & Lueker, George S. (1976).["Testing for the consecutive ones property, interval graphs, and graph planarity using PQ-tree algorithms"](https://www.sciencedirect.com/science/article/pii/S0022000076800451?via%3Dihub).*[Journal of Computer and System Sciences](https://en.wikipedia.org/wiki/Journal_of_Computer_and_System_Sciences)*.**13**(3): 335–379.[doi](https://en.wikipedia.org/wiki/Doi_%28identifier%29):[10.1016/S0022-0000(76)80045-1](https://doi.org/10.1016%2FS0022-0000%2876%2980045-1).
-   [PQ Tree Algorithm and Consecutive Ones Problem](https://gregable.com/2008/11/pq-tree-algorithm.html)
-   [CF243E Matrix PQTree - RainAir's Blog](https://blog.aor.sd.cn/archives/1657/)
