#include <bits/stdc++.h>
using namespace std;

int N;
vector<pair<char, short>> list;

void solve(int n, int from, int to, int other) {
  if (n == 1) {
    cout << from << " " << to << "\n";
    return;
  }
  solve(n - 1, from, other, to);
  cout << from << " " << to << "\n";
  solve(n - 1, other, to, from);
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  cin >> N;
  cout << (1 << N) - 1 << "\n";
  solve(N, 1, 3, 2);

  return 0;
}