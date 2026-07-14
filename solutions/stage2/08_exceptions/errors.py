# ============================================================
# Stage 2 — Exercise 8: Exceptions — REFERENCE SOLUTION
# ============================================================

from collections.abc import Callable

# --- Task 8.1 — raising a ValueError ---


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("division by zero")
    return a / b


# --- Task 8.2 — custom exception type ---


class ValidationError(Exception):
    def __init__(self, field: str, reason: str) -> None:
        self.field = field
        self.reason = reason
        super().__init__(f"{field}: {reason}")


# --- Task 8.3 — using the custom exception ---


def check_age(age: int) -> None:
    if age < 0:
        raise ValidationError("age", "must not be negative")
    if age > 150:
        raise ValidationError("age", "unrealistically large")


# --- Task 8.4 — exception chaining ---


def find(mapping: dict[str, str], key: str) -> str:
    if key in mapping:
        return mapping[key]
    raise LookupError(f"key {key!r} not found") from KeyError(key)


# --- Task 8.5 — retry helper ---


def retry(attempts: int, fn: Callable[[], None]) -> None:
    last_exception: Exception | None = None
    for _ in range(attempts):
        try:
            fn()
            return
        except Exception as exc:
            last_exception = exc
    if last_exception is not None:
        raise last_exception
