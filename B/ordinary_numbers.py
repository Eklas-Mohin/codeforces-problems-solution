def main():
    t = int(input())
    
    for i in range(t):
        n = int(input())
        ans = 0
        for x in range(1, 10):
            k = x
            while k <= n:
                ans += 1
                k = k * 10 + x
        print(ans)
    
if __name__ == '__main__':
    main()