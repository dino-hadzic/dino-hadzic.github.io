---
title: Range min/max operations & historical range extremes
---

This article explains the problem of maintaining historical range extremes with a segment tree, described by Ji Ruyi (吉老师) in the [2016 Chinese national training team paper](https://github.com/OI-wiki/libs/blob/master/%E9%9B%86%E8%AE%AD%E9%98%9F%E5%8E%86%E5%B9%B4%E8%AE%BA%E6%96%87/%E5%9B%BD%E5%AE%B6%E9%9B%86%E8%AE%AD%E9%98%9F2016%E8%AE%BA%E6%96%87%E9%9B%86.pdf).

## Range extremes

Broadly speaking, a range extreme operation means replacing all numbers in the interval $[l,r]$ by their $\max$ or $\min$ with $x$, i.e. $a_i=\max(a_i,x)$ or $a_i=\min(a_i,x)$.

???+ note "[HDU5306 Gorgeous Sequence](https://acm.hdu.edu.cn/showproblem.php?pid=5306)"
    Maintain a sequence $a$ and perform the following operations:
    
    1.  `0 l r t` $\forall l\le i\le r,~ a_i=\min(a_i,t)$.
    2.  `1 l r` output $\max\limits_{i=l}^r a_i$.
    3.  `2 l r` output $\sum\limits_{i=l}^r a_i$.
    
    Multiple test cases; it is guaranteed that $T\le 100,~\sum n,\sum m\le 10^6$.

Taking the range $\min$ means that only the numbers greater than $t$ change. So the object of this operation is no longer the whole interval but "the numbers in this interval greater than $t$". Hence the idea: each node maintains the maximum $Max$ of its interval, the second maximum $Se$, the interval sum $Sum$ and the number of maxima $Cnt$. Now consider the operation of taking the $\min$ with $t$ over an interval.

1.  If $Max\le t$, this $t$ obviously has no effect; return directly.
2.  If $Se<t < Max$, then $t$ changes exactly the maximum of the current interval. So we add $Cnt(t-Max)$ to the interval sum, then set $Max$ to $t$ and apply a tag.
3.  If $t\le Se$, we do not know how many numbers are affected by the update. So our strategy is: brute-force recurse downward and perform the operation, then push the information upward.

What is the complexity of this algorithm? Potential analysis yields a complexity of $O(m\log n)$. See the paper for the detailed analysis.

```cpp
--8<-- "docs/ds/code/seg-beats/seg-beats_1.cpp"
```

???+ note "[BZOJ4695 最假女选手](https://loj.ac/p/6565)"
    Maintain a sequence $a$ and perform the following operations:
    
    1.  `1 l r x` $\forall l\le i\le r,~ a_i=a_i+x$.
    2.  `2 l r x` $\forall l\le i\le r,~ a_i=\max(a_i,x)$.
    3.  `3 l r x` $\forall l\le i\le r,~ a_i=\min(a_i,x)$.
    4.  `4 l r` output $\sum\limits_{i=l}^r a_i$.
    5.  `5 l r` output $\max\limits_{i=l}^r a_i$.
    6.  `6 l r` output $\min\limits_{i=l}^r a_i$.
    
    $n,m\le 5\times 10^5,~|a_i|\le 10^8$. All type $1$ operations have $|x|\le 10^3$; the other operations satisfy $|x|\le10^8$.

With the same method we maintain the maximum, the second maximum, the number of maxima, the minimum, the second minimum, the number of minima and the interval sum. Besides this information we also need to maintain tags for range $\max$, range $\min$ and range addition. Compared to the previous problem, this raises the issue of the order in which tags are pushed down. We adopt the following strategy:

1.  The range addition tag has the highest priority; the other two tags are of equal standing.
2.  When applying an addition tag $v$ to a node, besides using $v$ to update the auxiliary information and the range addition tag of the current node, we also use this $v$ to update the range $\max$ and range $\min$ tags.
3.  When taking the $\min$ with $v$ on a node (ignoring the brute-force search here and assuming the tag satisfies the condition for being applied), besides updating the auxiliary information, we compare with the range $\max$ tag. If $v$ is smaller than the range $\max$ tag, all numbers will eventually become $v$, so set the range $\max$ tag to $v$ as well. Otherwise do nothing.
4.  Taking the range $\max$ with $v$ is analogous.

When maintaining the information, if there is only one or two numbers, the sets may overlap – for example a number may be both the maximum and the second minimum – which requires special handling.

```cpp
--8<-- "docs/ds/code/seg-beats/seg-beats_2.cpp"
```

Ji Ruyi proved that the complexity of this algorithm is $O(m\log^2 n)$.

???+ note "Mzl loves segment tree"
    Two sequences $A,B$; initially all numbers in $B$ are $0$. The operations to maintain are:
    
    1.  range $\min$ on $A$;
    2.  range $\max$ on $A$;
    3.  range addition on $A$;
    4.  query the range sum of $B$.
    
    After each operation, if the value of $A_i$ changed, add $1$ to $B_i$. $n,m\le 3\times 10^5$.

First consider the easiest operation, range addition. As long as $x\neq 0$, every number in the interval changes, so it suffices to perform one range addition on $B$.

For the range extreme operations, you find that applying and pushing down tags corresponds one-to-one with the array $B$. Essentially you divide the numbers of the sequence into three classes: maxima, minima and non-extremes, and maintain them separately (you just do not build the concrete sets of extremes, but this does not hinder the maintenance operations). Therefore, when applying a tag, update the information of $B$ along the way (note: do not apply a tag to $B$! Update the information!). When querying, you query on $A$ and update the information of $B$ while pushing down tags. After finding the required nodes, return the information of $B$. This operation essentially hands the information about extremes over to $B$ for maintenance. The overlap of the sets must still be handled as well.

???+ note "[CTSN loves segment tree](https://www.luogu.com.cn/problem/U180387)"
    Maintain two sequences $a,b$ and perform the following operations:
    
    1.  `1 l r x` $\forall l\le i\le r,~ a_i=\min(a_i,x)$.
    2.  `2 l r x` $\forall l\le i\le r,~ b_i=\min(b_i,x)$.
    3.  `3 l r x` $\forall l\le i\le r,~ a_i=a_i+x$.
    4.  `4 l r x` $\forall l\le i\le r,~ b_i=b_i+x$.
    5.  `5 l r` output $\max\limits_{i=l}^r (a_i+b_i)$.
    
    $n,m\le 3\times 10^5,~|a_i|,|b_i|,|x|\le 10^9$.

We divide the candidate answers $A_i+B_i$ in the interval $[l,r]$ into four classes: neither $A_i$ nor $B_i$ is a range maximum of the sequences $A,B$; $A_i$ is a range maximum of $A$ but $B_i$ is not a range maximum of $B$; $A_i$ is not a range maximum of $A$ but $B_i$ is a range maximum of $B$; both $A_i$ and $B_i$ are range maxima of $A,B$. Denote them by $C_{0,0},C_{1,0},C_{0,1},C_{1,1}$ respectively. In addition we maintain the range maximum and second maximum of the sequences $A,B$ as usual. The handling of the maximum and second maximum of $A,B$ when pushing down range addition tags and $\min$ tags is the same as in the two examples above. A $\min$ tag on $A$ affects $C_{1,1}$ and $C_{1,0}$, a tag on $B$ affects $C_{1,1}$ and $C_{0,1}$. Addition on $A,B$ affects all of $C_{0,0},C_{1,0},C_{0,1},C_{1,1}$. One only needs to be careful with the boundary cases where $C_{0,0},C_{1,0},C_{0,1}$ do not exist (e.g. in the interval $[i,i]$ only the maxima of $A,B$ and $C_{1,1}$ exist).

Next we need to consider how to maintain $C_{0,0},C_{1,0},C_{0,1},C_{1,1}$ during pushup. After updating the maxima of $A,B$, we discuss whether the maxima of $A,B$ in the left and right children equal the maxima of $A,B$ of the current node. We explain using the left child as an example; the right child is handled similarly:

-   When both the $A$ and $B$ maxima of the left child equal the $A,B$ maxima of the current node, the $C_{0,0},C_{1,0},C_{0,1},C_{1,1}$ of the left child contribute to the $C_{0,0},C_{1,0},C_{0,1},C_{1,1}$ of the current node respectively.
-   When the $A$ maximum of the left child equals the $A$ maximum of the current node but the $B$ maximum does not, the $C_{1,0},C_{1,1}$ of the left child contribute to the $C_{1,0}$ of this node, and $C_{0,0},C_{0,1}$ contribute to the $C_{0,0}$ of this node.
-   When the $A$ maximum of the left child does not equal the $A$ maximum of the current node but the $B$ maximum does, the $C_{0,1},C_{1,1}$ of the left child contribute to the $C_{0,1}$ of this node, and $C_{0,0},C_{1,0}$ contribute to the $C_{0,0}$ of this node.
-   When neither the $A$ nor the $B$ maximum of the left child equals the $A,B$ maxima of the current node, the $C_{0,0},C_{1,0},C_{0,1},C_{1,1}$ of the left child contribute only to the $C_{0,0}$ of this node.

The $\max(C_{0,0},C_{1,0},C_{0,1},C_{1,1})$ of the range query result is the answer.

Since range $\min$ and range addition must be maintained simultaneously, the complexity is still $O(m\log^2 n)$.

```cpp
--8<-- "docs/ds/code/seg-beats/seg-beats_4.cpp"
```

### Summary

In this chapter we gave four example problems, explaining respectively the maintenance of basic range extreme operations, the handling of priorities among several tags, the idea of classifying sets of numbers, and the maintenance of several classes. Essentially, the basic idea of handling range extremes is the classified maintenance of information about sets of numbers and their efficient merging. In the next chapter we discuss problems related to historical range extremes.

## Historical extreme problems

### Historical extremes are not persistence

Note that the historical extreme problems discussed in this chapter differ from the so-called persistent data structures. We call this special class of problems historical extreme problems. They can be divided into three kinds.

#### Historical maximum

Simply put, the historical maximum of a position is the maximum of all numbers that have ever appeared at that position. Formally, we define an auxiliary array $B$, initially identical to $A$. After every operation on $A$, we take the $\max$ over the whole array:

$$
\forall i\in[1,n],\ B_i=\max(B_i,A_i)
$$

Then we call $B_i$ the historical maximum of this position.

#### Historical minimum

The definition is similar to the historical maximum: after every operation on $A$, we take the $\min$ over the whole array. Then we call $B_i$ the historical minimum of this position.

#### Historical version sum

The auxiliary array $B$ is initially all $0$. After every operation, we add the whole array $A$ onto the array $B$:

$$
\forall i\in[1,n], \ B_i=B_i+A_i
$$

We call $B_i$ the historical version sum at position $i$.

Next, we divide historical extreme problems into four classes for discussion.

### Problems solvable with tags

???+ note "[CPU 监控](https://www.luogu.com.cn/problem/P4314)"
    The sequences $A,B$ are initially identical:
    
    1.  range assignment of $x$ on $A$;
    2.  range addition of $x$ on $A$;
    3.  query the range $\max$ of $A$;
    4.  query the range $\max$ of $B$.
    
    After every operation we perform an update $\forall i\in [1,n],\ B_i=\max(B_i,A_i)$. $n,m\le 10^5$.

Let us first ignore operation 1. Then there is only range addition; we maintain a tag $Add$ denoting the value added to the current interval, and this tag solves the range $\max$ problem. Next consider the historical range $\max$. We define a tag $Pre$ with the meaning: the historical maximum of the $Add$ tag during the lifetime of this tag.

This definition may be rather vague, so let us first explain the lifetime of a tag. A tag goes through the following process:

1.  it is created at node $u$;
2.  while node $u$ receives several new tags, it is merged with them (tags of the same kind);
3.  the tag of node $u$ is pushed down to the children of $u$, and the tag of $u$ is cleared.

We regard the period from step 1 up to (but not including) step 3 as the lifetime of the tag of node $u$. When two tags are merged into one, their lifetimes are merged as well (i.e. the earlier creation time is taken as the start of the lifetime). An equivalent formulation: it is the time period from the moment the tag of this node was last pushed down to the current moment.

Why define the lifetime? Using this concept we can prove: during the lifetime of a node's tag, its children do not change at all and remain in the state they had before this lifetime. The reason is simple: during this period you have not pushed down any tags.

Therefore you can guarantee that the historical maximum of $Add$ during the lifetime of the current tag can be applied to the tags and information of the children, because the tags and information of the children have not changed during this time period. So when pushing the tag of $u$ down to its child $s$, it is easy to see that

$$
Pre_s=\max(Pre_s,Pre_u+Add_s),Add_s=Add_u+Add_s
$$

Updating the information is similar: just update with the corresponding tag.

Next, we consider operation 1.

A range assignment turns all numbers into one number. After that, whether range addition or assignment follows, all numbers in the interval remain the same number (unless you end the lifetime of the current tag by pushing it down). Therefore we can regard all tags after the first range assignment as range assignment tags. That is, the lifetime of a tag is roughly divided into two phases:

1.  merging of several addition tags, without having received an assignment tag;
2.  an assignment tag, with no addition tags (addition tags are converted into assignment tags).

So we split the Pre tag of this node into $(P_1,P_2)$: $P_1$ denotes the maximum addition tag of the first phase, $P_2$ the maximum assignment tag of the second phase. Using a similar method we can push down tags and update information. The time complexity is $O(m\log n)$ (this problem has no range extreme operations with $x$!).

```cpp
--8<-- "docs/ds/code/seg-beats/seg-beats_3.cpp"
```
