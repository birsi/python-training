# ============================================================
# Stage 1 — Exercise 1: Basics — REFERENCE SOLUTION
# ============================================================


# --- Task 1.1 — greet ---


def greet(name: str) -> str:
    return f"Hello, {name}!"


# --- Task 1.2 — constant convention ---

MAX_RETRIES: int = 3


# --- Task 1.3 — no automatic zero values ---


def zero_values() -> tuple[int, str, bool]:
    return (0, "", False)


# --- Task 1.4 — true division ---


def average(a: int, b: int) -> float:
    return a / b


# --- Task 1.5 — floor division ---


def floor_divide(a: int, b: int) -> int:
    return a // b
