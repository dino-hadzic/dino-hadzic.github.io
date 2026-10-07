---
title: Problem setting
---

## Preparation before setting problems

### Having a certain level

On the one hand, it is hard for someone to set a problem harder than their own level by themselves; a certain level in OI helps to come up with better ideas and good solutions. On the other hand, one's OI level to some extent reflects OI experience: contestants who have seen more problems also have their own views on what a "good problem" is.

### Having a serious and responsible attitude

Problems are set for others to solve; rather than showing off, setting problems is mostly about serving others. An algorithm contest is a contest among contestants, not a battle between the problem setter and the solvers. Therefore, the goal of problem setting should not be to defeat the contestants (of course, reasonable protection against AK and good discrimination are also very important), but to let contestants gain something from the contest. It is very important to spend enough time and effort learning how to set problems and to set them seriously and responsibly.

### Being prepared to spend a lot of time

If you want to set problems seriously, you will inevitably spend a lot of time. Without being mentally prepared, this may lead to a rushed contest preparation and insufficient quality, and afterwards to regret for not having spent the time on studying. But problem setting can also bring many good memories; if you are truly interested in it and well prepared mentally, what you gain from it can make up for the time spent.

### Reading this article carefully

This article introduces the whole process of problem setting from two aspects: how to set problems and how to set them well. Anyone who wants to set problems will surely benefit a lot from reading it carefully.

## Problem content

When setting a problem, the idea, i.e. the essential content of the problem, is its soul and the first step of problem setting.

### Sources of ideas

1.  Inspired by existing problems (but do not copy them or strengthen them meaninglessly, e.g. moving a sequence problem onto a cactus).
2.  Inspired by topics you have learned (but do not piece together unrelated topics).
3.  Inspired by life/games (but be careful not to turn a game into a huge simulation).
4.  You don't know why, you just thought of a problem.

### What kinds of ideas are bad

#### About existing problems

Existing (previously seen) problems can be roughly divided into three kinds: completely identical, almost identical, and identical in solution.

-   Completely identical: the AC code of one problem gets AC on the other.
-   Almost identical: changing the AC code of one problem into AC code of the other can be done by someone who cannot solve that problem.
-   Identical in solution: the core idea and solution are the same, but the implementation and less important details differ.

From bottom to top, these three kinds form an inclusion relation.

The following should not happen:

1.  Setting an existing problem knowing that an "almost identical" problem exists.
2.  Setting an "almost identical" existing problem because you did not use a search engine and did not know it existed.
3.  Setting an existing problem when a problem "identical in solution" is widely known (e.g. a NOIP or NOI problem).
4.  A problem "identical in solution" appearing among the non-giveaway problems of a selective exam.

The following had better not happen:

1.  Setting an existing problem knowing that a problem at least "identical in solution" exists.
2.  Setting a problem "identical in solution" because you did not use a search engine and did not know it existed.
3.  Setting an "almost identical" existing problem under any circumstances.

Exceptions where the requirements can be relaxed:

1.  School mock contests.
2.  Mock contests aimed at topic-specific training.
3.  Low-difficulty contests, or problems intended as giveaways.

#### About "toxic" problems

"Toxic problem" is a very vague and subjective notion; here we only cite some earlier discussions on the topic together with our own understanding. The topic is very open and everyone is welcome to share their views.

> A good problem should not be two problems glued together; a good problem has its own idea – and it should highlight that idea without too much wrapping.
>
> A good problem should be novel. A truly good problem is one that inspires people to come up with new good problems.
>
> — [vfk, "UOJ 精神之源流" (The Source of the UOJ Spirit)][1]

Example: ["XR-1" 柯南家族](https://www.luogu.com.cn/problem/P5346) – the two halves of the solution are completely disconnected: the first half is ["template" suffix sorting on a tree](https://www.luogu.com.cn/problem/P5353), and the second half is a classic tree problem. Even if the node weights of the tree are entered arbitrarily, the second part can still be solved; the two parts are unrelated.

> One class of OI problems is mainly mathematical: both the problem statement and the solution have the characteristics of a math problem, and the solution involves no algorithmic knowledge. Such OI problems are collectively called pure math problems.
>
> — [王天懿, "论偏题的危害" (On the Harm of Off-topic Problems)][2]

Classic example: [NOIP2017 小凯的疑惑](https://uoj.ac/problem/329)

The difference between math problems in OI and other math problems, which also reflects the essence of OI, is that in OI math problems the focus is usually not on **what** the answer is, but on how to **speed up** computing the answer. If the focus of a problem is "how to compute" rather than "how to compute quickly", such a math problem is generally not suitable for OI.

> Some off-topic problems involve university physics, leaving contestants helpless when faced with physics concepts they have never encountered, creating a knowledge barrier.
>
> — [王天懿, "论偏题的危害" (On the Harm of Off-topic Problems)][2]

Classic example: ["清华集训 2015" 多边形下海](https://uoj.ac/problem/159)

Not just physics: OI problems should not involve too much knowledge from other disciplines, and if they do, detailed explanations should be given; knowledge from other disciplines should not be a major obstacle to solving the problem.

> A good problem, whatever its difficulty, should have its own thinking difficulty and require contestants to think and discover some properties.
>
> The code of a good problem may be long, but never because it was made long by forced nesting or added conditions; it should be long naturally, so that people feel the code for this problem simply should be this long.
>
> — [王天懿, "论偏题的危害" (On the Harm of Off-topic Problems)][2]

Classic examples: ["SDOI2010" 猪国杀](https://loj.ac/problem/2885), ["集训队互测 2015" 未来程序·改](https://uoj.ac/problem/98)

In ordinary OI contests, thinking difficulty should be the main part. Of course, engineering problems like those on Day 2+ of THUWC/THUSC also have their reasons to exist – after all, the purpose of these camps, besides testing contestants' algorithm design ability, is also to connect with university study, engineering code and the ability to learn from documentation. But in ordinary OI contests, what should be tested is mostly algorithm design and thinking ability.

## Problem statement

### Writing formulas in LaTeX

There are many LaTeX tutorials online, e.g.:

-   [Introduction to LaTeX](../tools/latex.md#图表)
-   [A collection of LaTeX math formulas](https://www.luogu.com.cn/blog/IowaBattleship/latex-gong-shi-tai-quan)
-   [Various LaTeX commands and symbols](https://blog.csdn.net/anxiaoxi45/article/details/39449445)

When using it, pay attention to the [formatting requirements for LaTeX formulas](../intro/format.md).

### Problem background

The problem background should be as short as possible. When the background is long, it should be separated from the problem description.

It must be absolutely avoided that the background seriously hinders understanding of the problem.

If necessary, two versions can be provided: a problem description combined with the background, and a concise problem description.

### Problem description

In short, the problem description must be **clear and easy to understand**.

Every definition in the statement that might not be understood should be explained; undefined concepts must not appear out of nowhere. For example: in [CF1172D Nauuo and Portals](https://codeforces.com/problemset/problem/1172/D) you must explain in the statement what a "portal" is.

Every concept in the statement should be described with a single term. For example: do not say "cost" at one point and "price" at another.

Do not use words with a meaning different from their original or common meaning without explanation. For example: do not use "path" to refer to an edge without explanation.

You must ensure that your statement does not contradict itself. For example: in [CF1173A Nauuo and Votes](https://codeforces.com/problemset/problem/1173/A), "?" is not treated as one kind of "result" because "?" means "there are more than one possible results".

You must ensure that your statement cannot be misread in a self-consistent way, even if such a reading is counterintuitive and nobody would think of it. For example: in [CF1172D Nauuo and Portals](https://codeforces.com/problemset/problem/1172/D), the reason "walk into" is tediously defined and distinguished from "teleport" is to prevent this reading: going through a portal leads to another portal, and arriving at a portal teleports you, so you would bounce back and forth forever.

Reading the problem description in order, one should be able to understand every sentence and grasp the task and requirements of the problem. Doubts should be resolved at least in the very next paragraph, rather than several paragraphs later, or only after reading the input/output format, or even by guessing from the samples. For example: in ["GuOJ Round #1" 琪露诺的冰雪宴会](https://github.com/OI-wiki/problemset/blob/master/contest/online/GuOJ/OI%20Archive%20-%20GuOJ1171.pdf), the goal of the problem, "the maximum amount of water the Misty Lake can eventually receive", first appears only in the output format, and together with the misleading sentence "Reimu can of course quickly compute the total cost of cleaning all the streams", it is even easier to misread the problem; this is unacceptable – the goal of the problem should be explained in the problem description itself. (This example also suffers from the background seriously hindering understanding of the problem.) The same mistake appears in [CF1423(4)N Bubblesquare Tokens](https://codeforces.com/problemset/problem/1423/N), where the goal of the problem, "friend pairs and number of tokens each of them gets on behalf of their friendship", first appears only in the output format.

### Input and output format

It suffices for the input and output format to be clear and **complete**; there are no rigid requirements. I personally suggest writing the input and output format following CF problems; see the [CF problem setter guidelines][3].

To make solving easier, the input and output format had better state the specific meaning of every variable, unless the meaning of a variable is very long and cannot be explained in one sentence (then you can write "see the problem description for its meaning").

Pay special attention: if the output contains decimals, please use an [SPJ](#special-judge) to limit the size of the error as far as possible, rather than requiring "round to x decimal places".

"Round to x decimal places" may require unlimited precision. For example: rounding to three decimal places is required and the actual answer is $0.0015$; then any error, however small, that makes the computed answer smaller than $0.0015$, even if the computed answer is $0.00149999\cdots$, produces a wrong output.

If an SPJ cannot be used, make sure the precision requirement is finite, e.g.: output the answer rounded to three decimal places. Let the correct answer be $ans$; the data guarantee that for any $x$ satisfying $\frac{|x-ans|}{\max(1,ans)}<10^{-9}$, the rounded result is the same as the rounded $ans$.

Some sentences that can serve as reference:

```latex
The first line of input contains three positive integers $n$, $m$, $k$ ($1\le n,m\le 2\cdot 10^5$, $1\le k\le 100$) — $n$ is the length of the sequence, $m$ is the number of operations, and the meaning of $k$ is given in the problem description.
```

```latex
The second line of input contains $n$ non-negative integers $a_1,a_2,\ldots,a_n$ ($1\le a_i\le 10^9$) — the sequence given in the problem.
```

```latex
The $i$-th of the next $m$ lines contains two positive integers $l_i$ and $r_i$ ($1\le l_i\le r_i\le n$), meaning that the $i$-th operation is performed on the interval $[l_i,r_i]$.
```

```latex
Each of the next $n-1$ lines contains two positive integers $u$ and $v$ ($1\le u,v\le n$), meaning that $u$ and $v$ are connected by an edge.

It is guaranteed that the given edges form a tree.
```

```latex
The only line of input contains a non-empty string of lowercase English letters whose length does not exceed $10^6$.
```

```latex
The second line of input contains a real number $x$ ($-10^6\le x\le 10^6$) with at most three decimal places; see the problem description for its meaning.
```

```latex
The output contains one real number; your output is considered correct if its absolute or relative error with respect to the correct answer is less than $10^{-6}$.
```

```latex
The second line of output contains $n$ positive integers describing the solution you constructed — the $i$-th number is the index of the $i$-th card you play.

If there are multiple valid answers, output any of them.
```

???+ note "Generating input data with a random number generator inside the contestant's code"
    Some problems, because the input is very large, require contestants to generate the data inside their code with a given data generator instead of reading it from standard input or a file, in order to prevent input from taking too long.
    
    This approach needs careful consideration because it has many drawbacks:
    
    -   it may introduce randomness in the data that the intended solution does not need, or make constructing data difficult
    -   it may make the input format harder to understand
    -   if the random number generator is poorly encapsulated, even understanding how to use the data generator may be difficult
    -   if the contestant does not use the language recommended by the setter, they may need to write a data generator themselves
    
    This approach is usually used to prevent input from taking too long, so one possible alternative is to distribute a sufficiently fast [input/output optimization](./io.md) template to ensure everyone's input time is as uniform as possible; then even a long input time will not affect the differences in running time between contestants. Another solution is to wrap the problem as a function-call-style (rather than IO-style) interactive problem; even if there is no interaction in the algorithm, an interactive problem can unify the input time, and the IOI has adopted the approach of making all problems interactive. However, both solutions restrict the languages contestants can use, and the setter must manually support every allowed language.
    
    Going back to the root of the problem, it is also worth considering whether such large input is really necessary, whether the goal could be achieved with smaller input, and whether solutions with complexity slightly worse than the intended one need to be hacked at all.

### Constraints

According to CF requirements, the constraints are written in the input format, but in China they are usually written at the end of the problem.

The most common mistake in constraints is incompleteness. Every number and every string in the input should have clearly defined bounds. The input/output format examples given above contain some correct ways of writing constraints.

Common omissions in constraints:

1.  The "integer" in "integer".
2.  The statement only says "integer" rather than "positive integer", and the constraints only give an upper bound without a lower bound.
3.  The character set of a string is not given.
4.  The number of decimal places of a real number is not given.
5.  Some variables are given no range.

You must ensure that the reference solution passes on **any set of data** satisfying the constraints stated in the problem.

???+ note "About "it is guaranteed that the data are generated randomly""
    Some problems say "it is guaranteed that the data are generated randomly"; often such a constraint is not the best solution, because "randomly generated" is not a clear constraint on the data and makes it difficult to judge the actual constraints and to provide hack data.
    
    Generally, "it is guaranteed that the data are generated randomly" can be replaced by the property of the data that the solution needs. For example, randomly generating a tree can often be replaced by limiting the height of the tree.
    
    If you must guarantee random generation, you should specify the exact generation procedure. For example, whether a tree is generated by randomly choosing parents or by randomly generating a Prüfer sequence.
    
    Note that non-deterministic algorithms are different from algorithms that depend on the randomness of the data. The former obtain the correct answer with high probability on any data, while the latter obtain the correct answer on most data and cannot obtain it on certain specific data.

### Samples

Samples should have a certain strength and be able to catch some simple mistakes. Someone who misreads the problem should be able to notice it from the samples.

For problems with several kinds of operations, each operation should appear in the samples.

For problems with several kinds of output (e.g. [CF1173A Nauuo and Votes](https://codeforces.com/problemset/problem/1173/A)), each kind of output should appear in the samples. Exception: problems that ask whether a solution exists although it is actually impossible for no solution to exist.

### Sample explanations

The more complex and harder to understand the problem description, the more a detailed sample explanation is needed.

The easier the problem, the more a detailed sample explanation is needed.

A detailed sample explanation can be accompanied by pictures.

Large samples may have no explanation.

Out of consideration for color-blind people, it is best not to make color necessary for understanding the sample explanation. Colored pictures can be used to make the explanation look nicer, but if color must convey some necessary information, it is best not to use red and yellow or red and green at the same time.

## Time limit, memory limit and partial scores

The purpose of the time and memory limits is to hack solutions with the wrong complexity. (Of course, also to prevent judging from taking too long; e.g. interactive problems that limit only the number of interactions but not the time complexity also have a time limit.)

Therefore, in principle the time limit should be the largest value that does not let wrong solutions pass.

Generally, the time limit should satisfy the following:

1.  At least twice the running time of std in the worst case.
2.  If the contest allows Java, Java should be able to pass.
3.  It should not let wrong solutions pass (except when they really cannot be hacked, or you intend to let some wrong solution pass).

To let large-constant solutions pass while hacking wrong ones, one can usually increase both the constraints and the time limit. But note that sometimes the intended solution (due to caching and other mysterious issues) suffers a huge increase in constant factor when the constraints grow, so increasing the constraints does not necessarily widen the gap in running time between the intended and the wrong solutions.

In formats with partial scores, you can also add graded data and data with slightly smaller constraints so that better wrong solutions and large-constant intended solutions do not pass fully but still get high partial scores.

Note that when the constraints are below $5\cdot 10^5$, you should consider whether the problem can be passed using [instruction sets](https://ouuan.github.io/post/n方过百万-暴力碾标算——指令集优化的基础使用).

Generally, the memory limit should be set large enough, unless the solution with better space complexity is really so clever that it is worth hacking the solutions with large space complexity. In that case, you can consider a partial score with a looser memory limit. It is worth noting that if you do not intend to hack solutions with large memory consumption, data structure problems usually need a large memory limit.

> A good problem should have selective power, with sufficient discrimination. There should be at least 4 levels of partial scores, so that beginners can score and experts can show their strength.
>
> — vfk, "UOJ 精神之源流" (The Source of the UOJ Spirit)

Partial scores are generally of two kinds: smaller constraints and special properties.

Smaller constraints should usually be set in several levels; even if you cannot think of a solution of some complexity, you can consider giving that complexity a level. Generally, to avoid hacking by constant factor, you can set a level with the maximum data divided by two.

"Graded data" is better replaced by multiple levels of partial scores.

Partial scores for special properties depend on the specific problem. Ideal special-property partial scores should guide contestants toward the intended solution. Unlike smaller-constraint partial scores, if you do not know a solution for a special property, it is better not to give that property a level. For example: the $k=1$ level of ["CTS2019" 随机立方体](https://loj.ac/problem/3119) was criticized by many during the problem discussion, saying that this level hindered thinking about the intended solution.

If the scoring method differs from the default (e.g. bundled subtasks in a contest with the usual OI format), it must be stated in the problem statement.

The wording "XX% of the data satisfy XX" is not recommended, especially when the constraints involve several variables. For example, "$30\%$ of the data satisfy $n \le 1000$" and "$40\%$ of the data satisfy $m \le 100$" may describe the properties of $70\%$ of the data or only of $40\%$. Generally, subtasks or a constraints table are a better choice.

## Making test data

Generating data is a necessary step in problem setting and is also needed for stress testing; mastering some data generation techniques makes the process easier and the data stronger.

### Generating random data

#### Generating random numbers

See the [Random functions](../misc/random.md) page.

A special reminder: when generating numbers from a range larger than the return value of the random function, **do not** write things like `rand() * rand()`; random numbers generated this way are very non-uniform.

In addition, when setting problems it is recommended to use [testlib](../tools/testlib/generator.md) to generate data; it guarantees that the same seed generates the same random numbers on different platforms, and the seed is generated automatically from the command line arguments.

#### Generating a random permutation

You can use the `std::shuffle` function from the STL, in the form `std::shuffle(a, a + n, rng)`, where `rng` is a random number generator, e.g. `std::mt19937 rng(std::chrono::steady_clock::now().time_since_epoch().count())`.

**Do not** use `std::random_shuffle`; it was deprecated in C++14 and removed in C++17.

#### Generating a random interval

A common wrong method: randomly generate the left endpoint $l$ in $[1,n]$, then randomly generate the right endpoint $r$ in $[l, n]$. Intervals generated this way lean to the right.

A roughly correct method (recommended): randomly generate two numbers in $[1, n]$, take the smaller as the left endpoint and the larger as the right endpoint.

A truly uniformly random method: generate a random number $x$ in $[0, n]$; if $x = 0$, generate a random number $y$ in $[1, n]$ and the interval is $[y, y]$; otherwise generate according to the "roughly correct method".

#### Generating a random tree

The common method is, for every node $i$ in $2\sim n$, to randomly choose a parent in $[1,i-1]$. Trees generated this way are not uniformly random, and the expected height is $O(\log n)$.

There is another random method: randomly choose the parent of $i$ in $[i\cdot low, i\cdot high]$. If $low$ and $high$ are set properly, fairly strong trees can be produced.

The truly uniformly random method uses the [Prüfer sequence](../graph/prufer.md): first generate a random Prüfer sequence, then build the tree from the sequence. In this case, the expected height of the tree is $O(\sqrt n)$.

In addition, you can generate a random permutation to renumber the nodes / shuffle the order of the edges.

### Constructing data

#### Interval-related problems

Common constructions: very small lengths (in particular, all single points), very large lengths (in particular, all the whole sequence).

#### Problems that require factorization

As many prime factors with multiplicity as possible: powers of $2$.

As many distinct prime factors as possible: the product of the first several primes.

As many divisors as possible: see sequence [A002182](http://oeis.org/A002182) on OEIS.

#### Problems that require the greatest common divisor

Making the two numbers whose greatest common divisor is to be computed adjacent terms of the [Fibonacci sequence](../math/combinatorics/fibonacci.md) makes the Euclidean algorithm reach its worst-case time complexity.

#### Problems on trees

Common constructions:

-   a chain
-   a star
-   a complete binary tree
-   a complete binary tree with every node replaced by a chain of length $\sqrt n$
-   a star with a chain hanging from it
-   a chain with some single nodes hanging from it
-   a tree of height $d$, $d>1$, whose root has two children: the left subtree is a chain of length $d-1$, and the right subtree is such a tree of height $d-1$.

Outside of a contest, you can also use [Tree-Generator](https://github.com/ouuan/Tree-Generator) to generate all kinds of trees.

### Generating data in batches

The author recommends the method of command line arguments + bat/sh.

For example:

`gen.cpp`:

```cpp
#include "testlib.h"

using namespace std;

int n, m, k;
vector<int> p;

int main(int argc, char* argv[]) {
  registerGen(argc, argv, 1);

  int i;

  n = atoi(argv[1]);
  m = atoi(argv[2]);
  k = rnd.next(1, n);

  for (i = 1; i <= n; ++i) p.push_back(i);

  shuffle(p.begin(), p.end());
  // shuffle using rnd.next()

  printf("%d %d %d\n", n, m, k);
  for (i = 0; i < n; ++i) {
    printf("%d%c", p[i], " \n"[i == n - 1]);
    // using the string as an array: space in between, newline at the end – a common trick when generating data
  }

  return 0;
}
```

`gen_scripts.bat`:

```bat
gen 10 10 > 1.in
gen 1 1 > 2.in
gen 100 200 > 3.in
gen 2000 1000 > 4.in
gen 100000 100000 > 5.in
```

The advantage is that only one generator needs to be written for different data, and the parameters of a given test can be modified easily.

### Requirements for test data

The data should include the minimum and maximum values of every parameter.

The data should include all kinds of corner cases.

When using subtasks, the data (including input and output) had better cover every part of the value range, rather than only the maximum values of the constraints.

To prevent special-case checks targeting specific constructions from passing, different constructions can be combined in one test, or most of the data can be constructed with a small random part mixed in.

The data should include all kinds of constructions, even if you do not know which wrong solution would fail on them. (In formats with per-test scoring this should be handled with discretion.)

Of course, if you know a wrong solution (one a normal person could think of and write) with a correctness problem, try to hack it.

A special reminder: if integer overflow is possible, be sure to hack solutions that overflow. In formats with partial scores, people who do not use long long should not get the same or even lower scores than brute force.

If there are pretests, they should be as strong as possible (and at the same time as few as possible). In other words, the pretests should (with as few tests as possible) include all known pitfalls of the problem.

If you want a few rather than no FSTs, you should still ensure the pretests are strong, because in the actual contest mistakes you did not anticipate are very likely to appear, leading to far more FSTs than expected.

### Data format

Here are some common requirements for the format of input data, which can serve as a general reference:

> 1.  Use the newline format of the testing environment.
> 2.  The last line of the file ends with a newline, i.e. the last character of the whole file must be `\n`.
> 3.  No line starts or ends with whitespace.
> 4.  No more than 1 consecutive space.

Data generated in a Windows environment usually have the newline format `\r\n`, while mainstream judging systems run on Linux, whose newline format is `\n`. Reading Windows-format newlines on Linux may cause abnormal newline handling when reading strings, leading to different program results in different environments; comparing output generated on Linux with reference output generated on Windows may show differences due to the different newline formats. To keep program behavior consistent, the newline format of all data must be converted to the newline format of the environment where the program runs.

Data with Linux newlines can generally be generated as follows:

1.  Generate the data directly in a Linux environment.
2.  Convert the input and output files with the [`dos2unix`](https://dos2unix.sourceforge.io/) tool, which is included in toolchains such as Cygwin and MinGW.
3.  Open the output file in binary mode and use `\n` as the newline.
4.  Write your own tool following the `dos2unix.cpp` code on [this page](https://help.luogu.com.cn/manual/luogu/problem/testcase-format#附录windows-环境下造数据注意事项).

## Special Judge

[SPJ writing tutorial](../tools/special-judge.md)

Problems that output a construction and problems that output floating-point numbers are two common types of problems that need an SPJ; other problems may also need one depending on the situation. On CF, all problems must use a testlib-based checker; for example, when the problem asks for several integers, testlib's built-in ncmp checker is used, and contestants can output whitespace arbitrarily (either spaces or newlines).

Checkers are usually written with testlib. Since a checker has to deal with all kinds of invalid output and needs to be extremely robust, it is very hard to write a good checker without testlib.

Two points to note when writing a checker:

1.  You need to deal with all kinds of invalid output, so check whether every variable read is within the valid range (`readInt(minvalue, maxvalue)`). For example: when reading a variable that will be used as an array index during checking, its range must be checked, otherwise the array may go out of bounds, which sometimes causes RE and sometimes may result in an AC verdict.
2.  In principle, the checker should not check whitespace (i.e. it should not use `readSpace()`, `readEoln()`, `readEof()`; it is worth mentioning that testlib automatically checks for extra output).

## Editorial

The goal of the editorial is that everyone expected to take part in the contest can understand it. So the requirements on the level of detail of the official editorial are higher than for an ordinary solution write-up.

### About partial scores

For problems with partial scores, the editorial may also describe the solutions for the partial scores.

### About topics

The topics used in the solution should be clearly pointed out. For topics whose difficulty is comparable to the difficulty of the problem, it is best to provide material for learning the topic (e.g. the address of a blog post).

### About definitions

Concepts should not appear out of nowhere in the editorial.

For example: the editorial of a DP problem must clearly explain the definition of the states.

### About details

If specific implementation details are clever, it is best to write them down; otherwise "see the code" is also acceptable. If you write "see the code", it is best to add some comments to the code.

### Reference solution

Redundant parts had better be removed from the reference solution. For example, some editorials keep the full define template (containing lots of defines and common functions to speed up solving, commonly used in online contests such as CF), most of which is unused; this is bad.

If there are implementation details not explained in detail in the editorial, it is best to add an appropriate amount of comments.

## The contest

### The problem difficulty in the contest announcement must be truthful

> Remember that authors tend to underestimate the difficulty of their problems.
>
> — reminder on the Codeforces PROPOSE A PROBLEM page

Problem setters are very likely to misjudge the difficulty of their problems, so if you want to state the difficulty in the contest announcement, consider it carefully and preferably ask someone to test the problems and assess them in advance.

### Distribution of problem difficulty

In mock contests in the style of Chinese OI, it is usually enough that the overall difficulty of the three problems matches the difficulty of the contest.

In online contests in the style of CF/ATC, you should try to ensure increasing difficulty (although, due to misjudged difficulty, this often cannot really be achieved) and try to avoid large difficulty gaps. A difficulty gap can be reduced by splitting a problem into an easy and a hard one (two subtasks), but splitting into subtasks needs careful consideration, and many people dislike subtasks in the CF format ([Are subtasks evil?](https://codeforces.com/blog/entry/71700)), for reasons including but not limited to:

-   due to the contest format, solving the easy version first and then the hard version may give less penalty and a higher total score
-   the scores of the subtasks are often not proportional to the difficulty of the problems
-   the easy version is often not a proper problem (not interesting)
-   the solution of the easy version often does not help in thinking about the intended solution of the hard version

### Distribution of problem topics

A contest should cover a wide range of topics as far as possible (except, of course, topic-specific training contests).

A classic counterexample: CTS2019, which covered dynamic programming, expectation, combinatorial counting, inclusion–exclusion, polynomials and other topics.

> I have to pick six problems out of five; there is nothing I can do.
>
> — the reason given by the CTS2019 contest setter: not enough problem proposals were received

## Problem setting platforms

### Polygon

Polygon is a very powerful platform for collaborative problem setting and can be the first choice for collaborative problem setting on any site (using the package feature to export to sites that do not support Polygon); it is also a very good choice for setting problems alone (especially on different devices). For usage, see the [Introduction to Polygon](../tools/polygon.md).

### Codeforces

Codeforces is one of the most famous algorithm competition sites in the world, with high-quality problems, very suitable for setters who already have some experience, want to further improve their problem setting skills and want to set a high-quality problem set. The downside is the slow review (usually several months), but you can start preparing the problems during the review (although there is a risk that a problem is rejected and the preparation is wasted).

#### Eligibility for setting problems

-   blue rating and participation in at least 25 rated contests;
-   purple rating and participation in at least 15 rated contests;
-   orange rating and participation in at least 5 rated contests;
-   red or black-red rating.

#### Submitting a contest proposal

Once you are eligible, you can see the [Propose a contest/problems](http://codeforces.com/proposals/new-contest) button in the sidebar.

After opening it, first write a contest proposal (in PROPOSE A CONTEST), then write problem proposals and add them to the contest.

Once the problems are decided, you can open the contest proposal to review (submit it for review).

#### Preparing problems on Polygon

See the [Introduction to Polygon](../tools/polygon.md).

#### Communicating with the coordinators

Communicating with the coordinators serves two purposes:

1.  Speeding up the review.
2.  After entering the preparation stage, the coordinators provide advice and help.

The official way to communicate is to submit an application in the form of a proposal in the proposal system; after a coordinator starts the review, the discussion takes place as comments under the proposal.

In practice, if a proposal has not been reviewed for a long time, you can consider contacting a coordinator by private message (CF does say "Don't send private messages or emails to coordinators", but 300iq said in a [comment](http://codeforces.com/blog/entry/64077#comment-478933) that you can message him privately).

### Comet OJ

[Comet OJ link](https://www.cometoj.com/)

No longer active (as of November 2021, the last contest was in January 2020).

Problem setting application: <https://info.cometoj.com/contests/Questionnaire_IssuerInfo/>

### CodeChef

An Indian algorithm competition platform with three formats: the 10-day Long Challenge with a challenge problem, the 2.5-hour ICPC-style Cook-Off, and the 3-hour IOI-style LunchTime.

Problem setting FAQ: <https://www.codechef.com/wiki/faq-problem-setters>

Problem setting guide: <https://www.codechef.com/problemsetting>

### AtCoder

A Japanese algorithm competition platform; contact for problem setting: `contest@atcoder.jp`.

### UOJ & LOJ

Chinese OJs with few contests.

### Luogu

Staff involved in problem setting need a certain level of verified awards; after creating a contest, the person in charge submits an application in the [ticket system](https://www.luogu.com.cn/ticket).

Public contest standards: <https://help.luogu.com.cn/rules/academic/opencontest-standard>

## References

1.  [vfk, "UOJ 精神之源流" (The Source of the UOJ Spirit)][1]

2.  [王天懿, "论偏题的危害" (On the Harm of Off-topic Problems)][2]

3.  [CF problem setter guidelines][3] ([image version accessible in China](https://github.com/OI-wiki/libs/blob/master/topic/rules.jpg))

4.  [Self-cultivation of a CF problem setter][4]

This article was ported by the author from [ouuan's problem setting standards](https://ouuan.github.io/post/ouuan-的出题规范/) with modifications and additions.

[1]: https://vfleaking.blog.uoj.ac/blog/909 "vfk《UOJ 精神之源流》"

[2]: https://github.com/OI-wiki/libs/blob/master/topic/7-%E7%8E%8B%E5%A4%A9%E6%87%BF-%E8%AE%BA%E5%81%8F%E9%A2%98%E7%9A%84%E5%8D%B1%E5%AE%B3.ppt "王天懿《论偏题的危害》"

[3]: https://docs.google.com/document/d/e/2PACX-1vRhazTXxSdj7JEIC7dp-nOWcUFiY8bXi9lLju-k6vVMKf4IiBmweJoOAMI-ZEZxatXF08I9wMOQpMqC/pub "CF 出题人须知"

[4]: https://github.com/OI-wiki/libs/blob/master/topic/CF%E5%87%BA%E9%A2%98%E4%BA%BA%E7%9A%84%E8%87%AA%E6%88%91%E4%BF%AE%E5%85%BB.md "CF 出题人的自我修养"
