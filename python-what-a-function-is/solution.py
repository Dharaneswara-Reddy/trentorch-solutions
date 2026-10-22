
def is_even(n: int) -> bool:
    """
    Return True if n is even, False otherwise.
    """
    if n % 2 == 0:
        return True
    else:
        return False


def greet_formal(name: str, title: str) -> str:
    """
    Return a greeting string in the exact form:
    "Good day, {title} {name}."
    """
    return f"Good day, {title} {name}."


def apply_twice(func, value):
    """
    Call func on value, then call func again on the result.
    Return the final result.
    """
    result = func(value)
    result = func(result)
    return result
