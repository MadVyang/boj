#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int N;
int r, c;

ll cnt = 0;
void check(int y, int x) {
  if (y == r && x == c)
    cout << cnt << endl;
  cnt++;
}

void traverse(int y, int x, int size) {
  if (size == 2) {
    check(y, x);
    x++;
    check(y, x);
    x--;
    y++;
    check(y, x);
    x++;
    check(y, x);
    return;
  }
  if (y <= r && r <= y + size && x <= c && c <= x + size) {
    // cout << y << " " << x << " " << size << endl;
    // cout << cnt << endl;
    traverse(y, x, size / 2);
    traverse(y, x + size / 2, size / 2);
    traverse(y + size / 2, x, size / 2);
    traverse(y + size / 2, x + size / 2, size / 2);
  } else {
    cnt += (ll)size * size;
  }
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);

  cin >> N >> r >> c;
  traverse(0, 0, 1 << N);

  return 0;
}