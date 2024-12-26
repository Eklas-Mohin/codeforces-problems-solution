def main():
    n = int(input())
    lst = list(map(int, input().split()))
    mn = min(lst)
    k = lst.count(mn)
    idx = lst.index(mn)

    if k > 1:
        print('Still Rozdil')
    else:
        print(idx + 1)

if __name__ == '__main__':
    main()
