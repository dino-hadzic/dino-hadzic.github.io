#include <algorithm>
#include <cstdlib>
#include <iostream>
#include <limits>
#include <vector>

using namespace std;

// --8<-- [start:sort]
// Parametar predloška T je tip elemenata; za njega mora biti definiran operator manje (<)
template <typename T>
// arr je niz koji treba sortirati, len je njegova duljina
void quick_sort(T arr[], const int len) {
  if (len <= 1) return;
  // Nasumično odaberi pivot
  const T pivot = arr[rand() % len];
  // i: indeks elementa koji trenutno obrađujemo
  // arr[0, j): elementi manji od pivota
  // arr[k, len): elementi veći od pivota
  int i = 0, j = 0, k = len;
  // Jedan prolaz trosmjernog quick sorta dijeli niz na:
  // manji od pivota | jednaki pivotu | veći od pivota
  while (i < k) {
    if (arr[i] < pivot)
      swap(arr[i++], arr[j++]);
    else if (pivot < arr[i])
      swap(arr[i], arr[--k]);
    else
      i++;
  }
  // Rekurzivno quick sortom sortiraj oba podniza
  quick_sort(arr, j);
  quick_sort(arr + k, len - k);
}

// --8<-- [end:sort]

int main() {
  int n;
  if (!(cin >> n) || n < 0) return 0;
  vector<int> a(n + 1);
  for (int i = 0; i < n; ++i) cin >> a[i];
  quick_sort(a.data(), n);
  for (int i = 0; i < n; ++i) cout << a[i] << ' ';
  cout << '\n';
}
