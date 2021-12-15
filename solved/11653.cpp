#include <bits/stdc++.h>
using namespace std;

int N;
bool check[10000005];
vector<int> primes;

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  for (int i = 2; i <= 10000; i++)
    for (int j = i * 2; j <= 10000; j += i)
      check[j] = true;

  for (int i = 2; i <= 10000; i++)
    if (!check[i])
      primes.push_back(i);
  // for (int i : primes) {
  //   cout << i << "\n";
  // }

  cin >> N;
  for (int i : primes) {
    while (N % i == 0) {
      cout << i << "\n";
      N /= i;
    }
  }
  if (N != 1)
    cout << N << "\n";
  // if (N == 1)
  //   cout << "1\n";

  return 0;
}