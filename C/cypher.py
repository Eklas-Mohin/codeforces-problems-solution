def main():
    t = int(input())

    for _ in range(t):
        n = int(input())
        lst = list(map(int, input().split()))
        for i in range(n):
            s = input()
            x, y = s.count('U'), s.count('D')
            x, y = x % 10, y % 10
            lst[i] = (lst[i] - x) % 10
            lst[i] = (lst[i] + y) % 10
            lst[i] = abs(lst[i])
        print(*lst)

if __name__ == '__main__':
    main()