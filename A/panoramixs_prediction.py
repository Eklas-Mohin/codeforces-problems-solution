import math

def is_prime(n):
    k = int(math.sqrt(n))

    if n > 2 and n % 2 == 0:
        return False
    for i in range(3, k + 1, 2):
        if n % i == 0:
            return False
        
    return True

def main():
    x = list(map(int, input().split()))
    flag = False

    while flag == False:
        x[0] += 1
        flag = is_prime(x[0])
        
    if x[0] == x[1]:
        print('YES')
    else:
        print('NO')
    
if __name__ == '__main__':
    main()