---
title: Two pointers
---

This page briefly introduces the two-pointer technique.

## Introduction

Two pointers is a simple yet flexible technique and idea: used alone it easily solves some specific problems, and combined with other algorithms it has a variety of uses.

As the name suggests, two pointers means using two pointers at the same time; in sequences and linked lists they point to positions, in trees and graphs they point to nodes, and they move either in the same direction or toward each other in order to maintain and collect information.

Let us now look at several concrete ways of using two pointers.

## Maintaining information about a range

When not combined with other data structures, the simplest pattern of maintaining range information with two pointers is to maintain information that has a certain monotonicity and for which adding and removing one element is easy to handle, such as the sum of positive numbers, the product of positive integers, and so on.

### Example 1

???+ note "Example 1 [LeetCode 713. Subarray Product Less Than K](https://leetcode-cn.com/problems/subarray-product-less-than-k/)"
    Given an array of positive integers $\mathit{nums}$ of length $n$ and an integer $k$, find the number of contiguous subarrays of the array whose product is less than $k$.
    
    Here $1 \leq n \leq 3 \times 10^4, 1 \leq nums[i] \leq 1000, 0 \leq k \leq 10^6$.

#### Procedure

Let the two pointers be $l,r$, and let an additional variable $\mathit{tmp}$ record the product of all numbers in $[l,r]$. Initially $l,r$ are both at the far left; first move $r$ to the right until we find $\mathit{tmp}\geq k$ for the first time, then fix $r$ and move $l$ to the right until $\mathit{tmp}\lt k$. Then for each $r$, $l$ is the left boundary it can extend to, and by the monotonicity of the product of positive integers, the number of ranges with right endpoint $r$ that satisfy the condition of the problem is $r-l+1$.

#### Implementation

```cpp
int numSubarrayProductLessThanK(vector<int>& nums, int k) {
  long long ji = 1ll, ans = 0;
  int l = 0;
  for (int i = 0; i < nums.size(); ++i) {
    ji *= nums[i];
    while (l <= i && ji >= k) ji /= nums[l++];
    ans += i - l + 1;
  }
  return ans;
}
```

Maintaining range information with two pointers can also be combined with other data structures such as difference arrays, monotonic queues, segment trees, persistent segment trees, and so on. Another algorithm that incorporates the two-pointer technique is Mo's algorithm: in Mo's algorithm the queries are sorted offline, and then two pointers are typically used to record the range currently being processed, with the range information gradually updated as the pointers move step by step.

### Example 2

Next, let us look at an example that uses two pointers on a tree together with tree difference arrays:

???+ note "Example 2 [Luogu P3066 Running Away From the Barn G](https://www.luogu.com.cn/problem/P3066)"
    Given a rooted tree with $n$ nodes with weighted edges, the nodes are numbered from 1 to $n$, and node 1 is the root of the tree. A parameter $t$ is also given; for every node $u$ of the tree, find how many nodes in the subtree of $u$ have a distance to $u$ not greater than $t$. Constraints: $1\leq n \leq 2\times 10^5,1 \leq t \leq 10^{18},1 \leq p_i \lt i,1 \leq w_i \leq 10^{12}$

#### Procedure

Traverse the whole tree with DFS from the root, using a stack to record the chain from the root to the current node; let one pointer $u$ point to the current node and another pointer $p$ point to the node of minimum depth among the nodes whose distance to $u$ is not greater than $t$. Record the distances to the root and determine $p$ by binary search each time. Then $u$ contributes to every node on the path from $p$ to $u$, which can be recorded with tree difference arrays.  
Note that $p$ must not be moved directly by brute force, otherwise the time complexity may degrade to $O(n^2)$.

### Exercises

[LeetCode 1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit](https://leetcode-cn.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/)

## Subsequence matching

???+ note "Example 3 [LeetCode 524. Longest Word in Dictionary through Deleting](https://leetcode-cn.com/problems/longest-word-in-dictionary-through-deleting/)"
    Given a string $s$ and an array of strings $\mathit{dictionary}$ as a dictionary, find and return the longest string in the dictionary that can be obtained by deleting some characters of $s$.

### Procedure

This kind of problem requires matching the strings $s$ and $t$ and deciding whether $t$ is a subsequence of $s$. To solve it, first place two pointers, one $i$ at the start of $s$ and one $j$ at the start of $t$. If $s[i]=t[j]$, the $j$-th character of $t$ has found its first match in $s$, so we can go on to check the rest, and $i$ and $j$ are both incremented by one. If the above equality does not hold, the $j$-th character of $t$ is still unmatched, so only $i$ is incremented and we continue searching in the remainder of $s$. Finally, if $j$ has moved to the past-the-end position, the whole string can be matched, i.e. $t$ is a subsequence of $s$; otherwise it is not.

### Implementation

```cpp
string findLongestWord(string s, vector<string>& dictionary) {
  sort(dictionary.begin(), dictionary.end());
  int mx = 0, r = 0;
  string ans = "";
  for (int i = dictionary.size() - 1; i >= 0; i--) {
    r = 0;
    for (int j = 0; j < s.length(); ++j) {
      if (s[j] == dictionary[i][r]) r++;
    }
    if (r == dictionary[i].length()) {
      if (r >= mx) {
        mx = r;
        ans = dictionary[i];
      }
    }
  }
  return ans;
}
```

This approach, where two pointers point to different objects which are then compared step by step, can also be used in some DP problems.

## Exploiting the sortedness of a sequence

Very often, the reason two pointers on a sequence correctly achieve their goal is some property of the sequence, and the most common one exploited is that the sequence is sorted.

???+ note "Example 4 [LeetCode 167. Two Sum II - Input Array Is Sorted](https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted/)"
    Given an integer array `numbers` sorted in **ascending order**, find two numbers in the array whose sum equals the target number `target`.

### Procedure

This problem is also a classic application of two pointers; although binary search is convenient too, it has an extra factor of $\log{n}$ in the time complexity, and the code is not concise enough.

Here is the two-pointer approach: since we need to find two numbers, and they cannot be at the same position, one of them must be on the left and the other on the right. Since the sum of the two numbers is fixed, the larger the smaller number is, the smaller the larger number is. Taking these properties into account, we can approach them from both ends.

First assume the answer is 1 and n. If we find $num[1]+num[n]\gt \mathit{target}$, one of the elements needs to become smaller, and $\mathit{num}[1]$ cannot become any smaller, so we decrement the pointer pointing to $n$ by one to make the larger number smaller.

Similarly, if we find $num[1]+num[n]\lt \mathit{target}$, one of the elements needs to become larger, and $\mathit{num}[n]$ cannot become any larger, so we increment the pointer pointing to 1 by one to make the smaller number larger.

Generalizing: if our two pointers currently point to $l,r$ with $l\lt r$, then if $num[l]+num[r]\gt \mathit{target}$, decrement $r$ by one, and if $num[l]+num[r]\lt \mathit{target}$, increment $l$ by one. In this way $l$ keeps moving right and $r$ keeps moving left, and in the end both converge to an answer.

### Implementation

```cpp
vector<int> twoSum(vector<int>& numbers, int target) {
  int r = numbers.size() - 1, l = 0;
  vector<int> ans;
  ans.clear();
  while (l < r) {
    if (numbers[l] + numbers[r] > target)
      r--;
    else if (numbers[l] + numbers[r] == target) {
      ans.push_back(l + 1), ans.push_back(r + 1);
      return ans;
    } else
      l++;
  }
  return ans;
}
```

In merge sort, merging two sorted arrays in $O(n+m)$ time is also an application of the two-pointer method that relies on the arrays being sorted.

### Exercises

[LeetCode 15. 3Sum](https://leetcode-cn.com/problems/3sum/)

## Finding a cycle in a singly linked list

### Procedure

There are also several ways to find a cycle in a singly linked list, but the fast and slow pointer method is one of the most concise, and we introduce it below.

First, both pointers point to the head of the list; let one pointer advance one step at a time and the other two steps at a time. If they meet, this proves there is a cycle; otherwise there is none. The time complexity is $O(n)$.

If there is a cycle, how do we find its starting point?

Let us write out the equations and take a look. Suppose that at the moment they meet, the slow pointer has taken $k$ steps in total, of which $l$ steps were on the cycle (when the fast and slow pointers meet on the cycle, the slow pointer has certainly not completed a full lap). The fast pointer has taken $2k$ steps; let the cycle length be $C$, then

$$
\begin{align}
& \ 2 k=n \times C+l+(k-l) \\
& \ k=n \times C \\
\end{align}
$$

At the first meeting, $n$ takes the smallest positive integer value 1. That is, $k=C$. Using this equality, after the two pointers meet we can move one of them to the head of the list and advance both one step at a time; the position where they meet again is the start of the cycle.

### Implementation

```cpp
--8<-- "docs/misc/code/two-pointer/two-pointer_1.cpp:core"
```

The time complexity is $O(n)$.
