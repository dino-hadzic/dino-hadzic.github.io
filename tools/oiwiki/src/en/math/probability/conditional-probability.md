---
title: Conditional probability and independence
---

## Introduction

When some event has already occurred, the probabilities of some random events change because of the increase in known information. For example, when pulling cards in a mobile gacha game, we might think that getting a six-star card and not getting one in a single pull are equally likely, but after $50$ consecutive pulls without a single six-star card, stubbornly insisting that "getting a six-star and not getting one are equally likely" no longer seems so wise.

In short, it is necessary to study the probability of events under certain known conditions.

## Conditional probability

### Definition

If the event $A$ is known to have occurred, the probability that the event $B$ occurs under this condition is called the **conditional probability**, denoted $P(B|A)$.

In a probability space $(\Omega, \mathcal{F}, P)$, if an event $A \in \mathcal{F}$ satisfies $P(A) > 0$, then the conditional probability $P(\cdot|A)$ is defined as

$$
P(B|A) = \frac{P(AB)}{P(A)} \quad \forall B \in \mathcal{F}
$$

One can verify that $P(\cdot|A)$ defined by the formula above is a probability function on $(\Omega, \mathcal{F})$.

The following two identities follow directly from the definition of conditional probability:

-   **multiplication rule of probability**: in a probability space $(\Omega, \mathcal{F}, P)$, if $P(A) > 0$, then for every event $B$ we have

$$
P(AB) = P(A)P(B|A)
$$

-   **law of total probability**: in a probability space $(\Omega, \mathcal{F}, P)$, if a family of events $A_1, \cdots, A_n$ are pairwise disjoint and their union is $\Omega$, then for every event $B$ we have

$$
P(B) = \sum_{i=1}^{n} P(A_i)P(B|A_i)
$$

### Bayes' theorem

In general, let the possible causes of the event $B$ be $A_1, A_2, \cdots, A_n$; then, when $P(A_i)$ and $P(B|A_i)$ are known, the probability of the event $B$ can be computed by the law of total probability. But in many situations, we need to infer backwards the probabilities of the individual cause events from the result "event $B$ occurred". Thus we have

$$
P(A_i|B) = \frac{P(A_iB)}{P(B)} = \frac{P(A_i)P(B|A_i)}{\sum_{j=1}^{n} P(A_j)P(B|A_j)}
$$

The formula above is Bayes' theorem.

## Independence of events

In the study of conditional probability, the case $P(B|A) = P(B)$ may occur. Intuitively, this means that whether the event $B$ occurs does not tell us anything about the event $A$, i.e. the event $B$ is "unrelated" to the event $A$. This leads to the following definition.

### Definition

If events $A$,$B$ in the same probability space satisfy

$$
P(AB) = P(A)P(B)
$$

then $A$,$B$ are called **independent**. For several events $A_1, A_2, \cdots, A_n$, we call them independent if and only if for every choice of events $\{ A_{i_k} : 1 \leq i_1 < i_2 < \cdots < i_k \leq n \}$ we have

$$
P( A_{i_1}A_{i_2} \cdots A_{i_r} ) = \prod_{k=1}^{r} P(A_{i_k})
$$

### Independence of several events

For several events, in general one cannot deduce that the events are independent from pairwise independence. Consider the following counterexample:

There is a regular tetrahedral die, three of whose faces are painted red, green and blue respectively, while the remaining face has all three colors. Now roll this die once, and let the events $A$,$B$,$C$ denote that the face touching the table contains red, green and blue, respectively.

It is easy to compute $P(A) = P(B) = P(C) = \frac{1}{2}$, while $P(AB) = P(BC) = P(CA) = P(ABC) = \frac{1}{4}$.

Clearly $A, B, C$ are pairwise independent, but since $P(ABC) \neq P(A)P(B)P(C)$, the events $A, B, C$ are not independent.
