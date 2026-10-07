#include <iostream>

int main() {
  int n = 0, u = 0, d = 0;
  std::cin >> u >> d >> n;
  int time = 0, dist = 0;
  while (true) {  // Infinite loop to enumerate the steps
    dist += u;
    time++;
    if (dist >= n) break;  // Leave the loop once the condition is met
    dist -= d;
  }
  std::cout << time << '\n';  // Print the result
  return 0;
}
