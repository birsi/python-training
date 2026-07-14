# ============================================================
# Stage 2 — Exercise 5: Classes
# ============================================================
#
# GOAL: Class basics: __init__, dunder methods, class vs instance
# attributes, and composition.
#
# Rules:
#   - Don't modify test_classes.py — it's the test suite.
#   - Check: pytest exercises/stage2/05_classes/
#     (functions fail with AttributeError until every task is done —
#     that's your to-do list)
#
# When you're done, ask Claude to review this exercise.
# ============================================================

# --- Task 5.1 ---------------------------------------------------
# Write class Point with __init__(self, x: float, y: float) -> None
# storing self.x and self.y, and a method
# distance_to(self, other: "Point") -> float returning the Euclidean
# distance between self and other.
#
# WHY: instance attributes are assigned to self inside __init__ —
# there's no automatic field list like a Go struct's declaration;
# whatever you assign to self is the object's state.

# TODO: your code here

# --- Task 5.2 ---------------------------------------------------
# Add __eq__(self, other: object) -> bool to Point, comparing x and y
# (return NotImplemented if other isn't a Point), and
# __repr__(self) -> str returning exactly f"Point(x={self.x}, y={self.y})"
#
# WHY: Python gives you no free structural equality or printing for
# custom classes — two Point(1, 2) instances are NOT == unless you
# implement __eq__ yourself, unlike Go where == on comparable structs
# compares fields automatically. __repr__ similarly must be written by
# hand for a useful representation.

# TODO: your code here

# --- Task 5.3 ---------------------------------------------------
# Write class Counter with a CLASS variable total_created: int = 0
# (incremented in __init__, shared across every instance), an INSTANCE
# variable count (starts at 0 per instance, set in __init__), and a
# method bump(self) -> None that does self.count += 1.
#
# WHY: total_created lives on the class and is shared by every instance
# (useful for tallying "how many Counters exist"); count is set on self
# in __init__ so each instance gets its own independent copy. Mixing
# these up — e.g. giving a class attribute a MUTABLE default like a
# list — is a classic trap since all instances would then silently
# share the same object.

# TODO: your code here

# --- Task 5.4 ---------------------------------------------------
# Write class Address with __init__(self, city: str, zip_code: str) -> None
# storing self.city and self.zip_code. Write class Employee with
# __init__(self, name: str, address: "Address") -> None storing self.name
# and self.address, and a method summary(self) -> str returning
# f"{self.name} ({self.address.city})"
#
# WHY: Python (like Go) favors composition over inheritance for "has-a"
# relationships — Employee doesn't inherit from Address, it just holds one.

# TODO: your code here
