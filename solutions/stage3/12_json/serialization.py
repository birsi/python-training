# ============================================================
# Stage 3 — Exercise 12: JSON — REFERENCE SOLUTION
# ============================================================

import dataclasses
import json
from dataclasses import dataclass
from datetime import datetime
from typing import Any

# --- Task 12.1 — User dataclass and to_json ---


@dataclass
class User:
    id: int
    name: str
    email: str | None = None


def to_json(user: User) -> str:
    return json.dumps(dataclasses.asdict(user))


# --- Task 12.2 — to_json_compact ---


def to_json_compact(user: User) -> str:
    data = {key: value for key, value in dataclasses.asdict(user).items() if value is not None}
    return json.dumps(data)


# --- Task 12.3 — from_json ---


def from_json(data: str) -> User:
    parsed = json.loads(data)
    return User(**parsed)


# --- Task 12.4 — extract_field ---


def extract_field(data: str, field: str) -> object | None:
    parsed = json.loads(data)
    if not isinstance(parsed, dict):
        return None
    return parsed.get(field)


# --- Task 12.5 — DateTimeEncoder and dump_with_datetime ---


class DateTimeEncoder(json.JSONEncoder):
    def default(self, o: object) -> object:
        if isinstance(o, datetime):
            return o.isoformat()
        return super().default(o)


def dump_with_datetime(data: dict[str, Any]) -> str:
    return json.dumps(data, cls=DateTimeEncoder)
