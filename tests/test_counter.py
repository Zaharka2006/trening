import pytest

from src.counter import calculate_taxes


@pytest.mark.parametrize('tax_rate, expected', [
    (10, [110, 220, 330]),
    (15, [115, 230, 345]),
    (20, [120, 240, 360])
])
def test_calculate_taxes(prices, tax_rate, expected):
    assert calculate_taxes(prices, tax_rate) == expected


def test_calculate_taxes_invalid_tax_rate(prices):
    with pytest.raises(ValueError):
        calculate_taxes(prices, -1)


def test_calculate_taxes_invalid_prices():
    with pytest.raises(ValueError):
        calculate_taxes([0, -1, 100], 0)
