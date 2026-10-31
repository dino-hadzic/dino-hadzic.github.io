---
title: Partition numbers
---

Partition: a representation of a natural number $n$ as a sum of non-increasing positive integers.

$$
n=r_1+r_2+\ldots+r_k \quad r_1 \ge r_2 \ge \ldots \ge r_k \ge 1
$$

Each positive integer in the sum is called a part.

Partition number: $p_n$. The number of ways to partition the natural number $n$.

The partition numbers starting from $0$:

| n     | 0 | 1 | 2 | 3 | 4 | 5 | 6  | 7  | 8  |
| ----- | - | - | - | - | - | - | -- | -- | -- |
| $p_n$ | 1 | 1 | 2 | 3 | 5 | 7 | 11 | 15 | 22 |

## Partitions into k parts

The number of partitions of $n$ into exactly $k$ parts is called the number of partitions into $k$ parts and is denoted $p(n,k)$.

Clearly, the number of partitions into $k$ parts $p(n,k)$ is also the number of solutions of the following equation:

$$
n-k=y_1+y_2+\ldots+y_k\quad y_1\ge y_2\ge\ldots\ge y_k\ge 0
$$

If exactly $j$ parts in this equation are nonzero, there are exactly $p(n-k,j)$ solutions. Hence we have the sum:

$$
p(n,k)=\sum_{j=0}^k p(n-k,j)
$$

Taking the difference of two adjacent sums, we get:

$$
p(n,k)=p(n-1,k-1)+p(n-k,k)
$$

If we lay this out in a table, the number in each cell equals the number to its upper left plus the number located as many cells above it as the column index.

| k        | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| -------- | - | - | - | - | - | - | - | - | - |
| $p(0,k)$ | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| $p(1,k)$ | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| $p(2,k)$ | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| $p(3,k)$ | 0 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 |
| $p(4,k)$ | 0 | 1 | 2 | 1 | 1 | 0 | 0 | 0 | 0 |
| $p(5,k)$ | 0 | 1 | 2 | 2 | 1 | 1 | 0 | 0 | 0 |
| $p(6,k)$ | 0 | 1 | 3 | 3 | 2 | 1 | 1 | 0 | 0 |
| $p(7,k)$ | 0 | 1 | 3 | 4 | 3 | 2 | 1 | 1 | 0 |
| $p(8,k)$ | 0 | 1 | 4 | 5 | 5 | 3 | 2 | 1 | 1 |

### Example problem

???+ note "Computing the number of partitions into k parts"
    Compute the number of partitions into $k$ parts $p(n,k)$. There are multiple test cases; $n$ is at most $10000$, $k$ is at most $1000$, and the answer is taken modulo $1000007$.
    
    Looking at the table and the recurrence, updating column by column is more favorable for storage. The program is easy to write:
    
    ```cpp
    #include <cstdio>
    #include <cstring>
    
    int p[10005][1005]; /*number of ways to partition the natural number n into k parts*/
    
    int main() {
      int n, k;
      while (~scanf("%d%d", &n, &k)) {
        memset(p, 0, sizeof(p));
        p[0][0] = 1;
        int i;
        for (i = 1; i <= n; ++i) {
          int j;
          for (j = 1; j <= k; ++j) {
            if (i - j >= 0) /*p[i-j][j]: all parts greater than 1*/
            {
              p[i][j] = (p[i - j][j] + p[i - 1][j - 1]) %
                        1000007; /*p[i-1][j-1]: at least one part equals 1.*/
            }
          }
        }
        printf("%d\n", p[n][k]);
      }
    }
    ```

### Generating function

From the formula for the sum of a geometric series, we have:

$$
\frac{1}{1-x^k}=1+x^k+x^{2k}+x^{3k}+\ldots
$$

$$
1+p_1 x+p_2 x^2+p_3 x^3+\ldots=\frac{1}{1-x}  \frac{1}{1-x^2}  \frac{1}{1-x^3}\ldots
$$

For partitions into $k$ parts, the generating function is slightly more complicated. Written out explicitly:

$$
\sum_{n,k=0}^\infty {p(n,k) x^n y^k }=\frac{1}{1-xy}  \frac{1}{1-x^2 y}  \frac{1}{1-x^3 y}\ldots
$$

### Ferrers diagram

Ferrers diagram: each part of a partition is represented by a row of dots. The number of dots in a row is the size of that part.

By the definition of a partition, the rows of a Ferrers diagram are arranged in decreasing order. The longest row is at the top.

For example, the Ferrers diagram of the partition $12=5+4+2+1$.

![](./images/ferrers.jpg)

Flipping a Ferrers diagram along its diagonal gives a new Ferrers diagram called the conjugate of the original, and the new partition is called the conjugate of the original partition. Clearly, conjugation is a symmetric relation.

For example, the conjugate of the partition $12=5+4+2+1$ above is the partition $12=4+3+2+2+1$.

Number of partitions with largest part $k$: the number of partitions of the natural number $n$ whose largest part is $k$.

By the definition of conjugation, we have the obvious conclusion:

The number of partitions with largest part $k$ equals the number of partitions into $k$ parts; both are $p(n,k)$.

## Partitions into distinct parts

Number of partitions into distinct parts: $pd_n$. The number of ways to partition the natural number $n$ into pairwise distinct parts. (Different)

| n      | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| ------ | - | - | - | - | - | - | - | - | - |
| $pd_n$ | 1 | 1 | 1 | 2 | 2 | 3 | 4 | 5 | 6 |

Similarly, we define the number of partitions into $k$ distinct parts $pd(n,k)$, representing partitions into distinct parts with at most $k$ parts; it is the number of solutions of this equation:

$$
n=r_1+r_2+\ldots+r_k\quad r_1>r_2>\ldots>r_k\ge 1
$$

Exactly as above, it is also the number of solutions of this equation:

$$
n-k=y_1+y_2+\ldots+y_k\quad y_1>y_2>\ldots>y_k\ge 0
$$

The difference from the previous case is that, because the parts are distinct, at most one part in the new equation can be zero. The conclusion stays the same: if exactly $j$ parts are different from $0$, there are exactly $pd(n-k,j)$ solutions, where $j$ can only be $k$ or $k-1$. Hence we directly obtain the recurrence:

$$
pd(n,k)=pd(n-k,k-1)+pd(n-k,k)
$$

Laying this out in a table just like binomial coefficients, the number in each cell equals the number in the previous column located as many cells above as the column index, plus the number in the same column located as many cells above as the column index.

| k         | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| --------- | - | - | - | - | - | - | - | - | - |
| $pd(0,k)$ | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| $pd(1,k)$ | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| $pd(2,k)$ | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| $pd(3,k)$ | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| $pd(4,k)$ | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| $pd(5,k)$ | 0 | 1 | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| $pd(6,k)$ | 0 | 1 | 2 | 1 | 0 | 0 | 0 | 0 | 0 |
| $pd(7,k)$ | 0 | 1 | 3 | 1 | 0 | 0 | 0 | 0 | 0 |
| $pd(8,k)$ | 0 | 1 | 3 | 2 | 0 | 0 | 0 | 0 | 0 |

### Example problem

???+ note "Computing the number of partitions into distinct parts"
    Compute the number of partitions into distinct parts $pd_n$. There are multiple test cases; $n$ is at most $50000$, and the answer is taken modulo $1000007$.
    
    Looking at the table and the recurrence, updating column by column is more favorable for storage. In the code the second dimension is compressed to save space, keeping only two adjacent columns.
    
    ```cpp
    #include <cstdio>
    #include <cstring>
    
    int pd[50005][2]; /*number of ways to partition the natural number n into k distinct parts*/
    
    int main() {
      int n;
      while (~scanf("%d", &n)) {
        memset(pd, 0, sizeof(pd));
        pd[0][0] = 1;
        int ans = 0;
        int j;
        for (j = 1; j < 350; ++j) {
          int i;
          for (i = 0; i < 350; ++i) {
            pd[i][j & 1] = 0; /*pd[i][j] depends only on pd[][j] and pd[][j-1]*/
          }
          for (i = 0; i <= n; ++i) {
            if (i - j >= 0) /*pd[i-j][j]: all parts greater than 1*/
            {
              pd[i][j & 1] = (pd[i - j][j & 1] + pd[i - j][(j - 1) & 1]) %
                             1000007; /*pd[i-j][j-1]: at least one part equals 1.*/
            }
          }
          ans = (ans + pd[n][j & 1]) % 1000007;
        }
        printf("%d\n", ans);
      }
    }
    ```

### Partitions into odd parts

Number of partitions into odd parts: $po_n$. The number of ways to partition the natural number $n$ into parts that are all odd. (Odd)

There is an obvious identity:

$$
\prod_{i=1}^\infty (1+x^i ) =\frac{\prod_{i=1}^\infty (1-x^{2i} ) }{\prod_{i=1}^\infty (1-x^i ) }=\prod_{i=1}^\infty \frac{1}{1-x^{2i-1} }
$$

The leftmost side is the generating function of the number of partitions into distinct parts, and the rightmost side is the generating function of the number of partitions into odd parts. Their corresponding coefficients are equal, so the number of partitions into odd parts equals the number of partitions into distinct parts:

$$
po_n=pd_n
$$

But clearly the number of partitions into $k$ odd parts and the number of partitions into $k$ distinct parts are not the same concept, so we do not list them here.

Let us introduce two more concepts:

Number of partitions into an even number of distinct parts: $pde_n$. The number of partitions of the natural number $n$ into distinct parts whose number of parts is even. (Even)

Number of partitions into an odd number of distinct parts: $pdo_n$. The number of partitions of the natural number $n$ into distinct parts whose number of parts is odd. (Odd)

Hence:

$$
pd_n=pde_n+pdo_n
$$

There are corresponding $k$-part concepts as well. Since they are too complicated, we do not list them.

## Pentagonal number theorem

Let us look separately at the denominator of the generating function of the partition numbers:

$$
\prod_{i=1}^\infty (1-x^i ) 
$$

Expanding this part, one is reminded of partitions into distinct parts, and the parity of the number of parts in such a partition matters.

Specifically, partitions into an even number of distinct parts are counted positively in the expansion, and partitions into an odd number of distinct parts are counted negatively. Therefore each coefficient of the expansion is the difference of these two counts, i.e.:

$$
\sum_{i=0}^\infty ({pde}_n-{pdo}_n ) x^n =\prod_{i=1}^\infty (1-x^i ) 
$$

Next we show that in most cases these two counts are equal, so the coefficient in the expansion is $0$; only at a few positions do the two counts differ by $1$ or $-1$.

Here we can use the method of constructing a correspondence (bijection).

Draw the Ferrers diagram of every partition into distinct parts. The last row is called the bottom of the diagram, and the number of dots on the bottom is denoted $b$ (Bottom); the longest $45$-degree segment connecting the last dot of the top row with some dot of the diagram is called the slide of the diagram, and the number of dots on the slide is denoted $s$ (Slide).

![](./images/bottom_slide.jpg)

To construct a correspondence between partitions into an even number of distinct parts and partitions into an odd number of distinct parts, we need to define a transformation that changes the number of rows by $1$ while keeping the parts distinct:

Transformation A: when $b$ is less than or equal to $s$, move the bottom to the right so that it becomes a new slide.

Transformation B: when $b$ is greater than $s$, move the slide to the bottom so that it becomes a new bottom.

For most $n$ and any partition into distinct parts, exactly one of these two transformations can be carried out, which constructs a one-to-one correspondence between partitions into an even number of distinct parts and partitions into an odd number of distinct parts. The numbers of partitions of the two kinds between which a one-to-one correspondence has been constructed are equal, so in this case the coefficient of the $n$-th term in the expansion is $0$.

But for some $n$, there exists exactly one partition into distinct parts on which the above transformations cannot be carried out.

-   Case 1: when $b=s$ and the bottom and the slide share a common dot, transformation A cannot be carried out. In this case

$$
n=s+(s+1)+\ldots+(s+s-1)=\frac{s(3s-1)}{2}
$$

The $n$-th term of the expansion depends on the parity of the number of parts of the partition and is $(-1)^s x^n$.

-   Case 2: when $b=s+1$ and the bottom and the slide share a common dot, transformation B cannot be carried out. In this case

$$
n=(s+1)+(s+2)+\ldots+(s+s)=\frac{s(3s+1)}{2}
$$

The $n$-th term of the expansion is $(-1)^s x^n$.

Replacing $s$ by $-s$ in the above expression gives $n=\frac{s(3s-1)}{2}$, where $s$ is a negative integer, and the $n$-th term of the expansion is still $(-1)^s x^n$.

Since the two cases cannot occur for the same $n$ simultaneously, we can combine the two conditions and obtain the condition that $n$ must satisfy:

$$
\exists k\in\mathbb{Z},n=\frac{k(3k-1)}{2}
$$

Thus we have proved:

$$
(1-x)(1-x^2 )(1-x^3 )\ldots=\sum_{k=-\infty}^{+\infty} (-1)^k x^{\frac{k(3k-1)}{2}} =\ldots+x^{26}-x^{15}+x^7-x^2+1-x+x^5-x^{12}+x^{22}-\ldots
$$

Recall that this expression is the reciprocal of the generating function of the partition numbers, so its product with the generating function of the partition numbers is $1$. Rearranging and comparing the coefficients on both sides, we obtain the recurrence for the sequence of partition numbers.

$$
(1+p_1 x+p_2 x^2+p_3 x^3+\ldots)(1-x-x^2+x^5+x^7-x^{12}-x^{15}+x^{22}+x^{26}-\ldots)=1
$$

$$
p_n=p_{n-1}+p_{n-2}-p_{n-5}-p_{n-7}+\ldots
$$

This recurrence has infinitely many terms, but if we stipulate that the partition number of a negative number is $0$ (the partition number of $0$ has already been defined as $1$), it reduces to finitely many terms.

### Example problem

???+ note "Computing partition numbers"
    Compute the partition number $p_n$. There are multiple test cases; $n$ is at most $50000$, and the answer is taken modulo $1000007$.
    
    We use the method of the pentagonal number theorem. The code:
    
    ```cpp
    #include <cstdio>
    
    long long a[100010];
    long long p[50005];
    
    int main() {
      p[0] = 1;
      p[1] = 1;
      p[2] = 2;
      int i;
      for (i = 1; i < 50005;
           i++) /*recurrence coefficients 1,2,5,7,12,15,22,26...i*(3*i-1)/2,i*(3*i+1)/2*/
      {
        a[2 * i] = i * (i * 3 - 1) / 2; /*pentagonal numbers are 1,5,12,22...i*(3*i-1)/2*/
        a[2 * i + 1] = i * (i * 3 + 1) / 2;
      }
      for (
          i = 3; i < 50005;
          i++) /*p[n]=p[n-1]+p[n-2]-p[n-5]-p[n-7]+p[12]+p[15]-...+p[n-i*[3i-1]/2]+p[n-i*[3i+1]/2]*/
      {
        p[i] = 0;
        int j;
        for (j = 2; a[j] <= i; j++) /*may be negative, so 1000007 is added in the expression*/
        {
          if (j & 2) {
            p[i] = (p[i] + p[i - a[j]] + 1000007) % 1000007;
          } else {
            p[i] = (p[i] - p[i - a[j]] + 1000007) % 1000007;
          }
        }
      }
      int n;
      while (~scanf("%d", &n)) {
        printf("%lld\n", p[n]);
      }
    }
    ```
