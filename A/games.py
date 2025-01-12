def main():
    n = int(input())
    s = []
    lst = []
    ans = 0

    for _ in range(n):
        a, b = map(int, input().split())
        s.append(a)
        lst.append(b)

    for num in s:
        ans = ans + lst.count(num)

    print(ans)

if __name__ == '__main__':
    main()
