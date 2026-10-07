---
title: Suffix tree
---

A suffix tree is a data structure that maintains all suffixes of a string.

## Notation

Let $S$ be the string for which we build the suffix tree, of length $n$ and over the alphabet $\Sigma$.

Let $S[i]$ denote the character of $S$ at position $i$, where $1 \le i \le n$.

Let $S [l, r]$ denote the string formed from $S$ by taking characters $l$ through $r$, called a substring of $S$.

Denote by $S [i, n]$ the suffix of $S$ starting at $i$, and by $S [1, i]$ the prefix of $S$ ending at $i$.

## Definition

The **suffix trie** of a string $S$ is the trie obtained by inserting all suffixes of S. In a suffix trie, the string corresponding to node x is the concatenation of the characters along the path from the root to x. We call
all nodes in the suffix trie corresponding to a suffix of $S$ suffix nodes.

A useful property of the suffix trie is easy to see: its non-root nodes accept exactly all distinct nonempty substrings of $S$. However, constructing it takes $O(n^2)$ time and space, which is often unacceptable. This motivates the suffix tree.

Mark as key nodes all nodes of the suffix trie with more than one child, together with all suffix nodes. The compressed trie that keeps only these key nodes, compressing each chain of non-key nodes into a single edge, is the **suffix tree**. If instead only nodes with more than one child and leaf nodes are marked as key nodes, the compressed trie keeping only those key nodes is the **implicit suffix tree**. Clearly, an implicit suffix tree is a further compression of a suffix tree.

In both a suffix tree and an implicit suffix tree, each edge corresponds to a string. Each non-root node $x$ corresponds to a set of strings formed by concatenating the strings along the path from the root to the parent of $x$, denoted by $fa_x$, with any nonempty prefix of the string on the edge from $fa_x$ to $x$. Denote this set by $str_x$. In an implicit suffix tree, a suffix that does not correspond to any node is called an **implicit suffix**.

From left to right, the figure below shows the suffix trie, suffix tree, and implicit suffix tree built for the string $\texttt{cabab}$.

![suffix-tree\_cabab1.png](./images/suffix-tree1.png)

Consider inserting the suffixes of $S$ into the suffix trie one by one. Starting with the second insertion, each insertion adds at most one node with more than one child and one suffix node. Thus the suffix tree has at most $2n$ nodes, which is an excellent bound.

## Building a suffix tree

### Supporting dynamic character insertion at the front

The parent tree of a suffix automaton (SAM) built for the reversed string is the suffix tree of the original string. Thus we can simply add the characters of the reversed string to the SAM one at a time.

???+ note "Reference implementation"
    ```cpp
    struct SuffixAutomaton {
      int tot, lst;
      int siz[N << 1];
      int buc[N], id[N << 1];
    
      struct Node {
        int len, link;
        int ch[26];
      } st[N << 1];
    
      SuffixAutomaton() : tot(1), lst(1) {}
    
      void extend(int ch) {
        int cur = ++tot, p = lst;
        lst = cur;
        siz[cur] = 1, st[cur].len = st[p].len + 1;
        for (; p && !st[p].ch[ch]; p = st[p].link) st[p].ch[ch] = cur;
        if (!p)
          st[cur].link = 1;
        else {
          int q = st[p].ch[ch];
          if (st[q].len == st[p].len + 1)
            st[cur].link = q;
          else {
            int pp = ++tot;
            st[pp] = st[q];
            st[pp].len = st[p].len + 1;
            st[cur].link = st[q].link = pp;
            for (; p && st[p].ch[ch] == q; p = st[p].link) st[p].ch[ch] = pp;
          }
        }
      }
    } SAM;
    ```

### Supporting dynamic character insertion at the back

Ukkonen's algorithm is an incremental construction algorithm. We insert the characters of $S$ into the tree in order, maintaining the correct suffix tree after each insertion.

#### Naive algorithm

We first introduce a brute-force construction, using the string $\texttt {abbbc}$ to illustrate the process.

Initially create a root, node $0$. For every edge, maintain an interval $[l,r]$ indicating that its string is $S[l,r]$. Also maintain the number $m$ of characters inserted so far, initially $0$.

First insert the character $\texttt a$: add an edge directly from node $0$ to a new node, labeled $[1,\infty]$. Here $\infty$ is a very large value representing the end of the string, so this edge automatically includes newly inserted characters.

![suffix-tree\_a.webp](./images/suffix-tree2.webp)

Next insert $\texttt b$, again adding an edge from $0$, labeled $[2,\infty⁡]$. The meaning of the existing edge $[1,\infty]$ changes automatically: as the end of the string moves, its string changes from $\texttt a$ to $\texttt {ab}$. This is correct because every previous suffix already appears as a leaf in the tree; all we need is to append the current character to every leaf.

![suffix-tree\_ab.webp](./images/suffix-tree3.webp)

Now insert another $\texttt b$. But $\texttt b$ is already a substring of the string inserted so far, so the tree already contains $\texttt b$. Do nothing, and record $k$ such that $S[k,m]$ is the current longest implicit suffix.

![suffix-tree\_abb.webp](./images/suffix-tree4.webp)

Next insert yet another $\texttt b$. Since the previous $\texttt b$ was not explicitly inserted, $k=3$, so the suffix to insert is $\texttt {bb}$. Searching down from the root for $\texttt {bb}$ shows that it too is already in the tree. Again, do nothing.

![suffix-tree\_abbb.webp](./images/suffix-tree5.webp)

Notice that we have ignored suffixes starting after $k$. If $S[k,m]$ is an implicit suffix, then for $l>k$, $S[l,m]$ is also implicit. Indeed, since $S[k,m]$ is implicit, there is a character $c$ such that $S[k, m] + c$ is a substring of $S$. Then $S [ l, m] + c$ is also a substring of $S$, so by the definition of an implicit suffix tree, $S[ l, m]$ does not appear as a leaf either.

Next insert $\texttt c$. Since $k=3$, search down from the root for $\texttt {bbc}$, which is not in the tree. We need to extend the node representing $\texttt {bb}$ with an outgoing edge $[5,\infty]$. However, that node does not actually exist: its position is inside an edge. Split the edge to create a new node, and add the required outgoing edge there. The insertion succeeds, so set $k\to k+1$, since $S[k,m]$ is no longer implicit.

![suffix-tree\_abbbc1.webp](./images/suffix-tree6.webp)

Since $k$ has changed, repeat this process until another implicit suffix appears or $k>m$ (the latter happens in this example).

![suffix-tree\_abbbc2.webp](./images/suffix-tree7.webp)

The construction is complete.

Each brute-force search and insertion from the root takes $O(n)$ time in the worst case, so the total complexity is $O(n^2)$.

#### Suffix links

The naive algorithm is slow mainly because each extend operation searches from the root for the insertion position of the longest implicit suffix. Instead, store this position. Use a pair $(now,rem)$ to describe the current longest implicitly represented suffix $S[k,m]$. Starting at node $now$, taking its outgoing edge beginning with $S[m-rem+1]$, and walking a distance $rem$ reaches a position that uniquely represents a string. When inserting a new character, we only need to search from the position described by $now$ and $rem$.

Now, when $k\to k + 1$, we only need to update $(now,rem)$. If $now=0$, simply set $rem \to rem-1$, since the next suffix has the length of the one just inserted plus $-1$. Otherwise, denote the substring corresponding to $str_{now}$ by $S[l,r]$. Find the node $now'$ corresponding to $S[l+1,r]$ and set $now\to now'$.

First, a lemma: for every non-leaf, non-root node $x$ in an implicit suffix tree, there is another non-leaf node $y$ such that $str_y$ is obtained by deleting the first character of the substring corresponding to $str_x$.

Proof. Let $s$ be the string obtained by deleting the first character of $str_x$. By the definition of an implicit suffix tree, there are two distinct characters $c_1,c_2$ such that both $str_x + c1$ and $str_x + c_2$ are substrings of $S$. Therefore $s + c_1$ and $s + c_2$ are also substrings of $S$, so $s$ also corresponds to a branching key node in the suffix trie. Hence there is a node $y$ in the implicit suffix trie such that $str_y=s$. This proves the lemma.

Using this lemma, define $\operatorname{Link}(x)=y$, called the **suffix link** of x. Thus $now'=\operatorname{Link}(now)$ always exists. It remains to compute $\operatorname{Link}$ for every non-root, non-leaf node of the implicit suffix tree.

#### Ukkonen's algorithm

The overall procedure of Ukkonen's algorithm is as follows:

To build the implicit suffix tree, add the characters of $S$ from left to right. Suppose the root is $0$, the implicit suffix tree of $S[1, m]$ has already been built, and its suffix links have been maintained. The longest implicit suffix of $S [1, m]$ is $S [k, m]$, at position $(now, rem)$ in the tree. Let $S [m + 1] = x$; we now need to add character $x$. Every suffix of $S [1, m]$ must have $x$ appended. All explicit suffixes correspond to leaves, whose incoming edges have right endpoint $\infty$, so they need no maintenance. We only need to consider how appending x to implicit suffixes changes the tree. Start with $S [k, m]$. There are two cases:

1.  At $(now, rem)$, a transition on $x$ already exists. The shape of the suffix tree does not change. Since $S [k, m+1]$ already appears in the suffix tree, for $l > k$, $S [ l, m + 1]$ also appears. Simply set $rem\to rem + 1$; no other change is needed.
2.  At $(now, rem)$, no transition on $x$ exists. If $(now, rem)$ is a node of the tree, add an outgoing edge $x$ there; otherwise split at this position to create a new node and add an outgoing edge $x$ to it. For $l > k$, we do not yet know how $S [ l, m]$ affects the shape of the suffix tree, so we must continue with $S [k + 1, m]$. To find the position of $S [k + 1, m]$ in the tree, if $now$ is not $0$, follow the suffix link by setting $now = \operatorname{Link}(now)$; otherwise set $rem\to rem − 1$. Finally set $k\to k + 1$ and repeat.

Each step takes constant time, and the algorithm stops after all characters have been inserted, so its time complexity is $O(n)$.

Ukkonen's algorithm only constructs the implicit suffix tree of $S$, which can be less useful than a suffix tree for some problems. When needed, append to $S$ a character that has never appeared before. All suffixes of S then correspond one-to-one with the leaves of the tree.

???+ note "Reference implementation"
    ```cpp
    struct SuffixTree {
      int ch[M + 5][RNG + 1], st[M + 5], len[M + 5], link[M + 5];
      int s[N + 5];
      int now{1}, rem{0}, n{0}, tot{1};
    
      SuffixTree() { len[0] = inf; }
    
      int new_node(int s, int le) {
        ++tot;
        st[tot] = s;
        len[tot] = le;
        return tot;
      }
    
      void extend(int x) {
        s[++n] = x;
        ++rem;
        for (int lst{1}; rem;) {
          while (rem > len[ch[now][s[n - rem + 1]]])
            rem -= len[now = ch[now][s[n - rem + 1]]];
          int &v{ch[now][s[n - rem + 1]]}, c{s[st[v] + rem - 1]};
          if (!v || x == c) {
            lst = link[lst] = now;
            if (!v)
              v = new_node(n, inf);
            else
              break;
          } else {
            int u{new_node(st[v], rem - 1)};
            ch[u][c] = v;
            ch[u][x] = new_node(n, inf);
            st[v] += rem - 1;
            len[v] -= rem - 1;
            lst = link[lst] = v = u;
          }
          if (now == 1)
            --rem;
          else
            now = link[now];
        }
      }
    } Tree;
    ```

## Uses

The path between any node and the root of a suffix tree represents a nonempty substring of $S$, which is useful in many string problems.

The DFS order of a suffix tree is the suffix array. Each subtree therefore corresponds to an interval in the suffix array. The longest common prefix of two suffixes is the LCA of their corresponding leaves. Thus the property of the suffix array's height array can be understood as follows: the LCA of a set of tree nodes is the LCA of the nodes with the smallest and largest DFS indices.

## Example problems

### [Luogu P3804: Suffix automaton (SAM) template](https://www.luogu.com.cn/problem/P3804)

Problem statement:

Given a string $S$ consisting only of lowercase letters.

Among all substrings of $S$ whose number of occurrences is not $1$, find the maximum product of the number of occurrences and the substring length.

??? note "Solution"
    Build the implicit suffix tree after inserting a terminator. Every path starting at the root forms a substring. The number of occurrences of an explicit suffix is the number of leaves in the corresponding node's subtree. Implicit suffixes need not be considered: each has the same occurrence count as the explicit suffix corresponding to the first node reached below it, but is necessarily shorter. Traverse the entire tree and compute the number of leaves in each node's subtree and the length of its path to the root. If the number of leaves is $>1$, update the answer. The complexity is $O(|S||\Sigma|)$.

??? note "Reference code"
    ```cpp
    --8<-- "docs/string/code/suffix-tree/suffix-tree_1.cpp"
    ```

### [CF235C Cyclical Quest](https://codeforces.com/problemset/problem/235/C)

Problem statement: given a main string $S$ of lowercase letters and $n$ query strings, for each query string $x_i$ find the total number of occurrences of all its cyclic shifts in the main string.

??? note "Solution"
    Build the implicit suffix tree after inserting a terminator.
    
    Enumerate the current cyclic shift, recording how long a prefix can be found in the tree.
    
    Repeat a process similar to Ukkonen's algorithm, keeping the current matched position $(now,rem)$. Try to insert the next character each time; continue if successful, otherwise break out of the loop.
    
    If the entire current cyclic shift is matched and has not appeared before, update the answer.
    
    When moving to the next cyclic shift, delete the first character of the currently matched substring. This is exactly equivalent to setting $now \to \operatorname{Link}(now)$. If $now=1$, simply set $rem\to rem-1$ instead.
    
    The complexity is $O(|S||\Sigma|+\sum|x_i|)$.

??? note "Reference code"
    ```cpp
    --8<-- "docs/string/code/suffix-tree/suffix-tree_2.cpp"
    ```

## References

1.  Dai Chenxin, "Construction of suffix trees", 2021 national training team paper.
2.  [Cool suffix tree magic - EternalAlexander's blog](https://www.luogu.com.cn/blog/EternalAlexander/xuan-ku-hou-zhui-shu-mo-shu)
