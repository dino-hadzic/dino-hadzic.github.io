---
title: Quick sort
---

This page briefly introduces quicksort.

## Definition

**Quicksort**, also known as partition-exchange sort, is a widely used sorting algorithm.

## Basic idea and implementation

### Procedure

Quicksort sorts an array by [divide and conquer](./divide-and-conquer.md).

Quicksort consists of three steps:

1.  split the sequence into two parts (while guaranteeing the relative order of magnitudes);
2.  recursively quicksort the two subsequences;
3.  no merging is needed, because the sequence is already completely sorted.

Unlike merge sort, the first step does not simply split the sequence into a front and a back half; the split has to preserve the relative order of magnitudes. Specifically, the first step splits the sequence into two parts such that no number in the first subsequence is larger than any number in the second. To guarantee the average time complexity, a number $m$ is usually chosen at random as the boundary between the two subsequences.

Then we maintain two pointers, a front one $p$ and a back one $q$, and check in turn whether the current number is on the side where it should be (front or back). If it is not – for example, if the back pointer $q$ meets a number smaller than $m$ – we can swap the numbers at positions $p$ and $q$ and move $p$ one step forward. Once the current numbers are all in place, we move the pointers and continue until they meet.

In fact, quicksort does not specify how exactly the first step is implemented; both the choice of $m$ and the partitioning have more than one implementation.

In the third step the sequences are already sorted and no number in the first is larger than any number in the second, so we simply concatenate them.

Below are basic implementations with a fixed pivot choice: the non-recursive C++ implementation picks the last element of the current subarray, while the recursive C++ and Python implementations pick the first element. They do not randomise the pivot, so on sorted input and similar cases they may degrade to $O(n^2)$.

=== "C++"
    === " Non-recursive implementation[^ref2]"
        ```cpp
        --8<-- "docs/basic/code/quick-sort/quick-sort_1.cpp:sort"
        ```
    
    === "Recursive implementation"
        ```cpp
        --8<-- "docs/basic/code/quick-sort/quick-sort_2.cpp:sort"
        ```

=== "Python[^ref2]"
    ```python
    --8<-- "docs/basic/code/quick-sort/quick-sort_2.py:sort"
    ```

## Properties

### Stability

Quicksort is an unstable sorting algorithm.

### Time complexity

The best-case and average time complexity of quicksort is $O(n\log n)$, and the worst case is $O(n^2)$.

In the best case every chosen pivot is the median of the sequence; the time complexity then satisfies the recurrence $T(n) = 2T(\dfrac{n}{2}) + \Theta(n)$, and by the master theorem $T(n) = \Theta(n\log n)$.

In the worst case every chosen pivot is the minimum or maximum of the sequence; the time complexity then satisfies $T(n) = T(n - 1) + \Theta(n)$, and summing gives $T(n) = \Theta(n^2)$.

The expected-case analysis below assumes that the keys are pairwise distinct and that the pivot is chosen uniformly at random from the current subarray each time.

??? note "Proof"
    We now prove that in this case the time complexity of the algorithm is $O(n\log n)$.
    
    **Lemma 1.** When quicksorting an array of $n$ elements, if $X$ is the number of distinct pairs of elements that were compared during partitioning, the time complexity of quicksort is $O(n + X)$.
    
    Each partitioning step chooses one element as the pivot, so partitioning happens at most $n$ times. Since each pair of elements is compared only a constant number of times during partitioning, and the amount of comparison work is of the same order as the other basic operations, the total time complexity is $O(n + X)$.
    
    Let $a_i$ be the $i$-th smallest number of the original array, define $A_{i,j} = \{ a_i, a_{i+1}, \dots, a_j \}$, and let $X_{i,j}$ be a discrete random variable taking the value $0$ or $1$ that indicates whether $a_i$ and $a_j$ are compared during sorting.
    
    Clearly the chosen pivots are all distinct, and elements are compared only with the pivot, so the number of distinct compared pairs is
    
    $$
    \begin{aligned} X = \sum \limits _ {i = 1} ^ {n - 1} \sum \limits _ {j = i + 1} ^ n X_{i,j} \end{aligned}
    $$
    
    By linearity of expectation,
    
    $$
    \begin{aligned} E[X] & = E \left[ \sum \limits _ {i = 1} ^ {n - 1} \sum \limits _ {j = i + 1} ^ n X_{i,j} \right] \\ & = \sum \limits _ {i = 1} ^ {n - 1} \sum \limits _ {j = i + 1} ^ n E[X_{i,j}] \\ & = \sum \limits _ {i = 1} ^ {n - 1} \sum \limits _ {j = i + 1} ^ n P(a_i\ \text{and}\ a_j\ \text{are compared}) \end{aligned}
    $$
    
    **Lemma 2.** $a_i$ and $a_j$ are compared if and only if $a_i$ or $a_j$ is the first element of the set $A_{i,j}$ chosen as a pivot.
    
    First necessity: if neither $a_i$ nor $a_j$ is the first pivot chosen from $A_{i,j}$, then $a_i$ and $a_j$ are not compared.
    
    If neither $a_i$ nor $a_j$ is the first pivot chosen from $A_{i,j}$, there must exist an $x$ with $i < x < j$ such that $a_x$ is the first pivot chosen from $A_{i,j}$. In the partition with pivot $a_x$, $a_i$ and $a_j$ are placed into two different subsequences of the array, so afterwards they are certainly never compared. And since elements are only compared with the pivot, $a_i$ and $a_j$ were not compared before or during this partition either. Hence $a_i$ and $a_j$ are not compared.
    
    Now sufficiency: if $a_i$ or $a_j$ is the first pivot chosen from $A_{i,j}$, then $a_i$ and $a_j$ are compared.
    
    Without loss of generality assume $a_i$ is the first pivot chosen from $A_{i,j}$. Since no other element of $A_{i,j}$ has been chosen as a pivot, all elements of $A_{i,j}$ are in the same subsequence of the array. In the partition with pivot $a_i$, $a_i$ is compared with every element of the current subsequence, so $a_i$ and $a_j$ are compared.
    
    Now compute $P(a_i\ \text{and}\ a_j\ \text{are compared})$. Before any element of $A_{i,j}$ is chosen as a pivot, all elements of $A_{i,j}$ are in the same subsequence of the array. Hence every element of $A_{i,j}$ is equally likely to be the first one chosen as a pivot. Since $A_{i,j}$ has $j - i + 1$ elements, by Lemma 2,
    
    $$
    P(a_i \text{ and } a_j \text{ are compared}) = P(a_i \text{ or } a_j \text{ is the first pivot chosen from the set } A_{i,j}) = \dfrac{2}{j-i+1}
    $$
    
    Therefore
    
    $$
    \begin{aligned} E[X] & = \sum \limits _ {i = 1} ^ {n - 1} \sum \limits _ {j = i + 1} ^ n P(a_i\ \text{and}\ a_j\ \text{are compared}) \\ & = \sum \limits _ {i = 1} ^ {n - 1} \sum \limits _ {j = i + 1} ^ n \dfrac{2}{j - i + 1} \\ & = \sum \limits _ {i = 1} ^ {n - 1} \sum \limits _ {k = 2} ^ {n - i + 1} \dfrac{2}{k} \\ & = \sum \limits _ {i = 1} ^ {n - 1} O(\log n) \\ & = O(n \log n) \end{aligned}
    $$
    
    Hence the expected time complexity of quicksort is $O(n \log n)$.

Choosing the pivot at random lowers the probability of hitting the worst partition. In addition, quicksort's memory accesses follow the principle of locality, which helps it perform well in practice.[^ref1]

## Optimisations

### Simple optimisation ideas

If quicksort is implemented purely according to the basic idea described above (or by copying a template), it usually cannot pass the template problem [P1177 【模板】快速排序](https://www.luogu.com.cn/problem/P1177), because test data can be constructed that makes naive quicksort degrade to $O(n^2)$.

Therefore the naive quicksort idea needs to be optimised. The three most common ideas are[^ref3]:

-   Choose the boundary element (the comparison pivot) by **median-of-three (the median of the first, last and middle elements)**. This avoids degradation on extreme data (such as ascending or descending sequences).
-   When the sequence is short, **insertion sort** is more efficient.
-   After each pass, **gather the elements equal to the pivot around the pivot**; this avoids degradation on extreme data (such as sequences where most elements are equal).

Below are several mature ways of optimising quicksort.

### 3-way quicksort

#### Definition

**3-way quicksort** splits the elements into three parts according to their relation to the pivot. Its idea is based on the solution of the [Dutch national flag problem](https://en.wikipedia.org/wiki/Dutch_national_flag_problem).

#### Procedure

Unlike the original quicksort, after randomly choosing the pivot $m$, 3-way quicksort splits the sequence to be sorted into three parts: less than $m$, equal to $m$ and greater than $m$. This achieves exactly the effect of gathering the elements equal to the pivot around the pivot.

#### Properties

When processing arrays with many duplicate values, 3-way quicksort is far more efficient than the original quicksort. Its best-case time complexity is $O(n)$.

#### Implementation

3-way quicksort is very easy to implement; a reference implementation is given below.

=== "C++"
    ```cpp
    --8<-- "docs/basic/code/quick-sort/quick-sort_3.cpp:sort"
    ```

=== "Python[^ref2]"
    ```python
    --8<-- "docs/basic/code/quick-sort/quick-sort_3.py:sort"
    ```

### Introsort

#### Definition

**Introsort** (introspective sort)[^ref4] is a combination of quicksort and [heap sort](./heap-sort.md), invented by David Musser in 1997. Introsort is really an optimisation of quicksort that guarantees a worst-case time complexity of $O(n\log n)$.

#### Properties

Introsort limits the partitioning depth of quicksort, usually to $2\lfloor \log_2n \rfloor$[^ref5], and switches to heap sort when the limit is exceeded. This keeps the locality of quicksort's memory accesses while preventing it from degrading to $O(n^2)$ in some cases.

#### Implementation

Since June 2000, the implementation of the `sort()` function in `stl_algo.h` of the SGI C++ STL has used introsort.

## Finding the k-th smallest element in linear time

In the code examples below, the element with ascending index $k$ is defined as the element at position $k$ (0-based) when the sequence is sorted in ascending order.

The simplest way to find the $k$-th smallest element (the $k$-th order statistic) is to sort first and then take the element at position $k$. This takes $O(n\log n)$, which is wasteful for this problem.

We can use the idea of quicksort to solve it. Consider the partitioning step of quicksort: after the "partition", the sequence $A_{p} \cdots A_{r}$ is split into $A_{p} \cdots A_{q}$ and $A_{q+1} \cdots A_{r}$; now, comparing the number of elements on the left ($q - p + 1$) with $k$, we can decide to recurse only into the left or only into the right part.

As with quicksort, the time complexity of this method depends on the pivot chosen in each partition. If the pivot is chosen at random, it can be proven that the expected time complexity is $O(n)$.

???+ note "Reference implementation"
    ```cpp
    --8<-- "docs/basic/code/quick-sort/quick-sort_4.cpp:sort"
    ```

### Median of medians

**Median of medians** provides a deterministic way of choosing the pivot in the partitioning step, so that the algorithm for "finding the $k$-th smallest element" achieves linear time even in the worst case.

The algorithm proceeds as follows:

1.  split the sequence into $\lceil n/5\rceil$ groups of at most five elements, keeping a last group with fewer than five;
2.  sort each group and take its median; for even length always take the smaller median;
3.  recursively select the median of these medians as the pivot, do a 3-way partition into less than, equal to and greater than the pivot, and recurse only into the strictly-less or strictly-greater part that contains the target.

#### Proof of time complexity

Let the number of groups be $g=\lceil n/5\rceil$. On each side of the pivot (inclusive) there are at least $\lfloor g/2\rfloor$ group medians; excluding the last group, each complete group contributes at least three elements not greater than, respectively not less than, the pivot. Hence each side has at least $3n/10-O(1)$ such elements, and the strictly-less and strictly-greater parts each have size at most $7n/10+O(1)$. We do not recurse into the equal part. Grouping, finding the group medians and partitioning take $O(n)$ in total. Altogether we get the inequality

$$
T(n)\le T(\lceil n/5\rceil)+T(7n/10+O(1))+O(n).
$$

Fix constants $a,b$ such that the two recursive sizes on the right sum to at most $9n/10+a$ and the non-recursive cost is at most $bn$. For $n\ge20a$ this sum is at most $19n/20$. Under the induction hypothesis $T(m)\le cm$, it suffices to take $c\ge20b$ and enlarge $c$ to cover finitely many base cases, giving $T(n)\le19cn/20+bn\le cn$. Hence the worst-case time complexity is $O(n)$.

## References and notes

[^ref1]: [C++ 性能榨汁机之局部性原理 - I'm Root lee !](http://irootlee.com/juicer_locality/) (Chinese)

[^ref2]: [Algorithm Implementation/Sorting/Quicksort – Wikibooks (Chinese)](https://zh.wikibooks.org/wiki/%E7%AE%97%E6%B3%95%E5%AE%9E%E7%8E%B0/%E6%8E%92%E5%BA%8F/%E5%BF%AB%E9%80%9F%E6%8E%92%E5%BA%8F)

[^ref3]: [Three kinds of quicksort and quicksort optimisations (Chinese)](https://blog.csdn.net/insistGoGo/article/details/7785038)

[^ref4]: [introsort](https://en.wikipedia.org/wiki/Introsort)

[^ref5]: E.g. [libstdc++ 14.2.0: `__introsort_loop` and `__sort`](https://github.com/gcc-mirror/gcc/blob/releases/gcc-14.2.0/libstdc%2B%2B-v3/include/bits/stl_algo.h#L1876-L1908). In fact, limiting the depth to $O(\log n)$ and switching to heap sort when the limit is reached suffices to guarantee a total time complexity of $O(n\log n)$.
