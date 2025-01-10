def main():
    n = int(input())
    arr = []
    ans = 1

    for _ in range(n):
        k = int(input())
        arr.append(k)

    for i in range(1, n):
        if arr[i] != arr[i - 1]:
            ans += 1

    print(ans)

if __name__ == '__main__':
    main()
