def main():
    n, x, y = map(int, input().split())
    k = (n * y) / 100

    if int(k) != k:
        k = int(k + 1)

    print(max(0, int(k - x)))

if __name__ == '__main__':
    main()
