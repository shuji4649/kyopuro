#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
int main()
{
    int N;
    cin >> N;
    string S;
    cin >> S;

    long long ans = 0;
    long long NumSum = 0;

    for (int i = 0; i < N; i++)
    {
        ans *= 10;
        int s = stoi(S[i]); 
        NumSum += (i + 1) * s;
        ans += NumSum;
    }

    cout << ans << endl;
    return 0;
}