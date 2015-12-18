def fact(n):
    """
    >>> fact(0)
    1
    """
    if n < 0:
        raise ValueError
    elif n == 0:
        return 1
    else:
        return n * fact(n - 1)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
