def main():
    matrix = [[0] * 5 for _ in range(5)]
    final_state = [[1] * 5 for _ in range(5)]

    for i in range(1, 4):
        row = list(map(int, input().split()))
        for j in range(1, 4):
            matrix[i][j] = row[j - 1] % 2

    for i in range(1, 4):
        for j in range(1, 4):
            if matrix[i][j] == 1:
                final_state[i][j] ^= 1
                final_state[i][j + 1] ^= 1
                final_state[i][j - 1] ^= 1
                final_state[i + 1][j] ^= 1
                final_state[i - 1][j] ^= 1

    for i in range(1, 4):
        print(''.join(map(str, final_state[i][1:4])))

if __name__ == '__main__':
    main()
