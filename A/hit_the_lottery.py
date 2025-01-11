def main():
    n = int(input())
    arr = [100, 20, 10, 5, 1]
    ans = 0

    for num in arr:
        ans = ans + n // num
        n = n % num

    print(ans)

if __name__ == '__main__':
    main()