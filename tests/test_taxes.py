import pytest

from src.taxes import calculate_tax


@pytest.mark.parametrize('price, tax_rate, discount, expected, rounded', [
    (100.5, 10, 20, 88.4, 1),
    (207.7, 20, 30, 174.47, 2),
    (321, 30, 40, 250, 0)
])
def test_calculate_tax_with_discount(price, tax_rate, discount, rounded, expected):
    assert calculate_tax(price, tax_rate, discount, rounded) == expected


def test_calculate_tax_without_discount():
    assert calculate_tax(price=100, tax_rate=10) == 110


def test_calculate_tax_invalid_prices():
    with pytest.raises(ValueError):
        calculate_tax(price=-20, tax_rate=10)


def test_calculate_tax_without_rounded():
    assert calculate_tax(price=57.98, tax_rate=15, discount=32) == 45.34


def test_calculate_tax_invalid_discount():
    with pytest.raises(ValueError):
        calculate_tax(price=-20, tax_rate=10, discount=-10)


def test_calculate_tax_valid_tax_rate():
    with pytest.raises(ValueError):
        calculate_tax(price=10, tax_rate=-10)


def test_calculate_tax_valid_type():
    with pytest.raises(TypeError):
        calculate_tax(price='a', tax_rate=10)
