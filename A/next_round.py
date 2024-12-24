def remove_zero(m):
    return m != 0

def main():
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    b = list(filter(remove_zero, b))
    
    ans = min(len(b), a[1])

    for i in range(a[1], len(b), 1):
        if b[i - 1] == b[i]:
            ans += 1
        else:
            break

    print(ans)

if __name__ == '__main__':
    main()
