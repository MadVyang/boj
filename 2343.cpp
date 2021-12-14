#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <math.h>
using namespace std;

int N, M;
int curr;
int arr[100005];

int solve() {
  int sum = 0;
  int mx = 0;
  int cnt = 0;
  for (int i = 0; i < N - 1; i++) {
    sum += arr[i];
    if (sum + arr[i + 1] > curr) {
      // cout << sum << "\n";
      if (mx < sum)
        mx = sum;
      sum = 0;
      cnt++;
    }
  }
  if (mx < sum + arr[N - 1])
    mx = sum + arr[N - 1];
  // cout << curr << " " << mx << " " << arr[N - 1] << " "
  //      << "\n";
  if (cnt >= M)
    return -1;
  if (sum + arr[N - 1] <= curr)
    return mx;
  else
    return -1;
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  cin >> N >> M;
  int sum = 0;
  for (int i = 0; i < N; i++) {
    cin >> arr[i];
    sum += arr[i];
  }
  curr = sum / M;

  int ans;
  while (true) {
    ans = solve();
    if (ans < 0)
      curr++;
    else
      break;
  }

  cout << ans << endl;

  return 0;
}
