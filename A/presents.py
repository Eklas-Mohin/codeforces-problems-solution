def main():
    n = int(input())
    arr = list(map(int, input().split()))
    ans = [1] * n

    for i in range(1, n):
        ans[arr[i] - 1] = i + 1

    print(*ans)

if __name__ == '__main__':
    main()