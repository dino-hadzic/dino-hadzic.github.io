---
title: Sorting in the standard library
---

This page briefly introduces the sorting algorithms implemented in the C and C++ standard libraries.

Unless stated otherwise, the functions listed on this page are defined in the header `<algorithm>`.

## qsort

See: [`qsort`](https://en.cppreference.com/w/c/algorithm/qsort), [`std::qsort`](https://en.cppreference.com/w/cpp/algorithm/qsort)

This function is the general-purpose array sorting function of the C standard library; the actual algorithm is up to the library implementation. It is defined in `<stdlib.h>`; in the C++ standard library it is defined in `<cstdlib>`.

???+ warning "Note[^note2]"
    Although the function is called `qsort`, neither the C nor the POSIX standard requires it to use [quicksort](./quick-sort.md), nor do they guarantee any complexity or stability.

### The comparison function for qsort and bsearch

The qsort function has four parameters: the array name, the number of elements, the element size and the comparison rule. The comparison rule is given by a comparison function; different comparison functions give different sorting orders.

The comparison function must take two parameters of type `const void *`. Its return value is a positive number, a negative number or 0.

An example comparison function:

```c
int compare(const void* p1, const void* p2)  // comparison function for an int array
{
  int* a = (int*)p1;
  int* b = (int*)p2;
  if (*a > *b)
    return 1;  // a positive value means a is greater than b
  else if (*a < *b)
    return -1;  // a negative value means a is less than b
  else
    return 0;  // 0 means a and b are equivalent
}
```

Note: returning the difference of the two elements instead of a positive/negative number is a typical mistake, because it may cause an overflow.

An example of sorting structs:

```c
struct eg  // example struct
{
  int e;
  int g;
};

// comparison function for a struct eg array: sort by member e
int compare(const void* p1, const void* p2) {
  struct eg* a = (struct eg*)p1;
  struct eg* b = (struct eg*)p2;
  if (a->e > b->e)
    return 1;  // a positive value means a is greater than b
  else if (a->e < b->e)
    return -1;  // a negative value means a is less than b
  else
    return 0;  // 0 means a and b are equivalent
}
```

This also shows that equivalence does not mean equality; it only means the two elements are equivalent under this comparison rule.

## std::sort

See: [`std::sort`](https://en.cppreference.com/w/cpp/algorithm/sort)

Usage:

```cpp
// a[0] .. a[n - 1] is the sequence to sort
// sort a in place in increasing order
std::sort(a, a + n);

// cmp is a custom comparison function
std::sort(a, a + n, cmp);
```

Note: the comparison function of sort returns `true` or `false` to express the order of two elements; this is completely different from the semantics of qsort's three-valued comparison function. See the sort documentation linked above for details.

If `cmp` defines a strict weak ordering, converting it to the three-valued rule of `qsort` should return `cmp(a,b) ? -1 : cmp(b,a) ? 1 : 0`; equivalent elements must return zero.

`std::sort` is the more commonly used sorting function in the C++ library. Its last parameter is a binary comparison function; when `cmp` is not given, it sorts in increasing order.

Older C++ standards only required its **average** time complexity to be $O(n\log n)$. C++11 and later standards require its **worst-case** time complexity to be $O(n\log n)$.

The C++ standard does not strictly prescribe the algorithm; the actual implementation depends on the standard library. For example, the implementations in [libstdc++ 14.2.0](https://github.com/gcc-mirror/gcc/blob/releases/gcc-14.2.0/libstdc%2B%2B-v3/include/bits/stl_algo.h#L1876-L1908) and [libc++ 20.1.8](https://github.com/llvm/llvm-project/blob/llvmorg-20.1.8/libcxx/include/__algorithm/sort.h#L709-L727) both use [introsort](./quick-sort.md#introsort).

## std::nth\_element

See: [`std::nth_element`](https://en.cppreference.com/w/cpp/algorithm/nth_element)

Usage:

```cpp
std::nth_element(first, nth, last);
std::nth_element(first, nth, last, cmp);
```

It rearranges the elements in `[first, last)` so that the element pointed to by `nth` becomes the element that would be in that position if `[first, last)` were sorted. All elements before the new `nth` element are less than or equal to all elements after it.

The actual implementation is up to the standard library; common implementations use algorithms such as [quickselect](https://en.wikipedia.org/wiki/Quickselect) or [introselect](https://en.wikipedia.org/wiki/Introselect), which after each partition continue only on the side containing the target position.

For both usages the C++ standard requires an average time complexity of $O(n)$, where n is `std::distance(first, last)`.

It is often used when building a [k-d tree](../ds/kdt.md).

## std::stable\_sort

See: [`std::stable_sort`](https://en.cppreference.com/w/cpp/algorithm/stable_sort)

Usage:

```cpp
std::stable_sort(first, last);
std::stable_sort(first, last, cmp);
```

Stable sort: guarantees that equal elements keep the same relative order as in the original sequence.

The time complexity is $O(n\log^2 n)$, or $O(n\log n)$ when extra memory is available.

## std::partial\_sort

See: [`std::partial_sort`](https://en.cppreference.com/w/cpp/algorithm/partial_sort)

Usage:

```cpp
// mid = first + k
std::partial_sort(first, mid, last);
std::partial_sort(first, mid, last, cmp);
```

Selects from `[first,last)` the `k` elements that come first according to `cmp`, sorts them and places them in `[first,mid)`; the order of the rest is not guaranteed. When `cmp` is not given, it sorts in increasing order.

Complexity: approximately $(\textit{last}-\textit{first})\log(\textit{mid}-\textit{first})$ applications of `cmp`.

How it works:

The idea of `std::partial_sort` is: run `make_heap()` on the elements in `[first, mid)` of the original container to build a max-heap, then compare each element of `[mid, last)` with `first`, maintaining that `first` holds the maximum of the heap. If the element is smaller than that maximum, swap them and adjust the elements in `[first, mid)` to restore the max-heap order. After all comparisons, run `sort_heap()` on `[first, mid)` to arrange them in increasing order. Note that heap order and increasing order are different things.

## Custom comparison

See: [Operator overloading](https://en.cppreference.com/w/cpp/language/operators)

Built-in types (such as `int`) and user-defined structs allow customising the comparison function used when calling the STL sorting functions. A function implementing a binary comparison can be passed as the last argument of the call.

For user-defined structs, at least one relational operator must be defined before using the STL sorting functions on them, or a binary comparison function must be supplied in the call. Defining `operator<` is usually recommended.[^note1]

Example:

```cpp
int a[1009], n = 10;
// ...
std::sort(a + 1, a + 1 + n);                  // increasing order
std::sort(a + 1, a + 1 + n, greater<int>());  // decreasing order
```

```cpp
struct data {
  int a, b;

  bool operator<(const data rhs) const {
    return (a == rhs.a) ? (b < rhs.b) : (a < rhs.a);
  }
} da[1009];

bool cmp(const data u1, const data u2) {
  return (u1.a == u2.a) ? (u1.b > u2.b) : (u1.a > u2.a);
}

// ...
std::sort(da + 1, da + 1 + 10);  // uses the < operator defined in the struct, increasing order
std::sort(da + 1, da + 1 + 10, cmp);  // compares with the cmp function, decreasing order
```

### Strict weak ordering

See also: [Applications in C++ – Order theory](../math/order-theory.md#c-中的应用)

The operator used for sorting must satisfy a [strict weak ordering](../math/order-theory.md#二元关系), otherwise unpredictable things happen (such as runtime errors or incorrect sorting).

Common mistakes:

-   using `<=` to define the less-than operator for sorting;
-   reading, inside the sorting operator, an external array whose values may change (common in shortest-path algorithms);
-   using the result of comparing maxima/minima of several numbers as the sorting operator (the classic mistake in problems such as "皇后游戏" (Queen's Game) / "加工生产调度" (Production Scheduling)).

## External links

-   [On the use of adjacent-swap sorting and its pitfalls (Chinese)](https://ouuan.github.io/浅谈邻项交换排序的应用以及需要注意的问题/)

## References and notes

[^note1]: Because most STL functions use `operator<` for comparison by default.

[^note2]: [qsort, qsort\_s - cppreference.com](https://en.cppreference.com/c/algorithm/qsort)
