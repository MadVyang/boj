#include <iostream>
#include <vector>
using namespace std;

int N;
int a, b;
vector<pair<char, short>> list;

//
int mem[1600000];

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  cin >> N;
  for (int i = 0; i < N; i++) {
    cin >> a >> b;
    list.push_back(make_pair(a, b));
  }

  int _max = 0;
  for (int i = 0; i < N; i++) {
    if (i > 0 && mem[i] < _max)
      mem[i] = _max;
    list[i].second += mem[i];
    if (mem[i] > _max)
      _max = mem[i];
    if (list[i].first + i <= N) {
      if (mem[list[i].first + i] < list[i].second)
        mem[list[i].first + i] = list[i].second;
    }
    // mem[i + 1] = mem[i + 1] < mem[i] ? mem[i] : mem[i + 1];
    // mem[i + list[i].first] = mem[i + list[i].first] < mem[i] + list[i].second
    //                              ? mem[i] + list[i].second
    //                              : mem[i + list[i].first];
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