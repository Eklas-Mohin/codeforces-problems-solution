def main():
    n, m = map(int, input().split())
    arr = []
    ans = []
    
    for i in range(m):
        a, b = map(str, input().split())
        if len(a) <= len(b):
            arr.append((a, a))
        else:
            arr.append((a, b))
            
    lst = list(map(str, input().split()))
    
    for i in range(n):
        for j in range(m):
            if lst[i] == arr[j][0]:
                ans.append(arr[j][1])
                break
            
    print(*ans)

if __name__ == '__main__':
    main()
    