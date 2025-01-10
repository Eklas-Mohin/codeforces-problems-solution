def main():
    k, n, w = map(int, input().split())
    x = int(k * ((w * (w + 1)) // 2))
    print(max(0, x - n))
    
if __name__ == '__main__':
    main()