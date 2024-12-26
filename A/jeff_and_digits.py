def main():
    n = int(input())
    lst = list(map(int, input().split()))
    five, zero = 0, 0

    for i in range(n):
        if lst[i] == 5:
            five += 1
        else:
            zero += 1
    
    if zero == 0:
        print(-1)
    else:
        k = five // 9
        k = k * 9
        ans = '5' * k + '0' * zero
        if k == 0:
            ans = '0'
        print(ans)

if __name__ == '__main__':
    main()
