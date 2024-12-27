def main():
    n = int(input())
    lst = list(map(int, input().split()))
    lst.sort(reverse = True)

    i = 0
    while n > 0 and i < 12:
        n = n - lst[i]
        i += 1

    if n > 0:
        print(-1)
    else:
        print(i)

if __name__ == '__main__':
    main()