
from train_fare import base_fare, concession, tatkal_charge


def test_base_fare_all_classes():
    assert base_fare("SL", 500) == 500
    assert base_fare("3A", 100) == 200
    assert base_fare("2A", 100) == 300
    assert base_fare("1A", 100) == 500


def test_base_fare_minimum():
    assert base_fare("SL", 10) == 50
    assert base_fare("3A", 20) == 50


def test_base_fare_invalid_class():
    try:
        base_fare("CC", 100)
        assert False
    except ValueError as exc:
        assert str(exc) == "unknown class"


def test_base_fare_invalid_distance():
    for distance in (0, -10):
        try:
            base_fare("SL", distance)
            assert False
        except ValueError as exc:
            assert str(exc) == "invalid distance"


def test_concession_tatkal():
    assert concession(3, "F", True) == 0
    assert concession(70, "M", True) == 0


def test_concession_children():
    assert concession(4, "M", False) == 100
    assert concession(5, "F", False) == 50
    assert concession(12, "M", False) == 50


def test_concession_adults():
    assert concession(30, "M", False) == 0
    assert concession(59, "F", False) == 0


def test_concession_senior_citizens():
    assert concession(60, "F", False) == 50
    assert concession(65, "M", False) == 40


def test_tatkal_sleeper():
    assert tatkal_charge("SL", 500) == 100
    assert tatkal_charge("SL", 1500) == 150


def test_tatkal_other_classes():
    assert tatkal_charge("3A", 500) == 150
    assert tatkal_charge("2A", 1000) == 300


def test_tatkal_minimum_charge():
    assert tatkal_charge("3A", 100) == 100


def test_tatkal_maximum_charge():
    assert tatkal_charge("3A", 2000) == 400
    assert tatkal_charge("1A", 5000) == 400
