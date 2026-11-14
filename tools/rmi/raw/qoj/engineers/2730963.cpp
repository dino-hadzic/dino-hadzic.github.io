#include <bits/stdc++.h>
#include "engineers.h"

using namespace std;

const int maxn = 200'012;

vector<int> g[maxn];
int tin[maxn], tout[maxn], c[maxn];
set<pair<int, int>> ch[maxn];
int n, d, timer;

void calc(int v, int p) {
    tin[v] = ++timer;
    
    for(int to : g[v]) {
        if(to != p) {
            calc(to, v);
            ch[v].insert({tout[to], to});
        }
    }

    tout[v] = timer;
}

int solve(int N, int D, std::vector<int> C, std::vector<int> P, std::vector<int> Q) {
    n = N, d = D;
    for(int i = 0; i < n - 1; i++) {
        g[P[i]].push_back(Q[i]);
        g[Q[i]].push_back(P[i]);
    }

    calc(0, -1);

    vector<int> p(n);

    for(int i = 0; i < n; i++) {
        c[i] = C[i];
        p[i] = i;
    }

    sort(p.begin(), p.end(), [](int x, int y) {
        return c[x] < c[y];
    });

    vector<int> bad(n, 0);
    set<pair<int, int>> s;

    int cur = 0;

    auto add = [&](int x) -> void {
        auto it = s.upper_bound(make_pair(tin[x], x));

        if(it != s.end() && it -> first <= tout[x]) {
            bad[x] = 1;
        }

        if(it != s.begin()) {
            it--;

            if(tin[x] <= tout[it -> second] && !bad[it -> second]) {
                cur--;
                bad[it -> second] = true;
            }
        }

        cur += (bad[x] == 0);
        
        s.insert({tin[x], x});
    };

    auto del = [&](int x) -> void {
        cur -= (bad[x] == 0);
        bad[x] = 0;
        s.erase({tin[x], x});

        auto it = s.upper_bound(make_pair(tin[x], x));
        
        if(it != s.begin()) {
            auto pos = it;
            it--;

            int v = it -> second;

            if((pos == s.end() || pos -> first > tout[v]) && bad[v]) {
                bad[v] = false;
                cur++;
            }
        }
    };

    auto get = [&]() -> int {
        if((int)s.size() <= 1) {
            return (int)s.size();
        }

        int ans = cur;

        int ver = s.begin() -> second;

        if(bad[ver]) {
            auto it = ch[ver].lower_bound(make_pair(s.rbegin() -> first, 0));
            auto ft = s.begin();
            ft++;
            
            if(it != ch[ver].end() && tin[it -> second] <= ft -> first) {
                ans++;
            }
        }

        return ans;
    };

    for(int i = 0; i < n; i++) {
        add(i);
    }

    int ans = n;
    for(int i = 0, j = 0; i < n; i++) {
        del(p[i]);
        
        while(c[p[i]] - c[p[j]] > d) {
            add(p[j]);
            j++;
        }

        ans = min(ans, get());
    }

    return (ans + 1) / 2;
}