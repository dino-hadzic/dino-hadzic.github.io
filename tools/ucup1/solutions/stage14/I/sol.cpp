// I. LaLa and Spirit Summoning
// Stupanj slobode generičkog ravninskog okvira = 2N - rang(skupa štapova) u
// generičkom 2D matroidu krutosti (Lamanov uvjet: |T| <= 2|V(T)| - 3 za svaki
// neprazni podskup T). Uvjet "boje različite" je particijski matroid, pa tražimo
// najveći zajednički nezavisan skup: presjek matroida (najkraći augmentirajući
// put u grafu zamjena). Orakl za krutost je (2,3)-igra kamenčićima (pebble game):
// ako se za brid (u,v) ne mogu skupiti 4 kamenčića, brid je ovisan, a njegov
// fundamentalni krug čine bridovi razapeti skupom Reach(u,v).
#include <bits/stdc++.h>
using namespace std;

int N, M;
vector<int> eu, ev, ec;

// stanje igre kamenčićima nad trenutnim skupom I
vector<int> peb, efrom, eto;
vector<vector<int>> inc;        // incidentni bridovi iz I (oba kraja)
vector<int> parentEdge, visitStamp;
int stampCounter = 0;

// DFS iz s po usmjerenim bridovima do vrha s kamenčićem (osim vrha 'other');
// ako ga nađe, okrene put i preseli kamenčić na s. Vraća uspjeh.
bool grabPebble(int s, int other) {
    stampCounter++;
    vector<int> st = {s};
    visitStamp[s] = stampCounter; parentEdge[s] = -1;
    int found = -1;
    while (!st.empty() && found < 0) {
        int x = st.back(); st.pop_back();
        if (x != s && x != other && peb[x] > 0) { found = x; break; }
        for (int id : inc[x]) {
            if (efrom[id] != x) continue;
            int y = eto[id];
            if (visitStamp[y] == stampCounter) continue;
            visitStamp[y] = stampCounter; parentEdge[y] = id;
            st.push_back(y);
        }
    }
    if (found < 0) return false;
    peb[found]--; peb[s]++;
    for (int x = found; x != s;) {                 // okretanje puta
        int id = parentEdge[x];
        int px = efrom[id];
        swap(efrom[id], eto[id]);
        x = px;
    }
    return true;
}

// pokušaj skupiti 4 kamenčića na {u, v}
bool collect4(int u, int v) {
    while (peb[u] + peb[v] < 4) {
        if (grabPebble(u, v)) continue;
        if (grabPebble(v, u)) continue;
        return false;
    }
    return true;
}

void insertEdge(int id) {                         // pretpostavka: nezavisan
    int u = eu[id], v = ev[id];
    bool ok = collect4(u, v);
    assert(ok);
    peb[u]--;
    efrom[id] = u; eto[id] = v;
    inc[u].push_back(id); inc[v].push_back(id);
}

// skup vrhova dostupnih iz {u, v} (nakon neuspjelog skupljanja)
void reach(int u, int v, vector<char>& mark) {
    stampCounter++;
    vector<int> st = {u, v};
    visitStamp[u] = visitStamp[v] = stampCounter;
    mark.assign(N, 0); mark[u] = mark[v] = 1;
    while (!st.empty()) {
        int x = st.back(); st.pop_back();
        for (int id : inc[x]) {
            if (efrom[id] != x) continue;
            int y = eto[id];
            if (visitStamp[y] == stampCounter) continue;
            visitStamp[y] = stampCounter; mark[y] = 1;
            st.push_back(y);
        }
    }
}

int main() {
    if (scanf("%d %d", &N, &M) != 2) return 0;
    eu.resize(M); ev.resize(M); ec.resize(M);
    for (int i = 0; i < M; i++) scanf("%d %d %d", &eu[i], &ev[i], &ec[i]);
    vector<char> inI(M, 0);
    peb.assign(N, 0); efrom.assign(M, -1); eto.assign(M, -1);
    inc.assign(N, {}); parentEdge.assign(N, -1); visitStamp.assign(N, 0);
    vector<int> colorOwner(M, -1);                // colorOwner[c] = brid iz I te boje

    while (true) {
        // 1) izgradi igru kamenčićima za I
        fill(peb.begin(), peb.end(), 2);
        for (auto& l : inc) l.clear();
        vector<int> I;
        for (int i = 0; i < M; i++) if (inI[i]) I.push_back(i);
        for (int id : I) insertEdge(id);
        fill(colorOwner.begin(), colorOwner.end(), -1);
        for (int id : I) colorOwner[ec[id]] = id;

        // 2) graf zamjena: y -> x ako I - x + y nezavisan u matroidu krutosti,
        //    x -> y ako I - x + y nezavisan u particijskom matroidu
        vector<char> inX2(M, 0);
        vector<vector<int>> arcM2(M);             // arcM2[y] = popis x
        vector<char> mark;
        for (int y = 0; y < M; y++) {
            if (inI[y]) continue;
            if (collect4(eu[y], ev[y])) { inX2[y] = 1; continue; }
            reach(eu[y], ev[y], mark);
            for (int x : I) if (mark[eu[x]] && mark[ev[x]]) arcM2[y].push_back(x);
        }
        vector<vector<int>> byColor(M);
        for (int y = 0; y < M; y++) if (!inI[y]) byColor[ec[y]].push_back(y);

        // 3) BFS od X1 = {y: boja slobodna} do X2
        vector<int> dist(M, -1), par(M, -1);
        deque<int> q;
        for (int y = 0; y < M; y++) if (!inI[y] && colorOwner[ec[y]] < 0) { dist[y] = 0; q.push_back(y); }
        int target = -1;
        while (!q.empty() && target < 0) {
            int z = q.front(); q.pop_front();
            if (!inI[z]) {
                if (inX2[z]) { target = z; break; }
                for (int x : arcM2[z]) if (dist[x] < 0) { dist[x] = dist[z] + 1; par[x] = z; q.push_back(x); }
            } else {
                for (int y : byColor[ec[z]]) if (dist[y] < 0) { dist[y] = dist[z] + 1; par[y] = z; q.push_back(y); }
            }
        }
        if (target < 0) break;
        for (int z = target; z >= 0; z = par[z]) inI[z] ^= 1;   // augmentacija = simetrična razlika
    }
    int r = 0;
    for (int i = 0; i < M; i++) r += inI[i];
    printf("%d\n", 2 * N - r);
    return 0;
}
