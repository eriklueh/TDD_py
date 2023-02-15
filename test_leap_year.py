import unittest


def is_leap(year):
    if year % 4 == 0 and year % 100 != 0:
        return True
    return year % 4 == 0 and year % 100 == 0 and year % 400 == 0


class LeapYearsTestCase(unittest.TestCase):
    def test_when_year_divisible_by_4_then_leap(self):
        self.assertTrue(is_leap(2020))
        self.assertTrue(is_leap(2024))

    def test_when_year_not_divisible_by_4_then_leap(self):
        self.assertFalse(is_leap(2021))
        self.assertFalse(is_leap(2023))

    def test_when_year_divisible_by_4_and_100_then_not_leap(self):
        self.assertFalse(is_leap(2300))
        self.assertFalse(is_leap(2500))

    def test_when_year_divisible_by_4_and_100_and_400_then_leap(self):
        self.assertTrue(is_leap(2000))
        self.assertTrue(is_leap(2400))
