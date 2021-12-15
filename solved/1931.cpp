#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;

int N;
vector<pair<int, int>> arr;

bool compare(pair<int, int> a, pair<int, int> b)
{
    if (a.second == b.second)
    {
        return a.first < b.first;
    }
    else
    {
        return a.second < b.second;
    }
}

int main()
{
    scanf("%d", &N);
    for (int i = 0; i < N; i++)
    {
        int a, b;
        scanf("%d%d", &a, &b);
        pair<int, int> p(a, b);
        arr.push_back(p);
    }
    sort(arr.begin(), arr.end(), compare);

    int c = 0;
    int count = 0;
    for (int i = 0; i < N; i++)
    {
        if (c <= arr[i].first)
        {
            count++;
            c = arr[i].second;
        }
    }
    printf("%d\n", count);

    return 0;
}