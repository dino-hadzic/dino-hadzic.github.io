#include <iostream>

int main() {
  int n = 0, u = 0, d = 0;
  std::cin >> u >> d >> n;
  int time = 0, dist = 0;
  while (true) {  // Beskonačna petlja za nabrajanje koraka
    dist += u;
    time++;
    if (dist >= n) break;  // Kad je uvjet ispunjen, izađi iz petlje
    dist -= d;
  }
  std::cout << time << '\n';  // Ispiši rezultat
  return 0;
}
