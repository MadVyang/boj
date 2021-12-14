#include <iostream>
#include <vector>
using namespace std;

int N;
int board[22][22];

vector<int> a, b;

int eval() {
  int A = a.size();
  int pa = 0;
  for (int i = 0; i < A; i++) {
    for (int j = i + 1; j < A; j++) {
      pa += board[a[i]][a[j]] + board[a[j]][a[i]];
    }
  }
  int B = b.size();
  int pb = 0;
  for (int i = 0; i < B; i++) {
    for (int j = i + 1; j < B; j++) {
      pb += board[b[i]][b[j]] + board[b[j]][b[i]];
    }
  }
  return pa > pb ? pa - pb : pb - pa;
}

// i번째를 a나 b로 넣기
int select(int i) {
  if (i == N) {
    return eval();
  }
  int pa = 0, pb = 0;
  a.push_back(i);
  pa = select(i + 1);
  a.pop_back();
  b.push_back(i);
  pb = select(i + 1);
  b.pop_back();
  return min(pa, pb);
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  cin >> N;
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
      cin >> board[i][j];
    }
  }
  cout << select(0) << '\n';

  return 0;
}