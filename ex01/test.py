from contextlib import redirect_stdout
from io import StringIO

from in_out import square, pow, outer

import unittest


class Ex01OutputTest(unittest.TestCase):

    def test_square(self):
        # Given / When
        actual = square(15)
        expected = 225

        # Then
        self.assertEqual(actual, expected)

    def test_pow(self):
        # Given / When
        actual = pow(4)
        expected = 256

        # Then
        self.assertEqual(actual, expected)

    def test_subject_tester_example(self):
        # Given
        # Redirects the output into a variable
        captured_output = StringIO()

        # When
        with redirect_stdout(captured_output):
            my_counter = outer(3, square)
            print(my_counter())
            print(my_counter())
            print(my_counter())
            print("---")
            another_counter = outer(1.5, pow)
            print(another_counter())
            print(another_counter())
            print(another_counter())
        actual = captured_output.getvalue().strip()

        expected = (
            "9\n"
            "81\n"
            "6561\n"
            "---\n"
            "1.8371173070873836\n"
            "3.056683336818703\n"
            "30.42684786675409"
        )

        # Then
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
