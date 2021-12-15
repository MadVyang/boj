#include <bits/stdc++.h>
using namespace std;

typedef unsigned long long ull;

int N, T;
ull H;

priority_queue<ull> q;

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  cin >> N >> H >> T;
  ull a;
  for (int i = 0; i < N; i++) {
    cin >> a;
    q.push(a);
  }
  ull max = 0;
  int t;
  for (t = 0; t < T; t++) {
    max = q.top();
    // cout << max << "\n";
    if (max < H)
      break;
    if (max > 1)
      max /= 2;
    // cout << max << "\n";
    q.pop();
    q.push(max);
  }
  max = q.top();
  if (max < H) {
    cout << "YES"
         << "\n" << t << "\n";
  } else {
    cout << "NO"
         << "\n" << max << "\n";
  }

  return 0;
}
