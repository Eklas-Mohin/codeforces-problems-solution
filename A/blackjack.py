def main():
    n = int(input())
    n = n - 10

    if n == 10:
        print(15)
    elif n <= 11 and n > 0:
        print(4)
    else:
        print(0)
    
if __name__ == '__main__':
    main()