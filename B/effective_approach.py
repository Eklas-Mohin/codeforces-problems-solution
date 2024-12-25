def main():
    n = int(input())
    lst = list(map(int, input().split()))
    q = int(input())
    queries = list(map(int, input().split()))
    vasya = petya = 0
    pos = [0] * (n + 1)

    for i in range(n):
        pos[lst[i]] = i + 1

    for i in range(q):
        vasya = vasya + pos[queries[i]]
        petya = petya - pos[queries[i]] + n + 1

    print(vasya, petya)

    
if __name__ == '__main__':
    main()