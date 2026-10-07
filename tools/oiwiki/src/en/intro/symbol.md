---
title: Table of mathematical symbols
---

This document specifies the recommended way of writing mathematical symbols on **OI Wiki** and gives some examples of their use.

It was compiled with reference to the symbol tables of [GB/T 3102.11-1993](https://openstd.samr.gov.cn/bzgk/gb/newGbInfo?hcno=3DE79450D562E62D41CB6E79FF411054), [ISO 80000-2:2019](https://www.iso.org/standard/64973.html) and *Concrete Mathematics*, so it is basically compatible with the notation of common Chinese textbooks and with the notation customary in OI.

For the LaTeX source of the symbols, see [the source code of this article](https://github.com/OI-wiki/OI-wiki/blob/master/docs/intro/symbol.md?plain=1)

## Mathematical logic

| No. | Symbol, expression | Meaning, equivalent expressions | Remarks and examples |
| --- | --- | --- | --- |
| <span id="n1.1">n1.1</span> | $p \land q$ | conjunction of $p$ and $q$ | $p$ and $q$. |
| <span id="n1.2">n1.2</span> | $p \lor q$ | disjunction of $p$ and $q$ | $p$ or $q$;<br>the "or" here is inclusive, i.e. if at least one of the statements $p$, $q$ is true, then $p \lor q$ is true. |
| <span id="n1.3">n1.3</span> | $\lnot p$ | negation of $p$ | not $p$. |
| <span id="n1.4">n1.4</span> | $p \implies q$ | $p$ implies $q$;<br>if $p$ is true, then $q$ is true | $q \impliedby p$ and $p \implies q$ mean the same. |
| <span id="n1.5">n1.5</span> | $p \iff q$ | $p$ is equivalent to $q$ | $(p \implies q) \land (q \implies p)$ and $p \iff q$ mean the same. |
| <span id="n1.6">n1.6</span> | $(\forall~x \in A)~~p(x)$ | for all $x$ in $A$, the proposition $p(x)$ is true | If it is clear from the context which set $A$ is being considered, the notation $(\forall~x)~~p(x)$ may be used.<br>$\forall$ is called the universal quantifier.<br>For the meaning of $x \in A$ see [n2.1](#n2.1). |
| <span id="n1.7">n1.7</span> | $(\exists~x \in A)~~p(x)$ | there exists an $x$ in $A$ such that $p(x)$ is true | If it is clear from the context which set $A$ is being considered, the notation $(\exists~x)~~p(x)$ may be used.<br>$\exists$ is called the existential quantifier.<br>For the meaning of $x \in A$ see [n2.1](#n2.1).<br>$(\exists!~x)~~p(x)$ (uniqueness quantifier) denotes that there is exactly one $x$ such that $p(x)$ is true.<br>$\exists!$ may also be written $\exists^1$. |

## Set theory

| No. | Symbol, expression | Meaning, equivalent expressions | Remarks and examples |
| --- | --- | --- | --- |
| <span id="n2.1">n2.1</span> | $x \in A$ | $x$ belongs to $A$, $x$ is an element of the set $A$ | $A \ni x$ and $x \in A$ mean the same. |
| <span id="n2.2">n2.2</span> | $y \notin A$ | $y$ does not belong to $A$, $y$ is not an element of the set $A$ | |
| <span id="n2.3">n2.3</span> | $\{x_1, x_2, \dots, x_n\}$ | the set with elements $x_1, x_2, \dots, x_n$ | May also be written $\{x_i ~\vert~ i \in I\}$, where $I$ denotes an index set. |
| <span id="n2.4">n2.4</span> | $\{x \in A ~\vert~ p(x)\}$ | the set of all elements of $A$ for which the proposition $p(x)$ is true | For example $\{x \in \textbf{R} ~\vert~ x \geq 5\}$;<br>if it is clear from the context which set $A$ is being considered, the notation $\{x ~\vert~ p(x)\}$ may be used (e.g. when only the set of real numbers is considered, $\{x ~\vert~ x \geq 5\}$ may be used)<br>$\vert$ may be replaced by a colon, e.g. $\{x \in A : p(x)\}$. |
| <span id="n2.5">n2.5</span> | $\operatorname{card} A$;<br>$\vert A\vert$;<br>$\# A$ | number of elements of $A$, cardinality of $A$ | |
| <span id="n2.6">n2.6</span> | $\varnothing$ | the empty set | $\emptyset$ should not be used. |
| <span id="n2.7">n2.7</span> | $B \subseteq A$ | $B$ is included in $A$, $B$ is a subset of $A$ | Every element of $B$ belongs to $A$.<br>$\subset$ may also be used in this meaning, but see the remark on [n2.8](#n2.8).<br>$A \supseteq B$ and $B \subseteq A$ mean the same. |
| <span id="n2.8">n2.8</span> | $B \subset A$ | $B$ is properly included in $A$, $B$ is a proper subset of $A$ | Every element of $B$ belongs to $A$, and at least one element of $A$ does not belong to $B$.<br>If $\subset$ takes the meaning of [n2.7](#n2.7), then the symbol for [n2.8](#n2.8) should be $\subsetneq$.<br>$A \supset B$ and $B \subset A$ mean the same. |
| <span id="n2.9">n2.9</span> | $A \cup B$ | union of $A$ and $B$ | $A \cup B := \{x ~\vert~ x \in A \lor x \in B\}$;<br>for the definition of $:=$ see [n4.3](#n4.3) |
| <span id="n2.10">n2.10</span> | $A \cap B$ | intersection of $A$ and $B$ | $A \cap B := \{x ~\vert~ x \in A \land x \in B\}$;<br>for the definition of $:=$ see [n4.3](#n4.3) |
| <span id="n2.11">n2.11</span> | $\displaystyle \bigcup\limits_{i=1}^n A_i$ | union of the sets $A_1, A_2, \dots, A_n$ | $\displaystyle \bigcup\limits_{i=1}^n A_i=A_1\cup A_2\cup \dots \cup A_n$;<br>$\displaystyle \bigcup\nolimits_{i=1}^n$, $\displaystyle \bigcup\limits_{i\in I}$, $\displaystyle \bigcup\nolimits_{i\in I}$ may also be used, where $I$ denotes an index set;<br>furthermore, if $P(i)$ is some proposition about $i$, $\displaystyle \bigcup_{P(i)} A_i$ may be used to denote the union of the $A_i$ for all $i$ for which $P(i)$ is true |
| <span id="n2.12">n2.12</span> | $\displaystyle \bigcap\limits_{i=1}^n A_i$ | intersection of the sets $A_1, A_2, \dots, A_n$ | $\displaystyle \bigcap\limits_{i=1}^n A_i=A_1\cap A_2\cap \dots \cap A_n$;<br>$\displaystyle \bigcap\nolimits_{i=1}^n$, $\displaystyle \bigcap\limits_{i\in I}$, $\displaystyle \bigcap\nolimits_{i\in I}$ may also be used, where $I$ denotes an index set;<br>furthermore, if $P(i)$ is some proposition about $i$, $\displaystyle \bigcap_{P(i)} A_i$ may be used to denote the intersection of the $A_i$ for all $i$ for which $P(i)$ is true |
| <span id="n2.13">n2.13</span> | $A \setminus B$ | difference of $A$ and $B$ | $A \setminus B = \{x ~\vert~ x \in A \land x \notin B\}$;<br>$A - B$ should not be used;<br>when $B$ is a subset of $A$, $\complement_A B$ may also be used, and if it is clear from the context which set $A$ is being considered, $A$ may be omitted.<br>When there is no ambiguity, $\overline{B}$ may also be used to denote the complement of the set $B$. |
| <span id="n2.14">n2.14</span> | $(a, b)$ | ordered pair $a$, $b$;<br>couple $a$, $b$ | $(a, b) = (c, d)$ if and only if $a = c$ and $b = d$. |
| <span id="n2.15">n2.15</span> | $(a_1, a_2, \dots, a_n)$ | ordered $n$-tuple | See [n2.14](#n2.14). |
| <span id="n2.16">n2.16</span> | $A \times B$ | Cartesian product of the sets $A$ and $B$ | $A \times B = \{(x, y) ~\vert~ x \in A \land y \in B\}$. |
| <span id="n2.17">n2.17</span> | $\displaystyle \prod\limits_{i=1}^{n} A_i$ | Cartesian product of the sets $A_1, A_2, \dots, A_n$ | $\displaystyle \prod\limits_{i=1}^{n} A_i=\{(x_1, x_2, \dots, x_n) ~\vert~ x_1 \in A_1, x_2 \in A_2, \dots, x_n \in A_n\}$;<br>$A \times A \times \dots \times A$ is denoted by $A^n$, where $n$ is the number of factors in the product;<br>for another use of this symbol see [n6.8](#n6.8) |
| <span id="n2.18">n2.18</span> | $\mathrm{id}_A$ | diagonal of $A\times A$ | $\mathrm{id}_A=\{(x, x)~\vert~x\in A\}$;<br>if it is clear from the context which set $A$ is being considered, $A$ may be omitted. |
| <span id="n2.19">n2.19</span> | $\mathbf{1}_A$ | indicator function | $\mathbf{1}_A(a)=[a\in A]$, for the definition of $[\cdot]$ see [n6.24](#n6.24). |
| <span id="n2.20">n2.20</span> | $\mathcal{P}(A)$;<br>$2^A$ | power set | $\mathcal{P}(A)=\{S:S\subseteq A\}$ |

## Standard number sets and intervals

| No. | Symbol, expression | Meaning, equivalent expressions | Remarks and examples |
| --- | --- | --- | --- |
| <span id="n3.1">n3.1</span> | $\mathbf{N}$ | the set of natural numbers | $\mathbf{N} = \{0, 1, 2, 3, \dots\}$;<br>$\mathbf{N}^* = \mathbf{N}_+ = \{1, 2, 3, \dots\}$;<br>other restrictions can be added as follows: $\mathbf{N}_{> 5} = \{n \in \mathbf{N} ~\vert~ n > 5\}$;<br>$\mathbb{N}$ may also be used. |
| <span id="n3.2">n3.2</span> | $\mathbf{Z}$ | the set of integers | $\mathbf{Z}^* = \mathbf{Z}_+ = \{n \in \mathbf{Z} ~\vert~ n \ne 0\}$;<br>other restrictions can be added as follows: $\mathbf{Z}_{> -3} = \{n \in \mathbf{Z} ~\vert~ n > -3\}$;<br>$\mathbb{Z}$ may also be used. |
| <span id="n3.3">n3.3</span> | $\mathbf{Q}$ | the set of rational numbers | $\mathbf{Q}^* = \mathbf{Q}_+ = \{r \in \mathbf{Q} ~\vert~ r \ne 0\}$;<br>other restrictions can be added as follows: $\mathbf{Q}_{< 0} = \{r \in \mathbf{Q} ~\vert~ r < 0\}$;<br>$\mathbb{Q}$ may also be used. |
| <span id="n3.4">n3.4</span> | $\mathbf{R}$ | the set of real numbers | $\mathbf{R}^* = \mathbf{R}_+ = \{x \in \mathbf{R} ~\vert~ x \ne 0\}$;<br>other restrictions can be added as follows: $\mathbf{R}_{> 0} = \{x \in \mathbf{R} ~\vert~ x > 0\}$;<br>$\mathbb{R}$ may also be used. |
| <span id="n3.5">n3.5</span> | $\mathbf{C}$ | the set of complex numbers | $\mathbf{C}^* = \mathbf{C}_+ = \{z \in \mathbf{C} ~\vert~ z \ne 0\}$;<br>$\mathbb{C}$ may also be used. |
| <span id="n3.6">n3.6</span> | $\mathbf{P}$ | the set of (positive) primes | $\mathbf{P} = \{2, 3, 5, 7, 11, 13, 17, \dots\}$;<br>$\mathbb{P}$ may also be used. |
| <span id="n3.7">n3.7</span> | $[a, b]$ | closed interval from $a$ to $b$ | $[a, b] = \{x \in \mathbf{R} ~\vert~ a \leq x \leq b\}$. |
| <span id="n3.8">n3.8</span> | $(a, b]$ | interval from $a$ to $b$, open on the left and closed on the right | $(a, b] = \{x \in \mathbf{R} ~\vert~ a < x \leq b\}$;<br>$(-\infty, b] = \{x \in \mathbf{R} ~\vert~ x \leq b\}$. |
| <span id="n3.9">n3.9</span> | $[a, b)$ | interval from $a$ to $b$, closed on the left and open on the right | $[a, b) = \{x \in \mathbf{R} ~\vert~ a \leq x < b\}$;<br>$[a, +\infty) = \{x \in \mathbf{R} ~\vert~ a \leq x\}$. |
| <span id="n3.10">n3.10</span> | $(a, b)$ | open interval from $a$ to $b$ | $(a, b) = \{x \in \mathbf{R} ~\vert~ a < x < b\}$;<br>$(-\infty, b) = \{x \in \mathbf{R} ~\vert~ x < b\}$;<br>$(a, +\infty) = \{x \in \mathbf{R} ~\vert~ a < x\}$. |

## Relations

| No. | Symbol, expression | Meaning, equivalent expressions | Remarks and examples |
| --- | --- | --- | --- |
| <span id="n4.1">n4.1</span> | $a = b$ | $a$ is equal to $b$ | $\equiv$ is used to emphasize that an equality is an identity<br>for another meaning of this symbol see [n4.18](#n4.18). |
| <span id="n4.2">n4.2</span> | $a \ne b$ | $a$ is not equal to $b$ | |
| <span id="n4.3">n4.3</span> | $a := b$ | $a$ is by definition equal to $b$ | See [n2.9](#n2.9),[n2.10](#n2.10) |
| <span id="n4.4">n4.4</span> | $a \approx b$ | $a$ is approximately equal to $b$ | Equality is not excluded. |
| <span id="n4.5">n4.5</span> | $a \simeq b$ | $a$ is asymptotically equal to $b$ | For example:<br>as $x\to a$, $\dfrac{1}{\sin(x-a)} \simeq \dfrac{1}{x-a}$;<br>for the meaning of $x \to a$ see [n4.15](#n4.15). |
| <span id="n4.6">n4.6</span> | $a \propto b$ | $a$ is proportional to $b$ | $a \sim b$ may also be used.<br>$\sim$ is also used for equivalence relations. |
| <span id="n4.7">n4.7</span> | $M \cong N$ | $M$ is congruent to $N$ | When $M$ and $N$ are point sets (geometric figures).<br>This symbol is also used for isomorphism of algebraic structures. |
| <span id="n4.8">n4.8</span> | $a < b$ | $a$ is less than $b$ | |
| <span id="n4.9">n4.9</span> | $b > a$ | $b$ is greater than $a$ | |
| <span id="n4.10">n4.10</span> | $a \leq b$ | $a$ is less than or equal to $b$ | |
| <span id="n4.11">n4.11</span> | $b \geq a$ | $b$ is greater than or equal to $a$ | |
| <span id="n4.12">n4.12</span> | $a \ll b$ | $a$ is much less than $b$ | |
| <span id="n4.13">n4.13</span> | $b \gg a$ | $b$ is much greater than $a$ | |
| <span id="n4.14">n4.14</span> | $\infty$ | infinity | This symbol is **not** a number.<br>$+\infty$, $-\infty$ may also be used. |
| <span id="n4.15">n4.15</span> | $x \to a$ | $x$ tends to $a$ | Usually appears in limit expressions.<br>$a$ may also be $\infty$, $+\infty$, $-\infty$. |
| <span id="n4.16">n4.16</span> | $m \mid n$ | $m$ divides $n$ | For integers $m$, $n$:<br>$(\exists~k \in \mathbf{Z})~~m\cdot k = n$. |
| <span id="n4.17">n4.17</span> | $m \perp n$ | $m$ and $n$ are coprime | For integers $m$, $n$:<br>$(\nexists~k \in \mathbf{Z}_{>1})~~(k \mid m) \land (k \mid n)$;<br>for another use of this symbol see [n5.2](#n5.2) |
| <span id="n4.18">n4.18</span> | $n \equiv k \pmod m$ | $n$ is congruent to $k$ modulo $m$ | For integers $n$, $k$, $m$:<br>$m \mid (n - k)$;<br>not to be confused with the meaning in [n4.1](#n4.1). |

## Elementary geometry

| No. | Symbol, expression | Meaning, equivalent expressions | Remarks and examples |
| --- | --- | --- | --- |
| <span id="n5.1">n5.1</span> | $\parallel$ | parallel | |
| <span id="n5.2">n5.2</span> | $\perp$ | perpendicular | for another use of this symbol see [n4.17](#n4.17) |
| <span id="n5.3">n5.3</span> | $\angle$ | (plane) angle | |
| <span id="n5.4">n5.4</span> | $\overline{\mathrm{AB}}$ | line segment $\mathrm{AB}$ | |
| <span id="n5.5">n5.5</span> | $\overrightarrow{\mathrm{AB}}$ | directed line segment $\mathrm{AB}$ | |
| <span id="n5.6">n5.6</span> | $d(\mathrm{A}, \mathrm{B})$ | distance between the points $\mathrm{A}$ and $\mathrm{B}$ | i.e. the length of $\overline{\mathrm{AB}}$. |

## Operations

| No. | Symbol, expression | Meaning, equivalent expressions | Remarks and examples |
| --- | --- | --- | --- |
| <span id="n6.1">n6.1</span> | $a + b$ | $a$ plus $b$ | |
| <span id="n6.2">n6.2</span> | $a - b$ | $a$ minus $b$ | |
| <span id="n6.3">n6.3</span> | $a \pm b$ | $a$ plus or minus $b$ | |
| <span id="n6.4">n6.4</span> | $a \mp b$ | $a$ minus or plus $b$ | $-(a \pm b) = -a \mp b$. |
| <span id="n6.5">n6.5</span> | $a \cdot b$;<br>$a \times b$;<br>$ab$ | $a$ multiplied by $b$ | If a decimal point appears, only $\times$ should be used;<br>for some use cases see [n2.16](#n2.16),[n2.17](#n2.17),[n14.11](#n14.11),[n14.12](#n14.12) |
| <span id="n6.6">n6.6</span> | $\dfrac{a}{b}$;<br>$a/b$;<br>$a:b$ | $a$ divided by $b$ | $\dfrac{a}{b}=a\cdot b^{-1}$;<br>$:$ may be used for the ratio of numerical values of the same dimension.<br>$÷$ should not be used. |
| <span id="n6.7">n6.7</span> | $\displaystyle \sum\limits_{i=1}^n a_i$ | $a_1 + a_2 + \dots + a_n$ | $\displaystyle \sum\nolimits_{i=1}^n a_i$, $\displaystyle \sum\limits_i a_i$, $\displaystyle \sum\nolimits_i a_i$, $\displaystyle \sum a_i$ may also be used;<br>if $P(i)$ is some proposition about $i$, $\displaystyle \sum_{P(i)} a_i$ may be used to denote the sum of the $a_i$ for all $i$ for which $P(i)$ is true. |
| <span id="n6.8">n6.8</span> | $\displaystyle \prod\limits_{i=1}^n a_i$ | $a_1 \cdot a_2 \cdot \dots \cdot a_n$ | $\displaystyle \prod\nolimits_{i=1}^n a_i$, $\displaystyle \prod\limits_i a_i$, $\displaystyle \prod\nolimits_i a_i$, $\displaystyle \prod a_i$ may also be used;<br>if $P(i)$ is some proposition about $i$, $\displaystyle \prod_{P(i)} a_i$ may be used to denote the product of the $a_i$ for all $i$ for which $P(i)$ is true;<br>for another use of this symbol see [n2.17](#n2.17) |
| <span id="n6.9">n6.9</span> | $a^p$ | $a$ to the power $p$ | |
| <span id="n6.10">n6.10</span> | $a^{1/2}$;<br>$\sqrt{a}$ | $a$ to the power $1/2$, square root of $a$ | $\sqrt{}a$ should be avoided. |
| <span id="n6.11">n6.11</span> | $a^{1/n}$;<br>$\sqrt[n]{a}$ | $a$ to the power $1/n$, $n$-th root of $a$ | $\sqrt[n]{}a$ should be avoided. |
| <span id="n6.12">n6.12</span> | $\bar{x}$;<br>$\bar{x}_a$ | arithmetic mean of $x$ | Other means include:<br>harmonic mean $\bar{x}_h$;<br>geometric mean $\bar{x}_g$;<br>quadratic mean / root mean square $\bar{x}_q$ or $\bar{x}_{rms}$.<br>$\bar{x}$ is also used for the conjugate of the complex number $x$, see [n11.6](#n11.6). |
| <span id="n6.13">n6.13</span> | $\operatorname{sgn} a$ | sign function of $a$ | For a real number $a$:<br>$\operatorname{sgn} a=1\quad (a>0)$;<br>$\operatorname{sgn} a=-1\quad (a<0)$;<br>$\operatorname{sgn} 0=0$;<br>see [n11.7](#n11.7). |
| <span id="n6.14">n6.14</span> | $\inf M$ | infimum of $M$ | Greatest lower bound of the non-empty set $M$. |
| <span id="n6.15">n6.15</span> | $\sup M$ | supremum of $M$ | Least upper bound of the non-empty set $M$. |
| <span id="n6.16">n6.16</span> | $\lvert a\rvert$ | absolute value of $a$ | $\operatorname{abs} a$ may also be used. |
| <span id="n6.17">n6.17</span> | $\lfloor a\rfloor$ | floor<br>the greatest integer less than or equal to the real number $a$ | For example:<br>$\lfloor 2.4\rfloor = 2$;<br>$\lfloor -2.4\rfloor = -3$. |
| <span id="n6.18">n6.18</span> | $\lceil a\rceil$ | ceiling<br>the least integer greater than or equal to the real number $a$ | For example:<br>$\lceil 2.4\rceil = 3$;<br>$\lceil -2.4\rceil = -2$. |
| <span id="n6.19">n6.19</span> | $\min(a, b)$;<br>$\min\{a, b\}$ | minimum of $a$ and $b$ | Can be generalized to finite sets.<br>To denote the minimum of an infinite set, $\inf$ is recommended, see [n6.14](#n6.14) |
| <span id="n6.20">n6.20</span> | $\max(a, b)$;<br>$\max\{a, b\}$ | maximum of $a$ and $b$ | Can be generalized to finite sets.<br>To denote the maximum of an infinite set, $\sup$ is recommended, see [n6.15](#n6.15) |
| <span id="n6.21">n6.21</span> | $n \bmod m$ | remainder of $n$ modulo $m$ | For positive integers $n$, $m$:<br>$(\exists~q\in\mathbf{N}, r\in[0, m))~~n=qm+r$;<br>where $r=n \bmod m$. |
| <span id="n6.22">n6.22</span> | $\gcd(a, b)$;<br>$\gcd\{a, b\}$ | greatest common divisor of the integers $a$ and $b$ | Can be generalized to finite sets. When there is no ambiguity it may be written $(a, b)$. |
| <span id="n6.23">n6.23</span> | $\operatorname{lcm}(a, b)$;<br>$\operatorname{lcm}\{a, b\}$ | least common multiple of the integers $a$ and $b$ | Can be generalized to finite sets. When there is no ambiguity it may be written $[a, b]$;<br>$(a, b)[a, b]=\lvert ab\rvert$. |
| <span id="n6.24">n6.24</span> | $[P]$ | Iverson bracket | If the proposition $P$ is true, then $[P]=1$, otherwise $[P]=0$. |
| <span id="n6.25">n6.25</span> | $a\uparrow b$;<br>$a\uparrow^{n} b$ | Knuth's arrow | For non-negative integers $a,b,n$:<br>$a\uparrow^{n} b=a~\underbrace{\uparrow\dots\uparrow}_{n \text{ times}}~b$;<br>$a\uparrow^{0} b=ab$;<br>$a\uparrow^{1} b=a\uparrow b=a^b$;<br>$a\uparrow^{n} 0=1\quad(n>0)$;<br>$a\uparrow^{n}b=a\uparrow^{n-1}(a\uparrow^{n}(b-1))$. |
| <span id="n6.26">n6.26</span> | $[x^n]f(x)$ | coefficient of the term $x^n$ in the polynomial / formal power series / formal Laurent series $f(x)$ | If $\displaystyle f(x)=\sum_{i} a_ix^i$, then $[x^n]f(x)=a_n$;<br>can be generalized to several variables, e.g. if $\displaystyle f(x,y)=\sum_{i,j}a_{i,j}x^iy^j$, then $[x^ny^m]f(x,y)=a_{n,m}$. |

## Combinatorics

In this section $n$ and $k$ are natural numbers, $a$ is a complex number, and $k\leq n$.

| No. | Symbol, expression | Meaning, equivalent expressions | Remarks and examples |
| --- | --- | --- | --- |
| <span id="n7.1">n7.1</span> | $n!$ | factorial | $n!=\prod_{k=1}^n k=1\cdot 2\cdot 3\cdot \dots \cdot n\quad (n>0)$;<br>$0!=1$. |
| <span id="n7.2">n7.2</span> | $a^{\underline{k}}$;<br>$(a)_{-k}$ | falling factorial power | $a^{\underline{k}}=a\cdot(a-1)\cdot \dots \cdot(a-k+1)\quad (k>0)$;<br>$a^{\underline{0}}=1$;<br>$n^{\underline{k}}=\dfrac{n!}{(n-k)!}$. |
| <span id="n7.3">n7.3</span> | $a^{\overline{k}}$;<br>$(a)_{+k}$ | rising factorial power | $a^{\overline{k}}=a\cdot(a+1)\cdot \dots \cdot(a+k-1)\quad (k>0)$;<br>$a^{\overline{0}}=1$;<br>$n^{\overline{k}}=\dfrac{(n+k-1)!}{(n-1)!}$. |
| <span id="n7.4">n7.4</span> | $\dbinom{n}{k}$ | binomial coefficient | $\dbinom{n}{k}=\dfrac{n!}{k!(n-k)!}$. |
| <span id="n7.5">n7.5</span> | $\displaystyle{n\brack k}$ | Stirling number of the first kind | $\displaystyle{n+1\brack k}=n{n\brack k}+{n\brack k-1}$;<br>$\displaystyle x^{\overline{n}}=\sum_{k=0}^n{n\brack k}x^k$. |
| <span id="n7.6">n7.6</span> | $\displaystyle{n\brace k}$ | Stirling number of the second kind | $\displaystyle{n\brace k}=\frac{1}{k!}\sum_{i=0}^k(-1)^i\binom{k}{i}(k-i)^n$;<br>$\displaystyle\sum_{k=0}^n{n\brace k}x^{\underline{k}}=x^n$. |

## Functions

| No. | Symbol, expression | Meaning, equivalent expressions | Remarks and examples |
| --- | --- | --- | --- |
| <span id="n8.1">n8.1</span> | $f$ | function | |
| <span id="n8.2">n8.2</span> | $f(x)$, $f(x_1, \dots, x_n)$ | value of the function $f$ at $x$<br>value of the function $f$ at $(x_1, \dots, x_n)$ | |
| <span id="n8.3">n8.3</span> | $\operatorname{dom} f$ | domain of $f$ | $\mathrm{D}(f)$ may also be used. |
| <span id="n8.4">n8.4</span> | $\operatorname{ran} f$ | range of $f$ | $\mathrm{R}(f)$ may also be used. |
| <span id="n8.5">n8.5</span> | $f:A\to B$ | $f$ is a mapping from $A$ to $B$ | $\operatorname{dom} f=A$ and $(\forall~x \in\operatorname{dom} f)~~ f(x) \in B$. |
| <span id="n8.6">n8.6</span> | $x\mapsto T(x), x\in A$ | the function that maps every $x\in A$ to $T(x)$ | $T(x)$ is used only for the definition and denotes the value of some function with argument $x\in A$. If this function is $f$, then $f(x)=T(x)$ for all $x\in A$. Hence $T(x)$ is usually used to define the function $f$.<br>For example:<br>$x\mapsto 3x^2y, x\in[0, 2]$;<br>this is a quadratic function of $x$ defined by $3x^2y$. If no function symbol is introduced, the function is denoted by $3x^2y$ |
| <span id="n8.7">n8.7</span> | $f^{-1}$ | inverse function of $f$ | The inverse function $f^{-1}$ of the function $f$ is defined if and only if $f$ is injective.<br>If $f$ is injective, then $\operatorname{dom}\left(f^{-1}\right) = \operatorname{ran} f$, $\operatorname{ran}\left(f^{-1}\right) = \operatorname{dom} f$, and $(\forall~x\in\operatorname{dom} f)~~f^{-1}(f(x)) = x$.<br>Not to be confused with the reciprocal of the function, $f(x)^{-1}$. |
| <span id="n8.8">n8.8</span> | $g\circ f$ | composition of the functions $f$ and $g$ | $(g\circ f)(x)=g(f(x))$. |
| <span id="n8.9">n8.9</span> | $f:x\mapsto y$ | $f(x)=y$, $f$ maps $x$ to $y$ | |
| <span id="n8.10">n8.10</span> | $f\vert_a^b$;<br>$f(\dots, u, \dots)\vert_{u=a}^{u=b}$ | $f(b)-f(a)$;<br>$f(\dots, b, \dots)-f(\dots, a, \dots)$ | Mainly used in the computation of definite integrals. |
| <span id="n8.11">n8.11</span> | $\displaystyle \lim\limits_{x\to a}f(x)$;<br>$\lim\nolimits_{x\to a}f(x)$ | limit of $f(x)$ as $x$ tends to $a$ | $\lim\nolimits_{x\to a}f(x)=b$ may be written $f(x)\to b\quad (x \to a)$.<br>The notations for the right-hand and left-hand limits are $\lim\nolimits_{x\to a+}f(x)$ and<br>$\lim\nolimits_{x\to a-}f(x)$ respectively. |
| <span id="n8.12">n8.12</span> | $f(x) = O(g(x))$ | $\lvert f(x)/g(x)\rvert$ is bounded within the limits implied by the context, the order of $f(x)$ is not higher than that of $g(x)$ | When both $f/g$ and $g/f$ are bounded, $f$ and $g$ are said to be of the same order.<br>The symbol "$=$" is used for historical reasons; here it does not denote equivalence, since it is not transitive.<br>For example:<br>$\sin x=O(x)\quad (x\to 0)$. |
| <span id="n8.13">n8.13</span> | $f(x) = o(g(x))$ | $f(x)/g(x)\to 0$ within the limits implied by the context, the order of $f(x)$ is higher than that of $g(x)$ | The symbol "$=$" is used for historical reasons; here it does not denote equivalence, since it is not transitive.<br>For example:<br>$\cos x=1+o(x)\quad (x\to 0)$. |
| <span id="n8.14">n8.14</span> | $\Delta f$ | finite increment of $f$ | The difference of two function values implied by the context. For example:<br>$\Delta x=x_2-x_1$;<br>$\Delta f(x)=f(x_2)-f(x_1)$. |
| <span id="n8.15">n8.15</span> | $\dfrac{\mathrm{d}f}{\mathrm{d}x}$;<br>$f'$ | derivative of $f$ with respect to $x$ | Only for functions of one variable.<br>The independent variable may be stated explicitly, e.g. $\dfrac{\mathrm{d}f(x)}{\mathrm{d}x}$, $f'(x)$. |
| <span id="n8.16">n8.16</span> | $\left(\dfrac{\mathrm{d}f}{\mathrm{d}x}\right)_{x=a}$;<br>$f'(a)$ | value of the derivative of $f$ at $a$ | See [n8.15](#n8.15) |
| <span id="n8.17">n8.17</span> | $\dfrac{\mathrm{d}^n f}{\mathrm{d}x^n}$;<br>$f^{(n)}$ | $n$-th derivative of $f$ with respect to $x$ | Only for functions of one variable.<br>The independent variable may be stated explicitly, e.g. $\dfrac{\mathrm{d}^n f(x)}{\mathrm{d}x^n}$, $f^{(n)}(x)$.<br>$f''$ and $f'''$ may be used for $f^{(2)}$ and $f^{(3)}$ respectively. |
| <span id="n8.18">n8.18</span> | $\dfrac{\partial f}{\partial x}$;<br>$f_x$ | partial derivative of $f$ with respect to $x$ | Only for functions of several variables.<br>The independent variable may be stated explicitly, e.g. $\dfrac{\partial f(x, y, \dots)}{\partial x}$, $f_x(x, y, \dots)$.<br>Can be extended to higher orders, e.g. $f_{xx}=\dfrac{\partial^2 f}{\partial x^2}=\dfrac{\partial}{\partial x}\left(\dfrac{\partial f}{\partial x}\right)$;<br>$f_{xy}=\dfrac{\partial^2 f}{\partial y\partial x}=\dfrac{\partial}{\partial y}\left(\dfrac{\partial f}{\partial x}\right)$. |
| <span id="n8.19">n8.19</span> | $\dfrac{\partial(f_1, \dots, f_m)}{\partial(x_1, \dots, x_n)}$ | Jacobian matrix | *see*[^n8.19-ref1] |
| <span id="n8.20">n8.20</span> | $\mathrm{d}f$ | total differential of $f$ | $\mathrm{d}f(x, y, \dots)=\dfrac{\partial f}{\partial x}\mathrm{d}x+\dfrac{\partial f}{\partial y}\mathrm{d}y+\dots$. |
| <span id="n8.21">n8.21</span> | $\delta f$ | (infinitesimal) variation of $f$ | |
| <span id="n8.22">n8.22</span> | $\displaystyle \int f(x)\mathrm{d}x$ | indefinite integral of $f$ | |
| <span id="n8.23">n8.23</span> | $\displaystyle \int\limits_a^b f(x)\mathrm{d}x$ | definite integral of $f$ from $a$ to $b$ | $\displaystyle \int\nolimits_a^b f(x)\mathrm{d}x$ may also be used;<br>the definite integral can also be defined over more general domains. For example $\displaystyle\int\limits_C$, $\displaystyle\int\limits_S$, $\displaystyle\int\limits_V$, $\displaystyle\oint$ denote the definite integral over the curve $C$, the surface $S$, the three-dimensional region $V$, and over a closed curve or surface respectively.<br>Multiple integrals may be written $\displaystyle\iint$, $\displaystyle\iiint$ etc. |
| <span id="n8.24">n8.24</span> | $f*g$ | convolution of the functions $f$ and $g$ | $\displaystyle (f*g)(x)=\int\limits_{-\infty}^{\infty}f(y)g(x-y)\mathrm{d}y$. |

[^n8.19-ref1]: $\dfrac{\partial(f_1, \dots, f_m)}{\partial(x_1, \dots, x_n)}=\begin{pmatrix}\dfrac{\partial f_1}{\partial x_1}&\cdots&\dfrac{\partial f_1}{\partial x_n}\\\vdots&\ddots&\vdots\\\dfrac{\partial f_m}{\partial x_1}&\cdots&\dfrac{\partial f_m}{\partial x_n}\end{pmatrix}$; for the definition of a matrix see [n12.1](#n12.1)

## Exponential and logarithmic functions

$x$ may be a complex number.

| No. | Symbol, expression | Meaning, equivalent expressions | Remarks and examples |
| --- | --- | --- | --- |
| <span id="n9.1">n9.1</span> | $\mathrm{e}$ | base of natural logarithms | $\displaystyle \mathrm{e}=\lim\limits_{n\to\infty}\left(1+\frac{1}{n}\right)^n=2.718~281~8\dots$;<br>do not write $e$. |
| <span id="n9.2">n9.2</span> | $a^x$ | exponential function of $x$ (to the base $a$) | See [n6.9](#n6.9). |
| <span id="n9.3">n9.3</span> | $\mathrm{e}^x$;<br>$\exp x$ | exponential function of $x$ (to the base $\mathrm{e}$) | |
| <span id="n9.4">n9.4</span> | $\log_a x$ | logarithm of $x$ to the base $a$ | When the base does not need to be specified, $\log x$ may be used.<br>$\log x$ should not be used in place of any of $\ln x$, $\lg x$, $\operatorname{lb} x$. |
| <span id="n9.5">n9.5</span> | $\ln x$ | natural logarithm of $x$ | $\ln x = \log_{\mathrm{e}} x$;<br>see [n9.4](#n9.4). |
| <span id="n9.6">n9.6</span> | $\lg x$ | common logarithm of $x$ | $\lg x = \log_{10} x$;<br>see [n9.4](#n9.4). |
| <span id="n9.7">n9.7</span> | $\operatorname{lb} x$ | logarithm of $x$ to the base $2$ | $\operatorname{lb} x = \log_2 x$;<br>see [n9.4](#n9.4). |

## Trigonometric and hyperbolic functions

| No. | Symbol, expression | Meaning, equivalent expressions | Remarks and examples |
| --- | --- | --- | --- |
| <span id="n10.1">n10.1</span> | $\pi$ | ratio of the circumference of a circle to its diameter | $\pi = 3.141~592~6\dots$. |
| <span id="n10.2">n10.2</span> | $\sin x$ | sine of $x$ | $\sin x=\dfrac{\mathrm{e}^{\mathrm{i}x}-\mathrm{e}^{-\mathrm{i}x}}{2\mathrm{i}}$;<br>$(\sin x)^n$, $(\cos x)^n$($n\geq 2$) etc. are usually written $\sin^n x$, $\cos^n x$ etc. |
| <span id="n10.3">n10.3</span> | $\cos x$ | cosine of $x$ | $\cos x = \sin(x + \pi/2)$. |
| <span id="n10.4">n10.4</span> | $\tan x$ | tangent of $x$ | $\tan x = \sin x/\cos x$;<br>$\operatorname{tg} x$ must not be used. |
| <span id="n10.5">n10.5</span> | $\cot x$ | cotangent of $x$ | $\cot x = 1/\tan x$;<br>$\operatorname{ctg} x$ must not be used. |
| <span id="n10.6">n10.6</span> | $\sec x$ | secant of $x$ | $\sec x = 1/\cos x$. |
| <span id="n10.7">n10.7</span> | $\csc x$ | cosecant of $x$ | $\csc x = 1/\sin x$;<br>$\operatorname{cosec} x$ must not be used. |
| <span id="n10.8">n10.8</span> | $\arcsin x$ | arc sine of $x$ | $y = \arcsin x \iff x = \sin y\quad (-\pi/2 \leq y \leq \pi/2)$. |
| <span id="n10.9">n10.9</span> | $\arccos x$ | arc cosine of $x$ | $y = \arccos x \iff x = \cos y\quad (0 \leq y \leq \pi)$. |
| <span id="n10.10">n10.10</span> | $\arctan x$ | arc tangent of $x$ | $y = \arctan x \iff x = \tan y\quad (-\pi/2 \leq y \leq \pi/2)$;<br>$\operatorname{arctg} x$ must not be used. |
| <span id="n10.11">n10.11</span> | $\operatorname{arccot} x$ | arc cotangent of $x$ | $y = \operatorname{arccot} x \iff x = \cot y\quad (0 \leq y \leq \pi)$;<br>$\operatorname{arcctg} x$ must not be used. |
| <span id="n10.12">n10.12</span> | $\operatorname{arcsec} x$ | arc secant of $x$ | $y = \operatorname{arcsec} x \iff x = \sec y\quad (0\leq y \leq \pi, y\ne \pi/2)$. |
| <span id="n10.13">n10.13</span> | $\operatorname{arccsc} x$ | arc cosecant of $x$ | $y = \operatorname{arccsc} x \iff x = \csc y\quad (-\pi/2 \leq y \leq \pi/2, y\ne 0)$;<br>$\operatorname{arccosec} x$ must not be used. |
| <span id="n10.14">n10.14</span> | $\sinh x$ | hyperbolic sine of $x$ | $\sinh x=\dfrac{\mathrm{e}^x-\mathrm{e}^{-x}}{2}$;<br>$\operatorname{sh} x$ must not be used. |
| <span id="n10.15">n10.15</span> | $\cosh x$ | hyperbolic cosine of $x$ | $\cosh^2 x = \sinh^2 x + 1$;<br>$\operatorname{ch} x$ must not be used. |
| <span id="n10.16">n10.16</span> | $\tanh x$ | hyperbolic tangent of $x$ | $\tanh x = \sinh x/\cosh x$;<br>$\operatorname{th} x$ must not be used. |
| <span id="n10.17">n10.17</span> | $\coth x$ | hyperbolic cotangent of $x$ | $\coth x = 1/\tanh x$. |
| <span id="n10.18">n10.18</span> | $\operatorname{sech} x$ | hyperbolic secant of $x$ | $\operatorname{sech} x = 1/\cosh x$. |
| <span id="n10.19">n10.19</span> | $\operatorname{csch} x$ | hyperbolic cosecant of $x$ | $\operatorname{csch} x = 1/\sinh x$;<br>$\operatorname{cosech} x$ must not be used. |
| <span id="n10.20">n10.20</span> | $\operatorname{arsinh} x$ | inverse hyperbolic sine of $x$ | $y = \operatorname{arsinh} x \iff x = \sinh y$;<br>$\operatorname{arsh} x$ must not be used. |
| <span id="n10.21">n10.21</span> | $\operatorname{arcosh} x$ | inverse hyperbolic cosine of $x$ | $y = \operatorname{arcosh} x \iff x = \cosh y\quad (y \geq 0)$;<br>$\operatorname{arch} x$ must not be used. |
| <span id="n10.22">n10.22</span> | $\operatorname{artanh} x$ | inverse hyperbolic tangent of $x$ | $y = \operatorname{artanh} x \iff x = \tanh y$;<br>$\operatorname{arth} x$ must not be used. |
| <span id="n10.23">n10.23</span> | $\operatorname{arcoth} x$ | inverse hyperbolic cotangent of $x$ | $y = \operatorname{arcoth} x \iff x = \coth y\quad (y \ne 0)$. |
| <span id="n10.24">n10.24</span> | $\operatorname{arsech} x$ | inverse hyperbolic secant of $x$ | $y = \operatorname{arsech} x \iff x = \operatorname{sech} y\quad (y \geq 0)$. |
| <span id="n10.25">n10.25</span> | $\operatorname{arcsch} x$ | inverse hyperbolic cosecant of $x$ | $y = \operatorname{arcsch} x \iff x = \operatorname{csch} y\quad (y \geq 0)$;<br>$\operatorname{arcosech} x$ must not be used. |

## Complex numbers

| No. | Symbol, expression | Meaning, equivalent expressions | Remarks and examples |
| --- | --- | --- | --- |
| <span id="n11.1">n11.1</span> | $\mathrm{i}$ | imaginary unit | $\mathrm{i}^2 = -1$;<br>$i$ or `i` must not be used |
| <span id="n11.2">n11.2</span> | $\operatorname{Re} z$ | real part of $z$ | See [n11.3](#n11.3). |
| <span id="n11.3">n11.3</span> | $\operatorname{Im} z$ | imaginary part of $z$ | If $z = x + \mathrm{i} y\quad (x, y\in\mathbf{R})$, then $x = \operatorname{Re} z$, $y = \operatorname{Im} z$. |
| <span id="n11.4">n11.4</span> | $\lvert z\rvert$ | modulus of $z$ | $\lvert z\rvert=\sqrt{(\operatorname{Re} z)^2+(\operatorname{Im} z)^2}$. |
| <span id="n11.5">n11.5</span> | $\arg z$ | argument of $z$ | If $z = r \mathrm{e}^{\mathrm{i}\varphi}$, where $r = \lvert z\rvert$ and $-\pi < \varphi \leq \pi$, then $\varphi = \arg z$.<br>$\operatorname{Re} z = r \cos \varphi$, $\operatorname{Im} z = r \sin \varphi$. |
| <span id="n11.6">n11.6</span> | $\bar{z}$;<br>$z^*$ | complex conjugate of $z$ | $\bar{z}=\operatorname{Re}z-\mathrm{i}\operatorname{Im}z$. |
| <span id="n11.7">n11.7</span> | $\operatorname{sgn} z$ | unit modulus function of $z$ | $\operatorname{sgn} z =z / \lvert z\rvert = \exp(\mathrm{i} \arg z)\quad (z \ne 0)$;<br>$\operatorname{sgn} 0 = 0$;<br>see [n6.13](#n6.13). |

## Matrices

| No. | Symbol, expression | Meaning, equivalent expressions | Remarks and examples |
| --- | --- | --- | --- |
| <span id="n12.1">n12.1</span> | $A$;<br>*see*[^n12.1-ref1] | matrix $A$ of type $m\times n$ | $a_{ij} = (A)_{ij}$;<br>$A = (a_{ij})$ may also be used. Here $m$ is the number of rows and $n$ the number of columns<br>when $m=n$ the matrix is called square<br>square brackets may be used instead of parentheses. |
| <span id="n12.2">n12.2</span> | $A + B$ | sum of the matrices $A$ and $B$ | $(A + B)_{ij} = (A)_{ij} + (B)_{ij}$;<br>the matrices $A$ and $B$ must have the same number of rows and the same number of columns. |
| <span id="n12.3">n12.3</span> | $x A$ | product of the scalar $x$ and the matrix $A$ | $(x A)_{ij} = x (A)_{ij}$. |
| <span id="n12.4">n12.4</span> | $AB$ | product of the matrices $A$ and $B$ | $\displaystyle(AB)_{ik} = \sum\limits_{j}(A)_{ij}(B)_{jk}$;<br>the number of columns of the matrix $A$ must equal the number of rows of the matrix $B$. |
| <span id="n12.5">n12.5</span> | $I$;<br>$E$ | identity matrix | $(I)_{ik} = \delta_{ik}$;<br>for the definition of $\delta_{ik}$ see [n14.9](#n14.9). |
| <span id="n12.6">n12.6</span> | $A^{-1}$ | inverse of the square matrix $A$ | $AA^{-1} = A^{-1}A = I\quad (\det A \ne 0)$.<br>For the definition of $\det A$ see [n12.10](#n12.10). |
| <span id="n12.7">n12.7</span> | $A^{\mathrm{T}}$;<br>$A'$ | transpose of $A$ | $(A^{\mathrm{T}})_{ik} = (A)_{ki}$. |
| <span id="n12.8">n12.8</span> | $\overline{A}$;<br>$A^*$ | complex conjugate matrix of $A$ | $\left(\overline{A}\right)_{ik}=\overline{(A)_{ik}}$. |
| <span id="n12.9">n12.9</span> | $A^{\mathrm{H}}$;<br>$A^{\dagger}$ | Hermitian conjugate matrix of $A$ | $A^{\mathrm{H}} = \left(\overline{A}\right)^{\mathrm{T}}$. |
| <span id="n12.10">n12.10</span> | $\det A$;<br>*see*[^n12.10-ref1] | determinant of the square matrix $A$ | $\lvert A\rvert$ may also be used. |
| <span id="n12.11">n12.11</span> | $\operatorname{rank}A$ | rank of the matrix $A$ | |
| <span id="n12.12">n12.12</span> | $\operatorname{tr}A$ | trace of the square matrix $A$ | $\displaystyle\operatorname{tr}A=\sum\limits_{i}(A)_{ii}$. |
| <span id="n12.13">n12.13</span> | $\lVert A\rVert$ | norm of the matrix $A$ | Satisfies the triangle inequality: if $A + B = C$, then $\lVert A\rVert+\lVert B\rVert \geq \lVert C\rVert$. |

[^n12.1-ref1]: $\begin{pmatrix}a_{11}&\cdots&a_{1n}\\\vdots&\ddots&\vdots\\a_{m1}&\cdots&a_{mn}\end{pmatrix}$

[^n12.10-ref1]: $\begin{vmatrix}a_{11}&\cdots&a_{1n}\\\vdots& &\vdots\\a_{n1}&\cdots&a_{nn}\end{vmatrix}$

## Coordinate systems

This section considers some coordinate systems in three-dimensional space. The point $\mathrm{O}$ is the **origin** of the coordinate system. Any point $\mathrm{P}$ is determined by the **position vector** from the origin $\mathrm{O}$ to the point $\mathrm{P}$.

| No. | Coordinates | Position vector and its differential | Name of coordinates | Remarks |
| --- | --- | --- | --- | --- |
| <span id="n13.1">n13.1</span> | $x$, $y$, $z$ | $\boldsymbol{r} = x \boldsymbol{e}_x + y \boldsymbol{e}_y + z \boldsymbol{e}_z$;<br>$\mathrm{d}\boldsymbol{r} = \mathrm{d}x~\boldsymbol{e}_x + \mathrm{d}y~\boldsymbol{e}_y + \mathrm{d}z~\boldsymbol{e}_z$ | Cartesian coordinates | The base vectors $\boldsymbol{e}_x$, $\boldsymbol{e}_y$, $\boldsymbol{e}_z$ form a right-handed orthogonal system, see [Figure 1](#figure-1) and [Figure 4](#figure-4).<br>The base vectors may also be denoted by $\boldsymbol{e}_1$, $\boldsymbol{e}_2$, $\boldsymbol{e}_3$ or $\boldsymbol{i}$, $\boldsymbol{j}$, $\boldsymbol{k}$, and the coordinates by $x_1$, $x_2$, $x_3$ or $i$, $j$, $k$. |
| <span id="n13.2">n13.2</span> | $\rho$, $\varphi$, $z$ | $\boldsymbol{r} = \rho~\boldsymbol{e}_{\rho} + z~\boldsymbol{e}_z$;<br>$\mathrm{d}\boldsymbol{r} = \mathrm{d}\rho~\boldsymbol{e}_{\rho} +\rho~\mathrm{d}\varphi~\boldsymbol{e}_{\varphi} + \mathrm{d}z~\boldsymbol{e}_z$ | cylindrical coordinates | $\boldsymbol{e}_{\rho}(\varphi)$, $\boldsymbol{e}_{\varphi}(\varphi)$, $\boldsymbol{e}_z$ form a right-handed orthogonal system, see [Figure 2](#figure-2).<br>If $z = 0$, then $\rho$ and $\varphi$ are the polar coordinates in the plane. |
| <span id="n13.3">n13.3</span> | $r$, $\vartheta$, $\varphi$ | $\boldsymbol{r} = r \boldsymbol{e}_r$;<br>$\mathrm{d}\boldsymbol{r} = \mathrm{d}r~\boldsymbol{e}_r + r~\mathrm{d}\vartheta~\boldsymbol{e}_{\vartheta} + r~\sin\vartheta~\mathrm{\mathrm{d}}\varphi~\boldsymbol{e}_{\varphi}$ | spherical coordinates | $\boldsymbol{e}_r(\vartheta, \varphi)$, $\boldsymbol{e}_{\vartheta}(\vartheta, \varphi)$, $\boldsymbol{e}_{\varphi}(\varphi)$ form a right-handed orthogonal system, see [Figure 3](#figure-3). |

If a [left-handed coordinate system](#figure-5) is used instead of a [right-handed coordinate system](#figure-4), this should be stated clearly in advance to avoid misuse of symbols.

![](./images/symbol-1.svg)

<span id="figure-1">**Figure 1**</span> Right-handed Cartesian coordinate system

![](./images/symbol-2.svg)

<span id="figure-2">**Figure 2**</span> Right-handed cylindrical coordinate system

![](./images/symbol-3.svg)

<span id="figure-3">**Figure 3**</span> Right-handed spherical coordinate system

![](./images/symbol-4.svg)

<span id="figure-4">**Figure 4**</span> Right-handed coordinate system

![](./images/symbol-5.svg)

<span id="figure-5">**Figure 5**</span> Left-handed coordinate system

## Scalars and vectors

In this section the base vectors are denoted by $\boldsymbol{e}_1$, $\boldsymbol{e}_2$, $\boldsymbol{e}_3$. Many of the concepts in this section can be generalized to $n$-dimensional space.

Scalars and vectors themselves are independent of the choice of coordinate system, whereas each scalar component of a vector depends on the choice of coordinate system.

For the base vectors $\boldsymbol{e}_1$, $\boldsymbol{e}_2$, $\boldsymbol{e}_3$, every vector $\boldsymbol{a}$ can be written as $\boldsymbol{a}=a_1\boldsymbol{e}_1+a_2\boldsymbol{e}_2+a_3\boldsymbol{e}_3$, where $a_1$, $a_2$ and $a_3$ are uniquely determined scalar values, called the "coordinates" of the vector with respect to this set of base vectors, and $a_1\boldsymbol{e}_1$, $a_2\boldsymbol{e}_2$ and $a_3\boldsymbol{e}_3$ are called the component vectors with respect to this set of base vectors.

In this section only Cartesian (orthogonal) coordinates of ordinary space are considered. Cartesian coordinates are denoted by $x$, $y$, $z$ or $a_1$, $a_2$, $a_3$ or $x_1$, $x_2$, $x_3$.

All indices $i$, $j$, $k$ in this section range from $1$ to $3$.

| No. | Symbol, expression | Meaning, equivalent expressions | Remarks and examples |
| --- | --- | --- | --- |
| <span id="n14.1">n14.1</span> | $\boldsymbol{a}$;<br>$\vec{a}$ | vector $\boldsymbol{a}$ | |
| <span id="n14.2">n14.2</span> | $\boldsymbol{a} + \boldsymbol{b}$ | sum of the vectors $\boldsymbol{a}$ and $\boldsymbol{b}$ | $(\boldsymbol{a} + \boldsymbol{b})_i = a_i + b_i$. |
| <span id="n14.3">n14.3</span> | $x\boldsymbol{a}$ | product of the scalar $x$ and the vector $\boldsymbol{a}$ | $(x\boldsymbol{a})_i = xa_i$. |
| <span id="n14.4">n14.4</span> | $\lvert \boldsymbol{a}\rvert$ | magnitude of the vector $\boldsymbol{a}$, norm of the vector $\boldsymbol{a}$ | $\lvert \boldsymbol{a}\rvert=\sqrt{a_x^2+a_y^2+a_z^2}$;<br>$\lVert a\rVert$ may also be used. |
| <span id="n14.5">n14.5</span> | $\boldsymbol{0}$;<br>$\vec{0}$ | zero vector | The magnitude of the zero vector is $0$. |
| <span id="n14.6">n14.6</span> | $\boldsymbol{e_a}$ | unit vector in the direction of $\boldsymbol{a}$ | $\boldsymbol{e_a} = \boldsymbol{a}/\lvert\boldsymbol{a}\rvert\quad (\boldsymbol{a}\ne \boldsymbol{0})$. |
| <span id="n14.7">n14.7</span> | $\boldsymbol{e}_x$, $\boldsymbol{e}_y$, $\boldsymbol{e}_z$;<br>$\boldsymbol{e}_1$, $\boldsymbol{e}_2$, $\boldsymbol{e}_3$ | unit vectors in the directions of the Cartesian coordinate axes | $\boldsymbol{i}$, $\boldsymbol{j}$, $\boldsymbol{k}$ may also be used. |
| <span id="n14.8">n14.8</span> | $a_x$, $a_y$, $a_z$;<br>$a_i$ | Cartesian components of the vector $\boldsymbol{a}$ | $\boldsymbol{a} = a_x \boldsymbol{e}_x + a_y \boldsymbol{e}_y + a_z \boldsymbol{e}_z$;<br>if the base vectors are determined by the context, the vector may be written $\boldsymbol{a} = (a_x, a_y, a_z)$.<br>$a_x = \boldsymbol{a}\cdot \boldsymbol{e}_x$, $a_y = \boldsymbol{a}\cdot \boldsymbol{e}_y$, $a_z = \boldsymbol{a}\cdot \boldsymbol{e}_z$;<br>$\boldsymbol{r} = x\boldsymbol{e}_x + y\boldsymbol{e}_y + z\boldsymbol{e}_z$ is the position vector with coordinates $x$, $y$, $z$. |
| <span id="n14.9">n14.9</span> | $\delta_{ik}$ | Kronecker delta symbol | $\delta_{ik}=[i=k]$, where for the definition of $[\cdot]$ see [n6.24](#n6.24), i.e.:<br>$\delta_{ik}=1\quad (i=k)$;<br>$\delta_{ik}=0\quad (i\ne k)$. |
| <span id="n14.10">n14.10</span> | $\varepsilon_{ijk}$ | Levi-Civita symbol | $\varepsilon_{123} = \varepsilon_{231} = \varepsilon_{312} = 1$;<br>$\varepsilon_{132} = \varepsilon_{321} = \varepsilon_{213} = -1$;<br>all other $\varepsilon_{ijk}$ are $0$. |
| <span id="n14.11">n14.11</span> | $\boldsymbol{a}\cdot\boldsymbol{b}$ | scalar/inner product of the vectors $\boldsymbol{a}$ and $\boldsymbol{b}$ | $\displaystyle\boldsymbol{a}\cdot\boldsymbol{b}=\sum\limits_i a_ib_i$. |
| <span id="n14.12">n14.12</span> | $\boldsymbol{a}\times\boldsymbol{b}$ | vector/outer product of the vectors $\boldsymbol{a}$ and $\boldsymbol{b}$ | In a right-handed Cartesian coordinate system, $\displaystyle (\boldsymbol{a}\times\boldsymbol{b})_i = \sum\limits_j\sum\limits_k\varepsilon_{ijk}a_jb_k$;<br>for the definition of $\varepsilon_{ijk}$ see [n14.10](#n14.10). |
| <span id="n14.13">n14.13</span> | $\mathbf{\nabla}$ | nabla operator | $\displaystyle \mathbf{\nabla} = \boldsymbol{e}_x\frac{\partial}{\partial x}+\boldsymbol{e}_y\frac{\partial}{\partial y}+\boldsymbol{e}_z\frac{\partial}{\partial z}=\sum\limits_i\boldsymbol{e}_i\frac{\partial}{\partial x_i}$. |
| <span id="n14.14">n14.14</span> | $\mathbf{\nabla}\varphi$;<br>$\operatorname{\mathbf{grad}}\varphi$ | gradient of $\varphi$ | $\displaystyle \mathbf{\nabla}\varphi=\sum\limits_i\boldsymbol{e}_i\frac{\partial\varphi}{\partial x_i}$;<br>for $\operatorname{\mathbf{grad}}$ use `\operatorname{\mathbf{grad}}`. |
| <span id="n14.15">n14.15</span> | $\mathbf{\nabla}\cdot\boldsymbol{a}$;<br>$\operatorname{\mathbf{div}}\boldsymbol{a}$ | divergence of $\boldsymbol{a}$ | $\displaystyle \mathbf{\nabla}\cdot\boldsymbol{a}=\sum\limits_i\frac{\partial a_i}{\partial x_i}$;<br>for $\operatorname{\mathbf{div}}$ use `\operatorname{\mathbf{div}}`. |
| <span id="n14.16">n14.16</span> | $\mathbf{\nabla}\times\boldsymbol{a}$;<br>$\operatorname{\mathbf{rot}}\boldsymbol{a}$ | curl (rotation) of $\boldsymbol{a}$ | $\displaystyle (\mathbf{\nabla}\times\boldsymbol{a})_i=\sum\limits_j\sum\limits_k\varepsilon_{ijk}\frac{\partial a_k}{\partial x_j}$;<br>for $\operatorname{\mathbf{rot}}$ use `\operatorname{\mathbf{rot}}`.<br>$\operatorname{\mathbf{curl}}$ should not be used.<br>For the definition of $\varepsilon_{ijk}$ see [n14.10](#n14.10). |
| <span id="n14.17">n14.17</span> | $\mathbf{\nabla}^2$;<br>$\Delta$ | Laplace operator | $\mathbf{\nabla}^2=\dfrac{\partial^2}{\partial x^2}+\dfrac{\partial^2}{\partial y^2}+\dfrac{\partial^2}{\partial z^2}$. |

## Special functions

In this section $z$, $w$ are complex numbers, $k$, $n$ are natural numbers, and $k\leq n$.

| No. | Symbol, expression | Meaning, equivalent expressions | Remarks and examples |
| --- | --- | --- | --- |
| <span id="n15.1">n15.1</span> | $\gamma$ | Euler–Mascheroni constant | $\displaystyle \gamma=\lim\limits_{n\to\infty}\left(\sum\limits_{k=1}^n\frac{1}{k}-\ln n\right)= 0.577~215~6 \dots$. |
| <span id="n15.2">n15.2</span> | $\Gamma(z)$ | gamma function | $\displaystyle\Gamma(z)=\int\limits_0^{\infty}t^{z-1}\mathrm{e}^{-t}\mathrm{d}t\quad (\operatorname{Re}z>0)$;<br>$\Gamma(n+1)=n!$. |
| <span id="n15.3">n15.3</span> | $\zeta(z)$ | Riemann zeta function | $\displaystyle\zeta(z)=\sum\limits_{n=1}^{\infty}\frac{1}{n^z}\quad (\operatorname{Re}z>1)$. |
| <span id="n15.4">n15.4</span> | $\operatorname{B}(z, w)$ | beta function | $\displaystyle\operatorname{B}(z, w)=\int\limits_0^1 t^{z-1}(1-t)^{w-1}\mathrm{d}t\quad (\operatorname{Re} z>0$, $\operatorname{Re} w>0)$;<br>$\operatorname{B}(z, w)=\dfrac{\Gamma(z)\Gamma(w)}{\Gamma(z+w)}$;<br>$\dfrac{1}{(n+1)\operatorname{B}(k+1, n-k+1)}=\dbinom{n}{k}$. |
