# ============================================================
# Stage 3 — Exercise 12: JSON
# ============================================================
#
# GOAL: Dataclass <-> JSON via json.dumps/json.loads, omitempty-style
# filtering, and handling unknown JSON shapes.
#
# Rules:
#   - Don't modify test_serialization.py — it's the test suite.
#   - Check: pytest exercises/stage3/12_json/
#     (functions fail with AttributeError until every task is done —
#     that's your to-do list)
#
# When you're done, ask Claude to review this exercise.
# ============================================================

# --- Task 12.1 ---------------------------------------------------
# Write @dataclass class User: with fields id: int, name: str,
# email: str | None = None. Then write def to_json(user: User) -> str:
# using json.dumps(dataclasses.asdict(user)).
#
# WHY: dataclasses.asdict walks a dataclass instance into a plain dict,
# which json.dumps already knows how to serialize — no manual field-by-
# field marshaling needed, unlike Go's struct tags.

# TODO: your code here

# --- Task 12.2 ---------------------------------------------------
# Write def to_json_compact(user: User) -> str: — like to_json but
# OMITS keys whose value is None.
#
# WHY: mirrors Go's omitempty struct tag — Python's json.dumps has no
# built-in "omit None fields" behavior; you filter the dict yourself
# before dumping.

# TODO: your code here

# --- Task 12.3 ---------------------------------------------------
# Write def from_json(data: str) -> User: that parses a JSON string
# back into a User via json.loads + User(**parsed).
#
# WHY: unlike Go's json.Unmarshal into a pointer, Python just parses to
# a dict and you spread it into the constructor — the dataclass's
# __init__ does the field assignment.

# TODO: your code here

# --- Task 12.4 ---------------------------------------------------
# Write def extract_field(data: str, field: str) -> object | None: that
# parses data as JSON; if the top-level result is a dict, returns
# .get(field) (which is None if the key is absent); if the top-level
# result is NOT a dict (e.g. a list or scalar), returns None instead of
# raising.
#
# WHY: mirrors Go's map[string]any for handling JSON of unknown/dynamic
# shape — json.loads on a JSON object already returns a plain
# dict[str, Any], so no special unmarshal step is needed; you just have
# to guard against the top level not being an object at all.

# TODO: your code here

# --- Task 12.5 ---------------------------------------------------
# Write class DateTimeEncoder(json.JSONEncoder): overriding
# def default(self, o: object) -> object: — if isinstance(o, datetime)
# return o.isoformat(), else return super().default(o). Then write
# def dump_with_datetime(data: dict[str, Any]) -> str: using
# json.dumps(data, cls=DateTimeEncoder).
#
# WHY: mirrors Go's custom MarshalJSON method — the stdlib json module
# doesn't know how to serialize arbitrary types like datetime;
# subclassing JSONEncoder and overriding default() is the escape hatch.

# TODO: your code here
