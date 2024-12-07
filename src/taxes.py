def calculate_tax(price: float , tax_rate: float) -> float:
    """ Эта функция рассчитывает стоимость товара с учётом указанного налога """

    if tax_rate < 0:
        raise ValueError('Неверный налоговый процент')

    if price <= 0:
        raise ValueError('Неверная цена')

    final_price = price + (price / 100 * tax_rate)

    return final_price
