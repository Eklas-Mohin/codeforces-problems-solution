def main():
    n = int(input())
    k = list(map(int, input().split()))
    s = sum(k)
    ans = 5

    for i in range(s + 1, s + 6):
        if (i - 1) % (n + 1) == 0:
            ans -= 1

    print(ans)
    
if __name__ == '__main__':
    main()