def main():
    t = int(input())
    
    for i in range(t):
        n = int(input())
        lst = list(map(int, input().split()))
        s = sum(lst)
        lst.sort()
        k = lst[0] * n
        print(s - k)
        
if __name__ == '__main__':
   main()