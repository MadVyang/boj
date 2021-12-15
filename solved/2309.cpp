#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int arr[9];

vector<int> selection;
int current = 0;
bool result = false;

void printS() {
  for (int i = 0; i < selection.size(); i++)
    cout << selection[i] << " ";
  cout << ": (" << current << " " << selection.size() << ")" << ' ';
}
// i번째를 선택하거나 안하기
// 선택할 번호, 현재 선택한 갯수
void select(int i, int count) {
  // printS();
  // cout << count << endl;
  if (count == 7) {
    if (current == 100) {
      // cout << "sibal\n";
      result = true;
    }
    return;
  }
  if (i == 9)
    return;
  if (result)
    return;

  current += arr[i];
  selection.push_back(arr[i]);
  select(i + 1, count + 1);
  current -= arr[i];
  selection.pop_back();

  select(i + 1, count);
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  for (int i = 0; i < 9; i++) {
    cin >> arr[i];
  }
  sort(arr, arr + 9);
  select(0, 0);
  for (int i = 0; i < 7; i++) {
    cout << selection[i] << '\n';
  }
}