import pytest

from src.taxes import calculate_tax


@pytest.mark.parametrize('tax_rate, expected', [
    (10, [110, 220, 330]),
    (15, [115, 230, 345]),
    (20, [120, 240, 360])
])
def test_calculate_tax(prices, tax_rate, expected):
    assert calculate_tax(prices, tax_rate) == expected


def test_calculate_tax_invalid_prices():
    with pytest.raises(ValueError):
        calculate_tax([0, -23, 100], 10)


def test_calculate_tax_valid_tax_rate(prices):
    with pytest.raises(ValueError):
        calculate_tax(prices, -10)