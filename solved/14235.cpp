#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int n;
priority_queue<int> q;

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);

  int a, value;
  cin >> n;
  for (int i = 0; i < n; i++) {
    cin >> a;
    for (int j = 0; j < a; j++) {
      cin >> value;
      q.push(value);
    }
    if (a == 0) {
      if (q.empty())
        cout << "-1\n";
      else {
        cout << q.top() << "\n";
        q.pop();
      }
    }
  }

  return 0;
}