// H. LaLa and Harvesting – službeni pristup
// Graf = kaktus + ciklus kroz listove DFS-stabla + "gusto" stablo s K bridova.
// 1. Kaktus + ciklus listova ima stablastu dekompoziciju širine <= 4:
//    Halinova dekompozicija (vrh, roditelj, prvi i zadnji list podstabla) u koju
//    za svaki vrh dodamo vrh ciklusa kaktusa najbliži korijenu (t(v)).
// 2. Unutarnji vrhovi stabla treće faze (stupanj >= 12) čine vrhovni pokrivač
//    tog stabla veličine <= (K-1)/11 <= 9; dodamo ih u svaku vreću -> širina <= 13.
// 3. Najteži nezavisan skup dinamikom po vrećama (bitmaske podskupova vreće)
//    uz rekonstrukciju.  Složenost O(N * 2^14 * 14).
#include <bits/stdc++.h>
using namespace std;

int n, m;
vector<vector<int>> cadj;              // susjedi u kaktusu, u redoslijedu ulaza
vector<int> par, dep, pre, topOf;      // topOf[v] = vrh najbliži korijenu na ciklusu brida (v, par v), ili -1
vector<vector<int>> ch;                // djeca u DFS-stablu, u DFS-redoslijedu
vector<char> vis;

void dfs(int v) {
    vis[v] = 1; pre.push_back(v);
    for (int w : cadj[v]) {
        if (!vis[w]) { par[w] = v; dep[w] = dep[v] + 1; ch[v].push_back(w); dfs(w); }
        else if (w != par[v] && dep[w] < dep[v])
            for (int x = v; x != w; x = par[x]) topOf[x] = w;   // povratni brid v -> predak w
    }
}

struct Bag { vector<int> v; vector<int> kids; };
vector<Bag> bags;
int newBag(vector<int> vs) {
    vs.erase(remove(vs.begin(), vs.end(), -1), vs.end());
    sort(vs.begin(), vs.end()); vs.erase(unique(vs.begin(), vs.end()), vs.end());
    bags.push_back({vs, {}});
    return (int)bags.size() - 1;
}

int main() {
    if (scanf("%d %d", &n, &m) != 2) return 0;
    vector<int> T(n);
    for (auto &t : T) scanf("%d", &t);
    cadj.assign(n, {});
    vector<bitset<500>> adj(n);
    for (int i = 0; i < m; i++) {
        int u, v; scanf("%d %d", &u, &v);
        cadj[u].push_back(v); cadj[v].push_back(u);
        adj[u][v] = adj[v][u] = 1;
    }
    int k; scanf("%d", &k);
    vector<int> deg3(n, 0), x0(1, -1);
    for (int i = 0; i < k; i++) {
        int x, y; scanf("%d %d", &x, &y);
        adj[x][y] = adj[y][x] = 1; deg3[x]++; deg3[y]++;
        if (i == 0) x0[0] = x;
    }

    // DFS-stablo kaktusa iz vrha 0
    par.assign(n, -1); dep.assign(n, 0); topOf.assign(n, -1); ch.assign(n, {}); vis.assign(n, 0);
    dfs(0);

    // listovi (stupanj 1 u stablu; korijen s jednim djetetom je list) u DFS-poretku -> ciklus
    vector<int> leaves;
    for (int v : pre)
        if ((v == 0 && ch[v].size() == 1) || (v != 0 && ch[v].empty())) leaves.push_back(v);
    int l = leaves.size();
    for (int i = 0; i < l; i++) {
        int a = leaves[i], b = leaves[(i + 1) % l];
        adj[a][b] = adj[b][a] = 1;
    }

    // a[v], b[v] = prvi i zadnji list u podstablu vrha v (list je i sam korijen ako je list)
    vector<int> A(n), B(n);
    for (int i = n - 1; i >= 0; i--) {
        int v = pre[i];
        bool leaf = (v == 0 && ch[v].size() == 1) || (v != 0 && ch[v].empty());
        A[v] = leaf ? v : A[ch[v].front()];
        B[v] = ch[v].empty() ? v : B[ch[v].back()];
    }

    // vrhovni pokrivač stabla treće faze: unutarnji vrhovi (ili x0 ako je K = 1)
    vector<int> cover;
    for (int v = 0; v < n; v++) if (deg3[v] >= 2) cover.push_back(v);
    if (cover.empty()) cover = x0;

    // stablasta dekompozicija
    vector<int> Z(n);
    for (int v = 0; v < n; v++) {
        vector<int> vs = {v, par[v], A[v], B[v], topOf[v]};
        vs.insert(vs.end(), cover.begin(), cover.end());
        Z[v] = newBag(vs);
    }
    for (int v = 0; v < n; v++) {
        int kc = ch[v].size();
        if (kc == 0) continue;
        int prev = Z[v];
        for (int i = 0; i < kc; i++) {
            int c = ch[v][i];
            vector<int> vs = {v, A[c], B[c], B[v], topOf[v]};
            vs.insert(vs.end(), cover.begin(), cover.end());
            int W = newBag(vs);
            bags[prev].kids.push_back(W);
            bags[W].kids.push_back(Z[c]);
            if (i + 1 < kc) {
                vector<int> ms = {v, B[c], A[ch[v][i + 1]], B[v], topOf[v]};
                ms.insert(ms.end(), cover.begin(), cover.end());
                int Mb = newBag(ms);
                bags[W].kids.push_back(Mb);
                prev = Mb;
            }
        }
    }
    int root = Z[0];
    int nb = bags.size();

    // BFS-poredak vreća, dinamika odozdo prema gore
    vector<int> order, bpar(nb, -1);
    order.push_back(root);
    for (size_t i = 0; i < order.size(); i++)
        for (int c : bags[order[i]].kids) { bpar[c] = order[i]; order.push_back(c); }

    const int NEG = -1000000000;
    vector<vector<int>> f(nb), wt(nb);
    vector<vector<char>> ind(nb);
    vector<int> posIn(n, -1);

    auto prepare = [&](int b) {
        auto &vs = bags[b].v; int s = vs.size();
        vector<int> conf(s, 0);
        for (int i = 0; i < s; i++) for (int j = 0; j < s; j++) if (i != j && adj[vs[i]][vs[j]]) conf[i] |= 1 << j;
        ind[b].assign(1 << s, 1); wt[b].assign(1 << s, 0);
        for (int mask = 1; mask < (1 << s); mask++) {
            int low = __builtin_ctz(mask), rest = mask ^ (1 << low);
            ind[b][mask] = ind[b][rest] && !(conf[low] & rest);
            wt[b][mask] = wt[b][rest] + T[vs[low]];
        }
    };
    // projekcija podskupova djeteta c na pozicije roditelja b: proj[mask], sharedC
    auto projection = [&](int b, int c, vector<int> &proj, int &sharedC) {
        auto &vb = bags[b].v; auto &vc = bags[c].v;
        for (int i = 0; i < (int)vb.size(); i++) posIn[vb[i]] = i;
        int sc = vc.size(); vector<int> mapbit(sc, 0); sharedC = 0;
        for (int j = 0; j < sc; j++) if (posIn[vc[j]] >= 0) { mapbit[j] = 1 << posIn[vc[j]]; sharedC |= 1 << j; }
        for (int i = 0; i < (int)vb.size(); i++) posIn[vb[i]] = -1;
        proj.assign(1 << sc, 0);
        for (int mask = 1; mask < (1 << sc); mask++) {
            int low = __builtin_ctz(mask);
            proj[mask] = proj[mask ^ (1 << low)] | mapbit[low];
        }
    };

    for (int idx = nb - 1; idx >= 0; idx--) {
        int b = order[idx];
        prepare(b);
        int s = bags[b].v.size();
        f[b].assign(1 << s, NEG);
        for (int mask = 0; mask < (1 << s); mask++) if (ind[b][mask]) f[b][mask] = wt[b][mask];
        vector<int> g(1 << s), proj;
        for (int c : bags[b].kids) {
            int sharedC; projection(b, c, proj, sharedC);
            fill(g.begin(), g.end(), NEG);
            int sc = bags[c].v.size();
            for (int mask = 0; mask < (1 << sc); mask++) if (ind[c][mask])
                g[proj[mask]] = max(g[proj[mask]], f[c][mask] - wt[c][mask & sharedC]);
            int sharedB = proj[sharedC];
            for (int mask = 0; mask < (1 << s); mask++) if (ind[b][mask]) f[b][mask] += g[mask & sharedB];
        }
    }

    // rekonstrukcija odozgo prema dolje
    vector<int> chosenMask(nb, 0);
    {
        int best = 0;
        for (int mask = 0; mask < (int)f[root].size(); mask++) if (f[root][mask] > f[root][best]) best = mask;
        chosenMask[root] = best;
    }
    vector<char> take(n, 0);
    for (int idx = 0; idx < nb; idx++) {
        int b = order[idx];
        auto &vs = bags[b].v;
        for (int i = 0; i < (int)vs.size(); i++) if (chosenMask[b] >> i & 1) take[vs[i]] = 1;
        vector<int> proj;
        for (int c : bags[b].kids) {
            int sharedC; projection(b, c, proj, sharedC);
            int target = chosenMask[b] & proj[sharedC];
            int best = -1, bestVal = NEG;
            for (int mask = 0; mask < (int)f[c].size(); mask++)
                if (ind[c][mask] && proj[mask] == target) {
                    int val = f[c][mask] - wt[c][mask & sharedC];
                    if (val > bestVal) { bestVal = val; best = mask; }
                }
            chosenMask[c] = best;
        }
    }

    long long W = 0; vector<int> res;
    for (int v = 0; v < n; v++) if (take[v]) { W += T[v]; res.push_back(v); }
    printf("%lld %d\n", W, (int)res.size());
    for (size_t i = 0; i < res.size(); i++) printf("%d%c", res[i], i + 1 == res.size() ? '\n' : ' ');
    if (res.empty()) printf("\n");
    return 0;
}
