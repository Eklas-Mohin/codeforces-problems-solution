def main():
    t = int(input())

    for _ in range(t):
        n = int(input())
        one = two = n // 3
        k = n - one - (two + two)
        if k == 1:
            one += 1
        elif k == 2:
            two += 1
        print(one, two)
            
if __name__ == '__main__':
    main()