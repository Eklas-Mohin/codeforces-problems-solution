def main():
    t = int(input())

    for i in range(t):
        n = int(input())
        s = set(map(int, input().split()))
        if len(s) == n:
            print('YES')
        else:
            print('NO')
    
if __name__ == '__main__':
    main()
