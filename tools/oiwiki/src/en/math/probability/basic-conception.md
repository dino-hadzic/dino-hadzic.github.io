---
title: Basic concepts
---

## Introduction

When studying a concrete random phenomenon, we usually focus on the following elements:

-   the sample space $\Omega$, which specifies all possible outcomes of the random phenomenon;
-   the event space $\mathcal{F}$, which represents all the events we are interested in;
-   the probability $P$, which describes how likely each event is to occur.

## Sample space, random events

### Definition

An outcome of a random phenomenon that cannot be subdivided further is called a **sample point**. The set of all sample points is called the **sample space**, usually denoted by $\Omega$.

A **random event** is a subset of the sample space $\Omega$; it consists of some sample points and is denoted by capital letters $A, B, C, \cdots$.

For an outcome $\omega$ of a random phenomenon and a random event $A$, we say that the event $A$ **occurred** if and only if $\omega \in A$.

For example, the number obtained by rolling a die once is a random phenomenon, and its sample space can be written as $\Omega=\{1,2,3,4,5,6\}$. Let the random event $A$ be "the number obtained is greater than $4$"; then $A = \{ 5, 6 \}$. If some roll of the die gives the number $\omega = 3$, then since $\omega \notin A$, the event $A$ did not occur.

### Operations on events

Since we defined random events as subsets of the sample space $\Omega$, we can transfer the operations on sets (such as intersection, union, complement, etc.) to random events. The notation is the same as for set operations.

In particular, the union of events $A \cup B$ can also be written as $A + B$, and the intersection of events $A \cap B$ can also be written as $AB$; they are then also called the **sum event** and the **product event**, respectively.

## Event space

When studying a concrete random phenomenon, we need to specify which events we are interested in. By the definition of a random event, clearly $\mathcal{F} \subset 2^{\Omega}$ (the notation $2^{\Omega}$ denotes the power set of $\Omega$), but $\mathcal{F} = 2^{\Omega}$ is not required. This may be somewhat hard to understand when the sample space $\Omega$ is finite, since $2^{\Omega}$, although larger, is still finite. But when $\Omega$ is an infinite set, the cardinality of $2^{\Omega}$ becomes even larger, and it inevitably contains some events with "not so nice properties" that we do not care about; in that case, giving up some properties just to accommodate these events is not worth it.

Although $\mathcal{F} = 2^{\Omega}$ is not required, this does not mean that any subset of $2^{\Omega}$ can be an event space. We are usually interested in the probabilities of the events obtained by performing operations on some events, so we want the event space $\mathcal{F}$ to satisfy the following conditions:

-   $\varnothing \in \mathcal{F}$;
-   if $A \in \mathcal{F}$, then the complementary event $\bar{A} \in \mathcal{F}$;
-   if there is a sequence of events $A_n \in \mathcal{F}, n = 1, 2, 3\dots$, then $\bigcup A_n \in \mathcal{F}$.

In short, the event space $\mathcal{F}$ is closed under complement and countable union, and contains the element $\varnothing$.

It can be proved that an event space $\mathcal{F}$ satisfying the above three conditions is also closed under countable intersection.

Taking the die roll as an example, when the sample space is written as $\Omega=\{1,2,3,4,5,6\}$, the following two sets can be event spaces:

-   $\mathcal{F}_1 = \{ \varnothing, \Omega \}$
-   $\mathcal{F}_2 = \{ \varnothing, \{1, 3, 5\}, \{2, 4, 6\}, \Omega \}$

but the following two sets cannot:

-   $\mathcal{F}_3 = \{ \varnothing, \{1\}, \Omega \}$ (not closed under complement)
-   $\mathcal{F}_4 = \{ \{1, 3, 5\}, \{2, 4, 6\} \}$ (does not contain $\varnothing$ and is not closed under union)

## Probability

### Definition

#### Classical definition

In the early practice of probability theory, the random phenomena involved were rather simple: concretely, the sample space $\Omega$ was a finite set, and intuitively all sample points were equally likely to occur. Therefore, people arrived at the following definition:

If a random phenomenon satisfies:

-   there are only finitely many basic outcomes;
-   every basic outcome is equally likely;

then for every event $A$, its probability is defined as

$$
P(A)=\frac{\#(A)}{\#(\Omega)}
$$

where $\#(\cdot)$ denotes a measure of the size of a random event (a set).

Later it was found that this definition can be directly generalized to some situations where $\Omega$ is infinite, which gave rise to the so-called [geometric probability](https://en.wikipedia.org/wiki/Geometric_probability).

#### Axiomatic definition

The above definition based on intuition has a big logical loophole: when defining the concept of "probability", it uses the notion of "likelihood", which leads to the problem of circular definition. Moreover, "equally likely" becomes ambiguous when the sample space is infinite, which gives rise to a series of problems including the [Bertrand paradox](https://en.wikipedia.org/wiki/Bertrand_paradox_(probability)).

After continued exploration, the Soviet mathematician Kolmogorov gave the axiomatic definition of probability for the first time in 1933 in his book "Foundations of the Theory of Probability":

A probability function $P$ is a map from the event space $\mathcal{F}$ to the closed interval $[0, 1]$ satisfying:

-   **normalization**: the probability of the event $\Omega$ is $1$, i.e. $P(\Omega)=1$;
-   **countable additivity**: if the events in a sequence $A_1, A_2, \cdots$ are pairwise disjoint, then $P\left( \bigcup_{i \geq 1} A_i \right) = \sum_{i \geq 1} P(A_i)$.

### Properties of the probability function

For any random events $A, B \in \mathcal{F}$, we have:

-   **monotonicity**: if $A \subset B$, then $P(A) \leq P(B)$;
-   **inclusion–exclusion principle**: $P(A+B) = P(A) + P(B) - P(AB)$;
-   $P(A - B) = P(A) - P(AB)$, where $A - B$ denotes the set difference.

## Probability space

We mentioned at the beginning that when studying a concrete random phenomenon, we usually focus on the sample space $\Omega$, the event space $\mathcal{F}$ and the probability function $P$. We call the triple $(\Omega, \mathcal{F}, P)$ a probability space.

Probability is meaningful only when discussed within a definite probability space. The Bertrand paradox mentioned earlier ultimately arises from an unclear definition of the sample space $\Omega$.

## References and notes

-   [概率论（数学分支）\_百度百科 (Probability theory (branch of mathematics) – Baidu Baike)](https://baike.baidu.com/item/概率论/829122)
-   [Probability - Wikipedia](https://en.wikipedia.org/wiki/Probability)
