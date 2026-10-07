---
title: Optimizations
---

## Preface

DFS (depth-first search) is a common algorithm and most problems can be solved with DFS, but in most cases it is only a "partial-score" algorithm; brute-force search is rarely the intended solution, because the time complexity of DFS is very high. (If you have not learned DFS yet, please catch up on that lesson first.)

If it cannot be the full solution, let us at least grab a few more points. This article introduces some practical optimization techniques (commonly called "pruning").

First, a template for depth-first search; the later templates will be modifications of it.

```cpp
int ans = worst case, now;  // now is the current answer

void dfs(input values) {
  if (target reached) ans = the better of the current and the existing answer;
  for (iterate over all possibilities)
    if (feasible) {
      perform operation;
      dfs(smaller problem);
      undo operation;
    }
}
```

Here `ans` may also be a record of the solution; then "the better of the current and the existing answer" becomes outputting the solution.

## Pruning methods

The three most common kinds of pruning are memoized search, optimality pruning, and feasibility pruning.

### Memoized search

Since in a search the same input values often lead to the same answer, we can memorize them in an array; see [memoized search](../dp/memo.md) for details.

**Template:**

```cpp
int g[MAXN];  // memoization array
int ans = worst case, now;

void dfs f(input values) {
  if (g[size] != invalid value) return;  // or record the answer, depending on the situation
  if (target reached) ans = the better of the current and the existing answer;  // output the answer, depending on the situation
  for (iterate over all possibilities)
    if (feasible) {
      perform operation;
      dfs(smaller problem);
      undo operation;
    }
}

int main() {
  // ...
  memset(g, invalid value, sizeof(g));  // initialize the memoization array
  // ...
}
```

### Optimality pruning

Another cause of slow searches is continuing to search when the current answer is already worse than the existing one. So we just need to check whether the current answer is already worse than the existing one.

**Template:**

```cpp
int ans = worst case, now;

void dfs(input values) {
  if (now is worse than ans) return;
  if (target reached) ans = the better of the current and the existing answer;
  for (iterate over all possibilities)
    if (feasible) {
      perform operation;
      dfs(smaller problem);
      undo operation;
    }
}
```

### Feasibility pruning

Continuing to search when the current solution is already unusable is also a cause of slowness.

**Template:**

```cpp
int ans = worst case, now;

void dfs(input values) {
  if (current solution is already unusable) return;
  if (target reached) ans = the better of the current and the existing answer;
  for (iterate over all possibilities)
    if (feasible) {
      perform operation;
      dfs(smaller problem);
      undo operation;
    }
}
```

## Pruning ideas

There are many pruning ideas, and most have to be analyzed for the specific problem; here we briefly introduce a few common ones.

-   Extreme-case method: consider the extreme case; if even the most extreme (most ideal) case cannot satisfy the conditions, then the result of the actual search certainly will not be better.

-   Adjustment method: by comparing subtrees, prune duplicate subtrees and subtrees that clearly are not the most "promising".

-   Mathematical methods: for example, using connected components in graph theory, analyzing modular equations in number theory, estimating lower bounds with inequalities, and so on.

## Example

???+ note "Job assignment problem"
    There are $n$ ($1 \leq n \leq  15$) jobs to be assigned to $n$ people, each of whom completes one job. The time person $i$ needs to complete job $k$ is a positive integer $t_{i,k}$ ($1 \leq t_{i,k} \leq 10^4$), where $1 \leq i, k \leq n$. Find an assignment that minimizes the total time needed to complete these $n$ jobs.

Since every person must be assigned a job, we can create a two-dimensional array `time[i][j]` representing the time person $i$ needs for job $j$. Using a loop, we assign jobs starting from person 1 until everyone has one. When assigning a job to person $i$, we loop over the jobs and check whether each has already been assigned; if not, we assign it to person $i$, otherwise we check the next job. A one-dimensional array `is_working[j]` records whether job $j$ has been assigned: `is_working[j]=0` if not, `is_working[j]=1` otherwise. Using the idea of backtracking, after the loop over workers ends we return to the previous worker, cancel the job assigned this time, and assign the next job until an assignment succeeds. In this way, backtracking all the way to worker 1, we obtain all feasible solutions.

Checking a job assignment really means checking that, when a feasible solution is obtained, the first-dimension indices of the two-dimensional array are pairwise distinct and so are the second-dimension indices. But we want the minimum total time for completing the $n$ jobs, i.e., the feasible solution with the smallest total time, so we define another global variable `cost_time_total_min` for the smallest total time found so far; initially `cost_time_total_min` is the sum of `time[i][i]`, i.e., the sum of the times on the diagonal. When everyone has been assigned a job, compare `count` with `cost_time_total_min`: if `count` is smaller than `cost_time_total_min`, a better solution has been found, and we assign `count` to `cost_time_total_min`.

Considering the efficiency of the algorithm, there is one more pruning optimization to do here. Whenever the partial cost `count` is computed, if `count` is already larger than `cost_time_total_min`, there is no need to continue assigning, because the solution obtained this way certainly will not be optimal.

??? note "Sample code"
    ```cpp
    --8<-- "docs/search/code/opt/opt_1.cpp"
    ```
