---
title: Palindromic tree
---

## Definition

A palindromic tree (EER Tree, also called a palindromic automaton) is an efficient data structure for storing all palindromic substrings of a string. It was first published by Mikhail Rubinchik and Arseny M. Shur in 2015. Inspired by suffix-based string data structures such as suffix trees, it provides simple, efficient solutions to a range of problems involving palindromes.

## Structure

A palindromic tree looks roughly like this:

![](./images/pam1.png)

Like other automata, a palindromic tree consists of transition edges and suffix links (fail pointers), and each node can represent a palindromic substring.

Palindromes can have odd or even lengths. As in Manacher's algorithm, we could insert a character outside the alphabet, such as '#', as a separator to make all palindrome lengths odd, but that is cumbersome. Is there a better way?

Of course there is. Build two trees: the nodes of one represent odd-length palindromic substrings, and the nodes of the other represent even-length palindromic substrings.

As in other automata, a node's fail pointer points to the node representing the longest palindromic suffix of its palindrome. A transition edge, however, does not append a character only at the end: it adds the same character to both ends of the original palindrome (which is natural, since the stored string must remain a palindrome).

At each node, also maintain the length len of its palindromic substring. This information makes the palindromic tree easy to construct.

## Construction

A palindromic tree has two initial states, representing palindromes of lengths $-1,0$, called the odd root and the even root. They do not represent actual strings and exist only as initial states, much like root nodes in other automata.

The even root's fail pointer points to the odd root. We do not care about the odd root's fail pointer because the odd root cannot fail to match (its next transition leads to a state of length $1$, a single character, which is always a palindromic substring).

As with a suffix automaton, we construct the palindromic tree incrementally.

Suppose the tree for the first $p-1$ characters has been built, and we now add the character at position $p$ of the original string.

Start at the node for the longest palindromic substring ending at the previous character. Repeatedly follow fail pointers until reaching a node satisfying $s_{p}=s_{p-len-1}$, meaning that the character preceding its palindrome equals the character being added.

Here is the figure from the paper:

![](./images/pam2.png)

Following fail pointers finds the node for A. Adding `X` at both ends gives the current palindrome, `XAX`. Clearly, this is the tree node for the longest palindromic substring ending at $p$. (This is where the node of length $-1$ helps: if no `X` matches, the condition becomes $s_p=s_p$ at the same position, naturally giving the node for the character `X`.) If this node does not exist, create it.

Next, compute the new node's fail pointer. The procedure is similar: starting from `A`, follow fail pointers to find `XBX`, the longest palindromic suffix of `XAX`, and make the fail pointer point to its node.

This node does not need to be created. The first $len_B$ and last $len_B$ characters of `A` are equal, both forming `B`. By the palindrome's symmetry, the first $len_B$ characters are surrounded by `X` on both sides; the trailing character is fixed to be `X`. Thus the node `XBX` must already be present.

If no fail match is found, link to the node of length $0$. This is valid because it is a suffix of every node.

## Proof of a linear number of states

### Theorem

A string $s$ has at most $|s|$ distinct palindromic substrings.

### Proof

Use mathematical induction.

-   If $|s| =1$, $s$ has one character and only one substring, which is a palindrome. Thus the claim holds.

-   If $|s| >1$, let $t=sc$, where $t$ is obtained from $s$ by appending a character $c$, and assume the claim holds for $s$. Consider the palindromic substrings ending at the last character $c$, with left endpoints sorted increasingly as $l_1,l_2,\dots,l_k$. Since $t[l_1..|t|]$ is a palindrome, for every position $l_1 \le p \le |t|$, $t[p..|t|]=t[l_1..l_1+|t|-p]$. Thus, for $1 < i \le k$, $t[l_i..|t|]$ already occurs in $t[1..|t|-1]$. Appending one character therefore increases the number of distinct palindromic substrings by at most $1$.

The theorem follows by mathematical induction.

Thus a palindromic tree has $O(|s|)$ states. Each state represents exactly one distinct palindromic substring, so the state from which its transition comes is unique. Therefore the total number of transitions is also $O(|s|)$.

## Correctness proof

In the figure above, add the current character `X`. By the proof of the linear state count, we only need to find the longest palindromic suffix containing the last `X`, namely `XAX`. Then find its longest palindromic suffix `XBX` and create the suffix link. The state for `XBX` already exists in the tree. The palindromic suffixes containing the last character are `XAX`, `XBX` itself, and all ancestors of its state in the fail tree.

For the construction of the palindromic tree of $s$, let $n=|s|$. Clearly, all operations other than following fail pointers take $O(n)$ time.

When adding a character, each fail jump changes the depth of the current node in the fail tree by $-1$, relative to the previous step. Connecting a fail link increases the depth by only 1 (except when fail is $0$, meaning a match is found only at $-1$: then, relative to $-1$, the depth increases by $+2$).

Since only $n$ characters are added, the depth increases only $n$ times, so there are at most $2n$ fail jumps.

Therefore constructing the palindromic tree of $s$ takes $O(|s|)$ time.

## Applications

### Number of distinct palindromic substrings

The proof of the linear state count shows that the number of distinct palindromic substrings of a string equals the number of states in its palindromic tree, excluding the odd and even roots.

### Occurrence counts of palindromic substrings

Build the palindromic tree and count occurrences in a way similar to a suffix automaton.

During construction, nodes are already inserted in topological order. It therefore suffices to iterate over all states in reverse order and add each state's occurrence count to that of the state pointed to by its fail pointer.

Example: [APIO2014: Palindromes](https://www.luogu.com.cn/problem/P3649)

Define the value of a substring of $s$ as its number of occurrences in $s$ multiplied by its length. For a given string $s$, find the maximum value among all palindromic substrings.

??? note "Reference code"
    ```cpp
    --8<-- "docs/string/code/pam/pam_1.cpp"
    ```

### Minimum palindromic factorization

> Given a string $s(1\le |s| \le 10^5)$, find the minimum $k$ such that there exist strings $s_1,s_2,\dots,s_k$, each $s_i(1\le i \le k)$ is a palindrome, and concatenating $s_1,s_2, \dots ,s_k$ in order produces $s$.

Consider dynamic programming. Let $dp[i]$ be the minimum number of parts in a factorization of the prefix of $s$ of length $i$. For the transition, enumerate all palindromes ending at the $i$-th character:

$$
dp[i]=1+\min_{ s[j+1..i] \text{ is a palindrome} } dp[j]
$$

A string may have $O(n^2)$ palindromic substrings, so this algorithm takes $O(n^2)$ time, which is unacceptable. To optimize the transitions, we establish the following lemmas.

For a string $s$, denote its prefix of length $i$ by $pre(s,i)$ and its suffix of length $i$ by $suf(s,i)$.

Period: if $0< p \le |s|$ and $\forall 1 \le i \le |s|-p,s[i]=s[i+p]$, then $p$ is called a period of $s$.

Border: if $0 \le r < |s|$ and $pre(s,r)=suf(s,r)$, then $pre(s,r)$ is called a border of $s$.

Relationship between periods and borders: $t$ is a border of $s$ if and only if $|s|-|t|$ is a period of $s$.

???+ note "Proof"
    If $t$ is a border of $s$, then $pre(s,|t|)=suf(s,|t|)$, so $\forall 1\le i \le |t|, s[i]=s[|s|-|t|+i]$. Hence $|s|-|t|$ is a period of $s$.
    
    If $|s|-|t|$ is a period of $s$, then $\forall 1 \le i \le |s|-(|s|-|t|)=|t|,s[i]=s[|s|-|t|+i]$. Thus $pre(s,|t|)=suf(s,|t|)$, so $t$ is a border of $s$.

#### Lemma 1

Let $t$ be a suffix of a palindrome $s$. Then $t$ is a border of $s$ if and only if $t$ is a palindrome.

???+ note "Proof"
    For $1 \le i \le |t|$, since $s$ and $t$ are palindromes, $s[i]=s[|s|-i+1]=s[|s|-|t|+i]$. Hence $t$ is a border of $s$.
    
    For $1 \le i \le |t|$, since $t$ is a border of $s$, $s[i]=s[|s|-|t|+i]$. Since $s$ is a palindrome, $s[i]=s[|s|-i+1]$. Thus $s[|s|-i+1]=s[|s|-|t|+i]$, so $t$ is a palindrome.

In the figure below, positions of the same color contain equal characters.

![](./images/pam3.png)

#### Lemma 2

Let $t$ be a border of $s$ with $|s|\le 2|t|$. Then $s$ is a palindrome if and only if $t$ is a palindrome.

???+ note "Proof"
    If $s$ is a palindrome, Lemma $1$ implies that $t$ is also a palindrome.
    
    If $t$ is a palindrome, since $t$ is a border of $s$, $\forall 1 \le i \le |t|, s[i]=s[|s|-|t|+i]=s[|s|-i+1]$. Since $|s| \le 2|t|$, $s$ is also a palindrome.

#### Lemma 3

If $t$ is a border of a palindrome $s$, then $|s|-|t|$ is a period of $s$. Moreover, $|s|-|t|$ is the minimum period of $s$ if and only if $t$ is the longest proper palindromic suffix of $s$.

#### Lemma 4

Let $x$ be a palindrome, $y$ the longest proper palindromic suffix of $x$, and $z$ the longest proper palindromic suffix of $y$. Let $u,v$ be strings satisfying $x=uy,y=vz$. Then the following three properties hold:

1.  $|u| \ge |v|$;

2.  If $|u| > |v|$, then $|u| > |z|$;

3.  If $|u| = |v|$, then $u=v$.

![](./images/pam4.png)

???+ note "Proof"
    1.  By Lemma $3$, $|u|=|x|-|y|$ is the minimum period of $x$, and $|v|=|y|-|z|$ is the minimum period of $y$. Suppose, for a contradiction, that $|u| < |v|$. Since $y$ is a suffix of $x$, $u$ is a period of both $x$ and $y$, contradicting that $|v|$ is the minimum period of $y$. Therefore $|u| \ge |v|$.
    2.  Since $y$ is a border of $x$, $v$ is a prefix of $x$. Let $w$ satisfy $x=vw$ (as shown below), where $z$ is a border of $w$. Suppose, for a contradiction, that $|u| \le |z|$. Then $|zu| \le 2|z|$, so by Lemma $2$, $w$ is a palindrome. By Lemma $1$, $w$ is a border of $x$. Since $|u| > |v|$, we have $|w| > |y|$, a contradiction. Therefore $|u| > |z|$.
    3.  Both $u,v$ are prefixes of $x$, and $|u|=|v|$, so $u=v$.
    
    ![](./images/pam5.png)

#### Corollary

After sorting all palindromic suffixes of $s$ by length, their lengths can be partitioned into $\log |s|$ arithmetic progressions.

???+ note "Proof"
    Let the lengths of all palindromic suffixes of $s$, sorted increasingly, be $l_1,l_2,\dots,l_k$. For any $2 \le i \le k-1$, if $l_{i}-l_{i-1}=l_{i+1}-l_{i}$, then $l_{i-1},l_{i},l_{i+1}$ form an arithmetic progression. Otherwise, $l_{i}-l_{i-1}\neq l_{i+1}-l_{i}$. By Lemma $4$, $l_{i+1}-l_{i}>l_{i}-l_{i-1}$ and $l_{i+1}-l_{i}>l_{i-1}$, so $l_{i+1}>2l_{i-1}$. Thus, whenever the length differences of two adjacent pairs change, the largest length is more than twice the smallest. Doubling can occur only $O(\log |s|)$ times, so the palindromic suffix lengths of $s$ can be partitioned into $\log |s|$ arithmetic progressions.

This corollary can also be proved with the weak periodicity lemma: classify all borders of the longest palindromic suffix of $s$ by length $x$, with $x \in [2^0,2^1),[2^1,2^2),\dots,[2^k,n)$, and consider the longest border in each of these $\log |s|$ groups. For detailed proofs, see Jin Ce's "Selected topics in string algorithms" and Chen Sunli's 2019 IOI national candidate team paper "Algorithms for substring period queries and their applications".

With this result, we can now optimize the $dp$ transitions.

#### Optimization

At each node $u$ of the palindromic tree, maintain two additional values, $diff[u]$ and $slink[u]$. The value $diff[u]$ is the difference between the lengths of the palindromes represented by $u$ and $fail[u]$, namely $len[u]-len[fail[u]]$. The value $slink[u]$ is obtained by following fail pointers upward from $u$ to the first node $v$ such that $diff[v] \neq diff[u]$, that is, the shortest node in the arithmetic progression containing $u$.

By the result proved above, following $slink$ pointers upward requires only $O(\log |s|)$ jumps for each appended character. Thus we can store the sum of the $dp$ values of all palindromes represented by an arithmetic progression (a $\min$ in the original problem) at the node of its longest palindrome.

Let $g[v]$ denote, for the arithmetic progression containing $v$, the sum of its $dp$ values, where $v$ is its longest node. Then $g[v]=\sum_{slink[x]=slink[v]} dp[i-len[x]]$, where $i$ is the current index.

Now consider how to update the arrays $g$ and $dp$. In the figure below, suppose we are processing character $i$, corresponding to node $x$ in the palindromic tree. The value $g[x]$ is the sum of the $dp$ values at the three orange positions (the shortest palindrome $slink[x]$ belongs to the next arithmetic progression). The previous occurrence of $fail[x]$ is at $i-diff[x]$ (ending at $i-diff[x]$), and $g[fail[x]]$ contains the $dp$ values at the blue positions. Thus $g[x]$ equals $g[fail[x]]$ plus the $dp$ value at one extra position, $i-(len[slink[x]]+diff[x])$. Finally use $g[x]$ to update $dp[i]$, completing the contribution of this arithmetic progression. Keep jumping to $slink[x]$ and repeat. See the example code for the implementation.

![](./images/pam6.png)

Finally, correctness relies on this fact: if $x$ and $fail[x]$ belong to the same arithmetic progression, the previous occurrence of $fail[x]$ is at $i-diff[x]$.

???+ note "Proof"
    By Lemma $1$, $fail[x]$ is a border of $x$, so it occurs at $i-diff[x]$.
    
    Suppose $fail[x]$ occurs in $(i-diff[x],i)$ at position $j$. Since $x$ and $fail[x]$ belong to the same arithmetic progression, $2|fail[x]| \ge x$. The extra occurrence of $fail[x]$ overlaps the occurrence at $i-diff[x]$ of $fail[x]$. Denote their overlap by $w$, and let $u$ satisfy $uw=fail[x]$. As in Lemma $1$, we can prove that $w$ is a palindrome and that the prefix of $x$, namely $s[i-len[x]+1..j]=uwu$, is also a palindrome. This contradicts that $fail[x]$ is the longest palindromic prefix (suffix) of $x$.

Example: [Codeforces 932G Palindrome Partition](https://codeforces.com/problemset/problem/932/G)

Given a string $s$, partition $s$ into $t_1, t_2, \dots, t_k$, where $k$ is even and $t_i=t_{k-i+1}$. Count the number of such partitions.

??? note "Solution"
    Construct $t= s[0]s[n - 1]s[1]s[n - 2]s[2]s[n - 3] \dots s[n / 2 - 1]s[n / 2]$. The problem is equivalent to counting factorizations of $t$ into even-length palindromes. Change the transitions above to sums and update the $dp$ array only at even positions. The time complexity is $O(n \log n)$ and the space complexity is $O(n)$.

??? note "Reference code"
    ```cpp
    --8<-- "docs/string/code/pam/pam_2.cpp"
    ```

## Example problems

-   [Longest double palindrome](https://www.luogu.com.cn/problem/P4555)

-   [Cheerleading rehearsal](https://www.luogu.com.cn/problem/P1659)

-   [SHOI2011: Double palindrome](https://www.luogu.com.cn/problem/P4287)

-   [HDU 5421 Victor and String](https://acm.hdu.edu.cn/showproblem.php?pid=5421)

-   [CodeChef Palindromeness](https://www.codechef.com/LTIME23/problems/PALPROB)

## Related resources

-   [EERTREE: An Efficient Data Structure for Processing Palindromes in Strings](https://arxiv.org/pdf/1506.04862)

-   [Palindromic tree](http://adilet.org/blog/palindromic-tree/)

-   Weng Wentao, "Palindromic trees and their applications", 2017 IOI national candidate team papers.

-   Chen Sunli, "Algorithms for substring period queries and their applications", 2019 IOI national candidate team papers.

-   Jin Ce, "Selected topics in string algorithms".

-   [A bit more about palindromes](https://codeforces.com/blog/entry/19193)

-   [A Subquadratic Algorithm for Minimum Palindromic Factorization](https://arxiv.org/pdf/1403.2431.pdf)
