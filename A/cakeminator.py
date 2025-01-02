def main():
    r, c = map(int, input().split())
    matrix = [['.' for i in range(c)] for i in range (r)]
    ans = 0

    for i in range(r):
        s = input()
        k = 0
        for ch in s:
            matrix[i][k] = ch
            k += 1
        if matrix[i].count('.') == c:
            ans += c
            for j in range(c):
                matrix[i][j] = '+'

    for i in range(c):
        a = 0
        b = 0
        for j in range(r):
            if matrix[j][i] == '+':
                a += 1
            elif  matrix[j][i] == '.':
                b += 1
        if a + b == r:
            ans += b

    print(ans)

if __name__ == '__main__':
    main()
