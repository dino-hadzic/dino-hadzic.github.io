---
title: Hill climbing
---

## Introduction

Hill climbing is a method of local best-choice selection that uses heuristics; it is an improvement of depth-first search that uses feedback information to help make decisions about generating solutions.

Put simply: when we currently cannot reach the optimal solution directly, but we can tell which of two solutions is better, we generate a new candidate solution based on some feedback information.

Therefore, hill climbing each time looks for a new solution near the best solution $x$ found so far. If the new solution $x'$ is better, we move to $x'$; otherwise we stay.

For unimodal functions this algorithm obviously works.

Q: If we already know the function is unimodal, why not use ternary search?

A: The advantage of hill climbing is that when you do not know how to write the intended solution (common in nasty computational geometry and nasty math problems), or when the state has many dimensions so that a divide-and-conquer approach is not easy to write (example 2 can be solved correctly with binary search), you can obtain the optimal solution by very brute-force computation.

However, for most functions that need to be optimized, hill climbing easily gets stuck in a local optimum, as in the figure below (the optimal solution is $\color{green}{\Uparrow}$, while the optimum hill climbing may find is $\color{red}{\Downarrow}$).

![](./images/hill-climbing.png)

## Concrete implementation

Hill climbing usually introduces a temperature parameter (similar to simulated annealing). By analogy, hill climbing is like a drunk rabbit hopping on a mountain: each time it jumps toward the place it believes is higher (which is often only an inaccurate guess of the trend); obviously it may reach the summit in one jump, but it may also overshoot and tumble over to the other side. That is fine, though: after tumbling over, the rabbit will jump back. Clearly this process is quite useless and the rabbit would never find its way, so during the process the rabbit sobers up and becomes more cautious with each jump, jumping a little less, in order to reach a suitable optimal point.

The rabbit gradually sobering up is the cooling process, i.e. the temperature parameter keeps decreasing during the climb.

About cooling: the cooling parameter is a constant slightly less than $1$, usually chosen from $[0.985, 0.999]$.

## Example problems

???+ example "[「JSOI2008」球形空间产生器 (Spherical Space Generator)](https://www.luogu.com.cn/problem/P4035)"
    Given $n + 1$ points in $n$-dimensional space that are known to lie on the same $n$-dimensional sphere, find the center of the sphere. $n \leq 10$, the absolute values of the coordinates do not exceed $20000$.

??? note "Solution"
    Clearly a unimodal function, so it can be solved with hill climbing. The algorithm for this problem:
    
    1.  Initialize the center as the centroid of the given points (i.e. each of its coordinates is the average of the corresponding coordinates of all given points), to reduce the amount of search.
    2.  For the current center, compute the average Euclidean distance from each known point to this center.
    3.  Iterate over all known points. Keep a change value $\textit{cans}$ (recorded separately for each dimension): for the Euclidean distance of each point, if it is greater than the average, add the difference to the change value, otherwise subtract it. In fact there is no need to compare at all: just ignore the absolute value and compute directly with the coordinates. This process can be visualized as a new center being pushed around in space: when it meets a point that is too far, it is pulled a bit toward the point, and when it meets a point that is too close, it is pushed a bit away from the point.
    4.  Multiply the recorded $\textit{cans}$ by the temperature, update the center, and go back to step 2.
    5.  Stop when the temperature is below some given threshold.
    
    Therefore, when updating the center we must not add the change value directly, but the product of the change value and the temperature.
    
    Not every hill climbing problem can be solved concretely with a temperature; this is just one example.

??? note "Reference code"
    ```cpp
    --8<-- "docs/misc/code/hill-climbing/hill-climbing_1.cpp"
    ```

???+ example "[「BZOJ 3680」吊打 XXX (Beat Up XXX)](https://hydro.ac/p/bzoj-P3680)"
    Find the weighted (generalized) Fermat point of $n$ points.

??? note "Solution"
    The framework is similar, with a bit of physics.

??? note "Reference code"
    ```cpp
    --8<-- "docs/misc/code/hill-climbing/hill-climbing_2.cpp"
    ```

## Optimization

An easy idea: to get as good an answer as possible, we can run hill climbing several times. Options include changing the initial state, changing the cooling parameter, changing the initial temperature, etc.; then keep a global best solution to record the answer. After each run of hill climbing, update the global optimum.

A possible problem with this is exceeding the time limit; in a real contest, generate large test data by hand and tune the parameters on it.

## Disadvantages

The disadvantage of hill climbing was already mentioned above: it easily gets stuck in a local optimum. When the objective function is not unimodal, this disadvantage is fatal. That is why we introduce [**simulated annealing**](./simulated-annealing.md).
