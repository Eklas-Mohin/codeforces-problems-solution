def main():
    s = input()
    t = input()
    t = t[::-1]

    if t == s:
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    main()
