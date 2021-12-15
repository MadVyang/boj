#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int N;

// vector<int> list;
// void print() {
//   for (int i : list)
//     cout << i + 1 << " ";
//   cout << endl;
// }
// void permutation(int i, int mask) {
//   if (list.size() == N) {
//     // print();
//     return;
//   }
//   if (i == N)
//     return;
//   if ((mask & (1 << i)) == 0) {
//     list.push_back(i);
//     permutation(0, mask | (1 << i));
//     list.pop_back();
//   }
//   permutation(i + 1, mask);
// }

int arr[10005];

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  cin >> N;
  for (int i = 0; i < N; i++)
    cin >> arr[i];
  int tmp = arr[0];
  prev_permutation(arr, arr + N);
  if (tmp < arr[0] || N == 1) {
    cout << "-1\n";
    return 0;
  }
  for (int i = 0; i < N; i++)
    cout << arr[i] << " ";
  cout << endl;
  return 0;
}
