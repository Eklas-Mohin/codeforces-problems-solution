def main():
    string = input()
    s = set()

    for character in string:
        if character >= 'a' and character <= 'z':
            s.add(character)
    
    print(len(s))

if __name__ == '__main__':
    main()