#include <algorithm>
#include <cstdlib>
#include <iostream>
#include <limits>
#include <vector>

using namespace std;

// --8<-- [start:sort]
// The template parameter T is the element type; it must define the less-than (<) operator
template <typename T>
// arr is the array to search, rk is the wanted rank (0-based), len is the array length
T find_kth_element(T arr[], int rk, const int len) {
  if (len <= 1) return arr[0];
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
  // Depending on the wanted rank and the two boundaries, recurse into the right part to find the k-th smallest
  // If there are more than k elements smaller than the pivot, the k-th smallest must be one of the elements
  // smaller than the pivot
  if (rk < j) return find_kth_element(arr, rk, j);
  // Otherwise, if the elements smaller than and equal to the pivot together are not more than k,
  // the k-th smallest must be one of the elements larger than the pivot
  else if (rk >= k)
    return find_kth_element(arr + k, rk - k, len - k);
  // Otherwise the pivot itself is the k-th smallest element
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
