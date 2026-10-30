---
title: Boolean algebra
---

In mathematical logic, Boolean algebra is a branch of algebra. In elementary algebra the values of variables are numbers, and the main operations studied are addition, multiplication, exponentiation, and the inverses of these three operations. In Boolean algebra, variables take only two values, **true** and **false** (usually written $1$ and $0$), and the main operations studied are conjunction (and, $\land$), disjunction (or, $\lor$), and negation (not, $\lnot$). Just as elementary algebra is a formalism for describing numerical operations, Boolean algebra is a formalism for describing logical operations.

## Boolean functions

???+ abstract "Definition"
    A **Boolean function** is a function of the form $f:\mathbf{B}^k\to \mathbf{B}$, where $\mathbf{B}=\{0,1\}$ is the **Boolean domain** and the non-negative integer $k$ is the **arity** of the Boolean function. A Boolean function with $k=1$ is a unary function, and so on. When $k=0$, we consider the function to degenerate into a constant in $\mathbf{B}$.

We generally only study unary and binary Boolean functions. Unless otherwise stated, the Boolean functions below are restricted to the unary and binary cases.

Besides the usual way of writing functions, we can also represent Boolean functions with **truth tables**, **logic gates**, and [Venn diagrams](https://en.wikipedia.org/wiki/Venn_diagram).

???+ abstract "Truth table"
    For a Boolean function, we enumerate all cases of its input and list the inputs and the corresponding outputs in a table; this table is called a truth table.

An $n$-ary Boolean function can also be represented by a **propositional formula** with $n$ variables; propositional formulas $p$ and $q$ are **logically equivalent** if and only if they describe the same Boolean function, written $p\iff q$.

Below are some common Boolean functions; we also collectively call these Boolean functions **logical connectives** or **logical operators**:

| Name (mathematical logic)                                           | Other names                 | Notation                               |
| -------------------------------------------------- | -------------------- | -------------------------------- |
| truth, tautology                                |                      | $\top$                           |
| falsity, contradiction                          |                      | $\bot$                           |
| proposition                                                 | identity                   | $A$                              |
| negation                                       | NOT               | $\lnot A$                        |
| conjunction                                    | AND               | $A \land B$                      |
| disjunction                                    | OR                | $A \lor B$                       |
| non-conjunction                               | NAND, Sheffer stroke  | $A \bar{\land} B$, $A\uparrow B$  |
| non-disjunction                               | NOR              | $A \bar{\lor} B$, $A\downarrow B$ |
|                                                    | exclusive OR (XOR) | $A \oplus B$                     |
|                                                    | exclusive NOR (XNOR)    | $A \odot B$                      |
| material implication[^note1]                 |                      | $A \to B$                        |
| material nonimplication[^note1]             |                      | $A \nrightarrow B$               |
| converse implication[^note1]                  |                      | $A \gets B$                      |
| converse nonimplication[^note1]              |                      | $A \nleftarrow B$                |
| biconditional, equivalence[^note1][^note2] |                      | $A \leftrightarrow B$            |
| non-equivalence[^note1][^note3]               |                      | $A \nleftrightarrow B$           |

The corresponding truth tables (from [Wikipedia](https://commons.wikimedia.org/wiki/File:Logical_connectives_table.svg)):

![](./images/logical-connectives-table.svg)

The corresponding Venn diagrams and [Hasse diagram](./order-theory.md#偏序集的可视化表示hasse-图) (with set inclusion $\subseteq$ as the partial order; from [Wikipedia](https://en.wikipedia.org/wiki/File:Logical_connectives_Hasse_diagram.svg)):

![](./images/logical-connectives-hasse-diagram.svg)

Since an $n$-ary Boolean function has $2^n$ possible inputs, there are $2\uparrow (2\uparrow n)$ $n$-ary Boolean functions, where $\uparrow$ is Knuth's up-arrow.

We call a combination of logical operators a **logical expression**.

If we regard $\mathbf{B}$ as the [residue classes](./number-theory/basic.md#同余类与剩余系) modulo $2$, then XOR is equivalent to addition modulo $2$ and AND is equivalent to multiplication modulo $2$, so we sometimes also denote the Boolean domain by $\mathbf{Z}_2$.

### Precedence

Unary logical operators have higher precedence than binary logical operators, i.e. $\lnot$ has higher precedence than $\land$, $\lor$, $\oplus$, etc.

There are several conventions for the precedence among binary logical operators: some sources hold that $\land$, $\lor$, $\oplus$ have higher precedence than $\to$, $\gets$, $\leftrightarrow$, while others hold the opposite view. Therefore it is recommended to add parentheses to make the order explicit.

For the rules in C++, see the [C++ operator precedence table](../lang/op.md#c-运算符优先级总表).

### Sole sufficient operators and functionally complete sets of operators

In fact, we can express all the other logical operators using only NAND or only NOR, and CPUs are built on this fact. However, since the four logical operators **AND, OR, NOT, XOR** have nicer properties, we generally use only these four functions when studying Boolean algebra.

??? example "How to express the other logical operators using NAND and NOR respectively"
    We have
    
    -   $\lnot p=p\bar{\land} p=p\bar{\lor} p$,
    -   $p\land q=(p\bar{\land}q)\bar{\land}(p\bar{\land}q)=(p\bar{\lor}p)\bar{\lor}(q\bar{\lor}q)$,
    -   $p\lor q=(p\bar{\land}p)\bar{\land}(q\bar{\land}q)=(p\bar{\lor}q)\bar{\lor}(p\bar{\lor}q)$,
    -   $p\to q=p\bar{\land} (q\bar{\land} q)=((p\bar{\lor}p)\bar{\lor}q)\bar{\lor}((p\bar{\lor}p)\bar{\lor}q)$.
    
    In addition
    
    -   $p=\lnot\lnot p$,
    -   $p\nleftrightarrow q=p\oplus q=(p\lor q)\land\lnot (p\land q)$,
    -   $p\leftrightarrow q=p\odot q=\lnot(p\oplus q)$,
    -   $p\nrightarrow q=\lnot(p\to q)$,
    -   $p\gets q=q\to p$,
    -   $p\nleftarrow q=\lnot(p\gets q)$.

Can we describe all logical operators using a given set of logical operators? This leads to the definition of a functionally complete set of operators.

???+ abstract "Definition"
    For a given set of logical operators, if all logical operators can be described using only the functions in this set, the set is called a **functionally complete operator set**. In particular, if all logical operators can be described using a single logical operator, that operator is called a **sole sufficient operator** or a **Sheffer function**.
    
    If removing any element from a functionally complete operator set makes it unable to describe all logical operators, the set is called a **minimal functionally complete operator set**.

It can be proven that among the logical operators only $\bar{\land}$ and $\bar{\lor}$ are sole sufficient operators.

Below are the common minimal functionally complete operator sets[^vaughan1942complete]:

-   $\{\bar{\land}\}$, $\{\bar{\lor}\}$,
-   $\{\land,\lnot\}$, $\{\lor,\lnot\}$, $\{\gets,\lnot\}$, $\{\to,\lnot\}$, $\{\nleftarrow,\lnot\}$, $\{\nrightarrow,\lnot\}$,
-   $\{\gets,\bot\}$, $\{\to,\bot\}$, $\{\nleftarrow,\top\}$, $\{\nrightarrow,\top\}$,
-   $\{\gets,\nleftarrow\}$, $\{\to,\nleftarrow\}$, $\{\gets,\nrightarrow\}$, $\{\to,\nrightarrow\}$,
-   $\{\gets,\nleftrightarrow\}$, $\{\to,\nleftrightarrow\}$, $\{\nleftarrow,\leftrightarrow\}$, $\{\nrightarrow,\leftrightarrow\}$,
-   $\{\lor,\leftrightarrow,\bot\}$, $\{\lor,\leftrightarrow,\nleftrightarrow\}$, $\{\lor,\nleftrightarrow,\top\}$,
-   $\{\land,\leftrightarrow,\bot\}$, $\{\land,\leftrightarrow,\nleftrightarrow\}$, $\{\land,\nleftrightarrow,\top\}$.

### Properties

First, properties related to algebraic structures:

-   AND and OR each form a [commutative monoid](./algebra/basic.md#群) on $\mathbf{B}$. That is, AND and OR are both commutative and associative and have an identity element ($x\land 1=x\lor 0=x$).
-   XOR and XNOR each form a [group](./algebra/basic.md#群) on $\mathbf{B}$. That is, XOR and XNOR are both commutative and associative, have an identity element ($x\oplus 0=x\odot 1=x$), and have inverse elements ($x\oplus x=0$, $x\odot x=1$).
-   NAND and NOR are not associative, so they do not form a semigroup.

For $\land$ and $\lor$, we have

-   distributivity:
    -   $a\land(b\diamond c)=(a\land b)\diamond (a\land c)$, where $\diamond$ can be $\land$, $\lor$, $\oplus$,
    -   $a\lor(b\diamond c)=(a\lor b)\diamond (a\lor c)$, where $\diamond$ can be $\land$, $\lor$, $\odot$.
-   **idempotence**: $x\land x=x$, $x\lor x=x$.
-   monotonicity: $a\to b\iff(a\land c)\to(b\land c)$, $a\to b\iff(a\lor c)\to(b\lor c)$.
-   **absorption**: $x\land(x\lor y)=x\lor(x\land y)=x$.
-   relation to "$\to$":
    -   $a \lor b \iff (\lnot a \to b) \land (\lnot b \to a)$,
    -   $a \land b \iff \lnot((a \to \lnot b) \lor (b \to \lnot a))$.

???+ abstract "Monotonicity of a Boolean function"
    For a Boolean function $f(x_1,\dots,x_n)$ and two elements $(a_1,\dots,a_n),(b_1,\dots,b_n)$ of $\mathbf{B}^n$, if $a_i\leq b_i,~~\forall i=1,\dots,n$ always implies $f(a_1,\dots,a_n)\leq f(b_1,\dots,b_n)$, the Boolean function is said to be monotone.

We also have the following properties:

-   **law of excluded middle**: $p\lor\lnot p$ is a tautology.
-   $\lnot p\iff p\to\bot$.
-   double negation / **involution** of $\lnot$: $\lnot\lnot x=x$.
-   involution of $\oplus$ and $\odot$: $x\oplus y\oplus y=x$, $x\odot y\odot y=x$.
-   De Morgan's laws: $\lnot(p\land q)=\lnot p\lor \lnot q$, $\lnot(p\lor q)=\lnot p\land \lnot q$.

## Normalization of logical expressions

Based on the above properties, we can apply equivalence transformations to logical expressions so that they conform to a particular normal form, which is useful in automated theorem proving. Common normal forms are the **conjunctive normal form** (CNF), the **disjunctive normal form** (DNF), and the **algebraic normal form** (ANF).

???+ abstract "Conjunctive and disjunctive normal form"
    We make the following recursive definitions:
    
    1.  **Literal**: for a variable $x$, $x$ and $\lnot x$ are literals.
    2.  Clause:
        -   a literal is a clause,
        -   if $A$ is a literal and $B$ is a clause, then $A\lor B$ is a clause.
    3.  Conjunctive normal form:
        -   if $A$ is a clause, then $(A)$ is a conjunctive normal form,
        -   if $A$ is a clause and $B$ is a conjunctive normal form, then $(A)\land B$ is a conjunctive normal form.
    
    Similarly, swapping $\land$ and $\lor$ in the above definition gives the definition of the disjunctive normal form.

For example, the following logical expressions are all in disjunctive normal form:

-   $(A\land\lnot B)\lor(C\land D\land\lnot E)$,
-   $(A\land B)\lor (C)$,
-   $(A\land B)$,
-   $(A)$.

The following logical expressions are all in conjunctive normal form:

-   $(\lnot A\lor\lnot B\lor C)\land(\lor D\lor\lnot E)$,
-   $(A\lor B)\land (C)$,
-   $(A\lor B)$,
-   $(A)$.

The following logical expressions are in neither conjunctive nor disjunctive normal form:

-   $\lnot(A\land B)$,
-   $A\land (B\lor (C\land D))$.

We can transform any logical expression containing only the operations $\lnot$, $\land$, $\lor$ into DNF with the following steps:

$$
\begin{array}{rcccl}
    \lnot\lnot x &&\mapsto&& x,\\
    \lnot(x\lor y) &&\mapsto&& \lnot x\land \lnot y,\\
    \lnot(x\land y) &&\mapsto&& \lnot x\lor \lnot y,\\
    x\land(y\lor z) &&\mapsto&& (x\land y)\lor (x\land z),\\
    (x\lor y)\land z &&\mapsto&& (x\land z)\lor (y\land z).
\end{array}
$$

To obtain the CNF of an expression $X$, it suffices to obtain the DNF of $\lnot X$, negate it, and apply De Morgan's laws.

???+ abstract "Algebraic normal form"
    First, we define monomials with the following recursive definition:
    
    -   a variable $x$ is a monomial,
    -   if $A$ is a monomial and $x$ is a variable, then $x\land A$ is a monomial.
    
    Then a logical expression of one of the following three forms is an algebraic normal form:
    
    1.  $1$, $0$,
    2.  the XOR of several non-equivalent monomials, e.g. $a\oplus b\oplus(a\land b)\oplus(a\land b\land c)$,
    3.  the XOR of several non-equivalent monomials and a single $1$, e.g. $1\oplus a\oplus b\oplus(a\land b)\oplus(a\land b\land c)$.

Note that algebraic normal forms are in one-to-one correspondence with polynomials over $\mathbf{Z}_2$, so the algebraic normal form is also called the **Zhegalkin polynomial**.

We can transform any logical expression containing only the operations $\lnot$, $\land$, $\lor$, $\oplus$ into ANF with the following steps:

1.  $\oplus$: expand directly, e.g. $(1\oplus x)\oplus(1\oplus x\oplus y)=1\oplus x\oplus 1\oplus x\oplus y=y$,
2.  $\land$: expand using distributivity, e.g. $x\land(1\oplus x\oplus y)=(x\land 1)\oplus (x\land x)\oplus (x\land y)=x\oplus (x\land y)$,
3.  $\lnot$: replace $\lnot x$ with $1\oplus x$, e.g. $\lnot(1\oplus x\oplus y)=1\oplus 1\oplus x\oplus y=x\oplus y$,
4.  $\lor$: replace $x\lor y$ with $1\oplus((1\oplus x)\land(1\oplus y))$ or $x\oplus y\oplus (x\land y)$, e.g. $(1\oplus x)\lor(1\oplus x\oplus y)=1\oplus((1\oplus 1\oplus x)\land(1\oplus 1\oplus x\oplus y))=1\oplus x\oplus(x\land y)$.

## References and notes

1.  [Boolean algebra - Wikipedia](https://en.wikipedia.org/wiki/Boolean_algebra)
2.  [Boolean function - Wikipedia](https://en.wikipedia.org/wiki/Boolean_function)
3.  [Logical connective - Wikipedia](https://en.wikipedia.org/wiki/Logical_connective)
4.  [Disjunctive normal form - Wikipedia](https://en.wikipedia.org/wiki/Disjunctive_normal_form)
5.  [Zhegalkin polynomial - Wikipedia](https://en.wikipedia.org/wiki/Zhegalkin_polynomial)

[^note1]: When used for propositional derivations, double long arrows should be used, e.g. $A\implies B$, $A\impliedby B$, $A\iff B$, etc.

[^note2]: Equivalent to XNOR.

[^note3]: Equivalent to XOR.

[^vaughan1942complete]: Vaughan, H. E. (1942). Complete sets of logical functions.*Transactions of the American Mathematical Society 51*: 117–32.
