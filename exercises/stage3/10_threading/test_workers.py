# ============================================================
# Tests — do not modify this file.
# When `pytest` passes, the exercise is solved.
# ============================================================
import threading
import time
from collections.abc import Callable

import workers


def test_run_all_waits_for_every_task() -> None:
    done: list[int] = []
    lock = threading.Lock()

    def make_task(n: int) -> Callable[[], None]:
        def task() -> None:
            time.sleep(0.01)
            with lock:
                done.append(n)

        return task

    workers.run_all(*(make_task(i) for i in range(20)))
    assert len(done) == 20


def test_safe_counter_under_concurrent_load() -> None:
    counter = workers.SafeCounter()
    threads_count = 50
    increments_per_thread = 2000

    def worker() -> None:
        for _ in range(increments_per_thread):
            counter.increment()

    threads = [threading.Thread(target=worker) for _ in range(threads_count)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    assert counter.value() == threads_count * increments_per_thread


def test_square_all() -> None:
    assert workers.square_all([1, 2, 3, 4]) == [1, 4, 9, 16]


def test_square_all_empty() -> None:
    assert workers.square_all([]) == []
