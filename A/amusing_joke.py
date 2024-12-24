def main():
    a = input().strip()
    b = input().strip()
    c = input().strip()
    a = a + b
    
    if sorted(a) == sorted(c):
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    main()