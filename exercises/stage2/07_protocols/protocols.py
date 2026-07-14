# ============================================================
# Stage 2 — Exercise 7: Protocols
# ============================================================
#
# GOAL: typing.Protocol structural typing (Python's implicit
# interfaces), __str__, and isinstance narrowing.
#
# Rules:
#   - Don't modify test_protocols.py — it's the test suite.
#   - Check: pytest exercises/stage2/07_protocols/
#     (functions fail with AttributeError until every task is done —
#     that's your to-do list)
#
# When you're done, ask Claude to review this exercise.
# ============================================================

# --- Task 7.1 ---------------------------------------------------
# Write class Shape(Protocol) with def area(self) -> float: ...
# (a typing.Protocol, imported as `from typing import Protocol`). Then
# write @dataclass class Circle with field radius: float and
# def area(self) -> float: return math.pi * self.radius ** 2. Then write
# @dataclass class Square with field side: float and
# def area(self) -> float: return self.side ** 2. Neither Circle nor
# Square should declare Shape as a base class or use any
# `implements`-like mechanism.
#
# WHY: this is the single most direct Go→Python parallel in the whole
# course — typing.Protocol gives you Go-style implicit interface
# satisfaction via structural typing: Circle and Square satisfy Shape
# just by having a matching area() method, with no inheritance
# declaration, exactly like Go interfaces.

# TODO: your code here

# --- Task 7.2 ---------------------------------------------------
# Write total_area(shapes: list[Shape]) -> float that sums .area() over
# every shape.

# TODO: your code here

# --- Task 7.3 ---------------------------------------------------
# Add __str__(self) -> str to Circle (returns
# f"Circle(radius={self.radius})") and to Square (returns
# f"Square(side={self.side})"). Then write
# describe(shape: Shape) -> str that returns str(shape).
#
# WHY: mirrors Go's fmt.Stringer — implementing __str__ gives your type
# a human-readable representation whenever it's printed or passed to
# str(), just like implementing String() string satisfies fmt.Stringer.

# TODO: your code here

# --- Task 7.4 ---------------------------------------------------
# Write describe_value(value: object) -> str using isinstance checks, in
# this exact order: bool -> "a boolean", int -> "an integer",
# str -> "a string", list -> "a list", else -> "something else".
#
# WHY: mirrors Go's type switch over any. The bool-before-int ordering
# is a Python-specific trap: isinstance(True, int) is True because bool
# is a subclass of int in Python — check order matters, or every bool
# would be reported as an integer.

# TODO: your code here
