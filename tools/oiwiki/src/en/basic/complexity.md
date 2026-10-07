---
title: Complexity
---

Time complexity and space complexity are important measures of the efficiency of an algorithm.

## Number of basic operations

The same algorithm runs at somewhat different speeds on different computers, and the actual running speed is hard to compute theoretically and tedious to measure, so we usually consider not the actual running time of an algorithm but the number of basic operations it has to perform.

On an ordinary computer, addition, subtraction, multiplication, division, accessing a variable (of a basic data type, likewise below) and assigning to a variable can all be regarded as basic operations.

Counting or estimating the basic operations can serve as a measure of the running time of an algorithm.

## Time complexity

### Definition

When measuring how fast an algorithm is, the size of the data must be taken into account. Data size generally means the number of numbers in the input, the number of vertices and edges of a graph given in the input, and so on. Generally, the larger the data, the longer the algorithm takes. In competitive programming, when judging the efficiency of an algorithm, what matters most is not its running time at some particular data size but how its running time grows with the data size – the **time complexity**.

### Introduction

The main reasons for considering how running time grows with data size are:

1.  Modern computers perform hundreds of millions or more basic operations per second, so the data we handle is usually large. If algorithm A takes $100n$ on data of size $n$ and algorithm B takes $n^2$, then B is faster for sizes below $100$, but within one second A can handle data of size in the millions while B can only handle tens of thousands. When longer running times are allowed, the effect of time complexity on the manageable data size becomes even more pronounced, far exceeding the difference in running time at the same data size;
2.  We express running time by the number of basic operations, yet different basic operations take different amounts of time – e.g. addition and subtraction are much faster than division. Computing the time complexity while ignoring the differences between basic operations, and the difference between one and ten basic operations, removes the effect of these differing costs.

Of course, running time is not determined entirely by the input size; it also depends on the input contents. So time complexity comes in several kinds, e.g.:

1.  worst-case time complexity, i.e. the time complexity corresponding to the slowest input of each size. In competitive programming the input can be anything within the given constraints, so to guarantee that an algorithm passes every input in a given range we usually consider the worst-case time complexity;
2.  average-case (expected) time complexity, i.e. the expected running time under the assumption that all inputs are equally likely.

"How running time grows with data size" is a vague notion; we need the **asymptotic notation** introduced below to express time complexity formally.

## Definition of asymptotic notation

Asymptotic notation is a standard description of the order of a function. Simply put, it ignores the slower-growing parts of a function and the coefficients of its terms (in complexity analysis the coefficients are usually called "constants"), while keeping the important part that shows the growth trend of the function.

A simple mnemonic: with equality (non-strict) use uppercase, without equality (strict) use lowercase; equal is $\Theta$, less is $O$, greater is $\Omega$. Big $O$ and little $o$ are originally the Greek letter omicron, but since the glyphs are identical they can also be read as the Latin uppercase $O$ and lowercase $o$.

In English the roots "-micro-" and "-mega-" commonly denote $10^{-6}$ (one millionth) and $10^{6}$ (one million), and also "small" and "large". Small and large are also the meanings commonly attached to the Greek letters omicron and omega.

### Big Θ notation

For functions $f(n)$ and $g(n)$, $f(n)=\Theta(g(n))$ if and only if $\exists c_1,c_2,n_0>0$ such that $\forall n \ge n_0, 0\le c_1\cdot g(n)\le f(n) \le c_2\cdot g(n)$.

In other words, if $f(n)=\Theta(g(n))$, then we can find two positive numbers $c_1, c_2$ such that $f(n)$ is sandwiched between $c_1\cdot g(n)$ and $c_2\cdot g(n)$.

For example, $3n^2+5n-3=\Theta(n^2)$; here $c_1, c_2, n_0$ can be $2, 4, 100$ respectively. Also $n\sqrt {n} + n{\log^5 n} + m{\log m} +nm=\Theta(n\sqrt {n} + m{\log m} + nm)$, because $\log^5 n=o(\sqrt n)$, so there is a large enough $n_0$ for which the omitted term does not exceed $n\sqrt n$.

### Big O notation

The $\Theta$ notation gives both an upper and a lower bound of a function; if we only know an asymptotic upper bound but not a lower bound, we can use the $O$ notation. $f(n)=O(g(n))$ if and only if $\exists c,n_0>0$ such that $\forall n \ge n_0,0\le f(n)\le c\cdot g(n)$.

When studying time complexity we usually use $O$, because we usually care about an upper bound on the program's running time, not a lower bound.

Note that "upper bound" and "lower bound" here refer to the growth trend of the function, not to the algorithm. The upper bound on the running time of an algorithm corresponds to the "worst-case time complexity", not to the big $O$ notation. So it is perfectly fine to express worst-case time complexity with $\Theta$; one could even say $\Theta$ is more precise than $O$. The main reasons for using $O$ are: first, sometimes we can only prove an upper bound on the time complexity and not a lower bound (this usually happens with more complex algorithms and analyses); second, $O$ is easier to type on a computer.

### Big Ω notation

Similarly, we use $\Omega$ to describe an asymptotic lower bound of a function. $f(n)=\Omega(g(n))$ if and only if $\exists c,n_0>0$ such that $\forall n \ge n_0,0\le c\cdot g(n)\le f(n)$.

### Little o notation

If $O$ corresponds to "less than or equal", then $o$ corresponds to "less than".

Little $o$ is used extensively in mathematical analysis: the Taylor expansion of a function at a point has a Peano remainder, and little $o$ expresses "strictly smaller", enabling asymptotic analysis with equivalent infinitesimals.

$f(n)=o(g(n))$ if and only if for every given positive $c$ there exists $n_0$ such that $\forall n \ge n_0,0\le f(n)< c\cdot g(n)$.

### Little ω notation

If $\Omega$ corresponds to "greater than or equal", then $\omega$ corresponds to "greater than".

$f(n)=\omega(g(n))$ if and only if for every given positive $c$ there exists $n_0$ such that $\forall n \ge n_0,0\le c\cdot g(n)< f(n)$.

![](images/order.svg)

### Common properties

-   $f(n) = \Theta(g(n))\iff f(n)=O(g(n))\land f(n)=\Omega(g(n))$.
-   $f_1(n) + f_2(n) = O(\max(f_1(n), f_2(n)))$.
-   $f_1(n) \times f_2(n) = O(f_1(n) \times f_2(n))$.
-   $\forall a>1, \log_a{n} = O(\log_2 n)$. By the change-of-base formula, for any fixed real base $a>1$ all logarithmic functions have the same growth rate, so the base of the logarithm is usually omitted in asymptotic time complexity.

## Simple examples of computing time complexity

### `for` loops

=== "C++"
    ```cpp
    int n, m;
    std::cin >> n >> m;
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < n; ++j) {
        for (int k = 0; k < m; ++k) {
          std::cout << "hello world\n";
        }
      }
    }
    ```

=== "Python"
    ```python
    n = int(input())
    m = int(input())
    for i in range(0, n):
        for j in range(0, n):
            for k in range(0, m):
                print("hello world")
    ```

=== "Java"
    ```java
    int n, m;
    n = input.nextInt();
    m = input.nextInt();
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            for (int k = 0; k < m; ++k) {
                System.out.println("hello world");
            }
        }
    }
    ```

If we take the input values $n$ and $m$ as the data size, the time complexity of the code above is $\Theta(n^2m)$.

### DFS

When running [DFS](../graph/dfs.md) on a [connected graph](../graph/concept.md#连通) with $n$ vertices and $m$ edges stored as adjacency lists, each vertex and each edge is visited only a constant number of times, so the complexity is $\Theta(n+m)$.

## Which quantities are constants

When we perform some number of operations, how do we decide whether that number affects the time complexity? For example:

=== "C++"
    ```cpp
    constexpr int N = 100000;
    for (int i = 0; i < N; ++i) {
      std::cout << "hello world\n";
    }
    ```

=== "Python"
    ```python
    N = 100000
    for i in range(0, N):
        print("hello world")
    ```

=== "Java"
    ```java
    final int N = 100000;
    for (int i = 0; i < N; ++i) {
        System.out.println("hello world");
    }
    ```

If the size of $N$ is not regarded as input size, then the time complexity of this code is $O(1)$.

When computing time complexity it is very important which variables are regarded as the input size; all quantities independent of the input size are regarded as constants and can be treated as $1$ when computing complexity.

Note that in theoretical discussions of time complexity, "the algorithm can solve problems of any size" is a basic assumption (in practice, of course, problems that are too large cannot be solved because time and memory are limited). Therefore, being able to solve a problem of bounded size in constant time (e.g. by precomputing the answer for every possible input within the data range) does not make an algorithm's time complexity $O(1)$.

## Master theorem

We can use the master theorem to quickly obtain the complexity of recursive algorithms. Assume $a\ge1$, $b>1$ are constants, $f$ is non-negative and $T(1)=\Theta(1)$. To simplify the discussion, additionally assume $n=b^L$ with $L$ a non-negative integer. The recurrence is:

$$
T(n) = a T\left(\frac{n}{b}\right)+f(n),\qquad \forall n=b^L,\ L\ge1.
$$

Then

$$
T(n) = \begin{cases}
    \Theta(n^{\log_b a}), & f(n) = O(n^{\log_b (a)-\epsilon}),\epsilon > 0, \\
    \Theta(f(n)), & f(n) = \Omega(n^{\log_b (a)+\epsilon}),\epsilon\ge 0, \\
    \Theta(n^{\log_b a}\log^{k+1} n), & f(n)=\Theta(n^{\log_b a}\log^k n),k\ge 0.
    \end{cases}
$$

Note that the second case additionally requires the regularity condition: there is a constant $0<c<1$ such that $a f(n/b) \leq c f(n)$ for all sufficiently large $n$.

The idea of the proof is to decompose a problem of size $n$ into $a$ problems of size $n/b$, and then merge them level by level up to the top. Each merge of subproblems costs $f(n)$ time.

??? note "Proof"
    Following the idea above, the proof goes as follows:
    
    At level $0$ (the top), merging the subproblems costs $f(n)$.
    
    At level $1$ (the subproblems from the first split) there are $a$ subproblems, each costing $f\left(\dfrac{n}{b}\right)$ to merge, so merging costs $a f\left(\dfrac{n}{b}\right)$ in total.
    
    Continuing level by level, we can draw the following recursion tree:
    
    ![](./images/master-theorem-proof.svg)
    
    The tree ends at level $L=\log_b n$ and has $a^L=n^{\log_b a}$ leaves. The non-leaf levels are numbered $0,\ldots,L-1$, so $T(n) = \Theta(n^{\log_b a}) + g(n)$ where $g(n) = \sum_{j = 0}^{L-1} a^{j} f(n / b^{j})$.
    
    In the first case, $f(n) = O(n^{\log_b a-\epsilon})$, hence $g(n) = O(n^{\log_b a})$.
    
    In the second case, the cost of the root is $T(n)=\Omega(f(n))$. By the regularity condition, while the subproblems are still large enough the total cost of level $j$ is at most $c^j f(n)$, and these levels sum to $O(f(n))$. The remaining constant number of bottom levels and the leaves cost $O(n^{\log_b a})=O(f(n))$ in total, hence $T(n)=\Theta(f(n))$.
    
    In the third case, let $p=\log_b a$. For sufficiently large subproblems, the total cost of level $j$ is $\Theta(n^p(L-j)^k)$ where $k\ge0$ is a fixed constant. Fix $r_0\ge1$ such that $b^{r_0}$ reaches that size; from $\sum_{r=r_0}^L r^k=\Theta(L^{k+1})$ the total cost of these levels is $\Theta(n^p\log^{k+1}n)$. The remaining bottom levels and leaves cost $O(n^p)$ in total, and adding them gives the result.

Here are some examples of using the master theorem.

1.  $T(n) = 2T\left(\dfrac{n}{2}\right) + 1$: then $a=2, b=2, {\log_2 2} = 1$, $\epsilon$ can be taken in $(0, 1]$, so the first case applies and $T(n) = \Theta(n)$;

2.  $T(n) = T\left(\dfrac{n}{2}\right) + n$: then $a=1, b=2, {\log_2 1} = 0$, $\epsilon$ can be taken in $(0, 1]$, so the second case applies and $T(n) = \Theta(n)$;

3.  $T(n) = T\left(\dfrac{n}{2}\right) + {\log n}$: then $a=1, b=2, {\log_2 1}=0$, $k$ can be taken as $1$, so the third case applies and $T(n) = \Theta(\log^2 n)$;

4.  $T(n) = T\left(\dfrac{n}{2}\right) + 1$: then $a=1, b=2, {\log_2 1} = 0$, $k$ can be taken as $0$, so the third case applies and $T(n) = \Theta(\log n)$.

## Amortised complexity

See [Amortised analysis](./amortized-analysis.md) for details.

## Space complexity

Similarly, how the memory used by an algorithm grows with the input size is measured by its **space complexity**.

## Computational complexity

This article introduced complexity from the viewpoint of algorithm analysis; if you are interested, you can learn more at [Computational complexity](../misc/cc-basic.md).
