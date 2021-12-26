#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

ll N, M;

bool arr[1000005];

bool check(ll i) {
  for (ll k = 2; k * k <= i; k++) {
    if (i % (k * k) == 0)
      return false;
  }
  return true;
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);

  cin >> N >> M;
  for (ll i = 2; i * i <= M; i++) {
    ll j;
    if (N % (i * i) == 0)
      j = N / (i * i);
    else
      j = N / (i * i) + 1;
    for (; j * i * i <= M; j++) {
      arr[j * i * i - N] = true;
      // cout << j * i * i - N << " ";
    }
  }
  // cout << endl;
  int cnt = 0;
  for (ll i = 0; i <= M - N; i++) {
    if (!arr[i]) {
      // cout << i << " ";
      cnt++;
    }
  }
  cout << cnt << endl;

  return 0;
}