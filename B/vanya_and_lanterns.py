def main():
    n, m = map(int, input().split())
    lst = list(map(int, input().split()))
    lst.sort()
    ans = max(lst[0], m - lst[n - 1])

    for i in range(1, n):
        ans = max(ans, (lst[i] - lst[i - 1]) / 2)
    print(ans)

if __name__== '__main__':
    main()