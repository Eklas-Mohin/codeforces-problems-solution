def main():
    n = int(input())
    lst = list(map(int, input().split()))

    mx, mn = max(lst), min(lst)
    mxc, mnc = lst.count(mx), lst.count(mn)
    diff = mx - mn
    way = mxc * mnc

    if mx == mn:
        way = (mxc * (mnc - 1)) // 2

    print(diff, way)
    
if __name__ == '__main__':
    main()