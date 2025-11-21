def maxProfit(prices):
    max_profit = 0

    for i in range(1, len(prices)):
        # Если цена сегодня выше, чем вчера, добавляем разницу к прибыли
        if prices[i] > prices[i - 1]:
            max_profit += prices[i] - prices[i - 1]

    return max_profit

# Пример использования
prices = [3, 6, 2, 4, 7, 1]
result = maxProfit(prices)
print(f"Максимальная прибыль: {result}")