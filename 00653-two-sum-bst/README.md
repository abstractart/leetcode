# 653. Two Sum IV - Input is a BST
## Решение 1 - InOrder traversal + BinarySearch
Complexity: O(n * log(n)) + O(n)
P.S
1. Поиск в бинарном дереве можно сделать без рекурсии и стэка за O(1)
```python3
def find(self, root, k):
    curr = root

    while(curr and curr.val != k):
        if k < curr.val:
            curr = curr.left
        else:
            curr = curr.right

    return curr
 ```
 2. Inorder traversal лучше делать через стэк а не рекурсию
InOrder traversal
## Решение 2 - InOrder Traversal + Hashmap
Complexity: O(n) + O(n)
## Решение 3 - InOrder + PostOrder
Complexity: O(n) + O(n)
