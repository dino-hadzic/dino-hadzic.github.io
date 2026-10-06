#include <algorithm>
#include <cmath>
#include <cstring>
#include <iostream>
#include <queue>
using namespace std;

struct f {
  long long d;
  long long p;
} a[100005];

bool cmp(f A, f B) { return A.d < B.d; }

// min-heap keeps track of the minimum
priority_queue<long long, vector<long long>, greater<long long>> q;

int main() {
  long long n, i;
  cin >> n;
  for (i = 1; i <= n; i++) {
    cin >> a[i].d >> a[i].p;
  }
  sort(a + 1, a + n + 1, cmp);
  long long ans = 0;
  for (i = 1; i <= n; i++) {
    if (a[i].d <= (int)q.size()) {  // deadline exceeded
      if (q.top() < a[i].p) {       // regret – replace the worst choice
        ans += a[i].p - q.top();
        q.pop();
        q.push(a[i].p);
      }
    } else {  // add to the queue directly
      ans += a[i].p;
      q.push(a[i].p);
    }
  }
  cout << ans << endl;
  return 0;
}
