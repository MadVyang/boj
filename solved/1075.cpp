#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

ll N, F;

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  cin >> N >> F;
  N -= N % 100;
  for (int i = 0; i < 100; i++) {
    ll t = N + i;
    if (t % F == 0) {
      if (i < 10)
        cout << "0";
      cout << i << "\n";
      break;
    }
  }

  return 0;
}