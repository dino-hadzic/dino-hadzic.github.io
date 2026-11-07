---
title: Linear basis
---

Recall the concept of basis vectors from high-school solid geometry: in three-dimensional Euclidean space we can find a set of basis vectors $\boldsymbol{i}$, $\boldsymbol{j}$, $\boldsymbol{k}$, after which every vector in the space can be expressed in terms of these basis vectors. In other words, we can **describe the infinite three-dimensional space using finitely many basis vectors**, which is enough to show the importance of basis vectors.

Three-dimensional Euclidean space is a special [vector space](./vector-space.md), and the basis vectors of three-dimensional Euclidean space are generalized to the linear basis in vector spaces.

Applications of the linear basis in OI generally involve only two kinds of vector spaces: the $n$-dimensional real vector space $\mathbf{R}^n$ and the $n$-dimensional vector space over the [Boolean domain](https://en.wikipedia.org/wiki/Boolean_domain) $\mathbf{Z}_2^n$; we discuss them in detail in the [Applications](#applications) section. If you are not familiar with linear algebra, we recommend starting from the applications part.

Below we introduce the linear basis starting from general vector spaces and give its common properties.

Prerequisites: [vector space](./vector-space.md).

A linear basis is a basis of a vector space and is an important tool for studying vector spaces.

## Definition

A maximal linearly independent subset of a vector space $V$ is called a **Hamel basis** or **linear basis** of $V$, or simply a **basis**.

By convention, the basis of the vector space $\{\theta\}$ is the empty set.

It can be proved that every vector space has a linear basis[^existence_basis]; we define the **dimension** of a vector space $V$ as the number of elements (or cardinality) of a linear basis, denoted $\dim V$.

## Properties

1.  For a finite-dimensional vector space $V$ of dimension $n$:

    1.  Any $n+1$ vectors in $V$ are linearly dependent.

    2.  Any $n$ linearly independent vectors in $V$ form a basis of $V$.

    3.  If every vector in $V$ can be linearly expressed by the set of vectors $a_1,a_2,\dots,a_n$, then it is a basis of $V$.

        ???+ note "Proof"
            Take any basis $b_1,b_2,\dots,b_n$ of $V$. By assumption, the set of vectors $b_1,b_2,\dots,b_n$ can be linearly expressed by $a_1,a_2,\dots,a_n$, so
            
            $$
            n=\operatorname{rank}\{b_1,b_2,\dots,b_n\}\leq\operatorname{rank}\{a_1,a_2,\dots,a_n\}\leq n
            $$
            
            Therefore $\operatorname{rank}\{a_1,a_2,\dots,a_n\}=n$

    4.  Any linearly independent set of vectors $a_1,a_2,\dots,a_m$ in $V$ can be extended to a basis of $V$ by inserting some vectors.

2.  (Dimension formula for subspaces) Let $V_1,V_2$ be finite-dimensional vector spaces over $\Bbb{P}$ such that $V_1+V_2$ and $V_1\cap V_2$ are also finite-dimensional. Then $\dim V_1+\dim V_2=\dim(V_1+V_2)+\dim(V_1\cap V_2)$

    ???+ note "Proof"
        Let $\dim V_1=n_1$, $\dim V_2=n_2$, $\dim(V_1\cap V_2)=m$.
        
        Take a basis $a_1,a_2,\dots,a_m$ of $V_1\cap V_2$ and extend it to bases of $V_1$ and $V_2$ respectively: $a_1,a_2,\dots,a_m,b_1,b_2,\dots,b_{n_1-m}$ and $a_1,a_2,\dots,a_m,c_1,c_2,\dots,c_{n_2-m}$.
        
        It remains only to prove that the set of vectors $a_1,a_2,\dots,a_m,b_1,b_2,\dots,b_{n_1-m},c_1,c_2,\dots,c_{n_2-m}$ is linearly independent.
        
        Suppose $\sum_{i=1}^m r_ia_i+\sum_{i=1}^{n_1-m} s_ib_i+\sum_{i=1}^{n_2-m} t_ic_i=\theta$.
        
        Then $\sum_{i=1}^{n_2-m} t_ic_i=-\sum_{i=1}^m r_ia_i-\sum_{i=1}^{n_1-m} s_ib_i$.
        
        Note that the left-hand side is in $V_2$ and the right-hand side is in $V_1$, so both sides are in $V_1\cap V_2$; hence $\sum_{i=1}^{n_2-m} t_ic_i=\sum_{i=1}^m k_ia_i$
        
        Thus $t_1=t_2=\dots=t_{n_2-m}=k_1=k_2=\dots=k_m=0$, and consequently $r_1=r_2=\dots=r_m=s_1=s_2=\dots=s_{n_1-m}=t_1=t_2=\dots=t_{n_2-m}=0$

3.  Let $V_1,V_2$ be finite-dimensional vector spaces over $\Bbb{P}$ such that $V_1+V_2$ and $V_1\cap V_2$ are also finite-dimensional. Then the following statements are equivalent:

    1.  $V_1+V_2=V_1\oplus V_2$.

    2.  $\dim V_1+\dim V_2=\dim(V_1+V_2)$.

    3.  If $a_1,a_2,\dots,a_n$ is a basis of $V_1$ and $b_1,b_2,\dots,b_m$ is a basis of $V_2$, then $a_1,a_2,\dots,a_n,b_1,b_2,\dots,b_m$ is a basis of $V_1+V_2$.

    ???+ note "Note"
        Statements 1 and 3 can be generalized to infinite-dimensional vector spaces.

## Examples

Consider bases of $\Bbb{R}^2$.

1.  As shown in the figure

    ![](./images/basis-1.svg)

    $u,v$ form a basis.

2.  As shown in the figure

    ![](./images/basis-2.svg)

    $u,v$ form a basis.

3.  As shown in the figure

    ![](./images/basis-3.svg)

    $u,v$ do not form a basis, because $u=-v$.

4.  As shown in the figure

    ![](./images/basis-4.svg)

    $u,v,w$ do not form a basis, because $u+4v+6w=\theta$.

## Orthogonal and orthonormal bases

If a basis $B$ of a vector space $V$ satisfies $\forall b,b'\in B,~(b,b')\ne 0\iff b=b'$ (i.e. the vectors are pairwise orthogonal), the basis is called an **orthogonal basis**.

If an orthogonal basis $B$ of a vector space $V$ also satisfies $\forall b\in B,~|b|=\sqrt{(b,b)}=1$, the basis is called an **orthonormal basis**.

Any basis of a finite-dimensional vector space $V$ can be transformed into an orthogonal basis by the [Gram–Schmidt process](https://en.wikipedia.org/wiki/Gram%E2%80%93Schmidt_process).

## Applications

Based on the above, we can use a linear basis to:

1.  find the rank of a given set of vectors;
2.  for a given set of vectors, find a maximal linearly independent subset (or a basis of the vector space it spans);
3.  insert some vectors into a given set of vectors and find a maximal linearly independent subset (or a basis of the vector space it spans) of the set after the insertions;
4.  for a maximal linearly independent subset (or basis) that has been found, determine whether a given vector can be linearly expressed by it;
5.  for a maximal linearly independent subset (or basis) that has been found, find special elements of the vector space it spans (such as the maximum element, the minimum element, etc.).

In OI, a linear basis in the $n$-dimensional real vector space $\mathbf{R}^n$ is usually called a **real linear basis**, and a linear basis in the $n$-dimensional vector space over the Boolean domain $\mathbf{Z}_2^n$ is called an **XOR linear basis**.

???+ tip "Tip"
    In $\mathbf{Z}_2$, addition is XOR and multiplication is AND; it can be proved that $\mathbf{Z}_2$ is a field.
    
    It can be proved that the algebraic structure $(\mathbf{Z}_2^n,+,\cdot,\mathbf{Z}_2)$ is a vector space, where:
    
    $$
    (a_1,\dots,a_n)+(b_1,\dots,b_n):=(a_1+b_1,\dots,a_n+b_n),
    $$
    
    $$
    k\cdot(a_1,\dots,a_n):=(ka_1,\dots,ka_n).
    $$
    
    That is, addition is XOR and scalar multiplication is AND.

Taking the XOR linear basis as an example, from a given set of Boolean sequences $X=\{x_1,\dots,x_m\}$ we can construct an XOR linear basis $B=\{b_1,\dots,b_n\}$ with the following properties:

1.  The XOR of any nonempty subset of $B$ is not $0$;
2.  For any element $x$ of $X$, some elements of $B$ can be chosen whose XOR equals $x$;
3.  Any set $B'$ satisfying the two properties above has no fewer elements than $B$.

Using an XOR linear basis we can:

1.  determine whether a number can be expressed as the XOR of a subset of a given set of numbers;
2.  count the number of ways a number can be expressed as the XOR of a subset of a given set of numbers;
3.  find the maximum/minimum/$k$-th largest/$k$-th smallest XOR of a subset of a given set of numbers;
4.  find the rank of a number among the subset XORs of a given set of numbers.

### Construction methods

Since there is no essential difference between the XOR linear basis and the real linear basis, we take the XOR linear basis as the example below; the real linear basis version of the code only needs a few simple modifications.

#### Greedy method

Convert each number $p$ of the original set to binary and scan from the highest bit to the lowest. For each bit $x$ that is $1$: if $a_x$ does not exist, set $a_x \leftarrow p$ and end the scan; if it exists, set $p\leftarrow p~\text{xor}~a_x$.

To query the maximum $\text{xor}$ of any number of elements of the original set, just scan the linear basis from the highest bit to the lowest; if $\text{xor}$-ing the answer with the current $a_x$ makes it larger, XOR the answer with $a_x$.

Why does this work? Because when scanning from high bits to low bits, if we are currently at bit $i$, it means we can guarantee that bit $i$ of the answer is $1$, and there is no later chance to change bit $i$.

The minimum $\text{xor}$ of any number of elements of the original set is simply the smallest element of the linear basis set.

Querying whether a number can be obtained as an XOR is similar to insertion: if the number $p$ being inserted is finally XOR-ed down to $0$, then it can be obtained as an XOR.

??? example "Code (Luogu P3812 [【模板】线性基 (Template: linear basis)](https://www.luogu.com.cn/problem/P3812))"
    ```cpp
    --8<-- "docs/math/code/basis/basis_1.cpp"
    ```

#### Gaussian elimination

Gaussian elimination amounts to constructing the linear basis from the viewpoint of systems of linear equations; its correctness is obvious.

??? example "Code (Luogu P3812 [【模板】线性基 (Template: linear basis)](https://www.luogu.com.cn/problem/P3812))"
    ```cpp
    --8<-- "docs/math/code/basis/basis_2.cpp"
    ```

### Properties

A linear basis constructed by the greedy method has the following properties:

-   The linear basis has no subset whose XOR is $0$.
-   The numbers in the linear basis have different highest set bits in binary.

A linear basis constructed by Gaussian elimination satisfies the following property:

-   The matrix after Gaussian elimination is in reduced row echelon form.

    > This property includes both properties satisfied by a linear basis constructed by the greedy method

    If the correctness of this property is unclear, see [Gaussian elimination](../numerical/gauss.md).

Here is a sample:

```text
5
633 211 169 841 1008
```

Binary representation:

```text
1001111001
0011010011
0010101001
1101001001
1111110000
```

Linear basis generated by the greedy method:

```text
1001111001
0100110000
0011010011
0001111010
0000000000
0000010000
0000000000
0000000000
0000000000
0000000000
```

Linear basis generated by Gaussian elimination:

```text
1000000011
0100100000
0010101001
0001101010
0000010000
0000000000
0000000000
0000000000
0000000000
0000000000
```

This is a very nice property that helps us solve many problems more conveniently. For example: given some numbers, choose some of them and XOR them together to maximize the XOR. If the linear basis is constructed by the greedy method, another greedy pass is needed: if the current bit of `ans` is `0`, XOR-ing is definitely better, otherwise if the current bit is `1`, it is definitely not better; whereas after constructing the linear basis by Gaussian elimination, we can simply XOR all elements of the linear basis together and output the result.

For other classic problems (querying whether a number can be obtained by XOR, querying the $k$-th largest number obtainable by XOR, etc.), a linear basis obtained by Gaussian elimination also solves them more conveniently.

### Time complexity

Let the vector length be $n$ and the total number of vectors be $m$. Then the time complexity is $O(nm)$. Gaussian elimination has a slightly larger constant.

For a real linear basis, the time complexity is $O(n^2m)$.

### Merging linear bases

Merging linear bases only requires brute force, i.e. inserting the vectors of one linear basis into the other one by one. The time complexity of a single merge is $O(n^2)$ (XOR linear basis) or $O(n^3)$ (real linear basis).

### Intersection of linear bases

The intersection of linear bases, strictly speaking, is a linear basis of the intersection of the two vector spaces they span. This section introduces two algorithms. For both algorithms, the time complexity of a single intersection is $O(n^2)$ (XOR linear basis) or $O(n^3)$ (real linear basis).

#### Naive algorithm

Let the linear bases to be intersected be $\alpha$ and $\beta$. The algorithm for intersecting linear bases only requires the following adjustments to the brute-force merging algorithm (taking the XOR linear basis as an example):

-   Try to insert the vectors $\beta_j$ of the linear basis $\beta$ into $\alpha$ using the [greedy method](#greedy-method), and initialize the intersection $\gamma$ of the linear bases as the empty set;
-   During insertion, record the contribution of the elements of the linear basis $\beta$ to the vector being inserted. Specifically, maintain a new vector $b$, initialized to $\beta_j$; moreover, if the vector being inserted is XOR-ed with the vector at position $x$ of the linear basis, then the contribution $b$ must also be XOR-ed with the contribution $b_x$ recorded at position $x$;
-   If the insertion succeeds and the vector $\beta_j'$ is inserted at position $x$ of the linear basis, set the $b_x$ recorded at position $x$ to the contribution $b$ of the elements of the linear basis $\beta$ in the process of obtaining $\beta_j'$;
-   If the insertion fails, insert the contribution $b$ of the elements of the linear basis $\beta$ recorded during the process into $\gamma$.

The linear basis $\gamma$ obtained this way is the desired intersection; of course, this algorithm also computes the union of the linear bases at the same time.

??? note "Explanation of the algorithm"
    Let the merged linear basis be $\{\alpha_1,\cdots,\alpha_m,\beta'_{j_1},\cdots,\beta'_{j_\ell}\}$, where $\beta'_{j_k}$ is the vector finally obtained when inserting $\beta_{j_k}$. Then $\{\alpha_1,\cdots,\alpha_m,\beta_{j_1},\cdots,\beta_{j_\ell}\}$ is also a linear basis of the merged space. Denote by $\beta^+$ the set $\{\beta_{j_1},\cdots,\beta_{j_\ell}\}$; then the merged basis can be written as $\alpha\cup\beta^+$. Moreover, every vector $c$ in the sum space can be uniquely written in the form
    
    $$
    c = a\oplus b
    $$
    
    where $a\in\operatorname{span}\alpha$ and $b\in\operatorname{span}\beta^+$. The $b$ in this decomposition is exactly the "contribution of the elements of the linear basis $\beta$" that the algorithm above **attempts** to record. Strictly speaking, it is only the contribution of those vectors of $\beta$ that were finally inserted successfully.
    
    For a successful insertion, the finally recorded $b$ is exactly the $b$ term of this decomposition. Let $\beta_j\in\beta^+$. Initially, $\beta_j=0\oplus\beta_j$, which is already the correct decomposition of $\beta_j$ in the basis $\alpha\cup\beta^+$. When updating $\beta'_j=a\oplus b$ to $\beta'_j\oplus c_x$, since $\beta_j'\oplus c_x=(a\oplus a_x)\oplus(b\oplus b_x)$, it suffices to update $b$ to $b\oplus b_x$ to keep the decomposition correct. Therefore, by induction, when $\beta'_j$ is finally inserted into the merged linear basis, the recorded contribution $b$ is exactly the $b$ term of the decomposition above.
    
    For a failed insertion, the vector to be inserted eventually becomes $0$, and the contribution $b$ at that moment is inserted into $\gamma$. If we repeat the argument above, we find that during the insertion it is still guaranteed that $\beta_j'=a\oplus b$ with $a\in\operatorname{span}\alpha$, except that $b$ no longer belongs to $\operatorname{span}\beta^+$. This is because at initialization, in $\beta_j=0\oplus\beta_j$ we have $\beta_j\notin\beta^+$. Apart from that, all terms XOR-ed in when updating the contribution belong to $\operatorname{span}\beta^+$. So, in fact, $b\oplus\beta_j\in\operatorname{span}\beta^+$.
    
    Then why does inserting all these $b$ from failed insertions into $\gamma$ yield a linear basis of the intersection space? First, if inserting $\beta_j$ fails, we eventually get $0=a\oplus b$, where $a\in\operatorname{span}\alpha$ and $b\in\operatorname{span}(\beta^+\cup\{\beta_j\})\subseteq\operatorname{span}\beta$. Therefore $b=a$ necessarily lies in the intersection space $\operatorname{span}\alpha\cap\operatorname{span}\beta$. Conversely, let $c$ be any element of the intersection space. Since $c\in\operatorname{span}\beta$, $c$ can be written as a linear combination (XOR sum) of elements of $\beta$:
    
    $$
    c = \bigoplus_{\beta_j\in\beta}\lambda_j\beta_j,
    $$
    
    where $\lambda_j\in\{0,1\}$. For each $\beta_j\notin\beta^+$, denote by $b_j$ the corresponding contribution inserted into $\gamma$; then
    
    $$
    c\oplus\bigoplus_{\beta_j\notin\beta^+}\lambda_jb_j = \bigoplus_{\beta_j\in\beta^+}\lambda_j\beta_j+\bigoplus_{\beta_j\notin\beta^+}\lambda_j(\beta_j\oplus b_j),
    $$
    
    Note that $b_j$ and $c$ both lie in the intersection space, so the left-hand side must also lie in the intersection space and can therefore be written as a linear combination of elements of $\alpha$; at the same time, for every term on the right-hand side, either $\beta_j\in\beta^+$, or $\beta_j\notin\beta^+$ and $\beta_j\oplus b_j\in\beta^+$, so the right-hand side is in fact a linear combination of elements of $\beta^+$. But $\alpha\cup\beta^+$ is linearly independent, so all coefficients are $0$, that is, $c=\bigoplus_{\beta_j\notin\beta^+}\lambda_jb_j\in\operatorname{span}\{b_1,\cdots,b_j\}$. This shows that the contributions $b$ of the vectors that could not be inserted together span the intersection space.
    
    According to this explanation, the purpose of maintaining the contribution $b$ during the process is in fact to maintain the decomposition $a\oplus b$; moreover, when the contribution is finally inserted into $\gamma$, we always have $a=b$. Therefore, whether we maintain the contribution of the elements of $\alpha$ or of $\beta$ (i.e. whether we maintain $a$ or $b$), the result is correct. To maintain the contribution of the elements of the linear basis $\alpha$, it suffices to change the initial values of the contributions: each vector $\alpha_i$ in $\alpha$ initially has contribution $\alpha_i$, while an inserted $\beta_j$ has initial contribution $0$.

The code for the template problem is as follows:

??? example "Code (Library Checker [Intersection of $\mathbf F_2$ vector spaces](https://judge.yosupo.jp/problem/intersection_of_f2_vector_spaces))"
    ```cpp
    --8<-- "docs/math/code/basis/basis_intersect_1.cpp"
    ```

#### Zassenhaus algorithm

Another equivalent approach is the Zassenhaus algorithm, which likewise computes the union and the intersection of two linear bases at the same time. The complexity is exactly the same as above.

The concrete steps are as follows:

-   Initialize an empty linear basis $\gamma$ of vectors of length $2n$, where the vectors are written in the form $(a,b)$ with $a$ and $b$ both of length $n$;
-   Insert the elements $\alpha_i$ of $\alpha$ into $\gamma$ in the form $(\alpha_i,\alpha_i)$;
-   Insert the elements $\beta_j$ of $\beta$ into $\gamma$ in the form $(\beta_j,0)$;
-   Among all nonzero elements $(c_k,d_k)$ of the resulting linear basis $\gamma$, the components $c_k$ of those vectors with nonzero $c_k$ together form a linear basis of the union of $\alpha$ and $\beta$, and the components $d_k$ of those vectors with zero $c_k$ together form a linear basis of the intersection of $\alpha$ and $\beta$.

The method of constructing the linear basis in the algorithm can be either the [greedy method](#greedy-method) or [Gaussian elimination](#gaussian-elimination), as long as the linear basis in $\gamma$ forms a matrix in row echelon form.

Comparing the elimination steps in the Zassenhaus algorithm with the naive algorithm above, it is easy to see that the Zassenhaus algorithm based on the greedy method is equivalent to the naive algorithm maintaining the contribution of the elements of $\alpha$. If instead we first insert all $(\alpha_i,0)$ and then all $(\beta_j,\beta_j)$, the Zassenhaus algorithm based on the greedy method is equivalent to the naive algorithm maintaining the contribution of the elements of $\beta$. By the equivalence of the elimination steps, the correctness of the Zassenhaus algorithm also holds.

In addition, an independent and more general algebraic proof can be given:

??? note "Proof of correctness"
    Let $V$ be a vector space with subspaces $U=\operatorname{span}\alpha$ and $W=\operatorname{span}\beta$. The algorithm itself amounts to finding, by reduction to row echelon form, a basis $\gamma$ of the subspace
    
    $$
    H = \operatorname{span}(\{(\alpha_i,\alpha_i):\alpha_i\in\alpha\}\cup\{(\beta_j,0):\beta_j\in\beta\})
    $$
    
    At the end of the algorithm, the elements $(c_k,d_k)$ of $\gamma$ need to be divided into two classes according to whether $c_k\neq 0$, so consider the projection map $\pi:H\rightarrow V$ with $\pi(a,b)=a$. Then $\pi(H)=U+W$, and it is easy to verify that
    
    $$
    \begin{aligned}
    \ker\pi &= H\cap(\{0\}\times V) = \{0\}\times(U\times W).
    \end{aligned}
    $$
    
    By the [theorem on linear maps](./linear-mapping.md#线性映射的核空间与像空间), $\dim H = \dim\pi(H)+\dim\ker\pi = \dim(U+W)+\dim(U\cap W)$.
    
    The first few columns of a matrix in row echelon form still form a matrix in row echelon form, so the number of rows with $c_k\neq 0$ is exactly the row rank of $\alpha\cup\beta$, i.e. $\dim(U+W)$; moreover, the set of $c_k$ in these rows forms a basis of $U+W$. The remaining nonzero rows number exactly $\dim(U\cap W)$ and all satisfy $c_k=0$. For the $d_k$ in these rows, since $(0,d_k)\in\ker\pi$, we have $d_k\in U\cap W$; moreover, the $(0,d_k)$, being rows of a matrix in row echelon form, are necessarily linearly independent, which shows that these $d_k$ are linearly independent. Putting it all together, these $d_k$ form a linearly independent set of size $\dim(U\cap W)$ in the intersection space $U\cap W$, so they must also be a basis of that space.

The code for the template problem is as follows:

??? example "Code (Library Checker [Intersection of $\mathbf F_2$ vector spaces](https://judge.yosupo.jp/problem/intersection_of_f2_vector_spaces))"
    ```cpp
    --8<-- "docs/math/code/basis/basis_intersect_2.cpp"
    ```

Note that when outputting, only the vectors whose first $n$ bits are all zero need to be considered.

### Extension: prefix linear basis

This section only discusses the case of the XOR linear basis, and assumes that a single vector can be stored in $O(1)$ space and that a single operation always takes $O(1)$ time.

When the maximum XOR on a range needs to be queried many times, a common approach is the [cat tree](../../ds/cat-tree.md) combined with a linear basis, with time complexity $O(nm\log m+n^2q)$, where $n$ is the vector length, $m$ is the sequence length and $q$ is the number of queries. Another feasible approach is the prefix linear basis (also called the timestamped linear basis), which reduces the complexity to $O(n(m+q))$.

The prefix linear basis allows us to maintain, for every prefix of the sequence, the linear bases of all suffixes of that prefix, so that the linear basis of every range can be queried. Note that the linear bases of all suffixes $[j,i]$ of a prefix $[1,i]$ of the sequence are nested in one another, i.e. the linear basis of $[j,i]$ always contains the linear basis of $[j+1,i]$; therefore, among the linear bases of these suffixes there are at most $n$ distinct ones, and the linear bases of all these suffixes from $[i,i]$ to $[1,i]$ can always be obtained by gradually adding new vectors to the empty set. Hence, using this monotonicity, we only need to mark each added vector $v$ with the largest index $t$ at which it appears, and the linear bases of all suffixes can be stored in $O(n)$ space. Moreover, when querying the linear basis corresponding to the range $[j,i]$, we only need to keep those vectors in the prefix linear basis at $i$ whose mark satisfies $t\ge j$.

Let us call the mark $t$ of each vector $v$ its timestamp. A vector $v$ in the linear basis can always be expressed as the XOR of some elements of the original sequence, e.g. $v_{i_1}\oplus v_{i_2}\oplus\cdots\oplus v_{i_k}$. Among all such possible representations, the maximum of the minimum indices is exactly $t$, i.e.

$$
t(v) = \max\{j:\exists i_1,\cdots,i_k\in[j,i]\text{ s.t. }v=v_{i_1}\oplus v_{i_2}\oplus\cdots\oplus v_{i_k}\}.
$$

This expression merely writes the description of the previous paragraph in formal language. The insight it gives us is that to maintain the timestamp of every vector $v$ in the linear basis, we only need to greedily choose vectors that are as new as possible to replace old ones.

Based on the [greedy method](#greedy-method) of constructing a linear basis mentioned above, the prefix linear basis makes the following adjustments in the construction process:

-   For every vector $a_x$ kept in the linear basis, store a timestamp $t_x$, initially set to $0$;
-   To add the $i$-th vector $v$ of the sequence, still scan from high bits to low bits, but also record the current time $i$;
-   If bit $x$ of $v$ is one, compare the timestamp $t_x$ of the existing vector $a_x$ in the linear basis with the current time $i$:
    -   If $i>t_x$, i.e. the vector being added is newer, set $a_x$ to $v$, update the timestamp to $i$, and continue the adding process with the XOR of the old $a_x$ and $v$, $a_x\oplus v$, using the previously recorded time $t_x$;
    -   If $i<t_x$, i.e. the vector being added is older, do not update $a_x$ or $t_x$; XOR $v$ with $a_x$ and continue adding.

In other words, if the current bit can be represented by a newer vector, use the newer vector directly; otherwise, keep the original vector. When updating the vector at position $x$, the XOR result $a_x\oplus v$ must not be stored at position $x$, because the timestamp of the XOR result $a_x\oplus v$ is $\min\{t(a_x)=t(v)\}=t(a_x)$, which is smaller than the timestamp $t(v)$ of the vector $v$ being added. For the same reason, the upward updates in the construction of a linear basis by [Gaussian elimination](#gaussian-elimination) may break the timestamp property, so it is no longer suitable for constructing a prefix linear basis.

The code for the template problem is as follows:

??? example "Code (Codeforces [1100F Ivan and Burgers](https://codeforces.com/problemset/problem/1100/F))"
    ```cpp
    --8<-- "docs/math/code/basis/prefix_basis.cpp"
    ```

If online queries are required, one can also store the prefix linear basis at every prefix using $O(mn)$ space and then answer queries; this can be seen as a kind of "persistent" linear basis. If the properties of a linear basis obtained by Gaussian elimination are needed, they can be handled separately at query time.

### Exercises

-   [Luogu P3812【模板】线性基 (Template: linear basis)](https://www.luogu.com.cn/problem/P3812)
-   [AcWing 3164. 线性基 (Linear basis)](https://www.acwing.com/problem/content/description/3167)
-   [SGU 275 to xor or not xor](https://codeforces.com/problemsets/acmsguru/problem/99999/275)
-   [HDU 3949 XOR](https://acm.hdu.edu.cn/showproblem.php?pid=3949)
-   [HDU 6579 Operation](https://acm.hdu.edu.cn/showproblem.php?pid=6579)
-   [Luogu P4151 \[WC2011\] 最大 XOR 和路径 (Maximum XOR path)](https://www.luogu.com.cn/problem/P4151)
-   [Library Checker - Intersection of $\mathbf F_2$ vector spaces](https://judge.yosupo.jp/problem/intersection_of_f2_vector_spaces)
-   [AtCoder Grand Contest 045 A - Xor Battle](https://atcoder.jp/contests/agc045/tasks/agc045_a)
-   [Codeforces 1100F Ivan and Burgers](https://codeforces.com/problemset/problem/1100/F)
-   [Luogu P3292 \[SCOI2016\] 幸运数字 (Lucky numbers)](https://www.luogu.com.cn/problem/P3292)

## References and notes

1.  丘维声，高等代数（下）．清华大学出版社． (Qiu Weisheng, Advanced Algebra (Vol. 2). Tsinghua University Press.)
2.  [Basis (linear algebra) - Wikipedia](https://en.wikipedia.org/wiki/Basis_%28linear_algebra%29)
3.  [Vector Basis -- from Wolfram MathWorld](https://mathworld.wolfram.com/VectorBasis.html)
4.  [Zassenhaus algorithm - Wikipedia](https://en.wikipedia.org/wiki/Zassenhaus_algorithm)

[^existence_basis]: [Proof that every vector space has a basis](https://en.wikipedia.org/wiki/Basis_%28linear_algebra%29#Proof_that_every_vector_space_has_a_basis)
