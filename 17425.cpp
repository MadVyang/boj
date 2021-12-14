#include <bits/stdc++.h>
using namespace std;

int T, N;
long long arr[1000005];

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  long long r = 0;
  for (int i = 2; i <= 1000000; i++) {
    for (int j = i; j <= 1000000; j += i) {
      arr[j] += i;
    }
  }
  for (int i = 2; i <= 1000000; i++) {
    arr[i] += arr[i - 1] + 1;
  }

  cin >> T;
  for (int t = 0; t < T; t++) {
    cin >> N;
    // long long r = 0;
    // for (int i = 1; i <= N; i++) {
    //   r += i * (N / i);
    // }
    cout << arr[N] + 1 << "\n";
  }

  return 0;
}
