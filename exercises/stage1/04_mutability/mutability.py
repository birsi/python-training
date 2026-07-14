# ============================================================
# Stage 1 — Exercise 4: Mutability
# ============================================================
#
# GOAL: Identity vs equality, the mutable-default-argument footgun,
# shallow vs deep copy, and mutable-vs-immutable pass semantics —
# Python's replacement for pointers.
#
# Rules:
#   - Don't modify test_mutability.py — it's the test suite.
#   - Check: pytest exercises/stage1/04_mutability/
#     (functions fail with AttributeError until every task is done —
#     that's your to-do list)
#
# When you're done, ask Claude to review this exercise.
# ============================================================

# --- Task 4.1 ---------------------------------------------------
# Write is_same_object(a: object, b: object) -> bool that returns
# a is b
#
# WHY: `is` checks identity (same object in memory — the closest Python
# gets to comparing Go pointers); `==` checks value equality. Two
# equal-looking lists are almost never the same object.

# TODO: your code here

# --- Task 4.2 ---------------------------------------------------
# Write add_item(item: str, bucket: list[str] | None = None) ->
# list[str]. You MUST use a None sentinel default, then
# `if bucket is None: bucket = []`, then append item and return bucket.
#
# WHY: mutable default arguments are evaluated ONCE at
# function-definition time and shared across every call that doesn't
# pass one explicitly — a classic Python footgun.
# `bucket: list[str] = []` as a literal default would silently leak
# state between unrelated calls.

# TODO: your code here

# --- Task 4.3 ---------------------------------------------------
# Write deep_copy_matrix(matrix: list[list[int]]) -> list[list[int]]
# that returns a copy where the inner lists are NOT shared with the
# original (use copy.deepcopy or a nested comprehension).
#
# WHY: a shallow copy (list(matrix) or matrix[:]) copies the outer list
# but the inner lists are still the SAME objects — mutating a copied
# row would mutate the original too. Mirrors Go's lesson that copying a
# struct containing a slice still shares the underlying array.

# TODO: your code here

# --- Task 4.4 ---------------------------------------------------
# Write increment_in_place(counter: dict[str, int], key: str) -> None
# that mutates the dict in place (adds 1, or sets to 1 if the key is
# missing). AND write increment_value(n: int) -> int that returns
# n + 1 (it cannot mutate the caller's int at all).
#
# WHY: Python doesn't have Go's explicit pointer-vs-value receiver
# choice — everything is "pass object reference," but whether a
# function's mutation is visible to the caller depends on whether the
# TYPE is mutable (list, dict, set) or immutable (int, str, tuple).
# increment_in_place can mutate because dicts are mutable;
# increment_value MUST return a new int because ints can't be mutated
# at all.

# TODO: your code here
