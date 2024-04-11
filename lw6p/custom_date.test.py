import unittest

from custom_date import CustomDate


class TestDate(unittest.TestCase):

    def test_first_date_constructor(self):
        # Arrange
        date = CustomDate(1, 1, 1)

        # Act

        # Assert
        self.assertEqual(date.get_day(), 1, "Значение дня должно быть равно 1")
        self.assertEqual(date.get_month(), 1, "Значение месяца должно быть равно 1")
        self.assertEqual(date.get_year(), 1, "Значения года должно равняться 1")

    def test_last_date_constructor(self):
        # Arrange
        date = CustomDate(31, 12, 9999)

        # Act

        # Assert
        self.assertEqual(date.get_day(), 31, "Значение дня должно быть равно 31")
        self.assertEqual(date.get_month(), 12, "Значение месяца должно быть равно 12")
        self.assertEqual(date.get_year(), 9999, "Значения года должно равняться 9999")

    def test_last_day_february_leap_constructor(self):
        # Arrange
        date = CustomDate(29, 2, 2000)

        # Act

        # Assert
        self.assertEqual(
            date.get_day(),
            29,
            "Значение дня должно быть равно 29 для февраля 2000 (Високосный)",
        )
        self.assertEqual(date.get_month(), 2, "Значение месяца должно быть равно 2")
        self.assertEqual(date.get_year(), 2000, "Значения года должно равняться 2000")

    def test_last_day_february_not_leap_constructor(self):
        # Assert должен произойти вместе с Arrange, т.к. он используется для проверки корректности конструктора

        # Arrange
        
        # Assert
        with self.assertRaises(ValueError, msg="День 29 не может быть в феврале 2001 (НЕвисокосный)"):
            CustomDate(29, 2, 2001)

    def test_invalid_day_set(self):
        # Arrange
        date = CustomDate(1, 1, 1)

        # Act

        # Assert
        with self.assertRaises(ValueError, msg="День 32 не может быть в январе"):
            date.set_day(32)

        with self.assertRaises(ValueError, msg="День 0 не может быть в январе, отсчёт с 1"):
            date.set_day(0)

    def test_invalid_month_set(self):
        # Arrange
        date = CustomDate(1, 1, 1)

        # Act

        # Assert
        with self.assertRaises(ValueError, msg="Не может быть 13 месяц в году"):
            date.set_month(13)

        with self.assertRaises(ValueError, msg="Не может быть 0 месяц в году, отсчёт с 1"):
            date.set_month(0)

    def test_invalid_year_set(self):
        # Arrange
        date = CustomDate(1, 1, 1)

        # Act

        # Assert
        with self.assertRaises(ValueError, msg="Не может быть 0 год, отсчёт с 1"):
            date.set_year(0)

        with self.assertRaises(ValueError, msg="Не может быть больше чем 9999 год"):
            date.set_year(10000)

    def test_next_day(self):
        # Arrange
        date = CustomDate(31, 12, 9998)

        # Act
        date.next_day()

        # Assert
        self.assertEqual(
            date.get_day(), 1, "Значение дня должно быть равно 1 после 31го числа"
        )
        self.assertEqual(
            date.get_month(), 1, "Значение месяца должно быть равно 1 после 12го месяца"
        )
        self.assertEqual(
            date.get_year(),
            9999,
            "Значения года должно равняться 9999 после 9998 числа",
        )

    def test_next_day_not_possible(self):
        # Arrange
        date = CustomDate(31, 12, 9999)

        # Act & Assert. Assert на исключение в Act
        with self.assertRaises(ValueError) as context:
            date.next_day()

        if context.exception is None:
            self.fail("Нельзя получить следующий день, 9999 год последний")

    def test_previous_day(self):
        # Arrange
        date = CustomDate(1, 1, 9999)

        # Act
        date.previous_day()

        # Assert
        self.assertEqual(
            date.get_day(), 31, "Значение дня должно быть равно 31 перед 1ым числом"
        )
        self.assertEqual(
            date.get_month(),
            12,
            "Значение месяца должно быть равно 12 перед 1ым месяцем",
        )
        self.assertEqual(
            date.get_year(), 9998, "Значения года должно равняться 9998 перед 9999"
        )

    def test_previous_day_not_possible(self):
        # Arrange
        date = CustomDate(1, 1, 1)

        # Act & Assert. Assert на исключение в Act
        with self.assertRaises(ValueError) as context:
            date.previous_day()

        if context.exception is None:
            self.fail("Нельзя получить предыдущий день, 1 год первый")

    def test_difference_in_days_with_first_date_earlier(self):
        # Arrange
        date1 = CustomDate(1, 1, 1)
        date2 = CustomDate(1, 1, 2)

        # Act
        diff = date1.difference_in_days(date2)

        # Assert
        self.assertEqual(
            diff,
            365,
            "Разница между 01.01.0001 и 01.01.0002 должна быть 365 дней (Последняя дата не включается). Разница считается по модулю",
        )

    def test_difference_in_days_with_first_date_later(self):
        # Arrange
        date1 = CustomDate(1, 1, 2)
        date2 = CustomDate(1, 1, 1)

        # Act
        diff = date1.difference_in_days(date2)

        # Assert
        self.assertEqual(
            diff,
            365,
            "Разница между 01.01.0002 и 01.01.0001 должна быть 365 дней (Последняя дата не включается). Разница считается по модулю",
        )

    def test_to_string(self):
        # Arrange
        date = CustomDate(1, 1, 1)

        # Act
        str_date = str(date)

        # Assert
        self.assertEqual(
            str_date,
            "01.01.0001",
            "Дата должна быть в формате ДД.ММ.ГГГГ, учитываются ведущие нули",
        )

    def test_compare_first_date_earlier_day(self):
        # Arrange
        date1 = CustomDate(1, 1, 1)
        date2 = CustomDate(2, 1, 1)

        # Act
        compare_value = date1.compare_to(date2)

        # Assert
        self.assertEqual(
            compare_value,
            -1,
            "Результат сравнения должен быть = -1, т.к. дата 1 раньше даты 2",
        )

    def test_compare_first_date_earlier_month(self):
        # Arrange
        date1 = CustomDate(1, 1, 1)
        date2 = CustomDate(1, 2, 1)

        # Act
        compare_value = date1.compare_to(date2)

        # Assert
        self.assertEqual(
            compare_value,
            -1,
            "Результат сравнения должен быть = -1, т.к. дата 1 раньше даты 2",
        )

    def test_compare_first_date_earlier_year(self):
        # Arrange
        date1 = CustomDate(1, 1, 1)
        date2 = CustomDate(1, 1, 2)

        # Act
        compare_value = date1.compare_to(date2)

        # Assert
        self.assertEqual(
            compare_value,
            -1,
            "Результат сравнения должен быть = -1, т.к. дата 1 раньше даты 2",
        )

    def test_compare_first_date_later_day(self):
        # Arrange
        date1 = CustomDate(2, 1, 1)
        date2 = CustomDate(1, 1, 1)

        # Act
        compare_value = date1.compare_to(date2)

        # Assert
        self.assertEqual(
            compare_value,
            1,
            "Результат сравнения должен быть = 1, т.к. дата 1 позже даты 2",
        )

    def test_compare_first_date_later_month(self):
        # Arrange
        date1 = CustomDate(1, 2, 1)
        date2 = CustomDate(1, 1, 1)

        # Act
        compare_value = date1.compare_to(date2)

        # Assert
        self.assertEqual(
            compare_value,
            1,
            "Результат сравнения должен быть = 1, т.к. дата 1 позже даты 2",
        )

    def test_compare_first_date_later_year(self):
        # Arrange
        date1 = CustomDate(1, 1, 2)
        date2 = CustomDate(1, 1, 1)

        # Act
        compare_value = date1.compare_to(date2)

        # Assert
        self.assertEqual(
            compare_value,
            1,
            "Результат сравнения должен быть = 1, т.к. дата 1 позже даты 2",
        )

    def test_compare_first_date_equal(self):
        # Arrange
        date1 = CustomDate(1, 1, 1)
        date2 = CustomDate(1, 1, 1)

        # Act
        compare_value = date1.compare_to(date2)

        # Assert
        self.assertEqual(
            compare_value,
            0,
            "Результат сравнения должен быть = 0, т.к. дата 1 равна дате 2",
        )


if __name__ == "__main__":
    unittest.main()
