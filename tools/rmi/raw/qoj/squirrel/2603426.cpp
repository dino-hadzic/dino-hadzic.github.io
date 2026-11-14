#include "squirrel.h"
#include <bits/stdc++.h>
using namespace std;
using ll=long long;

const int N=2010;
int n, p[N], rt[N], ans[N];

void chk(int l, int r, int w) {
  for(int i=l; i<=r; i++) {
    if(!ans[i]) {
      ans[i]=w, rt[i]=r; break;
    }
    else if(rt[i]>r) swap(r, rt[i]), swap(w, ans[i]);
  }
  for(int i=n-1; i>=0; i--) {
    if(!ans[i] || rt[i]>=p[i+1]) p[i]=i;
    else p[i]=p[i+1];
  }
}

void solve(int N, std::vector<std::vector<int>> A, ll & answer, vector<int>& solution) {
  n=N;
  vector<array<int, 3>> vec, vec2;
  for(int i=0; i<n; i++) for(int j=0; j<=i; j++) vec.push_back({A[i][j], j, i});
  sort(vec.rbegin(), vec.rend());
  answer=0;
  for(int i=0; i<=n; i++) p[i]=i;
  for(auto [w, l, r]:vec) {
    if(p[l]<=r) answer+=w, chk(l, r, w);
    else vec2.pop_back();
  }
  solution.resize(n);
  for(int i=0; i<n; i++) solution[i]=ans[i];
}
