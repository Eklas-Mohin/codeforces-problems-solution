def main():
    t = int(input())

    for i in range(t):
        n = int(input())
        n = 180 - n
        if 360 % n == 0:
            print('YES')
        else:
            print('NO')

if __name__== '__main__':
    main()