# ============================================================
# Tests — do not modify this file.
# When `pytest` passes, the exercise is solved.
# ============================================================
import asyncio
import time

import pipeline


def test_producer_consumer() -> None:
    async def scenario() -> list[int]:
        queue: asyncio.Queue[int | None] = asyncio.Queue()
        await pipeline.producer(queue, [1, 2, 3])
        return await pipeline.consumer(queue)

    assert asyncio.run(scenario()) == [1, 2, 3]


def test_fetch_all_values() -> None:
    assert asyncio.run(pipeline.fetch_all([1, 2, 3])) == ["result-1", "result-2", "result-3"]


def test_fetch_all_is_concurrent() -> None:
    start = time.monotonic()
    asyncio.run(pipeline.fetch_all([1, 2, 3, 4, 5]))
    elapsed = time.monotonic() - start
    # sequential would take ~5 * 0.03s = 0.15s; concurrent should be close to one sleep.
    assert elapsed < 0.12


def test_fetch_with_timeout_succeeds() -> None:
    assert asyncio.run(pipeline.fetch_with_timeout(1, timeout=1.0)) == "result-1"


def test_fetch_with_timeout_expires() -> None:
    assert asyncio.run(pipeline.fetch_with_timeout(1, timeout=0.001)) is None
