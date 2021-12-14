#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int N, M;
int A[100005];
int k;

int solve(int i) {
  int low = 0, high = N - 1;
  while (low <= high) {
    int mid = (low + high) / 2;
    if (A[mid] == i)
      return 1;
    else if (A[mid] > i)
      high = mid - 1;
    else
      low = mid + 1;
  }
  return 0;
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  cin >> N;
  for (int i = 0; i < N; i++) {
    cin >> A[i];
  }
  sort(A, A + N);
  // for (int i = 0; i < N; i++) {
  //   cout << A[i];
  // }
  cin >> M;
  for (int i = 0; i < M; i++) {
    cin >> k;
    cout << solve(k) << "\n";
  }

  return 0;
}