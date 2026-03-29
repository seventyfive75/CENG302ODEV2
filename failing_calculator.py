from typing import Iterable


def average_ratios(numbers: Iterable[float]) -> float:
    """Return the average of 100 / number for each nonzero value.

    Raises:
        ValueError: if numbers is empty or contains zero.
    """
    values = list(numbers)
    if not values:
        raise ValueError("numbers must contain at least one value")

    ratios = []
    for number in values:
        if number == 0:
            raise ValueError("numbers must not contain zero")
        ratios.append(100 / number)

    return sum(ratios) / len(ratios)


if __name__ == "__main__":
    try:
        print(average_ratios([10, 5, 0]))
    except ValueError as error:
        print(f"Error: {error}")
