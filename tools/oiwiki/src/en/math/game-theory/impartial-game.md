---
title: Impartial games
---

Prerequisites: [Introduction to game theory](./intro.md)

This article discusses [impartial games](./intro.md#公平组合博弈).

Among impartial games, the most basic and most important one is normal Nim. The Sprague–Grundy theorem states that every impartial game under the normal play rule is equivalent to a single-pile Nim game. From this, the concepts of the Sprague–Grundy function and nimbers can be developed, which completely characterize an impartial game under the normal play rule. Therefore, this article first establishes the results on normal Nim and the Sprague–Grundy theory. After that, it discusses some impartial games that commonly appear in algorithm competitions.

Finally, this article briefly discusses misère Nim. Misère games are much more complicated than normal games and rarely appear in algorithm competitions. Unless stated otherwise, all games mentioned in this article are assumed to be normal impartial games.

???+ info "“State”, “position” and “game”"
    This article uses these three words interchangeably. In game theory, the state of a game usually includes all information that may be relevant to the game up to a certain moment of the game. In the general setting, the state of a game usually includes the past actions of both players, the values of random variables that have already been realized, the content of the information known to both players, and so on. The position of a game is, relatively speaking, not a standard term of game theory; it usually refers to the situation that both players face at a certain moment of the game, e.g. the placement of the pieces in a board game. Only for impartial games (or, more generally, zero-sum, deterministic, perfect-information games), since the game involves no randomness and the set of future actions of the players and the payoff functions do not depend on the history leading to the current position (i.e. the previous actions of both players), there is no difference between the state and the position of the game, and both can be regarded as a node of the game graph. Since a game can always be described by its initial position, the word “position” is sometimes also used directly to refer to the game itself.

## Nim

The rules of Nim are very simple:

???+ abstract "Nim"
    There are $n$ piles of stones, and the $i$-th pile has $a_i$ stones. Two players alternately remove any number of stones from any single pile, but they may not pass. The player who removes the last stone wins.

It is easy to verify that Nim is an impartial game under the normal play rule.

???+ example "Example"
    Here is an example. Currently there are $3$ piles of stones, with $2,5,4$ stones respectively. Then one may remove $2$ stones from pile $1$, and the position becomes $0, 5, 4$; or one may remove $4$ stones from pile $2$, and the position becomes $2, 1, 4$. If at some moment the position becomes $0, 0, 5$ and it is player A's turn, then A can remove the $5$ stones of pile $3$, i.e. remove the last stone, and A wins.

### Game graph and states

In Nim, the possible changes of the position can be described by a game graph.

Regard every possible state as a node of a graph, and draw an edge from each state to its successor states (i.e. the states reachable by one move); this yields a directed acyclic graph, which is the game graph. The graph is acyclic because in Nim every move strictly decreases the total number of stones.

???+ example "Example"
    For example, for the Nim game whose initial position has $3$ piles with $1,1,2$ stones respectively, the following game graph can be drawn:
    
    ![Example of a game graph](./images/nim.svg)
    
    As will be mentioned shortly, the red nodes in the figure denote winning states and the black nodes denote losing states.

Since Nim is an impartial game, whether a player has a winning strategy depends only on the current state of the game, not on the identity of the player. Therefore, all states can be divided into **winning states** (for the player to move) and **losing states** (for the player to move), denoted by $\mathcal N$-states and $\mathcal P$-states respectively[^n-vs-p]. This definition applies to all impartial games.

By the following lemma, all states can be labeled inductively as winning or losing states:

???+ note "Lemma"
    In an impartial game under the normal play rule,
    
    1.  a state with no successor states is a losing state $\mathcal P$,
    2.  a state is a winning state $\mathcal N$ if and only if at least one of its successor states is a losing state $\mathcal P$,
    3.  a state is a losing state $\mathcal P$ if and only if all of its successor states are winning states $\mathcal N$.

??? note "Proof"
    For the first item, if the player currently has no available move, then the player has already lost the game.
    
    For the second item, if the state has at least one successor state that is a losing state, then the player can move to that losing state; the opponent then faces a state that is losing for the player to move, so the player wins.
    
    For the third item, if no successor state is a losing state, then no matter what, the player can only move to a winning state; the opponent then faces a state that is winning for the player to move, so the player loses the game.

In all impartial games, the game graph is a directed acyclic graph. Hence, by these three properties, after drawing the game graph one can compute in $O(|V|+|E|)$ time whether each state is a winning or a losing state. Here $|V|$ is the number of states of the game graph and $|E|$ is the number of edges, i.e. the total number of moves available from all states.

This lemma can be generalized to misère games and to the case where the directed graph may contain cycles. See the section [Games on directed graphs](#games-on-directed-graphs) for the related discussion.

### Nim-sum

Let us continue studying Nim.

By drawing the game graph, one can determine whether a given position is a first-player win. However, this takes $\Omega(\prod_{i=1}^n(a_i+1))$ time, which is too slow to be practical. In fact, one can observe that whether a state of Nim is a first-player win depends only on the Nim-sum of the numbers of stones in the current position.

???+ abstract "Nim-sum"
    The **Nim-sum** of natural numbers $a_1,a_2,\cdots,a_n$ is defined as $a_1\oplus a_2\oplus\cdots\oplus a_n$.

The Nim-sum is simply the [exclusive or (xor) operation](../bit.md#bitwise-operations).

???+ note "Theorem"
    In Nim, the state $(a_1,a_2,\cdots,a_n)$ is a losing state $\mathcal P$ if and only if the Nim-sum
    
    $$
    a_1\oplus a_2\oplus\cdots\oplus a_n = 0.
    $$

??? note "Proof"
    Apply induction over all possible states:
    
    1.  If $a_i=0$ for all $i=1,\cdots,n$, the state has no successor states and its Nim-sum equals $0$, so the claim holds.
    2.  If $k = a_1\oplus a_2\oplus\cdots\oplus a_n\neq 0$, then we need to show that the state is a winning state. That is, we need to construct a legal move such that the successor state is a losing state; by the induction hypothesis, it suffices to show that the successor state satisfies $a'_1\oplus a'_2\oplus\cdots\oplus a'_n=0$. By the properties of the Nim-sum (i.e. xor), this is equivalent to saying that there is an $i$-th pile from which some stones can be removed so that its size becomes $a_i\oplus k$, i.e. $a_i>a_i\oplus k$.
    
        Indeed, let the highest $1$ in the binary representation of $k$ be at bit $d$. Then there must be some $a_i$ whose binary bit $d$ is $1$. For the corresponding pile, we must have $a_i>a_i\oplus k$, because bit $d$ of $a_i\oplus k$ is $0$ and the higher bits are the same as those of $a_i$.
    3.  If $a_1\oplus a_2\oplus\cdots\oplus a_n= 0$, then we need to show that the state is a losing state. By the induction hypothesis, it suffices to show that the Nim-sums of all its successor states are not $0$. This is necessarily the case: any legal move changes $a_i$ to $a'_i\neq a_i$, which necessarily changes the Nim-sum to $a'_i\oplus a_i\neq 0$.

Hence, whether a state of Nim is a first-player win can be determined in $O(n)$ time.

## Sprague–Grundy theory

The Sprague–Grundy theory states that every impartial game under the normal play rule is equivalent to a single-pile Nim game. The main scenario where this result is applied is when the game consists of several mutually independent subgames. In that case, the state of the game can be determined by computing the Nim-sum of the SG function values of the subgames. If the game itself does not have such a structure, then to determine winning and losing states it suffices to apply the lemma of the previous section [Game graph](#game-graph-and-states).

### Notation for games

As explained above, every impartial game can be described by drawing its game graph. Since in the game graph the properties of each state are determined only by its successor states, a state $S$ in the game graph can be represented by the set of its successor states.

???+ example "Example (continued)"
    Taking the game graph above as an example, we obtain the following representation of the states:
    
    $$
    \begin{aligned}
    S_{0,0,0} &= \{\},\\
    S_{0,1,0} &= \{S_{0,0,0}\} = \{\{\}\},\\
    S_{0,0,1} &= \{S_{0,0,0}\} = \{\{\}\},\\
    S_{0,0,2} &= \{S_{0,0,0},S_{0,0,1}\} = \{\{\},\{\{\}\}\},\\
    S_{0,1,1} &= \{S_{0,1,0},S_{0,0,1}\} = \{\{\{\}\}\},\\
    S_{0,1,2} &= \{S_{0,0,2},S_{0,1,0},S_{0,1,1}\} = \{\{\{\},\{\{\}\}\},\{\{\}\},\{\{\{\}\}\}\}.
    \end{aligned}
    $$
    
    Here $S_{0,1,0}=S_{0,0,1}$.

A game can be represented by its initial state.

Although the representation of an impartial game can be quite complicated, single-pile Nim is relatively much simpler. When there is only one pile with $n$ stones, it can be represented as

$$
*0 = \{\},~*n = \{*m : m<n,~m\in\mathbf N\} = \{*0,*1,\cdots,*(n-1)\}.
$$

Here the notation $*n$ denotes (the initial state of) the single-pile Nim game with $n$ stones.

???+ example "Example (continued)"
    With this notation, the states in the example above can be written simply as
    
    $$
    S_{0,0,0} = *0,~
    S_{0,1,0} = S_{0,0,1} = *1,~
    S_{0,0,2} = *2,~
    S_{0,1,1} = \{*1\},~
    S_{0,1,2} = \{*1, *2, \{*1\}\}.
    $$

In the following discussion, the notation $T\in S$ should be understood as: state $T$ is a successor state of state $S$.

### Sums and equivalence of games

The equivalence relation of games relies on the concept of the sum of games[^more-sums].

???+ note "Sum of games"
    The **sum** of games $G$ and $H$, also called the **combined game**, denoted $G+H$, is the game
    
    $$
    G + H = \{g + H : g \in G\} \cup \{G + h : h \in H\}.
    $$

The sum of games can be understood as a game consisting of two subgames played simultaneously without interfering with each other; in each move a player can and must choose exactly one of the subgames and make one move in it, and the game ends when no move is possible in either subgame. The concept of the sum of games can be generalized to any number of games, and it is associative and commutative – that is, the result of combining several games does not depend on the order in which they are combined or on the order of the games. Nim is the sum of several single-pile Nim games.

One observation is that although in single-pile Nim every state except the one with no stones is a first-player win, these different single-pile Nim games do not yield the same game when combined with other single-pile Nim games. For example, the game $*n$ yields a losing game only when combined with another $*n$; combined with any other single-pile Nim game $*n'\neq *n$, it yields a winning game.

The lesson of this observation is that the properties of a game can be studied by examining its sums with other games. This leads to the concept of equivalence of games.

???+ abstract "Equivalence relation of games"
    If for all games $H$ the games $G_1+H$ and $G_2+H$ are both losing states or both winning states, then the games $G_1$ and $G_2$ are called **equivalent**, denoted $G_1\approx G_2$.

It is easy to verify that $\approx$ defined this way is indeed an [equivalence relation](../order-theory.md#二元关系) on the set of all impartial games.

### Sprague–Grundy function

The analysis of Nim shows that different single-pile Nim games are not equivalent to each other. However, every impartial game is equivalent to some single-pile Nim game. Hence, every impartial game can be assigned a number; this is the Sprague–Grundy function.

To prove these results, we first need to establish two lemmas about the equivalence relation of games. First, combining a losing game with any game yields a game equivalent to the original one.

???+ note "Lemma 1"
    For a game $G$ and any losing game $A\in\mathcal P$, we have $G\approx G + A$.

??? note "Proof"
    By definition, it suffices to show that for any game $H$, the games $G+H$ and $G+A+H$ are both losing states or both winning states.
    
    If the game $G+H$ has a winning strategy, then the game $G+A+H$ also has a winning strategy. If the opponent moves in the subgame $A$, move in the subgame $A$ to restore it to a losing state; otherwise, move according to the winning strategy of the game $G+H$. This guarantees the final victory.
    
    If the game $G+H$ is a losing game, then the game $G+A+H$ is also a losing game. This is because whether the move in this turn is made in the subgame $G+H$ or in the subgame $A$, the opponent can restore the corresponding subgame to a losing state in the next turn. In the end, the first player cannot win.

Second, two games are equivalent if and only if their sum is a losing game. This lemma provides a method for proving that two games are equivalent.

???+ note "Lemma 2"
    The games $G$ and $G'$ are equivalent if and only if $G+G'\in\mathcal P$ is a losing game.

??? note "Proof"
    If the games $G$ and $G'$ are equivalent, then $G+G'$ and $G+G$ are both winning or both losing, and the game $G+G$ is a losing game. This is because for any move of the first player, the second player can make the same move in the other subgame, so in the end the first player is the one who cannot move.
    
    Conversely, if $G+G'$ is a losing game, then by Lemma 1, $G\approx G+(G+G') = (G+G)+G' \approx G'$.

Using these lemmas, we obtain the following theorem:

???+ note "Theorem (Sprague–Grundy)"
    For any (finite) impartial game $G$, there exists $n\in\mathbf N$ such that $G\approx *n$.

??? note "Proof"
    To prove the conclusion of the theorem, we apply mathematical induction. Let the game be $G = \{G_1,G_2,\cdots,G_k\}$. By the induction hypothesis, there exist $n_1,n_2,\cdots,n_k$ such that $G_i\approx *n_i$; then we may consider the game
    
    $$
    G' = \{*n_1,*n_2,\cdots,*n_k\}.
    $$
    
    We will show that $G'\approx *m$, where $m=\operatorname{mex}\{n_1,n_2,\cdots,n_k\}$ is the smallest natural number not appearing in the set.
    
    In the first step, we need to show that $G\approx G'$. By Lemma 2, it suffices to show that the game $G+G'$ is a losing game. Without loss of generality, assume $G\neq *0$. If the first player chooses $G_i$, then the second player can choose $*n_i$; conversely, if the first player chooses $*n_i$, the second player can choose $G_i$. In either case, after these two moves the game becomes $G_i+*n_i$, which is a losing game by Lemma 2 and $G_i\approx *n_i$. This proves $G\approx G'$.
    
    In the second step, we need to show that $G'\approx*m$. By Lemma 2, it suffices to show that $G'+*m$ is a losing game. Without loss of generality, assume $G'\neq *0$. If the first player chooses $*n_i\in *m$, then by the definition of $m$ the second player can choose $*n_i\in G'$, turning the position into $*n_i + *n_i\in\mathcal P$, and the first player loses. If the first player chooses $*n_i\in G'$ with $n_i<m$, then the second player can choose $*n_i\in *m$, and the position likewise becomes $*n_i+*n_i\in\mathcal P$, and the first player loses. Finally, if the first player chooses $*n_i\in G'$ with $n_i>m$, then the second player can choose $*m\in *n_i$, turning the position into $*m+*m\in\mathcal P$, and the first player loses. This proves $G'\approx *m$.
    
    By the transitivity of the equivalence relation, $G\approx *m$. This completes the induction and proves that every game $G$ is equivalent to a single-pile Nim game.

This result shows that every impartial game $G$ can be assigned a natural number $n$ such that $G\approx *n$.

???+ abstract "Nimber"
    The **nimber** corresponding to an impartial game $G$ is the unique natural number $n$ such that $G\approx *n$.

The function mapping impartial games to nimbers is called the **Sprague–Grundy function**, abbreviated as the **SG function**, and denoted $\operatorname{SG}(\cdot)$. Since every state of an impartial game is itself an impartial game, the corresponding nimber can be computed for every state of an impartial game; it is also called the SG function value of that state.

From the proof of the theorem in this section, the Sprague–Grundy function can be computed recursively as follows:

???+ note "Corollary"
    The Sprague–Grundy function value $\operatorname{SG}(x)$ corresponding to a state $x$ of an impartial game $G$ satisfies
    
    $$
    \operatorname{SG}(x) = \operatorname{mex}\{\operatorname{SG}(x'): x'\in x\}.
    $$
    
    Here $\operatorname{mex}(A):=\min\{n\in\mathbf N:n\notin A\}$ is the smallest natural number not appearing in the set $A$.

In other words, the SG function value of a state equals the $\operatorname{mex}$ of the SG function values of all its successor states.

Using the SG function value (i.e. the nimber), one can determine whether a state is a first-player win.

???+ note "Corollary"
    A state $x$ of an impartial game $G$ is a first-player win if and only if $\operatorname{SG}(x)\neq 0$.

Finally, the SG function value of a sum of games is the Nim-sum (i.e. xor) of the SG function values of the subgames.

???+ note "Theorem (Sprague–Grundy)"
    For impartial games $G_1,G_2,\cdots,G_n$, we have
    
    $$
    \operatorname{SG}(G_1+ G_2+\cdots + G_n) = \operatorname{SG}(G_1)\oplus \operatorname{SG}(G_2)\oplus\cdots\oplus\operatorname{SG}(G_n).
    $$

??? note "Proof"
    Since $*a_1+ *a_2 + \cdots + *a_n$ is exactly the Nim game with pile sizes $(a_1,a_2,\cdots,a_n)$, by the result on Nim, the game
    
    $$
    *a_1+ *a_2 + \cdots + *a_n + *(a_1\oplus a_2\oplus\cdots\oplus a_n)
    $$
    
    is a first-player loss. By Lemma 2, we have
    
    $$
    *a_1+ *a_2 + \cdots + *a_n \approx *(a_1\oplus a_2\oplus\cdots\oplus a_n).
    $$
    
    Therefore,
    
    $$
    \operatorname{SG}(*a_1 + *a_2 + \cdots + *a_n) = a_1\oplus a_2\oplus\cdots\oplus a_n.
    $$
    
    Let $a_i=\operatorname{SG}(G_i)$; then $G_i\approx *a_i$, so by the algebraic properties of $\approx$ we have
    
    $$
    (G_1+ G_2+\cdots + G_n) + (*a_1 + *a_2 + \cdots + *a_n) = \sum_{i=1}^n(G_i+*a_i) \in\mathcal P.
    $$
    
    Hence,
    
    $$
    \begin{aligned}
    \operatorname{SG}(G_1+ G_2+\cdots + G_n) &= \operatorname{SG}(*a_1 + *a_2 + \cdots + *a_n) \\
    &= a_1\oplus a_2\oplus \cdots \oplus a_n \\
    &= \operatorname{SG}(G_1)\oplus \operatorname{SG}(G_2)\oplus\cdots\oplus\operatorname{SG}(G_n).
    \end{aligned}
    $$

Using this theorem, the computation of the SG function value of a sum of games can be greatly simplified.

From this, the method of computing SG function values can be summarized as follows:

-   for several independent games, compute their SG function values separately and then take the Nim-sum;
-   for a single game, the SG function value of each state is the $\operatorname{mex}$ of the SG function values of all its successor states;
-   in particular, the SG function value of a terminal state (i.e. a state with no successor states) is $\operatorname{mex}\varnothing = 0$.

### Nimbers

Every impartial game corresponds to a unique nimber. The set of (finite) nimbers is exactly the set of natural numbers $\mathbf N$. However, its algebraic properties differ from those of the natural numbers. Specifically, two operations can be defined on nimbers: the Nim-sum $\oplus$ and the Nim-product $\otimes$:

???+ abstract "Operations on nimbers"
    For nimbers $a,b$, one can define:
    
    -   the Nim-sum $a\oplus b=\operatorname{mex}(\{a'\oplus b:a'<a,~a'\in\mathbf N\}\cup\{a\oplus b':b'<b,~b'\in\mathbf N\})$,
    -   the Nim-product $a\otimes b=\operatorname{mex}(\{(a'\otimes b)\oplus(a\otimes b')\oplus(a'\otimes b'):a'<a,~b'<b,~a',b'\in\mathbf N\})$.

The set of all nimbers under the operations $\oplus$ and $\otimes$ forms a [field](../algebra/basic.md#域) of characteristic $2$. Moreover, these operations and their inverses are closed on the first $2^{2^n}$ nimbers; this yields a family of [finite fields](../algebra/field-theory.md#有限域) $\mathbf F_{2^{2^n}}$ of size $2^{2^n}$.

## Common impartial games

Although the Sprague–Grundy theory completely solves the problem of impartial games, when dealing with actual impartial games, directly applying the Sprague–Grundy theorem is still not efficient. For example, in Nim, computing the Sprague–Grundy values by brute force has exponential complexity. Therefore, the results for specific impartial games often have to be guessed by tabulating (printing a table of values with a program).

This section lists some common impartial games and the results about them. When stating the results, this section only gives the rule for deciding winning and losing states. The winning strategy is then to make the appropriate move so that the position left to the opponent is exactly a losing state. Since variants of these games often appear in algorithm competitions, it is also important to master the proofs of the results for each game.

???+ info "Method of proof for the results in this section"
    The proofs of the results in this section are all verifications. For a game, the result describes its first-player losing states and first-player winning states. In the proof, it suffices to verify that from a first-player losing state only first-player winning states can be reached, and that from a first-player winning state at least one first-player losing state can always be reached. To turn these proofs into rigorous ones, one needs to build the game graph and then apply mathematical induction to the states of the game graph; these verification steps are exactly the inductive part.

### Bachet's game

Compared with single-pile Nim, Bachet's game (also known as the Bash game) restricts the number of stones that can be removed in one move.

???+ abstract "Bachet's game"
    There is one pile of $n$ stones in total. Two players alternately remove at least $1$ and at most $k$ stones. The player who removes the last stone wins.

The following result holds:

???+ note "Theorem"
    The game is a first-player loss if and only if $n\equiv 0\pmod {k+1}$.

??? note "Proof 1"
    When $n\not\equiv 0\pmod {k+1}$, it suffices to remove $n\bmod{(k+1)}\in[1,k]$ stones to ensure that the opponent is in a losing state. Hence this is a first-player winning state.
    
    Conversely, when $n\equiv 0\pmod {k+1}$, either there is no choice left, or after we remove $k'$ stones the opponent can immediately remove $k+1-k'$ stones, putting us back into a losing state.

??? note "Proof 2"
    As an application of the Sprague–Grundy theorem, we can compute $f(n)$, the SG function value of the position with $n$ stones remaining.
    
    For $n\le k$, it can be shown inductively that $f(n)=n$. This is the same as single-pile Nim, because the restriction on the number of removed stones plays no role. For $n>k$, we need to show that $f(n)=n\bmod{(k+1)}$. Since $1$ to $k$ stones can be removed each time, we have
    
    $$
    f(n) = \operatorname{mex}\{f(n-k),f(n-k+1),\cdots,f(n-1)\}.
    $$
    
    By the induction hypothesis, this runs through all residues modulo $k+1$ except $n\bmod{(k+1)}$. Therefore, $f(n) = n\bmod{(k+1)}$.

### Moore's Nim-k

Compared with Nim, Moore's Nim-$k$ allows removing stones from at most $k$ piles in one move.

???+ abstract "Moore's Nim-$k$"
    There are $n$ piles of stones, and the $i$-th pile has $a_i$ stones. Two players alternately remove any number of stones from at least $1$ and at most $k$ piles, but they may not pass. The player who removes the last stone wins.

The following result holds:

???+ note "Theorem"
    Write the number of stones in each pile in binary, and for each bit position $d$ count how many piles have a $1$ at bit $d$ of their size, then compute the remainder of this count modulo $(k+1)$. If this remainder equals $0$ for every bit position, the first player loses; otherwise, the first player wins.

??? note "Proof"
    Following the proof of the result on Nim, this result is easy to prove. Let $d$ be the highest binary bit whose remainder is not $0$, and let the corresponding remainder be $k'\le k$. Then the winning strategy is to choose $k'$ piles among those whose size has a $1$ at bit $d$, and to choose the numbers of stones to remove exactly so that in the opponent's position the remainder at every bit position is $0$. The only thing that needs to be explained is that the choice of the numbers of removed stones is always feasible.
    
    Indeed, as long as bit $d$ of all the $k'$ chosen piles is set to $0$, the remainder at bit $d$ of the result becomes $0$; since the higher bits are unchanged, the lower bits of these piles can be set arbitrarily. For the lower bit positions, process them from high to low: suppose $c$ piles have been chosen and the remainder of the remaining piles at this bit is $r$. If $c\ge k+1-r$, set this bit to $1$ in exactly $k+1-r$ of the chosen piles; otherwise $c+r\le k$, so additionally choose $r$ piles that have a $1$ at this bit, set this bit of theirs to $0$, and set this bit of the previously chosen piles to $0$. In this way, the number of chosen piles never exceeds $k$.

### Staircase Nim

Staircase Nim is slightly more complicated: it allows stones to be moved between adjacent piles.

???+ abstract "Staircase Nim"
    There are $n$ piles of stones, and the $i$-th pile has $a_i$ stones. Two players move alternately; in each move, a player either removes any number of stones from pile $1$, or moves any number of stones from pile $i>1$ to pile $i-1$, but may not pass. The player who removes the last stone wins.

The following result holds:

???+ note "Theorem"
    The game is a first-player loss if and only if the Nim-sum of the sizes of the odd-indexed piles $a_1\oplus a_3\oplus\cdots\oplus a_{n-1+(n\bmod 2)}=0$.

??? note "Proof"
    Whenever a player moves stones from an even-indexed pile to an odd-indexed pile, the opponent can move these stones further to the next even-indexed pile (or remove them), so such a move does not affect the position of the odd-indexed piles. Then moving stones from each odd-indexed pile down to the adjacent even-indexed pile (or removing them) can be regarded as an independent single-pile Nim game. By the result of the Sprague–Grundy theorem on sums of games, the SG function value of staircase Nim is the Nim-sum of the SG function values of these subgames. This yields the result above.

### Fibonacci Nim

Fibonacci Nim is similar to Bachet's game: there is only one pile of stones, and the number of stones removed in each move is restricted. Unlike Bachet's game, in Fibonacci Nim the restriction on the number of removed stones is dynamic.

???+ abstract "Fibonacci Nim"
    There is one pile of $n$ stones in total. Two players alternately remove stones. The first player to move is not restricted in the number of stones removed, but may not remove all the stones; afterwards, the number of stones removed in each move may not exceed twice the number of stones removed in the previous move (i.e. the opponent's turn). The number of stones removed in each move may not be $0$. The player who removes the last stone wins.

The following result holds:

???+ note "Theorem"
    At the start of the game, the first player loses if and only if the number of stones $n$ is a [Fibonacci number](../combinatorics/fibonacci.md).

??? note "Proof"
    Let $q$ be the quota of the current position, i.e. the maximum number of stones that may be removed. Then in the first turn $q=n-1$, and in later turns $q$ is twice the number of stones removed in the previous (opponent's) turn. Consider the [Fibonacci coding](../combinatorics/fibonacci.md#fibonacci-coding) of the remaining number of stones $n$, i.e. the unique decomposition of $n$ into a sum of non-adjacent positive Fibonacci numbers. We need to show that the current state is a winning state if and only if $q$ is greater than or equal to the smallest Fibonacci number in the decomposition of $n$.
    
    The winning strategy is: if possible, remove all the remaining stones; otherwise, remove the smallest Fibonacci number in the decomposition. Since the second smallest Fibonacci number in the decomposition is necessarily strictly greater than twice the smallest one, as long as in the current turn of a winning state not all stones can be removed, in the next turn the opponent cannot remove the second smallest Fibonacci number (i.e. the smallest Fibonacci number in the next turn) either, so the opponent is necessarily in a losing state.
    
    Conversely, if the current state is a losing state, then let $k$ be the number of stones removed now; it is necessarily strictly less than the smallest Fibonacci number $F$ in the current decomposition. Suppose the smallest Fibonacci number in the next turn is $F'$; it is necessarily also the smallest Fibonacci number in the decomposition of $F - k$. If $F'\le 2$, then from $k\ge 1$ the quota in the next turn is $2k\ge 2\ge F'$, which is already a winning state. Otherwise, let $F'=F''+F'''$ with $F''>F'''$, that is, $F''',F'',F'$ are three consecutive terms of the Fibonacci sequence. If $k<F''$, then no carry occurs when computing $k + (F-k)$ in Fibonacci coding, so naturally $F$ cannot be obtained. Hence we must have $k\ge F''$. This shows that the quota in the next turn is $2k>F''+F'''=F'$, which is a winning state.

### Wythoff's game

Wythoff's game allows removing stones from several piles at the same time, but requires that the same number of stones be removed from each pile.

???+ abstract "Wythoff's game"
    There are two piles of stones, with $a_1$ and $a_2$ stones respectively. Two players alternately remove stones from one or both piles; they may not pass, and when removing from both piles, the numbers of removed stones must be equal. The player who removes the last stone wins.

The following result holds:

???+ note "Theorem"
    Without loss of generality, let $a_1\le a_2$; then the first player loses if and only if $a_1 = \lfloor(a_2-a_1)\phi\rfloor$, where $\phi=(\sqrt{5}+1)/2$ is the golden ratio.

To prove this result, the following lemma is needed:

???+ abstract "Beatty sequence"
    Let $r > 1$ be an irrational number. The Beatty sequence it generates is $\mathcal B_r = \{\lfloor kr\rfloor : k \in\mathbf N_+\}$.

???+ note "Rayleigh's theorem"
    Let $r,s > 1$ be two irrational numbers with $\dfrac{1}{r}+\dfrac{1}{s}=1$. Then the sequences $\mathcal B_r$ and $\mathcal B_s$ form a partition of the set of positive integers $\mathbf N_+$. In this case, they are also called complementary Beatty sequences.

??? note "Proof"
    Let $\mathcal A_r=\{kr:k\in\mathbf N_+\}$. Consider sorting the elements of the set $\mathcal A=\mathcal A_r\cup\mathcal A_s$ to obtain the sequence $\{a_i\}_{i\in\mathbf N_+}$. It suffices to show that $i=\lfloor a_i\rfloor$ holds for all $i\in\mathbf N_+$ to conclude that $\mathcal B_r\cup\mathcal B_s$ is a partition of the set of positive integers $\mathbf N_+$.
    
    First, we show that the sequence has no repeated elements. Suppose otherwise, that there exist $k,\ell\in\mathbf N_+$ with $kr=\ell s$. Then
    
    $$
    \dfrac{\ell}{k} = \dfrac{r}{s} = r - 1.
    $$
    
    But the left-hand side is rational while the right-hand side is irrational, a contradiction. Hence the numbers in the sequence are pairwise distinct.
    
    Next, we show that the set $\mathcal A$ contains exactly $\lfloor a_i\rfloor$ numbers less than or equal to $a_i$. Without loss of generality, let $a_i\in\mathcal A_r$, i.e. $a_i=kr$; counting the elements of the sets $\mathcal A_r$ and $\mathcal A_s$ separately, we find that the set $\mathcal A$ contains exactly
    
    $$
    k + \left\lfloor\dfrac{kr}{s}\right\rfloor = k + \lfloor k(r-1)\rfloor = \lfloor kr\rfloor = \lfloor a_i\rfloor
    $$
    
    elements less than or equal to $a_i$. Furthermore, since the sequence $\{a_i\}$ is strictly increasing, there are exactly $i$ numbers less than or equal to $a_i$. This gives $i=\lfloor a_i\rfloor$.

From this, the proof of the result above follows.

??? note "Proof of the result on Wythoff's game"
    For all first-player losing states $(a_1,a_2)$ with $a_1 < a_2$ described in the theorem, let $k = a_2 - a_1 \in\mathbf N_+$; then $a_1=\lfloor k\phi\rfloor$ and $a_2=\lfloor k(\phi+1)\rfloor$. Since $\phi$ is the golden ratio, $\dfrac{1}{\phi}+\dfrac{1}{\phi+1}=1$. By Rayleigh's theorem, the sequences $\{\lfloor k\phi\rfloor\}$ and $\{\lfloor k(\phi+1)\rfloor\}$ form a partition of the set of positive integers $\mathbf N_+$. This actually says that among all first-player losing states $(a_1,a_2)$ with $a_1 < a_2$, the components $a_1$ and $a_2$ take every positive integer exactly once, and their difference $a_2-a_1$ also takes every positive integer exactly once.
    
    Since in Wythoff's game a legal move either keeps one of the components unchanged or keeps the difference of the components unchanged, starting from a first-player losing state one indeed cannot reach another first-player losing state by a single legal move. Conversely, for any first-player winning state $(a_1,a_2)$, assume without loss of generality that $a_1\le a_2$ and let $k=a_2-a_1$. If $a_1>\lfloor k\phi\rfloor$, then the first player can remove $(a_1 - \lfloor k\phi\rfloor)$ stones from each of the two piles, turning the position into a losing state. Otherwise, since $(a_1,a_2)$ is a first-player winning state, we have $a_1 < \lfloor k\phi\rfloor$, hence $k\ge 1$. By the conclusion of the previous paragraph (together with the losing state $(0,0)$), for this $a_1$ there necessarily exists a unique losing state $(a_1,a_2')$ (here $a_1\le a_2'$ is not required). Furthermore, if $a_1 \ge a_2'$, then clearly $a_2' \le a_1 < a_2$; otherwise, if $a_1 < a_2'$, then we can take $k'=a_2'-a_1$ such that $a_1=\lfloor k'\phi\rfloor$, and since also $a_1 < \lfloor k\phi\rfloor$, we get $k' < k$, hence $a_2'=a_1 + k' < a_1+k = a_2$. Therefore, as long as $a_1 < \lfloor k\phi\rfloor$, we must have $a_2' < a_2$, and the first player only needs to remove $(a_2-a'_2)$ stones from the second pile to turn the position into a losing state.

### Coin-turning games

Coin-turning games are also a common class of impartial games.

???+ abstract "Coin-turning game"
    Let $(S,\preceq)$ be a [well-founded partially ordered set](../order-theory.md), and let the map $f:S\rightarrow\mathcal P\mathcal PS$ satisfy that for all $s\in S$ the set $f(s)$ is nonempty, for every $T\in f(s)$ we have $s\in T$, and for all $t\in T$ we have $t\preceq s$. At every element of the set $S$ there is a coin, which may be heads up or tails up. The players move alternately: a player chooses a coin $s$ that is heads up and a set $T\in f(s)$, and flips all coins in the set $T$. The player who turns all coins tails up wins.

Coin-turning games are actually a large class of games. Depending on the specific choice of the poset $S$ and the map $f$, the concrete form of the coin-turning game varies. The condition that the map $f$ must satisfy in the description of the game says that in the set $T$ of coins a player chooses to flip, there is always a coin $s$ that is heads up such that all other elements of $T$ are ordered before $s$. This guarantees that the game terminates after finitely many moves.

???+ example "Example"
    1.  Let $S=\{1,2,\cdots,n\}$ and $f(s)=\{\{t,s\}:t \le s\}$. This amounts to saying: there is a row of $n$ coins; in each move, flip a coin that is heads up, and optionally choose one coin to its left and flip it as well.
    2.  Let $S=\{1,2,\cdots,n\}$ and $f(s)=\{[t,s]:t \le s\}$. This amounts to saying: there is a row of $n$ coins; in each move, flip a contiguous segment of coins, but the rightmost coin among them must be heads up before flipping.
    3.  Let $S=\{1,2,\cdots,n\}^2$ and $f(s)=\{\{s\}\}$. This amounts to saying: there are $n$ rows and $n$ columns of coins, and in each move only one coin that is heads up may be flipped.
    4.  Let $S$ be the set of nodes of a rooted tree, and let $f(s)$ be the set of all those subsets of the set of nodes on the path from vertex $s$ to the root that contain $s$ itself. This amounts to saying: there is a rooted tree with a coin placed at each node; in each move, flip a coin that is heads up, and optionally choose the coins at several of its ancestor nodes and flip them as well.

Although there are many kinds of coin-turning games, the approach to solving them is the same. For a coin-turning game $(S,f)$, let $G_s$ be the position in which only the coin at element $s$ is heads up. These positions are called basic positions. Then any position $G$ can be regarded as the sum of the games corresponding to these basic positions. That is, the following result holds:

???+ note "Theorem"
    For a coin-turning game $(S,f)$ and a position $G$, let $H(G)\subseteq S$ be the set of positions of the coins that are heads up. Then the SG function value of the position $G$ is
    
    $$
    \operatorname{SG}(G) = \bigoplus_{s\in H(G)}\operatorname{SG}(G_s).
    $$

??? note "Proof"
    Consider a related game: in a position $G'$, some stones are placed at every element of the set $S$; in each move, a player may remove one stone at $s$, choose a set $T\in f(s)$, and then place one stone at each element of the set $T\setminus\{s\}$. For this kind of game, we can still define basic positions $G'_s$, i.e. positions with exactly one stone placed at location $s$ only. In this game, every position is the sum of the basic positions corresponding to all its stones. This is because, as long as every newly placed stone is associated with the removed stone, every stone appearing during the game can be associated with one of the stones of the initial position, so the subgames corresponding to different stones of the initial position proceed without interfering with each other, and the whole game can be regarded as the sum of these subgames. Since the SG values of the basic positions corresponding to stones at the same location are the same, by the properties of xor the SG value of the position $G'$ is determined only by the parity of the numbers of stones at the individual locations, not by the exact numbers. Therefore, for a game position $G'$, if we denote by $H(G')$ the set of locations with an odd number of stones, the analysis of this paragraph can be summarized by the formula:
    
    $$
    \operatorname{SG}(G') = \bigoplus_{s\in H(G')} \operatorname{SG}(G'_s).
    $$
    
    Hence, to prove the formula in the theorem, it remains only to establish the equivalence between the game $G'$ and the game $G$.
    
    We need to show that for a position $G'$ of the new game and a position $G$ of the coin-turning game, as long as the locations with an odd number of stones in $G'$ coincide with the locations of the heads-up coins in $G$, the games $G'$ and $G$ are equivalent. By Lemma 2 of the section [Sprague–Grundy function](#spraguegrundy-function), this is equivalent to proving that the position $G+G'$ is a losing state. The winning strategy of the second player is simple: if the first player removes a stone at $s$ where more than one stone is placed, the second player simply mimics the first player's move; otherwise, the second player chooses the same $s$ and $T\in f(s)$ as the first player, but in the other subgame – if the first player removes a stone, the second player flips coins, and if the first player flips coins, the second player removes a stone. No matter how the first player moves, the second player can keep moving and ensure that in the remaining position the locations with an odd number of stones coincide with the locations of the heads-up coins. Thus the game necessarily ends when the first player has no legal move, so the first player loses. This proves the theorem.

Using this result, to determine whether a position is a winning one, it suffices to compute the SG function values of the basic positions corresponding to all heads-up coins and then take the Nim-sum. The SG function values of these basic positions are also not hard to compute, since their successor positions are already given by the map $f$, and the SG values of the successor positions can be computed inductively:

$$
\operatorname{SG}(G_s) = \operatorname{mex}\limits_{T\in f(s)}\bigoplus_{t\in T\setminus\{s\}}\operatorname{SG}(G_t).
$$

This effectively provides a recurrence for the SG function values of the basic positions.

### Bipartite graph game

Prerequisites: [Maximum bipartite matching](../../graph/graph-matching/bigraph-match.md)

At the end of this section, we discuss the bipartite graph game. Although this game is usually called the bipartite graph game, its description and the proof of its result have nothing to do with the structure of bipartite graphs, so its result actually holds for general undirected graphs. However, maximum matching in general graphs is rather complicated, so this result usually appears in problems about bipartite graphs.

???+ abstract "Bipartite graph game"
    Two players move alternately. The position faced by each player consists of an undirected graph $G=(V,E)$ and one of its vertices $v\in V$. In a player's turn, if the current position is $(G,v)$, the player must choose a vertex $u$ adjacent to $v$. Then the vertex $v$ and all its incident edges are deleted from the graph $G$, yielding the residual graph $G'$. The new position is $(G',u)$, which is handed to the next player. If at the start of a player's turn the current vertex $v$ has no adjacent vertex in the graph (i.e. there is no legal choice), that player cannot move and therefore loses the game.

The following result holds:

???+ note "Theorem"
    The game is a first-player win if and only if the vertex $v$ is an essential vertex of maximum matchings of the graph $G$, that is, in every maximum matching of the graph $G$ the vertex $v$ is a matched vertex.

??? note "Proof"
    First, let the vertex $v$ be an essential vertex of maximum matchings of the graph $G$. Let $M$ be a maximum matching of $G$. Then the first player can move the position to the vertex $u$ matched with the vertex $v$ in $M$. Since the vertex $v$ appears in every maximum matching of the graph $G$, the size of a maximum matching of the residual graph $G'$ is at most $|M|-1$; moreover, removing the edge $(u,v)$ from $M$ yields a matching $M'$ of the graph $G'$ of size $|M|-1$. Combining these two facts, $M'$ is a maximum matching of the graph $G'$. But in the position faced by the second player, the vertex $u$ is not a matched vertex of the matching $M'$. Therefore, the second player is necessarily in a losing state.
    
    Conversely, suppose there is a maximum matching $M$ in which $v$ is an unmatched vertex. Since $M$ does not contain the vertex $v$, it is also a maximum matching of the residual graph $G'$; hence any maximum matching $N$ of $G'$ is a maximum matching of $G$ not containing the vertex $v$. A vertex $u$ adjacent to the vertex $v$ must be a matched vertex of $N$; otherwise, the edge $(u,v)$ could be added to $N$ to obtain a larger matching of $G$. This shows that $u$ is an essential vertex of maximum matchings of $G'$. Therefore, no matter how the first player chooses, the second player is in a winning state.

The algorithm for finding the essential vertices of maximum matchings of a bipartite graph is described on the [maximum bipartite matching page](../../graph/graph-matching/bigraph-match.md#essential-vertices-of-maximum-matchings).

In addition, the bipartite graph game has a variant:

???+ abstract "Variant of the bipartite graph game"
    Let $G=(V,E)$ be an undirected graph with a stone placed at every vertex. Two players alternately remove stones. At the start of the game, the first player may remove any stone; in later turns, the vertex from which a player removes a stone must be adjacent to the vertex from which the opponent removed a stone in the previous turn. The first player who cannot remove a stone loses the game.

Clearly, this variant amounts to letting the first player choose the initial position in the bipartite graph game described above, and then starting the bipartite graph game from the second player. Therefore, in this variant the first player loses if and only if every vertex is an essential vertex of maximum matchings, i.e. the graph $G$ has a [perfect matching](../../graph/graph-matching/graph-match.md#definition).

## Misère Nim

This section discusses how to solve misère Nim.

???+ abstract "Misère Nim"
    There are $n$ piles of stones, and the $i$-th pile has $a_i$ stones. Two players alternately remove any number of stones from any single pile, but they may not pass. The player who removes the last stone loses.

The following result holds:

???+ note "Theorem"
    In misère Nim, the state $(a_1,a_2,\cdots,a_n)$ is a losing state $\mathcal P$ if and only if
    
    1.  there exists $i$ with $a_i>1$, and the Nim-sum $a_1\oplus a_2\oplus\cdots\oplus a_n=0$, or
    2.  $a_i\le 1$ for all $i$, and the number of remaining nonempty piles is odd.

??? note "Proof"
    Since having no move available is a first-player winning state $\mathcal N$, it can be shown inductively that if every pile has at most one stone, then an odd number of nonempty piles corresponds to a first-player losing state $\mathcal P$, and an even number of nonempty piles corresponds to a first-player winning state $\mathcal N$.
    
    Next, consider the case where some piles have strictly more than $1$ stone.
    
    Case A: if only one pile has strictly more than $1$ stone, then the Nim-sum is necessarily not $0$. Moreover, the first player can choose to move to a position in which every pile has at most $1$ stone, and can control the parity of the number of remaining nonempty piles. Hence this is a first-player winning state $\mathcal N$.
    
    Case B: now more than one pile has strictly more than $1$ stone; then no matter how one moves, in the next position at least one pile has strictly more than $1$ stone. By the induction hypothesis, in the next position a first-player loss corresponds to a zero Nim-sum, and a first-player win corresponds to a nonzero Nim-sum. This is exactly the same as the induction hypothesis for normal Nim. Therefore, repeating the argument for Nim, we see that the current position also satisfies the result that a zero Nim-sum corresponds to a first-player losing state.

## Games on directed graphs

The impartial games discussed in this article require that the same position cannot appear twice, and that there is no possibility of a draw. Therefore, the corresponding game graph is always a directed acyclic graph. This section relaxes this restriction and discusses how to decide, on a general directed graph, whether each state is a first-player win, a first-player loss, or a draw.

The rules of a game on a directed graph are largely the same as those of other impartial games: starting from the initial state, the players alternately move one step along an edge of the directed graph until no move is possible. Depending on whether the game is under the normal or the misère rule, the player who cannot move is the loser or the winner respectively. In such a game, the outcome of each state has three possibilities: first-player win, first-player loss, and draw. In a draw, the game never terminates. Although slightly more complicated, the [lemma](#game-graph-and-states) about losing and winning states still holds, and the remaining states are draw states:

-   if a state has successor states, then it is a first-player win if and only if one of its successor states is a losing state;
-   if a state has successor states, then it is a first-player loss if and only if all of its successor states are winning states;
-   if a state cannot be classified as a winning or a losing state, then it is a draw state.

To classify all states into these three kinds, it suffices to use an approach similar to [topological sorting](../../graph/topo.md):

1.  During initialization, record the out-degrees of all states, push all states with out-degree zero into a queue, and mark them as losing or winning states depending on whether the game is under the normal or the misère rule.
2.  Pop the state at the front of the queue. If it is a losing state, mark all its not yet decided predecessor states as winning states; otherwise, the current state is a winning state, so decrease the out-degree of all its predecessor states by one and mark the predecessor states whose out-degree becomes zero as losing states. Push the predecessor states that can be decided as winning or losing into the queue.
3.  The algorithm terminates when the queue is empty. The states that have not been decided as winning or losing are all draw states.

This algorithm classifies all states in $O(|V|+|E|)$ time.

## Example problems

This section discusses some typical example problems.

???+ example "[Luogu P2148 \[SDOI2009\] E&D](https://www.luogu.com.cn/problem/P2148)"
    There are $2n$ piles of stones. For $k=1,2,\cdots,n$, piles $2k-1$ and $2k$ form a group. Two players move alternately; in each move, a player chooses a group of piles, removes one of the piles, and splits the other pile into two nonempty piles, placing them at the two positions of that group. If all piles have only one stone, the current player has no legal move and loses the game. Given the sizes of the piles $\{a_i\}_{i=1}^{2n}$, determine whether it is a first-player winning state.

??? note "Solution"
    Clearly, the games in different groups of piles are mutually independent, so it suffices to compute the SG function value of the game of each group to obtain the SG value of the whole game and thus decide whether it is a winning state. The key is how to compute the SG function value of each group of piles. This is not easy. A common approach to such game theory problems is tabulation. Let the SG value of a group of piles with $(i,j)$ stones be $f(i,j)$. Then writing a brute-force program that prints the table yields the following result:
    
    ```text
    0 1 0 2 0 1 0 3 0 1 0 2 0 1 0 4 
    1 1 2 2 1 1 3 3 1 1 2 2 1 1 4 4
    0 2 0 2 0 3 0 3 0 2 0 2 0 4 0 4
    2 2 2 2 3 3 3 3 2 2 2 2 4 4 4 4
    0 1 0 3 0 1 0 3 0 1 0 4 0 1 0 4
    1 1 3 3 1 1 3 3 1 1 4 4 1 1 4 4
    0 3 0 3 0 3 0 3 0 4 0 4 0 4 0 4
    3 3 3 3 3 3 3 3 4 4 4 4 4 4 4 4
    0 1 0 2 0 1 0 4 0 1 0 2 0 1 0 4
    1 1 2 2 1 1 4 4 1 1 2 2 1 1 4 4
    0 2 0 2 0 4 0 4 0 2 0 2 0 4 0 4
    2 2 2 2 4 4 4 4 2 2 2 2 4 4 4 4
    0 1 0 4 0 1 0 4 0 1 0 4 0 1 0 4
    1 1 4 4 1 1 4 4 1 1 4 4 1 1 4 4
    0 4 0 4 0 4 0 4 0 4 0 4 0 4 0 4
    4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4
    ```
    
    This table is very regular. A simple observation: the table splits into several $2\times 2$ matrices, the top-left corner is always $0$, and the other three values are always equal. So we may compress the table by replacing each $2\times 2$ matrix with the common value other than the top-left corner:
    
    ```text
    1 2 1 3 1 2 1 4 
    2 2 3 3 2 2 4 4 
    1 3 1 3 1 4 1 4 
    3 3 3 3 4 4 4 4 
    1 2 1 4 1 2 1 4 
    2 2 4 4 2 2 4 4 
    1 4 1 4 1 4 1 4 
    4 4 4 4 4 4 4 4 
    ```
    
    One can see that this compressed table equals the values at the same positions of the previous full table plus one. The problem is now essentially solved. Let the indices start from $0$; then the value $g(i,j)$ at position $(i,j)$ of the table is given by the following recurrence:
    
    $$
    g(i,j) =
    \begin{cases}
    0, & \text{if }2\mid i\text{ and }2\mid j,\\
    g(\lfloor i/2\rfloor,\lfloor j/2\rfloor)+1,& \text{otherwise}.
    \end{cases}
    $$
    
    The required SG function is $f(i,j)=g(i-1,j-1)$. Using this recurrence, the algorithm can compute the value of $f(i,j)$ in $O(\log\max\{i,j\})$ time.
    
    Of course, by a simple induction one can see that $g(i,j)$ is actually the minimum number of times $i$ and $j$ must be simultaneously and repeatedly divided by $2$ to obtain two even numbers. In other words, it is the number of trailing consecutive $1$ bits in the bitwise or of $i$ and $j$. Hence this value can also be computed directly with `__builtin_ctz(~(i | j))`.
    
    In problems of this kind, once the expression of the SG function is obtained by tabulating and observing, it is easy to prove by induction, so the key to solving the problem is to obtain these results in some form rather than to derive them. For example, once the result is known, the recurrence in this problem can be proved inductively as follows. Let $S_k$ be the set of SG values of the positions obtainable by splitting $k$ stones into two nonempty piles; then $f(i,j) = \operatorname{mex}(S_i \cup S_j)$. Hence $S_k$ satisfies the recurrence:
    
    $$
    S_k = \{\operatorname{mex}(S_i \cup S_j) : i + j = k,~i,j\in\mathbf N_+\}.
    $$
    
    We need to show that $d\in S_k$ if and only if bit $d$ (the lowest bit being bit $0$) of the binary representation of $(k-1)$ is $1$.
    
    We use mathematical induction. The base case $S_1=\varnothing$ clearly holds. Suppose the claim holds for all positive integers less than $k$. Then $d\in S_k$ if and only if there exist $i,j\in\mathbf N_+$ with $i+j=k$ such that bit $d$ of both $(i-1)$ and $(j-1)$ is $0$, and for every $d' < d$ at least one of them has bit $d'$ equal to $1$. Clearly such a split exists if and only if, considering only bits $0\sim d$, i.e. modulo $2^{d+1}$, the value of $(k-1)=(i-1)+(j-1)+1$ lies in the range $[2^d,2^{d+1})$. This condition is equivalent to bit $d$ of $(k-1)$ being $1$. Hence the induction step holds. The original claim is proved.

??? note "Reference code"
    ```cpp
    --8<-- "docs/math/code/impartial-game/impartial-game-1.cpp"
    ```

???+ example "[Luogu P5675 \[GZOI2017\] 取石子游戏 (Stone-taking game)](https://www.luogu.com.cn/problem/P5675)"
    There are $n$ piles of stones, and the $i$-th pile has $a_i$ stones. Two people play Nim. Now one may designate any number of piles as the initial position, and designate one of them as the pile from which the first player must remove stones in the first turn, but one cannot specify the number of stones removed. How many ways of designating are there such that the first player cannot win? The data satisfy $n,a_i\le 200$.

??? note "Solution"
    For problems of this kind, one needs to use the results on common games and combine them with knowledge from other areas. Suppose the first player is required to remove stones from the $i$-th pile, and the Nim-sum of the sizes of all designated piles is $v$; then the first player cannot win if and only if $a_i \le a_i\oplus v$, that is, the size $a_i$ of the $i$-th pile does not exceed the Nim-sum $a_i\oplus v$ of the sizes of the remaining designated piles other than the $i$-th one. Since the data range is very small, enumerate directly the pile designated for the first move; when enumerating the $i$-th pile, each remaining pile is either chosen or not, and the number of ways yielding each Nim-sum can be computed by DP; finally, sum up the numbers of ways corresponding to values greater than or equal to $a_i$.

??? note "Reference code"
    ```cpp
    --8<-- "docs/math/code/impartial-game/impartial-game-2.cpp"
    ```

???+ example "[Luogu P2599 \[ZJOI2009\] 取石子游戏 (Stone-taking game)](https://www.luogu.com.cn/problem/P2599)"
    There are $n$ piles of stones, and the $i$-th pile has $a_i$ stones. Two people alternately remove stones; each time, one may only choose one of the two piles at the leftmost or rightmost end and remove any number of stones from it, but may not pass. The player who removes the last stone wins. Determine whether the first player wins.

??? note "Solution"
    Since in this problem there are no mutually independent subgames, in principle only the [lemma for deciding losing and winning states](#game-graph-and-states) is used. Start the analysis from the simplest case. When $n\le 2$, this is Nim. When $n \ge 3$, the problem becomes complicated. However, since only the piles at the two ends can be operated on, let their sizes be $x$ and $y$. Furthermore, let $f(x,y)$ be the indicator function of a first-player winning state, i.e. $f(x,y)=1$ when the first player wins and $f(x,y)=0$ otherwise. It is easy to see that the values of $f(x,y)$ satisfy the recurrence: $f(x,y)=0$ if and only if $f(x,t)=f(s,y)=1$ for all $s < x$ and $t < y$. The base of the recurrence is when $x=0$ or $y=0$; then the game has fewer than $n$ piles, and the sizes of the middle piles must be considered further. Therefore, let us temporarily assume that $f(x,0)$ and $f(0,y)$ are known, and consider how to derive all values of $f(x,y)$ from them. This is not difficult. Consider an infinite matrix indexed by $\mathbf N\times\mathbf N$; computing $f(x,y)$ amounts to filling it with $0$ and $1$, and the conditions to satisfy are that each row and each column contain at most one $0$, and that if no $0$ has appeared at earlier positions in the same row and the same column, this position must be $0$. The position of the $0$ in each row actually defines a function from the row index $x$ to the column index $y$. After trying a few simple examples (i.e. tabulating), one can see that if the unique $x$ with $f(x,0)=0$ is $x_0$ and the unique $y$ with $f(0,y)=0$ is $y_0$, then for any positive integer $x$ the value for which $f(x,y)=0$ holds is
    
    $$
    y = \begin{cases}
    0, & x = x_0,\\
    x - 1, & x_0 < x \le y_0,\\
    x + 1, & y_0 \le x < x_0,\\
    x, & \text{otherwise}.
    \end{cases}
    $$
    
    That is, once $x_0$ and $y_0$ are known, any value $f(x,y)$ can be computed in $O(1)$ time, deciding whether the current state is a first-player winning state. And $x_0$ and $y_0$ can be computed recursively. For example, $x_0$ is the unique solution of $f(x,0)=0$, but at the same time the value of $f(x,0)$ can be computed by removing the rightmost pile and considering only the remaining $n-1$ piles; that is, considering only the first $n-1$ piles, one can likewise compute $f_{1,n-1}(x,y)$, and then clearly $f(x,0)=f_{1,n-1}(x,a_{n-1})$; similarly, after removing the leftmost pile and computing $f_{2,n}(x,y)$, we get $f(0,y)=f_{2,n}(a_2,y)$. Of course, the computation of the inner functions $f_{1,n-1}(x,y)$ and $f_{2,n}(x,y)$ depends on functions at even deeper levels. This is a typical [interval DP](../../dp/interval.md). At each level, it suffices to maintain $x_0$ and $y_0$ of the corresponding function.

??? note "Reference code"
    ```cpp
    --8<-- "docs/math/code/impartial-game/impartial-game-3.cpp"
    ```

## Exercises

First, some template problems. They are simple applications of the results of this page:

-   [Luogu P2197【模板】Nim 游戏 (Template: Nim)](https://www.luogu.com.cn/problem/P2197)
-   [Luogu P2252 \[SHOI2002\] 取石子游戏 (Stone-taking game)](https://www.luogu.com.cn/problem/P2252)
-   [Luogu P2594 \[ZJOI2009\] 染色游戏 (Coloring game)](https://www.luogu.com.cn/problem/P2594)
-   [Luogu P3185 \[HNOI2007\] 分裂游戏 (Splitting game)](https://www.luogu.com.cn/problem/P3185)
-   [Luogu P3480 \[POI 2009\] KAM-Pebbles](https://www.luogu.com.cn/problem/P3480)
-   [Luogu P4101 \[HEOI2014\] 人人尽说江南好 (Everyone praises Jiangnan)](https://www.luogu.com.cn/problem/P4101)
-   [Luogu P4279 \[SHOI2008\] 小约翰的游戏 (Little John's game)](https://www.luogu.com.cn/problem/P4279)
-   [Luogu P6487 \[COCI 2010/2011 #4\] HRPA](https://www.luogu.com.cn/problem/P6487)
-   [Luogu P6560 \[SBCOI2020\] 时光的流逝 (The passage of time)](https://www.luogu.com.cn/problem/P6560)
-   [Luogu P7589 黑白棋（2021 CoE-II B）(Black and white pieces)](https://www.luogu.com.cn/problem/P7589)
-   [AtCoder Regular Contest 168 B - Arbitrary Nim](https://atcoder.jp/contests/arc168/tasks/arc168_b)

Then some problems that require more thought or are more comprehensive:

-   [Luogu P2490 \[SDOI2011\] 黑白棋 (Black and white pieces)](https://www.luogu.com.cn/problem/P2490)
-   [Luogu P3179 \[HAOI2015\] 数组游戏 (Array game)](https://www.luogu.com.cn/problem/P3179)
-   [Luogu P5363 \[SDOI2019\] 移动金币 (Moving coins)](https://www.luogu.com.cn/problem/P5363)
-   [Luogu P5970 \[POI 2016\] Nim z utrudnieniem](https://www.luogu.com.cn/problem/P5970)
-   [Luogu P6791 \[SNOI2020\] 取石子 (Taking stones)](https://www.luogu.com.cn/problem/P6791)
-   [Luogu P7864「EVOI-RD1」摘叶子 (Picking leaves)](https://www.luogu.com.cn/problem/P7864)
-   [Luogu P8347「Wdoi-6」另一侧的月 (The moon on the other side)](https://www.luogu.com.cn/problem/P8347)
-   [AtCoder Grand Contest 002 E - Candy Piles](https://atcoder.jp/contests/agc002/tasks/agc002_e)
-   [AtCoder Grand Contest 010 F - Tree Game](https://atcoder.jp/contests/agc010/tasks/agc010_f)
-   [AtCoder Grand Contest 017 D - Game on Tree](https://atcoder.jp/contests/agc017/tasks/agc017_d)
-   [AtCoder Beginner Contest 278 G - Generalized Subtraction Game](https://atcoder.jp/contests/abc278/tasks/abc278_g)
-   [SPOJ COT3 - Combat on a tree](https://www.spoj.com/problems/COT3/)
-   [Codeforces 494 E. Sharti](https://codeforces.com/problemset/problem/494/E)
-   [Codeforces 1149 E. Election Promises](https://www.luogu.com.cn/problem/CF1149E)
-   [Codeforces 1451 F. Nullify The Matrix](https://codeforces.com/problemset/problem/1451/F)
-   [Codeforces 1704 F. Colouring Game](https://codeforces.com/problemset/problem/1704/F)

Finally, some problems on the bipartite graph game. Since they require bipartite matching algorithms, they are listed separately:

-   [Luogu P4136 谁能赢呢？(Who can win?)](https://www.luogu.com.cn/problem/P4136)
-   [Luogu P4617 \[COCI 2017/2018 #5\] Planinarenje](https://www.luogu.com.cn/problem/P4617)
-   [Luogu P4055 \[JSOI2009\] 游戏 (Game)](https://www.luogu.com.cn/problem/P4055)
-   [Luogu P1971 \[NOI2011\] 兔兔与蛋蛋游戏 (Bunny and Egg's game)](https://www.luogu.com.cn/problem/P1971)
-   [Codeforces 1147 F. Zigzag Game](https://codeforces.com/problemset/problem/1147/F)

## References and notes

-   [（转载）Nim 游戏博弈（收集完全版）by exponent - 博客园 (Nim games – game theory (complete collection, repost), exponent, cnblogs)](http://www.cnblogs.com/exponent/articles/2141477.html)
-   [\[组合游戏与博弈论\]【学习笔记】by Candy? - 博客园 (Combinatorial games and game theory – study notes, Candy?, cnblogs)](https://www.cnblogs.com/candy99/p/6548836.html)
-   [Nim - Wikipedia](https://en.wikipedia.org/wiki/Nim)
-   [Sprague–Grundy theorem - Wikipedia](https://en.wikipedia.org/wiki/Sprague%E2%80%93Grundy_theorem)
-   [Nimber - Wikipedia](https://en.wikipedia.org/wiki/Nimber)
-   [Beatty Sequence - Wikipedia](https://en.wikipedia.org/wiki/Beatty_sequence)
-   [Games on arbitrary graphs - CP Algorithms](https://cp-algorithms.com/game_theory/games_on_graphs.html)
-   [算法学习笔记（74): 二分图博弈 by Pecco - 知乎 (Algorithm study notes (74): bipartite graph game, Pecco, Zhihu)](https://zhuanlan.zhihu.com/p/359334008)
-   Conway, John H. On numbers and games. AK Peters/CRC Press, 2000.
-   Berlekamp, Elwyn R., John H. Conway, and Richard K. Guy. Winning ways for your mathematical plays, volume 1-4. AK Peters/CRC Press, 2001-2004.

[^n-vs-p]: The names “$\mathcal N$-state” and “$\mathcal P$-state” stand for “Next player wins” and “Previous player wins” respectively.

[^more-sums]: The “sums” discussed in this article are all **disjunctive sums** under the **long rule**. This is also the most common way of combining games. Besides it, there are other possible ways of combining games. For a detailed discussion of them, see Chapter 14 of Conway, John H. On numbers and games. AK Peters/CRC Press, 2000.
