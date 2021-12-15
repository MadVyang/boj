#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int N, K;
bool visited[100005];

queue<pair<int, int>> q;

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  cin >> N >> K;

  int res = 0;
  q.push(make_pair(N, 0));
  while (!q.empty()) {
    int i = q.front().first;
    int cnt = q.front().second;
    q.pop();
    if (i < 0 || i > 100000 || visited[i])
      continue;
    if (i == K) {
      res = cnt;
      break;
    }
    visited[i] = true;

    q.push(make_pair(i + 1, cnt + 1));
    q.push(make_pair(i - 1, cnt + 1));
    q.push(make_pair(2 * i, cnt + 1));
  }

  cout << res << endl;

  return 0;
}
