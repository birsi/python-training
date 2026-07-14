# ============================================================
# Tests — do not modify this file.
# When `pytest` passes, the exercise is solved.
# ============================================================
import generics


def test_first_ints() -> None:
    assert generics.first([1, 2, 3]) == 1


def test_first_strs() -> None:
    assert generics.first(["a", "b"]) == "a"


def test_stack() -> None:
    s: generics.Stack[int] = generics.Stack()
    assert s.is_empty() is True
    s.push(1)
    s.push(2)
    assert s.peek() == 2
    assert s.pop() == 2
    assert s.pop() == 1
    assert s.is_empty() is True


def test_max_of_ints() -> None:
    assert generics.max_of([3, 1, 4, 1, 5]) == 5


def test_max_of_floats() -> None:
    assert generics.max_of([1.5, 2.5, 0.5]) == 2.5


def test_map_option_present() -> None:
    assert generics.map_option(4, lambda n: n * 2) == 8


def test_map_option_none() -> None:
    assert generics.map_option(None, lambda n: n * 2) is None


def test_map_option_different_types() -> None:
    assert generics.map_option("hi", len) == 2
