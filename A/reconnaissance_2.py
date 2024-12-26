def main():
    n = int(input())
    lst = list(map(int, input().split()))
    x, y, diff = 0, 0, 10000000000

    for i in range(1, n):
        k = abs(lst[i] - lst[i - 1])
        if k < diff:
            diff = k
            x = i 
            y = i + 1
    
    k = abs(lst[0] - lst[n - 1])
    if k < diff:
        x = 1
        y = n

    print(x, y)
    
if __name__ == '__main__':
    main()