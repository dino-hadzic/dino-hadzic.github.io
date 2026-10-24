---
title: Basics of the theory of computation
---

This section introduces basic knowledge of the theory of computation. This content does not play a big role in OI (but it is still slightly useful: if you encounter an NP-hard problem, you may assume that it has no solution of polynomial complexity), so you can learn it out of interest or as preparation for future studies.

Many conclusions in this article are stated without proof; if you are interested, you can look up the corresponding proofs yourself.

Prerequisites: [Time complexity](../basic/complexity.md).

## Problems

### Languages

An **alphabet** is a non-empty finite set; the elements of this set are called **symbols**.

Let $\Sigma^\ast$ denote the set of strings formed by concatenating a non-negative number of symbols from $\Sigma$; a **language** over the alphabet $\Sigma$ is a subset of $\Sigma^\ast$.

Note that "language" here is an abstract concept: strings in the usual sense form a language, but the set of all directed acyclic graphs can also be a language (a bijection can be established between 01-strings and directed graphs; the concrete method does not need to be known).

Since any language can be converted into the form of 01-strings, in the following text $\Sigma=\{0, 1\}$ unless stated otherwise.

### Decision problems

A decision problem is a problem that can only be answered with YES/NO; in essence it is deciding whether a string belongs to a language, i.e. $f:\Sigma^\ast\rightarrow\{0, 1\}, f(x)=1\iff x\in L$ is a decision problem for the alphabet $\Sigma$ and the language $L$. For example, "decide whether a graph is a directed acyclic graph" is a decision problem.

Because of their simplicity, decision problems are often the object of study in the theory of computation. Unless stated otherwise, "problem" in this article means "decision problem"; of course, some statements can sometimes be easily generalized to other problems.

A language can also refer to the decision problem "decide whether a string belongs to this language", so "language" and "problem" can be regarded as synonyms.

### Function problems

The answer to a function problem is not only YES/NO; it can be a number or something else. For example, "compute the sum of two numbers" is a function problem.

Any function problem can be converted into a decision problem; for example, "compute the sum of two numbers" can be converted into "decide whether the sum of two numbers equals a third number".

A decision problem can also be converted into a function problem: compute the indicator function of the decision problem, i.e. the function $f$ in the definition of a decision problem above.

## Turing machines

### Deterministic Turing machines

Unless stated otherwise, "Turing machine" usually means "deterministic Turing machine"; this is also the case in this article.

There are many different definitions of a Turing machine; here we pick one of them, and Turing machines under other definitions are usually equivalent in computational power to the Turing machine defined below.

A Turing machine is a machine that operates on a tape that extends infinitely in both directions and is divided into cells; it has internal states and a head that can modify the tape and move along it.

Formally, a Turing machine is a 7-tuple $M=\langle Q,\Gamma,b,\Sigma,\delta,q_0,F\rangle$, where:

-   $Q$ is a finite non-empty **set of states**;
-   $\Gamma$ is a finite non-empty **tape alphabet**;
-   $b\in\Gamma$ is the **blank symbol**, the only symbol that may appear on the tape infinitely often during the computation;
-   $\Sigma\subseteq(\Gamma\setminus\{b\})$ is the **set of input symbols**, the symbols that may appear on the initial tape (i.e. the input);
-   $q_0\in Q$ is the **initial state**;
-   $F\subseteq Q$ is the set of **accepting states**; if a Turing machine halts in some accepting state, we say that the contents of the initial tape are **accepted** by this Turing machine.
-   $\delta :(Q\setminus F)\times \Gamma \not \to Q\times \Gamma \times \{L,R\}$ is a partial function (i.e. a function defined only on a subset of its domain) called the **transition function**. If $\delta$ is undefined in the current state, the Turing machine halts.

Starting from the initial state and the beginning of the tape, at each step the Turing machine acts according to the current internal state $x$ and the symbol $y$ in the tape cell currently pointed to by the head: if $\delta(x, y)$ is undefined, it halts; otherwise, if $\delta(x, y)=(a, b, c)$, it changes the internal state to $a$, changes the symbol in the cell pointed to by the head to $b$, and moves one cell to the left if $c$ is $L$, or one cell to the right if it is $R$.

Actually, knowing the details of how a Turing machine works is unnecessary; it suffices to build an intuitive understanding.

The output of a Turing machine $M$ on input $x$ is written $M(x)$ ($M(x)=1$ if and only if $M$ accepts $x$, and $M(x)=0$ if and only if $M$ halts within finitely many steps on input $x$ and $M$ does not accept $x$); the parentheses may also contain several arguments separated by commas, and in a concrete implementation an element representing the comma can be added to the alphabet to separate the arguments.

The time complexity of solving a problem on a Turing machine and on a von Neumann computer differs by at most a polynomial factor, so a Turing machine can be used as the computational model when studying complexity classes.

### Non-deterministic Turing machines

A non-deterministic Turing machine is a kind of Turing machine; it differs from a deterministic Turing machine in that a deterministic Turing machine can only transition to one state at each step, while a non-deterministic Turing machine can transition to several states "simultaneously", thus computing in parallel in several "branches"; as soon as one of these "branches" halts in an accepting state, the non-deterministic Turing machine accepts the input.

In fact, any deterministic Turing machine can simulate the polynomial-time behavior of a non-deterministic Turing machine in exponential time, in a way similar to iterative deepening search.

In real life, a deterministic Turing machine corresponds to a single-core processor that only supports serial processing, while a non-deterministic Turing machine corresponds to an ideal multi-core processor that supports parallel processing of unlimited size.

### Multi-tape Turing machines

A standard Turing machine can only operate on one tape, but for convenience this article studies multi-tape Turing machines. For a $k$-tape Turing machine, one of the tapes is a read-only input tape, while the remaining $k-1$ tapes can be read and written, and one of these $k-1$ tapes is used for output.

The number of tapes of a multi-tape Turing machine must be finite.

The space used by a multi-tape Turing machine is the number of cells visited by the heads on all tapes other than the input tape.

### Encoding of Turing machines

Turing machines can be encoded by natural numbers, i.e. there is a surjective function $f:\mathbb{N}\to\mathbb{M}$ such that every natural number corresponds to a Turing machine, and every Turing machine has infinitely many encodings. Therefore, a set consisting of several Turing machines can be a language.

The Turing machine encoded by the natural number $\alpha$ is denoted $M_{\alpha}$.

### Universal Turing machine

There is a Turing machine $\mathcal U$ satisfying:

1.  if $M_{\alpha}$ halts in finite time on input $x$, then $\mathcal{U}(x, \alpha)=M_{\alpha}(x)$; otherwise $\mathcal{U}(x, \alpha)$ does not halt in finite time;
2.  if for every $x\in\{0, 1\}^\ast$, $M_\alpha$ halts within time $T(|x|)$ on input $x$, then for every $x\in\{0, 1\}^\ast$, $\mathcal{U}(x, \alpha)$ halts within time $O(T(|x|)\log T(|x|))$.

That is: there is a universal Turing machine that can simulate any Turing machine, and the time it spends is only slower than the simulated Turing machine by a factor logarithmic in its running time.

## Computability

### Uncomputable problems

For a decision problem, if there is a Turing machine that always halts within finitely many steps and decides correctly, then the problem is **Turing-computable**; otherwise the problem is **Turing-uncomputable**.

Since Turing machines can be encoded by natural numbers, the number of Turing machines is countably infinite, while the number of languages (i.e. sets of binary strings) is uncountably infinite, and each Turing machine decides at most one language; therefore Turing-uncomputable problems must exist.

### Halting problem

The halting problem is a classic Turing-uncomputable problem: given $\alpha$ and $x$, decide whether $M_{\alpha}$ halts within finitely many steps on input $x$.

??? note "Proof that the halting problem is Turing-uncomputable"
    Define the function $\mathsf{UC}:\{0,1\}^\ast\to\{0,1\}$ as:
    
    $$
    \mathsf{UC}(\alpha)=\begin{cases}0&M_\alpha(\alpha)=1\\1&\text{otherwise}\end{cases}
    $$
    
    We first prove that the function $\mathsf{UC}$ is Turing-uncomputable:
    
    Suppose there is a Turing machine $M_{\beta}$ that computes $\mathsf{UC}$. Then by the definition of $\mathsf{UC}$ we get $\mathsf{UC}(\beta)=1\iff M_\beta(\beta)\neq 1$, and from the fact that $M_{\beta}$ computes $\mathsf{UC}$ we get $M_{\beta}(\beta)=\mathsf{UC}(\beta)$, a contradiction; so the assumption does not hold, and there is no Turing machine that computes $\mathsf{UC}$.
    
    Let $M_{\mathsf{HALT}}$ be a Turing machine that solves the halting problem; the value of $M_{\mathsf{HALT}}(x,\alpha)$ is the answer to the decision problem of whether $M_\alpha$ halts within finitely many steps on input $x$. Then we can construct a Turing machine $M_{\mathsf{UC}}$ that computes the function $\mathsf{UC}$:
    
    $M_\mathsf{UC}$ first calls $M_\mathsf{HALT}(α,α)$; if it outputs $0$, then $M_\mathsf{UC}(α)=1$; otherwise, $M_\mathsf{UC}$ uses the universal Turing machine to simulate the computation and obtain the answer.
    
    Since the function $\mathsf{UC}$ is Turing-uncomputable, $M_\mathsf{HALT}$ does not exist, which means that the halting problem is Turing-uncomputable.

## Church–Turing thesis

The Church–Turing thesis states that if a class of problems can be solved by an effective method, then this class of problems can be solved by some Turing machine.

Here, an "effective method" must satisfy:

1.  it consists of finitely many clear instructions;
2.  when it is used to solve one of the problems in this class, the method must finish within finitely many steps and produce the correct answer.

This thesis has not been proven, but it is a fundamental axiom of the theory of computation.

## Complexity classes

There are many complexity classes; this article only introduces a small number of the more common ones.

### R and RE

For a language $L$ and a Turing machine $M$, if $M$ halts within finitely many steps on every input and $M(x)=1\iff x\in L$, we say that $M$ **decides** $L$.

For a language $L$ and a Turing machine $M$, if $M$ halts within finitely many steps on every input belonging to $L$ and $M(x)=1\iff x\in L$, we say that $M$ **recognizes** $L$.

The complexity class $\mathsf R$ is the set of languages that can be decided by some Turing machine, i.e. all Turing-computable languages.

The complexity class $\mathsf{RE}$ is the set of languages that can be recognized by some Turing machine. $\mathsf{RE}$ is also called the class of recursively enumerable languages.

From the definitions we get $\mathsf{R}\subseteq\mathsf{RE}$.

### DTIME

If there is a deterministic Turing machine that decides a language and, for any input $x$, halts within time $O(f(|x|))$, then this language belongs to the class $\mathsf{DTIME}(f(n))$.

### P

The complexity class $\mathsf P$ denotes the decision problems that can be solved by a deterministic Turing machine in polynomial time, i.e.:

$$
\mathsf{P}=\bigcup\limits_{k\in\mathbb{N}}\mathsf{DTIME}(n^k)
$$

Linear programming, computing the greatest common divisor, and the decision version of finding a maximum matching in a graph are all problems in the class $\mathsf P$.

### EXPTIME

The complexity class $\mathsf{EXPTIME}$ denotes the decision problems that can be solved by a deterministic Turing machine in exponential time, i.e.:

$$
\mathsf{EXPTIME}=\bigcup\limits_{k\in\mathbb{N}}\mathsf{DTIME}(2^{n^k})
$$

A weakened version of the halting problem — given the encoding of a Turing machine and a positive integer $k$, decide whether this Turing machine halts within $k$ steps — is a problem in the class $\mathsf{EXPTIME}$. This is because solving this problem takes $O(k)$ time, while the number $k$ can be encoded as a binary string of length $O(\log k)$.

### NTIME

If there is a non-deterministic Turing machine that decides a language and, for any input $x$, halts within time $O(f(|x|))$, then this language belongs to the class $\mathsf{NTIME}(f(n))$.

### NP

The complexity class $\mathsf{NP}$ denotes the decision problems that can be solved by a non-deterministic Turing machine in polynomial time, i.e.:

$$
\mathsf{NP}=\bigcup\limits_{k\in\mathbb{N}}\mathsf{NTIME}(n^k)
$$

All problems in the class $\mathsf P$ are problems in the class $\mathsf{NP}$. For more problems in the class $\mathsf{NP}$, see the NPC problems and NP-intermediate problems below.

#### NP-hard

If all problems in the class $\mathsf{NP}$ can be reduced to a problem $H$ in polynomial time, then the problem $H$ is NP-hard.

In other words, if the NP-hard problem $H$ could be solved in one unit of time, then all problems in the class $\mathsf{NP}$ could be solved in a polynomial number of units of time.

#### NP-complete

If a problem is both a problem in the class $\mathsf{NP}$ and NP-hard, then this problem is NP-complete, or in other words it is an NPC problem.

Some classic NPC problems: the decision version of the traveling salesman problem, the decision version of the maximum independent set problem, the decision version of the minimum vertex cover problem, the decision version of the longest path problem, the decision version of 0-1 integer programming, the set cover problem, the graph coloring problem, the knapsack problem, the 3-dimensional matching problem, and the decision version of the maximum cut problem.

The function versions of NPC problems are usually NP-hard; for example, "decide whether a graph contains a clique of size $k$" is both a problem in the class $\mathsf{NP}$ and NP-hard, so it is an NPC problem, while its function version "find a maximum clique of a graph" is not an NPC problem, but this function version is still NP-hard.

Similarly, other complexity classes also have "XX-complete" problems; for example, all problems in the class $\mathsf{EXPTIME}$ can be reduced in polynomial time to an EXPTIME-complete problem.

#### co-NP

A problem is in the class $\mathsf{co-NP}$ if and only if its complement is a problem in the class $\mathsf{NP}$. If we understand a "problem" as a "language", and a "language" as a subset of $\Sigma^\ast$, then the meaning of "complement" becomes clear.

For example: "given $n$ subsets, decide whether $k$ of them can be chosen to cover the whole set" is an NPC problem, while its complement "given $n$ subsets, decide whether no $k$ of them cover the whole set" is a problem in the class $\mathsf{co-NP}$. If the answer to the first problem is "yes", this amounts to finding a counterexample for the second problem, so the answer to the second problem is "no".

#### NP-intermediate

If a problem is in the class $\mathsf{NP}$ but is neither in the class $\mathsf{P}$ nor an NPC problem, it is called an NP-intermediate problem.

As far as is currently known, the graph isomorphism problem, the discrete logarithm problem, and the integer factorization problem may be NP-intermediate.

Ladner's theorem states that if $\mathsf{P}\ne\mathsf{NP}$, then there must exist problems that are NP-intermediate.

### NEXPTIME

The complexity class $\mathsf{NEXPTIME}$ denotes the decision problems that can be solved by a non-deterministic Turing machine in exponential time, i.e.:

$$
\mathsf{NEXPTIME}=\bigcup\limits_{k\in\mathbb{N}}\mathsf{NTIME}(2^{n^k})
$$

### #P

Problems in the class $\mathsf{\#P}$ are not decision problems, but counting problems related to problems in the class $\mathsf{NP}$: counting the number of solutions of a problem in the class $\mathsf{NP}$ is a problem in the class $\mathsf{\#P}$. In other words, counting in how many branches of a non-deterministic Turing machine that always halts in polynomial time a string is accepted is a problem in the class $\mathsf{\#P}$.

Counting the matchings or perfect matchings of a general graph or a bipartite graph is #P-complete; the corresponding decision problem is "decide whether a graph has a (perfect) matching".

### DSPACE

If there is a deterministic Turing machine that decides a language within space $O(f(|x|))$ on input $x$, then this language belongs to the class $\mathsf{DSPACE}(f(n))$.

-   $\mathsf{REG}=\mathsf{DSPACE}(O(1))$, i.e. the regular languages, that is, the languages that can be decided by automata.

-   $\mathsf{L}=\mathsf{DSPACE}(O(\log n))$; note that the space used by a Turing machine does not include the space occupied by the input.

-   $\mathsf{PSPACE}=\bigcup\limits_{k\in\mathbb N}\mathsf{DSPACE}(n^k)$

-   $\mathsf{EXPSPACE}=\bigcup\limits_{k\in\mathbb N}\mathsf{DSPACE}(2^{n^k})$

### NSPACE

If there is a non-deterministic Turing machine that decides a language within space $O(f(|x|))$ on input $x$, then this language belongs to the class $\mathsf{NSPACE}(f(n))$.

-   $\mathsf{REG}=\mathsf{DSPACE}(O(1))=\mathsf{NSPACE}(O(1))$

-   $\mathsf{NL}=\mathsf{NSPACE}(O(\log n))$

-   $\mathsf{CSL}=\mathsf{NSPACE}(O(n))$, i.e. the context-sensitive languages.

-   $\mathsf{PSPACE}=\mathsf{NPSPACE}=\bigcup\limits_{k\in\mathbb N}\mathsf{NSPACE}(n^k)$

-   $\mathsf{EXPSPACE}=\mathsf{NEXPSPACE}=\bigcup\limits_{k\in\mathbb N}\mathsf{NSPACE}(2^{n^k})$

## Polynomial time

Simply put, if there is a positive number $k$ such that the time complexity of an algorithm is $O(n^k)$ (note: not $\Theta(n^k)$), where $n$ is the problem size (the length of the input), then the algorithm is said to run in **polynomial time**. If a problem has a polynomial-time algorithm (on a deterministic Turing machine) that solves it, then this problem belongs to the complexity class $\mathsf{P}$.

Polynomial time can be divided into strongly polynomial time and weakly polynomial time; besides these, there is also pseudo-polynomial time.

### Strongly polynomial time

We first define a computational model called the arithmetic model. In the arithmetic model, arithmetic operations between numbers (addition, subtraction, multiplication, division, comparison) can be performed in unit time (i.e. in $O(1)$ time, independent of the size of the numbers).

If the number of operations of an algorithm in the arithmetic model is polynomial in the number of numbers in the input, and the space complexity is polynomial in the input size (rather than the number of numbers), then the algorithm runs in **strongly polynomial time**. Since arithmetic operations in the usual computational model can be performed in time polynomial in the input size (i.e. the logarithm of the size of the numbers), a strongly polynomial-time algorithm is necessarily a polynomial-time algorithm.

Generally speaking, the time complexity of a strongly polynomial-time algorithm is independent of the range of values.

### Weakly polynomial time

If an algorithm runs in polynomial time but not in strongly polynomial time, then it runs in **weakly polynomial time**.

For example, the Euclidean algorithm for computing the greatest common divisor, with time complexity $O(\log a + \log b)$ ($a$ and $b$ are the sizes of the input numbers), runs in weakly polynomial time.

### Pseudo-polynomial time

If the running time of an algorithm is polynomial in the range of values, it is said to run in **pseudo-polynomial time**. A pseudo-polynomial-time algorithm may or may not run in polynomial time; the reason it may not is that representing a positive integer of size $n$ generally needs only $O(\log n)$ binary digits, so an algorithm that is polynomial in the range of values is usually exponential in the length of the input. Although by definition pseudo-polynomial time may also be polynomial time, when we say that an algorithm runs in pseudo-polynomial time, we usually mean that it does not run in polynomial time.

For example, the knapsack problem is NP-hard, but it has a pseudo-polynomial-time solution based on dynamic programming.

If an NPC/NP-hard problem has a pseudo-polynomial-time solution, the problem is called **weakly NPC**/**weakly NP-hard**. If an NPC/NP-hard problem has no pseudo-polynomial-time solution under the assumption $\mathsf{P} \ne \mathsf{NP}$, the problem is called **strongly NPC**/**strongly NP-hard**.

## Constructible functions

### Time-constructible functions

Sometimes we want a Turing machine to know how much time it has used, for example, to force the Turing machine to halt after $T(n)$ steps of computation. But if computing $T(n)$ itself takes more than $T(n)$ time, this cannot be done. For this reason, time-constructible functions are defined to avoid such trouble.

If there is a Turing machine $M$ such that, on input $1^n$ ($n$ ones), $M$ halts within time $O(f(n))$ and outputs the binary representation of $f(n)$ (note that the output of the Turing machine here is not accept/reject but a string; the output can be written on the tape), then $f(n)$ is a **time-constructible function**.

Since reading the input takes $O(n)$ time, non-constant functions in $o(n)$ are not time-constructible.

### Space-constructible functions

Space-constructible functions can be defined similarly.

If there is a Turing machine $M$ such that, on input $1^n$ ($n$ ones), $M$ halts within space $O(f(n))$ and outputs the binary representation of $f(n)$, then $f(n)$ is a **space-constructible function**.

## Relations between complexity classes

### Time hierarchy theorems

#### Deterministic time hierarchy theorem

If $f(n)$ is a time-constructible function, then:

$$
\mathsf {DTIME}\left(o\left({\frac {f(n)}{\log f(n)}}\right)\right)\subsetneq \mathsf {DTIME}(f(n))
$$

From the deterministic time hierarchy theorem we get $\mathsf{P}\subsetneq\mathsf{EXPTIME}$.

??? note "Proof of the deterministic time hierarchy theorem"
    Define the language $L=\{(x, y)|\mathcal{U}((x, y), x)\text{ halts and rejects within }f(|x|+|y|)\text{ time}\}$. Since $f(n)$ is a time-constructible function, $L$ can be decided by computing according to the definition, in time $O(f(|x|+|y|))$, so $L\in\mathsf{DTIME}(f(n))$.
    
    Now suppose $L\in\mathsf{DTIME}(o\left({\dfrac {f(n)}{\log f(n)}}\right))$, and let $M_z$ be the Turing machine that decides $L$ in time $o\left({\dfrac {f(n)}{\log f(n)}}\right)$.
    
    Let the running time of the universal Turing machine $\mathcal{U}(x, z)$ with respect to $x$ be $g(|x|)$. From the introduction of the universal Turing machine above we get $g(n)=o(f(n))$, so when $y$ is large enough, $g(|z|+|y|)<f(|z|+|y|)$.
    
    Let $y'$ be a large enough $y$. Then $\mathcal{U}((z, y'), z)$ must halt within time $f(|z|+|y'|)$, hence $M_z(z, y')\ne M_z(z, y')$, a contradiction; so the assumption does not hold, and the deterministic time hierarchy theorem is proven.

#### Non-deterministic time hierarchy theorem

If $g(n)$ is a time-constructible function and $f(n+1)=o(g(n))$, then $\mathsf{NTIME}(f(n))\subsetneq\mathsf{NTIME}(g(n))$.

From the non-deterministic time hierarchy theorem we get $\mathsf{NP}\subsetneq\mathsf{NEXPTIME}$.

### Space hierarchy theorem

If $f(n)$ is a space-constructible function and $f(n)=\Omega(\log n)$, then $\mathsf{SPACE}(o(f(n)))\subsetneq\mathsf{SPACE}(f(n))$.

Here $\mathsf{SPACE}$ can stand for $\mathsf{DSPACE}$ or $\mathsf{NSPACE}$.

From the space hierarchy theorem we get $\mathsf{PSPACE}\subsetneq\mathsf{EXPSPACE}$.

### Savitch's theorem

A deterministic Turing machine can simulate a non-deterministic Turing machine within the square of the space consumed by the non-deterministic one (although the time consumed may be much larger), i.e.:

If $f(n)=\Omega(\log n)$, then:

$$
\mathsf{NSPACE}\left(f\left(n\right)\right)\subseteq \mathsf {DSPACE}\left(\left(f\left(n\right)\right)^2\right)
$$

Corollary: $\mathsf{PSPACE}=\mathsf{NPSPACE}$, $\mathsf{EXPSPACE}=\mathsf{NEXPSPACE}$.

### P?=NP

Whether the complexity classes $\mathsf{P}$ and $\mathsf{NP}$ are equal is a famous unsolved problem in computational complexity theory.

If $\mathsf{P}=\mathsf{NP}$, then $\mathsf{NP}=\mathsf{co-NP}$ follows, but not the other way around (currently there is no way to prove $\mathsf{P}=\mathsf{NP}$ from $\mathsf{NP}=\mathsf{co-NP}$).

???+ note "Why is NP?=co-NP not obvious?"
    Since a problem in $\mathsf{NP}$ and its corresponding problem in $\mathsf{co-NP}$ have opposite answers, it is easy to come up with this idea: for a problem in $\mathsf{co-NP}$, I just need to invert the output of the non-deterministic Turing machine that solves its complement, and the $\mathsf{co-NP}$ problem is solved, so $\mathsf{NP}=\mathsf{co-NP}$.
    
    In fact, the method described above does solve the $\mathsf{co-NP}$ problem, but it does not find a non-deterministic Turing machine that solves it: if what a Turing machine does is invert the output of a non-deterministic Turing machine, then this Turing machine is not a non-deterministic Turing machine. This is because a non-deterministic Turing machine accepts if it accepts in some branch and rejects if it rejects in all branches; inverting its output turns this into accepting in all branches and rejecting in one branch, which no longer fits the definition of a non-deterministic Turing machine. So the fact that this Turing machine can solve the $\mathsf{co-NP}$ problem does not make the $\mathsf{co-NP}$ problem a problem in $\mathsf{NP}$.

If $\mathsf{P}=\mathsf{NP}$, then $\mathsf{EXPTIME}=\mathsf{NEXPTIME}$ also follows.

If $\mathsf{P}\ne\mathsf{NP}$, then NP-intermediate is non-empty.

## References

1.  [计算复杂性（1）自动机与正则语言 (Computational complexity (1): automata and regular languages)](https://lingerois.com/p/%E8%AE%A1%E7%AE%97%E5%A4%8D%E6%9D%82%E6%80%A71-%E8%87%AA%E5%8A%A8%E6%9C%BA%E4%B8%8E%E6%AD%A3%E5%88%99%E8%AF%AD%E8%A8%80/);

2.  [计算复杂性（2）图灵机与可计算性 (Computational complexity (2): Turing machines and computability)](https://lingerois.com/p/%E8%AE%A1%E7%AE%97%E5%A4%8D%E6%9D%82%E6%80%A72-%E5%9B%BE%E7%81%B5%E6%9C%BA%E4%B8%8E%E5%8F%AF%E8%AE%A1%E7%AE%97%E6%80%A7/);

3.  the relevant entries on [Wikipedia](https://en.wikipedia.org/) and the references of those entries.
