#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

stack<ll> nums;
ll K, N, a;

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  cin >> N >> K;
  for (int i = 0; i < N; i++) {
    cin >> a;
    nums.push(a);
  }

  int cnt = 0;
  while (K > 0) {
    if (nums.empty())
      break;
    ll curr = nums.top();
    nums.pop();
    if (curr <= K) {
      // cout << curr << " " << K / curr << endl;
      // cout << K << endl;
      cnt += K / curr;
      K %= curr;
    }
  }
  cout << cnt << endl;

  return 0;
}