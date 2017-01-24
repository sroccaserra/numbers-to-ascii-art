import sys

from ascii_art.number_to_ascii_art import number_to_ascii_art


def main():
    args = sys.argv
    numbers = [int(arg) for arg in args[1:]]
    number_representations = [number_to_ascii_art(number)
                              for number in numbers]
    for number_representation in number_representations:
        print()
        for line in number_representation:
            print(line)


if __name__ == '__main__':
    main()
