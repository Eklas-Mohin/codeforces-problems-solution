def main():
    n = list(map(int, input().split()))
    lst = list(map(int, input().split()))
    ans = 0

    for i in range(n[0]):
        lst[i] = (lst[i] +  n[1] - 1) // n[1]
    
    for i in range(1, n[0]):
        if lst[i] >= lst[ans]:
            ans = i
    
    print(ans + 1)

if __name__ == '__main__':
    main()