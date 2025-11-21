def climb_stairs(n):
    # Базовые случаи
    if n == 1:
        return 1
    if n == 2:
        return 2

    # Инициализация для n >= 3
    dp = [0] * (n + 1)
    dp[1] = 1  # только 1 способ: (1)
    dp[2] = 2  # 2 способа: (1,1) или (2)

    # Заполняем массив для ступенек от 3 до n
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


# Получаем входные данные
n = int(input().strip())
# Выводим результат
print(climb_stairs(n))