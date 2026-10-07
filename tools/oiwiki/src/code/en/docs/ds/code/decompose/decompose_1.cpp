#include <cmath>
#include <iostream>
using namespace std;
int id[50005], len;
// id is the block index, len=sqrt(n), i.e. s from the solution above; sqrt gives the optimal complexity
long long a[50005], b[50005], s[50005];

// array a holds the data, array b records the value added to a whole block, like a lazy_tag, s
// is the sum of the elements in the block
void add(int l, int r, long long x) {  // range addition
  int sid = id[l], eid = id[r];
  if (sid == eid) {  // within a single block
    for (int i = l; i <= r; i++) a[i] += x, s[sid] += x;
    return;
  }
  for (int i = l; id[i] == sid; i++) a[i] += x, s[sid] += x;
  for (int i = sid + 1; i < eid; i++)
    b[i] += x, s[i] += len * x;  // update the sum array (complete blocks)
  for (int i = r; id[i] == eid; i--) a[i] += x, s[eid] += x;
  // the two lines above: incomplete blocks are simply summed directly, and that's it
}

long long query(int l, int r, long long p) {  // range query
  int sid = id[l], eid = id[r];
  long long ans = 0;
  if (sid == eid) {  // within a single block, sum directly by brute force
    for (int i = l; i <= r; i++) ans = (ans + a[i] + b[sid]) % p;
    return ans;
  }
  for (int i = l; id[i] == sid; i++) ans = (ans + a[i] + b[sid]) % p;
  for (int i = sid + 1; i < eid; i++) ans = (ans + s[i]) % p;
  for (int i = r; id[i] == eid; i--) ans = (ans + a[i] + b[eid]) % p;
  // same idea as the range update above
  return ans;
}

int main() {
  int n;
  cin >> n;
  len = sqrt(n);  // by the AM-GM inequality the complexity is optimal at sqrt(n)
  for (int i = 1; i <= n; i++) {  // as required by the problem statement
    cin >> a[i];
    id[i] = (i - 1) / len + 1;
    s[id[i]] += a[i];
  }
  for (int i = 1; i <= n; i++) {
    int op, l, r, c;
    cin >> op >> l >> r >> c;
    if (op == 0)
      add(l, r, c);
    else
      cout << query(l, r, c + 1) << endl;
  }
  return 0;
}

/*
https://loj.ac/s/1151495
 */
