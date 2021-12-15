#include <iostream>

using namespace std;

unsigned long long mem[10001];

int N;

int main()
{
    mem[0] = 0;
    mem[1] = 1;
    for (int i = 2; i <= 10000; i++)
    {
        mem[i] = mem[i - 1] + mem[i - 2];
    }

    cin >> N;
    cout << mem[N] << endl;

    return 0;
}