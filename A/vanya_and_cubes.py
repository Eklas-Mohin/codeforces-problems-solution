def main():
    n = int(input())
    a, b, ans = 1, 2, 0

    while a <= n:
        ans += 1
        n = n - a
        a = a + b
        b += 1

    print(ans)

if __name__ == '__main__':
    main()