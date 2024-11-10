import unittest
from string_calculator import (
    StringCalculator,
    NegativeNumbersError,
)


class TestStringCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = StringCalculator()

    def test_empty_string_returns_zero(self):
        self.assertEqual(self.calculator.add(""), 0)

    def test_single_number_returns_value(self):
        self.assertEqual(self.calculator.add("1"), 1)
        self.assertEqual(self.calculator.add("2"), 2)

    def test_two_numbers_returns_sum(self):
        self.assertEqual(self.calculator.add("1,2"), 3)
        self.assertEqual(self.calculator.add("3,5"), 8)

    def test_multiple_numbers_returns_sum(self):
        self.assertEqual(self.calculator.add("1,2,3"), 6)
        self.assertEqual(self.calculator.add("1,2,3,4,5"), 15)

    # Step 2: 改行対応のテストケース追加
    def test_newline_as_separator(self):
        self.assertEqual(self.calculator.add("1\n2"), 3)
        self.assertEqual(self.calculator.add("3\n4"), 7)

    def test_mixed_separators(self):
        self.assertEqual(self.calculator.add("1\n2,3"), 6)
        self.assertEqual(self.calculator.add("1,2\n3,4"), 10)
        self.assertEqual(self.calculator.add("1,2\n3\n4,5"), 15)

    # Step 3: 負の数のテストケース追加
    def test_single_negative_number_throws_exception(self):
        with self.assertRaises(NegativeNumbersError) as context:
            self.calculator.add("-1")
        self.assertEqual(str(context.exception), "負の数は許可されていません: -1")

    def test_multiple_negative_numbers_throws_exception(self):
        with self.assertRaises(NegativeNumbersError) as context:
            self.calculator.add("1,-2,-3,4,-5")
        self.assertEqual(
            str(context.exception), "負の数は許可されていません: -2, -3, -5"
        )

    def test_negative_with_newlines_throws_exception(self):
        with self.assertRaises(NegativeNumbersError) as context:
            self.calculator.add("1\n-2,3\n-4")
        self.assertEqual(str(context.exception), "負の数は許可されていません: -2, -4")

    # Step 4: 1000以上の数を無視するテストケース追加
    def test_numbers_greater_than_1000_are_ignored(self):
        self.assertEqual(self.calculator.add("2,1001"), 2)
        self.assertEqual(self.calculator.add("1000,1001"), 1000)
        self.assertEqual(self.calculator.add("1,999,1000,1001,2"), 2002)

    def test_mixed_large_numbers_and_newlines(self):
        self.assertEqual(self.calculator.add("2\n1001"), 2)
        self.assertEqual(self.calculator.add("1000\n1001,2"), 1002)
        self.assertEqual(self.calculator.add("1\n2,1001\n1002,3"), 6)


if __name__ == "__main__":
    unittest.main()
