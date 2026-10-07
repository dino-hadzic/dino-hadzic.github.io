---
title: Binary search
---

This page briefly introduces binary search, binary search on the answer, and ternary search, which is derived from the bisection method.

## Binary search

Binary search, also known as half-interval search or logarithmic search, is an algorithm for finding an element in a sorted sequence.

### Procedure

Take searching for a number in an ascending array as an example.

Each time it visits the middle element of the current part of the array. If the middle element is exactly the one we are looking for, the search ends; if the middle element is smaller than the value sought, then all elements to the left are not greater than the middle element, so the sought element cannot be among them and we only need to search to the right; if the middle element is greater than the value sought, by the same reasoning we only need to search to the left.

Concretely, let the indices of array $a$ start from $1$, let its length be $n$, and suppose we want to find the position of the number $x$. Let $l,r$ denote that we currently only consider the elements of the array whose index $i$ satisfies $l\le i\le r$. Initially set $l\gets1$, $r\gets n$. Each time, visit the middle element $a_{\textit{mid}}$, where $\textit{mid}=\left\lfloor\dfrac{l+r}{2}\right\rfloor$, and distinguish cases:

-   If $a_{\textit{mid}}<x$, since the array is ascending, all numbers with index less than or equal to $\textit{mid}$ are certainly smaller than $x$, so there is no need to search them; we only need to search the numbers with index greater than $\textit{mid}$, i.e. set $l\gets \textit{mid}+1$ and leave $r$ unchanged.
-   If $a_{\textit{mid}}>x$, since the array is ascending, all numbers with index greater than or equal to $\textit{mid}$ are certainly greater than $x$, so there is no need to search them; we only need to search the numbers with index less than $\textit{mid}$, i.e. leave $l$ unchanged and set $r\gets \textit{mid}-1$.
-   If $a_{\textit{mid}}=x$, we have found the position of $x$ and the algorithm ends.

If the position of $x$ has not been found by the time the considered range becomes empty, i.e. $l>r$, then $x$ is not in the array $a$.

### Properties

#### Time complexity

The best-case time complexity of binary search is $O(1)$.

The average and worst-case time complexity of binary search are both $O(\log n)$. Since the algorithm halves the search interval at every step, for an array of length $n$ it performs at most $O(\log n)$ comparisons with the target element.

#### Space complexity

The space complexity of the iterative version of binary search is $O(1)$.

The space complexity of the recursive version (without tail-call elimination) is $O(\log n)$.

### Implementation

```cpp
int binary_search(int x, int l = 1, int r = n) {  // find the index of x in an ascending array
  int ret = -1;                                   // return -1 if not found
  while (l <= r) {
    int mid = (l + r) >> 1;  // l + r may overflow, see the Note below
    if (a[mid] < x)
      l = mid + 1;
    else if (a[mid] > x)
      r = mid - 1;
    else {  // equality is tested last because in most steps the element is either greater or smaller
      ret = mid;
      break;
    }
  }
  return ret;
}
```

???+ note "Note"
    -   See [compiler optimizations – shifts instead of multiplication](../lang/optimizations.md#移位代替乘法): when $s$ is a signed number and you can guarantee $s\ge 0$, `s >> 1` uses fewer instructions than `s / 2`.
    
    -   When $l$ or $r$ is very large, $l+r$ may overflow. If $r-l$ does not overflow in that case, `(l + r) >> 1` in the code can be replaced by `l + ((r - l) >> 1)`.

???+ warning "Warning"
    When $s$ is a negative odd number, the results of `s >> 1` and `s / 2` differ by $1$ and are not the same. This is because the former rounds toward negative infinity (standardized in C++20, implementation-defined before that), while the latter rounds toward zero. See [C++ bitwise operators](../lang/op.md#位操作符). Therefore, when $l + r$ may be negative, `(l + r) / 2` may evaluate to $r$, which in the `r = mid` variant leads to an **infinite loop**. For example, when $l = -1,~r = 0$, `(l + r) / 2` equals $0$. This difference must be kept in mind when implementing the code.

### bsearch

The `bsearch` function is the binary search implemented by the C standard library, defined in `<stdlib.h>`. In the C++ standard library the function is defined in `<cstdlib>`. `qsort` and `bsearch` are the only two algorithm-type functions in the C standard library.

Compared with the four parameters of `qsort` ([sorting-related STL](./stl-sort.md)), `bsearch` adds the parameter "address of the element to search for" at the leftmost position. It is passed as an address so that the same comparison function as for `qsort` can be reused directly, allowing an immediate search after sorting. Therefore a concrete value cannot be passed to this parameter directly: the value to search for must first be stored in a variable, and then the address of that variable is passed.

Thus `bsearch` has five parameters in total: the address of the element to search for, the address of the start of the array, the number of elements, the size of an element, and the comparison rule. The comparison rule is still specified through a comparison function; see [sorting-related STL](./stl-sort.md).

The return value of `bsearch` is the address of the element found, with return type `void *`.

Note: `bsearch` differs in two respects from `std::lower_bound` and `std::upper_bound`, which are introduced below:

-   when several elements satisfy the condition, which one is returned is unspecified;
-   when the corresponding element cannot be found, it returns `NULL`.

Nearly the same functionality as `bsearch` can be achieved with `lower_bound` (it becomes exactly the same once the not-found case is handled separately), so problems that can be solved with `bsearch` can be rewritten directly with `lower_bound`.

## Binary search on the answer

Binary search on the answer is an algorithm that exploits the generalized ordering property of the answer to a problem (usually also called monotonicity) and quickly finds the answer in a way similar to binary search.

Unless otherwise stated, binary search on the answer usually refers to integer answers, i.e. the answer is known to be an integer.

Problems that can use binary search on the answer are usually of the form "find the maximum (minimum) value satisfying condition $P$" and have the following properties:

1.  given any number $x$, it is easy to check whether $x$ satisfies the condition;
2.  rough lower and upper bounds on the answer can be determined, i.e. we can determine $L$ and $R$ such that if the answer $x$ exists, then $x$ necessarily satisfies $L\le x \le R$;
3.  the range between these rough bounds is large, so checking the candidates one by one would exceed the time limit;
4.  condition $P$ has a generalized ordering property.

Suppose there is a function $f(x)$ with $f(x)=1$ if and only if $x$ satisfies condition $P$, and $f(x)=0$ otherwise. Then the generalized ordering property of condition $P$ can be defined as follows:

-   If for all $L\le i<j \le R$, $f(i)\le f(j)$, i.e. $f(x)$ is non-decreasing. Writing $f(i)$ for $i=L,\dots,R$ as a 01 sequence gives the shape `00...011...1`. In this case binary search on the answer can find the **minimum** value satisfying condition $P$.

-   If for all $L \le i<j \le R$, $f(i)\ge f(j)$, i.e. $f(x)$ is non-increasing. The corresponding 01 sequence has the shape `11...100...0`. In this case binary search on the answer can find the **maximum** value satisfying condition $P$.

In other words, the first ordering property means: if we know that $x$ satisfies condition $P$, then all numbers greater than $x$ certainly satisfy condition $P$ as well. Binary search on the answer finds the $x$ described by "all numbers smaller than it do not satisfy condition $P$, while it and all numbers greater than it satisfy condition $P$".

The second ordering property means: if we know that $x$ satisfies condition $P$, then all numbers smaller than $x$ certainly satisfy condition $P$ as well. Binary search on the answer finds the $x$ described by "it and all numbers smaller than it satisfy condition $P$, while all numbers greater than it do not satisfy condition $P$".

### Procedure

Take finding the minimum value with binary search on the answer as an example (the algorithm then requires the problem to have the first ordering property described above). Let the rough lower and upper bounds on the answer be $L$ and $R$.

Let $l,r$ denote that we can currently be sure the answer $x$ satisfies $l \le x \le r$. Similarly to binary search, initially set $l\gets L$, $r\gets R$. Each time we check whether $\textit{mid}=\left\lfloor\dfrac{l+r}{2}\right\rfloor$ satisfies condition $P$ and distinguish cases:

-   If $\textit{mid}$ does not satisfy the condition (i.e. $f(\textit{mid})$ is $0$), by the ordering property of the problem no number less than or equal to $\textit{mid}$ satisfies the condition, so none of them need to be considered; hence set $l\gets \textit{mid}+1$ and leave $r$ unchanged.
-   If $\textit{mid}$ satisfies the condition (i.e. $f(\textit{mid})$ is $1$), by the ordering property of the problem all numbers greater than or equal to $\textit{mid}$ satisfy the condition; but since the problem asks for the minimum, no number greater than $\textit{mid}$ needs to be considered, and it suffices to consider the numbers less than or equal to $\textit{mid}$. So set $r \gets \textit{mid}$ and leave $l$ unchanged.

When the answer range satisfies $l=r$ (i.e. $l<r$ no longer holds), the algorithm ends. Then $l$ or $r$ is the answer.

Note: if no answer exists within the bounds (the so-called no-solution case), every query $f(\textit{mid})$ returns $0$, so after the algorithm ends $l=r=R$ and $f(l)=0$. Hence, if the no-solution case needs to be detected, it suffices to additionally check whether $f(l)$ equals $0$.

Similarly to binary search, the algorithm halves the search interval at every step, so its time complexity is $O(M \log (R-L+1))$, where $M$ is the time complexity of checking once whether $\textit{mid}$ satisfies condition $P$.

### Implementation

Based on the algorithm description above, the following implementation can be given:

```cpp
// find the smallest integer x in [L, R] satisfying condition P, requires L <= R
// condition P must have the first ordering property, i.e. f(x) is non-decreasing
// in code, usually check(x) = f(x)
// returns -1 if there is no solution in the interval
int binary_search_min(int L, int R) {
  if (L > R) return -1;
  int l = L, r = R;
  while (l < r) {
    int mid = (l + r) >> 1;
    if (check(mid))  // f(mid) = 1, condition P is satisfied
      r = mid;       // the answer is in [l, mid]
    else
      l = mid + 1;  // the answer is in [mid + 1, r]
  }
  // now l == r
  if (!check(l)) return -1;  // no-solution check
  return l;
}
```

When `-1` is used to denote no solution, it must be guaranteed that it cannot be confused with a valid answer.

### Implementation details

When reading solutions, we may see another implementation:

```cpp
// find the smallest integer x in [L, R] satisfying check(x)
// check must be non-decreasing on [L, R]
// returns -1 if the interval is empty or has no solution
int binary_search_min(int L, int R) {
  if (L > R) return -1;
  int l = L, r = R;
  while (l <= r) {
    int mid = (l + r) >> 1;
    if (check(mid))
      r = mid - 1;
    else
      l = mid + 1;
  }

  if (l > R) return -1;
  return l;
}
```

The two variants compute the same answer but maintain different loop invariants.

??? note "Why do both variants find the minimum feasible value?"
    First assume $[L,R]$ is nonempty and an answer exists in the interval; denote the smallest number satisfying condition $P$ by $\textit{ans}$. Since $f$ is non-decreasing, within the original interval $[L,R]$ we have
    
    $$
    f(x)=0\quad (x<\textit{ans}),\qquad
    f(x)=1\quad (x\ge \textit{ans}).
    $$
    
    **The `l < r` variant keeps the answer inside a closed interval.**
    
    The invariant it maintains is
    
    $$
    l\le \textit{ans}\le r.
    $$
    
    Each time take $\textit{mid}=\left\lfloor\dfrac{l+r}{2}\right\rfloor$. If $f(\textit{mid})=1$, then $\textit{ans}\le\textit{mid}$, so set $r\gets\textit{mid}$; if $f(\textit{mid})=0$, then $\textit{ans}>\textit{mid}$, so set $l\gets\textit{mid}+1$. Both updates preserve the invariant.
    
    While $l<r$, we have $l\le\textit{mid}<r$, so every iteration strictly shrinks the interval. When the loop ends, $l=r$, and by the invariant $\textit{ans}=l$.
    
    **The `l <= r` variant excludes the part already decided; the answer may lie just past the right boundary.**
    
    The invariant it maintains is: within the original interval $[L,R]$, all $x<l$ satisfy $f(x)=0$ and all $x>r$ satisfy $f(x)=1$. Given that an answer exists, this means
    
    $$
    l\le \textit{ans}\le r+1.
    $$
    
    If $f(\textit{mid})=1$, then all $x\ge\textit{mid}$ in the original interval satisfy $f(x)=1$, so we may set $r\gets\textit{mid}-1$; if $f(\textit{mid})=0$, then all $x\le\textit{mid}$ in the original interval satisfy $f(x)=0$, so we may set $l\gets\textit{mid}+1$.
    
    Every iteration excludes at least one integer from the interval still to be searched, so the loop eventually terminates.
    
    While the loop runs, $l\le\textit{mid}\le r$. If $r\gets\textit{mid}-1$ is executed, the new right boundary satisfies $r\ge l-1$; if $l\gets\textit{mid}+1$ is executed, the new left boundary satisfies $l\le r+1$. Hence, whichever update is applied, afterwards $l\le r+1$. The loop ends when $l>r$, and combined with the integrality of the boundaries this means that necessarily $l=r+1$. Then from the answer-position invariant $l\le\textit{ans}\le r+1$ we get $\textit{ans}=l$.
    
    Note here that the interval $[l,r]$ still to be searched does not always contain the answer. For example, if in some round we happen to get $\textit{mid}=\textit{ans}$, then after $r\gets\textit{mid}-1$ we have $\textit{ans}=r+1$. Although the answer is then no longer in $[l,r]$, it still satisfies the invariant $l\le\textit{ans}\le r+1$, so the correctness proof above is unaffected.
    
    **When there is no solution, the two variants stop at different positions.**
    
    For the `l <= r` variant, if $l\le R$ after the loop ends, then since the left boundary always satisfies $l\ge L$, $l$ lies within the original interval. From $l=r+1$ and the invariant "all $x>r$ in the original interval satisfy $f(x)=1$", we get $f(l)=1$, so `check(l)` need not be called again.
    
    If there is no solution, in the end $l=R+1$, which is already outside the original search interval. Since we only require `check` to be usable on $[L,R]$, we should first check `l > R` rather than calling `check(l)` directly to decide whether a solution exists.
    
    For the `l < r` variant, recalling the earlier description, if there is no solution in the interval then in the end $l=r=R$. Then one must additionally check whether `check(l)` is $0$ to distinguish whether the answer is $R$ or there is no solution in the interval.
    
    In summary, given $L\le R$ and $f$ non-decreasing on $[L,R]$, both variants terminate after finitely many iterations. If a feasible value exists in the interval, both end with $l=\textit{ans}$ and return the smallest integer in the interval satisfying the condition; if there is no solution, the `l < r` variant detects it via `check(l)` after the loop, and the `l <= r` variant via `l > R` after the loop, and both return the agreed no-solution marker. For an empty interval with $L>R$, both pieces of code return the no-solution marker before entering the loop. Thus, although the two implementations maintain different loop invariants and stop at different positions, both correctly perform the required minimum-feasible-value query and produce the same return value.

These two variants show that the correctness of a binary search implementation depends on the interplay between the meaning of the boundaries, the loop invariant, the loop condition and the update rules. Whether the interval endpoints are included, or whether the loop uses `l < r` or `l <= r`, is not enough on its own to judge whether a variant is correct.

To prove a variant correct, one needs to confirm:

1.  the initialization satisfies the loop invariant;
2.  every update preserves the invariant and strictly decreases the number of integers in the interval still to be searched, thereby guaranteeing that the loop terminates;
3.  when the loop ends, the invariant and the termination condition determine that the return value is the answer; if no solution is allowed, it must also be explained how the no-solution case is recognized.

When discussing implementations, one must carefully distinguish between "the interval still to be searched" and "the interval guaranteed to contain the final answer": because of the differing boundary conditions, the two are not necessarily the same, and one cannot uniformly require the answer to always lie in the interval still to be searched.

Several common variants are listed below. All assume $L\le R$, that the problem has the first ordering property, and that the minimum feasible value $\textit{ans}$ exists. The position of the answer is given by the column "answer-position invariant".

| Variant                                                   | Initial $l,r$     | Loop condition | $\textit{mid}$                            | When $f(\textit{mid})=1$ | When $f(\textit{mid})=0$ | Answer-position invariant | At the end | Returns |
| --------------------------------------------------------- | ----------------- | -------------- | ----------------------------------------- | ------------------------ | ------------------------ | ------------------------- | ---------- | ------- |
| Closed interval $[l,r]$, excludes the decided part        | $l=L,\ r=R$       | $l\le r$       | $\left\lfloor\dfrac{l+r}{2}\right\rfloor$ | $r\gets\textit{mid}-1$   | $l\gets\textit{mid}+1$   | $l\le\textit{ans}\le r+1$ | $l=r+1$    | $l$     |
| Closed interval $[l,r]$, keeps the answer                 | $l=L,\ r=R$       | $l<r$          | $\left\lfloor\dfrac{l+r}{2}\right\rfloor$ | $r\gets\textit{mid}$     | $l\gets\textit{mid}+1$   | $l\le\textit{ans}\le r$   | $l=r$      | $l$     |
| Half-open interval $[l,r)$, excludes the decided part     | $l=L,\ r=R+1$     | $l<r$          | $\left\lfloor\dfrac{l+r}{2}\right\rfloor$ | $r\gets\textit{mid}$     | $l\gets\textit{mid}+1$   | $l\le\textit{ans}\le r$   | $l=r$      | $l$     |
| Half-open interval $(l,r]$, keeps the answer              | $l=L-1,\ r=R$     | $l+1<r$        | $\left\lfloor\dfrac{l+r}{2}\right\rfloor$ | $r\gets\textit{mid}$     | $l\gets\textit{mid}$     | $l<\textit{ans}\le r$     | $l+1=r$    | $r$     |
| Open interval $(l,r)$, maintains both boundaries          | $l=L-1,\ r=R+1$   | $l+1<r$        | $\left\lfloor\dfrac{l+r}{2}\right\rfloor$ | $r\gets\textit{mid}$     | $l\gets\textit{mid}$     | $l<\textit{ans}\le r$     | $l+1=r$    | $r$     |

A few more remarks on the table:

-   In row 3, $[l, r)$ is the interval still to be searched, but the answer may be exactly $r$.
-   Row 4 keeps the answer inside $(l, r]$ and relies on the initial right boundary $R$ satisfying $f(R) = 1$. While the loop runs, $r - l \ge 2$, so in rows 4 and 5 rounding the midpoint up is also correct.
-   In row 5, $(l, r)$ denotes the positions between the two boundaries that still need to be checked. The initial $L - 1$ can be regarded as a virtual sentinel with value 0 and $R + 1$ as a virtual sentinel with value 1. The loop only calls the predicate within the original interval, so the function values at the sentinels never actually need to be computed.
-   To handle the no-solution case: rows 1, 3 and 5 can check whether the return value is $R + 1$; row 2 needs to check $f(l)$; row 4 needs to check $f(R)$ first.

### Minimizing the maximum and maximizing the minimum

Minimizing the maximum and maximizing the minimum are typical problems that can be solved by binary search on the answer.

Take minimizing the maximum as an example. Usually each candidate solution corresponds to a set $S$ to be considered. If, over all candidate solutions, we want to minimize the maximum of the numbers in the corresponding set $S$, the problem can be transformed into: find the smallest $k$ such that there exists a solution with $\max(S) \le k$.

This problem has the generalized ordering property: if there exists a solution with $\max(S) \le k$, then for $i\ge k$ that solution also satisfies $\max(S)\le i$. Hence for $i \ge k$ there exists a solution with $\max(S) \le i$, which likewise meets the problem's requirement. Therefore it can be solved by binary search on the answer. Maximizing the minimum is analogous.

### Binary search on the answer in the STL

#### std::lower\_bound and std::upper\_bound

The C++ standard library implements:

-   [`std::lower_bound`](https://en.cppreference.com/w/cpp/algorithm/lower_bound), which finds the first element not less than the given value;
-   [`std::upper_bound`](https://en.cppreference.com/w/cpp/algorithm/upper_bound), which finds the first element greater than the given value.

Both are implemented with binary search, so the elements must be sorted before calling them (sorted here means with respect to the comparison function below, not necessarily in the mathematical sense), so that their problems satisfy the generalized ordering property (i.e. for `std::lower_bound`, if $a_i$ is not less than the given value, then the numbers after $i$ are also not less than the given value; for `std::upper_bound`, if $a_i$ is greater than the given value, then the numbers after $i$ are also greater than the given value).

`std::lower_bound` and `std::upper_bound` each take four parameters:

-   `first`: the starting [iterator](../lang/csl/iterator.md) of the sequence, pointing to its first element;
-   `last`: the ending iterator of the sequence, pointing to the **position after** the last element. In other words, if `last` is a bidirectional iterator, `--last` points to the last element of the sequence;
-   `value`: the given value;
-   `comp` (optional): the comparison function, written the same way as for `sort`. Note that `std::lower_bound` calls it as `comp(element, value)`, whereas `std::upper_bound` calls it as `comp(value, element)`.

Both return an iterator to the element satisfying the condition, of the same type as the one passed in. That is, if array pointers are passed in, the array pointer to the matching element is returned. If no element satisfies the condition, `last` is returned.

Both are defined in the header `<algorithm>`.

???+ note "Usage examples"
    -   In a 1-indexed array $a$ of length $n$, find the first number not less than $x$ among positions $l$ to $r$ and get its index: `lower_bound(a+l,a+r+1,x)-a`.
    -   In a 0-indexed array $a$ of length $n$, find the first number greater than $x$ (it must exist) and get its value: `*upper_bound(a,a+n,x)`.
    -   In a vector $a$ of length $n$, find the first number not less than $x$ and get its index (note that vectors are 0-indexed): `lower_bound(a.begin(),a.end(),x)-a.begin()`.

???+ note "About iterators"
    The starting and ending iterators above must be ForwardIterators. Array pointers and the iterators of vector, set, map and string all meet this requirement.

??? note "About the time complexity of the algorithm"
    In the libstdc++ standard library implementation used by GCC, both functions access the middle element with `std::advance`. This means the complexity of the function is $O(\log n)$ only when the iterator supports random access (e.g. array or vector iterators are passed in). If random access is not supported (e.g. set or map), the complexity of the function is the sum of the time to access the middle element in each query (usually linear). For example, performing an operation like `lower_bound(st.begin(),st.end(),val)` on a set or map has time complexity $O(n)$. In that case the member function `st.lower_bound(val)` should be used instead.

??? note "Implementing `std::lower_bound` and `std::upper_bound` with `bsearch`"
    Since bsearch returns NULL when the element cannot be found (see [bsearch](./binary.md#bsearch)), for example when searching for 3 in the sequence 1, 2, 4, 5, 6, implementing the functionality of `lower_bound` with `bsearch` becomes difficult.
    
    When implementing `std::lower_bound` and `std::upper_bound` with `bsearch`, one can exploit the parameter convention of its comparison function: the first parameter points to the element being searched for, and the second points to an element of the array being searched. So it suffices that the comparison function can obtain the address of the start of the array.
    
    ```cpp
    int A[100005];  // example global array
    
    // compare compares the values pointed to by two int pointers: *p1 > *p2 returns a positive number, equal returns
    // 0, less returns a negative number
    int compare(const void*, const void*);
    
    // find the address of the first element not less than the element searched for
    int lower(const void* p1, const void* p2) {
      int* a = (int*)p1;
      int* b = (int*)p2;
      if ((b == A || compare(a, b - 1) > 0) && compare(a, b) > 0)
        return 1;
      else if (b != A && compare(a, b - 1) <= 0)
        return -1;  // uses pointer subtraction, so the element type must be specified
      else
        return 0;
    }
    
    // find the address of the first element greater than the element searched for
    int upper(const void* p1, const void* p2) {
      int* a = (int*)p1;
      int* b = (int*)p2;
      if ((b == A || compare(a, b - 1) >= 0) && compare(a, b) >= 0)
        return 1;
      else if (b != A && compare(a, b - 1) < 0)
        return -1;  // uses pointer subtraction, so the element type must be specified
      else
        return 0;
    }
    ```
    
    Note: if the answer is the past-the-end position (e.g. the element searched for is greater than all elements), the method above still returns `NULL`, which must be handled separately.
    
    Since today's OI contestants rarely write pure C and this method is of limited use, it is not a focus. Beginners are advised to use the C++ functions `std::lower_bound` and `std::upper_bound` directly.

#### std::partition\_point

C++11 introduced [`std::partition_point`](https://en.cppreference.com/w/cpp/algorithm/partition_point). Its purpose is to quickly locate the "partition point" in an already partitioned sequence via binary search on the answer.

`std::partition_point` has three parameters:

-   `first`, `last`: as above;
-   `p`: a unary [predicate](../lang/csl/container.md#关联式容器). This is a callable object that accepts one argument $v$ and returns a boolean indicating whether $v$ satisfies the partition condition.

Let the sequence passed in be $a$; the function returns an iterator to the first element that does not satisfy the partition condition, i.e. an iterator to the element with the smallest index $x$ such that $p(a_x)$ is `false`.

The sequence must be partitioned, i.e. it must have the second generalized ordering property described above. In other words, listing the result of $p(v)$ for every element $v$ of the sequence as a 01 sequence gives the shape `11...100...0`, and the function returns an iterator to the position of the first $0$.

??? note "Relationship between `std::partition_point` and `std::lower_bound`/`std::upper_bound`"
    In fact, `std::lower_bound` and `std::upper_bound` are special forms of `std::partition_point`.
    
    Define a function `f` with the code `bool f(int v) { return !(val <= v); }`. Passing `f` as the predicate to `std::partition_point` gives the same result as `std::lower_bound`. Likewise for `std::upper_bound`.

### Binary search on a real-valued answer

Binary search on a real-valued answer, also called floating-point binary search, is the variant of binary search on the answer in which the answer is a real number.

Unlike the integer case, the real-valued case usually does not require the exact answer, but a real approximation meeting a given precision requirement.

#### Procedure

Take finding the minimum as an example. Let the rough lower and upper bounds on the answer be $L$ and $R$. Let $l,r$ denote that we can currently be sure the answer $x$ satisfies $l\le x\le r$. Initially set $l\gets L$, $r\gets R$. Each time take $\textit{mid}=\dfrac{l+r}{2}$ (note that this is real arithmetic) and check whether $\textit{mid}$ satisfies condition $P$:

-   If $\textit{mid}$ satisfies the condition, similarly to the integer case set $r\gets \textit{mid}$ and leave $l$ unchanged.
-   If $\textit{mid}$ does not satisfy the condition, similarly to the integer case set $l\gets \textit{mid}$ and leave $r$ unchanged.

Note that, unlike the integer case, the real-valued case cannot shrink the interval via `mid + 1` or `mid - 1`, because there are no adjacent elements in the real numbers; we can only set a boundary equal to $\textit{mid}$ and rely on the interval length being halved repeatedly to approach the answer.

The algorithm ends when the interval length $r-l$ does not exceed the given precision $\textit{eps}$, or when a preset number of iterations is reached. Then $l$, $r$ or $\dfrac{l+r}{2}$ can all serve as an approximation of the answer (if the final return value is required to satisfy condition $P$, return $r$). To find the maximum, simply reverse the directions of the two cases above: if $\textit{mid}$ satisfies the condition, set $l\gets \textit{mid}$; otherwise set $r\gets \textit{mid}$ (correspondingly, if the final return value is required to satisfy condition $P$, return $l$).

With `while (r - l > eps)`, the time complexity of binary search on a real-valued answer is $O(M \log((R-L)/\textit{eps}))$. With a fixed number of iterations $k$, the time complexity is $O(Mk)$. Here $M$ is the time complexity of checking once whether $\textit{mid}$ satisfies condition $P$. Because of floating-point errors in real arithmetic, implementations usually do not test $l=r$ directly but test $r-l<\textit{eps}$, or simply loop a fixed number of times, e.g. $60$ to $100$, to avoid infinite loops and guarantee precision.

#### Implementation

```cpp
double binary_search_iter(double L, double R) {  // fixed-iteration-count implementation
  double l = L, r = R;
  for (int i = 0; i < 100; ++i) {
    double mid = (l + r) / 2;
    if (check(mid))
      r = mid;
    else
      l = mid;
  }
  return r;
}

const double eps = 1e-7;  // required precision, usually 1/100 of the precision required by the problem or smaller

double binary_search_eps(double L, double R) {  // eps implementation
  double l = L, r = R;
  while (r - l > eps) {
    double mid = (l + r) / 2;
    if (check(mid))
      r = mid;
    else
      l = mid;
  }
  return r;
}
```

???+ warning "Warning"
    `eps` should not be too large, or the precision is insufficient; nor too small, or it may be unreachable due to floating-point errors and cause an infinite loop. If the answer range is very large or the precision requirement very high, a fixed number of iterations is recommended instead of `while (r - l > eps)`.

### Example problem

???+ note "[Luogu P1873 Cutting Trees](https://www.luogu.com.cn/problem/P1873)"
    Lumberjack Mirko needs to cut $M$ meters of wood. This is an easy job for Mirko, since he has a beautiful new woodcutting machine that can fell a forest like wildfire. However, Mirko is only allowed to cut a single row of trees.
    
    Mirko's machine works as follows: Mirko sets a height parameter $H$ (in meters), the machine raises a giant saw blade to height $H$ and cuts off all parts of the trees higher than $H$ (of course, the parts of trees not higher than $H$ meters remain intact). Mirko then gets the parts of the trees that were cut off.
    
    For example, if the heights of a row of trees are $20,~15,~10,~17$ and Mirko raises the blade to a height of $15$ meters, the remaining heights of the trees after cutting will be $15,~15,~10,~15$, and Mirko will get $5$ meters of wood from the first tree and $2$ meters from the fourth, $7$ meters of wood in total.
    
    Mirko cares a lot about ecology, so he does not want to cut off too much wood. That is exactly why he sets the blade as high as possible. Your task is to help Mirko find the maximum integer height $H$ of the blade such that he gets at least $M$ meters of wood. That is, if the blade were raised by another $1$ meter, he would not get $M$ meters of wood.

??? note "Solution idea"
    We could enumerate the answer from $0$ to $10^9$, but this naive approach certainly would not get full marks, since enumerating from $0$ to $10^9$ takes too long. Instead we can binary search the answer on the interval $[0,~10^9]$ and check the feasibility of each candidate (usually with a greedy method). **This is binary search on the answer.**

??? note "Reference code"
    ```cpp
    --8<-- "docs/basic/code/binary/binary_2.cpp"
    ```
    
    After reading the code above, you surely have two questions:
    
    1.  Why is the search interval half-open (closed on the left, open on the right)?
    
        Because at the end of the search it looks like this (taking the maximum feasible value as an example):
    
        ![](./images/binary-final-1.svg)
    
        and then
    
        ![](./images/binary-final-2.svg)
    
        For the minimum feasible value it is exactly the opposite.
    2.  Why return the left value?
    
        As above. When the loop ends, $l+1=r$, `check(l)` is true and `check(r)` is false, so $l$ is the maximum feasible value.

## Ternary search

### Introduction

The bisection method can be used to approximately find the zero of a function. If we need to find the extremum point of a unimodal function, ternary search is usually needed.

This section uses the following strict unimodality convention: for a function $f(x)$ defined on $[l,r]$, if there exists $x^*\in[l,r]$ such that $f(x)$ is strictly increasing on $[l,x^*]$ and strictly decreasing on $[x^*,r]$, then $f(x)$ is called a unimodal function. Both intervals contain $x^*$, so $x^*$ is the unique maximum point and $f(x^*)$ is the maximum.

??? note "Why not find the extremum point as a zero of the derivative?"
    First, unimodality does not guarantee that the zero of the derivative is unique, and a point where the derivative is zero is not necessarily the maximum point. For example,
    
    $$
    f(x)=\begin{cases}
      (x-1)^3+1,&0\le x<2,\\
      (3-x)^3+1,&2\le x\le 4.
    \end{cases}
    $$
    
    The zeros of $f'(x)$ are $x=1$ and $x=3$, while the maximum of $f(x)$ is attained at $x=2$, where it is not differentiable.
    
    Second, for some functions the process and result of differentiation are rather complicated, and the function may not even be expressible in the form $y=f(x)$.
    
    Finally, in some problems the unimodal function whose extremum is sought is not a single function but one obtained from several functions through special operations (e.g. the maximum of the minimum of several linear functions with differing monotonicity). In that case the derivative may be a piecewise function, and the function may be non-differentiable at some points.

???+ warning "Note"
    Ternary search can find both the maximum of a unimodal function and the minimum of a "unimodal valley" function. For convenience of exposition, unless otherwise stated, the text below takes finding the maximum of a unimodal function as the example.

### Procedure

The basic idea of ternary search is similar to the bisection method, but at each step two points $\textit{lmid} < \textit{rmid}$ (the two blue points in the figure below) are chosen within the current interval $[l,r]$ (between the two orange points in the figure). As shown in the figure, if $f(\textit{lmid})<f(\textit{rmid})$, then the function is necessarily increasing on $[l,\textit{lmid})$ (the red part of the figure), the maximum point (the green point) is certainly not in this interval, and the interval can be discarded; however, the possibility that the maximum point lies to the right of $\textit{rmid}$ cannot be excluded, so nothing more can be discarded. And vice versa.

![](images/ternary.svg)

The correctness of ternary search does not depend on the specific choice of $\textit{lmid}$ and $\textit{rmid}$; it suffices that they are two distinct points within the interval, and usually the two trisection points are taken. However, their choice affects the efficiency of ternary search. Each step discards one of the two side intervals, so the two points can also be taken close to the midpoint in order to enlarge the discarded interval. If we take $\textit{mid}\pm\delta$ with $\delta>0$ sufficiently small, comparing the function values amounts to determining the sign of the approximate derivative $\dfrac{f(\textit{mid}+\delta)-f(\textit{mid}-\delta)}{2\delta}$. Since the functions encountered in algorithm competitions usually have good smoothness, we can use this to roughly decide on which side of $\textit{mid}$ the extremum point lies, thereby achieving efficiency close to the bisection method.

### Implementation

Pseudocode:

$$
\begin{array}{l}
\textbf{Algorithm}\operatorname{TernarySearch}(f,l,r):\\
\textbf{Input. } \text{A unimodal function } f(x) \text{ and its domain } [l,r].  \\
\textbf{Output. } \text{The maximizer }x^*\text{, up to an error of }\varepsilon\text{, and its value } f(x^*). \\
\textbf{Method. } \\
\begin{array}{ll}
1 & \textbf{while } r - l > \varepsilon\\
2 & \qquad \textit{mid}\gets (l+r)/2\\
3 & \qquad \textit{lmid}\gets \textit{mid} - \varepsilon / 3 \\
4 & \qquad \textit{rmid}\gets \textit{mid} + \varepsilon / 3 \\
5 & \qquad \textbf{if } f(\textit{lmid}) < f(\textit{rmid}) \\
6 & \qquad \qquad l\gets \textit{lmid} \\
7 & \qquad \textbf{else } \\
8 & \qquad \qquad r\gets \textit{rmid} \\
9 & x^* \gets (l+r)/2 \\
10& \textbf{return } x^*,~ f(x^*)
\end{array}
\end{array}
$$

???+ tip "Choice of split points"
    In the code, the split points are chosen as $\textit{mid} \pm \varepsilon / 3$ to guarantee that they always lie between the current $l$ and $r$, thereby avoiding an infinite loop.

???+ info "The integer case"
    If the domain of $f(x)$ is the integers, both the ternary search above and the golden-section search below should terminate as soon as $r-l$ is very small. For very small $r-l$, the maximum point has to be found by brute-force enumeration.

### Optimization: golden-section search

If a single call of $f(x)$ is expensive and the number of calls of $f(x)$ needs to be reduced further, the constant factor of ternary search can be improved with golden-section search. This is also an important part of the optimum seeking method proposed by Hua Luogeng.

In ternary search, each iteration needs two function calls, and after one iteration the interval length shrinks to at most $1/2$ of the original. This means that to reach precision $\varepsilon$, at least

$$
2\log_2\dfrac{r-l}{\varepsilon}
$$

function calls are needed. This is the best result ternary search can achieve. If other split points are chosen, e.g. the trisection points, the number of calls increases further, since the interval shrinks more slowly per iteration.

The improvement of golden-section search is to reuse a split point computed earlier. Thus, apart from the first iteration which needs two function calls, every other iteration needs only one. Let the golden ratio be

$$
\phi = \dfrac{\sqrt{5}-1}{2} \approx 0.618.
$$

In each iteration, the split points chosen are the left and right golden-section points:

$$
m^l = \phi l +(1-\phi)r,~m^r = (1-\phi)l+\phi r.
$$

Splitting a segment at golden-section points has a self-similar structure. That is, $m^l$ is the left golden-section point of the segment $[l,r]$ and also the right golden-section point of the segment $[l,m^r]$. The benefit of choosing split points this way is that in iteration $k>1$ one of the chosen split points has always been computed before, so the previous result can be reused directly.

![](./images/golden-section-search.svg)

With split points chosen this way, reaching precision $\varepsilon$ needs only

$$
1 + \log_{\phi^{-1}}\dfrac{r-l}{\varepsilon} \approx 1 + 1.44\log_2\dfrac{r-l}{\varepsilon}
$$

function calls. Asymptotically, fewer function calls are needed.

Pseudocode:

$$
\begin{array}{l}
\textbf{Algorithm}\operatorname{GoldenSectionSearch}(f,l,r):\\
\textbf{Input. } \text{A unimodal function } f(x) \text{ and its domain } [l,r].  \\
\textbf{Output. } \text{The maximizer }x^*\text{, up to an error of }\varepsilon\text{, and its value } f(x^*). \\
\textbf{Method. } \\
\begin{array}{ll}
1 & \textit{lmid} \gets \phi l + (1-\phi)r \\
2 & \textit{rmid} \gets (1-\phi)l + \phi r \\
3 & \textit{lval} \gets f(\textit{lmid}) \\
4 & \textit{rval} \gets f(\textit{rmid}) \\
5 & \textbf{while } r - l > \varepsilon \\
6 & \qquad \textbf{if } \textit{lval} > \textit{rval} \\
7 & \qquad \qquad r \gets \textit{rmid} \\
8 & \qquad \qquad \textit{rmid} \gets \textit{lmid} \\
9 & \qquad \qquad \textit{rval} \gets \textit{lval} \\
10& \qquad \qquad \textit{lmid} \gets \phi l + (1-\phi)r \\
11& \qquad \qquad \textit{lval} \gets f(\textit{lmid}) \\
12& \qquad \textbf{else} \\
13& \qquad \qquad l \gets \textit{lmid} \\
14& \qquad \qquad \textit{lmid} \gets \textit{rmid} \\
15& \qquad \qquad \textit{lval} \gets \textit{rval} \\
16& \qquad \qquad \textit{rmid} \gets (1-\phi)l + \phi r \\
17& \qquad \qquad \textit{rval} \gets f(\textit{rmid}) \\
18& x^* \gets (l+r)/2 \\
19& \textbf{return }x^*,~f(x^*)
\end{array}
\end{array}
$$

### Example problem

???+ note "[Luogu P3382 - Ternary Search](https://www.luogu.com.cn/problem/P3382)"
    Given a polynomial of degree $N$ and a range $[l, r]$, find the unique value $x$ such that the function is increasing on $[l, x]$ and decreasing on $[x, r]$.

??? note "Solution idea"
    The problem asks for the value of the argument at which the degree-$N$ polynomial attains its maximum on $[l, r]$, so ternary search can obviously be used. The implementation below uses the two trisection points and moves the interval endpoints to the split points actually compared; when the interval is small enough, it outputs the midpoint of the interval.

??? note "Reference code"
    === "C++"
        ```cpp
        --8<-- "docs/basic/code/binary/binary_1.cpp"
        ```
    
    === "Python"
        ```python
        --8<-- "docs/basic/code/binary/binary_1.py"
        ```

### Exercises

-   [UVa 1476 - Error Curves](https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=447&page=show_problem&problem=4222)
-   [UVa 10385 - Duathlon](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=15&page=show_problem&problem=1326)
-   [UOJ 162 - Tsinghua Training 2015, Light Bulb Test](https://uoj.ac/problem/162)
-   [Luogu P7579 - RdOI R2, Weigh](https://www.luogu.com.cn/problem/P7579)

## Fractional programming

See: [Fractional programming](../misc/frac-programming.md)

Fractional programming is usually described as the following problem: each item has two attributes $c_i$, $d_i$, and some items must be selected in a certain way so that $\dfrac{\sum{c_i}}{\sum{d_i}}$ is maximized or minimized.

Classic examples include the optimal ratio cycle, the optimal ratio spanning tree and so on.

Fractional programming can be solved with the bisection method.

## References and notes

-   [Ternary search - Wikipedia](https://en.wikipedia.org/wiki/Ternary_search)
-   [Golden-section search - Wikipedia](https://en.wikipedia.org/wiki/Golden-section_search)
-   [Ternary search - CP Algorithms](https://cp-algorithms.com/num_methods/ternary_search.html)
