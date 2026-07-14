# ============================================================
# Stage 2 — Exercise 8: Exceptions
# ============================================================
#
# GOAL: Raising exceptions, custom exception types, exception chaining,
# and a retry helper.
#
# Rules:
#   - Don't modify test_errors.py — it's the test suite.
#   - Check: pytest exercises/stage2/08_exceptions/
#     (functions fail with AttributeError until every task is done —
#     that's your to-do list)
#
# When you're done, ask Claude to review this exercise.
# ============================================================

# --- Task 8.1 ---------------------------------------------------
# Write divide(a: float, b: float) -> float — raise
# ValueError("division by zero") if b == 0, else return a / b.
#
# WHY: Python's idiom is EAFP ("easier to ask forgiveness than
# permission") via exceptions, not Go's explicit (value, error) return —
# errors are raised, not returned, and propagate automatically up the
# call stack until caught.

# TODO: your code here

# --- Task 8.2 ---------------------------------------------------
# Write class ValidationError(Exception) with
# __init__(self, field: str, reason: str) -> None storing self.field,
# self.reason, and calling super().__init__(f"{field}: {reason}").
#
# WHY: mirrors Go's custom ValidationError struct implementing the error
# interface via Error() string — Python's equivalent is simply
# subclassing Exception and calling super().__init__(message).

# TODO: your code here

# --- Task 8.3 ---------------------------------------------------
# Write check_age(age: int) -> None — raise
# ValidationError("age", "must not be negative") if age < 0; raise
# ValidationError("age", "unrealistically large") if age > 150;
# otherwise return None.

# TODO: your code here

# --- Task 8.4 ---------------------------------------------------
# Write find(mapping: dict[str, str], key: str) -> str — if key is
# present return the value; else
# raise LookupError(f"key {key!r} not found") from KeyError(key)
#
# WHY: raise ... from ... sets __cause__ explicitly — Python's
# equivalent of Go's %w wrapping + errors.Is/errors.As; a caller can
# inspect exc.__cause__ to get at the original underlying exception
# instead of just a flat error string.

# TODO: your code here

# --- Task 8.5 ---------------------------------------------------
# Write retry(attempts: int, fn: Callable[[], None]) -> None — call
# fn() up to attempts times; return as soon as one call succeeds
# (doesn't raise); if ALL attempts raise, re-raise the LAST exception.

# TODO: your code here
