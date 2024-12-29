def main():
    string = input()
    hello = 'hello'
    temp = ''
    curr = 0

    for c in hello:
        for j in range(curr, len(string)):
            if c == string[j]:
                curr += 1
                temp = temp + c
                break
            curr += 1   

    if temp == hello:
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    main()