def main():
    t = int(input())

    for _ in range(t):
        x = int(input())
        if x % 33 == 0:
            print('YES')
        else:
            print('NO')

if __name__ == '__main__':
    main()
