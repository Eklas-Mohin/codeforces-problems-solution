def main():
    s = input()
    t = input()
    k = []
    m = []
    p = 0

    if len(s) != len(t):
        print('NO')
        return

    for i in range(len(s)):
        if s[i] != t[i]:
            k.append(s[i])
            m.append(t[i])
            p += 1

    if p == 2 and k[0] == m[1] and k[1] == m[0]:
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    main()
