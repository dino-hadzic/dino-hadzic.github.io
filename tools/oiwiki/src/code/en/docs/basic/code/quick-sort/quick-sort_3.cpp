#include <algorithm>
#include <cstdlib>
#include <iostream>
#include <limits>
#include <vector>

using namespace std;

// --8<-- [start:sort]
// The template parameter T is the element type; it must define the less-than (<) operator
template <typename T>
// arr is the array to be sorted, len is its length
void quick_sort(T arr[], const int len) {
  if (len <= 1) return;
  // Choose the pivot at random
  const T pivot = arr[rand() % len];
  // i: index of the element currently being processed
  // arr[0, j): elements smaller than the pivot
  // arr[k, len): elements larger than the pivot
  int i = 0, j = 0, k = len;
  // One pass of 3-way quicksort splits the sequence into:
  // smaller than pivot | equal to pivot | larger than pivot
  while (i < k) {
    if (arr[i] < pivot)
      swap(arr[i++], arr[j++]);
    else if (pivot < arr[i])
      swap(arr[i], arr[--k]);
    else
      i++;
  }
  // Recursively quicksort the two subsequences
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
