def main():
    n = input()
    arr = list(map(int, input().split()))
    s = sum(arr)
    ans = 0

    for num in arr:
        k = s - num
        if k % 2 == 0:
            ans += 1

    print(ans)

if __name__ == '__main__':
    main()