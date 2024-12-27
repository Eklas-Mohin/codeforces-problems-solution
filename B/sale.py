def main():
    x = list(map(int, input().split()))
    lst = list(map(int, input().split()))
    lst.sort()
    ans = 0

    i = 0
    while i < x[0] and i < x[1] and lst[i] < 0:
        ans = ans + lst[i]
        i = i + 1

    print(abs(ans))

if __name__ == '__main__':
    main()
