def main():
    t = int(input())

    for i in range(t):
        n = int(input())
        lst = list(map(int, input().split()))
        lst.sort()
        lst[0] += 1
        ans = 1
        for j in range(n):
            ans = ans * lst[j]
        print(ans)

if __name__ == '__main__':
    main()