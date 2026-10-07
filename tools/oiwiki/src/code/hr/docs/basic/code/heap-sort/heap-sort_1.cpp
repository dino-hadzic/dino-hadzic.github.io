#include <algorithm>
#include <cstdlib>
#include <iostream>
#include <limits>
#include <vector>

using namespace std;

// --8<-- [start:sort]
void sift_down(int arr[], int start, int end) {
  // Izračunaj indekse roditelja i djece
  int parent = start;
  int child = parent * 2 + 1;
  while (child <= end) {  // Usporedba samo dok je indeks djeteta unutar granica
    // Prvo usporedi dvoje djece i odaberi veće
    if (child + 1 <= end && arr[child] < arr[child + 1]) child++;
    // Ako je roditelj veći od djeteta, popravak je gotov – izađi iz funkcije
    if (arr[parent] >= arr[child])
      return;
    else {  // Inače zamijeni roditelja i dijete, pa dijete usporedi s unucima
      swap(arr[parent], arr[child]);
      parent = child;
      child = parent * 2 + 1;
    }
  }
}

void heap_sort(int arr[], int len) {
  // Kreni od roditelja posljednjeg čvora i radi sift down da izgradiš hrpu (heapify)
  for (int i = (len - 1 - 1) / 2; i >= 0; i--) sift_down(arr, i, len - 1);
  // Zamijeni prvi element s elementom ispred već sortiranog dijela, pa ponovno popravi hrpu (elemente ispred upravo postavljenog), sve dok niz nije sortiran
  for (int i = len - 1; i > 0; i--) {
    swap(arr[0], arr[i]);
    sift_down(arr, 0, i - 1);
  }
}

// --8<-- [end:sort]

int main() {
  int n;
  if (!(cin >> n) || n < 0) return 0;
  vector<int> a(n + 1);
  for (int i = 0; i < n; ++i) cin >> a[i];
  heap_sort(a.data(), n);
  for (int i = 0; i < n; ++i) cout << a[i] << ' ';
  cout << '\n';
}
