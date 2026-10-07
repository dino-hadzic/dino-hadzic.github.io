---
title: Queue
---

This page introduces queue-related data structures and their applications.

![](./images/queue.svg)

## Introduction

A queue is a list with the property that an element entering the queue earlier must leave it earlier. It is therefore also called a first-in, first-out (FIFO) list.

## Implementation

### Implementing a queue with an array

A queue is commonly simulated with an array and two variables marking its front and back.

```cpp
int q[SIZE], ql = 1, qr;
```

The queue operations correspond to the following code:

-   Insert an element: `q[++qr] = x;`
-   Remove an element: `ql++;`
-   Access the front: `q[ql]`
-   Access the back: `q[qr]`
-   Clear the queue: `ql = 1; qr = 0;`

??? example "[Luogu B3616: Queue (template)](https://www.luogu.com.cn/problem/B3616) — array implementation"
    ```cpp
    --8<-- "docs/ds/code/queue/queue_1.cpp"
    ```

### Implementing a queue with two stacks

A less common method simulates a queue using two [stacks](./stack.md).

Use two stacks, $F$ and $S$, where $F$ represents the back of the queue and $S$ represents the front. Support push (insert at the back) and pop (remove from the front) as follows:

-   push: insert into stack $F$.
-   pop: if $S$ is nonempty, pop from $S$. Otherwise, transfer the elements of $F$ to $S$ in reverse order (pop and push one by one, reversing the order), then pop from $S$.

Each element is inserted, transferred, and removed only once, so the amortized complexity is $O(1)$.

??? example "[Luogu B3616: Queue (template)](https://www.luogu.com.cn/problem/B3616) — two-stack implementation"
    ```cpp
    --8<-- "docs/ds/code/queue/queue_2.cpp"
    ```

## Queues in the C++ STL

The C++ STL provides the container `std::queue`. Include the `<queue>` header before using it.

???+ info "Definition of `queue` in the STL"
    ```cpp
    // clang-format off
    template<
        class T,
        class Container = std::deque<T>
    > class queue;
    ```
    
    `T` is the type of data stored in the queue.
    
    `Container` is the type of the underlying container used to store elements. It must provide the following functions with their usual semantics:
    
    -   `back()`
    -   `front()`
    -   `push_back()`
    -   `pop_front()`
    
    The STL containers `std::deque` and `std::list` satisfy these requirements. If not specified, the underlying container defaults to `std::deque`.

The STL `queue` container provides several member functions. Commonly used ones include:

-   Element access
    -   `q.front()` returns the front element
    -   `q.back()` returns the back element
-   Modifiers
    -   `q.push()` inserts an element at the back
    -   `q.pop()` removes the front element
-   Capacity
    -   `q.empty()` returns whether the queue is empty
    -   `q.size()` returns the number of elements in the queue

The container `queue` also provides several operators. One commonly used operator is assignment `=`, as in this example:

```cpp
std::queue<int> q1, q2;

// Insert 1 at the back of q1
q1.push(1);

// Assign q1 to q2
q2 = q1;

// Print the front element of q2
std::cout << q2.front() << std::endl;
// Output: 1
```

## Special queues

### Double-ended queues

A double-ended queue, or deque, allows insertion and removal at both the front and the back. It combines the functionality of a stack and a queue. Specifically, it supports four operations:

-   Insert an element at the front
-   Insert an element at the back
-   Remove an element from the front
-   Remove an element from the back

Simulating a deque with an array works in the same way as for an ordinary queue.

A deque can also be maintained with the two-stack approach. However, when one stack is empty, alternating queries to the front and back invalidate the amortized analysis. Instead, move only half the elements of the nonempty stack to the empty one, preserving the roles of the front and back stacks. This still gives amortized constant-time insertion and removal.

??? note "Proof sketch"
    Insertion contributes only constant time, so consider removal. Suppose the queue initially contains $m$ elements. We compute the time needed to remove all of them, from either end. The first rebalancing takes $O(m)$ time, after which each stack contains $\frac{m}{2}$ elements. Emptying one stack then takes $O(\frac{m}{2})$ time and triggers another rebalancing taking $O(\frac{m}{2})$ time, and so on until all elements are removed. The total complexity is therefore
    
    $$
    T(m)=T\left(\frac{m}{2}\right)+O(m)
    $$
    
    By the master theorem, $T(m)=O(m)$. Thus this approach still has amortized constant-time complexity.

??? example "[Luogu B3656: Deque 1 (template)](https://www.luogu.com.cn/problem/B3656) — reference implementation"
    ```cpp
    --8<-- "docs/ds/code/queue/queue_3.cpp"
    ```

#### Deques in the C++ STL

The C++ STL also provides the container `std::deque`. Include the `<deque>` header before using it.

??? info "Definition of `deque` in the STL"
    ```cpp
    // clang-format off
    template<
        class T,
        class Allocator = std::allocator<T>
    > class deque;
    ```
    
    `T` is the type of data stored in the deque.
    
    `Allocator` is the allocator. We do not discuss it further here; the default is usually sufficient.

The STL `deque` container provides several member functions. Commonly used ones include:

-   Element access
    -   `q.front()` returns the front element
    -   `q.back()` returns the back element
-   Modifiers
    -   `q.push_back()` inserts an element at the back
    -   `q.pop_back()` removes the back element
    -   `q.push_front()` inserts an element at the front
    -   `q.pop_front()` removes the front element
    -   `q.insert()` inserts an element before a specified position (pass an iterator and the element)
    -   `q.erase()` removes the element at a specified position (pass an iterator)
-   Capacity
    -   `q.empty()` returns whether the deque is empty
    -   `q.size()` returns the number of elements in the deque

The container `deque` also provides several operators. Commonly used ones include:

-   Assignment `=` assigns a value to a `deque`, as with `queue`.
-   `[]` accesses elements, as with `vector`.

The `<queue>` header also provides the priority queue `std::priority_queue`. Since it is more closely related to a [heap](./heap.md), we do not discuss it further here.

#### Deques in Python

In Python, `collections.deque` provides a deque container.

For example:

???+ note "Implementation"
    ```python
    from collections import deque
    
    # Create a deque initialized with [1, 2, 3]
    queue = deque([1, 2, 3])
    
    # Insert 4 at the back
    queue.append(4)
    
    # Insert 0 at the front
    queue.appendleft(0)
    
    # Access the queue
    # >>> queue
    # deque([0, 1, 2, 3, 4])
    ```

### Circular queues

Simulating a queue with an array creates a problem: over time, the entire queue moves toward the end of the array. Once it reaches the end, another insertion overflows even if there is free space at the beginning. This overflow despite available space is called "false overflow".

To avoid false overflow, organize the array circularly, treating index 0 as the successor of the last position. The successor of index `x` is `(x + 1) % SIZE`. This forms a circular queue.

## References

1.  [std::queue - zh.cppreference.com](https://zh.cppreference.com/w/cpp/container/queue)
2.  [std::deque - zh.cppreference.com](https://zh.cppreference.com/w/cpp/container/deque)
