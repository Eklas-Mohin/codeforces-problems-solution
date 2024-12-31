def main():
    s = input()
    st = set()
    k = []
    cnt = 0

    for c in s:
        st.add(c)
    for c in st:
        k.append(s.count(c))
    
    for num in k:
        if num % 2 == 1:
            cnt += 1

    if cnt > 0:
        cnt -= 1

    if cnt % 2 == 0:
        print('First')
    else:
        print('Second')

if __name__ == '__main__':
    main()
