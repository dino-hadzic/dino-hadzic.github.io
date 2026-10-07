---
title: Matrix-tree theorem
---

The matrix-tree theorem (Kirchhoff's theorem) solves the problem of counting the spanning trees of a graph.

## Notation used in this article

The graphs in this article, both undirected and directed, may have multiple edges, but by default they have no self-loops.

??? note "The case with self-loops"
    Self-loops do not affect the number of spanning trees; simply ignore them when computing the Laplacian matrix. However, when counting Eulerian circuits with the BEST theorem, self-loops must be counted in the degrees.

### Undirected graphs

Let $G$ be an undirected graph with $n$ vertices. Define the degree matrix $D(G)$ by

$$
D_{ii}(G) = \mathrm{deg}(i),\ D_{ij} = 0,\ i\neq j.
$$

Let $\#e(i,j)$ be the number of edges between vertices $i$ and $j$, and define the adjacency matrix $A$ by

$$
A_{ij}(G)=A_{ji}(G)=\#e(i,j),\ i\neq j.
$$

Define the Laplacian matrix (also called the Kirchhoff matrix) $L$ by

$$
L(G) = D(G) - A(G).
$$

Denote the number of all spanning trees of $G$ by $t(G)$.

### Directed graphs

Let $G$ be a directed graph with $n$ vertices. Define the out-degree matrix $D^\mathrm{out}(G)$ by

$$
D^\mathrm{out}_{ii}(G) = \mathrm{deg}^\mathrm{out}(i),\ D^\mathrm{out}_{ij} = 0,\ i\neq j.
$$

Define the in-degree matrix $D^\mathrm{in}(G)$ analogously.

Let $\#e(i,j)$ be the number of directed edges from vertex $i$ to vertex $j$, and define the adjacency matrix $A$ by

$$
A_{ij}(G)=\#e(i,j),\ i\neq j.
$$

Define the out-degree Laplacian matrix $L^\mathrm{out}$ by

$$
L^\mathrm{out}(G) = D^\mathrm{out}(G) - A(G).
$$

Define the in-degree Laplacian matrix $L^\mathrm{in}$ by

$$
L^\mathrm{in}(G) = D^\mathrm{in}(G) - A(G).
$$

Denote the number of all root-directed spanning arborescences of $G$ with root $k$ by $t^\mathrm{root}(G,k)$. A root-directed arborescence (in-arborescence) is a directed graph whose underlying undirected graph is a tree and in which every edge points toward the parent.

Denote the number of all leaf-directed spanning arborescences of $G$ with root $k$ by $t^\mathrm{leaf}(G,k)$. A leaf-directed arborescence (out-arborescence) is a directed graph whose underlying undirected graph is a tree and in which every edge points toward a child.

## Statement of the theorem

The matrix-tree theorem has several forms.

Define $[n]=\{1,2,\cdots,n\}$; the submatrix $A_{S,T}$ of a matrix $A$ is the submatrix obtained by selecting the entries $A_{i,j}\pod{i\in S,j\in T}$.

???+ note "Theorem 1 (matrix-tree theorem, undirected graph, determinant form)"
    For an undirected graph $G$ and any $k$,
    
    $$
    t(G) = \det L(G)_{[n]\setminus\{k\},[n]\setminus\{k\}}.
    $$
    
    In other words, all principal minors of order $n-1$ of the Laplacian matrix of an undirected graph are equal, and all of them equal the number of spanning trees of the graph.

???+ note "Corollary 1 (matrix-tree theorem, undirected graph, eigenvalue form)"
    Let $\lambda_1\ge\lambda_2\ge\cdots\ge\lambda_{n-1}\ge\lambda_n=0$ be the $n$ eigenvalues of $L(G)$. Then
    
    $$
    t(G) = \frac{1}{n}\lambda_1\lambda_2\cdots\lambda_{n-1}.
    $$

???+ note "Theorem 2 (matrix-tree theorem, directed graph, root-directed arborescences, determinant form)"
    For a directed graph $G$ and any $k$,
    
    $$
    t^\mathrm{root}(G,k) = \det L^\mathrm{out}(G)_{[n]\setminus\{k\},[n]\setminus\{k\}}.
    $$
    
    In other words, the principal minor obtained by deleting the $k$-th row and $k$-th column of the out-degree Laplacian matrix of a directed graph equals the number of root-directed arborescences with root $k$.

Therefore, to count all root-directed arborescences of a graph, it suffices to enumerate every root $k$ and sum $t^\mathrm{root}(G,k)$.

???+ note "Theorem 3 (matrix-tree theorem, directed graph, leaf-directed arborescences, determinant form)"
    For a directed graph $G$ and any $k$,
    
    $$
    t^\mathrm{leaf}(G,k) = \det L^\mathrm{in}(G)_{[n]\setminus\{k\},[n]\setminus\{k\}}.
    $$
    
    In other words, the principal minor obtained by deleting the $k$-th row and $k$-th column of the in-degree Laplacian matrix of a directed graph equals the number of leaf-directed arborescences with root $k$.

Therefore, to count all leaf-directed arborescences of a graph, it suffices to enumerate every root $k$ and sum $t^\mathrm{leaf}(G,k)$.

???+ note "Remark"
    Root-directed arborescences are also called in-arborescences, but since computing them uses out-degrees, we use the term "root-directed" to avoid confusion between $\mathrm{in}$ and $\mathrm{out}$.

## Proof of the theorem

Notice that the forms of the theorems above are extremely similar; here we give a unified proof and at the same time extend the previous results to weighted graphs.

The rough outline of the proof is as follows:

-   first, all cases can be reduced to counting root-directed arborescences in a directed graph;
-   using the language of matrices, we give a necessary and sufficient condition for a chosen set of edges to form a root-directed arborescence;
-   we relate the choice of edges to the determinant of the Laplacian matrix through the Cauchy–Binet formula;
-   finally, we convert the determinant-form result into the eigenvalue-form result.

### Lemma: the Cauchy–Binet formula

???+ note "Lemma 1 (Cauchy–Binet)"
    Given an $n\times m$ matrix $A$ and an $m\times n$ matrix $B$,
    
    $$
    \det(AB)=\sum_{S\subset[m];~|S|=n}\det A_{[n],S}\det B_{S,[n]},
    $$
    
    where the summation means that $S$ ranges over all subsets of $[m]$ of size $n$. If $n>m$, necessarily $\det(AB)=0$.

??? note "Proof (combinatorial view)"
    Following the model of ["NOI2021" Path Intersections](https://loj.ac/p/3533), first consider the following combinatorial meaning of the determinant. For an $n\times n$ matrix $C$, build a directed acyclic graph $G=(V,E)$. The vertex set is $V=[2]\times[n]\subset\mathbb R^2$, i.e. two columns of points in the plane. Denote the left column by $L=\{l_i=(1,i):i\in[n]\}$ and the right column by $R=\{r_i=(2,i):i\in[n]\}$; the directed edge set is $E=\{(l_i,r_j):i,j\in[n]\}$, with edge weights $w(l_i,r_j)=C_{i,j}$. In this graph, a subset of edges $E^\sigma\subset E$ of size $n$ is called a path system if its starting points are pairwise distinct and its endpoints are pairwise distinct. Clearly, path systems $E^\sigma$ correspond one-to-one to permutations $\sigma$ of $[n]$. Notice that if a path system is drawn in the plane, its edges may cross pairwise, and the number of crossings (with multiplicity) equals the number of inversions of $\sigma$. This is because the edges $(l_i,r_{\sigma(i)})$ and $(l_j,r_{\sigma(j)})$ cross if and only if $(i-j)(\sigma(i)-\sigma(j))< 0$, i.e. they form an inversion. For convenience, call the parity of the number of inversions of the corresponding permutation, i.e. the parity of the number of crossings of the path system, the parity of the path system. Thus, if we count the path systems with weights and subtract the number of path systems with an odd number of crossings from the number with an even number of crossings, we obtain the Leibniz expansion of the determinant:
    
    $$
    \det(C)=\sum_{\sigma\in S_n}\mathrm{sgn}(\sigma)\prod_{i\in[n]}C_{i,\sigma(i)},
    $$
    
    where $S_n$ is the permutation group on $[n]$, and $\mathrm{sgn}(\sigma)$ is the sign of the permutation $\sigma$ (equal to $1$ when the number of inversions is even and $-1$ when it is odd).
    
    Having understood the combinatorial meaning of the determinant, we can prove the Cauchy–Binet formula with the following combinatorial model. For an $n\times m$ matrix $A$ and an $m\times n$ matrix $B$, build a directed acyclic graph $G=(V,E)$. The vertex set is $V=L\cup D\cup R$, where $L=\{l_i=(1,i):i\in[n]\}$, $D=\{d_i=(2,i):i\in[m]\}$ and $R=\{r_i=(3,i):i\in[n]\}$; the directed edge set is $E=E_L\cup E_R$, where $E_L=\{(l_i,d_j):i\in[n],j\in[m]\}$ and $E_R=\{(d_j,r_i):j\in[m],i\in[n]\}$, with edge weights $w(l_i,d_j)=A_{i,j}$ and $w(d_j,r_i)=B_{j,i}$ respectively. Again consider path systems from $L$ through $D$ to $R$ (paths pairwise sharing no vertex), count them with weights, and subtract the number of path systems with an odd number of crossings from the number with an even number of crossings. We now show that the left and right sides of the Cauchy–Binet formula compute this quantity in two different ways.
    
    For the left side, based on the graph $G$ described above, build a new graph $G'$ with vertex set $V'=L\cup R$ and edge set $E'=\{(l_i,r_j):i,j\in[n]\}$, and assign to the edge $(l_i,r_j)$ the weight $\sum_{k\in[m]}A_{i,k}B_{k,j}$, i.e. the weighted count of simple paths from $l_i$ to $r_j$ in the original graph $G$. This weight is exactly $(AB)_{i,j}$. This amounts to collapsing the three-layer graph into a two-layer graph. However, the path systems (counted with weights) in the two-layer graph $G'$ do not correspond one-to-one to the path systems in the three-layer graph $G$. Since each path in the two-layer graph corresponds to several simple paths in the three-layer graph, counting path systems in the two-layer graph multiplies the weights, which amounts to taking all pairwise combinations of the corresponding sets of paths in the three-layer graph, and this necessarily includes cases where paths share an intermediate stop. But these pairs of paths sharing an intermediate stop do not contribute to the final answer, because for $i_1< i_2$, $j_1< j_2$ and any intermediate point $d$ there are two pairs of simple paths $(l_{i_1}\rightarrow d\rightarrow r_{j_1}, l_{i_2}\rightarrow d\rightarrow r_{j_2})$ and $(l_{i_1}\rightarrow d\rightarrow r_{j_2}, l_{i_2}\rightarrow d\rightarrow r_{j_1})$, and the parities of the numbers of crossings of these two path systems in the three-layer graph are necessarily opposite, because looking only at the starting points and endpoints, the two systems have swapped endpoints. Therefore, the contributions of paths sharing an intermediate stop cancel in pairs when counting in the collapsed two-layer graph. In the remaining cases, if the starting points and endpoints of two paths are given, then no matter how the intermediate points are chosen (as long as they are not the same point), the parity of the number of crossings of these two paths does not change. Hence all path systems of the original graph $G$ corresponding to one path system in $G'$ have the same parity. Consequently, $\det(AB)$ provides one way to compute the difference of path-system counts described above.
    
    For the right side, it amounts to enumerating all possible combinations of intermediate points. Given any set of intermediate points $S\subset D=[m]$ with $|S|=n$, consider separately the path systems from $L$ to $S$ and from $S$ to $R$; they can be concatenated into path systems from $L$ to $R$, and the composition of the permutations of the first two path systems equals the permutation of the resulting path system, so the product of the parities of the first two equals the parity of the result. Therefore, the difference of counts of path systems with intermediate set $S$ is exactly the product of the difference of counts of path systems from $L$ to $S$ and the difference of counts of path systems from $S$ to $R$. Summing over all possible $S$ gives the right side, so it too equals the difference of path-system counts described above.

??? note "Proof (algebraic view)"
    The combinatorial proof above can actually be translated word by word into an algebraic proof. Here we instead give a different, more technical algebraic proof that uses several well-known facts. When $m< n$, the determinant is zero, because
    
    $$
    \mathrm{rank}(AB)\le \min\{\mathrm{rank}(A),\mathrm{rank}(B)\}\le m< n.
    $$
    
    When $m=n$, the Cauchy–Binet formula says that the determinant of a product of square matrices equals the product of their determinants.
    
    When $m>n$, notice that
    
    $$
    x^{m-n}\det(xI_n+AB) = \det(xI_m+BA).
    $$
    
    It is also known that the coefficient of $x^{n-k}$ in $\det(xI_n+C)$ is the sum of all principal minors of order $k$ of $C$. Hence, comparing coefficients on both sides of the identity above,
    
    $$
    \det(AB) = \sum_{S\subset[m];~|S|=n}\det (BA)_{S,S} = \sum_{S\subset[m];~|S|=n}\det B_{S,[n]}\det A_{[n],S} = \sum_{S\subset[m];~|S|=n}\det A_{[n],S}\det B_{S,[n]}.
    $$
    
    Here the second equality uses the result for the case $m=n$.

### Describing the structure of a graph with incidence matrices

Let $G=(V,E)$ be a directed graph with $n$ vertices and $m$ edges, where edge $e$ has weight $w(e)$. Define the $m\times n$ out-incidence matrix

$$
M^\mathrm{out}_{ij}=\begin{cases}
\sqrt{w(e_i)},&\exists u(e_i=(v_j,u)),\\
0,&\textrm{otherwise},
\end{cases}
$$

and the $m\times n$ in-incidence matrix

$$
M^\mathrm{in}_{ij}=\begin{cases}
\sqrt{w(e_i)},&\exists u(e_i=(u,v_j)),\\
0,&\textrm{otherwise}.
\end{cases}
$$

Each of their rows records one edge: the out-incidence matrix $M^\mathrm{out}$ records the tail of the edge, and the in-incidence matrix $M^\mathrm{in}$ records the head of the edge.

A simple computation shows

$$
D^\mathrm{out}(G) = (M^\mathrm{out})^T M^\mathrm{out},\ A(G) = (M^\mathrm{out})^T M^\mathrm{in},\ D^\mathrm{in}(G) = (M^\mathrm{in})^T M^\mathrm{in}.
$$

Consequently

$$
L^\mathrm{out}(G) = (M^\mathrm{out})^T (M^\mathrm{out}-M^\mathrm{in}),\ L^\mathrm{in}(G) = (M^\mathrm{in}-M^\mathrm{out})^T M^\mathrm{in}.
$$

The Cauchy–Binet formula above shows that a principal minor of the Laplacian matrix is in fact a sum over a family of substructures. Each substructure reflects the properties of the corresponding subgraph.

???+ note "Lemma 2"
    For a vertex subset $W\subseteq V$ and an edge subset $S\subseteq E$ satisfying $|W|=|S|\le n$, if the subgraph $T=(V,S)$ is a root-directed forest with roots $V\setminus W$, then the expression
    
    $$
    \det(M^\mathrm{out}_{S,W})\det(M^\mathrm{out}_{S,W}-M^\mathrm{in}_{S,W})
    $$
    
    equals $\prod_{e\in S}w(e)$, denoted $w(T)$; otherwise, the expression equals zero.

??? note "Proof"
    Without loss of generality let $w(e)=1$. Indeed, by the multilinearity of the determinant, a factor $\sqrt{w(e)}$ can be pulled out of every row of each determinant, and the product of these factors is $w(T)$.
    
    First we analyze when the two factors are zero. The first factor $\det(M^\mathrm{out}_{S,W})$ has at most one nonzero entry in each row, namely $+1$. If any row is entirely zero, or two rows have their $+1$ in the same column, the determinant is necessarily zero. So this determinant is nonzero if and only if every row and every column has exactly one $+1$, i.e. the tail of every edge in $S$ lies in $W$, and every vertex of $W$ is the tail of exactly one edge of $S$. If $T$ is a root-directed forest with roots $V\setminus W$, a necessary condition is that every vertex except the roots has exactly one parent, which guarantees that this factor is nonzero; but the converse need not hold, because the absence of cycles is not guaranteed, so we must also examine the second factor. Note that the heads of the edges in $S$ need not lie in $W$.
    
    Assume the first factor is nonzero; then the subgraph $T$ is a root-directed forest if and only if $T$ has no cycle. Now the second factor $\det(M^\mathrm{out}_{S,W}-M^\mathrm{in}_{S,W})$ has one $+1$ in each row, and possibly one or zero $-1$. For edges whose head also lies in $W$: if the head of $e_i$ is the tail of $e_j$, adding the row of $e_j$ to the row of $e_i$ cancels the $-1$ in row $e_i$. One can imagine that this row now describes the simple path formed by $e_i$ followed by $e_j$. If a new $-1$ appears in this row, then the head of $e_j$ also lies in $W$ and the position of the $-1$ is the head of $e_j$; so we can find the edge whose tail is the head of $e_j$ and add it to this row again. Such an edge always exists, because the previous paragraph shows that every vertex of $W$ is the tail of exactly one edge of $S$. This process continues until no $-1$ appears in the row, which amounts to repeatedly appending new edges to the simple path $e_i\rightarrow e_j\rightarrow \cdots\rightarrow e_k$. At this point, if only one $+1$ remains in the row, the head of $e_k$ is not in the chosen vertex set $W$ and the process stops; if the last edge added happens to cancel the existing $+1$, i.e. only zeros remain in the row, then the head of the new edge $e_k$ is the tail of the initial edge $e_i$, i.e. a cycle has appeared; if the process never terminates, the path has entered a cycle, and the rows of the edges on that cycle likewise become zero. Therefore, the necessary and sufficient condition for having no cycle is that the determinant can be transformed by the operations above into a form where every row has exactly one $+1$. Since the positions of these $+1$ entries are the tails of the edges of the respective rows, the resulting matrix is in fact $M^\mathrm{out}_{S,W}$, so the two determinants are equal.
    
    In summary, if $T$ is not a root-directed forest, then either $\det(M^\mathrm{out}_{S,W})=0$ or $\det(M^\mathrm{out}_{S,W}-M^\mathrm{in}_{S,W})=0$; otherwise both are nonzero and their product equals $\left(\det(M^\mathrm{out}_{S,W})\right)^2=1$.

### Matrix-tree theorem for weighted directed graphs

We can now prove the main result of this article. All forms of the matrix-tree theorem stated above are special cases of this theorem.

???+ note "Theorem 4 (matrix-tree theorem, weighted directed graph, root-directed arborescences, determinant form)"
    For any $k$,
    
    $$
    \sum_{T\in\mathcal T^\mathrm{root}(G,k)}w(T)=\det L^\mathrm{out}(G)_{[n]\setminus\{k\},[n]\setminus\{k\}}.
    $$
    
    Here $\mathcal T^\mathrm{root}(G,k)$ is the set of root-directed spanning arborescences of $G$ with root $k$.

??? note "Proof"
    Let $W=[n]\setminus\{k\}$ be the set of remaining vertices other than $k$. Then, by the Cauchy–Binet formula, the right side can be written as
    
    $$
    \det L^\mathrm{out}(G)_{W,W} = \sum_{S\subset[m];~|S|=n-1}\det(M^\mathrm{out}_{S,W})\det(M^\mathrm{out}_{S,W}-M^\mathrm{in}_{S,W}).
    $$
    
    Ranging over all $S$, by Lemma 2 the right side accumulates a term $w(T)$ if and only if $T=(V,S)$ forms a root-directed forest with roots $V\setminus W=\{k\}$, i.e. $T$ is a root-directed spanning arborescence with root $k$.

When $w(e)=1$, the weight of every tree is $1$, so the left side is the count of all such trees, i.e. $t^\mathrm{root}(G,k)$, which gives Theorem 2. By analogy, the result extends directly to leaf-directed arborescences, which gives Theorem 3. Finally, to count spanning trees of an undirected graph, we can apply the following corollary.

???+ note "Corollary 2 (matrix-tree theorem, weighted undirected graph, determinant form)"
    For an undirected graph $G$ and any $k$,
    
    $$
    \sum_{T\in\mathcal T(G)}w(T) = \det L(G)_{[n]\setminus\{k\},[n]\setminus\{k\}}.
    $$
    
    Here $\mathcal T(G)$ is the set of spanning trees of $G$. This also shows that all principal minors of order $(n-1)$ of $L(G)$ are equal.

??? note "Proof"
    For an undirected graph $G=(V,E)$, build the directed graph $G'=(V,E')$ with $E'=\{(v_i,v_j):(v_i,v_j)\in E\}\cup\{(v_j,v_i):(v_i,v_j)\in E\}$, i.e. every undirected edge of $G$ is split into two oppositely directed edges. Fix any $k$; then the root-directed spanning arborescences of $G'$ with root $k$ correspond one-to-one to the spanning trees of $G$. From the former to the latter, simply remove the orientation of the edges and the choice of root; from the latter to the former, simply start from the chosen root $k$ and orient the edges one by one toward the root. Therefore,
    
    $$
    \sum_{T\in\mathcal T(G)}w(T) = \sum_{T\in\mathcal T^\mathrm{root}(G',k)}w(T) = \det L^\mathrm{out}(G')_{[n]\setminus\{k\},[n]\setminus\{k\}} = \det L(G)_{[n]\setminus\{k\},[n]\setminus\{k\}}.
    $$
    
    Here we used $L^\mathrm{out}(G')=L(G)$, which is easy to verify directly.

### Eigenvalue form

Again we first consider the result on directed graphs.

???+ note "Theorem 5"
    For a directed graph $G$, define the multivariate polynomial
    
    $$
    \chi(x_1,\cdots,x_n)=\det(\mathrm{diag}(x_1,\cdots,x_n)-L^\mathrm{out}(G)).
    $$
    
    Here $\mathrm{diag}(x_1,\cdots,x_n)$ denotes the diagonal matrix with diagonal entries $x_1,\cdots,x_n$. Then
    
    $$
    (-1)^{n-r}[x_{k_1}\cdots x_{k_r}]\chi(x_1,\cdots,x_n)
    $$
    
    equals the (weighted) number of root-directed forests of $G$ with roots $\{k_1,\cdots,k_r\}$.

??? note "Proof"
    Following the proof of Theorem 4, notice that if we set $W=[n]\setminus\{k_1,\cdots,k_r\}$, then the expression in the theorem is $\det L^\mathrm{out}(G)_{W,W}$ (just look at the Leibniz expansion of the determinant). By the Cauchy–Binet formula, it equals
    
    $$
    \det L^\mathrm{out}(G)_{W,W} = \sum_{S\subset[m];~|S|=n-r}\det(M^\mathrm{out}_{S,W})\det(M^\mathrm{out}_{S,W}-M^\mathrm{in}_{S,W}).
    $$
    
    Ranging over all $S$, by Lemma 2 the right side accumulates a term $w(T)$ if and only if $T=(V,S)$ forms a root-directed forest with roots $V\setminus W=\{k_1,\cdots,k_r\}$.

Substituting $x$ for all the unknowns, we obtain the characteristic polynomial of the Laplacian matrix

$$
P(x) = \det(xI-L^\mathrm{out}(G)) = \chi(x,\cdots,x).
$$

???+ note "Lemma 3"
    The Laplacian matrix $L^\mathrm{out}(G)$ has at least one zero eigenvalue.

??? note "Proof"
    It suffices to show that its determinant is zero. Following the proofs of Theorems 4 and 5, take $W=[n]$ (i.e. the set of roots is empty); the value of this determinant should equal the number of root-directed forests with zero trees. There are none, so the determinant is zero.

???+ note "Corollary 3"
    For a directed graph $G$, the total weight of all root-directed forests consisting of $k$ trees equals the coefficient
    
    $$
    (-1)^{n-k}[x^k]P(x).
    $$

??? note "Proof"
    Just sum over all possible choices of the $k$ roots.

Define a $k$-spanning forest as a spanning subgraph of the graph that has $k$ connected components and no cycle.

???+ note "Corollary 4"
    Let $\mathcal T_k(G)$ be the set of $k$-spanning forests of an undirected graph $G$, and $P(x)=\det(xI-L(G))$ the characteristic polynomial of its Laplacian matrix. Then
    
    $$
    \sum_{T\in\mathcal T_k(G)}w(T)Q(T) = (-1)^{n-k}[x^k]P(x).
    $$
    
    Here $Q(T)$ is the product of the numbers of vertices of the connected components of the forest $T$. In particular, when $k=1$ we have $Q(T)=n$, hence
    
    $$
    n\sum_{T\in\mathcal T(G)}w(T) = \lambda_1\lambda_2\cdots\lambda_{n-1}.
    $$

??? note "Proof"
    Following the proof of Corollary 2, we can apply Corollary 3 directly. Every root-directed forest of $k$ trees in the directed graph corresponds to a $k$-spanning forest in the undirected graph. However, since every $k$-spanning forest $T$ has $Q(T)$ ways to choose its roots, it appears in $Q(T)$ root-directed forests of the directed graph.

## Applications

### Cayley's formula

???+ note "Corollary 5 (Cayley)"
    There are $n^{n-2}$ labeled unrooted trees of size $n$.

??? note "Proof"
    Equivalently, it suffices to show that the complete graph on $n$ vertices has $n^{n-2}$ spanning trees. To this end, write down the Laplacian matrix
    
    $$
    L(G) = \left(\begin{matrix} n-1 & -1 & \cdots & -1 \\ -1 & n-1 & \cdots & -1 \\ \vdots & \vdots & \ddots & \vdots \\ -1 & -1 & \cdots & n-1  \end{matrix}\right)_{n\times n}.
    $$
    
    Computing any of its principal minors gives
    
    $$
    \det(nI_{n-1}-{\bf 1}{\bf 1}^T) = n^{n-1}\det(I_{n-1}-n^{-1}{\bf 1}{\bf 1}^T) = n^{n-1}(1-n^{-1}{\bf 1}^T{\bf 1}) = n^{n-1}(1-(n-1)/n) = n^{n-2}.
    $$
    
    Applying Theorem 1 yields the result.

### BEST theorem

Prerequisites: [Eulerian graphs](./euler.md)

This theorem relates the number of Eulerian circuits of a directed Eulerian graph to the number of its root-directed arborescences, thereby solving the problem of counting Eulerian circuits in directed graphs. Note that counting Eulerian circuits in an arbitrary undirected graph is #P-complete.

When implementing this algorithm, one should first check whether the given graph is Eulerian, remove all vertices of degree zero, then build the graph and compute the number of root-directed arborescences, and obtain the count of Eulerian circuits from the BEST theorem. Note that if the Eulerian circuits are required to start at a given vertex, the answer must additionally be multiplied by the out-degree of that vertex, which amounts to choosing the first edge of the circuit.

Before proving the BEST theorem, we need the following fact.

???+ note "Property (criterion for a directed graph to have an Eulerian circuit)"
    A directed graph has an Eulerian circuit if and only if the vertices of nonzero degree are strongly connected and every vertex has equal out-degree and in-degree.

For Eulerian graphs, since out-degree and in-degree are equal, we may drop the superscripts and write $\mathrm{deg}(v)$. The BEST theorem can be stated as follows.

???+ note "Theorem 6 (BEST theorem)"
    Let $G$ be a directed Eulerian graph and $k$ any vertex. Then the number of distinct Eulerian circuits $\mathrm{ec}(G)$ of $G$ is
    
    $$
    \mathrm{ec}(G) = t^\mathrm{root}(G,k)\prod_{v\in V}(\deg (v) - 1)!.
    $$
    
    This also shows that for any two vertices $k, k'$ of an Eulerian graph $G$, $t^\mathrm{root}(G,k)=t^\mathrm{root}(G,k')$.

??? note "Proof"
    The idea of the proof is to establish a correspondence between Eulerian circuits starting at $k$ and pairs consisting of a root-directed arborescence with root $k$ together with an ordering of the outgoing edges at every vertex. Once the Eulerian circuit is required to start from $k$, the count to be proved should equal
    
    $$
    \mathrm{deg}(k)\mathrm{ec}(G) = t^\mathrm{root}(G,k)\deg(k)!\prod_{v\neq k}(\deg (v) - 1)!.
    $$
    
    The construction corresponding to the combinatorial meaning of this count is as follows. For an Eulerian circuit starting at $k$, according to the order in which the edges appear in the circuit, we can construct
    
    -   a root-directed arborescence with root $k$, formed by the last outgoing edge at every non-root vertex, i.e. $t^\mathrm{root}(G,k)$,
    -   the ordering of all outgoing edges at the root $k$, i.e. $\mathrm{deg}(k)!$, and
    -   the ordering of all outgoing edges except the last one at every non-root vertex $v\neq k$, i.e. $(\mathrm{deg}(v)-1)!$.
    
    We now show that the map given by this construction is a bijection.
    
    On the one hand, given an Eulerian circuit, we must prove that the last outgoing edges of all non-root vertices form a root-directed arborescence. By construction, every non-root vertex in the tree indeed has exactly one outgoing edge, so it suffices to prove that these edges do not form a cycle. Notice that if we order all vertices by the time of their last occurrence in the Eulerian circuit, the last outgoing edge of a non-root vertex necessarily points to a vertex strictly later in this order. If there were a cycle, it would contain a latest vertex; since it lies on the cycle, it points to a vertex that is not later, contradicting the above. Hence the last outgoing edges of the non-root vertices necessarily form a root-directed arborescence.
    
    On the other hand, given any root-directed arborescence and orderings of the remaining outgoing edges, we can recover an Eulerian circuit such that the construction above yields the given arborescence and orderings. To do so, start from the root $k$; whenever we arrive at a vertex, according to the given ordering of outgoing edges at that vertex, choose the earliest not-yet-used outgoing edge as the next edge of the Eulerian circuit; if all outgoing edges in the ordering at this vertex have been used, choose the outgoing edge of this vertex in the root-directed arborescence as the next edge. Since the graph is Eulerian, every vertex has in-degree equal to out-degree, so this process cannot terminate at a non-root vertex, i.e. the resulting walk is indeed a circuit. To prove that the resulting walk is a valid Eulerian circuit, it suffices to prove that this process traverses all edges.
    
    If it does not, there must be some vertex $v$ with some outgoing edge not traversed. Consider vertex $v$. Vertex $v$ cannot be the root, because the process ends at the root, and if the root still had an outgoing edge left, this would contradict the termination of the process. So $v$ is not the root. According to the process described above, as long as a non-root vertex $v$ has any outgoing edge left, its tree edge $e$ must also be left. Write $e=(v,u)$. Since some incoming edge of $u$ has not been traversed, and the out-degree of $u$ equals its in-degree, some outgoing edge of $u$ must not have been traversed. We can then examine vertex $u$ similarly. This reasoning moves the examined vertex from $v$ to $u$, i.e. one step toward the root along the arborescence. By induction, some outgoing edge of the root $k$ must then be untraversed. We have already shown this is impossible, so we get a contradiction. This shows that the walk obtained in the previous paragraph is indeed a valid Eulerian circuit.
    
    One can verify that both maps are injective, so they must both be bijections. This proves the theorem.

## Implementation

Write down the Laplacian matrix of the graph, delete one row and one column, and compute the determinant of the resulting matrix. The determinant can be computed by Gaussian elimination.

For example, the number of spanning trees of a square (a 4-cycle):

$$
\begin{pmatrix}
2 & 0 & 0 & 0 \\
0 & 2 & 0 & 0 \\
0 & 0 & 2 & 0 \\
0 & 0 & 0 & 2 \end{pmatrix}-\begin{pmatrix}
0 & 1 & 0 & 1 \\
1 & 0 & 1 & 0 \\
0 & 1 & 0 & 1 \\
1 & 0 & 1 & 0 \end{pmatrix}=\begin{pmatrix}
2 & -1 & 0 & -1 \\
-1 & 2 & -1 & 0 \\
0 & -1 & 2 & -1 \\
-1 & 0 & -1 & 2 \end{pmatrix}
$$

$$
\begin{vmatrix}
2 & -1 & 0 \\
-1 & 2 & -1 \\
0 & -1 & 2 \end{vmatrix} = 4
$$

This can be solved by Gaussian elimination in $O(n^3)$ time.

??? note "Implementation"
    ```cpp
    #include <algorithm>
    #include <cmath>
    #include <cstdlib>
    #include <cstring>
    #include <iostream>
    using namespace std;
    constexpr double eps = 1e-7;
    
    struct matrix {
      static constexpr int MAXN = 20;
      int n, m;
      double mat[MAXN][MAXN];
    
      matrix() { memset(mat, 0, sizeof(mat)); }
    
      void print() {
        cout << "MATRIX " << n << " " << m << endl;
        for (int i = 0; i < n; i++) {
          for (int j = 0; j < m; j++) {
            cout << mat[i][j] << "\t";
          }
          cout << endl;
        }
      }
    
      void random(int n) {
        this->n = n;
        this->m = n;
        for (int i = 0; i < n; i++)
          for (int j = 0; j < n; j++) mat[i][j] = rand() % 100;
      }
    
      void initSquare() {
        this->n = 4;
        this->m = 4;
        memset(mat, 0, sizeof(mat));
        mat[0][1] = mat[0][3] = -1;
        mat[1][0] = mat[1][2] = -1;
        mat[2][1] = mat[2][3] = -1;
        mat[3][0] = mat[3][2] = -1;
        mat[0][0] = mat[1][1] = mat[2][2] = mat[3][3] = 2;
        this->n--;  // remove one row
        this->m--;  // remove one column
      }
    
      double gauss() {
        double ans = 1;
        for (int i = 0; i < n; i++) {
          int sid = i;
          for (int j = i + 1; j < n; j++)
            if (abs(mat[j][i]) > abs(mat[sid][i])) sid = j;
          if (abs(mat[sid][i]) <= eps) return 0;
          if (sid != i) {
            for (int j = 0; j < n; j++) swap(mat[sid][j], mat[i][j]);
            ans = -ans;
          }
          for (int j = i + 1; j < n; j++) {
            double ratio = mat[j][i] / mat[i][i];
            for (int k = 0; k < n; k++) {
              mat[j][k] -= mat[i][k] * ratio;
            }
          }
        }
        for (int i = 0; i < n; i++) ans *= mat[i][i];
        return ans;
      }
    };
    
    int main() {
      srand(1);
      matrix T;
      // T.random(2);
      T.initSquare();
      T.print();
      double ans = T.gauss();
      T.print();
      cout << ans << endl;
    }
    ```

## Example problems

???+ note "Example 1: [\"HEOI2015\" Little Z's Rooms](https://loj.ac/problem/2122)"
    **Solution.** A direct application of the matrix-tree theorem. Treat every empty room as a node, build the graph from the input, obtain the Laplacian matrix $L$, delete any $i$-th row and $i$-th column of $L$, and compute the determinant of this minor. The determinant is computed by Gaussian elimination to upper triangular form followed by multiplying the diagonal. In this problem, Gaussian elimination has to be performed over $\mathbb{Z}/10^9\mathbb{Z}$, which can be done with the Euclidean algorithm (repeated division) instead of inverses.

???+ note "Example 2: [\"FJOI2007\" Wheel Virus](https://www.luogu.com.cn/problem/P2144)"
    **Solution.** This problem has many solutions; the matrix-tree theorem is the most direct one. For input $n$, its Laplacian matrix of order $n+1$ is easily written as:
    
    $$
    L_n = \begin{bmatrix}
    n&  -1&  -1&  -1&  \cdots&  -1&  -1\\
    -1&  3&  -1&  0&  \cdots&  0&  -1\\
    -1&  -1&  3&  -1&  \cdots&  0&  0\\
    -1&  0&  -1&  3&  \cdots&  0&  0\\
    \vdots&  \vdots&  \vdots&  \vdots&  \ddots&  \vdots&  \vdots\\
    -1&  0&  0&  0&  \cdots&  3&  -1\\
    -1&  -1&  0&  0&  \cdots&  -1&  3\\
    \end{bmatrix}_{n+1}
    $$
    
    Compute the determinant of its minor of order $n$; all that remains is big-integer arithmetic.

??? note "Example 2+"
    Strengthen the data of Example 2: require $n\leq 100000$, but with the answer taken modulo 1000007. (Solving this requires some linear algebra.)
    
    **Solution.** Derive a recurrence and then use fast matrix exponentiation.
    
    Derivation of the recurrence:
    
    Notice that the matrix obtained from $L_n$ by deleting row 1 and column 1 is very regular, so we are actually computing the determinant of the matrix
    
    $$
    M_n = \begin{bmatrix}
    3&  -1&  0&  \cdots&  0&  -1\\
    -1&  3&  -1&  \cdots&  0&  0\\
    0&  -1&  3&  \cdots&  0&  0\\
    \vdots&  \vdots&  \vdots&  \ddots&  \vdots&  \vdots\\
    0&  0&  0&  \cdots&  3&  -1\\
    -1&  0&  0&  \cdots&  -1&  3\\
    \end{bmatrix}_{n}
    $$
    
    Expanding the determinant of $M_n$ along the first column, we get
    
    $$
    \det M_n = 3\det \begin{bmatrix}
    3&  -1&  \cdots&  0&  0\\
    -1&  3&  \cdots&  0&  0\\
    \vdots&  \vdots&  \ddots&  \vdots&  \vdots\\
    0&  0&  \cdots&  3&  -1\\
    0&  0&  \cdots&  -1&  3\\
    \end{bmatrix}_{n-1} + \det\begin{bmatrix}
    -1&  0&  \cdots&  0&  -1\\
    -1&  3&  \cdots&  0&  0\\
    \vdots&  \vdots&  \ddots&  \vdots&  \vdots\\
    0&  0&  \cdots&  3&  -1\\
    0&  0&  \cdots&  -1&  3\\
    \end{bmatrix}_{n-1} + (-1)^n \det\begin{bmatrix}
    -1&  0&  \cdots&  0&  -1\\
    3&  -1&  \cdots&  0&  0\\
    -1&  3&  \cdots&  0&  0\\
    \vdots&  \vdots&  \ddots&  \vdots&  \vdots\\
    0&  0&  \cdots&  3&  -1\\
    \end{bmatrix}_{n-1}
    $$
    
    Denote the determinants of these three matrices by $d_{n-1}, a_{n-1}, b_{n-1}$.  
    Notice that $d_n$ is a tridiagonal determinant; a similar expansion gives the recurrence $d_n=3d_{n-1}-d_{n-2}$. Similarly, by expansion we get $a_{n-1}=-d_{n-2}-1$ and $(-1)^n b_{n-1}=-d_{n-2}-1$.  
    Substituting these recurrences into the expression above, we get:
    
    $$
    \det M_n = 3d_{n-1}-2d_{n-2}-2
    $$
    
    $$
    d_n = 3d_{n-1}-d_{n-2}
    $$
    
    So we guess that $\det M_n$ also satisfies a non-homogeneous second-order linear recurrence. The method of undetermined coefficients gives the final recurrence
    
    $$
    \det M_n = 3\det M_{n-1} - \det M_{n-2} + 2
    $$
    
    Rewriting it as $(\det M_n+2) = 3(\det M_{n-1}+2) - (\det M_{n-2} + 2)$, the answer follows by fast matrix exponentiation.

???+ note "Example 3: [\"BZOJ3659\" WHICH DREAMED IT](https://hydro.ac/p/bzoj-P3659)"
    **Solution.** This problem is a direct application of the BEST theorem, but note that since the statement says "two ways of completing the task are considered different if and only if the keys are used in a different order", for every Eulerian circuit room 1 may start along any of its outgoing edges, so the answer must additionally be multiplied by the out-degree of room 1.

???+ note "Example 4: [\"Joint Provincial Selection 2020 A\" Homework](https://loj.ac/p/3304)"
    **Solution.** First, Möbius inversion is needed to transform the problem into computing the sum of edge weights over all spanning trees; since this is not closely related to this article, it is omitted.
    
    Write the entries of the determinant as $w_ix+1$; the final answer is the coefficient of the linear term of the determinant. Indeed, the answer is really the sum over edges of (the number of spanning trees in which that edge is forced) $\times$ (the weight of that edge), and the edge that contributes the linear coefficient is exactly the forced edge. Terms of degree higher than one can be ignored; the complexity is $O(n^3)$.
    
    ["Beijing Provincial Training 2019" Counting Spanning Trees](https://www.luogu.com.cn/problem/P5296) is a more general case: compute the sum of $k$-th powers of the total weights of spanning trees; the determinant entries are constructed similarly, see the editorials on Luogu for details.

???+ note "Example 5: [AGC051D C4](https://atcoder.jp/contests/agc051/tasks/agc051_d)"
    **Solution.** Counting Eulerian circuits in an undirected graph is #P-complete, but the graph in this problem is quite simple: once we fix how many of the $S-T$ edges are directed from $S$ to $T$, the orientations of the other three groups of edges are determined, and then applying the BEST theorem directly gives an $O(a+b+c+d)$ solution.
