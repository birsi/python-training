# ============================================================
# Stage 1 — Exercise 2: Functions — REFERENCE SOLUTION
# ============================================================

from collections.abc import Callable

# --- Task 2.1 — default parameters ---


def greet(name: str, greeting: str = "Hello") -> str:
    return f"{greeting}, {name}!"


# --- Task 2.2 — *args ---


def sum_all(*args: int) -> int:
    return sum(args)


# --- Task 2.3 — **kwargs ---


def build_profile(**kwargs: str) -> dict[str, str]:
    return dict(kwargs)


# --- Task 2.4 — closures and nonlocal ---


def make_counter() -> Callable[[], int]:
    count = 0

    def increment() -> int:
        nonlocal count
        count += 1
        return count

    return increment


# --- Task 2.5 — functions as values ---


def apply_twice(f: Callable[[int], int], x: int) -> int:
    return f(f(x))
