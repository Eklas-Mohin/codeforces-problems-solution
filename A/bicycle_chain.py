def main():
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))
    lst = []

    for i in range(n):
        for j in range(m):
            if b[j] % a[i] == 0:
                lst.append(b[j] // a[i])

    lst.sort(reverse = True)
    print(lst.count(lst[0]))

if __name__== '__main__':
    main()