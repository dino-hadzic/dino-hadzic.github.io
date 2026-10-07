#include <cmath>
#include <iostream>
using namespace std;
int id[50005], len;
// id je broj bloka, len=sqrt(n), tj. s iz gornjeg rješenja; za sqrt je složenost optimalna
long long a[50005], b[50005], s[50005];

// niz a su podaci, niz b pamti vrijednost dodanu cijelom bloku, slično lazy_tag, s
// je zbroj elemenata u bloku
void add(int l, int r, long long x) {  // dodavanje na intervalu
  int sid = id[l], eid = id[r];
  if (sid == eid) {  // unutar jednog bloka
    for (int i = l; i <= r; i++) a[i] += x, s[sid] += x;
    return;
  }
  for (int i = l; id[i] == sid; i++) a[i] += x, s[sid] += x;
  for (int i = sid + 1; i < eid; i++)
    b[i] += x, s[i] += len * x;  // ažuriraj niz zbrojeva (potpuni blokovi)
  for (int i = r; id[i] == eid; i--) a[i] += x, s[eid] += x;
  // gornja dva retka: nepotpuni blokovi jednostavno se zbroje izravno, i to je to
}

long long query(int l, int r, long long p) {  // upit na intervalu
  int sid = id[l], eid = id[r];
  long long ans = 0;
  if (sid == eid) {  // unutar jednog bloka zbroji izravno (brute force)
    for (int i = l; i <= r; i++) ans = (ans + a[i] + b[sid]) % p;
    return ans;
  }
  for (int i = l; id[i] == sid; i++) ans = (ans + a[i] + b[sid]) % p;
  for (int i = sid + 1; i < eid; i++) ans = (ans + s[i]) % p;
  for (int i = r; id[i] == eid; i--) ans = (ans + a[i] + b[eid]) % p;
  // isti princip kao kod gornje izmjene intervala
  return ans;
}

int main() {
  int n;
  cin >> n;
  len = sqrt(n);  // po AG-nejednakosti složenost je optimalna za sqrt(n)
  for (int i = 1; i <= n; i++) {  // prema tekstu zadatka
    cin >> a[i];
    id[i] = (i - 1) / len + 1;
    s[id[i]] += a[i];
  }
  for (int i = 1; i <= n; i++) {
    int op, l, r, c;
    cin >> op >> l >> r >> c;
    if (op == 0)
      add(l, r, c);
    else
      cout << query(l, r, c + 1) << endl;
  }
  return 0;
}

/*
https://loj.ac/s/1151495
 */
