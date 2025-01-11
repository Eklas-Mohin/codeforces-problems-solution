def main():
    n = int(input())
    lst = list(map(int, input().split()))
    cnt, mx = 1, 1

    for i in range(1, n):
        if lst[i] >= lst[i - 1]:
            cnt += 1
            mx = max(cnt, mx)
        else:
            cnt = 1

    print(mx)

if __name__ == '__main__':
    main()
