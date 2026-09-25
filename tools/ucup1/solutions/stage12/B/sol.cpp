// B - Magical Wallet
// dp[j] = najveci broj kupljenih proizvoda ako je u novcaniku iznos j,
// pri cemu j uvijek drzimo u kanonskom obliku m(j) = najveci broj koji se
// dobije permutiranjem znamenki (znamenke sortirane silazno).
#include <bits/stdc++.h>
using namespace std;

const int MAXV = 10000;  // svi iznosi su < 10^4
int canon[MAXV];
vector<int> perms[MAXV];  // perms[j] za kanonske j: svi razliciti brojevi od znamenki j

int main() {
    int n, x;
    scanf("%d %d", &n, &x);
    // kanonski predstavnik i lista permutacija za svaki iznos
    for (int v = 0; v < MAXV; v++) {
        string s = to_string(v);  // bez dopunjavanja nulama: 12 nije 0012
        sort(s.rbegin(), s.rend());
        canon[v] = stoi(s);
    }
    for (int v = 0; v < MAXV; v++) {
        if (canon[v] != v) continue;
        string s = to_string(v);
        sort(s.begin(), s.end());
        set<int> st;  // vodece nule se ignoriraju, pa stoi radi tocno to
        do { st.insert(stoi(s)); } while (next_permutation(s.begin(), s.end()));
        perms[v] = vector<int>(st.begin(), st.end());
    }
    vector<int> dp(MAXV, -1), nd;
    dp[canon[x]] = 0;
    for (int i = 0; i < n; i++) {
        int a;
        scanf("%d", &a);
        nd = dp;  // preskacemo trgovinu
        for (int j = 0; j < MAXV; j++) {
            if (dp[j] < 0) continue;
            for (int k : perms[j])  // slozimo znamenke u k i platimo a
                if (k >= a) nd[canon[k - a]] = max(nd[canon[k - a]], dp[j] + 1);
        }
        dp.swap(nd);
    }
    printf("%d\n", *max_element(dp.begin(), dp.end()));
}
