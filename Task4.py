def maxProfit(prices):
    min_price = float('inf')  # Начинаем с очень большого числа
    max_profit = 0

    for price in prices:
        # Обновляем минимальную цену, если нашли меньшую
        if price < min_price:
            min_price = price
        # Рассчитываем потенциальную прибыль и обновляем максимальную
        else:
            profit = price - min_price
            if profit > max_profit:
                max_profit = profit

    return max_profit


# Проверка на примере
prices = [7, 5, 6, 2, 4]
print(f"Максимальная прибыль: {maxProfit(prices)}")