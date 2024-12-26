def main():
    lst = list(map(int, input().split()))
    k = (lst[0] + 1) // 2
    
    if lst[1] * 2 <= (lst[0] + 1):
        print(lst[1] * 2 - 1)
    else:
        print((lst[1] - k) * 2)

if __name__ == '__main__':
    main()