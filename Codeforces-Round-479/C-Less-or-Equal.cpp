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
    int arr[n];
    for (int &i : arr) {
        cin >> i;
    }

    sort(arr, arr + n);
    int x = arr[0];
    if (k > 1) {
        x = arr[k - 1];
    }

    if (k < n && arr[k] == x) {
        x = -1;
    }

    if (k == 0) {
        x = arr[0] - 1;
    }

    if (x == 0) {
        x = -1;
    }

    cout << x << endl;

    return 0;
}
