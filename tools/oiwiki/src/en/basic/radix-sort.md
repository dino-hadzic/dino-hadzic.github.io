---
title: Radix sort
---

???+ warning "Note"
    This page is not about [**counting sort**](./counting-sort.md).

This page briefly introduces radix sort.

## Definition

**Radix sort** is a non-comparison sorting algorithm, originally used to sort punched cards. Radix sort splits the elements to be sorted into $k$ keys and sorts all elements by sorting on each key in turn.

If the comparison goes from the $1$st key to the $k$-th key, the radix sort is called MSD (Most Significant Digit first) radix sort;

if the comparison goes from the $k$-th key to the $1$st key, it is called LSD (Least Significant Digit first) radix sort.

## Comparing elements with k keys

Below, $a_i$ denotes the $i$-th key of element $a$.

If the elements have $k$ keys, the default way of comparing two elements $a$ and $b$ is:

-   compare the $1$st keys $a_1$ and $b_1$: if $a_1 < b_1$ then $a < b$, if $a_1 > b_1$ then $a > b$, if $a_1 = b_1$ go to the next step;
-   compare the $2$nd keys $a_2$ and $b_2$: if $a_2 < b_2$ then $a < b$, if $a_2 > b_2$ then $a > b$, if $a_2 = b_2$ go to the next step;
-   …
-   compare the $k$-th keys $a_k$ and $b_k$: if $a_k < b_k$ then $a < b$, if $a_k > b_k$ then $a > b$, if $a_k = b_k$ then $a = b$.

Examples:

-   when comparing natural numbers, if we align them at the units digit and pad with leading $0$s, the $i$-th digit from the left can serve as the $i$-th key;
-   when comparing strings lexicographically, the $i$-th character from the left can serve as the $i$-th key;
-   the default comparison of C++'s `std::pair` and `std::tuple` is the same as described above.

## MSD radix sort

Based on the comparison of elements with $k$ keys, one idea is: first compare the $1$st keys of all elements to determine the rough order among them; then, for **elements with the same $1$st key**, compare their $2$nd keys… and so on.

Since the comparison goes from the $1$st to the $k$-th key, the sorting algorithm derived from this idea is called MSD (Most Significant Digit first) radix sort.

### Algorithm

Split the elements into $k$ keys; first sort stably by the $1$st key, then for each group of **elements with the same key** sort stably by the $2$nd key (recursively)… finally, for each group of **elements with the same key**, sort stably by the $k$-th key.

Generally we assume radix sort is stable, so in MSD radix sort we also only consider using a **stable algorithm** (usually counting sort) for the inner sort on a key.

For correctness, see the comparison of elements with $k$ keys above.

### Sample code

#### Sorting natural numbers

Below is a recursive MSD radix sort handling at most `MAXN` integers in $[0,2^{32}-1]$. Initially `digit=10`; when changing the radix, `RADIX` and `powRADIX` must be updated together.

??? example "Sample code"
    ```cpp
    --8<-- "docs/basic/code/radix-sort/radix-sort_1.cpp:core"
    ```

#### Sorting strings

Below is a recursive MSD radix sort that sorts `std::string`s containing only lowercase English letters in lexicographic order:

??? example "Sample code"
    ```cpp
    --8<-- "docs/basic/code/radix-sort/radix-sort_2.cpp:core"
    ```

Since comparing two strings easily reaches linear $O(n)$ complexity, for sorting strings MSD radix sort beats most comparison-based sorting algorithms both in time complexity and in actual running time.

### Relation to bucket sort

Prerequisite: [Bucket sort](./bucket-sort.md)

Bucket sort needs another sorting algorithm to sort the elements inside each bucket. But in fact we can simply keep applying bucket sort to each bucket until, at some step, a bucket has $\le 1$ elements.

So another way of understanding MSD radix sort is: bucket sort implemented with bucket sort.

This also suggests an optimisation of the constant factor of MSD radix sort: if at some step a bucket has $\le B$ elements ($B$ is a constant of your choice), run insertion sort directly and return, reducing the number of recursive calls.

## LSD radix sort

MSD radix sort compares from the $1$st key to the $k$-th key, which requires recursion or iteration; its constant factor is fairly large, and it is slightly inconvenient for comparing natural numbers.

Reversing the recursive procedure – comparing from the $k$-th key to the $1$st key – gives LSD (Least Significant Digit first) radix sort, a sorting algorithm that works without recursion.

### Algorithm

Split the elements into $k$ keys; then sort **all elements** stably by the $k$-th key, then sort **all elements** stably by the $(k-1)$-th key, then by the $(k-2)$-th key… finally sort **all elements** stably by the $1$st key. This completes a stable sort of the whole sequence.

![an example of a full LSD radix sort run](images/radix-sort-1.svg)

LSD radix sort also needs a **stable algorithm** for the inner sort on a key. Likewise, counting sort is usually used.

For the correctness of LSD radix sort, see [the solution of exercise 8.3-3 in *Introduction to Algorithms* (3rd ed.)](https://walkccc.github.io/CLRS/Chap08/8.3/#83-3) or the explanation below:

### Correctness

Recall the comparison of elements with $k$ keys:

-   to determine the order of $a$ and $b$ from $a_1$ and $b_1$ alone, we need to know in advance the conclusion of comparing $a_2$ and $b_2$, to handle the case $a_1 = b_1$;
-   to determine the order of $a$ and $b$ from $a_2$ and $b_2$ alone, we need to know in advance the conclusion of comparing $a_3$ and $b_3$, to handle the case $a_2 = b_2$;
-   …
-   to determine the order of $a$ and $b$ from $a_{k-1}$ and $b_{k-1}$ alone, we need to know in advance the conclusion of comparing $a_k$ and $b_k$, to handle the case $a_{k-1} = b_{k-1}$;
-   $a_k$ and $b_k$ can be compared directly.

Now reverse the order:

-   $a_k$ and $b_k$ can be compared directly;
-   knowing the conclusion of comparing $a_k$ and $b_k$, we get the conclusion of comparing $a_{k-1}$ and $b_{k-1}$;
-   …
-   knowing the conclusion of comparing $a_2$ and $b_2$, we get the conclusion of comparing $a_1$ and $b_1$;
-   knowing the conclusion of comparing $a_1$ and $b_1$, we finally get the conclusion of comparing $a$ and $b$.

Rearranging the elements as we compare each key in this process gives LSD radix sort.

### Pseudocode

$$
\begin{array}{ll}
1 & \textbf{Input. } \text{An array } A \text{ consisting of }n\text{ elements, where each element has }k\text{ keys.}\\
2 & \textbf{Output. } \text{Array }A\text{ will be sorted in nondecreasing order stably.} \\
3 & \textbf{Method. }  \\
4 & \textbf{for }i\gets k\textbf{ down to }1\\
5 & \qquad\text{sort }A\text{ into nondecreasing order by the }i\text{-th key stably}
\end{array}
$$

### Sample code

Below is a sort of elements with $k$ keys implemented with LSD radix sort.

??? example "Sample code"
    ```cpp
    --8<-- "docs/basic/code/radix-sort/radix-sort_lsd.cpp:core"
    ```

In fact, iterating from back to front is not required for stability; it suffices to perform the equivalent of `std::exclusive_scan` on the `cnt` array.

???+ note "Example [Luogu P1177【模板】排序](https://www.luogu.com.cn/problem/P1177)"
    Given $n$ positive integers, output them in increasing order.
    
    ```cpp
    --8<-- "docs/basic/code/radix-sort/radix-sort_3.cpp"
    ```

## Properties

### Stability

If the inner sort on the keys is stable, both MSD and LSD radix sort are stable sorting algorithms.

### Time complexity

Generally, radix sort is faster than comparison-based sorting algorithms (such as quicksort). But since it needs extra memory, when memory is scarce an in-place algorithm (such as quicksort) may be a better choice.[^ref1]

The time bounds below assume that extracting a single key and moving one element (or its index) each take $O(1)$ time. In general, if the range of every key is small, [counting sort](./counting-sort.md) can be used as the inner sort, and the time complexities of LSD and MSD are respectively

$$
O\left(kn+\sum_{i=1}^k w_i\right),\qquad O\left(kn+\sum_{i=1}^k b_iw_i\right),
$$

where $b_i$ is the number of buckets in which counting sort is actually run at level $i$ and $w_i$ is the size of the value range of the $i$-th key. If the key ranges are large, a comparison-based $O(nk\log n)$ sort can be used directly without radix sort.

### Space complexity

We consider the auxiliary space besides the input, assuming each element or its index takes $O(1)$ space. Using counting sort, LSD can reuse a temporary array of length $n$ and the count array, so the auxiliary space is $O(n+\max_i w_i)$. A recursive MSD that reuses the temporary array but keeps the bucket boundaries at each recursion level uses $O(n+\sum_{i=1}^k w_i)$. When the value range of each digit is fixed, these simplify to $O(n)$ and $O(n+k)$ respectively, where $k$ is the number of keys.

## References and notes

[^ref1]: Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, and Clifford Stein.*Introduction to Algorithms*(3rd ed.). MIT Press and McGraw-Hill, 2009. ISBN 978-0-262-03384-8. "8.3 Radix sort", pp. 199.
