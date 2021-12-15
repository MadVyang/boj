#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

ll md = 1000000003;
bool visited[1005][1005];
ll mem[1005][1005];

int N, K;

ll solve2(int n, int k) {
  if (visited[n][k])
    return mem[n][k];
  if (n == 2 * k)
    return 2;
  if (k == 1)
    return n;
  mem[n][k] = (solve2(n - 1, k) + solve2(n - 2, k - 1)) % md;
  visited[n][k] = true;
  return mem[n][k];
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  cin >> N >> K;
  solve2(N, K);
  if (N / 2 < K)
    cout << "0\n";
  else
    cout << ((mem[N - 3][K - 1] + mem[N - 1][K]) % md) << endl;
  return 0;
}