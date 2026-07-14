# ============================================================
# Stage 3 — Exercise 10: Threading
# ============================================================
#
# GOAL: Starting threads, waiting for all of them, and protecting shared
# state with a Lock.
#
# Rules:
#   - Don't modify test_workers.py — it's the test suite.
#   - Check: pytest exercises/stage3/10_threading/
#     (functions fail with AttributeError until every task is done —
#     that's your to-do list)
#
# When you're done, ask Claude to review this exercise.
# ============================================================

# --- Task 10.1 ---------------------------------------------------
# Write def run_all(*fns: Callable[[], None]) -> None: that starts each
# function in its OWN threading.Thread, then joins all of them before
# returning.
#
# WHY: Thread.start() returns immediately — without joining, run_all
# would return before any work happened. The test measures that.

# TODO: your code here

# --- Task 10.2 ---------------------------------------------------
# Write class SafeCounter: with __init__(self) -> None setting
# self._lock = threading.Lock() and self._value = 0; increment(self) -> None
# (with self._lock: self._value += 1); value(self) -> int
# (with self._lock: return self._value).
#
# WHY: self._value += 1 is a read-modify-write — two threads doing it
# "simultaneously" can interleave and lose updates. Python has no -race
# flag like Go, so correctness under enough concurrent load is the
# signal: this test uses enough threads and iterations that missing the
# lock reliably produces a wrong final count on CPython, even with the
# GIL.

# TODO: your code here

# --- Task 10.3 ---------------------------------------------------
# Write def square_all(nums: list[int]) -> list[int]: that computes each
# square in its OWN thread, writing to result[i], then joins and returns
# result.
#
# WHY no lock needed here: each thread writes a DIFFERENT index —
# disjoint memory, no shared variable, no lock required. Knowing when
# you don't need a lock matters as much as knowing when you do.

# TODO: your code here
