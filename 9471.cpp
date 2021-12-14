#include <iostream>

using namespace std;

int mem[10000000];
bool remain[1000001];
int P;
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> P;
    int N, M;
    for (int i = 1; i <= P; i++)
    {
        cin >> N >> M;
        for (int j = 0; j <= 1000001; j++)
        {
            remain[j] = false;
        }
        mem[0] = 0;
        mem[1] = 1;
        // remain[mem[0]] = true;
        remain[mem[1]] = true;

        int check = false;
        int checkCycle = -1;
        for (int j = 2;; j++)
        {
            mem[j] = (mem[j - 1] + mem[j - 2]) % M;
            if (remain[mem[j]])
            {
                if (!check)
                {
                    check = true;
                    checkCycle = j - 1;
                }
                else if (mem[j] == mem[j % checkCycle])
                {
                    if (j == checkCycle * 2)
                    {
                        cout << i << " " << checkCycle << '\n';
                        break;
                    }
                }
                else
                {
                    check = false;
                    checkCycle = j - 1;
                }
            }
            else
            {
                check = false;
                remain[mem[j]] = true;
            }
        }
    }

    return 0;
}

// 1000000 => 1500000