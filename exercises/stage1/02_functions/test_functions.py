# ============================================================
# Tests — do not modify this file.
# When `pytest` passes, the exercise is solved.
# ============================================================
import functions


def test_greet_default_greeting() -> None:
    assert functions.greet("Ada") == "Hello, Ada!"


def test_greet_custom_greeting() -> None:
    assert functions.greet("Ada", "Hi") == "Hi, Ada!"


def test_sum_all_no_args() -> None:
    assert functions.sum_all() == 0


def test_sum_all_multiple_args() -> None:
    assert functions.sum_all(1, 2, 3) == 6


def test_sum_all_single_arg() -> None:
    assert functions.sum_all(5) == 5


def test_build_profile() -> None:
    assert functions.build_profile(name="Ada", role="engineer") == {
        "name": "Ada",
        "role": "engineer",
    }


def test_build_profile_empty() -> None:
    assert functions.build_profile() == {}


def test_make_counter_increments() -> None:
    c = functions.make_counter()
    assert c() == 1
    assert c() == 2
    assert c() == 3


def test_make_counter_independent_instances() -> None:
    c = functions.make_counter()
    assert c() == 1
    c2 = functions.make_counter()
    assert c2() == 1


def test_apply_twice_increment() -> None:
    assert functions.apply_twice(lambda n: n + 1, 5) == 7


def test_apply_twice_double() -> None:
    assert functions.apply_twice(lambda n: n * 2, 3) == 12
