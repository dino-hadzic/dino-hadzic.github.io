---
title: Top Tree
---

author: F7487

## Self-Adjusting Top Tree

### Introduction

The Self-Adjusting Top Tree is a data structure for maintaining a fully dynamic forest, based on Top Tree theory, proposed by Tarjan and Werneck in 2005 in their paper Self-Adjusting Top Trees; it is abbreviated SATT.

A Self-Adjusting Top Tree supports, on any tree of the forest, path updates/queries, subtree updates/queries, and non-local search.

The Splay Tree is the foundation of SATT, but the Splay Tree used by SATT differs in details from an ordinary Splay (it has some extensions).

### Motivating problem

Maintain a forest supporting the following operations:

-   Delete or add an edge; it is guaranteed that the result is still a forest before and after the operation.

-   Modify the weights on a simple path of some tree.

-   Modify the weights of the subtree rooted at some vertex.

-   Query the sum of weights on a simple path of some tree.

-   Query the sum of weights of the subtree rooted at some vertex.

### Tree contraction

Any tree can be contracted into a single edge using the theory of **tree contraction**.

Concretely, tree contraction has two basic operations: **Compress** and **Rake**. The Compress operation picks a vertex $x$ of degree $2$; denote the two vertices adjacent to $x$ by $y$ and $z$; we add a new edge $yz$, store the information of vertex $x$ and edges $xz$, $xy$ in $yz$, and delete them. As shown in the figure.

![](./images/top-tree1.svg)

The Rake operation picks a vertex $x$ of degree $1$, where the vertex $y$ adjacent to $x$ must have degree greater than $1$; let $z$ be the other neighbor of $y$. We store the information of vertex $x$ and edge $xy$ in edge $yz$ and delete them. As shown in the figure.

![](./images/top-tree2.svg)

It is not hard to prove that any tree can be contracted into a single edge using only Compress and Rake operations, as shown in the figure.

![](./images/top-tree3.svg)

### Clusters

For convenience, we denote the original tree before any operations by $T$. The tree obtained from $T$ after some tree contraction operations (possibly none) is denoted $T_x$.

Let us study the information contained in some edge of some $T_x$.

Besides its own information (of course, if the edge does not exist in $T$, it has no information of its own), this edge may also contain information of other vertices and edges merged into it by Compress/Rake operations. Let us pick an edge from the tree contraction process in the figure below and see which vertices and edges of $T$ the information it contains represents.

![](./images/top-tree4.svg)

In the figure, the chosen edge and the corresponding part of the graph are circled in red.

We can see that the vertices and edges in $T$ represented by the information of this edge are connected. Generalizing, the information stored in any edge of any $T_x$ always forms a connected subgraph of $T$. We call such a connected subgraph a **cluster**.

However, a cluster is an **incomplete subgraph**: some endpoints of the edges it contains are not contained in the cluster itself. We call these endpoints the **endpoints** of the cluster, the vertices of the connected subgraph it contains **internal nodes**, and the edges of the connected subgraph **internal edges**.

Every cluster has the following properties:

1.  A cluster stores and maintains only the information of its internal nodes and internal edges.

2.  A cluster has two endpoints. These are the two vertices joined in $T_x$ by the edge representing the cluster. The path between the two endpoints is called the **cluster path**; if the two endpoints of a cluster are $x$ and $y$, we denote the cluster by $C(x,y)$.

3.  Internal nodes are adjacent only to endpoints or internal nodes.

In particular, every edge of $T$ is a cluster by itself (containing only the edge's own information); such a cluster is called a **base cluster**. For the final $T_x$ obtained by contracting $T$ down to a single edge, the cluster represented by that edge contains the information of the whole $T$ except the two endpoints; this cluster is called the **root cluster**.

![](./images/top-tree5.svg)

In the figure, the base clusters mentioned above are marked in red.

Looking at Compress/Rake from the perspective of clusters, we find that both operations "merge two into one", leaving a new cluster, so the tree contraction process is also the process of merging all base clusters into a single cluster.

We thus also obtain the figure below, another representation of a sequence of tree contraction operations.

![](./images/top-tree6.svg)

### Top Tree

We now want to represent the whole tree contraction process of some tree.

We could use the two methods above, but this is very cumbersome: if the contraction takes $n$ steps, we need $n$ trees to represent the whole contraction.

For a more convenient representation of a tree contraction of some tree, we introduce the **Top Tree**.

![](./images/top-tree7.jpg)

The figure shows a Top Tree based on the contraction method and original tree above.

A Top Tree has the following properties:

1.  A Top Tree corresponds to an original tree and one way of contracting it; every node of the Top Tree represents some edge of some $T_x$, i.e. some cluster formed during the contraction. Nodes of the form $N_x$ in the figure represent the cluster formed by the operation `compress(x)`.

2.  A node of the Top Tree has two children (each representing a cluster); the cluster represented by this node is the new cluster obtained by merging these two clusters with a Compress or Rake operation.

3.  The leaves of the Top Tree are base clusters and its root is the root cluster. Hence, if we layer a Top Tree by topological order, each layer represents a $T_x$.

### Maintaining information with a ternary Self-Adjusting Top Tree

#### Principle

The enormous simplification of the tree contraction process by the Top Tree shows us the possibility of maintaining information on a tree by maintaining the contraction process; SATT maintains tree information exactly by this principle.

Note that the tree contraction process is also a process of gradually adding information of the tree: once we execute `compress(x)`, the information of vertex $x$ starts to appear in some cluster from that moment on, affecting our results.

Suppose we maintain some tree $T$ with a Top Tree, every vertex and edge has a weight, and we want to maintain the sum of weights of $T$.

If we now want to modify the weight of some vertex $x$ of $T$, we obviously have to update the information of all Top Tree nodes whose cluster contains $x$, which costs $O(n)$ per operation.

However, if the chosen vertex has few Top Tree nodes whose cluster contains $x$, i.e. its information is added to clusters as late as possible, the time complexity of a single operation improves greatly. As shown in the figure.

![](./images/top-tree8.jpg)

SATT maintains tree information by changing the order in which the information of **a vertex/a path** is added to clusters during tree contraction (to reduce the per-operation cost of modifying it).

### Actual structure

We first layer the original tree $T$ and fix a root. Then consider the root cluster of the Top Tree of some contraction order; it has two endpoints. We let one of these endpoints be the root of the original tree and choose the other arbitrarily.

![](./images/top-tree9.jpg)

As in the figure, a pair of endpoints is chosen for the root cluster; here the endpoints are circled together with the cluster.

From the basic operations of tree contraction we know that the vertices and edges on the cluster path $(j,h,c,jh,hc)$ are finally added to $C(k,g)$ by Compress operations, while the vertices not on the cluster path $(a,b,i,f,g,e,ig,\cdots)$ are added to $C(k,g)$ by Rake operations.

Take out the cluster path separately; it is a tree of special shape (a chain), and we build a top tree for it (the contraction order it represents is arbitrary).

![](./images/top-tree10.jpg)

We call this structure the **Compress Tree**, because in this Top Tree the two children of any node are merged into their parent by a Compress operation.

The nodes of a Compress Tree are called **Compress Nodes**. Considering only the current cluster path, a non-leaf Compress Node represents one compress: merge the information of the left and right children, then add the information of vertex $x$ stored by this `compress(x)` itself. This Compress Tree maintains the information of the cluster path of $C(k,g)$.

Moreover, in the Compress Tree we actually impose some restrictions on the Top Tree used. Note that the Compress Tree maintains a chain whose vertices have pairwise distinct depths in $T$; we require that the inorder traversal order of the base clusters in the Compress Tree agrees with the depths of the corresponding edges in $T$, with smaller inorder position meaning smaller depth. The same holds for the `compress(x)` corresponding to each vertex $x$.

Now let us maintain the information off the cluster path. Suppose the vertices and edges off the cluster path have already formed maximal clusters, and these maximal clusters are formed by raking together the smaller clusters circled in blue. We represent the process of merging several smaller clusters into a maximal cluster by a ternary tree; analogously, we call this structure the **Rake Tree**, and the nodes of the Rake Tree **Rake Nodes**. Every Rake Node represents a cluster formed by raking its left and right children onto the smaller cluster represented by its middle child. See the figure below; every node of the Rake Tree represents smaller clusters of $T$ with the same endpoints.

![](./images/top-tree11.jpg)

In the figure, the maximal clusters are circled in blue and the smaller clusters in yellow.

We treat those smaller clusters the same way: choose a cluster path for them, build a Compress Tree, … and recurse, producing many Compress Trees and Rake Trees representing the contraction process.

![](./images/top-tree12.jpg)

The figure above shows the Rake-Compress Tree of the original tree (since every Rake Node is attached to a Compress Tree, it looks like a Rake Tree attached to many Compress Trees) and the Compress Tree representing the root cluster path.

Consider joining these trees together in some way so that they form an ordered whole. Let the common endpoint of the set of smallest clusters represented by a Rake Tree be vertex $x$. To the middle children of these Rake Nodes (a set of Compress Trees) we add the other endpoint, different from $x$, while preserving the inorder traversal and the basic properties of the Top Tree, as shown in the figure.

![](./images/top-tree13.jpg)

This step effectively lets the addition of a vertex of $T$ by a Rake operation happen directly in the Compress Tree; this not only lets us maintain the information of Rake Nodes correctly (just merge the information of the three children), but also makes the structure of the Compress Tree more complete. Next, we change the Compress Tree into a ternary tree: if the common endpoint of some Rake Tree is vertex $x$, we hang the Rake Tree as the middle child of `compress(x)`, as shown in the figure.

![](./images/top-tree14.jpg)

The meaning of the ternarized `compress(x)` node now becomes: first rake its middle child onto the cluster path, then aggregate the information of the left and right children and vertex $x$.

Finally, we handle the Compress Tree of the root cluster path: consistently with all other Compress Trees, add its two endpoints in inorder, so that its root stores the information of the whole $T$.

Thus we have achieved maintaining the information of a tree with a ternary Self-Adjusting Top Tree.

![](./images/top-tree15.jpg)

To summarize, SATT has the following properties:

1.  SATT consists of Compress Trees and Rake Trees; a Compress Tree is a special Top Tree and a Rake Tree is a ternary tree; both correspond to the contraction process of a tree.

2.  A node of a Compress Tree has at most three children. A Compress Tree supports rotations like those of a Splay tree (it suffices to keep the inorder traversal unchanged; when rotating a node, its middle child stays put).

3.  A node of a Rake Tree always has a middle child. A Rake Tree supports rotations like those of a Splay tree (it suffices to keep the inorder traversal unchanged; when rotating a node, its middle child stays put).

4.  The topological order of SATT reflects the contraction order of the original tree $T$.

Can SATT achieve the "change of the order in which the information of a vertex/a path is added to clusters during tree contraction" mentioned above? The answer is yes.

SATT has an operation `access(x)` that makes vertex $x$ the non-root endpoint of the root cluster and at the same time makes `compress(x)` the root of the SATT.

With `access(x)` we can, in amortized $O(\log n)$, rotate the node representing `compress(x)` to the root of the whole SATT; by the fourth property of SATT, we have changed the order of the operation `compress(x)` so that it is executed last, so the information of vertex $x$ is added last; thus when we want to modify the information of vertex $x$, we only need to update `compress(x)`.

### Implementation

#### Push functions

First consider pushing information upwards, i.e. the function `Pushup(x)`. When maintaining the information of a SATT node, we first distinguish whether the node is in a Compress Tree or a Rake Tree; the reason is explained above and not repeated here. Below we take maintaining the subtree size of a vertex as an example.

```cpp
// ls(x) left child of x
// rs(x) right child of x
// ms(x) middle child of x
// type==0 is a Compress Node
// type==1 is a Rake Node
void pushup(int x, int type) {
  if (type == 0)
    size[x] = size[rs(x)] + size[ms(x)] + 1;
  else
    size[x] = size[rs(x)] + size[ms(x)] + size[ls(x)];
  return;
}
```

To query the subtree size of vertex $x$, Access it to the SATT root; the answer is the size of its middle child $+1$, because, as explained above, after Access its middle child is exactly its real subtree.

Then consider pushing information downwards, i.e. the function `Pushdown(x)`. If we want to modify a whole subtree of the original tree, a natural idea is: Access this node directly to the SATT root and put a tag on its middle child. Similarly, to query a subtree, Access and then query the middle child.

If we want to modify a whole path of the original tree, we expose the two endpoints of the path, where `expose(x, y)` means making vertex $x$ the root of $T$ and vertex $y$ the other endpoint of the root cluster. Correspondingly in the SATT, the Compress Tree of the root cluster is then the path from $x$ to $y$. So we just put a tag on the Compress Tree of the root cluster. Similarly, to query a path, expose and then query the root.

Thus we know how to solve the motivating problem.

```cpp
void pushdown(int x, int type) {
  if (type == 0) {
    // handle the path
    chain[ls(x)] += chain[x] chain[rs(x)] += chain[x];
    val[ls(x)] += chain[x];
    val[rs(x)] += chain[x];
    // handle the subtree
    subtree[ls(x)] += subtree[x];
    subtree[rs(x)] += subtree[x];
    subtree[ms(x)] += subtree[x];
    val[ls(x)] += subtree[x];
    val[rs(x)] += subtree[x];
    val[ms(x)] += subtree[x];
    subtree[x] = 0;
  } else {
    subtree[ls(x)] += subtree[x];
    subtree[rs(x)] += subtree[x];
    subtree[ms(x)] += subtree[x];
    val[ls(x)] += subtree[x];
    val[rs(x)] += subtree[x];
    val[ms(x)] += subtree[x];
    subtree[x] = 0;
  }
  return;
}

// push down the tags
void pushall(int x, int type) {
  if (!isroot(x)) pushall(father[x], type);
  pushdown(x, type);
  return;
}
```

#### Splay functions

We know that both the Rake Trees and the Compress Trees of a SATT can be rotated, i.e. they can be maintained with Splay. Hence we can write the following code:

```cpp
// is the middle child of some node or has no parent
// ls left child of a SATT node
// rs right child of a SATT node
// ms middle child of a SATT node
// type==1 in a Rake Tree
// type==0 in a Compress Tree
bool isroot(int x) { return rs(father[x]) != x && ls(father[x]) != x; }

bool direction(int x) { return rs(father[x]) == x; }

void rotate(int x, int type) {
  int y = father[x], z = father[y], d = direction(x), w = son[x][d ^ 1];
  if (z) son[z][ms(z) == y ? 2 : direction(y)] = x;
  son[x][d ^ 1] = y;
  son[y][d] = w;
  if (w) father[w] = y;
  father[y] = x;
  father[x] = z;
  pushup(y, type);
  pushup(x, type);
  return;
}

void splay(int x, int type, int goal = 0) {
  pushall(x, ty);  // push down the tags
  for (int y; y = father[x], (!isroot(x)) && y != goal; rotate(x, ty)) {
    if (father[y] != goal && (!isroot(y))) {
      rotate(direction(x) ^ diretion(y) ? x : y, type);
    }
  }
  return;
}
```

It is worth noting that the functions `direction` and `isroot` differ from those of an ordinary Splay, because no matter how the node is rotated, its middle child never changes.

#### Access functions

The meaning of `access(x)` is: rotate vertex $x$ to the root of the whole SATT so that vertex $x$ becomes one of the two endpoints of the root cluster (the other endpoint being the root of $T$), without changing the structure or the root of the original tree.

To implement `access(x)`, we first rotate it to the root of the Compress Tree it belongs to, then remove the right child of vertex $x$, making vertex $x$ an endpoint of the cluster corresponding to its Compress Tree.

```cpp
if (rs(x)) {
  int y = new_node();
  setfather(ms(x), y, 0);
  setfather(rs(x), y, 2);
  rs(x) = 0;
  setfather(y, x, 2);
  pushup(y, 1);
  pushup(x, 0);
}
```

If vertex $x$ has now reached the root, we stop; otherwise, we perform the following steps to let it jump over the Rake Tree above it:

1.  Splay its parent (necessarily a Rake Node) to the root of its Rake Tree;

2.  Splay the grandparent of $x$ (necessarily a Compress Node) to the root of its Compress Tree.

3.  If the grandparent of $x$ has a right child, swap vertex x with the grandparent's right child, update the information, and stop.

4.  If the grandparent has no right child, first make vertex $x$ the grandparent's right child; now the former parent of vertex $x$ has no middle child, and by the property of Rake Nodes above it cannot exist. So call the `Delete` function to delete it, and stop.

Steps 1 and 2 together are called **Local Splay**. Steps 3 and 4 together are called **Splice**. For convenience, we write all of them in the function `Splice(x)`.

The function `Delete(x)` mentioned above works as follows:

1.  Check whether the vertex $x$ to be deleted has a left child; if so, rotate the successor in the left child's subtree below vertex $x$ (as the new left child), then make the right child (if any) the right child of the left child; now the left child of vertex $x$ replaces vertex $x$. This corresponds to the merge operation of Splay.

2.  If there is no left child, let its right child replace vertex $x$ directly.

It is not hard to see that `Splice(x)` changes the choice of endpoints of some clusters of the original tree. After one splice, we treat the parent of vertex $x$ as the new vertex $x$ and perform the next splice.

In the end we find that the vertex $x$ we started with is necessarily at the rightmost position of the Compress Tree of the root cluster. We just need a final **Global Splay** to rotate it to the root of the SATT.

```cpp
// ls left child of a SATT node
// rs right child of a SATT node
// ms middle child of a SATT node
// son[x][0] ls
// son[x][1] rs
// son[x][2] ms
// type==1 in a Rake Tree
// type==0 in a Compress Tree
int new_node() {
  if (top) {
    top--;
    return Stack[top + 1];
  }
  return ++tot;
}

void setfather(int x, int fa, int type) {
  if (x) father[x] = fa;
  son[fa][type] = x;
}

void Delete(int x) {
  setfather(ms(x), father[x], 1);
  if (ls(x)) {
    int p = ls(x);
    pushdown(p, 1);
    while (rs(p)) p = rs(p), pushdown(p, 1);
    splay(p, 1, x);
    setfather(rs(x), p, 1);
    setfather(p, father[x], 2);
    pushup(p, 1);
    pushup(father[x], 0);
  } else
    setfather(rs(x), father[x], 2);
  Clear(x);
}

void splice(int x) {
  // local splay
  splay(x, 1);
  int y = father[x];
  splay(y, 0);
  pushdown(x, 1);
  // splice
  if (rs(y)) {
    swap(father[ms(x)], father[rs(y)]);
    swap(ms(x), rs(y));
  } else
    Delete(x);
  pushup(x, 1);
  pushup(y, 0);
}

void access(int x) {
  splay(x, 0);
  if (rs(x)) {
    int y = new_node();
    setfather(ms(x), y, 0);
    setfather(rs(x), y, 2);
    rs(x) = 0;
    setfather(y, x, 2);
    pushup(y, 1);
    pushup(x, 0);
  }
  while (father[x]) {
    splice(father[x]);
    x = father[x];
    pushup(x, 0);
  }
  splay(x, 0)  // global splay
}
```

To make a vertex the root of the original tree, we Access vertex $x$ to the SATT root; at this point vertex $x$ is already an endpoint of the final cluster. By the inorder property of the Compress Tree, mirroring the Compress Tree containing vertex $x$ (swapping the left and right children of all nodes) makes vertex $x$ the root of the original tree. In the implementation, we do this by putting a reversal tag on vertex $x$ and pushing it down later.

```cpp
void makeroot(int x) {
  access(x);
  push_rev(x);
}
```

Thus `expose(x, y)` follows immediately:

```cpp
void expose(int x, int y) {
  makeroot(x);
  access(y);
}
```

### Link & Cut

Now we want to add an edge between two unconnected vertices of the original tree. We first make one of them, vertex $x$, the root of the original tree, then rotate the other vertex $y$ to the root; at this point vertex $y$ should become the right child of vertex $x$. Then hang this edge on the right child of vertex $y$ (in a SATT that only maintains vertices this step can be omitted).

```cpp
void Link(int x, int y, int z) {
  // z represents the edge connecting x and y
  access(x);
  makeroot(y);
  setfather(y, x, 1);
  setfather(z, y, 0);
  pushup(x, 0);
  pushup(y, 0);
}
```

`Cut` works on much the same principle as `Link`.

```cpp
void cut(int x, int y) {
  expose(x, y);
  clear(rs(x));  // delete the base cluster xy
  father[x] = ls(y) = rs(x);
  pushup(y, 0);
}
```

### Complete code

??? note "[Luogu P3690【模板】动态树](https://www.luogu.com.cn/problem/P3690)"
    ```cpp
    --8<-- "docs/ds/code/top-tree/top-tree_1.cpp"
    ```

### Proof of the time complexity of SATT

In a SATT (with $n$ nodes), let the potential function of its current state $x$ be

$$
\varphi(x)= \sum_{i=1}^{n} r(i)
$$

where $r(i) = \lceil \log_2 \text{siz}(i) \rceil$ and $\text{siz}(i)$ is the size of the subtree rooted at $i$.

Then the amortized complexity of a splay in the SATT is obviously still $3n\log n + 1$, even though the SATT is a ternary tree.

Hence for the SATT, as long as we prove that the complexity of the Access function is correct, we have proved the time complexity of the SATT.

Let us analyze the amortized complexity of Access step by step.

We first rotate vertex $x$ to the root of its Compress Tree; the amortized complexity of this step is

$$
a \leq  3\log n +1
$$

Next we make vertex $x$ have no right child; the amortized complexity of this step is

$$
a = 1 + r'(\gamma)- 0 \leq \log n +1
$$

![](./images/top-tree16.jpg)

The figure shows the process of removing the right child of vertex $x$.

Then comes the alternation of Local Splay and Splice; after several Splices, vertex $x$ is rotated to the root of the SATT. We analyze one pair of Local Splay, Splice:

![](./images/top-tree17.jpg)

![](./images/top-tree18.jpg)

![](./images/top-tree19.jpg)

The figures show one Splice on vertex $x$, excluding the final left rotation of vertex $x$.

For convenience, let $r_x(i)$ be the $r$ value of vertex $i$ in state $x$.

From the figure, it is easy to see that the amortized complexity of the operation from state 1 to state 2 (the Local Splay rotating the parent of vertex $x$ to the root of its Rake Tree) is

$$
a \leq  3(r_2(\gamma)- r_1(\gamma))+1
$$

From the figure, it is easy to see that the amortized complexity of the operation from state 2 to state 3 (the Local Splay rotating the grandparent of vertex $x$ to the root of its Compress Tree) is

$$
a \leq  3(r_3(B)- r_2(B))+1
$$

The key is to analyze the operation from state 3 to state 4 (Splice)

$$
a = r_4(\gamma) -r_3(\gamma) +1
$$

It is not hard to see that $r_4(\gamma) \leq r_3(B)$

so the amortized complexity of this operation is

$$
\begin{aligned}
a &\leq r_3(B)- r_3(\gamma)+1\\
&\leq 3(r_3(B)- r_3(\gamma))+1\\
\end{aligned}
$$

Combining the above, the complexity of one Splice is

$$
a\leq 3r_3(B)+3r_3(B)+3r_2(\gamma)-3r_3(\gamma)-3r_2(B)-3r_1(\gamma)+3
$$

Denote by $r'(X)$ the $r$ value of the vertex $X$ of the next Splice (i.e. vertex $B$ in state 4), and note that $r_3(\gamma),r_1(\gamma) \ge r_1(X)$, $r_3(B),r_2(\gamma) \leq r'(X)$ and $r_3(B)=r_2(B)$, so

$$
a\leq  9(r'(X)-r(X))+3
$$

Besides the complexity above, a Splice may also incur additional amortized cost due to `delete(x)`; denote this part by $a' \leq 3\log n +1$.

Ignoring $a'$ for now, the $r'(X)$ of each Splice equals the $r(X)$ of the next one, and the $r(X)$ of the first Splice equals the $r(X)$ at the time we initially rotated vertex $x$ to the root of its Compress Tree; so for the complexity of one `access(x)` without counting `delete(x)`, we have:

$$
a \leq 9(r'(x)-r(x))+ 3k + 1
$$

where $k$ is the number of Splices.

It seems that $a$ carries a term $3k+1$ that prevents the amortized analysis, but we have a way to deal with it. Note that zig-zig/zig-zag rotations can be amortized as follows

$$
\begin{aligned}
a &\leq 3(r'(X)-r(X)) + q\\
&\leq 3(q-1)(r'(X)-r(X))
\end{aligned}
$$

If we can find enough zig-zig and zig-zag operations, we can spread this $3k+1$ over them and thereby eliminate the $3k+1$.

We find that the Global Splay contains exactly this many zig-zig and zag-zig operations for us to use, because the number of nodes in the Global Splay is certainly greater than $k$, and the number of nodes on the path from vertex $x$ to the root of the Global Splay is at least $k$; in other words, one `access(x)` necessarily contains at least $\dfrac k2$ zig-zag operations. Counting the amortized complexity $a \leq 3\log n +1$ of the Global Splay, the amortized complexity of one `access(x)` without counting `delete(x)` is

$$
\begin{aligned}
a&\leq 9(r'(X)-r(X)) + 3k + 1 + 18(r''(X)-r'(X)) -S+1 +3 \log n +1,S \ge 3k\\
a&\leq 18(r''(X)-r(X)) +2 +3\log n+1\\
a&\leq 21(r''(X)-r(X)) +3
\end{aligned}
$$

Now include $a'$ and write the total formula for $m$ `access(x)` operations.

$$
\sum_{i=1}^m a_i' + \sum_{i=1}^m a_i = \sum_{i=1}^m c_i + \varphi(x_n) -\varphi(x_0)
$$

What we want is the actual complexity

$$
\begin{aligned}
\sum_{i=1}^m c_i &= \sum_{i=1}^m a_i +\sum_{i=1}^m a_i' - \varphi(x_n) +\varphi(x_0)\\
&\le \sum_{i=1}^m a_i' + 21m\log n +n\log n +3m
\end{aligned}
$$

Note that the essence of `delete(x)` is deleting a Rake Node, but in $m$ operations we add at most $m$ Rake Nodes; by the definition of Rake Nodes we initially have at most $n$ Rake Nodes, so in total we perform at most $m+n$ `delete(x)` operations. From $a' \leq 3\log n +1$ we get

$$
\sum_{i=1}^m c_i \leq 3(m+n)\log n + 21m\log n +n\log n +4m +n
$$

So we have proved the complexity of Access, and the other functions are either based on Access or take constant time per operation, so we have proved the complexity of SATT.

By the way, if, like in LCT, we omit the Global Splay and instead directly rotate the vertex being Accessed once at every Splice, the time complexity is still correct (in practice the version without Global Splay is much faster and runs neck and neck with LCT on Luogu P3690).

### Examples

#### Example 1

???+ note "[CEOI 2019 Dynamic Diameter](https://loj.ac/p/3163)"
    Given a tree with $n$ nodes and edge weights, there are $q$ updates; each modifies the weight of one edge and asks for the diameter of the tree. Must be online.

To maintain the dynamic diameter, after building the SATT we only need to maintain the answer of every node in `Pushup(x)` and finally query the answer at the root (i.e. the diameter of the whole tree).

```cpp
void pushup(int x, int op) {
  if (op == 0) {
    // Compress Node
    len[x] = len[ls(x)] + len[rs(x)];
    diam[x] = maxs[ls(x)][1] + maxs[rs(x)][0];
    diam[x] =
        max(diam[x], max(maxs[ls(x)][1], maxs[rs(x)][0]) + maxs[ms(x)][0]);
    diam[x] = max(diam[x], max(max(diam[ls(x)], diam[rs(x)]), diam[ms(x)]));
    maxs[x][0] =
        max(maxs[ls(x)][0], len[ls(x)] + max(maxs[ms(x)][0], maxs[rs(x)][0]));
    maxs[x][1] =
        max(maxs[rs(x)][1], len[rs(x)] + max(maxs[ms(x)][0], maxs[ls(x)][1]));
  } else {
    // Rake Node
    diam[x] = maxs[ls(x)][0] + maxs[rs(x)][0];
    diam[x] =
        max(diam[x], maxs[ms(x)][0] + max(maxs[ls(x)][0], maxs[rs(x)][0]));
    diam[x] = max(max(diam[x], diam[ms(x)]), max(diam[ls(x)], diam[rs(x)]));
    maxs[x][0] = max(maxs[ms(x)][0], max(maxs[ls(x)][0], maxs[rs(x)][0]));
  }
  return;
}
```

Here $diam$ is the answer of the current node (the diameter of the cluster represented by this node). $len$ is the length of the cluster path containing the current Compress Node, and $maxs_{0/1}$ is the maximum distance from the Compress Node to the internal nodes and endpoints of the cluster without choosing the cluster-path child/without choosing the parent (for a Rake Node only $maxs_0$ is stored, the maximum distance from the upper endpoint of the current cluster to the internal nodes and endpoints). For each query just read diam at the SATT root; correctness is obvious.

Note the changes to `Pushrev(x)`.

```cpp
void pushrev(int x) {
  if (!x) return;
  r[x] ^= 1;
  swap(ls(x), rs(x));
  swap(maxs[x][0], maxs[x][1]);
}
```

#### Example 2

???+ note "[\"CSP-S 2019\" Centroid of a tree](https://loj.ac/p/3213)"
    Given a tree, for each edge delete it alone and compute the sum of the indices of the centroids of the two resulting subtrees; output the total sum.

If we could maintain the centroid of a tree dynamically in $O(\log n)$, we would have solved this problem.

SATT supports maintaining the centroid dynamically in $O(\log n)$; this requires **non-local search**.

For a property on a tree, if a vertex/edge that has this property in the whole tree also has it in every subtree containing it, we call the property **local**; otherwise we call it **non-local**. Local information can generally be maintained via `pushup(x)`.

For example, the minimum weight is local, because if a vertex/edge has the minimum weight in the whole tree, it also has the minimum weight in every subtree containing it, while the second smallest weight is obviously non-local.

The $diam$ we maintained above is also local information.

Back to the problem: the centroid is obviously non-local information and cannot be maintained by a simple `pushup(x)`. We consider searching on the SATT:

Our search starts from the root of the SATT, i.e. the root cluster. Note that the centroid has a nice property: if the number of vertices on one side of an edge is greater than or equal to the number on the other side, then there is at least one centroid on that side of the edge (there may be two centroids).

Let $sum$ denote the number of vertices of a cluster, and $maxs$ the maximum $sum$ among the middle children of all Rake Nodes of a Rake Tree.

```cpp
void pushup(int x, int op) {
  if (op == 0) {
    // Compress Node
    sum[x] = sum[ls(x)] + sum[rs(x)] + sum[ms(x)] + 1;
  } else {
    // Rake Node
    maxs[x] = max(maxs[ls(x)], max(maxs[rs(x)], sum[ms(x)]));
    sum[x] = sum[ls(x)] + sum[rs(x)] + sum[ms(x)];
  }
}
```

![](./images/top-tree20.jpg)

The figure shows the SATT during Non-local Search and the corresponding original tree $T$.

We make the following comparisons:

1.  Compare the $sum$ of cluster $compress(Y)$ with the $sum$ of the union of cluster $compress(Z)$, cluster $A$ and vertex $X$ (temporarily called cluster $\alpha$). If the $sum$ of $compress(Y)$ is greater than or equal to the latter, at least one centroid lies in the subtree of $compress(Y)$, and we recurse into $compress(Y)$. (If equality holds, vertex $X$ is also a centroid and must be recorded.)

2.  Compare the $sum$ of cluster $compress(Z)$ with the $sum$ of the union of cluster $compress(Y)$, cluster $A$ and vertex $X$ (temporarily called cluster $\beta$). If the $sum$ of $compress(Z)$ is greater than or equal to the latter, at least one centroid lies in the subtree of $compress(Z)$, and we recurse into $compress(Z)$. (If equality holds, vertex $X$ is also a centroid and must be recorded.)

3.  Compare the $sum$ of the smaller cluster with the largest $sum$ in the Rake Tree of the middle child of vertex $x$ with the $sum$ of the union of cluster $compress(Y)$, cluster $A$, vertex $X$ and the other smaller clusters (temporarily called cluster $Y$). If the $sum$ of that smaller cluster is greater than or equal to the latter, at least one centroid lies in the subtree of that smaller cluster, and we recurse into it. If equality holds, vertex $X$ is also a centroid and must be recorded.

4.  If none of the comparisons above recurses, vertex $X$ is certainly a centroid; record it and stop.

The first step of the search is obviously correct; how should we search afterwards?

Suppose we recurse into $Y$; now the information stored at $Y$ is incomplete, because $compress(Y)$ only stores the information of its own cluster, while we want the centroid of the whole tree. The solution is to record the information of the previous cluster and, when comparing at vertex $Y$, merge the information of the previous cluster with that of vertex $Y$. The concrete implementation is as follows:

```cpp
void non_local_search(int x, int lv, int rv, int op) {
  // lv and rv are the information of the previously searched cluster
  if (!x) return;
  psd(x, 0);
  if (op == 0) {
    if (maxs[ms(x)] >=
        sum[ms(x)] - maxs[ms(x)] + sum[rs(x)] + sum[ls(x)] + lv + 1 + rv) {
      if (maxs[ms(x)] ==
          sum[ms(x)] - maxs[ms(x)] + sum[rs(x)] + sum[ls(x)] + lv + 1 + rv) {
        if (ans1)
          ans2 = x;
        else
          ans1 = x;
      }
      non_local_search(
          ms(x),
          sum[ms(x)] - maxs[ms(x)] + sum[rs(x)] + sum[ls(x)] + 1 + lv + rv, 0,
          1);
      return;
    }
    if (ss[rs(x)] + rv >= ss[ms(x)] + ss[ls(x)] + lv + 1) {
      if (ss[rs(x)] + rv == ss[ms(x)] + ss[ls(x)] + lv + 1) {
        if (ans1)
          ans2 = x;
        else
          ans1 = x;
      }
      non_local_search(rs(x), sum[ms(x)] + 1 + sum[ls(x)] + lv, rv, 0);
      return;
    }
    if (sum[ls(x)] + lv >= sum[ms(x)] + sum[rs(x)] + 1 + rv) {
      if (sum[ls(x)] + lv == sum[ms(x)] + sum[rs(x)] + 1 + rv) {
        if (ans1)
          ans2 = x;
        else
          ans1 = x;
      }
      non_local_search(ls(x), lv, rv + sum[ms(x)] + 1 + sum[rs(x)], 0);
      return;
    }
  } else {
    if (maxs[ls(x)] == maxs[x]) {
      non_local_search(ls(x), lv, rv, 1);
      return;
    }
    if (maxs[rs(x)] == maxs[x]) {
      non_local_search(rs(x), lv, rv, 1);
      return;
    }
    non_local_search(ms(x), lv, rv, 0);
    return;
  }
  if (ans1)
    ans2 = x;
  else
    ans1 = x;
}
```

??? note "Sample code"
    ```cpp
    --8<-- "docs/ds/code/top-tree/top-tree_2.cpp"
    ```

### Reference

1.  Robert E. Tarjan and Renato F. Werneck. 2005. Self-adjusting top trees. In Proceedings of the sixteenth annual ACM-SIAM symposium on Discrete algorithms (SODA '05). Society for Industrial and Applied Mathematics, USA, 813–822. DOI 10.5555/1070432.1070547

2.  [negiizhao's blog](https://negiizhao.blog.uoj.ac/blog/4912)
