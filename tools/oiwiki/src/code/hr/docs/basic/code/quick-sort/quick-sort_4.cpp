#include <algorithm>
#include <cstdlib>
#include <iostream>
#include <limits>
#include <vector>

using namespace std;

// --8<-- [start:sort]
// Parametar predloška T je tip elemenata; za njega mora biti definiran operator manje (<)
template <typename T>
// arr je niz u kojem tražimo, rk je traženi rang (od 0), len je duljina niza
T find_kth_element(T arr[], int rk, const int len) {
  if (len <= 1) return arr[0];
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
  // Ovisno o traženom rangu i položaju dviju granica, rekurzivno traži k-ti najmanji u odgovarajućem dijelu
  // Ako je elemenata manjih od pivota više od k, k-ti najmanji je sigurno jedan od elemenata
  // manjih od pivota
  if (rk < j) return find_kth_element(arr, rk, j);
  // Inače, ako elemenata manjih i jednakih pivotu zajedno nema više od k,
  // k-ti najmanji je sigurno jedan od elemenata većih od pivota
  else if (rk >= k)
    return find_kth_element(arr + k, rk - k, len - k);
  // Inače je pivot upravo k-ti najmanji element
  return pivot;
}

// --8<-- [end:sort]

int main() {
  int n, k;
  if (!(cin >> n >> k) || n <= 0 || k < 0 || k >= n) return 0;
  vector<int> a(n);
  for (int& x : a) cin >> x;
  cout << find_kth_element(a.data(), k, n) << '\n';
}
