---
title: Suffix automaton (SAM)
---

## Notation

-   $\Sigma$: the alphabet. Its size is denoted $|\Sigma|$.
-   $s$: the string. Its length is $|s| = n$, indices start at $0$.
-   $t_0$: the initial state.
-   $\operatorname{endpos}(t)$: the set of end positions of the substring $t$ in the string $s$.
-   $\operatorname{link}(v)$: the suffix link of the state $v$.
-   $\operatorname{len}(v)$: the length of the longest substring corresponding to the state $v$.
-   $\operatorname{longest}(v)$: the longest substring corresponding to the state $v$.
-   $\operatorname{minlen}(v)$: the length of the shortest substring corresponding to the state $v$.
-   $\operatorname{shortest}(v)$: the shortest substring corresponding to the state $v$.

## Overview of the suffix automaton

The **suffix automaton** (SAM) is a powerful data structure that can solve many string-related problems.

For example, the following string problems can all be solved in linear time with a SAM:

-   find all occurrences of one string in another string;
-   count how many distinct substrings a given string has.

Intuitively, the SAM of a string can be understood as a compressed form of **all substrings** of the given string. A remarkable fact is that the SAM stores all this information in a highly compressed form. For a string of length $n$, its space complexity is only $O(n)$. Moreover, the time complexity of constructing the SAM is also only $O(n)$. Precisely, for $n\ge 3$, a SAM has at most $2n-1$ nodes and $3n-4$ transitions.

## Definition

The SAM of a string $s$ is the minimal [DFA](../misc/fsm.md#确定性有限状态自动机) that accepts all suffixes of $s$.

In other words:

-   The SAM is a directed acyclic graph. The nodes are called **states**, and the edges are called **transitions** between states.
-   The graph has a source $t_0$, called the **initial state**, from which all other nodes are reachable.
-   Every **transition** is labeled with some character. All transitions leaving a node are **distinct**.
-   There are one or more **terminal states**. If we start from the initial state $t_0$ and eventually arrive at a terminal state, then the concatenation of the labels of all transitions on the path is necessarily a suffix of the string $s$. Conversely, every suffix of $s$ can be formed by a path from $t_0$ to some terminal state.
-   Among all automata satisfying the conditions above, the SAM has the smallest number of nodes.

The key to the SAM lies precisely in this minimality. In fact, directly building a [trie](./trie.md) of all suffixes of $s$ (the suffix trie) also yields a DFA accepting all suffixes of $s$. However, in the worst case the automaton obtained this way has $\Theta(n^2)$ nodes, which is unacceptable. From the examples below one can see that many nodes in the DFA obtained from the trie of all suffixes are redundant and can thus be merged. The SAM takes this merging of nodes to the extreme, keeping the size of the resulting DFA within $O(n)$. In this sense, the SAM is a "compressed" trie of all suffixes of the string.

### Substrings and paths

The simplest and most important property of the SAM is that it contains information about all substrings of the string $s$. For any path starting from the initial state $t_0$, if we write down the labels of all transitions on the path, we obtain a **substring** of $s$. Conversely, every substring of $s$ corresponds to some path starting from $t_0$.

To simplify the wording, we say that a substring **corresponds** to this path (the path starting from $t_0$ whose transition labels form the substring). Conversely, we say that any path **corresponds** to the string formed by its labels.

There may be more than one path reaching a given state, so we say that a state corresponds to a set of strings, each of which corresponds to one of those paths.

### Simple examples

Here we show the suffix automata of some simple strings.

The initial state is drawn in blue, and terminal states in green.

For the string $s=\varepsilon$:

![](./images/SAM/SA.svg)

For the string $s=\texttt{a}$:

![](./images/SAM/SAa.svg)

For the string $s=\texttt{aa}$:

![](./images/SAM/SAaa.svg)

For the string $s=\texttt{ab}$:

![](./images/SAM/SAab.svg)

For the string $s=\texttt{abb}$:

![](./images/SAM/SAabb.svg)

For the string $s=\texttt{abbb}$:

![](./images/SAM/SAabbb.svg)

In the last example one can see that if we built the trie of all its suffixes directly, the paths $\texttt{bbb}$ and $\texttt{abbb}$ would lead to different nodes; but both nodes are terminal states, and no matter which character is appended, no longer match can be obtained. This shows that the two nodes behave identically with respect to the transitions of the automaton and can therefore be merged into a single node. This yields the SAM shown in the figure. The discussion below extends this idea of merging nodes to all situations and shows that, as long as nodes are merged sensibly, the resulting SAM has only $O(n)$ nodes and transitions.

## Linear-time construction algorithm

Before describing the algorithm that constructs the SAM in linear time, we need to introduce two concepts that are very important for understanding the construction and briefly prove their properties. The end positions $\operatorname{endpos}$ define the nodes of the SAM (i.e. they give the necessary and sufficient condition for merging nodes), while the suffix link $\operatorname{link}$ is simply the natural counterpart in the SAM of the [failure pointer](./ac-automaton.md#失配指针) of the Aho–Corasick automaton.

### End positions `endpos`

Consider any nonempty substring $t$ of the string $s$ and denote by $\operatorname{endpos}(t)$ the set of all end positions of $t$ in $s$ (assume characters of the string are indexed from zero). For example, for the string $\texttt{abcbc}$ we have $\operatorname{endpos}(\texttt{bc})=\{2,4\}$.

Two substrings $t_1$ and $t_2$ may have exactly the same end positions: $\operatorname{endpos}(t_1)=\operatorname{endpos}(t_2)$. This defines an equivalence relation among the substrings of $s$. All nonempty substrings of $s$ can be partitioned into **equivalence classes** according to their sets of end positions $\operatorname{endpos}$.

It is a fact that each such equivalence class corresponds to one state of the SAM[^state-endpos]. That is, as long as two substrings have the same end positions, their paths in the SAM lead to the same state. In other words, every non-initial state of the SAM corresponds to one or more nonempty substrings with the same $\operatorname{endpos}$. In short, the states of the SAM are exactly the equivalence classes of all nonempty substrings, plus the initial state.

Let us accept this fact for now; we will base the construction algorithm on it. We will also show that all properties the SAM must satisfy, except minimality, are satisfied; minimality follows from the [Myhill–Nerode theorem](../misc/fsm.md#myhillnerode-定理).

From the values of $\operatorname{endpos}$ we can derive several important conclusions that explain the relationship between the different substrings corresponding to the same state.

???+ note "Lemma 1"
    Two nonempty substrings $u$ and $w$ of $s$ (assume $\left|u\right|\le \left|w\right|$) have the same $\operatorname{endpos}$ if and only if every occurrence of $u$ in $s$ is as a suffix of $w$.

??? note "Proof"
    The lemma is obvious. If $u$ and $w$ have the same $\operatorname{endpos}$, then $u$ is a suffix of $w$ and occurs in $s$ only as a suffix of $w$. Conversely, by definition, if $u$ is a suffix of $w$ and occurs in $s$ only as a suffix of $w$, then the two substrings have the same $\operatorname{endpos}$.

???+ note "Lemma 2"
    Consider two nonempty substrings $u$ and $w$ (assume $\left|u\right|\le \left|w\right|$). Then either $\operatorname{endpos}(u)\cap \operatorname{endpos}(w)=\varnothing$ or $\operatorname{endpos}(w)\subseteq \operatorname{endpos}(u)$, depending on whether $u$ is a suffix of $w$:
    
    $$
    \begin{cases}
    \operatorname{endpos}(w) \subseteq \operatorname{endpos}(u), & \text{if } u \text{ is a suffix of } w, \\
    \operatorname{endpos}(w) \cap \operatorname{endpos}(u) = \varnothing, & \text{otherwise}.
    \end{cases}
    $$

??? note "Proof"
    If the sets $\operatorname{endpos}(u)$ and $\operatorname{endpos}(w)$ have at least one common element, then since the strings $u$ and $w$ end at the same position, $u$ is a suffix of $w$. Hence at every position where $w$ occurs, the substring $u$ also occurs. Therefore $\operatorname{endpos}(w)\subseteq \operatorname{endpos}(u)$.

???+ note "Lemma 3"
    Consider an equivalence class of substrings with the same $\operatorname{endpos}$ and sort all substrings in the class by decreasing length. Then each substring is exactly $1$ shorter than the previous one and, at the same time, is a suffix of the previous one. In other words, for any two substrings of the same equivalence class, the shorter one is a suffix of the longer one, and the lengths of the substrings in the class are consecutive, taking all integer values in some interval.

??? note "Proof"
    If the equivalence class contains only one substring, the lemma obviously holds. Now consider equivalence classes with more than $1$ substring.
    
    By Lemma 1, of two distinct strings with the same $\operatorname{endpos}$, one is necessarily longer and the other shorter, and the shorter one is always a proper suffix of the longer one. That is, there are no strings of equal length in an equivalence class.
    
    Let $w$ be the longest string in the class and $u$ the shortest. By Lemma 1, the string $u$ is a proper suffix of $w$. Now consider any suffix of $w$ with length in the interval $[\left|u\right|,\left|w\right|]$. It is easy to see that this suffix is in the same equivalence class, because it can occur in $s$ only as a suffix of $w$ (since the shorter suffix $u$ occurs in $s$ only as a suffix of $w$). Hence, by Lemma 1, this suffix has the same $\operatorname{endpos}$ as $w$.

In one sentence: the substrings corresponding to the same state have pairwise distinct lengths which form consecutive natural numbers, and the shorter ones are always suffixes of the longer ones.

### Suffix link `link`

Consider some state $v\neq t_0$ in the SAM. We already know that the state $v$ corresponds to an equivalence class of substrings with the same $\operatorname{endpos}$. If we define $w$ as the longest of these strings, then all the other strings are suffixes of $w$.

We also know that the first few suffixes of $w$ (considered in decreasing order of length) all belong to this equivalence class, and the remaining suffixes (at least one — the empty suffix) are in other equivalence classes. Let $t$ be the longest of these other suffixes; then we connect the suffix link of $v$ to the state corresponding to the equivalence class of $t$.

In other words, the state pointed to by the **suffix link** $\operatorname{link}(v)$ of $v$ corresponds to the longest suffix of $w$ whose $\operatorname{endpos}$ set differs from that of $w$, which is also the longest suffix of $w$ that occurs in $s$ more times than $w$.

For convenience, we stipulate that the equivalence class of the initial state $t_0$ contains only the empty string and that $\operatorname{endpos}(t_0)=\{-1,0,\ldots,\left|s\right|-1\}$.

???+ note "Lemma 4"
    All suffix links form a tree rooted at $t_0$.

??? note "Proof"
    Consider any state $v\neq t_0$; the state pointed to by the suffix link $\operatorname{link}(v)$ corresponds to strictly shorter strings (definition of the suffix link, Lemma 3). Hence, moving along suffix links, we always reach the initial state $t_0$, which corresponds to the empty string.

???+ note "Lemma 5"
    The tree whose nodes are the $\operatorname{endpos}$ sets and whose edges are given by set inclusion (i.e. the $\operatorname{endpos}$ set of every child is contained in the $\operatorname{endpos}$ set of its parent) coincides with the tree formed by the suffix links $\operatorname{link}$.

??? note "Proof"
    By Lemma 2, the $\operatorname{endpos}$ sets of any SAM form a tree (because two sets are either disjoint or one is a subset of the other).
    
    Now consider any state $v\neq t_0$ and its suffix link $\operatorname{link}(v)$; from the definition of the suffix link and Lemma 2 we obtain
    
    $$
    \operatorname{endpos}(v)\subsetneq \operatorname{endpos}(\operatorname{link}(v)).
    $$
    
    Note that this should be $\subsetneq$ rather than $\subseteq$, because if $\operatorname{endpos}(v)=\operatorname{endpos}(\operatorname{link}(v))$, then $v$ and $\operatorname{link}(v)$ should have been merged into one node.
    
    Moreover, $\operatorname{endpos}(\operatorname{link}(v))$ is exactly the smallest $\operatorname{endpos}$ set that properly contains $\operatorname{endpos}(v)$.

Combining the previous lemmas: the tree formed by the suffix links is essentially the tree formed by the $\operatorname{endpos}$ sets.

Below is an **example** of the suffix link tree produced when constructing the SAM of the string $\texttt{abcbc}$; the nodes are labeled with the longest substring of the corresponding equivalence class.

![](./images/SAM/SA_suffix_links.svg)

Developing some intuition about the suffix automaton from the figure will help in understanding the construction algorithm and the applications below.

???+ example "Explanation of the figure"
    -   There is a longest path in the SAM whose labels are exactly the string $\texttt{abcbc}$ itself. This path starts at the initial state, and every state it passes through corresponds to a prefix of $\texttt{abcbc}$ ($\varepsilon,\texttt{a},\texttt{ab},\texttt{abc},\texttt{abcb},\texttt{abcbc}$). These states are crucial in the [applications](#suffix-link-tree) below.
    -   The suffix link tree can be viewed as the result of "compressing" the paths along which these "prefix states" move along suffix links to the root (the initial state).
    
        -   Along each such path, the sets of strings corresponding to the nodes form a partition of all suffixes of the corresponding prefix. For example, the path from the state labeled $\texttt{abcbc}$ along suffix links to the root is $\texttt{abcbc}\rightarrow\texttt{bc}\rightarrow\varepsilon$. Here the node $\texttt{abcbc}$ actually corresponds to the set of strings $\{\texttt{abcbc},\texttt{bcbc},\texttt{cbc}\}$, the node $\texttt{bc}$ to the set $\{\texttt{bc},\texttt{c}\}$, and the node $\varepsilon$ to the empty string.
        -   Different paths may share the same node, which is why we speak of "compression". For example, the paths $\texttt{abc}\rightarrow\texttt{bc}\rightarrow\varepsilon$ and $\texttt{abcbc}\rightarrow\texttt{bc}\rightarrow\varepsilon$ share the node $\texttt{bc}$. This is because $\operatorname{endpos}(\texttt{bc})=\{2,4\}$, and the string $\texttt{bc}$ ending at position $2$ is immediately preceded by the character $\texttt{a}$, while the string $\texttt{bc}$ ending at position $4$ is immediately preceded by the character $\texttt{c}$; therefore, when a character is prepended (i.e. when moving against the suffix links), the set of end positions (i.e. the state) splits.
        -   The suffix link tree only needs to "compress" these suffix paths sensibly, without considering any other nodes. This is because every substring is a suffix of some prefix and hence necessarily appears on some such path. The construction algorithm below essentially adds characters one by one and, for each newly added prefix, builds such a suffix path and "compresses" it sensibly into the previously existing paths (i.e. it does not rebuild states and transitions that already exist).
        -   The terminal states are exactly all nodes on the suffix path of the string $\texttt{abcbc}$ itself.
    -   Transitions leading to the same state necessarily have the same label, and their sources must lie on some (contiguous) path in the suffix link tree. For example, there are two states with a transition to the state $\texttt{abcb}$: $\texttt{abc}$ and $\texttt{bc}$. They lie on the path $\texttt{abc}\rightarrow\texttt{bc}$ of the suffix link tree. Note that they correspond to the sets of strings $\{\texttt{abc}\}$ and $\{\texttt{bc},\texttt{c}\}$ respectively; appending the character $\texttt{b}$ to these strings gives the set of strings $\{\texttt{abcb},\texttt{bcb},\texttt{cb}\}$ corresponding to the state $\texttt{abcb}$.
    
        -   After appending a character, different states may transition to the same state because appending a character can only reduce the number of occurrences, so originally different sets of end positions may become identical.
    -   In the suffix link tree, the $\operatorname{endpos}$ set of every node is the union of the $\operatorname{endpos}$ sets of its children, plus at most one additional position. This new position exists if and only if the node corresponds exactly to the prefix of the original string ending at that position. Since in the figure no non-root, non-leaf node of the suffix link tree corresponds to a prefix of the string $\texttt{abcbc}$, this situation does not occur there.

The suffix automaton stores information about all substrings of the string. This can be understood from two perspectives:

-   The SAM itself can be viewed as a compressed version of the trie of all suffixes of the string. Hence it stores information about all prefixes of all suffixes of the string, which amounts to storing information about all substrings of the string.
-   The suffix link tree of the SAM can be viewed as a compressed version of the suffix paths of all prefixes of the string. Hence it stores information about all suffixes of all prefixes of the string, which also amounts to storing information about all substrings of the string.

Both perspectives are useful when dealing with different problems.

### Summary

Before discussing the algorithm itself further, let us summarize the previous content and introduce some auxiliary notation.

-   The substrings of $s$ can be partitioned into several equivalence classes according to their sets of end positions $\operatorname{endpos}$.

-   The SAM consists of the initial state $t_0$ and one state for each $\operatorname{endpos}$ equivalence class (of nonempty substrings).

-   Every state $v$ matches one or more substrings. We denote by $\operatorname{longest}(v)$ the longest of these strings and by $\operatorname{len}(v)$ its length. Similarly, we denote by $\operatorname{shortest}(v)$ the shortest substring and by $\operatorname{minlen}(v)$ its length. Then all strings corresponding to this state are distinct suffixes of the string $\operatorname{longest}(v)$, and their lengths take exactly every integer value in the interval $[\operatorname{minlen}(v),\operatorname{len}(v)]$.

-   For any state $v\neq t_0$, the suffix link is defined as the edge to the state corresponding to the suffix of $\operatorname{longest}(v)$ of length $\operatorname{minlen}(v)-1$. All suffix links form a tree rooted at $t_0$. This tree also represents the inclusion relation among the $\operatorname{endpos}$ sets.

-   For any state $v\neq t_0$, $\operatorname{minlen}(v)$ can be expressed via the suffix link $\operatorname{link}(v)$:

    $$
    \operatorname{minlen}(v)=\operatorname{len}(\operatorname{link}(v))+1.
    $$

-   If we start from any state $v_0$ and follow the suffix links, we always reach the initial state $t_0$. In doing so we obtain a sequence of pairwise disjoint intervals $[\operatorname{minlen}(v_i),\operatorname{len}(v_i)]$ whose union forms the contiguous interval $[0,\operatorname{len}(v_0)]$.

### Algorithm

Now we can discuss the algorithm for constructing the SAM. The algorithm is **online**: we can add the characters of the string one by one and maintain the SAM accordingly at every step.

Before discussing the detailed implementation, let us first get a feel, with the help of figures, for how the SAM may change when a new character $c$ is added.

???+ note "A simple understanding of the incremental construction"
    From the SAM of the string $s$, we can construct the SAM of the string $s+c$. According to the earlier explanation of the figure, it suffices to construct the suffix path of the newly added prefix (i.e. $s+c$) and compress it into the existing paths. Moreover, by the earlier description, the nodes on the new suffix path can all be reached by transitions on the character $c$ from the nodes on the suffix path of the original string $s$.
    
    We first consider what form the suffix path of the original string $s$ may have before the new character $c$ is added, and how it transitions on the character $c$. The most general case is shown in the following figure:
    
    ![](./images/SAM/sam-suffix-path-1.svg)
    
    In the figure, the suffix path of the original string $s$ is $p_0\rightarrow p_1\rightarrow\cdots\rightarrow p_6\rightarrow t_0$, and the suffix links are drawn as red arrows. Some of these nodes (namely $p_2\sim p_6$) already have a transition on the character $c$; because appending the same character to consecutive suffixes yields consecutive suffixes again, the targets of these transitions form another suffix path $q_1\rightarrow q_2\rightarrow q_3\rightarrow t_0$. Two observations can be made here:
    
    -   On the suffix path of the original string $s$, the nodes without a transition on $c$ are necessarily the first few nodes. As soon as some node (in the figure, $p_2$) has a transition on $c$, all subsequent nodes on the path also have a transition on $c$.
    
        **Explanation**: let $s_2=\operatorname{longest}(p_2)$; then all subsequent nodes correspond to suffixes of $s_2$, so if $s_2+c$ occurs in $s$, then every suffix of $s_2$ followed by $c$ also occurs in $s$, and hence all these nodes have a transition on $c$.
    -   Although the nodes that transition on the character $c$ to a node $q_i$ necessarily form a contiguous segment in the suffix link tree, this segment need not lie entirely on the suffix path from $p_0$ to the root. Specifically, only the first few nodes of the segment corresponding to the first node $q_1$ **may** be off this suffix path. For example, the node $q_1$ in the figure corresponds to the nodes $p_1'\rightarrow p_2\rightarrow p_3$, where $p_1'$ is not on the suffix path of $p_0$.
    
        **Explanation**: let $s_2=\operatorname{longest}(p_2)$; then $s_2+c$ corresponds to $q_1$, but in the figure clearly $s_2+c\neq\operatorname{longest}(q_1)$, because the latter is $\operatorname{longest}(p'_1)+c$. This shows that some of the strings corresponding to $q_1$ cannot be reached from $s_2$ and its suffixes. Conversely, the strings in $q_2$ are necessarily suffixes of $s_2+c$, so after removing the trailing $c$ they are necessarily suffixes of $s_2$. That is, the nodes that transition on $c$ to $q_2$ must lie on the suffix path starting at $p_2$. This is why only part of the segment corresponding to the first node $q_1$ may be off the suffix path of $p_0$.
    
    For this figure, what changes if we append a character $c$ to the end of the original string $s$ and construct the corresponding suffix path? The answer is shown in the following figure:
    
    ![](./images/SAM/sam-suffix-path-2.svg)
    
    Since the node $q_0$ is reached from the node $p_0$ corresponding to the original string $s$ by a transition on the character $c$, it corresponds to the new string $s+c$. Therefore its suffix path $q_0\rightarrow q_1''\rightarrow q_2\rightarrow q_3\rightarrow t_0$ is the newly added suffix path. If a node $p_i$ on the original suffix path already had a transition on $c$, the new suffix path necessarily passes through the nodes reached by those transitions, so the old nodes can be reused directly. On the new suffix path there is exactly one completely new node, $q_0$, which receives the transitions from those initial nodes of the original suffix path that had no transition on $c$.
    
    Besides these obvious facts, note that the original node $q_1$ has also been copied once, or in other words split into two nodes $q'_1\rightarrow q_1''$. This is because the new suffix path only partially overlaps with the existing path: among the strings corresponding to the original node $q_1$, only the shorter ones (i.e. those that can be reached from the nodes $p_2$ and $p_3$) appear on the new suffix path, while the longer ones (i.e. those that can be reached from the node $p_1'$) do not appear on it; hence the new suffix path can pass through only part of the node $q_1$, which must be split into two nodes to represent this situation. By the same reasoning, as explained earlier, the nodes $q_2$ and $q_3$ after $q_1$ cannot be reached from nodes off the suffix path of $p_0$, so all strings corresponding to these nodes appear on the new suffix path and no splitting is needed.
    
    From the point of view of what states in the SAM represent, every state is an $\operatorname{endpos}$ set. Suppose the new end position added when extending the string is $i$; then the new node $q_0$ is the set of end positions $\{i\}$, the split nodes $q_1'$ and $q_1''$ correspond to the sets $\operatorname{endpos}(q_1)$ and $\operatorname{endpos}(q_1)\cup\{i\}$ respectively, and the subsequent nodes $q_2$ and $q_3$ actually have $i$ added to their original sets of end positions. That is, although $q_2$ and $q_3$ and their transitions have not changed, their corresponding $\operatorname{endpos}$ sets have indeed grown.
    
    What has been described above is the most complex, most general case (namely **case 3** below). In practice, the node $p'_1$ may not exist, so no splitting is needed (namely **case 2** below). To detect this situation, it suffices to check whether $\operatorname{longest}(q_1)=\operatorname{longest}(p_2)+c$, i.e. $\operatorname{len}(q_1)=\operatorname{len}(p_2)+1$. It is also possible that none of the nodes on the suffix path of $p_0$ has a transition on $c$; in that case it suffices to create $q_0$ (namely **case 1** below).

Having grasped the idea of adding a suffix path, we now discuss the concrete steps of the incremental construction.

#### Procedure

To guarantee linear space complexity, we will only store the values of $\operatorname{len}$ and $\operatorname{link}$ and the list of transitions of every state; we will not mark terminal states (but we will show later how to assign these marks after constructing the SAM).

Initially the SAM contains only one state $t_0$, numbered $0$ (the other states are numbered $1,2,\ldots$). For convenience, for the state $t_0$ we set $\operatorname{len}(t_0)=0$ and $\operatorname{link}(t_0)=-1$ ($-1$ denotes a virtual state).

Now it only remains to implement the procedure that appends a character $c$ to the current string. The algorithm proceeds as follows:

???+ note "Incremental construction procedure of the SAM"
    -   Let $\textit{last}$ be the state corresponding to the whole string before the character $c$ is added (initially we set $\textit{last}=0$, and the last step of the algorithm updates $\textit{last}$).
    -   Create a new state $\textit{cur}$ and set $\operatorname{len}(\textit{cur})$ to $\operatorname{len}(\textit{last})+1$; at this point the value of $\operatorname{link}(\textit{cur})$ is still unknown.
    -   Now we perform the following procedure: starting from the state $\textit{last}$, if the current state does not yet have a transition labeled with the character $c$, we add a transition on $c$ to the state $\textit{cur}$ and move the current state along its suffix link. If during this process we encounter a state that already has a transition on $c$, we stop and call this state $p$.
    -   **Case 1**: if no such state $p$ is found, we have reached the virtual state $-1$; we set $\operatorname{link}(\textit{cur})$ to $0$ and go to the last step.
    -   Suppose now that we have found a state $p$ with a transition on the character $c$. Denote the target of this transition by $q$. Then either $\operatorname{len}(p)+1=\operatorname{len}(q)$ or $\operatorname{len}(p)+1<\operatorname{len}(q)$.
    -   **Case 2**: if $\operatorname{len}(p)+1=\operatorname{len}(q)$, we just set $\operatorname{link}(\textit{cur})$ to $q$ and go to the last step.
    -   **Case 3**: otherwise things are a bit more complicated and we need to **clone** the state $q$: we create a new state $\textit{clone}$ and copy all information of $q$ (suffix link and transitions) except the value of $\operatorname{len}$. We set $\operatorname{len}(\textit{clone})$ to $\operatorname{len}(p)+1$.
    
        After cloning, we point the suffix link from $\textit{cur}$ to $\textit{clone}$, and also from $q$ to $\textit{clone}$.
    
        Finally we need to walk back from the state $p$ along suffix links, and as long as the visited state has a transition to the state $q$, we redirect that transition to the state $\textit{clone}$.
    -   After handling any of the three cases above, we update the value of $\textit{last}$ to the state $\textit{cur}$.

If we also want to know which states are **terminal** and which are not, we can find all terminal states after constructing the complete SAM of the string $s$. To do so, we start from the state corresponding to the whole string (stored in the variable $\textit{last}$) and follow its suffix links until we reach the initial state. We mark all visited states as terminal. It is easy to see that in this way we mark exactly all suffixes of $s$, and these states are the terminal ones.

Since we create only one or two new states for each character of $s$, the SAM contains only a **linear number** of states. That the SAM also has only a linear number of transitions, and that the overall running time of the algorithm is linear, has not yet been made clear and will be explained below.

#### Explanation

We explain the details of every step of the algorithm and show its **correctness**.

???+ note "Detailed explanation of the algorithm"
    -   If a transition $(p,q)$ satisfies $\operatorname{len}(p)+1=\operatorname{len}(q)$, we call this transition **continuous**. Otherwise, i.e. when $\operatorname{len}(p)+1<\operatorname{len}(q)$, the transition is called **non-continuous**.
    
        From the description of the algorithm one can see that continuous and non-continuous transitions are also handled differently in the algorithm. Continuous transitions are fixed; we never change them again. In contrast, when a new character is inserted into the string, non-continuous transitions may change (the endpoints of the transition edge may change).
    -   To avoid ambiguity, we denote by $s$ the string before the current character $c$ is inserted into the SAM.
    -   The algorithm starts by creating a new state $\textit{cur}$, which corresponds to the whole string $s+c$. The reason for creating a new node is clear: at the same time we also create a new equivalence class.
    -   After creating the new state, we move along suffix links from the state $\textit{last}$ corresponding to the whole string $s$. For every visited state we try to add a transition on the character $c$ to the new state $\textit{cur}$.
    
        However, we can only add transitions that do not conflict with existing ones. Hence, as soon as we find an existing transition on $c$, we must stop.
    -   The simplest case is that we reach the virtual state $-1$, which means that we added a transition on $c$ for all suffixes of $s$. This also means that the character $c$ never occurred in the string $s$ before. Therefore the suffix link of $\textit{cur}$ is the state $0$.
    -   Otherwise (i.e. in cases 2 and 3), we found an existing transition $(p,q)$. This means that we are trying to add to the automaton a string $x+c$ that **already exists** (where $x=\operatorname{longest}(p)$ is a suffix of $s$, and the string $x+c$ has already appeared as a substring of $s$). Since we assume the automaton of the string $s$ was built correctly, we should not add a new transition here.
    
        The difficulty, however, is: to which state should the suffix link from $\textit{cur}$ point? We need to point the suffix link to a state whose longest corresponding string is exactly $x+c$, i.e. whose $\operatorname{len}$ should be $\operatorname{len}(p)+1$. However, such a state may not exist, i.e. $\operatorname{len}(q)>\operatorname{len}(p)+1$. In this case we must create such a state by splitting the state $q$.
    -   Of course, if the transition $(p,\,q)$ is continuous, then $\operatorname{len}(q)=\operatorname{len}(p)+1$. In this case everything is simple. We just point the suffix link of $\textit{cur}$ to the state $q$.
    -   Otherwise the transition is non-continuous, i.e. $\operatorname{len}(q)>\operatorname{len}(p)+1$, which means that the state $q$ corresponds not only to the suffix $x+c$ of length $\operatorname{len}(p)+1$, but also to longer substrings of $s$. We have no choice but to split the state $q$ into two sub-states, so that the length of the first sub-state is $\operatorname{len}(p)+1$.
    
        How do we split a state? We **clone** the state $q$, producing a state $\textit{clone}$, and set $\operatorname{len}(\textit{clone})$ to $\operatorname{len}(p)+1$. Since we do not want to change the paths passing through $q$, we copy all transitions of $q$ to $\textit{clone}$. We also set the suffix link from $\textit{clone}$ to the target of the suffix link of $q$, and set the suffix link of $q$ to $\textit{clone}$.
    
        After splitting the state, we set the suffix link from $\textit{cur}$ to $\textit{clone}$.
    
        In the last step we redirect some transitions that originally pointed to $q$ to $\textit{clone}$. Which transitions do we need to modify? It suffices to redirect the transitions corresponding to all suffixes of the string $x+c$ (where $x=\operatorname{longest}(p)$). That is, we need to keep moving along suffix links from the node $p$ until we reach the virtual state $-1$, or until the transition of the current state on $c$ no longer points to the state $q$.

### Linear time complexity

We assume that the alphabet size is **constant**, i.e. that the operations of searching for a transition on a character, adding a transition, and finding the next transition all take $O(1)$ time. If the transitions of every node are stored both as an array of length $\left|\Sigma\right|$ (for quickly looking up a transition by label) and as a dynamic list (for quickly iterating over all existing transitions), trading space for time, then the time complexity of the algorithm[^time-complexity] is $O(n)$ and the space complexity is $O(n\left|\Sigma\right|)$.

??? note "Proof"
    If we consider the parts of the algorithm, there are three places where the time complexity is not obviously linear:
    
    -   the first is traversing the suffix links from the state $\textit{last}$ and adding transitions on the character $c$;
    -   the second is copying the transitions when the state $q$ is cloned into a new state $\textit{clone}$;
    -   the third is modifying the transitions pointing to $q$ and redirecting them to $\textit{clone}$.
    
    We use the fact that the size of the SAM (the number of states and transitions) is **linear** (the proof for the number of states is the algorithm itself; the proof for the number of transitions is given below, after the implementation of the algorithm).
    
    Hence the total complexity of the **first and second** places is obviously linear, because a single operation adds, amortized, only one new transition to the automaton.
    
    It remains to estimate the total complexity of the **third** place, where we redirect the transitions originally pointing to $q$ to $\textit{clone}$. Let $v=\operatorname{longest}(p)$; this is a suffix of the string $s$. In each iteration the length of $v$ decreases, so the starting position of $v$ as a suffix of $s$ necessarily moves to the right. Therefore the number of times $p$ moves along suffix links in the loop does not exceed the distance by which the starting position of $v$ as a suffix of $s$ moves to the right. Since $p$ must move at least once for the loop to terminate, and $p$ is at least the result of moving $\textit{last}$ once along a suffix link, when the loop terminates the starting position of $v$ as a suffix of $s$ is not to the left of that of the string $\operatorname{longest}(\operatorname{link}(\operatorname{link}(\textit{last})))$. Moreover, when the loop terminates, the starting position of the string $v$ as a suffix of $s$ is exactly the starting position of $v+c$ as a suffix of $s+c$, and as a suffix of $s+c$ the string $v+c$ is exactly the string $\operatorname{longest}(\operatorname{link}(\operatorname{link}(\textit{cur})))$. Since $\textit{cur}$ is the updated value of $\textit{last}$, the number of moves in the loop does not exceed the distance by which the starting position of $\operatorname{longest}(\operatorname{link}(\operatorname{link}(\textit{last})))$ as a suffix of the current string moves to the right between before and after the update, plus one (the move necessary to terminate the loop).
    
    Since the position of the string $\operatorname{longest}(\operatorname{link}(\operatorname{link}(\textit{last})))$ as a suffix of the current string is monotonically increasing throughout the construction of the SAM[^monotone-loc], its total movement does not exceed $n$. This shows that the number of iterations of the loop that modifies the transitions pointing to $q$ does not exceed $2n$. This is exactly what we needed to prove.

Of course, if the alphabet size is not constant and we are not willing to spend $O(n\left|\Sigma\right|)$ space, the time complexity of the SAM is not linear. The transitions from a node then need to be stored in a balanced tree supporting fast lookup and insertion. Hence, if we denote the alphabet by $\Sigma$ and its size by $\left|\Sigma\right|$, the asymptotic time complexity of the algorithm is $O(n\log\left|\Sigma\right|)$ and the space complexity is $O(n)$.

### Implementation

First, we implement a data structure that stores all the information of a transition. If needed, you can add a terminal flag here, or some other information. We will store the list of transitions in a `map`, which allows us to process the whole string in $O(n)$ total space and $O(n\log\left|\Sigma\right|)$ time. Of course, when the alphabet size $\left|\Sigma\right|=K$ is a small constant (e.g. 26), it is more convenient to declare `next` as `int[K]`.

```cpp
struct state {
  int len, link;
  std::map<char, int> next;
};
```

The SAM itself will be stored in an array of `state` structs. We keep the current size of the automaton `sz` and the variable `last`, the state corresponding to the current whole string.

```cpp
constexpr int MAXLEN = 100000;
state st[MAXLEN * 2];
int sz, last;
```

We define a function to initialize the SAM (create a SAM with only the initial state).

```cpp
void sam_init() {
  for (int i = 0; i < sz; i++) st[i].next.clear();
  st[0].len = 0;
  st[0].link = -1;
  sz = 1;
  last = 0;
}
```

Finally we give the implementation of the main function: append a character to the end of the current string and build the automaton accordingly on top of the previous one.

???+ note "Implementation"
    ```cpp
    void sam_extend(char c) {
      int cur = sz++;
      st[cur].len = st[last].len + 1;
      int p = last;
      while (p != -1 && !st[p].next.count(c)) {
        st[p].next[c] = cur;
        p = st[p].link;
      }
      if (p == -1) {
        st[cur].link = 0;
      } else {
        int q = st[p].next[c];
        if (st[p].len + 1 == st[q].len) {
          st[cur].link = q;
        } else {
          int clone = sz++;
          st[clone].len = st[p].len + 1;
          st[clone].next = st[q].next;
          st[clone].link = st[q].link;
          while (p != -1 && st[p].next[c] == q) {
            st[p].next[c] = clone;
            p = st[p].link;
          }
          st[q].link = st[cur].link = clone;
        }
      }
      last = cur;
    }
    ```

As mentioned before, if you trade memory for time (space complexity $O(n\left|\Sigma\right|)$, where $\left|\Sigma\right|$ is the alphabet size), you can construct the SAM over an alphabet of arbitrary size in $O(n)$ time[^time-complexity]. But then you need to store, for every state, an array of size $\left|\Sigma\right|$ (for quickly finding the transition by character) and a list of all existing transitions (for quickly iterating over all existing transitions).

## More properties

### Number of states

For a string $s$ of length $n$, the number of states in its SAM **does not exceed** $2n-1$ (assuming $n\ge 2$).

??? note "Proof"
    The algorithm itself proves this claim. Initially the automaton contains one state, the first and second iterations create only one node each, and each of the remaining $n-2$ steps creates at most $2$ states.
    
    However, we can also **prove** this estimate **without relying on the algorithm**. If $s$ consists of a single repeated character, the number of states is $n+1$ and the claim is obvious; so assume $s$ contains at least two distinct characters. Recall that the number of states equals the number of distinct $\operatorname{endpos}$ sets. These $\operatorname{endpos}$ sets form a tree (the $\operatorname{endpos}$ set of a parent contains the $\operatorname{endpos}$ set of a child). Consider modifying this tree slightly: whenever it has an internal node with only one child (which means the child's set misses at least one position of the parent's set), we create a set containing these missing positions as a new child. In the end we obtain a tree in which every internal node has more than one child and the number of leaves does not exceed $n$. Such a tree has at most $2n-1$ nodes, so the number of distinct $\operatorname{endpos}$ sets in the original tree also does not exceed $2n-1$.
    
    The string $\texttt{abbb} \cdots \texttt{bbb}$ attains this upper bound: in every iteration starting from the third, the algorithm splits a state, producing exactly $2n-1$ states in the end.

### Number of transitions

For a string $s$ of length $n$, the number of transitions in its SAM **does not exceed** $3n-4$ (assuming $n\ge 3$).

??? note "Proof"
    We first estimate the number of continuous transitions. Consider the spanning tree of the automaton formed by the longest paths from the state $t_0$ to all states. The spanning tree contains only continuous edges, so their number is less than the number of states, i.e. the number of edges does not exceed $2n-2$.
    
    Now we estimate the number of non-continuous transitions. Let the current non-continuous transition be $(p,\,q)$ with character $c$. Take its corresponding string $u+c+w$, where the string $u$ corresponds to the longest path from the initial state to $p$, and $w$ corresponds to the longest path from $q$ to any terminal state. On the one hand, the strings of the form $u+c+w$ corresponding to different non-continuous transitions are distinct (because $u$ consists only of continuous transitions, the first non-continuous transition passed along $u+c+w$ is exactly $(p,\,q)$). On the other hand, by the definition of terminal states, every string of the form $u+c+w$ is a suffix of the whole string $s$. Since $s$ has only $n$ nonempty suffixes, and no string of the form $u+c+w$ equals $s$ (because the path corresponding to $s$ contains only continuous transitions), the total number of non-continuous transitions does not exceed $n-1$.
    
    Adding the two estimates, we obtain the upper bound $3n-3$. However, the maximum number of states can only be attained in cases like $\texttt{abbb} \cdots \texttt{bbb}$, and then the number of transitions is clearly less than $3n-3$.
    
    Hence we obtain a tighter upper bound on the number of transitions of the SAM: $3n-4$. The string $\texttt{abbb} \cdots \texttt{bbbc}$ attains this bound.

### Suffix link tree

Although the SAM is constructed to obtain information about its states and transitions, the suffix links $\operatorname{link}$ recorded during the construction and the lengths $\operatorname{len}$ of the longest substrings corresponding to the states are often more important in applications than the transitions of the SAM, and can even be used on their own without the transitions.

During the construction of the SAM, the value of the state $\textit{last}$ needs to be updated. It corresponds to the string before (or after) each addition of a character, i.e. to all prefixes of the whole string $s$. Denote the state corresponding to the $i$-th prefix by $v_i$; this gives $n$ states $v_0,v_1,\cdots,v_{n-1}$ in total. In addition, we define the initial state $t_0$ to be $v_{-1}$, corresponding to the empty prefix. We tentatively call these states "prefix nodes".

Lemma 4 mentioned that all states and all suffix links form a tree directed toward the root $t_0$; this tree is also called the **suffix link tree** (Chinese OI contestants often also call it the **parent tree**). It records information about all suffixes of all prefixes of the string, i.e. about all substrings.

The suffix link tree has the following properties:

-   The string corresponding to an ancestor is always a suffix of the string corresponding to a descendant.
-   The $\operatorname{endpos}$ set of every node is exactly the set of indices $i$ of all "prefix nodes" $v_i$ in its subtree.
-   The $\operatorname{endpos}$ set of an ancestor in the suffix link tree always strictly contains the $\operatorname{endpos}$ set of a descendant.
-   The value of $\operatorname{len}$ at every node is the length of the longest common suffix of the prefixes corresponding to all "prefix nodes" $v_i$ in its subtree.
-   Except for the root $t_0$, the number of distinct substrings corresponding to a node is its $\operatorname{len}$ value minus the $\operatorname{len}$ value of its parent, i.e. $\operatorname{len}(v)-\operatorname{len}(\operatorname{link}(v))$.

These properties have many applications. For example, the longest common suffix of the $i$-th and the $j$-th prefix is exactly the longest string corresponding to the LCA of $v_i$ and $v_j$.

Finally, the suffix link tree built for the string $s$ has the same structure as the [suffix tree](./suffix-tree.md) built for its reverse $s_R$. This is often used to construct the suffix tree offline.

## Applications

Let us now look at some problems that can be solved with a SAM. For simplicity, assume that the alphabet size $|\Sigma|$ is constant. This allows us to consider the complexity of adding a character and of traversing to be constant.

### Checking whether a string occurs

???+ example "Problem"
    Given a text $T$ and several patterns $P$, we want to check whether the string $P$ occurs as a substring of $T$.

??? note "Solution"
    We build the suffix automaton of the text $T$ in $O(\left|T\right|)$ time. To check whether the pattern $P$ occurs in $T$, we follow the transitions (edges) from $t_0$ according to the characters of $P$. If at some point no transition is available, the pattern $P$ is not a substring of $T$. If we can process the whole string $P$ this way, the pattern occurs in $T$.
    
    For every string $P$, the time complexity of the algorithm is $O(\left|P\right|)$. Moreover, this algorithm also finds the maximum length of a prefix of the pattern $P$ that occurs in the text.

### Number of distinct substrings

???+ example "Problem"
    Given a string $S$, count the number of distinct substrings.

??? note "Solution 1"
    Build the suffix automaton of the string $S$.
    
    Every substring of $S$ corresponds to a path in the automaton. Hence the number of distinct substrings equals the number of distinct nonempty paths in the automaton starting at $t_0$.
    
    Since the SAM is a directed acyclic graph, the number of distinct paths can be computed by dynamic programming. Let $d_{v}$ be the number of paths starting from the state $v$ (including the path of length zero); then we have the following recurrence:
    
    $$
    d_{v}=1+\sum_{w:(v,w,c)\in \text{SAM}}d_{w}
    $$
    
    That is, $d_{v}$ equals $1$ plus the sum of the $d$ values of the targets of all transitions of $v$, where $(v,w,c)\in \text{SAM}$ denotes that the suffix automaton has a transition from $v$ to $w$ on $c$.
    
    So the number of distinct substrings is $d_{t_0}-1$ (because the empty substring must be excluded).
    
    Total time complexity: $O(\left|S\right|)$.

??? note "Solution 2"
    Another method is to use the information of the suffix link tree obtained after building the suffix automaton. The number of substrings corresponding to a node is $\operatorname{len}(v)-\operatorname{len}(\operatorname{link}(v))$; just sum over all nodes except $t_0$.
    
    The total time complexity is still $O(\left|S\right|)$.

Example problems: [[Template] Suffix automaton](https://www.luogu.com.cn/problem/P3804), [SDOI2016 Generating spells (生成魔咒)](https://loj.ac/problem/2033)

### Total length of all distinct substrings

???+ example "Problem"
    Given a string $S$, compute the total length of all distinct substrings.

??? note "Solution 1"
    The approach is similar to the previous problem, except that now we need to do the dynamic programming in two parts: the number of distinct substrings $d_{v}$ and their total length $ans_{v}$.
    
    We already described how to compute $d_{v}$ in the previous problem. The value of $ans_{v}$ can be computed by the following recurrence:
    
    $$
    ans_{v}=\sum_{w:(v,w,c)\in \text{SAM}}(d_{w}+ans_{w})
    $$
    
    We take the answer of every adjacent node $w$ and add $d_{w}$ (because every substring starting from the state $v$ is extended by one character).
    
    The time complexity of the algorithm is still $O(\left|S\right|)$.

??? note "Solution 2"
    The information of the suffix link tree can be used here as well. The sum of the lengths of all suffixes of the longest substring corresponding to a node is
    
    $$
    \dfrac{\operatorname{len}(v)\times (\operatorname{len}(v)+1)}{2},
    $$
    
    and subtracting the corresponding value of its $\operatorname{link}$ node gives the net contribution of that node; just sum over all nodes except $t_0$.
    
    The total time complexity is still $O(\left|S\right|)$.

### Lexicographically k-th smallest substring

???+ example "Problem"
    Given a string $S$. There are several queries; each query gives a number $K_i$ and asks for the lexicographically $K_i$-th smallest substring among all distinct substrings of $S$.

??? note "Solution"
    The idea for solving this problem develops from the ideas for the previous two problems. The lexicographically $K_i$-th smallest substring corresponds to the lexicographically $K_i$-th smallest nonempty path in the SAM, so after computing the number of paths from every state, we can easily find the $K_i$-th smallest path starting from the root of the SAM.
    
    The preprocessing time complexity is $O(\left|S\right|)$, and the complexity of a single query is $O(\left|ans\right|\cdot\left|\Sigma\right|)$ (where $ans$ is the answer to the query and $\left|\Sigma\right|$ is the alphabet size).

??? info "Remark"
    Although this is a classic suffix automaton problem, since it involves lexicographic order it is actually most convenient to solve with a suffix array.

Example problems: [SPOJ - SUBLEX](https://www.spoj.com/problems/SUBLEX/), [TJOI2015 String theory (弦论)](https://loj.ac/problem/2102)

### Smallest cyclic shift

???+ example "Problem"
    Given a string $S$. Find the lexicographically smallest cyclic shift.

??? note "Solution"
    It is easy to see that the string $S+S$ contains all cyclic shifts of $S$ as substrings.
    
    So the problem reduces to finding the smallest path of length $\left|S\right|$ in the suffix automaton of $S+S$, which can be done trivially: we start from the initial state and greedily visit the smallest character.
    
    The total time complexity is $O(\left|S\right|)$.

### Number of occurrences

???+ example "Problem"
    For a given text $T$, there are several queries; each query gives a pattern $P$ and asks how many times $P$ occurs in $T$ as a substring.

??? note "Solution 1"
    Using the information of the suffix link tree, a DFS suffices to preprocess the size of the $\operatorname{endpos}$ set of every node.
    
    The initial set size of all "prefix nodes" is $1$, and that of non-"prefix nodes" is $0$. Then, when backtracking along suffix links from bottom to top, the set size of every parent is increased by the set sizes of all its children (do not forget the parent's own initial value). The value obtained at every node this way is the size of the $\operatorname{endpos}$ set of that node. The reason the set sizes of different children can be added directly is that the same $v_i$ appears in only one subtree, so there is no double counting.
    
    For a query, look up the node corresponding to the pattern $P$ in the automaton; if it exists, the answer is the size of the $\operatorname{endpos}$ set of that node; otherwise the answer is $0$.
    
    The preprocessing time complexity is $O(|T|)$. The time complexity of a single query is $O(|P|)$.

??? note "Solution 2"
    Build the suffix automaton of the text $T$.
    
    Next we preprocess: for every state $v$ of the automaton, compute $cnt_{v}$ equal to the size of the set $\operatorname{endpos}(v)$. In fact, all substrings corresponding to the same state $v$ occur the same number of times in the text $T$, which equals the number of positions in the set $\operatorname{endpos}$.
    
    However, we cannot construct the sets $\operatorname{endpos}$ explicitly, so we only consider their sizes $cnt$.
    
    To compute these values, we do the following. For every state, if it was not created by cloning (and it is not the initial state $t_0$), we initialize its $cnt$ to 1. Then we iterate over all states in decreasing order of their length $\operatorname{len}$ and add the current value $cnt_{v}$ to the state pointed to by the suffix link, i.e.:
    
    $$
    cnt_{\operatorname{link}(v)}+=cnt_{v}
    $$
    
    This gives the correct answer for every state.
    
    Why is this correct? There are exactly $\left|T\right|$ states not obtained by cloning (except $t_0$), and the first $i$ of them are created when we insert the first $i$ characters, each corresponding to one end position. Hence we initially assign $cnt=1$ to these states and $cnt=0$ to the other states.
    
    Next, for every $v$ we perform $cnt_{\operatorname{link}(v)}+=cnt_{v}$. The meaning behind this is that if the string corresponding to the state $v$ occurs $cnt_{v}$ times, then all its suffixes also end at exactly the same places, i.e. they also occur $cnt_{v}$ times.
    
    Why do we not double count in this process (i.e. count some positions twice)? Because we add the positions of a state to only **one** other state, so a state cannot pass its positions to another state in two different ways.
    
    Hence we can compute the values $cnt$ of all states in $O(\left|T\right|)$ time.
    
    Finally, to answer a query we only need to look up the value $cnt_{t}$, where $t$ is the state corresponding to the pattern; if the pattern does not exist, the answer is $0$. The time complexity of a single query is $O(\left|P\right|)$.

### Position of the first occurrence

???+ example "Problem"
    Given a text $T$ and several queries. Each query asks for the position of the first occurrence of the string $P$ in the string $T$ (the starting position of $P$).

??? note "Solution 1"
    Using the information of the suffix link tree, a DFS suffices to preprocess the minimum of the $\operatorname{endpos}$ set of every node.
    
    The initial value of all "prefix nodes" $v_i$ is $i$, and that of non-"prefix nodes" is $\infty$. Then, when backtracking along suffix links from bottom to top, the value of every parent is compared with the values of all its children and the minimum is taken (do not forget the parent's own initial value). The value obtained at every node this way is the minimum of the $\operatorname{endpos}$ set of that node.
    
    For a query, look up the node corresponding to the pattern $P$ in the automaton; if it exists, the answer is the value of that node minus $|P|-1$; otherwise there is no answer.
    
    The preprocessing time complexity is $O(|T|)$. The time complexity of a single query is $O(|P|)$.

??? note "Solution 2"
    We build a suffix automaton. We preprocess the positions $\operatorname{firstpos}$ for all states of the SAM. That is, for every state $v$ we want to find the end position $\operatorname{firstpos}[v]$ of the first occurrence of this state. In other words, we want to find the minimum element of every set $\operatorname{endpos}$ first (obviously we cannot maintain all $\operatorname{endpos}$ sets explicitly).
    
    To maintain the positions $\operatorname{firstpos}$, we extend the function `sam_extend()`. When we create a new state $\textit{cur}$, we set:
    
    $$
    \operatorname{firstpos}(\textit{cur})=\operatorname{len}(\textit{cur})-1.
    $$
    
    When we clone the node $q$ into $\textit{clone}$, we set:
    
    $$
    \operatorname{firstpos}(\textit{clone})=\operatorname{firstpos}(q).
    $$
    
    (Because the only other option for the value, $\operatorname{firstpos}(\textit{cur})$, is obviously too large.)
    
    Then the answer to a query is $\operatorname{firstpos}(t)-\left|P\right|+1$, where $t$ is the state corresponding to the string $P$. A single query takes only $O(\left|P\right|)$ time.

### All occurrence positions

???+ example "Problem"
    The problem is the same as above, but this time we need to find all positions where the pattern $P$ occurs in the text $T$.

??? note "Solution 1"
    After finding the node corresponding to the pattern $P$, use the information of the suffix link tree and traverse the subtree, outputting every "prefix node" as soon as it is found.
    
    The complexity of a single query is $O(|P|)+O(\textit{answer}(P))$, where $\textit{answer}(P)$ is the number of answers for this query. Following the [proof that the number of states is linear](#number-of-states), one can show that the size of a subtree of the suffix link tree does not exceed twice the size of the $\operatorname{endpos}$ set of that node, so the complexity of traversing the subtree is $O(\textit{answer}(P))$.

??? note "Solution 2"
    We again build the suffix automaton of the text $T$. Similarly to the previous problem, we compute the positions $\operatorname{firstpos}$ for all states.
    
    If $t$ is the state corresponding to the pattern $P$, clearly $\operatorname{firstpos}(t)$ is one of the answers. We have found the state of the automaton corresponding to $P$. Which other positions remain to be found? Exactly those corresponding to the states of strings having $P$ as a suffix. In other words, we need to find all states from which the state $t$ can be reached via suffix links.
    
    Hence, to solve this problem, we need to store for every state a list of the suffix links pointing to it. The answer to the query then consists of the $\operatorname{firstpos}$ values of all states that we can find from the state $t$ by a DFS or BFS using only the reversed suffix links.
    
    The preprocessing complexity is $O(|T|)$, and the complexity of a single query is $O(|P|+\textit{answer}(P))$.
    
    We will not visit a state twice (because every state has only one suffix link, so there are no two different paths pointing to the same state).
    
    We only need to consider two different states that may have the same $\operatorname{firstpos}$ value. This situation occurs only when one state is cloned from the other. However, this does not affect the complexity analysis. Following the [proof that the number of states is linear](#number-of-states), the number of all such states having $P$ as a suffix does not exceed $2\textit{answer}(P)$.
    
    Moreover, we can remove duplicate positions by not considering the $\operatorname{firstpos}$ values of cloned nodes. In fact, every occurrence position in the subtree of $t$ corresponds to exactly one non-cloned state. Therefore, if we record for every state a flag `is_clone` indicating whether the state was created by cloning, we can simply ignore the cloned states and output only the $\operatorname{firstpos}$ values of all other states.
    
    Below is a rough implementation:
    
    ```cpp
    struct state {
      bool is_clone;
      int first_pos;
      std::vector<int> inv_link;
      // some other variables
    };
    
    // after constructing the SAM
    for (int v = 1; v < sz; v++) st[st[v].link].inv_link.push_back(v);
    
    // output all occurrence positions
    void output_all_occurrences(int v, int P_length) {
      if (!st[v].is_clone) cout << st[v].first_pos - P_length + 1 << endl;
      for (int u : st[v].inv_link) output_all_occurrences(u, P_length);
    }
    ```

### Shortest non-occurring string

???+ example "Problem"
    Given a string $S$ and a particular alphabet, we want to find a shortest string that does not occur in $S$.

??? note "Solution"
    We do dynamic programming on the suffix automaton of the string $S$.
    
    Suppose we have already processed part of the substring and are currently in the state $v$; we want to find the minimum number of characters that must be added to encounter a nonexistent transition, and denote this number at the node $v$ by $d_v$.
    
    Computing $d_{v}$ is very simple. If at least one character of the alphabet has no transition at $v$, then $d_{v}=1$. Otherwise adding one character is not enough, and we need the minimum over all transitions:
    
    $$
    d_{v}=1+\min_{w:(v,w,c)\in \text{SAM}}d_{w}
    $$
    
    The answer to the problem is $d_{t_0}$, and the string can be reconstructed backwards from the computed array $d$.

### Longest common substring of two strings

???+ example "Problem"
    Given two strings $S$ and $T$, find the longest common substring, where a common substring is a string $X$ that occurs as a substring in both $S$ and $T$.

??? note "Solution"
    We build the suffix automaton of the string $S$.
    
    Now we process the string $T$: for each of its prefixes, we look for the longest suffix of that prefix that occurs in $S$. In other words, for every position in the string $T$ we want to find the length of the longest common substring of $S$ and $T$ ending at that position.
    
    To achieve this, we use two variables, the **current state** $v$ and the **current length** $l$. These two variables describe the current match: its length and the state corresponding to it.
    
    Initially $v=t_0$ and $l=0$, i.e. the match is the empty string.
    
    Now we describe how to add a character $T_{i}$ and recompute the answer for it:
    
    -   If there is a transition from $v$ on the character $T_{i}$, we simply take the transition and increase $l$ by one.
    -   If there is no such transition, we need to shorten the current match, which means we need to follow the suffix link:
    
        $$
        v=\operatorname{link}(v)
        $$
    
        At the same time, the current length needs to be shortened. Obviously we need to set $l$ to $\operatorname{len}(v)$, because the longest string corresponding to the state reached after following this suffix link is a substring.
    -   If there is still no transition on this character, we keep following suffix links and decreasing $l$ until we find a transition or reach the initial state $t_0$ which also has no such transition (this means that the character $T_{i}$ does not occur in $S$ at all, and then $v=l=0$).
    
    Obviously the answer to the problem is the maximum of all values $l$.
    
    The time complexity of this part is $O(\left|T\right|)$, because at every move we either increase $l$ by one or move along suffix links a few times, decreasing the value of $l$ each time.
    
    Implementation:
    
    ```cpp
    string lcs(const string &S, const string &T) {
      sam_init();
      for (int i = 0; i < S.size(); i++) sam_extend(S[i]);
    
      int v = 0, l = 0, best = 0, bestpos = 0;
      for (int i = 0; i < T.size(); i++) {
        while (v && !st[v].next.count(T[i])) {
          v = st[v].link;
          l = st[v].len;
        }
        if (st[v].next.count(T[i])) {
          v = st[v].next[T[i]];
          l++;
        }
        if (l > best) {
          best = l;
          bestpos = i;
        }
      }
      if (best == 0) return "";
      return T.substr(bestpos - best + 1, best);
    }
    ```

Example problem: [SPOJ Longest Common Substring](https://www.spoj.com/problems/LCS/en/)

### Longest common substring of multiple strings

???+ example "Problem"
    Given $k$ strings $S_i$. We need to find their longest common substring, i.e. a string $X$ that occurs as a substring in every string.

??? note "Solution 1"
    We concatenate all the strings into one longer string $T$, separating the strings by special characters $D_i$ (one character per string):
    
    $$
    T=S_1+D_1+S_2+D_2+\cdots+S_k+D_k.
    $$
    
    Then we build the suffix automaton of the string $T$.
    
    Now we need to find in the automaton a string that exists in all strings $S_i$, for which we can use the added special characters. If $S_j$ contains a substring $X$, then from the node $t$ corresponding to the substring $X$ there necessarily exists a path reaching $D_j$ without passing through any other special character $D_1,\cdots,D_{j-1},D_{j+1},\cdots,D_k$. For a common substring $X$, such a path must exist for every special character $D_j$.
    
    Hence we need to compute reachability, i.e. for every state of the automaton and every character $D_i$, whether such a path exists. This can easily be computed with DFS or BFS and dynamic programming. After that, the answer to the problem is the longest among the longest substrings $\operatorname{longest}(v)$ of all states $v$ that can reach all special characters.

??? note "Solution 2"
    Without loss of generality, let the **shortest** string be $S_1$ and build the SAM for it. Using the algorithm for the longest common substring of two strings, compute the length of the longest common substring of each remaining string with $S_1$. During the matching, every time a character of the string $S_j$ being matched is added, we move accordingly on the SAM, so we can directly record, for every state of the SAM, the length of the longest substring of $S_j$ it matched **during the matching process**.
    
    Because during the matching, whenever a state of the SAM is matched, all its ancestors in the suffix link tree are necessarily matched at the same time, but the matching length information of the ancestors is not updated, after finishing the matching of the string $S_j$ we need to update along the suffix links from bottom to top, propagating the information about the longest matched substring from children to parents. Here, note that the longest matching length recorded at a parent must not exceed its own $\operatorname{len}$ value. This gives, for every state of the SAM of $S_1$, the length of the longest substring of $S_j$ it **can actually match**.
    
    Finally, it suffices to match each of $S_2,\cdots,S_k$ once and take the minimum of the actually matched lengths recorded at every state of the SAM; this gives the length of the longest common substring of $S_2,\cdots,S_k$ that every state of the SAM can actually match. Then traverse all states of the SAM, and the maximum is the length of the longest common substring of these $k$ strings.
    
    The time complexity of the algorithm is $O(\sum_i |S_i|)$. Although the SAM of the string $S_1$ is traversed $k$ times, since $|S_1|$ is the smallest, $k|S_1|\le \sum_i |S_i|$, so the main term of the complexity is still traversing all strings during the matching.

Example problem: [SPOJ Longest Common Substring II](https://www.spoj.com/problems/LCS2/)

## Exercises

-   [[Template] Suffix automaton](https://www.luogu.com.cn/problem/P3804)
-   [SDOI2016 Generating spells (生成魔咒)](https://loj.ac/problem/2033)
-   [SPOJ - SUBLEX](https://www.spoj.com/problems/SUBLEX/)
-   [TJOI2015 String theory (弦论)](https://loj.ac/problem/2102)
-   [SPOJ Longest Common Substring](https://www.spoj.com/problems/LCS/en/)
-   [SPOJ Longest Common Substring II](https://www.spoj.com/problems/LCS2/)
-   [Codeforces 1037H Security](https://codeforces.com/problemset/problem/1037/H)
-   [Codeforces 666E Forensic Examination](https://codeforces.com/problemset/problem/666/E)
-   [HDU4416 Good Article Good sentence](https://acm.hdu.edu.cn/showproblem.php?pid=4416)
-   [HDU4436 str2int](https://acm.hdu.edu.cn/showproblem.php?pid=4436)
-   [HDU6583 Typewriter](https://acm.hdu.edu.cn/showproblem.php?pid=6583)
-   [Codeforces 235C Cyclical Quest](https://codeforces.com/problemset/problem/235/C)
-   [CTSC2012 Familiar article (熟悉的文章)](https://www.luogu.com.cn/problem/P4022)
-   [NOI2018 Your name (你的名字)](https://uoj.ac/problem/395)

## References

We first list some of the original literature related to the SAM:

-   A. Blumer, J. Blumer, A. Ehrenfeucht, D. Haussler, R. McConnell. Linear Size Finite Automata for the Set of All Subwords of a Word. An Outline of Results. \[1983]
-   A. Blumer, J. Blumer, A. Ehrenfeucht, D. Haussler. The Smallest Automaton Recognizing the Subwords of a Text. \[1984]
-   Maxime Crochemore. Optimal Factor Transducers. \[1985]
-   Maxime Crochemore. Transducers and Repetitions. \[1986]
-   A. Nerode. Linear automaton transformations. \[1958]

In addition, the topic can be found in some more recent resources and in many books on string algorithms:

-   Maxime Crochemore, Wojciech Rytter. Jewels of Stringology. \[2002]
-   Bill Smyth. Computing Patterns in Strings. \[2003]
-   Bill Smyth. Методы и алгоритмы вычислений на строках (Russian translation of the previous book). \[2006]

Some further materials:

-   "Suffix automaton" (《后缀自动机》), Chen Lijie.
-   "Extending the suffix automaton to the trie" (《后缀自动机在字典树上的拓展》), Liu Yanyi.
-   "The suffix automaton and its applications" (《后缀自动机及其应用》), Zhang Tianyang.
-   <https://www.cnblogs.com/zinthos/p/3899679.html>
-   <https://codeforces.com/blog/entry/20861>
-   <https://zhuanlan.zhihu.com/p/25948077>

**This page is mainly translated from the blog post [Суффиксный автомат](http://e-maxx.ru/algo/suffix_automata) and its English translation [Suffix Automaton](https://cp-algorithms.com/string/suffix-automaton.html). The Russian version is licensed under Public Domain + Leave a Link; the English version is licensed under CC-BY-SA 4.0.**

[^state-endpos]: The reason every state must be taken as one $\operatorname{endpos}$ equivalence class is actually the Myhill–Nerode theorem mentioned in the next paragraph. Briefly, if two strings $t$ and $u$ have different $\operatorname{endpos}$ sets, they cannot correspond to the same state of the SAM: the paths from the same state to terminal states are always the same, which means that the ways of appending characters to $t$ and $u$ to reach the end of $s$ are also the same, and this exactly says that $t$ and $u$ have the same end positions in the string $s$. Conversely, as long as two strings $t$ and $u$ have the same $\operatorname{endpos}$ sets, they can be mapped to the same state of the SAM. That this is feasible is the content of the proof of the Myhill–Nerode theorem, which we will not discuss further here. However, from this discussion one can at least believe that the SAM obtained by putting strings with the same $\operatorname{endpos}$ sets into the same state is necessarily minimal, because further merging of nodes is impossible.

[^time-complexity]: If no additional list is used to record the available transitions of the current state, and only an array storing all possible transitions (whether they exist or not) is used and copied directly when cloning a node, then the time complexity is also $O(n\left|\Sigma\right|)$.

[^monotone-loc]: What the main text does not explain is whether the position of $\operatorname{longest}(\operatorname{link}(\operatorname{link}(\textit{last})))$ is also monotonically (weakly) increasing in cases 1 and 2. Case 1 is easy to verify, because after the update $\operatorname{link}(\textit{last})=t_0$, and $\operatorname{link}(\operatorname{link}(\textit{last}))$ is the virtual state $-1$; we may regard its corresponding string as the empty string located at the end of the current string, whose position takes the maximum value. In case 2, the transition is continuous, which means $\operatorname{longest}(q) = \operatorname{longest}(p)+c$. However, appending a new character to the end of a substring only makes it harder for that substring to occur in the string; that is, when the set of end positions of the suffix of $\operatorname{longest}(p)$ of length $\operatorname{len}(\operatorname{link}(p))$ strictly contains $\operatorname{endpos}(p)$, the set of end positions of the suffix of $\operatorname{longest}(q)$ of length $\operatorname{len}(\operatorname{link}(p))+1$ may still be the same as $\operatorname{endpos}(q)$. Hence $\operatorname{len}(\operatorname{link}(q))\le\operatorname{len}(\operatorname{link}(p))+1$, i.e. the starting position of $\operatorname{longest}(\operatorname{link}(p))$ as a suffix of $s$ is necessarily not greater than the starting position of $\operatorname{longest}(\operatorname{link}(q))$ as a suffix of $s+c$. And when the state $p$ with a transition on $c$ is found for the first time, at least one move must have been made, which shows that the starting position of $\operatorname{longest}(\operatorname{link}(p))$ as a suffix of $s$ is not less than the starting position of $\operatorname{longest}(\operatorname{link}(\operatorname{link}(\textit{last})))$ as a suffix of $s$. Finally, $\operatorname{longest}(\operatorname{link}(q))=\operatorname{longest}(\operatorname{link}(\operatorname{link}(\textit{cur})))$. This shows that in case 2 the position of $\operatorname{longest}(\operatorname{link}(\operatorname{link}(\textit{last})))$ is also monotonically (weakly) increasing.
