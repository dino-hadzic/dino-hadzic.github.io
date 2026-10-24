#include <iostream>
using namespace std;

struct myrand {
  int A, C, M, x;

  myrand(int A, int C, int M) {
    this->A = A;
    this->C = C;
    this->M = M;
    this->x = 0;
  }

  // generira sljedeći slučajni broj u slučajnom nizu
  int next() { return x = ((long long)A * x + C) % M; }
};

myrand rnd(3, 5, 97);  // inicijaliziraj generator slučajnih brojeva

int main() {
  int x = rnd.next();
  cout << x << endl;
  return 0;
}