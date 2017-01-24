from ascii_art.number_to_ascii_art import number_to_ascii_art,\
    split_large_numbers, transpose_lines, join_columns


class TestLargerNumbersToAscii:
    def test_the_number_ten(self):
        assert number_to_ascii_art(10) == [
            '  #  ###',
            '  #  # #',
            '  #  # #',
            '  #  # #',
            '  #  ###'
        ]

    def test_the_number_eleven(self):
        assert number_to_ascii_art(11) == [
            '  #    #',
            '  #    #',
            '  #    #',
            '  #    #',
            '  #    #'
        ]

    def test_the_number_two_hundreds_and_thirty_five(self):
        assert number_to_ascii_art(235) == [
            '###  ###  ###',
            '  #    #  #  ',
            '###  ###  ###',
            '#      #    #',
            '###  ###  ###'
        ]


class TestSplitLargeNumbers:
    def test_split_number_10(self):
        assert split_large_numbers(10) == [1, 0]

    def test_split_number_11(self):
        assert split_large_numbers(11) == [1, 1]

    def test_split_number_1789(self):
        assert split_large_numbers(1789) == [1, 7, 8, 9]


class TestMergeSingleNumberRepresentations:
    def test_transpose_lines(self):
        single_numbers = [['a', 'b', 'c', 'd', 'e'], ['f', 'g', 'h', 'i', 'j']]

        assert transpose_lines(single_numbers) == \
            [['a', 'f'], ['b', 'g'], ['c', 'h'], ['d', 'i'], ['e', 'j']]

    def test_join_lines(self):
        transposed =\
            [['a', 'f'], ['b', 'g'], ['c', 'h'], ['d', 'i'], ['e', 'j']]

        assert join_columns(transposed) ==\
            ['a  f', 'b  g', 'c  h', 'd  i', 'e  j']
