#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    #ifndef ONLINE_JUDGE
        freopen("input.txt", "r", stdin);
        freopen("output.txt", "w", stdout);
    #endif

    int n, mx = 0;
    string str, ans, temp = "";
    map<string, int> p;
    cin >> n >> str;

    for (int i = 1; i < n; ++i) {
        temp = temp + str[i - 1] + str[i];
        p[temp] += 1;
        if (p[temp] > mx) {
            mx = p[temp];
            ans = temp;
        }
        temp = "";
    }

    cout << ans << endl;

    return 0;
}
