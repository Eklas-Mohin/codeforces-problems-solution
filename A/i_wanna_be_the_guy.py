def main():
    n = int(input())
    lst1 = list(map(int, input().split()))
    lst2 = list(map(int, input().split()))
    s = set()

    s.update(lst1[1:])
    s.update(lst2[1:])

    if len(s) == n:
        print('I become the guy.')
    else:
        print('Oh, my keyboard!')
    
if __name__ == '__main__':
    main()