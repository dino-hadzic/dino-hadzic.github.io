---
title: Introduction to suffix arrays
---

## Conventions

For string-related definitions, see [String basics](./basic.md).

String indices start from $1$.

The length of the string $s$ is $n$.

"Suffix $i$" denotes the suffix starting at the $i$-th character; when stored, the suffix $s[i\dots n]$ of the string $s$ is represented by $i$.

## What is a suffix array?

A suffix array (Suffix Array) mainly involves two arrays: $sa$ and $rk$.

Here $sa[i]$ denotes the index of the $i$-th smallest suffix after sorting all suffixes; this is the suffix array itself, also called the index array $sa$ below;

$rk[i]$ denotes the rank of suffix $i$; it is an important auxiliary array, also called the rank array $rk$ below.

These two arrays satisfy the property $sa[rk[i]]=rk[sa[i]]=i$.

### Explanation

Example of a suffix array:

[![](./images/sa1.png)][2]

## How to compute a suffix array?

### O(n^2logn) approach

We believe everyone can come up with this approach on their own: sort the array holding all suffix strings with `sort`. Since the sort performs $O(n\log n)$ string comparisons, and each string comparison takes $O(n)$ character comparisons, the time complexity of this sort is $O(n^2\log n)$.

### O(nlog^2n) approach

This approach uses the idea of doubling.

First, sort all substrings of $s$ of length $1$, i.e. the individual characters, to obtain the sorted index array $sa_1$ and rank array $rk_1$.

The doubling process:

1.  Using the ranks of two substrings of length $1$, i.e. $rk_1[i]$ and $rk_1[i+1]$, as the first and second sort keys, we can sort all substrings of $s$ of length $2$: $\{s[i\dots \min(i+1, n)]\ |\ i \in [1,\ n]\}$, obtaining $sa_2$ and $rk_2$;

2.  then, using the ranks of two substrings of length $2$, i.e. $rk_2[i]$ and $rk_2[i+2]$, as the first and second sort keys, we can sort all substrings of $s$ of length $4$: $\{s[i\dots \min(i+3, n)]\ |\ i \in [1,\ n]\}$, obtaining $sa_4$ and $rk_4$;

3.  doubling in this way, using the ranks of substrings of length $w/2$, i.e. $rk_{w/2}[i]$ and $rk_{w/2}[i+w/2]$, as the first and second sort keys, we can sort all substrings of $s$ of length $w$, $s[i\dots \min(i+w-1,\ n)]$, obtaining $sa_w$ and $rk_w$. Here, similarly to the rules of lexicographic ordering, when $i+w>n$, $rk_w[i+w]$ is treated as negative infinity;

4.  $rk_w[i]$ is the rank of the substring $s[i\dots i + w - 1]$, so when $w \geqslant n$ the resulting index array $sa_w$ is exactly the suffix array we need.

#### Procedure

Illustration of sorting by doubling:

[![](./images/sa2.png)][2]

Clearly the doubling process takes $O(\log n)$ rounds, and in each round sorting the substrings with `sort` is $O(n\log n)$, where each substring comparison costs $2$ character comparisons;

besides that, in each doubling round after `sort` there is an additional $O(n)$ update of $rk$, but it is negligible compared with $O(n\log n)$;

so the time complexity of this algorithm is $O(n\log^2n)$.

??? note "Implementation"
    ```cpp
    #include <algorithm>
    #include <cstdio>
    #include <cstring>
    #include <iostream>
    
    using namespace std;
    
    constexpr int N = 1000010;
    
    char s[N];
    int n, w, sa[N], rk[N << 1], oldrk[N << 1];
    
    // To prevent accessing rk[i+w] from going out of bounds, the array is twice as large.
    // Of course one could check the bounds before accessing, but a double-size array is simpler.
    
    int main() {
      int i, p;
    
      scanf("%s", s + 1);
      n = strlen(s + 1);
      for (i = 1; i <= n; ++i) sa[i] = i, rk[i] = s[i];
    
      for (w = 1; w < n; w <<= 1) {
        sort(sa + 1, sa + n + 1, [](int x, int y) {
          return rk[x] == rk[y] ? rk[x + w] < rk[y + w] : rk[x] < rk[y];
        });  // a lambda is used here
        memcpy(oldrk, rk, sizeof(rk));
        // since the old rk is overwritten while computing rk, copy it first
        // if two substrings are equal, their rk must be equal too, so deduplicate
        for (p = 0, i = 1; i <= n; ++i) {
          if (oldrk[sa[i]] == oldrk[sa[i - 1]] &&
              oldrk[sa[i] + w] == oldrk[sa[i - 1] + w]) {
            rk[sa[i]] = p;
          } else {
            rk[sa[i]] = ++p;
          }
        }
      }
    
      for (i = 1; i <= n; ++i) printf("%d ", sa[i]);
    
      return 0;
    }
    ```

### O(nlogn) approach

In the $O(n\log^2n)$ approach above, a single sort costs $O(n\log n)$; if we could sort in $O(n)$, we could compute the suffix array in $O(n\log n)$.

Prerequisites: [Counting sort](../basic/counting-sort.md), [Radix sort](../basic/radix-sort.md).

Since the sort keys while computing the suffix array are ranks, whose value range is $O(n)$, and the sort is by two keys, radix sort can optimize the sorting to $O(n)$.

??? note "Implementation"
    ```cpp
    #include <algorithm>
    #include <cstdio>
    #include <cstring>
    #include <iostream>
    
    using namespace std;
    
    constexpr int N = 1000010;
    
    char s[N];
    int n, sa[N], rk[N << 1], oldrk[N << 1], id[N], cnt[N];
    
    int main() {
      int i, m, p, w;
    
      scanf("%s", s + 1);
      n = strlen(s + 1);
      m = 127;
      for (i = 1; i <= n; ++i) ++cnt[rk[i] = s[i]];
      for (i = 1; i <= m; ++i) cnt[i] += cnt[i - 1];
      for (i = n; i >= 1; --i) sa[cnt[rk[i]]--] = i;
      memcpy(oldrk + 1, rk + 1, n * sizeof(int));
      for (p = 0, i = 1; i <= n; ++i) {
        if (oldrk[sa[i]] == oldrk[sa[i - 1]]) {
          rk[sa[i]] = p;
        } else {
          rk[sa[i]] = ++p;
        }
      }
    
      for (w = 1; w < n; w <<= 1, m = n) {
        // counting sort by the second key: id[i] + w
        memset(cnt, 0, sizeof(cnt));
        memcpy(id + 1, sa + 1,
               n * sizeof(int));  // id keeps a copy of sa, which is effectively oldsa
        for (i = 1; i <= n; ++i) ++cnt[rk[id[i] + w]];
        for (i = 1; i <= m; ++i) cnt[i] += cnt[i - 1];
        for (i = n; i >= 1; --i) sa[cnt[rk[id[i] + w]]--] = id[i];
    
        // counting sort by the first key: id[i]
        memset(cnt, 0, sizeof(cnt));
        memcpy(id + 1, sa + 1, n * sizeof(int));
        for (i = 1; i <= n; ++i) ++cnt[rk[id[i]]];
        for (i = 1; i <= m; ++i) cnt[i] += cnt[i - 1];
        for (i = n; i >= 1; --i) sa[cnt[rk[id[i]]]--] = id[i];
    
        memcpy(oldrk + 1, rk + 1, n * sizeof(int));
        for (p = 0, i = 1; i <= n; ++i) {
          if (oldrk[sa[i]] == oldrk[sa[i - 1]] &&
              oldrk[sa[i] + w] == oldrk[sa[i - 1] + w]) {
            rk[sa[i]] = p;
          } else {
            rk[sa[i]] = ++p;
          }
        }
      }
    
      for (i = 1; i <= n; ++i) printf("%d ", sa[i]);
    
      return 0;
    }
    ```

### Some constant-factor optimizations

If you submit the code above to [LOJ #111: Suffix sorting](https://loj.ac/problem/111):

![](./images/sa3.png)

This is because the code above really does have a large constant factor.

#### The second key needs no counting sort

Think about what sorting by the second key really does: it puts those $sa[i]$ that fall outside the string (i.e. $sa[i] + w > n$) at the front of the $sa$ array, and then the rest in their original order:

```cpp
int cur = 0;
for (int i = n - w + 1; i <= n; i++) id[++cur] = i;
for (int i = 1; i <= n; i++)
  if (sa[i] > w) id[++cur] = sa[i] - w;
```

#### Optimizing the value range of the counting sort

After each update of $rk$ we computed a $p$; this $p$ is exactly the value range of $rk$, so set the value range to it.

#### If all ranks are distinct, the suffix array can be generated directly

Consider the new $rk$ array: if its value range is $[1,n]$, all ranks are distinct and no further sorting is needed.

??? note "Implementation"
    ```cpp
    #include <algorithm>
    #include <cstdio>
    #include <cstring>
    #include <iostream>
    
    using namespace std;
    
    constexpr int N = 1000010;
    
    char s[N];
    int n;
    int m, p, rk[N * 2], oldrk[N], sa[N * 2], id[N], cnt[N];
    
    int main() {
      scanf("%s", s + 1);
      n = strlen(s + 1);
      m = 128;
    
      for (int i = 1; i <= n; i++) cnt[rk[i] = s[i]]++;
      for (int i = 1; i <= m; i++) cnt[i] += cnt[i - 1];
      for (int i = n; i >= 1; i--) sa[cnt[rk[i]]--] = i;
    
      for (int w = 1;; w <<= 1, m = p) {  // m = p is the value range optimization
        int cur = 0;
        for (int i = n - w + 1; i <= n; i++) id[++cur] = i;
        for (int i = 1; i <= n; i++)
          if (sa[i] > w) id[++cur] = sa[i] - w;
    
        memset(cnt, 0, sizeof(cnt));
        for (int i = 1; i <= n; i++) cnt[rk[i]]++;
        for (int i = 1; i <= m; i++) cnt[i] += cnt[i - 1];
        for (int i = n; i >= 1; i--) sa[cnt[rk[id[i]]]--] = id[i];
    
        p = 0;
        memcpy(oldrk, rk, sizeof(oldrk));
        for (int i = 1; i <= n; i++) {
          if (oldrk[sa[i]] == oldrk[sa[i - 1]] &&
              oldrk[sa[i] + w] == oldrk[sa[i - 1] + w])
            rk[sa[i]] = p;
          else
            rk[sa[i]] = ++p;
        }
    
        if (p == n) break;  // when p = n no further sorting is needed
      }
    
      for (int i = 1; i <= n; i++) printf("%d ", sa[i]);
    
      return 0;
    }
    ```

### O(n) approach

In ordinary problems, computing the suffix array by doubling with a small constant is entirely sufficient; the parts other than computing the suffix array often have $O(n\log n)$ complexity too, so doubling is not the bottleneck.

But if you encounter special problems, problems with tight time limits, or you want an even shorter running time, you need to learn the $O(n)$ methods for computing the suffix array.

#### SA-IS

See [Induced sorting and the SA-IS algorithm](https://riteme.site/blog/2016-6-19/sais.html); its [comment page](https://github.com/riteme/riteme.github.io/issues/28) is also worth reading.

#### DC3

See [\[2009\] Suffix arrays – a powerful tool for processing strings, by Luo Suiqian][2].

## Applications of suffix arrays

### Finding the smallest cyclic shift

Duplicating the string $S$ into $SS$ turns this into a suffix sorting problem.

Example problem: ["JSOI2007" Character encryption](https://www.luogu.com.cn/problem/P4051).

### Finding a substring in a string

The task is to find a pattern $S$ in a text $T$ online. Online means that we know the text $T$ in advance, but we learn the pattern $S$ only when queried. We can first build the suffix array of $T$ and then search for the substring $S$. If the substring $S$ occurs in $T$, it must be a prefix of some suffixes of $T$. Since we have sorted all suffixes, we can achieve this by binary searching for $S$ in the array $p$. Comparing the substring $S$ with the current suffix takes $O(|S|)$, so the time complexity of finding a substring is $O(|S|\log |T|)$. Note that if the substring occurs multiple times in $T$, all occurrences are adjacent in the array $p$. Therefore the number of occurrences can be found with another binary search, and printing the position of each occurrence is also easy.

### Taking characters from both ends of a string to minimize lexicographic order

Example problem: ["USACO07DEC" Best Cow Line](https://www.luogu.com.cn/problem/P2870).

Problem: given a string, each time take one character from its front or back to form a new string; among all strings that can be formed this way, which is lexicographically smallest?

??? note "Solution"
    The brute-force approach decides, in $O(n)$ in the worst case, whether to take from the front or the back (i.e. it compares the string obtained by taking from the front with the reversed string obtained by taking from the back); we only need to optimize this decision.
    
    Since we need to compare within the set formed by the suffixes of the original string and the suffixes of the reversed string, we can append the reversed string to the original string with a character that never occurs in between (such as `#`; in code the null character can be used directly), compute the suffix array, and make this decision in $O(1)$.

??? note "Reference code"
    ```cpp
    --8<-- "docs/string/code/sa/sa_1.cpp"
    ```

## The height array

### LCP (longest common prefix)

The LCP of two strings $S$ and $T$ is the largest $x$ ($x\le \min(|S|, |T|)$) such that $S_i=T_i\ (\forall\ 1\le i\le x)$.

Below, $lcp(i,j)$ denotes (the length of) the longest common prefix of suffix $i$ and suffix $j$.

### Definition of the height array

$height[i]=lcp(sa[i],sa[i-1])$, i.e. the longest common prefix of the suffix ranked $i$-th and the suffix ranked just before it.

$height[1]$ can be treated as $0$.

### A lemma needed to compute the height array in O(n)

$height[rk[i]]\ge height[rk[i-1]]-1$

???+ note "Proof"
    When $height[rk[i-1]]\le1$, the inequality obviously holds (the right side is at most $0$).
    
    When $height[rk[i-1]]>1$:
    
    by the definition of $height$, we have $lcp(sa[rk[i-1]], sa[rk[i-1]-1]) = height[rk[i-1]] > 1$.
    
    Since suffix $i-1$ and suffix $sa[rk[i-1]-1]$ have a longest common prefix of length $height[rk[i-1]]$,
    
    let us denote this longest common prefix by $aA$. (Here $a$ is a character and $A$ is a non-empty string of length $height[rk[i-1]]-1$.)
    
    Then suffix $i-1$ can be written as $aAD$, and suffix $sa[rk[i-1]-1]$ as $aAB$. ($B < D$, $B$ may be empty, $D$ is non-empty.)
    
    Furthermore, suffix $i$ can be written as $AD$, and there exists a suffix ($sa[rk[i-1]-1]+1$) $AB$.
    
    Since suffix $sa[rk[i]-1]$ is ranked exactly one position below suffix $sa[rk[i]]$, i.e. suffix $i$, and $AB < AD$,
    
    we have $AB \leqslant$ suffix $sa[rk[i]-1] < AD$, so suffix $i$ and suffix $sa[rk[i]-1]$ obviously share the common prefix $A$.
    
    Hence $lcp(i,sa[rk[i]-1])$ is at least $height[rk[i-1]]-1$, i.e. $height[rk[i]]\ge height[rk[i-1]]-1$.

### Code for computing the height array in O(n)

It suffices to compute it directly using the lemma above:

```cpp
for (i = 1, k = 0; i <= n; ++i) {
  if (rk[i] == 0) continue;
  if (k) --k;
  while (s[i + k] == s[sa[rk[i] - 1] + k]) ++k;
  height[rk[i]] = k;
}
```

$k$ never exceeds $n$ and is decremented at most $n$ times, so it is incremented at most $2n$ times; the total complexity is $O(n)$.

## Applications of the height array

### Longest common prefix of two substrings

$lcp(sa[i],sa[j])=\min\{height[i+1..j]\}$

Intuitively: if $height$ stays greater than some number, the first that many characters never change; conversely, since the suffixes are already sorted, it is impossible for them to change and then change back.

For a rigorous proof see [\[2004\] Suffix arrays, by Xu Zhilei][1].

With this theorem, computing the longest common prefix of two substrings becomes an [RMQ problem](../topic/rmq.md).

### Comparing two substrings of a string

Suppose we need to compare $A=S[a..b]$ and $B=S[c..d]$.

If $lcp(a, c)\ge\min(|A|, |B|)$, then $A<B\iff |A|<|B|$.

Otherwise, $A<B\iff rk[a]< rk[c]$.

### Number of distinct substrings

A substring is a prefix of a suffix, so we can enumerate every suffix, count the total number of prefixes, and subtract the duplicates.

The "total number of prefixes" is in fact the number of substrings, $n(n+1)/2$.

If we enumerate the suffixes in suffix-sorted order, the new substrings added each time are the prefixes remaining after the LCP with the previous suffix. These prefixes are certainly new, otherwise the property $lcp(sa[i],sa[j])=\min\{height[i+1..j]\}$ would be violated. Only these prefixes are new, because the LCP part was already counted when enumerating the previous suffix.

So the answer is:

$\frac{n(n+1)}{2}-\sum\limits_{i=2}^nheight[i]$

### Maximum length of a substring occurring at least k times

Example problem: ["USACO06DEC" Milk Patterns](https://www.luogu.com.cn/problem/P2852).

??? note "Solution"
    Occurring at least $k$ times means that after suffix sorting there are at least $k$ consecutive suffixes with this substring as a common prefix.
    
    So the answer is the maximum over the minima of every $k-1$ adjacent $height$ values.
    
    This can be solved with a monotonic queue in $O(n)$, but other methods are enough to get AC too.

??? note "Reference code"
    ```cpp
    --8<-- "docs/string/code/sa/sa_2.cpp"
    ```

### Whether some string occurs at least twice in the text without overlapping

We can binary search the length $|s|$ of the target string, split the $h$ array into segments of consecutive LCPs greater than or equal to $|s|$, and use RMQ to find the maximum and minimum index occurring in each segment; if the distance between these two indices satisfies the condition, there must be a string of length $|s|$ occurring twice without overlapping.

### Several consecutive equal substrings

We can enumerate the length $|s|$ of the repeated string, split the whole string into blocks of size $|s|$, and query LCP and LCS at the starts of two adjacent blocks; for details see [\[2009\] Suffix arrays – a powerful tool for processing strings][2].

Example problem: ["NOI2016" Excellent partition](https://loj.ac/p/2083).

### Combined with disjoint set union

Some problems require you to split the suffix array into segments where consecutive LCP lengths are greater than or equal to some value, i.e. to split the $h$ array into segments whose minimum is greater than or equal to some value and compute the answer for each segment. If there are multiple queries, we can process them offline. We observe that as the given value decreases monotonically, the number of segments satisfying the condition keeps decreasing, and each new segment is formed by joining two or more old segments, where the parts of the new segment not contained in the old segments all have $h$ equal to the value just reached. We only need to maintain a disjoint set union, merging two adjacent segments each time and maintaining the statistics.

Classic problem: ["NOI2015" Wine tasting](https://uoj.ac/problem/131)

### Combined with a segment tree

Some problems ask for the first several numbers satisfying a condition, and these numbers lie within one interval of the suffix order. Then we can use the property of merge sort to merge the information of two nodes, and use a segment tree to maintain and query the answer for an interval.

### Combined with a monotonic stack

Example problem: ["AHOI2013" Difference](https://loj.ac/problem/2377)

??? note "Solution"
    The first two terms of the summand are easy to handle: they equal $n(n-1)(n+1)/2$ (every suffix appears $n-1$ times, and the total length of the suffixes is $n(n+1)/2$); the key is the last term, i.e. the pairwise LCP of the suffixes.
    
    We know that $lcp(i,j)=k$ is equivalent to $\min\{height[i+1..j]\}=k$. So we can attribute $lcp(i,j)$ as the contribution to the answer of the position $\min\{x|i+1\le x\le j, height[x]=lcp(i,j)\}$.
    
    Consider which suffixes' LCP each position contributes to the answer: it is in fact choosing one suffix among the consecutive suffixes to its left whose $height$ is greater than its own, and one among the consecutive suffixes to its right whose $height$ is not less than its own. This can be computed with a [monotonic stack](../ds/monotonic-stack.md).
    
    The monotonic stack part is similar to [Luogu P2659 Beautiful sequence](https://www.luogu.com.cn/problem/P2659) and the [hanging line method](../misc/hoverline.md).

??? note "Reference code"
    ```cpp
    --8<-- "docs/string/code/sa/sa_3.cpp"
    ```

Similar problem: ["HAOI2016" Find equal characters](https://loj.ac/problem/2064).

## Practice problems

-   [UVa 760 - DNA Sequencing](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=24&page=show_problem&problem=701)
-   [UVa 1223 - Editor](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=24&page=show_problem&problem=3664)
-   [Codechef - Tandem](https://www.codechef.com/problems/TANDEM)
-   [Codechef - Substrings and Repetitions](https://www.codechef.com/problems/ANUSAR)
-   [Codechef - Entangled Strings](https://www.codechef.com/problems/TANGLED)
-   [Codeforces - Martian Strings](http://codeforces.com/problemset/problem/149/E)
-   [Codeforces - Little Elephant and Strings](http://codeforces.com/problemset/problem/204/E)
-   [SPOJ - Ada and Terramorphing](http://www.spoj.com/problems/ADAPHOTO/)
-   [SPOJ - Ada and Substring](http://www.spoj.com/problems/ADASTRNG/)
-   [UVa - 1227 - The longest constant gene](https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=3668)
-   [SPOJ - Longest Common Substring](http://www.spoj.com/problems/LCS/en/)
-   [UVa 11512 - GATTACA](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=2507)
-   [QOJ 11240 - Suffixes and Palindromes](https://qoj.ac/problem/11240)
-   [GYM - Por Costel and the Censorship Committee](http://codeforces.com/gym/100923/problem/D)
-   [UVa 1254 - Top 10](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=3695)
-   [UVa 12191 - File Recover](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=3343)
-   [UVa 12206 - Stammering Aliens](https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=3358)
-   [Codechef - Jarvis and LCP](https://www.codechef.com/problems/INSQ16F)
-   [Luogu P8617 - Repeated pattern](https://www.luogu.com.cn/problem/P8617)
-   [UVa 11107 - Life Forms](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=2048)
-   [UVa 12974 - Exquisite Strings](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=862&page=show_problem&problem=4853)
-   [UVa 10526 - Intellectual Property](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1467)
-   [UVa 12338 - Anti-Rhyme Pairs](https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=3760)
-   [DevSkills Reconstructing Blue Print of Life](https://devskill.com/CodingProblems/ViewProblem/328)
-   [UVa 12191 - File Recover](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=3343)
-   [SPOJ - Suffix Array](http://www.spoj.com/problems/SARRAY/)
-   [Gym 102470J - Stammering Aliens](https://codeforces.com/gym/102470/problem/J)
-   [SPOJ - LCS2](http://www.spoj.com/problems/LCS2/)
-   [Codeforces - Fake News (hard)](http://codeforces.com/contest/802/problem/I)
-   [SPOJ - Longest Commong Substring](http://www.spoj.com/problems/LONGCS/)
-   [SPOJ - Lexicographical Substring Search](http://www.spoj.com/problems/SUBLEX/)
-   [Codeforces - Forbidden Indices](http://codeforces.com/contest/873/problem/F)
-   [Codeforces - Tricky and Clever Password](http://codeforces.com/contest/30/problem/E)
-   [Gym 101470B - Circle of digits](https://codeforces.com/gym/101470/problem/B)

## References

This page (the part introduced in [4070a9b](https://github.com/OI-wiki/OI-wiki/pull/950/commits/4070a9b3db8576db16c74d3ec33806ad10476eef)) is mainly translated from the blog post [Суффиксный массив](http://e-maxx.ru/algo/suffix_array) and its English translation [Suffix Array](https://cp-algorithms.com/string/suffix-array.html). The Russian version is licensed under Public Domain + Leave a Link; the English version under CC-BY-SA 4.0.

Papers:

1.  [\[2004\] Suffix arrays, by Xu Zhilei][1]

2.  [\[2009\] Suffix arrays – a powerful tool for processing strings, by Luo Suiqian][2]

[1]: https://github.com/OI-wiki/libs/blob/master/%E9%9B%86%E8%AE%AD%E9%98%9F%E5%8E%86%E5%B9%B4%E8%AE%BA%E6%96%87/%E5%9B%BD%E5%AE%B6%E9%9B%86%E8%AE%AD%E9%98%9F2004%E8%AE%BA%E6%96%87%E9%9B%86/%E8%AE%B8%E6%99%BA%E7%A3%8A--%E5%90%8E%E7%BC%80%E6%95%B0%E7%BB%84.pdf "[2004] Suffix arrays, by Xu Zhilei"

[2]: https://github.com/OI-wiki/libs/blob/master/%E9%9B%86%E8%AE%AD%E9%98%9F%E5%8E%86%E5%B9%B4%E8%AE%BA%E6%96%87/%E5%9B%BD%E5%AE%B6%E9%9B%86%E8%AE%AD%E9%98%9F2009%E8%AE%BA%E6%96%87%E9%9B%86/11.%E7%BD%97%E7%A9%97%E9%AA%9E%E3%80%8A%E5%90%8E%E7%BC%80%E6%95%B0%E7%BB%84%E2%80%94%E2%80%94%E5%A4%84%E7%90%86%E5%AD%97%E7%AC%A6%E4%B8%B2%E7%9A%84%E6%9C%89%E5%8A%9B%E5%B7%A5%E5%85%B7%E3%80%8B/%E5%90%8E%E7%BC%80%E6%95%B0%E7%BB%84%E2%80%94%E2%80%94%E5%A4%84%E7%90%86%E5%AD%97%E7%AC%A6%E4%B8%B2%E7%9A%84%E6%9C%89%E5%8A%9B%E5%B7%A5%E5%85%B7.pdf "[2009] Suffix arrays – a powerful tool for processing strings, by Luo Suiqian"
