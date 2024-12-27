def main():
    string = input()
    l, i , ans = len(string) - 1, 0, 'YES'

    while i <= l:
        if string[i] == '1':
            if i < l and string[i + 1] == '4':
                i = i + 1
                if i < l and string[i + 1] == '4':
                    i = i + 1
        else:
            ans = 'NO'
        i = i + 1
        
    print(ans)

if __name__ == '__main__':
    main()
