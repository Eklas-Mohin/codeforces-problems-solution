def main():
    t = int(input())
    
    for i in range(t):
        n = int(input())
        lst = list(map(int, input().split()))
        s = sum(lst)
        if s % 2:
            print('NO')
            continue
        
        odd = lst.count(1)
        even = lst.count(2)
        if odd % 2 == 0 and even % 2 == 0:
            print('YES')
        elif odd > 0 and odd % 2 == 0:
            print('YES')
        else:
            print('NO')
                
if __name__ == '__main__':
    main()