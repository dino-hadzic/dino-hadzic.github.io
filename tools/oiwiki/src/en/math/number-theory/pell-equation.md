---
title: Pell's equation
---

Prerequisites: [Continued fractions](./continued-fraction.md), [Quadratic fields](./quadratic.md)

## Introduction

This article discusses solving the (generalized) Pell equation. The generalized Pell equation is the Diophantine equation in $x$ and $y$

$$
x^2-Dy^2=N,
$$

where $D$ is a positive integer that is not a perfect square[^not-square] and $N$ is a nonzero integer. Pell's equation in the narrow sense refers to the special case $N=1$ or $N=\pm 1$, and sometimes also includes the case $N=\pm 4$. The generalized Pell equation is closely related to finding quadratic integers of norm $N$ in a ring of real quadratic integers, and the cases usually called Pell's equation (in the narrow sense) can be viewed as finding the units of a ring of real quadratic integers.

When this article mentions Pell's equation, it refers specifically to the case $N=1$. Correspondingly, the case $N=-1$ is called the negative Pell equation[^neg-pell] (negative Pell's equation).

## Structure of the solutions

The integer solutions $(x,y)$ of the generalized Pell equation are closely related to the quadratic integer $x+y\sqrt{D}$, so in the literature the solutions of Pell's equation are often written in the form $x+y\sqrt{D}$. Since the norm of a quadratic integer is

$$
N(x+y\sqrt{D}) = x^2-Dy^2,
$$

the generalized Pell equation roughly amounts to finding quadratic integers of norm $N$. However, there is indeed a subtle difference between the two. When $x$ and $y$ are both integers, $x+y\sqrt{D}$ is certainly a quadratic integer; conversely, a quadratic integer does not necessarily require $x$ and $y$ to both be integers — in the case $D\equiv 1\pmod 4$, $x$ and $y$ can also both be half-integers[^half-int].

This difference is especially important when finding the fundamental unit. The units of a ring of quadratic integers are the quadratic integers of norm $\pm 1$. For $D\equiv 2,3\pmod 4$, to find such units it suffices to solve the generalized Pell equation in the case $N=\pm 1$; but for $D\equiv 1\pmod 4$, the case $N=\pm 4$ must also be considered. The method for finding units is discussed [below](#the-case-of-norm-4).

To understand the structure of the solutions of the generalized Pell equation, we start from [Brahmagupta's identity](https://en.wikipedia.org/wiki/Brahmagupta%27s_identity):

$$
(x_1^2-Dy_1^2)(x_2^2-Dy_2^2)=(x_1x_2+Dy_1y_2)^2-D(x_1y_2+x_2y_1)^2.
$$

It amounts to the fact that the norm of quadratic integers preserves multiplication, i.e.

$$
\begin{aligned}
N\left(x_1+y_1\sqrt{D}\right)N\left(x_2+y_2\sqrt{D}\right) &= N\left((x_1+y_1\sqrt{D})(x_2+y_2\sqrt{D})\right) \\
&= N\left((x_1x_2+Dy_1y_2)+(x_1y_2+x_2y_1)\sqrt{D}\right).
\end{aligned}
$$

Using this identity, integer solutions of the equation $x^2-Dy^2=N_1$ and the equation $x^2-Dy^2=N_2$ can be composed into an integer solution of the equation $x^2-Dy^2=N_1N_2$. Of course, from the viewpoint of quadratic integers, composing solutions is just multiplying quadratic integers, which shows the convenience of writing the solutions of Pell's equation as quadratic integers. In particular, taking $N_1=N$ and $N_2=1$, we see that if we know one solution of $x^2-Dy^2=N$ and all solutions of the corresponding Pell equation $x^2-Dy^2=1$, we can obtain more solutions of $x^2-Dy^2=N$. Of course, this method does not necessarily generate all solutions. But it at least shows that understanding the structure of the solutions of Pell's equation plays an important role in understanding the structure of the solutions of the generalized Pell equation.

### Pell's equation

Geometrically, the equation $x^2-Dy^2=1$ is a hyperbola whose real axis is the $x$-axis and whose imaginary axis is the $y$-axis. Every point of the hyperbola corresponds uniquely to a nonzero value of $x+y\sqrt{D}$: the left branch of the hyperbola corresponds to negative values of $x+y\sqrt{D}$, and the right branch to positive values. Moreover, on each branch the values of $x+y\sqrt{D}$ strictly increase as we move along the hyperbola from bottom to top. The value of the quadratic integer thus gives the solutions of Pell's equation a natural order.

The hyperbola is symmetric with respect to both the $x$-axis and the $y$-axis, so when discussing the solutions of Pell's equation it suffices to consider the part in the first quadrant; the remaining solutions can be obtained by symmetry. This amounts to considering only the solutions with $x+y\sqrt{D}>1$. If the equation has nontrivial solutions other than $(\pm 1,0)$, then there certainly exists a solution $(x_1,y_1)$ in the first quadrant with the smallest value of $x+y\sqrt{D}$; it is also the lattice point in the first quadrant (excluding the coordinate axes) with both the smallest abscissa and the smallest ordinate, and it is called the fundamental solution of Pell's equation[^fundamental-solution]. By the preceding discussion, all integer pairs $(x_k,y_k)$ satisfying $x_k+y_k\sqrt{D}=(x_1+y_1\sqrt{D})^k$ are solutions of Pell's equation, and all of them lie in the first quadrant. Conversely, these are indeed all the solutions of Pell's equation in the first quadrant. Using symmetry again, we obtain the following conclusion:

???+ note "Theorem"
    Let $(x_1,y_1)$ be the fundamental solution of Pell's equation $x^2-Dy^2=1$. Then the set of all its solutions is
    
    $$
    \{(x,y):x+y\sqrt{D}=\pm(x_1+y_1\sqrt{D})^k,k\in\mathbf Z\}.
    $$

??? note "Proof"
    We first prove that there are no other solutions in the first quadrant. Suppose, to the contrary, that there is another solution $x+y\sqrt{D}$ and that for some $k\ge 0$ we have
    
    $$
    x_k+y_k\sqrt{D}< x+y\sqrt{D}< x_{k+1}+y_{k+1}\sqrt{D}.
    $$
    
    Geometrically, this says that the lattice point $(x,y)$ falls on the hyperbola between $(x_k,y_k)$ and $(x_{k+1},y_{k+1})$ (endpoints excluded). Multiplying the inequality by $x_k-y_k\sqrt{D}=(x_k+y_k\sqrt{D})^{-1}$, we get
    
    $$
    1< (x+y\sqrt{D})(x_k-y_k\sqrt{D})=(xx_k-Dyy_k)+(x_ky-xy_k)\sqrt{D} < x_1+y_1\sqrt{D}.
    $$
    
    By the monotonicity mentioned above, this inequality says that $(xx_k-Dyy_k,x_ky-xy_k)$ is a lattice point lying between $(1,0)$ and $(x_1,y_1)$. This contradicts the choice of $(x_1,y_1)$.
    
    When extending the solutions in the first quadrant to the whole plane, negating the exponent $k$ (i.e. taking the reciprocal of the whole expression) is the reflection in the $x$-axis, and negating the whole expression is the reflection in the origin. Adding the trivial solution for $k=0$, we obtain all solutions of Pell's equation.

The preceding discussion only assumed the existence of the fundamental solution. What we now need to show is that Pell's equation always has a nontrivial solution.

???+ note "Theorem"
    Pell's equation $x^2-Dy^2=1$ always has an integer solution other than $(\pm 1,0)$.

??? note "Proof"
    First, [Dirichlet's theorem](./continued-fraction.md#用渐近分数逼近实数) shows that there are infinitely many pairs of positive integers $(x,y)$ such that
    
    $$
    \left|\dfrac{x}{y}-\sqrt{D}\right| \le \dfrac{1}{y^2}
    $$
    
    holds, and they all satisfy the inequality
    
    $$
    |x^2-Dy^2|=y^2\left|\dfrac{x}{y}-\sqrt{D}\right|\left|\dfrac{x}{y}+\sqrt{D}\right| \le \dfrac{1}{y^2}+2\sqrt{D}<1+2\sqrt{D}.
    $$
    
    Hence there must exist an integer $m\in(-1-2\sqrt{D},1+2\sqrt{D})$ such that infinitely many pairs $(x,y)$ satisfy $x^2-Dy^2 = m$. Classifying these $(x,y)$ by their residues modulo $m$, we see that for some pair of integers $(x_0,y_0)$ there must exist infinitely many pairs $(x,y)$ such that $x\equiv x_0\pmod m$ and $y\equiv y_0\pmod m$ hold. Taking any two distinct pairs $(x_1,y_1)$ and $(x_2,y_2)$ satisfying these conditions, we have
    
    $$
    \dfrac{x_1+y_1\sqrt{D}}{x_2+y_2\sqrt{D}}=\dfrac{x_1x_2-Dy_1y_2}{m}+\dfrac{x_2y_1-x_1y_2}{m}\sqrt{D}.
    $$
    
    Since by the congruences
    
    $$
    \begin{aligned}
    x_1x_2-Dy_1y_2 &\equiv x_0^2-Dy_0^2 = m \equiv 0 \pmod{|m|},\\
    x_2y_1-x_1y_2 &\equiv x_0y_0-x_0y_0 = 0 \pmod{|m|},
    \end{aligned}
    $$
    
    this shows that the right-hand side above is an integer solution. Moreover, since $(x_1,y_1)\neq(x_2,y_2)$, it is not trivial. This shows that Pell's equation indeed has a nontrivial solution.

Of course, the proof given in this section is non-constructive; when we discuss the method of solving Pell's equation below, we will directly construct a solution of Pell's equation from the convergents of a continued fraction, thereby providing another proof that Pell's equation has a nontrivial solution. In addition, although the structure of the solutions of Pell's equation obtained in this section agrees with the structure of the units of the ring of real quadratic integers, for the case $D\equiv 1\pmod 4$ this section has not completely settled the structure of the units of the corresponding ring of quadratic integers; this will be discussed further below.

### Generalized Pell equation

The graph of the generalized Pell equation $x^2-Dy^2=N$ is also a hyperbola in the plane, also with the $x$-axis and the $y$-axis as axes of symmetry. It was pointed out above that some solutions of the equation $x^2-Dy^2=N$ may differ only by a factor that is a solution of Pell's equation, which means the solutions of $x^2-Dy^2=N$ can be partitioned into equivalence classes. For two solutions $(x_1,y_1)$ and $(x_2,y_2)$ of the equation $x^2-Dy^2=N$, if there is a solution $(u,v)$ of Pell's equation such that $x_2+y_2\sqrt{D}=(x_1+y_1\sqrt{D})(u+v\sqrt{D})$ holds, then the solutions $(x_1,y_1)$ and $(x_2,y_2)$ are called equivalent. A necessary and sufficient condition for two solutions to be equivalent is

$$
N\mid (x_1x_2-Dy_1y_2),\ N\mid (x_2y_1-x_1y_2).
$$

Since the solutions of Pell's equation are relatively easy to find, a natural idea is to find one solution in each of the equivalence classes above. Once these solutions are known, all the required solutions of the generalized Pell equation can be obtained using the solutions of the corresponding Pell equation. Among the equivalence classes of solutions of the generalized Pell equation, by symmetry, every equivalence class has a solution whose ordinate $y$ is nonnegative and as small as possible: if such a solution is unique, it is called the fundamental solution of that equivalence class; otherwise, the equivalence class necessarily has two solutions with nonnegative and smallest $y$, and they are symmetric with respect to the $y$-axis; in this case the one with $x>0$ is chosen as the fundamental solution. Thus, solving the generalized Pell equation $x^2-Dy^2=N$ amounts to finding its set $U$ of fundamental solutions. Let $(r,s)$ be the fundamental solution of the corresponding Pell equation; then the set of all solutions of the generalized Pell equation is

$$
\{(x,y):x+y\sqrt{D}=\pm(r+s\sqrt{D})^k(u+v\sqrt{D}),k\in\mathbf Z,u+v\sqrt{D}\in U\}.
$$

The generalized Pell equation necessarily has finitely many fundamental solutions. This is because from the expression for the general solution above, the absolute value $|u+v\sqrt{D}|$ must lie between $r-s\sqrt{D}$ and $r+s\sqrt{D}$. The references at the end of the article give stricter estimates of the range of the coordinates of the fundamental solutions. Of course, unlike Pell's equation, the generalized Pell equation may have no solutions.

To obtain all solutions in the same equivalence class from one solution $(u,v)$ of the generalized Pell equation and the fundamental solution $(r,s)$ of Pell's equation, besides composing solutions one can also use the following recurrence

$$
x_{k} = 2rx_{k-1} - x_{k-2},\ y_{k} = 2ry_{k-1} - y_{k-2},
$$

where $x_k+y_k\sqrt{D}=(r+s\sqrt{D})^k(u+v\sqrt{D})$. This is because both $x_k$ and $y_k$ can be written, for some pair of real numbers $(A,B)$, in the form $A(r+s\sqrt{D})^k+B(r-s\sqrt{D})^k$, and by Vieta's formulas $r\pm s\sqrt{D}$ are the two real roots of the equation $x^2-2rx+1=0$, so $x_k$ and $y_k$ both satisfy the second-order linear recurrence with constant coefficients above. Compared with composing solutions, this recurrence requires fewer multiplications.

## Solution methods

Both Pell's equation and the generalized Pell equation can be solved using continued fractions.

### PQa algorithm

All the algorithms discussed in this article are based on the PQa algorithm, which can be used to compute the continued fraction expansion of a particular quadratic irrational.

Let integers $P_0,Q_0,D$ satisfy $Q_0\neq 0$, $D>0$ and not a perfect square, and $P_0^2\equiv D\pmod{Q_0}$. Then the continued fraction expansion $[a_0,a_1,\cdots]$ of the quadratic irrational

$$
\omega=\dfrac{P_0+\sqrt{D}}{Q_0}
$$

can be obtained by the following [recurrence formulas](./continued-fraction.md#二次无理数):

$$
a_k = \left\lfloor\dfrac{P_k+\sqrt{D}}{Q_k}\right\rfloor,\ P_{k+1} = a_kQ_k - P_k,\ Q_{k+1} = \dfrac{D-P_{k+1}^2}{Q_k}.
$$

Furthermore, the numerator $A_k$ and the denominator $B_k$ of the $k$-th convergent of $\omega$ are given by the following [recurrence formulas](./continued-fraction.md#递推关系):

$$
A_k = a_kA_{k-1} + A_{k-2},\ B_k = a_kB_{k-1} + B_{k-2}
$$

with $A_{-1} = 1$, $A_{-2}=0$, $B_{-1}=0$, $B_{-2}=1$.

The correctness of these formulas has already been proved in the article on continued fractions. It is also explained there that, since a quadratic irrational is a [periodic continued fraction](./continued-fraction.md#二次无理数), the triples $(P_k,Q_k,a_k)$ eventually enter a cycle, and the algorithm always terminates in finitely many steps. Let the minimal length of the period be $\ell$ and the earliest starting position of the period be $k_0$; then the continued fraction expansion of the quadratic irrational can be written as

$$
\omega=[a_0,\cdots,a_{k_0-1},\overline{a_{k_0},\cdots,a_{k_0+\ell-1}}].
$$

To solve Pell's equation with the PQa algorithm, we need to establish the following result:

???+ note "Theorem"
    Continue with the notation above. Let $G_k=Q_0A_k-P_0B_k$. Then the integer pair $(G_{k-1},B_{k-1})$ satisfies the relation
    
    $$
    G_{k-1}^2-DB_{k-1}^2=(-1)^{k}Q_0Q_{k},
    $$
    
    and their greatest common divisor $\gcd(G_{k-1},B_{k-1})$ divides $Q_{k}$.

??? note "Proof"
    In the continued fraction expansion of $\omega$, let the $k$-th remainder (complete quotient) be $\omega_{k}$, i.e.
    
    $$
    \omega = [a_0,a_1,\cdots,a_{k-1},\omega_k] = \dfrac{\omega_k A_{k-1}+A_{k-2}}{\omega_k B_{k-1}+B_{k-2}}.
    $$
    
    Substituting $\omega=(P_0+\sqrt{D})/Q_0$ and $\omega_k=(P_k+\sqrt{D})/Q_k$ into the equation above, we get
    
    $$
    \dfrac{P_0+\sqrt{D}}{Q_0} = \dfrac{(P_k+\sqrt{D})A_{k-1}+Q_kA_{k-2}}{(P_k+\sqrt{D})B_{k-1}+Q_kB_{k-2}}.
    $$
    
    Clearing the denominators on both sides, comparing the coefficients of the rational and irrational parts, and substituting the expression for $G_k$, we obtain the following equations:
    
    $$
    \begin{aligned}
    G_{k-1} &= P_kB_{k-1} + Q_kB_{k-2},\\
    DB_{k-1} &= P_kG_{k-1} + Q_kG_{k-2}.
    \end{aligned}
    $$
    
    Therefore, multiplying the first equation by $G_{k-1}$ and subtracting the second multiplied by $B_{k-1}$, we have
    
    $$
    \begin{aligned}
    G_{k-1}^2-DB_{k-1}^2 &= (B_{k-2}G_{k-1}-B_{k-1}G_{k-2})Q_k \\
    &= (A_{k-1}B_{k-2}-B_{k-1}A_{k-2})Q_0Q_k \\
    &= (-1)^kQ_0Q_k.
    \end{aligned}
    $$
    
    The last step uses the [difference formula](./continued-fraction.md#误差估计) for convergents. This proves the first claim.
    
    To prove the second claim, substitute the expression for $G_k$ into the first claim:
    
    $$
    (Q_0A_{k-1}-P_0B_{k-1})^2 - DB_{k-1}^2 = (-1)^kQ_0Q_k.
    $$
    
    So, using $Q_0\mid(P_0^2-D)$, we have
    
    $$
    Q_0A_{k-1}^2 +\left(\dfrac{P_0^2-D}{Q_0}B_{k-1}- 2P_0A_{k-1}\right)B_{k-1} = (-1)^kQ_k.
    $$
    
    Hence $\gcd(G_{k-1},B_{k-1}) = \gcd(Q_0A_{k-1},B_{k-1})$ divides $Q_k$.

This result provides a way of finding solutions of the equation $x^2-Dy^2=N$. If we choose $Q_0>0$ appropriately and choose $P_0$ to be a solution of the congruence $P_0^2\equiv D\pmod{Q_0}$, then by running the PQa algorithm on $(P_0+\sqrt{D})/Q_0$ until we find $(-1)^kQ_0Q_{k}=N$, the pair $(G_{k-1},B_{k-1})$ becomes a solution of the original equation. Moreover, if $Q_k=\pm 1$, then the solution obtained in this way is certainly primitive, that is, $G_{k-1}$ and $B_{k-1}$ are certainly coprime.

This idea is the core of solving Pell's equation and the generalized Pell equation. Having understood this idea, we now deal with some details of the algorithm and prove that all solutions can be obtained in this way.

### Pell's equation

To solve Pell's equation $x^2-Dy^2=1$, it suffices to run the PQa algorithm on $(P_0,Q_0,D)=(0,1,D)$ until $(-1)^kQ_k=1$ appears; then $(A_{k-1},B_{k-1})$ is a solution of Pell's equation (since $G_{k-1}$ is just $A_{k-1}$ in this case). Of course, for Pell's equation this process can be described more precisely.

First, the solution must appear at the end of the period. The process above amounts to expanding $\sqrt{D}$ as a continued fraction. For this, we already have the [result](./continued-fraction.md#纯循环连分数):

$$
\sqrt{D} = [\lfloor\sqrt{D}\rfloor,\overline{a_1,\cdots,a_{\ell-1},2\lfloor\sqrt{D}\rfloor}].
$$

Here the period length is $\ell$, and the period starts at the $1$st term (indices start from $0$). Moreover, its $\ell$-th remainder equals $\lfloor\sqrt{D}\rfloor+\sqrt{D}$, which shows that $Q_{\ell}=1$. Therefore, if $\ell$ is even, then $(A_{\ell-1},B_{\ell-1})$ is a nontrivial solution of Pell's equation; if $\ell$ is odd, then $(A_{2\ell-1},B_{2\ell-1})$ is a nontrivial solution of Pell's equation.

Next we need to show that the solution just obtained is certainly the fundamental solution. This conclusion rests on two reasons: first, the fractions $x/y$ corresponding to all positive integer solutions $(x,y)$ of Pell's equation appear among the convergents of $\sqrt{D}$, which guarantees that $(x,y)$ must be some $(A_k,B_k)$ produced during the PQa algorithm; second, apart from the end of the period, $Q_k=1$ does not appear at any other position, and since the recurrences for $A_k$ and $B_k$ guarantee that they grow as the index increases, the smallest positive integer solution (i.e. the fundamental solution) must appear at the position just indicated. These two reasons follow respectively from the following two theorems:

???+ note "Theorem"
    Let the equation $x^2-Dy^2=N$ have a positive integer solution $(x,y)$. If $|N|<\sqrt{D}$, then $\dfrac{x}{y}$ must equal a convergent of $\sqrt{D}$.

??? note "Proof"
    When $N>0$, since $x^2-Dy^2>0$, we have $x>y\sqrt{D}$. Hence
    
    $$
    \left|\dfrac{x}{y}-\sqrt{D}\right| = \dfrac{N}{y(x+y\sqrt{D})}<\dfrac{N}{2y^2\sqrt{D}}<\dfrac{1}{2y^2}.
    $$
    
    By [Legendre's criterion](./continued-fraction.md#渐近分数的判定), $\dfrac{x}{y}$ is a convergent of $\sqrt{D}$.
    
    When $N<0$, $x>y\sqrt{D}$ no longer holds. So instead we consider the solutions of the equation $y^2-\dfrac{1}{D}x^2=-\dfrac{N}{D}$. Since $\dfrac{|N|}{D}<\sqrt{\dfrac{1}{D}}$, the argument above still holds. This shows that $\dfrac{y}{x}$ is a convergent of $\dfrac{1}{\sqrt{D}}$. By the [reciprocal theorem](./continued-fraction.md#递推关系), $\dfrac{x}{y}$ is also a convergent of $\sqrt{D}$.

???+ note "Theorem"
    While running the PQa algorithm above on $(P_0,Q_0,D)=(0,1,D)$, $Q_k=1$ necessarily implies $\ell\mid k$.

??? note "Proof"
    In the continued fraction expansion of $\sqrt{D}$, all remainders except the $0$-th are [purely periodic continued fractions](./continued-fraction.md#纯循环连分数). Let $Q_k=1$. By Galois's result, the remainder $\omega_k=P_k+\sqrt{D}>1$ must have conjugate $-1<P_k-\sqrt{D}<0$, which shows that $P_k=\lfloor\sqrt{D}\rfloor$. Therefore the remainder $\omega_k$ equals $\omega_\ell$. But a repeated remainder means the continued fraction is periodic, so if $k$ is not a multiple of $\ell$, this contradicts $\ell$ being the smallest positive period. Hence necessarily $\ell\mid k$.

Summarizing the discussion of this section: it suffices to expand $\sqrt{D}$ as a continued fraction, i.e. run the PQa algorithm starting from $(P_0,Q_0,D)=(0,1,D)$, and when $Q_\ell=1$ is obtained for the first time, we have reached the end of the first period. At this point, if $\ell$ is even, then $(A_{\ell-1},B_{\ell-1})$ is the fundamental solution of Pell's equation; otherwise, $(A_{2\ell-1},B_{2\ell-1})$ is the fundamental solution of Pell's equation. For the case where the period length $\ell$ is odd, there is no need to continue the PQa algorithm to twice the period; we will show shortly that $A_{2\ell-1}+B_{2\ell-1}\sqrt{D}=(A_{\ell-1}+B_{\ell-1}\sqrt{D})^2$, so the fundamental solution of Pell's equation can be computed directly from $(A_{\ell-1},B_{\ell-1})$. All other solutions of Pell's equation can be computed from the fundamental solution of Pell's equation.

??? example "Examples"
    1.  Solve the equation $x^2-14y^2=1$.
    
        Running the PQa algorithm on $(P_0,Q_0,D)=(0,1,14)$ gives the following (the first period is marked in red):
    
        | $k$ | $P$ | $Q$ |        $a$       |  $A$  |  $B$ |  $G$  | $G^2-DB^2$ |
        | :-: | :-: | :-: | :--------------: | :---: | :--: | :---: | :--------: |
        | $0$ | $0$ | $1$ |        $3$       |  $3$  |  $1$ |  $3$  |    $-5$    |
        | $1$ | $3$ | $5$ | $\color{red}{1}$ |  $4$  |  $1$ |  $4$  |     $2$    |
        | $2$ | $2$ | $2$ | $\color{red}{2}$ |  $11$ |  $3$ |  $11$ |    $-5$    |
        | $3$ | $2$ | $5$ | $\color{red}{1}$ |  $15$ |  $4$ |  $15$ |     $1$    |
        | $4$ | $3$ | $1$ | $\color{red}{6}$ | $101$ | $27$ | $101$ |    $-5$    |
        | $5$ | $3$ | $5$ |        $1$       | $116$ | $31$ | $116$ |     $2$    |
    
        The period length $\ell=4$ is even. The smallest positive integer solution of the equation is $(G_3,B_3)=(15,4)$.
    2.  Solve the equation $x^2-41y^2=1$.
    
        Running the PQa algorithm on $(P_0,Q_0,D)=(0,1,41)$ gives the following (the first period is marked in red):
    
        | $k$ | $P$ | $Q$ |        $a$        |   $A$   |   $B$  |   $G$   | $G^2-DB^2$ |
        | :-: | :-: | :-: | :---------------: | :-----: | :----: | :-----: | :--------: |
        | $0$ | $0$ | $1$ |        $6$        |   $6$   |   $1$  |   $6$   |    $-5$    |
        | $1$ | $6$ | $5$ |  $\color{red}{2}$ |   $13$  |   $2$  |   $13$  |     $5$    |
        | $2$ | $4$ | $5$ |  $\color{red}{2}$ |   $32$  |   $5$  |   $32$  |    $-1$    |
        | $3$ | $6$ | $1$ | $\color{red}{12}$ |  $397$  |  $62$  |  $397$  |     $5$    |
        | $4$ | $6$ | $5$ |        $2$        |  $826$  |  $129$ |  $826$  |    $-5$    |
        | $5$ | $4$ | $5$ |        $2$        |  $2049$ |  $320$ |  $2049$ |     $1$    |
        | $6$ | $6$ | $1$ |        $12$       | $25414$ | $3969$ | $25414$ |    $-5$    |
        | $7$ | $6$ | $5$ |        $2$        | $52877$ | $8258$ | $52877$ |     $5$    |
    
        The period length $\ell=3$ is odd. The smallest positive integer solution of the equation is $(G_5,B_5)=(2049,320)$. It can also be computed from $(G_2,B_2)=(32,5)$:
    
        $$
        (32+5\sqrt{41})^2=2049+320\sqrt{41}.
        $$

### Negative Pell equation

By the discussion in the previous section, the solutions of the negative Pell equation must also correspond to convergents of $\sqrt{D}$, and can only appear where $(-1)^kQ_k=-1$. This can only happen at the end of the period. Therefore, the negative Pell equation has a solution if and only if the period length $\ell$ is odd. When a solution exists, $(A_{\ell-1},B_{\ell-1})$ is the fundamental solution of the negative Pell equation. The method of solving it is the same as in the previous section.

Using an approach similar to the earlier proof of the structure of the solutions of Pell's equation, the following result can be proved:

???+ note "Theorem"
    Let the equation $x^2-Dy^2=-1$ have a solution, with fundamental solution $(x_1,y_1)$. Then all integer solutions of $x^2-Dy^2=\pm 1$ belong to the set
    
    $$
    \{(x,y):x+y\sqrt{D}=\pm(x_1+y_1\sqrt{D})^k,k\in\mathbf Z\}.
    $$
    
    In particular, the integer solution $(x_2,y_2)$ satisfying $x_2+y_2\sqrt{D}=(x_1+y_1\sqrt{D})^2$ is exactly the fundamental solution of $x^2-Dy^2=1$.

??? note "Proof"
    By symmetry, it suffices to consider positive integer solutions, i.e. the case $x+y\sqrt{D}>1$. But since $x^2-Dy^2=\pm 1$ consists of two hyperbolas, $x+y\sqrt{D}$ cannot be put in one-to-one correspondence with $(x,y)$. To deal with this difficulty, we first prove that the $(x_2,y_2)$ above is the fundamental solution of $x^2-Dy^2=1$.
    
    Clearly, $(x_2,y_2)$ is a solution of $x^2-Dy^2=1$. If $(z,w)$ is the fundamental solution of $x^2-Dy^2=1$, then necessarily $1<z+w\sqrt{D}\le x_2+y_2\sqrt{D}$. If the inequality on the right is strict, then dividing the inequality by $x_1+y_1\sqrt{D}$ gives $-x_1+y_1\sqrt{D}<(z+w\sqrt{D})(-x_1+y_1\sqrt{D})<x_1+y_1\sqrt{D}$. Expanding the middle term of this inequality gives an expression of the form $x'+y'\sqrt{D}$, whose norm is $-1$ and where $(x',y')$ is also an integer solution. Taking reciprocals in this inequality, we find that $-x'+y'\sqrt{D}$ also falls between $-x_1+y_1\sqrt{D}$ and $x_1+y_1\sqrt{D}$. The quadratic integers $\pm x'+y'\sqrt{D}$ are reciprocals of each other, so one of them must be greater than $1$. But no other quadratic integer of norm $-1$ should appear between $1$ and $x_1+y_1\sqrt{D}$, which contradicts the minimality of $x_1+y_1\sqrt{D}$. Hence necessarily $x_2+y_2\sqrt{D}=z+w\sqrt{D}$, i.e. $(x_2,y_2)$ is the fundamental solution of the equation $x^2-Dy^2=1$.
    
    Based on this, if there were a solution $(x,y)$ of the equation $x^2-Dy^2=\pm 1$ not corresponding to any $(x_1+y_1\sqrt{D})^k$, then there would exist $k$ such that $(x_1+y_1\sqrt{D})^{2k}<x+y\sqrt{D}<(x_1+y_1\sqrt{D})^{2k+2}$; removing the factor $(x_1+y_1\sqrt{D})^{2k+1}$ shows that there is a quadratic integer $x'+y'\sqrt{D}\neq 1$ of norm $\pm 1$ lying between $-x_1+y_1\sqrt{D}$ and $x_1+y_1\sqrt{D}$. Repeating the reciprocal argument of the previous paragraph, this contradicts the minimality of $x_1+y_1\sqrt{D}$. Thus the original claim is proved.

Since $(A_{\ell-1},B_{\ell-1})$ is the smallest positive integer solution of the negative Pell equation, and all positive integer solutions of $x^2-Dy^2=\pm 1$ appear in the set

$$
\{(x,y):x+y\sqrt{D}=(A_{\ell-1}+B_{\ell-1}\sqrt{D})^k,k\in\mathbf N_+\}
$$

and since these positive integer solutions must correspond to the convergents of $\sqrt{D}$ at the end of a period (one position before it), and the numerators and denominators of the convergents are strictly increasing, for all $k\in\mathbf N_+$ we always have

$$
(A_{\ell-1}+B_{\ell-1}\sqrt{D})^k = A_{k\ell-1}+B_{k\ell-1}\sqrt{D}.
$$

Among all these positive integer solutions, those with odd $k$ are solutions of the negative Pell equation and those with even $k$ are solutions of Pell's equation; the two alternate.

To decide whether the negative Pell equation has a solution, one needs to compute the period length of the continued fraction expansion of $\sqrt{D}$, which is not easy to compute, so one would like to find a simpler criterion. However, there is currently no criterion with concise, easily computable conditions[^solubility-neg-pell]. Here we only give a simple result.

???+ note "Theorem"
    If the equation $x^2-Dy^2=-1$ has a solution, then $4$ does not divide $D$ and $D$ has no prime factor of the form $4k+3$. Conversely, if $D=2$ or $D$ is a prime of the form $4k+1$, then the equation necessarily has a solution.

??? note "Proof"
    First, if the negative Pell equation has a solution, this means that $-1$ is a quadratic residue modulo $D$, hence $-1$ is also a quadratic residue modulo any divisor $d$ of $D$, so $d\neq 4$ and $d$ is not a prime of the form $4k+3$. Conversely, the equation $x^2-2y^2=-1$ has the nontrivial solution $(1,1)$. What remains is the case where $D$ is a prime of the form $4k+1$.
    
    Let $D$ be a prime of the form $4k+1$; we need to prove that the equation $x^2-Dy^2=-1$ has a solution. The idea is to start from the fundamental solution $(u,v)$ of Pell's equation $x^2-Dy^2=1$ and construct a solution $(\alpha,\beta)$ of $x^2-Dy^2=-1$. If $u$ is even, reducing both sides of $u^2-Dv^2=1$ modulo $4$ gives $v^2\equiv -1\pmod 4$, but $-1$ is not a quadratic residue modulo $4$. This contradiction shows that $u$ is odd. Consider the equation $Dv^2=u^2-1=(u+1)(u-1)$. Since $u$ is odd, $\gcd(u+1,u-1)=\gcd(u+1,2)=2$. Based on this fact, distributing the factors of $Dv^2$ between $u+1$ and $u-1$, one of them must be $2\alpha^2$ and the other $2D\beta^2$, where $\alpha$ and $\beta$ are coprime positive integers and $v=2\alpha\beta$. Substituting $u=\alpha^2+D\beta^2$ and $v=2\alpha\beta$ into $u^2-Dv^2=1$ gives $\alpha^2-D\beta^2=\pm 1$. Since $(u,v)$ is the fundamental solution of Pell's equation and $(\alpha,\beta)$ is a pair of positive integers smaller than $(u,v)$, the right-hand side of this equation cannot be $+1$, so it can only be $-1$. This proves that $x^2-Dy^2=-1$ has the solution $(\alpha,\beta)$.

If $D$ is composite, then having no prime factor of the form $4k+3$ and being squarefree does not guarantee that the equation $x^2-Dy^2=-1$ has a solution; for example, $x^2-34y^2=-1$ has no solution.

??? example "Example"
    From the computations in the examples above, the equation $x^2-14y^2=-1$ has no solution, and the smallest positive integer solution of the equation $x^2-41y^2=-1$ is $(G_2,B_2)=(32,5)$.

### The case of norm ±4

Next we discuss the solutions of the equation $x^2-Dy^2=\pm 4$. Here the behavior of the solutions depends on the value of $D\bmod 4$.

Some cases are easy. If $D\equiv 0\pmod 4$, then $x$ is even, so $(x/2,y)$ is a solution of the equation $u^2-(D/4)v^2=\pm 1$. In the remaining cases, $x,y$ must be both odd or both even. If $x,y$ are both odd, reducing both sides of the equation modulo $4$ gives $D\equiv 1\pmod 4$. So if $D\equiv 2,3\pmod 4$, then $x,y$ can only be both even, hence $(x/2,y/2)$ is a solution of the equation $u^2-Dv^2=\pm 1$. Therefore, except for the case $D\equiv 1\pmod 4$, the solutions of the equation $x^2-Dy^2=\pm 4$ can all be obtained from the solutions of the corresponding (negative) Pell equation.

Now we discuss the case $D\equiv 1\pmod 4$, which cannot simply be reduced to the cases already solved. To find the fundamental solution, we can apply the PQa algorithm to $(P_0,Q_0,D)=(1,2,D)$; when $Q_\ell=2$ is obtained for the first time, we have reached the end of the first period. If the period length $\ell$ is even, then $(G_{\ell-1},B_{\ell-1})$ is the fundamental solution of the equation $x^2-Dy^2=4$; otherwise, $(G_{\ell-1},B_{\ell-1})$ is the fundamental solution of the equation $x^2-Dy^2=-4$. Starting from $(G_{\ell-1},B_{\ell-1})$, all solutions of the equation $x^2-Dy^2=\pm 4$ can be obtained:

$$
\left\{(x,y):\dfrac{x+y\sqrt{D}}{2}=\pm\left(\dfrac{G_{\ell-1}+B_{\ell-1}\sqrt{D}}{2}\right)^k,k\in\mathbf Z\right\}.
$$

If the period length $\ell$ is even, all of these are solutions of the equation $x^2-Dy^2=4$; otherwise, when $k$ is odd, $(x,y)$ is a solution of the equation $x^2-Dy^2=-4$, and when $k$ is even, $(x,y)$ is a solution of the equation $x^2-Dy^2=4$.

The correctness of this algorithm relies on the following facts:

???+ note "Theorem"
    Let the equation $x^2-Dy^2=\pm 4$ have a positive integer solution $(x,y)$. If $D\equiv 1\pmod 4$, then $\dfrac{(x+y)/2}{y}$ must be a convergent of $\dfrac{1+\sqrt{D}}{2}$.

??? note "Proof"
    First note that in this case $x,y$ must have the same parity, so $(x+y)/2$ is an integer. If $(x,y)$ is a solution of the equation $x^2-Dy^2=4$, then $x>y\sqrt{D}>2y$, so
    
    $$
    \left|\dfrac{(x+y)/2}{y}-\dfrac{1+\sqrt{D}}{2}\right| = \dfrac{2}{y(x+y\sqrt{D})}<\dfrac{1}{2y^2}.
    $$
    
    By [Legendre's criterion](./continued-fraction.md#渐近分数的判定), $\dfrac{(x+y)/2}{y}$ is a convergent of $\dfrac{1+\sqrt{D}}{2}$.
    
    If $(x,y)$ is a solution of the equation $x^2-Dy^2=-4$, then to establish the inequality above it suffices to prove $4y<x+y\sqrt{D}$. This holds at least for all cases except $D=5,13$. For the cases $D=5,13$, substituting $x=\sqrt{Dy^2-4}$ into this inequality shows that it is equivalent to $2(\sqrt{D}-2)y^2>1$. Except for $(D,y)=(5,1)$, this inequality holds for all $D=5,13$ and positive integers $y$. What remains is to verify the case $(D,y)=(5,1)$; here the solution of the equation $x^2-5y^2=-4$ is $(x,y)=(1,1)$, and what needs to be verified is that $\dfrac{1}{1}$ is a convergent of $\dfrac{1+\sqrt{5}}{2}=[\overline{1}]$, which obviously holds.

???+ note "Theorem"
    Let $D$ be a positive integer that is not a perfect square. The continued fraction expansion of the quadratic irrational $\omega=\dfrac{1+\sqrt{D}}{2}$ has the form
    
    $$
    \omega = [\lfloor\omega\rfloor,\overline{a_1,\cdots,a_{\ell-1},2\lfloor\omega\rfloor-1}],
    $$
    
    where $\ell$ is the period length, and $a_k=a_{\ell-k}$ holds for every $1\le k<\ell$.

??? note "Proof"
    Since $\lfloor\omega\rfloor-1+\omega>1$, and its conjugate equals $\lfloor\omega\rfloor - \omega$, which lies between $-1$ and $0$, by [Galois's result](./continued-fraction.md#纯循环连分数) $\lfloor\omega\rfloor-1+\omega$ is a purely periodic continued fraction and can be written as
    
    $$
    \lfloor\omega\rfloor-1+\omega = [\overline{2\lfloor\omega\rfloor-1,a_1,\cdots,a_{\ell-1}}].
    $$
    
    And Galois's result on the reciprocal of the negative conjugate shows that
    
    $$
    \dfrac{1}{\omega-\lfloor\omega\rfloor} = [\overline{a_{\ell-1},\cdots,a_1,2\lfloor\omega\rfloor-1}].
    $$
    
    Therefore, by the definition of a continued fraction, we have
    
    $$
    \lfloor\omega\rfloor-1+\omega = 2\lfloor\omega\rfloor-1 + \dfrac{1}{\dfrac{1}{\omega-\lfloor\omega\rfloor}} = [2\lfloor\omega\rfloor-1,\overline{a_{\ell-1},\cdots,a_1,2\lfloor\omega\rfloor-1}].
    $$
    
    The uniqueness of the continued fraction expansion shows that $a_k=a_{\ell-k}$ holds for all $1\le k<\ell$, and hence the expansion to be proved also holds.

???+ note "Theorem"
    Let $D\equiv 1\pmod 4$. While running the PQa algorithm above on $(P_0,Q_0,D)=(1,2,D)$, $Q_k=2$ necessarily implies $\ell\mid k$.

??? note "Proof"
    In the continued fraction expansion of $\dfrac{1+\sqrt{D}}{2}$, all remainders except the $0$-th are [purely periodic continued fractions](./continued-fraction.md#纯循环连分数). Let $Q_k=2$. By Galois's result, the conjugate of the remainder $\omega_k=\dfrac{P_k+\sqrt{D}}{2}$ must satisfy $-1<\dfrac{P_k-\sqrt{D}}{2}<0$, i.e. $\sqrt{D}-2<P_k<\sqrt{D}$. Since in the PQa algorithm we always have $Q_k\mid P_k^2-D$ (see the [proof of correctness of the algorithm](./continued-fraction.md#二次无理数)), $P_k$ must be odd, which shows that the value of $P_k$ is unique, namely $P_k=P_0+2(\lfloor\omega\rfloor-1)$, that is, the remainder $\omega_k=\omega_\ell$. But a repeated remainder means the continued fraction is periodic, so if $k$ is not a multiple of $\ell$, this contradicts $\ell$ being the smallest positive period. Hence necessarily $\ell\mid k$.

???+ note "Theorem"
    Let $(x_1,y_1)$ be the smallest positive integer solution of the equation $x^2-Dy^2=\pm 4$. Then the set of all its solutions is
    
    $$
    \left\{(x,y):\dfrac{x+y\sqrt{D}}{2}=\pm\left(\dfrac{x_1+y_1\sqrt{D}}{2}\right)^k,k\in\mathbf Z\right\}.
    $$

??? note "Proof"
    By symmetry, it suffices to consider positive integer solutions $(x,y)$. The only thing to prove here is that the pairs of real numbers $(x,y)$ in the set are indeed integer solutions of the equation $x^2-Dy^2=\pm 4$. For the rest, it suffices to repeat the proof of the structure of the solutions of the equation $x^2-Dy^2=\pm 1$.
    
    What actually needs to be proved is that for any integer solutions $(x_1,y_1)$ and $(x_2,y_2)$ of the equation $x^2-Dy^2=\pm 4$, the pair of positive real numbers $(x_3,y_3)$ defined by
    
    $$
    \dfrac{x_3+y_3\sqrt{D}}{2} = \dfrac{x_1+y_1\sqrt{D}}{2}\dfrac{x_2+y_2\sqrt{D}}{2}.
    $$
    
    is still an integer solution. Expanding the right-hand side and comparing the coefficients of the rational and irrational terms, we get
    
    $$
    x_3=\dfrac{x_1x_2+Dy_1y_2}{2},\ y_3=\dfrac{x_1y_2+x_2y_1}{2}.
    $$
    
    Since for $i=1,2$ we have $x_i\equiv x_i^2\equiv Dy_i^2\equiv Dy_i\pmod 2$, we get
    
    $$
    \begin{aligned}
    2x_3 &= x_1x_2+Dy_1y_2 \equiv D^2y_1y_2+Dy_1y_2=D(D+1)y_1y_2 \equiv 0 \pmod 2,\\
    2y_3 &= x_1y_2+x_2y_1 \equiv Dy_1y_2+Dy_2y_1 = 2Dy_1y_2 \equiv 0 \pmod 2.
    \end{aligned}
    $$
    
    This shows that $x_3$ and $y_3$ are both integers. Using the fact that the norm preserves multiplication, $(x_3,y_3)$ is a solution of $x^2-Dy^2=\pm 4$.

Combining these facts and repeating the arguments of the previous sections, the correctness of the algorithm above for solving the equation $x^2-Dy^2=\pm 4$ can be established. These results show that the equation $x^2-Dy^2=\pm 4$ has a simple solution structure similar to that of the equation $x^2-Dy^2=\pm 1$: all its solutions can be expressed through its smallest positive integer solution, without solving other equations.

In fact, all solutions of the equation $x^2-Dy^2=\pm 1$ can be found among the solutions of the equation $x^2-Dy^2=\pm 4$, so from this point of view the equation $x^2-Dy^2=\pm 4$ is more fundamental. Clearly, $(x,y)$ is a solution of the equation $x^2-Dy^2=\pm 1$ if and only if $(2x,2y)$ is a solution of the equation $x^2-Dy^2=\pm 4$. The analysis above pointed out that when $D\equiv 2,3\pmod 4$, all solutions of the equation $x^2-Dy^2=\pm 4$ must be both even, and hence correspond to solutions of $x^2-Dy^2=\pm 1$.

When $D\equiv 0\pmod 4$, in a solution $(x,y)$ of the equation $x^2-Dy^2=\pm 4$, $x$ must be even, but $y$ may be odd. If in the smallest positive integer solution $(x_1,y_1)$ of the equation $x^2-Dy^2=\pm 4$, $y_1$ is even, then $y$ is also even in all solutions, and these integer solutions are in one-to-one correspondence with the integer solutions of the equation $x^2-Dy^2=\pm 1$; but if in the smallest integer solution $(x_1,y_1)$, $y_1$ is odd, then the parity of $y_k$ agrees with that of $k$ and alternates, so only when $k$ is even does it correspond to a solution of the equation $x^2-Dy^2=\pm 1$. If in the smallest positive integer solution of $x^2-Dy^2=\pm 4$, $y_1$ is odd and the norm of $x_1+y_1\sqrt{D}$ is $-4$, then for such $D$ the equation $x^2-Dy^2=-4$ has a solution but $x^2-Dy^2=-1$ has none.

When $D\equiv 1\pmod 4$, a solution $(x,y)$ of the equation $x^2-Dy^2=\pm 4$ may be both odd or both even. If the smallest positive integer solution $(x_1,y_1)$ is already both even, then all its integer solutions must also be both even, so they always correspond to integer solutions of the equation $x^2-Dy^2=\pm 1$. If the smallest positive integer solution $(x_1,y_1)$ is both odd, then the following result holds:

???+ note "Theorem"
    Let $(x_1,y_1)$ be the smallest positive integer solution of the equation $x^2-Dy^2=\pm 4$. If $x_1$ and $y_1$ are both odd, then $D\equiv 5\pmod 8$, and an integer solution $(x,y)$ of this equation is both even if and only if
    
    $$
    \dfrac{x+y\sqrt{D}}{2} = \pm\left(\dfrac{x_1+y_1\sqrt{D}}{2}\right)^{3k},k\in\mathbf Z.
    $$

??? note "Proof"
    Reducing both sides of the equation $x_1^2-Dy_1^2=\pm 4$ modulo $8$ gives $D\equiv 5\pmod 8$. To prove the second claim, we first prove that $(x_3,y_3)$ are both even; since
    
    $$
    \dfrac{x_3+y_3\sqrt{D}}{2} = \left(\dfrac{x_1+y_1\sqrt{D}}{2}\right)^{3} = \dfrac{x_1^3+3Dx_1y_1^2}{8}+\dfrac{3x_1^2y_1+Dy_1^3}{8}\sqrt{D},
    $$
    
    it suffices to prove that the right-hand side is an integer. Since the square of an odd number is congruent to $1$ modulo $8$, we have
    
    $$
    \begin{aligned}
    &x_1^3+3Dx_1y_1^2 = x_1(x_1^2+3Dy_1^2) \equiv x_1(1+3\times 5\times 1) = 16x_1 = 0 \pmod 8,\\
    &3x_1^2y_1+Dy_1^3 = y_1(3x_1^2+Dy_1^2) \equiv y_1(3\times 1+5\times 1) = 8y_1 = 0 \pmod 8.
    \end{aligned}
    $$
    
    This shows that $x_3,y_3$ are both even. Furthermore, for all $k\in\mathbf Z$ we have
    
    $$
    \dfrac{x+y\sqrt{D}}{2} = \pm\left(\dfrac{x_1+y_1\sqrt{D}}{2}\right)^{3k} = \pm\left(\dfrac{x_3+y_3\sqrt{D}}{2}\right)^k \in \mathbf Z[\sqrt{D}],
    $$
    
    so in this case $(x,y)$ are both even. Conversely, for $r=1,2$ we always have
    
    $$
    \pm\left(\dfrac{x_1+y_1\sqrt{D}}{2}\right)^{3k+r} = \pm\left(\dfrac{x_3+y_3\sqrt{D}}{2}\right)^k\left(\dfrac{x_r+y_r\sqrt{D}}{2}\right).
    $$
    
    To prove that the corresponding $(x,y)$ are not integers, it suffices to prove that this expression is not an integer, i.e. that the second factor of the product on the right-hand side is not an integer. For $r=1$ this is just the hypothesis; for $r=2$, since
    
    $$
    \dfrac{x_2+y_2\sqrt{D}}{2} = \left(\dfrac{x_1+y_1\sqrt{D}}{2}\right)^2 = \dfrac{x_1^2+Dy_1^2}{4} + \dfrac{x_1y_1}{2}\sqrt{D},
    $$
    
    and $x_1^2+Dy_1^2\equiv 1+1\times 1=2\pmod 4$, $x_1y_1\equiv 1\pmod 2$, this expression is not an integer either. This proves that the corresponding solutions are both even only when the exponent is a multiple of $3$.

That is to say, one out of every three solutions of the equation $x^2-Dy^2=\pm 4$ is both even, and it corresponds to an integer solution of $x^2-Dy^2=\pm 1$. This also shows that for $D\equiv 1\pmod 4$, the equation $x^2-Dy^2=-4$ has a solution if and only if the equation $x^2-Dy^2=-1$ has a solution.

The discussion so far is already sufficient to compute the fundamental unit of a ring of real quadratic integers. Let $D$ be a positive squarefree integer. For the case $D\equiv 2,3\pmod 4$, it suffices to find the smallest positive integer solution of $x^2-Dy^2=\pm 1$; for the case $D\equiv 1\pmod 4$, it suffices to find the smallest positive integer solution of $x^2-Dy^2=\pm 4$. Once the smallest positive integer solution $(x,y)$ is obtained, for $D\equiv 2,3\pmod 4$ the fundamental units are $\pm x\pm y\sqrt{D}$; for $D\equiv 1\pmod 4$ the fundamental units are $\dfrac{\pm x\pm y\sqrt{D}}{2}$.

??? example "Examples"
    1.  Solve the equation $x^2-14y^2=\pm 4$.
    
        From the computations in the earlier example, the smallest positive integer solution of the equation $x^2-14y^2=4$ is $(30,8)$, and the equation $x^2-14y^2=-4$ has no solution.
    2.  Solve the equation $x^2-41y^2=\pm 4$.
    
        Running the PQa algorithm on $(P_0,Q_0,D)=(1,2,41)$ gives the following (the first period is marked in red):
    
        |  $k$ | $P$ | $Q$ |        $a$       |   $A$   |   $B$  |   $G$   | $G^2-DB^2$ |
        | :--: | :-: | :-: | :--------------: | :-----: | :----: | :-----: | :--------: |
        |  $0$ | $1$ | $2$ |        $3$       |   $3$   |   $1$  |   $5$   |    $-16$   |
        |  $1$ | $5$ | $8$ | $\color{red}{1}$ |   $4$   |   $1$  |   $7$   |     $8$    |
        |  $2$ | $3$ | $4$ | $\color{red}{2}$ |   $11$  |   $3$  |   $19$  |    $-8$    |
        |  $3$ | $5$ | $4$ | $\color{red}{2}$ |   $26$  |   $7$  |   $45$  |    $16$    |
        |  $4$ | $3$ | $8$ | $\color{red}{1}$ |   $37$  |  $10$  |   $64$  |    $-4$    |
        |  $5$ | $5$ | $2$ | $\color{red}{5}$ |  $211$  |  $57$  |  $365$  |    $16$    |
        |  $6$ | $5$ | $8$ |        $1$       |  $248$  |  $67$  |  $429$  |    $-8$    |
        |  $7$ | $3$ | $4$ |        $2$       |  $707$  |  $191$ |  $1223$ |     $8$    |
        |  $8$ | $5$ | $4$ |        $2$       |  $1662$ |  $449$ |  $2875$ |    $-16$   |
        |  $9$ | $3$ | $8$ |        $1$       |  $2369$ |  $640$ |  $4098$ |     $4$    |
        | $10$ | $5$ | $2$ |        $5$       | $13507$ | $3649$ | $23365$ |    $-16$   |
        | $11$ | $5$ | $8$ |        $1$       | $15876$ | $4289$ | $27463$ |     $8$    |
    
        The period length $\ell=5$ is odd. The smallest positive integer solution of the equation $x^2-41y^2=-4$ is $(G_4,B_4)=(64,10)$, and the smallest positive integer solution of the equation $x^2-41y^2=4$ is $(G_9,B_9)=(4098,640)$. They are related as follows:
    
        $$
        \dfrac{4098+640\sqrt{41}}{2} = \left(\dfrac{64+10\sqrt{41}}{2}\right)^2.
        $$
    
        Of course, since $D\equiv 1\pmod 8$, by the result above the smallest positive integer solutions of the equation $x^2-41y^2=\pm 4$ must be both even and are always $2$ times the smallest positive integer solutions of the equation $x^2-41y^2=\pm 1$, so they can also be obtained directly from the earlier example.
    3.  Solve the equation $x^2-13y^2=\pm 4$.
    
        Running the PQa algorithm on $(P_0,Q_0,D)=(1,2,13)$ gives the following (the first period is marked in red):
    
        | $k$ | $P$ | $Q$ |        $a$       |  $A$ |  $B$ |  $G$  | $G^2-DB^2$ |
        | :-: | :-: | :-: | :--------------: | :--: | :--: | :---: | :--------: |
        | $0$ | $1$ | $2$ |        $2$       |  $2$ |  $1$ |  $3$  |    $-4$    |
        | $1$ | $3$ | $2$ | $\color{red}{3}$ |  $7$ |  $3$ |  $11$ |     $4$    |
        | $2$ | $3$ | $2$ |        $3$       | $23$ | $10$ |  $36$ |    $-4$    |
        | $3$ | $3$ | $2$ |        $3$       | $74$ | $33$ | $119$ |     $4$    |
    
        The period length $\ell=1$ is odd. The smallest positive integer solution of the equation $x^2-13y^2=-4$ is $(G_0,B_0)=(3,1)$, and the smallest positive integer solution of the equation $x^2-13y^2=4$ is $(G_1,B_1)=(11,3)$.
    
        Since the smallest positive integer solutions of this equation are both odd, we can use the pair $(G_2,B_2)=(36,10)$ at the end of the third period to obtain the smallest positive integer solution $(18,5)$ of the corresponding (negative) Pell equation $x^2-13y^2=\pm 1$. It can also be obtained by direct computation:
    
        $$
        \dfrac{36+10\sqrt{13}}{2}=\left(\dfrac{3+\sqrt{13}}{2}\right)^3.
        $$
    
        Moreover, this is a solution of the negative Pell equation. The smallest positive integer solution of the corresponding Pell equation is $(649,180)$.
    4.  Solve the equation $x^2-52y^2=\pm 4$.
    
        Since the smallest positive integer solutions of the equation $x^2-13y^2=\pm 1$ are $(18,5)$ and $(649,180)$ respectively, the smallest positive integer solutions of the equation $x^2-52y^2=\pm 4$ are $(36,10)$ and $(1298,360)$ respectively.

### General case

Finally, we discuss how to solve the generalized Pell equation.

For the case $|N|<\sqrt{D}$ there is a simple method. The result above shows that a solution $(x,y)$ of the equation $x^2-Dy^2=N$ must satisfy that $\dfrac{x}{y}$ equals some convergent of $\sqrt{D}$. Moreover, by the structure of the solutions discussed above, every fundamental solution $(x,y)$ satisfies that $x+y\sqrt{D}$ is less than or equal to the fundamental solution $x_1+y_1\sqrt{D}$ of the corresponding Pell equation $x^2-Dy^2=1$. By the monotonicity of the sequence of denominators $B_k$ in the PQa algorithm, these fundamental solutions of the generalized Pell equation must appear before the fundamental solution of the corresponding Pell equation appears. Therefore, it suffices to run the PQa algorithm on $(P_0,Q_0,D)=(0,1,D)$ until $Q_{\ell'}=1$ with $\ell'$ even, and along the way check for every $(A_k,B_k)$ that appears whether there is an integer $f$ such that

$$
A_k^2-DB_k^2 = (-1)^{k+1}Q_{k+1} = N/f^2
$$

holds; if so, record $(fA_{k},fB_{k})$ as a smallest positive integer solution. All the $(fA_k,fB_k)$ recorded by this process are exactly all the smallest positive integer solutions of the equation $x^2-Dy^2=N$. Using $(A_{\ell'-1},B_{\ell'-1})$, i.e. the fundamental solution of the corresponding Pell equation, all solutions of the generalized Pell equation can be generated from these smallest positive integer solutions. Note that, depending on whether the period length $\ell$ is even or odd, the $\ell'$ above may be $\ell$ or $2\ell$.

For more general $N$, the method above no longer applies. First, enumerate all square factors $f^2$ of $N$, let $m=N/f^2$, and enumerate all solutions $z$ of the congruence $z^2\equiv D\pmod{|m|}$ satisfying $-|m|/2<z \le |m|/2$. Then run the PQa algorithm on $(P_0,Q_0,D)=(z,|m|,D)$ until $Q_k=\pm 1$ or a full period has been completed. In the second case, no solution of the equation associated with this pair $(f,z)$ exists. In the first case, one further needs to check whether $(-1)^kQ_k=N/|N|$. If the signs agree, then $(fG_{k-1},fB_{k-1})$ is a solution of the equation $x^2-Dy^2=N$. Otherwise, it is a solution of the equation $x^2-Dy^2=-N$, and a solution of $x^2-Dy^2=N$ can be obtained by composing it with the fundamental solution of the corresponding negative Pell equation if and only if a solution of that negative Pell equation exists. After going through all pairs $(f,z)$, we obtain exactly one solution of the equation $x^2-Dy^2=N$ in each equivalence class of solutions, and this solution is the fundamental solution or the smallest positive integer solution of that equivalence class. Using them and the fundamental solution of the corresponding Pell equation, all integer solutions of the equation can be generated. This algorithm is called the **Lagrange–Matthews–Mollin algorithm**.

The correctness of this algorithm is guaranteed by the following theorem:

???+ note "Theorem"
    Let the equation $x^2-Dy^2=N$ have an integer solution $(x,y)$ with $x\ge 0, y>0,\gcd(x,y)=1$. Let $Q_0=|N|$; then $\gcd(Q_0,y)=1$. Let $P_0$ be a solution of the congruence $x\equiv -P_0y\pmod{Q_0}$ with $-Q_0/2<P_0\le Q_0/2$, and let the integer $X$ be such that $x=Q_0X-P_0y$ holds. Then $P_0^2\equiv D\pmod{Q_0}$, $\dfrac{X}{y}$ is a convergent $\dfrac{A_{k-1}}{B_{k-1}}$ of $\omega=\dfrac{P_0+\sqrt{D}}{Q_0}$, and $Q_k=(-1)^k\dfrac{N}{|N|}$.

??? note "Proof"
    Using $x\equiv -P_0y\pmod{Q_0}$ and $x^2-Dy^2=N\equiv 0\pmod{Q_0}$, clearly $P_0^2\equiv D\pmod{Q_0}$. Hence,
    
    $$
    P_0x+Dy\equiv -P_0^2y+Dy = (D-P_0^2)y\equiv 0\pmod{Q_0}.
    $$
    
    Based on this, consider the integer matrix
    
    $$
    \begin{pmatrix}P & R \\ Q & S\end{pmatrix}
    =
    \begin{pmatrix}X & \dfrac{P_0x+Dy}{Q_0} \\ y & x\end{pmatrix}.
    $$
    
    Its determinant is
    
    $$
    PS-QR = \dfrac{x(x+P_0y)-y(P_0x+Dy)}{Q_0} = \dfrac{x^2-Dy^2}{Q_0} = \pm 1.
    $$
    
    Moreover, letting $\zeta =\sqrt{D} > 1$, we have
    
    $$
    \dfrac{P\zeta+R}{Q\zeta+S} = \dfrac{(x+P_0y)\sqrt{D}+(P_0x+Dy)}{(x+y\sqrt{D})Q_0} = \dfrac{P_0+\sqrt{D}}{Q_0} = \omega.
    $$
    
    We now prove that $\dfrac{P}{Q}$ is a convergent of $\omega$. Suppose $\dfrac{P}{Q}$ has the [continued fraction expansion](./continued-fraction.md#简单连分数)
    
    $$
    \dfrac{P}{Q} = [a_0,a_1,\cdots,a_k]
    $$
    
    with $PS-QR = (-1)^{k-1}$. If $\dfrac{p_k}{q_k}$ denotes its $k$-th convergent, then $(p_k,q_k)=(P,Q)$, and by the [difference formula for convergents](./continued-fraction.md#误差估计), $p_kq_{k-1}-q_kp_{k-1}=(-1)^{k-1}$. This shows that
    
    $$
    p_k(S-q_{k-1}) = q_k(R-p_{k-1}).
    $$
    
    We distinguish cases:
    
    -   If $S=0$, then it is easy to verify that $Q=R=1$, so $\omega=P+\zeta^{-1}=[P,\zeta]$, and hence $\dfrac{P}{Q}=P$ is the $0$-th convergent of $\omega$;
    -   If $Q=S>0$, then $Q=S=1$ and $P-R=\pm 1$. In this case,
        -   if $P=R+1$, then $\omega=R+\dfrac{1}{1+\zeta^{-1}}=[R,1,\zeta]$, so $\dfrac{P}{Q}=\dfrac{R+1}{1}=[R,1]$ is the $1$st convergent of $\omega$;
        -   if $P=R-1$, then $\omega=R-1+\dfrac{1}{1+\zeta}=[R-1,\zeta-1]$, so $\dfrac{P}{Q}=R-1$ is the $0$-th convergent of $\omega$;
    -   If $Q\neq S>0$, then since $Q=q_k\mid(S-q_{k-1})$, there always exists an integer $\kappa$ such that $S=\kappa q_k+q_{k-1}$ and $R=\kappa p_k+p_{k-1}$ hold. Since $q_k\ge q_{k-1}$ and $S>0$, we have $\kappa\ge 0$. Hence $\omega=\dfrac{(\kappa+\zeta)p_k+p_{k-1}}{(\kappa+\zeta)q_k+q_{k-1}}=[a_0,a_1,\cdots,a_k,\kappa+\zeta]$, so $\dfrac{P}{Q}$ is its $k$-th convergent.
    
    In summary, $\dfrac{X}{y}$ is always a convergent of $\omega=\dfrac{P_0+\sqrt{D}}{Q_0}$, and in the notation of the PQa algorithm we write it as $\dfrac{A_{k-1}}{B_{k-1}}$. Since $A_{k-1}^2-DB_{k-1}^2=(-1)^kQ_0Q_k$, we have $Q_k=(-1)^k\dfrac{N}{|N|}$.

This theorem guarantees that all positive solutions of the equation are found among the convergents of the corresponding quadratic irrationals. Since, when computing convergents with the PQa algorithm, the convergents are guaranteed to be positive once the period is entered, it suffices to enumerate all quadratic irrationals allowed by the conditions of the theorem and compute their convergents up to the end of one period to find a solution. Since two solutions appearing among the convergents of the same quadratic irrational must be equivalent, as soon as the first solution satisfying $(-1)^kQ_k=N/|N|$ is obtained, the subsequent computation can be stopped. Unlike all the previous algorithms, here the $k$ satisfying the condition may appear before the period is entered.

??? example "Examples"
    1.  Solve the equation $x^2-157y^2=12$.
    
        Since $12^2<157$, we run the PQa algorithm on $(P_0,Q_0,D)=(0,1,157)$; the result is as follows (the first period is marked in red):
    
        |  $k$ |  $P$ |  $Q$ |        $a$        |         $A$        |        $B$       |         $G$        | $G^2-DB^2$ |
        | :--: | :--: | :--: | :---------------: | :----------------: | :--------------: | :----------------: | :--------: |
        |  $0$ |  $0$ |  $1$ |        $12$       |        $12$        |        $1$       |        $12$        |    $-13$   |
        |  $1$ | $12$ | $13$ |   $\color{red}1$  |        $13$        |        $1$       |        $13$        |    $12$    |
        |  $2$ |  $1$ | $12$ |   $\color{red}1$  |        $25$        |        $2$       |        $25$        |    $-3$    |
        |  $3$ | $11$ |  $3$ |   $\color{red}7$  |        $188$       |       $15$       |        $188$       |    $19$    |
        |  $4$ | $10$ | $19$ |   $\color{red}1$  |        $213$       |       $17$       |        $213$       |    $-4$    |
        |  $5$ |  $9$ |  $4$ |   $\color{red}5$  |       $1253$       |       $100$      |       $1253$       |     $9$    |
        |  $6$ | $11$ |  $9$ |   $\color{red}2$  |       $2719$       |       $217$      |       $2719$       |    $-12$   |
        |  $7$ |  $7$ | $12$ |   $\color{red}1$  |       $3972$       |       $317$      |       $3972$       |    $11$    |
        |  $8$ |  $5$ | $11$ |   $\color{red}1$  |       $6691$       |       $534$      |       $6691$       |    $-11$   |
        |  $9$ |  $6$ | $11$ |   $\color{red}1$  |       $10663$      |       $851$      |       $10663$      |    $12$    |
        | $10$ |  $5$ | $12$ |   $\color{red}1$  |       $17354$      |      $1385$      |       $17354$      |    $-9$    |
        | $11$ |  $7$ |  $9$ |   $\color{red}2$  |       $45371$      |      $3621$      |       $45371$      |     $4$    |
        | $12$ | $11$ |  $4$ |   $\color{red}5$  |      $244209$      |      $19490$     |      $244209$      |    $-19$   |
        | $13$ |  $9$ | $19$ |   $\color{red}1$  |      $289580$      |      $23111$     |      $289580$      |     $3$    |
        | $14$ | $10$ |  $3$ |   $\color{red}7$  |      $2271269$     |     $181267$     |      $2271269$     |    $-12$   |
        | $15$ | $11$ | $12$ |   $\color{red}1$  |      $2560849$     |     $204378$     |      $2560849$     |    $13$    |
        | $16$ |  $1$ | $13$ |   $\color{red}1$  |      $4832118$     |     $385645$     |      $4832118$     |    $-1$    |
        | $17$ | $12$ |  $1$ | $\color{red}{24}$ |     $118531681$    |     $9459858$    |     $118531681$    |    $13$    |
        | $18$ | $12$ | $13$ |        $1$        |     $123363799$    |     $9845503$    |     $123363799$    |    $-12$   |
        | $19$ |  $1$ | $12$ |        $1$        |     $241895480$    |    $19305361$    |     $241895480$    |     $3$    |
        | $20$ | $11$ |  $3$ |        $7$        |    $1816632159$    |    $144983030$   |    $1816632159$    |    $-19$   |
        | $21$ | $10$ | $19$ |        $1$        |    $2058527639$    |    $164288391$   |    $2058527639$    |     $4$    |
        | $22$ |  $9$ |  $4$ |        $5$        |    $12109270354$   |    $966424985$   |    $12109270354$   |    $-9$    |
        | $23$ | $11$ |  $9$ |        $2$        |    $26277068347$   |   $2097138361$   |    $26277068347$   |    $12$    |
        | $24$ |  $7$ | $12$ |        $1$        |    $38386338701$   |   $3063563346$   |    $38386338701$   |    $-11$   |
        | $25$ |  $5$ | $11$ |        $1$        |    $64663407048$   |   $5160701707$   |    $64663407048$   |    $11$    |
        | $26$ |  $6$ | $11$ |        $1$        |   $103049745749$   |   $8224265053$   |   $103049745749$   |    $-12$   |
        | $27$ |  $5$ | $12$ |        $1$        |   $167713152797$   |   $13384966760$  |   $167713152797$   |     $9$    |
        | $28$ |  $7$ |  $9$ |        $2$        |   $438476051343$   |   $34994198573$  |   $438476051343$   |    $-4$    |
        | $29$ | $11$ |  $4$ |        $5$        |   $2360093409512$  |  $188355959625$  |   $2360093409512$  |    $19$    |
        | $30$ |  $9$ | $19$ |        $1$        |   $2798569460855$  |  $223350158198$  |   $2798569460855$  |    $-3$    |
        | $31$ | $10$ |  $3$ |        $7$        |  $21950079635497$  |  $1751807067011$ |  $21950079635497$  |    $12$    |
        | $32$ | $11$ | $12$ |        $1$        |  $24748649096352$  |  $1975157225209$ |  $24748649096352$  |    $-13$   |
        | $33$ |  $1$ | $13$ |        $1$        |  $46698728731849$  |  $3726964292220$ |  $46698728731849$  |     $1$    |
        | $34$ | $12$ |  $1$ |        $24$       | $1145518138660728$ | $91422300238489$ | $1145518138660728$ |    $-13$   |
        | $35$ | $12$ | $13$ |        $1$        | $1192216867392577$ | $95149264530709$ | $1192216867392577$ |    $12$    |
    
        The period length $\ell=17$ is odd, so within two periods we need to look at the cases where $G_k^2-157B_k^2$ differs from $12$ by a square factor, namely the cases $k=1,9,13,19,23,31$. The corresponding solutions are the $(fG,fB)$ in the following table:
    
        |  $k$ | $f$ |      $fG_k$      |      $fB_k$     |    $x$    |   $y$   |
        | :--: | :-: | :--------------: | :-------------: | :-------: | :-----: |
        |  $1$ | $1$ |       $13$       |       $1$       |    $13$   |   $1$   |
        |  $9$ | $1$ |      $10663$     |      $851$      |  $10663$  |  $851$  |
        | $13$ | $2$ |     $579160$     |     $46222$     |  $579160$ | $46222$ |
        | $19$ | $2$ |    $483790960$   |    $38610722$   | $-579160$ | $46222$ |
        | $23$ | $1$ |   $26277068347$  |   $2097138361$  |  $-10663$ |  $851$  |
        | $31$ | $1$ | $21950079635497$ | $1751807067011$ |   $-13$   |   $1$   |
    
        All the $(fG,fB)$ are exactly the smallest positive integer solutions in all equivalence classes of the solution set of the equation $x^2-157y^2=12$. To obtain all solutions from these, one can use the fundamental solution $(46698728731849,3726964292220)$ of the corresponding Pell equation. For instance, they can be converted into the fundamental solutions $(x,y)$ of their equivalence classes; these solutions are also listed in the table above.
    2.  Solve the equation $x^2-157y^2=12$.
    
        This time we solve it with the Lagrange–Matthews–Mollin algorithm. First, enumerate the square factors of $N=12$:
    
        -   for $f^2=1^2$, we have $m=12$, and the congruence $z^2\equiv 157\pmod{12}$ has solutions $z=\pm 1,\pm 5$;
        -   for $f^2=2^2$, we have $m=3$, and the congruence $z^2\equiv 157\pmod{3}$ has solutions $z=\pm 1$.
    
        For all possible combinations $(f,z)$, run the PQa algorithm with initial parameters $(P_0,Q_0,D)=(z,|m|,D)$ and find the first position where $(-1)^kQ_k=1$; the corresponding $(fG_{k-1},fB_{k-1})$ is a solution. The results are shown in the following table:
    
        | $f$ |  $z$ |  $m$ |  $k$ |    $fG_{k-1}$    |    $fB_{k-1}$   |
        | :-: | :--: | :--: | :--: | :--------------: | :-------------: |
        | $1$ |  $1$ | $12$ | $32$ | $21950079635497$ | $1751807067011$ |
        | $1$ | $-1$ | $12$ |  $2$ |       $13$       |       $1$       |
        | $1$ |  $5$ | $12$ | $24$ |   $26277068347$  |   $2097138361$  |
        | $1$ | $-5$ | $12$ | $10$ |      $10663$     |      $851$      |
        | $2$ |  $1$ |  $3$ | $20$ |    $483790960$   |    $38610722$   |
        | $2$ | $-1$ |  $3$ | $14$ |     $579160$     |     $46222$     |
    
        These are exactly the smallest positive integer solutions of all equivalence classes listed above; they can be converted into fundamental solutions using the fundamental solution of Pell's equation.
    3.  Solve the equation $x^2-79y^2=\pm 101$.
    
        We again use the Lagrange–Matthews–Mollin algorithm. Since $N=101$ is prime, we must have $f=1$. Then $m=101$, and the corresponding congruence $z^2\equiv 79\pmod{101}$ has solutions $z=\pm 33$.
    
        Running the PQa algorithm on $(P_0,Q_0,D)=(33,101,79)$ gives the following (the first period is marked in red):
    
        | $k$ |  $P$  |  $Q$  |       $a$      |  $A$  |   $B$  |   $G$   | $G^2-DB^2$ |
        | :-: | :---: | :---: | :------------: | :---: | :----: | :-----: | :--------: |
        | $0$ |  $33$ | $101$ |       $0$      |  $0$  |   $1$  |  $-33$  |   $1010$   |
        | $1$ | $-33$ | $-10$ |       $2$      |  $1$  |   $2$  |   $35$  |    $909$   |
        | $2$ |  $13$ |  $9$  |       $2$      |  $2$  |   $5$  |   $37$  |   $-606$   |
        | $3$ |  $5$  |  $6$  | $\color{red}2$ |  $5$  |  $12$  |  $109$  |    $505$   |
        | $4$ |  $7$  |  $5$  | $\color{red}3$ |  $17$ |  $41$  |  $364$  |   $-303$   |
        | $5$ |  $8$  |  $3$  | $\color{red}5$ |  $90$ |  $217$ |  $1929$ |   $1010$   |
        | $6$ |  $7$  |  $10$ | $\color{red}1$ | $107$ |  $258$ |  $2293$ |   $-707$   |
        | $7$ |  $3$  |  $7$  | $\color{red}1$ | $197$ |  $475$ |  $4222$ |    $909$   |
        | $8$ |  $4$  |  $9$  | $\color{red}1$ | $304$ |  $733$ |  $6515$ |   $-606$   |
        | $9$ |  $5$  |  $6$  |       $2$      | $805$ | $1941$ | $17252$ |    $505$   |
    
        The period length $\ell=6$ is even. Up to the end of one period, no $Q_k=\pm 1$ appears, so there is no solution in this case. Similarly, running the PQa algorithm on $(P_0,Q_0,D)=(-33,101,79)$ shows the same situation. Therefore, the equation has no solution.

## Exercises

-   [LOJ 6687.「Project Euler 66」解方程 (Solving the equation)](https://loj.ac/p/6687)
-   [SPOJ EQU2 - Yet Another Equation](https://www.spoj.com/problems/EQU2/)
-   [SPOJ PELL2 - Pell (Mid pelling)](https://www.spoj.com/problems/PELL2/)
-   [UVa 12909. Numeric Center](https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=862&page=show_problem&problem=4774)
-   [UVa 10241. Semi-triangular and also Square](https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=14&page=show_problem&problem=1182)

## References and notes

-   [Pell's equation - Wikipedia](https://en.wikipedia.org/wiki/Pell%27s_equation)
-   [John P. Robertson - Solving the generalized Pell equation $x^2-Dy^2=N$](https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=5ac34a344ee346855184ff949eeaed18685b155c)
-   [Keith Matthews - The Diophantine Equation $x^2-Dy^2=N$,$D>0$](http://www.numbertheory.org/PDFS/patz5.pdf)
-   [Existence of Solution to Pell’s Equation - Suryateja Gavva's Blog](https://surya-teja.com/2011/01/11/existence-of-solution-to-pells-equation/)
-   [Calculating the simple continued fraction of a quadratic irrational - Number Theory Web](http://www.numbertheory.org/php/surd.html) (PQa algorithm)
-   [Solving the diophantine equation x2–Dy2 = N, D > 0 and not a perfect square, N ≠ 0 - Number Theory Web](http://www.numbertheory.org/php/patz.html) (Lagrange–Matthews–Mollin algorithm)

[^not-square]: When $D$ is a perfect square, factoring directly gives $(x+y\sqrt{D})(x-y\sqrt{D})=N$, so all solutions can be found by going through the divisors of $N$. In particular, when $N=1$ the equation only has the solutions $(\pm 1,0)$; when $N=-1$ and $D\neq 1$ the equation has no solution.

[^neg-pell]: Some Chinese sources also call it the Pell equation of the second kind.

[^half-int]: That is, rational numbers of the form $n+\dfrac12$ with $n\in\mathbf Z$.

[^fundamental-solution]: Note that the definition of the fundamental solution of Pell's equation does not agree with the definition of the fundamental unit of a ring of real quadratic integers. First, in some rings of real quadratic integers the fundamental unit $x+y\sqrt{D}$ has half-integer $x,y$, and hence is not a solution of Pell's equation. Second, the same ring of real quadratic integers has four fundamental units, but there is only one fundamental solution, since the fundamental solution requires $x,y$ to both be positive.

[^solubility-neg-pell]: A more practical criterion and tool can be found [here](http://www.numbertheory.org/php/hardy_williams.html) and in the references given there. The list of positive integers $D$ for which the equation $x^2-Dy^2=-1$ has a solution is [OEIS A031396](https://oeis.org/A031396).
