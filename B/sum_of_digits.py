def main():
    string = input()
    s = 0

    if len(string) == 1:
        print(0)
        return

    cnt = 1
    for char in string:
        x = ord(char)
        s = s + x - 48

    while s > 9:
        temp = s
        s = 0
        cnt += 1
        while temp != 0:
            s = s + temp % 10
            temp //= 10

    print(cnt)

if __name__== '__main__':
    main()