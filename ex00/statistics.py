def mean(*args) -> float:
    """
    Calculates the mean of a list of N numbers.

    Args:
        *args: A list of N numbers.
    Returns:
        The list's mean as float.
    """
    if not args:
        raise TypeError("At least one value must be given.")

    total = count = 0

    for arg in args:
        total += arg
        count += 1

    return total / count


def median(*args) -> float:
    """
    Calculates the median of a list of N numbers.

    If the list has an odd length, returns the middle value.

    If the list has an even length, returns the mean of the two middle values.

    Args:
        *args: A list of N numbers.
    Returns:
        The list's median as float.
    """
    if not args:
        raise TypeError("At least one value must be given.")

    sorted_numbers = sorted(args)
    length = len(sorted_numbers)
    middle_index = length // 2

    # Even number of elements
    if length % 2 == 0:
        return (sorted_numbers[middle_index - 1]
                + sorted_numbers[middle_index]) / 2
    # Odd number of elements
    else:
        return sorted_numbers[middle_index]


def quartile(*args) -> (float, float):
    """
    Calculates the first and third quartiles of a list of N numbers. The
    method used is a quite simple method. This choice was only made to fit the
    subject's example.

    First quartile's index is equal to the whole division of N by 4.

    Third quartile's index is equal to 3 times the whole division of N by 4.

    Args:
        *args: A list of N numbers.
    Returns:
        A tuple containing first and third quartiles.
    """
    if not args:
        raise TypeError("At least one value must be given.")

    sorted_numbers = sorted(args)
    length = len(sorted_numbers)
    q1_index = length // 4
    q3_index = length * 3 // 4

    return sorted_numbers[q1_index], (sorted_numbers[q3_index])


def std(*args) -> float:
    """
    Calculates the standard deviation of a list of N numbers.

    Args:
        *args: A list of N numbers.
    Returns:
        The list's standard deviation as float.
    """
    if not args:
        raise TypeError("At least one value must be given.")

    variance = var(*args)
    # Calculates the standard deviation by getting the square root of variance
    standard_deviation = variance ** 0.5
    return standard_deviation


def var(*args) -> float:
    """
    Calculates the variance of a list of N numbers.

    Args:
        *args: A list of N numbers.
    Returns:
        The list's variance as float.
    """
    if not args:
        raise TypeError("At least one value must be given.")

    # Calculates the mean value
    mean_value = mean(*args)
    # Creates a list containing N times the mean value
    array = [mean_value] * len(args)
    # For each element in the list, subtracts the mean value
    array = [arg - mean_value for arg in args]
    # For each element in the list, squares it
    array = [val ** 2 for val in array]
    # Calculates the mean value of the transformed array
    variance = mean(*array)
    return variance


def ft_statistics(*args, **kwargs) -> None:
    """
    Obtains different statistic values for a list of N numbers.

    Args:
        *args: A list of N numbers.
        **kwargs: Key-value pairs where the value is a string specifying
            which statistic to compute. Supported values are: `mean`, `median`,
            `quartile` (first and third quartiles), `std` (standard deviation)
            and `var` (variance).

    Notes:
        The keys in **kwargs are ignored. Only the values determine
        which computations are performed.
    """
    for key, value in kwargs.items():
        if not args:
            print("ERROR")
            continue
        match value:
            case "quartile":
                res = quartile(*args)
                print(f"quartile : [{res[0]}, {res[1]}]")
            case "mean":
                res = mean(*args)
                print("mean :", res)
            case "median":
                res = median(*args)
                print("median :", res)
            case "std":
                res = std(*args)
                print("std :", res)
            case "var":
                res = var(*args)
                print("var :", res)
            case _:
                pass
