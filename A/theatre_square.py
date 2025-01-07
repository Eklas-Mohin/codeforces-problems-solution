def main():
    n, m, a = map(int, input().split())
    x = (n + a - 1) // a
    y = (m + a - 1) // a
    print(x * y)
        
if __name__ == '__main__':
   main()