def main():
    k = int(input())
    l = int(input())
    m = int(input())
    n = int(input())
    d = int(input())
    lst = [False] * d
    ans = 0

    for i in range(k, d + 1, k):
        lst[i - 1] = True
    for i in range(l, d + 1, l):
        lst[i - 1] = True
    for i in range(m, d + 1, m):
        lst[i - 1] = True
    for i in range(n, d + 1, n):
        lst[i - 1] = True
    for i in range(d):
        ans = ans + lst[i]
        
    print(ans)
    
if __name__ == '__main__':
    main()