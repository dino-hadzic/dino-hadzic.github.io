---
title: Randomization techniques
---

## Overview

Prerequisites: [Random numbers](../misc/random.md) and [Basics of probability](../math/probability/basic-conception.md)

This article gives a simple classification of randomization-related techniques in OI/ICPC and introduces each category. It also introduces some methods that are rarely used in OI/ICPC but are close to OI/ICPC in style; such content is marked with `(*)`.

This classification does not represent a broad consensus and certainly cannot cover all possibilities, so it is only for reference.

**Notation and conventions**:

-   $\mathrm{Pr}[A]$ denotes the probability that event $A$ occurs.
-   $\mathrm{E}[X]$ denotes the expectation of the random variable $X$.
-   The assignment sign $:=$ denotes the introduction of a new quantity, e.g. $Y:=1926$ means introducing a quantity $Y$ with value $1926$.

## Covering the target element with a random set

In a huge solution space there is one (or more) solution we want. We can try to "cast a net" several times; as long as one cast catches the target solution, we succeed.

### Example: deciding whether a graph is tripartite

???+ note "Problem"
    Given a simple undirected graph with $n$ vertices and $m$ edges, color every vertex with one of the three colors R, G, B so that every pair of neighbors gets different colors, or report that there is no solution.

For each vertex $v$, independently and uniformly at random choose a color $C_v$ from $\{R,G,B\}$, and require that $v$ is **not** colored $C_v$. The probability that the optimal solution happens to satisfy these restrictions is obviously $\big(\frac 23\big)^n$.

Under these restrictions, for a pair of neighbors $(u,v)$ the requirement "$u$ and $v$ have different colors" is equivalent to the following "implication" relation:

-   For every color $X$ different from $C_u$ and $C_v$, if $u$ is colored $X$, then $v$ is colored $\{R,G,B\}\setminus\{X,C_v\}$.

Therefore we can introduce a Boolean variable $B_v$ for every $v$, whose value indicates which of the two remaining colors $v$ gets. With a 2-SAT model the problem can then be solved in $O(n+m)$.

This way, the success probability of a single run is $\big(\frac 23\big)^n$. Repeating the algorithm $-\big(\frac 32\big)^n\log \epsilon$ times and outputting a solution as soon as one run finds it guarantees correctness with probability $1-\epsilon$. (See "Analysis of probability upper bounds" below for details.)

***

**Review**: in this problem the "solution space" is the set $\{R,G,B\}^n$, and each time we randomly impose restrictions in order to search for the "target solution", i.e. a valid coloring, within a reduced range.

### Example: [CodeChef SELEDGE](https://www.codechef.com/problems/SELEDGE)

???+ note "Problem summary"
    Given an undirected graph where both vertices and edges have non-negative weights, find a set of edges $S$ of size $\leq K$ that maximizes the sum of weights of the vertices incident to $S$ minus the sum of weights of the edges in $S$. The weight of each vertex is counted only once.

Observation: if three chosen edges form a chain, deleting the middle one is never worse; if some chosen edges form a cycle, deleting any one of them is never worse.

Corollary: the edge set of the optimal solution necessarily forms several disjoint stars (i.e. trees of diameter at most 2).

Corollary: the edge set of the optimal solution necessarily forms a bipartite graph.

We color each vertex independently and uniformly at random with one of two colors, black or white, and require that this coloring is exactly the black-and-white coloring of the bipartite graph corresponding to the optimal solution.

Let us try to compute the probability that the optimal solution satisfies this requirement:

-   Consider a star with $n$ vertices; it obviously has 2 colorings, so the probability that it is colored correctly is $\dfrac 2{2^n}=2^{1-n}$.
-   Suppose the stars in the optimal solution have $a_1,\cdots,a_l$ vertices respectively; then necessarily $(a_1-1)+\cdots+(a_l-1)\leq K$, where $K$ is the maximum number of edges that may be chosen.
-   Hence the probability that all stars are colored correctly is $2^{1-a_1}\cdots 2^{1-a_l}\geq 2^{-K}$.

Under the above requirement, let us try to build a min-cost flow model to compute the optimal answer:

-   Build a bipartite graph: white vertices are on the left and connected to $S$, black vertices are on the right and connected to $T$.
    -   For a white vertex $v$, add an edge from $S$ to it with capacity 1 and cost $-A_v$, and an edge with capacity $\infty$ and cost 0.
    -   For a black vertex $v$, add an edge from it to $T$ with capacity 1 and cost $-A_v$, and an edge with capacity $\infty$ and cost 0.
-   For every edge $(u,v,B)$ of the original graph with $u$ white and $v$ black, add an edge from $u$ to $v$ with capacity 1 and cost $B$.
-   Limit the flow in this graph to at most $K$; the answer is the negation of the minimum cost.

If we solve it with SPFA-based min-cost flow, the complexity is $O\big(K^2(n+m)\big)$. Proof:

-   First, obviously SPFA is run $\leq K$ times.
-   Then, during one run of SPFA, any vertex is pushed into the queue at most $O(K)$ times. This is because:
    -   At any moment at most $3K$ edges carry flow, since otherwise more than $K$ edges would be chosen in the original graph.
    -   On any augmenting path of length $L$, at least $\dfrac L2-2$ edges are reverse edges of some edge carrying flow, because all forward edges go from the left side of the graph to the right side, and only these reverse edges go from the right side to the left.
    -   Combining the two points above, the length of any augmenting path does not exceed $6K+4$.
-   In total, the complexity is $O\big(K^2(n+m)\big)$.

Similarly to the previous problem, we need to repeat the whole procedure $-2^K \log\epsilon$ times to get correctness with probability $1-\epsilon$. Total complexity: $O\big(2^KK^2(n+m)\cdot -\log\epsilon\big)$.

## Hitting the target set with a random element

We need to find an arbitrary element of some set; to do so, we choose elements at random, hoping to hit exactly this set.

### Example: [Gym 101550I](https://codeforces.com/gym/101550/attachments)

???+ note "Problem summary"
    There is a graph of the following shape: two parallel chains, plus two parallel edges connecting the two chains. Given several simple paths in this graph (each path represents a phone call), choose as few edges as possible on which to place wiretaps so that every given path contains at least one wiretap.

The whole graph can be decomposed into a cycle plus four chains sticking out of it. For any of these four chains (call it $C$), consider how to place wiretaps on it:

-   Subject to intercepting all calls conducted entirely inside $C$, use the fewest wiretaps.
-   Subject to the previous point, make the shortest distance from a wiretap on $C$ to the cycle as small as possible.
    -   The purpose of this requirement is to intercept as many calls with exactly one endpoint inside $C$ as possible.

Next, consider the 4 edges in total where the chains meet the cycle; we enumerate by brute force whether or not each of these edges has a wiretap. Obviously, if we want to intercept calls that cross from a chain to the cycle, placing wiretaps on these 4 edges is certainly optimal. Now we can divide the call routes into the following kinds:

1.  Call routes entirely on a chain. These are certainly already intercepted, so they can be ignored.
2.  Call routes crossing from a chain to the cycle that are already intercepted. They can be ignored.
3.  Call routes crossing from a chain to the cycle that are not intercepted. We can simply cut off their part on the chain (since the placement of wiretaps on the chain is already fixed) and keep only the part on the cycle.
4.  Call routes entirely on the cycle.

Thus the problem is reduced to a problem on the cycle.

Suppose that in the optimal solution wiretaps are placed on the set $S$ of edges of the cycle. If we already know any element $e$ of $S$, we can:

-   first cut the cycle into a chain at $e$;
-   then greedily, starting from $e$, repeatedly find the next edge on which to place a wiretap; note that with suitable preprocessing every step of the greedy can be done in $O(1)$;
-   and thereby solve the problem in $O(|S|)$.

So we choose an edge $e'$ on the cycle at random, require $e'\in S$, run the above procedure, repeat several times and take the best result.

Analysis of the complexity of a single run:

-   Observation: let $S'$ denote the optimal solution among all solutions containing $e'$; then $|S'|\leq |S|+1$.
-   Hence the complexity of a single run is $O(|S'|)=O(|S|)$.

Analysis of the success probability:

-   Obviously the success probability of a single run is $\dfrac {|S|}n$, where $n$ is the length of the cycle.
-   So we need $-\dfrac n{|S|}\log\epsilon$ repetitions to get correctness with probability $1-\epsilon$.

In total, the complexity of the algorithm is $O\big(|S|\cdot -\dfrac n{|S|}\log\epsilon\big)=O(-n\log\epsilon)$.

### Example: [CSES 1685 New Flight Routes](https://cses.fi/problemset/task/1685)

???+ note "Problem summary"
    Given a directed graph, add the minimum number of edges so that the graph becomes strongly connected; you must **output a construction**.

First contract the strongly connected components of the original graph. Our goal is obviously to make every sink (vertex with no outgoing edges) able to reach every source (vertex with no incoming edges).

It is not hard to prove that we will only add edges from sinks to sources, because any other added edge corresponds to an edge from a sink to a source that is no weaker than it.

Our core operation is: take a sink $t$ and a source $s$ (they need not be in the same weakly connected component) and add the edge $t\to s$ so that **neither $s$ nor $t$ is a sink or a source anymore** (call this goal I). Ideally, each such operation reduces the number of sinks and the number of sources by one each, and we keep operating until only one sink or only one source remains, which is a trivial situation. Hence we conjecture that the answer is the maximum of the number of sources and the number of sinks.

It is not hard to see that the above operation achieves goal I if and only if $t$ has a predecessor other than $s$ and $s$ has a successor other than $t$. It can be proved (the proof is given shortly) that in any DAG with at least two sources and at least two sinks such a pair $(s,t)$ exists; but the existence result does not help us construct a solution, and further analysis is needed.

-   Even with this necessary and sufficient condition it is hard to obtain an algorithm directly, mainly because adding the edge $t\to s$ may affect the validity of other pairs $(s',t')$, which is hard to handle.

Note that we know very little about the relations between sources and sinks (even quickly querying whether a pair $s-t$ is reachable requires DFS + bitset preprocessing, which the time limit does not allow); this suggests that we need some very general and powerful property.

Observation: there are at most $n+m-1$ pairs $(s,t)$ that do not satisfy goal I, where $n$ is the number of sources and $m$ is the number of sinks.

-   Reason: if every such pair $(s,t)$ is regarded as an edge between $s$ and $t$, the graph formed by all these edges looks like several disjoint chains, so the number of edges does not exceed the number of vertices minus one.
-   The motivation for this observation is that, in order to apply an existence result in an algorithm, the preliminary step is often to strengthen the qualitative result into a quantitative one.

Corollary: choosing $(s,t)$ uniformly at random, the probability that it satisfies the above requirement is $\geq \dfrac {(n-1)(m-1)}{nm}$.

-   Note that this result is strictly stronger than the existence result given earlier.

Corollary: if we independently and uniformly at random choose $\dfrac {\min(n,m)}2$ pairs $(s,t)$ with no common elements in succession and perform the operation on them **in order** (i.e. add the edges $t\to s$), the probability that all these operations satisfy goal I is $\geq \dfrac 14$.

-   Reason:

$$
\begin{aligned}
&\phantom{=\ }\dfrac {(n-1)(m-1)}{nm}\cdot\dfrac{(n-2)(m-2)}{(n-1)(m-1)}\cdots\dfrac{(n-k)(m-k)}{(n-k+1)(m-k+1)}\\
&=\dfrac{(n-k)(m-k)}{nm}\\
&\geq \dfrac 14
\end{aligned}
$$

And after choosing $k$ pairs $(s,t)$ in succession, checking whether all of them satisfy goal I is easy: just contract the strongly connected components once more and check whether both $n$ and $m$ decreased by $k$. Note that if they decrease by $k=\dfrac{\min(n,m)}2$ each time, then $\min(n,m)$ necessarily becomes 1 within $O\big(\log(n+m)\big)$ rounds, which brings us to the trivial case.

???+ note "Pseudocode of the algorithm"
    ```text
    while(n>1 and m>1):
        randomly choose k=min(n,m)/2 pairs (s,t)
        add edge t->s for all these pairs
        if new_n>n-k or new_m>m-k:
            roll_back()
    solve_trivial()
    ```

Complexity: $O\big((|V|+|E|) \log |V|\big)$.

***

**Review**: we needed to find any pair $(s,t)$ achieving goal I, so we chose $(s,t)$ at random.

## Obtaining properties of random data through randomization

If the data of a problem is generated randomly, we may be able to solve it by exploiting properties of random data. And in some cases, even if the data is not generated randomly, we can use randomization to give it some properties of random data, which helps to solve the problem.

### Example: randomized incremental algorithm

A randomly generated sequence of elements may have properties such as "the expected number of changes of the prefix optimum is very small", and the randomized incremental algorithm obtains these properties by randomly shuffling the input sequence.

See [Randomized incremental algorithm](../geometry/random-incremental.md) for details.

### Example: randomized solution of [TopCoder MagicMolecule](https://archive.topcoder.com/ProblemStatement/pm/11705)

???+ note "Problem summary"
    Given an undirected graph with $n$ vertices and vertex weights, among all cliques of size at least $\dfrac {2n}3$, find the one with the maximum sum of vertex weights.
    
    $n\leq 50$

It is easy to think of meet in the middle. Split the vertex set evenly into a left half and a right half $V_L,V_R$ (both of size $\dfrac n2$), and compute the array $f_{L,k}$, the maximum weight sum over all cliques with $\geq k$ elements inside the vertex set $L\subseteq V_L$. Then we enumerate every clique $C_R$ of the right half, compute which vertices of the left half are connected to all vertices of $C_R$ (call this vertex set $N_L$), and update the answer with $f_{N_L,\frac 23 n-|C_R|}+\textit{value}(C_R)$.

-   Note that every $f_{L,k}$ can be computed with an $O(1)$ transition. Concretely, take $d$ to be an arbitrary element of $L$ and distinguish cases:
    -   If in the optimal solution $d$ is not in the clique, the transition is from $f_{L\setminus \{d\},k}$.
    -   If in the optimal solution $d$ is in the clique, the transition is from $f_{L\cap N(d),k}+\textit{value}(d)$, where $N(d)$ is the set of neighbors of $d$.
    -   Do not forget to also update $f_{L,k}$ with $f_{L,k+1}$.

This solution exceeds the time limit. Let us try to optimize:

-   Split the vertex set in half uniformly at random. Then, with considerable probability, the vertex set $C_{res}$ of the optimal solution is also split exactly in half (i.e. $|C_{res}\cap V_L|=|C_{res}\cap V_R|$).
    -   Of course, $|C_{res}|$ may be odd. For simplicity we assume here that it is even; the odd case does not change the solution essentially.
    -   Experiments show that with about 20 random attempts, with very high probability at least one satisfies this property. In other words, if our algorithm relies on the property "$C_{res}$ is split in half", then repeating the algorithm 20 times and taking the best result also guarantees the correct answer with very high probability.
-   With this property, we can directly require that both the left clique $L$ and the right clique $C_R$ have size $\geq \dfrac n3$. This brings two improvements to the complexity:
    -   $f$ can drop the dimension recording the size.
    -   Since only cliques of size $\geq \dfrac n3$ need to be considered, the number of left cliques $L$ and right cliques $C_R$ to consider is also greatly reduced, to about $1.8\cdot 10^6$.
-   Now the bottleneck becomes computing the weight sum of some subset on one side, because this requires $O\big(2^{|V_L|}+2^{|V_R|}\big)$ preprocessing.
    -   Solution: split in half again inside $V_L$ and $V_R$; when querying the weight sum of a subset, split the subset into a left and a right half, query each, and add the answers.
-   This passes the problem.

***

**Review**: a random set has the property "the sizes of the two halves of a partition do not differ too much", and we obtained this property through a random partition.

## Randomization for hashing

### Example: [UOJ #207 共价大爷游长沙](https://uoj.ac/problem/207) ("Covalent Grandpa Tours Changsha")

???+ note "Problem summary"
    Maintain a dynamically changing tree and a dynamically changing set of pairs of vertices. You need to support:
    
    -   deleting and adding an edge, with the guarantee that the result is still a tree;
    -   adding/deleting a pair of vertices;
    -   given an edge $e$, deciding whether, for every pair of vertices $(s,t)$ in the set, $e$ lies on the simple path between $s$ and $t$.

For every edge $e$ of the graph we define the set $S_e$ as the set of key paths (i.e. the pairs $(a,b)$ from the problem) passing through this edge. Consider dynamically maintaining a hash of the set $S_e$ for every edge; then we can easily decide whether $S_e$ equals the full set (i.e. whether $e$ is a "must-pass edge").

The hashing works as follows: assign to every $(a,b)$ a random non-negative integer $H_{(a,b)}$ below $2^{64}$; the hash of a set is then the XOR of the $H$ values of its elements.

In this way, the hash of any fixed set is necessarily uniformly distributed on $R:=\left\{0,1,\cdots,2^{64}-1\right\}$ (in other words, the hash takes values in $R$, each with equal probability). This is because:

1.  A single $H_{(a,b)}$ is obviously uniformly distributed.
2.  The XOR of two independent random variables uniformly distributed on $R$ is necessarily also uniformly distributed on $R$. The proof is not hard and is left to the reader.

Hence the correctness of the algorithm is guaranteed.

As for maintaining this hash, an LCT (link-cut tree) suffices.

### Example: [CodeChef PANIC](https://www.codechef.com/problems/PANIC) and analysis of its error rate

Rough outline of the solution:

1.  It can be proved[^ref1] that $S(N)$ satisfies a linear recurrence of order $O(K)$ in $N$.
2.  Find this recurrence with the BM (Berlekamp–Massey) algorithm.
3.  Using the recurrence, compute $S(N)$ with the Cayley–Hamilton theorem.

Here we only focus on the second part, namely how to find the recurrence of a sequence of matrices. So we only need to consider the following problem:

???+ note "Problem"
    Given a sequence of matrices that satisfies a homogeneous linear recurrence modulo $P:=998244353$ (scalar multiplication and addition in the recurrence are defined as scalar multiplication and addition of matrices), find the shortest recurrence.

If a sequence of matrices satisfies a recurrence $F$, then each of its entries also satisfies $F$. However, if we compute the shortest recurrence $F'$ for a single entry, $F'$ may be shorter than $F$, which causes a problem.

Solution: assign to every entry $(i,j)$ of the matrix a random weight $x_{i,j}<P$, then for every matrix in the sequence compute the weighted sum of all its entries modulo $P$, string the numbers computed for the individual matrices into a sequence, and finally run the BM algorithm on the resulting sequence.

Error rate analysis:

-   Suppose the above procedure found a recurrence $F'$ of order $l$ different from $F$ (and obviously not longer than $F$).
-   Since the sequence of matrices does not satisfy $F'$, there must exist an entry $(i,j)$ of the matrix such that the corresponding sequence $S_{i,j}$ does not satisfy $F'$ at some $N$. That is:

$$
S(N)_{i,j}-F'_1S(N-1)_{i,j}-\cdots-F'_lS(N-l)_{i,j}\not\equiv 0\pmod {P}
$$

-   Suppose $(i,j)$ is the only entry that does not satisfy the recurrence; then necessarily:

$$
T_{i,j}:=\Big(x_{i,j}\cdot\big(S(N)_{i,j}-F'_1S(N-1)_{i,j}-\cdots-F'_lS(N-l)_{i,j}\big)\bmod P\Big)=0
$$

-   Obviously this holds only when $x_{i,j}=0$, which has probability $P^{-1}$.
-   What if there are several entries that do not satisfy the recurrence?
    -   For every such entry $(i,j)$, it is easy to prove that $T_{i,j}$ is uniformly distributed on $R:=\{0,1,\cdots,P-1\}$.
    -   The sum (in the modular sense) of several mutually independent random variables uniformly distributed on $R$ is still uniformly distributed on $R$. The proof is not hard and is left to the reader.
    -   Hence the error rate in this case is also $P^{-1}$.

### Example: [UOJ #552 同构判定鸭](https://uoj.ac/problem/552) ("Isomorphism-Checking Duck") and analysis of its error rate

???+ note "Problem summary"
    Given two directed graphs $G_0,G_1$ whose edges are labeled with lowercase letters, for each of the two graphs compute "the multiset of strings corresponding to all paths" (possibly an infinite set), and decide whether these two multisets are equal. If they are not equal, you must output a shortest string whose numbers of occurrences in the two multisets differ.

Let $f_{K,i,j}$ denote the hash of the multiset of all strings corresponding to all paths of length $j$ in the graph $G_K$ starting at vertex $i$. Consider the states in increasing order of $j$; for the transition, enumerate the outgoing edges of $i$ and require that this edge is the first edge of the path.

To decide whether a bad string of length $=L$ exists, it suffices to "aggregate" $\{f_{0,*,L}\}$ and $\{f_{1,*,L}\}$ separately and compare them (the wildcard `*` here stands for every vertex; e.g. $\{f_{0,*,L}\}$ denotes the set of all $f_{0,i,L}$ where $i$ ranges over all vertices). The official editorial[^ref2] proves that the length of the shortest bad string (if it exists) does not exceed $n_1+n_2$, so the complexity of this solution is reliable.

Next, consider the concrete hashing method. Note that the usual hashing method, i.e. mapping the string $a_1a_2\cdots a_k$ to $\big(a_1+Pa_2+P^2a_3+\cdots+P^{k-1}a_k\big)\bmod Q$ and defining the hash of a multiset as the sum of the hashes of its elements modulo $Q$, does not work here. A counterexample: the sets `{"ab","cd"}` and `{"cb","ad"}` have the same hash regardless of the values of $P,Q$.

The problem with the above approach is that the hash of a string is a sum, so each of its terms can be split off and recombined. To avoid this problem, we consider turning the hash into a product. Moreover, the commutativity of multiplication would make different positions indistinguishable; to avoid this we assign different weights to different positions.

For every pair $(c,j)$ (where $c$ is a character and $j$ is an integer denoting the position of $c$ within some string) we generate a random number $x_{c,j}$ in advance. Then we map the string $a_1a_2\cdots a_k$ to $x_{a_1,1}x_{a_2,2}\cdots x_{a_k,k}\bmod Q$ (where $Q$ is a **randomly chosen** prime), and define the hash of a multiset as the sum of the hashes of its elements modulo $Q$. Next we analyze its error rate.

???+ note "(*) Schwartz–Zippel lemma"
    Let $f\in F[z_1,\cdots,z_k]$ be a nonzero polynomial in $k$ variables of degree $d$ over a field $F$, and let $S$ be a finite subset of $F$. Then at most $d\cdot |S|^{k-1}$ tuples $(z_1,\cdots,z_k)\in S^k$ satisfy $f(z_1,\cdots,z_k)=0$.
    
    ??? note "If you do not know what a field is"
        You only need to remember that these two things are fields:
        
        1.  The residue system modulo a prime, with its operations.
        2.  The set of real numbers, with its operations.
    
    Corollary: if $z_1,\cdots,z_k$ are all chosen independently and uniformly at random from $S$, then $\mathrm{Pr}\big[f(z_1,\cdots,z_k)=0\big]\leq \dfrac d{|S|}$.

Let $F$ denote the field corresponding to the residue system modulo $Q$. Then for an $L\leq n_1+n_2$, $\sum\limits_i f_{0,i,L}$ and $\sum\limits_i f_{1,i,L}$ each correspond to a multivariate polynomial of degree $L$ over $F$ in the set of variables $\{x_{*,*}\}$; let us denote these two polynomials $P_0,P_1$.

If two different multisets of strings have the same hash, there are two possibilities:

1.  $P_0\equiv P_1\pmod {Q}$, i.e. the coefficients of every term of $P_0$ and $P_1$ are equal modulo $Q$.
2.  $P_0\not\equiv P_1\pmod {Q}, P_0(x_{*,*})\equiv P_1(x_{*,*})\pmod {Q}$, i.e. $P_0,P_1$ are not identically equal, but the set of values $\{x_{*,*}\}$ we chose happens to make their values at this point equal.

Analysis of the probability of the former:

-   Observation: for arbitrary $A\neq B; A,B\leq N$ and a randomly chosen prime $Q\leq Q_{\max}$, we necessarily have:

$$
\mathrm{Pr}\big[A\equiv B\pmod {Q}\big]=O\Big(\dfrac{\log N \log Q_{max}}{Q_{max}}\Big)
$$

-   This is because: any $Q$ making $A\equiv B$ hold must satisfy $Q\big|(A-B)$, and there are $\omega(A-B)\leq \log_2 N$ such $Q$; by the prime number theorem, there are $\Theta\Big(\dfrac {Q_{\max}}{\log Q_{\max}}\Big)$ distinct primes up to $Q_{\max}$. Dividing the two gives the formula above.
-   In the above observation, take $A,B$ (with $A\neq B$) to be the coefficients of some particular term in $P_0,P_1$ (which equal the numbers of occurrences of the string corresponding to this term in $G_0,G_1$); then it is easy to see that $A,B\leq (m_1+m_2)^{L}$, giving:

$$
\mathrm{Pr}\big[A\equiv B\pmod {Q}\big]=O\Big(\dfrac{L\log (m_1+m_2) \log Q_{max}}{Q_{max}}\Big)
$$

-   So taking $Q_{\max}\approx 10^{12}$ is more than enough. If the machine cannot support arithmetic on such large integers, double hashing can be used instead.

Analysis of the probability of the latter:

-   In the Schwartz–Zippel lemma:
    -   take the field $F$ to be the field corresponding to the residue system modulo $Q$;
    -   take $f(x_{*,*})=P_0(x_{*,*})-P_1(x_{*,*})$, a nonzero polynomial of degree $L$;
    -   take $S=F$.
-   We get: the desired probability is $\leq \dfrac LQ$.

Note that we need to guarantee correctness for every $L$, so to be rigorous we also need the union bound (see below).

In practice we do not have to choose the modulus at random, because, for instance, using your own birthday as the modulus is effectively already a random number.

### Example: (\*) number of distinct elements in a submatrix

???+ note "Problem"
    Given an $n\times m$ matrix, answer $q$ queries for the number of distinct elements in a contiguous submatrix; an online algorithm is required.
    
    A relative error of $\epsilon$ and an error rate of $\delta$ are allowed; in other words, for at least $(1-\delta)q$ queries you must give an answer whose relative error with respect to the correct answer does not exceed $\epsilon$.
    
    $n\cdot m\leq 2\cdot10^5;q\leq 10^6;\epsilon=0.5,\delta=0.2$

Lemma: let $X_{1\cdots k}$ be mutually independent random variables uniformly distributed on $[0,1]$. Then $\mathrm{E}\big[\min\limits_i X_i\big]=\dfrac 1{k+1}$.

-   Proof: consider a unit circle on which $k+1$ points are distributed with uniformly random **relative positions**, at positions $0,X_1,X_2,\cdots,X_k$ respectively. Then $\min\limits_i X_i$ equals the length of one particular gap among the $k+1$ gaps. Since these gaps are "symmetric", the expected length of any particular gap is $\dfrac 1{k+1}$.

We take $k$ to be the number of distinct elements and use the above lemma to recover $k$ from $\min\limits_i X_i$.

Consider using some hash function that maps every element of the matrix uniformly and independently at random to a real number in $[0,1]$, with equal elements mapped to equal real numbers. Then the real numbers corresponding to all elements of a submatrix, after removing duplicates, are exactly an instance of the earlier set $\{X_1,\cdots,X_k\}$, where $k$ equals the number of distinct elements in the submatrix.

Thus we obtain an algorithm:

1.  Assign hash values in $[0,1]$ to the elements of the matrix. To guarantee randomness, the hash function can be implemented directly with a `map` and a random number generator: whenever a new, previously unseen value appears, give it a random hash value.
2.  When answering a query, find the minimum $M$ of the hash values in the submatrix and output $\dfrac 1M-1$.

However, this algorithm is not satisfactory. The expectation of its output is $\mathrm{E}\Big[\dfrac 1{\min\limits_i X_i}-1\Big]$, but in fact this value does not equal $\dfrac 1{\mathrm{E}\big[\min\limits_i X_i\big]}-1=k$; rather (it can be proved) it equals $\infty$.

That is, we cannot directly put a single realization of $\min\limits_i X_i$ in the denominator; we must first compute its expectation and then put the expected value in the denominator.

How to compute the expectation? Sample at random several times and take the average.

We run the above procedure with $C$ different groups of hash functions; when answering a query we compute $C$ different values of $M$, compute their average $\overline M$, and output $\big(\overline M\big)^{-1}-1$.

Experiments show that $C\approx 80$ suffices to meet the requirements. The rigorous proof is very tedious and is omitted here.

Finally, how to find the minimum in a submatrix? A two-dimensional sparse table suffices: preprocessing $O(nm\log n\log m)$, answering a query $O(1)$.

## Other applications of randomization in algorithms

Other roles of randomization include:

-   Preventing the test data author from breaking the solution with specially crafted data. For example, randomly shuffling the order of neighbors during a search.
-   Guaranteeing that the "operations" performed during the algorithm are (in some sense) uniform. For example, the [simulated annealing](../misc/simulated-annealing.md) algorithm.

In these scenarios randomization is often (but not always) associated with heuristic hacks and attempts to scrape partial points.

### Example: ["TJOI2015" 线性代数](https://loj.ac/problem/2100) ("Linear Algebra")

The standard algorithm for this problem is network flow, but here we adopt the following heuristic approach:

-   Each time pick a random position, flip the value at this position, compare and update the answer.

??? note "Code"
    ```cpp
    #include <algorithm>
    #include <cstdlib>
    #include <iostream>
    
    int n;
    
    int a[510], b[510], c[510][510], d[510];
    int p[510], q[510];
    
    int maxans = 0;
    
    void check() {
      memset(d, 0, sizeof d);
      int nowans = 0;
      for (int i = 1; i <= n; i++)
        for (int j = 1; j <= n; j++) d[i] += a[j] * c[i][j];
      for (int i = 1; i <= n; i++) nowans += (d[i] - b[i]) * a[i];
      maxans = std::max(maxans, nowans);
    }
    
    int main() {
      srand(19260817);
      std::cin >> n;
      for (int i = 1; i <= n; i++)
        for (int j = 1; j <= n; j++) std::cin >> c[i][j];
      for (int i = 1; i <= n; i++) std::cin >> b[i];
      for (int i = 1; i <= n; i++) a[i] = 1;
      check();
      for (int T = 1000; T; T--) {
        int tmp = rand() % n + 1;
        a[tmp] ^= 1;
        check();
      }
      std::cout << maxans << '\n';
    }
    ```

### Example: (\*) randomized heap[^ref3]

The most common implementation of a mergeable heap is probably the leftist tree, which keeps the tree leaning left by maintaining tree heights, thereby guaranteeing the complexity of merging. However, maintaining heights is a bit troublesome, and we would like to avoid it.

So we can consider using a randomized heap: instead of swapping children according to tree height, we swap them randomly.

???+ note "Code"
    ```cpp
    struct Node {
      int child[2];
      long long val;
    } nd[100010];
    
    int root[100010];
    
    int merge(int u, int v) {
      if (!(u && v)) return u | v;
      int x = rand() & 1, p = nd[u].val > nd[v].val ? u : v;
      nd[p].child[x] = merge(nd[p].child[x], u + v - p);
      return p;
    }
    
    void pop(int &now) { now = merge(nd[now].child[0], nd[now].child[1]); }
    ```

A randomized heap imposes no hard or soft requirements on the shape of the heap; the expected complexity of the merge operation holds for any two heaps (as arguments of the `merge` function). We prove this below.

???+ note "Proof of the expected complexity"
    We will prove: for an arbitrary heap $A$, if we start from the root and each time randomly go left or right (until we can go no further), the expected length of the path (i.e. the number of vertices on the path) is $h(A)\leq\log_2 (|A|+1)$.
    
    -   Note that in the above procedure the expected complexity of merging heaps $A,B$ is $O\big(h(A)+h(B)\big)$, so the above claim guarantees the expected complexity of the randomized heap.
    
    The proof is by mathematical induction. The base case is $A$ being empty, where the claim is obvious. From now on assume $A$ is nonempty.
    
    Let the two subtrees of $A$ be $L,R$. Then:
    
    $$
    \begin{align} h(A)
    &=1+\frac{h(L)+h(R)}2
    \\&\leq1+\frac{\log_2(|L|+1)+\log_2(|R|+1)}2
    \\&=\log_2{2\sqrt{(|L|+1)(|R|+1)}}
    \\&\leq\log_2{\frac{2\big((|L|+1)+(|R|+1)\big)}2}
    \\&=\log_2{(|A|+1)} \end{align}
    $$
    
    This completes the proof.

## Proof techniques related to randomness

Below we list a few rather useful techniques.

Naturally, these few items cannot be everything; if you know a technique that is not listed, feel free to add it.

### Analysis of probability upper bounds

See the page [Probability inequalities](../math/probability/concentration-inequality.md) for details.

Besides the various inequalities mentioned on that page, the following result is also frequently used in derivations:

**Use of Euler's number**: $\Big(1-\dfrac{1}{n}\Big)^n\leq \dfrac{1}{\mathrm{e}},\forall n\geq1$

-   The left-hand side is monotonically increasing in $n\geq 1$ and its limit at $+\infty$ is $\dfrac{1}{\mathrm{e}}$, hence the result.
-   This tells us that if there are $n$ mutually independent events, each occurring with probability $1-\dfrac 1n$, then the probability that all of them occur is at most $\dfrac{1}{\mathrm{e}}$.

### The idea of "coupling"

The idea of "coupling" is often used when handling more than one random object at the same time, or when handling a random object and a deterministic object at the same time.

#### Introduction: connectivity of random graphs

???+ note "Problem"
    For $n \in \mathbf{N}^*; p,q\in [0,1]$ with $q\leq p$, prove: the expected number of connected components of the random graph $G_1(n,p)$ does not exceed the expected number of connected components of the random graph $G_2(n,q)$. Here $G(n,\alpha)$ denotes a simple undirected graph $G$ with $n$ vertices in which each of the $\dfrac {n(n-1)}2$ possible edges appears with probability $\alpha$, these probabilities being mutually independent.

This result looks as natural as can be, but a rigorous proof is not so easy.

???+ note "Proof idea"
    Imagine that each of the two graphs uses a 0/1 random number generator to learn whether each edge exists, where the generator $T_1$ of $G_1$ outputs 1 with probability $p$ each time, and the generator $T_2$ of $G_2$ outputs 1 with probability $q$ each time. Then, to construct a graph, it suffices to run the corresponding generator $\dfrac {n(n-1)}2$ times.
    
    Now we merge the two generators into one. Consider a random number generator $T$ that each time outputs 0 with probability $q$, 1 with probability $p-q$, and 2 with probability $1-p$. If we run this $T$ $\dfrac {n(n-1)}2$ times, we can construct $G_1$ and $G_2$ simultaneously. Specifically, if the output is 0, we consider the current edge to be in neither $G_1$ nor $G_2$; if the output is 1, we consider the current edge to be only in $G_1$; if the output is 2, we consider the current edge to be in both $G_1$ and $G_2$.
    
    It is easy to verify that the $G_1$ and $G_2$ generated this way conform to their definitions, and that in every instance the edge set of $G_2$ is a subset of the edge set of $G_1$. Therefore in every instance the number of connected components of $G_2$ is at least the number of connected components of $G_1$; then the expectations naturally satisfy the same relation.

The idea used in this proof is called "coupling", and it can be understood literally. In this example it manifests as merging two originally independent random processes into one.

#### Application: [NERC 2019 Problem G: Game Relics](https://codeforces.com/contest/1267/problem/G)

???+ note "Problem summary"
    There are several items, each with a price $c_i$. You want to obtain all items, and to do so you may perform two operations arbitrarily:
    
    1.  Choose an item $i$ you do not own yet and buy it for $c_i$ coins.
    2.  Pay $x$ coins and draw one item uniformly at random from all items (including those you already own). If you do not own this item yet, you obtain it; otherwise you get nothing, but $\dfrac x2$ coins are refunded. $x$ is a constant given in the input.
    
    Find the expected cost under the optimal strategy.

Observation: if we choose to draw, we will certainly keep drawing until we obtain a new item.

-   Reason: if a draw does not yield a new item, the new situation is exactly the same as the situation before the draw, so if the optimal move in the old situation was "draw once", then the optimal move in the new situation must also be "draw once more".

We can compute $f_k$: if we currently own $k$ distinct items, how much we expect to pay to draw a new item. By the observation just made, we can directly treat $f_k$ as a fixed cost, i.e. transform the problem into "each time pay $f_k$ coins to randomly obtain a new item".

???+ note "Computing the expected cost"
    Obviously $f_k=\dfrac x2 \cdot (R-1)+x$, where $R$ is the expected number of draws needed to get a new item.
    
    Lemma: if a coin shows heads with probability $p$, the expected number of tosses until the first heads is $\dfrac 1p$.
    
    -   Intuitively: $\dfrac 1p \cdot p = 1$, so in that many tosses we expect to get 1 heads, which looks right.
    -   This intuition can be made rigorous via the [law of large numbers](https://en.wikipedia.org/wiki/Law_of_large_numbers), i.e. by considering $n\to \infty$ experiments of "keep tossing the coin until heads". Details of the derivation are omitted.
    -   Another feasible proof is to plug in the definition of expectation directly and compute by brute force. Details of the derivation are omitted.
    
    Obviously the probability that one draw yields a new item is $\dfrac {n-k}n$, so $R=\dfrac n{n-k}$.

Conclusion: the optimal strategy must be to first draw several times, and then buy all items that were not drawn.

This conclusion agrees with intuition, because $f_k$ is increasing in $k$, so drawing early does seem a bit better than drawing late.

???+ note "Proof"
    First consider proving a special case. We will prove:
    
    -   random process $A$: first buy item $x$, then keep drawing until all items are obtained
    -   ... is certainly no better than ...
    -   random process $B$: keep drawing until all items other than $x$ are obtained, then buy $x$ if we still do not have it.
    
    Consider letting random processes $A$ and $B$ use the same random number generator. That is, the first draw of $A$ and the first draw of $B$ yield the same element, and likewise for the second, third ...
    
    Obviously, the numbers of draws of $A$ and $B$ are then necessarily equal. For an item $y\neq x$ drawn by $A$, observe that:
    
    -   the number of items already owned when $A$ draws $y$ is certainly greater than or equal to the number of items already owned when $B$ draws $y$.
    
    Therefore the cost of a single draw in $B$ is no higher than the cost of a single draw in $A$, and hence the total cost of drawing is also no higher than in $A$.
    
    Obviously the purchase cost of $B$ is likewise no higher than that of $A$. In summary, $B$ is certainly no worse than $A$.
    
    Then this result can be generalized to the general case by mathematical induction. Specifically, each time we find the last purchase in the current strategy, and by the above result, moving this purchase to the end is certainly no worse. Details omitted.

Based on this conclusion, we transform the problem equivalently once more: change the operation "choose an item and pay its price to buy it" into "randomly choose an item not yet owned and pay its price to buy it". The reason for the equivalence is that, since purchases are only used for cleaning up at the end, it does not matter which item is chosen.

Now we find that "drawing" and "buying" have essentially become the same operation, differing only in the price paid. The choice between buying and drawing has no influence at all on the order in which items are obtained, and every order of obtaining items is equally likely.

Observation: at a given moment, we should choose to buy if and only if the cost of the next draw (determined by the number of items already drawn) is greater than the average price of the remaining items (if they are equal, either choice is fine).

-   It can be proved that, as time goes on, the growth rate of the drawing cost is never lower than the growth rate of the average price of the remaining items. This shows that there is only one "critical point" of switching from drawing to buying, which further confirms the earlier conclusion.

Finally, we enumerate all possible situations (i.e. sets of already owned elements), compute the probability of each situation occurring (the number of arrangements of the owned elements divided by the total number of arrangements), multiply by the cost of the optimal decision in this situation (determined by the number of owned elements and the total price of the remaining items), and add everything up. This process can be optimized with a knapsack-style DP, which passes the problem.

***

**Review**: we can see that the coupling technique is used twice in this problem. The first time is in the proof, where we let two random processes use the same random source; the second time is when buying is turned into random buying (i.e. a random source is introduced), so that the two operations of buying and drawing are essentially "coupled" into the same operation (i.e. the drawing and buying operations share one random source).

## References

[^ref1]: [PANIC - Editorial](https://discuss.codechef.com/t/panic-editorial/80145)

[^ref2]: [UOJ NOI Round #4 Day2 题解](https://peehs-moorhsum.blog.uoj.ac/blog/6375) (editorial)

[^ref3]: [Anna Gambin and Adam Malinowski, Randomized Meldable Priority Queues](https://www.researchgate.net/publication/2801527_Randomized_Meldable_Priority_Queues)
