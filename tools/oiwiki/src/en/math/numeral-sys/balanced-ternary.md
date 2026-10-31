---
title: Balanced ternary
---

## Definition

Balanced ternary is also called symmetric ternary. It is a generalized positional numeral system.

The digits of regular ternary are `0`, `1`, and `2`, while the digits of balanced ternary are `-1`, `0`, and `1`. Its base is also `3` (because there are three possible values). Since it is inconvenient to write `-1` as a digit, we will use the letter `Z` instead of `-1`.

## Explanation

Here are a few examples:

| decimal | balanced ternary | decimal | balanced ternary |
| --- | ----- | --- | ----- |
| `0` | `0`   | `5` | `1ZZ` |
| `1` | `1`   | `6` | `1Z0` |
| `2` | `1Z`  | `7` | `1Z1` |
| `3` | `10`  | `8` | `10Z` |
| `4` | `11`  | `9` | `100` |

Negative numbers are very easy to represent in this numeral system: simply invert the digits of the positive number (`Z` becomes `1`, `1` becomes `Z`).

| decimal | balanced ternary |
| ---- | ----- |
| `-1` | `Z`   |
| `-2` | `Z1`  |
| `-3` | `Z0`  |
| `-4` | `ZZ`  |
| `-5` | `Z11` |

It is easy to see that the most significant digit of a negative number is `Z`, and that of a positive number is `1`.

## Procedure

In the conversion to balanced ternary, we first need to write the given number `x` in standard ternary. When `x` is written in standard ternary, each of its digits is `0`, `1`, or `2`. Iterating from the lowest digit, we can skip any `0` and `1`, but if we encounter a `2` we should first turn it into `Z` and add `1` to the next digit. If we encounter the digit `3`, it should be converted to `0` and `1` added to the next digit.

### Example 1

Convert `64` to balanced ternary.

First, we rewrite this number in standard ternary:

$$
\text 64_{10} = 02101_3
$$

Let us start from the digit that affects the whole number the least (the lowest digit):

-   `101` is skipped (because `0` and `1` are allowed in balanced ternary);
-   `2` becomes `Z`, and `1` is added to the digit to its left, giving `1Z101`;
-   `1` is skipped, giving `1Z101`.

The final result is `1Z101`.

Let us convert it back to decimal:

$$
\texttt {1Z101}=81 \times 1 +27 \times (-1) + 9 \times 1 + 3 \times 0 + 1 \times 1 = 64_{10}
$$

### Example 2

Convert `237` to balanced ternary.

First, we rewrite this number in standard ternary:

$$
\text 237_{10} = 22210_3
$$

-   `0` and `1` are skipped (because `0` and `1` are allowed in balanced ternary);
-   `2` becomes `Z`, and `1` is added to the digit to the left, giving `23Z10`;
-   `3` becomes `0`, and `1` is added to the digit to the left, giving `30Z10`;
-   `3` becomes `0`, and `1` is added to the digit to the left (`0` by default), giving `100Z10`;
-   `1` is skipped, giving `100Z10`.

The final result is `100Z10`.

Let us convert it back to decimal:

$$
\texttt{100Z10} = 243 \cdot 1 + 81 \cdot 0 + 27 \cdot 0 + 9 \cdot (-1) + 3 \cdot 1 + 1 \cdot 0 = 237_{10}
$$

## Properties

For a balanced ternary number $X_3$, we can multiply each digit $x_i$ by the corresponding weight $3^i$ to uniquely obtain a decimal number $Y_{10}$.

Then, does a decimal number $Y_{10}$ **uniquely correspond to one balanced ternary number**?

The answer is yes; this property is called the uniqueness of balanced ternary.

???+ note "Proof"
    We prove it by **contradiction**:
    
    Suppose that for a decimal number $Y_{10}$ there exist two **different balanced ternary numbers** $A_3,B_3$ that equal $Y_{10}$ when converted to decimal; we want to prove $A_3 = B_3$. We consider cases:
    
    1.  When $Y_{10}=0$, obviously $A_3 = B_3 = 0_3$, which contradicts the assumption.
    2.  When $Y_{10}>0$:
    
        -   Number the digits of $A_3$ and $B_3$ from the lowest to the highest; let $a_i$ be the $i$-th digit of $A_3$ and $b_i$ the $i$-th digit of $B$. In $A_3,B_3$ there must exist an $i$ such that $a_i\neq b_i$. We can see that the digits $i-1,i-2,\dots,0$ are irrelevant to the proof. Therefore, we shift $A_3,B_3$ right by $i$ digits to obtain $A_3',B_3'$; the original problem is equivalent to proving $A_3'=B_3'$.
        -   For the $0$-th digit of $A_3',B_3'$, $a_0 \neq b_0$. Suppose $b_0 > a_0$ (the result is the same when $a_0>b_0$); it is easy to see that $b_0 - a_0 \in \{1,2\}$. The contribution of the digits $i=1,2,3,\dots$ of $A_3'$ to the value of $A_3'$ is $S_1 = a_1 \times 3^1 + a_2 \times 3^2+ \dots$, and the contribution of the digits $i=1,2,3,\dots$ of $B_3'$ to the value of $B_3'$ is $S_2 = b_1 \times 3^1 + b_2 \times 3^2 + \dots$. Since $A_3' = B_3'$, we get $S_1 - S_2 = b_0 - a_0$. $S_1,S_2$ have the common factor $3$, while $b_0 - a_0$ is not divisible by $3$, which contradicts the assumption; therefore $A_3'\neq B_3'$
    3.  When $Y_{10}<0$, the proof is the same as for $Y_{10}>0$.
    
    Hence, for any decimal number $Y_{10}$ there is a unique corresponding balanced ternary number $X_3$.

## Exercises

[Topcoder SRM 604 PowerOfThree](https://archive.topcoder.com/ProblemStatement/pm/12917)

**This page is partly translated from the article [Троичная сбалансированная система счисления](http://e-maxx.ru/algo/balanced_ternary) and its English translation [Balanced Ternary](https://cp-algorithms.com/algebra/balanced-ternary.html). The Russian version is licensed under Public Domain + Leave a Link; the English version under CC-BY-SA 4.0.**
