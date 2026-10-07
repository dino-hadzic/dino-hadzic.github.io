#include <iomanip>
#include <iostream>
using namespace std;
int n;
bool vis[50];  // oznake posjećenosti
int a[50];     // niz permutacije, redom čuva trenutni rezultat pretrage

void dfs(int step) {
  if (step == n + 1) {  // rub rekurzije
    for (int i = 1; i <= n; i++) {
      cout << setw(5) << a[i];  // širina polja 5
    }
    cout << endl;
    return;
  }
  for (int i = 1; i <= n; i++) {
    if (!vis[i]) {  // je li broj i već u permutaciji koja se gradi
      vis[i] = true;
      a[step] = i;
      dfs(step + 1);
      vis[i] = false;  // ovaj korak više ne koristi taj broj; poništi oznaku da ga sljedeći korak smije koristiti
    }
  }
  return;
}

int main() {
  cin >> n;
  dfs(1);
  return 0;
}
