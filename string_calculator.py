class NegativeNumbersError(Exception):
    pass


class StringCalculator:
    MAX_ALLOWED_NUMBER = 1000

    def add(self, numbers: str) -> int:
        if not numbers:
            return 0

        # まず改行をカンマに置換してから分割
        numbers = numbers.replace("\n", ",")
        nums = [int(num) for num in numbers.split(",")]

        # 負の数をチェック
        negative_numbers = [num for num in nums if num < 0]
        if negative_numbers:
            raise NegativeNumbersError(
                f"負の数は許可されていません: {', '.join(map(str, negative_numbers))}"
            )

        # 1000以下の数のみを合計
        return sum(num for num in nums if num <= self.MAX_ALLOWED_NUMBER)
