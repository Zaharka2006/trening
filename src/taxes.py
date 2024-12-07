def calculate_tax(prices: list[float], tax_rate) -> list[float]:
    """ Эта функция рассчитывает стоимость товара с учётом указанного налога """
    final_prices = []

    if tax_rate < 0:
        raise ValueError('Неверный налоговый процент')

    for item in prices:
        if item <= 0:
            raise ValueError('Неверная цена')

        tax = item / 100 * tax_rate
        final_price = item + tax
        final_prices.append(final_price)

    return final_prices
