# ============================================================
# Tests — do not modify this file.
# When `pytest` passes, the exercise is solved.
# ============================================================
import mutability


def test_is_same_object_same_reference() -> None:
    x = [1, 2]
    assert mutability.is_same_object(x, x) is True


def test_is_same_object_equal_but_distinct() -> None:
    assert mutability.is_same_object([1, 2], [1, 2]) is False


def test_add_item_no_shared_default_bucket() -> None:
    b1 = mutability.add_item("a")
    b2 = mutability.add_item("b")
    assert b1 == ["a"]
    assert b2 == ["b"]  # would be ["a", "b"] if the mutable-default trap were present


def test_add_item_with_explicit_bucket() -> None:
    assert mutability.add_item("x", ["existing"]) == ["existing", "x"]


def test_deep_copy_matrix_does_not_share_inner_lists() -> None:
    original = [[1, 2], [3, 4]]
    copied = mutability.deep_copy_matrix(original)
    copied[0][0] = 99
    assert original[0][0] == 1
    assert copied == [[99, 2], [3, 4]]


def test_increment_in_place_and_increment_value() -> None:
    d = {"a": 1}
    mutability.increment_in_place(d, "a")
    assert d == {"a": 2}
    mutability.increment_in_place(d, "b")
    assert d == {"a": 2, "b": 1}

    assert mutability.increment_value(5) == 6
    n = 5
    mutability.increment_value(n)
    assert n == 5  # unchanged — ints are immutable, can't mutate the caller's variable
