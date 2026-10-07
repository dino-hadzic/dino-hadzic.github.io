---
title: Alpha–beta pruning
---

This page briefly introduces the Minimax algorithm and alpha–beta pruning.

## Minimax algorithm

The Minimax algorithm, also called the minimizing-maximum algorithm, is an algorithm that minimizes the potential loss in the worst (i.e., maximum-loss) scenario.

### Procedure

In two-player zero-sum games with fully determined positions, adversarial search is often required: a search tree is built in which every node is a determined state. On odd levels it is our turn to move, and on even levels it is the opponent's turn. Every leaf of the search tree is assigned an evaluation; the larger the evaluation, the better our chances of winning. We pursue better chances, while the opponent tries to reduce our chances; in the search tree this means that nodes on odd levels (our nodes) always choose the child state with the best chances, while nodes on even levels (the opponent's nodes) always choose the child state with the worst chances (for us).

The Minimax algorithm traverses the search tree from top to bottom, uses the information from subtrees to update the answer while backtracking, and finally obtains the value of the root — this is the maximum score we can achieve when both sides play optimally.

### Example

Let us look at a simple example.

Call us MAX and the opponent MIN; the picture is as follows:

![](images/minimax-1.svg)

For example, in the following situation, assume we search from left to right and the value at the root is our chance of winning:

![](images/minimax-2.svg)

We should choose the middle route. If we choose the left route, the worst chance is $3$; if we choose the middle route, the worst chance is $15$; if we choose the right route, the worst chance is $1$. Although the right route may offer a chance of $22$, a sufficiently rational opponent will leave us with a chance of only $1$. After weighing the options, the middle route is clearly better.

![](images/minimax-3.svg)

In fact, when looking at the right route, once we find that the chance may be $1$, we no longer need to look at the branches with chances $12$, $20$, and $22$. Compared with the chances of the two routes on the left, we can already be sure that the right route is not the best.

The naive Minimax algorithm often has to build a huge search tree, making the time and space complexity unbearable. Alpha–beta pruning is a method that optimizes Minimax by pruning with the lower and upper bounds of both sides' scores at every node of the search tree.

Note that in different problems, the values at the nodes of the search tree have different meanings: they can be evaluations, scores, winning probabilities, and so on. For convenience, below we uniformly call them scores.

## Alpha–beta pruning

Alpha–beta pruning is search pruning for the Minimax algorithm.

### Procedure

In the Minimax algorithm, if the scores of all children of a node are known, the score of that node can be computed: for a MAX node take the maximum score, and for a MIN node take the minimum score.

When the search reaches a node but has not yet finished it, we cannot compute the score of that node, but we can compute the range of both sides' scores **among the nodes searched so far**. During the search we maintain two variables, $\alpha$ and $\beta$, which denote the lower and upper bounds of the scores that, when the game reaches this node and **considering all nodes searched so far**, the Alpha player (the side seeking the maximum score) and the Beta player (the side seeking the minimum score) can guarantee, respectively.

The pruning strategy of alpha–beta pruning depends on the values of $\alpha$ and $\beta$ when searching the current node. If the current node is a MAX node, the Alpha player can continue searching its children to raise the lower bound $\alpha$ of the score. However, if after some search we already have $\alpha\ge\beta$, continuing to search this node will not affect the result of the game: once this node is reached, the Alpha player can guarantee a score of at least $\alpha$; but the Beta player already knows a strategy (deviating from the current path) that guarantees a score of at most $\beta\le\alpha$, so the Beta player has no reason to let the game reach the **current node**. Similarly, if the current node is a MIN node and, after searching one of its children, we already find that $\beta\le\alpha$ holds at this node, then there is likewise no need to search the other children, because the Alpha player has no reason to let the game enter the **current node**. Summarizing both cases: when $\alpha \geq \beta$, the remaining branches of this node need not be searched (that is, pruning can be performed). Note that pruning is also possible when $\alpha = \beta$, because the opponent already has an alternative that guarantees a score no worse for them than $\alpha$ (i.e., $\beta$), and continuing to search the remaining branches will not change the result at the nodes above.

During the search, there is no need to maintain node scores; it suffices to maintain $\alpha$ and $\beta$. Initially, let $\alpha=-\infty,~\beta=+\infty$. When searching downward, the information in $\alpha$ and $\beta$ is passed down as well, to record the alternatives of both players.

After a child has been searched, the information at the current node must be updated. Suppose the current node $X$ is a MAX node and we have just finished searching its child $Y$. Then the $\beta$ value at node $X$ does not change; only the $\alpha$ value needs to be updated with the maximum of itself and the score of child $Y$. If child $Y$ is a leaf, directly update the $\alpha$ value at the current node $X$ with the score of child $Y$; otherwise, it suffices to update the $\alpha$ value of the current node $X$ with the $\beta$ value of child $Y$. There are three possibilities:

1.  The $\beta$ value of child $Y$ lies strictly between the $\alpha$ and $\beta$ values of node $X$. Since child $Y$ inherited the $\alpha$ value of node $X$ and does not update it, after searching child $Y$ we still have $\beta > \alpha$, which means that no pruning occurred while searching child $Y$. The final $\beta$ value of child $Y$ equals the minimum of the $\beta$ value inherited from node $X$ and the scores of all children of $Y$. Since this minimum is strictly smaller than the $\beta$ value of node $X$, it must be the minimum score among all children of child $Y$. Therefore, as a MIN node, the score of child $Y$ is exactly this $\beta$ value. Using it to update the $\alpha$ value of node $X$ is justified.
2.  The $\beta$ value of child $Y$ equals the $\beta$ value of node $X$. As described above, this means that the scores of all children of child $Y$ are no smaller than the $\beta$ value of node $X$. This further means that the Beta player has no reason to let the game enter node $X$: as soon as the Alpha player chooses child $Y$, the Beta player cannot obtain a score lower than $\beta$. Therefore, updating the $\alpha$ value of node $X$ with the $\beta$ value of child $Y$ in this case serves to make $\alpha=\beta$ at node $X$, triggering the pruning condition. Its effect is the same as updating the $\alpha$ value of node $X$ with the actual score at $Y$ — a number greater than or equal to the $\beta$ value at node $X$.
3.  The $\beta$ value of child $Y$ is less than or equal to the $\alpha$ value of node $X$. In this case child $Y$ triggered the pruning condition; its actual score does not exceed the $\beta$ value of child $Y$, let alone the $\alpha$ value of node $X$. Updating the $\alpha$ value of node $X$ with the actual score of child $Y$ does not change the $\alpha$ value. This has the same effect as updating the $\alpha$ value of node $X$ with the $\beta$ value of child $Y$.

This analysis shows that after the search of some child is complete, only in the first case does $\alpha$ (or $\beta$) accurately record the actual score of that child as a MAX node (or MIN node). In the other cases, although it is not necessarily the accurate score, the information it provides is sufficient to guarantee that pruning is performed correctly, and thus does not affect the score recorded at the root.

### Example

This section analyzes an example to show how the $\alpha$ and $\beta$ values at each node are updated during the search. Along the way, the scores of the nodes involved are computed as well. This lets us observe the relationship between the actual score at each node and the recorded $\alpha$ and $\beta$ values. Note, however, that when implementing this algorithm, the actual scores of these nodes are not computed.

For the following situation, assume we search from left to right:

![](images/alpha-beta-1.svg)

At initialization, let $\alpha = -\infty,~\beta = +\infty$, and pass this information down along the search path.

![](images/alpha-beta-2.svg)

When the search reaches node A, since the score of the left child is $3$ and node A is a MIN node trying to find a move with a smaller score, the $\beta$ value is changed to $3$, because $3$ is less than the current $\beta$ value ($\beta = +\infty$). Then the score of the right child of node A is $17$; the $\beta$ value of node A is not changed now, because $17$ is greater than the current $\beta$ value ($\beta = 3$). Now all children of node A have been searched, so the score of node A can be computed as $3$, which agrees with the $\beta$ value recorded at this node (case 1 above).

![](images/alpha-beta-3.svg)

Node A is a child of node B; after computing the score of node A, the $\alpha$ and $\beta$ values of node B can be updated. Since node B is a MAX node trying to find a move with a larger score, the $\alpha$ value is changed to $3$, because the $\beta$ value at child A ($\beta=3$) is greater than the current $\alpha$ value ($\alpha = -\infty$). Then the right child C of node B is searched, and the $\alpha$ and $\beta$ values of node B are passed to node C.

![](images/alpha-beta-4.svg)

For node C, since the score of the left child is $2$ and node C is a MIN node, the $\beta$ value is changed to $2$. Now $\alpha \geq \beta$, so the remaining children of node C need not be searched, because we can be sure that the Alpha player will not allow the game to reach node C. Node C is a MIN node, and its score is $2$, not exceeding the recorded $\beta$ value (case 3 above). Since all children of node B have been searched, the score of node B can be computed as $3$, the same as the recorded $\alpha$ value (case 1 above).

![](images/alpha-beta-5.svg)

After computing the score of node B, since node B is a child of node D, the $\alpha$ and $\beta$ values of node D can be updated. Since node D is a MIN node, the $\beta$ value is changed to $3$. Then node D passes the $\alpha$ and $\beta$ values to node E, and node E passes them on to node F. Node F has only one child, with score $15$; since $15$ is greater than the current $\beta$ value and node F is a MIN node, its $\beta$ value is not updated, and then the score of node F can be computed as $15$, greater than the recorded $\beta$ value (case 2 above).

![](images/alpha-beta-6.svg)

After computing the score of node F, since node F is a child of node E, the $\alpha$ and $\beta$ values of node E can be updated. Node E is a MAX node, so the $\alpha$ value is updated; now $\alpha \geq \beta$, so the remaining branches of node E (i.e., node G) can be pruned. Then, since node E is a MAX node, the score of node E is set to $15$, strictly greater than the recorded $\alpha$ value (case 3 above). Using the $\alpha$ value of node E to update the $\beta$ value of node D leaves it at $3$. Now all children of node D have been searched, so the score of node D can be computed as $3$, equal to the recorded $\beta$ value (case 1 above).

![](images/alpha-beta-7.svg)

After computing the score of node D, since node D is a child of node H, the $\alpha$ and $\beta$ values of node H can be updated. Node H is a MAX node, so $\alpha$ is updated. Then, following the search order, the $\alpha$ and $\beta$ values of node H are passed in turn to nodes I, J, K. For node K, the score of its left child is $2$, and node K is a MIN node, so $\beta$ is updated; now $\alpha \geq \beta$, so the remaining branches of node K can be pruned. Then the score of node K is set to $2$, less than or equal to the recorded $\beta$ value (case 3 above).

![](images/alpha-beta-8.svg)

After computing the score of node K, since node K is a child of node J, the $\alpha$ and $\beta$ values of node J can be updated. Node J is a MAX node, so $\alpha$ is updated, but since the score of node K is less than $\alpha$, the $\alpha$ value of node J stays at $3$. Then the $\alpha$ and $\beta$ values of node J are passed to node L. Since node L is a MIN node, $\beta = 3$ is updated; now $\alpha \geq \beta$, so the remaining branches of node L can be pruned. Since node L has no remaining branches, no actual pruning happens here. Then the score of node L is set to $3$, which is less than or equal to the recorded $\beta$ value (case 3 above).

![](images/alpha-beta-9.svg)

After computing the score of node L, since node L is a child of node J, the $\alpha$ and $\beta$ values of node J can be updated. Node J is a MAX node, so $\alpha$ is updated, but since the score of node L is less than or equal to $\alpha$, the $\alpha$ value of node J stays at $3$. Now all children of node J have been searched, so the score of node J can be computed as $3$, which equals the recorded $\alpha$ value (case 2 above).

After computing the score of node J, since node J is a child of node I, the $\alpha$ and $\beta$ values of node I can be updated. Node I is a MIN node, so $\beta$ is updated; now $\alpha \geq \beta$, so the remaining branches of node I can be pruned. It is worth noting that, because of the existence of the right child, the actual score of node I is $2$, less than the recorded $\beta$ value (case 3 above).

After computing the score of node I, since node I is a child of node H, the $\alpha$ and $\beta$ values of node H can be updated. Node H is a MAX node, so $\alpha$ is updated, but since the score of node I is less than or equal to $\alpha$, the $\alpha$ value of node H stays at $3$. Now all children of node H have been searched, so the score of node H can be computed as $3$, which equals the recorded $\alpha$ value (case 1 above).

![](images/alpha-beta-10.svg)

This is the final result.

### Implementation

???+ example "Sample code"
    ```cpp
    int alpha_beta(int u, int alph, int beta, bool is_max) {
      if (!son_num[u]) return val[u];
      if (is_max) {
        for (int i = 0; i < son_num[u]; ++i) {
          int d = son[u][i];
          alph = max(alph, alpha_beta(d, alph, beta, !is_max));
          if (alph >= beta) break;
        }
        return alph;
      } else {
        for (int i = 0; i < son_num[u]; ++i) {
          int d = son[u][i];
          beta = min(beta, alpha_beta(d, alph, beta, !is_max));
          if (alph >= beta) break;
        }
        return beta;
      }
    }
    ```

## References and notes

-   [Minimax Algorithm - Wikipedia](https://en.wikipedia.org/wiki/Minimax#Minimax_algorithm_with_alternate_moves)
-   [Alpha–beta pruning - Wikipedia](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning)

**Parts of this article are taken from the blog post [Minimax Algorithm and α-β Pruning Explained – 文剑木然 (Chinese)](https://blog.csdn.net/wenjianmuran/article/details/90633418), licensed under CC 4.0 BY-SA. The content has been modified.**
