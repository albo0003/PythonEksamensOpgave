from backend.calculations import calorie_estimate

def test_calorie_estimate_basic():
    # 70 * 24 = 1680
    assert calorie_estimate(70) == 1680


def test_calorie_estimate_zero():
    assert calorie_estimate(0) == 0

