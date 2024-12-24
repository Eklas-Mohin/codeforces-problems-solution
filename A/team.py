def main():
    n = int(input())
    ans = 0

    for _ in range(n):
        s = input().split(' ')
        x = [int(val) for val in s]
        k = sum(x)
        if k >= 2:
            ans += 1

    print(ans)

if __name__ == "__main__":
    main()
