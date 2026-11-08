---
title: Gaussian elimination
---

## Introduction

Gaussian elimination (Gauss–Jordan elimination) is a classical algorithm for solving systems of linear equations. It has an important place and value in modern mathematics and is an important part of linear algebra courses.

Besides solving systems of linear equations, Gaussian elimination can also be used to compute determinants, find the inverse of a matrix, and in other computing and engineering applications.

## The elimination method and the idea of Gaussian elimination

### Definition

The elimination method consists of expressing an unknown from one equation of the system as an algebraic expression containing another unknown and substituting it into another equation; this eliminates one unknown and yields a solution. Alternatively, one equation of the system is multiplied by some constant and added to another equation, which also achieves the elimination of one unknown. The elimination method is mainly used to solve systems of two linear equations in two unknowns.

### Explanation

Example 1: use the elimination method to solve the system of two linear equations in two unknowns:

$$
\begin{cases}
4x+y&=100 \\
x-y&=100
\end{cases}
$$

Solution: adding the two equations of the system eliminates $y$ and gives:

$$
5x = 200
$$

Solving gives:

$$
x = 40
$$

Substituting $x = 40$ into the second equation of the system gives:

$$
y = -60
$$

### The core of the theory of the elimination method

The core of the theory of the elimination method is mainly as follows:

-   swapping two equations does not change the solution;

-   multiplying an equation by a nonzero number $k$ does not change the solution;

-   adding an equation multiplied by a number $k$ to another equation does not change the solution.

### The idea of Gaussian elimination

The German mathematician Gauss thought about and analyzed the elimination method and came to the following conclusions:

-   in the elimination method, what takes part in the computation and changes are the coefficients of the variables in the equations;

-   the variables themselves do not take part in the computation and do not change;

-   the variables can be represented by the positions of the coefficients, so the variables can be omitted;

-   if the variables are simplified away in the computation, the solution of the equations does not change.

Based on these conclusions, Gauss proposed Gaussian elimination: first the augmented matrix of the system is reduced to reduced row echelon form by elementary row operations, then values are assigned to the free unknowns using linear independence as the criterion, and finally the general solution of the system is written out.

## The five-step method of Gaussian elimination

## Explanation

In Gaussian elimination, assigning values to the free unknowns after the augmented matrix has been reduced to its reduced form requires knowledge of linear dependence, and the assignment involves an element of human experience, which causes some difficulty in learning. Therefore, Gaussian elimination is divided into five steps, giving the five-step method, whose content is as follows:

1.  reduce the augmented matrix to reduced row echelon form by elementary row operations;

2.  reconstruct the system of linear equations;

3.  solve for the first variable;

4.  supplement the free unknowns;

5.  write out the general solution of the system.

We use an example to further illustrate how the algorithm works.

## Procedure

Example 2: use the five-step method of Gaussian elimination to solve the system of linear equations:

$$
\begin{cases}
2x_1+5x_3+6x_4&=9 \\
x_3+x_4&=-4 \\
2x_3+2x_4&=-8
\end{cases}
$$

### Reducing the augmented matrix to reduced row echelon form by (elementary) row operations

The augmented matrix is the new matrix formed by joining the coefficient matrix $A$ of the system with the column of constants $b$, i.e., $(A | b)$. Reducing the augmented matrix to reduced row echelon form by elementary row operations uses exactly the idea of Gaussian elimination: the variables are omitted and represented by the positions of their coefficients. The vertical bar in the augmented matrix separates the coefficient matrix from the column of constants and represents the equals sign.

$$
\left(\begin{matrix}
2 & 0 & 5 & 6 \\
0 & 0 & 1 & 1 \\
0 & 0 & 2 & 2
\end{matrix} \middle|
\begin{matrix}
9 \\
-4 \\
-8
\end{matrix} \right)
$$

$$
\xrightarrow{r_3-2r_2}
\left(\begin{matrix}
2 & 0 & 5 & 6 \\
0 & 0 & 1 & 1 \\
0 & 0 & 0 & 0
\end{matrix} \middle|
\begin{matrix}
9 \\
-4 \\
0
\end{matrix} \right)
$$

reduced to row echelon form

$$
\xrightarrow{\frac{r_1}{2}}
\left(\begin{matrix}
1 & 0 & 2.5 & 3 \\
0 & 0 & 1 & 1 \\
0 & 0 & 0 & 0
\end{matrix} \middle|
\begin{matrix}
4.5 \\
-4 \\
0
\end{matrix} \right)
$$

$$
\xrightarrow{r_1-r_2 \times 2.5}
\left(\begin{matrix}
1 & 0 & 0 & 0.5 \\
0 & 0 & 1 & 1 \\
0 & 0 & 0 & 0
\end{matrix} \middle|
\begin{matrix}
14.5 \\
-4 \\
0
\end{matrix} \right)
$$

reduced to reduced row echelon form

### Reconstructing the system of linear equations

$$
\begin{cases}
x_1+0.5x_4 &= 14.5\\
x_3+x_4 &= -4 \\
\end{cases}
$$

???+ note "Explanation"
    Reconstructing the system of linear equations means rewriting it in the form of linear equations based on the reduced row echelon form, i.e., the coefficients at the various positions of the reduced row echelon form are assigned variables again, and the vertical bar in the middle is turned back into an equals sign.

### Solving for the first variable

$$
\begin{cases}
x_1 = -0.5x_4+14.5\notag \\
x_3 = -x_4-4\notag
\end{cases}
$$

???+ note "Explanation"
    This means that in the reconstructed system of linear equations, the first variable of each equation is expressed in terms of the other quantities. For example, the first variables of the two equations of the system are $x_1$ and $x_3$.

### Supplementing the free unknowns

$$
\begin{cases}
x_1 = -0.5x_4+14.5 \\
x_2 = x_2 \\
x_3 = -x_4-4 \\
x_4 = x_4
\end{cases}
$$

???+ note "Explanation"
    In step 3, the variables $x_1$ and $x_3$ were solved for, which shows that the remaining variables $x_2$ and $x_4$ are not constrained by the system of equations; they are free unknowns and can take arbitrary values. Therefore, the solution obtained in step 3 needs to be supplemented, and the way to do so is to write $x_2 = x_2,x_4 = x_4$. This way of supplementing the solution agrees with the definition of a free unknown and is easy to understand: since the free unknowns are unconstrained, they can only equal themselves.

### Writing out the general solution of the system

$$
\begin{aligned}
\begin{pmatrix} x_1 \\ x_2 \\ x_3 \\ x_4 \end{pmatrix} &=
\begin{pmatrix} 0 \\ 1 \\ 0 \\ 0 \end{pmatrix} x_2+
\begin{pmatrix} -0.5 \\ 0 \\ -1 \\ 1 \end{pmatrix} x_4 +
\begin{pmatrix} 14.5 \\ 0 \\ -4 \\ 0 \end{pmatrix} \\
&= \begin{pmatrix} 0 \\ 1 \\ 0 \\ 0 \end{pmatrix} C_1+
\begin{pmatrix} -0.5 \\ 0 \\ -1 \\ 1 \end{pmatrix} C_2 +
\begin{pmatrix} 14.5 \\ 0 \\ -4 \\ 0 \end{pmatrix}
\end{aligned}
$$

where $C_1$ and $C_2$ are arbitrary constants.

???+ note "Explanation"
    This means that, based on step 4, the solution is expressed as a combination of column vectors; at the same time, since $x_2$ and $x_4$ are free unknowns that can take arbitrary values, on the right-hand side of the solution we set them to arbitrary constants $C_1$ and $C_2$ respectively, which completes the solution of the system.

## Computing the determinant

### Explanation

The determinant of an $N \times N$ square matrix can be understood as the signed volume of the geometric body spanned by all its column vectors.

For example:

$$
\begin{vmatrix}
1 & 0 \\
0 & 1 \end{vmatrix} = 1
$$

$$
\begin{vmatrix}
1 & 2 \\
2 & 1 \end{vmatrix} = -3
$$

The determinant is given by the formula

$$
\operatorname{det}(A)=\sum_{\sigma \in S_{n}} \operatorname{sgn}(\sigma) \prod_{i=1}^{n} a_{i, \sigma(i)}
$$

where $S_n$ is the set of all permutations of length $n$, $\sigma$ is a permutation, and if the number of inversions of $\sigma$ is even then $\operatorname{sgn}(\sigma)=1$, otherwise $\operatorname{sgn}(\sigma)=−1$.

Understanding the invariance of the determinant through the notion of volume is a very simple approach:

-   transposing the matrix does not change the determinant;

-   swapping rows (columns) of the matrix negates the determinant;

-   adding or subtracting rows (columns) of the matrix does not change the determinant;

-   multiplying all elements of a row (column) of the matrix by a number $k$ scales the determinant proportionally.

Hence, after applying Gaussian elimination to the matrix, we obtain a diagonal matrix whose determinant is determined by the product of the diagonal elements. Its sign is determined by the number of row swaps (if it is odd, the sign of the determinant should be flipped). Therefore, we can compute the determinant of a matrix with Gauss's algorithm in $O(n^3)$ complexity.

Note that if at some point we cannot find a nonzero cell in the current column, the algorithm should stop and return 0.

### Implementation

```cpp
constexpr double EPS = 1E-9;
int n;
vector<vector<double>> a(n, vector<double>(n));

double det = 1;
for (int i = 0; i < n; ++i) {
  int k = i;
  for (int j = i + 1; j < n; ++j)
    if (abs(a[j][i]) > abs(a[k][i])) k = j;
  if (abs(a[k][i]) < EPS) {
    det = 0;
    break;
  }
  swap(a[i], a[k]);
  if (i != k) det = -det;
  det *= a[i][i];
  for (int j = i + 1; j < n; ++j) a[i][j] /= a[i][i];
  for (int j = 0; j < n; ++j)
    if (j != i && abs(a[j][i]) > EPS)
      for (int k = i + 1; k < n; ++k) a[j][k] -= a[i][k] * a[j][i];
}

cout << det;
```

## Matrix inversion

For a square matrix $A$, if there exists a square matrix $A^{-1}$ such that $A \times A^{-1} = A^{-1} \times A = I$, then the matrix $A$ is called invertible, and $A^{-1}$ is called its inverse matrix.

Given a square matrix $A$ of order $n$, its inverse matrix is found as follows:

1.  construct the $n \times 2n$ matrix $(A, I_n)$;
2.  use Gaussian elimination to reduce it to the reduced form $(I_n, A^{-1})$, which gives the inverse matrix $A^{-1}$ of $A$. If the left half of the final reduced form is not the identity matrix $I_n$, then the matrix $A$ is not invertible.

The proof of correctness of this method requires a fair amount of linear algebra and is omitted here for reasons of space. Interested readers can look up the relevant material themselves.

## Solving systems of XOR equations with Gaussian elimination

A system of XOR equations is a system of the form

$$
\begin{cases}
a_{1,1}x_1 \oplus a_{1,2}x_2 \oplus \cdots \oplus a_{1,n}x_n &= b_1\\
a_{2,1}x_1 \oplus a_{2,2}x_2 \oplus \cdots \oplus a_{2,n}x_n &= b_2\\
\cdots &\cdots \\ a_{m,1}x_1 \oplus a_{m,2}x_2 \oplus \cdots \oplus a_{m,n}x_n &= b_m
\end{cases}
$$

where $\oplus$ denotes "bitwise exclusive or" (i.e., `xor`, or `^` in C++), and all coefficients/constants in the equations (i.e., $a_{i,j}$ and $b_i$) are $0$ or $1$.

Since "XOR" is commutative and associative, the system can be solved by step-by-step elimination as in Gaussian elimination. Note that during elimination we should use "XOR elimination" rather than "addition/subtraction elimination", and there is no need to multiply or divide to change coefficients (since all coefficients are $0$ or $1$).

Note that the augmented matrix of a system of XOR equations is a $01$-matrix (a matrix containing only $0$ and $1$), so we can use `std::bitset` from C++ for optimization and reduce the time complexity to $O(\dfrac{n^2m}{\omega})$, where $n$ is the number of unknowns, $m$ is the number of equations, and $\omega$ is usually $32$ (machine dependent).

Reference implementation:

```cpp
std::bitset<1010> matrix[2010];  // matrix[1~n]: augmented matrix, position 0 holds the constant

std::vector<bool> GaussElimination(
    int n, int m)  // n is the number of unknowns, m the number of equations; returns the solution of the system
                   // (returns an empty vector if there are multiple solutions / no solution)
{
  for (int i = 1; i <= n; i++) {
    int cur = i;
    while (cur <= m && !matrix[cur].test(i)) cur++;
    if (cur > m) return std::vector<bool>(0);
    if (cur != i) swap(matrix[cur], matrix[i]);
    for (int j = 1; j <= m; j++)
      if (i != j && matrix[j].test(i)) matrix[j] ^= matrix[i];
  }
  std::vector<bool> ans(n + 1);
  for (int i = 1; i <= n; i++) ans[i] = matrix[i].test(0);
  return ans;
}
```

## Exercises

-   [Codeforces - Wizards and Bets](http://codeforces.com/contest/167/problem/E)
-   [Luogu - SDOI2010 外星千足虫 (Alien Millipedes)](https://www.luogu.com.cn/problem/P2447)
