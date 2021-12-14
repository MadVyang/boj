#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

unordered_map<string, int> hash_map;

int t11, t12, t21, t22, t31, t32;
int a, b, c;
int main() {
  scanf("%d:%d", &t11, &t12);
  scanf("%d:%d", &t21, &t22);
  scanf("%d:%d", &t31, &t32);
  a = t11 * 60 + t12;
  b = t21 * 60 + t22;
  c = t31 * 60 + t32;

  int count = 0;
  do {
    int t1, t2;
    char name[30];
    scanf("%d:%d ", &t1, &t2);
    scanf("%s", name);

    int t = t1 * 60 + t2;
    if (t <= a) {
      if (!hash_map.count(name)) {
        hash_map[name] = 1;
      }
    }
    if (t >= b && t <= c) {
      if (hash_map[name] == 1) {
        hash_map[name] = -1;
        count++;
      }
    }

  } while (getc(stdin) == '\n');
  printf("%d\n", count);
  return 0;
}