---
title: DSU complexity
---

This section is reproduced and adapted from [Time Complexity -- A Brief Discussion of Potential Analysis](https://www.luogu.com.cn/blog/Atalod/shi-jian-fu-za-du-shi-neng-fen-xi-qian-tan), with the permission of the original author.

## Definitions

### Ackermann function

First we give the definition of $\alpha(n)$. To do so, we first define $A_k(j)$.

Define $A_k(j)$ as:

$$
A_k(j)=\left\{
\begin{aligned}
&j+1& &k=0&\\
&A_{k-1}^{(j+1)}(j)& &k\geq1&
\end{aligned}
\right.
$$

This is the Ackermann function.

Here $f^i(x)$ denotes applying $f$ to $x$ $i$ times in succession, i.e. $f^0(x)=x$, $f^i(x)=f(f^{i-1}(x))$.

Then define $\alpha(n)$ as the smallest integer such that $A_{\alpha(n)}(1)\geq n$. Note that we previously described it as $A_{\alpha(n)}(\alpha(n))\geq n$; either way they both grow very slowly and their values never exceed 4.

### Basic definitions

Every node has a rank. The rank here is not the number of nodes but the depth. The initial rank of a node is 0; when merging, if the two nodes have different ranks, the node with the smaller rank is attached to the node with the larger rank and the larger node's rank is not updated. Otherwise one node is attached to the other at random and the rank of the root is increased by 1. The rank of the root thus gives the height of the tree. Denote the rank of $x$ by $rnk(x)$, and similarly the parent of $x$ by $fa(x)$. We always have $rnk(x)+1\leq rnk(fa(x))$.

To define the potential function, we first need an auxiliary function $level(x)$, where $level(x)=\max(k:rnk(fa(x))\geq A_k(rnk(x)))$. When $rnk(x)\geq1$, define another auxiliary function $iter(x)=\max(i:rnk(fa(x))\geq A_{level(x)}^i(rnk(x))$. The $x$ in these definitions all satisfy $rnk(x)>0$ and $x$ is not the root of any tree.

The definitions above may make you a little dizzy. Let us sort them out again: for an $x$ and $fa(x)$, if $rnk(x)>0$, we can always find a pair $i,k$ such that $rnk(fa(x))\geq A_k^i(rnk(x))$; $level(x)=\max(k)$, and under that premise $iter(x)=\max(i)$. $level$ describes the maximum iteration level of $A$, and $iter$ the maximum number of iterations at that maximum level.

For these two functions, $level(x)$ always increases or stays the same as operations proceed, and if $level(x)$ does not increase, $iter(x)$ also only increases or stays the same. Moreover, they always satisfy the following two inequalities:

$$
0\leq level(x)<\alpha(n)
$$

$$
1\leq iter(x)\leq rnk(x)
$$

Considering the definitions of $level(x)$, $iter(x)$ and $A_k^j$, these are easy to prove and are left to the reader as an exercise for getting familiar with the definitions.

Define the potential function $\Phi(S)=\sum\limits_{x\in S}\Phi(x)$, where $S$ denotes the whole DSU and $x$ a node in it. Define $\Phi(x)$ as:

$$
\Phi(x)=
\begin{cases}
\alpha(n)\times \mathit{rnk}(x)& \mathit{rnk}(x)=0\ \text{or}\ x\ \text{is the root of some tree}\\
(\alpha(n)-\mathit{level}(x))\times \mathit{rnk}(x)-iter(x)& \text{otherwise}
\end{cases}
$$

Then we prove that the amortized time complexity is $\Theta(\alpha(n))$ through the changes in potential caused by the operations. Note that the $union(x,y)$ operation discussed here guarantees that $x$ and $y$ are both roots of some trees, so there is no need to additionally perform $find(x)$ and $find(y)$.

One can see that the potential is always non-negative. Also, at the start the potential of the DSU is $0$.

## Proof

### The union(x,y) operation

Its time cost is $\Theta(1)$, so we consider the change in potential it causes.

Here we assume $rnk(x)\leq rnk(y)$, i.e. $x$ is attached to $y$. Then the only nodes whose potential can increase are $x$ (changing from a root to a non-root), $y$ (its rank may increase) and the children of $y$ before the operation (the rank of their parent may increase). We first prove that the potential of a child $c$ of $y$ before the operation cannot increase, and if it decreases, it decreases by at least $1$.

Let the potential of $c$ before the operation be $\Phi(c)$ and after the operation $\Phi(c')$; here $c$ can be any non-root node with $rnk(c)>0$, and the operation can be any operation, including the find operation below. We distinguish three cases.

1.  Neither $iter(c)$ nor $level(c)$ increased. Clearly $\Phi(c)=\Phi(c')$.
2.  $iter(c)$ increased and $level(c)$ did not. Here $iter(c)$ increased by at least one, i.e. $\Phi(c')\leq \Phi(c)-1$; the potential function decreased, by at least 1.
3.  $level(c)$ increased and $iter(c)$ may have decreased. But since $0<iter(c)\leq rnk(c)$, $iter(c)$ decreases by at most $rnk(c)-1$, while $level(c)$ increases by at least $1$. From the definition $\Phi(c)=(\alpha(n)-level(c))\times rnk(c)-iter(c)$ we get $\Phi(c')\leq\Phi(c)-1$.
4.  Other cases. Since $rnk(c)$ is unchanged and $rnk(fa(c))$ does not decrease, these do not exist.

So the only nodes whose potential can increase are $x$ or $y$. Now $x$ changes from a root to a non-root; if $rnk(x)=0$ we always have $\Phi(x)=\Phi(x')=0$. Otherwise we must have $\alpha(x)\times rnk(x)\geq(\alpha(n)-level(x))\times rnk(x)-iter(x)$, i.e. $\Phi(x')\leq \Phi(x)$.

Therefore the only node whose potential may increase is $y$, and the potential of $y$ increases by at most $\alpha(n)$. Hence the amortized time complexity of the $union$ operation is $\Theta(\alpha(n))$.

### The find(a) operation

If the search path contains $\Theta(s)$ nodes, the time complexity of the search is obviously $\Theta(s)$. If, due to the find operation, no node's potential increases and at least $s-\alpha(n)$ nodes have their potential decreased by at least $1$, then the time complexity of $find(a)$ is proven to be $\Theta(\alpha(n))$. To avoid confusion, $a$ is used as the argument here, while every $x$ that appears refers generically to some node in the DSU.

First we prove that no node's potential increases. Clearly, we proved above that the potential of all non-root nodes does not increase, and the $rnk$ of the root does not change, so no node's potential increases.

Next we prove that at least $s-\alpha(n)$ nodes have their potential decreased by at least $1$. We proved above that if $level(x)$ or $iter(x)$ changes, the potential decreases by at least $1$. So it suffices to prove that at least $s-\alpha(n)$ nodes have $level(x)$ or $iter(x)$ changed.

Recall the definition of the potential of a non-root node, $\Phi(x)=(\alpha(n)-level(x))\times rnk(x)-iter(x)$, where $level(x)$ and $iter(x)$ are the largest numbers such that $rnk(fa(x))\geq A_{level(x)}^{iter(x)}(rnk(x))$.

So if $root_x$ denotes the root of the tree containing $x$, it suffices to prove $rnk(root_x)\geq A_{level(x)}^{iter(x)+1}(rnk(x))$. By the definition of $A_k^i$, $A_{level(x)}^{iter(x)+1}(rnk(x))=A_{level(x)}(A_{level(x)}^{iter(x)}(rnk(x)))$.

Note that we may use $k(x)$ for $level(x)$ and $i(x)$ for $iter(x)$ to keep the formulas from getting too long. Here that is $rnk(root_x)\geq A_{k(x)}(A_{k(x)}^{i(x)}(x))$.

When you get here you may have a "what on earth is this" feeling. That means you may need to read it a few more times, or skip some content and come back later.

Here we need an outer $A_{k(x)}$, which means we may need to find another node $y$. Let $y$ be a node after $x$ on the search path with $k(y)=k(x)$, where "after on the search path" means "an ancestor of $x$". Obviously not every $x$ has such a $y$. It is easy to prove that there are at most $\alpha(n)+2$ nodes $x$ without such a $y$, because only the last $x$ for each $k$, together with $a$ and $root_a$, have no such $y$.

We stress again that $fa(x)$ refers to the parent of $x$ **before** path compression, and the parent of $x$ **after** path compression is always denoted $root_x$. For every $x$ for which $y$ exists, we always have $rnk(y)\geq rnk(fa(x))$. At the same time we have $rnk(fa(x))\geq A_{k(x)}^{i(x)}(rnk(x))$. Since $k(x)=k(y)$, we refer to both as $k$, i.e. $rnk(fa(x))\geq A_k^{i(x)}(rnk(x))$. We need to construct an $A_k$, so we can ignore the value of $iter(y)$ and directly use the weakened version $rnk(fa(y))\geq A_k(rnk(y))$.

If we combine the inequalities, something magical happens. We find that $rnk(fa(y))\geq A_k^{i(x)+1}(rnk(x))$. In other words, iterating from $rnk(x)$ toward $rnk(fa(y))$, $A_k$ can be applied at least $i(x)+1$ times without exceeding $rnk(fa(y))$.

Obviously $rnk(root_y)\geq rnk(fa(y))$, and $rnk(x)$ does not change during path compression. Therefore we get $rnk(root_x)\geq A_k^{i(x)+1}(rnk(x))$, which means the value of $iter(x)$ increases by at least 1; if $rnk(x)$ did not increase, then $level(x)$ must have increased.

So $\Phi(x)$ decreased by at least 1. Since there are at least $s-\alpha(n)-2$ such nodes $x$, in the end $\Phi(S)$ decreases by at least $s-\alpha(n)-2$, and the amortized time complexity is $\Theta(\alpha(n)+2)=\Theta(\alpha(n))$.

## Why a DSU can be hacked

This question asks: if we do not union by rank, which properties are broken so that the time complexity of the DSU can no longer be guaranteed to be $\Theta(m\alpha(n))$?

If, when merging, a node with larger $rnk$ is attached to a node with smaller $rnk$, we set the $rnk$ of the node with the smaller $rnk$ to the other node's $rnk$ plus one. This way we can guarantee $rnk(fa(x))\geq rnk(x)+1$, so there is no violation of properties resembling "compile errors everywhere".

Obviously, in this case what we break is the statement in the analysis of $union(x,y)$ that "the potential of $y$ increases by at most $\alpha(n)$".

There is a structure that lowers the time complexity of a path-compression DSU to $\Omega(m\log_{1+\frac{m}{n}}n)$, defined as follows:

a binomial tree (actually somewhat different from the usual binomial tree), where $j$ is a constant and $T_k$ is a $T_{k-1}$ with a $T_{k-j}$ added as a child of the root.

![Binomial tree](./images/dsu-complexity.svg)

Boundary condition: $T_1$ through $T_j$ are each a single node.

Let $rnk(T_k)=r_k$; here we have $r_k=(k-1)/j$ (proof omitted). In each round of operations we attach it to a single node and then query the $j$ nodes at the bottom. That is, when we attach it to the single node, the potential of the single node rises by $(k-1)/j+1$. With $j=\lfloor\frac{m}{n}\rfloor$, $i=\lfloor\log_{j+1}\frac{n}{2}\rfloor$, $k=ij$, the increase in potential is:

$$
\alpha(n)\times((ij-1)/j+1)=\alpha(n)\times((\lfloor\log_{\lfloor\frac{m}{n}\rfloor+1}\frac{n}{2}\rfloor\times \lfloor\frac{m}{n}\rfloor-1)/\lfloor\frac{m}{n}\rfloor+1)
$$

Rearranging and removing all the floor symbols, we get that the increase in potential is $\geq \alpha(n)\times(\log_{1+\frac{m}{n}}n-\frac{n}{m})$, and for $m$ operations that is $\Omega(m\log_{1+\frac{m}{n}}n-n)=\Omega(m\log_{1+\frac{m}{n}}n)$.

## About union by size (heuristic merging)

Since union by rank is harder to write than union by size, many strong contestants choose to write the DSU with union by size. Specifically, a $size(x)$ is maintained for each root, and each time the smaller $size$ is merged into the larger one.

So, can union by size be hacked?

First, this can be explained through the properties of rank used in the proof. If $size$ can take the place of $rnk$, then union by size can be used. To summarize quickly, the properties of rank used in the proof are the following three:

1.  In each merge, at most one node's rank rises, and by at most 1.
2.  We always have $rnk(fa(x))\geq rnk(x)+1$.
3.  The rank of a node never decreases.

Regarding the second and third, $siz$ obviously satisfies them, but the first is not satisfied: if $x$ is merged into $y$, $siz(y)$ grows by $siz(x)$.

So we can consider replacing $rnk(x)$ with $\log_2 siz(x)$.

Regarding the first property, since the $siz$ of a node at most doubles, $\log_2 siz(x)$ rises by at most 1. For the second and third properties the conclusion is fairly obvious, and the proof is omitted here.

So if you do not want to write union by rank, just write union by size; the time complexity is still $\Theta(m\alpha(n))$.
