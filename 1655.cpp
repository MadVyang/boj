#include <stdio.h>
#include <queue>

using namespace std;

int N;
int a;
priority_queue<int, vector<int>, less<int>> maxq;
priority_queue<int, vector<int>, greater<int>> minq;

int main() {
  scanf("%d", &N);
  for (int i = 0; i < N; i++) {
    scanf("%d", &a);
    if (maxq.size() <= minq.size())
      maxq.push(a);
    else
      minq.push(a);
    if (maxq.size() > 0 && minq.size() > 0 && maxq.top() > minq.top()) {
      int a = maxq.top(), b = minq.top();
      maxq.pop();
      minq.pop();
      maxq.push(b);
      minq.push(a);
    }
    printf("%d\n", maxq.top());
  }

  return 0;
}