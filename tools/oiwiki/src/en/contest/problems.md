---
title: Overview of problem types
---

Algorithm competitions feature a wide variety of problem types.

## Traditional problems

**Traditional problems** are currently the most common problem type in algorithm competitions.

The contestant submits source code, and the judging system uses input data prepared in advance together with the corresponding output data as test cases[^note1]. After compiling the contestant's source code[^note2], it feeds the input data to the contestant's program and compares the contestant's output with the prepared output to decide whether the program is correct. This kind of judging is called **black-box judging**[^note3].

A time limit and a memory limit are usually set for each test case as well.

The time limit refers to the limit on the program's running time[^note4]. The running time of the contestant's program on a single test case must not exceed the given time limit.

The memory limit refers to the limit on the amount of memory used by the program. The maximum memory occupied by the contestant's program while running must not exceed the given memory limit.

After the program finishes normally, the contestant's output is compared with the test case output. This comparison is generally a full-text comparison after filtering out trailing newlines at the end of the file and trailing spaces at the ends of lines. For certain special problems, a [Special Judge](../tools/special-judge.md) is used for the comparison.

After this process, the judging system gives one of several **verdicts**[^note5] depending on the running state of the program:

-   Accepted (AC): the contestant's program is accepted.
-   Compile Error (CE): the contestant's program fails to compile.
-   Wrong Answer (WA): the contestant's program finishes normally, but its output does not match the test case output.
-   Presentation Error (PE): the contestant's program finishes normally, but the output format does not meet the requirements[^note6].
-   Runtime Error (RE): the contestant's program terminates abnormally (the return value of the program on exit is nonzero).
-   Time Limit Exceeded (TLE): the running time of the contestant's program exceeds the given time limit.
-   Memory Limit Exceeded (MLE): the maximum memory occupied by the contestant's program exceeds the given memory limit.
-   Output Limit Exceeded (OLE): the amount of output produced by the contestant's program exceeds the maximum limit.

In ICPC contests, your program must get AC on all test cases of a problem for the problem to count as solved. In OI contests, getting AC on a test case earns the points for that test case[^note7].

## Output-only problems

**Output-only problems** are problems where the answer is submitted directly. Such problems usually provide the input files and require the submission of an archive, a folder or plain files containing `XXX1.out`, `XXX2.out`, `XXX3.out`, …, `XXXn.out`.

After the answers are submitted, the judging system compares the answer files with the reference answers and awards a certain number of points according to the quality of the contestant's answers and the degree of task completion.

Since output-only problems do not require running a source program, they have no time or memory limits.

There are generally two ways to solve such problems:

-   by hand. This approach is simple and crude, but it is hopeless on larger data;
-   by writing a program to produce the answer files.

## Interactive problems

**Interactive problems** are problems where the contestant's program must interact with the judging program to complete the task. A common situation is that the contestant's program sends queries to the judging program and receives its responses. The judging program may restrict the contestant's queries, or adjust its response strategy to increase the number of queries as much as possible, which brings more variety to the problems.

A more detailed explanation of interactive problems can be found at [Interactive problems](./interaction.md).

There are two main methods of interaction. Although they differ considerably in technical terms, there is no real difference between them in the nature of the algorithms being tested.

### STDIO interaction

STDIO interaction (standard I/O interaction) is the interaction method used by online platforms such as Codeforces and AtCoder, and it is also the standard in ICPC-series contests. Codeforces provides a more concise [explanation (in English)](https://codeforces.com/blog/entry/45307).

???+ note "Example problem [LOJ #559. LibreOJ Round #9, ZQC's Maze](https://loj.ac/problem/559)"
    Please note the addition at the very bottom.
    
    This is an interactive problem.
    
    You are in a dark maze consisting of $n \times m$ cells and must reach the exit of the maze to complete the maze challenge.
    
    Initially you are at the start of the maze, i.e. at $(1,1)$, facing right, and the exit is at $(n,m)$. Any two cells of the maze are connected, and there is exactly one path between them; the distance between two adjacent cells (4-connected: up, down, left, right) is one unit length. There may be a wall between two adjacent cells; the thickness of a wall is negligible compared with a cell. The boundary of the maze consists of walls, and every wall is connected to the boundary. The maze is completely dark, meaning that you cannot obtain any information other than $(n,m)$.
    
    To avoid getting lost in the dark as much as possible, each time you move you can only start from the current cell, follow the left or right wall with your left or right hand on it, and move so that the hand on the wall travels exactly one unit length. Note that if the left or right wall does not exist, you cannot move along that side.
    
    Staying in the dark too long makes you afraid, so you need to leave the maze as early as possible. If you do not leave the maze within the given number of steps, the challenge fails.

For such problems, the contestant simply writes queries to standard output as usual, **flushes the output buffer**, and then reads the result from standard input. Only after the contestant's program flushes the output buffer can the judging program connected to it by pipes (called the interactor) receive the data immediately. In C/C++, `fflush(stdout)` and `std::cout << std::flush` do this (`std::cout << std::endl` also flushes the buffer automatically when starting a new line, but `std::cout << '\n'` does not); in Pascal it is `flush(output)`.

### Grader interaction

Grader interaction is common in international OI contests such as IOI and APIO (especially contests on the CMS platform).

???+ note "Example problem [UOJ #206. APIO2016 Gap](https://uoj.ac/problem/206)"
    There are $N$ strictly increasing nonnegative integers $a_1,a_2,\cdots,a_N (0\leq a_1<a2<\cdots<a_N\leq 10^{18})$. You need to find the maximum value among $a_{i+1}−a_i (0\leq i\leq N−1)$.
    
    Your program cannot read this sequence of integers directly, but you can query information about the sequence through a given function. For details of the query function, refer to the implementation details section below according to the language you use.
    
    You need to implement a function that returns the maximum value among $a_{i+1}−a_i (0\leq i\leq N−1)$.

For such problems, the contestant only needs to write a specific function that accomplishes some task, and it interacts by calling several given helper functions. To make local testing easier, the problem provides a header file and a reference judging program `grader.cpp` (for Pascal, a library `graderlib`); the contestant compiles their own program together with `grader.cpp` to obtain the executable.

```sh
g++ grader.cpp my_solution.cpp -o my_solution -Wall -O2
./my_solution   # run the program
```

The compiled program behaves similarly to a program for a traditional problem. It opens fixed files, reads data in a fixed format, calls the function written by the contestant, and displays the result along with some information (e.g. the number of queries, the correctness of the answer) on standard output.

During actual judging, the contestant's program is compiled with a different `grader.cpp`. This `grader.cpp` calls the contestant's function in a similar way and records the score. Generally, all global symbols in this version of `grader.cpp` are made `static`, so it cannot be circumvented through conflicting names, but any attempt to break the grader's restrictions is punished with disqualification.

### Differences

An obvious advantage of STDIO interaction is that it can support any programming language, but the time spent on input and output easily becomes a bottleneck in problem design, sometimes making it impossible to distinguish differences in the time efficiency of programs; grader interaction is exactly the opposite: since the overhead of function calls is small, on the order of $10^6$ queries can often be allowed, but the restriction to certain languages is its weakness.

If you design problems or organize contests yourself, the two need to be carefully weighed and compared.

## Communication problems

**Communication problems** are problems where two contestant programs must communicate and cooperate to complete some task. The first program receives the input of the problem and produces some output; the input of the second program is related to the output of the first (sometimes passed unchanged as a parameter, sometimes processed by the judge), and it must produce the solution to the problem.

Examples of communication problems include [UOJ #178. New Year's Telegram](https://uoj.ac/problem/178), [#454. UER #8, Snowball Fight](https://uoj.ac/problem/454) and others.

Local testing methods vary with the setup of the problem; common forms include:

-   manual input;
-   writing a helper program that converts the output of the first program into the input of the second;
-   connecting the standard input/output of the two programs with bidirectional pipes.

Because judging platforms have limited support for communication problems, so far they are only common in IOI-series contests and contests held by a few online platforms such as UOJ. It remains an area yet to be explored.

## Function-completion problems

**Function-completion problems** are problems where the contestant must complete a program. They can be understood as an interactive problem in which the contestant's code is given and helper functions have to be written.

They usually take one of the following forms:

-   a program is given, and it is stated where the code block to be completed will be embedded;
-   no program is given; instead, the input information is passed as parameters of the function to be submitted.

Such problems are common on [LeetCode](https://leetcode.com/) and [PTA - Pintia](https://pintia.cn/problem-sets).

## Other types

???+ note "Example problem [Quine](https://loj.ac/problem/4)"
    Write a program that outputs its own source code.
    
    The code must contain at least ten visible characters.

The problem is a classic, but it is hard to implement on the vast majority of online judges.

??? note "Reference code"
    **Note**: the source code does not include the first line below (i.e. `// clang-format off`).
    
    ```cpp
    // clang-format off
    #include<cstdio>
    
    char *s={"#include<cstdio>%cchar *s={%c%s%c};%cint main(){printf(s,10,34,s,34,10);return 0;}"};
    
    int main(){printf(s,10,34,s,34,10);return 0;}
    ```

## References and notes

[^note1]: Because of technical and resource limitations, the test cases of a problem in most cases cannot cover all the data that satisfy the constraints.

[^note2]: For interpreted languages such as Python, the program is run directly by the interpreter.

[^note3]: In fact the implementation of judging systems is far more complex than this; only a rough outline of the judging process is given here.

[^note4]: More precisely, it is usually the user time of the program.

[^note5]: Most of these verdicts also apply to other problem types.

[^note6]: Most judging systems classify the PE status under WA.

[^note7]: Some test cases may carry partial credit: when the contestant completes part of the task on a test case, or the contestant's output is correct but not good enough, a certain proportion of the points can be awarded.
