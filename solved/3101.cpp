#include <stdio.h>

unsigned long long N, K;
int main(void) {
  scanf("%d %d\n", &N, &K);

  int arr[300000];
  for (int i = 0; i < N; i++)
    arr[i] = i + 1;
  for (int i = 0; i < N; i++)
    arr[i + N] = N - i - 1;

  bool even = true;
  unsigned long long tx = 0, ty = 0;
  unsigned long long ans = 1;

  for (int i = 0; i < K; i++) {
    char c;
    scanf("%c", &c);
    if (c == 'U') {
      ty--;
      if (ty >= N - 1)
        tx++;
    }
    if (c == 'D') {
      ty++;
      if (ty > N - 1)
        tx--;
    }
    if (c == 'L') {
      ty--;
      if (ty < N - 1)
        tx--;
    }
    if (c == 'R') {
      ty++;
      if (ty <= N - 1)
        tx++;
    }
    even = !even;

    unsigned long long base;
    if (ty <= N - 1)
      base = ty * (ty + 1) / 2 + 1;
    else {
      unsigned long long tmp = N * 2 - ty - 1;
      base = N * N - tmp * (tmp + 1) / 2 + 1;
    }
    unsigned long long offset = even ? tx : arr[ty] - tx - 1;
    ans += base + offset;
  }
  printf("%llu", ans);
}