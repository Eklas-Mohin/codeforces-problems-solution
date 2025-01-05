def main():
    t = int(input())

    for i in range(t):
        n, k = map(int, input().split())
        lst1 = list(map(int, input().split()))
        lst2 = list(map(int, input().split()))
        lst1.sort()
        lst2.sort(reverse = True)
        cnt = 0
        for j in range(n):
            if lst1[j] < lst2[cnt] and cnt < k:
                lst1[j] = lst2[cnt]
                cnt += 1
        print(sum(lst1))

if __name__== '__main__':
    main()