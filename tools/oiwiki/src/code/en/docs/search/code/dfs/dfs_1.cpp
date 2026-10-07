#include <iomanip>
#include <iostream>
using namespace std;
int n;
bool vis[50];  // visited flags
int a[50];     // permutation array, stores the current search result in order

void dfs(int step) {
  if (step == n + 1) {  // base case
    for (int i = 1; i <= n; i++) {
      cout << setw(5) << a[i];  // field width 5
    }
    cout << endl;
    return;
  }
  for (int i = 1; i <= n; i++) {
    if (!vis[i]) {  // is the number i already used in the permutation being built
      vis[i] = true;
      a[step] = i;
      dfs(step + 1);
      vis[i] = false;  // this step no longer uses the number; clear the flag so the next step may use it
    }
  }
  return;
}

int main() {
  cin >> n;
  dfs(1);
  return 0;
}
