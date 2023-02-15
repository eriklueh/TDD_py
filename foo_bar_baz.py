def is_even(x):
    return x % 2 == 0


def is_prime(x):
    if x == 1:
        return True
    elif x > 1:
        for i in range(2, x):
            if (x % i) == 0:
                break
        else:
            return True
    return False


def is_odd(x):
    return not is_even(x)


def foo_bar_baz(x):
    if is_even(x):
        return tuple(("foo",))
    if is_prime(x):
        return tuple(("bar", "baz"))
    if is_odd(x):
        return tuple(("bar",))
