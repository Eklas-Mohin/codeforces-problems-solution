def main():
    n = int(input())
    arr = list(map(int, input().split()))
    
    if 1 in arr:
        print('HARD')
    else:
        print('EASY')

if __name__ == '__main__':
    main()