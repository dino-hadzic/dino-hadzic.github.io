---
title: Interactive problems
---

Interactive problems already appeared at the IOI in the last century. Although in recent years they have not appeared in contests below the provincial-selection level, in 2019 two interactive problems, "P5208 [WC2019] I 君的商店" and "P5473 [NOI2019] I 君的探险", appeared one after another in contests of the NOI series, which may mean that interactive problems are returning to the NOI series.

Interactive problems do not require much algorithmic background and usually have no strict time limit; how good a program is often depends only on the limit on the number of interactions. Therefore, when learning interactive problems, it is recommended to progress gradually by difficulty. If you want to train algorithmic thinking rather than merely learn algorithms, solving interactive problems is a very good way. Although interactive problems usually require few already-mastered algorithms, it is still recommended to try them only after mastering a certain number of algorithms of the advanced (NOIP senior) and provincial-selection level, because by then your algorithmic thinking and breadth of knowledge have reached a certain level. For a basic introduction to interactive problems, see the **OI Wiki** section [Problem types – interactive problems](./problems.md#interactive-problems).

Errors specific to interactive problems:

-   The contestant must flush the buffer after every output, otherwise an Idleness limit exceeded error occurs. In addition, if the problem has multiple test cases and the program can know the answer before reading all the data, it still has to read all the data, otherwise ILE also occurs because the input gets mixed up (you may issue several queries at once and then receive the answers to all of them at once). Also, try not to use fast input.
-   If the program makes too many queries, Codeforces gives a Wrong Answer verdict (but the judging system states the reason for the Wrong Answer), while UVa gives a Protocol Limit Exceeded (PLE) verdict.
-   If the program's interaction format is wrong, UVa gives a Protocol Violation (PV) verdict.

Since input and output in interactive problems are fairly tedious, it is recommended to encapsulate the input and output functions separately.

If during a contest the problem setter provides a grader header (for debugging grader-style interactive problems) or a checker program (for debugging stdio-style interactive problems), debugging an interactive problem is relatively easy, because stress testing interactive problems is much harder than stress testing ordinary problems. Without `testlib.h`, the stdio interaction library for a problem with many interaction details usually takes about 3k of code, plus another 3k for the stress tester, so it takes at least an hour to implement. However, whether or not a debugging program is available, debugging the code of an interactive problem usually requires the contestant to simulate the interaction with the program by hand; therefore interactive problems require the contestant to be able to design a high-quality program, to get it right on the first try as far as possible, and to have strong static debugging skills.

Example problems:

-   [CF679A Bear and Prime 100](https://codeforces.com/problemset/problem/679/A)
-   [CF843B Interactive LowerBound](https://codeforces.com/problemset/problem/843/B)
-   [UOJ206\[APIO2016\]Gap](http://uoj.ac/problem/206)
-   [CF750F New Year and Finding Roots](https://codeforces.com/problemset/problem/750/F)
-   [UVa12731 Mysterious Space Station](https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=823&page=show_problem&problem=4584)

## CF679A Bear and Prime 100

Every prime has exactly two divisors, so we directly enumerate the divisors of the number to be guessed. The limit is at most 20 queries, and when trying to factor larger numbers (such as 92) we find that we need to enumerate primes up to at most $\lfloor\frac{n}{2}\rfloor$. So we first sieve the primes below 50 and query all of them every time.

Since stress testing is easy for this problem, we can simply try every number in the range. We will find that the program cannot handle squares of primes correctly. So we also put in the squares of 2, 3, 5, 7, namely 4, 9, 25, 49 – 19 numbers in total, which fits the problem constraints.

??? note "Reference code"
    ```cpp
    #include <cstdio>
    constexpr int prime[] = {2,  3,  4,  5,  7,  9,  11, 13, 17, 19,
                             23, 25, 29, 31, 37, 41, 43, 47, 49};
    int cnt = 0;
    char res[5];
    
    int main() {
      for (int i : prime) {
        printf("%d\n", i);
        fflush(stdout);
        scanf("%s", res);
        if (res[0] == 'y' && ++cnt == 2) return printf("composite"), 0;
      }
      printf("prime");
      return 0;
    }
    ```

## CF843B Interactive LowerBound

The linked list has at most $5 \times 10 ^ 4$ elements, but we may only make $1999$ queries and can only obtain the element after a given one, so the usual method of traversing the whole list is not available. There is only one way to directly get close to the position of the target element: random sampling.

For $n < 2000$ we simply enumerate; for $n \ge 2000$ we sample 1000 points at random – the expected distance between these points is then very small, so we can start from the largest value smaller than $x$ and walk forward; it can be shown that we obtain the answer before reaching the next sampled point. As soon as we find an element greater than or equal to $x$ during the walk, we can exit immediately.

Although the overall idea is simple, in practice, if you have not learned imperfect randomized algorithms such as simulated annealing, it may well be harder to come up with.

Also, since Codeforces has a hacking mechanism, many people deliberately hack code that does not seed the random number generator, so `srand((size_t)new char)` is needed before `random_shuffle()`.

??? note "Reference code"
    ```cpp
    #include <algorithm>
    #include <cstdio>
    #include <cstdlib>
    constexpr int N = 50005;
    int n, start, x;
    int a[N];
    
    int main() {
      scanf("%d%d%d", &n, &start, &x);
      if (n < 2000) {
        int ans = 2e9;
        for (int i = 1; i <= n; i++) {
          printf("? %d\n", i), fflush(stdout);
          int val, next;
          scanf("%d%d", &val, &next);
          if (val >= x) ans = std::min(ans, val);
        }
        if (ans == 2e9) ans = -1;
        printf("! %d", ans), fflush(stdout);
      } else {
        srand((size_t) new char);
        int p = start, ans = 0;
        for (int i = 1; i <= n; i++) a[i] = i;
        std::random_shuffle(a + 1, a + n + 1);
        for (int i = 1; i <= 1000; i++) {
          printf("? %d\n", a[i]), fflush(stdout);
          int val, next;
          scanf("%d%d", &val, &next);
          if (val < x && val > ans) p = a[i], ans = val;
        }
        while (p != -1 && ans < x) {
          printf("? %d\n", p), fflush(stdout);
          int val, next;
          scanf("%d%d", &val, &next);
          ans = val;
          p = next;
        }
        if (ans < x) ans = -1;
        printf("! %d", ans), fflush(stdout);
      }
      return 0;
    }
    ```

## UOJ206\[APIO2016]Gap

We discuss the two subtasks separately:

1.  Limit on the number of queries.

    Consider the first query. Since we know none of the numbers at the start, we need to query the range $[1, 10 ^ {18}]$ to obtain the maximum and minimum.

    Since the query limit is exactly $\frac{N + 1}{2}$, we think about how every query can obtain values we have not obtained before, so that we get all numbers of the sequence roughly within the allowed number of queries. The method is simple: after each query $[s, t]$, if the values obtained are $mn, mx$, the next query is $[mn + 1, mx - 1]$.

2.  Limit on the size of the query ranges.

    Since the problem requires that the total number of numbers inside the query ranges not exceed $3N$, we think about minimizing the query ranges. The method above is no longer usable, because the total number of numbers inside its query ranges is of order $O(N ^ 2)$. We could consider binary splitting of the value range, but this method is unreliable and can be hacked to $O(N ^ 2)$ in the worst case. So we need a more efficient way to partition the value range that avoids querying points in already-queried ranges again and thereby wasting chances.

    Since the answer is not smaller than $\lfloor\frac{a_n - a_1}{N - 1}\rfloor$, we can partition the value range by this value: let $i$ initially be 0 and $ans$ initially be the value above; each time query $[i, i + ans]$ and update $ans$, then increase $i$ with step $ans$.

    However, this method does not apply well to subtask 1 either, because in the worst case many queries may contain no number at all in their range.

??? note "Reference code"
    ```cpp
    #include <algorithm>
    #include <cstdio>
    
    #include "gap.h"
    
    long long findGap(int T, int N) {
      static long long a[100005] = {}, ans = 0;
      long long s = 0, t = 1e18, s1, t1;
      if (T == 1) {
        int l = 1, r = N;
        while (l <= r) {
          MinMax(s, t, &s1, &t1);
          a[l++] = s1, a[r--] = t1;
          s = s1 + 1, t = t1 - 1;
        }
        for (int i = 2; i <= N; i++) ans = std::max(ans, a[i] - a[i - 1]);
      } else if (T == 2) {
        MinMax(s, t, &s1, &t1);
        ans = (t1 - s1) / (N - 1);
        long long l = s1 + 1, r = t1, last = s1;
        for (long long i = l; i <= r;) {
          MinMax(i, i + ans, &s1, &t1);
          i += ans + 1;
          if (s1 != -1) ans = std::max(ans, s1 - last), last = t1;
        }
      }
      return ans;
    }
    ```

## CF750F New Year and Finding Roots

Seeing the strict requirements $h \le 7$ and at most $16$ queries, we need to make the most of the information obtained from each access very strictly.

For $h \le 4$ we can simply brute-force. For $h > 4$, however, we need a very efficient traversal algorithm.

Random sampling is not a good method, because with random sampling we cannot tell whether we are close enough to the root, and with pure random sampling the probability of hitting the root at least once is $1 - (\frac{2 ^ h - 2}{2 ^ h - 1})$; even after excluding repeated samples, the probability of hitting the root is still very small.

Since $1 \le k \le 3$ and we do not know which side is closer to the root, we consider the worst case: when $k = 3$, the first two traversal directions lead away from the root and only the third one leads toward it. So we must traverse in all three directions.

Consider the two traversal methods, BFS and DFS. Since the BFS search tree may be very large, we prefer DFS. Of course, if we know the current depth and it is small enough that the size of the search tree within that depth range is at most the number of remaining queries, we can use BFS directly.

Knowing the depth of the current node and the direction of the current traversal is a big advantage. However, knowing whether we are currently heading toward the root or toward the leaves is very difficult. With DFS, we only learn the current direction when the traversal reaches the root ($k = 2$) or a leaf ($k = 1$). So we need to know the depth of the current node as far as possible, and we cannot use methods like iterative deepening that stop in the middle of a traversal.

Consider a random initial node; starting from it we may encounter the worst case described above.

If $k = 1$, we immediately know the depth of the current node.

If $k = 2$, the current node is the root.

If $k = 3$, we directly consider DFS in all three directions. Two of the directions lead straight toward the leaves and have traversal paths of equal length; the other direction leads toward the root, but may accidentally turn toward the leaves on the way, so its traversal path is longer. At this point we can compute the depth of the current node.

When $k = 1$ or $k = 3$, we need to consider the longer traversal path. We can find the node of minimum depth on the path (it is necessarily shallower than the initial node). If we mark visited nodes and do not traverse them again, there is only one traversal path starting from that node. Although this path may still lead toward the leaves, it necessarily contains a node shallower than its starting point, and we can repeat the steps above from that node.

Of course, considering the worst case for $h = 7$ (each time we take only one step toward the root and then head straight for the leaves), we find that with DFS alone we need $\frac{(1 + 7) \times 7}{2} = 28$ queries in the worst case. But we already know the depth of the initial node, so we can compute the depths of all traversed nodes and, according to our earlier discussion of BFS, decide whether we can start BFS directly from the shallowest node.

Now we can compute that the worst case needs 17 queries. So we consider removing one node from the search tree (since DFS can only traverse blindly, we consider BFS): when doing a BFS of depth $k$, the search tree has at most $2 ^ k - 1$ nodes, and it may take $2 ^ k - 1$ queries to determine which node has exactly 2 neighbors. However, if we have already queried $2 ^ k - 2$ of these nodes, we know that the last node must be the root.

The optimal solution in the worst case is then: for $h = 7$, DFS from a leaf, each time taking only one step toward the root and then heading straight for the leaves; after 10 queries, the currently known shallowest node has depth 4, and since its parent is known, we start BFS directly from its parent (the search tree has depth 3 and $2 ^ 3 - 1 = 7$ nodes). After $2 ^ 3 - 2 = 6$ queries in the BFS, we determine that the last node of the BFS search tree is the root.

Thus our algorithm fits exactly within 16 queries in the worst case.

??? note "Reference code"
    ```cpp
    #include <algorithm>
    #include <cstdio>
    #include <queue>
    #include <vector>
    using namespace std;
    constexpr int N = 256 + 5;
    int T, h, chance;
    bool ok;
    vector<int> to[N], path;
    
    bool read(int x) {
      if (to[x].empty()) {
        printf("? %d\n", x), fflush(stdout);
        int k, t;
        scanf("%d", &k);
        if (k == 0) exit(0);
        for (int i = 0; i < k; i++) {
          scanf("%d", &t);
          to[x].push_back(t);
        }
        if (k == 2) {
          printf("! %d\n", x), fflush(stdout);
          return ok = true;
        }
        chance--;
      }
      return false;
    }
    
    bool dfs(int x) {
      if (to[x].empty()) path.push_back(x);
      if (read(x)) return true;
      for (int i : to[x])
        if (to[i].empty()) return dfs(i);
      return false;
    }
    
    void bfs(int s, int k) {
      queue<int> q;
      for (int i : to[s])
        if (to[i].empty()) q.push(i);
      for (int i = 1; i < k; i++) {
        int x = q.front();
        q.pop();
        if (read(x)) return;
        for (int j : to[x])
          if (to[j].empty()) q.push(j);
      }
      for (int i = 1; i < k; i++) {
        int x = q.front();
        q.pop();
        if (read(x)) return;
      }
      printf("! %d\n", q.front()), fflush(stdout);
    }
    
    int main() {
      for (scanf("%d", &T); T--;) {
        ok = false;
        for (int i = 0; i < N; i++) to[i].clear();
        chance = 16;
        scanf("%d", &h);
        if (h == 0) exit(0);
        vector<int> long_path;
        if (read(1)) continue;
        int root, dep;
        if (to[1].size() == 1)
          root = 1, dep = h;
        else {
          for (int i : to[1]) {
            path.clear();
            if (dfs(i)) break;
            if (path.size() > long_path.size()) swap(path, long_path);
          }
          if (ok) continue;
          dep = h - (path.size() + long_path.size()) / 2;
          root = long_path.at((long_path.size() - (h - dep)) - 1);
        }
        while ((1 << (dep - 1)) - 2 > chance) {
          path.clear();
          if (dfs(root)) break;
          dep = h - (h - dep + path.size()) / 2;
          root = path.at((path.size() - (h - dep)) - 1);
        }
        if (!ok) bfs(root, 1 << (dep - 2));
      }
      return 0;
    }
    ```

## UVa12731 Mysterious Space Station

Since the only feedback is whether we hit a wall when moving, we should consider walking as close to the wall as possible without losing the robot; this has several benefits:

-   When walking along the wall, it is easy to know whether we will hit the wall, so we obtain as much information as possible.
-   The cells along the wall never contain a portal, so the robot cannot get lost.

Therefore, if we know the robot may be at some position along the wall and want to determine whether it really is there, we can use the ["wall follower" rule](https://en.wikipedia.org/wiki/Maze_solving_algorithm). By a topological principle, in a maze with walls on both sides, if we enter at the entrance and always keep one hand on the same wall, we are guaranteed to find the exit. Since the wall in this problem is closed, it suffices to walk along the path next to the wall to be guaranteed to return to the starting point without hitting a wall. Moreover, since the path along the wall is the maximal closed loop on the map, the actual code does not need to deliberately bump into walls to ensure the robot is at the wall; we can mark the wall path on the map. And as soon as we hit a wall, we should quickly go back the way we came, which avoids losing the robot and reduces the number of steps.

From this we derive a trial-and-error method for determining whether the robot is on a specific cell: move the robot onto the wall path without stepping on unknown cells or known portals, then walk one lap along the wall path. If we do not hit a wall during this process, we can be sure the robot really is on the specific cell.

Using the method above, we can first mark all unknown cells on the map, then check each unknown cell from top to bottom and left to right to see whether it is a portal. First walk to the cell above the unknown cell, then move down and then left. Then use the method above to check whether the robot is to the left of the unknown cell. If not, the robot is not where it should be, i.e., the unknown cell is a portal.

After finding the unknown cells, we need to determine the pairing of the 2k unknown cells; the method is simple: brute-force pairing suffices. Since $k \le 5$, at most $9 + 7 + 5 + 3$ trials are needed. For comparison, checking all unknown cells on the map takes at most $121 - 40$ trials.

The code below currently only passes the mirror problem on UOJ: [#247.【Rujia Liu's Present 7】Mysterious Space Station](http://uoj.ac/problem/247), and fails the original UVa problem. Even after modifying Rujia Liu's reference solution from UOJ it still fails, and Rujia Liu cannot be contacted for the time being. So the code below is based on UOJ.

That said, Rujia Liu's reference solution is of much higher quality than the code below; the [reference solution that passes the UOJ mirror problem](http://uoj.ac/submission/105789) can be viewed on UOJ. On the same data, the reference solution uses far fewer moves.

??? note "Reference code"
    ```cpp
    #include <algorithm>
    #include <cstdio>
    #include <cstring>
    #include <iostream>
    #include <queue>
    #include <stack>
    
    #define Wall 0
    #define Unknown 1
    #define Space 2
    #define Gate 3
    #define Path 4
    
    const int N = 20;
    const int dir[8][2] = {{0, 1},  {1, 0}, {0, -1}, {-1, 0},
                           {-1, 1}, {1, 1}, {1, -1}, {-1, -1}};
    const char dirs[5] = "ESWN";
    int n, m, k;
    int a[N][N], id[N][N];
    
    struct point {
      int x, y;
    
      point(int x = 0, int y = 0) : x(x), y(y) {}
    
      bool operator==(const point& tmp) const { return x == tmp.x && y == tmp.y; }
    
      bool operator!=(const point& tmp) const { return !(*this == tmp); }
    
      point side(int d) const { return point(x + dir[d][0], y + dir[d][1]); }
    
      int check(int d) { return a[x + dir[d][0]][y + dir[d][1]]; }
    
      int id() { return ::id[x][y]; }
    } start;
    
    std::vector<std::pair<point, int>> path;
    std::pair<point, point> ans[N];
    std::pair<point, bool> vis[N];
    
    bool walk(int d) {
      printf("MoveRobot %c\n", dirs[d]);
      fflush(stdout);
      int ret;
      scanf("%d", &ret);
      return ret;
    }
    
    bool walk(int d, std::stack<int>& st) {
      if (walk(d)) {
        st.push(d);
        return true;
      }
      return false;
    }
    
    bool read() {
      if (scanf("%d%d%d", &n, &m, &k) != 3) return false;
      if (n == 0) return false;
      memset(a, 0, sizeof(a));
      for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++) {
          char c;
          std::cin >> c;
          if (c == 'S') start = point(i, j);
          if (c == '*')
            a[i][j] = Wall;
          else
            a[i][j] = Unknown;
        }
      return true;
    }
    
    void answer() {
      for (int i = 0; i < k; i++)
        printf("Answer %d %d\n", ans[i].first.id(), ans[i].second.id());
      fflush(stdout);
    }
    
    // Wall follower: since the Path along the wall is a maximal closed loop,
    // it suffices not to hit any obstacle while walking along the Path
    void wall_follower_init(point x, int last, int wallside, point s) {
      if (x == s && !path.empty()) return;
      if (x.check(wallside) == Path) {
        path.push_back(std::make_pair(x, wallside));
        wall_follower_init(x.side(wallside), wallside, last ^ 2, s);
      } else if (x.check(last) == Wall) {
        for (int i = 0; i < 4; i++)
          if (i != (last ^ 2) && x.check(i) != Wall) {
            path.push_back(std::make_pair(x, i));
            wall_follower_init(x.side(i), i, last, s);
            return;
          }
      } else {
        path.push_back(std::make_pair(x, last));
        wall_follower_init(x.side(last), last, wallside, s);
      }
    }
    
    void init() {
      int cnt = 1;
      for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++) {
          if (a[i][j] == Unknown) {
            id[i][j] = cnt++;
            for (int k = 0; k < 8; k++)
              if (point(i, j).check(k) == Wall) {
                a[i][j] = Path;
                break;
              }
          } else
            id[i][j] = 0;
        }
      path.clear();
      int wallside = 0, last = 0;
      for (int i = 0; i < 4; i++)
        if (start.check(i) == Wall) {
          wallside = i;
          break;
        }
      for (int i = 0; i < 4; i++)
        if (start.check(i) == Path && i != (wallside ^ 2)) {
          last = i;
          break;
        }
      wall_follower_init(start, last, wallside, start);
    }
    
    void undo(std::stack<int>& st) {
      while (!st.empty()) walk(st.top() ^ 2), st.pop();
    }
    
    bool wall_follower(point x) {
      std::stack<int> st;
      bool ok = true;
      int i = 0;
      while (i < path.size() && path[i].first != x) i++;
      for (int j = i; ok && j < path.size(); j++) {
        if (walk(path[j].second))
          st.push(path[j].second);
        else
          ok = false;
      }
      for (int j = 0; ok && j < i; j++) {
        if (walk(path[j].second))
          st.push(path[j].second);
        else
          ok = false;
      }
      if (!ok) undo(st);
      return ok;
    }
    
    // Make sure we are currently at x: feeling our way step by step, it suffices
    // to reach Path along directions that avoid obstacles, unknown cells and
    // portals. Used when finding portals and pairing them
    void bfs(point s, point t, std::vector<int>& v) {
      static int map[N][N] = {};
      memset(map, -1, sizeof(map));
      std::queue<point> q;
      map[s.x][s.y] = 4;
      q.push(s);
      while (!q.empty()) {
        point x = q.front();
        q.pop();
        if (x == t) break;
        for (int i = 0; i < 4; i++) {
          point y = x.side(i);
          if ((x.check(i) == Path || x.check(i) == Space) && map[y.x][y.y] == -1) {
            map[y.x][y.y] = i;
            q.push(y);
          }
        }
      }
      for (point x = t; x != s; x = x.side(map[x.x][x.y] ^ 2)) {
        v.push_back(map[x.x][x.y]);
      }
      std::reverse(v.begin(), v.end());
    }
    
    bool move(point s, point t, std::stack<int>& st) {  // used when near a portal
      static std::vector<int> v;
      v.clear();
      bfs(s, t, v);
      for (int i : v)
        if (!walk(i, st)) return false;
      return true;
    }
    
    // move toward the wall as fast as possible
    bool make_sure(point x, int last) {
      if (a[x.x][x.y] == Path) return wall_follower(x);
      for (int i = 0; i < 4; i++)
        if ((x.check(i) == Path || x.check(i) == Space) && i != (last ^ 2)) {
          if (!walk(i)) return false;
          bool ret = make_sure(x.side(i), i);
          walk(i ^ 2);
          return ret;
        }
      return false;
    }
    
    void find_gate() {
      int cnt = 0;
      std::stack<int> st;
      for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
          if (cnt == k * 2 && a[i][j] == Unknown)
            a[i][j] = Space;
          else if (a[i][j] == Unknown) {
            bool ok = true;
            if (!move(start, point(i - 1, j), st))
              ok = false;
            else if (!walk(1, st))
              ok = false;
            else if (!walk(2, st))
              ok = false;
            else if (!make_sure(point(i, j - 1), -1))
              ok = false;
            if (!ok) {
              vis[cnt++] = std::make_pair(point(i, j), false);
              a[i][j] = Gate;
              for (int k = 0; k < 8; k++) {
                point y = point(i, j).side(k);
                if (point(i, j).check(k) == Unknown) a[y.x][y.y] = Space;
              }
            } else
              a[i][j] = Space;
            undo(st);
          }
    }
    
    void make_gate_pair() {
      int cnt = 0;
      std::stack<int> st;
      for (int i = 0; i < k * 2; i++)
        if (!vis[i].second)
          for (int j = 0; !vis[i].second && j < k * 2; j++)
            if (j != i && !vis[j].second) {
              bool ok = true;
              if (!move(start, vis[i].first.side(2), st))
                ok = false;
              else if (!walk(0, st))
                ok = false;
              else if (!make_sure(vis[j].first.side(0), -1))
                ok = false;
              if (ok) {
                ans[cnt++] = std::make_pair(vis[i].first, vis[j].first);
                vis[i].second = vis[j].second = true;
              }
              undo(st);
            }
    }
    
    int main() {
      while (read()) {
        init();
        find_gate();
        make_gate_pair();
        answer();
      }
      return 0;
    }
    ```

## Exercises

-   [Rujia Liu's contest dedicated to interactive problems, Rujia Liu's Present 7, is of very high quality and recommended.](https://onlinejudge.org/contests/328-9976a2e2/)
-   [P5473\[NOI2019\]I 君的探险](https://www.luogu.com.cn/problem/P5473)
-   [P5208\[WC2019\]I 君的商店](https://www.luogu.com.cn/problem/P5208)

## References and further reading

-   [Implementing interactive problems for an online judge with Linux pipes (Chinese)](https://www.cnblogs.com/tsreaper/p/pipe-interactive.html)
