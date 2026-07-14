# ============================================================
# Stage 3 — Exercise 11: Asyncio
# ============================================================
#
# GOAL: asyncio.Queue as a channel, asyncio.gather for fan-in, and
# asyncio.wait_for for timeouts.
#
# Rules:
#   - Don't modify test_pipeline.py — it's the test suite.
#   - Check: pytest exercises/stage3/11_asyncio/
#     (functions fail with AttributeError until every task is done —
#     that's your to-do list)
#
# When you're done, ask Claude to review this exercise.
# ============================================================

# --- Task 11.1 ---------------------------------------------------
# Write async def producer(queue: "asyncio.Queue[int | None]", items: list[int]) -> None:
# that does await queue.put(item) for each item in items, then
# await queue.put(None) as a sentinel signaling completion.
#
# WHY: mirrors Go's channel close() — asyncio.Queue has no built-in
# "closed" state, so a sentinel value is the idiomatic way to signal
# "no more items."

# TODO: your code here

# --- Task 11.2 ---------------------------------------------------
# Write async def consumer(queue: "asyncio.Queue[int | None]") -> list[int]:
# that loops: item = await queue.get(); if item is None, stop; else
# append it to a results list. Return the results.
#
# WHY: mirrors Go's for v := range ch, looping until the channel is
# closed.

# TODO: your code here

# --- Task 11.3 ---------------------------------------------------
# Write async def fetch(item_id: int) -> str: that does
# await asyncio.sleep(0.03) then returns f"result-{item_id}". Then
# write async def fetch_all(ids: list[int]) -> list[str]: using
# asyncio.gather to run all fetch() calls concurrently, returning
# results in the SAME order as ids.
#
# WHY: mirrors Go's fan-in pattern collecting goroutine results —
# asyncio.gather runs every coroutine concurrently and returns results
# in the same order as the input, regardless of completion order.

# TODO: your code here

# --- Task 11.4 ---------------------------------------------------
# Write async def fetch_with_timeout(item_id: int, timeout: float) -> str | None:
# that tries to return await asyncio.wait_for(fetch(item_id), timeout)
# and returns None if it times out (note: since Python 3.11,
# asyncio.TimeoutError is an alias for the builtin TimeoutError, so
# catching TimeoutError is correct and preferred).
#
# WHY: mirrors Go's select with a timeout case (case <-time.After(...))
# — asyncio.wait_for races a coroutine against a deadline.

# TODO: your code here
