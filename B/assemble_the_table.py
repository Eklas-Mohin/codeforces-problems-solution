def main():
    n = int(input())
    lst = list(map(int, input().split()))
    lst.sort()
    k = 2 * n - 1

    for i in range(n):
        print(lst[i], lst[k])
        k = k - 1
    
if __name__ == '__main__':
    main()
