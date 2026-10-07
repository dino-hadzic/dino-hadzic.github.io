---
title: Boyer–Moore algorithm
---

Prerequisites: [Prefix function and the KMP algorithm](./kmp.md).

The KMP algorithm pushes the use of prefix-matching information to its limit,

while the basic idea behind the BM algorithm is to obtain more information through suffix matching than prefix matching provides, achieving faster character skips.

## Introduction

Imagine that our pattern string $pat$ is placed at the left end of the text string $string$, so that their first characters are aligned.

$$
\begin{aligned}
\textit{pat}:\qquad\qquad &\texttt{EXAMPLE} \\
\textit{string}:\qquad\quad &\texttt{HERE IS A SIMPLE EXAMPLE} \dots \\
&\qquad\ \ \ \, \, \Uparrow
\end{aligned}
$$

We make the following definitions here and will not repeat them later:

the length of $pat$ is $patlen$; in particular, for 0-based strings we define $patlastpos=patlen-1$ as the position of the last character of $pat$;

the length of $string$ is $stringlen$, and $stringlastpos = stringlen-1$.

Suppose we know the $patlen$-th character $char$ of $string$ (aligned with the last character of $pat$). Consider what information we can obtain:

### Observation 1

If we know that the character $char$ does not occur in $pat$, we do not need to consider occurrences of $pat$ starting at the $1$st, $2$nd, …, $patlen$-th character of $string$; we can directly slide $pat$ down by $patlen$ characters.

### Observation 2

More generally, **if the position of the last (i.e. rightmost) occurrence of the character $char$ in $pat$ is $delta_1$ characters away from the end**,

then without matching we can directly slide $pat$ by $delta_1$ characters: if the sliding distance were less than $delta_1$, the character $char$ alone could not be matched, and of course the pattern $pat$ could not be matched either.

Therefore, unless the character $char$ matches the last character of $pat$, $string$ should skip $delta_1$ characters (equivalent to sliding $pat$ by $delta_1$ characters). And we obtain a function $delta_1(char)$ for computing $delta_1$:

$$
\begin{array}{ll}
\textbf{int}\ delta1(\textbf{char}\ char) \\
\qquad \textbf{if}\ \text{char is not in pat || char is the last character of pat} \\
\qquad\qquad\textbf{return}\ patlen \\
\qquad \textbf{else} \\
\qquad\qquad\textbf{return}\ patlastpos-i\quad\textbf{//}\ \text{i is the position of the rightmost occurrence of char in pat, i.e. pat[i]=char}
\end{array}
$$

Note that this table obviously only needs to be computed up to position $patlastpos-1$.

Now suppose $char$ matched the last character of $pat$; then we check whether the character before $char$ matches the second-to-last character of $pat$:

if so, we keep going backwards until the whole pattern $pat$ is matched (at which point we have successfully found an occurrence of $pat$ in $string$);

or we may, after matching the last $m$ characters of $pat$, mismatch on the $(m+1)$-th character from the end. Then we want to slide $pat$ to the next position where a match could occur, and of course we want to slide as far as possible.

### Observation 3(a)

As mentioned in **Observation 2**, when a mismatch occurs on the $(m+1)$-th character from the end after matching the last $m$ characters of $pat$, in order to align the mismatched character in $string$ with the corresponding character in $pat$,

we need to slide $pat$ by $k$ characters, which means we should turn our attention to the character $k+m$ positions further (i.e. the character in $string$ aligned with the end of $pat$ after sliding $pat$ by k).

And $k=delta_1-m$,

so our attention should jump forward along $string$ by $delta_1-m+m = delta_1$ characters.

However, we have a chance to skip even more characters; please read on.

### Observation 3(b)

If we know that the next $m$ characters of $string$ match the last $m$ characters of $pat$, let us call this substring $subpat$.

We also know that after the mismatched character $char$ in $string$ there is a substring matching $subpat$; if $subpat$ occurs in $pat$ before the character corresponding to the mismatched character, we can slide $pat$ down by some distance

so that the $subpat$ occurring in $pat$ before the character corresponding to the mismatched character $char$ (a plausible reoccurrence, abbreviated pr below) is aligned with the $subpat$ in $string$. If there are several $subpat$ in $pat$, following the right-to-left suffix matching order we take the first one (the rightmost plausible reoccurrence, abbreviated rpr below).

Suppose $pat$ slides down by $k$ characters (i.e. the distance between the $subpat$ at the end of $pat$ and its rightmost plausible reoccurrence); then our attention should slide forward along $string$ by $k+m$ characters. We call this distance $delta_2(j)$:

Let $rpr(j)$ be the position of the rightmost plausible reoccurrence of $subpat=pat[j+1\dots patlastpos]$ when a mismatch occurs at $pat[j]$, with $rpr(j) < j$ (only a simple definition is given here; a more precise discussion follows in the algorithm design section below). Then clearly $k=j-rpr(j),\ m=patlastpos-j$.

So we have:

$$
\begin{array}{ll}
\textbf{int}\ delta2(\textbf{int}\ j) \quad\textbf{//}\ \text{j is the position in pat of the character corresponding to the mismatched character} \\
\qquad\qquad\textbf{return}\ patlastpos-rpr(j) \\
\end{array}
$$

Thus, on a mismatch, we can jump our attention on $string$ forward by $\max(delta_1,delta_2)$ characters.

## Procedure

The arrow points to the mismatched character $char$:

$$
\begin{aligned}
\textit{pat}:\qquad\qquad &\texttt{AT-THAT} \\
\textit{string}:\ \ \ \dots\ &\texttt{WHICH-FINALLY-HALTS.--AT-THAT-POINT} \dots \\
&\qquad\ \ \ \, \, \Uparrow
\end{aligned}
$$

$\texttt{F}$ does not occur in $pat$, so by **Observation 1** we directly move $pat$ down by $patlen$ characters, i.e. 7 characters:

$$
\begin{aligned}
\textit{pat}:\qquad\qquad &\qquad\quad\ \ \, \texttt{AT-THAT} \\
\textit{string}:\ \ \ \dots\ &\texttt{WHICH-FINALLY-HALTS.--AT-THAT-POINT} \dots \\
&\qquad\ \ \ \, \, \qquad\quad\ \ \ \Uparrow
\end{aligned}
$$

By **Observation 2**, we need to move $pat$ down by 4 characters so that the hyphens are aligned:

$$
\begin{aligned}
\textit{pat}:\qquad\qquad &\qquad\qquad\quad\ \ \, \texttt{AT-THAT} \\
\textit{string}:\ \ \ \dots\ &\texttt{WHICH-FINALLY-HALTS.--AT-THAT-POINT} \dots \\
&\qquad\ \ \ \; \qquad\qquad\qquad \Uparrow
\end{aligned}
$$

Now *char*:$\texttt{T}$ matches; move the pointer on $string$ one step to the left and continue matching:

$$
\begin{aligned}
\textit{pat}:\qquad\qquad &\qquad\qquad\quad\ \ \, \texttt{AT-THAT} \\
\textit{string}:\ \ \ \dots\ &\texttt{WHICH-FINALLY-HALTS.--AT-THAT-POINT} \dots \\
&\qquad\ \ \ \; \qquad\qquad\quad\ \, \Uparrow
\end{aligned}
$$

By **Observation 3(a)**, $\texttt{L}$ mismatches; since $\texttt{L}$ is not in $pat$, $pat$ moves down by $k=delta_1-m=7-1=6$ characters, while the pointer on $string$ moves down by $delta_1=7$ characters:

$$
\begin{aligned}
\textit{pat}:\qquad\qquad &\qquad\qquad\qquad\qquad\ \ \,\, \texttt{AT-THAT} \\
\textit{string}:\ \ \ \dots\ &\texttt{WHICH-FINALLY-HALTS.--AT-THAT-POINT} \dots \\
&\qquad\ \ \ \; \qquad\qquad\qquad\qquad\ \ \ \, \, \Uparrow
\end{aligned}
$$

Now $char$ once again matches the last character $\texttt{T}$ of $pat$; the pointer on $string$ matches leftwards, matches $\texttt{A}$, continues leftwards, and finds a mismatch at the character $\texttt{-}$:

$$
\begin{aligned}
\textit{pat}:\qquad\qquad &\qquad\qquad\qquad\qquad\ \ \,\, \texttt{AT-THAT} \\
\textit{string}:\ \ \ \dots\ &\texttt{WHICH-FINALLY-HALTS.--AT-THAT-POINT} \dots \\
&\qquad\ \ \ \; \qquad\qquad\qquad\quad\ \ \ \,\, \Uparrow
\end{aligned}
$$

Intuitively it is clear that, by **Observation 3(b)**, we move $pat$ down by $k=5$ characters so that the suffix $\texttt{AT}$ is aligned; this slide gives the largest sliding distance for the $string$ pointer, with $delta_2=k+patlastpos-j=5+6-4=7$, i.e. the pointer on $string$ slides down by 7 characters.

From a formal point of view, here $delta_1=7-1-2=4,\ delta_2=7, \max(delta_1,delta_2)= 7$,
which formally supports the jump of **Observation 3(b)**:

$$
\begin{aligned}
\textit{pat}:\qquad\qquad &\qquad\qquad\qquad\qquad\qquad\quad \;\, \texttt{AT-THAT} \\
\textit{string}:\ \ \ \dots\ &\texttt{WHICH-FINALLY-HALTS.--AT-THAT-POINT} \dots \\
&\qquad\ \ \ \; \qquad\qquad\qquad\qquad\qquad\quad \ \ \; \Uparrow
\end{aligned}
$$

Now we find that every character of $pat$ equals the corresponding character of $string$: we have found an occurrence of $pat$ in $string$. And it cost only 14 references to $string$, of which 7 are the comparisons necessary for a successful match ($patlen=7$), while the other 7 let us skip 22 characters.

## Algorithm design

### The original matching algorithm

#### Explanation

Now consider the following string matching algorithm using $delta_1$ and $delta_2$:

$$
\begin{array}{ll}
i \gets patlastpos. \\
j \gets patlastpos. \\
\textbf{loop}\\
\qquad \textbf{if}\ j < 0 \\
\qquad \qquad \textbf{return}\ i+1 \\
\\
\qquad \textbf{if}\ string[i]=pat[j] \\
\qquad \qquad j \gets j-1 \\
\qquad \qquad i \gets i-1 \\
\qquad \qquad \textbf{continue} \\
\\
\qquad i \gets i+max(delta_1(string[i]), delta_2(j)) \\
\\
\qquad \textbf{if}\ i > stringlastpos \\
\qquad \qquad \textbf{return}\ false \\
\qquad j \gets patlastpos \\
\end{array}
$$

If the algorithm above does $\textbf{return}\ false$, $pat$ is not in $string$; if it returns a number, it is the position of the first occurrence of $pat$ in $string$ from the left.

Now let us describe more precisely the function $rpr(j)$ on which the computation of $delta_2$ relies.

By the earlier definition, $rpr(j)$ denotes the position of the rightmost plausible reoccurrence of the substring $subpat=pat[j+1\dots patlastpos]$ when a mismatch occurs at $pat[j]$.

In other words, we need to find the best $k$ such that $pat[k\dots k+patlastpos-j-1]=pat[j+1\dots patlastpos]$, taking two special cases into account:

1.  When $k<0$, this amounts to padding a virtual prefix in front of $pat$, which actually also conforms to the principle of the $delta_2$ jump.
2.  When $k>0$, if $pat[k-1]=pat[j]$, then this $pat[k\dots k+patlastpos-j-1]$ cannot serve as a plausible reoccurrence of $subpat$.
    The reason is that $pat[j]$ itself is the mismatched character, so after sliding $pat$ down by $k$ characters, the suffix matching would still mismatch at $pat[k-1]$.

Two more constraints must be noted:

1.  $k < j$. Because when $k=j$, we have $pat[k]=pat[j]$, and a character that mismatches at $pat[j]$ would also mismatch at $pat[k]$.
2.  Considering that $delta_2(patlastpos)= 0$, we define $rpr(patlastpos) = patlastpos$.

#### Procedure

Since understanding $rpr(j)$ is the core of implementing the Boyer–Moore algorithm, we explain it in detail with the following two examples:

$$
\begin{aligned}
\textit{j}:\qquad\qquad\quad\ \ &\texttt{0 1 2 3 4 5 6 7 8} \\
\textit{pat}:\qquad\qquad\ \  &\texttt{A B C X X X A B C} \\
\textit{rpr(j)}:\qquad\quad\  \  &\texttt{5 4 3 2 1 0 2 1 8} \\
\textit{sgn}:\qquad\qquad\ \   &\texttt{- - - - - - - - +}
\end{aligned}
$$

For $rpr(0)$, $subpat$ is $\texttt{BCXXXABC}$; the rightmost plausible reoccurrence before $pat[0]$ can only be $\texttt{[(BCXXX)ABC]XXXABC}$, i.e. the rightmost plausible reoccurrence position is -5, so $rpr(j)=-5$;

for $rpr(1)$, $subpat$ is $\texttt{CXXXABC}$; the rightmost plausible reoccurrence before $pat[1]$ is $\texttt{[(CXXX)ABC]XXXABC}$, so $rpr(j)=-4$;

for $rpr(2)$, $subpat$ is $\texttt{XXXABC}$; the rightmost plausible reoccurrence before $pat[2]$ is $\texttt{[(XXX)ABC]XXXABC}$, so $rpr(j)=-3$;

for $rpr(3)$, $subpat$ is $\texttt{XXABC}$; the rightmost plausible reoccurrence before $pat[3]$ is $\texttt{[(XX)ABC]XXXABC}$, so $rpr(j)=-2$;

for $rpr(4)$, $subpat$ is $\texttt{XABC}$; the rightmost plausible reoccurrence before $pat[4]$ is $\texttt{[(X)ABC]XXXABC}$, so $rpr(j)=-1$;

for $rpr(5)$, $subpat$ is $\texttt{ABC}$; the rightmost plausible reoccurrence before $pat[5]$ is $\texttt{[ABC]XXXABC}$, so $rpr(j)=0$;

for $rpr(6)$, $subpat$ is $\texttt{BC}$; since $string[0]=string[6]$, i.e. $string[0]$ equals the mismatched character $string[6]$, $string[0\dots 2]$ is not a valid plausible reoccurrence of $subpat$, so the rightmost plausible reoccurrence is $\texttt{[(BC)]ABCXXXABC}$, hence $rpr(j)=-2$;

for $rpr(7)$, $subpat$ is $\texttt{C}$; similarly, since $string[7]=string[1]$, $string[1\dots 2]$ is not a valid plausible reoccurrence of $subpat$, and the rightmost plausible reoccurrence is $\texttt{[(C)]ABCXXXABC}$, hence $rpr(j)=-1$;

for $rpr(8)$, by the definition of $delta_2$, $rpr(patlastpos)=patlastpos$, giving $rpr(8)=8$.

Now let us look at another example:

$$
\begin{aligned}
\textit{j}:\qquad\qquad\quad\ \ &\texttt{0 1 2 3 4 5 6 7 8} \\
\textit{pat}:\qquad\qquad\ \ &\texttt{A B Y X C D E Y X} \\
\textit{rpr(j)}:\qquad\quad\  \  &\texttt{8 7 6 5 4 3 2 1 8} \\
\textit{sgn}:\qquad\qquad\ \   &\texttt{- - - - - - + - +}
\end{aligned}
$$

For $rpr(0)$, $subpat$ is $\texttt{BYXCDEYX}$; the rightmost plausible reoccurrence before $pat[0]$ can only be $\texttt{[(BYXCDEYX)]ABYXCDEYX}$, i.e. the rightmost plausible reoccurrence position is -8, so $rpr(j)=-8$;

for $rpr(1)$, $subpat$ is $\texttt{YXCDEYX}$; the rightmost plausible reoccurrence before $pat[1]$ can only be $\texttt{[(YXCDEYX)]ABYXCDEYX}$, $rpr(j)=-7$;

for $rpr(2)$, $subpat$ is $\texttt{XCDEYX}$; the rightmost plausible reoccurrence before $pat[2]$ can only be $\texttt{[(XCDEYX)]ABYXCDEYX}$, $rpr(j)=-6$;

for $rpr(3)$, $subpat$ is $\texttt{CDEYX}$; the rightmost plausible reoccurrence before $pat[3]$ can only be $\texttt{[(CDEYX)]ABYXCDEYX}$, $rpr(j)=-5$;

for $rpr(4)$, $subpat$ is $\texttt{DEYX}$; the rightmost plausible reoccurrence before $pat[4]$ can only be $\texttt{[(DEYX)]ABYXCDEYX}$, $rpr(j)=-4$;

for $rpr(5)$, $subpat$ is $\texttt{EYX}$; the rightmost plausible reoccurrence before $pat[5]$ can only be $\texttt{[(EYX)]ABYXCDEYX}$, $rpr(j)=-3$;

for $rpr(6)$, $subpat$ is $\texttt{YX}$; since $string[2\dots 3]=string[7\dots 8]$ and $string[6]\neq string[1]$, the rightmost plausible reoccurrence before $pat[6]$ is $\texttt{AB[YX]CDEYX}$, $rpr(j)=2$;

for $rpr(7)$, $subpat$ is $\texttt{X}$; although $string[3]=string[8]$, since $string[2] = string[7]$, the rightmost plausible reoccurrence before $pat[7]$ is $\texttt{[X]ABYXCDEYX}$, $rpr(j)=-1$;

for $rpr(8)$, by the definition of $delta_2$, $rpr(patlastpos)=patlastpos$, giving $rpr(8)=8$.

### An improvement to the matching algorithm

Finally, in practice it is estimated that about 80% of the search time is spent on the jumps of **Observation 1**, i.e. the case where $string[i]$ and $pat[patlastpos]$ do not match and we then skip the whole $patlen$ to the next match attempt.

So we can make a special optimization for this:

we define a $delta0$:

$$
\begin{array}{ll}
\textbf{int}\ delta0(\textbf{char}\ char) \\
\qquad \textbf{if}\ char=pat[patlastpos] \\
\qquad\qquad \textbf{return}\ large\ \ \text{// large is an integer that must satisfy large>stringlastpos+patlen} \\
\qquad \textbf{return}\ delta1(char)
\end{array}
$$

Replacing $delta_1$ with $delta0$, we obtain the improved matching algorithm:

$$
\begin{array}{ll}
i \gets patlastpos \\
\textbf{loop} \\
\qquad\textbf{if} \ i > stringlastpos \\
\qquad\qquad\textbf{return}\ false\\
\\
\qquad\textbf{while}\ i < stringlen \\
\qquad\qquad i \gets i+delta0(string(i)) \ \ \text{// unless string[i] matches the last character of pat, slide down by at most patlen }\\\
\qquad\textbf{if}\ i \leqslant\ large \qquad\qquad\qquad\qquad \text{// this means no character of string matches the last character of pat}\ \\
\qquad\qquad\textbf{return}\ false\\
\\
\qquad i \gets i-large \\
\qquad j \gets patlastpos. \\
\qquad\textbf{while}\ j \geqslant\ 0 \ and \  string[i]=pat[j]\\
\qquad \qquad j \gets j-1 \\
\qquad \qquad i \gets i-1 \\
\\
\qquad \textbf{if}\ j < 0 \\
\qquad \qquad \textbf{return}\ i+1 \\
\qquad i \gets i+max(delta_1(string[i]), delta_2(j)) \\
\\
\end{array}
$$

Here $large$ plays multiple roles: first, it performs fast bad-character jumps similar to the Horspool algorithm introduced later; second, it helps detect whether the string search is finished.

With this improvement, compared with the original algorithm, the redundant computation of $delta_2$ is no longer needed on every **Observation 1** jump, which noticeably improves string search performance on common alphabets.

## Details of building delta2

### Introduction

In the October 1977 issue of *Communications of the ACM*, the paper by Boyer and Moore[^bm] only described the static $delta_2$ table,

while the discussion of a concrete implementation for constructing $delta_2$ appeared in the KMP algorithm paper[^kmp] formally published jointly by Knuth, Morris and Pratt in *SIAM Journal on Computing* in June 1977.

### Naive algorithm

Before introducing Knuth's algorithm for building $delta_2$, by definition we have a naive algorithm suitable for small problems:

1.  For every position `i` in the interval `[0, patlen)`, determine the interval of its possible reoccurrence positions according to the length of `subpat`, namely `[-subpatlen, i]`;
2.  compare the possible reoccurrence positions character by character from right to left, looking for the rightmost reoccurrence position of $subpat$ that meets the requirements of $delta_2$;
3.  finally, do not forget to set $delta_2(lastpos)= 0$.

???+ note "Implementation"
    ```Rust
    use std::cmp::PartialEq;
    
    pub fn build_delta_2_table_naive(p: &[impl PartialEq]) -> Vec<usize> {
        let patlen = p.len();
        let lastpos = patlen - 1;
        let mut delta_2 = vec![];
        
        for i in 0..patlen {
            let subpatlen = (lastpos - i) as isize;
            
            if subpatlen == 0 {
                delta_2.push(0);
                break;
            }
            
            for j in (-subpatlen..(i + 1) as isize).rev() {
                // subpat matches
                if (j..j + subpatlen)
                .zip(i + 1..patlen)
                .all(|(rpr_index, subpat_index)| {
                    if rpr_index < 0 {
                        return true;
                    }
                    
                    if p[rpr_index as usize] == p[subpat_index] {
                        return true;
                    }
                    
                    false
                })
                && (j <= 0 || p[(j - 1) as usize] != p[i])
                {
                    delta_2.push((lastpos as isize - j) as usize);
                    break;
                }
            }
        }
        
        delta_2
    }
    ```

In particular, we give the necessary explanations of Rust language features, not to be repeated below:

-   `usize` and `isize` are the unsigned and signed integers with the same byte width as a memory pointer; on 32-bit machines they correspond to `u32` and `i32`, on 64-bit machines to `u64` and `i64`.
-   Numbers of type `usize` are used when indexing arrays, vectors and slices (because this is random memory access and the index cannot be negative), so if negative values need to be handled we use `isize`, while indexing requires `usize` again; this is why the `as` keyword is used for explicit conversion between the two.
-   `impl PartialEq` is only used as a generic, supporting both `Unicode`-encoded `char` and binary `u8`.

Clearly, the time complexity of this brute-force algorithm is $O(n^3)$.

### Efficient algorithm

Next we introduce the efficient algorithm with $O(n)$ time complexity, which however requires an additional $O(n)$ space.

Although Knuth proposed this construction method in 1977, his original version of the construction algorithm has a flaw: for some $pat$ it does not actually produce a $delta_2$ conforming to the definition.

Rytter's 1980 article in *SIAM Journal on Computing*[^rytter] proposed a correction; the following is the construction algorithm for $delta_2$:

First, considering that the definition of $delta_2$ is rather complex, we classify by the reoccurrence position of $subpat$ and handle each class separately; this is the key idea of the efficient implementation.

Ordered by reoccurrence position from far to near, i.e. by offset from large to small, we distinguish the following classes:

1.  The reoccurrence of the whole $subpat$ lies entirely to the left of $pat$, e.g. $\texttt{[(EYX)]ABYXCDEYX}$; then $delta_2(j) = patlastpos\times 2 - j$;

2.  the reoccurrence of $subpat$ is partly to the left of $pat$ and partly the head of $pat$, e.g. $\texttt{[(XX)ABC]XXXABC}$; then $patlastpos < delta_2(j) < patlastpos\times 2 - j$;
    we also classify here the boundary case where $subpat$ is entirely the head of $pat$ (depending on the implementation it could also be classified below), e.g. $\texttt{[ABC]XXXABC}$; then $patlastpos = delta_2(j)$;

3.  the reoccurrence of $subpat$ lies entirely inside $pat$, e.g. $\texttt{AB[YX]CDEYX}$; then $delta_2(j) < patlastpos$.

Now let us discuss how to compute these three cases efficiently:

#### The first case

This is the simplest case: a single pass suffices, and $delta_2$ can be initialized along the way.

#### The second case

Let us observe when the reoccurrence of $subpat$ is partly to the left of $pat$ and partly the head of $pat$. It should be when some suffix of $subpat$ equals some prefix of $pat$,

e.g. in the earlier example:

$$
\begin{aligned}
\textit{j}:\qquad\qquad\quad\ \ &\texttt{0 1 2 3 4 5 6 7 8} \\
\textit{pat}:\qquad\qquad\ \  &\texttt{A B C X X X A B C} \\
\end{aligned}
$$

the reoccurrence for $delta_2(3)$ is $\texttt{[(XX)ABC]XXXABC}$; among the suffixes of $subpat$ $\texttt{XXABC}$ and the prefixes of pat there is an equal pair, $\texttt{ABC}$.

In fact, the key to computing both the second and the third case is the computation and application of the prefix function.

So whenever $j$ takes a value such that $subpat$ contains this equal suffix, we obtain a reoccurrence of $subpat$ of the second case; for the example we only need $j \leqslant 5$,

and when $j = 5$ we have the boundary case where $subpat$ is entirely the head of $pat$.

We can compute $delta_2(j)$ in this case:

let the length of this pair of equal prefix and suffix be $\textit{prefixlen}$; we know $subpatlen = patlastpos - j$, so the length of the part to the left of $pat$ is $subpatlen-\textit{prefixlen}$,

and $rpr(j) = -(subpatlen-\textit{prefixlen})$, so we get $delta_2(j) = patlastpos - rpr(j) = patlastpos \times 2 - j - \textit{prefixlen}$.

After that there may be several pairs of equal prefixes and suffixes, e.g.:

$$
\begin{aligned}
\textit{j}:\qquad\qquad\quad\ \ &\texttt{0 1 2 3 4 5 6 7 8 9} \\
\textit{pat}:\qquad\qquad\ \  &\texttt{A B A A B A A B A A} \\
\end{aligned}
$$

For $j\leq2$ we have $\texttt{ABAABAA}$, for $2< j \leq 5$ we have $\texttt{ABAA}$, and for $5<j\leq8$ we have $\texttt{A}$.

The flaw of Knuth's algorithm is that it only considers the longest pair, but in fact we need to consider all cases where a suffix of $subpat$ equals a prefix of $pat$, which is equivalent to computing all equal proper suffixes and proper prefixes of $pat$ and, by length from largest to smallest, computing different $delta_2(j)$ over intervals of $j$.

Using the prefix function and applying the state transition equation for computing the prefix function in reverse, $j^{(n)} = \pi[j^{(n-1)}-1]$, we obtain the lengths of all equal proper prefixes and proper suffixes of $pat$. Starting from $\pi[patlastpos]$ as the length of the longest pair, we then run the state transition equation in reverse to obtain the length of the next longest pair of equal proper prefix and suffix.

This completes the computation of $delta_2$ for the second case.

#### The third case

The reoccurrence of $subpat$ lies exactly inside $pat$ (excluding the head of $pat$), i.e. we look for $subpat$ in $pat[0\dots patlastpos-1]$ in right-to-left order.

If we solve it with the BM algorithm, we obtain a recursive BM implementation of the third case, with the termination condition $patlen \leqslant  2$.

Moreover, by the definition of $delta_2$, the next (i.e. left) character of the found reoccurrence of $subpat$ must not equal the next character of the $subpat$ that is the suffix of $pat$.

This nicely suggests that we can compute the third case with a process similar to computing the prefix function, only with a left-right reversed prefix function:

-   two pointers point respectively to the left endpoint of the substring and to the "prefix" position of the longest common prefix-suffix of the substring; they move from right to left, and keep moving when the two characters pointed to are equal, which corresponds to the "prefix" growing;
-   when the two characters are not equal, the previously equal part satisfies the reoccurrence requirement of $delta_2$, and the pointer to the "prefix" position is moved back until a new character equality is formed or it goes out of bounds.

As with the prefix function, an auxiliary array is needed for backtracking; the space of the prefix array generated when computing the second case can be reused.

### Implementation

??? note "Implementation of the above"
    ```rust
    use std::cmp::PartialEq;
    use std::cmp::min;
    
    pub fn build_delta_2_table_improved_minghu6(p: &[impl PartialEq]) -> Vec<usize> {
        let patlen = p.len();
        let lastpos = patlen - 1;
        let mut delta_2 = Vec::with_capacity(patlen);
        
        // the first case
        // delta_2[j] = lastpos * 2 - j
        for i in 0..patlen {
            delta_2.push(lastpos * 2 - i);
        }
        
        // the second case
        // lastpos <= delata2[j] = lastpos * 2 - j
        let pi = compute_pi(p);  // compute the prefix function
        let mut i = lastpos;
        let mut last_i = lastpos; // only for initialization
        while pi[i] > 0 {
            let start;
            let end;
            
            if i == lastpos {
                start = 0;
            } else {
                start = patlen - pi[last_i];
            }
            
            end = patlen - pi[i];
            
            for j in start..end {
                delta_2[j] = lastpos * 2 - j - pi[i];
            }
            
            last_i = i;
            i = pi[i] - 1;
        }
        
        // the third case
        // delata2[j] < lastpos
        let mut j = lastpos;
        let mut t = patlen;
        let mut f = pi;
        loop {
            f[j] = t;
            while t < patlen && p[j] != p[t] {
                // the min function ensures that possible later backtracking does not overwrite earlier data
                delta_2[t] = min(delta_2[t], lastpos - 1 - j);
                t = f[t];
            }
            
            t -= 1;
            if j == 0 {
                break;
            }
            j -= 1;
        }
        
        // no practical meaning, only for a complete definition
        delta_2[lastpos] = 0;
        
        delta_2
    }
    ```

## The Galil rule's improvement of the worst case for multiple matches

### The multiple-match problem of suffix matching algorithms

The previous search algorithm only dealt with finding the first match of $pat$ in $string$, while for finding all matches of $pat$ in $string$ there are many different algorithmic approaches. The core concern of this problem is: how to use the information about previously successfully matched characters to reduce the worst-case time complexity to linear.

After a successful match, if the pointer on $string$ simply slides forward by $patlen$ and suffix matching restarts, the worst case falls back to $O(mn)$ time complexity (by convention, $m$ is $patlen$ and $n$ is $stringlen$, also below).

For example, an extreme case: $pat$: $\texttt{AAA}$, $string$: $\texttt{AAAAA}\dots$.

For this, Knuth proposed a method that uses a "finite" set of states to record $patlen$ characters; this algorithm guarantees that every character of $string$ is compared at most once, but at the cost that this "finite" set of states may not be small: for a $pat$ whose characters are pairwise distinct, $\dfrac{1}{2}m^{2}+m$ states are needed.

Below we introduce the Galil algorithm[^galil-rule], whose idea is simple and requires no additional preprocessing overhead.

### The Galil rule

Suppose a $pat$ is a prefix of the string $UUUU\dots$ formed by repeating some substring $U$ n times; then we call $U$ a period of $pat$.

For example, $pat: \texttt{ABCABCAB}$ is a prefix of the repetition $\texttt{ABCABCABC}$ of $\texttt{ABC}$, so the length $3$ of $\texttt{ABC}$ is the period length of this $pat$, i.e. $pat$ satisfies $pat[i] = pat[i+3]$.

$pat$ has at least one period of length equal to itself; we define the shortest period as $k$, $k\leq patlen$.

During the search, if our $pat$ successfully completes a match, then by the property of the period we actually only need to slide $string$ forward by $k$ characters and compare whether these $k$ characters are correspondingly equal in order to directly decide whether there is another match of $pat$.

To compute the length of this shortest period, suppose we know a pair of equal prefix-suffix of $pat$ of length $\textit{prefixlen}$; then $pat[i] = pat[i+(patlen-\textit{prefixlen})]$. Thus we obtain a period of length $patlen-\textit{prefixlen}$,

and when we know the longest pair of equal prefix-suffix of $pat$, we obtain the shortest period of $pat$.

The length of the longest equal prefix-suffix, $\pi[patlastpos]$, is already available from our computation of $delta_2$, so in fact without additional preprocessing time and space we can improve the worst-case time complexity of the suffix matching algorithm to linear.

??? note "Final implementation of the BM search algorithm combining the above optimizations"
    ```rust
    #[cfg(target_pointer_width = "64")]
    const LARGE: usize = 10_000_000_000_000_000_000;
    
    #[cfg(not(target_pointer_width = "64"))]
    const LARGE: usize = 2_000_000_000;
    
    pub struct BMPattern<'a> {
        pat_bytes: &'a [u8],
        delta_1: [usize; 256],
        delta_2: Vec<usize>,
        k: usize  // length of the shortest period of pat
    }
    
    impl<'a> BMPattern<'a> {
        // ...
        
        pub fn find_all(&self, string: &str) -> Vec<usize> {
            let mut result = vec![];
            let string_bytes = string.as_bytes();
            let stringlen = string_bytes.len();
            let patlen = self.pat_bytes.len();
            let pat_last_pos = patlen - 1;
            let mut string_index = pat_last_pos;
            let mut pat_index;
            let l0 =  patlen - self.k;
            let mut l = 0;
            
            while string_index < stringlen {
                let old_string_index = string_index;
                
                while string_index < stringlen {
                    string_index += self.delta0(string_bytes[string_index]);
                }
                if string_index < LARGE {
                    break;
                }
                
                string_index -= LARGE;
                
                // If string_index moved, at least one failed match happened since the last successful match.
                // In that case the offset of the Galil rule's second match must be reset to zero.
                if old_string_index < string_index {
                    l = 0;
                }
                
                pat_index = pat_last_pos;
                
                while pat_index > l && string_bytes[string_index] == self.pat_bytes[pat_index] {
                    string_index -= 1;
                    pat_index -= 1;
                }
                
                if pat_index == l && string_bytes[string_index] == self.pat_bytes[pat_index] {
                    result.push(string_index - l);
                    
                    string_index += pat_last_pos - l + self.k;
                    l = l0;
                } else {
                    l = 0;
                    string_index += max(
                        self.delta_1[string_bytes[string_index] as usize],
                        self.delta_2[pat_index],
                    );
                }
            }
            
            result
        }
    }
    ```

### Performance impact of the worst case in practice

From a practical point of view, the theoretical worst case does not easily affect performance; even in random-text tests over a very small alphabet of only 4 characters, the impact of this worst case is too small to observe.

Therefore, if not well designed, using the Galil rule can slightly drag down average performance, but for some extremely special $pat$ and $string$, such as the example $pat$: $\texttt{AAA}$, $string$: $\texttt{AAAAA}\dots$, applying the Galil rule does improve performance several times over.

## Improved algorithms

### Simplified Boyer–Moore algorithm

The most complex part of the BM algorithm is the construction of the $delta_2$ table (i.e. the good-suffix table), and in practice it was found that matching performance on common alphabets mainly relies on the $delta_1$ table (i.e. the bad-character table). Hence a simplified BM algorithm using only the $delta_1$ table appeared, whose performance is usually very close to the original.

### Boyer–Moore–Horspol algorithm

The Horspol algorithm is likewise based on the bad-character rule, applying $delta_1$ to the character aligned with the end of $pat$. The effect is similar to the improvement of the original matching algorithm, and its performance is usually better than the original version.

???+ note "Implementation"
    ```rust
    pub struct HorspoolPattern<'a> {
        pat_bytes: &'a [u8],
        bm_bc: [usize; 256],
    }
    
    impl<'a> HorspoolPattern<'a> {
        // ...
        pub fn find_all(&self, string: &str) -> Vec<usize> {
            let mut result = vec![];
            let string_bytes = string.as_bytes();
            let stringlen = string_bytes.len();
            let pat_last_pos = self.pat_bytes.len() - 1;
            let mut string_index = pat_last_pos;
            
            while string_index < stringlen {
                if &string_bytes[string_index-pat_last_pos..string_index+1] == self.pat_bytes {
                    result.push(string_index-pat_last_pos);
                }
                
                string_index += self.bm_bc[string_bytes[string_index] as usize];
            }
            
            result
        }
    }
    ```

### Boyer–Moore–Sunday algorithm

The Sunday algorithm also uses the bad-character rule, but compared with Horspool it goes one step further, directly looking at the character following the one aligned with the end of $pat$.

Implementing it only requires a slight modification of the $delta_1$ table, equivalent to building it on a $pat$ of length $patlen+1$.

The Sunday algorithm is commonly regarded as one of the practical algorithms that are simplest to implement and have the best average performance in the general case; it usually performs a bit better than Horspool and BM.

???+ note "Implementation"
    ```rust
    pub struct SundayPattern<'a> {
        pat_bytes: &'a [u8],
        sunday_bc: [usize; 256],
    }
    
    impl<'a> SundayPattern<'a> {
        // ...
        fn build_sunday_bc(p: &'a [u8]) -> [usize; 256] {
            let mut sunday_bc_table = [p.len() + 1; 256];
            
            for i in 0..p.len() {
                sunday_bc_table[p[i] as usize] = p.len() - i;
            }
            
            sunday_bc_table
        }
        
        pub fn find_all(&self, string: &str) -> Vec<usize> {
            let mut result = vec![];
            let string_bytes = string.as_bytes();
            let pat_last_pos = self.pat_bytes.len() - 1;
            let stringlen = string_bytes.len();
            let mut string_index = pat_last_pos;
            
            while string_index < stringlen {
                if &string_bytes[string_index - pat_last_pos..string_index+1] == self.pat_bytes {
                    result.push(string_index - pat_last_pos);
                }
                
                if string_index + 1 == stringlen {
                    break;
                }
                
                string_index += self.sunday_bc[string_bytes[string_index + 1] as usize];
            }
            
            result
        }
    }
    ```

### BMHBNFS algorithm

This algorithm combines Horspool and Sunday; it is the `find` algorithm used by CPython in the implementation of the `stringlib` module[^b5s], abbreviated B5S below.

The basic idea of B5S is:

1.  Following the idea of suffix matching, first compare whether the characters at position $patlastpos$ are equal; if they are, compare whether the characters at positions $0\dots patlastpos-1$ are equal; if they are still equal, a match is found;

2.  if a mismatch occurs at any stage, enter the jump stage;

3.  in the jump stage, first look at whether the character following position $patlastpos$ is in $pat$; if not, directly slide right by $patlen+1$, which is the maximal use of the Sunday algorithm;

    if this character is in $pat$, apply a Horspool jump with $delta_1$ to the character at $patlastpos$.

Depending on whether saving time or saving space is the primary goal, the implementations of the algorithm differ greatly.

#### Time-saving version

???+ note "Implementation"
    ```rust
    pub struct B5STimePattern<'a> {
        pat_bytes: &'a [u8],
        alphabet: [bool;256],
        bm_bc: [usize;256],
        k: usize
    }
    
    impl<'a> B5STimePattern<'a> {
        pub fn new(pat: &'a str) -> Self {
            assert_ne!(pat.len(), 0);
            
            let pat_bytes = pat.as_bytes();
            let (alphabet, bm_bc, k) = B5STimePattern::build(pat_bytes);
            
            B5STimePattern { pat_bytes, alphabet, bm_bc, k }
        }
        
        fn build(p: &'a [u8]) -> ([bool;256], [usize;256], usize)  {
            let mut alphabet = [false;256];
            let mut bm_bc = [p.len(); 256];
            let lastpos = p.len() - 1;
            
            for i in 0..lastpos {
                alphabet[p[i] as usize] = true;
                bm_bc[p[i] as usize] = lastpos - i;
            }
            
            alphabet[p[lastpos] as usize] = true;
            
            (alphabet, bm_bc, compute_k(p))
        }
        
        pub fn find_all(&self, string: &str) -> Vec<usize> {
            let mut result = vec![];
            let string_bytes = string.as_bytes();
            let pat_last_pos = self.pat_bytes.len() - 1;
            let patlen = self.pat_bytes.len();
            let stringlen = string_bytes.len();
            let mut string_index = pat_last_pos;
            let mut offset = pat_last_pos;
            let offset0 = self.k - 1;
            
            while string_index < stringlen {
                if string_bytes[string_index] == self.pat_bytes[pat_last_pos] {
                    if &string_bytes[string_index-offset..string_index] == &self.pat_bytes[pat_last_pos-offset..pat_last_pos] {
                        result.push(string_index-pat_last_pos);
                        
                        offset = offset0;
                        
                        // Galil rule
                        string_index += self.k;
                        continue;
                    }
                }
                
                if string_index + 1 == stringlen {
                    break;
                }
                
                offset = pat_last_pos;
                
                if !self.alphabet[string_bytes[string_index+1] as usize] {
                    string_index += patlen + 1;  // sunday
                } else {
                    string_index += self.bm_bc[string_bytes[string_index] as usize];  // horspool
                }
            }
            
            result
        }
    }
    ```

The performance of this version of B5S is very good; among the suffix matching algorithms introduced so far it is usually the fastest.

#### Space-saving version

Also implemented in CPython's `stringlib`, it uses two integers to approximately replace the character table and $delta_1$, saving a great deal of space:

1.  A simple Bloom filter replaces the character table (alphabet)

    ???+ note "Implementation"
        ```rust
        pub struct BytesBloomFilter {
            mask: u64,
        }
        
        impl BytesBloomFilter {
            pub fn new() -> Self {
                SimpleBloomFilter {
                    mask: 0,
                }
            }
            
            fn insert(&mut self, byte: &u8) {
                (self.mask) |= 1u64 << (byte & 63);
            }
            
            fn contains(&self, char: &u8) -> bool {
                (self.mask & (1u64 << (byte & 63))) != 0
            }
        }
        ```

    A Bloom filter is a `Set`-type data structure designed to save a great deal of storage space by sacrificing accuracy (and in fact running time too); its characteristic is that it may misjudge an item not in the set as present (False Positives, FP for short), but it never judges an item in the set as absent (False Negatives, FN for short). Therefore, using it we may fail to get the maximal character jump because of an FP, but we will never skip characters that should match because of an FN.

    Theoretical analysis shows that the above "Bloom filter" implementation has an FP probability of about 0.5 when the length of $pat$ is 50 bytes, and about 0.15 when the length of $pat$ is 10 bytes.

    Although this is not a standard Bloom filter — first of all it does not actually use a real hash function; it is really just a character mapping that maps a byte 0–255 to the number formed by its low six bits —

    considering that we are searching characters in memory, this simplification is very important: even with [xxHash](https://cyan4973.github.io/xxHash/), the fastest currently known non-cryptographic hash algorithm, the computation would still take an order of magnitude more time.

    Also, when pat is under 30 bytes, more than one hash function would be needed to reach the optimal FP probability. But there is little point in doing so, because an array holding two `u128` numbers can already build a character table for the full character set.

2.  Use $delta_1(pat[patlastpos])$ instead of the whole $delta_1$

    Looking at $delta_1$, its most frequent use is when the very first character of the suffix match already mismatches, which is the most common mismatch case; so let `skip = delta1(pat[patlastpos])`.

    On a mismatch in the first stage, slide down directly by `skip` characters; but on a mismatch in the second stage, lacking the information of the whole $delta_1$, we can only slide down by one character.

    ???+ note "Implementation"
        ```rust
        pub struct B5SSpacePattern<'a> {
            pat_bytes: &'a [u8],
            alphabet: BytesBloomFilter,
            skip: usize,
        }
        
        impl<'a> B5SSpacePattern<'a> {
            pub fn new(pat: &'a str) -> Self {
                assert_ne!(pat.len(), 0);
                
                let pat_bytes = pat.as_bytes();
                let (alphabet, skip) = B5SSpacePattern::build(pat_bytes);
                
                B5SSpacePattern { pat_bytes, alphabet, skip}
            }
            
            fn build(p: &'a [u8]) -> (BytesBloomFilter, usize)  {
                let mut alphabet = BytesBloomFilter::new();
                let lastpos = p.len() - 1;
                let mut skip = p.len();
                
                for i in 0..p.len()-1 {
                    alphabet.insert(&p[i]);
                    
                    if p[i] == p[lastpos] {
                        skip = lastpos - i;
                    }
                }
                
                alphabet.insert(&p[lastpos]);
                
                (alphabet, skip)
            }
            
            pub fn find_all(&self, string: &'a str) -> Vec<usize> {
                let mut result = vec![];
                let string_bytes = string.as_bytes();
                let pat_last_pos = self.pat_bytes.len() - 1;
                let patlen = self.pat_bytes.len();
                let stringlen = string_bytes.len();
                let mut string_index = pat_last_pos;
                
                while string_index < stringlen {
                    if string_bytes[string_index] == self.pat_bytes[pat_last_pos] {
                        if &string_bytes[string_index-pat_last_pos..string_index] == &self.pat_bytes[..patlen-1] {
                            result.push(string_index-pat_last_pos);
                        }
                        
                        if string_index + 1 == stringlen {
                            break;
                        }
                        
                        if !self.alphabet.contains(&string_bytes[string_index+1]) {
                            string_index += patlen + 1;  // sunday
                        } else {
                            string_index += self.skip;  // horspool
                        }
                    } else {
                        if string_index + 1 == stringlen {
                            break;
                        }
                        
                        if !self.alphabet.contains(&string_bytes[string_index+1]) {
                            string_index += patlen + 1;  // sunday
                        } else {
                            string_index += 1;
                        }
                    }
                
                }
                
                result
            }
        }
        ```

    This version of the algorithm is not as fast as the previous suffix matching algorithms, but the gap is small, and its performance is still better than KMP, thanks to its excellent space complexity of at most two `u64` integers.

## Theoretical analysis

Below is the performance of the algorithms on a common alphabet; the vertical axis is akin to execution cost (cost refers to the cost on a mismatch after successfully matching m characters, skip refers to the probability of sliding down by k characters on a mismatch), and smaller is better. The horizontal axis is the length of the pattern string pat:

![Performance comparison of string search algorithms](./images/BM/plot256.svg)

Performance on a smaller alphabet (DNA base-pair sequences {A, C, T, G}):

![Performance comparison of string search algorithms on a small alphabet](./images/BM/plot4.svg)

In summary, on larger alphabets, such as in everyday searching, the Boyer–Moore family of algorithms performs excellently, relying mainly on the $delta_1$ table for character jumps;

on the other hand, on smaller alphabets the role of $delta_1$ diminishes, and the role of $delta_2$ comes into play.

If some spare space is available, the complete Boyer–Moore algorithm with $O(m)$ space complexity is more general and has the best overall performance.

## References and notes

[^bm]: [The 1977 Boyer–Moore algorithm paper](https://dl.acm.org/doi/10.1145/359842.359859)

[^kmp]: [The 1977 KMP algorithm paper](https://epubs.siam.org/doi/abs/10.1137/0206024)

[^rytter]: [Rytter's 1980 paper correcting Knuth](https://epubs.siam.org/doi/10.1137/0209037)

[^galil-rule]: [The 1979 paper introducing the Galil algorithm](https://doi.org/10.1145%2F359146.359148)

[^b5s]: [Introduction to the B5S algorithm](http://effbot.org/zone/stringlib.htm#BMHBNFS)
