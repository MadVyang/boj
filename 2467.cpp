#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <math.h>
using namespace std;

int N;
long long a;
vector<long long> m, p;

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  cin >> N;
  for (int i = 0; i < N; i++) {
    cin >> a;
    if (a < 0)
      m.push_back(a);
    else
      p.push_back(a);
  }
  reverse(p.begin(), p.end());
  int mSize = m.size();
  int pSize = p.size();

  // cout << mSize << " " << pSize << endl;

  int sm, sp;
  int mi = 0, pi = 0;
  long long _min = 2000000005;
  if (mSize > 0 && pSize > 0) {
    for (int k = 0;; k++) {
      if (_min > abs(m[mi] + p[pi])) {
        _min = abs(m[mi] + p[pi]);
        sm = m[mi];
        sp = p[pi];
      }

      if (mi == mSize - 1 && pi == pSize - 1)
        break;

      if (mi == mSize - 1) {
        pi++;
      } else if (pi == pSize - 1) {
        mi++;
      } else if (abs(m[mi]) > abs(p[pi])) {
        if (mi < mSize - 1)
          mi++;
      } else {
        if (pi < pSize - 1)
          pi++;
      }
      // cout << k << " " << mi << " " << pi << endl;
    }
  }

  reverse(p.begin(), p.end());
  reverse(m.begin(), m.end());
  if (mSize >= 2 && _min > abs(m[0] + m[1])) {
    _min = abs(m[0] + m[1]);
    sm = m[1];
    sp = m[0];
  }
  if (pSize >= 2 && _min > abs(p[0] + p[1])) {
    _min = abs(p[0] + p[1]);
    sm = p[0];
    sp = p[1];
  }
  cout << sm << " " << sp << endl;

  return 0;
}
