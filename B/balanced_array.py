def main():
    t = int(input())

    for i in range(t):
        n = int(input())
        k = n // 2
        if k % 2 != 0:
            print('NO')
            continue
        arr = []
        for j in range(1, k + 1):
            arr.append(2 * j)
        s = sum(arr)
        m = 0
        for j in range(1, k):
            arr.append(2 * j - 1)
            m += 2 * j - 1
        arr.append(s - m)
        print('YES')
        print(*arr)

if __name__ == '__main__':
    main()
