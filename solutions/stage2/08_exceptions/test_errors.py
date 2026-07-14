# ============================================================
# Tests — do not modify this file.
# When `pytest` passes, the exercise is solved.
# ============================================================
import errors
import pytest


def test_divide() -> None:
    assert errors.divide(6, 2) == 3.0
    with pytest.raises(ValueError, match="division by zero"):
        errors.divide(1, 0)


def test_validation_error() -> None:
    e = errors.ValidationError("age", "must not be negative")
    assert str(e) == "age: must not be negative"
    assert e.field == "age"
    assert e.reason == "must not be negative"
    assert isinstance(e, Exception)


def test_check_age_valid() -> None:
    errors.check_age(30)  # should not raise


def test_check_age_negative() -> None:
    with pytest.raises(errors.ValidationError) as exc_info:
        errors.check_age(-1)
    assert exc_info.value.reason == "must not be negative"


def test_check_age_too_large() -> None:
    with pytest.raises(errors.ValidationError) as exc_info:
        errors.check_age(200)
    assert exc_info.value.reason == "unrealistically large"


def test_find() -> None:
    assert errors.find({"a": "1"}, "a") == "1"
    with pytest.raises(LookupError) as exc_info:
        errors.find({}, "missing")
    assert isinstance(exc_info.value.__cause__, KeyError)


def test_retry_succeeds_eventually() -> None:
    calls = {"n": 0}

    def flaky() -> None:
        calls["n"] += 1
        if calls["n"] < 3:
            raise RuntimeError("not yet")

    errors.retry(5, flaky)
    assert calls["n"] == 3


def test_retry_reraises_last_exception() -> None:
    def always_fails() -> None:
        raise RuntimeError("nope")

    with pytest.raises(RuntimeError, match="nope"):
        errors.retry(3, always_fails)
