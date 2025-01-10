def main():
    n, h = map(int, input().split())
    hl = list(map(int, input().split()))
    ans = n

    for i in range(n):
        if hl[i] > h:
            ans += 1

    print(ans)

if __name__ == '__main__':
    main()