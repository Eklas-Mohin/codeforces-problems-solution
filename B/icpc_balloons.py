def main():
    t = int(input())
    
    for i in range(t):
        n = int(input())
        string = input()
        ans = 0
        arr = [False] * 26
        for c in string:
            a = ord(c) -  65
            if arr[a] == False:
                ans += 2
                arr[a] = True
            else:
                ans += 1
        print(ans)

if __name__ == '__main__':
    main()