---
title: WBLT
---

## Introduction

The **Weight Balanced Leafy Tree**, hereafter **WBLT**, is a kind of balanced tree whose main advantages over other balanced trees are a simple implementation and a small constant factor. It supports range operations and can be made persistent.

As the name suggests, the Weight Balanced Leafy Tree is a combination of the Weight Balanced Tree and the Leafy Tree.

In a Weight Balanced Tree, every node stores the size of the subtree below it, and the tree height is guaranteed by keeping the ratio between the sizes of the left and right subtrees within a certain range.

In a Leafy Tree, the original information is stored only in the **leaves**, while the internal nodes are used only to maintain information about their children and the shape of the data structure. The familiar segment tree is also a kind of Leafy Tree.

![](images/leafy-tree-1.svg)

Trees in this article always refer to binary Leafy Trees, i.e. every node has either $0$ or $2$ children. In this article, $n$ refers to the number of leaves of the tree. A tree with $n$ leaves has $2n-1$ nodes in total, so the space occupied by a WBLT is $\Theta(n)$.

## Basic structure and balance maintenance

This section introduces the basic structure of the WBLT, defines the concept of $\alpha$‑balance of a tree, and explains how to maintain the balance of the tree by rotations or by merging.

### Node information

To implement a basic WBLT, it suffices to record the following information in every node:

-   `lc[x]`, `rc[x]`: the left and right children;
-   `sz[x]`: the number of leaves in the subtree rooted at $x$.

To implement a balanced tree with a WBLT, information related to the keys must also be recorded in every node:

-   `val[x]`: the key at node $x$.

Since only the leaves actually store keys, the information stored at the other nodes is obtained by merging the information of their children, to facilitate later queries.

For example, a common way of merging is to store in the node the larger of the keys of its two children. In this way, every node stores the maximum key among all leaves in the subtree rooted at it. Based on this, the node information is updated as follows:

???+ example "Reference code"
    ```cpp
    --8<-- "docs/ds/code/wblt/wblt-1.cpp:push-up"
    ```

Of course, if needed, a corresponding `push_down(x)` function can also be implemented.

### Helper functions

Apart from the basic maintenance of node information, a WBLT usually also needs to implement the following helper functions for memory management:

-   `new_node()`: creates a new node;
-   `del_node(x)`: deletes node $x$;
-   `new_leaf(v)`: creates a new leaf with key $v$;
-   `join(x, y)`: joins subtrees, i.e. creates a new node $z$ with $x$ and $y$ as its left and right children;
-   `cut(x)`: cuts a subtree apart, i.e. obtains the two children of node $x$ and deletes node $x$.

If an implementation of the WBLT relies heavily on cutting and joining subtrees, it creates many new nodes and releases an equal number of old ones. If the old useless nodes are not recycled in time, the space is no longer linear. Below is an array implementation of these helper functions:

???+ example "Reference code"
    ```cpp
    --8<-- "docs/ds/code/wblt/wblt-1.cpp:helper"
    ```

Once these helper functions are encapsulated, there is no difference between the array implementation and the pointer implementation in the subsequent functions.

### The concept of balance

For a tree, we can define its **balance** at an internal node $x$ as

$$
\rho(x) = \dfrac{\min\{w(T_{\operatorname{left}(x)}),w(T_{\operatorname{right}(x)})\}}{w(T_x)}.
$$

Here $T_x$ denotes the subtree rooted at $x$, $w(\cdot)$ denotes the weight of a subtree (its number of leaves), and $\operatorname{left}(x)$ and $\operatorname{right}(x)$ denote the left and right children of $x$ respectively. In particular, at leaves we set $\rho(x)=1/2$.

For $\alpha\in(0,1/2]$, if the balance at some node $x$ satisfies $\rho(x)\ge\alpha$, the node is called **$\alpha$‑balanced**. If the tree is $\alpha$‑balanced at every node, the tree is called **$\alpha$‑balanced**. The set of such trees is denoted $BB[\alpha]$. A tree is **$\alpha$‑balanced** if and only if it is a leaf, or it is $\alpha$‑balanced at its root and both of its subtrees are $\alpha$‑balanced.

An obvious benefit of a tree being $\alpha$‑balanced is that its height is $O(\log n)$. This is because, with every step from a leaf toward the root, the number of leaves contained in the subtree grows to at least $1/(1-\alpha)$ times the previous number, so only $O(\log_{\frac{1}{1-\alpha}}n) = O(\log n)$ steps can be made. This guarantees that in an $\alpha$‑balanced tree the complexity of a single query is always strictly $O(\log n)$, and the constant of the algorithm is inversely proportional to $\log(1/(1-\alpha))$ (base $2$). When $\alpha$ lies within the reasonable range given below, this constant is roughly $2\sim 3.5$.

The balance of a WBLT can usually be maintained by rotations or by merging. For a WBLT implemented in either way, the complexity of a single insertion, deletion, etc. is strictly $O(\log n)$. However, unlike the [Treap](./treap.md) with fixed priorities, the structure of a WBLT is not unique, so the structures of the trees obtained by the two maintenance methods differ, although this does not affect their use. Of course, balance can also be maintained with a strategy similar to the [scapegoat tree](./sgt.md), using rebuilding to achieve amortized $O(\log n)$ complexity, but this loses the advantages of the WBLT such as persistence and range operations, and is therefore not recommended.

Below we introduce the methods of maintaining balance by rotations and by merging respectively, and implement the corresponding balance maintenance and merge functions. Once these functions are encapsulated, the two ways of maintaining balance make no further difference in the subsequent concrete implementation of the balanced tree. Moreover, whichever method is used, the time complexity of a single balance maintenance operation is $O(1)$, and the complexity of a single merge of trees $T_1$ and $T_2$ is $O\left(\left|\log\dfrac{w(T_1)}{w(T_2)}\right|\right)$.

???+ info "Omitting the weight notation"
    To maintain the balance of a tree, only the weight information of the subtrees needs to be kept. Therefore, for convenience of exposition, the following two sections on balance maintenance will use the notation for a tree and for its weight interchangeably. For example, the weight of the subtree $x$ is also denoted by $x$ rather than $w(x)$. Similarly, the tree obtained by merging subtrees $x$ and $y$ is also denoted by its weight and written directly as the tree $x+y$.

### Maintenance by rotations

The rotation operation of the WBLT is exactly the same as the [rotation operation of the Treap](./treap.md#rotation), and the same rotation strategy as in the Treap can be used. Of course, a rotation itself can also be seen as a process of redistributing subtree weights, so it can also be done by cutting and joining subtrees. The results of the two implementations are exactly the same, but the second implementation is more convenient for making the WBLT persistent.

???+ example "Reference code"
    === "Not relying on joining"
        ```cpp
        --8<-- "docs/ds/code/wblt/wblt-1.cpp:rotate-not-by-joining"
        ```
    
    === "Relying on joining"
        ```cpp
        --8<-- "docs/ds/code/wblt/wblt-1.cpp:rotate-by-joining"
        ```

Suppose that after some modification operation on the tree, we are restoring the balance of the tree from the bottom up. Now the left and right subtrees $x$ and $y$ are no longer balanced with each other, but each of them is balanced itself. Without loss of generality, suppose the right subtree $y$ is too light, i.e. $y<\alpha(x+y)$. The shape of the tree is then as shown by the tree on the left of the figure.

![](images/wblt-balance.svg)

A naive balance maintenance strategy is to rotate $x$ to the root, so that its former right child $w$ together with $y$ becomes the right child of the new tree, while its former left child $z$ becomes the left child of the new tree. This amounts to moving the weight of $w$ from the left side of the original tree to its right side. If the weight of $w$ is appropriate, such an operation can restore the balance of the tree. The resulting tree is shown as the tree on the right of the figure.

However, if $w$ itself is too heavy, such an operation may move too much weight to the right subtree, making the left subtree of the new tree too light, i.e. $z<\alpha(x+y)$. In this case, since the weights of subtrees $z$ and $y$ are both too small, the only option is to split $w$ into two subtrees and join them with $z$ and $y$ respectively, so that they become the two subtrees of the new tree. This amounts to first rotating node $w$ to the position of node $x$, and then rotating it to the root. Again, the resulting tree can be expected to be balanced; its shape is shown as the tree in the middle of the figure.

These two rotation strategies are called single rotation and double rotation respectively. The choice between single and double rotation mainly depends on the proportion of the subtree $w$ relative to the subtree $x$, i.e. there is a threshold $\beta$ such that

-   when $w\le\beta x$, the single rotation strategy should be chosen;
-   when $w>\beta x$, the double rotation strategy should be chosen.

The difficulty lies in the choice of the threshold $\beta$, which requires some concrete calculation. Blum and Mehlhorn proved that for the parameters[^wrong-range]

$$
\alpha\in\left(\dfrac{2}{11},1-\dfrac{\sqrt{2}}{2}\right]\approx(0.182,0.292],~\beta=\frac{1}{2-\alpha},
$$

the above strategy combining single and double rotations can maintain the balance of a WBLT that became unbalanced due to a single insertion or deletion.

??? note "Proof"
    What needs to be proved is that if the tree becomes unbalanced after a single insertion or deletion, its balance can be restored by the above strategy. With reference to the figure above, let
    
    $$
    \rho_1 = \dfrac{y}{x+y}, ~\rho_2 = \dfrac{w}{x}, ~\rho_3 = \dfrac{v}{w}.
    $$
    
    Then $\rho_1<\alpha\le\rho_2,\rho_3\le 1-\alpha$. There is also an implicit condition here on the range of $\rho_1$:
    
    -   if the imbalance was caused by inserting a single element, then we should have
    
        $$
        \dfrac{y}{x-1+y} \ge \alpha \implies \rho_1 \ge \dfrac{\alpha y}{y+\alpha} \ge \dfrac{\alpha}{1+\alpha}.
        $$
    -   if the imbalance was caused by deleting a single element, then we should have
    
        $$
        \dfrac{y+1}{x+y+1} \ge \alpha \implies \rho_1 \ge \dfrac{\alpha y}{y+1-\alpha} \ge \dfrac{\alpha}{2-\alpha}.
        $$
    
    Since for $0<\alpha<1/2$ we always have $\alpha/(2-\alpha)<\alpha/(1+\alpha)$, deleting an element causes a more severe imbalance than adding an element, especially when the tree is very small.
    
    Next, the operation of restoring balance splits into two cases:
    
    ??? note "Case 1: $w$ is not too heavy, i.e. $\rho_2\le\beta$, single rotation"
        First, $z$ and $w+y$ are balanced. This is because
        
        $$
        \left(1-\dfrac{\alpha}{2-\alpha}\right)\alpha+\dfrac{\alpha}{2-\alpha} \le \dfrac{w+y}{x+y} = (1-\rho_1)\rho_2+\rho_1 < (1-\alpha)\dfrac{1}{2-\alpha}+\alpha.
        $$
        
        The expression on the left is always greater than $\alpha$ for $\alpha\in(0,1)$, and the expression on the right is never greater than $(1-\alpha)$ for $\alpha\in(0,1-\sqrt{2}/2]$.
        
        Second, $w$ and $y$ are balanced. Similarly, consider
        
        $$
        \dfrac{y}{w+y} = \dfrac{\rho_1}{(1-\rho_1)\rho_2+\rho_1}.
        $$
        
        On the one hand, for all $\alpha\in(0,(3-\sqrt{5})/2)$,
        
        $$
        \dfrac{y}{w+y} < \dfrac{\alpha}{(1-\alpha)\alpha+\alpha} < 1-\alpha.
        $$
        
        On the other hand, for all $\alpha\in(0,1/3)$, except in the case of deleting an element with $y=1$, we have
        
        $$
        \rho_1 \ge \min\left\{\dfrac{\alpha}{1+\alpha},\dfrac{2\alpha}{3-\alpha}\right\} = \dfrac{2\alpha}{3-\alpha},
        $$
        
        so
        
        $$
        \dfrac{y}{w+y} \ge \dfrac{\dfrac{2\alpha}{3-\alpha}}{\left(1-\dfrac{2\alpha}{3-\alpha}\right)\dfrac{1}{2-\alpha}+\dfrac{2\alpha}{3-\alpha}} > \alpha.
        $$
        
        Finally, consider the remaining case, i.e. deleting an element with $y=1$. The most likely imbalance occurs when $x=\lfloor 2/\alpha\rfloor-2$ and $w=\lfloor\beta x\rfloor$. The tree can be rebalanced if and only if
        
        $$
        \dfrac{1}{1+\lfloor\beta x\rfloor}\ge\alpha \iff \lfloor\beta x\rfloor\le\dfrac{1}{\alpha}-1 \iff \beta x < \dfrac{1}{\alpha} \iff x < \dfrac{2}{\alpha}-1.
        $$
        
        And this always holds. This completes the proof of this case. Note that the proof of the last case uses the fact that weights are always integers, and cannot be merged into the previous discussion.
    
    ??? note "Case 2: $w$ is too heavy, i.e. $\rho_2>\beta$, double rotation"
        First, $z+u$ and $v+y$ are balanced. This is because
        
        $$
        \dfrac{\alpha}{2-\alpha}+\left(1-\dfrac{\alpha}{2-\alpha}\right)\dfrac{1}{2-\alpha}\alpha < \dfrac{v+y}{x+y} = \rho_1+(1-\rho_1)\rho_2\rho_3 <\alpha+(1-\alpha)^3
        $$
        
        The expression on the left is always greater than $\alpha$ for $\alpha\in(0,1)$, and the expression on the right is always less than $(1-\alpha)$ for $\alpha\in(0,(3-\sqrt{5})/2)$.
        
        Then, $z$ and $u$ are balanced. This is because for $\alpha\in(0,1)$ we always have
        
        $$
        \alpha=\dfrac{\dfrac{1}{2-\alpha}\alpha}{1-\dfrac{1}{2-\alpha}(1-\alpha)}<\dfrac{u}{z+u} = \dfrac{\rho_2(1-\rho_3)}{1-\rho_2\rho_3} <\dfrac{(1-\alpha)^2}{1-(1-\alpha)\alpha} < 1-\alpha.
        $$
        
        Finally, $v$ and $y$ are balanced. Similarly to the other cases, consider
        
        $$
        \dfrac{y}{v+y} = \dfrac{\rho_1}{\rho_1+(1-\rho_1)\rho_2\rho_3}.
        $$
        
        On the one hand, for all $\alpha\in(0,1-\sqrt{2}/2]$,
        
        $$
        \dfrac{y}{v+y} < \dfrac{\alpha}{\alpha+(1-\alpha)\dfrac{1}{2-\alpha}\alpha} \le 1-\alpha.
        $$
        
        On the other hand,
        
        $$
        \dfrac{y}{v+y} \ge \dfrac{\rho_1}{\rho_1+(1-\rho_1)(1-\alpha)^2}.
        $$
        
        The expression on the right is not less than $\alpha$ if and only if
        
        $$
        \rho_1 \ge \dfrac{\alpha(1-\alpha)}{1+\alpha(1-\alpha)}.
        $$
        
        If the imbalance was caused by an insertion, then $\rho_1\ge \alpha/(1+\alpha)$, which obviously holds. Otherwise, the situation is somewhat more complicated:
        
        -   when $y\ge 3$, $\rho_1\ge 3\alpha/(4-\alpha)$, and $3\alpha/(4-\alpha)\ge\alpha(1-\alpha)/(1+\alpha(1-\alpha))$ holds for all $\alpha\in[1-\sqrt{3}/2,1)$;
        -   when $y=2$, the most likely imbalance occurs when $x=\lfloor 3/\alpha\rfloor-3$, $w=\lfloor(1-\alpha)x\rfloor$ and $v=\lfloor(1-\alpha)w\rfloor$, and then $y/(v+y)\ge\alpha$ holds for all $\alpha\in(3/22,1)$;
        -   when $y=1$, the most likely imbalance occurs when $x=\lfloor 2/\alpha\rfloor-2$, $w=\lfloor(1-\alpha)x\rfloor$ and $v=\lfloor(1-\alpha)w\rfloor$, and then $y/(v+y)\ge\alpha$ holds for all $\alpha\in(2/11,1)$.
        
        The discussion of the last two cases likewise uses the fact that the weights of all nodes are integers.
    
    Combining the two cases, for $\alpha\in(2/11,1-\sqrt{2}/2]$ the above strategy combining single and double rotations guarantees the balance of the tree.
    
    From this analysis one can see that the hardest case for maintaining balance occurs when deleting nodes from small trees. Apart from $\beta=1/(2-\alpha)$, the correctness proof for other choices of parameters can likewise be obtained by repeating the above process, except that some of the inequalities used need to be adjusted accordingly.

Later, Hirai and Yamamoto completely determined the range of all feasible $(\alpha,\beta)$ by a machine-checked proof; the result is a rather complicated two-dimensional figure:

![](images/wblt-param-range.svg)

In their paper they recommend the following strategy for maintaining balance:

-   when $x>3y$, declare an imbalance;
-   when $w\le 2z$, choose the single rotation strategy, otherwise choose the double rotation strategy.

The reason is that this is the only strategy within the feasible parameter range that can be expressed with simple integers, thereby avoiding the loss of efficiency caused by floating-point arithmetic. Their recommended strategy amounts to taking $(\alpha,\beta)=(1/4,2/3)$. In practice, suitable parameters can be chosen according to the specific situation.

A reference implementation follows:

???+ example "Reference code"
    ```cpp
    --8<-- "docs/ds/code/wblt/wblt-1.cpp:too-heavy"
    --8<-- "docs/ds/code/wblt/wblt-1.cpp:balance"
    ```

Once the balance maintenance strategy is implemented, the algorithm for merging two trees is very simple. Still assuming $x>y$, the merge strategy is as follows:

-   if the right subtree $y$ is empty, directly return the left subtree $x$;
-   if the left and right subtrees $x$ and $y$ are already balanced, i.e. $y\ge\alpha(x+y)$, directly join the two subtrees;
-   otherwise, merge the right subtree $w$ of $x$ with $y$, join the left subtree $z$ with the result of their merge, and rebalance the new tree.

A reference implementation follows:

???+ example "Reference code"
    ```cpp
    --8<-- "docs/ds/code/wblt/wblt-1.cpp:merge-by-balancing"
    ```

It can be proved that this maintains the balance of the merged tree, and that the complexity of this operation is $O(|\log(x/y)|)$.

??? note "Proof of balance and complexity"
    It suffices to consider the case where $y$ is too light, i.e. $y<\alpha(x+y)$. In this case, we first merge $w$ and $y$, then join $z$ and $w+y$. What needs to be proved is that adjusting the balance only at the root of the tree suffices to guarantee the balance of the tree. Suppose the left and right subtrees of the tree $w+y$ are $c$ and $d$ respectively, and the left and right subtrees of $c$ are $a$ and $b$ respectively. Adjusting the balance at the root splits into three cases:
    
    ??? note "Case 1: $z$ and $w+y$ are already balanced and no further adjustment is needed, i.e. $z\ge\alpha(x+y)$"
        By the definition of balance, the subtrees $z$ and $w+y$ are both balanced and balanced with each other, so the whole tree is balanced too.
    
    ??? note "Case 2: $z$ is too light and $c$ is not too heavy, so balance can be restored by a single rotation, i.e. $z<\alpha(x+y)$ and $c\le\beta(w+y)$"
        In this case, since $z$ and $w$ are balanced but $y$ is too light relative to $x = z+w$, the weight of the subtree $z$ satisfies
        
        $$
        \alpha(1-\alpha)(x+y) <  \alpha(z+w) \le z \le \alpha(x+y) .
        $$
        
        And the weight of $c$ satisfies
        
        $$
        \alpha(w+y) \le c \le \beta(w+y).
        $$
        
        Hence $z$ and $c$ are balanced with each other as long as
        
        $$
        \dfrac{\alpha}{1-\alpha}<\dfrac{1-\alpha}{\alpha}\alpha<\dfrac{c}{z}=\dfrac{w+y}{z}\dfrac{c}{w+y} < \dfrac{1-\alpha(1-\alpha)}{\alpha(1-\alpha)}\beta\le\dfrac{1-\alpha}{\alpha},
        $$
        
        which requires
        
        $$
        \beta\le \dfrac{(1-\alpha)^2}{1-\alpha(1-\alpha)}.
        $$
        
        Also, $z+c$ and $d$ are balanced with each other as long as
        
        $$
        \alpha\le (1-\beta)(1-\alpha)\le \dfrac{d}{w+y}\dfrac{w+y}{x+y}  = \dfrac{d}{x+y} < \dfrac{d}{c+d} \le 1-\alpha,
        $$
        
        which requires
        
        $$
        \beta \le \dfrac{1-2\alpha}{1-\alpha}.
        $$
    
    ??? note "Case 3: $z$ is too light and $c$ is too heavy, so balance can be restored by a double rotation, i.e. $z<\alpha(x+y)$ and $c>\beta(w+y)$"
        Similarly to Case 2, we have
        
        $$
        \begin{aligned}
        \alpha(1-\alpha)(x+y) < z &\le \alpha(x+y),\\
        \beta(w+y)<c &\le (1-\alpha)(w+y),\\
        \alpha c\le a,b &\le (1-\alpha)c.
        \end{aligned}
        $$
        
        Hence $z$ and $a$ are balanced with each other as long as
        
        $$
        \dfrac{\alpha}{1-\alpha}\le\dfrac{1-\alpha}{\alpha}\beta\alpha\le\dfrac{a}{z} = \dfrac{w+y}{z}\dfrac{a}{c+d} < \dfrac{1-\alpha(1-\alpha)}{\alpha(1-\alpha)}(1-\alpha)^2,
        $$
        
        which requires
        
        $$
        \beta\ge\dfrac{\alpha}{(1-\alpha)^2}.
        $$
        
        Second, $b$ and $d$ are balanced with each other as long as
        
        $$
        \dfrac{\alpha}{1-\alpha}\le\dfrac{\beta}{1-\beta}\alpha \le \dfrac{b}{d} = \dfrac{c}{d}\dfrac{b}{c} \le \dfrac{1-\alpha}{\alpha}(1-\alpha) < \dfrac{1-\alpha}{\alpha},
        $$
        
        which requires
        
        $$
        \beta\ge\dfrac{1}{2-\alpha}.
        $$
        
        Finally, $z+a$ and $b+d$ are balanced with each other as long as
        
        $$
        \alpha<(1-\alpha)(1-(1-\alpha)^2)\le\frac{b+d}{x+y} = \dfrac{w+y}{x+y}\dfrac{b+d}{w+y} < (1-\alpha(1-\alpha))(1-\beta\alpha) \le 1-\alpha,
        $$
        
        which requires
        
        $$
        \beta\ge\dfrac{\alpha}{1-\alpha+\alpha^2}.
        $$
    
    Combining the three cases, as long as
    
    $$
    0<\alpha\le 1-\dfrac{\sqrt{2}}{2},~\dfrac{1}{2-\alpha}\le\beta\le\dfrac{1-2\alpha}{1-\alpha},
    $$
    
    it is guaranteed that the merged tree can be adjusted to balance by the strategy combining single and double rotations. This obviously includes the parameter range given in the main text.
    
    Finally, let us briefly explain why the complexity of this algorithm is $O(|\log(x/y)|)$. In the merge procedure, if $y$ is too light relative to $x$, we try to merge it with the right subtree of $x$; this process continues until the subtree rooted at some descendant of $x$ is balanced with $y$. Since with every level descended the subtree weight shrinks to at most $(1-\alpha)$ times the previous weight, at most $\log_{\frac{1}{1-\alpha}}(x/y)$ iterations are needed to find a subtree balanced with $y$. Therefore, this merge algorithm calls the balancing algorithm $O(|\log(x/y)|)$ times[^merge-complexity-cmp], so the complexity is $O(|\log(x/y)|)$.
    
    Although it is not obvious, this argument relies on the following conclusion: in the process of repeatedly taking right subtrees, $y$ cannot go, within one iteration, from being too light relative to the subtree on the left to being too heavy relative to it. This is because the range of weights of subtrees that can be balanced with $y$ lies between $\alpha y/(1-\alpha)$ and $(1-\alpha)y/\alpha$. Therefore, if within one iteration we went from "$y$ too light" to "$y$ too heavy", the weight of the subtree of $x$ would have shrunk during that iteration to at least $\alpha^2/(1-\alpha)^2$ times the previous weight. But in a single iteration, the subtree weight can shrink to at most $\alpha$ times the previous weight, and in the above range of $\alpha$, $\alpha>\alpha^2/(1-\alpha)^2$. This shows that the presupposed situation is impossible, and after some iteration the situation in which $y$ is balanced with some subtree of $x$ must occur.

### Maintenance by merging

Merging two subtrees means that, under the guarantee that the keys of the left subtree are never greater than the keys of the right subtree, a new tree is built such that the information of all its leaves is exactly the union of the leaf information of the left and right subtrees, while guaranteeing the balance of the tree.

For this, there is the following strategy[^more-join] (still assuming $x\ge y$):

-   if the right subtree $y$ is empty, directly return the left subtree $x$;
-   if the left and right subtrees $x$ and $y$ are already balanced, i.e. $y\ge\alpha(x+y)$, directly join the two subtrees;
-   otherwise, the right subtree $y$ is too light, but if the left subtree $z$ of $x$ and $w+y$ can be balanced, i.e. $z\ge\alpha(x+y)$, first merge $w$ and $y$, then merge $z$ and $w+y$;
-   otherwise, both $z$ and $y$ are too light; in this case, first merge $z$ with the left subtree $u$ of $w$, then merge the right subtree $v$ of $w$ with $y$, and then **merge** the results of the two merges into the new tree.

Comparing this strategy with the balancing strategy above, one can see that the ways the nodes are combined in the last two cases are similar to the results of the single and double rotations in the balancing strategy above respectively, except that joining subtrees is replaced by merging.

It can be proved that when

$$
0<\alpha \le 1-\dfrac{\sqrt{2}}{2}\approx 0.292
$$

the tree obtained in this way is always balanced, and the complexity of this operation is $O(|\log(x/y)|)$. In other words, the cost of merging two trees is independent of their absolute sizes and depends only on their relative sizes.

??? note "Proof of balance and complexity"
    Let $\tau(x,y)$ be the number of times two subtrees are directly joined when merging two subtrees of weights $x$ and $y$. Strictly speaking, we need to prove that when $0<\alpha\le 1-\sqrt{2}/2$, there exists a constant $C>0$ such that for all $x\ge y>0$,
    
    $$
    \tau(x,y) \le 1+C\log^+\dfrac{\alpha x}{(1-\alpha)^2y},
    $$
    
    where $\log^+ x = \max\{0,\log x\}$; moreover, for all $x/y\le(1-\alpha)/\alpha$, $\tau(x,y)=1$. In fact, the constant in the formula can be taken as
    
    $$
    C = -\dfrac{2}{\log(1-\alpha)}.
    $$
    
    This shows that the complexity of the merge algorithm is $O(|\log(x/y)|)$.
    
    To prove that the tree obtained by the merge algorithm is always balanced and that the above complexity expression holds, we use induction. All lattice points in the first quadrant $(x,y)\in\mathbf N^2_+$ can be ordered lexicographically by $(x+y,|x-y|)$; this is obviously a well-order on this set, and we can perform induction along this order. The base case is $(x,y)=(1,1)$; then both subtrees have only one leaf, the subtree obtained by direct joining is necessarily balanced, and $\tau(x,y)=1$, in accordance with the formula above. Now suppose the induction has reached $(x,y)$ and the conclusion holds for all points before $(x,y)$. There are three cases:
    
    ??? note "Case 1: the trees $x$ and $y$ are balanced, i.e. $y\ge\alpha(x+y)$"
        In this case, the tree obtained by direct joining is also balanced, and the tree joining algorithm is called only once, so $\tau(x,y)=1$.
    
    ??? note "Case 2: the tree $y$ is too light, but $z$ is not too light, i.e. $y<\alpha(x+y)\le z$"
        In this case, first merge $w$ and $y$, then merge $z$ and $w+y$, so
        
        $$
        \tau(x,y) = \tau(w,y) + \tau(z,w+y).
        $$
        
        By the induction hypothesis, the subtree $w+y$ is already balanced. For the second merge, one can actually prove directly that $z$ and $w+y$ are balanced:
        
        $$
        \alpha \le \dfrac{z}{z+(w+y)} = \dfrac{z}{x+y} < \dfrac{z}{z+w} \le 1-\alpha.
        $$
        
        Therefore, merging $z$ and $w+y$ is in fact a direct join of two subtrees, and $\tau(z,w+y) = 1$. Hence the final tree is also balanced.
        
        Now estimate the size of $\tau(w,y)$. Since $y<(\alpha/(1-\alpha))x$ and $\alpha x\le w\le(1-\alpha)x$, by bounding we get
        
        $$
        \dfrac{\alpha}{1-\alpha}<1-\alpha=\dfrac{\alpha x}{(\alpha/(1-\alpha))x}< \dfrac{w}{y} \le \dfrac{(1-\alpha)x}{y}.
        $$
        
        This shows that $w$ and $y$ can be unbalanced only when $w>y$, so
        
        $$
        \begin{aligned}
        \tau(w,y) &\le 1+C\log^+\dfrac{\alpha w}{(1-\alpha)^2y} \le 1+C\log^+\dfrac{\alpha x}{(1-\alpha)y} \\
        &= 1 + C\log(1-\alpha) + C\log^+\dfrac{\alpha x}{(1-\alpha)^2y}.
        \end{aligned}
        $$
        
        The equality in the last step holds because $x/y>(1-\alpha)/\alpha$.
        
        Therefore,
        
        $$
        \tau(x,y) \le 2 + C\log(1-\alpha) + C\log^+\dfrac{\alpha x}{(1-\alpha)^2y}.
        $$
    
    ??? note "Case 3: the trees $y$ and $z$ are both too light, i.e. $y,z<\alpha(x+y)$"
        In this case, first merge $z$ and $u$, then merge $v$ and $y$, and finally merge $z+u$ and $v+y$. Therefore,
        
        $$
        \tau(x,y) = \tau(z,u) + \tau(v,y) + \tau(z+u,v+y).
        $$
        
        Similarly to the previous case, we can estimate the weight ratio of the two subtrees in each merge.
        
        Since $z,y<\alpha(x+y)$, we have $w>(1-2\alpha)(x+y)$. At the same time, by the balance conditions, $\alpha\le z/x,w/x,u/w,v/w\le 1-\alpha$. This shows that
        
        $$
        \begin{aligned}
        \dfrac{\alpha}{1-\alpha}<\dfrac{\alpha}{1-\alpha}\frac{1}{1-\alpha}\le \dfrac{z}{u} &= \dfrac{z}{w}\dfrac{w}{u} < \dfrac{\alpha}{1-2\alpha}\dfrac{1}{\alpha} \le \dfrac{1-\alpha}{\alpha},\\
        \dfrac{\alpha}{1-\alpha}\le\alpha\dfrac{1-2\alpha}{\alpha}< \dfrac{v}{y} &= \dfrac{v}{w}\dfrac{w}{y} \le (1-\alpha)\dfrac{(1-\alpha)x}{y} = (1-\alpha)^2\dfrac{x}{y}.
        \end{aligned}
        $$
        
        For the last term, we have
        
        $$
        \dfrac{z+u}{v+y} = \dfrac{x+y}{v+y}-1 = \dfrac{x+y}{y}\dfrac{y}{v+y} - 1 < (1-\alpha)\left(\dfrac{x}{y}+1\right)-1 < (1-\alpha)\dfrac{x}{y}.
        $$
        
        Conversely, we have
        
        $$
        \dfrac{z+u}{v+y} = \dfrac{x+y}{v+y}-1 \ge \dfrac{x+y}{(1-\alpha)^2x+y}-1 > \dfrac{1}{(1-\alpha)^3+\alpha}-1 > \dfrac{\alpha}{1-\alpha}.
        $$
        
        Using these inequalities, one can show that the final tree is necessarily balanced. By the induction hypothesis, merging $z$ and $u$ and merging $v$ and $y$ both guarantee that the resulting trees are balanced. Moreover, the first step, merging $z$ and $u$, is in fact a direct join of two trees. For merging the trees $z+u$ and $v+y$, there are two subcases:
        
        -   if $z+u\le v+y$, then their weight ratio is strictly greater than $\alpha/(1-\alpha)$, so they can be joined directly, and the result is balanced;
        -   otherwise, their weight ratio is necessarily strictly less than $x/y$, but $(z+u)+(v+y)=x+y$, so $|(z+u)-(v+y)|<|x-y|$; by the lexicographic order given above, the induction hypothesis can also be applied in this case, and the result is balanced too.
        
        Applying the induction hypothesis further gives:
        
        $$
        \begin{aligned}
        \tau(z,u) &= 1,\\
        \tau(v,y) &\le 1+C\log^+\dfrac{\alpha x}{y},\\
        \tau(z+u,v+y) &\le 1 + C\log^+\dfrac{\alpha x}{(1-\alpha)y}.
        \end{aligned}
        $$
        
        Directly adding the three inequalities would make the coefficient in front of the logarithmic term $2C$, and the induction could not be completed. Therefore, a more careful estimate is needed here.
        
        When $\min\{v/y,(z+u)/(v+y)\}\le(1-\alpha)/\alpha$, one of $\tau(v,y)$ and $\tau(z+u,v+y)$ must be $1$, so
        
        $$
        \begin{aligned}
        \tau(v,y) + \tau(z+u,v+y) &\le 2 + C\log^+\dfrac{\alpha x}{(1-\alpha)y}\\
        &= 2 + C\log(1-\alpha) + C\log^+\dfrac{\alpha x}{(1-\alpha)^2y}.
        \end{aligned}
        $$
        
        Otherwise, we should have
        
        $$
        \begin{aligned}
        \tau(v,y) + \tau(z+u,v+y) 
        &\le 2 + C\log^+\dfrac{\alpha v}{(1-\alpha)^2y} + C\log^+\dfrac{\alpha(z+u)}{(1-\alpha)^2(v+y)}\\
        &= 2 + C\log\dfrac{\alpha}{(1-\alpha)^2} + C\log^+\dfrac{\alpha v(z+u)}{(1-\alpha)^2y(v+y)}.
        \end{aligned}
        $$
        
        For $0<\alpha\le 1-\sqrt{2}/2$,
        
        $$
        \dfrac{\alpha}{(1-\alpha)^2} < 1-\alpha.
        $$
        
        Moreover,
        
        $$
        \begin{aligned}
        \dfrac{v(z+u)}{y(v+y)} &= \left(\dfrac{v+y}{y}-1\right)\left(\dfrac{x+y}{y}\dfrac{y}{v+y} - 1\right) \\
        &= \dfrac{x+y}{y} + 1 -\dfrac{x+y}{y}\dfrac{y}{v+y}-\dfrac{v+y}{y} < \dfrac{x}{y}.
        \end{aligned}
        $$
        
        This shows that in the latter case we also have
        
        $$
        \tau(v,y) + \tau(z+u,v+y) < 2 + C\log(1-\alpha) + C\log^+\dfrac{\alpha x}{(1-\alpha)^2y}.
        $$
        
        The overall merge complexity is
        
        $$
        \tau(x,y) \le 3 + C\log(1-\alpha) + C\log^+\dfrac{\alpha x}{(1-\alpha)^2y}.
        $$
    
    Combining all cases, we have
    
    $$
    \tau(x,y) \le 3 + C\log(1-\alpha) + C\log^+\dfrac{\alpha x}{(1-\alpha)^2y}.
    $$
    
    Therefore, it suffices to take $2+C\log(1-\alpha)\le 0$ to complete the induction for the complexity. An obvious choice is
    
    $$
    C = -\dfrac{2}{\log(1-\alpha)}.
    $$
    
    This constant shows that when merging two trees, the number of direct joins of subtrees roughly does not exceed twice the difference in tree heights.

A reference implementation follows:

???+ example "Reference code"
    ```cpp
    --8<-- "docs/ds/code/wblt/wblt-1.cpp:merge"
    ```

Using this merge strategy, balance maintenance of the tree is also easy to implement: when unbalanced, simply merge the left and right subtrees directly.

???+ example "Reference code"
    ```cpp
    --8<-- "docs/ds/code/wblt/wblt-1.cpp:balance-by-merging"
    ```

Since the sizes of the two trees that need rebalancing are always nearly balanced, the complexity of maintaining balance is $O(1)$.

## Basic balanced tree operations

Using the functions implemented above, a WBLT can support all basic operations of a balanced tree. This section takes a multiset as an example to discuss how to implement a balanced tree with a WBLT.

### Building the tree

Building the tree is very similar to a segment tree: simply recurse downward, bisecting the interval, until the interval length is $1$, at which point the information to be maintained is placed in a leaf, and merge the interval information when backtracking.

???+ example "Reference code"
    ```cpp
    --8<-- "docs/ds/code/wblt/wblt-2.cpp:build"
    ```

The time complexity is $O(n)$.

### Insertion and deletion

For insertion, we need to recurse downward from the root until we find the leaf with the smallest key among the leaves whose key is greater than or equal to the element to be inserted, then create two new nodes, one of which stores the newly inserted value, while the other, as the new parent of the two leaves, takes the place of this smallest leaf, and then attach these two leaves to this parent. When backtracking, the balance of the tree must be maintained.

![](./images/wblt-insert-delete.svg)

As shown in the figure, we want to insert an element with value $4$ into the tree on the left. First find the leaf with value $5$, then create the leaf $4$ and the internal node $\text{d}$, and attach $4$ and $5$ to $\text{d}$. This gives the tree on the right.

For deletion, consider the reverse of the above process. That is, find a leaf whose key equals the value to be deleted, delete it and its parent, and replace the parent's position with the parent's other child. When backtracking, the balance of the tree must likewise be maintained.

A reference implementation follows:

???+ example "Reference code"
    ```cpp
    --8<-- "docs/ds/code/wblt/wblt-1.cpp:insert-remove"
    ```

Pay attention to handling the empty tree. If you do not want to handle the empty tree, you can insert an $\infty$ element into the tree in advance.

The time complexity of both operations is $O(\log n)$.

### Querying the rank

Since the shape of a WBLT is very similar to a segment tree, the rank query can use a method similar to binary search on a segment tree: if the maximum of the left subtree is greater than or equal to the value being queried, jump to the left child; otherwise, jump to the right child and add the weight of the left subtree to the answer.

A reference implementation follows:

???+ example "Reference code"
    ```cpp
    --8<-- "docs/ds/code/wblt/wblt-1.cpp:rank"
    ```

The time complexity is $O(\log n)$.

### Querying by rank

Again we use the idea of binary search on a segment tree, except that here we compare the weights of the nodes.

A reference implementation follows:

???+ example "Reference code"
    ```cpp
    --8<-- "docs/ds/code/wblt/wblt-1.cpp:kth-element"
    ```

The time complexity is $O(\log n)$.

### Finding the predecessor and successor

Simply combine the two functions above.

A reference implementation follows:

???+ example "Reference code"
    ```cpp
    --8<-- "docs/ds/code/wblt/wblt-1.cpp:prev-next"
    ```

If you want to implement them directly, note that nodes with the same key may be stored in multiple leaves.

### Splitting

Splitting a WBLT is similar to the [non-rotating Treap](./treap.md#splitting-split): depending on the subtree size or key, decide whether to recursively split the left or the right subtree. The difference is that a WBLT needs to **merge** the split-off subtrees in order to maintain the balance of the final split trees.

A reference implementation of splitting by subtree size follows:

???+ example "Reference code"
    ```cpp
    --8<-- "docs/ds/code/wblt/wblt-2.cpp:split"
    ```

The time complexity is $O(\log n)$.

??? note "Complexity proof"
    The number of levels of downward recursion obviously does not exceed the tree height, which is $O(\log n)$. What needs to be proved is that the complexity of merging the subtrees split off on the left and right sides respectively is $O(\log n)$. We may consider only the subtrees on the left, since the right side is symmetric. Let the subtrees split off on the left be, from bottom to top, $T_1,T_2,\cdots,T_\ell$; the number of these subtrees is $\ell\in O(\log n)$. The merge process can be described as: starting from $T'_1=T_1$, merge $T'_{i-1}$ with $T_i$ to obtain $T'_i$, recursively until all subtrees are merged. The total complexity of merging can be expressed as
    
    $$
    \sum_{i=2}^\ell \tau(T_i,T'_{i-1}),
    $$
    
    where $\tau(T_i,T'_{i-1})$ is the complexity of merging $T_i$ and $T'_{i-1}$.
    
    If we always had $w(T_i)\ge w(T'_{i-1})$, then by the complexity expression for merging two subtrees,
    
    $$
    \tau(T_i,T'_{i-1}) \in O\left(\log\dfrac{w(T_i)}{w(T'_{i-1})}\right) \subseteq O\left(\log\dfrac{w(T'_i)}{w(T'_{i-1})}\right).
    $$
    
    Since the constants in these big-$O$ notations are all the same, they can be added directly and telescoped.
    
    However, it should be noted that $w(T_i)\ge w(T'_{i-1})$ does not always hold, because $T'_{i-1}$ is split off from the right subtree corresponding to $T_i$ in the original tree, and this right subtree may be larger than the left subtree $T_i$. Nevertheless, even if $T'_{i-1}$ is larger than $T_i$, as part of the right subtree, the weight $w(T'_{i-1})$ does not exceed $(1-\alpha)/\alpha$ times $w(T_i)$, which means that in this case $T'_{i-1}$ and $T_i$ must be balanced, and the complexity of merging is $O(1)$.
    
    Summarizing the two cases, the complexity of a single merge can be written as
    
    $$
    \tau(T_i,T'_{i-1}) \in O\left(\log\dfrac{w(T'_i)}{w(T'_{i-1})}\right) + O(1).
    $$
    
    Hence the total complexity of merging is
    
    $$
    O\left(\sum_{i=2}^\ell\left( 1+\log\dfrac{w(T'_i)}{w(T'_{i-1})}\right) \right) \subseteq O(\ell+\log w(T'_\ell)) \subseteq O(\log n).
    $$
    
    This also shows that the total complexity of the split algorithm is $O(\log n)$.

## Reference implementation

This article has introduced how to perform the basic operations of a balanced tree using a WBLT. Below is the [ordinary balanced tree template](https://loj.ac/p/104) implemented with a WBLT.

??? example "Reference code"
    ```cpp
    --8<-- "docs/ds/code/wblt/wblt-1.cpp:full-text"
    ```

Using merging and splitting, the artistic balanced tree can also be implemented. Below is the [artistic balanced tree template](https://loj.ac/p/105) implemented with a WBLT; the lazy tags must be pushed down when accessing nodes downward.

??? example "Reference code"
    ```cpp
    --8<-- "docs/ds/code/wblt/wblt-2.cpp:full-text"
    ```

Note that a WBLT requires twice the space; when splitting and merging are involved, pay attention to garbage collection and recycle useless nodes in time, otherwise the space is not linear.

## References and notes

-   [Weight-balanced tree - Wikipedia](https://en.wikipedia.org/wiki/Weight-balanced_tree)
-   Nievergelt, J.; Reingold, E. M. (1973). "Binary Search Trees of Bounded Balance". SIAM Journal on Computing. 2: 33–43.
-   Blum, Norbert; Mehlhorn, Kurt (1980). "On the average number of rebalancing operations in weight-balanced trees". Theoretical Computer Science. 11 (3): 303–320.
-   Hirai, Y.; Yamamoto, K. (2011). "Balancing weight-balanced trees". Journal of Functional Programming. 21 (3): 287.
-   Blelloch, Guy E.; Ferizovic, Daniel; Sun, Yihan (2016), "Just Join for Parallel Ordered Sets", Symposium on Parallel Algorithms and Architectures, Proc. of 28th ACM Symp. Parallel Algorithms and Architectures (SPAA 2016), ACM, pp. 253–264.
-   Straka, Milan. (2011). "Adams’Trees Revisited: Correctness Proof and Efficient Implementation." International Symposium on Trends in Functional Programming. Berlin, Heidelberg: Springer Berlin Heidelberg.

[^wrong-range]: The parameter range $\alpha < 1-\dfrac{\sqrt{2}}{2},~\beta=\dfrac{1-2\alpha}{1-\alpha}$ given in the original paper by Nievergelt and Reingold is wrong. The paper by Hirai and Yamamoto provides corresponding counterexamples; the problem mainly arises on some very small trees, which causes the whole inductive proof to fail. Of course, in actual programming contests it is hard to construct data that break these wrong parameters, so in practice this may not have much impact.

[^merge-complexity-cmp]: Since a single balancing operation amounts to at most two subtree joins, and when the two subtrees are already balanced at the end, the subtree joining algorithm must be called once more, if we count the number of calls to the subtree joining algorithm, the constants of the merge operation based on balancing and of the balancing operation based on direct merging below are the same.

[^more-join]: From the proof later on, one can see that in the third case, $z$ and $w+y$ are always balanced, and in the fourth case, $z$ and $u$ are always balanced. They can all be joined directly, without merging.
