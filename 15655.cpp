#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <stack>
using namespace std;

int N, M;
int arr[10];

vector<int> sel;

void print() {
  for (int i = 0; i < M; i++)
    cout << sel[i] << " ";
  cout << '\n';
}

// i번째를 고르거나 안고른 뒤 i+1번째로 넘어가기
void solve(int i, int mask) {
  // cout << i << " " << mask << " " << (1 << (i + 1)) << '\n';
  if (sel.size() == M) {
    print();
    return;
  }
  if (i == N)
    return;

  if ((mask & (1 << (i))) == 0) {
    // cout << "sibal\n";
    sel.push_back(arr[i]);
    solve(i, mask | (1 << (i)));
    sel.pop_back();
  }
  solve(i + 1, mask);
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  cin >> N >> M;
  for (int i = 0; i < N; i++)
    cin >> arr[i];
  sort(arr, arr + N);
  // for (int i = 0; i < N; i++)
  //   cout << arr[i] << " ";
  // cout << '\n';
  solve(0, 0);

  return 0;
}