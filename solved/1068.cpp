#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

ll N;
int p[55];

bool isAlive(int i) {
  if (i == -1)
    return true;
  if (i == -2)
    return false;
  return isAlive(p[i]);
}

bool isLeaf(int i) {
  for (int j = 0; j < N; j++) {
    if (p[j] == i)
      return false;
  }
  return isAlive(p[i]);
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);

  cin >> N;
  int root = -1;
  for (int i = 0; i < N; i++) {
    cin >> p[i];
    if (p[i] == -1)
      root = i;
  }
  int a;
  cin >> a;
  p[a] = -2;

  int cnt = 0;
  for (int i = 0; i < N; i++) {
    if (isLeaf(i))
      cnt++;
  }
  cout << cnt << endl;

  return 0;
}