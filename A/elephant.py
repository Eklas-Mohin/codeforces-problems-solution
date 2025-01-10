def main():
    n = int(input())
    k, ans = 5, 0

    while k > 0:
        ans = ans + n // k
        n = n % k
        k = k - 1

    print(ans)


if __name__ == '__main__':
    main()
