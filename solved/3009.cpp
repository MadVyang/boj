#include <iostream>

using namespace std;

int A[2000];
int B[2000];
int a, b;
int main()
{
    for (int i = 0; i < 3; i++)
    {
        cin >> a >> b;
        A[a] = 1 - A[a];
        B[b] = 1 - B[b];
    }
    for (int i = 0; i < 1001; i++)
    {
        if (A[i] == 1)
            a = i;
        if (B[i] == 1)
            b = i;
    }
    cout << a << " " << b << endl;

    return 0;
}
