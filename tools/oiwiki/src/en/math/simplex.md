---
title: Simplex method
---

Prerequisites: [Basics of linear programming](./linear-programming.md)

## Introduction

In algorithm competitions, the simplex method is often used to solve linear programming problems. However, since the linear programming problems encountered in competitions mostly have a more special structure and can often be reduced to network flow problems, the simplex method is not commonly used, and its efficiency does not match that of algorithms designed specifically for network flow problems.

## Basic concepts

Suppose we want to solve the following linear programming problem in [standard form](./linear-programming.md#标准形式) with $n$ decision variables and $m+n$ constraints:

$$
\begin{aligned}
\min_{x}\; & z = c^Tx \\
\text{subject to }& Ax = b, \\
& x \ge 0.
\end{aligned}
$$

Without loss of generality, assume that the system of linear equations determined by these $m$ equality constraints has a solution and that $A$ has full rank, so $\operatorname{rank}A = m \le n$.

### An example

Before rigorously describing the steps of the simplex method, this section first examines a concrete example to make it easier to understand.

???+ example "Example"
    Consider the linear programming problem
    
    $$
    \begin{aligned}
    \max\; & 10 x_1 + 12 x_2 + 12 x_3 \\
    \text{subject to } & x_1 + 2 x_2 + 2x_3 \le 20, \\
    & 2x_1 + x_2 + 2x_3 \le 20, \\
    & 2x_1 + 2x_2 + x_3 \le 20,\\
    & x_1,x_2,x_3 \ge 0.
    \end{aligned}
    $$
    
    By adding slack variables, we obtain its standard form:
    
    $$
    \begin{aligned}
    \min\; & -10 x_1 - 12 x_2 - 12 x_3 \\
    \text{subject to } & x_1 + 2 x_2 + 2x_3 + x_4 = 20, \\
    & 2x_1 + x_2 + 2x_3 + x_5 = 20, \\
    & 2x_1 + 2x_2 + x_3 + x_6 = 20,\\
    & x_1,x_2,x_3,x_4,x_5,x_6 \ge 0.
    \end{aligned}
    $$
    
    Look at the equality constraints of this problem: they actually express the variables $x_4,x_5,x_6$ in terms of the variables $x_1,x_2,x_3$. Rearranging the original problem slightly, we get
    
    $$
    \begin{array}{rrrrrr}
    \min_{x_i\ge 0}  &  z  = &  0 &  -10x_1 &  -12x_2 &  -12x_3\;\\
    \text{subject to}& x_4 = & 20 &    -x_1 &   -2x_2 &   -2x_3, \\
                & x_5 = & 20 &   -2x_1 &    -x_2 &   -2x_3, \\
                & x_6 = & 20 &   -2x_1 &   -2x_2 &    -x_3. \\
    \end{array}
    $$
    
    From this form it is clear that if we set $x_1=x_2=x_3=0$, we obtain a feasible solution of the original problem
    
    $$
    x = (0,0,0,20,20,20)^T.
    $$
    
    Its corresponding value is $z=0$. For convenience, we call the variables $x_1,x_2,x_3$ that were set to zero nonbasic variables, and the remaining variables $x_4,x_5,x_6$ basic variables.
    
    This feasible solution is obviously not optimal. As long as we increase the values of $x_1,x_2,x_3$ appropriately so that $x_4,x_5,x_6$ remain nonnegative, the solution stays feasible. Moreover, since the coefficients of $x_1,x_2,x_3$ in the objective function are all strictly negative, increasing their values will certainly decrease the value of the objective function. For instance, we may choose to increase the value of $x_1$. To decrease the objective function as much as possible, we need to increase the value of $x_1$ as much as possible. But to keep the solution feasible, we must ensure $x_4,x_5,x_6\ge 0$. Therefore, $x_1$ can be increased at most to
    
    $$
    \min\left\{\dfrac{20}{1},\dfrac{20}{2},\dfrac{20}{2}\right\} = 10.
    $$
    
    The feasible solution then becomes
    
    $$
    x = (10,0,0,10,0,0)^T.
    $$
    
    Since $x_1$ has become a basic variable, to return to the initial situation (i.e., three basic variables expressed in terms of three nonbasic variables), we need to choose a new nonbasic variable. Since $x_5,x_6$ are both zero, either of them can be chosen as the nonbasic variable and set to zero. Let us choose $x_5$ as the nonbasic variable. Substituting
    
    $$
    x_1 = 10 - 0.5x_5 - 0.5x_2 - x_3
    $$
    
    into the original problem, we can rewrite it as
    
    $$
    \begin{array}{rrrrrr}
    \min_{x_i\ge 0}  &   z = &-100&   +5x_5 &   -7x_2 &   -2x_3\;\\
    \text{subject to}& x_4 = & 10 & +0.5x_5 & -1.5x_2 &    -x_3, \\
                & x_1 = & 10 & -0.5x_5 & -0.5x_2 &    -x_3, \\
                & x_6 = &  0 &    +x_5 &    -x_2 &    +x_3. \\
    \end{array}
    $$
    
    This brings us back to the initial situation.
    
    Continue to look at the current objective function. The coefficient of the nonbasic variable $x_3$ is still negative. We may consider increasing the value of $x_3$. To ensure $x_4,x_1,x_6\ge 0$, the variable $x_3$ can be increased at most to
    
    $$
    \min\left\{\dfrac{10}{1},\dfrac{10}{1}\right\} = 10.
    $$
    
    Note that in the expression for $x_6$, the coefficient of $x_3$ is positive, so no matter how much we increase $x_3$, $x_6$ never becomes negative. This is why the braces contain only two terms this time. When $x_3$ increases to $10$, $x_1,x_4$ both become zero, so either of them can be chosen as the new nonbasic variable. Let us choose $x_4$. Substituting
    
    $$
    x_3 = 10 + 0.5x_5 - 1.5x_2 - x_4
    $$
    
    into the above problem, the problem becomes
    
    $$
    \begin{array}{rrrrrr}
    \min_{x_i\ge 0}  &   z = &-120&   +4x_5 &   -4x_2 &   +2x_4\;\\
    \text{subject to}& x_3 = & 10 & +0.5x_5 & -1.5x_2 &    -x_4, \\
                & x_1 = &  0 &    -x_5 &    +x_2 &    +x_4, \\
                & x_6 = & 10 & +1.5x_5 & -2.5x_2 &    -x_4. \\
    \end{array}
    $$
    
    Simply substituting $x_5=x_2=x_4=0$, we can read off from this form that the current feasible solution is
    
    $$
    x = (0,0,10,0,0,10)^T,
    $$
    
    and its corresponding value is $z=-120$.
    
    Repeat the previous operations. Since the coefficient of $x_2$ is negative, its value can be increased; but to keep $x_3,x_6$ nonnegative, it can only be increased to
    
    $$
    \min\left\{\dfrac{10}{1.5},\dfrac{10}{2.5}\right\} = 4.
    $$
    
    Since the minimum in the braces is attained in the expression for the variable $x_6$, it becomes zero when $x_2=4$. Substituting the expression
    
    $$
    x_2 = 4 + 0.6x_5 - 0.4x_6 - 0.4x_4
    $$
    
    into the above problem, the original problem can be rewritten as
    
    $$
    \begin{array}{rrrrrr}
    \min_{x_i\ge 0}  &   z = &-136& +1.6x_5 & +1.6x_6 & +3.6x_4\;\\
    \text{subject to}& x_3 = &  4 & -0.4x_5 & +0.6x_6 & -0.4x_4, \\
                & x_1 = &  4 & -0.4x_5 & -0.4x_6 & +0.6x_4, \\
                & x_2 = &  4 & +0.6x_5 & -0.4x_6 & -0.4x_4. \\
    \end{array}
    $$
    
    Again setting the nonbasic variables $x_5,x_6,x_4$ to zero, we obtain the current feasible solution
    
    $$
    x = (4,4,4,0,0,0)^T.
    $$
    
    The corresponding value is $z=-136$.
    
    Since the coefficients of all nonbasic variables in the objective function are positive, the above process of improving the objective function cannot continue, so the current feasible solution is optimal. The algorithm terminates.

In this example, the algorithm starts from a feasible solution and keeps improving the objective function until no further improvement is possible. This is the basic idea of the simplex method.

### Basic feasible solution

Since $A$ has full rank, we can always choose a subset $B\subseteq\{1,2,\cdots,n\}$ of size $m$ such that $A_B$ is an invertible square matrix. Thus $x_B$ can be expressed in terms of the remaining variables $x_N$:

$$
x_B = A_B^{-1}b - A_B^{-1}A_Nx_N.
$$

Here $N=\{1,2,\cdots,n\}\setminus B$, the matrices $A_B,A_N$ are the submatrices of $A$ formed by the columns with indices $i\in B$ and $i\in N$, respectively, and the vectors $x_B,x_N$ are the subvectors of $x$ formed by the components with indices $i\in B$ and $i\in N$, respectively. If $i\in B$, then $x_i$ is called a **basic variable**; otherwise $x_i$ is called a **non-basic variable**. The set of all basic variables is called a **basis**; in this article a basis is denoted by the corresponding index set $B$.

???+ tip "“Basis”"
    The name “basis” can be understood from the viewpoint of linear algebra. Let $V$ be the linear space spanned by all column vectors of $A$. Then the column vectors corresponding to the basis $B$ form a basis of the space $V$.

In the expression for the basic variables $x_B$, setting $x_N=0$ gives a solution of all the equality constraints[^notation]

$$
x = (x_B,x_N) = (A_B^{-1}b,0).
$$

The solution obtained this way is called a **basic solution** of the linear programming problem. If it also satisfies all the nonnegativity constraints, i.e., $x \ge 0$, then it is also a feasible solution of the original problem and is called a **basic feasible solution** (BFS). During the iterations of the simplex method, the current solution must always be kept a basic feasible solution.

### Pivoting

Each iteration of the simplex method is called a **pivot** (pivoting). In terms of the result, each pivot always removes an old basic variable and adds a new basic variable, thereby improving the value of the objective function.

???+ tip "“Pivoting”"
    The name “pivoting” (literally “turning an axis”) can likewise be understood from the viewpoint of linear algebra. As mentioned above, the column vectors corresponding to the basis $B$ form a basis of the space $V$, so they also correspond to the coordinate axes of the space $V$ represented in that basis. Therefore, the pivoting process is the process of rotating one coordinate axis to a new position.

To determine which basic variable to add, we can express the objective function in terms of the nonbasic variables as

$$
\begin{aligned}
c^Tx &= c^T_Bx_B + c^T_Nx_N \\
&= c_B^TA_B^{-1}b + (c_N^T - c_B^TA_B^{-1}A_N)x_N.
\end{aligned}
$$

Setting $x_N=0$ gives the value of the objective function at the current basic feasible solution, $z=c_B^TA_B^{-1}b$. The coefficients of the second term in the expression describe how the objective function changes as $x_N$ changes:

$$
\tilde c_N = \dfrac{\partial z}{\partial x_N} = c_N - A_N^T(A_B^{-1})^Tc_B.
$$

Note that $c_B - A_B^T(A_B^{-1})^Tc_B = 0$, so we may call the vector

$$
\tilde c = (\tilde c_B^T,\tilde c_N^T)^T = c - A^T(A_B^{-1})^Tc_B
$$

the **reduced cost** of the linear programming problem at the basic feasible solution $x$. A component $\tilde c_i<0$ means that increasing the value of the variable $x_i$ improves the objective function of the original problem. Such a variable can only be a nonbasic variable, and it is called the **entering variable** of this pivot, because after the pivot $x_i$ becomes a basic variable and is no longer always set to zero (although it may still equal zero).

After choosing the entering variable, we still need to choose the old basic variable to remove. For this, we only need to determine which existing basic variable becomes zero first as $x_i$ increases. Substituting $x_N=(x_i,x_{N\setminus\{i\}})=(x_i,0)$ into the expression for $x_B$ gives

$$
x_B = A_B^{-1}b - A_B^{-1}A_ix_i.
$$

Therefore, the maximum amount by which $x_i$ can be increased equals

$$
\theta = \min\left\{\dfrac{(A_B^{-1}b)_j}{(A_B^{-1}A_i)_j}:(A_B^{-1}A_i)_j>0\right\}.
$$

The variable that becomes zero first is the basic variable $x_{B_j}$ corresponding to the index $j$ at which this expression attains its minimum. It is also the “bottleneck” in the process of increasing $x_i$: increasing $x_i$ further would make $x_{B_j}$ negative. This variable is the **leaving variable** of this pivot. The method of determining the leaving variable is called the **minimum ratio test**.

Let the entering variable be $x_i$ and the leaving variable be $x_{i'}$. After the pivot, the basic variables are $x_{B\setminus\{i'\}\cup\{i\}}$ and the nonbasic variables are $x_{N\setminus\{i\}\cup\{i'\}}$.

### Termination conditions

The simplex method is the process of starting from a basic feasible solution and pivoting repeatedly. The discussion of pivoting in the previous section was not complete: it ignored some special cases. Some of these special cases correspond to termination of the algorithm, while others require extra handling.

First, the entering variable may not exist, i.e., $\tilde c\ge 0$. In this case there is no way to further improve the optimal value, which means the current basic feasible solution is optimal, and the algorithm terminates. To prove this rigorously, we need the [complementary slackness conditions](./linear-programming.md#互补松弛条件). Let $y=(A_B^{-1})^Tc_B$. Note that throughout the algorithm, $x$ always remains a feasible solution and the complementary slackness conditions hold, i.e.,

$$
x^T(c-A^Ty) = \tilde c^Tx = \tilde c_B^Tx_B + \tilde c_N^Tx_N = 0.
$$

Therefore, as long as $y$ is a feasible solution of the dual problem, i.e., $A^Ty\le c$, we can conclude that $x$ and $y$ are optimal solutions of the primal and dual problems, respectively. This condition is exactly $\tilde c\ge 0$, i.e., no entering variable exists.

???+ tip "“Shadow price”"
    The vector $y=(A_B^{-1})^Tc_B$ is often called the **dual vector**. When the basic feasible solution corresponding to $B$ is an optimal solution of the primal problem, the vector $y$ is an optimal solution of the dual problem. Therefore, when solving the primal problem with the simplex method, we also obtain an optimal solution of the dual problem. Since the vector $y$ is the partial derivative of the current value with respect to the constraint constants, i.e.,
    
    $$
    \dfrac{\partial(c^Tx)}{\partial b} = (A_B^{-1})^Tc_B = y,
    $$
    
    it is also called the **shadow price**.

Second, the leaving variable may not exist, i.e., $A_B^{-1}A_i\le 0$. In this case there is no “bottleneck” in the pivoting process, which means the objective function can be improved indefinitely by increasing the value of $x_i$, making it tend to $-\infty$. This means the given linear programming problem is unbounded, and the algorithm terminates.

Finally, the choice of the entering and leaving variables may not be unique. An inappropriate choice may lead to too many pivots, or even make the algorithm cycle and fail to terminate. Handling these situations is slightly more complicated and requires applying some [pivot rules](#pivot-rules) to prevent cycling and reduce the number of pivots.

### Simplex tableau

When implementing the pivoting process concretely, we only need to maintain the coefficient matrix of the linear programming problem after each pivot:

$$
\tilde T_B = 
\begin{pmatrix}
-z_B & \tilde c^T_N \\
x_B & A_B^{-1}A_N
\end{pmatrix}
=
\begin{pmatrix}
-c_B^TA_B^{-1}b & c_N^T - c_B^TA_B^{-1}A_N \\
A_B^{-1}b & A_B^{-1}A_N 
\end{pmatrix}.
$$

It corresponds to the linear programming problem:

$$
\begin{array}{rrrr}
\min_{x\ge 0}    &       & c_B^TA_B^{-1}b & + \tilde c_N^Tx_N\; \\
\text{subject to}& x_B = & A_B^{-1}b      & - A_B^{-1}A_Nx_N.
\end{array}
$$

The matrix $\tilde T_B$ is called the **condensed simplex tableau** of the linear programming problem with respect to the basis $B$. The top-left corner of the tableau, $(\tilde T_B)_{00}$, is (the negative of) the value of the current solution; the entry $(\tilde T_B)_{0i}$ in row $0$, column $i$ is the reduced cost of the $i$-th nonbasic variable $x_{N_i}$; the entry $(\tilde T_B)_{j0}$ in row $j$, column $0$ is the value of the $j$-th basic variable $x_{B_j}$; and $A_B^{-1}A_N$ consists of the coefficients in the expression of the basic variables $x_B$ in terms of the nonbasic variables $x_N$.

It is easy to see that all the information needed for a pivot can be read directly from the condensed simplex tableau. Concretely, using the condensed simplex tableau, a single pivot consists of the following operations:

1.  Choose a column $i=1,\cdots,n-m$ such that $(\tilde T_B)_{0i}<0$. If no such $i$ exists, the current solution is optimal, and $-(\tilde T_B)_{00}$ is the optimal value.
2.  Choose a row $j=1,\cdots,m$ such that $(\tilde T_B)_{ji}>0$ and $(\tilde T_B)_{j0}/(\tilde T_B)_{ji}$ is minimal. If no such $j$ exists, the original problem is unbounded.
3.  Let the variable $x_{N_i}$ enter the basis, let the variable $x_{B_j}$ leave the basis, and update the simplex tableau.

Now let us discuss concretely how to update the simplex tableau. Before the update, row $j$ represents the equation

$$
x_{B_j} = (\tilde T_B)_{j0} - \sum_{i=1}^{n-m}(\tilde T_B)_{ji}x_{N_i}.
$$

To update the simplex tableau, we need to express $x_{N_i}$ in terms of $x_{N\setminus\{N_i\}\cup\{B_j\}}$, that is:

$$
x_{N_i} = \dfrac{(\tilde T_B)_{j0}}{(\tilde T_B)_{ji}} - \dfrac{1}{(\tilde T_B)_{ji}}x_{B_j} - \sum_{i'\neq i}\dfrac{(\tilde T_B)_{ji'}}{(\tilde T_B)_{ji}}x_{N_{i'}}.
$$

Substituting it into the remaining equations, we get

$$
x_{B_{j'}} = \left((\tilde T_B)_{j'0} - (\tilde T_B)_{j'i}\dfrac{(\tilde T_B)_{j0}}{(\tilde T_B)_{ji}}\right) + \dfrac{(\tilde T_B)_{j'i}}{(\tilde T_B)_{ji}}x_{B_j} - \sum_{i'\neq i}\left((\tilde T_B)_{j'i'}-(\tilde T_B)_{j'i}\dfrac{(\tilde T_B)_{ji'}}{(\tilde T_B)_{ji}}\right)x_{N_{i'}}.
$$

Row $0$ is similar, except that the left-hand side of the equation becomes $-z_B$. Although the formulas look complicated, the implementation requires only two steps:

1.  Update row $j$: let $\alpha=(\tilde T_B)_{ji}$, set the entry in column $i$ to $1$, and then divide every entry of the row by $\alpha$;
2.  Update each row $j'\neq j$: let $\beta=(\tilde T_B)_{j'i}$, set the entry in column $i$ to $0$, and then subtract $\beta$ times row $j$ from the entire row.

???+ tip "“Simplex tableau”"
    The **simplex tableau** is the matrix
    
    $$
    T_B = 
    \begin{pmatrix}
    -z_B & \tilde c^T \\
    x_B & A_B^{-1}A 
    \end{pmatrix}
    =
    \begin{pmatrix}
    -c_B^TA_B^{-1}b & c^T - c_B^TA_B^{-1}A \\
    A_B^{-1}b & A_B^{-1}A 
    \end{pmatrix}.
    $$
    
    Compared with the condensed simplex tableau, it has $m$ more columns, corresponding to the $m$ basic variables; moreover, the column corresponding to the $j$-th basic variable is always $e_j$, i.e., the vector that is $1$ only in row $j$ and $0$ in all other rows. Since these columns provide no extra information, they are often omitted when implementing the simplex method, which yields the condensed simplex tableau.
    
    The simplex tableau makes it easier to understand the steps for updating the tableau. Since every simplex tableau $T_B$ can be obtained by multiplying the same matrix $T_0$ on the left by an invertible matrix $L_B$ that depends on the basis, i.e.,
    
    $$
    T_B=
    \begin{pmatrix}
    -c_B^TA_B^{-1}b & c^T - c_B^TA_B^{-1}A \\
    A_B^{-1}b & A_B^{-1}A 
    \end{pmatrix}
    =
    \begin{pmatrix}
    1 & -c_B^TA_B^{-1} \\
    O & A_B^{-1}
    \end{pmatrix}
    \begin{pmatrix}
    0 & c^T \\
    b & A 
    \end{pmatrix}=L_BT_0,
    $$
    
    these simplex tableaus and $T_0$ can be transformed into one another by a number of [elementary row operations](./linear-algebra/elementary-operations.md). Therefore, when updating the simplex tableau, it suffices to perform elementary row operations so that the column corresponding to the entering variable becomes $e_j$. Transferring the required operations to the condensed simplex tableau gives exactly the steps described above.

A reference implementation of updating the condensed simplex tableau follows:

???+ example "Reference implementation"
    ```cpp
    --8<-- "docs/math/code/simplex/simplex_0.cpp:pivot"
    ```

From this implementation we see that the time complexity of a single update of the simplex tableau is $O(mn)$. When discussing [pivot rules](#pivot-rules) later, we will show that the complexity of determining the leaving and entering variables also does not exceed $O(mn)$, so the time complexity of a single pivot is $O(mn)$.

For ease of understanding, we list here the detailed steps of the computation with the condensed simplex tableau for the example shown earlier.

???+ example "Example (continued)"
    Initially, the condensed simplex tableau is as follows:
    
    $$
    \begin{array}{|l|c|ccc|}
    \hline
        &    & x_1 & x_2 & x_3 \\
    \hline
        & 0  & -10 & -12 & -12 \\
    \hline
    x_4= & 20 &   1 & 2   &   2 \\
    x_5= & 20 &   2 & 1   &   2 \\
    x_6= & 20 &   2 & 2   &   1 \\
    \hline
    \end{array}
    $$
    
    According to the reduced costs in row $0$, any of $x_1,x_2,x_3$ may enter the basis. Let $x_1$ enter. Then, by the minimum ratio test, either of $x_5,x_6$ may leave the basis. Let $x_5$ leave. The condensed simplex tableau is updated as follows:
    
    $$
    \begin{array}{|l|c|ccc|}
    \hline
        &    & x_5 & x_2 & x_3 \\
    \hline
        &100 & 5   & -7  & -2  \\
    \hline
    x_4= & 10 &-0.5 & 1.5 &   1 \\
    x_1= & 10 & 0.5 & 0.5 &   1 \\
    x_6= &  0 & -1  & 1   &  -1 \\
    \hline
    \end{array}
    $$
    
    According to the reduced costs in row $0$, either of $x_2,x_3$ may enter the basis. Let $x_3$ enter. Then, by the minimum ratio test, either of $x_4,x_1$ may leave the basis. Let $x_4$ leave. The condensed simplex tableau is updated as follows:
    
    $$
    \begin{array}{|l|c|ccc|}
    \hline
        &    & x_5 & x_2 & x_4 \\
    \hline
        &120 & 4   & -4  & 2   \\
    \hline
    x_3= & 10 &-0.5 & 1.5 &  1  \\
    x_1= &  0 &  1  & -1  & -1  \\
    x_6= & 10 & -1.5& 2.5 &  1  \\
    \hline
    \end{array}
    $$
    
    According to the reduced costs in row $0$, only $x_2$ may enter the basis. Let $x_2$ enter. Then, by the minimum ratio test, only $x_6$ may leave the basis. Let $x_6$ leave. Using the elementary row operations described above, the simplex tableau is updated as follows:
    
    $$
    \begin{array}{|l|c|ccc|}
    \hline
        &    & x_5 & x_6  & x_4 \\
    \hline
        &136 & 1.6 & 1.6 & 3.6 \\
    \hline
    x_3= & 4  & 0.4 &-0.6 & 0.4 \\
    x_1= &  4 & 0.4 & 0.4 &-0.6 \\
    x_2= &  4 & -0.6& 0.4 & 0.4 \\
    \hline
    \end{array}
    $$
    
    According to the reduced costs in row $0$, no entering variable exists. Therefore, the current solution
    
    $$
    x=(4,4,4,0,0,0)^T
    $$
    
    is optimal, and the optimal value (of the minimization problem) is $-136$.

Besides implementing the simplex method with a simplex tableau, one can also use the revised simplex method, which further improves the time and space complexity of the algorithm, reducing the complexity of a single update to $O(m^2)$; it is especially efficient when $m\ll n$ or when $A$ is a sparse matrix.

## Geometric background

This section introduces the geometric background of the simplex method.

The [analysis](./linear-programming.md#可行域与问题的解) of the feasible region of a linear programming problem

$$
\mathcal D = \{x\in\mathbf R^n : Ax = b,~ x\ge 0\}
$$

shows that:

-   An optimal solution of a linear programming problem (if it exists) can always be chosen to be a vertex of the feasible region $\mathcal D$. Solving the linear programming problem thus becomes finding, among all vertex solutions, the one with the best objective value.
-   The coordinates of each vertex can be obtained by solving the system of equations formed by $n$ tight constraints. For constraints in standard form, all $m$ equality constraints are necessarily tight, and the remaining $n-m$ constraints can only be chosen from the nonnegativity constraints. Choosing these nonnegativity constraints as tight constraints amounts to setting the corresponding decision variables $x_N$ to $0$; accordingly, the system $Ax = b$ reduces to the system of linear equations $A_Bx_B = b$ in the remaining $m$ decision variables $x_B$. As long as $A_B$ is invertible, we can solve $x_B = A_B^{-1}b$. This gives a solution $(x_B,x_N)=(A_B^{-1}b,0)$; if $x_B\ge 0$, these are the coordinates of a vertex of $\mathcal D$.

It is easy to see that the concept of a vertex solution coincides with the basic feasible solution defined earlier. Therefore, it suffices to find the best one among all basic feasible solutions to obtain an optimal solution of the original problem. Although this greatly simplifies the problem, the number of vertices of the feasible region may be exponential, so exhaustive enumeration is not realistic.

To overcome this difficulty, we can move along the [edges](./linear-programming.md#可行域与问题的解) of the feasible region, from one vertex to an adjacent vertex. Since adjacent vertices necessarily lie on the same edge, they satisfy at least $n-1$ common tight constraints. In other words, the tight constraints of adjacent vertices can and must differ in exactly one constraint. Therefore, for a basic feasible solution $x$, replacing one of its basic variables with a nonbasic variable yields an **adjacent** basic feasible solution $x'$. This is exactly the pivot operation.

Hence, the process in which the simplex method starts from a basic feasible solution and keeps pivoting to improve the objective function is in fact the process of starting from a vertex of the corresponding feasible region and repeatedly moving to adjacent vertices, improving the objective function along the way.

???+ example "Example (continued)"
    In the example discussed in this article, the feasible region is a three-dimensional polyhedron with five vertices, as shown in the figure below:
    
    ![](./images/simplex-geo.svg)
    
    Geometrically, the solution process described above corresponds to the following path among the vertices of the polyhedron:
    
    $$
    (0,0,0) \rightarrow (10,0,0) \rightarrow (0,0,10) \rightarrow (4,4,4).
    $$

## Implementation details

With the simplex tableau, we can already solve many linear programming problems. However, for the most general case, there are still many details of the simplex method worth exploring in depth.

### Slack form

The [method](./linear-programming.md#标准形式) of converting a linear programming problem from general form into standard form has already been discussed. However, to conveniently solve it with the simplex method, we also need to ensure that the coefficient matrix $A$ has full rank. Although it is feasible to first convert to standard form and then eliminate linearly dependent constraints, for simplicity the following strategy is usually adopted:

1.  Convert the linear programming problem into **inequality form**, i.e., the form $\min\{c^Tx : Ax \le b,~ x \ge 0\}$;
2.  By adding slack variables $s$, convert the problem into standard form: $\min\{c^Tx : Ax + s = b,~ x\ge 0,~ s \ge 0\}$.

The advantage of this is that the coefficient matrix $(A,I)$ of the resulting standard form always has full rank, and there always exists a (not necessarily feasible) basic solution $(x,s)=(0,b)$. This special standard form is also called **slack form**.

### Initial basic feasible solution

The simplex method described above always assumes that a basic feasible solution is known. Sometimes a basic feasible solution is easy to find. For example, if $b\ge 0$ in the slack form above, then $(x,s)=(0,b)$ is a basic feasible solution. This is the situation encountered in the numerical example earlier.

For the general case, the **two-phase method** can be used. In the two-phase method, the simplex method is run twice. The first phase solves a feasibility linear programming problem to obtain a basic feasible solution of the original problem. The second phase starts from this basic feasible solution and applies the simplex method to solve the original problem.

Suppose we have a problem in standard form $\min\{c^Tx : Ax = b \ge 0,~ x\ge 0\}$. In the first phase, we need to solve the problem

$$
\min\{1^Tx_a : Ax + x_a = b,~ x\ge 0,~ x_a\ge 0\}.
$$

This is essentially a feasibility linear programming problem, in which the newly added variables $x_a$ are also called **artificial variables**. It always has the basic feasible solution $(x,x_a)=(0,b)$, so it can be solved directly with the simplex method. If the optimal value of this problem is strictly greater than $0$, then there is no $x\ge 0$ such that $Ax=b$, i.e., the original problem is infeasible. If the optimal value of this problem equals $0$, then the artificial variables in its optimal solution can only be zero. If some artificial variables are still basic variables, they can be driven out of the basis by a few pivots. Finally, when all artificial variables are nonbasic, the basic solution obtained in the first phase can be used as the initial basic feasible solution for the second phase.

???+ note "Implementing the first phase without explicitly introducing artificial variables"
    When implementing the first phase, it is not necessary to introduce artificial variables explicitly. For an arbitrarily chosen initial basis $B$, we have
    
    $$
    x_B + A_B^{-1}A_Nx_N = A_B^{-1}b.
    $$
    
    If $(A_B^{-1}b)_j\ge 0$, no artificial variable is needed; otherwise, an additional artificial variable $x^{-}_{B_j}$ must be introduced, i.e.,
    
    $$
    x_{B_j} - x^-_{B_j} + (A_B^{-1}A_N)_{(j)}x_N = (A_B^{-1}b)_j.
    $$
    
    Denote the index set $L:=\{j:(A_B^{-1}b)_j<0\}$. Then every simplex tableau of the first phase is obtained from the following simplex tableau by a number of elementary row operations:
    
    $$
    \begin{array}{|r|c|cccc|}
    \hline
                    &                       & x_N                      & x_{B_{\sim L}} & x_{B_L}  &x_{B_{L}}^- \\  
    \hline
                    & 0                     & 0^T                      & 0^T            & 0^T      & 1^T        \\
    \hline
    x_{B_{\sim L}}=  & (A_B^{-1}b)_{\sim L}  & (A_B^{-1}A_N)_{(\sim L)} & I              &  O       &  O         \\
    x_{B_{L}}^-=     & (A_B^{-1}b)_L         & (A_B^{-1}A_N)_{(L)}      & O              &  I       & -I         \\
    \hline
    \end{array}
    $$
    
    Similarly to how the simplex tableau is reduced to the condensed simplex tableau, this one can be simplified appropriately (multiply the $x_{B_{L}}^-$ rows on the left by $1^T$ and add them to row $0$, then drop the last three columns):
    
    $$
    \begin{array}{|r|c|cccc|}
    \hline
                    &                      & x_N                      \\  
    \hline
                    & 1^T(A_B^{-1}b)_L     & 1^T(A_B^{-1}A_N)_{(L)}   \\
    \hline
    x_{B_{\sim L}}= & (A_B^{-1}b)_{\sim L} & (A_B^{-1}A_N)_{(\sim L)} \\
    -x_{B_{L}}=     & (A_B^{-1}b)_L        & (A_B^{-1}A_N)_{(L)}      \\
    \hline
    \end{array}
    $$
    
    This largely agrees with the ordinary condensed simplex tableau, except that the variables in the last row are marked with a negative sign, indicating that the row still contains an artificial variable, i.e., the original slack variable is still infeasible. Using this tableau, the pivoting process is as follows:
    
    1.  If $L=\varnothing$, the algorithm terminates.
    2.  Otherwise, choose the entering variable $x_{N_i}$ according to the condition that its reduced cost in row $0$ is negative. If none exists, the original problem is infeasible, and the algorithm terminates.
    3.  Then choose the leaving variable $x_{B_j}$ according to column $i$. The minimum ratio test is still used, but it must also ensure that the currently feasible variables stay feasible and the currently infeasible variables stay infeasible, i.e., choose
    
        $$
        \arg\min_{j}\left\{\dfrac{(\tilde T_B)_{j0}}{(\tilde T_B)_{ji}}:(j\notin L\land(\tilde T_B)_{ji}>0)\lor(j\in L\land(\tilde T_B)_{ji}<0)\right\}
        $$
    
        as the row of the leaving variable. If there are several such leaving variables, prefer an infeasible one.
    4.  Let $x_{N_i}$ enter the basis, let $x_{B_j}$ leave the basis, and update the simplex tableau.
    5.  If $j\in L$, remove $j$ from $L$ (i.e., remove the negative-sign mark from that row) and add one to $(\tilde T_B)_{0i}$.
    
    The columns of the artificial variables can be omitted because, while they are still basic variables, their columns are $e_j$ and need not be recorded, and once they are no longer basic, they will never enter the basis again and need not be recorded either. When an artificial variable leaves the basis, it must be replaced by the corresponding non-artificial variable; this is exactly the purpose of the last step of the above process.
    
    A reference implementation follows:
    
    ??? example "Reference implementation"
        ```cpp
        --8<-- "docs/math/code/simplex/simplex_0.cpp:initialize"
        ```
    
    Before the first phase begins, an extra row is added to record the first-phase objective function. When pivoting, the whole tableau is pivoted, including the second-phase objective function. In this way, when the first phase finishes, the second-phase objective function has also been updated accordingly, and the second-phase simplex method can start directly.

The two-phase method can also be carried out with a single run of the simplex method. It suffices to take a sufficiently large positive number $M$ and directly solve the problem

$$
\min\{c^Tx + M1^Tx_a : Ax + x_a = b,~ x\ge 0,~ x_a\ge 0\}
$$

to obtain an optimal solution of the original problem. In the implementation, $M$ is not assigned a concrete numerical value; instead, the computations treat $M$ as an unknown, sufficiently large positive number. This method is called the **big $M$ method**.

???+ warning "The practical efficiency of the naive algorithm is exponential"
    Since the slack form always has an initial basic solution, which merely may not be feasible, a simple idea for finding an initial basic feasible solution is the following: start from an infeasible basic solution, and repeatedly use pivots to drive infeasible basic variables out of the basis, letting the nonbasic variable whose column has a likewise negative entry in the corresponding row enter the basis, until all basic variables are nonnegative. A reference implementation follows:
    
    ??? example "Reference implementation"
        ```cpp
        --8<-- "docs/math/code/simplex/simplex_2.cpp:initialize"
        ```
    
    Although this is simple, compared with the two-phase method it has no objective function describing the degree of infeasibility of the current basis, so it lacks a clear direction of improvement. Practical tests show that, whereas the two-phase method or the big $M$ method usually needs only $O(m)$ pivots, this naive algorithm usually needs $O(2^m)$ pivots and easily falls into cycling when $n,m$ are large. Although the constant in the number of pivots of the naive algorithm is very small, it is only applicable when $n,m<50$.

### Pivot rules

When pivoting, if there are several candidate entering or leaving variables, a **pivot rule** is needed to decide which variable enters or leaves the basis. Using the simplex tableau, all the rules discussed in this section can find the entering and leaving variables in $O(mn)$ time, so the time complexity of a single pivot remains $O(mn)$.

The choice of the entering variable often determines the number of pivots before the algorithm terminates. Common rules are:

-   choose the first entering variable found;
-   choose the entering variable with the smallest index (part of Bland's rule);
-   choose the entering variable with the largest absolute value of the reduced cost (i.e., $|\tilde c_i|$) (Dantzig's rule);
-   choose the entering variable with the largest improvement of the objective value in a single pivot (i.e., $|\tilde c_i|\theta_i$);
-   choose the entering variable corresponding to the steepest edge, i.e., the one with the largest improvement of the objective value per unit length moved along the edge (i.e., $|\tilde c_i|/\sqrt{1+\|A_B^{-1}A_i\|^2}$);
-   choose an entering variable at random.

In practice, the steepest-edge rule is the most efficient[^steepest-edge]. It is generally believed that with a suitable pivot rule, the optimal solution of most problems is obtained within roughly $2m$ pivots. However, for every currently known pivot rule there exist specially constructed examples[^klee-minty] that force the number of pivots to be exponential. This is exactly why the simplex method runs very efficiently in practice, yet its theoretical worst-case complexity is exponential.

The choice of the leaving variable often determines whether the algorithm falls into cycling. If several bases correspond to the same basic feasible solution (i.e., the degenerate case), the algorithm may cycle among these bases forever. Such situations are not common, so many implementations of the simplex method do not specify a rule for choosing the leaving variable. There are two common rules for avoiding cycling:

-   Bland's rule: always choose the entering and leaving variables with the smallest indices.
-   Lexicographic rule: always choose the leaving variable $x_{B_j}$ corresponding to the row $j$ with $(A_B^{-1}A_i)_j>0$ for which

    $$
    \left(\dfrac{(A_B^{-1}b)_j}{(A_B^{-1}A_i)_j},\dfrac{(A_B^{-1})_{j1}}{(A_B^{-1}A_i)_j},\cdots,\dfrac{(A_B^{-1})_{jm}}{(A_B^{-1}A_i)_j}\right)
    $$

    is lexicographically smallest. The choice of the entering variable does not matter.

    Note that if the linear programming problem is in slack form, all these quantities can be found directly in the simplex tableau $T_B$ of the form described earlier; otherwise, after finding an initial basic solution (not necessarily feasible), the coefficients in the columns corresponding to the basic variables of this initial basis (with their order kept fixed) can be used as the coefficients of $A_B^{-1}$.

Bland's rule is very inefficient because the rule itself chooses the entering and leaving variables in the same way, which easily causes the same variable to repeatedly enter and then leave the basis. In comparison, the lexicographic rule is more practical. The lexicographic rule amounts to a small perturbation of the parameters of the linear programming problem[^lexico], so that no degenerate basic feasible solutions exist, and hence no cycling is possible.

## Reference implementation

This section provides a reference implementation of the two-phase simplex method based on the condensed simplex tableau.

??? example "[Luogu P13337【模板】线性规划 (Template: linear programming)](https://www.luogu.com.cn/problem/P13337)"
    ```cpp
    --8<-- "docs/math/code/simplex/simplex_0.cpp:full-text"
    ```

## Example problems

???+ example "[「NOI2008」志愿者招募 (Volunteer recruitment)](https://www.luogu.com.cn/problem/P3980)"
    An event lasting $n$ days in total needs volunteers, and on day $i$ at least $b_i$ volunteers are needed. There are $m$ types of volunteers; volunteers of type $j$ can serve during the contiguous interval of days $[l_j,r_j]$, and the unit recruitment cost is $c_j$. Find the optimal recruitment plan that minimizes the cost of recruiting volunteers.

??? note "Solution"
    Suppose $x_j$ volunteers of type $j$ are recruited. Then we can formulate the linear programming problem
    
    $$
    \begin{align*}
    \min_{x}\; & \sum_{j=1}^mc_jx_j \\
    \text{subject to }& \sum_{j=1}^m a_{ij}x_j \ge b_i,~i=1,\cdots,n,\\
    & x_j\ge 0,~j=1,\cdots,m.
    \end{align*}
    $$
    
    where the coefficients are
    
    $$
    a_{ij} = 
    \begin{cases}
    1,& l_j\le i\le r_j,\\
    0,& \text{otherwise.}
    \end{cases}
    $$
    
    The original problem has no obvious initial feasible solution. Therefore, consider its [dual problem](./linear-programming.md#对偶问题):
    
    $$
    \begin{align*}
    \max_{y}\; & \sum_{i=1}^n b_iy_i \\
    \text{subject to } & \sum_{i=1}^na_{ij}y_i \le c_j,~j=1,\cdots,m,\\
    & y_i\ge 0,~i=1,\cdots,n.
    \end{align*}
    $$
    
    By adding slack variables, an initial feasible solution is easily obtained, so the first phase can be skipped and the problem solved directly with the simplex method. By duality, the solution obtained is also the solution of the original problem.
    
    ```cpp
    --8<-- "docs/math/code/simplex/simplex_1.cpp"
    ```

## Exercises

-   [Luogu P13337【模板】线性规划 (Template: linear programming)](https://www.luogu.com.cn/problem/P13337)
-   [UOJ#179. 线性规划 (Linear programming)](https://uoj.ac/problem/179)
-   [Luogu P4232 无意识之外的捉迷藏 (Hide-and-seek beyond the unconscious)](https://www.luogu.com.cn/problem/P4232)
-   [Codeforces 1430 G. Yet Another DAG Problem](https://codeforces.com/problemset/problem/1430/G)
-   [AtCoder Beginner Contest 231 H - Minimum Coloring](https://atcoder.jp/contests/abc231/tasks/abc231_h)

## References

-   [线性规划之单纯形法【超详解 + 图解】(The simplex method in linear programming: a very detailed explanation with illustrations)](https://www.cnblogs.com/ECJTUACM-873284962/p/7097864.html)
-   [Papers of the 2016 Chinese national training team](https://github.com/OI-wiki/libs/blob/master/%E9%9B%86%E8%AE%AD%E9%98%9F%E5%8E%86%E5%B9%B4%E8%AE%BA%E6%96%87/%E5%9B%BD%E5%AE%B6%E9%9B%86%E8%AE%AD%E9%98%9F2016%E8%AE%BA%E6%96%87%E9%9B%86.pdf)
-   Introduction to Algorithms (算法导论)
-   Matoušek, Jiří, and Bernd Gärtner. Understanding and using linear programming. Vol. 1. Berlin: Springer, 2007.
-   Inayatullah, Syed, Nasir Touheed, and Muhammad Imtiaz. "A streamlined artificial variable free version of simplex method." PloS one 10, no. 3 (2015): e0116156.
-   Floudas, Christodoulos A., and Panos M. Pardalos, eds. Encyclopedia of optimization. Springer Science & Business Media, 2008.

[^notation]: In principle, since all vectors are column vectors by default, $(x_B,x_N)$ should be written as $(x_B^T,x_N^T)^T$. However, to simplify notation, all similar cases in this article are written directly as $(x_B,x_N)$, with the transpose symbol omitted.

[^steepest-edge]: For test results, see Forrest, John J., and Donald Goldfarb. "Steepest-edge simplex algorithms for linear programming." Mathematical programming 57, no. 1 (1992): 341-374.

[^klee-minty]: A classic counterexample can be found in Klee, Victor, and George J. Minty. "How good is the simplex algorithm." Inequalities 3, no. 3 (1972): 159-175.

[^lexico]: A detailed explanation can be found in [these lecture notes](https://misha.fish/archive/docs/3272-fall-2022/lecture8.pdf).
