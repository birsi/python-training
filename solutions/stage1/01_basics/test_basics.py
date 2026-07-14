# ============================================================
# Tests — do not modify this file.
# When `pytest` passes, the exercise is solved.
# ============================================================
import basics


def test_greet_ada() -> None:
    assert basics.greet("Ada") == "Hello, Ada!"


def test_greet_pythonista() -> None:
    assert basics.greet("Pythonista") == "Hello, Pythonista!"


def test_max_retries_constant() -> None:
    assert basics.MAX_RETRIES == 3


def test_zero_values() -> None:
    assert basics.zero_values() == (0, "", False)


def test_average() -> None:
    assert basics.average(1, 2) == 0.5
    assert basics.average(4, 2) == 2.0
    assert basics.average(7, 2) == 3.5


def test_floor_divide() -> None:
    assert basics.floor_divide(7, 2) == 3
    assert basics.floor_divide(-7, 2) == -4
    assert basics.floor_divide(8, 4) == 2
