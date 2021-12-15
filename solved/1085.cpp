#include <iostream>
#include <cmath>

using namespace std;

int x, y, w, h;
int main()
{
    cin >> x >> y >> w >> h;
    int a = w - x, b = h - y;
    cout << min(min(x, y), min(a, b)) << endl;
    return 0;
}

// (A-B)*N+A>=V
// N>= (V-A)/(A-B)