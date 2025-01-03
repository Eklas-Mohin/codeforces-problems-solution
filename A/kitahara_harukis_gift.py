def main():
    n = int(input())
    lst = list(map(int, input().split()))
    a, b = lst.count(100), lst.count(200)

    if a % 2 == 0 and b % 2 == 0:
        print('YES')
    elif a > 0 and a % 2 == 0:
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    main()