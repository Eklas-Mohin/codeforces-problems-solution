def main():
    x = list(map(int, input().split()))
    queue = list(input())
    n, t = x[0], x[1]

    for _ in range(t):
        i = 1
        while i < n:
            if queue[i] == 'G' and queue[i - 1] == 'B':
                queue[i - 1], queue[i] = queue[i], queue[i - 1]
                i += 1
            i += 1

    print(''.join(queue))

if __name__ == '__main__':
    main()
