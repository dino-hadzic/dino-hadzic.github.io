---
title: Subsequence automaton
---

Before reading this article, please read [Automata](../misc/fsm.md).

## Definition

A subsequence automaton is an automaton that accepts exactly the subsequences of a string.

In this article, we denote that string by $s$.

### States

If $s$ contains $n$ characters, its subsequence automaton has $n+1$ states.

Let $t$ be a subsequence of $s$. Then $\delta(start, t)$ is the ending position of the first occurrence of $t$ in $s$.

In other words, state $i$ represents the set difference between the subsequences of the prefix $s[1..i]$ and those of the prefix $s[1..i-1]$.

All states in a subsequence automaton are accepting states.

### Transitions

From the definition of the states, $\delta(u, c)=\min\{i|i>u,s[i]=c\}$, which is the position of the next occurrence of the character $c$.

Why the "next" occurrence? If $i>j$, the subsequences of the suffix $s[i..|s|]$ form a subset of the subsequences of the suffix $s[j..|s|]$, so choosing the earliest possible occurrence is always optimal.

## Implementation

Scan from right to left, maintaining the earliest occurrence of each character:

$$
\begin{array}{ll}
1 & \textbf{Input. } \text{A string } S\\
2 & \textbf{Output. } \text{The state transition of the sequence automaton of }S \\
3 & \textbf{Method. }  \\
4 & \textbf{for }c\in\Sigma\\
5 & \qquad next[c]\gets null\\
6 & \textbf{for }i\gets|S|\textbf{ downto }1\\
7 & \qquad next[S[i]]\gets i\\
8 & \qquad \textbf{for }c\in\Sigma\\
9 & \qquad\qquad \delta(i-1,c)\gets next[c]\\
10 & \textbf{return }\delta
\end{array}
$$

The complexity of this construction is $O(n|\Sigma|)$.

## Example problem

???+ example "[HEOI2015: Shortest non-common substring](https://loj.ac/problem/2123)"
    Given two strings $A$ and $B$ of lowercase English letters ($1\le |A|, |B|\le 2000$), find:
    
    1.  a shortest substring of $A$ that is not a substring of $B$;
    2.  a shortest substring of $A$ that is not a subsequence of $B$;
    3.  a shortest subsequence of $A$ that is not a substring of $B$;
    4.  a shortest subsequence of $A$ that is not a subsequence of $B$.

??? note "Solution"
    Parts 1 and 3 require suffix automata and have similar solutions. Here we only explain parts 2 and 4.
    
    Part 2 is straightforward: enumerate the substrings of A and feed them into the subsequence automaton of B. If a substring is not accepted, consider it as a candidate for the answer.
    
    Part 4 requires DP. Let $f(i, j)$ be the number of additional characters needed to obtain a non-common subsequence when we are in state $i$ in A's subsequence automaton and state $j$ in B's subsequence automaton. The transition is:
    
    $$
    f(i, j)=\min_{\delta_A(i,c)\ne \textit{null}}f(\delta_A(i, c), \delta_B(j, c))+1.
    $$
    
    The base case is $f(i, \textit{null})=0$.

??? note "Reference code"
    ```cpp
    --8<-- "docs/string/code/seq-automaton/seq-automaton_1.cpp"
    ```
