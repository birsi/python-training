# ============================================================
# Stage 3 — Exercise 10: Threading — REFERENCE SOLUTION
# ============================================================

import threading
from collections.abc import Callable

# --- Task 10.1 — run_all ---


def run_all(*fns: Callable[[], None]) -> None:
    threads = [threading.Thread(target=fn) for fn in fns]
    for t in threads:
        t.start()
    for t in threads:
        t.join()


# --- Task 10.2 — SafeCounter ---


class SafeCounter:
    def __init__(self) -> None:
        self._lock = threading.Lock()
        self._value = 0

    def increment(self) -> None:
        with self._lock:
            self._value += 1

    def value(self) -> int:
        with self._lock:
            return self._value


# --- Task 10.3 — square_all ---


def square_all(nums: list[int]) -> list[int]:
    result = [0] * len(nums)

    def square(i: int, n: int) -> None:
        result[i] = n * n

    threads = [threading.Thread(target=square, args=(i, n)) for i, n in enumerate(nums)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    return result
