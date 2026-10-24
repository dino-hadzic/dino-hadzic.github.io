---
title: Finite state machine
---

Prerequisites: [Languages and decision problems](./cc-basic.md#problems)

A **finite state machine** (FSM; below also simply called an automaton) is the simplest kind of computational model, which shows in the fact that both its descriptive power and its resources are extremely limited. Automata are widely used in competitive programming and in computer science, and their idea appears in many string algorithms, so it is recommended to learn automata before studying some string algorithms ([KMP](../string/kmp.md), [AC automaton](../string/ac-automaton.md), [SAM](../string/sam.md)).

## Introduction to automata

First, let us understand what automata are for: an automaton is a mathematical model that decides whether a sequence of signals satisfies some specific pattern or rule.

Some terms in this sentence deserve a closer explanation. A "sequence of signals" means a series of signals arranged in order, for example the characters of a string from first to last, the elements of an array from $1$ to $n$, the digits of a number from the highest to the lowest, and so on. "Deciding whether some rule is satisfied" can be understood as: we care whether this sequence belongs to some specific set. This set is defined by rules we fix in advance, for example "all binary strings of even length" or "all palindromes".

Sometimes we need to answer questions of this kind: does a given sequence have a certain property? For example, is a binary number odd, is a string a palindrome, is it a subsequence of another string, and so on. An automaton is exactly the mathematical tool for solving such problems.

An automaton works very much like a flowchart. Suppose you want to order a milk tea in a food delivery app; all your choices form a sequence. The following flowchart is an example:

![order fsm](./images/fsm1.svg)

For example, if your sequence of choices is "open the ordering screen -> choose milk tea -> have money for the milk tea", then the states you pass through in order may be "delivery app -> ordering screen -> pay for the milk tea -> milk tea bought". In this way our "milk tea automaton" decided, based on our choices, whether we bought a milk tea. We can also notice that there may be more than one way to reach a state. Likewise, if you did not buy a milk tea, you may have left the ordering screen directly, or had no money for it and therefore not bought it.

With this automaton we divided the sequences of signals into two classes: the sequences in which a milk tea was bought and the sequences in which it was not. Depending on the state we end up in, we have solved a decision problem.

Although we have just compared the way an automaton works to a flowchart, a flowchart itself is only an intuitive visualization tool and does not constitute a mathematical definition of an automaton. To describe the structure of an automaton more precisely, we need to abstract the elements of the flowchart. After the abstraction, we find that the structure of a flowchart can in fact be simplified to a directed graph in which every node represents a state and every directed edge represents a transition between states.

Therefore, the core structure of an automaton can formally be viewed as a directed graph, which we call the **state diagram**.

An automaton works similarly to a flowchart, with these differences: every node of an automaton is a decision node; a node of an automaton is merely a state rather than a task; an edge of an automaton can accept many kinds of characters (not limited to `T` or `F`).

For example, the automaton that performs the task "decide whether a binary number is even" is as follows:

![example fsm](./images/fsm2.svg)

Starting from the start node, accept the binary representation of the number from the highest digit to the lowest and look where we end up. If we end up in the node with the red circle, the number is even; otherwise it is not.

Here we need to stress that below we will often mention terms such as "character" and "alphabet (character set)"; this does not mean that automata can only be applied to strings. A character need not be a letter like $\tt abc\cdots z$; it can also be a choice.

If we need to decide the relation between a finite sequence of signals and another sequence of signals (for example, whether this finite sequence of signals is a substring of the other sequence of signals), the usual approach is to build an automaton for this finite sequence of signals. This will be covered when learning KMP.

Note that an automaton is only a **mathematical model**, and **not an algorithm**, nor a **data structure**. There are many ways to implement the same automaton, possibly with different time and space complexities.

Next you can choose to keep studying automata on this page, or go and learn concrete examples such as [KMP](../string/kmp.md), the [AC automaton](../string/ac-automaton.md) or the [SAM](../string/sam.md).

FSMs are divided into two classes: deterministic finite automata and nondeterministic finite automata.

## Deterministic finite automaton

A **deterministic finite automaton** (DFA) is characterized by the fact that its decision process is deterministic. Taking the "milk tea automaton" as an example: as soon as you open the ordering screen, you enter the ordering screen; unexpected situations such as the network crashing so that it does not open, or the phone running out of battery and going dark, do not happen.

???+ abstract "DFA"
    A DFA is a 5-tuple $(Q,\Sigma,\delta,q_0,F)$ consisting of:
    
    1.  A **finite set of states** $Q$. If we view a DFA as a directed graph, the states of the DFA correspond to the vertices of the graph.
    2.  An **alphabet** $\Sigma$. The automaton can only take these characters as input.
    3.  A **transition function** $\delta:Q\times \Sigma \to Q$, a function that takes two arguments and returns one value, where the first argument and the return value are states and the second argument is a character of the alphabet. If we view a DFA as a directed graph, the transition function of the DFA corresponds to the edges between vertices, and each edge carries one character.
    4.  A **start state** $q_0\in Q$, which is a special state. In different articles the start state is usually denoted by $s$, $\textit{start}$ or $q_0$; in this article we use $q_0$.
    5.  A **set of accepting states** $F\subseteq Q$, which is a set of special states.

A DFA can be represented simply by the following structure:

???+ example "Reference implementation"
    ```cpp
    --8<-- "docs/misc/code/fsm/dfa.hpp:dfa"
    ```

The process of finding the sequence of states of an input string $w$ in a DFA and deciding whether it is accepted is called a **computation**.

???+ abstract "Computation of a DFA"
    Let $M=(Q,\Sigma,\delta,q_0,F)$ be a DFA and $w=w_1w_2\cdots w_n\in\Sigma^*$ a string. If there exists a sequence of states $r_0,r_1,\cdots,r_n$ in $Q$ such that
    
    -   $r_0=q_0$,
    -   $\delta(r_i,w_{i+1})=r_{i+1}$ holds for every $i=0,1,\cdots,n-1$,
    -   $r_n\in F$,
    
    then we say that $M$ **accepts** $w$. Otherwise, we say that $M$ **does not accept** $w$.

When a DFA reads a string, it starts at the start state and makes transitions character by character according to the transition function. If, after reading all characters of the string, it is in an accepting state, we say that the DFA **accepts** the string; otherwise we say that the DFA **does not accept** the string.

???+ abstract "Formal language"
    A **formal language**, or simply **language**, over an alphabet $\Sigma$ is a set $L$ of strings over $\Sigma$.

???+ abstract "Language recognized by an automaton"
    For an automaton $M$, the language $L(M)$ it recognizes is defined as the set of all strings it accepts, $\{w\mid M\text{ accepts }w\}$.

Not every language can be recognized by a DFA.

???+ abstract "Regular language"
    If a language can be recognized by some DFA, it is called a **regular language**.

As mentioned above, an automaton can be represented by a state diagram. The following is a DFA that accepts the strings $\tt a$, $\tt ab$, $\tt aac$ and no others:

![](./images/fsm3.svg)

(The failure state is omitted in the figure; all transitions not drawn lead to that failure state.)

## Nondeterministic finite automaton

A **nondeterministic finite automaton**[^nfa-and-nfaepsilon] (NFA) is the natural generalization of a DFA. In an NFA, for any state and any character there may be zero, one or several successor states. In addition, the NFAs discussed in this section are allowed to accept the empty character, that is, they can move from a state to one of its successor states without consuming any character.

Take the "milk tea automaton" again as an example. After placing the order, even though you have money for the milk tea, you may fail to buy it because of a poor network connection: this is the existence of several successors. It is also possible that, because your hands were too slow, you fail to buy the milk tea because it is sold out even though the input string (the sequence of actions) is the same: this is the existence of the empty character, which may or may not be followed. A small modification of the previous automaton implements the behavior described above:

![order nfa](./images/fsm4.svg)

Obviously every DFA is an NFA, so NFAs can recognize at least all regular languages. But can an NFA, as an extension of a DFA, recognize more languages? In fact it cannot; we will discuss the equivalence of DFAs and NFAs later.

???+ abstract "NFA"
    Let $\mathcal{P}(Q)$ denote the power set of $Q$. Let $\varepsilon\notin\Sigma$ denote the empty string and write $\Sigma_\varepsilon = \Sigma\cup\{\varepsilon\}$. An NFA is a 5-tuple $(Q,\Sigma,\delta,q_0,F)$ consisting of:
    
    1.  A **finite set of states** $Q$,
    2.  An **alphabet** $\Sigma$,
    3.  A **transition function** $\delta:Q\times \Sigma_{\varepsilon} \to \mathcal{P}(Q)$, a function that takes two arguments and returns a **set of states**, where the first argument is a state, the second argument is a character of the alphabet or the empty string $\varepsilon$, and the return value is the set of all possible successor states (possibly empty),
    4.  A **start state** $q_0\in Q$,
    5.  A **set of accepting states** $F\subseteq Q$.

The computation of an NFA amounts to running several DFAs at the same time. Every step exhausts all possibilities, and in the end, as long as one branch reaches an accepting state, the NFA accepts the whole string.

???+ abstract "Computation of an NFA"
    Let $N=(Q,\Sigma,\delta,q_0,F)$ be an NFA. If a string $w$ can be written as some $y_1y_2\cdots y_m$ (where $y_i\in\Sigma_\varepsilon$) and there exists a sequence of states $r_0,r_1,\cdots,r_m$ in $Q$ such that
    
    -   $r_0=q_0$,
    -   $r_{i+1}\in\delta(r_i,y_{i+1})$ holds for every $i=0,1,\cdots,m-1$,
    -   $r_m\in F$,
    
    then we say that $N$ **accepts** $w$. Otherwise, we say that $N$ **does not accept** $w$.

Since empty characters are allowed, when writing the string $w$ as $y_1y_2\cdots y_m\in\Sigma^*_\varepsilon$ arbitrarily many empty characters may be inserted. For example, the string $\texttt{abc}$ can be written as $\texttt{a}\varepsilon\texttt{bc}\varepsilon\varepsilon\in\Sigma^*_\varepsilon$. Compared with a DFA, where every input corresponds to exactly one outcome, every input of an NFA may correspond to several outcomes, forming a set of outcomes.

## Equivalence of DFA and NFA

We call two automata equivalent if and only if they recognize the same language. DFAs and NFAs are equivalent, that is, every NFA is equivalent to some DFA; therefore the class of languages recognized by NFAs is also the class of all regular languages. Every DFA can directly be viewed as an NFA; conversely, an NFA can be converted into a DFA by the **powerset construction**.

???+ abstract "Powerset construction"
    Let the NFA be $N = (Q, \Sigma, \delta, q_0, F)$. Define $E(q)$ as the set of states reachable from state $q$ using only $\varepsilon$-transitions (including $q$ itself), that is, the $\varepsilon$-closure of $q$.
    
    Construct the DFA $M = (Q', \Sigma, \delta', E(q_0), F')$, where:
    
    -   the **finite set of states** is $Q' = \mathcal{P}(Q)$,
    -   the **transition function** $\delta' : Q' \times \Sigma \to Q'$ satisfies $\delta'(S, c) = \bigcup_{q \in S,~q' \in \delta(q, c)} E(q')$,
    -   the **set of accepting states** is $F' = \{ S \subseteq Q \mid S \cap F \neq \varnothing \}$.
    
    Obviously, at every step of the computation the state of $M$ corresponds to the set of states $N$ may be in.

Although NFAs and DFAs have the same power to recognize languages, NFAs are still useful. This is because for some regular languages the number of states needed by an NFA is far smaller than the number needed by a DFA. For example, one can construct an NFA with $n$ states whose corresponding minimal DFA has $\Theta(2^n)$ states. In that case running the NFA directly has a better time complexity.

## Time complexity of running a DFA and an NFA

Let the length of the given string be $n$, the number of states of the automaton $s$, and the size of the alphabet a constant. Then obviously the time complexity of running a DFA is $O(n)$: it suffices to simulate the process described above.

Running an NFA naively has time complexity $O(ns^2)$, because every successor has to be considered, together with the cost of merging states. Of course, using a bitset or the Method of Four Russians the complexity of the computation can be improved to $O\left(\dfrac{ns^2}{w}\right)$ or $O\left(\dfrac{ns^2}{w\cdot \log n}\right)$.

## Regular expressions and regular languages

This section discusses the definition and properties of regular expressions and regular languages, and studies the relation between regular expressions and FSMs.

### Regular expressions

A **regular expression** is another common way to describe regular languages. Although we see this name in many modern programming languages (for example Python), what these languages implement is in fact a superset of regular expressions.

???+ abstract "Regular expression"
    Given an alphabet $\Sigma$, a regular expression is a string of symbols defined inductively by the following rules:
    
    1.  any character $c \in \Sigma$ is a regular expression;
    2.  the empty string symbol $\varepsilon$ is a regular expression;
    3.  the empty language symbol $\varnothing$ is a regular expression;
    4.  if $R_1$ and $R_2$ are regular expressions, then $(R_1 + R_2)$, $(R_1 R_2)$ (also written $(R_1 \cdot R_2)$) and $(R_1^\ast)$ are regular expressions.

The purpose of a regular expression is to describe a language with these symbols. Every regular expression has a corresponding formal language.

???+ abstract "Language represented by a regular expression"
    Let $L(R)$ be the formal language corresponding to the regular expression $R$. Then:
    
    1.  if $R = c$, where $c \in \Sigma$, then $L(R) = \{c\}$;
    2.  if $R = \varepsilon$, then $L(R) = \{\varepsilon\}$;
    3.  if $R = \varnothing$, then $L(R) = \varnothing$;
    4.  if $R = (R_1 + R_2)$, then $L(R) = L(R_1) \cup L(R_2)$;
    5.  if $R = (R_1 R_2) = (R_1\cdot R_2)$, then $L(R) = \{ uv \mid u \in L(R_1),~ v \in L(R_2) \}$, where $uv$ denotes the concatenation of the two strings one after the other;
    6.  if $R = (R_1^\ast)$, then $L(R) = \{u_1 u_2 \cdots u_n \mid u_i \in L(R_1),\ n \in \mathbf{N}_+\}\cup\{\varepsilon\}$, which is also called the **Kleene star** or the **Kleene closure**, or closure for short.

Of course, once the precedence of the operations is fixed, these parentheses may be omitted when no confusion arises.

???+ example "Example"
    Let $L(R_1) = \{0,\ 01\}$ and $L(R_2) = \{\varepsilon,\ 1,\ 11,\ 111,\ \dots\}$. Then:
    
    -   $L(R_1R_2) = \{0,\ 01,\ 011,\ 0111,\ \dots\}$,
    -   $L(R_2^\ast) = L(R_2)$,
    -   $L(R_1 + R_2) = \{0,\ 01,\ \varepsilon,\ 1,\ 11,\ 111,\ \dots\}$.

Every regular expression can be converted into an NFA by [Thompson's construction](https://en.wikipedia.org/wiki/Thompson%27s_construction), and every DFA can be converted into a regular expression by the state elimination method[^state-elimination-method]. Therefore regular expressions and FSMs are equivalent.

### Regular languages

In this subsection we do not consider concrete regular expressions, but regular expressions with variables as parameters (a variable can be any regular language). Applying the algebraic laws of regular expressions helps to simplify regular expressions.

???+ note "Algebraic properties of regular languages"
    1.  Commutativity of union: $L + M = M + L$
    2.  Associativity of union: $(L + M) + N = L + (M + N)$
    3.  Associativity of concatenation: $(LM)N = L(MN)$
    4.  $\varnothing$ is the identity of union: $\varnothing + L = L + \varnothing = L$
    5.  $\varepsilon$ is the identity of concatenation: $\varepsilon L = L \varepsilon = L$
    6.  $\varnothing$ is the annihilator of concatenation: $\varnothing L = L \varnothing = \varnothing$
    7.  Distributivity: $L(M + N) = LM + LN$, $(M + N)L = ML + NL$
    8.  Idempotence of union: $L + L = L$
    9.  Laws about closure: $(L^\ast)^\ast = L^\ast$, $\varnothing^\ast = \varepsilon$, $\varepsilon^\ast = \varepsilon$

The **closure properties** of regular languages are also important. These properties allow us to start from some simple automata and, through certain operations, construct finite state machines (FSMs) that recognize other languages. In short, closure can be used as a tool for building complex FSMs.

About the closure properties of regular languages we have:

???+ note "Closure properties of regular languages"
    Let $L,M$ be two regular languages over the alphabet $\Sigma$, and let $h:\Sigma\to\Sigma^*$ be a map. Define the homomorphism of a string $s=s_1s_2\cdots s_n$ as $h(s)=h(s_1)h(s_2)\cdots h(s_n)$. Then,
    
    1.  the union $L + M$ of two regular languages is regular,
    2.  the concatenation $LM$ of two regular languages is regular,
    3.  the closure $L^*$ of a regular language is regular,
    4.  the complement $\Sigma^*\setminus L$ of a regular language is regular,
    5.  the intersection $L\cap M$ of two regular languages is regular,
    6.  the difference $L\setminus M$ of two regular languages is regular,
    7.  the reversal $L^R=\{s_n\cdots s_2s_1 \mid s=s_1s_2\cdots s_n\in L\}$ of a regular language is regular,
    8.  the homomorphic image $h(L)=\{h(s)\mid s\in L\}$ of a regular language is regular,
    9.  the inverse homomorphic image $h^{-1}(L) = \{ s \in \Sigma^\ast \mid h(s) \in L \}$ of a regular language is regular.

A simple corollary is that all finite languages are regular languages. In fact, the [trie](../string/trie.md) is exactly an automaton recognizing them.

## Myhill–Nerode theorem

The Myhill–Nerode theorem gives a criterion for deciding whether a language is regular. The theorem describes the structural characteristics of regular languages through the concept of equivalence classes.

???+ abstract "Nerode equivalence relation"
    For a language $L$ and any strings $x,y\in \Sigma^\ast$, if for every $z\in\Sigma^*$ we have $xz\in L\iff yz\in L$, then the strings $x$ and $y$ are called equivalent with respect to $L$, written $x\equiv_L y$.

That is, if for two strings $x$ and $y$, appending the same arbitrary string $z$ (including the empty string) to $x$ and to $y$ always yields strings that either both belong to $L$ or both do not belong to $L$, then we say that $x$ and $y$ are equivalent with respect to $L$.

According to the definition above, we partition the set of all finite strings into one or more equivalence classes. If and only if the number of these equivalence classes is finite, these equivalence classes can be used to construct a DFA recognizing the language. The number of states of this DFA equals the number of equivalence classes. Moreover, this number of states is the smallest among all DFAs that can recognize the language. This is the Myhill–Nerode theorem.

???+ note "Myhill–Nerode theorem"
    A language $L$ is regular if and only if the number of equivalence classes into which the equivalence relation $\equiv_L$ partitions $\Sigma^\ast$ is finite.
    
    For any DFA recognizing the language $L$, any two strings $x$ and $y$ that drive it to the same state must be in the same equivalence class.
    
    Furthermore, the number of equivalence classes is the number of states of the minimal DFA recognizing $L$. Every equivalence class corresponds to exactly one state of the minimal DFA. This minimal DFA is unique up to isomorphism.

This theorem provides a way to construct a DFA using the equivalence relation:

-   The set of states consists of all equivalence classes obtained from the partition by the equivalence relation. In each equivalence class pick an arbitrary representative string (for example some string of minimum length).
-   To construct the transition function, it suffices to append the character of the transition to the chosen representative string and find the state corresponding to the equivalence class of the resulting string; this is the successor state of the corresponding transition. Since all strings in the same equivalence class are equivalent, the arbitrarily chosen representative does not affect the result of the transition.
-   The start state is the equivalence class corresponding to the empty string $\varepsilon$.
-   The set of accepting states is the set of equivalence classes whose representative string belongs to the given language.

As a classic example, the [suffix automaton](../string/sam.md) is exactly the minimal DFA constructed using the Myhill–Nerode theorem.

The Myhill–Nerode theorem is usually applied to construct the DFAs corresponding to some infinite regular languages. Very often the conditions of the problem are fairly simple, and it suffices to examine the set of strings of not too large length to construct an automaton recognizing the whole language.

### Example problem

This section uses one example problem to show how the Myhill–Nerode theorem is applied in practice.

???+ example "[P12294 \[THUPC 2025 决赛\] 一个 01 串，n 次三目运算符，最后值为 1（加强版）](https://www.luogu.com.cn/problem/P12294) (P12294, THUPC 2025 Final: A 01 string, n ternary operators, final value 1, hard version)"
    The truth table $s_0s_1\cdots s_7$ of a ternary operation on $a,b,c$ ($s$ consists only of $0$ and $1$) means: if the bit of $s$ at position $a+2b+4c$ is $1$, the result is $1$, otherwise it is $0$.
    
    Given the table $s$ and $q$ strings of $0$ and $1$ of length $2n+1$, you need to answer for each string separately:
    
    whether it is possible to perform $n$ operations, each replacing three consecutive digits by the corresponding value of the operation, so that the result of the computation is $1$; give a construction, or determine that there is no solution.
    
    $1\le 2n+1\le 10^5,~\sum(2n+1)\le 3\times 10^5$.

??? note "Solution"
    The set of $01$ strings from which $1$ can be obtained is a regular language (that is, there exists a DFA that decides whether a $01$ string can produce $1$)[^prove-regular-language]. So consider using the Myhill–Nerode theorem. Because the conditions are fairly simple, experiments show that it suffices to partition the $01$ strings of length $\le 9$ into equivalence classes; when deciding whether two strings are equivalent, it suffices to enumerate suffixes of length $\le 6$ to append. If for two strings, after appending any suffix of length $\le 6$, either both can produce the string we want or neither can, the two strings are equivalent.
    
    Every transition amounts to appending a new character $0$ or $1$ to the current string and then replacing the new string by the shortest string in its equivalence class. Build an automaton according to these transitions. This automaton can decide in $O(n)$ whether a string of length $n$ admits a way of evaluation whose result is $1$. At the same time the number of states of the automaton is very small.
    
    For convenience, we build $6$ automata, which respectively tell whether there is a way of evaluation whose result is $0,1,00,01,10,11$. Over all possible operation tables, the maximum number of states of the automaton is $47$.
    
    Using the automata, after suitable preprocessing, static range queries (does the range admit a way of evaluation whose result is $1$) can be implemented with a sparse table or a cat tree: the former answers one query in $O(\log n)$, the latter in $O(1)$.
    
    Consider divide and conquer for the construction problem. Let $f(l,r,t)$ denote a way of merging the range $[l,r]$ into $t\in\{0,1,00,01,10,11\}$. Here we use heuristic splitting: maintain two pointers $i,j$, one scanning from left to right and the other from right to left, to enumerate the split point $\textit{mid}$ as $i$ or $j$. For $t\in\{0,1\}$, enumerate how $t$ is split into a left part and a right part, where $t$ has length $2$ in one part and length $1$ in the other. (For example, for the median table $s=00010111$, $1$ can be split into $01$ and $1$.) For $t\in\{00,01,10,11\}$, $t$ is split directly into a left part and a right part.
    
    If the resulting left and right parts are $t_1$ and $t_2$, we further check whether $[l,\textit{mid}]$ can produce $t_1$ and whether $[\textit{mid}+1,r]$ can produce $t_2$; if so, we directly recurse. If the $O(1)$ cat tree is used for the check, the complexity of the construction by heuristic splitting is $O(n\log n)$; otherwise, using the sparse table for the check, the complexity of the construction is $O(n\log^2n)$.
    
    With a cat tree, the total complexity is $O(n|Q|\log n+n\log n)$, where $|Q|\le 47$. For convenience, the reference code uses a sparse table and reduces the constant factor by using blocks at the bottom level; the corresponding total complexity is $O(n|Q|\log n+n\log^2 n)$.

??? note "Reference code"
    ```cpp
    --8<-- "docs/misc/code/fsm/fsm_1.cpp:main"
    ```

### Exercises

-   [Median Replace Hard](https://qoj.ac/problem/12010)
-   [JOISC 2024 卡牌收集 (Card Collection)](https://www.luogu.com.cn/problem/P10436) (by building an automaton with the Myhill–Nerode theorem, this problem can be extended to multiple range queries)

## DFA minimization

As mentioned above, two DFAs are equivalent if and only if they recognize the same regular language. According to the language recognized, all DFAs are partitioned into infinitely many equivalence classes. When running algorithms such as DP of DP, the $|Q|$ of the constructed DFA may be too large, making the complexity of the transitions of the outer DP too high. Therefore, we often need to find the minimal DFA in the equivalence class the DFA belongs to, in order to reduce the complexity of the transitions of the outer DP.

The Myhill–Nerode theorem of the previous section provides one construction method. However, for some more complex problems, constructing directly via the Myhill–Nerode theorem requires traversing a set of fairly long strings, which takes a lot of time. Therefore, we need a method that starts from an already constructed DFA (which is usually easy) and directly constructs a minimal DFA. This is called the **DFA minimization** problem.

The algorithm commonly used for DFA minimization is **Hopcroft's algorithm**. The Myhill–Nerode theorem states that for any DFA recognizing some language, the strings that drive it to the same state must be Nerode equivalent. All Nerode equivalent strings correspond to the same state of the minimal DFA, so a state of the minimal DFA must be a set of several states of the current DFA (here we assume that all states of the current DFA are reachable from $q_0$; otherwise the unreachable states must be removed first). We can start from the set of states of the existing DFA and partition them into several equivalence classes without examining concrete strings. Hopcroft's algorithm starts from the coarsest partition $\{F,Q\setminus F\}$ and refines this partition using a sequence of witnesses $A$ until no further refinement is possible. This is the core idea of Hopcroft's algorithm.

A **witness** $A$ is a set of states such that it and its complement $Q\setminus A$ certainly correspond to different Nerode equivalence classes. That is, for any $u\in A$ and $v\in Q\setminus A$ there exists some string $s\in\Sigma^*$ such that, after reading the string $s$ starting from $u$ and from $v$ respectively, exactly one of them is in an accepting state. Therefore, if two states $u,v\in Q$ are such that under some character $c$ exactly one of them moves into the witness $A$ and the other moves outside the witness $A$, that is, exactly one of $\delta(u,c)\in A$ and $\delta(v,c)\in A$ holds, then $u,v$ are likewise not equivalent: after reading the string $cs$ starting from $u$ and from $v$ respectively, exactly one of them is in an accepting state. Therefore, the partition can be refined using whether $\delta(u,c)\in A$ holds. Concretely, let

$$
S_x = \{u\mid u\in P_x,~\delta(u,c)\in A\}.
$$

If neither $S_x$ nor $P_x\setminus S_x$ is empty, then the set of states $P_x$ in the current partition can be refined into $S_x$ and $P_x\setminus S_x$.

At the very beginning, put the set of accepting states $F$ into the witness set $W$ as a witness, that is, $W\gets\{F\}$, and maintain the current partition as $P\gets\{F,~Q\setminus F\}$. The initial witness is obviously valid: states in $F$ and in $Q\setminus F$ can never be equivalent. Each time, take an arbitrary set $A$ out of the witness set $W$ and use it to refine the current partition. Enumerate all characters $c\in\Sigma$. For every set of states $P_x$ in the current partition $P$, compute the $S_x$ described above. If $S_x\neq\varnothing$ and $|S_x|\neq|P_x|$, it means that $P_x$ can be further split into the two sets $S_x$ and $P_x\setminus S_x$; directly replace $P_x$ in $P$ by them.

Whenever a finer partition is obtained, new witnesses are obtained as well. In principle, both newly obtained $S_x$ and $P_x\setminus S_x$ could be put into the witness set $W$ to wait for further verification. However, this is not necessary. It is easy to understand that for the three witnesses $P_x,S_x,P_x\setminus S_x$ it suffices to verify any two of them to guarantee the correctness of the result: there are only three outcomes, $\delta(u,c)\in S_x$, $\delta(u,c)\in P_x\setminus S_x$ and $\delta(u,c)\notin P_x$, and splitting a set into three parts needs only two tests. Therefore, when splitting $P_x$ into $S_x$ and $P_x\setminus S_x$: if $P_x$ is still in the witness set $W$, this means the witness $P_x$ has not been verified yet, and we need to replace $P_x$ in the witness set $W$ by the two sets $S_x$ and $P_x\setminus S_x$; otherwise, the current partition is certainly equivalent to[^smaller-evidence] the result of having verified $P_x$, so it suffices to put the smaller of $S_x$ and $P_x\setminus S_x$ into the witness set $W$. Similar to heuristic splitting, this yields a good complexity.

Written as pseudocode, the process above is:

$$
\begin{array}{l}
\textbf{Algorithm } \text{Hopcroft's Algorithm}(Q, \Sigma, \delta, q_0, F): \\
\textbf{Input. } \text{DFA } M=(Q, \Sigma, \delta, q_0, F). \\
\textbf{Output. } \text{A partition of } Q \text{ into equivalence classes of the minimal DFA.} \\
\textbf{Method. } \\
\begin{array}{ll}
1 & P \gets \{F,\; Q \setminus F\} \\
2 & W \gets \{F\} \\
3 & \textbf{while } W \ne \varnothing \\
4 & \quad \text{choose and remove any } A \in W \\
5 & \quad \textbf{for each } c \in \Sigma \\
6 & \quad \quad S \gets \{ q \in Q \mid \delta(q,c) \in A \} \\
7 & \quad \quad \textbf{for each } Y \in P \text{ such that } S \cap Y \ne \varnothing \text{ and } Y \setminus S \ne \varnothing \\
8 & \quad \quad \quad Y_1 \gets S \cap Y,~Y_2 \gets Y \setminus S \\
9 & \quad \quad \quad P \gets (P \setminus \{Y\}) \cup \{Y_1, Y_2\} \\
10 & \quad \quad \quad \textbf{if } Y \in W \\
11 & \quad \quad \quad \quad W \gets (W \setminus \{Y\}) \cup \{Y_1, Y_2\} \\
12 & \quad \quad \quad \textbf{else} \\
13 & \quad \quad \quad \quad \text{add the smaller of } Y_1 \text{ and } Y_2 \text{ to } W \\
14 & \textbf{return } P
\end{array}
\end{array}
$$

When implementing the algorithm, the bottleneck of the complexity is the computation of $S$. Directly traversing all $q\in Q$ and checking whether $\delta(q,c)\in A$ holds is not feasible. Therefore, before the algorithm runs, we need to precompute the reverse transitions $\{q\in Q\mid \delta(q,c)=a\}$, so that, using these reverse transitions and traversing $a\in A$, the set $S$ is obtained. This guarantees that every transition $\delta(q,c)=a$ is traversed only when $a$ belongs to some witness; and the way of selecting witnesses described above guarantees that in the sequence of witnesses $A_1\supset A_2\supset\cdots\supset A_k$ containing $a$ that are actually used in the algorithm, each one is at least twice as large as the next, so $k\in O(\log |Q|)$. In other words, every transition is traversed at most $O(\log |Q|)$ times, and the total number of transitions is $|Q||\Sigma|$, so the total complexity is $O(|Q||\Sigma|\log |Q|)$.

The reference implementation is as follows:[^detail]

??? example "Reference implementation"
    ```cpp
    --8<-- "docs/misc/code/fsm/dfa.hpp:hopcroft"
    ```

This reference implementation allows the states of the automaton to carry labels with arbitrary integer values rather than the simple binary labels "accepting" and "non-accepting". From the reference implementation one can see that the only difference from the basic Hopcroft's algorithm lies in the construction of the initial partition and the witness set. Such an extended automaton is also called a [Moore machine](https://en.wikipedia.org/wiki/Moore_machine). One of its applications can be seen in the second example problem of this section.

### Example problems

This section uses two example problems to show how the technique of DFA minimization is applied in practice.

???+ example "Example problem"
    Given a string $a$ of length $n$ over $01?$, with the initial variable $x = 0$, we traverse every character $a_i$ in order and perform the following operations:
    
    1.  if $a_i = 0$, let $x \gets x - \text{lowbit}(x)$;
    2.  if $a_i = 1$, let $x \gets x + \text{lowbit}(2^k - 1 - x)$;
    3.  if $a_i = ?$, choose $0$ or $1$ freely and perform the corresponding one of the two operations above.
    
    If in the end $x \in [0, r]$, the sequence of operations is called good.
    
    Now, for every $i = 1 \ldots n$, find how many "good" complete sequences there are under the constraint $a_i = 0$. In particular, when $a_i = 1$ the answer is $0$.
    
    $1\le n\le 10^5,~1\le k\le 20,~0\le r<2^k$. Output the answer modulo $998244353$.

??? note "Solution"
    Consider a naive DP. Let $f_{i,j}$ denote the number of ways to start from $x=0$, perform the operations on $[1,i]$ and have the current number equal to $j$. Let $g_{i,j}$ denote the number of ways to start from $x=j$, perform the operations on $[i,n]$ and end with $x \in [0, r]$. The answer under the constraint $a_i=0$ is then $\sum_j f_{i-1,j}g_{i+1,j - \text{lowbit}(j)}$. The complexity is $O(n2^k)$.
    
    Consider directly building the transitions of $j$ into a DFA, then running DFA minimization, and then doing the DP.

??? note "Reference code"
    ```cpp
    --8<-- "docs/misc/code/fsm/fsm_2.cpp:main"
    ```

???+ example "[Minimal Subset Difference](https://codeforces.com/contest/956/problem/F)"
    Define $f(n)$ as the minimum absolute value that can be obtained by inserting plus or minus signs between all digits of the decimal number $n$.
    
    There are $T$ queries. Each query gives $l, r, k$; find the number of $m$ such that $l \le m \le r$ and $f(m) \le k$.
    
    $1 \le T \le 5\times 10^4$, $1 \le l \le r \le 10^{18}$, $0 \le k \le 9$.

??? note "Solution"
    First we give a greedy way to compute $f(n)$. Consider the number from the highest digit to the lowest; initially, let the obtained sum be $0$. When we reach some digit, if the number obtained so far is less than or equal to $0$ we add the current digit, otherwise we subtract it. Handled this way, the absolute value of the greedily computed result is certainly at most $9$. Therefore the absolute value of the true $f(n)$ is certainly at most $9$.
    
    Let us think further: to obtain the final answer, how large can the numbers obtained in the intermediate steps be? Since the answer is certainly at most $9$, there are at most $19$ digits, and each step adds or subtracts at most $9$, the number obtained during the process is certainly at most $90$, otherwise it cannot come back down at the end. In fact, this upper bound can be lowered further[^upper-bound].
    
    Consider a naive DP of DP. First, think about how the inner DP decides the answer of a number: define $g_{i,c}$ as whether this number, based only on its first $i$ digits, can produce $c$. By the above, only values $c$ at most $90$ need to be kept. If the current digit is $v$, we have the transition:
    
    $$
    g_{i+1,c+v}\gets g_{i+1,c+v}\lor g_{i,c},~
    g_{i+1,|c-v|}\gets g_{i+1,|c-v|}\lor g_{i,c}.
    $$
    
    The outer DP is a digit DP. Split the query into a difference. Let the state be $f_{\textit{len},\textit{lim},\textit{sta}}$, whose indices respectively mean that we have considered up to the $\textit{len}$-th digit, whether there is an upper bound restriction, and that the automaton is currently in state $\textit{sta}$.
    
    Unlike an ordinary DFA, we need to record the corresponding answer for every state of the automaton. Running a brute-force search once, we find that the inner DP has only $19564$ states. Then we directly run DFA minimization, which reduces the number of states to $715$.
    
    Now we precompute all the digit DP answers with $\textit{lim}=0$; then with multiple test cases we only need to run the case $\textit{lim}=1$ and the answer is obtained very quickly.
    
    The time complexity is $O(|S||\Sigma|\log |S|+(|Q||\Sigma|+T)|\Sigma|\log_{10} V)$ ($|S|=19564$, $|Q|=715$).

??? note "Reference code"
    ```cpp
    --8<-- "docs/misc/code/fsm/fsm_3.cpp:main"
    ```

### Exercises

-   [Language Recognition](http://poj.org/problem?id=3576)
-   [Equanimous](https://qoj.ac/problem/7083)

## Common applications of automata

This section lists some common applications of automata in competitive programming[^is-dfa].

### Trie

The [trie](../string/trie.md) is the first automaton most competitive programmers encounter; it accepts exactly the elements of a given set of strings. The transition function consists of the edges of the trie, and the accepting states are the states reached when each string is inserted into the trie.

### KMP automaton

The [KMP algorithm](../string/kmp.md) can be viewed as an automaton: the KMP automaton based on a string $s$ accepts exactly the strings that have $s$ as a suffix, and its accepting state is $|s|$.

The transition function is as follows, where the indices of $s$ start from $1$ and $\pi(i)$ denotes the length of the longest common proper prefix and suffix of the prefix $s[1..i]$ (that is, $\pi[i-1]$ in the [prefix function](../string/kmp.md)):

$$
\delta(i, c)=
\begin{cases}
i+1&i<|s|\land s[i+1]=c\\
0&s[1]\ne c\land i=0\\
\delta(\pi(i),c)&(i=|s|\lor s[i+1]\ne c)\land i>0
\end{cases}
$$

### AC automaton

The [AC automaton](../string/ac-automaton.md) accepts exactly the strings that have some element of a given set of strings as a suffix. That is, trie + KMP.

### Suffix automaton

The [suffix automaton](../string/sam.md) accepts exactly the suffixes of a given string.

### Generalized suffix automaton

The [generalized suffix automaton](../string/general-sam.md) accepts exactly the suffixes of some element of a given set of strings. That is, trie + SAM.

The relation between the generalized SAM and the SAM is the same as the relation between the AC automaton and the KMP automaton.

### Palindromic automaton

The [palindromic automaton](../string/pam.md) is special in that it cannot be conveniently defined as an automaton.

If we do need to define it, it accepts exactly the **center and right half** of every palindromic substring of some string.

For odd palindromes, "center and right half" means literally that; for even palindromes it is defined as a special character followed by the right half. This definition looks strange, but it is what makes the PAM a real automaton rather than merely two trees.

### Subsequence automaton

The [subsequence automaton](../string/seq-automaton.md) accepts exactly the subsequences of a given string.

### DP of DP

[DP of DP](../dp/dp-of-dp.md) is an application of automata; it can be seen as the technique of first building an automaton through an inner DP, and then performing counting or optimization tasks through an outer DP on the automaton.

## Suffix links

Since automata are inseparably related to matching, and a basic idea of matching is "if this string does not work, try whether its suffix does", many automata (KMP, AC automaton, SAM, PAM) have the concept of a suffix link.

A state corresponds to several strings. Its suffix link points to the state of the automaton corresponding to the longest common proper suffix of the strings corresponding to that state. In general, the suffix links form a tree, and the suffix link trees of different automata share some properties, which is worth paying attention to when learning them.

## Further reading

-   [计算复杂性（1）Warming Up: 自动机模型 (Computational Complexity (1), Warming Up: automaton models)](https://lingeros-tot.github.io/2019/03/05/Warming-Up-自动机模型/)
-   [国家集训队 2021 论文 徐哲安 浅谈有限状态自动机及其应用 (Chinese National Team 2021 paper collection, Xu Zhe'an: A brief discussion of finite state automata and their applications)](https://github.com/OIerTFX/IOI/blob/master/%E5%9B%BD%E5%AE%B6%E9%9B%86%E8%AE%AD%E9%98%9F2021%E8%AE%BA%E6%96%87%E9%9B%86/pdf-files/%E5%BE%90%E5%93%B2%E5%AE%89%20%E6%B5%85%E8%B0%88%E6%9C%89%E9%99%90%E7%8A%B6%E6%80%81%E8%87%AA%E5%8A%A8%E6%9C%BA%E5%8F%8A%E5%85%B6%E5%BA%94%E7%94%A8.pdf)
-   [Myhill–Nerode theorem - Wikipedia](https://en.wikipedia.org/wiki/Myhill%E2%80%93Nerode_theorem)
-   Knuutila, Timo. "Re-describing an algorithm by Hopcroft." Theoretical Computer Science 250, no. 1-2 (2001): 333-363.
-   Hopcroft, John E., Rajeev Motwani, and Jeffrey D. Ullman. "Introduction to automata theory, languages, and computation." 2nd ed. Addison-Wesley, 2001.

[^nfa-and-nfaepsilon]: In this definition we allow transitions between states on the empty character ($\varepsilon$), so more precisely this is a nondeterministic finite automaton with $\varepsilon$-transitions (NFA-$\varepsilon$). Some textbooks simply call it an NFA; for brevity this article follows that usage. In theory NFA and NFA-$\varepsilon$ are distinguished, but in fact their computational power is the same.

[^state-elimination-method]: See Section 3.2 of [国家集训队 2021 论文 徐哲安 浅谈有限状态自动机及其应用 (Chinese National Team 2021 paper collection, Xu Zhe'an: A brief discussion of finite state automata and their applications)](https://github.com/OIerTFX/IOI/blob/master/%E5%9B%BD%E5%AE%B6%E9%9B%86%E8%AE%AD%E9%98%9F2021%E8%AE%BA%E6%96%87%E9%9B%86/pdf-files/%E5%BE%90%E5%93%B2%E5%AE%89%20%E6%B5%85%E8%B0%88%E6%9C%89%E9%99%90%E7%8A%B6%E6%80%81%E8%87%AA%E5%8A%A8%E6%9C%BA%E5%8F%8A%E5%85%B6%E5%BA%94%E7%94%A8.pdf).

[^prove-regular-language]: See the [official editorial](https://qoj.ac/download.php?type=attachments&id=2079&r=1).

[^smaller-evidence]: "Equivalent to" here means that although $P_x$ may not actually have been verified, verifying the current partition with $P_x$ would not bring any improvement. Simply put, in the tree of witness sets produced by splitting sets, some ancestor of it and all side branches along the path have already been verified, so it can be shown inductively that this is equivalent to it having been verified as well.

[^detail]: There is one detail in the implementation of the algorithm: for a witness $A$, it is possible that after verifying some of the characters, this witness set has already been split into $B$ and $C$. Without loss of generality let $|B|\ge |C|$. In the reference implementation, the smaller set $C$ is inserted at the end of the witness queue, while the larger witness set $B$ replaces $A$ at its original position. When the algorithm continues, the remaining characters are in fact verified only using the witness $B$. This is correct, because for the characters already verified, at least the two sets $A$ and $C$ have been verified; and for the characters not yet verified, at least the two sets $B$ and $C$ are verified.

[^upper-bound]: See Example 5.2 of [国家集训队 2021 论文 徐哲安 浅谈有限状态自动机及其应用 (Chinese National Team 2021 paper collection, Xu Zhe'an: A brief discussion of finite state automata and their applications)](https://github.com/OIerTFX/IOI/blob/master/%E5%9B%BD%E5%AE%B6%E9%9B%86%E8%AE%AD%E9%98%9F2021%E8%AE%BA%E6%96%87%E9%9B%86/pdf-files/%E5%BE%90%E5%93%B2%E5%AE%89%20%E6%B5%85%E8%B0%88%E6%9C%89%E9%99%90%E7%8A%B6%E6%80%81%E8%87%AA%E5%8A%A8%E6%9C%BA%E5%8F%8A%E5%85%B6%E5%BA%94%E7%94%A8.pdf).

[^is-dfa]: The definition of an automaton in this article requires it to be complete, that is, every state must have a transition on every character. In the descriptions of these string-related automata, the failure state is usually omitted. The trie, the SAM and others are such examples. To fit the definition given in this article, the failure state needs to be added explicitly to the descriptions of these automata.
