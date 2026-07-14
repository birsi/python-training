# ============================================================
# Stage 3 — Exercise 9: Generics — REFERENCE SOLUTION
# ============================================================

from collections.abc import Callable

# --- Task 9.1 — first ---


def first[T](items: list[T]) -> T:
    return items[0]


# --- Task 9.2 — generic Stack ---


class Stack[T]:
    def __init__(self) -> None:
        self._items: list[T] = []

    def push(self, item: T) -> None:
        self._items.append(item)

    def pop(self) -> T:
        return self._items.pop()

    def peek(self) -> T:
        return self._items[-1]

    def is_empty(self) -> bool:
        return len(self._items) == 0


# --- Task 9.3 — constrained type parameter ---


def max_of[T: (int, float)](items: list[T]) -> T:
    return max(items)


# --- Task 9.4 — map_option ---


def map_option[T, U](value: T | None, fn: Callable[[T], U]) -> U | None:
    if value is None:
        return None
    return fn(value)
