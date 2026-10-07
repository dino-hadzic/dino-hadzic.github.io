---
title: Disjoint set union
---

![](images/disjoint-set.svg)

## Introduction

A disjoint set union (DSU, also called union-find) is a data structure for managing which set each element belongs to. It is implemented as a forest in which every tree represents a set and the nodes of a tree represent the elements of the corresponding set.

As the name suggests, a DSU supports two operations:

-   Unite: merge the sets containing two elements (merge the corresponding trees).
-   Find: determine which set an element belongs to (find the root of the corresponding tree); this can be used to check whether two elements belong to the same set.

With suitable modifications a DSU can support deleting or moving a single element, or maintaining edge weights in the tree. Using a dynamically allocated segment tree one can also implement a [persistent DSU](./persistent-seg.md#拓展基于主席树的可持久化并查集).

???+ warning "Warning"
    A DSU cannot split sets apart with low complexity.

## Initialization

Initially every element is in its own set, represented as a tree consisting only of a root. For convenience we set the parent of a root to itself.

???+ example "Implementation"
    === "C++"
        ```cpp
        struct dsu {
          vector<size_t> pa;
        
          explicit dsu(size_t size) : pa(size) { iota(pa.begin(), pa.end(), 0); }
        };
        ```
    
    === "Python"
        ```python
        class Dsu:
            def __init__(self, size):
                self.pa = list(range(size))
        ```

## Find

We move up the tree until we reach the root.

![](images/disjoint-set-find.svg)

???+ example "Implementation"
    === "C++"
        ```cpp
        size_t dsu::find(size_t x) { return pa[x] == x ? x : find(pa[x]); }
        ```
    
    === "Python"
        ```python
        def find(self, x):
            return x if self.pa[x] == x else self.find(self.pa[x])
        ```

### Path compression

Every element visited during a find belongs to that set, so we can attach it directly to the root to speed up later finds.

![](images/disjoint-set-compress.svg)

???+ example "Implementation"
    === "C++"
        ```cpp
        size_t dsu::find(size_t x) { return pa[x] == x ? x : pa[x] = find(pa[x]); }
        ```
    
    === "Python"
        ```python
        def find(self, x):
            if self.pa[x] != x:
                self.pa[x] = self.find(self.pa[x])
            return self.pa[x]
        ```

## Unite

To merge two trees we only need to attach the root of one tree to the root of the other.

![](images/disjoint-set-merge.svg)

???+ example "Implementation"
    === "C++"
        ```cpp
        void dsu::unite(size_t x, size_t y) { pa[find(x)] = find(y); }
        ```
    
    === "Python"
        ```python
        def unite(self, x, y):
            self.pa[self.find(x)] = self.find(y)
        ```

### Union by rank/size (heuristic merging)

When merging, the choice of which root becomes the root of the new tree affects the complexity of future operations. We can attach the tree with fewer nodes or smaller depth to the other one to avoid degeneration.

??? note "Detailed complexity discussion"
    Since all we need to support are set union and find, when merging two sets into one we get a correct result no matter which set is attached below the other. Different ways of attaching do, however, differ in time complexity. Specifically, if we attach a set tree with fewer nodes and smaller depth under a larger set tree, subsequent find operations clearly take less time than with the other way of attaching (and this also gives a better worst-case time complexity).
    
    Of course, we do not always meet sets that are exactly as described above -- smaller in both node count and depth. Since both node count and depth are easy to maintain, we usually pick one of them as the estimation function. Whichever is chosen, the time complexity is $O (m\alpha(m,n))$; for the detailed proof see the papers cited in the references.
    
    In actual contest code, even without heuristic merging the code often finishes within the time limit. Tarjan's paper[^tarjan1984worst] proved that with only path compression and no heuristic merging the worst-case time complexity is $O (m \log n)$. Andrew Yao's paper[^yao1985expected] proved that with only path compression and no heuristic merging, the average time complexity is still $O (m\alpha(m,n))$.
    
    If only heuristic merging is used without path compression, the time complexity is $O(m\log n)$. Since a single path compression may cause a large number of modifications, path compression is sometimes unsuitable. For example, in persistent DSUs and in "segment tree divide and conquer over time + DSU", a DSU with heuristic merging only is normally used.

Reference implementation of union by size (note that the initialization has to be adjusted):

???+ example "Implementation"
    === "C++"
        ```cpp
        struct dsu {
          vector<size_t> pa, size;
        
          explicit dsu(size_t size_) : pa(size_), size(size_, 1) {
            iota(pa.begin(), pa.end(), 0);
          }
        
          void unite(size_t x, size_t y) {
            x = find(x), y = find(y);
            if (x == y) return;
            if (size[x] < size[y]) swap(x, y);
            pa[y] = x;
            size[x] += size[y];
          }
        };
        ```
    
    === "Python"
        ```python
        class Dsu:
            def __init__(self, size):
                self.pa = list(range(size))
                self.size = [1] * size
        
            def unite(self, x, y):
                x, y = self.find(x), self.find(y)
                if x == y:
                    return
                if self.size[x] < self.size[y]:
                    x, y = y, x
                self.pa[y] = x
                self.size[x] += self.size[y]
        ```

## Reference implementation

A complete implementation of a DSU with path compression and union by size is shown below:

??? example "Reference implementation for the template problem [Luogu P3367 \"Template\" Disjoint Set Union](https://www.luogu.com.cn/problem/P3367)"
    === "C++"
        ```cpp
        --8<-- "docs/ds/code/dsu/dsu_0.cpp"
        ```
    
    === "Python"
        ```python
        --8<-- "docs/ds/code/dsu/dsu_0.py"
        ```

## Complexity

With both path compression and heuristic merging, the average time of each DSU operation is only $O(\alpha(n))$. Here $\alpha$ is the inverse of the Ackermann function, which grows extremely slowly. In other words, the average running time of a single DSU operation can be regarded as a very small constant. The proof of the time complexity is on [this page](./dsu-complexity.md).

???+ info "Inverse Ackermann function"
    The [Ackermann function](https://en.wikipedia.org/wiki/Ackermann_function) $A(m, n)$ is defined as follows:
    
    $A(m, n) = \begin{cases}n+1&\text{if }m=0\\A(m-1,1)&\text{if }m>0\text{ and }n=0\\A(m-1,A(m,n-1))&\text{otherwise}\end{cases}$
    
    The inverse Ackermann function $\alpha(n)$ is defined as the inverse of the Ackermann function, i.e. the largest integer $m$ such that $A(m, m) \leqslant n$.

The space complexity of a DSU is obviously $O(n)$.

## Extended operations

On top of the plain DSU, a series of modifications can be made so that it supports more operations or maintains more complex information.

### DSU with deletion

A plain DSU cannot support deletion because deleting a node would inevitably delete all nodes in the subtree rooted at it. To solve this problem, a DSU with deletion uses virtual nodes to guarantee that all nodes that actually store data are always leaves. To this end, at initialization we create a virtual node for every data node and set the parent of the data node to that virtual node. Since merging two sets only ever connects the two tree roots, from beginning to end only virtual nodes have children. This guarantees that deleting a node never accidentally deletes other nodes.

Note that after deleting a single node, a new virtual node must be created as its parent; otherwise subsequent unite and delete operations cannot be performed correctly.

??? example "Reference implementation for the template problem [SPOJ JMFILTER - Junk-Mail Filter](https://www.spoj.com/problems/JMFILTER/)"
    === "C++"
        ```cpp
        --8<-- "docs/ds/code/dsu/dsu_4.cpp"
        ```
    
    === "Python"
        ```python
        --8<-- "docs/ds/code/dsu/dsu_4.py"
        ```

A similar method can also be used to move a single element between sets. See the example problems for implementation details.

### Weighted DSU

We can also define some weight on the edges of the DSU, together with the operation performed on these weights during path compression, in order to solve more problems. For instance, for the classic "NOI2001" Food Chain we can maintain the additive group modulo $3$ on the edge weights. For problems of this kind, maintaining edge weights modulo a very small modulus, one can also split each node of the DSU into several states. This trick for the special case is also called a "DSU with types" or "extended-domain DSU". These approaches are explained through example problems below.

To maintain edge weights in a DSU, the edge weight is pushed down and stored in the child node. Thus every node stores the weight of the edge between itself and its parent. The weight only needs to be adjusted when the parent of a node changes. In general this may happen during path compression and when merging two nodes. For example, if the edge weight is the distance between the current node and its parent, then during path compression, every time the parent of the current node is replaced by the root, the distance from the parent to the root must be added to the weight stored in the current node; similarly, when merging the sets of two nodes, the weight of the newly created edge between the two roots has to be computed.

??? example "Reference implementation for the template problem [Library Checker - Unionfind with Potential](https://judge.yosupo.jp/problem/unionfind_with_potential)"
    === "C++"
        ```cpp
        --8<-- "docs/ds/code/dsu/dsu_5.cpp"
        ```
    
    === "Python"
        ```python
        --8<-- "docs/ds/code/dsu/dsu_5.py"
        ```

## Example problems

In algorithm contests, most problems that test the DSU directly require a special structure designed for the problem.

???+ example "[UVa11987 Almost Union-Find](https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=229&page=show_problem&problem=3138)"
    Implement a DSU-like data structure supporting the following operations:
    
    1.  merge the sets containing two elements;
    2.  move a single element into the set containing another element;
    3.  query the size and the sum of the elements of the set containing an element.

??? note "Solution"
    In this problem operations 1 and 3 are easy; the difficulty lies in operation 2. Suppose element $x$ is to be moved into the set containing element $y$. In a plain DSU, simply setting the parent of $x$ to the root of the set containing $y$ does not work, because that would move all elements in the subtree of $x$ together with it. The solution is to guarantee that element $x$ has no children. To this end, when building the DSU we create a virtual node $\tilde x$ for every element $x$ and point the parent of $x$ to the corresponding virtual node $\tilde x$. This way, when merging two sets, one tree root is always attached to another tree root, and all tree roots are virtual nodes, so only virtual nodes have children, while none of the nodes that actually store elements have children. Moving an element is then much easier to implement.

??? note "Reference implementation"
    === "C++"
        ```cpp
        --8<-- "docs/ds/code/dsu/dsu_1.cpp"
        ```
    
    === "Python"
        ```python
        --8<-- "docs/ds/code/dsu/dsu_1.py"
        ```

???+ example "[Luogu P2024 \"NOI2011\" Food Chain](https://www.luogu.com.cn/problem/P2024)"
    In the animal kingdom there are three kinds of animals $A,B,C$, whose food chain forms an interesting cycle: $A$ eats $B$, $B$ eats $C$, $C$ eats $A$.
    
    There are $N$ animals, numbered $1 \sim N$. Each animal is one of $A,B,C$, but we do not know which.
    
    Someone describes the food-chain relations among these $N$ animals using two kinds of statements:
    
    -   the first kind is `1 X Y`, meaning $X$ and $Y$ are of the same kind;
    -   the second kind is `2 X Y`, meaning $X$ eats $Y$.
    
    This person makes $K$ statements about the $N$ animals, one after another, using the two kinds above; some of the $K$ statements are true and some are false. A statement is false if it satisfies any one of the following three conditions, and true otherwise:
    
    -   the current statement conflicts with some earlier true statements;
    -   $X$ or $Y$ in the current statement is greater than $N$;
    -   the current statement says that $X$ eats $X$.
    
    Your task is to output the total number of false statements given $N$ and the $K$ statements.

??? note "Solution 1"
    Maintain the food-chain information with a weighted DSU. If $x$ and $y$ are of the same kind, then $x\equiv y\pmod 3$; if $x$ eats $y$, then $x - y \equiv 1 \pmod 3$. This turns the problem into the template problem above.
    
    Specifically, for each statement, apart from the obviously false ones with $x>n$ or $y>n$, we need to check whether $x$ and $y$ are already connected: if so, compute their distance modulo 3 and compare it with what the statement claims; otherwise connect them according to the information in the statement. Apart from the obvious cases, a statement is false if and only if the two nodes mentioned are already connected and the corresponding distance contradicts the statement.

??? note "Reference implementation 1"
    === "C++"
        ```cpp
        --8<-- "docs/ds/code/dsu/dsu_6.cpp"
        ```
    
    === "Python"
        ```python
        --8<-- "docs/ds/code/dsu/dsu_6.py"
        ```

??? note "Solution 2"
    Split each animal $x$ into three states. In the implementation we can simply treat the different states as different elements:
    
    -   states in the same set as $x$ belong to the same species as $x$;
    -   states in the same set as $x+n$ can be eaten by $x$;
    -   states in the same set as $x+2n$ can eat $x$.
    
    Then for a statement:
    
    -   `1 x y` is false if and only if:
    
        1.  $x>N$ or $y>N$;
        2.  $y$ is in the same set as $x+n$ or $x+2n$.
    -   `2 x y` is false if and only if:
    
        1.  $x>N$ or $y>N$;
        2.  $y$ is in the same set as $x$ or $x+2n$.
    -   If the statement is true, merge the corresponding states.

??? note "Reference implementation 2"
    === "C++"
        ```cpp
        --8<-- "docs/ds/code/dsu/dsu_2.cpp"
        ```
    
    === "Python"
        ```python
        --8<-- "docs/ds/code/dsu/dsu_2.py"
        ```

???+ example "[ABC396E Min of Restricted Sum](https://atcoder.jp/contests/abc396/tasks/abc396_e)"
    You are given integers $N, M$ and integer sequences of length $M$: $X=(X_1,X_2,\ldots,X_M)$, $Y=(Y_1,Y_2,\ldots,Y_M)$, $Z=(Z_1,Z_2,\ldots,Z_M)$. It is guaranteed that all elements of $X$ and $Y$ are in the range $1$ to $N$.
    
    A sequence of non-negative integers $A=(A_1,A_2,\ldots,A_N)$ of length $N$ is called a **good integer sequence** if and only if it satisfies the following condition:
    
    -   for every integer $i$ with $1 \leq i \leq M$, $A_{X_i} \oplus A_{Y_i} = Z_i$, where $\oplus$ denotes the XOR operation.
    
    Determine whether such a good integer sequence exists. If it does, find the good integer sequence minimizing the sum of elements $\displaystyle \sum_{i=1}^N A_i$ and output it.

??? note "Solution"
    XOR is just a "same" or "different" relation on a single binary bit. So if we separate all the binary bits of the $A_i$, the XOR relations can be maintained with a weighted DSU (or a DSU with types). Elements in the same connected component necessarily correspond to the same bit of different numbers in $A$. When computing the answer, the elements of a component are generally divided into two groups whose values must differ; assigning $0$ to the larger group and $1$ to the other guarantees the minimum total weight.

??? note "Reference implementation"
    === "C++"
        ```cpp
        --8<-- "docs/ds/code/dsu/dsu_3.cpp"
        ```
    
    === "Python"
        ```python
        --8<-- "docs/ds/code/dsu/dsu_3.py"
        ```

## Exercises

-   ["NOI2015" Automatic Program Analysis](https://uoj.ac/problem/127)
-   ["JSOI2008" Star Wars](https://www.luogu.com.cn/problem/P1197)
-   ["NOIP2023" Three-Valued Logic](https://www.luogu.com.cn/problem/P9869)
-   ["NOI2002" Legend of the Galactic Heroes](https://www.luogu.com.cn/problem/P1196)

## Other applications

Kruskal's algorithm in [minimum spanning tree algorithms](../graph/mst.md) and Tarjan's algorithm for the [lowest common ancestor](../graph/lca.md) are algorithms based on the DSU.

For the related topic see [applications of DSU](../topic/dsu-app.md).

## References and further reading

1.  [Zhihu answer: Is there really a path-halving optimization in the DSU?](https://www.zhihu.com/question/28410263/answer/40966441)
2.  Gabow, H. N., & Tarjan, R. E. (1985). A Linear-Time Algorithm for a Special Case of Disjoint Set Union. JOURNAL OF COMPUTER AND SYSTEM SCIENCES, 30, 209-221.[PDF](https://dl.acm.org/doi/pdf/10.1145/800061.808753)
3.  [CSDN: Extended-domain DSU & weighted DSU](https://blog.csdn.net/qqqqqwerttwtwe/article/details/145440100)

[^tarjan1984worst]: Tarjan, R. E., & Van Leeuwen, J. (1984). Worst-case analysis of set union algorithms. Journal of the ACM (JACM), 31(2), 245-281.[ResearchGate PDF](https://www.researchgate.net/profile/Jan_Van_Leeuwen2/publication/220430653_Worst-case_Analysis_of_Set_Union_Algorithms/links/0a85e53cd28bfdf5eb000000/Worst-case-Analysis-of-Set-Union-Algorithms.pdf)

[^yao1985expected]: Yao, A. C. (1985). On the expected performance of path compression algorithms.[SIAM Journal on Computing, 14(1), 129-133.](https://epubs.siam.org/doi/abs/10.1137/0214010?journalCode=smjcat)
