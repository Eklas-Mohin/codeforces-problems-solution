def main():
    n, m = map(int, input().split())
    arr = [['.' for _ in range(m)] for _ in range(n)]
    tmp = [['.' for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if (i + j) % 2 == 0:
                arr[i][j] = 'W'
            else:
                arr[i][j] = 'B'

    for i in range(n):
        t = input()
        for j in range(m):
            tmp[i][j] = t[j]

    for i in range(n):
        for j in range(m):
            if tmp[i][j] == '-':
                arr[i][j] = '-'

    for row in arr:
        print(''.join(row))

if __name__ == '__main__':
    main()
