def main():
    a, b = map(int, input().split())
    y = 6
    x = 6 - max(a, b) + 1

    while x % 2 == 0 and y % 2 == 0:
        x //= 2
        y //= 2
    if y % x == 0:
        y = y // x
        x = 1

    print(str(x) + '/' + str(y))

if __name__ == '__main__':
    main()