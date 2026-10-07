---
title: Slope Trick optimization
---

## Introduction

For a class of two-dimensional DP problems, if the value function $f(i,x)$ is a convex function of $x$ for every fixed $i$, then the whole function $f(i,\cdot)$ can be viewed as the state at $i$, and maintaining its difference (or slope)

$$
\Delta f(i,x) = f(i,x+1)-f(i,x)
$$

instead of the function itself often optimizes the transitions. This idea of optimizing DP is called Slope Trick.

???+ info "\"Slope\""
    Since the functions involved in most problems take values only at integer points, there is no essential difference between calling it the difference or the slope; following the term Slope Trick, this article consistently calls it the slope.

In concrete problems the slope may be maintained in different ways. If the range of the slope values is narrow, it is more convenient to maintain the points where the slope changes (i.e. the kinks); if the domain of the function is narrow, it may be more convenient to maintain the slope sequence itself. In more complex situations, it may be necessary to maintain both the slope of each segment and the length of that segment. Whatever the concrete way of maintenance, the essence of these problems is to use the fact that the slope sequence changes little during state transitions to simplify the transitions. Therefore they can all be called Slope Trick.

## Convex functions

Before discussing concrete problems, it is necessary to first understand the basic properties of convex functions and how their slopes change under various transformations of convex functions.

### Convex functions on the real line

The more general definition of a convex function is given on $\mathbf R$.

![](../images/slope-trick/epigraph-convex-def.svg)

???+ abstract "Convex function on $\mathbf R$"
    If a function $f:\mathbf R\rightarrow\mathbf R\cup\{\pm\infty\}$ satisfies, for all $x,y\in\mathbf R$ and $\alpha\in(0,1)$,
    
    $$
    f(\alpha x+(1-\alpha)y) \le \alpha f(x)+(1-\alpha)f(y),
    $$
    
    then $f$ is called a **convex function**; here the arithmetic rules for $\pm\infty$ are that $\pm\infty$ multiplied by any positive real number or plus any real number equals itself, and that $-\infty<x<+\infty$ for every real number $x\in\mathbf R$.

Of course, if the inequality sign is replaced by $\ge$, the function is correspondingly called concave[^convex-def]. Since for a concave function $f$, $-f$ is always convex, this section only considers convex functions.

???+ info "This article only considers proper convex functions"
    To avoid discussing the value of $\infty-\infty$ and additional complicated analysis, when discussing concepts related to convex functions this article always assumes that the function never takes the value $-\infty$ and is not identically $+\infty$. Such convex functions are called **proper convex functions**. This is sufficient for understanding the content involved in competitive programming.

Of course, a function $f$ is often not defined for all real numbers. If the domain of $f$ is only a subset of $\mathbf R$, it can be extended to a function on $\mathbf R$:

$$
\tilde f(x) = \begin{cases} f(x), & x\in\operatorname{dom}f,\\ +\infty,& x\notin\operatorname{dom}f.\end{cases}
$$

Then $f$ is called convex if and only if the corresponding $\tilde f$ satisfies the definition of a convex function above. Therefore, unless stated otherwise, the domain of the convex functions mentioned in this article is always the set of real numbers $\mathbf R$. Clearly, a convex function $f$ can take finite values only on an interval (i.e. a convex subset of $\mathbf R$).

???+ example "Simple examples"
    Common examples of convex functions include:
    
    1.  constant functions: $f(x)=c$, where $c\in\mathbf R$;
    2.  linear functions: $f(x)=kx+b$, where $k,b\in\mathbf R$ and $k\neq 0$;
    3.  the absolute value function: $f(x)=|x-a|$, where $a\in\mathbf R$;
    4.  the restriction of any convex function to some interval, e.g. $0_{[a,b]}(x)$ (in the context of convex analysis also called the indicator function of $[a,b]$).

Of course, more complex convex functions can be composed using the convexity-preserving transformations mentioned below.

### Convex functions on discrete point sets

In competitive programming, many functions are defined only at some integer values. In general they are not convex functions (as defined above), because their domain is no longer a convex set. To handle this situation, the convexity of functions on discrete point sets has to be defined separately. In short, the function first has to be linearly interpolated, extending its domain to an interval, and then its convexity is examined.

![](../images/slope-trick/epigraph-convex-discrete.svg)

???+ abstract "Convex function on a discrete point set"
    Let $S\subset\mathbf R$ be a discrete point set, i.e. for every closed interval $[a,b]$ the set $S\cap[a,b]$ is finite. For a function $f:S\rightarrow\mathbf R\cup\{\pm\infty\}$, define the function $\tilde f:\mathbf R\rightarrow\mathbf R\cup\{\pm\infty\}$ such that:
    
    -   for $x\in S$, $\tilde f(x)=f(x)$,
    -   for $x\in(\inf S,\sup S)\setminus S$, with $s_-=\max\{s\in S:s\le x\}$ and $s_+=\min\{s\in S:s\ge x\}$,
    
        $$
        \tilde f(x) = \dfrac{s_+-x}{s_+-s_-}f(s_-)+\dfrac{x-s_-}{s_+-s_-}f(s_+),
        $$
    -   for $x\notin[\inf S,\sup S]$, $\tilde f(x)=+\infty$.
    
    Then, if $\tilde f(x)$ is a convex function on $\mathbf R$, $f(x)$ is called a **convex function** on $S$.

Since convex functions on $\mathbf R$ are more convenient to handle, when this article mentions convex functions it means, unless stated otherwise, convex functions on $\mathbf R$. If a function in this article is given only by its values at some integer points, its values at the other real numbers are determined by the $\tilde f$ in the definition, which amounts to directly discussing the corresponding piecewise linear function $\tilde f$.

Convex functions on the integers $\mathbf Z$ have a more intuitive equivalent definition:

???+ note "Equivalent definition of a convex function on $\mathbf Z$"
    A function $f:\mathbf Z\rightarrow\mathbf R\cup\{\pm\infty\}$ is convex if and only if
    
    $$
    f(x)-f(x-1)\le f(x+1)-f(x)
    $$
    
    holds for all $x\in\mathbf Z$.

??? note "Proof"
    This statement is a simple corollary of the slope characterization of convex functions.
    
    If $f$ is a convex function on $\mathbf Z$, then, since the slope is weakly increasing,
    
    $$
    \Delta f(x-1,x)\le \Delta f(x-1,x+1) \le\Delta f(x,x+1).
    $$
    
    This is exactly the condition above.
    
    Conversely, if the condition above holds, then for any $x_1<x_2$,
    
    $$
    \Delta f(x_1,x_2) = \dfrac{1}{x_2-x_1}\sum_{i=x_1}^{x_2-1}\left(f(i+1)-f(i)\right).
    $$
    
    This is the arithmetic mean of all differences with $x_1\le i<x_2$. Increasing $x_2$ by one amounts to inserting a larger difference; increasing $x_1$ by one amounts to removing the smallest difference. Both operations make the mean weakly increase. This shows that the slope $\Delta f(x_1,x_2)$ is weakly increasing, i.e. $f$ is a convex function on $\mathbf Z$.

In other words, as long as the slope (difference) is monotonically non-decreasing, the sequence can be regarded as a convex function on $\mathbf Z$.

### Two characterizations of convex functions

In fact, the way of characterizing convex functions by slopes can be generalized to the general case.

???+ note "Slope characterization of convex functions"
    Let $S$ be $\mathbf R$ or a discrete subset of it. A function $f:S\rightarrow\mathbf R\cup\{\pm\infty\}$ is convex if and only if the slope
    
    $$
    \Delta f(x_1,x_2) = \dfrac{f(x_2)-f(x_1)}{x_2-x_1}
    $$
    
    is a weakly increasing function of $x_1$ and of $x_2$ for all $x_1,x_2\in S$ with $x_1<x_2$.

??? note "Proof"
    For a function $f(x)$ on $\mathbf R$ and $x_1<x_2$, and for $\alpha\in(0,1)$, let $x_3=\alpha x_1+(1-\alpha)x_2$; then
    
    $$
    \Delta f(x_1,x_3) \le \Delta f(x_1,x_2) \le \Delta f(x_3,x_2)
    $$
    
    is equivalent to
    
    $$
    \dfrac{f(x_3)-f(x_1)}{1-\alpha} \le f(x_2)-f(x_1) \le \dfrac{f(x_2)-f(x_3)}{\alpha}.
    $$
    
    Both inequalities are equivalent to $f(x_3)\le\alpha f(x_1)+(1-\alpha)f(x_2)$, i.e. to the convexity of $f(x)$.
    
    For a function $f(x)$ on a discrete subset $S$ of $\mathbf R$, the necessity of the weakly increasing slope condition follows from the convexity of $\tilde f(x)$. We now prove its sufficiency, for which it suffices to show that $\Delta\tilde f(x_1,x_2)$ is also weakly increasing. Let $S=\{s_i\}$ with $s_i$ strictly increasing in $i$, and let $s_{i_1}\le x_1\le s_{i_1+1}$ and $s_{i_2}\le x_2\le s_{i_2+1}$; naturally $i_1\le i_2$. Let $\Delta_i=\Delta f(s_i,s_{i+1})$; then one can prove $\Delta_{i_1}\le\Delta\tilde f(x_1,x_2)\le\Delta_{i_2}$.
    
    There are two cases. If $i_1=i_2$, then $\Delta_{i_1}=\Delta\tilde f(x_1,x_2)=\Delta_{i_2}$ and the inequality clearly holds. Otherwise,
    
    $$
    \Delta\tilde f(x_1,x_2) = \dfrac{1}{x_2-x_1}\left((s_{i_1+1}-x_1)\Delta_{i_1}+(x_2-s_{i_2})\Delta_{i_2}+\sum_{j=i_1+1}^{i_2-1}(s_{j+1}-s_j)\Delta_j\right).
    $$
    
    Since the slope is increasing on $S$, $\Delta_i$ is increasing in $i$, so $\Delta_{i_1}\le\Delta\tilde f(x_1,x_2)\le\Delta_{i_2}$.
    
    Using this conclusion, for $x_1<x_2$ and $\alpha\in(0,1)$ let $x_3=\alpha x_1+(1-\alpha)x_2$ and take $i_3$ such that $s_{i_3}\le x_3\le s_{i_3+1}$; then
    
    $$
    \Delta\tilde f(x_1,x_3) \le \Delta_{i_3} \le \Delta\tilde f(x_3,x_2).
    $$
    
    Substituting the expression for $x_3$ gives the convexity of $\tilde f(x)$.

A monotonically non-decreasing slope can be regarded as an equivalent definition of a convex function. Precisely because the slope of a convex function is monotonic, when maintaining slopes one usually chooses data structures such as a [heap (priority queue)](../../ds/heap.md) or a [balanced tree](../../ds/bst.md).

This article will also use another equivalent characterization of convex functions. For a function $f:\mathbf R\rightarrow\mathbf R\cup\{\pm\infty\}$, consider the region of the plane above the graph of the function, i.e.

$$
\operatorname{epi} f = \{(x,y)\in\mathbf R^2 : y\ge f(x)\}.
$$

This region is also called the **epigraph** of the function $f$. The convexity of a function is equivalent to the convexity of its epigraph:

???+ note "Epigraph characterization of convex functions"
    A function $f:\mathbf R\rightarrow\mathbf R\cup\{\pm\infty\}$ is convex if and only if $\operatorname{epi}f$ is a convex set in $\mathbf R^2$.

??? note "Proof"
    If $f$ is convex, then for $(x_1,y_1),(x_2,y_2)\in\operatorname{epi}f$ and any $\alpha\in(0,1)$,
    
    $$
    \alpha y_1+(1-\alpha)y_2 \ge \alpha f(x_1)+(1-\alpha)f(x_2) \ge f(\alpha x_1+(1-\alpha) x_2).
    $$
    
    Hence $\alpha(x_1,y_1)+(1-\alpha)(x_2,y_2)\in\operatorname{epi}f$.
    
    Conversely, if $\operatorname{epi}f$ is a convex set, then for any $x_1<x_2$ and $\alpha\in(0,1)$,
    
    $$
    \alpha(x_1,f(x_1))+(1-\alpha)(x_2,f(x_2)) \in \operatorname{epi}f.
    $$
    
    This is equivalent to $\alpha f(x_1)+(1-\alpha)f(x_2)\ge f\left(\alpha x_1+(1-\alpha)x_2\right)$, i.e. the convexity of $f$.

We will see later that, using the epigraph, the infimal convolution of convex functions can be related to the Minkowski sum of convex sets.

## Transformations of convex functions

Next, this article introduces some convexity-preserving transformations frequently encountered in Slope Trick.

### Non-negative linear combinations

For convex functions $f$ and $g$ and non-negative real numbers $\alpha,\beta\ge0$, the function $\alpha f+\beta g$ is also convex. Moreover,

$$
\Delta(\alpha f+\beta g) = \alpha\Delta f + \beta\Delta g.
$$

Therefore, if the slopes of the convex functions $f$ and $g$ are maintained, the slope of their non-negative linear combination $\alpha f+\beta g$ is obtained simply by computing segment by segment.

In problems where slopes are maintained, one of the functions often has a simple form, in which case lazy tags can be used to reduce the modification complexity. In problems where kinks are maintained, to compute the slope kinks of $f+g$ it suffices to merge the slope kinks of $f$ and $g$.

### Infimal convolution (Minkowski sum)

Another common operation on convex functions is the infimal convolution. For functions $f$ and $g$, the function

$$
h(x) = \inf_{y\in\mathbf R}f(y)+g(x-y)
$$

is called the **infimal convolution**[^inf-conv] of $f$ and $g$. If $f$ and $g$ are both convex, their infimal convolution is also convex.

![](../images/slope-trick/epigraph-convex-minkowski.svg)

??? example "Explanation of the figure"
    As shown in the figure, to obtain the infimal convolution $h$ of $f$ and $g$, every point on the graph of $f$ (the red dashed line in the third figure) can be regarded as the origin, and the graph of $g$ (the blue dashed line in the third figure) is drawn in the corresponding coordinate system. As the origin of the coordinate system moves along the graph of $f$, the outline of the trace swept by the graph (epigraph) of $g$ (i.e. the lower convex hull) is exactly the graph of $h$. One can see that every slope segment of $h$ is either a slope segment of $f$ or a slope segment of $g$: they are just re-sorted by slope. In this process the roles of $f$ and $g$ can be exchanged, i.e. moving the graph of $f$ along the graph of $g$ gives the same result.

Geometrically, $\operatorname{epi}h$ is exactly the [Minkowski sum](../../geometry/convex-hull.md#minkowski-sum) of $\operatorname{epi}f$ and $\operatorname{epi}g$. If $f$ and $g$ are both piecewise linear functions, then $h$ is also piecewise linear, and its slope segments can be regarded as the result of merging (and re-sorting) the slope segments of $f$ and $g$.

??? note "Proof"
    Let $f,g$ be convex functions and $h$ their infimal convolution. Let $x_1<x_2$ and $\alpha\in(0,1)$. By the definition of the infimal convolution, for every $\varepsilon>0$ there exist $y_i,z_i\in\mathbf R$ with $y_i+z_i=x_i$ and
    
    $$
    h(x_i) + \varepsilon > f(y_i) + g(z_i).
    $$
    
    Hence, combining the convexity of $f,g$ and the definition of $h$,
    
    $$
    \begin{aligned}
    \alpha h(x_1)+(1-\alpha)h(x_2) + \varepsilon 
    &> \alpha f(y_1) + (1-\alpha) f(y_2) + \alpha g(z_1) + (1-\alpha) g(z_2)\\
    &\ge f\left(\alpha y_1+(1-\alpha)y_2\right) + g\left(\alpha z_1+(1-\alpha)z_2\right)\\
    &\ge h(\alpha x_1+(1-\alpha)x_2).
    \end{aligned}
    $$
    
    Since $\varepsilon>0$ was chosen arbitrarily,
    
    $$
    \alpha h(x_1)+(1-\alpha)h(x_2) \ge h(\alpha x_1+(1-\alpha)x_2).
    $$
    
    This gives the convexity of $h$.
    
    Then, as for the geometric intuition, strictly speaking only the following can be proved:
    
    $$
    \operatorname{epi} f + \operatorname{epi} g\subseteq \operatorname{epi}h \subseteq \operatorname{cl}(\operatorname{epi} f + \operatorname{epi} g).
    $$
    
    Here $\operatorname{cl}$ denotes the closure.
    
    For any $(x,y)\in\operatorname{epi} f + \operatorname{epi} g$, there exist $(x_1,y_1)\in\operatorname{epi} f$ and $(x_2,y_2)\in\operatorname{epi} g$ such that $x=x_1+x_2$ and
    
    $$
    y = y_1+y_2 \ge f(x_1)+g(x_2) \ge h(x_1+x_2)=h(x).
    $$
    
    Hence $(x,y)\in\operatorname{epi}h$. This shows $\operatorname{epi} f + \operatorname{epi} g\subseteq \operatorname{epi}h$.
    
    Conversely, for any $(x,y)\in\operatorname{epi}h$ we have $y\ge h(x)$. By the definition of $h$, for every $\varepsilon>0$ there exist $x_1+x_2=x$ such that
    
    $$
    y + \varepsilon > f(x_1) + g(x_2).
    $$
    
    Let $y_1=f(x_1)$ and $y_2=g(x_2)$; then $y+\varepsilon>y_1+y_2$. This shows that for every $\varepsilon>0$ there is a point $(x_1,y_1)+(x_2,y_2)\in\operatorname{epi} f + \operatorname{epi} g$ lying on the segment between the points $(x,y)$ and $(x,y+\varepsilon)$. Letting $\varepsilon\rightarrow 0$ gives $\operatorname{epi}h \subseteq \operatorname{cl}(\operatorname{epi} f + \operatorname{epi} g)$.
    
    Therefore, as long as $\operatorname{epi} f + \operatorname{epi} g$ is a closed set, $\operatorname{epi} f + \operatorname{epi} g = \operatorname{epi}h$. One condition that guarantees this is that $f$ and $g$ are both proper convex functions and [lower semi-continuous](https://en.wikipedia.org/wiki/Semi-continuity). For competitive programming applications this is sufficient; for example, piecewise linear functions always satisfy these conditions.

In practical problems, if one of $f$ and $g$ has few slope segments, the smaller set of slope segments can be inserted directly into the larger one; otherwise, it may be necessary to use methods such as [small-to-large merging](../../graph/dsu-on-tree.md) or [mergeable heaps](../../ds/heap.md) to reduce the overall complexity of merging, or to find a suitable approach according to the specific problem.

### Minimum and maximum operations

The maximum of two convex functions is still a convex function, but the minimum of two convex functions is not necessarily convex.

Many common minimum operations can be transformed into infimal convolutions:

???+ example "Examples"
    -   $f(x)=\min_{y\in [x+a,x+b]}g(y)$ is still a convex function, since it can be viewed as an infimal convolution:
    
        $$
        f(x) = \min_{y\in\mathbf R}g(y) + 0_{[-b,-a]}(x-y).
        $$
    -   $f(x)=\min\{g(x-a_i)+b_i\}$ is a convex function on $\mathbf Z$, as long as $g(x)$ is a convex function on $\mathbf Z$ and the function $h:a_i\mapsto b_i$ defined on the finite set $\{a_i\}\subset\mathbf Z$ is also convex on that discrete set. This is because the extended function $\tilde f(x)$ can be viewed as an infimal convolution:
    
        $$
        \tilde f(x) = \min_{y\in\mathbf R}\tilde h(y)+\tilde g(x-y).
        $$
    
        Therefore the function $f(x)$ before extension is also convex.

But not all minimum operations preserve convexity.

???+ example "Counterexample"
    Let $g(x)$ be a convex function; the function $f(x)=\min\{g(x-1)+kx,g(x)\}$ is not necessarily convex.

In some special problems, although the transition equation of the dynamic program can be written as the minimum of two convex functions and is hard to transform into an infimal convolution, the value function nevertheless remains convex. In practice, finding a reasonable way to transition the slopes for such problems usually requires a combination of printing tables and guessing.

Having understood convex functions and their common transformations, we can understand the Slope Trick method of optimizing DP through concrete problems. The examples in this article are roughly divided into two groups, maintaining kinks and maintaining slopes, in order to understand the common operations and implementation details of these two ways of maintenance. But, as emphasized earlier, the way of maintenance is not the essence of Slope Trick; a suitable way of maintaining slope segments should be chosen according to the needs of the specific problem.

## Maintaining kinks

This class of problems usually appears in problems that require minimizing a sum of several absolute values. Since in these problems the absolute value of the slope of the value function is not large, it is more convenient to maintain the kinks where the slope changes.

Maintaining kinks means maintaining the points of a piecewise linear function where the slope changes. This amounts to maintaining, for each slope segment $[l_i,r_i]$ with slope $k_i$, only the information about its endpoints, while the slope itself need not be maintained separately; therefore, in these problems, every time the slope changes it should change only by a fixed amount. For example, if the kink set $\xi_{-s}\le\cdots\le\xi_{-1}\le\xi_{1}\le\cdots\le\xi_{t}$ is maintained, this means: on the interval $[\xi_{-1},\xi_1]$ the slope is $0$; each time a kink is passed to the left, the slope decreases by one; each time a kink is passed to the right, the slope increases by one; hence on the interval $[\xi_2,\xi_3]$ the slope is $2$, on the interval $[\xi_{-3},\xi_{-2}]$ the slope is $-2$, and so on. Formally, the function can be written using the slope kinks as

$$
f(x) = f(\xi_1) + \sum_{i=-s}^{-1}\max\{\xi_i-x,0\} + \sum_{i=1}^{t}\max\{x-\xi_i,0\}.
$$

Its minimum is $f(\xi_{-1})=f(\xi_1)$, and it is attained at any point of the interval $[\xi_{-1},\xi_1]$.

![](../images/slope-trick/epigraph-convex-kinks.svg)

### Example: increasing sequence of minimum cost

???+ example "[\[BalticOI 2004\] Sequence](https://www.luogu.com.cn/problem/P4331)"
    Given a sequence $\{a_i\}$ of length $n$, find a strictly increasing sequence $\{b_i\}$ minimizing $\sum_i|a_i-b_i|$; output the minimum and any optimal solution $\{b_i\}$.

??? note "Solution"
    First, $\{b_i\}$ being strictly increasing is equivalent to $\{b'_i\}=\{b_i-i\}$ being weakly increasing. Therefore we can find, for $\{a'_i\}=\{a_i-i\}$, the weakly increasing sequence $\{b'_i\}=\{b_i-i\}$ with the smallest difference and then recover the sequence $\{b_i\}$.
    
    Consider the naive DP solution. Let $f_i(x)$ be the minimum difference between the chosen numbers and the first $i$ numbers of $\{a'_i\}$ when the first $i$ numbers of the sequence $\{b'_i\}$ have been chosen and the $i$-th number does not exceed $x$:
    
    $$
    f_i(x) = \min\sum_{j=1}^i|a'_j-b'_j|\text{ s.t. }b'_1\le b'_2\le\cdots\le b'_i\le x.
    $$
    
    The state transition equation is easily obtained:
    
    $$
    f_i(x) = \min_{y\le x}f_{i-1}(y)+|a'_i-y|.
    $$
    
    The initial state is $f_0(x)\equiv 0$, and what we finally need is $\min_xf_n(x)$. Using the transformations of convex functions mentioned above, going from $f_{i-1}(x)$ to $f_i(x)$ takes two transformations:
    
    1.  First, add $|a'_i-x|$, which amounts to adding $-1$ to all slope segments in the interval $(-\infty,a'_i]$ and adding $1$ to all slope segments in the interval $[a'_i,+\infty)$;
    2.  Take the minimum of the resulting function, turning $g(x)=f_{i-1}(x)+|a'_i-x|$ into $f_i(x)=\min_{y\le x}g(y)$. By the analysis above, this amounts to the infimal convolution of $g(x)$ and $0_{[0,+\infty)}$. Since the latter has only one slope segment, with slope $0$ and extending infinitely to the right, inserting it into the slope segments of $g(x)$ amounts to deleting all of its positive-slope segments.
    
    Having clarified these operations, we could already maintain all slope segments directly with a balanced tree, but the code is complex. Note that in this problem the slope changes by at most $1$ each time, so the absolute values of all slopes do not exceed $n$. It is more convenient not to maintain the slope segments directly but to maintain the slope kinks instead.
    
    Let the kink set of $f_{i-1}(x)$ be $\xi_{-k}\le\cdots\le\xi_{-1}\le\xi_{1}\le\cdots\le\xi_{\ell}$. Then the two steps above correspond respectively to:
    
    1.  adding one kink $a'_i$ of a negative-slope segment and one kink $a'_i$ of a positive-slope segment;
    2.  popping all kinks $\xi_1,\cdots,\xi_{\ell}$ of positive-slope segments.
    
    In the actual maintenance, since after each operation there are no kinks of positive-slope segments, i.e. the slope kinks have the form $\xi_{-k}\le\cdots\le\xi_{-1}$, and the operations always happen at the boundary between positive- and negative-slope segments, it suffices to maintain a max-heap storing all kinks. The two steps correspond respectively to:
    
    1.  inserting $a'_i$ twice;
    2.  popping the top of the heap.
    
    Of course, after each step the minimum of the current function also has to be maintained. Since after the operation there are no positive-slope segments, the minimum of the function is its value at the top of the max-heap. Let the top of the heap before each operation be $\xi_{-1}$ and the minimum $f_{i-1}(\xi_{-1})$. Since the popped top of the heap is the smallest kink of the positive-slope segments, the minimum of the function equals the function value there, so it suffices to directly compute the function value at the top of the heap before popping, namely
    
    $$
    f_{i-1}(\max\{a'_i,\xi_{-1}\})+|\max\{a'_i,\xi_{-1}\}-a'_i|=f_{i-1}(\xi_{-1})+\max\{0,\xi_{-1}-a'_i\}.
    $$
    
    Here the first terms are equal because $f_{i-1}(x)$ has no positive-slope segments. Therefore it suffices to keep adding $\max\{0,\xi_{-1}-a'_i\}$ to the minimum each time.
    
    This problem also asks to output an optimal solution. Since when the last operation finishes the optimal solution is the top of the heap, the value of $b'_n$ can be determined directly. If the $i$-th optimal solution $b'_i$ is known and we want the optimal solution of $f_{i-1}(x)$ subject to $x\le b'_i$, we only need to note that, since $f_{i-1}(x)$ is convex, the closer to its global minimum point, the better the solution; hence it suffices to record the global minimum point of $f_{i-1}(x)$ and take the minimum of it and $b'_i$ to obtain the optimal $b'_{i-1}$.
    
    The time complexity is $O(n\log n)$.
    
    ```cpp
    --8<-- "docs/dp/code/opt/slope-trick/sequence.cpp"
    ```

Template problems:

-   [Codeforces 713 C. Sonya and Problem Without a Legend](https://codeforces.com/problemset/problem/713/C)
-   [Luogu P2893 \[USACO08FEB\] Making the Grade G](https://www.luogu.com.cn/problem/P2893)
-   [Luogu P4331 \[BalticOI 2004\] Sequence](https://www.luogu.com.cn/problem/P4331)
-   [Luogu P4597 Sequence](https://www.luogu.com.cn/problem/P4597)
-   [AtCoder Dwango Programming Contest 2 Qualifiers E - Fireworks](https://atcoder.jp/contests/dwango2016-prelims/tasks/dwango2016qual_e)

### Example: transitions with constraints

???+ example "[\[NOISG 2018 Finals\] Safety](https://www.luogu.com.cn/problem/P11598)"
    Given a sequence $\{a_i\}$ of length $n$, find a sequence $\{b_i\}$ such that $|b_i-b_{i-1}|\le h$ holds for all $1<i\le n$ and $\sum_i|a_i-b_i|$ is minimized; output the minimum.

??? note "Solution"
    The content is roughly similar to the previous problem, only the constraint on the sequence $\{b_i\}$ has changed. Likewise, let $f_i(x)$ be the minimum difference of the first $i$ numbers when the $i$-th number takes the value $x$:
    
    $$
    f_i(x) = \min\sum_{j=1}^i|a_j-b_j|\text{ s.t. }|b_{j-1}-b_j|\le h,\forall 1<j\le i,~b_i=x.
    $$
    
    From this, the state transition equation is
    
    $$
    f_i(x) = |a_i-x| + \min_{|y-x|\le h} f_{i-1}(y). 
    $$
    
    The initial condition is $f_0(x)\equiv 0$. What we finally need is still $\min_xf_n(x)$.
    
    The state transition decomposes into operations on convex functions, in two steps:
    
    1.  First take the minimum of $f_{i-1}(x)$, obtaining $\min_{|y-x|\le h} f_{i-1}(y)$, which amounts to the infimal convolution of $f_{i-1}(x)$ and $0_{[-h,h]}(x)$;
    2.  Then add $|a_i-x|$ to the resulting function.
    
    Again, since the slope changes by one each time, we can consider maintaining kinks. Then these two steps can be described as:
    
    1.  moving all negative-slope segments to the left by $h$ and all positive-slope segments to the right by $h$;
    2.  inserting $a_i$ twice.
    
    Clearly, for this problem it is convenient to maintain the positive- and negative-slope segments separately. Since the operations are mainly concentrated around the zero-slope segment, consider using a [pair of opposing heaps](../../ds/binary-heap.md#dual-heap), i.e. maintain the kinks of the negative- and positive-slope segments with a max-heap and a min-heap respectively. The global shift of the kinks is done with lazy tags. The second step requires inserting one $a_i$ into each of the two heaps; moreover, after the insertion the top of the max-heap is not necessarily still less than or equal to the top of the min-heap. In that case, swap the two tops until the order relation between the tops is satisfied.
    
    Finally, consider how to update the minimum during the operations. Since the shift in the first step does not change the minimum, we only need to consider the operation of swapping the heap tops. Let $\xi_{-1}>\xi_1$; when the tops $\xi_{-1}$ and $\xi_1$ are swapped, the function changes from
    
    $$
    \max\{0,\xi_{-1}-x\}+\max\{0,x-\xi_1\}
    $$
    
    to
    
    $$
    \max\{0,\xi_{1}-x\}+\max\{0,x-\xi_{-1}\}.
    $$
    
    In this process the shape of the function does not change, it is only shifted downwards by $|\xi_{-1}-\xi_1|$. Therefore, to keep the function unchanged before and after swapping the tops, it suffices to add $|\xi_{-1}-\xi_1|$ to the minimum.
    
    The time complexity of the algorithm is still $O(n\log n)$, since after each element is added the swap of the heap tops is performed at most once.
    
    ```cpp
    --8<-- "docs/dp/code/opt/slope-trick/safety.cpp"
    ```

Template problems:

-   [Luogu P4272 \[CTSC2009\] Sequence transformation](https://www.luogu.com.cn/problem/P4272)
-   [Luogu P11598 \[NOISG 2018 Finals\] Safety](https://www.luogu.com.cn/problem/P11598)
-   [AtCoder Beginner Contest 217 H - Snuketoon](https://atcoder.jp/contests/abc217/tasks/abc217_h)
-   [AtCoder Regular Contest 070 E - NarrowRectangles](https://atcoder.jp/contests/arc070/tasks/arc070_c)
-   [AtCoder Regular Contest 123 D - Inc, Dec - Decomposition](https://atcoder.jp/contests/arc123/tasks/arc123_d)

## Maintaining slopes

There are also problems in which maintaining slopes is more convenient. Such problems can usually also be solved with [regret greedy](../../basic/greedy.md#regret-solutions) or the idea of simulated cost flow. In a cost flow model the minimum cost is often a convex function of the flow, which provides the basis for applying Slope Trick.

### Example: stock trading

???+ example "[Codeforces 865 D. Buy Low Sell High](https://codeforces.com/problemset/problem/865/D)"
    Given a sequence of stock prices $\{p_i\}$ over $n$ days (all positive), with initially $0$ shares held, each day you may buy one share, sell one share or do nothing; find the maximum profit after $n$ days.

??? note "Solution"
    First consider the naive DP solution. Let $f_i(x)$ be the maximum profit at the end of day $i$ when $x\ge 0$ shares are held; then
    
    $$
    f_i(x) = \max\{f_{i-1}(x-1)-p_i,f_{i-1}(x),f_{i-1}(x+1)+p_i\}.
    $$
    
    The initial state is $f_0(0)=0$, and $f_0(x)=-\infty$ for all $x\neq 0$. The answer to the problem is $f_n(0)$.
    
    Going from $f_{i-1}(x)$ to $f_i(x)$ takes two transformations:
    
    1.  Take the supremal convolution of $f_{i-1}(x)$ with the piecewise linear function $\tilde h_i(x)$ (clearly concave) corresponding to the function
    
        $$
        h_i(x) = \begin{cases}p_i,&x=-1,\\0,&x=0,\\-p_i,&x=1\end{cases}
        $$
    
    2.  Since this makes the function take finite values in the interval $[-1,0)$, which contradicts the requirement $x\ge 0$, the part of the function in $[0,+\infty)$ has to be cut out.
    
    Converted into changes of slope segments, these are the following two steps:
    
    1.  insert a slope segment of length $2$ with slope $-p_i$;
    2.  among the slope segments with finite slope, delete the segment of length $1$ with the largest slope.
    
    Since the lengths of the slope segments are always natural numbers, we may maintain a number of slope segments of length one, so that only the slope of each segment needs to be recorded. Since only insertion and access to the maximum are needed, a single max-heap suffices. The operation has two steps:
    
    1.  insert $-p_i$ twice;
    2.  pop the top of the heap.
    
    The value of $f_i(0)$ also has to be maintained. Since the value at $x=-1$ of the function obtained in the first step is $f_{i-1}(0)+p_i$, its value at $x=0$ is this value plus the heap top that is about to be popped — which is the slope of the function on the interval $[-1,0]$. Since the truncation does not change the function value at $x=0$, this is exactly $f_i(0)$.
    
    Comparing the implementation of this algorithm with the code of [Increasing sequence of minimum cost](#example-increasing-sequence-of-minimum-cost) above shows that this algorithm is equivalent to computing the minimum cost of turning the stock price sequence into a weakly decreasing sequence.
    
    The time complexity is $O(n\log n)$.
    
    ```cpp
    --8<-- "docs/dp/code/opt/slope-trick/stock.cpp"
    ```

Template problems:

-   [Codeforces 865 D. Buy Low Sell High](https://codeforces.com/problemset/problem/865/D)

### Example: moving soil

???+ example "[\[USACO16OPEN\] Landscaping P](https://www.luogu.com.cn/problem/P2748)"
    Given sequences $\{a_i\}$ and $\{b_i\}$ of length $n$, denoting respectively the amount of soil the $i$-th garden already has and the amount it needs (no more and no less). Buying one unit of soil and putting it in any garden costs $X$, removing one unit of soil from any garden costs $Y$, and moving one unit of soil from garden $i$ to garden $j$ costs $Z|i-j|$. Find the minimum cost of satisfying the needs of all gardens. ($a_i,b_i\le 10$)

??? note "Solution"
    Consider the naive DP solution. Let $f_i(x)$ be the minimum cost of satisfying the needs of the first $i$ gardens with a net surplus of $x$ units of soil carried to the later gardens. If $x<0$, this means a net deficit of $|x|$ units of soil that has to be brought from the later gardens. Then the state transition equation can be written as
    
    $$
    f_i(x) = \min_{y\in\mathbf R} f_{i-1}(y) + |y|Z + h((x-y)+(b_i-a_i)).
    $$
    
    Here the function $h(\delta)$ denotes the cost when the net amount of soil bought for the current garden is $\delta$, i.e.
    
    $$
    h(\delta) = \max\{0,\delta\}X + \max\{0,-\delta\}Y = \max\{\delta X,-\delta Y\}.
    $$
    
    It is clearly convex. The meaning of this state transition equation is:
    
    -   when the net surplus of soil of the previous $i-1$ gardens is $y$, the minimum cost is $f_{i-1}(y)$;
    -   the cost of moving the net surplus (deficit) of soil between $i$ and $i-1$ is $|y|Z$;
    -   the minimum cost of adjusting, by buying and selling, the amount of soil in the $i$-th garden from $a_i$ to $b_i$ and the net surplus of soil from $y$ to $x$ is $h((x-y)+(b_i-a_i))$.
    
    The initial state is $f_0(0)=0$, and $f_0(x)=+\infty$ for all $x\neq 0$. The answer to the problem is $f_n(0)$.
    
    Transforming the function $f_{i-1}(x)$ into $f_i(x)$ can be divided into three steps:
    
    1.  First, add $|x|Z$ to get $f_{i-1}(x)+|x|Z$;
    2.  Then take the infimal convolution with $h(x)$ to get $\min_{y\in\mathbf R}f_{i-1}(y)+|y|Z+h(x-y)$;
    3.  Finally, shift the function to the left by $(b_i-a_i)$ units.
    
    Converted into operations on slope segments, also in three steps:
    
    1.  add $-Z$ to all slope segments to the left of the origin and $Z$ to all slope segments to the right of the origin;
    2.  replace all slope segments with slope less than $-Y$ by $-Y$, and all slope segments with slope greater than $X$ by $X$;
    3.  shift all slope segments to the left by $(b_i-a_i)$ units.
    
    In the original problem $a_i$ and $b_i$ are very small, so it suffices to maintain a number of slope segments of length $1$. Although there are infinitely many slope segments, there is an upper bound $X$ and a lower bound $-Y$, and the number of slope segments strictly between them is not large. Since no insertion operations are involved, the slope segments on the two sides of the origin can be maintained with two stacks, and the range-add and range-min/max operations are all done with lazy tags. The three steps above correspond respectively to:
    
    1.  putting lazy tags on the left and right stacks: add $-Z$ on the left, $Z$ on the right;
    2.  every time an element is popped from a stack, take the maximum with $-Y$ and the minimum with $X$. If the left stack is empty, pop $-Y$. If the right stack is empty, pop $X$;
    3.  popping the $(b_i-a_i)$ elements at the top of the left stack and inserting them into the right stack; of course, when $b_i-a_i<0$, the other way round.
    
    When moving stack tops, update the answer: moving to the left subtracts the current slope, moving to the right adds the current slope.
    
    The complexity of the algorithm is $O(n\max\{a_i,b_i\})$.
    
    ```cpp
    --8<-- "docs/dp/code/opt/slope-trick/landscaping.cpp"
    ```

Template problems:

-   [Luogu P2748 \[USACO16OPEN\] Landscaping P](https://www.luogu.com.cn/problem/P2748)
-   [Kyoto University PC 2016 H - WAAAAAAAAAAAAALL](https://atcoder.jp/contests/kupc2016/tasks/kupc2016_h)
-   [JAG Practice Contest 2017 J - Farm Village](https://atcoder.jp/contests/jag2017autumn/tasks/jag2017autumn_j)

## Exercises

At the end of this article, we provide some problems that have appeared in various programming contests and can be solved with Slope Trick, for practice.

-   [Luogu P3642 \[APIO2016\] Fireworks](https://www.luogu.com.cn/problem/P3642)
-   [Luogu P9962 \[THUPC 2024 Preliminary\] A tree](https://www.luogu.com.cn/problem/P9962)
-   [Luogu P11317 \[RMI 2021\] Paths](https://www.luogu.com.cn/problem/P11317)
-   [AtCoder Beginner Contest 383 G - Bar Cover](https://atcoder.jp/contests/abc383/tasks/abc383_g)
-   [Codeforces 280 D. k-Maximum Subsequence Sum](https://codeforces.com/problemset/problem/280/D)
-   [Codeforces 280 E. Sequence Transformation](https://codeforces.com/problemset/problem/280/E)
-   [Codeforces 802 O. April Fools' Problem (hard)](https://codeforces.com/contest/802/problem/O)
-   [Codeforces 1209 H. Moving Walkways](https://codeforces.com/contest/1209/problem/H)
-   [Codeforces 1229 F. Mateusz and Escape Room](https://codeforces.com/contest/1229/problem/F)
-   [Codeforces 1534 G. A New Beginning](https://codeforces.com/problemset/problem/1534/G)
-   [Codeforces 1787 H. Codeforces Scoreboard](https://codeforces.com/problemset/problem/1787/H)
-   [2019 Summer Petrozavodsk Camp H. Honorable Mention](https://codeforces.com/gym/102331/problem/H)
-   [2018 ACM-ICPC World Finals C. Conquer The World](https://codeforces.com/gym/102482/problem/C)
-   [300iq Contest 3 F. Farm of Monsters](https://codeforces.com/gym/102538/problem/F)

## References and notes

-   [\[Tutorial\] Slope Trick - zscoder](https://codeforces.com/blog/entry/47821)
-   [Slope trick explained - Kuroni](https://codeforces.com/blog/entry/77298)
-   [Slope Trick - USACO Guide](https://usaco.guide/adv/slope-trick?lang=cpp)
-   [\[Tutorial\] Intuition on Slope Trick - maomao90](https://codeforces.com/blog/entry/103222)

[^convex-def]: Different textbooks may use different names for convex functions.

[^inf-conv]: Also often called $\min$-convolution, $\inf$-convolution or $(\min,+)$-convolution.
