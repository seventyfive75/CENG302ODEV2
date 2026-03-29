from typing import Iterable, List

DEFAULT_TAX_RATE = 0.15
DEFAULT_LOG_FILE = "log.txt"


def calculate_total(amount: float, tax_rate: float = DEFAULT_TAX_RATE) -> float:
    """Return the total amount after applying tax."""
    return amount * (1 + tax_rate)


def format_total(amount: float) -> str:
    """Return a human-readable total string."""
    return f"Total: {amount:.2f}"


def append_to_log(values: List[float], filename: str = DEFAULT_LOG_FILE) -> None:
    """Append processed values to a log file."""
    with open(filename, "a", encoding="utf-8") as log_file:
        log_file.write(f"{values}\n")


def process_data(data: Iterable[float], tax_rate: float = DEFAULT_TAX_RATE, log_file: str = DEFAULT_LOG_FILE) -> List[float]:
    """Process a list of numeric values and return totals with side effects separated."""
    totals: List[float] = []

    for value in data:
        total = calculate_total(value, tax_rate)
        print(format_total(total))
        totals.append(total)

    append_to_log(totals, log_file)
    return totals
