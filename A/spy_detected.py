def main():
    t = int(input())

    for _ in range(t):
        n = int(input())
        lst = list(map(int, input().split()))
        s = set(lst)
        for num in s:
            if lst.count(num) == 1:
                print(lst.index(num) + 1)
                break

if __name__ == '__main__':
    main()