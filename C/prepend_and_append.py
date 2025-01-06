def main():
    t = int(input())

    for i in range(t):
        n = int(input())
        string = input()
        l, r, k = 0, n - 1, 0
        while r > l and string[r] != string[l]:
            if string[l] != string[r]:
                k += 2
                l += 1
                r -= 1
        print(n - k)

if __name__== '__main__':
    main()