def callLimit(limit: int):
    """
    Decorator factory that defines a maximum amount of time the bound method
    can be called. The purpose of this layer is to capture the parameter limit.

    Args:
        limit (int): The maximum amount of time the bound method can be called.

    Returns:
        function: The actual decorator.
    """
    count = 0

    def callLimiter(function):
        """
        The decorator function. The purpose of this layer is to capture the
        function being decorated.

        Args:
            - function (function): The decorated function.

        Returns:
            function: A wrapped version of the decorated function.
        """
        def limit_function(*args, **kwargs):
            """
            Executes the bound method. If the count has reached the limit,
            prints an error message instead of executing.

            Args:
                *args: Variable length argument list.
                **kwargs: Arbitrary keyword arguments.
            """
            nonlocal count
            if count >= limit:
                print(f"Error: {function} call too many times")
            else:
                function(*args, **kwargs)
                count += 1

        return limit_function

    return callLimiter
