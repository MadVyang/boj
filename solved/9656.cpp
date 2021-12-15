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
  win[1] = 0;
  win[2] = 1;
  win[3] = 0;
  win[4] = 1;
  win[5] = 0;

  cout << (N % 2 == 0 ? "SK" : "CY") << "\n";

  return 0;
}
