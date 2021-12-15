#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int N;

ll mem[100][2];

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  mem[1][0] = 0; // 1
  mem[1][1] = 1;
  mem[2][0] = 1; // 10
  mem[2][1] = 0;
  mem[3][0] = 1; // 100 101
  mem[3][1] = 1;
  mem[4][0] = 2; // 1000 1001 1010
  mem[4][1] = 1;
  for (int i = 4; i <= 90; i++) {
    mem[i][0] = mem[i - 1][0] + mem[i - 1][1];
    mem[i][1] = mem[i - 1][0];
  }

  cin >> N;

  cout << mem[N][0] + mem[N][1] << endl;

  return 0;
}