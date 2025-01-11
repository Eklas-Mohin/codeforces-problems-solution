def main():
    n = int(input())
    lst = list(map(int, input().split()))
    lst.sort(reverse=True)
    s = sum(lst)
    x, i = 0, 0

    while s >= x:
        s = s - lst[i]
        x = x + lst[i]
        i += 1

    print(i)

if __name__ == '__main__':
    main()
