def main():
    n = int(input())
    k = n * n
    arr = []
    brr = []

    for i in range(1, k + 1):
        arr.append(i)
    brr = arr.copy()
    brr = brr[::-1]

    if n % 2 == 0:
        k = 0
        for i in range(n):
            print(*arr[k:k+n//2], *brr[k:k+n//2])
            k = k + n // 2
    else:
        pass

if __name__ == '__main__':
    main()