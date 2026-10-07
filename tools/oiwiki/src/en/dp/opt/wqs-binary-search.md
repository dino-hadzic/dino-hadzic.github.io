---
title: WQS binary search
---

## Introduction

This article introduces a method for optimizing dynamic programming problems using WQS binary search. In different articles it is also called weighted binary search, convex optimization DP, DP with complete convex monotonicity, the method of Lagrange multipliers, and so on; outside China it is also known as the Aliens Trick. It was first summarized by Wang Qinshi in the paper "浅析一类二分方法" (A brief analysis of a class of binary search methods).

WQS binary search is usually used to solve the following class of optimization problems: they come with a cardinality constraint, so solving them directly is expensive; but once this constraint is removed, the problem itself becomes much easier.

For example, suppose the problem is to choose $m$ out of $n$ items and optimize some relatively complicated objective function. If we let $f(i,j)$ be the optimal value of the objective when choosing $j$ items among the first $i$, then the answer to the original problem is $f(n,m)$. In such problems the state transition equation is usually two-dimensional. Implementing this transition directly has time complexity $O(nm)$, which is unacceptable.

Suppose further that the optimization problem without the cardinality constraint is easy to solve. However, the optimal number of chosen items need not satisfy the cardinality constraint of the original problem. Suppose too many items are chosen. Then we can attach a fixed penalty $k$ (the "weight" in "weighted binary search") to every chosen item and still solve the optimization problem without the cardinality constraint. Depending on the value of $k$, the optimal number of chosen items will differ; moreover, as $k$ changes, the optimal number changes monotonically. Therefore, by binary search we can find a $k$ for which the optimal number of chosen items is exactly $m$. If the optimal value of the objective is then $f_k(n)$, we only need to remove the loss of value caused by the extra penalty to obtain the answer to the original problem, $f(n,m)=f_k(n)-km$. If solving the penalized problem once has complexity $O(T(n))$, the overall complexity of the algorithm drops to $O(T(n)\log L)$, where $O(\log L)$ is the number of binary search steps on $k$.

This is the basic idea of WQS binary search. However, for this idea to work, the prerequisite is that $f(n,m)$ is convex in $m$. Otherwise, there may be no penalty $k$ for which the optimal number is exactly $m$. This is also why this DP optimization is often called "convex optimization DP" or "DP with complete convex monotonicity".

## Traditional method

Let the non-empty set $X$ be the (finite) decision space, $f:X\rightarrow\mathbf R$ the objective function, and let $g:X\rightarrow\mathbf R^d$ be another function used to impose a constraint. The problem to be solved can be viewed as computing the value of the value function $v(y)$ of the following optimization problem at some point:

$$
\begin{aligned}
v(y)=\min_{x\in X}\;&f(x)\\
\text{subject to }&g(x)=y.
\end{aligned}
$$

For example, for the cardinality-constrained problem mentioned above, $X$ can be understood as the family of all subsets of the set of items, $x\in X$ is a single subset, $f(x)$ is the value of that subset, and $g(x)$ is the number of elements of the subset $x$. Of course, $g(x)$ need not be a cardinality constraint; examples of more general constraints are given later.

???+ info "Convention"
    For convenience of exposition, this article only discusses problems that minimize the objective function. Problems that maximize the objective are analogous, except that the (lower) convex functions in this article must be replaced by concave functions (also called upper convex functions). Alternatively, by adding a minus sign, a maximization problem can be turned into the problem of minimizing the negative of the objective.

### Geometric intuition

Since most problems encountered in competitive programming are combinatorial optimization problems, the decision space $X$ usually has no nice structure, so we can instead consider the set

$$
\mathcal D = \{(g(x),f(x))\in\mathbf R^d\times\mathbf R:x\in X\}.
$$

The traditional method mainly handles the case $d=1$, i.e. the case of a single constraint. The figure below gives one possible illustration of the point set $\mathcal D$ in this case.

![](../images/wqs-binary-search/wqs-f-g-space.svg)

The red and blue points in the figure form the set $\mathcal D$ obtained by projecting all possible choices in $X$ onto the plane $(g(x),f(x))$. The original problem asks for the minimum ordinate $v(y)$ among the points whose abscissa is $y$. As $y$ varies, all such points $(y,v(y))$ form the set of red points in the figure.

To obtain the ordinate of the point $(y,v(y))$, we can cut the set $\mathcal D$ with a line of slope $\lambda\in\mathbf R$. As shown in the figure, when the slope of the line is chosen appropriately, the line through the point $(y,v(y))$ is the one with the smallest intercept $f(x)-\lambda g(x)$ among all lines of slope $\lambda$ passing through points of $\mathcal D$. Denote this minimum by

$$
h(\lambda) = \min_{x\in X}f(x)-\lambda g(x).
$$

Then, since $(y,v(y))$ also lies on this line, we obtain the solution of the original problem

$$
v(y) = h(\lambda) + \lambda y.
$$

Suppose that for all $\lambda$ in a reasonable range the function $h(\lambda)$ above is easy to compute. This often holds in competitive programming, since the constraint of the original problem has been removed. Then the two most important questions we face are:

1.  whether there exists a slope $\lambda$ such that the minimum intercept is attained exactly at the point $(y,v(y))$, and
2.  if so, how to find such a slope $\lambda$.

The first question is relatively easy. As the slope $\lambda$ changes, the set cut out by all these lines (i.e. the intersection of the corresponding upper half-planes) is necessarily a convex set. Therefore, these lines can pass through a point if and only if the point lies on the lower convex hull of this convex set. This is equivalent to saying that the function $v(y)$ is [convex](./slope-trick.md#离散点集上的凸函数).

The second question is more delicate. Since the abscissa of the desired point is already known to be $y$, a natural idea is to compute, along with $h(\lambda)$, the value of the constraint function $g(x)$ at the current optimal solution $x_\lambda$. For example, in the example mentioned above, when solving the penalized problem we can record the number of items chosen when the penalized objective attains its optimum. Then we compare $g(x_\lambda)$ with the desired $y$ and adjust the value of $\lambda$ for the next computation accordingly. This is the most traditional WQS binary search method.

In summary, the basic procedure of traditional WQS binary search is as follows:

1.  initially, choose a reasonable interval for $\lambda$;
2.  choose a $\lambda$ in the current interval;
3.  solve the penalized problem $h(\lambda)=\min_{x\in X}f(x)-\lambda g(x)$ and record the value $g(x_\lambda)$ of $g(x)$ at its optimal solution $x_\lambda$;
4.  if $g(x_\lambda)=y$, we obtain the optimal value of the original problem $v(y)=h(\lambda)+\lambda y$ and the algorithm terminates immediately;
5.  otherwise, adjust the interval of $\lambda$ according to the relation between $g(x_\lambda)$ and $y$, and return to step 2.

This basic procedure is already enough to solve some problems, but it is not complete. Next, this article discusses improvements to this basic procedure.

### Handling the collinear case

When applying the basic procedure, the first problem encountered is that the collinear case is not handled correctly.

If there are three or more collinear red points on the lower convex hull of the point set $\mathcal D$, the basic procedure above may fail to correctly determine the relation between $g(x_\lambda)$ and $y$. For example, let the abscissas of the three collinear red points be $y_1,y_2,y_3$, and let the slope of the line through them be $\lambda^*$. Then, to correctly compute $v(y_2)$, we must ensure that the last problem computed when the algorithm terminates is $h(\lambda^*)$, because $\lambda^*$ is the only slope for which the line minimizing the intercept can pass through the point $(y_2,v(y_2))$. However, in the process of solving $h(\lambda^*)$, the recorded $g(x_{\lambda^*})$ may be any of $y_1,y_2,y_3$. If the recorded $g(x_{\lambda^*})$ is not equal to $y_2$, the algorithm will mistakenly continue and adjust the interval of $\lambda$ in the direction away from $y_2$, eventually producing a wrong result.

To handle the collinear case, one approach is to always make the recorded $g(x_\lambda)$ corresponding to the optimal solution $x_\lambda$ as large (or as small) as possible. At the same time, the termination condition of the binary search is changed from finding a $\lambda$ satisfying $g(x_\lambda)=y$ exactly to finding the smallest (or largest) $\lambda$ satisfying $g(x_\lambda)\ge y$ (or $g(x_\lambda)\le y$). In the example of the previous paragraph, this amounts to making the recorded $g(x_{\lambda^*})$ equal to $y_3$ when computing the problem $h(\lambda^*)$. This guarantees that the last problem computed when the algorithm terminates is $h(\lambda^*)$. When implementing this approach, note that the final output is not $h(\lambda)+\lambda g(x_{\lambda})$ but $h(\lambda)+\lambda y$, because the recorded $g(x_\lambda)$ need not equal the actual constraint $y$.

Another approach is binary search over real numbers. If all the numbers involved in the problem are integers, obviously the slope in WQS binary search is also an integer. Real numbers are introduced into the binary search so that, when the correct option $\lambda^*$ is wrongly excluded, the fractional part allows us to adjust back and eventually approach the correct answer $\lambda^*$. For example, in the example above, if when computing $h(\lambda^*)$ the recorded $g(x_{\lambda^*})$ is $y_1$, which is smaller than the desired $y_2$, the algorithm will turn to the interval $(\lambda^*,\lambda_r]$, where $\lambda_r$ is the right endpoint of the interval containing $\lambda$. In the integer case this interval should really be written as $[\lambda^*+1,\lambda_r]$, which excludes the possibility of approaching the correct answer $\lambda^*$ in the rest of the algorithm. However, in real-valued binary search the interval considered is still $(\lambda^*,\lambda_r]$, and for $\lambda$ in this interval the $g(x_\lambda)$ recorded when solving $h(\lambda)$ is always at least $y_3$, hence strictly greater than $y_2$. Therefore, as the algorithm continues, the right half of the interval is repeatedly discarded, so the final range of $\lambda$ is guaranteed to be near $\lambda^*$. Of course, since we already know that the desired slope is an integer, the precision at which the real-valued binary search terminates need not be high; it suffices that the interval contains only one integer, and this integer is the desired $\lambda^*$.

After correctly handling the collinear case, WQS binary search is enough to solve the vast majority of WQS binary search problems encountered in competitive programming. However, this method still has some shortcomings: it cannot handle cases where $g(x_\lambda)$ is hard to record, nor the case of several coplanar points in higher-dimensional WQS binary search. This article will further examine the properties of the optimization problem $v(y)$ and propose a more general approach.

## Dual method

This section introduces an implementation of WQS binary search that only requires that, for all $\lambda\in\mathbf R^d$, the value

$$
h(\lambda) = \min_{x\in X}f(x)-\lambda\cdot g(x)
$$

can be computed efficiently, and that the optimal value $v(y)$ of the original problem is a convex function of $y\in\mathbf R^d$[^high-d-convex]. In one sentence, this section will prove that the value function $v(y)$ of the original problem equals the optimal value of its dual problem

$$
v^\star(y) = \sup_{\lambda\in\mathbf R^d} h(\lambda)+\lambda\cdot y,
$$

and the objective of the dual problem is a concave function of $\lambda\in\mathbf R^d$, hence unimodal, so it can be solved efficiently by [ternary search](../../basic/binary.md#三分法) or the [golden-section search](../../basic/binary.md#优化黄金分割法), with complexity still $O(T(n)\log^d L)$. This completely resolves the problems that may arise from recording the value of $g(x_\lambda)$ in the traditional WQS binary search method, and at the same time allows the idea of WQS binary search to be applied in higher dimensions.

In addition, this section also shows that the range of $g(x_\lambda)$ can be obtained from $h(\lambda)$ without extra bookkeeping while solving $h(\lambda)$. For example, for $d=1$ and problems involving only integers, it can be shown that the range of $g(x_\lambda)$ is exactly

$$
[h(\lambda-1)-h(\lambda),h(\lambda)-h(\lambda+1)].
$$

This actually also provides another way to handle the collinearity problem for problems where the binary search procedure described above must be used.

Next, this section uses the theory of convex analysis to prove these conclusions. For concrete applications of these methods, see the section [Example problems](#example-problems).

### Lagrangian duality

Consider solving this problem with the [method of Lagrange multipliers](https://en.wikipedia.org/wiki/Lagrange_multiplier). Introducing a Lagrange multiplier $\lambda\in\mathbf R^d$, the Lagrangian can be written as

$$
L(x,\lambda,y) = f(x) - \lambda\cdot g(x)+\lambda\cdot y.
$$

Since as soon as one component of $g(x)-y$ is non-zero we can let the corresponding component of $\lambda$ tend to (positive or negative) infinity, we have

$$
\sup_{\lambda\in\mathbf R^d}L(x,\lambda,y)
= \begin{cases}
f(x),&g(x)=y,\\
+\infty,&\text{otherwise}.
\end{cases}
$$

This shows that the original problem can be written as

$$
\begin{aligned}
v(y) &= \min_{x\in X}\sup_{\lambda\in\mathbf R^d}L(x,\lambda,y).
\end{aligned}
$$

Exchanging the two extremum operations yields its [dual problem](https://en.wikipedia.org/wiki/Duality_%28optimization%29):

$$
\begin{aligned}
v^\star(y)&=\sup_{\lambda\in\mathbf R^d}\min_{x\in X}L(x,\lambda,y)\\
&=\sup_{\lambda\in\mathbf R^d}h(\lambda)+\lambda\cdot y.
\end{aligned}
$$

We will shortly show that, under the condition that $v(y)$ is a convex function of $y$, strong duality holds, i.e. $v^\star(y)=v(y)$.

### Convex conjugate

To show that strong duality holds, we need the notion of the convex conjugate.

???+ abstract "Convex conjugate"
    For a function $f:\mathbf R^d\rightarrow\mathbf R\cup\{\pm\infty\}$, its **convex conjugate**, also called its **Legendre–Fenchel transformation**, is the function
    
    $$
    f^*(x^*) = \sup_{x\in\mathbf R^d}x^*\cdot x - f(x).
    $$

Viewed as a function of the variable $x^*$, $f^*(x^*)$ is the supremum of a family of linear functions, so it is necessarily a convex function on $\mathbf R^d$.

???+ info "The "slope vector" and "intercept" of a hyperplane"
    The equations of the hyperplanes in the vector space $\mathbf R^{d+1}$ discussed in this article all have the form
    
    $$
    y = k\cdot x + b.
    $$
    
    That is, this article does not involve hyperplanes parallel to the $y$ axis. For convenience, this article loosely calls $k$ the "slope vector" of the hyperplane and $b$ its "intercept". Writing the equation of this hyperplane in a more standard form, we get
    
    $$
    k\cdot x - y = -b.
    $$
    
    One of its normal vectors is $(k,-1)$. Therefore, the so-called slope vector is actually the first $d$ components of the normal vector of the hyperplane normalized so that its last component equals $-1$.

Geometrically, the convex conjugate of a function $f(x)$ describes the following: among all hyperplanes with slope vector $x^*$ that intersect the epigraph of $f(x)$

$$
\operatorname{epi}f = \{(x,y)\in\mathbf R^d\times\mathbf R:f(x)\le y\}
$$

the minimum intercept $f(x)-x^*\cdot x$ is $-f^*(x^*)$. In other words, the function $f(x)$ always lies above the hyperplane $y = x^*\cdot x-f^*(x^*)$ and touches it at the point $(x_0,f(x_0))$; of course, there may be other points of tangency. Such a hyperplane is called a **supporting hyperplane** of $f(x)$ at $x_0$. The intercept of a supporting hyperplane of $f(x)$ is uniquely determined by its slope vector, and the convex conjugate provides this mapping from slope vector to intercept.

Minimizing $f(x)-\lambda\cdot g(x)$ over the set $X$ is equivalent to minimizing $v(y)-\lambda\cdot y$ over the set $\{(y,v(y))\}$:

$$
\begin{aligned}
\min_x f(x)-\lambda\cdot g(x) &= \min_{y\in g(X)}\left(\min_{x\in X:g(x)=y} f(x) - \lambda\cdot g(x)\right)\\
&= \min_{y\in g(X)}\left(\min_{x\in X:g(x)=y} f(x)\right) - \lambda\cdot y \\
&= \min_{y\in g(X)}v(y) - \lambda\cdot y.
\end{aligned}
$$

Therefore,

$$
h(\lambda) = \min_{y\in g(X)}v(y) - \lambda\cdot y = -v^*(\lambda).
$$

This shows that $h(\lambda)$ is a concave function of $\lambda\in\mathbf R^d$. Furthermore,

$$
v^\star(y) = \sup_{\lambda\in\mathbf R^d}\lambda\cdot y-v^*(\lambda) = v^{**}(y).
$$

That is, the value function $v^{\star}(y)$ of the dual problem is the double convex conjugate of the value function $v(y)$ of the original problem, also called the **biconjugate**.

So the question becomes: which functions $v(y)$ have a biconjugate equal to themselves? The answer is given by the following theorem:

???+ note "Theorem (Fenchel–Moreau)"
    For a function $f:\mathbf R^d\rightarrow\mathbf R\cup\{\pm\infty\}$, its biconjugate equals itself, i.e. $f^{**}=f$, if and only if one of the following three conditions holds:
    
    1.  $f(x)$ is a proper convex function and [lower semi-continuous](https://en.wikipedia.org/wiki/Semi-continuity),
    2.  $f(x)\equiv+\infty$, or
    3.  $f(x)\equiv-\infty$.

??? note "Proof"
    A function is proper if and only if it never takes the value $-\infty$ and is not identically $+\infty$.
    
    For improper functions, one can verify that $f(x)\equiv+\infty$ and $f(x)\equiv-\infty$ are conjugates of each other. Apart from that, as soon as $f(x)$ takes the value $-\infty$ at some point, necessarily $f^*(x^*)\equiv+\infty$. So the only improper functions satisfying $f^{**}=f$ are these two cases. The discussion below is restricted to proper functions. For proper functions, the condition of being lower semi-continuous and convex is equivalent to the epigraph being a closed convex set.
    
    The necessity of this condition is easy. Since $f=f^{**}$ is the convex conjugate of $f^*$, as the supremum of a family of linear functions its epigraph is necessarily the intersection of a family of closed convex sets, hence a closed convex set. This shows that a proper function satisfying $f^{**}=f$ must be lower semi-continuous and convex.
    
    Conversely, these conditions are also sufficient. As with the proofs of other strong duality theorems, the proof can be divided into two steps.
    
    In the first step, we show that weak duality holds, i.e. $f(x)\ge f^{**}(x)$. By the definition of the convex conjugate, for all $x,x^*\in\mathbf R^d$ we have
    
    $$
    f^*(x^*) \ge x^*\cdot x-f(x).
    $$
    
    This shows that for all $x,x^*\in\mathbf R^d$ we also have
    
    $$
    f(x) \ge x^*\cdot x-f^*(x^*).
    $$
    
    Taking the supremum over $x^*$ on the right-hand side of the inequality gives $f(x)\ge f^{**}(x)$.
    
    In the second step, we use the [hyperplane separation theorem](https://en.wikipedia.org/wiki/Hyperplane_separation_theorem) to show $f(x)\le f^{**}(x)$. Suppose not: there exists $x_0\in\mathbf R^d$ such that $f(x_0)>f^{**}(x_0)$. Since the epigraph $\operatorname{epi}(f)$ of $f(x)$ is a closed convex set and the singleton $\{(x_0,f^{**}(x_0))\}$ is a compact convex set, by the hyperplane separation theorem there exist $(\lambda,t)\in\mathbf R^d\times\mathbf R$ and $\alpha\in\mathbf R$ such that for all $x\in\operatorname{dom} f:=\{x\in\mathbf R^d:f(x)<+\infty\}$ and all $y\ge f(x)$ we have
    
    $$
    \lambda\cdot x-ty <\alpha <\lambda\cdot x_0 - tf^{**}(x_0)
    $$
    
    Since $y$ can be chosen arbitrarily large, necessarily $t\ge 0$. This again splits into two cases.
    
    First, consider the case $t>0$. Dividing every part of the inequality by $t$ and setting $\lambda'=t^{-1}\lambda$ and $\alpha'=t^{-1}\alpha$, we get
    
    $$
    \lambda'\cdot x-y < \alpha'< \lambda'\cdot x_0-f^{**}(x_0).
    $$
    
    For all $x\in\operatorname{dom} f$, setting $y=f(x)$, we have
    
    $$
    \alpha' > \lambda'\cdot x - f(x).
    $$
    
    Hence, taking the supremum over $x$ on the right-hand side,
    
    $$
    \alpha' \ge \sup_{x\in\mathbf R^d}\lambda'\cdot x - f(x) = f^*(\lambda').
    $$
    
    Furthermore,
    
    $$
    f^{**}(x_0) < \lambda'\cdot x_0-f^*(\lambda') \le \sup_{x^*\in\mathbf R^d}x^*\cdot x_0-f^*(x^*) = f^{**}(x_0).
    $$
    
    This contradiction shows that the case $t>0$ cannot occur.
    
    Finally, consider the case $t=0$. In fact, we will show that by a small perturbation it can be reduced to the case $t>0$. Take any $\lambda_0\in\operatorname{dom}f^*$; by the definition of the convex conjugate, for any $x\in\operatorname{dom}f$ and $y\ge f(x)$ we have
    
    $$
    \lambda_0\cdot x-y\le f^*(\lambda_0).
    $$
    
    Therefore, for any $\varepsilon>0$,
    
    $$
    (\lambda+\varepsilon\lambda_0)\cdot x - \varepsilon y<\alpha+\varepsilon f^*(\lambda_0).
    $$
    
    At the same time, since $\alpha<\lambda\cdot x_0$, for sufficiently small $\varepsilon>0$ we also have
    
    $$
    \alpha+\varepsilon f^*(\lambda_0) < (\lambda+\varepsilon\lambda_0)\cdot x_0 - \varepsilon f^{**}(x_0).
    $$
    
    Therefore, taking $\lambda'=\lambda+\varepsilon\lambda_0$, $t'=\varepsilon$ and $\alpha'=\alpha+\varepsilon f^*(\lambda_0)$, we have
    
    $$
    \lambda'\cdot x-t'y <\alpha' <\lambda'\cdot x_0 - t'f^{**}(x_0).
    $$
    
    This brings us back to the previous case, which again leads to a contradiction.
    
    This contradiction shows that there is no point $x_0\in\mathbf R^d$ with $f(x_0)>f^{**}(x_0)$. Hence, we always have $f(x_0)\le f^{**}(x_0)$.
    
    Combining the results of the two steps, we obtain $f^{**}(x)=f(x)$.

Therefore, strong duality holds if and only if $v(y)$ is a convex function of $y\in\mathbf R^d$[^other-conditions].

### Subgradients

The previous section showed that the value function $h(\lambda)$ of the penalized problem is the negative of the convex conjugate of the value function $v(y)$ of the original problem. Since the definition of the convex conjugate is in fact a parametrized optimization problem, a result analogous to the [envelope theorem](https://en.wikipedia.org/wiki/Envelope_theorem) also holds for it. However, since convex functions are not everywhere differentiable, we first need to generalize the definition of the derivative to convex functions. This leads to the notion of the subgradient.

???+ abstract "Subgradient"
    For a convex function $f:\mathbf R^d\rightarrow\mathbf R\cup\{\pm\infty\}$ and $x_0\in\operatorname{dom}f$, if a vector $x^*\in\mathbf R^d$ satisfies, for every $x\in\mathbf R^d$,
    
    $$
    f(x) \ge f(x_0)+x^*\cdot(x-x_0),
    $$
    
    then $x^*$ is called a **subgradient** of $f(x)$ at $x_0$. The set of all subgradients of $f(x)$ at $x_0$ is called its **subdifferential** at that point, denoted $\partial f(x_0)$.

Geometrically, the subdifferential of a convex function $f(x)$ at $x_0$ is the set of slope vectors of all its supporting hyperplanes at that point. In the one-dimensional case, the subdifferential is

$$
\partial f(x_0) = [\partial_-f(x_0),\partial_+f(x_0)],
$$

where $\partial_-f(x_0)$ and $\partial_+f(x_0)$ are the left and right derivatives of $f(x)$ at $x_0$, respectively. Furthermore, for the function $\tilde f(x)$ obtained by extending a convex function $f:\mathbf Z\rightarrow\mathbf R\cup\{\pm\infty\}$ on the integers, its left and right derivatives at an integer point $x=k$ are the first-order differences on the left and right:

$$
\partial\tilde f(k) = [f(k)-f(k-1),f(k+1)-f(k)]. 
$$

Clearly, a convex function $f(x)$ is differentiable at a point $x_0$ if and only if its subdifferential $\partial f(x_0)$ there is a singleton.

Since the convex conjugate provides the mapping from the slope vector of a supporting hyperplane to its intercept, we can use the convex conjugate to decide whether a slope vector $x^*$ is a subgradient of the convex function $f(x)$ at a given point $x$.

???+ note "Theorem (convex conjugate and subgradients)"
    For a proper convex function $f:\mathbf R^d\rightarrow\mathbf R\cup\{\pm\infty\}$ and any $x,x^*\in\mathbf R^d$, we have
    
    $$
    x^*\in\partial f(x) \iff x^*\cdot x = f(x) + f^*(x^*).
    $$
    
    Furthermore, if $f$ is also lower semi-continuous, then both conditions are equivalent to $x\in\partial f^*(x^*)$.

??? note "Proof"
    By the definition of the subgradient, $x^*\in\partial f(x)$ if and only if
    
    $$
    f(x') \ge f(x) + x^*\cdot(x'-x),~\forall x'\in\mathbf R^d.
    $$
    
    This is equivalent to
    
    $$
    x^*\cdot x - f(x) \ge x^*\cdot x'-f(x'),~\forall x'\in\mathbf R^d.
    $$
    
    which is in turn equivalent to
    
    $$
    x^*\cdot x - f(x) \ge \sup_{x'\in\mathbf R^d}x^*\cdot x'-f(x') = f^*(x^*).
    $$
    
    But by the definition of the convex conjugate, we always have
    
    $$
    x^*\cdot x - f(x) \le f^*(x^*).
    $$
    
    Therefore, the "greater than or equal" in the previous formula is actually equivalent to equality, i.e. equivalent to
    
    $$
    x^*\cdot x = f(x) + f^*(x^*).
    $$
    
    This completes the first part of the proof.
    
    In the case where $f$ is a lower semi-continuous proper convex function, by the Fenchel–Moreau theorem we have $f^{**}=f$. Therefore, these two conditions are equivalent to
    
    $$
    x^*\cdot x = f^*(x^*) + f^{**}(x).
    $$
    
    Applying the conclusion of the first part again, they are also equivalent to $x\in\partial f^*(x^*)$.

This result shows that if $f^{**}=f$, then the subdifferential $\partial f^{*}(x^*)$ of the convex conjugate $f^*$ at $x^*$ is exactly the set of $x$-components of the intersection points of the supporting hyperplane with slope vector $x^*$ and the epigraph $\operatorname{epi}f$.

???+ note "Corollary"
    For a lower semi-continuous proper convex function $f:\mathbf R^d\rightarrow\mathbf R\cup\{\pm\infty\}$ and any $x,x^*\in\mathbf R^d$, we have
    
    $$
    \begin{aligned}
    \partial f(x) &= \arg\max_{y^*\in\mathbf R^d} x\cdot y^* - f^*(y^*),\\
    \partial f^*(x^*) &= \arg\max_{y\in\mathbf R^d} x^*\cdot y - f(y).
    \end{aligned}
    $$

??? note "Proof"
    We prove the second equality. The proof of the first is similar.
    
    By the definition of the convex conjugate,
    
    $$
    f^*(x^*) = \sup_{y\in\mathbf R^d} x^*\cdot y - f(y),
    $$
    
    so
    
    $$
    x \in \arg\max_{y\in\mathbf R^d} x^*\cdot y - f(y)
    $$
    
    if and only if $f^*(x^*) = x^*\cdot x - f(x)$, and this equality holds if and only if $x\in\partial f^*(x^*)$. This proves that the two sets are equal.

Applied to the setting of this article, this result shows that when solving the problem

$$
h(\lambda) = \min_{x\in X}f(x)-\lambda\cdot g(x) = \min_{y\in g(X)}v(y) - \lambda\cdot y
$$

the set of values of the constraint function $g(x)$ over the set of optimal decisions is exactly $\partial(-h(\lambda))$. For $d=1$ and problems involving only integers, this set is the interval

$$
[h(\lambda-1)-h(\lambda),h(\lambda)-h(\lambda+1)].
$$

For consecutive integers $\lambda$, these intervals join end to end, so when used for binary search only one endpoint needs to be computed.

## Proving convexity

The prerequisite for applying WQS binary search is the convexity of the value function. In competitive programming, convexity can be guessed by tabulating values, by intuition, and so on. However, rigorously proving convexity is often not easy. This section uses the following classic problem to introduce common ways of proving convexity in competitive programming.

???+ example "Tree planting problem"
    There are $n$ pits and $m$ trees must be planted. Trees cannot be planted in two adjacent pits. A sequence $\{a_i\}$ of length $n$ is given, representing the profit of planting a tree in each pit; the profit may be positive or negative. Find the maximum possible total profit after planting these $m$ trees.
    
    In short, this is the problem of finding a maximum-weight independent set of size $m$ on a chain of length $n$.

These methods can be roughly divided into four categories:

-   reduction to the convexity of the value function of a convex optimization problem (including [linear programming](../../math/linear-programming.md) etc.) with respect to its parameters, which includes building [minimum-cost flow](../../graph/flow/min-cost.md) models and the like;
-   using the state transition equation, convexity can also be proved inductively, possibly using some [convexity-preserving transformations](./slope-trick.md#凸函数的变换);
-   for interval partition problems, one can verify that the cost function of each interval satisfies the [quadrangle inequality](./quadrangle.md);
-   finally, for special problems, convexity can also be shown directly by an exchange argument.

These proof methods are often themselves tied to some way of solving the problem.

### Reduction to parametrized convex optimization

Consider a parametrized convex optimization problem of the following form:

$$
v(y)=\inf_{x\in\mathcal D(y)} f(x,y).
$$

Here the objective $f:\mathbf R^m\times\mathbf R^d\rightarrow\mathbf R\cup\{\pm\infty\}$ is, for every $y\in\mathbf R^d$, a convex function of $x\in\mathbf R^m$, and the feasible region $\mathcal D:\mathbf R^d\rightarrow \mathcal P(\mathbf R^m)$ is a set-valued function on $\mathbf R^d$ such that for every $y\in\mathbf R^d$ the set $\mathcal D(y)$ is convex. These conditions guarantee that for any parameter $y\in\mathbf R^d$ this is a convex optimization problem.

???+ note "Theorem"
    Suppose the parametrized convex optimization problem above satisfies the following conditions:
    
    1.  the objective $f(x,y)$ is a convex function of $(x,y)$;
    2.  the graph $\{(x,y):x\in\mathcal D(y)\}$ of the feasible-region mapping $y\mapsto\mathcal D(y)$ is a convex set.
    
    If $v(y)>-\infty$ for every $y\in\mathbf R^d$, then the value function $v(y)$ is a proper convex function of $y$.

??? note "Proof"
    For any $y_1,y_2\in\mathbf R^d$ and $\alpha\in(0,1)$, we need to prove
    
    $$
    v(\alpha y_1+(1-\alpha)y_2) \le \alpha v(y_1) + (1-\alpha) v(y_2).
    $$
    
    If $v(y_1)=+\infty$ or $v(y_2)=+\infty$, the right-hand side is $+\infty$ and the inequality holds trivially. Otherwise, $v(y_1)$ and $v(y_2)$ are both finite. For any $\varepsilon>0$ and $i=1,2$, there exists $x_i\in\mathcal D(y_i)$ such that $f(x_i,y_i)< v(y_i)+\varepsilon$. By the convexity of the graph of the mapping $\mathcal D$,
    
    $$
    \alpha x_1+(1-\alpha)x_2 \in \mathcal D(\alpha y_1+(1-\alpha)y_2).
    $$
    
    That is, $\alpha x_1+(1-\alpha)x_2$ is a feasible solution of the optimization problem with parameter $\alpha y_1+(1-\alpha)y_2$. By optimality and the convexity of the objective,
    
    $$
    \begin{aligned}
    v(\alpha y_1+(1-\alpha)y_2)
    &\le f(\alpha x_1+(1-\alpha)x_2,\alpha y_1+(1-\alpha)y_2) \\
    &\le \alpha f(x_1,y_1) + (1-\alpha)f(x_2,y_2) \\
    &< \alpha v(y_1) + (1-\alpha) v(y_2) + \varepsilon.
    \end{aligned}
    $$
    
    Since $\varepsilon$ was arbitrary, letting $\varepsilon\rightarrow 0$ gives
    
    $$
    v(\alpha y_1+(1-\alpha)y_2) \le \alpha v(y_1) + (1-\alpha) v(y_2).
    $$
    
    Therefore, the value function $v(y)$ is convex.

In competitive programming, the most common convex optimization problem is linear programming.

???+ note "Corollary"
    Let $c\in\mathbf R^n$, $A_1\in\mathbf R^{d_1\times n}$, $A_2\in\mathbf R^{d_2\times n}$, $y_1\in\mathbf R^{d_1}$, $y_2\in\mathbf R^{d_2}$. Consider the following parametrized linear program:
    
    $$
    v(y_1,y_2)=\min_{x\in\mathbf R^n} c\cdot x \text{ subject to }A_1x\le y_1,A_2x=y_2,x\ge 0.
    $$
    
    Then the value function $v(y_1,y_2)$ is a convex function of $(y_1,y_2)$.

Whether the constraints are inequalities or equalities, the value function of a linear program is a convex function of the constraint parameters.

Many graph problems can be written as linear programs:

-   network flow problems: maximum flow, minimum cut, minimum-cost flow;
-   shortest paths without negative cycles;
-   maximum (weight) matching, minimum vertex cover, etc. in bipartite graphs;
-   maximum (weight) matching in general graphs;
-   the minimum spanning tree problem[^mst].

Therefore, the value functions of these problems are convex (concave) functions of the problems' parameters.

???+ warning "Integrality constraints"
    When modeling real problems with graph models, there are usually implicit integrality constraints, e.g. an edge can only be chosen or not chosen, flows can only be integers, etc. Therefore, they can only be turned into integer linear programming (ILP) problems rather than linear programming (LP) problems. Since ILP is not a convex optimization problem, its value function need not be a convex function of the problem's parameters. Relaxing the integrality constraints of an ILP yields an LP, but the latter need not have an optimal solution satisfying the integrality constraints. Therefore, the optimal value of the LP obtained by relaxing the integrality constraints may be strictly better than that of the corresponding ILP, and the two are not necessarily equivalent.
    
    The graph problems listed above can all be written as LPs without imposing integrality constraints; but for some other problems, such as the maximum independent set problem in general graphs, the integrality constraints are necessary. Moreover, even if a graph problem can be written as an LP, adding extra linear constraints to the problem may still break the equivalence between the corresponding ILP and LP, so that the constrained graph problem can no longer be written as a linear program.

For example, in the context of minimum-cost flow, the following common result holds:

???+ note "Corollary"
    In the [minimum-cost flow model](../../graph/flow/min-cost.md), the minimum cost $v(m)$ is a convex function of the flow $m$.

??? note "Proof"
    Let $G=(V,E)$ be a directed graph, let edge $(i,j)$ have capacity $c_{ij}$ and cost $w_{ij}$ per unit of flow, and let the source and sink be $s$ and $t$. Denote the decision variables by $\{f_{ij}\}$, where $f_{ij}$ is the flow on edge $(i,j)\in E$. Then minimum-cost flow can be written as the following linear program:
    
    $$
    \begin{aligned}
    v(m)=\min_{\{f_{ij}\}}\;&\sum_{(i,j)\in E}w_{ij}f_{ij}\\
    \text{subject to }&\sum_{(j,i)\in E}f_{ji} - \sum_{(i,j)\in E}f_{ij} = 
    \begin{cases}
    -m, & i=s,\\
    m,  & i=t,\\
    0,  & \text{otherwise},
    \end{cases}
    ~\forall i\in V,\\
    &0\le f_{ij}\le c_{ij},~\forall (i,j)\in E.
    \end{aligned}
    $$
    
    Therefore, the minimum cost $v(m)$ is a convex function of the parameter $m$.

Many competitive programming problems can be reduced to network flow and other graph problems, so the convexity of their value functions can be established in a similar way.

Using this method, we obtain the first convexity proof for the tree planting problem:

??? example "Convexity proof 1"
    The maximum profit of the tree planting problem can actually be obtained from the following maximum-cost maximum-flow model:
    
    -   from the source $s$, add an edge to node $r$ with capacity $m$ and cost $0$;
    -   from node $r$, add an edge to every odd node $i=1,3,\cdots,2\lceil n/2\rceil-1$ with capacity $1$ and cost $0$;
    -   from every even node $i=0,2,\cdots,2\lfloor n/2\rfloor$, add an edge to the sink $t$ with capacity $1$ and cost $0$;
    -   for every $i=1,\cdots,n$, add an edge from the odd one of the nodes $i-1$ and $i$ to the even one, with capacity $1$ and cost $a_i$.
    
    The final answer is the maximum cost obtained. Converting this graph model into the corresponding linear program (see the proof of the corollary above), the total flow $m$ appears in the inequality bounding the flow on edge $(s,r)$. By the corollary, the maximum cost $v(m)$ is a concave function of the flow $m$.
    
    Using this flow model, the problem can be solved in $O(n\log n)$ by simulating the cost flow or by [greedy with regret](../../basic/greedy.md#regret-solutions).

### Using the state transition equation

Although the state transition equation does not provide an efficient way of computing, it can often be used to prove that the state function $f(i,j)$ is convex in the parameter $j$. Concretely, viewing the function $f(i,\cdot)$ as the state at $i$, the transition equation for $f(i,j)$ can be seen as a recurrence for $f(i,\cdot)$, so that one can prove inductively that every $f(i,\cdot)$ is convex. This kind of convexity proof is more common in the setting of [Slope Trick DP optimization](./slope-trick.md), and that page also discusses common convexity-preserving transformations.

This method can also be used to prove the convexity of the tree planting problem:

??? example "Convexity proof 2"
    Let $f(i,j)$ be the maximum profit when planting $j$ trees in the first $i$ pits. Consider the following transition equation:
    
    $$
    f(i,j) = \max\{f(i-1,j),f(i-2,j-1)+a_i\}.
    $$
    
    View this transition equation as a recurrence for the function $f(i,\cdot)$. Since two different functions appear inside the maximum, it cannot be expressed as a supremal convolution. Nevertheless, one can still prove inductively that the function $f(i,\cdot)$ is concave.
    
    In fact, we need to prove inductively the following two statements:
    
    -   $f(i,j)-f(i-2,j-1)$ is decreasing in $j$;
    -   $f(i,j)-f(i-1,j)$ is increasing in $j$.
    
    The base case is trivial. Suppose they hold for all natural numbers up to and including $i-1$; we now prove them for $i$. Direct verification suffices.
    
    First, by the induction hypothesis,
    
    $$
    f(i-1,j) - f(i-2,j-1) = (f(i-1,j)-f(i-3,j-1)) - (f(i-2,j-1)-f(i-3,j-1))
    $$
    
    is decreasing in $j$. Therefore,
    
    $$
    f(i,j) - f(i-2,j-1) = \max\{f(i-1,j) - f(i-2,j-1), a_i\}
    $$
    
    is decreasing in $j$, and
    
    $$
    f(i,j) - f(i-1,j) = \max\{0,a_i-(f(i-1,j) - f(i-2,j-1))\}
    $$
    
    is increasing in $j$. This completes the induction.
    
    Furthermore,
    
    $$
    f(i,j) - f(i,j-1) = (f(i,j)-f(i-2,j-1)) - (f(i,j-1) - f(i-1,j-1)) - (f(i-1,j-1) - f(i-2,j-1))
    $$
    
    is decreasing in $j$. This shows that $f(i,j)$ is a concave function of $j$, so the value function $v(m)=f(n,m)$ is a concave function of $m$.
    
    A by-product of this proof is that for every $i$ there exists $p_i$ such that
    
    $$
    f(i,j) =
    \begin{cases}
    f(i-1,j), & j\le p_i,\\
    f(i-2,j-1) + a_i, & j> p_i.
    \end{cases}
    $$
    
    This means the sequence $f(i,\cdot)$ can be maintained directly with a balanced tree in $O(n\log^2n)$. The advantage is that the general case of an arbitrary planting gap can be handled, and all values of $v(m)$ are obtained at once.

### Quadrangle inequality

Another common class of problems with convexity in competitive programming is [interval partition problems](./quadrangle.md#区间分拆问题). That page proves that if the cost function of a single interval satisfies the quadrangle inequality, then the minimum cost of the interval partition problem with a constrained number of intervals is a convex function of the number of intervals. That page also provides some ways to decide whether a function $w(l,r)$ satisfies the quadrangle inequality. The most direct way is to compute its second-order mixed difference:

$$
\begin{aligned}
\Delta_l \Delta_r w(l,r) &= \Delta_l(w(l,r+1)-w(l,r)) \\
&= w(l+1,r+1)-w(l+1,r)-w(l,r+1)+w(l,r).
\end{aligned}
$$

The function $w(l,r)$ satisfies the quadrangle inequality if and only if $\Delta_l \Delta_r w(l,r)$ is non-positive. Intuitively, a function satisfying the quadrangle inequality usually means that extending the interval on both sides — i.e. moving the left endpoint left and the right endpoint right — has some synergistic effect.

The tree planting problem can also be viewed as an interval partition problem and proved by verifying the quadrangle inequality.

??? example "Convexity proof 3"
    Prepend an $a_0$, which can be any value, to the profit sequence. Then the tree planting problem is equivalent to the interval partition problem of splitting the sequence $\{a_0,a_1,\cdots,a_n\}$ into $m$ segments, where the profit function of each segment is
    
    $$
    w(l,r) = \max_{i\in[l+1,r]} a_i
    $$
    
    That is, the profit of each segment is the maximum profit among all trees except the first one — this guarantees the planting gap.
    
    Since this is a maximization problem, we need to verify "crossing is greater than nesting", i.e. for any $a<b<c<d$,
    
    $$
    w(a,c)+w(b,d) \ge w(a,d)+w(b,c).
    $$
    
    Substituting the expression of the profit function and setting
    
    $$
    A = \max_{i\in[a+1,b]} a_i,~ B = \max_{i\in[b+1,c]} a_i,~ C = \max_{i\in[c+1,d]}a_i,
    $$
    
    the inequality to be proved can be written as
    
    $$
    \max\{A,B\} + \max\{B,C\} \ge \max\{A,B,C\} + B.
    $$
    
    Note that the larger of the two terms $\max\{A,B\}$ and $\max\{B,C\}$ on the left-hand side equals $\max\{A,B,C\}$, while the smaller of them is always at least $B$, so the inequality holds.
    
    After converting the tree planting problem into an interval partition problem, we only need to preprocess range maxima with a sparse table or the like so that the cost of a single interval can be computed in $O(1)$, and then apply the algorithms for interval partition problems to solve it in $O(n\log n\log L)$ or $O(n(n+m))$ time. This method can also handle an arbitrary planting gap.

### Exchange argument

In combinatorial optimization, proving the convexity of the value function often uses an exchange argument. Concretely, starting from the optimal solutions of the problems with parameters $m-1$ and $m+1$, one constructs, by exchanging some elements, a feasible solution with parameter $m$ whose value does not exceed $(v(m-1)+v(m+1))/2$, and then uses the optimality of $v(m)$ to prove convexity. Compared with the convex optimization setting, in combinatorial optimization there is no natural way to construct an "intermediate form" of two solutions, so applying an exchange argument usually requires some ingenuity.

???+ warning ""Increasing marginal cost" does not necessarily imply convexity"
    In combinatorial optimization, objective functions often have some "increasing marginal cost" property, but this does not necessarily imply convexity. A typical example is [\[IOI 2005\] Riv – Rivers](https://www.luogu.com.cn/problem/P3354): the chain version of this problem satisfies the quadrangle inequality and is therefore convex, but the tree version has instances where convexity fails.
    
    A common property used to characterize "increasing marginal cost" is supermodularity. For a function $f:\mathcal PX\rightarrow\mathbf R$ on the family $\mathcal PX$ of subsets of a finite set $X$, if it satisfies one of the following two equivalent properties:
    
    1.  (crossing is less than nesting) for any subsets $A,B\subseteq X$, $f(A)+f(B) \le f(A\cup B) + f(A\cap B)$;
    2.  (increasing marginal cost) for any subsets $A\subseteq B\subseteq X$ and $x\in X\setminus B$, $f(A\cup\{x\})-f(A)\le f(B\cup\{x\})-f(B)$;
    
    then $f$ is called **supermodular**. However, in an optimization problem with a supermodular objective, the value function
    
    $$
    v(m) = \min_{A\subseteq X} f(A) \text{ subject to }|A|=m
    $$
    
    is **not necessarily** a convex function of $m$. The reason is that from optimal solutions with subset sizes $m-1$ and $m+1$ one generally cannot construct a feasible solution of subset size $m$ satisfying the value relation above.

The exchange argument provides yet another proof of the convexity of the tree planting problem.

??? example "Convexity proof 4"
    We use an exchange argument. Let the optimal plans for planting $m-1$ and $m+1$ trees be given by $\{x_i^{(m-1)}\}\in\{0,1\}^n$ and $\{x_i^{(m+1)}\}\in\{0,1\}^n$ respectively, where a value of $1$ means a tree is planted in that pit and $0$ means no tree is planted. Define the sequence $\{z_i\}\in\{0,\pm 1\}^n$ by
    
    $$
    z_i = x_i^{(m+1)} - x_i^{(m-1)},~i=1,\cdots,n.
    $$
    
    This sequence marks the differences between the two plans. Positions with value $0$ mean that the pit either has a tree in both plans or in neither; positions with value $-1$ and $+1$ mean that a tree is planted in that pit only in plan $x^{(m-1)}$ or only in plan $x^{(m+1)}$, respectively. Since no plan may plant trees in adjacent pits, we have the following observations:
    
    -   within a contiguous non-zero segment, the values $z_i$ must alternate between $\pm 1$;
    -   the $0$s on the left and right of a maximal contiguous non-zero segment must mean that no tree is planted there in either plan.
    
    Therefore, if in some maximal contiguous non-zero segment the sum of $z_i$ is exactly $+1$, i.e. in that stretch of pits plan $x^{(m+1)}$ plants one more tree than plan $x^{(m-1)}$, we can swap the planting positions of the two plans within that segment. This yields two feasible plans each planting $m$ trees. Since we did not change the overall planting positions and counts of the two plans but merely redistributed them, the total profit is unchanged and still equals $v(m-1)+v(m+1)$. However, these two plans with $m$ trees need not be optimal, so each of their profits does not exceed $v(m)$. This proves
    
    $$
    v(m-1) + v(m+1) \le 2v(m),
    $$
    
    i.e. $v(m)$ is a concave function of $m$.
    
    Now only one question remains: whether a maximal contiguous non-zero segment with sum exactly $+1$ exists. Since it is a sum of alternating $\pm 1$s, the sum of a contiguous non-zero segment can only be $0$ or $\pm 1$. And since the sums of all these maximal contiguous non-zero segments add up to $2$, there must be at least two maximal contiguous non-zero segments with sum exactly $+1$. This completes the proof.

## Example problems

This section presents several example problems applying WQS binary search in different settings.

### Template problems

???+ example "[Luogu P1484 Tree planting](https://www.luogu.com.cn/problem/P1484)"
    There are $n$ pits and **at most** $m$ trees are to be planted. Trees cannot be planted in two adjacent pits. A sequence $\{a_i\}$ of length $n$ is given, representing the profit of planting a tree in each pit; the profit may be positive or negative. Find the maximum possible total profit.

??? note "Solution"
    Slightly different from the tree planting problem discussed earlier, this problem asks for at most $m$ trees rather than exactly $m$. Still letting $v(m)$ denote the value function of the problem discussed earlier, the answer to this problem is actually $\tilde v(m)=\max_{k\le m}v(k)$. Since $v(m)$ is concave, i.e. unimodal, the answer amounts to keeping only the part of $v(m)$ rising to the peak, after which the function stays at the peak; this is equivalent to keeping only the part where the tangent slope is non-negative. Therefore, the only difference from the problem discussed earlier is that the initial slope range in the WQS binary search is $[0,\max_ia_i]$ rather than $[\min_ia_i,\max_ia_i]$.
    
    After removing the cardinality constraint with WQS binary search, the problem becomes computing a maximum-weight independent set on a chain, except that the original profits $\{a_i\}$ are replaced by $\{a_i+k\}$. This is a classic dynamic programming problem. Let $f(i,j)$ be the maximum profit of the subproblem on the first $i$ pits when a tree is planted ($j=1$) or not planted ($j=0$) in pit $i$. The transition equation is then
    
    $$
    \begin{aligned}
    f(i,0) &= \max\{f(i-1,0),f(i-1,1)\},\\
    f(i,1) &= f(i-1,0) + a_i + k.
    \end{aligned}
    $$
    
    The initial conditions are $f(0,0)=0$ and $f(0,1)=-\infty$, and the final answer is $\max\{f(n,0),f(n,1)\}$. A single computation takes $O(n)$, and the overall time complexity is $O(n\log L)$, where $L=\max_i|a_i|$.
    
    Reference implementation:
    
    === "Traditional method"
        ```cpp
        --8<-- "docs/dp/code/opt/wqs-binary-search/plant-tree-1.cpp"
        ```
    
    === "Dual method"
        ```cpp
        --8<-- "docs/dp/code/opt/wqs-binary-search/plant-tree-2.cpp"
        ```

???+ example "[Luogu P2619 \[National Training Team\] Tree I](https://www.luogu.com.cn/problem/P2619)"
    Given a weighted undirected connected graph in which every edge is black or white, find the minimum weight of a spanning tree with exactly $m$ white edges.

??? note "Solution"
    First, an exchange argument shows that $v(m)$ is convex. Without loss of generality, assume all edge weights are distinct: cases with two equal edge weights can be perturbed slightly into cases with distinct weights; then, letting the magnitude of the perturbation tend to zero, one shows that convexity still holds in the limiting case — i.e. when two edges have equal weight. The key to the proof is the following lemma:[^edge-swap]
    
    ???+ note "Lemma"
        Let $S$ and $T$ be two spanning trees of an undirected connected graph $G=(V,E)$. For any $e\in S\setminus T$, there exists at least one edge $f\in T\setminus S$ such that both $S-e+f$ and $T-f+e$ are spanning trees of $G$.
    
    ??? note "Proof"
        Let $e=(u,v)$ and let $P$ be the unique path in tree $T$ connecting $u$ and $v$. Since $P+e$ is the unique cycle in the graph $T+e$, deleting any edge $f$ of $P$ makes $T-f+e$ a spanning tree. Meanwhile, the graph $S-e$ is a forest with two connected components, whose vertex sets we denote $V_1$ and $V_2$; so choosing an edge $f\in P$ such that $f$ connects $V_1$ and $V_2$ guarantees that $S-e+f$ is a spanning tree. Such an edge $f$ always exists, because $u$ and $v$ belong to $V_1$ and $V_2$ respectively and $P$ connects $u$ and $v$. Moreover, $f\notin S$, because in the graph $S-e$ the sets $V_1$ and $V_2$ are not connected. This completes the proof.
    
    Let $T_{m-1}$ and $T_{m+1}$ be minimum spanning trees with $m-1$ and $m+1$ white edges respectively. Let $e$ be a white edge in $T_{m+1}\setminus T_{m-1}$; applying the lemma above, there exists an edge $f\in T_{m-1}\setminus T_{m+1}$ such that $T'=T_{m+1}-e+f$ and $T''=T_{m-1}+e-f$ are both spanning trees. Since only one pair of edges was exchanged, the total weight of trees $T'$ and $T''$ is still $v(m-1)+v(m+1)$. We then distinguish two cases:
    
    -   if $f$ is a black edge, then $T'$ and $T''$ both have $m$ white edges. Each of their weights is at least $v(m)$. This proves $2v(m)\le v(m-1)+v(m+1)$, so $v(m)$ is convex in $m$;
    -   if $f$ is a white edge, then $T'$ and $T''$ have $m+1$ and $m-1$ white edges respectively, so their weights are at least $v(m+1)$ and $v(m-1)$ respectively. But we showed above that their weights add up to exactly $v(m-1)+v(m+1)$. This means the weight of $T'$ equals $v(m+1)$. Comparing $T'$ with $T_{m+1}$, the weights of $e$ and $f$ must be equal. This contradicts the assumption, so this case cannot occur.
    
    This proves that $v(m)$ is a convex function of $m$.
    
    Having established the convexity of $v(m)$, the problem can be solved with WQS binary search. Remove the cardinality constraint, subtract $k$ from the weight of every white edge, and solve the minimum spanning tree problem. For this we can apply [Kruskal's algorithm](../../graph/mst.md#kruskal-算法). Maintaining connectivity with a disjoint-set union, the complexity of the algorithm is $O(E\log E+E\alpha(V))$, where $E$ and $V$ are the numbers of edges and vertices and $\alpha(\cdot)$ is the inverse Ackermann function. The main part of the complexity, $O(E\log E)$, is for sorting the edges, which can be further optimized in this problem. Although the minimum spanning tree has to be computed many times during the WQS binary search, each time only the weights of the white edges are shifted by the same amount. So we can sort the white and black edges separately in preprocessing, and then, each time we compute the minimum spanning tree, simply merge the white edges with adjusted weights and the black edges. This reduces the overall complexity to $O(E\log E+E\alpha(V)\log L)$, where $L$ is the length of the range of edge weights.
    
    Reference implementation:
    
    === "Traditional method"
        ```cpp
        --8<-- "docs/dp/code/opt/wqs-binary-search/black-white-mst-1.cpp"
        ```
    
    === "Dual method"
        ```cpp
        --8<-- "docs/dp/code/opt/wqs-binary-search/black-white-mst-2.cpp"
        ```

### Interval partition problems

???+ example "[Luogu P6246 \[IOI 2000\] Post Offices, strengthened version, strengthened version](https://www.luogu.com.cn/problem/P6246)"
    Given an increasing sequence of positive integers $\{a_i\}$ of length $n$ representing the positions of $n$ villages along a highway, $m$ post offices must be built. The positions of the post offices must minimize the sum of the distances from every village to its nearest post office. Find this minimum.

??? note "Solution"
    This is a typical [interval partition problem](./quadrangle.md#区间分拆问题). Please refer to that page for the implementation details of the binary-search queue.
    
    Each post office serves the villages nearest to it, and these villages must be consecutive villages along the highway. So building $m$ post offices amounts to partitioning all villages into $m$ consecutive segments and building the cheapest post office for each segment. It is well known that the post office should be built at the median of the village positions. Thus the cost function of the interval $[l,r]$ is
    
    $$
    w(l,r) = \sum_{i=l}^r|a_i-a_{\lfloor(l+r)/2\rfloor}|.
    $$
    
    It satisfies the quadrangle inequality because its second-order mixed difference is non-positive:
    
    $$
    \Delta_l\Delta_r w(l,r)
    = \Delta_l(a_{r+1} - a_{\lfloor(l+r+1)/2\rfloor})
    = a_{\lfloor(l+r+1)/2\rfloor}-a_{\lfloor(l+r+2)/2\rfloor} \le 0.
    $$
    
    This shows that the problem can be solved with a binary-search queue combined with WQS binary search in $O(n\log n\log L)$.
    
    Reference implementation:
    
    === "Traditional method"
        ```cpp
        --8<-- "docs/dp/code/opt/wqs-binary-search/post-office-1.cpp"
        ```
    
    === "Dual method"
        ```cpp
        --8<-- "docs/dp/code/opt/wqs-binary-search/post-office-2.cpp"
        ```

### Two-dimensional constraints

???+ example "[Codeforces 739 E. Gosha is hunting](https://codeforces.com/problemset/problem/739/E)"
    There are $n$ Pokémon; the sequences $\{p_i\}$ and $\{q_i\}$ give the probabilities of catching the $i$-th Pokémon with a Poké Ball and an Ultra Ball, respectively. At one Pokémon you may throw one Poké Ball, or one Ultra Ball, or one of each, or nothing. There are $m_1$ Poké Balls and $m_2$ Ultra Balls, which must be allocated sensibly and thrown simultaneously. Find the maximum expected number of Pokémon caught. Whether a single catch succeeds is independent of the outcomes of the other catches.
    
    More generally, this can be abstracted as the following problem:
    
    Given three sequences of positive reals $\{A_i\},\{B_i\},\{C_i\}$ of length $n$, with $C_i\le A_i+B_i$ for all $i=1,\cdots,n$, find optimal index sets $X$ and $Y$ with $|X|=m_1$ and $|Y|=m_2$ maximizing
    
    $$
    \sum_{i\in X\setminus Y}A_i + \sum_{i\in Y\setminus X}B_i + \sum_{i\in X\cap Y}C_i.
    $$

??? note "Solution"
    The original problem can be viewed as the special case of this more general problem with
    
    $$
    A_i = p_i,~ B_i = q_i,~ C_i = p_i+q_i-p_iq_i
    $$
    
    Therefore, it suffices to discuss the solution of the more general problem.
    
    Let $v(m_1,m_2)$ denote the value function of this problem; we need to prove that it is a concave function of $(m_1,m_2)$. Consider the following cost flow model:
    
    -   from the source $s$, add an edge to each of the nodes $x$ and $y$, with capacities $m_1$ and $m_2$ respectively and cost $0$;
    -   for all $i=1,\cdots,n$, add an edge from each of the nodes $x$ and $y$ to node $i$, with capacity $1$ and costs $A_i$ and $B_i$ respectively;
    -   for all $i=1,\cdots,n$, add two edges from node $i$ to the sink $t$, both with capacity $1$ and with costs $0$ and $C_i-A_i-B_i$ respectively.
    
    The answer to the problem is the maximum-cost maximum flow of this model. The condition $C_i-A_i-B_i\le 0$ guarantees that when the flow through node $i$ is $1$, the outgoing edge with cost $0$ is chosen first. Writing this flow model as a linear program, $m_1$ and $m_2$ appear in the inequalities bounding the flow on edges $(s,x)$ and $(s,y)$ respectively. Therefore, $v(m_1,m_2)$ is indeed a concave function of $(m_1,m_2)$.
    
    To apply WQS binary search, consider the optimization problem with the cardinality constraints removed. Let $k_1$ and $k_2$ be the extra rewards obtained when putting an index into set $X$ and $Y$ respectively. Without the cardinality constraints, the decision for each index is independent, so
    
    $$
    h(k_1,k_2) = \sum_{i=1}^n\max\{0,A_i+k_1,B_i+k_2,C_i+k_1+k_2\}.
    $$
    
    The answer to the original problem is given by
    
    $$
    v(m_1,m_2) = \min_{k_1,k_2} h(k_1,k_2) - k_1m_1 - k_2m_2
    $$
    
    The total time complexity is $O(n\log^2L)$, where $O(\log L)$ is the number of binary search steps in one dimension.
    
    Reference implementation for the Pokémon catching problem:
    
    ```cpp
    --8<-- "docs/dp/code/opt/wqs-binary-search/gosha-is-hunting.cpp"
    ```

### More general constraints

???+ example "[Codeforces 1661 F. Teleporters](https://codeforces.com/problemset/problem/1661/F)"
    There are $n$ segments whose lengths are given by the sequence $\{a_i\}$. They may be cut arbitrarily into segments of integer length, and the goal is to minimize the sum of the squares of all segment lengths. Find the minimum number of cuts needed so that this sum of squares does not exceed $V$.

??? note "Solution"
    Let $f(a,m)$ be the minimum sum of squares obtainable by cutting a segment of length $a$ $m$ times. By the AM–QM inequality, when the sum of two numbers is fixed, the smaller their difference, the smaller the sum of their squares. So the more uniform the lengths of the resulting segments, the smaller the total sum of squared lengths. However, because of the integrality constraint, the most uniform case is obtaining $a\bmod (m+1)$ segments of length $\lceil a/(m+1)\rceil$ and $m+1-(a\bmod (m+1))$ segments of length $\lfloor a/(m+1)\rfloor$. Hence we have the following expression:
    
    $$
    \begin{aligned}
    f(a,m) &= (a\bmod (m+1))\left\lceil\dfrac{a}{m+1}\right\rceil^2 + (m+1-(a\bmod (m+1)))\left\lfloor\dfrac{a}{m+1}\right\rfloor^2 \\
    &= (a\bmod (m+1))\left(\left\lfloor\dfrac{a}{m+1}\right\rfloor+1\right)^2 + (m+1-(a\bmod (m+1)))\left\lfloor\dfrac{a}{m+1}\right\rfloor^2.
    \end{aligned}
    $$
    
    The second equality holds because $\lceil a/(m+1)\rceil \neq \lfloor a/(m+1)\rfloor + 1$ if and only if $a\bmod (m+1) = 0$.
    
    One can prove that the function $f(a,m)$ is convex in $m$. For this, we need to extend it to $m\in\mathbf R_{+}$. When $\lfloor a/(m+1)\rfloor = q$, we have
    
    $$
    \begin{aligned}
    f(a,m) &= (a-(m+1)q)(q+1)^2 + ((m+1)(q+1)-a)q^2 \\
    &= a(2q+1) - q(q+1)(m+1).
    \end{aligned}
    $$
    
    This is a line with slope $-q(q+1)$. Therefore, $f(a,m)$ is a piecewise linear function whose slope increases as $m$ increases. This shows that $f(a,m)$ is convex, and of course its restriction to integer points is also convex[^conv-int].
    
    Using $f(\cdot,\cdot)$, the minimum sum of squares when all segments are cut $m$ times in total can be written as the value function of the following optimization problem:
    
    $$
    v(m) = \min_{\{m_i\}}\sum_i f(a_i,m_i)\text{ subject to }\sum_i m_i=m,~m_i\in\mathbf N.
    $$
    
    This is the [infimal convolution](./slope-trick.md#卷积下确界minkowski-和) of several convex functions, so it is also convex. If the problem asked for $v(m)$, it could be solved with the same method as the previous examples in $O(n\log^2L)$ time; but this problem asks for the smallest $m$ with $v(m)\le V$. Computing $v(m)$ by WQS binary search and then binary searching on $m$ does not work, since its complexity reaches $O(n\log^3L)$. For this problem, there are the following two approaches.
    
    **Method 1**: still binary search on the slope $k$, but base the search on estimates of lower and upper bounds for $v(m)$.
    
    In the traditional WQS binary search method, for a given slope $k$ one can compute the range of the corresponding optimal values of $m$. Since these $(m,v(m))$ are collinear, this amounts to determining the range of $v(m)$. Therefore, we can binary search directly on the slope $k$. After obtaining the slope $k$, we can use the line equation
    
    $$
    v(m) = h(k) + km
    $$
    
    to compute the smallest $m$. The overall complexity is $O(n\log^2L)$.
    
    To determine the range of $v(m)$, we need to determine the range of $m$. One approach is to record the largest optimal solution when computing $h(k)$ and use it to compute a lower bound on the corresponding $v(m)$; another is to use $h(k)-h(k-1)$ to obtain an upper bound on the corresponding $m$, and thus a lower bound on the corresponding $v(m)$. The reference implementation uses the second approach, which does not depend on the specific structure of the problem and needs no special handling.
    
    **Method 2**: rewrite the optimization problem so that the value function of the dual problem is exactly the solution of this problem.
    
    This problem can be viewed directly as the following optimization problem:
    
    $$
    m(V) = \min_{\{m_i\}} \sum_i m_i \text{ subject to }\sum_i f(a_i,m_i) \le V.
    $$
    
    The analysis in this article still applies to this problem. Hence, the desired $m(V)$ can be computed using its dual problem:
    
    $$
    m(V) = \max_{\lambda} \sum_i\min_{m_i}(m_i - \lambda f(a_i,m_i)) + \lambda V.
    $$
    
    The overall complexity of the algorithm is still $O(n\log^2L)$.
    
    Reference code:
    
    === "Method 1"
        The code is for illustration only; to pass the constraints of the original problem, 128-bit integers are needed and the initial binary search interval must be adjusted to $[0,10^{60}]$.
        
        ```cpp
        --8<-- "docs/dp/code/opt/wqs-binary-search/teleporters-1.cpp"
        ```
    
    === "Method 2"
        The code is for illustration only; due to floating-point precision issues it cannot pass the constraints of the original problem.
        
        ```cpp
        --8<-- "docs/dp/code/opt/wqs-binary-search/teleporters-2.cpp"
        ```

## Exercises

Finally, here are some problems that can be solved with WQS binary search, for practice:

-   [Luogu P1484 Tree planting](https://www.luogu.com.cn/problem/P1484)
-   [Luogu P1792 \[National Training Team\] Tree planting](https://www.luogu.com.cn/problem/P1792)
-   [Luogu P2619 \[National Training Team\] Tree I](https://www.luogu.com.cn/problem/P2619)
-   [Luogu P3620 \[APIO/CTSC2007\] Data Backup](https://www.luogu.com.cn/problem/P3620)
-   [Luogu P4072 \[SDOI2016\] Expedition](https://www.luogu.com.cn/problem/P4072)
-   [Luogu P4383 \[Eight Provinces Joint Selection 2018\] Link-Cut Tree](https://www.luogu.com.cn/problem/P4383)
-   [Luogu P4983 Forgetting](https://www.luogu.com.cn/problem/P4983)
-   [Luogu P5308 \[COCI 2018/2019 #4\] Akvizna](https://www.luogu.com.cn/problem/P5308)
-   [Luogu P5633 Minimum degree-constrained spanning tree](https://www.luogu.com.cn/problem/P5633)
-   [Luogu P5896 \[IOI 2016\] aliens](https://www.luogu.com.cn/problem/P5896)
-   [Luogu P6246 \[IOI 2000\] Post Offices, strengthened version, strengthened version](https://www.luogu.com.cn/problem/P6246)
-   [AtCoder Beginner Contest 218 H - Red and Blue Lamps](https://atcoder.jp/contests/abc218/tasks/abc218_h)
-   [AtCoder Beginner Contest 305 Ex - Shojin](https://atcoder.jp/contests/abc305/tasks/abc305_h)
-   [AtCoder Regular Contest 164 E - Segment-Tree Optimization](https://atcoder.jp/contests/arc164/tasks/arc164_e)
-   [Codeforces 125 E. MST Company](https://codeforces.com/problemset/problem/125/E)
-   [Codeforces 321 E. Ciel and Gondolas](https://codeforces.com/problemset/problem/321/E)
-   [Codeforces 739 E. Gosha is hunting](https://codeforces.com/problemset/problem/739/E)
-   [Codeforces 802 O. April Fools' Problem (hard)](https://codeforces.com/contest/802/problem/O)
-   [Codeforces 958 E2. Guard Duty (medium)](https://codeforces.com/problemset/problem/958/E2)
-   [Codeforces 1279 F. New Year and Handle Change](https://codeforces.com/problemset/problem/1279/F)
-   [Codeforces 1661 F. Teleporters](https://codeforces.com/problemset/problem/1661/F)
-   [Codeforces 1799 F. Halve or Subtract](https://codeforces.com/problemset/problem/1799/F)
-   [2019 Summer Petrozavodsk Camp H. Honorable Mention](https://codeforces.com/gym/102331/problem/H)

## References and notes

-   [Wang Qinshi, "浅析一类二分方法" (A brief analysis of a class of binary search methods)](https://github.com/hzwer/shareOI/blob/master/%E5%9F%BA%E7%A1%80%E7%AE%97%E6%B3%95/%E6%B5%85%E6%9E%90%E4%B8%80%E7%B1%BB%E4%BA%8C%E5%88%86%E6%96%B9%E6%B3%95_%E7%8E%8B%E9%92%A6%E7%9F%B3.pdf)
-   [Theoretical grounds of lambda optimization by adamant - Codeforces blog](https://codeforces.com/blog/entry/98334)
-   [A rigorous WQS binary search method by YeahPotato - Luogu blog](https://www.luogu.com.cn/article/vsffwrc3)
-   [Study notes: a detailed explanation of WQS binary search and common misconceptions by ikrvxt - CSDN blog](https://blog.csdn.net/Emm_Titan/article/details/124035796)
-   [Convex conjugate - Wikipedia](https://en.wikipedia.org/wiki/Convex_conjugate)
-   [Fenchel–Moreau theorem - Wikipedia](https://en.wikipedia.org/wiki/Fenchel%E2%80%93Moreau_theorem)
-   [Subderivative - Wikipedia](https://en.wikipedia.org/wiki/Subderivative)
-   [Boyd, Stephen P., and Lieven Vandenberghe. Convex optimization. Cambridge university press, 2004.](https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf)
-   Papadimitriou, Christos H., and Kenneth Steiglitz. Combinatorial optimization: algorithms and complexity. Courier Corporation, 1998.
-   Conforti, Michele, Gérard Cornuéjols, and Giacomo Zambelli. Integer programming. Springer International Publishing, 2014.
-   Schrijver, Alexander. Combinatorial optimization: polyhedra and efficiency. Vol. 24, no. 2. Berlin: Springer, 2003.

[^high-d-convex]: In practical problems, $y$ may only take finitely many lattice points in $\mathbf R^d$. The condition actually needed here is that the solution $v(y)$ of the original problem can be extended to a convex function $\tilde v:\mathbf R^d\rightarrow \mathbf R\cup\{\pm\infty\}$ on $\mathbf R^d$, i.e. $v(y)$ is **convex-extensible**. For convenience, the main text still uses $v(y)$ to denote the extended function. Geometrically, this amounts to saying that all the points of the set $\{(y,v(y))\}$ lie on the lower convex hull of their convex hull. In the one-dimensional case, this condition is [easy to characterize](./slope-trick.md#离散点集上的凸函数) in algebraic terms; in higher dimensions it is slightly more complicated, and [these lecture notes](https://kzmurota.fpark.tmu.ac.jp/paper/HIMSummerSchool15Murota.pdf) provide some simple sufficient conditions.

[^other-conditions]: The conditions given in the theorem may look stronger than mere convexity, but for the situations encountered in competitive programming, especially when $X$ is a finite set, requiring only convexity is already enough. The function $\tilde v$ obtained by extending a proper convex function $v$ on a discrete set is necessarily a lower semi-continuous convex function, because the convex hull of finitely many points is a closed convex set, and a lower semi-continuous convex function is exactly one whose epigraph is a closed convex set. As for the word "proper" in "proper convex function", it is guaranteed as long as $v(y)$ is convex and takes a finite value at at least one point.

[^mst]: There are two common [ways](https://math.arizona.edu/~glickenstein/math443f14/golari.pdf) of writing the minimum spanning tree problem as a linear program: the subtour-elimination formulation and the cut-based formulation. Only the former guarantees that the resulting linear program is equivalent to the original problem.

[^edge-swap]: This lemma also holds for general [matroids](../../math/matroid.md). It is called the **symmetric base-exchange property**; see the [Wikipedia page](https://en.wikipedia.org/wiki/Basis_of_a_matroid). Therefore, the convexity conclusion of this problem can be generalized to general matroids.

[^conv-int]: Of course, the convex hulls of $f(a,m)$ and of its restriction to integer points are not the same, because $f(a,m)$ may have extreme points at non-integer positions. This shows that $f(a,m)$ with a real domain cannot be used directly in the optimization problem of this exercise.
