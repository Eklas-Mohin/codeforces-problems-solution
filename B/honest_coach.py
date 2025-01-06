def main():
    t = int(input())

    for i in range(t):
        n = int(input())
        lst = list(map(int, input().split()))
        lst.sort()
        ans = 1e12
        for j in range(1, n):
            k = lst[j] - lst[j - 1]
            ans = min(ans, k)
        print(ans)

if __name__ == '__main__':
    main()