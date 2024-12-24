def main():
    n = int(input())
    lst = list(map(int, input().split()))
    ans = 0
    mn = mx = lst[0]

    for i in range(n):
        if lst[i] < mn:
            ans += 1
            mn = lst[i]
        elif lst[i] > mx:
            ans += 1
            mx = lst[i]
            
    print(ans)

if __name__ == '__main__':
    main()