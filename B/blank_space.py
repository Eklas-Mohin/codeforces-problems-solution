def main():
    t = int(input())

    for i in range(t):
        n = int(input())
        lst = list(map(int, input().split()))
        mx, j = 0, 0
        while j < n:
            if lst[j] == 0:
                cnt = 0
                while j < n and lst[j] == 0:
                    cnt += 1
                    j += 1
                if mx < cnt:
                    mx = cnt
            j += 1
        print(mx)
                    
if __name__ == '__main__':
    main()