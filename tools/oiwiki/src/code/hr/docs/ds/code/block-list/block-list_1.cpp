#include <cctype>
#include <cstring>
#include <iostream>
using namespace std;
constexpr int sqn = 1e3;

struct node {  // definicija blokovne vezane liste
  node* nxt;
  int size;
  char d[(sqn << 1) + 5];

  node() { size = 0, nxt = NULL; }

  void pb(char c) { d[size++] = c; }
}* head = NULL;

char inits[(int)1e6 + 5];
int llen, q;

void readch(char& ch) {  // učitaj znak
  do cin >> ch;
  while (!isalpha(ch));
}

void check(node* p) {  // provjera – ne zaboravi podijeliti blok
  if (p->size >= (sqn << 1)) {
    node* q = new node;
    for (int i = sqn; i < p->size; i++) q->pb(p->d[i]);
    p->size = sqn, q->nxt = p->nxt, p->nxt = q;
  }
}

void insert(char c, int pos) {  // umetanje elementa; razmišljaj o tome kao o vezanoj listi
  node* p = head;
  int tot, cnt;
  if (pos > llen++) {
    while (p->nxt != NULL) p = p->nxt;
    p->pb(c), check(p);
    return;
  }
  for (tot = head->size; p != NULL && tot < pos; p = p->nxt, tot += p->size);
  tot -= p->size, cnt = pos - tot - 1;
  for (int i = p->size - 1; i >= cnt; i--) p->d[i + 1] = p->d[i];
  p->d[cnt] = c, p->size++;
  check(p);
}

char query(int pos) {  // upit
  node* p;
  int tot;
  for (p = head, tot = head->size; p != NULL && tot < pos;
       p = p->nxt, tot += p->size);
  tot -= p->size;
  return p->d[pos - tot - 1];
}

int main() {
  cin.tie(nullptr)->sync_with_stdio(false);
  cin >> inits >> q;
  llen = strlen(inits);
  node* p = new node;
  head = p;
  for (int i = 0; i < llen; i++) {
    if (i % sqn == 0 && i) p->nxt = new node, p = p->nxt;
    p->pb(inits[i]);
  }
  char a;
  int k;
  while (q--) {
    readch(a);
    if (a == 'Q')
      cin >> k, cout << query(k) << '\n';
    else
      readch(a), cin >> k, insert(a, k);
  }
  return 0;
}
