#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int T, N;

ll md = 1000000009;
ll mem[100004][4];

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  mem[1][1] = 1;
  mem[1][2] = 0;
  mem[1][3] = 0;

  mem[2][1] = 0;
  mem[2][2] = 1;
  mem[2][3] = 0;

  mem[3][1] = 1;
  mem[3][2] = 1;
  mem[3][3] = 1;

  mem[4][1] = 2;
  mem[4][2] = 0;
  mem[4][3] = 1;

  for (int i = 5; i <= 100000; i++) {
    mem[i][1] = (mem[i - 1][2] + mem[i - 1][3]) % md;
    mem[i][2] = (mem[i - 2][1] + mem[i - 2][3]) % md;
    mem[i][3] = (mem[i - 3][1] + mem[i - 3][2]) % md;
  }

  cin >> T;
  for (int i = 0; i < T; i++) {
    cin >> N;
    cout << (mem[N][1] + mem[N][2] + mem[N][3]) % md << "\n";
  }

  return 0;
}
