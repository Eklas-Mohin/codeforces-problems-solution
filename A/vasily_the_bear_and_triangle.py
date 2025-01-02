def main():
    x, y = map(int, input().split())

    if x > 0 and y > 0:
        print(0, x + y, x + y, 0)
    elif x < 0 and y > 0:
        print(x - y, 0, 0, y - x)
    elif x < 0 and y < 0:
        print(x + y, 0, 0, x + y)
    else:
        print(0, y - x, x - y, 0)
        
if __name__ == '__main__':
    main()