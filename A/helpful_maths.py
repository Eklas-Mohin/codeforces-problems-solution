def main():
    x = list(map(str, input().split('+')))
    x.sort()
    print('+'.join(x))

if __name__ == '__main__':
    main()