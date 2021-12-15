#include <bits/stdc++.h>
using namespace std;

int T;
int M, N, x, y;

void solve() {
  int m, n;
  int inc = 1;
  for (int k = 0;; k += inc) {
    m = k % M + 1;
    n = k % N + 1;
    if (m == x && n == y) {
      cout << k + 1 << "\n";
      break;
    }
    if (k > M * N) {
      cout << -1 << "\n";
      break;
    }
    if (m == x)
      inc = M;
  }
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  cin >> T;
  for (int i = 0; i < T; i++) {
    cin >> M >> N >> x >> y;
    solve();
  }

  return 0;
}
