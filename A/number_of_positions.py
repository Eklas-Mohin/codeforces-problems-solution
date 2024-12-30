def main():
    inp = list(map(int, input().split()))
    n, a, b = inp[0], inp[1], inp[2]
    x = n - a
    y = b + 1
    
    print(min(x, y))
    
if __name__ == '__main__':
    main()