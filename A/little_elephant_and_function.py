def main():
    n = int(input())
    arr = [n]

    for i in range(1, n):
        arr.append(i)
    
    print(*arr)

if __name__ == '__main__':
    main()
