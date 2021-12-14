#include <iostream>

using namespace std;

int mem[1500001];
unsigned long long N;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> N;
    N %= 1500000;

    mem[0] = 0;
    mem[1] = 1;

    for (int i = 2; i <= 1500000; i++)
    {
        mem[i] = (mem[i - 1] + mem[i - 2]) % 1000000;
    }
    cout << mem[N] << '\n';

    return 0;
}

// 1000000 => 1500000