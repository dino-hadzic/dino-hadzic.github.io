---
title: Optimal in-place suffix sorting algorithm
---

This chapter introduces an in-place suffix sorting algorithm with linear time complexity[^in-place-sa-sort] (Optimal In-Place Suffix Sorting).

???+ warning "Warning"
    This chapter is **only recommended** if you are **very, very familiar** with SA-IS[^nzc09a][^sa-is-intro].

## Global setup

The target string is $\texttt{Pat}$, the suffix array is $\texttt{SA}$, string indices start at 0, and the last character is a sentinel, which we may assume to be 0.

## Suffix sorting over an integer alphabet

In fact, this part can be viewed as an in-place version of the SA-IS algorithm.

Since it is the algorithm whose details are described most clearly in the original paper and whose implementation is relatively simple, and since it is also the basis for understanding the subsequent algorithms, it is the focus of this article.

The principle of the in-place approach is to use the renamed $\texttt{Pat}$ in place of the S and L buckets, and to replace the type bucket with an extra $O(n)$ operations.

### Renaming the target string Pat

Simply put, we rename $\texttt{Pat}$ without changing the relative order of the suffixes, and use the renamed $\texttt{Pat}$ in place of the original S and L buckets to indicate the bucket head or the bucket tail.

The renaming replaces every S-type character in $\texttt{Pat}$ with the tail index of its bucket, and every L-type character with the head index of its bucket.

As shown in the following figure:

$$
\begin{aligned}
\texttt{Index}:\qquad&\texttt{ 0   1   2   3   4   5   6   7   8   9  10  11  12} \\
\texttt{Pat}:\qquad&\texttt{ 2   1   1   3   3   1   1   3   3   1   2   1   0} \\
\texttt{Type}:\qquad&\texttt{ L   S   S   L   L   S   S   L   L   S   L   L   S} \\
\texttt{Bucket}:\qquad&\texttt{(0)}\texttt{ }\texttt{(1}\texttt{ }\texttt{ }\texttt{ 1 }\texttt{ }\texttt{ 1 }\texttt{ }\texttt{ 1 }\texttt{ }\texttt{ 1 }\texttt{ }
\texttt{ 1) }\texttt{(2 }\texttt{ }\texttt{ 2) }\texttt{(3}\texttt{ }\texttt{ }\texttt{ 3 }\texttt{ }\texttt{ 3 }\texttt{ }\texttt{ 3)}
\end{aligned}
$$

The renamed $\texttt{Pat'}$ (from now on we simply call the renamed $\texttt{Pat'}$ $\texttt{Pat}$):

$$
\begin{aligned}
\texttt{Index}:\qquad&\texttt{ 0   1   2   3   4   5   6   7   8   9  10  11  12} \\
\texttt{Pat'}:\qquad&\texttt{ 7   6   6   9   9   6   6   9   9   6   7   1   0}
\end{aligned}
$$

Since, within a bucket, the suffixes of L-type characters are smaller and go to the bucket head, while the suffixes of S-type characters are larger and go to the bucket tail, the relative order of the suffixes is preserved.

Let us describe the concrete steps of the renaming:

1.  As in SA-IS, count every character in $\texttt{Pat}$ and compute the prefix sums (counting sort) to build the S/L buckets, except that here the prefix sums are stored in $\texttt{SA}$;
2.  Scan every character of $\texttt{Pat}$ from tail to head; this way we only need to remember the type of the previous character to determine the type of every character on the fly, and then rename it according to the prefix sums.

### Sorting the LMS characters

The key point here is the use of an internal counter trick.

#### Initialization

Initially, every entry of $\texttt{SA}$ is set to E (EMPTY).

Scan $\texttt{Pat}$ from tail to head; if an LMS character $\texttt{Pat[i]}$ is found, set the mark of $\texttt{SA[Pat[i]]}$:

if $\texttt{SA[Pat[i]]}$ is E, set it to U (UNIQUE);

if $\texttt{SA[Pat[i]]}$ is U, set it to M (MULTIPLE);

otherwise, do nothing.

The result is shown in the following figure:

$$
\begin{aligned}
\texttt{Index}:\qquad&\texttt{ 0   1   2   3   4   5   6   7   8   9  10  11  12} \\
\texttt{Pat}:\qquad&\texttt{ 7   6   6   9   9   6   6   9   9   6   7   1   0} \\
\texttt{LMS}:\qquad&\texttt{ }\texttt{ }\texttt{ }\texttt{ }\texttt{ ∗ }\texttt{ }\texttt{ }\texttt{ }\texttt{ }\texttt{ }\texttt{ }\texttt{ }\texttt{ }\texttt{ }\texttt{ }\texttt{ }\texttt{ }\texttt{ }\texttt{ * }\texttt{ }\texttt{ }\texttt{ }\texttt{ }\texttt{ }\texttt{ }\texttt{ }\texttt{ }\texttt{ }\texttt{ }\texttt{ }\texttt{ }\texttt{ }\texttt{ * }\texttt{ }\texttt{ }\texttt{ }\texttt{ }\texttt{ }\texttt{ }\texttt{ }\texttt{ }\texttt{ }\texttt{ * } \\
\texttt{SA}:\qquad&\texttt{(}\underline{\color{red}{\texttt{U}}}\texttt{) }\texttt{(E)}\texttt{ }\texttt{(E }\texttt{ }\texttt{ E }\texttt{ }\texttt{ E }\texttt{ }\texttt{ E }\texttt{ }\texttt{ }\underline{\color{red}{\texttt{M}}}\texttt{) }\texttt{(E }\texttt{ }\texttt{ E) }\texttt{(E}\texttt{ }\texttt{ }\texttt{ E }\texttt{ }\texttt{ E }\texttt{ }\texttt{ E)}
\end{aligned}
$$

#### Putting the indices of the LMS characters into SA

Scan $\texttt{Pat}$ from tail to head, and for an LMS character $\texttt{Pat[i]}$ distinguish cases according to the mark in $\texttt{SA[Pat[i]]}$:

U: simply set $\texttt{SA[Pat[i]] = i}$

M: this means the bucket contains at least two LMS characters.

1.  If the bucket contains at least three LMS characters:
    use the second-to-last position of the bucket as a temporary counter recording the number of LMS characters already filled into the bucket (the last position of the bucket is the mark M);
    insert new LMS characters starting from the third-to-last position and increment the temporary counter by 1;
    if the bucket turns out to be full, shift all elements of the bucket from the head to the third-to-last position 2 places to the right, then insert the new element at the second position of the bucket (the first position of the bucket is filled with E).

2.  If the bucket contains exactly 2 LMS characters, obviously no counter is needed; just insert them in order from right to left.

A normal value:

    according to our earlier discussion, whether the bucket has two or more than two LMS characters, this means that $\texttt{i}$ is the position of the last LMS character to be inserted into the bucket,

    so we only need to scan leftwards from the bucket head, find the first position marked E, and set it to $\texttt{i}$.

Finally, scan $\texttt{SA}$ once more from tail to head and clear any remaining special marks M (the bucket was not filled up, so M and the counter were not overwritten).

This is done by shifting the LMS characters in the bucket 2 places to the right, as in the step above, and filling the freed positions on the left with E.

As shown in the following figure:

$$
\begin{aligned}
\texttt{Index}:\qquad&\texttt{ }\texttt{ 0   1   2   3   4   5   6   7   8   9  10  11  12} \\
\texttt{Pat}:\qquad&\texttt{ }\texttt{ 7   6   6   9   9   6   6   9   9   6   7   1   0} \\
\texttt{SA}:\qquad&\texttt{(}\underline{\color{red}{\texttt{12}}}\texttt{)}\texttt{ (E)}\texttt{ (E }\texttt{ }\texttt{ E }\texttt{ }\texttt{ E }\texttt{ }\texttt{ E }\texttt{ }\texttt{ M}\texttt{) }\texttt{(E }\texttt{ }
\texttt{ E) }\texttt{(E}\texttt{ }\texttt{ }\texttt{ E }\texttt{ }\texttt{ E }\texttt{ }\texttt{ E)}\\
\texttt{SA}:\qquad&\texttt{(12) }\texttt{(E)}\texttt{ (E }\texttt{ }\texttt{ E }\texttt{ }
\texttt{ }\underline{\color{red}{\texttt{9}}}\texttt{ }\texttt{ }{\color{red}{\texttt{ 1 }}}\texttt{ }\texttt{ }
{\color{red}{\texttt{M}}}\texttt{) }\texttt{(E }\texttt{ }\texttt{ E) }\texttt{(E}\texttt{ }\texttt{ }\texttt{ E }
\texttt{ }\texttt{ E }\texttt{ }\texttt{ E)} \\
\texttt{SA}:\qquad&\texttt{(12) }\texttt{(E)}\texttt{ (E }\texttt{ }\texttt{ }{\underline{\color{red}{\texttt{5}}}}
\texttt{ }\texttt{ }\texttt{ }{\texttt{9}}\texttt{ }\texttt{ }{\color{red}{\texttt{ 2 }}}\texttt{ }\texttt{ }
{\color{red}{\texttt{M}}}\texttt{) }\texttt{(E }\texttt{ }\texttt{ E) }\texttt{(E}\texttt{ }\texttt{ }\texttt{ E }
\texttt{ }\texttt{ E }\texttt{ }\texttt{ E)}\\
\texttt{SA}:\qquad&\texttt{(12) }\texttt{(E)}\texttt{ (}\underline{\color{red}{\texttt{1}}}\texttt{ }\texttt{ }{\texttt{ 5}}\texttt{ }\texttt{ }\texttt{ }{\texttt{9}}\texttt{ }\texttt{ }{\color{red}{\texttt{ 3 }}}\texttt{ }\texttt{ }{\color{red}{\texttt{M}}}\texttt{) }\texttt{(E }\texttt{ }\texttt{ E) }\texttt{(E}\texttt{ }\texttt{ }\texttt{ E }\texttt{ }\texttt{ E }\texttt{ }\texttt{ E)}\\
\texttt{SA}:\qquad&\texttt{(12) }\texttt{(E)}\texttt{ (}\texttt{E }\texttt{ }\texttt{ E }\texttt{ }{\color{red}{\texttt{ 1 }}\texttt{ }{\texttt{ 5 }}\texttt{ }\texttt{ }{\texttt{9}}}\texttt{) }\texttt{(E }\texttt{ }\texttt{ E) }\texttt{(E}\texttt{ }\texttt{ }\texttt{ E }\texttt{ }\texttt{ E }\texttt{ }\texttt{ E)}
\end{aligned}
$$

In this phase, since every bucket only needs to be shifted and scanned once, the time complexity is $O(n)$.

### Induced sorting of the LMS substrings

#### Induced sorting of the LMS prefixes

The LMS prefixes are sorted by induced sorting; as in SA-IS, this part is exactly the same as the later induced sorting of the suffixes (the same function is used), so we skip it here.

We directly give the sorting result here:

$$
\begin{aligned}
\texttt{Index}:\qquad&\texttt{ }\texttt{ 0   1   2   3   4   5   6   7   8   9  10  11  12} \\
\texttt{SA}:\qquad&\texttt{(}\texttt{12}\texttt{)}\texttt{(11)}\texttt{ (1 }\texttt{ }\texttt{ 5 }\texttt{ }\texttt{ 9 }\texttt{ }\texttt{ 2 }\texttt{ }\texttt{ 6}\texttt{) }\texttt{(10 }\texttt{ }\texttt{ 0) }\texttt{(4}\texttt{ }\texttt{ }\texttt{ 8 }\texttt{ }\texttt{ 3 }\texttt{ }\texttt{ 7)}
\end{aligned}
$$

#### Moving the sorted LMS substrings to the tail of SA

$$
\begin{aligned}
\texttt{Index}:\qquad&\texttt{ 0   1   2   3   4   5   6   7   8   9  10  11  12} \\
\texttt{SA}:\qquad&\texttt{ }\texttt{E }\texttt{ }\texttt{ E }\texttt{ }\texttt{ E }\texttt{ }\texttt{ E }\texttt{ }\texttt{ E }\texttt{ }\texttt{ E }\texttt{ }\texttt{ E }\texttt{ }\texttt{ E }\texttt{ }\texttt{ E }\texttt{ }{\underline{\color{red}{\texttt{12}}}}\texttt{ }\texttt{ }\texttt{ }{\underline{\color{red}{\texttt{1}}}}\texttt{ }\texttt{ }\texttt{ }{\underline{\color{red}{\texttt{5}}}}\texttt{ }\texttt{ }\texttt{ }{\underline{\color{red}{\texttt{9}}}}
\end{aligned}
$$

### Building the reduced sub-target string Pat1

Scan the LMS substrings at the tail of $\texttt{SA}$ from left to right, determine their order ("renaming"), and store the renamed value of $\texttt{SA[i]}$ in $\texttt{SA}\left[\left\lfloor\frac{\texttt{SA}[i]}{2} \right\rfloor\right]$.

Since LMS characters are never adjacent, there are no conflicts; this places the renamed values in the original order of the substrings they represent in $\texttt{Pat}$:

$$
\begin{aligned}
\texttt{Index}:\qquad&\texttt{ 0   1   2   3   4   5   6   7   8   9  10  11  12} \\
\texttt{SA}:\qquad&\texttt{ }\underline{\color{red}{\texttt{1}}}\texttt{ }\texttt{ }\texttt{ E }\texttt{ }\texttt{ }\underline{\color{red}{\texttt{1}}}\texttt{ }\texttt{ }\texttt{ E }\texttt{ }\texttt{ }\underline{\color{red}{\texttt{2}}}\texttt{ }\texttt{ }\texttt{ E }\texttt{ }\texttt{ }\underline{\color{red}{\texttt{0}}}\texttt{ }\texttt{ }\texttt{ E }\texttt{ }\texttt{ E }\texttt{ 12 }\texttt{ }\texttt{ 1 }\texttt{ }\texttt{ 5 }\texttt{ }\texttt{ 9 }
\end{aligned}
$$

Then scan $\texttt{SA}$ and collect these renamed values at the head of $\texttt{SA}$:

$$
\begin{aligned}
\texttt{Index}:\qquad&\texttt{ 0   1   2   3   4   5   6   7   8   9  10  11  12} \\
\texttt{SA}:\qquad&\texttt{ }\underline{\color{red}{\texttt{1}}}\texttt{ }\texttt{ }\texttt{ }\underline{\color{red}{\texttt{1}}}\texttt{ }\texttt{ }\texttt{ }\underline{\color{red}{\texttt{2}}}\texttt{ }\texttt{ }\texttt{ }\underline{\color{red}{\texttt{0}}}\texttt{ }\texttt{ }\texttt{ E }\texttt{ }\texttt{ E }\texttt{ }\texttt{ E }\texttt{ }\texttt{ E }\texttt{ }\texttt{ E }\texttt{ 12 }\texttt{ }\texttt{ 1 }\texttt{ }\texttt{ 5 }\texttt{ }\texttt{ 9 }
\end{aligned}
$$

### Solving Pat1 recursively and completing the sorting of the LMS suffixes

As in SA-IS, recursively solve the suffix sorting of the reduced $\texttt{Pat1}$ at the head of $\texttt{SA}$ and store the result at the tail of $\texttt{SA}$:

$$
\begin{aligned}
\texttt{Index}:\qquad&\texttt{ 0   1   2   3   4   5   6   7   8   9  10  11  12} \\
\texttt{SA}:\qquad&\texttt{ }\texttt{1 }\texttt{ }\texttt{ 1 }\texttt{ }\texttt{ 2 }\texttt{ }\texttt{ 0 }\texttt{ }\texttt{ E }\texttt{ }\texttt{ E }\texttt{ }\texttt{ E }\texttt{ }\texttt{ E }\texttt{ }\texttt{ E }\texttt{ }\texttt{ }{\underline{\color{red}{\texttt{3}}}}\texttt{ }\texttt{ }\texttt{ }{\underline{\color{red}{\texttt{0}}}}\texttt{ }\texttt{ }\texttt{ }{\underline{\color{red}{\texttt{1}}}}\texttt{ }\texttt{ }\texttt{ }{\underline{\color{red}{\texttt{2}}}}
\end{aligned}
$$

Move $\texttt{SA1}$ from the tail of $\texttt{SA}$ to the head of $\texttt{SA}$, scan $\texttt{Pat}$ again from tail to head, and put its LMS characters, in the order they appear in $\texttt{Pat}$, at the tail of $\texttt{SA}$:

$$
\begin{aligned}
\texttt{Index}:\qquad&\texttt{ 0   1   2   3   4   5   6   7   8   9  10  11  12} \\
\texttt{SA}:\qquad&\texttt{ }{\underline{\color{red}{\texttt{3}}}}\texttt{ }\texttt{ }\texttt{ }{\underline{\color{red}{\texttt{0}}}}\texttt{ }\texttt{ }\texttt{ }{\underline{\color{red}{\texttt{1}}}}\texttt{ }\texttt{ }\texttt{ }{\underline{\color{red}{\texttt{2}}}}\texttt{ }\texttt{ }\texttt{ E }\texttt{ }\texttt{ E }\texttt{ }\texttt{ E }\texttt{ }\texttt{ E }\texttt{ }\texttt{ E }\texttt{ }\texttt{ }{\underline{\color{red}{\texttt{1}}}}\texttt{ }\texttt{ }\texttt{ }{\underline{\color{red}{\texttt{5}}}}\texttt{ }\texttt{ }\texttt{ }{\underline{\color{red}{\texttt{9}}}}\texttt{ }\texttt{ }{\underline{\color{red}{\texttt{12}}}}
\end{aligned}
$$

Using the "lookup table" at the tail of $\texttt{SA}$, convert the $\texttt{SA1}$ values at the head of $\texttt{SA}$ back into the indices of the corresponding LMS suffixes in $\texttt{Pat}$:

$$
\begin{aligned}
\texttt{Index}:\qquad&\texttt{ 0   1   2   3   4   5   6   7   8   9  10  11  12} \\
\texttt{SA}:\qquad&{\underline{\color{red}{\texttt{12}}}}\texttt{ }\texttt{ }\texttt{ }{\underline{\color{red}{\texttt{1}}}}\texttt{ }\texttt{ }\texttt{ }{\underline{\color{red}{\texttt{5}}}}\texttt{ }\texttt{ }\texttt{ }{\underline{\color{red}{\texttt{9}}}}\texttt{ }\texttt{ }\texttt{ E }\texttt{ }\texttt{ E }\texttt{ }\texttt{ E }\texttt{ }\texttt{ E }\texttt{ }\texttt{ E }\texttt{ }\texttt{ 1 }\texttt{ }\texttt{ 5 }\texttt{ }\texttt{ 9 }\texttt{ 12 }
\end{aligned}
$$

Put the sorted LMS suffixes at the head of $\texttt{SA}$ into their corresponding buckets in order (filling from the tail):

$$
\begin{aligned}
\texttt{Index}:\qquad&\texttt{ }\texttt{ 0   1   2   3   4   5   6   7   8   9  10  11  12} \\
\texttt{SA}:\qquad&\texttt{(}{\underline{\color{red}{\texttt{12}}}}\texttt{)}\texttt{ }\texttt{(E)}\texttt{ (}\texttt{E }\texttt{ }\texttt{ E }\texttt{ }\texttt{ }{\underline{\color{red}{\texttt{1}}}}\texttt{ }\texttt{ }\texttt{ }{\underline{\color{red}{\texttt{5}}}}\texttt{ }\texttt{ }\texttt{ }{\underline{\color{red}{\texttt{9}}}}\texttt{)}\texttt{ }\texttt{(E }\texttt{ }\texttt{ E) }\texttt{(E}\texttt{ }\texttt{ }\texttt{ E }\texttt{ }\texttt{ E }\texttt{ }\texttt{ E)}
\end{aligned}
$$

### Induced sorting of all suffixes in Pat1

This part uses the internal counter trick from before to perform the in-place version of induced sorting.

Suppose we already have the sorted LMS suffixes (at the bucket tails) and use them to induce the L-type suffixes[^induction-order]:

$$
\begin{aligned}
\texttt{Index}:\qquad&\texttt{ }\texttt{ 0   1   2   3   4   5   6   7   8   9  10  11  12} \\
\texttt{Pat}:\qquad&\texttt{ }\texttt{ 7   6   6   9   9   6   6   9   9   6   7   1   0} \\
\texttt{SA}:\qquad&\texttt{(12) }\texttt{(E)}\texttt{ (}\texttt{E }\texttt{ }\texttt{ E }\texttt{ }{\texttt{ 1 }\texttt{ }{\texttt{ 5 }}\texttt{ }\texttt{ }{\texttt{9}}}\texttt{) }\texttt{(E }\texttt{ }\texttt{ E) }\texttt{(E}\texttt{ }\texttt{ }\texttt{ E }\texttt{ }\texttt{ E }\texttt{ }\texttt{ E)}
\end{aligned}
$$

As when sorting the LMS characters, first count the L-type characters with special marks:

$$
\begin{aligned}
\texttt{Index}:\qquad&\texttt{ }\texttt{ 0   1   2   3   4   5   6   7   8   9  10  11  12} \\
\texttt{Pat}:\qquad&\texttt{ }\texttt{ 7   6   6   9   9   6   6   9   9   6   7   1   0} \\
\texttt{SA}:\qquad&\texttt{(}{{\texttt{12}}}\texttt{)}\texttt{ }\texttt{(}{\underline{\color{red}{\texttt{U}}}}\texttt{)}\texttt{ }\texttt{(E }\texttt{ }\texttt{ E }\texttt{ }\texttt{ 1 }\texttt{ }\texttt{ 5 }\texttt{ }{\texttt{ 9}}\texttt{) }\texttt{(}{\underline{\color{red}{\texttt{M}}}}\texttt{ }\texttt{ }\texttt{ E) }\texttt{(}{\underline{\color{red}{\texttt{M}}}}\texttt{ }\texttt{ }\texttt{ E }\texttt{ }\texttt{ E }\texttt{ }\texttt{ E)}
\end{aligned}
$$

Scan SA from left to right, as when sorting the LMS characters; the slightly more complicated part is determining the type of $\texttt{suf[SA[i] - 1]}$, which requires a case analysis (see the code for details):

$$
\begin{aligned}
\texttt{Index}:\qquad&\texttt{ }\texttt{ 0   1   2   3   4   5   6   7   8   9  10  11  12} \\
\texttt{SA}:\qquad&\texttt{(}{\overrightarrow{\color{red}{\texttt{12}}}\texttt{)}\texttt{(}{\underline{\color{red}{\texttt{11}}}}}\texttt{)}\texttt{  (E   E   1   5   9) (M   E) (M   E   E   E)}\\
\texttt{SA}:\qquad&\texttt{(}\texttt{12}\texttt{)}\texttt{(}{\overrightarrow{\color{red}{\texttt{11}}}}\texttt{)}\texttt{  (E   E   1   5   9)}\texttt{(}{\underline{\color{red}{\texttt{10}}}}\texttt{ }\texttt{ }\texttt{ E)}\texttt{ (M   E   E   E)}\\
\texttt{SA}:\qquad&\texttt{(12)(11)}\texttt{  (E   E  }\texttt{ }\texttt{ } {\overrightarrow{\color{red}{\texttt{1}}}}\texttt{ }\texttt{  5   9)}\texttt{(10 }\texttt{ }\texttt{ }{\underline{\color{red}{\texttt{0}}}}\texttt{)}\texttt{ (M   E   E   E)}\\
\texttt{SA}:\qquad&\texttt{(12)(11)}\texttt{  (E   E   1 }\texttt{ }\texttt{ } {\overrightarrow{\color{red}{\texttt{5}}}}\texttt{ }\texttt{  9)}\texttt{(10   0)}\texttt{ (}{\color{red}{\texttt{M   1}}}\texttt{ }\texttt{ }\texttt{ }{\underline{\color{red}{\texttt{4}}}}\texttt{ }\texttt{ }\texttt{ E)}\\
\texttt{SA}:\qquad&\texttt{(12)(11)}\texttt{  (E   E   1   5}\texttt{ }\texttt{ } {\overrightarrow{\color{red}{\texttt{9}}}}\texttt{)}\texttt{(10   0)}\texttt{ (}{\color{red}{\texttt{M   2}}}\texttt{ }\texttt{ }\texttt{ 4 }\texttt{ }\texttt{ }{\underline{\color{red}{\texttt{8}}}}\texttt{)}\\
\texttt{SA}:\qquad&\texttt{(12)(11)}\texttt{  (E   E   1   5   9)(10   0)}\texttt{ (}{\overrightarrow{\color{red}{\texttt{4}}}}\texttt{ }\texttt{ 8 }\texttt{ }\texttt{ }{\underline{\color{red}{\texttt{3}}}}\texttt{ }\texttt{ }\texttt{ E}\texttt{)}\\
\texttt{SA}:\qquad&\texttt{(12)(11)}\texttt{  (E   E   1   5   9)(10   0)}\texttt{ (4 }\texttt{ }\texttt{ }{\overrightarrow{\color{red}{\texttt{8}}}}\texttt{ }\texttt{ 3 }\texttt{ }\texttt{ }{\underline{\color{red}{\texttt{7}}}}\texttt{)}
\end{aligned}
$$

Unlike SA-IS, after the induced sorting of one type of characters, the LMS characters must be cleaned up so that they do not interfere with the subsequent in-place induced sorting:

$$
\begin{aligned}
\texttt{Index}:\qquad&\texttt{ }\texttt{ 0   1   2   3   4   5   6   7   8   9  10  11  12} \\
\texttt{SA}:\qquad&\texttt{(12)(11)}\texttt{  (E   E  }\texttt{ }\texttt{ }{\underline{\color{red}{\texttt{E}}}}\texttt{ }\texttt{ }\texttt{ }{\underline{\color{red}{\texttt{E}}}}\texttt{ }\texttt{ }\texttt{ }{\underline{\color{red}{\texttt{E}}}}\texttt{)}\texttt{(10   0)}\texttt{ (4   8   3   7)}
\end{aligned}
$$

Inducing the S suffixes from the L suffixes is completely symmetric to inducing the L suffixes from the LMS suffixes, so we do not describe it separately here.

At this point, the induced sorting is complete.

#### Implementation

In terms of time there is no significant difference from SA-IS, while the memory usage drops to less than $\dfrac{1}{3}$ of the original (with 1 times more code), so the algorithm lives up to the title of the original paper, Optimal In-Place Suffix Sorting[^in-place-sa-sort].

??? note "Reference code"
    ```rust
    use std::cmp::max;
    use std::cmp::Ordering;
    use std::slice::from_raw_parts_mut;
    
    
    const LTYPE: bool = false;
    const STYPE: bool = true;
    const MAX_SA_VALUE: usize = usize::MAX / 2;
    const EMPTY: usize = MAX_SA_VALUE + 1;
    const UNIQUE: usize = MAX_SA_VALUE + 2;
    const MULTI: usize = MAX_SA_VALUE + 3;  // >= 258
    
    
    fn lms_str_cmp<E: Ord>(l1: &[E], l2: &[E]) -> Ordering {
        for (x, y) in l1.iter().zip(l2.iter()) {
            let cmp_res = x.cmp(&y);
            
            if cmp_res != Ordering::Equal { return cmp_res; }
        }
        
        Ordering::Equal
    }
    
    #[inline]
    fn pat_char_type(cur: usize, prev: usize, last_scanned_type: bool) -> bool {
        if cur < prev || cur == prev && last_scanned_type == STYPE { STYPE }
        else { LTYPE }
    }
    
    
    fn rename_pat(pat: &mut [usize], sa: &mut [usize]) {
        let patlastpos = pat.len() - 1;
        // set everything to bucket head
        //sa.fill(0);
        for i in 0..sa.len() { sa[i] = 0 }
        
        for i in 0..pat.len() { sa[pat[i]] += 1 }
        for i in 1..sa.len() { sa[i] += sa[i - 1] }
        
        for i in 0..pat.len() - 1 {
            pat[i] = sa[pat[i]] - 1;
        };
        // set L-suffixes to bucket head
        //sa.fill(0);
        for i in 0..sa.len() { sa[i] = 0 }
        
        for i in 0..pat.len() { sa[pat[i]] += 1 }
        let mut last_scanned_type = STYPE;
        pat[patlastpos] = 0;
        for i in (0..pat.len() - 1).rev() {
            if pat_char_type(pat[i], pat[i + 1], last_scanned_type) == STYPE {
                last_scanned_type = STYPE;
            } else {
                pat[i] -= sa[pat[i]] - 1;
                last_scanned_type = LTYPE;
            }
        }
    
    }
    
    
    fn sort_lms_char(pat: &mut [usize], sa: &mut [usize]) -> usize {
        //sa.fill(EMPTY);
        for i in 0..sa.len() { sa[i] = EMPTY }
        
        let mut last_scanned_type = STYPE;
        for i in (0..pat.len() - 1).rev() {
            if pat_char_type(pat[i], pat[i + 1], last_scanned_type) == STYPE {
                last_scanned_type = STYPE;
            } else {
                if last_scanned_type == STYPE {  // pat[i + 1] is LMS type
                    sa[pat[i + 1]] += 1;
                }
                
                last_scanned_type = LTYPE;
            }
        }
        
        let mut lms_cnt = 0;
        last_scanned_type = STYPE;
        for i in (0..pat.len() - 1).rev() {
            if pat_char_type(pat[i], pat[i + 1], last_scanned_type) == STYPE {
                last_scanned_type = STYPE;
            } else {
                let e_i = i + 1;
                let e = pat[e_i];
                
                if last_scanned_type == STYPE {  // pat[i + 1] is LMS type
                    lms_cnt += 1;
                    if sa[e] == UNIQUE {
                        sa[e] = e_i;
                    } else if sa[e] >= MULTI && sa[e - 1] == EMPTY {
                        if sa[e - 2] == EMPTY {
                            sa[e - 2] = e_i;
                            sa[e - 1] = 1;  // set counter
                        } else {  // MUL = 2
                            sa[e] = e_i;
                            sa[e - 1] = EMPTY;
                        }
                    } else if sa[e] >= MULTI && sa[e - 1] != EMPTY {
                        let c = sa[e - 1];  // get counter
                        
                        if sa[e - 2 - c] == EMPTY {
                            sa[e - 2 - c] = e_i;
                            sa[e - 1] += 1;  // update counter
                        } else {
                            for j in (1..c + 1).rev() {
                                sa[e - c + j] = sa[e - 2 - c + j]
                            }
                            sa[e - c] = e_i;
                            sa[e - c - 1] = EMPTY;
                        }
                    } else if sa[e] < EMPTY {
                        for j in (0..e).rev() {
                            if sa[j] == EMPTY {
                                sa[j] = e_i;
                                break;
                            }
                        }
                    }
                }
                
                last_scanned_type = LTYPE;
            }
        }
        
        for i in (0..pat.len()).rev() {
            if sa[i] >= MULTI {
                let c = sa[i - 1];
                for j in (1..c + 1).rev() {  // reverse order so earlier elements do not overwrite later ones
                    sa[i - c + j] = sa[i - 2 - c + j];
                }
                sa[i - c - 1] = EMPTY;
                sa[i - c] = EMPTY;
            }
        }
        
        lms_cnt
    }
    
    
    fn sort_lms_substr(pat: &mut [usize], sa: &mut [usize]) {
        // step 1
        induced_sort(pat, sa);
        
        // step 2
        let pat_last_pos = pat.len() - 1;
        let mut lms_cnt = 0;
        let mut i = pat_last_pos;
        let mut bucket_tail_ptr = pat_last_pos + 1;  // for renamed bucket ver
        let mut bucket = EMPTY;  // can be omitted, but makes the code easier to write
        let mut num = 0;  // S type number of bucket
        while i > 0 {
            if pat[sa[i]] != bucket {  // reach new bucket
                num = 0;
                
                let mut l = 0;
                while pat[sa[i - l]] == pat[sa[i]] {  // scan the bucket to count its S characters; by definition the loop must stop when l=i
                    let pat_i = sa[i - l];             // l < i, i.e. i - l > 0, 0 <= pat_i < patlen - 1
                    if pat[pat_i] < pat[pat_i + 1] {
                        let mut k = pat_i;
                        while k > 0 && pat[k - 1] == pat[pat_i] { k -= 1 }
                        num += pat_i - k + 1;
                    } else {
                        break;   // bucket has no S characters, stop scanning
                    }
                    
                    l += 1;
                }
                
                bucket_tail_ptr = i;
                bucket = pat[sa[bucket_tail_ptr]];
            }
            
            if num > 0
            && i > bucket_tail_ptr - num
            && sa[i] > 0
            && pat[sa[i]] < pat[sa[i] - 1]  {
                sa[pat_last_pos - lms_cnt] = sa[i];
                lms_cnt += 1;
            }
            
            i -= 1;
        }
        
        sa[pat_last_pos - lms_cnt ] = sa[i];  // i = 0
        lms_cnt += 1;
        //sa[0..pat_last_pos - lms_cnt + 1].fill(EMPTY);
        for i in 0..pat_last_pos - lms_cnt + 1 { sa[i] = EMPTY }
    }
    
    
    fn construct_pat1(pat: &mut [usize], sa: &mut [usize], lms_cnt: usize) -> bool {
        let patlen = pat.len();
        
        let mut prev_lms_str_len = 1;
        let mut rank = 0;
        sa[(patlen - 1) / 2] = rank;
        let mut has_duplicated_char = false;
        for i in patlen - lms_cnt + 1..patlen {  // start from the character after the sentinel
            let mut j = sa[i];
            while pat[j] <= pat[j + 1] { j += 1 } // find the first L character to the right of suf(sa[i]); since the sentinel LMS suffix is excluded, this cannot go out of bounds
            let mut k = j;
            while k + 1 < patlen && pat[k] >= pat[k + 1] { k += 1 }  // find the first LMS character to the right of suf(sa[i])
            let cur_lms_str_len = k + 1 - sa[i];
            let cmp_res = lms_str_cmp(&pat[sa[i]..sa[i] + cur_lms_str_len], &pat[sa[i - 1]..sa[i - 1] + prev_lms_str_len]);
            
            if  cmp_res != Ordering::Equal {
                rank += 1
            }
            
            if rank == sa[sa[i - 1] / 2] {
                has_duplicated_char = true;
            }
            let rank_index = sa[i] / 2;
            sa[rank_index] = rank;  // integer division
            
            prev_lms_str_len = cur_lms_str_len;
        }
        
        // move to head of sa
        let mut j = 0;
        for i in 0..patlen - lms_cnt {
            if sa[i] != EMPTY {
                sa[j] = sa[i];
                if i > j {
                    sa[i] = EMPTY;
                }
                j += 1;
            }
        }
        //sa[lms_cnt..patlen].fill(EMPTY);
        for i in lms_cnt..patlen { sa[i] = EMPTY }
        
        has_duplicated_char
    }
    
    fn sort_lms_suf(pat: &mut [usize], sa: &mut [usize], lms_cnt: usize, has_duplicated_char: bool) {
        // solve T1 recursively
        let patlen = pat.len();
        let salen = sa.len();
        unsafe {
            let sa_ptr = sa.as_mut_ptr();
            let mut pat1 = from_raw_parts_mut(sa_ptr, lms_cnt);
            let mut sa1 = from_raw_parts_mut(sa_ptr.offset((patlen - lms_cnt) as isize), salen - (patlen - lms_cnt));
            
            if has_duplicated_char {
                _compute_suffix_array_16_1(&mut pat1, &mut sa1);
            } else {
                for i in 0..lms_cnt { sa1[pat1[i]] = i }
            }
        }
        
        // move SA1 to SA[0...n1-1]
        for i in 0..lms_cnt {
            sa[i] = sa[patlen- lms_cnt + i];
        }
        
        // put all LMS-suffixes in SA tail
        let mut last_scanned_type = STYPE;
        let mut j = 0;
        for i in (0..pat.len() - 1).rev() {
            if pat[i] < pat[i + 1] || pat[i] == pat[i + 1] && last_scanned_type == STYPE {
                last_scanned_type = STYPE;
            } else {
                if last_scanned_type == STYPE {
                    sa[patlen - 1 - j] = i + 1;
                    j += 1;
                }
                
                last_scanned_type = LTYPE;
            }
        }
        
        // backward map the LMS-suffixes rank
        for i in 0..lms_cnt {
            let relative_rank = sa[i];
            sa[i] = sa[patlen - lms_cnt + relative_rank];
            sa[patlen - lms_cnt + relative_rank] = EMPTY;
        }
        
        let mut tail = EMPTY;
        let mut rfp = EMPTY;
        for i in (1..lms_cnt).rev() { // sa[0] stays in place
            if pat[sa[i]] != tail {
                tail = pat[sa[i]];
                rfp = tail;
            }
            
            sa[rfp] = sa[i];
            if rfp != i { sa[i] = EMPTY }
            rfp -= 1;
        }
    }
    
    // PASS!
    fn induced_sort(pat: &mut [usize], sa: &mut [usize]) {
        let patlen = pat.len();
        
        // place L-suff in SA
        // init
        let mut last_scanned_type = STYPE;
        for i in (0..patlen - 1).rev() {
            if pat_char_type(pat[i], pat[i + 1], last_scanned_type) == LTYPE {
                sa[pat[i]] += 1;  // >= EMPTY
                last_scanned_type = LTYPE;
            } else {
                last_scanned_type = STYPE;
            }
        }
        //place
        let mut i = 0;
        while i < patlen {
            if sa[i] < EMPTY && sa[i] > 0 {
                let j = sa[i] - 1;
                let mut is_ltype = false;
                if pat[j] > pat[j + 1] {
                    is_ltype = true;
                } else if pat[j] == pat[j + 1] {  // check whether sa[i] is the index of an L suffix
                    let next_i = sa[pat[sa[i]]];
                    if next_i >= MULTI {
                        is_ltype = true;
                    } else if next_i < EMPTY && pat[sa[i]] + 1 < patlen {
                        if sa[pat[sa[i]] + 1] == EMPTY {
                            is_ltype = true;
                        } else if sa[pat[sa[i]] + 1] < EMPTY {
                            if pat[sa[pat[sa[i]] + 1]] == pat[sa[i]] {
                                is_ltype = true;
                            }
                        }
                    }
                }
                
                if is_ltype {
                    if sa[pat[j]] == UNIQUE {
                        sa[pat[j]] = j;
                    } else if sa[pat[j]] >= MULTI && sa[pat[j] + 1] == EMPTY {
                        if sa[pat[j]] - EMPTY > 2 {
                            sa[pat[j] + 2] = j;
                            sa[pat[j] + 1] = 1;  // set counter
                        } else {
                            sa[pat[j]] = j;
                        }
                    } else if sa[pat[j]] >= MULTI && sa[pat[j] + 1] != EMPTY {
                        let e = pat[j];
                        let c = sa[e + 1];
                        let lfp = e + c + 2;
                        if  c + 2 < sa[pat[j]] - EMPTY {  // not yet at the bucket tail
                            sa[lfp] = j;
                            sa[e + 1] += 1;  // update counter
                        } else {
                            for k in 1..c + 1 {
                                sa[e + k - 1] = sa[e + k + 1];
                            }
                            sa[e + c] = j;
                            sa[e + c + 1] = EMPTY;
                            if i >= e + 2 && i <= e + c + 1 {
                                i -= 2;
                            }
                        }
                    } else if sa[pat[j]] < EMPTY {
                        for k in pat[j]..patlen {
                            if sa[k] == EMPTY {
                                sa[k] = j;
                                break;
                            }
                        }
                    }
                }
            } else if sa[i] >= MULTI {
                i += 1;
            }
            
            i += 1;
        }
        
        // remove LMS-suff form SA, a bucket may contain several LMS suffixes
        last_scanned_type = STYPE;
        for i in (0..pat.len() - 1).rev() {
            if pat_char_type(pat[i], pat[i + 1], last_scanned_type) == STYPE {
                last_scanned_type = STYPE;
            } else {
                if last_scanned_type == STYPE {  // pat[i + 1] is LMS type
                    if sa[pat[i + 1]] <= EMPTY {
                        sa[pat[i + 1]] = UNIQUE;
                    } else {
                        sa[pat[i + 1]] += 1;
                    }
                }
                
                last_scanned_type = LTYPE;
            }
        }
        i = patlen - 1;
        while i > 0 {
            if sa[i] > EMPTY {
                let c = sa[i] - EMPTY;
                for k in 0..c {
                    sa[i - k] = EMPTY;
                }
                i -= c - 1;
            }
            
            i -= 1;
        }
        sa[0] = pat.len() - 1;
        
        // place S-suff in SA
        // init
        let mut last_scanned_type = STYPE;
        for i in (0..patlen - 1).rev() {
            if pat_char_type(pat[i], pat[i + 1], last_scanned_type) == STYPE {
                if sa[pat[i]] >= EMPTY {
                    sa[pat[i]] += 1;
                } else {
                    sa[pat[i]] = UNIQUE;
                }
                last_scanned_type = STYPE;
            } else {
                last_scanned_type = LTYPE;
            }
        }
        i = patlen - 1;
        while i > 0 {
            if sa[i] < EMPTY && sa[i] > 0 {
                let j = sa[i] - 1;
                let mut is_stype = false;
                if pat[j] < pat[j + 1] {
                    is_stype = true;
                } else if pat[j] == pat[j + 1] {  // check whether sa[i] is the index of an S suffix
                    let next_i = sa[pat[sa[i]]];
                    if next_i >= MULTI {
                        is_stype = true;
                    } else if next_i < EMPTY && pat[sa[i]] - 1 > 0 {
                        if sa[pat[sa[i]] - 1] == EMPTY {
                            is_stype = true;
                        } else if sa[pat[sa[i]] - 1] < EMPTY {
                            if pat[sa[pat[sa[i]] - 1]] == pat[sa[i]] {
                                is_stype = true;
                            }
                        }
                    }
                }
                
                if is_stype {
                    if sa[pat[j]] == UNIQUE {
                        sa[pat[j]] = j;
                    } else if sa[pat[j]] >= MULTI && sa[pat[j] - 1] == EMPTY {
                        if sa[pat[j]] - EMPTY > 2 {
                            sa[pat[j] - 2] = j;
                            sa[pat[j] - 1] = 1;  // set counter
                        } else {
                            sa[pat[j]] = j;
                        }
                    } else if sa[pat[j]] >= MULTI && sa[pat[j] - 1] != EMPTY {
                        let e = pat[j];
                        let c = sa[e - 1];
                        let num = sa[pat[j]] - EMPTY;
                        if c + 2 < num {  // not yet at the bucket head
                            let rfp = e - c - 2;
                            sa[rfp] = j;
                            sa[e - 1] += 1;
                        } else {
                            for k in 1..c + 1 {
                                sa[e - k + 1] = sa[e - k - 1];
                            }
                            sa[e - c] = j;
                            sa[e - c - 1] = EMPTY;
                            if i >= e - num + 1 && i <= e - 2 {
                                i += 2;
                            }
                        }
                    } else if sa[pat[j]] < EMPTY {
                        for k in (0..pat[j]).rev() {
                            if sa[k] == EMPTY {
                                sa[k] = j;
                                break;
                            }
                        }
                    }
                }
            } else if sa[i] >= MULTI {
                i -= 1;
            }
            i -= 1;
        }
    }
    
    fn _compute_suffix_array_16_1(pat: &mut [usize], sa: &mut [usize]) {
        rename_pat(pat, sa);
        let lms_cnt = sort_lms_char(pat, sa);
        sort_lms_substr(pat, sa);
        let has_duplicated_char = construct_pat1(pat, sa, lms_cnt);
        sort_lms_suf(pat, sa, lms_cnt, has_duplicated_char);
        induced_sort(pat, sa);
    }
    
    pub fn suffix_array_16(pat: &[u8]) -> Vec<usize> {
        let mut pat = pat.into_iter().map(|x| *x as usize).collect::<Vec<usize>>();
        pat.push(0);
        let mut sa = vec![0; max(pat.len(), 256) * 1];
        _compute_suffix_array_16_1(&mut pat[..], &mut sa[..]);
        
        sa
    }
    
    fn input() -> String {
        use std::io;
        
        let mut input = String::new();
        io::stdin().read_line(&mut input).unwrap();
        String::from(input.trim())
    }
    
    
    fn main() {
        let pat = input();
        
        let sa_16 = suffix_array_16(pat.as_bytes());
        
        for i in 1..pat.len() + 1 { print!("{} ", sa_16[i] + 1) }
    }
    ```

## Suffix sorting over a read-only integer alphabet

A complex problem is solved with complex methods: divide and conquer is used to deal with the tight space constraints.

The difficulty in implementing the algorithm lies in building BitMaps[^np12] on $\texttt{SA}$ to replace the bucket tail/head positions that were originally indicated by the renamed T.

BitMaps here refers to an ordered dictionary (multiset) represented by a bit vector; it is a compact data structure.

Those interested can, for now, only read the original paper and the papers on BitMaps cited in this article.

## Suffix sorting over a read-only general alphabet

The prerequisites are merge sort and heap sort.

Since the author has doubts about the time complexity of the method used there to determine character types, it is not described here either; reading the original paper is recommended.

## Notes

[^in-place-sa-sort]: Li, Zhize; Li, Jian; Huo, Hongwei (2016).*Optimal In-Place Suffix Sorting*. Proceedings of the 25th International Symposium on String Processing and Information Retrieval (SPIRE). Lecture Notes in Computer Science. 11147. Springer. pp. 268–284. arXiv:1610.08305. doi:10.1007/978-3-030-00479-8\_22. ISBN:978-3-030-00478-1.

[^nzc09a]: Ge Nong, Sen Zhang, and Wai Hong Chan. Linear suffix array construction by almost pure induced-sorting. In Data Compression Conference (DCC), pages 193–202. IEEE, 2009.

[^sa-is-intro]: Recommended reading: this [blog post](https://riteme.site/blog/2016-6-19/sais.html) and its [issue list](https://github.com/riteme/riteme.github.io/issues/28)

[^induction-order]: For LML suffixes, the S-type suffixes are induced first; the only difference is that the sentinel must also be counted when computing the LML suffixes.

[^np12]: Gonzalo Navarro and Eliana Providel. Fast, small, simple rank/select on bitmaps. In Proc. 11th International Symposium on Experimental Algorithms (SEA), pages 295–306, 2012.
