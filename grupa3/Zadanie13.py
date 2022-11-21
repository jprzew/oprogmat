def factorial2(n):
    """Calculates factorial (recursively)

    Args:
        n: int -- natural number

    Returns:
        factorial of the given number
    """

    if n == 0:
        return 1

    result = factorial2(n - 1) * n
    return result

print(factorial2(4))
