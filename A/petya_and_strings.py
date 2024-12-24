def main():
    a = input().lower()
    b = input().lower()
    
    if a == b:
        print(0)
    elif a > b:
        print(1)
    else:
        print(-1)

if __name__ == '__main__':
    main()