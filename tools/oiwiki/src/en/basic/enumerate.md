---
title: Enumeration
---

This page briefly introduces enumeration.

## Introduction

**Enumeration** is a problem-solving strategy that guesses the answer based on existing knowledge.

The idea of enumeration is to keep guessing: try the candidates from the set of possibilities one by one, and then check whether the condition of the problem holds.

## Key points

### Describe the solution space

Build a concise mathematical model.

When enumerating, be clear about: what are the possible cases? Which elements need to be enumerated?

### Reduce the enumeration space

What is the range of the enumeration? Does everything really need to be enumerated?

When solving a problem by enumeration, think these two things through, or you will pay an unnecessary time cost.

### Choose a suitable enumeration order

Decide according to the problem. For example, if the problem asks for the largest prime satisfying a condition, it is natural to enumerate from large to small.

## Example

Below is an example of solving a problem by enumeration and optimising the enumeration range.

??? note "Example"
    Given an array whose elements are pairwise distinct and all non-zero, find the number of ordered pairs of elements whose sum is $0$.

??? note "Solution idea"
    Code that enumerates two numbers is easy to write.
    
    === "C++"
        ```cpp
        for (int i = 0; i < n; ++i)
          for (int j = 0; j < n; ++j)
            if (a[i] + a[j] == 0) ++ans;
        ```
    
    === "Python"
        ```python
        for i in range(n):
            for j in range(n):
                if a[i] + a[j] == 0:
                    ans += 1
        ```
    
    === "Java"
        ```java
        for (int i = 0; i < n; ++i)
          for (int j = 0; j < n; ++j)
            if (a[i] + a[j] == 0) ++ans;
        ```
    
    Let us see how to optimise the enumeration range. If $(a_i,a_j)$ satisfies the condition, so does $(a_j,a_i)$; and since no element is $0$, the condition implies $i\ne j$. Therefore we can enumerate only $j<i$, so that each unordered pair is counted once, and multiply the result by $2$ to get the number of ordered pairs. The code:
    
    === "C++"
        ```cpp
        for (int i = 0; i < n; ++i)
          for (int j = 0; j < i; ++j)
            if (a[i] + a[j] == 0) ++ans;
        ans *= 2;
        ```
    
    === "Python"
        ```python
        for i in range(n):
            for j in range(i):
                if a[i] + a[j] == 0:
                    ans += 1
        ans *= 2
        ```
    
    === "Java"
        ```java
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < i; ++j)
                if (a[i] + a[j] == 0) ++ans;
        ans *= 2;
        ```
    
    It is easy to see that the enumeration range of $j$ has been reduced, which reduces the running time of this code.
    
    We can optimise further.
    
    Do both numbers really have to be enumerated? Once one number is chosen, the condition of the problem already determines what the other element (the other number) must satisfy; if we can find a way to check directly whether the required number exists, we save the time of enumerating the second number. More advanced: when the constraints allow, we can use a bucket[^1] to record the numbers seen so far.
    
    === "C++"
        ```cpp
        --8<-- "docs/basic/code/enumerate/enumerate_1.cpp"
        ```
    
    === "Python"
        ```python
        met = [False] * (MAXN * 2 + 1)
        for i in range(n):
            if met[MAXN - a[i]]:
                ans += 1
            met[a[i] + MAXN] = True
        ans *= 2
        ```
    
    === "Java"
        ```java
        boolean[] met = new boolean[MAXN * 2 + 1];
        for (int i = 0; i < n; ++i) {
            if (met[MAXN - a[i]]) ++ans;
            met[MAXN + a[i]] = true;
        }
        ans *= 2;
        ```

### Complexity analysis

-   Time complexity: a single pass over the array $a$ solves the problem, so for sufficiently large $n$ the time complexity is $O(n)$.
-   Space complexity: $O(n+\max\{|x|:x\in a\})$.

## Exercises

-   [2811: Lights Out - OpenJudge](http://bailian.openjudge.cn/practice/2811/)

## References and notes

[^1]: [Bucket sort](../basic/bucket-sort.md), [the majority element problem](../misc/main-element.md#离线算法) and [an explanation of the bucket data structure on Stack Overflow](https://stackoverflow.com/questions/42399355/what-is-a-bucket-or-double-bucket-data-structure)
