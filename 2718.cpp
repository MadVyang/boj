#include <bits/stdc++.h>
using namespace std;
// typedef long long ll;

int T, N;

// int mem[100000];

// int main() {
//   ios_base::sync_with_stdio(false);
//   cin.tie(NULL);
//   cout.tie(NULL);

//   mem[1] = 1;
//   mem[2] = 5;
//   mem[3] = 11;
//   mem[4] = 36;

//   for (int i = 5; i <= 10000; i++) {
//     mem[i] = mem[i - 1] + mem[i - 2] * (mem[2] - 1) + 5 * i + 5;
//   }

//   // cin >> T;
//   // for (int i = 0; i < T; i++) {
//   //   cin >> N;
//   //   cout << mem[N] << "\n";
//   // }
//   for (int i = 1; i <= 10; i++) {
//     // cin >> N;
//     cout << mem[i] << "\n";
//   }

//   return 0;
// }

#include <stdio.h>

int arr[1000000];
// int N;

int sol(int n) {
  if (n == 1)
    return 1;
  if (n == 2)
    return 5;
  if (n == 3)
    return 11;
  if (n == 4)
    return 36;
  if (arr[n])
    return arr[n];

  int r = sol(n - 1) + sol(n - 2) * 4;

  if (n % 2)
    r += 2;
  else
    r += 3;

  int i;
  for (i = 1; (n - i) >= 3; i++) {
    if ((n - i) % 2)
      r += 2 * sol(i);
    else
      r += 3 * sol(i);
  }

  return arr[n] = r;
}

int main() {
  // scanf("%d", &N);
  // printf("%d", sol(N));

  cin >> T;
  for (int i = 0; i < T; i++) {
    cin >> N;
    cout << sol(N) << "\n";
  }
  // for (int i = 1; i <= 10; i++) {
  //   // cin >> N;
  //   cout << mem[i] << "\n";
  // }
  return 0;
}