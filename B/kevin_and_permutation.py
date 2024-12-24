def main():
    t = int(input())

    for _ in range(t):
        m = list(map(int, input().split()))
        n, k = m[0], m[1]
        x = (n + k - 1) // k
        mn = 1
        cur = x + 1
        ans = []

        for i in range(1, n + 1):
            if i % k == 0:
                ans.append(mn)
                mn += 1
            else:
                ans.append(cur)
                cur += 1
                
        if n % k != 0:
            ans[n - 1] = mn

        print(*ans)

if __name__ == '__main__':
    main()
