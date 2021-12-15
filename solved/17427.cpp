#include <bits/stdc++.h>
using namespace std;

int N;

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  long long r = 0;
  cin >> N;
  for (int i = 1; i <= N; i++) {
    r += i * (N / i);
  }
  cout << r << endl;

  return 0;
}
