#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

ll N;
char s[52];

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);

  cin >> N;
  string t;
  cin >> t;
  int l = t.length();
  for (int j = 0; j < l; j++) {
    s[j] = t[j];
  }
  for (int i = 1; i < N; i++) {
    cin >> t;
    for (int j = 0; j < l; j++) {
      if (s[j] != t[j])
        s[j] = '?';
    }
  }
  cout << s << "\n";

  return 0;
}