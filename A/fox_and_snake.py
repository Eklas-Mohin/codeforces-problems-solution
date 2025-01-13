def main():
    r, c = map(int, input().split())

    for i in range(1, r + 1):
        if i % 2:
            print('#' * c)
        elif i % 4 == 0:
            print('#'+'.' * (c - 1))
        else:
            print('.' * (c - 1) + '#')

if __name__ == '__main__':
    main()