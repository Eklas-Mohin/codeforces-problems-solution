def main():
    n = int(input())
    fibs = [0, 1]
    x, k, cnt = 1, 0, 0
    ans = []

    while k <= 1e9:
        k = fibs[x] + fibs[x - 1]
        fibs.append(k)
        x += 1 
    fibs.reverse()

    for i in range(x):
        if n >= fibs[i]:
            ans.append(fibs[i])
            n = n - fibs[i]
            cnt += 1
            if cnt == 3:
                break

    while cnt < 3:
        ans.append(0)
        cnt += 1
        
    print(*ans)

if __name__ == '__main__':
    main()