#include <bits/stdc++.h>
using namespace std;

int N;

void solve() {}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  cin >> N;
  int t = 1;
  int len = 1;
  int result = 0;
  while (true) {
    if (t * 10 <= N) {
      t *= 10;
      result += (t * 0.9 * len);
      len++;
    } else if (t <= N) {
      t++;
      result += len;
    } else if (t > N)
      break;
  }
  cout << result << endl;

  return 0;
}
