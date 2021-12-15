#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

vector<int> nums;
int N, M, a;

// int find(int i, int low, int high) {
//   // int low = 0, high = (int)nums.size() - 1;
//   int mid;
//   while (low <= high) {
//     mid = (low + high) / 2;
//     if (nums[mid] == i)
//       return mid;
//     if (nums[mid] < i)
//       low = mid + 1;
//     else
//       high = mid - 1;
//   }
//   return -1;
// }

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  cin >> N;
  for (int i = 0; i < N; i++) {
    cin >> a;
    nums.push_back(a);
  }
  sort(nums.begin(), nums.end());
  cin >> M;
  for (int i = 0; i < M; i++) {
    cin >> a;

    auto ub = upper_bound(nums.begin(), nums.end(), a);
    auto lb = lower_bound(nums.begin(), nums.end(), a);

    cout << ub - lb << " ";
  }
  cout << "\n";

  return 0;
}