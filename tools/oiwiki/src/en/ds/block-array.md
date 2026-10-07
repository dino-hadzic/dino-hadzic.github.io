---
title: Block array
---

## Building a block array

A block array means splitting an array into several blocks; the information within a block is stored for the block as a whole, and if a query runs into incomplete blocks at the two ends, they are handled directly by brute force. Usually the block length is $O(\sqrt{n})$. For a detailed analysis, see Xu Mingkuan's paper "A Preliminary Study of Block Decomposition Algorithms with Non-standard Block Sizes" in the 2017 Chinese national training team papers.

Below we directly give code for one way of building a block array.

???+ note "Implementation"
    ```cpp
    num = sqrt(n);
    for (int i = 1; i <= num; i++)
      st[i] = n / num * (i - 1) + 1, ed[i] = n / num * i;
    ed[num] = n;
    for (int i = 1; i <= num; i++) {
      for (int j = st[i]; j <= ed[i]; j++) {
        belong[j] = i;
      }
      size[i] = ed[i] - st[i] + 1;
    }
    ```

Here `st[i]` and `ed[i]` are the start and end of a block, and `size[i]` is the size of the block.

## Storing and modifying information within blocks

### Example 1: [The Master's Magic](https://www.luogu.com.cn/problem/P2801)

Two operations:

1.  add $z$ to every number in the range $[x,y]$;
2.  count the numbers in the range $[x,y]$ that are greater than or equal to $z$.

We need to query the number of elements within a block that are greater than or equal to a given number, so we need an array `t` holding the sorted elements of each block, while `a` is the original (unsorted) array. For updates of whole blocks we use something like permanent lazy tags: the array `delta` records the value currently added to the whole block. Let $q$ be the total number of queries and updates; then the time complexity is $O(q\sqrt{n}\log n)$.

The array `delta` records the value assigned to each block as a whole.

???+ note "Implementation"
    ```cpp
    void Sort(int k) {
      for (int i = st[k]; i <= ed[k]; i++) t[i] = a[i];
      sort(t + st[k], t + ed[k] + 1);
    }
    
    void Modify(int l, int r, int c) {
      int x = belong[l], y = belong[r];
      if (x == y)  // if the range lies within one block, modify directly
      {
        for (int i = l; i <= r; i++) a[i] += c;
        Sort(x);
        return;
      }
      for (int i = l; i <= ed[x]; i++) a[i] += c;     // modify the starting segment directly
      for (int i = st[y]; i <= r; i++) a[i] += c;     // modify the ending segment directly
      for (int i = x + 1; i < y; i++) delta[i] += c;  // tag the middle blocks as a whole
      Sort(x);
      Sort(y);
    }
    
    int Answer(int l, int r, int c) {
      int ans = 0, x = belong[l], y = belong[r];
      if (x == y) {
        for (int i = l; i <= r; i++)
          if (a[i] + delta[x] >= c) ans++;
        return ans;
      }
      for (int i = l; i <= ed[x]; i++)
        if (a[i] + delta[x] >= c) ans++;
      for (int i = st[y]; i <= r; i++)
        if (a[i] + delta[y] >= c) ans++;
      for (int i = x + 1; i <= y - 1; i++)
        ans +=
            ed[i] - (lower_bound(t + st[i], t + ed[i] + 1, c - delta[i]) - t) + 1;
      // use lower_bound to find the position of the first number >= c in each complete middle block
      return ans;
    }
    ```

### Example 2: Ark of the Cold Night

Two operations:

1.  set every number in the range $[x,y]$ to $z$;
2.  count the numbers in the range $[x,y]$ that are less than or equal to $z$.

The array `delta` records the value to which the whole block is currently assigned. When the block has not been assigned as a whole, this is marked with a special value (such as `0x3f3f3f3f3f3f3f3fll`). For the boundary blocks, do a `pushdown` before querying, pushing the information stored for the block down to every number. After an assignment, remember to `sort` again. Everything else is the same as in the previous problem.

???+ note "Implementation"
    ```cpp
    void Sort(int k) {
      for (int i = st[k]; i <= ed[k]; i++) t[i] = a[i];
      sort(t + st[k], t + ed[k] + 1);
    }
    
    void PushDown(int x) {
      if (delta[x] != 0x3f3f3f3f3f3f3f3fll)  // this value marks that the block has not been assigned as a whole
        for (int i = st[x]; i <= ed[x]; i++) a[i] = t[i] = delta[x];
      delta[x] = 0x3f3f3f3f3f3f3f3fll;
    }
    
    void Modify(int l, int r, int c) {
      int x = belong[l], y = belong[r];
      PushDown(x);
      if (x == y) {
        for (int i = l; i <= r; i++) a[i] = c;
        Sort(x);
        return;
      }
      PushDown(y);
      for (int i = l; i <= ed[x]; i++) a[i] = c;
      for (int i = st[y]; i <= r; i++) a[i] = c;
      Sort(x);
      Sort(y);
      for (int i = x + 1; i < y; i++) delta[i] = c;
    }
    
    int Binary_Search(int l, int r, int c) {
      int ans = l - 1, mid;
      while (l <= r) {
        mid = (l + r) / 2;
        if (t[mid] <= c)
          ans = mid, l = mid + 1;
        else
          r = mid - 1;
      }
      return ans;
    }
    
    int Answer(int l, int r, int c) {
      int ans = 0, x = belong[l], y = belong[r];
      PushDown(x);
      if (x == y) {
        for (int i = l; i <= r; i++)
          if (a[i] <= c) ans++;
        return ans;
      }
      PushDown(y);
      for (int i = l; i <= ed[x]; i++)
        if (a[i] <= c) ans++;
      for (int i = st[y]; i <= r; i++)
        if (a[i] <= c) ans++;
      for (int i = x + 1; i <= y - 1; i++) {
        if (0x3f3f3f3f3f3f3f3fll == delta[i])
          ans += Binary_Search(st[i], ed[i], c) - st[i] + 1;
        else if (delta[i] <= c)
          ans += size[i];
      }
      return ans;
    }
    ```

## Exercises

1.  [Point update, range query](https://loj.ac/problem/130)
2.  [Range update, range query](https://loj.ac/problem/132)
3.  ["Template" Segment Tree 2](https://www.luogu.com.cn/problem/P3373)
4.  ["Ynoi2019 Mock Contest" Yuno loves sqrt technology III](https://www.luogu.com.cn/problem/P5048)
5.  ["Violet" Dandelion](https://www.luogu.com.cn/problem/P4168)
6.  [Writing Poems](https://www.luogu.com.cn/problem/P4135)
