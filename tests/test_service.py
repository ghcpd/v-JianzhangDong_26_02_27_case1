from app.service import calculate_total, calculate_average, filter_high_value_orders


def test_total():
    assert calculate_total([100, 200, 300]) == 600


def test_average():
    assert calculate_average([100, 200, 300]) == 200


def test_filter():
    result = filter_high_value_orders([100, 2000, 3000])
    assert result == [2000, 3000]