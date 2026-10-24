constexpr int SEED = 5489u;

// --8<-- [start:core]

#include <ctime>
#include <iostream>
#include <random>

using namespace std;

int main() {
  mt19937 myrand(SEED);  // zamijeni SEED bilo kojim cijelim brojem ili s time(nullptr)
  cout << myrand() << endl;
  return 0;
}

// --8<-- [end:core]