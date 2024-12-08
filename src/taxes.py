from typing import Union


def calculate_tax(price: Union[float, int], tax_rate: float, discount: float = 0, rounded: int = 2) -> float:
    """ Эта функция рассчитывает стоимость товара с учётом указанного налога """

    if tax_rate < 0:
        raise ValueError('Неверный налоговый процент')

    elif not isinstance(price, (float, int)):
        raise TypeError('Неверный формат цены')

    elif price < 0:
        raise ValueError('Неверная цена')

    elif discount < 0:
        raise ValueError('Неверная скидка')

    elif discount > 0:
        tax_price = price + (price / 100 * tax_rate)
        discount_price = tax_price - (tax_price / 100 * discount)
        return round(discount_price, rounded)

    else:
        tax_price = price + (price / 100 * tax_rate)

    return round(tax_price, rounded)
