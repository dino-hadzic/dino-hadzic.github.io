---
title: Shell sort
---

This page briefly introduces Shell sort.

## Definition

**Shell sort**, also known as diminishing increment sort, is an improved version of [insertion sort](./insertion-sort.md). It is named after its inventor, Donald Shell.

## Procedure

The sort compares and moves records that are not adjacent:

1.  split the sequence to be sorted into several subsequences (the elements of each subsequence are equally spaced in the original array);
2.  sort these subsequences with insertion sort;
3.  decrease the gap between the elements of each subsequence and repeat the process until the gap is reduced to $1$.

For ease of analysis, below is the pseudocode of a single pass of insertion sort with gap $h$, denoted $\text{InsertionSort}(h)$. The indices of array $A$ run from $1$ to $n$, and $v$ holds the value currently being inserted; Shell sort calls this procedure for gaps from largest to smallest.

$$
\begin{array}{ll}
1 & \textbf{for } j\gets h+1 \textbf{ to } n\\
2 & \qquad v\gets A_j\\
3 & \qquad i\gets j-h\\
4 & \qquad \textbf{while } i\ge 1 \textbf{ and } A_i>v\\
5 & \qquad\qquad A_{i+h}\gets A_i\\
6 & \qquad\qquad i\gets i-h\\
7 & \qquad A_{i+h}\gets v
\end{array}
$$

## Properties

### Stability

Shell sort is an unstable sorting algorithm.

### Time complexity

The best-case time of Shell sort depends on the gap sequence and on whether it exits early; the $3h+1$ implementation without early exit given below has a best case of $\Theta(n\log n)$.

The average and worst-case time complexity of Shell sort depend on the choice of the gap sequence. Let the gap sequence be $H$; below are two classic choices of $H$, both of which bring the complexity of the sort down to $o(n^2)$.

???+ note "Proposition 1"
    If the gap sequence is $H= \{ 2^k-1\mid k=1,2,\ldots,\lfloor\log_2 n\rfloor \}$ (from largest to smallest), the time complexity of Shell sort is $O(n^{3/2})$.

???+ note "Proposition 2"
    If the gap sequence is $H= \{ k=2^p\cdot 3^q\mid p,q\in \mathbb N,k\le n \}$ (from largest to smallest), the time complexity of Shell sort is $O(n\log^2 n)$.

To prove these two propositions, we first state and prove an important theorem that reflects the main feature of Shell sort.

???+ note "Theorem 1"
    Once the program has executed $\text{InsertionSort}(h)$, no matter how the function $\text{InsertionSort}$ is called afterwards and how the array $A$ changes, each of the following subsequences remains sorted:
    
    $$
    \begin{array}{c}
    A_1,A_{1+h},A_{1+2h},\ldots \\
    A_2,A_{2+h},A_{2+2h},\ldots \\
    \vdots \\
    A_h,A_{h+h},A_{h+2h},\ldots
    \end{array}
    $$

Let us prove Theorem 1.

We first prove Lemma 1.

???+ note "Lemma 1"
    Let $n,m$ be nonnegative integers, $l$ a positive integer, and $X(x_1,x_2,\ldots,x_{n+l})$, $Y(y_1,y_2,\ldots,y_{m+l})$ two arrays satisfying:
    
    $$
    y_1 \le x_{n+1},y_2 \le x_{n+2},\ldots,y_l \le x_{n+l}
    $$
    
    Then, after sorting both arrays in ascending order, the condition above still holds.

??? note "Proof of Lemma 1"
    Let the sorted array $X$ be $X'(x'_1,\ldots,x'_{n+l})$ and the sorted array $Y$ be $Y'(y'_1,\ldots,y'_{m+l})$.
    
    For any $1\le i\le l$, $X$ contains at most $l-i$ elements strictly greater than $x'_{n+i}$. Hence among the chosen $l$ elements $\{x_{n+1},\ldots,x_{n+l}\}$ at least $i$ are not greater than $x'_{n+i}$. Denote them $x_{n+k_1},\ldots,x_{n+k_i}$; combined with the original paired inequalities we get:
    
    $$
    y_{k_1}\le x_{n+k_1}\le x'_{n+i},y_{k_2}\le x_{n+k_2}\le x'_{n+i},\ldots,y_{k_i}\le x_{n+k_i}\le x'_{n+i}
    $$
    
    So $x'_{n+i}$ is greater than or equal to at least $i$ elements of $Y$, i.e. of $Y'$, and therefore naturally $y'_i\le x'_{n+i}\,(1\le i\le l)$.

Back to the proof of the original statement. Let the length of the array be $N$. It suffices to prove that $\text{InsertionSort}(k)$ preserves existing $h$-sortedness, and then induct on the number of calls. Here $h,k$ are arbitrary positive integers. If $h\ge N$, there are no pairs of elements at distance $h$ to check, so the claim trivially holds. Below assume $h<N$.

Denote the array before and after the call by $A$ and $A'$. Before the call, $A_i\le A_{i+h}$ for $1\le i\le N-h$. For each $1\le w\le\min(k,N-h)$, write by division with remainder

$$
w+h=v+tk,\qquad 1\le v\le k,\quad t\ge0.
$$

Consider the two complete subsequences with gap $k$ starting at indices $w$ and $v$:

$$
Y=(A_w,A_{w+k},A_{w+2k},\ldots),\qquad
X=(A_v,A_{v+k},A_{v+2k},\ldots).
$$

Let there be exactly $l$ nonnegative integers $j$ with $w+h+jk\le N$. Then $X$ has length $t+l$ and $Y$ has length at least $l$; by the existing $h$-sortedness, the first $l$ terms of $Y$ and the last $l$ terms of $X$ satisfy

$$
y_{j+1}=A_{w+jk}\le A_{w+h+jk}=x_{t+j+1},\qquad 0\le j<l.
$$

$\text{InsertionSort}(k)$ sorts exactly each such complete subsequence in ascending order. By Lemma 1 the correspondence still holds after sorting, i.e.

$$
A'_{w+jk}\le A'_{w+h+jk},\qquad 0\le j<l.
$$

The lemma still applies even when $v=w$ and the two subsequences are actually the same. Every index $1\le i\le N-h$ can be uniquely written as $i=w+jk$ with $1\le w\le k$, $j\ge0$, and necessarily $w\le N-h$. Hence the discussion above covers all $i$ and gives $A'_i\le A'_{i+h}$, so $h$-sortedness is preserved and Theorem 1 is proved.

This theorem reveals the key to why Shell sort can achieve a better complexity with a particular set $H$: throughout the whole process it keeps the sortedness of the previously processed subsequences, so in later calls the number of moves of the pointer $i$ is greatly reduced.

Next we single out and prove a number-theoretic lemma. This theorem became very famous in the OI community because of the problem [Luogu P3951 Xiao Kai's Puzzle](https://www.luogu.com.cn/problem/P3951), and in the proof of the complexity of Shell sort it greatly extends Theorem $1$.

???+ note "Lemma 2"
    If $a,b\ge2$ are coprime integers, the largest positive integer not in the set $\{ax+by\mid x,y\in \mathbb N \}$ is $ab-a-b$.

??? note "Proof of Lemma 2"
    The proof has two steps:
    
    -   First we prove that the equation $ax+by=ab-a-b$ has no solution with both $x,y$ nonnegative integers:
    
        Without the nonnegativity restriction, two solutions $(b-1,-1),(-1,a-1)$ are easily found.
    
        From the form of the general solution $x=x_0+tb,y=y_0-ta$, it is easy to see that these two solutions are "adjacent" (since $b-1-b=-1$).
    
        As $t$ increases, $x$ increases and $y$ decreases, so if the equation had a nonnegative integer solution it would have to lie between these two solutions; but they are "adjacent" and there is no other solution between them.
    
        Hence there is no nonnegative integer solution.
    -   Then we prove that for any integer $c > ab-a-b$ the equation $ax+by=c$ has a nonnegative integer solution:
    
        Find a solution $(x_0,y_0)$ with $0\le x_0 < b$ (this is possible by the form of the general solution).
    
        Then:
    
        $$
        by_0=c-ax_0\ge c-a(b-1)>ab-a-b-ab+a=-b
        $$
    
        So $b(y_0+1) > 0$, and since $b>0$, we get $y_0+1>0$, i.e. $y_0\ge 0$.
    
        Hence $(x_0,y_0)$ is a nonnegative integer solution.
    
    This completes the proof.

The following theorem shows how Lemma $2$ extends Theorem $1$.

???+ note "Theorem 2"
    Let $h_{t+1}>h_t>h_{t-1}$ be positive integers. If $\gcd(h_{t+1},h_t)=1$, then after the program has executed $\text{InsertionSort}(h_{t+1})$ and $\text{InsertionSort}(h_t)$, executing $\text{InsertionSort}(h_{t-1})$ has time complexity $O\left(\dfrac{nh_{t+1}h_t}{h_{t-1}} \right)$, and for every $j$ the number of moves of $i$ is of order $O\left(\dfrac{h_{t+1}h_t}{h_{t-1}} \right)$.

??? note "Proof of Theorem 2"
    Below, $A$ denotes the array before the call to $\text{InsertionSort}(h_{t-1})$. Fix the index $j$ of the outer loop; the value to be inserted is $v=A_j$.
    
    For $j\le h_{t+1}h_t$, the number of moves of $i$ is obviously of order $O\left(\dfrac{h_{t+1}h_t}{h_{t-1}} \right)$.
    
    So below assume $j>h_{t+1}h_t$.
    
    For any positive integer $k$ with $1\le k\le j-h_{t+1}h_t$, note: $h_{t+1}h_t-h_{t+1}-h_t<h_{t+1}h_t\le j-k\le j-1$.
    
    Since $\gcd(h_{t+1},h_t)=1$, by Lemma $2$ there exist nonnegative integers $a,b$ such that $ah_{t+1}+bh_t=j-k$.
    
    That is:
    
    $$
    k=j-ah_{t+1}-bh_t
    $$
    
    By Theorem $1$:
    
    $$
    A_{j-bh_t}\le A_{j-(b-1)h_t}\le \ldots\le A_{j-h_t}\le A_j
    $$
    
    and
    
    $$
    A_{j-bh_t-ah_{t+1}}\le A_{j-bh_t-(a-1)h_{t+1}}\le \ldots\le A_{j-bh_t-h_{t+1}}\le A_{j-bh_t}
    $$
    
    Combining these gives $A_k=A_{j-ah_{t+1}-bh_t}\le A_j$.
    
    So for any $1\le k\le j-h_{t+1}h_t$ we have $A_k\le A_j$.
    
    In the already processed prefix of the subsequence that $v$ belongs to, only elements whose original index lies in $(j-h_{t+1}h_t,j)$ can be greater than $v$, and there are at most $\left\lceil\dfrac{h_{t+1}h_t}{h_{t-1}}\right\rceil$ of them. Earlier insertions only sorted the prefix of this subsequence, so in the pseudocode above $i$ decreases by $h_{t-1}$ each step and, once it has passed these elements, meets an element not greater than $v$ or runs off the left end of the array, which exits the while loop. The number of moves is $O\left(\dfrac{h_{t+1}h_t}{h_{t-1}} \right)$.
    
    Having proved the move complexity for each $j$, we obtain the total time complexity:
    
    $$
    \sum_{j=h_{t-1}+1}^n{O\left(\frac{h_{t+1}h_t}{h_{t-1}} \right)}=O\left(\frac{nh_{t+1}h_t}{h_{t-1}}\right)
    $$
    
    This completes the proof.

Looking carefully at the proof of Theorem $2$, we notice that Theorem 1 admits "linear combinations": if $A$ is sorted with gap $h$ and also sorted with gap $k$, then it is also sorted with any gap that is a linear combination of $h$ and $k$ with nonnegative coefficients. This "linearity" is exactly what Lemma $2$ guarantees.

With these two theorems we can prove Propositions $1$ and $2$.

??? note "Proof of Proposition 1"
    Write $H$ as a sequence:
    
    $$
    H(h_1=1,h_2=3,h_3=7,\ldots,h_{\lfloor \log_2 n\rfloor}=2^{\lfloor \log_2 n\rfloor}-1)
    $$
    
    Shell sort executes in order: $\text{InsertionSort}(h_{\lfloor \log_2 n\rfloor}),\text{InsertionSort}(h_{\lfloor \log_2 n\rfloor-1}),\ldots,\text{InsertionSort}(h_2),\text{InsertionSort}(h_1)$.
    
    Let $n\ge4$; we analyze the complexity in two parts:
    
    -   For the first several gaps $h_t$ satisfying $h_t\ge \sqrt{n}$, the time complexity of $\text{InsertionSort}(h_t)$ is obviously $O\left(\dfrac{n^2}{h_t} \right)$.
    
        Take $k=\min\{t:h_t\ge\sqrt n\}$; then $h_k=\Theta(\sqrt n)$ and:
    
        $$
        O\left(\frac{n^2}{h_k} \right)=O(n^{3/2})
        $$
    
        And for $h_i$ with $i> k$, since $2h_i< h_{i+1}$, we get:
    
        $$
        O\left(\frac{n^2}{h_i} \right)=O(n^{3/2}/2^{i-k})\,(i>k)
        $$
    
        So the total time complexity of the part with gaps at least $\sqrt n$ is:
    
        $$
        \sum_{i=k}^{\lfloor \log_2 n\rfloor}{O(n^{3/2}/2^{i-k})}=O(n^{3/2})
        $$
    -   For the remaining terms with $h_t< \sqrt{n}$, the complexity of the first two is still $O(n^{3/2})$, while for the later terms $h_t$, by Theorem $2$ the time complexity is:
    
        $$
        O\left(\frac{nh_{t+2}h_{t+1}}{h_t} \right)=O\left(\frac{nh_{t+2}\cdot h_{t+2}/2}{h_{t+2}/4} \right)=O(nh_{t+2})
        $$
    
        Using the property $2h_i < h_{i+1}$ again, the total time complexity of this part is ($k$ below has the same meaning as in the previous case):
    
        $$
        2O(n^{3/2})+\sum_{i=1}^{k-3}{O(nh_{i+1})}=O(n^{3/2})+\sum_{i=1}^{k-3}{O(nh_{k-1}/2^{k-i-3})}=O(n^{3/2})+O(nh_{k-1})=O(n^{3/2})
        $$
    
    Altogether, the total time complexity is $O(n^{3/2})$.

??? note "Proof of Proposition 2"
    Note the following fact: if $\text{InsertionSort}(2)$ and $\text{InsertionSort}(3)$ have already been executed, then since $2\cdot 3-2-3=1$, by Theorem $2$ for each element only the element immediately before it can be greater than it, and all earlier elements are smaller. So the pointer $i$ exits the while loop after at most two steps. In other words, executing $\text{InsertionSort}(1)$ at this point has complexity reduced to $O(n)$.
    
    Going further: if $\text{InsertionSort}(4)$ and $\text{InsertionSort}(6)$ have already been executed, consider the subsequence of elements with odd indices and the subsequence with even indices. This is equivalent to executing $\text{InsertionSort}(2)$ and $\text{InsertionSort}(3)$ on these two subsequences separately. Likewise, executing $\text{InsertionSort}(2)$ then is equivalent to executing $\text{InsertionSort}(1)$ on the two subsequences separately, which also takes only time of the order of the sum of the two lengths, i.e. $O(n)$, to make the array $2$-sorted.
    
    Continuing by induction we get: if $\text{InsertionSort}(2h)$ and $\text{InsertionSort}(3h)$ have already been executed, the complexity of executing $\text{InsertionSort}(h)$ is also only $O(n)$.
    
    Next we analyze the complexity in two parts:
    
    -   For the part with $h_t>n/3$, the complexity of executing each $\text{InsertionSort}(h_t)$ is $O(n^2/h_t)$.
    
        Since $n^2/h_t<3n$, the complexity of a single insertion sort is $O(n)$.
    
        The number of such terms is of order $O(\log^2 n)$, so the time complexity of this part is $O(n\log^2 n)$.
    -   For the part with $h_t\le n/3$, since $3h_t\le n$, $\text{InsertionSort}(2h_t)$ and $\text{InsertionSort}(3h_t)$ have already been executed before, so the time complexity of executing $\text{InsertionSort}(h_t)$ is $O(n)$.
    
        Likewise, the number of terms in this part is of order $O(\log^2 n)$, so the time complexity of this part is $O(n\log^2 n)$.
    
    Altogether, the total time complexity is $O(n\log^2 n)$.

### Space complexity

The space complexity of Shell sort is $O(1)$.

## Implementation

=== "C++[^ref1]"
    ```cpp
    template <typename T>
    void shell_sort(T array[], int length) {
      int h = 1;
      while (h < length / 3) {
        h = 3 * h + 1;
      }
      while (h >= 1) {
        for (int i = h; i < length; i++) {
          for (int j = i; j >= h && array[j] < array[j - h]; j -= h) {
            std::swap(array[j], array[j - h]);
          }
        }
        h = h / 3;
      }
    }
    ```

=== "Python"
    ```python
    def shell_sort(array, length):
        h = 1
        while h < length / 3:
            h = int(3 * h + 1)
        while h >= 1:
            for i in range(h, length):
                j = i
                while j >= h and array[j] < array[j - h]:
                    array[j], array[j - h] = array[j - h], array[j]
                    j -= h
            h = int(h / 3)
    ```

## References and notes

[^ref1]: [Shellsort – Wikipedia](https://en.wikipedia.org/wiki/Shellsort)
