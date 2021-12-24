#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

ll N, K;
vector<int> tmp;

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);

  cin >> N >> K;
  int n = N;
  int cnt = 0;
  while (n > 0) {
    tmp.push_back(n % 2);
    cnt += n % 2;
    n /= 2;
  }
  tmp.push_back(0);
  // cout << cnt << endl;
  int sum = 0;
  int buy = 0;
  for (int i = 0; i < (int)tmp.size() - 1; i++) {
    if (cnt <= K) {
      break;
    }
    // sum += (1 << i) * tmp[i];
    // cout << (1 << i) << " " << tmp[i] << " " << sum << endl;
    if (tmp[i] == 2) {
      cnt--;
      tmp[i + 1]++;
    }
    if (tmp[i] == 1) {
      buy += 1 << i;
      tmp[i + 1]++;
    }
  }

  cout << buy << endl;
  return 0;
}