def main():
    n, k = map(int, input().split())
    ans = -1e12

    for i in range(n):
        fi, ti = map(int, input().split())
        tmp = ti - k
        if tmp > 0:
            fi = fi - tmp
        ans = max(fi, ans)

    print(ans)
        
if __name__ == '__main__':
    main()
