# ============================================================
# Stage 1 — Exercise 3: Collections
# ============================================================
#
# GOAL: List/dict/set comprehensions, the comma-ok idiom, and the
# list-sharing mutation trap.
#
# Rules:
#   - Don't modify test_containers.py — it's the test suite.
#   - Check: pytest exercises/stage1/03_collections/
#     (functions fail with AttributeError until every task is done —
#     that's your to-do list)
#
# When you're done, ask Claude to review this exercise.
# ============================================================

# --- Task 3.1 ---------------------------------------------------
# Write evens(nums: list[int]) -> list[int] that returns the even
# numbers from nums, using a list comprehension.

# TODO: your code here

# --- Task 3.2 ---------------------------------------------------
# Write word_lengths(words: list[str]) -> dict[str, int] that maps each
# word to its length, using a dict comprehension.

# TODO: your code here

# --- Task 3.3 ---------------------------------------------------
# Write unique_sorted(nums: list[int]) -> list[int] that dedupes nums
# via set() and returns a sorted list.

# TODO: your code here

# --- Task 3.4 ---------------------------------------------------
# Write safe_get(d: dict[str, int], key: str) -> int | None using
# dict.get()
#
# WHY: mirrors Go's comma-ok idiom (`v, ok := m[key]`) — `dict.get(key,
# default)` (default None here) is Python's one-step check-and-fetch,
# no separate "ok" boolean needed.

# TODO: your code here

# --- Task 3.5 ---------------------------------------------------
# Write append_to_all(lists: list[list[int]], value: int) -> None that
# mutates EACH inner list in place by appending value. Returns None on
# purpose — the point is the side effect.
#
# WHY: Python lists are mutable objects accessed by reference —
# mutating a list inside a function is visible to the caller, exactly
# like Go's slice-sharing trap.

# TODO: your code here
