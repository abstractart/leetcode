# 121. Best Time to Buy and Sell Stock
## Bruteforce
Сложность: O(n^2)

Итерируемся в два вложенных цикла и сравниваем все возможные пары значений (покупка, продажа) и ищем максимальное

## Two pointers
Сложность: O(n)
Объявляем 2 указателя: buy, sell

в цикле проверяем: если цена продажи меньше или равна цене покупки то переключаем buy = sell a sell = buy + 1
если иначе то пытаемся посчитать прибыль и сравнить с максимальной которую нашли на предыдыщих шагах
## DP
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/discuss/2060477/DPPython-My-bottom-up-DP-Thinking-Process
