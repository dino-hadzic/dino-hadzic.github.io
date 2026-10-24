---
title: Majority element problem
---

## Problem description

Given a sequence of $n$ elements, it is guaranteed that there is an element $a$ that appears **strictly more** than $n/2$ times; find this element.

## Solutions

### Offline algorithm

If the whole sequence is known from the start, a natural idea is to count the occurrences of each element in the sequence; the one that appears more than $n/2$ times is the majority element. We can create a bucket to count the occurrences of each value and output the element that appears more than $n/2$ times.

But the above approach introduces a bucket for counting, which is not space efficient. Obviously, if the sequence has a majority element, then after sorting, the element at position $\lfloor n/2\rfloor+1$ of the sequence must be the majority element, and it can be found with [`nth_element`](https://en.cppreference.com/w/cpp/algorithm/nth_element.html). This way we find the majority element in linear time without introducing extra space.

### Online algorithm

In some situations we need to process streaming data online; then we need an algorithm that does not require knowing all the data in advance, but gradually computes the answer using only the data given so far. The **majority vote algorithm** (Boyer–Moore) [^ref1] is such an algorithm that solves the majority element problem online.

Since the majority element appears more than $n/2$ times, for a complete sequence, after repeatedly canceling one majority element together with one element different from it, the majority element must remain at the end. Using this observation, we can design an online algorithm that performs such cancellations. Let two variables `val` and `cnt` represent the current majority candidate and how many copies of the candidate would remain if such cancellations were performed so far. Initially `cnt` is set to $0$. Each time we take an element from the data stream: if the current `cnt` is $0$, the majority candidate has been completely canceled and the currently recorded `val` is certainly not the majority element, so we set the current element as the majority candidate. Then we check whether the current element equals the majority candidate; if so, `cnt` increases by $1$, and if not, this element should be canceled together with one majority candidate, so `cnt` decreases by $1$. Repeat the above until the data stream is fully read; `val` is then the majority element.

???+ warning "Note"
    When the original data has no majority element, the result given by this algorithm is wrong. To determine whether a majority element exists in the sequence, the data stream must be read again, counting the occurrences of `val` and checking whether it exceeds $n/2$.
    
    To read the data stream again, you can reset the input position indicator using library functions such as [`std::basic_istream<CharT,Traits>::seekg`](https://en.cppreference.com/w/cpp/io/basic_istream/seekg) (stream input) or [`rewind`](https://en.cppreference.com/w/c/io/rewind), [`fseek`](https://en.cppreference.com/w/c/io/fseek) (C-style input).

## Example problems

???+ example "[Luogu P2397 yyy loves Maths VI (mode)](https://www.luogu.com.cn/problem/P2397)"
    Find the majority element of the given sequence.

??? note "Reference code"
    ```cpp
    --8<-- "docs/misc/code/main-element/main-element_1.cpp"
    ```

???+ example "[LeetCode 229. Majority Element II](https://leetcode.cn/problems/majority-element-ii)"
    Given an integer array of size $n$, find all elements that appear more than $\lfloor n/3\rfloor$ times.

??? note "Reference code"
    ```cpp
    --8<-- "docs/misc/code/main-element/main-element_2.cpp:core"
    ```

## References

[^ref1]: [Boyer–Moore majority vote algorithm - Wikipedia](https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_majority_vote_algorithm)
