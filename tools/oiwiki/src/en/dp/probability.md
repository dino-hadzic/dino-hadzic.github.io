---
title: Probability DP
---

## Introduction

Probability DP is used to solve probability and expectation problems; we recommend first getting familiar with [Probability & expectation](../math/probability/exp-var.md). In general, probability problems are solved with a forward loop, while expectation problems use a backward loop. If the defined state transition equation has aftereffects, [Gaussian elimination](../math/numerical/gauss.md) is also needed. Probability DP is also tested in combination with other topics, e.g. [state compression](./state.md) or DP transitions on trees.

## Probability DP

These problems are solved by forward computation, i.e. from the initial state toward the result. As with general DP, the difficulty is still describing the state transition equation; the problems are merely wrapped in probability theory.

### Example

???+ example "[Codeforces 148D Bag of mice](https://codeforces.com/problemset/problem/148/D)"
    A bag contains $w$ white mice and $b$ black mice; the princess and the dragon take turns drawing mice from the bag. Whoever draws a white mouse first wins; if the bag becomes empty and nobody has drawn a white mouse, the dragon wins. The princess draws one mouse per turn; after the dragon draws a mouse, one more mouse runs out of the bag. The drawn mice and the escaping mouse are random. The princess draws first. Find the probability that the princess wins.

??? note "Solution"
    Let $f_{i,j}$ be the probability that the princess wins when it is her turn and the bag contains $i$ white and $j$ black mice. Boundary: $f_{0,j}=0$ since with no white mice the dragon wins, and $f_{i,0}=1$ since any drawn mouse is white and the princess wins.
    Consider the transitions of $f_{i,j}$:
    
    -   The princess draws a white mouse and wins. Probability $\dfrac{i}{i+j}$.
    -   The princess draws a black mouse, the dragon draws a white mouse, the dragon wins. Probability $\dfrac{j}{i+j}\cdot\dfrac{i}{i+j-1}$.
    -   The princess draws a black mouse, the dragon draws a black mouse, a black mouse escapes; transition to $f_{i,j-3}$. Probability $\dfrac{j}{i+j}\cdot\dfrac{j-1}{i+j-1}\cdot\dfrac{j-2}{i+j-2}$.
    -   The princess draws a black mouse, the dragon draws a black mouse, a white mouse escapes; transition to $f_{i-1,j-2}$. Probability $\dfrac{j}{i+j}\cdot\dfrac{j-1}{i+j-1}\cdot\dfrac{i}{i+j-2}$.
    
    Since we want the probability that the princess wins, the second case does not take part in the computation. We must also make sure the last two cases are valid, so we check the sizes of $i,j$: the third case needs at least 3 black mice, and the fourth needs 1 white and 2 black mice.

??? note "Sample code"
    ```cpp
    --8<-- "docs/dp/code/probability/probability_1.cpp"
    ```

### Exercises

-   [POJ3071 Football](http://poj.org/problem?id=3071)
-   [CodeForces 768D Jon and Orbs](https://codeforces.com/problemset/problem/768/D)

## Expectation DP

### Example

???+ example "[POJ2096 Collecting Bugs](http://poj.org/problem?id=2096)"
    A piece of software has $s$ subsystems and can produce $n$ kinds of bugs. Someone finds one bug per day; the bug belongs to some kind and to some subsystem. The probability that a bug belongs to a given subsystem is $\dfrac{1}{s}$, and the probability that it belongs to a given kind is $\dfrac{1}{n}$. Find the expected number of days until all $n$ kinds of bugs have been found and a bug has been found in each of the $s$ subsystems.

??? note "Solution"
    Let $f_{i,j}$ be the expected number of days to reach the target state when bugs of $i$ kinds and in $j$ subsystems have already been found. The target state is to have found bugs of $n$ kinds in $s$ subsystems. Hence $f_{n,s}=0$, because the target has been reached and no more days are needed; so we start the recurrence from the target state, and the answer is $f_{0,0}$.
    
    Consider the state transitions of $f_{i,j}$:
    
    -   $f_{i,j}$: the found bug belongs to one of the $i$ already found kinds and one of the $j$ subsystems, probability $p_1=\dfrac{i}{n}\cdot\dfrac{j}{s}$.
    -   $f_{i,j+1}$: the found bug belongs to one of the $i$ already found kinds but not to an already found subsystem, probability $p_2=\dfrac{i}{n}\cdot(1-\dfrac{j}{s})$.
    -   $f_{i+1,j}$: the found bug does not belong to an already found kind but belongs to one of the $j$ subsystems, probability $p_3=(1-\dfrac{i}{n})\cdot\dfrac{j}{s}$.
    -   $f_{i+1,j+1}$: the found bug belongs neither to an already found kind nor to an already found subsystem, probability $p_4=(1-\dfrac{i}{n})\cdot(1-\dfrac{j}{s})$.
    
    By linearity of expectation we obtain the state transition equation:
    
    $$
    \begin{aligned}
    f_{i,j} &= p_1\cdot f_{i,j}+p_2\cdot f_{i,j+1}+p_3\cdot f_{i+1,j}+p_4\cdot f_{i+1,j+1} + 1\\
    &= \dfrac{p_2\cdot f_{i,j+1}+p_3\cdot f_{i+1,j}+p_4\cdot f_{i+1,j+1}+1}{1-p_1}
    \end{aligned}
    $$

??? note "Sample code"
    ```cpp
    --8<-- "docs/dp/code/probability/probability_2.cpp"
    ```

???+ example "[\"NOIP2016\" Changing Classrooms](http://uoj.ac/problem/262)"
    Niuniu has classes in $n$ time slots; in slot $i$ the class is in classroom $c_i$, and he may apply to move it to classroom $d_i$; the application succeeds with probability $p_i$, and he may apply for at most $m$ classes. After the class in slot $i$ he must walk to the classroom of slot $i+1$. Given a graph with $v$ classrooms and $e$ paths, where moving costs stamina, which classes should he apply for so that the expected total stamina spent moving between classrooms is minimized, i.e. find the minimum expected total distance.

??? note "Solution"
    For this undirected connected graph, first compute shortest paths with Floyd, which makes the later state transitions convenient. Treat one move as one stage (going from slot $i$ to slot $i+1$ is one move); in each step there is probability $p_i$ of reaching $d_i$, but only $m$ of all the $d_i$ may be chosen, and probability $1-p_i$ of reaching $c_i$. Find the minimum expected total distance after all $n$ stages.
    
    Define $f_{i,j,0/1}$ as the minimum expected total distance when in slot $i$, having used $j$ classroom changes up to and including this slot, and changing (1) or not changing (0) the classroom in this slot. The answer is $\min \{f_{n,i,0},f_{n,i,1}\} ,i\in[0,m]$. Note the boundary $f_{1,0,0}=f_{1,1,1}=0$.
    
    Consider the state transitions of $f_{i,j,0/1}$:
    
    -   If we do not change in this stage, i.e. $f_{i,j,0}$. It may come from the previous state without a change, giving $f_{i-1,j,0}+w_{c_{i-1},c_{i}}$; it may also come from the previous state with a change, and using conditional and total probability we get $f_{i-1,j,1}+w_{d_{i-1},c_{i}}\cdot p_{i-1}+w_{c_{i-1},c_{i}}\cdot (1-p_{i-1})$. The state transition equation is:
    
    $$
    \begin{aligned}
    f_{i,j,0}=min(f_{i-1,j,0}+w_{c_{i-1},c_{i}},f_{i-1,j,1}+w_{d_{i-1},c_{i}}\cdot p_{i-1}+w_{c_{i-1},c_{i}}\cdot (1-p_{i-1}))
    \end{aligned}
    $$
    
    -   If we change in this stage, i.e. $f_{i,j,1}$. Similarly, it may come from the previous state without a change or with a change. Multiply by $(1-p_i)$ for the no-change case and by $p_i$ for the change case, enumerate all the cases that can occur and compute them. We do not spell out all transition cases here; after the previous example these transitions should be easy to write down.

??? note "Sample code"
    ```cpp
    --8<-- "docs/dp/code/probability/probability_3.cpp"
    ```

Comparing these two problems, we see that for expectation DP, whether a concrete value or an optimum is asked for has some influence on the form of the transitions; but whether the DP computes probabilities or expectations, it is inseparable from probability knowledge and from the steps of writing down and simplifying formulas, and the details to think about when writing the state transition equation are similar.

### Exercises

-   [HDU3853 LOOPS](https://acm.hdu.edu.cn/showproblem.php?pid=3853)
-   [HDU4035 Maze](https://acm.hdu.edu.cn/showproblem.php?pid=4035)
-   [\"SCOI2008\" Bonus Level](https://www.luogu.com.cn/problem/P2473)

## DP with aftereffects

### Example

???+ example "[CodeForces 24D Broken robot](https://codeforces.com/problemset/problem/24/D)"
    Given an $n \times m$ grid. A robot starts in row $x$, column $y$; in each step it chooses with equal probability to stay in place, move one step left, right, or down. If the robot is at the boundary it does not move outside the grid. Find the expected number of steps for the robot to reach the last row.

??? note "Solution"
    When $m=1$, each step has probability $\dfrac{1}{2}$ of staying and $\dfrac{1}{2}$ of moving down one cell; the answer is $2\cdot (n-x)$.
    Let $f_{i,j}$ be the expected number of steps for the robot to reach row $n$ starting from row i, column j; the final state is $f_{n,j}=0$.
    Since the robot chooses with equal probability to stay, move left, move right or move down, the state transitions of $f_{i,j}$ are:
    
    -   $f_{i,1}=\dfrac{1}{3}\cdot(f_{i+1,1}+f_{i,2}+f_{i,1})+1$
    -   $f_{i,j}=\dfrac{1}{4}\cdot(f_{i,j}+f_{i,j-1}+f_{i,j+1}+f_{i+1,j})+1$
    -   $f_{i,m}=\dfrac{1}{3}\cdot(f_{i,m}+f_{i,m-1}+f_{i+1,m})+1$
    
    Between rows only downward moves are possible, so there are no aftereffects. Between columns the robot can move left and right, which may create cycles, so the no-aftereffect property fails.
    Rearranging the equations gives:
    
    -   $2f_{i,1}-f_{i,2}=3+f_{i+1,1}$
    -   $3f_{i,j}-f_{i,j-1}-f_{i,j+1}=4+f_{i+1,j}$
    -   $2f_{i,m}-f_{i,m-1}=3+f_{i+1,m}$
    
    Since the recurrence runs backward, every $f_{i+1,j}$ is known.
    Since there are $m$ columns, the right-hand side is a column vector with $m$ rows, and the left-hand side is a matrix with $m$ rows and $m$ columns. Using the augmented matrix we get a matrix with $m$ rows and $m+1$ columns, and [Gaussian elimination](../math/numerical/gauss.md) then yields the answer.

??? note "Sample code"
    ```cpp
    --8<-- "docs/dp/code/probability/probability_4.cpp"
    ```

### Exercises

-   [HDU 4418 Time Travel](https://acm.hdu.edu.cn/showproblem.php?pid=4418)
-   [\"HNOI2013\" Random Walk](https://loj.ac/problem/2383)

## References

[kuangbin: Probability DP summary](https://www.cnblogs.com/kuangbin/archive/2012/10/02/2710606.html)
