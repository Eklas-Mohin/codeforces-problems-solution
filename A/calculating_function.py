def main():
    n = int(input())
    if n % 2:
        n = -n - 1
    print(n // 2)

if __name__ == '__main__':
    main()
