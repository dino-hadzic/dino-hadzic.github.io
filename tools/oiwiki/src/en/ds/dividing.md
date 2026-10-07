---
title: Partition tree
---

## Introduction

The partition tree (dividing tree) is a data structure for solving the range $K$-th largest problem; its constant factor and difficulty of understanding are both much lower than those of the persistent segment tree (the so-called "chairman tree"). At the same time, the partition tree is closely tied to the "$K$-th largest", so it is a data structure based on sorting.

Prerequisites: [persistent segment tree](persistent-seg.md#主席树)

## Procedure

### Building the tree

Building a partition tree is relatively simple, but more complex compared to other trees.

![](./images/dividing-1.svg)

As shown in the figure, every level has a seemingly unordered array. In fact, every number marked in red is one that **goes to the left child**. And what is the rule of distribution? Compare with **the median of this level**: if it is less than or equal to the median, it goes to the left, otherwise to the right. But note: it is not strictly **"less than or equal goes left, otherwise right"**, because the median may have duplicates, and it also depends on the parity of $N$. The code below handles this cleverly; please refer to it.

We cannot sort every level every time; not to mention the constant factor, even the theoretical complexity would not pass. Think about it: to find the median, one sort is enough. Why? For example, the median of $l,r$ is exactly `num[mid]` after sorting.

Two key arrays:

tree\[log(N),N]: the tree itself; all values must be stored, space complexity $O(n\log n)$.
toleft\[log(N),n]: the number of elements among 1\~i at each level that go to the left child; this needs some understanding – it is a prefix sum.

???+ note "Implementation"
    ```pascal
    procedure Build(left,right,deep:longint); // left,right are the interval endpoints, deep is the level
    var
      i,mid,same,ls,rs,flag:longint; // flag is used to balance the counts on the left and right
    begin
      if left=right then exit; // reached the bottom level
      mid:=(left+right) >> 1;
      same:=mid-left+1;
      for i:=left to right do 
        if tree[deep,i]<num[mid] then
          dec(same);
      
      ls:=left; // pointer to the first position in the left child
      rs:=mid+1; // pointer to the first position in the right child
      for i:=left to right do
      begin
        flag:=0;
        if (tree[deep,i]<num[mid])or((tree[deep,i]=num[mid])and(same>0)) then // condition for going left
        begin
          flag:=1; tree[deep+1,ls]:=tree[deep,i]; inc(ls);
          if tree[deep,i]=num[mid] then // balance the counts on the left and right
            dec(same);
        end
        else
        begin
          tree[deep+1,rs]:=tree[deep,i]; inc(rs);
        end;
        toleft[deep,i]:=toleft[deep,i-1]+flag;
      end;
      Build(left,mid,deep+1); // continue
      Build(mid+1,right,deep+1);
    end;
    ```

### Query

Let us first digress to the persistent segment tree. When using it to find the range $K$-th smallest, we take $K$ as the reference: going left we just go left, going right we subtract the count that went left; it is the same in the partition tree.

The hard part of the query is the **shrinking of the interval**. In the figure below, the query is from $3$ to $7$, so on the next level only $2$ to $3$ needs to be queried. Of course, we define $[\text{left},\text{right}]$ as the shrunken interval (target interval), while $[l,r]$ is still the interval of the current node. Why mark the target interval? Because it is **the basis for deciding whether the answer is on the left or on the right**.

![](./images/dividing-2.svg)

???+ note "Implementation"
    ```pascal
    function Query(left,right,k,l,r,deep:longint):longint;
    var
      mid,x,y,cnt,rx,ry:longint;
    begin
      if left=right then // writing l=r is also fine, because the target interval must contain the answer
        exit(tree[deep,left]);
      mid:=(l+r) >> 1;
      x:=toleft[deep,left-1]-toleft[deep,l-1]; // number of elements from l to left going to the left child
      y:=toleft[deep,right]-toleft[deep,l-1]; // number of elements from l to right going to the left child
      ry:=right-l-y; rx:=left-l-x; // ry is the number from l to right going to the right child, rx the number from l to left going right
      cnt:=y-x; // number of elements from left to right going to the left child
      if cnt>=k then // standard, as with the persistent segment tree
        Query:=Query(l+x,l+y-1,k,l,mid,deep+1) // l+x shrinks the left boundary, l+y-1 the right one. In the figure above this means discarding nodes 1 and 2.
      else
        Query:=Query(mid+rx+1,mid+ry+1,k-cnt,mid+1,r,deep+1); // the same shrinking of the interval, just on the right side. Remember to subtract cnt from k.
    end;
    ```

## Properties

Time complexity: a single query needs only $O(\log n)$, so $m$ queries take $O(m\log n)$.

Space complexity: only $O(n\log n)$ numbers need to be stored.

Measured results: persistent segment tree: $1482 \text{ms}$, partition tree: $889 \text{ms}$. (Non-recursive, with a smaller constant.)

## Applications of the partition tree

Example problem: [Luogu P3157\[CQOI2011\] 动态逆序对](https://www.luogu.com.cn/problem/P3157)

> Problem summary: given a permutation of $n$ elements ($n\leq 10^5$) and $m$ queries ($m\leq 5\times 10^4$), each query deletes one number from the permutation; compute the number of inversions of the permutation after the deletion.

This problem can be solved with CDQ divide and conquer in $\Theta(n\log^2n)$ time and $\Theta(n)$ space, and the constant factor of CDQ is also excellent.

If the problem were forced online, it would usually be solved with the nested tree "Fenwick tree + persistent segment tree", with time complexity $\Theta(n\log^2n)$ and space complexity $\Theta(n\log^2n)$; the constant is slightly larger, but it also passes.

With a partition tree the problem can be solved online in $\Theta(n\log^2n)$ time and $\Theta(n\log n)$ space, and the constant is much smaller than that of the nested tree solution (roughly comparable to CDQ).

???+ warning "Note"
    For ease of implementation, this article splits the large array into two small arrays by the middle position, i.e. the partition tree below corresponds to the process of merge sort rather than quick sort. The topmost level is the sorted array, the bottom level is the original array.

We call a node of the partition tree a right node if and only if it goes to the right child on the next level, i.e. it is one of the numbers located later in the original array; left nodes are defined similarly. If the topmost level is sorted during construction, then, similarly to counting inversions with merge sort, one finds that the number of inversions of an array is the sum over all left nodes of the number of right nodes before each of them.

Now consider the deletion. Deleting a left node decreases the number of inversions of the whole array by the number of right nodes before it, while deleting a right node decreases it by the number of left nodes after it. So we can dynamically maintain "the number of right nodes before each left node" and "the number of left nodes after each right node". This can be maintained simply with a Fenwick tree.

Note that when maintaining with a Fenwick tree, only contributions within the same block of the partition tree may be counted; we must not leave the block. For the Fenwick tree there is a rather clever way to handle this.

Observe that the index range of every block of the partition tree must be of the form $[c\times 2^k+1,(c+1)\times 2^k]$, listed as follows (since the code does not deal with the bottom level of the partition tree, only levels up to the second-to-last are listed):

    [0001 0010] [0011 0100] [0101 0110] [0111 1000] [1001 1010] [1011 1100] [1101 1110] [1111 10000]  lev=1
    [0001 0010 0011 0100]   [0101 0110 0111 1000]   [1001 1010 1011 1100]   [1101 1110 1111 10000]    lev=2
    [0001 0010 0011 0100 0101 0110 0111 1000]       [1001 1010 1011 1100 1101 1110 1111 10000]        lev=3
    [0001 0010 0011 0100 0101 0110 0111 1000 1001 1010 1011 1100 1101 1110 1111 10000]                lev=4

Recall the principle of the Fenwick tree: when jumping upward, each time we do `x += lowbit(x)`. If we can guarantee not to jump out of the block while jumping upward, we guarantee that only the values of elements within the block are affected. Querying upward is similar.

To guarantee not jumping out of the block while jumping upward, it suffices to ensure that $lowbit(x)<2^{lev}$ holds when jumping.

Jumping downward is handled completely differently. If the indices of each block are written 0-indexed, they are of the form $[c\times 2^k,(c+1)\times 2^k)$. Then it suffices to shift the value of an index right by k bits to find out which block it is in. While jumping downward, constantly check whether we have left the block.

Note that a Fenwick tree implemented this way accesses a maximum index equal to the power of two closest to n, so the array size must not be just n.

Since updates are needed on $\log n$ levels, and an update on the $k$-th level has time complexity $\Theta(k)$, the final time complexity is $\Theta(n\log n+m\log^2n)$.

Code:

```cpp
--8<-- "docs/ds/code/dividing/dividing_1.cpp"
```

## Afterword

Reference blog post: [link](https://blog.csdn.net/littlewhite520/article/details/70250722).
