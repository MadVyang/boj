#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

ll N, M;
vector<int> arr;

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);

  cin >> N >> M;
  for (int i = 1; i <= N; i++)
    arr.push_back(i);

  int cnt = 0;
  int p = 0;
  for (int i = 0; i < M; i++) {
    int a;
    cin >> a;
    int index = find(arr.begin(), arr.end(), a) - arr.begin();
    if (index < p) {
      if (p - index <= (int)(arr.size()) / 2)
        cnt += p - index;
      else
        cnt += (int)(arr.size()) + index - p;
    } else {
      if (index - p <= (int)(arr.size()) / 2)
        cnt += index - p;
      else
        cnt += (int)(arr.size()) + p - index;
    }
    p = index;
    arr.erase(arr.begin() + p);
  }
  cout << cnt << endl;

  return 0;
}