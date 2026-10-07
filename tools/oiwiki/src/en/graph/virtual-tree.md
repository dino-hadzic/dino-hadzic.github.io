---
title: Virtual tree
---

## Introduction

???+ note "["SDOI2011" War of Attrition](https://www.luogu.com.cn/problem/P2495)"
    In a war, the battlefield consists of $n$ islands and $n-1$ bridges, and it is guaranteed that there is exactly one path between any two islands. Our army has found out that the enemy headquarters is on the island numbered $1$ and that they no longer have enough energy to sustain the fight; victory is in sight. It is known that $k$ other islands are rich in energy; to prevent the enemy from obtaining energy, our army's task is to blow up some bridges so that the enemy cannot reach any energy-rich island. Since bridges differ in material and structure, blowing up different bridges has different costs, and our army wants to achieve the goal with the minimum total cost.
    
    The reconnaissance department also found that the enemy has a mysterious machine. Even after we cut off all energy, they can use that machine. Its effect not only repairs all the bridges we blew up, but also redistributes the resources at random (though it is guaranteed that resources will not be placed on island $1$). However, the reconnaissance department also found that this machine can only be used $m$ times, so we just need to complete each task.
    
    For all data, $2\le n\le 2.5\times 10^5,1\le m\le 5\times 10^5,\sum k_i\le 5\times 10^5,1\le k_i\le n-1$.

### Naive approach

For the problem above, it is not hard to see that if the tree has few nodes, we can directly run a DP.

First, we call the nodes selected in a query the **"key nodes"**.

Let $Dp(i)$ denote the **minimum cost** to make $i$ not connected to any key node in its subtree.

Let $w(a,b)$ denote the weight of the edge between $a$ and $b$.

Then, enumerating the children $v$ of $i$:

-   if $v$ is not a key node: $Dp(i)=Dp(i) + \min \{Dp(v),w(i,v)\}$;
-   if $v$ is a key node: $Dp(i)=Dp(i) + w(i,v)$.

Great, this gives us an $O(nq)$ solution.

Sounds interesting.

### Optimized approach

It is not hard to notice that many nodes are actually useless. Take the figure below as an example:

![vtree-1](images/vtree-tree.svg)

If the key nodes we select are:

![vtree-2](images/vtree-key-vertex.svg)

In the figure only the two red nodes are **key nodes**, and all other nodes are "non-key nodes".

For this problem, we only need to ensure that the red nodes cannot reach node $1$.

By inspection we can conclude that the right subtree of node $1$ (although there may actually be several subtrees, here there are only two, so we call it that for now) does not contain a single red node, **so there is no need to DP on it**.

Looking at the constraints of the problem, the total number of red nodes (key nodes) is of the same order as $n$, which means that in a single query the red nodes are actually very sparse with respect to the whole tree, so it would be nice if we could make the complexity depend on the total number of red nodes.

Therefore we need to **condense the information, condensing a whole big tree into a small tree**.

## Virtual Tree

This brings us to the concept of the **"virtual tree"**.

Let us first look intuitively at what a virtual tree looks like.

In the figures below, the red nodes are the key nodes we selected. Both red and black nodes are nodes of the virtual tree. The black edges are the edges of the virtual tree.

![vtree-3](images/vtree-vtree1.svg)

![vtree-4](images/vtree-vtree2.svg)

![vtree-5](images/vtree-vtree3.svg)

![vtree-6](images/vtree-vtree4.svg)

Since the LCA of any two key nodes also carries important information that needs to be kept, we need to keep their LCAs too, so the virtual tree does not necessarily contain only key nodes.

It is not hard to see that the ancestor-descendant relationships in the virtual tree do not change. (That is, nothing weird happens like $a$ originally being an ancestor of $b$ and later $a$ becoming a descendant of $b$.)

But we cannot enumerate the LCAs by brute force in $O(k^2)$, so it is natural to think of the following: first sort the key nodes by DFS order, then compute the LCA of every two adjacent key nodes (adjacent meaning that the absolute difference of their indices in the sorted sequence equals 1), and add it to the virtual tree.

Our top priority is how to construct the virtual tree.

Before proposing a method, let us first confirm a fact: in the virtual tree, as long as the ancestor-descendant relationships are not changed, nodes can be added arbitrarily.

That is, if we wanted to, we could add all nodes of the original tree into the virtual tree without getting WA (although it would cause TLE).

Therefore, for convenience, we can first add node $1$ to the virtual tree, which does not affect the answer.

### First construction method: sort twice + connect via LCA

Since the LCA of several nodes may be the same node, we must not add it to the virtual tree multiple times.

A very intuitive method is:

-   sort the key nodes by DFS order;
-   traverse once, compute the LCA of every two adjacent key nodes, and remove duplicates;
-   then build the tree according to the ancestor-descendant relationships in the original tree.

In the implementation, on the **sequence of key nodes**, enumerate **every two adjacent elements**, compute their LCA pairwise, and add it to the sequence $A$.

Because of the properties of the DFS order, the sequence $A$ now already contains **all nodes of the virtual tree**, but possibly with duplicates.

So we **sort the sequence $A$ by DFS order in increasing order and remove duplicates**.

Finally, on the sequence $A$, enumerate **adjacent** pairs of **node indices** $x,y$, compute their LCA and connect $\operatorname{LCA}(x,y),y$; the virtual tree is then constructed.

Why does connecting $\operatorname{LCA}(x,y)$ and $y$ neither miss nor duplicate anything?

??? note "Proof"
    If $x$ is an ancestor of $y$, then $x$ is connected directly to $y$. Since the DFS order guarantees that the DFS indices of $x$ and $y$ are adjacent, there is no key node on the path from $x$ to $y$.
    
    If $x$ is not an ancestor of $y$, then treat $\operatorname{LCA}(x,y)$ as an ancestor of $y$; by the previous case it can also be proved that there is no key node on the path from $\operatorname{LCA}(x,y)$ to $y$.
    
    Therefore connecting $\operatorname{LCA}(x,y)$ and $y$ neither misses nor duplicates anything.
    
    Also, does it matter that the first node is not connected to by any node? Since the first node must be the root of this tree, it does not matter, so the total number of edges is $m-1$.

Since at least two real nodes are needed to "summon" one virtual node, plus one root node, the number of nodes of the virtual tree is at most twice the number of real nodes.

Time complexity $O(m\log n)$, where $m$ is the number of key nodes and $n$ the total number of nodes.

#### Implementation

```cpp
int dfn[MAXN];
int h[MAXN], m, a[MAXN], len;  // stores the key nodes

bool cmp(int x, int y) {
  return dfn[x] < dfn[y];  // sort by dfs order
}

void build_virtual_tree() {
  sort(h + 1, h + m + 1, cmp);  // sort the key nodes by dfs order
  for (int i = 1; i < m; ++i) {
    a[++len] = h[i];
    a[++len] = lca(h[i], h[i + 1]);  // insert the lca
  }
  a[++len] = h[m];
  sort(a + 1, a + len + 1, cmp);  // sort all nodes of the virtual tree by dfs order
  len = unique(a + 1, a + len + 1) - a - 1;  // remove duplicates
  for (int i = 1, lc; i < len; ++i) {
    lc = lca(a[i], a[i + 1]);
    conn(lc, a[i + 1]);  // add the edge; if there are edge weights, it is distance(lc,a[i+1])
  }
}
```

This is actually enough to construct a virtual tree.

### Second construction method: using a monotonic stack

How to construct a virtual tree with a monotonic stack?

First we need to clarify a goal: we use the monotonic stack to maintain a chain of the virtual tree.

That is, two adjacent nodes in the stack are also adjacent in the virtual tree, and the stack is monotonically increasing from bottom to top (meaning the DFS indices of the nodes in the stack increase monotonically); simply put, the parent of a node is the node below it in the stack.

First we add node $1$ to the stack.

Then we add the key nodes in increasing DFS order.

If the LCA of the current node and the top of the stack is the top of the stack itself, then they are on the same chain. So we simply push the current node onto the stack.

![vtree-7](./images/vtree-add1.svg)

If the LCA of the current node and the top of the stack is not the top of the stack:

![vtree-8](./images/vtree-add2.svg)

At this moment, the chain maintained by the monotonic stack is:

![vtree-9](./images/vtree-add3.svg)

and we need to turn the chain into:

![vtree-10](./images/vtree-add4.svg)

So we just pop the nodes marked with dashed lines from the stack; before popping, do not forget to add the edge to their parent in the virtual tree.

![vtree-11](./images/vtree-add5.svg)

If after popping the top of the stack is not the LCA, push the LCA onto the stack.

Then push the current node onto the stack.

A concrete example follows. Suppose we want to build a virtual tree for nodes 4, 6 and 7 of the following tree:

![vtree-12](./images/vtree-construction1.svg)

Then the steps are as follows:

-   Sort the 3 key nodes $6,4,7$ by DFS order, obtaining the sequence $[4,6,7]$.
-   Push $1$ onto the stack.

![vtree-13](./images/vtree-construction2.svg)

We use red nodes to represent nodes in the stack, and cyan nodes to represent nodes popped from the stack.

-   Take the first element of the sequence as the current node, namely $4$. Take the top of the stack, which is $1$. Compute the LCA of $1$ and $4$: $LCA(1,4)=1$.
-   We find $LCA(1,4)=$ the top of the stack, which means they are on one chain of the virtual tree, so we directly push the current node $4$ onto the stack; the stack is now $4,1$.

![vtree-14](./images/vtree-construction3.svg)

-   Take the second element of the sequence as the current node, $6$. Take the top of the stack, $4$. Compute the LCA of $6$ and $4$: $LCA(6,4)=1$.
-   We find $LCA(6,4)\neq$ the top of the stack, so we enter the checking phase.
-   Checking phase: the DFS index of the top node $4$ is greater than $LCA(6,4)$, but the DFS index of the second node (the one below the top) $1$ equals the LCA (equal DFS indices actually mean equal nodes), which means the LCA is already in the stack, so we directly add the edge $1\to4$, i.e. the edge from the LCA to the top of the stack. And pop $4$ from the stack.

![vtree-15](./images/vtree-construction4.svg)

-   After the checking phase, push $6$ onto the stack; the stack is now $6,1$.

![vtree-16](./images/vtree-construction5.svg)

-   Take the third element of the sequence as the current node, $7$. Take the top of the stack, $6$. Compute the LCA of $7$ and $6$: $LCA(7,6)=3$.
-   We find $LCA(7,6)\neq$ the top of the stack, so we enter the checking phase.
-   Checking phase: the DFS index of the top node $6$ is greater than $LCA(7,6)$, but the DFS index of the second node (the one below the top) $1$ is less than the LCA, which means the LCA has never been in the stack, so we directly add the edge $3\to6$, i.e. the edge from the LCA to the top of the stack. Pop $6$ from the stack and push $LCA(6,7)$ onto the stack.
-   After the checking phase, push $7$ onto the stack; the stack is now $1,3,7$.

![vtree-17](./images/vtree-construction6.svg)

-   All 3 nodes of the sequence have been pushed onto the stack, so we exit the loop.
-   There are still 3 nodes in the stack: $1,3,7$; they are obviously on one chain, so we directly add the edges $1\to3$ and $3\to7$.
-   The virtual tree is built!

![vtree-18](./images/vtree-construction7.svg)

Next, if we delete the nodes that were never in the stack (the non-cyan nodes), the corresponding virtual tree looks like this:

![vtree-19](./images/vtree-construction8.svg)

There are many details; for example, if the virtual tree is stored with adjacency lists, the adjacency lists need to be cleared. But clearing the whole adjacency list directly is very slow, so we **clear the adjacency list of an element at the moment an element that has never been in the stack is pushed**.

The time complexity is again $O(m\log n)$ (because of the sorting), where $m$ is the number of key nodes and $n$ the total number of nodes.

#### Implementation

The C++ code for building the virtual tree looks roughly like this:

???+ note "Implementation"
    ```cpp
    bool cmp(const int x, const int y) { return id[x] < id[y]; }
    
    void build() {
      sort(h + 1, h + k + 1, cmp);
      sta[top = 1] = 1, g.sz = 0, g.head[1] = -1;
      // push node 1, clear the adjacency list of node 1, set the edge count of the adjacency list to 0
      for (int i = 1, l; i <= k; ++i)
        if (h[i] != 1) {
          // if node 1 is a key node, do not add it again
          l = lca(h[i], sta[top]);
          // compute the LCA of the current node and the top of the stack
          if (l != sta[top]) {
            // if the LCA differs from the top of the stack, the current node is not on the chain currently stored in the stack
            while (id[l] < id[sta[top - 1]])
              // while the Dfs index of the second node is greater than the Dfs index of the LCA
              g.push(sta[top - 1], sta[top]), top--;
            // connect and pop the chain that does not overlap with the chain of the current node
            if (id[l] > id[sta[top - 1]])
              // if the LCA is not equal to the second node (here "greater than" is no different from "not equal")
              g.head[l] = -1, g.push(l, sta[top]), sta[top] = l;
            // the LCA is pushed for the first time: clear its adjacency list, add the edge, pop the top and push the LCA
            // onto the stack
            else
              g.push(l, sta[top--]);
            // the LCA is exactly the second node, just pop the top of the stack
          }
          g.head[h[i]] = -1, sta[++top] = h[i];
          // the current node is certainly pushed for the first time: clear its adjacency list and push it
        }
      for (int i = 1; i < top; ++i)
        g.push(sta[i], sta[i + 1]);  // connect the remaining last chain
      return;
    }
    ```

And so we have learned how to build a virtual tree!

For the problem War of Attrition, just run the DP described at the beginning on the virtual tree; we have effectively used the virtual tree to exclude the useless non-key nodes! Still consider all children $v$ of $i$:

-   if $v$ is not a key node: $Dp(i)=Dp(i) + \min \{Dp(v),w(i,v)\}$
-   if $v$ is a key node: $Dp(i)=Dp(i) + w(i,v)$

And so this problem is easily solved.

## Recommended exercises

-   ["SDOI2011" War of Attrition](https://www.luogu.com.cn/problem/P2495)
-   ["HEOI2014" Big Project](https://www.luogu.com.cn/problem/P4103)
-   [CF613D Kingdom and its Cities](http://codeforces.com/contest/613/problem/D/)
-   ["HNOI2014" World Tree](https://www.luogu.com.cn/problem/P3233)
