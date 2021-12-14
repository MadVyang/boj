#include <iostream>
#include <vector>
using namespace std;

int N;
int a, b;
vector<pair<char, short>> list;

//
int mem[1500005];
// int mem2[1500005];

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  cin >> N;
  for (int i = 0; i < N; i++) {
    cin >> a >> b;
    list.push_back(make_pair(a, b));
  }

  int max = 0;
  for (int i = 0; i < N; i++) {
    if (i > 0 && mem[i] < max)
      mem[i] = max;
    list[i].second += mem[i];
    if (mem[i] > max)
      max = mem[i];
    if (list[i].first + i <= N) {
      if (mem[list[i].first + i] < list[i].second)
        mem[list[i].first + i] = list[i].second;
    }
  }

  int answer = 0;
  for (int i = 0; i <= N; i++) {
    // cout << mem[i] << " ";
    if (answer < mem[i])
      answer = mem[i];
  }
  // cout << endl;
  cout << answer << endl;

  return 0;
}