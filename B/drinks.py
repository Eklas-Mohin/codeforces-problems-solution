def main():
    total = 0
    n = int(input())
    k = list(map(int, input().split()))
    total = sum(k)
    print(total / n)

if __name__ == '__main__':
    main()
