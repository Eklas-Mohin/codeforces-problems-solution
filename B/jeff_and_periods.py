def main():
    n = int(input())
    x = list(map(int, input().split()))
    s = set(x)
    k = max(x)
    m = [[0 for _ in range(1)] for _ in range(k + 1)]
    ans = []

    for i in range(n):
        k = x[i]
        m[k].append(i)

    for num in s:
        l = len(m[num])
        k = m[num]
        st = set()
        j = 0
        for i in range(2, l):
            j = k[i] - k[i - 1]
            st.add(j)
        if len(st) == 0:
            ans.append((num, 0))
        elif len(st) == 1:
            ans.append((num, j))

    ans.sort(key = lambda a: a[0])
    print(len(ans))
    for i in range(len(ans)):
        print(*ans[i])

if __name__ == '__main__':
    main()
