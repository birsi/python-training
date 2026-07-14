# ============================================================
# Stage 2 — Exercise 6: Dataclasses — REFERENCE SOLUTION
# ============================================================

import math
from dataclasses import dataclass

# --- Task 6.1 — plain dataclass ---


@dataclass
class Point:
    x: float
    y: float


# --- Task 6.2 — frozen dataclass ---


@dataclass(frozen=True)
class ImmutablePoint:
    x: float
    y: float


# --- Task 6.3 — computed property ---


@dataclass
class Vector:
    x: float
    y: float

    @property
    def magnitude(self) -> float:
        return math.sqrt(self.x**2 + self.y**2)


# --- Task 6.4 — mutating methods ---


@dataclass
class BankAccount:
    balance: float = 0.0

    def deposit(self, amount: float) -> None:
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        if amount > self.balance:
            raise ValueError("insufficient funds")
        self.balance -= amount
