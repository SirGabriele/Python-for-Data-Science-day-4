from contextlib import redirect_stdout
from io import StringIO

from callLimit import callLimit

import unittest
import re


class Ex02OutputTest(unittest.TestCase):

    def test_subject_tester_example(self):
        # Given
        # Redirects the output into a variable
        captured_output = StringIO()
        error_call_limit_pattern = r"Error: <function .*?> call too many times"

        # When
        with redirect_stdout(captured_output):
            @callLimit(3)
            def f():
                print("f()")

            @callLimit(1)
            def g():
                print("g()")
            for i in range(3):
                f()
                g()
        actual = captured_output.getvalue().strip()
        # Counts the amount of times a call limit is triggered
        matches = re.findall(error_call_limit_pattern, actual)

        # Then
        self.assertEqual(actual.count("f()"), 3)
        self.assertEqual(actual.count("g()"), 1)
        self.assertEqual(len(matches), 2)


if __name__ == "__main__":
    unittest.main()
