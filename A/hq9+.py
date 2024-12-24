def main():
    st = input()
    hq = 'HQ9'

    for c in st:
        if c in hq:
            print('YES')
            return
        
    print('NO')

if __name__ == '__main__':
    main()