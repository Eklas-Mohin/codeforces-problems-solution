def main():
    string = input()
    ll = len(string)
    ans = 'NO'
    cnt = 1

    for i in range(1, ll):
        if string[i] == string[i - 1]:
            cnt += 1
            if cnt == 7:
                ans = 'YES'
                break
        else:
            cnt = 1

    print(ans)
    
if __name__ == '__main__':
    main()