#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int N;
vector<int> origin, sorted;
vector<bool> check;

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);

  cin >> N;
  for (int i = 0; i < N; i++) {
    int a;
    cin >> a;
    origin.push_back(a);
    sorted.push_back(a);
    check.push_back(true);
  }
  sort(sorted.begin(), sorted.end());
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
      if (check[j] && origin[i] == sorted[j]) {
        cout << j << " ";
        check[j] = false;
        break;
      }
    }
  }
  cout << "\n";

  return 0;
}