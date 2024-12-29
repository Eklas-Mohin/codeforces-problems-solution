def main():
    sn = list(map(int, input().split()))
    s, n = sn[0], sn[1]
    lp = []
    ans = 'YES'

    for _ in range(n):
        lst = list(map(int, input().split()))
        x, y = lst[0], lst[1]
        lp.append((x, y))
    lp.sort(key = lambda a: a[0])

    for i in lp:
        if s > i[0]:
            s = s + i[1]
        else:
            ans = 'NO'
            break

    print(ans)

if __name__ == '__main__':
    main()
