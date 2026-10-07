---
title: Generalized suffix automaton
---

## Prerequisites

The generalized suffix automaton is based on the following topics:

-   [trie](./trie.md)
-   [suffix automaton](./sam.md)

Please read this article only after you are very familiar with both topics above, and in particular after you have a good understanding of **suffix links** in the **suffix automaton**.

## Introduction

### Origin

The generalized suffix automaton is a structure proposed by Liu Yanyi in his 2015 Chinese national team paper "Extending the suffix automaton to the trie" (《后缀自动机在字典树上的拓展》): the suffix automaton is built directly on top of a trie.

> Most string problems that can be handled with a suffix automaton can be extended to a trie. — Liu Yanyi

### Conventions

See the [string conventions](./basic.md).

There are $k$ strings, namely $S_1, S_2, S_3 \dots S_k$.

By convention, the root of the trie and of the generalized suffix automaton is node $0$.

### Overview

The suffix automaton (SAM) is a powerful tool for substring problems on a single string.

The generalized suffix automaton (general suffix automaton), on the other hand, integrates the suffix automaton into a trie to solve substring problems on multiple strings.

## Common pseudo-generalized suffix automata

1.  Concatenate the strings directly using special characters, then build the SAM.
2.  For every string, repeat the construction on the same SAM, resetting the `last` pointer to zero before each construction.

Methods 1 and 2 are simple to implement and usually achieve the same correctness as the generalized suffix automaton on contest problems. For this reason many people online choose such implementations; for example, the last application in the suffix automaton article uses method 1 [(link to the original)](./sam.md).

However, for both method 1 and method 2 the time complexity is rather dangerous.

## Building the generalized suffix automaton

According to the original paper, one should first build a trie on the strings and then build the generalized suffix automaton on top of the trie.

### Using the trie

First we build a trie for the strings, which is nothing difficult: if you have mastered the prerequisites, you can build it very quickly. To keep the code in this article consistent, we give one possible trie implementation here.

??? note "Implementation"
    ```cpp
    constexpr int MAXN = 2000000;
    constexpr int CHAR_NUM = 30;
    
    struct Trie {
      int next[MAXN][CHAR_NUM];  // transitions
      int tot;                   // total number of nodes: [0, tot)
    
      void init() { tot = 1; }
    
      int insertTrie(int cur, int c) {
        if (next[cur][c]) return next[cur][c];
        return next[cur][c] = tot++;
      }
    
      void insert(const string &s) {
        int root = 0;
        for (auto ch : s) root = insertTrie(root, ch - 'a');
      }
    };
    ```

Here we have obtained a trie built on the `next` array.

### Building the suffix automaton

If we regard such a tree directly as a suffix automaton, we get the following conclusions:

-   for node `i`, its `len[i]` equals its depth in the trie;
-   if we topologically sort the trie, we get a sequence whose `len` is non-decreasing; a BFS gives the same result.

The construction of a suffix automaton, in turn, can be viewed as repeatedly inserting strictly increasing values of `len`, with difference $1$. So we can take the result of the topological sort of the trie as a queue and then insert the nodes into the suffix automaton in the order of this queue.

In an ordinary suffix automaton, the `len` of the previous node is a fixed value, namely the `len` of the `last` node. In the generalized suffix automaton, however, the insertion queue is a non-strictly increasing sequence. Therefore, for every value, its `last` must be known and fixed: in the trie, it is its parent.

Since the trie already contains an approximate suffix automaton, it suffices to process the structure of the whole trie appropriately to turn it into a generalized suffix automaton. We can update every node of the whole trie in the order of the queue described above. In the end we obtain the generalized suffix automaton.

The update operation for each node is obtained by slightly modifying the insertion operation of the SAM.

During the whole insertion process, note the following: since we insert in non-decreasing order of `len`, when copying data after `clone`, we must not copy data whose `len` is smaller than the current `len`.

### Procedure

Following the logic above, the whole construction can be described by the following steps:

1.  insert all strings into the trie;
2.  run a BFS from the root of the trie, recording the order and the parent of every node;
3.  following the BFS order, build every node on the original trie, taking care not to touch data whose `len` is smaller than the current `len`.

### Proof that the number of operations is linear

Since we only process the sequence obtained by the BFS, every node of the trie is guaranteed to be visited exactly once.

For the worst case, consider the situation where the trie itself has the most nodes, i.e. no two strings share a common prefix; then the number of nodes is $\sum_{i=1}^{k}|S_i|$, the sum of the lengths of all strings.

The complexity of the update operation of the suffix automaton has already been proven in [suffix automaton](./sam.md).

Hence it can be proven that the worst-case complexity is linear.

Usually the average complexity of a pseudo-generalized suffix automaton equals the worst-case complexity of the generalized suffix automaton; when facing a large number of strings, the efficiency of the pseudo-generalized suffix automaton is far below that of the standard generalized suffix automaton.

### Implementation

A few necessary modifications of the insertion function give us the required function.

??? note "Sample code"
    ```cpp
    struct GSA {
      int len[MAXN];             // node length
      int link[MAXN];            // suffix link, link
      int next[MAXN][CHAR_NUM];  // transitions
      int tot;                   // total number of nodes: [0, tot)
    
      int insertSAM(int last, int c) {
        int cur = next[last][c];
        len[cur] = len[last] + 1;
        int p = link[last];
        while (p != -1) {
          if (!next[p][c])
            next[p][c] = cur;
          else
            break;
          p = link[p];
        }
        if (p == -1) {
          link[cur] = 0;
          return cur;
        }
        int q = next[p][c];
        if (len[p] + 1 == len[q]) {
          link[cur] = q;
          return cur;
        }
        int clone = tot++;
        for (int i = 0; i < CHAR_NUM; ++i)
          next[clone][i] = len[next[q][i]] != 0 ? next[q][i] : 0;
        len[clone] = len[p] + 1;
        while (p != -1 && next[p][c] == q) {
          next[p][c] = clone;
          p = link[p];
        }
        link[clone] = link[q];
        link[cur] = clone;
        link[q] = clone;
        return cur;
      }
    
      void build() {
        queue<pair<int, int>> q;
        for (int i = 0; i < CHAR_NUM; ++i)
          if (next[0][i]) q.push({i, 0});
        while (!q.empty()) {
          auto item = q.front();
          q.pop();
          auto last = insertSAM(item.second, item.first);
          for (int i = 0; i < CHAR_NUM; ++i)
            if (next[last][i]) q.push({i, last});
        }
      }
    }
    ```

-   Since in the order obtained by the BFS the parent node keeps changing, there is no need to store the `last` pointer.
-   In the insertion operation, `int cur = next[last][c];` differs from `int cur = tot++;` of the ordinary suffix automaton, because the node we insert already exists in the tree structure, so we only need to fetch it directly.
-   When copying data after `clone`, there is the check `next[clone][i] = len[next[q][i]] != 0 ? next[q][i] : 0;`, which differs from the direct assignment `next[clone][i] = next[q][i];` of the ordinary suffix automaton; this is to avoid updating values whose `len` is greater than that of the current node. This works because `len` in the array is assigned only once that value has been visited by the BFS and inserted into the suffix automaton.

## Properties

1.  The structure of the generalized suffix automaton is the same as that of the suffix automaton; the vast majority of the properties of the suffix automaton also hold for the generalized suffix automaton ([properties of the suffix automaton](./sam.md)).
2.  After the generalized suffix automaton is built, the trie structure is usually destroyed, i.e. the generalized suffix automaton usually cannot be used to solve trie problems. Of course, one can also allocate twice the space and build the suffix automaton in a separate space.

## Applications

### Number of distinct substrings over all strings

By the properties of the suffix automaton, the number of substrings ending at node $i$ equals $len[i] - len[link[i]]$.

So the answer is obtained by iterating over all nodes and summing.

Example problem: [[Template] Generalized suffix automaton (generalized SAM)](https://www.luogu.com.cn/problem/P6139)

??? note "Sample code"
    ```cpp
    --8<-- "docs/string/code/general-sam/general-sam_1.cpp"
    ```

### Longest common substring of multiple strings

For every node we need an array `flag` of length $k$ (for this problem a mere marker array suffices; if the number of occurrences of the substring is needed, it has to become a counter array).

When inserting a string into the trie, we count at all nodes and store the counts in the array belonging to the current string.

Then we traverse the nodes in decreasing order of `len` and, via the suffix links, merge the `flag` of the current node into the other nodes.

Traverse all nodes and find the node with the largest `len` whose `flag` is nonzero for all `k`; the $len$ of this node is the answer.

Example problem: [SPOJ Longest Common Substring II](https://www.spoj.com/problems/LCS2/)

??? note "Sample code"
    ```cpp
    --8<-- "docs/string/code/general-sam/general-sam_2.cpp"
    ```
