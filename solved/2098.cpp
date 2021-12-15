#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int N;
int g[20][20];

bool visited[20];

const int mx = 987654321;
int mn = mx;
vector<int> list;

int mem[20][70000];

int dfs(int i, int mask) {
  if (mem[i][mask])
    return mem[i][mask];
  if (list.size() == N) {
    if (g[i][0])
      return g[i][0];
    else
      return mx;
  }

  visited[i] = true;

  int m = mx;
  for (int j = 0; j < N; j++) {
    if (g[i][j] && !visited[j]) {
      list.push_back(j);
      int r = dfs(j, mask | (1 << j)) + g[i][j];
      if (r < m)
        m = r;
      list.pop_back();
    }
  }
  visited[i] = false;
  return mem[i][mask] = m;
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  cin >> N;
  for (int i = 0; i < N; i++)
    for (int j = 0; j < N; j++)
      cin >> g[i][j];

  list.push_back(0);
  cout << dfs(0, 0) << endl;

  return 0;
}
