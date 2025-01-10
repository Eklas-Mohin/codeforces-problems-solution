def main():
    n = int(input())
    string = input()
    st = set()

    for character in string:
        st.add(character.lower())

    if len(st) == 26:
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    main()