#include <iostream>
#include <queue>

using namespace std;

int N, M, V;
bool graph[1001][1001];
bool check[1001];
queue<int> bfsQueue;

void _dfs(int v)
{
    if (check[v])
        return;
    check[v] = true;
    cout << v << ' ';
    for (int i = 0; i <= N; i++)
    {
        if (graph[v][i])
        {
            _dfs(i);
        }
    }
}
void dfs(int v)
{
    for (int i = 0; i <= N; i++)
    {
        check[i] = false;
    }
    _dfs(v);
    cout << '\n';
}

void bfs()
{
    for (int i = 0; i <= N; i++)
    {
        check[i] = false;
    }
    while (bfsQueue.size())
    {
        int v = bfsQueue.front();
        bfsQueue.pop();
        if (check[v])
            continue;
        check[v] = true;
        cout << v << ' ';
        for (int i = 0; i <= N; i++)
        {
            if (graph[v][i] && !check[i])
            {
                bfsQueue.push(i);
            }
        }
    }
    cout << '\n';
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> N >> M >> V;
    int a, b;
    for (int i = 0; i < M; i++)
    {
        cin >> a >> b;
        graph[a][b] = true;
        graph[b][a] = true;
    }
    dfs(V);

    bfsQueue.push(V);
    bfs();

    return 0;
}