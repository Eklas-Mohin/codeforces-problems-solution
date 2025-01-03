def main():
    s = input()
    t = input()
    ans = 'YES'

    for c in t:
        k = s.count(c)
        l = t.count(c)
        if k < l and c != ' ':
            ans = 'NO'
            break

    print(ans)

if __name__ == '__main__':
    main()
