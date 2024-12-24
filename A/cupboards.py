def main():
    n = int(input())
    a = b = c = d = 0
    
    for _ in range(n):
        lst = list(map(int, input().split()))
        if lst[0] == 0:
            a += 1
        else:
            b += 1
        if lst[1] == 0:
            c += 1
        else:
            d += 1

    x = max(a, b)
    y = max(c, d)
    ans = min(x, y)
    print(ans)

if __name__ == '__main__':
    main()