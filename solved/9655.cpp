#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int N;
int win[1005];

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  cin >> N;
  win[1] = 1;
  win[2] = 0;
  win[3] = 1;
  win[4] = 0;
  win[5] = 1;

  cout << (N % 2 == 1 ? "SK" : "CY") << "\n";

  return 0;
}
