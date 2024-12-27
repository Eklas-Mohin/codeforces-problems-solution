def main():
    x = list(map(int, input().split()))
    n = min(x[0], x[1])
    m = max(x[0], x[1])
    ans = 0

    for i in range(n + 1):
        for j in range(n + 1):
            c = i * i + j
            d = j * j + i
            if c == n and d == m:
                ans += 1
        if i * i > n:
            break

    print(ans)
    
if __name__ == '__main__':
    main()