#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int N;

vector<int> nums;
vector<ll> ans;

void solve(int i) {
  if (i < 0) {
    if (nums.size() == 0)
      return;
    ll res = 0;
    for (int i : nums) {
      res *= 10;
      res += i;
    }
    auto it = find(ans.begin(), ans.end(), res);
    if (it == ans.end())
      ans.push_back(res);
    return;
  }

  nums.push_back(i);
  solve(i - 1);
  nums.pop_back();
  solve(i - 1);
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);

  cin >> N;
  solve(9);
  sort(ans.begin(), ans.end());
  // for (int i = 0; i < ans.size(); i++)
  //   cout << i << " " << ans[i] << " / ";
  // cout << endl;
  // cout << ans.size() << endl;
  if (N >= ans.size())
    cout << "-1\n";
  else
    cout << ans[N] << endl;

  return 0;
}