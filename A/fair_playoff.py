def main():
    t = int(input())

    for _ in range(t):
        lst = list(map(int, input().split()))
        a = max(lst[0], lst[1])
        b = max(lst[2], lst[3])
        a, b = max(a, b), min(a, b)
        lst.sort(reverse=True)
        if a == lst[0] and b == lst[1]:
            print('YES')
        else:
            print('NO')

if __name__== '__main__':
    main()