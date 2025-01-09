def main():
    t = int(input())

    for i in range(t):
        n, k = map(int, input().split())
        x = (k * n) // (n - 1)
        if x % n == 0:
            x = x - 1
        print(x)

if __name__== '__main__':
    main()