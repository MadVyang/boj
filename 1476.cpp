#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

int E, S, M;
int e = 1, s = 1, m = 1;

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  cin >> E >> S >> M;
  for (int i = 1;; i++) {
    if (e == E && s == S && m == M) {
      cout << i << '\n';
      break;
    }
    e++;
    s++;
    m++;
    if (e == 16)
      e = 1;
    if (s == 29)
      s = 1;
    if (m == 20)
      m = 1;
  }

  return 0;
}