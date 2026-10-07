---
title: Constructive problems
---

This page briefly introduces constructive problems.

## Introduction

Constructive problems are a common type of problem in contests.

In form, the answer to the problem often has some regularity, so that even when the size of the problem grows rapidly, there is still a chance to obtain the answer fairly easily.

This requires thinking about how the growth of the problem size affects the answer, and whether this effect can be generalised. For example, when designing a dynamic programming approach, we consider what effect the transition from one state to a successor state has.

## Characteristics

A very noticeable feature of constructive problems is their high degree of freedom: a problem may have many possible constructions, but there is some relatively simple one that satisfies the requirements. This seems to loosen the requirements and make the problem easier, but very often it is exactly this freedom that leaves us with no clear idea of where to start.

Another feature is their flexible and varied form. There is no general method or recipe that solves all constructive problems; it is even hard to find common ground in the lines of reasoning.

## Examples

Below are some examples to help the reader feel the ideas behind constructive problems and to provide inspiration. We recommend thinking carefully before reading the solutions, and everyone is welcome to share interesting constructive problems.

### Example 1

???+ note "[Codeforces Round #384 (Div. 2) C. Vladik and fractions](http://codeforces.com/problemset/problem/743/C)"
    Construct three pairwise distinct positive integers $x,y,z$ such that for the given $n$, $\dfrac{1}{x}+\dfrac{1}{y}+\dfrac{1}{z}=\dfrac{2}{n}$.

??? note "Solution idea"
    The construction can be seen from the second sample.
    
    Split $\dfrac{2}{n}$ into $\dfrac{1}{n}+\dfrac{1}{n}$ and write the second term as $\dfrac{1}{n+1}+\dfrac{1}{n(n+1)}$. So $n,n+1,n(n+1)$ is a valid solution. In particular, there is no solution for $n=1$, because the sum of the reciprocals of three distinct positive integers is at most $1+\dfrac{1}{2}+\dfrac{1}{3}<2$.

### Example 2

???+ note "[Luogu P3599 Koishi Loves Construction](https://www.luogu.com.cn/problem/P3599)"
    Task1: determine whether it is possible, and construct, a permutation of $1\dots n$ of length $n$ whose $n$ prefix sums are pairwise distinct modulo $n$.
    
    Task2: determine whether it is possible, and construct, a permutation of $1\dots n$ of length $n$ whose $n$ prefix products are pairwise distinct modulo $n$.

??? note "Solution idea"
    For both tasks, when $n=1$ simply take the permutation $[1]$. Below assume $n>1$.
    
    Task1:
    
    When $n$ is odd, no valid solution exists; when $n$ is even, we can construct a sequence of the form $n,1,n-2,3,\cdots$.
    
    First, $n$ must appear in the first position, otherwise the two prefix sums right before and after $n$ would be equal modulo $n$;
    
    then consider how to construct the whole sequence:
    
    construct the prefix sum sequence and derive the original sequence from it; the differences of adjacent prefix sums (plus the first term) must be pairwise distinct modulo $n$, because the difference sequence of the prefix sums corresponds to the original permutation.
    
    So we try prefix sums that modulo $n$ look like
    
    $$
    0,1,-1,2,-2,\cdots
    $$
    
    and it is easy to see that this satisfies all the constraints.
    
    Task2:
    
    When $n$ is a composite number other than $4$, no valid solution exists; for $n=4$ take $[1,3,2,4]$ separately. When $n$ is prime, we can construct a sequence of the form $1,\dfrac{2}{1},\dfrac{3}{2},\cdots,\dfrac{n-1}{n-2},n$, where division means multiplying by the [modular inverse](../math/number-theory/inverse.md) modulo $n$ and taking the representative in $[1,n]$.
    
    First, when does a solution exist:
    
    for composite $n$ other than $4$ there is none. For a composite number there exist two smaller numbers $p,q$ with $p\times q \equiv 0 \pmod n$, e.g. $(3\times6)\bmod 9=0$. Once both $p$ and $q$ have appeared, the prefix product stays $0$, so composites other than $4$ have no solution. Specially, $4=2\times 2$ has no such pair $p,q$, so a valid solution exists.
    
    How to construct the sequence:
    
    as in Task1, $1$ must be in the first position, otherwise the prefix products before and after $1$ would be equal; and $n$ must be in the last position, because all prefix products after $n$ are $0$ modulo $n$. Analysing the samples given in the problem, we find that every sample has a valid solution whose prefix products modulo $n$ are $1,2,3,\cdots,n$, so we can construct the sequence described above. It remains to prove that these $n$ numbers are pairwise distinct.
    
    These numbers are exactly the inverses of $1 \cdots n-2$ plus $1$, hence distinct, and the problem is solved.

### Example 3

???+ note "[AtCoder Grand Contest 032 B](https://atcoder.jp/contests/agc032/tasks/agc032_b)"
    Given an integer $N$, construct an undirected graph with $N$ vertices numbered $1\ldots N$ satisfying:
    
    -   the graph is simple and connected;
    -   there is an integer $S$ such that for every vertex, the sum of the indices of its neighbours equals $S$.
    
    It is guaranteed that a solution exists.

??? note "Solution idea"
    By analysing the cases $n=3,4,5$ we can find a construction.
    
    Build a complete $k$-partite graph in which the $k$ parts have equal sums. Then $S$ is the same for every vertex, namely
    
    $$
    S=\dfrac{(k-1)\sum_{i=1}^{n}i}{k}.
    $$
    
    If $n$ is even, pair the vertices from both ends: $\{1,n\},\{2,n-1\}\cdots$.
    
    If $n$ is odd, take $n$ alone as one part and pair the remaining $n-1$: $\{n\},\{1,n-1\},\{2,n-2\}\cdots$.
    
    The connectivity of the constructed graph for $n\ge 3$ is easy to prove and omitted here.
    
    The problem is solved.

### Example 4

???+ note "[BZOJ 4971 \"Lydsy1708 月赛\" The knapsack from memory](https://vjudge.net/problem/BZOJ-4971)"
    After a hard day's work, little Q fell asleep. In his dream he recalled learning the 0-1 knapsack when he entered university; as a freshman he solved a simple 0-1 knapsack problem which went like this:
    
    Given $n$ items with volumes $v_1,v_2,\ldots,v_n$, compute the number of ways to choose some of them (possibly none) so that the total volume is exactly $w$. Since the answer may be very large, output it modulo $P$.
    
    Because of staying up late solving problems for a long time, he only saw $w$ and $P$ in the sample input and that the sample output is $k$, but could not see how many items there were or their volumes. Until he woke up, little Q never saw $n$ and $v$; write a program to help him recall the sample input.
    
    Multiple test cases; $50\le w\le20000$, $1\le P\le2^{30}$, $0\le k\le\min(20000,P-1)$; you must output $1\le n\le40$ items with $1\le v_i\le20000$.

??? note "Solution idea"
    This is one of the constructive problems with the highest degree of freedom, which makes it hard to know where to start.
    
    Since $k<P$, we can directly construct a set of items with exactly $k$ ways.
    
    One construction: take $i$ small items of volume $1$ and several large items of volume $w-t$, where $1\le i\le20$ and $0\le t\le i$. Since $i<w$ and $w-t\ge w-20>w/2$, every way of filling the knapsack exactly must use exactly one large item.
    
    Let the contribution of a large item of volume $w-t$ to the number of ways be $C$; then $C=\dbinom{i}{t}$, and the contributions of different large items add up. Even with equal volumes, different items are counted separately.
    
    Let $f_{i,j}$ be the minimum number of large items that, together with $i$ ones, gives exactly $j$ ways.
    
    Fix $i$, set $f_{i,0}=0$ and all other states to $+\infty$. Compute the unbounded-knapsack transition in increasing order of $j$:
    
    $$
    f_{i,j}=1+\min_{0\le t\le i;~C\le j}f_{i,j-C},\qquad 1\le j\le20000.
    $$
    
    Recording the $t$ that attains the minimum lets us recover the volume $w-t$ of each large item. Computing this for all $0\le k\le20000$ gives $\min_{1\le i\le 20}(i+f_{i,k})\le 29<40$, so this preprocessing range is sufficient.

??? note "Reference implementation"
    ```cpp
    --8<-- "docs/basic/code/construction/construction_1.cpp"
    ```
