def main():
    t = int(input())

    for _ in range(t):
        a, b = map(int, input().split())
        if a * 2 < b:
            print(a, a + a) 
        else:
            print(-1, -1)
        
if __name__ == '__main__':
    main()
