from ascii_art.number_to_ascii_art import number_to_ascii_art


class TestSingleNumbersToAscii:
    def test_the_number_zero(self):
        assert number_to_ascii_art(0) == [
            '###',
            '# #',
            '# #',
            '# #',
            '###'
        ]

    def test_the_number_one(self):
        assert number_to_ascii_art(1) == [
            '  #',
            '  #',
            '  #',
            '  #',
            '  #'
        ]

    def test_the_number_two(self):
        assert number_to_ascii_art(2) == [
            '###',
            '  #',
            '###',
            '#  ',
            '###'
        ]

    def test_the_number_three(self):
        assert number_to_ascii_art(3) == [
            '###',
            '  #',
            '###',
            '  #',
            '###'
        ]

    def test_the_number_nine(self):
        assert number_to_ascii_art(9) == [
            '###',
            '# #',
            '###',
            '  #',
            '###'
        ]
