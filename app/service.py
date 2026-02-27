from .constants import DEFAULT_THRESHOLD


def calculate_total(orders: list[float]) -> float:
    return sum(orders)


def calculate_average(orders: list[float]) -> float:
    if not orders:
        return 0.0
    return sum(orders) / len(orders)


def filter_high_value_orders(orders: list[float], threshold: float = DEFAULT_THRESHOLD) -> list[float]:
    return [o for o in orders if o >= threshold]