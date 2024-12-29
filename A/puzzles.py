def main():
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    y.sort()
    ans = 10e9

    for i in range(x[1] - x[0] + 1):
        k = y[i + x[0] - 1] - y[i]
        ans = min(ans, k)
    
    print(ans)
            
if __name__ == '__main__':
    main()