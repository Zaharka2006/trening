def calculate_tax(price: float, tax_rate: float, discount: float = 0) -> float:
    """ Эта функция рассчитывает стоимость товара с учётом указанного налога """

    if tax_rate < 0:
        raise ValueError('Неверный налоговый процент')

    elif price < 0:
        raise ValueError('Неверная цена')

    elif discount < 0:
        raise ValueError('Неверная скидка')

    elif discount > 0:
        tax_price = price + (price / 100 * tax_rate)
        discount_price = tax_price - (tax_price / 100 * discount)
        return discount_price

    else:
        tax_price = price + (price / 100 * tax_rate)

    return tax_price
