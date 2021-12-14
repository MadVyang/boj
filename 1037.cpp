#include <bits/stdc++.h>
using namespace std;

int N;
int arr[55];

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  cin >> N;
  for (int i = 0; i < N; i++) {
    cin >> arr[i];
  }
  sort(arr, arr + N);
  cout << arr[0] * arr[N - 1] << "\n";

  return 0;
}
