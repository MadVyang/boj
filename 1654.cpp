#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

vector<ll> nums;
ll K, N, a;

ll check(ll len) {
  ll cnt = 0;
  for (ll i : nums) {
    cnt += i / len;
  }
  // cout << len << " " << cnt << "\n";
  return cnt;
}

ll solve(ll low, ll high) {
  ll mid;
  while (low < high) {
    mid = (low + high) / 2;
    if (check(mid) < N)
      high = mid;
    else
      low = mid + 1;
  }
  return mid;
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  cin >> K >> N;
  for (int i = 0; i < K; i++) {
    cin >> a;
    nums.push_back(a);
  }
  ll res = solve(0LL, 2147483648LL);
  if (check(res) >= N)
    cout << res << endl;
  else
    cout << res - 1 << endl;

  return 0;
}