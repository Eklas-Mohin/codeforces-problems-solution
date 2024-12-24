def main():
    t = int(input())

    for _ in range(t):
        str = input()
        if len(str) <= 10:
            print(str)
        else:
            print(str[0] + f'{len(str) - 2}' + str[len(str) - 1])

if __name__ == '__main__':
    main()
