def get_input(prompt: str) -> float:
    """
    Vraagt de gebruiker om een getal en geeft dit terug als float.
    """
    return float(input(prompt))


def add(a: float, b: float) -> float:
    """
    Tel twee getallen bij elkaar op.
    """
    return a + b


def subtract(a: float, b: float) -> float:
    """
    Trek b af van a.
    """
    return a - b


def multiply(a: float, b: float) -> float:
    """
    Vermenigvuldigt twee getallen.
    """
    return a * b


def divide(a: float, b: float) -> float:
    """
    Deelt a door b.
    """
    return a / b


def show_result(result: float) -> None:
    """
    Toont het resultaat aan de gebruiker.
    """
    print("Resultaat:", result)