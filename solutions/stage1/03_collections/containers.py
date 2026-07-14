# ============================================================
# Stage 1 — Exercise 3: Collections — REFERENCE SOLUTION
# ============================================================


# --- Task 3.1 — list comprehension ---


def evens(nums: list[int]) -> list[int]:
    return [n for n in nums if n % 2 == 0]


# --- Task 3.2 — dict comprehension ---


def word_lengths(words: list[str]) -> dict[str, int]:
    return {word: len(word) for word in words}


# --- Task 3.3 — dedupe via set ---


def unique_sorted(nums: list[int]) -> list[int]:
    return sorted(set(nums))


# --- Task 3.4 — comma-ok idiom ---


def safe_get(d: dict[str, int], key: str) -> int | None:
    return d.get(key)


# --- Task 3.5 — list-sharing mutation ---


def append_to_all(lists: list[list[int]], value: int) -> None:
    for inner in lists:
        inner.append(value)
