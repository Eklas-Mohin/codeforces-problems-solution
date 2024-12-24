def main():
    st = list(input())

    ans = ''
    i = 0
    
    while i < (len(st)):
        if st[i] == '.':
            ans += '0'
            i += 1
        elif st[i] == '-' and st[i + 1] == '.':
            ans += '1'
            i += 2
        else:
            ans += '2'
            i += 2

    print(ans)

if __name__ == '__main__':
    main()
