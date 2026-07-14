# ============================================================
# Stage 3 — Exercise 11: Asyncio — REFERENCE SOLUTION
# ============================================================

import asyncio

# --- Task 11.1 — producer ---


async def producer(queue: "asyncio.Queue[int | None]", items: list[int]) -> None:
    for item in items:
        await queue.put(item)
    await queue.put(None)


# --- Task 11.2 — consumer ---


async def consumer(queue: "asyncio.Queue[int | None]") -> list[int]:
    results: list[int] = []
    while True:
        item = await queue.get()
        if item is None:
            break
        results.append(item)
    return results


# --- Task 11.3 — fetch and fetch_all ---


async def fetch(item_id: int) -> str:
    await asyncio.sleep(0.03)
    return f"result-{item_id}"


async def fetch_all(ids: list[int]) -> list[str]:
    return await asyncio.gather(*(fetch(item_id) for item_id in ids))


# --- Task 11.4 — fetch_with_timeout ---


async def fetch_with_timeout(item_id: int, timeout: float) -> str | None:
    try:
        return await asyncio.wait_for(fetch(item_id), timeout)
    except TimeoutError:
        return None
