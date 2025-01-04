import math 

def main():
    up = 1e13
    up = int(math.sqrt(up + 1))
    br = [True] * (up + 1)
    br[0] = br[1] = False
    x = math.sqrt(up + 1)
    x = int(x)

    for i in range(4, up, 2):
        br[i] = False
    
    for i in range(3, x + 1, 2):
        if br[i]:
            for j in range(2 * i, up, i):
                br[j] = False

    n = int(input())
    lst = list(map(int, input().split()))
    for num in lst:
        sq = int(math.sqrt(num))
        if sq * sq == num and br[sq]:
            print('YES')
        else:
            print('NO')

if __name__== '__main__':
    main()