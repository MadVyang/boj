#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

int N;
string board[55];
vector<pair<pair<int, int>, pair<int, int>>> cands;

void swap(pair<pair<int, int>, pair<int, int>> cand) {
  int tmp = board[cand.first.first][cand.first.second];
  board[cand.first.first][cand.first.second] =
      board[cand.second.first][cand.second.second];
  board[cand.second.first][cand.second.second] = tmp;
}

int valuation() {
  int ver = 0;
  for (int i = 0; i < N; i++) {
    int _ver = 1;
    for (int j = 1; j < N; j++) {
      if (board[i][j - 1] != board[i][j]) {
        if (ver < _ver)
          ver = _ver;
        _ver = 1;
      } else
        _ver++;
    }
    if (ver < _ver)
      ver = _ver;
  }
  int hor = 0;
  for (int j = 0; j < N; j++) {
    int _hor = 1;
    for (int i = 1; i < N; i++) {
      if (board[i - 1][j] != board[i][j]) {
        if (hor < _hor)
          hor = _hor;
        _hor = 1;
      } else
        _hor++;
    }
    if (hor < _hor)
      hor = _hor;
  }
  // if (hor > 14 || ver > 14)
  //   cout << ver << " " << hor << "\n";
  return ver > hor ? ver : hor;
}

void print() {
  for (int i = 0; i < N; i++) {
    cout << board[i] << '\n';
  }
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  cin >> N;
  for (int i = 0; i < N; i++) {
    cin >> board[i];
  }

  // find candidates
  for (int i = 0; i < N - 1; i++) {
    for (int j = 0; j < N; j++) {
      if (board[i][j] != board[i + 1][j])
        cands.push_back(make_pair(make_pair(i, j), make_pair(i + 1, j)));
    }
  }
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N - 1; j++) {
      if (board[i][j] != board[i][j + 1])
        cands.push_back(make_pair(make_pair(i, j), make_pair(i, j + 1)));
    }
  }

  int max = -1;
  for (auto &cand : cands) {
    swap(cand);
    int value = valuation();
    // if (value > 14) {
    //   print();
    //   cout << '\n';
    // }
    if (max < value)
      max = value;
    swap(cand);
  }
  cout << max << '\n';

  return 0;
}