def main():
    num = input()
    cnt = flag = 0
    k = False

    for n in num:
        if n == '4' or n == '7':
            cnt += 1
            k = True

    while cnt > 0:
        if cnt % 10 == 4 or cnt % 10 == 7:
            pass
        else:
            flag = 1
            break
        cnt //= 10
        
    if flag == 0 and k == True:
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    main()