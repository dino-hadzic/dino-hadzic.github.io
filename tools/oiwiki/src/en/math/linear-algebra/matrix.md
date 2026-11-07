---
title: Matrices
---

This article introduces a very important concept of linear algebra, the matrix. It mainly covers the properties of matrices, operations on them, and some applications of matrix multiplication.

## Vectors and matrices

In linear algebra, vectors are divided into column vectors and row vectors.

???+ warning "Warning"
    In Taiwan the translations of the terms „列” and „行” are exactly the opposite of those used in mainland China. **OI Wiki** follows the mainland Chinese convention: „列” is translated as column and „行” as row.

The main object of study in linear algebra is the column vector; by convention, column vectors are denoted by bold lowercase letters. In linear algebra, where a large number of vectors and matrices are used, the vector arrow above the letter may be omitted in handwriting when no confusion arises.

Vectors are also special matrices. To write a row vector, the transpose symbol is written at the upper right of the bold lowercase letter. In linear algebra, a row vector usually represents an equation.

## Introduction

Matrices were introduced because of systems of linear equations. Like vectors, matrices embody the idea of "packing" data so that it can be processed together.

For example, take the system of linear equations:

$$
\begin{equation}
    \begin{cases}
        7x_1+8x_2+9x_3=13 \\
        4x_1+5x_2+6x_3=12 \\
        x_1+2x_2+3x_3=11
    \end{cases}
\end{equation}
$$

Matrices are usually written with parentheses or square brackets. Extracting the coefficients above, we can write the system as a matrix multiplication:

$$
\begin{equation}
    \begin{pmatrix}
        7 & 8 & 9 \\
        4 & 5 & 6 \\
        1 & 2 & 3
    \end{pmatrix}\begin{pmatrix}
        x_1 \\ x_2 \\ x_3
    \end{pmatrix}=\begin{pmatrix}
      13 \\ 12 \\ 11
    \end{pmatrix}
\end{equation}
$$

Abbreviated as:

$$
Ax=b
$$

That is, the column vector of unknowns x is multiplied on the left by a matrix A, giving the column vector b. This expression can be regarded as the basic form of linear algebra.

The main computational model studied in linear algebra is the inner (dot) product. The inner product is the process of first multiplying and then adding: a row vector is multiplied on the left of a column vector, and the result is a number.

Matrix multiplication is an extension of the inner product. Matrix multiplication is equivalent to taking a row from the left matrix and a column from the right matrix, computing their inner product, and thus obtaining the corresponding entry of the result matrix; the mnemonic is "row on the left, column on the right".

When the object of study is the column vector on the right, matrix multiplication amounts to multiplying the column vector on the left. From the point of view of left multiplication, a matrix is a transformation of column vectors: each column vector of the right matrix in the product is transformed, yielding the corresponding column vector of the result matrix.

A matrix can transform a single column vector, it can transform a set of column vectors "packed" together, and it can even transform the whole space, that is, all column vectors. When a matrix is viewed as a transformation of the whole space, it detaches itself from the space and becomes a pure transformation.

## Definition

For a matrix $A$, the main diagonal consists of the entries $A_{i,i}$.

The identity matrix is usually denoted by $I$; it has ones on the main diagonal and zeros elsewhere.

### Matrices of the same type

Two matrices with the same number of rows and the same number of columns are called matrices of the same type.

### Square matrix

A matrix whose number of rows equals its number of columns is called a square matrix. A square matrix is a special kind of matrix. The customary phrase "matrix of order $n$" actually refers to a square matrix of order $n$. Square matrices of the same order are matrices of the same type.

When studying systems of equations, sets of vectors, and the rank of a matrix, general matrices are used. When studying eigenvalues and eigenvectors, and quadratic forms, square matrices are used.

#### Main diagonal

The entries of a square matrix whose row index equals the column index form the main diagonal.

#### Symmetric matrix

If the entries of a square matrix are symmetric with respect to the main diagonal, that is, if for all $i$ and $j$ the entry in row $i$, column $j$ equals the entry in row $j$, column $i$, the square matrix is called a symmetric matrix.

#### Diagonal matrix

A square matrix whose entries outside the main diagonal are all $0$ is called a diagonal matrix and is usually written as:

$$
\operatorname{diag}\{\lambda_1,\cdots,\lambda_n\}
$$

where $\lambda_1,\cdots,\lambda_n$ are the entries on the main diagonal.

A diagonal matrix is a symmetric matrix.

If all entries of a diagonal matrix are $1$, it is called the identity matrix and denoted by $I$. Whenever the multiplication is possible, regardless of shape, any matrix multiplied by the identity matrix remains unchanged.

#### Triangular matrix

If all entries of a square matrix below the main diagonal (lower left) are $0$, it is called an upper triangular matrix. If all entries above the main diagonal (upper right) are $0$, it is called a lower triangular matrix.

The product of two upper (lower) triangular matrices is again an upper (lower) triangular matrix. If none of the diagonal entries is $0$, an upper (lower) triangular matrix is invertible, and its inverse is also upper (lower) triangular.

#### Unit triangular matrix

If all diagonal entries of an upper triangular matrix $A$ are $1$, then $A$ is called a unit upper triangular matrix. If all diagonal entries of a lower triangular matrix $A$ are $1$, then $A$ is called a unit lower triangular matrix.

The product of two unit upper (lower) triangular matrices is again a unit upper (lower) triangular matrix, and the inverse of a unit upper (lower) triangular matrix is also a unit upper (lower) triangular matrix.

## Operations

### Linear operations on matrices

The linear operations on matrices are addition, subtraction, and scalar multiplication; all of them are performed entry by entry. Only matrices of the same type can be added or subtracted.

### Transpose of a matrix

The transpose of a matrix is denoted by writing the transpose symbol "T" at the upper right of the matrix; it means swapping the rows and columns of the matrix.

A symmetric matrix remains unchanged under transposition.

### Matrix multiplication

Matrix multiplication is a generalization of the inner product of vectors.

The product of two matrices is meaningful only when the number of columns of the first matrix equals the number of rows of the second.

Let $A$ be a $P \times M$ matrix, $B$ an $M \times Q$ matrix, and let the matrix $C$ be the product of $A$ and $B$;

then the entry in row $i$, column $j$ of $C$ can be written as:

$$
C_{i,j} = \sum_{k=1}^MA_{i,k}B_{k,j}
$$

In matrix multiplication, the number in row $i$, column $j$ of the result $C$ is obtained by **multiplying and then adding** the $M$ numbers of row $i$ of $A$ with the $M$ numbers of column $j$ of $B$. This **multiplying and then adding** is exactly the inner product of vectors. The number in row $i$, column $j$ of the product matrix is exactly the inner product of the $i$-th row vector of the factor $A$ and the $j$-th column vector of the factor $B$; the mnemonic is **row on the left, column on the right**.

The vectors studied in linear algebra are mostly column vectors; with this way of defining matrix multiplication, one often studies left multiplication, i.e., multiplying a column vector by a matrix on the left. Here one can also see the idea of “batch processing”: many inner products of vectors are handled at once.

Matrix multiplication is associative, but in general it is not commutative.

Using associativity, matrix multiplication can be optimized with the idea of [binary exponentiation](../binary-exponentiation.md).

In contests, since linear recurrences can be expressed in the form of matrix multiplication, matrix exponentiation is also commonly used to compute a particular term of a linearly recurrent sequence.

#### Optimization

First of all, for relatively small matrices one can consider manually unrolling the loops to reduce the constant factor.

The loops can be rearranged to improve spatial locality; such an optimization does not change the time complexity of matrix multiplication, but it yields a constant-factor improvement.

```cpp
// Taking the reference code below as an example
mat operator*(const mat& T) const {
  mat res;
  for (int i = 0; i < sz; ++i)
    for (int j = 0; j < sz; ++j)
      for (int k = 0; k < sz; ++k) {
        res.a[i][j] += mul(a[i][k], T.a[k][j]);
        res.a[i][j] %= MOD;
      }
  return res;
}

// is worse than
mat operator*(const mat& T) const {
  mat res;
  int r;
  for (int i = 0; i < sz; ++i)
    for (int k = 0; k < sz; ++k) {
      r = a[i][k];
      for (int j = 0; j < sz; ++j)
        res.a[i][j] += T.a[k][j] * r, res.a[i][j] %= MOD;
    }
  return res;
}
```

### Inverse of a square matrix

The inverse matrix $P$ of a square matrix $A$ is the matrix such that $A \times P = I$.

The inverse matrix does not necessarily exist. If it exists, it can be computed with [Gaussian elimination](../numerical/gauss.md).

### Determinant of a square matrix

The determinant is an operation on square matrices.

## Reference code

Generally, a matrix can be simulated with a two-dimensional array.

```cpp
struct mat {
  LL a[sz][sz];

  mat() { memset(a, 0, sizeof a); }

  mat operator-(const mat& T) const {
    mat res;
    for (int i = 0; i < sz; ++i)
      for (int j = 0; j < sz; ++j) {
        res.a[i][j] = (a[i][j] - T.a[i][j]) % MOD;
      }
    return res;
  }

  mat operator+(const mat& T) const {
    mat res;
    for (int i = 0; i < sz; ++i)
      for (int j = 0; j < sz; ++j) {
        res.a[i][j] = (a[i][j] + T.a[i][j]) % MOD;
      }
    return res;
  }

  mat operator*(const mat& T) const {
    mat res;
    int r;
    for (int i = 0; i < sz; ++i)
      for (int k = 0; k < sz; ++k) {
        r = a[i][k];
        for (int j = 0; j < sz; ++j)
          res.a[i][j] += T.a[k][j] * r, res.a[i][j] %= MOD;
      }
    return res;
  }

  mat operator^(LL x) const {
    mat res, bas;
    for (int i = 0; i < sz; ++i) res.a[i][i] = 1;
    for (int i = 0; i < sz; ++i)
      for (int j = 0; j < sz; ++j) bas.a[i][j] = a[i][j] % MOD;
    while (x) {
      if (x & 1) res = res * bas;
      bas = bas * bas;
      x >>= 1;
    }
    return res;
  }
};
```

## Two views of a system of linear equations

There are two ways to look at the matrix A, or the transformation A.

The first view: by rows, looking at each row of A. In this way A is regarded as a system of equations, which leads to solving equations by elimination.

The second view: by columns, looking at each column of A. The matrix A itself is made up of column vectors. Then the transformation A is regarded as a set of column vectors, and x are the unknown coefficients; we ask whether this set of column vectors in A can be combined, with suitable unknowns, to produce the column vector b.

For example, the example at the beginning of the article becomes:

$$
\begin{equation}
    \begin{pmatrix}
        7 \\ 4 \\ 1
    \end{pmatrix}x_1+\begin{pmatrix}
        8 \\ 5 \\ 2
    \end{pmatrix}x_2+\begin{pmatrix}
        9 \\ 6 \\ 3
    \end{pmatrix}x_3=\begin{pmatrix}
      13 \\ 12 \\ 11
    \end{pmatrix}
\end{equation}
$$

Solving the system becomes the question of whether, by adjusting the three coefficients x, the three given basis vectors can be combined into the result vector.

The column view is more novel than the row view. From the column perspective, linear independence and linear dependence can be studied.

## Applications of matrix multiplication

### Speeding up recurrences with matrices

Take the [Fibonacci sequence](../combinatorics/fibonacci.md) as an example. In the Fibonacci sequence, $F_1 = F_2 = 1$, $F_i = F_{i - 1} + F_{i - 2}(i \geq 3)$.

If a problem asks for the value of the $n$-th term of the Fibonacci sequence, the simplest method is to compute it directly by recurrence. But if $n$ is of the order of $10^{18}$, the recurrence is no longer feasible; then we can consider speeding up the recurrence with matrices.

According to the [matrix form of the recurrence](../combinatorics/fibonacci.md#matrix-form) of the Fibonacci sequence:

$$
\begin{bmatrix}
  F_{n-1} & F_{n-2}
\end{bmatrix} \begin{bmatrix}
  1 & 1 \\
  1 & 0
\end{bmatrix} = \begin{bmatrix}
  F_n & F_{n-1}
\end{bmatrix}
$$

Define the initial matrix $\text{ans} = \begin{bmatrix}F_2 & F_1\end{bmatrix} = \begin{bmatrix}1 & 1\end{bmatrix}, \text{base} = \begin{bmatrix} 1 & 1 \\ 1 & 0 \end{bmatrix}$. Then $F_n$ equals the entry in the first row and first column of the matrix $\text{ans} \text{base}^{n-2}$, that is, the entry in the first row and first column of $\begin{bmatrix}1 & 1\end{bmatrix} \begin{bmatrix} 1 & 1 \\ 1 & 0 \end{bmatrix}^{n-2}$.

???+ warning "Note"
    Matrix multiplication is not commutative, so it must never be written as "the entry in the first row and first column of $\begin{bmatrix} 1 & 1 \\ 1 & 0 \end{bmatrix}^{n-2} \begin{bmatrix}1 & 1\end{bmatrix}$". Also, for $n \leq 2$ it suffices to output $1$ directly, without performing matrix exponentiation.

Why do we multiply by the $n-2$-th power of the matrix $\text{base}$ rather than the $n$-th? Because $F_1, F_2$ can be obtained without any matrix multiplication. In other words, after just one multiplication we already have $F_3$. If it is still unclear why the exponent is $n-2$, we recommend working it out by hand.

Below is sample code (the core part) that computes the $n$-th Fibonacci number modulo $10^9+7$.

```cpp
constexpr int mod = 1000000007;

struct Matrix {
  int a[3][3];

  Matrix() { memset(a, 0, sizeof a); }

  Matrix operator*(const Matrix &b) const {
    Matrix res;
    for (int i = 1; i <= 2; ++i)
      for (int j = 1; j <= 2; ++j)
        for (int k = 1; k <= 2; ++k)
          res.a[i][j] = (res.a[i][j] + a[i][k] * b.a[k][j]) % mod;
    return res;
  }
} ans, base;

void init() {
  base.a[1][1] = base.a[1][2] = base.a[2][1] = 1;
  ans.a[1][1] = ans.a[1][2] = 1;
}

void qpow(int b) {
  while (b) {
    if (b & 1) ans = ans * base;
    base = base * base;
    b >>= 1;
  }
}

int main() {
  int n = read();
  if (n <= 2) return puts("1"), 0;
  init();
  qpow(n - 2);
  println(ans.a[1][1] % mod);
}
```

Here is a slightly more complicated example.

$$
\begin{gathered}
f_{1} = f_{2} = 0\\
f_{n} = 7f_{n-1}+6f_{n-2}+5n+4\times 3^n
\end{gathered}
$$

We notice that $f_n$ depends on $f_{n-1}, f_{n-2}, n$, so we try to construct a matrix describing the state.

However, if the matrix contains only these three entries $\begin{bmatrix}f_n& f_{n-1}& n\end{bmatrix}$, it is hard to construct the transition equation, because exponentiation and $+1$ cannot be described by a matrix.

So we construct a larger matrix.

$$
\begin{bmatrix}f_n& f_{n-1}& n& 3^n & 1\end{bmatrix}
$$

We want to construct a recurrence matrix that transitions to

$$
\begin{bmatrix}
f_{n+1}& f_{n}& n+1& 3^{n+1} & 1
\end{bmatrix}
$$

The transition matrix is

$$
\begin{bmatrix}
7 & 1 & 0 & 0 & 0\\
6 & 0 & 0 & 0 & 0\\
5 & 0 & 1 & 0 & 0\\
12 & 0 & 0 & 3 & 0\\
5 & 0 & 1 & 0 & 1
\end{bmatrix}
$$

### Expressing updates with matrices

???+ note "[「THUSCH 2017」大魔法师 (The Great Magician)](https://loj.ac/p/2980)"
    The great magician Little L has made $n$ magic crystal balls; each ball has energy values of three attributes: water, fire, and earth. Little L lines up these $n$ balls on the ground from front to back and begins today's magic show.
    
    We denote by $A_i,\ B_i,\ C_i$ the water, fire, and earth energy of the $i$-th ball from the front (indices start at $1$).
    
    Little L plans to cast $m$ spells. Each time, he chooses an interval $[l, r]$ and then casts one of the following $7$ kinds of spells, grouped into $3$ categories:
    
    1.  Magic excitation: the energy of a **specific attribute** of every ball in the interval bursts, thereby strengthening the energy of another **specific attribute**. Specifically, there are three possible forms:
    
        -   the fire element excites the water energy: $A_i = A_i + B_i$.
        -   the earth element excites the fire energy: $B_i = B_i + C_i$.
        -   the water element excites the earth energy: $C_i = C_i + A_i$.
    
            **Note that strengthening the energy of one attribute does not change the energy of the other attribute; for example, $A_i = A_i + B_i$ does not increase or decrease $B_i$.**
    2.  Magic enhancement: Little L waves his staff and spends $v$ points of his own mana to change the energy of a **specific attribute** of every ball in the interval. Specifically, there are three possible forms:
    
        -   the fire energy is increased by a constant: $A_i = A_i + v$.
        -   the water energy is multiplied: $B_i=B_i \cdot v$.
        -   the earth energy is absorbed and fused: $C_i = v$.
    3.  Magic release: Little L gathers the energy of all balls in the interval, fuses them into a new crystal ball, and gives it to the audience. The energy of each attribute of the resulting ball equals the algebraic sum of the corresponding energies of all balls in the interval. **Note that the process of magic release does not actually change the energy of the balls in the interval.**
    
    It is worth mentioning that the balls Little L makes and fuses are made of custom crystals from the OI factory, so these balls have an energy threshold of $998244353$. When the energy of some attribute of a ball becomes greater than or equal to this threshold, the energy is automatically taken modulo the threshold, preventing the ball from exploding.
    
    Little W, Little L's (only) spectator, watched the whole show and received every ball Little L fused during the show. Little W wants to know the energy values of the three attributes of these balls.

Since associativity and distributivity hold for matrices, point updates naturally generalize to intervals: after deriving the matrices, it suffices to maintain the product of the matrices over an interval with a segment tree.

Below are several examples.

The transition for $A_i = A_i + v$

$$
\begin{bmatrix}
A & B & C & 1
\end{bmatrix}
\begin{bmatrix}
1 & 0 & 0 & 0\\
0 & 1 & 0 & 0\\
0 & 0 & 1 & 0\\
v & 0 & 0 & 1\\
\end{bmatrix}=
\begin{bmatrix}
A+v & B & C & 1\\
\end{bmatrix}
$$

The transition for $B_i=B_i \cdot v$

$$
\begin{bmatrix}
A & B & C & 1
\end{bmatrix}
\begin{bmatrix}
1 & 0 & 0 & 0\\
0 & v & 0 & 0\\
0 & 0 & 1 & 0\\
0 & 0 & 0 & 1\\
\end{bmatrix}=
\begin{bmatrix}
A & B \cdot v & C & 1\\
\end{bmatrix}
$$

???+ note "[「LibreOJ 6208」树上询问 (Queries on a Tree)](https://loj.ac/p/6208)"
    There is a tree with $n$ nodes, rooted at node $1$. Each node has two weights $k_i, t_i$, both initially $0$.
    
    Three kinds of operations are given:
    
    1.  operation $\operatorname{Add}( x , d )$: for all nodes on the path from $x$ to the root, $k_i\leftarrow k_i + d$
    2.  operation $\operatorname{Mul}( x , d )$: for all nodes on the path from $x$ to the root, $t_i\leftarrow t_i + d \times k_i$
    3.  operation $\operatorname{Query}( x )$: query the weight $t_x$ of node $x$
    
        $n,~m \leq 100000, ~-10 \leq d \leq 10$

Thinking about it directly, it is not easy to come up with how to push down the operations and maintain the information. But matrices can express it easily.

$$
\begin{aligned}
\begin{bmatrix}k & t & 1 \end{bmatrix}
\begin{bmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
d & 0 & 1
\end{bmatrix}
&=
\begin{bmatrix}k+d & t & 1 \end{bmatrix}\\
\begin{bmatrix}k & t & 1 \end{bmatrix}
\begin{bmatrix}
1 & d & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{bmatrix}
&=
\begin{bmatrix}k & t+d \times k & 1 \end{bmatrix}
\end{aligned}
$$

### Counting paths of fixed length

???+ note "Problem statement"
    Given a directed graph with $n$ vertices in which every edge has weight $1$, and an integer $k$, your task is to find, for every pair of vertices $(u,v)$, the number of paths of length $k$ from $u$ to $v$ (not necessarily simple, i.e., vertices or edges on the path may be visited several times).

We represent the directed graph by its adjacency matrix $G$ (for every edge $(u\to v)$ of the graph, set $G[u,v]=1$, and all other entries are $0$; if there are multiple edges, let $G[u,v]$ be the number of multiple edges). The algorithm below also works when the graph has self-loops.

Obviously, this adjacency matrix corresponds to the answer for $k=1$.

Suppose we know the matrix of the numbers of paths of length $k$, denoted $C_k$, and we want to find $C_{k+1}$. Obviously we have the DP transition

$$
C_{k+1}[i,j] = \sum_{p = 1}^{n} C_k[i,p] \cdot G[p,j]
$$

We can regard this as matrix multiplication, so the transition above can be described as

$$
C_{k+1} = C_k \cdot G
$$

Expanding this recurrence, we obtain

$$
C_k = \underbrace{G \cdot G \cdots G}_{k \text{ times}} = G^k
$$

To compute this matrix power, we can use the idea of fast exponentiation (binary exponentiation) and compute the result in $O(n^3 \log k)$.

### Shortest paths of fixed length

???+ note "Problem statement"
    You are given a weighted directed graph with $n$ vertices and an integer $k$. For every pair of vertices $(u,v)$, find the length of the shortest path from $u$ to $v$ that contains exactly $k$ edges. (The path is not necessarily simple, i.e., vertices or edges on the path may be visited several times.)

We again construct the adjacency matrix $G$ of the graph, where $G[i,j]$ denotes the weight of the edge from $i$ to $j$. If there is no edge between the vertices $i,j$, then $G[i,j]=\infty$. (In the case of multiple edges, take the minimum weight.)

Obviously the matrix above corresponds to the answer for $k=1$. We again assume that we know the answer for $k$, denoted by the matrix $L_k$. Now we want the answer for $k+1$. Obviously we have the transition

$$
L_{k+1}[i,j] = \min_{1\le p \le n} \left\{L_k[i,p] + G[p,j]\right\}
$$

In fact, we can draw an analogy with matrix multiplication: you notice that the transition above merely replaces the sum of products in matrix multiplication by addition followed by taking the minimum, so we define this operation as $\odot$, that is,

$$
A \odot B = C~~\Longleftrightarrow~~C[i,j]=\min_{1\le p \le n}\left\{A[i,p] + B[p,j]\right\}
$$

Thus we obtain

$$
L_{k+1} = L_k \odot G
$$

Expanding the recurrence gives

$$
L_k = \underbrace{G \odot \ldots \odot G}_{k\text{ times}} = G^{\odot k}
$$

We can still compute the expression above with matrix exponentiation, since the operation is obviously associative. The time complexity is $O(n^3 \log k)$.

### Counting paths / shortest paths of bounded length

The algorithms above apply only when the number of edges is fixed. However, we can improve the algorithm to handle the case where the number of edges is at most $k$. Specifically, consider the following problem:

???+ note "Problem statement"
    Given a directed graph with $n$ vertices whose edges have weight $1$, and an integer $k$, your task is to find, for every pair of vertices $(u,v)$, the number of paths from $u$ to $v$ of length at most $k$ (not necessarily simple, i.e., vertices or edges on the path may be visited several times).

For every vertex $v$ we create an auxiliary vertex $v'$ to record the answer, and add the two edges $(v,v')$ and $(v',v')$ to the graph. Then for a pair of vertices $(u,v)$, the number of paths from $u$ to $v$ with at most $k$ edges equals the number of paths from $u$ to $v'$ with exactly $k+1$ edges, because every path with $m(m \le k)$ edges $(p_0=u)\to p_1\to p_2 \to \dots \to p_{m-1} \to (p_m=v)$ corresponds one-to-one to a path with $k+1$ edges $(p_0=u)\to p_1 \to p_2 \to \dots \to p_{m-1} \to (p_m=v) \to v'  \to \dots \to v'$.

For the shortest path with at most $k$ edges, it suffices to add a self-loop of weight $0$ to every vertex.

## Exercises

-   [Luogu P1962 斐波那契数列 (Fibonacci Sequence)](https://www.luogu.com.cn/problem/P1962), the example above; same problem as POJ3070
-   [Luogu P1349 广义斐波那契数列 (Generalized Fibonacci Sequence)](https://www.luogu.com.cn/problem/P1349), the $\text{base}$ matrix needs a small change
-   [Luogu P1939【模板】矩阵加速（数列）(Template: Matrix Acceleration (Sequences))](https://www.luogu.com.cn/problem/P1939), the $\text{base}$ matrix becomes a $3 \times 3$ matrix, and the derivation is similar to the one above.

**Part of this page is translated from the blog post [Кратчайшие пути фиксированной длины, количества путей фиксированной длины](http://e-maxx.ru/algo/fixed_length_paths) and its English translation [Number of paths of fixed length/Shortest paths of fixed length](https://cp-algorithms.com/graph/fixed_length_paths.html). The Russian version is licensed under Public Domain + Leave a Link; the English version is licensed under CC-BY-SA 4.0.**
