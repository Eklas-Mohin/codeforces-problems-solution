def main():
    n = int(input())

    for i in range(2 * n + 1):
        k = 2 * n - i
        if i <= n:
            k = i
        tmp = []
        for j in range(k + 1):
            tmp.append(j)
        for j in range( k - 1, -1, -1):
            tmp.append(j)

        res = ''
        for j in range(len(tmp)):
            res = res + str(tmp[j]) + ' '
        res = res.strip()
        sp = (n - k) * 2
        print(' ' * sp + res)
        
if __name__ == '__main__':
    main()