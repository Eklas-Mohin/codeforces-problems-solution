def main():
    x = list(map(int, input().split()))
    n, k, l, c, d, p, nl, np = x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7]

    l = l * k
    c = c * d
    l = l // nl
    p = p // np
    
    x = min(l, min(p, c))
    print(x // n)
    
if __name__ == '__main__':
    main()