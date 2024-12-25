def main():
    n = int(input())
    points = []
    ans = 0

    for _ in range(n):
        k = list(map(int, input().split()))
        points.extend(k)
    
    for i in range(n):
        x = points[2 * i]
        y = points[2 * i + 1]
        a = b = c = d = 0
        for j in range(n):
            xx = points[2 * j]
            yy = points[2 * j + 1]
            if x == xx and yy > y:
                a = 1
            if x == xx and yy < y:
                b = 1
            if y == yy and x > xx:
                c = 1
            if y == yy and x < xx:
                d = 1
        if a + b + c + d == 4:
            ans += 1

    print(ans)

if __name__ == '__main__':
    main()