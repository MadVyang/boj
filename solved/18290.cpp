#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <stack>
#include <math.h>
using namespace std;

int N, M, K;
int board[20][20];

vector<pair<int, int>> list;

const int _MIN = -10000 * 100;

bool check(int i, int j) {
  for (auto &p : list) {
    if (abs(p.first - i) + abs(p.second - j) == 1)
      return false;
  }
  return true;
}

// (i,j)를 선택하거나 안했을때 최대값
int solve(int i, int j) {
  if (list.size() == K) {
    int sum = 0;
    for (auto &p : list)
      sum += board[p.first][p.second];
    return sum;
  }
  if (i >= N)
    return _MIN;
  if (j >= M)
    return solve(i + 1, 0);
  int yes = _MIN, no = _MIN;
  if (check(i, j)) {
    list.push_back(make_pair(i, j));
    yes = solve(i, j + 1);
    list.pop_back();
  }
  no = solve(i, j + 1);

  return max(yes, no);
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  cin >> N >> M >> K;
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < M; j++) {
      cin >> board[i][j];
    }
  }

  cout << solve(0, 0) << '\n';

  return 0;
}
