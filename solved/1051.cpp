#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

ll N, M;
char arr[55][55];

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);

  cin >> N >> M;
  for (int i = 0; i < N; i++)
    cin >> arr[i];

  int mn = N < M ? N : M;
  for (int k = mn; k >= 1; k--) {
    for (int i = 0; i < N - k; i++) {
      for (int j = 0; j < M - k; j++) {
        if (arr[i][j] == arr[i][j + k] && arr[i][j] == arr[i + k][j] &&
            arr[i][j] == arr[i + k][j + k]) {
          cout << (k + 1) * (k + 1) << endl;
          return 0;
        }
      }
    }
  }
  cout << 1 << endl;

  return 0;
}