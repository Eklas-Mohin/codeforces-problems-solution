import math

def main():
    n, k = map(int, input().split())

    x = (n * (n + 1)) // 2
    k = int(k % x)
    x = -1 + math.sqrt(1 + 8 * k)
    x //= 2
    x = (x * (x + 1)) // 2

    print(int(k - x))

if __name__ == '__main__':
    main()