# 56. Merge Intervals
## Решение 1 (Придумал сам)
Сложность O(n * log(n)) + O(1)

- Сортируем массив интервалов по возрастанию (чтобы потенциальные пересечения находились рядом)
- инициализируем коллекцию под объединенные интервалы
- Идем в цикле по массиву интервалов, если последний интервал в массиве объединений пересекается с текущим то их нужно смержить изменив последний элемент в массиве объединений
- если они не пересекаются то просто добавляем в массив смерженных интервалов исходный интервал.
