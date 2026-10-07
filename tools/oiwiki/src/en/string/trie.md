---
title: Trie (prefix tree)
---

## Definition

A trie, also called a prefix tree, is pronounced like "try" and is named after "retrieval". As the name suggests, it is a tree that works like a dictionary.

## Introduction

Let us first look at a picture:

![trie1](./images/trie1.png)

As we can see, this trie represents letters with edges, and a path from the root to a node of the tree represents a string. For example, $1\to4\to 8\to 12$ represents the string `caa`.

The structure of a trie is very simple: we use $\delta(u,c)$ to denote the next node that the edge labeled with character $c$ leads to from node $u$, i.e. the node representing the string obtained by appending the character $c$ to the string of node $u$. (The range of $c$ depends on the alphabet size and is not necessarily $0\sim 26$.)

Sometimes we need to mark which strings have been inserted into the trie; it is enough to mark the node representing the string after each insertion.

## Implementation

Here is a template wrapped in a struct:

=== "C++"
    ```cpp
    struct trie {
      int nex[100000][26], cnt;
      bool exist[100000];  // whether a string ends at this node
    
      void insert(char *s, int l) {  // insert a string
        int p = 0;
        for (int i = 0; i < l; i++) {
          int c = s[i] - 'a';
          if (!nex[p][c]) nex[p][c] = ++cnt;  // if it does not exist, add a node
          p = nex[p][c];
        }
        exist[p] = true;
      }
    
      bool find(char *s, int l) {  // find a string
        int p = 0;
        for (int i = 0; i < l; i++) {
          int c = s[i] - 'a';
          if (!nex[p][c]) return 0;
          p = nex[p][c];
        }
        return exist[p];
      }
    };
    ```

=== "Python"
    ```python
    class trie:
        def __init__(self):
            self.nex = [[0 for i in range(26)] for j in range(100000)]
            self.cnt = 0
            self.exist = [False] * 100000  # whether a string ends at this node
    
        def insert(self, s):  # insert a string
            p = 0
            for i in s:
                c = ord(i) - ord("a")
                if not self.nex[p][c]:
                    self.cnt += 1
                    self.nex[p][c] = self.cnt  # if it does not exist, add a node
                p = self.nex[p][c]
            self.exist[p] = True
    
        def find(self, s):  # find a string
            p = 0
            for i in s:
                c = ord(i) - ord("a")
                if not self.nex[p][c]:
                    return False
                p = self.nex[p][c]
            return self.exist[p]
    ```

=== "Java"
    ```java
    public class Trie {
        int[][] tree = new int[10000][26];
        int cnt = 0;
        boolean[] end = new boolean[10000];
        
        public void insert(String word) {
            int p = 0;
            char[] chars = word.toCharArray();
            for (int i = 0; i < chars.length; i++) {
                int c = chars[i] - 'a';
                if (tree[p][c] == 0) {
                    tree[p][c] = ++cnt;
                }
                p = tree[p][c];
            }
            end[p] = true;
        }
        
        public boolean find(String word) {
            int p = 0;
            char[] chars = word.toCharArray();
            for (int i = 0; i < chars.length; i++) {
                int c = chars[i] - 'a';
                if (tree[p][c] == 0) {
                    return false;
                }
                p = tree[p][c];
            }
            return end[p];
        }
    }
    ```

## Applications

### String retrieval

The most basic application of a trie: checking whether a string appears in the "dictionary".

???+ note "[And so the wrong roll call began (Luogu P2580)](https://www.luogu.com.cn/problem/P2580)"
    Given $n$ names, then $m$ roll calls are performed; for each one, answer "the name does not exist", "the name is called for the first time", or "the name has already been called".
    
    $1\le n\le 10^4$, $1\le m\le 10^5$, the length of each string does not exceed $50$.
    
    ??? note "Solution"
        Build a trie from all the names, then check in the trie whether the string exists and whether it has already been called; when it is called for the first time, mark it as called.
    
    ??? note "Reference code"
        ```cpp
        --8<-- "docs/string/code/trie/trie_1.cpp"
        ```

### Aho–Corasick automaton

A trie is a part of the [Aho–Corasick automaton](./ac-automaton.md).

### Maintaining XOR extremes

If we treat the binary representation of a number as a string, we can build a trie over the alphabet $\{0,1\}$.

???+ note "[BZOJ1954 Longest XOR path](https://hydro.ac/p/bzoj-P1954)"
    Given a tree with edge weights, find $(u, v)$ such that the XOR of the edge weights on the path from $u$ to $v$ is maximized, and output this maximum. The XOR of a path here means the XOR of all edge weights on it.
    
    The number of nodes does not exceed $10^5$, and the edge weights are in $[0,2^{31})$.
    
    ??? note "Solution"
        Pick an arbitrary root $root$ and let $T(u, v)$ denote the XOR of the edge weights on the path between $u$ and $v$; then $T(u,v)=T(root, u)\oplus T(root,v)$, because the part above the [LCA](../graph/lca.md) appears twice and cancels out under XOR.
        
        If we insert all $T(root, u)$ into a trie, then for each $T(root, u)$ we can quickly find the $T(root, v)$ that maximizes the XOR with it:
        
        start from the root of the trie; if we can go into a subtree whose bit differs from the current bit of $T(root, u)$, go there; otherwise there is no choice.
        
        Correctness of the greedy: if we go this way, this bit is $1$; if not, this bit is $0$. And higher bits take priority and should be as large as possible.
    
    ??? note "Reference code"
        ```cpp
        --8<-- "docs/string/code/trie/trie_2.cpp"
        ```

### Maintaining XOR sums

A 01-trie is a trie over the alphabet $\{0,1\}$. A 01-trie can maintain the XOR sum of a set of numbers, with support for modifications (delete + reinsert) and global increment by one (i.e. adding `1` to every maintained value; this is essentially a special kind of modification).

If we want to maintain the XOR sum, the trie must be built from the lowest bit to the highest bit of the values.

**Convention**: in the text, "upward" from the current node means the path from the current node to the root, and "downward" means the subtree of the current node.

#### Insertion and deletion

If we maintain the XOR sum, we **only need** to know the **parity** of the numbers of zeros and ones at each bit; i.e. for the digit `1`, the digit at this bit is `1` if and only if the number of ones at this bit is odd. Keep in mind at all times: if we only maintain the XOR sum, it is enough to know the number of ones at each bit, and we do not need to know exactly which numbers the trie contains.

For each node we record the following three quantities:

-   `ch[o][0/1]` are the two children of node `o`; `ch[o][0]` means the next bit is `0`, and similarly `ch[o][1]` means the next bit is `1`.
-   `w[o]` is the number of values passing through the edge from node `o` to its parent (the weight). Each time a number `x` is inserted, the weights along the path in the trie corresponding to the binary representation of `x` are increased by `1`.
-   `xorv[o]` is the XOR sum maintained by the subtree rooted at `o`.

The code for maintaining a node looks like this.

```cpp
void maintain(int o) {
  w[o] = xorv[o] = 0;
  if (ch[o][0]) {
    w[o] += w[ch[o][0]];
    xorv[o] ^= xorv[ch[o][0]] << 1;
  }
  if (ch[o][1]) {
    w[o] += w[ch[o][1]];
    xorv[o] ^= (xorv[ch[o][1]] << 1) | (w[ch[o][1]] & 1);
  }
  // w[o] = w[o] & 1;
  // Only the parity is needed, not the exact value. Of course this line can also be deleted, since above we only use its parity.
}
```

The code for insertion and deletion is very similar.

Things to note:

-   `MAXH` here denotes the depth of the trie, i.e. we force the distance from every leaf to the root to be `MAXH`. For smaller values we might not need to build so deep (e.g. when inserting the number `4`, whose binary representation is `100`, inserting the three bits `001` from the root would be enough), but we still force the insertion of `MAXH` bits. The purpose is to handle carries conveniently during the global `+1`. For example, if the original number is `3` (`11`), after the increment it becomes `4` (`100`); if we had inserted only `2` bits when inserting `3`, the carry would be lost.

-   During insertion and deletion, we only need to modify `w[]` of the leaf, and then maintain the nodes on the way back up the recursion.

???+ note "Implementation"
    ```cpp
    namespace trie {
    constexpr int MAXH = 21;
    int ch[_ * (MAXH + 1)][2], w[_ * (MAXH + 1)], xorv[_ * (MAXH + 1)];
    int tot = 0;
    
    int mknode() {
      ++tot;
      ch[tot][1] = ch[tot][0] = w[tot] = xorv[tot] = 0;
      return tot;
    }
    
    void maintain(int o) {
      w[o] = xorv[o] = 0;
      if (ch[o][0]) {
        w[o] += w[ch[o][0]];
        xorv[o] ^= xorv[ch[o][0]] << 1;
      }
      if (ch[o][1]) {
        w[o] += w[ch[o][1]];
        xorv[o] ^= (xorv[ch[o][1]] << 1) | (w[ch[o][1]] & 1);
      }
      w[o] = w[o] & 1;
    }
    
    void insert(int &o, int x, int dp) {
      if (!o) o = mknode();
      if (dp > MAXH) return (void)(w[o]++);
      insert(ch[o][x & 1], x >> 1, dp + 1);
      maintain(o);
    }
    
    void erase(int o, int x, int dp) {
      if (dp > 20) return (void)(w[o]--);
      erase(ch[o][x & 1], x >> 1, dp + 1);
      maintain(o);
    }
    }  // namespace trie
    ```

#### Global increment by one

Global increment by one means adding `1` to every value in the trie.

Formally, if the trie maintains the values $V_1, V_2, V_3 \dots V_n$, then after a global increment by one the maintained values should become $V_1+1, V_2+1, V_3+1 \dots V_n+1$

```cpp
void addall(int o) {
  swap(ch[o][0], ch[o][1]);
  if (ch[o][0]) addall(ch[o][0]);
  maintain(o);
}
```

##### Procedure

Think about how `+1` is performed in binary.

We only need to find the first `0` from the lowest bit to the highest, turn it into `1`, and turn all the `1`s below that position into `0`.

Here are a few examples to get a feeling (the numbers in parentheses are the corresponding decimal values):

    1000(8)  + 1 = 1001(9)  ;
    10011(19) + 1 = 10100(20) ;
    11111(31) + 1 = 100000(32);
    10101(21) + 1 = 10110(22) ;
    100000000111111(16447) + 1 = 100000001000000(16448);

In the trie this corresponds to swapping the left and right children and then recursing down the `0` edge **after the swap**.

Recall the definition of `w[o]`: `w[o]` is the number of values passing through the edge from node `o` to its parent (the weight).

Does this definition feel a bit odd? Perhaps it would be more common to store in the parent the weights of the edges to its two children. But here, when swapping the left and right children, it is clearly more convenient to store in the child the weight of the edge to its parent.

### Merging 01-tries

This means merging two 01-tries as described above, while also merging the information they maintain.

There may be few articles about merging tries, but the idea of merging tries is very similar to merging segment trees, so you can look up "segment tree merging" to learn how to merge tries.

Merging tries is actually very simple: imagine a function `int merge(int a, int b)` that takes the node numbers of two tries at the same relative position and returns the number of the merged node after merging.

#### Procedure

How to implement it?

There are three cases:

-   if `a` has no node at this position, the new merged node is `b`;
-   if `b` has no node at this position, the new merged node is `a`;
-   if both `a` and `b` exist, merge the information of `b` into `a`, the new merged node is `a`, and then recursively handle the left and right children of node a.

    **Note**: if a and b need to be merged into a new tree, a new node can be created here and merged into; this implementation only merges the information of b into a.

#### Implementation

```cpp
int merge(int a, int b) {
  if (!a) return b;  // if a has no node at this position, return b
  if (!b) return a;  // if b has no node at this position, return a
  /*
    If both `a` and `b` exist,
    merge the information of `b` into `a`.
  */
  w[a] = w[a] + w[b];
  xorv[a] ^= xorv[b];
  /* Do not use maintain():
    maintain() merges the information of the two children of node a,
    whereas here we need to merge the information of nodes a and b.
   */
  ch[a][0] = merge(ch[a][0], ch[b][0]);
  ch[a][1] = merge(ch[a][1], ch[b][1]);
  return a;
}
```

In fact, any trie can be merged; in other words, trie merging is not limited to 01-tries.

???+ note "[【luogu-P6018】【Ynoi2010】Fusion tree](https://www.luogu.com.cn/problem/P6018)"
    You are given a tree with $n$ nodes, each node has a value. Then there are $m$ operations.
    The following operations must be supported.
    
    -   Apply $+1$ to the value of every node at distance $1$ from node $x$. The distance between two nodes in the tree is defined as the number of edges on the shortest path between them.
    
    -   Apply $-v$ to the value of node $x$.
    
    -   Output the XOR sum of the values of all nodes at distance $1$ from node $x$.
        For $100\%$ of the data, $1\le n \le 5\times 10^5$, $1\le m \le 5\times 10^5$, $0\le a_i \le 10^5$, $1 \le x \le n$, $opt\in\{1,2,3\}$.
        It is guaranteed that the value of every node is non-negative at all times.
    
    ??? note "Solution"
        For each node, build a trie maintaining the values of its children; the trie must support global increment by one.
        We can keep a lazy tag at each node recording how much the children's values have been increased.
    
    ??? note "Reference code"
        ```cpp
        --8<-- "docs/string/code/trie/trie_3.cpp"
        ```

???+ note "[【luogu-P6623】【Provincial Selection 2020 Version A】Tree](https://www.luogu.com.cn/problem/P6623)"
    You are given a rooted tree $T$ with $n$ nodes numbered from $1$, rooted at node $1$; each node has a positive integer value $v_i$.
    Let $c_1,c_2,\dots,c_k$ be the numbers of all nodes in the subtree of node $x$ (including $x$ itself); the value of node $x$ is defined as:  
    $val(x)=(v_{c_1}+d(c_1,x)) \oplus (v_{c_2}+d(c_2,x)) \oplus \cdots \oplus (v_{c_k}+d(c_k, x))$, where $d(x,y)$  
    denotes the number of edges on the unique simple path between nodes $x$ and $y$ in the tree, $d(x,x) = 0$. $\oplus$ denotes the XOR operation.
    Compute $\sum\limits_{i=1}^n val(i)$.
    
    ??? note "Solution"
        Consider the contribution of each node to all of its ancestors.
        For each node, build a trie initially containing only the value of that node; then, from bottom to top, merge the tries of the children, perform a global increment by one, and then add to the answer.
    
    ??? note "Reference code"
        ```cpp
        constexpr int _ = 526010;
        int n;
        int V[_];
        int debug = 0;
        
        namespace trie {
        constexpr int MAXH = 21;
        int ch[_ * (MAXH + 1)][2], w[_ * (MAXH + 1)], xorv[_ * (MAXH + 1)];
        int tot = 0;
        
        int mknode() {
          ++tot;
          ch[tot][1] = ch[tot][0] = w[tot] = xorv[tot] = 0;
          return tot;
        }
        
        void maintain(int o) {
          w[o] = xorv[o] = 0;
          if (ch[o][0]) {
            w[o] += w[ch[o][0]];
            xorv[o] ^= xorv[ch[o][0]] << 1;
          }
          if (ch[o][1]) {
            w[o] += w[ch[o][1]];
            xorv[o] ^= (xorv[ch[o][1]] << 1) | (w[ch[o][1]] & 1);
          }
          w[o] = w[o] & 1;
        }
        
        void insert(int &o, int x, int dp) {
          if (!o) o = mknode();
          if (dp > MAXH) return (void)(w[o]++);
          insert(ch[o][x & 1], x >> 1, dp + 1);
          maintain(o);
        }
        
        int merge(int a, int b) {
          if (!a) return b;
          if (!b) return a;
          w[a] = w[a] + w[b];
          xorv[a] ^= xorv[b];
          ch[a][0] = merge(ch[a][0], ch[b][0]);
          ch[a][1] = merge(ch[a][1], ch[b][1]);
          return a;
        }
        
        void addall(int o) {
          swap(ch[o][0], ch[o][1]);
          if (ch[o][0]) addall(ch[o][0]);
          maintain(o);
        }
        }  // namespace trie
        
        int rt[_];
        long long Ans = 0;
        vector<int> E[_];
        
        void dfs0(int o) {
          for (int i = 0; i < E[o].size(); i++) {
            int node = E[o][i];
            dfs0(node);
            rt[o] = trie::merge(rt[o], rt[node]);
          }
          trie::addall(rt[o]);
          trie::insert(rt[o], V[o], 0);
          Ans += trie::xorv[rt[o]];
        }
        
        int main() {
          n = read();
          for (int i = 1; i <= n; i++) V[i] = read();
          for (int i = 2; i <= n; i++) E[read()].push_back(i);
          dfs0(1);
          printf("%lld", Ans);
          return 0;
        }
        ```

### Persistent trie

See [Persistent trie](../ds/persistent-trie.md).
