import unittest
from string_calculator import (
    StringCalculator,
)


class TestStringCalculator(unittest.TestCase):
    # 各テストケースの前に実行される設定
    def setUp(self):
        self.calculator = StringCalculator()

    # 空の文字列を入力すると0を返す
    def test_empty_string_returns_zero(self):
        self.assertEqual(self.calculator.add(""), 0)

    # 単一の数字の文字列の場合はその数値を返す
    def test_single_number_returns_value(self):
        self.assertEqual(self.calculator.add("1"), 1)
        self.assertEqual(self.calculator.add("2"), 2)

    # Step1:


if __name__ == "__main__":
    unittest.main()
