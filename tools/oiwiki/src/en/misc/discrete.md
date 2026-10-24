---
title: Discretization
---

## Introduction

Discretization is a data-processing technique that can essentially be viewed as a kind of [hashing](../string/hash.md#the-idea-of-hashing) which guarantees that the data still preserves its original [total/partial order](../math/order-theory.md#偏序集) after hashing.

Put simply, when some data cannot conveniently be used directly as array indices, either because the values are very large or because their type does not support it, and only the relative order between elements affects the final result, we can process the problem using the ranks of the original data instead; this is discretization.

Large integers, floating-point numbers, strings, and so on can all be discretized.

## Implementation

Discretizing an array and then performing queries on it is a fairly common use case.

### Method 1

Usually the original array contains repeated elements, and equal elements are generally discretized to the same value.

The method is as follows:

1.  Create a copy of the original array.

2.  Sort the values in the copy in ascending order.

3.  Remove duplicates from the sorted copy.

4.  Find the position of every element of the original array in the copy; the position is the rank, which becomes the discretized value.

```cpp
// arr[i] is the initial array, the index range is [1, n]

for (int i = 1; i <= n; ++i)  // step 1
  tmp[i] = arr[i];
std::sort(tmp + 1, tmp + n + 1);                          // step 2
int len = std::unique(tmp + 1, tmp + n + 1) - (tmp + 1);  // step 3
for (int i = 1; i <= n; ++i)                              // step 4
  arr[i] = std::lower_bound(tmp + 1, tmp + len + 1, arr[i]) - tmp;
```

For the STL algorithms used in the reference implementation, see [STL algorithms](../lang/csl/algorithm.md).

Likewise, we can also discretize a [std::vector](../lang/csl/sequence-container.md#vector):

```cpp
// std::vector<int> arr;
std::vector<int> tmp(arr);  // tmp is a copy of arr
std::sort(tmp.begin(), tmp.end());
tmp.erase(std::unique(tmp.begin(), tmp.end()), tmp.end());
for (int i = 0; i < n; ++i)
  arr[i] = std::lower_bound(tmp.begin(), tmp.end(), arr[i]) - tmp.begin();
```

### Method 2

Depending on the problem requirements, equal elements are sometimes discretized to different values according to their input order.

In that case implementing it with the `std::lower_bound()` function becomes somewhat difficult, and a different approach is needed:

1.  Create a copy of the original array and at the same time record the position where each element occurs.

2.  Sort the copy by value in ascending order; when values are equal, sort by order of occurrence in ascending order.

3.  Put the discretized numbers back into the original array.

```cpp
struct Data {
  int idx, val;

  bool operator<(const Data& o) const {
    if (val == o.val)
      return idx < o.idx;  // when values are equal, the element that appears earlier gets the smaller discretized value
    return val < o.val;
  }
} tmp[MAXN];  // std::pair can be used as well

for (int i = 1; i <= n; ++i) tmp[i] = Data{i, arr[i]};
std::sort(tmp + 1, tmp + n + 1);
for (int i = 1; i <= n; ++i) arr[tmp[i].idx] = i;
```

### Complexity

For method 1, removing duplicates has complexity $O(n)$, sorting has complexity $O(n \log n)$, and the final $n$ lookups have complexity $O(n \log n)$.

For method 2, sorting has complexity $O(n \log n)$.

Hence the total time complexity of both methods is $O(n \log n)$.

The space complexity is $O(n)$.

## Exercises

-   [\[HAOI2014\] 贴海报 (Posting Posters)](https://www.luogu.com.cn/problem/P3740)
-   [\[NOI2015\] 程序自动分析 (Automatic Program Analysis)](https://www.luogu.com.cn/problem/P1955)
