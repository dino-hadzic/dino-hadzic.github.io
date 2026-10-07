---
title: DP of DP
---

## Introduction

This article introduces the idea of "DP of DP" and shows, through two examples, how it is applied to concrete problems.

## Idea

The so-called "DP of DP" actually refers to the method in which, during dynamic programming, the solution process of a subproblem (usually a DP) is abstracted into an automaton (DFA), and then a new layer of DP is designed on top of this automaton.

This technique is mainly applied to a class of **sequence counting**, **probability** or **expectation** problems. A typical problem has the following structure:

-   Given an alphabet $\Sigma$ and a set $A\subseteq\Sigma^n$ of "valid sequences" of length $n$ over it. Depending on the alphabet, the sequences may be binary strings, digit strings, state sequences, etc.
-   For every concrete sequence $s\in\Sigma^n$, dynamic programming can determine whether it is valid (i.e. $s\in A$), compute its weight or some related value.
-   Finally, we want to count the number of all sequences in $A$, their total weight, an expected value, etc.

Here, enumerating all sequences is infeasible. So we consider abstracting the process of "checking whether a sequence is valid" (i.e. the inner DP) into a [deterministic finite automaton](../misc/fsm.md#确定性有限状态自动机) (DFA). In general, for a fixed sequence $s\in\Sigma^n$, the state function of the inner DP can be written as $g(i,x;s)$, i.e. the value of some quantity when the prefix of $s$ of length $i$ has been processed and the other state components are $x$. Correspondingly, the state transition equation of the inner DP is

$$
g(i,\cdot;s) = G(g(i-1,\cdot;s),s_i).
$$

That is, the function $g(i,\cdot;s)$ is uniquely determined by the previous function $g(i-1,\cdot;s)$ and the current character $s_i$. If we regard the function $g(i,\cdot;s)$ as a state of the automaton, then the state transition equation of the inner DP gives a transition of the automaton. Therefore the automaton $(Q,\Sigma,\delta,q_0,F)$ corresponding to the inner DP has the following structure:

-   the state set $Q$ is the set of all functions $g(i,\cdot;s)$ for all possible $s\in\Sigma^n$ and $i=0,1,\cdots,n$;
-   the transition function $\delta:Q\times\Sigma\to Q$ is the $G$ in the state transition equation of the inner DP;
-   the start state $q_0$ is usually obvious, namely the initial state of the inner DP;
-   the set of accepting states $F$ corresponds to all valid sequences $s\in A$.

The function $g(i,\cdot;s)$ itself can be rather complex, so when handling concrete problems one usually needs [state compression](./state.md) or DFA minimization techniques to compress the state space. This is also the main reason why DP of DP can significantly reduce the time and space complexity compared to brute-force DP.

After abstracting the inner DP into a DFA, we can design a new DP on this DFA to solve the original problem, namely the outer DP. For ease of presentation, take a simple counting problem as an example. The state function of the outer DP is defined as $f(i,q)$, the number of prefixes of length $i$ that reach the state $q\in Q$ of the DFA. Its state transition equation is

$$
f(i,q) = \sum_{c\in\Sigma}\sum_{q'\in Q:\delta(q',c)=q} f(i-1,q').
$$

The initial value is of course $f(0,q_0)=1$, and the final answer can usually be computed easily from $\{f(n,q):q\in F\}$. The outer DP is in fact a special case of [DP on a DAG](./dag.md).

## Examples

The next two examples explain the general approach of DP of DP in detail.

### Example 1

???+ example "[Hero meet devil](https://www.luogu.com.cn/problem/P10614)"
    Given a string $S$ over the alphabet `ACGT` with $|S|\le 15$. For every $0\leq i \leq |S|$, count the strings $T$ of length $m$ over the alphabet `ACGT` whose longest common subsequence with $S$ has length $i$.

??? note "Solution"
    The first idea is a DP: let $f_{i,j}$ be the number of strings $T$ of length $i$ whose longest common subsequence with $S$ has length $j$. But this cannot be transitioned; the main problem is that we do not know which characters this longest common subsequence corresponds to.
    
    Consider the naive process of computing the longest common subsequence. Let $g_{i,j}$ be the length of the longest common subsequence of the first $i$ characters of $T$ and the first $j$ characters of $S$; then
    
    $$
    g_{i,j} = \max\{g_{i-1,j},g_{i,j-1},g_{i-1,j-1}+[T_i=S_j]\}.
    $$
    
    We observe that for a given $i$, recording the values of the one-dimensional array $g_i$ suffices to maintain exactly the state of the longest common subsequence of $S$ and the first $i$ characters of $T$. Since the length of $S$ is only $15$, this idea is feasible.
    
    So we redefine the state: $f_{i,x}$ is the number of strings $T$ of length $i$ whose DP array with respect to $S$ (i.e. $g_i$) is in state $x$. This DP seems to have many states, but we notice that $g_{i,j}-g_{i,j-1}\in\{0,1\}$, so we can maintain the difference array of $g_i$, and the number of states is $2^{|S|}$.
    
    Now consider the transition. It is easy to see that if we know the array $g_i$ and also $T_{i+1}$, we can compute $g_{i+1}$ via the naive LCS transition (the DP equation above). Thus the naive LCS becomes the inner DP that helps $f$ transition.
    
    Therefore we enumerate $T_{i+1}$, compute the state $x'$ that $x$ transitions to, and add $f_{i,x}$ to $f_{i+1,x'}$ to complete the state transition of the outer DP. Finally, let $\textit{ans}_i$ be the answer for LCS length $i$; enumerate every state $x$ and add $f_{m,x}$ to $\textit{ans}_{\operatorname{popcount}(x)}$.

??? note "Sample code"
    ```cpp
    --8<-- "docs/dp/code/dp-of-dp/dp-of-dp_1.cpp"
    ```

### Example 2

???+ example "[\[ZJOI2019\] Mahjong](https://loj.ac/p/3042)"
    Suppose mahjong tiles come in $n$ ranks, with $4$ tiles of each rank. Define a set (mentsu) as three tiles of consecutive ranks $i,i+1,i+2$ (a run) or three tiles of the same rank $i,i,i$ (a triplet), and a pair as two tiles of the same rank $i,i$. A sequence of mahjong tiles is winning if and only if it (viewed as a multiset) can be split into four sets and one pair, or into seven distinct pairs. Given the initial $13$ tiles, the remaining $4n-13$ tiles are shuffled uniformly at random and drawn one by one. Find the expected number of additional tiles drawn until there exists a winning subsequence, modulo $998244353$.

??? note "Solution"
    First, for a hand of tiles we only need to consider the count of each rank, not their order. Therefore, any prefix of any hand can be converted into a sequence of length $n$ with each position in $0\sim 4$. Initially the number of tiles of rank $i$ is $a_i$, which restricts the $i$-th number $x_i$ of the sequence to integers in $[a_i,4]$. Note that the converted sequence ignores the order of drawing, whereas the tile sequence in the problem takes the order into account.
    
    Let $X$ be the minimum number of draws after which the hand can win. Computing the expectation $\mathbf E[X]$ directly is rather hard, so consider the following transformation. Let $h_i$ be the number of ways to choose $i$ tiles from the remaining ones (different tiles of the same rank are considered distinct) such that the hand is **not winning**. In the corresponding tile sequence these $i$ tiles necessarily precede the remaining $(4n-13-i)$ tiles, but the order of these $i$ tiles and the order of the remaining $(4n-13-i)$ tiles are arbitrary, so the number of tile sequences in which drawing only the first $i$ tiles does not win is
    
    $$
    h_i\cdot i!(4n-13-i)!.
    $$
    
    Since the total number of tile sequences is $(4n-13)!$, the probability that drawing only the first $i$ tiles does not win is
    
    $$
    \mathbf P[X>i] = \dfrac{h_i\cdot i!(4n-13-i)!}{(4n-13)!}.
    $$
    
    Using the tail-sum formula we obtain the required expectation
    
    $$
    \mathbf E[X] = \sum_{i=0}^\infty\mathbf P[X>i] = 1 + \sum_{i=1}^{4n-13}\dfrac{h_i\cdot i!(4n-13-i)!}{(4n-13)!}.
    $$
    
    The problem has now been reduced to computing $h_i$. We solve it with the DP of DP method.
    
    First, consider the inner DP, i.e. using dynamic programming to decide whether a (converted) sequence corresponds to a winning hand. The seven-pairs case is easy, so we focus on the first form of winning. Let $g_{0/1,i,j,k}$ be the maximum number of sets after processing the first $i$ ranks, with $j$ groups $(i-1,i)$ and $k$ tiles of rank $i$ left over, and with no pair/a pair present (i.e. $0/1$). If running the DP on a sequence yields a $g_{1,n}$ containing a number greater than or equal to $4$, the sequence is winning.
    
    The state transition of this DP is rather complex. We discuss it in two steps. Step one: consider the transition of $g_{0/1,i}$. This means: when adding $x_i$ tiles of rank $i$ to the current hand without forming a new pair, how does the number of sets transition. Clearly, if after adding $x_i$ tiles of rank $i$ we want to get $\ell$ runs, $j$ groups $(i-1,i)$ and $k$ single tiles $i$, then we should transition from $(g_{0/1,i-1})_{\ell,j}$ (this choice avoids waste as much as possible), and use the remaining $(x_i-\ell-j-k)$ tiles to form as many triplets as possible. Enumerating all possibilities gives the following transition equation:
    
    $$
    \tilde G(g_{0/1,i-1}, x_i)_{j,k} = \max\left\{(g_{0/1,i-1})_{\ell,j} + \ell + \left\lfloor\dfrac{x_i-\ell-j-k}{3}\right\rfloor:\ell+j+k\le x_i\right\}.
    $$
    
    Step two: consider the case where a pair must be formed. When adding $x_i$ tiles of rank $i$ there are three transitions:
    
    -   add $x_i$ tiles to $g_{0,i-1}$ and transition to $g_{0,i}$;
    -   add $x_i$ tiles to $g_{1,i-1}$ and transition to $g_{1,i}$;
    -   if $x_i\ge 2$, add $x_i-2$ tiles to $g_{0,i-1}$ and transition to $g_{1,i}$.
    
    This gives all transitions from $g_{i-1}$ to $g_i$ by adding $x_i$ tiles.
    
    Having solved the state transition of the inner DP, we can build the **winning-hand automaton**. The transitions of the automaton are the transitions of the inner DP above; we also need to consider how to represent each state of the automaton. Each state corresponds to one possible value of $g_i$. It has three dimensions $(0/1,j,k)$. Since the $(i-1,i)$ and $i$ kept in the $j$ and $k$ dimensions are all used to form runs in the future, and three identical runs can always be rearranged into three triplets, we only need to consider the need for at most $2$ identical runs, so at most $2$ of each shape need to be kept, i.e. $j,k\in\{0,1,2\}$. Therefore $g_i$ can be represented as a $2\times 3\times 3$ array. In addition, to maintain the seven-pairs winning shape, each state also needs a counter for the maximum number of pairs that can currently be formed.
    
    The range of each element of the array $g_i$ may be $\{-\infty\}\cup\mathbf N$, but since a number of sets greater than or equal to $4$ is always a win, each element can be capped at $4$. Since a winning sequence stays winning after adding any tiles, we can use the idea of DFA minimization and compress all winning states into a single state. Therefore, for non-winning states, each position in $g_1$ only takes values in $\{-\infty\}\cup\{0,1,2,3\}$, and each position in $g_0$ takes values in $\{-\infty\}\cup\{0,1,2,3,4\}$. In the implementation, $-\infty$ is represented by $-1$.
    
    Even so, the number of possible states is still very large, $1+7\times 5^9\times 6^9$ in total. Enumerating them is not realistic. In fact, the vast majority of these possibilities never actually appear in a winning-hand automaton. To avoid considering states that do not actually exist, we can use the idea of BFS, starting from the initial state and expanding states step by step until we stop at the winning state. The resulting automaton has $N = 2092$ states.
    
    Finally, consider how to DP on the winning-hand automaton (the outer DP). Let $f_{i,j,k}$ be the number of ways to have processed the first $i$ ranks, drawn $j$ tiles in total, and arrived at state $k$ of the automaton. For the transition, enumerate the number of drawn tiles $0\leq t\leq 4-a_i$, where $a_i$ is the number of tiles of rank $i$ among the initial $13$, multiply the previous count by the number of ways $\dbinom{4-a_i}{t}$ to choose $t$ of the $4-a_i$ tiles, and accumulate. Formally:
    
    $$
    f_{i,j+t,k'} \gets f_{i,j+t,k'} + \dbinom{4-a_i}{t}f_{i-1,j,k}.
    $$
    
    Here $k'=\delta(k,a_i+t)$ is the state reached by adding $a_i+t$ tiles to state $k$ of the automaton. After the outer DP finishes, we can compute the number of ways to have drawn $i$ tiles and still not won, i.e.
    
    $$
    h_i=\sum_{k\notin F} f_{n,i,k},
    $$
    
    where $F$ is the set of winning states. Substituting into the expression above gives the required expectation.

??? note "Sample code"
    ```cpp
    --8<-- "docs/dp/code/dp-of-dp/dp-of-dp_2.cpp"
    ```

## Exercises

-   [CF979E Kuro and Topological Parity](https://codeforces.com/problemset/problem/979/E)
-   [\[TJOI2018\] Garden Party](https://loj.ac/p/2575)
-   [\[NOI2022\] Removing Stones](https://loj.ac/p/3848)
