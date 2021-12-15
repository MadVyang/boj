#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

ll ccw(ll x1, ll y1, ll x2, ll y2, ll x3, ll y3) {
  ll res = x1 * y2 - x2 * y1 + x2 * y3 - x3 * y2 + x3 * y1 - x1 * y3;
  if (res > 0)
    return 1;
  else if (res < 0)
    return -1;
  return 0;
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  ll x1, y1, x2, y2, x3, y3, x4, y4;
  cin >> x1 >> y1 >> x2 >> y2 >> x3 >> y3 >> x4 >> y4;
  if (ccw(x1, y1, x2, y2, x3, y3) * ccw(x1, y1, x2, y2, x4, y4) <= 0 &&
      ccw(x3, y3, x4, y4, x1, y1) * ccw(x3, y3, x4, y4, x2, y2) <= 0)
    cout << 1 << endl;
  else
    cout << 0 << endl;
  return 0;
}
