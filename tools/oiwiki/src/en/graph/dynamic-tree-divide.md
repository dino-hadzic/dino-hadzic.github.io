---
title: Dynamic centroid decomposition
---

## Dynamic centroid decomposition

Dynamic centroid decomposition is used for counting path information on a tree **with modifications of vertex or edge weights**.

### Centroid tree

Let us recall how centroid decomposition works.

For a vertex $x$, the simple paths in its subtree are of two kinds: those passing through $x$, consisting of one or two paths starting at $x$; and those not passing through $x$, i.e. those already contained in the subtrees of its children.

To compute the simple paths inside a subtree, we pick a decomposition center $rt$, compute the information about the paths of the subtree passing through this vertex, and then, for each of its children, treat the connected component containing that child after removing $rt$ as a subtree and recurse. The chosen decomposition centers form a tree structure called the **centroid tree**. Observe that the total size of the components represented by the vertices on the same level of the centroid tree (i.e. the components whose decomposition center is that vertex) is $O(n)$. This means the time complexity of centroid decomposition depends on the depth of the centroid tree: if the depth is $h$, the complexity is $O(nh)$.

It can be proven that the depth of the centroid tree is minimal, $O(\log n)$, when we always pick the centroid of the component as the decomposition center. This lets us collect information about the $O(n^2)$ paths of the tree in $O(n\log n)$ time.

Since the shape of the tree does not change during dynamic centroid decomposition, the shape of the centroid tree does not change either.

Reference code for building the centroid tree:

```cpp
void calcsiz(int x, int f) {
  siz[x] = 1;
  maxx[x] = 0;
  for (int j = h[x]; j; j = nxt[j])
    if (p[j] != f && !vis[p[j]]) {
      calcsiz(p[j], x);
      siz[x] += siz[p[j]];
      maxx[x] = max(maxx[x], siz[p[j]]);
    }
  maxx[x] =
      max(maxx[x], sum - siz[x]);  // maxx[x] is the size of the largest subtree when x is the root
  if (maxx[x] < maxx[rt])
    rt = x;  // must not be <= here, so that rt does not change in the second calcsiz
}

void pre(int x) {
  vis[x] = true;  // the vertex x is no longer considered from now on
  for (int j = h[x]; j; j = nxt[j])
    if (!vis[p[j]]) {
      sum = siz[p[j]];
      rt = 0;
      maxx[rt] = inf;
      calcsiz(p[j], -1);
      calcsiz(rt, -1);  // computed twice; the second pass gives the subtree sizes with rt as the root
      fa[rt] = x;
      pre(rt);  // record the parent in the centroid tree
    }
}

int main() {
  sum = n;
  rt = 0;
  maxx[rt] = inf;
  calcsiz(1, -1);
  calcsiz(rt, -1);
  pre(rt);
}
```

### Performing modifications

For queries and modifications we simply walk up the parents in the centroid tree and update. Since the depth of the centroid tree is at most $O(\log n)$, the complexity is guaranteed.

During dynamic centroid decomposition we need the distances from a vertex to its ancestors in the centroid tree and similar information. Since a vertex has at most $O(\log n)$ ancestors, we can additionally compute the depth $dep[x]$ while building the centroid tree, or use LCA, to precompute these distances or query them on the fly. **Note**: the distances from a vertex to its ancestors in the centroid tree are not necessarily increasing and must not be accumulated!

During dynamic centroid decomposition the information of a vertex may be counted several times in its centroid-tree ancestors, so we need to cancel the effect of the duplicates. The usual approach is to keep two kinds of records for each component: the distances to the decomposition center, and the distances to the parent of that center in the centroid tree. This is shown in the examples.

??? note "Example [“ZJOI2007” 捉迷藏](https://www.luogu.com.cn/problem/P2056)"
    Given a tree with $n$ vertices, all initially black, support two operations:
    
    1.  flip the color of a vertex (white to black, black to white);
    2.  report the distance between the two farthest black vertices of the tree.
    
        $n\le 10^5,m\le 5\times 10^5$

Build the centroid tree and keep two **deletable heaps** for every vertex $x$. $dist[x]$ stores the distances to $x$ of all black vertices in the component represented by $x$; $ch[x]$ stores the distances to $x$ of the black vertices in all children of $x$ in the centroid tree and in $x$ itself. Because of the greedy way the answer is computed in this problem, and because two paths from the same subtree cannot form a complete path, we insert into this heap only the value of the vertex itself and the maximum of each subtree. Observe that the sum of the two largest values in $ch[x]$ (or of all values if there are fewer than two) is the length of the longest path with black endpoints passing through $x$ when $x$ is the decomposition center. We store the answers of all vertices in a deletable heap $ans$; the maximum of this heap is the required answer.

We maintain the deletable heaps $dist[x],ch[x],ans$ according to the definitions above. When a value in $dist[x]$ changes, we can also update $ch[x]$ and $ans$ in $O(\log n)$.

Now let us see how $dist[x]$ changes when we flip the color of a vertex. If the vertex was black, we perform a deletion; if it was white, we perform an insertion.

Suppose we flip the color of vertex $x$. For each of its ancestors $u$ we insert into or delete from $dist[u]$ the value $dist(x,u)$, maintaining $ch[x]$ and $ans$ at the same time. In particular, we insert into or delete from $ch[x]$ the value $0$.

Reference code:

```cpp
--8<-- "docs/graph/code/dynamic-tree-divide/dynamic-tree-divide_1.cpp"
```

???+ note "Example [Luogu P6329【模板】点分树 | 震波](https://www.luogu.com.cn/problem/P6329)"
    Given a tree with $n$ vertices where every vertex $x$ has a weight $v[x]$, support two operations:
    
    1.  query the sum of the weights of the vertices at distance at most $y$ from vertex $x$;
    2.  set the weight of vertex $x$ to $y$, i.e. $v[x]=y$.

We store the distance information in dynamically allocated segment trees indexed by value.

Similarly to the previous problem, for every vertex we maintain a segment tree $dist[x]$ storing the distances of all vertices in component $x$ to vertex $x$: the index is the distance and the value is increased by the vertex weight. The segment tree $ch[x]$ stores the distances of all vertices in component $x$ to the parent of $x$ in the centroid tree.

In this problem all queries and modifications have to be carried out on all ancestors in the centroid tree.

Take a query as an example. To find the sum of weights of the vertices at distance at most $y$ from $x$, we first add to the answer the sum of the values in $dist[x]$ with indices from $0$ to $y$. Then we traverse all ancestors $u$ of $x$; let $v$ be the ancestor one level below $u$, and let $d=dist(x,u)$. If we do not enter the subtree containing $x$, i.e. the subtree rooted at $v$, we add to the answer the sum of the values in $dist[u]$ with indices from $0$ to $y-d$. Since we have counted the part rooted at $v$ twice, we subtract from the answer the sum of the values in $ch[v]$ with indices from $0$ to $y-d$.

For a modification we update $dist[x]$ and $ch[x]$ at the same time.

Reference code:

```cpp
--8<-- "docs/graph/code/dynamic-tree-divide/dynamic-tree-divide_2.cpp"
```
