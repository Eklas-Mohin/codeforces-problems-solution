def main():
    row = col = 0

    for i in range(0, 5):
        mat = list(map(int, input().split()))
        for j in range(0, 5):
            if mat[j] == 1:
                row = i + 1
                col = j + 1

    print(abs(row - 3) + abs(col - 3))

if __name__ == '__main__':
    main()
