#include <bits/stdc++.h>
using namespace std;

int arr[101];
int arr2[101];
int dp[10001][101] = {};
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);

  int n, k;
  cin >> n >> k;
  for (int i = 0; i < n; i++) cin >> arr[i];
  sort(arr, arr + n);
  arr2[0] = arr[0];
  int count = 1;
  for (int i = 1; i < n; i++) {
    if (arr[i - 1] == arr[i]) continue;
    arr2[count++] = arr[i];
  }
  for (int i = 0; i <= k; i++) {
    for (int j = 0; j < n; j++) {
      dp[i][j] = 123456789;
    }
  }
  for (int i = 0; i < n; i++) {
    if (arr[i] <= k) dp[arr[i]][i] = 1;
  }

  for (int i = 0; i <= k; i++) {
    for (int j = 0; j < n; j++) {
      if (arr[j] > i) break;
      for (int l = 0; l <= j; l++) {
        dp[i][j] = min(dp[i][j], dp[i - arr[j]][l] + 1);
      }
    }
  }

  int ans = dp[k][0];
  for (int i = 0; i < n; i++) {
    ans = min(ans, dp[k][i]);
  }
  if (ans >= 123456789) ans = -1;
  cout << ans << endl;

  return 0;
}