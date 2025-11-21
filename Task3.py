def getRow(rowIndex):
    row = [1]

    for i in range(1, rowIndex + 1):
        # Создаем новую строку на основе предыдущей
        new_row = [1]  # Первый элемент всегда 1

        # Заполняем средние элементы
        for j in range(1, i):
            new_row.append(row[j - 1] + row[j])

        new_row.append(1)  # Последний элемент всегда 1
        row = new_row

    return row


# Пример использования
print(getRow(int(input())))