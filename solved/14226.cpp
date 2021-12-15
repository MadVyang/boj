#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int N;

queue<tuple<short, short, short>> q;

bool visited[3000][2000];

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  q.push(make_tuple(1, 0, 0));

  cin >> N;

  // for (int i = 2; i <= 1000; i++) {
  //   N = i;
  while (!q.empty()) {
    tuple<short, short, short> curr = q.front();
    short a = get<0>(curr), b = get<1>(curr), c = get<2>(curr);
    // cout << a << " " << b << " " << c << endl;
    if (a == N)
      break;
    q.pop();
    if (visited[a][b])
      continue;
    visited[a][b] = true;

    if (a < 1000)
      q.push(make_tuple(a, a, c + 1));
    if (b > 0 && a < 1000)
      q.push(make_tuple(a + b, b, c + 1));
    if (a > 1)
      q.push(make_tuple(a - 1, b, c + 1));
  }

  cout << get<2>(q.front()) << endl;
  // }

  return 0;
}