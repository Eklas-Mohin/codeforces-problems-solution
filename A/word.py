def main():
    word = input()
    l = u = 0

    for x in word:
        if x >= 'a' and x <= 'z':
            l += 1
        else:
            u += 1
            
    if l >= u:
        print(word.lower())
    else:
        print(word.upper())

if __name__ == '__main__':
    main()