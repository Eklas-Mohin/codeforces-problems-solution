def main():
    t = int(input())

    for _ in range(t):
        a, b = map(int, input().split())
        k = min(a + a, b + b)
        k = max(k, max(a, b))
        print(k ** 2)

if __name__ == '__main__':
    main()