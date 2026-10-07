---
title: Dancing Links
---

This page introduces the exact cover problem, the repeat cover problem, the algorithm that solves them ("Algorithm X"), and the doubly linked cross list Dancing Links used to optimize Algorithm X. It also explains how, with suitable modeling, DLX can be used to solve some search problems.

## Exact cover problem

### Definition

The exact cover problem is: given many sets $S_i (1 \le i \le n)$ and a set $X$, find an unordered tuple $(T_1, T_2, \cdots , T_m)$ satisfying the following conditions:

1.  $\forall i, j \in [1, m],T_i\bigcap T_j = \varnothing (i \neq j)$
2.  $X = \bigcup\limits_{i = 1}^{m}T_i$
3.  $\forall i \in[1, m], T_i \in \{S_1, S_2, \cdots, S_n\}$

### Explanation

For example, if we are given

$$
\begin{aligned}
  & S_1 = \{5, 9, 17\} \\
  & S_2 = \{1, 8, 119\} \\
  & S_3 = \{3, 5, 17\} \\
  & S_4 = \{1, 8\} \\
  & S_5 = \{3, 119\} \\
  & S_6 = \{8, 9, 119\} \\
  & X = \{1, 3, 5, 8, 9, 17, 119\}
\end{aligned}
$$

then $(S_1, S_4, S_5)$ is a valid solution.

### Problem transformation

By discretizing all numbers in $\bigcup\limits_{i = 1}^{n}S_i$, we obtain the following model:

> Given a 0-1 matrix, you may choose some rows so that in the end every column[^note1] has exactly one 1.
> For example, modeling the example above gives the following matrix:

$$
\begin{pmatrix}
0 & 0 & 1 & 0 & 1 & 1 & 0 \\
1 & 0 & 0 & 1 & 0 & 0 & 1 \\
0 & 1 & 1 & 0 & 0 & 1 & 0 \\
1 & 0 & 0 & 1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 & 0 & 0 & 1 \\
0 & 0 & 0 & 1 & 1 & 0 & 1
\end{pmatrix}
$$

> Here the $i$-th row represents $S_i$, and the numbers in that row denote, in order, $[1 \in S_i],[3 \in S_i],[5 \in S_i],\cdots,[119 \in S_i]$.

### Implementation

#### Brute force 1

One method is to enumerate which rows to choose and finally check whether the choice is valid.

Since every row has two states (chosen or not), the time complexity of enumerating rows is $O(2^n)$;

and every check takes $O(nm)$ time. So the total complexity is $O(nm\cdot2^n)$.

??? note "Implementation"
    ```cpp
    int ok = 0;
    for (int state = 0; state < 1 << n; ++state) {  // enumerate whether each row is chosen
      for (int i = 1; i <= n; ++i)
        if ((1 << i - 1) & state)
          for (int j = 1; j <= m; ++j) a[i][j] = 1;
      int flag = 1;
      for (int j = 1; j <= m; ++j)
        for (int i = 1, bo = 0; i <= n; ++i)
          if (a[i][j]) {
            if (bo)
              flag = 0;
            else
              bo = 1;
          }
      if (!flag)
        continue;
      else {
        ok = 1;
        for (int i = 1; i <= n; ++i)
          if ((1 << i - 1) & state) printf("%d ", i);
        puts("");
      }
      memset(a, 0, sizeof(a));
    }
    if (!ok) puts("No solution.");
    ```

#### Brute force 2

Considering the special property of a 0-1 matrix, every row can be viewed as an $m$-bit binary number.

The original problem therefore becomes:

> Given $n$ $m$-bit binary numbers, choose some of them so that the AND of any two chosen numbers is 0 and the OR of all chosen numbers is $2^m - 1$. `tmp` denotes the OR of the binary numbers chosen so far.

Since every row has two states (chosen or not), the time complexity of enumerating rows is $O(2^n)$;

and every computation of `tmp` takes $O(n)$ time. So the total complexity is $O(n\cdot2^n)$.

??? note "Implementation"
    ```cpp
    int ok = 0;
    for (int i = 1; i <= n; ++i)
      for (int j = m; j >= 1; --j) num[i] = num[i] << 1 | a[i][j];
    for (int state = 0; state < 1 << n; ++state) {
      int tmp = 0;
      bool flag = true;
      for (int i = 1; i <= n; ++i)
        if ((1 << i - 1) & state) {
          if (tmp & num[i]) {
            flag = false;
            break;
          }
          tmp |= num[i];
        }
      if (flag && tmp == (1 << m) - 1) {
        ok = 1;
        for (int i = 1; i <= n; ++i)
          if ((1 << i - 1) & state) printf("%d ", i);
        puts("");
      }
    }
    if (!ok) puts("No solution.");
    ```

## Repeat cover problem

The repeat cover problem is similar to the exact cover problem, but without the restriction on overlapping elements. [Algorithm X](#algorithm-x), described below, was originally designed for the exact cover problem, but with a few modifications and optimizations (marked in the text) it solves the repeat cover problem just as efficiently.

## Algorithm X

Donald E. Knuth proposed Algorithm X; its idea is similar to the brute force just described, but it is easy to optimize.

### Procedure

Continuing with the example above, we obtain the following 0-1 matrix:

$$
\begin{pmatrix}
  0 & 0 & 1 & 0 & 1 & 1 & 0 \\
  1 & 0 & 0 & 1 & 0 & 0 & 1 \\
  0 & 1 & 1 & 0 & 0 & 1 & 0 \\
  1 & 0 & 0 & 1 & 0 & 0 & 0 \\
  0 & 1 & 0 & 0 & 0 & 0 & 1 \\
  0 & 0 & 0 & 1 & 1 & 0 & 1
\end{pmatrix}
$$

1.  Now the first row has $3$ ones, the second row has $3$, the third row has $3$, the fourth row has $2$, the fifth row has $2$, and the sixth row has $3$. Choose the first row, delete it, and mark all columns in which it has a $1$;

    $$
    \begin{pmatrix}
      \color{Blue}0 & \color{Blue}0 & \color{Blue}1 & \color{Blue}0 & \color{Blue}1 & \color{Blue}1 & \color{Blue}0 \\
      1 & 0 & \color{Red}0 & 1 & \color{Red}0 & \color{Red}0 & 1 \\
      0 & 1 & \color{Red}1 & 0 & \color{Red}0 & \color{Red}1 & 0 \\
      1 & 0 & \color{Red}0 & 1 & \color{Red}0 & \color{Red}0 & 0 \\
      0 & 1 & \color{Red}0 & 0 & \color{Red}0 & \color{Red}0 & 1 \\
      0 & 0 & \color{Red}0 & 1 & \color{Red}1 & \color{Red}0 & 1
      \end{pmatrix}
    $$

2.  Choose all marked columns, delete them, and mark the rows that contain a $1$ in these columns (for the repeat cover problem no marking is needed);

    $$
    \begin{pmatrix}
      \color{Blue}0 & \color{Blue}0 & \color{Blue}1 & \color{Blue}0 & \color{Blue}1 & \color{Blue}1 & \color{Blue}0 \\
      1 & 0 & \color{Blue}0 & 1 & \color{Blue}0 & \color{Blue}0 & 1 \\
      \color{Red}0 & \color{Red}1 & \color{Blue}1 & \color{Red}0 & \color{Blue}0 & \color{Blue}1 & \color{Red}0 \\
      1 & 0 & \color{Blue}0 & 1 & \color{Blue}0 & \color{Blue}0 & 0 \\
      0 & 1 & \color{Blue}0 & 0 & \color{Blue}0 & \color{Blue}0 & 1 \\
      \color{Red}0 & \color{Red}0 & \color{Blue}0 & \color{Red}1 & \color{Blue}1 & \color{Blue}0 & \color{Red}1
    \end{pmatrix}
    $$

3.  Choose all marked rows and delete them;

    $$
    \begin{pmatrix}
      \color{Blue}0 & \color{Blue}0 & \color{Blue}1 & \color{Blue}0 & \color{Blue}1 & \color{Blue}1 & \color{Blue}0 \\
      1 & 0 & \color{Blue}0 & 1 & \color{Blue}0 & \color{Blue}0 & 1 \\
      \color{Blue}0 & \color{Blue}1 & \color{Blue}1 & \color{Blue}0 & \color{Blue}0 & \color{Blue}1 & \color{Blue}0 \\
      1 & 0 & \color{Blue}0 & 1 & \color{Blue}0 & \color{Blue}0 & 0 \\
      0 & 1 & \color{Blue}0 & 0 & \color{Blue}0 & \color{Blue}0 & 1 \\
      \color{Blue}0 & \color{Blue}0 & \color{Blue}0 & \color{Blue}1 & \color{Blue}1 & \color{Blue}0 & \color{Blue}1
    \end{pmatrix}
    $$

    **This means that this row has been chosen, and the columns in which it has a $1$ may not contain any other 1s**.

    We thus obtain a new, smaller 0-1 matrix:

    $$
    \begin{pmatrix}
      1 & 0 & 1 & 1 \\
      1 & 0 & 1 & 0 \\
      0 & 1 & 0 & 1
    \end{pmatrix}
    $$

4.  Now the first row (originally the second) has $3$ ones, the second row (originally the fourth) has $2$, and the third row (originally the fifth) has $2$. Choose the first row (originally the second), delete it, and mark all columns in which it has a $1$;

    $$
    \begin{pmatrix}
      \color{Blue}1 & \color{Blue}0 & \color{Blue}1 & \color{Blue}1 \\
      \color{Red}1 & 0 & \color{Red}1 & \color{Red}0 \\
      \color{Red}0 & 1 & \color{Red}0 & \color{Red}1
    \end{pmatrix}
    $$

5.  Choose all marked columns, delete them, and mark the rows that contain a $1$ in these columns;

    $$
    \begin{pmatrix}
      \color{Blue}1 & \color{Blue}0 & \color{Blue}1 & \color{Blue}1 \\
      \color{Blue}1 & \color{Red}0 & \color{Blue}1 & \color{Blue}0 \\
      \color{Blue}0 & \color{Red}1 & \color{Blue}0 & \color{Blue}1
    \end{pmatrix}
    $$

6.  Choose all marked rows and delete them;

    $$
    \begin{pmatrix}
      \color{Blue}1 & \color{Blue}0 & \color{Blue}1 & \color{Blue}1 \\
      \color{Blue}1 & \color{Blue}0 & \color{Blue}1 & \color{Blue}0 \\
      \color{Blue}0 & \color{Blue}1 & \color{Blue}0 & \color{Blue}1
    \end{pmatrix}
    $$

    This gives an empty matrix. But the last deleted row `1 0 1 1` is not all $1$s, which means the choice was wrong;

    $$
    \begin{pmatrix}
    \end{pmatrix}
    $$

7.  Backtrack to step 4 and consider choosing the second row (originally the fourth): delete it and mark all columns in which it has a $1$;

    $$
    \begin{pmatrix}
      \color{Red}1 & 0 & \color{Red}1 & 1 \\
      \color{Blue}1 & \color{Blue}0 & \color{Blue}1 & \color{Blue}0 \\
      \color{Red}0 & 1 & \color{Red}0 & 1
    \end{pmatrix}
    $$

8.  Choose all marked columns, delete them, and mark the rows that contain a $1$ in these columns;

    $$
    \begin{pmatrix}
      \color{Blue}1 & \color{Red}0 & \color{Blue}1 & \color{Red}1 \\
      \color{Blue}1 & \color{Blue}0 & \color{Blue}1 & \color{Blue}0 \\
      \color{Blue}0 & 1 & \color{Blue}0 & 1
    \end{pmatrix}
    $$

9.  Choose all marked rows and delete them;

    $$
    \begin{pmatrix}
      \color{Blue}1 & \color{Blue}0 & \color{Blue}1 & \color{Blue}1 \\
      \color{Blue}1 & \color{Blue}0 & \color{Blue}1 & \color{Blue}0 \\
      \color{Blue}0 & 1 & \color{Blue}0 & 1
      \end{pmatrix}
    $$

    We thus obtain the following matrix:

    $$
    \begin{pmatrix}
      1 & 1
    \end{pmatrix}
    $$

10. Now the first row (originally the fifth) has $2$ ones; delete them all and obtain an empty matrix:

    $$
    \begin{pmatrix}
    \end{pmatrix}
    $$

11. The last deletion removed a row consisting entirely of $1$s, so we succeeded and the algorithm ends.

    The answer is the three deleted rows: $1, 4, 5$.

We strongly recommend simulating the process of matrix deletion, restoration, and backtracking yourself before reading on.

From the steps above, the flow of Algorithm X can be summarized as follows:

1.  In the current matrix $M$, choose and mark a row $r$, and add $r$ to $S$;
2.  if all $r$ have been tried and there is no solution, the algorithm ends and reports that there is no solution;
3.  mark the rows $r_i$ and columns $c_i$ related to $r$ (related rows and columns are defined as in step 2 of [Algorithm X](#procedure); the same applies below);
4.  delete all marked rows and columns to obtain a new matrix $M'$;
5.  if $M'$ is empty and $r$ consists entirely of $1$s, the algorithm ends and outputs the set $S$ of deleted rows;

    if $M'$ is empty and $r$ does not consist entirely of $1$s, restore the rows $r_i$ and columns $c_i$ related to $r$ and jump to step 1;

    if $M'$ is not empty, jump to step 1.

It is easy to see that Algorithm X requires a large number of "delete row", "delete column", "restore row", and "restore column" operations.

A naive idea is to store the matrix in a two-dimensional array and use four additional arrays to store, for each row, the indices of its adjacent rows, so that every deletion and restoration only updates elements in these four arrays. However, since in the matrices of typical problems the number of 0s far exceeds the number of 1s, the space complexity of this approach is hard to accept.

Donald E. Knuth came up with the idea of maintaining these operations with a doubly linked cross list.

The process of constantly jumping around on this list is vividly described as "dancing", so the doubly linked cross list used to optimize Algorithm X is also called "Dancing Links".

## Algorithm X optimized with Dancing Links

### Preprocessor directive

```cpp
#define IT(i, A, x) for (i = A[x]; i != x; i = A[i])
```

### Definition

A doubly linked cross list has four pointer fields, pointing to the elements above, below, to the left, and to the right; moreover, every element $i$ in the whole list system corresponds to one cell, so we also need to record the column and row in which $i$ lies, as shown in the figure:

![dlx-1.svg](./images/dlx-1.svg)

A large doubly linked list is more complex:

![dlx-2.svg](./images/dlx-2.svg)

Every row has a row head pointer, and every column has a column header.

The row head pointers are `first[]`, and the column headers are the $c + 1$ newly created sentinel nodes. It is worth noting that **the row head pointer is not a sentinel node in the list**. It is virtual, similar to the `first[]` array in an adjacency list, and **points directly** to the first element of that row.

In addition, every column has a `siz[]` denoting the number of elements in that column.

In particular, node $0$ having no right node is equivalent to this Dancing Links being empty.

```cpp
constexpr int MS = 1e5 + 5;
int n, m, idx, first[MS], siz[MS];
int L[MS], R[MS], U[MS], D[MS];
int col[MS], row[MS];
```

### Procedure

#### The remove operation

`remove(c)` means deleting column $c$ from the Dancing Links, together with the rows and columns related to it.

First delete $c$; at this point:

-   the right node of the node to the left of $c$ should be the right node of $c$.
-   the left node of the node to the right of $c$ should be the left node of $c$.

That is, `L[R[c]] = L[c], R[L[c]] = R[c];`.

![dlx-3.svg](./images/dlx-3.svg)

Then walk down along this column and delete every row passed.

How do we delete a row? Enumerate the pointer $j$ of the current row; at this point:

-   the lower node of the node above $j$ should be the lower node of $j$.
-   the upper node of the node below $j$ should be the upper node of $j$.

Note that the element count of each column must be updated.

That is, `U[D[j]] = U[j], D[U[j]] = D[j], --siz[col[j]];`.

![dlx-4.svg](./images/dlx-4.svg)

The implementation of the `remove` function is as follows:

???+ note "Implementation"
    ```cpp
    void remove(const int &c) {
      int i, j;
      L[R[c]] = L[c], R[L[c]] = R[c];
      // traverse this column from top to bottom
      IT(i, D, c)
      // traverse this row from left to right
      IT(j, R, i)
      U[D[j]] = U[j], D[U[j]] = D[j], --siz[col[j]];
    }
    ```

#### The recover operation

`recover(c)` means restoring column $c$ in the Dancing Links, together with the rows and columns related to it.

`recover(c)` is the inverse operation of `remove(c)`, so we do not repeat the explanation here.

**It is worth noting that** the order of all operations in `recover(c)` **is exactly the reverse of** that in `remove(c)`**.**

The implementation of `recover(c)` is as follows:

???+ note "Implementation"
    ```cpp
    void recover(const int &c) {
      int i, j;
      IT(i, U, c) IT(j, L, i) U[D[j]] = D[U[j]] = j, ++siz[col[j]];
      L[R[c]] = R[L[c]] = c;
    }
    ```

#### The build operation

`build(r, c)` means creating a new Dancing Links of size $r \times c$, i.e., with $r$ rows and $c$ columns.

Create $c + 1$ nodes as column headers.

The left node of the $i$-th node is $i - 1$, its right node is $i + 1$, its upper node is $i$, and its lower node is $i$. In particular, the left node of node $0$ is $c$, and the right node of node $c$ is $0$.

We thus obtain a circular doubly linked list:

![dlx-5.svg](./images/dlx-5.svg)

This initializes a Dancing Links.

The implementation of `build(r, c)` is as follows:

???+ note "Implementation"
    ```cpp
    void build(const int &r, const int &c) {
      n = r, m = c;
      for (int i = 0; i <= c; ++i) {
        L[i] = i - 1, R[i] = i + 1;
        U[i] = D[i] = i;
      }
      L[0] = c, R[c] = 0, idx = c;
      memset(first, 0, sizeof(first));
      memset(siz, 0, sizeof(siz));
    }
    ```

#### The insert operation

`insert(r, c)` means inserting a node in row $r$, column $c$.

The insertion has two cases:

-   If row $r$ has no elements, simply insert an element and make `first[r]` point to it.

    This is done with `first[r] = L[idx] = R[idx] = idx;`.

-   If row $r$ has elements, connect the new element to $c$ and $first(r)$ in a special way.

    Let the new element be $idx$; then:

    -   Insert $idx$ directly below $c$; at this point:

        -   the node below $idx$ is the former lower node of $c$;
        -   the upper node of the node below $idx$ (i.e., the former lower node of $c$) is $idx$;
        -   the upper node of $idx$ is $c$;
        -   the lower node of $c$ is $idx$.

        Remember to record the column and row of $idx$ and to update the element count of this column.

        ```cpp
        col[++idx] = c, row[idx] = r, ++siz[c];
        U[idx] = c, D[idx] = D[c], U[D[c]] = idx, D[c] = idx;
        ```

        **We strongly recommend that the reader fully master the order of these steps before continuing.**

    -   Insert $idx$ directly to the right of $first(r)$; at this point:

        -   the node to the right of $idx$ is the former right node of $first(r)$;
        -   the left node of the former right node of $first(r)$ is $idx$;
        -   the left node of $idx$ is $first(r)$;
        -   the right node of $first(r)$ is $idx$.

        ```cpp
        L[idx] = first[r], R[idx] = R[first[r]];
        L[R[first[r]]] = idx, R[first[r]] = idx;
        ```

        **We strongly recommend that the reader fully master the order of these steps before continuing.**

The operation `insert(r, c)` is easier to understand with a picture:

![dlx-6.svg](./images/dlx-6.svg)

Pay attention to the direction of the curved arrows.

The implementation of `insert(r, c)` is as follows:

???+ note "Implementation"
    ```cpp
    void insert(const int &r, const int &c) {
      row[++idx] = r, col[idx] = c, ++siz[c];
      U[idx] = c, D[idx] = D[c], U[D[c]] = idx, D[c] = idx;
      if (!first[r])
        first[r] = L[idx] = R[idx] = idx;
      else {
        L[idx] = first[r], R[idx] = R[first[r]];
        L[R[first[r]]] = idx, R[first[r]] = idx;
      }
    }
    ```

#### The dance operation

`dance()` is the process of recursively deleting and restoring rows and columns.

1.  If node $0$ has no right node, the matrix is empty; record the answer and return;
2.  choose the column with the fewest elements and delete it;
3.  traverse all rows that have a $1$ in this column and enumerate whether each is chosen;
4.  recursively call `dance()`; if feasible, return; if not, restore the chosen row;
5.  if there is no solution, return.

The implementation of `dance()` is as follows:

???+ note "Implementation"
    ```cpp
    bool dance(int dep) {
      int i, j, c = R[0];
      if (!R[0]) {
        ans = dep;
        return true;
      }
      IT(i, R, 0) if (siz[i] < siz[c]) c = i;
      remove(c);
      IT(i, D, c) {
        stk[dep] = row[i];
        IT(j, R, i) remove(col[j]);
        if (dance(dep + 1)) return true;
        IT(j, L, i) recover(col[j]);
      }
      recover(c);
      return false;
    }
    ```

Here `stk[]` is used to record the answer.

Note that each time we preferentially choose the column with the fewest elements for deletion; this gives the program a certain heuristic quality and keeps the branching of the search tree minimal.

For the repeat cover problem, an estimate function (similar to the one in [A\*](astar.md)) can be used for pruning during the search: if the number of chosen rows in the current best case already exceeds the current best solution, we can return immediately.

## Template

??? note "[Template code](https://www.luogu.com.cn/problem/P4929)"
    ```cpp
    --8<-- "docs/search/code/dlx/dlx_1.cpp"
    ```

## Properties

The number of recursions and backtracks in DLX depends on the number of $1$s in the matrix, not on parameters such as $r, c$ of the matrix. Therefore its time complexity is **exponential**; the theoretical complexity is roughly $O(c^n)$, where $c$ is some constant very close to $1$ and $n$ is the number of $1$s in the matrix.

In practice, however, DLX performs well and can usually solve most problems.

## Modeling

The difficulty of DLX lies not entirely in building the list, but in modeling.

Please make sure you have fully mastered the DLX template before reading on.

Whenever we get a problem, we should consider what the rows and columns represent:

-   rows represent *decisions*, since every row corresponds to a set, and thus to choosing/not choosing;

-   columns represent *states*, since the $i$-th column corresponds to some condition $P_i$.

For a given row, since the values in different columns differ, **we define a decision from different states**.

### Example 1 [P1784 Sudoku](https://www.luogu.com.cn/problem/P1784)

??? note "Solution idea"
    First consider what a decision is.
    
    In this problem, every decision can be represented by an ordered triple of the form $(r, c, w)$.
    
    Note that the "box" is not a parameter of the decision, because **it can be expressed by every fixed $(r, c)$**.
    
    Therefore there are $9 \times 9 \times 9 = 729$ rows.
    
    Next consider what a state is.
    
    Let us think about what effects the decision $(r, c, w)$ has. Let $b$ be the box containing $(r, c)$.
    
    1.  Row $r$ uses a $w$ (represented by $9 \times 9 = 81$ columns);
    2.  column $c$ uses a $w$ (represented by $9 \times 9 = 81$ columns);
    3.  box $b$ uses a $w$ (represented by $9 \times 9 = 81$ columns);
    4.  a number is filled into $(r, c)$ (represented by $9 \times 9 = 81$ columns).
    
    Therefore there are $81 \times 4 = 324$ columns and $729 \times 4 = 2916$ ones in total.
    
    Thus we have successfully transformed the $9 \times 9$ Sudoku problem into an exact cover problem **with $729$ rows, $324$ columns, and $2916$ ones in total**.

??? note "Sample code"
    ```cpp
    --8<-- "docs/search/code/dlx/dlx_2.cpp"
    ```

### Example 2 [Target Sudoku](https://www.luogu.com.cn/problem/P1074)

??? note "Solution idea"
    The model of this problem is **exactly the same** as that of [Sudoku](https://www.luogu.com.cn/problem/P1784); the main difference lies in updating the answer.
    
    For this problem we can keep an array of weights, and every time a Sudoku solution is found,
    
    multiply the number at each position by its weight and add it to the answer.

??? note "Sample code"
    ```cpp
    --8<-- "docs/search/code/dlx/dlx_3.cpp"
    ```

### Example 3 ["NOI2005" Wisdom Beads](https://www.luogu.com.cn/problem/P4205)

??? note "Solution idea"
    Definition: the shape of a bead as given in the problem is called the *standard shape* of that bead.
    
    Obviously, we can change the shape of a bead by changing two parameters: $d$ (the number of clockwise $90^{\circ}$ rotations) and $f$ (whether it is flipped horizontally).
    
    Again, we first consider what a decision is.
    
    In this problem, every decision can be represented by an ordered tuple of the form $(v, d, f, i)$.
    
    It means that the $i$-th bead in its *standard shape* is placed with its upper-left corner at position $v$, after $d$ clockwise rotations by $90^{\circ}$.
    
    Conveniently, we can let $f = 1$ mean no horizontal flip and $f = -1$ mean a horizontal flip, which simplifies the code.
    
    Therefore there are $55 \times 4 \times 2 \times 12 = 5280$ rows.
    
    Note that, because of some invalid placements such as $(1, 0, 1, 4)$,
    
    **in practice only $2730$ rows need to be built for an empty bead board.**
    
    Next consider what a state is.
    
    The state in this problem is relatively simple.
    
    Let us think about what effects the decision $(v, d, f, i)$ has.
    
    1.  Some cells are occupied (represented by $55$ columns);
    2.  the $i$-th bead is used (represented by $12$ columns).
    
    Therefore there are $55 + 12 = 67$ columns and $5280 \times (5 + 1) = 31680$ ones in total.
    
    Thus we have successfully transformed the Wisdom Beads game into an exact cover problem **with $5280$ rows, $67$ columns, and $31680$ ones in total**.

??? note "Sample code"
    ```cpp
    --8<-- "docs/search/code/dlx/dlx_4.cpp"
    ```

## Exercises

-   [SUDOKU - Sudoku](https://www.spoj.com/problems/SUDOKU/)
-   ["kuangbin" Topic 3: Dancing Links](https://vjudge.net/contest/65998#overview)

## External links

-   [The Jumping Dancer: the Dancing Links algorithm for the exact cover problem – 万仓一黍 (Chinese)](https://www.cnblogs.com/grenet/p/3145800.html)
-   [Search: the DLX algorithm – 静听风吟 (Chinese)](https://www.cnblogs.com/aininot260/p/9629926.html)
-   [*Training Guide for Beginners in Algorithm Competitions* (《算法竞赛入门经典 - 训练指南》)](https://book.douban.com/subject/35431537/)

## Notes

[^note1]: (Terminology difference between mainland China and Taiwan) Taiwan: 直行 (column), 橫列 (row)
