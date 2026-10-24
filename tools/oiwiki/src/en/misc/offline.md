---
title: Introduction to offline algorithms
---

This chapter introduces the idea of offline algorithms, common algorithms, and optimizations.

Offline algorithms are designed under the assumption that **all data is known before solving**, and they apply to problems with multiple queries. Their counterpart is the [online algorithm](https://en.wikipedia.org/wiki/Online_algorithm).

For example, [selection sort](../basic/selection-sort.md) cannot run until the globally smallest element of the array is known, so it is an offline algorithm, whereas [insertion sort](../basic/insertion-sort.md) can receive data dynamically and sort it without requiring all data to be known before execution, so it is an online algorithm.

For the same problem, offline algorithms are often superior to online algorithms in terms of design difficulty and other aspects. To prevent contestants from using offline algorithms, problems sometimes "force online"; a common way is that the parameters of the next query can only be obtained from the answer to the previous query ([interactive problems](../contest/problems.md#interactive-problems) and [communication problems](../contest/problems.md#communication-problems) also belong to this category).

Common ideas of offline algorithms include solving all queries together (e.g. [CDQ divide and conquer](./cdq-divide.md)), deriving the answers to other similar queries from the answer to one query (e.g. [parallel binary search](./parallel-binsearch.md) and [Mo's algorithm](./mo-algo-intro.md)), and so on.

Since an offline algorithm is an idea rather than a specific algorithm, it is used together with all kinds of data structures or algorithms, and the types of problems related to it are correspondingly more varied.
