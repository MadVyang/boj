#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int N;

vector<int> list;
void print() {
  for (int i : list)
    cout << i + 1 << " ";
  cout << '\n';
}
void permutation(int i, int mask) {
  if (list.size() == N) {
    print();
    return;
  }
  if (i == N)
    return;
  if ((mask & (1 << i)) == 0) {
    list.push_back(i);
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
  permutation(0, 0);
  return 0;
}
