# ============================================================
# Stage 1 — Exercise 2: Functions
# ============================================================
#
# GOAL: Default parameters, *args/**kwargs, closures, and functions as
# values.
#
# Rules:
#   - Don't modify test_functions.py — it's the test suite.
#   - Check: pytest exercises/stage1/02_functions/
#     (functions fail with AttributeError until every task is done —
#     that's your to-do list)
#
# When you're done, ask Claude to review this exercise.
# ============================================================

# --- Task 2.1 ---------------------------------------------------
# Write greet(name: str, greeting: str = "Hello") -> str that returns
# f"{greeting}, {name}!"
#
# WHY: Python has native default parameter values — no need for Go's
# "check if zero-value, substitute a default" trick.

# TODO: your code here

# --- Task 2.2 ---------------------------------------------------
# Write sum_all(*args: int) -> int that sums all positional args
# (0 if none are given)
#
# WHY: Go's variadic parameters use `...int`; Python's is `*args`, and
# callers can also unpack an existing sequence into it with `*my_list`.

# TODO: your code here

# --- Task 2.3 ---------------------------------------------------
# Write build_profile(**kwargs: str) -> dict[str, str] that returns the
# keyword arguments as a plain dict
#
# WHY: **kwargs gathers arbitrary keyword arguments into a dict — Go has
# no equivalent; the closest you'd get there is passing a whole struct
# or map.

# TODO: your code here

# --- Task 2.4 ---------------------------------------------------
# Write make_counter() -> Callable[[], int] that returns a zero-arg
# closure; each call increments an internal counter (starting at 0)
# and returns the new value. You'll need `nonlocal`.
#
# WHY: closures need the `nonlocal` keyword to REBIND a variable in the
# enclosing scope (merely READING it works without `nonlocal`) —
# contrast with Go, where closures capture by reference implicitly with
# no keyword needed.

# TODO: your code here

# --- Task 2.5 ---------------------------------------------------
# Write apply_twice(f: Callable[[int], int], x: int) -> int that
# returns f(f(x))
#
# WHY: functions as first-class values / higher-order functions — same
# idea as Go passing a `func(int) int` as an argument.

# TODO: your code here
