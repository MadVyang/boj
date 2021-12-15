#include <stdio.h>
#define max(a, b) a > b ? a : b;

int N, K;
int W[100], V[100];
int mem[105][100005];

int solve(int toAdd, int weight, int value) {
  if (toAdd == N)
    return 0;
  if (mem[toAdd][weight]) {
    return mem[toAdd][weight];
  }

  int whenNotAdd = 0, whenAdd = 0;
  whenNotAdd = solve(toAdd + 1, weight, value);
  if (weight + W[toAdd] <= K)
    whenAdd = solve(toAdd + 1, weight + W[toAdd], value + V[toAdd]) + V[toAdd];
  int r = max(whenAdd, whenNotAdd);
  mem[toAdd][weight] = r;
  return r;
}

int main() {
  scanf("%d%d", &N, &K);
  for (int i = 0; i < N; i++) {
    scanf("%d%d", &W[i], &V[i]);
  }
  int r = solve(0, 0, 0);
  printf("%d\n", r);
  return 0;
}