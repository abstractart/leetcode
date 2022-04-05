# 94. Binary Tree Inorder Traversal
Решение 1 - рекурсия
Сложность: O(n) + O(n) на стек вызовов рекурсии

Решение 2 - итеративное + стэк

Алгоритм:
1. обьявляем указатель current и stack
2. объявляем цикл с условием (curr != None or len(stack) > 0) (есть непосещенные вершины)
  4. вложенный цикл, проверяем, существование current и наличие левого поддерева current 
    4. если есть то добавляем его в стэк
    5. присваиваем указателю current = current.left
5. таким образом у нас получается current == None и что в стеке значения лежат от меньшего к большему
6. достаем голову стэка если он не пуст (она будет являться минимумом среди всех непосещенных вершин)
7. обрабатываем её (выводим на экран, кладем в список итп)
8. переключаем указатель current = current.right
9 новый виток цикла(начинаем обрабывать левое поддерево вершины которая больше последней обработанной/является её потомком справа)

Решение 3 - morris traversal