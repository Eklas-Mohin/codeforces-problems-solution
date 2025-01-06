def main():
    t = int(input())

    for i in range(t):
        n = int(input())
        string = input()
        k = 0
        for character in string:
            k = max(k, ord(character) - 96)
        print(k)
                    
if __name__ == '__main__':
    main()