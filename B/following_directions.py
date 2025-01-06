def main():
    t = int(input())

    for i in range(t):
        n = int(input())
        string = input()
        flag = False
        x, y = 0, 0
        for character in string:
            if character == 'R':
                x += 1
            elif character == 'L':
                x -= 1
            elif character == 'U':
                y += 1
            else:
                y -= 1
            if x == 1 and y == 1:
                flag = True
                break
        if flag:
            print('YES')
        else:
            print('NO')
                    
if __name__ == '__main__':
    main()