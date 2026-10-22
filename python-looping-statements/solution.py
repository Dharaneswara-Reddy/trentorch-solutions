def countdown_with_skip(start: int) -> list:
    """
    Count down from start to 1, skipping 3.
    """
    result = []

    while start >= 1:
        if start == 3:
            start -= 1
            continue

        result.append(start)
        start -= 1

    return result


def find_first_negative(numbers: list) -> int | None:
    """
    Find the first negative number using a while loop.
    """
    index = 0

    while index < len(numbers):
        if numbers[index] < 0:
            result = numbers[index]
            break
        index += 1
    else:
        return None

    return result


def sum_with_index(numbers: list) -> dict:
    """
    Map each index to the running sum up to that index.
    """
    result = {}
    running_sum = 0

    for index, number in enumerate(numbers):
        running_sum += number
        result[index] = running_sum

    return result


def manual_iteration_trace(items: list) -> list:
    """
    Retrieve all elements manually using an iterator and next().
    """
    result = []
    iterator = iter(items)

    while True:
        try:
            item = next(iterator)
            result.append(item)
        except StopIteration:
            break

    return result
