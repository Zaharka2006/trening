import pytest

from src.taxes import calculate_tax


@pytest.mark.parametrize('price, tax_rate, expected', [
    (100, 10, 110),
    (200, 20, 240),
    (300, 30, 390)
])
def test_calculate_tax(price, tax_rate, expected):
    assert calculate_tax(price, tax_rate) == expected


def test_calculate_tax_invalid_prices():
    with pytest.raises(ValueError):
        calculate_tax(-20, 10)


def test_calculate_tax_valid_tax_rate():
    with pytest.raises(ValueError):
        calculate_tax(10, -10)