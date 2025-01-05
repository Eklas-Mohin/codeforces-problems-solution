def main():
    t = int(input())

    for i in range(t):
        n = int(input())
        even = (n + 1) // 2
        odd = n // 2
        cnt = 0
        lst = list(map(int, input().split()))
        for j in range(n):
            if lst[j] % 2 != j % 2:
                cnt += 1
            if lst[j] % 2 == 1:
                odd -= 1
            else:
                even -= 1
        if cnt % 2 == 0 and odd == 0 and even == 0:
            print(cnt // 2)
        else:
            print(-1)
                
if __name__ == '__main__':
    main()