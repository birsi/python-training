# ============================================================
# Stage 1 — Exercise 1: Basics
# ============================================================
#
# GOAL: Type-hinted variables, f-strings, the constant convention, no
# automatic zero values, and true vs floor division.
#
# Rules:
#   - Don't modify test_basics.py — it's the test suite.
#   - Check: pytest exercises/stage1/01_basics/
#     (functions fail with AttributeError until every task is done —
#     that's your to-do list)
#
# When you're done, ask Claude to review this exercise.
# ============================================================

# --- Task 1.1 ---------------------------------------------------
# Write greet(name: str) -> str that returns f"Hello, {name}!"
#
# WHY: Python's f-strings embed expressions directly in a string literal
# with {expr} — the closest equivalent to Go's fmt.Sprintf, but built
# into the language's string syntax itself.

# TODO: your code here

# --- Task 1.2 ---------------------------------------------------
# Declare a module-level "constant" MAX_RETRIES: int = 3
#
# WHY: Python has no `const` keyword. By convention, ALL_CAPS names are
# treated as constants — nothing stops mutation at runtime, it's
# discipline, not enforcement.

# TODO: your code here

# --- Task 1.3 ---------------------------------------------------
# Write zero_values() -> tuple[int, str, bool] that returns (0, "", False)
#
# WHY: unlike Go, Python variables have no automatic zero value.
# `var count int` in Go is already usable as 0; in Python, `count: int`
# alone (just an annotation, no assignment) leaves the name unbound —
# referencing it raises NameError. Every value must be explicitly assigned.

# TODO: your code here

# --- Task 1.4 ---------------------------------------------------
# Write average(a: int, b: int) -> float using / (true division)
#
# WHY: unlike Go, dividing two ints with / in Python 3 already produces
# a float — no manual float(x) conversion needed before dividing.

# TODO: your code here

# --- Task 1.5 ---------------------------------------------------
# Write floor_divide(a: int, b: int) -> int using // (floor division)
#
# WHY: // floors toward negative infinity — this differs from Go's
# truncation toward zero for negative operands: -7 // 2 == -4 in
# Python, but -7/2 truncates to -3 in Go.

# TODO: your code here
