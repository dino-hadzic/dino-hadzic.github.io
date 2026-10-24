
constexpr int SEED = 5489;

// --8<-- [start:core]

#include <iostream>
#include <random>
#include <vector>

using namespace std;

struct myrand {
  vector<unsigned int> vec;
  int l, j, k, cur;

  template <class URBG>
  myrand(int l, int j, int k, URBG &&rng) {
    this->l = l;
    this->j = j;
    this->k = k;
    cur = 0;
    for (int i = 0; i < l; i++) {
      vec.push_back(rng());  // prvih nekoliko elemenata slučajnog niza generiraj drugom metodom
    }
  }

  unsigned int next() {
    vec[cur] = vec[(cur - j + l) % l] * vec[(cur - k + l) % l];
    // tip unsigned se koristi da bi se automatski računalo modulo 2^32
    return vec[cur++];
  }
};

// posljednji argument može se zamijeniti drugim generatorom slučajnih brojeva, sjeme postavi sam
myrand rnd(11, 4, 7, mt19937(SEED));

int main() {
  unsigned int x = rnd.next();
  cout << x << endl;
  return 0;
}

// --8<-- [end:core]
