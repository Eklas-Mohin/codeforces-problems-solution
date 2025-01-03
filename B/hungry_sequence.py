def main():
    k = 100007
    n = int(input())
    arr = []

    for i in range(n):
        arr.append(i + k)
    
    print(*arr)

if __name__ == '__main__':
    main()