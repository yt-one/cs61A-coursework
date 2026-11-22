"""Lab 7: Iterators and Generators."""


from socket import fromfd
from collections.abc import Iterator


def count_occurrences(t: Iterator[int], n: int, x: int) -> int:
    """Return the number of times that x is equal to one of the
    first n items of iterator t.

    >>> s = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    >>> count_occurrences(s, 10, 9)
    3
    >>> t = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    >>> count_occurrences(t, 3, 10)
    2
    >>> u = iter([3, 2, 2, 2, 1, 2, 1, 4, 4, 5, 5, 5])
    >>> count_occurrences(u, 1, 3)  # Only iterate over 3
    1
    >>> count_occurrences(u, 3, 2)  # Only iterate over 2, 2, 2
    3
    >>> list(u)                     # Ensure that the iterator has advanced the right amount
    [1, 2, 1, 4, 4, 5, 5, 5]
    >>> v = iter([4, 1, 6, 6, 7, 7, 6, 6, 2, 2, 2, 5])
    >>> count_occurrences(v, 6, 6)
    2
    """
    "*** YOUR CODE HERE ***"
    count = 0
    for i in range(n):
        if next(t) == x:
            count += 1
    return count


def repeated(t: Iterator[int], k: int) -> int:
    """Return the first value in iterator t that appears k times in a row,
    calling next on t as few times as possible.

    >>> s = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    >>> repeated(s, 2)
    9
    >>> t = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    >>> repeated(t, 3)
    8
    >>> u = iter([3, 2, 2, 2, 1, 2, 1, 4, 4, 5, 5, 5])
    >>> repeated(u, 3)
    2
    >>> repeated(u, 3)
    5
    >>> v = iter([4, 1, 6, 6, 7, 7, 8, 8, 2, 2, 2, 5])
    >>> repeated(v, 3)
    2
    """
    assert k > 1
    "*** YOUR CODE HERE ***"
    count = 0
    last = None
    for val in t:
        if val == last:
            count += 1
        else:
            count = 1
        if count == k:
            return val
        last = val
    return None


def hailstone(n):
    """Yield the items of the hailstone sequence starting at n.

    >>> hail_gen = hailstone(10)
    >>> [next(hail_gen) for _ in range(10)]
    [10, 5, 16, 8, 4, 2, 1, 4, 2, 1]
    >>> next(hail_gen)
    4
    """
    "*** YOUR CODE HERE ***"
    yield n
    if n == 1:
        yield from hailstone(4)
    elif n % 2 == 0:
        yield from hailstone(n // 2)
    else:
        yield from hailstone(3 * n + 1)


def merge(a, b):
    """Yield the items of increasing infinite iterators a and b in order,
    removing repeats. Assume that a and b have no repeats.

    >>> def sequence(start, step):
    ...     while True:
    ...         yield start
    ...         start += step
    >>> a = sequence(2, 3)  # 2, 5, 8, 11, 14, ...
    >>> b = sequence(3, 2)  # 3, 5, 7, 9, 11, 13, 15, ...
    >>> result = merge(a, b)
    >>> type(result)
    <class 'generator'>
    >>> [next(result) for _ in range(10)]
    [2, 3, 5, 7, 8, 9, 11, 13, 14, 15]
    """
    next_a, next_b = next(a), next(b)
    while True:
        if next_a == next_b:
            "*** YOUR CODE HERE ***"
            yield next_a
            next_a = next(a)
            next_b = next(b)
        elif next_a < next_b:
            "*** YOUR CODE HERE ***"
            yield next_a
            next_a = next(a)
        else:
            "*** YOUR CODE HERE ***"
            yield next_b
            next_b = next(b)    


def squares(total: int, k: int) -> Iterator[list[int]]:
    """Yield the ways in which perfect squares greater or equal to k*k sum to total.

    >>> list(squares(10, 1))  # All lists of perfect squares that sum to 10
    [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [4, 1, 1, 1, 1, 1, 1], [4, 4, 1, 1], [9, 1]]
    >>> list(squares(20, 2))  # Only use perfect squares greater or equal to 4 (2*2).
    [[4, 4, 4, 4, 4], [16, 4]]
    """
    assert total > 0 and k > 0
    if total == k * k:
        yield [k * k]
    elif total > k * k:
        for s in squares(total-k*k, k):
            yield s + [k * k]
        yield from squares(total, k + 1)
