---
title: Aho–Corasick automaton
---

## Overview

The AC (Aho–Corasick) automaton is an automaton built **on the structure of a trie** combined with **the idea of KMP**, used to solve tasks such as multi-pattern matching.

The AC automaton is essentially an automaton on a trie.

Before reading this article, please read [KMP](./kmp.md) and [Trie](./trie.md).

## Explanation

Simply put, building an AC automaton takes two steps:

1.  the basic trie structure: build a trie from all the patterns;
2.  the idea of KMP: build fail pointers for all nodes of the trie.

Once it is built, we can use it for multi-pattern matching.

## Building the trie

Initially the AC automaton inserts several patterns into a trie, and then builds the AC automaton on that trie. This trie is an ordinary trie, built by the usual trie construction method.

Note that a node of the trie represents a prefix of some pattern. Below we also call it a state. One node represents one state, and the edges of the trie are the state transitions.

Formally, for patterns $s_1,s_2,\cdots,s_n$, denote by $Q$ the set of all states after building a trie from them.

## Fail pointers

The AC automaton uses a fail pointer to assist in matching multiple patterns.

The fail pointer of a state $u$ points to another state $v$, where $v\in Q$ and $v$ is the longest suffix of $u$ (i.e. among all states that are suffixes, we take the longest one as the fail pointer).

Comparing the fail pointer with the next pointer in [KMP](./kmp.md):

1.  Similarity: both are pointers used to jump on a mismatch.
2.  Difference: the next pointer gives the longest border (i.e. the longest equal prefix and suffix), while the fail pointer points to the longest suffix of the current state among the prefixes of all patterns.

This is because KMP matches only one pattern, while the AC automaton matches multiple patterns. The node pointed to by the fail pointer may belong to a different pattern, with a different prefix.

In summary, the fail pointer of the AC automaton points to the state that is the longest suffix of the current state.

Note: when the AC automaton matches, multiple patterns can be matched at the same position.

### Building the pointers

Below we introduce the **basic idea** of building fail pointers:

To build fail pointers, we can refer to the idea of building next pointers in KMP.

Consider the current node $u$ in the trie; the parent of $u$ is $p$, and $p$ points to $u$ via the edge with character $c$, i.e. $\operatorname{trie}(p, c)=u$. Assume the fail pointers of all nodes with depth less than that of $u$ have already been computed.

1.  If $\operatorname{trie}(\operatorname{fail}(p), c)$ exists: let the fail pointer of $u$ point to $\operatorname{trie}(\operatorname{fail}(p), c)$. This amounts to appending the character $c$ to $p$ and to $\operatorname{fail}(p)$, giving $u$ and $\operatorname{fail}(u)$ respectively;
2.  if $\operatorname{trie}(\operatorname{fail}(p), c)$ does not exist: we continue to look for $\operatorname{trie}(\operatorname{fail}(\operatorname{fail}(p)), c)$. We repeat this check, jumping along fail pointers until the root;
3.  if it still does not exist, let the fail pointer point to the root.

This completes the construction of $\operatorname{fail}(u)$.

### Example

Below we use several GIF animations to demonstrate the construction of fail pointers for the trie formed by the strings $\mathtt{i}$, $\mathtt{he}$, $\mathtt{his}$, $\mathtt{she}$, $\mathtt{hers}$:

1.  Yellow node: the current node $u$.
2.  Green nodes: nodes already processed by the BFS.
3.  Orange edges: fail pointers.
4.  Red edge: the fail pointer just computed.

![AC\_automation\_gif\_b\_3.gif](./images/ac-automaton1.gif)

Let us focus on the construction of the fail pointer of node $6$:

![AC\_automation\_6\_9.png](./images/ac-automaton1.png)

Find the parent of $6$, node $5$, with $\operatorname{fail}(5)=10$. However, node $10$ has no outgoing edge with the letter $\mathtt{s}$; we continue to the fail pointer of $10$, $\operatorname{fail}(10)=0$. We find that node $0$ has an outgoing edge with the letter $\mathtt{s}$ pointing to node $7$; therefore $\operatorname{fail}(6)=7$.

The figure below shows the state after the construction is complete:

![finish](./images/ac-automaton4.png)

## Trie and trie graph

Let us look at the construction function `build`. This function has two goals: building the fail pointers and building the automaton. The relevant variables are defined as follows:

1.  `tr[u].son[c]`: there are two ways to understand it. We can simply understand it as an edge of the trie, i.e. $\operatorname{trie}(u, c)$; or as the state (node) reached by appending a character $c$ to the state (node) $u$, i.e. a state transition function $\operatorname{trans}(u, c)$. For convenience, we use the second interpretation below.
2.  Queue `q`: used for the BFS traversal of the trie.
3.  `tr[u].fail`: the fail pointer of node $u$.

???+ note "Implementation"
    === "C++"
        ```cpp
        void build() {
          queue<int> q;
          for (int i = 0; i < 26; i++)
            if (tr[0].son[i]) q.push(tr[0].son[i]);
          while (!q.empty()) {
            int u = q.front();
            q.pop();
            for (int i = 0; i < 26; i++) {
              if (tr[u].son[i]) {
                tr[tr[u].son[i]].fail = tr[tr[u].fail].son[i];
                q.push(tr[u].son[i]);
              } else
                tr[u].son[i] = tr[tr[u].fail].son[i];
            }
          }
        }
        ```
    
    === "Python"
        ```python
        def build():
            for i in range(0, 26):
                if tr[0][i] != 0:
                    q.append(tr[0][i])
            while q:
                u = q.pop(0)
                for i in range(0, 26):
                    if tr[u][i] != 0:
                        fail[tr[u][i]] = tr[fail[u]][i]
                        q.append(tr[u][i])
                    else:
                        tr[u][i] = tr[fail[u]][i]
        ```

### Explanation

The `build` function enqueues the nodes in BFS order and computes their fail pointers one by one. The root of the trie here is $0$; we enqueue the children of the root one by one. If we enqueued the root itself, then during the first BFS step the fail pointers of the root's children would be set to themselves. Therefore we enqueue the children of the root instead of the root.

Then the BFS starts: each time we take the node $u$ at the front of the queue ($\operatorname{fail}(u)$ was already computed earlier in the BFS) and iterate over the alphabet (here $0 \sim 25$, corresponding to $\mathtt{a} \sim \mathtt{z}$, i.e. the children of $u$):

1.  If $\operatorname{trans}(u, c)$ exists, we assign the fail pointer of $\operatorname{trans}(u, c)$ to be $\operatorname{trans}(\operatorname{fail}(u), c)$. According to the earlier description we should use a `while` loop to keep jumping along fail pointers, checking whether a node for the character $c$ exists, and only then assign; but here the code is simplified by a special treatment explained below;
2.  otherwise, let $\operatorname{trans}(u, c)$ point to the state $\operatorname{trans}(\operatorname{fail}(u), c)$.

The treatment here is that the code in the `else` branch modifies the structure of the trie, linking the non-existent trie states to the corresponding state of the fail pointer. In the original trie each node represents a string $S$ that is a prefix of some pattern. After modifying the trie structure, although many transitions are added, the string represented by each node (state) does not change.

And $\operatorname{trans}(S, c)$ amounts to appending a character $c$ to $S$ to obtain another state $S'$. If $S'$ exists, there is a pattern whose prefix is $S'$; otherwise we let $\operatorname{trans}(S, c)$ point to $\operatorname{trans}(\operatorname{fail}(S), c)$. Since the string corresponding to $\operatorname{fail}(S)$ is a suffix of $S$, the string corresponding to $\operatorname{trans}(\operatorname{fail}(S), c)$ is also a suffix of $S'$.

In other words, when jumping on the trie we only jump from $S$ to $S'$, which amounts to matching $S'$; but when jumping on the AC automaton we jump from $S$ to a suffix of $S'$, that is, we match a character $c$ and then discard part of the prefix of $S$. Discarding a prefix obviously preserves the match. At the same time, if the text matches $S$, it obviously also matches a suffix of $S$, so the fail pointer likewise discards a prefix. The so-called fail pointer is in fact a set of suffixes of $S$.

The children array `son` of a trie node has another, simpler interpretation: if a mismatch happens at position $u$, we jump to position $\operatorname{fail}(u)$. Note that this may require jumping along the fail array several times before reaching the next matching position. So we can use `son` to directly record the next matching position, which guarantees the time complexity of the program.

This modification of the trie structure makes the matching transitions more complete. At the same time it compresses the paths of fail pointer jumps, so that what originally required many fail jumps becomes a single jump.

### Procedure

Again we use several GIF animations to show the construction process:

![AC\_automation\_gif\_b\_pro3.gif](./images/ac-automaton2.gif)

1.  Blue node: the node $u$ reached by the BFS.
2.  Blue edges: edges added from the current node by the AC automaton's modification of the trie structure.
3.  Black edges: edges added by the AC automaton's modification of the trie structure.
4.  Red edge: the fail pointer computed for the current node.
5.  Yellow edges: fail pointers.
6.  Gray edges: trie edges.

We can see that the many interleaved black edges turn the trie into a **trie graph**. The black edges to the root are omitted in the figure (otherwise it would be even messier). Let us focus on the situation when node $5$ is processed. We compute the fail pointer of $\operatorname{trans}(5, \mathtt{s})=6$:

![AC\_automation\_b\_7.png](./images/ac-automaton2.png)

The original strategy is to follow fail pointers: we jump to $\operatorname{fail}(5)=10$, find no trie edge with $\mathtt{s}$, jump to $\operatorname{fail}(10)=0$, find $\operatorname{trie}(0, \mathtt{s})=7$, hence $\operatorname{fail}(6)=7$; but with the black and blue edges, after jumping to $\operatorname{fail}(5)=10$ we directly follow $\operatorname{trans}(10, \mathtt{s})=7$ and arrive at node $7$.

These are the two things `build` accomplishes: building the fail pointers and building the trie graph. This trie graph also plays a key role during queries.

## Multi-pattern matching

Next we analyze the matching function `query`:

???+ note "Implementation"
    === "C++"
        ```cpp
        int query(const char t[]) {
          int u = 0, res = 0;
          for (int i = 1; t[i]; i++) {
            u = tr[u].son[t[i] - 'a'];
            for (int j = u; j && tr[j].cnt != -1; j = tr[j].fail) {
              res += tr[j].cnt, tr[j].cnt = -1;
            }
          }
          return res;
        }
        ```
    
    === "Python"
        ```python
        def query(t: str) -> int:
            u, res = 0, 0
            for c in t:
                u = tr[u][c - ord("a")]
                j = u
                while j and e[j] != -1:
                    res += e[j]
                    e[j] = -1
                    j = fail[j]
            return res
        ```

### Explanation

Here $u$ is the node of the trie currently reached by the matching, and `res` is the answer to return. We loop over the text, and $u$ tracks the current character in the trie. Using fail pointers we find all matched patterns and add them to the answer. Then we reset the occurrence count of the matched patterns to zero, so that the same pattern is not counted twice. As analyzed above, the structure of the trie is in fact a trans function; once this function is built, while matching the string we discard part of the prefix to obtain the minimal match. The fail pointers then point to further matched states. Finally, one more figure. For the automaton above:

![AC\_automation\_b\_13.png](./images/ac-automaton3.png)

If we try to match $\mathtt{ushersheishis}$ starting from the root, $p$ changes as follows:

![AC\_automation\_gif\_c.gif](./images/ac-automaton3.gif)

1.  Red node: the node $p$.
2.  Pink arrows: the jumps of $p$ on the automaton.
3.  Blue edges: successfully matched patterns.
4.  Blue nodes: the nodes (states) visited while jumping along fail pointers.

## Efficiency optimization

For the problem, see Luogu [P5357 [template] AC automaton](https://www.luogu.com.cn/problem/P5357).

In our AC automaton, each match keeps jumping along fail edges to find all matches, but this is rather inefficient and exceeds the time limit on some problems.

So how do we optimize it? First we need to know a property of fail pointers: in an AC automaton, if we keep only the fail edges, the remaining graph must be a tree.

This is obvious, because fail pointers never form a cycle and always lead to a smaller depth, which proves the claim.

Thus the matching of the AC automaton can be transformed into a chain-sum problem on the fail tree, and we only need to optimize that part.

We offer two approaches here.

### Topological sort optimization

Observe that the time is mostly wasted on jumping along fail pointers every time. If we can record things in advance and sum them up at the end, efficiency improves.

So we perform a topological sort on the fail tree (an in-tree) and compute the number of occurrences of all patterns in one pass.

Compared with the original, the `build` function adds an in-degree counting part to prepare for the topological sort.

???+ note "Build"
    ```cpp
    void build() {
      queue<int> q;
      for (int i = 0; i < 26; i++)
        if (tr[0].son[i]) q.push(tr[0].son[i]);
      while (!q.empty()) {
        int u = q.front();
        q.pop();
        for (int i = 0; i < 26; i++) {
          if (tr[u].son[i]) {
            tr[tr[u].son[i]].fail = tr[tr[u].fail].son[i];
            tr[tr[tr[u].fail].son[i]].du++;  // in-degree count
            q.push(tr[u].son[i]);
          } else
            tr[u].son[i] = tr[tr[u].fail].son[i];
        }
      }
    }
    ```

Then during the query we only mark the `ans` of the node we reach, and at the end we use the topological sort to compute the answer.

???+ note "Query"
    ```cpp
    void query(const char t[]) {
      int u = 0;
      for (int i = 1; t[i]; i++) {
        u = tr[u].son[t[i] - 'a'];
        tr[u].ans++;
      }
    }
    
    void topu() {
      queue<int> q;
      for (int i = 0; i <= tot; i++)
        if (tr[i].du == 0) q.push(i);
      while (!q.empty()) {
        int u = q.front();
        q.pop();
        ans[tr[u].idx] = tr[u].ans;
        int v = tr[u].fail;
        tr[v].ans += tr[u].ans;
        if (!--tr[v].du) q.push(v);
      }
    }
    ```

Finally the main function:

???+ note "Main function"
    ```cpp
    int main() {
      // do_something();
      AC::build();
      scanf("%s", s + 1);
      AC::query(s);
      AC::topu();
      for (int i = 1; i <= n; i++) printf("%d\n", AC::ans[idx[i]]);
      // do_another_thing();
    }
    ```

??? note "Template problem [Luogu P5357 [template] AC automaton](https://www.luogu.com.cn/problem/P5357), reference code with topological sort optimization"
    ```cpp
    --8<-- "docs/string/code/ac-automaton/ac-automaton_topu.cpp"
    ```

### DFS optimization

The idea is close to the topological sort, except that we use DFS instead of the topological sort. In fact the two methods are essentially the same: both sum the subtrees of the fail tree.

For the full code see template 3 in the summary.

## DP on the AC automaton

This part is explained using [P2292 \[HNOI2004\] L language](https://www.luogu.com.cn/problem/P2292) as the example problem.

It is not hard to come up with a naive approach: build the AC automaton, perform transitions on the AC automaton over the substrings of all fail pointers, and finally take the maximum as the answer.

The main code is as follows. If you are not familiar with the type definitions in the code, you can first look at the full code at the end:

???+ note "Main code of the query part"
    ```cpp
    int query(const char t[]) {
      int u = 0, len = strlen(t + 1);
      for (int i = 1; i <= len; i++) dp[i] = 0;
      for (int i = 1; i <= len; i++) {
        u = tr[u].son[t[i] - 'a'];
        for (int j = u; j; j = tr[j].fail) {
          if (tr[j].idx && (dp[i - tr[j].depth] || i - tr[j].depth == 0)) {
            dp[i] = dp[i - tr[j].depth] + tr[j].depth;
          }
        }
      }
      int ans = 0;
      for (int i = 1; i <= len; i++) ans = std::max(ans, dp[i]);
      return ans;
    }
    ```

But the complexity of this approach is not linear (because we jump along the fail pointers of every node), and it exceeds the time limit on the second subtask, so we need to optimize.

Let us look at the special property of the problem: we notice that all words have length at most $20$, which suggests a bitmask (state compression) optimization.

We notice that the current time bottleneck is mainly the fail-jumping step; if we can optimize this step to $O(1)$, the whole problem can be solved in strictly linear time.

Among the first $20$ letters, we can store the possible substring lengths, compress them into a state, and store it in each child node.

Then in `build` we can write:

???+ note "Building fail pointers"
    ```cpp
    void build() {
      queue<int> q;
      for (int i = 0; i < 26; i++)
        if (tr[0].son[i]) {
          q.push(tr[0].son[i]);
          tr[tr[0].son[i]].depth = 1;
        }
      while (!q.empty()) {
        int u = q.front();
        q.pop();
        int v = tr[u].fail;
        // the state is updated here
        tr[u].stat = tr[v].stat;
        if (tr[u].idx) tr[u].stat |= 1 << tr[u].depth;
        for (int i = 0; i < 26; i++) {
          if (tr[u].son[i]) {
            tr[tr[u].son[i]].fail = tr[tr[u].fail].son[i];
            tr[tr[u].son[i]].depth = tr[u].depth + 1;  // record the depth
            q.push(tr[u].son[i]);
          } else
            tr[u].son[i] = tr[tr[u].fail].son[i];
        }
      }
    }
    ```

Then in the query we can remove the fail-jumping loop and simplify the code as follows:

???+ note "Query"
    ```cpp
    int query(const char t[]) {
      int u = 0, mx = 0;
      unsigned st = 1;
      for (int i = 1; t[i]; i++) {
        u = tr[u].son[t[i] - 'a'];
        st <<= 1;  // moved one position down: the length of every bit grows by 1
        if (tr[u].stat & st) st |= 1, mx = i;
      }
      return mx;
    }
    ```

Our `tr[u].stat` maintains the set of lengths along the whole fail chain starting from node $u$ (since the lengths are less than $32$, this is not a problem), while `st` maintains the set of lengths over the last $32$ positions of the query string up to the current point (thanks to the natural overflow of the compressed state).

If the result of the `&` operation is non-zero, the intersection of the two length sets is non-empty, and we have found a match.

??? note "[P2292 \[HNOI2004\] L language](https://www.luogu.com.cn/problem/P2292), full code"
    ```cpp
    --8<-- "docs/string/code/ac-automaton/ac_automaton_luoguP2292.cpp"
    ```

## Summary

Time complexity: let $|s_i|$ be the length of a pattern, $|S|$ the length of the text, and $|\Sigma|$ the size of the alphabet (a constant, usually $26$). If the trie graph is built, the time complexity is $O(\sum|s_i|+n|\Sigma|+|S|)$, where $n$ is the number of nodes of the AC automaton, which can reach $O(\sum|s_i|)$. If the trie graph is not built and empty children are not visited while building the fail pointers, the time complexity is $O(\sum|s_i|+|S|)$.

??? note "Template problem [Luogu P3808 AC automaton (simple version)](https://www.luogu.com.cn/problem/P3808), reference code"
    ```cpp
    --8<-- "docs/string/code/ac-automaton/ac-automaton_1.cpp"
    ```

??? note "Template problem [Luogu P3796 AC automaton (simple version II)](https://www.luogu.com.cn/problem/P3796), reference code"
    ```cpp
    --8<-- "docs/string/code/ac-automaton/ac-automaton_2.cpp"
    ```

??? note "Template problem [Luogu P5357 [template] AC automaton](https://www.luogu.com.cn/problem/P5357), reference code with DFS optimization"
    ```cpp
    --8<-- "docs/string/code/ac-automaton/ac-automaton_3.cpp"
    ```
