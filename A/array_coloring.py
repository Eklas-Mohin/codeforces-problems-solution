def main():
    t = int(input())

    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        s = sum(arr)
        if s % 2:
            print('NO')
        else:
            print('YES')
    
if __name__ == '__main__':
    main()