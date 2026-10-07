---
title: 2-SAT
---

SAT is short for the satisfiability problem. Its general form is the k-satisfiability problem, k-SAT for short. For $k>2$ the problem is NP-complete, so we only study the case $k=2$.

## Definition

2-SAT, simply put, gives $n$ Boolean formulas, each involving two variables, such as $a \vee b$, meaning that at least one of the variables $a, b$ must hold. We then have to decide whether a satisfying assignment exists; obviously there may be several, and problems usually ask for just one. Also, $\neg a$ denotes the negation of $a$.

## Approach

???+ example "[Luogu P4782 \"Template\" 2-SAT](https://www.luogu.com.cn/problem/P4782)"
    There are $n$ Boolean variables $x_1\sim x_n$ and $m$ conditions to satisfy; each condition has the form "$x_i$ is `true`/`false` or $x_j$ is `true`/`false`". For example, "$x_1$ is true or $x_3$ is false", "$x_7$ is false or $x_2$ is false".
    
    The goal of the 2-SAT problem is to assign a value to every variable so that all conditions are satisfied.

Express the problem above with Boolean formulas. Let $a$ mean that $x_a$ is true (so $\neg a$ means that $x_a$ is false). If someone's requirements are $a$ and $b$, that is $(a \vee b)$ (at least one of the variables $a, b$ holds). Build a directed graph for these relations between variables: represent whether $a$ holds or not by vertices of the graph, and the edges $\neg a\to b$ and $\neg b\to a$ mean: if $a$ **does not hold**, then $b$ **must hold**; likewise, if $b$ **does not hold**, then $a$ **must hold**. Once the graph is built, we can solve the 2-SAT problem with the SCC condensation algorithm.

|     Original formula      |            Edges in the graph             |
| :----------------: | :-----------------------------: |
|   $\neg a \vee b$  | $a \to b$ and $\neg b \to \neg a$ |
|     $a \vee b$     | $\neg a \to b$ and $\neg b \to a$ |
| $\neg a\vee\neg b$ | $a \to \neg b$ and $b \to \neg a$ |

Many 2-SAT problems require finding relations of the form "if $a$ **does not hold**, then $b$ **holds**".

## Solving

Think about what it means for two vertices to be in the same strongly connected component. By the logical meaning of the edges described above: if two vertices are in the same strongly connected component, the conditions they represent are **either both satisfied or both unsatisfied**.

After building the graph, we [find the SCCs with Tarjan's algorithm](./scc.md) and check, for every Boolean variable $a$, whether the vertex representing "$a$ holds" and the vertex representing "$a$ does not hold" are in the same SCC (the same condition cannot be both satisfied and unsatisfied, or both unsatisfied and not-unsatisfied); if so, we output that there is no solution, otherwise a solution exists.

To output a solution, the value of a variable is determined by its topological order in the graph. If variable $x$ comes after $\neg x$ in topological order, set $x$ to true. Applied to Tarjan's condensation: when the index of the SCC containing $x$ is smaller than that of the SCC containing $\neg x$, set $x$ to true. This is because Tarjan's algorithm uses a stack when finding strongly connected components: a component that is later in the topological order after condensation is visited later in Tarjan's algorithm, so it is popped from the stack and condensed earlier and receives a smaller component index. Hence the SCC indices produced by Tarjan's algorithm correspond to the **reverse topological order**.

The algorithm traverses the whole graph once; since $n$ and $m$ are of the same order in this graph, computing the answer takes $O(n)$, so the total complexity is $O(n)$.

??? note "Implementation"
    ```cpp
    --8<-- "docs/graph/code/2-sat/2-sat_3.cpp"
    ```

## Examples

### Example 1

???+ example "[HDU3062 Party](https://acm.hdu.edu.cn/showproblem.php?pid=3062)"
    $n$ married couples are invited to a party, but because of venue limitations only one person from each couple may attend. Among the $2n$ people, some pairs have serious conflicts (of course spouses have none), and two people in conflict will not both show up at the party. Is it possible for $n$ people to attend at the same time?

Following the analysis above, if the husband of couple $a_1$ does not get along with the wife of couple $a_2$, we add an edge from the husband of $a_1$ to the husband of $a_2$ and an edge from the wife of $a_2$ to the wife of $a_1$, then condense, color and check.

??? note "Reference code"
    ```cpp
    --8<-- "docs/graph/code/2-sat/2-sat_1.cpp"
    ```

### Example 2

???+ example "[2018-2019 ACM-ICPC Asia Seoul Regional K TV Show Game](https://codeforces.com/gym/101987/problem/K)"
    There are $k$ lamps, each red or blue, but initially the colors are unknown. There are $n$ people; each chooses three lamps and guesses their colors. A person who guesses the colors of at least two lamps correctly wins a prize. Decide whether there is a coloring of the lamps such that everyone wins a prize, and if so output one such coloring.

According to [Wu Yu – "Solving 2-SAT problems by symmetry"](https://github.com/OI-wiki/libs/blob/master/%E9%9B%86%E8%AE%AD%E9%98%9F%E5%8E%86%E5%B9%B4%E8%AE%BA%E6%96%87/%E5%9B%BD%E5%AE%B6%E9%9B%86%E8%AE%AD%E9%98%9F2003%E8%AE%BA%E6%96%87%E9%9B%86/%E4%BC%8D%E6%98%B1--%E7%94%B1%E5%AF%B9%E7%A7%B0%E6%80%A7%E8%A7%A32-SAT%E9%97%AE%E9%A2%98/%E4%BC%8D%E6%98%B1.ppt), we conclude: to output a feasible solution of a 2-SAT problem, it suffices to select and delete bottom-up on the DAG obtained by Tarjan condensation.

In the implementation this can be done by building the reverse graph of the DAG and running a topological sort on it; or one can use the property that after Tarjan condensation a smaller component index means the vertex is closer to the leaves, and give priority to vertices with smaller component index.

The code for the second implementation is given below.

??? note "Reference code"
    ```cpp
    --8<-- "docs/graph/code/2-sat/2-sat_2.cpp"
    ```

## Exercises

-   [Luogu P5782 Peace Committee](https://www.luogu.com.cn/problem/P5782)
-   [POJ3683 Priest John's Busiest Day](http://poj.org/problem?id=3683)
