def main():
    n = int(input())
    
    while True:
        n += 1
        k = n
        s = set()
        while k > 0:
            s.add(k % 10)
            k //= 10
        if len(s) == 4:
            print(n)
            break

if __name__== '__main()__':
    main()