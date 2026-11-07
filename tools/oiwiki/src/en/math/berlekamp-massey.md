---
title: Berlekamp–Massey algorithm
---

The Berlekamp–Massey algorithm is an algorithm for finding the shortest linear recurrence of a sequence. Given a sequence of length $n$ whose shortest recurrence has order $m$, the Berlekamp–Massey algorithm finds the shortest recurrence of every prefix of the sequence in $O(nm)$ time. In the worst case $m = O(n)$, so the worst-case complexity of the algorithm is $O(n^2)$.

### Definition

A recurrence of a sequence $\{a_0 \dots a_{n - 1} \}$ is defined as a sequence $\{r_0\dots r_m\}$ satisfying

$\sum_{j = 0} ^ m r_j a_{i - j} = 0, \forall i \ge m$

where $r_0 = 1$. The number $m$ is called the **order** of the recurrence.

The shortest recurrence of the sequence $\{a_i\}$ is the recurrence of minimum order.

### Method

Slightly differently from the definition above, here we define new recurrence coefficients $\{f_0 \dots f_{m - 1}\}$ satisfying:

$a_i = \sum_{j = 0} ^ {m - 1} f_j a_{i - j - 1}, \forall i \ge m$

It is easy to see that $f_i = -r_{i + 1}$, and the order $m$ is the same as in the previous definition.

We can find the recurrence incrementally: consider the terms of $\{a_i\}$ in order, and whenever the recurrence gives a wrong result, adjust the recurrence coefficients $\{f_i\}$. For convenience, we denote the shortest recurrence of the first $i$ terms by $F_i = \{f_{i, j}\}$.

Obviously $F_0 = \{\}$ initially. Suppose the recurrence coefficients $F_{i - 1}$ hold for the first $i - 1$ terms of the sequence $\{a_i\}$; then for the $i$-th term there are two cases:

1.  The recurrence coefficients also hold for $a_i$; then no adjustment is needed, and we simply set $F_i = F_{i - 1}$.
2.  The recurrence coefficients do not hold for $a_i$; then $F_{i - 1}$ has to be adjusted to obtain the new $F_i$.

Let $\Delta_i = a_i - \sum_{j = 0} ^ m f_{i - 1, j} a_{i - j - 1}$, i.e. the difference between $a_i$ and the result of the recurrence $F_{i - 1}$.

If this is the first time the recurrence coefficients are modified, then $a_i$ is the first nonzero term of the sequence. In this case we simply let $F_i$ consist of $i$ copies of $0$; obviously this is a valid shortest recurrence.

Otherwise, let $k$ be the number of terms of $\{a_i\}$ that had been considered at the time of the last modification of the recurrence coefficients. If there exists a sequence $G = \{g_0 \dots g_{m' - 1}\}$ satisfying

$\sum_{j = 0} ^ {m' - 1} g_j a_{i' - j - 1} = 0, \forall i' \in [m', i)$

and $\sum_{j = 0} ^ {m' - 1} g_j a_{i - j - 1} = \Delta_i$, then it is not hard to see that adding $F_k$ and $G$ term by term yields valid recurrence coefficients $F_i$.

Consider how to construct $G$. One feasible construction is

$G = \{0, 0, \dots, 0, \frac{\Delta_i}{\Delta_k}, -\frac{\Delta_i}{\Delta_k}F_{k-1}\}$

where there are $i - k - 1$ copies of $0$ in front in total, and the final $-\frac{\Delta_i}{\Delta_k} F_{k-1}$ means that every term of $F_{k-1}$ is multiplied by $-\frac{\Delta_i}{\Delta_k}$ and appended to the sequence.

It is easy to verify that then $\sum_{j = 0} ^ {m' - 1} g_j a_{i - j - 1} = \Delta_k \frac{\Delta_i}{\Delta_k} = \Delta_i$, so the $G$ constructed this way is valid. We simply assign to $F_i$ the term-by-term sum of $F_k$ and $G$.

If the recurrence $\{r_i\}$ in the sense of the original definition is required, simply negate all $\{f_j\}$ and insert $r_0 = 1$ at the beginning.

From the algorithm described above it can be seen that if the order of the shortest recurrence of the sequence is $m$, the complexity of the algorithm is $O(nm)$. In the worst case $m = O(n)$, so the worst-case complexity of the algorithm is $O(n^2)$.

When implementing the algorithm, since each adjustment of the recurrence coefficients only needs the recurrence coefficients $F_k$ from the previous adjustment, if only the shortest recurrence of the whole sequence is needed, we can store only the current recurrence coefficients and those from the last adjustment, for a space complexity of $O(n)$.

??? note "Reference implementation"
    ```cpp
    vector<int> berlekamp_massey(const vector<int> &a) {
      vector<int> v, last;  // v is the answer, 0-based, p is the module
      int k = -1, delta = 0;
    
      for (int i = 0; i < (int)a.size(); i++) {
        int tmp = 0;
        for (int j = 0; j < (int)v.size(); j++)
          tmp = (tmp + (long long)a[i - j - 1] * v[j]) % p;
    
        if (a[i] == tmp) continue;
    
        if (k < 0) {
          k = i;
          delta = (a[i] - tmp + p) % p;
          v = vector<int>(i + 1);
    
          continue;
        }
    
        vector<int> u = v;
        int val = (long long)(a[i] - tmp + p) * power(delta, p - 2) % p;
    
        if (v.size() < last.size() + i - k) v.resize(last.size() + i - k);
    
        (v[i - k - 1] += val) %= p;
    
        for (int j = 0; j < (int)last.size(); j++) {
          v[i - k + j] = (v[i - k + j] - (long long)val * last[j]) % p;
          if (v[i - k + j] < 0) v[i - k + j] += p;
        }
    
        if ((int)u.size() - i < (int)last.size() - k) {
          last = u;
          k = i;
          delta = a[i] - tmp;
          if (delta < 0) delta += p;
        }
      }
    
      for (auto &x : v) x = (p - x) % p;
      v.insert(v.begin(), 1);
    
      return v;  // $\forall i, \sum_{j = 0} ^ m a_{i - j} v_j = 0$
    }
    ```

The plain Berlekamp–Massey algorithm finds the shortest recurrence of a sequence with finitely many terms. If the sequence whose recurrence we want has infinitely many terms, but an upper bound on the order of the shortest recurrence is known, it suffices to take the first $2m$ terms of the sequence to obtain the shortest recurrence of the whole sequence. (Proof omitted.)

### Applications

Since the numerical stability of the Berlekamp–Massey algorithm is rather poor, it is rarely used for problems over the real numbers. For convenience of exposition, in the following we assume that all computations are carried out in the residue system modulo some prime $p$.

#### Shortest recurrence of a sequence of vectors or matrices

If we want the shortest recurrence of a sequence of vectors $\boldsymbol{v}_i$, let the dimension of the vectors be $n$; we can pick a random $n$-dimensional row vector $\mathbf u^T$ and compute the shortest recurrence of the scalar sequence $\{\boldsymbol{u}^T\boldsymbol{v}_i\}$. By the Schwartz–Zippel lemma, the two shortest recurrences coincide with probability at least $1 - \frac n p$.

Finding the shortest recurrence of a sequence of matrices $\{A_i\}$ is similar: if the matrices have size $n \times m$, it suffices to pick a random $1 \times n$ row vector $\mathbf u^T$ and a random $m \times 1$ column vector $\boldsymbol{v}$ and compute the shortest recurrence of the scalar sequence $\{\boldsymbol{u}^T A_i \boldsymbol{v}\}$. By the Schwartz–Zippel lemma we similarly obtain that the probability that the two coincide is at least $1 - \frac{n + m} p$.

#### Speeding up matrix exponentiation

Let $\boldsymbol{f}_i$ be an $n$-dimensional column vector and let the transition satisfy $\boldsymbol{f}_i = A \boldsymbol{f}_{i - 1}$. Then $\{\boldsymbol{f}_i\}$ is a linearly recurrent sequence of vectors of order at most $n$. (Proof omitted.)

We can compute $\boldsymbol{f}_0 \dots \boldsymbol{f}_{2n - 1}$ directly by brute force, then find the shortest recurrence of $\{\boldsymbol{f}_i\}$ by the method described above, and finally apply the [homogeneous linear recurrence with constant coefficients](./poly/linear-recurrence.md).

If the vector we want is $\boldsymbol{f}_m$, the complexity of the algorithm is $O(n^3 + n\log n \log m)$. If $A$ is a sparse matrix with only $k$ nonzero entries, the complexity can be reduced to $O(nk + n\log n \log m)$. However, since the algorithm needs at least $O(nk)$ time for preprocessing anyway, when the constraints are not tight one can also use the $O(n^2 \log m)$ linear recurrence algorithm, whose complexity is acceptable as well.

#### Minimal polynomial of a matrix

The minimal polynomial of a square matrix $A$ is the polynomial $f$ of minimum degree satisfying $f(A) = 0$.

In fact, the minimal polynomial is just the shortest recurrence of $\{A^i\}$, so it suffices to apply the Berlekamp–Massey algorithm directly. If $A$ is a square matrix of order $n$, the degree of the minimal polynomial is obviously at most $n$.

The bottleneck is computing $A^i$, since multiplying matrices directly at every step would give a complexity of $O(n^4)$. However, when finding the shortest recurrence of a sequence of matrices we actually find the shortest recurrence of $\{\boldsymbol{u}^T A^i \boldsymbol{v}\}$, so it suffices to compute $A^i \boldsymbol{v}$.

If $A$ has $k$ nonzero entries, the complexity is $O(kn + n^2)$.

#### Determinant of a sparse matrix

If we can compute the characteristic polynomial of a square matrix $A$, its constant term multiplied by $(-1)^n$ is the determinant. However, the minimal polynomial is not necessarily the characteristic polynomial.

In fact, if we multiply $A$ by a random diagonal matrix $B$, the minimal polynomial of $AB$ is the characteristic polynomial with probability at least $1 - \frac {2n^2 - n} p$. At the end we just divide by $\text{det}\;B$.

If $A$ is a square matrix of order $n$ with $k$ nonzero entries, the complexity is $O(kn + n ^ 2)$.

#### Rank of a sparse matrix

Let $A$ be an $n\times m$ matrix. First pick a random $n\times n$ diagonal matrix $P$ and a random $m\times m$ diagonal matrix $Q$, then compute the minimal polynomial of $Q A P A^T Q$.

In fact, no matrix multiplication is needed: when computing the minimal polynomial we multiply $Q A P A^T Q$ by a vector, so we simply multiply these matrices into the vector one after another. The answer is the degree of the minimal polynomial after all factors $x$ have been removed from it.

If $A$ has $k$ nonzero entries and $n \le m$, the complexity is $O(kn + n ^ 2)$.

#### Solving sparse systems of equations

**Problem**: we are given $A \mathbf x = \mathbf b$, where $A$ is a **full-rank** sparse $n \times n$ matrix and $\mathbf b$ and $\mathbf x$ are $1\times n$ column vectors. $A, \mathbf b$ are known, and we need to solve for $x$ in complexity below $n^\omega$.

**Method**: obviously $\mathbf x = A^{-1} \mathbf b$. If we can find the shortest recurrence $\{r_0 \dots r_{m - 1}\}$ ($m \le n$) of $\{A^i \mathbf b\}$ ($i \ge 0$), then we have the result

$A^{-1} \mathbf b = -\frac 1 {r_{m - 1}} \sum_{i = 0} ^ {m - 2} A^i \mathbf b r_{m - 2 - i}$

(Proof omitted.)

Since $A$ is a sparse matrix, we just compute $\mathbf b \dots A^{2n - 1} \mathbf b$ directly by definition.

Likewise, if $A$ has $k$ nonzero entries, the complexity is $O(kn + n^2)$.

??? note "Reference implementation"
    ```cpp
    vector<int> solve_sparse_equations(const vector<tuple<int, int, int>> &A,
                                       const vector<int> &b) {
      int n = (int)b.size();  // 0-based
    
      vector<vector<int>> f({b});
    
      for (int i = 1; i < 2 * n; i++) {
        vector<int> v(n);
        auto &u = f.back();
    
        for (auto [x, y, z] : A)  // [x, y, value]
          v[x] = (v[x] + (long long)u[y] * z) % p;
    
        f.push_back(v);
      }
    
      vector<int> w(n);
      mt19937 gen;
      for (auto &x : w) x = uniform_int_distribution<int>(1, p - 1)(gen);
    
      vector<int> a(2 * n);
      for (int i = 0; i < 2 * n; i++)
        for (int j = 0; j < n; j++) a[i] = (a[i] + (long long)f[i][j] * w[j]) % p;
    
      auto c = berlekamp_massey(a);
      int m = (int)c.size();
    
      vector<int> ans(n);
    
      for (int i = 0; i < m - 1; i++)
        for (int j = 0; j < n; j++)
          ans[j] = (ans[j] + (long long)c[m - 2 - i] * f[i][j]) % p;
    
      int inv = power(p - c[m - 1], p - 2);
    
      for (int i = 0; i < n; i++) ans[i] = (long long)ans[i] * inv % p;
    
      return ans;
    }
    ```

### Example problems

1.  [LibreOJ #163. 高斯消元 2 (Gaussian elimination 2)](https://loj.ac/p/163)
2.  [ICPC 2021 Taipei, Gym 103443E. Composition with Large Red Plane, Yellow, Black, Gray, and Blue](https://codeforces.com/gym/103443/problem/E)
