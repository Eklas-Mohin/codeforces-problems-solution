def main():
    t = int(input())
    
    for _ in range(t):
        a, b = map(int, input().split())
        k = ((a + b - 1) // b) * b
        print(k - a)
    
if __name__ == '__main__':
    main()