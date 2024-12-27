def main():
    n = int(input())
    lst, cnt, ans = [], 0, ''

    for _ in range(n):
        string = input()
        lst.append(string)
        k = lst.count(string)
        if k > cnt:
            ans = string
            cnt = k

    print(ans)
    
if __name__ == '__main__':
    main()