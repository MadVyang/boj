#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

ll N;
ll arr[55];

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);

  cin >> N;
  for (int i = 0; i < N; i++) {
    cin >> arr[i];
  }
  ll mx = 0, sel = -1;
  for (int i = 0; i < N; i++) {
    double check = DBL_MAX;
    ll cnt = 0;
    for (int j = i - 1; j >= 0; j--) {
      double gr = (double)(arr[i] - arr[j]) / (i - j);
      if (gr + (0.00000000001) < check) {
        check = gr;
        cnt++;
        // cout << arr[i] << " ( a ) " << arr[j] << endl;
      }
    }

    check = -DBL_MAX;
    for (int j = i + 1; j < N; j++) {
      double gr = (double)(arr[j] - arr[i]) / (j - i);
      if (gr - (0.00000000001) > check) {
        check = gr;
        cnt++;
        // cout << arr[i] << " ( b ) " << arr[j] << endl;
      }
    }

    if (cnt > mx) {
      mx = cnt;
      sel = i;
    }
  }
  // cout << sel << " " << mx << endl;
  cout << mx << endl;

  return 0;
}