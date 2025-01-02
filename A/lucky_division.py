import math

def main():
    n = int(input())
    k = int(math.sqrt(n + 1))
    divs = []

    for i in range(1, k + 1):
        if n % i == 0:
            a = str(i)
            b = str(n // i)
            x = a.count('4') + a.count('7')
            if x == len(a):
                print('YES')
                return
            x = b.count('4') + b.count('7')
            if x == len(b):
                print('YES')
                return

    print('NO')

if __name__== '__main__':
    main()