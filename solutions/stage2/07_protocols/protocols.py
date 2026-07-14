# ============================================================
# Stage 2 — Exercise 7: Protocols — REFERENCE SOLUTION
# ============================================================

import math
from dataclasses import dataclass
from typing import Protocol

# --- Task 7.1 — structural typing with Protocol ---


class Shape(Protocol):
    def area(self) -> float: ...


@dataclass
class Circle:
    radius: float

    def area(self) -> float:
        return math.pi * self.radius**2

    # --- Task 7.3 — __str__ ---

    def __str__(self) -> str:
        return f"Circle(radius={self.radius})"


@dataclass
class Square:
    side: float

    def area(self) -> float:
        return self.side**2

    # --- Task 7.3 — __str__ ---

    def __str__(self) -> str:
        return f"Square(side={self.side})"


# --- Task 7.2 — total_area ---


def total_area(shapes: list[Shape]) -> float:
    return sum(shape.area() for shape in shapes)


# --- Task 7.3 — describe ---


def describe(shape: Shape) -> str:
    return str(shape)


# --- Task 7.4 — isinstance narrowing ---


def describe_value(value: object) -> str:
    if isinstance(value, bool):
        return "a boolean"
    if isinstance(value, int):
        return "an integer"
    if isinstance(value, str):
        return "a string"
    if isinstance(value, list):
        return "a list"
    return "something else"
