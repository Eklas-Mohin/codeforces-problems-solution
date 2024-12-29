def main():
    input_string = input()
    input_string = input_string.lower()
    vowels = 'aeiouy'
    output_string = ''

    for character in input_string:
        if character not in vowels:
            output_string += '.' + character

    print(output_string)

if __name__ == '__main__':
    main()