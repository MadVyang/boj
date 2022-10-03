#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int N;
vector<int> g[100001];

int MAX = 30;
int parent[100001][31];
int depth[100001];
void dfs(int i)
{
  for (int k = 1; k <= MAX; k++)
  {
    parent[i][k] = parent[parent[i][k - 1]][k - 1];
  }
  for (auto j : g[i])
  {
    if (j != parent[i][0])
    {
      parent[j][0] = i;
      depth[j] = depth[i] + 1;
      dfs(j);
    }
  }
}

int main()
{
  ios_base::sync_with_stdio(0);
  cin.tie(0);

  cin >> N;
  for (int i = 0; i < N - 1; i++)
  {
    int a, b;
    cin >> a >> b;
    g[a].push_back(b);
    g[b].push_back(a);
  }
  dfs(1);

  int M;
  cin >> M;
  for (int i = 0; i < M; i++)
  {
    int a, b;
    cin >> a >> b;
    if (a == 1 || b == 1)
    {
      printf("%d\n", 1);
      continue;
    }
    if (depth[a] > depth[b])
    {
      int tmp = a;
      a = b;
      b = tmp;
    }
    if (depth[a] != depth[b])
    {
      for (int i = MAX; i >= 0; i--)
      {
        if (depth[parent[b][i]] >= depth[a])
          b = parent[b][i];
      }
    }

    auto ret = a;
    if (a != b)
    {
      for (int i = MAX; i >= 0; i--)
      {
        if (parent[b][i] != parent[a][i])
        {
          a = parent[a][i];
          b = parent[b][i];
        }
        ret = parent[a][i];
      }
    }
    printf("%d\n", ret);
    // cout << ret << endl;
  }

  return 0;
}