from app.utils import validate_orders


def test_validate():
    data = ["100", "200", 300]
    result = validate_orders(data)
    assert result == [100.0, 200.0, 300.0]