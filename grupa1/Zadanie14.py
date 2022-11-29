def fibonacci2(n):
    """Calculates n-th Fibonacci number (iteratively)

    Args:
        n: int - natural number (including zero)

    Returns:
        n-th Fibonacci number
    """

    if n == 0:
        return 0

    calculated = [0, 1]
    for k in range(2, n + 1):
        calculated.append(calculated[-1] + calculated[-2])

    return calculated[-1]

print(fibonacci2(3))