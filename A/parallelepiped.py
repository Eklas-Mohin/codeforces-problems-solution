import math

def main():
    areas = list(map(int, input().split()))
    a, b, c = areas[0], areas[1], areas[2]

    h = math.sqrt((a * b) / c) * 4
    w = math.sqrt((a * c) / b) * 4
    l = math.sqrt((c * b) / a) * 4
    
    print(int(h + w + l))

if __name__ == '__main__':
    main()