import unittest
from foo_bar_baz import foo_bar_baz


class FooBarBazTestCase(unittest.TestCase):
    def test_when_even_then_foo(self):
        self.assertEqual(("foo",), foo_bar_baz(2))
        self.assertEqual(("foo",), foo_bar_baz(72))

    def test_when_odd_and_not_prime_then_bar(self):
        self.assertEqual(("bar",), foo_bar_baz(81))

    def test_when_prime_then_baz(self):
        self.assertEqual(("bar", "baz"), foo_bar_baz(1))
        self.assertEqual(("bar", "baz"), foo_bar_baz(7))


if __name__ == '__main__':
    unittest.main()
