
from train_fare import base_fare, concession, tatkal_charge


def test_base_fare_class_branches():
    assert base_fare("SL", 100) == 100
    assert base_fare("3A", 100) == 200
    assert base_fare("2A", 100) == 300
    assert base_fare("1A", 100) == 500


def test_base_fare_invalid_class_branch():
    try:
        base_fare("CC", 100)
        assert False
    except ValueError:
        pass


def test_base_fare_distance_branches():
    for distance in [0, -1]:
        try:
            base_fare("SL", distance)
            assert False
        except ValueError:
            pass
    assert base_fare("SL", 10) == 50
    assert base_fare("SL", 100) == 100


def test_concession_tatkal_branch():
    assert concession(4, "F", True) == 0
    assert concession(30, "M", False) == 0


def test_concession_age_branches():
    assert concession(4, "M", False) == 100
    assert concession(5, "F", False) == 50
    assert concession(12, "M", False) == 50
    assert concession(13, "M", False) == 0
    assert concession(59, "F", False) == 0


def test_concession_senior_gender_branches():
    assert concession(60, "F", False) == 50
    assert concession(60, "M", False) == 40


def test_tatkal_sleeper_branches():
    assert tatkal_charge("SL", 500) == 100
    assert tatkal_charge("SL", 1500) == 150


def test_tatkal_other_class_branches():
    assert tatkal_charge("3A", 100) == 100
    assert tatkal_charge("3A", 500) == 150
    assert tatkal_charge("3A", 2000) == 400
