#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int N;
int arr[1005];
int dp[1005];

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  cin >> N;
  for (int i = 0; i < N; i++)
    cin >> arr[i];
  dp[0] = 1;

  for (int i = 1; i < N; i++) {
    int mx = 0;
    for (int j = i - 1; j >= 0; j--) {
      if (arr[i] > arr[j] && dp[j] > mx)
        mx = dp[j];
    }
    dp[i] = mx + 1;
    // if (mx < dp[i])
    //   mx = dp[i];
  }

  int mx = 1;
  for (int i = 0; i < N; i++)
    if (dp[i] > mx)
      mx = dp[i];
  cout << mx << endl;

  return 0;
}
