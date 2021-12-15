#include <bits/stdc++.h>
using namespace std;

int N;
int num[1000002];
vector<int> comp;

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  cin >> N;
  for (int i = 0; i < N; i++) {
    cin >> num[i];
    comp.push_back(num[i]);
  }
  sort(comp.begin(), comp.end());
  comp.erase(unique(comp.begin(), comp.end()), comp.end());

  for (int i = 0; i < N; i++) {
    int k = lower_bound(comp.begin(), comp.end(), num[i]) - comp.begin();
    cout << k << " ";
  }
  cout << endl;

  return 0;
}