---
title: Ordinary Mo's algorithm
---

## Form

Assume $n=m$. Then, for a range query problem on a sequence, if the answer for $[l,r]$ can be extended in $O(1)$ to the answer for $[l-1,r],[l+1,r],[l,r+1],[l,r-1]$ (i.e. the ranges adjacent to $[l,r]$), the answers to all queries can be computed in $O(n\sqrt{n})$.

## Explanation

Sort the queries offline, process them in order, and transfer the answer from the previous range to the next one by brute force (just move step by step).

## Sorting method

For a range $[l,r]$, sort in ascending order with the index of the block containing $l$ as the first key and $r$ as the second key.

## Implementation

```cpp
void move(int pos, int sign) {
  // update nowAns
}

void solve() {
  BLOCK_SIZE = int(ceil(pow(n, 0.5)));
  sort(querys, querys + m);
  for (int i = 0; i < m; ++i) {
    const query &q = querys[i];
    while (l > q.l) move(--l, 1);
    while (r < q.r) move(++r, 1);
    while (l < q.l) move(l++, -1);
    while (r > q.r) move(r--, -1);
    ans[q.id] = nowAns;
  }
}
```

## Complexity analysis

The following discussion assumes that $n$ and $m$ are of the same order of magnitude.

The first step is dividing into blocks; the time complexity of this step is $O(\sqrt{n}\cdot\sqrt{n}\log\sqrt{n}+n\log n)=O(n\log n)$.

Next comes the essence of Mo's algorithm; below we use a simple, middle-school-level method to prove that its time complexity is $O(n\sqrt{n})$.

???+ note "Proof"
    Proof: let the maximum values of $L$ in each block be $\max_1,\max_2,\max_3, \cdots , \max_{\lceil\sqrt{n}\rceil}$.
    
    From the first sort we know that $\max_1 \le \max_2 \le \cdots \le \max_{\lceil\sqrt{n}\rceil}$.
    
    Obviously, the time complexity of computing the first query of each block by brute force is $O(n)$.
    
    Consider the worst case: in every block the maximum value of $R$ is $n$, and every modification operation has to change $L$ from $\max_{i - 1}$ to $\max_i$ or from $\max_i$ to $\max_{i - 1}$.
    
    Consider $R$: since $R$ is already sorted within a block, the time complexity of all its modifications within one block is $O(n)$. For all blocks this is $O(n\sqrt{n})$.
    
    The key is analyzing $L$: since the time complexity of each change is $O(\max_i-\max_{i-1})$, the time complexity within one block is $O(\sqrt{n}\cdot(\max_i-\max_{i-1}))$.
    
    Adding up the time complexities of $L$ over all blocks, we get:
    
    The total time complexity for $L$ is
    
    $$
    \begin{aligned}
    & O(\sqrt{n}(\max{}_1-1)+\sqrt{n}(\max{}_2-\max{}_1)+\sqrt{n}(\max{}_3-\max{}_2)+\cdots+\sqrt{n}(\max{}_{\lceil\sqrt{n}\rceil}-\max{}_{\lceil\sqrt{n}\rceil-1))} \\
    = \phantom{} & O(\sqrt{n}\cdot(\max{}_1-1+\max{}_2-\max{}_1+\max{}_3-\max{}_2+\cdots+\max{}_{\lceil\sqrt{n}\rceil-1}-\max{}_{\lceil\sqrt{n}\rceil-2}+\max{}_{\lceil\sqrt{n}\rceil}-\max{}_{\lceil\sqrt{n}\rceil-1)}) \\
    = \phantom{} & O(\sqrt{n}\cdot(\max{}_{\lceil\sqrt{n}\rceil}-1))\\
    \end{aligned}
    $$
    
    (telescoping sum)
    
    By the problem, $\max_{\lceil\sqrt{n}\rceil}$ is at most $n$, so the total time complexity for $L$ in the worst case is $O(n\sqrt{n})$.

In summary, the time complexity of Mo's algorithm is $O(n\sqrt{n})$.

However, for other values of $m$, such as $m<n$, the way of dividing into blocks has to change in order to do better.

How should we divide into blocks?

Let the block length be $S$. Then for any number of queries within the same block, the distance moved is $n$; there are $\displaystyle \frac{n}{S}$ blocks in total, so the total number of moves is $\displaystyle \frac{n^2}{S}$; moves may cross blocks, so we also have to add a complexity of $mS$, and the total complexity is $\displaystyle O\left(\frac{n^2}{S}+mS\right)$. We want this value to be as small as possible, so the two terms should be as close to equal as possible; we find that taking $S$ equal to $\displaystyle \frac{n}{\sqrt{m}}$ is optimal, and the complexity is then $\displaystyle O\left(\frac{n^2}{\displaystyle \frac{n}{\sqrt{m}}}+m\left(\frac{n}{\sqrt{m}}\right)\right)=O(n\sqrt{m})$.

In fact, if the block length is set inaccurately, the time complexity of Mo's algorithm suffers greatly. For example, if $m$ is of the same order as $\sqrt n$ and the block length is mistakenly set to $\sqrt n$, it is easy to construct a test case where the time complexity is $O(n \sqrt n)$ instead of the correct $O(n^{5/4})$.

Mo's algorithm looks very brute-force, largely because its block-based sorting method looks very crude. One might think of sorting all ranges with a seemingly more refined method. One approach is to view every range $[l, r]$ as a point $(l, r)$ in the plane, build a Manhattan minimum spanning tree over all points, and transfer answers between queries along the edges of the Manhattan minimum spanning tree. This seems to improve the time complexity of Mo's algorithm, but in fact the upper bound on the time complexity of sorting the queries by blocks is already optimal.

Assume $n, m$ are of the same order and $n$ is a perfect square. Consider ranges of the form $[a \sqrt n, b \sqrt n](1 \le a, b \le \sqrt n)$; there are $n$ such ranges in total. If all ranges are viewed as points in the plane, the Manhattan distance between two points is exactly the transfer cost between the two ranges, and the minimum Manhattan distance between any two ranges is $\sqrt n$, so the time complexity of processing all queries is at least $O(n \sqrt n)$. The construction of test data in other cases is similar.

Mo's algorithm has another characteristic: when $n$ stays the same, the larger $m$ is, the smaller the average transfer cost per query becomes. Some other offline algorithms share this characteristic (such as Tarjan's algorithm for LCA), but for Mo's algorithm the average transfer cost varies most noticeably with $m$.

## Example problem & code

???+ note "Example [「国家集训队」小 Z 的袜子 (Little Z's Socks)](https://www.luogu.com.cn/problem/P1494)"
    Problem summary:
    
    There is a sequence $\{c_i\}$ of length $n$. Now $m$ queries are given; each gives two numbers $l,r$, and two different numbers are chosen at random among those with indices from $l$ to $r$; find the probability that the two numbers are equal.

### Procedure

Idea: a template problem for Mo's algorithm.

For a range $[l,r]$, sort in ascending order with the index of the block containing $l$ as the first key and $r$ as the second key.

Then compute the answers starting from the first query of the sequence; the first query is computed directly by brute force, with complexity $O(n)$, and the answers to the later queries are obtained based on the previous query.

Concrete procedure:

For a range $[i,i]$, since the range has only one element, we can easily know the answer. Then we move step by step from the current range (whose answer is known) toward the next range.

Let $col[i]$ denote how many times color $i$ currently occurs, and let $ans$ denote how many feasible pairings there currently are (in how many ways a pair of socks of the same color can be chosen). Then update the answer at each move: let the current color be $k$; if the range is being extended, add $\dbinom{col[k]+1}{2}-\dbinom{col[k]}{2}$ to $ans$; if it is being shrunk, subtract $\dbinom{col[k]}{2}-\dbinom{col[k]-1}{2}$ from $ans$. The answer to the query is $\displaystyle \frac{ans}{\dbinom{r-l+1}{2}}$.

There is an optimization here: $\displaystyle \dbinom{a}{2}=\frac{a (a-1)}{2}$.

Therefore $\displaystyle \dbinom{a+1}{2}-\dbinom{a}{2}=\frac{(a+1) a}{2}-\frac{a (a-1)}{2}=\frac{a}{2}\cdot (a+1-a+1)=\frac{a}{2}\cdot 2=a$.

So $\dbinom{col[k]+1}{2}-\dbinom{col[k]}{2}=col[k]$.

Total complexity of the algorithm: $O(n\sqrt{n} )$

In the code below, `deno` denotes the denominator of the answer, `nume` the numerator, `sqn` the block size $\sqrt{n}$, `arr` is the input array, `node` is the struct storing a query, `tab` is the sequence of queries (after sorting), and `col` is as described above.

**Note: because of `++l` and `--r`, the positions of the 4 while loops that move the range in the code below are crucial, and their relative order must not be changed arbitrarily.**

??? note "Discussion of the order of the four loops"
    The process of moving the range in Mo's algorithm is equivalent to adding the elements of $[1,r]$ and deleting the elements of $[1,l-1]$. Therefore:
    
    -   In the case $l\le r$, the elements of $[1,l-1]$ have been added once and deleted once, the elements of $[l,r]$ have been added once, and the elements of $[r+1,+\infty)$ have not been added. This range is a valid range.
    -   In the case $l=r+1$, the elements of $[1,r]$ have been added once and deleted once, and the elements of $[r+1,+\infty)$ have not been added. In this case the range represents an empty range.
    -   In the case $l>r+1$, the elements of $[r+1,l-1]$ (this range is nonempty) have been deleted once but not added, so the number of times these elements have been added is negative.
    
    Therefore, if the situation $l>r+1$ occurs at some moment, there will be an element whose number of additions is negative. This causes problems in some tasks; for example, if we maintain all numbers in the range with a `set`, the problem of "needing to delete an element that does not exist in the `set`" arises.
    
    The four while loops in the code have $4!=24$ possible orderings in total. Without loss of generality, let the first loop operate on the left endpoint; then there are the following $12$ orderings (the other $12$ are symmetric). The table below lists the correctness of these 12 variants and also gives counterexamples for the incorrect ones.
    
    | Loop order            | Correctness | Counterexample or note |
    | ----------------- | --- | ----------- |
    | `l--,l++,r--,r++` | incorrect  | $l<r<l'<r'$ |
    | `l--,l++,r++,r--` | incorrect  | $l<r<l'<r'$ |
    | `l--,r--,l++,r++` | incorrect  | $l<r<l'<r'$ |
    | `l--,r--,r++,l++` | correct  | the proof is rather tedious       |
    | `l--,r++,l++,r--` | correct  |             |
    | `l--,r++,r--,l++` | correct  |             |
    | `l++,l--,r--,r++` | incorrect  | $l<r<l'<r'$ |
    | `l++,l--,r++,r--` | incorrect  | $l<r<l'<r'$ |
    | `l++,r++,l--,r--` | incorrect  | $l<r<l'<r'$ |
    | `l++,r++,r--,l--` | incorrect  | $l<r<l'<r'$ |
    | `l++,r--,l--,r++` | incorrect  | $l<r<l'<r'$ |
    | `l++,r--,r++,l--` | incorrect  | $l<r<l'<r'$ |
    
    Of all 24 orderings only 6 are correct, and for 2 of them the proof is rather tedious; here we only give the proof for 4 of them.
    
    The common feature of these 4 correct variants is that the first two steps first extend the range (`l--` or `r++`), and the last two steps then shrink it (`l++` or `r--`). Written this way, the first two steps extend the range and can maintain $l\le r+1$; after executing the first two steps, $l\le l'\le r'\le r$ certainly holds, and executing the last two steps only shrinks the range to $[l',r']$, so $l\le r+1$ still holds; therefore this way of writing it is correct.

### Implementation

??? note "Reference code"
    ```cpp
    --8<-- "docs/misc/code/mo-algo/mo-algo_1.cpp"
    ```

## Optimization of ordinary Mo's algorithm

### Procedure

Let us look at the following test data

```text
// let the block size be 2 (assumption)
1 1
2 100
3 1
4 100
```

Simulating by hand, we find that the r pointer moves roughly 300 times; after we finish processing the first block, $l = 2, r = 100$, and at that point only two moves of the l pointer would be needed to get the answer to the fourth query, but instead we move the r pointer to 1 to get the answer to the third query and then move it to 100 to get the answer to the fourth query, which is ninety-odd extra pointer moves. How do we optimize this? Here we use odd-even sorting.

What is odd-even sorting? Odd-even sorting means that for queries belonging to odd-numbered blocks, r is sorted in ascending order, and for queries belonging to even-numbered blocks, r is sorted in descending order; this way, after our r pointer finishes the queries of an odd block, it processes the queries of the even block on its way back, and then moves toward n again to process the queries of the next odd block, which optimizes the number of moves of the r pointer. In general, this optimization makes the program about 30% faster.

### Implementation

Sorting code:

=== "Compressed"
    ```cpp
    // clang-format off
    // there is a small detail here that will be discussed below
    int unit; // block size
    struct node {
      int l, r, id;
      bool operator < (const node &x) const {
        return l / unit == x.l / unit ? (r == x.r ? 0 : ((l / unit) & 1) ^ (r < x.r)) : l < x.l;
      }
    };
    ```

=== "Expanded"
    ```cpp
    struct node {
      int l, r, id;
    
      bool operator<(const node &x) const {
        if (l / unit != x.l / unit) return l < x.l;
        // note: the following two lines must not use less-than (greater-than) or equal, otherwise an error occurs (see the small detail below)
        if ((l / unit) & 1) return r < x.r;
        return r > x.r;
      }
    };
    ```

???+ warning "Small detail"
    If `sort` is used to compare two structs, it must not happen that $a < b$ and $b < a$ are both true at the same time, otherwise a runtime error occurs; see [Common mistakes](../contest/common-mistakes.md#mistakes-that-lead-to-re).

For the compressed version, without the special check `r == x.r`, when the l values belong to the same odd block and the r values are equal, the problem from the small detail above occurs (simulate it by hand yourself); for the expanded version, the same problem occurs if less-than (greater-than) or equal is written.

## References

-   [莫队算法学习笔记 (Notes on learning Mo's algorithm) | Sengxian's Blog](https://blog.sengxian.com/algorithms/mo-s-algorithm)
