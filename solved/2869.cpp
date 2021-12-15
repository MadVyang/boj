#include <iostream>

using namespace std;

int A, B, V;
int main()
{
    cin >> A >> B >> V;
    if (A == V)
        cout << 1 << endl;
    else if ((V - B) % (A - B) == 0)
        cout << (V - B) / (A - B) << endl;
    else
        cout << (V - B) / (A - B) + 1 << endl;

    return 0;
}

// (A-B)*N+A>=V
// N>= (V-A)/(A-B)