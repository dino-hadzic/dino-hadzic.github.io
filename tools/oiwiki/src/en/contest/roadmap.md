---
title: Learning roadmap
---

???+ note "Note"
    This article is still being edited and discussed; feel free to add further learning paths or share your ideas in the comments!

This article presents a learning roadmap for algorithm competitions.

The roadmap is both a guide for beginners learning the material of algorithm competitions and a review checklist.

## 1 C++ language basics

Start with C++ syntax and take it step by step.

### 1.1 Hello, World!

Begin your journey through algorithm competitions with a `Hello, World!`

At the same time, get to know roughly what the skeleton of a C++ source program looks like.

-   [Hello, World!](../lang/helloworld.md)
-   [C++ syntax basics](../lang/basic.md)

### 1.2 Variables and operations

Computers were originally created to compute. So let us first learn how to perform some simple computational tasks.

-   [Variables](../lang/var.md)
-   [Operations](../lang/op.md)

### 1.3 Control flow

#### 1.3.1 Branching

Sometimes we need to execute different statements under different conditions; this is where branch statements come in.

-   [Branching](../lang/branch.md)

Branch statements include the following:

-   the if statement
-   the if-else statement
-   the if-elif-else statement
-   the switch statement

#### 1.3.2 Loops

To execute several statements repeatedly, we need loop statements.

-   [Loops](../lang/loop.md)

Loop statements include the following:

-   the for statement
-   the while statement
-   the do-while statement

### 1.4 Arrays and structs

Arrays store large amounts of data of the same type. Structs, on the other hand, can bundle several variables together.

-   [Arrays](../lang/array.md)
-   [Structs](../lang/struct.md)

### 1.5 Functions and recursion

Use functions to make programs modular and reduce the cost of implementation.

Recursion is the first hurdle for beginners: "a function calling itself" does not sound easy to understand, but if you look carefully at the essence, you will find that there is no fundamental difference between "calling yourself" and "calling someone else".

-   [Functions](../lang/func.md)
-   [Recursion and divide and conquer](../basic/divide-and-conquer.md)

## 2 CSP-J, entry level

### 2.1 Enumeration and simulation

By now you can already use C++ to complete some simple tasks, but that is far from enough.

To solve some simple problems correctly, you need to learn to implement code by enumerating (exhaustively trying) or simulating the logic in your head. This does not look very efficient, but sometimes it works very well.

-   [Enumeration](../basic/enumerate.md)
-   [Simulation](../basic/simulate.md)

### 2.2 Recursion and divide and conquer

Recursion is a method in which a function keeps calling itself in its own definition; divide and conquer is the process of repeatedly decomposing a problem into several subproblems, solving them and merging the results.

-   [Recursion and divide and conquer](../basic/divide-and-conquer.md)

### 2.3 Strings

A data type you often meet when solving informatics problems is the string; you need to learn some STL functions for manipulating strings. Of course, simulation is also a good way to solve string problems.

-   [String basics](../string/basic.md)
-   [STL functions](../string/lib-func.md)

### 2.4 Sorting

When you are given a set of data, how to turn it from unordered into ordered is also an important question. When you have no idea what to do, consider sorting the array. This is also the foundation of many algorithms that follow.

There are quite a few sorting methods, but once you understand them they are not hard to remember.

-   [Introduction to sorting](../basic/sort-intro.md)
-   [Selection sort](../basic/selection-sort.md)
-   [Bubble sort](../basic/bubble-sort.md)
-   [Insertion sort](../basic/insertion-sort.md)
-   [Counting sort](../basic/counting-sort.md)
-   [Radix sort](../basic/radix-sort.md)
-   [Quick sort](../basic/quick-sort.md)
-   [Merge sort](../basic/merge-sort.md)
-   [Heap sort](../basic/heap-sort.md)
-   [Bucket sort](../basic/bucket-sort.md)
-   [Sorting-related STL](../basic/stl-sort.md)

The NOI syllabus only requires selection, bubble and insertion sort at the entry level, three sorting algorithms in total, but the others are not especially hard either and may appear in the first round, so they are all listed here.

### 2.5 Binary search and binary lifting

Binary search essentially applies the idea of divide and conquer: it keeps shrinking the search range until the answer is found. Note, however, that this way of searching must be applied to ordered data structures.

-   [Binary search](../basic/binary.md)

Binary lifting is different: by repeatedly doubling, it turns processing in a linear range into logarithmic processing, greatly improving the time complexity. (This topic needs a bit of mathematical background; it is fine to skip it for now.)

-   [Binary lifting](../basic/binary-lifting.md)

### 2.6 Search

In the entry-level group, search problems often appear as maze problems, usually with map-like data; in addition, search is very commonly used to efficiently enumerate cases when constructing valid solutions, and it can also be used to grab partial points.

#### 2.6.1 Depth-first search (DFS)

Depth-first search refers to the algorithm that conveniently implements brute-force enumeration with a recursive function; it is somewhat similar to the DFS algorithm in graph theory, but not entirely the same.

-   [DFS (search)](../search/dfs.md)

#### 2.6.2 Breadth-first search (BFS)

If every state is modeled as a vertex of a graph, we can carry out an exhaustive search.

-   [BFS (search)](../search/bfs.md)

#### 2.6.3 Search optimization

Many problems can be solved with DFS, but the complexity of this algorithm obviously cannot pass. Therefore some optimizations are needed to make it run faster. Such optimizations reduce attempts that cannot succeed and are called "pruning". Optimizations related to BFS are more flexible, but the basic idea is the same as here.

-   [DFS pruning optimizations](../search/opt.md)

### 2.7 Introduction to data structures

#### 2.7.1 Linear data structures

Arrays, linked lists, queues and stacks are all linear structures. Clever use of these structures can accomplish many convenient things.

-   [Stack](../ds/stack.md)
-   [Queue](../ds/queue.md)
-   [Linked list](../ds/linked-list.md)

#### 2.7.2 More complex data structures

-   [Trees and binary trees](../graph/tree-basic.md)
-   [The concept of a graph](../graph/concept.md)
-   [Storing graphs](../graph/save.md)

### 2.8 Introduction to dynamic programming

Dynamic programming (DP) is a method for solving complex problems by breaking the original problem down into relatively simple subproblems.

Since dynamic programming is not a specific algorithm but a method for solving a certain kind of problem, it appears in all sorts of data structures, and the kinds of problems related to it are even more varied.

-   [Introduction to dynamic programming](../dp/index.md)

#### 2.8.1 The knapsack problem

Given a knapsack of limited capacity, choose some items with volume and value to put in it so that the total value is maximized. This is the first hurdle that stops many competitive programmers; from here on, algorithms become somewhat harder to understand.

-   [Knapsack DP](../dp/knapsack/basic.md)

#### 2.8.2 Linear dynamic programming

In dynamic programming, one of the hardest parts is designing the states, which requires construction-related techniques. Once you have written down the states and the state transition equation, finishing a dynamic programming problem is not hard.

-   [Construction](../basic/construction.md)
-   [Dynamic programming basics](../dp/basic.md)

Memoized search is a way of implementing search that records information about states already visited, thereby avoiding visiting the same state repeatedly. Some problems can also use memoized search to reduce the difficulty of reasoning.

Because memoized search ensures that every state is visited only once, it is also a common way of implementing dynamic programming.

-   [Memoized search](../dp/memo.md)

#### 2.8.3 More complex dynamic programming

Interval dynamic programming is an extension of linear dynamic programming; when dividing the problem into stages, it depends heavily on the order in which the elements appear in a stage and on which elements of the previous stage they were merged from.

-   [Interval DP](../dp/interval.md)

### 2.9 Mathematics

#### 2.9.1 Arbitrary-precision arithmetic

What if even `long long` (or int64) is not enough? Use arbitrary-precision arithmetic. Essentially it simulates the four basic arithmetic operations.

-   [Arbitrary-precision computation](../math/bignum.md)

#### 2.9.2 Base conversion

In computers, besides binary, octal and hexadecimal are also commonly used. Sometimes knowing how to use the right base also helps a lot in solving problems.

-   [Numeral systems](../math/numeral-sys/base.md)

#### 2.9.3 Bit operations

Bit operations are operations performed on the binary representation of integers. Since computers store data internally in binary, bit operations are quite fast.

There are 6 basic bit operations: bitwise AND, bitwise OR, bitwise XOR, bitwise NOT, left shift and right shift.

-   [Bit operations](../math/bit.md)

#### 2.9.4 Number theory

-   [Number theory basics](../math/number-theory/basic.md)
-   [Prime numbers](../math/number-theory/prime.md)
-   [Sieves](../math/number-theory/sieve.md)
-   [Greatest common divisor](../math/number-theory/gcd.md)
-   [Euler's totient function](../math/number-theory/euler-totient.md)
-   [Prime factorization](../math/number-theory/pollard-rho.md)

#### 2.9.5 Combinatorial counting

-   [Permutations and combinations](../math/combinatorics/combination.md)
-   [Pigeonhole principle](../math/combinatorics/drawer-principle.md)
-   [Inclusion-exclusion principle](../math/combinatorics/inclusion-exclusion-principle.md)

***

With this you have learned all the algorithms within the scope of the entry-level group, but to master them you need to keep solving a sufficient number of problems to consolidate the knowledge you have acquired.
