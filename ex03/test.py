from contextlib import redirect_stdout
from io import StringIO
from unittest.mock import patch

from new_student import Student, generate_id

import unittest


class Ex03OutputTest(unittest.TestCase):

    def test_generate_id(self):
        # Given
        expected_pattern = r"[a-z]{15}"

        # When
        actual = generate_id()

        # Then
        self.assertRegex(actual, expected_pattern)

    def test_when_providing_id_should_raise_type_error(self):
        # Given / When
        with self.assertRaises(TypeError) as cm:
            Student(name="Edward", surname="agle", id="toto")

        # Then
        self.assertIn(
            "Student.__init__() got an unexpected"
            " keyword argument 'id'",
            str(cm.exception)
        )

    def test_when_providing_login_should_raise_type_error(self):
        # Given / When
        with self.assertRaises(TypeError) as cm:
            Student(name="Edward", surname="agle", login="Eagle")

        # Then
        self.assertIn(
            "Student.__init__() got an unexpected"
            " keyword argument 'login'",
            str(cm.exception)
        )

    def test_when_not_providing_name_should_raise_type_error(self):
        # Given / When
        with self.assertRaises(TypeError) as cm:
            Student(surname="agle")

        # Then
        self.assertIn(
            "missing 1 required positional argument: 'name'",
            str(cm.exception)
        )

    def test_when_not_providing_surname_should_raise_type_error(self):
        # Given / When
        with self.assertRaises(TypeError) as cm:
            Student(name="Edward")

        # Then
        self.assertIn(
            "missing 1 required positional argument: 'surname'",
            str(cm.exception)
        )

    def test_default_value_of_active_should_be_true(self):
        # Given / When
        student = Student(name="Edward", surname="agle")

        # Then
        self.assertEqual(student.active, True)

    @patch("random.choices", return_value="trannxhndgtolvh")
    def test_subject_tester_example(self, _):
        # Given
        # Redirects the output into a variable
        captured_output = StringIO()
        expected_pattern = (
            "Student(name='Edward', surname='agle', active=True,"
            " login='Eagle', id='trannxhndgtolvh')"
        )

        # When
        with redirect_stdout(captured_output):
            student = Student(name="Edward", surname="agle")
            print(student)
        actual = captured_output.getvalue().strip()

        # Then
        self.assertEqual(actual, expected_pattern)


if __name__ == "__main__":
    unittest.main()
