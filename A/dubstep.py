def main():
    string = input()
    lyrics = string.replace('WUB', ' ')
    print(' '.join(lyrics.split()))
        
if __name__ == '__main__':
    main()
