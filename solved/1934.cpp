#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int T;

int gcd(int a, int b) {
  if (a < b)
    return gcd(b, a);
  if (a % b == 0)
    return b;
  return gcd(b, a % b);
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  cin >> T;
  for (int i = 0; i < T; i++) {
    int A, B;
    cin >> A >> B;
    cout << A * B / gcd(A, B) << "\n";
  }

  return 0;
}
