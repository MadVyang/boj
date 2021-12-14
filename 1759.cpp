#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <stack>
#include <math.h>
using namespace std;

int L, C;
char arr[20];
char ms[5] = {'a', 'e', 'i', 'o', 'u'};

vector<char> list;

bool isM(char a) {
  for (char m : ms) {
    if (a == m)
      return true;
  }
  return false;
}

void print() {
  for (auto &c : list)
    cout << c << "";
  cout << '\n';
}

// i번째를 선택하거나 안하거나
void solve(int i, int mcount, int jcount) {
  if (list.size() == L) {
    if (mcount >= 1 && jcount >= 2)
      print();
    return;
  }
  if (i == C)
    return;

  int madd = 0, jadd = 0;
  if (isM(arr[i]))
    madd = 1;
  else
    jadd = 1;
  list.push_back(arr[i]);
  solve(i + 1, mcount + madd, jcount + jadd);
  list.pop_back();

  solve(i + 1, mcount, jcount);
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  cin >> L >> C;
  for (int i = 0; i < C; i++) {
    cin >> arr[i];
  }
  sort(arr, arr + C);
  solve(0, 0, 0);

  return 0;
}

// a c i s t w