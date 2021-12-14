#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int N;
ll arr[100005];
ll sum[100005];
ll odd[100005];
ll even[100005];

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  cin >> N;
  ll so = 0, se = 0;
  for (int i = 1; i <= N; i++) {
    cin >> arr[i];
    if (i % 2 == 1) {
      so += arr[i];
      odd[i] = so;
    } else {
      se += arr[i];
      even[i] = se;
    }
  }
  ll last = arr[N];

  ll mx = 0;
  // T = odd
  for (int i = 1; i <= N; i += 2) {
    ll curr = odd[i] - arr[i] + even[N - 2] - even[i - 1] + arr[N];
    if (curr > mx) {
      // cout << odd[i] << " " << even[N - 2] << " " << even[i - 1] << "\n";
      mx = curr;
    }
  }
  // T = even
  for (int i = 2; i <= N; i += 2) {
    ll curr = odd[i - 1] + even[N - 2] - even[i - 2];
    if (curr > mx) {
      // cout << odd[i - 1] << " " << even[N - 2] << " " << even[i - 2] << "\n";
      mx = curr;
    }
  }

  cout << mx << endl;

  return 0;
}
