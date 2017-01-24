CONVERSION_TABLE = {
    0: [
        '###',
        '# #',
        '# #',
        '# #',
        '###'
    ],
    1: [
        '  #',
        '  #',
        '  #',
        '  #',
        '  #'
    ],
    2: [
        '###',
        '  #',
        '###',
        '#  ',
        '###'
    ],
    3: [
        '###',
        '  #',
        '###',
        '  #',
        '###'
    ],
    4: [
        '#  ',
        '# #',
        '###',
        '  #',
        '  #'
    ],
    5: [
        '###',
        '#  ',
        '###',
        '  #',
        '###'
    ],
    6: [
        '###',
        '#  ',
        '###',
        '# #',
        '###'
    ],
    7: [
        '###',
        '  #',
        ' # ',
        ' # ',
        ' # '
    ],
    8: [
        '###',
        '# #',
        '###',
        '# #',
        '###'
    ],
    9: [
        '###',
        '# #',
        '###',
        '  #',
        '###'
    ]
}


def split_large_numbers(number):
    return [int(i) for i in str(number)]


def single_number_representation(single_number):
    return CONVERSION_TABLE[single_number]


def transpose_lines(single_number_representations):
    zipped = zip(*single_number_representations)
    as_list = list(map(list, list(zipped)))
    return as_list


def join_columns(transposed_lines):
    return list(map(lambda column: "  ".join(column), transposed_lines))


def number_to_ascii_art(number):
    numbers = split_large_numbers(number)
    numbers_representations = list(map(single_number_representation, numbers))
    transposed_lines = transpose_lines(numbers_representations)
    return join_columns(transposed_lines)
