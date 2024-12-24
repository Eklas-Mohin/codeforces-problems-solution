def main():
    t =int(input())

    for _ in range(t):
        lst = list(map(int, input().split()))
        s = sum(lst) - lst[0]
        ans = 0
        
        if s >= lst[0]:
            k = 1
            while lst[0] > 0:
                lst[0] -= lst[k]
                k += 1
                ans += 1
        else:
            ans = (lst[0] // s) * 3
            lst[0] = lst[0] % s
            k = 1
            while lst[0] > 0:
                lst[0] -= lst[k]
                k += 1
                ans += 1

        print(ans)

if __name__ == '__main__':
    main()