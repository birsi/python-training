# ============================================================
# Tests — do not modify this file.
# When `pytest` passes, the exercise is solved.
# ============================================================
import dataclasses

import models
import pytest


def test_point_equality() -> None:
    assert models.Point(1, 2) == models.Point(1, 2)
    assert models.Point(1, 2) != models.Point(1, 3)
    assert dataclasses.is_dataclass(models.Point) is True


def test_immutable_point_frozen() -> None:
    p = models.ImmutablePoint(1, 2)
    with pytest.raises(dataclasses.FrozenInstanceError):
        p.x = 5  # type: ignore[misc]


def test_vector_magnitude() -> None:
    assert models.Vector(3, 4).magnitude == 5.0


def test_bank_account_deposit_and_withdraw() -> None:
    acc = models.BankAccount(100.0)
    acc.deposit(50)
    assert acc.balance == 150.0
    acc.withdraw(30)
    assert acc.balance == 120.0
    with pytest.raises(ValueError):
        acc.withdraw(1000)
