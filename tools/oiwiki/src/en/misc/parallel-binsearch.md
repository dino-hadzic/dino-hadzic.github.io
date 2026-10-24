---
title: Parallel binary search
---

## Introduction

In informatics competitions some problems can be solved by binary search. But when such a problem has many queries and running a separate binary search for every query could lead to TLE, parallel binary search is used. The main idea of parallel binary search is to solve many queries together. (So this is an offline algorithm.)

Problems that can be solved by parallel binary search must satisfy the following properties[^ref1]:

1.  the answer to a query can be binary searched;
2.  **the contributions of the updates to checking an answer are independent of each other**, updates do not affect each other's effect;
3.  if an update contributes to checking an answer, the contribution is a fixed value independent of the checking criterion;
4.  the contributions satisfy commutativity and associativity and are additive;
5.  the problem allows an offline algorithm.

## Explanation

Denote by $[l,r]$ the value range of the answers and by $[L,R]$ the domain of the answers. (That is, when computing the answers only the operations and queries with indices in the interval $[L,R]$ are considered, and the answers to these queries lie in $[l,r]$.)

-   We first store all operations in an array **in chronological order**, and then start the divide and conquer.
-   At every level of the recursion we use a data structure (commonly a Fenwick tree) to determine the relation between the answers to the current queries and $mid$.
-   According to the relation between the determined answer and $mid$ (less than or equal to $mid$, or greater than $mid$) we split the currently processed sequence of operations into two parts $q1$ and $q2$ and process each of them recursively.
-   When $l=r$, the answer has been found; record it and return.

Note that during parallel binary search, if the value range currently processed is $[l,r]$, the queries whose final answer is not in $[l,r]$ are processed at some other time.

## Procedure

???+ tip "Note"
    1.  For readability, the code in this text may not follow the common style used in actual competitions.
    2.  If some piece of code is hard to understand, first refer to the explanations of the previous problems, because content that has already been explained is not repeated, to save space.

Let us start from ordinary binary search:

### Querying the global k-th smallest

???+ note "Problem 1"
    Find the $k$-th smallest number in a sequence.

??? note "Solution"
    Of course we can simply sort. What about binary search? We can use a data structure to record how many numbers there are in every value range, then guess by binary search and verify with the data structure.

???+ note "Problem 2"
    Find the $k$-th smallest number in a sequence, many times.

??? note "Solution"
    We can run a binary search for every query; but we can also binary search all queries together.
    
    First consider the essence of binary search: suppose we want to guess a number in $[l,r]$, and after guessing we learn whether the guess was too large, too small, or exactly right. Of course we could enumerate from $l$ to $r$, but a better method is binary search: guess that the answer is $m = \lfloor\frac{l + r}{2}\rfloor$, then verify the correctness of $m$ and adjust the bounds. This way the complexity of every query is $O(\log n)$; if the number of queries is $q$, the time complexity is $O(q\log n)$.
    
    Coming back, for all current queries we can guess that the answer to every query is $mid$, then verify in turn whether the answer to each query should be less than or equal to $mid$ or greater than $mid$, split the queries into two parts (not greater/greater), and continue the binary search for each part. Note: if the answer to a query is greater than $mid$, its $k$ must be updated before moving it to the right side, i.e. if there are $t$ numbers less than or equal to $mid$ in the current sequence, then after the split the query actually asks for the $k - t$-th smallest number in the right interval. If a part has $l = r$, the binary search of this part ends. Using knowledge about segment trees: each time we split the whole interval $[1,n]$ in which the answer may lie (assuming it has been discretized) into several parts; such splits are performed $O(\log n)$ times in total, and one split runs over the whole sequence of operations once. If operating on the whole sequence while supporting the corresponding queries has time complexity $O(T)$, the time complexity of parallel binary search is $O(T\log n)$.

??? note "Reference code"
    ```cpp
    struct Query {
      int id, k;  // the id of this query, the k of this query
    };
    
    int ans[N], a[N];  // ans[i] is the answer to the query with id i, a is the original sequence
    int val[N], cnt[N];  // after discretization, the corresponding values and their counts (assumed to be computed already)
    
    // returns the number of elements of the original sequence whose value is in [l,r]
    int check(int l, int r) {
      int res = 0;
      for (int i = l; i <= r; i++) {
        res += cnt[i];
      }
      return res;
    }
    
    // parallel binary search
    void solve(int l, int r, vector<Query> q) {
      int m = (l + r) / 2;
      if (l == r) {
        for (unsigned i = 0; i < q.size(); i++) ans[q[i].id] = val[l];
        return;
      }
      vector<Query> q1, q2;
      int t = check(l, m);
      for (unsigned i = 0; i < q.size(); i++) {
        if (q[i].k <= t)
          q1.push_back(q[i]);
        else
          q[i].k -= t, q2.push_back(q[i]);
      }
      solve(l, m, q1), solve(m + 1, r, q2);
      return;
    }
    ```

### Querying the k-th smallest in a range

???+ note "Problem 3"
    Find the $k$-th smallest number in a range of a sequence, many times.

??? note "Solution"
    When the queries involve a given range, binary searching by the previous method would make the time complexity of the `check` function explode. We still consider the relation between a query and the midpoint $m$ of the value range: if there are $t$ numbers less than or equal to $m$ in the query range and the query asks for the $k$-th smallest number in the range, then when $k \leq t$ the answer should be less than or equal to $m$; otherwise the answer should be greater than $m$. (Mind the boundary cases.) Here we have to record the number of elements in a range that are less than or equal to a given number, i.e. point add and range sum, which can be handled quickly with a Fenwick tree. To improve efficiency, we only count the numbers of the sequence whose value is in the value range $[l,r]$, i.e. before recursing further we not only split the queries but also split the currently processed numbers into two halves by value range.

??? note "Reference code (key part)"
    ```cpp
    struct Num {
      int p, x;
    };  // the number at position p of the sequence has value x
    
    struct Query {
      int l, r, k, id;
    };  // a query with id id asking for the k-th smallest number in [l,r]
    
    int ans[N];
    void add(int p, int x);  // Fenwick tree, add x at position p
    int query(int p);        // Fenwick tree, sum over [1,p]
    void clear();            // Fenwick tree, clear
    
    void solve(int l, int r, vector<Num> a, vector<Query> q)
    // a contains the numbers of the given sequence whose value is in the value range [l,r]
    {
      int m = (l + r) / 2;
      if (l == r) {
        for (unsigned i = 0; i < q.size(); i++) ans[q[i].id] = l;
        return;
      }
      vector<Num> a1, a2;
      vector<Query> q1, q2;
      for (unsigned i = 0; i < a.size(); i++)
        if (a[i].x <= m)
          a1.push_back(a[i]), add(a[i].p, 1);
        else
          a2.push_back(a[i]);
      for (unsigned i = 0; i < q.size(); i++) {
        int t = query(q[i].r) - query(q[i].l - 1);
        if (q[i].k <= t)
          q1.push_back(q[i]);
        else
          q[i].k -= t, q2.push_back(q[i]);
      }
      clear();
      solve(l, m, a1, q1), solve(m + 1, r, a2, q2);
      return;
    }
    ```

Below we provide a competition-style implementation of parallel binary search for the problem [【模板】可持久化线段树 2 (Template: Persistent Segment Tree 2)](https://www.luogu.com.cn/problem/P3834).

??? note "Reference code"
    ```cpp
    --8<-- "docs/misc/code/parallel-binsearch/parallel-binsearch_1.cpp"
    ```

### K-th smallest in a range with updates

???+ note "Problem 4 ([Dynamic Rankings](https://www.luogu.com.cn/problem/P2617))"
    Given a sequence, support point updates and range queries for the $k$-th smallest.

??? note "Solution"
    An update operation can be understood directly as deleting a number from the original sequence and adding another one; for convenience, queries and updates are collectively called "operations". Since later operations depend on earlier ones, we cannot separate the counting from the processing of the queries as in Problem 3, so we store all operations in one array, distinguish their types with a flag, and process the operations one by one. To make the handling with the Fenwick tree easier, an update operation can be split into an erase operation and an insert operation.
    
    **Optimizations**
    
    1.  Note that every time the operations are classified, only their order changes, so we can operate directly on the original array. Concretely, during the binary search we replace the arrays $q, a$ that record the operations with one large global array, and the information recorded during the binary search becomes $L, R$, i.e. which interval of the global array is currently being processed. We use temporary arrays to record the current classification, and before recursing further we write the information from the temporary arrays back to the original array.
    2.  Clearing the Fenwick tree every time would make the time complexity explode; instead, every time the Fenwick tree is used we record the positions currently modified (this is already achieved by the temporary arrays mentioned in 1), and after the current operation is finished we add $-1$ at the same positions to quickly reset it to zero.
    3.  The initialization of the sequence at the beginning can be simplified to insert operations.

??? note "Reference code (key part)"
    ```cpp
    struct Opt {
      int x, y, k, type, id;
      // for a query: type = 1, x, y are the left and right endpoints of the range, k means the k-th smallest is asked
      // for an update: type = 0, x is the updated position, y is the value after the update,
      // k indicates whether the current operation is an insert (1) or an erase (-1), used when updating the Fenwick tree.
      // id records the original id of every operation, because the order of the operations gets scrambled during the binary search
    };
    
    Opt q[N], q1[N], q2[N];
    // q holds all operations,
    // during the binary search the operations classified to the left are stored in q1, those classified to the right in q2.
    int ans[N];
    void add(int p, int x);
    int query(int p);  // Fenwick tree functions, see Problem 3 for their meaning
    
    void solve(int l, int r, int L, int R)
    // the current value range is [l,r], the interval of processed operations is [L,R]
    {
      if (l > r || L > R) return;
      int cnt1 = 0, cnt2 = 0, m = (l + r) / 2;
      // cnt1, cnt2 are the numbers of operations classified to the left and to the right, respectively
      if (l == r) {
        for (int i = L; i <= R; i++)
          if (q[i].type == 1) ans[q[i].id] = l;
        return;
      }
      for (int i = L; i <= R; i++)
        if (q[i].type == 1) {  // it is a query: classify
          int t = query(q[i].y) - query(q[i].x - 1);
          if (q[i].k <= t)
            q1[++cnt1] = q[i];
          else
            q[i].k -= t, q2[++cnt2] = q[i];
        } else
          // it is an update: update the Fenwick tree & classify
          if (q[i].y <= m)
            add(q[i].x, q[i].k), q1[++cnt1] = q[i];
          else
            q2[++cnt2] = q[i];
      for (int i = 1; i <= cnt1; i++)
        if (q1[i].type == 0) add(q1[i].x, -q1[i].k);  // clear the Fenwick tree
      for (int i = 1; i <= cnt1; i++) q[L + i - 1] = q1[i];
      for (int i = 1; i <= cnt2; i++)
        q[L + cnt1 + i - 1] = q2[i];  // merge the elements of the temporary arrays back into the original array
      solve(l, m, L, L + cnt1 - 1), solve(m + 1, r, L + cnt1, R);
      return;
    }
    ```

### Optimization for static sequences

???+ note "Problem 5 ([【模板】可持久化线段树 2 (Template: Persistent Segment Tree 2)](https://www.luogu.com.cn/problem/P3834))"
    Given a sequence, answer range queries for the $k$-th smallest.

??? note "Solution"
    Both tree-in-tree structures and parallel binary search solve the $k$-th smallest in a range with updates in $O(n \log^2 n)$, but the static $k$-th smallest in a range can be solved with a persistent segment tree in $O(n \log n)$ time, while almost all parallel binary search implementations of the static $k$-th smallest in a range have time complexity $O(n \log^2 n)$ and risk TLE on large inputs. (Here it is assumed that the value range is of the same order as the length of the sequence; the case where the value range and the sequence length are not of the same order can be reduced to the same-order case by discretization.)
    
    **Optimizations**
    
    1.  In every round of splitting, if there are $t$ numbers less than or equal to $mid$ in the current sequence, then after the split a query actually asks for the $k - t$-th smallest number in the right interval, so the queries split into the right interval are modified. If the original value range of the answers is $[L,R]$ and the value range of the answers in some split is $[l,r]$, then for the queries participating in this split the influence of all values in $[L,l)$ on them has already been eliminated earlier.
    2.  Since every round of splitting has to depend only on the current value range of the answers $[l,r]$, the Fenwick tree has to be loaded and cleared many times.
    
    What if the split depends not only on the current value range of the answers?
    
    From this we obtain an optimization related to the global sequence: maintain a pointer $pos$ that tracks the $mid$ (the center of the division) of every round of splitting, set the indices in the Fenwick tree corresponding to all elements $\leq pos$ to $1$, and the remaining positions of the Fenwick tree to $0$. Before every split, move $pos$ and update the Fenwick tree. The number of moves of the pointer $pos$ is of the same order as $n \log n$. During a split, for every query we query the value of the corresponding range in the Fenwick tree; if the condition holds, the query is split into the left interval, otherwise into the right one, and **the queries do not need to be modified**.

    Since the center of the division is tracked, $pos$ has to update the Fenwick tree precisely. Before the parallel binary search, sort the sequence by element value and record the index of every element; when the pointer moves, modify the corresponding indices in the Fenwick tree. For the vast majority of **problems that can be solved by parallel binary search and have no updates**, this optimization can be applied to greatly reduce the number of uses of the data structure.
    
    Since many load and clear operations of the Fenwick tree are eliminated, applying this optimization usually improves the efficiency of parallel binary search noticeably (even though it is only a constant factor optimization), and for the static $k$-th smallest in a range the efficiency is no worse than that of the persistent segment tree with the better time complexity. It is worth noting that for the static $k$-th smallest in a range there also exists a parallel binary search implementation with time complexity $O(n \log n)$.

??? note "Reference code (key part)"
    ```cpp
    struct Query {
      int i, l, r, k;
    };  // the i-th query asks for the k-th smallest value in the range [l,r]
    
    Query s[200005], t1[200005], t2[200005];
    int n, m, cnt, pos, p[200005], ans[200005];
    pair<int, int> a[200005];
    
    void add(int x, int y);  // Fenwick tree: add y at position x
    int sum(int x);          // Fenwick tree: prefix sum over [1,x]
    
    // the currently processed queries are [l,r], the value range of the answers is [ql,qr]
    void overall_binary(int l, int r, int ql, int qr) {
      if (l > r) return;
      if (ql == qr) {
        for (int i = l; i <= r; i++) ans[s[i].i] = ql;
        return;
      }
      int cnt1 = 0, cnt2 = 0, mid = (ql + qr) >> 1;
      // track the center of the division; the values [1,pos] are considered loaded into the Fenwick tree
      while (pos <= n - 1 && a[pos + 1].first <= mid)
        add(a[pos + 1].second, 1), ++pos;
      while (pos >= 1 && a[pos].first > mid) add(a[pos].second, -1), --pos;
    
      for (int i = l; i <= r; i++) {
        int now = sum(s[i].r) - sum(s[i].l - 1);
        if (s[i].k <= now)
          t1[++cnt1] = s[i];
        else
          t2[++cnt2] = s[i];  // note: the query information should not be modified
      }
      for (int i = 1; i <= cnt1; i++) s[l + i - 1] = t1[i];
      for (int i = 1; i <= cnt2; i++) s[l + cnt1 + i - 1] = t2[i];
    
      overall_binary(l, l + cnt1 - 1, ql, mid);
      overall_binary(l + cnt1, r, mid + 1, qr);
    }
    
    int main() {
      scanf("%d%d", &n, &m);
      for (int i = 1; i <= n; i++) {
        scanf("%d", &a[i].first);
        a[i].second = i;
        p[++cnt] = a[i].first;
      }
      sort(a + 1, a + n + 1);  // sort the sequence, discretization
      sort(p + 1, p + n + 1);
      cnt = unique(p + 1, p + n + 1) - p - 1;
      for (int i = 1; i <= n; i++)
        a[i].first = lower_bound(p + 1, p + cnt + 1, a[i].first) - p;
      // reading the queries is omitted
      overall_binary(1, m, 1, cnt);
      for (int i = 1; i <= n; i++) printf("%d\n", p[ans[i]]);
      return 0;
    }
    ```

### Predecessor and successor in a range

???+ note "Problem 6"
    In a sequence, query many times the predecessor of $k$ in a range (the largest number strictly less than $k$) or its successor (the smallest number strictly greater than $k$); it is guaranteed that such a number exists.

??? note "Solution"
    Take the predecessor as an example: the usual way to solve such problems with data structures is to first query how many numbers in the range are strictly less than $k$ (let their count be $x$), and then query the $x$-th smallest number in the range. For the successor, query how many numbers in the range are not greater than $k$ (count $x$), and then query the $x+1$-th smallest number in the range.
    
    Consider solving this problem with parallel binary search: parallel binary search is an efficient offline algorithm for the $k$-th smallest in a range, while [CDQ divide and conquer](./cdq-divide.md) can efficiently compute ranks within a range offline. First run CDQ divide and conquer once to compute the ranks, and then parallel binary search gives the predecessor and successor within the range.
    
    This problem can also be solved offline in one pass with CDQ divide and conquer combined with a segment tree, but the efficiency is far lower than the two passes of CDQ divide and conquer + parallel binary search.

### Constructing a monotonic sequence

???+ note "Problem 7 ([Sequence](https://www.luogu.com.cn/problem/P4597))"
    Given a sequence, each operation can change some number by $+1$ or $−1$. The sequence has to be made non-decreasing, and only numbers that existed before the modifications may appear in the modified sequence; output the minimum number of operations.

??? note "Solution"
    Problems of this kind can also be solved with dynamic programming or regret greedy.
    
    Under the condition of minimizing the number of operations, there always exists a solution in which every number of the final sequence existed in the sequence before the modifications; this claim can be proved by mathematical induction. Since the problem does not need information about the final sequence, the problem is reduced to finding the minimum number of operations.
    
    Since the final sequence has to be non-decreasing, parallel binary search can be used. In every round of parallel binary search we determine the value range of the range $[l,r]$ of the final sequence, where the value range of the answers is $[ql,qr]$. Let $mid=\lfloor\frac{ql + qr}{2}\rfloor$; at the start of every round all numbers are by default split into $[mid+1,qr]$ (the number of elements to be split into $[ql,mid]$ is set to $0$), and the initial cost is set to the number of operations needed to set the whole range $[l,r]$ of the sequence to $mid+1$. Enumerate the numbers $i$ in the range $[l,r]$ in turn and compute the total number of operations to set $[l,i]$ to $mid$ and $[i+1,r]$ to $mid+1$; if it is better than the previous number of operations, update the minimum number of operations and the number of elements to be split into $[ql,mid]$.
    
    The split already guarantees that the monotonicity of the final sequence is not broken, and since the minimum number of operations is taken every time, for the numbers finally split into the left interval taking $mid$ is certainly better than taking $mid+1$, so the sequence obtained by parallel binary search is certainly non-decreasing with the minimum number of operations. It remains to compute the number of operations and output it.

??? note "Reference code (key part)"
    ```cpp
    int a[500005], ans[500005];  // a: original sequence, ans: constructed sequence
    
    void overall_binary(int l, int r, int ql, int qr) {
      if (l > r) return;
      if (ql == qr) {
        for (int i = l; i <= r; i++) ans[i] = ql;
        return;
      }
      int cnt = 0,
          mid = ql + ((qr - ql) >> 1);  // by default start by filling everything with mid+1 and splitting all into the right interval
      long long res = 0ll, sum = 0ll;
      for (int i = l; i <= r; i++) sum += abs(a[i] - (mid + 1));
      res = sum;
      for (int i = l; i <= r;
           i++) {  // try changing [l,i] from mid+1 to mid and splitting it into the left interval
        sum -= abs(a[i] - (mid + 1));
        sum += abs(a[i] - mid);
        if (sum < res) cnt = i - l + 1, res = sum;  // taking mid on [l,i] is better, update
      }
      overall_binary(l, l + cnt - 1, ql, mid);
      overall_binary(l + cnt, r, mid + 1, qr);
    }
    ```

### Practice problems

-   [“国家集训队” 矩阵乘法 (National Training Team: Matrix Multiplication)](https://www.luogu.com.cn/problem/P1527)
-   [“POI2011 R3 Day2” 流星 Meteors](https://loj.ac/p/2169)
-   [二逼平衡树 (two-level balanced tree, tree-in-tree)](https://loj.ac/p/106)
-   [\[BalticOI 2004\] Sequence 数字序列 (Number Sequence)](https://www.luogu.com.cn/problem/P4331)

## References and notes

-   Xu Haoran (许昊然). 浅谈数据结构题的几个非经典解法 (A brief discussion of several non-classical solutions to data structure problems). [2013 年信息学奥林匹克中国国家队侯选队员论文集 (Collected papers of the candidates for the Chinese national team for the Olympiad in Informatics 2013)](https://github.com/OI-wiki/libs/blob/master/%E9%9B%86%E8%AE%AD%E9%98%9F%E5%8E%86%E5%B9%B4%E8%AE%BA%E6%96%87/%E5%9B%BD%E5%AE%B6%E9%9B%86%E8%AE%AD%E9%98%9F2013%E8%AE%BA%E6%96%87%E9%9B%86.pdf).

[^ref1]: Xu Haoran (许昊然). 浅谈数据结构题的几个非经典解法 (A brief discussion of several non-classical solutions to data structure problems). [2013 年信息学奥林匹克中国国家队侯选队员论文集 (Collected papers of the candidates for the Chinese national team for the Olympiad in Informatics 2013)](https://github.com/OI-wiki/libs/blob/master/%E9%9B%86%E8%AE%AD%E9%98%9F%E5%8E%86%E5%B9%B4%E8%AE%BA%E6%96%87/%E5%9B%BD%E5%AE%B6%E9%9B%86%E8%AE%AD%E9%98%9F2013%E8%AE%BA%E6%96%87%E9%9B%86.pdf).
