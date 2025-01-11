def main():
    n = int(input())
    lst = list(map(int, input().split()))

    lst.sort()
    print(*lst)

if __name__ == '__main__':
    main()
