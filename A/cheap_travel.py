def main():
    n, m, a, b = list(map(int, input().split()))

    p1 = n * a
    p2 = (int((n + m - 1) / m)) * b
    p3 = p2 - b
    k = n - ((p3 // b) * m)
    p3 = p3 + k * a
    ans = min(p1, min(p2, p3))

    print(ans)

if __name__ == '__main__':
    main()