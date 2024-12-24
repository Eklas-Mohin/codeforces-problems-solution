def main():
    n = int(input())
    arr = []

    if n % 2 == 1:
        print(-1)
    else:
        for i in range(1, n + 1, 2):
            arr.append(i + 1)
            arr.append(i)
            
    print(*arr)
    
if __name__ == '__main__':
    main()