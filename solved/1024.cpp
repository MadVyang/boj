#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

ll N, M;

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);

  cin >> N >> M;

  bool solved = false;
  for (ll k = M; k <= 100; k++) {
    for (ll i = N / k - 100; i <= N / k + 100; i++) {
      if (i < -1)
        continue;
      ll j = i + k;
      if ((j * (j + 1) / 2) - (i * (i + 1) / 2) == N) {
        for (ll k = i + 1; k <= j; k++)
          cout << k << " ";
        cout << endl;
        solved = true;
        break;
      }
    }
    if (solved)
      break;
  }
  if (!solved)
    cout << "-1\n";
  return 0;
}