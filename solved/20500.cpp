#include <bits/stdc++.h>
using namespace std;

typedef unsigned long long ull;
ull md = 1000000007;
int N;
ull arr[2000];
ull mem[2000][3];

ull cnt = 0;
void solve(ull t, int len) {
  // cout << t << " " << len << "\n";
  if (len == N) {
    if (t % 15 == 0) {
      // cout << t << endl;
      cnt++;
      cnt %= md;
    }
    return;
  }
  ull t1 = (t * 10 + 1) % md;
  ull t2 = (t * 10 + 5) % md;
  solve(t1, len + 1);
  solve(t2, len + 1);
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  cin >> N;
  arr[1] = 0;
  arr[2] = 1;
  arr[3] = 1;
  arr[4] = 3;

  // mem[1][0] = 0;
  // mem[1][1] = 1;
  // mem[1][2] = 1;

  mem[2][0] = 1;
  mem[2][1] = 1;
  mem[2][2] = 0;

  mem[3][0] = 1;
  mem[3][1] = 1;
  mem[3][2] = 2;

  mem[4][0] = 3;
  mem[4][1] = 3;
  mem[4][2] = 2;

  for (int i = 5; i <= 1515; i++) {
    mem[i][0] = mem[i - 1][1] + mem[i - 1][2];
    mem[i][1] = mem[i - 1][0] + mem[i - 1][2];
    mem[i][2] = mem[i - 1][0] + mem[i - 1][1];
    mem[i][0] %= md;
    mem[i][1] %= md;
    mem[i][2] %= md;
  }
  cout << mem[N][0] << endl;
  // solve(0, 0);
  // cout << cnt << endl;

  return 0;
}
