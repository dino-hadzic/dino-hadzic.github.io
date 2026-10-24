---
title: Mo's algorithm with bitset
---

Bitsets are often used for decision and counting problems that are hard to maintain with conventional data structures, while Mo's algorithm can maintain interval information that is hard to maintain with conventional data structures. Combining the two lets us exploit the advantages of both at the same time.

## Example problem [「Ynoi2016」掉进兔子洞 (Falling into the Rabbit Hole)](https://www.luogu.com.cn/problem/P4688)

This problem matches exactly the characteristics of Mo's algorithm with bitset mentioned above. It is easy to think of storing, in a separate bitset for each interval, all the values that appear in it; the answer to one query is then the sum of the lengths of all intervals minus the number of elements in the intersection of the three $\times 3$.

However, using a bitset inside Mo's algorithm also requires adapting the algorithm to the characteristics of bitsets:

1.  A bitset cannot handle multiple occurrences of the same value well. We can take the discretized value of the current element plus the number of its occurrences so far in the current interval as the object inserted into the bitset.
2.  When we normally use Mo's algorithm, we may not pay attention to the order of the 4 ways of moving the pointers, so during the pointer moves the left endpoint of the interval may end up to the right of the right endpoint, i.e. the interval length becomes negative, making the number of elements negative. In other situations this has no effect, but in this problem the element inserted into the bitset depends on the number of elements, so we must pay attention to the order of the 4 ways of moving the pointers: write the statements that move the left pointer to the left and the right pointer to the right first, to avoid inserting negative numbers into the bitset.
3.  Although bitsets use little memory, they still cannot cope with a data size of $10 ^ 5 \times 10 ^ 5$. So we need to split the queries into a constant number of parts and process them separately, which keeps the memory just sufficient while leaving the time complexity unchanged.

??? note "Reference code"
    ```cpp
    --8<-- "docs/misc/code/mo-algo-with-bitset/mo-algo-with-bitset_1.cpp"
    ```

## Exercises

-   [小清新人渣的本愿 (The Humble Wish of a Scumbag)](https://www.luogu.com.cn/problem/P3674)
-   [「Ynoi2017」由乃的玉米田 (Yuno's Cornfield)](https://www.luogu.com.cn/problem/P5355)
-   [「Ynoi2011」WBLT](https://www.luogu.com.cn/problem/P5313)
