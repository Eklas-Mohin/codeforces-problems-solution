#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    #ifndef ONLINE_JUDGE
        freopen("input.txt", "r", stdin);
        freopen("output.txt", "w", stdout);
    #endif

    int n, k;
    cin >> n >> k;

    while (k--) {
        if (n % 10 == 0) {
            n /= 10;
        } else {
            n -= 1;
        }
    }

    cout << n << endl;

    return 0;
}
