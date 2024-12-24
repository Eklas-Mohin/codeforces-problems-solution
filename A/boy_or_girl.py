def main():
    s = input()
    st = set()

    for c in s:
        st.add(c)
        
    if len(st) % 2 == 0:
        print('CHAT WITH HER!')
    else:
        print('IGNORE HIM!')

if __name__ == '__main__':
    main()