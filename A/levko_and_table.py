def main():
    r, n = map(int, input().split())
    matrix = [[0 for i in range(r)] for i in range (r)]

    for i in range(r):
        matrix[i][i] = n
        print(*matrix[i])

if __name__ == '__main__':
    main()
