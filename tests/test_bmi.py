from backend.calculations import calculate_bmi

def test_calculate_bmi_normal():
    # 70kg, 175cm → BMI ≈ 22.86
    assert calculate_bmi(70, 175) == 22.86


def test_calculate_bmi_tall_person():
    # 80kg, 200cm → BMI = 20.0
    assert calculate_bmi(80, 200) == 20.0
