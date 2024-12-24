def main():
    n = int(input())
    arr = list(map(int, input().split()))
    mn = mx = arr[0]
    ans = mnp = mxp = 0

    for i in range(1, n):
        if arr[i] <= mn:
            mn = arr[i]
            mnp = i
        if arr[i] > mx:
            mx = arr[i]
            mxp = i

    ans = mxp + n - mnp - 1
    if (mxp >= mnp):
        ans = ans - 1
        
    print(ans)

if __name__ == '__main__':
    main()