#include <bits/stdc++.h>
using namespace std;

int a, b;

int solve(int x, int y) {
  if (x < y)
    return solve(y, x);
  for (int i = 2; i <= y; i++) {
    if (x % i == 0 && y % i == 0)
      return i * solve(x / i, y / i);
  }
  return x * y;
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  cin >> a >> b;
  cout << a * b / solve(a, b) << endl << solve(a, b) << endl;

  return 0;
}
