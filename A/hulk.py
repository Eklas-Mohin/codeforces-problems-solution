def main():
    n = int(input())
    arr = []

    for i in range(1, n):
        if i % 2:
            arr.append('I hate that')
        else:
            arr.append('I love that')
    
    if n % 2:
        arr.append('I hate it')
    else:
        arr.append('I love it')

    print(*arr)

if __name__ == '__main__':
    main()