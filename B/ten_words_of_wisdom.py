def main():
    t = int(input())

    for _ in range(t):
        n = int(input())
        mx, ans = 0, 0
        for i in range(1, n + 1):
            a, b = map(int, input().split())
            if b > mx and a <= 10:
                ans = i
                mx = b

        print(ans)
        
if __name__== '__main__':
    main()