import unittest


def foo_bar_baz(x):
    if x % 2 == 0:
        return tuple(("foo",))

    if x == 1:
        return tuple(("bar", "baz"))
    elif x > 1:
        for i in range(2, x):
            if (x % i) == 0:
                break
        else:
            return tuple(("bar", "baz"))

    if x % 2 != 0:
        return tuple(("bar",))


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
