def square(x: int | float) -> int | float:
    """Returns the square of x"""
    return x ** 2


def pow(x: int | float) -> int | float:
    """Returns x raised to the power of x"""
    return x ** x


def outer(x: int | float, function) -> object:
    """
    Returns a callable that repeatedly applies a function to a number.

    Args:
        - x (int | float): The starting value.
        - function (function): The function to repeatedly apply to the number.

    Returns:
        A function that, when called, applies function to x, updates the
        internally stored value and returns it.

    Example:
        counter = outer(3, square)
        counter() // Returns 9
        counter() // Returns 81
        counter() // Returns 6561
    """
    value = x

    def inner():
        """Function that returns the result of the bound function."""
        nonlocal value
        value = function(value)
        return value

    return inner
