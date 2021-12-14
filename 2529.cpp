#include <iostream>
#include <vector>
using namespace std;

int N;
char arr[20];

int mx, mn;

vector<int> list, mxlist, mnlist;

unsigned long long value(vector<int> a) {
  unsigned long long v = 0;
  for (int i : a) {
    v *= 10;
    v += i;
  }
  return v;
}

void print(vector<int> a) {
  for (int i : a)
    cout << i << "";
  cout << endl;
}

void solve(int i, int mask) {
  // print(list);
  if (list.size() == N + 1) {
    if (arr[N - 1] == '<' && list[N - 1] > list[N])
      return;
    if (arr[N - 1] == '>' && list[N - 1] < list[N])
      return;
    if (value(list) < value(mnlist) || mnlist.size() == 0) {
      mnlist.clear();
      mnlist.assign(list.begin(), list.end());
    }
    if (value(list) > value(mxlist) || mxlist.size() == 0) {
      mxlist.clear();
      mxlist.assign(list.begin(), list.end());
    }
    return;
  }
  if (i == 10)
    return;
  for (int j = 0; j < (int)list.size() - 1; j++) {
    // cout << i << '\n';
    if (arr[j] == '<' && list[j] > list[j + 1])
      return;
    if (arr[j] == '>' && list[j] < list[j + 1])
      return;
  }
  solve(i + 1, mask);
  if ((mask & (1 << i)) == 0) {
    list.push_back(i);
    solve(0, mask | (1 << i));
    list.pop_back();
  }
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  cin >> N;
  for (int i = 0; i < N; i++) {
    cin >> arr[i];
  }
  solve(0, 0);
  print(mxlist);
  print(mnlist);

  return 0;
}