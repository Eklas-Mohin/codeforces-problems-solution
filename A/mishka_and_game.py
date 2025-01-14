def main():
    n = int(input())
    mishka = chris = 0

    for _ in range(n):
        a, b = map(int, input().split())
        if a > b:
            mishka += 1
        elif b > a:
            chris += 1

    if mishka > chris:
        print('Mishka')
    elif mishka < chris:
        print('Chris')
    else:
        print('Friendship is magic!^^')

if __name__ == '__main__':
    main()