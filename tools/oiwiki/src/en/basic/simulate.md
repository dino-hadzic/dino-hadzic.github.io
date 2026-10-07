---
title: Simulation
---

This page briefly introduces simulation.

## Introduction

Simulation means using the computer to simulate the operations required by the problem.

Simulation problems are usually characterised by a lot of code, many operations and convoluted logic. Because of the amount of code, bugs are often hard to find, and getting it wrong during a contest wastes a great deal of time.

## Tips

When solving simulation problems, following these suggestions may speed things up:

-   Before writing code, write out the flow to be implemented on paper in as much detail as possible.
-   In the code, modularise each part as much as possible into functions, structs or classes.
-   Concepts that may be reused can be converted into a single uniform form for easier handling: for example, if a problem gives you "YY-MM-DD hour:minute", extract it into a function and convert it to seconds – this reduces confusion.
-   Debug piece by piece. The advantage of modularisation is precisely that each part can be debugged separately.
-   Think clearly while coding; do not write whatever comes to mind, but follow the steps written down on paper.

In fact, the steps above are very helpful when solving other kinds of problems as well.

## Worked example

???+ note "[Climbing Worm](https://open.kattis.com/problems/climbingworm)"
    A worm of negligible length is at the bottom of a well $n$ inches deep. Each time it climbs up $u$ inches, but then it must rest before it can climb again. While resting it slides down $d$ inches. It then repeats the process of climbing and resting. How many climbs does the worm need at minimum to get out of the well? If the worm reaches exactly the top of the well after a climb, we also consider it to have climbed out.

??? note "Solution idea"
    The problem guarantees that the worm can get out, i.e. $u\ge n$ or $u>d$. Under this condition we can simulate directly. Use a loop to repeat the climbing process, and break out when the height reached is greater than or equal to the depth of the well.

??? note "Sample code"
    === "C++"
        ```cpp
        --8<-- "docs/basic/code/simulate/simulate_1.cpp"
        ```
    
    === "Python"
        ```python
        --8<-- "docs/basic/code/simulate/simulate_1.py"
        ```
    
    === "Java"
        ```java
        --8<-- "docs/basic/code/simulate/simulate_1.java"
        ```

## Exercises

-   ["NOIP2014" Rock-paper-scissors (The Big Bang Theory version) - Universal Online Judge](https://uoj.ac/problem/15)
-   ["OpenJudge 3750" World of Warcraft](http://bailian.openjudge.cn/practice/3750/)
-   ["SDOI2010" Pig Kingdom Kill - LibreOJ](https://loj.ac/problem/2885)
