# ============================================================
# Stage 2 — Exercise 6: Dataclasses
# ============================================================
#
# GOAL: @dataclass, frozen=True, @property, and mutating methods on a
# dataclass.
#
# Rules:
#   - Don't modify test_models.py — it's the test suite.
#   - Check: pytest exercises/stage2/06_dataclasses/
#     (functions fail with AttributeError until every task is done —
#     that's your to-do list)
#
# When you're done, ask Claude to review this exercise.
# ============================================================

# --- Task 6.1 ---------------------------------------------------
# Write @dataclass class Point with fields x: float and y: float —
# nothing else, just the auto-generated __init__/__repr__/__eq__.
#
# WHY: @dataclass generates __init__, __repr__, and __eq__ for you from
# the field list alone — the closest thing Python has to Go's plain
# struct with automatic field-wise equality.

# TODO: your code here

# --- Task 6.2 ---------------------------------------------------
# Write @dataclass(frozen=True) class ImmutablePoint with fields
# x: float and y: float.
#
# WHY: closest Python equivalent to Go's value semantics — a frozen
# dataclass can't be mutated in place; "changing" one means constructing
# a new one (e.g. via dataclasses.replace()).

# TODO: your code here

# --- Task 6.3 ---------------------------------------------------
# Write @dataclass class Vector with fields x: float and y: float, plus
# @property def magnitude(self) -> float: computing
# math.sqrt(self.x**2 + self.y**2)
#
# WHY: @property lets you add a read-only COMPUTED attribute to a
# dataclass that looks like plain attribute access from the caller's
# side (v.magnitude, no parens) — mirrors a Go value-receiver method
# that only reads the struct.

# TODO: your code here

# --- Task 6.4 ---------------------------------------------------
# Write @dataclass class BankAccount with field balance: float = 0.0,
# plus methods deposit(self, amount: float) -> None (self.balance +=
# amount) and withdraw(self, amount: float) -> None (raise ValueError if
# amount > self.balance, else subtract).
#
# WHY: contrast with Task 6.2 — this dataclass is NOT frozen, so its
# methods mutate self directly: the ergonomic-Python equivalent of Go's
# pointer-receiver methods.

# TODO: your code here
