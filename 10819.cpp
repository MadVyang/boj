#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int N;
int arr[10];
int mx = 0;

vector<int> list;
void print() {
  for (int i : list)
    cout << i + 1 << " ";
  cout << '\n';
}

int eval() {
  int r = 0;
  for (int i = 0; i < N - 1; i++) {
    r += list[i] > list[i + 1] ? list[i] - list[i + 1] : list[i + 1] - list[i];
  }
  return r;
}
void permutation(int i, int mask) {
  if (list.size() == N) {
    if (eval() > mx)
      mx = eval();
    // print();
    return;
  }
  if (i == N)
    return;
  if ((mask & (1 << i)) == 0) {
    list.push_back(arr[i]);
    permutation(0, mask | (1 << i));
    list.pop_back();
  }
  permutation(i + 1, mask);
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  cin >> N;
  for (int i = 0; i < N; i++)
    cin >> arr[i];
  permutation(0, 0);
  cout << mx << endl;
  return 0;
}
