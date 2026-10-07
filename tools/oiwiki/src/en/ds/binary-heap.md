---
title: Binary heap
---

## Structure

Let us start with the structure of a binary heap: it is a binary tree, and moreover a complete binary tree, where every node stores one element (or, put differently, has a weight).

Heap property: the weight of a parent is not less than the weight of its children (max-heap). Similarly we can define a min-heap. This article uses the max-heap as the example.

By the heap property the root holds the maximum (so the getmax operation is solved).

## Procedures

### Insertion

Insertion means inserting an element into the binary heap while guaranteeing that it is still a complete binary tree afterwards.

The simplest way is to insert after the rightmost leaf of the bottom level.

If the bottom level is full, add a new level.

After the insertion the heap property might be violated?

**Sift up**: if the weight of this node is greater than the weight of its parent, swap them, and repeat this process until the condition fails or the root is reached.

It can be proved that after inserting and sifting up, no other node violates the heap property.

The time complexity of sifting up is $O(\log n)$.

![Insertion into a binary heap](./images/binary_heap_insert.svg)

### Deletion

Deletion means removing the largest element of the heap, i.e. deleting the root.

But if we delete it directly, we get two heaps, which is hard to handle.

So consider the reverse of insertion: try to move the root to the position of the last node and then simply delete it.

In practice this is not easy to do, so the usual method is to directly swap the root with the last node.

Then we directly delete the root (now at the position of the last node), but the new root may not satisfy the heap property...

**Sift down**: among the children of this node find the largest one, swap it with the node, and repeat this process down to the bottom level.

It can be proved that after deleting and sifting down, no other node violates the heap property.

Time complexity $O(\log n)$.

### Increasing the weight of a node

Obviously, after modifying it directly, one sift up suffices; the time complexity is $O(\log n)$.

## Implementation

We notice that the operations introduced above rely mainly on two cores: sift up and sift down.

Consider representing the heap by a sequence $h$. The two children of $h_i$ are $h_{2i}$ and $h_{2i+1}$, and $1$ is the root:

![Heap structure of h](./images/binary-heap-array.svg)

Reference code:

```cpp
void up(int x) {
  while (x > 1 && h[x] > h[x / 2]) {
    std::swap(h[x], h[x / 2]);
    x /= 2;
  }
}

void down(int x) {
  while (x * 2 <= n) {
    t = x * 2;
    if (t + 1 <= n && h[t + 1] > h[t]) t++;
    if (h[t] <= h[x]) break;
    std::swap(h[x], h[t]);
    x = t;
  }
}
```

### Building a heap

Consider the following problem: starting from an empty heap, insert $n$ elements, order irrelevant.

Inserting them one by one takes $O(n \log n)$ time; is there a better way?

#### Method 1: sift up

Start from the root and proceed in BFS order.

```cpp
void build_heap_1() {
  for (i = 1; i <= n; i++) up(i);
}
```

This approach is still equivalent to inserting one by one; the elements are merely placed in the array in advance, which improves the constant. So in the worst case the time complexity satisfies the recurrence $T(n) = T(n - 1) + \Theta(\log n)$, which sums to $T(n) = \Theta(n \log n)$.

#### Method 2: sift down

Now change the approach: start from the leaves and sift down one by one.

```cpp
void build_heap_2() {
  for (i = n; i >= 1; i--) down(i);
}
```

Another way to see it: each step "merges" two already adjusted heaps, which shows correctness.

Note that leaves need no adjustment, so we can start from about position $n/2$ of the sequence, which improves the constant. Using the interpretation of merging two heaps each time, we can write the recurrence $T(n) = 2T(\dfrac{n}{2}) + O(\log n)$ for the time complexity, and by the master theorem $T(n) = \Theta(n)$.

The reason a heap can be built in $\Theta(n)$ is that the heap property is very weak: a binary heap is not unique.

With a strong condition like sortedness this would not be possible.

## Applications

### Dual heap

??? note "[SPOJ RMID2 - Running Median Again](https://www.spoj.com/problems/RMID2/)"
    Maintain a sequence supporting two operations:
    
    1.  insert an element into the sequence
    2.  output and delete the current median of the sequence (if the length of the sequence is even, output the smaller median)

This problem can be further abstracted as: dynamically maintain the $k$-th largest number in a sequence, where the value of $k$ may change.

For this kind of problem we can use the **dual heap** (two heaps) technique (which avoids the hassle of writing a segment tree over values or a BST).

A dual heap consists of a max-heap and a min-heap: the min-heap maintains the large values, i.e. the $k$ largest values (including the $k$-th), and the max-heap maintains the small values, i.e. the other numbers smaller than the $k$-th largest.

The data structure formed by these two heaps supports the following operations:

-   maintenance: while the size of the min-heap is less than $k$, repeatedly take the top of the max-heap and insert it into the min-heap until the size of the min-heap equals $k$; while the size of the min-heap is greater than $k$, repeatedly take the top of the min-heap and insert it into the max-heap until the size of the min-heap equals $k$;
-   insert an element: if the inserted element is greater than or equal to the top of the min-heap, insert it into the min-heap, otherwise insert it into the max-heap, then maintain the dual heap;
-   query the $k$-th largest element: the top of the min-heap is the answer;
-   delete the $k$-th largest element: delete the top of the min-heap, then maintain the dual heap;
-   $k$ $+1/-1$: maintain the dual heap directly according to the new value of $k$.

Obviously, querying the $k$-th largest element takes $O(1)$. Since after an insertion, deletion or change of $k$ the size of the min-heap differs from the desired $k$ by at most $1$, each maintenance needs at most one adjustment of elements between the max-heap and the min-heap, so all these operations take $O(\log n)$.

??? note "Reference code"
    ```cpp
    --8<-- "docs/ds/code/binary-heap/binary-heap_1.cpp"
    ```

### Exercises

-   [SPOJ RMID - Running Median](https://www.spoj.com/problems/RMID)
-   [Luogu P1801 Black Box](https://www.luogu.com.cn/problem/P1801)
