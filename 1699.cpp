#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int dp[100005];
int N;
int solve(int n) {
  // cout << n << endl;
  if (dp[n])
    return dp[n];
  if (n == 1)
    return 1;
  for (int i = 2; i * i <= n; i++)
    if (i * i == n)
      return 1;

  // if (n < 1)
  //   return 999999;

  int min = 999999;
  for (int i = 1; i * i <= n; i++) {
    int curr = solve(n - i * i) + 1;
    if (min > curr)
      min = curr;
  }
  dp[n] = min;
  return min;
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  cin >> N;
  cout << solve(N) << endl;
  return 0;
}