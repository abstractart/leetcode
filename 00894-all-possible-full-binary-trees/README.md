# 894. All Possible Full Binary Trees

## Solution
Инвариант
```
n = 1 -> tree only with root
```
Соотношение
```
f(n) = [TreeNode(0, f(1), f(n - 1 - 1), TreeNode(0, f(3), f(n - 3 -1)), ..., TreeNode(0, f(n - 1 - 1), f(1))]
```
Кешируем повторяющиеся вычисления (варианты деревьев с количеством нод)
