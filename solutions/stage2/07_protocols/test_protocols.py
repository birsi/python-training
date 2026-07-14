# ============================================================
# Tests — do not modify this file.
# When `pytest` passes, the exercise is solved.
# ============================================================
import math

import protocols


def test_circle_and_square_satisfy_shape() -> None:
    c: protocols.Shape = protocols.Circle(2)
    s: protocols.Shape = protocols.Square(3)
    assert round(c.area(), 2) == 12.57
    assert s.area() == 9


def test_total_area() -> None:
    total = protocols.total_area([protocols.Circle(1), protocols.Square(2)])
    assert abs(total - (math.pi + 4)) < 1e-9


def test_str_representations() -> None:
    assert str(protocols.Circle(2)) == "Circle(radius=2)"
    assert str(protocols.Square(3)) == "Square(side=3)"


def test_describe() -> None:
    assert protocols.describe(protocols.Circle(1)) == "Circle(radius=1)"


def test_describe_value() -> None:
    assert protocols.describe_value(True) == "a boolean"
    assert protocols.describe_value(5) == "an integer"
    assert protocols.describe_value("hi") == "a string"
    assert protocols.describe_value([1, 2]) == "a list"
    assert protocols.describe_value(3.14) == "something else"
