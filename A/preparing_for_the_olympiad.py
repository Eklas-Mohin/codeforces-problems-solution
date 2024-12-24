def main():
    t = int(input())

    for _ in range(t):
        n = int(input())
        m = list(map(int, input().split()))
        s = list(map(int, input().split()))
        
        ans = 0
        for i in range(n - 1):
            if m[i] > s[i + 1]:
                ans = ans + m[i] - s[i + 1]

        ans += m[n - 1]
        print(ans)
            
if __name__ == '__main__':
    main()