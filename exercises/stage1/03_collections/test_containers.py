# ============================================================
# Tests — do not modify this file.
# When `pytest` passes, the exercise is solved.
# ============================================================
import containers


def test_evens_mixed() -> None:
    assert containers.evens([1, 2, 3, 4, 5, 6]) == [2, 4, 6]


def test_evens_empty() -> None:
    assert containers.evens([]) == []


def test_evens_none_even() -> None:
    assert containers.evens([1, 3, 5]) == []


def test_word_lengths() -> None:
    assert containers.word_lengths(["a", "bb", "ccc"]) == {"a": 1, "bb": 2, "ccc": 3}


def test_word_lengths_empty() -> None:
    assert containers.word_lengths([]) == {}


def test_unique_sorted() -> None:
    assert containers.unique_sorted([3, 1, 2, 3, 1]) == [1, 2, 3]


def test_unique_sorted_empty() -> None:
    assert containers.unique_sorted([]) == []


def test_safe_get_present() -> None:
    assert containers.safe_get({"a": 1}, "a") == 1


def test_safe_get_missing() -> None:
    assert containers.safe_get({"a": 1}, "b") is None


def test_append_to_all_mutates_in_place() -> None:
    data = [[1, 2], [3], []]
    containers.append_to_all(data, 9)
    assert data == [[1, 2, 9], [3, 9], [9]]
