def main():
    n, x1, y1, x2, y2 = map(int, input().split())
    string = input()
    array = [c for c in string]
    ans = 0
    flag = False

    for char in array:
        if char == 'E' and x2 > x1:
            x1 += 1
        elif char == 'W' and x2 < x1:
            x1 -= 1
        elif char == 'N' and y2 > y1:
            y1 += 1
        elif char == 'S' and y2 < y1:
            y1 -= 1
        ans += 1
        if x1 == x2 and y1 == y2:
            flag = True
            break

    if flag:
        print(ans)
    else:
        print(-1)
    
if __name__ == '__main__':
    main()
