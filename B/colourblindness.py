def main():
    t = int(input())
    
    for i in range(t):
        n = int(input())
        s = input()
        t = input()
        flag = True
        for j in range(n):
            if s[j] != t[j] and (s[j] == 'R' or t[j] == 'R'):
                flag = False
        if flag:
            print('YES')
        else:
            print('NO')
        
if __name__ == '__main__':
   main()