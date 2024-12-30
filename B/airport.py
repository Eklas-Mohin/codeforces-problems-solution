def main():
    inp = list(map(int, input().split()))
    lst = list(map(int, input().split()))
    tmp = lst.copy()
    mn, mx = 0, 0

    for i in range(inp[0]):
        k = lst[0]
        p = 0
        for j in range(inp[1]):
            if lst[j] > k:
                k = lst[j]
                p = j
        mx = mx + k
        lst[p] = lst[p] - 1

    for i in range(inp[0]):
        k = max(tmp)
        p = 0
        for j in range(inp[1]):
            if tmp[j] <= k and tmp[j] > 0:
                k = tmp[j]
                p = j
        mn = mn + k
        tmp[p] = tmp[p] - 1

    print(mx, mn)

if __name__ == '__main__':
    main()
