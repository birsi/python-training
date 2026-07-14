<div align="center">

# 🎓 Python Training

**Hands-on Python exercises that check themselves with `pytest`** —
designed to be worked through with [Claude Code](https://claude.com/claude-code) acting as your personal tutor and reviewer.

[![Python](https://img.shields.io/badge/Python-3.12%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Exercises](https://img.shields.io/badge/Exercises-12-blueviolet)](#-curriculum)
[![Tutor](https://img.shields.io/badge/Tutor-Claude%20Code-D97757?logo=claude&logoColor=white)](https://claude.com/claude-code)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)

*Every exercise ships with a locked test file.*
*When `pytest` passes, you've solved it.* ✅

</div>

---

## ⚙️ How it works

1. 📝 Each directory in `exercises/` is a self-contained lesson with tasks marked `# TODO: your code here` in the main `.py` file.
2. 🔴 A fresh exercise **fails at test time** — `AttributeError: module 'basics' has no attribute 'greet'` literally names what you still need to build.
3. 🟢 You write code, re-run the test, and work from missing-attribute errors to failing assertions to green.
4. 🤖 Claude reviews your work: not just "do the tests pass", but whether it's idiomatic Python.

```bash
# check a single exercise (do this constantly while working)
pytest exercises/stage1/01_basics/

# run everything (only clean once ALL exercises are solved)
pytest exercises/
```

> [!NOTE]
> The `test_*.py` file in each exercise is the spec — **don't modify it**.
> Unlike Go or TypeScript, Python has no compiler to pin function signatures ahead of time —
> that's what `mypy --strict` is for (see [Ground rules](#-ground-rules)). A fresh exercise file
> has no stub at all, just the `# TODO` comment, so tests fail one at a time with a clear
> `AttributeError` naming exactly what's missing.

## 🚀 Setup

Requires [Python](https://www.python.org/downloads/) 3.12+.

```bash
git clone <this-repo>
cd python-training
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements-dev.txt
pytest solutions/   # sanity check: everything green
```

## 🤖 Training with Claude Code

This repo ships with a [`CLAUDE.md`](./CLAUDE.md) that turns Claude Code into a Python tutor. Start a session in the repo root:

```bash
claude
```

Then drive the training conversationally:

| 💬 You say | 🤖 Claude does |
|---|---|
| *"Where should I start?" / "What's next?"* | Checks your progress across all exercises and points you at the right one |
| *"Explain task 8.2, I don't get it"* | Teaches the concept with **fresh** examples — without handing you the answer |
| *"I'm stuck on task 11.3"* | Gives escalating hints, smallest first |
| *"Review exercise 6"* | Runs the tests (+ `mypy --strict`, `ruff`), reads your code, gives feedback |
| *"Show me the solution for task 9.4"* | Only then reveals the reference solution |

Claude is instructed to **never solve exercises for you** unless you explicitly ask.

You can of course also train without Claude — solve the TODOs, run the tests, and compare against `solutions/` yourself.

## 📚 Curriculum

The three stages mirror how Python proficiency develops for someone who already thinks in a statically-typed language: first the **mechanics** (values, functions, collections — and where Python quietly diverges from Go/TS), then Python's **way of modeling** (classes, dataclasses, structural typing, exceptions), then its **power features** (generics, concurrency, boundaries).

Each exercise comes with **official reading** — read it up front or in parallel, then let the tests check your understanding. All links go to [docs.python.org](https://docs.python.org/3/) (the CPython project's own documentation) or [peps.python.org](https://peps.python.org/) for the handful of features defined by a PEP rather than a docs page. Before Stage 1, skim the [Python Tutorial](https://docs.python.org/3/tutorial/) once — everything below builds on it.

### 🌱 Stage 1 — Foundations: values, functions, and Python's data structures

The mechanics you need for everything else — including the traps that bite people coming from a language with a compiler and real pointers: Python has no zero values, mutable default arguments are shared across calls, and "pass by reference vs. value" is really "mutable vs. immutable type."

| Exercise | Topics | 📖 Official reading |
|---|---|---|
| [01_basics](exercises/stage1/01_basics/) | Type-hinted variables, f-strings, the `UPPER_CASE` constant convention, no automatic zero values, `/` vs `//` division | Tutorial: [An Informal Introduction to Python](https://docs.python.org/3/tutorial/introduction.html) · Language Reference: [Assignment statements](https://docs.python.org/3/reference/simple_stmts.html#assignment-statements) |
| [02_functions](exercises/stage1/02_functions/) | Default parameters, `*args`/`**kwargs`, closures (`nonlocal`), functions as values | Tutorial: [More Control Flow Tools — defining functions](https://docs.python.org/3/tutorial/controlflow.html#more-on-defining-functions) |
| [03_collections](exercises/stage1/03_collections/) | List/dict/set comprehensions, `dict.get` as the comma-ok idiom, the list-sharing mutation trap | Tutorial: [Data Structures](https://docs.python.org/3/tutorial/datastructures.html) · Library: [`dict`](https://docs.python.org/3/library/stdtypes.html#dict) |
| [04_mutability](exercises/stage1/04_mutability/) | `is` vs `==`, the mutable-default-argument footgun, shallow vs. deep copy, mutable vs. immutable pass semantics | Library: [`copy` — shallow and deep copy](https://docs.python.org/3/library/copy.html) · Glossary: [mutable](https://docs.python.org/3/glossary.html#term-mutable) · [Programming FAQ](https://docs.python.org/3/faq/programming.html) (search "changing list") |

### 🧩 Stage 2 — Modeling: classes, dataclasses, and errors as exceptions

How Python structures programs without Go's implicit-everything-by-value structs or TS's nominal `implements`. Plain classes first, then `@dataclass` for the ergonomic case, then `typing.Protocol` — Python's structural typing, the closest thing to Go's implicit interface satisfaction — and finally exceptions, which replace `(value, error)` returns entirely.

| Exercise | Topics | 📖 Official reading |
|---|---|---|
| [05_classes](exercises/stage2/05_classes/) | `__init__`, `__repr__`/`__eq__` (no free structural equality), class vs. instance attributes, composition | Tutorial: [Classes](https://docs.python.org/3/tutorial/classes.html) · Language Reference: [Data model](https://docs.python.org/3/reference/datamodel.html) (dunder methods) |
| [06_dataclasses](exercises/stage2/06_dataclasses/) | `@dataclass`, `frozen=True`, `@property`, mutating methods | Library: [`dataclasses`](https://docs.python.org/3/library/dataclasses.html) |
| [07_protocols](exercises/stage2/07_protocols/) | `typing.Protocol` structural typing, `__str__`, `isinstance` narrowing over `object` | Library: [`typing.Protocol`](https://docs.python.org/3/library/typing.html#typing.Protocol) · Glossary: [duck-typing](https://docs.python.org/3/glossary.html#term-duck-typing) |
| [08_exceptions](exercises/stage2/08_exceptions/) | Raising `ValueError`, custom exception classes, `raise ... from ...` chaining, a `retry()` helper | Tutorial: [Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html) · Library: [Built-in Exceptions](https://docs.python.org/3/library/exceptions.html) |

### 🔮 Stage 3 — Power features: generics, concurrency, boundaries

Python's answers to Go's headline features. Generics first (PEP 695's native `[T]` syntax), then concurrency in two steps — shared memory with `threading.Lock` (10), then `asyncio`'s cooperative, message-passing style via `Queue`/`gather` (11) — and finally JSON, where untyped outside data enters your typed world.

| Exercise | Topics | 📖 Official reading |
|---|---|---|
| [09_generics](exercises/stage3/09_generics/) | PEP 695 generic functions/classes (`def first[T](...)`, `class Stack[T]`), bounded type parameters | [PEP 695 — Type Parameter Syntax](https://peps.python.org/pep-0695/) · [What's New in Python 3.12](https://docs.python.org/3/whatsnew/3.12.html) (generic syntax section) |
| [10_threading](exercises/stage3/10_threading/) | `threading.Thread` + join-all, `threading.Lock`-guarded shared state, disjoint-index parallelism | Library: [`threading`](https://docs.python.org/3/library/threading.html) |
| [11_asyncio](exercises/stage3/11_asyncio/) | `asyncio.Queue` producer/consumer, `asyncio.gather` fan-in, `asyncio.wait_for` timeouts | Library: [Coroutines and Tasks](https://docs.python.org/3/library/asyncio-task.html) (`gather`, `wait_for`) · [Queues](https://docs.python.org/3/library/asyncio-queue.html) |
| [12_json](exercises/stage3/12_json/) | Dataclass ⇄ JSON via `json.dumps`/`json.loads`, `omitempty`-style filtering, unknown-shape JSON via `dict[str, Any]` | Library: [`json`](https://docs.python.org/3/library/json.html) |

> [!TIP]
> Work through the exercises **in order** — concepts are deliberately reused: mutability rules (03, 04) explain why frozen dataclasses matter (06), structural typing (07) is what makes the generic `Stack[T]` (09) easy to reason about, and the `Lock` discipline from threading (10) motivates why `asyncio` (11) sidesteps locks entirely by being single-threaded.

## 📏 Ground rules

- 🎨 **Run `ruff format`** — formatting is not a matter of taste. (`ruff format --check .` must print nothing.)
- 🔎 **Run `ruff check`** — catches unused imports, shadowing, and other lint issues.
- 🏷️ **Full type hints, checked with `mypy --strict`.** No untyped `def`s, no unannotated `Any`.
- 🔒 **Don't touch the `test_*.py` files.** They're the spec.
- 🚫 **No bare `except:`.** Catch specific exception types — swallowing everything hides bugs.

## 🙈 Solutions

Reference solutions live in [`solutions/`](./solutions), mirroring the exercise structure. **Spoilers!** Try the exercise, ask Claude for hints, and only then compare.

## 🗂️ Project layout

```
exercises/            ← your workspace: 12 exercises across 3 stages
solutions/             ← reference solutions (same layout, same tests)
CLAUDE.md              ← tutor instructions for Claude Code
Makefile               ← check-solutions / check-all / fmt / lint / typecheck
pyproject.toml         ← pytest / mypy / ruff configuration
requirements-dev.txt   ← pytest, mypy, ruff
```

---

<div align="center">

Made for learning. **Fork it, train with it, share it.** 🚀

Looking for the same course for Go or TypeScript? → [go-training](https://github.com/birsi/go-training) · [typescript-training](https://github.com/birsi/typescript-training)

</div>
