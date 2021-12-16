#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

ll N, M;
int sixs[105], ones[105];

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);

  cin >> N >> M;
  int minSix = 1000, minOne = 1000;
  for (int i = 0; i < M; i++) {
    cin >> sixs[i] >> ones[i];
    if (sixs[i] < minSix)
      minSix = sixs[i];
    if (ones[i] < minOne)
      minOne = ones[i];
  }
  int result = (N / 6) * minSix + (N % 6) * minOne;
  if ((N / 6 + 1) * minSix < result)
    result = (N / 6 + 1) * minSix;
  if ((N * minOne) < result)
    result = N * minOne;
  cout << result << endl;

  return 0;
}