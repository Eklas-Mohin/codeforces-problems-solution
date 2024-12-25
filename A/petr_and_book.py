def main():
    n = int(input())
    p = list(map(int, input().split()))

    while True:
        for i in range(7):
            n = n - p[i]
            if n <= 0:
                print(i + 1)
                return

if __name__ == '__main__':
    main()