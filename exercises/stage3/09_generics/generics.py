# ============================================================
# Stage 3 — Exercise 9: Generics
# ============================================================
#
# GOAL: PEP 695 generic functions and classes, and bounded type parameters.
#
# Rules:
#   - Don't modify test_generics.py — it's the test suite.
#   - Check: pytest exercises/stage3/09_generics/
#     (functions fail with AttributeError until every task is done —
#     that's your to-do list)
#
# When you're done, ask Claude to review this exercise.
# ============================================================

# --- Task 9.1 ---------------------------------------------------
# Write def first[T](items: list[T]) -> T: returning items[0].
#
# WHY: Python 3.12 introduced native generic syntax — def first[T](...)
# closely resembles Go's func First[T any](...).

# TODO: your code here

# --- Task 9.2 ---------------------------------------------------
# Write class Stack[T]: with __init__(self) -> None (an empty internal
# list), push(self, item: T) -> None, pop(self) -> T (remove and return
# the last item — let IndexError propagate naturally if empty, no need
# to catch it), peek(self) -> T (return the last item without removing
# it), and is_empty(self) -> bool.
#
# WHY: a generic class parameterized over the element type it holds,
# just like Go's type Stack[T any] struct { items []T }.

# TODO: your code here

# --- Task 9.3 ---------------------------------------------------
# Write def max_of[T: (int, float)](items: list[T]) -> T: returning the
# largest item (a constrained type parameter — T may only be int or
# float, using PEP 695's constraint syntax).
#
# WHY: mirrors Go's cmp.Ordered constraint — PEP 695 lets you constrain
# T to a fixed set of types directly in the [...] clause, right where
# the type parameter is introduced.

# TODO: your code here

# --- Task 9.4 ---------------------------------------------------
# Write def map_option[T, U](value: T | None, fn: Callable[[T], U]) -> U | None:
# — if value is None return None, else return fn(value).
#
# WHY: a capstone tying Optionals + generics together — two independent
# type parameters (T in, U out) flowing through one function, similar
# to Go generics tutorials' "map over a container" pattern.

# TODO: your code here
