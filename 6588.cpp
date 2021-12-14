#include <bits/stdc++.h>
using namespace std;

int N;
bool arr[1000005];
vector<int> primes;

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  for (int i = 2; i <= 1000000; i++)
    arr[i] = true;
  for (int i = 2; i <= 1000000; i++) {
    for (int j = i + i; j <= 1000000; j += i) {
      arr[j] = false;
    }
  }
  for (int i = 2; i <= 1000000; i++)
    if (arr[i]) {
      primes.push_back(i);
      // cout << i << endl;
    }

  while (true) {
    cin >> N;
    if (N == 0)
      break;
    for (int p : primes) {
      if (arr[N - p]) {
        cout << N << " = " << p << " + " << N - p << "\n";
        break;
      }
    }
  }

  return 0;
}
