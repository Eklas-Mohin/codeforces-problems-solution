def main():
    n = int(input())
    ans = 0

    for _ in range(n):
        s = input()
        if '+' in s:
            ans += 1
        else:
            ans -= 1
            
    print(ans)
    
if __name__ == '__main__':
    main()