#include <cstring>
constexpr int MAXN = 100000;  // here MAXN is the bound on the absolute value of the array elements

int solve(int n, int a[]) {
  bool met[MAXN * 2 + 1];  // a bucket that can hold the values in [-MAXN, MAXN]
  memset(met, 0, sizeof(met));
  int ans = 0;
  for (int i = 0; i < n; ++i) {
    if (met[MAXN - a[i]]) ++ans;  // if the wanted element is already in the bucket, increase the answer
    met[MAXN + a[i]] = true;  // in any case, put the current element into the bucket
  }
  return ans * 2;
}
