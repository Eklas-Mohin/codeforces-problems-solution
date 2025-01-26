def main():
    t = int(input())
    for i in range(t):
        s = input()
        if len(s) > 2 and s[0] == '1' and s[1] == '0' and s[2] != '0':
            st = s[2:]
            k = int(st)
            if k >= 2:
                print('YES')
            else:
                print('NO')
        else:
            print('NO')

if __name__ == '__main__':
    main()