import pytest

from src.taxes import calculate_tax


@pytest.mark.parametrize('price, tax_rate, discount, expected', [
    (100, 10, 20, 88),
    (200, 20, 30, 168),
    (300, 30, 40, 234)
])
def test_calculate_tax_with_discount(price, tax_rate, discount, expected):
    assert calculate_tax(price, tax_rate, discount) == expected


def test_calculate_tax_without_discount():
    assert calculate_tax(price=100, tax_rate=10) == 110


def test_calculate_tax_invalid_prices():
    with pytest.raises(ValueError):
        calculate_tax(price=-20, tax_rate=10)


def test_calculate_tax_invalid_discount():
    with pytest.raises(ValueError):
        calculate_tax(price=-20, tax_rate=10, discount=-10)


def test_calculate_tax_valid_tax_rate():
    with pytest.raises(ValueError):
        calculate_tax(price=10, tax_rate=-10)
