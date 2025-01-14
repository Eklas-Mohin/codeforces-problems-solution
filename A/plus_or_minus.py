def main():
    t = int(input())

    for _ in range(t):
        a, b, c = map(int, input().split())
        if a + b == c:
            print('+')
        else:
            print('-')

if __name__ == '__main__':
    main()