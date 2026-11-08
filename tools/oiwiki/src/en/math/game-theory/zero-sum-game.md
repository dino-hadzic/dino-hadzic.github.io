---
title: Zero-sum games
---

Prerequisites: [Introduction to game theory](./intro.md)

This article discusses (two-player) [zero-sum games](./intro.md#zero-sum-and-non-zero-sum-games).

In a zero-sum game, the sum of the two players' payoffs is always zero, so one side's gain necessarily means the other side's loss. A zero-sum game can be regarded as a special case of a constant-sum game. Conversely, any constant-sum game can be equivalently transformed into a zero-sum game by adding or subtracting a constant from all payoffs of one side, so it suffices to discuss zero-sum games.

The zero-sum games commonly seen in algorithmic competitions can be roughly divided into two kinds: sequential zero-sum games and simultaneous zero-sum games.

## Sequential zero-sum games

In a sequential zero-sum game, the two players move alternately until the game ends.

In a sequential zero-sum game, the players' payoff function has a recursive structure. The positions $S$ of the game can be divided into three kinds: terminal positions $S_0$, positions $S_1$ where player $1$ moves, and positions $S_2$ where player $2$ moves. Suppose that at a terminal position $s\in S_0$ the payoff of player $1$ is $v(s)$, so that correspondingly the payoff of player $2$ is $-v(s)$. Therefore, when it is player $2$'s turn to move, maximizing their payoff is the same as minimizing the payoff of player $1$. Hence, assuming both sides play optimally, the maximum payoff $V(s)$ that player $1$ can obtain at position $s\in S$ satisfies the following recurrence:

$$
V(s) = \begin{cases}
v(s), & s \in S_0,\\
\max_{t\in s} V(t), & s\in S_1,\\
\min_{t\in s} V(t), & s\in S_2.
\end{cases}
$$

Here $t\in s$ means that $t$ is a successor position of $s$. This is exactly the [minimax idea](../../search/alpha-beta.md#minimax-algorithm).

When applying this algorithm to actual problems, the following concrete approaches are commonly used:

-   If the game involves only a small number of positions, it suffices to implement this algorithm directly by brute force.

-   If the game involves a very large number of positions with no special structure, one may consider [Alpha–Beta pruning](../../search/alpha-beta.md#alphabeta-pruning) combined with other search pruning techniques.

-   If a single position in the game is often a successor of several positions, one may consider memoized search or other dynamic programming algorithms to avoid repeated searching.

-   If the final payoff of a player in the game is the sum of the payoffs of all actions before the end of the game, the modeling can be optimized appropriately. Concretely, suppose that when a terminal position $s\in S_0$ is reached, the action sequences of players $i=1,2$ are $\{a^{(i)}_j\}_{j=1}^{k_i}$ respectively, the payoff of action $a$ is $w(a)$, and the payoff function of player $1$ is

    $$
    v(s) = \sum_{j=1}^{k_1}w(a_j^{(1)}) - \sum_{j=1}^{k_2}w(a_j^{(2)}).
    $$

    Then we can define $\tilde V(s)$ as the maximum difference between the payoff of the player to move and the payoff of their opponent in the part of the game after position $s\in S$. For the initial state $s_0$ in which player $1$ moves first, we have $V(s_0)=\tilde V(s_0)$, so computing $\tilde V(\cdot)$ suffices to solve the original problem. For $\tilde V(\cdot)$ we have the following recurrence:

    $$
    \tilde V(s) = \begin{cases}
    0, & s \in S_0, \\
    \max_{t\in s} \{w(a_{s\to t}) - \tilde V(t)\}, & s\in S_1\cup S_2.
    \end{cases}
    $$

    Here $a_{s\to t}$ denotes the action that moves the state from $s$ to $t$; if there are several such actions, the one with the highest payoff $w(a)$ is taken.

-   Impartial combinatorial games are all sequential zero-sum games: it suffices to set the payoffs of the winner and the loser to $+1$ and $-1$ respectively. Then the recurrence for the payoff function $V(\cdot)$ is in fact exactly the [lemma](./impartial-game.md#game-graph-and-states) that determines winning and losing positions.

    A common variant of such problems asks for the minimum number of moves the winner needs, or the maximum number of moves the loser can hold out. For this, it suffices to note that when we run a BFS from the terminal states and determine winning and losing positions according to the lemma, the BFS layer in which a position is determined to be winning or losing is exactly the required number of moves. This is because a position is determined to be winning as soon as one of its successors is a losing position, so it is always derived from the losing successor with the smallest layer number; while a position is determined to be losing only when all of its successors are winning positions, so it is always derived from the winning successor with the largest layer number.

    This method can likewise be generalized to general [directed graph games](./impartial-game.md#games-on-directed-graphs).

### Example problem

???+ example "[Codeforces 794 E. Choosing Carrot](https://codeforces.com/problemset/problem/794/E)"
    There is a sequence $\{a_i\}$ of length $n$. Two players, $1$ and $2$, alternately take a number from one of the two ends of the sequence until only the last number remains. The goal of player $1$ is to maximize this last remaining number, and the goal of player $2$ is to minimize it. Before the game officially starts, player $1$ may additionally make $k$ moves first. Assume both players play optimally throughout. For each $k = 0,1,2,\cdots,n-1$, find the number remaining at the end of the game. Here $1 \le n \le 3\times 10^5$.

??? note "Solution"
    No matter how the two sides take numbers, the remaining part of the sequence is always a contiguous interval, so a position in the game can be described just by the interval $[l,r]$ and the player $i=1,2$ to move, and the problem can be solved by dynamic programming. Let $f(l,r,i)$ be the number remaining at the end of the game when the position is described by $(l,r,i)$. From the analysis above, for $l < r$ this function satisfies the transition equations:
    
    $$
    \begin{aligned}
    f(l,r,1) &= \max\{f(l+1,r,2),f(l,r-1,2)\},\\
    f(l,r,2) &= \min\{f(l+1,r,1),f(l,r-1,1)\}.
    \end{aligned}
    $$
    
    The boundary condition is $f(l,l,1)=f(l,l,2) = a_l$. From this, the function values of all possible positions can be computed in $\Theta(n^2)$ time. For each $k$, the answer is
    
    $$
    g(k) = \max f(l,r,1) \text{ subject to } r - l + 1 = n - k.
    $$
    
    This algorithm cannot pass the constraints of the original problem, so we need to optimize the transitions. There are many ways to do this; here we present only one.
    
    View the transition equations as operations on the whole sequence. The two transition equations respectively mean taking the maximum and the minimum of adjacent numbers to obtain a new sequence; call them the "maximization operation" and the "minimization operation". Each operation shortens the sequence by one. All intervals of length $d$ give $(n-d+1)$ results in total, which corresponds to the sequence obtained by applying $(d-1)$ operations to the sequence. Moreover, to obtain the result $f(l,r,1)$, the last operation must be a maximization operation. Therefore, in these sequences of operations the two kinds of operations alternate, and the last one is always a maximization operation.
    
    Consider the change two consecutive operations make to the sequence. Without loss of generality, suppose the minimization operation is performed first and then the maximization operation. Then the sequence $a_1,a_2,a_3$ becomes
    
    $$
    \max\{\min\{a_1,a_2\},\min\{a_2,a_3\}\}.
    $$
    
    Enumerating all possible orderings of the three numbers $a_1,a_2,a_3$ shows that this expression always equals $a_2$, except in the case $a_1 < a_2$ and $a_2 > a_3$ (i.e., $a_2$ is a strict local maximum). In other words, if a sequence has no strict local maximum, the only effect of two consecutive operations on it is to delete one number from each end of the sequence. This obviously simplifies the transitions greatly. The only remaining question is: how to guarantee that the sequence has no strict local maximum? In fact, applying a maximization operation to the sequence once already guarantees that there is no strict local maximum. Hence, the results of all even numbers of operations can be obtained by taking the sequence obtained from the initial sequence by two operations and deleting pairs of numbers from both ends one pair at a time; the results of all odd numbers of operations can be obtained by taking the sequence obtained from the initial sequence by one operation and deleting pairs of numbers from both ends one pair at a time. (The case of zero operations, i.e., $k=n-1$, in which the answer is $\max_i a_i$, needs to be handled separately.)
    
    Since at most $3$ full operations on the sequence are needed, and computing the answers afterwards takes only $2$ passes, the total time complexity of the algorithm is $\Theta(n)$.

??? note "Reference code"
    ```cpp
    --8<-- "docs/math/code/zero-sum-game/zero-sum-game-1.cpp"
    ```

### Exercises

-   [Luogu P2734 \[USACO3.3\] 游戏 A Game](https://www.luogu.com.cn/problem/P2734)
-   [Luogu P4576 \[CQOI2013\] 棋盘游戏 (Board Game)](https://www.luogu.com.cn/problem/P4576)
-   [Luogu P7097 \[yLOI2020\] 牵丝戏 (Puppet Play)](https://www.luogu.com.cn/problem/P7097)
-   [Codeforces 388 C. Fox and Card Game](https://codeforces.com/problemset/problem/388/C)
-   [Codeforces 794 E. Choosing Carrot](https://codeforces.com/problemset/problem/794/E)
-   [Codeforces 1628 D2. Game on Sum (Hard Version)](https://codeforces.com/problemset/problem/1628/D2)
-   [Luogu P3210 \[HNOI2010\] 取石头游戏 (Stone Taking Game)](https://www.luogu.com.cn/problem/P3210)

## Simultaneous zero-sum games

In a simultaneous zero-sum game, the two players move at the same time.

Simultaneous zero-sum games are usually represented by a payoff matrix. Suppose the action set of player $i=1,2$ is $A_i$, and that when players $i=1,2$ take actions $a_i\in A_i$ respectively, the payoffs of the two players are $v(a_1,a_2)$ and $-v(a_1,a_2)$ respectively.

???+ example "Example"
    Consider the game of rock-paper-scissors. Suppose a win scores $1$ point, a loss scores $-1$ point, and a draw scores $0$ points. Then the payoffs of the two players in the game can be represented as
    
    $$
    \begin{pmatrix}
    0,0 & 1,-1 & -1,1 \\
    -1,1 & 0,0 & 1,-1 \\
    1,-1 & -1,1 & 0,0
    \end{pmatrix}.
    $$
    
    General two-player simultaneous games can also be represented in a similar form, which is why they are also called [bimatrix games](https://en.wikipedia.org/wiki/Bimatrix_game). For zero-sum games, since the payoff matrix of player $1$ and the payoff matrix of player $2$ are negatives of each other, it suffices to consider only the payoff matrix of player $1$:
    
    $$
    V = (v(a_1,a_2))_{(a_1,a_2)\in A_1\times A_2} = \begin{pmatrix}
    0 & 1 & -1 \\
    -1 & 0 & 1 \\
    1 & -1 & 0
    \end{pmatrix}.
    $$

The problem to solve is: given the payoff matrix $V = (v(a_1,a_2))_{(a_1,a_2)\in A_1\times A_2}$, how to find the optimal strategies and the maximum payoffs of the two players?

### Mixed strategies

Compared with sequential zero-sum games, the roles of the two players in a simultaneous game are symmetric. However, since we have already solved sequential zero-sum games, let us consider the sequential version of the simultaneous game. For example, if we assume that player $1$ acts first and player $2$ acts afterwards, then, by the discussion above, the payoff of player $1$ at the end of the game is given by

$$
w_-=\max_{a_1\in A_1}\min_{a_2\in A_2} v(a_1,a_2)
$$

Since the action of player $1$ is one-sidedly visible to player $2$, this should be the worst outcome player $1$ can obtain. Symmetrically, if we assume that player $2$ acts first, then the payoff of player $1$ is given by

$$
w_+ = \min_{a_2\in A_2}\max_{a_1\in A_1} v(a_1,a_2)
$$

Since the action of player $2$ is one-sidedly visible to player $1$, this should be the best outcome player $1$ can obtain. Player $1$ should expect to obtain a payoff $w\in[w_-,w_+]$ when the game is actually played. Although the inequality $w_-\le w_+$ always holds (for a proof see the [weak duality theorem](../linear-programming.md#duality-principle)), equality need not hold, so using only the analysis tools of sequential games, the outcome of the game generally cannot be uniquely determined.

???+ example "Example (continued)"
    In rock-paper-scissors, if the moves are made one after the other, the first player always loses and the second player always wins. In mathematical language, this is the following inequality:
    
    $$
    w_- = -1 \le +1 = w_+.
    $$
    
    Here $w_- = w_+$ does not hold.

The analysis above misses a key feature of simultaneous games: a player cannot accurately predict the opponent's action. Formally, this means that both sides may adopt some randomized strategy. This idea does not help in the context of sequential games, because no matter how the first player randomly chooses an action, the second player can always observe this action exactly and respond to it specifically. But in a simultaneous game, the strategic ambiguity introduced by a randomized strategy prevents the opponent from effectively targeting our action.

???+ example "Example (continued)"
    In rock-paper-scissors, if player $1$ chooses one of the three actions rock, scissors, paper uniformly at random, then, depending on the action of player $2$, the possible payoffs of player $1$ are
    
    $$
    \dfrac{1}{3}(0,1,-1)^T + \dfrac{1}{3}(-1,0,1)^T + \dfrac{1}{3}(1,-1,0)^T = (0,0,0)^T.
    $$
    
    Now, no matter how player $2$ chooses their action, the expected payoff of player $1$ is always $0$. This is clearly better than deterministically choosing a single action.

This leads to the concept of a mixed strategy.

???+ abstract "Mixed strategy"
    In a simultaneous game, a **mixed strategy** of player $i$, or **strategy** for short, is a function $s_i:A_i\to[0,1]$ satisfying $\sum_{a_i\in A_i}s_i(a_i)=1$. In other words, a strategy $s_i$ is a probability distribution on the action set $A_i$ of player $i$. The set of all mixed strategies of player $i$ is denoted by $S_i=\Delta(A_i)$, where $\Delta(A_i)$ denotes the set of all probability distributions on $A_i$. If $s_i$ is a degenerate probability distribution, i.e., there exists $a\in A_i$ with $s_i(a)=1$, then the strategy $s_i$ is also called a **pure strategy**.

The payoff of a mixed strategy is the expectation of the payoffs of the individual actions:

$$
v(s_1,s_2) = \sum_{a_1\in A_1}\sum_{a_2\in A_2}s_1(a_1)s_2(a_2)v(a_1,a_2).
$$

Viewing an individual action as the corresponding pure strategy, the action set $A_i$ can be embedded into the set of (mixed) strategies $S_i$, and the $v(s_1,s_2)$ defined by the formula above can be regarded as the extension of $v(a_1,a_2)$ from $A_1\times A_2$ to $S_1\times S_2$.

### Von Neumann's theorem

Once mixed strategies are introduced, the results of the maximin idea and the minimax idea coincide, and hence the outcome of a simultaneous zero-sum game is also uniquely determined.

???+ note "Theorem (von Neumann)"
    In a simultaneous zero-sum game allowing mixed strategies, if both sides play optimally, the maximum payoff of player $1$ is
    
    $$
    w = \max_{s_1\in S_1}\min_{s_2\in S_2} v(s_1,s_2) = \min_{s_2\in S_2}\max_{s_1\in S_1} v(s_1,s_2),
    $$
    
    and the maximum payoff of player $2$ is $-w$.

??? note "Proof"
    Let $w = \max_{s_1\in S_1}\min_{s_2\in S_2} v(s_1,s_2)$. Consider the inner minimization problem. Since $v(s_1,s_2)=\sum_{a_2\in A_2}s_2(a_2)v(s_1,a_2)$, we have $\min_{s_2\in S_2}v(s_1,s_2)=\min_{a_2\in A_2}v(s_1,a_2)$, and the pure strategy corresponding to an optimal solution of the latter is an optimal solution of the former. Therefore, $w = \max_{s_1\in S_1}\min_{a_2\in A_2} v(s_1,a_2)$. Then, introducing an auxiliary variable $u$, the problem can be rewritten as
    
    $$
    w = \max_{u,s_1} u \text{ subject to }u \le \min_{a_2\in A_2} v(s_1,a_2).
    $$
    
    This constraint is equivalent to $u\le v(s_1,a_2)$ holding for all $a_2\in A_2$. Finally, substituting the definition of the mixed strategy $s_1$ and the expression for the payoff function $v(s_1,a_2)$, the original problem is equivalent to the [linear programming problem](../linear-programming.md)
    
    $$
    (P) \qquad
    \begin{aligned}
    w = \max_{u,s_1}\; & u\\
    \text{subject to }& \sum_{a_1\in A_1}s_1(a_1)v(a_1,a_2) \ge u,~\forall a_2\in A_2,\\
    & \sum_{a_1\in A_1}s_1(a_1) = 1,\\
    & s_1(a_1) \ge 0,~\forall a_1\in A_1.
    \end{aligned}
    $$
    
    This problem is clearly feasible and its objective function is bounded, so an optimal solution exists. By the [duality principle](../linear-programming.md#duality-principle), its optimal value equals the optimal value of the dual problem:
    
    $$
    (D) \qquad
    \begin{aligned}
    w = \min_{t,s_2}\; & t\\
    \text{subject to }&\sum_{a_2\in A_2}s_2(a_2)v(a_1,a_2) \le t,~\forall a_1\in A_1,\\
    &\sum_{a_2\in A_2}s_2(a_2) = 1,\\
    &s_2(a_2)\ge 0,~\forall a_2\in A_2.
    \end{aligned}
    $$
    
    Repeating the steps above, this problem is equivalent to $\min_{s_2\in S_2}\max_{s_1\in S_1}v(s_1,s_2)$. This proves the theorem.

The optimal strategies of the two sides form a [Nash equilibrium](https://en.wikipedia.org/wiki/Nash_equilibrium) of this game. That is, assuming both sides choose the optimal strategies in the equilibrium, no player can strictly benefit by unilaterally deviating from the equilibrium strategy.

### Reduction to a linear programming problem

The proof of von Neumann's theorem also shows how to solve simultaneous zero-sum games. Let $n$ and $m$ be the numbers of actions available to players $1$ and $2$ respectively. Given the payoff matrix $V\in\mathbf R^{n\times m}$ of player $1$, we can solve the following linear programming problem:

$$
\begin{aligned}
w = \max_{(u,s)\in\mathbf R\times\mathbf R^n}\; & u\\
\text{subject to }& V^Ts \ge u\mathbf 1,\\
& \mathbf 1^Ts = 1,\\
& s \ge 0.
\end{aligned}
$$

This is a linear programming problem with $n+1$ variables and $m+1$ constraints (not counting the nonnegativity constraints), which can be solved efficiently by the [simplex method](../simplex.md). Since $u$ may be negative, one can first add the same constant $c$ to all entries of $V$ so that they all become positive, which allows requiring $u\ge 0$; this does not change the optimal strategy, and the obtained $w$ minus $c$ is the value of the original game. The optimal solution $s$ obtained by the algorithm is the optimal (mixed) strategy of player $1$. To obtain the optimal strategy of player $2$, it suffices to read off the dual variables (i.e., the shadow prices) of the optimal solution of this problem from the simplex tableau.

### Exercises

-   [Luogu P4232 无意识之外的捉迷藏 (Hide-and-Seek Beyond Consciousness)](https://www.luogu.com.cn/problem/P4232)

## References and notes

-   [Zero-sum game - Wikipedia](https://en.wikipedia.org/wiki/Zero-sum_game)
-   [Minimax theorem - Wikipedia](https://en.wikipedia.org/wiki/Minimax_theorem)
