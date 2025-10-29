from contextlib import redirect_stdout
from io import StringIO

from statistics import ft_statistics, mean, median, quartile, std, var

import unittest


class Ex00OutputTest(unittest.TestCase):

    def test_when_empty_args_function_mean_should_raise_type_error(self):
        # Given / When
        with self.assertRaises(TypeError) as cm:
            mean()

        # Then
        self.assertIn(
            "At least one value must be given.",
            str(cm.exception)
        )

    def test_when_empty_args_function_median_should_raise_type_error(self):
        # Given / When
        with self.assertRaises(TypeError) as cm:
            median()

        # Then
        self.assertIn(
            "At least one value must be given.",
            str(cm.exception)
        )

    def test_when_empty_args_function_quartile_should_raise_type_error(self):
        # Given / When
        with self.assertRaises(TypeError) as cm:
            quartile()

        # Then
        self.assertIn(
            "At least one value must be given.",
            str(cm.exception)
        )

    def test_when_empty_args_function_std_should_raise_type_error(self):
        # Given / When
        with self.assertRaises(TypeError) as cm:
            std()

        # Then
        self.assertIn(
            "At least one value must be given.",
            str(cm.exception)
        )

    def test_when_empty_args_function_var_should_raise_type_error(self):
        # Given / When
        with self.assertRaises(TypeError) as cm:
            var()

        # Then
        self.assertIn(
            "At least one value must be given.",
            str(cm.exception)
        )

    def test_when_odd_args_function_median_should_return_median(self):
        # Given / When
        actual = median(5, 234, 112, 65, 9231)
        expected = 112

        # Then
        self.assertEqual(actual, expected)

    def test_when_even_args_function_median_should_return_median(self):
        # Given / When
        actual = median(5, 234, 112, 65)
        expected = 88.5

        # Then
        self.assertEqual(actual, expected)

    def test_when_odd_args_function_quartile_should_return_median(self):
        # Given / When
        actual = quartile(5, 432, 213, 533, 65, 8)
        expected = (8, 432)

        # Then
        self.assertEqual(actual, expected)

    def test_when_even_args_function_quartile_should_return_median(self):
        # Given / When
        actual = quartile(5, 432, 213, 533, 65, 8, 12)
        expected = (8, 432)

        # Then
        self.assertEqual(actual, expected)

    def test_subject_tester_example(self):
        # Given
        # Redirects the output into a variable
        captured_output = StringIO()

        # When
        with redirect_stdout(captured_output):
            ft_statistics(
                1, 42, 360, 11, 64,
                toto="mean", tutu="median", tata="quartile"
            )
            print("-----")
            ft_statistics(
                5, 75, 450, 18, 597, 27474, 48575,
                hello="std", world="var"
            )
            print("-----")
            ft_statistics(
                5, 75, 450, 18, 597, 27474, 48575,
                ejfhhe="heheh", ejdjdejn="kdekem"
            )
            print("-----")
            ft_statistics(toto="mean", tutu="median", tata="quartile")
        actual = captured_output.getvalue().strip()

        expected = (
            "mean : 95.6\n"
            "median : 42\n"
            "quartile : [11, 64]\n"
            "-----\n"
            "std : 17982.70124086944\n"
            "var : 323377543.9183673\n"
            "-----\n"
            "-----\n"
            "ERROR\n"
            "ERROR\n"
            "ERROR"
        )

        # Then
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
