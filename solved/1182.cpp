#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <math.h>
using namespace std;

int N, S;
int arr[22];

int cnt = 0;
void solve(int i, int sum) {
  if (i == N)
    return;
  if (sum + arr[i] == S)
    cnt++;
  // cout << arr[i] << " ";
  solve(i + 1, sum + arr[i]);
  solve(i + 1, sum);
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  cin >> N >> S;
  for (int i = 0; i < N; i++)
    cin >> arr[i];
  solve(0, 0);
  cout << cnt << '\n';
  return 0;
}
