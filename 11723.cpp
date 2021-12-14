#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <math.h>
using namespace std;

int M;
int arr[22];

string cmd;
int x;

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  cin >> M;
  for (int i = 0; i < M; i++) {
    cin >> cmd;
    if (cmd == "add") {
      cin >> x;
      arr[x] = 1;
    } else if (cmd == "remove") {
      cin >> x;
      arr[x] = 0;
    } else if (cmd == "check") {
      cin >> x;
      cout << arr[x] << "\n";
    } else if (cmd == "toggle") {
      cin >> x;
      if (arr[x])
        arr[x] = 0;
      else
        arr[x] = 1;
    } else if (cmd == "all") {
      for (int j = 1; j <= 20; j++)
        arr[j] = 1;
    } else if (cmd == "empty") {
      for (int j = 1; j <= 20; j++)
        arr[j] = 0;
    }
  }

  return 0;
}
