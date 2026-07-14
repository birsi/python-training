# ============================================================
# Stage 2 — Exercise 5: Classes — REFERENCE SOLUTION
# ============================================================

import math

# --- Task 5.1 — Point and distance_to ---


class Point:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def distance_to(self, other: "Point") -> float:
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    # --- Task 5.2 — __eq__ and __repr__ ---

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Point):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __repr__(self) -> str:
        return f"Point(x={self.x}, y={self.y})"


# --- Task 5.3 — class vs instance attributes ---


class Counter:
    total_created: int = 0

    def __init__(self) -> None:
        self.count = 0
        Counter.total_created += 1

    def bump(self) -> None:
        self.count += 1


# --- Task 5.4 — composition ---


class Address:
    def __init__(self, city: str, zip_code: str) -> None:
        self.city = city
        self.zip_code = zip_code


class Employee:
    def __init__(self, name: str, address: "Address") -> None:
        self.name = name
        self.address = address

    def summary(self) -> str:
        return f"{self.name} ({self.address.city})"
