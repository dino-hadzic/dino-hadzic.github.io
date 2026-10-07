---
title: Tree hashing
---

When checking whether some trees are isomorphic, we often convert the trees into hash values and store those, in order to reduce the complexity.

Tree hashing is very flexible and all kinds of hashing schemes can be designed; but a scheme designed carelessly is quite likely to be wrong and can be broken by adversarial tests. Below we present a class of methods that are easy to implement and hard to break.

## Method

These methods need a hash function for multisets. The hash value of the subtree rooted at a vertex is the hash value of the multiset of hash values of the subtrees rooted at all its children, i.e.:

$$
h_x = f(\{ h_i \mid i \in son(x) \})
$$

where $h_x$ is the hash value of the subtree rooted at $x$ and $f$ is the multiset hash function.

Take the hash function used in the code as an example:

$$
f(S) = \left( c + \sum_{x \in S} g(x) \right) \bmod m
$$

where $c$ is a constant, usually $1$ is fine. $m$ is the modulus; usually $2^{32}$ or $2^{64}$ with natural overflow is used, but a large prime also works. $g$ is a mapping from integers to integers; the code uses xor shift, but other functions can be chosen, although polynomials are not recommended. To guard against a problem setter deliberately breaking the xor hash, one can also XOR a random constant before and after the mapping.

This hash is very easy to write. If rerooting is needed, in the second DP pass it suffices to subtract the hash of the subtree.

## Examples

### [UOJ #763. 树哈希](https://uoj.ac/problem/763)

This is a template problem. Not much to say: run one DFS with $1$ as the root and you are done.

??? note "Reference code"
    ```cpp
    --8<-- "docs/graph/code/tree-hash/tree-hash_1.cpp"
    ```

### [\[BJOI2015\] 树的同构](https://www.luogu.com.cn/problem/P5043)

The isomorphism in this problem is for unrooted trees, while the method described above is for rooted trees. Hence two isomorphic unrooted trees have the same hash value only when their roots coincide. Since the constraints are small, we can compute the hash value with every vertex as the root by brute force, sort them, and compare.

If the constraints are larger, we can use rerooting DP: traverse the tree twice and obtain the hash value with each vertex as the root. We can also use the multiset hash function from above: put the hash values for all roots into a multiset, compute the hash of that multiset, and compare (approach 1).

The complexity can also be improved by finding the centroids. A tree has at most two centroids, so it suffices to compute the hash values with them as roots. Then we can either compare these hash values separately (approach 2), or, when there is one centroid, take its hash value as the hash of the whole tree, and when there are two, take the smaller (or larger) of the two.

??? note "Approach 1"
    ```cpp
    --8<-- "docs/graph/code/tree-hash/tree-hash_2.cpp"
    ```

??? note "Approach 2"
    ```cpp
    --8<-- "docs/graph/code/tree-hash/tree-hash_3.cpp"
    ```

### [HDU 6647 Bracket Sequences on Tree](https://acm.hdu.edu.cn/showproblem.php?pid=6647)

The problem asks for the number of essentially different bracket sequences produced by traversing an unrooted tree.

First note that two non-isomorphic rooted trees never generate the same bracket sequence. Let us first consider the number of essentially different bracket sequences produced by traversing a rooted tree. Let $u$ be the root of the subtree currently considered and let $f(u)$ denote the number of ways for this subtree. Starting from $u$ we traverse downwards in any order, which gives $|son(u)|!$ permutations; for every child $v$, the subtree of $v$ has $f(v)$ ways, so $f(u)=|son(u)|! \cdot \prod_{v \in son(u)} f(v)$. However, isomorphic subtrees produce duplicates, so $f(u)$ has to be divided by the product of the factorials of the numbers of occurrences of each essentially different subtree, similar to permutations of a multiset.

The DP above gives the number of ways for the root. Then, by rerooting DP, we pass the hash value and the counting information from the parent to the child and obtain the hash value and the number of ways with every vertex as the root. Every distinct subtree only needs to be counted once.

??? note "Reference code"
    ```cpp
    --8<-- "docs/graph/code/tree-hash/tree-hash_4.cpp"
    ```

## References

The hashing method in this article is taken and extended from the blog post [一种好写且卡不掉的树哈希](https://peehs-moorhsum.blog.uoj.ac/blog/7891) ("A tree hash that is easy to write and cannot be broken").
