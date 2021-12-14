#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int A, B, C;
int mem[200][200][200];

ll w(int a, int b, int c) {
  // cout << a << " " << b << " " << c << "\n";
  if (mem[a + 100][b + 100][c + 100])
    return mem[a + 100][b + 100][c + 100];
  if (a <= 0 || b <= 0 || c <= 0)
    return 1;
  if (a > 20 || b > 20 || c > 20)
    return w(20, 20, 20);
  if (a == b && b == c)
    return 1LL << a;
  if (a < b && b < c)
    // return 1LL << min(min(a, b), c);
    return mem[a + 100][b + 100][c + 100] =
               w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c);
  return mem[a + 100][b + 100][c + 100] = w(a - 1, b, c) + w(a - 1, b - 1, c) +
                                          w(a - 1, b, c - 1) -
                                          w(a - 1, b - 1, c - 1);
}

void test(int a, int b, int c) {
  cout << "w(" << a << ", " << b << ", " << c << ") = " << w(a, b, c) << "\n";
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  // for (int i = 0; i <= 50; i++)
  //   for (int j = 0; j <= 50; j++)
  //     for (int k = 0; k <= 50; k++)
  //       test(i, j, k);

  // for (int i = 0; i <= 50; i++)
  //   test(i, i, i);

  while (true) {
    cin >> A >> B >> C;
    if (A == -1 && B == -1 && C == -1)
      break;
    test(A, B, C);
  }

  // test(5, 10, 11);

  return 0;
}