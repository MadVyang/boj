#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <math.h>
using namespace std;

int K;
int arr[15];

vector<int> list;
void print() {
  for (int i : list)
    cout << i << " ";
  cout << "\n";
}
void solve(int i) {
  if (list.size() == 6) {
    print();
    return;
  }
  if (i == K)
    return;
  list.push_back(arr[i]);
  solve(i + 1);
  list.pop_back();
  solve(i + 1);
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  while (true) {
    cin >> K;
    if (K == 0)
      break;
    for (int i = 0; i < K; i++)
      cin >> arr[i];
    solve(0);
    cout << "\n";
  }

  return 0;
}
