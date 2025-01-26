def main():
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    q = list(map(int, input().split()))
    x = [1]
    y = [a[0]]

    for i in range(1, n):
        x.append(y[i - 1] + 1)
        y.append(x[i] + a[i] - 1)

    for num in q:
        l = 0
        r = n - 1
        while r >= l:
            mid = (l + r) // 2
            if x[mid] <= num and num <= y[mid]:
                print(mid + 1)
                break
            elif x[mid] < num:
                l = mid + 1
            else:
                r = mid - 1

if __name__ == '__main__':
    main()