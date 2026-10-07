---
title: String basics
---

## Definitions

### Alphabet

An **alphabet** (character set) $\Sigma$ is a set equipped with a [total order](../math/order-theory.md#偏序集), which means that any two distinct elements $\alpha$ and $\beta$ of $\Sigma$ can be compared: either $\alpha<\beta$ or $\beta<\alpha$. The elements of the alphabet $\Sigma$ are called characters.

### String

A **string** $S$ is a sequence formed by arranging $n\ (n\ge 0)$ characters in order; $n$ is called the length of $S$ and is denoted $|S|$. In particular, when $n=0$ the string $S$ contains no characters and is called the **empty string**, denoted $\varepsilon$.

If string indices start from $1$, the $i$-th character of $S$ is denoted $S[i]$;

if string indices start from $0$, the $i$-th character of $S$ is denoted $S[i-1]$.

### Substring

A **substring** of a string $S$, $S[i..j]，i≤j$, is the part of $S$ from position $i$ to position $j$, i.e. the string formed by $S[i],S[i+1],\ldots,S[j]$ in order.

Sometimes $S[i..j]$ with $i>j$ is used to denote the empty string $\varepsilon$.

### Subsequence

A **subsequence** of a string $S$ is a sequence obtained by extracting some elements from $S$ without changing their relative order, i.e. $S[p_1],S[p_2],\ldots,S[p_k]$, $1\le p_1< p_2<\cdots< p_k\le|S|$, $k\ge 0$.

### Suffix

A **suffix** is a special substring that starts at some position $i$ and ends at the end of the whole string. The suffix of $S$ starting at $i$ is denoted $\textit{Suffix(S,i)}$, i.e. $\textit{Suffix(S,i)}=S[i..|S|-1]$.

A **proper suffix** is any suffix of $S$ other than $S$ itself.

For example, all suffixes of the string `abcabcd` are `{ε, d, cd, bcd, abcd, cabcd, bcabcd, abcabcd}`, and its proper suffixes are `{ε, d, cd, bcd, abcd, cabcd, bcabcd}`.

### Prefix

A **prefix** is a special substring that starts at the beginning of the string and ends at some position $i$. The prefix of $S$ ending at $i$ is denoted $\textit{Prefix(S,i)}$, i.e. $\textit{Prefix(S,i)}=S[0..i]$.

A **proper prefix** is any prefix of $S$ other than $S$ itself.

For example, all prefixes of the string `abcabcd` are `{ε, a, ab, abc, abca, abcab, abcabc, abcabcd}`, and its proper prefixes are `{ε, a, ab, abc, abca, abcab, abcabc}`.

### Lexicographic order

Strings are compared using the $i$-th character as the $i$-th key; the empty character is smaller than any character of the alphabet (i.e. $a< aa$).

### Palindrome

A **palindrome** is a string that reads the same forwards and backwards, i.e. a string $s$ satisfying $\forall 1\le i\le|s|, s[i]=s[|s|+1-i]$.

### Hamming distance

The **Hamming distance** is a distance between two strings of equal length: the number of positions at which the corresponding characters of the two strings differ.

Informally, if we XOR the two strings, the number of $1$s in the result is the Hamming distance between them.

## Storing strings

-   Store the string in a `char` array, using the null character `\0` to mark the end of the string (C-style strings).
-   Use the [`string` class](../lang/csl/string.md) provided by the C++ standard library.
-   String constants can be written as string literals (strings enclosed in double quotes).
