---
title: Suffix balanced tree
---

## Definition

The order among suffixes is defined by lexicographic order, and a suffix balanced tree is a balanced tree that maintains this order of the suffixes; in other words, the suffix balanced tree of a string $T$ is the ordered set of all suffixes of $T$. A node of the suffix balanced tree corresponds to one suffix of the original string.

In particular, the inorder traversal of the suffix balanced tree is exactly the suffix array.

## Construction

To build the suffix balanced tree of a string $T$ of length $n$, we add its suffixes to the suffix balanced tree in reverse order.

Denote the set maintained by the suffix balanced tree by $X$ and the suffix added so far by $S$; adding the next suffix then means adding $\texttt{c}S$ to $X$ (this can also be understood as follows: the suffix balanced tree maintains the string $S$, and in the next step we prepend a character $\texttt{c}$ to $S$). This operation is really just inserting a node into the balanced tree.

Here we use a balanced tree whose expected height is $O(\log n)$, e.g. a scapegoat tree or a treap.

### Approach 1

When inserting, we compare two suffixes by brute force and thereby decide which subtree to continue into. This way a single insertion performs at most $O(\log n)$ comparisons, and a single comparison takes at most $O(n)$ time, for a total of $O(n\log n)$.

There are $n$ insertions in total, so the time complexity of this approach has the upper bound $O(n^2 \log n)$.

### Approach 2

Note that $\texttt{c}S$ and $S$ differ only in $\texttt{c}$, and $S$ already belongs to $X$; we can use this to speed up the insertion.

Suppose we currently compare the strings $\texttt{c}S$ and $A$, where $A, S \in X$. In every comparison we first compare the first characters of both strings. If the first characters differ, the order of the two strings is already determined; if the first characters are equal, we only need to determine the order of the two strings with the first character removed. Both strings without their first character already belong to $X$, so the remaining comparison can be done with the balanced tree's rank query in $O(\log n)$. This way a single insertion takes at most $O(\log^2 n)$.

There are $n$ insertions in total, so the time complexity of this approach has the upper bound $O(n \log^2 n)$.

### Approach 3

Following approach 2, if we could determine the order of two nodes of the balanced tree in $O(1)$, we could build the suffix balanced tree in $O(n \log n)$ time.

Let $val_i$ denote the value of node $i$. If, while building the balanced tree, we maintain an additional tag $tag_i$ in every node such that $tag_i > tag_j \iff val_i > val_j$, then the order of two nodes of the balanced tree can be determined in $O(1)$ by comparing $tag_i$.

Let us assign a real interval to every node of the balanced tree, with the root getting $(0, 1)$. For node $i$, denote its real interval by $(l, r)$; then $tag_i = \frac{l + r}{2}$, its left subtree gets the real interval $(l, tag_i)$, and its right subtree gets the real interval $(tag_i, r)$. It is easy to prove that $tag_i$ satisfies the requirement above.

Since we use a balanced tree with expected height $O(\log n)$, the precision is guaranteed to some extent. In practice one can also use a larger interval, e.g. let the root correspond to $(0, 10^{18})$.

### Approach 4

In fact, we can first build the suffix array and then build the suffix balanced tree from the suffix array. The complexity bottleneck of this approach is the complexity of building the suffix array, or the complexity of inserting $n$ elements at once into the chosen balanced tree.

## Deletion

Suppose the suffix added so far is $\texttt{c}S$ and the previously added suffix is $S$. The suffix balanced tree also supports deleting the suffix $\texttt{c}S$ (this can also be understood as follows: the suffix balanced tree maintains the string $\texttt{c}S$, and we delete the leading $\texttt{c}$).

Similarly to insertion, deleting $\texttt{c}S$ is done with the balanced tree's node deletion operation.

## Advantages of the suffix balanced tree

-   The idea of the suffix balanced tree is fairly clear; it is easier to understand than the suffix automaton and other suffix structures, and anyone who can write a balanced tree can write it.
-   The complexity of the suffix balanced tree does not depend on the alphabet size.
-   The suffix balanced tree supports deleting a character at the beginning of the string.
-   If a balanced tree that supports persistence is used, the suffix balanced tree can be made persistent as well.

## Example problems

### [P3809 [Template] Suffix sorting](https://www.luogu.com.cn/problem/P3809)

A template problem for the suffix array: after building the suffix balanced tree, we obtain the suffix array by an inorder traversal.

??? note "Sample code (scapegoat tree version)"
    ```cpp
    --8<-- "docs/string/code/suffix-bst/suffix-bst_1.cpp"
    ```

### [P6164 [Template] Suffix balanced tree](https://www.luogu.com.cn/problem/P6164)

???+ note "Problem statement"
    Given an initial string $s$ and $q$ operations:
    
    1.  Append several characters to the end of the current string.
    2.  Delete several characters from the end of the current string.
    3.  Query: how many times does the string $t$ occur as a contiguous substring of the current string?
    
    The problem is **forced online**; the total change in length of the string and the initial length are $\le 8 \times 10^5$, $q \le 10^5$, and the total length of the queries is $\le 3 \times 10^6$.

For operations 1 and 2: since the suffix balanced tree conveniently maintains insertion and deletion at the front, the idea is to turn insertion and deletion at the back into insertion and deletion at the front. If, instead of the suffix balanced tree of $s$, we maintain the suffix balanced tree of the reverse of $s$, we achieve exactly this transformation. Insertion and deletion in the balanced tree are both $O(\log n)$, so adding or deleting one character takes $O(\log n)$ time. If the total number of added and deleted characters is $N$, the total time complexity of this part is $O(N \log n)$.

For operation 3: the number of occurrences of $t$ equals the number of suffixes having $t$ as a prefix, and the number of suffixes having $t$ as a prefix equals the rank of its successor minus the rank of its predecessor. Appending a very large character to $t$ yields a successor of $t$. Decreasing the last character of $t$ by 1 yields a predecessor of $t$.

Now we need to query the rank of some string $t$ in the suffix balanced tree; since we cannot guarantee that $t$ appears in the suffix balanced tree, each time we can only compare the strings by brute force. A single comparison takes $O(|t|)$ time, and each query performs at most $O(\log n)$ comparisons, so the complexity of a single query is $O(|t|\log n)$. If the sum of the lengths of all query strings is $L$, the total time complexity of this part is $O(L \log n)$.

??? note "Sample code (scapegoat tree version)"
    ```cpp
    --8<-- "docs/string/code/suffix-bst/suffix-bst_2.cpp"
    ```

## References

-   Chen Lijie – "Applications of weight-balanced trees and suffix balanced trees in informatics olympiads" (陈立杰 -《重量平衡树和后缀平衡树在信息学奥赛中的应用》)
