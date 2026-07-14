# ============================================================
# Stage 1 — Exercise 4: Mutability — REFERENCE SOLUTION
# ============================================================

import copy

# --- Task 4.1 — identity vs equality ---


def is_same_object(a: object, b: object) -> bool:
    return a is b


# --- Task 4.2 — mutable default argument footgun ---


def add_item(item: str, bucket: list[str] | None = None) -> list[str]:
    if bucket is None:
        bucket = []
    bucket.append(item)
    return bucket


# --- Task 4.3 — shallow vs deep copy ---


def deep_copy_matrix(matrix: list[list[int]]) -> list[list[int]]:
    return copy.deepcopy(matrix)


# --- Task 4.4 — mutable vs immutable pass semantics ---


def increment_in_place(counter: dict[str, int], key: str) -> None:
    counter[key] = counter.get(key, 0) + 1


def increment_value(n: int) -> int:
    return n + 1
