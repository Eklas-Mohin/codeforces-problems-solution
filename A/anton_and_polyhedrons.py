def main():
    dict = {
        'Tetrahedron': 4,
        'Cube': 6,
        'Octahedron': 8,
        'Dodecahedron': 12,
        'Icosahedron': 20
    }
    n = int(input())
    ans = 0

    for _ in range(n):
        key = input()
        ans = ans + dict[key]
    
    print(ans)

if __name__ == '__main__':
    main()