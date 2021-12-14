#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int N;
int arr[25];
vector<int> sub, tmp;
void gen(int i) {
  if (i == N) {
    int sum = 0;
    for (auto k : tmp)
      sum += k;
    sub.push_back(sum);
    return;
  }
  tmp.push_back(arr[i]);
  gen(i + 1);
  tmp.pop_back();
  gen(i + 1);
}
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  cin >> N;
  for (int i = 0; i < N; i++) {
    cin >> arr[i];
  }
  gen(0);
  sort(sub.begin(), sub.end());
  // for (auto aa : sub)
  //   cout << aa << " ";
  // cout << endl;

  int ans = *(sub.end() - 1) + 1;
  // cout << ans << endl;
  for (int i = 0; i < (int)sub.size() - 1; i++) {
    if (sub[i] != sub[i + 1] && sub[i] + 1 != sub[i + 1]) {
      ans = sub[i] + 1;
      break;
    }
  }
  cout << ans << endl;
  return 0;
}
