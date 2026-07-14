# ============================================================
# Tests — do not modify this file.
# When `pytest` passes, the exercise is solved.
# ============================================================
import classes


def test_distance_to() -> None:
    assert classes.Point(0, 0).distance_to(classes.Point(3, 4)) == 5.0


def test_point_eq() -> None:
    assert classes.Point(1, 2) == classes.Point(1, 2)
    assert classes.Point(1, 2) != classes.Point(1, 3)


def test_point_repr() -> None:
    assert repr(classes.Point(1, 2)) == "Point(x=1, y=2)"


def test_counter_class_and_instance_state() -> None:
    c1 = classes.Counter()
    c2 = classes.Counter()
    assert classes.Counter.total_created == 2
    c1.bump()
    c1.bump()
    c2.bump()
    assert c1.count == 2
    assert c2.count == 1
    assert classes.Counter.total_created == 2


def test_employee_summary() -> None:
    employee = classes.Employee("Ada", classes.Address("London", "W1"))
    assert employee.summary() == "Ada (London)"
