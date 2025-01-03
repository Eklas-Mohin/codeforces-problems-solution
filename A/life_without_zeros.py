def main():
    a = input()
    b = input()
    c = str(int(a) + int(b))

    a, b, c = int(a[::-1]), int(b[::-1]), int(c[::-1])
    x, y, z = 0, 0, 0

    while a > 0 or b > 0 or c > 0:
        if a % 10:
            x = x * 10 + a % 10
        if b % 10:
            y = y * 10 + b % 10
        if c % 10:
            z = z * 10 + c % 10
        a = a // 10
        b = b // 10
        c = c // 10

    if x + y == z:
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    main()