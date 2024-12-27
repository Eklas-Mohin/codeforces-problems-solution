def main():
    nm = list(map(int, input().split()))
    lst = list(map(int, input().split()))
    ans, pre = 0, 1

    for i in range(nm[1]):
        if pre > lst[i]:
            ans = ans + nm[0] - pre + 1
            pre = 1
        ans = ans + lst[i] - pre
        pre = lst[i]
            
    print(ans)

if __name__ == '__main__':
    main()