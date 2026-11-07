---
title: Linear programming basics
---

## Introduction

Linear programming (LP) is the collective name for methods that study extremal problems of a linear objective function under linear constraints; it is a branch of operations research and has applications in many areas. Some special cases of linear programming, such as network flow and multi-commodity flow problems, may appear in competitive programming problems. Problems that can only be solved with linear programming algorithms rarely appear in competitive programming; the vast majority of such problems can be solved more efficiently by network flow modeling and similar methods.

### A simple example

For a problem to be written in the form of a linear program, it must have both several linear constraints and a linear objective function.

Consider the following example:

???+ example "Example"
    A breakfast chef can make a certain amount of baozi (steamed stuffed buns) and youtiao (fried dough sticks) every day; both breakfasts are very popular with customers. To maximize profit, the chef wants to make as many breakfasts as possible, but in practice he is limited by various resources such as ingredients and time. For this purpose, the chef recorded the amount of ingredients, the preparation time and the corresponding profit for each portion of breakfast, as shown in the following table:
    
    | Breakfast | Vegetable oil | Flour | Time | Profit |
    | :-: | :-: | :-: | :-: | :-: |
    | Baozi | $4$ | $7$ | $8$ | $5$ |
    | Youtiao | $7$ | $3$ | $6$ | $6$ |
    
    Suppose the chef can buy at most $66$ units of vegetable oil and $60$ units of flour per day, and can spend at most $96$ units of preparation time. How should the chef arrange the production quantities of baozi and youtiao so that the daily profit is maximized?

In mathematical language, let $x_1$ and $x_2$ be the quantities of baozi and youtiao the chef makes, respectively. Then "the total vegetable oil needed does not exceed $66$ units" can be expressed as

$$
4x_1 + 7x_2 \le 66.
$$

Similarly, "the total flour needed does not exceed $60$ units" and "the total time needed does not exceed $96$ units" can be expressed as

$$
\begin{aligned}
7x_1 + 3x_2 &\le 60,\\
8x_1 + 6x_2 &\le 96.
\end{aligned}
$$

Moreover, the chef cannot produce a negative number of breakfasts, so there is also the condition

$$
x_1,x_2\ge 0.
$$

Under these restrictions, the chef wants to maximize the profit:

$$
z = 5x_1 + 6x_2.
$$

This is a typical linear programming problem. Its objective function is a linear function of the decision variables, and the constraints consist of linear equations or inequalities in the decision variables.

### Graphical method

Linear programming problems with only two decision variables can be solved intuitively by the graphical method.

Consider the geometric picture corresponding to the problem of this section

$$
\begin{aligned}
\max_{x_1,x_2}\;& z = 5x_1 + 6x_2 \\
\text{subject to } & 4x_1 + 7x_2 \le 66,\\
& 7x_1 + 3x_2 \le 60,\\
& 8x_1 + 6x_2 \le 96,\\
& x_1,x_2\ge 0
\end{aligned}
$$

The last line of constraints says that all admissible points $(x_1,x_2)$ lie in the first quadrant, and the other three constraints say that the admissible points must lie below the lines $4x_1 + 7x_2 = 66$, $7x_1 + 3x_2 = 60$ and $8x_1 + 6x_2 = 96$. The intersection of these regions (the green region in the figure below) is the set of all points that can be chosen:

![](images/linear-programming.svg)

Next we need to maximize the value of $z=5x_1+6x_2$. If we view this equation as the equation of the line $5x_1+6x_2=z$, then as $z$ varies we get a family of parallel lines, and the larger $z$ is, the closer the line is to the upper right. Therefore, we only need to keep moving the line until it reaches a critical position where moving it a little further to the upper right would make it no longer intersect the region shown in the figure; the $z$ corresponding to this line is the required maximum.

As shown in the figure, this happens at the position marked by the red point. It is the intersection of the lines $4x_1 + 7x_2 = 66$ and $7x_1 + 3x_2 = 60$. Solving the equations of the two lines simultaneously, we find that its coordinates are $(6,6)$. This is the unique optimal solution of the problem. The chef's maximum profit is $z=66$.

When the problem involves more than two decision variables, the graphical method no longer applies. However, some observations from the example of this section remain valid. Each inequality constraint of a linear programming problem describes a "half-plane", and the set of all feasible solutions is the intersection of these "half-planes", so it is always a "convex polygon". The optimal solution of the problem can always be attained at some "vertex" of this "convex polygon". The coordinates of these "vertices" can be obtained by solving the equations of the "boundaries" of these "half-planes" simultaneously. Extending these observations to higher-dimensional spaces led to an efficient method for solving linear programming problems: the simplex method. It is also the method most commonly used in competitive programming.

Another issue worth noting is that, in principle, the baozi and youtiao made by the chef are not infinitely divisible and should be integers. Although this was not explicitly required when solving the problem, the final optimal solution is indeed integral, so the answer remains feasible even if we add the integrality restriction. However, for many optimization problems the optimal solution may not be attainable at an integer point; such problems are actually integer programming problems rather than plain linear programming problems. This class of problems is briefly discussed at the end of this article.

## Basic concepts

This section introduces the basic concepts of linear programming problems.

### Linear programming problem

A linear programming problem $P$ usually consists of the following two parts:

-   a linear objective function, i.e. a function of the form

    $$
    f(x_1,x_2,\cdots,x_n)=c_1x_1+c_2x_2+\cdots+c_nx_n
    $$

    where $c_i\in\mathbf R$ are constants;

-   linear constraints, i.e. inequality or equality constraints of the form

    $$
    g_j(x_1,x_2,\cdots,x_n)=a_{j1}x_1+a_{j2}x_2+\cdots+a_{jn}x_n \le (=,\ge) b_j
    $$

    where $a_{ji},b_j\in\mathbf R$ are constants.

A linear programming problem asks to maximize or minimize the objective function while satisfying the given constraints. A solution $(x_1,x_2,\cdots,x_n)\in\mathbf R^n$ that satisfies the given constraints is called a **feasible solution**; among all feasible solutions, one at which the objective function attains its extremum is called an **optimal solution**.

### Standard form

For convenience of description and further processing, a standard form of linear programming problems is usually specified. Different references may specify it differently; in this article the standard form of a linear program is defined as follows:

$$
\begin{aligned}
\min_{\{x_i\}}\;& \sum_{i=1}^n c_ix_i \\
\text{subject to }& \sum_{i=1}^n a_{ji}x_i = b_j \ge 0,~j=1,\cdots,m,\\
& x_i \ge 0,~i = 1,\cdots,n.
\end{aligned}
$$

That is, the linear programming problem is a minimization problem, all decision variables have nonnegativity constraints, and apart from that it contains only equality constraints whose right-hand constants are nonnegative. Using [matrices](./linear-algebra/matrix.md), this problem can be expressed more concisely:

$$
\min\{c^Tx : Ax = b \ge 0,~ x\ge 0\}.
$$

Here $x=(x_i)\in\mathbf R^n$ is the vector of decision variables, and $b=(b_j)\in\mathbf R^m$ and $A=(a_{ji})\in\mathbf R^{m\times n}$ are the constants appearing in the constraints. The size of a linear programming problem refers to the number of its decision variables and the number of its constraints.

???+ tip "Vector inequalities"
    Vector inequalities like $b \ge 0$ will appear many times in this article. In general, for vectors $x,y\in\mathbf R^n$, the inequality $x\le y$ means $\forall i(x_i\le y_i)$, i.e. a coordinate-wise comparison of real numbers. This relation is a [partial order](./order-theory.md#二元关系) on the vector space, which means that there are pairs of vectors that cannot be compared.

The choice of the standard form is only for convenience of exposition and is not special in any way, because every linear programming problem can be equivalently written in each of the following six forms:

$$
\begin{aligned}
&\min\{c^Tx : Ax = b,~ x\ge 0\},\\
&\min\{c^Tx : Ax \ge b\},\\
&\min\{c^Tx : Ax \ge b,~ x\ge 0\},\\
&\max\{c^Tx : Ax = b,~ x\ge 0\}, \\
&\max\{c^Tx : Ax \le b\},\\
&\max\{c^Tx : Ax \le b,~ x\ge 0\}.\\
\end{aligned}
$$

The following operations can equivalently transform every linear programming problem into any of these six forms:

1.  By adding a minus sign, i.e. replacing $c$ by $-c$, a maximization problem is converted into a minimization problem and vice versa.
2.  By adding a minus sign, i.e. replacing $a_j^Tx \lesseqqgtr b_j$ by $-a_j^Tx \gtreqqless -b_j$, the direction of an inequality constraint is reversed, or the right-hand constant of an equality constraint is made nonnegative.
3.  Every equality constraint $a_j^Tx = b_j$ can be replaced by two inequality constraints of opposite directions, $a_j^Tx \ge b_j$ and $a_j^Tx \le b_j$.
4.  Every inequality constraint $a_j^Tx \le(\ge) b_j$ can be converted, by adding a nonnegative slack variable $s_j$, into the equality constraint $a_j^Tx +(-) s_j = b_j$ together with the corresponding nonnegativity constraint $s_j\ge 0$.
5.  If some decision variable $x_i$ has no nonnegativity constraint, it can be replaced by the difference of two nonnegative variables, i.e. $x_i = x^+_i - x^-_i$ with $x^+_i,x^-_i \ge 0$.

The size of the linear programming problem obtained by these operations is at most twice the size of the original problem, and the feasible and optimal solutions of these problems are easily converted into one another. Therefore, a linear programming problem in general form can always be first converted into the standard form (or into one of the six forms above) and then solved.

??? example "Example"
    Consider the linear programming problem
    
    $$
    \begin{aligned}
    \max\;& 3x_1 - 2x_2 + x_3 \\
    \text{subject to }& 2x_1 + 3x_2 + 4x_3 \ge 1,\\
    & 3x_1 + 4x_2 \le 5,\\
    & 5x_2 - x_3 = -1, \\
    & x_1, x_2 \ge 0.
    \end{aligned}
    $$
    
    By operations 1, 2 and 3 it can be converted into the form $\min\{c^Tx : Ax \ge b\}$, namely
    
    $$
    \begin{aligned}
    \min\;& -3x_1 + 2x_2 - x_3 \\
    \text{subject to }& 2x_1 + 3x_2 + 4x_3 \ge 1,\\
    & -3x_1 - 4x_2 \ge -5,\\
    & 5x_2 - x_3 \ge -1, \\
    & -5x_2 + x_3 \ge 1, \\
    & x_1 \ge 0,\\
    & x_2 \ge 0.
    \end{aligned}
    $$
    
    By operations 4 and 5 it can be converted into the form $\max\{c^Tx : Ax = b,~ x\ge 0\}$, namely
    
    $$
    \begin{aligned}
    \max\;& 3x_1 - 2x_2 + x^+_3 - x^-_3 \\
    \text{subject to }& 2x_1 + 3x_2 + 4x^+_3 - 4x^-_3 - x_4 = 1,\\
    & 3x_1 + 4x_2 + x_5 = 5,\\
    & 5x_2 - x^+_3 + x^-_3 = -1, \\
    & x_1, x_2, x^+_3, x^-_3, x_4, x_5 \ge 0.
    \end{aligned}
    $$

### Feasible region and solutions of the problem

The set $\mathcal D\subseteq\mathbf R^n$ of all feasible solutions is called the **feasible region** of the linear programming problem $P$. Geometrically, each inequality constraint $a_j^T x \le b_j$ describes a half-space $\{x\in\mathbf R^n:a_j^T x \le b_j\}$, and each equality constraint $a^T_jx = b_j$ describes a hyperplane $\{x\in\mathbf R^n:a_j^Tx=b_j\}$, so the feasible region must be the intersection of finitely many half-spaces and hyperplanes. In the field of optimization[^poly-names], such a geometric body is usually called a **polyhedron** in $\mathbf R^n$. A polyhedron is always a closed convex set, but it need not be bounded. A bounded polyhedron is also called a **polytope**. A polytope can be viewed as the generalization of a polygon in the plane to higher-dimensional spaces, and a polyhedron further generalizes it to the possibly unbounded case.

???+ example "Examples of polyhedra"
    Here are some common polyhedra:
    
    1.  The empty set $\varnothing$, also called the **nullitope**, whose dimension is defined to be $-1$.
    2.  An **affine subspace**, i.e. the intersection $\{x\in\mathbf R^n:Ax = b\}$ of several hyperplanes. It corresponds to the solution set of the system of linear equations $Ax = b$: when the system has no solution, it is the empty set; otherwise it can always be written in the form $x_0+V$, where $x_0\in\mathbf R^n$ and $V\subseteq\mathbf R^n$ is a linear subspace of dimension $n-\operatorname{rank}A$. In particular, hyperplanes are also affine subspaces.
    3.  A **polyhedral cone**, i.e. the set $\{\sum_i\alpha_ix_i:\alpha_i\ge 0\}$ of all nonnegative linear combinations of finitely many points $\{x_i\}$ in space. It is a convex cone with apex at the origin. Equivalently, it can be viewed as a polyhedron bounded by several hyperplanes passing through the origin, i.e. $\{x\in\mathbf R^n : Ax\le 0\}$. In particular, half-spaces are also polyhedral cones.
    4.  Polytopes, i.e. bounded polyhedra. In particular, polytopes of dimension $-1$, $0$, $1$, $2$ and $3$ are the familiar empty set, point, segment, polygon and polyhedron (in the usual sense), respectively. A set is a polytope if and only if it is the convex hull $\{\sum_i\alpha_ix_i:\alpha_i\ge 0,~\sum_i\alpha_i=1\}$ of finitely many points $\{x_i\}$. A $k$-dimensional polytope is the convex hull generated by at least $k+1$ points.
    5.  A **simplex**, i.e. a $k$-dimensional polytope generated by exactly $k+1$ points. It is the simplest $k$-dimensional polytope. In particular, simplices of dimension $-1$, $0$, $1$, $2$ and $3$ are the empty set, a point, a segment, a triangle and a tetrahedron, respectively. The simplest example of a $k$-dimensional simplex is $\{x\in\mathbf R^{k+1}:x_i\ge 0,~\sum_ix_i=1\}$. In fact, any $k$-dimensional simplex can be transformed into this special case by an affine transformation (i.e. translation and scaling). It is worth noting that the simplex method is not really carried out on a simplex.
    
    Any polyhedron can be viewed as the [Minkowski sum](../geometry/convex-hull.md#minkowski-sum) of a polyhedral cone and a polytope: the former describes the unbounded part of the polyhedron, and the latter describes the shape of its bounded part. This polyhedral cone is unique: the polyhedral cone obtained by decomposing the polyhedron $\{x\in\mathbf R^n:Ax\le b\}$ must be $\{x\in\mathbf R^n:Ax\le 0\}$.

The solutions of a linear program are closely related to the structure of the polyhedron. For a polyhedron $\mathcal D\subseteq\mathbf R^n$ and a vector $c\in\mathbf R^n\setminus\{0\}$, consider the following linear programming problem $P$ (the minimization case can be discussed similarly):

$$
\max\{c^Tx:x\in\mathcal D\}.
$$

Geometrically, this amounts to moving the hyperplane $H:c^Tx = z$ in the direction of the vector $c$ so that $z$ is as large as possible, under the condition that the hyperplane $H$ and the feasible region $\mathcal{D}$ have at least one common point. There are three possibilities:

-   The feasible region $\mathcal D$ is empty. This means that the problem $P$ has no feasible solution, i.e. some of its constraints contradict each other. In this case the problem $P$ is called **infeasible**, and its optimal value is defined to be $-\infty$.

-   The feasible region $\mathcal D$ is nonempty, but it contains a ray with direction vector $d$ satisfying $c^Td>0$, i.e. there exists $x_0\in\mathbf R^n$ such that $x_0+td\in\mathcal D$ for all $t\ge 0$. Since the hyperplane $H$ can be moved indefinitely in the direction of the vector $c$, and during the movement the set $H\cap\mathcal D$ contains at least some point of this ray and hence is always nonempty, the objective function $c^Tx = c^Tx_0 + tc^Td$ can take arbitrarily large values. In this case the problem $P$ is called **unbounded**, and its optimal value is defined to be $+\infty$.

-   The feasible region $\mathcal D$ is nonempty and contains no such ray. In this case the problem $P$ is called **bounded**. Let $z^*\in\mathbf R$ denote the optimal value of the problem $P$. The hyperplane $H^*:c^Tx = z^*$ is in a critical position: it intersects the polyhedron $\mathcal D$, and $\mathcal D$ is contained in the half-space $\{x:c^Tx\le z^*\}$. Such a hyperplane is called a **supporting hyperplane** of the polyhedron $\mathcal D$. The set of optimal solutions of the problem $P$ is exactly $H^*\cap\mathcal D$. As the intersection of a supporting hyperplane and the polyhedron, the set $H^*\cap\mathcal D$ must be a polyhedron and is contained in the boundary of $\mathcal D$. It is called a **face** of the polyhedron $\mathcal D$. Figuratively speaking, the polyhedron is enclosed by these faces. Besides these faces formed by intersecting supporting hyperplanes with the polyhedron, a polyhedron in general has two more faces: the empty set and the polyhedron itself. All faces of a polyhedron, under set inclusion, form the structure of a [lattice](../math/order-theory.md#有向集与格).

    The dimension of a face of a $d$-dimensional polyhedron must be an integer between $-1$ and $d$. A face of dimension $0$ (i.e. a point) is called a **vertex** or **corner point** of the polyhedron $\mathcal D$, a face of dimension $1$ is called an **edge** of the polyhedron $\mathcal D$, and a face of dimension $d-1$ is called a **facet** of the polyhedron $\mathcal D$. However, not every polyhedron has vertices. Since a face of a face of a polyhedron is again a face of the polyhedron, and only affine subspaces have no strictly smaller nonempty faces, all minimal faces of the polyhedron $\mathcal D$ are affine subspaces. Moreover, the minimal faces of the same polyhedron have the same dimension; in particular, the dimension of the minimal faces of the polyhedron $\mathcal D=\{x\in\mathbf R^n:Ax\le b\}$ is $n-\operatorname{rank}A$.

    Since the faces of a polyhedron are exactly the solution sets of bounded linear programming problems, we need to understand how to determine the equations of the faces of a polyhedron. Let the polyhedron $\mathcal D$ be described by several constraints $a_j^Tx \lesseqqgtr b_j$, and let $F$ be a face of $\mathcal D$. If some constraint holds with equality at all $x\in F$, the constraint is said to be **tight** on the face $F$. The points of the face $F$ obviously satisfy the system of equations obtained by setting these tight constraints to equalities, and the intersection of the affine subspace determined by this system with the polyhedron $\mathcal D$ is exactly the face $F$. Conversely, taking any subset of the constraints of the polyhedron $\mathcal D$, turning these constraints into equalities and solving the resulting system, the intersection of the resulting affine subspace with the polyhedron is a face of $\mathcal D$. Moreover, the more tight constraints are chosen, the smaller (with respect to inclusion) the resulting face.

    In particular, the coefficient matrix $\begin{pmatrix}A\\ I\end{pmatrix}$ of the feasible region $\mathcal D=\{x\in\mathbf R^n:Ax=b,~x\ge 0\}$ of a linear program in standard form has rank $n$, so its minimal faces are exactly its vertices. That is, if the problem is bounded, its optimal solution can always be chosen to be some vertex. Moreover, this vertex can be obtained by choosing $n$ linearly independent tight constraints and solving them simultaneously. This is precisely the convenience of the standard form of linear programs.

???+ example "Example"
    In the figure below, $\mathcal D$ is the feasible region. When the coefficients of the objective function are $c_1,c_2,c_3$, we get the three cases of a unique optimal solution, multiple optimal solutions and unboundedness, respectively. In the first two cases, the corresponding thick solid red line is (one of) the supporting hyperplanes corresponding to the solution set, and the optimal solution sets are the vertex $B$ and the edge $\overline{CD}$ of the polyhedron $\mathcal D$, respectively. In the third case, since the feasible region $\mathcal D$ contains a ray with direction $c_3$, the hyperplane with normal vector $c_3$ can be moved indefinitely in the direction of $c_3$, and so the problem is unbounded.
    
    ![](./images/lp-feasible.svg)

This discussion ignored the case $c=0$. In this case the linear programming problem obviously cannot be unbounded, so either the problem itself is infeasible, or the optimal value equals $0$ and the optimal solution set is $\mathcal D$ itself. Such special linear programs are also called **feasibility linear programming** problems.

It is worth pointing out that deciding whether a linear programming problem is feasible or bounded, and finding a feasible solution of a system of inequalities, are just as hard as solving the linear programming problem itself[^reducible]. For example, the proof of the strong duality theorem below shows that solving a bounded linear programming problem amounts to finding a feasible solution of a set of inequalities. Therefore, for tasks such as deciding whether a system of inequalities has a solution or whether a system of equations has a nonnegative solution, the most effective way is to solve the corresponding feasibility linear program[^other-methods].

Moreover, if a constraint of a linear programming problem is not tight on any face of the feasible region, the constraint is **redundant**. In the example of the breakfast chef at the beginning of this article, the working-time constraint is a redundant constraint. The problem of deciding whether some inequality $a_j^Tx\le b_j$ of a given system of inequalities is redundant can be solved by solving the linear programming problem $\max\{a_j^Tx:x\in\mathcal D\}$ and comparing the result with $b_j$.

## Common algorithms

In competitive programming, few problems can only be solved by linear programming algorithms. Most problems that can be solved by linear programming methods can usually also be solved by more specialized and more efficient algorithms such as network flow.

Common algorithms for solving linear programming problems are:

-   the [simplex method](./simplex.md)
-   the ellipsoid method
-   interior-point methods

Although the worst-case complexity of the simplex method is exponential while the complexity of interior-point methods is polynomial, both kinds of algorithms perform very well on most practical problems. In contrast, although the theoretical complexity of the ellipsoid method is polynomial, it usually runs slowly and is not practical.

It is currently unknown whether there is a strongly polynomial algorithm for linear programming problems.

## Dual problem

Every linear programming problem corresponds to a dual problem. The solutions of the primal (original) problem and the dual problem are closely related. The dual problem not only helps to understand the structure of the problem more deeply, but can often also improve the efficiency of solving the primal problem.

For the linear programming problem $P$ (all lowercase variables involved are vectors)

$$
\begin{aligned}
\min_{x_1,x_2,x_3}\;& c_1^Tx_1 + c_2^Tx_2 + c_3^Tx_3 \\
\text{subject to }& A_{11}x_1 + A_{12}x_2 + A_{13}x_3 \ge b_1,\\
& A_{21}x_1 + A_{22}x_2 + A_{23}x_3 = b_2,\\
& A_{31}x_1 + A_{32}x_2 + A_{33}x_3 \le b_3,\\
& x_1\ge 0,~ x_3\le 0,
\end{aligned}
$$

its dual problem $D$ is the linear programming problem

$$
\begin{aligned}
\max_{y_1,y_2,y_3}\;&b_1^Ty_1+b_2^Ty_2+b_3^Ty_3 \\
\text{subject to }&A_{11}^Ty_1 + A_{21}^Ty_2 + A_{31}^Ty_3\le c_1,\\
&A_{12}^Ty_1 + A_{22}^Ty_2 + A_{32}^Ty_3 = c_2,\\
&A_{13}^Ty_1 + A_{23}^Ty_2 + A_{33}^Ty_3 \ge c_3,\\
&y_1\ge 0,~ y_3\le 0.
\end{aligned}
$$

Here the decision variables $y_1,y_2,y_3$ of the dual problem are the Lagrange multipliers of the three kinds of constraints of the primal problem, respectively; conversely, the decision variables $x_1,x_2,x_3$ of the primal problem are the Lagrange multipliers of the three kinds of constraints of the dual problem, respectively. It is easy to verify that the dual of the dual problem is the primal problem.

The correspondence between the primal problem $P$ and the dual problem $D$ is as follows:

| Minimization problem | Maximization problem |
| :----: | :----: |
| greater-than-or-equal constraint | nonnegative variable |
| less-than-or-equal constraint | nonpositive variable |
| equality constraint | free variable |
| nonnegative variable | less-than-or-equal constraint |
| nonpositive variable | greater-than-or-equal constraint |
| free variable | equality constraint |
| objective function coefficients | right-hand constants of constraints |
| right-hand constants of constraints | objective function coefficients |

In particular, the dual problem of the linear programming problem in standard form

$$
\min\{c^Tx:Ax=b,~x\ge 0\}
$$

is

$$
\max\{b^Ty:A^Ty\le c\}.
$$

### Duality principle

The primal and dual problems are not only mirror images of each other in form, but their solutions are also closely related. This is called the **duality principle**. For convenience of exposition, in this section the primal problem is taken in standard form when stating and proving theorems.

First, the **weak duality theorem** states that the maximum of the dual problem does not exceed the minimum of the primal problem.

???+ note "Weak duality theorem"
    For all $A\in\mathbf R^{m\times n}$, $b\in\mathbf R^m$ and $c\in\mathbf R^n$, we always have
    
    $$
    \max\{b^Ty:A^Ty\le c\} \le \min\{c^Tx:Ax=b,~x\ge 0\}.
    $$

??? note "Proof"
    If either the primal or the dual problem is infeasible, the inequality is trivial. Suppose both problems are feasible. Then for all feasible $x$ and $y$ we have
    
    $$
    b^Ty = x^TA^Ty \le x^Tc.
    $$
    
    Taking the extrema on both sides, we obtain the weak duality theorem.

To further discuss the relationship between the solutions of the primal and dual problems, we also need Farkas' lemma (and its various variants). It gives a necessary and sufficient condition for a system of linear equations to have a nonnegative solution.

???+ note "Farkas' lemma"
    For $A\in\mathbf R^{m\times n}$ and $b\in\mathbf R^m$, exactly one of the following holds:
    
    1.  there exists $x\in\mathbf R^n$ such that $Ax=b$ and $x\ge 0$;
    2.  there exists $y\in\mathbf R^m$ such that $A^T y\ge 0$ and $b^Ty<0$.

??? note "Proof"
    If both cases held at the same time, we would have $0\le (A^Ty)^Tx = y^T(Ax) = b^Ty<0$, a contradiction. So at most one case holds. Next we show that at least one case holds. Let $C=\{Ax:x\ge 0\}$ be the polyhedral cone generated by the column vectors of $A$. If $b\in C$, case 1 holds; otherwise we need to show that case 2 holds. Since the polyhedral cone $C$ can also be written as the intersection of finitely many half-spaces passing through the origin, it is a closed convex set. Since moreover $b\notin C$, by the hyperplane separation theorem there exist $y\in\mathbf R^m$ and $\alpha\in\mathbf R$ such that $b^Ty<\alpha$ and $z^Ty>\alpha$ for all $z\in C$. Since $0\in C$, we have $\alpha<0$, and hence $b^Ty<0$. Furthermore, since $t(A^Ty)^Tx>\alpha$ for all $x\ge 0$ and $t>0$, letting $t\to+\infty$ shows that $(A^Ty)^Tx\ge 0$ holds for all $x\ge 0$, i.e. $A^Ty\ge 0$. This is exactly case 2.

Geometrically, case 1 says that the point $b$ lies in the polyhedral cone $C$ generated by the column vectors of $A$; case 2 says that there is a hyperplane $H:y^Tx = 0$ through the origin with normal vector $y$ that strictly separates the point $b$ from the polyhedral cone $C$. Therefore, Farkas' lemma is a kind of [hyperplane separation theorem](https://en.wikipedia.org/wiki/Hyperplane_separation_theorem).

Using Farkas' lemma, we obtain a way to decide whether the primal problem is unbounded based on the feasibility of the primal and dual problems.

???+ note "Corollary"
    A linear programming problem is unbounded if and only if it is feasible and its dual problem is infeasible.

??? note "Proof"
    We again take the primal problem in standard form as an example. For a linear programming problem in general form, it suffices to first convert it into standard form, because the transformations described [earlier](#standard-form) do not change the feasibility and boundedness of the problem and its dual.
    
    On the one hand, if the primal problem is unbounded, it is obviously feasible and its optimal value is $-\infty$. In this case the dual problem must be infeasible, since otherwise its optimal value would be at least some real number, contradicting the weak duality theorem.
    
    On the other hand, suppose the primal problem is feasible and the dual problem is infeasible. Writing the free variable in the constraint $A^Ty\le c$ as the difference of two nonnegative variables $y=y^+-y^-$ and adding a nonnegative slack variable $s$, it is equivalent to the constraint $Mz=c$ with $z\ge 0$, where $M=(A^T,-A^T,I)$ and $z=(y^+,y^-,s)$. Since $M^Td=(Ad,-Ad,d)$, applying Farkas' lemma to $M$ and $c$ shows that either there exists $y$ such that $A^Ty\le c$, or there exists $d\ge 0$ such that $Ad=0$ and $c^Td<0$, and exactly one of the two holds. By assumption, the latter holds. Then, taking any feasible solution $x_0$ of the primal problem, we have $A(x_0+td)=b$ and $x_0+td\ge 0$ for all $t\ge 0$, while $c^T(x_0+td)=c^Tx_0+tc^Td\to-\infty~(t\to+\infty)$. This shows that the primal problem is unbounded.

Combining the weak duality theorem and this corollary, there are only the following four possible cases for the solutions of the primal and dual problems:

1.  both the primal and the dual problem are infeasible, i.e. $-\infty\le+\infty$;
2.  the primal problem is infeasible and the dual problem is unbounded, i.e. $+\infty\le+\infty$;
3.  the primal problem is unbounded and the dual problem is infeasible, i.e. $-\infty\le-\infty$;
4.  both the primal and the dual problem are bounded.

In the fourth case a stronger conclusion holds: the optimal values of the primal and dual problems are equal. Combining the last three cases, we obtain the **strong duality theorem**: as long as one of the primal and dual problems is feasible, their optimal values must be equal.

???+ note "Strong duality theorem"
    For all $A\in\mathbf R^{m\times n}$, $b\in\mathbf R^m$ and $c\in\mathbf R^n$, we have
    
    $$
    \max\{b^Ty:A^Ty\le c\} = \min\{c^Tx:Ax=b,~x\ge 0\}.
    $$
    
    as long as one of the two sets is nonempty.

??? note "Proof"
    In the preceding discussion, the only case in which the optimal value was not determined is when both the primal and the dual problem are feasible. In this case, consider the following feasibility linear programming problem $Q$:
    
    $$
    \max\{0:c^Tx \le b^Ty,~Ax=b,~x\ge 0,~A^Ty\le c\}.
    $$
    
    If the problem $Q$ has a feasible solution $(x^*,y^*)\in\mathbf R^n\times\mathbf R^m$, then by the weak duality theorem and optimality we have
    
    $$
    b^Ty^* \le \max\{b^Ty:A^Ty\le c\} \le \min\{c^Tx:Ax=b,~x\ge 0\} \le c^Tx^*,
    $$
    
    but $c^Tx^*\le b^Ty^*$, so all these inequalities hold with equality; that is, not only does strong duality hold, but $x^*$ and $y^*$ are optimal solutions of the primal and dual problems, respectively.
    
    Therefore, it suffices to prove that the problem $Q$ is feasible. Suppose not. Following the proof of the corollary above, consider the dual problem $DQ$ of the problem $Q$:
    
    $$
    \min\{c^T\mu - b^T\lambda : ct - A^T\lambda \ge 0,~ -bt + A\mu = 0,~t\ge 0,~\mu\ge 0\}.
    $$
    
    Since $(t,\lambda,\mu)=(0,0,0)$ is a feasible solution of the dual problem $DQ$, by the corollary above the infeasibility of the problem $Q$ means that the dual problem $DQ$ is unbounded, i.e. there exists $(t^*,\lambda^*,\mu^*)$ such that
    
    $$
    c^T\mu^* - b^T\lambda^* <0,~ ct^* - A^T\lambda^* \ge 0,~ -bt^* + A\mu^* = 0,~t^*\ge 0,~\mu^*\ge 0.
    $$
    
    Now if $t^*>0$, these inequalities actually say that $(x,y)=(\mu^*/t^*,\lambda^*/t^*)$ is a feasible solution of the previous problem, contradicting the assumption. So we must have $t^*=0$. This means
    
    $$
    c^T\mu^* < b^T\lambda^*,~ A^T\lambda^*\le 0,~ A\mu^*=0,~\mu^*\ge 0.
    $$
    
    However, since we have already assumed that the primal and dual problems in the theorem are both feasible, i.e. there exists $(x_0,y_0)$ such that
    
    $$
    Ax_0 = b,~ x_0\ge 0,~ A^Ty_0\le c
    $$
    
    holds, we have
    
    $$
    0 = (A\mu^*)^Ty_0 = (A^Ty_0)^T\mu^* \le c^T\mu^* < b^T\lambda^* = x_0^TA^T\lambda^* \le 0.
    $$
    
    This is clearly a contradiction. This contradiction shows that the problem $Q$ is feasible, and hence that strong duality holds.

From the proof of the strong duality theorem we also obtain the following corollary:

???+ note "Corollary"
    Suppose feasible solutions $x^*$ and $y^*$ of the primal and dual problems, respectively, satisfy strong duality, i.e. $c^Tx^* = b^Ty^*$. Then they are also optimal solutions of the primal and dual problems, respectively.

The strong duality theorem shows that for a feasible linear programming problem, it suffices to solve its dual problem to obtain the optimal value of the primal problem.

### Complementary slackness conditions

As with other optimization problems, the complementary slackness conditions are part of the optimality conditions of linear programming problems. Moreover, since the objective function is linear, for linear programming problems the complementary slackness conditions are a necessary and sufficient condition for a feasible solution to be optimal.

The **complementary slackness** condition says that a variable of the dual (primal) problem can take a nonzero value only when the corresponding constraint of the primal (dual) problem holds with equality (i.e. the constraint is tight). If we also regard a variable taking a nonzero value as a slack constraint, this amounts to saying that corresponding variables and constraints of the primal and dual problems cannot be slack at the same time. Hence this condition is called the complementary slackness condition.

Taking the linear programming problem in standard form as an example, the following conclusion holds:

???+ note "Theorem"
    Suppose $x^*$ and $y^*$ are feasible solutions of the primal problem $\min\{c^Tx:Ax=b,~x\ge 0\}$ and the dual problem $\max\{b^Ty:A^Ty\le c\}$, respectively. Then the complementary slackness condition holds, i.e.
    
    $$
    (x^*)^T(A^Ty^*-c) = 0
    $$
    
    if and only if $x^*$ and $y^*$ are also optimal solutions of the primal and dual problems, respectively.

??? note "Proof"
    Since $x^*$ and $y^*$ are both feasible solutions, we have
    
    $$
    b^Ty^* - c^Tx^* = (x^*)^T(A^T y^* - c).
    $$
    
    Therefore, the complementary slackness condition holds if and only if $b^Ty^* = c^Tx^*$. By the corollary of the strong duality theorem, this condition holds if and only if $x^*$ and $y^*$ are optimal solutions of the primal and dual problems, respectively.

The standard form may be too special. A slightly more general form of the theorem is as follows:

???+ note "Theorem"
    Suppose $x^*$ and $y^*$ are feasible solutions of the primal problem $\min\{c^Tx:Ax\ge b,~x\ge 0\}$ and the dual problem $\max\{b^Ty:A^Ty\le c,~y\ge 0\}$, respectively. Then the complementary slackness conditions hold, i.e.
    
    $$
    (x^*)^T(A^Ty^*-c) = (y^*)^T(Ax^*-b) = 0
    $$
    
    if and only if $x^*$ and $y^*$ are also optimal solutions of the primal and dual problems, respectively.

??? note "Proof"
    The proof is basically the same as above, except that this time the difference is written as
    
    $$
    b^Ty^* - c^Tx^* = (x^*)^T(A^T y^* - c) - (y^*)^T(Ax^*-b).
    $$

The complementary slackness conditions provide a simple criterion for checking the optimality of a feasible solution of a linear programming problem.

### Primal-dual method

The dual problem can assist in solving the primal problem. A method often used when solving linear programming problems is the **primal-dual method**. By solving a sequence of relatively simple auxiliary problems, it gradually improves the solution of the dual problem and thereby obtains an optimal solution of the primal problem.

For the primal problem in standard form

$$
(P)\qquad\min\{c^Tx : Ax=b\ge 0,~ x\ge 0\}
$$

and its dual problem

$$
(D)\qquad\max\{b^Ty : A^Ty\le c\},
$$

the previous section showed that to find their optimal solutions, it suffices to find a pair of feasible solutions of the problems $(P)$ and $(D)$ that satisfy the complementary slackness condition $x^T(A^Ty-c)=0$. So consider the following procedure:

1.  Starting from a feasible solution $y$ of the dual problem $(D)$, compute the set of tight constraints of the dual problem

    $$
    I = \{i : (A^Ty - c)_i = 0\}.
    $$

2.  By the complementary slackness condition, if there is a feasible solution $x$ of the problem $(P)$ such that $x_i>0$ holds only for $i\in I$, this means that a pair of optimal solutions has already been found. Therefore, consider the linear programming problem

    $$
    (RP)\qquad
    \begin{aligned}
    \min_{x,s}\;& 1^Ts \\
    \text{subject to } & Ax + s = b, \\
    & x_i \ge 0,~\forall i \in I,\\
    & x_i = 0,~\forall i \notin I,\\
    & s \ge 0.
    \end{aligned}
    $$

3.  If the minimum of the problem $(RP)$ is $0$, then $x^*$ in the optimal solution $(x^*,0)$ is an optimal solution of the original problem $(P)$. Otherwise, we can find a solution $\bar y$ of its dual problem $(DRP)$:

    $$
    (DRP)\qquad
    \begin{aligned}
    \max_{y}\;& b^Ty \\
    \text{subject to }& \sum_{j}a_{ji}y_j \le 0,~\forall i\in I,\\
    & y \le 1.
    \end{aligned}
    $$

    By the strong duality theorem, $b^T\bar y = 1^Ts^*>0$.

4.  Improve the feasible solution of the dual problem $(D)$ according to the solution of the problem $(DRP)$. Let $y' = y + \varepsilon \bar y$, where $\varepsilon>0$; then we certainly have $b^Ty' = b^Ty + \varepsilon b^T\bar y > b^Ty$. Therefore, as long as $y'$ remains a feasible solution of the dual problem $(D)$, the value of $\varepsilon$ should be chosen as large as possible.

    For $i\in I$, we have

    $$
    \sum_ja_{ji}y'_j = \sum_ja_{ji}y_j + \varepsilon \sum_ja_{ji}\bar y_j \le c_i,
    $$

    so these constraints of the problem $(D)$ are always satisfied.

    For the remaining constraints, i.e. for $i\notin I$, it suffices to take

    $$
    \varepsilon = \min\left\{\dfrac{c_i - \sum_{j}a_{ji}y_j}{\sum_{j}a_{ji}\bar y_j}:i\notin I,~\textstyle\sum_{j}a_{ji}\bar y_j>0\right\}
    $$

    which improves the solution of the dual problem as much as possible while preserving feasibility; then return to step 1 and continue iterating. In particular, if the set in the expression above is empty, i.e. $\varepsilon=+\infty$, then the dual problem $(D)$ is unbounded and the original problem $(P)$ is infeasible.

In this procedure, only the problem $(DRP)$ actually needs to be solved; it is connected to the problem $(RP)$ through the strong duality theorem. The problem $(DRP)$ provides a direction for improving the solution of the dual problem, and compared with the dual problem $(D)$ itself, the problem $(DRP)$ has a simpler form. The problem $(DRP)$ is always feasible ($y=0$ is a feasible solution), and the constraint $y\le 1$ is just a normalization condition that guarantees that the problem $(DRP)$ is bounded.

In competitive programming, the primal-dual method is widely applied to all kinds of combinatorial optimization problems. For example, the [Hungarian algorithm](../graph/graph-matching/bigraph-weight-match.md#hungarian-algorithm-kuhnmunkres-algorithm) for maximum weight bipartite matching, the [cycle-canceling algorithm](../graph/flow/min-cost.md) and the [SSP algorithm (primal-dual algorithm)](../graph/flow/min-cost.md#ssp-algorithm) for minimum-cost flow, [Dijkstra's algorithm](../graph/shortest-path.md#dijkstras-algorithm) for shortest paths, the [Ford–Fulkerson augmenting algorithm](../graph/flow/max-flow.md#fordfulkerson-augmentation) for maximum flow, etc., can all be viewed as direct applications of the primal-dual method.

## Integer programming

**Integer programming** usually refers to **integer linear programming** (ILP). The integer linear program in standard form is as follows:

$$
\begin{aligned}
\min_{x}\; & c^Tx \\
\text{subject to } & Ax = b \ge 0,\\
& x \ge 0,\\
& x \in \mathbf Z^n,
\end{aligned}
$$

where $A\in\mathbf R^{m\times n}$, $b\in\mathbf R^m$, $c\in\mathbf R^n$. That is, integer linear programming is the problem obtained by adding to a linear programming problem the constraint that the decision variables must be integers.

The integrality constraint significantly increases the complexity of integer programming problems. Many combinatorial optimization problems, such as the knapsack problem, the satisfiability problem and numerous optimization problems in graph theory, can be expressed as integer programming models, and most of these problems have been proven to be NP-hard.

### Totally unimodular matrices

For this very reason, for many large-scale integer optimization problems one sometimes considers relaxing the integrality constraints and solving a linear programming problem instead. In general, the optimal value of the relaxed linear programming problem is only a lower bound estimate of that of the original integer programming problem (assuming the problem is a minimization problem). However, if the optimal solution of the relaxed linear programming problem happens to be an integer solution, then it must also be an optimal solution of the original integer programming problem.

A natural question is whether there are conditions that guarantee that all optimal solutions of a linear programming problem are integer solutions. The concept of a totally unimodular matrix provides exactly such a condition.

???+ abstract "Totally unimodular matrix"
    If the determinants of all square submatrices of a matrix $A\in\mathbf R^{m\times n}$ are $0$ or $\pm 1$, then the matrix $A$ is called a **totally unimodular matrix**.

In particular, all entries of a totally unimodular matrix are $0$ or $\pm 1$. Using the concept of a totally unimodular matrix, the following conclusion can be stated:

???+ note "Theorem"
    For a totally unimodular matrix $A\in\mathbf Z^{m\times n}$, $b\in\mathbf Z^{m}$ and $c\in\mathbf Z^n$, the linear programming problem and its dual problem
    
    $$
    \min\{c^Tx : Ax=b,x\ge 0\} = \max\{b^Ty: A^Ty\le c\}
    $$
    
    both have integer optimal solutions, as long as they are both bounded.

??? note "Proof"
    It was shown earlier that the set of optimal solutions of a linear programming problem can be taken to be one of its minimal faces, and the latter is the solution set of the system of equations obtained by setting several linearly independent tight constraints to equalities:
    
    $$
    \{x\in\mathbf R^n : a_j^Tx = b_j,~\forall j\in J\}.
    $$
    
    Denote this system by $A_Jx=b_J$, and let $A_J=(A_1,A_2)$, where $A_1$ is a square matrix of full rank with determinant $\pm 1$. Then, by Cramer's rule, the solution
    
    $$
    x = \begin{pmatrix}A_1^{-1}b_J \\ 0\end{pmatrix}
    $$
    
    is an integer solution on the minimal face.

Among common graph-theoretic models, the coefficient matrices of the linear programming problems corresponding to network flow, shortest paths, bipartite graphs, etc. are all totally unimodular. Therefore, as long as these problems involve only integer parameters, their optimal solutions can be taken to be integers, without worrying that the solution of the linear programming problem corresponds to a fractional flow, a fractional matching, etc. Hence, problems such as [maximum flow](../graph/flow/max-flow.md), [minimum cut](../graph/flow/min-cut.md), [minimum-cost flow](../graph/flow/min-cost.md), [shortest paths](../graph/shortest-path.md), [difference constraints](../graph/diff-constraints.md), and [maximum (weight) bipartite matching and minimum vertex cover](../graph/graph-matching/bigraph-match.md#linear-programming-formulation) can all be converted into linear programming problems and solved. Moreover, maximum flow and minimum cut, shortest paths and difference constraints, and maximum bipartite matching and minimum vertex cover are pairwise dual problems.

In addition, there are some common graph-theoretic models whose feasible solutions happen to be exactly all the vertices of some polytope whose vertices are all integer points. Therefore, by cleverly choosing the constraints, the solution of the corresponding combinatorial optimization problem can be made exactly the optimal solution of some linear programming problem. For example, graph-theoretic models such as general graph matching and spanning trees belong to this situation, so problems such as [maximum (weight) matching in general graphs](../graph/graph-matching/general-weight-match.md) and [minimum spanning tree](../graph/mst.md) can likewise be converted into linear programming problems.

## References and notes

-   Schrijver, Alexander. Theory of linear and integer programming. John Wiley & Sons, 1998.
-   Papadimitriou, Christos H., and Kenneth Steiglitz. Combinatorial optimization: algorithms and complexity. Courier Corporation, 1998.
-   [Duality in linear programming. Part 1—definition and construction. by adamant - Codeforces blog](https://codeforces.com/blog/entry/105049)
-   [Duality in linear programming. Part 2—in competitive programming. by adamant - Codeforces blog](https://codeforces.com/blog/entry/105789)

[^poly-names]: Different references may define these two terms differently: some call the bounded case a "polyhedron" and the unbounded case a "polytope"; some do not assume that they are necessarily convex sets; some use "polyhedron" for polytopes in three-dimensional space. This article adopts definitions consistent with Schrijver (1998), Boyd and Vandenberghe (2004) and others.

[^reducible]: More precisely, they are mutually reducible to each other in polynomial time.

[^other-methods]: Other methods for solving systems of inequalities include Fourier–Motzkin elimination and the Agmon–Motzkin–Schoenberg relaxation method. They are more direct, but often not efficient.
