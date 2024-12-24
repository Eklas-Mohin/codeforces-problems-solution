def main():
    n = int(input())
    mx = cnt = 0

    for _ in range(n):
        x = list(map(int, input().split()))
        cnt = cnt - x[0] + x[1]
        mx = max(mx, cnt)
        
    print(mx)

if __name__ == '__main__':
    main()