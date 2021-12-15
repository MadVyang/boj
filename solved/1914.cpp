#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

ll N;
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

  cin >> N;
  cout << (1LL << N) - 1 << "\n";
  if (N <= 20)
    solve(N, 1, 3, 2);

  return 0;
}