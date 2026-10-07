---
title: Introduction to heaps
---

A heap is a tree in which every node has a key, and the key of every node is greater than or equal to / less than or equal to the key of its parent.

A heap in which the key of every node is greater than or equal to the key of its parent is called a min-heap, otherwise a max-heap. [The `priority_queue` in the STL](../lang/csl/container-adapter.md#优先队列) is in fact a max-heap.

The main operations supported by a (min-)heap are: inserting a number, querying the minimum, deleting the minimum, merging two heaps, and decreasing the value of an element.

Some more powerful heaps (mergeable heaps) can also (efficiently) support operations such as merge.

Some even more powerful heaps also support persistence, i.e. querying or operating on any historical version and producing a new version.

## Types of heaps

|    Operation `\` data structure[^ref4]   |                                      Pairing heap                                     |      Binary heap     |      Leftist tree     |          Binomial heap         |        Fibonacci heap       |
| :---------------------: | :--------------------------------------------------------------------------: | :----------: | :----------: | :------------------: | :----------------: |
|        insert       |                                    $O(1)$                                    |  $O(\log n)$ |  $O(\log n)$ |  $O(\log n)$[^ref1]  |       $O(1)$       |
|     find-min     |                                    $O(1)$                                    |    $O(1)$    |    $O(1)$    | $O(1)$[^ref2][^ref3] |       $O(1)$       |
|    delete-min    |                              $O(\log n)$[^ref3]                              |  $O(\log n)$ |  $O(\log n)$ |      $O(\log n)$     | $O(\log n)$[^ref3] |
|        merge       |                                    $O(1)$                                    |    $O(n)$    |  $O(\log n)$ |      $O(\log n)$     |       $O(1)$       |
| decrease-key | $o(\log n)$ (lower bound $\Omega(\log \log n)$, upper bound $O(2^{2\sqrt{\log \log n}})$)[^ref3] |  $O(\log n)$ |  $O(\log n)$ |      $O(\log n)$     |    $O(1)$[^ref3]   |
|         supports persistence        |                                   $\times$                                   | $\checkmark$ | $\checkmark$ |     $\checkmark$     |      $\times$      |

[^ref1]: A single insertion costs $O(\log n)$, but for $k$ consecutive insertions one can build a binomial heap containing only the elements to insert and then merge it with the original binomial heap, for an amortized cost of $O(1)$

[^ref2]: One can keep a pointer to the minimum element and update it during the other operations, so that the query takes $O(1)$

[^ref3]: The complexity is amortized

[^ref4]: Table taken from [Wikipedia](https://en.wikipedia.org/wiki/Priority_queue#Summary_of_running_times)

By convention, when "heap" is mentioned without qualification it usually refers to a binary heap.
