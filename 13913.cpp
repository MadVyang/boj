#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int N, K, res;
bool visited[200005];
int from[200005];
queue<pair<int, int>> q;

vector<int> way;

void research(int i) {
  if (way.size() <= res) {
    way.push_back(i);
    research(from[i]);
  } else {
    for (int i = (int)way.size() - 1; i >= 0; i--)
      cout << way[i] << " ";
    cout << "\n";
  }
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  cin >> N >> K;

  q.push(make_pair(N, 0));
  while (!q.empty()) {
    int i = q.front().first;
    int cnt = q.front().second;
    q.pop();
    // if (i < 0 || i > 200000 || visited[i])
    //   continue;
    if (i == K) {
      res = cnt;
      break;
    }

    if (N < K) {
      if (i + 1 >= 0 && i + 1 <= 200000 && !visited[i + 1]) {
        q.push(make_pair(i + 1, cnt + 1));
        from[i + 1] = i;
        visited[i + 1] = true;
      }
      if (2 * i >= 0 && 2 * i <= 200000 && !visited[2 * i]) {
        q.push(make_pair(2 * i, cnt + 1));
        from[2 * i] = i;
        visited[2 * i] = true;
      }
    }
    if (i - 1 >= 0 && i - 1 <= 200000 && !visited[i - 1]) {
      q.push(make_pair(i - 1, cnt + 1));
      from[i - 1] = i;
      visited[i - 1] = true;
    }
  }
  // for (int i = 0; i < 20; i++) {
  //   cout << i << "->" << from[i] << " ";
  // }
  // cout << endl;

  cout << res << endl;
  research(K);

  return 0;
}