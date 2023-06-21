class Solution:
  def fib(self, n: int) -> int:
    acc = {}
    acc[0] = 0
    acc[1] = 1

    return self.helper(n, acc)

  def helper(self, n, acc):
    if n not in acc:
      acc[n] = self.helper(n - 1, acc) + self.helper(n - 2, acc)

    return acc[n]
