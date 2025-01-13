def main():
    t = int(input())

    for _ in range(t):
        x, y, n = map(int, input().split())
        k = (n // x) * x
        k = k + y
        if k > n:
            k = k - x
        print(k)

if __name__ == '__main__':
    main()