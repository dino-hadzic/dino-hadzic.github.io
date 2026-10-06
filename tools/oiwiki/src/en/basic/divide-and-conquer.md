---
title: Recursion and divide and conquer
---

This page introduces the difference between recursion and divide-and-conquer algorithms, and how they are used together.

## Recursion

### Definition

**Recursion**, in mathematics and computer science, refers to using the function itself in the definition of the function; in computer science it additionally refers to a method of solving a problem by repeatedly breaking it down into subproblems of the same kind.

### Introduction

To understand recursion, you first have to understand what recursion is.

The basic idea of recursion is that a function calls itself directly or indirectly, so that solving the original problem is turned into solving many subproblems with the same properties but smaller size. When solving, we only need to focus on how to split the original problem into suitable subproblems, not on how the subproblems are solved.

Here are some examples that help understand recursion:

1.  [What is recursion?](./divide-and-conquer.md)
2.  How do you sort a pile of numbers? Answer: split them in two halves, sort the left half, then the right half, then merge; as for how to sort the left and right halves, please re-read this sentence.
3.  How old are you? Answer: one more than last year; I was born in 1999.
4.  ![an example for understanding recursion](images/divide-and-conquer-1.png)

Recursion is very common in mathematics. For example, the formal set-theoretic definition of the natural numbers is: 1 is a natural number; every natural number has a successor, and that successor is also a natural number.

The two most important features of recursive code are the termination condition and the self-call. The self-call solves subproblems, while the termination condition defines the answer to the simplest subproblem.

```cpp
int func(input value) {
  if (termination condition) return solution of the smallest subproblem;
  return func(reduced size);
}
```

### Why write recursion

1.  Clear structure and good readability. For example, implementing [merge sort](./merge-sort.md) in two different ways:

    === "C++"
        ```cpp
        --8<-- "docs/basic/code/divide-and-conquer/divide-and-conquer_1.cpp:sort"
        ```

    === "Python"
        ```python
        --8<-- "docs/basic/code/divide-and-conquer/divide-and-conquer_1.py:sort"
        ```

    In both pieces of code, `merge(a, front, mid, end)` merges in place the two sorted closed intervals `[front,mid]` and `[mid+1,end]` of the same array.

2.  Practice in analysing the structure of problems. When you notice that a problem can be decomposed into smaller problems of the same structure, having written a lot of recursion makes you spot this feature quickly and solve the problem efficiently.

### Drawbacks of recursion

During program execution, recursion is implemented using the stack. Every time a function call is entered, a stack frame is pushed, and every time a function returns, a frame is popped. The stack is not infinite, so when the recursion depth is too large, a **stack overflow** results.

A recursive implementation may need an extra call stack, whereas an iterative implementation can use only constant auxiliary space. For example, given the head of a linked list, compute its length:

```cpp
// Typical iterative traversal
int size(Node *head) {
  int size = 0;
  for (Node *p = head; p != nullptr; p = p->next) size++;
  return size;
}

// Recursive traversal, each level handles one node
int size_recursion(Node *head) {
  if (head == nullptr) return 0;
  return size_recursion(head->next) + 1;
}
```

[![comparison of the two](images/divide-and-conquer-2.svg)](https://quick-bench.com/q/rZ7jWPmSdltparOO5ndLgmS9BVc)

### Optimising recursion

Main pages: [Search optimisation](../search/opt.md) and [Memoisation](../dp/memo.md)

A fairly basic recursive implementation may recurse too many times and easily exceed the time limit. In that case the recursion needs to be optimised.[^ref1]

## Divide and conquer

### Definition

**Divide and conquer** literally means "divide and rule": a complex problem is split into two or more identical or similar subproblems, until finally the subproblems can be solved directly; the solution of the original problem is the combination of the solutions of the subproblems.

### Procedure

The core idea of divide-and-conquer algorithms is exactly "divide and rule".

The rough flow has three steps: divide -> conquer -> combine.

1.  Decompose the original problem into subproblems of the same structure;
2.  once decomposed down to some easily solvable boundary, solve recursively;
3.  combine the solutions of the subproblems into the solution of the original problem.

Problems solvable by divide and conquer usually have these features:

-   The problem becomes easy to solve once its size is reduced enough.
-   The problem can be decomposed into several smaller problems of the same kind, i.e. it has optimal substructure; the solutions of the subproblems can be combined into the solution of the problem.
-   The subproblems are independent of each other, i.e. they share no common subproblems.

???+ warning "Note"
    If the subproblems are not independent, divide and conquer solves the common subproblems repeatedly and does a lot of unnecessary work. Divide and conquer can still be used in that case, but [dynamic programming](../dp/basic.md) is generally better.

Take merge sort as an example. Suppose the function implementing merge sort is called `merge_sort`. Make its responsibility clear: **sort the array passed in**. This problem can obviously be decomposed: sorting an array equals sorting its left and right halves separately and then merging them into one array.

```cpp
void merge_sort(an array) {
  if (easy to handle) return;
  merge_sort(left half of the array);
  merge_sort(right half of the array);
  merge(left half of the array, right half of the array);
}
```

Pass it half an array, and after processing that half is sorted. Note that `merge_sort` is extremely similar to the post-order traversal template of a binary tree. The divide-and-conquer pattern is **divide -> conquer (hit the bottom) -> combine (backtrack)**: first split left and right, then handle the merge; backtracking is popping the stack, which corresponds to post-order traversal.

The `merge` function is implemented in the same way as merging two sorted linked lists.

## Key points

### Key points of writing recursion

**Understand what a function does and trust that it can accomplish the task; never jump into the function trying to explore more details**, otherwise you will drown in endless details – how many stack frames can a human brain hold?

Take traversing a binary tree as an example.

```cpp
void traverse(TreeNode* root) {
  if (root == nullptr) return;
  traverse(root->left);
  traverse(root->right);
}
```

These few lines are enough to traverse any binary tree. For the recursive function `traverse(root)`, just trust that given a root node `root`, it will traverse that tree. So all that is needed is to pass the node's left and right children to this function.

The same extends to traversing an $N$-ary tree. The code is exactly the same as for a binary tree. Of course, for an $N$-ary tree there is obviously no in-order traversal.

```cpp
void traverse(TreeNode* root) {
  if (root == nullptr) return;
  for (auto child : root->children) traverse(child);
}
```

## Differences

### Recursion vs. enumeration

The difference between recursion and enumeration: enumeration splits the problem horizontally and then solves the subproblems one by one; recursion decomposes the problem level by level, splitting vertically.

### Recursion vs. divide and conquer

Recursion is a programming technique, a way of thinking about solving problems; divide and conquer is largely based on recursion, but is an algorithmic idea for solving more specific problems.

## Worked example

???+ note "[437. Path Sum III](https://leetcode.com/problems/path-sum-iii/)"
    You are given a binary tree in which each node contains an integer value.
    
    Find the number of paths that sum to a given value.
    
    The path does not need to start at the root or end at a leaf, but it must go downwards (travelling only from parent nodes to child nodes).
    
    The tree has no more than 1000 nodes and the node values are integers in the range $[-10^6,10^6]$.
    
    Example:
    
    ```text
    root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8
    
          10
         /  \
        5   -3
       / \    \
      3   2   11
     / \   \
    3  -2   1
    
    Return 3. The paths that sum to 8 are:
    
    1.  5 -> 3
    2.  5 -> 2 -> 1
    3. -3 -> 11
    ```
    
    ```cpp
    --8<-- "docs/basic/code/divide-and-conquer/divide-and-conquer_2.h"
    ```

??? note "Sample code"
    ```cpp
    --8<-- "docs/basic/code/divide-and-conquer/divide-and-conquer_2.cpp"
    ```

??? note "Problem analysis"
    The problem looks complicated, yet the code is extremely concise.
    
    First, solving a tree problem recursively necessarily traverses the whole tree, so the binary tree traversal framework (recursively calling the function itself on the left and right subtrees) must appear in the main function `pathSum`. Then what should each node do? It should look at how many qualifying paths it and its subtree contain. And that is the whole problem.
    
    Following the technique described earlier, define clearly, based on this analysis, what each recursive function should do:
    
    the `pathSum` function: given a node and a target value, return the total number of paths in the tree rooted at this node whose sum equals the target.
    
    the `count` function: given a node and a target value, return the number of paths starting at this node whose sum equals the target.
    
    ??? note "Sample code"
        ```cpp
        --8<-- "docs/basic/code/divide-and-conquer/divide-and-conquer_2.cpp"
        ```
    
    Once again: **understand what each function can do and trust that they can accomplish it.**
    
    To summarise, `pathSum` provides the binary tree traversal framework and calls `count` on every node during the traversal (pre-order is used here, but in-order and post-order would also work). `count` is also a binary tree traversal, used to find target-sum paths that start at the given node.

## Exercises

-   [Recursion practice on LeetCode](https://leetcode.com/explore/learn/card/recursion-i/)
-   [Divide and conquer problems on LeetCode](https://leetcode.com/tag/divide-and-conquer/)

## References and notes

[^ref1]: [labuladong 的算法小抄 – Recursion explained (Chinese)](https://labuladong.gitbook.io/algo/suan-fa-si-wei-xi-lie/di-gui-xiang-jie)
