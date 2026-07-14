# ============================================================
# Tests — do not modify this file.
# When `pytest` passes, the exercise is solved.
# ============================================================
import json
from datetime import datetime

import serialization


def test_to_json() -> None:
    user = serialization.User(1, "Ada", "ada@example.com")
    assert json.loads(serialization.to_json(user)) == {
        "id": 1,
        "name": "Ada",
        "email": "ada@example.com",
    }


def test_to_json_compact_omits_none() -> None:
    user = serialization.User(2, "Bo")
    parsed = json.loads(serialization.to_json_compact(user))
    assert parsed == {"id": 2, "name": "Bo"}
    assert "email" not in parsed


def test_to_json_compact_keeps_present_email() -> None:
    user = serialization.User(1, "Ada", "a@x.com")
    assert json.loads(serialization.to_json_compact(user)) == {
        "id": 1,
        "name": "Ada",
        "email": "a@x.com",
    }


def test_from_json() -> None:
    assert serialization.from_json('{"id": 3, "name": "Cy", "email": null}') == (
        serialization.User(3, "Cy", None)
    )


def test_extract_field_present() -> None:
    assert serialization.extract_field('{"a": 1, "b": [1, 2]}', "b") == [1, 2]


def test_extract_field_missing() -> None:
    assert serialization.extract_field('{"a": 1}', "missing") is None


def test_extract_field_non_dict_top_level() -> None:
    assert serialization.extract_field("[1, 2, 3]", "a") is None


def test_dump_with_datetime() -> None:
    result = serialization.dump_with_datetime({"created": datetime(2026, 1, 1, 12, 0, 0)})
    assert json.loads(result) == {"created": "2026-01-01T12:00:00"}
