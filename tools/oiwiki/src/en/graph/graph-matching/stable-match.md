---
title: Stable matching
---

## Introduction

The **stable matching problem** is a classical problem in combinatorial optimization and cooperative game theory. Compared with traditional graph matching problems, stable matching introduces individual preferences and a stability requirement, which makes algorithm design rely more on preference orders than on the graph structure alone. In the model of the stable matching problem, every individual has preferences over potential partners, and the goal is to establish a stable matching among them. In a stable matching there is no group of individuals that would collude and deviate from the current matching because they could obtain a better choice. Stable matching and related problems are widely applied in labor markets, school admissions, allocation of medical resources, and so on.

The stable matching problem that appears most often in competitive programming is one-to-one matching in a two-sided market, i.e. the stable marriage problem. This article focuses on the stable marriage problem and its algorithms.

## Stable marriage problem

The stable marriage problem is the earliest studied stable matching problem. Similarly to bipartite matching, it can be described as a matching problem in the marriage market: suppose there are some men and women, every person has a preference order over the opposite sex, and the goal is to find a matching such that no man and woman would rather abandon their respective partners and choose each other.

### Problem statement

The matching market consists of a set of men $M$ and a set of women $W$. Every person has a strict preference order over the opposite sex:

-   for every man $m\in M$ there is a strict total order $\preceq_m$ on the set $W\cup\{m\}$;
-   for every woman $w\in W$ there is a strict total order $\preceq_w$ on the set $M\cup\{w\}$.

Besides comparing members of the opposite sex with each other, every person also includes themselves in this preference order. This means a person only accepts members of the opposite sex they prefer to being single; these are called **acceptable**. Clearly the preference order among unacceptable partners is irrelevant; in principle it suffices to give the preference order among acceptable partners only. Hence preferences in which unacceptable partners exist are also called preferences with incomplete lists.

???+ example "Example"
    Suppose $m$ is a man, $w_1,w_2,w_3$ are three women, and the preference relation $w_1\prec_m m \prec_m w_2\prec_m w_3$ holds. Then man $m$ prefers being single to being matched with woman $w_1$; prefers being matched with woman $w_2$ to being single; and prefers being matched with woman $w_3$ to being matched with woman $w_2$. For man $m$, woman $w_1$ is unacceptable, and women $w_2,w_3$ are acceptable.

A **matching** $\mu:M\cup W\rightarrow M\cup W$ in the market must satisfy the following properties:

-   Every person is matched only to a member of the opposite sex or to themselves, i.e. for all $m\in M$ we have $\mu(m)\in W\cup\{m\}$ and for all $w\in W$ we have $\mu(w)\in M\cup\{w\}$.
-   Matching is mutual, i.e. for all $i\in M\cup W$ we have $i = \mu(\mu(i))$.

A matching $\mu$ may have two kinds of instability:

-   If there is an individual $i\in M\cup W$ such that $\mu(i)\prec_i i$, that is, individual $i$ would rather be single than with their current partner, then $i$ is called a **blocking individual** of the matching $\mu$.
-   If there is a pair $m\in M$ and $w\in W$ such that $\mu(m)\prec_m w$ and $\mu(w)\prec_w m$, that is, man $m$ and woman $w$ would rather be with each other than with their current partners, then $(m,w)$ is called a **blocking pair** of the matching $\mu$.

If a matching $\mu$ has neither blocking individuals nor blocking pairs, the matching $\mu$ is called **stable**. In a stable matching nobody can break the current situation: single people cannot find anyone willing to be with them; married people neither want to divorce and be single nor can find anyone willing to elope with them.

The stable matching problem asks: for any given set of preference orders, does a stable matching always exist? If so, how can such a stable matching be found?

### Gale–Shapley algorithm

In 1962 Gale and Shapley proposed the **deferred acceptance algorithm**, which finds a stable matching for any given set of preference orders. Hence a stable matching always exists.

The Gale–Shapley algorithm has two symmetric versions, in which the men propose and the women propose, respectively. Taking the men-proposing Gale–Shapley algorithm as an example, the procedure is as follows:

1.  At the start of the algorithm, every woman is considered to hold a proposal from herself, and every man is marked active.
2.  An active man proposes to the woman he likes most among the acceptable women he has not yet proposed to; if no such woman exists, nothing needs to be done. Whether or not he proposed, all men are marked inactive.
3.  A woman who received new proposals compares them with the proposal she held before, keeps only the one she likes most (possibly herself), and rejects all other proposals. The rejected men are marked active again.
4.  Repeat the previous two steps until there are no active men. At that point the women accept the proposals they currently hold. The resulting matching is a stable matching.

Since every man proposes to every woman at most once, the algorithm is guaranteed to finish in $O(|M||W|)$ time.

A reference implementation follows:

??? example "Template problem [SPOJ STABLEMP - Stable Marriage Problem](https://www.spoj.com/problems/STABLEMP/) reference implementation"
    ```cpp
    --8<-- "docs/graph/code/graph-matching/stable-match/stable-match.cpp"
    ```

### Properties of stable matchings

Stable matchings have nice theoretical properties. First, the Gale–Shapley algorithm constructively proves that a stable matching always exists.

???+ note "Theorem 1 (Gale and Shapley, 1962)"
    The Gale–Shapley algorithm produces a stable matching. Hence a stable matching exists.

??? note "Proof"
    A man never proposes to a woman he does not accept, and a woman immediately rejects a proposal from a man she does not accept. Hence the men and women who end up matched to each other must be mutually acceptable, and there can be no blocking individual. To prove that the matching is stable, it suffices to show that there is no blocking pair.
    
    By contradiction. Suppose $(m,w)$ is a blocking pair. Then, since $\mu(m)\prec_m w$, man $m$ must have already proposed to $w$. But since woman $w$ rejected $m$, she must have received a proposal from a man $m'$ she likes more. If $m'\neq \mu(w)$, then woman $w$ can only like $\mu(w)$ more than $m'$. Hence, compared with $m$, woman $w$ must like her final partner $\mu(w)$ more. This contradicts $(m,w)$ being a blocking pair. So the matching is stable.

???+ note "Corollary"
    If $|M|=|W|$ and all members of the opposite sex are acceptable, then there is a stable perfect matching.

In the Gale–Shapley algorithm, either the men or the women may propose. In general, the stable matchings produced by the two versions of the Gale–Shapley algorithm are different. In fact, the stable matching produced by the men-proposing Gale–Shapley algorithm is the most favorable one for the men among all stable matchings, and vice versa.

???+ note "Theorem 2 (Gale and Shapley, 1962)"
    Let $\mu_M$ and $\mu_W$ be the stable matchings produced by the men-proposing and the women-proposing Gale–Shapley algorithm, respectively. For any stable matching $\mu$, we have $\mu(m)\preceq_m\mu_M(m)$ for all $m\in M$, and $\mu(w)\preceq_w\mu_W(w)$ for all $w\in W$.

??? note "Proof"
    By symmetry, it suffices to prove that $\mu(m)\preceq_m\mu_M(m)$ holds for all $m\in M$. To this end, consider again the men-proposing Gale–Shapley algorithm, and let $k(m,w)$ denote the round of the algorithm in which woman $w$ rejects the proposal of man $m$. This round is well defined for all $(m,w)$ satisfying $\mu_M(m)\prec_m w$.
    
    Suppose $\mu_M$ is not the most favorable for all men, that is, there is a stable matching $\mu$ and a man $m\in M$ such that $\mu_M(m)\prec_m\mu(m)$. Since the matching $\mu_M$ is stable, we have $m\preceq_m\mu_M(m)\prec_m\mu(m)$, so $\mu(m)$ is a woman and $k(m,\mu(m))$ must be well defined. Without loss of generality, let $m$ be the one among all such men for which $k(m,\mu(m))$ is smallest. Suppose that during the algorithm, when woman $w=\mu(m)$ rejected man $m$, she was holding the proposal of man $m'$, that is, $m=\mu(w)\prec_w m'$. Since $\mu$ is a stable matching, $(m',w)$ cannot be a blocking pair, and $\mu(m')\neq w$, so $w\prec_{m'}\mu(m')$. Since during the Gale–Shapley algorithm woman $w$ does not necessarily keep the proposal of $m'$ until the end, we have $\mu_M(m')\preceq_{m'}w\prec_{m'}\mu(m')$. Then $k(m',\mu(m'))$ is well defined. Moreover, since $w\prec_{m'}\mu(m')$, woman $w$ holds the proposal of $m'$ only after woman $\mu(m')$ has rejected the proposal of $m'$, that is, $k(m',\mu(m')) < k(m,\mu(m))$. This contradicts the choice of $m$. Hence, by contradiction, $\mu_M$ is the stable matching most favorable for all men.

A matching market may have an exponential number of stable matchings. Let $\mathcal S$ be the set of all stable matchings. On this set two partial orders can be defined:

-   $\mu_1\preceq_M\mu_2$ if and only if $\mu_1(m)\preceq_m\mu_2(m)$ holds for all $m\in M$;
-   $\mu_1\preceq_W\mu_2$ if and only if $\mu_1(w)\preceq_w\mu_2(w)$ holds for all $w\in W$.

These two partial orders express that the matching outcome is better for all men and for all women, respectively. In general, two stable matchings need not be comparable. However, any two stable matchings induce the decomposition shown in the figure, such that in the three resulting parts $\mu_1\preceq_M\mu_2$, $\mu_1=\mu_2$ and $\mu_2\preceq_M\mu_1$ hold, respectively. Note that, although not drawn explicitly, the part with $\mu_1=\mu_2$ actually includes the case of being matched to oneself (i.e. unmatched).

![](./images/stable-match-decompose.svg)

This decomposition relies on the following lemma:

???+ note "Lemma (Knuth, 1976)"
    Let $\mu_1$ and $\mu_2$ be two stable matchings. Let $M(\mu_i)=\{m\in M : \mu_j(m)\prec_m\mu_i(m)\}$ and $W(\mu_i)=\{w\in W:\mu_j(w)\prec_w\mu_i(w)\}$ be the sets of men and women, respectively, who prefer their outcome in $\mu_i$, where $i,j=1,2$ and $i\neq j$. Then $\mu_1$ and $\mu_2$ are both bijections between $M(\mu_1)$ and $W(\mu_2)$, and both bijections between $M(\mu_2)$ and $W(\mu_1)$.

??? note "Proof"
    Let $m\in M(\mu_1)$. Since $m\preceq_m \mu_2(m)\prec_m\mu_1(m)$, we have $\mu_1(m)\in W$. Let $w=\mu_1(m)$. Since $\mu_2(w)\neq m$, and $\mu_2(w)\prec_w m$ would mean $(m,w)$ is a blocking pair of $\mu_2$, we have $\mu_1(w)=m\prec_w\mu_2(w)$. That is, $w\in W(\mu_2)$. This shows $\mu_1(M(\mu_1))\subseteq W(\mu_2)$. By symmetry, we can also establish $\mu_2(W(\mu_2))\subseteq M(\mu_1)$. Since $\mu_1$ and $\mu_2$ are both injective, $|M(\mu_1)|=|W(\mu_2)|$ and both maps are surjective. This shows that $\mu_1$ and $\mu_2$ are both bijections between $M(\mu_1)$ and $W(\mu_2)$. Similarly, they are both bijections between $M(\mu_2)$ and $W(\mu_1)$.

This lemma shows that the posets $(\mathcal S,\preceq_M)$ and $(\mathcal S,\preceq_W)$ are [dual](../../math/order-theory.md#对偶) to each other. Moreover, under each partial order the set $\mathcal S$ forms a [lattice](../../math/order-theory.md#有向集与格). Since $\mathcal S$ is finite, both lattices must have a greatest and a least element. These two extreme elements are exactly the stable matchings produced by the two versions of the Gale–Shapley algorithm mentioned above.

???+ note "Theorem 3 (Conway and Knuth, 1976)"
    The posets $(\mathcal S,\preceq_M)$ and $(\mathcal S,\preceq_W)$ are mutually dual lattices. Moreover, $\mu_M$ and $\mu_W$ are the greatest and least elements of $(\mathcal S,\preceq_M)$, respectively, and the least and greatest elements of $(\mathcal S,\preceq_W)$, respectively.

??? note "Proof"
    By the lemma, it is easy to show that the two posets are dual. If $\mu_1\preceq_M\mu_2$, this means $M(\mu_1)=\varnothing$; by the lemma, $W(\mu_2)=\varnothing$, which is exactly $\mu_2\preceq_W\mu_1$. And vice versa. This shows the two are dual to each other. Combined with Theorem 2 above, we get that $\mu_M$ and $\mu_W$ are the extreme elements of the two posets. What remains to be proved is that the two posets are lattices. By symmetry, it suffices to prove that $(\mathcal S,\preceq_M)$ is a lattice. By the symmetry of the meet and join operations, it suffices to prove that the join of two stable matchings is again a stable matching. Formally, for any $\mu_1,\mu_2\in\mathcal S$, we need to prove that the matching $\mu=\mu_1\lor_M\mu_2$ satisfying $\mu(m)=\mu_1(m)\lor_m\mu_2(m)$ for all $m\in M$ is a stable matching, where $\lor_m$ is the join operation under the total order $\preceq_m$ (i.e. the one of the two that $m$ likes more).
    
    We keep the notation of the lemma. For $i\in M(\mu_1)\cup W(\mu_2)$, let $\mu(i)=\mu_1(i)$; otherwise, let $\mu(i)=\mu_2(i)$. By the lemma, $\mu_1$ and $\mu_2$ both map the set $M(\mu_1)\cup W(\mu_2)$ onto itself, so $\mu$ is a well-defined matching. Since $\mu_1$ and $\mu_2$ are both stable and have no blocking individuals, neither does $\mu$. Suppose $(m,w)$ is a blocking pair of $\mu$. If $m\in M(\mu_1)$, then $\mu_2(m)\prec_m\mu_1(m)=\mu(m)\prec_m w$. In this case, if $w\in W(\mu_2)$, then $\mu_1(w)=\mu(w)\prec_w m$, so $(m,w)$ is a blocking pair of $\mu_1$, a contradiction; otherwise $w\in W\setminus W(\mu_2)$, and $\mu_2(w)=\mu(w)\prec_w m$, so $(m,w)$ is a blocking pair of $\mu_2$, also a contradiction. Similarly, the case $m\in M\setminus M(\mu_1)$ can only lead to a contradiction. By contradiction, no such blocking pair exists. Hence $\mu_1\lor_M\mu_2$ is a stable matching. This proves the proposition.

Finally, in all stable matchings the sets of unmatched men and women are fixed.

???+ note "Theorem 4 (McVitie and Wilson, 1970)"
    Let $\mu_1$ and $\mu_2$ be two stable matchings. Then $\mu_1$ and $\mu_2$ have the same set of fixed points.

??? note "Proof"
    Suppose there is $m\in M$ such that $\mu_1(m)=m$ and $\mu_2(m)\neq m$ for some $\mu_1,\mu_2\in\mathcal S$. Then $m\in M(\mu_2)$. By the lemma, $m=\mu_1(m)\in W(\mu_1)$, contradicting $m\in M$. Hence no such $m\in M$ exists. Similarly, no such $w\in W$ exists. Therefore any two stable matchings must have the same set of fixed points.

Besides the properties discussed in this section, stable matchings also have some nice strategic properties. For these, see the references at the end of the article.

## Related problems

Stable matching and similar problems also appear in many other settings.

### College admissions problem

If the one-to-one restriction in the stable marriage problem is relaxed to allow many-to-one matching, we get the **college admissions problem**. Here a college may admit several students as long as its admission quota is not exceeded; a student, however, may still enter at most one college. Similar situations appear in company hiring, hospitals recruiting medical interns, and so on.

For this kind of problem the Gale–Shapley algorithm still applies. For example, in the student-proposing Gale–Shapley algorithm, a college may maintain a waitlist of length not exceeding its quota, and whenever the number of applications exceeds the quota, it simply rejects the worst student's application. The earlier discussion of the properties of stable matchings still applies to this setting. In particular, the version of Theorem 4 here states that in all stable matchings the number of students a college can admit is fixed. This is also called the **rural hospitals theorem**, because it means that no matter how the matching mechanism is changed, as long as the result is stable, rural hospitals that cannot fill their positions for doctors will never fill them.

### Stable roommates problem

If the condition in the stable marriage problem that only members of the opposite sex can be matched is relaxed, we get the **stable roommates problem**. Here, initially there are only some students who need to be paired up as roommates. For this kind of problem a stable matching need not exist. In 1985 Irving proposed an algorithm that solves this problem in $O(n^2)$ time.

### Housing market problem

In the stable marriage problem two groups of individuals have preferences over each other, so it is a two-sided matching problem. Besides this, one-sided matching problems can also be considered. A common setting is the **housing market problem**. There are $n$ residents, each owning a house. Every person has a strict preference over all houses. Now the houses are to be reallocated to the residents such that no resident is allocated a house worse than their initial one, and no group of residents of any size can privately exchange their properties to obtain a more satisfactory outcome. This problem can be solved by the Top Trading Cycle algorithm in $O(n^2)$ time. This kind of problem also appears in settings such as kidney transplantation.

## Exercises

-   [UOJ 41.【清华集训 2014】矩阵变换](https://uoj.ac/problem/41)
-   [Codeforces 1147 F. Zigzag Game](https://codeforces.com/problemset/problem/1147/F)

## References and notes

-   [什么是算法：如何寻找稳定的婚姻搭配 (What is an algorithm: how to find stable marriage pairings) - Matrix67](https://matrix67.com/blog/archives/2976)
-   [Gale–Shapley 算法：在二分图中寻找稳定匹配 (Gale–Shapley algorithm: finding a stable matching in a bipartite graph)](https://reimuyk.github.io/2021-03-24-Gale-Shapley-Algorithm/)
-   [Stable matching problem - Wikipedia](https://en.wikipedia.org/wiki/Stable_matching_problem)
-   [Lattice of stable matchings - Wikipedia](https://en.wikipedia.org/wiki/Lattice_of_stable_matchings)
-   [Stable roommates problem - Wikipedia](https://en.wikipedia.org/wiki/Stable_roommates_problem)
-   [Top trading cycle - Wikipedia](https://en.wikipedia.org/wiki/Top_trading_cycle)
-   [Stable matching: Theory, evidence, and practical design - the 2012 Nobel Prize in Economics](https://www.nobelprize.org/uploads/2018/06/popular-economicsciences2012.pdf)
-   [Notes on Matching and Market Design by Xiang Sun](https://www.xiangsun.org/wp-content/uploads/2013/02/notes-2015-matching.pdf)
-   Gale, David, and Lloyd S. Shapley. "College admissions and the stability of marriage." The American Mathematical Monthly 69, no. 1 (1962): 9-15.
-   Irving, Robert W. "An efficient algorithm for the stable roommates problem." Journal of Algorithms 6, no. 4 (1985): 577-595.
-   Knuth, Donald Ervin. "Mariages stables et leurs relations avec d'autres problèmes combinatoires." Les Presses de l'Université de Montréal (1976).
-   McVitie, David G., and Leslie B. Wilson. "Stable marriage assignment for unequal sets." BIT Numerical Mathematics 10, no. 3 (1970): 295-309.
-   Roth, Alvin E., and Marilda Sotomayor. "Two-sided matching." Handbook of game theory with economic applications 1 (1992): 485-541.
-   Roth, Alvin E. "Deferred acceptance algorithms: History, theory, practice, and open questions." International Journal of Game Theory 36, no. 3-4 (2008): 537-569.
