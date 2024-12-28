def main():
    k = int(input())
    string = input().strip()
    tmp = sorted(string)
    kstring = ''

    for i in range(0, len(tmp), k):
        kstring = kstring + tmp[i]
    x = kstring * k

    if sorted(x) == sorted(tmp):
        print(kstring * k)
    else:
        print(-1)
        
if __name__ == '__main__':
    main()
