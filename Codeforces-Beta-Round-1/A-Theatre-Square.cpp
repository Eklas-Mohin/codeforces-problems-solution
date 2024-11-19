#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    #ifndef ONLINE_JUDGE
        freopen("input.txt", "r", stdin);
        freopen("output.txt", "w", stdout);
    #endif

    long long n, m, a;
    cin >> n >> m >> a;

    cout << ((n + a - 1) / a) * ((m + a - 1) / a) << endl;

    return 0;
}